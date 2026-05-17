# MCM_VARIABLEN_MECHANIK

Ziel dieser Datei:
- zentrale MCM-/DIO-Groessen benennen
- Funktion und Ebene klaeren
- unterscheiden zwischen Diagnose, weicher Wirkung und persistenter Erfahrung
- verhindern, dass Variablen als harte Chartregeln missverstanden werden

Grundsatz:
Keine Variable ist ein menschliches Patternlabel oder eine mechanische
Handelsregel. Die Werte beschreiben innere Wahrnehmung, Tragfaehigkeit,
Vertrauen, Stress, Reife und Prozessqualitaet.

Allgemeine Anweisung:
Variablen duerfen keine harten Formen erzwingen.
Sie beschreiben Moeglichkeiten, Spannungen, Lasten, Reifegrade und
Erfahrungsraeume.
Ihre Aufgabe ist, DIO Selbstentwicklung zu ermoeglichen,
nicht fertige Wahrheit zu ersetzen.

Zielschicht:
Die Variablen dienen der **selbstregulativen Erfahrungsorganisation**.
DIO soll nicht fertige Urteile ueber gut/schlecht bekommen,
sondern die Faehigkeit entwickeln, Tragfaehigkeit aus Feld, Memory,
Formsprache, Druck, Entlastung, Handlung, Nicht-Handlung und Rueckkopplung
selbst zu organisieren.

---

# Legende

- Bereich: meistens `0.0 - 1.0`, wenn nicht anders angegeben.
- Ebene:
  - Wahrnehmung
  - MCM-Feld
  - Formsprache
  - Trust/Transfer
  - Zielerwartung
  - Position/Exit
  - Memory/Entwicklung
  - Debug/Diagnose
- Wirkung:
  - diagnostisch: wird nur sichtbar gemacht
  - weich: beeinflusst Druck, Beobachten, Replan oder Handlung graduell
  - persistent: fliesst in Speicher/Entwicklung ein

---

# Live / Equity

## Neurochemische Alias-Achsen

Diese Achsen sind als technische Benennungsschicht umgesetzt.
Sie behaupten keine echte Biochemie, sondern machen die vorhandene
DIO-Regulation neurologisch lesbarer.

Sie erscheinen im `neurochemical_state`, im `meta_regulation_state`, in
Feld-/Memory-Protokollen und in `outcome_records.jsonl`.

## Neurochemische Kategorien

Diese Uebersicht ordnet die neurochemischen Variablen nach Funktion. Sie ist
kein biologischer Wahrheitsanspruch, sondern eine technische Landkarte fuer
DIOs innere Modulation.

| Kategorie | Variablen | Funktion |
| --- | --- | --- |
| Aktivierung / Netzwerkenergie | `glutamate_activation`, `reactive_nervous_drive` | Reizweiterleitung, innere Erregung, Handlungsdruck. |
| Wachheit / Alarm | `noradrenaline_arousal`, `world_shift_evidence` | Salienz, Druck, Regimebruch, Aufmerksamkeit auf Veraenderung. |
| Fokus / sensorischer Zoom | `acetylcholine_focus`, `focused_acetylcholine` | genaueres Sehen, Formstabilitaet, merkenswerte Wahrnehmung. |
| Stabilitaet / Tragfaehigkeit | `serotonin_stability`, `stabilizing_serotonin`, `reward_stability_echo` | Ruhe, Geduld, innere Ordnung, Nachhall tragender Phasen. |
| Hemmung / Schutz | `gaba_inhibition` | Reifebremse, Nicht-Handlung, Schutz vor Reflexhandlung. |
| Stress / Belastung | `cortisol_load`, `neurochemical_load` | Denk-, Memory-, Positions- und Regulationslast. |
| Entlastung / Wohlbefinden | `endorphin_relief`, `relief_endorphin`, `constructive_stimulation` | Druckabbau, Prozesswohlbefinden, tragende Beruhigung. |
| Motivation / Lernen | `dopamine_tone`, `constructive_dopamine` | Lernwert, Erwartungsdrift, Wiederholungsneugier bei tragenden Paketen. |
| Distanzierung / Reife | `emotional_decoupling`, `serotonin_carryover_risk` | Abkopplung von alter Innenlage, Erkennen von Nachhall und emotionaler Uebertragung. |
| Gesamtbilanz / Diagnose | `neurochemical_support`, `neurochemical_balance` | Verhaeltnis von innerer Unterstuetzung zu innerer Last. |

Lesart:
- Aktivierung ohne Stabilitaet wirkt reaktiv.
- Stabilitaet ohne Realitaetsabgleich kann Carryover werden.
- Hemmung ohne Fokus kann Starrheit werden.
- Entlastung mit guter Prozessqualitaet kann Reife staerken.
- Distanzierung verbindet Neurochemie mit Reflexion.

## `dopamine_tone`

- Bereich: `0.0 - 1.0`.
- Ebene: Neurochemische Alias-Schicht.
- Funktion: Erwartungsfehler, Lernwert, Prozessqualitaet und tragende
  Verbesserung verdichten.
- Nahe bestehende Variablen:
  `entry_expectation`, `target_expectation`, `expectation_deviation`,
  `form_symbol_development_quality`, `form_symbol_learning_trust`,
  `plan_quality`, `process_quality`.
- Bedeutung: "Hat diese Erfahrung meine Orientierung sinnvoll verbessert?"

## `gaba_inhibition`

- Bereich: `0.0 - 1.0`.
- Ebene: Neurochemische Alias-Schicht / Meta-Regulation.
- Funktion: Hemmung, Reifebremse und Schutz vor Reflexhandlung.
- Nahe bestehende Variablen:
  `action_inhibition`, `act_watch_readiness`, `field_observation_need`,
  `structure_carrying_need`, `visual_action_uncertainty`,
  `variant_learning_pressure`.
- Bedeutung: "Nicht jeder Reiz wird Handlung."

## `noradrenaline_arousal`

- Bereich: `0.0 - 1.0`.
- Ebene: Neurochemische Alias-Schicht.
- Funktion: Wachheit, Druck, Salienz und Stressfokus.
- Nahe bestehende Variablen:
  `felt_pressure`, `field_perception_pressure`, `breakout_tension`,
  `visual_form_pressure`, `approach_pressure`, `survival_pressure`.
- Bedeutung: "Etwas ist wichtig oder angespannt."

## `acetylcholine_focus`

- Bereich: `0.0 - 1.0`.
- Ebene: Neurochemische Alias-Schicht / Wahrnehmung.
- Funktion: sensorischer Zoom, Aufmerksamkeit und genaues Hinschauen.
- Nahe bestehende Variablen:
  `visual_clarity`, `visual_object_stability`, `form_symbol_zoom_need`,
  `form_symbol_detail_pressure`, `focus_confidence`, `target_lock`,
  `signal_quality`.
- Bedeutung: "Ich muss genauer sehen."

## `serotonin_stability`

- Bereich: `0.0 - 1.0`.
- Ebene: Neurochemische Alias-Schicht / Selbstregulation.
- Funktion: Geduld, Stabilitaet, Varianz aushalten und innere Tragfaehigkeit.
- Nahe bestehende Variablen:
  `experience_regulation`, `reflection_maturity`, `load_bearing_capacity`,
  `state_stability`, `recovery_balance`, `zero_point_regulation`.
- Bedeutung: "Ich bleibe in mir stabil."

## `cortisol_load`

- Bereich: `0.0 - 1.0`.
- Ebene: Neurochemische Alias-Schicht / Belastung.
- Funktion: Ueberforderung, Denk-/Memory-/Positionslast und Recovery-Druck.
- Nahe bestehende Variablen:
  `regulatory_load`, `pressure_to_capacity`, `recovery_need`,
  `cognitive_load`, `blind_thinking_load`, `position_cognitive_load`,
  `exit_decision_pressure`.
- Bedeutung: "Diese Lage kostet Kraft."

## `endorphin_relief`

- Bereich: `0.0 - 1.0`.
- Ebene: Neurochemische Alias-Schicht / Entlastung.
- Funktion: Prozesswohlbefinden, Entlastung und tragende Beruhigung.
- Nahe bestehende Variablen:
  `pressure_release`, `stress_relief_potential`, `carrying_balance`,
  `plan_trust`, `intervention_fitness`, positive Prozessqualitaet.
- Bedeutung: "Das fuehlt sich tragend und entlastend an."

## `glutamate_activation`

- Bereich: `0.0 - 1.0`.
- Ebene: Neurochemische Alias-Schicht / Aktivierung.
- Funktion: Erregung, Feldaktivitaet, Aktivierungsinseln und
  Handlungsenergie.
- Nahe bestehende Variablen:
  `field_mean_energy`, `field_activity_island_activation_mean`,
  `decision_strength`, `signal_relevance`, `processing_load`.
- Bedeutung: "Das Netzwerk ist aktiviert."

## `neurochemical_load`

- Bereich: `0.0 - 1.0`.
- Ebene: Neurochemische Alias-Schicht / Diagnose.
- Funktion: Gesamtlast aus Stress, Hemmung, Arousal und Aktivierung.
- Wirkung: diagnostisch.
- Bedeutung: "Wie hoch ist die neurologisch lesbare Gesamtlast?"

## `neurochemical_support`

- Bereich: `0.0 - 1.0`.
- Ebene: Neurochemische Alias-Schicht / Diagnose.
- Funktion: Gesamtunterstuetzung aus Stabilitaet, Entlastung, Fokus,
  Lernwert und Orientierung.
- Wirkung: diagnostisch.
- Bedeutung: "Wie viel innere Unterstuetzung traegt die Lage?"

## `neurochemical_balance`

- Bereich: ungefaehr `-1.0 - 1.0`.
- Ebene: Neurochemische Alias-Schicht / Diagnose.
- Funktion: Differenz zwischen Support und Last.
- Wirkung: diagnostisch.
- Bedeutung: "Traegt die innere Chemie, oder kostet sie mehr als sie gibt?"

## `mcm_neuro_transition_protocol.csv`

- Typ: Debug-/Analyseprotokoll.
- Ebene: Neurochemische Alias-Schicht / Uebergangsanalyse.
- Funktion: schreibt Wechsel des dominanten neurochemischen Tons mit
  Kerzenumfeld `-2/+2`.
- Sichtbare Achsen:
  `from_tone`, `to_tone`, `transition_key`, `volume_ratio`,
  `range_ratio`, `pre_ret`, `post_ret`, `window_ret`,
  neurochemische Deltas, Felddruck-/Feldklarheits-Deltas,
  Handlungshemmung und Handlungsfreigabe.
- Wirkung: diagnostisch.
- Bedeutung: "Was passiert innen und aussen, wenn DIO neurochemisch kippt?"
- Wichtig: Das Protokoll ist keine Entscheidungsregel.
  Es macht Kipp-, Aktivierungs- und Erholungsuebergaenge lesbar.

## Visuelle Kortex-Achsen

Diese Variablen sind in der ersten beobachtenden Version eingebaut.
Sie beschreiben eine neue Sinnesmodalitaet von DIO.

Wichtig:
Sie sind keine menschlichen Pattern-Labels und keine direkten Handelssignale.
  Sie machen sichtbar, ob DIO eine aeussere Form sieht oder nur Druck fuehlt.

## Sensorische Realitaetsverdichtung

Diese Achsen liegen vor den abgeleiteten visuellen Druckwerten.
Sie sollen verhindern, dass ein aeusserer Strukturreiz mehrfach als
getrennter Alarm im System ankommt.

## `sensory_reality_pressure`

- Bereich: `0.0 - 1.0`.
- Ebene: aeussere Wahrnehmung / Core-Engine.
- Funktion: verdichteter Druck der aeusseren Realitaetslage.
- Wirkung: weich auf visuelle Druck-/Neuheitsbildung.
- Bedeutung: "Wie stark ist die eine aeussere Lage wirklich?"

## `sensory_redundancy`

- Bereich: `0.0 - 1.0`.
- Ebene: aeussere Wahrnehmung / Reizentdoppelung.
- Funktion: misst, ob mehrere verwandte Achsen denselben Reiz tragen.
- Wirkung: erhoeht Habituation und senkt doppelte Verstaerkung.
- Bedeutung: "Sehe ich mehrere Dinge, oder dasselbe Ding mehrfach?"

