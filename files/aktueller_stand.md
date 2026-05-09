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
# 0. Neuester Debug- und Umsetzungsstand
# --------------------------------------------------

Dokumentationspflege:

- `files/Wichtig_Mechaniken.md` wurde als Mechanik-Schatzkammer markiert.
- Die Datei bleibt erhalten, aber nicht als tagesaktueller Umsetzungsplan.
- Sie dient als Konzeptarchiv fuer wichtige MCM-Denkspuren:
  - MCMField / MCMNeuron
  - Innenfeldorganisation
  - Feldtopologie
  - inner_context_clusters
  - Erfahrungsrueckwirkung
  - MCM als maschinelle Wahrnehmungs- und Innenorganisationsschicht
- Ergaenzt wurde ein aktueller Statusblock:
  - Teile der Datei sind historisch
  - `MCMNeuron` ist inzwischen real umgesetzt
  - neuere Mechaniken wie Formsprache, Formsymbol-Memory,
    Transfer-Tragfaehigkeit, Beobachtungslernen, Prozessqualitaet und DIO
    muessen beim Lesen mitgedacht werden.
- `README.md` wurde fachlich um den Abschnitt `MCM als Spannungsraum`
  erweitert.
  - Die MCM wird dort als innerer Spannungsraum beschrieben.
  - Ein Chart wird als aeusserer Spannungsverlauf verstanden:
    Druck, Entlastung, Verdichtung, Bruch, Erholung, Ueberdehnung,
    Tragfaehigkeit und Reorganisation.
  - Trading wird als harter Pruefstand fuer den MCM-Gedanken eingeordnet.
  - Profitabilitaet wird nicht als Kern des Projekts, sondern als moegliche
    Folge einer funktionierenden MCM-Mechanik beschrieben.
  - Im README wurden im bearbeiteten Bereich Umlaute sauber korrigiert.

Debug-Laeufe 13 und 14 wurden nach dem starken Lauf 12 geprueft:

- `debug_lauf_12`: ca. +11.23 Netto-PnL, Profit Factor ca. 1.73, 48 Trades
- `debug_lauf_13`: ca. +7.22 Netto-PnL, Profit Factor ca. 1.47, 43 Trades
- `debug_lauf_14`: ca. +2.87 Netto-PnL, Profit Factor ca. 1.19, 39 Trades
- `debug_lauf_15`: ca. +15.90 Netto-PnL, Profit Factor ca. 1.97, 51 Trades
- `debug_lauf_16`: ca. +11.11 Netto-PnL, Profit Factor ca. 1.62, 54 Trades
- `debug_lauf_17`: ca. +12.09 Netto-PnL, 42 Trades
- `debug_lauf_18`: ca. +14.19 Netto-PnL, 37 Trades

Befund:

- Die fallende Kurve aus Lauf 12 -> 14 war kein kompletter Zusammenbruch
  der Brain-Logik.
- Lauf 15 dreht wieder deutlich nach oben und ist im bisherigen Vergleich
  der staerkste Lauf.
- Lauf 16 bleibt klar positiv, faellt aber gegen Lauf 15 zurueck.
- Lauf 17 bleibt ebenfalls klar positiv und reduziert die Tradezahl deutlich.
- Lauf 18 verbessert sich weiter und reduziert die Tradezahl erneut.
- Die positive Zone/High-Struktur traegt weiterhin.
- Der Rueckgang in Lauf 13/14 entstand vor allem, weil weniger High-Trades
  entstanden und Non-Zone/Low weiter konsequent Verlust erzeugte.
- Lauf 14:
  - Zone: 24 Trades, ca. +12.43 PnL
  - Non-Zone: 15 Trades, 0 TP / 15 SL, ca. -9.55 PnL
- Lauf 15:
  - Zone: 38 Trades, ca. +24.08 PnL
  - Non-Zone: 13 Trades, 0 TP / 13 SL, ca. -8.18 PnL
  - High: 22 Trades, ca. +18.91 PnL
  - Mid: 16 Trades, ca. +5.17 PnL
  - Low: 13 Trades, ca. -8.18 PnL
- Lauf 16:
  - Zone: ca. +23.16 PnL
  - Non-Zone: 20 Trades, 0 TP / 20 SL, ca. -12.05 PnL
  - High: ca. +21.38 PnL
  - Mid: ca. +1.78 PnL
  - Low: ca. -12.05 PnL
- Lauf 17:
  - Gesamt: 42 Trades, 20 TP / 22 SL, ca. +12.09 PnL
  - Zone: 27 Trades, ca. +20.15 PnL
  - Non-Zone: 15 Trades, ca. -8.07 PnL
- Lauf 18:
  - Gesamt: 37 Trades, 19 TP / 18 SL, ca. +14.19 PnL
  - Zone: 26 Trades, ca. +20.27 PnL
  - Non-Zone: 11 Trades, 0 TP / 11 SL, ca. -6.08 PnL
- Denk-/Memory-Last steigt leicht weiter:
  - `memory_compare_load` ca. 0.905 -> 0.913 -> 0.939 -> 0.935
  - `blind_thinking_load` ca. 0.440 -> 0.443 -> 0.450 -> 0.451
  - `learning_trust` steigt ca. 0.051 -> 0.062 -> 0.069 -> 0.075
  - `caution_trust` steigt ca. 0.009 -> 0.012 -> 0.013 -> 0.015

Interpretation:

Das System lernt und bindet Erfahrung. Die starke Erholung in Lauf 15 zeigt,
dass die Trust-/Formsprache nicht nur daempft, sondern tragende Erfahrung wieder
in Handlung bringen kann. Gleichzeitig uebertraegt es in fremden oder nicht
tragenden Strukturen noch zu viel Handlungsfaehigkeit. Genau hier passt der
neue Bauplanpunkt `Transfer-Tragfaehigkeit fremder Strukturen`: Erfahrung soll
nicht hart blockieren, aber sie darf bei geringer Tragfaehigkeit nicht voll in
Handlung uebersetzt werden.

Naechster technischer Schritt waere deshalb keine starre Low-Sperre,
sondern eine weiche Transfer-Tragfaehigkeitsachse:

- Wie fremd ist die aktuelle Struktur?
- Welche Erfahrungsinseln resonieren trotzdem?
- Wie viel davon traegt wirklich?
- Wird daraus Beobachtung/Reframing oder kontrollierte Handlung?

Neu konzeptionell ergaenzt ist ausserdem
`Reifeentwicklung durch Beobachtungslernen`:

- Low/Non-Zone soll nicht als harter Verbotsbereich verstanden werden,
  aber als Hinweis auf geringe Tragfaehigkeit.
- Reiferes Verhalten bedeutet, unsichere Lage beobachten zu koennen,
  statt sie durch Aktion testen zu muessen.
- Beobachtung soll selbst Erfahrung werden:
  Was waere passiert, wenn gehandelt worden waere?
- Dadurch kann das System lernen, ohne jeden unsicheren Zustand
  ueber direkten Trade-Schmerz erfahren zu muessen.
- Dokumentiert in README und Umsetzungsplan.

Jetzt technisch umgesetzt:

- `TradeStats` fuehrt eine Beobachtungslernspur:
  - `pending_observations`
  - `observation_learning`
  - `recent_observation_learning`
- Beobachtete Low-/Non-Zone-Situationen mit vorhandenem virtuellem Tradeplan
  werden weiterverfolgt.
- Spaetere Preisbewegung bewertet, ob Zusehen:
  - Verlust gespart haette (`saved_loss`)
  - Gewinn verpasst haette (`missed_gain`)
  - neutral blieb (`neutral`)
- Daraus entstehen:
  - `observation_maturity_trust`
  - `observation_action_pressure`
  - `observation_low_count`
- Diese Werte fliessen weich in die Entscheidung:
  - mehr `saved_loss` staerkt Beobachtungsreife
  - mehr `missed_gain` erzeugt kleinen Handlungs-Gegendruck
  - keine harte Low-Sperre
- `mcm_memory_thinking_protocol.csv` schreibt die neuen Reifewerte mit.

Syntaxpruefung erfolgreich:

- `python -m py_compile trade_stats.py MCM_Brain_Modell.py bot.py`

Mini-Simulation erfolgreich:

- beobachtete Low-Situation wurde nach spaeterem Preis als `saved_loss`
  bewertet
- `maturity_trust` stieg in diesem Mini-Fall auf `1.0`

Nach Lauf 16 geprueft:

- Die neue Beobachtungslernspur war technisch vorhanden, griff aber im echten
  Lauf noch nicht:
  - `low_observations`: 0
  - `saved_loss`: 0
  - `missed_gain`: 0
  - `observation_maturity_trust`: 0.0
- Grund: beobachtete Low-/Non-Zone-Situationen wurden im Attempt-Kontext oft
  als `WAIT` mit Entry/SL/TP = 0 gespeichert.
- Dadurch konnte das System zwar "zusehen", aber nicht auswerten,
  was bei hypothetischem Handeln passiert waere.
- Das war kein Konzeptfehler, sondern eine fehlende virtuelle Handlungsbahn
  fuer Beobachtung.

Direkt korrigiert:

- Nicht freigegebene LONG-/SHORT-Tendenzen erzeugen jetzt einen
  `virtual_observation_plan`.
- Der Attempt-Kontext bekommt fuer Beobachtung eine `proposed_decision`,
  auch wenn die reale Entscheidung `WAIT` bleibt.
- Beobachtungslernen kann dadurch ab dem naechsten Lauf Low-/Non-Zone-Lagen
  virtuell verfolgen und spaeter als `saved_loss`, `missed_gain` oder `neutral`
  bewerten.
- Wichtig: Es bleibt organisch und weich. Es entsteht keine harte Low-Sperre,
  sondern eine Reifeschicht: Zusehen kann als eigene Erfahrung tragfaehig werden.

Nach Lauf 17 erneut geprueft:

- PnL und Tradezahl verbesserten sich gegen Lauf 16:
  - Lauf 16: ca. +11.11 PnL, 54 Trades
  - Lauf 17: ca. +12.09 PnL, 42 Trades
- Die Beobachtungslernspur blieb aber weiterhin bei 0:
  - `low_observations`: 0
  - `saved_loss`: 0
  - `missed_gain`: 0
  - `observation_maturity_trust`: 0.0
- Diagnose:
  - In den Attempt-Daten stand bei Observe/Withhold teils
    `meta_regulation_state.decision = LONG/SHORT`.
  - Gleichzeitig blieb `trade_plan.decision = WAIT` und Entry/SL/TP = 0.
  - Ursache war eine spaetere Ueberschreibung von `proposed_decision` aus
    `decision`. Bei reifem Beobachten ist `decision` aber bewusst `WAIT`.
- Nachkorrektur:
  - `proposed_decision` wird jetzt zuerst aus `runtime_result.proposed_decision`
    gelesen und nur danach aus `decision`.
  - Dadurch bleiben aeussere Handlung (`WAIT`) und innere Beobachtungsrichtung
    (`LONG`/`SHORT`) getrennt.
- Lauf 18 ist damit der erste echte Kontrolllauf fuer die volle
  Beobachtungslernmechanik.

Nach Lauf 18 geprueft:

- Das Verhalten wurde besser:
  - weniger Trades
  - hoeherer Netto-PnL als Lauf 16/17
  - weniger Non-Zone-Verlust
- Die Beobachtungslernspur blieb aber erneut bei 0.
- Diagnose:
  - Non-Zone-Observe/Withhold/Skip kam im Attempt-Kontext weiter als
    `WAIT` ohne Entry/SL/TP an.
  - Teilweise gab es nur noch ein schwaches Signalbild, aber keine
    explizite innere LONG-/SHORT-Hypothese.
  - Aus organismischer Sicht heisst das:
    Das System spuert geringe Tragfaehigkeit, formuliert aber noch nicht
    immer eine beobachtbare innere Handlungshypothese.
