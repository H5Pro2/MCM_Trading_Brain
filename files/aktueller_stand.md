# ==================================================
# AKTUELLER STAND – MCM TRADING BRAIN
# ==================================================

Dieses Dokument beschreibt den aktuellen realen Ist-Zustand des Systems.

Es trennt sauber zwischen:

- bereits real im Code umgesetzt
- bereits korrigierten Fehlern
- real noch offenen Ausbaublöcken
- nächsten sinnvollen Schritten

Der Bauplan bleibt in `UMSETZUNGSPLAN.md`.
Dieses Dokument beschreibt nur den realen Stand des aktuellen Dateistands.

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
sondern im Architektur-Endausbau, in der Experience-Vertiefung
und in der weiteren Ausrichtung auf zustandswirkungsbasierte Experience-Bewertung.

---

# --------------------------------------------------
# 2. Bereits real umgesetzt
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
- formale `inner_context_clusters`-Anbindung
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

### Innenkontextcluster und Pattern-Verdichtung sind begonnen

`inner_context_clusters` sind im aktuellen Code nicht mehr nur Zielidee,
sondern bereits in `Bot`, Experience-Aktualisierung und Memory-State verankert.

Zusätzlich sind im aktuellen Stand Pattern-Werte vorhanden:

- `inner_pattern_support`
- `inner_pattern_conflict`
- `inner_pattern_fragility`
- `inner_pattern_bearing`
- `pattern_reinforcement`
- `pattern_attenuation`
- `pattern_action_support`
- `pattern_observe_pressure`
- `pattern_replan_pressure`

Neu ergänzt ist eine erste aktive Kontextspur:

- `active_context_trace`
- `activation`
- Decay pro Runtime-Tick
- Reaktivierung aus `inner_context_clusters`
- schwache Rückwirkung auf Pattern-Modulation
- schwache Rückwirkung auf Replay-/Feldimpuls

Noch nicht erreicht ist die tiefe lokale Rückstreuung bis in `MCMNeuron.memory_trace`.

---

# --------------------------------------------------
# 2.5 Persistenz
# --------------------------------------------------

Persistenz ist vorhanden für:

- `signature_memory`
- `context_clusters`
- `inner_context_clusters`
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
# 3. Bereits korrigierte Fehler aus dem früheren Fixblock
# --------------------------------------------------

# --------------------------------------------------
# 3.1 state_delta ist korrigiert
# --------------------------------------------------

Bereits umgesetzt:

- ereignislokale Bildung von `state_before`, `state_after`, `state_delta`
- gemeinsamer Übergang für Stats-Kontext und Episode-Payload
- Snapshot-Commit erst nach dem jeweiligen Event
- alte Null-/Doppelsnapshot-Pfade im Entry-/Pending-/Nicht-Handlungs-Pfad bereinigt

Folge:

- Episode / Experience arbeiten an diesen Stellen wieder auf realen Zustandsübergängen

---

# --------------------------------------------------
# 3.2 Statistik-Semantik ist korrigiert
# --------------------------------------------------

Bereits umgesetzt:

- `pnl_netto` startet als reiner Nettowert bei `0.0`
- `current_equity` wird getrennt als `start_equity + pnl_netto` geführt
- `expectancy` baut damit auf realem Nettowert statt auf Equity-Basis auf

Folge:

- Nettoergebnis und Erwartungswert sind semantisch wieder sauber getrennt

---

# --------------------------------------------------
# 3.3 Exit-Strukturdiagnose ist korrigiert
# --------------------------------------------------

Bereits umgesetzt:

- Exit-/Cancel-Pfade nutzen aktuellen Exit-Kontext statt alten Entry-Kontext
- aktuelle `structure_perception_state` läuft bis in `on_exit()` / `on_cancel()`
- `outcome_records` tragen reale Exit-Strukturqualität
- `structure_bands` werden daraus sauber neu aufgebaut

Folge:

- Exit-KPI über Strukturqualität ist im aktuellen Backtest-/Bot-Pfad fachlich belastbar

---

