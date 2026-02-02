---
term: OP_2OVER (0X70)
definition: Opcode die het 3e en 4e element van de stack naar de bovenkant kopieert.
---

Kopieert de twee Elements die op de vierde en derde positie vanaf de bovenkant van de stapel staan en plaatst ze vervolgens bovenop de stapel. Bijvoorbeeld, als de stapel is:


```text
A
B
C
D
```


`OP_2OVER` zal produceren:


```text
C
D
A
B
C
D
```