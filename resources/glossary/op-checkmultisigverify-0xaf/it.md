---
term: OP_CHECKMULTISIGVERIFY (0XAF)

---
Combina un `OP_CHECKMULTISIG` e un `OP_VERIFY`. Prende più firme e chiavi pubbliche per verificare che `M` su `N` firme siano valide, proprio come fa `OP_CHECKMULTISIG`. Poi, come `OP_VERIFY`, se la verifica fallisce, lo script si ferma immediatamente con un errore. Se la verifica ha successo, lo script continua senza inserire alcun valore nello stack. Questo opcode è stato rimosso in Tapscript.