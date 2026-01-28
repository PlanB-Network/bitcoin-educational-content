---
term: OP_TUCK (0X7D)

definition: Opcode som kopierer toppen av stakken og setter den inn på tredje posisjon.
---
Kopierer elementet øverst i bunken og setter det inn mellom det andre og tredje elementet i bunken. For eksempel, hvis stakken er:

```text
A
B
C
D
```

`OP_TUCK` vil duplisere det øverste elementet `A` og plassere det i tredje posisjon. Den resulterende stabelen vil være:

```text
A
B
A
C
D
```