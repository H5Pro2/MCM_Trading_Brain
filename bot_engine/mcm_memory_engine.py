# ==================================================
# mcm_memor_engine.py
# Dynamisches MCM-Gedächtnis
# ==================================================

import json
import os
import random
from typing import Dict, Any, List, Optional
from config import Config

import numpy as np


class RegimeNode:

    # --------------------------------------------------
    # INIT
    # --------------------------------------------------
    def __init__(self, node_id: int, center: List[float], side_stats=None, visits: int = 1):

        self.node_id = int(node_id)
        self.center = [float(x) for x in center]
        self.visits = int(visits)

        if side_stats is None:
            side_stats = {
                "LONG": {
                    "tp": 0,
                    "sl": 0,
                    "rr_sum": 0.0,
                    "rr_count": 0,
                    "entry_shift_sum": 0.0,
                    "entry_shift_count": 0,
                },
                "SHORT": {
                    "tp": 0,
                    "sl": 0,
                    "rr_sum": 0.0,
                    "rr_count": 0,
                    "entry_shift_sum": 0.0,
                    "entry_shift_count": 0,
                },
            }

        self.side_stats = side_stats

    # --------------------------------------------------
    # DISTANCE
    # --------------------------------------------------
    def distance(self, vector: List[float]) -> float:

        a = np.array(self.center, dtype=float)
        b = np.array(vector, dtype=float)

        if len(a) != len(b):
            m = min(len(a), len(b))
            a = a[:m]
            b = b[:m]

        return float(np.linalg.norm(a - b))

    # --------------------------------------------------
    # ADAPT
    # --------------------------------------------------
    def adapt(self, vector: List[float], lr: float = 0.08):

        self.visits += 1

        for i, value in enumerate(vector):
            self.center[i] = float(
                self.center[i] + (lr * (float(value) - self.center[i]))
            )

    # --------------------------------------------------
    # TO_DICT
    # --------------------------------------------------
    def to_dict(self) -> Dict[str, Any]:

        return {
            "node_id": self.node_id,
            "center": self.center,
            "visits": self.visits,
            "side_stats": self.side_stats,
        }

    # --------------------------------------------------
    # FROM_DICT
    # --------------------------------------------------
    @classmethod
    def from_dict(cls, data: Dict[str, Any]):

        return cls(
            node_id=data.get("node_id", 0),
            center=data.get("center", []),
            side_stats=data.get("side_stats"),
            visits=data.get("visits", 1),
        )
        
