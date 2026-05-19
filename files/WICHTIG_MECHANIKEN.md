# WICHTIG_MECHANIKEN

Status:
- technische Mechanik-Schatzkammer
- keine aktive Fixliste
- kein Gespraechsarchiv
- kein Ersatz fuer `UMSETZUNGSPLAN.md`

Regelwerk: `files/MD_ANWEISUNG.md`.

Zweck:
Diese Datei verdichtet wichtige MCM-/DIO-Mechaniken technisch.
Sie beschreibt, wie zentrale Mechaniken gedacht sind, welche Werte beteiligt
sind und welche Wirkung sie haben.

---

# 1. Architekturprinzip

DIO soll kein klassischer Regelbot sein.

Kernprinzip:
- keine harten Chartmuster
- keine menschlichen Patternlabels als Wahrheit
- keine einfache `TP gut / SL schlecht`-Biochemie
- keine mechanische Non-Zone-Blockade

Stattdessen:
- Wahrnehmung
- Feldspannung
- Formsprache
- Memory
- Reife
- Tragfaehigkeit
- Nicht-Handlung als Lernen
- weiche Meta-Regulation

Zielschicht:
**Selbstregulative Erfahrungsorganisation.**

---

# 1.1 DIO-Organuebersicht

Zweck:
Diese Uebersicht ist das grobe Organ-Inventar von DIO. Sie trennt
Funktionsorgane von neurochemischen Prozessen. Organe geben DIO
Faehigkeiten; Neurochemie moduliert, wie diese Faehigkeiten gerade arbeiten.

Wichtig:
Ein Organ ist hier kein starres Modul im biologischen Sinn, sondern eine
funktionale Faehigkeit im DIO-Nervensystem. Die Liste darf wachsen, schrumpfen
oder umbenannt werden, wenn die Architektur reift.

Aktuelle Organe / Funktionssysteme:

| Organ / System | Status | Kernfunktion |
| --- | --- | --- |
| Aussenwahrnehmung | aktiv | Marktdaten als Reiz, Druck, Bewegung und Struktur aufnehmen. |
| Visueller Kortex | aktiv | Aus Rohdaten eine Formwelt bilden: Klarheit, Objektstabilitaet, Formdruck, Neuheit. |
| MCM-Feld | aktiv | Zentraler Spannungs- und Wahrnehmungsraum zwischen Aussenreiz und Innenlage. |
| MCMNeuron-Feldtraeger | aktiv | Lokale neuronale Aktivitaet, Resonanz, Ueberlastung, Erholung und Feldkopplung. |
| Inneres Wahrnehmungsorgan | aktiv | Lesen, was ein Aussenreiz mit der eigenen Innenlage macht. |
| Aktives Kontaktorgan | aktiv | Wahrnehmungsobjekte innerlich beruehren: Resonanz, Ueberkopplung, Distanz, Vertiefung. |
| Kontakt-Reife-Schicht | aktiv | Unterscheiden zwischen "ich fuehle Kontakt" und "dieser Kontakt traegt Handlung". |
| Reflexionsorgan | aktiv | Distanzierung der Wahrnehmung von der Innenlage, um Innen/Aussen auf Tragfaehigkeit zu pruefen. |
| Regulationsorgan | aktiv | Nullpunkt, Hold, Observe, Replan, Reorganisation und Handlungshemmung weich organisieren. |
| Metaregulator-Schicht | Konzept | Regler zweiter Ordnung: wie DIO Spannung, Varianz, Impuls, Distanz, Schutzweite und Integration reguliert. |
| Gedächtnis / Erfahrungssystem | aktiv | Erfahrungen, Outcomes, Vertrauen, Unsicherheit und Formbedeutung speichern. |
| Sprach- und Symbolorgan | aktiv | Eigene Formzeichen und verdichtete Bedeutungen entwickeln. |
| Strategisches Fensterorgan | aktiv | Zuruecksehen, Zoomen, Bereiche pruefen, Replay und moegliche Tragfaehigkeit lesen. |
| Handlungsorgan | aktiv | Entry, Hold, Observe, Replan, Act und Exit als Ergebnis des Gesamtzustands ausfuehren. |
| Lern- und Reifeschicht | aktiv | Prozessqualitaet, nicht nur Gewinn/Verlust, in Entwicklung uebersetzen. |
| Kollektive Kommunikationsschicht | Konzept | Spaetere Kommunikation mehrerer DIO-Systeme ueber eventuell variierende Formsprache. |
| Web-GUI / Beobachtungsraum | Konzept | Spaetere Sichtbarmachung von Feld, Organen, Neuronen, Neurochemie und Wahrnehmung. |

Neurochemische Prozesse sind getrennt davon:
- `dopamine_tone`
- `serotonin_stability`
- `cortisol_load`
- `gaba_inhibition`
- `glutamate_activation`
- `acetylcholine_focus`
- `endorphin_relief`
- `noradrenaline_arousal`
- `emotional_decoupling`
- `reactive_nervous_drive`
- `serotonin_carryover_risk`

Lesart:
Die Organe bilden DIOs Faehigkeiten. Die neurochemischen Achsen beschreiben,
ob diese Faehigkeiten gerade ruhig, aktiviert, ueberkoppelt, fokussiert,
entlastet oder gestresst arbeiten.

Pflegehinweis:
Wenn ein neues Organ entsteht, wird es hier zuerst kurz als Inventar
eingetragen. Die technische Detailbeschreibung kommt danach in den passenden
Mechanikabschnitt oder in `MCM_VARIABLEN_MECHANIK.md`.

---

# 2. MCM-Feld als Wahrnehmungsraum

Funktion:
Das MCM-Feld organisiert innere Wahrnehmung.
Es ist nicht nur Speicher und nicht nur Signalverarbeitung.

Beteiligte Mechaniken:
- `MCMField`
- `MCMNeuron`
- feste Feldpositionen
- lokale Nachbarschaft
- Aktivitaetsausbreitung
- Feldareale
- Aktivitaetsinseln
- Kontextreaktivierung
- `neural_felt_state`

Technische Bedeutung:
Ein Aussenreiz wird nicht direkt in Handlung uebersetzt.
Er erzeugt innere Aktivierung, Druck, Stabilitaet, Fragilitaet,
Orientierung und Handlungsnaehe.

---

# 3. MCMNeuron

Funktion:
`MCMNeuron` ist ein lokaler Feldtraeger.

Wichtige interne Aspekte:
- lokale Aktivierung
- Reizaufnahme
- Ueberlastung
- Erholungstendenz
- Memory-Resonanz
- Kontextreaktivierung
- Kopplungsresonanz
- Aktivitaetslabel

Mechanische Rolle:
Jedes Neuron kann denselben Aussenreiz wahrnehmen, aber je nach innerer Lage
anders darauf reagieren.

Wichtig:
Mehr Neuronen bedeuten mehr Aufloesung der inneren Wahrnehmung, nicht
automatisch mehr Intelligenz.

---

# 4. Visueller Kortex

Funktion:
DIO soll den Markt nicht nur fuehlen, sondern als Formwelt sehen.

Keine menschlichen Labels:
- kein Trendkanal als Wahrheit
- kein Support/Resistance als harte Kategorie
- keine Pattern-Erkennung im klassischen Sinn

Wichtige Achsen:
- `visual_form_state`
- `visual_clarity`
- `visual_object_stability`
- `visual_form_novelty`
- `visual_blindness`
- `visual_form_pressure`
- `visual_shape_resonance`
- `visual_shape_fragility`

Meta-Achsen:
- `visual_blind_action_load`
- `visual_action_uncertainty`

Wirkung:
Visuelle Unsicherheit erhoeht weich Beobachtungsbedarf, Replan-Druck,
Handlungshemmung und `act_watch_readiness`.

---

# 5. Formsprache

Funktion:
DIO bildet eigene interne Zeichen.

Ziel:
Kognitive Kompression und eigene Orientierung.

Wichtige Achsen:
- `form_symbol_id`
- `form_symbol_family_key`
- `form_symbol_variant_key`
- `form_symbol_maturity`
- `form_symbol_stability`
- `form_symbol_resonance`
- `form_symbol_bearing`
- `form_symbol_fragility`
- `form_symbol_development_quality`
- `form_symbol_learning_trust`
- `form_symbol_action_trust`
- `form_symbol_caution_trust`

