---
term: OP_CHECKSIGADD (0XBA)

---
Estrae i primi tre valori dallo stack: una `chiave pubblica`, un `CScriptNum` `n` e una `firma`. Se la firma non è il vettore vuoto e non è valida, lo script termina con un errore. Se la firma è valida o è il vettore vuoto (`OP_0`), si presentano due scenari:


- Se la firma è il vettore vuoto: un `CScriptNum` con il valore di `n` viene spinto sullo stack e l'esecuzione continua;
- Se la firma non è un vettore vuoto e rimane valida: un `CScriptNum` con il valore di `n + 1` viene spinto sulla pila e l'esecuzione continua.

Per semplificare, `OP_CHECKSIGADD` esegue un'operazione simile a quella di `OP_CHECKSIG`, ma invece di spingere true o false sullo stack, aggiunge `1` al secondo valore in cima allo stack se la firma è valida, oppure lascia questo valore invariato se la firma rappresenta un vettore vuoto. `OP_CHECKSIGADD` consente di creare in Tapscript le stesse politiche di firma multipla di `OP_CHECKMULTISIG` e `OP_CHECKMULTISIGVERIFY`, ma in modo verificabile in batch, ovvero eliminando il processo di ricerca nella verifica di una firma multipla tradizionale e quindi accelerando la verifica e riducendo il carico operativo sulle CPU dei nodi. Questo opcode è stato aggiunto in Tapscript esclusivamente per le esigenze di Taproot.