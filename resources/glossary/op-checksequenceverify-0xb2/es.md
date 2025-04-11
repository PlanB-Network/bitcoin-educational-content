---
term: OP_CHECKSEQUENCEVERIFY (0XB2)

---
Anula la transacción si se observa alguna de estas características:


- La pila está vacía;
- El valor en la parte superior de la pila es menor que `0`;
- El indicador de desactivación para el valor en la parte superior de la pila no está definido y; La versión de la transacción es menor que `2` o; El indicador de desactivación para el campo `nSequence` de la entrada está activado o; El tipo de bloqueo de tiempo no es el mismo entre el campo `nSequence` y el valor en la parte superior de la pila (tiempo real o número de bloques) o; El valor en la parte superior de la pila es mayor que el valor del campo `nSequence` de la entrada.

Si una o más de estas características son observadas, el script que contiene el `OP_CHECKSEQUENCEVERIFY` no puede ser satisfecho. Si todas las condiciones son válidas, entonces `OP_CHECKSEQUENCEVERIFY` actúa como un `OP_NOP`, lo que significa que no realiza ninguna acción sobre el script. Es como si desapareciera. por tanto, `OP_CHECKSEQUENCEVERIFY` impone una restricción temporal relativa al gasto del UTXO asegurado con el script que lo contiene. Puede hacerlo en forma de tiempo real o como un número de bloques. Para ello, restringe los valores posibles para el campo `nSequence` de la entrada que lo gasta, y este campo `nSequence` restringe a su vez cuándo puede incluirse en un bloque la transacción que incluye esta entrada.

> ► *Este opcode sustituye a `OP_NOP`. Se colocó en `OP_NOP3`. A menudo se hace referencia a él por su acrónimo "CSV". Nota, `OP_CSV` no debe confundirse con el campo `nSequence` de una transacción. El primero utiliza el segundo, pero sus naturalezas y acciones son diferentes.*