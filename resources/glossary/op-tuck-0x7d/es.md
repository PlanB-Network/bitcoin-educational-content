---
term: OP_TUCK (0X7D)

definition: Opcode que copia la parte superior de la pila e la inserta en la tercera posición.
---
Copia el elemento situado en la parte superior de la pila y lo inserta entre el segundo y el tercer elemento de la pila. Por ejemplo, si la pila es:

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