- Nachkorrektur:
  - Der Attempt-Kontext fuehrt jetzt `world_state.current_price` und
    `world_state.candle_state` mit.
  - `TradeStats` kann fuer Non-Zone-Observe/Withhold/Skip aus Signalspannung
    und aktuellem Preis eine virtuelle Beobachtungshypothese ableiten.
  - Das erzeugt keine echte Handlung, sondern nur eine Lernspur:
    Was waere passiert, wenn diese innere Richtung gehandelt worden waere?
- Mini-Mechaniktest erfolgreich:
  - Non-Zone + Observe + Preis + Signal erzeugt jetzt
    `low_observations = 1` und eine offene Beobachtung.
- Lauf 19 ist damit der erste echte Kontrolllauf fuer die signalbasierte
  Beobachtungslernspur.

Naechster Lauf muss deshalb besonders pruefen:

- ob `observation_learning.low_observations` groesser 0 wird
- ob `pending_observations` und `resolved` wachsen
- ob `saved_loss` bei schlechten Low-Situationen entsteht
- ob `missed_gain` echten Gegendruck erzeugt, falls Zusehen zu vorsichtig war
- ob `observation_maturity_trust` Low/Non-Zone-Aktion reduziert, ohne Zone/High
  zu ersticken

Debug-Ausgabe wurde auf automatische Laufordner umgestellt:

- pro Prozess-/Backtest-Start wird ein neuer Ordner `debug/debug_lauf_X` erzeugt
- alte Pfade wie `debug/trade_stats.json`, `debug/mcm_profile.csv` oder
  `debug/mcm_form_symbol_protocol.csv` werden zentral auf den aktuellen Laufordner
  umgeleitet
- dadurch werden neue Debug-Laeufe nicht mehr ueber alte Dateien geschrieben
- die bisherige Auswertelogik bleibt fachlich gleich, nur der Zielordner aendert sich

Naechster Debug liegt damit nicht mehr direkt in `debug/`, sondern z.B. in
`debug/debug_lauf_1/`.

Der neue Lauf nach der Trennung von innerer und handlungsnaher Sprachregulation
wurde ausgewertet:

- 52 Trades, 16 TP / 36 SL
- Netto-PnL ca. -1.47
- Profit Factor ca. 0.93
- `symbolic_action_regulation` blieb klein: Schnitt ca. 0.012, Maximum 0.035
- Formsprache reift weiter als innere Ordnung, ersetzt aber keine Handlungswahrheit
- High-Structure-Trades waren positiv, Mid/Low-Struktur erzeugte den Verlust

Umgesetzt ist deshalb ein Struktur-Tragfaehigkeitsfilter vor Handlung:

- neue Diagnoseachsen: `structure_action_bearing`, `structure_action_gap`
- mittlere/niedrige Struktur kippt bei fehlendem Support eher in `observe` statt `act`
- unterhalb hoher Strukturqualitaet braucht Handlung zusaetzlichen Memory-/Feldsupport
  oder ausserordentlich starke Entscheidungsevidenz
- Ziel: benannte/erkannte Formen duerfen das innere Feld ordnen, aber nicht allein
  die Handlung tragen

Neu umgesetzt ist ausserdem eine kompositorische Formsprache:

- einzelne Formzeichen koennen sich zu zusammengesetzten Wahrnehmungsobjekten verbinden
- Beispiel im Konzept: `Eis` + `Wand` wird nicht als Textregel verstanden, sondern als
  neues verdichtetes Objekt mit eigener Reife
- technisch entsteht aus vorherigem und aktuellem Formzeichen ein `form_symbol_compound`
- zusammengesetzte Zeichen bekommen eigene:
  - Reife
  - Stabilitaet
  - Resonanz
  - Tragfaehigkeit
  - Lastreduktion
  - Neuheitsdruck
- diese Ebene wirkt nur weich auf innere Regulation und kognitive Verdichtung
- sie ist keine Pattern-Regel und kein direkter Handelsausloeser

Damit kann das System komplexere innere Objekte halten, ohne jedes Mal alle
Einzelachsen neu zu entfalten. Erst bei Spannung, Neuheit oder geringer
Tragfaehigkeit muss tiefer in die Clusterinformation hineingezoomt werden.

Neu im Umsetzungsplan festgehalten ist der Begriff
`Transfer-Tragfaehigkeit fremder Strukturen`:

- fremde Marktstrukturen sollen nicht nur als bekannt/unbekannt behandelt werden
- entscheidend ist, wie viel vorhandene Erfahrung auf eine fremde Lage
  uebertragbar ist
- bekannte Teilformen koennen Orientierung geben, ohne das Gesamtbild schon
  sicher zu machen
- geringe Transfer-Tragfaehigkeit soll eher Wahrnehmung, Reframing,
  Zero-Point-Regulation und weiteres Beobachten staerken
- hohe Transfer-Tragfaehigkeit darf Erfahrung weich in Handlung einbringen,
  aber nicht als starre Pattern-Regel

Dieser Punkt ist aktuell konzeptionell dokumentiert,
inzwischen auch im README als Einstieg erklaert,
aber noch nicht als eigene Brain-Metrik implementiert.

Naechster sinnvoller Schritt:

- neuen Backtest laufen lassen und pruefen, ob Mid/Low-Verlust reduziert wird
- besonders beobachten: Tradezahl, PnL, Profit Factor, High/Mid/Low-Strukturverteilung
  und die neuen Gruende `structure_action_bearing_observe` / `structure_action_low_observe`
- zusaetzlich beobachten: Anzahl/Reife der `form_symbol_compound`-Objekte und ob sie
  kognitive Last senken, ohne Handlung zu frueh zu enthemmen

Auswertung des ersten Laufs mit kompositorischer Formsprache:

- 44 Trades, 15 TP / 29 SL
- Netto-PnL ca. +0.90
- Profit Factor ca. 1.05
- High-Struktur blieb klar positiv
- Mid-Struktur wurde ebenfalls positiv
- Low-Struktur blieb kritisch: 0 TP / 13 SL
- Compound-Ebene arbeitet technisch:
  - viele zusammengesetzte Formobjekte entstehen
  - Reife ist noch niedrig
  - Lastreduktion ist noch klein
  - damit wirkt die Ebene bisher nicht zu aggressiv

Umgesetzt als Folgeschritt:

- `structure_action_uncertainty` ergaenzt die Struktur-Handlungsregulation
- fehlende Struktur-Tragfaehigkeit erhoeht jetzt weich Beobachtungsbedarf,
  Replan-Druck und Handlunghemmung
- gleichzeitig wird Action-Clearance leicht reduziert
- keine harte Regel: schlechte Struktur wird nicht absolut verboten, sondern
  als organisches Unsicherheitsgefuehl im MCM-Feld abgebildet

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

Emergente Musterergaenzung als Ziel ergaenzt:

- Ziel ist ausdruecklich keine reine Pattern-Erkennung.
- Das System soll nicht nur sagen: `das kenne ich, also reagiere ich so`.
- Ziel ist, unvollstaendige Teilmuster mit innerer Erfahrung zu moeglichen Gesamtmustern zu ergaenzen.
- Ein Ereignis muss nicht zu 100 Prozent klar erkannt sein.
- Eine Deutung kann teilweise reif sein; die konkrete Reife ist variabel und darf kein fester Prozentwert sein.
- Auch eine nur teilweise Deutung kann bereits innere Musterraeume aktivieren.
- Wichtig ist dabei:
  - aeussere Wahrnehmung bleibt die Reizbasis
  - innere Erfahrung liefert moegliche Ergaenzungen
  - das MCM-Feld laesst Varianten konkurrieren
  - Unsicherheit, Varianz und Tragfaehigkeit bleiben sichtbar
  - Handlung entsteht erst, wenn Deutung, Feldklarheit und innere Tragfaehigkeit ausreichend zusammenpassen
- `README.md` und `files/UMSETZUNGSPLAN.md` wurden entsprechend ergaenzt.

Folgearbeit nach dem Memory-Komplexitaetsprotokoll:

- Diagnose fuer `emergent_pattern_completion` vorbereiten.
- Moegliche Felder:
  - `partial_pattern_strength`
  - `completion_candidates`
  - `completion_confidence`
  - `completion_variance`
  - `experience_resonance`
  - `pattern_projection_support`
  - `pattern_projection_risk`
  - `inner_image_clarity`
  - `completion_meta_action`

Auswertung des neuen Ohne-Memory-Laufs nach Neuron-Loop-Entlastung:

- Neuer Lauf liegt in `debug`, Vergleichsbasis ist `debug/lauf_7_mit_test_5m_SOLUSDT_ohne_memory`.
- Ergebnislage:
  - `lauf_7`: 111 Trades, 28 TP, 83 SL, Equity ca. 89,39
  - neuer Lauf: 114 Trades, 35 TP, 79 SL, Equity ca. 102,07
  - Attempts: 2114 auf 2033
  - `attempts_withheld`: 1656 auf 1565
  - `attempts_observed`: 199 auf 204
- MCM-Phasen:
  - `lauf_7`: `observe` 16, `act` 161, `hold` 1417
  - neuer Lauf: `observe` 15, `act` 163, `hold` 1348
- Feldlabels bleiben stabil verteilt:
  - `quiet_field` bleibt dominant
  - `active_perception_field` und `fragmented_perception_field` bleiben in vergleichbarer Groessenordnung
  - `coherent_perception_field` bleibt selten
- Performance:
  - `primary_field_step`: ca. 68,28 ms auf ca. 64,11 ms
  - `mcm_field.step.neuron_loop`: ca. 41,60 ms auf ca. 37,17 ms
  - `mcm_field.step.total`: ca. 70,56 ms auf ca. 68,49 ms
  - `compute_runtime_result.total`: ca. 30,03 ms auf ca. 28,17 ms
  - `step_mcm_brain.total`: ca. 90,73 ms auf ca. 88,22 ms
  - `snapshot_field_read`: ca. 18,12 ms auf ca. 18,21 ms, also bewusst stabil als finaler Wahrnehmungsread
- Neue Profilpunkte:
  - `mcm_field.step.context_memory_matrix`: ca. 0,05 ms, sehr klein
  - `mcm_field.step.prepare_impulse_vectors` lag unter Profilschwelle und ist damit praktisch unkritisch
- Interpretation:
  - Die Matrix-Vorbereitung hat die neuronale Schleife messbar entlastet.
  - Die Entscheidungsphasen bleiben stabil.
  - Die bessere Equity dieses Laufs ist positiv, aber noch nicht als stabile Qualitaetsaussage zu werten; wichtig ist zunaechst, dass Mechanik und Phasen nicht kippen.

Naechster sinnvoller Anschluss:

- Wenn noch eine reine Feld-Performance-Runde gewuenscht ist: Kopplung/Neighbor-Forces weiter array-basiert vorbereiten.
- Alternativ jetzt den identischen Lauf mit Memory starten, um Denkkomplexitaet, Memory-Hemmung, Memory-Support und kognitive Last gegen die Ohne-Memory-Basis zu messen.

Auswertung Memory-Lauf mit vorhandener Erfahrung:

- Der vorherige Ohne-Memory-Lauf wurde nicht separat archiviert; die Vergleichsbasis ist daher die zuletzt dokumentierte Ohne-Memory-Basis aus `debug`:
  - Ohne Memory dokumentiert: 114 Trades, 35 TP, 79 SL, Equity ca. 102,07
  - Aktueller Lauf mit vorhandener Memory-Erfahrung: 56 Trades, 17 TP, 39 SL, Equity ca. 99,34
