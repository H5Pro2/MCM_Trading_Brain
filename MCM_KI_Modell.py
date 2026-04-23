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

        self.neurons = [MCMNeuron(dims=self.D) for _ in range(self.N)]
        self.energy = np.zeros((self.N, self.D), dtype=float)
        self.velocity = np.zeros((self.N, self.D), dtype=float)
        self._refresh_arrays_from_neurons()

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

        if len(energy) <= 1:
            return neighbor_state_map

        local_neighbors = max(1, int(self.local_neighbor_count or 1))
        deltas = energy[:, None, :] - energy[None, :, :]
        distances = np.linalg.norm(deltas, axis=2)

        for index in range(self.N):
            order = np.argsort(distances[index])
            selected = []

            for neighbor_index in list(order):
                if int(neighbor_index) == int(index):
                    continue

                selected.append(np.asarray(energy[int(neighbor_index)], dtype=float).copy())

                if len(selected) >= local_neighbors:
                    break

            neighbor_state_map[index] = list(selected or [])

        return neighbor_state_map

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