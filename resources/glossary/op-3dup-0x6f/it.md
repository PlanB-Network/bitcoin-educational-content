---
term: OP_3DUP (0X6F)

definition: Opcode che duplica i tre elementi in cima allo stack.
---
Duplica i primi tre elementi della pila e li mette in cima alla pila. Ad esempio, se la pila è:

```text
A
B
C
D
```

`OP_3DUP` produrrà:

```text
A
B
C
A
B
C
D
```