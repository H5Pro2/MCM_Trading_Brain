# aktueller_stand.md

# --------------------------------------------------
# Beobachtung
# --------------------------------------------------

## Projektstatus gesamt

- Die frühere Fix-Basis ist weitgehend umgesetzt.
- Der aktuelle Schwerpunkt liegt nicht mehr auf Basis-Fixes, sondern auf dem offenen Architektur-Endausbau.
- Die Zielarchitektur ist jetzt fachlich als **3 Ebenen** geschärft:
  - Ebene 1 = sehen / äußeres Wahrnehmen
  - Ebene 2 = denken / inneres Wahrnehmen / Handeln
  - Ebene 3 = Entwicklung aus Erfahrung / Verarbeitung / Wahrnehmung
- Thread-Trennung ist als Zielbild dokumentiert und im Runtime-Pfad bereits teilweise umgesetzt.

## Bereits umgesetzt

### Lern- und Persistenzbasis

- Entry ist nicht mehr der zentrale Lernschreibpunkt.
- Outcome ist der zentrale Commit-Punkt für Signature-/Context-Lernen.
- Attempt-/Outcome-Logging ist getrennt aufgebaut.
- `trade_stats.json` bleibt Aggregat-Datei.
- Attempt-Details laufen in `attempt_records.jsonl`.
- Outcome-Details laufen in `outcome_records.jsonl`.

### Runtime / Performance

- Runtime-Thread-Modell ist vorhanden.
- Marktfenster werden an die Runtime publiziert.
- Runtime-Ticks wurden reduziert.
- Idle-Last wurde reduziert.
- Dirty-/Cooldown-Save für Memory-State ist eingeführt.
- Runtime-State ist beim Persistenz-Save optional.
- Debug-Dateischreiben ist gedrosselt.

### MCM-Rechenkern

- Feldkopplung wurde von voller NxN-Kopplung auf lokale Nachbarschaft reduziert.
- Cluster-Erkennung läuft nicht mehr zwingend bei jedem Tick.
- Outcome-Ticks können Cluster weiter sofort erzwingen.
- Interne MCM-Zyklen sind bereits reduziert.

### Zustandsbahn / Datenbahn

- Soft-Perception für Struktur ist vorhanden.
- Zustandsketten für Wahrnehmung / Verarbeitung / Gefühl / Denken / Meta / Erwartung sind vorhanden.
- Runtime-Snapshots / Decision-State / Brain-Snapshot / Experience-Space sind angelegt.
- Outcome-Decomposition und Experience-Rückkopplung sind vorhanden.
- `bot_gate_funktions.py` gibt weiter die vollständige Zustandsbahn für Handlung und Nicht-Handlung zurück.
- `MCM_Brain_Modell.py` enthält bereits Runtime-, Episoden- und Experience-Blöcke inklusive `similarity_axes`, `axis_shift` und `in_trade_updates`.

### Zielarchitektur / Dokumentation

- `README.md` und `UMSETZUNGSPLAN.md` führen die Basis nicht mehr als offenen Altblock, sondern den offenen Erweiterungsstand.
- Die Zielarchitektur wurde auf die 3 Ebenen präzisiert:
  - äußeres Wahrnehmen
  - inneres Wahrnehmen / Denken / Handeln
  - Entwicklungsebene
- Das Zusammenspiel der Mechanik ist damit fachlich klarer gefasst:
  - Thread 1 liefert nur äußere Wahrnehmung
  - Thread 2 verarbeitet, denkt und handelt
  - Ebene 3 bewertet Episoden und verändert langfristig die Innenbahn

## Aktuell noch offen

### Architektur-Endausbau

- permanenter Innenprozess vollständig zu Ende ziehen
- harte Bahntrennung in der Runtime weiter vervollständigen
- Entscheidungsepisode als zentrales Lernobjekt vollständig ausbauen
- internen Erfahrungsraum weiter ausbauen
- Nicht-Handlung als echtes Lernobjekt weiter vertiefen
- In-Trade-Beobachtung / In-Trade-Lernen weiter ausbauen
- neue KPI-/Nachweis-Ebene für die offenen Architekturphasen ergänzen

