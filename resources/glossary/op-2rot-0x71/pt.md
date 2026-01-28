---
term: OP_2ROT (0X71)

definition: Opcode que move o 5º e o 6º elementos da pilha para o topo.
---
Move os dois elementos que estão na sexta e quinta posições do topo da pilha para o topo. Por exemplo, se a pilha for:

```text
A
B
C
D
E
F
```

o `OP_2ROT` produzirá:

```text
E
F
A
B
C
D
```