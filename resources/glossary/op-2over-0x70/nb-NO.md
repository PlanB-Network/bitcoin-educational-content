---
term: OP_2OVER (0X70)

definition: Opcode som kopierer det 3. og 4. elementet i stakken til toppen.
---
Kopierer de to elementene som er i fjerde og tredje posisjon fra toppen av bunken, og plasserer dem deretter på toppen av bunken. For eksempel, hvis bunken er:

```text
A
B
C
D
```

`OP_2OVER` vil produsere:

```text
C
D
A
B
C
D
```