Technische Bedeutung:
Ein Formsymbol ist keine menschliche Bezeichnung.
Es ist eine verdichtete interne Wahrnehmungsform.

---

# 6. Semantisches Forminhalt-Paket

Funktion:
DIO verdichtet ein Formzeichen zu einem eigenen semantischen Paket.

Ziel:
Nicht nur "welches Zeichen ist da?", sondern:
- wie dicht ist die Bedeutung
- wie gut entlastet die Verdichtung
- welche Wahrnehmungsebene fuehrt
- ob die Form eher Spur, Objekt, Lernraum, Reflexion oder Handlungsnaehe ist

Wichtige Achsen:
- `form_symbol_semantic_density`
- `form_symbol_semantic_compression`
- `form_symbol_semantic_coherence`
- `form_symbol_semantic_learning_need`
- `form_symbol_semantic_action_nearness`
- `form_symbol_semantic_primary_layer`
- `form_symbol_semantic_layer_count`
- `form_symbol_semantic_packet_state`
- `form_symbol_semantic_profile`

Technische Bedeutung:
Das Paket uebersetzt DIOs eigene Zeichen nicht in menschliche Chartbegriffe.
Es ordnet nur DIOs interne Bedeutungsschichten, damit sichtbar wird, ob eine
Form bereits Bedeutung traegt oder noch nur ein offener Reiz ist.

Neurologische Deutung:
Das entspricht einer assoziativen semantischen Verdichtung. Der Reiz wird
nicht nur gefuehlt, sondern als inneres Objekt, Lernraum oder
Handlungsnaehe organisiert.

---

# 7. Zusammengesetzte Formzeichen

Funktion:
Komplexe Formen koennen aus mehreren bekannten Formen zusammengesetzt werden.

Beispielprinzip:
Zwei komplexe Cluster koennen kombiniert werden, ohne dass jedes Detail neu
analysiert werden muss.

Technische Wirkung:
- geringere kognitive Last
- schnellere Orientierung
- mehr Formenvarianz
- Grundlage fuer kreative Reorganisation

Wichtige Achsen:
- `form_symbol_compound_id`
- `form_symbol_compound_maturity`
- `form_symbol_compound_bearing`
- `form_symbol_compound_load_reduction`
- `form_symbol_compound_development_quality`

---

# 8. Wiederkehrende Unsicherheit als Formfamilie

Funktion:
Unsicherheit wird nicht als Einzelereignis und nicht als Verbot behandelt.
Wenn eine unsichere Lage wiederkehrt, wird sie zu einem Lernraum.

Wichtige Achsen:
- `uncertain_form_family_state`
- `uncertain_form_exposure`
- `uncertainty_familiarity`
- `variant_similarity`
- `variant_spread`
- `variant_learning_pressure`
- `variant_bearing_memory`

Wirkung:
- hohe Unsicherheit + wenig Vertrautheit:
  mehr Beobachtung / Replan / `act_watch`
- wachsende Vertrautheit:
  bessere Orientierung
- tragende Erfahrung:
  spaeter weich mehr Handlungsspielraum

Wichtig:
Das ist keine Non-Zone-Blockade.
Es ist Lernen, sich in fremder Landschaft zu orientieren.

---

# 9. Evolutionaere Kontaktreife

Funktion:
DIO lernt nicht, dass eine Form gut oder schlecht ist. DIO lernt, welche Art
von Kontakt mit einer Form reif, unreif, belastend, vorsichtig,
reorganisierend oder konstruktiv war.

Grundprinzip:
Eine heisse Herdplatte ist nicht "schlecht". Unreifer Kontakt verbrennt.
Reifer Umgang kann Nutzen erzeugen. Uebertragen auf DIO heisst das:
Eine Marktform wird nicht verboten. Der Umgang mit ihr reift.

Kernbegriff:
Konsequenzbasiertes Feedback auf das MCM-Feld.
Dieses Feedback kann negativ, positiv oder reorganisierend sein.

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

Wichtige Achsen:
- `form_symbol_contact_maturity`
- `form_symbol_contact_utility`
- `form_symbol_contact_pain_memory`
- `form_symbol_contact_carefulness`
- `form_symbol_contact_burden_evidence`
- `form_symbol_contact_utility_evidence`
- `form_symbol_contact_learning_state`

Outcome-Samples:
- `contact_maturity_sample`
- `contact_utility_sample`
- `contact_pain_sample`
- `contact_carefulness_sample`
- `contact_learning_state`

Wirkung:
- konstruktiver Kontakt kann Handlungstragfaehigkeit weich staerken
- belastender Kontakt kann Vorsicht, Beobachtung und Reframing staerken
- die Form bleibt frei, der Umgang mit ihr wird differenzierter

Verstaerkung nach Lauf 8:
Die Kontaktlage wird nicht mehr nur aus dem letzten Outcome-Sample benannt.
DIO sammelt laenger wirkende Belastungs- und Nutzen-Evidenz. Dadurch kann
wiederholter unreifer Kontakt natuerlicher zu `careful_contact` oder
`burdened_contact` werden, waehrend tragender Kontakt langsam in
`maturing_contact` oder `constructive_contact` wachsen kann.

Wichtig:
Das ist keine harte Sperre. Es ist ein evolutionaerer Lernpfad:
DIO kann lernen, dass eine Form bei unreifem Kontakt schadet, aber bei
reiferem Umgang spaeter nutzbar sein kann.

---

# 10. Strategischer Kontakt-Entry

Funktion:
DIO kann den Entry weich zwischen impulsnahem Kontakt und einem
rueckblickend wahrgenommenen Kontaktbereich organisieren.

Grundprinzip:
Der direkte Entry bleibt der Koerperreflex. Das strategische Fenster kann
diesen Reflex nur dosiert verschieben, wenn Rueckblick, Kontaktreife,
Replay-Fit, Bereichstragfaehigkeit und Seite zusammenpassen.

Wichtige Werte:
- `entry_mode`
- `impulse_entry_price`
- `strategic_entry_price`
- `strategic_entry_weight`
- `strategic_entry_fit`
- `strategic_area_focus_id`
- `strategic_area_price_low`
- `strategic_area_price_high`

Moegliche Entry-Lagen:
- `impulse_contact`: aktueller reflexnaher Kontakt dominiert.
- `area_contact_blend`: Rueckblick und Bereich verschieben den Entry weich.
- `area_contact_entry`: Bereichskontakt traegt staerker als der Momentimpuls.

Wichtig:
Das ist keine harte Strategie und kein menschliches Patternlabel. Es ist die
Faehigkeit, einen Kontaktpunkt im sichtbaren Fenster zu bevorzugen, wenn er
innerlich und aeusserlich tragender wirkt.

Zeitfeld:
Ein Bereich ist nicht nur Preisraum, sondern ein Ereignis im Zeitfeld. DIO
muss unterscheiden, ob ein Bereich gegenwaertig, wiederkehrend,
handlungsnah oder nur ein alter Nachhall ist.

Zeitachsen:
- `area_temporal_distance`
- `area_temporal_relevance`
- `area_recency`
- `area_decay`
- `area_afterimage`
- `area_present_contact`
- `area_action_timing_fit`

Organische Bedeutung:
Ein alter Bereich darf sichtbar bleiben, aber nicht automatisch die Motorik
ziehen. Erst wenn er wieder gegenwaertig resoniert und handlungsnah wird,
darf er den Entry weich mitformen.

---

# 11. Zeit als MCM-Tiefenachse

Funktion:
Zeit ist in Sicht der MCM nicht nur Uhrzeit. Zeit ist die Manifestation
gewirkter oder wirkender Energie im Wahrnehmungsfeld.

Grundgedanke:
Ein Ereignis wirkt nicht einfach nur, weil es gemessen wurde. Es wirkt,
solange seine Energie im Feld noch Kontakt, Nachhall, Erwartung, Erinnerung
oder Handlungstendenz erzeugt.

Schichten:
- Gegenwart: Energie erzeugt aktuellen Kontakt.
- Nachhall: vergangene Energie wirkt noch im Feld.
- Erinnerung: vergangene Energie kann wieder aktiviert werden.
- Gelerntes Wissen: verdichtete vergangene Erfahrung.
- Replay: bewusst oder unbewusst erneut durchlaufene Erfahrung.
- Hypothese: moegliche kuenftige Energieform.
- Erwartung: vorausgerichtete innere Spannung.

