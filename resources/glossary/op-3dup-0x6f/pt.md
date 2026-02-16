---
term: OP_3DUP (0X6F)

definition: Opcode que duplica os três elementos no topo da pilha.
---
Duplica os três primeiros elementos da pilha e, em seguida, coloca-os no topo da pilha. Por exemplo, se a pilha for:

```text
A
B
C
D
```

o `OP_3DUP` produzirá:

```text
A
B
C
A
B
C
D
```