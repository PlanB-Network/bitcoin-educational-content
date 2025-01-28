---
term: OP_TOALTSTACK (0X6B)

---
Toma la parte superior de la pila principal (*pila principal*) y la mueve a la pila alterna (*pila alterna*). Este opcode se utiliza para almacenar temporalmente los datos a un lado para su uso posterior en el script. El elemento movido se elimina así de la pila principal. a continuación, se utilizará `OP_FROMALTSTACK` para volver a colocarlo encima de la pila principal.