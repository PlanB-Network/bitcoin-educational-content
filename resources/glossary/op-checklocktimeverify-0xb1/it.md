---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)

---
Rende la transazione non valida se non sono soddisfatte tutte le condizioni:


- La pila non è vuota;
- Il valore in cima alla pila è maggiore o uguale a `0`;
- Il tipo di timelock è lo stesso tra il campo `nLockTime` e il valore in cima alla pila (tempo reale o numero di blocco);
- Il campo `nSequenza` dell'input non è uguale a `0xffffff`;
- Il valore in cima alla pila è maggiore o uguale al valore del campo `nLockTime` della transazione.

Se una di queste condizioni non è soddisfatta, lo script contenente l'opzione `OP_CHECKLOCKTIMEVERIFY` non può essere soddisfatto. Se tutte queste condizioni sono valide, `OP_CHECKLOCKTIMEVERIFY` agisce come un `OP_NOP`, cioè non esegue alcuna azione sullo script. È come se sparisse. `OP_CHECKLOCKTIMEVERIFY` impone quindi un vincolo temporale sulla spesa dell'UTXO assicurato con lo script che lo contiene. Può farlo sotto forma di data temporale Unix o di numero di blocco. Per fare ciò, limita i possibili valori del campo `nLockTime` della transazione che lo spende, e questo campo `nLockTime` limita a sua volta il momento in cui la transazione può essere inclusa in un blocco.

> ► *Questo opcode sostituisce `OP_NOP`. È stato collocato su `OP_NOP2`. Viene spesso indicato con l'acronimo "CLTV". Si noti che `OP_CLTV` non deve essere confuso con il campo `nLockTime` di una transazione. Il primo utilizza il secondo, ma la loro natura e le loro azioni sono diverse.*