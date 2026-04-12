from pathlib import Path

content = """# ==================================================
# AKTUELLER STAND – MCM TRADING BRAIN
# ==================================================

Dieses Dokument beschreibt den aktuellen realen Ist-Zustand des Systems.

Es trennt sauber zwischen:

- bereits real im Code umgesetzt
- fachlich vorbereitet, aber noch nicht vollständig ausgebaut
- nächsten sinnvollen Ausbauschritten

Der Bauplan bleibt in `UMSETZUNGSPLAN.md`.
Dieses Dokument beschreibt nur den realen Stand des letzten Dateistands.

---

# --------------------------------------------------
# 1. Gesamtstatus
# --------------------------------------------------

Das Projekt ist nicht mehr in einer frühen Fix- oder Basisphase.

Die Kernbasis steht bereits im Code:

- äußere Wahrnehmung ist vorhanden
- innere Runtime ist vorhanden
- Entscheidungstendenz ist vorhanden
- Action-Intent- und Execution-State sind vorhanden
- technische Handlungsbahn ist vorhanden
- Episode / Review / Experience sind vorhanden
- Persistenz für Memory- und Runtime-Zustände ist vorhanden
- Visual- und Inner-Snapshots für die GUI sind vorhanden

Die Hauptarbeit liegt damit nicht mehr in der Einführung der Grundmechanik,
sondern im Architektur-Endausbau und in der Experience-Vertiefung.

---

# --------------------------------------------------
# 2. Bereits fix umgesetzt
# --------------------------------------------------

# --------------------------------------------------
# 2.1 Ebene 1 – äußeres Wahrnehmen
# --------------------------------------------------

Ebene 1 ist als eigenständige Wahrnehmungsbasis real vorhanden.

Bereits produktiv vorhanden:

- `candle_state`
- `tension_state`
- `visual_market_state`
- `structure_perception_state`
- `temporal_perception_state`
- `outer_market_state`

Die Wahrnehmung wird aus Marktdaten / `window` aufgebaut
und als neutrales Wahrnehmungspaket weitergegeben.

### Fachliche Bedeutung

Die Außenwelt ist nicht mehr nur einfache Signalquelle,
sondern bereits mehrschichtig beschrieben als:

- Candle-Zustand
- Spannungszustand
- äußere Marktform
- Struktur-Wahrnehmung
- zeitliche Wahrnehmung / Ablaufwahrnehmung

Damit ist Ebene 1 real vorhanden und nicht mehr nur geplant.

---

# --------------------------------------------------
# 2.2 Ebene 2 – inneres Wahrnehmen / Denken / Handeln
# --------------------------------------------------

Ebene 2 ist bereits als laufende innere Runtime-Schicht vorhanden.

Bereits real vorhanden:

- `MCMBrainRuntime`
- Runtime-Snapshot
- Runtime-Decision-State
- Runtime-Brain-Snapshot
- Runtime-Marktimpuls-Verarbeitung
- Runtime-Idle-Followup

Die innere Zustandskette ist angelegt und im Codepfad vertreten:

- `outer_visual_perception_state`
- `inner_field_perception_state`
- `perception_state`
- `processing_state`
- `felt_state`
- `thought_state`
- `meta_regulation_state`
- `expectation_state`

### Entscheidungstendenz

Die Handlung entsteht bereits nicht mehr direkt aus einem simplen Signal.

Vorhanden ist eine vorgelagerte Entscheidungstendenz:

- `act`
- `observe`
- `hold`
- `replan`

### Handlungsbahn vor technischer Ausführung

Zwischen Entscheidung und technischer Order liegen bereits weitere Zustände:

- `action_intent_state`
- `execution_state`

Damit ist Entscheidung bereits stärker von technischer Ausführung getrennt.

### Technische Handlungsbahn

Weiterhin aktiv vorhanden:

- Pending
- Entry
- Position
- Exit

Die technische Mechanik ist damit bereits an die innere Zustandslogik gekoppelt.

---

# --------------------------------------------------
# 2.3 MCM-Zustandsraum
# --------------------------------------------------

Der MCM-Zustandsraum ist bereits explizit lesbar.

Vorhanden sind reale Zustandsachsen wie:

- `field_density`
- `field_stability`
- `regulatory_load`
- `action_capacity`
- `recovery_need`
- `survival_pressure`

Diese Größen laufen bereits durch Runtime-, Decision-, Snapshot- und Experience-Strukturen.

### Fachliche Bedeutung

Die Zielidee,
den Innenraum des Systems explizit lesbar zu machen,
ist real begonnen und produktiv im Code vertreten.

---

# --------------------------------------------------
# 2.4 Ebene 3 – Entwicklung aus Erfahrung
# --------------------------------------------------

Die Entwicklungsebene ist bereits substanziell umgesetzt.

Vorhanden sind:

- `mcm_decision_episode`
- `mcm_decision_episode_internal`
- `mcm_experience_space`
- `outcome_decomposition`
- Review-Logik
- Signature-Memory
- Context-Cluster
- persistenter Memory-State
- In-Trade-Update-Auswertung
- Experience-Linking
- Similarity-/Axis-/Drift-/Reinforcement-Ansätze
- Felt-/Affective-Episode-Auswertung

### Nicht-Handlung ist integriert

Nicht-Handlung ist nicht mehr nur Sonderfall,
sondern realer Teil des Episoden- und Experience-Flusses:

- `observed_only`
- `withheld`
- `replanned`
- `abandoned`

### Zustandsdelta ist integriert

Episode / Experience führen bereits:

- `state_before`
- `state_after`
- `state_delta`

Damit ist die Kopplung von Handlung / Nicht-Handlung und Zustandsveränderung bereits real umgesetzt.

---

# --------------------------------------------------
# 2.5 Persistenz
# --------------------------------------------------

Persistenz ist vorhanden für:

- `signature_memory`
- `context_clusters`
- `mcm_runtime_snapshot`
- `mcm_runtime_decision_state`
- `mcm_runtime_brain_snapshot`
- `mcm_decision_episode`
- `mcm_experience_space`
- weitere Memory-Zustände

Damit kann der Bot relevante Langzeitanteile seines Zustandsraums halten.

---

# --------------------------------------------------
# 2.6 Visualisierung / Snapshots
# --------------------------------------------------

Für die Visualisierung existieren bereits reale Ausgaben aus dem Bot:

- `debug/bot_visual_snapshot.json`
- `debug/bot_inner_snapshot.json`
- `bot_memory/memory_state.json`
- `debug/trade_stats.json`
- `debug/trade_equity.csv`

Damit ist bereits eine hybride Visualisierung vorhanden:

- Außenwelt
- Innenwelt
- Memory / Entwicklung
- klassische Equity-/PnL-Nachweise

Die GUI ist also nicht mehr rein alt,
sondern bereits in einer Übergangsform.

---

# --------------------------------------------------
# 3. Fachlich vorbereitet, aber noch nicht vollständig ausgebaut
# --------------------------------------------------

Die Richtung der nächsten Vertiefung ist fachlich klar.
Dieser Teil ist anschlussfähig,
aber noch nicht vollständig in dieser Tiefe durchgezogen.

# --------------------------------------------------
# 3.1 Tragfähigkeit als zentrale Bewertungsgröße
# --------------------------------------------------

Experience soll nicht primär bewerten:

- Profit
- Trefferquote
- klassische Trade-Kennzahlen

Sondern:

- wie tragfähig eine Situation für das System war
- wie viel innere Reibung sie erzeugt hat
- ob Handlung in dieser Situation effizient tragbar war

Damit verschiebt sich die Experience-Bewertung fachlich von Ergebnisbewertung
zu Tragfähigkeitsbewertung.

---

# --------------------------------------------------
# 3.2 Lernen als Umgangsfähigkeit
# --------------------------------------------------

Das System soll nicht lernen:

- was abstrakt „richtig“ ist
- wie man maximal aggressiv tradet

Sondern:

- womit es gut umgehen kann
- in welchen Situationen es handlungsfähig bleibt
- welche Struktur-Zustands-Kombinationen effizient tragbar sind

Lernen bedeutet damit:

- effizienter mit Situationen umgehen können
- nicht einfach mehr handeln

---

# --------------------------------------------------
# 3.3 Energie / Reibung / Kohärenz
# --------------------------------------------------

Der Nullpunkt der MCM bedeutet fachlich nicht:

- Stillstand
- Inaktivität
- Handlungsunfähigkeit

Sondern:

- hohe Kohärenz mit der Umwelt
- geringe innere Reibung
- geringe energetische Belastung
- hohe Energieeffizienz bei aktiver Interaktion

Abweichung vom Zentrum bedeutet:

- mehr Reibung
- mehr regulatorische Last
- mehr Unsicherheit
- mehr Energieverbrauch

---

# --------------------------------------------------
# 3.4 Erfahrungscluster
# --------------------------------------------------

Experience soll fachlich stärker als Cluster-System gedacht werden.

Cluster repräsentieren nicht nur ähnliche Datenlagen,
sondern:

- Typen von Situationen
- wiederkehrende Struktur-Zustands-Muster
- deren Tragfähigkeit für das System

---

# --------------------------------------------------
# 3.5 Outcome als Zustandswirkung
# --------------------------------------------------

Outcome soll fachlich nicht nur als Geldzahl wirken,
sondern als Veränderung im Innenraum.

Beispiel:

- Gewinn -> Entlastung / Stabilisierung / evtl. Euphorie
- Verlust -> Belastung / Rückzug / Recovery-Bedarf

Wichtig:

- positive Wirkung darf nicht blind verstärken
- Euphorie ist nicht automatisch Stabilität
- Verlust ist nicht nur schlecht, sondern regulatorisches Feedback

---

# --------------------------------------------------
# 4. Was davon technisch bereits vorbereitet ist
# --------------------------------------------------

Für diese Vertiefung gibt es bereits reale technische Anknüpfungspunkte im Code:

- `context_clusters`
- `signature_memory`
- `mcm_experience_space`
- `similarity_axes`
- `drift`
- `reinforcement`
- `attenuation`
- `review_score`
- `structural_bearing_quality`
- `observation_quality`
- `decision_path_quality`
- `state_before / state_after / state_delta`
- Felt-/Episode-Profile
- Proof-/Attempt-Feedback-Metriken

### Einordnung

Das bedeutet:

- die Richtung ist technisch vorbereitet
- die Experience-Vertiefung ist anschlussfähig
- aber die volle fachliche Interpretation als Tragfähigkeits- und Energie-System ist noch nicht komplett ausformuliert bzw. verhärtet

---

# --------------------------------------------------
# 5. Was noch nicht fertig ist
# --------------------------------------------------

# --------------------------------------------------
# 5.1 KPI / Auswertung
# --------------------------------------------------

Der KPI-Bereich ist aktuell in einer Übergangsform.

Noch aktiv vorhanden sind klassische Kennzahlen wie:

- `pnl_netto`
- `pnl_tp`
- `pnl_sl`
- `equity_peak`
- `max_drawdown_abs`
- `max_drawdown_pct`
- `winrate`
- `profit_factor`
- `expectancy`

Gleichzeitig existieren aber bereits neuere Nachweisgrößen wie:

- `attempt_density`
- `context_quality`
- `overtrade_pressure`
- `pressure_to_capacity`
- `regulatory_load`
- `action_capacity`
- `recovery_need`
- `survival_pressure`
- `pressure_release`
- `load_bearing_capacity`
- `state_stability`
- `capacity_reserve`
- `recovery_balance`

Damit ist der Nachweisbereich nicht mehr rein alt,
aber noch nicht vollständig auf Tragfähigkeitsmetriken umgestellt.

---

# --------------------------------------------------
# 5.2 GUI / Visualisierung
# --------------------------------------------------

Die GUI ist bereits weiter als ein reines Equity-/PnL-Fenster.

Bereits angebunden sind:

- Visual-Snapshot
- Inner-Snapshot
- Memory-State
- Stats
- Equity-Historie

Offen ist trotzdem noch:

- die alte KPI-Zentrierung weiter zurückzubauen
- Außenwelt / Innenwelt / Entwicklung noch klarer zu trennen
- Experience- und Tragfähigkeitsverläufe stärker in den Mittelpunkt zu stellen

Die GUI ist damit bereits im Umbau,
aber noch nicht vollständig in der Zielarchitektur angekommen.

---

# --------------------------------------------------
# 5.3 Experience-Vertiefung
# --------------------------------------------------

Die fachliche Vertiefung ist ausgearbeitet,
aber noch nicht vollständig als klare technische Logik durchgezogen.

Noch offen ist insbesondere:

- Tragfähigkeit als explizite Bewertungsgröße
- Lernen als Umgangsfähigkeit
- Reibung / Energie als Experience-Kosten
- Cluster-Bewertung über Tragfähigkeit statt Ergebnis
- stärkere Entkopplung von Profitlogik

---

# --------------------------------------------------
# 5.4 Runtime / Architekturtrennung
# --------------------------------------------------

Weiter zu schärfen ist:

- Ebene 1 = reine Wahrnehmung
- Ebene 2 = reiner Innenprozess
- Ebene 3 = reine Entwicklung / Experience

Ziel:

- weniger Vermischung von Runtime und Bot-State
- klarere strukturelle Trennung der Ebenen

---

# --------------------------------------------------
# 5.5 Tests
# --------------------------------------------------

Dedizierte Tests fehlen weiterhin insbesondere für:

- `bot_gate_funktions.py`
- `mcm_core_engine.py`

---

# --------------------------------------------------
# 6. Nächste Schritte
# --------------------------------------------------

# --------------------------------------------------
# 6.1 Hauptblock
# --------------------------------------------------

Nächster sinnvoller Hauptblock ist:

- Experience fachlich von Ergebnisbewertung auf Tragfähigkeitsbewertung schärfen
- Zustandswirkung von Outcome sauberer formulieren
- Cluster stärker als Erfahrungsräume nutzen
- Lernen explizit als Umgangsfähigkeit modellieren

---

# --------------------------------------------------
# 6.2 Danach
# --------------------------------------------------

Danach sinnvoll:

- Runtime / Architektur weiter trennen
- KPI-Bereich weiter umbauen
- GUI weiter auf Außenwelt / Innenwelt / Entwicklung ausrichten
- dedizierte Tests ergänzen

---

# --------------------------------------------------
# 7. Fazit
# --------------------------------------------------

Der reale Stand des Projekts ist:

- Kernmechanik steht
- Wahrnehmung steht
- Runtime steht
- Handlungsbahn steht
- Experience steht
- Persistenz steht
- Snapshot-/GUI-Basis steht

Der nächste Hauptschritt ist nicht mehr Basis-Fixerei,
sondern:

- Architektur-Endausbau
- Experience-/Tragfähigkeits-Vertiefung
- spätere KPI-/GUI-Neuausrichtung
"""

path = Path("/mnt/data/aktueller_stand_korrigiert.md")
path.write_text(content, encoding="utf-8")
print(f"Wrote {path}")
