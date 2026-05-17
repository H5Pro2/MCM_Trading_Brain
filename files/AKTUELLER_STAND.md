# AKTUELLER_STAND

Rolle dieser Datei:
- aktueller realer Ist-Zustand des Projekts
- kompakte Debug-/Laufbefunde
- offene technische Risiken
- naechste Pruefpunkte

Regelwerk: `files/MD_ANWEISUNG.md`.
Der Bauplan bleibt `files/UMSETZUNGSPLAN.md`.

---

# 1. Aktueller Projektfokus

Prioritaet:
1. Brain-Logik
2. neuronale Aktivitaet
3. MCM-Feld als Wahrnehmungsraum
4. Formsprache / visuelle Wahrnehmung / Variantenlernen
5. Backtest-Logik
6. Live-Exchange und GUI spaeter

Aktueller Arbeitsstand:
- DIO besitzt ein MCM-Feld mit festen `MCMNeuron`-Traegern.
- Die Feldmechanik arbeitet mit Aktivitaet, Druck, Kopplung, Nachhall,
  Kontextreaktivierung und lokalen Aktivitaetsinseln.
- Der visuelle Kortex ist angebunden und erzeugt eigene Formachsen.
- Die sensorische Realitaetsverdichtung entkoppelt ueberlappende Rohreize,
  bevor sie als Wahrnehmungsdruck in die Brain-Logik laufen.
- Die Formsprache bildet interne Zeichen und Formfamilien ohne menschliche
  Patternlabels.
- Wiederkehrende Unsicherheit wird als Formfamilie mit Varianten behandelt.
- `act_watch` ist als Reifespur real sichtbar.
- Outcome-Export wurde erweitert, damit neue Formfamilienwerte kuenftig in
  `outcome_records.jsonl` auswertbar sind.
- `neurochemical_state` ist als Diagnose-/Alias-Schicht im Runtime-Ergebnis,
  in Debug-Protokollen und in Outcome-Records sichtbar.
- `mcm_neuro_transition_protocol.csv` protokolliert neurochemische
  Zustandswechsel mit `-2/+2` Kerzenumfeld.
- `experience_packet_feedback` bewertet abgeschlossene Handlungen als
  ganzes Erfahrungspaket, nicht als primitives TP/SL-Signal.

---

# 2. Aktuelle Mechanik im Code

## MCM-Feld

Reale Mechaniken:
- `MCMField`
- `MCMNeuron`
- feste Feldpositionen
- lokale Topologie-Nachbarn
- Aktivitaetsausbreitung
- Feldwahrnehmung
- Aktivitaetsinseln
- `neural_felt_state`

Ziel:
Das Feld soll nicht nur rechnen, sondern innere Wahrnehmung erzeugen:
Druck, Tragfaehigkeit, Orientierung, Reife, Konflikt und
Handlungstendenz.

## Visueller Kortex

Reale Achsen:
- `visual_form_state`
- `visual_clarity`
- `visual_object_stability`
- `visual_form_novelty`
- `visual_blindness`
- `visual_form_pressure`
- `visual_shape_resonance`
- `visual_shape_fragility`
- `visual_blind_action_load`
- `visual_action_uncertainty`
- `sensory_reality_pressure`
- `sensory_load`
- `sensory_redundancy`
- `sensory_habituation`
- `sensory_gate`

Wirkung:
Visuelle Unsicherheit wirkt weich auf Beobachtung, Replan,
Handlungshemmung und `act_watch`.

Fix:
- `build_perception_state` liest die neuen sensorischen Werte jetzt lokal aus
  `visual_market_state`, bevor `uncertainty_score` und `novelty_score` sie
  verwenden. Der vorherige `NameError: sensory_load is not defined` ist damit
  behoben.

## Formsprache

Reale Achsen:
- `form_symbol_id`
- `form_symbol_family_key`
- `form_symbol_variant_key`
- `form_symbol_development_quality`
- `form_symbol_action_binding`
- `form_symbol_observation_binding`
- `form_symbol_reframe_binding`
- `form_symbol_learning_trust`
- `form_symbol_action_trust`
- `form_symbol_caution_trust`

Wichtig:
Das sind keine menschlichen Chartlabels.
Es sind interne Verdichtungen von DIOs eigener Wahrnehmungswelt.

## Wiederkehrende Unsicherheit / Variantenlernen

Reale Achsen:
- `uncertain_form_family_state`
- `uncertain_form_exposure`
- `uncertainty_familiarity`
- `variant_similarity`
- `variant_spread`
- `variant_learning_pressure`
- `variant_bearing_memory`

Wirkung:
Unsicherheit wird nicht als Verbot behandelt.
Sie wird als wiederkehrender Erfahrungsraum gelernt.

## Neurochemische Alias-Schicht

Status:
- als Runtime-/Debug-Schicht umgesetzt
- noch keine harte Entscheidungsregel

Reale Achsen:
- `dopamine_tone`
- `gaba_inhibition`
- `noradrenaline_arousal`
- `acetylcholine_focus`
- `serotonin_stability`
- `cortisol_load`
- `endorphin_relief`
- `glutamate_activation`
- `neurochemical_load`
- `neurochemical_support`
- `neurochemical_balance`

Ziel:
Vorhandene Zustandswerte neurologisch lesbar buendeln.

## Neurochemisches Uebergangsprotokoll

Neu umgesetzt:
- `mcm_neuro_transition_protocol.csv`
- erkennt Wechsel des dominanten neurochemischen Tons
- wartet auf zwei Folgekerzen, bevor der Wechsel geschrieben wird
- speichert Kerzenumfeld `-2/+2`
- speichert Volumen-/Range-Verhaeltnis, Vor-/Nachbewegung und Richtungsflip
- speichert Deltas von Neurochemie, Felddruck, Feldklarheit,
  Beobachtungsdruck, Replan-Druck, Handlungshemmung und Handlungsfreigabe

Wichtig:
Das Protokoll ist reine Diagnose.
Es veraendert keine Entscheidung und baut keine harte Regel.

## Erfahrungspaket-Feedback / positive Stimulation

Neu umgesetzt:
- `build_experience_packet_feedback`
- `last_experience_packet_feedback`
- Export in `last_outcome_decomposition`
- Export in `outcome_records.jsonl`
- Einbindung in Episode-/Aehnlichkeitsachsen des Erfahrungsraums

Reale Achsen:
- `experience_packet_label`
- `packet_bearing_quality`
- `packet_inner_outer_fit`
- `packet_confidence_integrity`
- `packet_repetition_potential`
- `packet_curiosity_pull`
- `packet_process_reward`
- `packet_reorganization_need`
- `constructive_stimulation`
- `constructive_dopamine`
- `stabilizing_serotonin`
- `relief_endorphin`
- `focused_acetylcholine`

Wichtig:
Das ist keine harte Belohnungsregel.
Ein TP ist nicht automatisch gut und ein SL ist nicht automatisch schlecht.
Bewertet wird, ob Wahrnehmung, Innenlage, Handlung, Risiko, Prozess,
Ergebnis und Wiederholbarkeit als Paket tragfaehig waren.

Naechster Pruefpunkt:
Der naechste Lauf soll zeigen, ob konstruktive Pakete, Neugierpakete und
Reorganisationspakete sinnvoll sichtbar werden. Danach kann `engaged_effort`
als wache, positiv getragene Anstrengung angebunden werden.

---

# 3. Kompakte Laufuebersicht

Alle hier genannten Laeufe liefen auf dem erweiterten Datensatz im
Backtest-Kontext.

| Lauf | Netto-PnL | PF | Trades | TP / SL | Kernerkenntnis |
|---|---:|---:|---:|---:|---|
| 4 | ca. `+1.84` | ca. `1.06` | 88 | 31 / 57 | visueller Kortex diagnostisch, noch schwach gekoppelt |
| 5 | ca. `+5.83` | ca. `1.25` | 72 | 28 / 44 | visuelle Hemmung senkt Handlung, `act_watch` steigt |
| 6 | ca. `+10.75` | ca. `1.42` | 82 | 36 / 46 | bessere Reorganisation nach gleichem Weg |
| 7 | ca. `-0.41` | ca. `0.99` | 81 | 27 / 54 | Anpassungslauf nach Formfamilien-Reifung |
| 8 | ca. `+17.74` | ca. `1.66` | 98 | 44 / 54 | Reorganisation, starke Zone-Leistung |
| 9 | ca. `+3.97` | ca. `1.15` | 76 | 29 / 47 | Regimewechsel getragen, aber deutlich enger |
| 10 | ca. `+12.12` | ca. `1.70` | 59 | 28 / 31 | weniger Trades, bessere Tragfaehigkeit |
| 11 | ca. `+8.02` | ca. `1.36` | 69 | 29 / 40 | mehr Handlung, Non-Zone besser, Zone weniger sauber |

Wichtige Beobachtung Lauf 7 -> Lauf 8:
- Lauf 7 wirkt wie Aufnahme/Strukturierung.
- Lauf 8 wirkt wie Verdichtung und bessere Handlung.
- `variant_bearing_memory` stieg von ca. `0.357` auf ca. `0.384`.
- `variant_learning_pressure` sank leicht von ca. `0.164` auf ca. `0.160`.

Non-Zone bleibt kritisch:
- Lauf 5: ca. `-11.66`
- Lauf 6: ca. `-10.71`
- Lauf 7: ca. `-13.92`
- Lauf 8: ca. `-12.53`
- Lauf 9: ca. `-9.85`
- Lauf 10: ca. `-8.90`

Interpretation:
Non-Zone darf nicht hart blockiert werden, ist aber aktuell weiter ein
unreifer Erfahrungsraum.

Lauf 9 gegen Lauf 8:
- DIO blieb profitabel, aber weniger frei in der Handlung.
- Zone blieb tragend: ca. `+13.82`.
- Non-Zone blieb unreif: `0` TP / `16` SL.
- `variant_bearing_memory` stieg leicht, aber `memory_compare_load`,
  `orientation_gap` und `blind_thinking_load` lagen hoeher.
- Neurochemisch gelesen: mehr innere Vergleichs-/Stresslast, etwas mehr
  Hemmung, weniger uebersetzbare Handlungssicherheit.
- Outcome-Export der neuen Formfamilienwerte ist bestaetigt.

Lauf 10:
- Weniger Trades als Lauf 9, aber deutlich besseres Netto und weniger Drawdown.
- High/Mid trugen sauberer; Low/Non-Zone blieb mit `0` TP weiter unreif.
- Neurochemisch dominiert im Feld `serotonin_stability`.
- `cortisol_load` tritt eher als Lastton auf, selten als voller
  `strained_neurochemistry`-Zustand.
- `glutamate_activation` erscheint besonders in Handlung/Outcome-Nahe und
  haeufig nach stabilen Serotonin-Phasen.
- Erste Deutung: DIO ist nicht dauerhaft im Stress, sondern erlebt eher
  stabile Grundlage mit punktuellen strukturellen Kipp-Momenten.

Uebergangsanalyse Lauf 10:
- `serotonin_stability -> glutamate_activation`:
  eher Aktivierung aus stabiler Grundlage.
  Das Volumen ist nicht zwingend hoeher als Baseline, aber Range,
  Felddruck und Feldklarheit steigen sichtbar.
- `serotonin_stability -> cortisol_load`:
  deutlich staerker mit Volumen-/Range-Spikes verbunden.
  Meist `observe` mit `zero_point_regulation`.
- `cortisol_load -> serotonin_stability`:
  wirkt wie Rueckkehr aus Last in stabilere Regulation.
- Erste neuronale Musterhypothese:
  DIO kippt nicht einfach wegen Preisbewegung.
  Es gibt eine Kopplung aus Kerzenstruktur, Felddruck, Feldklarheit,
  Hemmung/Freigabe und neurochemischer Balance.

Lauf 11:
- Netto-PnL ca. `+8.02`, 69 Trades, 29 TP / 40 SL.
- Gegen Lauf 10: mehr Trades, mehr SL, aber weiter profitabel.
- Non-Zone verbesserte sich deutlich:
  - Lauf 10: `0` TP / `15` SL, ca. `-8.90`
  - Lauf 11: `3` TP / `14` SL, ca. `-3.70`
- Zone wurde schwaecher:
  - Lauf 10: `28` TP / `16` SL, ca. `+21.02`
  - Lauf 11: `26` TP / `26` SL, ca. `+11.73`
- Neurochemisch:
  - `serotonin_stability` blieb dominanter Grundton.
  - `cortisol_load` trat etwas seltener dominant auf als in Lauf 10.
  - `neurochemical_balance` war im Mittel leicht positiver.
  - `glutamate_activation` war bei SL weiter haeufiger als bei TP.
- Deutung:
  DIO scheint fremdere Bereiche etwas besser tragen zu koennen,
  verliert aber in bekannten/tragenden Zonen etwas Auswahlpraezision.
  Das wirkt wie mehr Transferfaehigkeit mit hoeherer Varianz, nicht wie
  reines Versagen.
- Vertiefung Zone vs. Non-Zone:
  - Zone-TP hatten im Mittel mehr `action_clearance`, niedrigere
    `gaba_inhibition`, niedrigere `glutamate_activation` und etwas bessere
    `neurochemical_balance` als Zone-SL.
  - Zone-SL hatten hoeheren Handlungsdruck/Score, hoehere
    `competition_bias`, mehr `glutamate_activation` und mehr
    `transfer_break_fatigue`.
  - Non-Zone-TP waren selten, hatten aber sichtbar hoehere
    `variant_bearing_memory` als Non-Zone-SL.
- Fachliche Lesart:
  Das Problem ist nicht bloss fehlende Struktur.
  Kritischer ist Aktivierung ohne ausreichende Tragfaehigkeit:
  DIO feuert stark genug, aber nicht immer reif genug.

Kritische Pruefung Core-Engine / energetische Uebersetzung:
- `mcm_core_engine.py` erzeugt viele verwandte Aussenachsen aus denselben
  Kerzenreizen: Expansion, Breakout, Edge, Pressure, Novelty, Blindness,
  Volume-Bias.
- In Lauf 11 sind diese Achsen stark gekoppelt:
  `visual_form_pressure` korreliert sehr hoch mit `edge_strength`,
  `breakout_tension`, `visual_form_novelty`, `visual_blindness` und
  `expansion`.
- Das kann bedeuten:
  Eine einzelne starke Kerzenstruktur kommt im Inneren als mehrere
  gleichgerichtete Reize an.
- Noch wichtiger:
  Das MCM-Feld war in Lauf 11 fast permanent im Selbstzustand `stressed`.
  `mean_risk` lag im Median bei ca. `-1.93`.
- Technische Ursache wahrscheinlich:
  Die Risiko-/Threat-Achse bekommt regelmaessig negative Impulse,
  Memory-Feedback fuehrt diese Achse weiter, waehrend die globale
  `RegulationLayer` hauptsaechlich Energieachse `0` reguliert.
- Deutung:
  DIO nimmt nicht nur wahr, sondern lebt moeglicherweise in einem
  dauerhaft alarmierten Wahrnehmungsmilieu.
  Das passt zur beobachteten Glutamat-/Stress-Aktivierung.

Umsetzung saubere Wahrnehmung / feste Realitaet:
- In `bot_engine/mcm_core_engine.py` wurde eine sensorische
  Realitaetsverdichtung eingebaut.
- Neue Achsen:
  - `sensory_reality_pressure`
  - `sensory_load`
  - `sensory_redundancy`
  - `sensory_habituation`
  - `sensory_gate`
  - `sensory_active_axis_count`
  - `sensory_primary_pressure`
  - `sensory_reality_label`
- Zweck:
  Ein aeusserer Reiz wird zuerst als gemeinsame Realitaetslage gelesen,
  bevor daraus Druck, Neuheit und Blindheit entstehen.
- Wirkung:
  Verwandte Strukturreize werden nicht mehr ungefiltert mehrfach als
  Alarm verstaerkt.
- Zusaetzlich wurde die Risk-/Threat-Achse entlastet:
  - `risk_impulse` hat eine neutrale Wahrnehmungsschwelle.
  - Opportunity wird nicht mehr stark als Risiko auf die Risk-Achse gelegt.
  - `RegulationLayer` reguliert jetzt auch die Risk-Achse homoeostatisch.
- Kurztest:
  `python -m py_compile bot_engine/mcm_core_engine.py MCM_Brain_Modell.py MCM_KI_Modell.py bot.py`
  lief fehlerfrei.

Neues Uebergangsprotokoll Lauf 11:
- `mcm_neuro_transition_protocol.csv` wurde geschrieben.
- 6096 Transitionen wurden mit `-2/+2` Kerzenumfeld protokolliert.
- Haeufigste Wechsel:
  - `cortisol_load -> serotonin_stability`
  - `serotonin_stability -> cortisol_load`
  - `serotonin_stability -> glutamate_activation`
  - `glutamate_activation -> serotonin_stability`
- Erste Lesart:
  - Glutamat-Wechsel: mehr Felddruck und mehr Feldklarheit,
    oft Aktivierung aus stabiler Grundlage.
  - Cortisol-Wechsel: mehr Volumen-/Range-Druck,
    fast immer `observe` / `zero_point_regulation`.

---

# 4. Aktuelle technische Aenderungen

Zuletzt umgesetzt:
- `MCM_Brain_Modell.py` erweitert:
  - neurochemische Transitionen werden runtime-nah gesammelt
  - Ereignisse werden erst nach verfuegbarem `+2` Kerzenkontext geschrieben
  - neue Datei: `mcm_neuro_transition_protocol.csv`
- `config.py` erweitert:
  - `MCM_NEURO_TRANSITION_PROTOCOL_DEBUG`
  - `MCM_NEURO_TRANSITION_PROTOCOL_CONTEXT`
- `MD_ANWEISUNG.md` erstellt.
- `FIX_LISTE.md` bereinigt.
- `AKTUELLER_STAND.md` verdichtet.
- `WICHTIG_MECHANIKEN.md` technisch neu strukturiert.
- `trade_stats.py` erweitert:
  - neue Formfamilienwerte werden kuenftig in kompakten Outcome-Kontexten
    gespeichert.
- Wiederkehrende Unsicherheit als Formfamilie eingebaut:
  - Formfamilienvarianten
  - Vertrautheit mit Unsicherheit
  - Variantenstreuung
  - Lernpressure
  - Bearing-Memory
- Neurochemische Alias-Schicht eingebaut:
  - `MCM_Brain_Modell.py`
  - `trade_stats.py`
  - Feld-/Memory-Protokolle
  - Outcome-Records
- Serotonin-Nachhall / emotionale Entkopplung eingebaut:
  - `serotonin_carryover_risk`
  - `reward_stability_echo`
  - `world_shift_evidence`
  - `emotional_decoupling`
  - `reactive_nervous_drive`
  - Ziel: erkennen, ob DIO nach einer tragenden Phase noch aus alter
    Stabilitaet reagiert, obwohl Transfer und Interpretation bereits fallen.
