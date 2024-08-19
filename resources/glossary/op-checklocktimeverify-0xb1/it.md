---
termine: OP_CHECKLOCKTIMEVERIFY (0XB1)
---

Rende la transazione non valida a meno che tutte queste condizioni siano soddisfatte:
* Lo stack non è vuoto;
* Il valore in cima allo stack è maggiore o uguale a `0`;
* Il tipo di blocco temporale è lo stesso tra il campo `nLockTime` e il valore in cima allo stack (tempo reale o numero di blocco);
* Il campo `nSequence` dell'input non è uguale a `0xffffffff`;
* Il valore in cima allo stack è maggiore o uguale al valore del campo `nLockTime` della transazione.

Se anche solo una di queste condizioni non è soddisfatta, lo script contenente `OP_CHECKLOCKTIMEVERIFY` non può essere soddisfatto. Se tutte queste condizioni sono valide, allora `OP_CHECKLOCKTIMEVERIFY` agisce come un `OP_NOP`, il che significa che non esegue alcuna azione sullo script. È come se scomparisse. `OP_CHECKLOCKTIMEVERIFY` impone quindi un vincolo temporale sulla spesa dell'UTXO assicurato con lo script che lo contiene. Può farlo sia sotto forma di una data di tempo Unix sia come numero di blocco. Per fare ciò, limita i valori possibili per il campo `nLockTime` della transazione che lo spende, e questo campo `nLockTime` a sua volta restringe quando la transazione può essere inclusa in un blocco.

> ► *Questo opcode è un sostituto di `OP_NOP`. È stato posizionato su `OP_NOP2`. È spesso indicato con l'acronimo "CLTV". Da notare, `OP_CLTV` non deve essere confuso con il campo `nLockTime` di una transazione. Il primo utilizza il secondo, ma le loro nature e azioni sono diverse.*