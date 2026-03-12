from debug_reader import dbr_trade_debug
from datetime import datetime
import csv

class ExitEngine:
    # ─────────────────────────────────────────────
    # Exit
    # ─────────────────────────────────────────────
    def process(self, window, position: dict, txt):

        if not position:
            return None

        side = str(position.get("side")).upper().strip()

        entry = float(position.get("entry", 0.0))
        tp = float(position.get("tp", 0.0))
        sl = float(position.get("sl", 0.0))

        entry_ts = position.get("entry_ts")

        meta = position.get("meta") or {}
        ai_meta = meta.get("mcm_ai") or {}

        energy = ai_meta.get("energy")

        if tp is None or sl is None or entry is None:
            return None

        if not isinstance(entry_ts, (int, float)):
            return None
        
        # --------------------------------------------------
        # TRADE EXIT DEBUG
        # --------------------------------------------------
        def trade_debug_exit(position, reason, pnl, time_str, txt):

            side = str(position.get("side")).upper().strip()

            entry = float(position.get("entry", 0.0))
            tp = float(position.get("tp", 0.0))
            sl = float(position.get("sl", 0.0))

            mfe = float(position.get("mfe", 0.0))
            mae = float(position.get("mae", 0.0))
            risk = float(position.get("risk", 0.0))

            meta = position.get("meta") or {}
            ai_meta = meta.get("mcm_ai") or {}

            resonance = meta.get("resonance")

            energy = ai_meta.get("energy")
            stimulus = ai_meta.get("stimulus")
            attractor = ai_meta.get("attractor")
            efficiency = ai_meta.get("efficiency")
            node = ai_meta.get("memory_node_id")
            mem_attr = ai_meta.get("memory_attractor")

            dbr_trade_debug(
                f"EXIT {reason} | "
                f"time={time_str} "
                f"side={side} "
                f"entry={entry:.4f} "
                f"tp={tp:.4f} "
                f"sl={sl:.4f} "
                f"risk={risk:.4f} "
                f"mfe={mfe:.4f} "
                f"mae={mae:.4f} "
                f"energy={energy} "
                f"stim={stimulus} "
                f"attr={attractor} "
                f"eff={efficiency} "
                f"node={node} "
                f"mem={mem_attr} "
                f"res={resonance} "
                f"pnl={pnl:.4f}",
                txt
            )
        # --------------------------------------------------
        # Sliding Hit Search ab entry_ts
        # --------------------------------------------------
        for c in window:

            ts = c.get("timestamp")
            if not isinstance(ts, (int, float)):
                continue

            if ts < entry_ts:
                continue

            high = c["high"]
            low = c["low"]
            close = c["close"]

            time_str = "N/A"
            if ts > 0:
                try:
                    time_str = datetime.fromtimestamp(ts / 1000).strftime("%d/%m/%Y %H:%M")
                except Exception:
                    time_str = "N/A"

            # ─────────────────────────────────────────────
            # LONG
            # ─────────────────────────────────────────────
            if side == "LONG":

                if low <= sl and high >= tp:
                    pnl = sl - entry
                    trade_debug_exit(
                        position,
                         "SL (BOTH HIT)",
                        pnl,
                        time_str,
                        txt                        
                    )
                    return {"reason": "sl_hit"}

                if low <= sl:
                    pnl = sl - entry
                    trade_debug_exit(
                        position,
                        "SL",
                        pnl,
                        time_str,
                        txt
                    )
                    return {"reason": "sl_hit"}

                if high >= tp:
                    pnl = tp - entry
                    trade_debug_exit(
                        position,
                        "TP",
                        pnl,
                        time_str,
                        txt
                    )
                    return {"reason": "tp_hit"}

            # ─────────────────────────────────────────────
            # SHORT
            # ─────────────────────────────────────────────
            if side == "SHORT":

                if high >= sl and low <= tp:
                    pnl = entry - sl
                    trade_debug_exit(
                        position,
                        "SL (BOTH HIT)",
                        pnl,
                        time_str,
                        txt
                    )
                    return {"reason": "sl_hit"}

                if high >= sl:
                    pnl = entry - sl
                    trade_debug_exit(
                        position,
                        "SL",
                        pnl,
                        time_str,
                        txt
                    )
                    return {"reason": "sl_hit"}

                if low <= tp:
                    pnl = entry - tp
                    trade_debug_exit(
                        position,
                        "TP",
                        pnl,
                        time_str,
                        txt
                    )
                    return {"reason": "tp_hit"}

        return None