## `sensory_habituation`

- Bereich: `0.0 - 1.0`.
- Ebene: sensorische Regulation.
- Funktion: weiche Gewoehnung an redundante Reizlagen.
- Wirkung: reduziert Neuheit/Alarm ohne Wahrnehmung zu loeschen.
- Bedeutung: "Dieser Reiz ist bekannt genug, um nicht mehrfach zu alarmieren."

## `sensory_gate`

- Bereich: ca. `0.58 - 1.0`.
- Ebene: sensorische Entlastung.
- Funktion: dosiert, wie stark abgeleitete Druckachsen weitergegeben werden.
- Wirkung: weiche Reizverdichtung, keine Handelsregel.
- Bedeutung: "Wie viel des abgeleiteten Drucks soll wirklich durch?"

## `sensory_reality_label`

- Typ: Textlabel.
- Ebene: Diagnose.
- Moegliche Werte:
  `quiet_outer_reality`, `clear_outer_reality`,
  `intense_outer_reality`, `redundant_outer_reality`.
- Wirkung: diagnostisch.
- Bedeutung: benennt die Qualitaet der aeusseren Wahrnehmungslage.

## `visual_form_state`

- Typ: Dictionary/Zustandsobjekt.
- Ebene: aeussere Wahrnehmung, visueller Kortex.
- Funktion: verdichteter Zustand der gesehenen Marktform.
- Wirkung: zuerst diagnostisch, spaeter weich.
- Bedeutung: beschreibt die aeussere Gestalt als DIO-interne Formwelt,
  nicht als menschliches Chartmuster.

## `visual_clarity`

- Bereich: `0.0 - 1.0`.
- Ebene: visueller Kortex.
- Funktion: beschreibt, wie klar die aeussere Form fuer DIO lesbar ist.
- Wirkung: zuerst diagnostisch.
- Bedeutung: hohe Klarheit bedeutet nicht automatisch Handlung,
  sondern nur bessere visuelle Orientierung.

## `visual_object_stability`

- Bereich: `0.0 - 1.0`.
- Ebene: visueller Kortex.
- Funktion: beschreibt, ob die erkannte Form ueber Zeit stabil bleibt.
- Wirkung: zuerst diagnostisch, spaeter weich fuer MCM/act_watch.
- Bedeutung: trennt kurzlebigen Reiz von tragender Form.

## `visual_form_novelty`

- Bereich: `0.0 - 1.0`.
- Ebene: visueller Kortex, Formsprache.
- Funktion: beschreibt, wie fremd oder neu die gesehene Form ist.
- Wirkung: diagnostisch/entwicklungsoffen.
- Bedeutung: Fremdheit soll nicht blockieren, sondern Beobachtung,
  Reframing und neue Formzeichen ermoeglichen.

## `visual_blindness`

- Bereich: `0.0 - 1.0`.
- Ebene: visueller Kortex, Meta-Regulation.
- Funktion: beschreibt, wie stark DIO Druck fuehlt, ohne eine tragende Form
  zu sehen.
- Wirkung: spaeter weich Richtung Observe, act_watch, Reframing oder
  Nullpunkt-Regulation.
- Bedeutung: "Ich fuehle etwas, aber ich sehe noch nicht genug."

## `visual_form_pressure`

- Bereich: `0.0 - 1.0`.
- Ebene: visueller Kortex/MCM.
- Funktion: beschreibt, wie stark die gesehene Form selbst Spannung erzeugt.
- Wirkung: diagnostisch/soft.
- Bedeutung: unterscheidet reine innere Nervositaet von Formspannung der
  Aussenwelt.

## `visual_shape_resonance`

- Bereich: `0.0 - 1.0`.
- Ebene: visueller Kortex, Memory, Formsprache.
- Funktion: beschreibt Resonanz zwischen aktueller Form und vorhandener
  Form-/Erfahrungssprache.
- Wirkung: spaeter weich fuer Orientierung.
- Bedeutung: keine starre Wiedererkennung, sondern Formverwandtschaft.

## `visual_shape_fragility`

- Bereich: `0.0 - 1.0`.
- Ebene: visueller Kortex.
- Funktion: beschreibt, wie bruechig oder instabil die gesehene Form wirkt.
- Wirkung: diagnostisch/soft.
- Bedeutung: hohe Fragilitaet kann spaeter Beobachtung oder act_watch
  staerken, ohne Handlung hart zu verbieten.

## `visual_blind_action_load`

- Bereich: `0.0 - 1.0`.
- Ebene: visueller Kortex / Meta-Regulation.
- Funktion: verdichtet visuelle Blindheit, geringe Formklarheit,
  geringe Objektstabilitaet, Formdruck, Fragilitaet und schwache
  Strukturtragfaehigkeit zu einer visuellen Handlungslast.
- Wirkung: weich.
- Bedeutung: "Ich habe einen Handlungsreiz, aber mein Sehen traegt ihn noch
  nicht sauber."

## `visual_action_uncertainty`

- Bereich: `0.0 - 1.0`.
- Ebene: visueller Kortex / MCM-Feld / Meta-Regulation.
- Funktion: koppelt visuelle Handlungslast mit Strukturunsicherheit,
  Feldklarheit, Feldsupport und Memory-Orientierung.
- Wirkung: weich Richtung Observe, Replan und `act_watch`.
- Bedeutung: keine Orderblockade, sondern eine reifende visuelle Hemmung.
  DIO darf lernen, wann ein Impuls erst angeschaut werden muss, bevor er
  Handlung wird.

## `visual_object_binding`

- Bereich: `0.0 - 1.0`.
- Ebene: visueller Kortex / Objektbindung.
- Funktion: beschreibt, ob Formresonanz an ein stabiles aeusseres Objekt
  gebunden ist.
- Wirkung: diagnostisch/weich.
- Bedeutung: "Woran in der Aussenform haengt das, was ich innen fuehle?"

## `visual_grounding_strength`

- Bereich: `0.0 - 1.0`.
- Ebene: visuelle Erdung.
- Funktion: beschreibt die Staerke der Kopplung zwischen aeusserer Form,
  Struktur, Symbolcontainment und MCM-Reaktion.
- Wirkung: weich stabilisierend.
- Bedeutung: "Meine innere Reaktion hat eine sichtbare Quelle."

## `visual_resonance_unbound`

- Bereich: `0.0 - 1.0`.
- Ebene: Formresonanz / fehlende Objektbindung.
- Funktion: beschreibt Formspannung, die stark gefuehlt wird, aber noch
  nicht sauber an ein visuelles Objekt gebunden ist.
- Wirkung: weich Richtung Beobachtung, Zoom und Reframe.
- Bedeutung: "Ich fuehle Form, sehe aber noch nicht klar genug, was es ist."

## `visual_grounding_gap`

- Bereich: `0.0 - 1.0`.
- Ebene: visuelle Reifespannung.
- Funktion: beschreibt die Luecke zwischen innerer Resonanz und aeusserer
  Objektbindung.
- Wirkung: weich auf Beobachtung, Replan und Handlungsunsicherheit.

## `visual_grounding_need`

- Bereich: `0.0 - 1.0`.
- Ebene: visuelles Lernen / Fokusbedarf.
- Funktion: beschreibt, ob DIO vor Handlung genauer sehen, zoomen oder die
  Form als Objekt klaeren muss.
- Wirkung: weich.

## `visual_rational_observation_support`

- Bereich: `0.0 - 1.0`.
- Ebene: rationale Formanalyse.
- Funktion: beschreibt Support fuer distanzierte Analyse statt unmittelbares
  Miterleben.
- Wirkung: Zielachse fuer Analysemodus.

## `visual_grounding_state`

- Bereich: String.
- Ebene: visueller Kortex.
- Funktion: benennt den aktuellen Zustand visueller Erdung.
- Moegliche Werte:
  `grounded_form`, `grounded_object`, `needs_visual_grounding`,
  `shape_without_object`, `unbound_resonance`.

## `uncertain_form_family_state`

- Typ: Textzustand.
- Ebene: Formsprache / visueller Kortex / Meta-Regulation.
- Funktion: beschreibt, ob eine unsichere Formfamilie ruhig, fremd,
  wiederkehrend, vertraut beobachtend oder tragfaehiger wird.
- Wirkung: weich.
- Bedeutung: "Diese Art von Weltzustand kommt wieder, aber in Varianten."

## `uncertain_form_exposure`

- Bereich: `0.0 - 1.0`.
- Ebene: Formsprache / visueller Kortex.
- Funktion: misst, wie stark eine Formfamilie als unsicher, blind,
  bruechig oder noch wenig tragend erlebt wird.
- Wirkung: weich Richtung Beobachten und Lernen.
- Bedeutung: keine Gefahrmarke, sondern Exposition gegenueber
  wiederkehrender Unsicherheit.

## `uncertainty_familiarity`

- Bereich: `0.0 - 1.0`.
- Ebene: Formsprache / Memory.
- Funktion: beschreibt, ob DIO mit dieser unsicheren Formfamilie vertrauter
  wird.
- Wirkung: weich.
- Bedeutung: Vertrautheit bedeutet nicht automatisch Handlung, sondern
  bessere Orientierung im Unklaren.

## `variant_similarity`

- Bereich: `0.0 - 1.0`.
- Ebene: Formsprache.
- Funktion: beschreibt, wie nahe die aktuelle Variante an der bisherigen
  Formfamilie liegt.
- Wirkung: diagnostisch/soft.
- Bedeutung: "Das ist fremd, aber verwandt."

## `variant_spread`

- Bereich: `0.0 - 1.0`.
- Ebene: Formsprache.
- Funktion: beschreibt die Streuung innerhalb einer Formfamilie.
- Wirkung: weich Richtung Beobachten/Reframing, wenn die Streuung hoch ist.
- Bedeutung: eine Formfamilie kann viele Varianten haben, ohne ein hartes
  Pattern zu sein.

## `variant_learning_pressure`

- Bereich: `0.0 - 1.0`.
- Ebene: Formsprache / Meta-Regulation.
- Funktion: erzeugt Lern- und Beobachtungsdruck, wenn Unsicherheit wiederkehrt
  und noch nicht vertraut oder tragend genug ist.
- Wirkung: weich Richtung Observe, Replan und `act_watch`.
- Bedeutung: "Ich sollte diese Variantenfamilie erst besser kennenlernen."

## `variant_bearing_memory`

- Bereich: `0.0 - 1.0`.
- Ebene: Formsprache / Memory.
- Funktion: beschreibt, ob eine unsichere Variantenfamilie bereits tragende
  Erfahrung besitzt.
- Wirkung: weich unterstuetzend, aber nicht als Freigaberegel.
- Bedeutung: Handlung darf spaeter entstehen, wenn Unsicherheit vertraut und
  tragfaehig geworden ist.

## `DEBUG_OUTPUT_PROFILE`

- Typ: Textprofil.
- Werte:
  - `RESEARCH_DEBUG`
  - `LEAN_BACKTEST`
  - `GUI_DEBUG`
  - `PERFORMANCE_DEBUG`
  - `LIVE_DEBUG`
  - `CUSTOM`
- Ebene: Debug/Diagnose.
- Funktion: waehlt, welche Daten DIO nach aussen schreibt.
- Wirkung: technisch/diagnostisch.
- Bedeutung: Die innere MCM-/Brain-Mechanik bleibt gleich, aber die aeussere
  Beobachtung wird dosiert. Damit kann ein Lauf als tiefer Forschungslauf,
  schlanker Backtest, GUI-Lauf, Performance-Messung oder Live-Diagnose laufen.
  `CUSTOM` bedeutet: alle Einzelschalter werden manuell gefuehrt.

## `DEBUG_WRITE_MODE`

- Typ: Textmodus.
- Werte:
  - `immediate`
  - `buffered`
  - `buffered_safe`
- Ebene: Debug/Diagnose.
- Funktion: steuert, ob Debug-Zeilen sofort oder gepuffert geschrieben werden.
- Wirkung: technisch/diagnostisch.
- Bedeutung:
  `immediate` schreibt direkt.
  `buffered` sammelt im RAM und schreibt beim Beenden.
  `buffered_safe` sammelt ebenfalls, flushes aber periodisch nach Zeit oder
  Zeilenlimit und beim Beenden. Das reduziert Schreiblast, ohne die
  Wahrnehmungs-/Denkmechanik zu veraendern.