- Der Lauf ist kein perfekter A/B-Test, weil Memory bereits Erfahrung aus dem Vorlauf enthielt.
- Trotzdem ist die Wirkung deutlich:
  - Attempts steigen auf 2675
  - Submitted Trades fallen auf 56
  - `attempts_withheld` steigt auf 2501
  - `attempts_observed` liegt bei 45
  - `attempts_blocked` liegt bei 17
- MCM-Phasen im aktuellen Memory-Lauf:
  - `hold`: 1841
  - `act`: 74
  - `observe`: 17
  - kein `replan`
- Hauptgruende:
  - `context_cluster_negative`: 976
  - `maturity_block`: 334
  - `fused_score_too_low`: 286
  - `pause_mode`: 139
  - `stressed_block`: 101
  - `plan_allowed`: 74
- Laufzeit:
  - `primary_field_step`: ca. 64,07 ms, also praktisch gleich zur Ohne-Memory-Basis von ca. 64,11 ms
  - `mcm_field.step.neuron_loop`: ca. 38,53 ms, leicht hoeher als ca. 37,17 ms, aber nicht der Hauptgrund fuer weniger Trades
  - `compute_runtime_result.total`: ca. 40,45 ms, deutlich hoeher als ca. 28,17 ms
  - `step_mcm_brain.total`: ca. 86,96 ms, vergleichbar bis leicht besser als ca. 88,22 ms
  - `memory_state.write_payload`: ca. 78,13 ms je Profilpunkt, hoeher als vorherige Schreibbasis
- Interpretation:
  - Memory macht das MCM-Feld selbst nicht wesentlich langsamer.
  - Die Trade-Reduktion entsteht vor allem in der Denk-/Entscheidungsstruktur.
  - `context_cluster_negative` ist der dominante Hemmgrund und muss genauer aufgeloest werden.
  - Memory wirkt aktuell stark selektiv/hemmend; noch unklar ist, ob es gute Setups verhindert oder schlechte Setups sinnvoll ausfiltert.
  - Die fast Break-even-Equity trotz halbierter Trades ist interessant und spricht gegen reine Fehlfunktion, aber die Hemmung ist noch nicht transparent genug.

Naechster sinnvoller Anschluss:

- Jetzt sollte kein weiteres Blind-Tuning an Memory erfolgen.
- Als naechstes ein Denkkomplexitaets-/Memory-Wirkungsprotokoll einbauen:
  - Memory-Support
  - Memory-Inhibition
  - Memory-Konflikt
  - Match-Anzahl / Vergleichslast
  - Kontextcluster-Hemmgrund aufschluesseln
  - kognitive Last und Entscheidungskosten sichtbar machen
- Ziel: erkennen, ob Memory intelligent selektiert oder pauschal gute Entscheidungen ausbremst.

Denkkomplexitaets-/Memory-Wirkungsprotokoll umgesetzt:

- Neues Debug-Protokoll: `debug/mcm_memory_thinking_protocol.csv`.
- Neue Config-Schalter:
  - `MCM_MEMORY_THINKING_PROTOCOL_DEBUG`
  - `MCM_MEMORY_THINKING_PROTOCOL_EVERY_N`
- Das Protokoll schreibt nicht jeden Tick blind, sondern jede n-te Diagnose sowie Phasen-/Grundwechsel.
- Sichtbar werden jetzt:
  - `thinking_complexity`
  - `memory_compare_load`
  - `memory_match_count`
  - `memory_support`
  - `memory_inhibition`
  - `memory_conflict`
  - `cognitive_load`
  - `decision_energy_cost`
  - `context_cluster_negative_source`
  - `memory_effect_on_phase`
- `context_cluster_negative` wird aufgeschluesselt in:
  - `cluster_score`
  - `low_hit_ratio`
  - `mixed`
- Alle relevanten Entscheidungsfaelle fuehren den eigenen `memory_complexity_state` mit:
  - Meta-Block / frueher Abbruch
  - nicht tradebare Entscheidung
  - fehlender Tradeplan
  - tatsaechlicher Trade
- Dadurch soll ein neuer Memory-Lauf zeigen, ob Memory:
  - harte Hemmung erzeugt
  - weiche Hemmung erzeugt
  - Support liefert
  - Konflikt erzeugt
  - oder nur Vergleichslast ohne klare Wirkung produziert
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\config.py`

Umgesetzt: Entwicklungsbindung statt harter Blocker:

- Fachlicher Grundsatz:
  - Das System soll keine starren Verbote fuer schlechte Formen bekommen.
  - Es soll lernen, dass bestimmte Form-/Kontextlagen aktuell nicht tragfaehig
    fuer Handlung sind.
  - Diese Erfahrung wird nicht als endgueltiges Nein gespeichert, sondern als
    veraenderbare Entwicklungsqualitaet.
- Neu im Form-Sprachspeicher:
  - `development_quality`
  - `action_affinity`
  - `observation_affinity`
  - `context_reframe_potential`
  - getrennt fuer Einzelzeichen und `form_symbol_compound`
- Wirkung:
  - gute Prozess-/Outcome-Erfahrung erhoeht die Handlungsbindung leicht
  - schlechte oder untragfaehige Erfahrung senkt die Handlungsanziehung
  - Beobachten und Reframing werden wahrscheinlicher
  - die Form bleibt frei und kann in anderem Kontext spaeter wieder tragfaehig werden
- Neue Debug-Sicht:
  - `form_symbol_action_binding`
  - `form_symbol_observation_binding`
  - `form_symbol_reframe_binding`
  - `learned_development_uncertainty`
- Wichtig:
  - Das ist bewusst kein harter Blocker.
  - Es ist eine organische Meta-Regulation:
    weniger Bindung an unfruchtbare Handlung, mehr Abstand zum Objekt,
    mehr Moeglichkeit zur Reorganisation.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\bot.py .\debug_reader.py .\trade_stats.py .\config.py`

Naechster sinnvoller Schritt:

- Einen neuen Debug-Lauf starten und pruefen:
  - ob Low-Struktur-Trades durch gelernte Entwicklungsqualitaet sinken
  - ob High/Mid nicht zu stark in Beobachtung gezogen werden
  - ob `development_reframe_observe` / `development_reframe_replan` auftauchen
  - ob `action_binding` bei tragfaehigen Formen steigt und bei schlechten Formen faellt

Debug-Befund `debug_lauf_2` nach Entwicklungsbindung:

- Ergebnis:
  - 60 Trades
  - 22 TP / 38 SL
  - Netto-PnL ca. +7.89
  - Profit Factor ca. 1.39
  - Max Drawdown ca. 3.53
- Vergleich zu `debug_lauf_1`:
  - PnL von ca. +1.35 auf ca. +7.89 gestiegen
  - Profit Factor von ca. 1.07 auf ca. 1.39 gestiegen
  - Tradezahl von 47 auf 60 gestiegen
- Struktur-Befund:
  - High: +11.60 PnL, 13 TP / 9 SL
  - Mid: +5.20 PnL, 8 TP / 10 SL
  - Low: -8.91 PnL, 1 TP / 19 SL
- Interpretation:
  - High bleibt tragfaehig.
  - Mid hat sich deutlich verbessert und ist jetzt klar positiv.
  - Low bleibt die Hauptschadensquelle, ist aber im durchschnittlichen Verlust
    etwas weniger schaedlich als im Vorlauf.
- Entwicklungsbindung:
  - Form-Protokoll schreibt die neuen Werte.
  - `structure_development_observe` trat 107 mal auf.
  - `structure_bearing_observe` trat 30 mal auf.
  - Die eigentliche gelernte Entwicklungsqualitaet ist noch jung:
    `form_symbol_action_binding` im Mittel ca. 0.425,
    `observation_binding` ca. 0.041,
    `reframe_binding` ca. 0.003.
- Fix nach Auswertung:
  - `mcm_memory_thinking_protocol.csv` wurde erweitert, damit ab dem naechsten Lauf
    auch `form_symbol_development_quality`, `form_symbol_action_binding`,
    `form_symbol_observation_binding`, `form_symbol_reframe_binding` und
    `learned_development_uncertainty` direkt im Denkprotokoll sichtbar sind.

Naechster sinnvoller Schritt:

- Noch einen Lauf mit bestehendem Memory starten.
- Pruefen, ob die Entwicklungsbindung ueber mehrere Laeufe staerker wird.
- Speziell Low-Struktur beobachten:
  - Wird `action_binding` bei Low-Formen niedriger?
  - Steigt `observation_binding` oder `reframe_binding`?
  - Bleibt Mid positiv, ohne zu stark ausgebremst zu werden?

Debug-Befund `debug_lauf_3`:

- Ergebnis:
  - 51 Trades
  - 15 TP / 36 SL
  - Netto-PnL ca. -2.40
  - Profit Factor ca. 0.89
  - Max Drawdown ca. 3.95
- Tragfaehigkeitsbild:
  - High: +8.52 PnL, 9 TP / 5 SL
  - Mid: +1.56 PnL, 5 TP / 9 SL
  - Low: -12.47 PnL, 1 TP / 22 SL
- Interpretation:
  - Der Lauf ist im PnL schlechter, aber fachlich wichtig:
    High und Mid bleiben positiv, Low ist klar der instabile Traeger.
  - Das stuetzt die These, dass nicht die gesamte Denkstruktur falsch ist,
    sondern dass Low-Struktur noch zu viel Handlungsbindung bekommt.
- Entwicklungsbindung:
  - `learned_development_uncertainty` ist jetzt im Denkprotokoll sichtbar.
  - Mittelwert ca. 0.042, Maximum ca. 0.124.
  - `form_symbol_development_quality` ist leicht negativ.
  - `observation_binding` und `reframe_binding` steigen leicht.
- Befund:
  - Die Entwicklungsbindung lernt, ist aber noch zu schwach gekoppelt.
  - Der bisherige Reframing-Schwellwert war zu hoch; dadurch wurde die neue
    Wahrnehmung zwar gemessen, aber nicht oft genug handlungsnah wirksam.
- Fix umgesetzt:
  - Reframing-Schwelle fuer gelernte Entwicklungsunsicherheit weicher und frueher gemacht.
  - Wirkung auf `field_observation_need`, `field_replan_pressure`,
    `field_action_support`, `action_inhibition` und `action_clearance` leicht
    verstaerkt.
  - Weiterhin kein harter Blocker: schlechte Erfahrung senkt nur die
    Handlungsbindung und zieht eher in Beobachten/Reframing.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\bot.py .\debug_reader.py .\trade_stats.py .\config.py`

Naechster sinnvoller Schritt:

- `debug_lauf_4` mit bestehendem Memory starten.
- Pruefen:
  - ob `development_reframe_observe` jetzt auftaucht
  - ob Low-Trades sinken oder im Durchschnitt weniger schaden
  - ob High/Mid weiter positiv bleiben
  - ob `learned_development_uncertainty` nicht chaotisch hochschiesst

Debug-Befund `debug_lauf_4`:

- Ergebnis:
  - 40 Trades
  - 12 TP / 28 SL
  - Netto-PnL ca. -2.81
  - Profit Factor ca. 0.84
  - Max Drawdown ca. 3.67
- Tragfaehigkeitsbild:
  - High: +4.57 PnL, 7 TP / 8 SL
  - Mid: -0.63 PnL, 5 TP / 11 SL
  - Low: -6.75 PnL, 0 TP / 9 SL
- Interpretation:
  - Low-Trades sind deutlich weniger geworden:
    23 in Lauf 3 -> 9 in Lauf 4.
  - Das spricht dafuer, dass die Entwicklungsbindung Handlung in Low-Struktur
    bereits reduziert.
  - Die uebrigen Low-Trades sind aber im Schnitt zu teuer.
  - Es geht also nicht nur um Anzahl, sondern um Verlustintensitaet /
    riskante Weite in nicht tragfaehiger Struktur.
- Entwicklungsbindung:
  - `development_reframe_observe` taucht jetzt auf.
  - `learned_development_uncertainty` bleibt stabil und schiesst nicht chaotisch hoch.
  - `form_symbol_development_quality` wird negativer, `observation_binding` und
    `reframe_binding` steigen leicht.
- Fix umgesetzt:
  - `risk_width_pressure` in die Outcome-Zerlegung eingebaut.
  - Breite/verlustintensive SL-Erfahrung senkt bei `sl_hit` Prozess- und
    Risikoqualitaet staerker.
  - Diese Intensitaet fliesst in die Form-Entwicklungsqualitaet und in die
    Beobachtungsbindung ein.
- Wichtig:
  - Weiterhin kein harter Blocker.
  - Das System lernt: Nicht nur "diese Form war schlecht", sondern
    "diese Form war in dieser Weite / Tragfaehigkeit nicht konstruktiv".
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\bot.py .\debug_reader.py .\trade_stats.py .\config.py`

