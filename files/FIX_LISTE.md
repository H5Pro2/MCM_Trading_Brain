# FIX_LISTE

Rolle dieser Datei:
- aktive Aufgaben
- naechste Pruefpunkte
- kurze Statusmarkierung

Details, Laufanalysen und Forschungsdeutung gehoeren nicht hierher.
Regelwerk: `files/MD_ANWEISUNG.md`.

---

# Aktiver Fokus

- [x] Neurochemische Alias-Schicht bauen.
  Ziel:
  - `neurochemical_state` im Runtime-Ergebnis erzeugen
  - vorhandene Werte als technische Achsen buendeln:
    `dopamine_tone`, `gaba_inhibition`, `noradrenaline_arousal`,
    `acetylcholine_focus`, `serotonin_stability`, `cortisol_load`,
    `endorphin_relief`, `glutamate_activation`
  - zunaechst Diagnose/Debug, spaeter weiche Meta-Regulation

- [ ] Naechsten Lauf mit neurochemischer Diagnose pruefen.
  Ziel:
  - TP/SL gegen `cortisol_load`, `gaba_inhibition`, `dopamine_tone`,
    `acetylcholine_focus`, `serotonin_stability` und `neurochemical_balance`
    auswerten
  - Regimewechsel nicht mechanisch bewerten, sondern Last/Support lesen
  - Lauf 10 als ersten neurochemischen Referenzlauf nutzen

- [x] Neurochemische Uebergaenge aus Lauf 10 vertiefen.
  Ziel:
  - `serotonin_stability -> glutamate_activation` gegen Handlung naeher
    untersuchen
  - strukturelle Kipp-Momente mit `cortisol_load`, `gaba_inhibition`,
    `zero_point_regulation` und `observe` vergleichen
  - klaeren, ob DIO aus Stabilitaet aktiviert oder aus Last kippt
  Befund:
  - erster `-2/+2` Kerzenvergleich spricht fuer zwei Muster:
    Glutamat-Aktivierung aus stabiler Grundlage vs. Cortisol-Kippmoment bei
    Volumen-/Range-Spikes

- [ ] Neues neurochemisches Uebergangsprotokoll im naechsten Lauf pruefen.
  Ziel:
  - `mcm_neuro_transition_protocol.csv` auf Vollstaendigkeit pruefen
  - Transitionen gegen TP/SL, `observe`, `act_watch`, `act` und
    `zero_point_regulation` lesen
  - klaeren, ob DIO aus Stabilitaet aktiviert oder unter Last kippt
  Status:
  - Lauf 11 bestaetigt Protokollausgabe.
  - Naechster Schritt: Zone-Verlust gegen Non-Zone-Verbesserung auswerten.

- [ ] Zone-Praezision gegen Transferfaehigkeit untersuchen.
  Ziel:
  - klaeren, warum Non-Zone in Lauf 11 besser wurde, Zone aber schwacher
  - `glutamate_activation` bei SL gegen TP vergleichen
  - pruefen, ob DIO zu viel Aktivierung in eigentlich bekannten Zonen
    zugelassen hat
  Befund:
  - Lauf 11 zeigt Aktivierung ohne ausreichend tragende Reife als Kernrisiko.
  - Non-Zone profitierte leicht von mehr Transfer, Zone verlor
    Auswahlpraezision.

- [ ] Aktivierungs-Tragfaehigkeit als Diagnoseachse vorbereiten.
  Ziel:
  - keine harte Regel bauen
  - `glutamate_activation` gegen `neurochemical_balance`,
    `action_inhibition`, `action_clearance`, `transfer_bearing` und
    `variant_bearing_memory` lesen
  - unterscheiden zwischen reifer Aktivierung und nervlicher Ueberfeuerung

- [x] Core-Engine Wahrnehmungsuebersetzung entlasten.
  Ziel:
  - pruefen, ob Chartreize mehrfach als gleichgerichteter Alarm wirken
  - Risiko-/Threat-Achse mit echter Rueckregulation versehen
  - keine harte Regel, sondern sensorische Habituation und Reizverdichtung
  - DIO soll Form sehen, nicht dauerhaft im Stressmilieu tasten
  Befund:
  - Lauf 11 zeigt fast permanent `stressed` und stark negative
    `mean_risk`-Achse.
  - `visual_form_pressure` ist stark mit mehreren Aussenreizachsen
    gekoppelt.

- [ ] Naechsten Lauf nach sensorischer Entdoppelung pruefen.
  Ziel:
  - `self_state=stressed`-Anteil und `mean_risk` vergleichen
  - `mcm_visual_cortex_protocol.csv` auf `sensory_redundancy`,
    `sensory_gate` und `sensory_reality_label` pruefen
  - klaeren, ob DIO weniger doppelte Strukturreize und mehr klare
    Realitaetsform wahrnimmt

- [x] Naechsten Lauf nach Outcome-Export-Erweiterung pruefen.
  Ziel:
  - pruefen, ob `outcome_records.jsonl` jetzt Formfamilienwerte enthaelt
  - TP/SL gegen `variant_learning_pressure`, `uncertainty_familiarity`,
    `variant_bearing_memory`, `visual_action_uncertainty` auswerten
  - Lauf 8 als Referenz nutzen

- [ ] Regimewechsel-Bewaeltigung aus Lauf 9 vertiefen.
  Ziel:
  - klaeren, warum Formvertrautheit nicht immer zu Handlungssicherheit wird
  - `memory_compare_load`, `orientation_gap`, `blind_thinking_load`,
    `action_clearance`, `action_inhibition` gegen TP/SL betrachten
  - keine harte Regel ableiten, sondern Reife-/Tragfaehigkeitsdiagnostik
    verbessern

- [ ] Sensorische Erfahrungssynchronisation nach Lauf 12/13 pruefen.
  Ziel:
  - klaeren, ob alte Memory-Signaturen zur neuen sensorischen Kodierung passen
  - nicht den Speicher loeschen, sondern Anpassungsdruck sichtbar machen
  - `memory_compare_load`, `sensory_gate`, `visual_form_pressure`,
    `action_inhibition`, `regulated_courage` und PnL-Verlauf gemeinsam lesen

- [ ] Serotonin-Nachhall beim Regimewechsel pruefen.
  Ziel:
  - erkennen, ob `serotonin_carryover_risk` im Abverkauf steigt
  - pruefen, ob DIO weiter aus alter Stabilitaetslage handelt
  - `emotional_decoupling` und `reactive_nervous_drive` gegen TP/SL und
    Equity-Bruch lesen

- [x] Selektive Wahrnehmung / perzeptive Regulation als naechsten
  Architekturblock vorbereiten.
  Ziel:
  - Wahrnehmungen nicht hart filtern, sondern ihre Naehe zum MCM-Feld weich
    regulieren
  - `perceptual_distance`, `object_contact_depth`, `field_attachment`,
    `release_capacity`, `selective_attention`, `background_containment`,
    `reflective_distance` und `inner_outer_alignment` als Zielachsen pruefen
  - DIO soll Reize sehen, vertiefen oder ablegen koennen, ohne jeden Eindruck
    vollstaendig zu durchleben

- [x] Bewusste Wahrnehmung / innere Reizwirkungsanalyse diagnostisch bauen.
  Ziel:
  - nicht nur Reize daempfen, sondern ihre Wirkung im MCM-Feld bewusst lesbar
    machen
  - pruefen: Was hat der aeussere Reiz mit dem MCM-Feld gemacht?
  - Zielachsen: `conscious_perception_state`, `stimulus_field_effect`,
    `inner_impact_trace`, `perceived_field_change`, `felt_afterimage`,
    `object_release_state`, `inner_outer_reflection`
  - Grundlage fuer echte Reflexion und regulatorische Steuerung schaffen

