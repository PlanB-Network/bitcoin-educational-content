---
term: OP_WITHIN (0XA5)

definition: Opcode que verifica se um valor se encontra num intervalo definido por outros dois valores.
---
Verifica se o elemento de topo da pilha está dentro do intervalo definido pelo segundo e terceiro elementos de topo. Em outras palavras, `OP_WITHIN` verifica se o elemento do topo é maior ou igual ao segundo e menor que o terceiro. Se esta condição for verdadeira, ele coloca `1` (verdadeiro) na pilha, caso contrário, ele coloca `0` (falso).