---
termine: OP_CHECKSEQUENCEVERIFY (0XB2)
---

Rende la transazione non valida se viene osservata anche solo una di queste caratteristiche:
* Lo stack è vuoto;
* Il valore in cima allo stack è inferiore a `0`;
* Il flag di disabilitazione per il valore in cima allo stack è indefinito e; La versione della transazione è inferiore a `2` oppure; Il flag di disabilitazione per il campo `nSequence` dell'input è impostato oppure; Il tipo di timelock non è lo stesso tra il campo `nSequence` e il valore in cima allo stack (tempo reale o numero di blocchi) oppure; Il valore in cima allo stack è maggiore del valore del campo `nSequence` dell'input.

Se viene osservata una o più di queste caratteristiche, lo script contenente `OP_CHECKSEQUENCEVERIFY` non può essere soddisfatto. Se tutte le condizioni sono valide, allora `OP_CHECKSEQUENCEVERIFY` agisce come un `OP_NOP`, il che significa che non esegue alcuna azione sullo script. È come se scomparisse. `OP_CHECKSEQUENCEVERIFY` impone quindi un vincolo temporale relativo alla spesa dell'UTXO assicurato con lo script che lo contiene. Può farlo sia in forma di tempo reale sia come numero di blocchi. Per fare ciò, limita i possibili valori per il campo `nSequence` dell'input che lo spende, e questo campo `nSequence` stesso limita quando la transazione che include questo input può essere inclusa in un blocco.

> ► *Questo opcode sostituisce `OP_NOP`. È stato posizionato su `OP_NOP3`. È spesso indicato con l'acronimo "CSV". Da notare, `OP_CSV` non deve essere confuso con il campo `nSequence` di una transazione. Il primo utilizza il secondo, ma le loro nature e azioni sono diverse.*