# Umsetzungsplan (offen) – Ebenen-Trennung, MCM-Zustandsraum, Selbstregulation

Dieses Dokument enthält **nur noch offene Punkte**.
Bereits umgesetzte Basisbausteine wurden entfernt.

---

WICHTIG !

# --------------------------------------------------
# Leitbild
# --------------------------------------------------

## Ziel der offenen Erweiterung

Ziel ist ein System, das einem menschlichen Trader strukturell näher kommt.

Es gibt dabei drei klar getrennte Ebenen:

- **Ebene 1** = äußeres Wahrnehmen
- **Ebene 2** = inneres Wahrnehmen / Denken / Handeln
- **Ebene 3** = Entwicklung aus Erfahrung / Selbstregulation

Handlung ist dabei **nicht** der Mittelpunkt.
Handlung ist nur ein möglicher Ausdruck des aktuellen Innenzustands.

Der Bot soll nicht lernen, permanent weiter zu versuchen.
Der Bot soll lernen, **handlungsfähig zu bleiben**.

Das zentrale Ziel ist daher:

- regulatorisches Gleichgewicht halten
- Überlebensfähigkeit im Markt erhalten
- Profitabilität als Existenzgrundlage abbilden
- Beobachtung / Pause / Sammlung als wertvolle Reaktion lernen
- Druck nach Fehlphasen abbauen statt weiter zu eskalieren
- gezielter und tragfähiger mit Erfahrungswerten und Umgebung interagieren

---

# --------------------------------------------------
# Ebene 1
# --------------------------------------------------

## Äußeres Wahrnehmen

### Aufgabe

- OHLCV lesen
- Workspace / Buffer pflegen
- reine Marktinformationen berechnen:
  - Candle-State
  - Energy
  - Coherence
  - Asymmetry
  - HH
  - LL
  - Struktur
- neutrales Stimulus-/Informationspaket erzeugen
- niemals denken
- niemals entscheiden
- niemals Memory ändern
- niemals Order / Pending / Position anfassen

### Gehört dahin

- `runner.py` Feed-/Polling-Ablauf
- `csv_feed.py` / `ph_ohlcv.py` / `workspace.py` Datenpfad
- `mcm_core_engine.py` Spannungs-/Chartinfos wie Energy / Coherence / Asymmetry
- `strukture_engine.py` reine Struktur-Wahrnehmung ohne Handelsfreigabe

### Output von Ebene 1

Nur ein neutrales Paket, zum Beispiel:

- `timestamp`
- `window_ref` oder `window_snapshot`
- `candle_state`
- `tension_state`
- `structure_perception_state`

---

# --------------------------------------------------
# Ebene 2
# --------------------------------------------------

## Inneres Wahrnehmen / Denken / Handeln

### Aufgabe

- Stimulus von Ebene 1 konsumieren
- Runtime permanent fortschreiben
- Wahrnehmung / Verarbeitung / Gefühl / Denken / Meta / Erwartung bilden
- MCM-Raum fortschreiben
- Zustandsbild des MCM-Raums sichtbar halten
- Entscheidungstendenz bilden:
  - `act`
  - `observe`
  - `hold`
  - `replan`
- danach technische Handlung ausführen:
  - Pending
  - Entry
  - Position
  - Exit

### Gehört dahin

- `MCMBrainRuntime` und Runtime-Fortschreibung in `MCM_Brain_Modell.py`
- Entscheidungsbahn `build_runtime_decision_tendency(...)` / `decide_mcm_brain_entry(...)`
- Handlungsbahn in `bot.py`:
  - `_handle_active_position(...)`
  - `_handle_pending_entry(...)`
  - `_handle_entry_attempt(...)`

---

# --------------------------------------------------
# Ebene 3
# --------------------------------------------------

## Entwicklung aus Erfahrung / Selbstregulation

### Aufgabe

- Experience / Episode / Review / Memory pflegen
- Nicht-Handlung als echte Erfahrung speichern
- Fehlphasen als regulatorische Information verwerten
- Beobachtung / Sammlung / Pause als entlastende Erfahrung bewerten
- tragfähige Handlung von hektischer Handlung unterscheiden lernen
- langfristig verändern, wie Ebene 2 künftig wahrnimmt, verarbeitet und reguliert

### Gehört dahin

- Episoden-/Erfahrungsraum / Review / Memory in `MCM_Brain_Modell.py`
- Persistenz und Zustandsspeicherung in `memory_state.py`
- KPI-/Nachweis-Pfad in `trade_stats.py`

---

# --------------------------------------------------
# Harte Regel der Trennung
# --------------------------------------------------

