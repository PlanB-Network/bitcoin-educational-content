---
term: OP_PUSHDATA4 (0X4E)
---

Permite empujar una cantidad muy grande de datos en la pila. Le siguen cuatro bytes (little-endian) que indican la longitud de los datos a empujar (hasta aproximadamente 4.3 GB). Este opcode se utiliza para insertar datos muy grandes en scripts, aunque su uso es extremadamente raro debido a limitaciones prácticas en el tamaño de la transacción.