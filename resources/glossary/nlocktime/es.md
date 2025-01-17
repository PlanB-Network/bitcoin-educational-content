---
term: NLOCKTIME

---
Campo incrustado en las transacciones que establece una condición basada en el tiempo antes de la cual la transacción no puede añadirse a un bloque válido. Este parámetro permite especificar una hora exacta (Unix timestamp) o un número específico de bloques como condición para que la transacción se considere válida. Por tanto, se trata de un bloqueo de tiempo absoluto (no relativo). El `nLockTime` afecta a toda la transacción y permite efectivamente la verificación del tiempo, mientras que el opcode `OP_CHECKLOCKTIMEVERIFY` sólo permite comparar el valor superior de la pila con el valor `nLockTime`.