---
term: TIMELOCK
---

Una primitiva di smart contract che permette di impostare una condizione basata sul tempo che deve essere soddisfatta affinché una transazione possa essere aggiunta a un blocco. Esistono due tipi di timelock su Bitcoin:
* Il timelock assoluto, che specifica un momento esatto prima del quale la transazione non può essere inclusa in un blocco;
* Il timelock relativo, che stabilisce un ritardo dall'accettazione di una transazione precedente.
Il timelock può essere definito sia come una data espressa in tempo Unix sia come un numero di blocco. Infine, il timelock può applicarsi a un output di transazione utilizzando un opcode specifico nello script di blocco (`OP_CHECKLOCKTIMEVERIFY` o `OP_CHECKSEQUENCEVERIFY`), o a un'intera transazione utilizzando campi di transazione specifici (`nLockTime` o `nSequence`).