---
term: OP_NUMEQUALVERIFY (0X9D)

---
Combina las operaciones `OP_NUMEQUAL` y `OP_VERIFY`. Compara numéricamente los dos elementos superiores de la pila. Si los valores son iguales, `OP_NUMEQUALVERIFY` elimina el resultado verdadero de la pila y continúa la ejecución del script. Si los valores no son iguales, el resultado es falso y el script falla inmediatamente.