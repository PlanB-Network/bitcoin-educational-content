---
term: OP_NOP (0X61)

---
Non produce alcun effetto sulla pila o sullo stato dello script. Non esegue alcun movimento, controllo o modifica. Semplicemente non fa nulla, a meno che non si decida altrimenti tramite un soft fork. In effetti, da quando sono stati modificati da Satoshi Nakamoto nel 2010, i comandi `OP_NOP` (da `OP_NOP1` (`0XB0`) a `OP_NOP10` (`0XB9`)) sono utilizzati per aggiungere nuovi opcode sotto forma di soft fork.

Pertanto, `OP_NOP2` (`0XB1`) e `OP_NOP3` (`0XB2`) sono già stati utilizzati per implementare rispettivamente `OP_CHECKLOCKTIMEVERIFY` e `OP_CHECKSEQUENCEVERIFY`. Vengono utilizzati in combinazione con `OP_DROP` per rimuovere i valori temporali associati dallo stack, consentendo così di continuare l'esecuzione dello script, indipendentemente dal fatto che il nodo sia aggiornato o meno. I comandi `OP_NOP`, quindi, consentono di inserire un punto di interruzione in uno script per verificare la presenza di ulteriori condizioni già esistenti o che potrebbero essere aggiunte con futuri soft fork. Da Tapscript, l'uso di `OP_NOP` è stato sostituito dal più efficiente `OP_SUCCESS`.