---
term: OP_3DUP (0X6F)
---

Duplicira prva tri Elements sa vrha steka, zatim ih postavlja na vrh steka. Na primer, ako je stek:


```text
A
B
C
D
```


`OP_3DUP` će proizvesti:


```text
A
B
C
A
B
C
D
```