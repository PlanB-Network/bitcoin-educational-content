---
termine: OP_CHECKHASHVERIFY (CHV)
---

Un nuovo opcode proposto nel 2012 in BIP17 da Luke Dashjr che avrebbe offerto le stesse funzionalità di `OP_EVAL` o P2SH. Era inteso per eseguire l'hash della fine dello `scriptSig`, confrontare il risultato con la cima dello stack e rendere la transazione non valida se i due hash non corrispondevano. Questo opcode non è mai stato implementato.