---
term: OP_PUSHDATA4 (0X4E)

---
Permite introducir una gran cantidad de datos en la pila. Va seguido de cuatro bytes (little-endian) que indican la longitud de los datos a empujar (hasta unos 4,3 GB). Este opcode se utiliza para insertar datos muy grandes en los scripts, aunque su uso es extremadamente raro debido a las limitaciones prácticas del tamaño de las transacciones.