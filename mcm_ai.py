# ==================================================
# mcm_ai.py
# MCM_AI (Self-Organizing Agent) + Trading Adapter
# ==================================================

import numpy as np
from sklearn.cluster import DBSCAN
from bot_engine.mcm_memory_engine import MCMMemoryEngine
from config import Config
# --------------------------------------------------
# Wahrnehmung
# --------------------------------------------------

class Perception:

    def encode(self, stimulus: str) -> float:
        """Stimulus → Energieimpuls"""

        mapping = {
            "positive": +1.45,
            "negative": -0.65,
            "threat": -1.75,
            "reward": +1.55,
            "neutral": 0.0,
        }

        return float(mapping.get(str(stimulus), 0.0))
    
# --------------------------------------------------
# MCM SelfModel
# --------------------------------------------------
class SelfModel:

    def evaluate(self, energy):

        mean_e = float(np.mean(energy))

        if mean_e >= 1.2:
            return "excited"

        if mean_e <= -1.5:
            return "stressed"

        return "stable"
    
# --------------------------------------------------
# MCM Feld
# --------------------------------------------------

class MCMField:

    def __init__(self, n_agents=80):

        self.N = n_agents

        self.energy = np.random.uniform(-0.3,0.3,self.N)
        self.velocity = np.zeros(self.N)

        self.k_center = 0.08
        self.coupling = 0.2
        self.noise = 0.05


    def step(self, impulse):

        # Energieimpuls
        self.energy += impulse

        # Zentrumskraft
        force = -self.k_center * self.energy

        # lokale Kopplung
        diff = self.energy[:,None] - self.energy[None,:]
        weights = np.exp(-(diff**2)/0.5)

        coupling_force = self.coupling * np.sum(weights * diff, axis=1)

        # Dynamik
        self.velocity += force + coupling_force
        self.velocity += np.random.randn(self.N) * self.noise

        self.energy += self.velocity

        self.energy = np.clip(self.energy,-3,3)


# --------------------------------------------------
# Clusterbildung
# --------------------------------------------------

class ClusterDetector:

    def detect(self, energy):

        points = energy.reshape(-1,1)

        db = DBSCAN(eps=0.4,min_samples=4).fit(points)

        labels = db.labels_

        clusters = []

        for c in set(labels):
            if c == -1:
                continue
            clusters.append(points[labels==c])

        return clusters


# --------------------------------------------------
# Gedächtnis
# --------------------------------------------------
class Memory(MCMMemoryEngine):
    pass

# --------------------------------------------------
# Attraktoren
# --------------------------------------------------

class AttractorSystem:

    def choose(self, memory):

        if memory is None:
            return "neutral"

        e = memory["center"]

        if e < -1.5:
            return "defense"

        if -1.5 <= e < -0.3:
            return "analysis"

        if -0.3 <= e < 1.2:
            return "cooperate"

        if e >= 1.2:
            return "explore"


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

        return actions[attractor]


# --------------------------------------------------
# KI Agent
# --------------------------------------------------

class MCM_AI:

    def __init__(self):

        self.perception = Perception()
        self.field = MCMField()
        self.cluster = ClusterDetector()
        self.memory = MCMMemoryEngine()
        self.attractor = AttractorSystem()
        self.action = ActionSystem()


    def step(self, stimulus):

        # Wahrnehmung
        impulse = self.perception.encode(stimulus)

        # Feld Dynamik
        self.field.step(impulse)

        # Attraktor
        attractor = self.attractor.choose(self.memory.strongest())

        # Handlung
        action = self.action.act(attractor)

        return action

# --------------------------------------------------
# TRADING ADAPTER
# --------------------------------------------------