## Grundregeln

- Ebene 1 liest Markt und erzeugt nur Wahrnehmungspakete.
- Ebene 2 konsumiert diese Pakete und bildet daraus Innenzustände.
- Ebene 3 bewertet Erfahrung und verändert langfristig die Innenbahn.
- Handlung darf nur noch aus Ebene 2 kommen.
- Ebene 1 kennt keine Orderlogik.
- Ebene 1 schreibt niemals Innenzustände.

### Ebene 1 schreibt nie

- `mcm_runtime_snapshot`
- `mcm_runtime_decision_state`
- `mcm_runtime_brain_snapshot`
- `mcm_decision_episode`
- `mcm_decision_episode_internal`
- `mcm_experience_space`
- `position`
- `pending_entry`

### Ebene 2 liest Chartdaten nur als Input

- keine eigene OHLCV-Beschaffung
- keine Vermischung mit Feed-Logik
- keine implizite Rückverlagerung von Handlungslogik in Ebene 1

---

# --------------------------------------------------
# Was dafür konkret weg muss
# --------------------------------------------------

## Noch offene strukturelle Altmischung

- `runner.py` darf nicht mehr direkt Logik + Brain + Handlung in einem Ablauf treiben.
- `bot._process_window(...)` darf nicht dauerhaft die breite Mischstelle bleiben.
- `step_mcm_runtime_idle(...)` darf nicht vom Chartpfad als Ersatz für den Innenprozess benutzt werden, sondern muss vollständig in den permanenten Innenloop von Ebene 2 gehören.

---

# --------------------------------------------------
# MCM-Basis des Zustandsraums
# --------------------------------------------------

## Fachliche Grundlage

Der Zustandsraum bleibt auf der **Mental Core Matrix** aufgebaut.

Neue Zustandsgrößen dürfen **nicht** als fremde starre Zusatzlogik neben das System gesetzt werden.
Sie müssen aus dem MCM-Raum selbst abgeleitet werden.

Das bedeutet:

- Zentrum
- Abweichung
- Varianz
- Rückführung

bleiben die Grundstruktur.

Darauf aufbauend wird der Raum lesbarer gemacht.

### Ziel

Nicht MCM ersetzen,
sondern den **laufenden MCM-Raum explizit als Zustandswiedergabe sichtbar machen**.

---

# --------------------------------------------------
# Phase A – MCM-Zustandswiedergabe des gesamten Raums
# --------------------------------------------------

## Ziel

Der Nettozustand des MCM-Feldes muss als eigene Größe sichtbar und nutzbar werden.

## Offene Umsetzungspunkte

- Feldverdichtung / Felddichte als eigene Ableitung aus dem MCM-Raum einführen.
- Nicht nur lokale Teilsignale, sondern Gesamtzustand des Feldes zusammenführen.
- Zustandsachsen aus dem MCM-Raum ableiten, z. B.:
  - `field_density`
  - `field_stability`
  - `regulatory_load`
  - `action_capacity`
  - `recovery_need`
- Nettozustand des MCM-Raums als explizite Zustandswiedergabe in Snapshots aufnehmen.
- Snapshot-/Debug-/GUI-Ausgabe für diese Größen ergänzen.
- Sicherstellen, dass diese Größen **aus dem MCM-Raum** kommen und nicht aus harten Handelsregeln.

## Ergebnis

Der Bot besitzt eine explizite Lesbarkeit seines gesamten Innenraums,
nicht nur einzelner Teilwerte.

---

# --------------------------------------------------
# Phase B – Permanenter Innenprozess
# --------------------------------------------------

## Ziel

Das Gehirn darf nicht nur beim Candle-Schritt aufgerufen werden.
Denken und innere Fortschreibung sollen als eigener permanenter Prozess laufen.

## Offene Umsetzungspunkte

- `MCMBrainRuntime` als dauerhafte Laufzeitschicht weiter vervollständigen.
- Reizübergabe entkoppeln:
  - Marktdatenpfad erzeugt nur Stimulus-/Perception-Impulse
  - Innenprozess konsumiert Impulse unabhängig vom Orderpfad
- Zustandsfortschreibung in kleinen Ticks statt nur einmal pro Marktfenster
- aktuellen Brain-Snapshot separat bereitstellen:
  - lesbar für Entscheidungsbahn
  - lesbar für GUI/Debug
  - schreibgeschützt außerhalb der Brain-Runtime
- Backtest und Live auf dasselbe Laufzeitmodell bringen:
  - Backtest = deterministische Tick-Fortschreibung
  - Live = permanenter Innenloop + technische Monitor-Threads

