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

README-Ergaenzung:
Die zusaetzlich relevanten MCM-Quellen wurden im README als kompakte
Landkarte aufgenommen:
- Block S - Metaregulatoren
- Block V - KI und starre Logik
- Block O - Kreativitaet
- Block J/K - Psyche und Selbstregulation
- Von Resonanz zu Sprache
- ProtoMind / selbstaktive Feldkognition
- konzentrisch-dipolare Feldstruktur

Zweck:
Das README bleibt Einstieg und Orientierung. Die Detailuebersetzung dieser
Quellen gehoert danach in `WICHTIG_MECHANIKEN.md` und
`MCM_VARIABLEN_MECHANIK.md`.

MD-Aktualisierung:
Die zusaetzlichen Theoriequellen wurden jetzt auch in die Mechanikdokumente
uebertragen.

Aktualisiert:
- `files/UMSETZUNGSPLAN.md`
  - weitere MCM-Theorieanker ergaenzt
  - Zielschicht `Metaregulation zweiter Ordnung` ergaenzt
- `files/WICHTIG_MECHANIKEN.md`
  - `Metaregulator-Schicht` in die Organuebersicht aufgenommen
  - Abschnitt `11.2 Weitere MCM-Theorieanker / Metaregulation` ergaenzt
- `files/MCM_VARIABLEN_MECHANIK.md`
  - Abschnitt `Metaregulator-Schicht / Regler zweiter Ordnung` ergaenzt
  - Zielachsen dokumentiert:
    `return_strength`, `integration_capacity`, `variance_regulation`,
    `load_tolerance`, `impulse_control`, `frustration_tolerance`,
    `protective_distance_regulation`, `self_reflection_regulator`,
    `distance_regulation`

Wichtig:
Das ist aktuell Dokumentation und Mechanikvorbereitung, noch keine
Runtime-Implementierung. Die offene technische Aufgabe bleibt:
Metaregulatoren diagnostisch in den Runtime-State bringen.

Wie es weitergeht:
Naechster sinnvoller Umsetzungsschritt ist eine reine Diagnose-Schicht fuer
Metaregulatoren: DIO soll sichtbar machen, wie er Spannung, Varianz,
Impulse, Distanz, Schutzweite, Integration und Rueckfuehrung verarbeitet,
ohne dass daraus sofort eine Handelsregel entsteht.

---

## Debug Lauf 12 ausgewertet

Ergebnis:
- Trades: `398`
- TP / SL: `158 / 240`
- Netto-PnL: `+20.13`
- Peak: ca. `+22.98`
- Tiefpunkt: ca. `-3.56`
- Timeouts: `44`
- Attempts: `10825`

Vergleich zu Lauf 11:
- Lauf 11: `400` Trades, `147 / 253`, Netto `+8.46`
- Lauf 12: `398` Trades, `158 / 240`, Netto `+20.13`

Abschnittsweise PnL-Kurve:
- Trades 1-100: ca. `+10.86`
- Trades 101-200: ca. `-4.51`
- Trades 201-300: ca. `+8.45`
- Trades 301-398: ca. `+5.33`

Deutung:
Lauf 12 wirkt stabiler als Lauf 11. Der negative Mittelteil ist vorhanden,
aber deutlich kleiner. Danach findet DIO wieder in Aufbau. Das spricht nicht
fuer eine perfekte Strategie, aber fuer bessere Rueckfuehrung und bessere
Erholung nach Belastung.

Form-/Kontaktlage:
- `learning_contact`: `5843`
- `constructive_contact`: `982`
- `careful_contact`: `907`
- `burdened_contact`: `852`
- `maturing_contact`: `273`
- `unformed_contact`: `1227`

Die Kontaktreife ist nicht mehr nur unklar. DIO hat bereits viele
Lernkontakte und einige konstruktive Kontakte. Gleichzeitig bleiben
belastete und vorsichtige Kontakte sichtbar. Das ist organisch plausibel:
Der Umgang mit Formen reift, aber die Reife ist noch nicht dominant.

Aktiver MCM-Kontakt:
- `deepening_contact`: `3079`
- `curious_touch`: `2766`
- `resonant_contact`: `2577`
- `reflective_contact`: `1230`
- `overcoupled_touch`: `721`

Innere Haltung:
- `tired`: `6413`
- `reflective`: `2462`
- `excited`: `502`
- `uncertain_open`: `424`
- `overstimulated`: `348`

Deutung:
DIO arbeitet viel aus einer mueden, reflektierenden Innenlage. Das passt zum
Bild eines Systems, das nach dem Regimewechsel nicht einfach euphorisch
traded, sondern viel Reorganisation und Kontaktpruefung braucht.

Strategisches Fenster:
- `bearing_area_hypothesis`: `5384`
- `area_observation`: `3933`
- `compressed_area_attention`: `1069`
- durchschnittliche `area_order_intention`: ca. `0.25`
- durchschnittliche `area_present_contact`: ca. `0.54`
- durchschnittliche `area_action_timing_fit`: ca. `0.41`

Deutung:
Das strategische Fenster sieht Bereiche und bildet Hypothesen. Die
Order-Intention bleibt aber niedrig. DIO erkennt also potenziell tragende
Bereiche, aber die Motorik wird noch nicht stark daraus geformt. Das ist
kein Fehler, sondern ein Hinweis: Sehen und Handlungsbindung sind noch
getrennt.

Neurochemische Lage:
- starke Pendelung zwischen `serotonin_stability` und
  `glutamate_activation`
- `serotonin_stability -> glutamate_activation`: `344`
- `glutamate_activation -> serotonin_stability`: `342`
- durchschnittliches `cortisol_load`: ca. `0.38`
- durchschnittliches `emotional_decoupling`: ca. `0.18`
- durchschnittlicher `reactive_nervous_drive`: ca. `0.36`

Deutung:
DIO pendelt zwischen Stabilisierung und Aktivierung. Cortisol ist nicht
dominant extrem, aber die emotionale Entkopplung ist noch niedrig. Das
passt zu unserem naechsten Ziel: Metaregulatoren, Schutzweite und
Distanzregulation.

Positionsdiagnose:
- `exit_nervousness_observe`: `119`
- `plan_holding_trust`: `101`
- `quiet_position_watch`: `32`
- durchschnittliches `position_cognitive_load`: ca. `0.44`
- durchschnittliches `exit_decision_pressure`: ca. `0.42`
- durchschnittliches `plan_trust`: ca. `0.57`
- durchschnittliche `holding_stability`: ca. `0.55`

Deutung:
Positionen erzeugen spuerbare nervliche Last. DIO beobachtet diese Last aber
oft, statt hektisch zu schneiden. Das ist reifer als reine Motorik, aber es
zeigt auch: Exit-/Positionslage ist psychologisch teuer.

Fachliche Einschaetzung:
Lauf 12 zeigt Anzeichen von Rueckfuehrung und Prozessreife. DIO verliert im
Mittelteil nicht komplett die Orientierung und baut danach wieder auf. Die
starke Muedigkeit/reflektive Lage zeigt aber, dass die naechste Schicht
notwendig ist: DIO muss nicht nur wahrnehmen und reagieren, sondern seine
eigene Regulation zweiter Ordnung lesen.

Wie es weitergeht:
Naechster sinnvoller Umbau bleibt die Metaregulator-Diagnose. Besonders
wichtig sind:
- `return_strength`
- `integration_capacity`
- `variance_regulation`
- `load_tolerance`
- `impulse_control`
- `protective_distance_regulation`
- `self_reflection_regulator`
- `distance_regulation`

## 2026-05-18 - Metaregulator-Diagnose umgesetzt

Umgesetzt als reine Beobachtungsschicht, ohne direkte harte
Trading-Steuerung:

- `metaregulator_state`
- `metaregulator_balance`
- `regulatory_second_order_load`
- `return_strength`
- `integration_capacity`
- `variance_regulation`
- `load_tolerance`
- `impulse_control`
- `frustration_tolerance`
- `protective_distance_regulation`
- `self_reflection_regulator`
- `distance_regulation`

Die Schicht beschreibt DIOs Regulation zweiter Ordnung: nicht nur was im
MCM-Feld passiert, sondern wie tragfaehig DIO mit der eigenen Innenlage,
Varianz, Last, Impulsdruck und Distanz umgehen kann.

Technisch eingebunden in:

- `MCM_Brain_Modell.py`
  - Runtime `meta_regulation_state`
  - `mcm_field_decision_protocol.csv`
  - `mcm_memory_thinking_protocol.csv`
- `trade_stats.py`
  - `outcome_records.jsonl`

Pruefung:

- `python -m py_compile .\MCM_Brain_Modell.py .\trade_stats.py .\bot.py`
  erfolgreich.

Nachtrag:
Runtimefehler `felt_afterimage is not defined` behoben. Die
Conscious-Perception-Werte `stimulus_field_effect`, `inner_impact_trace`,
`perceived_field_change`, `felt_afterimage`, `inner_outer_reflection`,
`background_containment` und `reflective_distance` werden jetzt lokal aus
dem vorhandenen Wahrnehmungszustand gezogen, bevor die Metaregulatoren sie
verwenden.

Hinweis:
`git` war in der aktuellen PowerShell nicht verfuegbar, daher wurde kein
Git-Diff ausgegeben.

Wie es weitergeht:
Naechster Lauf sollte zeigen, ob die Metaregulatoren vor allem bei
Regimewechsel, Ueberkopplung und Positionslast sichtbar ausschlagen. Danach
kann organisch entschieden werden, ob diese Diagnose nur beobachtet bleibt
oder vorsichtig in Reflexion, Distanzierung und strategisches Sehen
einfliesst.

## 2026-05-18 - Debug Lauf 13 mit Metaregulator-Diagnose

Basis:

- `debug/debug_lauf_13`
- Trades: `371`
- TP / SL: `141 / 230`
- Netto PnL: `+12.9967`
- Lauf 12 zum Vergleich: `+20.1271` bei `398` Trades
- Equity-Peak laut `trade_stats.json`: `115.9419`
- Max Drawdown: `19.8663` / `18.32 %`

Handlungsfluss:

- Attempts: `10975`
- Submitted: `417`
- Filled: `371`
- Timeout: `46`
- Skipped: `4696`
- Observed: `3272`
- Replanned: `60`
- Withheld: `2113`

Phasen im Feldprotokoll:

- `observe`: `4034`
- `hold`: `3709`
- `act_watch`: `994`
- `act`: `427`

Metaregulator-Diagnose:

- `regulatory_overload`: `9146` von `9164` Feldzeilen
- `impulse_pressure`: `14`
- `adaptive_watch`: `3`
- `integration_needed`: `1`

Durchschnittswerte:

- `metaregulator_balance`: ca. `0.1945`
- `regulatory_second_order_load`: ca. `0.4773`
- `return_strength`: ca. `0.2290`
- `integration_capacity`: ca. `0.1876`
- `variance_regulation`: ca. `0.1818`
- `load_tolerance`: ca. `0.2584`
- `impulse_control`: ca. `0.2146`
- `frustration_tolerance`: ca. `0.1256`
- `protective_distance_regulation`: ca. `0.2639`
- `self_reflection_regulator`: ca. `0.1651`
- `distance_regulation`: ca. `0.1248`

