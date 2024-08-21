---
term: OP_3DUP (0X6F)
---

Duplikuje tři nejvyšší prvky zásobníku a poté je umístí zpět na vrchol zásobníku. Například, pokud je zásobník:

```text
A
B
C
D
```

`OP_3DUP` vytvoří:

```text
A
B
C
A
B
C
D
```