---
term: OP_FROMALTSTACK (0X6C)

definition: Opcode que move um elemento da pilha alternativa para a pilha principal.
---
Remove o item superior da pilha alternativa (*pilha alternativa*) e coloca-o no topo da pilha principal (*pilha principal*). Este opcode é utilizado para recuperar dados temporariamente armazenados na pilha alternativa. Simplificando, é a operação inversa de `OP_TOALTSTACK`.