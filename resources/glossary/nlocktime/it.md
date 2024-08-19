---
termine: NLOCKTIME
---

Un campo incorporato nelle transazioni che stabilisce una condizione basata sul tempo prima della quale la transazione non può essere aggiunta a un blocco valido. Questo parametro consente di specificare un tempo esatto (timestamp Unix) o un numero specifico di blocchi come condizione affinché la transazione sia considerata valida. Pertanto, è un blocco temporale assoluto (non relativo). Il `nLockTime` influisce sull'intera transazione e consente effettivamente la verifica temporale, mentre l'opcode `OP_CHECKLOCKTIMEVERIFY` permette solo di confrontare il valore in cima allo stack con il valore di `nLockTime`.