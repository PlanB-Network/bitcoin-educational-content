---
term: OP_NUMEQUALVERIFY (0X9D)
---

Kombiniert die Operationen `OP_NUMEQUAL` und `OP_VERIFY`. Es vergleicht numerisch die zwei obersten Elemente auf dem Stapel. Wenn die Werte gleich sind, entfernt `OP_NUMEQUALVERIFY` das wahre Ergebnis vom Stapel und setzt die Ausführung des Skripts fort. Wenn die Werte nicht gleich sind, ist das Ergebnis falsch, und das Skript schlägt sofort fehl.