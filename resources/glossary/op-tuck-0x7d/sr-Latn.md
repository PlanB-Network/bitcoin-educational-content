---
term: OP_TUCK (0X7D)
---

Kopira stavku sa vrha steka i umeće je između druge i treće stavke steka. Na primer, ako je stek:


```text
A
B
C
D
```


`OP_TUCK` će duplicirati gornju stavku `A` i postaviti je na treću poziciju. Rezultujuća gomila će biti:


```text
A
B
A
C
D
```