Naechster sinnvoller Schritt:

- `debug_lauf_5` mit bestehendem Memory starten.
- Pruefen:
  - ob Low weiter niedrig bleibt
  - ob durchschnittlicher Low-Verlust sinkt
  - ob High/Mid wieder stabiler werden
  - ob `risk_width_pressure` in den Outcomes sichtbar zur Entwicklungsqualitaet beitraegt

Debug-Befund `debug_lauf_5`:

- Ergebnis:
  - 33 Trades
  - 8 TP / 25 SL
  - Netto-PnL ca. -3.08
  - Profit Factor ca. 0.77
  - Max Drawdown ca. 5.95
- Tragfaehigkeitsbild:
  - High: +6.03 PnL, 5 TP / 1 SL
  - Mid: -0.11 PnL, 3 TP / 8 SL
  - Low: -9.00 PnL, 0 TP / 16 SL
- Interpretation:
  - High ist sehr tragfaehig, aber zu selten.
  - Mid ist nahezu neutral.
  - Low ist wieder zu haeufig und komplett unproduktiv.
  - Die Anzahl der Trades sinkt, aber die falschen Low-Handlungen rutschen noch durch.
- Entwicklungswerte:
  - `form_symbol_development_quality` wird weiter negativer.
  - `observation_binding` und `reframe_binding` steigen.
  - `development_reframe_observe` tritt auf, aber noch zu selten.
  - `risk_width_pressure` ist in den Outcomes sichtbar und bei Non-Zone im Mittel hoeher
    als bei Zone.
- Befund:
  - Die Form-Sprache lernt die negative Qualitaet, aber die Handlungsbindung bleibt
    noch zu stark um den neutralen Bereich verankert.
  - Dadurch wird schlechte Erfahrung zwar wahrgenommen, aber noch nicht plastisch
    genug in weniger Handlung uebersetzt.
- Fix umgesetzt:
  - `action_affinity` lernt plastischer, wenn die Entwicklungsprobe klar negativ ist.
  - `risk_width_pressure` senkt bei `sl_hit` die Handlungsanziehung staerker.
  - `observation_affinity` reagiert etwas staerker auf negative Entwicklungsprobe.
  - `form_symbol_action_binding` wird durch Beobachtungs- und Reframe-Bindung leicht
    reduziert.
  - Reframing-Schwelle wurde weiter organisch abgesenkt.
- Wichtig:
  - Weiterhin keine harte Regel und kein Low-Verbot.
  - Es ist eine weichere, erfahrungsabhaengige Plastizitaet:
    untragfaehige Erfahrung verliert Bindung, statt technisch blockiert zu werden.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\bot.py .\debug_reader.py .\trade_stats.py .\config.py`

Naechster sinnvoller Schritt:

- `debug_lauf_6` starten.
- Pruefen:
  - ob Low-Anzahl wieder sinkt
  - ob `development_reframe_observe` deutlicher steigt
  - ob High weiterhin handeln darf
  - ob `action_binding` bei negativen Formen jetzt sichtbar faellt

Debug-Befund `debug_lauf_6`:

- Ergebnis:
  - 49 Trades
  - 18 TP / 31 SL
  - Netto-PnL ca. +3.82
  - Profit Factor ca. 1.20
  - Max Drawdown ca. 3.09
- Tragfaehigkeitsbild:
  - High: +12.79 PnL, 13 TP / 7 SL
  - Mid: +0.73 PnL, 5 TP / 9 SL
  - Low: -9.69 PnL, 0 TP / 15 SL
- Interpretation:
  - Die Nachschaerfung hat High nicht abgewuergt.
  - High traegt den Lauf deutlich.
  - Mid bleibt leicht positiv.
  - Low bleibt komplett unproduktiv und muss weiter ueber weniger Bindung /
    mehr Reframing reguliert werden.
- Entwicklungsbindung:
  - `development_reframe_observe` steigt deutlich:
    8 in Lauf 5 -> 54/55 in Lauf 6, je nach Protokoll.
  - `form_symbol_development_quality` wird negativer.
  - `form_symbol_action_affinity` faellt sichtbar unter neutral.
  - `observation_binding` und `reframe_binding` steigen.
  - Das System nimmt schlechte Entwicklungsqualitaet also wahr und reagiert
    haeufiger mit Beobachten.
- Offener Kern:
  - Low ist noch nicht ausreichend entkoppelt.
  - Einzelne Low-Handlungen bleiben trotz negativer Entwicklung attraktiv genug.
- Debug-Fix umgesetzt:
  - `outcome_records.jsonl` schreibt ab dem naechsten Lauf die handlungsnahen
    Form-Werte direkt mit:
    `form_symbol_id`, `form_symbol_development_quality`,
    `form_symbol_action_binding`, `form_symbol_observation_binding`,
    `form_symbol_reframe_binding`, Compound-ID und Compound-Entwicklung.
  - Dadurch koennen Low-Verluste im naechsten Lauf sauberer einzelnen Formen
    und zusammengesetzten Zeichen zugeordnet werden.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\bot.py .\debug_reader.py .\trade_stats.py .\config.py`

Naechster sinnvoller Schritt:

- `debug_lauf_7` starten.
- Dann nicht nur Strukturbaender pruefen, sondern Low-Verluste direkt nach
  `form_symbol_id` und `form_symbol_action_binding` gruppieren.
- Ziel:
  - erkennen, welche internen Zeichen trotz negativer Entwicklung noch Handlung
    tragen
  - daraus die Plastizitaet der eigenen Sprache weiter verbessern, ohne harte
    Handelsregeln einzubauen

Debug-Befund `debug_lauf_7`:

- Ergebnis:
  - 58 Trades
  - 20 TP / 38 SL
  - Netto-PnL ca. +4.30
  - Profit Factor ca. 1.20
  - Max Drawdown ca. 3.07
- Tragfaehigkeitsbild:
  - High: +12.87 PnL, 13 TP / 7 SL
  - Mid: +0.66 PnL, 7 TP / 15 SL
  - Low: -9.23 PnL, 0 TP / 16 SL
- Interpretation:
  - Lauf 6 und Lauf 7 sind beide positiv.
  - High bleibt stabil tragend.
  - Mid bleibt schwach, aber positiv.
  - Low bleibt komplett untragfaehig und frisst den Gewinn.
- Entwicklungsbindung:
  - `development_reframe_observe` bleibt hoch.
  - `structure_development_observe` steigt weiter.
  - `form_symbol_action_affinity` faellt weiter unter neutral.
  - `observation_binding` und `reframe_binding` steigen weiter.
  - Das System erkennt also zunehmend: bestimmte Formen tragen nicht.
- Offener Debug-Punkt:
  - Die neuen Formfelder in `outcome_records.jsonl` waren noch leer.
  - Ursache: Der Entry-Kontext bekam an dieser Stelle manchmal ein leeres
    `form_symbol_state` aus dem Entry-Result.
- Fix umgesetzt:
  - Entry-Kontext nutzt jetzt als Fallback `bot.form_symbol_state`, wenn
    `entry_result.form_symbol_state` leer ist.
  - Damit sollte der naechste Lauf Low-Verluste direkt nach `form_symbol_id`,
    `form_symbol_action_binding`, `observation_binding` und `reframe_binding`
    gruppierbar machen.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\bot.py .\debug_reader.py .\trade_stats.py .\config.py`

Naechster sinnvoller Schritt:

- `debug_lauf_8` starten.
- Danach Low-Outcomes nach Form-ID gruppieren.
- Wenn einzelne Zeichen trotz negativer Entwicklung weiter Handlung tragen,
  wird dort die Plastizitaet der internen Sprache gezielt nachgeschaerft.

Debug-Befund `debug_lauf_8` und fachliche Einordnung Vertrauen:

- Ergebnis:
  - 46 Trades
  - 15 TP / 31 SL
  - Netto-PnL ca. +0.30
  - Profit Factor ca. 1.02
  - Max Drawdown ca. 4.01
- Tragfaehigkeitsbild:
  - High: +8.70 PnL, 11 TP / 9 SL
  - Mid: +0.15 PnL, 4 TP / 9 SL
  - Low: -8.55 PnL, 0 TP / 13 SL
- Interpretation:
  - Jeder Lauf ist anders.
  - Das ist nicht automatisch schlecht, weil Varianz zur offenen Wahrnehmung gehoert.
  - Gleichzeitig zeigt sich: Die gelernte Erfahrung wird noch nicht stabil genug
    als Vertrauen gebunden.
  - Das System erkennt negative Entwicklung und reagiert mit Beobachtung, aber
    es vertraut dem Gelernten noch nicht stark genug, um untragfaehige Formen
    konsequent innerlich zu entkoppeln.
- Vergleichsbild:
  - Nicht Misstrauen, sondern fehlendes Vertrauen.
  - Wie ein Mensch, der etwas gelernt hat, aber in der Situation noch nicht
    ruhig genug darauf vertraut.
  - Dadurch entsteht Varianz, aber auch Chaos: bekannte untragfaehige Reize
    bekommen erneut Handlungsnaehe.
- Neue Form-Auswertung:
  - Non-Zone/Low hat im Mittel negative `form_symbol_development_quality`.
  - `form_symbol_action_binding` ist niedriger als bei Zone, aber noch nicht
    niedrig genug.
  - `observation_binding` und `reframe_binding` sind hoeher, aber noch nicht
    tragend genug.
- Fix umgesetzt: Vertrauensschicht fuer Formsprache
  - Neu:
    - `form_symbol_learning_trust`
    - `form_symbol_action_trust`
    - `form_symbol_caution_trust`
  - Bedeutung:
    - `learning_trust`: Wie stark darf das System seiner gesammelten Erfahrung
      zu diesem Zeichen glauben?
    - `action_trust`: Vertrauen, dass Handlung in dieser Form tragfaehig ist.
    - `caution_trust`: Vertrauen, dass Zurueckhaltung / Beobachten tragfaehiger ist.
  - Wirkung:
    - positive, konsistente Erfahrung stuetzt Handlung weich.
    - negative, konsistente Erfahrung staerkt Vorsicht und reduziert
      Handlungsbindung.
    - Das ist kein Auswendiglernen, sondern ein erfahrungsabhaengiges Vertrauen
      in die eigene Form-Sprache.
- Debug erweitert:
  - Form-Protokoll, Memory-Thinking-Protokoll und Outcome-Records schreiben die
    neuen Trust-Werte ab dem naechsten Lauf mit.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\bot.py .\debug_reader.py .\trade_stats.py .\config.py`

