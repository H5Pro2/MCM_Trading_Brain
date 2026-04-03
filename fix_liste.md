# --------------------------------------------------

# Beobachtung

# --------------------------------------------------

* README und Umsetzungsplan verlangen weiter:

  * Struktur nur als Wahrnehmung
  * Außen-/Innenzustand getrennt
  * Trade-Versuche als eigenes Lernobjekt
  * Outcome-Rückkopplung mit Kontext
  * Overtrade über Erfahrung statt starre Verbote.  
* `MCM_Brain_Modell.py`

  * `register_pending_learning_context(...)` setzt nur Pending-Signature/Cluster-Zuordnung.
  * `commit_pending_learning_context(...)` schreibt Signature/Cluster erst mit `outcome`.
  * `apply_outcome_stimulus(...)` ruft dieses Commit im Outcome-Pfad auf.  
* `bot_gate_funktions.py`

  * gibt `world_state`, `structure_perception_state`, `outer_visual_perception_state`, `inner_field_perception_state`, `processing_state`, `perception_state`, `felt_state`, `thought_state`, `meta_regulation_state`, `expectation_state`, `state_signature` weiter. 
* `bot.py`

  * Exit-Pfad trägt `context=dict(self.position.get("meta", {}) ...)` und `outcome_decomposition` an `stats.on_exit(...)` weiter.
  * Backtest-Pending-Timeout ruft `apply_outcome_stimulus(self, "timeout", self.pending_entry)` und danach `stats.on_cancel(... outcome_decomposition=..., context=meta)` auf.
  * Gate-Block erzeugt `blocked_context`, ruft `stats.on_attempt(status="blocked_value_gate", ...)` und danach `apply_outcome_stimulus(...)`.   
* `trade_stats.py`

  * hält weiterhin `recent_attempts`, `attempt_records`, `outcome_records` im Hauptfile `trade_stats.json`.
  * `on_exit(...)` schreibt `outcome_records`.
  * `on_attempt(...)` erhöht Zähler und `recent_attempts`; aus dem sichtbaren Stand ist dort kein eigener persistenter `attempt_records`-Append erkennbar.  
* Älterer Stand mit `self.stats._save()` direkt nach `current_timestamp` ist nicht mehr der aktuelle Stand; das ist nur in älteren Dateiständen sichtbar.   

# --------------------------------------------------

# Interpretation

# --------------------------------------------------

* **P0 ist aktuell umgesetzt.**

  * Entry lernt nicht mehr direkt.
  * Outcome ist der zentrale Lernschreibpunkt.  
* **P1 ist nur teilweise umgesetzt.**

  * Meta-/State-Kette wird durchgereicht.
  * Timeout-Pfad ist geschlossen.
  * Aber das vollständige Lernobjekt liegt weiter nicht sauber getrennt vor, weil `trade_stats.json` weiterhin Detail-Records im Hauptfile trägt und `attempt_records` im sichtbaren Stand nicht analog zu `outcome_records` befüllt wirkt.   
* **P2 bleibt offen.**

  * README/Plan fordern stärkere Rückkopplung von Versuchsdichte / Overtrade / Kontextqualität.
  * Im sichtbaren Outcome-Pfad ist diese Schärfung noch nicht erkennbar; `update_experience_state(...)` arbeitet mit Zuständen, aber die Attempt-Metriken sind daraus nicht sichtbar gekoppelt.  
* **Tests bleiben der größte Nachweis-Blocker.**

  * Im geprüften Stand ist weiter nur `trade_stats` funktional sichtbar ausgebaut; zusätzliche Absicherung für Brain / Gate / Pending-Kette ist aus den vorliegenden Dateien nicht nachgewiesen. 

# --------------------------------------------------

# Schlussfolgerung

# --------------------------------------------------

* **Fix-Liste aktuell**

  * **P0**

    * kein Fix mehr als Pflichtblocker
    * nur Regression absichern:

      * Entry darf nur Pending-Kontext setzen
      * Outcome darf erst Signature/Cluster schreiben.  

  * **P1**

    * `trade_stats.json` entschlacken

      * `attempt_records` / `outcome_records` aus Hauptfile auslagern oder getrennt persistieren
      * Hauptfile nur für Aggregate + letzte Kurzinfos halten. 
    * `attempt_records` vollständig schreiben

      * `submitted`
      * `filled`
      * `cancelled` / `timeout`
      * `blocked_value_gate`
      * jeweils aus `pending_entry["meta"]` bzw. Attempt-Kontext.  
    * Attempt-/Outcome-Record formal trennen

      * Versuchsobjekt separat
      * Outcome-Objekt separat
      * Verknüpfung über Timestamp / Signature / Cluster / Event-Typ. 

  * **P2**

    * Tests ergänzen:

      * `MCM_Brain_Modell.py`

        * Entry lernt nicht
        * Outcome lernt
      * `bot.py`

        * Pending → Fill
        * Pending → Timeout
        * Live/Cancel → Meta + Outcome-Decomposition
      * `bot_gate_funktions.py`

        * Übergabe aller Zustandsblöcke
      * `mcm_core_engine.py`

        * stabile Tension-/State-Ausgabe.  
    * Outcome-Rückkopplung schärfen

      * Attempt-Dichte
      * Overtrade
      * Kontextqualität
      * diese Größen in `update_experience_state(...)` / Outcome-Pfad einspeisen.  

* **Priorisierte Reihenfolge**

  * 1. `trade_stats.py` Record-Struktur bereinigen
  * 2. vollständige Attempt-/Outcome-Persistenz aufbauen
  * 3. Tests für Brain / Bot / Gate / Core nachziehen
  * 4. Outcome-Rückkopplung um Attempt-Dichte / Overtrade / Kontextqualität erweitern

---

geändert wurde:
keine datei
