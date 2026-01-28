---
term: OP_3DUP (0X6F)
definition: Opkod duplikujący trzy elementy na szczycie stosu.
---

Duplikuje trzy górne Elements stosu, a następnie umieszcza je na wierzchu stosu. Na przykład, jeśli stos to:


```text
A
B
C
D
```


`OP_3DUP` spowoduje:


```text
A
B
C
A
B
C
D
```