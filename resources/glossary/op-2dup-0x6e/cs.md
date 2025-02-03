---
term: OP_2DUP (0X6E)

---
Duplikuje dva horní prvky zásobníku a umístí je na jeho vrchol. Pokud je například zásobník:

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