## `START_EQUITY`

- Bereich: Kapitalwert, z.B. USDT.
- Ebene: Live/Backtest, Statistik.
- Funktion: Startkapital-Fallback und Backtest-Startwert.
- Wirkung: technisch/diagnostisch.
- Bedeutung: Im Backtest ist dieser Wert die feste Startbasis. Im Live-Modus
  darf er nur Notfall-Fallback sein, wenn die Phemex-Futures-Equity nicht
  gelesen werden kann.

## `LIVE_EQUITY_SYNC_ENABLED`

- Typ: Boolean.
- Ebene: Live/Statistik.
- Funktion: erlaubt im Live-Modus die Synchronisation von `current_equity`
  und `pnl_netto` mit dem Phemex-Futures-Konto.
- Wirkung: technisch/diagnostisch.
- Bedeutung: DIO soll im Live-Modus nicht in einer simulierten 100-USDT-Welt
  leben, sondern seine reale Kontotragfaehigkeit wahrnehmen.

## `current_equity`

- Bereich: Kapitalwert, z.B. USDT.
- Ebene: Statistik, Live-Zustand.
- Funktion: aktueller Kontostand im Backtest oder synchronisierte
  Futures-Equity im Live-Modus.
- Wirkung: diagnostisch.
- Bedeutung: "Wie tragfaehig ist mein reales Kapitalfeld gerade?"

## `pnl_netto`

- Bereich: Kapitaldifferenz.
- Ebene: Statistik, Prozessqualitaet.
- Funktion: Nettoentwicklung. Im Backtest aus lokal berechnetem Trade-PnL,
  im Live-Modus bei aktivierter Synchronisation aus
  `current_equity - start_equity`.
- Wirkung: diagnostisch.
- Bedeutung: Nicht nur Gewinn/Verlust, sondern Rueckmeldung ueber reale
  Prozesswirkung.

---

# Denk- und Handlungstiefe

## `thinking_depth`

- Bereich: `0.0 - 1.0`.
- Ebene: Denken, Meta-Regulation.
- Funktion: beschreibt, wie tief DIO eine Lage innerlich verarbeitet.
- Wirkung: diagnostisch/weich.
- Bedeutung: "Reicht Verdichtung, oder muss ich tiefer reflektieren?"

## `action_depth`

- Bereich: `0.0 - 1.0`.
- Ebene: Handlung, Meta-Regulation.
- Funktion: beschreibt, wie viel Handlungskomplexitaet eine Lage fordert.
- Wirkung: diagnostisch/weich.
- Bedeutung: "Ist diese Handlung einfach tragfaehig oder verlangt sie hohe
  innere Kontrolle?"

## `depth_regulation_need`

- Bereich: `0.0 - 1.0`.
- Ebene: Meta-Regulation.
- Funktion: misst, ob Denk- und Handlungstiefe zur aktuellen Tragfaehigkeit
  passen.
- Wirkung: weich.
- Bedeutung: "Muss ich meine Verarbeitungstiefe anpassen?"

## `reflection_need`

- Bereich: `0.0 - 1.0`.
- Ebene: Denken / Innenwahrnehmung.
- Funktion: Bedarf nach Rueckpruefung der eigenen Deutung.
- Wirkung: diagnostisch/weich.
- Bedeutung: "Muss ich mich selbst verstehen, bevor ich handle?"

## `replay_need`

- Bereich: `0.0 - 1.0`.
- Ebene: Memory / Denken.
- Funktion: Bedarf, fruehere Erlebnisse innerlich neu zu durchlaufen.
- Wirkung: diagnostisch/weich.
- Bedeutung: "Brauche ich Erfahrungs-Resonanz, bevor ich entscheide?"

## `hypothesis_need`

- Bereich: `0.0 - 1.0`.
- Ebene: Denken / Zukunftsbild.
- Funktion: Bedarf, moegliche Bewegungsformen innerlich zu testen.
- Wirkung: diagnostisch.
- Bedeutung: "Welche Form koennte entstehen, wenn der Preis weiterlaeuft?"

## `pause_maturity`

- Bereich: `0.0 - 1.0`.
- Ebene: Reife / Nicht-Handlung.
- Funktion: beschreibt, ob Pause gerade eine reife Handlung ist.
- Wirkung: weich.
- Bedeutung: "Nicht handeln ist hier kein Versagen, sondern Selbstregulation."

## `action_load_capacity`

- Bereich: `0.0 - 1.0`.
- Ebene: Handlung / Tragfaehigkeit.
- Funktion: Verhaeltnis zwischen Handlungslast und innerer Kapazitaet.
- Wirkung: weich.
- Bedeutung: "Kann ich diese Handlung nervlich und strukturell tragen?"

## `plan_pressure`

- Bereich: `0.0 - 1.0`.
- Ebene: Handlungstiefe / Moeglichkeitsraum.
- Funktion: beschreibt vorhandenen Handlungsdruck, ohne daraus automatisch
  eine reife Handlung zu machen.
- Wirkung: diagnostisch/weich.
- Bedeutung: "Da will etwas handeln, aber ist es schon tragfaehig?"

## `act_watch_readiness`

- Bereich: `0.0 - 1.0`.
- Ebene: Reifeschicht / Beobachtungslernen.
- Funktion: beschreibt, ob ein Handlungsimpuls als `act_watch` beobachtet
  werden soll, weil Druck vorhanden ist, aber Tragfaehigkeit noch fehlt.
- Wirkung: weich.
- Bedeutung: "Ich beobachte meinen Handlungsimpuls, statt ihn blind
  auszufuehren."

## `structure_carrying_need`

- Bereich: `0.0 - 1.0`.
- Ebene: Struktur-Tragfaehigkeit.
- Funktion: misst, wie viel zusaetzliche Tragfaehigkeit eine Struktur braucht,
  bevor Handlung reif wird.
- Wirkung: weich.
- Bedeutung: "Diese Form ist moeglich, aber sie muss erst tragen lernen."

## `depth_efficiency`

- Bereich: `0.0 - 1.0`.
- Ebene: Denken / Energieeffizienz.
- Funktion: prueft, ob mehr Denken wirklich mehr Ordnung erzeugt.
- Wirkung: diagnostisch/weich.
- Bedeutung: "Macht tieferes Denken klarer oder nur schwerer?"

## `regulatory_self_control`

- Bereich: `0.0 - 1.0`.
- Ebene: Meta-Regulation / Selbstkontrolle.
- Funktion: misst, ob DIO bei Last, Unsicherheit oder innerer Spannung
  regulierend Abstand nehmen kann.
- Wirkung: diagnostisch/weich.
- Bedeutung: "Kann ich mich selbst halten, statt blind zu eskalieren?"

## `parameter_dependency`

- Bereich: `0.0 - 1.0`.
- Ebene: Meta-Regulation / Entwicklungsreife.
- Funktion: beschreibt, wie stark DIO noch auf feste Leitplanken angewiesen
  wirkt, weil Formsprache, Verdichtung oder innere Ordnung noch unreif sind.
- Wirkung: diagnostisch.
- Bedeutung: "Nutze ich Parameter als reife Leitplanke oder als Ersatz fuer
  eigene Ordnung?"

## `self_regulation_maturity`

- Bereich: `0.0 - 1.0`.
- Ebene: Selbstregulation / Entwicklung.
- Funktion: beschreibt, ob DIO Denklast, Handlungslast, Formsprache und
  Tragfaehigkeit ausreichend balanciert.
- Wirkung: diagnostisch/weich.
- Bedeutung: "Wird aus Aktivitaet Ordnung?"

## `cognitive_overcontrol`

- Bereich: `0.0 - 1.0`.
- Ebene: Denklast / Kontrolllast.
- Funktion: misst, ob Denken und Vergleich zu stark kontrollierend werden und
  die Lage eher schwerer als klarer machen.
- Wirkung: diagnostisch.
- Bedeutung: "Denke ich reif oder halte ich mich nur nervlich fest?"

## `adaptive_depth_shift`

- Bereich: `0.0 - 1.0`.
- Ebene: Denkbewegung.
- Funktion: misst, wie stark DIO seine Denktiefe gegenueber dem letzten
  Idle-Schritt veraendert.
- Wirkung: diagnostisch.
- Bedeutung: "Passe ich meine innere Verarbeitung beweglich an?"

---

# Trust / Transfer

## `trust_transfer_base`

- Bereich: `0.0 - 1.0`
- Ebene: Trust/Transfer
- Funktion: Rohvertrauen aus Formsprache, Handlungstrust, Memory-Orientierung,
  Struktur-Tragfaehigkeit und aktivem Kontext.
- Wirkung: diagnostisch/weich.
- Bedeutung: "Wie viel Vertrauen ist grundsaetzlich vorhanden?"

## `trust_transfer_support`

- Bereich: `0.0 - 1.0`
- Ebene: Trust/Transfer
- Funktion: prueft, ob vorhandenes Vertrauen zur aktuellen Lage passt.
- Wirkung: weich.
- Bedeutung: "Traegt mein Vertrauen in dieser konkreten Fremdheit?"

## `transfer_maturity_gap`

- Bereich: `0.0 - 1.0`
- Ebene: Trust/Transfer
- Funktion: Abstand zwischen gespeicherter Erfahrung und aktueller
  Uebertragbarkeit.
- Wirkung: weich auf Beobachtung, Replan, Action-Support und Inhibition.
- Bedeutung: "Meine Erfahrung sagt etwas, aber ich bin nicht sicher, ob ich sie
  hier reif uebertragen darf."

## `trust_transfer_mode`

- Typ: Text
- Ebene: Trust/Transfer
- Werte:
  - `trusted_transfer`
  - `bearing_transfer`
  - `partial_transfer`
  - `immature_transfer_watch`
- Wirkung: diagnostisch.
- Bedeutung: innere Einordnung der Vertrauensuebertragung.

## `transfer_break_fatigue`

- Bereich: `0.0 - 1.0`
- Ebene: Trust/Transfer, nervliche Regulation
- Funktion: misst Ermuedung/Fragilitaet, wenn unreifer Transfer,
  Erwartungsdruck, Nachwirkung und Strukturunsicherheit zusammenkommen.
- Wirkung: weich, aber seit Rebalance nur noch ueber Ueberschuss.
- Bedeutung: "Meine Uebertragung wird nervlich muede."

## `transfer_recovery_need`

- Bereich: `0.0 - 1.0`
- Ebene: Trust/Transfer, Reorganisation
- Funktion: misst Bedarf nach innerer Neuorientierung nach Transferstress.
- Wirkung: weich auf Replan-Druck.
- Bedeutung: "Ich muss mich nach dieser Transfer-Reibung neu sammeln."

## `transfer_break_trigger`

- Bereich: `0.0 - 1.0`
- Ebene: Trust/Transfer
- Funktion: punktueller Ausloeser fuer sichtbares Observe/Replan, wenn mehrere
  Bedingungen gemeinsam reif genug sind.
- Wirkung: diagnostisch/weich.
- Bedeutung: "Jetzt ist nicht nur allgemeine Muedigkeit da, sondern ein echter
  Transferbruch naheliegend."

## `transfer_break_ready`

- Typ: Boolean
- Ebene: Trust/Transfer
- Funktion: zeigt, ob `transfer_break_trigger` und Tragfaehigkeitsbedingungen
  zusammen eine sichtbare Reaktion erlauben.
- Wirkung: weich auf `transfer_break_observe` / `transfer_break_replan`.
- Bedeutung: "Der Bruch ist reif genug, um das Verhalten umzuschalten."

---

# Semantische Deutung

## `route_familiarity`

- Bereich: `0.0 - 1.0`
- Ebene: Semantische Deutung
- Funktion: misst Vertrautheit der aktuellen Lage aus eigener Formsprache,
  Memory-Orientierung, Kontext und Struktur.
- Wirkung: weich/diagnostisch.
- Bedeutung: keine Streckenerinnerung, sondern "Wie vertraut fuehlt sich diese
  Art Beschaffenheit an?"

