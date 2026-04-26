import numpy as np
from sklearn.cluster import DBSCAN
import random
from config import Config
# --------------------------------------------------
Default_N_AGENTS = 160
DIMS = 3
# --------------------------------------------------
# Wahrnehmung
# --------------------------------------------------

class Perception:

    def encode(self, stimulus):
        """Stimulus → Energieimpuls"""

        mapping = {
            "positive": +1.45,
            "negative": -0.65,
            "threat": -1.75,
            "reward": +1.55,
            "neutral": 0.0
        }

        return mapping.get(stimulus, 0.0)
    
# --------------------------------------------------
# MCM SelfModel
# --------------------------------------------------
class SelfModel:

    def evaluate(self, energy):

        mean_e = float(np.mean(energy[:,0]))
        motivation = float(np.mean(energy[:,1]))
        risk = float(np.mean(energy[:,2]))

        if risk <= -1.5:
            return "stressed"

        if motivation >= 1.2:
            return "excited"

        if abs(mean_e) < 0.2:
            return "stable"

        return "active"
    
# --------------------------------------------------
# MCM Feld
# --------------------------------------------------

class MCMField:

    def __init__(self, n_agents=Default_N_AGENTS, dims=DIMS):

        self.N = max(1, int(n_agents or Default_N_AGENTS))
        self.D = max(1, int(dims or DIMS))

        self.k_center = 0.0035
        self.coupling = 0.08
        self.noise = 0.18
        self.coupling_sigma = float(getattr(Config, "MCM_FIELD_COUPLING_SIGMA", 0.5) or 0.5)
        self.local_neighbor_count = max(1, int(getattr(Config, "MCM_FIELD_LOCAL_NEIGHBORS", 8) or 8))
        self.max_abs_state = 3.0
        self.areal_radius = float(getattr(Config, "MCM_FIELD_AREAL_RADIUS", 0.78) or 0.78)
        self.areal_min_size = max(2, int(getattr(Config, "MCM_FIELD_AREAL_MIN_SIZE", 3) or 3))

        self.neurons = [MCMNeuron(dims=self.D) for _ in range(self.N)]
        self.energy = np.zeros((self.N, self.D), dtype=float)
        self.velocity = np.zeros((self.N, self.D), dtype=float)
        self.areal_state = {
            "areal_count": 0,
            "areal_activation_mean": 0.0,
            "areal_stability_mean": 0.0,
            "areal_pressure_mean": 0.0,
            "areal_drift": 0.0,
            "areal_dominance": 0.0,
            "areal_fragmentation": 0.0,
            "areal_coherence_mean": 0.0,
            "areal_conflict_mean": 0.0,
            "areal_states": [],
            "areal_links": [],
        }
        self._last_areal_centers = []
        self._refresh_arrays_from_neurons()
        self._refresh_areal_state()

    # --------------------------------------------------
    def _propagate_runtime_parameters(self):

        for neuron in list(self.neurons or []):
            neuron.center_force = float(self.k_center)
            neuron.coupling_strength = float(self.coupling)
            neuron.noise_strength = float(self.noise)
            neuron.coupling_sigma = float(self.coupling_sigma)
            neuron.max_abs_state = float(self.max_abs_state)

    # --------------------------------------------------
    def _sync_neurons_from_arrays(self):

        energy = np.asarray(getattr(self, "energy", []), dtype=float)
        velocity = np.asarray(getattr(self, "velocity", []), dtype=float)

        if energy.shape != (self.N, self.D):
            repaired_energy = np.zeros((self.N, self.D), dtype=float)
            if energy.size > 0:
                rows = min(int(energy.shape[0]) if energy.ndim >= 1 else 0, self.N)
                cols = min(int(energy.shape[1]) if energy.ndim >= 2 else 0, self.D)
                if rows > 0 and cols > 0:
                    repaired_energy[:rows, :cols] = energy[:rows, :cols]
            energy = repaired_energy
            self.energy = np.asarray(energy, dtype=float)

        if velocity.shape != (self.N, self.D):
            repaired_velocity = np.zeros((self.N, self.D), dtype=float)
            if velocity.size > 0:
                rows = min(int(velocity.shape[0]) if velocity.ndim >= 1 else 0, self.N)
                cols = min(int(velocity.shape[1]) if velocity.ndim >= 2 else 0, self.D)
                if rows > 0 and cols > 0:
                    repaired_velocity[:rows, :cols] = velocity[:rows, :cols]
            velocity = repaired_velocity
            self.velocity = np.asarray(velocity, dtype=float)

        for index, neuron in enumerate(list(self.neurons or [])):
            neuron.state = np.asarray(energy[index], dtype=float).copy()
            neuron.velocity = np.asarray(velocity[index], dtype=float).copy()
            neuron._clip_state()

    # --------------------------------------------------
    def _refresh_arrays_from_neurons(self):

        if not self.neurons:
            self.energy = np.zeros((self.N, self.D), dtype=float)
            self.velocity = np.zeros((self.N, self.D), dtype=float)
            return

        self.energy = np.asarray([
            np.asarray(neuron.state, dtype=float).copy()
            for neuron in list(self.neurons or [])
        ], dtype=float)
        self.velocity = np.asarray([
            np.asarray(neuron.velocity, dtype=float).copy()
            for neuron in list(self.neurons or [])
        ], dtype=float)

    # --------------------------------------------------
    def _build_local_neighbor_state_map(self):

        neighbor_state_map = {index: [] for index in range(self.N)}
        energy = np.asarray(getattr(self, "energy", []), dtype=float)

        if energy.ndim != 2 or len(energy) <= 1:
            return neighbor_state_map

        agent_count = min(int(self.N), int(len(energy)))
        local_neighbors = max(1, min(agent_count - 1, int(self.local_neighbor_count or 1)))

        for index in range(agent_count):
            local_delta = energy - energy[int(index)]
            local_distances = np.linalg.norm(local_delta, axis=1)
            local_distances[int(index)] = np.inf

            if len(local_distances) > local_neighbors + 1:
                order = np.argpartition(local_distances, local_neighbors)[:local_neighbors]
                order = order[np.argsort(local_distances[order])]
            else:
                order = np.argsort(local_distances)

            selected = []

            for neighbor_index in list(order):
                if len(selected) >= local_neighbors:
                    break

                if not np.isfinite(local_distances[int(neighbor_index)]):
                    continue

                selected.append(np.asarray(energy[int(neighbor_index)], dtype=float).copy())

            neighbor_state_map[index] = list(selected or [])

        return neighbor_state_map

    # --------------------------------------------------
    def _build_areal_components(self, distances):

        if len(distances) <= 1:
            return []

        radius = max(float(self.areal_radius or 0.78), 1e-9)
        expanded_radius = radius * 1.35
        local_neighbors = max(1, int(self.local_neighbor_count or 1))
        adjacency = {index: set() for index in range(self.N)}

        for index in range(self.N):
            order = np.argsort(distances[index])
            selected_neighbors = []

            for neighbor_index in list(order):
                if int(neighbor_index) == int(index):
                    continue

                distance = float(distances[index, int(neighbor_index)])
                if distance <= radius:
                    selected_neighbors.append(int(neighbor_index))
                elif len(selected_neighbors) < local_neighbors and distance <= expanded_radius:
                    selected_neighbors.append(int(neighbor_index))
                elif len(selected_neighbors) >= local_neighbors:
                    break

            for neighbor_index in list(selected_neighbors or []):
                adjacency[index].add(int(neighbor_index))
                adjacency[int(neighbor_index)].add(int(index))

        components = []
        visited = set()

        for start_index in range(self.N):
            if start_index in visited:
                continue

            stack = [int(start_index)]
            component = []
            visited.add(int(start_index))

            while stack:
                current_index = int(stack.pop())
                component.append(int(current_index))

                for neighbor_index in list(adjacency.get(current_index, set()) or set()):
                    if int(neighbor_index) in visited:
                        continue

                    visited.add(int(neighbor_index))
                    stack.append(int(neighbor_index))

            if len(component) >= int(self.areal_min_size):
                components.append(sorted(int(item) for item in list(component or [])))

        return list(components or [])

    # --------------------------------------------------
    def _build_areal_state(self):

        energy = np.asarray(getattr(self, "energy", []), dtype=float)
        velocity = np.asarray(getattr(self, "velocity", []), dtype=float)

        if energy.ndim != 2 or len(energy) == 0:
            self.areal_state = {
                "areal_count": 0,
                "areal_activation_mean": 0.0,
                "areal_stability_mean": 0.0,
                "areal_pressure_mean": 0.0,
                "areal_drift": 0.0,
                "areal_dominance": 0.0,
                "areal_fragmentation": 0.0,
                "areal_coherence_mean": 0.0,
                "areal_conflict_mean": 0.0,
                "areal_states": [],
                "areal_links": [],
            }
            self._last_areal_centers = []
            return dict(self.areal_state or {})

        agent_count = int(len(energy))
        distances = np.zeros((agent_count, agent_count), dtype=float)
        for index in range(agent_count):
            local_delta = energy - energy[int(index)]
            distances[int(index)] = np.linalg.norm(local_delta, axis=1)

        components = self._build_areal_components(distances)
        areal_states = []
        current_centers = []

        for areal_index, component in enumerate(list(components or [])):
            component_indices = [int(item) for item in list(component or [])]
            component_energy = np.asarray(energy[component_indices], dtype=float)
            component_velocity = np.asarray(velocity[component_indices], dtype=float)
            component_distances = np.asarray(distances[np.ix_(component_indices, component_indices)], dtype=float)

            activation_values = []
            stability_values = []
            pressure_values = []
            memory_norm_values = []
            coupling_norm_values = []
            regulation_norm_values = []
            external_norm_values = []

            for neuron_index in list(component_indices or []):
                neuron = self.neurons[int(neuron_index)]
                activation_values.append(float(getattr(neuron, "activation", 0.0) or 0.0))
                stability_values.append(float(getattr(neuron, "stability", 0.0) or 0.0))
                pressure_values.append(float(getattr(neuron, "regulation_pressure", 0.0) or 0.0))
                memory_norm_values.append(float(np.linalg.norm(np.asarray(getattr(neuron, "memory_trace", []), dtype=float))))
                coupling_norm_values.append(float(np.linalg.norm(np.asarray(getattr(neuron, "last_coupling_force", []), dtype=float))))
                regulation_norm_values.append(float(np.linalg.norm(np.asarray(getattr(neuron, "last_regulation_force", []), dtype=float))))
                external_norm_values.append(float(np.linalg.norm(np.asarray(getattr(neuron, "last_external_impulse", []), dtype=float))))

            center = np.mean(component_energy, axis=0)
            mean_velocity_vector = np.mean(component_velocity, axis=0)
            current_centers.append(np.asarray(center, dtype=float))

            upper_triangle = component_distances[np.triu_indices(len(component_indices), k=1)]
            mean_internal_distance = float(np.mean(upper_triangle)) if upper_triangle.size > 0 else 0.0
            density = float(max(0.0, min(1.0, 1.0 - (mean_internal_distance / max(self.areal_radius * 1.35, 1e-9)))))
            activation_mean = float(np.mean(activation_values)) if activation_values else 0.0
            stability_mean = float(np.mean(stability_values)) if stability_values else 0.0
            pressure_mean = float(np.mean(pressure_values)) if pressure_values else 0.0
            velocity_mean = float(np.mean(np.linalg.norm(component_velocity, axis=1))) if len(component_velocity) > 0 else 0.0
            center_abs = np.abs(np.asarray(center, dtype=float))
            coherence = float(np.max(center_abs)) if center_abs.size > 0 else 0.0
            conflict = float(np.std(component_energy[:, 0])) if component_energy.shape[1] > 0 else 0.0

            areal_label = "adaptive_areal"
            if pressure_mean >= 0.24 and stability_mean < 0.42:
                areal_label = "strain_areal"
            elif activation_mean >= 0.55 and velocity_mean >= 0.22:
                areal_label = "active_areal"
            elif stability_mean >= 0.68 and density >= 0.52:
                areal_label = "settled_areal"
            elif conflict >= 0.28:
                areal_label = "conflict_areal"

            bounds_min = np.min(component_energy, axis=0)
            bounds_max = np.max(component_energy, axis=0)

            areal_states.append({
                "areal_id": f"areal_{int(areal_index)}",
                "member_indices": [int(item) for item in list(component_indices or [])],
                "center": [float(round(value, 4)) for value in np.asarray(center, dtype=float).tolist()],
                "mean_velocity_vector": [float(round(value, 4)) for value in np.asarray(mean_velocity_vector, dtype=float).tolist()],
                "bounds_min": [float(round(value, 4)) for value in np.asarray(bounds_min, dtype=float).tolist()],
                "bounds_max": [float(round(value, 4)) for value in np.asarray(bounds_max, dtype=float).tolist()],
                "mass": int(len(component_indices)),
                "density": float(round(density, 4)),
                "activation_mean": float(round(activation_mean, 4)),
                "stability_mean": float(round(stability_mean, 4)),
                "pressure_mean": float(round(pressure_mean, 4)),
                "memory_norm_mean": float(round(float(np.mean(memory_norm_values)) if memory_norm_values else 0.0, 4)),
                "coupling_norm_mean": float(round(float(np.mean(coupling_norm_values)) if coupling_norm_values else 0.0, 4)),
                "regulation_force_norm_mean": float(round(float(np.mean(regulation_norm_values)) if regulation_norm_values else 0.0, 4)),
                "external_impulse_norm_mean": float(round(float(np.mean(external_norm_values)) if external_norm_values else 0.0, 4)),
                "velocity_mean": float(round(velocity_mean, 4)),
                "coherence": float(round(coherence, 4)),
                "conflict": float(round(conflict, 4)),
                "state_label": str(areal_label),
            })

        areal_links = []

        for left_index, left_state in enumerate(list(areal_states or [])):
            left_center = np.asarray(left_state.get("center", []), dtype=float)

            for right_index in range(left_index + 1, len(areal_states)):
                right_state = dict(areal_states[right_index] or {})
                right_center = np.asarray(right_state.get("center", []), dtype=float)
                if len(left_center) == 0 or len(right_center) == 0:
                    continue

                distance = float(np.linalg.norm(left_center - right_center))
                if distance > (self.areal_radius * 3.2):
                    continue

                relation_label = "bridged"
                if np.sign(left_center[0] if len(left_center) > 0 else 0.0) != np.sign(right_center[0] if len(right_center) > 0 else 0.0):
                    relation_label = "counter_tension"
                elif distance <= (self.areal_radius * 1.6):
                    relation_label = "coupled"

                areal_links.append({
                    "source_areal_id": str(left_state.get("areal_id", f"areal_{left_index}")),
                    "target_areal_id": str(right_state.get("areal_id", f"areal_{right_index}")),
                    "distance": float(round(distance, 4)),
                    "relation_label": str(relation_label),
                })

        areal_drift = 0.0
        previous_centers = [np.asarray(item, dtype=float) for item in list(self._last_areal_centers or [])]
        if current_centers and previous_centers:
            drift_values = []
            for center in list(current_centers or []):
                distances_to_previous = [
                    float(np.linalg.norm(np.asarray(center, dtype=float) - np.asarray(previous_center, dtype=float)))
                    for previous_center in list(previous_centers or [])
                ]
                if distances_to_previous:
                    drift_values.append(float(min(distances_to_previous)))
            if drift_values:
                areal_drift = float(np.mean(drift_values))

        areal_count = int(len(areal_states))
        dominance = float(max((float(item.get("mass", 0) or 0) / max(1, self.N)) for item in list(areal_states or []))) if areal_states else 0.0
        fragmentation = float(min(1.0, areal_count / max(1.0, float(self.N) / max(1.0, float(self.areal_min_size)))))
        areal_activation_mean = float(np.mean([float(item.get("activation_mean", 0.0) or 0.0) for item in list(areal_states or [])])) if areal_states else 0.0
        areal_stability_mean = float(np.mean([float(item.get("stability_mean", 0.0) or 0.0) for item in list(areal_states or [])])) if areal_states else 0.0
        areal_pressure_mean = float(np.mean([float(item.get("pressure_mean", 0.0) or 0.0) for item in list(areal_states or [])])) if areal_states else 0.0
        areal_coherence_mean = float(np.mean([float(item.get("coherence", 0.0) or 0.0) for item in list(areal_states or [])])) if areal_states else 0.0
        areal_conflict_mean = float(np.mean([float(item.get("conflict", 0.0) or 0.0) for item in list(areal_states or [])])) if areal_states else 0.0

        self.areal_state = {
            "areal_count": int(areal_count),
            "areal_activation_mean": float(round(areal_activation_mean, 4)),
            "areal_stability_mean": float(round(areal_stability_mean, 4)),
            "areal_pressure_mean": float(round(areal_pressure_mean, 4)),
            "areal_drift": float(round(areal_drift, 4)),
            "areal_dominance": float(round(dominance, 4)),
            "areal_fragmentation": float(round(fragmentation, 4)),
            "areal_coherence_mean": float(round(areal_coherence_mean, 4)),
            "areal_conflict_mean": float(round(areal_conflict_mean, 4)),
            "areal_states": list(areal_states or []),
            "areal_links": list(areal_links or []),
        }
        self._last_areal_centers = [np.asarray(item, dtype=float) for item in list(current_centers or [])]
        return dict(self.areal_state or {})

    # --------------------------------------------------
    def _refresh_areal_state(self):
        return self._build_areal_state()

    # --------------------------------------------------
    def read_snapshot(self):

        neuron_payload = []

        for index, neuron in enumerate(list(self.neurons or [])):
            neuron_snapshot = dict(neuron.read_snapshot() or {})
            neuron_snapshot["agent_index"] = int(index)
            neuron_payload.append(neuron_snapshot)

        return {
            "energy": np.asarray(self.energy, dtype=float).copy(),
            "velocity": np.asarray(self.velocity, dtype=float).copy(),
            "neurons": list(neuron_payload or []),
            "areal_state": dict(self.areal_state or {}),
            "areal_states": [dict(item or {}) for item in list((self.areal_state or {}).get("areal_states", []) or []) if isinstance(item, dict)],
            "areal_links": [dict(item or {}) for item in list((self.areal_state or {}).get("areal_links", []) or []) if isinstance(item, dict)],
        }

    # --------------------------------------------------
    def step(
        self,
        impulse,
        motivation_impulse=0.0,
        risk_impulse=0.0,
        replay_impulse=None,
    ):

        self._propagate_runtime_parameters()
        self._sync_neurons_from_arrays()

        neighbor_state_map = self._build_local_neighbor_state_map()

        for index, neuron in enumerate(list(self.neurons or [])):
            neuron.step(
                external_impulse=impulse,
                neighbor_states=list(neighbor_state_map.get(index, []) or []),
                replay_impulse=replay_impulse,
                motivation_impulse=motivation_impulse,
                risk_impulse=risk_impulse,
            )

        self._refresh_arrays_from_neurons()
        self.energy = np.clip(np.asarray(self.energy, dtype=float), -self.max_abs_state, self.max_abs_state)
        self._sync_neurons_from_arrays()
        self._refresh_arrays_from_neurons()
        self._refresh_areal_state()
        return self.read_snapshot()

