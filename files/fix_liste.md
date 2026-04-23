# ==================================================
# FIX-LISTE – AKTUALISIERT AUF REALEN CODESTAND
# ==================================================

Diese Liste enthält nur noch reale offene Punkte aus dem aktuellen Dateistand.

Bereits umgesetzte Korrekturen wurden aus dem offenen PRIO-1-Block entfernt.
Architektur-Ausbau und fachlicher Ausbau bleiben getrennt.

---

# --------------------------------------------------
# 1. STATUS
# --------------------------------------------------

Das Projekt ist nicht mehr in einer frühen Fix- oder Basisphase.

Die Kernmechanik steht bereits:

- äußere Wahrnehmung
- innere Runtime
- Entscheidungstendenz
- Action-Intent / Execution-State
- technische Handlungsbahn
- Episode / Review / Experience
- Persistenz
- Snapshot-/GUI-Basis

Offen sind jetzt nicht mehr die alten Basisfehler,
sondern ein kleiner Restblock im Nachweisraum sowie der weitere Architektur-Endausbau.

---

# --------------------------------------------------
# 2. BEREITS KORRIGIERT IM AKTUELLEN CODESTAND
# --------------------------------------------------

# --------------------------------------------------
# 2.1 state_delta korrigiert
# --------------------------------------------------

Bereits umgesetzt:

- ereignislokale Bildung von `state_before`, `state_after`, `state_delta`
- gemeinsamer Übergang für Stats-Kontext und Episode-Payload
- Snapshot-Commit erst nach dem jeweiligen Event
- alte Null-/Doppelsnapshot-Pfade in Entry-/Pending-/Nicht-Handlungs-Pfaden bereinigt

Folge:

- Episode / Experience arbeiten an diesen Stellen wieder auf realen Zustandsübergängen

---

# --------------------------------------------------
# 2.2 Statistik-Semantik korrigiert
# --------------------------------------------------

Bereits umgesetzt:

- `pnl_netto` startet als reiner Nettowert bei `0.0`
- `current_equity` wird getrennt als `start_equity + pnl_netto` geführt
- `expectancy` baut damit auf realem Nettowert statt auf Equity-Basis auf

Folge:

- Nettoergebnis und Erwartungswert sind semantisch wieder sauber getrennt

---

# --------------------------------------------------
# 2.3 structure_bands / Exit-Strukturdiagnose korrigiert
# --------------------------------------------------

Bereits umgesetzt:

- Exit-/Cancel-Pfade nutzen aktuellen Exit-Kontext statt alten Entry-Kontext
- aktuelle `structure_perception_state` läuft bis in `on_exit()` / `on_cancel()`
- `outcome_records` tragen reale Exit-Strukturqualität
- `structure_bands` werden daraus sauber neu aufgebaut

Folge:

- Exit-KPI über Strukturqualität ist im aktuellen Backtest-/Bot-Pfad wieder fachlich belastbar

---

# --------------------------------------------------
# 2.4 attempt_feedback / proof-Felder korrigiert
# --------------------------------------------------

Bereits umgesetzt:

- Proof-/Regulationsfelder werden im Attempt-Feedback sauber aggregiert
- Snapshot-Fallbacks sind vorhanden
- In-Trade-Update-Pfade tragen die fehlenden Felder weiter
- Experience-Linking / Episode-History führt diese Felder weiter

Bereits sauber geführt insbesondere:

- `regulatory_load`
- `action_capacity`
- `survival_pressure`
- `pressure_release`
- `load_bearing_capacity`
- `state_stability`
- `capacity_reserve`
- `recovery_balance`

Folge:

- die alte statistische Abflachung dieser Diagnosegrößen ist im aktuellen Code nicht mehr der Hauptfehler

---

# --------------------------------------------------
# 3. PRIO 1 – REALE OFFENE KORREKTUREN
# --------------------------------------------------

# --------------------------------------------------
# 3.1 Nachweisraum / Live-Handoff zwischen Pending, Fill und Position schließen
# --------------------------------------------------