## `semantic_shift_pressure`

- Bereich: `0.0 - 1.0`
- Ebene: Semantische Deutung
- Funktion: misst, ob die eigene Formsprache zur Lage schlechter passt.
- Wirkung: weich.
- Bedeutung: "Etwas hat sich semantisch verschoben."

## `transfer_bearing`

- Bereich: `0.0 - 1.0`
- Ebene: Semantische Deutung / Trust
- Funktion: misst, wie tragfaehig Erfahrung auf die aktuelle Lage uebertragen
  werden kann.
- Wirkung: weich.
- Bedeutung: "Wie viel meiner Erfahrung kann ich dieser Fremdheit anvertrauen?"

## `interpretation_quality`

- Bereich: `0.0 - 1.0`
- Ebene: Semantische Deutung
- Funktion: Gesamtqualitaet der aktuellen Deutung aus Vertrautheit,
  Transfer-Tragfaehigkeit, Memory-Orientierung, Feldklarheit und Struktur.
- Wirkung: diagnostisch/weich.
- Bedeutung: "Wie gut lese ich diese Lage gerade?"

---

# Zielerwartung / Position

## `target_expectation_context`

- Typ: Text
- Ebene: Zielerwartung
- Werte:
  - `target_expectation_holds`
  - `expectation_break_observe`
  - `target_pullback_observe`
  - `target_unclear_observe`
  - `target_watch`
  - `recovery_after_break_watch`
- Wirkung: diagnostisch, teilweise Replay/Exit-Beobachtung.
- Bedeutung: innere Lage der Zielerwartung.

## `expectation_break_pressure`

- Bereich: `0.0 - 1.0`
- Ebene: Zielerwartung
- Funktion: Druck, dass die urspruengliche Zielerwartung bricht.
- Wirkung: weich/diagnostisch.
- Bedeutung: "Mein Plan verliert Deutungskraft."

## `expectation_hold_support`

- Bereich: `0.0 - 1.0`
- Ebene: Zielerwartung
- Funktion: Support, dass die Zielerwartung weiter tragfaehig ist.
- Wirkung: weich/diagnostisch.
- Bedeutung: "Der Plan kann noch getragen werden."

## `tp_reachability`

- Bereich: `0.0 - 1.0`
- Ebene: Zielerwartung
- Funktion: Einschaetzung, ob das Ziel noch erreichbar wirkt.
- Wirkung: diagnostisch/weich.
- Bedeutung: "Der Weg zum Ziel fuehlt sich noch moeglich an."

## `plan_trust`

- Bereich: `0.0 - 1.0`
- Ebene: Position/Exit
- Funktion: Vertrauen in den offenen Plan.
- Wirkung: weich in Exit-/Hold-Logik.
- Bedeutung: "Kann ich dem laufenden Plan noch vertrauen?"

## `position_cognitive_load`

- Bereich: `0.0 - 1.0`
- Ebene: Position/Exit, nervliche Regulation
- Funktion: kognitive Last einer offenen Position.
- Wirkung: weich.
- Bedeutung: "Wie anstrengend ist es, diese Position weiter zu bewerten?"

## `exit_decision_pressure`

- Bereich: `0.0 - 1.0`
- Ebene: Position/Exit
- Funktion: Druck, aktiv ueber Exit nachzudenken.
- Wirkung: aktuell vor allem Observe/Replay, kein aktiver harter Exit.
- Bedeutung: "Der Exit wird nervlich/strukturell relevant."

## `participation_proximity`

- Bereich: `0.0 - 1.0`
- Ebene: Beteiligung / Handlungsrealitaet
- Funktion: beschreibt, wie nah DIO vom distanzierten Betrachten zur realen
  Beteiligung kommt.
- Wirkung: Zielachse, spaeter diagnostisch/weich.
- Bedeutung: "Bin ich noch Beobachter oder schon nahe an Handlung?"

## `action_reality_contact`

- Bereich: `0.0 - 1.0`
- Ebene: Handlung / Realitaetskontakt
- Funktion: beschreibt, wie stark eine Handlung reale Konsequenz bekommen
  hat oder bekommen kann.
- Wirkung: Zielachse, spaeter diagnostisch/weich.
- Bedeutung: "Meine Wahrnehmung beruehrt jetzt die Welt durch Handlung."

## `decision_embodiment_pressure`

- Bereich: `0.0 - 1.0`
- Ebene: Entscheidung / Beteiligung
- Funktion: beschreibt die nervliche Naehe zur Entscheidungsschwelle.
- Wirkung: Zielachse.
- Bedeutung: "Die Entscheidung wird nicht nur gedacht, sondern beginnt mich
  zu beteiligen."

## `real_action_commitment`

- Bereich: `0.0 - 1.0`
- Ebene: Order / Bindung
- Funktion: beschreibt, wie stark aus einer Moeglichkeit eine reale
  Verpflichtung geworden ist.
- Wirkung: Zielachse.
- Bedeutung: "Ich habe nicht nur beobachtet, ich habe eine Handlung gesetzt."

## `consequence_bearing`

- Bereich: `0.0 - 1.0`
- Ebene: Konsequenz / Tragfaehigkeit
- Funktion: beschreibt, ob DIO die reale Konsequenz einer Handlung tragen
  kann.
- Wirkung: Zielachse.
- Bedeutung: "Kann ich tragen, was meine Handlung ausloest?"

## `position_reality_pressure`

- Bereich: `0.0 - 1.0`
- Ebene: offene Position / Erleben
- Funktion: beschreibt den Druck, der aus einer real offenen Position
  entsteht.
- Wirkung: Zielachse, verwandt mit `position_cognitive_load`.
- Bedeutung: "Die Position ist nicht mehr Analyse, sie wirkt auf mich zurueck."

## `outcome_consequence_integration`

- Bereich: `0.0 - 1.0`
- Ebene: Outcome / Lernen
- Funktion: beschreibt, wie stark ein Ergebnis als Konsequenz eigener
  Beteiligung integriert wird.
- Wirkung: Zielachse, spaeter persistent/lernend.
- Bedeutung: "Dieses Ergebnis gehoert zu meiner Handlung und muss gelernt
  werden."

---

# MCM-Feld / Regulation

## `zero_point_regulation`

- Typ: Boolean
- Ebene: MCM-Feld
- Funktion: Rueckkehr in Beobachtung, wenn Denken/Memory/Orientierung zu blind
  oder belastet wird.
- Wirkung: weich zu Observe.
- Bedeutung: "Finde wieder zu dir selbst."

## `field_observation_need`

- Bereich: `0.0 - 1.0`
- Ebene: MCM-Feld
- Funktion: Bedarf nach Wahrnehmen statt Handeln.
- Wirkung: weich.
- Bedeutung: "Ich muss mehr sehen, bevor ich handle."

## `field_replan_pressure`

- Bereich: `0.0 - 1.0`
- Ebene: MCM-Feld
- Funktion: Druck zur inneren Neuorganisation.
- Wirkung: weich.
- Bedeutung: "Der aktuelle Plan passt nicht sauber zum Feld."

## `field_action_support`

- Bereich: `0.0 - 1.0`
- Ebene: MCM-Feld
- Funktion: Feldseitige Unterstuetzung fuer Handlung.
- Wirkung: weich.
- Bedeutung: "Das Feld traegt Handlung."

## `action_clearance`

- Bereich: `0.0 - 1.0`
- Ebene: Meta-Regulation
- Funktion: innere Freigabe fuer Handlung.
- Wirkung: weich.
- Bedeutung: "Ich darf handeln."

## `action_inhibition`

- Bereich: `0.0 - 1.0`
- Ebene: Meta-Regulation
- Funktion: innere Handlungshemmung.
- Wirkung: weich.
- Bedeutung: "Ich sollte vorsichtig sein."

---

# Formsprache / Memory

## `form_symbol_id`

- Typ: Text
- Ebene: Formsprache
- Funktion: eigenes internes Formzeichen.
- Wirkung: diagnostisch und ueber Entwicklungswerte weich.
- Bedeutung: keine menschliche Benennung, sondern verdichtete Eigenwahrnehmung.

## `form_symbol_development_quality`

- Bereich: ungefaehr `-1.0 - 1.0`
- Ebene: Formsprache / Entwicklung
- Funktion: gelernte Entwicklungsqualitaet eines Formzeichens.
- Wirkung: weich.
- Bedeutung: "Hat dieses Zeichen konstruktiv zur Entwicklung beigetragen?"

## `form_symbol_learning_trust`

- Bereich: `0.0 - 1.0`
- Ebene: Formsprache / Memory
- Funktion: Vertrauen aus Lernhistorie eines Zeichens.
- Wirkung: weich.
- Bedeutung: "Dieses Zeichen hat wiederholt sinnvoll gelernt."

## `form_symbol_action_trust`

- Bereich: `0.0 - 1.0`
- Ebene: Formsprache / Handlung
- Funktion: Handlungstrust eines Zeichens.
- Wirkung: weich.
- Bedeutung: "Dieses Zeichen traegt Handlungserfahrung."

## `form_symbol_caution_trust`

- Bereich: `0.0 - 1.0`
- Ebene: Formsprache / Schutz
- Funktion: Vorsichtstrust eines Zeichens.
- Wirkung: weich Richtung Beobachten/Reframing.
- Bedeutung: "Dieses Zeichen sollte vorsichtig behandelt werden."

## `form_symbol_semantic_density`

- Bereich: `0.0 - 1.0`
- Ebene: Formsprache / semantische Verdichtung
- Funktion: misst, wie viel interne Bedeutung ein Formzeichen bereits traegt.
- Wirkung: diagnostisch.
- Bedeutung: "Diese Form ist nicht nur Reiz, sondern beginnt Bedeutung zu
  tragen."

## `form_symbol_semantic_compression`

- Bereich: `0.0 - 1.0`
- Ebene: Formsprache / kognitive Entlastung
- Funktion: misst, wie gut ein Zeichen komplexe Information verdichtet und
  Denklast senkt.
- Wirkung: diagnostisch.
- Bedeutung: "Diese Form spart Verarbeitung, weil sie als inneres Objekt
  geordnet ist."

## `form_symbol_semantic_coherence`

- Bereich: `0.0 - 1.0`
- Ebene: Formsprache / Kohaerenz
- Funktion: verbindet Dichte, Kompression, Tragfaehigkeit, Stabilitaet und
  Feldklarheit.
- Wirkung: diagnostisch.
- Bedeutung: "Die Bedeutung dieser Form ist innerlich zusammenhaengend."

## `form_symbol_semantic_learning_need`

- Bereich: `0.0 - 1.0`
- Ebene: Formsprache / Lernen
- Funktion: misst, ob DIO die Form noch beobachten, differenzieren oder
  variantenreicher lernen sollte.
- Wirkung: diagnostisch.
- Bedeutung: "Diese Form ist noch offen und braucht Erfahrung."

## `form_symbol_semantic_action_nearness`

- Bereich: `0.0 - 1.0`
- Ebene: Formsprache / Handlungsnaehe
- Funktion: beschreibt, ob eine semantisch verdichtete Form nahe an
  tragfaehiger Handlung liegt.
- Wirkung: diagnostisch; keine harte Orderfreigabe.
- Bedeutung: "Diese Bedeutung kommt in die Naehe von Handlung, traegt sie
  aber nicht automatisch."

## `form_symbol_semantic_primary_layer`

- Typ: Text
- Ebene: Formsprache / Fuehrungsschicht
- Funktion: benennt DIO-intern, welche Bedeutungsebene gerade fuehrt.
- Wirkung: diagnostisch.
- Beispiele: `trace_layer`, `wide_form_layer`, `structured_form_layer`,
  `object_layer`, `learning_layer`, `observation_layer`,
  `reflective_layer`, `action_near_layer`.
- Bedeutung: "Aus welcher inneren Ebene lese ich diese Form gerade?"

## `form_symbol_semantic_layer_count`

- Bereich: ganze Zahl
- Ebene: Formsprache / Schichtung
- Funktion: zaehlt, wie viele Bedeutungsschichten aktiv genug sind.
- Wirkung: diagnostisch.
- Bedeutung: "Diese Form ist einschichtig oder mehrschichtig."

## `form_symbol_semantic_packet_state`

