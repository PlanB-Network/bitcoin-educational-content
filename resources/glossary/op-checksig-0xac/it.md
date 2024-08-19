---
termine: OP_CHECKSIG (0XAC)
---

Verifica la validità di una firma rispetto a una data chiave pubblica. Prende i due elementi in cima allo stack: la firma e la chiave pubblica, e valuta se la firma è corretta per l'hash della transazione e la chiave pubblica specificata. Se la verifica ha successo, spinge il valore `1` (vero) nello stack, altrimenti `0` (falso). Questo opcode è stato modificato in Tapscript per verificare le firme Schnorr.