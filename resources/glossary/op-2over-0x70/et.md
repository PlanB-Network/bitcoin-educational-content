---
term: OP_2OVER (0X70)

definition: Opkood, mis kopeerib pinu 3. ja 4. elemendi ülaosale.
---
Kopeerib kaks elementi, mis on virna neljandas ja kolmandas positsioonis, ja asetab need virna tippu. Näiteks kui virnas on:

```text
A
B
C
D
```

`OP_2OVER` toodab:

```text
C
D
A
B
C
D
```