# --------------------------------------------------
# Clusterbildung
# --------------------------------------------------

class ClusterDetector:

    def __init__(self):

        self.tick_seq = 0
        self.last_clusters = []
        self.last_cluster_centers = []
        self.last_mean_velocity = 0.0
        self.last_topology = {
            "cluster_center_drift": 0.0,
            "cluster_count_drift": 0.0,
            "field_velocity_trend": 0.0,
            "reorganization_direction": "stable",
        }
        self.eps = float(getattr(Config, "MCM_CLUSTER_EPS", 0.4) or 0.4)
        self.min_samples = max(2, int(getattr(Config, "MCM_CLUSTER_MIN_SAMPLES", 4) or 4))
        self.detect_every_n = max(1, int(getattr(Config, "MCM_CLUSTER_EVERY_N_TICKS", 2) or 2))

    def detect(self, energy, force: bool = False, mean_velocity=None):

        self.tick_seq = int(self.tick_seq or 0) + 1

        current_velocity = float(mean_velocity or 0.0) if mean_velocity is not None else float(self.last_mean_velocity or 0.0)
        previous_velocity = float(self.last_mean_velocity or 0.0)
        field_velocity_trend = float(current_velocity - previous_velocity)

        if (not bool(force)) and self.last_clusters and (self.tick_seq % self.detect_every_n) != 0:
            self.last_mean_velocity = float(current_velocity)
            self.last_topology["field_velocity_trend"] = float(field_velocity_trend)
            return [np.array(item, copy=True) for item in list(self.last_clusters or [])]

        points = np.asarray(energy, dtype=float)

        if len(points) < self.min_samples:
            previous_cluster_count = len(list(self.last_cluster_centers or []))

            self.last_clusters = []
            self.last_cluster_centers = []
            self.last_mean_velocity = float(current_velocity)
            self.last_topology = {
                "cluster_center_drift": 0.0,
                "cluster_count_drift": float(previous_cluster_count),
                "field_velocity_trend": float(field_velocity_trend),
                "reorganization_direction": "dissolving" if previous_cluster_count > 0 else "stable",
            }
            return []

        db = DBSCAN(eps=self.eps, min_samples=self.min_samples).fit(points)

        labels = db.labels_

        clusters = []

        for c in set(labels):
            if c == -1:
                continue
            clusters.append(np.array(points[labels == c], copy=True))

        current_centers = [
            np.mean(item, axis=0)
            for item in list(clusters or [])
            if len(item) > 0
        ]
        previous_centers = [
            np.asarray(item, dtype=float)
            for item in list(self.last_cluster_centers or [])
        ]

        cluster_center_drift = 0.0
        if current_centers and previous_centers:
            drift_values = []

            for center in current_centers:
                distances = [
                    float(np.linalg.norm(np.asarray(center, dtype=float) - prev_center))
                    for prev_center in previous_centers
                ]
                if distances:
                    drift_values.append(float(min(distances)))

            if drift_values:
                cluster_center_drift = float(np.mean(drift_values))

        cluster_count_drift = float(
            abs(len(current_centers) - len(previous_centers))
            / max(1, max(len(current_centers), len(previous_centers)))
        )

        reorganization_direction = "stable"

        if not previous_centers and current_centers:
            reorganization_direction = "forming"
        elif previous_centers and not current_centers:
            reorganization_direction = "dissolving"
        elif cluster_center_drift >= 0.18 or cluster_count_drift >= 0.50:
            reorganization_direction = "reorganizing"
        elif field_velocity_trend > 0.08:
            reorganization_direction = "accelerating"
        elif field_velocity_trend < -0.08:
            reorganization_direction = "settling"

        self.last_clusters = [np.array(item, copy=True) for item in list(clusters or [])]
        self.last_cluster_centers = [
            np.asarray(item, dtype=float)
            for item in list(current_centers or [])
        ]
        self.last_mean_velocity = float(current_velocity)
        self.last_topology = {
            "cluster_center_drift": float(cluster_center_drift),
            "cluster_count_drift": float(cluster_count_drift),
            "field_velocity_trend": float(field_velocity_trend),
            "reorganization_direction": str(reorganization_direction),
        }

        return [np.array(item, copy=True) for item in list(self.last_clusters or [])]