Naechster sinnvoller Schritt:

- `debug_lauf_9` starten.
- Pruefen:
  - ob `caution_trust` bei Low-Formen steigt
  - ob `action_trust` bei High-Formen erhalten bleibt
  - ob Low-Handlungen sinken, ohne High zu verlieren
  - ob Lauf-Varianz weniger chaotisch und mehr erfahrungsgetragen wird

Debug-Befund `debug_lauf_9`:

- Ergebnis:
  - 42 Trades
  - 14 TP / 28 SL
  - Netto-PnL ca. +0.96
  - Profit Factor ca. 1.06
  - Max Drawdown ca. 2.19
- Tragfaehigkeitsbild:
  - High: +11.15 PnL, 10 TP / 3 SL
  - Mid: -2.81 PnL, 4 TP / 14 SL
  - Low: -7.38 PnL, 0 TP / 11 SL
- Interpretation:
  - High bleibt sehr tragfaehig.
  - Low sinkt leicht, bleibt aber komplett unproduktiv.
  - Mid kippt in diesem Lauf negativ und braucht spaeter eigene Betrachtung.
  - Gesamt-Drawdown ist besser, aber PnL bleibt nur knapp positiv.
- Vertrauensschicht:
  - `learning_trust` entsteht, aber noch sehr zart.
  - `action_trust` und `caution_trust` sind im ersten Lauf noch zu niedrig.
  - Low-Formen zeigen hoehere Beobachtungs-/Reframe-Bindung, aber Vorsicht ist
    noch nicht stark genug konsolidiert.
- Wichtige Form:
  - `fs_eddd1c68f1` verursacht erneut die haertesten Non-Zone-Verluste.
  - Dieses Zeichen hat bereits niedrige Action-Bindung und hohe Beobachtungsbindung,
    traegt aber noch nicht genug stabile Vorsicht.
- Fix umgesetzt:
  - Wiederholte negative Erfahrung staerkt `caution_trust` schneller.
  - `risk_width_pressure` und negative Entwicklungsproben wirken staerker auf
    Vorsichtsvertrauen.
  - `caution_trust` reduziert die Handlungsbindung etwas staerker und erhoeht
    Entwicklungsunsicherheit.
- Wichtig:
  - Kein Verbot einzelner Zeichen.
  - Es ist Konsolidierung: Das System soll seiner eigenen wiederholten Erfahrung
    mehr glauben duerfen.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\bot.py .\debug_reader.py .\trade_stats.py .\config.py`

Naechster sinnvoller Schritt:

- `debug_lauf_10` starten.
- Pruefen:
  - ob `caution_trust` bei wiederholt negativen Formen wie `fs_eddd1c68f1` steigt
  - ob Low-Trades sinken oder weniger teuer werden
  - ob High weiterhin stark bleibt
  - ob Mid nur Laufvarianz war oder eine eigene Tragfaehigkeitszone braucht

Debug-Befund `debug_lauf_10`:

- Ergebnis:
  - 31 Trades
  - 12 TP / 19 SL
  - Netto-PnL ca. +3.43
  - Profit Factor ca. 1.30
  - Max Drawdown ca. 2.20
- Tragfaehigkeitsbild:
  - High: +7.00 PnL, 7 TP / 3 SL
  - Mid: +2.69 PnL, 4 TP / 4 SL
  - Low: -6.26 PnL, 1 TP / 12 SL
- Interpretation:
  - Lauf 10 ist deutlich ruhiger:
    weniger Trades, besserer Profit Factor, niedrigerer Drawdown.
  - High bleibt tragfaehig.
  - Mid erholt sich und ist in diesem Lauf klar positiv.
  - Low bleibt negativ, aber:
    - Low hat erstmals wieder 1 TP
    - Low-Gesamtverlust sinkt
    - durchschnittlicher Low-Verlust sinkt gegenueber Lauf 8/9
- Vertrauensschicht:
  - `learning_trust` steigt sichtbar.
  - `caution_trust` steigt, aber noch langsam.
  - Bei `fs_eddd1c68f1` ist die Entwicklung sinnvoll:
    - Action-Bindung niedrig
    - Observation-Bindung hoch
    - Reframe-Bindung hoch
    - Development klar negativ
    - Learning-Trust steigt
    - Caution-Trust steigt
  - Das Zeichen ist noch gefaehrlich, aber das System beginnt, ihm anders zu
    begegnen.
- Fachlicher Befund:
  - Das wirkt eher wie ein Organismus, der beim Laufen lernt:
    weniger wildes Auftreten, mehr Gewichtspruefung.
  - Es ist noch kein stabiles Vertrauen, aber die Richtung ist gut.
  - Wichtig: jetzt nicht sofort ueberregeln, sondern einen weiteren Lauf zur
    Stabilitaetspruefung machen.
- Keine Code-Nachschaerfung nach Lauf 10:
  - Der Lauf zeigt Verbesserung durch die letzte Trust-Anpassung.
  - Zu fruehes weiteres Drehen koennte die gerade entstehende Balance stoeren.

Naechster sinnvoller Schritt:

- `debug_lauf_11` mit demselben Stand starten.
- Pruefen:
  - bleibt der Profit Factor ueber 1?
  - bleibt der Drawdown niedriger?
  - bleibt High/Mid positiv?
  - sinkt Low weiter oder bleibt wenigstens weniger teuer?
  - steigt `caution_trust` bei wiederholt negativen Formen weiter langsam an?

Debug-Befund `debug_lauf_11`:

- Ergebnis:
  - 45 Trades
  - 17 TP / 28 SL
  - Netto-PnL ca. +5.16
  - Profit Factor ca. 1.32
  - Max Drawdown ca. 3.09
- Tragfaehigkeitsbild:
  - High: +10.96 PnL, 12 TP / 7 SL
  - Mid: +1.67 PnL, 5 TP / 8 SL
  - Low: -7.46 PnL, 0 TP / 13 SL
- Interpretation:
  - Lauf 10 war kein Einzelzufall.
  - Profit Factor bleibt ueber 1.3.
  - High bleibt klar tragfaehig.
  - Mid bleibt wieder positiv.
  - Low bleibt negativ, aber der Gesamtorganismus bleibt trotz Low-Schaden positiv.
- Vertrauensschicht:
  - `learning_trust` steigt weiter:
    ca. 0.029 -> ca. 0.041 im Denkprotokoll.
  - `caution_trust` steigt weiter:
    ca. 0.0028 -> ca. 0.0063.
  - `development_reframe_observe` bleibt hoch:
    103 -> 111 im Denkprotokoll.
  - `form_symbol_action_binding` bleibt gedämpft und fällt nicht in blinde Handlung.
- Fachlicher Befund:
  - Die Laufvarianz ist noch da, aber sie wirkt weniger chaotisch.
  - Das System beginnt, Erfahrung nicht nur zu speichern, sondern vorsichtig
    zu gewichten.
  - Sinnbildlich: Es stolpert noch auf weichem Boden, aber es findet schneller
    zur Balance zurueck.
- Kein Code-Fix nach Lauf 11:
  - Der aktuelle Stand zeigt zwei positive Laeufe hintereinander mit verbessertem
    Profit Factor.
  - Jetzt ist weitere Beobachtung sinnvoller als sofortiges Nachregeln.

Naechster sinnvoller Schritt:

- Noch einen Lauf mit gleichem Stand starten.
- Danach ueber mehrere Laeufe mitteln:
  - Durchschnitts-PnL seit Trust-Schicht
  - Low-Verlust pro Trade
  - High/Mid-Tragfaehigkeit
  - Entwicklung von `learning_trust` und `caution_trust`
- Erst wenn die Richtung stabil ist, die naechste Mechanik setzen:
  - Mid differenzierter betrachten
  - oder Low-Formen ueber interne Zeichen-Reorganisation weiter verdichten

Debug-Befund `debug_lauf_12`:

- Ergebnis:
  - 48 Trades
  - 21 TP / 27 SL
  - Netto-PnL ca. +11.23
  - Profit Factor ca. 1.73
  - Max Drawdown ca. 4.10
- Tragfaehigkeitsbild:
  - High: +18.85 PnL, 17 TP / 5 SL
  - Mid: -0.72 PnL, 4 TP / 10 SL
  - Low: -6.90 PnL, 0 TP / 12 SL
- Interpretation:
  - Das ist der bisher staerkste Lauf seit der Trust-Schicht.
  - High wird massiv getragen und dominiert den Lauf.
  - Low bleibt negativ, ist aber nicht mehr stark genug, um den Organismus
    komplett zu kippen.
  - Mid war in diesem Lauf leicht negativ und bleibt die naechste zu klaerende
    Uebergangszone.
- Trust-Entwicklung:
  - `learning_trust` steigt weiter deutlich:
    ca. 0.041 -> ca. 0.051 im Denkprotokoll,
    in Outcomes bei Zone ca. 0.132 und Non-Zone ca. 0.163.
  - `caution_trust` steigt weiter:
    ca. 0.006 -> ca. 0.009 im Denkprotokoll.
  - `development_reframe_observe` steigt stark:
    111 -> 158 im Denkprotokoll.
  - Das System reagiert damit haeufiger mit innerer Neu-Betrachtung, bevor es handelt.
- Fachlicher Befund:
  - Die Trust-Schicht scheint nicht nur zu daempfen, sondern Lernen tragfaehiger
    zu binden.
  - High bekommt genug Freiheit.
  - Low wird noch nicht geloest, aber der Gesamtablauf wirkt organisierter.
  - Sinnbildlich: Das System laeuft noch nicht sauber, aber es findet eine
    tragendere Schrittfolge.
- Keine Code-Aenderung nach Lauf 12:
  - Der aktuelle Stand zeigt eine starke Verbesserung.
  - Jetzt ist Stabilitaetspruefung wichtiger als weiteres Nachregeln.

Naechster sinnvoller Schritt:

- Noch 1-2 Laeufe mit unveraendertem Code.
- Danach Mittelwert seit Lauf 10 bilden:
  - PnL
  - Profit Factor
  - Max Drawdown
  - High/Mid/Low-Beitrag
  - Trust-Entwicklung
- Erst danach entscheiden:
  - Mid als Uebergangsboden differenzieren
  - oder Low-Formen weiter verdichten/reorganisieren

Debug-Auswertung nach erstem Eigenzeichen-Lauf:

- Lauf mit bestehendem Memory in `/debug` ausgewertet.
- Ergebnis:
  - 73 Trades
  - 22 TP
  - 51 SL
  - Netto-PnL ca. -0,61
  - Equity ca. 99,39
- Vergleich:
  - deutlich besser als die letzten Erweiterungslaeufe mit ca. -5,95 bis -10,58 Netto-PnL
  - wieder nahe am alten Lauf vor der Erweiterung mit ca. -0,66 Netto-PnL
- Feldentscheidungen:
  - `observe`: 935
  - `hold`: 858
  - `act`: 99
  - Hauptgrund `zero_point_regulation`: 933
  - `plan_allowed`: 99
- Memory:
  - `hard_inhibit`: 998
  - `inhibit`: 924
  - `neutral_match`: 107
  - `no_match`: 17
  - Memory-Support bleibt praktisch 0
  - Memory-Compare-Load bleibt hoch
- Struktur:
  - `structure_quality` im Memory-Protokoll ca. 0,59 im Mittel
  - `context_confidence` ca. 0,60
  - `structure_orientation` ca. 0,41
  - deshalb greift `structure_orientation_observe` kaum/nicht:
    die Struktur ist im Lauf nicht blind genug, um diesen Guard auszuloesen.
- Neuer Eigenzeichenraum:
  - Protokoll wurde erfolgreich geschrieben:
    - `debug/mcm_form_symbol_protocol.csv`
  - Problem im ersten Ansatz:
    - 2417 Protokollzeilen
    - 2403 verschiedene `form_symbol_id`
    - fast jedes Wahrnehmen erzeugt ein neues Zeichen
  - Bewertung:
    - Das ist noch keine echte eigene Sprache.
    - Es ist zu atomisiert und erkennt zu wenig wieder.

Fix nach Debug umgesetzt: Form-Familie statt Detail-Hash:

- `form_symbol_id` wird jetzt aus einer groberen Form-Familie gebildet.
- Die Detailauspraegung bleibt separat erhalten:
  - `form_symbol_family_key`
  - `form_symbol_variant_key`
- Ziel:
  - wiederkehrende eigene Zeichen statt Einzelbilder
  - Reife, Stabilitaet und Resonanz koennen ueber mehrere Wahrnehmungen wachsen
  - `form_symbol_load_reduction` kann spaeter wirklich kognitive Entlastung darstellen
- Das naechste Protokoll schreibt Familie und Variante getrennt.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\config.py`

