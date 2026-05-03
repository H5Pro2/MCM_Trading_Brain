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

Aktuelle Arbeitspriorität:

- zuerst neuronale Aktivität und kognitive Innenfunktion fertigstellen
- danach das MCM-Feld als Wahrnehmungsfeld sauber ausbauen
- Fokus auf `MCMNeuron`, lokale Aktivierung, Kopplung, Nachhall, Kontext-Memory, `MCMField`, Innenmuster und Experience
- Backtest-Logik bleibt sauberer Ausführungs- und Kontrollpfad, aber Testdateien sind nicht die aktuelle Hauptarbeit
- Live-Exchange / echter Live-Handoff erst am Schluss validieren
- GUI-Ausbau vorerst nachrangig behandeln
- Testausbau vorerst nachrangig behandeln

Damit ist der aktuelle Schwerpunkt nicht Live-Betrieb und nicht Oberfläche,
sondern die fachlich saubere Umsetzung des inneren Gehirns:
erst neuronale Aktivität, dann das Mental-Core-Matrix-Feld als Wahrnehmungsraum.

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
- `neural_felt_state` ist als lesende neuronale Felt-Schicht begonnen
- `neural_felt_bearing`, `neural_felt_pressure`, `neural_felt_memory_resonance`, `neural_felt_context_reactivation` und `neural_felt_label` laufen in `inner_context_clusters`, `current_vector`, `felt_state` und `memory_state`
- `neural_felt_*` läuft zusätzlich in Experience-Summary, Episode-Felt-Summary, Similarity-Achsen, Runtime-Snapshot, Decision-State, Brain-Snapshot und `active_context_trace`
- `active_context_trace` trägt `neural_felt_*` als Lesefeld; Replay-/Feldimpuls und Pattern-Verstärkung wurden dadurch nicht erhöht
- `inner_field_history` ist als lesender Feldverlauf über mehrere Ticks angebunden und über `memory_state` persistierbar
- `inner_field_history_*` läuft in `inner_context_clusters`, `current_vector`, Experience-Summary, Runtime-/Brain-Snapshot, `active_context_trace` und `episode_internal["signal"]`
- `active_context_trace` trägt `inner_field_history_*` nur als Lesefeld; Replay-/Feldimpuls und Pattern-Verstärkung wurden dadurch nicht erhöht
- feste Feldtopologie ist begonnen: `MCMField` führt feste `field_position` und `topology_neighbors` je `MCMNeuron`
- neuronale Aktivität ist geschärft: `MCMNeuron` bildet jetzt lokale `receptivity`, `overload`, `recovery_tendency`, `memory_resonance`, `context_reactivation`, `coupling_resonance`, `activity_label` und `activation_components`
- Reizaufnahme wird pro Neuron lokal moduliert, sodass derselbe Außenreiz nicht mehr nur global gleichförmig wirkt
- `activation` ist jetzt eine zusammengesetzte Lesung aus Außenreiz, Replay, Kontext-Memory, Kopplung, Memory-Feedback, Velocity und lokaler Resonanz
- `MCMField` ist als Wahrnehmungsfeld geschärft: neuronale Aktivität breitet sich schwach über feste Topologie-Nachbarn aus
- `field_perception_state` erkennt lokale Aktivitätsinseln mit Masse, Aktivierung, Druck, Kohärenz, Kontextreaktivierung, Spread und Label
- `field_perception_state` bewertet Aktivitätsinseln jetzt zusätzlich als Wahrnehmungsqualität: `field_perception_focus`, `field_perception_clarity`, `field_perception_stability`, `field_perception_fragmentation`, `field_perception_strain` und `dominant_activity_island_id`
- Feldlabels wie `active_perception_field`, `coherent_perception_field`, `fragmented_perception_field`, `memory_reactivated_field` und `strained_field` sind als Leseschicht vorhanden
- `field_topology_layout_state` läuft in `inner_field_perception_state`, `inner_context_clusters`, `current_vector`, `active_context_trace` und Experience-Similarity-Achsen
- neue neuronale Aktivitätswerte und `field_perception_state` laufen in Neuron-Snapshots, Arealzustände, `inner_field_perception_state` und `neural_felt_state`
- Aktivitätsinseln und `field_perception_label` laufen jetzt in `inner_pattern_identity`, `field_pattern_signature`, `field_pattern_vector`, `inner_context_clusters`, `memory_state` und `mcm_experience_space`
- die Innenmuster-Identität unterscheidet dadurch nicht mehr nur globale Feld-/Arealwerte, sondern auch wahrgenommene lokale Aktivitätsinseln im MCM-Feld
- `processing_state` bildet aus Feldinseln jetzt `field_perception_pressure`, `field_perception_support`, `field_perception_clarity`, Fokus, Stabilität, Fragmentierung und Strain
- `felt_state` nutzt die geschärfte Feldwahrnehmung für Risiko, Gelegenheit, inneren Konflikt, Druck, Stabilität, Alignment und dominante Spannung
- `thought_state` nutzt Fokus/Stabilität/Fragmentierung/Strain für Denk-/Areal-Druck, Unterstützung, Reife, Grübeltiefe, Entscheidungsdruck, Entscheidungsbereitschaft und Thought-Alignment
- `meta_regulation_state` nutzt die geschärfte Feldwahrnehmung jetzt für `field_perception_instability`, `field_observation_need`, `field_replan_pressure` und `field_action_support`
- fragmentierte/angespannte MCM-Felder können dadurch auch bei starkem Signal gezielt `observe` oder `replan` auslösen; klare/stabile Felder können kontrolliertes `act` stützen
- Architekturentscheid übernommen: Experience soll nicht `TP gut / SL schlecht` lernen, sondern eine neurochemisch gedämpfte Wirkung aus Profitabilität, Entlastung, Stabilität, Disziplin, Tragfähigkeit, Varianz und Überlast bilden
- Profitabilität bleibt notwendige innere Zielspannung, wird aber durch Regelqualität, Tragfähigkeit, Stabilität und Varianz gedämpft; chaotischer Gewinn darf nicht blind stärken, sauberer Verlust nicht blind schwächen
- `build_experience_neurochemical_effect()` ist im Brain angebunden und liefert getrennte Wirkachsen: `profit_reward`, `relief_signal`, `stability_signal`, `discipline_signal`, `confidence_signal`, `overactivation_signal`, `chaos_penalty`, `variance_penalty`, `overstrain_penalty`, `carrying_capacity_delta`, `self_confidence_delta` und `process_quality`
- `_experience_reward_delta()` ist jetzt nur noch ein Kompatibilitäts-Wrapper auf `experience_effect_score`; die eigentliche Erfahrungsmechanik liegt in der neurochemisch gedämpften Wirkfunktion
- `experience_neurochemical_effect` und die flachen Wirkachsen laufen in Experience-Summary, Episode-History, Experience-Space und als gleitende Link-Profile (`avg_*` / `last_*`) in die Musterlinks
- SL-Episoden werden nicht automatisch schlecht bewertet, aber nach oben gedeckelt; sauberer Verlust kann Prozessstabilität bestätigen, erzeugt aber kein euphorisches Gewinnsignal
- Experience-Similarity führt jetzt zusätzliche neurochemische Achsen für Profit, Entlastung, Stabilität, Disziplin, Confidence, Überaktivierung, Chaos, Varianz, Überlast, Tragfähigkeit und Selbstvertrauen
- `inner_context_clusters` speichern jetzt `experience_neurochemical_profile`, `neurochemical_support`, `neurochemical_strain` und gleitende neurochemische `avg_*` / `last_*` Werte
- `pattern_reinforcement`, `pattern_attenuation` und `trust` werden schwach durch neurochemische Tragfähigkeit oder Belastung moduliert; die Feld-/Musterwerte bleiben weiterhin dominierend
- `active_context_trace` trägt die neurochemischen Achsen als Nachhall und nutzt sie schwach für `activation`, `action_support`, `observe_pressure`, `replan_pressure` und Replay-Impuls
- tragfähige Muster bekommen dadurch etwas mehr stabile Wiedererreichbarkeit; chaotische/überaktive Muster erzeugen eher Dämpfung, Beobachtungsdruck und weniger Replay-Nachhall
- `memory_state.py` persistiert die neuen neurochemischen Clusterprofile
- `active_context_trace` trägt `field_topology_layout_state` nur als Lesefeld; Replay-/Feldimpuls und Pattern-Verstärkung wurden dadurch nicht erhöht
- `field_areal_topology_*` läuft in `inner_context_clusters`, `current_vector`, `active_context_trace`, `episode_internal["signal"]` und Experience-Similarity-Achsen
- `field_areal_topology_*` bleibt Lesewert und verändert Replay-/Feldimpuls oder Pattern-Verstärkung nicht
- `inner_pattern_identity` ist als erste Innenmuster-Identität begonnen und läuft in `inner_context_clusters`, `current_vector`, Cluster-Rückgabe, `memory_state` und `active_context_trace`
- `active_context_trace` trägt `field_pattern_signature_key`, `inner_pattern_identity`, `inner_pattern_identity_label` und `inner_pattern_identity_confidence` nur als Lesefelder
- `inner_pattern_identity_stability` ist als Lesewert ergänzt und läuft in Cluster-Rückgabe, `active_context_trace`, `mcm_runtime_brain_snapshot["signal"]`, `episode_internal["signal"]`, `mcm_experience_space` und `memory_state`
- `inner_pattern_identity_streak`, `inner_pattern_identity_recurrent`, `inner_pattern_identity_changed` und `inner_pattern_identity_last_seen_tick` bleiben reine Wiedererkennungs-/Stabilitätswerte ohne stärkere Replay-/Feldimpuls-Gewichtung
- Runtime-Profiling ist als Debug-Schicht angebunden und schreibt nach `debug/mcm_profile.csv`
- Profiling misst `step_mcm_brain`, `field.step`, `cluster.detect`, Runtime-/Visual-Snapshot-Schreiben und `memory_state` Build/Write

