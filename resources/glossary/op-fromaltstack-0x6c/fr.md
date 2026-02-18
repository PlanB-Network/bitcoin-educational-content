---
term: OP_FROMALTSTACK (0X6C)
definition: Opcode déplaçant un élément de la pile alternative vers la pile principale.
---

Retire le sommet de la pile alternative (*alt stack*) et le place sur le sommet de la pile principale (*main stack*). Cet opcode est utilisé pour récupérer des données stockées temporairement sur la pile alternative. Pour simplifier, c'est l'opération inverse de `OP_TOALTSTACK`.
