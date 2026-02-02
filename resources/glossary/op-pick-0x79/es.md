---
term: OP_PICK (0X79)

definition: Opcode que duplica un elemento de la pila a una profundidad especificada hacia la parte superior.
---
Duplica un elemento de la pila y lo coloca en la parte superior de la misma, basándose en la profundidad especificada por el valor en la parte superior de la pila antes de la operación. Por ejemplo, si el valor en la parte superior de la pila es `4`, `OP_PICK` duplicará el cuarto elemento desde la parte superior de la pila, y colocará esta copia en la parte superior.