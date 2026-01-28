---
term: OP_HASH160 (0XA9)

definition: Opcode que aplica hash al elemento superior con SHA256 y luego con RIPEMD160.
---
Toma el elemento superior de la pila y lo sustituye por su hash, utilizando simultáneamente las funciones `SHA256` y `RIPEMD160`. Este proceso de dos pasos genera una huella digital de 160 bits.