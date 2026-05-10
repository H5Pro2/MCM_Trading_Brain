# ==================================================
# AKTUELLER STAND – MCM TRADING BRAIN
# ==================================================

Dieses Dokument beschreibt den aktuellen realen Ist-Zustand des Systems.

Es trennt sauber zwischen:

- bereits real im Code umgesetzt
- bereits korrigierten Fehlern
- real noch offenen Ausbaublöcken
- nächsten sinnvollen Schritten

Der Bauplan bleibt in `UMSETZUNGSPLAN.md`.
Dieses Dokument beschreibt nur den realen Stand des aktuellen Dateistands.

---

# --------------------------------------------------
# 0. Neuester Debug- und Umsetzungsstand
# --------------------------------------------------

Dokumentationspflege:

- `files/WICHTIG_MECHANIKEN.md` wurde als Mechanik-Schatzkammer markiert.
- Die Datei bleibt erhalten, aber nicht als tagesaktueller Umsetzungsplan.
- Sie dient als Konzeptarchiv fuer wichtige MCM-Denkspuren:
  - MCMField / MCMNeuron
  - Innenfeldorganisation
  - Feldtopologie
  - inner_context_clusters
  - Erfahrungsrueckwirkung
  - MCM als maschinelle Wahrnehmungs- und Innenorganisationsschicht
- Ergaenzt wurde ein aktueller Statusblock:
  - Teile der Datei sind historisch
  - `MCMNeuron` ist inzwischen real umgesetzt
  - neuere Mechaniken wie Formsprache, Formsymbol-Memory,
    Transfer-Tragfaehigkeit, Beobachtungslernen, Prozessqualitaet und DIO
    muessen beim Lesen mitgedacht werden.
- `README.md` wurde fachlich um den Abschnitt `MCM als Spannungsraum`
  erweitert.
  - Die MCM wird dort als innerer Spannungsraum beschrieben.
  - Ein Chart wird als aeusserer Spannungsverlauf verstanden:
    Druck, Entlastung, Verdichtung, Bruch, Erholung, Ueberdehnung,
    Tragfaehigkeit und Reorganisation.
  - Trading wird als harter Pruefstand fuer den MCM-Gedanken eingeordnet.
  - Profitabilitaet wird nicht als Kern des Projekts, sondern als moegliche
    Folge einer funktionierenden MCM-Mechanik beschrieben.
  - Im README wurden im bearbeiteten Bereich Umlaute sauber korrigiert.

Debug-Laeufe 13 und 14 wurden nach dem starken Lauf 12 geprueft:

- `debug_lauf_12`: ca. +11.23 Netto-PnL, Profit Factor ca. 1.73, 48 Trades
- `debug_lauf_13`: ca. +7.22 Netto-PnL, Profit Factor ca. 1.47, 43 Trades
- `debug_lauf_14`: ca. +2.87 Netto-PnL, Profit Factor ca. 1.19, 39 Trades
- `debug_lauf_15`: ca. +15.90 Netto-PnL, Profit Factor ca. 1.97, 51 Trades
- `debug_lauf_16`: ca. +11.11 Netto-PnL, Profit Factor ca. 1.62, 54 Trades
- `debug_lauf_17`: ca. +12.09 Netto-PnL, 42 Trades
- `debug_lauf_18`: ca. +14.19 Netto-PnL, 37 Trades
- `debug_lauf_19`: ca. +13.67 Netto-PnL, 41 Trades
- `debug_lauf_20`: ca. +12.64 Netto-PnL, 47 Trades
- `debug_lauf_21`: ca. +10.30 Netto-PnL, 46 Trades
- `debug_lauf_22`: ca. +1.67 Netto-PnL, 40 Trades
- `debug_lauf_23`: ca. +16.13 Netto-PnL, 41 Trades
- `debug_lauf_24`: ca. +7.05 Netto-PnL, 39 Trades
- `debug_lauf_25`: ca. +12.76 Netto-PnL, 43 Trades
- `debug_lauf_26`: ca. +2.99 Netto-PnL, 39 Trades
- `debug_lauf_27`: ca. +1.93 Netto-PnL, 33 Trades, versehentlich mit
  `MCM_MATURED_EXIT_MODE = "active"`
- `debug_lauf_28`: ca. +8.90 Netto-PnL, 49 Trades, wieder im Observe-Modus
- `debug_lauf_29`: ca. +5.81 Netto-PnL, 36 Trades, mit
  `exit_candidate_observe`-Diagnose
- `debug_lauf_30`: ca. +11.60 Netto-PnL, 33 Trades, weiter im Observe-Modus
- `debug_lauf_31`: ca. +17.46 Netto-PnL, 47 Trades, mit
  Kandidaten-Replay-Summen
- `debug_lauf_32`: ca. +9.81 Netto-PnL, 48 Trades, Replay-CSV vorhanden
- `debug_lauf_33`: ca. +7.78 Netto-PnL, 25 Trades, saubere Replay-CSV
- `debug_lauf_34`: ca. +19.67 Netto-PnL, 39 Trades, sehr starker Lauf

Befund:

- Die fallende Kurve aus Lauf 12 -> 14 war kein kompletter Zusammenbruch
  der Brain-Logik.
- Lauf 15 dreht wieder deutlich nach oben und ist im bisherigen Vergleich
  der staerkste Lauf.
- Lauf 16 bleibt klar positiv, faellt aber gegen Lauf 15 zurueck.
- Lauf 17 bleibt ebenfalls klar positiv und reduziert die Tradezahl deutlich.
- Lauf 18 verbessert sich weiter und reduziert die Tradezahl erneut.
- Lauf 19 bleibt klar positiv und aktiviert erstmals die Beobachtungslernspur.
- Lauf 20 bestaetigt die Beobachtungslernspur, aber die Tradezahl steigt wieder.
- Lauf 21 faellt weiter im PnL, obwohl Beobachtungslernen aktiv bleibt.
- Lauf 22 zeigt einen massiven PnL-Rueckgang trotz weniger Trades.
- Lauf 23 erholt sich stark nach Korrektur des realen Struktur-Scopes.
- Lauf 24 mit `MCM_MATURED_EXIT_MODE = "observe"` bleibt positiv,
  erzeugt aber noch keine gereiften Exit-Beobachtungen.
- Lauf 25 bleibt positiv und erzeugt erstmals gereifte Exit-Beobachtungen
  im Observe-Modus.
- Lauf 26 bleibt knapp positiv, faellt aber deutlich zurueck.
- Die gereifte Exit-Beobachtung wird staerker sichtbar, ist aber noch gemischt:
  sie erkennt echte Schutzmomente, wuerde aber auch spaetere TP-Trades zu frueh
  beschneiden, wenn sie bereits aktiv handeln duerfte.
- Lauf 27 bestaetigt diese Warnung im Active-Modus:
  `matured_exit` reduziert zwar einzelne Risiken, beschneidet aber die
  Gewinnentwicklung zu frueh und drueckt den Gesamtlauf weiter.
- Lauf 28 bestaetigt die neue Positionslast-Diagnose:
  `plan_holding_trust` ist stark positiv, `exit_nervousness_observe`
  markiert dagegen die belasteten Verlustlagen.
- Lauf 29 faellt gegen Lauf 28 zurueck, bestaetigt aber die neue
  Exit-Kandidaten-Schicht: Kandidaten lagen nur auf spaeteren SL-Lagen.
- Lauf 30 erholt sich deutlich und bestaetigt die Trennung erneut:
  `plan_holding_trust` lag ausschliesslich auf TP-Trades, echte
  `exit_candidate_observe`-Markierungen lagen ausschliesslich auf SL-Trades.
- Lauf 31 ist der bisher staerkste Lauf dieser Sequenz. Gleichzeitig zeigt
  das neue Replay, dass ein aktiver Kandidaten-Exit noch nicht reif ist:
  mehrere SLs waeren kleiner geworden, aber ein spaeterer TP waere zu frueh
  abgeschnitten worden.
- Lauf 32 faellt gegen Lauf 31 zurueck, bleibt aber positiv. Hauptgrund:
  weniger High-Trades und deutlich mehr Low/Non-Zone-Verlust. Das Replay
  bestaetigt weiter: Kandidaten reduzieren viele kleine SLs, aber ein TP-Cut
  verhindert aktive Reife.
- Lauf 33 ist kleiner und etwas schwacher, bestaetigt aber denselben Kern:
  Exit-Kandidaten markieren Verlustlagen, aktives Schliessen bleibt wegen
  eines TP-Cuts unreif. Daraus wurde `exit_pullback_observe` abgeleitet.
- Lauf 34 springt stark nach oben. Entscheidend ist nicht nur ein guenstiger
  Marktabschnitt, sondern dass `plan_holding_trust` perfekt trennt und
  Low/Non-Zone fast neutral bleibt. Der offene Schwachpunkt bleibt der
  aktive Kandidaten-Exit wegen weiterem TP-Cut.
- Lauf 35 bleibt klar positiv:
  45 Trades, 21 TP / 24 SL, ca. +13.62 PnL, Profit Factor ca. 1.91,
  Max Drawdown ca. 2.41.
  `plan_holding_trust` bleibt die tragende Schicht:
  22 Trades, 21 TP / 1 SL, ca. +28.13 PnL.
  `exit_nervousness_observe` markiert fast nur Verlustlast:
  21 Trades, 0 TP / 21 SL, ca. -13.27 PnL.
  Das Exit-Kandidaten-Replay zeigt erstmals keinen TP-Cut:
  6 Faelle, alle haetten Verlust reduziert, kein harmed/TP-Cut.
- Lauf 36 bleibt ebenfalls positiv:
  36 Trades, 18 TP / 18 SL, ca. +11.93 PnL, Profit Factor ca. 2.05,
  Max Drawdown ca. 2.21.
  `plan_holding_trust` trennt perfekt:
  18 Trades, 18 TP / 0 SL, ca. +23.27 PnL.
  `exit_nervousness_observe` bleibt Verlustmarker:
  15 Trades, 0 TP / 15 SL, ca. -9.64 PnL.
  Das Replay bleibt sauber:
  3 Faelle, alle haetten Verlust reduziert, kein TP-Cut.
- Fachliche Einordnung Lauf 35/36:
  Der nach Lauf 33/34 eingefuehrte adverse-depth-Filter schuetzt deutlich
  besser vor vorschnellen TP-Cuts. Gleichzeitig bleibt die aktive
  Exit-Entscheidung observe-only, weil die Stichprobe noch klein ist.
  Die naechste Schwachstelle ist nicht der Exit-Kandidat selbst,
  sondern Low/Non-Zone und form_dev_negative:
  Lauf 36 hat Low/Non-Zone mit 10 Trades, 0 TP / 10 SL und ca. -6.92 PnL.
- Nach Lauf 34 wurde die fachliche Deutung erweitert:
  Ein Trade ist nicht nur Entry/TP/SL, sondern eine Handlung mit
  Erwartungshaltung. TP wird als Zielraum verstanden, SL als
  Tragfaehigkeitsgrenze und die offene Position als laufende Pruefung,
  ob die urspruengliche Zielerwartung noch traegt.
- Daraus folgt:
  Exit-Druck darf nicht automatisch Exit-Reife bedeuten. Entscheidend ist,
  ob die Zielerwartung wirklich bricht oder ob nur die Positionslast steigt.
  Diese Schicht wurde in README und UMSETZUNGSPLAN dokumentiert.
- Naechster sinnvoller Schritt:
  `target_expectation_context`, `tp_reachability`,
  `target_path_integrity`, `expectation_deviation`,
  `expectation_break_pressure` und `expectation_hold_support`
  zunaechst nur als Backtest-/Replay-Diagnose ergaenzen.
  Ziel: TP-Cuts besser von echten SL-Schutzmomenten trennen,
  ohne harte Exit-Regeln einzubauen.
- Erwartungsdiagnose wurde observe-only umgesetzt:
  - neues Protokoll `mcm_target_expectation_protocol.csv`
  - neue Felder im Positionskontext:
    `target_expectation_context`, `tp_reachability`,
    `target_path_integrity`, `expectation_deviation`,
    `expectation_break_pressure`, `expectation_hold_support`,
    `target_room_pressure`, `target_semantic_confidence`
  - Exit-Kandidaten und Replay erhalten diese Werte ebenfalls.
  Wichtig: Die aktive Exit-Entscheidung wird dadurch noch nicht veraendert.
  Die Schicht misst nur, ob Zielerwartung haelt oder bricht.
- Naechster Debug-Fokus:
  Pruefen, ob Kandidaten mit spaeterem SL hohe `expectation_break_pressure`
  und niedrige `expectation_hold_support` zeigen,
  waehrend spaetere TP/Plan-Holds hohe `tp_reachability` behalten.
- Lauf 37 bestaetigt die Erwartungsdiagnose deutlich:
  - Gesamt: 46 Trades, 18 TP / 28 SL, ca. +5.97 PnL,
    Profit Factor ca. 1.35, Max Drawdown ca. 3.78.
  - `target_expectation_holds`: 19 Outcome-Trades,
    18 TP / 1 SL, ca. +22.69 PnL.
  - `expectation_break_observe`: 23 Outcome-Trades,
    0 TP / 23 SL, ca. -14.43 PnL.
  - TP-Outcomes zeigen im Mittel:
    `tp_reachability` ca. 0.77,
    `expectation_break_pressure` ca. 0.19,
    `expectation_hold_support` ca. 0.77.
  - SL-Outcomes zeigen im Mittel:
    `tp_reachability` ca. 0.40,
    `expectation_break_pressure` ca. 0.64,
    `expectation_hold_support` ca. 0.43.
- Lauf 37 Replay:
  6 Exit-Kandidaten, alle spaeter SL,
  alle mit `target_expectation_context=expectation_break_observe`,
  alle haetten Verlust reduziert,
  kein harmed/TP-Cut.
  Das ist die bisher sauberste Bestaetigung,
  dass Zielerwartung die Trennung zwischen Exit-Nervositaet
  und echtem Erwartungsbruch sichtbar macht.
- Offene Schwachstelle bleibt Low/Non-Zone:
  17 Trades, 0 TP / 17 SL, ca. -10.43 PnL.
  Die naechste Umsetzung sollte Low/Non-Zone nicht hart blockieren,
  sondern die neue Erwartungsdiagnose vor Entry/Handlung als
  Reife-/Tragfaehigkeitswahrnehmung nutzbar machen.
- Lauf 38 bestaetigt die Reorganisationsvermutung:
  Nach Einfuehrung der neuen Zielerwartungs-Wahrnehmung war Lauf 37
  schwacher, Lauf 38 springt wieder deutlich nach oben.
  Ergebnis: 40 Trades, 20 TP / 20 SL, ca. +14.97 PnL,
  Profit Factor ca. 2.19, Max Drawdown ca. 2.39.
- Die Erwartungsdiagnose bleibt stabil:
  - `target_expectation_holds`: 21 Trades, 20 TP / 1 SL,
    ca. +27.04 PnL.
  - `expectation_break_observe`: 14 Trades, 0 TP / 14 SL,
    ca. -9.03 PnL.
  - TP-Outcomes:
    `tp_reachability` ca. 0.77,
    `expectation_break_pressure` ca. 0.19,
    `expectation_hold_support` ca. 0.76.
  - SL-Outcomes:
    `tp_reachability` ca. 0.40,
    `expectation_break_pressure` ca. 0.62,
    `expectation_hold_support` ca. 0.43.
- Lauf 38 Replay zeigt einen wichtigen Reorganisationsfall:
  4 Exit-Kandidaten, 3 haetten Verlust reduziert,
  1 Fall haette einen spaeteren TP massiv abgeschnitten.
  Der TP-Cut war ebenfalls als `expectation_break_observe` markiert.
  Das bedeutet:
  Die Erwartungsdiagnose trennt Outcomes sehr gut,
  aber ein einzelner tiefer Ruecksetzer kann noch wie Erwartungsbruch wirken,
  obwohl der groessere Plan spaeter wieder traegt.
- Fachliche Folgerung:
  Zielerwartung darf noch nicht aktiv als Exit-Entscheidung genutzt werden.
  Vor einer Aktivierung braucht es eine Unterscheidung zwischen:
  - echter Erwartungsbruch
  - tiefe Rueckatmung/Reorganisation
  - kurzfristige Feldverschiebung nach neuer Wahrnehmung
  Dazu sollten `target_recovery_potential`, `prior_target_hold_support`
  oder eine mehrstufige Erwartungsbruch-Bestaetigung geprueft werden.
- Recovery-/Reorganisationsdiagnose wurde observe-only umgesetzt:
  - `target_recovery_potential`
  - `prior_target_hold_support`
  - `prior_tp_reachability`
  - `prior_target_path_integrity`
  - `expectation_break_persistence`
  - `expectation_break_count`
  - `deep_pullback_recovery_watch`
  Die offene Position merkt sich damit kurzfristig,
  ob vor einem scheinbaren Erwartungsbruch bereits starker Zielhalt bestand.
  Ein Bruch mit hohem Recovery-Potential wird nicht als endgueltige
  Entscheidung verstanden, sondern als tiefe Rueckatmung/Reorganisation
  beobachtet.
- Naechster Debug-Fokus Lauf 39:
  Pruefen, ob der bisherige TP-Cut-Typ als `deep_pullback_recovery_watch`
  sichtbar wird, waehrend echte SL-Kandidaten weiterhin eine hohe
  `expectation_break_persistence` und niedrige Recovery zeigen.
- Lauf 39 ausgewertet:
  47 Trades, 23 TP / 24 SL, ca. +15.30 PnL,
  Profit Factor ca. 2.10, Max Drawdown ca. 3.26.
  Der Lauf bleibt damit stark positiv und liegt nah bei Lauf 38.
- Die Zielerwartungsachse bleibt stabil:
  - `target_expectation_holds`: 24 Trades,
    23 TP / 1 SL, ca. +28.66 PnL.
  - `expectation_break_observe`: 9 Trades,
    0 TP / 9 SL, ca. -5.29 PnL.
  - TP-Outcomes:
    `tp_reachability` ca. 0.78,
    `expectation_break_pressure` ca. 0.18,
    `expectation_hold_support` ca. 0.78.
  - SL-Outcomes:
    `tp_reachability` ca. 0.43,
    `expectation_break_pressure` ca. 0.62,
    `expectation_hold_support` ca. 0.46.
- Recovery-Schicht Lauf 39:
  `deep_pullback_recovery_watch` wurde sichtbar,
  markierte aber in diesem Lauf 9 Outcome-Trades,
  alle spaeter SL, ca. -5.01 PnL.
  Im Replay wurden 2 von 4 Exit-Kandidaten als
  `deep_pullback_recovery_watch` markiert,
  beide waren spaeter SL.
  Damit ist die Recovery-Schicht fachlich noch nicht reif,
  aber sie liefert einen wichtigen negativen Befund:
  vorheriger Zielhalt allein reicht nicht,
  um echte Reorganisation von fortgesetztem Bruch zu unterscheiden.
- Fachliche Folgerung aus Lauf 39:
  `deep_pullback_recovery_watch` darf keinesfalls aktiv schuetzen.
  Es braucht zusaetzlich eine echte Rueckkehrbewegung in den Zielpfad,
  also nicht nur vorherige Tragfaehigkeit,
  sondern erkennbare Recovery im aktuellen Verlauf.
  Naechste Diagnoseidee:
  - `target_recovery_momentum`
  - `target_recovery_confirmation`
  - `break_to_recovery_delta`
  - `recovery_after_break_watch`
  Ziel: Reorganisation erst erkennen,
  wenn nach dem Bruch wieder Zielpfad-Staerke entsteht.
- Recovery-Diagnose wurde nach Lauf 39 umgebaut:
  `deep_pullback_recovery_watch` braucht jetzt echte aktuelle
  Rueckkehrbewegung, nicht nur frueheren Zielhalt.
  Neue observe-only Felder:
  - `target_recovery_momentum`
  - `target_recovery_confirmation`
  - `break_to_recovery_delta`
  - `recovery_after_break_watch`
  Die offene Position merkt sich dafuer die letzten Zielpfadwerte
  (`last_tp_reachability`, `last_target_path_integrity`,
  `last_expectation_hold_support`, `last_expectation_break_pressure`,
  `last_current_r`, `last_target_progress`).
  Ziel:
  Ein Reorganisationssignal darf erst entstehen,
  wenn nach einem Bruch wieder messbare Zielpfad-Staerke zurueckkommt.
- Naechster Debug-Fokus Lauf 40:
  Pruefen, ob `deep_pullback_recovery_watch` deutlich seltener auf echte SLs
  faellt und ob `recovery_after_break_watch` auftaucht,
  wenn der Markt nach einem Bruch wieder in Richtung Zielpfad zurueckkehrt.
- Lauf 40 ausgewertet:
  40 Trades, 20 TP / 20 SL, ca. +14.59 PnL,
  Profit Factor ca. 2.29.
  Der Lauf bleibt stark positiv und bestaetigt die Stabilisierung.
- Zielerwartungsachse Lauf 40:
  - `target_expectation_holds`: 20 Trades,
    20 TP / 0 SL, ca. +25.94 PnL.
  - `expectation_break_observe`: 13 Trades,
    0 TP / 13 SL, ca. -7.38 PnL.
  - TP-Outcomes:
    `tp_reachability` ca. 0.78,
    `expectation_break_pressure` ca. 0.18,
    `expectation_hold_support` ca. 0.78.
  - SL-Outcomes:
    `tp_reachability` ca. 0.40,
    `expectation_break_pressure` ca. 0.63,
    `expectation_hold_support` ca. 0.43.
- Recovery-Rueckkehrdiagnose Lauf 40:
  Die strengere Momentum-Bedingung beruhigt die falsche Recovery-Lesung.
  `deep_pullback_recovery_watch` taucht im Outcome/Replay nicht mehr als
  Problem auf.
  Replay: 2 Kandidaten, beide spaeter SL,
  beide `expectation_break_observe`,
  beide haetten Verlust reduziert,
  kein harmed/TP-Cut.
  Damit ist der Umbau gegenueber Lauf 39 fachlich verbessert.
- Offener Punkt:
  `recovery_after_break_watch` wurde noch nicht sichtbar relevant.
  Das ist akzeptabel, weil die Schicht observe-only ist.
  Naechste Laeufe sollten pruefen, ob echte Rueckkehrfaelle spaeter
  auftauchen oder ob die Recovery-Schicht bewusst selten bleiben soll.
- Erweiterter Datensatz / Lauf 41 als Robustheitstest gestartet und
  ausgewertet (`debug/debug_lauf_1` nach Archivierung alter Laeufe):
  107 Trades, 36 TP / 71 SL, ca. +8.10 PnL.
  Der Lauf bleibt positiv, ist aber deutlich schwerer als die kurze
  15-Tage-Laborstrecke.
- Phasenbild Lauf 41:
  - Phase A / bekanntere Pull-Strecke:
    bis ca. Trade 48 Aufbau auf ca. 122.6 Equity,
    ca. +22.61 PnL in dieser Phase.
  - Phase B / Richtungswechsel in laengere Short-/Abwaertsstruktur:
    Trade 49-81 Rueckgang auf ca. 108.3 Equity,
    ca. -14.30 PnL in dieser Phase.
    DIO erkennt fast durchgehend Erwartungsbruch,
    bleibt aber in der fremden neuen Semantik noch verletzlich.
  - Phase C / spaetere Seitwaerts-/Re-Explore-Phase:
    Trade 82-107 seitwaerts um ca. 108-110 Equity,
    ca. -0.21 PnL in dieser Phase.
    DIO wird wieder etwas aktiver/experimenteller,
    aber ohne sprunghaften positiven Aufbau.
- Fachliche Einordnung:
  Die Nutzerbeobachtung ist plausibel:
  DIO trifft zuerst auf bekannte/tragende Strecke,
  baut Equity auf,
  wird beim Regimewechsel zurueckhaltender und flacher,
  erkennt viele Lagen als Erwartungsbruch,
  und beginnt in der spaeteren Seitwaertsphase wieder vorsichtiger zu testen.
  Das spricht fuer Wahrnehmungsanpassung,
  nicht nur fuer eine einfache PnL-Kurve.
- Benennung im MCM-Feld geschaerft:
  Die alte Feldgroessen-Variable wurde in `MCM_FIELD_NEURON` umbenannt.
  Fachlich passt das besser zur aktuellen Zielrichtung,
  weil das MCM-Feld nicht mehr als Agenten-Schwarm,
  sondern als neuronales Wahrnehmungsfeld gelesen wird.
- Neue Erweiterungslogik dokumentiert:
  Kollektive MCM-Erweiterung / DIO-Studienraum / soziale Semantik.
  Forschungsfrage:
  Entwickeln getrennte DIO-Systeme bei gleichen oder aehnlichen Formen
  eigene, moeglicherweise variierende Begriffe,
  und koennen diese ueber Form, Spannung, Tragfaehigkeit,
  Zielerwartung und Outcome uebersetzt werden?
  Vorsichtige Zielformulierung:
  Uebersetzung gleicher Formen bei eventuell variierender Sprache.
  Diese Ebene ist kein aktueller Kernpfad,
  sondern ein spaeterer Forschungszweig nach stabilem Einzel-DIO.
- Die positive Zone/High-Struktur traegt weiterhin.
- Der Rueckgang in Lauf 13/14 entstand vor allem, weil weniger High-Trades
  entstanden und Non-Zone/Low weiter konsequent Verlust erzeugte.
- Lauf 14:
  - Zone: 24 Trades, ca. +12.43 PnL
  - Non-Zone: 15 Trades, 0 TP / 15 SL, ca. -9.55 PnL
- Lauf 15:
  - Zone: 38 Trades, ca. +24.08 PnL
  - Non-Zone: 13 Trades, 0 TP / 13 SL, ca. -8.18 PnL
  - High: 22 Trades, ca. +18.91 PnL
  - Mid: 16 Trades, ca. +5.17 PnL
  - Low: 13 Trades, ca. -8.18 PnL
- Lauf 16:
  - Zone: ca. +23.16 PnL
  - Non-Zone: 20 Trades, 0 TP / 20 SL, ca. -12.05 PnL
  - High: ca. +21.38 PnL
  - Mid: ca. +1.78 PnL
  - Low: ca. -12.05 PnL
- Lauf 17:
  - Gesamt: 42 Trades, 20 TP / 22 SL, ca. +12.09 PnL
  - Zone: 27 Trades, ca. +20.15 PnL
  - Non-Zone: 15 Trades, ca. -8.07 PnL
- Lauf 18:
  - Gesamt: 37 Trades, 19 TP / 18 SL, ca. +14.19 PnL
  - Zone: 26 Trades, ca. +20.27 PnL
  - Non-Zone: 11 Trades, 0 TP / 11 SL, ca. -6.08 PnL
- Lauf 19:
  - Gesamt: 41 Trades, 20 TP / 21 SL, ca. +13.67 PnL
  - Zone: 30 Trades, ca. +19.66 PnL
  - Non-Zone: 11 Trades, 0 TP / 11 SL, ca. -6.00 PnL
  - Beobachtungslernen:
    - `low_observations`: 948
    - `resolved`: 948
    - `saved_loss`: 519
    - `missed_gain`: 424
    - `neutral`: 5
    - `observation_maturity_trust`: ca. 0.549
    - `observation_action_pressure`: ca. 0.447
- Lauf 20:
  - Gesamt: 47 Trades, 22 TP / 25 SL, ca. +12.64 PnL
  - Zone: 37 Trades, ca. +19.84 PnL
  - Non-Zone: 10 Trades, 0 TP / 10 SL, ca. -7.20 PnL
  - Beobachtungslernen:
    - `low_observations`: 903
    - `resolved`: 891
    - `saved_loss`: 507
    - `missed_gain`: 378
    - `neutral`: 6
    - `observation_maturity_trust`: ca. 0.571
    - `observation_action_pressure`: ca. 0.424
- Lauf 21:
  - Gesamt: 46 Trades, 20 TP / 26 SL, ca. +10.30 PnL
  - Zone: 30 Trades, ca. +18.55 PnL
  - Non-Zone: 16 Trades, ca. -8.25 PnL
  - Beobachtungslernen:
    - `low_observations`: 1026
    - `resolved`: 1013
    - `saved_loss`: 566
    - `missed_gain`: 440
    - `neutral`: 7
    - `observation_maturity_trust`: ca. 0.561
    - `observation_action_pressure`: ca. 0.434
- Lauf 22:
  - Gesamt: 40 Trades, 14 TP / 26 SL, ca. +1.67 PnL
  - Zone: 25 Trades, ca. +11.24 PnL
  - Non-Zone: 15 Trades, 0 TP / 15 SL, ca. -9.56 PnL
  - Beobachtungslernen:
    - `low_observations`: 1040
    - `resolved`: 1040
    - `saved_loss`: 548
    - `missed_gain`: 487
    - `neutral`: 5
    - `observation_maturity_trust`: ca. 0.529
    - `observation_action_pressure`: ca. 0.468
- Lauf 23:
  - Gesamt: 41 Trades, 21 TP / 20 SL, ca. +16.13 PnL
  - Zone: 34 Trades, ca. +20.09 PnL
  - Non-Zone: 7 Trades, 0 TP / 7 SL, ca. -3.96 PnL
  - Equity-Peak: ca. +18.28 nach Trade 37
  - Ruecklauf vom Peak bis Schluss: ca. -2.15
  - Beobachtungslernen:
    - `low_observations`: 963
    - `resolved`: 956
    - `saved_loss`: 528
    - `missed_gain`: 423
    - `neutral`: 5
    - `observation_maturity_trust`: ca. 0.554
    - `observation_action_pressure`: ca. 0.442
- Lauf 24:
  - Gesamt: 39 Trades, 17 TP / 22 SL, ca. +7.05 PnL
  - Zone: 28 Trades, ca. +14.79 PnL
  - Non-Zone: 11 Trades, 0 TP / 11 SL, ca. -7.74 PnL
  - `matured_exits`: 0
  - keine `matured_exit_observe`-Ereignisse gefunden
  - Beobachtungslernen:
    - `low_observations`: 1095
    - `resolved`: 1086
    - `saved_loss`: 601
    - `missed_gain`: 480
    - `neutral`: 5
    - `observation_maturity_trust`: ca. 0.555
    - `observation_action_pressure`: ca. 0.442
- Lauf 25:
  - Gesamt: 43 Trades, 21 TP / 22 SL, ca. +12.76 PnL
  - Zone: 31 Trades, ca. +21.39 PnL
  - Non-Zone: 12 Trades, 0 TP / 12 SL, ca. -8.62 PnL
  - Equity-Peak: ca. +14.38 nach Trade 40
  - Ruecklauf vom Peak bis Schluss: ca. -1.61
  - `matured_exits`: 0, weil `observe` nicht aktiv schliesst
  - `matured_exit_debug.csv`: 7 gereifte Exit-Beobachtungen
  - Beobachtungslernen:
    - `low_observations`: 1053
    - `resolved`: 1039
    - `saved_loss`: 578
    - `missed_gain`: 453
    - `neutral`: 8
    - `observation_maturity_trust`: ca. 0.559
    - `observation_action_pressure`: ca. 0.436