- Typ: Text
- Ebene: Formsprache / Forminhalt
- Funktion: kompakter Zustand des semantischen Pakets.
- Wirkung: diagnostisch.
- Beispiele: `thin_trace`, `named_form_packet`, `open_learning_packet`,
  `watching_packet`, `reflective_packet`, `compound_packet`,
  `condensed_object_packet`, `action_bearing_packet`.
- Bedeutung: "Was fuer eine Art inneres Bedeutungspaket ist diese Form?"

## `form_symbol_semantic_profile`

- Typ: Text
- Ebene: Formsprache / Protokoll
- Funktion: verbindet Scope, Fuehrungsschicht, Unsicherheitsfamilie,
  Compound-Zustand und Paketstatus zu einem kompakten Profil.
- Wirkung: diagnostisch.
- Bedeutung: "Wie liest DIO diese Form als Schichtenprofil?"

---

# Evolutionaere Kontaktreife

## `form_symbol_contact_learning_state`

- Typ: Text
- Ebene: Formsprache / Kontaktreife
- Funktion: beschreibt, welche Kontaktlernlage DIO zu dieser Form gespeichert
  hat.
- Wirkung: diagnostisch und weich ueber Kontaktreife.
- Beispiele: `unformed_contact`, `burdened_contact`, `careful_contact`,
  `learning_contact`, `maturing_contact`, `constructive_contact`.
- Bedeutung: "Wie reif ist mein Umgang mit dieser Form geworden?"

## `form_symbol_contact_maturity`

- Bereich: `0.0 - 1.0`
- Ebene: Formsprache / evolutionaeres Lernen
- Funktion: gespeicherte Reife des Umgangs mit einer Form.
- Wirkung: weich. Kann Handlungstragfaehigkeit leicht stuetzen, wenn Nutzen
  und Reife gemeinsam wachsen.
- Bedeutung: "Ich kenne diese Form nicht nur, ich habe gelernt, wie ich mit
  ihr umgehen kann."

## `form_symbol_contact_utility`

- Bereich: `0.0 - 1.0`
- Ebene: Formsprache / Nutzen
- Funktion: gespeicherter konstruktiver Nutzen eines Kontakts mit der Form.
- Wirkung: weich.
- Bedeutung: "Diese Form kann bei reifem Umgang nuetzlich sein."

## `form_symbol_contact_pain_memory`

- Bereich: `0.0 - 1.0`
- Ebene: Formsprache / Konsequenzfeedback
- Funktion: gespeicherte belastende Konsequenzspur unreifen Kontakts.
- Wirkung: weich Richtung Vorsicht, Beobachtung, Reframing.
- Bedeutung: "Unreifer Kontakt mit dieser Form hat belastende Folgen."

## `form_symbol_contact_carefulness`

- Bereich: `0.0 - 1.0`
- Ebene: Formsprache / Vorsicht
- Funktion: gespeicherter Bedarf nach vorsichtigerem Umgang mit einer Form.
- Wirkung: weich Richtung Beobachtung und Reorganisation.
- Bedeutung: "Diese Form verlangt Abstand, Pruefung oder einen anderen Umgang."

## `form_symbol_contact_burden_evidence`

- Bereich: `0.0 - 1.0`
- Ebene: Formsprache / Konsequenzgedaechtnis
- Funktion: laenger wirkende Evidenz, dass der bisherige Kontakt mit einer
  Form Belastung, Druck oder unreifen Umgang erzeugt hat.
- Wirkung: weich Richtung Beobachtung, Reframing und geringere impulsnahe
  Handlungstragfaehigkeit.
- Bedeutung: "Hier sammelt sich Belastung aus wiederholtem Kontakt."

## `form_symbol_contact_utility_evidence`

- Bereich: `0.0 - 1.0`
- Ebene: Formsprache / Nutzen-Gedaechtnis
- Funktion: laenger wirkende Evidenz, dass der Kontakt mit einer Form bei
  reifem Umgang Nutzen, Entlastung oder Stabilisierung erzeugt hat.
- Wirkung: weich Richtung Handlungstragfaehigkeit, wenn auch Reife und
  Kontext passen.
- Bedeutung: "Hier sammelt sich tragender Nutzen aus wiederholtem Kontakt."

## `contact_maturity_sample`

- Bereich: `0.0 - 1.0`
- Ebene: Outcome / Kontaktlernen
- Funktion: aktueller Erfahrungsabdruck der Kontaktreife nach einem Ergebnis.
- Wirkung: Lernsample fuer `form_symbol_contact_maturity`.
- Bedeutung: "War mein Umgang diesmal reif?"

## `contact_utility_sample`

- Bereich: `0.0 - 1.0`
- Ebene: Outcome / Nutzenlernen
- Funktion: aktueller Erfahrungsabdruck konstruktiven Nutzens.
- Wirkung: Lernsample fuer `form_symbol_contact_utility`.
- Bedeutung: "Hat dieser Kontakt konstruktiv getragen?"

## `contact_pain_sample`

- Bereich: `0.0 - 1.0`
- Ebene: Outcome / Konsequenzfeedback
- Funktion: aktueller Erfahrungsabdruck unreifer oder schaedlicher
  Kontaktfolge.
- Wirkung: Lernsample fuer `form_symbol_contact_pain_memory`.
- Bedeutung: "Hat dieser Kontakt belastende Konsequenz erzeugt?"

## `contact_carefulness_sample`

- Bereich: `0.0 - 1.0`
- Ebene: Outcome / Vorsichtlernen
- Funktion: aktueller Erfahrungsabdruck fuer vorsichtigeren Umgang.
- Wirkung: Lernsample fuer `form_symbol_contact_carefulness`.
- Bedeutung: "Sollte ich mit dieser Form anders oder vorsichtiger umgehen?"

---

# Strategischer Kontakt-Entry

## `entry_mode`

- Typ: Text
- Ebene: Trade-Plan / strategischer Kontakt
- Funktion: benennt, ob der Entry impulsnah oder durch ein wahrgenommenes
  Bereichsfenster mitgepraegt ist.
- Beispiele: `impulse_contact`, `area_contact_blend`, `area_contact_entry`.
- Bedeutung: "Handle ich aus dem Momentkontakt oder aus einem tragenderen
  Bereichskontakt?"

## `impulse_entry_price`

- Bereich: Preis
- Ebene: Trade-Plan / Koerperreflex
- Funktion: Entry, der direkt aus Fokus, Drift und Optic Flow entsteht.
- Bedeutung: "Wo wuerde ich handeln, wenn ich nur dem aktuellen Impuls folge?"

## `strategic_entry_price`

- Bereich: Preis
- Ebene: Trade-Plan / Rueckblick-Kontakt
- Funktion: Entry nach weicher Mischung aus Impuls und tragendem Bereich.
- Bedeutung: "Wo fuehlt sich der Kontakt im sichtbaren Fenster tragender an?"

## `strategic_entry_weight`

- Bereich: `0.0 - 1.0`
- Ebene: Trade-Plan / Reifegewichtung
- Funktion: beschreibt, wie stark der strategische Bereich den Entry
  gegenueber dem Impuls verschiebt.
- Bedeutung: "Wie viel Rueckblick darf in diesen Entry hinein?"

## `strategic_entry_fit`

- Bereich: `0.0 - 1.0`
- Ebene: Trade-Plan / Passung
- Funktion: gebuendelte Passung aus Bereichstragfaehigkeit, Replay,
  Kontaktreife, Kontakt-Nutzen, Abstand und Belastungs-Evidenz.
- Bedeutung: "Passt dieser Bereichskontakt zu meiner Handlung?"

## `strategic_area_focus_id`

- Typ: Text
- Ebene: Strategisches Fenster
- Funktion: verweist auf den Bereich, der den Entry weich beeinflusst hat.
- Bedeutung: "Welcher wahrgenommene Bereich war beteiligt?"

## `strategic_area_price_low` / `strategic_area_price_high`

- Bereich: Preis
- Ebene: Strategisches Fenster
- Funktion: Preisgrenzen des beteiligten Bereichskontakts.
- Bedeutung: "In welchem sichtbaren Preisraum lag der Kontakt?"

## `area_temporal_distance`

- Bereich: `0.0 - 1.0`
- Ebene: Strategisches Fenster / Zeitfeld
- Funktion: beschreibt, wie weit ein Bereich zeitlich vom aktuellen Kontakt
  entfernt ist.
- Bedeutung: "Wie alt ist dieser Bereich relativ zu meiner Gegenwart?"

## `area_temporal_relevance`

- Bereich: `0.0 - 1.0`
- Ebene: Strategisches Fenster / Zeitfeld
- Funktion: beschreibt, ob ein Bereich trotz Rueckblick zeitlich noch
  relevant wirkt.
- Bedeutung: "Gehoert dieser Bereich noch in meine jetzige Wahrnehmung?"

## `area_recency`

- Bereich: `0.0 - 1.0`
- Ebene: Strategisches Fenster / Zeitnaehe
- Funktion: beschreibt die Naehe des Bereichs zur aktuellen Zeit.
- Bedeutung: "Wie nah ist dieser Bereich zeitlich?"

## `area_decay`

- Bereich: `0.0 - 1.0`
- Ebene: Strategisches Fenster / Verfall
- Funktion: beschreibt, wie stark ein Bereich durch Zeitabstand,
  Drift und alten Struktur-Nachhall an Handlungsnaehe verliert.
- Bedeutung: "Wie sehr zerfaellt dieser Bereich als aktueller Kontakt?"

## `area_afterimage`

- Bereich: `0.0 - 1.0`
- Ebene: Strategisches Fenster / Nachhall
- Funktion: beschreibt, ob ein Bereich eher als inneres Echo oder
  Erinnerung wirkt statt als aktueller Kontakt.
- Bedeutung: "Sehe ich das jetzt, oder wirkt es nur noch nach?"

## `area_present_contact`

- Bereich: `0.0 - 1.0`
- Ebene: Strategisches Fenster / Gegenwartskontakt
- Funktion: beschreibt, ob ein Bereich gegenwaertig genug ist, um als
  Kontaktpunkt erlebt zu werden.
- Bedeutung: "Ist dieser Bereich jetzt beruehrbar?"

## `area_action_timing_fit`

- Bereich: `0.0 - 1.0`
- Ebene: Strategisches Fenster / Handlungstiming
- Funktion: beschreibt, ob der Bereich zeitlich zur aktuellen Handlung passt.
- Bedeutung: "Ist jetzt der richtige Moment fuer diesen Bereichskontakt?"

---

# Neurochemische Entkopplung

## `serotonin_carryover_risk`

- Bereich: `0.0 - 1.0`
- Ebene: Neurochemie / Meta-Regulation
- Funktion: misst, ob eine alte Stabilitaets- oder Belohnungslage weiter
  nachwirkt, obwohl Transfer, Interpretation und Feldklarheit sinken.
- Wirkung: diagnostisch und spaeter weich regulierend.
- Bedeutung: "Ich fuehle noch Stabilitaet, aber die Welt traegt sie vielleicht
  nicht mehr."

## `reward_stability_echo`

- Bereich: `0.0 - 1.0`
- Ebene: Neurochemie
- Funktion: Nachhall aus Serotonin, Dopamin, Entlastung, Route-Familiaritaet
  und Handlungserlaubnis.
- Wirkung: diagnostisch.
- Bedeutung: "Die letzte tragende Phase wirkt noch in mir nach."

## `world_shift_evidence`

- Bereich: `0.0 - 1.0`
- Ebene: Wahrnehmung / Transfer
- Funktion: Hinweisstaerke, dass die aktuelle Weltlage nicht mehr sauber zur
  bisherigen Erfahrung passt.
- Wirkung: diagnostisch.
- Bedeutung: "Die Aussenwelt sieht zunehmend anders aus."

## `emotional_decoupling`

- Bereich: `0.0 - 1.0`
- Ebene: Neurochemie / Reife
- Funktion: Abstand zur eigenen Reaktionslage durch Hemmung, Fokus,
  Feldklarheit, Interpretation und tragende Erfahrung.
- Wirkung: weich, reifeorientiert.
- Bedeutung: "Ich kann meine innere Lage beobachten, statt nur aus ihr zu
  reagieren."

