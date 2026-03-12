# ==================================================
# coherence_visual_gui.py
# ==================================================
# READ-ONLY DEBUG GUI
# - liest tension_debug.txt
# - visualisiert coherence / energy / asymmetry
# - kein Schreiben
# - kein Reset
# - kein Bot-Start
# - dark style analog zu _gui.py
# ==================================================

import os
import re
import tkinter as tk
from tkinter import ttk

import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# ==================================================
# CONFIG
# ==================================================
DEBUG_PATH = "debug/tension_debug.txt"
REFRESH_MS = 1000
MAX_POINTS = 100

BG = "#121212"
FG = "#e0e0e0"
FG_DIM = "#9aa0a6"
ACCENT = "#4fc3f7"
GOOD = "#66bb6a"
BAD = "#ef5350"
WARN = "#ffa726"
GRID = "#2a2a2a"
PANEL = "#1b1b1b"

LINE_RE = re.compile(
    r"energy:\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)\s*\|\s*"
    r"coherence:\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)\s*\|\s*"
    r"energy:\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)"
)


# ==================================================
# PARSER
# ==================================================
def parse_tension_file(path: str):

    rows = []

    if not os.path.exists(path):
        return rows

    try:
        with open(path, "r", encoding="utf-8") as f:
            for idx, raw in enumerate(f, start=1):
                line = raw.strip()
                if not line:
                    continue

                m = LINE_RE.search(line)
                if not m:
                    continue

                try:
                    energy = float(m.group(1))
                    coherence = float(m.group(2))
                    asymmetry = int(float(m.group(3)))
                except Exception:
                    continue

                rows.append(
                    {
                        "index": idx,
                        "energy": energy,
                        "coherence": coherence,
                        "asymmetry": asymmetry,
                        "resonance": abs(energy) * abs(coherence),
                    }
                )
    except Exception:
        return []

    return rows