### Zielbild der 3 Ebenen weiter verhärten

#### Ebene 1 = sehen / äußeres Wahrnehmen

- OHLCV lesen
- Workspace / Buffer pflegen
- Candle-State / Energy / Coherence / Asymmetry / HH / LL / Struktur berechnen
- nur neutrales Stimulus-/Informationspaket erzeugen
- niemals denken
- niemals entscheiden
- niemals Memory ändern
- niemals Order / Pending / Position anfassen

#### Ebene 2 = denken / inneres Wahrnehmen / Handeln

- Stimulus von Ebene 1 konsumieren
- Runtime permanent fortschreiben
- Wahrnehmung / Verarbeitung / Gefühl / Denken / Meta / Erwartung bilden
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

#### Ebene 3 = Entwicklung aus Erfahrung / Verarbeitung / Wahrnehmung

- Experience / Episode / Review / Memory pflegen
- Nicht nur Outcome speichern, sondern auch Wahrnehmung und Denkverlauf bewerten
- langfristig verändern, wie Ebene 2 künftig wahrnimmt, verarbeitet und reguliert

### Teststand offen

- dedizierte Tests für `bot_gate_funktions.py`
- dedizierte Tests für `mcm_core_engine.py`

# --------------------------------------------------
# Interpretation
# --------------------------------------------------

## Was der aktuelle Stand bedeutet

- Das Projekt ist nicht mehr in einem frühen Fix-Zustand.
- Die Basis für Lernen, Persistenz, Runtime und Performance steht.
- Die offene Hauptarbeit ist jetzt strukturell:
  - Runtime als dauerhafter Innenprozess
  - saubere Entkopplung von Außenwelt und Innenwelt
  - Episode / Erfahrungsraum / Review als zentrale Lerneinheit
  - Entwicklungsebene als langfristige Rückkopplung auf die Innenbahn

## Was nicht mehr Hauptproblem ist

- reine Basis-Persistenz
- direkter Hot-Path-Vollsave
- volles NxN-Feld als ursprüngliche Hauptbremse
- ungedrosseltes Debug-Schreiben
- alter P0/P1-Block der Fix-Liste

## Wo der Fokus jetzt liegen sollte

1. Offene Phasen aus `UMSETZUNGSPLAN.md`
2. Runtime-/Bahntrennung weiter verhärten
3. 3-Ebenen-Zielarchitektur auch technisch vollständig durchziehen
4. Episodenmodell und Erfahrungsraum ausbauen
5. dedizierte Tests für die noch offenen Kernmodule ergänzen

# --------------------------------------------------
# Schlussfolgerung
# --------------------------------------------------

## Kurzfazit

- Die alte Fix-Liste ist im Kern abgearbeitet.
- Der aktuelle Stand ist: Basis steht, Architektur-Endausbau ist offen.
- Das Projekt befindet sich jetzt im Übergang von:
  - funktionierender Lern-/Runtime-Basis
  - hin zu einer konsequent getrennten MCM-Innenwelt mit dauerhafter Laufzeitschicht
  - plus einer klaren Entwicklungsebene, die aus Erfahrung die Innenbahn langfristig verändert

## Priorität ab jetzt

- Kein Rückfall in alte Basis-Fixes.
- Fokus auf:
  - permanenter Innenprozess
  - harte Thread-/Bahntrennung
  - Ebene 1 / äußeres Wahrnehmen sauber isolieren
  - Ebene 2 / inneres Wahrnehmen und Denken weiter entkoppeln
  - Ebene 3 / Entwicklungsebene vertiefen
  - Entscheidungsepisode
  - Erfahrungsraum
  - offene Testabdeckung

# --------------------------------------------------
# geändert wurde
# --------------------------------------------------

- `aktueller_stand.md`

# --------------------------------------------------
# was wurde umgesetzt ?
# --------------------------------------------------

- Zusammenfassung des aktuellen Projektstands auf den bestätigten 3-Ebenen- und Architektur-Endausbau-Stand aktualisiert.
