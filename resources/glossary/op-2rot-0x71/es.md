---
term: OP_2ROT (0X71)

definition: Opcode que mueve los elementos 5º y 6º de la pila a la parte superior.
---
Mueve los dos elementos que están en la sexta y quinta posición de la parte superior de la pila a la parte superior. Por ejemplo, si la pila es:

```text
A
B
C
D
E
F
```

`OP_2ROT` producirá:

```text
E
F
A
B
C
D
```