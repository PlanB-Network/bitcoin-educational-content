---
term: OP_EQUALVERIFY (0X88)
---

Kombiniert die Funktionen von `OP_EQUAL` und `OP_VERIFY`. Zuerst wird die Gleichheit der obersten zwei Werte auf dem Stapel überprüft, dann wird gefordert, dass das Ergebnis nicht Null ist, andernfalls ist die Transaktion ungültig. `OP_EQUALVERIFY` wird insbesondere in Skripten zur Adressüberprüfung verwendet.