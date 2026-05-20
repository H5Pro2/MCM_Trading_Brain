# MD_ANWEISUNG

Ziel dieser Datei:
- klare Funktion jeder Markdown-Datei festlegen
- Dopplungen vermeiden
- verhindern, dass Gesprächsnotizen technische Dokumentation aufblähen
- festlegen, wo Laufanalysen, Fixes, Mechaniken und Architektur hingehören

Grundsatz:
Jede Information hat genau einen Hauptort.
Andere Dateien dürfen darauf verweisen, aber nicht dieselbe Auswertung oder
dieselbe Erklärung erneut ausformulieren.

---

# 1. UMSETZUNGSPLAN.md

Status:
- heiliger Bauplan
- nur mit ausdrücklicher Zustimmung des Nutzers aendern

Aufgabe:
- Zielarchitektur
- Systemphilosophie
- erlaubte und verbotene Entwicklungsrichtungen
- große Mechanikbloecke
- langfristige Ausbaustufen

Darf enthalten:
- Grundprinzipien der MCM
- Zielmechaniken
- wichtige Architekturentscheidungen
- Begruendungen, warum eine Mechanik existiert
- technische Zielachsen, wenn sie zur Systemmechanik gehören

Darf nicht enthalten:
- detaillierte einzelne Laufanalysen
- Tagesprotokolle
- kleine Bugfix-Historie
- Rohdaten aus Debug-Läufen
- doppelte Kopien aus `AKTUELLER_STAND.md`

Regel:
Der Umsetzungsplan beschreibt, **wohin** das System soll.
Er beschreibt nicht jeden Schritt, der bereits passiert ist.

---

# 2. README.md

Status:
- fachlicher Einstieg für Menschen

Aufgabe:
- Projekt verständlich erklären
- MCM-Gedanken fachlich sauber einordnen
- zentrale Begriffe einführen
- Leser orientieren, ohne jede Mechanik voll auszuformulieren

Darf enthalten:
- kurze Projektbeschreibung
- wichtigste Konzepte
- grobe Architektur
- Hinweise auf relevante Dateien
- kompakte Beispiele zum Verstehen

Darf nicht enthalten:
- lange Forschungsgespraeche
- komplette Laufhistorie
- offene To-do-Details
- tiefe Variablenlisten
- Wiederholung des ganzen Umsetzungsplans

Regel:
README ist Einstieg und Orientierung, nicht Forschungslog.

---

# 3. WICHTIG_MECHANIKEN.md

Status:
- technische Mechanik-Schatzkammer
- kein Gespraechsarchiv

Aufgabe:
- wichtige Mechaniken technisch verdichten
- alte Denkspuren bereinigt in brauchbare Mechanikform bringen
- erklären, wie Mechaniken funktionieren
- nur dauerhaft relevante Konzepte behalten

Darf enthalten:
- technische Mechanikbeschreibung
- Eingangs-/Ausgangswerte
- Wirkweise
- Abgrenzung gegen harte Regeln
- Hinweise auf Codebereiche
- kurze Beispiele, wenn sie das technische Verstehen verbessern

Darf nicht enthalten:
- Unterhaltungstext
- persoenliche Reflexionen
- lange philosophische Prosa
- Laufberichte
- doppelte Fixlistenpunkte
- historische Aussagen, die inzwischen technisch überholt sind, ohne klare
  Kennzeichnung

Regel:
Wenn eine Idee aus dem Gespraech wichtig ist, wird sie hier **technisch
übersetzt**, nicht wortnah archiviert.

---

# 4. MCM_VARIABLEN_MECHANIK.md

Status:
- Variablen- und Zustandslexikon

Aufgabe:
- zentrale Variablen benennen
- Wertebereich, Ebene, Funktion und Wirkung klären
- verhindern, dass Variablen als harte Trading-Regeln missverstanden werden

Darf enthalten:
- Variablenname
- Wertebereich
- Ebene
- Funktion
- Wirkung
- kurze Bedeutung in einem Satz
- nahe verwandte Variablen, wenn noetig

Darf nicht enthalten:
- Laufanalysen
- lange Architekturprosa
- Aufgabenlisten
- komplette Konzeptdiskussionen

Regel:
Diese Datei beantwortet:
"Was bedeutet diese Variable technisch?"

---

# 4b. MCM_REZEPTOR_MATRIX.md

Status:
- Wirkpfad- und Rezeptorübersicht

Aufgabe:
- Variablen nach Rezeptorfamilie und Zielregler einordnen
- organisch erlaubte Überlappung von stoerender Doppelwirkung trennen
- sichtbar machen, ob Signale diagnostisch, weich regulierend oder
  persistent lernend wirken
- verhindern, dass dieselbe Last mehrfach auf denselben Zielregler drückt

Darf enthalten:
- Rezeptorfamilien
- Zielregler
- Speicherpfade
- prüfpflichtige Kaskaden
- Arbeitsregeln für neue Variablen

Darf nicht enthalten:
- Laufanalysen
- philosophische Langtexte
- komplette Variablenlexika
- Fix-Historie

Regel:
Diese Datei beantwortet:
"Wirkt diese Variable auf einen eigenen Rezeptor oder doppelt auf denselben
Regler?"

---

# 5. AKTUELLER_STAND.md

Status:
- aktueller Ist-Zustand des Projekts

Aufgabe:
- realen Codezustand zusammenfassen
- wichtigste aktuelle Debug-Erkenntnisse festhalten
- aktuelle Engpässe und nächste Prüfpunkte benennen

Darf enthalten:
- zuletzt relevante Laufzusammenfassung
- kompakte Tabellen oder Stichpunkte zu den wichtigsten Runs
- aktuelle technische Ist-Mechaniken
- bekannte Risiken
- nächste sinnvolle Prüfpunkte

