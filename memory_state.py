# ==================================================
# memory_state.py
# Persistente Erfahrungsspeicherung
# - Signature Memory
# - Context Cluster
# - MCM Memory
# ==================================================
import json
import os
from config import Config


# --------------------------------------------------
# PATH
# --------------------------------------------------
def _memory_state_path(path: str | None = None) -> str:

    if path is not None:
        return str(path)

    configured = getattr(Config, "MCM_MEMORY_STATE_PATH", "bot_memory/memory_state.json")
    configured = str(configured or "bot_memory/memory_state.json")
    return configured


# --------------------------------------------------
# FS
# --------------------------------------------------
def _ensure_dir(path: str):

    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)


# --------------------------------------------------
# CAST HELPERS
# --------------------------------------------------
def _to_int(value, default: int = 0) -> int:

    try:
        return int(value)
    except Exception:
        return int(default)


# --------------------------------------------------
def _to_float(value, default: float = 0.0) -> float:

    try:
        return float(value)
    except Exception:
        return float(default)


# --------------------------------------------------
def _to_str(value, default: str | None = None) -> str | None:

    if value is None:
        return default

    try:
        return str(value)
    except Exception:
        return default


# --------------------------------------------------
def _to_float_list(values) -> list[float]:

    cleaned = []

    for value in list(values or []):
        try:
            cleaned.append(float(value))
        except Exception:
            continue

    return cleaned


# --------------------------------------------------
def _to_str_list(values) -> list[str]:

    cleaned = []

    for value in list(values or []):
        if value is None:
            continue

        try:
            cleaned.append(str(value))
        except Exception:
            continue

    return cleaned


# --------------------------------------------------
# NORMALIZE SIGNATURE MEMORY
# --------------------------------------------------
def normalize_signature_memory(signature_memory) -> dict:

    normalized = {}

    if not isinstance(signature_memory, dict):
        return normalized

    for key, item in signature_memory.items():
        if key is None or not isinstance(item, dict):
            continue

        signature_key = str(key).strip()
        if not signature_key:
            continue

        normalized[signature_key] = {
            "seen": max(0, _to_int(item.get("seen", 0), 0)),
            "tp": max(0, _to_int(item.get("tp", 0), 0)),
            "sl": max(0, _to_int(item.get("sl", 0), 0)),
            "cancel": max(0, _to_int(item.get("cancel", 0), 0)),
            "timeout": max(0, _to_int(item.get("timeout", 0), 0)),
            "score": max(-6.0, min(6.0, _to_float(item.get("score", 0.0), 0.0))),
            "last_outcome": _to_str(item.get("last_outcome"), None),
            "age": max(0, _to_int(item.get("age", 0), 0)),
            "signature_vector": _to_float_list(item.get("signature_vector", [])),
        }

    if len(normalized) > 180:
        sorted_items = sorted(
            normalized.items(),
            key=lambda entry: (
                abs(_to_float((entry[1] or {}).get("score", 0.0), 0.0)),
                -max(0, _to_int((entry[1] or {}).get("age", 0), 0)),
                max(0, _to_int((entry[1] or {}).get("seen", 0), 0)),
            ),
            reverse=True,
        )[:180]
        normalized = dict(sorted_items)

    return normalized


# --------------------------------------------------
# NORMALIZE CONTEXT CLUSTERS
# --------------------------------------------------
def normalize_context_clusters(context_clusters) -> dict:

    normalized = {}

    if not isinstance(context_clusters, dict):
        return normalized

    for cluster_id, item in context_clusters.items():
        if cluster_id is None or not isinstance(item, dict):
            continue

        cluster_key = str(cluster_id).strip()
        if not cluster_key:
            continue

        normalized[cluster_key] = {
            "cluster_id": _to_str(item.get("cluster_id"), cluster_key),
            "center_vector": _to_float_list(item.get("center_vector", [])),
            "variance": max(0.0, _to_float(item.get("variance", 0.0), 0.0)),
            "radius": max(0.0, _to_float(item.get("radius", 0.0), 0.0)),
            "seen": max(0, _to_int(item.get("seen", 0), 0)),
            "tp": max(0, _to_int(item.get("tp", 0), 0)),
            "sl": max(0, _to_int(item.get("sl", 0), 0)),
            "cancel": max(0, _to_int(item.get("cancel", 0), 0)),
            "timeout": max(0, _to_int(item.get("timeout", 0), 0)),
            "score": max(-12.0, min(12.0, _to_float(item.get("score", 0.0), 0.0))),
            "trust": max(0.0, min(1.0, _to_float(item.get("trust", 0.0), 0.0))),
            "age": max(0, _to_int(item.get("age", 0), 0)),
            "signature_keys": _to_str_list(item.get("signature_keys", []))[-24:],
            "last_signature_key": _to_str(item.get("last_signature_key"), None),
            "last_outcome": _to_str(item.get("last_outcome"), None),
            "last_distance": max(0.0, _to_float(item.get("last_distance", 0.0), 0.0)),
        }

    return normalized


# --------------------------------------------------
# NORMALIZE MCM MEMORY
# --------------------------------------------------
def normalize_mcm_memory(memory_items) -> list[dict]:

    normalized = []

    for item in list(memory_items or []):
        if not isinstance(item, dict):
            continue

        normalized.append(
            {
                "center": _to_float(item.get("center", 0.0), 0.0),
                "strength": max(1, _to_int(item.get("strength", 1), 1)),
            }
        )

    normalized = sorted(
        normalized,
        key=lambda item: max(1, _to_int(item.get("strength", 1), 1)),
        reverse=True,
    )[:24]

    return normalized


