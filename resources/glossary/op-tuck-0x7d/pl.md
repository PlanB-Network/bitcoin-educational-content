---
term: OP_TUCK (0X7D)
---

Kopiuje element znajdujący się na szczycie stosu i wstawia go pomiędzy drugi i trzeci element stosu. Na przykład, jeśli stos to:


```text
A
B
C
D
```


`OP_TUCK` zduplikuje górny element `A` i umieści go na trzeciej pozycji. Wynikowy stos będzie wyglądał następująco:


```text
A
B
A
C
D
```