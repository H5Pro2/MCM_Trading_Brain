# FIX_LISTE

Rolle dieser Datei:
- aktive Aufgaben
- nächste Prüfpunkte
- kurze Statusmarkierung

Details, Laufanalysen und Forschungsdeutung gehören nicht hierher.
Regelwerk: `files/MD_ANWEISUNG.md`.

---

# Aktiver Fokus

- [x] `_gui.py` vereinfacht und neu angeordnet.
  - Nur noch Markt-/Chartfenster, Candle State, Trade Stats/KPI,
    Backtest-Prozent und Equity-Kurve.
  - Zusätzliche Diagnose-, Memory-, Innenwelt- und Neuronenpanels entfernt.
  - `_gui.py` nutzt automatisch den neuesten `debug/debug_lauf_x`-Ordner.
  - Optionaler Start mit `--debug-run debug_lauf_44`.
  - `py_compile` für `_gui.py` sauber.

- [x] Emergenz als Kernprinzip ergänzt.
  - Emergenz wird nicht direkt programmiert.
  - MCM stellt den Möglichkeitsraum bereit, in dem sich stabile emergente
    Varianz, Strukturdeutung, Reife und Verhalten bilden können.
  - Profit/PnL ist nicht Kernziel, sondern mögliches Nebenprodukt
    tragfähiger innerer Organisation.
  - Ergänzt in `README.md`, `UMSETZUNGSPLAN.md`,
    `WICHTIG_MECHANIKEN.md` und `AKTUELLER_STAND.md`.

- [x] Markdown-Umlaute korrigiert.
  - `README.md` und `files/*.md` von häufigen `ae/oe/ue`-Schreibweisen
    auf echte UTF-8-Umlaute umgestellt.
  - Code, Variablennamen, technische Keys und Dateinamen bleiben ASCII.

- [x] Erfahrungsbericht zum Bau und Verhalten des DIO/MCM-Systems angelegt.
  - Datei: `files/ERFAHRUNGSBERICHT_DIO_MCM.md`
  - Zweck: technische Forschungsnotiz über Sprünge, Verhalten und
    Besonderheiten der nichtklassischen MCM-Programmierung.

- [x] Neurochemische Alias-Schicht bauen.
  Ziel:
  - `neurochemical_state` im Runtime-Ergebnis erzeugen
  - vorhandene Werte als technische Achsen bündeln:
    `dopamine_tone`, `gaba_inhibition`, `noradrenaline_arousal`,
    `acetylcholine_focus`, `serotonin_stability`, `cortisol_load`,
    `endorphin_relief`, `glutamate_activation`
  - zunächst Diagnose/Debug, später weiche Meta-Regulation

- [ ] Nächsten Lauf mit neurochemischer Diagnose prüfen.
  Ziel:
  - TP/SL gegen `cortisol_load`, `gaba_inhibition`, `dopamine_tone`,
    `acetylcholine_focus`, `serotonin_stability` und `neurochemical_balance`
    auswerten
  - Regimewechsel nicht mechanisch bewerten, sondern Last/Support lesen
  - Lauf 10 als ersten neurochemischen Referenzlauf nutzen

- [x] Neurochemische Übergaenge aus Lauf 10 vertiefen.
  Ziel:
  - `serotonin_stability -> glutamate_activation` gegen Handlung näher
    untersuchen
  - strukturelle Kipp-Momente mit `cortisol_load`, `gaba_inhibition`,
    `zero_point_regulation` und `observe` vergleichen
  - klären, ob DIO aus Stabilität aktiviert oder aus Last kippt
  Befund:
  - erster `-2/+2` Kerzenvergleich spricht für zwei Muster:
    Glutamat-Aktivierung aus stabiler Grundlage vs. Cortisol-Kippmoment bei
    Volumen-/Range-Spikes

- [ ] Neues neurochemisches Übergangsprotokoll im nächsten Lauf prüfen.
  Ziel:
  - `mcm_neuro_transition_protocol.csv` auf Vollständigkeit prüfen
  - Transitionen gegen TP/SL, `observe`, `act_watch`, `act` und
    `zero_point_regulation` lesen
  - klären, ob DIO aus Stabilität aktiviert oder unter Last kippt
  Status:
  - Lauf 11 bestätigt Protokollausgabe.
  - Nächster Schritt: Zone-Verlust gegen Non-Zone-Verbesserung auswerten.

- [ ] Zone-Präzision gegen Transferfähigkeit untersuchen.
  Ziel:
  - klären, warum Non-Zone in Lauf 11 besser wurde, Zone aber schwacher
  - `glutamate_activation` bei SL gegen TP vergleichen
  - prüfen, ob DIO zu viel Aktivierung in eigentlich bekannten Zonen
    zugelassen hat
  Befund:
  - Lauf 11 zeigt Aktivierung ohne ausreichend tragende Reife als Kernrisiko.
  - Non-Zone profitierte leicht von mehr Transfer, Zone verlor
    Auswahlpräzision.

- [ ] Aktivierungs-Tragfähigkeit als Diagnoseachse vorbereiten.
  Ziel:
  - keine harte Regel bauen
  - `glutamate_activation` gegen `neurochemical_balance`,
    `action_inhibition`, `action_clearance`, `transfer_bearing` und
    `variant_bearing_memory` lesen
  - unterscheiden zwischen reifer Aktivierung und nervlicher Überfeuerung

- [x] Core-Engine Wahrnehmungsübersetzung entlasten.
  Ziel:
  - prüfen, ob Chartreize mehrfach als gleichgerichteter Alarm wirken
  - Risiko-/Threat-Achse mit echter Rückregulation versehen
  - keine harte Regel, sondern sensorische Habituation und Reizverdichtung
  - DIO soll Form sehen, nicht dauerhaft im Stressmilieu tasten
  Befund:
  - Lauf 11 zeigt fast permanent `stressed` und stark negative
    `mean_risk`-Achse.
  - `visual_form_pressure` ist stark mit mehreren Außenreizachsen
    gekoppelt.

- [ ] Nächsten Lauf nach sensorischer Entdoppelung prüfen.
  Ziel:
  - `self_state=stressed`-Anteil und `mean_risk` vergleichen
  - `mcm_visual_cortex_protocol.csv` auf `sensory_redundancy`,
    `sensory_gate` und `sensory_reality_label` prüfen
  - klären, ob DIO weniger doppelte Strukturreize und mehr klare
    Realitätsform wahrnimmt

- [x] Nächsten Lauf nach Outcome-Export-Erweiterung prüfen.
  Ziel:
  - prüfen, ob `outcome_records.jsonl` jetzt Formfamilienwerte enthält
  - TP/SL gegen `variant_learning_pressure`, `uncertainty_familiarity`,
    `variant_bearing_memory`, `visual_action_uncertainty` auswerten
  - Lauf 8 als Referenz nutzen

- [ ] Regimewechsel-Bewaeltigung aus Lauf 9 vertiefen.
  Ziel:
  - klären, warum Formvertrautheit nicht immer zu Handlungssicherheit wird
  - `memory_compare_load`, `orientation_gap`, `blind_thinking_load`,
    `action_clearance`, `action_inhibition` gegen TP/SL betrachten
  - keine harte Regel ableiten, sondern Reife-/Tragfähigkeitsdiagnostik
    verbessern

- [ ] Sensorische Erfahrungssynchronisation nach Lauf 12/13 prüfen.
  Ziel:
  - klären, ob alte Memory-Signaturen zur neuen sensorischen Kodierung passen
  - nicht den Speicher löschen, sondern Anpassungsdruck sichtbar machen
  - `memory_compare_load`, `sensory_gate`, `visual_form_pressure`,
    `action_inhibition`, `regulated_courage` und PnL-Verlauf gemeinsam lesen

- [ ] Serotonin-Nachhall beim Regimewechsel prüfen.
  Ziel:
  - erkennen, ob `serotonin_carryover_risk` im Abverkauf steigt
  - prüfen, ob DIO weiter aus alter Stabilitätslage handelt
  - `emotional_decoupling` und `reactive_nervous_drive` gegen TP/SL und
    Equity-Bruch lesen

- [x] Selektive Wahrnehmung / perzeptive Regulation als nächsten
  Architekturblock vorbereiten.
  Ziel:
  - Wahrnehmungen nicht hart filtern, sondern ihre Nähe zum MCM-Feld weich
    regulieren
  - `perceptual_distance`, `object_contact_depth`, `field_attachment`,
    `release_capacity`, `selective_attention`, `background_containment`,
    `reflective_distance` und `inner_outer_alignment` als Zielachsen prüfen
  - DIO soll Reize sehen, vertiefen oder ablegen können, ohne jeden Eindruck
    vollständig zu durchleben

- [x] Bewusste Wahrnehmung / innere Reizwirkungsanalyse diagnostisch bauen.
  Ziel:
  - nicht nur Reize dämpfen, sondern ihre Wirkung im MCM-Feld bewusst lesbar
    machen
  - prüfen: Was hat der äußere Reiz mit dem MCM-Feld gemacht?
  - Zielachsen: `conscious_perception_state`, `stimulus_field_effect`,
    `inner_impact_trace`, `perceived_field_change`, `felt_afterimage`,
    `object_release_state`, `inner_outer_reflection`
  - Grundlage für echte Reflexion und regulatorische Steuerung schaffen

