---
term: OP_CHECKSIGVERIFY (0XAD)

---
Esegue la stessa operazione di `OP_CHECKSIG`, ma se la verifica della firma fallisce, lo script si arresta immediatamente con un errore e la transazione non è quindi valida. Se la verifica ha successo, lo script continua senza inserire il valore `1` (true) nello stack. In sintesi, `OP_CHECKSIGVERIFY` esegue l'operazione `OP_CHECKSIG` seguita da `OP_VERIFY`. Questo opcode è stato modificato in Tapscript per verificare le firme Schnorr.