- [ ] Lauf 17 mit bewusster Wahrnehmung auswerten.
  Ziel:
  - `conscious_perception_state`, `field_attachment`, `perceptual_distance`,
    `release_capacity` und `inner_outer_alignment` gegen TP/SL,
    Regimewechsel und Equity-Verlauf lesen
  - pruefen, ob DIO im Abverkauf ueberkoppelt, reflektiv Abstand findet oder
    Reize loslassen kann
  - danach erst entscheiden, ob eine weiche Regulation auf diese Achsen
    aufgebaut wird

- [x] Bewusste Wahrnehmungslabels feiner kalibrieren.
  Befund aus neuem `debug_lauf_1`:
  - alle Protokollzeilen stehen auf `open_perception`
  - alle Release-Zustaende stehen auf `holding`
  - numerische Achsen bewegen sich, aber die Labels unterscheiden noch nicht
    fein genug
  Ziel:
  - keine harte Handelsregel
  - Labels dynamischer aus relativer Innenlage bilden
  - `object_contact`, `reflective_check`, `overcoupled_field` und
    `release_ready` natuerlich sichtbar machen

- [x] Lauf 2 mit innerer Haltung auswerten.
  Ziel:
  - pruefen, ob `conscious_perception_state` und `inner_posture_state` nun
    streuen
  - `curious`, `excited`, `overstimulated`, `tired`, `calm` und `reflective`
    gegen TP/SL, Equity-Bruch und Regimewechsel lesen
  - keine harte Regel ableiten, sondern erst pruefen, welche inneren
    Haltungen tragfaehig oder belastend werden

- [x] Diffuse Offenheit weich weiterentwickeln.
  Befund aus Lauf 2:
  - `uncertain_open` und `open_perception` waren bei Trades negativ
  - benannte Aktivierung wie `excited`, `curious` oder `overcoupled_field`
    war nicht automatisch schlecht
  Ziel:
  - keine harte Blockade auf `uncertain_open`
  - DIO soll diffuse Offenheit eher in Beobachtung, Objektkontakt,
    Reflexion oder Loslassen ueberfuehren
  - pruefen, ob dadurch weniger blinde Handlungen entstehen

- [ ] Lauf 3 mit diffuser Offenheitsreifung pruefen.
  Ziel:
  - `diffuse_open_development_pressure` und `posture_development_hint` gegen
    TP/SL und Equity-Verlauf lesen
  - pruefen, ob `uncertain_open`-Trades sinken
  - pruefen, ob gute Aktivierung (`curious`, `excited`, tragendes
    `overcoupled_field`) nicht erstickt wird

- [ ] Wache Anstrengung statt Gleichgueltigkeit bauen.
  Befund aus Lauf 3:
  - Trades sanken, PnL brach dennoch stark ein
  - Zone war positiv, Non-Zone massiv negativ
  - `uncertain_open` sank, aber Schaden wanderte in schwache
    `object_contact`-/Non-Zone-Handlungen
  Ziel:
  - kein harter Non-Zone-Block
  - `diffuse_open_development_pressure` nicht pauschal Courage senken lassen
  - `engaged_effort` / wache Anstrengung als Gegenpol zu Unterspannung
    pruefen
  - Non-Zone bei niedriger Tragfaehigkeit eher in Beobachtungslernen,
    Reflexion oder Loslassen ueberfuehren

- [x] Erfahrungspaket-Feedback / positive Stimulation bauen.
  Ziel:
  - kein `TP = gut` / `SL = schlecht`
  - gesamtes Paket bewerten: Struktur, Innenlage, Wahrnehmung, Haltung,
    Handlung, Risiko, Ergebnis, Wiederholbarkeit
  - gute Prozessleistung positiv stimulieren
  - schlechte Paketqualitaet als Reorganisationssignal nutzen
  - auch Abverkauf positiv bewerten koennen, wenn Entscheidung und Prozess
    tragfaehig waren
  - Grundlage fuer `engaged_effort` als positiv getragene Wachheit schaffen
  Status:
  - umgesetzt in `build_experience_packet_feedback`
  - sichtbar in `last_outcome_decomposition` und `outcome_records.jsonl`
  - in Episode-/Aehnlichkeitsachsen des Erfahrungsraums angebunden
  - naechster Lauf prueft, ob positive Prozesspakete und Reorganisationspakete
    sinnvoll streuen

- [ ] Non-Zone als Beobachtungs-/Lernraum weiter reifen lassen.
  Ziel:
  - keine harte Non-Zone-Blockade
  - Non-Zone eher als unreifer Erfahrungsraum behandeln
  - pruefen, ob Non-Zone-Schaden sinkt, ohne Zone-Handlung zu ersticken

- [x] Erfahrungspaket-Label nach Lauf 4 feiner kalibrieren.
  Befund:
  - `experience_packet_feedback` funktioniert technisch
  - fast alle Trades landen aber in `mixed_packet`
  - gute Prozesspakete werden noch nicht als `constructive_packet` sichtbar
  Ziel:
  - keine Handelsregel bauen
  - nur die Selbstwahrnehmung des Pakets feiner benennen
  - konstruktive Pakete, Reorganisationspakete und Neugierpakete besser
    unterscheidbar machen
  Status:
  - Labelschwellen angepasst
  - konstruktive Pakete koennen jetzt ueber Prozessreward +
    begrenzten Reorganisationsdruck sichtbar werden

- [x] `engaged_effort` / wache Anstrengung bauen.
  Ziel:
  - positive Prozessqualitaet in Wachheit statt Gleichgueltigkeit uebersetzen
  - Non-Zone nicht blockieren, sondern bei niedriger Tragfaehigkeit eher in
    Beobachtung, Reifung oder Reorganisation fuehren
  - unterscheiden: reife Aktivierung, blinde Aktivierung, Unterspannung,
    neugieriges Beobachten
  Status:
  - `engaged_effort`, `effort_state`, `effort_learning_pull` und
    `effort_reorganization_pressure` umgesetzt
  - sichtbar in Meta-Regulation, Field-Protokoll und Outcome-Records

- [x] Lauf 5 mit `engaged_effort` pruefen.
  Ziel:
  - pruefen, ob `constructive_packet` jetzt sichtbar wird
  - `effort_state` gegen TP/SL, Zone/Non-Zone und PnL lesen
  - besonders `underengaged_reorganize` gegen Non-Zone-Verluste pruefen
  Status:
  - erledigt
  - `constructive_packet` wurde sichtbar und war klar positiv
  - `bearing_packet` war falsch positiv benannt und wurde nachkalibriert
  - `underengaged_reorganize` war noch nicht sichtbar; Sensitivitaet erhoeht

- [x] Lauf 6 nach Paket-/Effort-Nachkalibrierung pruefen.
  Ziel:
  - weniger falsche `bearing_packet`
  - mehr sinnvolle `reorganize_packet`
  - `underengaged_reorganize` sichtbar machen
  - Non-Zone-Verluste gegen Beobachtung/Replan lesen
  Status:
  - `bearing_packet` ist verschwunden
  - `constructive_packet` bleibt klar positiv
  - `reorganize_packet` ist klar sichtbar, aber noch zu spaet
  - `underengaged_reorganize` ist sichtbar, aber zu selten