- Lauf 26:
  - Gesamt: 39 Trades, 14 TP / 25 SL, ca. +2.99 PnL
  - Zone: 26 Trades, ca. +10.17 PnL
  - Non-Zone: 13 Trades, 0 TP / 13 SL, ca. -7.18 PnL
  - Equity-Peak: ca. +5.67 nach Trade 31
  - Ruecklauf vom Peak bis Schluss: ca. -2.68
  - `matured_exits`: 0, weil `observe` nicht aktiv schliesst
  - `matured_exit_debug.csv`: 11 gereifte Exit-Beobachtungen
  - Signalabgleich:
    - 6 Signale lagen vor spaeteren SL-Outcomes, verteilt auf 4 Trades.
    - 5 Signale lagen vor spaeteren TP-Outcomes, verteilt auf 2 Trades.
    - Damit erkennt die Exit-Reife reale Schutzmomente, ist aber noch nicht
      reif genug fuer aktive Ausfuehrung.
  - Beobachtungslernen:
    - `low_observations`: 1138
    - `resolved`: 1121
    - `saved_loss`: 627
    - `missed_gain`: 489
    - `neutral`: 5
    - `observation_maturity_trust`: ca. 0.561
    - `observation_action_pressure`: ca. 0.436
- Lauf 27:
  - Modus: `MCM_MATURED_EXIT_MODE = "active"`
  - Gesamt: 33 Trades, ca. +1.93 PnL
  - Klassische Outcomes:
    - 7 `tp_hit`, ca. +8.67 PnL
    - 11 `sl_hit`, ca. -6.07 PnL
  - Gereifte Exits:
    - 15 `matured_exit`
    - 5 positiv, 10 negativ
    - Netto aus `outcome_records`: ca. -0.67 PnL
  - Zone:
    - 22 Trades, ca. +3.93 PnL
    - davon 8 gereifte Exits
  - Non-Zone:
    - 11 Trades, ca. -2.00 PnL
    - davon 7 gereifte Exits
  - Equity-Peak: ca. +3.88 nach Trade 23
  - Ruecklauf vom Peak bis Schluss: ca. -1.95
  - Interpretation:
    - Active-Exit ist noch zu frueh.
    - DIO beendet zu viele Positionen aus einzelner Exit-Wahrnehmung.
    - Es entsteht Schutz, aber nicht genug Reife/Unterscheidung zwischen
      echter Gefahr und normaler Gewinnatmung.
- Lauf 28:
  - Modus: `MCM_MATURED_EXIT_MODE = "observe"`
  - Gesamt: 49 Trades, 20 TP / 29 SL, ca. +8.90 PnL
  - Zone: 37 Trades, ca. +15.81 PnL
  - Non-Zone: 12 Trades, 0 TP / 12 SL, ca. -6.91 PnL
  - Equity-Peak: ca. +15.53 nach Trade 34
  - Ruecklauf vom Peak bis Schluss: ca. -6.63
  - `matured_exit_debug.csv`: 8 Exit-Reife-Beobachtungen
  - `matured_exits`: 0, weil `observe` nicht aktiv schliesst
  - Beobachtungslernen:
    - `low_observations`: 919
    - `resolved`: 910
    - `saved_loss`: 492
    - `missed_gain`: 411
    - `neutral`: 7
    - `observation_maturity_trust`: ca. 0.543
    - `observation_action_pressure`: ca. 0.452
  - Positionslast-Diagnose gegen Outcomes:
    - `plan_holding_trust`: 23 Trades, 20 TP / 3 SL, ca. +23.43 PnL
    - `exit_nervousness_observe`: 24 Trades, 0 TP / 24 SL, ca. -13.51 PnL
    - `quiet_position_watch`: 2 Trades, 0 TP / 2 SL, ca. -1.02 PnL
  - Interpretation:
    - Die neue Diagnoseschicht trennt gute Haltephasen und belastete
      Verlustphasen deutlich.
    - `intervention_fitness` bleibt bei den reinen Exit-Reife-Beobachtungen
      niedrig bis mittel. Das passt zur These:
      DIO spuert Exit-Spannung, ist aber noch nicht reif genug fuer aktives
      Schliessen.
- Lauf 29:
  - Modus: `MCM_MATURED_EXIT_MODE = "observe"`
  - Gesamt: 36 Trades, 14 TP / 22 SL, ca. +5.81 PnL
  - Zone: 27 Trades, ca. +10.89 PnL
  - Non-Zone: 9 Trades, 0 TP / 9 SL, ca. -5.08 PnL
  - Equity-Peak: ca. +5.98 nach Trade 29
  - Ruecklauf vom Peak bis Schluss: ca. -0.17
  - `matured_exit_debug.csv`: 4 Exit-Reife-Beobachtungen
  - `matured_exits`: 0, weil `observe` nicht aktiv schliesst
  - Beobachtungslernen:
    - `low_observations`: 1061
    - `resolved`: 1061
    - `saved_loss`: 581
    - `missed_gain`: 473
    - `neutral`: 7
    - `observation_maturity_trust`: ca. 0.550
    - `observation_action_pressure`: ca. 0.446
  - Positionslast-Diagnose:
    - `exit_nervousness_observe`: 20 Trades, 0 TP / 20 SL, ca. -11.02 PnL
    - `plan_holding_trust`: 14 Trades, 14 TP / 0 SL, ca. +18.07 PnL
    - `quiet_position_watch`: 2 Trades, 0 TP / 2 SL, ca. -1.25 PnL
  - Exit-Kandidaten:
    - `exit_candidate_observe` im Outcome-Kontext:
      13 Trades, 0 TP / 13 SL, ca. -7.37 PnL
    - konkrete Kandidaten-Events im Protokoll:
      3 echte Kandidaten, alle vor spaeteren SLs
    - `plan_trust_holds`:
      21 Trades, 14 TP / 7 SL, ca. +14.29 PnL
    - `exit_pressure_unfit_observe`:
      1 Trade, spaeter SL, ca. -0.55 PnL
  - Interpretation:
    - Der Lauf ist schwacher als erwartet, aber die neue Kandidatenschicht
      zeigt nicht in die falsche Richtung.
    - Sie markiert keine spaeteren TPs als echte Exit-Kandidaten.
    - Der Rueckgang entsteht eher durch weniger Gesamttrades und weniger
      Zone-PnL gegen Lauf 28, nicht durch einen falschen aktiven Exit.
- Denk-/Memory-Last steigt leicht weiter:
  - `memory_compare_load` ca. 0.905 -> 0.913 -> 0.939 -> 0.935
  - `blind_thinking_load` ca. 0.440 -> 0.443 -> 0.450 -> 0.451
  - `learning_trust` steigt ca. 0.051 -> 0.062 -> 0.069 -> 0.075
  - `caution_trust` steigt ca. 0.009 -> 0.012 -> 0.013 -> 0.015

Interpretation:

Das System lernt und bindet Erfahrung. Die starke Erholung in Lauf 15 zeigt,
dass die Trust-/Formsprache nicht nur daempft, sondern tragende Erfahrung wieder
in Handlung bringen kann. Gleichzeitig uebertraegt es in fremden oder nicht
tragenden Strukturen noch zu viel Handlungsfaehigkeit. Genau hier passt der
neue Bauplanpunkt `Transfer-Tragfaehigkeit fremder Strukturen`: Erfahrung soll
nicht hart blockieren, aber sie darf bei geringer Tragfaehigkeit nicht voll in
Handlung uebersetzt werden.

Naechster technischer Schritt waere deshalb keine starre Low-Sperre,
sondern eine weiche Transfer-Tragfaehigkeitsachse:

- Wie fremd ist die aktuelle Struktur?
- Welche Erfahrungsinseln resonieren trotzdem?
- Wie viel davon traegt wirklich?
- Wird daraus Beobachtung/Reframing oder kontrollierte Handlung?

Neu konzeptionell ergaenzt ist ausserdem
`Reifeentwicklung durch Beobachtungslernen`:

- Low/Non-Zone soll nicht als harter Verbotsbereich verstanden werden,
  aber als Hinweis auf geringe Tragfaehigkeit.
- Reiferes Verhalten bedeutet, unsichere Lage beobachten zu koennen,
  statt sie durch Aktion testen zu muessen.
- Beobachtung soll selbst Erfahrung werden:
  Was waere passiert, wenn gehandelt worden waere?
- Dadurch kann das System lernen, ohne jeden unsicheren Zustand
  ueber direkten Trade-Schmerz erfahren zu muessen.
- Dokumentiert in README und Umsetzungsplan.

Jetzt technisch umgesetzt:

- `TradeStats` fuehrt eine Beobachtungslernspur:
  - `pending_observations`
  - `observation_learning`
  - `recent_observation_learning`
- Beobachtete Low-/Non-Zone-Situationen mit vorhandenem virtuellem Tradeplan
  werden weiterverfolgt.
- Spaetere Preisbewegung bewertet, ob Zusehen:
  - Verlust gespart haette (`saved_loss`)
  - Gewinn verpasst haette (`missed_gain`)
  - neutral blieb (`neutral`)
- Daraus entstehen:
  - `observation_maturity_trust`
  - `observation_action_pressure`
  - `observation_low_count`
- Diese Werte fliessen weich in die Entscheidung:
  - mehr `saved_loss` staerkt Beobachtungsreife
  - mehr `missed_gain` erzeugt kleinen Handlungs-Gegendruck
  - keine harte Low-Sperre
- `mcm_memory_thinking_protocol.csv` schreibt die neuen Reifewerte mit.

Syntaxpruefung erfolgreich:

- `python -m py_compile trade_stats.py MCM_Brain_Modell.py bot.py`

Mini-Simulation erfolgreich:

- beobachtete Low-Situation wurde nach spaeterem Preis als `saved_loss`
  bewertet
- `maturity_trust` stieg in diesem Mini-Fall auf `1.0`

Nach Lauf 16 geprueft:

- Die neue Beobachtungslernspur war technisch vorhanden, griff aber im echten
  Lauf noch nicht:
  - `low_observations`: 0
  - `saved_loss`: 0
  - `missed_gain`: 0
  - `observation_maturity_trust`: 0.0
- Grund: beobachtete Low-/Non-Zone-Situationen wurden im Attempt-Kontext oft
  als `WAIT` mit Entry/SL/TP = 0 gespeichert.
- Dadurch konnte das System zwar "zusehen", aber nicht auswerten,
  was bei hypothetischem Handeln passiert waere.
- Das war kein Konzeptfehler, sondern eine fehlende virtuelle Handlungsbahn
  fuer Beobachtung.

Direkt korrigiert:

- Nicht freigegebene LONG-/SHORT-Tendenzen erzeugen jetzt einen
  `virtual_observation_plan`.
- Der Attempt-Kontext bekommt fuer Beobachtung eine `proposed_decision`,
  auch wenn die reale Entscheidung `WAIT` bleibt.
- Beobachtungslernen kann dadurch ab dem naechsten Lauf Low-/Non-Zone-Lagen
  virtuell verfolgen und spaeter als `saved_loss`, `missed_gain` oder `neutral`
  bewerten.
- Wichtig: Es bleibt organisch und weich. Es entsteht keine harte Low-Sperre,
  sondern eine Reifeschicht: Zusehen kann als eigene Erfahrung tragfaehig werden.

Nach Lauf 17 erneut geprueft:

- PnL und Tradezahl verbesserten sich gegen Lauf 16:
  - Lauf 16: ca. +11.11 PnL, 54 Trades
  - Lauf 17: ca. +12.09 PnL, 42 Trades
- Die Beobachtungslernspur blieb aber weiterhin bei 0:
  - `low_observations`: 0
  - `saved_loss`: 0
  - `missed_gain`: 0
  - `observation_maturity_trust`: 0.0
- Diagnose:
  - In den Attempt-Daten stand bei Observe/Withhold teils
    `meta_regulation_state.decision = LONG/SHORT`.
  - Gleichzeitig blieb `trade_plan.decision = WAIT` und Entry/SL/TP = 0.
  - Ursache war eine spaetere Ueberschreibung von `proposed_decision` aus
    `decision`. Bei reifem Beobachten ist `decision` aber bewusst `WAIT`.
- Nachkorrektur:
  - `proposed_decision` wird jetzt zuerst aus `runtime_result.proposed_decision`
    gelesen und nur danach aus `decision`.
  - Dadurch bleiben aeussere Handlung (`WAIT`) und innere Beobachtungsrichtung
    (`LONG`/`SHORT`) getrennt.
- Lauf 18 ist damit der erste echte Kontrolllauf fuer die volle
  Beobachtungslernmechanik.

Nach Lauf 18 geprueft:

- Das Verhalten wurde besser:
  - weniger Trades
  - hoeherer Netto-PnL als Lauf 16/17
  - weniger Non-Zone-Verlust
- Die Beobachtungslernspur blieb aber erneut bei 0.
- Diagnose:
  - Non-Zone-Observe/Withhold/Skip kam im Attempt-Kontext weiter als
    `WAIT` ohne Entry/SL/TP an.
  - Teilweise gab es nur noch ein schwaches Signalbild, aber keine
    explizite innere LONG-/SHORT-Hypothese.
  - Aus organismischer Sicht heisst das:
    Das System spuert geringe Tragfaehigkeit, formuliert aber noch nicht
    immer eine beobachtbare innere Handlungshypothese.
- Nachkorrektur:
  - Der Attempt-Kontext fuehrt jetzt `world_state.current_price` und
    `world_state.candle_state` mit.
  - `TradeStats` kann fuer Non-Zone-Observe/Withhold/Skip aus Signalspannung
    und aktuellem Preis eine virtuelle Beobachtungshypothese ableiten.
  - Das erzeugt keine echte Handlung, sondern nur eine Lernspur:
    Was waere passiert, wenn diese innere Richtung gehandelt worden waere?
- Mini-Mechaniktest erfolgreich:
  - Non-Zone + Observe + Preis + Signal erzeugt jetzt
    `low_observations = 1` und eine offene Beobachtung.
- Lauf 19 ist damit der erste echte Kontrolllauf fuer die signalbasierte
  Beobachtungslernspur.

Nach Lauf 19 geprueft:

- Der Beobachtungslernkanal funktioniert jetzt real im Backtest.
- Es wurden 948 Low-/Non-Zone-Beobachtungen erzeugt und aufgeloest.
- Mehr als die Haelfte der hypothetischen Low-Handlungen haette Verlust
  gespart (`saved_loss`: 519).
- Ein grosser Anteil haette aber auch Gewinn verpasst (`missed_gain`: 424).
- Interpretation:
  - Low/Non-Zone ist nicht einfach "schlecht".
  - Low/Non-Zone ist ein instabiler Spannungsraum.
  - Das System lernt dort jetzt nicht nur Vermeidung, sondern Ambivalenz:
    Zusehen kann reif sein, kann aber auch Chancen kosten.
- Die bisherige Kopplung ist deshalb fachlich passend vorsichtig:
  - `maturity_trust` staerkt Beobachtungsreife.
  - `action_pressure` erzeugt Gegenspannung, wenn Zusehen zu viel Gewinn
    verpasst haette.
- Keine direkte Code-Nachschaerfung nach Lauf 19:
  - Das war der erste echte Aktivierungslauf.
  - Eine sofortige Drosselung wuerde zu frueh auf einen einzelnen Lauf
    reagieren.
  - Lauf 20 soll zeigen, ob die neue Reifeschicht stabil lernt oder zu viel
    Ambivalenz/Handlungsdruck erzeugt.

Nach Lauf 20 geprueft:

- Die Beobachtungslernspur ist stabil:
  - `maturity_trust` steigt von ca. 0.549 auf ca. 0.571
  - `action_pressure` faellt von ca. 0.447 auf ca. 0.424
- Gleichzeitig steigt die Tradezahl von 41 auf 47.
- Die Zone traegt weiter stabil, aber mit mehr SL-Anteil.
- Non-Zone bleibt bei 0 TP und 10 SL negativ.
- Interpretation:
  - Das System bildet jetzt Beobachtungsreife.
  - Diese Reife wird im Brain aber noch zu schwach in reale Zurueckhaltung,
    Beobachtung oder Replan uebersetzt.
  - Es fehlt nicht mehr die Lernspur, sondern die Reife-Kopplung ist noch zu
    zart.

Direkt nachgeschaerft:

- `observation_maturity_balance` wurde ergaenzt:
  - `maturity_trust - action_pressure`
  - nur positive Balance wirkt als Reifedruck.
- Die Kopplung bleibt weich:
  - etwas weniger `act_push`
  - etwas mehr `observe_pull`
  - minimal mehr `replan_pull`
- Keine harte Low-/Non-Zone-Sperre.
- Ziel fuer Lauf 21:
  - weniger unreife Handlung bei weiterhin freier Zone
  - stabilere Non-Zone-Reduktion
  - keine komplette Unterdrueckung von Chancen, weil `action_pressure`
    weiter als Gegenspannung erhalten bleibt.

Nach Lauf 21 geprueft:

- Der PnL-Rueckgang ist real und relevant.
- Die Reifespur selbst bleibt aktiv:
  - viele Low-Beobachtungen
  - mehr `saved_loss` als `missed_gain`
  - aber weiter deutliche Ambivalenz.
- Die globale Reife-Kopplung war fachlich zu breit:
  - Sie kann gute Zone-Handlungen mitdaempfen.
  - Gleichzeitig loest sie das eigentliche Problem nicht vollstaendig:
    Viele negative Non-Zone-Outcomes entstehen offenbar nicht nur durch
    direkten Non-Zone-Einstieg, sondern durch Strukturkippen waehrend
    offener Positionen.
- Neue Korrektur:
  - `observation_maturity_balance` bleibt erhalten.
  - Neu ist `observation_maturity_scope`.
  - Die Reife-Balance wirkt jetzt nur stark, wenn die aktuelle
    Strukturtragfaehigkeit niedrig ist.
  - Daraus entsteht `observation_scoped_balance`.
- Ziel:
  - Zone/tragende Struktur weniger pauschal bremsen.
  - Low-/Non-Zone-Spannung staerker in Observe/Replan uebersetzen.
  - Keine harte Sperre, sondern kontextabhaengige Reiferegulation.
- Zusaetzlicher Befund:
  - Das naechste groessere Thema ist wahrscheinlich nicht nur Entry-Reife,
    sondern Halte-/Exit-Reife:
    Was passiert, wenn eine Position tragend startet, aber das Feld waehrend
    der offenen Position in Non-Zone kippt?

Nach Lauf 22 geprueft:

- Der scoped Reife-Fix war nicht tragfaehig.
- PnL faellt stark auf ca. +1.67.
- Ursache in der Auswertung:
  - Zone-PnL bricht von ca. +18.55 auf ca. +11.24 ein.
  - Non-Zone-Verlust steigt auf ca. -9.56.
  - Die Tradezahl sinkt, aber die Qualitaet der verbleibenden Trades faellt.
- Technischer Befund:
  - `observation_maturity_scope` stand auch bei hoher realer
    `structure_quality` oft fast auf 1.0.
  - Damit war die Reifewirkung weiterhin zu breit und nicht sauber an echte
    Low-/Non-Zone-Struktur gebunden.
- Korrektur:
  - `observation_maturity_scope` wird jetzt aus der realen aktuellen
    `structure_perception_state.structure_quality` berechnet.
  - Nur wenn diese reale Strukturqualitaet niedrig ist, wirkt die Reife-Balance
    stark.
  - Tragende Zone soll dadurch weniger pauschal gedämpft werden.
- Lauf 23 muss pruefen, ob die scoped Reife jetzt wirklich lokal wirkt.

Nach Lauf 23 geprueft:

- Der reale Struktur-Scope funktioniert deutlich besser:
  - durchschnittlicher `observation_maturity_scope`: ca. 0.121
  - bei tragender Struktur ist der Scope haeufig 0
  - `observation_scoped_balance` wirkt nur noch lokal stark
- Zone erholt sich auf ca. +20.09 PnL.
- Non-Zone-Verlust sinkt stark auf ca. -3.96.
- Gesamt-PnL steigt auf ca. +16.13.
- Der Lauf war zwischenzeitlich noch profitabler:
  - Peak ca. +18.28
  - Schluss ca. +16.13
  - Ruecklauf ca. -2.15 am Ende
- Interpretation:
  - Entry-Reife / Low-Regulation wirkt jetzt deutlich besser.
  - Der naechste Engpass ist wahrscheinlich Halte-/Exit-Reife:
    Wenn das System bereits deutlich im Gewinn ist oder eine offene Position
    spaeter Struktur verliert, braucht es eine reifere Sicherungs- oder
    Reorganisationsreaktion.
- Keine weitere Entry-Daempfung nach Lauf 23.
- Naechster sinnvoller Schritt:
  Halte-/Exit-Reife als eigene weiche Schicht vorbereiten:
  - Peak-Gewinn nicht starr sichern
  - aber Rueckgabe nach Strukturkippen wahrnehmen
  - offene Positionen bei sinkender Tragfaehigkeit beobachten/reduzieren/
    frueher verlassen koennen
  - ohne gute Trendfortsetzung abzuwuergen

Neu vorbereitet:

- Halte-/Exit-Reife besitzt jetzt einen Schalter in `config.py`:
  - `MCM_MATURED_EXIT_MODE = "fixed"`
  - `"fixed"`: nur klassisches TP/SL-Auslaufen
  - `"observe"`: gereifte Exit-Reife wird nur protokolliert, aber nicht
    ausgefuehrt
  - `"active"`: gereifte Exit-Entscheidung darf im Backtest eine Position
    schliessen
- Standard bleibt bewusst `fixed`.
- Die Mechanik bewertet offene Positionen ueber:
  - bisherigen maximalen Gewinnlauf (`mfe_r`)
  - Rueckgabe vom Peak (`giveback_r`)
  - aktuelle Strukturqualitaet
  - Druck/Kapazitaets-Verhaeltnis
  - Recovery-/Tragfaehigkeitslage
- Fester TP/SL-Exit hat weiterhin Vorrang.
- Im Live-Modus wird ein gereifter Exit aus Sicherheitsgruenden noch nicht
  automatisch ausgefuehrt, sondern nur als Reife-Ereignis beobachtbar.
- `TradeStats` kann `matured_exit` mit echtem Exit-Preis abrechnen und als
  eigenes Outcome sichtbar machen.

Nach Lauf 24 geprueft:

- `observe` hat keine echten Exits ausgefuehrt, wie gewuenscht.
- Es wurden aber auch keine gereiften Exit-Beobachtungen erzeugt.
- Ursache:
  - Die erste Exit-Reife-Schwelle war zu streng.
  - Zudem war die Positionslage in den Outcome-Kontexten noch nicht ausreichend
    sichtbar, um MFE/MAE/Rueckgabe nachtraeglich sauber zu bewerten.
- Nachkorrektur:
  - `MCM_MATURED_EXIT_MIN_MFE_R` von 1.00 auf 0.70 gesenkt.
  - `MCM_MATURED_EXIT_GIVEBACK_R` von 0.35 auf 0.25 gesenkt.
  - `position_watch_state` fuehrt jetzt MFE, MAE, Risiko, MFE-R, MAE-R,
    Fill-Ratio und Bars-open im Exit-Kontext.
  - `matured_exit_debug.csv` wird geschrieben, wenn Exit-Reife erkannt wird.
- Lauf 25 im Modus `observe` soll jetzt zeigen, ob Exit-Reife ueberhaupt
  diagnostisch sichtbar wird.

Nach Lauf 25 geprueft:

- `observe` hat weiterhin keine echten Exits ausgefuehrt, wie gewuenscht.
- Die Exit-Reife ist jetzt diagnostisch sichtbar:
  - 7 Eintraege in `matured_exit_debug.csv`
  - typische Signale: Gewinnlauf vorhanden, Rueckgabe vom Peak sichtbar,
    Strukturqualitaet teils nur mittel, Druck/Kapazitaet erhoeht
- Lauf 25 schliesst mit ca. +12.76 PnL und liegt damit deutlich ueber Lauf 24.
- Zone bleibt der tragende Kern:
  - 31 Zone-Trades, ca. +21.39 PnL
  - 12 Non-Zone-Trades, 0 TP / 12 SL, ca. -8.62 PnL
- Nachkorrektur:
  - `matured_exit_debug.csv` schreibt ab dem naechsten Lauf zusaetzlich
    Timestamp, Entry, TP, SL und Risiko.
  - Damit kann Lauf 26 sauberer zeigen, ob ein gereifter Exit spaetere
    SLs verhindert haette oder gute TP-Laeufe zu frueh gekappt haette.

Naechster Lauf muss deshalb besonders pruefen:

- ob die 7 Exit-Reife-Signale aus Lauf 25 reproduzierbar bleiben
- ob Exit-Reife eher vor spaeterem SL, vor Gewinnrueckgabe oder vor normalem TP
  entsteht
- ob Non-Zone weiter 0 TP / alle SL bleibt
- ob die Zone frei genug handeln darf

Nach Lauf 26 geprueft:

- Die Exit-Reife-Signale sind reproduzierbar und steigen von 7 auf 11.
- Die Signale sind fachlich nicht leer:
  - bei 4 spaeteren SL-Trades haette ein gereifter Exit Schaden reduziert
  - bei 2 spaeteren TP-Trades haette ein gereifter Exit Gewinn zu frueh
    begrenzt
- Daraus folgt:
  - `active` ist noch zu frueh
  - die Exit-Reife braucht eine Bestaetigungsschicht, z.B. wiederholte
    Verschlechterung ueber mehrere Bars, negativer `current_r`, sinkende
    Strukturtragfaehigkeit oder steigender Druck/Kapazitaets-Konflikt
  - ein einzelnes Exit-Reife-Signal darf nur Wahrnehmung sein, noch keine
    Handlung

Nach Lauf 27 geprueft:

- Der versehentliche Active-Lauf bestaetigt die Diagnose aus Lauf 26.
- `matured_exit` wurde 15-mal ausgefuehrt.
- Netto waren die gereiften Exits nach Outcome-Protokoll negativ.
- `MCM_MATURED_EXIT_MODE` wurde wieder auf `observe` gesetzt.
- Statistik-Korrektur:
  - `matured_exit_pnl` wurde bisher brutto vor Gebuehren gezaehlt.
  - Ab jetzt wird `matured_exit_pnl` netto nach Gebuehren gezaehlt, passend zu
    `outcome_records`.
- Naechster Schritt bleibt:
  - Exit-Reife nur beobachten
  - Bestaetigungsschicht bauen
  - erst danach wieder ein `active`-Experiment

Fachliche Ergaenzung nach Lauf 27:

- Offene Positionen erzeugen eine eigene kognitive und regulatorische Last.
- Das laufende Neubewerten waehrend einer Position ist nicht kostenlos.
- Ein fester TP/SL ist deshalb auch eine Entlastungs- und Haltestruktur.
- Hohe innere Belastung darf nicht automatisch zu Exit-Handlung fuehren.
- In bestimmten Lagen ist die reifere Reaktion:
  - Ich sehe Spannung.
  - Ich fuehle Belastung.
  - Aber mein aktueller innerer Zustand traegt keine neue Entscheidung.
  - Also greife ich nicht ein und lasse den vorherigen Plan laufen.
- Dokumentiert in:
  - `files/UMSETZUNGSPLAN.md` als `Positionslast und reife Nicht-Intervention`
  - `README.md` als `Positionslast und Nicht-Intervention`

Technisch jetzt vorbereitet:

- Offene Positionen fuehren eine neue Diagnose `position_intervention_state`.
- Sichtbar werden:
  - `position_cognitive_load`
  - `exit_decision_pressure`
  - `holding_stability`
  - `plan_trust`
  - `intervention_fatigue`
  - `inner_noise`
  - `intervention_fitness`
  - `intervention_unfit_state`
  - `exit_evidence`
  - `sustained_exit_pressure`
- Diese Werte werden in Exit-Kontexte, Position-Updates und Outcome-Kontexte
  geschrieben.
- Neues Debug-Protokoll:
  - `debug/mcm_position_intervention_protocol.csv`
- Wichtig:
  - Diese Schicht ist diagnostisch.
  - Sie schliesst keine Position.
  - Sie soll im naechsten Lauf zeigen, ob Exit-Reife eher aus echter
    Strukturverschlechterung oder aus innerer Exit-Nervositaet entsteht.

Nach Lauf 28 geprueft:

- Die neue Positionslast-Diagnose ist fachlich aussagekraeftig.
- `plan_holding_trust` markiert ueberwiegend die Trades, die bis TP laufen
  sollten.
- `exit_nervousness_observe` markiert alle finalen Verlusttrades dieses Laufs.
- Daraus folgt:
  - die neue Schicht sollte nicht einfach aktive Exits ausloesen
  - sie kann aber als Bestaetigungsschicht fuer spaetere Exit-Kandidaten dienen
  - naechster Schritt waere eine sehr vorsichtige Exit-Kandidatenlogik:
    nur wenn Exit-Nervositaet, niedriger Plan-Trust, sinkende Haltestabilitaet
    und ausreichend hohe Interventionseignung zusammenkommen

Jetzt technisch vorbereitet:

- Neue reine Beobachtungsschicht `exit_candidate_observe_state`.
- Sie entsteht nur aus gekoppelter Bestaetigung:
  - `exit_decision_pressure` hoch genug
  - `plan_trust` niedrig genug
  - `holding_stability` schwach genug
  - `intervention_fitness` ausreichend
  - `exit_evidence` ausreichend
  - `intervention_unfit_state` nicht dominierend
- Neues Debug-Protokoll:
  - `debug/mcm_exit_candidate_observe.csv`
- Neue Config-Schwellen:
  - `MCM_EXIT_CANDIDATE_MIN_PRESSURE`
  - `MCM_EXIT_CANDIDATE_MAX_PLAN_TRUST`
  - `MCM_EXIT_CANDIDATE_MAX_HOLDING_STABILITY`
  - `MCM_EXIT_CANDIDATE_MIN_FITNESS`
  - `MCM_EXIT_CANDIDATE_MIN_EVIDENCE`
- Wichtig:
  - Diese Schicht ist weiter nur diagnostisch.
  - Sie schliesst keine Position.
  - Lauf 29 soll pruefen, ob `exit_candidate_observe` vor spaeteren SLs
    entsteht, ohne spaetere TPs zu markieren.

Nach Lauf 29 geprueft:

- `exit_candidate_observe` hat den ersten Härtetest bestanden.
- Echte Kandidatenereignisse lagen vor spaeteren SLs.
- In den Outcome-Kontexten lagen alle `exit_candidate_observe`-Markierungen
  ebenfalls auf spaeteren SL-Trades.
- Es gab keine TP-Zerstoerung durch die Kandidatenschicht, weil weiter nur
  beobachtet wurde.
- Noch offen:
  - Die Kandidatenlogik ist moeglicherweise streng genug, aber noch zu spaet
    oder zu selten.
  - Vor aktiver Nutzung braucht es mindestens einen weiteren Observe-Lauf.
  - Danach kann ein hypothetisches Kandidaten-PnL-Protokoll gebaut werden:
    Was waere passiert, wenn nur `exit_candidate_observe` geschlossen haette?

Nach Lauf 30 geprueft:

- Gesamt:
  - 33 Trades, 16 TP / 17 SL
  - Netto-PnL ca. +11.60
  - Profit Factor ca. 2.27
  - Max Drawdown ca. 2.21
- Struktur:
  - Zone: 28 Trades, 16 TP / 12 SL, ca. +14.30 PnL
  - Non-Zone: 5 Trades, 0 TP / 5 SL, ca. -2.71 PnL
  - High: 13 Trades, ca. +9.79 PnL
  - Mid: 15 Trades, ca. +4.52 PnL
  - Low: 5 Trades, ca. -2.71 PnL
- Positionslast-Diagnose:
  - `plan_holding_trust`: 16 Trades, 16 TP / 0 SL, ca. +20.75 PnL
  - `exit_nervousness_observe`: 17 Trades, 0 TP / 17 SL, ca. -9.16 PnL
