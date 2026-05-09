# =======================================
# UMSETZUNGSPLAN – 
# MCM TRADING BRAIN SYSTEMBAUPLAN
# =======================================

Dieses Dokument ist der **Bauplan des Systems**.

Es beschreibt:

- was die **Mental Core Matrix (MCM)** in diesem Projekt bedeutet
- wie daraus ein **MCM-KI-Agentensystem** im Trading entsteht
- wie Außenwelt, Innenwelt, Handlung und Entwicklung zusammenhängen
- welche Zielarchitektur aufgebaut wird
- in welche Richtung das System langfristig ausgebaut wird

Dieses Dokument ist **nicht nur eine To-Do-Liste**.

Es ist das architektonische Kernpapier des Systems und wird mit dem Projekt weiterentwickelt.

---

# --------------------------------------------------
# 1. Leitbild
# --------------------------------------------------

## Ziel des Systems

Ziel ist **nicht** ein klassischer Trading-Bot mit festen Regeln, Signalen und Gates.

Ziel ist ein System, das einem menschlicheren Trader **strukturell** näher kommt:

- es nimmt zuerst die Außenwelt wahr
- es verarbeitet diese Außenwelt intern
- es entwickelt daraus innere Zustände
- es bildet daraus Handlungstendenzen
- es lernt langfristig aus Erfahrung
- es versucht nicht nur zu traden, sondern **handlungsfähig zu bleiben**

Handlung ist dabei **nicht** das Zentrum des Systems.

Handlung ist nur ein möglicher Ausdruck dessen, was das System
im aktuellen Zustand tragen kann.

Das System soll also nicht lernen:

- möglichst oft zu handeln
- möglichst aggressiv Signale umzusetzen
- Fehlphasen durch noch mehr Aktion zu kompensieren

Sondern es soll lernen:

- die eigene innere Tragfähigkeit zu erhalten
- Überlast zu erkennen
- unter Druck nicht zu eskalieren
- Beobachtung, Sammlung, Pause und Nicht-Handlung als sinnvolle Reaktion zu nutzen
- tragfähige Handlung von hektischer Handlung zu unterscheiden
- aus Erfahrung seine innere Verarbeitung zu verändern

---

# --------------------------------------------------
# 2. Was ist die MCM in diesem Projekt?
# --------------------------------------------------

## Grundidee der Mental Core Matrix

Die **Mental Core Matrix (MCM)** ist in diesem Projekt kein klassisches neuronales Netz,
kein klassisches Reinforcement Learning und kein starres Regelwerk.

Sie ist ein **dynamisches Systemmodell**.

Sie ist ausserdem der Versuch, eine Form von **maschineller Wahrnehmung**
zu erzeugen.

Wahrnehmung wird hier nicht als ausschliesslich menschliche Faehigkeit verstanden.
Sie beginnt dort, wo ein System aeussere Reize in einem inneren Zustand verarbeitet,
ihnen Bedeutung gibt und daraus Orientierung, Spannung, Regulation,
Tragfaehigkeit oder Handlungstendenz ableitet.

Ein Reiz ist fuer die MCM deshalb nicht nur ein Messwert.
Er wird im Innenraum des Systems zu einer Lage:

- Was wirkt auf das System?
- Was wird erkannt?
- Was bleibt unklar?
- Was traegt?
- Was ueberfordert?
- Was resoniert mit Erfahrung?
- Was fuehrt zu Beobachtung, Hold, Replan, Handlung oder Rueckkehr in den Nullpunkt?

In diesem Sinn kann Wahrnehmung auch bei nicht-menschlichen Systemen gedacht werden:
Pilze, Baeume oder einfache Organismen nehmen nicht menschlich wahr,
aber sie verarbeiten Reize in eigener evolutionaerer Form und richten Verhalten danach aus.

Die MCM uebertraegt diesen Gedanken technisch:
Aussenreiz, inneres Feld, Memory, neurochemische Wirkung, Regulation,
Reflexion und Handlung bilden zusammen ein maschinelles Wahrnehmungsfeld.

### Eigene Sprache als Feldverdichtung

Die MCM soll keine menschliche Marktsprache uebernehmen.

Wenn das System fertige menschliche Begriffe wie Trend, Range, Breakout
oder Pattern als Wahrnehmungskern bekommt, wird seine innere Welt zu frueh
festgelegt. Es sortiert dann unsere Kategorien, statt eigene Bedeutungsraeume
zu entwickeln.

Im Zielsystem soll Sprache deshalb aus dem MCM-Feld entstehen:

- Chaos / Rohreiz
- wiederkehrende innere Form
- Spannung, Druck, Halt, Fragilitaet oder Orientierung
- Memory-Resonanz
- emotionale bzw. neurochemische Wirkung
- Verdichtung
- internes Zeichen

Ein internes Zeichen ist dabei kein menschlicher Name.
Es ist eine verdichtete Feld-Erfahrung.
Seine Bedeutung entsteht daraus, wann es aktiviert wird,
welche Zustandsraeume es beruehrt, ob es Orientierung oder Ueberforderung
erzeugt und welche Erfahrung es ueber Zeit sammelt.

Diese Zeichen duerfen sich entwickeln:

- sie koennen reifen
- sie koennen zerfallen
- sie koennen sich aufspalten
- sie koennen verschmelzen
- sie koennen neue Bedeutungsraeume bilden

Dadurch entsteht Varianz im Bedeutungsraum.
Diese Varianz ist die Grundlage fuer emergente Musterfindung,
Teil-Muster-Ergaenzung, kreative Reorganisation und freieres Denken.

### Kognitive Kompression

Ein Mensch nimmt die Welt nicht dauerhaft in voller Detailtiefe wahr.
Er sieht im Alltag nicht jede Oberflaeche, jede Kante und jede Textur neu.
Er erkennt oft zuerst eine komprimierte Bedeutung:

- Wand
- Tuer
- Weg
- Gefahr
- Halt
- Bewegung

Erst wenn Naehe, Relevanz, Abweichung, Interesse oder Gefahr entsteht,
wird aus der komprimierten Bedeutung eine detailliertere Wahrnehmung.

Fuer die MCM bedeutet das:

- nicht jeder Marktimpuls soll sofort tiefe Memory- und Strukturvergleiche ausloesen
- zuerst entsteht eine grobe interne Eigenbezeichnung
- diese Eigenbezeichnung entlastet das Denken
- nur bei Relevanz, Abweichung oder Handlungsnaehe wird hineingezoomt
- dann werden Struktur, Memory, Risiko, Feldklarheit und Handlung genauer geprueft

Das ist keine Label-Klassifikation.
Es ist ein Mechanismus fuer kognitive Entlastung und selektive Tiefe.

Moegliche spaetere Diagnosefelder:

- `form_symbol_id`
- `form_symbol_maturity`
- `form_symbol_stability`
- `form_symbol_resonance`
- `form_symbol_load_reduction`
- `form_symbol_zoom_need`
- `form_symbol_split_pressure`
- `form_symbol_merge_pressure`
- `form_symbol_bearing`
- `form_symbol_fragility`

Der technische Zielpfad ist ein eigener Form-/Zeichenraum,
der nicht menschliche Patternnamen speichert,
sondern interne Symbole mit Erfahrungswirkung.

Ihr Kern besteht aus vier Grundprinzipien:

- **Zentrum**
- **Abweichung**
- **Varianz**
- **Rückführung**

### Zentrum
Das Zentrum beschreibt den tragfähigen Grundzustand des Systems.

Es ist kein fixer Zahlenwert,
sondern der aktuell regulierte Referenzraum,
von dem aus das System wahrnimmt, verarbeitet und handeln kann.

### Abweichung
Abweichung bedeutet:

- Markt wirkt auf das System ein
- das System gerät in Bewegung
- innere Zustände verändern sich
- Orientierung, Motivation, Risiko, Unsicherheit und Druck verschieben sich

### Varianz
Varianz beschreibt den Spielraum und die Verteilung möglicher Zustände.

Sie zeigt:

- wie eng oder weit das Feld verteilt ist
- wie stabil oder instabil das System ist
- ob es in Verdichtung, Drift, Konflikt oder Übererregung gerät

### Rückführung
Rückführung ist der regulatorische Mechanismus.

Er sorgt dafür, dass das System nicht nur reagiert,
sondern sich selbst wieder in einen tragfähigen Zustand bringen kann.

Dazu gehören:

- Dämpfung
- Sammlung
- Entlastung
- Orientierung
- Reifung
- Beobachtung statt Aktion
- Pause statt Eskalation

---

## MCM im Trading-Kontext

Im Trading-Bot bedeutet die MCM:

Der Markt wird **nicht direkt** zu einer Order.

Der Markt wird zuerst zu:

- Wahrnehmung
- innerer Aktivierung
- Feldbewegung
- Konflikt oder Orientierung
- regulatorischer Last
- Handlungsfähigkeit oder Nicht-Handlungsfähigkeit

