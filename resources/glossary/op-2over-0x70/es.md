---
term: OP_2OVER (0X70)

definition: Opcode que copia los elementos 3º y 4º de la pila en la parte superior.
---
Copia los dos elementos que están en la cuarta y tercera posición desde la parte superior de la pila, y luego los coloca en la parte superior de la pila. Por ejemplo, si la pila es:

```text
A
B
C
D
```

`OP_2OVER` producirá:

```text
C
D
A
B
C
D
```