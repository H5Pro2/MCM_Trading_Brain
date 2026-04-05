# --------------------------------------------------
# Beobachtung
# --------------------------------------------------

* `README.md` und `UMSETZUNGSPLAN.md` führen die Basis nicht mehr als offenen Altblock, sondern nur noch den offenen Erweiterungsstand.

* `README.md` ist jetzt zusätzlich auf die Zielarchitektur mit **3 Ebenen** ausgerichtet:

  * Ebene 1 = sehen / äußeres Wahrnehmen
  * Ebene 2 = denken / inneres Wahrnehmen / Handeln
  * Ebene 3 = Entwicklung aus Erfahrung / Verarbeitung / Wahrnehmung.

* `MCM_Brain_Modell.py`

  * `register_pending_learning_context(...)` setzt Pending-Kontext.
  * `commit_pending_learning_context(...)` schreibt Signature/Cluster erst mit `outcome`.
  * `apply_outcome_stimulus(...)` ruft dieses Commit im Outcome-Pfad auf.
  * `update_experience_state(...)` verarbeitet `attempt_density`, `overtrade_pressure`, `context_quality`, `fill_ratio`, `timeout_ratio`, `blocked_ratio`.
  * `build_outcome_decomposition(...)` koppelt `attempt_density`, `overtrade_pressure`, `context_quality` bereits in die Qualitätswerte zurück.
  * `MCMBrainRuntime` / Runtime-Snapshot / Episode / Experience-Space sind als Architekturbausteine bereits vorhanden.

* `bot_gate_funktions.py`

  * gibt weiter `world_state`, `structure_perception_state`, `outer_visual_perception_state`, `inner_field_perception_state`, `processing_state`, `perception_state`, `felt_state`, `thought_state`, `meta_regulation_state`, `expectation_state`, `state_signature` zurück.

* `bot.py`

  * Exit-Pfad trägt `context=dict(self.position.get("meta", {}) ...)` und `outcome_decomposition` an `stats.on_exit(...)` weiter.
  * Backtest-Pending-Timeout ruft `apply_outcome_stimulus(self, "timeout", self.pending_entry)` und danach `stats.on_cancel(... outcome_decomposition=..., context=meta)` auf.
  * Gate-Block erzeugt `blocked_context`, ruft `stats.on_attempt(status="blocked_value_gate", ...)` und danach `apply_outcome_stimulus(...)`.
  * Attempt-Persistenzpfade für `submitted`, `filled`, `timeout`, `blocked_value_gate`, `cancelled` sind angeschlossen.

* `trade_stats.py`

  * hält `recent_attempts` weiter im Hauptfile `trade_stats.json`.
  * entfernt Altfelder `attempt_records` und `outcome_records` beim Laden und Snapshot.
  * schreibt Attempt-Details separat nach `attempt_records.jsonl`.
  * schreibt Outcome-Details separat nach `outcome_records.jsonl`.
  * baut KPI-Nachweis mit `attempt_density`, `context_quality`, `overtrade_pressure` aus den Record-Dateien auf.

* `memory_state.py`

  * persistiert bereits Runtime-, Episode- und Experience-Zustände.
  * bildet damit die Persistenzbasis für Innenprozess und Entwicklungsebene.

* Tests

  * `test_mcm_brain_learning_timing.py` deckt Entry-vs-Outcome-Lernzeitpunkt ab.
  * `test_trade_stats_outcome_decomposition.py` deckt Attempt-/Outcome-Seitendateien und `last_outcome_decomposition` ab.
  * `test_bot_timeout_outcome_persistence.py` deckt Pending-Timeout → Outcome-Decomposition → Cancel-Persistenz ab.
  * `test_bot_pending_fill_persistence.py` deckt Pending → Fill → Attempt-Persistenz ab.
  * `test_bot_live_cancel_persistence.py` deckt Live-Cancel → Meta + Outcome-Decomposition → Persistenz ab.
  * Kein eigener dedizierter Teststand für `bot_gate_funktions.py` sichtbar.
  * Kein eigener dedizierter Teststand für `mcm_core_engine.py` sichtbar.

