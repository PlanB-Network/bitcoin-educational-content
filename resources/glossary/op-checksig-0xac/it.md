---
term: OP_CHECKSIG (0XAC)

---
Verifica la validità di una firma rispetto a una determinata chiave pubblica. Prende i primi due elementi della pila: la firma e la chiave pubblica, e valuta se la firma è corretta per l'hash della transazione e la chiave pubblica specificata. Se la verifica ha successo, spinge il valore `1` (true) sullo stack, altrimenti `0` (false). Questo opcode è stato modificato in Tapscript per verificare le firme Schnorr.