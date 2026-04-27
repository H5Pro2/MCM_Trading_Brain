from __future__ import annotations

import argparse
import json
import math
import tkinter as tk
from datetime import datetime
from pathlib import Path

import matplotlib
matplotlib.use("TkAgg")
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.figure import Figure


# ==================================================
# CONFIG
# ==================================================
REFRESH_MS = 1
MAX_DRAW_NEURONS = 1000
GRID_SIZE = 220
LINK_NEIGHBORS = 4
LINK_MAX_DISTANCE = 0.115
LINK_LOCAL_RADIUS_FACTOR = 1.36
LINK_SMALL_FIELD_NEIGHBORS = 3
HEAT_SIGMA = 0.030
SAMPLE_ACTIVITY_FLOOR = 0.018
TRACE_DECAY = 0.90
CLUSTER_CONTOUR_LEVELS = (0.36, 0.54, 0.72)
INPUT_HOTSPOT_COUNT = 8
INPUT_HOTSPOT_MIN_STRENGTH = 0.035
ACTIVE_LINK_FLOOR = 0.16
ACTIVE_LINK_MAX_DRAW = 260
ACTIVE_LINK_MIN_DRAW = 36
BASE_LINK_MAX_DRAW = 900
AREAL_FLOW_MAX_MARKERS = 10
AREAL_FLOW_MIN_ACTIVITY = 0.075
AREAL_FLOW_RADIUS = 0.075

C = {
    "bg_root": "#0d0f13",
    "bg_panel": "#13161c",
    "bg_card": "#181c24",
    "bg_chart": "#0b0f16",
    "border": "#252a36",
    "border_hi": "#2e3548",
    "text_hi": "#e8eaf0",
    "text_med": "#8b92a8",
    "text_lo": "#4a5168",
    "text_label": "#5c6480",
    "inn_green": "#4caf78",
    "inn_orange": "#d4894a",
    "inn_red": "#c05050",
    "inn_blue": "#5b8dd9",
    "inn_purple": "#8b72be",
    "grid": "#1a1f2b",
}

HEAT_CMAP = LinearSegmentedColormap.from_list(
    "mcm_soft_heat",
    [
        "#000000",
        "#101724",
        "#183047",
        "#235364",
        "#367474",
        "#d4894a",
    ],
)

TRACE_CMAP = LinearSegmentedColormap.from_list(
    "mcm_trace_heat",
    [
        "#000000",
        "#0e1828",
        "#12334d",
        "#234f5a",
    ],
)

matplotlib.rcParams.update({
    "figure.facecolor": C["bg_card"],
    "axes.facecolor": C["bg_chart"],
    "axes.edgecolor": C["border"],
    "axes.labelcolor": C["text_med"],
    "axes.titlecolor": C["text_hi"],
    "xtick.color": C["text_lo"],
    "ytick.color": C["text_lo"],
    "grid.color": C["grid"],
    "grid.linewidth": 0.5,
    "text.color": C["text_med"],
    "font.family": "monospace",
    "font.size": 8,
})


# ==================================================
# HELPERS
# ==================================================
def safe_float(value, default: float = 0.0) -> float:
    try:
        return float(value)
    except Exception:
        return float(default)


# --------------------------------------------------
def safe_int(value, default: int = 0) -> int:
    try:
        return int(float(value))
    except Exception:
        return int(default)


# --------------------------------------------------
def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(float(low), min(float(high), float(value)))


# --------------------------------------------------
def safe_load_json(path: Path) -> dict:
    try:
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


# --------------------------------------------------
def fmt_ts(value) -> str:
    try:
        if value is None:
            return "–"

        ts = int(float(value))
        if ts > 10_000_000_000_000:
            ts = ts // 1000

        if ts > 10_000_000_000:
            dt = datetime.fromtimestamp(ts / 1000)
        else:
            dt = datetime.fromtimestamp(ts)

        return dt.strftime("%d.%m.%Y %H:%M:%S")
    except Exception:
        return "–"


# --------------------------------------------------
def fmt_num(value, digits: int = 3) -> str:
    try:
        return f"{float(value):.{digits}f}"
    except Exception:
        return "–"


# --------------------------------------------------
def numeric_color(value: float, invert: bool = False) -> str:
    v = clamp(value)
    if invert:
        v = 1.0 - v
    if v >= 0.67:
        return C["inn_green"]
    if v >= 0.34:
        return C["inn_orange"]
    return C["inn_blue"]


# --------------------------------------------------
def text_state_color(text: str) -> str:
    s = str(text or "").lower()
    if any(word in s for word in ["stress", "critical", "blocked", "over", "chaotic"]):
        return C["inn_red"]
    if any(word in s for word in ["observe", "wait", "hold", "neutral", "reorganizing"]):
        return C["inn_orange"]
    if any(word in s for word in ["stable", "active", "aligned", "ready", "settling"]):
        return C["inn_green"]
    return C["inn_blue"]


