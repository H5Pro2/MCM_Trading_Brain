# FIX_LISTE

Diese Datei ist ab jetzt nur die aktive Arbeitsliste.

Rolle:
- offene Fixes
- naechste Pruefpunkte
- kurze technische Befunde
- keine langen Laufanalysen
- keine Forschungsprosa

Ausfuehrliche Auswertung steht in `files/AKTUELLER_STAND.md`.
Die alte lange Fixliste wurde nach `files/FIX_LISTE_ARCHIV.md` verschoben.

---

# Aktueller Fokus

- [ ] Nervliche Varianz diagnostisch erfassen.
  Ziel:
  - nicht Varianz hart entfernen
  - erkennen, ob DIO nach Stress reif reorganisiert oder nur kompensiert
  - Phase-B-Stress und Phase-C-Recovery messbar machen
  Geplante Groessen:
  - `nervous_variance`
  - `regulation_oscillation`
  - `recovery_after_stress`
  - `stress_to_recovery_delta`

- [ ] Lauf 9 auf gleichem erweitertem Datensatz pruefen.
  Pruefen:
  - PnL / Profit Factor / Giveback
  - Zone-Freiheit
  - Non-Zone-Schaden
  - `transfer_break_trigger`
  - `transfer_break_ready`
  - `immature_transfer_observe`
  - Exit-Replay TP-Cut-Risiko

---

# Zuletzt erledigt

- [x] Dateien im `files`-Ordner vereinheitlicht.
  Ergebnis:
  - `AKTUELLER_STAND.md`
  - `BILDER/`
  - `FIX_LISTE.md`
  - `FIX_LISTE_ARCHIV.md`
  - `MCM_VARIABLEN_MECHANIK.md`
  - `UMSETZUNGSPLAN.md`
  - `WICHTIG_MECHANIKEN.md`

- [x] Aktive Fixliste von Forschungslog getrennt.
  Ergebnis:
  - `FIX_LISTE.md` bleibt kurz und handlungsorientiert.
  - Details und Laufdeutungen stehen in `AKTUELLER_STAND.md`.

- [x] `transfer_break_fatigue` neu balanciert.
  Ergebnis:
  - weniger permanente Daempfung
  - neue Werte `transfer_break_trigger` und `transfer_break_ready`
  - sichtbare `transfer_break_*` Entscheidungen haengen an mehreren
    gleichzeitigen Reife-/Tragfaehigkeitsbedingungen.

- [x] Lauf 8 geprueft.
  Kurzbefund:
  - profitabel, aber hohe Varianz
  - Phase B Stress-/Ueberlebensphase
  - Phase C starke Reorganisation
  - Zone traegt weiter
  - Non-Zone bleibt Stresskanal

---

# Arbeitsregel

Nach jedem neuen Lauf:
- `AKTUELLER_STAND.md`: ausfuehrliche Analyse und Interpretation.
- `FIX_LISTE.md`: nur kurze Checkbox, Kurzbefund und naechster Pruefpunkt.