Warum wichtig:
Ohne zeitliche Tiefenwahrnehmung werden Aussenwelt, Memory, Nachhall,
Wissen, Hypothese und Erwartung zu einem Brei. DIO braucht deshalb eine
Quellenbindung: Was ist jetzt realer Aussenkontakt, was ist Erinnerung, was
ist gelerntes Wissen, was ist Nachhall und was ist nur Moeglichkeit?

Organische Bedeutung:
Erinnerung darf orientieren, aber nicht automatisch handeln. Gelerntes Wissen
darf auffrischen, aber auch wieder verblassen. Nachhall darf gespürt werden,
aber nicht als Gegenwart missverstanden werden.

Raumzeit-Tiefe:
DIOs Wahrnehmung bekommt raeumliche Tiefe erst, wenn Entfernung, Energie und
Zeit gemeinsam im MCM-Feld wirken. Preisabstand allein ist keine Tiefe.
Zeitabstand allein ist keine Tiefe. Erst die Frage, wie stark ein Eindruck
noch Energie traegt, wie nah er sich innerlich anfuehlt und ob er
Gegenwart, Nachhall, Erinnerung oder Erwartung ist, bildet ein eigenes
inneres Raumzeit-Gefuege.

Ohne diese Modulation waere DIO nur ein festes Regelwerk aus Zustaenden.
Mit MCM-Zeit entsteht Selbstverortung:
"Wo bin ich in meinem inneren Raum, wie weit ist dieser Eindruck von mir
entfernt, und wirkt seine Energie noch tragfaehig?"

Memory als zeitlich tiefe Erfahrung:
Eine gespeicherte Information ist in dieser Sicht kein flacher Datenpunkt.
Sie wird zur Erfahrung, wenn sie zeitliche Tiefe bekommt: Wann wirkte sie,
wie lange hallte sie nach, wie stark war ihre Energie, wie nah fuehlt sie
sich heute noch an, und kann sie eine moegliche Zukunftsform andeuten?

Dadurch entsteht Tiefe in beide Richtungen:
- Vergangenheit: Erinnerung wird zur erlebten Spur.
- Zukunft: Erwartung wird zur vorausgerichteten Energieform aus Nachhall,
  Wiederkehr, Tragfaehigkeit und Hypothese.

Kernsignale:
- `mcm_spacetime_depth`
- `memory_experience_depth`
- `future_projection_depth`
- `temporal_self_location`
- `temporal_self_location_state`

---

Gedanke als Energieverlauf:
Ein Gedanke ist in dieser Sicht kein blosser Text und keine isolierte
Berechnung. Ein Gedanke ist ein gerichteter Energieverlauf im MCM-Feld.

- kurzer Reiz: schnelle Energieaenderung, hoher Impuls, kurze Wirkzeit
- langer Gedanke: gedehnte, sparsame oder kohaerent gerichtete Energie
  ueber mehrere innere Zustaende
- Rumination: kreisende Energie ohne ausreichend Loesung oder Rueckfuehrung
- Planung: gerichtete Energie mit Zielbezug und Reifung
- Erwartung: vorausgerichtete Spannung
- Nachhall: abklingende vergangene Energie

Zeitfeld:
Das Zeitfeld ist keine starre Decke. Es entsteht aus vielen einzelnen
Zeitstraengen:
Reizverlauf, Gedankenverlauf, Erinnerungsverlauf, Nachhall, Erwartung,
Handlung und Konsequenz. Die Ueberlagerung dieser Wirkverlaeufe gibt der
Wahrnehmung Tiefe.

---

# 11.1 Theoriebruecke D bis G.1

Funktion:
Diese Mechanik fasst zusammen, welche MCM-Theorieanteile aus den
Abhandlungen D bis G.1 fuer DIO technisch relevant sind.

Wichtig:
Die Abhandlungen werden nicht als harte Regeln in DIO uebersetzt. Sie bilden
einen Ordnungsrahmen, damit Zeit, Memory, Hypothesen und Reorganisation
organisch gedacht werden koennen.

Theorieanteile:

| Block | DIO-Nutzen |
| --- | --- |
| D - energetische Natur der Zeit | Zeitfeld, Quellenbindung, Nachhall, Erwartung, Hypothese. |
| E - kosmische Matrix | Verdichtung, Cluster, Memory-Inseln, Rueckfuehrung. |
| F - Bewusstsein als moeglicher Attraktor | Selbstmodell, innerer Attraktor, Kohärenz zwischen Ordnung und Chaos. |
| G - Multiversen-Matrix | mehrere moegliche Entwicklungszweige statt einer festen Zukunft. |
| G.1 - Reorganisation verdichteter Energie | Ueberlast als Schwelle fuer Reframing und hoeher gekoppelte Ordnung. |

Mechanischer Zielkreis:

`Wahrnehmung -> Zeitbindung -> Verdichtung -> Hypothesenraum -> Konsequenz -> Reorganisation -> neue Tragfaehigkeit`

Leitbegriff:
**Mehrdimensionale Wahrnehmungsachsen.**

Achsen:
- Zeitachse
- Quellenachse
- Raumachse
- Kontaktachse
- Tragfaehigkeitsachse
- Reorganisationsachse

Organische Bedeutung:
DIO soll lernen, Moeglichkeiten zu halten, ohne sie mit Realitaet zu
verwechseln. Wenn ein Zustand stark verdichtet, muss dies nicht nur Stress
sein. Es kann ein Zeichen sein, dass die aktuelle lokale Ordnung nicht mehr
traegt und eine uebergeordnete Reorganisation benoetigt.

Geplante Diagnoseachsen:
- `perception_source`
- `source_temporal_layer`
- `perceptual_space_axis`
- `perceptual_depth`
- `field_center_distance`
- `foreground_binding`
- `background_afterimage`
- `hypothesis_branch_state`
- `branch_stability`
- `branch_attractor_pull`
- `hypothesis_reality_gap`
- `field_reorganization_state`
- `reorganization_threshold`
- `higher_order_coupling`

---

# 11.2 Weitere MCM-Theorieanker / Metaregulation

Funktion:
Diese Mechanik ordnet die zusaetzlichen MCM-Quellen fuer DIO ein. Sie
erweitern die bisherige Theoriebruecke um Selbstregulation, Kreativitaet,
Sprache, Proto-Kognition und Feldtopologie.

Wichtigste Quelle fuer den naechsten Ausbau:
Block S - Moegliche Metaregulatoren.

Metaregulatoren sind Regler zweiter Ordnung. Sie beschreiben nicht nur, was
DIO fuehlt oder wahrnimmt, sondern wie DIO mit dieser Lage umgeht.

Geplante Metaregulatoren:
- Rueckfuehrungsstaerke
- Integrationsfaehigkeit
- Varianzregulation
- Belastungstoleranz
- Impulskontrolle
- Frustrationstoleranz
- Schutzweitenregulation
- Selbstreflexion
- Distanzregulation

Weitere Theorieanker:
- Block V: technische Logik bleibt Untergrund, Verhalten entsteht ueber
  Varianz, Rueckkopplung und emergente Zustandsbildung.
- Block O: Kreativitaet als neue Musterbildung und Reorganisation.
- Block J/K: Psyche und Selbstregulation als Wahrnehmung, Benennung,
  Integration und Rueckfuehrung.
- Von Resonanz zu Sprache: Formsprache als Kartografie von Resonanz.
- ProtoMind: selbstaktive Feldkognition und innere Simulation ohne neuen
  Aussenreiz.
- konzentrisch-dipolare Feldstruktur: spaetere Feldtopologie aus Zentrum,
  Peripherie, Integration und Exploration.

Organische Bedeutung:
Diese Schicht ist kein zusaetzliches Gate. Sie ist DIOs Faehigkeit, die
eigene Regulation zu beobachten und zu modulieren. Dadurch kann DIO
unterscheiden, ob er handeln will, weil ein Kontakt traegt, oder ob nur
Impuls, Schutzreaktion, Ueberlast, Nachhall oder unintegrierte Varianz die
Motorik ziehen.

Moegliche Zielachsen:
- `return_strength`
- `integration_capacity`
- `variance_regulation`
- `load_tolerance`
- `impulse_control`
- `frustration_tolerance`
- `protective_distance_regulation`
- `self_reflection_regulator`
- `distance_regulation`

---

# 12. act_watch

