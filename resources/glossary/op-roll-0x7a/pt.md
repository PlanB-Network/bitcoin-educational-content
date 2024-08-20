---
term: OP_ROLL (0X7A)
---

Move um item da pilha para o topo da pilha, com base na profundidade especificada pelo valor no topo da pilha antes da operação. Por exemplo, se o valor no topo da pilha for `4`, `OP_ROLL` selecionará o quarto item a partir do topo da pilha, e moverá este valor para o topo. `OP_ROLL` desempenha a mesma função que `OP_PICK`, exceto que remove o item de sua posição original.