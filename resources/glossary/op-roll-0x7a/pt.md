---
term: OP_ROLL (0X7A)

definition: Opcode que move um elemento da pilha numa profundidade especificada para o topo.
---
Move um item da pilha para o topo da pilha, baseado na profundidade especificada pelo valor no topo da pilha antes da operação. Por exemplo, se o valor no topo da pilha é `4`, `OP_ROLL` irá selecionar o quarto item do topo da pilha, e irá mover este valor para o topo. `OP_ROLL` tem a mesma função que `OP_PICK`, exceto que remove o item de sua posição original.