---
term: OP_HASH160 (0XA9)

definition: Opcode che esegue l'hash dell'elemento in cima prima con SHA256 e poi con RIPEMD160.
---
Prende l'elemento superiore dallo stack e lo sostituisce con il suo hash, utilizzando contemporaneamente le funzioni `SHA256` e `RIPEMD160`. Questo processo in due fasi genera un'impronta digitale a 160 bit.