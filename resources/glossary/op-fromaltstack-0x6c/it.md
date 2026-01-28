---
term: OP_FROMALTSTACK (0X6C)

definition: Opcode che sposta un elemento dall'alternate stack allo stack principale.
---
Rimuove il primo elemento dalla pila alternativa (*alt stack*) e lo colloca in cima alla pila principale (*main stack*). Questo opcode viene utilizzato per recuperare i dati temporaneamente memorizzati nello stack alternativo. In poche parole, è l'operazione inversa di `OP_TOALTSTACK`.