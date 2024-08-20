---
term: OP_CHECKHASHVERIFY (CHV)
---

Un nuevo opcode propuesto en 2012 en BIP17 por Luke Dashjr que ofrecería las mismas funcionalidades que `OP_EVAL` o P2SH. Su intención era hashear el final del `scriptSig`, comparar el resultado con el tope de la pila y declarar la transacción como inválida si los dos hashes no coincidían. Este opcode nunca fue implementado.