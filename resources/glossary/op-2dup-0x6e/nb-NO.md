---
term: OP_2DUP (0X6E)

definition: Opcode som dupliserer de to øverste elementene på stakken.
---
Dupliserer de to øverste elementene i bunken, og plasserer dem deretter på toppen av bunken. For eksempel, hvis bunken er:

```text
A
B
C
D
```

`OP_2DUP` vil produsere:

```text
A
B
A
B
C
D
```