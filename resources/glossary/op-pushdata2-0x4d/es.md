---
term: OP_PUSHDATA2 (0X4D)

definition: Opcode que coloca hasta 65 KB de datos en la pila.
---
Permite introducir una gran cantidad de datos en la pila. Va seguido de dos bytes (little-endian) que especifican la longitud de los datos a introducir (hasta unos 65 KB). Se utiliza para insertar datos de mayor tamaño en los scripts.