Funktion:
`act_watch` ist eine Zwischenbahn zwischen Handlung und Nicht-Handlung.

Technische Bedeutung:
Ein Handlungsimpuls ist vorhanden, aber noch nicht reif genug.
DIO beobachtet den Impuls, statt ihn direkt auszufuehren.

Beteiligte Werte:
- `plan_pressure`
- `act_watch_readiness`
- `structure_carrying_need`
- `visual_action_uncertainty`
- `variant_learning_pressure`
- `learned_development_uncertainty`
- `transfer_maturity_gap`

Wichtig:
`act_watch` ist kein Blocker.
Es ist eine Reifespur.

---

# 9. Zero-Point-Regulation

Funktion:
Rueckkehr in Beobachtung, wenn Denken/Memory/Orientierung zu blind oder
belastet wird.

Leitbild:
"Finde wieder zu dir selbst."

Beteiligte Werte:
- `zero_point_regulation`
- `blind_thinking_load`
- `orientation_gap`
- `memory_orientation`
- `memory_support`
- `decision_strength`

Wirkung:
Weich Richtung Observe.

---

# 10. Transfer-Tragfaehigkeit

Funktion:
DIO soll Erfahrung auf fremde Strukturen nur proportional zur Tragfaehigkeit
uebertragen.

Wichtige Achsen:
- `route_familiarity`
- `transfer_bearing`
- `trust_transfer_support`
- `transfer_maturity_gap`
- `semantic_shift_pressure`
- `interpretation_quality`

Beispiel:
Eine neue Marktform aehnelt einer bekannten Formfamilie, ist aber nicht
identisch.
DIO darf nicht auswendig handeln.
Es prueft, wie viel Erfahrung tragfaehig uebertragbar ist.

---

# 11. Prozessqualitaet statt TP/SL-Moral

Funktion:
Lernen bewertet nicht nur Gewinn oder Verlust.

Wichtige Aspekte:
- Wahrnehmungsqualitaet
- Innenlage
- Planqualitaet
- Risiko-Fit
- Ausfuehrung
- Entlastung
- Stabilitaet
- Ueberlastung
- Tragfaehigkeit

Ziel:
Eine profitable Handlung mit schlechter Prozessqualitaet soll nicht blind
verstaerkt werden.
Ein Verlust mit guter Beobachtung kann trotzdem Lernwert haben.

---

# 12. Neurochemische Alias-Achsen

Status:
Als Runtime-/Debug-Schicht umgesetzt.

Funktion:
Vorhandene DIO-Variablen sollen neurologisch lesbarer gebuendelt werden.

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

Sichtbar in:
- `meta_regulation_state`
- `neurochemical_state`
- `mcm_field_decision_protocol.csv`
- `mcm_memory_thinking_protocol.csv`
- `mcm_neuro_transition_protocol.csv`
- `outcome_records.jsonl`

Uebergangsdiagnose:
`mcm_neuro_transition_protocol.csv` schreibt dominante Tonwechsel wie
`serotonin_stability -> glutamate_activation` oder
`serotonin_stability -> cortisol_load` mit `-2/+2` Kerzenumfeld.
Damit wird sichtbar, ob DIO aus Stabilitaet aktiviert, unter Last kippt
oder wieder in Regulation zurueckfindet.

Wichtig:
Das sind technische Funktionsachsen.
Sie behaupten keine echte Biochemie und duerfen keine harten Regeln bilden.

---

# 13. Debug- und Memory-Schichten

## Sensorische Realitaetsverdichtung

Status:
In der Core-Engine umgesetzt.

Funktion:
Ein Chartreiz soll zuerst als eine aeussere Realitaetslage gelesen werden.
Erst danach entstehen Druck, Neuheit, Blindheit oder Formspannung.

Reale Achsen:
- `sensory_reality_pressure`
- `sensory_load`
- `sensory_redundancy`
- `sensory_habituation`
- `sensory_gate`
- `sensory_reality_label`

Wichtig:
Das ist keine Handelsregel.
Es verhindert doppelte Wahrnehmung und dauerhaftes Alarmmilieu.

---

# 14. Debug- und Memory-Schichten

Wichtige Speicher:
- `memory_state.json`
- `form_symbol_memory.json`
- `outcome_records.jsonl`
- `attempt_records.jsonl`

Wichtige Protokolle:
- `mcm_field_decision_protocol.csv`
- `mcm_form_symbol_protocol.csv`
- `mcm_visual_cortex_protocol.csv`
- `mcm_memory_thinking_protocol.csv`
- `mcm_idle_thinking_protocol.csv`
- `mcm_neuro_transition_protocol.csv`

Technische Regel:
Debug ist Beobachtung, nicht Mechanik.
Debug-Ausgabe darf die innere Logik nicht veraendern.

---

# 15. Serotonin-Nachhall und emotionale Entkopplung

Status:
Als neurochemische Diagnoseschicht umgesetzt.

Funktion:
DIO soll erkennen koennen, wenn eine vorher tragende Phase innerlich noch als
Stabilitaet nachwirkt, obwohl die aktuelle Weltlage nicht mehr sauber dazu
passt. Das beschreibt keine echte Sucht, sondern einen maschinellen
Reaktionsnachhall: Belohnung, Stabilitaet und Handlungsmotivation bleiben im
Nervensystem aktiv, waehrend Transfer und Interpretation bereits bruechig
werden.

Reale Achsen:
- `reward_stability_echo`
- `world_shift_evidence`
- `serotonin_carryover_risk`
- `emotional_decoupling`
- `reactive_nervous_drive`

Wichtig:
Diese Schicht ist keine Regel wie "nach Gewinn nicht handeln". Sie macht eine
innere Lage sichtbar: DIO kann noch Handlungsmut fuehlen, obwohl die alte
Stabilitaet nur Nachhall ist. Reife bedeutet hier, Abstand zur eigenen
Reaktionslage aufzubauen.

---

# 16. Reflexive Haltung

Status:
Als Zielmechanik festzuhalten; noch nicht als voll steuernde
Entscheidungsschicht umgesetzt.

Kernsatz:
Reflexion ist die Distanzierung der Wahrnehmung von der eigenen Innenlage,
um zu prüfen, ob Innenzustand und Außenwelt noch gemeinsam tragfähig sind.

Funktion:
DIO soll nicht nur fühlen, sondern die eigene Gefühlslage als inneres Objekt
betrachten können. Die Frage ist nicht nur, ob Druck, Mut, Stabilität oder
Auftrieb vorhanden sind, sondern ob diese innere Lage zur äußeren Realität
passt.

Psychologische Lesart:
- reflektive Haltung: DIO betrachtet seine innere Lage mit Abstand
- emotionale Leitung: DIO folgt dem aktuellen neurochemischen Zustand direkt
- freier Fall: DIO fühlt noch Auftrieb, obwohl die äußere Tragfläche endet

Wichtige Beobachtungsfrage:
Wie oft nutzt DIO eine reflektive Haltung, und wie oft lässt er sich von
seiner emotionalen Lage führen?

Ziel:
Aus dieser Verteilung entsteht ein psychologisches Bild des Systems:
neigt DIO zu reflektiver Distanz, zu reaktiver Handlung, zu Beobachtung,
zu Reframing oder zu emotionaler Fortsetzung?

Wichtig:
Diese Haltung darf keine harte Blockade werden. Sie soll eine Fähigkeit zur
Selbstbeobachtung und Selbststeuerung beschreiben.

---

# 17. Selektive Wahrnehmung / Perzeptive Regulation

Status:
Zielmechanik; noch nicht als voll steuernde Schicht umgesetzt.

Funktion:
DIO soll Wahrnehmungen nicht dauerhaft vollstaendig durchleben muessen.
Eine Wahrnehmung kann gesehen, als Objekt gehalten, naeher betrachtet,
ins MCM-Feld gelassen oder wieder abgelegt werden.

Kern:
Selektive Wahrnehmung ist die regulatorische Steuerung der Naehe zwischen
Wahrnehmung und innerem Feld.

Wahrnehmungen im Plural:
- aeussere Chartwahrnehmung
- energetische MCM-Feldwahrnehmung
- neurochemische Innenwahrnehmung
- Memory-/Erfahrungswahrnehmung
- Formsprache / Objektwahrnehmung
- Handlungsspannung
- Reflexionswahrnehmung