# ==================================================
# UI BLOCKS
# ==================================================
class CardFrame(tk.Frame):
    def __init__(self, parent, title: str = "", title_color: str | None = None, **kwargs):
        bg = kwargs.pop("bg", C["bg_card"])
        super().__init__(parent, bg=bg, highlightbackground=C["border"], highlightthickness=1, **kwargs)
        self.body = tk.Frame(self, bg=bg)

        if title:
            tk.Label(
                self,
                text=title.upper(),
                bg=bg,
                fg=title_color or C["text_label"],
                font=("Courier New", 8, "bold"),
                anchor="w",
                padx=8,
                pady=5,
            ).pack(fill="x")
            tk.Frame(self, bg=C["border"], height=1).pack(fill="x")

        self.body.pack(fill="both", expand=True)


# ==================================================
# MAIN GUI
# ==================================================
class MCMNeuronFieldGUI:

    def __init__(self, root: tk.Tk, base_dir: Path):
        self.root = root
        self.base_dir = Path(base_dir)
        self.inner_path = self.base_dir / "debug" / "bot_inner_snapshot.json"
        self.outcome_path = self.base_dir / "debug" / "trade_stats.json"
        self._after_id = None
        self._fixed_layout_cache: dict[int, np.ndarray] = {}
        self._link_cache: dict[int, list[tuple[int, int]]] = {}
        self._heat_memory = None
        self._heat_trace = None
        self._last_heat = None

        self.root.title("MCM Neuron Tissue Field")
        self.root.configure(bg=C["bg_root"])
        self.root.minsize(1200, 780)

        self._build_layout()
        self._refresh()

    # --------------------------------------------------
    def _build_layout(self):
        header = tk.Frame(self.root, bg=C["bg_panel"], highlightbackground=C["border"], highlightthickness=1)
        header.pack(fill="x", padx=6, pady=6)

        tk.Label(
            header,
            text="MCM NEURON TISSUE FIELD",
            bg=C["bg_panel"],
            fg=C["text_hi"],
            font=("Courier New", 14, "bold"),
            anchor="w",
        ).pack(side="left", padx=10, pady=8)

        self.lbl_status = tk.Label(
            header,
            text="INNER: –",
            bg=C["bg_panel"],
            fg=C["inn_blue"],
            font=("Courier New", 8, "bold"),
            anchor="e",
        )
        self.lbl_status.pack(side="right", padx=10, pady=8)

        self.lbl_outcome = tk.Label(
            header,
            text="OUTCOME: –",
            bg=C["bg_panel"],
            fg=C["text_med"],
            font=("Courier New", 8, "bold"),
            anchor="e",
        )
        self.lbl_outcome.pack(side="right", padx=10, pady=8)

        self.card_field = CardFrame(
            self.root,
            title="Neuronales Gewebe / Aktivitätsverarbeitung",
            title_color=C["inn_purple"],
            bg=C["bg_card"],
        )
        self.card_field.pack(fill="both", expand=True, padx=6, pady=(0, 6))

        content = tk.Frame(self.card_field.body, bg=C["bg_card"])
        content.pack(fill="both", expand=True)

        plot_frame = tk.Frame(content, bg=C["bg_card"])
        plot_frame.pack(side="left", fill="both", expand=True)

        side_panel = tk.Frame(content, bg=C["bg_panel"], highlightbackground=C["border"], highlightthickness=1, width=255)
        side_panel.pack(side="right", fill="y", padx=(6, 0))
        side_panel.pack_propagate(False)

        self.side_labels = {}
        self._build_side_panel(side_panel)

        self.fig = Figure(figsize=(13.0, 7.9), dpi=100)
        self.fig.subplots_adjust(left=0.025, right=0.985, top=0.91, bottom=0.035)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=plot_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    # --------------------------------------------------
    def _build_side_panel(self, parent: tk.Frame):
        sections = [
            ("FELD", ["tissue", "snapshot", "density", "stability", "load", "capacity"]),
            ("AKTIVITÄT", ["activity", "coupling", "external", "context_memory", "input_drive"]),
            ("TOPOLOGIE", ["topology_state", "topology_links", "topology_density", "topology_coherence", "topology_tension"]),
            ("VERBINDUNG", ["links", "active_links", "areal_flow", "hotspots"]),
            ("OUTCOME", ["trades", "winrate", "pnl", "attempts"]),
            ("ZUSTAND", ["reorganization"]),
        ]

        for section_title, keys in sections:
            tk.Label(
                parent,
                text=section_title,
                bg=C["bg_panel"],
                fg=C["inn_purple"],
                font=("Courier New", 8, "bold"),
                anchor="w",
            ).pack(fill="x", padx=8, pady=(8, 2))

            for key in keys:
                label = tk.Label(
                    parent,
                    text=f"{key}: –",
                    bg=C["bg_panel"],
                    fg=C["text_med"],
                    font=("Courier New", 8),
                    anchor="w",
                    justify="left",
                )
                label.pack(fill="x", padx=12, pady=1)
                self.side_labels[str(key)] = label

    # --------------------------------------------------
    def _set_side_value(self, key: str, value, color: str | None = None):
        label = dict(getattr(self, "side_labels", {}) or {}).get(str(key))
        if label is None:
            return None

        label.config(
            text=f"{key}: {value}",
            fg=color or C["text_med"],
        )
        return label

    # --------------------------------------------------
    def _read_inner_snapshot(self) -> dict:
        return safe_load_json(self.inner_path)

    # --------------------------------------------------
    def _read_outcome_snapshot(self) -> dict:
        return safe_load_json(self.outcome_path)

    # --------------------------------------------------
    def _resolve_outcome_state(self, stats: dict) -> dict:
        data = dict(stats or {})
        kpi = dict(data.get("kpi_summary", {}) or {})
        proof = dict(kpi.get("proof", {}) or {})

        trades = safe_int(data.get("trades", 0), 0)
        tp = safe_int(data.get("tp", 0), 0)
        sl = safe_int(data.get("sl", 0), 0)
        cancels = safe_int(data.get("cancels", 0), 0)
        attempts = safe_int(data.get("attempts", 0), 0)
        pnl = safe_float(data.get("pnl_netto", 0.0), 0.0)
        winrate = float(tp / trades) if trades > 0 else 0.0

        return {
            "trades": int(trades),
            "tp": int(tp),
            "sl": int(sl),
            "cancels": int(cancels),
            "attempts": int(attempts),
            "pnl_netto": float(pnl),
            "winrate": float(winrate),
            "regulatory_load": safe_float(proof.get("regulatory_load", 0.0), 0.0),
            "action_capacity": safe_float(proof.get("action_capacity", 0.0), 0.0),
            "survival_pressure": safe_float(proof.get("survival_pressure", 0.0), 0.0),
            "state_stability": safe_float(proof.get("state_stability", 0.0), 0.0),
        }

    # --------------------------------------------------
    def _resolve_neuron_points(self, inner: dict) -> list[dict]:
        inner_field = dict(inner.get("inner_field_perception_state", {}) or {})

        population = [
            dict(item or {})
            for item in list(inner_field.get("field_neuron_population", []) or [])
            if isinstance(item, dict)
        ]

        if population:
            return population[:MAX_DRAW_NEURONS]

        agents = [
            dict(item or {})
            for item in list(inner_field.get("field_agent_points", []) or [])
            if isinstance(item, dict)
        ]
        return agents[:MAX_DRAW_NEURONS]

    # --------------------------------------------------
    def _resolve_tissue_count(self, inner: dict, points: list[dict]) -> int:
        inner_field = dict(inner.get("inner_field_perception_state", {}) or {})
        configured_count = safe_int(inner_field.get("field_neuron_count", 0), 0)
        if configured_count <= 0:
            configured_count = safe_int(inner_field.get("field_agent_count", 0), 0)
        if configured_count <= 0:
            configured_count = len(points)
        return max(1, min(MAX_DRAW_NEURONS, int(configured_count or len(points) or 1)))

    # --------------------------------------------------
    def _fixed_tissue_layout(self, count: int) -> np.ndarray:
        n = max(1, int(count or 1))
        if n in self._fixed_layout_cache:
            return self._fixed_layout_cache[n]

        rng = np.random.default_rng(104729 + n)
        cols = int(math.ceil(math.sqrt(n * 1.82)))
        rows = int(math.ceil(n / max(1, cols)))

        points = []
        for row in range(rows):
            for col in range(cols):
                if len(points) >= n:
                    break

                base_x = col / max(1, cols - 1)
                base_y = row / max(1, rows - 1)

                if row % 2:
                    base_x += 0.5 / max(2, cols)

                jitter_x = rng.normal(0.0, 0.010)
                jitter_y = rng.normal(0.0, 0.012)
                x = max(0.020, min(0.980, base_x + jitter_x))
                y = max(0.030, min(0.970, base_y + jitter_y))
                points.append((float(x), float(y)))

        arr = np.asarray(points, dtype=float)
        self._fixed_layout_cache[n] = arr
        return arr

    # --------------------------------------------------
    def _links_for_layout(self, layout: np.ndarray) -> list[tuple[int, int]]:
        n = int(len(layout))
        if n in self._link_cache:
            return self._link_cache[n]

        links = set()
        if n <= 1:
            self._link_cache[n] = []
            return []

        nearest_distances = []
        for index in range(n):
            delta = layout - layout[index]
            dist = np.sqrt(np.sum(delta * delta, axis=1))
            order = np.argsort(dist)
            for neighbor in order:
                ni = int(neighbor)
                if ni == index:
                    continue
                nearest_distances.append(float(dist[ni]))
                break

        local_spacing = float(np.median(nearest_distances)) if nearest_distances else float(LINK_MAX_DISTANCE)
        dynamic_radius = min(
            float(LINK_MAX_DISTANCE),
            max(local_spacing * float(LINK_LOCAL_RADIUS_FACTOR), local_spacing + 0.010),
        )
        max_neighbors = max(
            1,
            min(int(LINK_NEIGHBORS), int(LINK_SMALL_FIELD_NEIGHBORS) if n <= 120 else int(LINK_NEIGHBORS)),
        )

        for index in range(n):
            delta = layout - layout[index]
            dist = np.sqrt(np.sum(delta * delta, axis=1))
            order = np.argsort(dist)
            linked = 0

            for neighbor in order:
                ni = int(neighbor)
                if ni == index:
                    continue

                link_distance = float(dist[ni])
                if link_distance > dynamic_radius:
                    break

                a, b = sorted((index, ni))
                links.add((a, b))
                linked += 1

                if linked >= max_neighbors:
                    break

        resolved = sorted(links)
        self._link_cache[n] = resolved
        return resolved

    # --------------------------------------------------
    def _activity_values(self, points: list[dict], count: int) -> np.ndarray:
        source_values = []
        for item in list(points or []):
            activation = clamp(safe_float(item.get("activation", 0.0)))
            impulse = clamp(safe_float(item.get("external_impulse_norm", 0.0)) / 0.8)
            context_memory = clamp(safe_float(item.get("context_memory_impulse_norm", 0.0)) / 0.8)
            coupling = clamp(safe_float(item.get("coupling_norm", 0.0)) / 0.8)
            pressure = clamp(safe_float(item.get("regulation_pressure", 0.0)))
            source_values.append(clamp((activation * 0.52) + (impulse * 0.20) + (context_memory * 0.12) + (coupling * 0.10) + (pressure * 0.06)))

        if not source_values:
            return np.zeros(max(1, int(count or 1)), dtype=float)

        source = np.asarray(source_values, dtype=float)
        target_count = max(1, int(count or len(source)))

        if len(source) == target_count:
            return source

        old_x = np.linspace(0.0, 1.0, len(source))
        new_x = np.linspace(0.0, 1.0, target_count)
        interpolated = np.interp(new_x, old_x, source)
        return np.asarray(interpolated, dtype=float)

    # --------------------------------------------------
    def _metric_values(self, points: list[dict], count: int, key: str, scale: float = 1.0) -> np.ndarray:
        source_values = []
        for item in list(points or []):
            source_values.append(clamp(safe_float(item.get(key, 0.0)) / max(1e-9, float(scale or 1.0))))

        if not source_values:
            return np.zeros(max(1, int(count or 1)), dtype=float)

        source = np.asarray(source_values, dtype=float)
        target_count = max(1, int(count or len(source)))

        if len(source) == target_count:
            return source

        old_x = np.linspace(0.0, 1.0, len(source))
        new_x = np.linspace(0.0, 1.0, target_count)
        interpolated = np.interp(new_x, old_x, source)
        return np.asarray(interpolated, dtype=float)

    # --------------------------------------------------
    def _input_drive_strength(self, inner: dict, inner_field: dict) -> float:
        outer = dict(inner.get("outer_visual_perception_state", {}) or {})
        perception = dict(inner.get("perception_state", {}) or {})
        processing = dict(inner.get("processing_state", {}) or {})

        return clamp(
            (abs(safe_float(inner_field.get("field_neuron_external_impulse_norm_mean", 0.0))) * 0.30)
            + (abs(safe_float(inner_field.get("field_neuron_context_memory_impulse_norm_mean", 0.0))) * 0.12)
            + (safe_float(outer.get("signal_relevance", 0.0)) * 0.20)
            + (safe_float(outer.get("visual_contrast", 0.0)) * 0.12)
            + (safe_float(perception.get("novelty_score", 0.0)) * 0.10)
            + (safe_float(processing.get("processing_intensity", 0.0)) * 0.08)
            + (safe_float(inner_field.get("replay_impulse", 0.0)) * 0.08)
        )

    # --------------------------------------------------
    def _input_hotspot_indices(self, points: list[dict], activity: np.ndarray, input_drive: float) -> np.ndarray:
        if len(activity) <= 0:
            return np.asarray([], dtype=int)

        source_scores = np.zeros(len(activity), dtype=float)
        usable_points = list(points or [])[:len(activity)]

        for index, item in enumerate(usable_points):
            external = clamp(safe_float(item.get("external_impulse_norm", 0.0)) / 0.8)
            pressure = clamp(safe_float(item.get("regulation_pressure", 0.0)))
            activation = clamp(safe_float(item.get("activation", 0.0)))
            source_scores[index] = (external * 0.56) + (pressure * 0.22) + (activation * 0.22)

        if float(np.max(source_scores)) <= 1e-9:
            source_scores = np.asarray(activity, dtype=float)

        if float(np.max(source_scores)) <= max(INPUT_HOTSPOT_MIN_STRENGTH, input_drive * 0.35):
            return np.asarray([], dtype=int)

        count = min(INPUT_HOTSPOT_COUNT, len(source_scores))
        return np.argsort(source_scores)[-count:]

    # --------------------------------------------------
    def _draw_input_hotspots(self, layout: np.ndarray, activity: np.ndarray, hotspot_indices: np.ndarray, input_drive: float) -> int:
        if hotspot_indices is None or len(hotspot_indices) <= 0:
            return 0

        indices = np.asarray(hotspot_indices, dtype=int)
        values = np.asarray(activity[indices], dtype=float)
        sizes = 34.0 + (values * 96.0) + (float(input_drive) * 38.0)

        self.ax.scatter(
            layout[indices, 0],
            layout[indices, 1],
            s=sizes,
            c=[C["inn_orange"] for _ in indices],
            alpha=0.045 + (0.055 * clamp(input_drive)),
            linewidths=0.0,
            zorder=9,
        )
        self.ax.scatter(
            layout[indices, 0],
            layout[indices, 1],
            s=4.0 + (values * 10.0),
            c=[C["inn_orange"] for _ in indices],
            alpha=0.36,
            edgecolors=C["border_hi"],
            linewidths=0.12,
            zorder=10,
        )
        return int(len(indices))

    # --------------------------------------------------
    def _draw_areal_flow_markers(self, layout: np.ndarray, activity: np.ndarray, heat: np.ndarray) -> int:
        if len(layout) <= 1 or len(activity) <= 1:
            return 0

        activity_mean = float(np.mean(activity)) if len(activity) else 0.0
        threshold = max(float(AREAL_FLOW_MIN_ACTIVITY), activity_mean * 1.18)
        candidates = [int(idx) for idx in np.argsort(activity)[::-1] if float(activity[int(idx)]) >= threshold]
        centers = []

        for idx in candidates:
            point = layout[int(idx)]
            too_close = False
            for existing in centers:
                dist = float(np.linalg.norm(point - layout[int(existing)]))
                if dist < AREAL_FLOW_RADIUS * 1.35:
                    too_close = True
                    break
            if too_close:
                continue
            centers.append(int(idx))
            if len(centers) >= int(AREAL_FLOW_MAX_MARKERS):
                break

        if not centers:
            return 0

        markers = []
        widths = []
        for idx in centers:
            point = layout[int(idx)]
            delta = layout - point
            dist = np.sqrt(np.sum(delta * delta, axis=1))
            mask = (dist > 1e-9) & (dist <= float(AREAL_FLOW_RADIUS) * 1.8)
            if not np.any(mask):
                continue

            weights = np.maximum(activity - float(activity[int(idx)]) * 0.45, 0.0) * mask.astype(float)
            if float(np.sum(weights)) <= 1e-9:
                neighbor = int(np.argsort(dist)[1])
                direction = layout[neighbor] - point
            else:
                target = np.average(layout, axis=0, weights=weights)
                direction = target - point

            norm = float(np.linalg.norm(direction))
            if norm <= 1e-9:
                continue

            unit = direction / norm
            length = 0.018 + (clamp(activity[int(idx)]) * 0.035)
            start_point = point - (unit * length * 0.38)
            end_point = point + (unit * length * 0.62)
            markers.append([start_point, end_point])
            widths.append(0.42 + (clamp(activity[int(idx)]) * 1.20))

        if not markers:
            return 0

        self.ax.add_collection(
            LineCollection(
                markers,
                colors=C["inn_blue"],
                linewidths=widths,
                alpha=0.34,
                zorder=6.4,
            )
        )
        return int(len(markers))

    # --------------------------------------------------
    def _draw_active_links(self, layout: np.ndarray, links: list[tuple[int, int]], activity: np.ndarray, coupling: np.ndarray, external: np.ndarray, hotspot_indices: np.ndarray) -> int:
        if not links or len(activity) <= 0:
            return 0

        activity_mean = float(np.mean(activity)) if len(activity) else 0.0
        activity_max = float(np.max(activity)) if len(activity) else 0.0
        hotspot_source = list(hotspot_indices) if hotspot_indices is not None else []
        hotspot_set = set(int(item) for item in hotspot_source if int(item) < len(activity))
        scored_links = []

        for a, b in list(links or []):
            ai = int(a)
            bi = int(b)
            if ai >= len(activity) or bi >= len(activity):
                continue

            link_activity = float((activity[ai] + activity[bi]) * 0.5)
            link_coupling = float((coupling[ai] + coupling[bi]) * 0.5) if len(coupling) > max(ai, bi) else 0.0
            link_external = float((external[ai] + external[bi]) * 0.5) if len(external) > max(ai, bi) else 0.0
            hotspot_boost = 0.030 if ai in hotspot_set or bi in hotspot_set else 0.0
            strength = float((link_activity * 0.48) + (link_coupling * 0.38) + (link_external * 0.11) + hotspot_boost)
            scored_links.append((strength, [layout[ai], layout[bi]]))

        if not scored_links:
            return 0

        scored_links = sorted(scored_links, key=lambda item: item[0], reverse=True)
        base_payload = scored_links[:min(int(BASE_LINK_MAX_DRAW), len(scored_links))]
        base_lines = [line for _, line in base_payload]

        if base_lines:
            self.ax.add_collection(
                LineCollection(
                    base_lines,
                    colors="#2f4058",
                    linewidths=0.22,
                    alpha=0.24,
                    zorder=4.8,
                )
            )

        strengths = np.asarray([float(value) for value, _ in scored_links], dtype=float)
        percentile_threshold = float(np.percentile(strengths, 78.0)) if len(strengths) else 0.0
        dynamic_threshold = max(float(ACTIVE_LINK_FLOOR) * 0.34, activity_mean * 0.72, percentile_threshold)
        active_payload = [(value, line) for value, line in scored_links if float(value) >= dynamic_threshold]

        min_active = min(int(ACTIVE_LINK_MIN_DRAW), len(scored_links))
        if len(active_payload) < min_active:
            active_payload = scored_links[:min_active]

        active_payload = active_payload[:min(int(ACTIVE_LINK_MAX_DRAW), len(active_payload))]
        if not active_payload:
            return 0

        field_lines = [line for _, line in active_payload]
        field_values = [value for value, _ in active_payload]
        max_strength = max(max(field_values), 1e-9)
        widths = [0.36 + (clamp(value / max_strength) * 1.55) for value in field_values]

        self.ax.add_collection(
            LineCollection(
                field_lines,
                colors=C["inn_blue"],
                linewidths=widths,
                alpha=0.42 + (activity_max * 0.24),
                zorder=6.2,
            )
        )

        return int(len(active_payload))

    # --------------------------------------------------
    def _build_heat_field(self, layout: np.ndarray, activity: np.ndarray) -> np.ndarray:
        grid_x = np.linspace(0.0, 1.0, GRID_SIZE)
        grid_y = np.linspace(0.0, 1.0, GRID_SIZE)
        xx, yy = np.meshgrid(grid_x, grid_y)
        heat = np.zeros_like(xx, dtype=float)

        if len(layout) <= 0:
            return heat

        active_count = min(180, len(activity))
        active_indices = np.argsort(activity)[-active_count:]
        sigma2 = float(HEAT_SIGMA * HEAT_SIGMA)

        for idx in active_indices:
            strength = float(activity[int(idx)] or 0.0)
            if strength <= SAMPLE_ACTIVITY_FLOOR:
                continue
            x, y = layout[int(idx)]
            dist2 = ((xx - x) ** 2) + ((yy - y) ** 2)
            heat += strength * np.exp(-dist2 / (2.0 * sigma2))

        max_value = float(np.max(heat)) if heat.size else 0.0
        if max_value > 1e-9:
            heat = heat / max_value

        if self._heat_memory is None or self._heat_memory.shape != heat.shape:
            self._heat_memory = heat
        else:
            self._heat_memory = (self._heat_memory * 0.64) + (heat * 0.36)

        current_heat = np.asarray(self._heat_memory, dtype=float)
        if self._heat_trace is None or self._heat_trace.shape != current_heat.shape:
            self._heat_trace = current_heat.copy()
        else:
            self._heat_trace = np.maximum(self._heat_trace * TRACE_DECAY, current_heat * 0.86)

        return current_heat

    # --------------------------------------------------
    # --------------------------------------------------
    def _draw_cluster_contours(self, heat: np.ndarray):
        if heat is None or heat.size <= 0:
            return None

        max_heat = float(np.max(heat)) if heat.size else 0.0
        if max_heat <= 0.08:
            return None

        x = np.linspace(0.0, 1.0, heat.shape[1])
        y = np.linspace(0.0, 1.0, heat.shape[0])
        levels = [level for level in CLUSTER_CONTOUR_LEVELS if level < max_heat]
        if not levels:
            return None

        return self.ax.contour(
            x,
            y,
            heat,
            levels=levels,
            colors=[C["inn_blue"], C["inn_green"], C["inn_orange"]][:len(levels)],
            linewidths=[0.45, 0.55, 0.75][:len(levels)],
            alpha=0.26,
            zorder=3,
        )

    # --------------------------------------------------
    def _draw_neuron_tissue(self, inner: dict, outcome: dict | None = None):
        self.ax.clear()
        self.ax.set_facecolor(C["bg_chart"])
        self.ax.set_title("Neuronales Gewebe · Input-Hotspots / lokale Kopplung / Areal-Flow / Heat-Trace")
        self.ax.set_xlim(0.0, 1.0)
        self.ax.set_ylim(0.0, 1.0)
        self.ax.set_aspect("auto")
        self.ax.set_xticks([])
        self.ax.set_yticks([])

        inner_field = dict(inner.get("inner_field_perception_state", {}) or {})
        field_state = dict(inner.get("field_state", {}) or {})
        points = self._resolve_neuron_points(inner)
        source_count = len(points)
        tissue_count = self._resolve_tissue_count(inner, points)

        if tissue_count <= 0:
            self._set_side_value("tissue_neurons", 0)
            self._set_side_value("snapshot_points", source_count)
            self.canvas.draw_idle()
            return

        layout = self._fixed_tissue_layout(tissue_count)
        links = self._links_for_layout(layout)
        activity = self._activity_values(points, tissue_count)
        coupling = self._metric_values(points, tissue_count, "coupling_norm", scale=0.8)
        external = self._metric_values(points, tissue_count, "external_impulse_norm", scale=0.8)
        context_memory = self._metric_values(points, tissue_count, "context_memory_impulse_norm", scale=0.8)
        heat = self._build_heat_field(layout, activity)

        field_density = clamp(field_state.get("field_density", 0.0))
        field_stability = clamp(field_state.get("field_stability", 0.0))
        regulatory_load = clamp(field_state.get("regulatory_load", 0.0))
        action_capacity = clamp(field_state.get("action_capacity", 0.0))
        activity_mean = float(np.mean(activity)) if len(activity) else 0.0
        activity_max = float(np.max(activity)) if len(activity) else 0.0
        coupling_mean = float(np.mean(coupling)) if len(coupling) else 0.0
        external_mean = float(np.mean(external)) if len(external) else 0.0
        context_memory_mean = float(np.mean(context_memory)) if len(context_memory) else 0.0
        topology_state = dict(inner_field.get("field_topology_state", {}) or {})
        topology_cluster_links = safe_int(inner_field.get("field_topology_cluster_link_count", topology_state.get("cluster_link_count", 0)), 0)
        topology_areal_links = safe_int(inner_field.get("field_topology_areal_link_count", topology_state.get("areal_link_count", 0)), 0)
        topology_link_density = clamp(safe_float(inner_field.get("field_topology_link_density", topology_state.get("link_density", 0.0))))
        topology_coherence = clamp(safe_float(inner_field.get("field_topology_coherence", topology_state.get("topology_coherence", 0.0))))
        topology_tension = clamp(safe_float(inner_field.get("field_topology_tension", topology_state.get("topology_tension", 0.0))))
        topology_state_label = str(inner_field.get("field_topology_state_label", topology_state.get("topology_state_label", "sparse_topology")) or "sparse_topology")
        reorganization_direction = str(inner_field.get("field_reorganization_direction", "stable") or "stable")
        reorg_color = text_state_color(reorganization_direction)
        outcome_state = self._resolve_outcome_state(dict(outcome or {}))

        if self._heat_trace is not None:
            self.ax.imshow(
                self._heat_trace,
                extent=(0.0, 1.0, 0.0, 1.0),
                origin="lower",
                cmap=TRACE_CMAP,
                alpha=0.34,
                interpolation="bicubic",
                aspect="auto",
                zorder=1,
            )

        self.ax.imshow(
            heat,
            extent=(0.0, 1.0, 0.0, 1.0),
            origin="lower",
            cmap=HEAT_CMAP,
            alpha=0.34,
            interpolation="bicubic",
            aspect="auto",
            zorder=2,
        )

        self._draw_cluster_contours(heat)

        input_drive = self._input_drive_strength(inner, inner_field)
        hotspot_indices = self._input_hotspot_indices(points, activity, input_drive)
        areal_flow_count = self._draw_areal_flow_markers(layout, activity, heat)
        active_link_count = self._draw_active_links(layout, links, activity, coupling, external, hotspot_indices)

        node_sizes = 2.4 + (activity * 14.0)
        glow_sizes = 18.0 + (activity * 95.0)
        node_colors = [numeric_color(v) for v in activity]

        self.ax.scatter(
            layout[:, 0],
            layout[:, 1],
            s=glow_sizes,
            c=node_colors,
            alpha=0.07 + (activity * 0.20),
            linewidths=0.0,
            zorder=7,
        )
        self.ax.scatter(
            layout[:, 0],
            layout[:, 1],
            s=node_sizes,
            c=node_colors,
            alpha=0.78,
            edgecolors="#102030",
            linewidths=0.16,
            zorder=8,
        )

        top_count = min(36, tissue_count)
        if top_count > 0:
            top_indices = np.argsort(activity)[-top_count:]
            self.ax.scatter(
                layout[top_indices, 0],
                layout[top_indices, 1],
                s=70 + (activity[top_indices] * 220),
                c=[numeric_color(v) for v in activity[top_indices]],
                alpha=0.11 + (activity[top_indices] * 0.16),
                linewidths=0.0,
                zorder=8,
            )

        input_hotspot_count = self._draw_input_hotspots(layout, activity, hotspot_indices, input_drive)

        self._set_side_value("tissue", tissue_count)
        self._set_side_value("snapshot", source_count)
        self._set_side_value("density", fmt_num(field_density))
        self._set_side_value("stability", fmt_num(field_stability), numeric_color(field_stability))
        self._set_side_value("load", fmt_num(regulatory_load), numeric_color(regulatory_load, invert=True))
        self._set_side_value("capacity", fmt_num(action_capacity), numeric_color(action_capacity))
        self._set_side_value("activity", fmt_num(activity_mean))
        self._set_side_value("coupling", fmt_num(coupling_mean))
        self._set_side_value("external", fmt_num(external_mean))
        self._set_side_value("context_memory", fmt_num(context_memory_mean), numeric_color(context_memory_mean))
        self._set_side_value("input_drive", fmt_num(input_drive))
        self._set_side_value("topology_state", topology_state_label, text_state_color(topology_state_label))
        self._set_side_value("topology_links", f"{topology_cluster_links}/{topology_areal_links}")
        self._set_side_value("topology_density", fmt_num(topology_link_density), numeric_color(topology_link_density))
        self._set_side_value("topology_coherence", fmt_num(topology_coherence), numeric_color(topology_coherence))
        self._set_side_value("topology_tension", fmt_num(topology_tension), numeric_color(topology_tension, invert=True))
        self._set_side_value("links", len(links))
        self._set_side_value("active_links", active_link_count, C["inn_blue"])
        self._set_side_value("areal_flow", areal_flow_count)
        self._set_side_value("hotspots", input_hotspot_count, C["inn_orange"])
        self._set_side_value("trades", outcome_state["trades"])
        self._set_side_value("winrate", fmt_num(outcome_state["winrate"]), numeric_color(outcome_state.get("winrate", 0.0)))
        self._set_side_value("pnl", fmt_num(outcome_state["pnl_netto"]))
        self._set_side_value("attempts", outcome_state["attempts"])
        self._set_side_value("reorganization", reorganization_direction, reorg_color)

        self.canvas.draw_idle()

    # --------------------------------------------------
    def _refresh(self):
        inner = self._read_inner_snapshot()
        outcome = self._read_outcome_snapshot()
        outcome_state = self._resolve_outcome_state(outcome)
        self.lbl_status.config(text=f"INNER: {fmt_ts(inner.get('timestamp'))}")
        self.lbl_outcome.config(
            text=(
                f"OUTCOME: trades={outcome_state['trades']} "
                f"pnl={fmt_num(outcome_state['pnl_netto'])} "
                f"win={fmt_num(outcome_state['winrate'])}"
            ),
            fg=numeric_color(outcome_state.get("winrate", 0.0)),
        )

        if inner:
            self._draw_neuron_tissue(inner, outcome=outcome)

        self._after_id = self.root.after(REFRESH_MS, self._refresh)

    # --------------------------------------------------
    def run(self):
        self.root.mainloop()


# ==================================================
# MAIN
# ==================================================
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default=".", help="Projektbasis mit debug/bot_inner_snapshot.json")
    args = parser.parse_args()

    root = tk.Tk()
    app = MCMNeuronFieldGUI(root=root, base_dir=Path(args.base))
    app.run()


if __name__ == "__main__":
    main()