Eine erste schwache lokale Rückstreuung bis in `MCMNeuron.memory_trace` ist angebunden; die tiefe lokale Erfahrungsareal-Bildung ist noch offen.
`neural_felt_state` bleibt eine lesende Innenwahrnehmung und ist keine neue Handelsregel.

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
# 4.0 MCMField-Speicherfehler korrigiert / Zieltopologie geschärft
# --------------------------------------------------

Real vorhanden:

- `MCM_KI_Modell.py` führt den Feldzustand weiterhin als mehrdimensionales `N x D`
- `_build_local_neighbor_state_map()` berechnet Nachbarschaften zeilenweise pro Neuron
- der alte permanente `N x N x D`-Deltablock ist im lokalen Nachbarschaftsaufbau entfernt
- weitergegeben werden nur lokale Nachbarn, nicht das gesamte Feld als globaler Neuroneneinfluss
- `velocity` beschreibt Zustandsnachlauf / Trägheit / Richtung der Zustandsveränderung, keine physische Neuronenbewegung

Fachliche Bedeutung:

- alle Neuronen können denselben Umweltreiz wahrnehmen
- informationsbildend ist aber ihre lokale Eigenreaktion
- lokale Nachbarschaft, Kopplung, Kohärenz und Resonanz können Informationsinseln bilden
- Cluster sollen dadurch nicht aus globalem Gleichschalten entstehen, sondern aus lokaler Feldorganisation
- die Zielrichtung wird auf feste Feldknoten / neuronales Gewebe geschärft
- nicht der Knoten bewegt sich, sondern Zustand, Aktivierung, Nachhall und Informationswirkung breiten sich im Feld aus
- höhere Neuronenzahl bedeutet höhere Auflösung der inneren Zustandswahrnehmung, nicht automatisch höhere Intelligenz

