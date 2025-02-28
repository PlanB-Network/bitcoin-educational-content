---
term: OP_3DUP (0X6F)

---
Duplikuje tři horní prvky zásobníku a umístí je na jeho vrchol. Například pokud je zásobník:

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