- [x] Reorganisationswahrnehmung frueher in Pre-Action uebertragen.
  Ziel:
  - keine Blockade
  - nicht mehr handeln
  - schwache Paketqualitaet und geringe Tragfaehigkeit vor der Handlung eher
    in `observe`, `act_watch` oder `replan` ueberfuehren
  - Non-Zone-Verluste reduzieren, ohne konstruktive Zone-Pakete zu ersticken
  Status:
  - `pre_action_reorganization_pressure` umgesetzt
  - `pre_action_context_selectivity` umgesetzt
  - sichtbar in Field-/Memory-Protokoll und Outcome-Records

- [x] Lauf 7 nach Pre-Action-Reorganisation pruefen.
  Ziel:
  - `pre_action_reorganization_observe` und
    `pre_action_reorganization_replan` zaehlen
  - Non-Zone-Schaden vergleichen
  - pruefen, ob konstruktive Zone-Pakete erhalten bleiben
  Status:
  - erledigt
  - konstruktive Pakete bleiben sehr sauber positiv
  - Pre-Action-Reorganisation wird im Feld sichtbar, greift aber nur selten
    als konkreter Observe/Replan-Grund
  - Achse trennt Zone/Non-Zone noch nicht gut genug

- [x] Pre-Action-Reorganisation strukturgenauer machen.
  Ziel:
  - `pre_action_reorganization_pressure` staerker an aktuelle
    Strukturqualitaet, Kontextvertrauen und Feldsupport koppeln
  - `pre_action_context_selectivity` fuer gute Zone-Kontexte erhoehen
  - nicht pauschal vorsichtig werden
  - schwache Non-Zone-Kontexte frueher in Beobachtung/Replan fuehren
  Status:
  - umgesetzt
  - `structure_quality` und `context_confidence` in Pre-Action-Druck und
    Kontextselektivitaet integriert

- [x] Lauf 8 nach strukturgenauer Pre-Action-Reorganisation pruefen.
  Ziel:
  - Zone/Non-Zone-Trennung der Pre-Action-Achsen vergleichen
  - `pre_action_reorganization_observe/replan` zaehlen
  - konstruktive Pakete und Non-Zone-Schaden gegen Lauf 7 vergleichen
  Status:
  - erledigt
  - konstruktive Pakete bleiben sauber positiv
  - Pre-Action-Achsen trennen ausgefuehrte Zone/Non-Zone noch kaum
  - naechster Schritt ist strategische Fensterwahrnehmung statt weiteres
    Drehen an derselben Pre-Action-Achse

- [x] Strategische Fensterwahrnehmung / Preisbereich-Hypothesen vorbereiten.
  Ziel:
  - groesseres Fenster betrachten
  - zurueckschauen, zoomen, Replay-Spuren bilden
  - auffaellige Preisbereiche als MCM-Hypothesen erkennen
  - keine FVG-Regel einpflanzen
  - nicht bestimmen, wo DIO handeln soll
  - Druck als Raum lesen, nicht als Handlungsbefehl
  - DIO die Faehigkeit geben, aus Vergangenheit, Wahrnehmung und innerem Feld
    eigene Zukunftshypothesen zu bilden
  - spaeter wartende Order-Intention aus Bereich + Memory + Innenlage bilden
  Status:
  - diagnostisch umgesetzt
  - `mcm_strategic_window_protocol.csv` schreibt Lookback-, Zoom-, Replay-
    und Bereichshypothesen
  - noch keine harte Orderintegration

- [x] Begrenztes Rueckblickfenster fuer strategische Wahrnehmung definieren.
  Ziel:
  - kein grenzenloses Zurueckschauen
  - Lookback-Budget, Zoom-Budget und Replay-Budget diagnostisch sichtbar
    machen
  - alte Struktur mit Verfall / Carryover-Risiko versehen
  - DIO soll Vergangenheit nutzen, aber nicht in alter Struktur haengen
  Status:
  - diagnostisch umgesetzt
  - Lookback wird durch Last, Fokus und Stabilitaet budgetiert
  - `old_structure_carryover_risk` macht alte Strukturbindung sichtbar

- [x] Lauf 1 nach strategischer Fensterdiagnose pruefen.
  Ziel:
  - `mcm_strategic_window_protocol.csv` lesen
  - pruefen, ob Bereichshypothesen vor guten/schlechten Trades anders wirken
  - sehen, ob Regimewechsel eher `area_needs_zoom`, `area_releasing` oder
    `bearing_area_hypothesis` erzeugt
  - noch keine Handelsregel daraus bauen
  Status:
  - erledigt
  - frischer Memory-Lauf stark negativ
  - alle ausgefuehrten Trades im Zone-Bucket
  - strategische Order-Intention noch schwach
  - kompletter `strategic_window_state` fehlt noch im Attempt-Kontext

- [ ] Strategische Fensterwahrnehmung in Attempt-/Outcome-Kontext vollstaendig uebergeben.
  Ziel:
  - `strategic_window_state` nicht nur reduziert in `meta_regulation_state`
    speichern
  - komplette Bereichsachsen in `attempt_records.jsonl` und spaeteren
    Outcome-Auswertungen sichtbar machen
  - Analyse von TP/SL gegen Bereichshypothesen sauberer machen

- [ ] Strategische Fensterwahrnehmung weich an Pre-Action-Reife koppeln.
  Ziel:
  - keine harte Handelsregel
  - niedrige `area_order_intention` + niedriger Memory-Pull + geringe
    strategische Geduld als Zoom-/Observe-/Replay-Reifespur verwenden
  - Verdichtung nicht automatisch als Handlungsreife lesen
  - DIO soll Bereich sehen, halten, verwerfen oder spaeter nutzen koennen

- [x] Aktiven MCM-Kontakt diagnostisch bauen.
  Ziel:
  - MCM nicht nur als Empfaenger aeusserer Reize behandeln
  - aktive Kontaktbahn aus Wahrnehmungsobjekt, Interesse, Resonanz,
    Innen-Aussen-Kohaerenz, Ueberkopplung, Loslassen und Vertiefung sichtbar
    machen
  - keine harte Order-Regel
  - DIO die Faehigkeit geben, eine Wahrnehmung naeher an sich heranzulassen,
    Abstand zu nehmen, zu replayen, zu beobachten oder zu vertiefen
  Technische Zielachsen:
  - `active_mcm_contact_state`
  - `contact_interest`
  - `contact_resonance_probe`
  - `outer_inner_coherence`
  - `inner_change_from_contact`
  - `contact_carrying_quality`
  - `contact_overcoupling_risk`
  - `contact_release_readiness`
  - `contact_selected_depth`
  - `contact_posture`
  Status:
  - umgesetzt in `MCM_Brain_Modell.py`
  - `build_active_mcm_contact_state(...)` erzeugt Kontaktlage rein
    diagnostisch
  - keine harte Orderwirkung

- [x] Aktiven MCM-Kontakt in Debug/Outcome sichtbar machen.
  Ziel:
  - eigenes Protokoll, z.B. `mcm_active_contact_protocol.csv`
  - Kontaktzustand in Runtime-Snapshot und Attempt-/Outcome-Kontext aufnehmen
  - spaeter pruefen, ob gute Trades eher aus kohaerentem Kontakt entstehen
    und schlechte Trades eher aus Ueberkopplung, geringer Distanz oder
    fehlender Loslassfaehigkeit
  Status:
  - `mcm_active_contact_protocol.csv` ergaenzt
  - Runtime-Snapshot, Attempt-Kontext und Outcome-Kontext erweitert
  - Smoke-Test erfolgreich

