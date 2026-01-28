---
term: OP_2DUP (0X6E)

definition: Opkood, mis dubleerib kaks pinu peal olevat elementi.
---
Duplitseerib virna kaks ülemist elementi ja asetab need virna tippu. Näiteks kui virnas on:

```text
A
B
C
D
```

`OP_2DUP` toodab:

```text
A
B
A
B
C
D
```