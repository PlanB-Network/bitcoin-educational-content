---
term: OP_2OVER (0X70)
---

Kopiuje dwa Elements, które znajdują się na czwartej i trzeciej pozycji od góry stosu, a następnie umieszcza je na wierzchu stosu. Na przykład, jeśli stos to:


```text
A
B
C
D
```


`OP_2OVER` wygeneruje:


```text
C
D
A
B
C
D
```