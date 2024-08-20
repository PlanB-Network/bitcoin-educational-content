---
term: OP_TUCK (0X7D)
---

Copia el elemento en la cima de la pila e inserta una copia entre el segundo y tercer elemento de la pila. Por ejemplo, si la pila es:

```text
A
B
C
D
```

`OP_TUCK` duplicará el elemento superior `A` y lo colocará en la tercera posición. La pila resultante será:

```text
A
B
A
C
D
```