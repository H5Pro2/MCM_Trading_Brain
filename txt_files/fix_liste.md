# --------------------------------------------------
# Beobachtung
# --------------------------------------------------

* `fix_liste.md` enthält aktuell noch bereits erledigte Punkte und ist damit nicht mehr auf echte Restarbeit reduziert.

* Die nächste offene Hauptarbeit ist nicht Test-first und nicht `MCM`-Druck-/Regulationsausbau-first.

* Vor weiterem Ausbau von:

  * `field_density`
  * `field_stability`
  * `regulatory_load`
  * `action_capacity`
  * `recovery_need`
  * `survival_pressure`

  soll zuerst die Wahrnehmungsbasis umgesetzt werden.

# --------------------------------------------------
# Interpretation
# --------------------------------------------------

* Prio 1 ist die äußere Wahrnehmung als neue Basis für die weitere Architektur.

* Diese Wahrnehmung soll nicht als Bilddaten-/CNN-System kommen, sondern als neutrales numerisches räumliches Wahrnehmungsfeld aus RAW-OHLCV.

* Mehrskalen-Wahrnehmung darf vorbereitet werden, aber keine harte Fraktal-Regel und keine fest codierte Fraktal-Erkennung.

* `HH/LL` und bestätigte Swing-Struktur bleiben nur sekundäre bestätigende Strukturwahrnehmung und nicht mehr Hauptbasis.

* Erst wenn diese Wahrnehmung stabil in Thread 1 und Thread 2 angeschlossen ist, wird auf dieser Basis der weitere MCM-Zustandsraum und Druck-/Regulationsausbau fortgesetzt.

* Tests bleiben niedrigste Priorität.

# --------------------------------------------------
# Schlussfolgerung
# --------------------------------------------------

* **Offene Fix-/Umbau-Liste**

  * **Prio 1 · Wahrnehmungsbasis zuerst**

    * neutrales `visual_market_state` einführen
    * Form fest halten als numerisches räumliches Wahrnehmungsfeld
    * Quelle bleibt nur RAW-OHLCV / Fensterdaten
    * keine Bilddateien
    * keine CNN-/Pixel-Verarbeitung
    * keine harte Fraktal-Logik
    * `HH/LL` nur noch sekundär verwenden

  * **Prio 2 · Thread-1-Anbindung der Wahrnehmung**

    * Thread 1 baut zusätzlich zu:

      * `candle_state`
      * `tension_state`
      * `structure_perception_state`

      auch:

      * `visual_market_state`

    * Ausgabe bleibt neutral
    * keine Entscheidung
    * kein Memory
    * keine Orders

  * **Prio 3 · Thread-2-Verarbeitung auf neue Wahrnehmung umstellen**

    * `outer_visual_perception_state` auf `visual_market_state` aufbauen
    * weitere Wahrnehmungs-/Verarbeitungsbahn daran angleichen:

      * `perception_state`
      * `processing_state`
      * `felt_state`
      * `thought_state`
      * `meta_regulation_state`
      * `expectation_state`

    * bestehende symbolische Strukturwahrnehmung nicht löschen, aber unterordnen

  * **Prio 4 · Danach erst weiterer MCM-Zustandsraum-Ausbau**

    * `field_density`
    * `field_stability`
    * `regulatory_load`
    * `action_capacity`
    * `recovery_need`
    * `survival_pressure`

    erst weiter vertiefen, wenn Wahrnehmungsbasis produktiv angeschlossen ist

  * **Prio 5 · Danach Architektur-Endausbau**

    * permanenter Innenprozess weiter vervollständigen
    * harte Runtime-Bahntrennung weiter zu Ende führen
    * Entscheidungsepisode weiter ausbauen
    * Erfahrungsraum / Review / Nicht-Handlung weiter vertiefen

  * **Kleinste Prio · Tests**

    * dedizierte Tests für `bot_gate_funktions.py`
    * dedizierte Tests für `mcm_core_engine.py`