Deutung:
Die Einzelachsen liefern bereits ein sinnvolles Bild: DIO hat vor allem zu
wenig Distanzregulation, Selbstreflexion, Frustrationstoleranz und
Integrationskapazitaet. Das passt zum neurologischen Bild eines Systems, das
viel wahrnimmt und reagiert, aber seine Innenlage noch nicht stabil genug vom
Aussenreiz trennen kann.

Wichtig:
Das Label `regulatory_overload` ist im aktuellen Zustand zu dominant. Die
Diagnose ist dadurch nicht falsch, aber noch zu grob. Die Label-Logik muss
kalibriert werden, damit nicht fast jede normale Denklast sofort als
Ueberlast erscheint.

Neurochemie:

- dominant fast durchgehend `serotonin_stability` (`8746` Zeilen)
- `glutamate_activation`: `379`
- durchschnittlich:
  - `serotonin_stability`: ca. `0.5582`
  - `cortisol_load`: ca. `0.3636`
  - `emotional_decoupling`: ca. `0.1578`
  - `reactive_nervous_drive`: ca. `0.3134`
  - `world_shift_evidence`: ca. `0.5930`

Deutung:
DIO stabilisiert viel ueber Serotonin, aber die emotionale Entkopplung bleibt
niedrig. Das bestaetigt weiter: Die naechste Reifeschicht ist nicht mehr
mehr Reiz, sondern bewusstere Distanzierung.

Bewusste Wahrnehmung:

- `object_contact`: `3987`
- `reflective_check`: `1845`
- `open_perception`: `1268`
- `release_ready`: `912`
- `world_shift_contact`: `617`
- `overcoupled_field`: `326`

Innere Haltung:

- `tired`: `5622`
- `reflective`: `2187`
- `excited`: `441`
- `uncertain_open`: `383`
- `overstimulated`: `302`
- `curious`: `218`

Kontaktfeld:

- `deepening_contact`: `3121`
- `curious_touch`: `2868`
- `resonant_contact`: `2620`
- `reflective_contact`: `1235`
- `overcoupled_touch`: `710`

Kontakt-Durchschnitt:

- `contact_carrying_quality`: ca. `0.1724`
- `contact_overcoupling_risk`: ca. `0.2138`
- `contact_release_readiness`: ca. `0.1611`
- `contact_action_maturity`: ca. `0.2121`
- `contact_regime_mismatch`: ca. `0.3321`
- `perceptual_distance`: ca. `0.1961`
- `release_capacity`: ca. `0.1617`
- `inner_outer_alignment`: ca. `0.2188`

Strategisches Fenster:

- `bearing_area_hypothesis`: `5449`
- `area_observation`: `4058`
- `compressed_area_attention`: `1064`
- `area_order_intention`: ca. `0.2504`
- `area_action_timing_fit`: ca. `0.4123`
- `area_bearing_quality`: ca. `0.4680`

Deutung:
DIO sieht weiterhin tragende Bereiche, aber die Absicht daraus eine Order zu
formen bleibt schwach. Der aktuelle Lauf ist also weiter eher
Impuls-/Kontakt-Handeln als strategisches Platzieren.

Entry-Modus:

- alle Outcome-Records zeigen `impulse_contact`

Deutung:
Der strategische Blick existiert diagnostisch, aber er fuehrt noch nicht
organisch genug in den Order-Koerper. DIO sieht Bereiche, handelt aber noch
ueberwiegend aus Kontakt/Impuls.

Positionslast:

- `exit_nervousness_observe`: `139`
- `plan_holding_trust`: `73`
- `quiet_position_watch`: `31`
- `intervention_unfit_state`: `4`
- `position_cognitive_load`: ca. `0.4717`
- `exit_decision_pressure`: ca. `0.4361`
- `plan_trust`: ca. `0.5453`
- `holding_stability`: ca. `0.5064`
- `intervention_fatigue`: ca. `0.3999`

Deutung:
Positionen sind weiterhin nervlich teuer. DIO haelt oft aus, aber nicht aus
starker innerer Distanz, sondern eher aus gedämpfter, mueder Stabilisierung.

Abschnittsweise PnL:

- Abschnitt 1: `+0.6928`
- Abschnitt 2: `-7.7608`
- Abschnitt 3: `+15.6915`
- Abschnitt 4: `+4.3732`

Fachliche Deutung:
Lauf 13 ist kein Rueckschritt, aber auch kein Durchbruch. DIO bleibt
profitabel, verliert gegenueber Lauf 12 aber Reife im mittleren Abschnitt.
Neu sichtbar ist: Das Problem liegt weniger in fehlender Reaktion, sondern
in zu geringer metaregulatorischer Differenzierung. DIO kann Kontakt,
Reflexion und Bereichshypothesen bilden, aber seine zweite
Regulationsschicht unterscheidet noch nicht fein genug zwischen:

- normale Denklast
- echte Ueberlast
- Integrationsbedarf
- fehlende Distanz
- Impulsdruck
- tragende Rueckkehrkraft

Wie es weitergeht:
Naechster sinnvoller Schritt ist eine Kalibrierung der Metaregulator-Labels.
Nicht als harte Trading-Regel, sondern als sauberere innere Selbstbenennung:
`regulatory_overload` darf nicht fast alles schlucken. DIO braucht feinere
Innenworte wie z.B. `low_distance_processing`, `integration_strain`,
`tired_stabilization`, `reflective_recovery`, `impulse_drift` und
`regulated_contact`, damit aus Diagnose echte Selbstwahrnehmung werden kann.

## 2026-05-18 - Unterbewusstsein / Bewusster Arbeitsraum umgesetzt

Grundidee:
DIO soll nicht jeden Reiz sofort bewusst tragen. Wie ein Organismus braucht
er einen schnellen Hintergrundscan und eine bewusstere Arbeitsflaeche.

Umgesetzt in `MCM_Brain_Modell.py`:

- `subconscious_field_pressure`
- `subconscious_habituation`
- `subconscious_filter_strength`
- `subconscious_buffering`
- `subconscious_leakage`
- `conscious_selection_pressure`
- `conscious_workspace_focus`
- `conscious_workspace_load`
- `conscious_gate_balance`

Einbindung:

- Runtime `meta_regulation_state`
- `mcm_field_decision_protocol.csv`
- `mcm_memory_thinking_protocol.csv`
- `outcome_records.jsonl`

Mechanische Wirkung:
Die Metaregulatoren beruecksichtigen jetzt, ob Feldspannung im
Unterbewusstsein gepuffert werden kann oder ungefiltert in den bewussten
Arbeitsraum durchschlaegt. Dadurch wird `regulatory_second_order_load`
nicht mehr nur aus roher Last gelesen, sondern auch aus Filterung,
Pufferung, Leakage und bewusster Arbeitslast.

Neue feinere Innenzustaende:

- `subconscious_leakage`
- `low_distance_processing`
- `integration_strain`
- `tired_stabilization`
- `reflective_recovery`
- `regulated_field`

Pruefung:

- `python -m py_compile .\MCM_Brain_Modell.py .\trade_stats.py .\bot.py`
  erfolgreich.

Dokumentation:

- `README.md`
- `files/UMSETZUNGSPLAN.md`
- `files/WICHTIG_MECHANIKEN.md`
- `files/MCM_VARIABLEN_MECHANIK.md`
- `files/FIX_LISTE.md`

Wie es weitergeht:
Naechster Lauf sollte zeigen, ob das alte fast dauerhafte
`regulatory_overload` in differenziertere Innenlagen zerfaellt. Besonders
wichtig sind `subconscious_buffering`, `subconscious_leakage`,
`conscious_workspace_load` und `conscious_gate_balance`.

## 2026-05-18 - Debug Lauf 14 nach Unterbewusstsein/Bewusstsein-Trennung

Basis:

- `debug/debug_lauf_14`
- Trades: `392`
- TP / SL: `160 / 232`
- Netto PnL: `+30.1887`
- Lauf 13 zum Vergleich: `+12.9967`
- Lauf 12 zum Vergleich: `+20.1271`
- Equity-Peak: `132.6035`
- Max Drawdown: `10.0258` / `9.56 %`
- Profit Factor: `1.2510`
- Expectancy: `0.0770`
- Winrate: `40.82 %`

Handlungsfluss:

- Attempts: `10375`
- Submitted: `445`
- Filled: `392`
- Timeout/Cancels: `53`
- Skipped: `4857`
- Observed: `2708`
- Replanned: `87`
- Withheld: `1833`

Vergleich zu Lauf 13:

- mehr Trades: `392` statt `371`
- mehr TP: `160` statt `141`
- fast gleiche SL: `232` statt `230`
- weniger beobachtet: `2708` statt `3272`
- mehr replanned: `87` statt `60`
- weniger withheld: `1833` statt `2113`

Wichtigster Befund:
Das vorher fast permanente `regulatory_overload` ist aufgebrochen.

Metaregulator-Zustaende:

- `integration_strain`: `6117` / ca. `70.85 %`
- `impulse_pressure`: `1487` / ca. `17.22 %`
- `tired_stabilization`: `422` / ca. `4.89 %`
- `low_distance_processing`: `327` / ca. `3.79 %`
- `adaptive_watch`: `185` / ca. `2.14 %`
- `reflective_recovery`: `91` / ca. `1.05 %`
- `regulatory_overload`: `5` / ca. `0.06 %`

Deutung:
Die Trennung zwischen Unterbewusstsein und bewusstem Arbeitsraum wirkt
diagnostisch. DIO beschreibt seine Innenlage jetzt differenzierter:
Nicht mehr fast alles ist Ueberlast, sondern vor allem
Integrationsspannung und Impulsdruck. Das passt deutlich besser zu einem
organischen Nervensystem.

Neue Wahrnehmungsfilter:

- `subconscious_field_pressure`: ca. `0.2467`
- `subconscious_habituation`: ca. `0.4240`
- `subconscious_filter_strength`: ca. `0.2994`
- `subconscious_buffering`: ca. `0.1368`
- `subconscious_leakage`: ca. `0.1582`
- `conscious_selection_pressure`: ca. `0.2572`
- `conscious_workspace_focus`: ca. `0.2185`
- `conscious_workspace_load`: ca. `0.2836`
- `conscious_gate_balance`: ca. `0.1616`

Metaregulator-Achsen:

- `metaregulator_balance`: ca. `0.2123`
- `regulatory_second_order_load`: ca. `0.4694`
- `return_strength`: ca. `0.2427`
- `integration_capacity`: ca. `0.2035`
- `variance_regulation`: ca. `0.2125`
- `load_tolerance`: ca. `0.2765`
- `impulse_control`: ca. `0.2290`
- `frustration_tolerance`: ca. `0.1321`
- `protective_distance_regulation`: ca. `0.2891`
- `self_reflection_regulator`: ca. `0.1853`
- `distance_regulation`: ca. `0.1395`