# --------------------------------------------------
# BUILD STATE
# --------------------------------------------------
def build_memory_state(bot) -> dict:

    if bot is None:
        return {
            "signature_memory": {},
            "context_clusters": {},
            "context_cluster_seq": 0,
            "last_signature_key": None,
            "last_signature_outcome": None,
            "last_signature_context": None,
            "last_context_cluster_id": None,
            "last_context_cluster_key": None,
            "mcm_memory": [],
            "mcm_last_attractor": None,
            "mcm_last_action": None,
        }

    mcm_memory = []
    mcm_brain = getattr(bot, "mcm_brain", None)

    if isinstance(mcm_brain, dict):
        memory_obj = mcm_brain.get("memory")
        memory_items = getattr(memory_obj, "memory", None)
        mcm_memory = normalize_mcm_memory(memory_items)

    return {
        "signature_memory": normalize_signature_memory(getattr(bot, "signature_memory", {})),
        "context_clusters": normalize_context_clusters(getattr(bot, "context_clusters", {})),
        "context_cluster_seq": max(0, _to_int(getattr(bot, "context_cluster_seq", 0), 0)),
        "last_signature_key": _to_str(getattr(bot, "last_signature_key", None), None),
        "last_signature_outcome": _to_str(getattr(bot, "last_signature_outcome", None), None),
        "last_signature_context": getattr(bot, "last_signature_context", None),
        "last_context_cluster_id": _to_str(getattr(bot, "last_context_cluster_id", None), None),
        "last_context_cluster_key": _to_str(getattr(bot, "last_context_cluster_key", None), None),
        "mcm_memory": mcm_memory,
        "mcm_last_attractor": _to_str(getattr(bot, "mcm_last_attractor", None), None),
        "mcm_last_action": _to_str(getattr(bot, "mcm_last_action", None), None),
    }


# --------------------------------------------------
# APPLY STATE
# --------------------------------------------------
def apply_memory_state(bot, state: dict | None) -> dict:

    payload = dict(state or {})

    if bot is None:
        return payload

    bot.signature_memory = normalize_signature_memory(payload.get("signature_memory", {}))
    bot.context_clusters = normalize_context_clusters(payload.get("context_clusters", {}))
    bot.context_cluster_seq = max(0, _to_int(payload.get("context_cluster_seq", 0), 0))

    bot.last_signature_key = _to_str(payload.get("last_signature_key"), None)
    bot.last_signature_outcome = _to_str(payload.get("last_signature_outcome"), None)
    bot.last_signature_context = payload.get("last_signature_context")
    bot.last_context_cluster_id = _to_str(payload.get("last_context_cluster_id"), None)
    bot.last_context_cluster_key = _to_str(payload.get("last_context_cluster_key"), None)
    bot.mcm_last_attractor = _to_str(payload.get("mcm_last_attractor"), None)
    bot.mcm_last_action = _to_str(payload.get("mcm_last_action"), None)

    mcm_brain = getattr(bot, "mcm_brain", None)
    if isinstance(mcm_brain, dict):
        memory_obj = mcm_brain.get("memory")
        if memory_obj is not None and hasattr(memory_obj, "memory"):
            memory_obj.memory = normalize_mcm_memory(payload.get("mcm_memory", []))

    return build_memory_state(bot)


# --------------------------------------------------
# READ
# --------------------------------------------------
def read_memory_state(path: str | None = None) -> dict:

    filepath = _memory_state_path(path)

    if not os.path.exists(filepath):
        return {
            "signature_memory": {},
            "context_clusters": {},
            "context_cluster_seq": 0,
            "last_signature_key": None,
            "last_signature_outcome": None,
            "last_signature_context": None,
            "last_context_cluster_id": None,
            "last_context_cluster_key": None,
            "mcm_memory": [],
            "mcm_last_attractor": None,
            "mcm_last_action": None,
        }

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except Exception:
        return {
            "signature_memory": {},
            "context_clusters": {},
            "context_cluster_seq": 0,
            "last_signature_key": None,
            "last_signature_outcome": None,
            "last_signature_context": None,
            "last_context_cluster_id": None,
            "last_context_cluster_key": None,
            "mcm_memory": [],
            "mcm_last_attractor": None,
            "mcm_last_action": None,
        }

    return {
        "signature_memory": normalize_signature_memory((raw or {}).get("signature_memory", {})),
        "context_clusters": normalize_context_clusters((raw or {}).get("context_clusters", {})),
        "context_cluster_seq": max(0, _to_int((raw or {}).get("context_cluster_seq", 0), 0)),
        "last_signature_key": _to_str((raw or {}).get("last_signature_key"), None),
        "last_signature_outcome": _to_str((raw or {}).get("last_signature_outcome"), None),
        "last_signature_context": (raw or {}).get("last_signature_context"),
        "last_context_cluster_id": _to_str((raw or {}).get("last_context_cluster_id"), None),
        "last_context_cluster_key": _to_str((raw or {}).get("last_context_cluster_key"), None),
        "mcm_memory": normalize_mcm_memory((raw or {}).get("mcm_memory", [])),
        "mcm_last_attractor": _to_str((raw or {}).get("mcm_last_attractor"), None),
        "mcm_last_action": _to_str((raw or {}).get("mcm_last_action"), None),
    }


# --------------------------------------------------
# LOAD
# --------------------------------------------------
def load_memory_state(bot, path: str | None = None) -> dict:

    state = read_memory_state(path)
    return apply_memory_state(bot, state)


# --------------------------------------------------
# SAVE
# --------------------------------------------------
def save_memory_state(bot, path: str | None = None) -> dict | None:

    if bot is None:
        return None

    filepath = _memory_state_path(path)
    payload = build_memory_state(bot)

    try:
        _ensure_dir(filepath)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
    except Exception:
        return None

    return payload