# --------------------------------------------------
# 3.4 attempt_feedback / proof-Felder sind korrigiert
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
# 4. Reale offene Punkte im aktuellen Stand
# --------------------------------------------------

# --------------------------------------------------
# 4.0 MCMField-Speicherfehler im lokalen Nachbarschaftsaufbau ist korrigiert
# --------------------------------------------------

Real vorhanden:

- `MCM_KI_Modell.py` führt den Feldzustand weiterhin als mehrdimensionales `N x D`
- `_build_local_neighbor_state_map()` berechnet Nachbarschaften zeilenweise pro Neuron
- der alte permanente `N x N x D`-Deltablock ist im lokalen Nachbarschaftsaufbau entfernt
- weitergegeben werden nur lokale Nachbarn, nicht das gesamte Feld als globaler Neuroneneinfluss

Fachliche Bedeutung:

- alle Neuronen können denselben Umweltreiz wahrnehmen
- informationsbildend ist aber ihre lokale Eigenreaktion
- lokale Nachbarschaft, Kopplung, Kohärenz und Resonanz können Informationsinseln bilden
- Cluster sollen dadurch nicht aus globalem Gleichschalten entstehen, sondern aus lokaler Feldorganisation

Weiter zu beobachten:

- `_build_areal_state()` arbeitet noch mit `N x N`-Distanzen
- das ist kein `N x N x D`-Deltablock, bleibt aber bei hoher Agentenzahl ein Optimierungspunkt
- Arealbildung soll dauerhaft lokal begrenzt bleiben und keine globale Speicherexplosion erzeugen

---

# --------------------------------------------------
# 4.1 Live-Handoff zwischen Pending, Fill und Position ist noch nicht vollständig geschlossen
# --------------------------------------------------

Real offen:

- `_handle_pending_entry()` schreibt im Live-Pfad `pending_update`, kehrt danach aber direkt zurück
- der Bot-seitige `filled`-Übergang mit `stats.on_attempt(status="filled")`, Episode-Event und `self.position`-Aufbau existiert aktuell nur im Nicht-Live-/Backtest-Pfad
- der Exchange-Sync erkennt offene Positionen failsafe-seitig, aber dieser Zustand wird noch nicht als vollständiger Bot-/Episode-/Stats-Handoff geführt

Folge:

- Backtest- und Live-Nachweisraum sind im Übergang `pending -> filled -> position` noch nicht gleichwertig
- ein Teil des realen Live-Handlungsverlaufs bleibt im Bot-internen Nachweisraum strukturell unvollständig

---

# --------------------------------------------------
# 4.2 Innenkontextcluster sind formal und als Pattern-Verdichtung begonnen, aber noch nicht aktiv genug
# --------------------------------------------------

Real vorhanden:

- `inner_context_clusters` sind bereits real in `Bot`, Experience-Aktualisierung und Persistenz verankert
- die Trennung von `context_clusters` und `inner_context_clusters` ist fachlich begonnen
- Pattern-Verdichtung ist real begonnen über Support, Conflict, Fragility, Bearing, Reinforcement und Attenuation
- Pattern-Werte wirken bereits in Review-Feedback, Runtime-Meta-Regulation und Entscheidungstendenz hinein

Neu real vorhanden:

- `active_context_trace` ist als Runtime-Zustand eingeführt
- aktive Kontextspur wird aus `inner_context_clusters` reaktiviert
- `activation` klingt pro Runtime-Tick ab
- Pattern-Werte werden schwach über aktive Kontextspur moduliert
- Runtime-Snapshot führt `active_context_trace` mit

Real offen:

- lokale Rückführung in `MCMNeuron.memory_trace` ist noch nicht umgesetzt
- Nachhall ist aktuell Runtime-/Pattern-/Replay-Modulation, noch keine tiefe lokale Feldplastizität
- Replay-Rückwirkung ist bewusst schwach begrenzt und noch kein lokaler Erfahrungsumbau

Fachlich ergänzt:

- Informationscluster sollen nicht durch Felddruck gelöscht werden
- Felddruck verändert Priorität, Aktivierung und Zugänglichkeit von Information
- nicht getragene Information verliert aktive Bindungsstärke und geht in Nachhall oder Latenz über
- dadurch wird lokaler Organisationsraum frei, ohne gespeicherte Erfahrung zu vernichten
- Reorganisation bedeutet Informationsumschichtung, nicht Blackout
- Kohärenzstärke beschreibt, wie verdichtet und tragfähig ein Cluster aktuell getragen wird
- diese Kohärenzstärke soll später farblich in der GUI sichtbar werden

Ziel:

- `context_clusters` als äußerer / gesamt-situativer Signaturraum klar halten
- `inner_context_clusters` als wiederkehrenden Innenmusterraum weiter ausbauen
- aktive Kontextspur im Replay-/Feldimpuls weiter kontrolliert beobachten und begrenzen
- Vermeidungs-, Entlastungs-, Reorganisations- und Tragfähigkeitslernen sauber auf Innenmuster legen
- Clusterzustände als aktiv getragen, nachhallend, latent oder frei werdend unterscheidbar machen

---

# --------------------------------------------------
# 4.3 Experience-Bewertungslogik ist noch nicht weit genug auf Zustandswirkung umgestellt
# --------------------------------------------------

Real offen:

- `_experience_reward_delta()` verzweigt weiterhin direkt über `tp_hit`, `sl_hit`, `cancel`, `timeout` und ähnliche Outcome-Wege
- Experience verarbeitet zwar bereits Zustandsfelder wie Tragfähigkeit, Regulationskosten, Entlastung und Handlungsspielraum, aber das formale Ergebnis dominiert fachlich noch zu stark
- Outcome ist damit reduziert, aber noch nicht weit genug aus Experience gelöst
- lokale Rückführung auf `inner_context_clusters`, Feldmuster und neuronale Teilträger wäre auf dieser Grundlage noch zu stark von Ergebnisetiketten geprägt

Folge:

- Experience ist fachlich schon deutlich besser als früher
- aber noch nicht konsequent genug auf Zustandswirkung, Tragfähigkeit und Umgangsfähigkeit ausgerichtet

Ziel:

- Experience bewertet primär `state_before`, `state_after`, `state_delta` und Tragfähigkeitswirkung
- `tp_hit`, `sl_hit`, `cancel`, `timeout` bleiben nur Ereigniskontext
- Lernen entsteht stärker aus Belastung, Entlastung, Stabilisierung, Fragilisierung und Handlungsfähigkeit
- lokale Rückführung wird erst auf dieser Grundlage fachlich sinnvoll

---

# --------------------------------------------------
# 4.4 MCM-Feldtopologie / Feldverlauf / Innenfeldspeicher sind noch nicht ausgebaut
# --------------------------------------------------

Offen:

- das MCM-Feld erkennt bereits laufende Feldcluster, reduziert diese aktuell aber zu stark auf kompakte Feldwerte und verdichtete Memory-Formen
- die Gesamtorganisation des Agentenfeldes ist noch nicht als eigene Feldwahrnehmung formalisiert
- Feldtopologie, Clusterbeziehungen, Driftverlauf, Fragmentierung, Verschmelzung und Rückführungsbewegung werden noch nicht als eigener Innenkontext sauber mitgeführt
- ein eigener persistenter Speicher für wiederkehrende Feldformen, Driftmuster und Regulationsverläufe fehlt aktuell
- die Visualisierung bildet das MCM-Feld bislang noch nicht als räumlich-dynamischen Innenraum ab

Ziel:

- Feldcluster nicht nur erkennen, sondern in ihrer Größe, Dichte, Stabilität, Verschiebung und Beziehung zueinander lesbar machen
- die Gesamtform des MCM-Feldes als Feldtopologie beschreiben
- Feldverlauf über Zeit mitführen
- einen verdichteten Innenfeldspeicher für wiederkehrende Clusterkonfigurationen, Feldformen, Driftmuster und Rückführungsbewegungen aufbauen

---

# --------------------------------------------------
# 4.5 Runtime / Bot-State sind noch nicht weit genug getrennt
# --------------------------------------------------