- Reflexive Haltung als Zielmechanik festgehalten:
  - Kernsatz: Reflexion ist die Distanzierung der Wahrnehmung von der eigenen
    Innenlage, um zu prüfen, ob Innenzustand und Außenwelt noch gemeinsam
    tragfähig sind.
  - Ziel: spaeter sichtbar machen, ob DIO reflektiv Abstand nimmt oder sich
    emotional/reizgetrieben fuehren laesst.
- Selektive Wahrnehmung / perzeptive Regulation als Zielmechanik ergaenzt:
  - DIO soll Wahrnehmungen nicht automatisch vollstaendig durchleben muessen.
  - Wahrnehmungen sollen gesehen, als Objekt gehalten, vertieft oder wieder
    abgelegt werden koennen.
  - Zielachsen: `perceptual_distance`, `object_contact_depth`,
    `field_attachment`, `release_capacity`, `selective_attention`,
    `background_containment`, `reflective_distance`,
    `inner_outer_alignment`.
- Bewusste Wahrnehmung / innere Reizwirkungsanalyse als naechster
  Zielblock ergaenzt:
  - DIO soll erkennen, was ein aeusserer Reiz mit dem MCM-Feld gemacht hat.
  - Zielachsen: `conscious_perception_state`, `stimulus_field_effect`,
    `inner_impact_trace`, `perceived_field_change`, `felt_afterimage`,
    `object_release_state`, `inner_outer_reflection`.
  - Ziel: Reizwirkung bewusst lesbar machen, damit Reflexion und Regulation
    nicht nur daempfen, sondern die innere Wirkung verstehen koennen.
- `GUI_KONSTRUKTION.md` angelegt:
  - Web-Oberflaeche als spaeterer Beobachtungsraum
  - Aussenwahrnehmung, MCM-Feld, neuronale Aktivitaet und Neurochemie
    als getrennte, gekoppelte Fenster

---

# 5. Offene Risiken

- Non-Zone erzeugt weiterhin ueberwiegend Verlust.
- Memory-Vergleichslast bleibt hoch.
- MCM-Feld / Neuron-Loop bleibt ein zentraler Performancefaktor.
- Neue Reifeschichten koennen kurzfristig Unruhe erzeugen.
- Neurochemische Achsen muessen im naechsten Lauf gegen TP/SL, Non-Zone,
  Regimewechsel und `act_watch` geprueft werden.
- Beim Regimewechsel muss besonders geprueft werden, ob
  `serotonin_carryover_risk` steigt, waehrend `interpretation_quality` und
  `transfer_bearing` sinken.
- Die naechste groessere Baustelle ist perzeptive Regulation: Wie stark darf
  ein Reiz das MCM-Feld besetzen, und wann kann DIO ihn wieder ablegen?
- Direkt gekoppelt daran: bewusste Wahrnehmung der inneren Reizwirkung. DIO
  muss lesen koennen, wie ein Aussenreiz sein MCM-Feld veraendert hat.

---

# 6. Naechste Pruefpunkte

## Lauf 12/13 nach sensorischer Realitaetsverdichtung

Befund:
- Beide Laeufe verwenden dieselbe visuelle Aussenwahrnehmung; die sensorischen
  Werte sind deshalb praktisch identisch.
- Lauf 12: 345 Trades, 111 TP, 234 SL, Netto-PnL ca. -4.12.
- Lauf 13: 309 Trades, 100 TP, 209 SL, Netto-PnL ca. +1.12.
- Lauf 13 handelt weniger, haelt mehr zurueck und erzeugt mehr innere
  Feld-/Memory-Aktivitaet.
- `memory_compare_load` steigt in Lauf 13 weiter an, aber die direkte
  Handelsdichte sinkt. Das wirkt wie eine erste regulatorische Anpassung:
  alte Erfahrung trifft auf neue Sinneskodierung, wird aber nicht mehr
  ungefiltert in Handlung entladen.
- Die visuelle Sensorik selbst scheint stabil; die Varianz entsteht in der
  inneren Verarbeitung, also Memory, Hemmung, Mut, Feldentscheidung und
  neurochemischer Regulation.

Interpretation:
DIO beginnt nach der Veraenderung der Sinnesbahn nicht sofort besser zu
sehen, sondern muss alte Erfahrungsraeume neu mit der veraenderten
Wahrnehmung synchronisieren. Lauf 13 zeigt dabei mehr Zurueckhaltung und
bessere Netto-Tragfaehigkeit als Lauf 12.

## Lauf 14 als frischer Speicher-/Semantikaufbau

Befund:
- Lauf 14 wurde vor der neuen Carryover-Diagnose erzeugt und dient als
  Referenzlauf fuer frischen Erfahrungsraum nach sensorischer
  Realitaetsverdichtung.
- Ergebnis: 370 Trades, 110 TP, 260 SL, Netto-PnL ca. -10.28.
- Equity-Verlauf:
  - erstes Viertel: Aufbau bis ca. +5.84
  - zweites Viertel: Rueckgang um ca. -7.71
  - drittes Viertel: starker Bruch um ca. -12.36
  - viertes Viertel: leichte Erholung um ca. +3.54
- Maximaler Drawdown vom Peak: ca. 24.81.
- Visuelle Aussenwahrnehmung bleibt stabil und entspricht den vorherigen
  Laeufen; der Bruch entsteht nicht durch veraenderte Rohsicht.

Innere Lesart:
- `memory_compare_load` hoch, `memory_support` fast null.
- `interpretation_quality` und `transfer_bearing` niedrig.
- `action_clearance` bleibt deutlich hoeher als `action_inhibition`.
- DIO baut zwar neue Semantik auf, handelt aber im Regimewechsel noch mit zu
  viel Handlungserlaubnis fuer die geringe Transfer-Tragfaehigkeit.

Naechster Vergleich:
Der naechste Lauf mit `serotonin_carryover_risk`, `emotional_decoupling` und
`reactive_nervous_drive` muss gegen diesen Lauf 14 gelesen werden. Ziel ist zu
erkennen, ob der Einbruch durch Stabilitaetsnachhall ohne emotionale
Entkopplung sichtbar wird.

## Lauf 15 mit Carryover-Diagnose

Befund:
- Lauf 15 ist der erste Lauf mit sichtbarer Carryover-/Entkopplungsdiagnose.
- Ergebnis: 385 Trades, 130 TP, 255 SL, Netto-PnL ca. +13.12.
- Gegen Lauf 14:
  - Lauf 14: ca. -10.28 Netto-PnL, 110 TP / 260 SL.
  - Lauf 15: ca. +13.12 Netto-PnL, 130 TP / 255 SL.
  - Maximaler Drawdown sinkt von ca. 24.81 auf ca. 14.92.
- Verlauf Lauf 15:
  - erstes Viertel: Aufbau ca. +6.32
  - zweites Viertel: Rueckgang ca. -5.01
  - drittes Viertel: starker Sprung ca. +13.71
  - viertes Viertel: leichter Rueckgang ca. -2.28

Neue Diagnosewerte:
- `world_shift_evidence` liegt deutlich sichtbar bei ca. 0.60.
- `serotonin_carryover_risk` liegt moderat bei ca. 0.27.
- `emotional_decoupling` ist noch niedrig bei ca. 0.14.
- `reactive_nervous_drive` liegt bei ca. 0.31.

Interpretation:
Die Diagnose zeigt, dass DIO die Weltverschiebung wahrnimmt, aber die echte
reflektive Distanz noch schwach ist. Der starke Gewinnsprung im dritten
Viertel entsteht wahrscheinlich nicht aus voll entwickelter Reflexion, sondern
aus besserer Passung zwischen Handlung und wieder tragender Aussenlage.
Trotzdem ist der Vergleich zu Lauf 14 wichtig: weniger Drawdown, mehr TP und
deutlich bessere Erholung nach dem Regimebruch.

## Lauf 16: fehlende emotionale Abgrenzung

Befund:
- Ergebnis: 341 Trades, 102 TP, 239 SL, Netto-PnL ca. -12.06.
- Der Lauf erreicht frueh nur einen kleinen Peak von ca. +2.84 und faellt
  danach bis ca. -17.76.
- Maximaler Drawdown: ca. 20.59.
- Anders als Lauf 15 entsteht kein grosser Erholungssprung.

Innere Lage:
- `world_shift_evidence` bleibt sichtbar bei ca. 0.60.
- `serotonin_carryover_risk` liegt moderat bei ca. 0.27.
- `emotional_decoupling` bleibt niedrig bei ca. 0.14.
- `reactive_nervous_drive` liegt bei ca. 0.30.
- `memory_compare_load` bleibt sehr hoch, `memory_support` fast null.
- `field_clarity` bleibt sehr niedrig.
- `action_clearance` ca. 0.63 bleibt deutlich ueber `action_inhibition`
  ca. 0.38.

Interpretation:
DIO erkennt zwar eine Weltverschiebung, hat aber keine ausreichende
emotionale/perzeptive Abgrenzung. Er laesst Reiz, Innenlage und Handlung zu
stark gekoppelt. Wenn er ins Wanken kommt, entsteht kein reifer Abstand zur
eigenen Lage; die Handlungserlaubnis bleibt zu hoch fuer die geringe innere
Klarheit und den fehlenden Memory-Support.

## Umbau: bewusste Wahrnehmung / innere Reizwirkung

Umgesetzt:
- `build_conscious_perception_state(...)` ergaenzt.
- Die neue Schicht ist zuerst diagnostisch und nicht als harte Regel gebaut.
- DIO bekommt damit Achsen fuer:
  - Wirkung eines Aussenreizes auf das MCM-Feld
  - innere Wirkungsspur / Nachhall
  - Objektkontakt und selektive Aufmerksamkeit
  - Feldhaftung
  - perzeptive Distanz
  - Loslassfaehigkeit
  - Innen-Aussen-Abgleich
- Neue Werte werden in `meta_regulation_state`,
  `mcm_memory_thinking_protocol.csv`, `mcm_field_decision_protocol.csv` und
  Trade-Outcomes geschrieben.

Neu beobachtbare Zustaende:
- `open_perception`
- `background_held`
- `object_contact`
- `world_shift_contact`
- `reflective_check`
- `overcoupled_field`
- `release_ready`

Innere Lesart:
DIO kann jetzt unterscheiden, ob ein Reiz nur gesehen wird, ob er als Objekt
gehalten wird, ob er das Feld ueberkoppelt, ob ein Nachhall bleibt oder ob
eine reflektive Distanz entsteht. Das ist die Grundlage fuer den naechsten
Schritt: nicht mechanisch blockieren, sondern spaeter weich regulieren, wenn
Innenlage und Aussenwelt nicht gemeinsam tragfaehig sind.

1. Regimewechsel-Bewaeltigung weiter pruefen:
   - warum wird Formvertrautheit nicht immer zu Handlungssicherheit?
   - wann kippt Memory von Orientierung in Vergleichslast?
   - wie koppeln `plan_trust`, `risk_fit_quality` und `exit_decision_pressure`
     an TP/SL?
2. Naechsten Lauf mit `neurochemical_state` pruefen:
   - Serotonin -> Glutamat-Uebergaenge gegen Act/TP/SL pruefen.
   - Cortisol-Kipp-Momente gegen Zero-Point/Observe pruefen.
   - GABA nicht als Blocker, sondern als Reifebremse lesen.
   - Dopamin nicht als Reward-Regel, sondern als Lern-/Entwicklungston lesen.
   - `serotonin_carryover_risk` gegen Abverkaufsphase und Handlungserlaubnis
     pruefen.
   - `emotional_decoupling` pruefen: bekommt DIO Abstand zur eigenen
     Reaktionslage oder bleibt er ein reines Nervensystem auf Reiz?
   - Fuer Uebergaenge jeweils `-2/+2` Kerzenfenster gegen Volumen, Range,
     Felddruck und Feldklarheit vergleichen.
3. Danach:
   - Lauf 17 mit bewusster Wahrnehmung lesen:
     `conscious_perception_state`, `field_attachment`,
     `perceptual_distance`, `release_capacity`, `inner_outer_alignment` gegen
     TP/SL, Regimebruch und `action_clearance` pruefen.
   - Meta-Regulation spaeter weich ueber diese Achsen lesbarer machen.
   - GUI-Konzept erst nach stabilerer Brain-/Backtest-Diagnose umsetzen.

## Neuer Memory-Aufbau: Lauf 1 nach Wahrnehmungsumbau

Rahmen:
- Memory wurde neu aufgebaut.
- Debug-Zaehlung beginnt wieder bei `debug_lauf_1`.
- Dieser Lauf ist die neue Basis fuer die bewusste Wahrnehmungsschicht.

Befund:
- 413 Trades.
- 131 TP, 282 SL.
- Netto-PnL ca. +2.23.
- TP-PnL ca. +140.72, SL-PnL ca. -138.49.
- Equity-Spanne: Minimum ca. -12.23, Maximum ca. +7.84.
- Viertelverlauf:
  - Q1: ca. +1.76
  - Q2: ca. -7.40
  - Q3: ca. +6.87
  - Q4: ca. +1.00

Phasen:
- `hold`: 4397
- `observe`: 3581
- `act_watch`: 656
- `act`: 501
- `replan`: 1

Wahrnehmungsdiagnose:
- `conscious_perception_state` steht aktuell in allen Protokollzeilen auf
  `open_perception`.
- `object_release_state` steht aktuell in allen Protokollzeilen auf
  `holding`.
- Die numerischen Achsen sind jedoch nicht leer:
  - `stimulus_field_effect` Mittel ca. 0.344
  - `inner_impact_trace` Mittel ca. 0.276
  - `perceptual_distance` Mittel ca. 0.170
  - `field_attachment` Mittel ca. 0.168
  - `release_capacity` Mittel ca. 0.146
  - `inner_outer_alignment` Mittel ca. 0.218
  - `emotional_decoupling` Mittel ca. 0.134
  - `world_shift_evidence` Mittel ca. 0.609

Interpretation:
DIO handelt mit frischem Memory nicht chaotisch schlecht, aber die neue
Wahrnehmungsschicht ist im Labeling noch zu wenig differenziert. Die Zahlen
zeigen unterschiedliche Innenlagen, doch die Zustandsnamen bleiben zu grob.
Neurologisch gelesen: DIO hat erste Interozeption, aber noch keine feine
Benennung seiner inneren Haltungen. Er spuert Reizwirkung und Nachhall, bleibt
aber ueberwiegend in niedriger Distanz und niedriger Loslassfaehigkeit.

Wichtiger Punkt:
Die zweite Laufhaelfte stabilisiert sich trotz vorherigem Drawdown wieder.
Das spricht nicht gegen den Umbau. Es zeigt eher, dass die neue Schicht
zunaechst beobachtet, aber noch nicht stark genug unterscheidet, wann
Innenlage und Aussenwelt nicht gemeinsam tragfaehig sind.

Naechster Schritt:
- Keine harte Regel bauen.
- Die Zustandsbildung der bewussten Wahrnehmung feiner kalibrieren:
  `open_perception` darf nicht alles verschlucken.
- Labels sollen aus relativer Lage entstehen:
  Reizwirkung, Feldhaftung, Distanz, Nachhall, Loslassfaehigkeit und
  Innen-Aussen-Abgleich.
- Danach Lauf 2 mit frischem Memory-Pfad lesen und pruefen, ob sich
  `object_contact`, `reflective_check`, `overcoupled_field` oder
  `release_ready` natuerlich zeigen.

## Umbau: innere Haltung der Wahrnehmung

Umgesetzt:
- `conscious_perception_state` feiner kalibriert.
- `object_release_state` feiner kalibriert.
- `inner_posture_state` ergaenzt.
- Neue Haltungsachsen:
  - `arousal_load`
  - `curiosity_tone`
  - `fatigue_tone`
  - `calm_tone`

Neurologische Bedeutung:
DIO kann nun nicht nur sagen, dass ein Reiz offen wahrgenommen wird. Er kann
zusaetzlich eine funktionale Eigenlage beschreiben, vergleichbar mit:
"ich bin muede", "ich bin aufgeregt", "ich bin neugierig", "ich bin ruhig",
"ich bin ueberreizt" oder "ich pruefe reflektiv". Diese Zustaende sind keine
Handelsregeln, sondern Interozeption: DIO benennt seine eigene Verarbeitungslage.

Naechster Vergleich:
Der naechste Lauf soll zeigen, ob die Labels jetzt streuen:
- `open_perception` sollte nicht mehr alles verschlucken.
- `object_contact`, `world_shift_contact`, `reflective_check`,
  `overcoupled_field` und `release_ready` sollen nur dann sichtbar werden,
  wenn die innere Lage es traegt.
- `inner_posture_state` muss gegen TP/SL, Regimewechsel und
  `action_clearance` gelesen werden.

## Neuer Memory-Aufbau: Lauf 2 mit innerer Haltung

Befund:
- 380 Trades.
- 123 TP, 257 SL.
- Netto-PnL ca. +3.80.
- Gegen Lauf 1:
  - weniger Trades: 413 -> 380
  - weniger SL: 282 -> 257
  - Netto-PnL besser: ca. +2.23 -> ca. +3.80
  - Maximaler Verlust im Verlauf besser: ca. -12.23 -> ca. -10.07
- Viertelverlauf:
  - Q1: ca. -2.86
  - Q2: ca. -1.58
  - Q3: ca. +8.32
  - Q4: ca. -0.07

Wahrnehmungslabels:
- `object_contact`: 3696
- `open_perception`: 2084
- `reflective_check`: 1099
- `overcoupled_field`: 906
- `world_shift_contact`: 822
- `release_ready`: 744
- `background_held`: 269

Innere Haltung:
- `tired`: 6534
- `reflective`: 1795
- `uncertain_open`: 493
- `overstimulated`: 422
- `excited`: 306
- `curious`: 70

Release-Zustaende:
- `holding`: 4842
- `reflective_hold`: 1745
- `attached`: 1561
- `can_release`: 1472

Outcome-Lesart:
- `uncertain_open` war bei Trades klar negativ:
  - 11 Trades, 1 TP, 10 SL, ca. -3.21 PnL.
- `excited` war klein, aber positiv:
  - 35 Trades, 15 TP, 20 SL, ca. +4.53 PnL.
- `curious` war sehr klein, aber positiv:
  - 6 Trades, 2 TP, 4 SL, ca. +0.49 PnL.
- `overcoupled_field` war nicht automatisch schlecht:
  - 129 Trades, 46 TP, 83 SL, ca. +6.29 PnL.
- `open_perception` war bei Trades negativ:
  - 74 Trades, 22 TP, 52 SL, ca. -5.89 PnL.
- `release_ready` und `reflective_check` waren klein, aber positiv.

