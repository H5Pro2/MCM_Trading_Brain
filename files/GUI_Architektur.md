Erstelle eine READ-ONLY Dark-Mode Desktop-GUI für einen Trading-Bot mit MCM-Architektur.

WICHTIG:
- Keine Schreibfunktion.
- Kein Bot-Start.
- Kein Reset.
- Keine Steuerung von Orders.
- Keine Eingriffe in den Bot.
- GUI ist nur Visualisierung und Leser.
- Kommunikation ausschließlich über vorhandene JSON- und CSV-Dateien.
- Keine Demo-Daten.
- Keine erfundenen Variablen.
- Nur tatsächlich vorhandene Zustände und Dateien verwenden.

ZIEL DER GUI:
Die GUI soll den Bot nicht wie einen klassischen Trading-Bot darstellen, sondern wie ein System mit getrennter Außenwahrnehmung und Innenverarbeitung.

Die GUI muss drei Ebenen sichtbar machen:
1. Außenwelt / Chart / Marktwahrnehmung
2. Innenwelt / Verarbeitung / Zustand / Entscheidungstendenz
3. Entwicklung / Erfahrung / Statistik / Memory

ARCHITEKTURPRINZIP:
- Strikte Trennung zwischen außen und innen
- Entscheidung ist nicht gleich Trade
- Nicht-Handlung ist ein echter Zustand
- GUI zeigt Wahrnehmung, Verarbeitung, Regulation und Erfahrung getrennt
- Keine starre Signaloptik
- Kein klassisches Buy/Sell-Bot-Design
- Eher Kontrollzentrum / Diagnosefenster / Zustandsraum

DATENQUELLEN:
- debug/trade_stats.json
- debug/trade_equity.csv
- bot_memory/memory_state.json
- debug/bot_visual_snapshot.json
- debug/bot_inner_snapshot.json
- Workspace-Datei bzw. Backtest-Datei je nach Modus

DATEIINHALTE / ZU VISUALISIERENDE BEREICHE:

AUSSEN-SNAPSHOT:
- timestamp
- window
- candle_state
- tension_state
- visual_market_state
- structure_perception_state

INNEN-SNAPSHOT:
- timestamp
- outer_visual_perception_state
- inner_field_perception_state
- perception_state
- processing_state
- felt_state
- thought_state
- meta_regulation_state
- expectation_state
- field_density
- field_stability
- regulatory_load
- action_capacity
- recovery_need
- survival_pressure

MEMORY / LANGZEIT:
- signature_memory
- context_clusters
- mcm_memory
- mcm_runtime_snapshot
- mcm_runtime_decision_state
- mcm_runtime_brain_snapshot
- mcm_decision_episode
- mcm_decision_episode_internal
- mcm_experience_space
- mcm_last_attractor
- mcm_last_action
- focus_point
- focus_confidence
- target_lock
- target_drift
- entry_expectation
- target_expectation
- approach_pressure
- pressure_release
- experience_regulation
- reflection_maturity
- load_bearing_capacity
- protective_width_regulation
- protective_courage
- inhibition_level
- habituation_level
- competition_bias
- observation_mode
- last_signal_relevance

STATISTIK / KPI:
- trades
- tp
- sl
- pnl_netto
- pnl_tp
- pnl_sl
- cancels
- attempts
- attempts_submitted
- attempts_filled
- attempts_cancelled
- attempts_timeout
- attempts_blocked
- attempts_skipped
- attempts_observed
- attempts_replanned
- attempts_withheld
- attempt_structure_zone
- attempt_non_structure_zone
- exploration_trades
- exploration_tp
- exploration_sl
- exploration_cancels
- exploration_pnl
- equity_peak
- max_drawdown_abs
- max_drawdown_pct
- kpi_summary

LAYOUT:
Baue die GUI als festes, ruhiges, dunkles Kontrollpanel.

OBEN:
- Header mit Coin, Modus, Timeframe, letzter Timestamp
- kompakte Systemstatus-Anzeige
- Statusfelder für:
  - Runtime aktiv / inaktiv
  - Snapshot aktuell / veraltet
  - Position offen / keine Position
  - Pending Entry / keiner
  - Entscheidungstendenz
  - Proposed Decision
  - Self State
  - Attractor

LINKE SPALTE = AUSSENWELT:
- OHLC/Chart-Bereich
- letzter sichtbarer Window-Ausschnitt
- optionale Candle-Darstellung
- darunter kompakte Außen-Zustandskarten:
  - candle_state
  - tension_state
  - visual_market_state
  - structure_perception_state
