---
term: OP_2ROT (0X71)
definition: Opcode die het 5e en 6e element van de stack naar de bovenkant verplaatst.
---

Verplaatst de twee Elements die op de zesde en vijfde positie staan van de top van de stapel naar de top. Bijvoorbeeld, als de stapel is:


```text
A
B
C
D
E
F
```


`OP_2ROT` zal produceren:


```text
E
F
A
B
C
D
```