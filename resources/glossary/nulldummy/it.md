---
term: NULLDUMMY

---
Regola di consenso introdotta con BIP147 nel soft fork SegWit che richiede che l'elemento fittizio utilizzato negli opcode `OP_CHECKMULTISIG` e `OP_CHECKMULTISIGVERIFY` sia un array di byte vuoto (`OP_0`). Questa misura è stata implementata per eliminare un vettore di malleabilità, vietando qualsiasi valore diverso da `OP_0` per questo elemento.