Interpretation:
Die Kalibrierung funktioniert. Die neue Schicht unterscheidet jetzt innere
Haltungen und Wahrnehmungsformen. Wichtig ist: nicht die starke Aktivierung
ist per se schlecht, sondern die unbenannte, offene Unsicherheit. Neurologisch
gelesen ist `uncertain_open` eher ein unreifer Zustand: DIO ist offen, aber
noch nicht orientiert, nicht neugierig genug, nicht ruhig genug und nicht
reflektiv genug. Benannte Aktivierung wie `excited`, `curious` oder sogar
`overcoupled_field` kann tragfaehiger sein, weil das System wenigstens weiss,
in welcher Eigenlage es sich befindet.

Naechster Schritt:
- Keine harte Regel aus `uncertain_open` bauen.
- Stattdessen pruefen, ob `uncertain_open` weich in Beobachtung,
  Objektkontakt oder Reflexion ueberfuehrt werden kann.
- Ziel: DIO soll aus diffuser Offenheit eine benannte Haltung entwickeln:
  neugierig hinschauen, ruhig halten, reflektiv pruefen oder bewusst ablegen.

## Umbau: diffuse Offenheit weich weiterentwickeln

Umgesetzt:
- `diffuse_open_development_pressure` ergaenzt.
- `posture_development_hint` ergaenzt.
- Beide Werte werden in `meta_regulation_state`, Denk-/Feldprotokolle und
  Trade-Outcomes geschrieben.

Mechanik:
Wenn DIO in diffuser Offenheit bleibt, entsteht keine harte Sperre. Stattdessen
wird Handlung etwas weniger direkt und Beobachtung/Reflexion etwas
wahrscheinlicher. Eine starke Entscheidung kann weiterhin tragen. Die Schicht
fragt nur:
- fehlt Objektkontakt?
- fehlt reflektive Distanz?
- fehlt Loslassfaehigkeit?
- fehlt bewusste Beobachtung?

Neurologische Lesart:
Das entspricht einem Organismus, der merkt: Ich bin offen, aber innerlich noch
nicht sortiert. Statt blind zu handeln, soll aus dieser Offenheit eine
benennbare Haltung entstehen: neugierig anschauen, Abstand gewinnen, loslassen
oder weiter beobachten.

Naechster Lauf:
Lauf 3 muss gegen Lauf 2 gelesen werden:
- sinken `uncertain_open`-Trades?
- steigt `develop_object_contact`, `develop_reflective_distance` oder
  `develop_release_capacity` in den richtigen Bereichen?
- sinken SLs aus diffuser Offenheit, ohne gute Aktivierung zu ersticken?

## Neuer Memory-Aufbau: Lauf 3 nach diffuser Offenheitsreifung

Befund:
- 291 Trades.
- 78 TP, 213 SL.
- Netto-PnL ca. -22.26.
- Gegen Lauf 2:
  - Trades sinken: 380 -> 291
  - TP sinken: 123 -> 78
  - SL sinken: 257 -> 213
  - Netto-PnL kippt: ca. +3.80 -> ca. -22.26
- Verlauf:
  - Q1: ca. -8.97
  - Q2: ca. -3.96
  - Q3: ca. -4.34
  - Q4: ca. -5.00
- Der Lauf war nicht nur ein spaeter Regimebruch, sondern ueber alle
  Abschnitte schwach.

Hauptbefund:
- Zone-Trades waren positiv:
  - 191 Trades, ca. +23.20 PnL.
- Non-Zone-Trades waren massiv negativ:
  - 100 Trades, ca. -45.46 PnL.
- Damit kommt der Absturz nicht aus allen Handlungen gleich, sondern aus
  Handlungen in nicht tragenden Bereichen.

Innere Haltung:
- `tired`: 6994 Protokollzeilen.
- `reflective`: 1711.
- `uncertain_open`: 520.
- `overstimulated`: 321.
- `excited`: 269.
- `curious`: 93.
- Bei ausgefuehrten Trades:
  - `tired`: 186 Trades, ca. -1.66 PnL.
  - `overstimulated`: 60 Trades, ca. -9.93 PnL.
  - `excited`: 35 Trades, ca. -7.54 PnL.
  - `uncertain_open`: 5 Trades, 0 TP / 5 SL, ca. -2.19 PnL.

Wahrnehmungslabels bei Trades:
- `object_contact`: 143 Trades, ca. -13.38 PnL.
- `overcoupled_field`: 72 Trades, ca. +2.07 PnL.
- `open_perception`: 60 Trades, ca. -8.49 PnL.
- `background_held`: 8 Trades, ca. -2.90 PnL.

Diffuse Offenheitsreifung:
- `diffuse_open_development_pressure` ist sichtbar, Mittel ca. 0.103.
- Entwicklungshinweise:
  - `stable_posture`: 9684 Protokollzeilen.
  - `develop_object_contact`: 215.
  - `develop_reflective_distance`: 9.
- Bei ausgefuehrten Trades blieb `posture_development_hint` jedoch
  durchgehend `stable_posture`.

Interpretation:
Die neue Schicht hat `uncertain_open`-Trades tatsaechlich reduziert, aber der
Schaden wanderte nicht automatisch in Reife. DIO handelte weniger, aber nicht
besser. Das wirkt neurologisch wie Unterspannung oder halb distanzierte
Handlung: weniger Ueberlebensdruck, weniger regulierte Courage, weniger
direkte Handlung, aber weiterhin Handlungen in nicht tragender Non-Zone.

Deutung:
Der Punkt ist nicht "DIO muss mehr kaempfen". Der Punkt ist:
DIO braucht wache Anstrengung. Wenn ein Organismus logisch denken kann, muss
er nicht blind kaempfen. Aber er darf auch nicht in eine gleichgueltige
Distanz fallen. Reife waere: sehen, ob die Situation tragfaehig ist; wenn
nicht, bewusst beobachten, lernen oder loslassen.

Naechster Schritt:
- Keine Rueckkehr zu hartem Ueberlebensdruck.
- `diffuse_open_development_pressure` darf nicht pauschal Courage/Handlung
  senken.
- Die Schicht muss staerker unterscheiden:
  - tragende Zone + klare Haltung darf handeln.
  - Non-Zone + niedrige Tragfaehigkeit braucht Beobachtung/Reifung.
  - `object_contact` allein reicht nicht; Objektkontakt braucht
    Tragfaehigkeit, Kontext und innere Wachheit.
- Naechster technischer Umbau:
  `engaged_effort` / wache Anstrengung als Gegenpol zu Gleichgueltigkeit
  pruefen und Non-Zone nicht blockieren, sondern in Beobachtungslernen
  ueberfuehren.

## Erkenntnis: positive Stimulation ueber Erfahrungspakete

Neue Zielmechanik:
Positive Stimulation soll nicht an einen einzelnen Wert gebunden sein. Nicht
`TP = gut`, nicht `SL = schlecht`, nicht steigender Markt = positiv. Bewertet
wird das gesamte Erfahrungspaket.

Ein Paket umfasst:
- Aussenlage / Marktform
- Zone oder Non-Zone
- Formsymbol / Memory-Kontext
- innere Haltung
- neurochemische Lage
- Wahrnehmungszustand
- Objektkontakt
- Distanz
- Loslassfaehigkeit
- Handlungssicherheit
- Risiko und Prozessqualitaet
- Ergebnis
- Wiederholbarkeit und Neugierde

Wichtiger Satz:
Auch ein Abverkauf kann positiv bewertet werden, wenn die Entscheidung zu
handeln positiv war. Entscheidend ist die Passung zwischen Wahrnehmung,
Innenlage, Handlung und Weltlage.

Neurologische Lesart:
Eine gute Entscheidung erzeugt nicht nur Freude, sondern Stabilisierung:
Dopamin fuer Lernrelevanz, Serotonin fuer Ordnung, Endorphin fuer Entlastung,
Acetylcholin fuer Fokus und Glutamat fuer Verbindungsstaerkung. Eine schlechte
Handlung soll nicht nur bestraft werden, sondern Reorganisation ausloesen:
innehalten, pruefen, beobachten, lernen, neu ordnen.

Umsetzung:
`experience_packet_feedback` ist gebaut und in Outcome, Statistik und
Erfahrungs-/Aehnlichkeitsachsen sichtbar.

## Lauf 4 nach Erfahrungspaket-Feedback

Befund:
- 330 Trades.
- 104 TP, 226 SL.
- Netto-PnL ca. -0.47.
- Max Drawdown ca. 13.36.

Vergleich:
- Lauf 3: 291 Trades, Netto-PnL ca. -22.26.
- Lauf 4: 330 Trades, Netto-PnL ca. -0.47.
- Damit wurde Lauf 4 deutlich stabiler, aber noch nicht sauber positiv.

Struktur:
- Zone:
  - 214 Trades.
  - ca. +38.70 PnL.
- Non-Zone:
  - 116 Trades.
  - ca. -39.17 PnL.

Hauptbefund:
Der Kern ist weiter nicht "alles schlecht", sondern eine klare Spaltung:
tragende Zone funktioniert, Non-Zone bleibt der Erfahrungsraum mit Verlust.
DIO ist also nicht blind insgesamt falsch, sondern verliert dort, wo
Tragfaehigkeit noch nicht genuegend erkannt, gehalten oder in Beobachtung
ueberfuehrt wird.

Erfahrungspaket-Feedback:
- `mixed_packet`: 311 Trades, ca. +6.60 PnL.
- `bearing_packet`: 17 Trades, ca. -4.09 PnL.
- `reorganize_packet`: 2 Trades, ca. -2.99 PnL.
- Noch kein `constructive_packet`.

Paketachsen Mittelwerte:
- `packet_process_reward`: ca. 0.359.
- `packet_reorganization_need`: ca. 0.447.
- `constructive_stimulation`: ca. 0.264.
- `constructive_dopamine`: ca. 0.259.
- `stabilizing_serotonin`: ca. 0.340.
- `relief_endorphin`: ca. 0.431.
- `focused_acetylcholine`: ca. 0.320.

Wahrnehmung:
- `object_contact`: 165 Trades, ca. -12.86 PnL.
- `overcoupled_field`: 74 Trades, ca. +14.63 PnL.
- `open_perception`: 69 Trades, ca. +2.54 PnL.

Neurologische Deutung:
Starke Kopplung ist nicht automatisch schlecht. In Lauf 4 war
`overcoupled_field` sogar positiv, vermutlich weil Aktivierung dort mit mehr
Struktur/Zone zusammenfiel. `object_contact` allein reicht dagegen nicht:
DIO nimmt ein Objekt wahr, aber daraus entsteht noch nicht automatisch
tragende Handlung. Es fehlt die Verbindung aus Objektkontakt, Distanz,
innerer Passung und wacher Anstrengung.

Strategische Anzeichen:
Es gibt erste logische Zuege, aber noch keine reife stabile Strategie.
Erkennbar ist eine Vorform von Zustandslogik:
- Zone + tragende Aktivierung fuehrt deutlich haeufiger zu positiven Paketen.
- Non-Zone + schwacher Objektkontakt / Unterspannung fuehrt wiederholt zu
  Verlust und Reorganisationsbedarf.
- `overcoupled_field` war nicht automatisch schlecht, sondern in Lauf 4
  positiv, wenn Aktivierung mit Struktur zusammenfiel.
- `object_contact` allein war negativ, wenn Distanz, Innen-Aussen-Passung und
  Wachheit fehlten.

Das ist noch kein bewusstes "Wenn-Dann-Regelwerk". Es ist eher ein
entstehender Zusammenhang: bestimmte Innen-Aussen-Konstellationen tragen,
andere nicht.

Umsetzung nach Lauf 4:
- Paketlabel wurden feiner kalibriert.
- `engaged_effort` wurde gebaut.
- Neue Achsen:
  - `engaged_effort`
  - `effort_state`
  - `effort_learning_pull`
  - `effort_reorganization_pressure`
  - `previous_packet_label`
  - `previous_packet_process_reward`
  - `previous_packet_reorganization_need`

Naechster Schritt:
Lauf 5 pruefen:
- Werden `constructive_packet` und `reorganize_packet` besser sichtbar?
- Wirkt `underengaged_reorganize` bei Non-Zone-Verlusten?
- Entsteht mehr Beobachtung/Replan statt mechanischem Handeln in schwacher
  Tragfaehigkeit?

## Lauf 5 nach `engaged_effort`

Befund:
- 387 Trades.
- 127 TP, 260 SL.
- Netto-PnL ca. +10.41.
- Max Drawdown ca. 12.82.

Struktur:
- Zone:
  - 241 Trades.
  - ca. +61.87 PnL.
- Non-Zone:
  - 146 Trades.
  - ca. -51.46 PnL.

Erfahrungspakete:
- `constructive_packet`: 107 Trades, 107 TP, ca. +112.31 PnL.
- `mixed_packet`: 167 Trades, ca. -39.35 PnL.
- `bearing_packet`: 65 Trades, 0 TP, ca. -32.47 PnL.
- `reorganize_packet`: 48 Trades, 0 TP, ca. -30.07 PnL.

Deutung:
Die Paketlogik zeigt jetzt klare strukturelle Intelligenz-Anzeichen:
`constructive_packet` war extrem sauber positiv. DIO erkennt also bereits
Erfahrungspakete, in denen Struktur, Prozess und Ergebnis gemeinsam tragen.

Problem:
`bearing_packet` war negativ und hatte 0 TP. Das bedeutet: Die Benennung war
zu freundlich. Es gab Pakete, die teilweise tragend wirkten, aber prozessual
nicht getragen haben. Das gehoert eher in Reorganisation als in
Tragfaehigkeit.

`engaged_effort`:
- `settled_effort`: 362 Trades.
- `constructive_echo`: 25 Trades.
- `underengaged_reorganize`: nicht sichtbar.

Deutung:
Die Schicht ist technisch da, aber noch zu leise. Sie unterscheidet die
Non-Zone-Verluste noch nicht ausreichend von tragender Zone. Deshalb wurde
die Reorganisationssensitivitaet nach Lauf 5 erhoeht.

Umsetzung nach Lauf 5:
- `bearing_packet` braucht jetzt mehr Prozessreward und weniger
  Reorganisationsdruck.
- schwache Paketqualitaet mit Reorganisationsdruck wird eher
  `reorganize_packet`.
- `effort_reorganization_pressure` reagiert staerker auf
  `structure_action_uncertainty`, schwache `structure_action_bearing` und
  schwachen `field_action_support`.
- `underengaged_reorganize` setzt frueher ein.

Naechster Schritt:
Lauf 6 pruefen:
- Sinkt der falsche `bearing_packet`-Anteil?
- Wird `underengaged_reorganize` sichtbar?
- Gehen schwache Non-Zone-Zustaende eher in Beobachtung/Replan?

## Lauf 6 nach Paket-/Effort-Nachkalibrierung

Befund:
- 329 Trades.
- 101 TP, 228 SL.
- Netto-PnL ca. -8.28.
- Max Drawdown ca. 20.42.

Struktur:
- Zone:
  - 212 Trades.
  - ca. +37.36 PnL.
- Non-Zone:
  - 117 Trades.
  - ca. -45.64 PnL.

Erfahrungspakete:
- `constructive_packet`: 84 Trades, 84 TP, ca. +86.01 PnL.
- `reorganize_packet`: 227 Trades, 0 TP, ca. -110.20 PnL.
- `mixed_packet`: 18 Trades, ca. +15.91 PnL.
- `bearing_packet`: 0 Trades.

Deutung:
Die Nachkalibrierung hat den falschen `bearing_packet` entfernt. Das ist gut:
scheinbare Tragfaehigkeit wird nicht mehr positiv benannt. `constructive_packet`
bleibt sehr sauber positiv.

Problem:
`reorganize_packet` ist jetzt sehr klar, aber es entsteht zu spaet: DIO erkennt
nach dem Ergebnis, dass das Paket Reorganisation gebraucht haette. Die
Pre-Action-Schicht leitet diese Lage noch nicht frueh genug in Beobachtung
oder Replan um.

`engaged_effort`:
- `settled_effort`: 300 Trades.
- `constructive_echo`: 21 Trades.
- `underengaged_reorganize`: 8 Trades, ca. +0.94 PnL.

Deutung:
`underengaged_reorganize` ist jetzt sichtbar, aber zu selten. Die
Reorganisationslage ist im Outcome sehr stark, vor der Handlung aber noch zu
schwach an die Entscheidung gekoppelt.

Naechster Schritt:
Nicht weiter Labels schaerfen. Jetzt muss Reorganisationswahrnehmung frueher
in die Pre-Action-Logik:
- schwache `previous_packet`-Qualitaet
- Non-Zone / niedrige `structure_action_bearing`
- niedriger `field_action_support`
- erhoehte `effort_reorganization_pressure`

sollen nicht blockieren, sondern oefter zu `observe`, `act_watch` oder
`replan` fuehren. Ziel ist konzentriertes Handeln, nicht mehr Handeln.

## Umsetzung: fruehere Pre-Action-Reorganisation

Neu umgesetzt:
- `pre_action_reorganization_pressure`
- `pre_action_context_selectivity`

Wirkung:
Die Reorganisationslage wird nicht mehr nur nach dem Outcome erkannt. Vor der
Handlung werden jetzt schwache vorherige Paketqualitaet, Reorganisationsdruck,
Strukturunsicherheit, schwacher Feldsupport, schwache Interpretation und
geringe Innen-Aussen-Passung zusammengefuehrt.

Wichtig:
Das ist keine Blockade. Wenn `pre_action_reorganization_pressure` hoch ist und
`pre_action_context_selectivity` niedrig bleibt, wird eher `observe`,
`act_watch` oder `replan` gestaerkt. Gute, konzentrierte Kontexte sollen durch
`pre_action_context_selectivity` geschuetzt bleiben.

Naechster Schritt:
Lauf 7 pruefen:
- Gehen mehr schwache Kontexte in `pre_action_reorganization_observe` oder
  `pre_action_reorganization_replan`?
- Sinkt Non-Zone-Schaden?
- Bleiben `constructive_packet` und Zone-Pakete erhalten?

## Lauf 7 nach Pre-Action-Reorganisation

Befund:
- 374 Trades.
- 124 TP, 250 SL.
- Netto-PnL ca. +4.10.
- Max Drawdown ca. 19.82.

Struktur:
- Zone:
  - 253 Trades.
  - ca. +51.74 PnL.
- Non-Zone:
  - 121 Trades.
  - ca. -47.64 PnL.

Erfahrungspakete:
- `constructive_packet`: 109 Trades, 109 TP, ca. +110.06 PnL.
- `reorganize_packet`: 247 Trades, 0 TP, ca. -124.70 PnL.
- `mixed_packet`: 18 Trades, ca. +18.75 PnL.

