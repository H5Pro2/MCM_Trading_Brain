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

Aktuelle Priorität:

- PRIO 1 ist ab jetzt die Fertigstellung der neuronalen Aktivität und kognitiven Innenfunktion
- danach folgt die saubere Funktion des MCM-Feldes als Mental-Core-Matrix-Wahrnehmungsfeld
- saubere Backtest-Logik bleibt der Kontrollpfad, ist aber nicht als Testdatei-Arbeit die aktuelle Hauptpriorität
- Live-Handoff / echter Exchange-Test bleibt wichtig, wird aber erst am Schluss validiert
- GUI-Ausbau bleibt nachrangig, solange Brain-Mechanik und Experience-Logik nicht fachlich fertig sind
- Testdateien / dedizierter Testausbau bleiben ebenfalls nachrangig, bis die neuronale und kognitive Mechanik steht

Der aktive Arbeitsfokus liegt damit zuerst auf `MCMNeuron`, neuronaler Aktivierung,
lokaler Kopplung, Regulation, Nachhall, Kontext-Memory und kognitiver Innenfunktion.
Danach liegt der Fokus auf `MCMField`, Feldtopologie, Innenmustern,
`inner_context_clusters` und Experience-Bewertung.

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
# 3. PRIO 1 – BRAIN-LOGIK / NEURONALE MECHANIK
# --------------------------------------------------

# --------------------------------------------------
# 3.1 Brain-Mechanik zuerst fertigstellen
# --------------------------------------------------

Aktive Arbeitsrichtung:

- zuerst `MCMNeuron` und neuronale Aktivität als tragende Innenmechanik stabilisieren
- lokale Nachbarschaft, Kopplung, Regulation, Nachhall und Kontext-Memory fachlich sauber halten
- kognitive Innenfunktion aus Wahrnehmung, Verarbeitung, Felt-State, Thought-State, Meta-Regulation und Erwartung sauber führen
- danach `MCMField` als Mental-Core-Matrix-Feld und Wahrnehmungsraum stabilisieren
- Feldtopologie, Arealbildung und Feldverlauf weiter als echte Innenraum-Mechanik ausbauen
- `inner_context_clusters` vom formalen Cluster-Speicher zum Innenmuster- und Innenfeldspeicher vertiefen
- Experience-Bewertung weiter auf Zustandswirkung, Tragfähigkeit, Belastung, Entlastung und Handlungsfähigkeit ausrichten
- Backtest-Pfade als sauberen Kontroll- und Ausführungspfad erhalten

Nicht aktive Hauptpriorität:

- Live-Exchange-Validierung
- GUI-Umbau
- Testdatei-Ausbau

Diese Punkte bleiben wichtig, folgen aber erst nach der fachlichen Stabilisierung des Brains.

---

# --------------------------------------------------
# 3.2 Nachweisraum / Live-Handoff zwischen Pending, Fill und Position schließen
# --------------------------------------------------

Teilweise korrigiert:

- `_handle_pending_entry()` fragt im Live-Pfad `get_active_order_snapshot()` ab
- `source="position_context"` wird an `_finalize_pending_fill_handoff()` übergeben
- `_finalize_pending_fill_handoff()` schreibt `stats.on_attempt(status="filled")`, Episode-Event und `self.position`
- `get_active_order_snapshot()` erzwingt vor der Snapshot-Auswertung einmalig einen synchronen Bootstrap-/Exchange-Sync
- `get_active_order_snapshot()` liest offene Order-TP/SL jetzt aus `takeProfitPrice/stopLossPrice` und `takeProfitRp/stopLossRp`
- `get_active_order_snapshot()` bleibt bei offener Order auch ohne Exchange-`timestamp` verwertbar
- `place_order()` übernimmt identische offene Orders jetzt inklusive `_ACTIVE_TP`, `_ACTIVE_SIDE` und Entry-/Risk-Kontext
- `_sync_with_exchange()` übernimmt eindeutig offene Orders jetzt inklusive `_ACTIVE_TP`, `_ACTIVE_SIDE` und Entry-/Risk-Kontext
- `_sync_with_exchange()` ergänzt bei bereits bestätigter aktiver Order fehlenden `_ACTIVE_TP`, `_ACTIVE_SIDE` und Entry-/Risk-Kontext aus `open_orders`
- `get_active_order_snapshot()` synchronisiert jetzt bei verschwundener aktiver Order aktiv nach
- wenn nach dem Sync eine Position offen ist, bleibt der Positionskontext für den Bot-Handoff erhalten
- wenn keine Position offen ist, wird die verschwundene Order als `exchange_disappeared` in das Cancel-Tracking gegeben
- Live-Fill schreibt den `live_handoff`-Kontext inklusive `pending_order_id`, `snapshot_id`, Entry/TP/SL, `entry_ts` und `handoff_reason` in `position_meta`
- Restart-Recovery schreibt `recovery_source` und `recovery_snapshot` in `meta`
- aktive Restart-Positionen erhalten einen verwertbaren `entry_ts` / `last_checked_ts`
- Restart-Recovery setzt `execution_state` auf `pending_recovered` oder `position_recovered`
- Restart-Recovery schreibt ein technisches Episode-Event über `pending_update` oder `position_update`
- Restart-Recovery markiert Memory-State als dirty und committet den Regulationssnapshot
- Restart-Recovery speichert den wiederhergestellten Zustand sofort per Forced-Save

