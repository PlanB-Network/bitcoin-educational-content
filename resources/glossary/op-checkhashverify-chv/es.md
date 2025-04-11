---
term: OP_CHECKHASHVERIFY (CHV)

---
Un nuevo opcode propuesto en 2012 en BIP17 por Luke Dashjr que ofrecería las mismas funcionalidades que `OP_EVAL` o P2SH. Pretendía hacer un hash del final del `scriptSig`, comparar el resultado con la parte superior de la pila y anular la transacción si los dos hashes no coincidían. Este opcode nunca fue implementado.