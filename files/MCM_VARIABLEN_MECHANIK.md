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

---

# Noch Zu Dokumentieren

- `nervous_variance`
- `regulation_oscillation`
- `recovery_after_stress`
- `stress_to_recovery_delta`
- terrain/path-texture-Sense, falls umgesetzt
