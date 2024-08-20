---
term: BIP17
---

Propuesta de Luke Dashjr que compitió con BIP12 y BIP16. BIP17 introdujo un nuevo opcode, `OP_CHECKHASHVERIFY`, diseñado para habilitar la verificación de un script presente en el `scriptSig` contra su hash presente en el `scriptPubKey` antes de desbloquear los fondos. BIP16 (P2SH) fue eventualmente preferido sobre BIP17 (CHV) tras un período de intensos debates.