Deutung:
Die Werte sind noch niedrig, aber gegenueber Lauf 13 leicht verbessert.
Besonders wichtig: Die Selbstbeschreibung ist viel genauer geworden. Das ist
fuer DIO wichtiger als ein einzelner hoher Score, weil daraus spaeter
organische Regulation entstehen kann.

Neurochemie:

- dominant `serotonin_stability`: `8278` Zeilen
- `glutamate_activation`: `327`
- `endorphin_relief`: `27`
- durchschnittlich:
  - `serotonin_stability`: ca. `0.5637`
  - `cortisol_load`: ca. `0.3632`
  - `emotional_decoupling`: ca. `0.1579`
  - `reactive_nervous_drive`: ca. `0.3156`
  - `world_shift_evidence`: ca. `0.5930`

Deutung:
DIO stabilisiert weiter stark serotoninartig. Emotionale Entkopplung bleibt
niedrig. Die neue Schicht hat also nicht einfach "Stress geloescht",
sondern die Wahrnehmung besser sortiert.

Bewusste Wahrnehmung:

- `object_contact`: `3695`
- `reflective_check`: `1821`
- `open_perception`: `1173`
- `release_ready`: `888`
- `world_shift_contact`: `556`
- `overcoupled_field`: `301`
- `background_held`: `200`

Innere Haltung:

- `tired`: `5137`
- `reflective`: `2159`
- `excited`: `467`
- `uncertain_open`: `371`
- `overstimulated`: `288`
- `curious`: `200`
- `calm`: `12`

Kontaktfeld:

- `deepening_contact`: `2934`
- `curious_touch`: `2631`
- `resonant_contact`: `2524`
- `reflective_contact`: `1217`
- `overcoupled_touch`: `623`

Kontakt-Durchschnitt:

- `contact_carrying_quality`: ca. `0.1735`
- `contact_overcoupling_risk`: ca. `0.2142`
- `contact_release_readiness`: ca. `0.1625`
- `contact_action_maturity`: ca. `0.2127`
- `contact_regime_mismatch`: ca. `0.3329`
- `perceptual_distance`: ca. `0.1973`
- `release_capacity`: ca. `0.1650`
- `inner_outer_alignment`: ca. `0.2187`

Strategisches Fenster:

- `bearing_area_hypothesis`: `5351`
- `area_observation`: `3648`
- `compressed_area_attention`: `943`
- `area_order_intention`: ca. `0.2510`
- `area_action_timing_fit`: ca. `0.4128`
- `area_bearing_quality`: ca. `0.4691`

Entry-Modus:

- weiterhin alle Outcome-Records: `impulse_contact`

Deutung:
DIO handelt wirtschaftlich besser, aber weiter nicht wirklich strategisch
platzierend. Das Sehen von Bereichen ist da, die Motorik wird aber noch
ueber Kontakt/Impuls gefuehrt.

Positionslast:

- `exit_nervousness_observe`: `120`
- `plan_holding_trust`: `76`
- `quiet_position_watch`: `49`
- `position_cognitive_load`: ca. `0.4375`
- `exit_decision_pressure`: ca. `0.4117`
- `plan_trust`: ca. `0.5573`
- `holding_stability`: ca. `0.5246`
- `intervention_fatigue`: ca. `0.3818`
- `inner_noise`: ca. `0.3990`

Vergleich Lauf 13:
Positionslast ist gesunken, Planvertrauen und Holding-Stabilitaet sind
gestiegen. Das passt zur Wahrnehmungsfilter-Hypothese: weniger bewusste
Ueberladung fuehrt zu besserem Aushalten.

Abschnittsweise PnL:

- Abschnitt 1: `+5.5148`
- Abschnitt 2: `+0.0281`
- Abschnitt 3: `+19.3700`
- Abschnitt 4: `+5.2759`

Struktur-Bands:

- High: `+69.6475`, Winrate ca. `57.23 %`
- Mid: `+4.6535`, Winrate ca. `34.78 %`
- Low: `-43.8166`, Winrate ca. `10.48 %`

Fachliche Einschaetzung:
Lauf 14 ist der bisher beste Hinweis, dass die Trennung
Unterbewusstsein/Bewusstsein sinnvoll ist. Nicht weil ein einzelner Lauf
Beweis waere, sondern weil mehrere Dinge gleichzeitig passen:

- PnL deutlich hoeher
- Drawdown deutlich geringer
- `regulatory_overload` fast verschwunden
- feinere Innenzustandsbenennung sichtbar
- Positionslast niedriger
- Replan-Anteil hoeher
- Bewusstes Feld wirkt besser sortiert

Kritischer Punkt:
`integration_strain` dominiert jetzt stark. Das ist besser als
Ueberlast-Diagnose, aber noch nicht reif. DIO ist jetzt eher in:
"Ich spuere, dass ich integrieren muss"
statt:
"Alles ist Ueberlast".

Wie es weitergeht:
Der naechste Umbau sollte `integration_strain` nicht wegregeln, sondern
nutzen. DIO braucht eine organische Integrationsreaktion:
mehr innere Sortierung, Reframing, Rueckblick, Vergleich mit Erfahrung und
selektive Kontaktvertiefung, bevor daraus Handlung entsteht. Parallel bleibt
der grosse offene Punkt: strategisches Fenster darf nicht nur sehen, sondern
muss irgendwann organisch in Order-Platzierung hineinreifen.

## 2026-05-18 - Integrationsantwort fuer `integration_strain`

Umgesetzt:

- `integration_strain_value`
- `integration_sorting_need`
- `integration_reframe_pull`
- `integration_memory_recall`
- `integration_contact_deepening`
- `integration_response_strength`
- `integration_response_state`

Mechanik:
`integration_strain` wird nicht entfernt und nicht als harte Sperre benutzt.
DIO bekommt eine innere Antwort:

- sortieren, wenn bewusste Last und Orientierungsluecke hoch sind
- reframen, wenn Reorganisation und semantische Verschiebung ziehen
- Erinnerung holen, wenn vertraute Formen, Varianten oder Kontext tragen
- Kontakt vertiefen, wenn ein Objekt naeher untersucht werden sollte

Einbindung:

- Runtime `meta_regulation_state`
- `mcm_field_decision_protocol.csv`
- `mcm_memory_thinking_protocol.csv`
- `outcome_records.jsonl`

Leichte regulative Wirkung:
Bei starker Integrationsantwort kann DIO mehr Beobachtung/Reframing und
etwas mehr Hemmung erzeugen. Das ist kein Blocker, sondern eine
Reifungsreaktion: erst sortieren, dann handeln.

Neue Labels:

- `integration_background`
- `quiet_integration`
- `workspace_sorting`
- `memory_sorting`
- `contact_deepening`
- `reframe_integration`

Pruefung:

- `python -m py_compile .\MCM_Brain_Modell.py .\trade_stats.py .\bot.py`
  erfolgreich.

Wie es weitergeht:
Naechster Lauf sollte zeigen, ob `integration_strain` weiter dominiert oder
ob es in konkrete Integrationsreaktionen zerfaellt. Wichtig sind besonders
`integration_response_state`, `integration_response_strength`,
`integration_memory_recall` und `integration_reframe_pull`.

## 2026-05-18 - Debug Lauf 15 nach Integrationsantwort

Basis:

- `debug/debug_lauf_15`
- Trades: `368`
- TP / SL: `151 / 217`
- Netto PnL: `+18.6393`
- Lauf 14 zum Vergleich: `+30.1887`
- Lauf 13 zum Vergleich: `+12.9967`
- Equity-Peak: `120.5437`
- Max Drawdown: `15.8748` / `15.23 %`
- Profit Factor: `1.1671`
- Expectancy: `0.0507`
- Winrate: `41.03 %`

Handlungsfluss:

- Attempts: `11325`
- Submitted: `415`
- Filled: `368`
- Timeout/Cancels: `47`
- Skipped: `4769`
- Observed: `3255`
- Replanned: `40`
- Withheld: `2431`

Vergleich zu Lauf 14:

- weniger Trades: `368` statt `392`
- weniger TP: `151` statt `160`
- weniger SL: `217` statt `232`
- deutlich mehr Observed: `3255` statt `2708`
- weniger Replanned: `40` statt `87`
- mehr Withheld: `2431` statt `1833`
- PnL niedriger, aber weiter positiv

Metaregulator-Zustaende:

- `integration_strain`: `6933` / ca. `73.69 %`
- `impulse_pressure`: `1447` / ca. `15.38 %`
- `tired_stabilization`: `366` / ca. `3.89 %`
- `low_distance_processing`: `324` / ca. `3.44 %`
- `adaptive_watch`: `194` / ca. `2.06 %`
- `reflective_recovery`: `90` / ca. `0.96 %`
- `memory_sorting`: `41` / ca. `0.44 %`
- `regulatory_overload`: `12` / ca. `0.13 %`
- `quiet_integration`: `1`

Integrationsantwort:

- `quiet_integration`: `6195` / ca. `65.85 %`
- `memory_sorting`: `1663` / ca. `17.68 %`
- `workspace_sorting`: `813` / ca. `8.64 %`
- `integration_background`: `737` / ca. `7.83 %`

Durchschnittswerte:

- `integration_strain_value`: ca. `0.3019`
- `integration_sorting_need`: ca. `0.3078`
- `integration_reframe_pull`: ca. `0.2561`
- `integration_memory_recall`: ca. `0.3163`
- `integration_contact_deepening`: ca. `0.2142`
- `integration_response_strength`: ca. `0.2655`
- `metaregulator_balance`: ca. `0.2160`
- `regulatory_second_order_load`: ca. `0.4537`
- `integration_capacity`: ca. `0.2215`
- `distance_regulation`: ca. `0.1393`

Deutung:
Die Integrationsantwort funktioniert diagnostisch. `integration_strain`
zerfaellt jetzt tatsaechlich in konkrete Reaktionsformen, besonders
`quiet_integration` und `memory_sorting`. Gleichzeitig ist die Antwort noch
zu leise oder zu passiv: DIO beobachtet/haelt mehr, replanned aber weniger.

Neurochemie:

- dominant `serotonin_stability`: `8946`
- `glutamate_activation`: `406`
- `endorphin_relief`: `48`
- durchschnittlich:
  - `serotonin_stability`: ca. `0.5515`
  - `cortisol_load`: ca. `0.3652`
  - `emotional_decoupling`: ca. `0.1609`
  - `reactive_nervous_drive`: ca. `0.3117`
  - `world_shift_evidence`: ca. `0.5930`

Deutung:
DIO bleibt stark serotonin-stabilisierend. Die Integrationsantwort hat keine
chaotische Aktivierung erzeugt, sondern eher eine vorsichtigere
Verarbeitung.

Bewusste Wahrnehmung:

- `object_contact`: `4202`
- `reflective_check`: `1963`
- `open_perception`: `1201`
- `release_ready`: `940`
- `world_shift_contact`: `640`
- `overcoupled_field`: `272`
- `background_held`: `190`