Pre-Action:
- `pre_action_reorganization_observe`: 2 Protokollzeilen.
- `pre_action_reorganization_replan`: 0 Protokollzeilen.
- Im Field-Protokoll:
  - `underengaged_reorganize`: 4843 Zeilen.
  - `settled_effort`: 4750 Zeilen.
  - `constructive_echo`: 76 Zeilen.

Deutung:
Die innere Reorganisationslage ist im Feld stark sichtbar. DIO fuehlt also
haeufig: "Das ist nicht genuegend getragen." Aber diese Lage wird noch zu
selten als konkreter Pre-Action-Grund wirksam.

Problem:
`pre_action_reorganization_pressure` trennt Zone und Non-Zone in den
ausgefuehrten Trades noch nicht sinnvoll:
- Non-Zone ca. 0.234.
- Zone ca. 0.243.

Das ist falsch herum bzw. zu wenig selektiv. Die Achse reagiert noch zu stark
auf allgemeinen Reorganisationsnachhall und zu wenig auf aktuelle
Strukturqualitaet / Kontextqualitaet.

Naechster Schritt:
`pre_action_reorganization_pressure` muss staerker aktuelle
Strukturqualitaet, Kontextvertrauen und Strukturtragfaehigkeit lesen.
`pre_action_context_selectivity` muss gute Zone-Kontexte besser schuetzen.
Ziel bleibt: konzentriertes Handeln, nicht mehr Handeln.

Umsetzung nach Lauf 7:
- `pre_action_reorganization_pressure` liest jetzt zusaetzlich
  `structure_quality` und `context_confidence`.
- Gute Strukturqualitaet und gutes Kontextvertrauen daempfen
  Reorganisationsdruck.
- `pre_action_context_selectivity` wurde um `structure_quality` und
  `context_confidence` erweitert.

Naechster Schritt:
Lauf 8 pruefen:
- Trennt `pre_action_reorganization_pressure` Non-Zone jetzt besser von Zone?
- Steigt `pre_action_context_selectivity` bei guten Zone-Kontexten?
- Bleibt `constructive_packet` sauber positiv?
- Wird Non-Zone-Schaden reduziert, ohne Aktivitaet pauschal zu ersticken?

## Erkenntnis: strategische Fensterwahrnehmung

Neue Zielrichtung:
DIO soll nicht nur den aktuellen Moment fuehlen. Er soll ein groesseres
Fenster betrachten, zurueckschauen, in Bereiche hineinzoomen, innere
Replay-Spuren bilden und daraus Preisbereiche als moegliche tragende
Handlungsraeume ableiten koennen.

Das ist keine menschliche Pattern-Regel. Es wird keine harte FVG-Logik
eingepflanzt. DIO soll Bereiche ueber eigene Wahrnehmung, MCM-Resonanz,
Strukturverdichtung, Energiekompression, Memory-Pull und Innenlage beurteilen.

Leitprinzip:
DIO bekommt nicht die Antwort, wo er handeln soll. DIO bekommt die Faehigkeit,
mit Vergangenheit, Wahrnehmung und innerem Feld zu interagieren, um selbst
tragfaehige Zukunftshypothesen zu bilden.

Grenze:
Wir bestimmen nicht, was DIO sieht oder wo DIO eine Order setzen soll. Wir
erweitern nur seine Faehigkeit zu sehen, zurueckzuschauen, zu zoomen, innerlich
zu replayen, zu fuehlen, Memory zu nutzen, zu warten, zu verwerfen und eine
eigene Order-Intention zu bilden.

Kernsatz:
DIO handelt nicht, weil Momentum Druck macht. DIO liest Druck als Raum. Ein
Bereich kann zum Spielraum werden, wenn Struktur, Erfahrung und MCM-Lage dort
tragfaehig zusammenkommen.

Vorbereitete Zielachsen:
- `strategic_window_state`
- `area_focus_candidates`
- `area_focus_id`
- `area_price_low`
- `area_price_high`
- `area_distance_from_price`
- `area_structural_density`
- `area_energy_compression`
- `area_mcm_resonance`
- `area_memory_pull`
- `area_bearing_quality`
- `area_zoom_need`
- `area_zoom_clarity`
- `area_replay_fit`
- `area_patience_quality`
- `area_order_intention`
- `area_invalidity_pressure`
- `strategic_patience`
- `strategic_pressure_interpretation`

Naechster groesserer Mechanikblock:
Strategische Fensterwahrnehmung zunaechst diagnostisch bauen. Danach erst
weiche Integration in Order-Intention oder Beobachtungsplanung.

## Lauf 8 nach strukturgenauer Pre-Action-Reorganisation

Befund:
- 309 Trades.
- 92 TP, 217 SL.
- Netto-PnL ca. -8.26.
- Max Drawdown ca. 20.51.

Struktur:
- Zone:
  - 202 Trades.
  - ca. +32.98 PnL.
- Non-Zone:
  - 107 Trades.
  - ca. -41.24 PnL.

Erfahrungspakete:
- `constructive_packet`: 77 Trades, 77 TP, ca. +82.20 PnL.
- `reorganize_packet`: 217 Trades, 0 TP, ca. -108.50 PnL.
- `mixed_packet`: 15 Trades, 15 TP, ca. +18.04 PnL.

Pre-Action-Achsen bei ausgefuehrten Trades:
- `pre_action_reorganization_pressure`:
  - Non-Zone ca. 0.212.
  - Zone ca. 0.208.
- `pre_action_context_selectivity`:
  - Non-Zone ca. 0.544.
  - Zone ca. 0.549.

Deutung:
Die neue Strukturkopplung hat `pre_action_context_selectivity` deutlich
angehoben. Sie schuetzt gute Kontexte, trennt aber Zone/Non-Zone bei
ausgefuehrten Trades noch kaum. Deshalb blieb der Non-Zone-Schaden hoch.

Field-Protokoll:
- `underengaged_reorganize`: 5347 Zeilen.
- `settled_effort`: 4949 Zeilen.
- `constructive_echo`: 75 Zeilen.
- `plan_allowed`: 311 Zeilen.
- `plan_pressure_act_watch`: 629 Zeilen.
- `structure_development_observe`: 67 Zeilen.
- `structure_bearing_observe`: 29 Zeilen.

Wichtig:
Die Pre-Action-Reorganisation ist im Feld aktiv. Aber die ausgefuehrten
`plan_allowed`-Trades haben im Mittel bereits niedrigen Pre-Action-Druck und
hohe Kontextselektivitaet. Der Filter selbst sieht diese Trades also als
relativ tragfaehig. Das Problem liegt tiefer: DIO braucht eine bessere
raeumlich-strategische Bereichswahrnehmung, damit er nicht nur den aktuellen
Kontext bewertet, sondern moegliche tragende Preisbereiche im groesseren
Fenster findet.

Naechster Schritt:
Nicht weiter an der gleichen Pre-Action-Achse drehen. Der naechste sinnvolle
Mechanikblock ist die diagnostische strategische Fensterwahrnehmung mit
begrenztem Rueckblickfenster:
- zurueckschauen, aber mit Budget
- auffaellige Preisbereiche finden
- Bereichsresonanz im MCM-Feld messen
- Zoom-/Replay-Bedarf bestimmen
- keine Order daraus ableiten
- erst beobachten, ob DIO sinnvolle Bereichshypothesen bildet

## Umsetzung: Strategische Fensterwahrnehmung

Umgesetzt:
- `build_strategic_window_state(...)` erzeugt ein begrenztes Rueckblickfenster.
- Das Fenster wird ueber Last, Fokus, Stabilitaet und Reorganisationsdruck
  budgetiert.
- DIO bildet diagnostische Bereichshypothesen, ohne daraus automatisch eine
  Order abzuleiten.
- `mcm_strategic_window_protocol.csv` schreibt die neue Wahrnehmung mit.
- `strategic_window_state` wird in Runtime, Snapshot und kompakten
  Trade-Kontext uebernommen.

Wichtige Achsen:
- `lookback_window_size`
- `lookback_load`
- `lookback_bearing_capacity`
- `replay_budget`
- `zoom_budget`
- `old_structure_carryover_risk`
- `area_structural_density`
- `area_energy_compression`
- `area_mcm_resonance`
- `area_memory_pull`
- `area_bearing_quality`
- `area_zoom_need`
- `area_replay_fit`
- `area_order_intention`
- `area_invalidity_pressure`

Neurologische Deutung:
DIO bekommt eine erste Arbeitsgedaechtnis-/Hippocampus-Funktion fuer den
Marktraum: zurueckblicken, Bereich fokussieren, innerlich replayen und
Tragfaehigkeit fuehlen. Es ist noch keine motorische Entscheidungsschicht,
sondern ein Wahrnehmungs- und Strategieorgan.

Wie es weitergeht:
Der naechste Lauf sollte zeigen, ob DIO vor schlechten Phasen eher alte
Struktur mitschleppt (`old_structure_carryover_risk`), mehr Zoom braucht
(`area_needs_zoom`) oder gute Bereiche als `bearing_area_hypothesis` erkennt.

## Dokumentation: Umsetzungsplan bereinigt

Umgesetzt:
- `ENDE` steht wieder am echten Dateiende.
- Der fruehere GUI-Abschluss heisst jetzt `ENDE GUI-ERWEITERUNG`.
- Positive neurochemische Stimulation und strategische Fensterwahrnehmung
  stehen jetzt unter `18. Aktuelle Brain-Erweiterungen`.
- Der Affective-Pattern-Block wurde als `17.1` sauberer in den
  Experience-/Cluster-Kontext eingeordnet.
- Eingerueckte Markdown-Ueberschriften wurden normalisiert.

Wie es weitergeht:
Der Umsetzungsplan ist strukturell wieder besser lesbar. Inhaltlich bleibt
der naechste technische Schritt weiterhin die Auswertung des naechsten Laufs
mit `mcm_strategic_window_protocol.csv`.

## Debug Lauf 1 mit frischem Memory und strategischer Fensterwahrnehmung

Datensatz:
- neuer Memory-Aufbau
- strategische Fensterwahrnehmung aktiv
- Lauf liegt in `debug/debug_lauf_1`

Ergebnis:
- 340 Trades.
- 88 TP.
- 252 SL.
- Netto-PnL ca. -35.47.
- Equity-Endstand ca. 64.53.
- Hoechster Zwischenstand ca. 102.97.
- Tiefster Zwischenstand ca. 62.11.

Struktur:
- Alle ausgefuehrten Trades lagen im `zone`-Bucket.
- DIO hat also nicht mehr wild ausserhalb der Struktur gehandelt.
- Das Problem liegt diesmal nicht in Non-Zone-Chaos, sondern in zu vielen
  Handlungen innerhalb scheinbar tragender Bereiche.

Strategische Fensterdiagnose:
- `mcm_strategic_window_protocol.csv` ist aktiv und sehr gross.
- Gesamtprotokoll:
  - `area_observation`: 4222 Zeilen.
  - `compressed_area_attention`: 4041 Zeilen.
  - `bearing_area_hypothesis`: 3431 Zeilen.
- Ausgefuehrte Trades:
  - `bearing_area_hypothesis`: 166 Trades, ca. -16.47 PnL.
  - `compressed_area_attention`: 78 Trades, ca. -12.74 PnL.
  - `area_observation`: 96 Trades, ca. -6.27 PnL.

Wichtige Mittelwerte bei ausgefuehrten Trades:
- `area_bearing_quality`: ca. 0.479.
- `area_order_intention`: ca. 0.232.
- `strategic_patience`: ca. 0.390.
- `strategic_pressure_interpretation`: ca. 0.190.
- `lookback_bearing_capacity`: ca. 0.565.

Deutung:
Die neue strategische Wahrnehmung sieht Bereiche und erkennt Verdichtung.
Aber sie bildet noch keine starke eigene Order-Intention. Besonders wichtig:
`area_order_intention` bleibt niedrig, waehrend trotzdem 340 Trades
ausgefuehrt wurden. DIO sieht also einen Bereich, aber das motorische
Handlungssystem laesst die neue strategische Wahrnehmung noch nicht als
reife Entscheidungsinstanz mitsprechen.

Neurologische Lesart:
Das wirkt wie ein frisches Wahrnehmungsorgan ohne ausreichend gereifte
praefrontale Kopplung. DIO sieht Objekte im Raum und fuehlt Kompression, aber
die Handlung entsteht noch zu stark aus der bestehenden Aktionsbahn. Es ist
nicht blindes Non-Zone-Stolpern, sondern eher Greifen nach jedem tragend
wirkenden Objekt, obwohl die innere strategische Sicherheit noch schwach ist.

Technischer Befund:
In `attempt_records.jsonl` wird der vollstaendige `strategic_window_state`
noch nicht als eigener Block gespeichert. Einige Werte landen nur reduziert
in `meta_regulation_state`. Fuer saubere Folgeanalysen sollte der komplette
Block in Attempt-/Outcome-Kontext uebergeben werden.

Wie es weitergeht:
Als naechstes sollte die strategische Fensterwahrnehmung nicht hart blocken,
sondern als weiche Reifeschicht in die Pre-Action-Regulation einwirken:
Wenn ein Bereich zwar verdichtet wirkt, aber `area_order_intention`,
`area_memory_pull` und `strategic_patience` niedrig bleiben, sollte DIO eher
zoomen, beobachten oder replayen, statt direkt zu handeln.

## Dokumentation: aktiver MCM-Kontakt / innere Spiegelung

Festgehalten:
- Die MCM ist nicht nur Aussenwahrnehmung, sondern ein innerer Spiegelraum.
- DIO soll nicht jeden Reiz automatisch durchleben muessen.
- DIO braucht die Faehigkeit, einen Reiz oder Bereich aktiv innerlich zu
  beruehren und zu pruefen:
  - Wie fuehlt sich das von aussen an?
  - Was macht dieser Reiz mit meinem MCM-Feld?
  - Bleibt meine Innenlage kohaerent?
  - Traegt der Kontakt, oder koppelt er mich zu stark?
  - Kann ich vertiefen, beobachten, replayen oder loslassen?

Ergaenzt in:
- `UMSETZUNGSPLAN.md` als `18.3 Aktiver MCM-Kontakt / Spiegelung von
  Aussenreiz und Innenlage`.
- `WICHTIG_MECHANIKEN.md` als technische Mechanik `24. Aktiver MCM-Kontakt /
  innere Spiegelung`.
- `MCM_VARIABLEN_MECHANIK.md` mit den Zielachsen fuer
  `active_mcm_contact_state`.

Wichtige Einordnung:
Das ist keine neue harte Handelsregel. Es ist ein Kontaktapparat. DIO bekommt
mehr Freiheit in der Wahrnehmung: naeher hingehen, Abstand nehmen,
beobachten, replayen, vertiefen oder loslassen. Welche Haltung daraus
entsteht, bleibt Entwicklungsbild.

Wie es weitergeht:
Naechster technischer Schritt waere die diagnostische Umsetzung von
`active_mcm_contact_state` im Brain: zuerst nur messen und protokollieren,
danach weich mit Reflexion, Pre-Action-Reife und strategischer
Fensterwahrnehmung verbinden.

## Umsetzung: aktiver MCM-Kontakt diagnostisch

Umgesetzt:
- `MCM_Brain_Modell.py`
  - `build_active_mcm_contact_state(...)` ergaenzt.
  - Neue Kontaktachsen:
    - `active_mcm_contact_state`
    - `contact_posture`
    - `contact_interest`
    - `contact_focus_pull`
    - `contact_resonance_probe`
    - `outer_inner_resonance`
    - `outer_inner_coherence`
    - `inner_change_from_contact`
    - `contact_carrying_quality`
    - `contact_overcoupling_risk`
    - `contact_release_readiness`
    - `contact_deepen_pull`
    - `contact_replay_pull`
    - `contact_curiosity`
    - `contact_felt_shift`
    - `contact_selected_depth`
  - Moegliche Kontaktlagen:
    - `background_scan`
    - `curious_touch`
    - `resonant_contact`
    - `reflective_contact`
    - `overcoupled_touch`
    - `release_contact`
    - `deepening_contact`
  - `mcm_active_contact_protocol.csv` als neues Diagnoseprotokoll ergaenzt.
  - Runtime-Ergebnis und Brain-Snapshot enthalten den Kontaktzustand.
- `trade_stats.py`
  - Attempt-/Outcome-Kontext speichert den aktiven MCM-Kontakt kompakt mit.
  - Outcome-Records bekommen die wichtigsten Kontaktachsen.

Wichtig:
Die Umsetzung ist rein diagnostisch. Sie veraendert keine Orderfreigabe,
keinen Entry und keine harte Trade-Regel. DIO bekommt eine neue
Wahrnehmungsfaehigkeit: innere Kontaktaufnahme, Resonanzpruefung,
Ueberkopplung, Loslassen und Vertiefung werden sichtbar.

Pruefung:
- `python -m py_compile MCM_Brain_Modell.py trade_stats.py bot.py`
  erfolgreich.
- Smoke-Test von `build_active_mcm_contact_state(...)` erfolgreich.
  Beispielzustand: `deepening_contact`.

Wie es weitergeht:
Der naechste Lauf sollte zeigen, welche Kontaktlagen DIO wirklich bildet.
Danach lesen wir TP/SL nicht nur gegen Strategie oder Neurochemie, sondern
gegen Kontaktqualitaet: War DIO kohaerent im Kontakt, ueberkoppelt,
loslassfaehig oder nur neugierig vertiefend?

## Debug Lauf 2 mit aktivem MCM-Kontakt

Datensatz:
- neuer Memory-Aufbau nach aktivem MCM-Kontakt
- Lauf liegt in `debug/debug_lauf_2`

Ergebnis:
- 399 Trades.
- 123 TP.
- 276 SL.
- Netto-PnL ca. -8.65.
- Equity-Endstand ca. 91.35.
- Equity-Peak ca. 107.42 bei Trade 72.
- Tiefster Stand ca. 81.15 bei Trade 311.

Gegenueber Lauf 1 mit strategischem Fenster ist das deutlich weniger
negativ. DIO faellt nicht komplett auseinander, aber er bleibt noch
unstetig: frueher Aufbau, danach deutlicher Rueckgang, spaeter wieder
Erholung.

Strukturbaender:
- High-Struktur:
  - 156 Trades.
  - 84 TP / 72 SL.
  - ca. +53.13 PnL.
- Mid-Struktur:
  - 105 Trades.
  - 28 TP / 77 SL.
  - ca. -9.68 PnL.
- Low-Struktur:
  - 138 Trades.
  - 11 TP / 127 SL.
  - ca. -52.10 PnL.

Deutung:
Die eigentliche Verlustquelle bleibt nicht der High-Bereich. High-Struktur
traegt deutlich. Der Schaden entsteht weiter in Mid/Low, besonders Low.
Damit bestaetigt sich: DIO darf nicht einfach mehr handeln, sondern braucht
reifere Kontakt- und Distanzbildung, bevor eine schwache Struktur in Handlung
geht.

