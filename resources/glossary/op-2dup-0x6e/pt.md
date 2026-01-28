---
term: OP_2DUP (0X6E)

definition: Opcode que duplica os dois elementos no topo da pilha.
---
Duplica os dois elementos do topo da pilha e, em seguida, coloca-os no topo da pilha. Por exemplo, se a pilha for:

```text
A
B
C
D
```

o `OP_2DUP` produzirá:

```text
A
B
A
B
C
D
```