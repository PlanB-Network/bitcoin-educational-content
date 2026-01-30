---
term: OP_2SWAP (0X72)

definition: Opkód zamění první dva prvky zásobníku s následujícími dvěma.
---
Vymění dva prvky na vrcholu zásobníku za dva prvky těsně pod nimi. Pokud je například zásobník:

```text
A
B
C
D
```

`OP_2SWAP` vytvoří:

```text
C
D
A
B
```