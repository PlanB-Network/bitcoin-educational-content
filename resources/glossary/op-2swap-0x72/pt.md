---
term: OP_2SWAP (0X72)

definition: Opcode que troca os dois primeiros elementos da pilha com os dois seguintes.
---
Troca os dois elementos no topo da pilha com os dois elementos imediatamente abaixo deles. Por exemplo, se a pilha for:

```text
A
B
C
D
```

o `OP_2SWAP` produzirá:

```text
C
D
A
B
```