Weiter zu beobachten:

- `_build_areal_state()` baut Areale jetzt ohne dauerhafte vollständige `N x N`-Distanzmatrix auf
- `_build_areal_components()` berechnet Distanzen zeilenweise pro Neuron
- interne Areal-Dichte wird pro Komponente zeilenweise berechnet
- kein permanenter `N x N x D`-Deltablock und keine dauerhafte globale Distanzmatrix im Arealaufbau

Aktueller Architekturabgleich:

- `MCMField` ist kompatibel auf feste Feldtopologie begonnen
- jedes `MCMNeuron` trägt `field_position` und `topology_neighbors`
- `energy` und `velocity` bleiben nach außen kompatibel als `N x D`-Sicht erhalten
- lokale Kopplung nutzt feste Topologie-Nachbarschaften statt dynamischer globaler Zustandsabstandssuche
- GUI-Lesart bleibt bewusst offen bis die Feldtopologie fachlich fertig steht

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
- `context_memory_impulse` ist im Inner-Snapshot als eigene lokale Kontext-Memory-Kennzahl vorhanden; die Neuron-GUI-Datei ist im aktuellen Upload nicht enthalten und daher nicht geprüft
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
# 4.3 Experience-Bewertungslogik ist auf neurochemische Zustandswirkung umgestellt
# --------------------------------------------------

Umgesetzt:

- `build_experience_neurochemical_effect()` bildet den eigentlichen Erfahrungswert aus Prozessqualität, Profitspannung, Entlastung, Stabilität, Disziplin, Confidence, Tragfähigkeit, Varianz, Chaos, Überlast und Überaktivierung
- `_experience_reward_delta()` verzweigt nicht mehr selbst über Outcome-Wege, sondern liest nur noch `experience_effect_score` aus der neurochemischen Wirkfunktion
- `tp_hit`, `sl_hit`, `cancel`, `timeout` bleiben Ereigniskontext, aber nicht mehr der Bewertungsanker
- SL-Episoden sind nach oben gedeckelt: sauberer Verlust kann Regelwerk und Tragfähigkeit bestätigen, aber kein starkes Belohnungssignal erzeugen
- chaotische TP-Episoden werden durch Chaos, Varianz und Überaktivierung gedämpft
- die Wirkachsen laufen in Experience-Summary, Episode-History, Experience-Space, Link-Buckets und Similarity-Achsen

Offen:

- die neue neurochemische Wirkung ist noch nicht stark in lokale Neuronen-/Feldverstärkung zurückgeführt
- die nächsten Schritte müssen beobachten, ob `avg_*` / `last_*` Profile in den Link-Buckets stabile Musterbindung oder sinnvolle Dämpfung erzeugen

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
- Feldtopologie läuft jetzt in `inner_field_perception_state`, `inner_context_clusters`, `current_vector`, Experience-Summary, Experience-Space, Experience-Link-Buckets und `memory_state`
- `field_topology_state` steht für die Neuron-GUI als Topologie-Zustand, Linkverhältnis, Link-Dichte, Kohärenz und Spannung bereit; die Neuron-GUI-Datei ist im aktuellen Upload nicht enthalten und daher nicht geprüft

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

