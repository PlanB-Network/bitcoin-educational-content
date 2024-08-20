---
term: OP_TOALTSTACK (0X6B)
---

Toma el elemento superior de la pila principal (*main stack*) y lo mueve a la pila alternativa (*alt stack*). Este código de operación se utiliza para almacenar temporalmente datos aparte para su uso posterior en el script. El elemento movido es así eliminado de la pila principal. `OP_FROMALTSTACK` se utilizará entonces para volver a colocarlo en la parte superior de la pila principal.