Weiter zu prüfen:

- echter Live-Test `pending -> filled -> position` gegen Exchange-Zustand
- ob TP/SL/Entry-Kontext nach Restart im echten Exchange-Fall vollständig belastbar bleibt

Folge:

- der Live-Fill-Handoff ist bot-seitig nachgezogen, aber noch nicht real-live-validiert
- dieser Punkt bleibt bewusst nachrangig, bis Brain-Mechanik und Backtest-Logik fachlich stabil sind

---

# --------------------------------------------------
# 3.3 MCMField-Speicherfehler korrigiert / feste Feldtopologie vorbereiten
# --------------------------------------------------

Bereits korrigiert im aktuellen Dateistand:

- `_build_local_neighbor_state_map()` nutzt feste Topologie-Nachbarschaften
- der alte permanente `N x N x D`-Zwischenspeicher ist an dieser Stelle entfernt
- lokale `N x K` Nachbarschaften bleiben erhalten
- jedes Neuron erhält `field_position` und `topology_neighbors`
- der Feldzustand selbst bleibt als `N x D` erhalten
- `MCMField.read_snapshot()` liefert `topology_rows`, `topology_cols`, `topology_positions` und `topology_neighbor_indices`

Fachliche Bedeutung:

- Neuronen dürfen denselben Umweltreiz wahrnehmen
- sie sollen aber nicht alle global vom gesamten Feld gleichgeschaltet werden
- lokale Eigenreaktion, Nachbarschaft, Kohärenz und Resonanz bilden die Informationsinseln
- `velocity` ist als Zustandsbewegung zu verstehen, nicht als Ortsbewegung des Neurons
- Zielbild ist ein neuronales Gewebe aus festen Feldknoten mit beweglichen MCM-Zuständen

Weiter zu beobachten:

- `_build_areal_state()` baut Areale jetzt ohne dauerhafte vollständige `N x N`-Distanzmatrix auf
- `_build_areal_components()` berechnet Distanzen zeilenweise pro Neuron
- interne Areal-Dichte wird pro Komponente zeilenweise berechnet
- Arealbildung soll lokale Informationsinseln sichtbar machen, nicht globale Feldgleichschaltung erzeugen

Offene Zielkorrektur:

- Cluster-/Areal-Lesung weiter auf gekoppelte Zustandsmuster im festen Feld ausrichten
- lokale Erfahrungsmodulation noch nicht stark an feste Feldknoten zurückführen
- höhere Feldauflösung weiter als höhere Wahrnehmungsauflösung behandeln
- `energy` / `velocity` kompatibel als bestehende Runtime-Oberfläche erhalten
- GUI-Snapshot/Visualisierung erst nach fertiger Topologie auf neuronales Gewebe angleichen

Priorität:

1. `field_topology_layout_state` weiter als Wahrnehmungs- und Nachweiswert führen
2. bestehende Runtime-Kompatibilität erhalten
3. Cluster-/Areal-Lesung weiter auf feste Feldknoten nachziehen
4. lokale Rückwirkung erst nach stabiler Topologie vertiefen
5. GUI-Darstellung danach auf neuronales Gewebe angleichen

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
# 4.3 Innenkontextcluster als Innenfeldspeicher und aktive Kontextspur vertiefen
# --------------------------------------------------

Teilweise umgesetzt:

- `MCMNeuron` führt jetzt eine explizitere neuronale Aktivitätslesung
- neue Neuronwerte: `receptivity`, `overload`, `recovery_tendency`, `memory_resonance`, `context_reactivation`, `coupling_resonance`, `activity_label`, `activation_components`
- Außenreiz wird pro Neuron lokal über Eigenzustand, Memory-Ausrichtung, Topologie-Bias und Regulationsdruck moduliert
- `activation` entsteht jetzt aus Außenreiz, Replay, Kontext-Memory, lokaler Kopplung, Memory-Feedback, Velocity und Resonanz
- `neural_felt_state` nutzt die neuen Werte für Überlast, Erholung, Kopplungsresonanz und Kontextreaktivierung
- `MCMField` führt jetzt eine schwache Aktivitätsdiffusion über feste Topologie-Nachbarn
- `field_perception_state` liest lokale Aktivitätsinseln als Wahrnehmungsstruktur
- Aktivitätsinseln führen Masse, Aktivierung, Druck, Kohärenz, Kontextreaktivierung, Spread und `state_label`
- Feldwahrnehmung führt jetzt zusätzlich Fokus, Klarheit, Stabilität, Fragmentierung, Strain und dominante Aktivitätsinsel
- Feldwahrnehmungslabels wie `active_perception_field`, `coherent_perception_field`, `fragmented_perception_field`, `memory_reactivated_field` und `strained_field` sind angebunden
- `field_perception_state` läuft in den MCM-Snapshot und in `inner_field_perception_state`
- Aktivitätsinseln und `field_perception_label` laufen jetzt in `inner_pattern_identity`, `field_pattern_signature`, `field_pattern_vector`, `inner_context_clusters`, `memory_state` und `mcm_experience_space`
- der Kontextcluster-Vektor enthält die Aktivitätsinselachsen, damit ähnliche Innenkontexte nicht nur nach globalem Feldzustand, sondern auch nach lokaler Feldwahrnehmung gruppiert werden
- `processing_state`, `felt_state` und `thought_state` nutzen die Feldwahrnehmung jetzt als kognitive Evidenzschicht
- neue Lesewerte: `field_perception_pressure`, `field_perception_support`, `field_perception_clarity`, `field_perception_focus`, `field_perception_stability`, `field_perception_fragmentation`, `field_perception_strain` plus Inselmetriken in Verarbeitung, Gefühl und Denken
- `meta_regulation_state` nutzt die Feldwahrnehmung jetzt für Handlungshemmung, Handlungsfreigabe, Beobachtungsbedarf und Replan-Druck
- neue Meta-Werte: `field_perception_instability`, `field_observation_need`, `field_replan_pressure`, `field_action_support`
- harte Feldwahrnehmungs-Gates sind ergänzt: starke Fragmentierung führt zu `field_island_fragmentation_guard`, starker Strain zu `field_island_strain_guard`, klare/stabile Feldwahrnehmung zu kontrolliertem `field_perception_clear_act`
- Experience-Umbau ist fachlich geschärft: kein binäres `TP gut / SL schlecht`, sondern neurochemisch gedämpfte Erfahrungswirkung
- Profitabilität bleibt als innere Zielspannung wichtig, aber nur gefiltert über Regelqualität, Tragfähigkeit, Stabilität, Varianz, Entlastung und Überlast
- `build_experience_neurochemical_effect()` ist umgesetzt und trennt Profitspannung, Entlastung, Stabilität, Disziplin, Confidence, Überaktivierung, Chaos, Varianz, Überlast, Tragfähigkeit und Selbstvertrauen
- `_experience_reward_delta()` ist nur noch ein Kompatibilitäts-Wrapper auf `experience_effect_score`
- die neurochemischen Wirkachsen laufen in Experience-Summary, Episode-History, Experience-Space, Link-Buckets und Experience-Similarity-Achsen
- SL-Episoden werden nach oben gedeckelt, damit sauberer Verlust Prozessqualität bestätigen kann, aber kein starkes Gewinnsignal wird
- chaotische TP-Episoden werden durch Chaos-, Varianz- und Überaktivierungsachsen gedämpft
- `inner_context_clusters` tragen jetzt `experience_neurochemical_profile`, `neurochemical_support`, `neurochemical_strain` und gleitende neurochemische `avg_*` / `last_*` Werte
- `pattern_reinforcement`, `pattern_attenuation` und `trust` werden schwach durch Tragfähigkeit/Stabilität oder Chaos/Überaktivierung moduliert
- `active_context_trace` nutzt die neurochemischen Achsen schwach für Nachhall, Handlungsstütze, Beobachtungsdruck, Replan-Druck und Replay-Impuls
- `memory_state.py` persistiert die neuen neurochemischen Clusterprofile
- der Innenraum wird real über `felt_state`, `thought_state`, `meta_regulation_state`, `expectation_state`, `state_before`, `state_after`, `state_delta` und `mcm_experience_space` getragen
- `inner_context_clusters` sind im aktuellen Code formal vorhanden, werden aktualisiert und persistiert
- Pattern-Verdichtung ist begonnen über `inner_pattern_support`, `inner_pattern_conflict`, `inner_pattern_fragility`, `inner_pattern_bearing`, `pattern_reinforcement` und `pattern_attenuation`
- `active_context_trace` ist als Runtime-Nachhall eingeführt
- aktive Kontextspur besitzt `activation`, Decay und Reaktivierung aus `inner_context_clusters`
- aktive Kontextspur wirkt schwach auf Pattern-Modulation zurück
- aktive Kontextspur wirkt schwach auf Replay-/Feldimpuls zurück
- aktive Kontextspur wird zusätzlich neurochemisch gedämpft: tragfähige Muster bleiben erreichbarer, chaotische/überaktive Muster werden vorsichtiger reaktiviert
- Rückführung in lokale `MCMNeuron.memory_trace` ist als erste schwache aktive Kontextspur umgesetzt
- `context_memory_impulse` wird im Inner-Snapshot als eigene lokale Kontext-Memory-Kennzahl sichtbar; die Neuron-GUI-Datei ist im aktuellen Upload nicht enthalten und daher nicht geprüft
- `field_neuron_context_memory_impulse_norm_mean` läuft jetzt in `inner_context_clusters`, `current_vector`, Experience-Link-Achsen und bleibt über `memory_state` persistierbar
- `context_memory_impulse` wird in der inneren Musterbeschriftung als `memory_reactivated_neurons` sichtbar, wenn lokale Kontextreaktivierung dominiert
- Experience-Similarity führt `context_memory_impulse_axis`, `active_context_activation_axis`, `active_context_balance_axis` und `context_memory_reactivation_axis`
- `neural_felt_state` ist als lesende neuronale Felt-Schicht angebunden
- `neural_felt_bearing`, `neural_felt_pressure`, `neural_felt_memory_resonance`, `neural_felt_context_reactivation` und `neural_felt_label` bleiben über `memory_state` persistierbar
- `neural_felt_*` läuft zusätzlich in Experience-Summary, Episode-Felt-Summary, Similarity-Achsen, Runtime-Snapshot, Decision-State, Brain-Snapshot und `active_context_trace`
- `active_context_trace` trägt `neural_felt_*` als Lesefeld ohne stärkere Replay-/Feldimpuls-Gewichtung
- `inner_field_history` ist als lesender Feldverlauf über mehrere Ticks angebunden und über `memory_state` persistierbar
- `inner_field_history_*` läuft in `inner_context_clusters`, `current_vector`, Experience-Summary, Runtime-/Brain-Snapshot, `active_context_trace` und `episode_internal["signal"]`
- `active_context_trace` trägt `inner_field_history_*` als Lesefeld ohne stärkere Replay-/Feldimpuls-Gewichtung
- feste Feldtopologie ist begonnen: `MCMField` führt feste `field_position` und `topology_neighbors` je `MCMNeuron`
- `field_topology_layout_state` läuft in `inner_field_perception_state`, `inner_context_clusters`, `current_vector`, `active_context_trace` und Experience-Similarity-Achsen
- `active_context_trace` trägt `field_topology_layout_state` als Lesefeld ohne stärkere Replay-/Feldimpuls-Gewichtung
- `field_areal_topology_*` läuft in `inner_context_clusters`, `current_vector`, `active_context_trace`, `episode_internal["signal"]` und Experience-Similarity-Achsen
- `field_areal_topology_*` bleibt Lesewert ohne stärkere Replay-/Feldimpuls-Gewichtung
- `inner_pattern_identity` ist als erste Innenmuster-Identität begonnen und läuft in `inner_context_clusters`, `current_vector`, Cluster-Rückgabe, `memory_state` und `active_context_trace`
- `active_context_trace` trägt `field_pattern_signature_key`, `inner_pattern_identity`, `inner_pattern_identity_label` und `inner_pattern_identity_confidence` ohne stärkere Replay-/Feldimpuls-Gewichtung
- `inner_pattern_identity_stability` ist als Lesewert ergänzt und läuft in Cluster-Rückgabe, `active_context_trace`, `mcm_runtime_brain_snapshot["signal"]`, `episode_internal["signal"]`, `mcm_experience_space` und `memory_state`
- `inner_pattern_identity_streak`, `inner_pattern_identity_recurrent`, `inner_pattern_identity_changed` und `inner_pattern_identity_last_seen_tick` bleiben reine Wiedererkennungs-/Stabilitätswerte ohne stärkere Replay-/Feldimpuls-Gewichtung
- Runtime-Profiling ist als Debug-Schicht angebunden und schreibt nach `debug/mcm_profile.csv`