- Exit-Kandidaten gegen Outcomes:
  - `exit_candidate_observe`: 7 Trades, 0 TP / 7 SL, ca. -3.88 PnL
  - `plan_trust_holds`: 22 Trades, 16 TP / 6 SL, ca. +17.61 PnL
  - `exit_pressure_unfit_observe`: 2 Trades, 0 TP / 2 SL, ca. -1.03 PnL
  - `no_exit_candidate`: 2 Trades, 0 TP / 2 SL, ca. -1.09 PnL
- Kandidatenprotokoll:
  - 1 echtes `exit_candidate_observe`-Ereignis im Protokoll
  - dieses lag ebenfalls vor einem spaeteren SL
  - `matured_exit_debug.csv` enthielt 10 gereifte Exit-Beobachtungen,
    aber keine davon wurde als echter Exit-Kandidat bestaetigt
- Interpretation:
  - Lauf 30 bestaetigt Lauf 29, aber mit deutlich besserem Gesamtergebnis.
  - Die Kandidatenschicht markiert weiter keine spaeteren TP-Trades als echte
    Exit-Kandidaten.
  - `plan_holding_trust` ist aktuell die klarste Reife-Spur:
    wenn Planvertrauen und Haltestabilitaet tragen, sollte DIO nicht eingreifen.
  - `exit_candidate_observe` ist noch kein aktiver Exit, aber ein ernsthafter
    Kandidat fuer ein hypothetisches Replay-Protokoll.

Umgesetzt: hypothetisches Kandidaten-PnL-Replay:

- Der erste echte `exit_candidate_observe` einer offenen Position wird als
  `exit_candidate_replay_state` gespeichert.
- Dieser Replay-Anker wird erst gesetzt, wenn TP/SL auf derselben Kerze nicht
  bereits den echten Exit ausgeloest haben.
- Beim echten Exit rechnet `trade_stats.py` jetzt eine zweite Spur:
  - echter Exit-PnL
  - hypothetischer Kandidaten-PnL
  - Differenz zwischen Kandidaten-Exit und echtem Exit
- Neues Protokoll:
  - `mcm_exit_candidate_replay.csv`
- Neue Summen in `trade_stats.json`:
  - `exit_candidate_replay_count`
  - `exit_candidate_replay_actual_pnl`
  - `exit_candidate_replay_hypothetical_pnl`
  - `exit_candidate_replay_delta_pnl`
  - `exit_candidate_replay_saved_loss_count`
  - `exit_candidate_replay_saved_giveback_count`
  - `exit_candidate_replay_harmed_count`
  - `exit_candidate_replay_tp_cut_count`
- Wichtig:
  - Das ist keine aktive Exit-Entscheidung.
  - DIO bleibt im Observe-Modus.
  - Das Replay prueft nur, ob die innere Exit-Wahrnehmung netto tragfaehig
    gewesen waere.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile bot.py trade_stats.py config.py`
- Naechster Schritt:
  - neuen Observe-Lauf starten
  - danach `mcm_exit_candidate_replay.csv` und die neuen Summen auswerten
  - erst bei wiederholter Netto-Verbesserung ueber einen schaltbaren
    Active-Modus nachdenken

Nach Lauf 31 geprueft:

- Gesamt:
  - 47 Trades, 24 TP / 23 SL
  - Netto-PnL ca. +17.46
  - Profit Factor ca. 2.30
  - Max Drawdown ca. 2.20
- Struktur:
  - Zone: 37 Trades, 24 TP / 13 SL, ca. +23.12 PnL
  - Non-Zone: 10 Trades, 0 TP / 10 SL, ca. -5.67 PnL
  - High: 25 Trades, ca. +18.71 PnL
  - Mid: 12 Trades, ca. +4.41 PnL
  - Low: 10 Trades, ca. -5.67 PnL
- Positionslast-Diagnose:
  - `plan_holding_trust`: 24 Trades, 24 TP / 0 SL, ca. +30.84 PnL
  - `exit_nervousness_observe`: 21 Trades, 0 TP / 21 SL, ca. -12.18 PnL
  - `quiet_position_watch`: 2 Trades, 0 TP / 2 SL, ca. -1.21 PnL
- Exit-Kandidaten:
  - `exit_candidate_observe`: 11 Trades, 0 TP / 11 SL, ca. -6.13 PnL
  - `plan_trust_holds`: 32 Trades, 24 TP / 8 SL, ca. +25.78 PnL
- Hypothetisches Replay:
  - 6 Replay-Faelle
  - echter PnL dieser Faelle: ca. -1.34
  - hypothetischer Kandidaten-PnL: ca. -2.21
  - Replay-Delta: ca. -0.87
  - 5 Faelle haetten Verlust reduziert
  - 1 Fall haette geschadet
  - dieser eine Fall haette einen spaeteren TP zu frueh abgeschnitten
- Interpretation:
  - Die Kandidatenschicht erkennt Verlustlagen weiterhin stark.
  - Aktives Schliessen ist aber noch nicht reif, weil ein einziger
    zu frueher Eingriff die kleinen Verlustverbesserungen ueberkompensiert.
  - Fachlich passt das zur DIO-Logik:
    Exit-Wahrnehmung ist vorhanden, aber Exit-Intervention braucht noch
    zusaetzliche Tragfaehigkeit gegen TP-Zerstoerung.
- Technische Korrektur nach Lauf 31:
  - `mcm_exit_candidate_replay.csv` wurde in Lauf 31 wegen globalem
    Debug-Sampling nicht geschrieben, obwohl die Summen korrekt waren.
  - `trade_stats.py` schreibt Replay-CSV jetzt samplingfrei direkt.
  - Syntaxpruefung erfolgreich:
    `python -m py_compile trade_stats.py bot.py config.py`

Nach Lauf 32 geprueft:

- Gesamt:
  - 48 Trades, 20 TP / 28 SL
  - Netto-PnL ca. +9.81
  - Profit Factor ca. 1.63
  - Max Drawdown ca. 2.80
- Rueckgang gegen Lauf 31:
  - Lauf 31: ca. +17.46 PnL, 24 TP / 23 SL
  - Lauf 32: ca. +9.81 PnL, 20 TP / 28 SL
  - High-Trades sinken von 25 auf 18
  - Low-Trades steigen von 10 auf 17
  - Low-PnL verschlechtert sich von ca. -5.67 auf ca. -9.41
- Struktur:
  - Zone: 31 Trades, 20 TP / 11 SL, ca. +19.22 PnL
  - Non-Zone: 17 Trades, 0 TP / 17 SL, ca. -9.41 PnL
  - High: 18 Trades, 14 TP / 4 SL, ca. +15.93 PnL
  - Mid: 13 Trades, 6 TP / 7 SL, ca. +3.29 PnL
  - Low: 17 Trades, 0 TP / 17 SL, ca. -9.41 PnL
- Positionslast-Diagnose:
  - `plan_holding_trust`: 21 Trades, 20 TP / 1 SL, ca. +25.06 PnL
  - `exit_nervousness_observe`: 25 Trades, 0 TP / 25 SL, ca. -13.97 PnL
  - `intervention_unfit_state`: 1 Trade, spaeter SL, ca. -0.55 PnL
- Exit-Kandidaten:
  - `exit_candidate_observe`: 14 Trades, 0 TP / 14 SL, ca. -8.21 PnL
  - `plan_trust_holds`: 28 Trades, 20 TP / 8 SL, ca. +21.09 PnL
- Hypothetisches Replay:
  - 10 Replay-Faelle
  - echter PnL dieser Faelle: ca. -3.82
  - hypothetischer Kandidaten-PnL: ca. -4.40
  - Replay-Delta: ca. -0.57
  - 9 Faelle haetten Verlust reduziert
  - 1 Fall haette einen spaeteren TP zu frueh abgeschnitten
- Interpretation:
  - Der Rueckgang kommt nicht von einer zerstoerten Kandidatenlogik,
    sondern von mehr Low-/Non-Zone-Handlung und weniger High-Tragfaehigkeit.
  - Die Exit-Kandidaten erkennen Verlustzonen weiterhin sehr gut.
  - Aktives Schliessen bleibt aber unreif, solange ein einzelner TP-Cut
    die vielen kleinen SL-Verbesserungen ueberwiegen kann.
- Technische Korrektur nach Lauf 32:
  - `mcm_exit_candidate_replay.csv` entsteht jetzt, wurde aber noch durch
    eine alte `dbr_debug`-Textzeile verschmutzt.
  - Textdebug wurde auf `mcm_exit_candidate_replay_debug.log` umgeleitet.
  - Ab Lauf 33 sollte die Replay-CSV strukturiert und sauber lesbar sein.
  - Syntaxpruefung erfolgreich:
    `python -m py_compile trade_stats.py bot.py config.py`

Nach Lauf 33 geprueft:

- Gesamt:
  - 25 Trades, 12 TP / 13 SL
  - Netto-PnL ca. +7.78
  - Profit Factor ca. 2.01
  - Max Drawdown ca. 2.67
- Struktur:
  - Zone: 19 Trades, 12 TP / 7 SL, ca. +11.67 PnL
  - Non-Zone: 6 Trades, 0 TP / 6 SL, ca. -3.89 PnL
  - High: 11 Trades, 8 TP / 3 SL, ca. +8.81 PnL
  - Mid: 8 Trades, 4 TP / 4 SL, ca. +2.85 PnL
  - Low: 6 Trades, 0 TP / 6 SL, ca. -3.89 PnL
- Positionslast-Diagnose:
  - `plan_holding_trust`: 13 Trades, 12 TP / 1 SL, ca. +14.97 PnL
  - `exit_nervousness_observe`: 10 Trades, 0 TP / 10 SL, ca. -5.92 PnL
  - `intervention_unfit_state`: 1 Trade, spaeter SL, ca. -0.53 PnL
- Exit-Kandidaten:
  - `exit_candidate_observe`: 7 Trades, 0 TP / 7 SL, ca. -4.36 PnL
  - `plan_trust_holds`: 16 Trades, 12 TP / 4 SL, ca. +13.17 PnL
- Hypothetisches Replay:
  - 5 Replay-Faelle
  - echter PnL dieser Faelle: ca. -1.36
  - hypothetischer Kandidaten-PnL: ca. -2.57
  - Replay-Delta: ca. -1.21
  - 4 Faelle haetten Verlust reduziert
  - 1 Fall haette einen spaeteren TP zu frueh abgeschnitten
- TP-Cut-Befund:
  - Der schädliche Kandidat lag bei `current_r` ca. -0.17R,
    aber nach bereits ca. 2.62R MFE.
  - Das wirkt nicht wie echte Exit-Reife, sondern wie Rueckatmung nach
    starkem Gewinnlauf.
  - Die hilfreichen SL-Schutzfaelle lagen deutlich adverser:
    grob zwischen -0.64R und -0.97R.
- Technisch umgesetzt:
  - neue weiche Zusatzreife `MCM_EXIT_CANDIDATE_MAX_CURRENT_R = -0.45`
  - ein Exit-Kandidat braucht jetzt echte adverse Tiefe
  - leichte Rueckatmung nach Gewinnlauf wird als `exit_pullback_observe`
    sichtbar, aber nicht als echter Kandidat gewertet
  - `adverse_depth_ok` wird in Candidate-/Replay-Kontexte geschrieben
  - Syntaxpruefung erfolgreich:
    `python -m py_compile bot.py trade_stats.py config.py`

Nach Lauf 34 geprueft:

- Gesamt:
  - 39 Trades, 22 TP / 17 SL
  - Netto-PnL ca. +19.67
  - Profit Factor ca. 3.03
  - Expectancy ca. +0.50 pro Trade
  - Max Drawdown ca. 1.73
- Struktur:
  - Zone: 32 Trades, 21 TP / 11 SL, ca. +20.20 PnL
  - Non-Zone: 7 Trades, ca. -0.53 PnL
  - High: 18 Trades, 14 TP / 4 SL, ca. +15.63 PnL
  - Mid: 14 Trades, 7 TP / 7 SL, ca. +4.57 PnL
  - Low: 7 Trades, 1 TP / 6 SL, ca. -0.53 PnL
- Positionslast-Diagnose:
  - `plan_holding_trust`: 22 Trades, 22 TP / 0 SL, ca. +29.34 PnL
  - `exit_nervousness_observe`: 17 Trades, 0 TP / 17 SL, ca. -9.67 PnL
- Exit-Kandidaten:
  - `exit_candidate_observe`: 11 Trades, 0 TP / 11 SL, ca. -6.26 PnL
  - `plan_trust_holds`: 27 Trades, 22 TP / 5 SL, ca. +26.50 PnL
- Hypothetisches Replay:
  - 3 Replay-Faelle
  - echter PnL dieser Faelle: ca. +0.17
  - hypothetischer Kandidaten-PnL: ca. -1.21
  - Replay-Delta: ca. -1.39
  - 2 Faelle haetten Verlust reduziert
  - 1 Fall haette einen spaeteren TP zu frueh abgeschnitten
- Interpretation:
  - Der starke Lauf ist nicht nur “guter Markt”.
  - Ein nicht funktionierendes System wuerde auch in Push-Phasen weiter
    planlos Low-/Non-Zone-Verlust akkumulieren.
  - Hier sieht man echte innere Ordnung:
    `plan_holding_trust` haelt tragende Positionen perfekt bis TP.
  - Low/Non-Zone ist nicht profitabel, aber in diesem Lauf kaum noch
    destruktiv.
  - Die offene Baustelle bleibt Exit-Intervention:
    Exit-Wahrnehmung erkennt Verlustlagen, aber ein einzelner TP-Cut macht
    aktives Schliessen weiter unreif.
- Naechste fachliche Frage:
  - Nicht Entry weiter verschärfen, sondern Exit-Kandidaten-Reife schärfen:
    Wann ist Belastung echte Exit-Reife, und wann nur eine haltbare
    Gegenbewegung innerhalb eines tragenden Plans?

Live-Mechanik geprueft und abgesichert:

- Die Live-Kette ist grundsaetzlich vorhanden:
  - `runner.py` holt OHLCV-Daten ueber die API
  - `workspace.py` schreibt `data/workspace.csv`
  - der Bot verarbeitet dieselbe Fensterlogik wie im Backtest
  - `place_orders.py` setzt Limit-Orders ueber ccxt/Phemex
  - TP/SL werden als `takeProfitPrice` und `stopLossPrice` an die Order gehaengt
  - der Order-Monitor prueft offene Orders, offene Positionen, Market-Shift,
    Missed-TP und Pending-Timeouts
- Mit Fake-Exchange erfolgreich geprueft:
  - Order setzen
  - aktive Order erkennen
  - Snapshot fuer Bot-Handoff bilden
  - Order canceln
  - Cancel-Cause konsumieren
- Korrektur eingebaut:
  - zentrales `ph_ohlcv.resolve_exchange_symbol()`
  - Live-Swap-Pfade nutzen konsistent `SOL/USDT:USDT`
  - Workspace kann weiterhin das menschlich lesbare Symbol `SOL/USDT` schreiben
- Sicherheitsfix eingebaut:
  - Im Live-Modus reicht ein lokales Candle-TP/SL nicht mehr, um intern zu
    finalisieren.
  - Der Bot finalisiert eine Live-Position erst, wenn
    `get_active_order_snapshot()` keinen offenen Order-/Positionskontext mehr
    meldet.
  - Solange die Exchange noch etwas Aktives sieht, schreibt der Bot
    `LIVE_EXIT_WAIT` nach `live_backtest_debug.csv` und haelt die Position intern.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile bot.py runner.py place_orders.py place_orders_funktions.py ph_ohlcv.py workspace.py api.py`
- Wichtig vor echtem Live-Test:
  - `api.py` enthaelt aktuell leere API-Schluessel.
  - Ein echter Live-Test sollte zuerst mit kleinster Groesse und beobachtetem
    `order_debug.csv` / `live_backtest_debug.csv` erfolgen.

Debug-Ausgabe wurde auf automatische Laufordner umgestellt:

- pro Prozess-/Backtest-Start wird ein neuer Ordner `debug/debug_lauf_X` erzeugt
- alte Pfade wie `debug/trade_stats.json`, `debug/mcm_profile.csv` oder
  `debug/mcm_form_symbol_protocol.csv` werden zentral auf den aktuellen Laufordner
  umgeleitet
- dadurch werden neue Debug-Laeufe nicht mehr ueber alte Dateien geschrieben
- die bisherige Auswertelogik bleibt fachlich gleich, nur der Zielordner aendert sich

Naechster Debug liegt damit nicht mehr direkt in `debug/`, sondern z.B. in
`debug/debug_lauf_1/`.

Der neue Lauf nach der Trennung von innerer und handlungsnaher Sprachregulation
wurde ausgewertet:

- 52 Trades, 16 TP / 36 SL
- Netto-PnL ca. -1.47
- Profit Factor ca. 0.93
- `symbolic_action_regulation` blieb klein: Schnitt ca. 0.012, Maximum 0.035
- Formsprache reift weiter als innere Ordnung, ersetzt aber keine Handlungswahrheit
- High-Structure-Trades waren positiv, Mid/Low-Struktur erzeugte den Verlust

Umgesetzt ist deshalb ein Struktur-Tragfaehigkeitsfilter vor Handlung:

- neue Diagnoseachsen: `structure_action_bearing`, `structure_action_gap`
- mittlere/niedrige Struktur kippt bei fehlendem Support eher in `observe` statt `act`
- unterhalb hoher Strukturqualitaet braucht Handlung zusaetzlichen Memory-/Feldsupport
  oder ausserordentlich starke Entscheidungsevidenz
- Ziel: benannte/erkannte Formen duerfen das innere Feld ordnen, aber nicht allein
  die Handlung tragen

Neu umgesetzt ist ausserdem eine kompositorische Formsprache:

- einzelne Formzeichen koennen sich zu zusammengesetzten Wahrnehmungsobjekten verbinden
- Beispiel im Konzept: `Eis` + `Wand` wird nicht als Textregel verstanden, sondern als
  neues verdichtetes Objekt mit eigener Reife
- technisch entsteht aus vorherigem und aktuellem Formzeichen ein `form_symbol_compound`
- zusammengesetzte Zeichen bekommen eigene:
  - Reife
  - Stabilitaet
  - Resonanz
  - Tragfaehigkeit
  - Lastreduktion
  - Neuheitsdruck
- diese Ebene wirkt nur weich auf innere Regulation und kognitive Verdichtung
- sie ist keine Pattern-Regel und kein direkter Handelsausloeser

Damit kann das System komplexere innere Objekte halten, ohne jedes Mal alle
Einzelachsen neu zu entfalten. Erst bei Spannung, Neuheit oder geringer
Tragfaehigkeit muss tiefer in die Clusterinformation hineingezoomt werden.

Neu im Umsetzungsplan festgehalten ist der Begriff
`Transfer-Tragfaehigkeit fremder Strukturen`:

- fremde Marktstrukturen sollen nicht nur als bekannt/unbekannt behandelt werden
- entscheidend ist, wie viel vorhandene Erfahrung auf eine fremde Lage
  uebertragbar ist
- bekannte Teilformen koennen Orientierung geben, ohne das Gesamtbild schon
  sicher zu machen
- geringe Transfer-Tragfaehigkeit soll eher Wahrnehmung, Reframing,
  Zero-Point-Regulation und weiteres Beobachten staerken
- hohe Transfer-Tragfaehigkeit darf Erfahrung weich in Handlung einbringen,
  aber nicht als starre Pattern-Regel

Dieser Punkt ist aktuell konzeptionell dokumentiert,
inzwischen auch im README als Einstieg erklaert,
aber noch nicht als eigene Brain-Metrik implementiert.

Naechster sinnvoller Schritt:

- neuen Backtest laufen lassen und pruefen, ob Mid/Low-Verlust reduziert wird
- besonders beobachten: Tradezahl, PnL, Profit Factor, High/Mid/Low-Strukturverteilung
  und die neuen Gruende `structure_action_bearing_observe` / `structure_action_low_observe`
- zusaetzlich beobachten: Anzahl/Reife der `form_symbol_compound`-Objekte und ob sie
  kognitive Last senken, ohne Handlung zu frueh zu enthemmen

Auswertung des ersten Laufs mit kompositorischer Formsprache:

- 44 Trades, 15 TP / 29 SL
- Netto-PnL ca. +0.90
- Profit Factor ca. 1.05
- High-Struktur blieb klar positiv
- Mid-Struktur wurde ebenfalls positiv
- Low-Struktur blieb kritisch: 0 TP / 13 SL
- Compound-Ebene arbeitet technisch:
  - viele zusammengesetzte Formobjekte entstehen
  - Reife ist noch niedrig
  - Lastreduktion ist noch klein
  - damit wirkt die Ebene bisher nicht zu aggressiv

Umgesetzt als Folgeschritt:

- `structure_action_uncertainty` ergaenzt die Struktur-Handlungsregulation
- fehlende Struktur-Tragfaehigkeit erhoeht jetzt weich Beobachtungsbedarf,
  Replan-Druck und Handlunghemmung
- gleichzeitig wird Action-Clearance leicht reduziert
- keine harte Regel: schlechte Struktur wird nicht absolut verboten, sondern
  als organisches Unsicherheitsgefuehl im MCM-Feld abgebildet

---

# --------------------------------------------------
# 1. Gesamtstatus
# --------------------------------------------------

Das Projekt ist nicht mehr in einer frühen Fix- oder Basisphase.

Die Kernbasis steht bereits im Code:

- äußere Wahrnehmung ist vorhanden
- innere Runtime ist vorhanden
- Entscheidungstendenz ist vorhanden
- Action-Intent- und Execution-State sind vorhanden
- technische Handlungsbahn ist vorhanden
- Episode / Review / Experience sind vorhanden
- Persistenz für Memory- und Runtime-Zustände ist vorhanden
- Visual- und Inner-Snapshots für die GUI sind vorhanden

Die Hauptarbeit liegt damit nicht mehr in der Einführung der Grundmechanik,
sondern im Architektur-Endausbau, in der Experience-Vertiefung
und in der weiteren Ausrichtung auf zustandswirkungsbasierte Experience-Bewertung.

Aktuelle Arbeitspriorität:

- zuerst neuronale Aktivität und kognitive Innenfunktion fertigstellen
- danach das MCM-Feld als Wahrnehmungsfeld sauber ausbauen
- Fokus auf `MCMNeuron`, lokale Aktivierung, Kopplung, Nachhall, Kontext-Memory, `MCMField`, Innenmuster und Experience
- Backtest-Logik bleibt sauberer Ausführungs- und Kontrollpfad, aber Testdateien sind nicht die aktuelle Hauptarbeit
- Live-Exchange / echter Live-Handoff erst am Schluss validieren
- GUI-Ausbau vorerst nachrangig behandeln
- Testausbau vorerst nachrangig behandeln

Damit ist der aktuelle Schwerpunkt nicht Live-Betrieb und nicht Oberfläche,
sondern die fachlich saubere Umsetzung des inneren Gehirns:
erst neuronale Aktivität, dann das Mental-Core-Matrix-Feld als Wahrnehmungsraum.

---

# --------------------------------------------------
# 2. Bereits real umgesetzt
# --------------------------------------------------

# --------------------------------------------------
# 2.1 Ebene 1 – äußeres Wahrnehmen
# --------------------------------------------------

Ebene 1 ist als eigenständige Wahrnehmungsbasis real vorhanden.

Bereits produktiv vorhanden:

- `candle_state`
- `tension_state`
- `visual_market_state`
- `structure_perception_state`
- `temporal_perception_state`
- `outer_market_state`

Die Wahrnehmung wird aus Marktdaten / `window` aufgebaut
und als neutrales Wahrnehmungspaket weitergegeben.

### Fachliche Bedeutung

Die Außenwelt ist nicht mehr nur einfache Signalquelle,
sondern bereits mehrschichtig beschrieben als:

- Candle-Zustand
- Spannungszustand
- äußere Marktform
- Struktur-Wahrnehmung
- zeitliche Wahrnehmung / Ablaufwahrnehmung

Damit ist Ebene 1 real vorhanden und nicht mehr nur geplant.

---

# --------------------------------------------------
# 2.2 Ebene 2 – inneres Wahrnehmen / Denken / Handeln
# --------------------------------------------------

Ebene 2 ist bereits als laufende innere Runtime-Schicht vorhanden.

Bereits real vorhanden:

- `MCMBrainRuntime`
- Runtime-Snapshot
- Runtime-Decision-State
- Runtime-Brain-Snapshot
- Runtime-Marktimpuls-Verarbeitung
- Runtime-Idle-Followup

Die innere Zustandskette ist angelegt und im Codepfad vertreten:

- `outer_visual_perception_state`
- `inner_field_perception_state`
- `perception_state`
- `processing_state`
- `felt_state`
- `thought_state`
- `meta_regulation_state`
- `expectation_state`

### Entscheidungstendenz

Die Handlung entsteht bereits nicht mehr direkt aus einem simplen Signal.

Vorhanden ist eine vorgelagerte Entscheidungstendenz:

- `act`
- `observe`
- `hold`
- `replan`

### Handlungsbahn vor technischer Ausführung

Zwischen Entscheidung und technischer Order liegen bereits weitere Zustände:

- `action_intent_state`
- `execution_state`

Damit ist Entscheidung bereits stärker von technischer Ausführung getrennt.

### Technische Handlungsbahn

Weiterhin aktiv vorhanden:

- Pending
- Entry
- Position
- Exit

Die technische Mechanik ist damit bereits an die innere Zustandslogik gekoppelt.

---

# --------------------------------------------------
# 2.3 MCM-Zustandsraum
# --------------------------------------------------

Der MCM-Zustandsraum ist bereits explizit lesbar.

Vorhanden sind reale Zustandsachsen wie:

- `field_density`
- `field_stability`
- `regulatory_load`
- `action_capacity`
- `recovery_need`
- `survival_pressure`

Diese Größen laufen bereits durch Runtime-, Decision-, Snapshot- und Experience-Strukturen.

### Fachliche Bedeutung

Die Zielidee,
den Innenraum des Systems explizit lesbar zu machen,
ist real begonnen und produktiv im Code vertreten.

---

# --------------------------------------------------
# 2.4 Ebene 3 – Entwicklung aus Erfahrung
# --------------------------------------------------

Die Entwicklungsebene ist bereits substanziell umgesetzt.

Vorhanden sind:

- `mcm_decision_episode`
- `mcm_decision_episode_internal`
- `mcm_experience_space`
- `outcome_decomposition`
- Review-Logik
- Signature-Memory
- Context-Cluster
- formale `inner_context_clusters`-Anbindung
- persistenter Memory-State
- In-Trade-Update-Auswertung
- Experience-Linking
- Similarity-/Axis-/Drift-/Reinforcement-Ansätze
- Felt-/Affective-Episode-Auswertung

### Nicht-Handlung ist integriert

Nicht-Handlung ist nicht mehr nur Sonderfall,
sondern realer Teil des Episoden- und Experience-Flusses:

- `observed_only`
- `withheld`
- `replanned`
- `abandoned`

### Zustandsdelta ist integriert

Episode / Experience führen bereits:

- `state_before`
- `state_after`
- `state_delta`

Damit ist die Kopplung von Handlung / Nicht-Handlung und Zustandsveränderung bereits real umgesetzt.

### Innenkontextcluster und Pattern-Verdichtung sind begonnen

`inner_context_clusters` sind im aktuellen Code nicht mehr nur Zielidee,
sondern bereits in `Bot`, Experience-Aktualisierung und Memory-State verankert.

Zusätzlich sind im aktuellen Stand Pattern-Werte vorhanden:

- `inner_pattern_support`
- `inner_pattern_conflict`
- `inner_pattern_fragility`
- `inner_pattern_bearing`
- `pattern_reinforcement`
- `pattern_attenuation`
- `pattern_action_support`
- `pattern_observe_pressure`
- `pattern_replan_pressure`

Neu ergänzt ist eine erste aktive Kontextspur:

