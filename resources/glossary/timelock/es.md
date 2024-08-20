---
term: TIMELOCK
---

Un primitivo de contrato inteligente que permite establecer una condición basada en tiempo que debe cumplirse para que una transacción sea añadida a un bloque. Hay dos tipos de timelocks en Bitcoin:
* El timelock absoluto, que especifica un momento exacto antes del cual la transacción no puede ser incluida en un bloque;
* El timelock relativo, que establece un retraso desde la aceptación de una transacción previa.
El timelock puede definirse ya sea como una fecha expresada en tiempo Unix o como un número de bloque. Finalmente, el timelock puede aplicarse a una salida de transacción utilizando un opcode específico en el script de bloqueo (`OP_CHECKLOCKTIMEVERIFY` o `OP_CHECKSEQUENCEVERIFY`), o a una transacción completa utilizando campos específicos de la transacción (`nLockTime` o `nSequence`).