---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)
---

Hace que la transacción sea inválida a menos que se cumplan todas estas condiciones:
* La pila no está vacía;
* El valor en la parte superior de la pila es mayor o igual a `0`;
* El tipo de bloqueo temporal es el mismo entre el campo `nLockTime` y el valor en la parte superior de la pila (tiempo real o número de bloque);
* El campo `nSequence` de la entrada no es igual a `0xffffffff`;
* El valor en la parte superior de la pila es mayor o igual al valor del campo `nLockTime` de la transacción.

Si alguna de estas condiciones no se cumple, el script que contiene el `OP_CHECKLOCKTIMEVERIFY` no puede ser satisfecho. Si todas estas condiciones son válidas, entonces `OP_CHECKLOCKTIMEVERIFY` actúa como un `OP_NOP`, lo que significa que no realiza ninguna acción sobre el script. Es como si desapareciera. `OP_CHECKLOCKTIMEVERIFY` impone así una restricción de tiempo en el gasto del UTXO asegurado con el script que lo contiene. Puede hacer esto ya sea en forma de una fecha de tiempo Unix o como un número de bloque. Para hacer esto, restringe los valores posibles para el campo `nLockTime` de la transacción que lo gasta, y este campo `nLockTime` a su vez restringe cuándo la transacción puede ser incluida en un bloque.

> ► *Este opcode es un reemplazo para `OP_NOP`. Fue colocado en `OP_NOP2`. A menudo se le refiere por su acrónimo "CLTV". Note, `OP_CLTV` no debe confundirse con el campo `nLockTime` de una transacción. El primero utiliza al segundo, pero sus naturalezas y acciones son diferentes.*