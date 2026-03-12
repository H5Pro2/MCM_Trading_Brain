# ==================================================
# bot.py
# CLEAN CORE
# Platzhalter für:
#   ResonanceGate
#   StructureEntryGate
#   MCM_AI
# --------------------------------------------------
# Architektur vorbereitet – Logik nicht implementiert
# ==================================================

from csv_feed import CSVFeed
from trade_stats import TradeStats
from bot_engine.exit_engine import ExitEngine
from bot_gates.trade_value_gate import TradeValueGate
from config import Config
from debug_reader import dbr_debug
from place_orders import (
    place_order,
    consume_cancelled,
    get_active_order_snapshot,
    is_order_active,
)

DEBUG = True

class Bot:

    # --------------------------------------------------
    # INIT
    # --------------------------------------------------
    def __init__(self, filepath: str):

        self.feed = CSVFeed(filepath)

        self.exit_engine = ExitEngine()
        self.value_gate = TradeValueGate()

        self.stats = TradeStats(
            path="debug/trade_stats.json",
            csv_path="debug/trade_equity.csv",
            reset=True,
        )

        # --------------------------------------------------
        # FUTURE MODULES (DEFAULT PLACEHOLDER)
        # --------------------------------------------------

        self.resonance_gate = None
        self.structure_gate = None
        self.mcm_ai = None
        self.memory = None

        # --------------------------------------------------

        self.position = None
        self.pending_entry = None
        self.processed = 0

        snapshot = get_active_order_snapshot()

        if snapshot:

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
    # WINDOW PROCESS
    # ==================================================
    def _process_window(self, window):

        # --------------------------------------------------
        # Restart Recovery Timestamp
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
                return

        # --------------------------------------------------
        # FUTURE PIPELINE HOOK
        # ResonanceGate
        # StructureEntryGate
        # MCM_AI
        # --------------------------------------------------

        side = None
        entry_price = None
        tp_price = None
        sl_price = None

        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        # VALUE GATE (Ökonomische Prüfung)
        # ------------------------------------------------------------------------------------------------------------------------------------------------------
        if side is not None:

            entry_result = {
                "decision": side,
                "entry_price": entry_price,
                "tp_price": tp_price,
                "sl_price": sl_price,
            }

            value_check = self.value_gate.evaluate(entry_result)

            if not value_check.get("trade_allowed", False):
                return
            # --------------------------------------------------
            # RR LIMITS
            # --------------------------------------------------
            RR_MIN = Config.MIN_RR
            RR_MAX = Config.MAX_RR

            adaptive_rr = max(RR_MIN, min(adaptive_rr, RR_MAX))

            risk = abs(entry_price - sl_price)

            if side == "LONG":
                tp_price = entry_price + (risk * adaptive_rr)

            if side == "SHORT":
                tp_price = entry_price - (risk * adaptive_rr)

            if DEBUG:
                dbr_debug(
                    f"side: {side} | tp_price={tp_price} | risk={risk * adaptive_rr}",
                    "entry_debug.txt"
                )
            # --------------------------------------------------
            # Slippage (nur Backtest)
            # --------------------------------------------------
            slip = float(getattr(Config, "SLIPPAGE", 0.0) or 0.0)

            if slip > 0.0 and Config.MODE == "BACKTEST":
                if side == "LONG":
                    entry_price = entry_price * (1 + slip)
                    tp_price = tp_price * (1 - slip)
                    sl_price = sl_price * (1 - slip)
                else:
                    entry_price = entry_price * (1 - slip)
                    tp_price = tp_price * (1 + slip)
                    sl_price = sl_price * (1 + slip)

            order_side = "sell" if side == "SHORT" else "buy"
            # --------------------------------------------------
            # Exchange Order (LIVE)
            # --------------------------------------------------
            order_id = None            

            if live_mode and Config.AKTIV_ORDER:
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
        # EXIT ENGINE
        # --------------------------------------------------
        if self.position is not None:

            last = window[-1]

            entry_price = float(self.position.get("entry", 0.0) or 0.0)
            side = str(self.position.get("side", "")).upper().strip()

            high = float(last["high"])
            low = float(last["low"])

            if side == "LONG":

                favorable = max(0.0, high - entry_price)
                adverse = max(0.0, entry_price - low)

            else:

                favorable = max(0.0, entry_price - low)
                adverse = max(0.0, high - entry_price)

            self.position["mfe"] = max(
                float(self.position.get("mfe", 0.0) or 0.0),
                favorable,
            )

            self.position["mae"] = max(
                float(self.position.get("mae", 0.0) or 0.0),
                adverse,
            )

            exit_signal = self.exit_engine.process(
                window,
                self.position,
                "trading_debug.txt",
            )

            if exit_signal is None:
                return

            reason = exit_signal.get("reason")

            if reason is None:
                return

            # --------------------------------------------------
            # LIVE CANCEL CHECK
            # --------------------------------------------------
            if live_mode and Config.AKTIV_ORDER:

                oid = self.position.get("order_id")

                if oid is not None and consume_cancelled(oid):

                    self.stats.on_cancel(
                        order_id=oid,
                        cause="exchange_cancel",
                    )

                    self.position = None

                    return

            # --------------------------------------------------
            # TRADE STATS
            # --------------------------------------------------
            self.stats.on_exit(
                entry=self.position.get("entry"),
                tp=self.position.get("tp"),
                sl=self.position.get("sl"),
                reason=reason,
                side=self.position.get("side"),
                amount=Config.ORDER_SIZE if live_mode else 1.0,
            )

            self.position = None

            return


    # ==================================================
    # ROW MODE
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
    # WINDOW MODE
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
