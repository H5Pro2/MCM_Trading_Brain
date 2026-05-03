# ============================================================
# debug_reader.py
# ============================================================
#   msg
#   Typ: beliebig → str(msg)
#   Bedeutung: zu schreibender Inhalt (eine Zeile)
#   path = "debug/debug.txt"
#   Typ: str
#   Bedeutung: Zieldatei
#   mode = "a"
#   Typ: str
#   "a" = anhängen
#   "w" = überschreiben
#   reset_on_start = True
#   Typ: bool
#   True = Datei einmalig beim Start löschen
#   False = Datei nie automatisch löschen
#   write_once = False
#   Typ: bool
#   True = immer mode="w" → nur eine Zeile, wird überschrieben
#   False = mode bleibt wie übergeben ("a" oder "w")
# ============================================================
import os
import time
from config import Config
_RESET_DONE = set()
_DEBUG_COUNTERS = {}
_PROFILE_HEADER_DONE = set()
_FILE_PROFILE_HEADER_DONE = set()
# ─────────────────────────────────────────────
def _ensure_dir(path: str):
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)
# ─────────────────────────────────────────────
def dbr_file_write_profile(path, elapsed_ms, bytes_written=0, operation="write", extra=None):
    try:
        if not bool(getattr(Config, "MCM_FILE_WRITE_PROFILE_DEBUG", False)):
            return

        elapsed = float(elapsed_ms or 0.0)
        min_ms = max(0.0, float(getattr(Config, "MCM_FILE_WRITE_PROFILE_MIN_MS", 0.0) or 0.0))
        if elapsed < min_ms:
            return

        profile_path = os.path.join("debug", "mcm_file_write_profile.csv")
        normalized_path = str(path or "-").replace("\\", "/")
        if normalized_path.endswith("debug/mcm_file_write_profile.csv"):
            return

        every_n = max(1, int(getattr(Config, "MCM_FILE_WRITE_PROFILE_EVERY_N", 1) or 1))
        count_key = f"file_profile::{normalized_path}"
        count = int(_DEBUG_COUNTERS.get(count_key, 0) or 0) + 1
        _DEBUG_COUNTERS[count_key] = count
        if (count % every_n) != 0:
            return

        _ensure_dir(profile_path)
        if profile_path not in _FILE_PROFILE_HEADER_DONE:
            if os.path.exists(profile_path):
                os.remove(profile_path)
            with open(profile_path, "w", encoding="utf-8") as f:
                f.write("timestamp;path;operation;elapsed_ms;bytes_written;extra\n")
            _FILE_PROFILE_HEADER_DONE.add(profile_path)

        cleaned_path = normalized_path.replace("\n", " ").replace(";", "|")
        cleaned_operation = str(operation or "write").replace("\n", " ").replace(";", "|")
        cleaned_extra = str(extra or "").replace("\n", " ").replace(";", "|")

        with open(profile_path, "a", encoding="utf-8") as f:
            f.write(
                f"{time.time():.6f};{cleaned_path};{cleaned_operation};"
                f"{elapsed:.4f};{int(bytes_written or 0)};{cleaned_extra}\n"
            )
    except Exception:
        pass
# ZENTRALES BACKEND
# ─────────────────────────────────────────────
def dbr_write(
    msg,
    path: str,
    mode: str = "a",
    reset_on_start: bool = False,
    write_once: bool = False,
):
    try:
        if msg is None:
            return

        s = str(msg)
        if not s:
            return

        _ensure_dir(path)

        if reset_on_start and path not in _RESET_DONE:
            if os.path.exists(path):
                os.remove(path)
            _RESET_DONE.add(path)

        if write_once:
            mode = "w"

        if mode == "a" and not write_once:
            every_n = max(1, int(getattr(Config, "DEBUG_WRITE_EVERY_N", 1) or 1))
            if every_n > 1:
                count = int(_DEBUG_COUNTERS.get(path, 0) or 0) + 1
                _DEBUG_COUNTERS[path] = count
                if (count % every_n) != 0:
                    return

        profile_start = time.perf_counter()
        with open(path, mode, encoding="utf-8") as f:
            f.write(s + "\n")
        dbr_file_write_profile(
            path,
            (time.perf_counter() - profile_start) * 1000.0,
            bytes_written=len((s + "\n").encode("utf-8")),
            operation=f"dbr_write:{mode}",
        )

    except Exception:
        pass

