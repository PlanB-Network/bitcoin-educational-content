---
term: OP_2DUP (0X6E)

definition: Opcode que duplica los dos elementos de la parte superior de la pila.
---
Duplica los dos elementos superiores de la pila y los coloca encima de ella. Por ejemplo, si la pila es:

```text
A
B
C
D
```

`OP_2DUP` producirá:

```text
A
B
A
B
C
D
```