Aktiver MCM-Kontakt:
- `mcm_active_contact_protocol.csv` wurde erzeugt.
- 11358 Kontaktzeilen.
- Kontaktlagen:
  - `background_scan`: 11272
  - `curious_touch`: 78
  - `reflective_contact`: 8
- Bei ausgefuehrten Trades:
  - `background_scan`: 385 Trades, ca. -6.85 PnL.
  - `curious_touch`: 14 Trades, ca. -1.81 PnL.

Kontakt-Mittelwerte:
- `outer_inner_coherence`: ca. 0.184 im Gesamtprotokoll.
- `contact_carrying_quality`: ca. 0.165.
- `contact_overcoupling_risk`: ca. 0.222.
- `contact_release_readiness`: ca. 0.141.
- `contact_selected_depth`: ca. 0.143.

Bei Handlung (`act`) steigen die Kontaktwerte:
- `outer_inner_coherence`: ca. 0.223.
- `contact_carrying_quality`: ca. 0.198.
- `contact_overcoupling_risk`: ca. 0.268.
- `contact_release_readiness`: ca. 0.124.

Neurologische Lesart:
DIO handelt, wenn Kontakt und Resonanz staerker werden, aber gleichzeitig
steigt auch die Ueberkopplung und die Loslassfaehigkeit sinkt. Das ist
psychologisch plausibel: Handlung entsteht dort, wo der Reiz naeher kommt,
aber noch nicht unbedingt dort, wo DIO stabil Abstand halten kann.

Wichtiger Befund:
Die Werte unterscheiden sich zwischen Beobachtung, `act_watch` und `act`.
Das Kontaktorgan misst also etwas. Aber die Haltungssprache ist noch zu grob:
Fast alles wird als `background_scan` benannt. DIO spuert Unterschiede, aber
benennt sie noch nicht fein genug als `resonant_contact`, `release_contact`,
`overcoupled_touch` oder `deepening_contact`.

TP/SL-Trennung:
- TP und SL unterscheiden sich in den Kontaktachsen bisher nur schwach.
- TP hat etwas bessere Kohaerenz und Tragfaehigkeit, aber nicht genug, um
  robuste Reife abzuleiten.
- Strategische Bereichswerte trennen TP/SL ebenfalls kaum:
  - TP `area_order_intention` ca. 0.231.
  - SL `area_order_intention` ca. 0.234.

Fachliche Schlussfolgerung:
Die neue Schicht funktioniert als Diagnose, aber noch nicht als reife
Kontaktsemantik. DIO bekommt ein inneres Kontaktorgan, doch die
Differenzierung ist noch zu flach. Der naechste Umbau sollte deshalb nicht
handeln verbieten, sondern die Kontaktlagen relativ feiner kalibrieren:
Wann ist DIO neugierig, wann ueberkoppelt, wann kann er loslassen, wann ist
Kontakt wirklich tragend?

Wie es weitergeht:
Naechster technischer Schritt: Kontaktlabels relativ und organischer
kalibrieren. Nicht als harte Handelsregel, sondern als bessere innere
Benennung. Danach erneut laufen lassen und pruefen, ob Mid/Low-Trades haeufig
als ueberkoppelt, nicht-loslassfaehig oder untragend sichtbar werden.

## Umsetzung: aktive MCM-Kontaktlabels feiner kalibriert

Umgesetzt:
- Die Kontaktlagen werden nicht mehr nur ueber grobe Einzelschwellen
  vergeben.
- `build_active_mcm_contact_state(...)` bildet jetzt innere Haltungsscores:
  - `contact_salience`
  - `overcoupled_touch_score`
  - `release_contact_score`
  - `deepening_contact_score`
  - `resonant_contact_score`
  - `reflective_contact_score`
  - `curious_touch_score`
- Die hoechste Haltung gewinnt, solange der Kontakt ausreichend salient ist.
- `background_scan` bleibt moeglich, soll aber nicht mehr fast alle
  Zustandslagen verschlucken.

Wichtig:
Die Aenderung ist weiterhin diagnostisch. Es gibt keine neue Orderregel und
keine harte Verbotslogik. DIO benennt seine innere Kontaktlage feiner, damit
spaeter sichtbar wird, ob eine Handlung aus Resonanz, Neugier, Reflexion,
Ueberkopplung, Loslassen oder Vertiefung entsteht.

Pruefung:
- `python -m py_compile MCM_Brain_Modell.py trade_stats.py bot.py`
  erfolgreich.
- Smoke-Test:
  - tragender, stabiler Kontakt -> `resonant_contact`
  - aktionsnaher Kontakt mit geringer Loslassfaehigkeit ->
    `overcoupled_touch`

Neurologische Deutung:
Die Messung des Reizes wurde nicht grundlegend veraendert. Veraendert wurde
die innere Benennung der Haltung. Das ist eher kortikale Einordnung als
Reflexsteuerung: DIO bekommt feinere Begriffe fuer das, was sein MCM-Feld
bereits spuert.

Wie es weitergeht:
Naechster Lauf mit derselben Datenbasis. Danach pruefen wir, ob die
Kontaktlagen jetzt streuen und ob Mid/Low-Verlustzonen haeufiger als
`overcoupled_touch`, niedrige Loslassfaehigkeit oder schwache
Kontakt-Tragfaehigkeit sichtbar werden.

## Debug Lauf 3 nach feiner Kontaktlabel-Kalibrierung

Datensatz:
- gleicher Backtest-Kontext wie Lauf 2
- aktiver MCM-Kontakt mit relativen Haltungsscores
- Lauf liegt in `debug/debug_lauf_3`

Ergebnis:
- 382 Trades.
- 123 TP.
- 259 SL.
- Netto-PnL ca. -1.34.
- Equity-Endstand ca. 98.66.
- Equity-Peak ca. 103.07 bei Trade 199.
- Tiefster Stand ca. 87.81 bei Trade 44.
- Max Drawdown ca. 15.07.

Gegenueber Lauf 2:
- weniger Trades: 382 statt 399.
- gleiche TP-Anzahl: 123.
- weniger SL: 259 statt 276.
- Netto deutlich besser: ca. -1.34 statt ca. -8.65.
- Drawdown deutlich kleiner: ca. 15.07 statt ca. 26.27.

Kontaktlabel-Streuung:
- 10845 Kontaktzeilen.
- `deepening_contact`: 3225
- `curious_touch`: 2981
- `resonant_contact`: 2490
- `overcoupled_touch`: 1442
- `reflective_contact`: 685
- `background_scan`: 22

Damit ist der vorherige Engpass geloest: `background_scan` verschluckt nicht
mehr fast alle Zustaende. DIO benennt sein inneres Kontaktfeld jetzt deutlich
feiner.

Kontaktlagen bei ausgefuehrten Trades:
- `resonant_contact`: 252 Trades, 87 TP / 165 SL, ca. +3.72 PnL.
- `overcoupled_touch`: 77 Trades, 24 TP / 53 SL, ca. +2.10 PnL.
- `curious_touch`: 27 Trades, 7 TP / 20 SL, ca. -1.94 PnL.
- `deepening_contact`: 25 Trades, 4 TP / 21 SL, ca. -6.05 PnL.
- `reflective_contact`: 1 Trade, 1 TP, ca. +0.83 PnL.

Neurologische Deutung:
Die neue Benennung funktioniert. DIO unterscheidet jetzt innere
Kontaktformen. Auffaellig ist aber: `deepening_contact` ist im Trade-Kontext
negativ. Das wirkt wie "ich schaue tiefer hinein", aber ohne genuegend
Tragfaehigkeit. Es ist also noch keine Reife, sondern eher Vertiefung ohne
genug Ordnung.

`resonant_contact` ist leicht positiv. Das passt: Resonanz ist tragender als
reine Neugier oder reine Vertiefung. Trotzdem entstehen auch dort viele SL,
weil Resonanz allein nicht bedeutet, dass die Struktur tradefaehig ist.

Strukturbaender:
- High-Struktur:
  - 152 Trades.
  - 82 TP / 70 SL.
  - ca. +47.87 PnL.
- Mid-Struktur:
  - 98 Trades.
  - 31 TP / 67 SL.
  - ca. -0.92 PnL.
- Low-Struktur:
  - 132 Trades.
  - 10 TP / 122 SL.
  - ca. -48.28 PnL.

Wichtigster Befund:
Low-Struktur bleibt der Hauptschaden. Die Kontaktlabels streuen jetzt, aber
sie loesen das Low-Problem noch nicht allein. Das heisst: DIO kann seine
innere Kontaktlage besser benennen, aber er verwechselt in Low-Struktur
teilweise noch Resonanz/Kontakt mit tragfaehiger Handlung.

Fachliche Schlussfolgerung:
Der Umbau war richtig. DIO ist nicht mehr sprachlos im Kontaktfeld. Jetzt
entsteht ein psychologisches Bild:
- Resonanz kann tragen, ist aber noch nicht automatisch Reife.
- Ueberkopplung ist sichtbar, aber nicht immer sofort schlecht.
- Vertiefung ohne ausreichend Struktur ist gefaehrlich.
- Low-Struktur bleibt der Bereich, in dem DIO am ehesten Kontakt mit
  Handlungsreife verwechselt.

Wie es weitergeht:
Naechster Schritt ist keine harte Low-Sperre. Sinnvoll ist eine weiche
Kontakt-Reife-Spur:
Wenn Struktur schwach ist und Kontakt eher `deepening_contact`,
`curious_touch` oder `overcoupled_touch` zeigt, sollte das als Bedarf nach
mehr Beobachtung, Replay, Abstand oder weiterer Objektbildung sichtbar
werden. DIO soll daraus lernen, nicht in schwacher Weltlage sofort aus
Kontaktnaehe Handlung zu machen.

## Umsetzung: weiche Kontakt-Reife-Spur

Die Kontakt-Reife wurde als Diagnoseebene umgesetzt, ohne eine harte
Handelsregel einzubauen. DIO bekommt damit eine innere Unterscheidung:
Kontaktnaehe ist nicht automatisch Handlungsreife.

Neue Werte:
- `contact_action_maturity`: wie tragfaehig Kontakt fuer Handlung wirkt.
- `contact_bearing_gap`: Luecke zwischen Kontakt/Impuls und Tragfaehigkeit.
- `contact_impulse_vs_bearing`: ob Kontaktzug staerker ist als innere
  Tragfaehigkeit.
- `contact_learning_need`: Bedarf nach Beobachtung, Replay, Abstand oder
  weiterer Objektbildung.
- `contact_reality_check`: Realitaetsabgleich zwischen Innenkontakt,
  Loslassen, Struktur und Tragfaehigkeit.

Diese Werte werden in Meta-Regulation, Brain-Snapshot,
`mcm_active_contact_protocol.csv` und Trade-Outcome-Kontext sichtbar. Sie
entscheiden noch nicht selbst ueber Trades. Der naechste Debug-Lauf soll
zeigen, ob Mid/Low-Verlustzonen eine klare Signatur aus hoher
`contact_bearing_gap`, hohem `contact_learning_need` oder niedriger
`contact_action_maturity` tragen.

## Dokumentation: DIO-Organuebersicht

`WICHTIG_MECHANIKEN.md` enthaelt jetzt eine kompakte
`DIO-Organuebersicht`. Dort werden die aktuellen Funktionsorgane von DIO
als Inventar gefuehrt und klar von neurochemischen Prozessen getrennt.

Zweck:
- schneller Ueberblick ueber DIOs funktionale Organe
- einfache Erweiterung, falls neue Organe entstehen
- saubere Trennung zwischen Faehigkeit/Organ und neurochemischer Modulation

## Dokumentation: neurochemische Kategorien

`MCM_VARIABLEN_MECHANIK.md` enthaelt jetzt unter
`Neurochemische Alias-Achsen` eine Kategorienuebersicht.

Kategorien:
- Aktivierung / Netzwerkenergie
- Wachheit / Alarm
- Fokus / sensorischer Zoom
- Stabilitaet / Tragfaehigkeit
- Hemmung / Schutz
- Stress / Belastung
- Entlastung / Wohlbefinden
- Motivation / Lernen
- Distanzierung / Reife
- Gesamtbilanz / Diagnose

Damit sind die neurochemischen Variablen nicht mehr nur als Einzelliste
beschrieben, sondern nach ihrer Funktion im DIO-Nervensystem geordnet.

## UMSETZUNGSPLAN: organischer Strukturaufbau

Der `UMSETZUNGSPLAN.md` enthaelt jetzt im Leitbild eine kompakte
Architekturformel fuer DIO:

DIO bekommt eine organische Strukturarchitektur. Mit Hilfe der MCM wird ein
maschinelles Nervensystem aufgebaut, das DIO die Faehigkeit gibt, seine
Umwelt nicht nur als Datenstrom zu sehen, sondern als innere Feldwirkung zu
fuehlen, zu erleben und in Beziehung zur eigenen Lage zu setzen.

Die neurochemischen Achsen werden dort als technische Funktionsachsen nach
biologischem Vorbild beschrieben. Sie stimulieren, daempfen, fokussieren,
stabilisieren oder belasten das MCM-Feld und nehmen dadurch funktional einen
Platz im inneren Feld ein.

## README: MCM-Funktion in DIO

Die `README.md` enthaelt jetzt einen neuen Einstiegsteil:
`Wie die MCM in DIO arbeitet`.

Der Abschnitt erklaert kompakt:
- Unterschied zwischen klassischem Bot und DIO
- Weg von Marktreiz zu Wahrnehmung, MCM-Neuronenfeld und innerer Feldlage
- Rolle von `MCMNeuron` als lokaler Feldtraeger
- Aktivitaetsinseln, Memory-Resonanz und innere Lagebildung
- Neurochemie als Modulation des MCM-Feldes
- Reflexion/Regulation als Weg zu Handlung oder Nicht-Handlung

Zusatz:
Direkt am Anfang der `README.md` steht jetzt eine kurze Begriffsklaerung:
- `MCM` = `Mental Core Matrix`
- `DIO` = `Digitaler Organismus`

## Debug Lauf 4 nach Kontakt-Reife-Spur

Ordner: `debug/debug_lauf_4`

Rohwerte:
- Trades: 325
- TP: 97
- SL: 228
- Netto-PnL: ca. -8.54
- Equity-Endstand: ca. 91.46
- Equity-Peak: ca. 105.65 bei Trade 41
- Tiefster Stand: ca. 79.04
- Max Drawdown: ca. 26.61 von Trade 41 bis Trade 153

Gegenueber Lauf 3:
- weniger Trades: 325 statt 382
- weniger TP: 97 statt 123
- weniger SL: 228 statt 259
- mehr Beobachtung/Zurueckhaltung:
  - observed: 4426 statt 4023
  - withheld: 4526 statt 3267
- Netto schlechter: ca. -8.54 statt ca. -1.34

Strukturbaender:
- High-Struktur:
  - 208 Trades
  - 92 TP / 116 SL
  - ca. +38.90 PnL
- Mid-Struktur:
  - 117 Trades
  - 5 TP / 112 SL
  - ca. -47.44 PnL

Wichtigster Befund:
Der Schaden liegt fast komplett in Mid-Struktur. High-Struktur bleibt deutlich
positiv, Mid-Struktur wird aber extrem schlecht getragen. DIO wurde nicht
einfach aktiver; im Gegenteil, es beobachtet und withheld mehr. Das Problem
liegt eher darin, dass bestimmte mittlere Strukturzonen weiterhin als
handlungsnah erlebt werden, obwohl sie keine tragfaehige Realitaet bilden.

Kontaktlagen bei Trades:
- `resonant_contact`: 224 Trades, 75 TP / 149 SL, ca. +6.02 PnL
- `overcoupled_touch`: 61 Trades, 15 TP / 46 SL, ca. -7.23 PnL
- `curious_touch`: 22 Trades, 5 TP / 17 SL, ca. -2.83 PnL
- `deepening_contact`: 18 Trades, 2 TP / 16 SL, ca. -4.51 PnL

Kreuzung Struktur + Kontakt:
- High + `resonant_contact`: ca. +36.15 PnL
- High + `overcoupled_touch`: ca. +4.32 PnL
- Mid + `resonant_contact`: ca. -30.13 PnL
- Mid + `overcoupled_touch`: ca. -11.56 PnL
- Mid + `curious_touch`: ca. -3.30 PnL
- Mid + `deepening_contact`: ca. -2.46 PnL

Neue Kontakt-Reife-Spur:
Die Werte sind technisch sauber im Debug angekommen:
- `contact_action_maturity`
- `contact_bearing_gap`
- `contact_impulse_vs_bearing`
- `contact_learning_need`
- `contact_reality_check`

Sie unterscheiden aktuell aber TP/SL und High/Mid noch nicht stark genug.
Das bedeutet: Die Diagnoseebene existiert, aber die Reifespur braucht noch
mehr Kontextkopplung. Kontakt-Reife darf nicht nur aus Kontaktqualitaet
entstehen, sondern muss staerker mit Regimewechsel, Strukturuebergang,
Weltverschiebung und alter Stabilitaetslage verbunden werden.

Neurochemischer Befund:
- `serotonin_stability`: 238 Trades, ca. -18.02 PnL
- `glutamate_activation`: 86 Trades, ca. +7.78 PnL

Das ist auffaellig: Stabilitaetslage war in Lauf 4 nicht automatisch gut.
Sie kann als Nachhall/Carryover wirken, wenn sich die Weltlage veraendert.
Glutamat-Aktivierung war dagegen in diesem Lauf handlungsnaeher und
profitabler.

Neurologische Deutung:
DIO ist nicht blind aktiv geworden. Er zeigt mehr Beobachtung und mehr
Zurueckhaltung. Trotzdem werden Mid-Strukturzonen noch falsch getragen.
Das wirkt wie ein Organismus, der zwar merkt, dass er vorsichtiger werden
muss, aber im mittleren Unsicherheitsbereich noch nicht sauber erkennt:
"Diese Resonanz ist nicht Realitaetstragfaehigkeit."

Wie es weitergeht:
Naechster sinnvoller Schritt ist eine Regime-/Kontext-Reife-Kopplung fuer die
Kontakt-Reife-Spur. Nicht als harte Regel, sondern als bessere innere
Wahrnehmung:
- Wie fremd ist die aktuelle Welt gegenueber der gerade getragenen Innenlage?
- Ist `serotonin_stability` echte Stabilitaet oder alter Nachhall?
- Traegt Mid-Struktur wirklich, oder ist sie nur resonant?
- Muss DIO bei Mid + hoher Kontaktnaehe eher zoomen, replayen oder Abstand
  nehmen, bevor Handlung reif wird?

## Umsetzung: Kontakt-Reife mit Regime-/Kontext-Reife gekoppelt