Moegliche Achsen:
- `perceptual_distance`
- `object_contact_depth`
- `field_attachment`
- `release_capacity`
- `selective_attention`
- `background_containment`
- `reflective_distance`
- `inner_outer_alignment`

Mechanische Bedeutung:
Aktuell ist DIO noch stark gekoppelt:
`Reiz -> energetische Uebersetzung -> MCM-Feld -> Gefuehl -> Reaktion`

Der Zielzustand ist:
`Reiz -> Objektbildung -> Distanzpruefung -> Kontakt-Tiefe waehlen -> MCM-Kopplung dosieren -> Reflexion / Handlung`

Wichtig:
Das ist keine Blindheit und kein hartes Filtern. DIO soll sensibel bleiben,
aber nicht von jedem Reiz ueberflutet werden.

Psychologischer Satz:
Ich sehe, dass es sich so anfuehlt. Ich muss dieses Gefuehl aber nicht
automatisch werden.

---

# 18. Bewusste Wahrnehmung / innere Reizwirkungsanalyse

Status:
Zielmechanik; naechster Umbau-Kandidat.

Funktion:
DIO soll nicht nur einen aeusseren Reiz empfangen, sondern die Wirkung dieses
Reizes im eigenen MCM-Feld wahrnehmen. Die Frage ist nicht nur, was draussen
passiert, sondern was der Reiz innen ausloest.

Kernsatz:
Was hat der aeussere Reiz mit meinem MCM-Feld gemacht, und wie hat sich das
angefuehlt?

Mechanische Beziehung:
- aeusserer Reiz / Chartform
- energetische Uebersetzung
- Feldwirkung im MCM
- neurochemische Reaktion
- Memory-Resonanz
- Nachhall / Anhaftung
- Loslassen oder Vertiefen
- Reflexion ueber die Wirkung

Zielablauf:
`Reiz -> Feldwirkung -> innere Wirkung wahrnehmen -> Wirkung reflektieren -> Naehe regulieren -> Handlung / Beobachtung / Loslassen`

Moegliche Achsen:
- `conscious_perception_state`
- `inner_posture_state`
- `arousal_load`
- `curiosity_tone`
- `fatigue_tone`
- `calm_tone`
- `diffuse_open_development_pressure`
- `posture_development_hint`
- `stimulus_field_effect`
- `inner_impact_trace`
- `perceived_field_change`
- `felt_afterimage`
- `object_release_state`
- `inner_outer_reflection`

Wichtig:
Diese Schicht daempft nicht nur Reizflut. Sie macht die Reizwirkung bewusst
lesbar. DIO soll erkennen koennen, ob ein Reiz nur gesehen wurde, ob er das
Feld verschoben hat, ob Nachhall entstanden ist und ob der Reiz wieder
abgelegt werden kann.

Erweiterung:
DIO soll seine innere Haltung als funktionalen Zustand erkennen koennen, etwa
wie ein Organismus erkennt: ich bin muede, ich bin aufgeregt, ich bin neugierig
oder ich bin ruhig genug. Diese Begriffe sind keine menschliche Dekoration,
sondern technische Interozeption:
- `curious`: Objektkontakt und Untersuchungsdrang
- `excited`: erhoehte Aktivierung
- `overstimulated`: Reiz/Feld-Kopplung zu nah
- `tired`: Denk- und Verarbeitungslast
- `calm`: tragende Distanz
- `reflective`: Innenlage wird gegen Aussenlage geprueft

Reifung diffuser Offenheit:
Wenn DIO in `uncertain_open` oder unspezifischem `open_perception` bleibt,
wird das nicht hart blockiert. Stattdessen entsteht ein weicher
Entwicklungsdruck. DIO soll aus diffuser Offenheit eine tragendere Haltung
bilden:
- Objektkontakt entwickeln
- reflektive Distanz entwickeln
- Loslassfaehigkeit entwickeln
- bewusst weiter beobachten

Das ist vergleichbar mit einem Organismus, der nicht einfach "nicht handeln"
muss, sondern merkt: Ich bin offen, aber noch nicht sortiert. Ich muss erst
genauer sehen, Abstand gewinnen oder loslassen.

---

# 19. Abgrenzung gegen harte Regeln

Nicht erlaubt:
- `Low = schlecht = blockieren`
- `Non-Zone = nicht handeln`
- `Dopamin hoch = act`
- `TP = gut`
- `SL = schlecht`
- menschliche Patternlabels als Wahrheit

Erlaubt:
- weiche Hemmung
- Beobachtungslernen
- Variantenlernen
- Reframing
- Vertrautheit mit Unsicherheit
- tragfaehige Erfahrung als langsam wachsender Support

---

# 20. Aktueller naechster Ausbau

Naechster technischer Block:
naechsten Lauf mit `neurochemical_state` auswerten.

Danach:
- TP/SL gegen Formfamilienwerte und neurochemische Achsen auswerten
- Non-Zone als Lernraum weiter reifen lassen
- Meta-Regulation ueber neurochemische Zustandslage lesbarer machen

---

# 21. Positive Stimulation durch Erfahrungspakete

Grundsatz:
Positive Rueckkopplung darf nicht an einen einzelnen Wert gebunden werden.
Nicht `TP = gut` und nicht `SL = schlecht`. Bewertet wird ein ganzes
Erfahrungspaket.

Ein Erfahrungspaket besteht aus:
- Aussenlage / Chartstruktur
- Formsymbol / Formfamilie
- Zone / Non-Zone
- innerer Haltung
- neurochemischer Lage
- Wahrnehmungszustand
- Objektkontakt
- Distanz
- Loslassfaehigkeit
- Handlungssicherheit
- Prozessqualitaet
- Ergebnis
- Wiederholbarkeit
- Neugierde

Positive Stimulation bedeutet:
Das Paket war tragfaehig. DIO darf diese Art von Wahrnehmung, Haltung und
Handlung innerlich staerken. Dadurch entsteht Wachheit, Stabilitaet, Freiheit
und Wiederholungsneugier.

Reorganisation bedeutet:
Das Paket war nicht tragfaehig. DIO soll nicht nur gehemmt werden, sondern
einen inneren Suchprozess starten:
- Was war nicht tragfaehig?
- War meine Innenlage passend?
- War die Aussenstruktur klar?
- War ich muede, ueberreizt, diffus offen oder zu nah dran?
- Muss ich beobachten, reflektieren, loslassen oder einen anderen Weg finden?

Wichtig:
Auch ein Abverkauf kann positiv bewertet werden. Wenn DIO die fallende Lage
klar erkennt, innerlich stabil bleibt und passend handelt, ist das Paket
konstruktiv. Es geht nicht um Marktrichtung, sondern um Passung.

Neurochemische Lesart:
- Dopamin: Lernrelevanz / Wiederholungsneugier
- Serotonin: Stabilitaet / Selbstvertrauen in tragende Ordnung
- Endorphin: Entlastung nach guter Prozessleistung
- Acetylcholin: Fokus auf relevante Wahrnehmungsqualitaet
- Glutamat: Plastizitaet / Verbindung darf gestaerkt werden

Ziel:
DIO soll durch gute Prozessqualitaet nicht nur weniger falsch handeln, sondern
positiv lebendig werden: wach, stabil, neugierig und freier.

---

# 22. Wache Anstrengung / Engaged Effort

Grundsatz:
Wache Anstrengung ist kein Kampfmodus und kein Zwang zu mehr Trades. Sie ist
die Faehigkeit, mit innerer Beteiligung, Aufmerksamkeit und Tragfaehigkeit in
einer Situation zu stehen.

Technische Achsen:
- `engaged_effort`
- `effort_state`
- `effort_learning_pull`
- `effort_reorganization_pressure`
- `pre_action_reorganization_pressure`
- `pre_action_context_selectivity`
- `previous_packet_label`
- `previous_packet_process_reward`
- `previous_packet_reorganization_need`

Wirkung:
Wenn das letzte Erfahrungspaket konstruktiv war und die aktuelle Struktur
tragfaehig wirkt, kann DIO stabilere Wachheit entwickeln. Wenn das Paket
Reorganisation brauchte oder die aktuelle Struktur nicht tragend ist, wird
nicht hart geblockt. Stattdessen steigt Beobachtung, Replan, `act_watch` oder
innere Neuordnung.