Zwingend offen:

- `_handle_pending_entry()` schreibt im Live-Pfad zwar `pending_update`, kehrt danach aber direkt mit `return True` zurück
- der Bot-seitige `filled`-Übergang mit `stats.on_attempt(status="filled")`, Episode-Event und `self.position`-Aufbau existiert aktuell nur im Nicht-Live-/Backtest-Pfad
- `get_active_order_snapshot()` liefert offene Orders, aber keinen Bot-seitig formalisierten Übergang von gefüllter Live-Order zu aktiver Position
- der Exchange-Sync erkennt offene Positionen failsafe-seitig, aber dieser Zustand wird noch nicht als vollständiger Bot-/Episode-/Stats-Handoff geführt

Folge:

- Backtest- und Live-Nachweisraum sind im Übergang `pending -> filled -> position` noch nicht gleichwertig
- ein Teil des realen Live-Handlungsverlaufs bleibt im Bot-internen Nachweisraum strukturell unvollständig

---

# --------------------------------------------------
# 4. PRIO 2 – STRUKTURELLE KORREKTUREN
# --------------------------------------------------

# --------------------------------------------------
# 4.1 Persistenz weiter entkoppeln
# --------------------------------------------------

Offen, aber nicht mehr maximal kritisch:

- Persistenz ist bereits über Dirty-Flag und Cooldown teilweise entschärft
- trotzdem liegen Save-/Flush-Pfade weiter nah am Kernlauf

Folge:

- Bot-Kern bleibt unnötig eng mit Save-/Flush-Logik gekoppelt

Wichtig:

- das ist ein realer Punkt
- aber kein ungefilterter Dauer-Schreibfehler mehr

---

# --------------------------------------------------
# 4.2 Runtime / Bot-State weiter trennen
# --------------------------------------------------

Offen:

- `Bot` bündelt weiter Außenwahrnehmung, Runtime, Handlungsbahn, Experience, Persistenz und Snapshot-Orchestrierung
- die Zieltrennung Ebene 1 / Ebene 2 / Ebene 3 ist damit noch nicht strukturell verhärtet

Ziel:

- weniger Vermischung von Runtime und Bot-State
- klarere Trennung von Wahrnehmung / Innenprozess / Entwicklung

---

# --------------------------------------------------
# 4.3 Innenkontextcluster als Innenfeldspeicher vertiefen
# --------------------------------------------------

Offen:

- der Innenraum wird bereits real über `felt_state`, `thought_state`, `meta_regulation_state`, `expectation_state`, `state_before`, `state_after`, `state_delta` und `mcm_experience_space` getragen
- `inner_context_clusters` sind im aktuellen Code bereits formal vorhanden, werden aktualisiert und persistiert
- noch nicht erreicht ist der Endausbau zu einem tieferen Innenmuster- und Innenfeldspeicher für wiederkehrende innere Spannungs-, Drift-, Regulations- und Reorganisationsmuster

Ziel:

- `context_clusters` als äußerer / gesamt-situativer Signaturraum klar halten
- `inner_context_clusters` fachlich davon getrennt als Innenmuster- / Innenfeldspeicher vertiefen
- Vermeidungs-, Entlastungs-, Reorganisations- und Wiedererkennungslernen sauber auf Innenmuster abbilden

---

# --------------------------------------------------
# 4.4 Experience-Bewertungslogik auf Zustandswirkung umstellen
# --------------------------------------------------

Offen:

- `_experience_reward_delta()` verzweigt weiterhin direkt über `tp_hit`, `sl_hit`, `cancel`, `timeout` und ähnliche Outcome-Wege
- Outcome-Gewicht ist damit reduziert, aber noch nicht weit genug zurückgebaut
- Experience bewertet bereits Teile von `state_delta`, aber das formale Ergebnis dominiert fachlich noch zu stark
- lokale Rückführung auf `inner_context_clusters`, Feldmuster und neuronale Teilträger wäre so noch zu stark von Ergebnisetiketten geprägt
- Nicht-Handlung, Cancel oder Timeout können regulatorisch sinnvoll sein, werden aber noch nicht konsequent primär als Zustandswirkung behandelt