1. neuronale Aktivität und kognitive Innenfunktion fertigstellen
2. `MCMNeuron` auf lokale Aktivierung, Kopplung, Regulation, Nachhall und Kontext-Memory schärfen
3. danach `MCMField` als Mental-Core-Matrix-Wahrnehmungsfeld sauber ausbauen
4. MCM-Feldtopologie / Feldverlauf / Innenfeldspeicher weiter ausbauen
5. `inner_context_clusters` als Innenmusterraum vertiefen
6. `_experience_reward_delta()` auf Zustandswirkung statt Outcome-Etiketten ausrichten
7. danach lokale Erfahrungsrückwirkung tiefer an Innenmuster, Feldformen und neuronale Teilträger koppeln
8. Backtest-Logik als sauberen Kontrollpfad stabil halten
9. Persistenz und Runtime-/Bot-State weiter entkoppeln, wenn die Erfahrungslogik stabiler ist
10. Tests erst nachziehen, wenn die neuronale und kognitive Mechanik fachlich stabil ist
11. GUI-Umbau nachziehen, wenn Brain- und Snapshot-Basis fachlich stabil sind
12. Live-Handoff und Restart-Fälle erst am Schluss real gegen Exchange-Zustand validieren

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

---

# --------------------------------------------------
# 8. Feldentscheidungs-Protokoll / Replay-Sicht
# --------------------------------------------------

Stand 2026-05-03:

- Ein kompaktes MCM-Feldentscheidungs-Protokoll ist eingebaut.
- `MCM_FIELD_DECISION_PROTOCOL_DEBUG` aktiviert die Protokollierung.
- `MCM_FIELD_DECISION_PROTOCOL_EVERY_N` steuert das Sampling; Phasenwechsel und der erste Feldentscheid werden sofort geschrieben.
- Die Datei `debug/mcm_field_decision_protocol.csv` zeigt pro Feldentscheidung:
  - Phase (`observe`, `replan`, `hold`, `act`)
  - Ausloeser / Guard
  - Feldlabel
  - Fokus, Klarheit, Stabilitaet, Fragmentierung und Strain
  - Handlungsfreigabe, Hemmung, regulierten Mut und Decision-Strength
  - Context- und Inner-Context-Cluster
- Im Bot entsteht zusaetzlich `mcm_field_decision_protocol` als laufender Zaehler fuer Phasen, Gruende und Feldlabels.
- Im Experience-Space entsteht `field_decision_outcome_protocol`, damit spaeter pro Phase sichtbar wird, ob `observe`, `replan`, `hold` oder `act` zu mehr Prozessqualitaet, Tragfaehigkeit und Stabilitaet gefuehrt haben.

Fachlicher Nutzen:

- Das MCM-Feld ist damit nicht nur ein Wahrnehmungszustand, sondern bekommt eine erste Replay-Spur.
- Backtests koennen jetzt zeigen, welche Feldzustaende welche Vor-Handlungsphase ausloesen.
- Spaeter kann verglichen werden, ob geduldiges Beobachten, Neuplanen oder Handeln stabilere Erfahrungsfolgen erzeugt.

---

# --------------------------------------------------
# 9. Schreiblast-/Speicher-Performance-Diagnose
# --------------------------------------------------

Stand 2026-05-03:

- Eine kompakte Dateischreib-Profilierung ist eingebaut.
- `MCM_FILE_WRITE_PROFILE_DEBUG` aktiviert die Messung.
- `MCM_FILE_WRITE_PROFILE_MIN_MS` und `MCM_FILE_WRITE_PROFILE_EVERY_N` begrenzen die Messlast.
- Die Datei `debug/mcm_file_write_profile.csv` zeigt:
  - Zielpfad
  - Schreiboperation
  - Dauer in Millisekunden
  - geschriebene Bytes
  - kurzen Kontext
- Gemessen werden aktuell:
  - zentrale Debug-Schreibvorgaenge aus `debug_reader.py`
  - Runtime-Profil-Ausgaben
  - `memory_state.json`
  - Visual-/Inner-Snapshot-JSON
  - MCM-Feldentscheidungs-Protokoll

Fachlicher Nutzen:

- Die naechste Optimierung kann datenbasiert erfolgen.
- Besonders sichtbar werden sollen grosse JSON-Rewrites, zu haeufige Snapshot-Schreibvorgaenge und kleine, aber sehr haeufige CSV-Appends.
- Danach kann entschieden werden, ob Sampling reicht oder ob Memory auf Hot/Cold-State, Delta-Log oder SQLite umgestellt werden sollte.

Auswertung des Laufs `1-2_2026_5m_SOLUSDT.csv` ohne Gedaechtnis:

- `attempt_records.jsonl` war mit ca. 106 MB der groesste Debug-Ausreisser.
- Gemessene Schreiblast:
  - Inner-Snapshot: ca. 60,5 s aggregiert, ca. 126 ms je Write
  - `memory_state.json`: ca. 30,1 s aggregiert, ca. 367 ms je Write
  - Visual-Snapshot: ca. 24,9 s aggregiert, ca. 52 ms je Write
  - Feldentscheidungs-Protokoll und Profil-CSV waren klein im Vergleich
- Gemessene Rechenlast:
  - `primary_field_step`: ca. 222 s aggregiert
  - `compute_runtime_result.total`: ca. 269 s aggregiert
  - `step_mcm_brain.total`: ca. 262 s aggregiert

