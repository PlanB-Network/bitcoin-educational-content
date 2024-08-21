---
term: OP_TUCK (0X7D)
---

Kopeerib virna tipus oleva elemendi ja sisestab selle teise ja kolmanda elemendi vahele. Näiteks, kui virn on:

```text
A
B
C
D
```

`OP_TUCK` dubleerib tipus oleva elemendi `A` ja asetab selle kolmandasse positsiooni. Tulemuseks olev virn saab olema:

```text
A
B
A
C
D
```