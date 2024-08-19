---
term: BIP113
---

Führte eine Änderung in der Berechnung aller Timelock-Operationen (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` und `OP_CHECKSEQUENCEVERIFY`) ein. Es legt fest, dass zur Bewertung der Gültigkeit von Timelocks diese nun mit dem MTP (*Median Time Past*, dt. Vergangene Mittelzeit), welcher der Median der Zeitstempel der letzten 11 Blöcke ist, verglichen werden müssen. Zuvor wurde nur der Zeitstempel des vorherigen Blocks verwendet. Diese Methode macht das System vorhersehbarer und verhindert die Manipulation des Zeitbezugs durch Miner. BIP113 wurde am 4. Juli 2016 über einen Soft Fork eingeführt, zusammen mit BIP68 und BIP112, die zum ersten Mal mit der BIP9-Methode aktiviert wurden.