"""
MCM Trading Bot - READ-ONLY Dashboard GUI
=========================================
Tkinter + Matplotlib | Dark Mode | Drei-Ebenen-Architektur
Außenwelt / Innenwelt / Entwicklung & Memory

Datenquellen:
  - debug/trade_stats.json
  - debug/trade_equity.csv
  - bot_memory/memory_state.json
  - debug/bot_visual_snapshot.json
  - debug/bot_inner_snapshot.json

Ausführung: python mcm_gui.py
Optional:   python mcm_gui.py --base /pfad/zum/bot
"""

import tkinter as tk
from tkinter import ttk, font as tkfont
import json
import csv
import os
import sys
import time
import threading
import argparse
from pathlib import Path
from datetime import datetime
from config import Config

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.patches import FancyArrowPatch
import matplotlib.gridspec as gridspec
import numpy as np

# ─────────────────────────────────────────────
#  KONFIGURATION
# ─────────────────────────────────────────────
REFRESH_MS   = 1000          # Refresh-Intervall in ms
CANDLE_COUNT = 60            # Anzahl Candles im Chart

# Basis-Pfad (überschreibbar via --base)
BASE_DIR = Path(".")

def set_base(path: str):
    global BASE_DIR
    BASE_DIR = Path(path)

FILE_VISUAL   = lambda: BASE_DIR / "debug" / "bot_visual_snapshot.json"
FILE_INNER    = lambda: BASE_DIR / "debug" / "bot_inner_snapshot.json"
FILE_STATS    = lambda: BASE_DIR / "debug" / "trade_stats.json"
FILE_EQUITY   = lambda: BASE_DIR / "debug" / "trade_equity.csv"
FILE_MEMORY   = lambda: BASE_DIR / "bot_memory" / "memory_state.json"

# ─────────────────────────────────────────────
#  FARBEN
# ─────────────────────────────────────────────
C = {
    # Backgrounds
    "bg_root":    "#0d0f13",
    "bg_panel":   "#13161c",
    "bg_card":    "#181c24",
    "bg_card2":   "#1c2130",
    "bg_header":  "#0a0c10",
    "border":     "#252a36",
    "border_hi":  "#2e3548",

    # Text
    "text_hi":    "#e8eaf0",
    "text_med":   "#8b92a8",
    "text_lo":    "#4a5168",
    "text_label": "#5c6480",

    # Außenwelt — neutral-kühl (Blaugrau)
    "out_hi":     "#7ab3d4",
    "out_med":    "#4d7fa0",
    "out_lo":     "#2a4a5e",

    # Innenwelt — regulatorisch codiert
    "inn_green":  "#4caf78",    # stabil / tragfähig
    "inn_orange": "#d4894a",    # Spannung / Übergang
    "inn_red":    "#c05050",    # Überlast
    "inn_blue":   "#5b8dd9",    # neutral / observe
    "inn_purple": "#8b72be",    # meta / regulation

    # Memory — gedämpft
    "mem_hi":     "#a0a8c0",
    "mem_med":    "#606880",
    "mem_lo":     "#363d50",

    # Chart
    "candle_up":  "#3d7a5c",
    "candle_dn":  "#7a3d3d",
    "candle_wick":"#505870",
    "chart_line": "#5b8dd9",
    "chart_bg":   "#0f1218",
    "chart_grid": "#1a1f2b",

    # KPI
    "kpi_pos":    "#4caf78",
    "kpi_neg":    "#c05050",
    "kpi_neu":    "#5b8dd9",

    # Status dots
    "dot_green":  "#4caf78",
    "dot_orange": "#d4894a",
    "dot_red":    "#c05050",
    "dot_grey":   "#363d50",
}

# ─────────────────────────────────────────────
#  MATPLOTLIB DARK STYLE
# ─────────────────────────────────────────────
plt.rcParams.update({
    "figure.facecolor":  C["bg_panel"],
    "axes.facecolor":    C["chart_bg"],
    "axes.edgecolor":    C["border"],
    "axes.labelcolor":   C["text_med"],
    "axes.titlecolor":   C["text_hi"],
    "xtick.color":       C["text_lo"],
    "ytick.color":       C["text_lo"],
    "grid.color":        C["chart_grid"],
    "grid.linewidth":    0.5,
    "text.color":        C["text_med"],
    "font.family":       "monospace",
    "font.size":         8,
})

# ─────────────────────────────────────────────
#  DATEN-LADEN (safe)
# ─────────────────────────────────────────────
def safe_load_json(path_fn) -> dict:
    try:
        p = path_fn()
        if not p.exists():
            return {}
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}