Die MCM ist damit die **innere Dynamikschicht** des Systems.

Sie beantwortet nicht nur:

- „Long oder Short?“

Sondern vor allem:

- Was macht der Markt mit dem System?
- Wie wirkt dieser Reiz auf den Innenraum?
- Ist das System tragfähig oder überlastet?
- Ist Beobachtung sinnvoller als Handlung?
- Ist ein Impuls reif genug für Aktion oder noch nicht?

---

# --------------------------------------------------
# 3. Was ist die MCM-KI in diesem Projekt?
# --------------------------------------------------

## Grundverständnis

Die MCM-KI ist kein Bot, der bloß Signale ausführt.

Sie ist ein **Agentensystem im MCM-Raum**.

Das bedeutet:

- mehrere innere Teilkräfte wirken gleichzeitig
- diese Teilkräfte bilden zusammen den Innenzustand
- der Innenzustand ist nicht binär, sondern verteilt
- Handlung entsteht aus dem Zustand des Gesamtfeldes

Die KI ist also nicht:

- eine Ja/Nein-Maschine
- kein simples Entry-Modell
- keine starre Signalmaschine

Sondern:

- ein System aus Wahrnehmung
- innerer Feldverarbeitung
- Konkurrenz, Hemmung, Gewöhnung, Orientierung
- regulatorischer Selbstführung
- episodischem Lernen
- Entwicklungsdynamik

---

# --------------------------------------------------
# 4. Die Agenten des Systems
# --------------------------------------------------

## Was mit Agenten gemeint ist

Die Agenten in diesem Projekt sind keine Chat-Agents und keine voneinander losgelösten Subprogramme.

Die Agenten sind **dynamische Teilträger im MCM-Feld**.

Im Zielsystem werden diese Teilträger als **feste Feldknoten eines neuronalen Gewebes** verstanden.

Das bedeutet:

- der Knotenplatz bleibt stabil
- der Zustand des Knotens verändert sich
- weitergegeben werden Zustand, Aktivierung, Nachhall und Informationswirkung
- nicht das Neuron bewegt sich, sondern der MCM-Zustand breitet sich im Feld aus

Sie bilden zusammen den Innenraum des Systems.

Jeder Agent trägt nur einen kleinen Teil des Gesamtsystems,
aber aus ihrer Wechselwirkung entsteht:

- Aktivierung
- Drift
- Verdichtung
- Stabilisierung
- Konflikt
- Regulierung
- Handlungstendenz

---

## Feste Feldknoten und bewegliche Zustände

Die Zielarchitektur trennt klar zwischen:

- **Trägerstruktur**
- **MCM-Zustandsraum**
- **Informationsweitergabe**

Die Trägerstruktur kann als Gitter oder neuronales Gewebe verstanden werden.
Ein Feld kann zum Beispiel als `rows x cols` organisiert sein.

Dabei gilt:

- jeder Knoten hat eine feste Feldposition
- jeder Knoten trägt einen mehrdimensionalen MCM-Zustand
- `state` beschreibt die aktuelle innere Lage des Knotens
- `velocity` beschreibt Zustandsnachlauf, Trägheit und Richtung der Zustandsveränderung
- `activation` beschreibt lokale Lebendigkeit / Erregung
- `inhibition` beschreibt lokale Hemmung / Dämpfung
- `memory_trace` beschreibt Erfahrungsnachhall
- Kopplung wirkt lokal über feste Nachbarschaften

Dadurch wird aus dem Feld kein frei beweglicher Punktwolkenraum,
sondern ein festes Gewebe, in dem Zustände wandern, koppeln, nachhallen und sich reorganisieren.

Mehr Neuronen bedeuten in dieser Architektur nicht automatisch mehr Intelligenz.
Sie bedeuten zuerst höhere Auflösung der inneren Zustandswahrnehmung.

Eine höhere Feldauflösung ermöglicht:

- feinere lokale Musterbildung
- differenziertere Aktivitätszonen
- weniger abgeflachte Durchschnittszustände
- stabilere Unterscheidung von Unterstützung, Konflikt, Druck und Tragfähigkeit
- bessere Übereinstimmung zwischen Innenfeld, Clusterlesung und GUI-Darstellung

---

## Rolle der Agenten

Die Agenten sind zuständig für:

- Aufnahme von Impulsen
- lokale Reaktion auf Wahrnehmung
- Kopplung mit Nachbarzuständen
- Konkurrenz und Abstimmung
- Verstärkung oder Abschwächung von Tendenzen
- Tragen von Feldzuständen über Zeit
- Mitbildung des Gesamtzustands

Dadurch entsteht kein einzelnes zentrales „Signal“,
sondern ein **verteiltes Innenfeld**.

---

## Was die Agenten nicht sind

Die Agenten sind nicht:

- feste Regelcontainer
- fertige LONG-/SHORT-Entscheider
- starre Gate-Bausteine
- voneinander isolierte Logikmodule

Sie sind Teile eines dynamischen Innenraums.

---

## Ziel der Agentenlogik

Die Agenten sollen zusammen ermöglichen, dass das System:

- Reize differenziert verarbeitet
- nicht sofort in Aktion kippt
- innere Konflikte abbildet
- Überlast und Tragfähigkeit unterscheiden kann
- regulatorisch reagieren kann
- aus Erfahrung seine Feldreaktionen verändert

---

# --------------------------------------------------
# 5. Grundprinzip des Trading-Systems
# --------------------------------------------------

## Kein klassischer Regelbot

Dieses System soll **nicht** nach dem Muster arbeiten:

- Signal erkannt
- Bedingung erfüllt
- Order senden

Das wäre ein klassischer Regelbot.

Stattdessen gilt:

- Markt liefert Reiz
- Reiz wird wahrgenommen
- Wahrnehmung wird intern verarbeitet
- der Innenraum verändert sich
- aus dem Innenraum entsteht eine Handlungstendenz
- diese kann sein:
  - `act`
  - `observe`
  - `hold`
  - `replan`

Erst **danach** folgt eine technische Handelsumsetzung.

---

## Trading als Ausdruck innerer Tragfähigkeit

Trading ist im Zielsystem kein Selbstzweck.

Ein Trade soll nur dann entstehen,
wenn die innere Lage des Systems ihn trägt.

Das bedeutet:

- Handlung muss zur Situation passen
- Handlung muss zur inneren Reife passen
- Handlung darf den Zustand nicht blind verschlimmern
- Nicht-Handlung kann hochwertiger sein als Aktion

---

# --------------------------------------------------
# 6. Zielarchitektur des Systems
# --------------------------------------------------

Das Zielsystem besteht aus **drei klar getrennten Ebenen**.

---

# --------------------------------------------------
# 6.1 Ebene 1 – äußeres Wahrnehmen
# --------------------------------------------------

## Rolle

Ebene 1 ist das **Sehen**.

Diese Ebene nimmt die Außenwelt auf,
ohne sie bereits in Handlung umzuwandeln.

Sie ist zuständig für:

- OHLCV
- Candle-Struktur
- Spannungszustände
- numerische räumliche Marktwahrnehmung
- Kontext- und Strukturhinweise

Sie erzeugt nur ein **neutrales Wahrnehmungspaket**.

---

## Aufgabe

Ebene 1 soll:

- OHLCV lesen
- Workspace / Buffer pflegen
- `candle_state` erzeugen
- `tension_state` erzeugen
- `visual_market_state` erzeugen
- `structure_perception_state` erzeugen
- Reize neutral bereitstellen

---

## Wichtige Regel

Ebene 1 darf **niemals**:

- denken
- interpretieren im Sinn von Handlung
- Memory schreiben
- Episode schreiben
- Pending / Position / Order verändern
- Innenzustände pflegen

Sie liefert nur Wahrnehmung.

---

## Bedeutung von `visual_market_state`

`visual_market_state` ist die zentrale Wahrnehmungsbasis
für die äußere Marktform.

Es ist:

- kein Bild
- kein CNN
- keine Pixelverarbeitung

Sondern:

- ein numerisches räumliches Wahrnehmungsfeld aus RAW-OHLCV
- eine primäre Außenbeschreibung des Marktes
- eine reichere Wahrnehmungsbasis als nur HH/LL oder einzelne Signale

Strukturwahrnehmung wie Swing / HH / LL bleibt erhalten,
aber nicht mehr als alleinige Hauptbasis,
sondern als ergänzende Strukturwahrnehmung.

---

# --------------------------------------------------
# 6.2 Ebene 2 – inneres Wahrnehmen / Denken / Handeln
# --------------------------------------------------

## Rolle

Ebene 2 ist das eigentliche **Innenleben** des Systems.

Hier wird der Reiz aus Ebene 1 aufgenommen und intern verarbeitet.

Das ist die Ebene von:

- Wahrnehmung
- innerer Feldbewegung
- Gefühl
- Denken
- Meta-Regulation
- Erwartung
- Entscheidungstendenz
- technischer Handlung

