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
- schwache lokale Rückstreuung bis in `MCMNeuron.memory_trace`
- `context_memory_impulse` als lokale Kontext-Memory-Kennzahl
- `field_neuron_context_memory_impulse_norm_mean` läuft in `inner_context_clusters`, `current_vector`, Experience-Link-Achsen und bleibt persistierbar
- innere Musterbeschriftung kann `memory_reactivated_neurons` ausweisen
- Experience-Similarity führt `context_memory_impulse_axis`, `active_context_activation_axis`, `active_context_balance_axis` und `context_memory_reactivation_axis`

Eine erste schwache lokale Rückstreuung bis in `MCMNeuron.memory_trace` ist angebunden; die tiefe lokale Erfahrungsareal-Bildung ist noch offen.

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

- `_build_areal_state()` baut Areale jetzt ohne dauerhafte vollständige `N x N`-Distanzmatrix auf
- `_build_areal_components()` berechnet Distanzen zeilenweise pro Neuron
- interne Areal-Dichte wird pro Komponente zeilenweise berechnet
- kein permanenter `N x N x D`-Deltablock und keine dauerhafte globale Distanzmatrix im Arealaufbau

---

# --------------------------------------------------
# 4.1 Live-Handoff zwischen Pending, Fill und Position ist bot-seitig nachgezogen
# --------------------------------------------------

Teilweise korrigiert:

- `_handle_pending_entry()` kann `source="position_context"` in den gemeinsamen Fill-Handoff überführen
- `_finalize_pending_fill_handoff()` führt Live- und Backtest-Fill über denselben Bot-internen Pfad
- `get_active_order_snapshot()` erzwingt vor der Snapshot-Auswertung einmalig einen synchronen Bootstrap-/Exchange-Sync
- `get_active_order_snapshot()` liest offene Order-TP/SL jetzt aus `takeProfitPrice/stopLossPrice` und `takeProfitRp/stopLossRp`
- `get_active_order_snapshot()` bleibt bei offener Order auch ohne Exchange-`timestamp` verwertbar
- `place_order()` übernimmt identische offene Orders jetzt inklusive `_ACTIVE_TP`, `_ACTIVE_SIDE` und Entry-/Risk-Kontext
- `_sync_with_exchange()` übernimmt eindeutig offene Orders jetzt inklusive `_ACTIVE_TP`, `_ACTIVE_SIDE` und Entry-/Risk-Kontext
- `_sync_with_exchange()` ergänzt bei bereits bestätigter aktiver Order fehlenden `_ACTIVE_TP`, `_ACTIVE_SIDE` und Entry-/Risk-Kontext aus `open_orders`
- `get_active_order_snapshot()` synchronisiert bei verschwundener aktiver Order aktiv nach
- erkannte Live-Positionen können dadurch als Positionskontext an den Bot zurückgegeben werden
- Live-Fill schreibt den `live_handoff`-Kontext inklusive `pending_order_id`, `snapshot_id`, Entry/TP/SL, `entry_ts` und `handoff_reason` in `position_meta`
- Restart-Recovery schreibt `recovery_source` und `recovery_snapshot` in `meta`
- aktive Restart-Positionen erhalten einen verwertbaren `entry_ts` / `last_checked_ts`
- Restart-Recovery setzt `execution_state` auf `pending_recovered` oder `position_recovered`
- Restart-Recovery schreibt ein technisches Episode-Event über `pending_update` oder `position_update`
- Restart-Recovery markiert Memory-State als dirty und committet den Regulationssnapshot
- Restart-Recovery speichert den wiederhergestellten Zustand sofort per Forced-Save

Weiter zu prüfen:

- echter Live-Test `pending -> filled -> position` gegen Exchange-Zustand
- Restart-Fall mit bereits gefüllter Order gegen echten Exchange-Zustand validieren
- ob TP/SL/Entry-Kontext nach Restart im echten Exchange-Fall vollständig belastbar bleibt

Folge:

- Backtest- und Live-Handoff nutzen bot-seitig denselben Fill-Abschluss, müssen aber real-live-validiert werden