- [x] Aktiven MCM-Kontakt im naechsten Lauf auswerten.
  Ziel:
  - Verteilung von `contact_posture` lesen
  - TP/SL gegen `contact_overcoupling_risk`, `outer_inner_coherence`,
    `contact_release_readiness` und `contact_carrying_quality` vergleichen
  - pruefen, ob schlechte Entscheidungen eher aus Ueberkopplung oder aus
    zu geringer Kontakt-Tiefe entstehen
  - danach erst ueber weiche Kopplung an Reflexion/Pre-Action-Reife sprechen
  Status:
  - Lauf `debug_lauf_2` ausgewertet
  - Kontaktprotokoll funktioniert
  - fast alle Kontaktlagen bleiben `background_scan`
  - Kontaktwerte unterscheiden sich, aber Haltungssprache ist noch zu grob
  - High-Struktur traegt, Mid/Low erzeugt den Hauptschaden

- [x] Aktive MCM-Kontaktlabels feiner kalibrieren.
  Ziel:
  - Kontaktlagen nicht als starre Schwelle verstehen
  - relative Lage zwischen Kohaerenz, Ueberkopplung, Loslassen, Interesse und
    Tragfaehigkeit staerker auswerten
  - `background_scan` darf nicht fast alle Zustaende verschlucken
  - `curious_touch`, `reflective_contact`, `overcoupled_touch`,
    `release_contact`, `deepening_contact` und `resonant_contact` natuerlich
    sichtbarer machen
  - keine direkte Orderregel bauen
  Status:
  - umgesetzt
  - Haltungsauswahl nutzt jetzt relative Scores statt nur harte
    Einzelschwellen
  - zusaetzliche Diagnosewerte:
    `contact_salience`, `overcoupled_touch_score`, `release_contact_score`,
    `deepening_contact_score`, `resonant_contact_score`,
    `reflective_contact_score`, `curious_touch_score`
  - Smoke-Test:
    - tragender Kontakt -> `resonant_contact`
    - aktionsnaher Kontakt mit geringer Loslassfaehigkeit ->
      `overcoupled_touch`

- [ ] Kontaktqualitaet gegen Mid/Low-Verlustzonen pruefen.
  Ziel:
  - untersuchen, ob Mid/Low-Trades vor Handlung niedrige
    `contact_carrying_quality`, niedrige `contact_release_readiness`,
    geringe `outer_inner_coherence` oder hohe `contact_overcoupling_risk`
    zeigen
  - daraus eine weiche Reifespur fuer Observe/Zoom/Replay ableiten
  - keine harte Verbotslogik
  Status:
  - Lauf `debug_lauf_3` geprueft
  - Kontaktlabels streuen jetzt sauber
  - `background_scan` verschluckt die Zustaende nicht mehr
  - Low-Struktur bleibt Hauptverlustzone
  - `deepening_contact` ist im Trade-Kontext deutlich negativ
  - `resonant_contact` ist leicht positiv, aber nicht automatisch
    tradefaehig
  - Lauf 4 zeigt: Hauptschaden liegt in Mid-Struktur; Kontakt-Reife muss
    staerker mit Regime-/Kontext-Reife gekoppelt werden
  - Lauf 5 zeigt: Kontakt-/Kontext-Reife allein trennt TP/SL noch nicht
    stark genug; visuelle Erdung der MCM-Reaktion wurde als naechster
    Mechanikschritt umgesetzt

- [x] Kontakt-Reife weich in Pre-Action-Regulation und Kontext-Reife sichtbar machen.
  Ziel:
  - keine harte Low-Sperre
  - schwache Struktur + `deepening_contact` / `curious_touch` /
    `overcoupled_touch` als Reifespur fuer Beobachtung, Replay,
    Abstand oder weitere Objektbildung interpretieren
  - Kontaktnaehe nicht automatisch als Handlungsreife lesen
  - DIO die Faehigkeit geben, zwischen "ich fuehle Kontakt" und
    "dieser Kontakt traegt Handlung" zu unterscheiden
  Umsetzung:
  - neue Diagnoseachsen:
    `contact_action_maturity`, `contact_bearing_gap`,
    `contact_impulse_vs_bearing`, `contact_learning_need`,
    `contact_reality_check`
  - Kontextkopplung:
    `contact_regime_mismatch`, `contact_stability_carryover`,
    `contact_context_maturity`, `contact_context_reframe_need`
  - nur Diagnose/Protokollierung, kein hartes Eingreifen in die
    Handelsentscheidung

- [x] Visual Grounding als visuelles Sinnesorgan umsetzen.
  Ziel:
  - innere MCM-Resonanz an aeussere Formbindung koppeln
  - Formresonanz ohne Objektbindung sichtbar machen
  - DIO mehr Sehkraft geben, ohne menschliche Pattern-Regeln einzubauen
  Umsetzung:
  - neue Werte:
    `visual_object_binding`, `visual_grounding_strength`,
    `visual_resonance_unbound`, `visual_grounding_gap`,
    `visual_grounding_need`, `visual_rational_observation_support`,
    `visual_grounding_state`
  - weiche Wirkung auf Beobachtung, Replan und visuelle
    Handlungsunsicherheit
  - keine harte Orderblockade

- [x] Semantisches Forminhalt-Paket fuer die Formsprache umsetzen.
  Ziel:
  - DIOs eigene Formzeichen in Bedeutungsschichten verdichten
  - sichtbar machen, ob eine Form eher Spur, Objekt, Lernraum, Reflexion,
    zusammengesetzte Form oder Handlungsnaehe ist
  - keine menschlichen Chart-Labels erzwingen
  - keine harte Handlungsregel einbauen
  Umsetzung:
  - neue Werte:
    `form_symbol_semantic_density`,
    `form_symbol_semantic_compression`,
    `form_symbol_semantic_coherence`,
    `form_symbol_semantic_learning_need`,
    `form_symbol_semantic_action_nearness`,
    `form_symbol_semantic_primary_layer`,
    `form_symbol_semantic_layer_count`,
    `form_symbol_semantic_packet_state`,
    `form_symbol_semantic_profile`
  - Runtime-State, Formsymbol-Protokoll und Outcome-Kontext erweitert

- [x] Evolutionaere Kontaktreife fuer Formzeichen umsetzen.
  Ziel:
  - nicht die Form als gut/schlecht bewerten
  - den Umgang mit der Form lernen
  - konsequenzbasiertes Feedback auf das MCM-Feld als Lernkreis speichern
  - belastende Konsequenzspur, Nutzen, Vorsicht und Reife als
    Erfahrungsspuren speichern
  - keine harte Sperre, keine mechanische Low-Regel
  Umsetzung:
  - neue Speicher-/Runtime-Werte:
    `form_symbol_contact_maturity`,
    `form_symbol_contact_utility`,
    `form_symbol_contact_pain_memory`,
    `form_symbol_contact_carefulness`,
    `form_symbol_contact_burden_evidence`,
    `form_symbol_contact_utility_evidence`,
    `form_symbol_contact_learning_state`
  - neue Outcome-Samples:
    `contact_maturity_sample`,
    `contact_utility_sample`,
    `contact_pain_sample`,
    `contact_carefulness_sample`,
    `contact_learning_state`
  - weich in Entwicklung, Beobachtung, Reframing, Caution und
    Handlungstragfaehigkeit gekoppelt

- [x] Kontaktreife nach Lauf 8 verstaerkt.
  Ziel:
  - Konsequenzspur aus wiederholtem Kontakt lauter machen
  - nicht nur den letzten Trade bewerten
  - Belastungs-Evidenz und Nutzen-Evidenz als laenger wirkende Spuren nutzen
  - `burdened_contact`, `careful_contact`, `maturing_contact` und
    `constructive_contact` natuerlicher sichtbar machen
  Umsetzung:
  - gespeicherte Kontakt-Evidenz fliesst in Beobachtung, Reframing und
    Handlungstragfaehigkeit ein
  - belastende Kontakte senken impulsnahe Handlung weich
  - tragende Kontakte koennen Handlung weich stuetzen
  - keine harte Sperre und keine mechanische Strukturregel