Darf nicht enthalten:
- jede einzelne alte Laufanalyse voll ausgeschrieben
- lange Wiederholungen aus `FIX_LISTE.md`
- lange Wiederholungen aus `UMSETZUNGSPLAN.md`
- Gespraechsprosa
- technische Variablenlexika

Regel:
`AKTUELLER_STAND.md` beschreibt:
"Was ist jetzt real und was wissen wir aktuell?"

Laufregel:
- Nur die letzten oder fachlich wichtigsten Läufe ausfuehrlich.
- Aeltere Läufe werden zu einer kurzen Vergleichstabelle verdichtet oder
  ausgelagert.
- Keine komplette Wiederholung in der Fixliste.

---

# 6. FIX_LISTE.md

Status:
- aktive Arbeitsliste

Aufgabe:
- offene Aufgaben
- nächste konkrete Prüfpunkte
- kurze Statusmarkierung

Darf enthalten:
- Checkboxen
- kurze Zielbeschreibung
- maximal 2-4 kurze Befundzeilen pro Punkt
- Verweis auf `AKTUELLER_STAND.md`, wenn Details noetig sind

Darf nicht enthalten:
- lange Laufanalysen
- Ergebnisberichte mit vielen Zahlen
- Forschungsprosa
- Mechanikerlaeuterungen
- erledigte Altaufgaben über lange Zeit

Regel:
`FIX_LISTE.md` beantwortet:
"Was ist als nächstes zu tun?"

Erledigte Punkte:
- nur kurz behalten
- später nach `FIX_LISTE_ARCHIV.md` verschieben oder entfernen

---

# 7. FIX_LISTE_ARCHIV.md

Status:
- Archiv erledigter oder alter Fixpunkte

Aufgabe:
- alte Fixpunkte auslagern
- Verlauf nachvollziehbar halten, ohne die aktive Fixliste aufzublaehen

Darf enthalten:
- abgeschlossene Fixpunkte
- kurze Ergebnisnotizen
- alte To-dos, die historisch relevant sind

Darf nicht enthalten:
- neue aktive Aufgaben
- aktuelle Prioritäten

---

# 8. GUI_KONSTRUKTION.md

Status:
- Konzeptdatei für spätere Web-Oberflaeche

Aufgabe:
- GUI-Idee technisch und gestalterisch sammeln
- Beobachtungsfenster für MCM, neuronale Aktivität, Außenwahrnehmung und
  Neurochemie beschreiben
- verhindern, dass GUI-Ideen in Brain-/Fix-Dateien verstreut werden

Darf enthalten:
- Panel-/Fensterkonzepte
- Datenquellen
- Darstellungsprinzipien
- technische Richtung für spätere Umsetzung
- Abgrenzung gegen überladene Variablenoberflaechen

Darf nicht enthalten:
- aktive Brain-Fixpunkte
- Laufanalysen
- komplette Variablenlexika
- harte Trading-Regeln

Regel:
Die GUI ist Beobachtungsraum, nicht Entscheidungsmechanik.

---

# 9. Laufanalysen / Debug-Läufe

Grundregel:
Laufanalysen gehören primaer in `AKTUELLER_STAND.md`, aber nur kompakt.

Empfohlene Struktur:

- Laufnummer
- Datensatz
- Memory-Status
- Trades / TP / SL
- Netto-PnL / Profit Factor / Drawdown, falls vorhanden
- wichtigste MCM-/Brain-Erkenntnis
- konkrete Folgefrage

Nicht erlaubt:
- dieselbe Laufanalyse in `FIX_LISTE.md` erneut ausschreiben
- lange psychologische Deutung in mehreren Dateien doppeln

Optionaler späterer Ausbau:
- `LAUF_ANALYSEN.md` oder `DEBUG_LAUF_ARCHIV.md`
  für historische Laufdetails, wenn `AKTUELLER_STAND.md` zu groß wird.

---

# 10. Gespraechsideen in technische Form bringen

Wenn im Gespraech eine wichtige Idee entsteht:

1. Prüfen:
   Gehört sie in den Umsetzungsplan?
   Falls ja, nur mit Zustimmung.

2. Technisch übersetzen:
   Keine langen Zitate, sondern:
   - Mechanikname
   - Zweck
   - beteiligte Variablen
   - Wirkung
   - Abgrenzung gegen harte Regeln

3. Zielort wählen:
   - Architekturziel: `UMSETZUNGSPLAN.md`
   - technische Mechanik: `WICHTIG_MECHANIKEN.md`
   - Variable: `MCM_VARIABLEN_MECHANIK.md`
   - Ist-Zustand: `AKTUELLER_STAND.md`
   - Aufgabe: `FIX_LISTE.md`

Regel:
Die Unterhaltung ist Quelle.
Die Markdown-Dateien sind technische Verdichtung.

---

# 11. Konkrete Aufraeumregel ab jetzt

Ab jetzt gilt:

- keine komplette Laufanalyse mehr in `FIX_LISTE.md`
- `AKTUELLER_STAND.md` nur noch mit kompakten aktuellen Befunden
- `WICHTIG_MECHANIKEN.md` wird von Gespraechsprosa bereinigt
- `MCM_VARIABLEN_MECHANIK.md` bleibt lexikalisch
- `README.md` bleibt Einstieg
- `UMSETZUNGSPLAN.md` bleibt Bauplan

Nächster sinnvoller Aufraeumschritt:
`FIX_LISTE.md` auf aktive Punkte reduzieren und alte erledigte Punkte nach
`FIX_LISTE_ARCHIV.md` verschieben.
