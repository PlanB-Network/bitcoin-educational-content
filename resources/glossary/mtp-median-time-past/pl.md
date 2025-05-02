---
term: MTP (MEDIANA CZASU PRZESZŁEGO)
---

Koncepcja ta jest wykorzystywana w protokole Bitcoin do określenia marginesu konsensusu sieci Timestamp. MTP definiuje się jako medianę znaczników czasu ostatnich 11 wydobytych bloków. Zastosowanie tego wskaźnika pomaga uniknąć nieporozumień między węzłami co do dokładnego czasu w przypadku rozbieżności. MTP był początkowo używany do weryfikacji ważności znaczników czasu bloków w przeszłości. Od BIP113 jest on również używany jako odniesienie do czasu sieciowego w celu weryfikacji ważności transakcji blokad czasowych (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` i `OP_CHECKSEQUENCEVERIFY`).