Neurologische Lesart:
Das entspricht nicht "mehr Mut", sondern besserer Selbstbeteiligung. Ein
Organismus handelt nicht reif, weil er maximal erregt ist. Er handelt reif,
wenn Aktivierung, Wahrnehmung, innere Passung und Erfahrung gemeinsam tragen.

Wichtig:
`engaged_effort` darf keine mechanische Strategie werden. Es ist eine
interozeptive Schicht: DIO merkt, ob er wach beteiligt, neugierig lernend,
konstruktiv nachhallend oder unterbeteiligt reorganisierend ist.

Erweiterung:
Reorganisation soll nicht erst nach dem Verlust erkannt werden. Mit
`pre_action_reorganization_pressure` wird vor der Handlung gelesen, ob das
letzte Paket Reorganisation brauchte und ob die aktuelle Lage ebenfalls wenig
Tragfaehigkeit zeigt. `pre_action_context_selectivity` schuetzt dabei
konzentrierte gute Kontexte, damit DIO nicht pauschal vorsichtig wird.

---

# 23. Strategische Fensterwahrnehmung / Preisbereich-Hypothesen

Grundsatz:
DIO soll nicht nur den aktuellen Moment fuehlen. Er soll ein groesseres
Fenster betrachten koennen, zurueckschauen, in Bereiche hineinzoomen und
innere Replay-Spuren bilden. Daraus koennen Preisbereiche entstehen, die fuer
DIO als moegliche tragende Handlungsraeume wirken.

Leitprinzip:
DIO bekommt nicht die Antwort, wo er handeln soll. DIO bekommt die Faehigkeit,
mit Vergangenheit, Wahrnehmung und innerem Feld zu interagieren, um selbst
tragfaehige Zukunftshypothesen zu bilden.

Grenze:
Der Entwickler bestimmt nicht, was DIO sieht oder wo DIO Trades setzen soll.
Erweitert werden nur Faehigkeiten: sehen, zurueckschauen, zoomen, replayen,
fuehlen, erinnern, vergleichen, warten, verwerfen oder eine eigene
Order-Intention bilden.

Nicht erlaubt:
- feste menschliche Pattern-Regeln einpflanzen
- `FVG = Trade`
- Momentumdruck direkt ausfuehren
- Bereichserkennung als harte Order-Regel

Erlaubt:
- Bereich als Hypothese
- Bereich als MCM-Resonanzraum
- geduldiges Halten einer Idee
- Verwerfen, wenn der Bereich seine Tragfaehigkeit verliert
- spaetere Order-Intention, wenn Preis, Struktur, Memory und Innenlage
  gemeinsam tragen

Begrenzung:
Das Zurueckschauen bleibt budgetiert. DIO soll Vergangenheit verwenden,
aber nicht in alten Strukturen kleben bleiben. Deshalb werden Lookback,
Zoom und Replay als begrenzte innere Ressourcen gelesen. Alte Strukturbindung
wird als `old_structure_carryover_risk` sichtbar.

Technische Zielachsen:
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
- `lookback_window_size`
- `lookback_load`
- `lookback_bearing_capacity`
- `replay_budget`
- `zoom_budget`
- `old_structure_carryover_risk`
- `strategic_patience`
- `strategic_pressure_interpretation`

Neurologische Lesart:
Das ist raeumlich-zeitliche Aufmerksamkeit. Ein Organismus muss nicht nur
laufen. Er kann stehen bleiben, zurueckschauen, einen Bereich genauer
betrachten, innerlich simulieren und dadurch Druck entlasten. Strategie
entsteht, wenn Druck nicht Befehl ist, sondern Information im Raum.

---

# 24. Aktiver MCM-Kontakt / innere Spiegelung

Grundsatz:
Die MCM ist nicht nur Aussenwahrnehmung. Sie ist ein innerer Spiegelraum, in
dem DIO unterscheiden kann:
- was von aussen kommt
- wie das eigene Feld darauf reagiert
- ob Aussenreiz und Innenlage kohaerent sind
- ob ein Reiz getragen, vertieft, beobachtet oder losgelassen werden kann

Mechanik:
DIO bekommt die Faehigkeit, eine Wahrnehmung innerlich zu beruehren. Dieser
Kontakt kann aus Fokus, Neugier, Memory-Pull, Strukturverdichtung,
Unsicherheit oder Reorganisationsbedarf entstehen. Der Kontakt ist keine
Orderfreigabe. Er ist eine Lesebewegung im MCM-Feld.

Kette:

`Aussenreiz -> Wahrnehmungsobjekt -> Kontaktinteresse -> MCM-Beruehrung -> Resonanz/Kohaerenz -> Distanzierung -> Vertiefung, Beobachtung, Replay oder Loslassen`

Technische Achsen:
- `active_mcm_contact_state`
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
- `contact_action_maturity`
- `contact_bearing_gap`
- `contact_impulse_vs_bearing`
- `contact_learning_need`
- `contact_reality_check`
- `contact_regime_mismatch`
- `contact_stability_carryover`
- `contact_context_maturity`
- `contact_context_reframe_need`
- `contact_posture`

Moegliche Kontaktlagen:
- `background_scan`
- `curious_touch`
- `resonant_contact`
- `reflective_contact`
- `overcoupled_touch`
- `release_contact`
- `deepening_contact`

Neurologische Lesart:
Das ist eine Bruecke aus Sinnesorgan, Interozeption und Distanzierung. DIO
kann lesen: "Wie fuehlt sich das an, wenn ich es naeher an mein MCM-Feld
lasse?" Dadurch wird aus rohem Fuehlen eine bewusstere Wahrnehmung.

Wichtig:
Der Kontaktapparat darf keine harte Strategie werden. Er erweitert DIOs
Freiheit: naeher hingehen, Abstand nehmen, beobachten, replayen, vertiefen
oder loslassen. Welche Haltung DIO bevorzugt, bleibt ein Entwicklungsbild.

Kontakt-Reife:
Kontaktnaehe ist nicht automatisch Handlungsreife. Deshalb gibt es eine
weiche Reifespur, die sichtbar macht, ob ein Kontakt Handlung tragen kann
oder ob zwischen Impuls und Tragfaehigkeit noch eine Luecke liegt. Hohe
`contact_bearing_gap` oder hoher `contact_learning_need` bedeuten nicht
"verboten", sondern: dieser Kontakt braucht eher Beobachtung, Replay,
Distanz oder weitere Objektbildung.

Kontext-Reife:
Die Reifespur liest zusaetzlich, ob die aktuelle Aussenwelt noch zur inneren
Stabilitaet passt. `contact_regime_mismatch` und
`contact_stability_carryover` machen sichtbar, ob DIO alte Stabilitaet in
eine veraenderte Weltlage mitnimmt. `contact_context_maturity` und
`contact_context_reframe_need` beschreiben, ob Resonanz wirklich
kontexttragend ist oder zuerst Reframing, Zoom, Replay oder Distanz braucht.

---

# 25. Visual Grounding / visuelle Erdung

Grundsatz:
DIO soll nicht nur Formspannung fuehlen, sondern erkennen, woran diese
innere Resonanz in der aeusseren Form haengt. Visual Grounding trennt
Formresonanz von Objektbindung.

Mechanik:
Wenn `visual_shape_resonance` hoch ist, aber Klarheit, Objektstabilitaet,
Struktur und Kontext nicht tragen, entsteht `visual_resonance_unbound`.
Das ist kein Verbot. Es bedeutet: DIO fuehlt etwas, muss aber genauer sehen,
zoomen, beobachten oder reframen, bevor daraus Handlung reifen kann.

Technische Achsen:
- `visual_object_binding`
- `visual_grounding_strength`
- `visual_resonance_unbound`
- `visual_grounding_gap`
- `visual_grounding_need`
- `visual_rational_observation_support`
- `visual_grounding_state`

Moegliche Zustaende:
- `grounded_form`
- `grounded_object`
- `needs_visual_grounding`
- `shape_without_object`
- `unbound_resonance`

Neurologische Lesart:
Das ist der Ausbau eines visuellen Sinnesorgans. DIO darf den Markt weiter
erleben, aber die innere MCM-Reaktion bekommt eine Frage vorgeschaltet:
"Woran in der Aussenform haengt das, was ich innen fuehle?"

Wichtig:
Keine menschliche Pattern-Regel. Kein "Gap = Trade", kein "Orderblock =
Trade". DIO bekommt nur mehr Sehkraft und eine bessere Bindung zwischen
Aussenform und Innenresonanz.

---