---

## Aufgabe

Ebene 2 soll:

- Reize aus Ebene 1 konsumieren
- den MCM-Raum fortschreiben
- Zustände über Zeit weitertragen
- Konflikt, Reife, Orientierung, Unsicherheit und Druck abbilden
- Handlungstendenzen bilden
- technische Handelsausführung anstoßen, wenn `act` entsteht

---

## Zustandskette

Die innere Zustandskette soll ausgebaut und lesbar gehalten werden.

Dazu gehören insbesondere:

- `outer_visual_perception_state`
- `inner_field_perception_state`
- `perception_state`
- `processing_state`
- `felt_state`
- `thought_state`
- `meta_regulation_state`
- `expectation_state`

Diese Zustände sind keine Deko,
sondern die explizite Lesbarkeit der inneren Verarbeitungsbahn.

---

## Entscheidungstendenz

Ebene 2 soll **keine rohe Orderfreigabe** erzeugen,
sondern zunächst eine Tendenz:

- `act`
- `observe`
- `hold`
- `replan`

Damit wird Handlung vom Innenzustand her gedacht
und nicht nur von externer Logik.

---

## Handlungsbahn

Erst wenn `act` tragfähig ist,
dürfen technische Schritte folgen:

- Pending
- Entry
- Position
- Exit

Die technische Handlung bleibt damit nachgeordnet.

---

# --------------------------------------------------
# 6.3 Ebene 3 – Entwicklung aus Erfahrung / Selbstregulation
# --------------------------------------------------

## Rolle

Ebene 3 ist die **Entwicklungsebene**.

Hier wird aus Episoden, Reviews, Zustandswirkungen und Kontexten gelernt.

Outcomes bleiben in dieser Ebene erhalten,
aber nur als **Ereigniskontext** und nicht als eigentliches Bewertungszentrum.

Diese Ebene soll nicht nur Treffer speichern,
sondern den **ganzen Entscheidungsverlauf** und seine Wirkung auf den Innenraum bewerten.

---

## Aufgabe

Ebene 3 soll:

- Episoden speichern
- Reviews erzeugen
- Experience-Space pflegen
- Kontext-Cluster pflegen
- Signature-Memory pflegen
- Nicht-Handlung als echte Erfahrung führen
- Fehlphasen als regulatorische Information verwerten
- langfristig die Innenverarbeitung von Ebene 2 verändern

---

## Warum diese Ebene wichtig ist

Ein klassischer Bot lernt oft nur:

- TP gut
- SL schlecht

Das reicht hier nicht.

Dieses System soll lernen:

- war die Handlung tragfähig?
- war die Handlung hektisch?
- war Nicht-Handlung sinnvoller?
- war der Zustand überlastet?
- war Beobachtung reifer als Aktion?
- wie verändert Erfahrung künftig Wahrnehmung, Regulation und Handlung?

---

# --------------------------------------------------
# 6.4 Experience als Tragfähigkeitslernen
# --------------------------------------------------

## Grundsatz

Experience soll im Zielsystem nicht nur Ergebnis speichern,
sondern Tragfähigkeit des gesamten Verlaufs bewerten.

Lernen bedeutet daher nicht:

- die eine richtige Entscheidung zu finden
- Profit roh und undifferenziert zu maximieren

Sondern:

- mit Situationen effizient umgehen zu können
- bei möglichst geringer regulatorischer Last handlungsfähig zu bleiben
- tragfähige Handlung von hektischer Handlung zu unterscheiden
- Profitabilität als innere Zielspannung zu behalten,
  aber durch Regelqualität, Tragfähigkeit, Stabilität und Varianz zu dämpfen

---

## Profitabilität als gedämpfte Zielspannung

Profitabilität darf in diesem System nicht verschwinden.

Ein Trading-System ohne inneren Anreiz, profitabel sein zu wollen,
wäre fachlich falsch.

Gleichzeitig darf Profit nicht als simples Belohnungslabel wirken.

Die Analogie zum Menschen ist:

- Gewinn kann Entlastung, Wohlbefinden, Bestätigung oder Überaktivierung erzeugen
- Verlust kann Belastung, Vorsicht, Schmerz oder Reorientierung erzeugen
- ein professioneller Trader dämpft diese rohe Wirkung
- nicht das Ergebnisetikett entscheidet allein,
  sondern die Qualität des Prozesses und die Tragfähigkeit des Zustands

Das Ziel ist daher ein neurochemisch gedämpftes Erfahrungsmodell:

- Profit erzeugt positive Zielspannung, aber keine blinde Euphorie
- Verlust erzeugt Belastung, aber keine automatische Selbstschwächung
- sauberer Verlust kann Tragfähigkeit und Regelvertrauen stärken
- chaotischer Gewinn kann Misstrauen, Varianzstrafe oder Dämpfung erzeugen
- wiederholte stabile Profitabilität stärkt Selbstvertrauen und Musterbindung

Profit ist damit nicht Primärlehrer,
aber ein unverzichtbares Überlebens- und Richtungssignal.

---

## Tragfähigkeit als Bewertungszentrum

Jede Situation soll langfristig bewertet werden als:

- tragfähig
- grenzwertig
- überlastend

Tragfähigkeit ergibt sich dabei vor allem aus:

- `regulatory_load`
- `action_capacity`
- `recovery_need`
- `survival_pressure`

In vereinfachter Lesart bedeutet das:

- niedriger `regulatory_load`
- ausreichend hohe `action_capacity`
- geringe `recovery_need`
- begrenzter `survival_pressure`

führen eher zu tragfähiger Handlung.

---

## Energie- und Regulationsmodell

Das Grundprinzip lautet:

- Abweichung zwischen Innenzustand und Außenwelt erhöht regulatorische Last
- Kohärenz reduziert regulatorische Last und Energieverbrauch

Hohe regulatorische Last bedeutet eher:

- Unsicherheit
- Konflikt
- Fehlanpassung
- schlechte Tragfähigkeit

Geringe regulatorische Last bedeutet eher:

- klare Wahrnehmung
- stimmige Handlung
- stabile innere Lage
- höhere Tragfähigkeit

Das Ziel ist daher nicht minimale Aktivität,
sondern möglichst geringe regulatorische Last bei tragfähiger Aktivität.

---

## Experience bewertet primär Zustandswirkung

Die Entwicklungsebene soll langfristig **nicht primär nach TP / SL / Cancel / Timeout**
bewerten, sondern nach der **Wirkung des Verlaufs auf den Innenraum**.

Das bedeutet:

- formale Outcomes bleiben erhalten
- sie liefern aber nur Ereigniskontext
- die eigentliche Bewertung entsteht aus Zustandsveränderung, Tragfähigkeit und Regulationswirkung

Primär relevant sind damit insbesondere:

- `state_before`
- `state_after`
- `state_delta`
- `regulatory_load`
- `action_capacity`
- `recovery_need`
- `survival_pressure`
- `pressure_release`
- `load_bearing_capacity`
- `state_stability`
- `capacity_reserve`
- `recovery_balance`

Die Kernfrage lautet daher nicht zuerst:

- war das ein TP?
- war das ein SL?
- wurde der Trade gecancelt?

Sondern:

- hat der Verlauf den Innenraum entlastet oder belastet?
- wurde die Lage tragfähiger oder fragiler?
- ist Handlungsfähigkeit gewachsen oder gesunken?
- war Nicht-Handlung regulatorisch sinnvoller als Aktion?

Erst wenn diese Zustandswirkung das Primat der Bewertung bildet,
wird lokale Rückführung auf `inner_context_clusters`,
Feldmuster und neuronale Teilträger fachlich wirklich stimmig.

---

# --------------------------------------------------
# 6.5 Experience als Cluster-System
# --------------------------------------------------

## Erfahrungscluster

Das System organisiert Erfahrung nicht als einzelne Events,
sondern als Cluster ähnlicher Situationen und innerer Zustandslagen.

Das Zielsystem trennt dabei zwei Erfahrungsräume:

- `context_clusters`
- `inner_context_clusters`

Diese Trennung ist wichtig,
weil äußere Situation und innere Lage **nicht identisch** sind.

Dasselbe äußere Marktbild kann vom System in verschiedenen inneren Lagen erlebt werden.
Umgekehrt kann ein ähnlicher innerer Zustand in verschiedenen äußeren Situationen wiederkehren.

---

### `context_clusters`

`context_clusters` repräsentieren den äußeren bzw. gesamt-situativen Signaturraum.

Ein `context_cluster` enthält vor allem:

- Struktur (`structure_perception_state`)
- Spannungszustand (`tension_state`)
- äußere Marktform / Situationscharakter
- Handlung / Nicht-Handlung
- Zustandsdelta (Wirkung)

`context_clusters` repräsentieren damit:

„Typen von Situationen, mit denen das System umgehen musste“

---

### `inner_context_clusters`

