---
term: OP_PUSHDATA1 (0X4C)

definition: Opcode que coloca hasta 255 bytes de datos en la pila.
---
Introduce una determinada cantidad de datos en la pila. Va seguido de un byte que indica la longitud de los datos a introducir (hasta 255 bytes). Este opcode se utiliza para incluir datos de tamaño variable en los scripts.