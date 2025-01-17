---
term: BIP113

---
Es wurde eine Änderung bei der Berechnung aller Timelock-Operationen (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` und `OP_CHECKSEQUENCEVERIFY`) eingeführt. Sie legt fest, dass zur Bewertung der Gültigkeit von Zeitsperren diese nun mit dem MTP (*Median Time Past*) verglichen werden müssen, der dem Median der Zeitstempel der letzten 11 Blöcke entspricht. Zuvor wurde nur der Zeitstempel des vorhergehenden Blocks verwendet. Diese Methode macht das System berechenbarer und verhindert die Manipulation der Zeitreferenz durch Miner. BIP113 wurde über eine Soft Fork am 4. Juli 2016 eingeführt, zusammen mit BIP68 und BIP112, die zum ersten Mal mit der BIP9-Methode aktiviert wurden.