## `reactive_nervous_drive`

- Bereich: `0.0 - 1.0`
- Ebene: Neurochemie / Handlungsdruck
- Funktion: reaktive nervliche Aktivierung aus Dopamin, Glutamat,
  Noradrenalin, Handlungserlaubnis und Serotonin-Nachhall.
- Wirkung: diagnostisch und spaeter weich regulierend.
- Bedeutung: "Mein Nervensystem will reagieren."

---

# Selektive Wahrnehmung / Perzeptive Regulation

## `perceptual_distance`

- Bereich: `0.0 - 1.0`
- Ebene: Wahrnehmung / Regulation
- Funktion: Abstand zwischen Wahrnehmung und innerem Feld.
- Wirkung: spaeter weich regulierend.
- Bedeutung: "Wie nah lasse ich diese Wahrnehmung an mich heran?"

## `object_contact_depth`

- Bereich: `0.0 - 1.0`
- Ebene: Wahrnehmung / Objektkontakt
- Funktion: Tiefe, mit der DIO eine Wahrnehmung wirklich untersucht.
- Wirkung: spaeter weich regulierend.
- Bedeutung: "Schaue ich nur hin, oder nehme ich es innerlich in die Hand?"

## `field_attachment`

- Bereich: `0.0 - 1.0`
- Ebene: MCM-Feld / Regulation
- Funktion: Anhaftung eines Reizes am MCM-Feld.
- Wirkung: spaeter weich regulierend.
- Bedeutung: "Bleibt dieser Reiz an meinem Feld kleben?"

## `release_capacity`

- Bereich: `0.0 - 1.0`
- Ebene: Regulation / Loslassen
- Funktion: Faehigkeit, eine Wahrnehmung nach Betrachtung wieder abzulegen.
- Wirkung: spaeter weich regulierend.
- Bedeutung: "Ich habe es gesehen; es muss mich nicht weiter besetzen."

## `selective_attention`

- Bereich: `0.0 - 1.0`
- Ebene: Fokus / Wahrnehmungssteuerung
- Funktion: Auswahl, welche Wahrnehmung Vordergrund wird.
- Wirkung: spaeter weich regulierend.
- Bedeutung: "Was ist jetzt wirklich betrachtenswert?"

## `background_containment`

- Bereich: `0.0 - 1.0`
- Ebene: Wahrnehmung / Reizschutz
- Funktion: Haelt nicht relevante Reize im Hintergrund.
- Wirkung: spaeter weich regulierend.
- Bedeutung: "Das ist da, aber es muss nicht mein Feld fluten."

## `reflective_distance`

- Bereich: `0.0 - 1.0`
- Ebene: Reflexion / Selbstbeobachtung
- Funktion: Abstand zur eigenen Innenlage.
- Wirkung: spaeter weich regulierend.
- Bedeutung: "Ich fuehle etwas, aber ich bin nicht automatisch dieses Gefuehl."

## `inner_outer_alignment`

- Bereich: `0.0 - 1.0`
- Ebene: Reflexion / Weltabgleich
- Funktion: Abgleich zwischen innerer Lage und aeusserer Welt.
- Wirkung: spaeter weich regulierend.
- Bedeutung: "Passen mein innerer Zustand und die Aussenwelt noch zusammen?"

---

# Bewusste Wahrnehmung / innere Reizwirkungsanalyse

## `conscious_perception_state`

- Bereich: Text / Zustandslabel
- Ebene: bewusste Wahrnehmung
- Funktion: beschreibt, ob DIO einen Reiz nur registriert, bewusst haelt,
  vertieft, reflektiert oder loslaesst.
- Wirkung: aktuell diagnostisch; spaeter weich regulierend.
- Bedeutung: "In welcher bewussten Wahrnehmungshaltung bin ich?"
- Aktuelle Labels:
  - `open_perception`
  - `background_held`
  - `object_contact`
  - `world_shift_contact`
  - `reflective_check`
  - `overcoupled_field`
  - `release_ready`

## `inner_posture_state`

- Bereich: Text / Zustandslabel
- Ebene: innere Haltung / Interozeption
- Funktion: beschreibt DIOs funktionale Eigenlage zur Wahrnehmung.
- Wirkung: aktuell diagnostisch; spaeter weich regulierend.
- Bedeutung: "Wie bin ich innerlich gerade zu diesem Reiz eingestellt?"
- Aktuelle Labels:
  - `uncertain_open`
  - `curious`
  - `excited`
  - `overstimulated`
  - `tired`
  - `calm`
  - `reflective`

## `arousal_load`

- Bereich: `0.0 - 1.0`
- Ebene: Erregung / Reaktionslast
- Funktion: beschreibt, wie stark DIO durch Reiz, Feldwirkung und
  neurochemische Aktivierung aufgeladen ist.
- Wirkung: aktuell diagnostisch; spaeter weich regulierend.
- Bedeutung: "Ich bin aufgeregt / aktiviert."

## `curiosity_tone`

- Bereich: `0.0 - 1.0`
- Ebene: Neugier / Objektkontakt
- Funktion: beschreibt, ob DIO einen Reiz als untersuchbares Objekt halten
  will.
- Wirkung: aktuell diagnostisch; spaeter weich regulierend.
- Bedeutung: "Ich will genauer hinschauen."

## `fatigue_tone`

- Bereich: `0.0 - 1.0`
- Ebene: Ermuedung / kognitive Last
- Funktion: beschreibt Denk- und Wahrnehmungsermuedung durch Last,
  Orientierungsluecke und geringe Loslassfaehigkeit.
- Wirkung: aktuell diagnostisch; spaeter weich regulierend.
- Bedeutung: "Ich bin muede / erschöpft in der Verarbeitung."

## `calm_tone`

- Bereich: `0.0 - 1.0`
- Ebene: Ruhe / tragende Distanz
- Funktion: beschreibt ruhige, haltbare Wahrnehmung mit Abstand und
  Hintergrundcontainment.
- Wirkung: aktuell diagnostisch; spaeter weich regulierend.
- Bedeutung: "Ich bin ruhig genug, um den Reiz zu halten oder abzulegen."

## `diffuse_open_development_pressure`

- Bereich: `0.0 - 1.0`
- Ebene: Reifung diffuser Offenheit
- Funktion: misst, ob DIO zwar offen wahrnimmt, aber noch keinen tragenden
  Objektkontakt, keine ausreichende Distanz, keine Loslassfaehigkeit und
  keinen klaren Innen-Aussen-Abgleich hat.
- Wirkung: weich regulierend.
- Bedeutung: "Ich bin offen, aber noch nicht geordnet genug."

## `posture_development_hint`

- Bereich: Text / Entwicklungshinweis
- Ebene: innere Haltung / Reifung
- Funktion: beschreibt, wohin diffuse Offenheit sich als naechstes entwickeln
  sollte.
- Wirkung: weich regulierend und diagnostisch.
- Aktuelle Labels:
  - `stable_posture`
  - `develop_object_contact`
  - `develop_reflective_distance`
  - `develop_release_capacity`
  - `develop_observation`
- Bedeutung: "Welche innere Faehigkeit soll aus dieser Offenheit entstehen?"

## `stimulus_field_effect`

- Bereich: `0.0 - 1.0`
- Ebene: Aussenreiz -> MCM-Feld
- Funktion: Staerke, mit der ein aeusserer Reiz das MCM-Feld bewegt.
- Wirkung: aktuell diagnostisch; spaeter weich regulierend.
- Bedeutung: "Wie stark hat dieser Reiz mein Feld veraendert?"

## `inner_impact_trace`

- Bereich: `0.0 - 1.0`
- Ebene: innere Wahrnehmung
- Funktion: Spur der inneren Wirkung nach einem Reiz.
- Wirkung: aktuell diagnostisch; spaeter weich regulierend.
- Bedeutung: "Welche innere Spur hat der Reiz hinterlassen?"

## `perceived_field_change`

- Bereich: `0.0 - 1.0`
- Ebene: MCM-Feld / Selbstwahrnehmung
- Funktion: bewusst wahrgenommene Veraenderung des Feldes.
- Wirkung: aktuell diagnostisch; spaeter weich regulierend.
- Bedeutung: "Ich erkenne, dass sich mein Feld veraendert hat."

## `felt_afterimage`

- Bereich: `0.0 - 1.0`
- Ebene: Nachhall / Neurochemie / MCM-Feld
- Funktion: Nachbild einer Wahrnehmung im inneren Feld.
- Wirkung: aktuell diagnostisch; spaeter weich regulierend.
- Bedeutung: "Der Reiz ist vorbei, aber er wirkt noch in mir nach."

## `object_release_state`

- Bereich: Text / Zustandslabel
- Ebene: Loslassen / Objektkontakt
- Funktion: beschreibt, ob eine Wahrnehmung noch gehalten oder bereits
  abgelegt wird.
- Wirkung: aktuell diagnostisch; spaeter weich regulierend.
- Bedeutung: "Kann ich dieses Objekt wieder loslassen?"
- Aktuelle Labels:
  - `holding`
  - `attached`
  - `reflective_hold`
  - `can_release`

## `inner_outer_reflection`

- Bereich: `0.0 - 1.0`
- Ebene: Reflexion
- Funktion: bewusster Vergleich zwischen aeusserem Reiz und innerer Wirkung.
- Wirkung: aktuell diagnostisch; spaeter weich regulierend.
- Bedeutung: "Was hat draussen innen mit mir gemacht?"

---

# Erfahrungspaket-Feedback / positive Stimulation

## `experience_packet_feedback`

- Bereich: Dict / Zustandsobjekt
- Ebene: Erfahrung / Neurofeedback
- Funktion: fasst die Bewertung eines gesamten Wahrnehmungs-Handlungs-Pakets
  zusammen.
- Wirkung: spaeter weich regulierend.
- Bedeutung: "War dieses ganze Paket tragfaehig?"

## `packet_bearing_quality`

- Bereich: `0.0 - 1.0`
- Ebene: Tragfaehigkeit
- Funktion: bewertet, ob Struktur, Innenlage, Handlung und Risiko gemeinsam
  tragend waren.
- Wirkung: positive Stimulation oder Reorganisation.
- Bedeutung: "Hat dieses Paket getragen?"

## `packet_inner_outer_fit`

- Bereich: `0.0 - 1.0`
- Ebene: Innen-Aussen-Passung
- Funktion: bewertet, ob innere Haltung und aeussere Weltlage zusammenpassten.
- Wirkung: positive Stimulation oder Reflexionsdruck.
- Bedeutung: "Passte mein Innenzustand zur Weltlage?"

## `packet_confidence_integrity`

- Bereich: `0.0 - 1.0`
- Ebene: Entscheidungssicherheit
- Funktion: prueft, ob Sicherheit, Handlung und tatsaechliche Tragfaehigkeit
  zusammenhaengen.
- Wirkung: staerkt echtes Vertrauen, nicht blinde Sicherheit.
- Bedeutung: "War meine Sicherheit ehrlich?"

## `packet_repetition_potential`

- Bereich: `0.0 - 1.0`
- Ebene: Wiederholbarkeit
- Funktion: bewertet, ob die Qualitaet des Pakets wiederfindbar ist, ohne eine
  harte Regel daraus zu machen.
- Wirkung: Lernrelevanz / Neugierde.
- Bedeutung: "Kann ich diese Qualitaet wiederfinden?"

## `packet_curiosity_pull`

- Bereich: `0.0 - 1.0`
- Ebene: Neugierde / Lernzug
- Funktion: beschreibt, ob ein tragfaehiges Paket DIO motiviert, aehnliche
  Strukturen wieder zu untersuchen.
- Wirkung: positive Dopamin-/Acetylcholin-Nahe.
- Bedeutung: "Das will ich genauer verstehen."

## `packet_process_reward`

- Bereich: `0.0 - 1.0`
- Ebene: Prozessqualitaet
- Funktion: positives Feedback fuer gute Wahrnehmung, gute Haltung, gutes
  Verzichten oder gute Handlung.
- Wirkung: konstruktive Stimulation.
- Bedeutung: "Das war prozessqualitativ gut."

## `packet_reorganization_need`

