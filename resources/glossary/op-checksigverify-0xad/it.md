---
termine: OP_CHECKSIGVERIFY (0XAD)
---

Esegue la stessa operazione di `OP_CHECKSIG`, ma se la verifica della firma fallisce, lo script si interrompe immediatamente con un errore e la transazione risulta quindi invalida. Se la verifica ha successo, lo script continua senza inserire un valore `1` (vero) nello stack. In sintesi, `OP_CHECKSIGVERIFY` esegue l'operazione `OP_CHECKSIG` seguita da `OP_VERIFY`. Questo opcode è stato modificato in Tapscript per verificare le firme Schnorr.