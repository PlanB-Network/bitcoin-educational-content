---
term: OP_TUCK (0X7D)

definition: Opcode kopírující vrchol zásobníku a vkládající jej na třetí pozici.
---
Zkopíruje položku na vrcholu zásobníku a vloží ji mezi druhou a třetí položku zásobníku. Například pokud je zásobník:

```text
A
B
C
D
```

`OP_TUCK` zduplikuje horní položku `A` a umístí ji na třetí pozici. Výsledný zásobník bude:

```text
A
B
A
C
D
```