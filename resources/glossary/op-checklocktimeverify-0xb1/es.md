---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)

---
Hace que la transacción no sea válida a menos que se cumplan todas estas condiciones:


- La pila no está vacía;
- El valor en la parte superior de la pila es mayor o igual que `0`;
- El tipo de bloqueo de tiempo es el mismo entre el campo `nLockTime` y el valor en la parte superior de la pila (tiempo real o número de bloque);
- El campo `nSequence` de la entrada no es igual a `0xffffffff`;
- El valor en la parte superior de la pila es mayor o igual que el valor del campo `nLockTime` de la transacción.

Si alguna de estas condiciones no se cumple, el script que contiene el `OP_CHECKLOCKTIMEVERIFY` no puede ser satisfecho. Si todas estas condiciones son válidas, entonces `OP_CHECKLOCKTIMEVERIFY` actúa como un `OP_NOP`, lo que significa que no realiza ninguna acción sobre el script. Es como si desapareciera. por tanto, `OP_CHECKLOCKTIMEVERIFY` impone una restricción temporal al gasto del UTXO asegurado con el script que lo contiene. Puede hacerlo en forma de una fecha de tiempo Unix o como un número de bloque. Para ello, restringe los valores posibles para el campo `nLockTime` de la transacción que lo gasta, y este campo `nLockTime` restringe por sí mismo cuándo puede incluirse la transacción en un bloque.

> ► *Este opcode sustituye a `OP_NOP`. Se colocó en `OP_NOP2`. A menudo se hace referencia a él por su acrónimo "CLTV". Nota, `OP_CLTV` no debe confundirse con el campo `nLockTime` de una transacción. El primero utiliza el segundo, pero sus naturalezas y acciones son diferentes.*