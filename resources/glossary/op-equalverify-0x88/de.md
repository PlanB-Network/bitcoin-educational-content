---
term: OP_EQUALVERIFY (0X88)

definition: Kombiniert OP_EQUAL und OP_VERIFY und macht die Transaktion ungültig, wenn die Werte voneinander abweichen.
---
Kombiniert die Funktionen von `OP_EQUAL` und `OP_VERIFY`. Es prüft zuerst die Gleichheit der beiden obersten Werte auf dem Stack und verlangt dann, dass das Ergebnis ungleich Null ist, ansonsten ist die Transaktion ungültig. `OP_EQUALVERIFY` wird vor allem in Skripten zur Adressüberprüfung verwendet.