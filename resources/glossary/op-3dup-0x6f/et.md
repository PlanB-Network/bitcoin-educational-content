---
term: OP_3DUP (0X6F)

definition: Opkood, mis dubleerib kolm pinu peal olevat elementi.
---
Duplitseerib virna kolm esimest elementi ja asetab need virna tippu. Näiteks kui virnas on:

```text
A
B
C
D
```

`OP_3DUP` annab tulemuseks:

```text
A
B
C
A
B
C
D
```