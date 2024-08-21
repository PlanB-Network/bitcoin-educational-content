---
term: OP_2OVER (0X70)
---

Kopeerib kaks elementi, mis asuvad virna neljandal ja kolmandal positsioonil ülevalt vaadates, ning asetab need virna tippu. Näiteks, kui virn on:

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