Erste Entlastung:

- Attempt-Records werden jetzt samplingfaehig geschrieben.
- `TRADE_STATS_ATTEMPT_RECORD_EVERY_N` schreibt standardmaessig nur jede 10. Attempt-Zeile.
- Submitted/Filled/Cancel/Timeout/Blocked-Value-Gate bleiben direkt sichtbar.
- Attempt-Kontexte werden standardmaessig kompakter geschrieben; schwere Snapshot-Nester werden auf Diagnoseachsen reduziert.
- `trade_stats.json` wird auf Attempt-Pfaden nur noch periodisch geschrieben; Exits und Cancels schreiben weiterhin sofort.

Interpretation:

- Die Verlangsamung kommt nicht nur aus Memory.
- Speicher/Debug verursacht deutlich messbare Zusatzlast.
- Der noch groessere Kern ist aber die Feldsimulation selbst, vor allem `primary_field_step` mit 230 Feldagenten.

Nachvergleich mit `debug/alter_debug` gegen den neuen `debug`-Lauf:

- `attempt_records.jsonl`: 101,15 MB -> 2,14 MB, ca. 2,1 Prozent der alten Groesse.
- `mcm_field_decision_protocol.csv`: 2,05 MB -> 0,40 MB.
- `mcm_profile.csv`: 1,10 MB -> 0,22 MB.
- `mcm_file_write_profile.csv`: 0,62 MB -> 0,15 MB.
- Neuer Lauf:
  - 2.225 Attempts
  - 113 Trades
  - 463 geschriebene Attempt-Records
- Alter Lauf:
  - 12.492 Attempts
  - 273 Trades
  - 12.492 geschriebene Attempt-Records

Normalisierte Einordnung:

- Attempt-Record-Schreiben ist nicht mehr der dominante Engpass.
- Snapshot- und Memory-Writes sind pro Write deutlich schneller geworden.
- `primary_field_step` bleibt der groesste Rechenblock.

Zweite Entlastung:

- `MCM_VISUAL_SNAPSHOT_WRITE_EVERY_N` wurde von 10 auf 25 erhoeht.
- `MCM_VISUAL_SNAPSHOT_FORCE_ON_STATE_CHANGE` wurde fuer die aktuelle Backtest-/Brain-Prioritaet deaktiviert.
- Ziel: weniger Visual-/Inner-Snapshot-Rewrites, solange GUI zweitrangig ist.

Fairer Nachvergleich mit gleicher Datei `test_5m_SOLUSDT`:

- Vergleich: `debug/lauf_1_mit_test_5m_SOLUSDT_ohne_memory` gegen aktuellen `debug`-Lauf.
- Attempts: 2.225 -> 1.934
- Trades: 113 -> 109
- `attempt_records.jsonl`: 2,136 MB -> 1,975 MB
- `mcm_field_decision_protocol.csv`: 0,397 MB -> 0,332 MB
- `mcm_profile.csv`: 0,216 MB -> 0,190 MB
- `mcm_file_write_profile.csv`: 0,146 MB -> 0,108 MB

Snapshot-Wirkung:

- Inner-Snapshot-Writes: 141 -> 32
- Visual-Snapshot-Writes: 141 -> 32
- Inner-Snapshot-Schreibzeit: 3.595 ms -> 803 ms
- Visual-Snapshot-Schreibzeit: 1.530 ms -> 359 ms
- `write_visualization_snapshot_bundle.total`: 1.824 ms -> 259 ms

Weiterhin groesster Rechenblock:

- `primary_field_step` blieb pro Schritt nahezu gleich:
  - vorher ca. 102,41 ms
  - danach ca. 101,50 ms
- Die Snapshot-Entlastung ist damit erfolgreich, aber die eigentliche Feldsimulation bleibt der naechste Optimierungsblock.

Start der `primary_field_step`-Pruefung:

- `MCMField.step()` hat nun feinere Profilpunkte:
  - `mcm_field.step.sync_neurons`
  - `mcm_field.step.build_neighbor_state_map`
  - `mcm_field.step.neuron_loop`
  - `mcm_field.step.activity_diffusion`
  - `mcm_field.step.refresh_arrays`
  - `mcm_field.step.refresh_areal_state`
  - `mcm_field.step.field_perception_state`
  - `mcm_field.step.total`
- Die lokale Nachbarschaftslogik wurde entlastet:
  - feste Nachbarlisten werden als Arrays vorgehalten
  - pro Tick werden weniger Dict-/Listenstrukturen gebaut
  - Kopplungskraefte koennen vektorisiert aus 2D-Neighbor-State-Arrays berechnet werden
  - ein redundanter zweiter Sync/Refresh nach dem Feldstep wurde entfernt
- Ein Micro-Smoke mit 230 Agenten lief syntaktisch und funktional durch.

Wichtig:

- Das ist noch keine finale Feldoptimierung, sondern der erste saubere Mess- und Entlastungsschritt.
- Der naechste Testlauf mit `test_5m_SOLUSDT` ohne Memory muss zeigen, ob `primary_field_step` im echten Backtest messbar sinkt und welcher Teil innerhalb von `mcm_field.step.*` dominiert.

