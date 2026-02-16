---
term: OP_2OVER (0X70)

definition: Opcode che copia il 3° e il 4° elemento dello stack in cima.
---
Copia i due elementi che si trovano nella quarta e nella terza posizione dalla cima della pila e li mette in cima alla pila. Ad esempio, se la pila è:

```text
A
B
C
D
```

`OP_2OVER` produrrà:

```text
C
D
A
B
C
D
```