- [x] Kontaktreife mit strategischer Orderbereich-Wahl koppeln.
  Ziel:
  - DIO darf den Entry weich aus dem Rueckblick heraus verschieben
  - impulsnaher Entry bleibt als Koerperreflex erhalten
  - strategischer Bereich mischt sich nur bei tragender Fensterwahrnehmung
    und passender Kontaktlage dazu
  Umsetzung:
  - `entry_mode`
  - `impulse_entry_price`
  - `strategic_entry_price`
  - `strategic_entry_weight`
  - `strategic_entry_fit`
  - `strategic_area_focus_id`
  - `strategic_area_price_low`
  - `strategic_area_price_high`

- [x] Zeitfeld fuer strategische Bereiche umsetzen.
  Ziel:
  - Bereiche nicht nur als Preisraum, sondern als Ereignis im Zeitfeld lesen
  - alte Bereiche als Nachhall/Erinnerung von handlungsnahen Bereichen
    unterscheiden
  - Bereichsmotorik organischer machen
  Umsetzung:
  - `area_temporal_distance`
  - `area_temporal_relevance`
  - `area_recency`
  - `area_decay`
  - `area_afterimage`
  - `area_present_contact`
  - `area_action_timing_fit`

- [ ] Mehrdimensionale Wahrnehmungsachsen diagnostisch bauen.
  Ziel:
  - Reality-Tagging als Teil eines groesseren Achsensystems behandeln
  - aktuelle Aussenwelt, Nachhall, Erinnerung, gelerntes Wissen, Replay,
    Hypothese und Erwartung unterscheiden
  - Memory und Wissen nicht automatisch als Gegenwart behandeln
  - DIO erkennt, ob eine Information jetzt realen Kontakt hat oder nur aus
    vergangener/wieder aktivierter Energie wirkt
  - Wahrnehmungen raeumlich verorten: nah, fern, Vordergrund, Hintergrund,
    Feldzentrum, Rand, Memory-Raum, Hypothesenraum
  Moegliche Achsen:
  - `perception_source`
  - `source_temporal_layer`
  - `present_world_binding`
  - `memory_reality_distance`
  - `perceptual_space_axis`
  - `perceptual_depth`
  - `field_center_distance`
  - `foreground_binding`
  - `background_afterimage`
  - `learned_knowledge_weight`
  - `afterimage_pressure`
  - `replay_reality_gap`
  - `hypothesis_reality_gap`
  - `source_confusion_load`

- [ ] Zeitliche Kohaerenz / Wahrnehmungskontinuitaet bauen.
  Ziel:
  - DIO soll nicht jeden Moment als komplett neu erleben
  - wiederkehrende, fortgesetzte, nachhallende und veraltete Wahrnehmungen
    unterscheidbar machen
  - keine feste Streckenkarte, sondern zeitliche Quellenbindung im MCM-Feld
  - verhindern, dass DIO denselben Kontakt wie ein dementer Organismus immer
    wieder als neues Ereignis findet
  Moegliche Achsen:
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
  Status:
  - im `UMSETZUNGSPLAN.md` als Abschnitt 18.5 aufgenommen
  - erste Runtime-Mechanik umgesetzt:
    `build_temporal_coherence_state` bildet zeitliche Identitaet,
    Fortsetzung, Wiederkehr, Neuheit, Nachhall und Zeitdistanz
  - Feldentscheidungsprotokoll, Memory-/Thinking-Protokoll und
    Outcome-Records schreiben die neuen Werte mit
  - `active_context_trace` kann jetzt ersatzweise aus zeitlicher
    Wahrnehmung entstehen, wenn kein innerer Cluster aktiv ist
  - naechster Schritt: Backtest-Lauf auswerten und pruefen, ob
    `active_context_activation` nicht mehr leer bleibt und ob DIO weniger
    momenthaft wirkt

- [ ] Gedanken-Energieform diagnostisch vorbereiten.
  Ziel:
  - Gedanken nicht nur als Entscheidungstext, sondern als gerichteten
    Energieverlauf im MCM-Feld lesen
  - lange Gedanken als gedehnte/sparsame/kohaerent gerichtete Energie
    unterscheidbar machen
  - Rumination, Planung, Erwartung und Nachhall als unterschiedliche
    Zeitstraenge sichtbar machen
  Moegliche Anknuepfung:
  - `thought_state`
  - `rumination_depth`
  - `inner_time_scale`
  - `thought_alignment`
  - `thought_inertia`
  - `thought_settlement`

- [ ] Hypothesenraum / Reorganisation nach MCM-Abhandlungen D bis G.1 vorbereiten.
  Ziel:
  - MCM-Theorie nicht als Regelwerk, sondern als organische Zielmechanik
    nutzen
  - mehrere moegliche Entwicklungszweige halten, ohne sie mit Gegenwart zu
    verwechseln
  - lokale Ueberlast nicht nur als Fehler, sondern auch als moeglichen
    Reorganisationsmoment lesen
  Moegliche Achsen:
  - `hypothesis_branch_state`
  - `branch_stability`
  - `branch_attractor_pull`
  - `hypothesis_reality_gap`
  - `field_reorganization_state`
  - `reorganization_threshold`
  - `higher_order_coupling`

