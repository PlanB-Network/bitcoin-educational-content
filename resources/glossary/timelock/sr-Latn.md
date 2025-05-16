---
term: TIMELOCK
---

Primitiva Smart contract koja omogućava postavljanje vremenski zasnovanog uslova koji mora biti ispunjen da bi transakcija bila dodata u blok. Postoje dve vrste vremenskih zaključavanja na Bitcoin:


- Apsolutni vremenski zaključavanje, koji određuje tačan trenutak pre kojeg transakcija ne može biti uključena u blok;
- Relativni vremenski zaključavanje, koji postavlja kašnjenje od prihvatanja prethodne transakcije.

Timelock se može definisati ili kao datum izražen u Unix vremenu ili kao broj bloka. Na kraju, timelock se može primeniti na izlaz transakcije korišćenjem specifičnog opkoda u skripti zaključavanja (`OP_CHECKLOCKTIMEVERIFY` ili `OP_CHECKSEQUENCEVERIFY`), ili na celu transakciju korišćenjem specifičnih polja transakcije (`nLockTime` ili `nSequence`).