def safe_load_csv(path_fn) -> list:
    try:
        p = path_fn()
        if not p.exists():
            return []
        rows = []
        with open(p, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
        return rows
    except Exception:
        return []

def get_nested(d: dict, *keys, default="–"):
    """Sicher durch verschachtelte Dicts navigieren."""
    cur = d
    for k in keys:
        if not isinstance(cur, dict):
            return default
        cur = cur.get(k, None)
        if cur is None:
            return default
    if cur == "" or cur == {}:
        return default
    return cur

def fmt_float(val, digits=2, default="–"):
    try:
        return f"{float(val):.{digits}f}"
    except (TypeError, ValueError):
        return default

def fmt_pct(val, default="–"):
    try:
        return f"{float(val)*100:.1f}%"
    except (TypeError, ValueError):
        return default

def state_color(val_str: str, invert=False) -> str:
    """Einfaches Farbmapping basierend auf Textwert."""
    if val_str in ("–", None, ""):
        return C["text_lo"]
    s = str(val_str).lower()
    pos_words = {"stable","low","calm","clear","balanced","released","adaptive",
                 "moderate","aligned","loaded","filled","tp","success","high_capacity",
                 "active","confident","structured"}
    neg_words = {"overload","critical","tense","divergent","blocked","failed",
                 "sl","high_load","unstable","chaotic","overloaded","extreme"}
    neu_words = {"observe","wait","sideways","boundary","neutral","medium","weak",
                 "cautious","range","transition","partial"}
    for w in neg_words:
        if w in s:
            return C["inn_red"] if not invert else C["inn_green"]
    for w in pos_words:
        if w in s:
            return C["inn_green"] if not invert else C["inn_red"]
    for w in neu_words:
        if w in s:
            return C["inn_orange"]
    return C["text_med"]

def num_color(val, lo=0.3, hi=0.7, invert=False) -> str:
    """Farbe basierend auf numerischem Wert 0..1."""
    try:
        v = float(val)
    except (TypeError, ValueError):
        return C["text_lo"]
    if invert:
        v = 1 - v
    if v >= hi:
        return C["inn_green"]
    if v >= lo:
        return C["inn_orange"]
    return C["inn_red"]

# ─────────────────────────────────────────────
#  WIEDERVERWENDBARE WIDGET-BAUSTEINE
# ─────────────────────────────────────────────

class CardFrame(tk.Frame):
    """Dunkle Karte mit optionalem Titel."""
    def __init__(self, parent, title="", title_color=None, **kwargs):
        bg = kwargs.pop("bg", C["bg_card"])
        super().__init__(parent, bg=bg,
                         highlightbackground=C["border"],
                         highlightthickness=1, **kwargs)
        if title:
            tk.Label(self, text=title.upper(),
                     bg=bg, fg=title_color or C["text_label"],
                     font=("Courier New", 7, "bold"),
                     anchor="w", padx=6, pady=3).pack(fill="x")
            tk.Frame(self, bg=C["border"], height=1).pack(fill="x")


class KVRow(tk.Frame):
    """Key-Value Zeile."""
    def __init__(self, parent, key: str, value: str = "–",
                 key_color=None, val_color=None, bg=None, **kwargs):
        _bg = bg or parent.cget("bg")
        super().__init__(parent, bg=_bg, **kwargs)
        self.key_lbl  = tk.Label(self, text=key, bg=_bg,
                                 fg=key_color or C["text_label"],
                                 font=("Courier New", 8), anchor="w")
        self.val_lbl  = tk.Label(self, text=str(value), bg=_bg,
                                 fg=val_color or C["text_hi"],
                                 font=("Courier New", 8, "bold"), anchor="e")
        self.key_lbl.pack(side="left", padx=(6,2))
        self.val_lbl.pack(side="right", padx=(2,6))

    def update(self, value: str, val_color=None):
        self.val_lbl.config(text=str(value),
                            fg=val_color or C["text_hi"])


class GaugeArc(tk.Canvas):
    """Halbbogen-Gauge (0..1)."""
    W, H = 80, 50

    def __init__(self, parent, label="", bg=None, **kwargs):
        _bg = bg or parent.cget("bg")
        super().__init__(parent, width=self.W, height=self.H,
                         bg=_bg, highlightthickness=0, **kwargs)
        self._label = label
        self._bg    = _bg
        self._draw(0.0, C["text_lo"])

    def set_value(self, val: float, color: str = None):
        v = max(0.0, min(1.0, val))
        c = color or num_color(v)
        self._draw(v, c)

    def _draw(self, val: float, color: str):
        self.delete("all")
        cx, cy = self.W//2, self.H - 6
        r = 34
        # Track
        self.create_arc(cx-r, cy-r, cx+r, cy+r,
                        start=0, extent=180, style="arc",
                        outline=C["border_hi"], width=4)
        # Fill
        extent = int(val * 180)
        if extent > 0:
            self.create_arc(cx-r, cy-r, cx+r, cy+r,
                            start=0, extent=extent, style="arc",
                            outline=color, width=4)
        # Value text
        self.create_text(cx, cy - 6, text=f"{val:.2f}",
                         fill=color, font=("Courier New", 9, "bold"))
        # Label
        self.create_text(cx, cy + 2, text=self._label,
                         fill=C["text_label"], font=("Courier New", 6))


class BarMeter(tk.Canvas):
    """Horizontaler Fortschrittsbalken."""
    def __init__(self, parent, width=120, height=10, bg=None, **kwargs):
        _bg = bg or parent.cget("bg")
        super().__init__(parent, width=width, height=height,
                         bg=_bg, highlightthickness=0, **kwargs)
        self._bar_width = width
        self._bar_height = height
        self._draw(0, C["text_lo"])

    def set_value(self, val: float, color: str = None):
        v = max(0.0, min(1.0, val))
        c = color or num_color(v)
        self._draw(v, c)

    def _draw(self, val: float, color: str):
        self.delete("all")
        # Track
        self.create_rectangle(0, 0, self._bar_width, self._bar_height,
                               fill=C["border"], outline="")
        # Fill
        fw = int(val * self._bar_width)
        if fw > 0:
            self.create_rectangle(0, 0, fw, self._bar_height,
                                   fill=color, outline="")


class StatusDot(tk.Frame):
    """Farbiger Punkt + Label."""
    def __init__(self, parent, label: str, color: str = None, **kwargs):
        bg = kwargs.pop("bg", parent.cget("bg"))
        super().__init__(parent, bg=bg, **kwargs)
        self._canvas = tk.Canvas(self, width=8, height=8,
                                  bg=bg, highlightthickness=0)
        self._canvas.pack(side="left", padx=(3,2), pady=2)
        self._lbl = tk.Label(self, text=label, bg=bg,
                              fg=C["text_med"], font=("Courier New", 8))
        self._lbl.pack(side="left")
        self._dot_color = color or C["dot_grey"]
        self._draw()

    def _draw(self):
        self._canvas.delete("all")
        self._canvas.create_oval(1, 1, 7, 7, fill=self._dot_color, outline="")

    def set_state(self, label: str, color: str):
        self._dot_color = color
        self._lbl.config(text=label, fg=color)
        self._draw()


# ─────────────────────────────────────────────
#  HAUPT-GUI
# ─────────────────────────────────────────────

class MCMGui:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("MCM Trading Bot — READ-ONLY Monitor")
        self.root.configure(bg=C["bg_root"])
        self.root.resizable(True, True)
        self.root.minsize(1280, 800)

        self._lock   = threading.Lock()
        self._data   = {
            "visual": {},
            "inner": {},
            "stats": {},
            "memory": {},
            "equity": [],
        }
        self._last_valid_data = {
            "visual": {},
            "inner": {},
            "stats": {},
            "memory": {},
            "equity": [],
        }
        self._after_id = None
        self._backtest_start_ts = None
        self._backtest_end_ts = None

        self._build_layout()
        self._start_refresh()

    # ──────────────────────────────
    #  LAYOUT AUFBAU
    # ──────────────────────────────
    def _build_layout(self):
        # --- HEADER ---
        self._build_header()

        # --- STATUSBAR ---
        self._build_statusbar()

        # --- HAUPTBEREICH (3 Spalten + Boden) ---
        main = tk.Frame(self.root, bg=C["bg_root"])
        main.pack(fill="both", expand=True, padx=4, pady=(2,0))

        # Spalten-Gewicht
        main.columnconfigure(0, weight=3, minsize=280)
        main.columnconfigure(1, weight=5, minsize=400)
        main.columnconfigure(2, weight=3, minsize=270)
        main.rowconfigure(0, weight=1)
        main.rowconfigure(1, weight=0)

        # Linke Spalte
        left = tk.Frame(main, bg=C["bg_root"])
        left.grid(row=0, column=0, sticky="nsew", padx=(0,3))
        self._build_left(left)

        # Mittlere Spalte
        mid = tk.Frame(main, bg=C["bg_root"])
        mid.grid(row=0, column=1, sticky="nsew", padx=3)
        self._build_middle(mid)

        # Rechte Spalte
        right = tk.Frame(main, bg=C["bg_root"])
        right.grid(row=0, column=2, sticky="nsew", padx=(3,0))
        self._build_right(right)

        # Unterer Bereich (volle Breite)
        bottom = tk.Frame(main, bg=C["bg_root"])
        bottom.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(4,2))
        self._build_bottom(bottom)

    # ──────────────────────────────
    #  HEADER
    # ──────────────────────────────
    def _build_header(self):
        hdr = tk.Frame(self.root, bg=C["bg_header"],
                       highlightbackground=C["border_hi"],
                       highlightthickness=1, height=30)
        hdr.pack(fill="x", padx=4, pady=(4,0))
        hdr.pack_propagate(False)

        # Coin / Modus / Timeframe / Timestamp
        self._hdr_coin  = tk.Label(hdr, text="– / –",
                                    bg=C["bg_header"], fg=C["text_hi"],
                                    font=("Courier New", 11, "bold"))
        self._hdr_coin.pack(side="left", padx=12)

        sep = tk.Label(hdr, text="│", bg=C["bg_header"], fg=C["border_hi"])
        sep.pack(side="left")

        self._hdr_mode = tk.Label(hdr, text="Mode: –",
                                   bg=C["bg_header"], fg=C["text_med"],
                                   font=("Courier New", 9))
        self._hdr_mode.pack(side="left", padx=8)

        sep2 = tk.Label(hdr, text="│", bg=C["bg_header"], fg=C["border_hi"])
        sep2.pack(side="left")

        self._hdr_tf = tk.Label(hdr, text="Timeframe: –",
                                 bg=C["bg_header"], fg=C["text_med"],
                                 font=("Courier New", 9))
        self._hdr_tf.pack(side="left", padx=8)

        sep3 = tk.Label(hdr, text="│", bg=C["bg_header"], fg=C["border_hi"])
        sep3.pack(side="left")

        self._hdr_ts = tk.Label(hdr, text="Last Tick: –",
                                 bg=C["bg_header"], fg=C["text_med"],
                                 font=("Courier New", 9))
        self._hdr_ts.pack(side="left", padx=8)

        # READ-ONLY Badge rechts
        tk.Label(hdr, text="READ-ONLY",
                 bg=C["bg_header"], fg=C["text_lo"],
                 font=("Courier New", 7, "bold")).pack(side="right", padx=12)

    # ──────────────────────────────
    #  STATUSBAR
    # ──────────────────────────────
    def _build_statusbar(self):
        bar = tk.Frame(self.root, bg=C["bg_panel"],
                       highlightbackground=C["border"],
                       highlightthickness=1, height=26)
        bar.pack(fill="x", padx=4, pady=(2,0))
        bar.pack_propagate(False)

        self._st_runtime   = StatusDot(bar, "Runtime: –",   bg=C["bg_panel"])
        self._st_snapshot  = StatusDot(bar, "Snapshot: –",  bg=C["bg_panel"])
        self._st_position  = StatusDot(bar, "Position: –",  bg=C["bg_panel"])
        self._st_pending   = StatusDot(bar, "Pending: –",   bg=C["bg_panel"])
        for w in (self._st_runtime, self._st_snapshot,
                  self._st_position, self._st_pending):
            w.pack(side="left", padx=6)

        tk.Frame(bar, bg=C["border_hi"], width=1, height=16).pack(side="left", padx=6)

        # Tendenz
        tk.Label(bar, text="Tendenz:", bg=C["bg_panel"], fg=C["text_label"],
                 font=("Courier New", 8)).pack(side="left", padx=(6,2))
        self._st_tendency = tk.Label(bar, text="–", bg=C["bg_panel"],
                                      fg=C["inn_orange"],
                                      font=("Courier New", 9, "bold"))
        self._st_tendency.pack(side="left", padx=(0,8))

        # Proposed Decision
        tk.Label(bar, text="Decision:", bg=C["bg_panel"], fg=C["text_label"],
                 font=("Courier New", 8)).pack(side="left", padx=(4,2))
        self._st_decision = tk.Label(bar, text="–", bg=C["bg_panel"],
                                      fg=C["inn_blue"],
                                      font=("Courier New", 9, "bold"))
        self._st_decision.pack(side="left", padx=(0,8))

        tk.Frame(bar, bg=C["border_hi"], width=1, height=16).pack(side="left", padx=6)

        # Self State
        tk.Label(bar, text="Self State:", bg=C["bg_panel"], fg=C["text_label"],
                 font=("Courier New", 8)).pack(side="left", padx=(4,2))
        self._st_self = tk.Label(bar, text="–", bg=C["bg_panel"],
                                  fg=C["text_med"],
                                  font=("Courier New", 9, "bold"))
        self._st_self.pack(side="left", padx=(0,8))

        # Attractor
        tk.Label(bar, text="Attractor:", bg=C["bg_panel"], fg=C["text_label"],
                 font=("Courier New", 8)).pack(side="left", padx=(4,2))
        self._st_attractor = tk.Label(bar, text="–", bg=C["bg_panel"],
                                       fg=C["mem_hi"],
                                       font=("Courier New", 9, "bold"))
        self._st_attractor.pack(side="left")

    # ──────────────────────────────
    #  LINKE SPALTE — AUSSENWELT
    # ──────────────────────────────
    def _build_left(self, parent):
        # Spaltentitel
        tk.Label(parent, text="AUSSENWELT", bg=C["bg_root"],
                 fg=C["out_med"], font=("Courier New", 9, "bold"),
                 anchor="center").pack(fill="x", pady=(4,2))

        # Chart-Card
        chart_card = CardFrame(parent, bg=C["bg_panel"])
        chart_card.pack(fill="x", pady=(0,3))

        tk.Label(chart_card, text="MARKTÜBERBLICK",
                 bg=C["bg_panel"], fg=C["out_med"],
                 font=("Courier New", 7, "bold"),
                 anchor="w", padx=6, pady=2).pack(fill="x")
        tk.Frame(chart_card, bg=C["border"], height=1).pack(fill="x")

        self._chart_fig = Figure(figsize=(3.2, 2.2), dpi=90,
                                  facecolor=C["chart_bg"])
        self._chart_ax  = self._chart_fig.add_subplot(111)
        self._chart_ax.set_facecolor(C["chart_bg"])
        self._chart_fig.tight_layout(pad=0.4)
        self._chart_canvas = FigureCanvasTkAgg(self._chart_fig, chart_card)
        self._chart_canvas.get_tk_widget().pack(fill="x")

        # Außen-Zustandskarten
        self._candle_card  = self._make_outer_card(parent, "CANDLE STATE")
        self._tension_card = self._make_outer_card(parent, "TENSION STATE")
        self._vms_card     = self._make_outer_card(parent, "VISUAL MARKET STATE")
        self._struct_card  = self._make_outer_card(parent, "STRUCTURE PERCEPTION")

        # Candle-State Zeilen
        self._c_open   = KVRow(self._candle_card, "Open",   bg=C["bg_card"])
        self._c_high   = KVRow(self._candle_card, "High",   bg=C["bg_card"])
        self._c_low    = KVRow(self._candle_card, "Low",    bg=C["bg_card"])
        self._c_close  = KVRow(self._candle_card, "Close",  bg=C["bg_card"])
        self._c_vol    = KVRow(self._candle_card, "Volume", bg=C["bg_card"])
        for w in (self._c_open, self._c_high, self._c_low,
                  self._c_close, self._c_vol):
            w.pack(fill="x")

        # Tension-State
        self._t_tension    = KVRow(self._tension_card, "Tension",    bg=C["bg_card"])
        self._t_volatility = KVRow(self._tension_card, "Volatility", bg=C["bg_card"])
        self._t_tension.pack(fill="x")
        self._t_volatility.pack(fill="x")
        self._t_bar_t = BarMeter(self._tension_card, width=120, height=6,
                                  bg=C["bg_card"])
        self._t_bar_v = BarMeter(self._tension_card, width=120, height=6,
                                  bg=C["bg_card"])
        self._t_bar_t.pack(anchor="e", padx=6, pady=(0,2))
        self._t_bar_v.pack(anchor="e", padx=6, pady=(0,4))

        # Visual Market State
        self._vms_state  = KVRow(self._vms_card, "Market State", bg=C["bg_card"])
        self._vms_trend  = KVRow(self._vms_card, "Trend",        bg=C["bg_card"])
        self._vms_state.pack(fill="x")
        self._vms_trend.pack(fill="x")

        # Structure
        self._sps_zone    = KVRow(self._struct_card, "Zone",    bg=C["bg_card"])
        self._sps_pattern = KVRow(self._struct_card, "Pattern", bg=C["bg_card"])
        self._sps_zone.pack(fill="x")
        self._sps_pattern.pack(fill="x")

    def _make_outer_card(self, parent, title) -> tk.Frame:
        card = CardFrame(parent, title=title,
                         title_color=C["out_lo"], bg=C["bg_card"])
        card.pack(fill="x", pady=(0,3))
        return card

    # ──────────────────────────────
    #  MITTLERE SPALTE — INNENWELT
    # ──────────────────────────────
    def _build_middle(self, parent):
        tk.Label(parent, text="INNENWELT", bg=C["bg_root"],
                 fg=C["inn_orange"], font=("Courier New", 9, "bold"),
                 anchor="center").pack(fill="x", pady=(4,2))

        # Tendenz-Banner
        tend_frame = tk.Frame(parent, bg=C["bg_card2"],
                               highlightbackground=C["border_hi"],
                               highlightthickness=1)
        tend_frame.pack(fill="x", pady=(0,3))

        tk.Label(tend_frame, text="TENDENZ:", bg=C["bg_card2"],
                 fg=C["text_label"], font=("Courier New", 8, "bold")).pack(side="left", padx=8)
        self._mid_tendency = tk.Label(tend_frame, text="–", bg=C["bg_card2"],
                                       fg=C["inn_orange"],
                                       font=("Courier New", 13, "bold"))
        self._mid_tendency.pack(side="left", padx=6)

        self._mid_decision_badge = tk.Label(tend_frame, text=" – ",
                                             bg=C["bg_card"], fg=C["text_hi"],
                                             font=("Courier New", 10, "bold"),
                                             padx=8, pady=2,
                                             relief="flat",
                                             highlightbackground=C["border_hi"],
                                             highlightthickness=1)
        self._mid_decision_badge.pack(side="right", padx=8, pady=3)

        # Kern-Achsen Gauges
        axes_card = CardFrame(parent, bg=C["bg_panel"])
        axes_card.pack(fill="x", pady=(0,3))

        axes_grid = tk.Frame(axes_card, bg=C["bg_panel"])
        axes_grid.pack(fill="x", padx=4, pady=4)

        self._gauges = {}
        gauge_defs = [
            ("field_density",    "Density"),
            ("field_stability",  "Stability"),
            ("regulatory_load",  "Reg.Load"),
            ("action_capacity",  "Capacity"),
            ("recovery_need",    "Recovery"),
            ("survival_pressure","Pressure"),
        ]
        for i, (key, lbl) in enumerate(gauge_defs):
            col = i % 3
            row = i // 3
            frm = tk.Frame(axes_grid, bg=C["bg_panel"])
            frm.grid(row=row, column=col, padx=6, pady=2)
            g = GaugeArc(frm, label=lbl, bg=C["bg_panel"])
            g.pack()
            self._gauges[key] = g
        for c in range(3):
            axes_grid.columnconfigure(c, weight=1)

        # Verarbeitungspanels (3x3 Grid)
        proc_card = CardFrame(parent, bg=C["bg_panel"])
        proc_card.pack(fill="both", expand=True, pady=(0,3))

        proc_grid = tk.Frame(proc_card, bg=C["bg_panel"])
        proc_grid.pack(fill="both", expand=True, padx=4, pady=4)
        for c in range(3):
            proc_grid.columnconfigure(c, weight=1)
        for r in range(3):
            proc_grid.rowconfigure(r, weight=1)

        proc_defs = [
            ("outer_visual_perception_state", "Äußere Wahrnehmung", 0, 0),
            ("inner_field_perception_state",  "Innere Wahrnehmung",  0, 1),
            ("perception_state",              "Perzeption",          0, 2),
            ("processing_state",              "Verarbeitung",        1, 0),
            ("felt_state",                    "Fühlen",              1, 1),
            ("thought_state",                 "Denken",              1, 2),
            ("meta_regulation_state",         "Meta-Regulation",     2, 0),
            ("expectation_state",             "Erwartung",           2, 1),
        ]
        self._proc_panels = {}
        for key, lbl, row, col in proc_defs:
            pf = self._make_proc_panel(proc_grid, lbl)
            pf["frame"].grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            self._proc_panels[key] = pf

        if str(getattr(Config, "MODE", "") or "").strip().upper() == "BACKTEST":
            pf = self._make_proc_panel(proc_grid, "Backtest %")
            pf["frame"].grid(row=2, column=2, padx=2, pady=2, sticky="nsew")
            pf["bar"].pack_forget()
            pf["label"].config(font=("Courier New", 18, "bold"))
            self._proc_panels["backtest_progress_pct"] = pf


    def _normalize_timestamp_ms(self, value):
        try:
            ts = float(value)
        except (TypeError, ValueError):
            return None

        if ts <= 0:
            return None

        if ts > 10_000_000_000_000:
            ts /= 1000.0
        elif ts < 10_000_000_000:
            ts *= 1000.0

        return float(ts)

    def _get_backtest_progress_pct(self, stats):
        if str(getattr(Config, "MODE", "") or "").strip().upper() != "BACKTEST":
            return None

        path = Path(str(getattr(Config, "BACKTEST_FILEPATH", "") or ""))
        if not path.exists():
            return None

        if self._backtest_start_ts is None or self._backtest_end_ts is None:
            first_ts = None
            last_ts = None

            try:
                with open(path, "r", encoding="utf-8") as f:
                    reader = csv.DictReader(f)

                    for row in reader:
                        raw_ts = row.get("timestamp_ms")
                        norm_ts = self._normalize_timestamp_ms(raw_ts)

                        if norm_ts is None:
                            continue

                        if first_ts is None:
                            first_ts = norm_ts

                        last_ts = norm_ts
            except Exception:
                return None

            self._backtest_start_ts = first_ts
            self._backtest_end_ts = last_ts

        current_ts = self._normalize_timestamp_ms(get_nested(stats, "current_timestamp", default=None))
        start_ts = self._backtest_start_ts
        end_ts = self._backtest_end_ts

        if current_ts is None or start_ts is None or end_ts is None or end_ts <= start_ts:
            return None

        progress = (current_ts - start_ts) / (end_ts - start_ts)
        progress = max(0.0, min(1.0, progress))

        return int(round(progress * 100.0))


    def _make_proc_panel(self, parent, title) -> dict:
        """Erstellt ein kleines Verarbeitungspanel, gibt ein dict zurück."""
        card = tk.Frame(parent, bg=C["bg_card"],
                        highlightbackground=C["border"],
                        highlightthickness=1)
        tk.Label(card, text=title.upper(), bg=C["bg_card"],
                 fg=C["text_label"], font=("Courier New", 6, "bold"),
                 anchor="w", padx=4, pady=2).pack(fill="x")
        tk.Frame(card, bg=C["border"], height=1).pack(fill="x")
        state_lbl = tk.Label(card, text="–", bg=C["bg_card"],
                              fg=C["text_med"],
                              font=("Courier New", 8, "bold"),
                              wraplength=110, justify="center")
        state_lbl.pack(expand=True, pady=4, padx=4)
        sub_lbl = tk.Label(card, text="", bg=C["bg_card"],
                           fg=C["text_lo"],
                           font=("Courier New", 7),
                           wraplength=110, justify="center")
        bar = BarMeter(card, width=100, height=5, bg=C["bg_card"])
        bar.pack(pady=(0,4))

        panel_dict = {"frame": card, "label": state_lbl, "sub": sub_lbl, "bar": bar}
        return panel_dict

    # ──────────────────────────────
    #  RECHTE SPALTE — MEMORY
    # ──────────────────────────────
    def _build_right(self, parent):
        tk.Label(parent, text="ENTWICKLUNG & MEMORY", bg=C["bg_root"],
                 fg=C["mem_hi"], font=("Courier New", 9, "bold"),
                 anchor="center").pack(fill="x", pady=(4,2))

        # Signature Memory
        sig_c = CardFrame(parent, title="Signatur Memory",
                           title_color=C["mem_med"], bg=C["bg_card"])
        sig_c.pack(fill="x", pady=(0,3))
        self._mem_sig_keys = KVRow(sig_c, "Keys", bg=C["bg_card"])
        self._mem_sig_avg  = KVRow(sig_c, "Avg",  bg=C["bg_card"])
        self._mem_sig_keys.pack(fill="x")
        self._mem_sig_avg.pack(fill="x")

        # Context Clusters
        ctx_c = CardFrame(parent, title="Kontext Cluster",
                           title_color=C["mem_med"], bg=C["bg_card"])
        ctx_c.pack(fill="x", pady=(0,3))
        self._mem_ctx_count   = KVRow(ctx_c, "Clusters", bg=C["bg_card"])
        self._mem_ctx_current = KVRow(ctx_c, "Current",  bg=C["bg_card"])
        self._mem_ctx_count.pack(fill="x")
        self._mem_ctx_current.pack(fill="x")

        # Letzte Episode
        ep_c = CardFrame(parent, title="Letzte Episode",
                          title_color=C["mem_med"], bg=C["bg_card"])
        ep_c.pack(fill="x", pady=(0,3))
        self._mem_ep_outcome = KVRow(ep_c, "Outcome", bg=C["bg_card"])
        self._mem_ep_drift   = KVRow(ep_c, "Drift",   bg=C["bg_card"])
        self._mem_ep_review  = KVRow(ep_c, "Review",  bg=C["bg_card"])
        self._mem_ep_obs     = KVRow(ep_c, "Observe", bg=C["bg_card"])
        self._mem_ep_bear    = KVRow(ep_c, "Bearing", bg=C["bg_card"])
        self._mem_ep_outcome.pack(fill="x")
        self._mem_ep_drift.pack(fill="x")
        self._mem_ep_review.pack(fill="x")
        self._mem_ep_obs.pack(fill="x")
        self._mem_ep_bear.pack(fill="x")

        # Erfahrungsraum
        exp_c = CardFrame(parent, title="Erfahrungsraum",
                           title_color=C["mem_med"], bg=C["bg_card"])
        exp_c.pack(fill="x", pady=(0,3))
        self._mem_ctx_link = KVRow(exp_c, "Context",       bg=C["bg_card"])
        self._mem_reinf    = KVRow(exp_c, "Reinforcement", bg=C["bg_card"])
        self._mem_atten    = KVRow(exp_c, "Attenuation",   bg=C["bg_card"])
        self._mem_bearing  = KVRow(exp_c, "BearingFx",     bg=C["bg_card"])
        self._mem_feltbear = KVRow(exp_c, "FeltBear",      bg=C["bg_card"])
        self._mem_ctx_link.pack(fill="x")
        self._mem_reinf.pack(fill="x")
        self._mem_atten.pack(fill="x")
        self._mem_bearing.pack(fill="x")
        self._mem_feltbear.pack(fill="x")

        # Fokus & Erwartung
        foc_c = CardFrame(parent, title="Fokus & Erwartung",
                           title_color=C["mem_med"], bg=C["bg_card"])
        foc_c.pack(fill="x", pady=(0,3))
        self._mem_focus   = KVRow(foc_c, "Focus",      bg=C["bg_card"])
        self._mem_conf    = KVRow(foc_c, "Confidence", bg=C["bg_card"])
        self._mem_target  = KVRow(foc_c, "Target",     bg=C["bg_card"])
        self._mem_expect  = KVRow(foc_c, "Expect",     bg=C["bg_card"])
        for w in (self._mem_focus, self._mem_conf,
                  self._mem_target, self._mem_expect):
            w.pack(fill="x")

        # MCM Snapshot
        mcm_c = CardFrame(parent, title="MCM Snapshot",
                           title_color=C["mem_med"], bg=C["bg_card"])
        mcm_c.pack(fill="x", pady=(0,3))
        self._mem_mcm_rt       = KVRow(mcm_c, "Runtime",  bg=C["bg_card"])
        self._mem_mcm_review   = KVRow(mcm_c, "Review",   bg=C["bg_card"])
        self._mem_mcm_rev_hint = KVRow(mcm_c, "RevHint",  bg=C["bg_card"])
        self._mem_mcm_carry    = KVRow(mcm_c, "Carry",    bg=C["bg_card"])
        self._mem_mcm_caution  = KVRow(mcm_c, "Caution",  bg=C["bg_card"])
        self._mem_mcm_action   = KVRow(mcm_c, "Last Act", bg=C["bg_card"])
        self._mem_mcm_attr     = KVRow(mcm_c, "Attractor",bg=C["bg_card"])
        for w in (self._mem_mcm_rt, self._mem_mcm_review,
                  self._mem_mcm_rev_hint, self._mem_mcm_carry,
                  self._mem_mcm_caution, self._mem_mcm_action,
                  self._mem_mcm_attr):
            w.pack(fill="x")

        # MCM Mini-Chart (Bar-Chart für Outcomes)
        self._mem_fig = Figure(figsize=(2.6, 1.4), dpi=90,
                                facecolor=C["bg_card"])
        self._mem_ax  = self._mem_fig.add_subplot(111)
        self._mem_ax.set_facecolor(C["bg_card"])
        self._mem_fig.tight_layout(pad=0.3)
        self._mem_canvas = FigureCanvasTkAgg(self._mem_fig, mcm_c)
        self._mem_canvas.get_tk_widget().pack(fill="x", pady=(2,4))

        # Capacity & Pressure
        cp_c = CardFrame(parent, title="Capacity & Druck",
                          title_color=C["mem_med"], bg=C["bg_card"])
        cp_c.pack(fill="x", pady=(0,3))
        self._mem_cp_cap  = KVRow(cp_c, "Capacity", bg=C["bg_card"])
        self._mem_cp_pres = KVRow(cp_c, "Pressure", bg=C["bg_card"])
        cap_bar_frame = tk.Frame(cp_c, bg=C["bg_card"])
        cap_bar_frame.pack(fill="x", padx=6, pady=(0,4))
        self._mem_cp_cap_bar  = BarMeter(cap_bar_frame, width=90, height=7,
                                          bg=C["bg_card"])
        self._mem_cp_pres_bar = BarMeter(cap_bar_frame, width=90, height=7,
                                          bg=C["bg_card"])
        self._mem_cp_cap.pack(fill="x")
        self._mem_cp_cap_bar.pack(pady=(1,1))
        self._mem_cp_pres.pack(fill="x")
        self._mem_cp_pres_bar.pack(pady=(1,1))

    # ──────────────────────────────
    #  UNTERER BEREICH
    # ──────────────────────────────
    def _build_bottom(self, parent):
        parent.columnconfigure(0, weight=5)
        parent.columnconfigure(1, weight=4)
        parent.columnconfigure(2, weight=3)

        # Equity-Kurve
        eq_c = CardFrame(parent, title="Equity-Kurve",
                          title_color=C["text_label"], bg=C["bg_panel"])
        eq_c.grid(row=0, column=0, sticky="ew", padx=(0,3))

        self._eq_fig = Figure(figsize=(4.0, 1.6), dpi=90,
                               facecolor=C["bg_panel"])
        self._eq_ax  = self._eq_fig.add_subplot(111)
        self._eq_ax.set_facecolor(C["chart_bg"])
        self._eq_fig.tight_layout(pad=0.4)
        self._eq_canvas = FigureCanvasTkAgg(self._eq_fig, eq_c)
        self._eq_canvas.get_tk_widget().pack(fill="x")

        # Attempts-Chart
        att_c = CardFrame(parent, title="Attempts & Outcomes",
                           title_color=C["text_label"], bg=C["bg_panel"])
        att_c.grid(row=0, column=1, sticky="ew", padx=3)

        self._att_fig = Figure(figsize=(3.0, 1.6), dpi=90,
                                facecolor=C["bg_panel"])
        self._att_ax  = self._att_fig.add_subplot(111)
        self._att_ax.set_facecolor(C["chart_bg"])
        self._att_fig.tight_layout(pad=0.4)
        self._att_canvas = FigureCanvasTkAgg(self._att_fig, att_c)
        self._att_canvas.get_tk_widget().pack(fill="x")

        # KPI-Karte
        kpi_c = CardFrame(parent, title="Trade Stats & KPI",
                           title_color=C["text_label"], bg=C["bg_panel"])
        kpi_c.grid(row=0, column=2, sticky="nsew", padx=(3,0))

        self._kpi_pnl    = KVRow(kpi_c, "PnL Netto",  bg=C["bg_panel"])
        self._kpi_wins   = KVRow(kpi_c, "Wins / Loss", bg=C["bg_panel"])
        self._kpi_trades = KVRow(kpi_c, "Trades",      bg=C["bg_panel"])
        self._kpi_canc   = KVRow(kpi_c, "Cancels",     bg=C["bg_panel"])
        self._kpi_atts   = KVRow(kpi_c, "Attempts",    bg=C["bg_panel"])
        self._kpi_obs    = KVRow(kpi_c, "Observed",    bg=C["bg_panel"])
        self._kpi_rep    = KVRow(kpi_c, "Replanned",   bg=C["bg_panel"])
        self._kpi_with   = KVRow(kpi_c, "Withheld",    bg=C["bg_panel"])
        self._kpi_dd     = KVRow(kpi_c, "Max DD",      bg=C["bg_panel"])
        self._kpi_peak   = KVRow(kpi_c, "Eq. Peak",    bg=C["bg_panel"])
        for w in (self._kpi_pnl, self._kpi_wins, self._kpi_trades,
                  self._kpi_canc, self._kpi_atts, self._kpi_obs,
                  self._kpi_rep, self._kpi_with, self._kpi_dd, self._kpi_peak):
            w.pack(fill="x")

        # Attempt-Summary-Bar
        sum_frame = tk.Frame(parent, bg=C["bg_panel"],
                              highlightbackground=C["border"],
                              highlightthickness=1)
        sum_frame.grid(row=1, column=0, columnspan=3, sticky="ew",
                       pady=(3,0))
        self._sum_lbl = tk.Label(sum_frame, text="Attempt Summary: –",
                                  bg=C["bg_panel"], fg=C["text_med"],
                                  font=("Courier New", 8),
                                  anchor="w", padx=6, pady=3)
        self._sum_lbl.pack(fill="x")

    # ──────────────────────────────
    #  REFRESH-LOOP
    # ──────────────────────────────
    def _start_refresh(self):
        self._refresh()

    def _refresh(self):
        try:
            self._load_all_data()
            self._update_all_widgets()
        except Exception as e:
            # Nie einfrieren – Fehler still schlucken
            pass
        self._after_id = self.root.after(REFRESH_MS, self._refresh)

    def _load_all_data(self):
        loaded = {
            "visual":  safe_load_json(FILE_VISUAL),
            "inner":   safe_load_json(FILE_INNER),
            "stats":   safe_load_json(FILE_STATS),
            "memory":  safe_load_json(FILE_MEMORY),
            "equity":  safe_load_csv(FILE_EQUITY),
        }

        merged = {}

        for key, value in loaded.items():
            if key == "equity":
                if isinstance(value, list) and len(value) > 0:
                    self._last_valid_data[key] = list(value)
                merged[key] = list(self._last_valid_data.get(key, []))
                continue

            if isinstance(value, dict) and len(value) > 0:
                self._last_valid_data[key] = dict(value)

            merged[key] = dict(self._last_valid_data.get(key, {}))

        with self._lock:
            self._data = dict(merged)

    # ──────────────────────────────
    #  UPDATE ALLER WIDGETS
    # ──────────────────────────────
    def _update_all_widgets(self):
        with self._lock:
            d = self._data.copy()
        v  = d.get("visual",  {})
        i  = d.get("inner",   {})
        s  = d.get("stats",   {})
        m  = d.get("memory",  {})
        eq = d.get("equity",  [])

        self._update_header(v, i, s)
        self._update_statusbar(v, i, m, s)
        self._update_left(v)
        self._update_middle(i, s)
        self._update_right(m, s)
        self._update_bottom(s, eq)
        self._update_chart(v)

    # --- HEADER ---
    def _update_header(self, v, i, s):
        ts_v = get_nested(v, "timestamp")
        ts_i = get_nested(i, "timestamp")
        ts   = ts_v if ts_v != "–" else ts_i

        coin = get_nested(v, "window", "symbol",
                          default=get_nested(s, "coin", default="–"))
        mode = get_nested(s, "mode", default="–")
        tf   = get_nested(v, "window", "timeframe",
                          default=get_nested(s, "timeframe", default="–"))

        self._hdr_coin.config(text=str(coin))
        self._hdr_mode.config(text=f"Mode: {mode}")
        self._hdr_tf.config(text=f"Timeframe: {tf}")
        self._hdr_ts.config(text=f"Last Tick: {ts}")

    # --- STATUSBAR ---
    def _update_statusbar(self, v, i, m, s):
        # Runtime
        rt = get_nested(m, "mcm_runtime_snapshot", "active",
                        default=get_nested(s, "runtime_active", default=None))
        if rt is True or str(rt).lower() in ("true","1","active"):
            self._st_runtime.set_state("Runtime: Active", C["dot_green"])
        elif rt is False or str(rt).lower() in ("false","0","inactive"):
            self._st_runtime.set_state("Runtime: Inactive", C["dot_grey"])
        else:
            self._st_runtime.set_state("Runtime: –", C["dot_grey"])

        # Snapshot-Aktualität
        ts = get_nested(v, "timestamp")
        if ts != "–":
            try:
                diff = time.time() - float(ts)
                fresh = diff < 10
            except (ValueError, TypeError):
                fresh = True
            self._st_snapshot.set_state(
                "Snapshot: Current" if fresh else "Snapshot: Stale",
                C["dot_green"] if fresh else C["dot_orange"])
        else:
            self._st_snapshot.set_state("Snapshot: –", C["dot_grey"])

        # Position
        pos = get_nested(m, "mcm_last_action", "position",
                         default=get_nested(s, "open_position", default=None))
        if pos and str(pos).lower() not in ("none","–","null","false","0"):
            self._st_position.set_state(f"Position: {pos}", C["dot_orange"])
        else:
            self._st_position.set_state("Position: None", C["dot_grey"])

        # Pending
        pend = get_nested(m, "mcm_runtime_decision_state", "pending_entry",
                          default=None)
        if pend and str(pend).lower() not in ("none","–","null","false"):
            self._st_pending.set_state(f"Pending: {pend}", C["dot_orange"])
        else:
            self._st_pending.set_state("Pending: None", C["dot_grey"])

        # Tendenz
        tend = get_nested(m, "mcm_runtime_decision_state", "decision_tendency",
                           default=get_nested(i, "meta_regulation_state",
                                              "decision", default="–"))
        tc = state_color(str(tend))
        self._st_tendency.config(text=str(tend).upper(), fg=tc)
        self._mid_tendency.config(text=str(tend).upper(), fg=tc)

        # Proposed Decision
        dec = get_nested(m, "mcm_runtime_decision_state", "proposed_decision",
                         default=get_nested(m, "mcm_last_action", "action",
                                            default="–"))
        dc = state_color(str(dec))
        self._st_decision.config(text=str(dec).upper(), fg=dc)
        self._mid_decision_badge.config(text=f" {str(dec).upper()} ", fg=dc)

        # Self State
        ss = get_nested(i, "meta_regulation_state",
                        default=get_nested(m, "mcm_runtime_brain_snapshot",
                                           "self_state", default="–"))
        self._st_self.config(text=str(ss), fg=state_color(str(ss)))

        # Attractor
        attr = get_nested(m, "mcm_last_attractor",
                          default=get_nested(m, "mcm_memory", "last_attractor",
                                             default="–"))
        self._st_attractor.config(text=str(attr), fg=C["mem_hi"])

    # --- LINKE SPALTE ---
    def _update_left(self, v):
        cs = get_nested(v, "candle_state")
        if isinstance(cs, dict):
            self._c_open.update(fmt_float(cs.get("open")))
            self._c_high.update(fmt_float(cs.get("high")),
                                 C["inn_green"])
            self._c_low.update(fmt_float(cs.get("low")),
                                C["inn_red"])
            self._c_close.update(fmt_float(cs.get("close")),
                                  C["out_hi"])
            self._c_vol.update(fmt_float(cs.get("volume"), 0))
        else:
            for w in (self._c_open, self._c_high, self._c_low,
                      self._c_close, self._c_vol):
                w.update("–")

        ts = get_nested(v, "tension_state")
        if isinstance(ts, dict):
            t_val = ts.get("tension",    ts.get("value", "–"))
            v_val = ts.get("volatility", "–")
            self._t_tension.update(fmt_float(t_val),
                                    num_color(t_val, invert=True))
            self._t_volatility.update(fmt_float(v_val),
                                       num_color(v_val, invert=True))
            try:
                self._t_bar_t.set_value(float(t_val), C["inn_orange"])
                self._t_bar_v.set_value(float(v_val), C["inn_orange"])
            except (TypeError, ValueError):
                pass
        else:
            ts_str = str(ts) if ts != "–" else "–"
            self._t_tension.update(ts_str, state_color(ts_str))
            self._t_volatility.update("–")

        vms = get_nested(v, "visual_market_state")
        if isinstance(vms, dict):
            self._vms_state.update(str(vms.get("state", "–")),
                                    state_color(str(vms.get("state", ""))))
            self._vms_trend.update(str(vms.get("trend", "–")))
        else:
            vms_str = str(vms) if vms != "–" else "–"
            self._vms_state.update(vms_str, state_color(vms_str))
            self._vms_trend.update("–")

        sps = get_nested(v, "structure_perception_state")
        if isinstance(sps, dict):
            self._sps_zone.update(str(sps.get("zone",    "–")),
                                   state_color(str(sps.get("zone", ""))))
            self._sps_pattern.update(str(sps.get("pattern", "–")))
        else:
            sps_str = str(sps) if sps != "–" else "–"
            self._sps_zone.update(sps_str, state_color(sps_str))
            self._sps_pattern.update("–")

    # --- MITTLERE SPALTE ---
    def _update_middle(self, i, s):
        field_state = get_nested(i, "field_state", default={})
        runtime_state = get_nested(i, "runtime_state", default={})

        if not isinstance(field_state, dict):
            field_state = {}

        if not isinstance(runtime_state, dict):
            runtime_state = {}

        # Gauges
        gauge_keys = [
            ("field_density",    False),
            ("field_stability",  False),
            ("regulatory_load",  True),
            ("action_capacity",  False),
            ("recovery_need",    True),
            ("survival_pressure",True),
        ]
        for key, inv in gauge_keys:
            raw = field_state.get(key, get_nested(i, key))
            if raw != "–":
                try:
                    v = float(raw)
                    self._gauges[key].set_value(v, num_color(v, invert=inv))
                except (TypeError, ValueError):
                    self._gauges[key].set_value(0, C["text_lo"])
            else:
                self._gauges[key].set_value(0, C["text_lo"])

        # Verarbeitungspanels
        proc_keys = [
            "outer_visual_perception_state",
            "inner_field_perception_state",
            "perception_state",
            "processing_state",
            "felt_state",
            "thought_state",
            "meta_regulation_state",
            "expectation_state",
        ]
        for key in proc_keys:
            panel = self._proc_panels.get(key)
            if panel is None:
                continue
            raw = get_nested(i, key)
            if isinstance(raw, dict):
                state_val = raw.get("state", raw.get("label",
                             raw.get("value", str(list(raw.values())[0])
                                     if raw else "–")))
            else:
                state_val = str(raw) if raw != "–" else "–"

            c = state_color(state_val)
            panel["label"].config(text=state_val, fg=c)
            num_val = None
            if isinstance(get_nested(i, key), dict):
                for sub in ("value", "score", "level", "load"):
                    sv = get_nested(i, key, sub)
                    if sv != "–":
                        try:
                            num_val = float(sv)
                            break
                        except (TypeError, ValueError):
                            pass
            if num_val is not None:
                panel["bar"].set_value(num_val, c)
            else:
                panel["bar"].set_value(0, C["text_lo"])

        progress_panel = self._proc_panels.get("backtest_progress_pct")
        if progress_panel is not None:
            progress_pct = self._get_backtest_progress_pct(s)
            decision_tendency = str(runtime_state.get("decision_tendency", "–") or "–")
            proposed_decision = str(runtime_state.get("proposed_decision", "–") or "–")
            observation_mode = bool(runtime_state.get("observation_mode", False))

            if progress_pct is None:
                progress_panel["label"].config(text="–", fg=C["text_lo"])
            else:
                progress_panel["label"].config(
                    text=f"{progress_pct}%",
                    fg=C["inn_blue"] if observation_mode else C["inn_orange"],
                )

            progress_panel["sub"].config(
                text=f"{decision_tendency.upper()} | {proposed_decision.upper()}",
                fg=state_color(decision_tendency),
            )

    # --- RECHTE SPALTE ---
    def _update_right(self, m, s):
        # Signature Memory
        sig = get_nested(m, "signature_memory")
        if isinstance(sig, dict):
            self._mem_sig_keys.update(str(len(sig)), C["mem_hi"])
            vals = [v for v in sig.values()
                    if isinstance(v, (int, float))]
            avg  = sum(vals)/len(vals) if vals else 0
            self._mem_sig_avg.update(fmt_float(avg), C["mem_hi"])
        elif isinstance(sig, list):
            self._mem_sig_keys.update(str(len(sig)), C["mem_hi"])
            self._mem_sig_avg.update("–")
        else:
            self._mem_sig_keys.update("–")
            self._mem_sig_avg.update("–")

        # Context Clusters
        ctx = get_nested(m, "context_clusters")
        if isinstance(ctx, (dict, list)):
            n = len(ctx)
            self._mem_ctx_count.update(str(n), C["mem_hi"])
            if isinstance(ctx, dict):
                cur = get_nested(m, "mcm_runtime_brain_snapshot",
                                 "current_cluster", default="–")
                self._mem_ctx_current.update(str(cur))
            else:
                self._mem_ctx_current.update("–")
        else:
            self._mem_ctx_count.update("–")
            self._mem_ctx_current.update("–")

        # Letzte Episode
        ep = get_nested(m, "mcm_decision_episode")
        ep_internal = get_nested(m, "mcm_decision_episode_internal", default={})
        review_notes = {}
        if isinstance(ep_internal, dict):
            review_notes = dict(ep_internal.get("review_notes", {}) or {})

        if isinstance(ep, dict):
            outcome = ep.get("outcome", ep.get("result", "–"))
            drift   = ep.get("drift",   "–")
            oc      = state_color(str(outcome))
            self._mem_ep_outcome.update(str(outcome), oc)
            try:
                df = float(drift)
                dc = C["inn_green"] if df < 0 else C["inn_orange"]
                self._mem_ep_drift.update(f"{df:+.3f}", dc)
            except (TypeError, ValueError):
                self._mem_ep_drift.update(str(drift))
        else:
            self._mem_ep_outcome.update("–")
            self._mem_ep_drift.update("–")

        if isinstance(review_notes, dict) and review_notes:
            review_score = review_notes.get("review_score", "–")
            observation_quality = review_notes.get("observation_quality", "–")
            structural_bearing_quality = review_notes.get("structural_bearing_quality", "–")

            self._mem_ep_review.update(fmt_float(review_score), num_color(review_score))
            self._mem_ep_obs.update(fmt_float(observation_quality), num_color(observation_quality))
            self._mem_ep_bear.update(fmt_float(structural_bearing_quality), num_color(structural_bearing_quality))
        else:
            self._mem_ep_review.update("–")
            self._mem_ep_obs.update("–")
            self._mem_ep_bear.update("–")

        # Experience Space
        exp = get_nested(m, "mcm_experience_space")
        if isinstance(exp, dict):
            current_context_id = str(
                get_nested(
                    m,
                    "mcm_runtime_decision_state",
                    "context_cluster_id",
                    default=get_nested(m, "last_context_cluster_id", default="-"),
                ) or "-"
            )
            context_links = dict(exp.get("context_links", {}) or {})
            context_item = dict(context_links.get(current_context_id, {}) or {})

            self._mem_ctx_link.update(str(current_context_id), C["mem_hi"])
            self._mem_reinf.update(
                fmt_float(context_item.get("reinforcement", "–")),
                num_color(context_item.get("reinforcement", "–")),
            )
            self._mem_atten.update(
                fmt_float(context_item.get("attenuation", "–")),
                num_color(context_item.get("attenuation", "–"), invert=True),
            )
            self._mem_bearing.update(
                fmt_float(context_item.get("bearing_effect", "–")),
                num_color(context_item.get("bearing_effect", "–")),
            )
            self._mem_feltbear.update(
                fmt_float(context_item.get("felt_bearing_score", "–")),
                num_color(context_item.get("felt_bearing_score", "–")),
            )
        else:
            for w in (
                self._mem_ctx_link,
                self._mem_reinf,
                self._mem_atten,
                self._mem_bearing,
                self._mem_feltbear,
            ):
                w.update("–")

        # Fokus & Erwartung
        self._mem_focus.update(str(get_nested(m, "focus_point")))
        self._mem_conf.update(fmt_float(get_nested(m, "focus_confidence")))
        self._mem_target.update(str(get_nested(m, "target_drift",
                                               default=get_nested(m, "target_lock"))))
        self._mem_expect.update(fmt_float(get_nested(m, "entry_expectation",
                                                     default=get_nested(
                                                         m, "target_expectation"))))

        # MCM Snapshot
        snap = get_nested(m, "mcm_runtime_snapshot")
        if isinstance(snap, dict):
            self._mem_mcm_rt.update(str(snap.get("runtime_ticks",
                                                   snap.get("runtime","–"))))
            self._mem_mcm_review.update(str(snap.get("review_state","–")))
            la = get_nested(m, "mcm_last_action")
            at = get_nested(m, "mcm_last_attractor")
            review_hint = get_nested(s, "review_tendency_hint")
            review_carry = get_nested(s, "review_carry_capacity")
            review_caution = get_nested(s, "review_caution_load")

            self._mem_mcm_rev_hint.update(str(review_hint), state_color(str(review_hint)))
            self._mem_mcm_carry.update(fmt_float(review_carry), num_color(review_carry))
            self._mem_mcm_caution.update(fmt_float(review_caution), num_color(review_caution, invert=True))
            self._mem_mcm_action.update(str(la), state_color(str(la)))
            self._mem_mcm_attr.update(str(at), state_color(str(at)))
        else:
            for w in (self._mem_mcm_rt, self._mem_mcm_review,
                      self._mem_mcm_rev_hint, self._mem_mcm_carry,
                      self._mem_mcm_caution, self._mem_mcm_action,
                      self._mem_mcm_attr):
                w.update("–")

        last_action  = get_nested(m, "mcm_last_action")
        last_attr    = get_nested(m, "mcm_last_attractor")
        if isinstance(last_action, dict):
            self._mem_mcm_action.update(str(last_action.get("action","–")))
        else:
            self._mem_mcm_action.update(str(last_action))
        self._mem_mcm_attr.update(str(last_attr))

        # MCM Mini-BarChart
        self._draw_mcm_barchart(s)

        # Capacity & Pressure
        cap  = get_nested(m, "mcm_experience_space", "load_bearing_capacity",
                          default=get_nested(s, "action_capacity", default="–"))
        pres = get_nested(m, "approach_pressure",
                          default=get_nested(m, "survival_pressure", default="–"))
        cap_str  = fmt_pct(cap,  default=fmt_float(cap))
        pres_str = fmt_pct(pres, default=fmt_float(pres))
        cap_c    = num_color(cap)
        pres_c   = num_color(pres, invert=True)
        self._mem_cp_cap.update(cap_str,  cap_c)
        self._mem_cp_pres.update(pres_str, pres_c)
        try:
            self._mem_cp_cap_bar.set_value(float(cap),  cap_c)
            self._mem_cp_pres_bar.set_value(float(pres), pres_c)
        except (TypeError, ValueError):
            pass

    def _draw_mcm_barchart(self, s):
        ax = self._mem_ax
        ax.clear()
        ax.set_facecolor(C["bg_card"])
        tp    = s.get("tp", 0)
        sl    = s.get("sl", 0)
        canc  = s.get("cancels", 0)
        try:
            vals = [int(tp), int(sl), int(canc)]
        except (TypeError, ValueError):
            vals = [0, 0, 0]
        labels = ["TP", "SL", "Canc"]
        colors = [C["inn_green"], C["inn_red"], C["mem_med"]]
        bars = ax.bar(labels, vals, color=colors, width=0.5)
        for bar, v in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                    str(v), ha='center', va='bottom',
                    color=C["text_med"], fontsize=6)
        ax.set_xticks(range(len(labels)))
        ax.set_xticklabels(labels, fontsize=6, color=C["text_med"])
        ax.set_yticks([])
        ax.spines[:].set_visible(False)
        self._mem_fig.tight_layout(pad=0.3)
        self._mem_canvas.draw_idle()

    # --- UNTERER BEREICH ---
    def _update_bottom(self, s, eq):
        # KPI
        pnl = s.get("pnl_netto", "–")
        try:
            pf  = float(pnl)
            pc  = C["kpi_pos"] if pf >= 0 else C["kpi_neg"]
            self._kpi_pnl.update(f"{pf:+.2f}", pc)
        except (TypeError, ValueError):
            self._kpi_pnl.update(str(pnl))

        tp = s.get("tp", "–")
        sl = s.get("sl", "–")
        self._kpi_wins.update(f"{tp} / {sl}")
        self._kpi_trades.update(str(s.get("trades", "–")))
        self._kpi_canc.update(str(s.get("cancels","–")))
        self._kpi_atts.update(str(s.get("attempts","–")))
        self._kpi_obs.update(str(s.get("attempts_observed","–")))
        self._kpi_rep.update(str(s.get("attempts_replanned","–")))
        self._kpi_with.update(str(s.get("attempts_withheld","–")))

        dd   = s.get("max_drawdown_pct","–")
        peak = s.get("equity_peak","–")
        try:
            ddf = float(dd)
            self._kpi_dd.update(f"{ddf:.2f}%",
                                 C["kpi_neg"] if ddf > 5 else C["kpi_neu"])
        except (TypeError, ValueError):
            self._kpi_dd.update(str(dd))
        self._kpi_peak.update(str(peak), C["mem_hi"])

        # Summary Bar
        subm = s.get("attempts_submitted", "–")
        skip = s.get("attempts_skipped",   "–")
        obs  = s.get("attempts_observed",  "–")
        repl = s.get("attempts_replanned", "–")
        with_ = s.get("attempts_withheld","–")
        canc = s.get("attempts_cancelled","–")
        self._sum_lbl.config(
            text=f"Attempt Summary:  Subm: {subm}  |  Skip: {skip}  |  "
                 f"Obs: {obs}  |  Repl: {repl}  |  Non-Action: {with_}  |  Canc: {canc}")

        # Equity-Kurve
        self._draw_equity(eq, s)

        # Attempts-Chart
        self._draw_attempts(s)

    def _draw_equity(self, eq_rows, s):
        ax = self._eq_ax
        ax.clear()
        ax.set_facecolor(C["chart_bg"])

        values = []
        for row in eq_rows:
            for key in ("pnl_netto", "equity", "value", "balance", "pnl_cumulative"):
                v = row.get(key)
                if v is not None:
                    try:
                        values.append(float(v))
                        break
                    except (TypeError, ValueError):
                        pass

        if values:
            x = range(len(values))
            ax.plot(x, values, color=C["chart_line"], linewidth=1.0)
            ax.fill_between(x, values, min(values),
                             alpha=0.12, color=C["chart_line"])
            ax.set_xlim(0, max(1, len(values)-1))
        else:
            # Zeige Peak aus stats
            peak = s.get("equity_peak")
            if peak:
                ax.text(0.5, 0.5, f"Peak: {peak}",
                        transform=ax.transAxes,
                        ha="center", va="center",
                        color=C["text_lo"], fontsize=8)
            else:
                ax.text(0.5, 0.5, "Keine Equity-Daten",
                        transform=ax.transAxes,
                        ha="center", va="center",
                        color=C["text_lo"], fontsize=8)

        ax.grid(True, alpha=0.3)
        ax.spines[:].set_color(C["border"])
        self._eq_fig.tight_layout(pad=0.4)
        self._eq_canvas.draw_idle()

    def _draw_attempts(self, s):
        ax = self._att_ax
        ax.clear()
        ax.set_facecolor(C["chart_bg"])

        cats = ["Subm","Fill","Canc","Obs","Repl","With"]
        keys = ["attempts_submitted","attempts_filled","attempts_cancelled",
                "attempts_observed","attempts_replanned","attempts_withheld"]
        vals = []
        for k in keys:
            try:
                vals.append(int(s.get(k, 0) or 0))
            except (TypeError, ValueError):
                vals.append(0)

        colors = [C["kpi_neu"], C["inn_green"], C["inn_red"],
                  C["inn_blue"], C["inn_orange"], C["mem_med"]]

        if any(v > 0 for v in vals):
            bars = ax.bar(cats, vals, color=colors, width=0.6)
            for bar, v in zip(bars, vals):
                if v > 0:
                    ax.text(bar.get_x() + bar.get_width()/2,
                            bar.get_height() + 0.3,
                            str(v), ha='center', va='bottom',
                            color=C["text_med"], fontsize=6)
        else:
            ax.text(0.5, 0.5, "Keine Attempt-Daten",
                    transform=ax.transAxes,
                    ha="center", va="center",
                    color=C["text_lo"], fontsize=8)

        ax.set_xticks(range(len(cats)))
        ax.set_xticklabels(cats, fontsize=6, color=C["text_med"])
        ax.set_yticks([])
        ax.spines[:].set_color(C["border"])
        self._att_fig.tight_layout(pad=0.4)
        self._att_canvas.draw_idle()

    # --- CHART ---
    def _update_chart(self, v):
        ax = self._chart_ax
        ax.clear()
        ax.set_facecolor(C["chart_bg"])

        chart_snapshot = get_nested(v, "chart_snapshot", default={})
        window = get_nested(v, "window")
        candles = []

        if isinstance(chart_snapshot, dict):
            candles = list(chart_snapshot.get("candles", []) or [])

        if not candles:
            if isinstance(window, dict):
                candles = window.get("candles",
                           window.get("ohlcv",
                           window.get("data", [])))
            elif isinstance(window, list):
                candles = list(window)

        if isinstance(candles, list) and len(candles) > 0:
            candles = candles[-CANDLE_COUNT:]
            opens, highs, lows, closes = [], [], [], []
            for c in candles:
                if isinstance(c, (list, tuple)) and len(c) >= 5:
                    opens.append(float(c[1]))
                    highs.append(float(c[2]))
                    lows.append(float(c[3]))
                    closes.append(float(c[4]))
                elif isinstance(c, dict):
                    opens.append(float(c.get("open",  c.get("o", 0))))
                    highs.append(float(c.get("high",  c.get("h", 0))))
                    lows.append(float(c.get("low",    c.get("l", 0))))
                    closes.append(float(c.get("close", c.get("c", 0))))

            if opens:
                n = len(opens)
                xs = range(n)
                for idx in xs:
                    up   = closes[idx] >= opens[idx]
                    col  = C["candle_up"] if up else C["candle_dn"]
                    body_lo = min(opens[idx], closes[idx])
                    body_hi = max(opens[idx], closes[idx])
                    body_h = max(body_hi - body_lo, 0.0000001)

                    ax.bar(idx, body_h, bottom=body_lo,
                           color=col, width=0.6, linewidth=0)
                    ax.plot([idx, idx], [lows[idx], highs[idx]],
                            color=C["candle_wick"], linewidth=0.5)

                close_trace = list(chart_snapshot.get("close_trace", []) or []) if isinstance(chart_snapshot, dict) else []
                if close_trace and len(close_trace) == n:
                    ax.plot(range(n), close_trace, color=C["chart_line"], linewidth=0.8, alpha=0.55)

                ax.set_xlim(-1, n)
                ax.set_xticks([])
        else:
            cs = get_nested(v, "candle_state")
            if isinstance(cs, dict):
                c_val = cs.get("close")
                if c_val:
                    ax.axhline(float(c_val), color=C["chart_line"],
                               linewidth=0.8, linestyle="--", alpha=0.6)
                    ax.text(0.5, 0.5, f"Close: {c_val}",
                            transform=ax.transAxes,
                            ha="center", va="center",
                            color=C["out_hi"], fontsize=9)
            else:
                ax.text(0.5, 0.5, "Keine Chart-Daten",
                        transform=ax.transAxes,
                        ha="center", va="center",
                        color=C["text_lo"], fontsize=8)

        ax.grid(True, alpha=0.25)
        ax.spines[:].set_color(C["border"])
        ax.tick_params(labelsize=6)
        self._chart_fig.tight_layout(pad=0.3)
        self._chart_canvas.draw_idle()

    # ──────────────────────────────
    #  CLEANUP
    # ──────────────────────────────
    def destroy(self):
        if self._after_id:
            self.root.after_cancel(self._after_id)
        self.root.destroy()


# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="MCM Trading Bot READ-ONLY GUI")
    parser.add_argument("--base", default=".",
                        help="Basis-Pfad zum Bot-Verzeichnis (default: .)")
    args = parser.parse_args()
    set_base(args.base)

    root = tk.Tk()
    root.geometry("1400x900")
    app  = MCMGui(root)
    root.protocol("WM_DELETE_WINDOW", app.destroy)

    try:
        root.mainloop()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()