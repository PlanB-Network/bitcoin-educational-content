---
termine: OP_CHECKSIGADD (0XBA)
---

Estrae i tre valori superiori dallo stack: una `chiave pubblica`, un `CScriptNum` `n`, e una `firma`. Se la firma non è il vettore vuoto e non è valida, lo script termina con un errore. Se la firma è valida o è il vettore vuoto (`OP_0`), vengono presentati due scenari:
* Se la firma è il vettore vuoto: un `CScriptNum` con il valore di `n` viene inserito nello stack, e l'esecuzione continua;
* Se la firma non è il vettore vuoto e rimane valida: un `CScriptNum` con il valore di `n + 1` viene inserito nello stack, e l'esecuzione continua.
Per semplificare, `OP_CHECKSIGADD` esegue un'operazione simile a `OP_CHECKSIG`, ma invece di inserire vero o falso nello stack, aggiunge `1` al secondo valore in cima allo stack se la firma è valida, o lascia invariato questo valore se la firma rappresenta il vettore vuoto. `OP_CHECKSIGADD` consente la creazione delle stesse politiche di multisignature in Tapscript come con `OP_CHECKMULTISIG` e `OP_CHECKMULTISIGVERIFY` ma in modo verificabile in batch, il che significa che rimuove il processo di ricerca nella verifica di un multisig tradizionale e quindi accelera la verifica riducendo il carico operativo sui CPU dei nodi. Questo opcode è stato aggiunto in Tapscript esclusivamente per le esigenze di Taproot.