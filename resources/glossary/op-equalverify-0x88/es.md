---
term: OP_EQUALVERIFY (0X88)
---

Combina las funciones de `OP_EQUAL` y `OP_VERIFY`. Primero verifica la igualdad de los dos valores superiores en la pila, luego requiere que el resultado sea distinto de cero, de lo contrario, la transacción es inválida. `OP_EQUALVERIFY` se utiliza notablemente en scripts de verificación de direcciones.