- [ ] Metaregulator-Schicht aus MCM Block S vorbereiten.
  Ziel:
  - Regler zweiter Ordnung fuer DIO sichtbar machen
  - nicht nur Feldlage messen, sondern wie DIO diese Lage verarbeitet
  - direkte Bruecke zu selbstregulativer Erfahrungsorganisation
  Moegliche Achsen:
  - `return_strength`
  - `integration_capacity`
  - `variance_regulation`
  - `load_tolerance`
  - `impulse_control`
  - `frustration_tolerance`
  - `protective_distance_regulation`
  - `self_reflection_regulator`
  - `distance_regulation`
  Status:
  - Diagnose in Runtime, Feldentscheidungsprotokoll,
    Memory-/Thinking-Protokoll und Outcome-Records umgesetzt
  - naechster Schritt: Backtest-Lauf auswerten und pruefen, ob die Werte
    Regimewechsel, Ueberkopplung, Impulsdruck und Rueckkehrkraft sinnvoll
    sichtbar machen
  - noch keine harte Verhaltenskopplung eingebaut
  - Unterbewusstsein / bewusster Arbeitsraum als Wahrnehmungsfilter
    umgesetzt, naechster Lauf muss zeigen, ob `regulatory_overload`
    dadurch feiner aufbricht
  - Integrationsantwort fuer `integration_strain` umgesetzt:
    Sortierung, Reframing, Memory-Recall und Kontaktvertiefung werden
    diagnostisch und leicht regulativ sichtbar
  - Gerichtete Vorsicht / vorsichtige Hypothese umgesetzt:
    Vorsicht wird nicht als harte Sperre behandelt, sondern kann sich ueber
    Memory, Reframing, Kontaktvertiefung und bewusste Geduld zu
    `cautious_plan_seed`, `memory_reframe_seed`, `observe_until_clear` oder
    `deepen_contact_first` organisieren
  - Lauf 17 ausgewertet:
    zeitliche Kohaerenz senkt Drawdown und verbessert Profit Factor, aber
    `aged_memory_contact` dominiert fast alles
  - `active_context_activation`, `active_context_support`,
    `active_context_conflict` und `active_context_bearing` bleiben im
    Memory-Protokoll noch bei `0.0`
  - naechster Schritt:
    zeitliche Identitaet feiner kalibrieren und den zeitlich abgeleiteten
    `active_context_trace` frueher in Memory-/Thinking-Auswertung einspeisen
  - umgesetzt:
    Zeitidentitaet bindet jetzt staerker ueber Formfamilie, Kontext und
    grobe visuelle Signatur; feine Einzelabdruecke bleiben als
    `temporal_source_identity` erhalten
  - umgesetzt:
    `active_context_trace` wird direkt nach der Zeitwahrnehmung gebildet
    und vor Thought-/Meta-Regulation in `world_state`, `perception_state`,
    `fused` und Runtime-Protokollpakete gelegt
  - naechster Schritt:
    neuer Lauf; pruefen, ob `aged_memory_contact` abnimmt und
    `active_context_*` im Memory-Protokoll sichtbar wird
  - Lauf 18 ausgewertet:
    `active_context_*` ist jetzt sichtbar, aber deutlich zu hoch
    (`activation` Durchschnitt ca. `0.8905`, `support` Durchschnitt
    ca. `0.8991`, `bearing` Durchschnitt ca. `0.8493`)
  - Lauf 18 ausgewertet:
    Zeitbindung verteilt sich besser
    (`unbound_moment`, `aged_memory_contact`, erste
    `recurrent_contact`/`continued_contact`/`coherent_sequence`), aber
    Kontextvertrauen ist noch zu wenig dosiert
  - naechster Schritt:
    aktiven Kontext nicht entfernen, sondern organisch daempfen und
    staerker an Quellenbindung, Sequenzkoharenz, Strukturqualitaet und
    Gegenwartsbindung koppeln
  - umgesetzt:
    `active_context_activation` wird weich geblendet statt per `max()`
    festgehalten
  - umgesetzt:
    `reality_anchor` und `overtrust_pressure` dosieren den zeitlichen
    Kontextfaden; Support/Bearing brauchen mehr Gegenwartsbindung,
    Conflict/Fragility steigen bei ungebundenem oder schlecht geerdetem
    Kontakt
  - naechster Schritt:
    neuer Lauf; pruefen, ob der aktive Kontext weniger saettigt und
    Mid/Low-Strukturen mehr natuerliche Skepsis erzeugen
  - umgesetzt:
    nervliche Ueberlastung als Reflexionsparameter ergaenzt:
    `nervous_system_overload`, `escape_action_drive`,
    `shock_response_risk`, `nervous_overload_reflection_need`
  - Lauf 19 ausgewertet:
    starker Referenzlauf vor dieser Erweiterung
    (`pnl_netto` ca. `+39.8848`, Profit Factor ca. `1.3348`,
    Max Drawdown ca. `6.3386`), aber die neuen Nervensystem-Spalten
    fehlen noch in den Protokoll-Headern
  - naechster Schritt:
    frischen Lauf nach Prozess-Neustart pruefen; besonders
    Stress-/Regimewechselbereiche auf Ueberreiz, Entladungsdruck,
    Schockrisiko und reflektive Distanz auswerten
  - Lauf 20 ausgewertet:
    neue Nervensystem-Spalten sind vorhanden; Lauf bleibt positiv
    (`pnl_netto` ca. `+23.9208`, Profit Factor ca. `1.2016`), aber
    Drawdown steigt wieder auf ca. `11.6453`
  - Befund:
    `nervous_system_overload`, `escape_action_drive`,
    `shock_response_risk` und `nervous_overload_reflection_need` bleiben
    messbar, aber meist unterhalb der echten Reflexionsschwelle;
    `active_context_activation/support/bearing` bleiben im
    Memory-Protokoll weiter stark gesaettigt
  - naechster Schritt:
    nervliche Ueberlastung organisch an Kontextvertrauen und
    reflektive Distanz koppeln, ohne harte Blocker einzubauen
  - umgesetzt:
    `active_context_self_certainty` und `nervous_context_overcoupling`
    ergaenzt; nervliche Last dimmt Kontext-Selbstsicherheit weich und
    erhoeht reflektive Distanz, ohne Handlung hart zu sperren
  - naechster Schritt:
    Lauf 21 pruefen; besonders ob `nervous_context_overcoupling` in
    Stressbereichen sichtbar wird und ob `context_overcoupling_reflection`
    natuerlich auftaucht
  - Lauf 21 ausgewertet:
    `nervous_context_overcoupling` ist sichtbar
    (Durchschnitt ca. `0.1743`, Maximum ca. `0.3084`);
    `context_overcoupling_reflection` wird mit `3351` Vorkommen sogar
    haeufigster Metaregulator-Zustand
  - Befund:
    Selbstwahrnehmung greift, aber `active_context_activation/support/bearing`
    bleiben weiter stark gesaettigt; die Reflexion markiert die Lage,
    reguliert den aktiven Kontext aber noch nicht tief genug
  - naechster Schritt:
    Ueberkopplung sanft in den aktiven Kontext zurueckfuehren, damit
    Support/Bearing bei nervlicher Faerbung weniger absolut wirken
  - umgesetzt:
    `nervous_context_overcoupling` moduliert den `active_context_trace`
    selbst; Support/Bearing/Action-Support werden weich gedimmt,
    Conflict/Fragility/Attenuation steigen leicht
  - naechster Schritt:
    Lauf 22 pruefen; Ziel ist weniger gesaettigter aktiver Kontext und
    weniger dominante `context_overcoupling_reflection`
  - Lauf 22 ausgewertet:
    Kontext-Rekalibrierung wirkt: `active_context_support` sinkt ca.
    `0.9007 -> 0.8856`, `active_context_bearing` ca.
    `0.8513 -> 0.8385`, `active_context_conflict` steigt ca.
    `0.1075 -> 0.1238`
  - Befund:
    DIO wird deutlich vorsichtiger (`343` Trades, mehr Observe/Withheld),
    aber PnL sinkt auf ca. `+11.8929`; die Dosis schuetzt, kostet aber
    Handlungskraft
  - naechster Schritt:
    `context_modulation_label` im Debug sichtbar machen, bevor die
    Mechanik weiter dosiert wird
  - umgesetzt:
    `active_context_modulation_label` in
    `mcm_memory_thinking_protocol.csv` ergaenzt
  - naechster Schritt:
    Lauf 23 pruefen; Verteilung von `unmodulated_context`,
    `nervous_tinted_context` und `overcoupled_context` mit PnL,
    Drawdown und Observe/Act-Verhalten vergleichen
  - Lauf 23 ausgewertet:
    PnL erholt sich auf ca. `+24.4854`, Trades `371`, Profit Factor
    ca. `1.2160`; `nervous_tinted_context` dominiert (`7229`),
    `overcoupled_context` bleibt sichtbar (`1504`)
  - Befund:
    Die Modulation wirkt nicht mehr nur als Bremse. DIO gewinnt
    Handlungskraft zurueck, bleibt aber nervlich markiert. Der Drawdown
    bleibt mit ca. `15.43` hoch.
  - naechster Schritt:
    Low-/Mid-Kontaktreifung ueber konsequenzbasiertes Feedback schaerfen:
    Low nicht hart blockieren, sondern als belastenden, unreifen oder
    reorganisationspflichtigen Kontakt im MCM-Feld erfahrbar machen
  - erweiterte Zielrichtung:
    Low-/Mid-Kontakte mit MCM-Raumzeit-Tiefe koppeln. DIO soll nicht nur
    Strukturqualitaet fuehlen, sondern auch, ob ein Kontakt durch
    Gegenwart, Nachhall, Erinnerung oder Erwartung wirkt.