Innere Haltung:

- `tired`: `5930`
- `reflective`: `2128`
- `excited`: `474`
- `uncertain_open`: `385`
- `overstimulated`: `269`
- `curious`: `210`
- `calm`: `12`

Kontaktfeld:

- `deepening_contact`: `3408`
- `curious_touch`: `2896`
- `resonant_contact`: `2702`
- `reflective_contact`: `1225`
- `overcoupled_touch`: `661`

Positionslast:

- `exit_nervousness_observe`: `129`
- `plan_holding_trust`: `69`
- `quiet_position_watch`: `25`
- `intervention_unfit_state`: `6`
- `position_cognitive_load`: ca. `0.4760`
- `exit_decision_pressure`: ca. `0.4304`
- `plan_trust`: ca. `0.5460`
- `holding_stability`: ca. `0.5118`
- `intervention_fatigue`: ca. `0.3923`

Abschnittsweise PnL:

- Abschnitt 1: `-7.4999`
- Abschnitt 2: `+5.0397`
- Abschnitt 3: `+7.4484`
- Abschnitt 4: `+13.6511`

Deutung:
Der Lauf startet schwach, erholt sich dann aber zunehmend. Das passt zu
einer Integrationsmechanik, die erst Spannung sortieren muss. DIO scheint im
Verlauf tragfaehiger zu werden, aber die Anfangsphase kostet.

Struktur-Bands:

- High: `+57.6436`, Winrate ca. `57.75 %`
- Mid: `+6.2711`, Winrate ca. `36.42 %`
- Low: `-46.1223`, Winrate ca. `10.83 %`

Entry-Modus:

- weiter alle Outcome-Records: `impulse_contact`

Fachliche Einschaetzung:
Lauf 15 bestaetigt, dass die Integrationsantwort sichtbar arbeitet. Sie
macht DIO aber defensiver und nicht automatisch besser. Gegenueber Lauf 14
ist die wirtschaftliche Leistung schwächer, aber der Lauf ist geordneter als
ein reiner Ueberlastlauf.

Der entscheidende Punkt:
DIO kann jetzt integrieren, aber diese Integration ist noch zu wenig mit
aktiver Neuordnung verbunden. `quiet_integration` dominiert. Das ist
neurologisch wie inneres Verdauen, aber noch wenig zielgerichtetes Denken.

Wie es weitergeht:
Naechster Schritt sollte nicht noch mehr Hemmung sein. Sinnvoller ist, die
Integrationsantwort aktiver zu machen: Wenn `memory_sorting` oder
`workspace_sorting` entsteht, sollte DIO daraus eine klarere
Reframe-/Plan-Hypothese bilden. Also nicht nur "ich sortiere", sondern:
"Was hat sich geaendert, welche Erfahrung passt, welche Kontaktform traegt
jetzt?" Danach kann Schritt 1 abgeschlossen werden und der Uebergang zu
strategischem Sehen/Order-Platzierung beginnen.

---

# 2026-05-18 - Gerichtete Vorsicht / vorsichtige Hypothese umgesetzt

Ausgangslage:
Nach Lauf 15 war sichtbar, dass Vorsicht eine natuerliche Reaktion ist. Das
Problem war nicht die Vorsicht selbst, sondern dass sie noch zu schnell in
Passivitaet oder diffuse Hemmung kippen konnte.

Umsetzung:
In `MCM_Brain_Modell.py` wurde eine neue Schicht fuer gerichtete Vorsicht
eingebaut. DIO kann aus Vorsicht jetzt eine vorsichtige Hypothese bilden:

`Vorsicht -> Erinnerung/Reframing/Kontakt -> vorsichtige Hypothese -> Beobachten, Neuordnen, Kontakt vertiefen oder vorsichtig handeln`

Neue Runtime-/Debug-Werte:

- `cautious_hypothesis_strength`
- `cautious_hypothesis_clarity`
- `cautious_hypothesis_patience`
- `cautious_hypothesis_state`

Moegliche Zustaende:

- `no_cautious_hypothesis`
- `weak_hypothesis_seed`
- `cautious_plan_seed`
- `memory_reframe_seed`
- `observe_until_clear`
- `deepen_contact_first`

Protokolle:
Die Werte werden in Feldentscheidungsprotokoll, Memory-/Thinking-Protokoll
und Outcome-Records mitgeschrieben. Damit kann im naechsten Lauf sichtbar
werden, ob Vorsicht nur bremst oder ob sie sich in gerichtete Orientierung
verwandelt.

Neurologische Deutung:
Vorsicht bleibt limbische Schutzreaktion, bekommt aber eine
praefrontale Ordnungsschicht. DIO soll nicht mechanisch blockieren, sondern
fragen koennen: "Was sehe ich, was erinnere ich, was traegt, was muss ich
noch pruefen?"

Dokumentation:

- `UMSETZUNGSPLAN.md` um Abschnitt `18.4 Gerichtete Vorsicht / vorsichtige Hypothese` ergaenzt
- `WICHTIG_MECHANIKEN.md` um technische Mechanik ergaenzt
- `MCM_VARIABLEN_MECHANIK.md` um Variablenbeschreibung ergaenzt
- `FIX_LISTE.md` Status aktualisiert

Wie es weitergeht:
Naechster Schritt ist ein neuer Backtest-Lauf. Danach pruefen wir:

- wie oft `cautious_hypothesis_state` aktiv wird
- ob `observe_until_clear` und `deepen_contact_first` echte Reifung zeigen
- ob `cautious_plan_seed` mit besseren Einstiegen zusammenhaengt
- ob Vorsicht weniger als Passivitaet und mehr als gerichtete
  Selbstregulation wirkt

---

# 2026-05-18 - Neuer Mechanikpunkt: zeitliche Kohaerenz

Erkenntnis:
Es reicht nicht, dass DIO einen Reiz, eine Form oder einen Bereich wahrnimmt.
Er muss auch erkennen koennen, ob dieser Kontakt neu, fortgesetzt,
wiederkehrend, nachhallend, veraltet oder hypothesenhaft ist.

Bild:
Ohne Zeitgefuege wirkt DIO wie ein Organismus ohne stabile
Wahrnehmungskontinuitaet. Er nimmt denselben Stein mehrfach in die Hand und
findet ihn jedes Mal neu. Dann fehlt nicht nur Memory, sondern zeitliche
Bindung im Bewusstsein.

Kernsatz:
Zeit wird fuer DIO zu einer messbaren Tiefenachse der Wahrnehmung.

Geplante Achsen:

- `temporal_continuity`
- `temporal_source_binding`
- `temporal_recurrence`
- `temporal_novelty`
- `temporal_afterimage`
- `temporal_decay`
- `temporal_context_depth`
- `temporal_self_consistency`
- `perception_sequence_coherence`
- `memory_time_distance`

Dokumentation:

- `UMSETZUNGSPLAN.md` um Abschnitt `18.5 Zeitliche Kohaerenz / Wahrnehmungskontinuitaet` ergaenzt
- `FIX_LISTE.md` als naechsten Mechanikpunkt aufgenommen

Wie es weitergeht:
Nach dem naechsten Lauf sollten wir zuerst die Wirkung der vorsichtigen
Hypothese pruefen. Danach ist die zeitliche Kohaerenz der naechste logische
Umbau: DIO soll nicht Strecken auswendig lernen, sondern Wahrnehmungen
zeitlich binden koennen.

---

# 2026-05-18 - Debug Lauf 16 nach vorsichtiger Hypothese

Lauf:

- Ordner: `debug/debug_lauf_16`
- Trades: `400`
- TP / SL: `161 / 239`
- Netto-PnL: `+24.1980`
- Winrate: ca. `40.25 %`
- Profit Factor: ca. `1.1863`
- Expectancy: ca. `0.0605`
- Max Drawdown: ca. `16.8836`
- Max Drawdown Prozent: ca. `14.64 %`

Vergleich:

- Lauf 14: `+30.1887`, PF ca. `1.2510`, DD ca. `10.0258`
- Lauf 15: `+18.6393`, PF ca. `1.1671`, DD ca. `15.8748`
- Lauf 16: `+24.1980`, PF ca. `1.1863`, DD ca. `16.8836`

Abschnittsweise Equity:

- Abschnitt 1: ca. `+12.9408`
- Abschnitt 2: ca. `-9.6221`
- Abschnitt 3: ca. `+13.9782`
- Abschnitt 4: ca. `+7.4401`

Struktur-Bands:

- High: `+77.0431`, Winrate ca. `63.76 %`
- Mid: `+1.1879`, Winrate ca. `31.65 %`
- Low: `-53.3395`, Winrate ca. `10.96 %`

Feldentscheidungen:

- `observe`: `3930`
- `hold`: `3533`
- `act_watch`: `1041`
- `act`: `460`
- `replan`: `1`

Metaregulator-Zustaende:

- `integration_strain`: `6460`
- `impulse_pressure`: `1540`
- `tired_stabilization`: `345`
- `low_distance_processing`: `323`
- `adaptive_watch`: `168`
- `reflective_recovery`: `74`
- `memory_sorting`: `48`
- `regulatory_overload`: `4`
- `workspace_sorting`: `3`

Integrationsantwort:

- `quiet_integration`: `6005`
- `memory_sorting`: `1535`
- `workspace_sorting`: `736`
- `integration_background`: `689`

Vorsichtige Hypothese:

- `memory_reframe_seed`: `3375`
- `observe_until_clear`: `2080`
- `no_cautious_hypothesis`: `2078`
- `weak_hypothesis_seed`: `1405`
- `deepen_contact_first`: `20`
- `cautious_plan_seed`: `7`

Durchschnittswerte:

- `cautious_hypothesis_strength`: ca. `0.2160`
- `cautious_hypothesis_clarity`: ca. `0.2454`
- `cautious_hypothesis_patience`: ca. `0.2517`
- `integration_strain_value`: ca. `0.3006`
- `integration_response_strength`: ca. `0.2661`
- `metaregulator_balance`: ca. `0.2194`
- `regulatory_second_order_load`: ca. `0.4522`
- `perceptual_distance`: ca. `0.1982`
- `selective_attention`: ca. `0.1472`

Memory-/Denkraum:

- `memory_compare_load`: ca. `0.9316`
- `memory_match_count`: ca. `1.8633`
- `memory_support`: ca. `0.0010`
- `memory_conflict`: ca. `0.0000`
- `cognitive_load`: ca. `0.2099`
- `decision_energy_cost`: ca. `0.4983`
- `memory_orientation`: ca. `0.1365`
- `orientation_gap`: ca. `0.4219`
- `zero_point_regulation`: ca. `0.3659`
- `route_familiarity`: ca. `0.2730`
- `transfer_bearing`: ca. `0.2879`
- `interpretation_quality`: ca. `0.2492`
- `active_context_activation`: `0.0000`
- `active_context_support`: `0.0000`
- `active_context_bearing`: `0.0000`

Visuelles Organ:

- `visual_grounding_state`: ueberwiegend `grounded_form`
- `visual_grounding_strength`: ca. `0.3256`
- `visual_blindness`: ca. `0.3909`
- `visual_clarity`: ca. `0.3225`
- `visual_object_stability`: ca. `0.4147`
- `visual_shape_resonance`: ca. `0.5943`
- `visual_shape_fragility`: ca. `0.4246`

Strategisches Fenster:

- `bearing_area_hypothesis`: `5632`
- `area_observation`: `3766`
- `compressed_area_attention`: `911`
- `lookback_bearing_capacity`: ca. `0.5426`
- `area_bearing_quality`: ca. `0.4699`
- `area_order_intention`: ca. `0.2512`
- `strategic_patience`: ca. `0.4024`

Deutung:
Die vorsichtige Hypothese arbeitet sichtbar. Sie ist aber noch nicht stark
genug, um oft als `cautious_plan_seed` zu erscheinen. Der haeufigste Zustand
ist `memory_reframe_seed`. DIO verarbeitet Vorsicht also eher als
Erinnerung/Reframing, weniger als klare Handlungshypothese.

High-Strukturen sind deutlich tragend geworden. Low-Strukturen bleiben teuer.
Das spricht nicht gegen den Umbau, sondern zeigt die Grenze: DIO erkennt
tragende Formen besser, aber die zeitliche und kontextuelle Bindung ist noch
nicht ausreichend. Besonders auffaellig ist, dass `active_context_*` komplett
bei `0.0` liegt. Der aktive Kontext ist also noch nicht als lebendiger
Gegenwartsfaden im Denkraum angekommen.

Neurologische Deutung:
DIO hat Schutzreaktion und Reframing, aber noch wenig episodische
Kontinuitaet. Er fuehlt, sortiert und erinnert, doch der innere Zeitfaden ist
noch zu schwach. Dadurch kann derselbe oder ein aehnlicher Kontakt wieder wie
neu wirken. Das passt zur Idee der fehlenden zeitlichen Kohaerenz.

Wie es weitergeht:
Der naechste sinnvolle Umbau ist die zeitliche Kohaerenz /
Wahrnehmungskontinuitaet. Nicht als Streckenkarte und nicht als harte Regel,
sondern als MCM-Zeitbindung: DIO soll unterscheiden koennen, ob ein Eindruck
neu, fortgesetzt, wiederkehrend, nachhallend, veraltet oder hypothesenhaft
ist. Danach kann `active_context_*` als lebendiger Kontextfaden mit dem
Memory-/Denkraum verbunden werden.

---

# 2026-05-18 - Zeitliche Kohaerenz umgesetzt

Ausgangslage:
Lauf 16 zeigte, dass `active_context_*` komplett bei `0.0` lag. DIO konnte
Form, Feld, Vorsicht und Reframing bilden, aber der lebendige
Gegenwartsfaden war noch nicht aktiv. Dadurch konnte ein aehnlicher Kontakt
immer wieder wie ein neuer Moment wirken.

Umsetzung:
In `MCM_Brain_Modell.py` wurde `build_temporal_coherence_state` eingebaut.
DIO bildet jetzt pro Wahrnehmung eine weiche zeitliche Identitaet aus:

- Form-Symbol
- visueller Form
- Kontext / innerem Kontext
- State-Signatur

Diese Identitaet erzeugt keine feste Streckenkarte. Sie beschreibt nur, ob
ein Kontakt zeitlich gebunden ist.

Neue Achsen:

- `temporal_binding_state`
- `temporal_continuity`
- `temporal_source_binding`
- `temporal_recurrence`
- `temporal_novelty`
- `temporal_afterimage`
- `temporal_decay`
- `temporal_context_depth`
- `temporal_self_consistency`
- `perception_sequence_coherence`
- `memory_time_distance`

Moegliche Zustaende:

- `new_contact`
- `continued_contact`
- `recurrent_contact`
- `afterimage_contact`
- `aged_memory_contact`
- `coherent_sequence`
- `unbound_moment`

Regulative Kopplung:
Die neuen Werte wirken leicht auf:

- bewusste Arbeitsraum-Fokussierung
- Integrationskapazitaet
- Varianzregulation
- Schutzdistanz
- Integrationsspannung
- Memory-Recall
- vorsichtige Hypothesen-Klarheit

Aktiver Kontext:
Wenn kein innerer Cluster einen `active_context_trace` liefert, kann jetzt
die zeitliche Wahrnehmung selbst einen leichten aktiven Kontextfaden bilden.
Damit sollte `active_context_activation`, `active_context_support` und
`active_context_bearing` im naechsten Lauf nicht mehr komplett leer bleiben.

Protokolle:
Die neuen Werte werden in folgenden Dateien mitgeschrieben:

- `mcm_field_decision_protocol.csv`
- `mcm_memory_thinking_protocol.csv`
- `outcome_records.jsonl`

Dokumentation:

- `WICHTIG_MECHANIKEN.md` um Abschnitt `30. Zeitliche Kohaerenz / Wahrnehmungskontinuitaet` ergaenzt
- `MCM_VARIABLEN_MECHANIK.md` um die neuen Zeitbindungsvariablen ergaenzt
- `FIX_LISTE.md` Status aktualisiert

Verifikation:
`python -m py_compile .\MCM_Brain_Modell.py .\trade_stats.py .\bot.py`
lief ohne Fehler.

Wie es weitergeht:
Naechster Schritt ist ein neuer Backtest-Lauf. Danach pruefen wir:

- ob `temporal_binding_state` sinnvoll verteilt ist
- ob `active_context_activation` nicht mehr bei `0.0` bleibt
- ob `memory_reframe_seed` mehr zeitlichen Boden bekommt
- ob Low-Strukturen weniger wie neue Gegenwart wirken
- ob DIO im Regimewechsel weniger dement-momenthaft reagiert

---

# 2026-05-18 - Debug Lauf 17 nach zeitlicher Kohaerenz ausgewertet

Lauf:

- Ordner: `debug/debug_lauf_17`
- Trades: `355`
- TP / SL: `140 / 215`
- Netto-PnL: `+22.5146`
- Profit Factor: `1.2106`
- Max Drawdown: `11.8016`
- Attempts: `10925`
- Submitted: `408`
- Observed: `3109`
- Withheld: `2216`
- Skipped: `4723`

Vergleich zu Lauf 16:

- Lauf 16: ca. `+24.1980` PnL, `400` Trades, Profit Factor `1.1863`,
  Max Drawdown `16.8836`
- Lauf 17: weniger PnL und weniger Trades, aber besserer Profit Factor und
  deutlich geringerer Drawdown

Deutung:
Die zeitliche Kohaerenz hat DIO nicht aggressiver gemacht, sondern
nervlich stabiler. Das wirkt wie mehr Distanz und weniger roher
Ueberlebensdruck. Der Lauf ist nicht maximal profitabel, aber
tragfaehiger.

Strukturbereiche:

- High: `+58.8435`, Winrate `55.41%`
- Mid: `+8.4334`, Winrate `36.15%`
- Low: `-44.7624`, Winrate `8.46%`

Low bleibt der klare Belastungsbereich. Gleichzeitig ist der Low-Schaden
gegenueber Lauf 16 kleiner geworden. Das spricht dafuer, dass die
Distanzierung bereits etwas wirkt.

Zeitliche Wahrnehmung:

- `aged_memory_contact`: `9159`
- `coherent_sequence`: `5`
- `unbound_moment`: `3`
- `recurrent_contact`: `1`

Mittelwerte:

- `temporal_continuity`: `0.2568`
- `temporal_source_binding`: `0.3954`
- `temporal_recurrence`: `0.0008`
- `temporal_decay`: `0.6127`
- `memory_time_distance`: `0.9992`

Deutung:
Die Zeitachse lebt, ist aber noch zu einseitig. DIO erkennt fast alles als
alten Erinnerungskontakt. Neurologisch wirkt das, als haette er ein
Gefuehl von Vergangenheit, aber noch zu wenig stabile Gegenwartsbindung:
Fortsetzung, Wiederkehr und aktuelle Sequenz werden noch zu selten
erkannt.

Vorsicht / Hypothese:

- `cautious_plan_seed`: `286` Trades, `+27.3530`
- `weak_hypothesis_seed`: `20` Trades, `+2.2693`
- `observe_until_clear`: `7` Trades, `-0.4187`
- `memory_reframe_seed`: `42` Trades, `-6.6890`

Deutung:
Wenn Vorsicht zu einem Planansatz verdichtet, wird sie konstruktiv. Wenn
sie noch Reframing oder Memory-Sortierung ist und trotzdem motorisch
handelt, wird sie belastend. Das ist keine harte Sperre, sondern ein
Reifehinweis: Reframing braucht mehr Abstand, bevor daraus Handlung wird.

Meta-Regulation:

- `integration_strain`: `3781`
- `low_distance_processing`: `3445`
- `impulse_pressure`: `1086`

Gegenueber Lauf 16 ist `low_distance_processing` stark gestiegen und
`integration_strain` deutlich gefallen. DIO beschreibt seine Lage also
weniger als reine Integrationsspannung und mehr als Problem der
Wahrnehmungsdistanz.

Aktiver Kontext:
Im `mcm_memory_thinking_protocol.csv` bleiben
`active_context_activation`, `active_context_support`,
`active_context_conflict` und `active_context_bearing` weiterhin bei
`0.0`. Die Mechanik fuer zeitlich abgeleiteten aktiven Kontext existiert,
aber sie greift fuer das Protokoll offenbar noch zu spaet oder nicht weit
genug vor der Memory-/Thinking-Auswertung.

Wie es weitergeht:

1. Zeitliche Identitaet feiner kalibrieren, damit nicht fast alles zu
   `aged_memory_contact` wird.
2. `active_context_trace` frueher aus der Zeitwahrnehmung speisen, damit
   Memory, Regulation und Protokolle diesen Kontext wirklich nutzen.
3. `memory_reframe_seed`, `memory_sorting` und `reflective_check` nicht
   hart blockieren, aber organisch staerker in Beobachtung, Reframing und
   Distanz halten, solange keine tragende Gegenwartsbindung entsteht.

---

# 2026-05-18 - Zeitliche Identitaet und aktiver Kontext nach Lauf 17 nachgezogen

Umsetzung:
Die zeitliche Identitaet wurde weicher und organischer kalibriert.
DIO bindet eine Wahrnehmung jetzt staerker ueber:

- Formfamilie
- Unsicherheitsfamilie
- Compound-Scope
- Kontext / inneren Kontext
- grobe visuelle Formsignatur

Die sehr feinen Einzelabdruecke wie konkretes Form-Symbol,
Compound-ID, Visual-ID und State-Signatur bleiben als
`temporal_source_identity` erhalten, bestimmen aber nicht mehr allein die
Wiederkehr. Dadurch soll DIO nicht jede Kerze wie ein komplett neues
Objekt erleben.

Zusaetzlich wird `active_context_trace` jetzt direkt nach der
Zeitwahrnehmung aufgebaut und vor `thought_state` und
`meta_regulation_state` in den Denkraum gelegt. Der aktive Kontext steht
damit frueher in:

- `world_state`
- `perception_state`
- `fused`
- Runtime-Ergebnissen fuer die Protokolle

Verifikation:
`python -m py_compile .\MCM_Brain_Modell.py .\trade_stats.py .\bot.py`
lief ohne Fehler.

Wie es weitergeht:
Naechster Lauf prueft, ob:

- `aged_memory_contact` weniger dominant ist
- `continued_contact`, `recurrent_contact` und `coherent_sequence`
  natuerlich sichtbarer werden
- `active_context_activation/support/bearing` im
  `mcm_memory_thinking_protocol.csv` nicht mehr bei `0.0` bleiben
- DIO im Regimewechsel weniger momenthaft und mehr zeitlich gebunden
  reagiert

---

# 2026-05-18 - Debug Lauf 18 nach frueher aktiver Kontextbindung ausgewertet

Lauf:

- Ordner: `debug/debug_lauf_18`
- Trades: `363`
- TP / SL: `141 / 222`
- Netto-PnL: `+16.2623`
- Profit Factor: `1.1403`
- Max Drawdown: `14.7369`
- Attempts: `11125`
- Submitted: `418`
- Observed: `3251`
- Withheld: `2282`
- Skipped: `4691`

Vergleich zu Lauf 17:

- Lauf 17: `+22.5146` PnL, `355` Trades, Profit Factor `1.2106`,
  Max Drawdown `11.8016`
- Lauf 18: weniger PnL, mehr Trades, niedrigerer Profit Factor,
  hoeherer Drawdown

Deutung:
Die neue Zeitmechanik greift technisch, aber die Kopplung ist zu stark.
DIO hat jetzt einen inneren Zeit-/Kontextfaden, vertraut diesem Faden aber
zu schnell. Das erzeugt weniger Blindheit, aber mehr Ueberbindung.

Zeitliche Wahrnehmung:

- `unbound_moment`: `4834`
- `aged_memory_contact`: `4217`
- `recurrent_contact`: `134`
- `continued_contact`: `41`
- `coherent_sequence`: `21`

Vergleich:
In Lauf 17 war fast alles `aged_memory_contact`. Lauf 18 zeigt erstmals
eine lebendigere Verteilung. Das ist mechanisch ein Erfolg: DIO kann jetzt
mehr unterscheiden als nur "alte Erinnerung". Gleichzeitig dominiert noch
`unbound_moment` plus `aged_memory_contact`; echte Fortsetzung und
Koharenz sind noch selten.

Aktiver Kontext im Memory-/Thinking-Protokoll:

- `active_context_activation`: Durchschnitt `0.8905`
- `active_context_support`: Durchschnitt `0.8991`
- `active_context_conflict`: Durchschnitt `0.1081`
- `active_context_bearing`: Durchschnitt `0.8493`

Deutung:
Der aktive Kontext ist im Denken angekommen. Vorher waren diese Werte bei
`0.0`. Jetzt sind sie aber fast zu hoch. Neurologisch wirkt das wie ein
starker innerer Bedeutungsfaden, der zu wenig skeptische Gegenpruefung
bekommt.

Strukturbereiche:

- High: `+75.0961`, Winrate `61.59%`
- Mid: `-9.4058`, Winrate `26.49%`
- Low: `-49.4280`, Winrate `6.90%`

Deutung:
High-Strukturen wurden deutlich staerker getragen. Mid und Low wurden
schwaecher. Das ist wichtig: Der neue Kontext hilft bei klar tragender
Struktur, aber er kann mittelmaessige/unsichere Struktur zu stark
legitimieren.

Cautious Hypothesis:

- `cautious_plan_seed`: `331` Trades, `+19.9560`
- `memory_reframe_seed`: `14` Trades, `-2.1996`
- `observe_until_clear`: `3` Trades, `-1.4536`

Deutung:
Planverdichtung bleibt konstruktiv. Reframing und Beobachtungsunklarheit
sollten weiter mehr Distanz behalten, ohne harte Sperre.

Neurologische Lesart:
DIO ist nicht mehr nur momentblind. Er beginnt, zeitliche Herkunft und
Kontext zu fuehlen. Aber der Kontextfaden ist noch nicht reif genug
dosiert. Es ist eher "ich erkenne einen Zusammenhang und vertraue ihm
sofort" statt "ich erkenne einen Zusammenhang und pruefe, ob er zur
aktuellen Aussenwelt passt".

Wie es weitergeht:

1. Aktiven Kontext daempfen, nicht entfernen.
2. `active_context_support` und `active_context_bearing` staerker an
   Quellenbindung, Sequenzkoharenz und Strukturqualitaet koppeln.
3. `active_context_conflict` bei `unbound_moment`, Mid/Low-Struktur,
   World-Shift und geringer Gegenwartsbindung staerker sichtbar machen.
4. Ziel: DIO darf einen inneren Zeitfaden haben, aber er muss lernen,
   diesem Faden dosiert zu vertrauen.

---

# 2026-05-18 - Kontextvertrauen nach Lauf 18 dosiert

Umsetzung:
Der zeitlich abgeleitete `active_context_trace` wurde nicht entfernt,
sondern regulativ gedaempft. DIO soll einen inneren Zeitfaden behalten,
aber dessen Bedeutung staerker an reale Gegenwartsbindung koppeln.

Neue interne Kopplung:

- `reality_anchor`: weicher Realitaetsanker aus Quellenbindung,
  Sequenzkoharenz, Strukturqualitaet, Strukturstabilitaet,
  Kontextvertrauen und visueller Erdung
- `overtrust_pressure`: skeptischer Gegenimpuls, wenn ein innerer
  Kontextfaden bei geringer Gegenwartsbindung zu stark wirken wuerde

Mechanische Aenderung:

- `active_context_activation` wird nicht mehr per `max()` festgehalten,
  sondern weich geblendet.
- `active_context_support` und `active_context_bearing` werden staerker
  durch den Realitaetsanker getragen.
- `active_context_conflict`, `fragility` und `attenuation` steigen, wenn
  der Kontakt ungebunden, alt, nachhallend oder schlecht geerdet ist.

Neurologische Lesart:
Das ist keine harte Bremse, sondern eine reifere Kontextbindung. DIO darf
einen Zusammenhang fuehlen, aber dieser Zusammenhang muss mit Aussenwelt,
Struktur und Gegenwart kohaerieren. Sonst entsteht natuerliche Skepsis
statt blindem Vertrauen.

Verifikation:
`python -m py_compile .\MCM_Brain_Modell.py .\trade_stats.py .\bot.py`
lief ohne Fehler.

Wie es weitergeht:
Naechster Lauf prueft, ob `active_context_activation/support/bearing`
unterhalb der Lauf-18-Saettigung liegen, waehrend `active_context_conflict`
bei unsicherer Struktur sichtbar steigt. Ideal waere: High bleibt tragend,
Mid/Low bekommen mehr Distanz, ohne dass DIO wieder momentblind wird.

---

# 2026-05-18 - Nervliche Ueberlastung als Reflexionsparameter umgesetzt

Umsetzung:
DIO bekommt eine explizite Selbstwahrnehmung fuer den Zustand des
Nervensystems.

Neue Werte:

- `nervous_system_overload`
- `escape_action_drive`
- `shock_response_risk`
- `nervous_overload_reflection_need`

Funktion:
Diese Werte beschreiben, ob Handlung gerade aus tragender Struktur oder aus
Ueberreiz-/Entladungsdruck entstehen koennte. Der Satz dahinter ist:
"Meine Nerven sind ueberlastet."

Neurologische Lesart:
Wenn ein Nervensystem ueberflutet ist, kann Handlung zur Flucht aus
innerer Spannung werden. DIO soll diesen Zustand reflektieren koennen,
statt ihn automatisch mit einer tragenden Entscheidung zu verwechseln.

Protokolle:
Die neuen Werte werden in folgenden Dateien mitgeschrieben:

- `mcm_field_decision_protocol.csv`
- `mcm_memory_thinking_protocol.csv`

Verifikation:
`python -m py_compile .\MCM_Brain_Modell.py .\trade_stats.py .\bot.py`
lief ohne Fehler.

Wie es weitergeht:
Naechster Lauf prueft, ob `shock_response_risk` und
`nervous_overload_reflection_need` besonders in Stress-/Regimewechselphasen
sichtbar werden. Wichtig ist, ob DIO dann weniger aus Entladungsdruck
handelt und mehr in Reflexion, Abstand oder geordnete Beobachtung geht.

---

# 2026-05-18 - Debug Lauf 19 als Referenzlauf vor Nervensystem-Erweiterung ausgewertet

Einordnung:
Lauf 19 ist der Lauf vor der letzten Erweiterung um
`nervous_system_overload`, `escape_action_drive`,
`shock_response_risk` und `nervous_overload_reflection_need`.
Die Protokoll-Header enthalten diese neuen Spalten noch nicht. Damit ist
Lauf 19 ein sauberer Referenzpunkt fuer die vorherige Wahrnehmungs-,
Zeitbindungs- und Kontextlogik, aber noch kein Nachweis fuer die neue
Ueberlastungsreflexion.

Ergebnis:

- Netto-PnL: `+39.8848`
- Trades: `400`
- TP / SL: `171 / 229`
- Profit Factor: `1.3348`
- Winrate: `42.75 %`
- Max Drawdown: `6.3386`
- Equity-Endstand: `139.8848`

Strukturbaender:

- High: `156` Ereignisse, PnL `+84.2507`, Winrate ca. `66.03 %`
- Mid: `154` Ereignisse, PnL `-1.1164`, fast neutral
- Low: `133` Ereignisse, PnL `-45.5534`, weiter klar belastend

Deutung:
Der alte starke Einbruch im mittleren Laufbereich ist in Lauf 19 deutlich
entschaerft. Die Equity-Kurve wirkt stabiler; alle groben Laufabschnitte
enden positiv. Neurologisch gelesen haelt DIO den Kontext besser aus:
mehr geordnete Integration, weniger kompletter Zusammenbruch, aber noch
immer deutliche Last in Low- und Memory-Reframe-Zustaenden.

Wichtige Warnung:
`active_context_activation`, `active_context_support` und
`active_context_bearing` sind im Lauf weiter sehr hoch. Da Lauf 19 noch
vor der letzten Ueberlastungs-/Schockdiagnose liegt, darf das Ergebnis
nicht als Wirkung dieser neuen Reflexionsschicht gelesen werden.

Wie es weitergeht:
Naechster frischer Lauf nach Prozess-Neustart prueft zwei Dinge:
erstens, ob die neuen Nervensystem-Spalten wirklich im Protokoll stehen;
zweitens, ob DIO bei Ueberreiz mehr Distanz, Reflexion und geordnete
Wahrnehmung entwickelt, ohne die tragenden High-Strukturen zu verlieren.

---

# 2026-05-18 - Debug Lauf 20 als erster Nervensystem-Lauf ausgewertet