- `active_context_trace`
- `activation`
- Decay pro Runtime-Tick
- Reaktivierung aus `inner_context_clusters`
- schwache Rückwirkung auf Pattern-Modulation
- schwache Rückwirkung auf Replay-/Feldimpuls
- schwache lokale Rückstreuung bis in `MCMNeuron.memory_trace`
- `context_memory_impulse` als lokale Kontext-Memory-Kennzahl
- `field_neuron_context_memory_impulse_norm_mean` läuft in `inner_context_clusters`, `current_vector`, Experience-Link-Achsen und bleibt persistierbar
- innere Musterbeschriftung kann `memory_reactivated_neurons` ausweisen
- Experience-Similarity führt `context_memory_impulse_axis`, `active_context_activation_axis`, `active_context_balance_axis` und `context_memory_reactivation_axis`
- `neural_felt_state` ist als lesende neuronale Felt-Schicht begonnen
- `neural_felt_bearing`, `neural_felt_pressure`, `neural_felt_memory_resonance`, `neural_felt_context_reactivation` und `neural_felt_label` laufen in `inner_context_clusters`, `current_vector`, `felt_state` und `memory_state`
- `neural_felt_*` läuft zusätzlich in Experience-Summary, Episode-Felt-Summary, Similarity-Achsen, Runtime-Snapshot, Decision-State, Brain-Snapshot und `active_context_trace`
- `active_context_trace` trägt `neural_felt_*` als Lesefeld; Replay-/Feldimpuls und Pattern-Verstärkung wurden dadurch nicht erhöht
- `inner_field_history` ist als lesender Feldverlauf über mehrere Ticks angebunden und über `memory_state` persistierbar
- `inner_field_history_*` läuft in `inner_context_clusters`, `current_vector`, Experience-Summary, Runtime-/Brain-Snapshot, `active_context_trace` und `episode_internal["signal"]`
- `active_context_trace` trägt `inner_field_history_*` nur als Lesefeld; Replay-/Feldimpuls und Pattern-Verstärkung wurden dadurch nicht erhöht
- feste Feldtopologie ist begonnen: `MCMField` führt feste `field_position` und `topology_neighbors` je `MCMNeuron`
- neuronale Aktivität ist geschärft: `MCMNeuron` bildet jetzt lokale `receptivity`, `overload`, `recovery_tendency`, `memory_resonance`, `context_reactivation`, `coupling_resonance`, `activity_label` und `activation_components`
- Reizaufnahme wird pro Neuron lokal moduliert, sodass derselbe Außenreiz nicht mehr nur global gleichförmig wirkt
- `activation` ist jetzt eine zusammengesetzte Lesung aus Außenreiz, Replay, Kontext-Memory, Kopplung, Memory-Feedback, Velocity und lokaler Resonanz
- `MCMField` ist als Wahrnehmungsfeld geschärft: neuronale Aktivität breitet sich schwach über feste Topologie-Nachbarn aus
- `field_perception_state` erkennt lokale Aktivitätsinseln mit Masse, Aktivierung, Druck, Kohärenz, Kontextreaktivierung, Spread und Label
- `field_perception_state` bewertet Aktivitätsinseln jetzt zusätzlich als Wahrnehmungsqualität: `field_perception_focus`, `field_perception_clarity`, `field_perception_stability`, `field_perception_fragmentation`, `field_perception_strain` und `dominant_activity_island_id`
- Feldlabels wie `active_perception_field`, `coherent_perception_field`, `fragmented_perception_field`, `memory_reactivated_field` und `strained_field` sind als Leseschicht vorhanden
- `field_topology_layout_state` läuft in `inner_field_perception_state`, `inner_context_clusters`, `current_vector`, `active_context_trace` und Experience-Similarity-Achsen
- neue neuronale Aktivitätswerte und `field_perception_state` laufen in Neuron-Snapshots, Arealzustände, `inner_field_perception_state` und `neural_felt_state`
- Aktivitätsinseln und `field_perception_label` laufen jetzt in `inner_pattern_identity`, `field_pattern_signature`, `field_pattern_vector`, `inner_context_clusters`, `memory_state` und `mcm_experience_space`
- die Innenmuster-Identität unterscheidet dadurch nicht mehr nur globale Feld-/Arealwerte, sondern auch wahrgenommene lokale Aktivitätsinseln im MCM-Feld
- `processing_state` bildet aus Feldinseln jetzt `field_perception_pressure`, `field_perception_support`, `field_perception_clarity`, Fokus, Stabilität, Fragmentierung und Strain
- `felt_state` nutzt die geschärfte Feldwahrnehmung für Risiko, Gelegenheit, inneren Konflikt, Druck, Stabilität, Alignment und dominante Spannung
- `thought_state` nutzt Fokus/Stabilität/Fragmentierung/Strain für Denk-/Areal-Druck, Unterstützung, Reife, Grübeltiefe, Entscheidungsdruck, Entscheidungsbereitschaft und Thought-Alignment
- `meta_regulation_state` nutzt die geschärfte Feldwahrnehmung jetzt für `field_perception_instability`, `field_observation_need`, `field_replan_pressure` und `field_action_support`
- fragmentierte/angespannte MCM-Felder können dadurch auch bei starkem Signal gezielt `observe` oder `replan` auslösen; klare/stabile Felder können kontrolliertes `act` stützen
- Architekturentscheid übernommen: Experience soll nicht `TP gut / SL schlecht` lernen, sondern eine neurochemisch gedämpfte Wirkung aus Profitabilität, Entlastung, Stabilität, Disziplin, Tragfähigkeit, Varianz und Überlast bilden
- Profitabilität bleibt notwendige innere Zielspannung, wird aber durch Regelqualität, Tragfähigkeit, Stabilität und Varianz gedämpft; chaotischer Gewinn darf nicht blind stärken, sauberer Verlust nicht blind schwächen
- `build_experience_neurochemical_effect()` ist im Brain angebunden und liefert getrennte Wirkachsen: `profit_reward`, `relief_signal`, `stability_signal`, `discipline_signal`, `confidence_signal`, `overactivation_signal`, `chaos_penalty`, `variance_penalty`, `overstrain_penalty`, `carrying_capacity_delta`, `self_confidence_delta` und `process_quality`
- `_experience_reward_delta()` ist jetzt nur noch ein Kompatibilitäts-Wrapper auf `experience_effect_score`; die eigentliche Erfahrungsmechanik liegt in der neurochemisch gedämpften Wirkfunktion
- `experience_neurochemical_effect` und die flachen Wirkachsen laufen in Experience-Summary, Episode-History, Experience-Space und als gleitende Link-Profile (`avg_*` / `last_*`) in die Musterlinks
- SL-Episoden werden nicht automatisch schlecht bewertet, aber nach oben gedeckelt; sauberer Verlust kann Prozessstabilität bestätigen, erzeugt aber kein euphorisches Gewinnsignal
- Experience-Similarity führt jetzt zusätzliche neurochemische Achsen für Profit, Entlastung, Stabilität, Disziplin, Confidence, Überaktivierung, Chaos, Varianz, Überlast, Tragfähigkeit und Selbstvertrauen
- `inner_context_clusters` speichern jetzt `experience_neurochemical_profile`, `neurochemical_support`, `neurochemical_strain` und gleitende neurochemische `avg_*` / `last_*` Werte
- `pattern_reinforcement`, `pattern_attenuation` und `trust` werden schwach durch neurochemische Tragfähigkeit oder Belastung moduliert; die Feld-/Musterwerte bleiben weiterhin dominierend
- `active_context_trace` trägt die neurochemischen Achsen als Nachhall und nutzt sie schwach für `activation`, `action_support`, `observe_pressure`, `replan_pressure` und Replay-Impuls
- tragfähige Muster bekommen dadurch etwas mehr stabile Wiedererreichbarkeit; chaotische/überaktive Muster erzeugen eher Dämpfung, Beobachtungsdruck und weniger Replay-Nachhall
- `memory_state.py` persistiert die neuen neurochemischen Clusterprofile
- `active_context_trace` trägt `field_topology_layout_state` nur als Lesefeld; Replay-/Feldimpuls und Pattern-Verstärkung wurden dadurch nicht erhöht
- `field_areal_topology_*` läuft in `inner_context_clusters`, `current_vector`, `active_context_trace`, `episode_internal["signal"]` und Experience-Similarity-Achsen
- `field_areal_topology_*` bleibt Lesewert und verändert Replay-/Feldimpuls oder Pattern-Verstärkung nicht
- `inner_pattern_identity` ist als erste Innenmuster-Identität begonnen und läuft in `inner_context_clusters`, `current_vector`, Cluster-Rückgabe, `memory_state` und `active_context_trace`
- `active_context_trace` trägt `field_pattern_signature_key`, `inner_pattern_identity`, `inner_pattern_identity_label` und `inner_pattern_identity_confidence` nur als Lesefelder
- `inner_pattern_identity_stability` ist als Lesewert ergänzt und läuft in Cluster-Rückgabe, `active_context_trace`, `mcm_runtime_brain_snapshot["signal"]`, `episode_internal["signal"]`, `mcm_experience_space` und `memory_state`
- `inner_pattern_identity_streak`, `inner_pattern_identity_recurrent`, `inner_pattern_identity_changed` und `inner_pattern_identity_last_seen_tick` bleiben reine Wiedererkennungs-/Stabilitätswerte ohne stärkere Replay-/Feldimpuls-Gewichtung
- Runtime-Profiling ist als Debug-Schicht angebunden und schreibt nach `debug/mcm_profile.csv`
- Profiling misst `step_mcm_brain`, `field.step`, `cluster.detect`, Runtime-/Visual-Snapshot-Schreiben und `memory_state` Build/Write

Eine erste schwache lokale Rückstreuung bis in `MCMNeuron.memory_trace` ist angebunden; die tiefe lokale Erfahrungsareal-Bildung ist noch offen.
`neural_felt_state` bleibt eine lesende Innenwahrnehmung und ist keine neue Handelsregel.

---

# --------------------------------------------------
# 2.5 Persistenz
# --------------------------------------------------

Persistenz ist vorhanden für:

- `signature_memory`
- `context_clusters`
- `inner_context_clusters`
- `mcm_runtime_snapshot`
- `mcm_runtime_decision_state`
- `mcm_runtime_brain_snapshot`
- `mcm_decision_episode`
- `mcm_experience_space`
- weitere Memory-Zustände

Damit kann der Bot relevante Langzeitanteile seines Zustandsraums halten.

---

# --------------------------------------------------
# 2.6 Visualisierung / Snapshots
# --------------------------------------------------

Für die Visualisierung existieren bereits reale Ausgaben aus dem Bot:

- `debug/bot_visual_snapshot.json`
- `debug/bot_inner_snapshot.json`
- `bot_memory/memory_state.json`
- `debug/trade_stats.json`
- `debug/trade_equity.csv`

Damit ist bereits eine hybride Visualisierung vorhanden:

- Außenwelt
- Innenwelt
- Memory / Entwicklung
- klassische Equity-/PnL-Nachweise

Die GUI ist also nicht mehr rein alt,
sondern bereits in einer Übergangsform.

---

# --------------------------------------------------
# 3. Bereits korrigierte Fehler aus dem früheren Fixblock
# --------------------------------------------------

# --------------------------------------------------
# 3.1 state_delta ist korrigiert
# --------------------------------------------------

Bereits umgesetzt:

- ereignislokale Bildung von `state_before`, `state_after`, `state_delta`
- gemeinsamer Übergang für Stats-Kontext und Episode-Payload
- Snapshot-Commit erst nach dem jeweiligen Event
- alte Null-/Doppelsnapshot-Pfade im Entry-/Pending-/Nicht-Handlungs-Pfad bereinigt

Folge:

- Episode / Experience arbeiten an diesen Stellen wieder auf realen Zustandsübergängen

---

# --------------------------------------------------
# 3.2 Statistik-Semantik ist korrigiert
# --------------------------------------------------

Bereits umgesetzt:

- `pnl_netto` startet als reiner Nettowert bei `0.0`
- `current_equity` wird getrennt als `start_equity + pnl_netto` geführt
- `expectancy` baut damit auf realem Nettowert statt auf Equity-Basis auf

Folge:

- Nettoergebnis und Erwartungswert sind semantisch wieder sauber getrennt

---

# --------------------------------------------------
# 3.3 Exit-Strukturdiagnose ist korrigiert
# --------------------------------------------------

Bereits umgesetzt:

- Exit-/Cancel-Pfade nutzen aktuellen Exit-Kontext statt alten Entry-Kontext
- aktuelle `structure_perception_state` läuft bis in `on_exit()` / `on_cancel()`
- `outcome_records` tragen reale Exit-Strukturqualität
- `structure_bands` werden daraus sauber neu aufgebaut

Folge:

- Exit-KPI über Strukturqualität ist im aktuellen Backtest-/Bot-Pfad fachlich belastbar

---

# --------------------------------------------------
# 3.4 attempt_feedback / proof-Felder sind korrigiert
# --------------------------------------------------

Bereits umgesetzt:

- Proof-/Regulationsfelder werden im Attempt-Feedback sauber aggregiert
- Snapshot-Fallbacks sind vorhanden
- In-Trade-Update-Pfade tragen die fehlenden Felder weiter
- Experience-Linking / Episode-History führt diese Felder weiter

Bereits sauber geführt insbesondere:

- `regulatory_load`
- `action_capacity`
- `survival_pressure`
- `pressure_release`
- `load_bearing_capacity`
- `state_stability`
- `capacity_reserve`
- `recovery_balance`

Folge:

- die alte statistische Abflachung dieser Diagnosegrößen ist im aktuellen Code nicht mehr der Hauptfehler

---

# --------------------------------------------------
# 4. Reale offene Punkte im aktuellen Stand
# --------------------------------------------------

# --------------------------------------------------
# 4.0 MCMField-Speicherfehler korrigiert / Zieltopologie geschärft
# --------------------------------------------------

Real vorhanden:

- `MCM_KI_Modell.py` führt den Feldzustand weiterhin als mehrdimensionales `N x D`
- `_build_local_neighbor_state_map()` berechnet Nachbarschaften zeilenweise pro Neuron
- der alte permanente `N x N x D`-Deltablock ist im lokalen Nachbarschaftsaufbau entfernt
- weitergegeben werden nur lokale Nachbarn, nicht das gesamte Feld als globaler Neuroneneinfluss
- `velocity` beschreibt Zustandsnachlauf / Trägheit / Richtung der Zustandsveränderung, keine physische Neuronenbewegung

Fachliche Bedeutung:

- alle Neuronen können denselben Umweltreiz wahrnehmen
- informationsbildend ist aber ihre lokale Eigenreaktion
- lokale Nachbarschaft, Kopplung, Kohärenz und Resonanz können Informationsinseln bilden
- Cluster sollen dadurch nicht aus globalem Gleichschalten entstehen, sondern aus lokaler Feldorganisation
- die Zielrichtung wird auf feste Feldknoten / neuronales Gewebe geschärft
- nicht der Knoten bewegt sich, sondern Zustand, Aktivierung, Nachhall und Informationswirkung breiten sich im Feld aus
- höhere Neuronenzahl bedeutet höhere Auflösung der inneren Zustandswahrnehmung, nicht automatisch höhere Intelligenz

Weiter zu beobachten:

- `_build_areal_state()` baut Areale jetzt ohne dauerhafte vollständige `N x N`-Distanzmatrix auf
- `_build_areal_components()` berechnet Distanzen zeilenweise pro Neuron
- interne Areal-Dichte wird pro Komponente zeilenweise berechnet
- kein permanenter `N x N x D`-Deltablock und keine dauerhafte globale Distanzmatrix im Arealaufbau

Aktueller Architekturabgleich:

- `MCMField` ist kompatibel auf feste Feldtopologie begonnen
- jedes `MCMNeuron` trägt `field_position` und `topology_neighbors`
- `energy` und `velocity` bleiben nach außen kompatibel als `N x D`-Sicht erhalten
- lokale Kopplung nutzt feste Topologie-Nachbarschaften statt dynamischer globaler Zustandsabstandssuche
- GUI-Lesart bleibt bewusst offen bis die Feldtopologie fachlich fertig steht

---

# --------------------------------------------------
# 4.1 Live-Handoff zwischen Pending, Fill und Position ist bot-seitig nachgezogen
# --------------------------------------------------

Teilweise korrigiert:

- `_handle_pending_entry()` kann `source="position_context"` in den gemeinsamen Fill-Handoff überführen
- `_finalize_pending_fill_handoff()` führt Live- und Backtest-Fill über denselben Bot-internen Pfad
- `get_active_order_snapshot()` erzwingt vor der Snapshot-Auswertung einmalig einen synchronen Bootstrap-/Exchange-Sync
- `get_active_order_snapshot()` liest offene Order-TP/SL jetzt aus `takeProfitPrice/stopLossPrice` und `takeProfitRp/stopLossRp`
- `get_active_order_snapshot()` bleibt bei offener Order auch ohne Exchange-`timestamp` verwertbar
- `place_order()` übernimmt identische offene Orders jetzt inklusive `_ACTIVE_TP`, `_ACTIVE_SIDE` und Entry-/Risk-Kontext
- `_sync_with_exchange()` übernimmt eindeutig offene Orders jetzt inklusive `_ACTIVE_TP`, `_ACTIVE_SIDE` und Entry-/Risk-Kontext
- `_sync_with_exchange()` ergänzt bei bereits bestätigter aktiver Order fehlenden `_ACTIVE_TP`, `_ACTIVE_SIDE` und Entry-/Risk-Kontext aus `open_orders`
- `get_active_order_snapshot()` synchronisiert bei verschwundener aktiver Order aktiv nach
- erkannte Live-Positionen können dadurch als Positionskontext an den Bot zurückgegeben werden
- Live-Fill schreibt den `live_handoff`-Kontext inklusive `pending_order_id`, `snapshot_id`, Entry/TP/SL, `entry_ts` und `handoff_reason` in `position_meta`
- Restart-Recovery schreibt `recovery_source` und `recovery_snapshot` in `meta`
- aktive Restart-Positionen erhalten einen verwertbaren `entry_ts` / `last_checked_ts`
- Restart-Recovery setzt `execution_state` auf `pending_recovered` oder `position_recovered`
- Restart-Recovery schreibt ein technisches Episode-Event über `pending_update` oder `position_update`
- Restart-Recovery markiert Memory-State als dirty und committet den Regulationssnapshot
- Restart-Recovery speichert den wiederhergestellten Zustand sofort per Forced-Save

Weiter zu prüfen:

- echter Live-Test `pending -> filled -> position` gegen Exchange-Zustand
- Restart-Fall mit bereits gefüllter Order gegen echten Exchange-Zustand validieren
- ob TP/SL/Entry-Kontext nach Restart im echten Exchange-Fall vollständig belastbar bleibt

Folge:

- Backtest- und Live-Handoff nutzen bot-seitig denselben Fill-Abschluss, müssen aber real-live-validiert werden

---

# --------------------------------------------------
# 4.2 Innenkontextcluster sind angebunden und als Pattern-Verdichtung begonnen
# --------------------------------------------------

Real vorhanden:

- `inner_context_clusters` sind bereits real in `Bot`, Experience-Aktualisierung und Persistenz verankert
- die Trennung von `context_clusters` und `inner_context_clusters` ist fachlich begonnen
- Pattern-Verdichtung ist real begonnen über Support, Conflict, Fragility, Bearing, Reinforcement und Attenuation
- Pattern-Werte wirken bereits in Review-Feedback, Runtime-Meta-Regulation und Entscheidungstendenz hinein

Neu real vorhanden:

- `active_context_trace` ist als Runtime-Zustand eingeführt
- aktive Kontextspur wird aus `inner_context_clusters` reaktiviert
- `activation` klingt pro Runtime-Tick ab
- Pattern-Werte werden schwach über aktive Kontextspur moduliert
- Runtime-Snapshot führt `active_context_trace` mit
- aktive Kontextspur wird schwach und lokal dosiert bis in `MCMNeuron.memory_trace` zurückgeführt
- `context_memory_impulse` ist im Inner-Snapshot als eigene lokale Kontext-Memory-Kennzahl vorhanden; die Neuron-GUI-Datei ist im aktuellen Upload nicht enthalten und daher nicht geprüft
- `field_neuron_context_memory_impulse_norm_mean` läuft in `inner_context_clusters` und bleibt über `memory_state` persistierbar
- `context_memory_impulse` wird in der inneren Musterbeschriftung als `memory_reactivated_neurons` sichtbar, wenn lokale Kontextreaktivierung dominiert

Real offen:

- wiederkehrende Feldformen sind noch nicht als echte lokale Erfahrungsareale im Neuronenfeld verankert
- Nachhall ist jetzt erste lokale Memory-Trace-Modulation, aber noch keine tiefe lokale Feldplastizität
- Replay-Rückwirkung bleibt bewusst schwach begrenzt und ist noch kein vollständiger lokaler Erfahrungsumbau

Fachlich ergänzt:

- Informationscluster sollen nicht durch Felddruck gelöscht werden
- Felddruck verändert Priorität, Aktivierung und Zugänglichkeit von Information
- nicht getragene Information verliert aktive Bindungsstärke und geht in Nachhall oder Latenz über
- dadurch wird lokaler Organisationsraum frei, ohne gespeicherte Erfahrung zu vernichten
- Reorganisation bedeutet Informationsumschichtung, nicht Blackout
- Kohärenzstärke beschreibt, wie verdichtet und tragfähig ein Cluster aktuell getragen wird
- diese Kohärenzstärke soll später farblich in der GUI sichtbar werden

Ziel:

- `context_clusters` als äußerer / gesamt-situativer Signaturraum klar halten
- `inner_context_clusters` als wiederkehrenden Innenmusterraum weiter ausbauen
- aktive Kontextspur im Replay-/Feldimpuls weiter kontrolliert beobachten und begrenzen
- Vermeidungs-, Entlastungs-, Reorganisations- und Tragfähigkeitslernen sauber auf Innenmuster legen
- Clusterzustände als aktiv getragen, nachhallend, latent oder frei werdend unterscheidbar machen

---

# --------------------------------------------------
# 4.3 Experience-Bewertungslogik ist auf neurochemische Zustandswirkung umgestellt
# --------------------------------------------------

Umgesetzt:

- `build_experience_neurochemical_effect()` bildet den eigentlichen Erfahrungswert aus Prozessqualität, Profitspannung, Entlastung, Stabilität, Disziplin, Confidence, Tragfähigkeit, Varianz, Chaos, Überlast und Überaktivierung
- `_experience_reward_delta()` verzweigt nicht mehr selbst über Outcome-Wege, sondern liest nur noch `experience_effect_score` aus der neurochemischen Wirkfunktion
- `tp_hit`, `sl_hit`, `cancel`, `timeout` bleiben Ereigniskontext, aber nicht mehr der Bewertungsanker
- SL-Episoden sind nach oben gedeckelt: sauberer Verlust kann Regelwerk und Tragfähigkeit bestätigen, aber kein starkes Belohnungssignal erzeugen
- chaotische TP-Episoden werden durch Chaos, Varianz und Überaktivierung gedämpft
- die Wirkachsen laufen in Experience-Summary, Episode-History, Experience-Space, Link-Buckets und Similarity-Achsen

Offen:

- die neue neurochemische Wirkung ist noch nicht stark in lokale Neuronen-/Feldverstärkung zurückgeführt
- die nächsten Schritte müssen beobachten, ob `avg_*` / `last_*` Profile in den Link-Buckets stabile Musterbindung oder sinnvolle Dämpfung erzeugen

Ziel:

- Experience bewertet primär `state_before`, `state_after`, `state_delta` und Tragfähigkeitswirkung
- `tp_hit`, `sl_hit`, `cancel`, `timeout` bleiben nur Ereigniskontext
- Lernen entsteht stärker aus Belastung, Entlastung, Stabilisierung, Fragilisierung und Handlungsfähigkeit
- lokale Rückführung wird erst auf dieser Grundlage fachlich sinnvoll

---

# --------------------------------------------------
# 4.4 MCM-Feldtopologie / Feldverlauf / Innenfeldspeicher sind noch nicht ausgebaut
# --------------------------------------------------

Teilweise umgesetzt:

- `field_cluster_links` und `field_areal_links` werden zu `field_topology_state` verdichtet
- `field_topology_state` führt Link-Anzahl, Link-Dichte, mittlere Distanz, Topologie-Kohärenz, Topologie-Spannung und Topologie-Label
- Feldtopologie läuft jetzt in `inner_field_perception_state`, `inner_context_clusters`, `current_vector`, Experience-Summary, Experience-Space, Experience-Link-Buckets und `memory_state`
- `field_topology_state` steht für die Neuron-GUI als Topologie-Zustand, Linkverhältnis, Link-Dichte, Kohärenz und Spannung bereit; die Neuron-GUI-Datei ist im aktuellen Upload nicht enthalten und daher nicht geprüft

Offen:

- ein eigener persistenter Speicher für wiederkehrende Feldformen, Driftmuster und Regulationsverläufe fehlt aktuell
- Feldverlauf über mehrere Ticks ist noch nicht als eigener Innenfeldpfad gespeichert
- die Visualisierung zeigt Feldformen, führt aber noch keinen persistenten Feldformverlauf

Ziel:

- Feldcluster nicht nur erkennen, sondern in ihrer Größe, Dichte, Stabilität, Verschiebung und Beziehung zueinander lesbar machen
- die Gesamtform des MCM-Feldes als Feldtopologie beschreiben
- Feldverlauf über Zeit mitführen
- einen verdichteten Innenfeldspeicher für wiederkehrende Clusterkonfigurationen, Feldformen, Driftmuster und Rückführungsbewegungen aufbauen

---

# --------------------------------------------------
# 4.5 Runtime / Bot-State sind noch nicht weit genug getrennt
# --------------------------------------------------

Offen:

- `Bot` bündelt weiter Außenwahrnehmung, Runtime, Handlungsbahn, Experience, Persistenz und Snapshot-Orchestrierung
- die Zieltrennung Ebene 1 / Ebene 2 / Ebene 3 ist damit noch nicht strukturell verhärtet

Ziel:

- weniger Vermischung von Runtime und Bot-State
- klarere Trennung von Wahrnehmung / Innenprozess / Entwicklung

---

# --------------------------------------------------
# 4.6 Persistenz ist entschärft, aber noch nicht ausreichend entkoppelt
# --------------------------------------------------

Offen:

- Persistenz ist bereits über Dirty-Flag und Cooldown teilweise entschärft
- Save-/Flush-Pfade liegen aber weiter nah am Kernlauf

Folge:

- Bot-Kern bleibt unnötig eng mit Save-/Flush-Logik gekoppelt

---

# --------------------------------------------------
# 5. Fachlich vorbereitet, aber noch nicht vollständig ausgebaut
# --------------------------------------------------

# --------------------------------------------------
# 5.1 Tragfähigkeit ist stärker verankert, aber noch nicht Endzustand
# --------------------------------------------------

Experience bewertet bereits stärker:

- Tragfähigkeit
- Regulationskosten
- Entlastung
- Handlungsspielraum

Noch nicht vollständig ausgebaut ist:

- die weitere Entkopplung von Ergebnislogik und Experience-Logik
- die noch konsequentere Ausrichtung auf Zustandswirkung statt Geldwirkung
- die formale Umstellung der Experience-Bewertungslogik von Outcome-Verzweigungen auf Zustandswirkung

---

# --------------------------------------------------
# 5.2 Lernen als Umgangsfähigkeit ist begonnen, aber noch nicht konsequent genug
# --------------------------------------------------

Das System lernt bereits erkennbar stärker:

- womit es umgehen kann
- in welchen Situationen es handlungsfähig bleibt
- wie Tragfähigkeit und Belastung zusammenhängen

Noch offen ist:

- Lernen als Umgangsfähigkeit technisch konsequenter durchzuziehen
- Cluster-Bewertung noch stärker auf Tragfähigkeit statt Ergebnis auszurichten

---

# --------------------------------------------------
# 5.3 Lokale Rückführung ist vorbereitet, aber fachlich noch nicht reif genug
# --------------------------------------------------

Vorbereitet ist bereits:

- Experience-Linking
- `inner_context_clusters`
- Similarity-/Drift-/Reinforcement-Mechanik
- Zustandsachsen für Tragfähigkeit, Belastung, Entlastung und Handlungsfähigkeit

Noch offen ist:

- lokale Erfahrungsrückwirkung erst nach sauberer Umstellung auf Zustandswirkung zu vertiefen
- lokale Hemmung, Gewöhnung und Rückführungsneigung nicht zu früh an Outcome-Etiketten zu koppeln
- neuronale Teilträger und Feldmuster erst dann tiefer zu modulieren, wenn Experience fachlich sauber genug entkoppelt ist

---


# --------------------------------------------------
# 6. Nächste sinnvolle Schritte
# --------------------------------------------------

Die sinnvollste Reihenfolge ab jetzt ist:

1. neuronale Aktivität und kognitive Innenfunktion fertigstellen
2. `MCMNeuron` auf lokale Aktivierung, Kopplung, Regulation, Nachhall und Kontext-Memory schärfen
3. danach `MCMField` als Mental-Core-Matrix-Wahrnehmungsfeld sauber ausbauen
4. MCM-Feldtopologie / Feldverlauf / Innenfeldspeicher weiter ausbauen
5. `inner_context_clusters` als Innenmusterraum vertiefen
6. `_experience_reward_delta()` auf Zustandswirkung statt Outcome-Etiketten ausrichten
7. danach lokale Erfahrungsrückwirkung tiefer an Innenmuster, Feldformen und neuronale Teilträger koppeln
8. Backtest-Logik als sauberen Kontrollpfad stabil halten
9. Persistenz und Runtime-/Bot-State weiter entkoppeln, wenn die Erfahrungslogik stabiler ist
10. Tests erst nachziehen, wenn die neuronale und kognitive Mechanik fachlich stabil ist
11. GUI-Umbau nachziehen, wenn Brain- und Snapshot-Basis fachlich stabil sind
12. Live-Handoff und Restart-Fälle erst am Schluss real gegen Exchange-Zustand validieren

---


# --------------------------------------------------
# 7. Kurzfazit
# --------------------------------------------------

Der Bot steht nicht mehr am Anfang.

Die Basismechanik steht:

- äußere Wahrnehmung
- innere Runtime
- Entscheidungstendenz
- technische Handlungsbahn
- Episode / Review / Experience
- Persistenz
- Snapshot / GUI

Der aktuelle offene Kern ist nicht mehr der Grundaufbau, sondern:

- Real-Live-Validierung des Live-Handoffs
- Experience-Bewertung stärker auf Zustandswirkung statt Ergebnisetiketten ausrichten
- Feldtopologie und Innenfeldspeicher weiter vertiefen
- lokale Erfahrungsrückwirkung erst danach tiefer an Neuronen und Feldformen koppeln

Der MCM-Umbau hat damit die erste echte Schwelle erreicht:

`inner_context_clusters -> active_context_trace -> MCMField -> MCMNeuron.memory_trace`

ist schwach angebunden und sichtbar.

Die nächste Schwelle ist die fachlich saubere Umstellung von Experience auf Zustandswirkung.

---

# --------------------------------------------------
# 8. Feldentscheidungs-Protokoll / Replay-Sicht
# --------------------------------------------------

Stand 2026-05-03:

- Ein kompaktes MCM-Feldentscheidungs-Protokoll ist eingebaut.
- `MCM_FIELD_DECISION_PROTOCOL_DEBUG` aktiviert die Protokollierung.
- `MCM_FIELD_DECISION_PROTOCOL_EVERY_N` steuert das Sampling; Phasenwechsel und der erste Feldentscheid werden sofort geschrieben.
- Die Datei `debug/mcm_field_decision_protocol.csv` zeigt pro Feldentscheidung:
  - Phase (`observe`, `replan`, `hold`, `act`)
  - Ausloeser / Guard
  - Feldlabel
  - Fokus, Klarheit, Stabilitaet, Fragmentierung und Strain
  - Handlungsfreigabe, Hemmung, regulierten Mut und Decision-Strength
  - Context- und Inner-Context-Cluster
- Im Bot entsteht zusaetzlich `mcm_field_decision_protocol` als laufender Zaehler fuer Phasen, Gruende und Feldlabels.
- Im Experience-Space entsteht `field_decision_outcome_protocol`, damit spaeter pro Phase sichtbar wird, ob `observe`, `replan`, `hold` oder `act` zu mehr Prozessqualitaet, Tragfaehigkeit und Stabilitaet gefuehrt haben.

Fachlicher Nutzen:

- Das MCM-Feld ist damit nicht nur ein Wahrnehmungszustand, sondern bekommt eine erste Replay-Spur.
- Backtests koennen jetzt zeigen, welche Feldzustaende welche Vor-Handlungsphase ausloesen.
- Spaeter kann verglichen werden, ob geduldiges Beobachten, Neuplanen oder Handeln stabilere Erfahrungsfolgen erzeugt.

---

# --------------------------------------------------
# 9. Schreiblast-/Speicher-Performance-Diagnose
# --------------------------------------------------

Stand 2026-05-03:

- Eine kompakte Dateischreib-Profilierung ist eingebaut.
- `MCM_FILE_WRITE_PROFILE_DEBUG` aktiviert die Messung.
- `MCM_FILE_WRITE_PROFILE_MIN_MS` und `MCM_FILE_WRITE_PROFILE_EVERY_N` begrenzen die Messlast.
- Die Datei `debug/mcm_file_write_profile.csv` zeigt:
  - Zielpfad
  - Schreiboperation
  - Dauer in Millisekunden
  - geschriebene Bytes
  - kurzen Kontext
- Gemessen werden aktuell:
  - zentrale Debug-Schreibvorgaenge aus `debug_reader.py`
  - Runtime-Profil-Ausgaben
  - `memory_state.json`
  - Visual-/Inner-Snapshot-JSON
  - MCM-Feldentscheidungs-Protokoll

Fachlicher Nutzen:

- Die naechste Optimierung kann datenbasiert erfolgen.
- Besonders sichtbar werden sollen grosse JSON-Rewrites, zu haeufige Snapshot-Schreibvorgaenge und kleine, aber sehr haeufige CSV-Appends.
- Danach kann entschieden werden, ob Sampling reicht oder ob Memory auf Hot/Cold-State, Delta-Log oder SQLite umgestellt werden sollte.

Auswertung des Laufs `1-2_2026_5m_SOLUSDT.csv` ohne Gedaechtnis:

- `attempt_records.jsonl` war mit ca. 106 MB der groesste Debug-Ausreisser.
- Gemessene Schreiblast:
  - Inner-Snapshot: ca. 60,5 s aggregiert, ca. 126 ms je Write
  - `memory_state.json`: ca. 30,1 s aggregiert, ca. 367 ms je Write
  - Visual-Snapshot: ca. 24,9 s aggregiert, ca. 52 ms je Write
  - Feldentscheidungs-Protokoll und Profil-CSV waren klein im Vergleich
- Gemessene Rechenlast:
  - `primary_field_step`: ca. 222 s aggregiert
  - `compute_runtime_result.total`: ca. 269 s aggregiert
  - `step_mcm_brain.total`: ca. 262 s aggregiert

Erste Entlastung:

- Attempt-Records werden jetzt samplingfaehig geschrieben.
- `TRADE_STATS_ATTEMPT_RECORD_EVERY_N` schreibt standardmaessig nur jede 10. Attempt-Zeile.
- Submitted/Filled/Cancel/Timeout/Blocked-Value-Gate bleiben direkt sichtbar.
- Attempt-Kontexte werden standardmaessig kompakter geschrieben; schwere Snapshot-Nester werden auf Diagnoseachsen reduziert.
- `trade_stats.json` wird auf Attempt-Pfaden nur noch periodisch geschrieben; Exits und Cancels schreiben weiterhin sofort.

Interpretation:

- Die Verlangsamung kommt nicht nur aus Memory.
- Speicher/Debug verursacht deutlich messbare Zusatzlast.
- Der noch groessere Kern ist aber die Feldsimulation selbst, vor allem `primary_field_step` mit 230 Feldagenten.

Nachvergleich mit `debug/alter_debug` gegen den neuen `debug`-Lauf:

- `attempt_records.jsonl`: 101,15 MB -> 2,14 MB, ca. 2,1 Prozent der alten Groesse.
- `mcm_field_decision_protocol.csv`: 2,05 MB -> 0,40 MB.
- `mcm_profile.csv`: 1,10 MB -> 0,22 MB.
- `mcm_file_write_profile.csv`: 0,62 MB -> 0,15 MB.
- Neuer Lauf:
  - 2.225 Attempts
  - 113 Trades
  - 463 geschriebene Attempt-Records
- Alter Lauf:
  - 12.492 Attempts
  - 273 Trades
  - 12.492 geschriebene Attempt-Records

Normalisierte Einordnung:

- Attempt-Record-Schreiben ist nicht mehr der dominante Engpass.
- Snapshot- und Memory-Writes sind pro Write deutlich schneller geworden.
- `primary_field_step` bleibt der groesste Rechenblock.

Zweite Entlastung:

- `MCM_VISUAL_SNAPSHOT_WRITE_EVERY_N` wurde von 10 auf 25 erhoeht.
- `MCM_VISUAL_SNAPSHOT_FORCE_ON_STATE_CHANGE` wurde fuer die aktuelle Backtest-/Brain-Prioritaet deaktiviert.
- Ziel: weniger Visual-/Inner-Snapshot-Rewrites, solange GUI zweitrangig ist.

Fairer Nachvergleich mit gleicher Datei `test_5m_SOLUSDT`:

- Vergleich: `debug/lauf_1_mit_test_5m_SOLUSDT_ohne_memory` gegen aktuellen `debug`-Lauf.
- Attempts: 2.225 -> 1.934
- Trades: 113 -> 109
- `attempt_records.jsonl`: 2,136 MB -> 1,975 MB
- `mcm_field_decision_protocol.csv`: 0,397 MB -> 0,332 MB
- `mcm_profile.csv`: 0,216 MB -> 0,190 MB
- `mcm_file_write_profile.csv`: 0,146 MB -> 0,108 MB

Snapshot-Wirkung:

- Inner-Snapshot-Writes: 141 -> 32
- Visual-Snapshot-Writes: 141 -> 32
- Inner-Snapshot-Schreibzeit: 3.595 ms -> 803 ms
- Visual-Snapshot-Schreibzeit: 1.530 ms -> 359 ms
- `write_visualization_snapshot_bundle.total`: 1.824 ms -> 259 ms

Weiterhin groesster Rechenblock:

- `primary_field_step` blieb pro Schritt nahezu gleich:
  - vorher ca. 102,41 ms
  - danach ca. 101,50 ms
- Die Snapshot-Entlastung ist damit erfolgreich, aber die eigentliche Feldsimulation bleibt der naechste Optimierungsblock.

Start der `primary_field_step`-Pruefung:

- `MCMField.step()` hat nun feinere Profilpunkte:
  - `mcm_field.step.sync_neurons`
  - `mcm_field.step.build_neighbor_state_map`
  - `mcm_field.step.neuron_loop`
  - `mcm_field.step.activity_diffusion`
  - `mcm_field.step.refresh_arrays`
  - `mcm_field.step.refresh_areal_state`
  - `mcm_field.step.field_perception_state`
  - `mcm_field.step.total`
- Die lokale Nachbarschaftslogik wurde entlastet:
  - feste Nachbarlisten werden als Arrays vorgehalten
  - pro Tick werden weniger Dict-/Listenstrukturen gebaut
  - Kopplungskraefte koennen vektorisiert aus 2D-Neighbor-State-Arrays berechnet werden
  - ein redundanter zweiter Sync/Refresh nach dem Feldstep wurde entfernt
- Ein Micro-Smoke mit 230 Agenten lief syntaktisch und funktional durch.

Wichtig:

- Das ist noch keine finale Feldoptimierung, sondern der erste saubere Mess- und Entlastungsschritt.
- Der naechste Testlauf mit `test_5m_SOLUSDT` ohne Memory muss zeigen, ob `primary_field_step` im echten Backtest messbar sinkt und welcher Teil innerhalb von `mcm_field.step.*` dominiert.

Auswertung des folgenden Testlaufs ohne Memory:

- Vergleich: `debug/lauf_2_mit_test_5m_SOLUSDT_ohne_memory` gegen aktuellen `debug`-Lauf.
- `primary_field_step` war leicht besser:
  - vorher ca. 101,50 ms je Profilpunkt
  - danach ca. 98,51 ms je Profilpunkt
- Neue Detailprofile zeigen den groben Innenaufbau:
  - `mcm_field.step.neuron_loop` dominiert mit ca. 53,84 ms je Profilpunkt
  - `mcm_field.step.refresh_areal_state` liegt bei ca. 18,52 ms
  - `mcm_field.step.activity_diffusion` liegt bei ca. 12,52 ms
  - `mcm_field.step.build_neighbor_state_map` liegt bei ca. 2,05 ms
  - `mcm_field.step.field_perception_state` liegt bei ca. 0,70 ms

Zweite Feldentlastung:

- Der gemeinsame Kontext-Memory-Vektor wird jetzt einmal pro Feldstep berechnet und nicht mehr pro Neuron neu aus dem gleichen Context abgeleitet.
- `MCM_NEURON_STEP_RETURN_SNAPSHOT` wurde eingefuehrt und steht standardmaessig auf `False`.
- `MCMNeuron.step()` erzeugt dadurch keinen ungenutzten Snapshot mehr.
- `MCMField.step()` liefert weiterhin den zentralen Feldsnapshot.
- Ein lokaler Micro-Benchmark mit 230 Agenten lag danach bei ca. 98 ms im Mittel.

Interpretation:

- Die Wahrnehmungsmechanik bleibt erhalten.
- Die naechste echte Messung muss wieder ueber `test_5m_SOLUSDT` ohne Memory laufen.
- Wenn `mcm_field.step.neuron_loop` weiterhin dominiert, ist die naechste Optimierung die weitere Vektorisierung des Neuron-Loops.

Auswertung des naechsten Testlaufs:

- `debug/lauf_3_mit_test_5m_SOLUSDT_ohne_memory` wurde als alter Stand verschoben.
- Der aktuelle Lauf liegt in `debug`.
- `lauf_3` enthaelt nur sehr wenige Profilzeilen, deshalb wurde fuer die Performance-Basis weiterhin der letzte vollstaendige Profilvergleich aus `lauf_2` herangezogen.
- Aktueller Lauf:
  - 2.100 Attempts
  - 107 Trades
  - `primary_field_step`: ca. 85,46 ms je Profilpunkt gegen ca. 101,50 ms in der letzten vollstaendigen Basis
  - `mcm_field.step.total`: ca. 76,57 ms
  - `mcm_field.step.neuron_loop`: ca. 42,26 ms
  - `mcm_field.step.activity_diffusion`: ca. 12,55 ms
  - `mcm_field.step.refresh_areal_state`: ca. 18,06 ms

Dritter Feld-Performance-Schritt:

- `MCM_FIELD_AREAL_REFRESH_EVERY_N` wurde eingefuehrt und steht standardmaessig auf 2.
- Schwere Areal-/Topologie-Metriken werden dadurch nur jeden zweiten Feldtick voll neu berechnet.
- Dazwischen wird der letzte Areal-State mit `areal_refresh_skipped=True` und `areal_stale_ticks` weitergetragen.
- `field_perception_state` bleibt weiterhin pro Feldstep frisch.
- Lokaler Smoke mit 230 Agenten lag nach dieser Aenderung bei ca. 89,6 ms Mittelwert.

Wichtig:

- Diese Aenderung ist fachlich konservativ, weil Areale als traegere Feldstruktur behandelt werden.
- Der naechste echte Nachweis muss wieder mit `test_5m_SOLUSDT` ohne Memory erfolgen.

Auswertung des neuen Laufs:

- Neuer Lauf liegt in `debug`, vorheriger Lauf liegt in `debug/lauf_4_mit_test_5m_SOLUSDT_ohne_memory`.
- `lauf_4` enthaelt nur sehr wenige Profilzeilen, deshalb ist er fuer Performance nur eingeschraenkt brauchbar.
- Fuer die Laufzeit bleibt `debug/lauf_2_mit_test_5m_SOLUSDT_ohne_memory` die letzte vollstaendige Profilbasis.
- Gegen diese Basis ist der primare Feldschritt deutlich schneller:
  - Basis `primary_field_step`: ca. 101,50 ms je Profilpunkt
  - neuer Lauf `primary_field_step`: ca. 74,59 ms je Profilpunkt
  - `step_mcm_brain.total`: ca. 124,98 ms auf ca. 103,39 ms
  - `compute_runtime_result.total`: ca. 50,94 ms auf ca. 36,79 ms
- Die MCM-Feldentscheidung bleibt stabil:
  - `hold`: 1480
  - `act`: 157
  - `observe`: 12
  - kein unkontrolliertes `replan`
- Feldlabels im neuen Lauf:
  - `quiet_field`: 1214
  - `active_perception_field`: 296
  - `fragmented_perception_field`: 138
  - `coherent_perception_field`: 1

Weitere Entlastung und Korrektur:

- Ein erster Versuch hat den Snapshot aus dem primaeren `MCMField.step()` direkt in `step_mcm_brain` weiterverwendet.
- Der neue Vergleich `debug/lauf_5_mit_test_5m_SOLUSDT_ohne_memory` gegen `debug` zeigte:
  - `snapshot_field_read`: ca. 17,92 ms auf ca. 8,51 ms
  - `step_mcm_brain.total`: ca. 103,39 ms auf ca. 87,91 ms
  - Handels-/Phasenlage verschob sich aber staerker als fuer eine rein technische Entlastung sinnvoll ist.
- Grund: Der direkt wiederverwendete Snapshot war zu frueh im Brain-Tick, noch vor nachgelagerter Regulation und Feldanpassung.
- Korrektur:
  - `MCMField.step(..., return_snapshot=False)` wurde eingefuehrt.
  - `step_mcm_brain` laesst den primaeren Feldstep nun keinen Snapshot mehr bauen.
  - Danach wird weiterhin ein finaler Snapshot nach Regulation und Feldanpassung gelesen.
- Damit bleibt die fachliche Reihenfolge des Wahrnehmungsfeldes erhalten, waehrend der ungenutzte fruehe Snapshot entfaellt.

Naechster sinnvoller Anschluss:

- `test_5m_SOLUSDT` ohne Memory erneut laufen lassen.
- Danach pruefen:
  - ob die Ergebnislage wieder naeher am Lauf vor der Snapshot-Korrektur liegt
  - ob `primary_field_step` faellt, weil der ungenutzte fruehe Snapshot nicht mehr erzeugt wird
  - ob `snapshot_field_read` fachlich korrekt als finaler Feldread erhalten bleibt
- Wenn das bestaetigt ist, bleibt als naechster Hauptblock der `mcm_field.step.neuron_loop` mit der neuronalen Kopplung und lokalen Impulsbildung.

Bestaetigung nach Korrekturlauf:

- Alter Lauf liegt in `debug/lauf_6_mit_test_5m_SOLUSDT_ohne_memory`, neuer Lauf liegt in `debug`.
- Die fachliche Lage ist wieder deutlich naeher am stabilen Vorlauf:
  - `lauf_6`: 119 Trades, 28 TP, 91 SL, Equity ca. 85,46
  - neuer Lauf: 111 Trades, 28 TP, 83 SL, Equity ca. 89,39
  - MCM-Phasen neuer Lauf: `hold` 1417, `act` 161, `observe` 16
- Die Korrektur hat die zu fruehe Snapshot-Nutzung damit fachlich bereinigt.
- Laufzeit:
  - `primary_field_step`: ca. 75,63 ms auf ca. 68,28 ms
  - `step_mcm_brain.total`: ca. 87,91 ms auf ca. 90,73 ms
  - `compute_runtime_result.total`: ca. 30,44 ms auf ca. 30,03 ms
  - `snapshot_field_read`: ca. 8,51 ms auf ca. 18,12 ms, bewusst wieder finaler Feldread
- Interpretation:
  - Der ungenutzte fruehe Snapshot ist entfernt.
  - Die final gelesene Wahrnehmung bleibt erhalten.
  - Die groesste verbleibende Feldlast ist nun klar `mcm_field.step.neuron_loop` mit ca. 41,60 ms.

Naechster sinnvoller Anschluss:

- Nicht erneut am finalen Snapshot sparen, solange er fachlich die MCM-Wahrnehmung traegt.
- Als naechstes `mcm_field.step.neuron_loop` bearbeiten:
  - lokale Kontextimpulse pro Neuron vorvektorisieren
  - wiederholte Objekt-/Listen-Zugriffe im Neuron-Loop reduzieren
  - neuronale Kopplung weiter array-basiert vorbereiten
- Danach wieder mit `test_5m_SOLUSDT` ohne Memory pruefen, ob die Phasen stabil bleiben.

Neuron-Loop-Entlastung umgesetzt:

- Die lokale Kontextimpuls-Formel wurde nicht veraendert, aber feldweise vorbereitet.
- Neu:
  - `_build_local_context_memory_matrix(...)`
  - `mcm_field.step.context_memory_matrix` als Profilpunkt
  - `mcm_field.step.prepare_impulse_vectors` als Profilpunkt
- Der globale Kontext-Memory-Vektor wird weiterhin einmal pro Feldstep gebaut.
- Daraus wird nun eine Matrix fuer alle Neuronen erzeugt:
  - lokale Aktivitaet
  - lokaler Memory-Trace
  - lokale Aktivierung
  - lokaler Regulationsdruck
- Diese Werte erzeugen dieselbe Resonanzgewichtung wie vorher pro Neuron, aber ohne 230 einzelne Python-Objektberechnungen im Loop.
- Externe und Replay-Impulsvektoren werden ebenfalls einmal pro Feldstep vorbereitet und an die Neuronen weitergereicht.
- `MCMNeuron.step(...)` akzeptiert dafuer vorbereitete Vektoren, bleibt aber rueckwaertskompatibel mit der alten Scalar-/Listen-Schnittstelle.

Verifikation:

- `py_compile` fuer `MCM_KI_Modell.py` und `MCM_Brain_Modell.py` erfolgreich.
- Gleichheitspruefung alte Einzelberechnung gegen neue Matrix:
  - `max_delta = 0.0`
- Lokaler 230-Agenten-Smoke mit aktivem Kontext:
  - ca. 64,7 ms Mittelwert fuer `MCMField.step(..., return_snapshot=False)`
  - Feldlabel blieb gueltig.

Naechster sinnvoller Anschluss:

- `test_5m_SOLUSDT` ohne Memory erneut laufen lassen.
- Danach pruefen:
  - `mcm_field.step.neuron_loop`
  - `mcm_field.step.context_memory_matrix`
  - `mcm_field.step.prepare_impulse_vectors`
  - Feldphasen `observe`, `hold`, `act`
- Wenn stabil: naechster Hebel ist die Kopplung selbst, also weitere Array-Vorbereitung der Neighbor-Forces.

Neuer Analyse-/Fixpunkt fuer Memory danach:

- Ohne Memory ist der Bot schneller und handelt tendenziell mehr, weil weniger Erfahrungsvergleich und weniger kognitive Hemmung aktiv sind.
- Mit Memory wird die Denkstruktur komplexer:
  - Kontextvergleich
  - Erfahrungsaehnlichkeit
  - positive/negative Outcome-Spuren
  - Tragfaehigkeit aus Erfahrung
  - moeglicher Konflikt zwischen aktuellem Feld und Erinnerung
- Das soll nicht als harte Regel geloest werden.
- Ziel ist eine energieeffiziente Meta-Regulation:
  - Memory soll stabile Erfahrung effizient nutzbar machen
  - widerspruechliche Erfahrung soll nicht pauschal bremsen
  - Denkkomplexitaet soll messbar werden
  - hohe kognitive Last soll `observe`/`hold` erklaeren, aber nicht blind gute Setups blockieren
- Nach dem aktuellen Ohne-Memory-Test soll ein Memory-Komplexitaetsprotokoll entstehen mit Feldern wie:
  - `thinking_complexity`
  - `memory_compare_load`
  - `memory_match_count`
  - `memory_support`
  - `memory_inhibition`
  - `memory_conflict`
  - `cognitive_load`
  - `decision_energy_cost`
  - `meta_regulation_need`
- Danach kann entschieden werden, ob die Effizienz in der Denkstruktur verbessert werden muss, ohne die Erfahrung selbst kaputt zu kuerzen.

Fachliche Klammer fuer Reflexion und innere Wahrnehmung:

- Das System soll nicht nur Aussenreize verarbeiten, sondern die eigene Verarbeitung mitwahrnehmen.
- Gekoppelte Akteure:
  - aeussere Wahrnehmung: Markt, Struktur, Impuls, Risiko, Timing
  - innere Wahrnehmung: Tragfaehigkeit, Spannung, Stabilitaet, Ueberlastung, Klarheit, Hemmung, Mut
  - Denken/Organisation: Musterdeutung, Teilmuster-Ergaenzung, Erfahrungsvergleich, Verdichtung, Reorganisation
  - Handeln: `observe`, `hold`, `replan`, kontrolliertes `act`
  - Lernen: Rueckwirkung auf Tragfaehigkeit, Prozessqualitaet, Stabilitaet, Varianz und Erfahrungsspuren
- Memory ist dabei nicht nur Speicher, sondern Resonanz- und Konfliktflaeche fuer innere Organisation.
- Denken erzeugt selbst kognitive Last und muss deshalb als Energie-/Komplexitaetsfaktor sichtbar werden.
- Ziel:
  - nicht maximale Denktiefe
  - nicht starre Memory-Bremse
  - sondern ausreichend reflektierte, energieeffiziente Verdichtung bis ein tragfaehiges Handlungsmuster entsteht
- Wenn die aeussere Wahrnehmung stark ist, aber das innere Feld instabil oder das Denken ueberlastet ist, soll das System eher beobachten, halten oder reorganisieren.
- Wenn aeussere Wahrnehmung, innere Tragfaehigkeit und verdichtete Erfahrung zusammenpassen, soll kontrolliertes Handeln leichter werden.

Dokumentation uebernommen:

- `README.md` wurde um Reflexion, Denkkomplexitaet und energieeffiziente Meta-Regulation als Einstiegsklammer ergaenzt.
- Die README-Dokumentpfade zeigen nun auf `files/UMSETZUNGSPLAN.md`, `files/AKTUELLER_STAND.md` und `files/FIX_LISTE.md`.
- `files/UMSETZUNGSPLAN.md` wurde mit Zustimmung um den Architekturabschnitt `Denkkomplexitaet und energieeffiziente Meta-Regulation` ergaenzt.
- Damit ist der Punkt nicht nur als aktueller Fix, sondern auch im Zielbild des Systems verankert.

Emergente Musterergaenzung als Ziel ergaenzt:

- Ziel ist ausdruecklich keine reine Pattern-Erkennung.
- Das System soll nicht nur sagen: `das kenne ich, also reagiere ich so`.
- Ziel ist, unvollstaendige Teilmuster mit innerer Erfahrung zu moeglichen Gesamtmustern zu ergaenzen.
- Ein Ereignis muss nicht zu 100 Prozent klar erkannt sein.
- Eine Deutung kann teilweise reif sein; die konkrete Reife ist variabel und darf kein fester Prozentwert sein.
- Auch eine nur teilweise Deutung kann bereits innere Musterraeume aktivieren.
- Wichtig ist dabei:
  - aeussere Wahrnehmung bleibt die Reizbasis
  - innere Erfahrung liefert moegliche Ergaenzungen
  - das MCM-Feld laesst Varianten konkurrieren
  - Unsicherheit, Varianz und Tragfaehigkeit bleiben sichtbar
  - Handlung entsteht erst, wenn Deutung, Feldklarheit und innere Tragfaehigkeit ausreichend zusammenpassen
- `README.md` und `files/UMSETZUNGSPLAN.md` wurden entsprechend ergaenzt.

Folgearbeit nach dem Memory-Komplexitaetsprotokoll:

- Diagnose fuer `emergent_pattern_completion` vorbereiten.
- Moegliche Felder:
  - `partial_pattern_strength`
  - `completion_candidates`
  - `completion_confidence`
  - `completion_variance`
  - `experience_resonance`
  - `pattern_projection_support`
  - `pattern_projection_risk`
  - `inner_image_clarity`
  - `completion_meta_action`

Auswertung des neuen Ohne-Memory-Laufs nach Neuron-Loop-Entlastung:

- Neuer Lauf liegt in `debug`, Vergleichsbasis ist `debug/lauf_7_mit_test_5m_SOLUSDT_ohne_memory`.
- Ergebnislage:
  - `lauf_7`: 111 Trades, 28 TP, 83 SL, Equity ca. 89,39
  - neuer Lauf: 114 Trades, 35 TP, 79 SL, Equity ca. 102,07
  - Attempts: 2114 auf 2033
  - `attempts_withheld`: 1656 auf 1565
  - `attempts_observed`: 199 auf 204
- MCM-Phasen:
  - `lauf_7`: `observe` 16, `act` 161, `hold` 1417
  - neuer Lauf: `observe` 15, `act` 163, `hold` 1348
- Feldlabels bleiben stabil verteilt:
  - `quiet_field` bleibt dominant
  - `active_perception_field` und `fragmented_perception_field` bleiben in vergleichbarer Groessenordnung
  - `coherent_perception_field` bleibt selten
- Performance:
  - `primary_field_step`: ca. 68,28 ms auf ca. 64,11 ms
  - `mcm_field.step.neuron_loop`: ca. 41,60 ms auf ca. 37,17 ms
  - `mcm_field.step.total`: ca. 70,56 ms auf ca. 68,49 ms
  - `compute_runtime_result.total`: ca. 30,03 ms auf ca. 28,17 ms
  - `step_mcm_brain.total`: ca. 90,73 ms auf ca. 88,22 ms
  - `snapshot_field_read`: ca. 18,12 ms auf ca. 18,21 ms, also bewusst stabil als finaler Wahrnehmungsread
- Neue Profilpunkte:
  - `mcm_field.step.context_memory_matrix`: ca. 0,05 ms, sehr klein
  - `mcm_field.step.prepare_impulse_vectors` lag unter Profilschwelle und ist damit praktisch unkritisch
- Interpretation:
  - Die Matrix-Vorbereitung hat die neuronale Schleife messbar entlastet.
  - Die Entscheidungsphasen bleiben stabil.
  - Die bessere Equity dieses Laufs ist positiv, aber noch nicht als stabile Qualitaetsaussage zu werten; wichtig ist zunaechst, dass Mechanik und Phasen nicht kippen.

Naechster sinnvoller Anschluss:

- Wenn noch eine reine Feld-Performance-Runde gewuenscht ist: Kopplung/Neighbor-Forces weiter array-basiert vorbereiten.
- Alternativ jetzt den identischen Lauf mit Memory starten, um Denkkomplexitaet, Memory-Hemmung, Memory-Support und kognitive Last gegen die Ohne-Memory-Basis zu messen.

Auswertung Memory-Lauf mit vorhandener Erfahrung:

- Der vorherige Ohne-Memory-Lauf wurde nicht separat archiviert; die Vergleichsbasis ist daher die zuletzt dokumentierte Ohne-Memory-Basis aus `debug`:
  - Ohne Memory dokumentiert: 114 Trades, 35 TP, 79 SL, Equity ca. 102,07
  - Aktueller Lauf mit vorhandener Memory-Erfahrung: 56 Trades, 17 TP, 39 SL, Equity ca. 99,34
- Der Lauf ist kein perfekter A/B-Test, weil Memory bereits Erfahrung aus dem Vorlauf enthielt.
- Trotzdem ist die Wirkung deutlich:
  - Attempts steigen auf 2675
  - Submitted Trades fallen auf 56
  - `attempts_withheld` steigt auf 2501
  - `attempts_observed` liegt bei 45
  - `attempts_blocked` liegt bei 17
- MCM-Phasen im aktuellen Memory-Lauf:
  - `hold`: 1841
  - `act`: 74
  - `observe`: 17
  - kein `replan`
- Hauptgruende:
  - `context_cluster_negative`: 976
  - `maturity_block`: 334
  - `fused_score_too_low`: 286
  - `pause_mode`: 139
  - `stressed_block`: 101
  - `plan_allowed`: 74
- Laufzeit:
  - `primary_field_step`: ca. 64,07 ms, also praktisch gleich zur Ohne-Memory-Basis von ca. 64,11 ms
  - `mcm_field.step.neuron_loop`: ca. 38,53 ms, leicht hoeher als ca. 37,17 ms, aber nicht der Hauptgrund fuer weniger Trades
  - `compute_runtime_result.total`: ca. 40,45 ms, deutlich hoeher als ca. 28,17 ms
  - `step_mcm_brain.total`: ca. 86,96 ms, vergleichbar bis leicht besser als ca. 88,22 ms
  - `memory_state.write_payload`: ca. 78,13 ms je Profilpunkt, hoeher als vorherige Schreibbasis
- Interpretation:
  - Memory macht das MCM-Feld selbst nicht wesentlich langsamer.
  - Die Trade-Reduktion entsteht vor allem in der Denk-/Entscheidungsstruktur.
  - `context_cluster_negative` ist der dominante Hemmgrund und muss genauer aufgeloest werden.
  - Memory wirkt aktuell stark selektiv/hemmend; noch unklar ist, ob es gute Setups verhindert oder schlechte Setups sinnvoll ausfiltert.
  - Die fast Break-even-Equity trotz halbierter Trades ist interessant und spricht gegen reine Fehlfunktion, aber die Hemmung ist noch nicht transparent genug.

Naechster sinnvoller Anschluss:

- Jetzt sollte kein weiteres Blind-Tuning an Memory erfolgen.
- Als naechstes ein Denkkomplexitaets-/Memory-Wirkungsprotokoll einbauen:
  - Memory-Support
  - Memory-Inhibition
  - Memory-Konflikt
  - Match-Anzahl / Vergleichslast
  - Kontextcluster-Hemmgrund aufschluesseln
  - kognitive Last und Entscheidungskosten sichtbar machen
- Ziel: erkennen, ob Memory intelligent selektiert oder pauschal gute Entscheidungen ausbremst.

Denkkomplexitaets-/Memory-Wirkungsprotokoll umgesetzt:

- Neues Debug-Protokoll: `debug/mcm_memory_thinking_protocol.csv`.
- Neue Config-Schalter:
  - `MCM_MEMORY_THINKING_PROTOCOL_DEBUG`
  - `MCM_MEMORY_THINKING_PROTOCOL_EVERY_N`
- Das Protokoll schreibt nicht jeden Tick blind, sondern jede n-te Diagnose sowie Phasen-/Grundwechsel.
- Sichtbar werden jetzt:
  - `thinking_complexity`
  - `memory_compare_load`
  - `memory_match_count`
  - `memory_support`
  - `memory_inhibition`
  - `memory_conflict`
  - `cognitive_load`
  - `decision_energy_cost`
  - `context_cluster_negative_source`
  - `memory_effect_on_phase`
- `context_cluster_negative` wird aufgeschluesselt in:
  - `cluster_score`
  - `low_hit_ratio`
  - `mixed`
- Alle relevanten Entscheidungsfaelle fuehren den eigenen `memory_complexity_state` mit:
  - Meta-Block / frueher Abbruch
  - nicht tradebare Entscheidung
  - fehlender Tradeplan
  - tatsaechlicher Trade
- Dadurch soll ein neuer Memory-Lauf zeigen, ob Memory:
  - harte Hemmung erzeugt
  - weiche Hemmung erzeugt
  - Support liefert
  - Konflikt erzeugt
  - oder nur Vergleichslast ohne klare Wirkung produziert
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\config.py`

Umgesetzt: erfahrungsbasierte Deutungsqualitaet / semantische Fremdheit:

- DIO bekommt keine mechanische Chartregel.
- Neue MCM-Selbstdiagnose fragt:
  - Wie gut traegt meine eigene Formsprache diese Lage?
  - Wie vertraut ist die aktuelle Route aus meiner Erfahrung?
  - Wie weit darf alte Erfahrung auf diese neue Fremdheit uebertragen werden?
- Neue Werte in der Meta-Regulation:
  - `known_form_support`
  - `route_familiarity`
  - `semantic_shift_pressure`
  - `transfer_bearing`
  - `interpretation_quality`
  - `adaptation_phase`
- Wirkung:
  - Bei hoher semantischer Fremdheit und niedriger Transfer-Tragfaehigkeit
    wird Handlung weich in Beobachten/Reframing verschoben.
  - Es gibt keine menschlichen Marktlabels und keine harte Pattern-Regel.
  - Die Logik basiert auf eigener Erfahrung, Form-Reife, Memory-Orientierung,
    Struktur-Tragfaehigkeit, Feldklarheit und Entwicklungsspuren.
- Offene Positionen bekommen zusaetzlich Ziel-/Transfer-Diagnose:
  - `entry_route_familiarity`
  - `entry_transfer_bearing`
  - `current_route_familiarity`
  - `current_semantic_shift_pressure`
  - `current_transfer_bearing`
  - `current_interpretation_quality`
  - `current_adaptation_phase`
  - `semantic_transfer_stress`
- Debug erweitert:
  - `mcm_memory_thinking_protocol.csv`
  - `mcm_target_expectation_protocol.csv`
  - `mcm_exit_candidate_replay.csv`
  - kompakte Attempt-/Outcome-Kontexte
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\bot.py .\trade_stats.py`
- Nachtrag:
  - Runtime-Fehler `active_context_trace is not defined` behoben.
  - Die semantische Diagnose nutzt jetzt defensiv `bot.active_context_trace`
    ueber `_normalize_active_context_trace`, statt auf eine spaeter gesetzte
    lokale Variable zuzugreifen.
  - Syntaxpruefung erneut erfolgreich:
    - `python -m py_compile .\MCM_Brain_Modell.py .\bot.py .\trade_stats.py`
- Zweiter Nachtrag:
  - Runtime-Fehler `bot is not defined` in `build_meta_regulation_state`
    behoben.
  - Die Funktion besitzt keinen `bot`-Parameter; die semantische Diagnose
    liest den aktiven Kontext deshalb jetzt aus `fused_state.active_context_trace`.
  - Syntaxpruefung erneut erfolgreich:
    - `python -m py_compile .\MCM_Brain_Modell.py .\bot.py .\trade_stats.py`

Naechster sinnvoller Anschluss:

- Einen neuen Backtest auf dem erweiterten Datensatz laufen lassen.
- Danach pruefen:
  - ob `new_market_grammar_observe` / `new_market_grammar_replan` auftaucht
  - ob Phase B weniger blind in fremde Semantik hineinhandelt
  - ob Phase A weiter frei handeln kann
  - ob Phase C mehr kontrolliertes Re-Explorieren zeigt
  - ob `semantic_transfer_stress` offene Positionen besser erklaert