Offen:

- wiederkehrende Feldformen sind noch nicht als echte lokale Erfahrungsareale im Neuronenfeld verankert
- Replay-Rückwirkung bleibt bewusst schwach begrenzt und ist noch kein vollständiger lokaler Erfahrungsumbau

Ergänzte Zieldefinition:

- Informationscluster werden nicht durch Felddruck gelöscht
- Felddruck verändert Priorität, Aktivierung und Zugänglichkeit
- nicht genutzte oder nicht mehr resonante Information verliert aktive Bindungsstärke
- diese Information bleibt als Nachhall oder latente Erfahrung reaktivierbar
- dadurch wird lokaler Organisationsraum frei für neue Clusterbildung
- Reorganisation bedeutet Informationsumschichtung statt Informationsverlust
- Kohärenzstärke beschreibt Verdichtung, Tragfähigkeit und aktuelle Bindung eines Clusters
- GUI-Farben sollen später diese Kohärenzstärke und den Clusterzustand sichtbar machen

Ziel:

- `context_clusters` als äußerer / gesamt-situativer Signaturraum klar halten
- `inner_context_clusters` fachlich davon getrennt als Innenmuster- / Innenfeldspeicher vertiefen
- aktive Kontextspur im Replay-/Feldimpuls weiter kontrolliert beobachten und begrenzen
- Vermeidungs-, Entlastungs-, Reorganisations- und Wiedererkennungslernen sauber auf Innenmuster abbilden
- Clusterzustände als aktiv getragen, nachhallend, latent oder frei werdend unterscheidbar machen

---

# --------------------------------------------------
# 4.4 Experience-Bewertungslogik weiter auf Zustandswirkung umstellen
# --------------------------------------------------

Umgesetzt:

- `build_experience_neurochemical_effect()` nutzt `state_support`, `state_strain` und `state_effect_delta` als Bewertungszentrum
- Areal-Stütze, Areal-Konflikt, Felt-Bearing und Regulationskosten laufen in die Bewertung ein
- aktive Kontextspur und `field_neuron_context_memory_impulse_norm_mean` laufen als schwacher Experience-Wirkraum in Support/Strain ein
- formale Outcomes wirken weiter als Ereigniskontext, aber ihre Wirkung wird stärker an `state_effect_delta` gebunden
- `_experience_reward_delta()` ist nur noch ein Wrapper auf die neurochemische Wirkfunktion
- Experience-Link-Buckets speichern gleitende `avg_*` und `last_*` Profile der neurochemischen Wirkachsen

Offen:

- die neurochemischen Link-Profile sind jetzt schwach als lokale Muster-/Replay-Modulation aktiv, aber noch nicht als tiefes lokales Neuronenareal gelernt
- lokale Rückführung auf Feldmuster und neuronale Teilträger bleibt bewusst schwach und muss real beobachtet werden
- `neural_felt_state` ist noch Diagnose-/Wahrnehmungsschicht und kein starker lokaler Lernverstärker
- `neural_felt_*` wird im `active_context_trace` nur sichtbar mitgetragen und verändert keine Replay-Gewichtung
- `inner_field_history_*` wird im `active_context_trace` und in `episode_internal["signal"]` nur sichtbar mitgetragen und verändert keine Replay-Gewichtung
- `field_topology_layout_state` wird im `active_context_trace` und in Experience-Similarity-Achsen nur sichtbar mitgetragen und verändert keine Replay-Gewichtung
- `field_areal_topology_*` wird im `active_context_trace`, in `episode_internal["signal"]` und in Experience-Similarity-Achsen nur sichtbar mitgetragen und verändert keine Replay-Gewichtung
- `inner_pattern_identity` wird im `active_context_trace` und in `episode_internal["signal"]` nur sichtbar mitgetragen und verändert keine Replay-Gewichtung
- Runtime-Profiling misst nur Laufzeiten und verändert keine Entscheidung, keine Replay-Gewichtung und keine Feldimpulse

Ziel:

- Experience bewertet primär `state_before`, `state_after`, `state_delta` und Tragfähigkeitswirkung
- `tp_hit`, `sl_hit`, `cancel`, `timeout` bleiben nur Ereigniskontext
- positive und negative Rückführung entsteht aus Belastung, Entlastung, Stabilisierung, Fragilisierung und Handlungsfähigkeit
- aktive Kontextspuren verstärken oder schwächen sich aus Wiedererkennung und Zustandswirkung, nicht aus starren Ergebnisetiketten
- Lernen wird dadurch sauberer als Umgangsfähigkeit statt Ergebnisreflex modelliert

---

# --------------------------------------------------
# 4.5 MCM-Feldtopologie / Feldverlauf / Innenfeldspeicher ausbauen
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
# 5.4 Tests später nachziehen
# --------------------------------------------------

Nachrangig, nicht aktuelle Hauptarbeit:

- dedizierte Tests für `bot_gate_funktions.py`
- dedizierte Tests für `mcm_core_engine.py`
- Fokus auf Zustandsentwicklung und Experience-Konsistenz
- Fokus nicht primär auf klassische Trade-Erfolgsmetriken

Wichtig:

- Testdateien werden erst priorisiert, wenn neuronale Aktivität, kognitive Innenfunktion und MCM-Feldmechanik fachlich stabiler sind
- bis dahin bleibt Backtest-Logik der praktische Kontrollpfad für saubere Brain-Funktion

---

# --------------------------------------------------

---

# --------------------------------------------------
# 6. Feldentscheidungs-Protokoll fuer Backtest / Replay
# --------------------------------------------------

Status 2026-05-03: umgesetzt.

Umgesetzt:

- `MCM_FIELD_DECISION_PROTOCOL_DEBUG` und `MCM_FIELD_DECISION_PROTOCOL_EVERY_N` in `config.py` angelegt.
- `MCM_Brain_Modell.py` schreibt ein kompaktes `debug/mcm_field_decision_protocol.csv`.
- Der erste Feldentscheid wird sofort geschrieben; danach greifen Sampling und Phasenwechsel.
- Laufende Zaehler fuer `observe`, `replan`, `hold`, `act`, Gruende und Feldlabels liegen in `bot.mcm_field_decision_protocol`.
- Experience-Space fuehrt `field_decision_outcome_protocol`, um Phasen spaeter gegen Prozessqualitaet, Tragfaehigkeit und Stabilitaet zu pruefen.

Naechster sinnvoller Anschluss:

- Backtest-Lauf auswerten und pruefen, ob Fragmentierung/Strain zu vielen `observe`/`replan` Phasen fuehrt.
- Danach Geschwindigkeit/Mem-Write-Last messen und die Speicherlogik verschlanken.

---

# --------------------------------------------------
# 7. Schreiblast-/Speicher-Performance messen
# --------------------------------------------------

Status 2026-05-03: erster Diagnose-Haken umgesetzt.

Umgesetzt:

- `MCM_FILE_WRITE_PROFILE_DEBUG`, `MCM_FILE_WRITE_PROFILE_MIN_MS` und `MCM_FILE_WRITE_PROFILE_EVERY_N` in `config.py` angelegt.
- `debug_reader.py` schreibt bei aktivierter Messung `debug/mcm_file_write_profile.csv`.
- Erfasst werden Pfad, Operation, Dauer, Bytes und Kontext.
- Messpunkte liegen auf Debug-Schreiber, Runtime-Profil, Memory-State-JSON, Runtime-Snapshot-JSON und Feldentscheidungs-Protokoll.

Naechster sinnvoller Anschluss:

- Einen echten Backtest laufen lassen und `debug/mcm_file_write_profile.csv` auswerten.
- Danach entscheiden:
  - Sampling/Intervalle hochsetzen
  - grosse JSON-Strukturen kappen
  - Hot/Cold-Memory trennen
  - oder Experience/Replay in SQLite bzw. Delta-Logs verschieben.

Ergebnis aus dem Lauf `1-2_2026_5m_SOLUSDT.csv` ohne Gedaechtnis:

- `attempt_records.jsonl` war mit ca. 106 MB zu gross.
- Inner-/Visual-Snapshots und `memory_state.json` erzeugten zusammen deutlich messbare Schreiblast.
- `primary_field_step` ist ebenfalls ein grosser Laufzeitblock und muss separat betrachtet werden.

Erste Optimierung umgesetzt:

- Attempt-JSONL wird ueber `TRADE_STATS_ATTEMPT_RECORD_EVERY_N` gesampelt.
- Attempt-Kontext wird ueber `TRADE_STATS_ATTEMPT_RECORD_COMPACT` verschlankt.
- `trade_stats.json` wird ueber `TRADE_STATS_JSON_SAVE_EVERY_N` auf Attempt-Pfaden periodisch statt bei jedem Attempt geschrieben.
- Outcome-/Exit-Pfade schreiben weiterhin sofort.

Naechster sinnvoller Anschluss:

- Gleichen Backtest erneut laufen lassen und Dateigroessen plus `mcm_file_write_profile.csv` vergleichen.
- Danach Snapshot-Frequenz und MCM-Feld-Rechenlast optimieren.

Nachvergleich `debug/alter_debug` gegen neuen `debug`-Lauf:

- `attempt_records.jsonl` fiel von ca. 101,15 MB auf ca. 2,14 MB.
- Die Attempt-Record-Entlastung greift.
- Snapshot-Writes bleiben nach der Entlastung der groesste Schreibblock.
- `primary_field_step` bleibt der groesste Rechenblock.

Zweite Optimierung umgesetzt:

- `MCM_VISUAL_SNAPSHOT_WRITE_EVERY_N` von 10 auf 25 gesetzt.
- `MCM_VISUAL_SNAPSHOT_FORCE_ON_STATE_CHANGE` fuer Backtest-/Brain-Prioritaet deaktiviert.

Naechster sinnvoller Anschluss:

- Erneut denselben Backtest laufen lassen.
- Danach pruefen, ob Snapshot-Writes wie erwartet weiter fallen.
- Danach `primary_field_step` fachlich optimieren, ohne die MCM-Wahrnehmungsmechanik platt zu machen.

Fairer Nachvergleich mit gleicher Datei `test_5m_SOLUSDT`:

- Snapshot-Writes fielen von 141 auf 32 je Snapshot-Art.
- `write_visualization_snapshot_bundle.total` fiel von ca. 1.824 ms auf ca. 259 ms.
- `attempt_records.jsonl` fiel von 2,136 MB auf 1,975 MB.
- `mcm_file_write_profile.csv` fiel von 0,146 MB auf 0,108 MB.
- `primary_field_step` blieb pro Schritt nahezu gleich bei ca. 101-102 ms.

Naechster sinnvoller Anschluss:

- Nicht weiter zuerst an Debug schreiben optimieren.
- Jetzt `primary_field_step` untersuchen:
  - Agentenanzahl
  - lokale Nachbarschaften
  - Insel-/Topologie-Ableitung
  - Snapshot-Feldableitung
  - Moeglichkeit, teure Feldmetriken nur jeden n-ten Tick voll zu berechnen und dazwischen fortzuschreiben.

Erster Schritt umgesetzt:

- `MCMField.step()` besitzt nun Detailprofile fuer Sync, Neighbor-Map, Neuron-Loop, Diffusion, Areal-State, Field-Perception und Total.
- Lokale Nachbarschaften werden als Arrays vorgehalten.
- Kopplung kann vektorisiert aus Neighbor-State-Arrays berechnet werden.
- Ein redundanter zweiter Sync/Refresh nach dem Feldstep wurde entfernt.

Naechster sinnvoller Anschluss:

- `test_5m_SOLUSDT` ohne Memory erneut laufen lassen.
- Danach `mcm_profile.csv` nach `mcm_field.step.*` auswerten.
- Wenn `neuron_loop` dominiert: Kopplung/Neuron-Step weiter vektorisieren.
- Wenn `refresh_areal_state` oder `field_perception_state` dominiert: schwere Areal-/Inselmetriken nur jeden n-ten Tick voll berechnen und dazwischen fortschreiben.

Auswertung nach dem ersten Feldprofil-Lauf:

- `primary_field_step` sank leicht von ca. 101,50 ms auf ca. 98,51 ms je Profilpunkt.
- Dominanter Innenblock ist `mcm_field.step.neuron_loop`.
- Danach folgen `refresh_areal_state` und `activity_diffusion`.
- `field_perception_state` ist nicht der Hauptengpass.

Zweiter Feld-Performance-Schritt umgesetzt:

- Kontext-Memory-Vektor wird pro Feldstep nur noch einmal gebaut.
- `MCM_NEURON_STEP_RETURN_SNAPSHOT=False` verhindert ungenutzte Snapshots aus jedem einzelnen `MCMNeuron.step()`.
- `MCMField.step()` liefert weiterhin den zentralen Snapshot.
- Micro-Benchmark mit 230 Agenten: ca. 98 ms Mittelwert.

Naechster sinnvoller Anschluss:

- `test_5m_SOLUSDT` ohne Memory erneut laufen lassen.
- Danach pruefen, ob `mcm_field.step.neuron_loop` im echten Lauf sinkt.
- Wenn ja: naechster Hebel `activity_diffusion` und/oder `refresh_areal_state` nur jeden n-ten Tick voll berechnen.

Auswertung des folgenden Debuglaufs:

