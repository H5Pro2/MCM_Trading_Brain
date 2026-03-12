# ==================================================
# trade_value_gate.py
# ==================================================
# MINIMAL TRADE VALUE GATE
#
# Prüft ausschließlich:
# 1) Struktur SL korrekt
# 2) Risk <= MAX_SL_PCT
# 3) RR >= MIN_RR
# 4) TP-Distanz >= Entry * TP_DISTANCE_TO_ENTRY
#
# Keine Richtungsentscheidung
# Keine TP/SL Berechnung
# ==================================================

from typing import Dict, Any
from config import Config


class TradeValueGate:

    # --------------------------------------------------
    # VALUE CHECK
    # --------------------------------------------------
    def evaluate(self, entry_result: Dict[str, Any]) -> Dict[str, Any]:

        decision = entry_result.get("decision")
        entry = entry_result.get("entry_price")
        tp = entry_result.get("tp_price")
        sl = entry_result.get("sl_price")

        # --------------------------------------------------
        # Basisprüfung
        # --------------------------------------------------
        if decision not in ("LONG", "SHORT"):
            return {"trade_allowed": False}

        if entry is None or tp is None or sl is None:
            return {"trade_allowed": False}

        entry = float(entry)
        tp = float(tp)
        sl = float(sl)

        if entry <= 0:
            return {"trade_allowed": False}

        # --------------------------------------------------
        # Struktur & Risk / Reward
        # --------------------------------------------------
        if decision == "LONG":

            if not sl < entry:
                return {"trade_allowed": False}

            risk = entry - sl
            reward = tp - entry

        else:  # SHORT

            if not entry < sl:
                return {"trade_allowed": False}

            risk = sl - entry
            reward = entry - tp

        if risk <= 0 or reward <= 0:
            return {"trade_allowed": False}

        # --------------------------------------------------
        # MAX SL DISTANZ
        # --------------------------------------------------
        max_sl_pct = float(getattr(Config, "MAX_SL_DISTANCE", 0.0) or 0.0)

        if max_sl_pct > 0:
            #if (risk / entry) > max_sl_pct:
            if abs(entry - sl) > (entry * max_sl_pct):
                return {"trade_allowed": False, "reason": "sl_distance_too_high"}
        # --------------------------------------------------
        # Mindest TP Distanz (Gebühren + Slippage Schutz)
        # --------------------------------------------------
        min_profit_distance = float(getattr(Config, "MIN_TP_DISTANCE", 0.0))

        profit_distance = abs(tp - entry)

        if profit_distance < (min_profit_distance * risk):
            return {"trade_allowed": False, "reason": "tp_distance_too_small"}
        # --------------------------------------------------
        # RR MINIMUM
        # --------------------------------------------------
        rr = reward / risk
        min_rr = float(getattr(Config, "MIN_RR", 0.0) or 0.0)

        if min_rr > 0:
            if rr < min_rr:
                return {"trade_allowed": False}

        # --------------------------------------------------
        # OK
        # --------------------------------------------------
        return {
            "trade_allowed": True,
            "risk": risk,
            "reward": reward,
            "rr": rr,
        }