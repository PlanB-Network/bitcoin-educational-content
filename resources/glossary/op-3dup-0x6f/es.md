---
term: OP_3DUP (0X6F)

definition: Opcode que duplica los tres elementos de la parte superior de la pila.
---
Duplica los tres primeros elementos de la pila y los coloca encima de ella. Por ejemplo, si la pila es:

```text
A
B
C
D
```

`OP_3DUP` producirá:

```text
A
B
C
A
B
C
D
```