---
term: OP_EQUALVERIFY (0X88)

---
Combina las funciones de `OP_EQUAL` y `OP_VERIFY`. Primero comprueba la igualdad de los dos valores superiores de la pila, luego requiere que el resultado sea distinto de cero, de lo contrario, la operación no es válida. `OP_EQUALVERIFY` se utiliza especialmente en scripts de verificación de direcciones.