# ─────────────────────────────────────────────
# WRAPPER (API-KOMPATIBEL)
# ─────────────────────────────────────────────
def dbr_debug(msg,txt="debug.csv"):
    dbr_write(msg, os.path.join("debug", txt), "a", True, False)
# ─────────────────────────────────────────────
def dbr_profile(section, elapsed_ms, extra=None, txt="mcm_profile.csv"):
    try:
        if not bool(getattr(Config, "MCM_RUNTIME_PROFILE_DEBUG", False)):
            return

        elapsed = float(elapsed_ms or 0.0)
        min_ms = max(0.0, float(getattr(Config, "MCM_RUNTIME_PROFILE_MIN_MS", 0.0) or 0.0))

        if elapsed < min_ms:
            return

        path = os.path.join("debug", str(txt or "mcm_profile.csv"))
        _ensure_dir(path)

        every_n = max(1, int(getattr(Config, "MCM_RUNTIME_PROFILE_EVERY_N", 1) or 1))
        count_key = f"profile::{path}"
        count = int(_DEBUG_COUNTERS.get(count_key, 0) or 0) + 1
        _DEBUG_COUNTERS[count_key] = count

        if (count % every_n) != 0:
            return

        if path not in _PROFILE_HEADER_DONE:
            if os.path.exists(path):
                os.remove(path)

            profile_config = (
                f"profile_debug={bool(getattr(Config, 'MCM_RUNTIME_PROFILE_DEBUG', False))}|"
                f"profile_min_ms={float(getattr(Config, 'MCM_RUNTIME_PROFILE_MIN_MS', 0.0) or 0.0)}|"
                f"profile_every_n={int(getattr(Config, 'MCM_RUNTIME_PROFILE_EVERY_N', 1) or 1)}|"
                f"snapshot_every_n={int(getattr(Config, 'MCM_VISUAL_SNAPSHOT_WRITE_EVERY_N', 1) or 1)}|"
                f"snapshot_force_on_state_change={bool(getattr(Config, 'MCM_VISUAL_SNAPSHOT_FORCE_ON_STATE_CHANGE', True))}|"
                f"memory_save_cooldown={float(getattr(Config, 'MCM_MEMORY_SAVE_COOLDOWN_SECONDS', 0.0) or 0.0)}"
            )
            profile_config = str(profile_config or "").replace("\n", " ").replace(";", "|")

            header_line = "section;elapsed_ms;extra\n"
            config_line = f"__profile_config__;0.0000;{profile_config}\n"
            profile_start = time.perf_counter()
            with open(path, "w", encoding="utf-8") as f:
                f.write(header_line)
                f.write(config_line)
            dbr_file_write_profile(
                path,
                (time.perf_counter() - profile_start) * 1000.0,
                bytes_written=len((header_line + config_line).encode("utf-8")),
                operation="profile_header",
            )
            _PROFILE_HEADER_DONE.add(path)

        cleaned_extra = str(extra or "").replace("\n", " ").replace(";", "|")

        line = f"{section};{elapsed:.4f};{cleaned_extra}\n"
        profile_start = time.perf_counter()
        with open(path, "a", encoding="utf-8") as f:
            f.write(line)
        dbr_file_write_profile(
            path,
            (time.perf_counter() - profile_start) * 1000.0,
            bytes_written=len(line.encode("utf-8")),
            operation="profile_append",
        )

    except Exception:
        pass
# ─────────────────────────────────────────────