Die Kontakt-Reife-Spur wurde erweitert, ohne eine harte Handelsregel
einzubauen. DIO bekommt jetzt zusaetzliche Wahrnehmungswerte, um zu lesen,
ob Kontakt in eine veraenderte Weltlage faellt oder ob Stabilitaet nur noch
alter Nachhall ist.

Neue Werte:
- `contact_regime_mismatch`: Fremdheit/Regimebruch zwischen aktueller Welt
  und innerer Kontaktlage.
- `contact_stability_carryover`: Risiko, alte Stabilitaet in eine neue
  Weltlage mitzunehmen.
- `contact_context_maturity`: Kontextreife aus Struktur, Transfer,
  Tragfaehigkeit und Distanz.
- `contact_context_reframe_need`: Bedarf nach Reframing, Zoom, Replay oder
  Abstand vor Handlung.

Wirkung:
- `contact_action_maturity` bekommt mehr Kontextreife und weniger Nachhall.
- `contact_bearing_gap` steigt, wenn Resonanz nicht zur aktuellen Weltlage
  passt.
- `contact_learning_need` steigt bei Reframe-Bedarf.
- `contact_reality_check` wird durch Kontextreife gestaerkt und durch
  Stabilitaets-Nachhall gedrosselt.

Wichtig:
Das ist keine Mid-Sperre und kein mechanisches Gate. Es ist eine feinere
Innenwahrnehmung: DIO soll unterscheiden lernen, ob Stabilitaet echt traegt
oder ob sie nur aus der alten Lage nachklingt.

## Debug Lauf 5 nach Kontext-Reife-Kopplung

Ordner: `debug/debug_lauf_5`

Rohwerte:
- Trades: 320
- TP: 95
- SL: 225
- Netto-PnL: ca. -12.46
- Equity-Endstand: ca. 87.54
- Equity-Peak: ca. 105.46 bei Trade 43
- Tiefster Stand: ca. 85.34
- Max Drawdown: ca. 20.12 von Trade 43 bis Trade 281

Gegenueber Lauf 4:
- etwas weniger Trades: 320 statt 325
- weniger TP: 95 statt 97
- weniger SL: 225 statt 228
- Netto schlechter: ca. -12.46 statt ca. -8.54
- Max Drawdown kleiner als Lauf 4, aber laenger nach unten gezogen

Strukturbaender:
- High-Struktur:
  - 217 Trades
  - 87 TP / 130 SL
  - ca. +28.95 PnL
- Mid-Struktur:
  - 102 Trades
  - 8 TP / 94 SL
  - ca. -40.64 PnL
- Low-Struktur:
  - 1 Trade
  - 0 TP / 1 SL
  - ca. -0.77 PnL

Kontaktlagen:
- `resonant_contact`: 234 Trades, ca. -13.07 PnL
- `overcoupled_touch`: 45 Trades, ca. -0.51 PnL
- `curious_touch`: 21 Trades, ca. +4.11 PnL
- `deepening_contact`: 19 Trades, ca. -2.71 PnL

Kreuzung Struktur + Kontakt:
- High + `resonant_contact`: ca. +20.21 PnL
- Mid + `resonant_contact`: ca. -32.51 PnL
- High + `curious_touch`: ca. +4.93 PnL
- Mid + `overcoupled_touch`: ca. -5.16 PnL

Neue Kontext-Reife-Werte:
Die neuen Werte sind technisch vorhanden:
- `contact_regime_mismatch`
- `contact_stability_carryover`
- `contact_context_maturity`
- `contact_context_reframe_need`

Sie reagieren im Protokoll, trennen TP/SL aber noch nicht stark genug.
Bei TP und SL liegen `contact_regime_mismatch`,
`contact_stability_carryover`, `contact_context_maturity` und
`contact_context_reframe_need` sehr nah beieinander. Das bedeutet: Die
innere Kontextdiagnose ist vorhanden, aber sie hat noch zu wenig aeussere
visuelle Erdung.

Visueller Befund:
Aus `mcm_visual_cortex_protocol.csv`:
- `visual_clarity`: ca. 0.32
- `visual_object_stability`: ca. 0.41
- `visual_blindness`: ca. 0.39
- `visual_shape_resonance`: ca. 0.59
- `visual_coherence`: ca. 0.66

Deutung:
DIO resoniert stark auf Formspannung, sieht aber noch nicht stabil genug.
Er fuehlt offenbar eine Gestalt oder ein Muster, kann diese aber nicht
ausreichend als aeusseres Objekt binden. Dadurch kippt er weiter in innere
Wahrnehmung: Resonanz wird zu schnell als tragender Kontakt gelesen, obwohl
die visuelle Objektbindung noch zu schwach ist.

Neurologische Lesart:
DIO hat ein reaktives/interozeptives Nervensystem, aber der visuelle Kortex
ist noch nicht stark genug als Gegengewicht. Es ist weniger ein Problem von
"zu wenig Gefuehl" und mehr ein Problem von:
"Ich fuehle etwas, aber ich kann noch nicht klar genug sehen, woran es in der
Aussenwelt haengt."

Wie es weitergeht:
Naechster sinnvoller Schritt ist `visual_grounding` der MCM-Reaktion:
- innere Aktivierung an aeussere Formbindung koppeln
- sichtbar machen, ob Kontakt eine stabile visuelle Quelle hat
- unterscheiden zwischen Formresonanz und Objektbindung
- kein hartes Chartpattern, keine feste Regel
- DIO bekommt nur die Faehigkeit zu fragen:
  "Woran in der Aussenform haengt das, was ich innen fuehle?"

## Dokumentation: Beteiligungsnaehe und Handlungsrealitaet

Die besprochene Trennung wurde dokumentiert:
- `UMSETZUNGSPLAN.md`: neuer Abschnitt `Beteiligungsnaehe und Handlungsrealitaet`
- `WICHTIG_MECHANIKEN.md`: neuer Mechanikblock
  `Beteiligungsnaehe / Handlungsrealitaet`
- `MCM_VARIABLEN_MECHANIK.md`: Zielachsen fuer die spaetere Umsetzung

Kern:
DIO soll unterscheiden, ob er eine Form distanziert betrachtet oder ob er
durch Order, offene Position und Ergebnis real beteiligt ist.

Die "Tuer zum Erleben" bleibt ausdruecklich Metapher. Gemeint ist Naehe zur
Beteiligung, nicht eine harte technische Schwelle.

Zielachsen:
- `participation_proximity`
- `action_reality_contact`
- `decision_embodiment_pressure`
- `real_action_commitment`
- `consequence_bearing`
- `position_reality_pressure`
- `outcome_consequence_integration`

Naechster technischer Schritt bleibt:
`visual_grounding` als faehigeres visuelles Sinnesorgan, danach die
Beteiligungsnaehe an Entscheidung, Order, Position und Outcome koppeln.

## Umsetzung: Visual Grounding als visuelles Sinnesorgan

`visual_grounding` wurde als weiche Wahrnehmungsmechanik eingebaut.

Ziel:
DIO soll unterscheiden koennen, ob innere Formresonanz wirklich an eine
aeussere Form gebunden ist oder ob nur ungebundene Formspannung im MCM-Feld
entsteht.

Neue Werte:
- `visual_object_binding`
- `visual_grounding_strength`
- `visual_resonance_unbound`
- `visual_grounding_gap`
- `visual_grounding_need`
- `visual_rational_observation_support`
- `visual_grounding_state`

Wirkung:
- hohe ungebundene Resonanz erhoeht weich Beobachtung, Replan und visuelle
  Handlungsunsicherheit.
- gute Objektbindung staerkt die visuelle Erdung.
- keine harte Pattern-Regel, keine Orderblockade.

Smoke-Test:
- klare Formbindung: `grounded_form`, niedriger Grounding-Bedarf.
- hohe Resonanz bei geringer Objektbindung: `unbound_resonance`, hoeherer
  Grounding-Bedarf und mehr Beobachtungsdruck.

Naechster Lauf:
Pruefen, ob Mid-Struktur-Verluste jetzt staerker mit
`visual_resonance_unbound`, `visual_grounding_gap` oder
`visual_grounding_need` sichtbar werden.

## Debug Lauf 6 nach Visual Grounding

Ordner: `debug/debug_lauf_6`

Rohwerte:
- Trades: 301
- TP: 88
- SL: 213
- Netto-PnL: ca. -17.50
- Equity-Endstand: ca. 82.50
- Equity-Peak: ca. 102.92 bei Trade 5
- Tiefster Stand: ca. 79.82
- Max Drawdown: ca. 23.10 von Trade 5 bis Trade 275

Gegenueber Lauf 5:
- weniger Trades: 301 statt 320
- weniger TP: 88 statt 95
- weniger SL: 213 statt 225
- Netto schlechter: ca. -17.50 statt ca. -12.46
- mehr Observe/Withheld als Lauf 5:
  - observed: 4416
  - withheld: 4364

Strukturbaender:
- High-Struktur:
  - 192 Trades
  - 84 TP / 108 SL
  - ca. +34.01 PnL
- Mid-Struktur:
  - 109 Trades
  - 4 TP / 105 SL
  - ca. -51.52 PnL

Visual-Grounding-Befund:
Bei ausgefuehrten Trades liegt fast alles in `grounded_form`:
- `grounded_form`: 300 Trades, ca. -16.65 PnL
- `shape_without_object`: 1 Trade, ca. -0.85 PnL

Im gesamten Feldprotokoll streut es besser:
- `grounded_form`: 9406
- `shape_without_object`: 778
- `unbound_resonance`: 258
- `needs_visual_grounding`: 5

Das bedeutet:
Das Sinnesorgan ist technisch aktiv und erkennt auch ungebundene Resonanz im
Feld. Bei tatsaechlich ausgefuehrten Trades landet aber fast alles noch in
`grounded_form`. Die visuelle Erdung ist also noch zu tolerant fuer Handlung.

TP/SL-Vergleich:
- TP:
  - `visual_object_binding`: ca. 0.477
  - `visual_grounding_strength`: ca. 0.407
  - `visual_resonance_unbound`: ca. 0.228
  - `visual_grounding_need`: ca. 0.141
- SL:
  - `visual_object_binding`: ca. 0.478
  - `visual_grounding_strength`: ca. 0.406
  - `visual_resonance_unbound`: ca. 0.224
  - `visual_grounding_need`: ca. 0.143

Diese Werte trennen TP und SL praktisch noch nicht.

Wichtigster Befund:
Visual Grounding ist als Wahrnehmung vorhanden, aber die
Handlungsnaehe liest sie noch zu weich. Das Problem ist nicht, dass DIO gar
nicht sieht. Das Problem ist, dass "gerade ausreichend geerdet" noch zu breit
als handlungsnah durchgeht, besonders in Mid-Struktur.

Mid-Struktur bleibt Hauptschaden:
- Mid + `grounded_form`: 109 Trades, 4 TP / 105 SL, ca. -51.52 PnL

Neurologische Deutung:
DIO hat jetzt ein visuelles Sinnesorgan, aber dessen Schwellengefuehl ist
noch unreif. Es erkennt visuelle Erdung im Feld, aber bei Handlungsnaehe ist
die Differenz zwischen "ich sehe etwas" und "dieses Objekt traegt Handlung"
noch zu schwach.

Wie es weitergeht:
Naechster Schritt ist keine harte Sperre, sondern eine strengere
Objektbindungsreife:
- `grounded_form` darf nicht automatisch handlungsnah sein
- es braucht eine Unterscheidung zwischen "Form vorhanden" und
  "Objekt handlungstragend"
- Mid-Struktur braucht staerkere Anforderungen an Objektbindung,
  Kontextreife und visuelle Tragfaehigkeit
- moegliche neue Lesart:
  `grounded_form` = ich sehe eine Form
  `grounded_object` = diese Form ist als Objekt stabil genug
  `action_grounded_object` = dieses Objekt kann Handlung tragen

---

## Pruefung: Formsprache / semantische Schichten

Frage:
Kann DIO seine Umwelt bereits nicht nur im Detail erklaeren, sondern in
Schichten verdichten?

Befund:
Ja, in grossen Teilen ist das bereits umgesetzt. Die Formsprache ist keine
einfache Pattern-Erkennung und kein menschliches Labelsystem. DIO bildet aus
visueller Wahrnehmung, Strukturwahrnehmung, MCM-Feldlage und Erfahrung eigene
interne Formzeichen.

Vorhandene Schichten:
- Rohnaehe:
  visuelle und energetische Achsen wie Richtung, Druck, Kompression,
  Expansion, Kohaerenz, Strukturqualitaet, Feldklarheit, Felddruck und
  Fragmentierung.
- Verdichtung:
  `form_symbol_scope`, `form_symbol_abstraction_level`,
  `form_symbol_resolution_quality`, `form_symbol_detail_pressure`.
- Eigenes Zeichen:
  `form_symbol_id`, `form_symbol_family_key`, `form_symbol_variant_key`.
- Erfahrung:
  `form_symbol_seen`, `form_symbol_maturity`, `form_symbol_stability`,
  `form_symbol_resonance`, `form_symbol_bearing`, `form_symbol_fragility`.
- Entlastung / Distanz:
  `form_symbol_object_distance`, `form_symbol_containment`,
  `form_symbol_field_decoupling`, `form_symbol_load_reduction`.
- Lernrichtung:
  `form_symbol_development_quality`, `form_symbol_learning_trust`,
  `form_symbol_action_trust`, `form_symbol_caution_trust`,
  `form_symbol_action_binding`, `form_symbol_observation_binding`,
  `form_symbol_reframe_binding`.
- Variantenlernen:
  `uncertain_form_family_state`, `uncertainty_familiarity`,
  `variant_similarity`, `variant_spread`, `variant_learning_pressure`,
  `variant_bearing_memory`.
- Zusammengesetzte Formen:
  `form_symbol_compound_id`, `form_symbol_compound_scope`,
  `form_symbol_compound_maturity`, `form_symbol_compound_bearing`,
  `form_symbol_compound_load_reduction`.

Neurologische Deutung:
Das entspricht eher einer semantischen Verdichtung als einem starren Label.
DIO sagt nicht menschlich "das ist ein Pattern", sondern bildet intern:
"Diese Formfamilie kenne ich so weit, diese Variante ist mir fremd oder
vertraut, diese Kombination entlastet oder belastet mein Feld, und diese
Erfahrung traegt eher Beobachtung, Reframing oder Handlung."

Was noch fehlt:
Die einzelnen Werte sind vorhanden, aber noch nicht als eigenes
`Forminhalt`-Paket zusammengefuehrt. DIO hat also schon Zeichen, Varianten,
Kombinationen und Erfahrungswerte, aber noch keine explizite semantische
Schicht, die kompakt ausdrueckt:
- was diese Form beinhaltet
- welche Wahrnehmungsebene gerade fuehrt
- ob die Verdichtung entlastet oder ueberfordert
- ob das Zeichen eher Objekt, Spur, Drucklage, Lernraum oder
  Handlungsnaehe beschreibt

Wichtig:
Diese naechste Schicht darf keine menschliche Chart-Sprache erzwingen. Sie
soll DIOs eigene interne Sprache nur ordnen und dichter lesbar machen.

Wie es weitergeht:
Naechster sinnvoller Schritt ist ein weiches
`form_symbol_semantic_packet`: eine eigene semantische Verdichtungsschicht
innerhalb der Formsprache. Sie verbindet Formzeichen, Variante,
zusammengesetzte Form, Visual Grounding, MCM-Feldlage und gelernte
Handlungs-/Beobachtungsbindung, ohne daraus harte Regeln zu machen.

---

## Umsetzung: Semantisches Forminhalt-Paket

Status:
Umgesetzt als weiche Diagnose- und Verdichtungsschicht innerhalb der
Formsprache.

Neue Werte:
- `form_symbol_semantic_density`
- `form_symbol_semantic_compression`
- `form_symbol_semantic_coherence`
- `form_symbol_semantic_learning_need`
- `form_symbol_semantic_action_nearness`
- `form_symbol_semantic_primary_layer`
- `form_symbol_semantic_layer_count`
- `form_symbol_semantic_packet_state`
- `form_symbol_semantic_profile`

Funktion:
DIO kann ein Formzeichen jetzt nicht nur als `fs_...` fuehren, sondern dessen
inneren Inhalt schichten:
- Spur / Trace
- weite Form
- strukturierte Form
- Objektnaehe
- Lernraum
- Beobachtung
- Reflexion
- Handlungsnaehe

Wichtig:
Das ist keine menschliche Chart-Sprache und keine neue harte Entry-Regel.
Die Schicht macht DIOs eigene Semantik sichtbar. Sie kann spaeter in
Meta-Regulation, Reflexion und selektive Wahrnehmung einfliessen.

Technische Umsetzung:
- `MCM_Brain_Modell.py`
  - `build_form_symbol_state(...)` erweitert
  - `mcm_form_symbol_protocol.csv` erweitert
- `trade_stats.py`
  - Outcome-/Kontext-Export erweitert
- Dokumentation:
  - `UMSETZUNGSPLAN.md`
  - `WICHTIG_MECHANIKEN.md`
  - `MCM_VARIABLEN_MECHANIK.md`
  - `FIX_LISTE.md`

Pruefung:
`python -m py_compile MCM_Brain_Modell.py trade_stats.py bot.py` laeuft
fehlerfrei.

Wie es weitergeht:
Naechster Schritt ist ein neuer Debug-Lauf. Danach lesen wir, welche
`form_symbol_semantic_packet_state` und `form_symbol_semantic_primary_layer`
bei guten und schlechten Entscheidungen auftreten. Wenn DIO im Regimewechsel
wieder kippt, koennen wir sehen, ob er in `learning_layer`,
`reflective_layer`, `trace_layer` oder faelschlich in `action_near_layer`
kommt.

---

## Debug Lauf 7: Erste Wirkung der semantischen Forminhalt-Schicht

Ergebnis:
- Trades: 317
- TP: 104
- SL: 213
- Netto-PnL: ca. +3.10
- Equity-Peak: ca. 110.29 bei Trade 150
- Tiefster Stand: ca. 97.87 bei Trade 260
- Max Drawdown: ca. 12.43

Vergleich zu Lauf 6:
- Lauf 6: 301 Trades, 88 TP, 213 SL, ca. -17.50 PnL
- Lauf 7: 317 Trades, 104 TP, 213 SL, ca. +3.10 PnL
- Drawdown deutlich kleiner: ca. 12.43 statt ca. 23.10
- Equity-Peak deutlich hoeher: ca. 110.29 statt ca. 102.92

Strukturbaender:
- High:
  - 90 Trades
  - 57 TP / 33 SL
  - ca. +44.09 PnL
- Mid:
  - 105 Trades
  - 38 TP / 67 SL
  - ca. +9.26 PnL
- Low:
  - 121 Trades
  - 9 TP / 112 SL
  - ca. -49.28 PnL