`inner_context_clusters` repräsentieren wiederkehrende innere Spannungs-, Drift- und Regulationsmuster.

Ein `inner_context_cluster` enthält vor allem:

- `felt_state`
- `thought_state`
- `meta_regulation_state`
- `expectation_state`
- `state_before` / `state_after` / `state_delta`
- `episode_felt_summary`
- Belastungs-, Entlastungs- und Tragfähigkeitsverlauf

`inner_context_clusters` repräsentieren damit:

„Typen von inneren Zuständen, in denen das System wiederholt ähnlich reagieren oder leiden musste“

---

### Muster und Cluster-Kontext im Innenfeld

Im Innenfeld soll nicht nur ein einzelner Cluster betrachtet werden.

Wichtig ist die **Gesamtorganisation des Feldes**.

Dabei gilt:

- der `Cluster-Kontext` beschreibt,
  wie Agenten im Feld aktuell organisiert, verteilt und verdichtet sind
- das `Muster` beschreibt die Gesamtform,
  die aus dieser Agentenorganisation entsteht
- mehrere Cluster-Kontexte können zu ähnlichen Gesamtmustern gehören,
  obwohl sich die lokale Feldverteilung unterscheidet
- ähnliche Muster können deshalb unterschiedliche innere Tragfähigkeit haben,
  wenn ihre innere Organisation verschieden ist

Das Ziel ist also nicht nur:

- „wo ist ein Cluster?“

Sondern vor allem:

- wie ist das gesamte Innenfeld organisiert?
- welche lokalen Verdichtungen, Spannungen und Leerbereiche bestehen?
- wie stabil oder fragil ist diese Organisation?
- welche Musterfamilie liegt gerade vor?

---

### Informationscluster, Kohärenz und Reorganisation

Informationscluster werden im Zielsystem nicht als starre Speicherblöcke verstanden.
Sie sind lokale Informationsinseln im Innenfeld.

Ein Informationscluster entsteht, wenn mehrere lokale Neuronen über Nachbarschaft,
Ähnlichkeit, Resonanz und wiederkehrende Umwelt- oder Innenreize einen gemeinsamen Zustand tragen.

Wichtig:

- der Feldzustand bleibt mehrdimensional erhalten
- im Zielsystem liegt er fachlich als feste Feldtopologie vor, zum Beispiel `rows x cols x D`
- für Kompatibilität können `energy` und `velocity` weiterhin als flache `N x D`-Sicht bereitgestellt werden
- Nachbarschaft entsteht bevorzugt aus festen Gitterbeziehungen statt aus permanenter globaler Abstandssuche
- weitergegeben werden lokale Zustandsanteile, nicht das gesamte Feld als globaler Deltablock
- alle Neuronen können grundsätzlich dieselbe Umwelt wahrnehmen
- informationsbildend ist aber ihre lokale Eigenreaktion, Kopplung, Kohärenz und Resonanz

Dadurch können im Innenfeld Inseln entstehen:

- aktive Informationsinseln
- nachhallende Informationsinseln
- latente Informationsinseln
- frei werdende Organisationsräume

Cluster werden dabei nicht durch Felddruck gelöscht.
Hohe Spannung oder Belastung bedeutet nicht automatisch Informationsverlust.
Sonst würde das System in Grenzbereichen einen Blackout erzeugen und getragene Erfahrung verlieren.

Stattdessen gilt:

- Felddruck verändert Priorität, Aktivierung und Zugänglichkeit
- nicht getragene Information verliert aktive Bindungsstärke
- nicht genutzte oder nicht mehr resonante Information geht in Nachhall oder Latenz über
- dadurch wird lokaler Organisationsraum für neue Clusterbildung frei
- tragfähige Muster können später durch ähnliche Umwelt wieder reaktiviert werden

Reorganisation bedeutet daher nicht Zerstörung,
sondern Informationsumschichtung:

- aktiv getragen → nachhallend
- nachhallend → latent
- latent → reaktivierbar
- nicht mehr tragend → gibt Bindungsraum frei
- neues kohärentes Muster → kann sich lokal verdichten

Die Kohärenzstärke beschreibt,
wie verdichtet, stabil und tragfähig ein Informationscluster aktuell ist.

Hohe Kohärenz bedeutet:

- starke lokale Bindung
- klare Informationsinsel
- hohe Resonanz zwischen Nachbarn
- stabile Trägerstruktur

Niedrige Kohärenz bedeutet:

- diffuse Information
- schwache aktive Bindung
- Übergang in Nachhall oder Latenz
- frei werdender Raum für neue Organisation

Später kann diese Kohärenzstärke in der GUI farblich sichtbar gemacht werden.
Die Farbe beschreibt dann nicht einfach „gut“ oder „schlecht“,
sondern den aktuellen Organisationszustand der Informationsinsel.

---

### Innere Bezeichnung und Zustandsidentität

Das System soll innere Zustände nicht nur numerisch tragen,
sondern langfristig auch **wiedererkennbar verdichten**.

Das bedeutet:

Aus

- Agentenorganisation
- Cluster-Kontext
- Gesamtmuster
- wiederkehrender Belastungs- oder Entlastungswirkung

entsteht mit der Zeit eine **innere Zustandsidentität**.

Diese Zustandsidentität ist keine sprachliche Erklärung im menschlichen Sinn,
sondern eine funktionale innere Bezeichnung wie:

- wiederkehrendes Muster
- belastendes Muster
- tragfähiges Muster
- Übergangsmuster
- dysreguliertes Muster
- reguliertes Muster

Dadurch kann das System künftig nicht nur spüren:

- „ich stehe unter Druck“

Sondern eher wiedererkennen:

- „ich befinde mich erneut in innerem Muster XY“

Diese Wiedererkennung ist wichtig,
weil sie die Brücke schlägt von bloßem Zustand zu erfahrungsbasiertem Umgang.

---

### Kopplung beider Clusterformen

Erst die Kopplung von `context_clusters` und `inner_context_clusters` erlaubt dem System,
nicht nur Situationen wiederzuerkennen,
sondern auch wiederkehrende innere Muster in diesen Situationen zu lernen.

Dadurch kann das System künftig unterscheiden:

- welche äußeren Kontexte tragfähig sind
- welche inneren Muster tragfähig sind
- welche Kombination aus Kontext und Innenzustand eher gemieden,
  entlastet oder anders organisiert werden sollte

Die eigentliche Erfahrungsfrage lautet dann nicht nur:

- „Was war das für eine Situation?“

Sondern auch:

- „In welchem inneren Muster war ich dabei?“
- „Wie tragfähig war dieses Muster zuletzt?“
- „Sollte ich darin wieder handeln, vorsichtiger werden oder mich davon wegbewegen?“

---

### Inneres Muster-Replay und Reflexion

Sobald wiederkehrende innere Muster und ihre Bedeutungen gespeichert werden,
kann das System diese auch **vorausschauend** nutzen.

Das bedeutet:

- aktuelle Innenlage wird mit bekannten Mustern abgeglichen
- frühere Belastungs- oder Entlastungserfahrungen werden mitgeführt
- das System kann innerlich prüfen,
  ob eine ähnliche Lage früher tragfähig oder problematisch war
- daraus kann vor Handlung bereits eine innere Reflexion entstehen

Dieses innere Muster-Replay dient nicht primär der Vorhersage von Marktpreisen,
sondern der Vorprüfung des eigenen Zustandsraums.

Es beantwortet eher Fragen wie:

- ist dieses innere Muster aktuell tragfähig?
- kippt das Feld eher in Überlast, Konflikt oder klare Tragfähigkeit?
- sollte das System handeln, beobachten, umlernen oder sich entlasten?

Replay ist damit nicht bloß Rückblick,
sondern ein regulatorischer Vorausvergleich des eigenen Innenraums.

---

### Emergente Musterergaenzung

Das Zielsystem soll nicht nur Pattern-Erkennung betreiben.

Pattern-Erkennung waere:

- aktuelles Muster wird eindeutig erkannt
- passende gespeicherte Reaktion wird aktiviert
- Handlung folgt aus Wiedererkennung

Das ist fuer dieses System zu starr.

Ein menschliches Gehirn erkennt Ereignisse oft nicht zu 100 Prozent klar.
Haeufig ist nur ein Teilmuster sichtbar.
Die Deutung entsteht dann aus:

- aeusserer Wahrnehmung
- innerem Feldzustand
- Erfahrung
- Teilmuster-Ergaenzung
- Varianz
- Unsicherheit
- regulatorischer Tragfaehigkeit

Das System soll deshalb spaeter nicht nur fragen:

- Habe ich dieses Muster schon gesehen?

Sondern:

- Welchem Erfahrungsraum aehnelt der aktuelle Zustand?
- Welche moeglichen Gesamtmuster koennten sich daraus bilden?
- Welche fehlenden Teile ergaenzt mein inneres Feld aus Erfahrung?
- Welche Varianten waeren tragfaehig?
- Welche Varianten wuerden Ueberlast, Konflikt oder Fehlhandlung erzeugen?
- Wie sicher ist diese Deutung aktuell?