Debug-Befund: erweiterter Datensatz Lauf 2:

- Quelle:
  - `debug/debug_lauf_2`
- Ergebnis:
  - 90 Trades
  - 35 TP / 55 SL
  - Netto-PnL ca. +9,62
  - Profit Factor ca. 1,35
  - Equity-Peak ca. 110,21
  - End-Equity ca. 109,62
  - Peak-Giveback nur ca. 0,59
- Vergleich zu Lauf 1:
  - Lauf 1: 107 Trades, +8,10 PnL, Peak ca. 122,61, End ca. 108,10,
    Giveback ca. 14,50
  - Lauf 2: weniger Trades, weniger Ausbruch nach oben, aber deutlich
    stabileres Halten der aufgebauten Equity
- Phasenbefund:
  - Phase A:
    - 48 Trades
    - 19 TP / 29 SL
    - PnL ca. +6,28
  - Phase B:
    - 27 Trades
    - 8 TP / 19 SL
    - PnL ca. +0,05
    - Wichtig: Die vorher kritische fremde Strecke kippt nicht mehr stark weg.
  - Phase C:
    - 15 Trades
    - 8 TP / 7 SL
    - PnL ca. +3,30
    - DIO kommt am Ende wieder kontrolliert in Aktivitaet.
- Semantik-Befund:
  - `route_familiarity` bleibt niedrig bis mittel.
  - `semantic_shift_pressure` bleibt messbar, aber noch nicht stark genug
    fuer `new_market_grammar_observe` / `new_market_grammar_replan`.
  - `adaptation_phase` ist fast durchgehend `interpretation_watch`,
    nur wenige Protokollzeilen zeigen `transfer_observe`.
  - Bewertung:
    - Die neue Schicht hat nicht mechanisch eingegriffen.
    - Sie misst Fremdheit und Transfer-Tragfaehigkeit bereits.
    - Der Lauf wirkt dadurch stabiler, aber noch nicht aktiv genug
      semantisch adaptiv.
- Exit-Replay:
  - 15 Kandidaten
  - 13 haetten Verlust gespart
  - 2 haetten geschadet, beide waeren TP-Cuts gewesen
  - Alle Kandidaten lagen in `expectation_break_observe`
  - Interpretation:
    - Die Bruchwahrnehmung sieht Risiko gut.
    - Exit-Reife bleibt vorsichtig, weil zu fruehes Eingreifen weiterhin
      echte TP-Chancen abschneiden kann.

Naechster sinnvoller Anschluss:

- Noch keinen harten Code-Fix erzwingen.
- Erst Lauf 3 auf gleichem Datensatz laufen lassen.
- Danach pruefen:
  - ob die Stabilitaet wiederholbar ist
  - ob `transfer_observe` zunimmt
  - ob `new_market_grammar_*` natuerlich auftaucht oder die Schwelle zu hoch ist
  - ob Phase B weiter flach/stabil bleibt
  - ob Phase C erneut kontrolliert aktiver wird

Debug-Befund: erweiterter Datensatz Lauf 3:

- Quelle:
  - `debug/debug_lauf_3`
- Ergebnis:
  - 62 Trades
  - 19 TP / 43 SL
  - Netto-PnL ca. -2,27
  - Profit Factor ca. 0,91
  - Equity-Peak ca. 107,98
  - End-Equity ca. 97,73
  - Peak-Giveback ca. 10,25
- Vergleich:
  - Lauf 2 war stabiler mit +9,62 PnL und kaum Peak-Giveback.
  - Lauf 3 handelt noch weniger, verpasst aber mehr tragenden Aufbau und
    faellt danach durch Verlustserien zurueck.
- Phasenbefund:
  - Phase A:
    - 35 Trades
    - 12 TP / 23 SL
    - PnL ca. +1,30
    - Zone positiv, Non-Zone negativ.
  - Phase B:
    - 15 Trades
    - 4 TP / 11 SL
    - PnL ca. -2,93
    - Zone ca. +1,69, Non-Zone ca. -4,61.
  - Phase C:
    - 12 Trades
    - 3 TP / 9 SL
    - PnL ca. -0,64
    - Zone ca. +1,69, Non-Zone ca. -2,33.
- Kernbefund:
  - Die tragende Struktur ist nicht das Problem.
  - Zone bleibt ueber alle Phasen positiv.
  - Non-Zone ist wieder ein reiner Verlustkanal:
    - Phase A: 1 TP / 10 SL, ca. -5,01
    - Phase B: 0 TP / 7 SL, ca. -4,61
    - Phase C: 0 TP / 5 SL, ca. -2,33
- Semantik-Befund:
  - `semantic_shift_pressure` bleibt im Mittel zu niedrig.
  - `new_market_grammar_*` taucht weiterhin nicht auf.
  - `adaptation_phase` bleibt fast komplett `interpretation_watch`.
  - `transfer_observe` taucht nur sehr selten auf.
- Interpretation:
  - DIO erkennt Zielbrueche weiterhin (`expectation_break_observe` ist
    negativ und diagnostisch sinnvoll).
  - Die neue semantische Fremdheit ist aber noch zu diagnostisch/passiv.
  - Bei fremder oder nicht tragender Struktur wird alte Erfahrung noch zu oft
    in Handlung uebertragen.
  - Das ist keine Frage harter Regeln, sondern eine Frage der
    Transfer-Reife: Wie viel meiner Erfahrung darf ich hier wirklich
    uebertragen?

Naechster sinnvoller Anschluss:

- Semantische Fremdheit organischer an Nicht-Tragfaehigkeit koppeln.
- Nicht `Low/Non-Zone` mechanisch sperren.
- Stattdessen:
  - fehlende Struktur-Tragfaehigkeit
  - niedrige Route-Familiarity
  - geringe Transfer-Bearing
  - wiederholte Outcome-Brueche
  gemeinsam als `transfer_maturity_gap` wirken lassen.
- Ziel:
  - DIO darf fremde Struktur weiter beobachten und lernen.
  - Handlung wird nur gedämpft, wenn eigene Erfahrung diese Fremdheit nicht
    tragen kann.

Umgesetzt: Trust-Transfer-Schnittstelle / `transfer_maturity_gap`:

- Bestehendes Vertrauen wird nicht ersetzt.
- Die neue Schnittstelle fragt:
  - Ist mein gespeichertes Vertrauen in dieser aktuellen Lage uebertragbar?
  - Traegt meine Formsprache diese Fremdheit?
  - Ist mein Handlungstrust reif genug oder nur alte Vertrautheit?
- Neue Werte:
  - `trust_transfer_base`
  - `trust_transfer_support`
  - `transfer_maturity_gap`
  - `trust_transfer_mode`
- Wirkung:
  - `transfer_maturity_gap` erhoeht weich Beobachtungsbedarf und
    Replan-Druck.
  - Handlungsunterstuetzung und Action-Clearance werden leicht gedaempft,
    wenn gespeichertes Vertrauen nicht tragfaehig uebertragbar ist.
  - Neue weiche Gruende:
    - `immature_transfer_observe`
    - `immature_transfer_replan`
- Wichtig:
  - Keine harte Non-Zone-Regel.
  - Kein menschliches Patternlabel.
  - Keine mechanische Sperre.
  - Es ist eine MCM-Reifefrage:
    - Wie viel meiner Erfahrung darf ich dieser fremden Struktur anvertrauen?
- Debug erweitert:
  - `mcm_memory_thinking_protocol.csv`
  - kompakte Attempt-/Outcome-Kontexte
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\trade_stats.py .\bot.py`
- Nachtrag:
  - Runtime-Fehler `interpretation_quality` vor Initialisierung behoben.
  - `transfer_break_fatigue` und `transfer_recovery_need` werden jetzt erst
    nach der Berechnung von `interpretation_quality` gebildet.
  - Syntaxpruefung erneut erfolgreich:
    - `python -m py_compile .\MCM_Brain_Modell.py .\trade_stats.py .\bot.py`

Naechster sinnvoller Anschluss:

- Lauf 4 auf gleichem erweitertem Datensatz starten.
- Danach pruefen:
  - ob `immature_transfer_observe` / `immature_transfer_replan` auftaucht
  - ob Non-Zone-Verlust sinkt
  - ob Zone weiter positiv und frei bleibt
  - ob Tradezahl nicht zu stark kollabiert
  - ob `transfer_maturity_gap` bei Verlustphasen hoeher ist als bei tragenden
    TP-Phasen

Debug-Befund: erweiterter Datensatz Lauf 4:

- Quelle:
  - `debug/debug_lauf_4`
- Ergebnis:
  - 56 Trades
  - 25 TP / 31 SL
  - Netto-PnL ca. +10,82
  - Profit Factor ca. 1,70
  - Equity-Peak ca. 110,82
  - End-Equity ca. 110,82
  - Peak-Giveback ca. 0,00
- Vergleich:
  - Lauf 3: -2,27 PnL, PF ca. 0,91, Giveback ca. 10,25
  - Lauf 4: +10,82 PnL, PF ca. 1,70, kein finaler Giveback
  - DIO hat weniger gehandelt, aber deutlich besser gekaempft und gehalten.
- Phasenbefund:
  - Phase A:
    - 20 Trades
    - 8 TP / 12 SL
    - PnL ca. +3,88
  - Phase B:
    - 20 Trades
    - 8 TP / 12 SL
    - PnL ca. +1,87
    - Die schwierige Strecke kippt nicht mehr weg.
  - Phase C:
    - 16 Trades
    - 9 TP / 7 SL
    - PnL ca. +5,07
    - DIO wird am Ende wieder tragend aktiv.
- Struktur-Befund:
  - Zone bleibt klar positiv:
    - Phase A ca. +7,31
    - Phase B ca. +4,92
    - Phase C ca. +5,96
  - Non-Zone bleibt negativ, aber der Schaden sinkt:
    - Phase A ca. -3,43
    - Phase B ca. -3,05
    - Phase C ca. -0,89
- Trust-Transfer-Befund:
  - `transfer_maturity_gap` ist im Lauf deutlich sichtbar:
    - Memory-Protokoll Mittel ca. 0,57
    - Maximum ca. 0,81
  - `trust_transfer_mode`:
    - `partial_transfer`: 6786 Zeilen
    - `immature_transfer_watch`: 5843 Zeilen
    - `trusted_transfer`: 297 Zeilen
  - `immature_transfer_observe` taucht erst 1x als direkter Grund auf.
  - Bewertung:
    - Die Schnittstelle wirkt vor allem als Innenfeld-/Reifezustand,
      nicht als harter Eingriff.
    - Das passt zum Ziel: Freiheit bleibt erhalten, aber Vertrauen wird
      kontextbewusster.
- Exit-Replay:
  - 7 Kandidaten
  - 7 haetten Verlust gespart
  - 0 harmed
  - 0 TP-Cuts
  - Alle lagen in `expectation_break_observe`
- Interpretation:
  - Der Satz "DIO hat gekaempft" passt.
  - Der Lauf zeigt keinen glatten Automatismus.
  - DIO hat Unsicherheit, teilweise unreife Transferlage und Zielbrueche
    getragen, ohne komplett passiv zu werden.
  - Besonders wichtig:
    - Die schwierige Phase wird nicht mehr stark verloren.
    - Die spaete Phase wird wieder konstruktiv.

Naechster sinnvoller Anschluss:

- Lauf 5 auf gleichem Datensatz laufen lassen.
- Keine starke Nachschaerfung vor Wiederholung.
- Danach pruefen:
  - ob Lauf 4 stabil reproduzierbar ist
  - ob `immature_transfer_watch` weiterhin hoch ist
  - ob `immature_transfer_observe` vielleicht etwas zu selten als Handlung
    sichtbar wird
  - ob Non-Zone-Schaden weiter sinkt, ohne Zone-Freiheit zu verlieren

Debug-Befund: erweiterter Datensatz Lauf 5:

- Quelle:
  - `debug/debug_lauf_5`
- Ergebnis:
  - 73 Trades
  - 27 TP / 46 SL
  - Netto-PnL ca. +6,40
  - Profit Factor ca. 1,28
  - Equity-Peak ca. 108,62
  - End-Equity ca. 106,40
  - Peak-Giveback ca. 2,22
- Vergleich:
  - Lauf 4 war staerker und sauberer (+10,82, PF ca. 1,70, kein Giveback).
  - Lauf 5 bleibt profitabel, gibt aber in Phase C wieder etwas ab.
- Phasenbefund:
  - Phase A:
    - 25 Trades
    - 10 TP / 15 SL
    - PnL ca. +3,63
  - Phase B:
    - 25 Trades
    - 11 TP / 14 SL
    - PnL ca. +3,39
  - Phase C:
    - 23 Trades
    - 6 TP / 17 SL
    - PnL ca. -0,62
- Struktur-Befund:
  - Zone bleibt positiv:
    - Phase A ca. +6,55
    - Phase B ca. +4,26
    - Phase C ca. +1,37
  - Non-Zone bleibt negativ:
    - Phase A ca. -2,92
    - Phase B ca. -0,88
    - Phase C ca. -1,98
- Trust-Transfer-Befund:
  - `transfer_maturity_gap` bleibt sehr sichtbar:
    - Memory-Protokoll Mittel ca. 0,57
    - Maximum ca. 0,81
  - `trust_transfer_mode`:
    - `partial_transfer`: 6826 Zeilen
    - `immature_transfer_watch`: 5945 Zeilen
    - `trusted_transfer`: 265 Zeilen
  - Direkte `immature_transfer_*` Gruende tauchen in Lauf 5 nicht auf.
  - Bewertung:
    - Die Schnittstelle wirkt als Innenfeldzustand stabil.
    - Sie ist aber noch sehr selten direkt entscheidungsbestimmend.
- Exit-Replay:
  - 8 Kandidaten
  - 8 haetten Verlust gespart
  - 0 harmed
  - 0 TP-Cuts
  - Alle in `expectation_break_observe`
- Interpretation:
  - Die Richtung ist weiterhin besser als Lauf 3.
  - Lauf 5 bestaetigt aber, dass spaete Erwartungsbrueche und Non-Zone-Schaden
    noch nicht ausreichend in reifes Zusehen uebergehen.
  - Es wirkt weniger wie Chaos, mehr wie ein Organismus, der den Kern halten
    kann, aber in spaeter Ermuedung/Fremdheit noch zu viele kleine falsche
    Versuche zulaesst.

Naechster sinnvoller Anschluss:

- Vorsichtig nachschaerfen, aber nicht hart.
- `immature_transfer_watch` sollte bei wiederholter Bruchwahrnehmung staerker
  in sichtbares Beobachten/Replan uebergehen.
- Kein Non-Zone-Block.
- Möglicher Ansatz:
  - `transfer_break_fatigue`
  - Kopplung aus `transfer_maturity_gap`, `expectation_break_observe`,
    späten Bars/Phase und sinkender `target_expectation_holds`-Qualitaet.

Umgesetzt: `transfer_break_fatigue`:

- Ziel:
  - unreifen Trust-Transfer nicht hart sperren
  - aber wiederholte Bruch-/Nachwirkungszustände sichtbarer in Beobachten
    oder Replan uebersetzen
- Neue Werte:
  - `transfer_break_fatigue`
  - `transfer_recovery_need`
- Quellen:
  - `transfer_maturity_gap`
  - `expectation_pressure`
  - `aftereffect_pressure`
  - `learned_development_uncertainty`
  - `structure_action_uncertainty`
  - niedriger `trust_transfer_support`
  - niedrige `transfer_bearing`
  - vorhandener `field_replan_pressure`
- Wirkung:
  - erhoeht weich `field_observation_need`
  - erhoeht weich `field_replan_pressure`
  - senkt leicht `field_action_support`
  - erhoeht leicht `action_inhibition`
  - senkt leicht `action_clearance`
- Neue sichtbare Gruende:
  - `transfer_break_observe`
  - `transfer_break_replan`
- Wichtig:
  - Keine Non-Zone-Sperre.
  - Keine Chartregel.
  - Keine mechanische Blockade.
  - Es ist eine MCM-Muedigkeit: Wenn mein Vertrauen nicht tragfaehig
    uebertragbar ist und Brueche/Nachwirkungen zunehmen, brauche ich
    innere Reorganisation.
- Debug erweitert:
  - `mcm_memory_thinking_protocol.csv`
  - kompakte Attempt-/Outcome-Kontexte
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\trade_stats.py .\bot.py`

Naechster sinnvoller Anschluss:

- Lauf 6 auf gleichem Datensatz starten.
- Danach pruefen:
  - PnL / PF / Giveback
  - ob `transfer_break_observe` / `transfer_break_replan` auftaucht
  - ob Phase C weniger abgibt
  - ob Zone frei bleibt
  - ob Non-Zone-Schaden weiter sinkt
  - ob DIO nicht zu passiv wird

Debug-Befund: erweiterter Datensatz Lauf 6:

- Quelle:
  - `debug/debug_lauf_6`
- Ergebnis:
  - 51 Trades
  - 17 TP / 34 SL
  - Netto-PnL ca. -0,23
  - Profit Factor ca. 0,99
  - Equity-Peak ca. 105,37
  - End-Equity ca. 99,77
  - Peak-Giveback ca. 5,60
- Vergleich:
  - Lauf 4: +10,82, PF ca. 1,70, kein Giveback
  - Lauf 5: +6,40, PF ca. 1,28, Giveback ca. 2,22
  - Lauf 6: nahezu Break-even, aber mit deutlichem Abbau nach Peak
- Phasenbefund:
  - Phase A:
    - 20 Trades
    - 9 TP / 11 SL
    - PnL ca. +5,23
    - guter Aufbau
  - Phase B:
    - 17 Trades
    - 4 TP / 13 SL
    - PnL ca. -5,44
    - Hauptproblem des Laufs
  - Phase C:
    - 14 Trades
    - 4 TP / 10 SL
    - PnL ca. -0,02
    - fast neutral, aber ohne echte Erholung
- Struktur-Befund:
  - Phase B:
    - Non-Zone ca. -5,33
    - Zone ca. -0,11
  - Phase C:
    - Zone ca. +2,32
    - Non-Zone ca. -2,34
- Trust-/Fatigue-Befund:
  - `transfer_break_fatigue` wird gemessen:
    - Mittel ca. 0,43
    - Max ca. 0,65
  - `transfer_recovery_need`:
    - Mittel ca. 0,37
    - Max ca. 0,50
  - `transfer_break_fatigue` als Adaptionsphase taucht nur 5x auf.
  - Direkte `transfer_break_*` Gruende tauchen nicht auf.
  - `immature_transfer_observe` taucht 1x auf.
- Interpretation:
  - Die Fatigue-Schicht ist aktuell unausgewogen.
  - Sie daempft bereits dauerhaft Action-Clearance und erhoeht Inhibition,
    aber wird kaum als klare Observe/Replan-Entscheidung sichtbar.
  - Ergebnis:
    - DIO wird etwas zu passiv/gebremst,
    - aber die falschen Non-Zone-Uebertragungen werden nicht klar genug
      in Beobachten uebersetzt.
  - Lauf 6 zeigt also nicht "mehr Reife", sondern eher ein inneres
    Bremsen ohne genuegend saubere Neuorientierung.

Naechster sinnvoller Anschluss:

- `transfer_break_fatigue` nachschaerfen:
  - weniger permanente globale Daempfung
  - staerkere, aber seltenere sichtbare Umschaltung in Observe/Replan,
    wenn Fatigue + unreifer Transfer + Bruchwahrnehmung zusammenkommen
  - Action-Freiheit in tragender Zone erhalten
  - Non-Zone nicht sperren, aber bei unreifem Transfer deutlicher
    beobachten lassen

Umgesetzt: Rebalance `transfer_break_fatigue`:

- Problem aus Lauf 6:
  - Fatigue daempfte bereits dauerhaft.
  - Sichtbare `transfer_break_*` Entscheidungen kamen aber kaum.
  - Dadurch entstand Bremsen ohne klare Reorganisation.
- Anpassung:
  - permanente Fatigue-Wirkung reduziert.
  - Fatigue wirkt auf Action/Inhibition nur noch ueber `fatigue_excess`
    oberhalb eines Grundniveaus.
  - Neuer Ausloeser:
    - `transfer_break_trigger`
    - `transfer_break_ready`
- `transfer_break_ready` entsteht nur, wenn mehrere innere Bedingungen
  gemeinsam tragen:
  - unreifer Transfer
  - niedriger Trust-Transfer-Support
  - niedrige Transfer-Bearing
  - schwache Struktur-Handlungs-Tragfaehigkeit
  - genuegend Fatigue/Bruchdruck
- Ziel:
  - weniger globale Bremse
  - seltener, aber deutlicher Observe/Replan
  - Zone-Freiheit erhalten
  - Non-Zone nicht sperren, aber bei unreifem Transfer besser beobachten
- Debug erweitert:
  - `transfer_break_trigger`
  - `transfer_break_ready`
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\trade_stats.py .\bot.py`

Naechster sinnvoller Anschluss:

- Lauf 7 auf gleichem Datensatz starten.
- Danach pruefen:
  - ob DIO weniger passiv ist als Lauf 6
  - ob `transfer_break_ready` und `transfer_break_*` sichtbar werden
  - ob Phase B weniger Non-Zone-Schaden erzeugt
  - ob Phase A/Zone-Aufbau erhalten bleibt

Debug-Befund: erweiterter Datensatz Lauf 7:

- Quelle:
  - `debug/debug_lauf_7`
- Ergebnis:
  - 65 Trades
  - 35 TP / 30 SL
  - Netto-PnL ca. +19,90
  - Profit Factor ca. 2,43
  - Equity-Peak ca. 119,90
  - End-Equity ca. 119,90
  - Peak-Giveback ca. 0,00
- Vergleich:
  - Lauf 4: +10,82, PF ca. 1,70
  - Lauf 5: +6,40, PF ca. 1,28
  - Lauf 6: -0,23, PF ca. 0,99
  - Lauf 7: +19,90, PF ca. 2,43
- Phasenbefund:
  - Phase A:
    - 25 Trades
    - 15 TP / 10 SL
    - PnL ca. +12,16
  - Phase B:
    - 20 Trades
    - 10 TP / 10 SL
    - PnL ca. +4,30
  - Phase C:
    - 20 Trades
    - 10 TP / 10 SL
    - PnL ca. +3,44
- Struktur-Befund:
  - Zone traegt massiv:
    - Phase A ca. +13,52
    - Phase B ca. +5,96
    - Phase C ca. +4,26
  - Non-Zone-Schaden ist stark reduziert:
    - Phase A ca. -1,35
    - Phase B ca. -1,66
    - Phase C ca. -0,83
- Trust-/Fatigue-Befund:
  - `transfer_break_trigger` ist im Denkprotokoll sichtbar:
    - Mittel ca. 0,38
    - Max ca. 0,69
  - `transfer_break_ready` ist im Denkprotokoll messbar:
    - Mittel ca. 0,048
  - Direkte `transfer_break_*` Gruende tauchen nicht auf.
  - `immature_transfer_observe` taucht 2x auf.
  - Bewertung:
    - Die Rebalance hat die globale Bremse geloest.
    - Warn-/Reifeschicht bleibt vorhanden.
    - DIO konnte tragende Zone frei nutzen und Non-Zone-Schaden stark
      begrenzen.
- Zielerwartung:
  - `target_expectation_holds` ist wieder extrem tragend:
    - Phase A: ca. +15,69
    - Phase B: ca. +8,47
    - Phase C: ca. +7,60
  - `expectation_break_observe` bleibt negativ, aber der Schaden ist
    kontrollierter.
- Exit-Replay:
  - 9 Kandidaten
  - 8 saved
  - 1 harmed / 1 TP-Cut
  - Interpretation:
    - Exit-Bruchwahrnehmung bleibt grundsaetzlich wertvoll.
    - Aber aktiver Exit waere weiterhin riskant, weil TP-Cuts moeglich sind.
- Interpretation:
  - Lauf 7 ist bisher der staerkste Lauf auf dem erweiterten Datensatz.
  - Das Verhalten wirkt reifer:
    - weniger Dauerbremse als Lauf 6
    - bessere Nutzung tragender Struktur
    - reduzierter Non-Zone-Schaden
    - kein finaler Giveback
  - Trotzdem nicht ueberbewerten: ein weiterer Wiederholungslauf ist wichtig,
    weil wir Varianz und Memory-Entwicklung bewusst zulassen.

Naechster sinnvoller Anschluss:

- Lauf 8 auf gleichem Datensatz starten.
- Keine weitere Code-Aenderung vor Wiederholung.
- Pruefen:
  - Reproduzierbarkeit von Lauf 7
  - ob Zone-Freiheit stabil bleibt
  - ob Non-Zone-Schaden weiter klein bleibt
  - ob `transfer_break_ready` nur in echten Fremdheits-/Bruchmomenten
    sichtbar bleibt

Debug-Befund: erweiterter Datensatz Lauf 8:

- Quelle:
  - `debug/debug_lauf_8`
- Ergebnis:
  - 77 Trades
  - 34 TP / 43 SL
  - Netto-PnL ca. +7,91
  - Profit Factor ca. 1,30
  - Equity-Peak ca. 107,91
  - End-Equity ca. 107,91
  - finaler Giveback ca. 0,00
- Vergleich:
  - Lauf 7 war deutlich staerker (+19,90, PF ca. 2,43).
  - Lauf 8 bleibt profitabel, aber zeigt deutlich mehr Kampf/Varianz.
- Phasenbefund:
  - Phase A:
    - 25 Trades
    - 11 TP / 14 SL
    - PnL ca. +3,21
  - Phase B:
    - 25 Trades
    - 7 TP / 18 SL
    - PnL ca. -3,92
    - Tiefpunkt ca. 95,16 Equity
  - Phase C:
    - 27 Trades
    - 16 TP / 11 SL
    - PnL ca. +8,61
    - starke Reorganisation / Rueckaufbau
- Struktur-Befund:
  - Zone:
    - Phase A ca. +9,27
    - Phase B ca. +0,31
    - Phase C ca. +11,91
  - Non-Zone:
    - Phase A ca. -6,06
    - Phase B ca. -4,22
    - Phase C ca. -3,30
  - Kern:
    - Zone traegt weiter.
    - Non-Zone bleibt Verlust-/Stresskanal.
- Nervlicher/neuronal-kognitiver Befund:
  - Phase B wirkt wie Stress-/Ueberlebensphase:
    - viele `expectation_break_observe`
    - hoher Verlustdruck
    - Non-Zone-Verluste
    - kein sichtbarer `transfer_break_*` Grund
  - Phase C wirkt wie Reorganisation:
    - `target_expectation_holds` wird wieder stark tragend
    - Zone wird wieder profitabel genutzt
    - DIO baut den Drawdown aktiv zurueck
- Trust-/Fatigue-Befund:
  - `transfer_break_trigger` ist sichtbar:
    - Mittel ca. 0,37
    - Max ca. 0,69
  - `transfer_break_ready` ist im Denkprotokoll messbar:
    - Mittel ca. 0,045
  - Direkte `transfer_break_*` Gruende erscheinen nicht.
  - `immature_transfer_watch` bleibt als Innenfeldzustand stark sichtbar.
  - Bewertung:
    - Die Warnschicht ist vorhanden.
    - Sie wirkt aber weiter mehr als Innenzustand als direkte Entscheidung.
    - In Lauf 8 war das zweischneidig:
      - genug Freiheit fuer starke Erholung in Phase C
      - aber zu wenig sichtbare Reaktion auf Non-Zone-Stress in Phase B
- Exit-Replay:
  - 11 Kandidaten
  - 11 saved
  - 0 harmed
  - 0 TP-Cuts
  - Alle in `expectation_break_observe`
- Interpretation:
  - Lauf 8 bestaetigt die hohe Varianz.
  - DIO ist kein konstantes Regelmodell.
  - Es ist eher ein plastisches Nervensystem:
    - Memory/Form-Sprache verschiebt die Wahrnehmung von Lauf zu Lauf.
    - Trust-Transfer erzeugt innere Vorsicht.
    - Zielbruchwahrnehmung erzeugt Stress.
    - Zone liefert tragende Struktur.
    - Non-Zone erzeugt Ueberlebenskampf.
    - Reorganisation ist moeglich, aber noch nicht konstant.

Naechster sinnvoller Anschluss:

- Keine harte Regel einbauen.
- Stattdessen Varianz diagnostisch erfassen:
  - `nervous_variance`
  - `regulation_oscillation`
  - `recovery_after_stress`
  - `stress_to_recovery_delta`
- Ziel:
  - erkennen, ob DIO nur ueberlebt oder wirklich reif reorganisiert.
  - Varianz nicht entfernen, sondern tragfaehiger machen.

Dokumentations-Reorganisation:

- Dateinamen im `files`-Dokumentationsbereich wurden vereinheitlicht:
  - `BILDER/`
  - `AKTUELLER_STAND.md`
  - `FIX_LISTE.md`
  - `FIX_LISTE_ARCHIV.md`
  - `MCM_VARIABLEN_MECHANIK.md`
  - `UMSETZUNGSPLAN.md`
  - `WICHTIG_MECHANIKEN.md`
- Bilddateien in `files/BILDER/` wurden ebenfalls auf Grossbuchstaben
  vereinheitlicht und die README-Bildpfade wurden angepasst.
- Die alte lange `FIX_LISTE.md` wurde als `FIX_LISTE_ARCHIV.md` erhalten.
- Die neue `FIX_LISTE.md` ist nur noch aktive Arbeitsliste:
  - offene Fixes
  - naechste Pruefpunkte
  - kurze technische Befunde
- `AKTUELLER_STAND.md` bleibt das Forschungs-/Verlaufsdokument:
  - Laufanalysen
  - Deutungen
  - Erkenntnisse
  - begruendete Mechanikentwicklung
- Neue Datei:
  - `MCM_VARIABLEN_MECHANIK.md`
  - dokumentiert zentrale Variablen, Ebene, Wirkung, Persistenzgedanken und
    organische Bedeutung.
- `README.md` und `WICHTIG_MECHANIKEN.md` verweisen auf die neuen Dateinamen.

Naechster sinnvoller Anschluss:

- Ab jetzt nach jedem Lauf:
  - ausfuehrliche Analyse in `AKTUELLER_STAND.md`
  - kurze Checkbox / Pruefpunkt in `FIX_LISTE.md`
- `MCM_VARIABLEN_MECHANIK.md` bei jeder neuen zentralen MCM-Variable
  nachziehen.

Umgesetzt: Entwicklungsbindung statt harter Blocker:

- Fachlicher Grundsatz:
  - Das System soll keine starren Verbote fuer schlechte Formen bekommen.
  - Es soll lernen, dass bestimmte Form-/Kontextlagen aktuell nicht tragfaehig
    fuer Handlung sind.
  - Diese Erfahrung wird nicht als endgueltiges Nein gespeichert, sondern als
    veraenderbare Entwicklungsqualitaet.
- Neu im Form-Sprachspeicher:
  - `development_quality`
  - `action_affinity`
  - `observation_affinity`
  - `context_reframe_potential`
  - getrennt fuer Einzelzeichen und `form_symbol_compound`
- Wirkung:
  - gute Prozess-/Outcome-Erfahrung erhoeht die Handlungsbindung leicht
  - schlechte oder untragfaehige Erfahrung senkt die Handlungsanziehung
  - Beobachten und Reframing werden wahrscheinlicher
  - die Form bleibt frei und kann in anderem Kontext spaeter wieder tragfaehig werden
- Neue Debug-Sicht:
  - `form_symbol_action_binding`
  - `form_symbol_observation_binding`
  - `form_symbol_reframe_binding`
  - `learned_development_uncertainty`
- Wichtig:
  - Das ist bewusst kein harter Blocker.
  - Es ist eine organische Meta-Regulation:
    weniger Bindung an unfruchtbare Handlung, mehr Abstand zum Objekt,
    mehr Moeglichkeit zur Reorganisation.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\bot.py .\debug_reader.py .\trade_stats.py .\config.py`