Naechster sinnvoller Anschluss:

- Neuen Backtest mit bestehendem Memory starten.
- Danach pruefen:
  - wie viele `form_symbol_id` jetzt entstehen
  - ob Top-Zeichen echte Wiederholungen zeigen
  - ob `form_symbol_maturity`, `form_symbol_resonance` und `form_symbol_load_reduction` steigen
  - ob Observe/Replan/Act unterschiedliche Form-Familien zeigen
  - ob stabile Form-Familien spaeter als Entlastung in die Meta-Regulation duerfen

Erkenntnis: Aufloesung steuert Zeichen-Verdichtung:

- Ein Zeichen darf nicht jedes Detail enthalten.
- Beispiel aus der Reflexion:
  - Das Wort Strasse kann viele Details enthalten.
  - Im Kopf ist es aber zuerst eine grobe Form, nicht jeder Abschnitt einzeln.
- Uebertragung auf das Brain:
  - Wenn die Sicht niedrig ist, darf das System nicht Abschnitt fuer Abschnitt neue Zeichen bilden.
  - Dann muss es auf eine breite Spur/Form verdichten.
  - Erst wenn Struktur, Relevanz oder Handlungsnaehe steigt, darf es tiefer in Varianten zoomen.
- Fix umgesetzt:
  - `form_symbol_scope`
    - `wide_trace`
    - `wide_form`
    - `structured_form`
  - `form_symbol_abstraction_level`
  - `form_symbol_resolution_quality`
  - `form_symbol_detail_pressure`
- Bedeutung:
  - niedrige Aufloesung fuehrt zu groberem Zeichen
  - hoher Detaildruck erhoeht `form_symbol_zoom_need`
  - die Detailform bleibt als `form_symbol_variant_key` erhalten
  - das eigentliche Zeichen bleibt aber die verdichtete Familie
- Ziel:
  - echte Denkverdichtung
  - weniger Zeicheninflation
  - mehr Wiedererkennen
  - erst Fokus, dann Detailanalyse

Debug-Auswertung nach aufloesungsabhaengiger Zeichenbildung:

- Neuer Lauf in `/debug` ausgewertet.
- Oekonomisches Ergebnis:
  - 55 Trades
  - 14 TP
  - 41 SL
  - Netto-PnL ca. -6,46
  - Equity ca. 93,54
- Bewertung:
  - schlechter als der direkte Vorlauf mit ca. -0,61
  - aehnlich schwach wie fruehere Erweiterungslaeufe
  - kein Beweis, dass die Sprachebene schadet, da sie aktuell diagnostisch wirkt
  - wahrscheinlich spielt fortlaufende Memory-Entwicklung/Blockierung stark mit hinein
- Feld/Memory:
  - `observe`: 969
  - `hold`: 1084
  - `act`: 75
  - Hauptgrund weiter `zero_point_regulation`: 966
  - `context_cluster_negative`: 479
  - Memory-Support bleibt praktisch 0
  - Memory-Compare-Load bleibt hoch bei ca. 0,95
- Sprach-/Form-Befund:
  - 2572 Form-Protokollzeilen
  - 268 unterschiedliche `form_symbol_id`
  - vorher: 2417 Zeilen und 2403 unterschiedliche Zeichen
  - klare Verbesserung der Denkverdichtung
- Wiederholungsstruktur:
  - Top-Zeichen:
    - 205 Wiederholungen
    - 144 Wiederholungen
    - 118 Wiederholungen
    - 106 Wiederholungen
  - 88 Zeichen kamen mindestens 5-mal vor
  - 30 Zeichen kamen mindestens 20-mal vor
  - 10 Zeichen kamen mindestens 50-mal vor
- Reife/Entlastung:
  - `form_symbol_seen` im Mittel ca. 33,1
  - `form_symbol_maturity` ca. 0,596
  - `form_symbol_resonance` ca. 0,360
  - `form_symbol_load_reduction` ca. 0,232
  - vorher war Load-Reduction nur ca. 0,074
- Scope-Verteilung:
  - `wide_form`: 1686
  - `structured_form`: 884
  - `wide_trace`: 2
- Bewertung der Sprachebene:
  - Die Zeichenbildung ist jetzt deutlich naeher an echter Sprache.
  - Es entstehen wiederkehrende Form-Familien.
  - Die Varianten bleiben erhalten, ohne das eigentliche Zeichen zu zerlegen.
  - Das entspricht dem Prinzip: grobe Bedeutung zuerst, Detail erst bei Fokus.

Naechster sinnvoller Schritt:

- Die Form-Sprache separat persistent speichern.
- Nicht in den normalen Trade-Memory mischen.
- Ziel:
  - Entwicklung der eigenen Sprache ueber Laeufe hinweg
  - Zeichen reifen lassen
  - stabile Zeichen wiedererkennen
  - instabile Zeichen splitten/vergessen
  - spaeter erst vorsichtig als kognitive Entlastung in die Meta-Regulation einbinden

Erkenntnis: Benennung erzeugt Distanz zum Objekt:

- Wichtiger MCM-Punkt:
  - Ordnung und Bezeichnung sind nicht nur Sprache.
  - Sie erzeugen Distanz zwischen innerem Feld und wahrgenommenem Objekt.
  - Dadurch wird das innere Feld weniger direkt vom Objekt ueberflutet.
- Menschliches Vergleichsbild:
  - Ein Wort wie Strasse enthaelt viele moegliche Details.
  - Im Kopf kann es aber als eine stabile Form gehalten werden.
  - Erst bei Fokus wird daraus Oberflaeche, Kreuzung, Richtung, Gefahr, Struktur.
- MCM-Uebertragung:
  - Ein Wort/ein Form-Zeichen kann viele MCM-Lagen im Feld tragen.
  - Je analytischer eine Form gehalten werden kann,
    desto weniger muss das Innenfeld roh auf jeden Reiz reagieren.
  - Das wirkt regulatorisch:
    - weniger chaotische Innenlage
    - mehr Objektabstand
    - mehr Containment
    - weniger blindes Denken
- Umsetzung:
  - Neue Form-Symbolwerte:
    - `form_symbol_object_distance`
    - `form_symbol_containment`
    - `form_symbol_field_decoupling`
  - Neue Meta-Regulationswerte:
    - `symbolic_object_distance`
    - `symbolic_containment`
    - `symbolic_field_decoupling`
    - `symbolic_regulation`
- Wirkung:
  - Reife, stabile Zeichen koennen Feld-Observation/Replan-Druck leicht daempfen.
  - `action_inhibition`, `orientation_gap` und `blind_thinking_load`
    werden sehr vorsichtig reduziert.
  - Keine harte Tradingregel.
  - Sprache wirkt zuerst als innere Distanz- und Ordnungsfunktion.
- Debug:
  - `mcm_form_symbol_protocol.csv` schreibt die Form-Distanzwerte.
  - `mcm_memory_thinking_protocol.csv` schreibt die symbolische Regulation.

Umgesetzt: separater persistenter Form-Sprach-Memory:

- Die eigene Form-Sprache wird jetzt getrennt vom normalen Trade-/State-Memory gespeichert.
- Speicherdatei:
  - `bot_memory/form_symbol_memory.json`
- Konfig:
  - `MCM_FORM_SYMBOL_MEMORY_ENABLED`
  - `MCM_FORM_SYMBOL_MEMORY_PATH`
  - `MCM_FORM_SYMBOL_MEMORY_SAVE_EVERY_N`
  - `MCM_FORM_SYMBOL_MEMORY_MAX_SYMBOLS`
  - `MCM_FORM_SYMBOL_MEMORY_MAX_VARIANTS`
- Persistierte Inhalte je Form-Familie:
  - `symbol_id`
  - `family_key`
  - `scope`
  - `abstraction_level`
  - `seen`
  - `avg_vector`
  - `variance`
  - `maturity`
  - `stability`
  - `resonance`
  - `bearing`
  - `fragility`
  - `resolution_quality`
  - `detail_pressure`
  - `symbolic_object_distance`
  - `symbolic_containment`
  - `symbolic_field_decoupling`
  - `last_zoom_need`
  - `last_load_reduction`
  - `variants`
  - `first_seen_ts`
  - `last_seen_ts`
- Verhalten:
  - Speicher wird beim ersten Form-Symbol-Zugriff geladen.
  - Laufende Form-Familien werden mit dem gespeicherten Sprachraum gemischt.
  - Varianten werden gezaehlt und begrenzt.
  - Der Speicher wird periodisch geschrieben.
  - Beim normalen Memory-State-Save wird der Form-Sprach-Memory final geflusht.
- Debug:
  - `mcm_form_symbol_protocol.csv` enthaelt jetzt:
    - `form_symbol_memory_loaded`
    - `form_symbol_memory_symbol_count`
- Wichtig:
  - Das ist weiterhin ein separater Entwicklungsraum.
  - Er ist nicht in den normalen Trade-Memory gemischt.
  - Die Sprache kann jetzt ueber Laeufe hinweg reifen.