# --------------------------------------------------
# Gedächtnis
# --------------------------------------------------

class Memory:

    def __init__(self):
        self.memory = []
        self.decay = 0.85
        self.max_items = 12

    def store(self, clusters):

        updated_memory = []

        for item in self.memory:
            updated_memory.append({
                "center": float(item["center"]),
                "strength": max(1, int(round(item["strength"] * self.decay)))
            })

        for c in clusters:

            center = float(np.mean(c[:,0]))
            strength = int(len(c))
            merged = False

            for item in updated_memory:
                if abs(item["center"] - center) <= 0.35:
                    item["center"] = 0.5 * (item["center"] + center)
                    item["strength"] += strength
                    merged = True
                    break

            if not merged:
                updated_memory.append({
                    "center": center,
                    "strength": strength
                })

        updated_memory = sorted(
            updated_memory,
            key=lambda x: x["strength"],
            reverse=True
        )[:self.max_items]

        self.memory = updated_memory

    def strongest(self):

        if not self.memory:
            return None

        return max(self.memory, key=lambda x: x["strength"])

    def replay_impulse(self, replay_scale=0.08):

        if not self.memory:
            return 0.0

        item = random.choice(self.memory)

        return replay_scale * float(item["center"])


# --------------------------------------------------
# Attraktoren
# --------------------------------------------------