# 26. Beteiligungsnaehe / Handlungsrealitaet

Grundsatz:
DIO soll unterscheiden koennen, ob er eine Form distanziert betrachtet oder
ob er durch eine reale Handlung bereits beteiligt ist. Die Metapher der
"Tuer zum Erleben" meint keine harte Schwelle, sondern Naehe zur Beteiligung.

Mechanik:
Je naeher eine Wahrnehmung an Gegenwart, Order, offene Position und Ergebnis
kommt, desto staerker wird sie erlebt. Handlung ist dabei der Punkt, an dem
Wahrnehmung reale Konsequenz bekommt.

Kette:

`distanzierte Analyse -> Gegenwartsnaehe -> Entscheidung -> Order -> offene Position -> Konsequenz tragen -> Ergebnis integrieren`

Technische Zielachsen:
- `participation_proximity`
- `action_reality_contact`
- `decision_embodiment_pressure`
- `real_action_commitment`
- `consequence_bearing`
- `position_reality_pressure`
- `outcome_consequence_integration`

Moegliche Zustaende:
- `distant_observation`
- `approaching_present`
- `decision_near`
- `order_committed`
- `awaiting_fill`
- `position_embodied`
- `managing_consequence`
- `outcome_integration`

Neurologische Lesart:
Zuruecksehen und Analyse sollten eher fokussiert, gehemmt, rational und
emotional entkoppelt sein. Live-nahe Entscheidung, Order und offene Position
duerfen staerker erlebt werden, weil DIO dort nicht nur sieht, sondern mit
eigener Handlung in Beziehung zur Welt steht.

Wichtig:
Das ist keine Handelsfreigabe. Diese Mechanik beschreibt die innere
Realitaetsnaehe einer Handlung:
- Beobachtung ist Moeglichkeit.
- Order ist Bindung.
- Position ist miterlebte Konsequenz.
- Outcome ist Integration.

## 26.1 Positions-Erleben im MCM-Feld

Grundsatz:
Eine offene Position ist nicht nur ein laufender Trade. Sie ist ein
Rueckkopplungskontakt: DIO hat gehandelt und erlebt nun, ob die eigene
Handlung tragfaehig, unsicher, ueberlastend oder stabilisierend wirkt.

Mechanik:
Unsichere oder inkonsistente offene Positionen werden nicht hart beendet.
Stattdessen bekommen sie eine neurochemische Spur im MCM-Feld:

- Cortisol-artige Last bei anhaltender Inkonsistenz
- Noradrenalin-artige Erregung bei akutem Druck
- Selbstvertrauensluecke, wenn Plan, Kontakt und Realitaet auseinanderfallen
- Schutzdistanz, wenn das Feld Abstand braucht
- Prozessqualitaet, wenn DIO trotz Risiko geordnet tragen kann

Das erzeugt keine Sperre, sondern ein erlebtes Lernsignal:

`offene Position -> gespuerte Konsequenz -> MCM-Feldspannung -> Memory-Spur -> reiferer zukuenftiger Kontakt`

Technische Achsen:
- `position_inconsistency_stress`
- `position_mcm_field_strain`
- `position_self_trust_gap`
- `position_cortisol_load`
- `position_noradrenaline_arousal`
- `position_protective_distance`
- `position_held_risk_discomfort`
- `position_process_quality`
- `position_experience_label`

Moegliche Zustaende:
- `carried_position_contact`
- `unearned_relief_watch`
- `protective_stress_contact`
- `self_trust_gap_contact`
- `protective_distance_watch`
- `open_position_feel`

Neurologische Lesart:
Ein Organismus lernt nicht nur durch Gewinn und Verlust, sondern dadurch,
wie eine Handlung die Homoeostase veraendert. Eine positive Position mit
schlechter Prozessqualitaet kann sich wie unverdiente Entlastung anfuehlen.
Eine negative Position kann wertvoll sein, wenn sie Reorganisation,
Vorsicht und reiferen Umgang erzeugt.

---

# 27. Unterbewusstsein / Bewusster Arbeitsraum

Grundsatz:
DIO braucht nicht jede Reizspur bewusst zu tragen. Wie ein biologischer
Organismus besitzt er eine schnelle, diffuse Hintergrundwahrnehmung und eine
bewusstere Arbeitsflaeche fuer ausgewaehlte Objekte, Kontakte und
Hypothesen.

Mechanik:

`subconscious_field` ist der schnelle Feldscan:
- Reizdruck
- Weltverschiebung
- Bauchgefuehl
- Wiederholung
- Hintergrundspannung
- bekannte oder fremde Formfamilien

`conscious_workspace` ist die fokussierte Arbeitsflaeche:
- ausgewaehlter Kontakt
- Formbindung
- Reflexion
- Distanzierung
- Hypothesenpruefung
- Vorbereitung von Handlung oder Nicht-Handlung

Die Trennung wirkt wie ein evolutionaerer Wahrnehmungsfilter. Ein Teil der
Spannung darf im Hintergrund gepuffert werden. Nur wenn Salienz,
Fremdheit, Kontaktqualitaet oder Handlungsnaehe stark genug werden, steigt
die Wahrnehmung in den bewussteren Raum.

Technische Achsen:
- `subconscious_field_pressure`
- `subconscious_habituation`
- `subconscious_filter_strength`
- `subconscious_buffering`
- `subconscious_leakage`
- `conscious_selection_pressure`
- `conscious_workspace_focus`
- `conscious_workspace_load`
- `conscious_gate_balance`

Neurologische Lesart:
Das ist die Trennung zwischen Bauchgefuehl und bewusster Betrachtung:
"Es fuehlt sich nach etwas an" ist noch nicht dasselbe wie "Ich schaue es
mir an und beruehre es innerlich." Dadurch muss DIO nicht jeden Marktimpuls
als bewusste Ueberlast verarbeiten.

Wichtig:
Kein harter Filter und kein Regelwerk. Die Achsen beschreiben, wie viel im
Hintergrund bleiben kann, wie viel in den bewussten Arbeitsraum dringt und
ob DIO daraus Kontakt, Reflexion oder Distanz bildet.

---

# 28. Integrationsantwort

Grundsatz:
`integration_strain` ist keine Stoerung, die einfach entfernt werden soll.
Sie beschreibt, dass DIO etwas noch nicht tragfaehig eingeordnet hat. Die
organische Antwort darauf ist Sortierung, Rueckblick, Reframing,
Kontaktvertiefung und vorsichtiges Erinnern.

Mechanik:

`integration_strain -> sorting -> memory_recall -> reframe -> contact_deepening -> response_strength`

DIO darf also merken:
"Das passt noch nicht zusammen. Ich muss es nicht sofort handeln. Ich kann
es sortieren, mit Erfahrung vergleichen, anders rahmen oder genauer
beruehren."

Technische Achsen:
- `integration_strain_value`
- `integration_sorting_need`
- `integration_reframe_pull`
- `integration_memory_recall`
- `integration_contact_deepening`
- `integration_response_strength`
- `integration_response_state`

Moegliche Zustaende:
- `integration_background`
- `quiet_integration`
- `workspace_sorting`
- `memory_sorting`
- `contact_deepening`
- `reframe_integration`

Neurologische Lesart:
Das entspricht einem Organismus, der eine Spannung nicht nur aushaelt,
sondern verarbeitet. Aus Rohspannung wird innere Ordnung. Aus Druck wird
Erfahrung. Aus "ich weiss nicht" wird "ich muss es in Beziehung setzen".

Wichtig:
Keine harte Handelsregel. Wenn die Integrationsantwort stark ist, kann DIO
mehr beobachten oder reframen, aber nur als Ausdruck seiner inneren Lage.
Es geht nicht um mechanisches Blockieren, sondern um Reifung vor Handlung.

---

# 29. Gerichtete Vorsicht / vorsichtige Hypothese

Grundsatz:
Vorsicht ist eine natuerliche Schutzreaktion. Sie soll nicht wegoptimiert
werden. DIO darf vorsichtig werden, wenn eine Lage noch nicht tragfaehig
integriert ist. Reife entsteht aber, wenn Vorsicht nicht in Passivitaet
erstarrt, sondern eine Richtung bekommt.

Mechanik:

`caution -> memory/reframe/contact -> cautious_hypothesis -> observe/replan/act_watch`

