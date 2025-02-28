---
term: BIP17

---
Propuesta de Luke Dashjr que competía con BIP12 y BIP16. BIP17 introdujo un nuevo opcode, `OP_CHECKHASHVERIFY`, diseñado para permitir la verificación de un script presente en el `scriptSig` contra su hash presente en el `scriptPubKey` antes de desbloquear los fondos. La BIP16 (P2SH) fue finalmente preferida a la BIP17 (CHV) tras un periodo de intensos debates.