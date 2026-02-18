---
term: OP_2DUP (0X6E)
definition: Opkod koji duplira dva elementa na vrhu steka.
---

Duplicira dva vrha Elements steka, zatim ih postavlja na vrh steka. Na primer, ako je stek:


```text
A
B
C
D
```


`OP_2DUP` će proizvesti:


```text
A
B
A
B
C
D
```