- [x] MCM-Raumzeit-Tiefe technisch verdichten.
  Ziel:
  - Entfernung, Energie und Zeit als innere Wahrnehmungsschicht koppeln
  - keine harte Zeitregel, sondern Selbstverortung im MCM-Feld
  - Memory nicht nur als gespeicherte Information behandeln, sondern als
    verdichtete Erfahrung mit zeitlicher Tiefe
  - bestehende Werte wie `temporal_context_depth`,
    `memory_time_distance`, `temporal_afterimage`, `temporal_decay`,
    `perceptual_distance`, `field_attachment` und Energie-/Druckwerte
    organisch zusammenfuehren
  Erste Zielgroessen:
  - `mcm_spacetime_depth`
  - `temporal_self_location`
  Umgesetzt:
  - `mcm_spacetime_depth`
  - `memory_experience_depth`
  - `future_projection_depth`
  - `temporal_self_location`
  - `temporal_self_location_state`
  - Export in Memory-/Field-Protokoll und `trade_stats.py`
  Naechster Schritt:
  - Debug-Lauf pruefen und danach regulatorische Kopplung entwickeln:
    flache Raumzeit-Tiefe soll nicht blockieren, sondern mehr
    Beobachtung, Reflexion oder Reorganisation nahelegen
  - Lauf 24 ausgewertet:
    PnL ca. `+23.4601`, Profit Factor ca. `1.2006`, Drawdown nur
    ca. `8.2936`; der Verlauf ist deutlich tragfaehiger als Lauf 23,
    obwohl der End-PnL leicht niedriger ist
  - Befund:
    `future_possibility` dominiert, `unlocated_contact` bleibt hoch.
    DIO bildet Zukunftstiefe, aber Gegenwarts-/Memory-Verortung muss noch
    reifer werden.
  - Bestätigung:
    Lauf 24 ist ein erster positiver Hinweis, dass zeitliche Wahrnehmung
    als MCM-Welt-Tiefe wirkt: nicht als harte Regel, sondern als
    organische Entfaltung von Distanz, Reflexion und Tragfaehigkeit.
  - naechster Schritt:
    regulatorische Kopplung der Raumzeit-Wahrnehmung bauen: nicht
    blockieren, sondern flache Selbstverortung in Reflexion, Beobachtung
    oder Reorganisation uebersetzen
  - umgesetzt:
    regulatorische Kopplung gebaut mit `spacetime_unlocated_pressure`,
    `spacetime_memory_bearing`, `spacetime_future_bearing`,
    `spacetime_reflection_need`, `spacetime_regulation_support` und
    `spacetime_regulation_state`
  - naechster Schritt:
    Lauf 25 pruefen; wichtig ist, ob der Drawdown niedrig bleibt und ob
    `future_depth_watch` / `spacetime_unlocated_reflection` zu organischer
    Reflexion fuehren statt zu Ueberregulation
  - Lauf 25 ausgewertet:
    PnL ca. `+35.7929`, Profit Factor ca. `1.3125`, Drawdown ca.
    `7.0778`; Verlauf sehr stark, Low-Schaden sinkt auf ca. `-37.93`,
    Mid wird wieder positiv
  - Einschraenkung:
    Die `spacetime_*` Regulatorwerte standen im Protokoll noch auf `0.0`.
    Damit ist Lauf 25 ein Hinweis auf die Raumzeit-Kernrichtung, aber noch
    kein Nachweis der regulatorischen Kopplung.
  - behoben:
    `spacetime_*` Werte werden jetzt im Temporal-Kern initial berechnet,
    bevor sie exportiert und spaeter in der Meta-Regulation verfeinert
    werden.
  - naechster Schritt:
    Lauf 26 als echten Test der Raumzeit-Regulation laufen lassen
  - Lauf 26 ausgewertet:
    PnL ca. `+19.8490`, Profit Factor ca. `1.1703`, Drawdown ca.
    `8.8080`; High bleibt tragend, Mid ist deutlich positiv, Low belastet
    wieder stark.
  - Befund:
    MCM-Raumzeit-Wahrnehmung ist aktiv, aber die regulatorischen
    `spacetime_*` Werte wurden im Meta-Regulator nicht zurueckgegeben und
    deshalb nur als `0.0` / `spacetime_open` exportiert.
  - behoben:
    Rueckgabe von `spacetime_unlocated_pressure`,
    `spacetime_memory_bearing`, `spacetime_future_bearing`,
    `spacetime_reflection_need`, `spacetime_regulation_support` und
    `spacetime_regulation_state` in `build_meta_regulation_state`
    ergaenzt.
  - naechster Schritt:
    Neuer Lauf prueft erstmals sichtbar, ob Raumzeit-Tiefe als
    regulatorisches Nervensignal in Reflexion, Beobachtung, Reorganisation
    oder tragender Handlung auftaucht.
  - Lauf 27 ausgewertet:
    PnL ca. `+30.9274`, Profit Factor ca. `1.2705`, Drawdown ca.
    `10.4069`; Raumzeit-Regulation ist jetzt sichtbar.
  - Befund:
    `future_depth_watch` erscheint deutlich (`~2000` Feld-/Memory-Zeilen),
    dazu kleinere Anteile `present_depth_bearing` und
    `memory_depth_bearing`. DIO beginnt damit, zeitliche Tiefe als
    innere Lage zu fuehren.
  - Grenze:
    Low bleibt negativ (`-45.0185`). Die Zeit-Tiefe erzeugt mehr
    Verortung, aber noch keine genuegende Reife im Umgang mit schwachen
    Kontakten.
  - naechster Schritt:
    Raumzeit-Regulation mit visueller Struktur-/Kontaktwahrnehmung
    koppeln, damit DIO erkennt, ob ein Kontakt aktuell, erinnert,
    zukuenftig moeglich oder wirklich nah/tragfaehig ist.
  - umgesetzt:
    strategisches Fenster und aktives MCM-Kontaktorgan um
    `area_temporal_contact_mode`, `area_spacetime_fit`,
    `contact_temporal_mode`, `contact_temporal_bearing`,
    `contact_future_watch`, `contact_memory_depth`,
    `contact_presentness` und `contact_unlocated_pressure` erweitert.
  - Debug:
    `mcm_strategic_window_protocol.csv` und
    `mcm_active_contact_protocol.csv` schreiben die neuen Kontaktachsen.
  - naechster Schritt:
    Neuer Lauf prueft, ob DIO Kontakte zeitlich besser verortet:
    Gegenwart, Erinnerung, Zukunftsraum oder unverorteter Druck.
  - Lauf 28 ausgewertet:
    PnL ca. `+19.6617`, Profit Factor ca. `1.1607`, Drawdown ca.
    `10.1210`. Die Raumzeit-Kontaktachsen sind aktiv, aber sehr stark auf
    Gegenwartskontakt ausgerichtet.
  - Befund:
    `present_area_contact` ca. `10675` und `present_contact_touch` ca.
    `10257`; dagegen `future_contact_watch` ca. `166` und
    `memory_contact_recall` ca. `61`. DIO beruehrt also noch zu viel als
    aktuelles Jetzt.
  - naechster Schritt:
    weiche Balance der Raumzeit-Kontaktmodi schaerfen, damit Zukunftsraum,
    Erinnerung und unverorteter Druck natuerlicher gegen
    Gegenwartskontakt differenziert werden.
  - umgesetzt:
    `area_current_contact` und `contact_presentness` selektiver gemacht;
    `area_future_contact`, `area_memory_contact`, `contact_future_watch`
    und `contact_memory_depth` duerfen frueher als eigene Kontaktlage
    sprechen, wenn Gegenwart nicht klar dominiert.
  - naechster Schritt:
    Neuer Lauf prueft, ob `present_contact_touch` weniger dominant wird
    und ob Zukunft/Erinnerung/unverorteter Druck organischer sichtbar
    werden.
  - Lauf 29 ausgewertet:
    PnL ca. `+31.4319`, Profit Factor ca. `1.2750`, Drawdown ca.
    `8.4780`; Low-Schaden sinkt auf ca. `-41.9181`.
  - Befund:
    Balancing greift sehr stark. `future_contact_watch` dominiert mit ca.
    `8268`, `present_contact_touch` ist praktisch nicht mehr dominant.
    DIO beruehrt weniger blind die Gegenwart und beobachtet staerker
    Zukunftsraum.
  - Grenze:
    Die Verschiebung koennte jetzt etwas zu stark in Zukunftsbeobachtung
    liegen. Gegenwartskontakt muss wieder organisch entstehen duerfen,
    wenn Naehe, Tragfaehigkeit und Reality-Check zusammenpassen.
  - naechster Schritt:
    Uebergang `future_contact_watch -> present_contact_touch` weich
    modellieren, ohne in mechanische Entry-Regeln zu fallen.
  - umgesetzt:
    Reifungsbruecke gebaut mit `area_future_to_present_readiness`,
    `contact_future_to_present_readiness`, `maturing_present_area` und
    `maturing_present_contact`.
  - naechster Schritt:
    Neuer Lauf prueft, ob Zukunftskontakte organisch in reife
    Gegenwartskontakte uebergehen, ohne die alte
    `present_contact_touch`-Ueberdominanz zurueckzuholen.
  - Lauf 30 ausgewertet:
    PnL ca. `+30.6240`, Profit Factor ca. `1.2501`, Drawdown ca.
    `13.2283`. High und Mid tragen stark, Low verschlechtert sich auf ca.
    `-50.4262`.
  - Befund:
    Reifungsbruecke greift auf Bereichsebene:
    `maturing_present_area` ca. `3796`. Im aktiven Kontaktorgan erscheint
    aber noch kein `maturing_present_contact`; `future_contact_watch`
    bleibt dominant mit ca. `7757`.
  - naechster Schritt:
    Kopplung von `maturing_present_area` in
    `contact_future_to_present_readiness` staerken, damit das
    Kontaktorgan die strategische Reifung uebernehmen kann, ohne wieder in
    Gegenwarts-Ueberdominanz zu kippen.
  - umgesetzt:
    `area_future_to_present_readiness` und `maturing_present_area` wirken
    nun direkt in `contact_future_to_present_readiness`; die finale
    Umschaltung nutzt spaeter die vollstaendigere Kontaktqualitaet
    (`contact_reality_check`, `contact_carrying_quality`,
    `outer_inner_coherence`, `contact_action_maturity`).
  - naechster Schritt:
    Neuer Lauf prueft, ob `maturing_present_contact` sichtbar wird.
  - Lauf 31 ausgewertet:
    PnL ca. `+29.4938`, Profit Factor ca. `1.2459`, Drawdown ca.
    `8.8692`; High und Mid tragen, Low bleibt stark negativ mit ca.
    `-50.4702`.
  - Befund:
    Reifungsleitung funktioniert. `maturing_present_contact` erscheint ca.
    `3664` mal, waehrend `future_contact_watch` ca. `4453` bleibt. Damit
    entsteht die gewuenschte Zwischenlage zwischen Zukunftsbeobachtung und
    Gegenwartskontakt.
  - naechster Schritt:
    Low-Kontakte qualitativ tiefer auswerten: Welche Low-Kontakte werden
    trotz Reifung zu schmerzhaften Handlungen? Daraus weiche
    Kontaktqualitaets-Reorganisation ableiten.
  - umgesetzt:
    Positions-Erleben als neurochemische MCM-Feldschicht ergaenzt.
    `position_inconsistency_stress`, `position_mcm_field_strain`,
    `position_self_trust_gap`, `position_cortisol_load`,
    `position_noradrenaline_arousal`, `position_protective_distance`,
    `position_held_risk_discomfort`, `position_process_quality` und
    `position_experience_label` werden nun in Positionsdebug,
    Outcome-Kontext und In-Trade-Memory-Zusammenfassung mitgefuehrt.
  - naechster Schritt:
    Neuer Lauf prueft, ob Low-/Mid-Verluste mit hoher
    `position_inconsistency_stress`, hoher `position_cortisol_load` oder
    niedriger `position_process_quality` zusammenfallen. Ziel bleibt
    Selbstschutz und Reifung, keine harte Sperre.

