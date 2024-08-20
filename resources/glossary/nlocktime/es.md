---
term: NLOCKTIME
---

Un campo incrustado en las transacciones que establece una condición basada en el tiempo antes de la cual la transacción no puede ser añadida a un bloque válido. Este parámetro permite especificar un tiempo exacto (marca de tiempo Unix) o un número específico de bloques como condición para que la transacción sea considerada válida. Por lo tanto, es un bloqueo de tiempo absoluto (no relativo). El `nLockTime` afecta a toda la transacción y permite efectivamente la verificación de tiempo, mientras que el opcode `OP_CHECKLOCKTIMEVERIFY` solo permite comparar el valor superior de la pila con el valor de `nLockTime`.