# --------------------------------------------------
# Interpretation
# --------------------------------------------------

* **P0 ist umgesetzt.**

  * Entry lernt nicht direkt.
  * Outcome ist der zentrale Lernschreibpunkt.
  * Der Regressionsnachweis dafür ist vorhanden.

* **P1 ist umgesetzt.**

  * `trade_stats.json` ist auf Aggregate + Kurzinfos reduziert.
  * Attempt-/Outcome-Details liegen getrennt in JSONL-Seitendateien.
  * Attempt-/Outcome-Record-Struktur ist funktional getrennt.

* **P2 ist fast vollständig umgesetzt.**

  * Outcome-Rückkopplung auf Attempt-Dichte / Overtrade / Kontextqualität ist im Brain-Pfad vorhanden.
  * KPI-/Nachweis-Schicht dafür ist in `trade_stats.py` vorhanden.
  * `bot.py`-Teststand für Pending → Fill, Pending → Timeout und Live-Cancel ist vorhanden.
  * Offen bleiben nur dedizierte Tests für Gate und Core.

* **Die alte Fix-Liste ist damit praktisch abgearbeitet.**

  * Der verbleibende Hauptblock liegt nicht mehr in P0/P1.
  * Der verbleibende Hauptblock liegt jetzt im offenen Architekturplan: permanenter Innenprozess, Runtime-Trennung, Entscheidungsepisode, interner Erfahrungsraum.

* **Der Architekturblock ist fachlich präzisiert.**

  * Es geht nicht nur um Thread 1 vs. Thread 2.
  * Es geht um das Zusammenspiel von:

    * äußerem Wahrnehmen
    * innerem Wahrnehmen / Denken / Handeln
    * Entwicklung aus Erfahrung.

* **Die eigentliche offene Arbeit liegt damit im Endausbau der Zielarchitektur.**

  * Ebene 1 soll nur sehen.
  * Ebene 2 soll nur intern verarbeiten, denken und handeln.
  * Ebene 3 soll aus Episoden, Reviews und Outcomes die langfristige Entwicklung formen.

# --------------------------------------------------
# Schlussfolgerung
# --------------------------------------------------

* **Fix-Liste aktuell**

  * **P0**

    * erledigt
    * nur Regression halten:

      * Entry darf nur Pending-Kontext setzen
      * Outcome darf erst Signature/Cluster schreiben

  * **P1**

    * erledigt
    * nur Regression halten:

      * `trade_stats.json` bleibt frei von `attempt_records` / `outcome_records`
      * Attempts bleiben in `attempt_records.jsonl`
      * Outcomes bleiben in `outcome_records.jsonl`

  * **P2**

    * offen bleiben nur Tests:

      * `bot_gate_funktions.py`

        * Übergabe aller Zustandsblöcke
      * `mcm_core_engine.py`

        * stabile Tension-/State-Ausgabe

  * **P3**

    * offener Architektur-Endausbau gemäß `UMSETZUNGSPLAN.md`:

      * permanenter Innenprozess vollständig zu Ende ziehen
      * harte Runtime-Bahntrennung weiter vervollständigen
      * Entscheidungsepisode vollständig ausbauen
      * internen Erfahrungsraum weiter vertiefen
      * Nicht-Handlung / Review / KPI-Ebene weiter ausbauen
      * Zielarchitektur auf 3 Ebenen sauber zu Ende führen:

        * Ebene 1 = sehen / äußeres Wahrnehmen
        * Ebene 2 = denken / inneres Wahrnehmen / Handeln
        * Ebene 3 = Entwicklung aus Erfahrung / Verarbeitung / Wahrnehmung

* **Priorisierte Reihenfolge**

  Test_Fix:
  * 1. Tests für `bot_gate_funktions.py` ergänzen
  * 2. Tests für `mcm_core_engine.py` ergänzen

  Umsetzung:
  * Prio | 1. offener Architekturplan `UMSETZUNGSPLAN.md`
  * Prio | 2. 3-Ebenen-Zielarchitektur in Runtime-/Episode-/Experience-Pfad vollständig angleichen

