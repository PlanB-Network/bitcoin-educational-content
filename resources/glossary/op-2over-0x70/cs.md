---
term: OP_2OVER (0X70)

definition: Opkód zkopíruje 3. a 4. prvek zásobníku na vrchol.
---
Zkopíruje dva prvky, které jsou na čtvrté a třetí pozici od vrcholu zásobníku, a umístí je na vrchol zásobníku. Například pokud je zásobník:

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