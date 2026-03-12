# MCM Trading System  
Mental Core Matrix – Market Energy Model

## Overview

This project implements a trading system based on the **Mental Core Matrix (MCM)** — a conceptual model I developed to describe dynamic decision processes in complex systems.

The MCM was **not originally designed for financial markets**.  
Instead, the trading system presented here is a **conceptual application of the MCM model to market dynamics**.

Financial markets are well suited for this application because they represent a complex system where countless participants continuously interact, forming emergent patterns of collective decision making.

This project explores the idea that **market charts represent energetic structures of collective behavior**, rather than simple sequences of prices.

---

# Core Idea

Traditional trading systems interpret market data primarily as numerical price series.

Indicators such as:

- RSI
- Moving averages
- MACD

are derived from these price values.

In this project a different perspective is used.

A market chart is interpreted as the **result of collective psychological interaction between market participants**.

Every price movement is the result of:

- expectations
- fear
- risk management
- reaction to information
- liquidity dynamics

From this perspective a chart can be seen as a **psychodynamic pattern of collective decision making**.

The goal of the system is therefore not to analyze prices directly, but to **model the energetic structure behind market movement**.

---

# Candles as Energy Surfaces

A standard OHLC candle contains four values:

- Open
- High
- Low
- Close

In this system a candle is interpreted as an **energy surface within the market tension field**.

The energetic characteristics of a candle are derived from:

- the range between High and Low
- the position of Open and Close
- the structural context of the candle
- the speed and direction of movement

This allows each candle to be interpreted as a **small energetic unit inside the global market system**.

Strong movements create higher energetic tension, while quiet market phases contain lower energy.

---

# Market Energy Representation

The raw candle data is transformed into a set of **state variables** that describe the energetic structure of the market.

These variables are computed in:

`mcm_core_engine.py`

```python
energy, coherence, asymmetry, coh_zone = compute_tension_from_ohlc(...)
```

:contentReference[oaicite:0]{index=0}

The resulting state parameters are:

| Variable | Meaning |
|--------|--------|
Energy | intensity of movement |
Coherence | directional consistency of price action |
Asymmetry | directional bias of the candle |
Cohesion Zone | market regime classification |

This transformation converts price data into an **energetic state representation of the market**.

---

# Trading Architecture

The trading system follows a structured pipeline.

```
OHLC Data
    ↓
compute_tension_from_ohlc
    ↓
Resonance Gate
    ↓
Structure Entry Gate
    ↓
Direction via Asymmetry
    ↓
Risk / RR Calculation
    ↓
MCM_AI Decision
    ↓
Trade Value Gate
    ↓
Order Execution
```

---

# Resonance Gate

The **Resonance Gate** filters market noise and detects valid market activity.

Implemented in:

```
resonance_gate.py
```

:contentReference[oaicite:1]{index=1}

It evaluates:

- resonance strength
- phase stability
- energy gradient
- short-term stability

Only if these conditions are met will the system allow structure analysis.

---

# Structure Entry Gate

The **StructureEntryGate** detects market structure patterns.

Implemented in:

```
structure_entry_gate.py
```

:contentReference[oaicite:2]{index=2}

Recognized structures include:

- Higher High (HH)
- Higher Low (HL)
- Lower High (LH)
- Lower Low (LL)

Additional metrics include:

- structure strength
- structure age
- structure break (BOS / CHOCH)

---

# Direction Determination

Trade direction is determined using **asymmetry smoothing**.

The system averages the last asymmetry values to determine directional bias.

```
asymmetry > 0 → LONG
asymmetry < 0 → SHORT
```

---

# Risk Model

Risk is calculated dynamically based on entry price and market energy.

```
risk = entry_price * risk_pct * energy_scale
```

Stop Loss is then derived from the entry price.

---

# MCM_AI

The **MCM_AI** represents the cognitive component of the system.

It receives the full market state including:

- energy
- coherence
- asymmetry
- resonance
- structure information
- risk parameters

The AI can:

- allow or block trades
- adjust entry position
- modify the risk-reward target
- learn from TP / SL outcomes

However, the AI **cannot worsen the structural entry**.

Example rule:

```
LONG:
entry_ai ≤ entry_structure

SHORT:
entry_ai ≥ entry_structure
```

---

# Trade Value Gate

Before a trade is executed it passes through the **TradeValueGate**.

This module verifies economic viability.

Implemented in:

```
trade_value_gate.py
```

Checks include:

- risk > 0
- reward > 0
- RR above minimum threshold
- stop loss distance within allowed range

---

# Backtesting Engine

The bot supports both:

```
BACKTEST mode
LIVE mode
```

Configuration is defined in:

```
config.py
```

:contentReference[oaicite:3]{index=3}

Backtesting uses historical OHLC data via a CSV feed.

```
csv_feed.py
```

:contentReference[oaicite:4]{index=4}

---

# Order Execution

Live order execution and monitoring are handled by:

```
place_orders.py
```

:contentReference[oaicite:5]{index=5}

Features include:

- order monitoring thread
- missed-TP detection
- reconnect handling
- restart synchronization

---

# Philosophy of the System

The architecture combines two different approaches:

**Rule-based structure**

- market structure
- resonance filters
- risk management

**Adaptive learning**

- MCM_AI evaluation
- memory of previous states
- reward feedback from TP / SL outcomes

This hybrid design allows the system to remain structurally stable while still adapting to evolving market conditions.

---

# Research Direction

This project explores the idea that markets can be modeled as **energetic systems of collective decision dynamics**.

By interpreting candles as energy surfaces and market movement as gradients of tension, the system attempts to analyze market behavior at a deeper structural level.

The trading bot therefore represents **one possible application of the Mental Core Matrix model** to financial markets.

---

# Disclaimer

This project is an experimental research implementation.

It should not be interpreted as financial advice.

Trading financial markets involves significant risk.