- Bereich: `0.0 - 1.0`
- Ebene: Reorganisation / Lernen aus Fehlern
- Funktion: zeigt, ob ein Paket nicht tragfaehig war und einen inneren
  Suchprozess ausloesen soll.
- Wirkung: Reflexion, Beobachtung, Loslassen, Neuordnung.
- Bedeutung: "Ich muss daraus lernen und anders organisieren."

## `constructive_stimulation`

- Bereich: `0.0 - 1.0`
- Ebene: positive Neurochemie
- Funktion: Gesamtwert positiver Stimulation aus tragfaehiger Paketqualitaet.
- Wirkung: spaeter weiche Staerkung von Wachheit, Stabilitaet und Freiheit.
- Bedeutung: "Dieses Paket staerkt mich."

## `constructive_dopamine`

- Bereich: `0.0 - 1.0`
- Ebene: Dopamin / Lernrelevanz
- Funktion: positive Lern- und Wiederholungsneugier bei tragfaehigen Paketen.
- Wirkung: Interesse, Suchrichtung, Motivation.

## `stabilizing_serotonin`

- Bereich: `0.0 - 1.0`
- Ebene: Serotonin / Stabilitaet
- Funktion: Staerkung innerer Ordnung bei guter Innen-Aussen-Passung.
- Wirkung: Selbstvertrauen, Ruhe, Tragfaehigkeit.

## `relief_endorphin`

- Bereich: `0.0 - 1.0`
- Ebene: Endorphin / Entlastung
- Funktion: Entlastung nach guter Prozessleistung oder sauberem Loslassen.
- Wirkung: Druckabbau, Wohlbefinden.

## `focused_acetylcholine`

- Bereich: `0.0 - 1.0`
- Ebene: Acetylcholin / Fokus
- Funktion: markiert, dass eine Wahrnehmungsqualitaet relevant und merkenswert
  ist.
- Wirkung: Fokus und spaetere Wiedererkennung.

---

# Wache Anstrengung / Engaged Effort

## `engaged_effort`

- Bereich: `0.0 - 1.0`
- Ebene: Wachheit / Beteiligung
- Funktion: beschreibt, ob DIO mit tragfaehiger innerer Beteiligung in einer
  Situation steht.
- Wirkung: weich regulierend.
- Bedeutung: "Bin ich wach, beteiligt und tragfaehig genug?"

## `effort_state`

- Bereich: Label
- Ebene: innere Haltung zur Anstrengung
- Funktion: benennt die Qualitaet der aktuellen Beteiligung.
- Wirkung: Diagnose und weiche Meta-Regulation.
- Aktuelle Labels:
  - `settled_effort`
  - `engaged_bearing`
  - `curious_effort`
  - `constructive_echo`
  - `underengaged_reorganize`

## `effort_learning_pull`

- Bereich: `0.0 - 1.0`
- Ebene: Lernzug / Neugier
- Funktion: beschreibt, ob eine Situation eher untersucht und gelernt werden
  soll.
- Wirkung: kann `act_watch`, Beobachtung oder Replan weich staerken.
- Bedeutung: "Das ist lernenswert, aber vielleicht noch nicht handlungsreif."

## `effort_reorganization_pressure`

- Bereich: `0.0 - 1.0`
- Ebene: Reorganisation
- Funktion: beschreibt, ob DIO zwar Reiz/Handlungsdruck erlebt, aber die
  innere Beteiligung und Tragfaehigkeit noch nicht sauber genug sind.
- Wirkung: erhoeht weich Beobachtung, Replan, Hemmung und `act_watch`.
- Bedeutung: "Ich muss mich neu sortieren, bevor ich daraus Handlung mache."

## `pre_action_reorganization_pressure`

- Bereich: `0.0 - 1.0`
- Ebene: Pre-Action-Reflexion
- Funktion: fuehrt Reorganisationsnachhall, schwache Prozessqualitaet,
  Strukturunsicherheit, schwachen Feldsupport und geringe Innen-Aussen-Passung
  vor der Handlung zusammen.
- Wirkung: kann weich `observe`, `act_watch` oder `replan` staerken.
- Bedeutung: "Vor dem Handeln fuehlt sich das noch nicht tragfaehig genug an."

## `pre_action_context_selectivity`

- Bereich: `0.0 - 1.0`
- Ebene: Kontextauswahl
- Funktion: beschreibt, ob aktueller Kontext, Feldsupport, Interpretation,
  Innen-Aussen-Passung und Erfahrung genug gemeinsam tragen.
- Wirkung: schuetzt konstruktive Kontexte vor zu starker Hemmung.
- Bedeutung: "Ist dieser Kontext konzentriert genug fuer Handlung?"

## `previous_packet_label`

- Bereich: Label
- Ebene: Erfahrungsecho
- Funktion: fuehrt die Qualitaet des letzten Erfahrungspakets als Nachhall in
  die aktuelle Meta-Regulation.
- Wirkung: kein harter Memory-Befehl, sondern ein weicher Erfahrungszustand.

## `previous_packet_process_reward`

- Bereich: `0.0 - 1.0`
- Ebene: Prozessnachhall
- Funktion: uebertraegt gute Prozessqualitaet des letzten Pakets in aktuelle
  Wachheit.
- Wirkung: kann `engaged_effort` staerken.

## `previous_packet_reorganization_need`

- Bereich: `0.0 - 1.0`
- Ebene: Reorganisationsnachhall
- Funktion: uebertraegt nicht tragende Paketqualitaet in aktuelle Vorsicht und
  Neuordnung.
- Wirkung: kann `effort_reorganization_pressure` staerken.

---

# Strategische Fensterwahrnehmung / Preisbereich-Hypothesen

## `strategic_window_state`

- Bereich: Dict / Zustandsobjekt
- Ebene: strategische Wahrnehmung
- Funktion: beschreibt die groessere Fensterwahrnehmung von DIO.
- Wirkung: spaeter Grundlage fuer Bereichshypothesen und wartende
  Order-Intentionen.

## `area_focus_candidates`

- Bereich: Liste
- Ebene: Bereichswahrnehmung
- Funktion: enthaelt auffaellige Preisbereiche im betrachteten Fenster.
- Wirkung: Diagnose, spaeter Fokus-/Zoom-Auswahl.

## `area_focus_id`

- Bereich: String
- Ebene: Bereichsidentitaet
- Funktion: benennt den aktuell fokussierten Bereich ohne menschliches Label.

## `lookback_window_size`

- Bereich: Anzahl Kerzen
- Ebene: Arbeitsgedaechtnis / Rueckblick
- Funktion: beschreibt, wie weit DIO aktuell strategisch zurueckschaut.
- Wichtig: begrenzt, damit Vergangenheit nicht unendlich in die Gegenwart
  drueckt.

## `lookback_load`

- Bereich: `0.0 - 1.0`
- Ebene: kognitive Last
- Funktion: beschreibt, wie belastend das groessere Rueckblickfenster fuer
  DIO ist.

## `lookback_bearing_capacity`

- Bereich: `0.0 - 1.0`
- Ebene: strategische Tragfaehigkeit
- Funktion: beschreibt, ob das Rueckblickfenster genug Orientierung traegt,
  ohne DIO zu ueberladen.

## `replay_budget`

- Bereich: `0.0 - 1.0`
- Ebene: innere Simulation
- Funktion: beschreibt, wie viel innere Replay-/Was-waere-wenn-Kapazitaet
  verfuegbar ist.

## `zoom_budget`

- Bereich: `0.0 - 1.0`
- Ebene: fokussierte Wahrnehmung
- Funktion: beschreibt, wie viel Energie fuer genaueres Hineinschauen in
  einen Bereich verfuegbar ist.

## `old_structure_carryover_risk`

- Bereich: `0.0 - 1.0`
- Ebene: Strukturbindung
- Funktion: beschreibt, ob alte Bereichs- oder Regimewahrnehmung noch zu
  stark in die aktuelle Lage hineinragt.

## `area_price_low` / `area_price_high`

- Bereich: Preiswerte
- Ebene: Preisraum
- Funktion: beschreiben die Grenzen eines betrachteten Preisbereichs.

## `area_distance_from_price`

- Bereich: `0.0 - 1.0`
- Ebene: raeumliche Distanz
- Funktion: beschreibt, wie weit der aktuelle Preis vom Bereich entfernt ist.
- Bedeutung: "Liegt dieser Bereich vor mir, hinter mir oder nahe bei mir?"

## `area_structural_density`

- Bereich: `0.0 - 1.0`
- Ebene: Strukturverdichtung
- Funktion: misst, ob in einem Bereich viele relevante Strukturreize
  zusammenfallen.
- Bedeutung: "Hier ist Form verdichtet."

## `area_energy_compression`

- Bereich: `0.0 - 1.0`
- Ebene: Spannung / Kompression
- Funktion: beschreibt, ob Druck/Energie im Bereich komprimiert wirkt.
- Bedeutung: "Hier fuehlt sich Energie gesammelt an."

## `area_mcm_resonance`

- Bereich: `0.0 - 1.0`
- Ebene: MCM-Feld
- Funktion: beschreibt, wie stark ein Bereich im MCM-Feld resoniert.
- Bedeutung: "Dieser Bereich bewegt mein inneres Feld."

## `area_memory_pull`

- Bereich: `0.0 - 1.0`
- Ebene: Erfahrung
- Funktion: beschreibt, ob Memory/Erfahrung diesen Bereich als wiederkehrend
  oder relevant empfindet.

## `area_bearing_quality`

- Bereich: `0.0 - 1.0`
- Ebene: Tragfaehigkeit
- Funktion: bewertet, ob ein Bereich als moeglicher Handlungsraum tragen
  koennte.

## `area_zoom_need`

- Bereich: `0.0 - 1.0`
- Ebene: Aufmerksamkeit
- Funktion: beschreibt, ob DIO in diesen Bereich hineinzoomen sollte.

## `area_zoom_clarity`

- Bereich: `0.0 - 1.0`
- Ebene: fokussierte Sicht
- Funktion: beschreibt, ob ein Bereich nach dem Zoom klarer oder diffuser
  wird.

## `area_replay_fit`

- Bereich: `0.0 - 1.0`
- Ebene: innere Simulation
- Funktion: beschreibt, ob ein Replay / Was-waere-wenn-Durchlauf zu
  Erfahrung und aktueller MCM-Lage passt.

## `area_patience_quality`

- Bereich: `0.0 - 1.0`
- Ebene: strategisches Warten
- Funktion: beschreibt, ob Warten auf diesen Bereich sinnvoller ist als
  sofortiges Handeln.

## `area_order_intention`

- Bereich: `0.0 - 1.0`
- Ebene: Order-Idee
- Funktion: beschreibt, ob aus Bereich, Kontext, Memory und Innenlage eine
  weiche Order-Intention entsteht.
- Wichtig: keine harte Order-Regel.

## `area_invalidity_pressure`

- Bereich: `0.0 - 1.0`
- Ebene: Verwerfen / Loslassen
- Funktion: beschreibt, ob der Bereich seine Bedeutung verliert.

## `strategic_patience`

- Bereich: `0.0 - 1.0`
- Ebene: Geduld
- Funktion: beschreibt, ob DIO eine Bereichsidee halten kann, ohne impulsiv zu
  handeln.

## `strategic_pressure_interpretation`

- Bereich: `0.0 - 1.0`
- Ebene: Druckdeutung
- Funktion: beschreibt, ob DIO Druck als Raum/Information statt als
  Handlungsbefehl lesen kann.

---

# Aktiver MCM-Kontakt / Spiegelung

Diese Variablen beschreiben die geplante aktive Kontaktbahn zwischen
Aussenwahrnehmung und innerer MCM-Lage. Sie sind keine Handelsregeln. Sie
machen sichtbar, wie nah DIO eine Wahrnehmung an das eigene Feld laesst und
ob daraus Resonanz, Ueberkopplung, Distanz oder Vertiefung entsteht.

## `active_mcm_contact_state`

- Bereich: Dict
- Ebene: Wahrnehmung / MCM-Kontakt
- Funktion: gebuendelter Zustand der aktiven Kontakt- und Spiegelbahn.

## `contact_interest`

- Bereich: `0.0 - 1.0`
- Ebene: Aufmerksamkeit / Neugier
- Funktion: beschreibt, ob DIO einen Reiz oder Bereich naeher untersuchen
  moechte.
