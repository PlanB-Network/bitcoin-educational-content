---
term: OP_2OVER (0X70)
---

Kopíruje dva prvky, které se nachází na čtvrté a třetí pozici od vrcholu zásobníku, a poté je umístí na vrchol zásobníku. Například, pokud je zásobník:

```text
A
B
C
D
```

`OP_2OVER` vytvoří:

```text
C
D
A
B
C
D
```