class AttractorSystem:

    def choose(self, memory, self_state):

        if memory is None:
            if self_state == "stressed":
                return "defense"
            if self_state == "excited":
                return "explore"
            return "neutral"

        e = memory["center"]

        if self_state == "stressed" and e < -0.3:
            return "defense"

        if self_state == "excited" and e >= 1.2:
            return "explore"

        if e < -1.5:
            return "defense"

        if -1.5 <= e < -0.3:
            return "analysis"

        if -0.3 <= e < 1.2:
            return "cooperate"

        if e >= 1.6:
            return "explore"

        return "neutral"

# --------------------------------------------------
# Handlungssystem
# --------------------------------------------------

class ActionSystem:

    def act(self, attractor):

        actions = {
            "defense": "block / withdraw",
            "analysis": "observe / process",
            "cooperate": "engage socially",
            "explore": "seek novelty",
            "neutral": "idle"
        }

        return actions.get(attractor, "idle")

# --------------------------------------------------
# MCM Neuron
# --------------------------------------------------
class MCMNeuron:

    def __init__(self, dims=DIMS):
        self.dims = max(1, int(dims or DIMS))

        self.state = np.random.uniform(-0.3, 0.3, self.dims)
        self.velocity = np.zeros(self.dims, dtype=float)

        self.last_external_impulse = np.zeros(self.dims, dtype=float)
        self.last_memory_impulse = np.zeros(self.dims, dtype=float)
        self.last_coupling_force = np.zeros(self.dims, dtype=float)
        self.last_regulation_force = np.zeros(self.dims, dtype=float)

        self.memory_trace = np.zeros(self.dims, dtype=float)
        self.activation = 0.0
        self.stability = 1.0
        self.regulation_pressure = 0.0

        self.center_force = float(getattr(Config, "MCM_CENTER_FORCE", 0.0100) or 0.0100)
        self.coupling_strength = float(getattr(Config, "MCM_COUPLING", 0.045) or 0.045)
        self.noise_strength = float(getattr(Config, "MCM_NOISE", 0.08) or 0.08)
        self.coupling_sigma = float(getattr(Config, "MCM_FIELD_COUPLING_SIGMA", 0.5) or 0.5)

        self.inertia = 0.92
        self.memory_decay = 0.86
        self.memory_gain = 0.18
        self.regulation_gain = 0.24
        self.max_abs_state = 3.0

    # --------------------------------------------------
    def _clip_state(self):
        self.state = np.clip(self.state, -self.max_abs_state, self.max_abs_state)

    # --------------------------------------------------
    def _resolve_impulse_vector(self, impulse=None, motivation_impulse=0.0, risk_impulse=0.0):
        vector = np.zeros(self.dims, dtype=float)

        if isinstance(impulse, (list, tuple, np.ndarray)):
            values = np.asarray(impulse, dtype=float).flatten()
            limit = min(len(values), self.dims)
            if limit > 0:
                vector[:limit] = values[:limit]
        else:
            vector[0] = float(impulse or 0.0)

        if self.dims > 1:
            vector[1] += float(motivation_impulse or 0.0)

        if self.dims > 2:
            vector[2] += float(risk_impulse or 0.0)

        return vector

    # --------------------------------------------------
    def _build_coupling_force(self, neighbor_states):
        if not neighbor_states:
            return np.zeros(self.dims, dtype=float)

        sigma = max(float(self.coupling_sigma or 0.5), 1e-9)
        force = np.zeros(self.dims, dtype=float)

        for neighbor in list(neighbor_states or []):
            neighbor_state = np.asarray(neighbor, dtype=float).flatten()
            if len(neighbor_state) != self.dims:
                continue

            diff = neighbor_state - self.state
            distance_sq = float(np.dot(diff, diff))
            weight = float(np.exp(-(distance_sq / sigma)))
            force += weight * diff

        return force * float(self.coupling_strength)

    # --------------------------------------------------
    def _build_regulation_force(self):
        center_pull = -float(self.center_force) * self.state

        overload = max(
            abs(float(self.state[0] if self.dims > 0 else 0.0)),
            abs(float(self.state[2] if self.dims > 2 else 0.0)),
        )

        regulation_scale = min(1.0, overload / 2.2)
        damping = -self.velocity * (self.regulation_gain * regulation_scale)

        regulation_force = center_pull + damping
        self.regulation_pressure = float(np.mean(np.abs(regulation_force)))
        return regulation_force

    # --------------------------------------------------
    def _update_memory_trace(self, total_impulse):
        self.memory_trace = (self.memory_trace * self.memory_decay) + (np.asarray(total_impulse, dtype=float) * self.memory_gain)
        return np.asarray(self.memory_trace, dtype=float)

    # --------------------------------------------------
    def read_snapshot(self):
        return {
            "state": [float(round(v, 4)) for v in self.state.tolist()],
            "velocity": [float(round(v, 4)) for v in self.velocity.tolist()],
            "memory_trace": [float(round(v, 4)) for v in self.memory_trace.tolist()],
            "activation": float(round(self.activation, 4)),
            "stability": float(round(self.stability, 4)),
            "regulation_pressure": float(round(self.regulation_pressure, 4)),
            "external_impulse": [float(round(v, 4)) for v in self.last_external_impulse.tolist()],
            "memory_impulse": [float(round(v, 4)) for v in self.last_memory_impulse.tolist()],
            "coupling_force": [float(round(v, 4)) for v in self.last_coupling_force.tolist()],
            "regulation_force": [float(round(v, 4)) for v in self.last_regulation_force.tolist()],
        }

    # --------------------------------------------------
    def step(
        self,
        external_impulse=None,
        neighbor_states=None,
        replay_impulse=None,
        motivation_impulse=0.0,
        risk_impulse=0.0,
    ):
        external_vector = self._resolve_impulse_vector(
            impulse=external_impulse,
            motivation_impulse=motivation_impulse,
            risk_impulse=risk_impulse,
        )
        replay_vector = self._resolve_impulse_vector(
            impulse=replay_impulse,
            motivation_impulse=0.0,
            risk_impulse=0.0,
        )

        self.last_external_impulse = np.asarray(external_vector, dtype=float)
        self.last_memory_impulse = np.asarray(replay_vector, dtype=float)

        coupling_force = self._build_coupling_force(neighbor_states)
        regulation_force = self._build_regulation_force()

        self.last_coupling_force = np.asarray(coupling_force, dtype=float)
        self.last_regulation_force = np.asarray(regulation_force, dtype=float)

        total_impulse = external_vector + replay_vector
        memory_feedback = self._update_memory_trace(total_impulse) * 0.35
        noise = np.random.randn(self.dims) * float(self.noise_strength)

        self.velocity = (self.velocity * self.inertia) + coupling_force + regulation_force + total_impulse + memory_feedback + noise
        self.state = self.state + self.velocity
        self._clip_state()

        self.activation = float(np.mean(np.abs(total_impulse + coupling_force)))
        self.stability = float(
            max(
                0.0,
                min(
                    1.0,
                    1.0 - (np.mean(np.abs(self.velocity)) / self.max_abs_state),
                ),
            )
        )

        return self.read_snapshot()
    
