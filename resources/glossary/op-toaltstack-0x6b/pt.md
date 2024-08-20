---
term: OP_TOALTSTACK (0X6B)
---

Leva o topo da pilha principal (*main stack*) e o move para a pilha alternativa (*alt stack*). Este opcode é usado para armazenar temporariamente dados à parte para uso posterior no script. O item movido é, assim, removido da pilha principal. `OP_FROMALTSTACK` será então usado para colocá-lo de volta no topo da pilha principal.