Ziel:

- Experience bewertet primär `state_before`, `state_after`, `state_delta` und Tragfähigkeitswirkung
- `tp_hit`, `sl_hit`, `cancel`, `timeout` bleiben nur Ereigniskontext
- positive und negative Rückführung entsteht aus Belastung, Entlastung, Stabilisierung, Fragilisierung und Handlungsfähigkeit
- lokale Rückführung auf Innenmuster, `inner_context_clusters` und neuronale Teilträger erfolgt erst auf dieser Grundlage
- Lernen wird dadurch sauberer als Umgangsfähigkeit statt Ergebnisreflex modelliert

---

# --------------------------------------------------
# 4.5 MCM-Feldtopologie / Feldverlauf / Innenfeldspeicher ausbauen
# --------------------------------------------------

Offen:

- das MCM-Feld erkennt bereits laufende Feldcluster, reduziert diese aktuell aber zu stark auf kompakte Feldwerte und verdichtete Memory-Formen
- die Gesamtorganisation des Agentenfeldes ist noch nicht als eigene Feldwahrnehmung formalisiert
- Feldtopologie, Clusterbeziehungen, Driftverlauf, Fragmentierung, Verschmelzung und Rückführungsbewegung werden noch nicht als eigener Innenkontext sauber mitgeführt
- ein eigener persistenter Speicher für wiederkehrende Feldformen, Driftmuster und Regulationsverläufe fehlt aktuell
- die Visualisierung bildet das MCM-Feld bislang noch nicht als räumlich-dynamischen Innenraum ab

Ziel:

- Feldcluster nicht nur erkennen, sondern in ihrer Größe, Dichte, Stabilität, Verschiebung und Beziehung zueinander lesbar machen
- die Gesamtform des MCM-Feldes als Feldtopologie beschreiben: Verdichtung, Streuung, Brücken, Trennung, Polarisierung, Rückführung
- Feldverlauf über Zeit mitführen, damit kognitive Verlagerung, Drift und regulatorische Reorganisation als Zustandsweg erkennbar werden
- einen verdichteten Innenfeldspeicher für wiederkehrende Clusterkonfigurationen, Feldformen, Driftmuster und Rückführungsbewegungen aufbauen
- diese Feldwahrnehmung direkt für Meta-Regulation, Handlungstendenz und Visualisierung nutzbar machen

---

# --------------------------------------------------
# 5. PRIO 3 – FACHLICHER AUSBAU
# --------------------------------------------------

# --------------------------------------------------
# 5.1 Review / Cluster-Bewertung weiter vertiefen
# --------------------------------------------------

Teilweise bereits umgesetzt:

- Tragfähigkeit ist bereits stärker als explizite Bewertungsgröße verankert
- Lernen ist bereits erkennbar stärker als Umgangsfähigkeit modelliert
- Reibung / Energie sind bereits über `bearing_regulation_cost`, `relief_quality`, `carrying_room`, `felt_bearing`, `felt_regulation_quality`, `experience_friction_cost` und `experience_energy_cost` technisch verankert
- `review_notes` bewertet bereits stärker Tragfähigkeit, Regulationskosten, Entlastung und Handlungsspielraum statt nur klassisch Ergebnis / Trade-Ausgang

Noch offen:

- Review und Cluster-Bewertung stärker auf Tragfähigkeit statt Ergebnis ausrichten
- innere Musterbewertung deutlicher von Geld- und Trade-Etiketten lösen
- Outcome noch klarer als Zustandswirkung statt Geldwirkung ausformen
- Lernen als Umgangsfähigkeit technisch noch konsequenter durchziehen
- nach der Grundumstellung der Experience-Bewertung die Folgeauswertung in Reviews, Link-Buckets und Cluster-Scoring nachziehen