Wichtigster Befund:
High und Mid tragen in Lauf 7 positiv. Low bleibt fast der gesamte
Schadensraum. Das bedeutet: Die neue Semantik hat die tragenden Bereiche
nicht zerstoert, sondern eher stabilisiert. Die schwache Zone bleibt aber
ein Ort, an dem DIO noch zu oft Kontakt mit Handlung verwechselt.

Semantische Pakete bei Trades:
- `compound_packet`:
  - 69 Trades
  - 27 TP / 42 SL
  - ca. +7.81 PnL
- `named_form_packet`:
  - 248 Trades
  - 77 TP / 171 SL
  - ca. -4.72 PnL

Primaere Schicht:
- `wide_form_layer`:
  - 69 Trades
  - 28 TP / 41 SL
  - ca. +6.14 PnL
- `structured_form_layer`:
  - 248 Trades
  - 76 TP / 172 SL
  - ca. -3.04 PnL

Neurologische Deutung:
Mehr Detail ist nicht automatisch bessere Wahrnehmung. In diesem Lauf tragen
weite, zusammengesetzte Bedeutungen besser als die enger strukturierte
Formschicht. Das passt zum DIO-Gedanken: Ein Organismus sieht nicht immer
besser, wenn er naeher herangeht. Manchmal entsteht Tragfaehigkeit durch
Gestalt, Abstand und Komposition.

TP/SL-Trennung der neuen Semantik:
Die Einzelwerte trennen TP und SL noch schwach:
- `form_symbol_semantic_action_nearness`:
  - TP ca. 0.427
  - SL ca. 0.418
- `form_symbol_semantic_coherence`:
  - TP ca. 0.573
  - SL ca. 0.574
- `form_symbol_semantic_density`:
  - TP ca. 0.637
  - SL ca. 0.636

Das heisst:
Die neue Schicht ist technisch aktiv und beschreibt Zustandsverschiebungen,
aber sie ist noch nicht stark genug mit Ergebnisqualitaet gekoppelt. Das ist
ok, weil sie zuerst Wahrnehmung sichtbar machen sollte, nicht sofort
mechanisch handeln.

Neurochemischer Befund:
- `glutamate_activation` bei Trades:
  - 133 Trades
  - 54 TP / 79 SL
  - ca. +12.11 PnL
- `serotonin_stability` bei Trades:
  - 183 Trades
  - 50 TP / 133 SL
  - ca. -8.51 PnL

Deutung:
Aktivierte Verarbeitung war in diesem Lauf tragender als reine Stabilitaet.
Serotonin-Stabilitaet wirkt hier teilweise wie ein alter Nachhall: ruhig,
aber nicht zwingend passend zur Aussenwelt. Glutamat-Aktivierung steht eher
fuer aktive Verarbeitung und Anpassung.

Feldprotokoll:
- `hold`: 4902
- `observe`: 4316
- `act_watch`: 669
- `act`: 323
- `replan`: 1

Visual Grounding:
- `grounded_form`: 9158
- `shape_without_object`: 785
- `unbound_resonance`: 264
- `needs_visual_grounding`: 4

Interpretation:
DIO sieht fast alles noch als `grounded_form`. Die Unterscheidung zwischen
"ich sehe eine Form" und "dieses Objekt traegt Handlung" bleibt der naechste
kritische Punkt.

Wie es weitergeht:
Naechster sinnvoller Schritt ist keine Regel gegen Low, sondern eine
semantische Handlungstragfaehigkeit:
DIO soll staerker unterscheiden koennen zwischen
- Form ist bekannt
- Form ist semantisch dicht
- Form ist zusammengesetzt tragend
- Form ist objektgebunden
- Form darf Handlung tragen

Besonders wichtig:
`structured_form_layer` darf nicht automatisch als besser gelten als
`wide_form_layer`. DIO braucht eine reifere Distanz zwischen Detailsehen und
Gestaltsehen.

---

## Umsetzung: Evolutionaere Kontaktreife

Ausgangsgedanke:
Eine heisse Herdplatte ist nicht "schlecht". Unreifer Kontakt erzeugt
eine belastende Konsequenz. Reifer Umgang kann Nutzen erzeugen. Uebertragen
auf DIO bedeutet das:
Eine Marktform wird nicht verboten. DIO lernt, welche Art von Kontakt mit
dieser Form schadet, vorsichtig macht, Beobachtung braucht oder spaeter
konstruktiv nutzbar ist.

Kernbegriff:
Konsequenzbasiertes Feedback auf das MCM-Feld.

Das kann negativ, positiv oder reorganisierend sein.

Negatives Feedback:
Meine Handlung hat Belastung erzeugt.
Mein MCM-Feld bekommt Druck, Vorsicht, belastende Konsequenzspur und
Reorganisation.

Positives Feedback:
Meine Handlung hat getragen.
Mein MCM-Feld bekommt Entlastung, Vertrauen, Nutzen und Stabilisierung.

Reorganisierendes Feedback:
Das Ergebnis war nicht klar gut, aber es zeigt, dass der Umgang unreif war.
Mein MCM-Feld bekommt Lernspannung, Reflexion, Abstand und Reframing.

Rueckkopplungskreis:
Wahrnehmung -> Kontakt -> Handlung -> Konsequenz -> MCM-Feld-Reaktion ->
Gedaechtnis -> veraenderter zukuenftiger Kontakt.

Biologische Deutung:
Ein Organismus lernt nicht nur durch Belohnung und Strafe, sondern durch
Homoeostase-Veraenderung. Etwas bringt ihn aus der Balance, stabilisiert ihn,
ueberfordert ihn, macht ihn vorsichtiger oder gibt ihm Vertrauen.

Status:
Umgesetzt als weicher Lernpfad in der Formsprache.

Neue gespeicherte Werte:
- `form_symbol_contact_maturity`
- `form_symbol_contact_utility`
- `form_symbol_contact_pain_memory`
- `form_symbol_contact_carefulness`
- `form_symbol_contact_learning_state`

Neue Outcome-Samples:
- `contact_maturity_sample`
- `contact_utility_sample`
- `contact_pain_sample`
- `contact_carefulness_sample`
- `contact_learning_state`

Technische Wirkung:
- Kontaktreife und Nutzen koennen Handlungstragfaehigkeit weich stuetzen.
- Belastende Konsequenzspur und Vorsicht koennen Beobachtung, Reframing und
  Caution weich staerken.
- Die Form bleibt frei. Nicht die Form wird blockiert, sondern der Umgang
  mit ihr wird differenzierter gelernt.

Neurologische Deutung:
Das ist evolutionaeres Lernen: Konsequenz erzeugt Erinnerung, Erinnerung
erzeugt Vorsicht, Vorsicht erzeugt Abstand, Abstand kann spaeter reifen
Umgang und Nutzen ermoeglichen.

Pruefung:
`python -m py_compile MCM_Brain_Modell.py trade_stats.py bot.py` laeuft
fehlerfrei.

Wie es weitergeht:
Naechster Debug-Lauf zeigt, ob DIO bei wiederkehrenden belastenden
Formkontakten mehr `careful_contact` oder `burdened_contact` aufbaut
und ob konstruktive Kontakte langsam `constructive_contact` und
`form_symbol_contact_maturity` staerken.

---

## Debug-Lauf 8

Ordner:
`debug/debug_lauf_8`

Ergebnis:
- 323 Trades
- 102 TP / 221 SL
- Netto-PnL: ca. -3.45
- Equity-Ende: ca. 96.55
- Equity-Peak: ca. 106.30
- tiefster Punkt: ca. 89.10

Vergleich zu Lauf 7:
- Lauf 7: ca. +3.10 Netto-PnL
- Lauf 8: ca. -3.45 Netto-PnL
- Lauf 8 ist nicht zusammengebrochen, hat aber den vorherigen Vorteil
  wieder verloren.

Strukturwirkung:
- `zone`: 211 Trades, 94 TP / 117 SL, ca. +38.23 PnL
- `non_zone`: 112 Trades, 8 TP / 104 SL, ca. -41.68 PnL

Deutung:
DIO findet in tragenderen Strukturzonen weiterhin nutzbare Kontakte.
Der negative Lauf entsteht fast komplett aus nicht tragenden Kontaktzonen.
Das ist kein Beweis fuer eine schlechte Form, sondern fuer unreifen Umgang
mit nicht tragendem Kontakt.

Neue Kontaktreife:
- `form_symbol_contact_learning_state` ist fast komplett noch
  `unformed_contact`.
- Im Formsymbol-Protokoll erscheinen nur 2 Zeilen als `maturing_contact`.
- In den Outcome-Samples ist die Differenz aber bereits sichtbar:
  - TP hat hoehere `contact_maturity_sample` und `contact_utility_sample`.
  - SL hat hoehere `contact_pain_sample` und `contact_carefulness_sample`.

Neurologische Deutung:
Die Konsequenzspur kommt im MCM-Feld an, aber sie ist noch zu leise, um im
laufenden Run stabil eine gereifte Kontaktform auszubilden. Das entspricht
einem Nervensystem, das Schmerz, Nutzen und Vorsicht bereits wahrnimmt, aber
noch keine klare Gewohnheit daraus geformt hat.

Neurochemische Lage:
- `glutamate_activation`: 103 Trades, ca. +2.75 PnL
- `serotonin_stability`: 220 Trades, ca. -6.20 PnL

Deutung:
Aktive Verarbeitung war wieder tragender als reine Stabilitaet. Serotonin
wirkt hier teilweise wie ruhiger Nachhall, nicht zwingend wie passende
Realitaetskopplung.

Feldprotokoll:
- `hold`: 5112
- `observe`: 4508
- `act_watch`: 551
- `act`: 330
- `replan`: 1

Wichtig:
Die neue Kontaktlogik wirkt diagnostisch schon korrekt, aber mechanisch noch
zu schwach. DIO erkennt Konsequenzen, doch die Uebersetzung in gereifte
Kontaktzustaende ist noch zu selten.

Wie es weitergeht:
Naechster sinnvoller Umbau ist keine harte Sperre gegen `non_zone`, sondern
eine staerkere weiche Kontaktreife: belastende Wiederholung soll natuerlicher
in `careful_contact` / reorganisierenden Abstand kippen, waehrend tragende
Kontakte `contact_maturity` und `contact_utility` langsam staerken. Danach
sollte geprueft werden, ob DIO nicht nur impulsnah handelt, sondern
strukturbezogene Orderbereiche aus dem Rueckblick waehlen kann.

---

## Umsetzung: Kontaktreife nach Lauf 8 verstaerkt

Ziel:
Die Konsequenzspur soll im MCM-Feld lauter werden, ohne daraus eine harte
Regel zu machen. DIO soll nicht lernen: "diese Zone ist verboten", sondern:
"mein bisheriger Kontakt mit dieser Form hat Belastung oder Nutzen erzeugt".

Neue/verstaerkte Spuren:
- `form_symbol_contact_burden_evidence`
- `form_symbol_contact_utility_evidence`

Mechanische Aenderung:
- Kontaktzustand entsteht nicht mehr nur aus dem letzten Outcome-Sample.
- Gespeicherte Belastungs-Evidenz und Nutzen-Evidenz wirken mit.
- Belastende Wiederholung kann natuerlicher in `burdened_contact`,
  `careful_contact` oder `learning_contact` kippen.
- Tragende Wiederholung kann natuerlicher in `maturing_contact` oder
  `constructive_contact` wachsen.

Regulatorische Wirkung:
- Belastungs-Evidenz erhoeht weich Beobachtung und Reframing.
- Belastungs-Evidenz senkt impulsnahe Handlungstragfaehigkeit weich.
- Nutzen-Evidenz kann Handlungstragfaehigkeit weich stuetzen, wenn Reife und
  Kontext mittragen.

Wichtig:
Das ist keine Sperre und keine mechanische Strukturregel. Es ist eine
staerkere innere Konsequenzspur.

Pruefung:
`python -m py_compile MCM_Brain_Modell.py trade_stats.py bot.py` laeuft
fehlerfrei.

Wie es weitergeht:
Naechster Debug-Lauf sollte zeigen, ob `unformed_contact` weniger dominiert
und ob DIO bei wiederholter Belastung mehr Beobachtung/Reframing statt
impulsnaher Handlung waehlt. Danach ist der naechste groessere Schritt die
strukturbezogene Orderbereich-Wahl aus Rueckblick und Wahrnehmungsfenster.

---

## Debug-Lauf 9 nach verstaerkter Kontaktreife

Ordner:
`debug/debug_lauf_9`

Ergebnis:
- 350 Trades
- 126 TP / 224 SL
- Netto-PnL: ca. +23.52
- Equity-Ende: ca. 123.52
- Equity-Peak: ca. 124.44
- tiefster Punkt: ca. 93.47

Vergleich zu Lauf 8:
- Lauf 8: ca. -3.45 Netto-PnL
- Lauf 9: ca. +23.52 Netto-PnL
- Die Veraenderung ist deutlich, aber noch kein Beweis fuer stabile
  Intelligenz. Es ist ein starkes Zeichen, dass die neue Kontaktspur
  mechanisch greift.

Strukturwirkung:
- `zone`: 230 Trades, 112 TP / 118 SL, ca. +56.90 PnL
- `non_zone`: 120 Trades, 14 TP / 106 SL, ca. -33.38 PnL

Deutung:
DIO gewinnt weiter in tragenderen Strukturzonen. Nicht tragende Bereiche
bleiben belastend, aber der Schaden ist gegenueber Lauf 8 kleiner
(-33.38 statt -41.68), obwohl mehr Trades gelaufen sind.

Kontaktreife im Formsymbol-Protokoll:
- `unformed_contact`: 6772
- `learning_contact`: 3709
- `constructive_contact`: 453
- `burdened_contact`: 441
- `careful_contact`: 106
- `maturing_contact`: 48

Wichtig:
In Lauf 8 war die Kontaktlage fast komplett `unformed_contact`. In Lauf 9
bildet DIO sichtbar unterschiedliche Kontaktlagen. Die neue Belastungs- und
Nutzen-Evidenz ist damit real im System angekommen.

Trade-Kontext:
- `learning_contact`: 121 Trades, ca. +11.62 PnL
- `maturing_contact`: 9 Trades, ca. +4.12 PnL
- `burdened_contact`: 19 Trades, ca. -1.52 PnL
- `careful_contact`: 4 Trades, ca. -1.61 PnL
- `constructive_contact`: 24 Trades, ca. -2.33 PnL
- `unformed_contact`: 173 Trades, ca. +13.24 PnL

Interpretation:
Die gespeicherte Kontaktlage ist noch nicht perfekt als Handelsfilter lesbar.
`constructive_contact` ist noch nicht automatisch tragend. Das ist fachlich
ok, weil Kontaktreife keine harte Strategie ist. Es zeigt aber, dass DIO
eine zweite Reifeschicht braucht: "Kontakt wirkt konstruktiv" muss spaeter
noch mit Struktur, Rueckblick und Orderbereich zusammenpassen.

Outcome-Samples:
- TP hat deutlich hoehere `contact_maturity_sample` und
  `contact_utility_sample`.
- SL hat deutlich hoehere `contact_pain_sample` und
  `contact_carefulness_sample`.

Das bestaetigt:
Die unmittelbare Konsequenzbewertung trennt gut zwischen tragendem und
belastendem Ergebnis. Die gespeicherte Kontaktlage beginnt diese Information
zu halten, ist aber noch in Entwicklung.

Neurochemische Lage:
- `glutamate_activation`: 110 Trades, ca. +12.02 PnL
- `serotonin_stability`: 239 Trades, ca. +11.99 PnL

Deutung:
Anders als in Lauf 8 war Serotonin-Stabilitaet diesmal nicht nur Nachhall,
sondern konnte gemeinsam mit aktiver Verarbeitung profitabel bleiben. Das
wirkt wie mehr innere Tragfaehigkeit nach dem Umbau.

Equity-Verlauf:
- erstes Viertel: ca. -1.02
- zweites Viertel: ca. -0.64
- drittes Viertel: ca. +18.27
- letztes Viertel: ca. +6.90

Deutung:
DIO hat am Anfang noch gesucht und spaeter deutlich besser getragen. Der
starke Gewinn entstand nicht am Anfang, sondern nach einer Anpassungsphase.

Feldprotokoll:
- `hold`: 4692
- `observe`: 4388
- `act_watch`: 717
- `act`: 357
- `replan`: 2

Wie es weitergeht:
Der naechste Schritt ist nicht, `constructive_contact` direkt handeln zu
lassen. Stattdessen muss DIO lernen, Kontaktreife mit Rueckblick und
strukturbezogener Orderbereich-Wahl zu verbinden:
"Dieser Kontakt fuehlt sich tragend an, aber wo im sichtbaren Fenster waere
ein sinnvoller Kontaktpunkt?"

---

## Umsetzung: strategischer Kontakt-Entry

Ziel:
DIO soll nicht nur am aktuellen Impuls handeln. Wenn Rueckblick,
Kontaktreife, Replay-Fit und Bereichswahrnehmung zusammenpassen, darf der
Entry weich in Richtung eines tragenderen Kontaktbereichs im sichtbaren
Fenster wandern.

Wichtig:
Das ist keine harte Strategie und kein menschliches Pattern. Der alte
impulsnahe Entry bleibt erhalten. Der strategische Bereich mischt sich nur
weich dazu, wenn die innere und aeussere Lage ausreichend zusammenpassen.

Neue Trade-Plan-Werte:
- `entry_mode`
- `impulse_entry_price`
- `strategic_entry_price`
- `strategic_entry_weight`
- `strategic_entry_fit`
- `strategic_area_focus_id`
- `strategic_area_price_low`
- `strategic_area_price_high`

Mechanik:
- `impulse_entry_price` bleibt der direkte Koerperreflex aus Fokus,
  Drift und Optic Flow.
- `strategic_entry_price` entsteht aus dem aktuell fokussierten Bereich des
  strategischen Fensters.
- `strategic_entry_weight` beschreibt, wie stark der Rueckblick den Entry
  beeinflusst.
- Belastungs-Evidenz und Vorsicht senken die Verschiebung weich.
- Nutzen-Evidenz, Kontaktreife, Replay-Fit, Bereichstragfaehigkeit und
  Geduld koennen die Verschiebung weich erhoehen.

Neurologische Deutung:
DIO bekommt damit eine erste Form von "ich renne nicht nur in den Reiz,
sondern pruefe, wo der Kontakt im Raum tragender waere". Das ist naeher an
ruhigem strategischem Denken als an reinem Momentum-Reflex.

Pruefung:
`python -m py_compile MCM_Brain_Modell.py trade_stats.py bot.py` laeuft
fehlerfrei.