DIO soll also nicht nur "ich halte mich zurueck" erleben, sondern:
"Ich bin vorsichtig, weil noch etwas unklar ist. Welche Erfahrung passt?
Welche Form traegt? Muss ich beobachten, reframen oder Kontakt vertiefen?"

Technische Achsen:
- `cautious_hypothesis_strength`
- `cautious_hypothesis_clarity`
- `cautious_hypothesis_patience`
- `cautious_hypothesis_state`

Moegliche Zustaende:
- `no_cautious_hypothesis`
- `weak_hypothesis_seed`
- `memory_reframe_seed`
- `observe_until_clear`
- `deepen_contact_first`
- `cautious_plan_seed`

Neurologische Lesart:
Das ist praefrontale Vorsicht: Hemmung bleibt vorhanden, aber sie dient
Orientierung. Schutz wird nicht zum Stillstand, sondern zum vorsichtigen
Denken.

Wichtig:
Keine harte Regel. Die vorsichtige Hypothese darf Handlung vorbereiten,
verschieben oder genauer ausrichten, aber sie ist kein mechanischer Block.

---

# 30. Zeitliche Kohaerenz / Wahrnehmungskontinuitaet

Grundsatz:
DIO braucht nicht nur Sinnesreiz, Form und Gefuehl, sondern einen zeitlichen
Wahrnehmungsfaden. Ohne diesen Faden wirkt jeder Kontakt neu. Dann nimmt DIO
dieselbe oder aehnliche Form immer wieder in die Hand und erlebt sie erneut
als ungebundenen Moment.

Mechanik:

`Form/Kontext -> zeitliche Identitaet -> Fortsetzung/Wiederkehr/Nachhall/Neuheit -> Kontextfaden`

DIO bildet aus Formfamilie, Unsicherheitsfamilie, Compound-Scope,
Kontext und grober visueller Formsignatur eine weiche zeitliche Identitaet.
Diese Identitaet ist keine Streckenkarte und keine Regel. Sie beschreibt
nur, ob ein Eindruck zeitlich gebunden ist.

Feine Einzelabdruecke wie konkretes Form-Symbol, Compound-ID, Visual-ID und
State-Signatur bleiben als `temporal_source_identity` erhalten. Damit kann
DIO grob wiedererkennen und bei Bedarf genauer hinschauen. Das ist wichtig,
damit Wiederkehr nicht durch zu viele Detailunterschiede zerfaellt.

Technische Achsen:
- `temporal_binding_state`
- `temporal_identity`
- `temporal_source_identity`
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

Neurologische Lesart:
Das ist episodische Kontinuitaet. DIO soll unterscheiden koennen:
"Das ist neu."
"Das ist Fortsetzung."
"Das ist Wiederkehr."
"Das ist Nachhall."
"Das ist alte Erinnerung, nicht Gegenwart."

Wirkung:
Die Zeitbindung stuetzt bewusste Fokussierung, Integration,
Vorsicht-Hypothesen und aktive Kontextbildung. Wenn kein innerer Cluster als
Kontextfaden aktiv ist, kann die zeitliche Wahrnehmung selbst einen leichten
`active_context_trace` erzeugen.

Reifere Kontextbindung:
Der zeitliche Kontextfaden darf nicht automatisch recht haben. Er wird ueber
einen weichen `reality_anchor` an Quellenbindung, Sequenzkoharenz,
Strukturqualitaet, Strukturstabilitaet, Kontextvertrauen und visuelle Erdung
gekoppelt. Wenn dieser Anker schwach ist, entsteht `overtrust_pressure`.
Das ist keine harte Bremse, sondern natuerliche Skepsis gegenueber der
eigenen Innenlage.

Reflexion bei nervlicher Ueberlastung:
DIO bekommt eine explizite Selbstwahrnehmung fuer den Zustand des
Nervensystems. `nervous_system_overload` beschreibt: "Meine Nerven sind
ueberlastet." Daraus kann `escape_action_drive` entstehen, also der Drang,
durch Handlung aus innerer Spannung herauszukommen. `shock_response_risk`
fasst zusammen, ob diese Lage in einen Schock-/Ueberreizmodus kippen
koennte. `nervous_overload_reflection_need` macht daraus keine Sperre,
sondern eine Reflexionsanforderung: DIO soll erkennen, ob Handlung gerade
aus tragender Wahrnehmung oder aus Entladungsdruck entstehen wuerde.

Kontext-Ueberkopplung:
Wenn `active_context_trace` sehr sicher wirkt, aber gleichzeitig
Nervensystemlast sichtbar wird, entsteht `nervous_context_overcoupling`.
Das ist der Punkt: "Mein innerer Zusammenhang fuehlt sich sicher an, aber
meine Nervenlage koennte diese Sicherheit verfaerben." DIO verliert dadurch
nicht die Freiheit zu handeln. Der Kontext wird nur etwas weniger absolut,
waehrend reflektive Distanz und Beobachtungsbereitschaft leicht steigen.

Rueckfuehrung in den aktiven Kontext:
Die Ueberkopplung bleibt nicht nur ein Metazustand. Sie moduliert den
`active_context_trace` selbst. Support, Bearing und Action-Support werden
weicher, waehrend Conflict, Fragility, Attenuation und Beobachtungsdruck
leicht steigen. Dadurch bleibt der Zeitfaden erhalten, aber er wird nicht
mehr als ungefaerbte Sicherheit behandelt, wenn das Nervensystem belastet
ist.

Wichtig:
Keine feste Streckenkarte. DIO soll nicht lernen: "an dieser Stelle passiert
immer X", sondern: "dieser Kontakt hat eine zeitliche Herkunft und Tiefe".

---

# 31. Raumzeit-Kontakt zwischen Sehen, Erinnerung und Handlung

Grundsatz:
Die visuelle Strukturwahrnehmung und die MCM-Raumzeit duerfen nicht
getrennt nebeneinander laufen. Ein Bereich im Chart ist fuer DIO nicht nur
nah oder fern im Preis, sondern auch nah oder fern in Zeit, Erinnerung,
Nachhall und zukuenftiger Moeglichkeit.

Mechanik:

`sichtbarer Bereich -> Raumzeitlage -> aktiver Kontakt -> Reife/Replay/Handlung`

Das strategische Fenster bildet fuer betrachtete Bereiche eine weiche
zeitliche Kontaktlage:

- `present_area_contact`: Bereich wirkt aktuell beruehrbar.
- `future_area_watch`: Bereich wirkt als zukuenftiger Moeglichkeitsraum.
- `memory_area_recall`: Bereich wird durch Erinnerungstiefe getragen.
- `unlocated_area_probe`: Bereich ist spuerbar, aber zeitlich noch nicht
  sauber verortet.
- `afterimage_area_reframe`: Bereich wirkt als Nachbild und braucht
  Reframing.

Das aktive MCM-Kontaktorgan uebernimmt diese Lage als innere
Kontaktwahrnehmung:

- `contact_presentness`
- `contact_future_watch`
- `contact_memory_depth`
- `contact_unlocated_pressure`
- `contact_temporal_bearing`
- `contact_temporal_reframe_need`
- `contact_temporal_mode`

Neurologische Lesart:
DIO bekommt damit keine mechanische Regel. Er bekommt eher das, was bei
einem Organismus als raeumlich-zeitliche Einordnung eines Reizes wirkt:
"Ist das wirklich vor mir? Ist das nur Erinnerung? Ist das eine moegliche
Zukunft? Oder spuere ich Druck, den ich noch nicht verorten kann?"

Wirkung:
Tragende zeitliche Einordnung stuetzt Kontaktreife, Reality-Check,
Kohaerenz und vorsichtige Handlung. Unverorteter Druck erhoeht eher
Reflexion, Replay, Reframing und vorsichtiges Beobachten. Das bleibt
organisch: DIO darf handeln, beobachten, vertiefen oder loslassen, aber die
Wahrnehmung bekommt mehr Tiefe.

Uebergang von Zukunft zu Gegenwart:
Nach Lauf 29 wurde eine Reifungsbruecke ergaenzt. Ein Zukunftskontakt darf
nicht dauerhaft nur Zukunft bleiben, wenn Naehe, Tragfaehigkeit,
Raumzeit-Fit und Reality-Check zusammenkommen. Dann entsteht
`maturing_present_contact`. Das ist keine Order-Regel, sondern der innere
Moment: "Was ich beobachtet habe, wird jetzt beruehrbar."