- [ ] Lauf 17 mit bewusster Wahrnehmung auswerten.
  Ziel:
  - `conscious_perception_state`, `field_attachment`, `perceptual_distance`,
    `release_capacity` und `inner_outer_alignment` gegen TP/SL,
    Regimewechsel und Equity-Verlauf lesen
  - prüfen, ob DIO im Abverkauf überkoppelt, reflektiv Abstand findet oder
    Reize loslassen kann
  - danach erst entscheiden, ob eine weiche Regulation auf diese Achsen
    aufgebaut wird

- [x] Bewusste Wahrnehmungslabels feiner kalibrieren.
  Befund aus neuem `debug_lauf_1`:
  - alle Protokollzeilen stehen auf `open_perception`
  - alle Release-Zustände stehen auf `holding`
  - numerische Achsen bewegen sich, aber die Labels unterscheiden noch nicht
    fein genug
  Ziel:
  - keine harte Handelsregel
  - Labels dynamischer aus relativer Innenlage bilden
  - `object_contact`, `reflective_check`, `overcoupled_field` und
    `release_ready` natürlich sichtbar machen

- [x] Lauf 2 mit innerer Haltung auswerten.
  Ziel:
  - prüfen, ob `conscious_perception_state` und `inner_posture_state` nun
    streuen
  - `curious`, `excited`, `overstimulated`, `tired`, `calm` und `reflective`
    gegen TP/SL, Equity-Bruch und Regimewechsel lesen
  - keine harte Regel ableiten, sondern erst prüfen, welche inneren
    Haltungen tragfähig oder belastend werden

- [x] Diffuse Offenheit weich weiterentwickeln.
  Befund aus Lauf 2:
  - `uncertain_open` und `open_perception` waren bei Trades negativ
  - benannte Aktivierung wie `excited`, `curious` oder `overcoupled_field`
    war nicht automatisch schlecht
  Ziel:
  - keine harte Blockade auf `uncertain_open`
  - DIO soll diffuse Offenheit eher in Beobachtung, Objektkontakt,
    Reflexion oder Loslassen überführen
  - prüfen, ob dadurch weniger blinde Handlungen entstehen