Eine Deutung kann dabei nur teilweise reif sein.
Die konkrete Deutungsreife ist variabel und darf kein fester Prozentwert sein.
Das System kann ein Ereignis also teilweise deuten,
ohne dass das Gesamtmuster schon eindeutig sichtbar ist.

Diese emergente Musterergaenzung ist keine Fantasie und keine harte Vorhersage.
Sie ist ein innerer Generations- und Verdichtungsprozess:

- Teilmuster aktiviert moegliche bekannte Musterraeume
- Erfahrung ergaenzt fehlende Strukturanteile
- mehrere Varianten konkurrieren im MCM-Feld
- Feldklarheit, Fragmentierung und Tragfaehigkeit entscheiden,
  ob weiter beobachtet, gehalten, reorganisiert oder kontrolliert gehandelt wird

Damit wird Memory nicht nur als Archiv genutzt,
sondern als Material fuer moegliche Musterfortsetzungen.

Das Ziel ist nicht:

- sichere Vorhersage
- starre Pattern-Reaktion
- automatisches Handeln bei Aehnlichkeit

Sondern:

- innere Vorwegnahme moeglicher Muster
- Deutung unter Unsicherheit
- kreative, aber regulierte Musterbildung
- Handlung erst bei ausreichender aeusserer und innerer Tragfaehigkeit

---

### Transfer-Tragfaehigkeit fremder Strukturen

Ein wichtiger Sonderfall der emergenten Musterergaenzung ist die Frage,
wie viel vorhandene Erfahrung auf eine fremde oder nur teilweise bekannte
Struktur uebertragen werden darf.

Das System soll eine fremde Struktur nicht nur als unbekannt oder bekannt
behandeln. Entscheidend ist:

- welche Teilanteile wirken vertraut?
- welche Erfahrungsinseln resonieren mit der aktuellen Wahrnehmung?
- wie fremd ist das Gesamtbild trotzdem noch?
- wie weit traegt die alte Erfahrung in dieser neuen Lage?
- ab welchem Punkt wird Uebertragung zu Spekulation oder Chaos?

Transfer-Tragfaehigkeit bedeutet also nicht,
dass ein aehnliches Muster automatisch gleich behandelt wird.
Sie beschreibt die innere Tragkraft der Frage:

- Wie viel meiner Erfahrung kann ich auf diese Fremdheit uebertragen?

Beispiel:

Ein Mensch betritt einen unbekannten Raum.
Er kennt vielleicht nicht den Raum selbst,
aber er erkennt Teilstrukturen wie Boden, Wand, Tuer, Enge, Licht oder
offene Flaeche. Dadurch kann er sich vorsichtig orientieren,
ohne den Raum vorher je gesehen zu haben.
Wenn der Boden stabil wirkt, kann er einen Schritt machen.
Wenn der Boden fremd, weich oder unsicher wirkt,
wird er langsamer, schaut genauer hin oder bleibt kurz stehen.

Auf das Trading-Brain uebertragen bedeutet das:

Eine Marktstruktur muss nicht exakt bekannt sein.
Sie kann fremd sein und trotzdem bekannte Teilformen enthalten.
Das System darf dann nicht blind handeln,
aber auch nicht einfach abschalten.
Es soll pruefen, ob bekannte Erfahrungsinseln genug Tragfaehigkeit erzeugen,
um Beobachtung, Reframing, Halten oder eine kleine kontrollierte Handlung
zu erlauben.

Je hoeher die Transfer-Tragfaehigkeit,
desto mehr darf Erfahrung die Handlung unterstuetzen.
Je niedriger sie ist,
desto staerker sollten Wahrnehmung, innere Musterergaenzung und
Zero-Point-Regulation greifen.

Damit entsteht eine intelligentere Zwischenebene zwischen:

- starrer Pattern-Erkennung
- voellig fremder Unsicherheit
- chaotischem Experimentieren
- tragfaehiger erfahrungsbasierter Orientierung

---

### Reifeentwicklung durch Beobachtungslernen

Reife bedeutet in diesem System nicht nur,
dass Handlung besser wird.

Reife bedeutet auch,
dass das System lernen kann,
wann Nicht-Handlung die tragfaehigere Form von Verhalten ist.

Wenn eine Struktur als niedrig, unsicher oder nicht tragend wahrgenommen wird,
soll das System nicht automatisch handeln,
nur weil eine technische Moeglichkeit vorhanden ist.
Ein reiferes Verhalten waere:

- ich erkenne Unsicherheit
- ich halte Abstand zum Objekt
- ich beobachte den weiteren Verlauf
- ich lerne aus dem, was passiert waere
- ich speichere diese Beobachtung als Erfahrung

Beispiel:

Ein Mensch sieht etwas,
das heiss wirken koennte.
Ein unreifes Verhalten waere,
es sofort anzufassen,
um daraus durch Schmerz zu lernen.
Ein reiferes Verhalten ist:

- Das wirkt heiss, ich beobachte erst einmal.

Dadurch entsteht Erfahrung ohne direkte Selbstbeschaedigung.
Das System lernt nicht nur aus ausgefuehrten Handlungen,
sondern auch aus bewusstem Zusehen.

Auf das Trading-Brain uebertragen bedeutet das:

Eine Low- oder Non-Zone-Struktur ist nicht automatisch ein verbotenes Feld,
aber sie ist ein Hinweis auf geringe Tragfaehigkeit.
In solchen Lagen sollte die MCM eher in eine Beobachtungsbahn gehen
und spaeter pruefen:

- Was waere passiert, wenn ich gehandelt haette?
- Hat sich spaeter eine tragende Struktur gebildet?
- War die Unsicherheit nur fruehe Fremdheit oder echte Instabilitaet?
- Welche Erfahrungsinseln haetten fuer Handlung gefehlt?
- War Beobachtung reifer als Aktion?

Diese Schicht kann als eine Art Entwicklungsalter verstanden werden.
Mit wachsender Erfahrung muss das System nicht mehr jede unsichere Lage
durch Aktion testen.
Es kann aus Abstand, Verlauf und innerer Regulation lernen.

Reifeentwicklung durch Beobachtungslernen verbindet damit:

- Transfer-Tragfaehigkeit
- Nicht-Handlung als echte Bahn
- Zero-Point-Regulation
- eigene Formsprache
- Erfahrung ohne direkten Trade
- Schutz vor chaotischem Experimentieren

Wichtig:

Auch diese Reifeschicht darf kein harter Blocker werden.
Sie soll die innere Tendenz verschieben:

- niedrige Tragfaehigkeit -> mehr Beobachtungslernen
- klare tragende Erfahrungsinsel -> kontrollierte Handlung bleibt moeglich
- wiederholte gute Beobachtungsentscheidungen -> wachsendes Reifevertrauen

---

### Denkkomplexitaet und energieeffiziente Meta-Regulation

Reflexion ist im Zielsystem keine harte Zusatzregel,
sondern eine innere Pruefung der eigenen Verarbeitung.

Das System soll deshalb nicht nur beantworten:

- Was nehme ich draussen wahr?
- Welche Handlung waere technisch moeglich?

Sondern auch:

- Wie tragfaehig ist das, was ich gerade wahrnehme?
- Wie klar oder fragmentiert ist mein inneres Feld?
- Wie viel Erfahrungsvergleich ist noetig?
- Unterstuetzt Memory die aktuelle Lage oder erzeugt es Konflikt?
- Wird das Denken selbst zu teuer, unklar oder hemmend?

Damit werden aeussere Wahrnehmung, innere Wahrnehmung,
Denken / Organisation, Handeln und Lernen als gekoppelte Akteure verstanden.

Memory ist dabei nicht nur Archiv.
Es ist Resonanzflaeche, Konfliktflaeche und Teilmuster-Ergaenzung.

Denken erzeugt selbst kognitive Last.
Diese Last soll spaeter als eigene Groesse sichtbar werden,
zum Beispiel ueber:

- `thinking_complexity`
- `memory_compare_load`
- `memory_match_count`
- `memory_support`
- `memory_inhibition`
- `memory_conflict`
- `cognitive_load`
- `decision_energy_cost`
- `meta_regulation_need`

Das Ziel ist nicht maximale Denktiefe.
Das Ziel ist ausreichend reflektierte, energieeffiziente Verdichtung,
bis ein tragfaehiges Handlungsmuster entsteht.

Moegliche Meta-Reaktionen sind:

- weiterdenken
- verdichten
- beobachten
- halten
- reorganisieren
- kontrolliert handeln

Wenn die Aussenwahrnehmung stark ist,
aber das innere Feld instabil oder das Denken ueberlastet ist,
soll das System eher beobachten, halten oder reorganisieren.