# ==================================================
# GUI
# ==================================================
class CoherenceVisualGUI:

    # --------------------------------------------------
    def __init__(self, root):

        self.root = root
        self.root.title("Coherence Visual Debug")
        self.root.configure(bg=BG)
        self.root.geometry("1420x900")

        self.last_mtime = None
        self.rows = []

        self._build_style()
        self._build_layout()
        self._build_plot()
        self._update_loop()

    # --------------------------------------------------
    def _build_style(self):

        style = ttk.Style()
        style.theme_use("default")
        style.configure("TFrame", background=BG)
        style.configure("TLabel", background=BG, foreground=FG, font=("Segoe UI", 10))
        style.configure("Title.TLabel", background=BG, foreground=ACCENT, font=("Segoe UI", 11, "bold"))
        style.configure("Value.TLabel", background=BG, foreground=FG, font=("Consolas", 11))
        style.configure("Dim.TLabel", background=BG, foreground=FG_DIM, font=("Segoe UI", 9))
        style.configure("Panel.TFrame", background=PANEL)

    # --------------------------------------------------
    def _build_layout(self):

        self.container = ttk.Frame(self.root)
        self.container.pack(fill="both", expand=True, padx=10, pady=10)

        self.header = ttk.Frame(self.container)
        self.header.pack(fill="x", pady=(0, 10))

        self.left_info = ttk.Frame(self.header)
        self.left_info.pack(side="left", fill="x", expand=True)

        self.right_info = ttk.Frame(self.header)
        self.right_info.pack(side="right")

        ttk.Label(self.left_info, text="COHERENCE VISUAL DEBUG", style="Title.TLabel").grid(row=0, column=0, sticky="w")
        ttk.Label(self.left_info, text=f"Datei: {DEBUG_PATH}", style="Dim.TLabel").grid(row=1, column=0, sticky="w")

        self.var_status = tk.StringVar(value="warte auf Datei")
        self.var_points = tk.StringVar(value="0")
        self.var_last_energy = tk.StringVar(value="-")
        self.var_last_coherence = tk.StringVar(value="-")
        self.var_last_asym = tk.StringVar(value="-")
        self.var_last_resonance = tk.StringVar(value="-")
        self.var_pos = tk.StringVar(value="0")
        self.var_neg = tk.StringVar(value="0")
        self.var_zero = tk.StringVar(value="0")
        self.var_coh_mean = tk.StringVar(value="-")
        self.var_energy_mean = tk.StringVar(value="-")

        self._stat(self.right_info, 0, 0, "Status", self.var_status)
        self._stat(self.right_info, 0, 2, "Punkte", self.var_points)
        self._stat(self.right_info, 1, 0, "Energy", self.var_last_energy)
        self._stat(self.right_info, 1, 2, "Coherence", self.var_last_coherence)
        self._stat(self.right_info, 2, 0, "Asym", self.var_last_asym)
        self._stat(self.right_info, 2, 2, "Resonance", self.var_last_resonance)
        self._stat(self.right_info, 3, 0, "Pos", self.var_pos)
        self._stat(self.right_info, 3, 2, "Neg", self.var_neg)
        self._stat(self.right_info, 4, 0, "Zero", self.var_zero)
        self._stat(self.right_info, 4, 2, "Ø Coh", self.var_coh_mean)
        self._stat(self.right_info, 5, 0, "Ø Eng", self.var_energy_mean)

        self.body = ttk.Frame(self.container)
        self.body.pack(fill="both", expand=True)

        self.plot_wrap = ttk.Frame(self.body, style="Panel.TFrame")
        self.plot_wrap.pack(side="left", fill="both", expand=True)

        self.side_wrap = ttk.Frame(self.body, style="Panel.TFrame")
        self.side_wrap.pack(side="right", fill="y", padx=(10, 0))

        ttk.Label(self.side_wrap, text="LETZTE WERTE", style="Title.TLabel").pack(anchor="w", padx=10, pady=(10, 8))

        self.listbox = tk.Listbox(
            self.side_wrap,
            bg=PANEL,
            fg=FG,
            selectbackground="#263238",
            selectforeground=FG,
            bd=0,
            highlightthickness=0,
            width=54,
            height=32,
            font=("Consolas", 10),
        )
        self.listbox.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    # --------------------------------------------------
    def _stat(self, parent, row, col, label, var):

        ttk.Label(parent, text=label, style="Dim.TLabel").grid(row=row, column=col, sticky="e", padx=(8, 4), pady=2)
        ttk.Label(parent, textvariable=var, style="Value.TLabel").grid(row=row, column=col + 1, sticky="w", padx=(0, 12), pady=2)

    # --------------------------------------------------
    def _build_plot(self):

        self.fig = Figure(figsize=(12, 7), dpi=100, facecolor=BG)

        self.ax_energy = self.fig.add_subplot(311)
        self.ax_coherence = self.fig.add_subplot(312)
        self.ax_scatter = self.fig.add_subplot(313)

        self.fig.subplots_adjust(left=0.06, right=0.98, top=0.97, bottom=0.06, hspace=0.36)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_wrap)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    # --------------------------------------------------
    def _apply_axis_style(self, ax, title):

        ax.set_facecolor(PANEL)
        ax.set_title(title, color=FG, fontsize=11)
        ax.tick_params(colors=FG_DIM, labelsize=9)
        ax.grid(True, color=GRID, linewidth=0.8, alpha=0.8)

        for spine in ax.spines.values():
            spine.set_color(GRID)

    # --------------------------------------------------
    def _read_if_changed(self):

        if not os.path.exists(DEBUG_PATH):
            self.rows = []
            self.var_status.set("Datei fehlt")
            return

        try:
            mtime = os.path.getmtime(DEBUG_PATH)
        except Exception:
            self.rows = []
            self.var_status.set("Dateifehler")
            return

        if self.last_mtime is not None and mtime == self.last_mtime:
            return

        self.last_mtime = mtime
        self.rows = parse_tension_file(DEBUG_PATH)
        self.var_status.set("aktualisiert")

    # --------------------------------------------------
    def _update_stats(self):

        rows = self.rows[-MAX_POINTS:]

        if not rows:
            self.var_points.set("0")
            self.var_last_energy.set("-")
            self.var_last_coherence.set("-")
            self.var_last_asym.set("-")
            self.var_last_resonance.set("-")
            self.var_pos.set("0")
            self.var_neg.set("0")
            self.var_zero.set("0")
            self.var_coh_mean.set("-")
            self.var_energy_mean.set("-")
            self.listbox.delete(0, tk.END)
            return

        last = rows[-1]

        pos = sum(1 for r in rows if r["asymmetry"] > 0)
        neg = sum(1 for r in rows if r["asymmetry"] < 0)
        zero = sum(1 for r in rows if r["asymmetry"] == 0)

        coh_mean = sum(r["coherence"] for r in rows) / len(rows)
        eng_mean = sum(r["energy"] for r in rows) / len(rows)

        self.var_points.set(str(len(rows)))
        self.var_last_energy.set(f"{last['energy']:.4f}")
        self.var_last_coherence.set(f"{last['coherence']:.4f}")
        self.var_last_asym.set(str(last["asymmetry"]))
        self.var_last_resonance.set(f"{last['resonance']:.4f}")
        self.var_pos.set(str(pos))
        self.var_neg.set(str(neg))
        self.var_zero.set(str(zero))
        self.var_coh_mean.set(f"{coh_mean:.4f}")
        self.var_energy_mean.set(f"{eng_mean:.4f}")

        self.listbox.delete(0, tk.END)
        for r in rows[-40:]:
            text = (
                f"#{r['index']:>5} | "
                f"eng={r['energy']:>7.4f} | "
                f"coh={r['coherence']:>7.4f} | "
                f"asym={r['asymmetry']:>2} | "
                f"res={r['resonance']:>7.4f}"
            )
            self.listbox.insert(tk.END, text)

    # --------------------------------------------------
    def _update_plot(self):

        rows = self.rows[-MAX_POINTS:]

        self.ax_energy.clear()
        self.ax_coherence.clear()
        self.ax_scatter.clear()

        self._apply_axis_style(self.ax_energy, "Energy Verlauf")
        self._apply_axis_style(self.ax_coherence, "Coherence Verlauf")
        self._apply_axis_style(self.ax_scatter, "Energy × Coherence")

        if not rows:
            self.canvas.draw_idle()
            return

        x = [r["index"] for r in rows]
        energy = [r["energy"] for r in rows]
        coherence = [r["coherence"] for r in rows]
        asym = [r["asymmetry"] for r in rows]
        resonance = [r["resonance"] for r in rows]

        self.ax_energy.plot(x, energy, linewidth=1.4)
        self.ax_energy.axhline(1.0, linewidth=0.9, linestyle="--", color=WARN)
        self.ax_energy.axhline(1.5, linewidth=0.9, linestyle=":", color=ACCENT)
        self.ax_energy.set_ylabel("energy", color=FG)

        self.ax_coherence.plot(x, coherence, linewidth=1.4)
        self.ax_coherence.axhline(0.0, linewidth=0.9, linestyle="--", color=FG_DIM)
        self.ax_coherence.axhline(1.0, linewidth=0.8, linestyle=":", color=GOOD)
        self.ax_coherence.axhline(-1.0, linewidth=0.8, linestyle=":", color=BAD)
        self.ax_coherence.set_ylim(-1.05, 1.05)
        self.ax_coherence.set_ylabel("coherence", color=FG)

        scatter_colors = []
        for value in asym:
            if value > 0:
                scatter_colors.append(GOOD)
            elif value < 0:
                scatter_colors.append(BAD)
            else:
                scatter_colors.append(WARN)

        self.ax_scatter.scatter(energy, coherence, s=[30 + (r * 18) for r in resonance], c=scatter_colors, alpha=0.75)
        self.ax_scatter.axvline(1.0, linewidth=0.9, linestyle="--", color=WARN)
        self.ax_scatter.axhline(0.0, linewidth=0.9, linestyle="--", color=FG_DIM)
        self.ax_scatter.set_xlabel("energy", color=FG)
        self.ax_scatter.set_ylabel("coherence", color=FG)
        self.ax_scatter.set_ylim(-1.05, 1.05)

        self.canvas.draw_idle()

    # --------------------------------------------------
    def _update_loop(self):

        self._read_if_changed()
        self._update_stats()
        self._update_plot()
        self.root.after(REFRESH_MS, self._update_loop)


# ==================================================
# MAIN
# ==================================================
def main():

    root = tk.Tk()
    app = CoherenceVisualGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