---

# --------------------------------------------------
# 4.2 Innenkontextcluster sind angebunden und als Pattern-Verdichtung begonnen
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
- aktive Kontextspur wird schwach und lokal dosiert bis in `MCMNeuron.memory_trace` zurückgeführt
- `context_memory_impulse` ist im Inner-Snapshot und in der Neuron-GUI als eigene lokale Kontext-Memory-Kennzahl sichtbar
- `field_neuron_context_memory_impulse_norm_mean` läuft in `inner_context_clusters` und bleibt über `memory_state` persistierbar
- `context_memory_impulse` wird in der inneren Musterbeschriftung als `memory_reactivated_neurons` sichtbar, wenn lokale Kontextreaktivierung dominiert

Real offen:

- wiederkehrende Feldformen sind noch nicht als echte lokale Erfahrungsareale im Neuronenfeld verankert
- Nachhall ist jetzt erste lokale Memory-Trace-Modulation, aber noch keine tiefe lokale Feldplastizität
- Replay-Rückwirkung bleibt bewusst schwach begrenzt und ist noch kein vollständiger lokaler Erfahrungsumbau

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

Teilweise umgesetzt:

- `field_cluster_links` und `field_areal_links` werden zu `field_topology_state` verdichtet
- `field_topology_state` führt Link-Anzahl, Link-Dichte, mittlere Distanz, Topologie-Kohärenz, Topologie-Spannung und Topologie-Label
- Feldtopologie läuft jetzt in `inner_field_perception_state`, `inner_context_clusters`, `current_vector`, Experience-Summary und `memory_state`
- `field_topology_state` ist in der Neuron-GUI als Topologie-Zustand, Linkverhältnis, Link-Dichte, Kohärenz und Spannung sichtbar

Offen:

- ein eigener persistenter Speicher für wiederkehrende Feldformen, Driftmuster und Regulationsverläufe fehlt aktuell
- Feldverlauf über mehrere Ticks ist noch nicht als eigener Innenfeldpfad gespeichert
- die Visualisierung zeigt Feldformen, führt aber noch keinen persistenten Feldformverlauf

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

1. Live-Handoff real testen: `pending -> filled -> position` gegen Exchange-Zustand validieren
2. Restart-Fall real testen: offene Order / gefüllte Position nach Bot-Neustart prüfen
3. `_experience_reward_delta()` real im Backtest/Live prüfen: Zustandswirkung gegen Outcome-Etiketten kontrollieren
4. aktive Kontextspur / Nachhall-Wirkung in Experience und Clusterbewertung weiter beobachten
5. MCM-Feldtopologie / Feldverlauf / Innenfeldspeicher weiter ausbauen
6. danach lokale Erfahrungsrückwirkung tiefer an Innenmuster, Feldformen und neuronale Teilträger koppeln
7. Persistenz und Runtime-/Bot-State weiter entkoppeln, wenn die Erfahrungslogik stabiler ist

---


# --------------------------------------------------
# 7. Kurzfazit
# --------------------------------------------------

Der Bot steht nicht mehr am Anfang.

Die Basismechanik steht:

- äußere Wahrnehmung
- innere Runtime
- Entscheidungstendenz
- technische Handlungsbahn
- Episode / Review / Experience
- Persistenz
- Snapshot / GUI

Der aktuelle offene Kern ist nicht mehr der Grundaufbau, sondern:

- Real-Live-Validierung des Live-Handoffs
- Experience-Bewertung stärker auf Zustandswirkung statt Ergebnisetiketten ausrichten
- Feldtopologie und Innenfeldspeicher weiter vertiefen
- lokale Erfahrungsrückwirkung erst danach tiefer an Neuronen und Feldformen koppeln

Der MCM-Umbau hat damit die erste echte Schwelle erreicht:

`inner_context_clusters -> active_context_trace -> MCMField -> MCMNeuron.memory_trace`

ist schwach angebunden und sichtbar.

Die nächste Schwelle ist die fachlich saubere Umstellung von Experience auf Zustandswirkung.