## Ergebnis

Außenreiz und innere Verarbeitung sind zeitlich entkoppelt.
Das Gehirn läuft kontinuierlich, nicht nur als Funktionsaufruf im Candle-Loop.

---

# --------------------------------------------------
# Phase C – Selbstregulation als eigentliches Lernziel
# --------------------------------------------------

## Ziel

Lernen bedeutet nicht nur, Outcomes zu speichern.
Lernen bedeutet, den eigenen inneren Zustand regulatorisch tragfähig zu halten.

## Offene Umsetzungspunkte

- Selbstregulation als zentrale Lernrichtung im Erfahrungsraum verankern.
- Fehlphasen nicht nur als Trade-Misserfolg, sondern als Überlastungsinformation behandeln.
- Beobachtung / Sammlung / Pause als entlastende und sinnvolle Reaktion bewerten.
- Handlung nicht nur nach Erfolgsquote, sondern nach regulatorischer Tragfähigkeit bewerten.
- Bewertung ergänzen für:
  - hektische Handlung
  - tragfähige Handlung
  - korrektes Nicht-Handeln
  - regulatorische Erholung
- Outcome-Decomposition und Review stärker an Selbstregulation koppeln.

## Ergebnis

Der Bot lernt nicht nur, was TP oder SL war,
sondern ob sein innerer Zustand tragfähig oder überlastet war.

---

# --------------------------------------------------
# Phase D – Überlebensdruck / Profitabilität als innere Zielspannung
# --------------------------------------------------

## Ziel

Profitabilität wird nicht als starre Regel,
sondern als Existenzgrundlage des Systems abgebildet.

## Offene Umsetzungspunkte

- PnL / Drawdown / Verlustserie als Innenreiz an den MCM-Raum koppeln.
- `survival_pressure` oder äquivalente Größe als laufenden Zustand ergänzen.
- Verluste als Belastung der Existenzbasis interpretieren.
- Gewonnene Stabilität und positive Outcomes als Entlastung interpretieren.
- Handlungsdrang bei hoher Existenzbelastung natürlicherweise dämpfen.
- Erholung und wiedergewonnene Stabilität natürlicherweise zu neuer Handlungsfähigkeit führen.
- Keine harte Regel wie `wenn pnl < x dann stop`.
- Stattdessen: Überlebensdruck als systemischer Reiz,
der Beobachtung, Sammlung und Schutzbreite attraktiver macht.

## Ergebnis

Profitabilität wird zur inneren Zielspannung des Systems,
nicht zu einem starren externen Schalter.

---

# --------------------------------------------------
# Phase E – Beobachtung / Pause / Sammlung als echte Zustandsbahn
# --------------------------------------------------

## Ziel

Wird der Druck zu hoch,
soll der Bot nicht einfach weiter probieren,
sondern ausharren, beobachten, verstehen und sich wieder sammeln.

## Offene Umsetzungspunkte

- Pause nicht nur als technisches Nach-SL-Verhalten,
  sondern als allgemeine regulatorische Zustandsbahn ausbauen.
- Beobachtung als aktiv wertvolle Reaktion modellieren.
- Druckabbau über Zeit, Ruhe und stabile Wahrnehmung fortschreiben.
- Wiederanlaufen von Handlung an zurückgewonnene Handlungsfähigkeit koppeln.
- `observe`, `hold` und `replan` als echte Regenerations- und Reifungszustände vertiefen.
- Review bewerten lassen, ob Nicht-Handlung in der Situation besser war als Aktion.

## Ergebnis

Nicht-Handlung wird kein leerer Zustand,
sondern ein echter Teil der Reifung und Selbstregulation.

---

# --------------------------------------------------
# Phase F – Harte Bahntrennung in der Runtime vervollständigen
# --------------------------------------------------

## Ziel

Die vorhandene Zustandskette soll auch architektonisch vollständig getrennt werden.

## Offene Umsetzungspunkte

- Wahrnehmungsbahn festziehen:
  - nur Markt-/Struktur-/Kontextimpulse
  - keine Orderfreigabe
- Innenbahn festziehen:
  - verarbeitet Impulse
  - pflegt Feld, Regulation, Drift, Konflikt, Reife, Unsicherheit
  - erzeugt nur Zustandsfortschreibung
- Entscheidungsbahn abtrennen:
  - liest Brain-Snapshot
  - erzeugt nur Entscheidungstendenz: `act`, `observe`, `hold`, `replan`
- Handlungsbahn abtrennen:
  - Pending / Entry / Position / Exit technisch ausführen
  - keine direkte Feldmutation
