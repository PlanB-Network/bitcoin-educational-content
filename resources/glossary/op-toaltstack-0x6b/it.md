---
term: OP_TOALTSTACK (0X6B)

definition:
---
Prende la parte superiore dello stack principale (*main stack*) e la sposta nello stack alternativo (*alt stack*). Questo opcode viene utilizzato per memorizzare temporaneamente i dati per un uso successivo nello script. L'elemento spostato viene quindi rimosso dalla pila principale. verrà quindi utilizzato l'opcode `OP_FROMALTSTACK` per rimetterlo in cima alla pila principale.