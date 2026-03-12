# ==================================================
# bot.py
# entry folgt über struktur st_process / st_process nicht über gate
# ==================================================
from config import Config
from logging import DEBUG
from csv_feed import CSVFeed
from trade_stats import TradeStats
from bot_engine.exit_engine import ExitEngine
from bot_gates.trade_value_gate import TradeValueGate
from place_orders import place_order, consume_cancelled, get_active_order_snapshot, is_order_active
from debug_reader import dbr_debug

from collections import deque
from bot_gates.resonance_gate import ResonanceGate
from mcm_ai import MCMTradingDecision
from bot_gates.structure_entry_gate import StructureEntryGate

DEBUG = True
# --------------------------------------------------

class Bot:

    def __init__(self, filepath: str):
        self.feed = CSVFeed(filepath)
        self.exit_engine = ExitEngine()
        self.value_gate = TradeValueGate()
        self.stats = TradeStats(
            path="debug/trade_stats.json",
            csv_path="debug/trade_equity.csv",
            reset=True
        )

        self.resonance_gate = ResonanceGate()        
        self.structure_gate = StructureEntryGate()          
        self.mcm_ai = MCMTradingDecision()
        self.memory = self.mcm_ai.ai.memory

        self.prev_structure_type = None

        self.asym_history = deque(maxlen=3) # ---- asym_history prüfung

        # --------------------------------------------------
        # NEW: STRUCTURE GATE + ZONE STATE (NORMAL BOT)
        # --------------------------------------------------

        self.position = None
        self.pending_entry = None
        self.processed = 0
        self.current_timestamp = None

        snapshot = get_active_order_snapshot()

        if snapshot:
            print("RESTART RECOVERY → ACTIVE ORDER FOUND")

            entry = float(snapshot["entry"])
            sl = float(snapshot["sl"])
            risk = abs(entry - sl)

            self.position = {
                "side": snapshot["side"],
                "entry": entry,
                "tp": float(snapshot["tp"]),
                "sl": sl,
                "mfe": 0.0,
                "mae": 0.0,
                "risk": risk,
                "order_id": snapshot.get("id"),
                "entry_ts": snapshot.get("entry_ts"),
                "last_checked_ts": snapshot.get("entry_ts"),
                "meta": {},
            }

    # ==================================================
    # INTERNE PIPELINE (NUR WINDOW → LOGIK)
    # ==================================================
    def _process_window(self, window):

        # --------------------------------------------------
        # Restart Recovery → Timestamp initialisieren
        # --------------------------------------------------
        if self.position and self.position.get("entry_ts") is None:
            ts = window[-1].get("timestamp")
            self.position["entry_ts"] = ts
            self.position["last_checked_ts"] = ts

        # ------------------------
        # LIVE / BACKTEST Modus prüfen
        # ------------------------
        live_mode = str(getattr(Config, "MODE", "LIVE")).upper() == "LIVE"
        if live_mode and self.position is None:
            if is_order_active():
                if DEBUG:
                    dbr_debug("EXIT: ORDER_ACTIVE_BLOCK", "live_backtest_debug.txt")
                return

        # --------------------------------------------------
        # Resonance Gate - resonante Marktphasen dürfen Struktur prüfen.
        # --------------------------------------------------
        res = self.resonance_gate.process(window)

        if res is None:
            return

        if not res.get("allow", False):
            return

        self.current_timestamp = window[-1].get("timestamp")
        self.stats.data["current_timestamp"] = self.current_timestamp
        self.stats._save()

        res["timestamp"] = window[-1].get("timestamp")

        asym = float(res.get("asymmetry", 0.0))
        self.asym_history.append(asym)

        # ------------------------
        # EXIT (immer zuerst)
        # ------------------------
        if self.position is not None:

            last = window[-1]

            # --------------------------------------------------
            # MCM EPISODE STEP
            # --------------------------------------------------
            try:

                if res:

                    state = {
                        "energy": float(res.get("energy", 0.0)),
                        "coherence": float(res.get("coherence", 0.0)),
                        "asymmetry": int(res.get("asymmetry", 0)),
                        "resonance": float(res.get("resonance", 0.0)),
                        "coh_zone": float(res.get("coh_zone", 0.0)),
                        "side": self.position.get("side"),
                        "timestamp": last.get("timestamp"),
                    }

                    self.memory.step_episode(state)

            except Exception:
                pass

            entry_price = float(self.position.get("entry", 0.0) or 0.0)
            side = str(self.position.get("side", "")).upper().strip()

            self.current_timestamp = window[-1]["timestamp"]

            high = float(last["high"])
            low = float(last["low"])

            if side == "LONG":
                favorable = max(0.0, high - entry_price)
                adverse = max(0.0, entry_price - low)
            else:
                favorable = max(0.0, entry_price - low)
                adverse = max(0.0, high - entry_price)

            self.position["mfe"] = max(float(self.position.get("mfe", 0.0) or 0.0), favorable)
            self.position["mae"] = max(float(self.position.get("mae", 0.0) or 0.0), adverse)
                            
            exit_signal = self.exit_engine.process(
                window,
                self.position,
                "trading_debug.txt"
            )
            if exit_signal is None:
                return

            reason = exit_signal.get("reason")
            if reason is None:
                return

            # LIVE: Cancel-Override (Order wurde gecancelt bevor Fill)
            if live_mode and Config.AKTIV_ORDER:
                oid = self.position.get("order_id")
                if oid is not None and consume_cancelled(oid):
                    self.stats.on_cancel(order_id=oid, cause="exchange_cancel")
                    self.position = None
                    return

            meta = self.position.get("meta", {})
            ai = meta.get("mcm_ai", {})

            self.stats.on_exit(
                entry=self.position.get("entry"),
                tp=self.position.get("tp"),
                sl=self.position.get("sl"),
                reason=reason,
                side=self.position.get("side"),
                amount=Config.ORDER_SIZE if live_mode else 1.0,
            )

            if DEBUG:
                dbr_debug(
                    f"AI_DECISION | ml={ai.get('ml_side')} ai={ai.get('ai_side')} "
                    f"rr={ai.get('rr_target')} stim={ai.get('stimulus')} "
                    f"attr={ai.get('attractor')} eff={ai.get('efficiency')} "
                    f"node={ai.get('memory_node_id')} mem={ai.get('memory_attractor')}",
                    "trading_debug.txt"
                )

            try:

                outcome = None

                if reason == "tp_hit":
                    outcome = "tp"

                if reason == "sl_hit":
                    outcome = "sl"

                if outcome is not None:

                    energy = None

                    meta = self.position.get("meta") or {}

                    ai_state = meta.get("mcm_ai") or {}

                    energy = ai_state.get("energy")

                    if energy is not None:

                        rr = 0.0

                        entry = float(self.position.get("entry"))
                        tp = float(self.position.get("tp"))
                        sl = float(self.position.get("sl"))

                        risk = abs(entry - sl)

                        if risk > 0:
                            rr = abs(tp - entry) / risk

                        structure = self.position.get("meta", {}).get("structure", {})
                        structure_type = structure.get("structure_type")

                        self.memory.update_reward(
                            float(energy),
                            outcome,
                            self.position.get("side"),
                            rr,
                            structure_type,
                            float(ai_state.get("entry_shift", 0.0) or 0.0)
                        )

            except Exception:
                pass

            self.position = None
            return

        # ------------------------------------------------------------------------
        # Pending Entry Fill prüfen WICHTIG! für (BACKTEST)
        # nicht aktiv in LIVE Mode
        # ------------------------------------------------------------------------
        if (not live_mode) and self.pending_entry is not None and self.position is None:

            side = self.pending_entry["side"]
            entry_price = self.pending_entry["entry"]
            created = self.pending_entry["created_index"]
            max_wait = self.pending_entry["max_wait_bars"]

            last = window[-1]

            filled = False

            if side == "LONG" and last["low"] <= entry_price: 
                filled = True

            if side == "SHORT" and last["high"] >= entry_price:
                filled = True

            if filled:
                risk = abs(entry_price - self.pending_entry["sl"])
                self.position = {
                    "side": side,
                    "entry": entry_price,
                    "tp": self.pending_entry["tp"],
                    "sl": self.pending_entry["sl"],
                    "mfe": 0.0,
                    "mae": 0.0,
                    "risk": float(risk),
                    "order_id": None,
                    "entry_ts": window[-1].get("timestamp"),
                    "last_checked_ts": window[-1].get("timestamp"),
                    "meta": {},
                }
                self.pending_entry = None
                return

            if (self.processed - created) > max_wait:
                self.stats.on_cancel(order_id=None, cause="backtest_timeout")
                self.pending_entry = None
                return

            # Pending bleibt aktiv → kein neuer Entry in derselben Candle
            return

         # ------------------------
        # ------------------------------------------------------------------------
        if self.position is None and self.pending_entry is None:

            # --------------------------------------------------
            # RESONANCE GATE
            # --------------------------------------------------
            if res is None:
                return

            # --------------------------------------------------
            # STRUCTURE ENTRY GATE
            # --------------------------------------------------
            structure_entry = self.structure_gate.process(
                window,
                self.prev_structure_type,
            )

            if structure_entry is None:
                return

            structure_type = structure_entry.get("structure_type")
            structure_strength = structure_entry.get("structure_strength")
            structure_age = structure_entry.get("structure_age")
            structure_range = structure_entry.get("structure_range")

            if structure_type not in ("HH", "HL", "LH", "LL"):
                return

            if structure_strength is None or structure_strength < 0.25:
                return

            if structure_age is None or structure_age > 20:
                return

            if structure_range is None or structure_range <= 0:
                return

            self.prev_structure_type = structure_type

            # --------------------------------------------------
            # DIRECTION ÜBER ASYMMETRY
            # --------------------------------------------------
            asymmetry = sum(self.asym_history) / len(self.asym_history)
            #asymmetry = float(res.get("asymmetry", 0.0))

            if asymmetry > 0:
                side = "LONG"
            elif asymmetry < 0:
                side = "SHORT"
            else:
                return

            if side == "LONG" and structure_type not in ("HH", "HL"):
                return
            if side == "SHORT" and structure_type not in ("LH", "LL"):
                return
            # --------------------
            # Pullback Funktion
            # --------------------
            last_close = float(structure_entry.get("entry_price"))            
            structure_range = float(structure_entry.get("structure_range") or 0.0)
            structure_strength = float(structure_entry.get("structure_strength") or 0.0)
            structure_age = float(structure_entry.get("structure_age") or 0.0)

            if structure_range <= 0:
                return

            pullback_factor = (
                0.50
                - 0.18 * min(abs(float(res.get("coherence", 0.0))), 1.0)
                - 0.12 * min(max(float(res.get("energy", 0.0)) / 2.0, 0.0), 1.0)
                - 0.10 * min(max(structure_strength, 0.0), 1.0)
                + 0.08 * min(max(structure_age / 20.0, 0.0), 1.0)
            )

            pullback_factor = max(0.18, min(0.62, pullback_factor))

            if side == "LONG":
                entry_price = last_close - (structure_range * pullback_factor)

            elif side == "SHORT":
                entry_price = last_close + (structure_range * pullback_factor)

            else:
                return

            # --------------------------------------------------
            # RISK / RR berechnet risk
            # --------------------------------------------------
            energy = float(res.get("energy", 0.0))
            base_risk_pct = float(getattr(Config, "ML_RISK_PCT", 0.01))
            energy_scale = max(0.1, min(abs(energy) / 2.0, 1.0))
            risk = entry_price * base_risk_pct * energy_scale

            if side == "LONG":
                sl_price = entry_price - risk
            elif side == "SHORT":
                sl_price = entry_price + risk
            else:
                return

            risk = abs(entry_price - sl_price)

            # --------------------------------------------------
            # PRE-AI STATE übergabe an MCM_AI
            # --------------------------------------------------
            trade_state = {
                **res,
                **structure_entry,

                "side": side,

                "energy": float(res.get("energy", 0.0)),
                "coherence": float(res.get("coherence", 0.0)),
                "asymmetry": float(res.get("asymmetry", 0.0)),
                "resonance": float(res.get("resonance", 0.0)),
                "coh_zone": float(res.get("coh_zone", 0.0)),

                "structure_break": structure_entry.get("structure_break"),

                "risk": float(risk),
                "rr": float(getattr(Config, "RR", 2.0)),

                "sl_price": float(sl_price),
                "tp_price": None,
            }

            # --------------------------------------------------
            # MCM_AI DECISION
            # --------------------------------------------------
            ai_decision = self.mcm_ai.decide(
                ml_side=side,
                structure=trade_state,
            )

            if not ai_decision.get("allow", False):
                return

            side = ai_decision.get("ai_side", side)

            adaptive_rr = float(ai_decision.get("rr_target", Config.RR))

            # --------------------------------------------------
            # AI ENTRY REFINEMENT
            # --------------------------------------------------

            entry_ai = ai_decision.get("entry_ai")

            if entry_ai is not None:

                entry_ai = float(entry_ai)

                if side == "LONG" and entry_ai <= entry_price:

                    shift = entry_price - entry_ai
                    entry_price = entry_ai
                    sl_price = sl_price - shift

                elif side == "SHORT" and entry_ai >= entry_price:

                    shift = entry_ai - entry_price
                    entry_price = entry_ai
                    sl_price = sl_price + shift

                risk = abs(entry_price - sl_price)
                
            entry_shift = 0.0
            structure_entry_price = float(structure_entry.get("entry_price") or 0.0)

            if structure_entry_price > 0.0:

                if side == "LONG":
                    entry_shift = max(0.0, structure_entry_price - entry_price)

                elif side == "SHORT":
                    entry_shift = max(0.0, entry_price - structure_entry_price)

            # --------------------------------------------------
            # TP BERECHNEN
            # --------------------------------------------------
            if side == "LONG":
                tp_price = entry_price + (risk * adaptive_rr)
            elif side == "SHORT":
                tp_price = entry_price - (risk * adaptive_rr)
            else:
                return

            rr_value = abs(tp_price - entry_price) / risk

            trade_state["tp_price"] = float(tp_price)
            trade_state["rr"] = float(rr_value)

            # --------------------------------------------------
            # Ökonomische Prüfung (RR / Mindestabstand)
            # --------------------------------------------------
            entry_result = {
                "decision": side,
                "entry_price": entry_price,
                "tp_price": tp_price,
                "sl_price": sl_price,
            }

            value_check = self.value_gate.evaluate(entry_result)

            if DEBUG:
                dbr_debug(f"VALUE_GATE: {value_check}", "value_check_debug.txt")

            if not value_check.get("trade_allowed", False):
                return

            # --------------------------------------------------
            # Slippage mit Energy koppelung. (nur Backtest !!)
            # Funktion um an realistischen Trade-Verhalten zu kommen
            # --------------------------------------------------
            base_slip = float(getattr(Config, "SLIPPAGE", 0.0) or 0.0)
            energy = float(res.get("energy", 0.0))

            # Energy-abhängige Slippage
            if Config.SOFT_HARD_SLP == ('soft'):
                slip = base_slip * (1.0 + abs(energy)) # soft
            else:
                slip = base_slip * (1 + 0.5*abs(energy) + 0.5*energy*energy) # extrem

            if DEBUG:
                dbr_debug(f"Slippage: {slip} - Energy-abhängige Slippage", "slippage_debug.txt")

            if slip > 0.0 and Config.MODE == "BACKTEST":

                if side == "LONG":
                    entry_price = entry_price * (1 + slip)

                    if Config.SOFT_HARD_SLP == 'extrem':
                        tp_price = tp_price * (1 - slip)
                        sl_price = sl_price * (1 - slip)

                elif side == "SHORT":
                    entry_price = entry_price * (1 - slip)

                    if Config.SOFT_HARD_SLP == 'extrem':
                        tp_price = tp_price * (1 + slip)
                        sl_price = sl_price * (1 + slip)

            order_side = "sell" if side == "SHORT" else "buy"

            # --------------------------------------------------
            # RR Execution Filter (LIVE)
            # Drawdown sinkt
            # Memory bleibt aktiv
            # RR kann wieder steigen
            # --------------------------------------------------
            order_id = None
            is_memory_trade = False
            rr_exec_min = float(getattr(Config, "RR_EXECUTION_MIN", 1.2))

            if live_mode and Config.AKTIV_ORDER and rr_value < rr_exec_min:
                is_memory_trade = True

            # --------------------------------------------------
            # Exchange Order (LIVE)
            # --------------------------------------------------
            if live_mode and Config.AKTIV_ORDER and not is_memory_trade:
                order_id = place_order(
                    order_type=order_side,
                    price=entry_price,
                    amount=Config.ORDER_SIZE,
                    open_orders=None,
                    tp=tp_price,
                    sl=sl_price,
                )

                if order_id is None:
                    return
                
        # --------------------------------------------------
        # Interne Position setzen
        # --------------------------------------------------
        risk_final = abs(entry_price - sl_price)

        last = window[-1]

        # --------------------------------------------------
        # MCM EPISODE START
        # --------------------------------------------------
        try:

            state = {
                "energy": float(res.get("energy", 0.0)),
                "coherence": float(res.get("coherence", 0.0)),
                "asymmetry": int(res.get("asymmetry", 0)),
                "resonance": float(res.get("resonance", 0.0)),
                "coh_zone": float(res.get("coh_zone", 0.0)),

                "structure_type": structure_entry.get("structure_type"),
                "structure_strength": structure_entry.get("structure_strength"),
                "structure_age": structure_entry.get("structure_age"),

                "side": side,
                "timestamp": last.get("timestamp"),
            }

            self.memory.start_episode(state)

        except Exception:
            pass

        self.position = {
            "side": side,
            "entry": entry_price,
            "tp": tp_price,
            "sl": sl_price,
            "mfe": 0.0,
            "mae": 0.0,
            "risk": float(risk_final),
            "order_id": order_id,
            "entry_ts": last.get("timestamp"),
            "last_checked_ts": last.get("timestamp"),
            "meta": {
                "resonance": res.get("resonance"),
                "structure": structure_entry,
                "mcm_ai": {
                    **ai_decision,
                    "energy": res.get("energy"),
                    "rr": rr_value,
                    "entry_shift": entry_shift,
                    "entry_structure": structure_entry.get("entry_price"),                    
                },
            },
        }

        return
        
    # ==================================================
    # MODUS 1: ROW-MODUS (internes Rolling)
    # ==================================================
    def run_rows(self, window_size: int = 2, delay_seconds: float = 0.0):
        buffer = []
        self.processed = 0

        for row in self.feed.rows(delay_seconds=delay_seconds):
            buffer.append(row)

            if len(buffer) < window_size:
                continue

            if len(buffer) > window_size:
                buffer.pop(0)

            self._process_window(buffer)
            self.processed += 1

    # ==================================================
    # MODUS 2: WINDOW-MODUS (direkt vom Feed)
    # ==================================================
    def run_window(self, size: int, delay_seconds: float = 0.0):
        if not hasattr(self, "processed"):
            self.processed = 0

        processed = 0

        for window in self.feed.window(size, delay_seconds=delay_seconds):
            self._process_window(window)
            processed += 1
            self.processed += 1

        return processed
