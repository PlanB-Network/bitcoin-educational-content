---
termine: OP_NOP (0X61)
---

Non produce alcun effetto sullo stack o sullo stato dello script. Non esegue movimenti, controlli o modifiche. Semplicemente non fa nulla a meno che non venga deciso diversamente tramite un soft fork. Infatti, da quando sono stati modificati da Satoshi Nakamoto nel 2010, i comandi `OP_NOP` (`OP_NOP1` (`0XB0`) fino a `OP_NOP10` (`0XB9`)) sono utilizzati per aggiungere nuovi opcode sotto forma di soft fork.

Così, `OP_NOP2` (`0XB1`) e `OP_NOP3` (`0XB2`) sono già stati utilizzati per implementare rispettivamente `OP_CHECKLOCKTIMEVERIFY` e `OP_CHECKSEQUENCEVERIFY`. Vengono utilizzati in combinazione con `OP_DROP` per rimuovere i valori temporali associati dallo stack, permettendo così la continuazione dell'esecuzione dello script, sia che il nodo sia aggiornato o meno. I comandi `OP_NOP`, quindi, consentono l'inserimento di un punto di interruzione in uno script per verificare ulteriori condizioni che già esistono o possono essere aggiunte con futuri soft fork. Da Tapscript, l'uso di `OP_NOP` è stato sostituito dal più efficiente `OP_SUCCESS`.