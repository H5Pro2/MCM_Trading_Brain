from pathlib import Path

content = """# ==================================================
# BEREINIGTE FIX-LISTE – NUR NOCH OFFENE PUNKTE
# ==================================================

Diese Liste enthält nur noch Punkte, die im aktuellen Ist-Stand noch offen sind.
Bereits umgesetzte Basismechanik wurde entfernt.

---

# --------------------------------------------------
# 1. STATUS
# --------------------------------------------------

Das Projekt ist nicht mehr in einer frühen Fix- oder Basisphase.

Offen ist nicht mehr die Grundmechanik,
sondern der weitere Ausbau.

---

# --------------------------------------------------
# 2. OFFENE PUNKTE
# --------------------------------------------------

# --------------------------------------------------
# 2.1 Experience / Review vertiefen
# --------------------------------------------------

Noch offen:

- Tragfähigkeit als explizite Bewertungsgröße sauber durchziehen
- Lernen explizit als Umgangsfähigkeit modellieren
- Reibung / Energie als Experience-Kosten klarer technisch verankern
- Cluster-Bewertung stärker auf Tragfähigkeit statt Ergebnis ausrichten
- Profitlogik weiter von Experience entkoppeln
- Outcome stärker als Zustandswirkung statt Geldwirkung ausformen

---

# --------------------------------------------------
# 2.2 Runtime / Architektur weiter trennen
# --------------------------------------------------

Noch offen:

- Ebene 1 weiter als reine Außenwahrnehmung schärfen
- Ebene 2 weiter als reinen Innenprozess schärfen
- Ebene 3 weiter als reine Entwicklung / Experience schärfen
- Vermischung von Runtime und Bot-State weiter reduzieren
- strukturelle Trennung der Ebenen weiter verhärten

---

# --------------------------------------------------
# 2.3 KPI / Auswertung umbauen
# --------------------------------------------------

Noch offen:

- klassische Trade-KPIs als Hauptbewertung zurückbauen oder umordnen
- Tragfähigkeit, innere Reibung, Belastung, Entlastung und Handlungsfähigkeit stärker als Nachweisgrößen aufbauen
- alte Ergebnislogik in der Bewertung weiter zurückdrängen

Aktuell noch alt geprägt sind insbesondere:

- pnl_netto
- pnl_tp
- pnl_sl
- equity_peak
- max_drawdown_abs
- max_drawdown_pct
- winrate
- profit_factor
- expectancy

---

# --------------------------------------------------
# 2.4 GUI / Visualisierung umbauen
# --------------------------------------------------

Noch offen:

- GUI stärker von alten Trade-Nachweisen lösen
- Außenwelt sauber darstellen
- Innenwelt sauber darstellen
- Zustandsachsen sauber darstellen
- Experience- / Tragfähigkeitsverlauf sichtbar machen
- alte Equity- / PnL-Zentrierung weiter zurückbauen
- umgesetzt daten Puffer - fertig

Aktuell noch alt geprägt:

- trade_stats.json
- trade_equity.csv

---

# --------------------------------------------------
# 2.5 Tests ergänzen
# --------------------------------------------------

Noch offen:

- dedizierte Tests für bot_gate_funktions.py
- dedizierte Tests für mcm_core_engine.py

---

# --------------------------------------------------
# 3. PRIORISIERTE RESTREIHENFOLGE
# --------------------------------------------------

# --------------------------------------------------
# PRIO 1
# --------------------------------------------------

- Experience / Review vertiefen
- Runtime / Architektur weiter trennen

# --------------------------------------------------
# PRIO 2
# --------------------------------------------------

- KPI / Auswertung umbauen
- GUI / Visualisierung umbauen

# --------------------------------------------------
# PRIO 3
# --------------------------------------------------

- dedizierte Tests ergänzen

---

# --------------------------------------------------
# 4. ENTFERNT AUS DER ALTEN FIX-LISTE
# --------------------------------------------------

Nicht mehr als offene Fix-Punkte führen:

- äußere Wahrnehmungsbasis
- MCM-Runtime-Grundmechanik
- Entscheidungstendenz
- technische Handlungsbahn
- Nicht-Handlung als echter Pfad
- Episode / Review / Experience-Basis
- Persistenz der Memory- und Runtime-Zustände
- Grundkopplung von Wahrnehmung → Runtime → Handlung → Experience

---

# --------------------------------------------------
# 5. AKTUELLER KERNSATZ
# --------------------------------------------------

Offen ist nicht mehr die Basislogik.

Offen ist der Architektur-Endausbau.
"""

path = Path("/mnt/data/bereinigte_fix_liste.md")
path.write_text(content, encoding="utf-8")
print(f"Wrote {path}")
