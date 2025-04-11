---
term: NLOCKTIME

---
Campo incorporato nelle transazioni che stabilisce una condizione temporale prima della quale la transazione non può essere aggiunta a un blocco valido. Questo parametro consente di specificare un'ora esatta (timestamp Unix) o un numero specifico di blocchi come condizione perché la transazione sia considerata valida. Si tratta quindi di un blocco temporale assoluto (non relativo). Il parametro `nLockTime` influisce sull'intera transazione e consente effettivamente la verifica del tempo, mentre l'opcode `OP_CHECKLOCKTIMEVERIFY` consente solo di confrontare il valore superiore dello stack con il valore `nLockTime`.