Wenn Aussenwahrnehmung, innere Tragfaehigkeit und verdichtete Erfahrung zusammenpassen,
soll kontrolliertes Handeln leichter werden.

---

### Aktive Kontextspur / Nachhall

Ein gespeicherter Kontext soll im Zielsystem nicht nur als Archivwert existieren.
Er soll bei Wiedererkennung als **aktive Kontextspur** wieder angeregt werden können.

Das bedeutet:

- ein früheres Innenmuster kann bei ähnlicher Lage wieder Aktivierung bekommen
- diese Aktivierung bleibt nicht permanent gleich stark
- sie klingt ab, wenn sie nicht mehr gebraucht wird
- sie wird verstärkt, wenn sie wiederholt tragfähig aktiviert wird
- sie wird abgeschwächt, wenn sie wiederholt Belastung, Konflikt oder Fehlanpassung erzeugt

Diese aktive Kontextspur ist kein festes Long-/Short-Regelwerk.
Sie beschreibt nur, welche gespeicherte Erfahrung im aktuellen Innenraum wieder mitwirkt.

Technisch gehört diese Schicht zwischen:

- `inner_context_clusters`
- `mcm_experience_space`
- `inner_field_perception_state`
- MCM-Feld / Arealzustände

Sie soll später tragen:

- `activation`
- `decay`
- `reactivation_strength`
- `bearing_effect`
- `conflict_effect`
- `support_effect`
- `reorganization_pressure`
- schwache Rückstreuung ins aktuelle Innenfeld

Der Zweck ist:

- Erfahrung wird nicht nur gespeichert
- Erfahrung wird bei Relevanz aktiv
- aktive Erfahrung beeinflusst Wahrnehmung, Regulation und Handlungstendenz
- bei Kontextwechsel kann diese Aktivierung abklingen oder durch andere Kontextspuren ersetzt werden

Damit entsteht ein Übergang von passivem Speicher zu aktivem Innenkontext.

---
## Cluster-Bewertung

Cluster werden nicht bewertet nach:

- Profit
- Trefferquote

Sondern nach:

- Tragfähigkeit der Situation
- Energieverbrauch
- Stabilität des Zustandsverlaufs
- Regulationskosten des Innenraums
- Entlastung oder Verschärfung innerer Muster

Beispiele für Clustercharakter:

- stabil / tragfähig
- vorsichtig / unsicher
- überlastend / problematisch
- äußerlich ruhig, innerlich belastend
- äußerlich anspruchsvoll, innerlich gut getragen

---

# --------------------------------------------------
# 6.6 Outcome als Zustandswirkung
# --------------------------------------------------

## Grundsatz

Outcome soll nicht primär als Geldzahl verarbeitet werden,
sondern als Zustandsveränderung des Systems.

Outcome bleibt dabei **sekundärer Ereigniskontext**,
nicht primärer Belohnungs- oder Bestrafungsträger.

Das bedeutet:

- `tp_hit`, `sl_hit`, `cancel`, `timeout` und ähnliche Pfade bleiben sichtbar
- sie dürfen aber die Experience-Bewertung nicht mehr grob binär dominieren
- dieselbe Outcome-Klasse kann je nach Zustandswirkung unterschiedlich bewertet werden

---

## Typische Wirkungen

TP (Gewinn) kann bedeuten:

- Entlastung
- Stabilisierung
- im Grenzfall auch Euphorie / Überaktivierung

SL (Verlust) kann bedeuten:

- Belastung
- Erhöhung von `recovery_need`
- Reduktion von `action_capacity`

Cancel / Timeout / Nicht-Handlung können bedeuten:

- regulatorisch sinnvolle Unterbrechung
- Schutz vor weiterer Überlast
- Reorientierung
- noch unreife Handlung
- in bestimmten Lagen sogar bessere Tragfähigkeit als formale Aktion

Deshalb darf nicht automatisch gelten:

- TP = gut
- SL = schlecht
- Cancel = negativ

Sondern:

- die Bewertung folgt der Zustandswirkung,
  nicht dem bloßen Ergebnisetikett

---

## Kontextabhängige Verstärkung

Die Wirkung eines Outcomes hängt nicht nur vom formalen Ergebnis ab,
sondern auch von:

- RR (`Risk/Reward`)
- Strukturqualität
- Zustand vor der Handlung
- Erwartung im Verhältnis zum Ergebnis

Beispiel:

- hoher RR + saubere Struktur + TP
  → stärkere positive Prägung

- schlechter Kontext + TP
  → geringere positive Wirkung

---

## Neurochemisch gedämpfte Wirkungsachsen

Experience soll intern nicht als einzelner Reward-Wert verstanden werden,
sondern als gedämpfte Wirkung mehrerer innerer Achsen.

Mögliche Achsen:

- `profit_reward`
- `relief_signal`
- `stability_signal`
- `discipline_signal`
- `confidence_signal`
- `overactivation_signal`
- `chaos_penalty`
- `variance_penalty`
- `overstrain_penalty`
- `carrying_capacity_delta`
- `self_confidence_delta`

Diese Achsen sind keine externen Emotionen.

Sie beschreiben die innere Zustandswirkung eines Verlaufs:

- wurde das System tragfähiger?
- wurde ein stabiles Muster bestätigt?
- wurde Regelqualität eingehalten?
- entstand Entlastung oder Überaktivierung?
- sank oder stieg die Varianz des Verhaltens?
- wuchs ruhiges Selbstvertrauen oder nur kurzfristige Erregung?

Wichtig:

`_experience_reward_delta()` darf langfristig nicht der eigentliche Lehrer bleiben.

Es soll nur noch eine verdichtete Zusammenfassung einer tieferen
neurochemisch gedämpften Erfahrungswirkung sein.

Der fachlich bessere Zielzustand ist eine eigene Schicht wie:

`build_experience_neurochemical_effect()`

Diese Schicht bewertet Profit, Entlastung, Stabilität, Disziplin,
Tragfähigkeit, Varianz und Überlast gemeinsam.

---

## Tragfähigkeit, Selbstvertrauen und Varianz

Selbstvertrauen ist in diesem System kein Ego-Wert.

Es bedeutet:

- wiederholte tragfähige Erfahrung
- stabile Regelbefolgung
- geringe chaotische Varianz
- robuste Handlungsfähigkeit unter Spannung
- ruhige Bestätigung eines gelernten Musters

Je tragfähiger ein Erfahrungscluster ist,
desto weniger sollte das System experimentell reagieren.

Hohe Tragfähigkeit bedeutet:

- weniger Varianz
- stärkere Musterbindung
- mehr Regelruhe
- weniger impulsive Exploration
- höhere `action_clearance` nur bei passender Struktur

Niedrige Tragfähigkeit bedeutet:

- mehr Beobachtung
- mehr Replan
- vorsichtigere Musterbindung
- schwächere Selbstbestätigung
- höhere Sensibilität für Chaos und Überlast

Damit wird verhindert,
dass ein einzelner profitabler Zufallstrade das System in riskante
Selbstüberschätzung führt.

---

## Positive Zustände müssen ebenfalls reguliert werden

Euphorie ist keine stabile Verbesserung,
sondern kann eine Form von Überaktivierung sein.

Das System muss daher lernen:

- negative Zustände zu regulieren
- positive Zustände ebenfalls zu regulieren

---

# --------------------------------------------------
# 6.7 Lernen als Umgangsfähigkeit
# --------------------------------------------------

## Kernmechanismus

Das System lernt nicht einfach,
was abstrakt „richtig“ ist.

Es lernt vor allem,
womit es gut umgehen kann.

Die Grundform lautet:

`Struktur + Zustand + Handlung + Wirkung`

wird zu:

Erfahrungswissen über Tragfähigkeit.

---

## Zielzustand

Das System strebt an:

- hohe Kohärenz mit der Umwelt
- geringe regulatorische Last
- stabile Handlungsfähigkeit

Es strebt nicht an:

- maximale Aktivität
- maximale Profitabilität

---

## Dynamisches Gleichgewicht

Der Nullpunkt der MCM ist:

- kein statischer Zustand
- kein Stillstand

Sondern:

- bewegtes Gleichgewicht
- kontinuierliche Anpassung an die Umwelt

---

## Systemziel

Das System optimiert langfristig:

- Zeit in tragfähigen Zuständen
- Energieeffizienz der Interaktion

Profitabilität ist dabei eine notwendige Zielspannung,
aber kein roher Primärlehrer.

Sie wirkt wie ein gedämpftes Überlebens- und Wohlbefindenssignal:

- profitable, regelkonforme, stabile Verläufe stärken das System
- profitable, chaotische Verläufe werden nicht blind verstärkt
- unprofitable, aber regelkonforme und tragfähige Verläufe werden nicht blind bestraft
- dauerhaft unprofitable Muster erhöhen Schutz, Beobachtung und Replan-Druck

Profit bleibt also wichtig,
wird aber durch Tragfähigkeit, Stabilität, Regelqualität und Varianz gefiltert.