# --------------------------------------------------
# KI Agent
# --------------------------------------------------

class MCM_AI:

    def __init__(self):

        self.perception = Perception()
        self.self_model = SelfModel()
        self.field = MCMField()
        self.cluster = ClusterDetector()
        self.memory = Memory()
        self.attractor = AttractorSystem()
        self.action = ActionSystem()
        self.regulation = RegulationLayer()


    def step(self, stimulus):

        # Wahrnehmung
        external_impulse = self.perception.encode(stimulus)

        # interner Replay-Impuls
        replay_impulse = self.memory.replay_impulse(replay_scale=0.05)
        total_impulse = external_impulse + replay_impulse

        # interne Gedankenzyklen
        internal_cycles = 3

        for _ in range(internal_cycles):
            self.field.step(replay_impulse)

        # Feld Dynamik mit externem Stimulus
        self.field.step(total_impulse)

        # Clusterbildung
        clusters = self.cluster.detect(self.field.energy)

        # Gedächtnis
        self.memory.store(clusters)

        # Selbstzustand
        self_state = self.self_model.evaluate(self.field.energy)

        # Regulation
        self.regulation.regulate(self.field)

        # Attraktor
        attractor = self.attractor.choose(self.memory.strongest(), self_state)

        # Handlung
        action = self.action.act(attractor)

        return action

# --------------------------------------------------
# Regulation / Homeostasis
# --------------------------------------------------

class RegulationLayer:

    def regulate(self, field):

        mean_energy = float(np.mean(field.energy[:,0]))

        # Energie zu hoch → Exploration bremsen
        if mean_energy > 1.6:
            field.velocity *= 0.65
            field.energy[:,0] -= 0.25

        # Energie zu niedrig → Defense bremsen
        if mean_energy < -1.8:
            field.velocity *= 0.7
            field.energy[:,0] += 0.15

        # Energie nahe Gleichgewicht stabilisieren
        if -0.4 < mean_energy < 0.4:
            field.velocity *= 0.95

# --------------------------------------------------
# Beispiel
# --------------------------------------------------
if __name__ == "__main__":

    ai = MCM_AI()

    stimuli = ["neutral", "positive", "negative", "reward", "threat"]

    for t in range(200):

        stimulus = random.choice(stimuli)

        action = ai.step(stimulus)

        mean_energy = np.mean(ai.field.energy[:, 0])

        print(t, stimulus, "→", action, "| energy:", round(mean_energy, 3))