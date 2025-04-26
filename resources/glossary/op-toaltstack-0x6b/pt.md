---
term: OP_TOALTSTACK (0X6B)

---
Pega no topo da pilha principal (*main stack*) e move-o para a pilha alternativa (*alt stack*). Este opcode é utilizado para armazenar temporariamente dados para utilização posterior no script. O item movido é, portanto, removido da pilha principal. o `OP_FROMALTSTACK` será então utilizado para colocá-lo de volta no topo da pilha principal.