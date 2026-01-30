---
term: OP_WITHIN (0XA5)

definition: Opcode che verifica se un valore si trova all'interno di un intervallo definito da altri due valori.
---
Verifica se l'elemento superiore della pila rientra nell'intervallo definito dal secondo e dal terzo elemento superiore. In altre parole, `OP_WITHIN` controlla se l'elemento superiore è maggiore o uguale al secondo e minore del terzo. Se questa condizione è vera, spinge `1` (vero) sulla pila, altrimenti spinge `0` (falso).