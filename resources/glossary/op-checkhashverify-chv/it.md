---
term: OP_CHECKHASHVERIFY (CHV)

---
Un nuovo opcode proposto nel 2012 in BIP17 da Luke Dashjr che offrirebbe le stesse funzionalità di `OP_EVAL` o P2SH. Era inteso per eseguire l'hash alla fine di `scriptSig`, confrontare il risultato con la parte superiore dello stack e rendere la transazione non valida se i due hash non corrispondevano. Questo opcode non è mai stato implementato.