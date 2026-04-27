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

---

# --------------------------------------------------
# 3.2 MCMField-Speicherfehler im lokalen Nachbarschafts-/Arealaufbau schließen
# --------------------------------------------------

Bereits korrigiert im aktuellen Dateistand:

- `_build_local_neighbor_state_map()` nutzt zeilenweise Distanzberechnung
- der alte permanente `N x N x D`-Zwischenspeicher ist an dieser Stelle entfernt
- lokale `N x K` Nachbarschaften bleiben erhalten
- jedes Neuron erhält nur lokale Nachbarn als Kopplungsumfeld
- der Feldzustand selbst bleibt als `N x D` erhalten

Fachliche Bedeutung:

- Neuronen dürfen denselben Umweltreiz wahrnehmen
- sie sollen aber nicht alle global vom gesamten Feld gleichgeschaltet werden
- lokale Eigenreaktion, Nachbarschaft, Kohärenz und Resonanz bilden die Informationsinseln

Weiter zu beobachten:

- `_build_areal_state()` baut Areale jetzt ohne dauerhafte vollständige `N x N`-Distanzmatrix auf
- `_build_areal_components()` berechnet Distanzen zeilenweise pro Neuron
- interne Areal-Dichte wird pro Komponente zeilenweise berechnet
- Arealbildung soll lokale Informationsinseln sichtbar machen, nicht globale Feldgleichschaltung erzeugen

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

- der Innenraum wird real über `felt_state`, `thought_state`, `meta_regulation_state`, `expectation_state`, `state_before`, `state_after`, `state_delta` und `mcm_experience_space` getragen
- `inner_context_clusters` sind im aktuellen Code formal vorhanden, werden aktualisiert und persistiert
- Pattern-Verdichtung ist begonnen über `inner_pattern_support`, `inner_pattern_conflict`, `inner_pattern_fragility`, `inner_pattern_bearing`, `pattern_reinforcement` und `pattern_attenuation`
- `active_context_trace` ist als Runtime-Nachhall eingeführt
- aktive Kontextspur besitzt `activation`, Decay und Reaktivierung aus `inner_context_clusters`
- aktive Kontextspur wirkt schwach auf Pattern-Modulation zurück
- aktive Kontextspur wirkt schwach auf Replay-/Feldimpuls zurück
- Rückführung in lokale `MCMNeuron.memory_trace` ist als erste schwache aktive Kontextspur umgesetzt
- `context_memory_impulse` wird im Inner-Snapshot und in der Neuron-GUI als eigene lokale Kontext-Memory-Kennzahl sichtbar
- `field_neuron_context_memory_impulse_norm_mean` läuft jetzt in `inner_context_clusters`, `current_vector`, Experience-Link-Achsen und bleibt über `memory_state` persistierbar
- `context_memory_impulse` wird in der inneren Musterbeschriftung als `memory_reactivated_neurons` sichtbar, wenn lokale Kontextreaktivierung dominiert
- Experience-Similarity führt `context_memory_impulse_axis`, `active_context_activation_axis`, `active_context_balance_axis` und `context_memory_reactivation_axis`


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

Teilweise umgesetzt:

- `_experience_reward_delta()` nutzt `state_support`, `state_strain` und `state_effect_delta` als Bewertungszentrum
- Areal-Stütze, Areal-Konflikt, Felt-Bearing und Regulationskosten laufen in die Bewertung ein
- aktive Kontextspur und `field_neuron_context_memory_impulse_norm_mean` laufen als schwacher Experience-Wirkraum in Support/Strain ein
- formale Outcomes wirken weiter als Ereigniskontext, aber ihre Wirkung wird stärker an `state_effect_delta` gebunden

Offen:

- `tp_hit`, `sl_hit`, `cancel`, `timeout` sind weiterhin sichtbar, aber nicht mehr der Bewertungsanker
- lokale Rückführung auf Feldmuster und neuronale Teilträger bleibt bewusst schwach und muss real beobachtet werden

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
- Feldtopologie läuft jetzt in `inner_field_perception_state`, `inner_context_clusters`, `current_vector`, Experience-Summary und `memory_state`
- `field_topology_state` ist in der Neuron-GUI als Topologie-Zustand, Linkverhältnis, Link-Dichte, Kohärenz und Spannung sichtbar

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
# 5.4 Tests ergänzen
# --------------------------------------------------

Noch offen:

- dedizierte Tests für `bot_gate_funktions.py`
- dedizierte Tests für `mcm_core_engine.py`
- Fokus auf Zustandsentwicklung und Experience-Konsistenz
- Fokus nicht primär auf klassische Trade-Erfolgsmetriken

---

# --------------------------------------------------
