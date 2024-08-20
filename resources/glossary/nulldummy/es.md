---
term: NULLDUMMY
---

Regla de consenso introducida con BIP147 en el soft fork de SegWit que requiere que el elemento ficticio utilizado en los opcodes `OP_CHECKMULTISIG` y `OP_CHECKMULTISIGVERIFY` sea un arreglo de bytes vacío (`OP_0`). Esta medida se implementó para eliminar un vector de maleabilidad prohibiendo cualquier valor distinto de `OP_0` para este elemento.