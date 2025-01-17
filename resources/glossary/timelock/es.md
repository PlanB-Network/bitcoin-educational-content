---
term: TIMELOCK

---
Una primitiva de contrato inteligente que permite establecer una condición basada en el tiempo que debe cumplirse para que una transacción se añada a un bloque. Existen dos tipos de timelocks en Bitcoin:


- El bloqueo temporal absoluto, que especifica un momento exacto antes del cual la transacción no puede incluirse en un bloque;
- El bloqueo de tiempo relativo, que establece un retraso desde la aceptación de una transacción anterior.

El timelock puede definirse como una fecha expresada en tiempo Unix o como un número de bloque. Por último, el bloqueo de tiempo puede aplicarse a la salida de una transacción utilizando un opcode específico en el script de bloqueo (`OP_CHECKLOCKTIMEVERIFY` u `OP_CHECKSEQUENCEVERIFY`), o a una transacción completa utilizando campos de transacción específicos (`nLockTime` o `nSequence`).