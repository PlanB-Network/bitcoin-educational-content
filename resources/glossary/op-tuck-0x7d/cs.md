---
term: OP_TUCK (0X7D)
---

Kopíruje prvek na vrcholu zásobníku a vloží ho mezi druhý a třetí prvek zásobníku. Například, pokud je zásobník:

```text
A
B
C
D
```

`OP_TUCK` zduplikuje prvek na vrcholu `A` a umístí ho na třetí pozici. Výsledný zásobník bude:

```text
A
B
A
C
D
```