Naechster sinnvoller Schritt:

- Einen neuen Debug-Lauf starten und pruefen:
  - ob Low-Struktur-Trades durch gelernte Entwicklungsqualitaet sinken
  - ob High/Mid nicht zu stark in Beobachtung gezogen werden
  - ob `development_reframe_observe` / `development_reframe_replan` auftauchen
  - ob `action_binding` bei tragfaehigen Formen steigt und bei schlechten Formen faellt

Debug-Befund `debug_lauf_2` nach Entwicklungsbindung:

- Ergebnis:
  - 60 Trades
  - 22 TP / 38 SL
  - Netto-PnL ca. +7.89
  - Profit Factor ca. 1.39
  - Max Drawdown ca. 3.53
- Vergleich zu `debug_lauf_1`:
  - PnL von ca. +1.35 auf ca. +7.89 gestiegen
  - Profit Factor von ca. 1.07 auf ca. 1.39 gestiegen
  - Tradezahl von 47 auf 60 gestiegen
- Struktur-Befund:
  - High: +11.60 PnL, 13 TP / 9 SL
  - Mid: +5.20 PnL, 8 TP / 10 SL
  - Low: -8.91 PnL, 1 TP / 19 SL
- Interpretation:
  - High bleibt tragfaehig.
  - Mid hat sich deutlich verbessert und ist jetzt klar positiv.
  - Low bleibt die Hauptschadensquelle, ist aber im durchschnittlichen Verlust
    etwas weniger schaedlich als im Vorlauf.
- Entwicklungsbindung:
  - Form-Protokoll schreibt die neuen Werte.
  - `structure_development_observe` trat 107 mal auf.
  - `structure_bearing_observe` trat 30 mal auf.
  - Die eigentliche gelernte Entwicklungsqualitaet ist noch jung:
    `form_symbol_action_binding` im Mittel ca. 0.425,
    `observation_binding` ca. 0.041,
    `reframe_binding` ca. 0.003.
- Fix nach Auswertung:
  - `mcm_memory_thinking_protocol.csv` wurde erweitert, damit ab dem naechsten Lauf
    auch `form_symbol_development_quality`, `form_symbol_action_binding`,
    `form_symbol_observation_binding`, `form_symbol_reframe_binding` und
    `learned_development_uncertainty` direkt im Denkprotokoll sichtbar sind.

Naechster sinnvoller Schritt:

- Noch einen Lauf mit bestehendem Memory starten.
- Pruefen, ob die Entwicklungsbindung ueber mehrere Laeufe staerker wird.
- Speziell Low-Struktur beobachten:
  - Wird `action_binding` bei Low-Formen niedriger?
  - Steigt `observation_binding` oder `reframe_binding`?
  - Bleibt Mid positiv, ohne zu stark ausgebremst zu werden?

Debug-Befund `debug_lauf_3`:

- Ergebnis:
  - 51 Trades
  - 15 TP / 36 SL
  - Netto-PnL ca. -2.40
  - Profit Factor ca. 0.89
  - Max Drawdown ca. 3.95
- Tragfaehigkeitsbild:
  - High: +8.52 PnL, 9 TP / 5 SL
  - Mid: +1.56 PnL, 5 TP / 9 SL
  - Low: -12.47 PnL, 1 TP / 22 SL
- Interpretation:
  - Der Lauf ist im PnL schlechter, aber fachlich wichtig:
    High und Mid bleiben positiv, Low ist klar der instabile Traeger.
  - Das stuetzt die These, dass nicht die gesamte Denkstruktur falsch ist,
    sondern dass Low-Struktur noch zu viel Handlungsbindung bekommt.
- Entwicklungsbindung:
  - `learned_development_uncertainty` ist jetzt im Denkprotokoll sichtbar.
  - Mittelwert ca. 0.042, Maximum ca. 0.124.
  - `form_symbol_development_quality` ist leicht negativ.
  - `observation_binding` und `reframe_binding` steigen leicht.
- Befund:
  - Die Entwicklungsbindung lernt, ist aber noch zu schwach gekoppelt.
  - Der bisherige Reframing-Schwellwert war zu hoch; dadurch wurde die neue
    Wahrnehmung zwar gemessen, aber nicht oft genug handlungsnah wirksam.
- Fix umgesetzt:
  - Reframing-Schwelle fuer gelernte Entwicklungsunsicherheit weicher und frueher gemacht.
  - Wirkung auf `field_observation_need`, `field_replan_pressure`,
    `field_action_support`, `action_inhibition` und `action_clearance` leicht
    verstaerkt.
  - Weiterhin kein harter Blocker: schlechte Erfahrung senkt nur die
    Handlungsbindung und zieht eher in Beobachten/Reframing.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\bot.py .\debug_reader.py .\trade_stats.py .\config.py`

Naechster sinnvoller Schritt:

- `debug_lauf_4` mit bestehendem Memory starten.
- Pruefen:
  - ob `development_reframe_observe` jetzt auftaucht
  - ob Low-Trades sinken oder im Durchschnitt weniger schaden
  - ob High/Mid weiter positiv bleiben
  - ob `learned_development_uncertainty` nicht chaotisch hochschiesst

Debug-Befund `debug_lauf_4`:

- Ergebnis:
  - 40 Trades
  - 12 TP / 28 SL
  - Netto-PnL ca. -2.81
  - Profit Factor ca. 0.84
  - Max Drawdown ca. 3.67
- Tragfaehigkeitsbild:
  - High: +4.57 PnL, 7 TP / 8 SL
  - Mid: -0.63 PnL, 5 TP / 11 SL
  - Low: -6.75 PnL, 0 TP / 9 SL
- Interpretation:
  - Low-Trades sind deutlich weniger geworden:
    23 in Lauf 3 -> 9 in Lauf 4.
  - Das spricht dafuer, dass die Entwicklungsbindung Handlung in Low-Struktur
    bereits reduziert.
  - Die uebrigen Low-Trades sind aber im Schnitt zu teuer.
  - Es geht also nicht nur um Anzahl, sondern um Verlustintensitaet /
    riskante Weite in nicht tragfaehiger Struktur.
- Entwicklungsbindung:
  - `development_reframe_observe` taucht jetzt auf.
  - `learned_development_uncertainty` bleibt stabil und schiesst nicht chaotisch hoch.
  - `form_symbol_development_quality` wird negativer, `observation_binding` und
    `reframe_binding` steigen leicht.
- Fix umgesetzt:
  - `risk_width_pressure` in die Outcome-Zerlegung eingebaut.
  - Breite/verlustintensive SL-Erfahrung senkt bei `sl_hit` Prozess- und
    Risikoqualitaet staerker.
  - Diese Intensitaet fliesst in die Form-Entwicklungsqualitaet und in die
    Beobachtungsbindung ein.
- Wichtig:
  - Weiterhin kein harter Blocker.
  - Das System lernt: Nicht nur "diese Form war schlecht", sondern
    "diese Form war in dieser Weite / Tragfaehigkeit nicht konstruktiv".
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\bot.py .\debug_reader.py .\trade_stats.py .\config.py`

Naechster sinnvoller Schritt:

- `debug_lauf_5` mit bestehendem Memory starten.
- Pruefen:
  - ob Low weiter niedrig bleibt
  - ob durchschnittlicher Low-Verlust sinkt
  - ob High/Mid wieder stabiler werden
  - ob `risk_width_pressure` in den Outcomes sichtbar zur Entwicklungsqualitaet beitraegt

Debug-Befund `debug_lauf_5`:

- Ergebnis:
  - 33 Trades
  - 8 TP / 25 SL
  - Netto-PnL ca. -3.08
  - Profit Factor ca. 0.77
  - Max Drawdown ca. 5.95
- Tragfaehigkeitsbild:
  - High: +6.03 PnL, 5 TP / 1 SL
  - Mid: -0.11 PnL, 3 TP / 8 SL
  - Low: -9.00 PnL, 0 TP / 16 SL
- Interpretation:
  - High ist sehr tragfaehig, aber zu selten.
  - Mid ist nahezu neutral.
  - Low ist wieder zu haeufig und komplett unproduktiv.
  - Die Anzahl der Trades sinkt, aber die falschen Low-Handlungen rutschen noch durch.
- Entwicklungswerte:
  - `form_symbol_development_quality` wird weiter negativer.
  - `observation_binding` und `reframe_binding` steigen.
  - `development_reframe_observe` tritt auf, aber noch zu selten.
  - `risk_width_pressure` ist in den Outcomes sichtbar und bei Non-Zone im Mittel hoeher
    als bei Zone.
- Befund:
  - Die Form-Sprache lernt die negative Qualitaet, aber die Handlungsbindung bleibt
    noch zu stark um den neutralen Bereich verankert.
  - Dadurch wird schlechte Erfahrung zwar wahrgenommen, aber noch nicht plastisch
    genug in weniger Handlung uebersetzt.
- Fix umgesetzt:
  - `action_affinity` lernt plastischer, wenn die Entwicklungsprobe klar negativ ist.
  - `risk_width_pressure` senkt bei `sl_hit` die Handlungsanziehung staerker.
  - `observation_affinity` reagiert etwas staerker auf negative Entwicklungsprobe.
  - `form_symbol_action_binding` wird durch Beobachtungs- und Reframe-Bindung leicht
    reduziert.
  - Reframing-Schwelle wurde weiter organisch abgesenkt.
- Wichtig:
  - Weiterhin keine harte Regel und kein Low-Verbot.
  - Es ist eine weichere, erfahrungsabhaengige Plastizitaet:
    untragfaehige Erfahrung verliert Bindung, statt technisch blockiert zu werden.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\bot.py .\debug_reader.py .\trade_stats.py .\config.py`

Naechster sinnvoller Schritt:

- `debug_lauf_6` starten.
- Pruefen:
  - ob Low-Anzahl wieder sinkt
  - ob `development_reframe_observe` deutlicher steigt
  - ob High weiterhin handeln darf
  - ob `action_binding` bei negativen Formen jetzt sichtbar faellt

Debug-Befund `debug_lauf_6`:

- Ergebnis:
  - 49 Trades
  - 18 TP / 31 SL
  - Netto-PnL ca. +3.82
  - Profit Factor ca. 1.20
  - Max Drawdown ca. 3.09
- Tragfaehigkeitsbild:
  - High: +12.79 PnL, 13 TP / 7 SL
  - Mid: +0.73 PnL, 5 TP / 9 SL
  - Low: -9.69 PnL, 0 TP / 15 SL
- Interpretation:
  - Die Nachschaerfung hat High nicht abgewuergt.
  - High traegt den Lauf deutlich.
  - Mid bleibt leicht positiv.
  - Low bleibt komplett unproduktiv und muss weiter ueber weniger Bindung /
    mehr Reframing reguliert werden.
- Entwicklungsbindung:
  - `development_reframe_observe` steigt deutlich:
    8 in Lauf 5 -> 54/55 in Lauf 6, je nach Protokoll.
  - `form_symbol_development_quality` wird negativer.
  - `form_symbol_action_affinity` faellt sichtbar unter neutral.
  - `observation_binding` und `reframe_binding` steigen.
  - Das System nimmt schlechte Entwicklungsqualitaet also wahr und reagiert
    haeufiger mit Beobachten.
- Offener Kern:
  - Low ist noch nicht ausreichend entkoppelt.
  - Einzelne Low-Handlungen bleiben trotz negativer Entwicklung attraktiv genug.
- Debug-Fix umgesetzt:
  - `outcome_records.jsonl` schreibt ab dem naechsten Lauf die handlungsnahen
    Form-Werte direkt mit:
    `form_symbol_id`, `form_symbol_development_quality`,
    `form_symbol_action_binding`, `form_symbol_observation_binding`,
    `form_symbol_reframe_binding`, Compound-ID und Compound-Entwicklung.
  - Dadurch koennen Low-Verluste im naechsten Lauf sauberer einzelnen Formen
    und zusammengesetzten Zeichen zugeordnet werden.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\bot.py .\debug_reader.py .\trade_stats.py .\config.py`

Naechster sinnvoller Schritt:

- `debug_lauf_7` starten.
- Dann nicht nur Strukturbaender pruefen, sondern Low-Verluste direkt nach
  `form_symbol_id` und `form_symbol_action_binding` gruppieren.
- Ziel:
  - erkennen, welche internen Zeichen trotz negativer Entwicklung noch Handlung
    tragen
  - daraus die Plastizitaet der eigenen Sprache weiter verbessern, ohne harte
    Handelsregeln einzubauen

Debug-Befund `debug_lauf_7`:

- Ergebnis:
  - 58 Trades
  - 20 TP / 38 SL
  - Netto-PnL ca. +4.30
  - Profit Factor ca. 1.20
  - Max Drawdown ca. 3.07
- Tragfaehigkeitsbild:
  - High: +12.87 PnL, 13 TP / 7 SL
  - Mid: +0.66 PnL, 7 TP / 15 SL
  - Low: -9.23 PnL, 0 TP / 16 SL
- Interpretation:
  - Lauf 6 und Lauf 7 sind beide positiv.
  - High bleibt stabil tragend.
  - Mid bleibt schwach, aber positiv.
  - Low bleibt komplett untragfaehig und frisst den Gewinn.
- Entwicklungsbindung:
  - `development_reframe_observe` bleibt hoch.
  - `structure_development_observe` steigt weiter.
  - `form_symbol_action_affinity` faellt weiter unter neutral.
  - `observation_binding` und `reframe_binding` steigen weiter.
  - Das System erkennt also zunehmend: bestimmte Formen tragen nicht.
- Offener Debug-Punkt:
  - Die neuen Formfelder in `outcome_records.jsonl` waren noch leer.
  - Ursache: Der Entry-Kontext bekam an dieser Stelle manchmal ein leeres
    `form_symbol_state` aus dem Entry-Result.
- Fix umgesetzt:
  - Entry-Kontext nutzt jetzt als Fallback `bot.form_symbol_state`, wenn
    `entry_result.form_symbol_state` leer ist.
  - Damit sollte der naechste Lauf Low-Verluste direkt nach `form_symbol_id`,
    `form_symbol_action_binding`, `observation_binding` und `reframe_binding`
    gruppierbar machen.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\bot.py .\debug_reader.py .\trade_stats.py .\config.py`

Naechster sinnvoller Schritt:

- `debug_lauf_8` starten.
- Danach Low-Outcomes nach Form-ID gruppieren.
- Wenn einzelne Zeichen trotz negativer Entwicklung weiter Handlung tragen,
  wird dort die Plastizitaet der internen Sprache gezielt nachgeschaerft.

Debug-Befund `debug_lauf_8` und fachliche Einordnung Vertrauen:

- Ergebnis:
  - 46 Trades
  - 15 TP / 31 SL
  - Netto-PnL ca. +0.30
  - Profit Factor ca. 1.02
  - Max Drawdown ca. 4.01
- Tragfaehigkeitsbild:
  - High: +8.70 PnL, 11 TP / 9 SL
  - Mid: +0.15 PnL, 4 TP / 9 SL
  - Low: -8.55 PnL, 0 TP / 13 SL
- Interpretation:
  - Jeder Lauf ist anders.
  - Das ist nicht automatisch schlecht, weil Varianz zur offenen Wahrnehmung gehoert.
  - Gleichzeitig zeigt sich: Die gelernte Erfahrung wird noch nicht stabil genug
    als Vertrauen gebunden.
  - Das System erkennt negative Entwicklung und reagiert mit Beobachtung, aber
    es vertraut dem Gelernten noch nicht stark genug, um untragfaehige Formen
    konsequent innerlich zu entkoppeln.
- Vergleichsbild:
  - Nicht Misstrauen, sondern fehlendes Vertrauen.
  - Wie ein Mensch, der etwas gelernt hat, aber in der Situation noch nicht
    ruhig genug darauf vertraut.
  - Dadurch entsteht Varianz, aber auch Chaos: bekannte untragfaehige Reize
    bekommen erneut Handlungsnaehe.
- Neue Form-Auswertung:
  - Non-Zone/Low hat im Mittel negative `form_symbol_development_quality`.
  - `form_symbol_action_binding` ist niedriger als bei Zone, aber noch nicht
    niedrig genug.
  - `observation_binding` und `reframe_binding` sind hoeher, aber noch nicht
    tragend genug.
- Fix umgesetzt: Vertrauensschicht fuer Formsprache
  - Neu:
    - `form_symbol_learning_trust`
    - `form_symbol_action_trust`
    - `form_symbol_caution_trust`
  - Bedeutung:
    - `learning_trust`: Wie stark darf das System seiner gesammelten Erfahrung
      zu diesem Zeichen glauben?
    - `action_trust`: Vertrauen, dass Handlung in dieser Form tragfaehig ist.
    - `caution_trust`: Vertrauen, dass Zurueckhaltung / Beobachten tragfaehiger ist.
  - Wirkung:
    - positive, konsistente Erfahrung stuetzt Handlung weich.
    - negative, konsistente Erfahrung staerkt Vorsicht und reduziert
      Handlungsbindung.
    - Das ist kein Auswendiglernen, sondern ein erfahrungsabhaengiges Vertrauen
      in die eigene Form-Sprache.
- Debug erweitert:
  - Form-Protokoll, Memory-Thinking-Protokoll und Outcome-Records schreiben die
    neuen Trust-Werte ab dem naechsten Lauf mit.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\bot.py .\debug_reader.py .\trade_stats.py .\config.py`

Naechster sinnvoller Schritt:

- `debug_lauf_9` starten.
- Pruefen:
  - ob `caution_trust` bei Low-Formen steigt
  - ob `action_trust` bei High-Formen erhalten bleibt
  - ob Low-Handlungen sinken, ohne High zu verlieren
  - ob Lauf-Varianz weniger chaotisch und mehr erfahrungsgetragen wird

Debug-Befund `debug_lauf_9`:

- Ergebnis:
  - 42 Trades
  - 14 TP / 28 SL
  - Netto-PnL ca. +0.96
  - Profit Factor ca. 1.06
  - Max Drawdown ca. 2.19
- Tragfaehigkeitsbild:
  - High: +11.15 PnL, 10 TP / 3 SL
  - Mid: -2.81 PnL, 4 TP / 14 SL
  - Low: -7.38 PnL, 0 TP / 11 SL
- Interpretation:
  - High bleibt sehr tragfaehig.
  - Low sinkt leicht, bleibt aber komplett unproduktiv.
  - Mid kippt in diesem Lauf negativ und braucht spaeter eigene Betrachtung.
  - Gesamt-Drawdown ist besser, aber PnL bleibt nur knapp positiv.
- Vertrauensschicht:
  - `learning_trust` entsteht, aber noch sehr zart.
  - `action_trust` und `caution_trust` sind im ersten Lauf noch zu niedrig.
  - Low-Formen zeigen hoehere Beobachtungs-/Reframe-Bindung, aber Vorsicht ist
    noch nicht stark genug konsolidiert.
- Wichtige Form:
  - `fs_eddd1c68f1` verursacht erneut die haertesten Non-Zone-Verluste.
  - Dieses Zeichen hat bereits niedrige Action-Bindung und hohe Beobachtungsbindung,
    traegt aber noch nicht genug stabile Vorsicht.
- Fix umgesetzt:
  - Wiederholte negative Erfahrung staerkt `caution_trust` schneller.
  - `risk_width_pressure` und negative Entwicklungsproben wirken staerker auf
    Vorsichtsvertrauen.
  - `caution_trust` reduziert die Handlungsbindung etwas staerker und erhoeht
    Entwicklungsunsicherheit.
- Wichtig:
  - Kein Verbot einzelner Zeichen.
  - Es ist Konsolidierung: Das System soll seiner eigenen wiederholten Erfahrung
    mehr glauben duerfen.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\bot.py .\debug_reader.py .\trade_stats.py .\config.py`

Naechster sinnvoller Schritt:

- `debug_lauf_10` starten.
- Pruefen:
  - ob `caution_trust` bei wiederholt negativen Formen wie `fs_eddd1c68f1` steigt
  - ob Low-Trades sinken oder weniger teuer werden
  - ob High weiterhin stark bleibt
  - ob Mid nur Laufvarianz war oder eine eigene Tragfaehigkeitszone braucht

Debug-Befund `debug_lauf_10`:

- Ergebnis:
  - 31 Trades
  - 12 TP / 19 SL
  - Netto-PnL ca. +3.43
  - Profit Factor ca. 1.30
  - Max Drawdown ca. 2.20
- Tragfaehigkeitsbild:
  - High: +7.00 PnL, 7 TP / 3 SL
  - Mid: +2.69 PnL, 4 TP / 4 SL
  - Low: -6.26 PnL, 1 TP / 12 SL
- Interpretation:
  - Lauf 10 ist deutlich ruhiger:
    weniger Trades, besserer Profit Factor, niedrigerer Drawdown.
  - High bleibt tragfaehig.
  - Mid erholt sich und ist in diesem Lauf klar positiv.
  - Low bleibt negativ, aber:
    - Low hat erstmals wieder 1 TP
    - Low-Gesamtverlust sinkt
    - durchschnittlicher Low-Verlust sinkt gegenueber Lauf 8/9
- Vertrauensschicht:
  - `learning_trust` steigt sichtbar.
  - `caution_trust` steigt, aber noch langsam.
  - Bei `fs_eddd1c68f1` ist die Entwicklung sinnvoll:
    - Action-Bindung niedrig
    - Observation-Bindung hoch
    - Reframe-Bindung hoch
    - Development klar negativ
    - Learning-Trust steigt
    - Caution-Trust steigt
  - Das Zeichen ist noch gefaehrlich, aber das System beginnt, ihm anders zu
    begegnen.
- Fachlicher Befund:
  - Das wirkt eher wie ein Organismus, der beim Laufen lernt:
    weniger wildes Auftreten, mehr Gewichtspruefung.
  - Es ist noch kein stabiles Vertrauen, aber die Richtung ist gut.
  - Wichtig: jetzt nicht sofort ueberregeln, sondern einen weiteren Lauf zur
    Stabilitaetspruefung machen.
- Keine Code-Nachschaerfung nach Lauf 10:
  - Der Lauf zeigt Verbesserung durch die letzte Trust-Anpassung.
  - Zu fruehes weiteres Drehen koennte die gerade entstehende Balance stoeren.

Naechster sinnvoller Schritt:

- `debug_lauf_11` mit demselben Stand starten.
- Pruefen:
  - bleibt der Profit Factor ueber 1?
  - bleibt der Drawdown niedriger?
  - bleibt High/Mid positiv?
  - sinkt Low weiter oder bleibt wenigstens weniger teuer?
  - steigt `caution_trust` bei wiederholt negativen Formen weiter langsam an?

Debug-Befund `debug_lauf_11`:

- Ergebnis:
  - 45 Trades
  - 17 TP / 28 SL
  - Netto-PnL ca. +5.16
  - Profit Factor ca. 1.32
  - Max Drawdown ca. 3.09
- Tragfaehigkeitsbild:
  - High: +10.96 PnL, 12 TP / 7 SL
  - Mid: +1.67 PnL, 5 TP / 8 SL
  - Low: -7.46 PnL, 0 TP / 13 SL
- Interpretation:
  - Lauf 10 war kein Einzelzufall.
  - Profit Factor bleibt ueber 1.3.
  - High bleibt klar tragfaehig.
  - Mid bleibt wieder positiv.
  - Low bleibt negativ, aber der Gesamtorganismus bleibt trotz Low-Schaden positiv.
- Vertrauensschicht:
  - `learning_trust` steigt weiter:
    ca. 0.029 -> ca. 0.041 im Denkprotokoll.
  - `caution_trust` steigt weiter:
    ca. 0.0028 -> ca. 0.0063.
  - `development_reframe_observe` bleibt hoch:
    103 -> 111 im Denkprotokoll.
  - `form_symbol_action_binding` bleibt gedämpft und fällt nicht in blinde Handlung.
- Fachlicher Befund:
  - Die Laufvarianz ist noch da, aber sie wirkt weniger chaotisch.
  - Das System beginnt, Erfahrung nicht nur zu speichern, sondern vorsichtig
    zu gewichten.
  - Sinnbildlich: Es stolpert noch auf weichem Boden, aber es findet schneller
    zur Balance zurueck.
- Kein Code-Fix nach Lauf 11:
  - Der aktuelle Stand zeigt zwei positive Laeufe hintereinander mit verbessertem
    Profit Factor.
  - Jetzt ist weitere Beobachtung sinnvoller als sofortiges Nachregeln.

Naechster sinnvoller Schritt:

- Noch einen Lauf mit gleichem Stand starten.
- Danach ueber mehrere Laeufe mitteln:
  - Durchschnitts-PnL seit Trust-Schicht
  - Low-Verlust pro Trade
  - High/Mid-Tragfaehigkeit
  - Entwicklung von `learning_trust` und `caution_trust`
- Erst wenn die Richtung stabil ist, die naechste Mechanik setzen:
  - Mid differenzierter betrachten
  - oder Low-Formen ueber interne Zeichen-Reorganisation weiter verdichten

Debug-Befund `debug_lauf_12`:

- Ergebnis:
  - 48 Trades
  - 21 TP / 27 SL
  - Netto-PnL ca. +11.23
  - Profit Factor ca. 1.73
  - Max Drawdown ca. 4.10
- Tragfaehigkeitsbild:
  - High: +18.85 PnL, 17 TP / 5 SL
  - Mid: -0.72 PnL, 4 TP / 10 SL
  - Low: -6.90 PnL, 0 TP / 12 SL
- Interpretation:
  - Das ist der bisher staerkste Lauf seit der Trust-Schicht.
  - High wird massiv getragen und dominiert den Lauf.
  - Low bleibt negativ, ist aber nicht mehr stark genug, um den Organismus
    komplett zu kippen.
  - Mid war in diesem Lauf leicht negativ und bleibt die naechste zu klaerende
    Uebergangszone.
- Trust-Entwicklung:
  - `learning_trust` steigt weiter deutlich:
    ca. 0.041 -> ca. 0.051 im Denkprotokoll,
    in Outcomes bei Zone ca. 0.132 und Non-Zone ca. 0.163.
  - `caution_trust` steigt weiter:
    ca. 0.006 -> ca. 0.009 im Denkprotokoll.
  - `development_reframe_observe` steigt stark:
    111 -> 158 im Denkprotokoll.
  - Das System reagiert damit haeufiger mit innerer Neu-Betrachtung, bevor es handelt.
- Fachlicher Befund:
  - Die Trust-Schicht scheint nicht nur zu daempfen, sondern Lernen tragfaehiger
    zu binden.
  - High bekommt genug Freiheit.
  - Low wird noch nicht geloest, aber der Gesamtablauf wirkt organisierter.
  - Sinnbildlich: Das System laeuft noch nicht sauber, aber es findet eine
    tragendere Schrittfolge.
- Keine Code-Aenderung nach Lauf 12:
  - Der aktuelle Stand zeigt eine starke Verbesserung.
  - Jetzt ist Stabilitaetspruefung wichtiger als weiteres Nachregeln.

Naechster sinnvoller Schritt:

- Noch 1-2 Laeufe mit unveraendertem Code.
- Danach Mittelwert seit Lauf 10 bilden:
  - PnL
  - Profit Factor
  - Max Drawdown
  - High/Mid/Low-Beitrag
  - Trust-Entwicklung
- Erst danach entscheiden:
  - Mid als Uebergangsboden differenzieren
  - oder Low-Formen weiter verdichten/reorganisieren

Debug-Auswertung nach erstem Eigenzeichen-Lauf:

- Lauf mit bestehendem Memory in `/debug` ausgewertet.
- Ergebnis:
  - 73 Trades
  - 22 TP
  - 51 SL
  - Netto-PnL ca. -0,61
  - Equity ca. 99,39
- Vergleich:
  - deutlich besser als die letzten Erweiterungslaeufe mit ca. -5,95 bis -10,58 Netto-PnL
  - wieder nahe am alten Lauf vor der Erweiterung mit ca. -0,66 Netto-PnL
- Feldentscheidungen:
  - `observe`: 935
  - `hold`: 858
  - `act`: 99
  - Hauptgrund `zero_point_regulation`: 933
  - `plan_allowed`: 99
- Memory:
  - `hard_inhibit`: 998
  - `inhibit`: 924
  - `neutral_match`: 107
  - `no_match`: 17
  - Memory-Support bleibt praktisch 0
  - Memory-Compare-Load bleibt hoch
- Struktur:
  - `structure_quality` im Memory-Protokoll ca. 0,59 im Mittel
  - `context_confidence` ca. 0,60
  - `structure_orientation` ca. 0,41
  - deshalb greift `structure_orientation_observe` kaum/nicht:
    die Struktur ist im Lauf nicht blind genug, um diesen Guard auszuloesen.
- Neuer Eigenzeichenraum:
  - Protokoll wurde erfolgreich geschrieben:
    - `debug/mcm_form_symbol_protocol.csv`
  - Problem im ersten Ansatz:
    - 2417 Protokollzeilen
    - 2403 verschiedene `form_symbol_id`
    - fast jedes Wahrnehmen erzeugt ein neues Zeichen
  - Bewertung:
    - Das ist noch keine echte eigene Sprache.
    - Es ist zu atomisiert und erkennt zu wenig wieder.

Fix nach Debug umgesetzt: Form-Familie statt Detail-Hash:

- `form_symbol_id` wird jetzt aus einer groberen Form-Familie gebildet.
- Die Detailauspraegung bleibt separat erhalten:
  - `form_symbol_family_key`
  - `form_symbol_variant_key`
- Ziel:
  - wiederkehrende eigene Zeichen statt Einzelbilder
  - Reife, Stabilitaet und Resonanz koennen ueber mehrere Wahrnehmungen wachsen
  - `form_symbol_load_reduction` kann spaeter wirklich kognitive Entlastung darstellen
- Das naechste Protokoll schreibt Familie und Variante getrennt.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\config.py`

Naechster sinnvoller Anschluss:

- Neuen Backtest mit bestehendem Memory starten.
- Danach pruefen:
  - wie viele `form_symbol_id` jetzt entstehen
  - ob Top-Zeichen echte Wiederholungen zeigen
  - ob `form_symbol_maturity`, `form_symbol_resonance` und `form_symbol_load_reduction` steigen
  - ob Observe/Replan/Act unterschiedliche Form-Familien zeigen
  - ob stabile Form-Familien spaeter als Entlastung in die Meta-Regulation duerfen

Erkenntnis: Aufloesung steuert Zeichen-Verdichtung:

- Ein Zeichen darf nicht jedes Detail enthalten.
- Beispiel aus der Reflexion:
  - Das Wort Strasse kann viele Details enthalten.
  - Im Kopf ist es aber zuerst eine grobe Form, nicht jeder Abschnitt einzeln.
- Uebertragung auf das Brain:
  - Wenn die Sicht niedrig ist, darf das System nicht Abschnitt fuer Abschnitt neue Zeichen bilden.
  - Dann muss es auf eine breite Spur/Form verdichten.
  - Erst wenn Struktur, Relevanz oder Handlungsnaehe steigt, darf es tiefer in Varianten zoomen.
- Fix umgesetzt:
  - `form_symbol_scope`
    - `wide_trace`
    - `wide_form`
    - `structured_form`
  - `form_symbol_abstraction_level`
  - `form_symbol_resolution_quality`
  - `form_symbol_detail_pressure`
