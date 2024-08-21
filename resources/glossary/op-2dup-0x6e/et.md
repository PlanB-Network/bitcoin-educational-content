---
term: OP_2DUP (0X6E)
---

Dubleerib kaks pealmist elementi virnas, seejärel asetab need virna tippu. Näiteks, kui virn on:

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