- [ ] Lauf 3 mit diffuser Offenheitsreifung prüfen.
  Ziel:
  - `diffuse_open_development_pressure` und `posture_development_hint` gegen
    TP/SL und Equity-Verlauf lesen
  - prüfen, ob `uncertain_open`-Trades sinken
  - prüfen, ob gute Aktivierung (`curious`, `excited`, tragendes
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
    prüfen
  - Non-Zone bei niedriger Tragfähigkeit eher in Beobachtungslernen,
    Reflexion oder Loslassen überführen

- [x] Erfahrungspaket-Feedback / positive Stimulation bauen.
  Ziel:
  - kein `TP = gut` / `SL = schlecht`
  - gesamtes Paket bewerten: Struktur, Innenlage, Wahrnehmung, Haltung,
    Handlung, Risiko, Ergebnis, Wiederholbarkeit
  - gute Prozessleistung positiv stimulieren
  - schlechte Paketqualität als Reorganisationssignal nutzen
  - auch Abverkauf positiv bewerten können, wenn Entscheidung und Prozess
    tragfähig waren
  - Grundlage für `engaged_effort` als positiv getragene Wachheit schaffen
  Status:
  - umgesetzt in `build_experience_packet_feedback`
  - sichtbar in `last_outcome_decomposition` und `outcome_records.jsonl`
  - in Episode-/Ähnlichkeitsachsen des Erfahrungsraums angebunden
  - nächster Lauf prüft, ob positive Prozesspakete und Reorganisationspakete
    sinnvoll streuen

- [ ] Non-Zone als Beobachtungs-/Lernraum weiter reifen lassen.
  Ziel:
  - keine harte Non-Zone-Blockade
  - Non-Zone eher als unreifer Erfahrungsraum behandeln
  - prüfen, ob Non-Zone-Schaden sinkt, ohne Zone-Handlung zu ersticken

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
  - konstruktive Pakete können jetzt über Prozessreward +
    begrenzten Reorganisationsdruck sichtbar werden

- [x] `engaged_effort` / wache Anstrengung bauen.
  Ziel:
  - positive Prozessqualität in Wachheit statt Gleichgueltigkeit übersetzen
  - Non-Zone nicht blockieren, sondern bei niedriger Tragfähigkeit eher in
    Beobachtung, Reifung oder Reorganisation führen
  - unterscheiden: reife Aktivierung, blinde Aktivierung, Unterspannung,
    neugieriges Beobachten
  Status:
  - `engaged_effort`, `effort_state`, `effort_learning_pull` und
    `effort_reorganization_pressure` umgesetzt
  - sichtbar in Meta-Regulation, Field-Protokoll und Outcome-Records

- [x] Lauf 5 mit `engaged_effort` prüfen.
  Ziel:
  - prüfen, ob `constructive_packet` jetzt sichtbar wird
  - `effort_state` gegen TP/SL, Zone/Non-Zone und PnL lesen
  - besonders `underengaged_reorganize` gegen Non-Zone-Verluste prüfen
  Status:
  - erledigt
  - `constructive_packet` wurde sichtbar und war klar positiv
  - `bearing_packet` war falsch positiv benannt und wurde nachkalibriert
  - `underengaged_reorganize` war noch nicht sichtbar; Sensitivitaet erhoeht

- [x] Lauf 6 nach Paket-/Effort-Nachkalibrierung prüfen.
  Ziel:
  - weniger falsche `bearing_packet`
  - mehr sinnvolle `reorganize_packet`
  - `underengaged_reorganize` sichtbar machen
  - Non-Zone-Verluste gegen Beobachtung/Replan lesen
  Status:
  - `bearing_packet` ist verschwunden
  - `constructive_packet` bleibt klar positiv
  - `reorganize_packet` ist klar sichtbar, aber noch zu spät
  - `underengaged_reorganize` ist sichtbar, aber zu selten

- [x] Reorganisationswahrnehmung früher in Pre-Action übertragen.
  Ziel:
  - keine Blockade
  - nicht mehr handeln
  - schwache Paketqualität und geringe Tragfähigkeit vor der Handlung eher
    in `observe`, `act_watch` oder `replan` überführen
  - Non-Zone-Verluste reduzieren, ohne konstruktive Zone-Pakete zu ersticken
  Status:
  - `pre_action_reorganization_pressure` umgesetzt
  - `pre_action_context_selectivity` umgesetzt
  - sichtbar in Field-/Memory-Protokoll und Outcome-Records

- [x] Lauf 7 nach Pre-Action-Reorganisation prüfen.
  Ziel:
  - `pre_action_reorganization_observe` und
    `pre_action_reorganization_replan` zaehlen
  - Non-Zone-Schaden vergleichen
  - prüfen, ob konstruktive Zone-Pakete erhalten bleiben
  Status:
  - erledigt
  - konstruktive Pakete bleiben sehr sauber positiv
  - Pre-Action-Reorganisation wird im Feld sichtbar, greift aber nur selten
    als konkreter Observe/Replan-Grund
  - Achse trennt Zone/Non-Zone noch nicht gut genug

- [x] Pre-Action-Reorganisation strukturgenauer machen.
  Ziel:
  - `pre_action_reorganization_pressure` stärker an aktuelle
    Strukturqualität, Kontextvertrauen und Feldsupport koppeln
  - `pre_action_context_selectivity` für gute Zone-Kontexte erhöhen
  - nicht pauschal vorsichtig werden
  - schwache Non-Zone-Kontexte früher in Beobachtung/Replan führen
  Status:
  - umgesetzt
  - `structure_quality` und `context_confidence` in Pre-Action-Druck und
    Kontextselektivitaet integriert

- [x] Lauf 8 nach strukturgenauer Pre-Action-Reorganisation prüfen.
  Ziel:
  - Zone/Non-Zone-Trennung der Pre-Action-Achsen vergleichen
  - `pre_action_reorganization_observe/replan` zaehlen
  - konstruktive Pakete und Non-Zone-Schaden gegen Lauf 7 vergleichen
  Status:
  - erledigt
  - konstruktive Pakete bleiben sauber positiv
  - Pre-Action-Achsen trennen ausgeführte Zone/Non-Zone noch kaum
  - nächster Schritt ist strategische Fensterwahrnehmung statt weiteres
    Drehen an derselben Pre-Action-Achse

- [x] Strategische Fensterwahrnehmung / Preisbereich-Hypothesen vorbereiten.
  Ziel:
  - größeres Fenster betrachten
  - zurückschauen, zoomen, Replay-Spuren bilden
  - auffällige Preisbereiche als MCM-Hypothesen erkennen
  - keine FVG-Regel einpflanzen
  - nicht bestimmen, wo DIO handeln soll
  - Druck als Raum lesen, nicht als Handlungsbefehl
  - DIO die Fähigkeit geben, aus Vergangenheit, Wahrnehmung und innerem Feld
    eigene Zukunftshypothesen zu bilden
  - später wartende Order-Intention aus Bereich + Memory + Innenlage bilden
  Status:
  - diagnostisch umgesetzt
  - `mcm_strategic_window_protocol.csv` schreibt Lookback-, Zoom-, Replay-
    und Bereichshypothesen
  - noch keine harte Orderintegration

- [x] Begrenztes Rückblickfenster für strategische Wahrnehmung definieren.
  Ziel:
  - kein grenzenloses Zurückschauen
  - Lookback-Budget, Zoom-Budget und Replay-Budget diagnostisch sichtbar
    machen
  - alte Struktur mit Verfall / Carryover-Risiko versehen
  - DIO soll Vergangenheit nutzen, aber nicht in alter Struktur hängen
  Status:
  - diagnostisch umgesetzt
  - Lookback wird durch Last, Fokus und Stabilität budgetiert
  - `old_structure_carryover_risk` macht alte Strukturbindung sichtbar

- [x] Lauf 1 nach strategischer Fensterdiagnose prüfen.
  Ziel:
  - `mcm_strategic_window_protocol.csv` lesen
  - prüfen, ob Bereichshypothesen vor guten/schlechten Trades anders wirken
  - sehen, ob Regimewechsel eher `area_needs_zoom`, `area_releasing` oder
    `bearing_area_hypothesis` erzeugt
  - noch keine Handelsregel daraus bauen
  Status:
  - erledigt
  - frischer Memory-Lauf stark negativ
  - alle ausgeführten Trades im Zone-Bucket
  - strategische Order-Intention noch schwach
  - kompletter `strategic_window_state` fehlt noch im Attempt-Kontext

- [ ] Strategische Fensterwahrnehmung in Attempt-/Outcome-Kontext vollständig übergeben.
  Ziel:
  - `strategic_window_state` nicht nur reduziert in `meta_regulation_state`
    speichern
  - komplette Bereichsachsen in `attempt_records.jsonl` und späteren
    Outcome-Auswertungen sichtbar machen
  - Analyse von TP/SL gegen Bereichshypothesen sauberer machen

- [ ] Strategische Fensterwahrnehmung weich an Pre-Action-Reife koppeln.
  Ziel:
  - keine harte Handelsregel
  - niedrige `area_order_intention` + niedriger Memory-Pull + geringe
    strategische Geduld als Zoom-/Observe-/Replay-Reifespur verwenden
  - Verdichtung nicht automatisch als Handlungsreife lesen
  - DIO soll Bereich sehen, halten, verwerfen oder später nutzen können

- [x] Aktiven MCM-Kontakt diagnostisch bauen.
  Ziel:
  - MCM nicht nur als Empfaenger äußerer Reize behandeln
  - aktive Kontaktbahn aus Wahrnehmungsobjekt, Interesse, Resonanz,
    Innen-Außen-Kohärenz, Überkopplung, Loslassen und Vertiefung sichtbar
    machen
  - keine harte Order-Regel
  - DIO die Fähigkeit geben, eine Wahrnehmung näher an sich heranzulassen,
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
  - später prüfen, ob gute Trades eher aus kohärentem Kontakt entstehen
    und schlechte Trades eher aus Überkopplung, geringer Distanz oder
    fehlender Loslassfähigkeit
  Status:
  - `mcm_active_contact_protocol.csv` ergänzt
  - Runtime-Snapshot, Attempt-Kontext und Outcome-Kontext erweitert
  - Smoke-Test erfolgreich

- [x] Aktiven MCM-Kontakt im nächsten Lauf auswerten.
  Ziel:
  - Verteilung von `contact_posture` lesen
  - TP/SL gegen `contact_overcoupling_risk`, `outer_inner_coherence`,
    `contact_release_readiness` und `contact_carrying_quality` vergleichen
  - prüfen, ob schlechte Entscheidungen eher aus Überkopplung oder aus
    zu geringer Kontakt-Tiefe entstehen
  - danach erst über weiche Kopplung an Reflexion/Pre-Action-Reife sprechen
  Status:
  - Lauf `debug_lauf_2` ausgewertet
  - Kontaktprotokoll funktioniert
  - fast alle Kontaktlagen bleiben `background_scan`
  - Kontaktwerte unterscheiden sich, aber Haltungssprache ist noch zu grob
  - High-Struktur trägt, Mid/Low erzeugt den Hauptschaden

- [x] Aktive MCM-Kontaktlabels feiner kalibrieren.
  Ziel:
  - Kontaktlagen nicht als starre Schwelle verstehen
  - relative Lage zwischen Kohärenz, Überkopplung, Loslassen, Interesse und
    Tragfähigkeit stärker auswerten
  - `background_scan` darf nicht fast alle Zustände verschlucken
  - `curious_touch`, `reflective_contact`, `overcoupled_touch`,
    `release_contact`, `deepening_contact` und `resonant_contact` natürlich
    sichtbarer machen
  - keine direkte Orderregel bauen
  Status:
  - umgesetzt
  - Haltungsauswahl nutzt jetzt relative Scores statt nur harte
    Einzelschwellen
  - zusätzliche Diagnosewerte:
    `contact_salience`, `overcoupled_touch_score`, `release_contact_score`,
    `deepening_contact_score`, `resonant_contact_score`,
    `reflective_contact_score`, `curious_touch_score`
  - Smoke-Test:
    - tragender Kontakt -> `resonant_contact`
    - aktionsnaher Kontakt mit geringer Loslassfähigkeit ->
      `overcoupled_touch`

- [ ] Kontaktqualität gegen Mid/Low-Verlustzonen prüfen.
  Ziel:
  - untersuchen, ob Mid/Low-Trades vor Handlung niedrige
    `contact_carrying_quality`, niedrige `contact_release_readiness`,
    geringe `outer_inner_coherence` oder hohe `contact_overcoupling_risk`
    zeigen
  - daraus eine weiche Reifespur für Observe/Zoom/Replay ableiten
  - keine harte Verbotslogik
  Status:
  - Lauf `debug_lauf_3` geprüft
  - Kontaktlabels streuen jetzt sauber
  - `background_scan` verschluckt die Zustände nicht mehr
  - Low-Struktur bleibt Hauptverlustzone
  - `deepening_contact` ist im Trade-Kontext deutlich negativ
  - `resonant_contact` ist leicht positiv, aber nicht automatisch
    tradefähig
  - Lauf 4 zeigt: Hauptschaden liegt in Mid-Struktur; Kontakt-Reife muss
    stärker mit Regime-/Kontext-Reife gekoppelt werden
  - Lauf 5 zeigt: Kontakt-/Kontext-Reife allein trennt TP/SL noch nicht
    stark genug; visuelle Erdung der MCM-Reaktion wurde als nächster
    Mechanikschritt umgesetzt

- [x] Kontakt-Reife weich in Pre-Action-Regulation und Kontext-Reife sichtbar machen.
  Ziel:
  - keine harte Low-Sperre
  - schwache Struktur + `deepening_contact` / `curious_touch` /
    `overcoupled_touch` als Reifespur für Beobachtung, Replay,
    Abstand oder weitere Objektbildung interpretieren
  - Kontaktnähe nicht automatisch als Handlungsreife lesen
  - DIO die Fähigkeit geben, zwischen "ich fühle Kontakt" und
    "dieser Kontakt trägt Handlung" zu unterscheiden
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
  - innere MCM-Resonanz an äußere Formbindung koppeln
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

- [x] Semantisches Forminhalt-Paket für die Formsprache umsetzen.
  Ziel:
  - DIOs eigene Formzeichen in Bedeutungsschichten verdichten
  - sichtbar machen, ob eine Form eher Spur, Objekt, Lernraum, Reflexion,
    zusammengesetzte Form oder Handlungsnähe ist
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

- [x] Evolutionaere Kontaktreife für Formzeichen umsetzen.
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
    Handlungstragfähigkeit gekoppelt

- [x] Kontaktreife nach Lauf 8 verstärkt.
  Ziel:
  - Konsequenzspur aus wiederholtem Kontakt lauter machen
  - nicht nur den letzten Trade bewerten
  - Belastungs-Evidenz und Nutzen-Evidenz als länger wirkende Spuren nutzen
  - `burdened_contact`, `careful_contact`, `maturing_contact` und
    `constructive_contact` natürlicher sichtbar machen
  Umsetzung:
  - gespeicherte Kontakt-Evidenz fliesst in Beobachtung, Reframing und
    Handlungstragfähigkeit ein
  - belastende Kontakte senken impulsnahe Handlung weich
  - tragende Kontakte können Handlung weich stuetzen
  - keine harte Sperre und keine mechanische Strukturregel

- [x] Kontaktreife mit strategischer Orderbereich-Wahl koppeln.
  Ziel:
  - DIO darf den Entry weich aus dem Rückblick heraus verschieben
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

- [x] Zeitfeld für strategische Bereiche umsetzen.
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
  - Reality-Tagging als Teil eines größeren Achsensystems behandeln
  - aktuelle Außenwelt, Nachhall, Erinnerung, gelerntes Wissen, Replay,
    Hypothese und Erwartung unterscheiden
  - Memory und Wissen nicht automatisch als Gegenwart behandeln
  - DIO erkennt, ob eine Information jetzt realen Kontakt hat oder nur aus
    vergangener/wieder aktivierter Energie wirkt
  - Wahrnehmungen raeumlich verorten: nah, fern, Vordergrund, Hintergrund,
    Feldzentrum, Rand, Memory-Raum, Hypothesenraum
  Mögliche Achsen:
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

- [ ] Zeitliche Kohärenz / Wahrnehmungskontinuität bauen.
  Ziel:
  - DIO soll nicht jeden Moment als komplett neu erleben
  - wiederkehrende, fortgesetzte, nachhallende und veraltete Wahrnehmungen
    unterscheidbar machen
  - keine feste Streckenkarte, sondern zeitliche Quellenbindung im MCM-Feld
  - verhindern, dass DIO denselben Kontakt wie ein dementer Organismus immer
    wieder als neues Ereignis findet
  Mögliche Achsen:
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
  - nächster Schritt: Backtest-Lauf auswerten und prüfen, ob
    `active_context_activation` nicht mehr leer bleibt und ob DIO weniger
    momenthaft wirkt

- [ ] Gedanken-Energieform diagnostisch vorbereiten.
  Ziel:
  - Gedanken nicht nur als Entscheidungstext, sondern als gerichteten
    Energieverlauf im MCM-Feld lesen
  - lange Gedanken als gedehnte/sparsame/kohärent gerichtete Energie
    unterscheidbar machen
  - Rumination, Planung, Erwartung und Nachhall als unterschiedliche
    Zeitstraenge sichtbar machen
  Mögliche Anknuepfung:
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
  - mehrere mögliche Entwicklungszweige halten, ohne sie mit Gegenwart zu
    verwechseln
  - lokale Überlast nicht nur als Fehler, sondern auch als möglichen
    Reorganisationsmoment lesen
  Mögliche Achsen:
  - `hypothesis_branch_state`
  - `branch_stability`
  - `branch_attractor_pull`
  - `hypothesis_reality_gap`
  - `field_reorganization_state`
  - `reorganization_threshold`
  - `higher_order_coupling`

- [ ] Metaregulator-Schicht aus MCM Block S vorbereiten.
  Ziel:
  - Regler zweiter Ordnung für DIO sichtbar machen
  - nicht nur Feldlage messen, sondern wie DIO diese Lage verarbeitet
  - direkte Brücke zu selbstregulativer Erfahrungsorganisation
  Mögliche Achsen:
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
  - nächster Schritt: Backtest-Lauf auswerten und prüfen, ob die Werte
    Regimewechsel, Überkopplung, Impulsdruck und Rückkehrkraft sinnvoll
    sichtbar machen
  - noch keine harte Verhaltenskopplung eingebaut
  - Unterbewusstsein / bewusster Arbeitsraum als Wahrnehmungsfilter
    umgesetzt, nächster Lauf muss zeigen, ob `regulatory_overload`
    dadurch feiner aufbricht
  - Integrationsantwort für `integration_strain` umgesetzt:
    Sortierung, Reframing, Memory-Recall und Kontaktvertiefung werden
    diagnostisch und leicht regulativ sichtbar
  - Gerichtete Vorsicht / vorsichtige Hypothese umgesetzt:
    Vorsicht wird nicht als harte Sperre behandelt, sondern kann sich über
    Memory, Reframing, Kontaktvertiefung und bewusste Geduld zu
    `cautious_plan_seed`, `memory_reframe_seed`, `observe_until_clear` oder
    `deepen_contact_first` organisieren
  - Lauf 17 ausgewertet:
    zeitliche Kohärenz senkt Drawdown und verbessert Profit Factor, aber
    `aged_memory_contact` dominiert fast alles
  - `active_context_activation`, `active_context_support`,
    `active_context_conflict` und `active_context_bearing` bleiben im
    Memory-Protokoll noch bei `0.0`
  - nächster Schritt:
    zeitliche Identitaet feiner kalibrieren und den zeitlich abgeleiteten
    `active_context_trace` früher in Memory-/Thinking-Auswertung einspeisen
  - umgesetzt:
    Zeitidentitaet bindet jetzt stärker über Formfamilie, Kontext und
    grobe visuelle Signatur; feine Einzelabdrücke bleiben als
    `temporal_source_identity` erhalten
  - umgesetzt:
    `active_context_trace` wird direkt nach der Zeitwahrnehmung gebildet
    und vor Thought-/Meta-Regulation in `world_state`, `perception_state`,
    `fused` und Runtime-Protokollpakete gelegt
  - nächster Schritt:
    neuer Lauf; prüfen, ob `aged_memory_contact` abnimmt und
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
  - nächster Schritt:
    aktiven Kontext nicht entfernen, sondern organisch dämpfen und
    stärker an Quellenbindung, Sequenzkoharenz, Strukturqualität und
    Gegenwartsbindung koppeln
  - umgesetzt:
    `active_context_activation` wird weich geblendet statt per `max()`
    festgehalten
  - umgesetzt:
    `reality_anchor` und `overtrust_pressure` dosieren den zeitlichen
    Kontextfaden; Support/Bearing brauchen mehr Gegenwartsbindung,
    Conflict/Fragility steigen bei ungebundenem oder schlecht geerdetem
    Kontakt
  - nächster Schritt:
    neuer Lauf; prüfen, ob der aktive Kontext weniger sättigt und
    Mid/Low-Strukturen mehr natürliche Skepsis erzeugen
  - umgesetzt:
    nervliche Überlastung als Reflexionsparameter ergänzt:
    `nervous_system_overload`, `escape_action_drive`,
    `shock_response_risk`, `nervous_overload_reflection_need`
  - Lauf 19 ausgewertet:
    starker Referenzlauf vor dieser Erweiterung
    (`pnl_netto` ca. `+39.8848`, Profit Factor ca. `1.3348`,
    Max Drawdown ca. `6.3386`), aber die neuen Nervensystem-Spalten
    fehlen noch in den Protokoll-Headern
  - nächster Schritt:
    frischen Lauf nach Prozess-Neustart prüfen; besonders
    Stress-/Regimewechselbereiche auf Überreiz, Entladungsdruck,
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
    Memory-Protokoll weiter stark gesättigt
  - nächster Schritt:
    nervliche Überlastung organisch an Kontextvertrauen und
    reflektive Distanz koppeln, ohne harte Blocker einzubauen
  - umgesetzt:
    `active_context_self_certainty` und `nervous_context_overcoupling`
    ergänzt; nervliche Last dimmt Kontext-Selbstsicherheit weich und
    erhoeht reflektive Distanz, ohne Handlung hart zu sperren
  - nächster Schritt:
    Lauf 21 prüfen; besonders ob `nervous_context_overcoupling` in
    Stressbereichen sichtbar wird und ob `context_overcoupling_reflection`
    natürlich auftaucht
  - Lauf 21 ausgewertet:
    `nervous_context_overcoupling` ist sichtbar
    (Durchschnitt ca. `0.1743`, Maximum ca. `0.3084`);
    `context_overcoupling_reflection` wird mit `3351` Vorkommen sogar
    häufigster Metaregulator-Zustand
  - Befund:
    Selbstwahrnehmung greift, aber `active_context_activation/support/bearing`
    bleiben weiter stark gesättigt; die Reflexion markiert die Lage,
    reguliert den aktiven Kontext aber noch nicht tief genug
  - nächster Schritt:
    Überkopplung sanft in den aktiven Kontext zurückführen, damit
    Support/Bearing bei nervlicher Faerbung weniger absolut wirken
  - umgesetzt:
    `nervous_context_overcoupling` moduliert den `active_context_trace`
    selbst; Support/Bearing/Action-Support werden weich gedimmt,
    Conflict/Fragility/Attenuation steigen leicht
  - nächster Schritt:
    Lauf 22 prüfen; Ziel ist weniger gesättigter aktiver Kontext und
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
  - nächster Schritt:
    `context_modulation_label` im Debug sichtbar machen, bevor die
    Mechanik weiter dosiert wird
  - umgesetzt:
    `active_context_modulation_label` in
    `mcm_memory_thinking_protocol.csv` ergänzt
  - nächster Schritt:
    Lauf 23 prüfen; Verteilung von `unmodulated_context`,
    `nervous_tinted_context` und `overcoupled_context` mit PnL,
    Drawdown und Observe/Act-Verhalten vergleichen
  - Lauf 23 ausgewertet:
    PnL erholt sich auf ca. `+24.4854`, Trades `371`, Profit Factor
    ca. `1.2160`; `nervous_tinted_context` dominiert (`7229`),
    `overcoupled_context` bleibt sichtbar (`1504`)
  - Befund:
    Die Modulation wirkt nicht mehr nur als Bremse. DIO gewinnt
    Handlungskraft zurück, bleibt aber nervlich markiert. Der Drawdown
    bleibt mit ca. `15.43` hoch.
  - nächster Schritt:
    Low-/Mid-Kontaktreifung über konsequenzbasiertes Feedback schaerfen:
    Low nicht hart blockieren, sondern als belastenden, unreifen oder
    reorganisationspflichtigen Kontakt im MCM-Feld erfahrbar machen
  - erweiterte Zielrichtung:
    Low-/Mid-Kontakte mit MCM-Raumzeit-Tiefe koppeln. DIO soll nicht nur
    Strukturqualität fühlen, sondern auch, ob ein Kontakt durch
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
    organisch zusammenführen
  Erste Zielgrößen:
  - `mcm_spacetime_depth`
  - `temporal_self_location`
  Umgesetzt:
  - `mcm_spacetime_depth`
  - `memory_experience_depth`
  - `future_projection_depth`
  - `temporal_self_location`
  - `temporal_self_location_state`
  - Export in Memory-/Field-Protokoll und `trade_stats.py`
  Nächster Schritt:
  - Debug-Lauf prüfen und danach regulatorische Kopplung entwickeln:
    flache Raumzeit-Tiefe soll nicht blockieren, sondern mehr
    Beobachtung, Reflexion oder Reorganisation nahelegen
  - Lauf 24 ausgewertet:
    PnL ca. `+23.4601`, Profit Factor ca. `1.2006`, Drawdown nur
    ca. `8.2936`; der Verlauf ist deutlich tragfähiger als Lauf 23,
    obwohl der End-PnL leicht niedriger ist
  - Befund:
    `future_possibility` dominiert, `unlocated_contact` bleibt hoch.
    DIO bildet Zukunftstiefe, aber Gegenwarts-/Memory-Verortung muss noch
    reifer werden.
  - Bestätigung:
    Lauf 24 ist ein erster positiver Hinweis, dass zeitliche Wahrnehmung
    als MCM-Welt-Tiefe wirkt: nicht als harte Regel, sondern als
    organische Entfaltung von Distanz, Reflexion und Tragfähigkeit.
  - nächster Schritt:
    regulatorische Kopplung der Raumzeit-Wahrnehmung bauen: nicht
    blockieren, sondern flache Selbstverortung in Reflexion, Beobachtung
    oder Reorganisation übersetzen
  - umgesetzt:
    regulatorische Kopplung gebaut mit `spacetime_unlocated_pressure`,
    `spacetime_memory_bearing`, `spacetime_future_bearing`,
    `spacetime_reflection_need`, `spacetime_regulation_support` und
    `spacetime_regulation_state`
  - nächster Schritt:
    Lauf 25 prüfen; wichtig ist, ob der Drawdown niedrig bleibt und ob
    `future_depth_watch` / `spacetime_unlocated_reflection` zu organischer
    Reflexion führen statt zu Überregulation
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
    bevor sie exportiert und später in der Meta-Regulation verfeinert
    werden.
  - nächster Schritt:
    Lauf 26 als echten Test der Raumzeit-Regulation laufen lassen
  - Lauf 26 ausgewertet:
    PnL ca. `+19.8490`, Profit Factor ca. `1.1703`, Drawdown ca.
    `8.8080`; High bleibt tragend, Mid ist deutlich positiv, Low belastet
    wieder stark.
  - Befund:
    MCM-Raumzeit-Wahrnehmung ist aktiv, aber die regulatorischen
    `spacetime_*` Werte wurden im Meta-Regulator nicht zurückgegeben und
    deshalb nur als `0.0` / `spacetime_open` exportiert.
  - behoben:
    Rückgabe von `spacetime_unlocated_pressure`,
    `spacetime_memory_bearing`, `spacetime_future_bearing`,
    `spacetime_reflection_need`, `spacetime_regulation_support` und
    `spacetime_regulation_state` in `build_meta_regulation_state`
    ergänzt.
  - nächster Schritt:
    Neuer Lauf prüft erstmals sichtbar, ob Raumzeit-Tiefe als
    regulatorisches Nervensignal in Reflexion, Beobachtung, Reorganisation
    oder tragender Handlung auftaucht.
  - Lauf 27 ausgewertet:
    PnL ca. `+30.9274`, Profit Factor ca. `1.2705`, Drawdown ca.
    `10.4069`; Raumzeit-Regulation ist jetzt sichtbar.
  - Befund:
    `future_depth_watch` erscheint deutlich (`~2000` Feld-/Memory-Zeilen),
    dazu kleinere Anteile `present_depth_bearing` und
    `memory_depth_bearing`. DIO beginnt damit, zeitliche Tiefe als
    innere Lage zu führen.
  - Grenze:
    Low bleibt negativ (`-45.0185`). Die Zeit-Tiefe erzeugt mehr
    Verortung, aber noch keine genuegende Reife im Umgang mit schwachen
    Kontakten.
  - nächster Schritt:
    Raumzeit-Regulation mit visueller Struktur-/Kontaktwahrnehmung
    koppeln, damit DIO erkennt, ob ein Kontakt aktuell, erinnert,
    zukünftig möglich oder wirklich nah/tragfähig ist.
  - umgesetzt:
    strategisches Fenster und aktives MCM-Kontaktorgan um
    `area_temporal_contact_mode`, `area_spacetime_fit`,
    `contact_temporal_mode`, `contact_temporal_bearing`,
    `contact_future_watch`, `contact_memory_depth`,
    `contact_presentness` und `contact_unlocated_pressure` erweitert.
  - Debug:
    `mcm_strategic_window_protocol.csv` und
    `mcm_active_contact_protocol.csv` schreiben die neuen Kontaktachsen.
  - nächster Schritt:
    Neuer Lauf prüft, ob DIO Kontakte zeitlich besser verortet:
    Gegenwart, Erinnerung, Zukunftsraum oder unverorteter Druck.
  - Lauf 28 ausgewertet:
    PnL ca. `+19.6617`, Profit Factor ca. `1.1607`, Drawdown ca.
    `10.1210`. Die Raumzeit-Kontaktachsen sind aktiv, aber sehr stark auf
    Gegenwartskontakt ausgerichtet.
  - Befund:
    `present_area_contact` ca. `10675` und `present_contact_touch` ca.
    `10257`; dagegen `future_contact_watch` ca. `166` und
    `memory_contact_recall` ca. `61`. DIO berührt also noch zu viel als
    aktuelles Jetzt.
  - nächster Schritt:
    weiche Balance der Raumzeit-Kontaktmodi schaerfen, damit Zukunftsraum,
    Erinnerung und unverorteter Druck natürlicher gegen
    Gegenwartskontakt differenziert werden.
  - umgesetzt:
    `area_current_contact` und `contact_presentness` selektiver gemacht;
    `area_future_contact`, `area_memory_contact`, `contact_future_watch`
    und `contact_memory_depth` dürfen früher als eigene Kontaktlage
    sprechen, wenn Gegenwart nicht klar dominiert.
  - nächster Schritt:
    Neuer Lauf prüft, ob `present_contact_touch` weniger dominant wird
    und ob Zukunft/Erinnerung/unverorteter Druck organischer sichtbar
    werden.
  - Lauf 29 ausgewertet:
    PnL ca. `+31.4319`, Profit Factor ca. `1.2750`, Drawdown ca.
    `8.4780`; Low-Schaden sinkt auf ca. `-41.9181`.
  - Befund:
    Balancing greift sehr stark. `future_contact_watch` dominiert mit ca.
    `8268`, `present_contact_touch` ist praktisch nicht mehr dominant.
    DIO berührt weniger blind die Gegenwart und beobachtet stärker
    Zukunftsraum.
  - Grenze:
    Die Verschiebung könnte jetzt etwas zu stark in Zukunftsbeobachtung
    liegen. Gegenwartskontakt muss wieder organisch entstehen dürfen,
    wenn Nähe, Tragfähigkeit und Reality-Check zusammenpassen.
  - nächster Schritt:
    Übergang `future_contact_watch -> present_contact_touch` weich
    modellieren, ohne in mechanische Entry-Regeln zu fallen.
  - umgesetzt:
    Reifungsbrücke gebaut mit `area_future_to_present_readiness`,
    `contact_future_to_present_readiness`, `maturing_present_area` und
    `maturing_present_contact`.
  - nächster Schritt:
    Neuer Lauf prüft, ob Zukunftskontakte organisch in reife
    Gegenwartskontakte übergehen, ohne die alte
    `present_contact_touch`-Überdominanz zurückzuholen.
  - Lauf 30 ausgewertet:
    PnL ca. `+30.6240`, Profit Factor ca. `1.2501`, Drawdown ca.
    `13.2283`. High und Mid tragen stark, Low verschlechtert sich auf ca.
    `-50.4262`.
  - Befund:
    Reifungsbrücke greift auf Bereichsebene:
    `maturing_present_area` ca. `3796`. Im aktiven Kontaktorgan erscheint
    aber noch kein `maturing_present_contact`; `future_contact_watch`
    bleibt dominant mit ca. `7757`.
  - nächster Schritt:
    Kopplung von `maturing_present_area` in
    `contact_future_to_present_readiness` stärken, damit das
    Kontaktorgan die strategische Reifung übernehmen kann, ohne wieder in
    Gegenwarts-Überdominanz zu kippen.
  - umgesetzt:
    `area_future_to_present_readiness` und `maturing_present_area` wirken
    nun direkt in `contact_future_to_present_readiness`; die finale
    Umschaltung nutzt später die vollständigere Kontaktqualität
    (`contact_reality_check`, `contact_carrying_quality`,
    `outer_inner_coherence`, `contact_action_maturity`).
  - nächster Schritt:
    Neuer Lauf prüft, ob `maturing_present_contact` sichtbar wird.
  - Lauf 31 ausgewertet:
    PnL ca. `+29.4938`, Profit Factor ca. `1.2459`, Drawdown ca.
    `8.8692`; High und Mid tragen, Low bleibt stark negativ mit ca.
    `-50.4702`.
  - Befund:
    Reifungsleitung funktioniert. `maturing_present_contact` erscheint ca.
    `3664` mal, während `future_contact_watch` ca. `4453` bleibt. Damit
    entsteht die gewuenschte Zwischenlage zwischen Zukunftsbeobachtung und
    Gegenwartskontakt.
  - nächster Schritt:
    Low-Kontakte qualitativ tiefer auswerten: Welche Low-Kontakte werden
    trotz Reifung zu schmerzhaften Handlungen? Daraus weiche
    Kontaktqualitäts-Reorganisation ableiten.
  - umgesetzt:
    Positions-Erleben als neurochemische MCM-Feldschicht ergänzt.
    `position_inconsistency_stress`, `position_mcm_field_strain`,
    `position_self_trust_gap`, `position_cortisol_load`,
    `position_noradrenaline_arousal`, `position_protective_distance`,
    `position_held_risk_discomfort`, `position_process_quality` und
    `position_experience_label` werden nun in Positionsdebug,
    Outcome-Kontext und In-Trade-Memory-Zusammenfassung mitgeführt.
  - nächster Schritt:
    Neuer Lauf prüft, ob Low-/Mid-Verluste mit hoher
    `position_inconsistency_stress`, hoher `position_cortisol_load` oder
    niedriger `position_process_quality` zusammenfallen. Ziel bleibt
    Selbstschutz und Reifung, keine harte Sperre.
  - Lauf 32 ausgewertet:
    PnL ca. `+30.0961`, Profit Factor ca. `1.2582`, Drawdown ca.
    `11.4720`; High trägt sehr stark, Mid fällt zurück, Low bleibt
    negativ, ist aber weniger schmerzhaft als Lauf 31.
  - Befund:
    Die Positions-Erlebensschicht ist lesbar. Low-Verluste zeigen im
    Mittel hohe `position_noradrenaline_arousal` ca. `0.5915`, hohen
    `position_held_risk_discomfort` ca. `0.7321`, niedrige
    `position_process_quality` ca. `0.3696` und meist
    `protective_stress_contact`.
  - nächster Schritt:
    `position_experience_label` und Positionsstress in das
    konsequenzbasierte Feedback zurückführen. Ziel:
    Formfamilien sollen belastende offene Konsequenzen als Vorsicht,
    Schmerzspur, Reorganisation oder reiferen Umgang lernen, ohne dass
    daraus eine harte Low-/Mid-Sperre entsteht.
  - umgesetzt:
    Positions-Erleben wirkt nun weich in die Formsymbol-Entwicklung:
    `position_consequence_burden`, `position_constructive_bearing` und
    `position_feedback_label` werden beim Outcome gebildet und in
    `outcome_records.jsonl` sichtbar.
  - nächster Schritt:
    Neuer Lauf prüft, ob belastete Low-/Mid-Kontakte nicht blockiert,
    sondern häufiger als `protective_reorganization_contact`,
    `careful_contact` oder gereifter Beobachtungskontakt gelernt werden.

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

- [ ] Variablen-Audit auf doppelte Funktionsdeutung fortsetzen.
  Status:
  - `MCM_VARIABLEN_MECHANIK.md` geprüft: `331` Variablenüberschriften,
    keine exakt doppelten Namen.
  - fehlende `Funktion:`-Zeilen für `sensory_reality_label`,
    `trust_transfer_mode` und `target_expectation_context` ergänzt.
  - Konvention gegen doppelte Funktionsdeutung ergänzt.
  Prüfgruppen:
  - Last/Druck/Stress
  - Distanz/Reflexion
  - Tragfähigkeit/Qualität
  - Kontaktlernen
  - Reorganisation/Reframing
  Nächster Schritt:
  - Variablen-Hierarchie bauen:
    Basisreiz -> Kontakt -> Position -> Outcome-Sample -> Memory ->
    Neurochemie/Diagnose.
  - Danach entscheiden, ob einzelne Achsen Alias bleiben, klarer getrennt
    oder zusammengelegt werden.
  - Überlappungs-Audit ergänzt:
    Überlappung ist organisch erlaubt, wenn andere Rezeptoren, Ebenen oder
    Zeitlagen beteiligt sind.
  - Prüfpflichtige Rezeptorkaskaden:
    Last-Kaskade, Reorganisation-Kaskade, Distanz-Kaskade,
    Tragfähigkeits-Kaskade.
  - nächster Schritt:
    Rezeptor-Matrix anlegen:
    `Signal -> Rezeptorfamilie -> Zielregler -> Wirkung -> Speicher?`.
    Damit wird sichtbar, ob Signale denselben Zielregler doppelt belasten.
  - umgesetzt:
    `MCM_REZEPTOR_MATRIX.md` angelegt und in `MD_ANWEISUNG.md` als eigener
    Dokumentationsort für Wirkpfade/Rezeptoren eingetragen.
  - nächster Schritt:
    Matrix aus dem Code weiter konkretisieren:
    `Signal -> Rezeptorfamilie -> Zielregler -> Wirkung -> Speicherstatus`.
    Besonders prüfen:
    Last-Kaskade, Distanz-Kaskade, Reorganisations-Kaskade und
    Tragfähigkeits-Kaskade.
  - Lauf 33 Befund:
    Das neue Positionsfeedback ist sichtbar. TP wird überwiegend als
    `carried_position_contact` gelesen, SL überwiegend als
    `protective_stress_contact`. Gleichzeitig steigt
    `protective_reorganization_contact` stark an.
  - nächster Schritt:
    Rezeptor-Matrix gegen Code prüfen:
    Wir müssen sicherstellen, dass `position_consequence_burden` als
    verdichtete Outcome-Last wirkt und nicht zusammen mit seinen Vorachsen
    dieselbe Schmerz-/Carefulness-Spur mehrfach verstärkt.
  - umgesetzt:
    Weiche Rezeptor-Sättigung ergänzt:
    `position_consequence_residual_for_care` und
    `position_consequence_residual_for_memory` verhindern, dass dieselbe
    Positionslast ungefiltert mehrfach auf Schmerz, Vorsicht und Memory
    wirkt.
  - nächster Schritt:
    Neuer Lauf prüft die Verteilung von `protective_reorganization_contact`,
    `careful_contact`, `burdened_contact` und `constructive_contact`.
  - Lauf 34 Befund:
    Rezeptor-Sättigung wirkt: `contact_carefulness_sample` sinkt deutlich,
    während `contact_pain_sample` stabil bleibt. Low-Schaden wird kleiner,
    aber Mid verliert Tragfähigkeit.
  - nächster Schritt:
    Mid-Kontakt-Reifung prüfen/umsetzen:
    Nicht Sättigung zurücknehmen, sondern besser unterscheiden, ob ein
    mittlerer Kontakt über `position_constructive_bearing`,
    `contact_temporal_bearing`, `area_bearing_quality` und
    `contact_reality_check` wirklich reift oder nur offen/neutral bleibt.
  - umgesetzt:
    `transitional_contact_band` und `transitional_contact_maturation`
    ergänzt. Die Achsen wirken nur im Outcome-Lernen und stärken
    Kontaktreife/Utility leicht, wenn ein uneindeutiger Kontakt zeitlich,
    raeumlich und prozessual tragfähig wird.
  - nächster Schritt:
    Neuer Lauf prüft Mid-PnL, `transitional_contact_maturation`,
    `contact_maturity_sample`, `contact_utility_sample` und die
    Kontaktlernzustands-Verteilung.
  - umgesetzt:
    Unterbewusste Nachhall-Tiefenwahrnehmung ergänzt:
    `subconscious_afterimage_depth`, `subconscious_afterimage_pressure`,
    `subconscious_afterimage_bearing`, `subconscious_afterimage_clarity`,
    `subconscious_afterimage_release` und
    `subconscious_afterimage_reflection_pull`.
    Die Achsen bilden keinen harten Schalter, sondern eine weiche
    Kompression alter Feldwirkung. Unklarer tiefer Nachhall zieht DIO eher
    in Beobachtung/Reflexion und reduziert Handlung nur leicht.
  - nächster Schritt:
    Neuer Lauf prüft, ob Nachhall als eigener Tiefenzustand sichtbar wird:
    Druck hoch, Klarheit/Release niedrig -> mehr reflektiver Abstand;
    Tragfähigkeit/Klarheit hoch -> Nachhall kann als Erfahrung getragen
    werden.
  - Lauf 34 Befund:
    Der Lauf enthält die neuen `subconscious_afterimage_*`-Spalten noch
    nicht und kann die neue Tiefen-Nachhall-Schicht daher nicht direkt
    prüfen. Ergebnis: ca. `+18.2779` Netto-PnL, `342` Trades,
    `131/211` TP/SL. High bleibt stark, Low ist weniger schadhaft, Mid
    bleibt der Hauptverlustbereich.
  - nächster Schritt:
    Neuen Lauf mit aktueller Mechanik starten. Danach speziell prüfen:
    Fallen Mid-Verluste mit hohem `subconscious_afterimage_pressure`,
    niedriger `subconscious_afterimage_clarity` und niedriger
    `subconscious_afterimage_release` zusammen?
  - Lauf 35 Befund:
    Neue Nachhall-Spalten sind aktiv. Ergebnis ca. `+18.2048` Netto-PnL,
    `345` Trades, `135/210` TP/SL, Drawdown ca. `8.8596`.
    Nachhall ist stabil messbar, wirkt im Feld bei `act_watch` etwas
    stärker reflektiv, unterscheidet aber in abgeschlossenen Outcomes TP
    und SL noch kaum. Strategische Fensterwahrnehmung ist aktiv
    (`bearing_area_hypothesis` dominiert), aber alle Entries bleiben
    `impulse_contact` mit `strategic_entry_weight = 0.0`.
  - nächster Schritt:
    Weiche motorische Alternative für strategische Bereichswahrnehmung
    bauen: `area_order_intention` und `area_bearing_quality` dürfen eine
    `area_contact_intention` nahelegen, ohne Impuls-Trades hart zu ersetzen
    oder Bereichshandel zu erzwingen.
  - umgesetzt:
    `area_motor_intention` und `area_motor_distance_fit` ergänzt.
    `entry_mode` kann nun `area_contact_intention` annehmen.
    `strategic_entry_weight` wird weicher aus `strategic_entry_fit` und
    `area_motor_intention` gebildet. Das bleibt eine Fähigkeit, keine
    Pflicht.
  - nächster Schritt:
    Neuer Lauf prüft:
    Wie oft entstehen `impulse_contact`, `area_contact_intention` und
    `area_contact_entry`? Tragen Bereichsentries besser im Mid-Bereich oder
    erzeugen sie zusätzliche Unsicherheit?
  - Runtimefix:
    `area_spacetime_fit is not defined` in `derive_trade_plan_from_brain`
    behoben. Der Wert wird jetzt vor `area_motor_intention` aus dem
    gewählten Bereich gelesen.
  - Prüfung:
    `py_compile` und eine direkte Funktionssimulation laufen sauber.
    Simulation erzeugte `area_contact_intention` mit positivem
    `strategic_entry_weight`.
  - umgesetzt:
    Feste RR-Konfiguration bereinigt:
    `RR`, `MAX_RR` und `MCM_EXCITED_RR_FACTOR` aus `config.py` entfernt.
    Alte `Config.RR`-Fallbacks wurden durch dynamische RR-Ableitungen
    ersetzt. `MIN_RR` bleibt als technische Sicherheitsuntergrenze,
    `RR_EXECUTION_MIN` bleibt als Live-Ausfuehrungsschutz.
  - nächster Schritt:
    Neuer Lauf prüft `rr_value`-Streuung nach `entry_mode`:
    `impulse_contact` gegen `area_contact_intention`, besonders im
    Mid-Bereich.
  - Lauf 36 Befund:
    RR-Bereinigung wirkt stark: Netto-PnL ca. `+37.2357`, `369` Trades,
    `155/214` TP/SL, Drawdown ca. `5.7776`. RR streut organisch
    (`p10` ca. `1.895`, Median ca. `4.439`, `p90` ca. `5.134`).
    Alle Entries bleiben jedoch `impulse_contact`; `strategic_entry_weight`
    und `area_motor_intention` bleiben im echten Lauf `0.0`.
  - nächster Schritt:
    Schnittstelle zwischen strategischem Fenster und Trade-Plan prüfen.
    Der Trade-Plan braucht den vollständigen `strategic_window_state`
    inklusive Kandidaten/Fokus, damit `area_contact_intention` real aus dem
    Sehen in die Motorik gelangt.
  - umgesetzt:
    `derive_trade_plan_from_brain(...)` nimmt `strategic_window_state` und
    `form_symbol_state` jetzt direkt entgegen. Runtime übergibt den frisch
    berechneten Zustand an virtuellen Beobachtungsplan und echten Trade-Plan.
  - Prüfung:
    `py_compile` sauber. Direkte Funktionssimulation ohne Bot-State erzeugt
    `area_contact_intention` mit positivem `strategic_entry_weight`.
  - nächster Schritt:
    Neuer Lauf prüft, ob die Bereichsmotorik jetzt im echten Debug
    tatsächlich erscheint.
  - Lauf 37 Befund:
    Direkte Übergabe reicht noch nicht. Ergebnis ca. `+22.3768` Netto-PnL,
    `356` Trades, `144/212` TP/SL, Drawdown ca. `10.1675`.
    Alle Entries bleiben `impulse_contact`; `area_contact_intention`,
    `strategic_entry_weight` und `area_motor_intention` entstehen im echten
    Lauf weiterhin nicht.
  - nächster Schritt:
    Entry-Wahlwahrnehmung bauen:
    DIO soll die zwei Möglichkeiten innerlich als Alternative erkennen:
    Impuls-Entry gegen Bereichs-Entry. Dazu Diagnose-/Regelkreiswerte wie
    `impulse_entry_intention`, `area_entry_intention`,
    `entry_choice_conflict`, `entry_choice_bearing` und
    `entry_choice_state` ergänzen.
  - umgesetzt:
    Entry-Wahlwahrnehmung im Trade-Plan, Runtime-Result, kompakten
    Tradeplan-Export und `MCM_VARIABLEN_MECHANIK.md` ergänzt.
    Die Schicht ist weich: sie beschreibt eine innere Wahlspannung zwischen
    Impuls und Bereich, ohne eine mechanische Pflichtentscheidung zu setzen.
  - nächster Schritt:
    Neuer Lauf prüft die Verteilung von `entry_choice_state`,
    `impulse_entry_intention`, `area_entry_intention` und ob daraus erstmals
    reale `area_contact_intention` entsteht.
  - Lauf 38 Befund:
    Ergebnis ca. `+43.8965` Netto-PnL, `369` Trades, `160/209` TP/SL.
    Die Bereichswahrnehmung ist im strategischen Fenster sichtbar, aber der
    echte Trade-Plan bleibt `impulse_contact` / `impulse_only`.
    Posthoc mit denselben strategischen Fensterdaten entstehen dagegen viele
    `area_contact_intention`-Fälle. Engpass ist deshalb die Kopplung
    zwischen bewusster Bereichswahrnehmung und Motorik.
  - umgesetzt:
    weiche Entry-Synchronisation im Runtime-Ergebnis ergänzt:
    Wenn ein Plan noch `impulse_only` ist, aber ein strategisches
    Bereichsfenster vorhanden ist, wird der Trade-Plan mit dieser
    Wahrnehmung erneut integriert. Neuer Diagnosewert: `entry_choice_sync`.
  - nächster Schritt:
    Neuer Lauf prüft, ob `entry_choice_sync=strategic_context_integrated`
    und `area_contact_intention` im echten Debug erscheinen.
  - Lauf 39 Befund:
    Ergebnis ca. `+20.2809` Netto-PnL, `331` Trades, `132/199` TP/SL.
    DIO beobachtet/enthält sich mehr (`withheld` und `observed` höher),
    aber `entry_choice_sync` bleibt im Trade-Plan `-` und alle Entries
    bleiben `impulse_contact`.
  - umgesetzt:
    Entry-Synchronisation vom nachträglichen Runtime-Ergebnis in den
    eigentlichen `prices`-/Trade-Plan-Aufbau vorgezogen. Dadurch wird die
    Bereichswahrnehmung vor der Ergebnisbildung integriert.
  - nächster Schritt:
    Neuer Lauf prüft, ob `entry_choice_sync` jetzt Werte wie
    `strategic_context_integrated`, `impulse_context_kept` oder
    `native_choice_state` zeigt und ob Bereichs-Entries entstehen.
  - Lauf 40/41 Befund:
    Lauf 40 ca. `+21.2217` Netto-PnL, `337` Trades, `134/203` TP/SL.
    Lauf 41 ca. `+13.9366` Netto-PnL, `327` Trades, `130/197` TP/SL.
    Beide Läufe zeigen weiter nur `impulse_contact`, `impulse_only` und
    `entry_choice_sync=-`.
  - Diagnose:
    Da der aktuelle Code `entry_choice_sync` direkt im Runtime-Plan setzt,
    deuten diese Läufe darauf hin, dass sie noch mit einem alten geladenen
    Python-Prozess entstanden sind.
  - nächster Schritt:
    Bot/Backtest-Prozess neu starten und Lauf 42 erzeugen. Erst dieser Lauf
    prüft die aktuelle Entry-Synchronisation sauber.
  - Lauf 42 Befund:
    Ergebnis ca. `+35.7606` Netto-PnL, `351` Trades, `148/203` TP/SL.
    Die strategische Bereichswahrnehmung bleibt aktiv, aber im
    Attempt-Kontext bleiben `entry_choice_sync=-`,
    `entry_choice_state=impulse_only` und `area_motor_intention=0.0`.
  - Ursache:
    `bot_gate_funktions.py` hat beim finalen Entry-Return die neuen
    Entry-Wahlfelder nicht weitergereicht. Die Signale wurden damit an der
    Gate-Schnittstelle abgeschnitten.
  - umgesetzt:
    `entry_mode`, `strategic_entry_weight`, `area_motor_intention`,
    `impulse_entry_intention`, `area_entry_intention`,
    `entry_choice_conflict`, `entry_choice_bearing`,
    `entry_choice_state`, `entry_choice_sync` und strategische Bereichspreise
    werden jetzt durch `bot_gate_funktions.py` weitergereicht und in
    `entry_debug.csv` sichtbar gemacht.
  - nächster Schritt:
    Lauf 43 prüft die echte Durchleitung bis `attempt_records`.
  - Lauf 43 Befund:
    Die Durchleitung ist bestätigt. `attempt_records.jsonl` enthält jetzt
    `entry_mode`, `entry_choice_state` und `entry_choice_sync`.
    Verteilung im Attempt-Kontext:
    `impulse_contact=1041`, `area_contact_intention=716`,
    `area_contact_entry=60`.
    In abgeschlossenen Outcomes trägt `area_contact_intention` positiv
    (ca. `+38.0107`), während `area_contact_entry` noch leicht negativ ist
    (ca. `-0.9201`).
  - nächster Schritt:
    Bereichskontakt nicht härter machen, sondern die Reife der direkten
    `area_contact_entry`-Fälle neurochemisch lesen: Warum wird aus
    tragender Bereichswahrnehmung manchmal zu früher oder zu naher Kontakt?
  - umgesetzt:
    Weiche direkte Kontaktreife ergänzt:
    `area_direct_readiness` beschreibt, ob ein Bereich nicht nur gesehen,
    sondern auch direkt motorisch berührbar wirkt.
    `area_motor_restraint` beschreibt die natürliche Zurückhaltung bei
    Konflikt, unreifem Kontakt, Nachhall oder fehlender Reife.
    Konflikt darf weiter sichtbar bleiben, zieht aber weniger stark in einen
    direkten `area_contact_entry`.
  - Prüfung:
    `py_compile` für `MCM_Brain_Modell.py`, `bot.py`,
    `bot_gate_funktions.py` und `trade_stats.py` sauber.
  - nächster Lauf:
    Lauf 44 prüft, ob direkte Bereichsentries seltener, reifer oder
    tragfähiger werden und ob `area_direct_readiness` /
    `area_motor_restraint` im Debug sauber erscheinen.

- [x] Emergente Strukturdeutung im Outcome sichtbar machen.
  Ziel:
  - hohe RR-Trades nicht nur als Zahl lesen
  - unterscheiden zwischen weitem Zielraum und tragender Strukturdeutung
  - keine harte Regel, nur Diagnose-/Auswertungsschicht
  Umgesetzt:
  - `outcome_records.jsonl` enthält künftig:
    `rr_value`, `structural_run_room`,
    `emergent_structure_reading`,
    `emergent_structure_confirmation`,
    `emergent_structure_state`,
    `target_expectation_value`
  - `MCM_VARIABLEN_MECHANIK.md` dokumentiert die neuen Felder.
  Prüfung:
  - `py_compile` für `trade_stats.py` sauber.
  Nächster Lauf:
  - Lauf 44 nach hohen RR-Trades auswerten:
    `confirmed_structural_interpretation`,
    `open_structural_hypothesis`,
    `wide_target_without_structure`.

- [x] Einfache DIO-GUI proportional kompakter setzen.
  Ziel:
  - gleiche Inhalte behalten
  - keine weiteren Datenfelder entfernen
  - Fenster und Diagrammflächen um 20 % kleiner anordnen
  Umgesetzt:
  - Hauptfenster, Markt, Stats, Candle, Backtest und Equity proportional
    verkleinert.
  - Mindestgröße ebenfalls proportional auf `960x560` gesetzt.
  - Matplotlib-Figuren passend mit skaliert.
  Prüfung:
  - `py_compile` für `_gui.py` sauber.

- [x] Lauf 44 und emergente Strukturdeutung prüfen.
  Ergebnis:
  - Lauf 44: `+30.1462` Netto-PnL, `327` Trades, Profit Factor ca. `1.31`.
  - High-Strukturen tragen deutlich, Low-Strukturen bleiben belastend.
  - Robust gelesen:
    `confirmed_structural_interpretation` = `38` Fälle, alle TP, ca.
    `+38.99` PnL.
  - `open_structural_hypothesis` = `144` Fälle, überwiegend SL, ca.
    `-33.91` PnL. Diese Schicht ist noch unreif und darf nicht mit
    bestätigter Struktur verwechselt werden.
  Umsetzung:
  - `trade_stats.py` schreibt die emergente Strukturdeutung künftig direkt in
    `outcome_records.jsonl`.
  - `trade_stats.json` erhält `kpi_summary.emergent_structure`.
  Prüfung:
  - `py_compile` für `trade_stats.py` sauber.

- [x] Lauf 45 und Wiederholung der Strukturtrennung prüfen.
  Ergebnis:
  - Lauf 45: `+27.8990` Netto-PnL, `339` Trades, Profit Factor ca. `1.26`.
  - `confirmed_structural_interpretation`: `49` Fälle, `49` TP, `0` SL,
    ca. `+54.16` PnL.
  - `open_structural_hypothesis`: `154` Fälle, `20` TP, `134` SL,
    ca. `-39.09` PnL.
  - Damit bestätigt sich: hohe RR-Struktur ist nur tragend, wenn sie auch
    bestätigt und prozessqualitativ getragen ist.
  Umsetzung:
  - Cancel-Outcomes bekommen künftig ebenfalls direkte
    `emergent_structure_*`-Felder.
  Prüfung:
  - `py_compile` für `trade_stats.py` sauber.
  Nächster Mechanikpunkt:
  - Offene Strukturhypothesen nicht blockieren, sondern als unreif erkennen
    und eher in Beobachtung, Replay oder Reifung halten.

- [ ] Emergente Gedächtnisspur als innere Denkschicht vorbereiten.
  Ziel:
  - offene Strukturhypothesen nicht löschen und nicht hart sperren
  - Gedankenkeime aus der akuten Motorik lösen und als innere Spur speichern
  - eigene DIO-Syntax für Gedanken zulassen
  - Wiederkehr, Variation, Verdichtung und Reifung messbar machen
  - Realitätsbindung sichern, damit keine freie Halluzinationsschicht entsteht
  Mögliche Felder:
  - `emergent_memory_trace`
  - `thought_seed_id`
  - `thought_seed_label`
  - `thought_trace_strength`
  - `thought_recall_potential`
  - `thought_maturity`
  - `reality_binding_score`
  - `hallucination_drift_risk`
  - `form_symbol_anchor`
  - `mcm_field_anchor`
  - `experience_memory_anchor`
  - `outcome_anchor`
  Wichtig:
  - keine Handlungssperre
  - keine freie Fantasieschicht
  - Nicht-Handlung als Erfahrung behandeln
  - MCM als Selbstspür- und Reflexionsanker verwenden
  Metaregulatorische Bindung:
  - Gedankenkeime nicht direkt motorisch entladen
  - Gedankenkeime nicht hart blockieren
  - `seed_focus`, `seed_replay`, `seed_mature`, `seed_store`,
    `seed_release`, `seed_action_ready`, `seed_drift_watch`,
    `seed_overthinking_watch` als mögliche Zustände prüfen
  - Realitätsbindung über Form, MCM-Feld, Erfahrung und spätere Konsequenz
    sichern
  - Grübelkaskaden und Überregulation diagnostisch sichtbar machen

- [ ] Spätere Web-GUI nur als Beobachtungsraum vorbereiten.
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
- [x] Outcome-Export für neue Formfamilienwerte ergänzt.
- [x] Lauf 7/8 als Doppellauf ausgewertet.
- [x] Lauf 9 nach Outcome-Export-Erweiterung ausgewertet.
- [x] `neurochemical_state` als Runtime-/Debug-/Outcome-Schicht umgesetzt.
- [x] `GUI_KONSTRUKTION.md` als Konzept für spätere Web-Oberflaeche angelegt.
- [x] Lauf 10 als erster neurochemischer Lauf grob ausgewertet.
- [x] `mcm_neuro_transition_protocol.csv` als automatisches
  `-2/+2` Analyseprotokoll gebaut.
- [x] `sensory_load`-Runtimefehler in `build_perception_state` behoben.
- [x] Erfahrungspaket-Feedback für positive neurochemische Stimulation
  umgesetzt.
- [x] Erfahrungspaket-Labels und `engaged_effort` umgesetzt.
- [x] Pre-Action-Reorganisation umgesetzt.
- [x] Strukturgenaue Pre-Action-Reorganisation umgesetzt.
- [x] Strategische Fensterwahrnehmung diagnostisch umgesetzt.
- [x] `UMSETZUNGSPLAN.md` strukturell bereinigt.
- [x] Debug Lauf 1 mit strategischer Fensterwahrnehmung ausgewertet.
- [x] MCM-Abhandlungen D bis G.1 als Theoriebrücke in README,
  UMSETZUNGSPLAN, WICHTIG_MECHANIKEN und MCM_VARIABLEN_MECHANIK
  zusammengefasst.
- [x] Weitere MCM-Theorieanker aus dem MCM-Repository in README,
  UMSETZUNGSPLAN, WICHTIG_MECHANIKEN und MCM_VARIABLEN_MECHANIK
  dokumentiert.
