---
term: OP_2ROT (0X71)

definition: Opcode che sposta il 5° e il 6° elemento dello stack in cima.
---
Sposta i due elementi che si trovano in sesta e quinta posizione dall'inizio della pila all'inizio. Ad esempio, se la pila è:

```text
A
B
C
D
E
F
```

`OP_2ROT` produrrà:

```text
E
F
A
B
C
D
```