class MCMMemoryEngine:

    # --------------------------------------------------
    # INIT
    # --------------------------------------------------
    def __init__(self, path="bot_memory/mcm_memory_engine.json"):

        self.path = path

        os.makedirs("bot_memory", exist_ok=True)

        self.sensory_buffer = []
        self.episodes = []
        self.regime_nodes = []
        self.transition_graph = {}
        self.reward_traces = []
        self.attractor_state = {
            "name": "neutral",
            "node_id": None,
        }

        self.max_buffer = 2000
        self.max_episodes = 500
        self.max_reward_traces = 500
        self.node_match_threshold = 0.85
        self.next_node_id = 1
        self.last_node_id = None
        self.active_episode = None

        self._load()

    # --------------------------------------------------
    # LOAD
    # --------------------------------------------------
    def _load(self):

        if not os.path.exists(self.path):
            return

        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.sensory_buffer = data.get("sensory_buffer", [])
            self.episodes = data.get("episodes", [])
            self.transition_graph = data.get("transition_graph", {})
            self.reward_traces = data.get("reward_traces", [])
            self.attractor_state = data.get(
                "attractor_state",
                {"name": "neutral", "node_id": None},
            )
            self.next_node_id = int(data.get("next_node_id", 1) or 1)
            self.last_node_id = data.get("last_node_id")

            self.regime_nodes = [
                RegimeNode.from_dict(item)
                for item in data.get("regime_nodes", [])
                if isinstance(item, dict)
            ]

        except Exception:
            self.sensory_buffer = []
            self.episodes = []
            self.regime_nodes = []
            self.transition_graph = {}
            self.reward_traces = []
            self.attractor_state = {
                "name": "neutral",
                "node_id": None,
            }
            self.next_node_id = 1
            self.last_node_id = None
            self.active_episode = None

    # --------------------------------------------------
    # SAVE
    # --------------------------------------------------
    def _save(self):

        try:

            data = {
                "sensory_buffer": self.sensory_buffer,
                "episodes": self.episodes,
                "regime_nodes": [node.to_dict() for node in self.regime_nodes],
                "transition_graph": self.transition_graph,
                "reward_traces": self.reward_traces,
                "attractor_state": self.attractor_state,
                "next_node_id": self.next_node_id,
                "last_node_id": self.last_node_id,
            }

            tmp_path = self.path + ".tmp"

            with open(tmp_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)

            os.replace(tmp_path, self.path)

        except Exception:
                pass

    # --------------------------------------------------
    # STATE VECTOR
    # --------------------------------------------------
    def _state_vector(self, state: Dict[str, Any]) -> List[float]:

            energy = float(state.get("energy", 0.0) or 0.0)
            coherence = float(state.get("coherence", 0.0) or 0.0)
            asymmetry = float(state.get("asymmetry", 0) or 0)
            resonance = float(state.get("resonance", 0.0) or 0.0)

            prev_energy = 0.0
            prev_coherence = 0.0
            prev2_energy = 0.0
            prev2_coherence = 0.0

            if len(self.sensory_buffer) >= 1:
                last = self.sensory_buffer[-1]
                prev_energy = float(last.get("energy", 0.0))
                prev_coherence = float(last.get("coherence", 0.0))

            if len(self.sensory_buffer) >= 2:
                last2 = self.sensory_buffer[-2]
                prev2_energy = float(last2.get("energy", 0.0))
                prev2_coherence = float(last2.get("coherence", 0.0))

            energy_gradient = energy - prev_energy
            coherence_gradient = coherence - prev_coherence

            energy_trend = prev_energy - prev2_energy
            coherence_trend = prev_coherence - prev2_coherence

            #zone = hier soll coh_zone übergeben werden das muss noch eingebaut werden

            coh_zone = float(state.get("coh_zone", 0.0) or 0.0)

            side_raw = str(state.get("side", "NONE")).upper().strip()
            if side_raw == "LONG":
                side = 1.0
            elif side_raw == "SHORT":
                side = -1.0
            else:
                side = 0.0

            # --------------------------------------------------
            # STRUCTURE TYPE
            # --------------------------------------------------
            structure_type = str(state.get("structure_type", "NONE"))

            if structure_type == "HH":
                structure_val = 1.0
            elif structure_type == "HL":
                structure_val = 0.5
            elif structure_type == "LH":
                structure_val = -0.5
            elif structure_type == "LL":
                structure_val = -1.0
            else:
                structure_val = 0.0

            structure_strength = float(state.get("structure_strength", 0.0) or 0.0)
            structure_age = float(state.get("structure_age", 0.0) or 0.0)

            # --------------------------------------------------
            # NORMALIZATION
            # --------------------------------------------------
            energy = energy / 3.0
            coherence = coherence
            asymmetry = asymmetry / 3.0
            resonance = resonance

            energy_gradient = energy_gradient / 2.0
            coherence_gradient = coherence_gradient / 2.0

            energy_trend = energy_trend / 2.0
            coherence_trend = coherence_trend / 2.0

            structure_strength = min(structure_strength / 5.0, 1.0)
            structure_age = min(structure_age / 50.0, 1.0)

            return [
                energy,
                coherence,
                asymmetry,
                resonance,
                energy_gradient,
                coherence_gradient,
                energy_trend,
                coherence_trend,
                coh_zone,
                side,
                structure_val,
                structure_strength,
                structure_age,
            ]

    # --------------------------------------------------
    # FIND BEST NODE
    # --------------------------------------------------
    def _find_best_node(self, vector: List[float]) -> Optional[RegimeNode]:

        if not self.regime_nodes:
            return None

        best_node = None
        best_dist = None

        for node in self.regime_nodes:
            dist = node.distance(vector)

            if best_dist is None or dist < best_dist:
                best_dist = dist
                best_node = node

        if best_dist is None:
            return None

        if best_dist <= self.node_match_threshold:
            return best_node

        return None

    # --------------------------------------------------
    # CREATE NODE
    # --------------------------------------------------
    def _create_node(self, vector: List[float]) -> RegimeNode:

        node = RegimeNode(
            node_id=self.next_node_id,
            center=vector,
        )

        self.next_node_id += 1
        self.regime_nodes.append(node)

        return node

    # --------------------------------------------------
    # ADD TRANSITION
    # --------------------------------------------------
    def _add_transition(self, from_node_id: int, to_node_id: int):

        if from_node_id is None or to_node_id is None:
            return

        if from_node_id == to_node_id:
            return

        from_key = str(from_node_id)
        to_key = str(to_node_id)

        if from_key not in self.transition_graph:
            self.transition_graph[from_key] = {}

        if to_key not in self.transition_graph[from_key]:
            self.transition_graph[from_key][to_key] = {
                "count": 0,
                "tp": 0,
                "sl": 0,
            }

        self.transition_graph[from_key][to_key]["count"] += 1

    # --------------------------------------------------
    # ATTRACTOR FROM NODE
    # --------------------------------------------------
    def _derive_attractor(self, node: Optional[RegimeNode]) -> str:

        if node is None:
            return "neutral"

        energy = float(node.center[0])
        coherence = float(node.center[1])
        resonance = float(node.center[3])

        if energy <= -1.4:
            return "defense"

        if resonance < 0.35:
            return "analysis"

        if coherence > 0.2 and energy >= 0.4:
            return "explore"

        if coherence < -0.2 and energy >= 0.4:
            return "analysis"

        return "cooperate"

    # --------------------------------------------------
    # RECORD STATE
    # --------------------------------------------------
    def record_state(self, state: Dict[str, Any]) -> Dict[str, Any]:

        vector = self._state_vector(state)

        buffer_item = {
            "energy": float(state.get("energy", 0.0) or 0.0),
            "coherence": float(state.get("coherence", 0.0) or 0.0),
            "asymmetry": int(state.get("asymmetry", 0) or 0),
            "resonance": float(state.get("resonance", 0.0) or 0.0),
            "coh_zone": float(state.get("coh_zone", 0.0) or 0.0),

            "structure_type": state.get("structure_type"),
            "structure_strength": state.get("structure_strength"),
            "structure_age": state.get("structure_age"),

            "side": str(state.get("side", "NONE")),
            "timestamp": state.get("timestamp"),
        }

        self.sensory_buffer.append(buffer_item)

        if len(self.sensory_buffer) > self.max_buffer:
            self.sensory_buffer = self.sensory_buffer[-self.max_buffer:]

        node = self._find_best_node(vector)

        if node is None:
            node = self._create_node(vector)
        else:
            node.adapt(vector)

        self._add_transition(self.last_node_id, node.node_id)

        self.last_node_id = node.node_id

        # --------------------------------------------------
        # MEMORY STABILIZATION
        # --------------------------------------------------
        if len(self.regime_nodes) > 400:
            self.consolidate_nodes()

        attractor_name = self._derive_attractor(node)

        self.attractor_state = {
            "name": attractor_name,
            "node_id": node.node_id,
        }

        # --------------------------------------------------
        # SAVE THROTTLE
        # --------------------------------------------------
        if not hasattr(self, "_save_counter"):
            self._save_counter = 0

        if not hasattr(self, "_save_interval"):
            self._save_interval = 500

        self._save_counter += 1

        if self._save_counter >= self._save_interval:
            self._save()
            self._save_counter = 0

        return {
            "node_id": node.node_id,
            "attractor": attractor_name,
            "center": list(node.center),
        }

    # --------------------------------------------------
    # START EPISODE
    # --------------------------------------------------
    def start_episode(self, state: Dict[str, Any]):

        node_info = self.record_state(state)

        self.active_episode = {
            "start_ts": state.get("timestamp"),
            "start_node_id": node_info.get("node_id"),
            "side": str(state.get("side", "NONE")).upper().strip(),
            "states": [dict(state)],
        }

    # --------------------------------------------------
    # STEP EPISODE
    # --------------------------------------------------
    def step_episode(self, state: Dict[str, Any]):

        if self.active_episode is None:
            self.start_episode(state)
            return

        node_info = self.record_state(state)

        self.active_episode["end_node_id"] = node_info.get("node_id")
        self.active_episode["end_ts"] = state.get("timestamp")
        self.active_episode["states"].append(dict(state))

    # --------------------------------------------------
    # FINALIZE EPISODE
    # --------------------------------------------------
    def finalize_episode(self, outcome: str, rr: float = 0.0):

        if self.active_episode is None:
            return

        episode = dict(self.active_episode)
        episode["outcome"] = str(outcome)
        episode["rr"] = float(rr or 0.0)

        self.episodes.append(episode)

        if len(self.episodes) > self.max_episodes:
            self.episodes = self.episodes[-self.max_episodes:]

        self.active_episode = None
        self._save()

    # --------------------------------------------------
    # MATCH NODE BY ENERGY
    # --------------------------------------------------
    def _match_node_by_energy(self, energy_value: float) -> Optional[RegimeNode]:

            if not self.regime_nodes:
                return None

            if not self.sensory_buffer:
                return None

            last = self.sensory_buffer[-1]

            coherence = float(last.get("coherence", 0.0))
            resonance = float(last.get("resonance", 0.0))

            best_node = None
            best_dist = None

            for node in self.regime_nodes:

                e = float(node.center[0])
                c = float(node.center[1])
                r = float(node.center[3])

                dist = (
                    abs(e - float(energy_value)) +
                    abs(c - coherence) +
                    abs(r - resonance)
                )

                if best_dist is None or dist < best_dist:
                    best_dist = dist
                    best_node = node

            if best_dist is None or best_dist > 1.2:
                return None

            return best_node

    # --------------------------------------------------
    # REGIME RR
    # --------------------------------------------------
    def regime_rr(self, energy_value, side):

        default_rr = float(getattr(__import__("config").Config, "RR", 2.0))
        min_rr = float(getattr(Config, "MIN_RR", 1.0))
        max_rr = float(getattr(Config, "MAX_RR", 4.0))

        side_key = str(side).upper().strip()
        if side_key not in ("LONG", "SHORT"):
            return default_rr

        if not self.sensory_buffer:
            return default_rr

        last = self.sensory_buffer[-1]

        state = {
            "energy": last.get("energy"),
            "coherence": last.get("coherence"),
            "asymmetry": last.get("asymmetry"),
            "resonance": last.get("resonance"),
            "coh_zone": last.get("coh_zone", 0.0),
            "side": side,
        }

        vector = self._state_vector(state)

        node = self._find_best_node(vector)

        if node is None:
            return default_rr

        stats = node.side_stats.get(side_key, {})
         
        rr_count = int(stats.get("rr_count", 0) or 0)
        rr_sum = float(stats.get("rr_sum", 0.0) or 0.0)

        '''
        if rr_count <= 0:
            return default_rr

        rr_delta = rr_sum / rr_count
        return float(default_rr + rr_delta)
        '''

        if rr_count <= 0:
            return default_rr
        
        rr_delta = rr_sum / rr_count

        rr_target = default_rr + rr_delta

        rr_target = max(
            float(min_rr),
            min(float(rr_target), float(max_rr))
        )

        return float(rr_target)

        ''''''

    # --------------------------------------------------
    # REGIME ENTRY OFFSET
    # --------------------------------------------------
    def regime_entry_offset(self, energy_value, side):

        side_key = str(side).upper().strip()
        if side_key not in ("LONG", "SHORT"):
            return 0.0

        if not self.sensory_buffer:
            return 0.0

        last = self.sensory_buffer[-1]

        state = {
            "energy": last.get("energy"),
            "coherence": last.get("coherence"),
            "asymmetry": last.get("asymmetry"),
            "resonance": last.get("resonance"),
            "coh_zone": last.get("coh_zone", 0.0),
            "side": side,
        }

        vector = self._state_vector(state)

        node = self._find_best_node(vector)

        if node is None:
            return 0.0

        stats = node.side_stats.get(side_key, {})

        entry_shift_count = int(stats.get("entry_shift_count", 0) or 0)
        entry_shift_sum = float(stats.get("entry_shift_sum", 0.0) or 0.0)

        if entry_shift_count <= 0:
            return 0.0

        return max(0.0, float(entry_shift_sum / entry_shift_count))
    
    # --------------------------------------------------
    # REGIME EFFICIENCY
    # --------------------------------------------------
    def regime_efficiency(self, energy_value, side):

        side_key = str(side).upper().strip()
        if side_key not in ("LONG", "SHORT"):
            return 0.5

        if not self.sensory_buffer:
            return 0.5

        last = self.sensory_buffer[-1]

        state = {
            "energy": last.get("energy"),
            "coherence": last.get("coherence"),
            "asymmetry": last.get("asymmetry"),
            "resonance": last.get("resonance"),
            "coh_zone": last.get("coh_zone", 0.0),
            "side": side,
        }

        vector = self._state_vector(state)

        node = self._find_best_node(vector)

        if node is None:
            return 0.5

        stats = node.side_stats.get(side_key, {})

        tp = int(stats.get("tp", 0) or 0)
        sl = int(stats.get("sl", 0) or 0)

        total = tp + sl

        if total <= 0:
            return 0.5

        return float(tp / total)

    # --------------------------------------------------
    # UPDATE REWARD
    # --------------------------------------------------
    def update_reward(self, energy_value, outcome, side, rr, structure_type=None, entry_shift=0.0):

        side_key = str(side).upper().strip()
        if side_key not in ("LONG", "SHORT"):
            return

        node = self._match_node_by_energy(float(energy_value))

        if node is None:
            vector = [
                float(energy_value),
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                1.0 if side_key == "LONG" else -1.0
            ]
            node = self._create_node(vector)

        stats = node.side_stats[side_key]

        if outcome == "tp":
            stats["tp"] += 1
            stats["rr_sum"] += float(rr)
            stats["rr_count"] += 1
            stats["entry_shift_sum"] += float(entry_shift)
            stats["entry_shift_count"] += 1

        if outcome == "sl":
            stats["sl"] += 1
            stats["rr_sum"] -= float(rr)
            stats["rr_count"] += 1
            stats["entry_shift_sum"] -= float(entry_shift)
            stats["entry_shift_count"] += 1

        self.reward_traces.append({
            "node_id": node.node_id,
            "energy": float(energy_value),
            "outcome": str(outcome),
            "side": side_key,
            "rr": float(rr),
        })

        if len(self.reward_traces) > self.max_reward_traces:
            self.reward_traces = self.reward_traces[-self.max_reward_traces:]

        if self.last_node_id is not None:
            from_key = str(self.last_node_id)
            to_key = str(node.node_id)

            if from_key in self.transition_graph and to_key in self.transition_graph[from_key]:
                if outcome == "tp":
                    self.transition_graph[from_key][to_key]["tp"] += 1
                if outcome == "sl":
                    self.transition_graph[from_key][to_key]["sl"] += 1

        self.finalize_episode(outcome=outcome, rr=rr)
        self._save()

    # --------------------------------------------------
    # STRONGEST
    # --------------------------------------------------
    def strongest(self):

        if not self.regime_nodes:
            return None

        best_node = None
        best_score = None

        for node in self.regime_nodes:

            long_tp = int(node.side_stats["LONG"]["tp"])
            short_tp = int(node.side_stats["SHORT"]["tp"])
            score = long_tp + short_tp + int(node.visits)

            if best_score is None or score > best_score:
                best_score = score
                best_node = node

        if best_node is None:
            return None

        return {
            "node_id": best_node.node_id,
            "center": float(best_node.center[0]),
            "visits": int(best_node.visits),
        }

    # --------------------------------------------------
    # REPLAY IMPULSE
    # --------------------------------------------------
    def replay_impulse(self, replay_scale=0.25):

        if not self.reward_traces:
            return 0.0

        positives = [
            item for item in self.reward_traces
            if str(item.get("outcome")) == "tp"
        ]

        if not positives:
            return 0.0

        item = random.choice(positives)

        return float(float(item.get("energy", 0.0)) * float(replay_scale))
    
    # --------------------------------------------------
    # PREDICT NEXT REGIME
    # --------------------------------------------------
    def predict_next_regime(self):

        if self.last_node_id is None:
            return None

        node_key = str(self.last_node_id)

        if node_key not in self.transition_graph:
            return None

        transitions = self.transition_graph[node_key]

        total = 0
        for data in transitions.values():
            total += int(data.get("count", 0))

        if total == 0:
            return None

        best_node = None
        best_prob = 0.0

        for node_id, data in transitions.items():

            prob = float(data.get("count", 0)) / total

            if prob > best_prob:
                best_prob = prob
                best_node = int(node_id)

        return {
            "next_node": best_node,
            "probability": best_prob
        }
    
    # --------------------------------------------------
    # NODE CONSOLIDATION
    # --------------------------------------------------
    def consolidate_nodes(self, merge_distance=0.35, min_visits=5):

        if len(self.regime_nodes) < 2:
            return

        merged = []

        for node in self.regime_nodes:

            merged_flag = False

            for target in merged:

                try:
                    dist = target.distance(node.center)

                    if dist < merge_distance:

                        total = target.visits + node.visits

                        if total <= 0:
                            continue

                        # gewichtetes Zentrum
                        target.center = [
                            (
                                (target.center[i] * target.visits) +
                                (node.center[i] * node.visits)
                            ) / total
                            for i in range(len(target.center))
                        ]

                        target.visits = total

                        for side in ("LONG", "SHORT"):

                            target.side_stats[side]["tp"] += node.side_stats[side]["tp"]
                            target.side_stats[side]["sl"] += node.side_stats[side]["sl"]
                            target.side_stats[side]["rr_sum"] += node.side_stats[side]["rr_sum"]
                            target.side_stats[side]["rr_count"] += node.side_stats[side]["rr_count"]

                        merged_flag = True
                        break

                except Exception:
                    pass

            if not merged_flag:
                merged.append(node)

        # schwache Nodes entfernen
        filtered = []

        for node in merged:

            if node.visits >= min_visits:
                filtered.append(node)

        self.regime_nodes = filtered    