---
term: NULLDUMMY

---
Regla de consenso introducida con BIP147 en la bifurcación suave SegWit que requiere que el elemento ficticio utilizado en los opcodes `OP_CHECKMULTISIG` y `OP_CHECKMULTISIGVERIFY` sea una matriz de bytes vacía (`OP_0`). Esta medida se implementó para eliminar un vector de maleabilidad prohibiendo cualquier valor distinto de `OP_0` para este elemento.