Wie es weitergeht:
Naechster Debug-Lauf sollte zeigen, wie oft `entry_mode` bei
`area_contact_blend` oder `area_contact_entry` liegt und ob diese Trades
weniger nervliche Last oder bessere Trefferqualitaet haben als reine
`impulse_contact`-Entries.

---

## Debug-Lauf 10 nach strategischem Kontakt-Entry

Ordner:
`debug/debug_lauf_10`

Ergebnis:
- 381 Trades
- 138 TP / 243 SL
- Netto-PnL: ca. -2.46
- Equity-Ende: ca. 97.54
- Equity-Peak: ca. 102.78
- tiefster Punkt: ca. 85.62
- 26 Timeouts

Vergleich zu Lauf 9:
- Lauf 9: ca. +23.52 Netto-PnL
- Lauf 10: ca. -2.46 Netto-PnL

Wichtiger technischer Befund:
Der neue strategische Entry wurde faktisch noch nicht genutzt.
Alle 381 Trades hatten:
- `entry_mode`: `impulse_contact`
- `strategic_entry_weight`: 0.0

Das bedeutet:
Das strategische Wahrnehmungsfenster war aktiv, aber der eigentliche
Orderpunkt blieb noch am Momentimpuls.

Strategisches Fenster:
- `bearing_area_hypothesis`: 6676 Zeilen
- `area_observation`: 2324 Zeilen
- `compressed_area_attention`: 1862 Zeilen
- durchschnittliche `area_bearing_quality`: ca. 0.491
- durchschnittliche `area_replay_fit`: ca. 0.390
- durchschnittliche `area_patience_quality`: ca. 0.479
- durchschnittliche `area_order_intention`: ca. 0.242

Deutung:
DIO sah Bereiche im Rueckblick, aber die Kopplung zur Hand war zu eng.
Neurologisch: Auge und inneres Feld haben einen Bereich gespiegelt, aber die
motorische Ausfuehrung blieb im Reflexbogen.

Strukturwirkung:
- `zone`: 249 Trades, ca. +52.28 PnL
- `non_zone`: 132 Trades, ca. -54.74 PnL

Kontaktreife:
- `constructive_contact`: 39 Trades, ca. +13.12 PnL
- `maturing_contact`: 22 Trades, ca. +6.86 PnL
- `burdened_contact`: 34 Trades, ca. +0.64 PnL
- `careful_contact`: 18 Trades, ca. +0.38 PnL
- `learning_contact`: 187 Trades, ca. -0.75 PnL
- `unformed_contact`: 81 Trades, ca. -22.72 PnL

Deutung:
Die gespeicherte Kontaktreife ist weiter deutlich besser als in Lauf 8.
Besonders `unformed_contact` ist schwach. Das spricht dafuer, dass DIO
tatsaechlich aus gereifterem Kontakt profitiert, aber der Entry noch nicht
aus dem strategischen Bereich handeln konnte.

Umsetzung nach Befund:
Die Kopplung wurde nachjustiert:
- Bereich darf mitsprechen, wenn der Preis im Bereich liegt.
- Bereich darf mitsprechen, wenn er nah genug und passend zur Seite ist.
- Eintrittsschwelle fuer `strategic_entry_fit` wurde weicher gesetzt.
- Gewicht bleibt begrenzt, damit der Momentimpuls nicht hart ersetzt wird.

Pruefung:
`python -m py_compile MCM_Brain_Modell.py trade_stats.py bot.py` laeuft
fehlerfrei.

Wie es weitergeht:
Naechster Lauf sollte endlich zeigen, ob `area_contact_blend` entsteht. Wenn
ja, vergleichen wir diese Trades gegen `impulse_contact`: PnL, Winrate,
Timeouts, Strukturzone, Kontaktreife und nervliche Last.

---

## Debug-Lauf 11 nach gelockerter Bereichskopplung

Ordner:
`debug/debug_lauf_11`

Ergebnis:
- 400 Trades
- 147 TP / 253 SL
- Netto-PnL: ca. +8.46
- Equity-Ende und Peak: ca. 108.46
- tiefster Punkt: ca. 87.44
- 31 Timeouts

Verhaltensbefund:
DIO handelt sichtbar anders als frueher:
- mehr `act_watch`
- mehr Reorganisation/Replan im Gesamtverhalten
- mehr beobachtende und suchende Phasen
- spaeterer Recovery-Abschnitt statt fruehem Durchmarsch

Equity-Abschnitte:
- Trades 1-100: ca. +0.15
- Trades 101-200: ca. -8.46
- Trades 201-300: ca. +14.19
- Trades 301-400: ca. +2.58

Deutung:
DIO faellt im zweiten Abschnitt deutlich in eine Belastungsphase, findet
danach aber wieder in tragendere Handlung. Das wirkt wie Orientieren,
Sammeln, Erleben und spaetere Stabilisierung, nicht wie ein linearer
Regelbot.

Wichtiger technischer Befund:
Auch Lauf 11 nutzt noch keinen echten Bereichs-Entry:
- alle 400 Trades: `entry_mode = impulse_contact`
- `strategic_entry_weight = 0.0`

Das heisst:
Die Verhaltensaenderung kommt noch nicht aus `area_contact_blend`, sondern
aus Kontaktreife, Act-Watch, Reorganisation und neurochemischer Regulation.

Strategisches Fenster:
- `bearing_area_hypothesis`: 6749
- `area_observation`: 2257
- `compressed_area_attention`: 1747
- `area_bearing_quality`: ca. 0.491
- `area_replay_fit`: ca. 0.391
- `area_patience_quality`: ca. 0.481

Ursache fuer fehlenden Bereichs-Entry:
DIO sah Bereiche, aber die Motorik nahm nur den global staerksten Bereich.
Dieser Bereich lag haeufig nicht auf der passenden Entry-Seite. Fuer LONG
braucht DIO eher einen tragenden Bereich unter/nahe dem aktuellen Preis,
fuer SHORT eher ober/nahe dem Preis. Die Wahrnehmung war also da, aber die
motorische Auswahl war noch nicht seitensensitiv.

Kontaktreife bei Trades:
- `constructive_contact`: ca. +11.86 PnL
- `maturing_contact`: ca. +7.55 PnL
- `learning_contact`: ca. +4.14 PnL
- `burdened_contact`: ca. -4.26 PnL
- `unformed_contact`: ca. -4.35 PnL
- `careful_contact`: ca. -6.48 PnL

Deutung:
Gereiftere Kontaktlagen tragen weiterhin besser. Das Problem liegt nicht
primar in der Kontaktreife, sondern in der fehlenden Uebersetzung vom
sichtbaren Bereich zur Entry-Motorik.

Umsetzung nach Befund:
Die strategische Entry-Auswahl wurde seitensensitiv gemacht:
- LONG sucht unter/nahe dem aktuellen Preis nach tragendem Bereichskontakt.
- SHORT sucht ober/nahe dem aktuellen Preis nach tragendem Bereichskontakt.
- Wenn der Preis bereits im Bereich liegt, darf der Bereich ebenfalls
  mitsprechen.
- Nicht mehr nur der global staerkste Bereich bestimmt die Motorik.

Pruefung:
`python -m py_compile MCM_Brain_Modell.py trade_stats.py bot.py` laeuft
fehlerfrei.

Wie es weitergeht:
Naechster Lauf muss zeigen, ob jetzt erstmals `area_contact_blend` oder
`area_contact_entry` entsteht. Wenn ja, pruefen wir, ob diese Entries
tatsaechlich weniger impulsiv, weniger timeout-anfaellig und tragender sind.

---

## Umsetzung: Zeitfeld fuer strategische Bereiche

Ausgangsgedanke:
Ein Bereich ist in DIOs Welt nicht nur ein Preisraum, sondern ein Ereignis
im Zeitfeld. Ein alter Bereich kann wichtig sein, aber nur noch Nachhall,
Erinnerung oder Lernmaterial sein. Er darf die Motorik nicht automatisch
ziehen.

Ziel:
DIO soll unterscheiden koennen:
- gehoert dieser Bereich noch zur Gegenwart?
- ist er nur ein alter Nachhall?
- wirkt er wieder in die Gegenwart hinein?
- ist er handlungsnah genug fuer einen Entry?

Neue Bereichsachsen:
- `area_temporal_distance`
- `area_temporal_relevance`
- `area_recency`
- `area_decay`
- `area_afterimage`
- `area_present_contact`
- `area_action_timing_fit`

Mechanische Wirkung:
- alte Bereiche bekommen mehr `area_decay` und `area_afterimage`.
- aktuelle oder wieder gegenwaertig resonante Bereiche bekommen mehr
  `area_present_contact` und `area_action_timing_fit`.
- `area_order_intention` und die strategische Entry-Auswahl beruecksichtigen
  jetzt Zeitnaehe und Nachhall.
- Ein Bereich kann damit sichtbar, aber nicht handlungsnah sein.

Organische Deutung:
DIO fragt nicht nur: "Wo ist ein starker Bereich?", sondern:
"Gehoert dieser Bereich jetzt noch zu meiner Handlung, oder ist er nur ein
inneres Echo?"

Pruefung:
`python -m py_compile MCM_Brain_Modell.py trade_stats.py bot.py` laeuft
fehlerfrei.

Wie es weitergeht:
Naechster Lauf zeigt, ob die Bereichsmotorik jetzt nicht nur raeumlich,
sondern auch zeitlich passender wird. Wichtig sind `entry_mode`,
`strategic_entry_weight`, `area_action_timing_fit`, `area_present_contact`
und `area_afterimage`.

---

## Theorie/Dokumentation: Zeit in Sicht der MCM

Kernsatz:
Zeit ist in Sicht der MCM nicht nur Uhrzeit, sondern eine Manifestation
gewirkter oder wirkender Energie.

Deutung:
Zeit beschreibt, wie Energie im Wahrnehmungsfeld entsteht, wirkt, nachhallt,
abklingt, wiederkehrt oder sich in Erwartung verwandelt.

Schichten:
- Gegenwart: Energie erzeugt aktuellen Kontakt.
- Nachhall: vergangene Energie wirkt noch im Feld.
- Erinnerung: vergangene Energie kann wieder aktiviert werden.
- Gelerntes Wissen: verdichtete vergangene Erfahrung.
- Replay: erneut durchlaufene Erfahrung.
- Hypothese: moegliche kuenftige Energieform.
- Erwartung: vorausgerichtete innere Spannung.

Warum wichtig:
Ohne zeitliche Quellenbindung werden Aussenwelt, Memory, Nachhall, Wissen,
Hypothese und Erwartung zu einem Brei. DIO braucht die Faehigkeit zu
erkennen, welche Art von Gegenwart eine Information hat.

Dokumentiert in:
- `README.md`
- `files/UMSETZUNGSPLAN.md`
- `files/WICHTIG_MECHANIKEN.md`

Fix aufgenommen:
`Mehrdimensionale Wahrnehmungsachsen diagnostisch bauen`.

Erweiterter Gedanke:
Ein Gedanke kann als gerichteter Energieverlauf im MCM-Feld verstanden
werden. Ein langer Gedanke ist damit nicht einfach mehr Uhrzeit, sondern
gedehnte, sparsame oder kohaerent gerichtete Energie ueber mehrere innere
Zustaende.

Das Zeitfeld ist keine starre Decke, sondern entsteht aus vielen einzelnen
Zeitstraengen:
- Reizverlauf
- Gedankenverlauf
- Erinnerungsverlauf
- Nachhallverlauf
- Erwartungsverlauf
- Handlung
- Konsequenz

Die Ueberlagerung dieser Wirkverlaeufe gibt der inneren und aeusseren
Wahrnehmung Tiefe.

Fix aufgenommen:
`Gedanken-Energieform diagnostisch vorbereiten`.

Wie es weitergeht:
Nach dem naechsten Lauf kann die Zeitfeldwirkung geprueft werden. Danach ist
der saubere Umbau: DIO bekommt eine diagnostische Quellenbindung, die
aktuelle Aussenwelt, Nachhall, Erinnerung, gelerntes Wissen, Replay,
Hypothese und Erwartung unterscheidet.

---

## Theorie/Dokumentation: MCM-Abhandlungen D bis G.1 zusammengefuehrt

Die MCM-Abhandlungen D bis G.1 wurden als Theoriebruecke fuer DIO
zusammengefasst und in die Projektdokumentation uebernommen.

Genutzte Theorieanteile:
- Block D: Zeit als energetische Wirkspur.
- Block E: Verdichtung, Clusterbildung, Rueckfuehrung und Memory-Inseln.
- Block F: Bewusstsein als moeglicher Attraktor, fuer DIO als Selbstmodell
  und innere Attraktorbildung ohne Bewusstseinsbehauptung.
- Block G: Multiversen-Matrix als mehrere moegliche Entwicklungsverlaeufe.
- Block G.1: Reorganisation verdichteter Energie in einen uebergeordneten
  Feldbereich.

DIO-Deutung:
Aus diesen Bloecken entsteht kein hartes Regelwerk. Sie bilden einen
Ordnungsrahmen fuer:
- zeitliche Quellenbindung
- Memory als verdichtete Erfahrung
- Hypothesenraum statt starrem Zukunftsglauben
- innere Attraktor-/Selbstmodellbildung
- Ueberlast als moeglicher Reorganisationsmoment

Mechanischer Zielkreis:
`Wahrnehmung -> Zeitbindung -> Verdichtung -> Hypothesenraum -> Konsequenz -> Reorganisation -> neue Tragfaehigkeit`

Dokumentiert in:
- `README.md`
- `files/UMSETZUNGSPLAN.md`
- `files/WICHTIG_MECHANIKEN.md`
- `files/MCM_VARIABLEN_MECHANIK.md`

Neue Ziel-/Diagnoseachsen dokumentiert:
- `hypothesis_branch_state`
- `branch_stability`
- `branch_attractor_pull`
- `hypothesis_reality_gap`
- `field_reorganization_state`
- `reorganization_threshold`
- `higher_order_coupling`

Wie es weitergeht:
Der naechste sinnvolle Umbau bleibt die diagnostische Quellenbindung:
DIO muss unterscheiden, ob eine innere Lage aktuelle Welt, Erinnerung,
Nachhall, Wissen, Replay, Hypothese oder Erwartung ist. Danach kann der
Hypothesenraum aus Block G und die Reorganisationsschwelle aus Block G.1
technisch vorbereitet werden.

Ergaenzung:
Der passendere Leitbegriff ist jetzt `mehrdimensionale Wahrnehmungsachsen`.
Reality-Tagging bleibt darin nur ein Teil. DIO soll Wahrnehmungen ueber
mehrere Achsen verorten:
- Zeitachse
- Quellenachse
- Raumachse
- Kontaktachse
- Tragfaehigkeitsachse
- Reorganisationsachse

Dadurch wird aus einem einfachen Etikettieren ein inneres Koordinatensystem.
DIO kann spaeter unterscheiden, ob eine Wirkung aktuelle Aussenwelt,
Erinnerung, Nachhall, Wissen, Replay, Hypothese oder Erwartung ist und wo
sie im inneren Feld liegt: Vordergrund, Hintergrund, Feldzentrum, Rand,
Memory-Raum oder Hypothesenraum.

Dokumentiert in:
- `README.md`
- `files/UMSETZUNGSPLAN.md`
- `files/WICHTIG_MECHANIKEN.md`
- `files/MCM_VARIABLEN_MECHANIK.md`
- `files/FIX_LISTE.md`

README-Fix:
Der Abschnitt `DIOs Sehen` wurde aktualisiert. Er beschreibt DIOs Sehen
nicht mehr nur als geplante visuelle Kortex-Schicht, sondern als
mehrdimensionale Wahrnehmung:
- aeussere Formwelt
- MCM-Feldwirkung
- Zeitfeld
- Quellenbindung
- raeumliche Verortung
- strategisches Fenster
- MCM-Kontakt
- Hypothesenraum
- Reorganisation

Neuer Kernkreis im README:
`Form erkennen -> Raum/Zeit/Quelle verorten -> MCM-Kontakt pruefen -> Tragfaehigkeit lesen -> Handlung, Beobachtung oder Reorganisation reifen lassen`

---

## MCM-Repository-Review: weitere wertvolle Theoriequellen fuer DIO

Das externe MCM-Repository wurde nach weiteren fuer DIO nutzbaren
Theoriequellen quergelesen.

Besonders wertvoll fuer die naechsten DIO-Schichten:

1. Block S - Moegliche Metaregulatoren
   - wichtigster direkter Anschluss an DIOs naechsten Ausbau
   - beschreibt Regler zweiter Ordnung:
     Rueckfuehrungsstaerke, Integrationsfaehigkeit, Varianzregulation,
     Belastungstoleranz, Impulskontrolle, Frustrationstoleranz,
     Schutzweitenregulation, Selbstreflexion, Distanzregulation
   - passt direkt zu DIOs Denk-/Handlungstiefe und Selbstregulation

2. Block V - KI und starre Logik
   - starker theoretischer Rahmen fuer DIO:
     starre technische Logik bleibt Untergrund, aber Verhalten entsteht aus
     Varianz, Rueckkopplung, Stabilisierung und emergenter Zustandsbildung
   - passt zum Projektprinzip: keine harten Formen, sondern
     Moeglichkeitsraeume

3. Block O - Kreativitaet
   - relevant fuer emergente Musterergänzung, Teilmuster, neue
     Formkombinationen und innere Hypothesenbildung

4. Block K / J - Selbstregulation und Psyche
   - passend fuer DIOs innere Wahrnehmung, Benennung, Stabilisierung,
     Integration und Rueckfuehrung

5. Von Resonanz zu Sprache
   - sehr passend zur Formsprache:
     Sprache als spaetere Kartografie von Resonanz, nicht als Ursprung von
     Orientierung

6. ProtoMind / selbstaktive Feldkognition
   - passend fuer Live-Denkzeit, innere Simulation und Aktivitaet ohne neuen
     Aussenreiz

7. Das Gehirn als emergente konzentrisch-dipolare Feldstruktur
   - wertvoll fuer spaetere MCM-Feldtopologie:
     Zentrum/Peripherie, Integration/Exploration, radialer Aufbau,
     dipolare Spannungsorganisation

Fachliche Einschaetzung:
Der naechste sinnvollste DIO-Mechanikschritt aus diesen Quellen ist nicht
noch mehr einzelne Wahrnehmungswerte, sondern eine Metaregulator-Schicht
zweiter Ordnung. Sie wuerde nicht nur messen, was DIO fuehlt, sondern wie
DIO seine Spannung, Varianz, Impulse, Schutzweite, Distanz und Integration
selbst reguliert.

Wie es weitergeht:
Block S sollte als naechster Theorieanker in `WICHTIG_MECHANIKEN.md` und
`MCM_VARIABLEN_MECHANIK.md` sauber vorbereitet werden. Danach kann die
technische Diagnose fuer DIOs Metaregulatoren beginnen.