- Bedeutung:
  - niedrige Aufloesung fuehrt zu groberem Zeichen
  - hoher Detaildruck erhoeht `form_symbol_zoom_need`
  - die Detailform bleibt als `form_symbol_variant_key` erhalten
  - das eigentliche Zeichen bleibt aber die verdichtete Familie
- Ziel:
  - echte Denkverdichtung
  - weniger Zeicheninflation
  - mehr Wiedererkennen
  - erst Fokus, dann Detailanalyse

Debug-Auswertung nach aufloesungsabhaengiger Zeichenbildung:

- Neuer Lauf in `/debug` ausgewertet.
- Oekonomisches Ergebnis:
  - 55 Trades
  - 14 TP
  - 41 SL
  - Netto-PnL ca. -6,46
  - Equity ca. 93,54
- Bewertung:
  - schlechter als der direkte Vorlauf mit ca. -0,61
  - aehnlich schwach wie fruehere Erweiterungslaeufe
  - kein Beweis, dass die Sprachebene schadet, da sie aktuell diagnostisch wirkt
  - wahrscheinlich spielt fortlaufende Memory-Entwicklung/Blockierung stark mit hinein
- Feld/Memory:
  - `observe`: 969
  - `hold`: 1084
  - `act`: 75
  - Hauptgrund weiter `zero_point_regulation`: 966
  - `context_cluster_negative`: 479
  - Memory-Support bleibt praktisch 0
  - Memory-Compare-Load bleibt hoch bei ca. 0,95
- Sprach-/Form-Befund:
  - 2572 Form-Protokollzeilen
  - 268 unterschiedliche `form_symbol_id`
  - vorher: 2417 Zeilen und 2403 unterschiedliche Zeichen
  - klare Verbesserung der Denkverdichtung
- Wiederholungsstruktur:
  - Top-Zeichen:
    - 205 Wiederholungen
    - 144 Wiederholungen
    - 118 Wiederholungen
    - 106 Wiederholungen
  - 88 Zeichen kamen mindestens 5-mal vor
  - 30 Zeichen kamen mindestens 20-mal vor
  - 10 Zeichen kamen mindestens 50-mal vor
- Reife/Entlastung:
  - `form_symbol_seen` im Mittel ca. 33,1
  - `form_symbol_maturity` ca. 0,596
  - `form_symbol_resonance` ca. 0,360
  - `form_symbol_load_reduction` ca. 0,232
  - vorher war Load-Reduction nur ca. 0,074
- Scope-Verteilung:
  - `wide_form`: 1686
  - `structured_form`: 884
  - `wide_trace`: 2
- Bewertung der Sprachebene:
  - Die Zeichenbildung ist jetzt deutlich naeher an echter Sprache.
  - Es entstehen wiederkehrende Form-Familien.
  - Die Varianten bleiben erhalten, ohne das eigentliche Zeichen zu zerlegen.
  - Das entspricht dem Prinzip: grobe Bedeutung zuerst, Detail erst bei Fokus.

Naechster sinnvoller Schritt:

- Die Form-Sprache separat persistent speichern.
- Nicht in den normalen Trade-Memory mischen.
- Ziel:
  - Entwicklung der eigenen Sprache ueber Laeufe hinweg
  - Zeichen reifen lassen
  - stabile Zeichen wiedererkennen
  - instabile Zeichen splitten/vergessen
  - spaeter erst vorsichtig als kognitive Entlastung in die Meta-Regulation einbinden

Erkenntnis: Benennung erzeugt Distanz zum Objekt:

- Wichtiger MCM-Punkt:
  - Ordnung und Bezeichnung sind nicht nur Sprache.
  - Sie erzeugen Distanz zwischen innerem Feld und wahrgenommenem Objekt.
  - Dadurch wird das innere Feld weniger direkt vom Objekt ueberflutet.
- Menschliches Vergleichsbild:
  - Ein Wort wie Strasse enthaelt viele moegliche Details.
  - Im Kopf kann es aber als eine stabile Form gehalten werden.
  - Erst bei Fokus wird daraus Oberflaeche, Kreuzung, Richtung, Gefahr, Struktur.
- MCM-Uebertragung:
  - Ein Wort/ein Form-Zeichen kann viele MCM-Lagen im Feld tragen.
  - Je analytischer eine Form gehalten werden kann,
    desto weniger muss das Innenfeld roh auf jeden Reiz reagieren.
  - Das wirkt regulatorisch:
    - weniger chaotische Innenlage
    - mehr Objektabstand
    - mehr Containment
    - weniger blindes Denken
- Umsetzung:
  - Neue Form-Symbolwerte:
    - `form_symbol_object_distance`
    - `form_symbol_containment`
    - `form_symbol_field_decoupling`
  - Neue Meta-Regulationswerte:
    - `symbolic_object_distance`
    - `symbolic_containment`
    - `symbolic_field_decoupling`
    - `symbolic_regulation`
- Wirkung:
  - Reife, stabile Zeichen koennen Feld-Observation/Replan-Druck leicht daempfen.
  - `action_inhibition`, `orientation_gap` und `blind_thinking_load`
    werden sehr vorsichtig reduziert.
  - Keine harte Tradingregel.
  - Sprache wirkt zuerst als innere Distanz- und Ordnungsfunktion.
- Debug:
  - `mcm_form_symbol_protocol.csv` schreibt die Form-Distanzwerte.
  - `mcm_memory_thinking_protocol.csv` schreibt die symbolische Regulation.

Umgesetzt: separater persistenter Form-Sprach-Memory:

- Die eigene Form-Sprache wird jetzt getrennt vom normalen Trade-/State-Memory gespeichert.
- Speicherdatei:
  - `bot_memory/form_symbol_memory.json`
- Konfig:
  - `MCM_FORM_SYMBOL_MEMORY_ENABLED`
  - `MCM_FORM_SYMBOL_MEMORY_PATH`
  - `MCM_FORM_SYMBOL_MEMORY_SAVE_EVERY_N`
  - `MCM_FORM_SYMBOL_MEMORY_MAX_SYMBOLS`
  - `MCM_FORM_SYMBOL_MEMORY_MAX_VARIANTS`
- Persistierte Inhalte je Form-Familie:
  - `symbol_id`
  - `family_key`
  - `scope`
  - `abstraction_level`
  - `seen`
  - `avg_vector`
  - `variance`
  - `maturity`
  - `stability`
  - `resonance`
  - `bearing`
  - `fragility`
  - `resolution_quality`
  - `detail_pressure`
  - `symbolic_object_distance`
  - `symbolic_containment`
  - `symbolic_field_decoupling`
  - `last_zoom_need`
  - `last_load_reduction`
  - `variants`
  - `first_seen_ts`
  - `last_seen_ts`
- Verhalten:
  - Speicher wird beim ersten Form-Symbol-Zugriff geladen.
  - Laufende Form-Familien werden mit dem gespeicherten Sprachraum gemischt.
  - Varianten werden gezaehlt und begrenzt.
  - Der Speicher wird periodisch geschrieben.
  - Beim normalen Memory-State-Save wird der Form-Sprach-Memory final geflusht.
- Debug:
  - `mcm_form_symbol_protocol.csv` enthaelt jetzt:
    - `form_symbol_memory_loaded`
    - `form_symbol_memory_symbol_count`
- Wichtig:
  - Das ist weiterhin ein separater Entwicklungsraum.
  - Er ist nicht in den normalen Trade-Memory gemischt.
  - Die Sprache kann jetzt ueber Laeufe hinweg reifen.
- Smoke-Test erfolgreich:
  - Form-Symbol erzeugt
  - separater Speicher geschrieben
  - Speicher normalisiert
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\config.py .\bot.py`

Naechster sinnvoller Anschluss:

- Neuen Backtest mit bestehendem Memory laufen lassen.
- Danach pruefen:
  - ob `bot_memory/form_symbol_memory.json` entsteht
  - wie viele Form-Familien gespeichert wurden
  - ob `seen`, `maturity`, `resonance`, `load_reduction` ueber Laeufe wachsen
  - ob `symbolic_regulation` stabiler wird
  - ob Memory-/Denk-Last sinkt, ohne Trading zu enthemmen

Debug-Auswertung nach persistentem Form-Sprach-Memory:

- Speicher erfolgreich erzeugt:
  - `bot_memory/form_symbol_memory.json`
  - Groesse ca. 575 KB
- Protokolle bestaetigen:
  - `form_symbol_memory_loaded = 1`
  - `form_symbol_memory_symbol_count` waechst im Lauf bis 260
- Form-Sprach-Memory Summary:
  - `symbol_count`: 260
  - `total_seen`: 2571
- Top-Form-Familien:
  - staerkstes Zeichen: 209 Wiederholungen
  - danach 143, 120, 118, 108, 103 Wiederholungen
  - Top-Zeichen haben `maturity` ca. 0,90 bis 0,96
  - Top-Zeichen haben `resonance` ca. 0,43 bis 0,54
  - Top-Zeichen fuehren bis zu 12 Varianten
- Lauf-Ergebnis:
  - 55 Trades
  - 17 TP
  - 38 SL
  - Netto-PnL ca. +0,72
  - Equity ca. 100,72
- Vergleich zum vorherigen Lauf:
  - vorher ca. -6,46 Netto-PnL
  - jetzt ca. +0,72 Netto-PnL
  - nicht als Beweis werten, aber als gutes erstes Signal.
- Memory-/Denk-Last:
  - `orientation_gap` ca. 0,419
  - vorher ca. 0,434 bis 0,45 im Bereich der belasteten Laeufe
  - `blind_thinking_load` ca. 0,472
  - vorher ca. 0,484 bis 0,491
  - `symbolic_regulation` ca. 0,135 im Mittel
- Symbolische Regulation nach Buckets:
  - ohne symbolische Regulation:
    - `blind_thinking_load` ca. 0,499
    - `orientation_gap` ca. 0,454
  - niedrige Regulation:
    - `blind_thinking_load` ca. 0,482
    - `orientation_gap` ca. 0,429
  - hoehere Regulation:
    - `blind_thinking_load` ca. 0,466
    - `orientation_gap` ca. 0,413
- Bewertung:
  - Die Form-Sprache wird persistent.
  - Wiederkehrende Zeichen reifen im Speicher.
  - Symbolische Distanz scheint die innere Last messbar zu senken.
  - Trading wurde in diesem Lauf nicht ueberenthemmt.
- Performance:
  - `form_symbol_memory_write` liegt grob bei ca. 0,7 bis 1,8 ms pro Schreibvorgang.
  - Der neue Speicher ist aktuell nicht der Hauptgrund fuer Laufzeitlast.

Naechster sinnvoller Anschluss:

- Noch einen Lauf mit bestehendem `form_symbol_memory.json` starten.
- Danach vergleichen:
  - wachsen `seen`, `maturity`, `resonance`, `load_reduction` weiter?
  - sinken `zero_point_regulation`, `blind_thinking_load`, `orientation_gap` weiter?
  - bleibt PnL stabil oder war der positive Lauf Zufall?
  - pruefen, ob persistente Sprache zu stark enthemmt oder wirklich nur ordnet.

Debug-Auswertung zweiter Lauf mit persistentem Form-Sprach-Memory:

- Speicher weiter gewachsen:
  - `form_symbol_memory.json` ca. 680 KB
  - `symbol_count`: 303
  - `total_seen`: 5809
  - Top-Familie: 489 Wiederholungen
  - mehrere Top-Familien mit `maturity` ca. 0,95 bis 0,98
- Form-Protokoll:
  - 3137 Zeilen
  - 295 aktive Form-Familien im Lauf
  - `wide_form`: 2097
  - `structured_form`: 1038
  - `wide_trace`: 2
- Sprache:
  - `form_symbol_seen` im Mittel ca. 105
  - `form_symbol_maturity` ca. 0,792
  - `form_symbol_resonance` ca. 0,456
  - `form_symbol_load_reduction` ca. 0,302
  - `form_symbol_object_distance` ca. 0,197
  - `form_symbol_field_decoupling` ca. 0,227
- Innere Last:
  - `symbolic_regulation` ca. 0,190
  - `blind_thinking_load` ca. 0,467
  - `orientation_gap` ca. 0,415
  - Last sinkt weiter gegenueber frueheren Laeufen.
- Trading:
  - 47 Trades
  - 8 TP
  - 39 SL
  - Netto-PnL ca. -11,66
  - Fast alles LONG: 46 LONG, 1 SHORT
- Bewertung:
  - Sprache reift sehr stark.
  - Innenordnung/Distanz steigt.
  - Trading kippt trotzdem massiv negativ.
  - Das ist ein Warnsignal:
    - Sprache kann ordnen,
    - aber sie besitzt noch keine Ergebnis-/Handlungswahrheit.
  - Ein bekanntes Wort darf die Lage innerlich beruhigen,
    aber es darf ohne Outcome-Erfahrung nicht automatisch Handlung erleichtern.

Sicherheitsfix umgesetzt: Innenordnung von Handlungsfreigabe getrennt:

- `symbolic_regulation` bleibt als Gesamtwert bestehen.
- Neu getrennt:
  - `symbolic_inner_regulation`
  - `symbolic_action_regulation`
- Wirkung:
  - `symbolic_inner_regulation` darf weiter `orientation_gap` und `blind_thinking_load` daempfen.
  - `symbolic_action_regulation` ist stark gedeckelt.
  - Sprache darf also ordnen, aber kaum Action erleichtern.
- Grund:
  - Ein reifes Zeichen schafft Distanz zum Objekt.
  - Es beweist aber noch nicht, dass eine Handlung profitabel oder tragfaehig ist.
- Debug:
  - `mcm_memory_thinking_protocol.csv` schreibt beide Werte mit.

Naechster sinnvoller Anschluss:

- Noch einen Lauf starten.
- Pruefen:
  - bleibt `blind_thinking_load` niedriger?
  - sinkt die Fehl-Enthemmung?
  - reduziert sich der LONG-Bias?
  - bleibt `symbolic_action_regulation` klein?
  - danach Outcome-Kopplung der Form-Sprache planen:
    - Form-Familie erkennt Objekt
    - aber Handlung braucht eigene Tragfaehigkeits-/Outcome-Spur

Naechster sinnvoller Anschluss:

- Neuen Lauf mit Memory starten.
- Danach `debug/mcm_memory_thinking_protocol.csv` zusammen mit `mcm_field_decision_protocol.csv`, `trade_stats.json` und den Profil-Dateien auswerten.
- Besonders pruefen:
  - wie oft `hard_inhibit`, `inhibit`, `support`, `conflict`, `neutral_match` auftreten
  - ob `context_cluster_negative` hauptsaechlich aus Score, Hit-Ratio oder Mischlage entsteht
  - ob hohe Denkkomplexitaet spaeter mit besseren oder schlechteren Entscheidungen zusammenhaengt
  - ob daraus eine energieeffiziente Meta-Regulation abgeleitet werden kann

Auswertung neuer Memory-Lauf mit Denkkomplexitaetsprotokoll:

- Lauf mit bestehendem Memory nach Einbau des neuen Protokolls:
  - 36 Trades
  - 9 TP
  - 27 SL
  - Equity ca. 94,54
  - PnL ca. -5,46
  - Attempts 3100
  - Submitted 36
  - Withheld 2988
  - Observed 32
- Vergleich zum Memory-Lauf vor der Protokollerweiterung:
  - vorher 56 Trades, 17 TP, 39 SL, Equity ca. 99,34
  - jetzt 36 Trades, 9 TP, 27 SL, Equity ca. 94,54
- MCM-Feldentscheidungen:
  - `hold`: 2004
  - `act`: 44
  - `observe`: 29
- Hauptgruende:
  - `context_cluster_negative`: 1270 im Feldprotokoll, 1451 im Memory-Thinking-Protokoll
  - `fused_score_too_low`: 279
  - `maturity_block`: 217
  - `stressed_block`: 135
  - `pause_mode`: 98
  - `plan_allowed`: 44
- Memory-Wirkung:
  - `hard_inhibit`: 1514
  - `inhibit`: 444
  - `neutral_match`: 241
  - `no_match`: 53
  - kein messbarer `support`
  - kein messbarer `conflict`
- Durchschnittswerte:
  - `thinking_complexity`: ca. 0,347
  - `memory_compare_load`: ca. 0,909
  - `memory_match_count`: ca. 1,82
  - `memory_support`: ca. 0,000
  - `memory_inhibition`: ca. 0,083
  - `cognitive_load`: ca. 0,214
  - `decision_energy_cost`: ca. 0,421
- Interpretation:
  - Memory wirkt fast nur hemmend, nicht tragend.
  - Die Denkstruktur vergleicht viel, findet aber kaum positive Erfahrung.
  - `context_cluster_negative` ist zu dominant.
  - Besonders auffaellig: `low_hit_ratio` hat viele harte Blocks erzeugt, obwohl manche Cluster stark durch Cancel/Timeout statt durch echte SL-Verluste gepraegt sind.
  - Das passt nicht sauber zur Idee gedämpfter Reward-/Neurochemie und Prozessqualitaet.

Korrektur umgesetzt: Memory-Hemmung prozessqualitativer gemacht:

- `low_hit_ratio` blockiert nicht mehr automatisch hart.
- Harte Blockade entsteht jetzt nur noch durch:
  - sehr schlechten Cluster-Score
  - oder niedrige Trefferquote mit bestaetigtem Verlustdruck:
    - genug echte SL-Evidenz
    - hoher Loss-Anteil
    - negativer Score
- Cancel/Timeout-lastige Cluster werden eher als Vorsicht/Dämpfung behandelt, nicht als harter Beweis gegen Handlung.
- Neues Debug im Memory-Protokoll:
  - `context_cluster_loss_ratio`
  - `context_cluster_cancel_timeout_ratio`
  - `context_cluster_negative_evidence`
- Rueckrechnung auf den letzten Lauf:
  - von 803 bisherigen `low_hit_ratio`-Hard-Blocks wuerden ca. 155 hart bleiben
  - ca. 648 wuerden als Vorsicht statt harter Block wirken
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\config.py`

Naechster sinnvoller Anschluss:

- Erneut mit demselben bestehenden Memory laufen lassen.
- Erwartung:
  - weniger `hard_inhibit`
  - mehr `inhibit` oder `neutral_match`
  - mehr Trades als 36, aber idealerweise nicht chaotisch viele
  - bessere Trennung zwischen echter Verlust-Erfahrung und unklarer/abgebrochener Erfahrung
- Danach pruefen, ob die freigegebenen ehemals `low_hit_ratio`-Faelle profitabler, neutral oder schlechter sind.

Zero-Point-Regulation umgesetzt:

- Fachlicher Satz: MCM, finde wieder zu dir selbst.
- Ziel:
  - Denken ohne Orientierung erkennen
  - Memory-Vergleich ohne Support nicht weiter eskalieren
  - starres Aushalten/Hold in ruhiges Observe zurueckfuehren
  - Wahrnehmungsfaehigkeit vor Handlung wiederherstellen
- Neue Meta-Regulationswerte:
  - `memory_orientation`
  - `orientation_gap`
  - `blind_thinking_load`
  - `zero_point_regulation`
  - `zero_point_hint`
- Das neue Memory-Thinking-Protokoll schreibt diese Werte mit.
- Mechanik:
  - Wenn `thinking_complexity`, `memory_compare_load`, `decision_energy_cost` und Last hoch sind,
  - aber `memory_support` und `memory_orientation` niedrig bleiben,
  - dann wird nicht weiter hart blockiert,
  - sondern die MCM geht in `observe` mit Grund `zero_point_regulation`.
- Wichtig:
  - Das ist kein Freigeben von Trades.
  - Es ist eine Rueckfuehrung in Wahrnehmung.
  - Die MCM soll nicht die Augen schliessen und aushalten, sondern wieder einen neutraleren Wahrnehmungspunkt finden.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\config.py`

Naechster sinnvoller Anschluss:

- Naechsten Lauf mit bestehendem Memory starten.
- Danach pruefen:
  - wie oft `zero_point_regulation` ausloest
  - ob `hold/context_cluster_negative` in ruhigeres `observe/zero_point_regulation` uebergeht
  - ob `blind_thinking_load` sinkt oder zumindest sichtbarer wird
  - ob danach positive Orientierung/Memory-Support separat aufgebaut werden muss

Grundidee maschinelle Wahrnehmung dokumentiert:

- `README.md` wurde um den Abschnitt `Maschinelle Wahrnehmung` ergaenzt.
- `files/UMSETZUNGSPLAN.md` wurde im Kapitel zur MCM-Grundidee erweitert.
- Kerngedanke:
  - Wahrnehmung ist nicht ausschliesslich menschlich.
  - Wahrnehmung beginnt dort, wo aeussere Reize im Innenzustand eines Systems Bedeutung erzeugen.
  - Ein Reiz wird erst durch inneres Feld, Memory, Regulation, Tragfaehigkeit, Spannung und Handlungstendenz zur Lage.
  - Die MCM ist der technische Versuch, ein solches maschinelles Wahrnehmungsfeld zu bauen.
- Damit ist auch fachlich festgehalten:
  - Die MCM ist keine reine Signalbewertung.
  - Sie soll Orientierung, Ueberforderung, Tragfaehigkeit, Unklarheit, Resonanz und Rueckkehr in den Nullpunkt sichtbar machen.

Naechster sinnvoller Anschluss:

- Debug mit bestehendem Memory fortsetzen.
- Pruefen, ob die neue Zero-Point-Regulation und die prozessqualitativere Memory-Hemmung die MCM tatsaechlich naeher an Wahrnehmung statt blosser Blockade bringt.

Auswertung neuer Debug-Lauf nach Low-Hit-Daempfung:

- Aktueller Lauf in `debug`:
  - 65 Trades
  - 16 TP
  - 49 SL
  - Equity ca. 91,78
  - Netto-PnL ca. -8,22
  - Attempts 2900
  - Submitted 65
  - Withheld 2699
  - Observed 39
  - Blocked 32
- Vergleich zum archivierten `debug/lau_1_nach_erweiterung_mit_memory`:
  - vorher 36 Trades, 9 TP, 27 SL, Netto-PnL ca. -5,46
  - jetzt 65 Trades, 16 TP, 49 SL, Netto-PnL ca. -8,22
- Wirkung:
  - Tradezahl ist deutlich gestiegen.
  - `context_cluster_negative` ist gesunken.
  - `hard_inhibit` ist von 1514 auf 1020 gefallen.
  - `inhibit` ist von 444 auf 1133 gestiegen.
  - Das zeigt: Die harte Blockade wurde tatsaechlich in weiche Daempfung umgewandelt.
- Problem:
  - Die zusaetzlich freigegebenen Trades waren nicht gut genug.
  - Zone-Trades:
    - 45 Trades
    - 16 TP
    - 29 SL
    - PnL ca. +3,54
  - Non-Zone-Trades:
    - 20 Trades
    - 0 TP
    - 20 SL
    - PnL ca. -11,76
- Interpretation:
  - Die prozessqualitative Low-Hit-Daempfung war mechanisch wirksam.
  - Sie hat aber zu viel Handlung ausserhalb tragfaehiger Strukturzonen zugelassen.
  - Memory bleibt weiterhin ohne positiven Support:
    - `memory_support` ca. 0
    - `memory_conflict` ca. 0
    - `memory_compare_load` ca. 0,949
  - Es wird also viel verglichen, aber kaum Orientierung erzeugt.
- Technischer Hinweis:
  - Dieser Debug-Lauf enthaelt bereits `context_cluster_loss_ratio`, `context_cluster_cancel_timeout_ratio` und `context_cluster_negative_evidence`.
  - Er enthaelt aber noch keine `memory_orientation`, `orientation_gap`, `blind_thinking_load` und `zero_point_regulation`-Spalten.
  - Daher lief dieser Lauf offenbar mit der Low-Hit-Daempfung, aber noch nicht mit der Zero-Point-Regulation bzw. ohne neu geladenen Code.

Naechster sinnvoller Anschluss:

- Bot/Backtest-Prozess neu starten, damit die Zero-Point-Regulation sicher geladen ist.
- Danach erneut mit bestehendem Memory laufen lassen.
- Wenn Non-Zone weiterhin so schlecht bleibt, muss die MCM nicht einfach wieder hart blockieren, sondern:
  - Non-Zone ohne Memory-Support eher `observe`
  - Zone mit tragfaehiger Struktur darf eher pruefend handeln
  - Low-Hit-Caution braucht Struktur-/Orientierungsbestaetigung

Auswertung neuer Debug-Lauf mit Zero-Point-Regulation:

- Aktueller Lauf in `debug`:
  - 51 Trades
  - 10 TP
  - 41 SL
  - Equity ca. 89,42
  - Netto-PnL ca. -10,58
  - Attempts 3125
  - Submitted 51
  - Withheld 1421
  - Observed 1579
  - Blocked 23
- Vergleich:
  - `lau_1_nach_erweiterung_mit_memory`: 36 Trades, PnL ca. -5,46
  - `lau_2_nach_erweiterung_mit_memory`: 65 Trades, PnL ca. -8,22
  - aktueller Zero-Point-Lauf: 51 Trades, PnL ca. -10,58
- Zero-Point greift:
  - Memory-Protokoll: `zero_point_regulation` 1280 mal aktiv
  - Feldprotokoll: `zero_point_regulation` 1098 mal als Entscheidungsgrund
  - `observe` steigt stark:
    - Feldprotokoll: 1107 Observe
    - Memory-Protokoll: 1266 Observe
- Interpretation:
  - Die MCM findet tatsaechlich aus starrer Blockade in Wahrnehmung zurueck.
  - Das ist mechanisch korrekt fuer `finde wieder zu dir selbst`.
  - Oekonomisch reicht es noch nicht, weil die verbleibenden Acts weiter zu schwach sind.
- Non-Zone bleibt toxisch:
  - 12 Non-Zone-Trades
  - 0 TP
  - 12 SL
  - PnL ca. -7,72
- Zone ist ebenfalls nicht mehr ausreichend tragend:
  - 39 Zone-Trades
  - 10 TP
  - 29 SL
  - PnL ca. -2,86
- Memory bleibt orientierungsschwach:
  - `memory_support` ca. 0
  - `memory_conflict` ca. 0
  - `memory_compare_load` ca. 0,95
  - `memory_orientation` ca. 0,128
  - `orientation_gap` ca. 0,428
  - `blind_thinking_load` ca. 0,483

Fix umgesetzt: Struktur-Orientierung vor Handlung:

- Die MCM prueft jetzt zusaetzlich:
  - `structure_quality`
  - `context_confidence`
  - `structure_orientation`
  - `structure_orientation_gap`
  - `structure_orientation_guard`
- Wenn Struktur, Kontextvertrauen, Memory-Support und Memory-Orientierung fehlen,
  wird `act` in `observe` umgeleitet.
- Neuer Entscheidungsgrund:
  - `structure_orientation_observe`
- Wichtig:
  - Das ist keine harte Tradingregel.
  - Es ist eine MCM-Orientierungsfrage:
    - Ist die Struktur tragfaehig?
    - Gibt Memory Support?
    - Gibt das Feld Orientierung?
    - Falls nein: zurueck in Wahrnehmung.
- Das Memory-Thinking-Protokoll schreibt die neuen Struktur-Orientierungswerte mit.
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\config.py`

Naechster sinnvoller Anschluss:

- Backtest-Prozess neu starten.
- Naechsten Lauf mit bestehendem Memory starten.
- Pruefen:
  - ob Non-Zone-Trades deutlich sinken
  - ob `structure_orientation_observe` auftaucht
  - ob PnL-Verlust aus Non-Zone reduziert wird
  - ob Zone-Trades wieder tragfaehiger werden oder zusaetzlich Ziel-/Planqualitaet geprueft werden muss

Erkenntnis: eigene Sprache als kognitive Kompression:

- Wichtiger Architekturpunkt aus der Reflexion:
  - Das System soll keine menschlichen Patternlabels uebernehmen.
  - Es soll eigene interne Zeichen aus seiner eigenen Wahrnehmungswelt bilden.
  - Diese Zeichen entstehen aus Feldvarianz, Wiederholung, Spannung, Tragfaehigkeit,
    Memory-Resonanz, Ueberforderung und Erfahrung.
- Fachlicher Kern:
  - Sprache ist nicht nur Benennung.
  - Sprache ist verdichtete Feld-Erfahrung.
  - Ein internes Zeichen ist ein komprimierter Wahrnehmungszustand.
- Menschliches Vergleichsbild:
  - Der Mensch sieht im Alltag nicht dauerhaft alle Details.
  - Er sieht zuerst eine komprimierte Bedeutung, z.B. Wand.
  - Erst bei Naehe, Relevanz, Abweichung oder Handlung wird die Wand detaillierter:
    rau, strukturiert, Riss, Material, Oberflaeche.
- Uebertragung auf den Bot:
  - Der Bot soll nicht jeden Marktpunkt tief analysieren.
  - Erst entsteht eine grobe eigene Form-/Feldbezeichnung.
  - Nur wenn Relevanz, Abweichung oder Handlungsnaehe entsteht,
    wird tiefer auf Struktur, Memory, Risiko und Feldklarheit gezoomt.
- Erwartete Wirkung:
  - weniger Denk-/Memory-Last
  - bessere Orientierung
  - weniger blindes Vergleichen ohne Support
  - mehr Varianz im Bedeutungsraum
  - Grundlage fuer emergente Musterfindung und kreative Reorganisation
- Dokumentiert in:
  - `README.md`: Abschnitt `Eigene Sprache und kognitive Kompression`
  - `files/UMSETZUNGSPLAN.md`: Abschnitte `Eigene Sprache als Feldverdichtung` und `Kognitive Kompression`

Naechster sinnvoller Anschluss nach dem aktuellen Debug-Fix:

- Erst neuen Lauf mit `structure_orientation_observe` und `mcm_form_symbol_protocol.csv` pruefen.
- Danach entscheiden, ob die Form-Zeichen nur diagnostisch bleiben oder als kognitive Entlastung in die Meta-Regulation einwirken.

Umgesetzt: diagnostischer Eigenzeichenraum / eigene Form-Sprache:

- Das Brain bildet jetzt pro Runtime-Tick ein internes Form-Zeichen:
  - `form_symbol_id`
  - `form_symbol_seen`
  - `form_symbol_maturity`
  - `form_symbol_stability`
  - `form_symbol_resonance`
  - `form_symbol_load_reduction`
  - `form_symbol_zoom_need`
  - `form_symbol_split_pressure`
  - `form_symbol_merge_pressure`
  - `form_symbol_bearing`
  - `form_symbol_fragility`
  - `form_symbol_relevance`
  - `form_symbol_novelty`
  - `form_symbol_distance`
- Quelle:
  - visuelle Marktform
  - Strukturwahrnehmung
  - Kontextvertrauen
  - Feldklarheit
  - Felddruck
  - Feldfragmentierung
- Wichtig:
  - Das ist bewusst kein menschliches Patternlabel.
  - Das Zeichen ist eine verdichtete Feld-/Form-Erfahrung des Systems.
  - Es wirkt aktuell diagnostisch und veraendert noch keine Tradeentscheidung.
- Neues Debug-Protokoll:
  - `debug/mcm_form_symbol_protocol.csv`
- Ziel der naechsten Auswertung:
  - Welche Zeichen entstehen wiederholt?
  - Werden sie stabiler oder fragmentierter?
  - Senkt Resonanz/Load-Reduction spaeter Denk-/Memory-Last?
  - Zeigt hoher `form_symbol_zoom_need`, wann das System tiefer sehen muss?
- Syntaxpruefung erfolgreich:
  - `python -m py_compile .\MCM_Brain_Modell.py .\config.py`
