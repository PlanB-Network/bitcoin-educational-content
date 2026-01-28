---
term: OP_2OVER (0X70)
definition: Opkod koji kopira 3. i 4. element steka na vrh.
---

Kopira dve Elements koje su na četvrtoj i trećoj poziciji od vrha steka, zatim ih postavlja na vrh steka. Na primer, ako je stek:


```text
A
B
C
D
```


`OP_2OVER` će proizvesti:


```text
C
D
A
B
C
D
```