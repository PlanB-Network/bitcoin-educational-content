---
term: OP_TUCK (0X7D)

definition: Opcode, mis kopeerib pinu ülaosa ja sisestab selle kolmandale kohale.
---
Kopeerib virna ülaosas oleva elemendi ja lisab selle virna teise ja kolmanda elemendi vahele. Näiteks kui virnas on:

```text
A
B
C
D
```

`OP_TUCK` dubleerib ülemise elemendi `A` ja paigutab selle kolmandale positsioonile. Tulemuseks on järgmine virn:

```text
A
B
A
C
D
```