- Der aktuelle Lauf lag in `debug`, der alte Stand in `debug/lauf_3_mit_test_5m_SOLUSDT_ohne_memory`.
- `lauf_3` enthaelt nur wenige Profilzeilen, daher bleibt `lauf_2` die letzte vollstaendige Performance-Basis.
- Gegen diese Basis fiel `primary_field_step` von ca. 101,50 ms auf ca. 85,46 ms je Profilpunkt.
- Aktuell dominieren:
  - `mcm_field.step.neuron_loop`
  - `mcm_field.step.refresh_areal_state`
  - `mcm_field.step.activity_diffusion`

Dritter Feld-Performance-Schritt umgesetzt:

- `MCM_FIELD_AREAL_REFRESH_EVERY_N=2` eingefuehrt.
- Areal-/Topologie-Metriken werden nur jeden zweiten Feldtick voll berechnet.
- Uebersprungene Ticks tragen den letzten Areal-State mit `areal_refresh_skipped=True`.
- `field_perception_state` wird weiterhin jeden Feldstep aktualisiert.
- Micro-Benchmark mit 230 Agenten: ca. 89,6 ms Mittelwert.

Naechster sinnvoller Anschluss:

- `test_5m_SOLUSDT` ohne Memory erneut laufen lassen.
- Danach pruefen:
  - sinkt `mcm_field.step.refresh_areal_state` erwartungsgemaess?
  - bleibt Feldentscheidung stabil?
  - dominiert danach `activity_diffusion` oder weiter `neuron_loop`?

Auswertung neuer Lauf gegen `lauf_4` und Profilbasis:

- `debug/lauf_4_mit_test_5m_SOLUSDT_ohne_memory` ist als Ergebnisvergleich brauchbar, enthaelt aber fast keine Profilzeilen.
- Fuer Performance bleibt `lauf_2` die letzte vollstaendige Profilbasis.
- Neuer Lauf:
  - `primary_field_step`: ca. 74,59 ms statt ca. 101,50 ms in der Basis
  - `step_mcm_brain.total`: ca. 103,39 ms statt ca. 124,98 ms
  - `compute_runtime_result.total`: ca. 36,79 ms statt ca. 50,94 ms
  - MCM-Phasen: `hold` 1480, `act` 157, `observe` 12
- Die Areal-Daempfung wirkt damit in der echten Replay-Logik, ohne die Feldentscheidung sichtbar zu destabilisieren.

Vierter Performance-Schritt geprueft und korrigiert:

- Erster Ansatz: primaeren Snapshot aus `MCMField.step()` direkt in `step_mcm_brain` weiterverwenden.
- Messung `lauf_5` gegen neuen `debug`-Lauf:
  - `snapshot_field_read`: ca. 17,92 ms auf ca. 8,51 ms
  - `step_mcm_brain.total`: ca. 103,39 ms auf ca. 87,91 ms
  - MCM-Phasen blieben grundsaetzlich stabil, aber die Handelslage verschob sich zu stark.
- Bewertung: Der Snapshot war fachlich zu frueh im Brain-Tick, weil danach noch Regulation/Feldanpassung erfolgt.
- Korrektur umgesetzt:
  - `MCMField.step(..., return_snapshot=False)` eingefuehrt.
  - Primaerer Feldstep in `step_mcm_brain` baut keinen ungenutzten Snapshot mehr.
  - Der finale Snapshot nach Regulation bleibt erhalten.

Naechster sinnvoller Anschluss:

- Gleichen Backtest ohne Memory erneut laufen lassen.
- Danach kontrollieren:
  - Ergebnis-/Phasenlage gegen `lauf_5`
  - `primary_field_step`, weil dort der ungenutzte fruehe Snapshot wegfallen sollte
  - `snapshot_field_read`, der als finaler Wahrnehmungsread bewusst erhalten bleibt
- Wenn das stabil ist, als naechstes `mcm_field.step.neuron_loop` weiter vektorisieren.

Korrektur bestaetigt mit neuem Lauf:

- Alter Lauf: `debug/lauf_6_mit_test_5m_SOLUSDT_ohne_memory`.
- Neuer Lauf: `debug`.
- Ergebnis:
  - `lauf_6`: 119 Trades, Equity ca. 85,46
  - neuer Lauf: 111 Trades, Equity ca. 89,39
  - Phasen neuer Lauf: `hold` 1417, `act` 161, `observe` 16
- Performance:
  - `primary_field_step`: ca. 75,63 ms auf ca. 68,28 ms
  - `step_mcm_brain.total`: ca. 87,91 ms auf ca. 90,73 ms
  - `compute_runtime_result.total`: ca. 30,44 ms auf ca. 30,03 ms
  - `snapshot_field_read`: wieder ca. 18,12 ms, weil finaler Snapshot bewusst erhalten bleibt
- Bewertung:
  - fachliche Korrektur erfolgreich
  - frueher ungenutzter Snapshot entfernt
  - finale MCM-Feldwahrnehmung bleibt erhalten

Naechster sinnvoller Anschluss:

- `mcm_field.step.neuron_loop` weiter entlasten.
- Fokus:
  - lokale Kontextimpulse pro Neuron vorvektorisieren
  - Python-Objektzugriffe im Loop reduzieren
  - Kopplungsvorbereitung weiter in Arrays halten