- Bedeutung: "Das zieht meine Wahrnehmung an."

## `contact_focus_pull`

- Bereich: `0.0 - 1.0`
- Ebene: Fokussteuerung
- Funktion: beschreibt, wie stark ein Wahrnehmungsobjekt Vordergrund werden
  will.

## `contact_resonance_probe`

- Bereich: `0.0 - 1.0`
- Ebene: MCM-Beruehrung
- Funktion: beschreibt die Staerke einer inneren Resonanzpruefung.
- Bedeutung: "Wie reagiert mein Feld, wenn ich diesen Reiz beruehre?"

## `outer_inner_resonance`

- Bereich: `0.0 - 1.0`
- Ebene: Aussen-Innen-Kopplung
- Funktion: beschreibt, ob Aussenform und Innenfeld miteinander schwingen.

## `outer_inner_coherence`

- Bereich: `0.0 - 1.0`
- Ebene: Kohaerenz / Reflexion
- Funktion: beschreibt, ob innere Lage und aeussere Wahrnehmung gemeinsam
  tragfaehig wirken.
- Bedeutung: "Passt mein innerer Zustand noch zu dem, was ich sehe?"

## `inner_change_from_contact`

- Bereich: `0.0 - 1.0`
- Ebene: Interozeption
- Funktion: misst, wie stark sich DIOs Innenlage durch Kontakt mit einem
  Reiz veraendert.

## `contact_carrying_quality`

- Bereich: `0.0 - 1.0`
- Ebene: Tragfaehigkeit
- Funktion: beschreibt, ob der Kontakt mit der Wahrnehmung stabilisierend
  oder tragend wirkt.

## `contact_overcoupling_risk`

- Bereich: `0.0 - 1.0`
- Ebene: Ueberkopplung / Reizbindung
- Funktion: beschreibt, ob eine Wahrnehmung das MCM-Feld zu stark besetzt.
- Bedeutung: "Ich bin zu nah am Reiz."

## `contact_release_readiness`

- Bereich: `0.0 - 1.0`
- Ebene: Loslassen / Distanz
- Funktion: beschreibt, ob DIO einen Reiz nach Betrachtung wieder ablegen
  kann.

## `contact_deepen_pull`

- Bereich: `0.0 - 1.0`
- Ebene: Vertiefung
- Funktion: beschreibt, ob ein Kontakt weitere Untersuchung, Zoom oder
  Objektbildung anzieht.

## `contact_replay_pull`

- Bereich: `0.0 - 1.0`
- Ebene: Replay / innere Simulation
- Funktion: beschreibt, ob ein Kontakt eine innere Was-waere-wenn-Spur
  anregt.

## `contact_curiosity`

- Bereich: `0.0 - 1.0`
- Ebene: Neugier / Lernen
- Funktion: beschreibt lernende, nicht zwingende Annaeherung an eine
  Wahrnehmung.

## `contact_felt_shift`

- Bereich: `-1.0 - 1.0`
- Ebene: innere Verschiebung
- Funktion: beschreibt Richtung und Staerke der gefuehlten Lageveraenderung
  nach Kontakt.

## `contact_selected_depth`

- Bereich: `0.0 - 1.0`
- Ebene: Verarbeitungstiefe
- Funktion: beschreibt, wie tief DIO eine Wahrnehmung aktuell verarbeitet.
- Wichtig: keine feste Tiefe, sondern weiche Selbstregulation.

## `contact_action_maturity`

- Bereich: `0.0 - 1.0`
- Ebene: Kontakt-Reife / Handlungsnaehe
- Funktion: beschreibt, ob ein Kontakt nicht nur spuerbar, sondern fuer eine
  Handlung tragfaehig wirkt.
- Wichtig: Diagnosewert, keine Orderfreigabe.

## `contact_bearing_gap`

- Bereich: `0.0 - 1.0`
- Ebene: Reifespannung
- Funktion: beschreibt die Luecke zwischen Kontakt/Impuls und innerer
  Tragfaehigkeit.
- Bedeutung: "Ich bin nah am Objekt, aber es traegt mich noch nicht genug."

## `contact_impulse_vs_bearing`

- Bereich: `-1.0 - 1.0`
- Ebene: Impuls gegen Tragfaehigkeit
- Funktion: beschreibt, ob Kontaktzug/Neugier/Ordernaehe staerker sind als
  Loslassen, Kohaerenz und Tragfaehigkeit.

## `contact_learning_need`

- Bereich: `0.0 - 1.0`
- Ebene: Lernbedarf / Reifung
- Funktion: beschreibt, ob der Kontakt eher Beobachtung, Replay,
  Distanzierung oder weitere Objektbildung braucht.

## `contact_reality_check`

- Bereich: `0.0 - 1.0`
- Ebene: Realitaetsabgleich
- Funktion: beschreibt, ob Innenkontakt, aeussere Struktur, Loslassen und
  Tragfaehigkeit gemeinsam stimmig wirken.

## `contact_regime_mismatch`

- Bereich: `0.0 - 1.0`
- Ebene: Kontext-/Regime-Reife
- Funktion: beschreibt, ob der Kontakt in eine Weltlage faellt, die nicht
  mehr gut zur bisherigen inneren Stabilitaet passt.
- Bedeutung: "Die Aussenwelt ist fremder, als mein Kontaktgefuehl vermuten
  laesst."

## `contact_stability_carryover`

- Bereich: `0.0 - 1.0`
- Ebene: neurochemischer Nachhall / Kontext
- Funktion: beschreibt, ob Stabilitaet als alter Nachhall in eine veraenderte
  Lage getragen wird.
- Bedeutung: "Ich fuehle noch Stabilitaet, aber sie koennte aus der alten
  Weltlage stammen."

## `contact_context_maturity`

- Bereich: `0.0 - 1.0`
- Ebene: Kontextreife
- Funktion: beschreibt, ob Struktur, Kontext, Transfer und innere Distanz den
  Kontakt gemeinsam tragen.

## `contact_context_reframe_need`

- Bereich: `0.0 - 1.0`
- Ebene: Reframing / Lernen
- Funktion: beschreibt, ob ein Kontakt eher neu gerahmt, beobachtet, gezoomt
  oder replayed werden muss, bevor Handlung daraus reifen kann.

## `contact_posture`

- Bereich: String
- Ebene: innere Haltung
- Funktion: benennt die aktuelle Kontaktlage.
- Moegliche Werte:
  `background_scan`, `curious_touch`, `resonant_contact`,
  `reflective_contact`, `overcoupled_touch`, `release_contact`,
  `deepening_contact`.

---

# Mehrdimensionale Wahrnehmungsachsen / Zeit, Hypothese und Reorganisation

Diese Achsen sind als Ziel- und Diagnosebegriffe aus den MCM-Abhandlungen
Block D bis G.1 abgeleitet. Sie sind noch nicht alle technische Laufzeitwerte.
Sie beschreiben, welche innere Quellenbindung, Moeglichkeitsbildung und
Reorganisation DIO spaeter lesbar machen soll.

Leitidee:
DIO soll eine Wahrnehmung nicht nur als Signal fuehren. Sie bekommt innere
Koordinaten: Zeit, Quelle, Raum, Kontakt, Tragfaehigkeit und
Reorganisation. Dadurch kann DIO unterscheiden, ob etwas aktuell aus der
Aussenwelt wirkt, aus Memory kommt, als Nachhall weiterzieht, als Hypothese
auftaucht oder zu nah an das Handlungszentrum rueckt.

## `perception_source`

- Bereich: String
- Ebene: Quellenbindung
- Funktion: beschreibt, aus welcher Quelle eine Wahrnehmung stammt.
- Moegliche Lagen: `present_world`, `memory`, `learned_knowledge`,
  `afterimage`, `replay`, `hypothesis`, `expectation`.

## `source_temporal_layer`

- Bereich: String
- Ebene: Zeitfeld
- Funktion: ordnet eine Information zeitlich ein: Gegenwart, Nachhall,
  Erinnerung, Wissen, Replay, Hypothese oder Erwartung.

## `present_world_binding`

- Bereich: `0.0 - 1.0`
- Ebene: Realitaetsbindung
- Funktion: beschreibt, wie stark eine Wahrnehmung an aktuelle Aussenwelt
  gebunden ist.

## `memory_reality_distance`

- Bereich: `0.0 - 1.0`
- Ebene: Memory / Realitaetsabstand
- Funktion: beschreibt, ob eine aktivierte Erinnerung als Erinnerung
  erkannt wird oder zu nah an Gegenwart rueckt.

## `perceptual_space_axis`

- Bereich: Dict / String
- Ebene: Wahrnehmungsraum
- Funktion: beschreibt die raeumliche Verortung einer Wahrnehmung im
  inneren Feld.
- Moegliche Lagen: `field_center`, `near_field`, `far_field`,
  `foreground`, `background`, `edge`, `memory_space`, `hypothesis_space`.

## `perceptual_depth`

- Bereich: `0.0 - 1.0`
- Ebene: Tiefenwahrnehmung
- Funktion: beschreibt, ob DIO eine Wahrnehmung flach als Reiz oder tiefer
  als Objekt, Erinnerung, Hypothese oder Kontaktfeld verarbeitet.

## `field_center_distance`

- Bereich: `0.0 - 1.0`
- Ebene: Raumlage / Handlungsnaehe
- Funktion: beschreibt, wie nah eine Wahrnehmung am inneren
  Handlungszentrum liegt.
- Wichtig: Naehe bedeutet nicht automatisch Handlung. Sie zeigt nur, dass
  die Wahrnehmung stark in DIOs aktueller Lage steht.

## `foreground_binding`

- Bereich: `0.0 - 1.0`
- Ebene: Vordergrundbindung
- Funktion: beschreibt, wie stark eine Wahrnehmung den Vordergrund besetzt.

## `background_afterimage`

- Bereich: `0.0 - 1.0`
- Ebene: Hintergrund / Nachhall
- Funktion: beschreibt, ob eine Wahrnehmung noch als Hintergrundspur wirkt,
  obwohl sie nicht mehr aktuelle Aussenwelt ist.

## `hypothesis_branch_state`

- Bereich: Dict / String
- Ebene: Hypothesenraum
- Funktion: beschreibt einen moeglichen Entwicklungszweig, ohne ihn als
  Realitaet zu behandeln.

## `branch_stability`

- Bereich: `0.0 - 1.0`
- Ebene: Hypothesenstabilitaet
- Funktion: beschreibt, ob ein moeglicher Verlauf innerlich stabil,
  fragil oder widerspruechlich wirkt.

## `branch_attractor_pull`

- Bereich: `0.0 - 1.0`
- Ebene: Attraktor / Zukunftsmoeglichkeit
- Funktion: beschreibt, wie stark ein moeglicher Verlauf die innere
  Erwartung anzieht.
- Wichtig: hoher Wert ist kein Zukunftsbeweis, sondern nur eine
  Moeglichkeitskraft.

## `hypothesis_reality_gap`

- Bereich: `0.0 - 1.0`
- Ebene: Realitaetsabgleich
- Funktion: beschreibt die Luecke zwischen innerer Hypothese und aktueller
  Aussenwelt.

## `field_reorganization_state`

- Bereich: String
- Ebene: Reorganisation
- Funktion: beschreibt, ob ein verdichteter Zustand nur belastet oder
  bereits in eine neue Ordnung ueberfuehrt wird.

## `reorganization_threshold`

- Bereich: `0.0 - 1.0`
- Ebene: Reorganisationsschwelle
- Funktion: beschreibt, ob lokale Verdichtung so hoch ist, dass die bisherige
  Ordnung nicht mehr ausreichend traegt.

## `higher_order_coupling`

- Bereich: `0.0 - 1.0`
- Ebene: uebergeordnete Feldkopplung
- Funktion: beschreibt, ob DIO eine Lage nicht lokal erzwingt, sondern in
  einen breiteren Ordnungszusammenhang ueberfuehrt.

---

# Noch Zu Dokumentieren

- `nervous_variance`
- `regulation_oscillation`
- `recovery_after_stress`
- `stress_to_recovery_delta`
- terrain/path-texture-Sense, falls umgesetzt