Auswertung des folgenden Testlaufs ohne Memory:

- Vergleich: `debug/lauf_2_mit_test_5m_SOLUSDT_ohne_memory` gegen aktuellen `debug`-Lauf.
- `primary_field_step` war leicht besser:
  - vorher ca. 101,50 ms je Profilpunkt
  - danach ca. 98,51 ms je Profilpunkt
- Neue Detailprofile zeigen den groben Innenaufbau:
  - `mcm_field.step.neuron_loop` dominiert mit ca. 53,84 ms je Profilpunkt
  - `mcm_field.step.refresh_areal_state` liegt bei ca. 18,52 ms
  - `mcm_field.step.activity_diffusion` liegt bei ca. 12,52 ms
  - `mcm_field.step.build_neighbor_state_map` liegt bei ca. 2,05 ms
  - `mcm_field.step.field_perception_state` liegt bei ca. 0,70 ms

Zweite Feldentlastung:

- Der gemeinsame Kontext-Memory-Vektor wird jetzt einmal pro Feldstep berechnet und nicht mehr pro Neuron neu aus dem gleichen Context abgeleitet.
- `MCM_NEURON_STEP_RETURN_SNAPSHOT` wurde eingefuehrt und steht standardmaessig auf `False`.
- `MCMNeuron.step()` erzeugt dadurch keinen ungenutzten Snapshot mehr.
- `MCMField.step()` liefert weiterhin den zentralen Feldsnapshot.
- Ein lokaler Micro-Benchmark mit 230 Agenten lag danach bei ca. 98 ms im Mittel.

Interpretation:

- Die Wahrnehmungsmechanik bleibt erhalten.
- Die naechste echte Messung muss wieder ueber `test_5m_SOLUSDT` ohne Memory laufen.
- Wenn `mcm_field.step.neuron_loop` weiterhin dominiert, ist die naechste Optimierung die weitere Vektorisierung des Neuron-Loops.

Auswertung des naechsten Testlaufs:

- `debug/lauf_3_mit_test_5m_SOLUSDT_ohne_memory` wurde als alter Stand verschoben.
- Der aktuelle Lauf liegt in `debug`.
- `lauf_3` enthaelt nur sehr wenige Profilzeilen, deshalb wurde fuer die Performance-Basis weiterhin der letzte vollstaendige Profilvergleich aus `lauf_2` herangezogen.
- Aktueller Lauf:
  - 2.100 Attempts
  - 107 Trades
  - `primary_field_step`: ca. 85,46 ms je Profilpunkt gegen ca. 101,50 ms in der letzten vollstaendigen Basis
  - `mcm_field.step.total`: ca. 76,57 ms
  - `mcm_field.step.neuron_loop`: ca. 42,26 ms
  - `mcm_field.step.activity_diffusion`: ca. 12,55 ms
  - `mcm_field.step.refresh_areal_state`: ca. 18,06 ms

Dritter Feld-Performance-Schritt:

- `MCM_FIELD_AREAL_REFRESH_EVERY_N` wurde eingefuehrt und steht standardmaessig auf 2.
- Schwere Areal-/Topologie-Metriken werden dadurch nur jeden zweiten Feldtick voll neu berechnet.
- Dazwischen wird der letzte Areal-State mit `areal_refresh_skipped=True` und `areal_stale_ticks` weitergetragen.
- `field_perception_state` bleibt weiterhin pro Feldstep frisch.
- Lokaler Smoke mit 230 Agenten lag nach dieser Aenderung bei ca. 89,6 ms Mittelwert.

Wichtig:

- Diese Aenderung ist fachlich konservativ, weil Areale als traegere Feldstruktur behandelt werden.
- Der naechste echte Nachweis muss wieder mit `test_5m_SOLUSDT` ohne Memory erfolgen.

Auswertung des neuen Laufs:

- Neuer Lauf liegt in `debug`, vorheriger Lauf liegt in `debug/lauf_4_mit_test_5m_SOLUSDT_ohne_memory`.
- `lauf_4` enthaelt nur sehr wenige Profilzeilen, deshalb ist er fuer Performance nur eingeschraenkt brauchbar.
- Fuer die Laufzeit bleibt `debug/lauf_2_mit_test_5m_SOLUSDT_ohne_memory` die letzte vollstaendige Profilbasis.
- Gegen diese Basis ist der primare Feldschritt deutlich schneller:
  - Basis `primary_field_step`: ca. 101,50 ms je Profilpunkt
  - neuer Lauf `primary_field_step`: ca. 74,59 ms je Profilpunkt
  - `step_mcm_brain.total`: ca. 124,98 ms auf ca. 103,39 ms
  - `compute_runtime_result.total`: ca. 50,94 ms auf ca. 36,79 ms
- Die MCM-Feldentscheidung bleibt stabil:
  - `hold`: 1480
  - `act`: 157
  - `observe`: 12
  - kein unkontrolliertes `replan`