- Danach gleicher Backtest ohne Memory als Stabilitaetsvergleich.

Neuron-Loop-Entlastung umgesetzt:

- `_build_local_context_memory_matrix(...)` eingefuehrt.
- Lokale Kontextimpulse werden nun pro Feldstep als Matrix vorbereitet.
- Die alte Einzel-Neuron-Formel bleibt erhalten:
  - lokale Aktivitaet
  - lokaler Memory-Trace
  - Aktivierung
  - Regulationsdruck
  - Resonanz-Clamp von 0,12 bis 1,0
- Externe und Replay-Impulsvektoren werden ebenfalls einmal pro Feldstep vorbereitet.
- `MCMNeuron.step(...)` akzeptiert vorbereitete Vektoren und bleibt mit der bisherigen Schnittstelle kompatibel.
- Neue Profilpunkte:
  - `mcm_field.step.context_memory_matrix`
  - `mcm_field.step.prepare_impulse_vectors`

Verifikation:

- `py_compile` erfolgreich.
- Matrix gegen alte Einzelberechnung: `max_delta = 0.0`.
- Lokaler 230-Agenten-Smoke: ca. 64,7 ms Mittelwert fuer Feldstep ohne Snapshot.

Naechster sinnvoller Anschluss:

- Gleichen Backtest ohne Memory laufen lassen.
- Danach kontrollieren:
  - sinkt `mcm_field.step.neuron_loop`?
  - bleiben `hold`, `act`, `observe` stabil?
  - wie gross sind die neuen Matrix-/Prepare-Profilpunkte?
- Wenn stabil: Kopplungsberechnung/Neighbor-Forces weiter vektorisieren.

Neuer Fixpunkt nach dem Ohne-Memory-Test:

- Denkstruktur-Komplexitaet mit Memory sichtbar machen.
- Ziel ist nicht, Memory hart zu beschneiden.
- Ziel ist eine energieeffiziente Meta-Regulation der Entscheidung:
  - wie komplex ist die aktuelle Denkstruktur?
  - wie viel Memory-Vergleich findet statt?
  - wie stark hemmt, stuetzt oder widerspricht Memory?
  - wie viel kognitive Last entsteht daraus?
  - fuehrt die Last zu weniger `act`, mehr `hold` oder mehr `observe`?
- Diagnosefelder fuer spaeteres Protokoll:
  - `thinking_complexity`
  - `memory_compare_load`
  - `memory_match_count`
  - `memory_support`
  - `memory_inhibition`
  - `memory_conflict`
  - `cognitive_load`
  - `decision_energy_cost`
  - `meta_regulation_need`
- Fachliche Idee:
  - stabile Erfahrung soll Entscheidungen effizienter und tragfaehiger machen
  - widerspruechliche oder duenne Erfahrung soll nicht chaotisch bremsen, sondern Meta-Regulation ausloesen
  - weniger Trades mit Memory ist nur dann gut, wenn schlechte Trades selektiv reduziert werden
- Reihenfolge:
  - zuerst aktueller Ohne-Memory-Test fuer Brain/MCM-Feld abschliessen
  - danach identischer Lauf mit Memory
  - dann Komplexitaets-/Meta-Regulations-Protokoll umsetzen

Ergaenzung fuer die spaetere Umsetzung:

- Reflexion und innere Wahrnehmung muessen als eigene gekoppelte Ebene sichtbar werden.
- Das System hat nicht nur Aussenwahrnehmung, sondern auch eine Innenwahrnehmung der eigenen Tragfaehigkeit.
- Zusammenhaengende Akteure:
  - Aussenwahrnehmung: Reiz, Marktstruktur, Risiko, Timing
  - Innenwahrnehmung: Stabilitaet, Spannung, Ueberlastung, Klarheit, Mut, Hemmung
  - Denken/Organisieren: Musterdeutung, Teilmuster-Ergaenzung, Erfahrungsvergleich, Reorganisation, Informationsverdichtung
  - Handlung: `observe`, `hold`, `replan`, kontrolliertes `act`
  - Lernen: Prozessqualitaet, Tragfaehigkeit, Stabilitaet, Varianz, Erfahrungsspuren
- Memory darf nicht nur als Archiv oder Bremse wirken.
- Memory soll Resonanz, Unterstuetzung, Konflikt und Teilmuster-Ergaenzung sichtbar machen.
- Kognitive Last durch Denken selbst muss gemessen werden, weil zu viel Organisation Handlung unklar oder teuer machen kann.
- Spaetere Meta-Regulation soll nicht hart regeln, sondern energieeffizient entscheiden:
  - weiterdenken
  - verdichten
  - beobachten
  - halten
  - reorganisieren
  - kontrolliert handeln

Dokumentation ergaenzt:

- `README.md` enthaelt jetzt eine kurze Einstiegsklammer zu Reflexion, Denkkomplexitaet und energieeffizienter Meta-Regulation.
- `README.md` verweist bei den Kerndokumenten auf die realen Pfade unter `files/`.
- `files/UMSETZUNGSPLAN.md` enthaelt jetzt mit Zustimmung den Architekturpunkt `Denkkomplexitaet und energieeffiziente Meta-Regulation`.
- Der offene Folgefix bleibt die konkrete Messung nach dem Ohne-Memory-Test und dem anschliessenden Memory-Vergleich.