- In-Trade-Beobachtungsbahn ergänzen:
  - läuft während `pending_entry` und `position`
  - blockiert nicht durch Exit-/Ordertechnik

## Ergebnis

Wahrnehmung, Innenverarbeitung, Entscheidung und technische Handlung sind nicht mehr ineinander verschachtelt.

---

# --------------------------------------------------
# Phase G – Entscheidungsepisode als zentrales Lernobjekt
# --------------------------------------------------

## Ziel

Nicht der einzelne Trade allein,
sondern die gesamte Entscheidungsepisode soll das zentrale Lernobjekt sein.

## Offene Umsetzungspunkte

- Episode klar als vollständigen Verlauf behandeln:
  - äußerer Reiz
  - Innenzustand
  - Entscheidungstendenz
  - Handlung oder Nicht-Handlung
  - In-Trade-Verlauf
  - Outcome
  - Review
- Nicht-Handlung vollständig in Episodenlogik aufnehmen.
- Bewertungsachsen ausbauen für:
  - regulatorische Tragfähigkeit
  - Entscheidungsreife
  - Unsicherheitsverarbeitung
  - Beobachtungsqualität
  - Korrekturqualität
- Episoden stärker als Lernträger im Experience-Space verankern.

## Ergebnis

Das System lernt aus ganzen inneren Entscheidungsverläufen,
nicht nur aus TP/SL-Endpunkten.

---

# --------------------------------------------------
# Phase H – In-Trade-Beobachtung und laufende Innenveränderung vertiefen
# --------------------------------------------------

## Ziel

Auch während Pending und Position soll der Innenprozess weiterlaufen und lernen.

## Offene Umsetzungspunkte

- Pending-Phase als eigene Beobachtungs- und Bewertungsphase vertiefen.
- Positionsphase als fortlaufende Innenbeobachtung ausbauen.
- In-Trade-Verlauf auf Druck, Stabilität, Drift, Unsicherheit und Tragfähigkeit abbilden.
- In-Trade-Ereignisse stärker in Review und Experience-Space einbeziehen.
- prüfen, wie sich laufende Marktveränderungen auf inneren Zustand und spätere Reifung auswirken.

## Ergebnis

Der Bot bleibt auch während eines laufenden Handels ein wahrnehmendes und lernendes System.

---

# --------------------------------------------------
# Phase I – Messbarkeit und Nachweis der offenen Architektur ergänzen
# --------------------------------------------------

## Ziel

Die neue Architektur muss nach außen nachvollziehbar werden.

## Offene Umsetzungspunkte

- KPI-/Nachweis-Ebene für neue Zustände ergänzen:
  - Felddichte
  - regulatorische Last
  - Überlebensdruck
  - Handlungsfähigkeit
  - Erholungsbedarf
  - Beobachtungsanteil
  - Pause-/Sammlungsanteil
- GUI-/Debug-Ausgabe für diese Zustände ergänzen.
- Teststand für neue Zustandsachsen ergänzen.
- dedizierte Tests ergänzen für:
  - `bot_gate_funktions.py`
  - `mcm_core_engine.py`
  - neue MCM-Gesamtzustandsachsen
  - regulatorische Pausen-/Beobachtungsdynamik

## Ergebnis

Der offene Architekturfortschritt ist nicht nur konzeptionell,
sondern auch messbar und testbar sichtbar.

---

# --------------------------------------------------
# Kompakte Zieldefinition
# --------------------------------------------------

Die MCM-KI soll als System mit getrennter Außenwelt-, Innenwelt- und Entwicklungsebene aufgebaut werden.

Der Markt liefert nur Reize.
Die Innenwelt verarbeitet diese Reize permanent weiter und bildet eine explizite Zustandswiedergabe des gesamten MCM-Raums.

Diese Zustandswiedergabe enthält insbesondere:

- Feldverdichtung
- regulatorische Last
- Überlebensdruck
- aktuelle Handlungsfähigkeit
- Erholungsbedarf

Lernen bedeutet, unter Druck nicht einfach weiter zu handeln,
sondern regulatorisch tragfähig zu bleiben.

Profitabilität wird als Existenzgrundlage des Systems als innere Zielspannung geführt.

Beobachtung, Sammlung, Pause und korrektes Nicht-Handeln werden als echte Erfahrung und als Teil der Reifung behandelt.

Neue Zustandswerte entstehen nicht als fremde starre Zusatzlogik,
sondern als explizite Lesbarkeit des laufenden Mental-Core-Matrix-Raums.
