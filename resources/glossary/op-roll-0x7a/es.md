---
term: OP_ROLL (0X7A)

---
Mueve un elemento de la pila a la parte superior de la pila, basándose en la profundidad especificada por el valor en la parte superior de la pila antes de la operación. Por ejemplo, si el valor en la parte superior de la pila es `4`, `OP_ROLL` seleccionará el cuarto elemento de la parte superior de la pila, y moverá este valor a la parte superior. la función de `OP_ROLL` es la misma que la de `OP_PICK`, salvo que elimina el elemento de su posición original.