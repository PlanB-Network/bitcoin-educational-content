---
term: OP_ROLL (0X7A)
---

Mueve un elemento de la pila al tope de la misma, basándose en la profundidad especificada por el valor en el tope de la pila antes de la operación. Por ejemplo, si el valor en el tope de la pila es `4`, `OP_ROLL` seleccionará el cuarto elemento desde el tope de la pila, y moverá este valor al tope. `OP_ROLL` cumple la misma función que `OP_PICK`, excepto que elimina el elemento de su posición original.