- Feldlabels im neuen Lauf:
  - `quiet_field`: 1214
  - `active_perception_field`: 296
  - `fragmented_perception_field`: 138
  - `coherent_perception_field`: 1

Weitere Entlastung und Korrektur:

- Ein erster Versuch hat den Snapshot aus dem primaeren `MCMField.step()` direkt in `step_mcm_brain` weiterverwendet.
- Der neue Vergleich `debug/lauf_5_mit_test_5m_SOLUSDT_ohne_memory` gegen `debug` zeigte:
  - `snapshot_field_read`: ca. 17,92 ms auf ca. 8,51 ms
  - `step_mcm_brain.total`: ca. 103,39 ms auf ca. 87,91 ms
  - Handels-/Phasenlage verschob sich aber staerker als fuer eine rein technische Entlastung sinnvoll ist.
- Grund: Der direkt wiederverwendete Snapshot war zu frueh im Brain-Tick, noch vor nachgelagerter Regulation und Feldanpassung.
- Korrektur:
  - `MCMField.step(..., return_snapshot=False)` wurde eingefuehrt.
  - `step_mcm_brain` laesst den primaeren Feldstep nun keinen Snapshot mehr bauen.
  - Danach wird weiterhin ein finaler Snapshot nach Regulation und Feldanpassung gelesen.
- Damit bleibt die fachliche Reihenfolge des Wahrnehmungsfeldes erhalten, waehrend der ungenutzte fruehe Snapshot entfaellt.

Naechster sinnvoller Anschluss:

- `test_5m_SOLUSDT` ohne Memory erneut laufen lassen.
- Danach pruefen:
  - ob die Ergebnislage wieder naeher am Lauf vor der Snapshot-Korrektur liegt
  - ob `primary_field_step` faellt, weil der ungenutzte fruehe Snapshot nicht mehr erzeugt wird
  - ob `snapshot_field_read` fachlich korrekt als finaler Feldread erhalten bleibt
- Wenn das bestaetigt ist, bleibt als naechster Hauptblock der `mcm_field.step.neuron_loop` mit der neuronalen Kopplung und lokalen Impulsbildung.

Bestaetigung nach Korrekturlauf:

- Alter Lauf liegt in `debug/lauf_6_mit_test_5m_SOLUSDT_ohne_memory`, neuer Lauf liegt in `debug`.
- Die fachliche Lage ist wieder deutlich naeher am stabilen Vorlauf:
  - `lauf_6`: 119 Trades, 28 TP, 91 SL, Equity ca. 85,46
  - neuer Lauf: 111 Trades, 28 TP, 83 SL, Equity ca. 89,39
  - MCM-Phasen neuer Lauf: `hold` 1417, `act` 161, `observe` 16
- Die Korrektur hat die zu fruehe Snapshot-Nutzung damit fachlich bereinigt.
- Laufzeit:
  - `primary_field_step`: ca. 75,63 ms auf ca. 68,28 ms
  - `step_mcm_brain.total`: ca. 87,91 ms auf ca. 90,73 ms
  - `compute_runtime_result.total`: ca. 30,44 ms auf ca. 30,03 ms
  - `snapshot_field_read`: ca. 8,51 ms auf ca. 18,12 ms, bewusst wieder finaler Feldread
- Interpretation:
  - Der ungenutzte fruehe Snapshot ist entfernt.
  - Die final gelesene Wahrnehmung bleibt erhalten.
  - Die groesste verbleibende Feldlast ist nun klar `mcm_field.step.neuron_loop` mit ca. 41,60 ms.

Naechster sinnvoller Anschluss:

- Nicht erneut am finalen Snapshot sparen, solange er fachlich die MCM-Wahrnehmung traegt.
- Als naechstes `mcm_field.step.neuron_loop` bearbeiten:
  - lokale Kontextimpulse pro Neuron vorvektorisieren
  - wiederholte Objekt-/Listen-Zugriffe im Neuron-Loop reduzieren
  - neuronale Kopplung weiter array-basiert vorbereiten
- Danach wieder mit `test_5m_SOLUSDT` ohne Memory pruefen, ob die Phasen stabil bleiben.

Neuron-Loop-Entlastung umgesetzt:

- Die lokale Kontextimpuls-Formel wurde nicht veraendert, aber feldweise vorbereitet.
- Neu:
  - `_build_local_context_memory_matrix(...)`
  - `mcm_field.step.context_memory_matrix` als Profilpunkt
  - `mcm_field.step.prepare_impulse_vectors` als Profilpunkt
- Der globale Kontext-Memory-Vektor wird weiterhin einmal pro Feldstep gebaut.
- Daraus wird nun eine Matrix fuer alle Neuronen erzeugt:
  - lokale Aktivitaet
  - lokaler Memory-Trace
  - lokale Aktivierung
  - lokaler Regulationsdruck
- Diese Werte erzeugen dieselbe Resonanzgewichtung wie vorher pro Neuron, aber ohne 230 einzelne Python-Objektberechnungen im Loop.
- Externe und Replay-Impulsvektoren werden ebenfalls einmal pro Feldstep vorbereitet und an die Neuronen weitergereicht.
- `MCMNeuron.step(...)` akzeptiert dafuer vorbereitete Vektoren, bleibt aber rueckwaertskompatibel mit der alten Scalar-/Listen-Schnittstelle.

