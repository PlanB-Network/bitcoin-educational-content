---
term: OP_2DUP (0X6E)
---

Duplikuje dva nejvyšší prvky zásobníku a poté je umístí na vrchol zásobníku. Například, pokud je zásobník:

```text
A
B
C
D
```

`OP_2DUP` vytvoří:

```text
A
B
A
B
C
D
```