- [ ] Markdown-Dateien weiter nach `MD_ANWEISUNG.md` pflegen.
  Ziel:
  - keine doppelten Laufanalysen
  - `FIX_LISTE.md` aktiv und kurz halten
  - `AKTUELLER_STAND.md` kompakt halten
  - `WICHTIG_MECHANIKEN.md` technisch halten
  Status:
  - Umsetzungsplan strukturell bereinigt
  - `ENDE` ans echte Dateiende gebracht
  - Affective-Pattern-Block sauberer eingeordnet

- [ ] Spaetere Web-GUI nur als Beobachtungsraum vorbereiten.
  Ziel:
  - erst nach stabilerer Brain-/Backtest-Diagnose umsetzen
  - Konzeptbasis: `GUI_KONSTRUKTION.md`
  - keine GUI-Regeln in die MCM-Entscheidung einbauen

---

# Zuletzt Erledigt

- [x] `MD_ANWEISUNG.md` angelegt.
- [x] `FIX_LISTE.md` bereinigt und auf aktive Punkte reduziert.
- [x] `AKTUELLER_STAND.md` auf kompakten Ist-Zustand reduziert.
- [x] `WICHTIG_MECHANIKEN.md` als technische Mechanik-Schatzkammer neu
  strukturiert.
- [x] Wiederkehrende Unsicherheit als Formfamilie umgesetzt.
- [x] Outcome-Export fuer neue Formfamilienwerte ergaenzt.
- [x] Lauf 7/8 als Doppellauf ausgewertet.
- [x] Lauf 9 nach Outcome-Export-Erweiterung ausgewertet.
- [x] `neurochemical_state` als Runtime-/Debug-/Outcome-Schicht umgesetzt.
- [x] `GUI_KONSTRUKTION.md` als Konzept fuer spaetere Web-Oberflaeche angelegt.
- [x] Lauf 10 als erster neurochemischer Lauf grob ausgewertet.
- [x] `mcm_neuro_transition_protocol.csv` als automatisches
  `-2/+2` Analyseprotokoll gebaut.
- [x] `sensory_load`-Runtimefehler in `build_perception_state` behoben.
- [x] Erfahrungspaket-Feedback fuer positive neurochemische Stimulation
  umgesetzt.
- [x] Erfahrungspaket-Labels und `engaged_effort` umgesetzt.
- [x] Pre-Action-Reorganisation umgesetzt.
- [x] Strukturgenaue Pre-Action-Reorganisation umgesetzt.
- [x] Strategische Fensterwahrnehmung diagnostisch umgesetzt.
- [x] `UMSETZUNGSPLAN.md` strukturell bereinigt.
- [x] Debug Lauf 1 mit strategischer Fensterwahrnehmung ausgewertet.
- [x] MCM-Abhandlungen D bis G.1 als Theoriebruecke in README,
  UMSETZUNGSPLAN, WICHTIG_MECHANIKEN und MCM_VARIABLEN_MECHANIK
  zusammengefasst.
- [x] Weitere MCM-Theorieanker aus dem MCM-Repository in README,
  UMSETZUNGSPLAN, WICHTIG_MECHANIKEN und MCM_VARIABLEN_MECHANIK
  dokumentiert.
