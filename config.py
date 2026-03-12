# ==================================================
# ZENTRALE BOT KONFIGURATION
# Nur tatsächlich verwendete Variablen
# ==================================================

class Config:

    # ==================================================
    # SYSTEM
    # ==================================================
    MODE = "BACKTEST"            # "BACKTEST" | "LIVE"
    AKTIV_ORDER = True           # Nur relevant im LIVE-Modus

    # ==================================================
    # DATENQUELLE
    # ==================================================
    BACKTEST_FILEPATH = "data/1-12_2025_5m_SOLUSDT.csv" 
    # workspace | 1-12_2023_5m_SOLUSDT | 1-12_2024_5m_SOLUSDT | 1-12_2025_5m_SOLUSDT | 1-2_2026_5m_SOLUSDT 
    # ==================================================
    # MARKT
    # ==================================================
    COIN = "SOL"                 # Basis-Asset
    USDT = "USDT"                # Quote-Asset
    SYMBOL = f"{COIN}/{USDT}"    # Handelssymbol
    TIMEFRAME = "5m"             # Candle Intervall
    MECHANIK = "swap"            # "swap" | "spot"

    ORDER_SIZE = 0.5             # Positionsgröße (Asset-Einheit)

    # ==================================================
    # WORKSPACE
    # ==================================================
    WINDOW_SIZE = 500            # Rolling Window Größe

    # ==================================================
    # ML / SIGNAL
    # ==================================================
    STRUCTURE_LOOKBACK = 50      # StructureGate Lookback
    ML_MIN_CONFIDENCE = 0.60     # Mindest ML Confidence

    # ==================================================
    # RISK MANAGEMENT
    # ==================================================
    RR = 2                        # Ziel Risk-Reward
    MIN_RR = 1                    # Minimal akzeptiertes RR
    MAX_RR = 5                    # für die MCM_AI
    RR_EXECUTION_MIN = 1.2        # RR unter 1.2 → kein echter Trade (Memory Trade / Learning only)
    MAX_SL_DISTANCE = 0.01        # Max erlaubte SL Distanz (%) - trade_value_gate.py
    MIN_TP_DISTANCE  = 0.80       # Min erlaubte TP Distanz (%) - trade_value_gate.py 
                                  # 0.8 sehr sauber | 0.5 sehr viele Trades
    # ==================================================
    # KOSTEN
    # ==================================================
    FEE_RATE = 0.0006            # Prozentuale Gebühr pro Seite
    FEE_PER_TRADE = 0.0          # Fixe Gebühr
    SLIPPAGE = 0.0005            # Slippage (nur Backtest)
    # energie basierter Slippage
    SOFT_HARD_SLP = 'soft'       # soft | extrem
    # soft simuliert:         extrem simuliert:
    #    normale Liquidität       hohe Volatilität
    #    normale Volatilität      dünnes Orderbuch
    #    realistische Börse       Liquiditätsstress   
    # ==================================================
    # EQUITY
    # ==================================================
    START_EQUITY = 100.0         # Startkapital Backtest

    # ==================================================
    # SYSTEM INTERNE PARAMETER (neu ergänzt)
    # ==================================================
    ML_MIN_WINDOW = 60           # Mindestkerzen für ML Prediction
    MONITOR_SLEEP_SEC = 10       # Order Monitor Loop Intervall
    IDLE_SYNC_SEC = 60           # Idle Sync Intervall
    PRICE_MATCH_TOL = 0.0001     # Preisvergleich Toleranz