Verifikation:

- `py_compile` fuer `MCM_KI_Modell.py` und `MCM_Brain_Modell.py` erfolgreich.
- Gleichheitspruefung alte Einzelberechnung gegen neue Matrix:
  - `max_delta = 0.0`
- Lokaler 230-Agenten-Smoke mit aktivem Kontext:
  - ca. 64,7 ms Mittelwert fuer `MCMField.step(..., return_snapshot=False)`
  - Feldlabel blieb gueltig.

Naechster sinnvoller Anschluss:

- `test_5m_SOLUSDT` ohne Memory erneut laufen lassen.
- Danach pruefen:
  - `mcm_field.step.neuron_loop`
  - `mcm_field.step.context_memory_matrix`
  - `mcm_field.step.prepare_impulse_vectors`
  - Feldphasen `observe`, `hold`, `act`
- Wenn stabil: naechster Hebel ist die Kopplung selbst, also weitere Array-Vorbereitung der Neighbor-Forces.

Neuer Analyse-/Fixpunkt fuer Memory danach:

- Ohne Memory ist der Bot schneller und handelt tendenziell mehr, weil weniger Erfahrungsvergleich und weniger kognitive Hemmung aktiv sind.
- Mit Memory wird die Denkstruktur komplexer:
  - Kontextvergleich
  - Erfahrungsaehnlichkeit
  - positive/negative Outcome-Spuren
  - Tragfaehigkeit aus Erfahrung
  - moeglicher Konflikt zwischen aktuellem Feld und Erinnerung
- Das soll nicht als harte Regel geloest werden.
- Ziel ist eine energieeffiziente Meta-Regulation:
  - Memory soll stabile Erfahrung effizient nutzbar machen
  - widerspruechliche Erfahrung soll nicht pauschal bremsen
  - Denkkomplexitaet soll messbar werden
  - hohe kognitive Last soll `observe`/`hold` erklaeren, aber nicht blind gute Setups blockieren
- Nach dem aktuellen Ohne-Memory-Test soll ein Memory-Komplexitaetsprotokoll entstehen mit Feldern wie:
  - `thinking_complexity`
  - `memory_compare_load`
  - `memory_match_count`
  - `memory_support`
  - `memory_inhibition`
  - `memory_conflict`
  - `cognitive_load`
  - `decision_energy_cost`
  - `meta_regulation_need`
- Danach kann entschieden werden, ob die Effizienz in der Denkstruktur verbessert werden muss, ohne die Erfahrung selbst kaputt zu kuerzen.

Fachliche Klammer fuer Reflexion und innere Wahrnehmung:

- Das System soll nicht nur Aussenreize verarbeiten, sondern die eigene Verarbeitung mitwahrnehmen.
- Gekoppelte Akteure:
  - aeussere Wahrnehmung: Markt, Struktur, Impuls, Risiko, Timing
  - innere Wahrnehmung: Tragfaehigkeit, Spannung, Stabilitaet, Ueberlastung, Klarheit, Hemmung, Mut
  - Denken/Organisation: Musterdeutung, Teilmuster-Ergaenzung, Erfahrungsvergleich, Verdichtung, Reorganisation
  - Handeln: `observe`, `hold`, `replan`, kontrolliertes `act`
  - Lernen: Rueckwirkung auf Tragfaehigkeit, Prozessqualitaet, Stabilitaet, Varianz und Erfahrungsspuren
- Memory ist dabei nicht nur Speicher, sondern Resonanz- und Konfliktflaeche fuer innere Organisation.
- Denken erzeugt selbst kognitive Last und muss deshalb als Energie-/Komplexitaetsfaktor sichtbar werden.
- Ziel:
  - nicht maximale Denktiefe
  - nicht starre Memory-Bremse
  - sondern ausreichend reflektierte, energieeffiziente Verdichtung bis ein tragfaehiges Handlungsmuster entsteht
- Wenn die aeussere Wahrnehmung stark ist, aber das innere Feld instabil oder das Denken ueberlastet ist, soll das System eher beobachten, halten oder reorganisieren.
- Wenn aeussere Wahrnehmung, innere Tragfaehigkeit und verdichtete Erfahrung zusammenpassen, soll kontrolliertes Handeln leichter werden.

Dokumentation uebernommen:

- `README.md` wurde um Reflexion, Denkkomplexitaet und energieeffiziente Meta-Regulation als Einstiegsklammer ergaenzt.
- Die README-Dokumentpfade zeigen nun auf `files/UMSETZUNGSPLAN.md`, `files/aktueller_stand.md` und `files/fix_liste.md`.
- `files/UMSETZUNGSPLAN.md` wurde mit Zustimmung um den Architekturabschnitt `Denkkomplexitaet und energieeffiziente Meta-Regulation` ergaenzt.
- Damit ist der Punkt nicht nur als aktueller Fix, sondern auch im Zielbild des Systems verankert.
