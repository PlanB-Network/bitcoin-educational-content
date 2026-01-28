---
term: OP_FROMALTSTACK (0X6C)

definition: Opcode que mueve un elemento de la pila alternativa a la pila principal.
---
Elimina el elemento superior de la pila alternativa (*pila alternativa*) y lo coloca en la parte superior de la pila principal (*pila principal*). Este opcode se utiliza para recuperar datos almacenados temporalmente en la pila alternativa. En pocas palabras, es la operación inversa de `OP_TOALTSTACK`.