---
term: OP_CHECKSEQUENCEVERIFY (0XB2)
---

Invalida la transacción si se observa cualquiera de estas características:
* La pila está vacía;
* El valor en la parte superior de la pila es menor que `0`;
* La bandera de desactivación para el valor en la parte superior de la pila no está definida y; La versión de la transacción es menor que `2` o; La bandera de desactivación para el campo `nSequence` de la entrada está establecida o; El tipo de bloqueo temporal no es el mismo entre el campo `nSequence` y el valor en la parte superior de la pila (tiempo real o número de bloques) o; El valor en la parte superior de la pila es mayor que el valor del campo `nSequence` de la entrada.

Si se observa una o más de estas características, el script que contiene el `OP_CHECKSEQUENCEVERIFY` no puede ser satisfecho. Si todas las condiciones son válidas, entonces `OP_CHECKSEQUENCEVERIFY` actúa como un `OP_NOP`, lo que significa que no realiza ninguna acción sobre el script. Es como si desapareciera. `OP_CHECKSEQUENCEVERIFY` impone así una restricción de tiempo relativo sobre el gasto del UTXO asegurado con el script que lo contiene. Puede hacer esto ya sea en forma de tiempo real o como un número de bloques. Para hacer esto, restringe los valores posibles para el campo `nSequence` de la entrada que lo gasta, y este campo `nSequence` a su vez restringe cuándo la transacción que incluye esta entrada puede ser incluida en un bloque.

> ► *Este opcode es un reemplazo para `OP_NOP`. Fue colocado en `OP_NOP3`. A menudo se le refiere por su acrónimo "CSV". Note, `OP_CSV` no debe confundirse con el campo `nSequence` de una transacción. El primero utiliza el segundo, pero sus naturalezas y acciones son diferentes.*