- Smoke-Test erfolgreich:
  - Form-Symbol erzeugt
  - separater Speicher geschrieben
  - Speicher normalisiert
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\config.py .\bot.py`

Naechster sinnvoller Anschluss:

- Neuen Backtest mit bestehendem Memory laufen lassen.
- Danach pruefen:
  - ob `bot_memory/form_symbol_memory.json` entsteht
  - wie viele Form-Familien gespeichert wurden
  - ob `seen`, `maturity`, `resonance`, `load_reduction` ueber Laeufe wachsen
  - ob `symbolic_regulation` stabiler wird
  - ob Memory-/Denk-Last sinkt, ohne Trading zu enthemmen

Debug-Auswertung nach persistentem Form-Sprach-Memory:

- Speicher erfolgreich erzeugt:
  - `bot_memory/form_symbol_memory.json`
  - Groesse ca. 575 KB
- Protokolle bestaetigen:
  - `form_symbol_memory_loaded = 1`
  - `form_symbol_memory_symbol_count` waechst im Lauf bis 260
- Form-Sprach-Memory Summary:
  - `symbol_count`: 260
  - `total_seen`: 2571
- Top-Form-Familien:
  - staerkstes Zeichen: 209 Wiederholungen
  - danach 143, 120, 118, 108, 103 Wiederholungen
  - Top-Zeichen haben `maturity` ca. 0,90 bis 0,96
  - Top-Zeichen haben `resonance` ca. 0,43 bis 0,54
  - Top-Zeichen fuehren bis zu 12 Varianten
- Lauf-Ergebnis:
  - 55 Trades
  - 17 TP
  - 38 SL
  - Netto-PnL ca. +0,72
  - Equity ca. 100,72
- Vergleich zum vorherigen Lauf:
  - vorher ca. -6,46 Netto-PnL
  - jetzt ca. +0,72 Netto-PnL
  - nicht als Beweis werten, aber als gutes erstes Signal.
- Memory-/Denk-Last:
  - `orientation_gap` ca. 0,419
  - vorher ca. 0,434 bis 0,45 im Bereich der belasteten Laeufe
  - `blind_thinking_load` ca. 0,472
  - vorher ca. 0,484 bis 0,491
  - `symbolic_regulation` ca. 0,135 im Mittel
- Symbolische Regulation nach Buckets:
  - ohne symbolische Regulation:
    - `blind_thinking_load` ca. 0,499
    - `orientation_gap` ca. 0,454
  - niedrige Regulation:
    - `blind_thinking_load` ca. 0,482
    - `orientation_gap` ca. 0,429
  - hoehere Regulation:
    - `blind_thinking_load` ca. 0,466
    - `orientation_gap` ca. 0,413
- Bewertung:
  - Die Form-Sprache wird persistent.
  - Wiederkehrende Zeichen reifen im Speicher.
  - Symbolische Distanz scheint die innere Last messbar zu senken.
  - Trading wurde in diesem Lauf nicht ueberenthemmt.
- Performance:
  - `form_symbol_memory_write` liegt grob bei ca. 0,7 bis 1,8 ms pro Schreibvorgang.
  - Der neue Speicher ist aktuell nicht der Hauptgrund fuer Laufzeitlast.

Naechster sinnvoller Anschluss:

- Noch einen Lauf mit bestehendem `form_symbol_memory.json` starten.
- Danach vergleichen:
  - wachsen `seen`, `maturity`, `resonance`, `load_reduction` weiter?
  - sinken `zero_point_regulation`, `blind_thinking_load`, `orientation_gap` weiter?
  - bleibt PnL stabil oder war der positive Lauf Zufall?
  - pruefen, ob persistente Sprache zu stark enthemmt oder wirklich nur ordnet.

Debug-Auswertung zweiter Lauf mit persistentem Form-Sprach-Memory:

- Speicher weiter gewachsen:
  - `form_symbol_memory.json` ca. 680 KB
  - `symbol_count`: 303
  - `total_seen`: 5809
  - Top-Familie: 489 Wiederholungen
  - mehrere Top-Familien mit `maturity` ca. 0,95 bis 0,98
- Form-Protokoll:
  - 3137 Zeilen
  - 295 aktive Form-Familien im Lauf
  - `wide_form`: 2097
  - `structured_form`: 1038
  - `wide_trace`: 2
- Sprache:
  - `form_symbol_seen` im Mittel ca. 105
  - `form_symbol_maturity` ca. 0,792
  - `form_symbol_resonance` ca. 0,456
  - `form_symbol_load_reduction` ca. 0,302
  - `form_symbol_object_distance` ca. 0,197
  - `form_symbol_field_decoupling` ca. 0,227
- Innere Last:
  - `symbolic_regulation` ca. 0,190
  - `blind_thinking_load` ca. 0,467
  - `orientation_gap` ca. 0,415
  - Last sinkt weiter gegenueber frueheren Laeufen.
- Trading:
  - 47 Trades
  - 8 TP
  - 39 SL
  - Netto-PnL ca. -11,66
  - Fast alles LONG: 46 LONG, 1 SHORT
- Bewertung:
  - Sprache reift sehr stark.
  - Innenordnung/Distanz steigt.
  - Trading kippt trotzdem massiv negativ.
  - Das ist ein Warnsignal:
    - Sprache kann ordnen,
    - aber sie besitzt noch keine Ergebnis-/Handlungswahrheit.
  - Ein bekanntes Wort darf die Lage innerlich beruhigen,
    aber es darf ohne Outcome-Erfahrung nicht automatisch Handlung erleichtern.

Sicherheitsfix umgesetzt: Innenordnung von Handlungsfreigabe getrennt:

- `symbolic_regulation` bleibt als Gesamtwert bestehen.
- Neu getrennt:
  - `symbolic_inner_regulation`
  - `symbolic_action_regulation`
- Wirkung:
  - `symbolic_inner_regulation` darf weiter `orientation_gap` und `blind_thinking_load` daempfen.
  - `symbolic_action_regulation` ist stark gedeckelt.
  - Sprache darf also ordnen, aber kaum Action erleichtern.
- Grund:
  - Ein reifes Zeichen schafft Distanz zum Objekt.
  - Es beweist aber noch nicht, dass eine Handlung profitabel oder tragfaehig ist.
- Debug:
  - `mcm_memory_thinking_protocol.csv` schreibt beide Werte mit.

Naechster sinnvoller Anschluss:

- Noch einen Lauf starten.
- Pruefen:
  - bleibt `blind_thinking_load` niedriger?
  - sinkt die Fehl-Enthemmung?
  - reduziert sich der LONG-Bias?
  - bleibt `symbolic_action_regulation` klein?
  - danach Outcome-Kopplung der Form-Sprache planen:
    - Form-Familie erkennt Objekt
    - aber Handlung braucht eigene Tragfaehigkeits-/Outcome-Spur

Naechster sinnvoller Anschluss:

- Neuen Lauf mit Memory starten.
- Danach `debug/mcm_memory_thinking_protocol.csv` zusammen mit `mcm_field_decision_protocol.csv`, `trade_stats.json` und den Profil-Dateien auswerten.
- Besonders pruefen:
  - wie oft `hard_inhibit`, `inhibit`, `support`, `conflict`, `neutral_match` auftreten
  - ob `context_cluster_negative` hauptsaechlich aus Score, Hit-Ratio oder Mischlage entsteht
  - ob hohe Denkkomplexitaet spaeter mit besseren oder schlechteren Entscheidungen zusammenhaengt
  - ob daraus eine energieeffiziente Meta-Regulation abgeleitet werden kann

Auswertung neuer Memory-Lauf mit Denkkomplexitaetsprotokoll:

- Lauf mit bestehendem Memory nach Einbau des neuen Protokolls:
  - 36 Trades
  - 9 TP
  - 27 SL
  - Equity ca. 94,54
  - PnL ca. -5,46
  - Attempts 3100
  - Submitted 36
  - Withheld 2988
  - Observed 32
- Vergleich zum Memory-Lauf vor der Protokollerweiterung:
  - vorher 56 Trades, 17 TP, 39 SL, Equity ca. 99,34
  - jetzt 36 Trades, 9 TP, 27 SL, Equity ca. 94,54
- MCM-Feldentscheidungen:
  - `hold`: 2004
  - `act`: 44
  - `observe`: 29
- Hauptgruende:
  - `context_cluster_negative`: 1270 im Feldprotokoll, 1451 im Memory-Thinking-Protokoll
  - `fused_score_too_low`: 279
  - `maturity_block`: 217
  - `stressed_block`: 135
  - `pause_mode`: 98
  - `plan_allowed`: 44
- Memory-Wirkung:
  - `hard_inhibit`: 1514
  - `inhibit`: 444
  - `neutral_match`: 241
  - `no_match`: 53
  - kein messbarer `support`
  - kein messbarer `conflict`
- Durchschnittswerte:
  - `thinking_complexity`: ca. 0,347
  - `memory_compare_load`: ca. 0,909
  - `memory_match_count`: ca. 1,82
  - `memory_support`: ca. 0,000
  - `memory_inhibition`: ca. 0,083
  - `cognitive_load`: ca. 0,214
  - `decision_energy_cost`: ca. 0,421
- Interpretation:
  - Memory wirkt fast nur hemmend, nicht tragend.
  - Die Denkstruktur vergleicht viel, findet aber kaum positive Erfahrung.
  - `context_cluster_negative` ist zu dominant.
  - Besonders auffaellig: `low_hit_ratio` hat viele harte Blocks erzeugt, obwohl manche Cluster stark durch Cancel/Timeout statt durch echte SL-Verluste gepraegt sind.
  - Das passt nicht sauber zur Idee gedämpfter Reward-/Neurochemie und Prozessqualitaet.

Korrektur umgesetzt: Memory-Hemmung prozessqualitativer gemacht:

- `low_hit_ratio` blockiert nicht mehr automatisch hart.
- Harte Blockade entsteht jetzt nur noch durch:
  - sehr schlechten Cluster-Score
  - oder niedrige Trefferquote mit bestaetigtem Verlustdruck:
    - genug echte SL-Evidenz
    - hoher Loss-Anteil
    - negativer Score
- Cancel/Timeout-lastige Cluster werden eher als Vorsicht/Dämpfung behandelt, nicht als harter Beweis gegen Handlung.
- Neues Debug im Memory-Protokoll:
  - `context_cluster_loss_ratio`
  - `context_cluster_cancel_timeout_ratio`
  - `context_cluster_negative_evidence`
- Rueckrechnung auf den letzten Lauf:
  - von 803 bisherigen `low_hit_ratio`-Hard-Blocks wuerden ca. 155 hart bleiben
  - ca. 648 wuerden als Vorsicht statt harter Block wirken
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\config.py`

Naechster sinnvoller Anschluss:

- Erneut mit demselben bestehenden Memory laufen lassen.
- Erwartung:
  - weniger `hard_inhibit`
  - mehr `inhibit` oder `neutral_match`
  - mehr Trades als 36, aber idealerweise nicht chaotisch viele
  - bessere Trennung zwischen echter Verlust-Erfahrung und unklarer/abgebrochener Erfahrung
- Danach pruefen, ob die freigegebenen ehemals `low_hit_ratio`-Faelle profitabler, neutral oder schlechter sind.

Zero-Point-Regulation umgesetzt:

- Fachlicher Satz: MCM, finde wieder zu dir selbst.
- Ziel:
  - Denken ohne Orientierung erkennen
  - Memory-Vergleich ohne Support nicht weiter eskalieren
  - starres Aushalten/Hold in ruhiges Observe zurueckfuehren
  - Wahrnehmungsfaehigkeit vor Handlung wiederherstellen
- Neue Meta-Regulationswerte:
  - `memory_orientation`
  - `orientation_gap`
  - `blind_thinking_load`
  - `zero_point_regulation`
  - `zero_point_hint`
- Das neue Memory-Thinking-Protokoll schreibt diese Werte mit.
- Mechanik:
  - Wenn `thinking_complexity`, `memory_compare_load`, `decision_energy_cost` und Last hoch sind,
  - aber `memory_support` und `memory_orientation` niedrig bleiben,
  - dann wird nicht weiter hart blockiert,
  - sondern die MCM geht in `observe` mit Grund `zero_point_regulation`.