class MCMTradingDecision:

    def __init__(self):

        self.ai = MCM_AI()

    def _build_stimulus(self, ml_side, structure):

        if ml_side is None:
            return "neutral"

        energy = float(structure.get("energy", 0.0))
        coherence = float(structure.get("coherence", 0.0))
        resonance = float(structure.get("resonance", 0.0))

        if ml_side == "LONG" and coherence > 0.0 and resonance >= 0.35:
            return "reward"

        if ml_side == "SHORT" and coherence < 0.0 and resonance >= 0.35:
            return "reward"

        if ml_side == "LONG" and coherence < 0.0:
            return "threat"

        if ml_side == "SHORT" and coherence > 0.0:
            return "threat"

        if energy > 1.0:
            return "positive"

        if energy < -1.0:
            return "negative"

        return "neutral"

    def decide(self, ml_side, structure):

        stimulus = self._build_stimulus(ml_side, structure)

        action = self.ai.step(stimulus)

        energy = float(structure.get("energy", 0.0))
        coherence = float(structure.get("coherence", 0.0))
        asymmetry = int(structure.get("asymmetry", 0))
        resonance = float(structure.get("resonance", 0.0))
        coh_zone = float(structure.get("coh_zone", 0.0))

        state = {
            "energy": energy,
            "coherence": coherence,
            "asymmetry": asymmetry,
            "resonance": resonance,
            "coh_zone": coh_zone,
            "side": ml_side,

            "structure_type": structure.get("structure_type"),
            "structure_strength": structure.get("structure_strength"),
            "structure_age": structure.get("structure_age"),

            "timestamp": structure.get("timestamp"),
        }

        memory_state = self.ai.memory.record_state(state)

        node_id = memory_state.get("node_id")
        mem_attr = memory_state.get("attractor")

        # --------------------------------------------------
        # REGIME PREDICTION
        # --------------------------------------------------
        prediction = self.ai.memory.predict_next_regime()

        future_weight = 1.0

        if prediction is not None:

            prob = float(prediction.get("probability", 0.0))

            if prob > 0.7:
                future_weight = 1.25
            elif prob < 0.3:
                future_weight = 0.75

        # --------------------------------------------------
        # SIDE BESTIMMEN
        # --------------------------------------------------
        if ml_side == "LONG":
            opp_side = "SHORT"
        elif ml_side == "SHORT":
            opp_side = "LONG"
        else:
            opp_side = "NONE"

        # --------------------------------------------------
        # REGIME EFFICIENCY
        # --------------------------------------------------
        eff_ml = self.ai.memory.regime_efficiency(
            energy,
            ml_side
        )

        rr_ml = self.ai.memory.regime_rr(
            energy,
            ml_side
        )

        entry_offset_ml = self.ai.memory.regime_entry_offset(
            energy,
            ml_side
        )

        eff_opp = self.ai.memory.regime_efficiency(
            energy,
            opp_side
        )

        rr_opp = self.ai.memory.regime_rr(
            energy,
            opp_side
        )

        entry_offset_opp = self.ai.memory.regime_entry_offset(
            energy,
            opp_side
        )

        # --------------------------------------------------
        # EXPERIENCE WEIGHT
        # --------------------------------------------------
        node_id = memory_state.get("node_id")

        experience = 1.0

        if node_id is not None:
            for node in self.ai.memory.regime_nodes:
                if node.node_id == node_id:
                    experience = min(1.5, 1.0 + (node.visits / 50.0))
                    break

        # --------------------------------------------------
        # SCORE BERECHNUNG
        # --------------------------------------------------
        score_ml = eff_ml * rr_ml * experience * future_weight
        score_opp = eff_opp * rr_opp

        # --------------------------------------------------
        # RR TARGET
        # --------------------------------------------------
        rr_target = rr_ml
        entry_offset = entry_offset_ml

        if score_opp > score_ml:
            rr_target = rr_opp
            entry_offset = entry_offset_opp

        # --------------------------------------------------
        # TRADE ERLAUBNIS
        # --------------------------------------------------
        allow = False

        if action in ["seek novelty", "engage socially", "observe / process"]:

            if max(score_ml, score_opp) > 0.0:
                allow = True

        # --------------------------------------------------
        # DIRECTION OVERRIDE
        # --------------------------------------------------
        ai_side = None

        if allow:

            if score_opp > score_ml and opp_side in ("LONG", "SHORT"):
                ai_side = opp_side
            else:
                ai_side = ml_side

        # --------------------------------------------------
        # RR CLAMP
        # --------------------------------------------------
        rr_target = max(
            float(getattr(Config, "MIN_RR", 2.0)),
            min(float(rr_target), float(getattr(Config, "MAX_RR", 4.0)))
        )

        # --------------------------------------------------
        # ENTRY REFINEMENT
        # --------------------------------------------------
        entry_structure = structure.get("entry_price")
        structure_range = structure.get("structure_range")

        entry_ai = None

        if entry_structure is not None and structure_range is not None:

            entry_structure = float(entry_structure)
            structure_range = float(structure_range)

            refine = max(0.0, float(entry_offset))
            if refine <= 0.0:
                refine = 0.15 * structure_range

            refine = min(refine, 0.50 * structure_range)

            if ai_side == "LONG":
                entry_ai = entry_structure - refine

            elif ai_side == "SHORT":
                entry_ai = entry_structure + refine

        # --------------------------------------------------
        # RETURN
        # --------------------------------------------------
        return {
            "allow": allow,
            "ml_side": ml_side,
            "ai_side": ai_side,
            "rr_target": rr_target,
            "entry_ai": entry_ai,
            "entry_offset": entry_offset,
            "stimulus": stimulus,
            "attractor": action,
            "efficiency": eff_ml,
            "memory_node_id": node_id,
            "memory_attractor": mem_attr,
        }