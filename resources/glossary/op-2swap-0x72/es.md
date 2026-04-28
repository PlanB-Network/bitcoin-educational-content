---
term: OP_2SWAP (0X72)

definition: Opcode que intercambia los dos primeros elementos de la pila por los dos siguientes.
---
Intercambia los dos elementos en la parte superior de la pila con los dos elementos justo debajo de ellos. Por ejemplo, si la pila es:

```text
A
B
C
D
```

`OP_2SWAP` producirá:

```text
C
D
A
B
```