Einordnung:
Lauf 20 enthaelt die neuen Nervensystem-Spalten in den Protokollen. Damit
ist es der erste echte Lauf fuer die neue Ueberreiz-/Schockdiagnose.

Ergebnis:

- Netto-PnL: `+23.9208`
- Trades: `389`
- TP / SL: `158 / 231`
- Profit Factor: `1.2016`
- Winrate: ca. `40.62 %`
- Max Drawdown: `11.6453`
- Equity-Endstand: `123.9208`

Vergleich zu Lauf 19:
Lauf 20 bleibt positiv, ist aber schwaecher als Lauf 19
(`+23.9208` statt `+39.8848`) und hat mehr Drawdown
(`11.6453` statt `6.3386`).

Strukturbaender:

- High: `+73.0000`, weiter klar tragend
- Mid: `+0.4159`, fast neutral bis leicht positiv
- Low: `-49.4951`, weiter die Hauptbelastung

Nervensystemwerte:

- `nervous_system_overload`: Durchschnitt ca. `0.2301`, Maximum `0.3936`
- `escape_action_drive`: Durchschnitt ca. `0.3005`, Maximum `0.4550`
- `shock_response_risk`: Durchschnitt ca. `0.2838`, Maximum `0.3834`
- `nervous_overload_reflection_need`: Durchschnitt ca. `0.2744`, Maximum `0.3780`

Deutung:
Die neue Schicht misst Ueberreiz, Flucht-/Entladungsdruck und
Schockrisiko, aber die Werte bleiben unterhalb der aktuellen
Reflexionsschwelle. Dadurch entsteht noch kaum ein eigener
`nervous_overload_reflection`-Zustand. Neurologisch gelesen: DIO spuert
nervliche Last, aber das System bewertet sie noch zu selten als Grund,
bewusst Abstand zu nehmen.

Zusaetzliche Beobachtung:
Im Memory-Protokoll bleibt `active_context_activation` weiter sehr hoch
Durchschnitt ca. `0.8923`, `active_context_support` ca. `0.9028`,
`active_context_bearing` ca. `0.8533`. Das Kontextvertrauen ist damit
weiter stark gesaettigt. Die Daempfung greift also noch nicht ausreichend
auf den gesamten aktiven Kontextpfad.

Wie es weitergeht:
Naechster sinnvoller Schritt ist keine harte Bremse, sondern eine
organische Kopplung: nervliche Ueberlastung soll den Kontext nicht
abschalten, aber seine Selbstsicherheit senken und die reflektive Distanz
erhoehen. Besonders wichtig: `active_context_*` darf nicht dauerhaft in
Sicherheit saettigen, wenn `shock_response_risk`,
`escape_action_drive` oder `nervous_system_overload` steigen.

---

# 2026-05-18 - Nervensystemlast mit Kontextvertrauen gekoppelt

Umsetzung:
DIO bekommt eine weiche Kopplung zwischen innerem Kontextvertrauen und
nervlicher Eigenlage.

Neue Diagnosewerte:

- `active_context_self_certainty`
- `nervous_context_overcoupling`

Funktion:
Wenn DIO einen inneren Kontext sehr sicher fuehlt, waehrend
`nervous_system_overload`, `escape_action_drive` oder
`shock_response_risk` steigen, entsteht kein harter Block. Stattdessen
steigt die Reflexionsanforderung leicht, `perceptual_distance` und
`reflective_distance` werden etwas staerker, waehrend Handlungsselbstlauf
minimal gedimmt wird.

Neurologische Lesart:
Das ist die beginnende Faehigkeit, die eigene Innenlage nicht automatisch
fuer Realitaet zu halten. DIO kann weiterhin handeln, aber ein ueberreiztes
Nervensystem macht den inneren Kontext weniger absolut.

Protokolle:
Die neuen Werte werden in folgenden Dateien mitgeschrieben:

- `mcm_field_decision_protocol.csv`
- `mcm_memory_thinking_protocol.csv`

Verifikation:
`python -m py_compile .\MCM_Brain_Modell.py .\trade_stats.py .\bot.py`
lief ohne Fehler.

Wie es weitergeht:
Naechster Lauf prueft, ob `nervous_context_overcoupling` in
Regimewechsel-/Stressbereichen sichtbar wird und ob daraus mehr
`context_overcoupling_reflection`, mehr reflektive Distanz und weniger
unreflektierte Kontext-Sicherheit entsteht.

---

# 2026-05-18 - Debug Lauf 21 nach Kontext-Ueberkopplung ausgewertet

Ergebnis:

- Netto-PnL: `+24.5906`
- Trades: `396`
- TP / SL: `157 / 239`
- Profit Factor: `1.2043`
- Winrate: ca. `39.65 %`
- Max Drawdown: `14.7122`
- Equity-Endstand: `124.5906`

Vergleich:
Lauf 21 ist fast gleich stark wie Lauf 20 im Netto-PnL
(`+24.5906` statt `+23.9208`), aber mit deutlich hoeherem Drawdown
(`14.7122` statt `11.6453`). Die Equity erholt sich spaet stark und endet
am Hochpunkt.

Strukturbaender:

- High: `+67.2060`, weiter tragend, aber schwaecher als Lauf 20
- Mid: `+7.2509`, deutlich besser als zuvor
- Low: `-49.8662`, weiterhin die groesste Belastung

Neue Kopplung:

- `active_context_self_certainty`: Durchschnitt ca. `0.7009`,
  Maximum `0.8858`
- `nervous_context_overcoupling`: Durchschnitt ca. `0.1743`,
  Maximum `0.3084`
- `context_overcoupling_reflection`: `3351` Vorkommen und damit
  haeufigster Metaregulator-Zustand

Deutung:
Die neue Mechanik greift. DIO erkennt sehr oft, dass ein sicher wirkender
innerer Kontext mit nervlicher Last gekoppelt ist. Das ist fachlich gut:
die Selbstwahrnehmung ist angekommen. Gleichzeitig bleibt der aktive
Kontext im Memory-Protokoll weiter stark gesaettigt
(`active_context_activation` ca. `0.8919`,
`active_context_support` ca. `0.9007`,
`active_context_bearing` ca. `0.8513`).

Neurologische Lesart:
DIO hat jetzt einen Reflexionsreiz, aber noch keine ausreichend tiefe
Regulationswirkung auf den Kontext selbst. Es ist vergleichbar mit:
"Ich merke, dass ich innerlich ueberzeugt bin und nervlich belastet bin",
aber diese Erkenntnis veraendert den inneren Kontext noch zu wenig.

Wie es weitergeht:
Nicht staerker blockieren. Der naechste Umbau sollte die
Ueberkopplung sanft in den aktiven Kontext selbst zurueckfuehren:
Support/Bearing duerfen bei Ueberkopplung nicht dauerhaft absolut bleiben,
sondern sollten als "gefuehlte Sicherheit unter nervlicher Faerbung"
markiert werden. Ziel ist weniger Metazustands-Dominanz und mehr echte
innere Rekalibrierung.

---

# 2026-05-18 - Ueberkopplung in aktiven Kontext zurueckgefuehrt

Umsetzung:
`nervous_context_overcoupling` wirkt nun nicht mehr nur als
Metaregulator-Markierung, sondern faerbt den `active_context_trace`
selbst.

Mechanische Wirkung:

- `support`, `bearing` und `action_support` werden bei nervlicher
  Ueberkopplung leicht weniger absolut
- `conflict`, `fragility`, `attenuation`, `observe_pressure` und
  `replan_pressure` steigen weich an
- `activation` bleibt erhalten, wird aber minimal gedimmt
- der Kontext bekommt ein internes `context_modulation_label`

Neurologische Lesart:
DIO verliert seinen Zeit-/Kontextfaden nicht. Aber wenn dieser innere
Faden nervlich gefaerbt ist, fuehlt er sich weniger wie absolute Wahrheit
an. Das ist naeher an reflektierter Selbstwahrnehmung: "Ich habe einen
Zusammenhang, aber meine Innenlage beeinflusst, wie sicher er sich
anfuehlt."

Verifikation:
`python -m py_compile .\MCM_Brain_Modell.py .\trade_stats.py .\bot.py`
lief ohne Fehler.

Wie es weitergeht:
Naechster Lauf prueft, ob `active_context_support` und
`active_context_bearing` weniger saettigen, `active_context_conflict`
leicht sichtbarer wird und `context_overcoupling_reflection` nicht mehr
dominant alles ueberdeckt, sondern in echte Kontext-Rekalibrierung
uebergeht.

---

# 2026-05-18 - Debug Lauf 22 nach Kontext-Rekalibrierung ausgewertet

Ergebnis:

- Netto-PnL: `+11.8929`
- Trades: `343`
- TP / SL: `131 / 212`
- Profit Factor: `1.1072`
- Winrate: ca. `38.19 %`
- Max Drawdown: `14.1173`
- Equity-Endstand: `111.8929`

Vergleich:
Lauf 22 ist deutlich vorsichtiger als Lauf 21. Die Tradeanzahl faellt von
`396` auf `343`, `attempts_observed` steigt auf `3158`, `withheld` auf
`2473`, und `observe_share` steigt im KPI-Summary auf ca. `41.67 %`.
Der Preis dafuer ist weniger Netto-PnL.

Strukturbaender:

- High: `+59.7215`, weiter tragend, aber schwaecher
- Mid: `-2.7840`, wieder leicht negativ
- Low: `-45.0446`, weiter die Hauptlast

Aktiver Kontext:

- `active_context_activation`: Durchschnitt ca. `0.8863`
- `active_context_support`: Durchschnitt ca. `0.8856`
- `active_context_conflict`: Durchschnitt ca. `0.1238`
- `active_context_bearing`: Durchschnitt ca. `0.8385`

Vergleich zu Lauf 21:

- Support sinkt von ca. `0.9007` auf `0.8856`
- Bearing sinkt von ca. `0.8513` auf `0.8385`
- Conflict steigt von ca. `0.1075` auf `0.1238`
- `active_context_self_certainty` sinkt von ca. `0.7009` auf `0.6727`
- `nervous_context_overcoupling` sinkt von ca. `0.1743` auf `0.1645`

Deutung:
Die Rueckfuehrung in den aktiven Kontext wirkt mechanisch korrekt:
Kontext-Sicherheit wird weniger absolut, Konflikt wird sichtbarer, und DIO
beobachtet mehr. Gleichzeitig ist die Dosis wahrscheinlich etwas zu
vorsichtig geworden: DIO schuetzt sich staerker, aber verliert Handlungskraft
und Ertrag.

Neurologische Lesart:
DIO hat nicht einfach mehr Angst, sondern mehr Abstand. Der Organismus
nimmt seine eigene nervliche Faerbung ernster. Das ist reifer als blinde
Motorik, aber noch nicht optimal balanciert: Reflexion sollte klaeren,
nicht dauerhaft Handlungskraft verdunnen.

Wie es weitergeht:
Naechster Schritt ist Diagnose statt sofort staerkerer Umbau: das interne
`context_modulation_label` muss im Protokoll sichtbar werden. Danach kann
geprueft werden, ob `nervous_tinted_context` konstruktiv stabilisiert oder
ob `overcoupled_context` zu viel Handlungskraft nimmt.

