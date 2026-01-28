---
term: OP_2ROT (0X71)

definition: Opkód přesune 5. a 6. prvek zásobníku na vrchol.
---
Přesune dva prvky, které se nacházejí na šesté a páté pozici, z vrcholu zásobníku na vrchol. Například pokud je zásobník:

```text
A
B
C
D
E
F
```

`OP_2ROT` vytvoří:

```text
E
F
A
B
C
D
```