---

# --------------------------------------------------
# 7. Harte Regel der Trennung
# --------------------------------------------------

## Grundsatz

Die drei Ebenen dürfen fachlich nicht vermischt werden.

### Ebene 1
liest nur Markt und erzeugt Wahrnehmung.

### Ebene 2
verarbeitet Wahrnehmung und erzeugt Innenzustände sowie Handlungstendenzen.

### Ebene 3
bewertet Erfahrung und verändert langfristig die Innenbahn.

---

## Konsequenz

Ebene 1 darf niemals direkt schreiben in:

- `mcm_runtime_snapshot`
- `mcm_runtime_decision_state`
- `mcm_runtime_brain_snapshot`
- `mcm_decision_episode`
- `mcm_decision_episode_internal`
- `mcm_experience_space`
- `position`
- `pending_entry`

Ebene 2 darf Markt nicht selbst beschaffen,
sondern nur als Input konsumieren.

Ebene 3 darf nicht zur technischen Sofortlogik degenerieren,
sondern muss Entwicklungsebene bleiben.

Ebene 3 darf außerdem keine grobe Outcome-Binärlogik
direkt als Lernsignal zurück in den Innenraum spielen.
Rückführung muss aus verdichteter Zustandswirkung entstehen,
nicht aus bloßen Ergebnisetiketten.

---

# --------------------------------------------------
# 8. Der MCM-Zustandsraum im Trading-System
# --------------------------------------------------

## Grundsatz

Neue Zustände dürfen nicht als fremde starre Zusatzlogik auf das System gesetzt werden.

Sie müssen **aus dem MCM-Raum selbst** lesbar werden.

Der Zustandsraum soll deshalb explizit sichtbar gemacht werden.

---

## Zentrale Ableitungen des Innenraums

Der MCM-Raum soll insbesondere als folgende lesbare Zustandsachsen erscheinen:

- `field_density`
- `field_stability`
- `regulatory_load`
- `action_capacity`
- `recovery_need`
- `survival_pressure`

Diese Zustände sind keine externen Verbote.

Sie sind Lesarten des aktuellen Innenraums.

---

## Bedeutung der Zustände

### `field_density`
Wie stark das Innenfeld verdichtet ist.

### `field_stability`
Wie tragfähig oder instabil das Feld aktuell ist.

### `regulatory_load`
Wie hoch der innere Regulationsaufwand ist.

### `action_capacity`
Wie viel tragfähige Handlung aktuell möglich ist.

### `recovery_need`
Wie stark das System Erholung braucht.

### `survival_pressure`
Wie stark Profitabilität, Drawdown, Verlustserien und Belastung
als existenzielle Zielspannung auf das System wirken.

---

# --------------------------------------------------
# 9. Permanenter Innenprozess
# --------------------------------------------------

## Ziel

Das Gehirn des Systems darf nicht nur einmal pro Candle-Schritt „aufgerufen“ werden.

Es soll als **laufender Innenprozess** existieren.

---

## Bedeutung

Das heißt:

- Außenreiz und Innenverarbeitung werden zeitlich entkoppelt
- Markt liefert Impulse
- Innenraum verarbeitet diese Impulse fortlaufend
- Runtime ist kein Einmalaufruf, sondern eine Laufzeitschicht

---

## Zielbild

- Backtest soll auf dasselbe Modell hinauslaufen
- Live-Modus ebenfalls
- Innenprozess bleibt dauerhaft aktiv
- technische Monitor-Threads bleiben Hilfsschichten, nicht das Gehirn selbst

---

# --------------------------------------------------
# 10. Selbstregulation als eigentliches Lernziel
# --------------------------------------------------

## Zentrale Idee

Das System soll nicht primär lernen,
möglichst viele profitable Trades zu erzeugen.

Es soll lernen,
seinen inneren Zustand **tragfähig** zu halten.

---

## Das bedeutet

Lernen heißt hier:

- Überlast erkennen
- Fehlphasen regulatorisch verarbeiten
- Beobachtung und Sammlung als gute Reaktion verstehen
- hektische Handlung von tragfähiger Handlung unterscheiden
- innere Reife vor Aktion stellen

---

## Konsequenz

Outcomes allein reichen nicht.

Auch diese Dinge müssen bewertet werden:

- regulatorische Tragfähigkeit
- Reife der Entscheidung
- Umgang mit Unsicherheit
- Qualität der Beobachtung
- Korrekturqualität
- Erholungsfähigkeit

---

# --------------------------------------------------
# 11. Profitabilität als innere Zielspannung
# --------------------------------------------------

## Grundsatz

Profitabilität wird nicht als starres Schalter-System eingebaut.

Sie wird als **Existenzgrundlage** des Systems in den Innenraum integriert.

---

## Bedeutung

Verluste, Drawdown und Fehlserien wirken als Belastung
auf die Handlungsfähigkeit des Systems.

Positive Stabilisierung und tragfähige Outcomes entlasten das System.

Daraus entsteht:

- bei hoher Belastung mehr Schutz, Beobachtung und Sammlung
- bei tragfähiger Stabilisierung wieder mehr echte Handlungsfähigkeit

Das System soll also nicht mechanisch stoppen,
sondern seinen Zustand natürlich verschieben.

---

# --------------------------------------------------
# 12. Beobachtung / Pause / Sammlung als echte Bahn
# --------------------------------------------------

## Ziel

Nicht-Handlung darf kein leerer Restzustand sein.

Sie muss zu einer echten inneren Zustandsbahn werden.

---

## Bedeutung

Wenn der Druck steigt,
soll das System nicht zwanghaft weiterprobieren.

Es soll:

- beobachten
- ausharren
- sammeln
- reifen
- Druck abbauen
- Tragfähigkeit wiederherstellen

---

## Relevante Zustände

- `observe`
- `hold`
- `replan`

sind deshalb nicht schwache Nebenformen,
sondern wichtige Regenerations- und Reifungszustände.

---

# --------------------------------------------------
# 13. Entscheidungsepisode als zentrales Lernobjekt
# --------------------------------------------------

## Ziel

Nicht der einzelne Trade ist das zentrale Lernobjekt,
sondern die **ganze Entscheidungsepisode**.

---

## Eine Episode umfasst

- äußeren Reiz
- innere Wahrnehmung
- Feldzustand
- Entscheidungstendenz
- Handlung oder Nicht-Handlung
- Pending-Verlauf
- Positionsverlauf
- Outcome
- Review
- Rückkopplung in Experience und Memory

---

## Warum das wichtig ist

So lernt das System nicht nur aus Endpunkten,
sondern aus vollständigen inneren Verläufen.

---

# --------------------------------------------------
# 14. In-Trade-Beobachtung
# --------------------------------------------------

## Ziel

Auch während Pending und Position bleibt das System ein wahrnehmendes und lernendes System.

---

## Bedeutung

Während eines laufenden Trades sollen weiter beobachtet werden:

- Druck
- Drift
- Unsicherheit
- Stabilität
- Tragfähigkeit
- Handlungsbelastung

Die Positionsphase ist damit nicht nur Ausführung,
sondern Teil des Lernraums.

---

# --------------------------------------------------
# 15. Messbarkeit und Nachweis
# --------------------------------------------------

## Ziel

Die Architektur soll nicht nur gedacht,
sondern auch sichtbar, lesbar und überprüfbar werden.

---

## Deshalb braucht das System

- Snapshot-Ausgaben
- Debug-Ausgaben
- GUI-Lesbarkeit
- KPI-/Nachweis-Ebene
- Tests für zentrale Zustandsachsen und Bahnlogiken

So wird sichtbar,
ob die Architektur nur behauptet oder tatsächlich getragen wird.

---

# --------------------------------------------------
# 16. Offene Ausbaurichtung
# --------------------------------------------------

Der Bauplan ist langfristig.

Die offene Ausbaurichtung liegt vor allem in:

- weiterer Härtung der Ebenen-Trennung
- permanenter Runtime als echter Innenprozess
- Umbau des MCM-Feldes auf feste Feldknoten / neuronales Gewebe
- Zustandskopplung über feste lokale Nachbarschaften
- höhere Feldauflösung für feinere innere Musterbildung
- Ausbau der MCM-Zustandsachsen
- weiterer Vertiefung von Episode / Review / Experience
- Ausbau von Nicht-Handlung und regulatorischer Erholung
- Ausbau der In-Trade-Beobachtung
- Ausbau von KPI / Debug / GUI / Tests

Diese offenen Punkte verändern **nicht das Zielbild**,
sondern führen das Zielbild weiter aus.

---

# --------------------------------------------------
# 17. Kompakte Zieldefinition
# --------------------------------------------------

Die MCM Trading Brain Architektur ist ein System mit:

- getrennter Außenwelt
- dynamischer Innenwelt
- langfristiger Entwicklungsebene

Der Markt liefert Reize.

