---
term: OP_2DUP (0X6E)
definition: Opcode die de twee bovenste elementen op de stack dupliceert.
---

Dupliceert de twee bovenste Elements van de stapel en plaatst ze bovenop de stapel. Bijvoorbeeld, als de stapel is:


```text
A
B
C
D
```


`OP_2DUP` zal produceren:


```text
A
B
A
B
C
D
```