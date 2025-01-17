---
term: TIMELOCK

---
Una primitiva dello smart contract che consente di impostare una condizione temporale che deve essere soddisfatta affinché una transazione venga aggiunta a un blocco. Esistono due tipi di timelock su Bitcoin:


- Il timelock assoluto, che specifica un momento esatto prima del quale la transazione non può essere inclusa in un blocco;
- Il timelock relativo, che stabilisce un ritardo rispetto all'accettazione di una transazione precedente.

Il blocco temporale può essere definito come una data espressa in tempo Unix o come un numero di blocco. Infine, il timelock può essere applicato all'output di una transazione utilizzando un opcode specifico nello script di locking (`OP_CHECKLOCKTIMEVERIFY` o `OP_CHECKSEQUENCEVERIFY`), oppure a un'intera transazione utilizzando campi specifici della transazione (`nLockTime` o `nSequence`).