Offen:

- `Bot` bündelt weiter Außenwahrnehmung, Runtime, Handlungsbahn, Experience, Persistenz und Snapshot-Orchestrierung
- die Zieltrennung Ebene 1 / Ebene 2 / Ebene 3 ist damit noch nicht strukturell verhärtet

Ziel:

- weniger Vermischung von Runtime und Bot-State
- klarere Trennung von Wahrnehmung / Innenprozess / Entwicklung

---

# --------------------------------------------------
# 4.6 Persistenz ist entschärft, aber noch nicht ausreichend entkoppelt
# --------------------------------------------------

Offen:

- Persistenz ist bereits über Dirty-Flag und Cooldown teilweise entschärft
- Save-/Flush-Pfade liegen aber weiter nah am Kernlauf

Folge:

- Bot-Kern bleibt unnötig eng mit Save-/Flush-Logik gekoppelt

---

# --------------------------------------------------
# 5. Fachlich vorbereitet, aber noch nicht vollständig ausgebaut
# --------------------------------------------------

# --------------------------------------------------
# 5.1 Tragfähigkeit ist stärker verankert, aber noch nicht Endzustand
# --------------------------------------------------

Experience bewertet bereits stärker:

- Tragfähigkeit
- Regulationskosten
- Entlastung
- Handlungsspielraum

Noch nicht vollständig ausgebaut ist:

- die weitere Entkopplung von Ergebnislogik und Experience-Logik
- die noch konsequentere Ausrichtung auf Zustandswirkung statt Geldwirkung
- die formale Umstellung der Experience-Bewertungslogik von Outcome-Verzweigungen auf Zustandswirkung

---

# --------------------------------------------------
# 5.2 Lernen als Umgangsfähigkeit ist begonnen, aber noch nicht konsequent genug
# --------------------------------------------------

Das System lernt bereits erkennbar stärker:

- womit es umgehen kann
- in welchen Situationen es handlungsfähig bleibt
- wie Tragfähigkeit und Belastung zusammenhängen

Noch offen ist:

- Lernen als Umgangsfähigkeit technisch konsequenter durchzuziehen
- Cluster-Bewertung noch stärker auf Tragfähigkeit statt Ergebnis auszurichten

---

# --------------------------------------------------
# 5.3 Lokale Rückführung ist vorbereitet, aber fachlich noch nicht reif genug
# --------------------------------------------------

Vorbereitet ist bereits:

- Experience-Linking
- `inner_context_clusters`
- Similarity-/Drift-/Reinforcement-Mechanik
- Zustandsachsen für Tragfähigkeit, Belastung, Entlastung und Handlungsfähigkeit

Noch offen ist:

- lokale Erfahrungsrückwirkung erst nach sauberer Umstellung auf Zustandswirkung zu vertiefen
- lokale Hemmung, Gewöhnung und Rückführungsneigung nicht zu früh an Outcome-Etiketten zu koppeln
- neuronale Teilträger und Feldmuster erst dann tiefer zu modulieren, wenn Experience fachlich sauber genug entkoppelt ist

---


# --------------------------------------------------
# 6. Nächste sinnvolle Schritte
# --------------------------------------------------

Die sinnvollste Reihenfolge ab jetzt ist:

1. Live-Handoff `pending -> filled -> position` im Bot-/Episode-/Stats-Raum schließen
2. Persistenz weiter entkoppeln und Runtime / Bot-State weiter trennen
3. `active_context_trace` Richtung Replay-/Feldimpuls prüfen
4. Experience-Bewertungslogik primär auf Zustandswirkung und Nachhall-Wirkung umstellen
5. MCM-Feldtopologie / Feldverlauf / Innenfeldspeicher weiter ausbauen
6. erst danach lokale Erfahrungsrückwirkung tiefer an Innenmuster und neuronale Teilträger legen

---


# --------------------------------------------------
# 7. Kurzfazit
# --------------------------------------------------

Der Bot steht nicht mehr am Anfang.

Die Basismechanik,
