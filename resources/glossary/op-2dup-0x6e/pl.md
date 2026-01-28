---
term: OP_2DUP (0X6E)
definition: Opkod duplikujący dwa elementy na szczycie stosu.
---

Duplikuje dwa górne Elements stosu, a następnie umieszcza je na wierzchu stosu. Na przykład, jeśli stos to:


```text
A
B
C
D
```


`OP_2DUP` wygeneruje:


```text
A
B
A
B
C
D
```