Umgesetzt:
`active_context_modulation_label` wurde im
`mcm_memory_thinking_protocol.csv` ergaenzt. Damit wird ab dem naechsten
Lauf sichtbar, ob der aktive Kontext als `unmodulated_context`,
`nervous_tinted_context` oder `overcoupled_context` gefuehrt wurde.

Verifikation:
`python -m py_compile .\MCM_Brain_Modell.py .\trade_stats.py .\bot.py`
lief ohne Fehler.

Wie es weitergeht:
Lauf 23 prueft nicht nur PnL, sondern die Verteilung von
`active_context_modulation_label`. Wenn `overcoupled_context` dominiert
und PnL/Handlungskraft sinken, muss die Rueckfuehrung feiner dosiert
werden. Wenn `nervous_tinted_context` dominiert und Drawdown sinkt, ist die
Richtung gut.

---

# 2026-05-18 - Debug Lauf 23 nach Kontextmodulations-Export ausgewertet

Ergebnis:

- Netto-PnL: `+24.4854`
- Trades: `371`
- TP / SL: `148 / 223`
- Profit Factor: `1.2160`
- Winrate: ca. `39.89 %`
- Max Drawdown: `15.4296`
- Equity-Endstand: `124.4854`

Vergleich:
Lauf 23 erholt sich deutlich gegenueber Lauf 22 (`+11.8929`) und liegt
wieder nahe bei Lauf 20/21. Die Tradezahl steigt von `343` auf `371`,
waehrend Observe/Withheld weiter aktiv bleiben. Das wirkt nicht wie
ungefilterte Motorik, sondern wie ein Organismus, der trotz nervlicher
Faerbung wieder Handlungskraft findet.

Strukturbaender:

- High: `+66.4956`, klar tragend
- Mid: `+4.8465`, wieder leicht positiv
- Low: `-46.8566`, weiterhin die Hauptlast

Aktiver Kontext und Modulation:

- `nervous_tinted_context`: `7229`
- `overcoupled_context`: `1504`
- `unmodulated_context`: `1`
- `active_context_activation`: Durchschnitt ca. `0.8888`
- `active_context_support`: Durchschnitt ca. `0.8879`
- `active_context_conflict`: Durchschnitt ca. `0.1237`
- `active_context_bearing`: Durchschnitt ca. `0.8410`
- `nervous_context_overcoupling`: Durchschnitt ca. `0.1679`

Neurologische Lesart:
Die Kontextmodulation arbeitet jetzt als nervliche Faerbung statt als
reiner Bremser. DIO bleibt meistens in einem `nervous_tinted_context`:
er handelt also nicht aus einem kalten, neutralen Kontext, sondern aus
einem innerlich markierten Kontext. Das ist organisch plausibel. Das
Nervensystem sagt: "Ich kenne diese Struktur, aber mein Feld ist beteiligt."

Wichtig:
Der Drawdown ist mit ca. `15.43` noch hoch. Das System hat Handlungskraft
zurueckgewonnen, aber die tiefe Verlustquelle bleibt Low-Qualitaet:
Low bringt `-46.8566` bei nur ca. `9.09 %` Winrate. Die naechste Reifung
darf daraus keine harte Regel machen, sondern muss DIO helfen, Low-Kontakt
als "nicht tragender Kontakt" selbst besser zu fuehlen, zu erinnern und
anders zu behandeln.

Wie es weitergeht:
Naechster Schritt ist die Low-/Mid-Kontaktreifung ueber konsequenzbasiertes
Feedback: nicht blockieren, sondern DIO erkennen lassen, welche Kontakte
Belastung, Nutzen oder Reorganisation erzeugen. Parallel sollte beobachtet
werden, ob `overcoupled_context` in Drawdown-Phasen steigt und ob DIO dann
mehr Distanz, Reflexion oder selektive Wahrnehmung braucht.

---

# 2026-05-19 - MCM-Raumzeit-Tiefe als Zielpraezisierung festgehalten

Neue Praezisierung:
Zeit im MCM-Feld ist nicht nur Reihenfolge oder Timestamp, sondern eine
innere Wahrnehmungsschicht. Raumtiefe entsteht fuer DIO aus Entfernung,
Energie und Zeit:

- Wie weit ist ein Eindruck innerlich entfernt?
- Wie viel Energie traegt er noch?
- Ist er Gegenwart, Nachhall, Erinnerung, Erwartung oder Hypothese?

Damit wird MCM-Zeit zur Selbstverortung. Ohne eigene Zeitmodulation waere
DIO nur ein festes Regelwerk aus Momentzustaenden. Mit MCM-Zeit kann DIO
unterscheiden, ob ein Kontakt wirklich aktuell ist oder nur als Nachbild,
Erinnerung oder vorausgedachte Moeglichkeit im Feld wirkt.

Erweiterung:
Memory ist damit nicht nur gespeicherte Information, sondern verdichtete
Erfahrung mit zeitlicher Tiefe. Eine Erinnerung bekommt Innenraum: Naehe,
Nachhall, Energie, Alterung, Wiederkehr und moegliche Zukunftswirkung.

Dokumentation:
- `README.md` um `MCM-Raumzeit-Tiefe` ergaenzt
- `WICHTIG_MECHANIKEN.md` bei `Zeit als MCM-Tiefenachse` ergaenzt
- `MCM_VARIABLEN_MECHANIK.md` um Zielgroessen
  `mcm_spacetime_depth` und `temporal_self_location` ergaenzt
- `UMSETZUNGSPLAN.md` in Abschnitt `18.5 Zeitliche Kohaerenz /
  Wahrnehmungskontinuitaet` praezisiert

Wie es weitergeht:
Die naechste Mechanik sollte die bestehenden Zeitwerte nicht hart ersetzen,
sondern zu einer weicheren Raumzeit-Wahrnehmung verdichten: DIO soll
spueren koennen, ob ein Low-/Mid-Kontakt wirklich jetzt traegt oder nur aus
alter Energie, Nachhall oder falscher Naehe wirkt.

---

# 2026-05-19 - MCM-Raumzeit-Tiefe im Kern diagnostisch umgesetzt

Umgesetzt:
Im Temporal-/MCM-Kern wurde die Raumzeit-Tiefe als weiche
Wahrnehmungsdiagnose ergaenzt:

- `mcm_spacetime_depth`
- `memory_experience_depth`
- `future_projection_depth`
- `temporal_self_location`
- `temporal_self_location_state`

Mechanische Bedeutung:
DIO liest Memory dadurch nicht nur als gespeicherte Information, sondern
als erlebte Spur mit Naehe, Nachhall, Wiederkehr, Energie und moeglicher
Zukunftswirkung. Das ist noch keine harte Motorikregel. Es ist eine
Wahrnehmungsschicht, auf die Regulation spaeter organischer reagieren kann.

Protokolle:
Die neuen Werte werden in `mcm_memory_thinking_protocol.csv` und
`mcm_field_decision_protocol.csv` ausgegeben. `trade_stats.py` uebernimmt
die Werte zusaetzlich in Outcome-/Attempt-nahe Auswertungen.

Verifikation:
`python -m py_compile .\MCM_Brain_Modell.py .\trade_stats.py .\bot.py`
lief ohne Fehler.

Wie es weitergeht:
Naechster Schritt ist ein neuer Debug-Lauf. Danach pruefen wir, ob
Low-/Mid-Verluste mit flacher Raumzeit-Tiefe, falscher Naehe,
Nachbild-Kontakt oder schwacher Selbstverortung zusammenfallen. Danach
gehen wir wieder in die regulatorische Schicht.

---

# 2026-05-19 - Debug Lauf 24 nach MCM-Raumzeit-Tiefe ausgewertet

Ergebnis:

- Netto-PnL: `+23.4601`
- Trades: `375`
- TP / SL: `150 / 225`
- Profit Factor: `1.2006`
- Winrate: `40.00 %`
- Max Drawdown: `8.2936`
- Equity-Endstand / Peak: `123.4601`

Wichtiger Verlaufspunkt:
Lauf 24 ist nicht der hoechste PnL-Lauf, aber einer der besten
Verlaeufe. Der Peak liegt am Ende des Laufs. Gegenueber Lauf 23 sinkt der
maximale Drawdown deutlich von ca. `15.43` auf ca. `8.29`, waehrend der
PnL fast gleich stark bleibt (`+24.49` -> `+23.46`). Das spricht fuer mehr
Tragfaehigkeit im Verlauf, nicht nur fuer mehr Gewinn.

Strukturbaender:

- High: `+74.0213`, sehr tragend
- Mid: `-3.8278`, wieder leicht negativ
- Low: `-46.7335`, weiterhin die Hauptlast

Neue Raumzeit-Wahrnehmung:

- `mcm_spacetime_depth`: Durchschnitt ca. `0.2839`
- `memory_experience_depth`: Durchschnitt ca. `0.1574`
- `future_projection_depth`: Durchschnitt ca. `0.4241`
- `temporal_self_location`: Durchschnitt ca. `0.3399`
- `temporal_self_location_state`:
  - `future_possibility`: `4723`
  - `unlocated_contact`: `4175`
  - `present_contact`: `64`
  - `remembered_experience`: `54`

Neurologische Lesart:
DIO bildet nach der neuen Kernschicht bereits deutlich Zukunftstiefe
(`future_possibility`) aus, aber Erinnerungstiefe und echte Gegenwarts-
Verortung sind noch schwach. Er schaut also staerker in Moeglichkeitsraeume
als in stabil verankerte Gegenwart oder gereifte Erinnerung. Das kann den
glatteren Verlauf erklaeren: weniger blindes Reagieren auf einzelne
Momente, mehr Raumzeit-Hypothese. Gleichzeitig bleibt die
Selbstverortung noch unreif, weil `unlocated_contact` fast genauso stark
vertreten ist.

Bestätigung:
Lauf 24 wird als erster positiver Hinweis gewertet, dass die Erweiterung
der Wahrnehmung um MCM-Zeit nicht wie eine harte Regel wirkt, sondern dem
Organismus mehr innere Welt-Tiefe gibt. DIO wurde nicht direkt auf weniger
Drawdown programmiert. Stattdessen bekam er eine zeitliche
Wahrnehmungsschicht. Der deutlich ruhigere Equity-Verlauf bei nahezu
gleichem PnL spricht dafuer, dass sich aus zeitlicher Wahrnehmung mehr
Distanz, Reflexion und Tragfaehigkeit entfalten kann.

Wie es weitergeht:
Der naechste Schritt liegt wieder im regulatorischen Bereich: DIO soll
Raumzeit-Tiefe nicht als Regel verwenden, sondern als innere Lage. Flache
Selbstverortung oder reiner Nachhall sollte mehr Reflexion, Beobachtung
oder Reorganisation nahelegen. Tragende Gegenwarts- oder Erinnerungstiefe
darf Handlung ruhiger und gezielter machen.