---

# --------------------------------------------------
# 5.2 KPI / Auswertung umbauen
# --------------------------------------------------

Noch offen:

- klassische Trade-KPIs als Hauptbewertung weiter zurückbauen oder umordnen
- Tragfähigkeit, innere Reibung, Belastung, Entlastung und Handlungsfähigkeit stärker als Nachweisgrößen aufbauen
- alte Ergebnislogik weiter zurückdrängen

Aktuell weiterhin alt geprägt:

- `pnl_tp`
- `pnl_sl`
- `equity_peak`
- `max_drawdown_abs`
- `max_drawdown_pct`
- `winrate`
- `profit_factor`

---

# --------------------------------------------------
# 5.3 GUI / Visualisierung umbauen
# --------------------------------------------------

Noch offen:

- GUI weiter von alter KPI-Zentrierung lösen
- Außenwelt / Innenwelt / Entwicklung noch klarer trennen
- Experience- und Tragfähigkeitsverlauf stärker in den Mittelpunkt stellen

Wichtig:

- Snapshot-/GUI-Basis ist vorhanden
- Datenpufferung ist bereits umgesetzt
- offen ist der inhaltliche Umbau, nicht mehr die reine Grundanzeige

---

# --------------------------------------------------
# 5.4 Tests ergänzen
# --------------------------------------------------

Noch offen:

- dedizierte Tests für `bot_gate_funktions.py`
- dedizierte Tests für `mcm_core_engine.py`
- Fokus auf Zustandsentwicklung und Experience-Konsistenz
- Fokus nicht primär auf klassische Trade-Erfolgsmetriken

---

# --------------------------------------------------
# 6. AUS DER ALTEN OFFEN-LISTE ENTFERNEN
# --------------------------------------------------

Nicht mehr als offene Fix-Punkte führen:

- `2.1 state_delta korrigieren`
- `2.2 Statistik-Semantik korrigieren`
- `2.3 structure_bands / Exit-Strukturdiagnose korrigieren`
- `2.4 attempt_feedback / proof-Felder korrigieren`
- äußere Wahrnehmungsbasis
- MCM-Runtime-Grundmechanik
- Entscheidungstendenz
- Action-Intent- / Execution-State-Grundmechanik
- technische Handlungsbahn
- Nicht-Handlung als echter Pfad
- Episode / Review / Experience-Basis
- Persistenz-Grundmechanik
- Snapshot-/GUI-Basis
- GUI-Datenpufferung

---

# --------------------------------------------------
# 7. PRIORISIERTE REIHENFOLGE
# --------------------------------------------------

# --------------------------------------------------
# PRIO 1
# --------------------------------------------------

- Live-Handoff zwischen Pending, Fill und Position im Bot-Nachweisraum schließen

# --------------------------------------------------
# PRIO 2
# --------------------------------------------------

- Persistenz weiter entkoppeln
- Runtime / Bot-State weiter trennen
- Experience-Bewertungslogik primär auf Zustandswirkung umstellen
- `inner_context_clusters` als Innenmuster- / Innenfeldspeicher ausbauen
- MCM-Feldtopologie / Feldverlauf / Innenfeldspeicher ausbauen

# --------------------------------------------------
# PRIO 3
# --------------------------------------------------

- Review / Cluster-Bewertung nach der Zustandswirkungs-Umstellung nachziehen
- KPI / Auswertung umbauen
- GUI / Visualisierung weiter umbauen
- dedizierte Tests ergänzen

---

# --------------------------------------------------
# 8. AKTUELLER KERNSATZ
# --------------------------------------------------

Offen ist nicht mehr die alte PRIO-1-Basisliste.

Offen sind jetzt:

- ein Restpunkt im Live-/Nachweisraum
- danach der Architektur-Endausbau
- darin ausdrücklich die Umstellung der Experience-Bewertung auf Zustandswirkung
- danach der fachliche Ausbau von Review, KPI und Visualisierung
