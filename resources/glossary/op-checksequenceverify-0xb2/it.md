---
term: OP_CHECKSEQUENCEVERIFY (0XB2)

---
Rende la transazione non valida se viene osservata una di queste caratteristiche:


- La pila è vuota;
- Il valore in cima alla pila è inferiore a `0`;
- Il flag di disabilitazione per il valore in cima alla pila è indefinito e; La versione della transazione è inferiore a `2` o; Il flag di disabilitazione per il campo `nSequence` dell'ingresso è impostato o; Il tipo di timelock non è lo stesso tra il campo `nSequence` e il valore in cima alla pila (tempo reale o numero di blocchi) o; Il valore in cima alla pila è maggiore del valore del campo `nSequence` dell'ingresso.

Se viene osservata una o più di queste caratteristiche, lo script contenente l'opzione `OP_CHECKSEQUENCEVERIFY` non può essere soddisfatto. Se tutte le condizioni sono valide, `OP_CHECKSEQUENCEVERIFY` agisce come un `OP_NOP`, cioè non esegue alcuna azione sullo script. È come se sparisse. `OP_CHECKSEQUENCEVERIFY` impone quindi un vincolo temporale relativo alla spesa dell'UTXO assicurato con lo script che lo contiene. Può farlo sotto forma di tempo reale o di numero di blocchi. A tal fine, limita i possibili valori del campo `nSequence` dell'input che lo spende, e questo campo `nSequence` limita a sua volta il momento in cui la transazione che include questo input può essere inclusa in un blocco.

> ► *Questo opcode sostituisce `OP_NOP`. È stato inserito in `OP_NOP3`. Viene spesso indicato con l'acronimo "CSV". Si noti che `OP_CSV` non deve essere confuso con il campo `nSequence` di una transazione. Il primo utilizza il secondo, ma la loro natura e le loro azioni sono diverse.*