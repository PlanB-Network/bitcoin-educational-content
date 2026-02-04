---
term: OP_NUMEQUALVERIFY (0X9D)
definition: Kombinerar OP_NUMEQUAL och OP_VERIFY, och misslyckas om de numeriska värdena skiljer sig åt.
---

Kombinerar operationerna `OP_NUMEQUAL` och `OP_VERIFY`. Den jämför numeriskt de två översta Elements på stacken. Om värdena är lika tar `OP_NUMEQUALVERIFY` bort det sanna resultatet från stacken och fortsätter exekveringen av skriptet. Om värdena inte är lika är resultatet falskt och skriptet misslyckas omedelbart.