- Wichtig:
  - Das ist kein Freigeben von Trades.
  - Es ist eine Rueckfuehrung in Wahrnehmung.
  - Die MCM soll nicht die Augen schliessen und aushalten, sondern wieder einen neutraleren Wahrnehmungspunkt finden.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\config.py`

Naechster sinnvoller Anschluss:

- Naechsten Lauf mit bestehendem Memory starten.
- Danach pruefen:
  - wie oft `zero_point_regulation` ausloest
  - ob `hold/context_cluster_negative` in ruhigeres `observe/zero_point_regulation` uebergeht
  - ob `blind_thinking_load` sinkt oder zumindest sichtbarer wird
  - ob danach positive Orientierung/Memory-Support separat aufgebaut werden muss

Grundidee maschinelle Wahrnehmung dokumentiert:

- `README.md` wurde um den Abschnitt `Maschinelle Wahrnehmung` ergaenzt.
- `files/UMSETZUNGSPLAN.md` wurde im Kapitel zur MCM-Grundidee erweitert.
- Kerngedanke:
  - Wahrnehmung ist nicht ausschliesslich menschlich.
  - Wahrnehmung beginnt dort, wo aeussere Reize im Innenzustand eines Systems Bedeutung erzeugen.
  - Ein Reiz wird erst durch inneres Feld, Memory, Regulation, Tragfaehigkeit, Spannung und Handlungstendenz zur Lage.
  - Die MCM ist der technische Versuch, ein solches maschinelles Wahrnehmungsfeld zu bauen.
- Damit ist auch fachlich festgehalten:
  - Die MCM ist keine reine Signalbewertung.
  - Sie soll Orientierung, Ueberforderung, Tragfaehigkeit, Unklarheit, Resonanz und Rueckkehr in den Nullpunkt sichtbar machen.

Naechster sinnvoller Anschluss:

- Debug mit bestehendem Memory fortsetzen.
- Pruefen, ob die neue Zero-Point-Regulation und die prozessqualitativere Memory-Hemmung die MCM tatsaechlich naeher an Wahrnehmung statt blosser Blockade bringt.

Auswertung neuer Debug-Lauf nach Low-Hit-Daempfung:

- Aktueller Lauf in `debug`:
  - 65 Trades
  - 16 TP
  - 49 SL
  - Equity ca. 91,78
  - Netto-PnL ca. -8,22
  - Attempts 2900
  - Submitted 65
  - Withheld 2699
  - Observed 39
  - Blocked 32
- Vergleich zum archivierten `debug/lau_1_nach_erweiterung_mit_memory`:
  - vorher 36 Trades, 9 TP, 27 SL, Netto-PnL ca. -5,46
  - jetzt 65 Trades, 16 TP, 49 SL, Netto-PnL ca. -8,22
- Wirkung:
  - Tradezahl ist deutlich gestiegen.
  - `context_cluster_negative` ist gesunken.
  - `hard_inhibit` ist von 1514 auf 1020 gefallen.
  - `inhibit` ist von 444 auf 1133 gestiegen.
  - Das zeigt: Die harte Blockade wurde tatsaechlich in weiche Daempfung umgewandelt.
- Problem:
  - Die zusaetzlich freigegebenen Trades waren nicht gut genug.
  - Zone-Trades:
    - 45 Trades
    - 16 TP
    - 29 SL
    - PnL ca. +3,54
  - Non-Zone-Trades:
    - 20 Trades
    - 0 TP
    - 20 SL
    - PnL ca. -11,76
- Interpretation:
  - Die prozessqualitative Low-Hit-Daempfung war mechanisch wirksam.
  - Sie hat aber zu viel Handlung ausserhalb tragfaehiger Strukturzonen zugelassen.
  - Memory bleibt weiterhin ohne positiven Support:
    - `memory_support` ca. 0
    - `memory_conflict` ca. 0
    - `memory_compare_load` ca. 0,949
  - Es wird also viel verglichen, aber kaum Orientierung erzeugt.
- Technischer Hinweis:
  - Dieser Debug-Lauf enthaelt bereits `context_cluster_loss_ratio`, `context_cluster_cancel_timeout_ratio` und `context_cluster_negative_evidence`.
  - Er enthaelt aber noch keine `memory_orientation`, `orientation_gap`, `blind_thinking_load` und `zero_point_regulation`-Spalten.
  - Daher lief dieser Lauf offenbar mit der Low-Hit-Daempfung, aber noch nicht mit der Zero-Point-Regulation bzw. ohne neu geladenen Code.

Naechster sinnvoller Anschluss:

- Bot/Backtest-Prozess neu starten, damit die Zero-Point-Regulation sicher geladen ist.
- Danach erneut mit bestehendem Memory laufen lassen.
- Wenn Non-Zone weiterhin so schlecht bleibt, muss die MCM nicht einfach wieder hart blockieren, sondern:
  - Non-Zone ohne Memory-Support eher `observe`
  - Zone mit tragfaehiger Struktur darf eher pruefend handeln
  - Low-Hit-Caution braucht Struktur-/Orientierungsbestaetigung

Auswertung neuer Debug-Lauf mit Zero-Point-Regulation:

- Aktueller Lauf in `debug`:
  - 51 Trades
  - 10 TP
  - 41 SL
  - Equity ca. 89,42
  - Netto-PnL ca. -10,58
  - Attempts 3125
  - Submitted 51
  - Withheld 1421
  - Observed 1579
  - Blocked 23
- Vergleich:
  - `lau_1_nach_erweiterung_mit_memory`: 36 Trades, PnL ca. -5,46
  - `lau_2_nach_erweiterung_mit_memory`: 65 Trades, PnL ca. -8,22
  - aktueller Zero-Point-Lauf: 51 Trades, PnL ca. -10,58
- Zero-Point greift:
  - Memory-Protokoll: `zero_point_regulation` 1280 mal aktiv
  - Feldprotokoll: `zero_point_regulation` 1098 mal als Entscheidungsgrund
  - `observe` steigt stark:
    - Feldprotokoll: 1107 Observe
    - Memory-Protokoll: 1266 Observe
- Interpretation:
  - Die MCM findet tatsaechlich aus starrer Blockade in Wahrnehmung zurueck.
  - Das ist mechanisch korrekt fuer `finde wieder zu dir selbst`.
  - Oekonomisch reicht es noch nicht, weil die verbleibenden Acts weiter zu schwach sind.
- Non-Zone bleibt toxisch:
  - 12 Non-Zone-Trades
  - 0 TP
  - 12 SL
  - PnL ca. -7,72
- Zone ist ebenfalls nicht mehr ausreichend tragend:
  - 39 Zone-Trades
  - 10 TP
  - 29 SL
  - PnL ca. -2,86
- Memory bleibt orientierungsschwach:
  - `memory_support` ca. 0
  - `memory_conflict` ca. 0
  - `memory_compare_load` ca. 0,95
  - `memory_orientation` ca. 0,128
  - `orientation_gap` ca. 0,428
  - `blind_thinking_load` ca. 0,483

Fix umgesetzt: Struktur-Orientierung vor Handlung:

- Die MCM prueft jetzt zusaetzlich:
  - `structure_quality`
  - `context_confidence`
  - `structure_orientation`
  - `structure_orientation_gap`
  - `structure_orientation_guard`
- Wenn Struktur, Kontextvertrauen, Memory-Support und Memory-Orientierung fehlen,
  wird `act` in `observe` umgeleitet.
- Neuer Entscheidungsgrund:
  - `structure_orientation_observe`
- Wichtig:
  - Das ist keine harte Tradingregel.
  - Es ist eine MCM-Orientierungsfrage:
    - Ist die Struktur tragfaehig?
    - Gibt Memory Support?
    - Gibt das Feld Orientierung?
    - Falls nein: zurueck in Wahrnehmung.
- Das Memory-Thinking-Protokoll schreibt die neuen Struktur-Orientierungswerte mit.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\config.py`

Naechster sinnvoller Anschluss:

- Backtest-Prozess neu starten.
- Naechsten Lauf mit bestehendem Memory starten.
- Pruefen:
  - ob Non-Zone-Trades deutlich sinken
  - ob `structure_orientation_observe` auftaucht
  - ob PnL-Verlust aus Non-Zone reduziert wird
  - ob Zone-Trades wieder tragfaehiger werden oder zusaetzlich Ziel-/Planqualitaet geprueft werden muss

Erkenntnis: eigene Sprache als kognitive Kompression:

- Wichtiger Architekturpunkt aus der Reflexion:
  - Das System soll keine menschlichen Patternlabels uebernehmen.
  - Es soll eigene interne Zeichen aus seiner eigenen Wahrnehmungswelt bilden.
  - Diese Zeichen entstehen aus Feldvarianz, Wiederholung, Spannung, Tragfaehigkeit,
    Memory-Resonanz, Ueberforderung und Erfahrung.
- Fachlicher Kern:
  - Sprache ist nicht nur Benennung.
  - Sprache ist verdichtete Feld-Erfahrung.
  - Ein internes Zeichen ist ein komprimierter Wahrnehmungszustand.
- Menschliches Vergleichsbild:
  - Der Mensch sieht im Alltag nicht dauerhaft alle Details.
  - Er sieht zuerst eine komprimierte Bedeutung, z.B. Wand.
  - Erst bei Naehe, Relevanz, Abweichung oder Handlung wird die Wand detaillierter:
    rau, strukturiert, Riss, Material, Oberflaeche.
- Uebertragung auf den Bot:
  - Der Bot soll nicht jeden Marktpunkt tief analysieren.
  - Erst entsteht eine grobe eigene Form-/Feldbezeichnung.
  - Nur wenn Relevanz, Abweichung oder Handlungsnaehe entsteht,
    wird tiefer auf Struktur, Memory, Risiko und Feldklarheit gezoomt.
- Erwartete Wirkung:
  - weniger Denk-/Memory-Last
  - bessere Orientierung
  - weniger blindes Vergleichen ohne Support
  - mehr Varianz im Bedeutungsraum
  - Grundlage fuer emergente Musterfindung und kreative Reorganisation
- Dokumentiert in:
  - `README.md`: Abschnitt `Eigene Sprache und kognitive Kompression`
  - `files/UMSETZUNGSPLAN.md`: Abschnitte `Eigene Sprache als Feldverdichtung` und `Kognitive Kompression`

Naechster sinnvoller Anschluss nach dem aktuellen Debug-Fix:

- Erst neuen Lauf mit `structure_orientation_observe` und `mcm_form_symbol_protocol.csv` pruefen.
- Danach entscheiden, ob die Form-Zeichen nur diagnostisch bleiben oder als kognitive Entlastung in die Meta-Regulation einwirken.

Umgesetzt: diagnostischer Eigenzeichenraum / eigene Form-Sprache:

- Das Brain bildet jetzt pro Runtime-Tick ein internes Form-Zeichen:
  - `form_symbol_id`
  - `form_symbol_seen`
  - `form_symbol_maturity`
  - `form_symbol_stability`
  - `form_symbol_resonance`
  - `form_symbol_load_reduction`
  - `form_symbol_zoom_need`
  - `form_symbol_split_pressure`
  - `form_symbol_merge_pressure`
  - `form_symbol_bearing`
  - `form_symbol_fragility`
  - `form_symbol_relevance`
  - `form_symbol_novelty`
  - `form_symbol_distance`
- Quelle:
  - visuelle Marktform
  - Strukturwahrnehmung
  - Kontextvertrauen
  - Feldklarheit
  - Felddruck
  - Feldfragmentierung
- Wichtig:
  - Das ist bewusst kein menschliches Patternlabel.
  - Das Zeichen ist eine verdichtete Feld-/Form-Erfahrung des Systems.
  - Es wirkt aktuell diagnostisch und veraendert noch keine Tradeentscheidung.
- Neues Debug-Protokoll:
  - `debug/mcm_form_symbol_protocol.csv`
- Ziel der naechsten Auswertung:
  - Welche Zeichen entstehen wiederholt?
  - Werden sie stabiler oder fragmentierter?
  - Senkt Resonanz/Load-Reduction spaeter Denk-/Memory-Last?
  - Zeigt hoher `form_symbol_zoom_need`, wann das System tiefer sehen muss?
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\config.py`