- Ziel: zeigen, was der Bot außen wahrnimmt
- keine Innenwerte in diesem Bereich

MITTLERE SPALTE = INNENWELT:
- zentrale Innenzustandskarten
- große hervorgehobene Kernachsen:
  - field_density
  - field_stability
  - regulatory_load
  - action_capacity
  - recovery_need
  - survival_pressure
- darunter Verarbeitungsstufen als getrennte Panels:
  - outer_visual_perception_state
  - inner_field_perception_state
  - perception_state
  - processing_state
  - felt_state
  - thought_state
  - meta_regulation_state
  - expectation_state
- Entscheidungstendenz klar sichtbar:
  - act
  - observe
  - hold
  - replan
- Ziel: zeigen, wie der Bot intern verarbeitet, nicht nur was er handelt

RECHTE SPALTE = ENTWICKLUNG / EXPERIENCE / MEMORY:
- signature_memory Überblick
- context_clusters Überblick
- mcm_memory Überblick
- letzte Episode
- letzter Review-Zustand
- Experience-Space Zusammenfassung
- felt_profile / felt_label wenn vorhanden
- similarity / drift / reinforcement / attenuation falls vorhanden
- Ziel: zeigen, wie Erfahrung den Bot verändert

UNTERER BEREICH:
- Equity-Kurve
- Attempts / Outcomes / Cancels / Non-Action Verlauf
- KPI-Zusammenfassung
- kompakte Tabellen oder Karten für:
  - Win/Loss
  - Attempts
  - Observe/Replan/Withheld
  - Drawdown
  - Capacity vs Pressure
  - Recovery-Balance

VISUELLE ANFORDERUNGEN:
- Dark Mode
- ruhiges Farbsystem
- keine grellen Neonfarben
- klare Trennung von Bereichen
- Außenwelt farblich neutral-kühl
- Innenwelt farblich leicht emotional/regulatorisch codiert
- Entwicklung/Memory etwas gedämpfter
- grün nur für tragfähig / stabil / entlastet
- orange für Spannung / Übergang
- rot für Überlast / hohe regulatorische Last
- kein klassisches Trading-Interface mit blinkenden Buy/Sell-Farben
- moderne technische Optik, aber nicht verspielt
- keine Animationen, die ablenken
- Fokus auf Lesbarkeit und Zustandsverständnis

FUNKTIONALE ANFORDERUNGEN:
- automatisches Refresh ca. jede Sekunde
- robust gegen fehlende Dateien
- robust gegen leere JSON/CSV
- kein Freeze bei fehlenden Daten
- statische Layout-Größen
- read-only
- kein Schreiben in Dateien
- kein Thread-Chaos
- GUI darf auch laufen, wenn einzelne Snapshot-Dateien noch fehlen
- verfügbare Daten anzeigen, fehlende sauber als "nicht vorhanden"

DARSTELLUNGSLOGIK:
- Außen und Innen niemals mischen
- Chart ist nur äußere Wahrnehmung
- decision_tendency separat sichtbar
- Trade-Ausführung untergeordnet
- Nicht-Handlung sichtbar als legitimer Zustand
- Memory/Experience nicht als Log-Müll, sondern als strukturierter Entwicklungsraum
- GUI soll dem Benutzer helfen zu sehen:
  - was der Bot wahrnimmt
  - was das mit seinem Innenraum macht
  - ob Handlung tragfähig ist
  - wie Erfahrung die innere Tendenz verändert

TECHNISCHE VORGABEN:
- Desktop GUI
- geeignet für Python Tkinter + Matplotlib
- performanter read-only Aufbau
- modulare Panels
- sauber getrennte Datenladefunktionen
- klare Zustands-Fallbacks
- keine Annahmen über nicht vorhandene Felder
- wenn ein Feld fehlt: leer oder neutral anzeigen

AUSGABE, DIE ICH VON DIR WILL:
1. vollständiges GUI-Konzept
2. genaue Bereichsaufteilung
3. genaue Liste aller Widgets / Panels
4. Zuordnung jeder vorhandenen Variable zu einem Bereich
5. Vorschlag für Farben / Typografie / Abstände
6. Vorschlag für Karten, Tabellen, Heatmaps, Statusleisten, Diagramme
7. Vorschlag für sinnvolle Reihenfolge der Informationsdichte
8. Fokus auf strukturelle Lesbarkeit des Bots als Außen-/Innen-/Erfahrungssystem

Die GUI soll am Ende wirken wie das Cockpit eines wahrnehmenden, verarbeitenden, lernenden Trading-Systems – nicht wie eine simple Ordermaske.