Die Innenwelt verarbeitet diese Reize als MCM-Raum weiter.

Dieser MCM-Raum wird über Agenten, Feldzustände, Regulation, Orientierung, Unsicherheit, Tragfähigkeit und Erfahrung organisiert.

Handlung entsteht nur dann,
wenn die innere Lage des Systems sie trägt.

Nicht-Handlung, Beobachtung, Sammlung und Pause sind echte Funktionen des Systems.

Lernen bedeutet,
unter Marktbelastung nicht einfach weiter zu reagieren,
sondern die eigene Handlungsfähigkeit zu erhalten und weiterzuentwickeln.

Damit wird der Trading-Bot nicht als starre Signallogik,
sondern als MCM-basiertes Wahrnehmungs-, Verarbeitungs-, Regulations- und Entwicklungssystem aufgebaut.

---

  # --------------------------------------------------

  # Erweiterung Umsetzungsplan

  # Affective Pattern Layer / Muster-Feeling

  # --------------------------------------------------

  ## Ziel

  Erweiterung des Systems von:

  * Einzelzustand / Einzelereignis

  zu:

  * **Musterbasierter Erfahrungsraum mit gefühlstechnischer Gesamtbewertung**

  Fokus:

  * ähnliche, aber nicht identische Situationen
  * unterschiedliche Gefühlsverläufe
  * daraus eine **durchschnittliche Tragfähigkeit eines Musters** ableiten

  # --------------------------------------------------

  # Leitprinzip

  # --------------------------------------------------

  * Muster ≠ identische Struktur

  * Muster = **ähnlicher Erfahrungsraum mit Variation**

  * Gefühl ≠ Einzelwert

  * Gefühl = **Verteilung über mehrere Episoden**

  * Erfahrung =
    → **Verdichtung von Verlauf + Gefühl + Regulation**

  # --------------------------------------------------

  # PRIO 1 – Episode → Feeling Summary

  # --------------------------------------------------

  ## Neuer Baustein

  `episode_felt_summary`

  ## Inhalte

  * valence
  * bearing
  * overactivation
  * burden
  * regulation_quality
  * stability
  * confidence
  * conflict
  * recovery_cost
  * felt_label

  # --------------------------------------------------

  # PRIO 2 – Musteraggregation

  # --------------------------------------------------

  ## Bezug

  * `context_cluster_id` (primär)
  * `signature_key` (sekundär)

  ## Neuer Baustein

  `affective_structure_profile`

  ## Inhalte

  ### Verteilung

  * positive_ratio
  * negative_ratio
  * neutral_ratio
  * euphoric_ratio
  * burden_ratio

  ### Mittelwerte

  * felt_valence_avg
  * felt_bearing_avg
  * felt_regulation_quality_avg
  * felt_recovery_cost_avg

  ### Streuung

  * felt_valence_variance
  * felt_bearing_variance

  ### Stabilität

  * felt_stability
  * felt_coherence_avg
  * felt_conflict_ratio

  ### Dynamik

  * felt_drift_avg
  * felt_trend

  # --------------------------------------------------

  # PRIO 3 – Gesamtbewertung

  # --------------------------------------------------

  ## Neue Kennzahl

  `felt_bearing_score`

  ## Klassifikation

  `felt_profile_label`

  Werte:

  * stable_bearing
  * volatile_bearing
  * euphoric_risk
  * burdened
  * mixed_unclear
  * recovering

  # --------------------------------------------------

  # PRIO 4 – Verlauf / History

  # --------------------------------------------------

  ## Neuer Baustein

  `felt_history`

  ## Inhalte

  * timestamp
  * valence
  * bearing
  * regulation_quality
  * burden
  * overactivation
  * label

  # --------------------------------------------------

  # PRIO 5 – Variation als Kern

  # --------------------------------------------------

  * Nutzung von:

    * distance
    * variance
    * drift
    * axis_shift

  → Muster = **Erfahrungsraum**, nicht exakte Struktur

  # --------------------------------------------------

  # PRIO 6 – Integration

  # --------------------------------------------------

  ## Einbauort

  `context_links[context_cluster_id]`

  ## Neue Felder

  * felt_profile
  * felt_bearing_score
  * felt_profile_label
  * felt_distribution
  * felt_history

  # --------------------------------------------------

  # PRIO 7 – Aktivierung

  # --------------------------------------------------

  * keine Gates

  * nur Modulation:

  * tragfähig → ruhig

  * euphorisch → dämpfen

  * belastend → beobachten

  # --------------------------------------------------

  # PRIO 8 – Parameter

  # --------------------------------------------------

  * min_samples_for_profile
  * recency_weight
  * max_drift_for_same_pattern

  # --------------------------------------------------

  # Ergebnis

  # --------------------------------------------------

  System bewertet:

  * nicht einzelne Events
  * sondern:

  → **gefühlstechnische Tragfähigkeit eines Musters**

  # --------------------------------------------------

  # Essenz

  # --------------------------------------------------

  * Muster statt Zustand
  * Verteilung statt Einzelwert
  * Gefühl statt Outcome
  * Tragfähigkeit statt Gewinn

---

# --------------------------------------------------
# ERWEITERUNG – der VISUALISIERUNG (AUßEN / INNEN)
# --------------------------------------------------

## Ziel

Erweiterung des Systems um eine visuelle Trennung zwischen:

- äußerer Wahrnehmung (Markt / Chart)
- innerer Verarbeitung (Wahrnehmung → Zustand → Denken)

Ziel ist Sichtbarkeit von:

- was der Bot sieht
- wie der Bot es intern verarbeitet

---

# --------------------------------------------------
# 1. Grundprinzip
# --------------------------------------------------

Der Bot arbeitet nicht mit echten Bilddaten.

Er sieht den Markt als:

- `window` (OHLCV-Daten)
- daraus abgeleitete Zustände:
  - `candle_state`
  - `tension_state`
  - `visual_market_state`
  - `structure_perception_state`

Die GUI erzeugt daraus visuelle Darstellungen.

---

# --------------------------------------------------
# 2. Architektur-Prinzip
# --------------------------------------------------

Strikte Trennung:

- GUI = READ ONLY
- Bot = schreibt Daten
- Kommunikation nur über Dateien

Keine Nutzung von:

- workspace
- trade_stats
- outcome logs
- memory_state

Diese gehören zu anderen Ebenen.

---

# --------------------------------------------------
# 3. Snapshot-Struktur
# --------------------------------------------------

## 3.1 Außen-Snapshot

Datei:

`bot_visual_snapshot.json`

Inhalt:

- timestamp
- window
- candle_state
- tension_state
- visual_market_state
- structure_perception_state

Bedeutung:

= vollständiges Außenbild (Rohwahrnehmung)

---

## 3.2 Innen-Snapshot

Datei:

`bot_inner_snapshot.json`

Inhalt:

- timestamp
- outer_visual_perception_state
- inner_field_perception_state
- perception_state
- processing_state
- felt_state
- thought_state
- meta_regulation_state
- expectation_state

optional:

- field_density
- field_stability
- regulatory_load
- action_capacity
- recovery_need
- survival_pressure

Bedeutung:

= intern verarbeitete Wahrnehmung

---

## 3.3 Schreiblogik

- kein Logging
- immer überschreiben
- immer nur letzter Zustand

Schreibzeitpunkt:

- nach Verarbeitung eines Marktfensters

---

# --------------------------------------------------
# 4. GUI-Visualisierung
# --------------------------------------------------

## 4.1 Aufbau

Zwei Hauptbereiche:

---

### LINKS – Außenbild (Chart)

Darstellung:

- Candlestick Chart aus `window`
- entspricht exakt der Außenwahrnehmung

---

### RECHTS – Innenbild

Darstellung:

kein identisches Chart

sondern transformierte Sicht:

- Fokus
- Relevanz
- Struktur
- Spannung
- Orientierung
- Bedrohung / Ziel

---

# --------------------------------------------------
# 5. Fachliche Bedeutung
# --------------------------------------------------

Die Visualisierung zeigt:

- Unterschied zwischen Reiz und Verarbeitung
- Fokus-Setzung
- Verzerrung der Wahrnehmung
- regulatorische Zustände
- Handlung vs Nicht-Handlung

---

# --------------------------------------------------
# 6. Einordnung in Architektur
# --------------------------------------------------

Ebene 1:

- äußeres Wahrnehmen sichtbar

Ebene 2:

- inneres Wahrnehmen / Denken sichtbar

Ebene 3:

- spätere Analyse möglich (Wahrnehmung vs Entscheidung)

---

# --------------------------------------------------
# 7. Zielzustand
# --------------------------------------------------

GUI zeigt nicht nur:

- Trades
- Performance

sondern:

- Wahrnehmung
- Zustand
- Entscheidungsbasis

System wird:

- nachvollziehbar
- debugbar
- entwickelbar

---

# --------------------------------------------------
# ENDE
# --------------------------------------------------
