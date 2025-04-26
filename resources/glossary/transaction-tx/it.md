---
term: TRANSAZIONE (TX)

---
Nel contesto di Bitcoin, una transazione (abbreviata in "TX") è un'operazione registrata sulla blockchain che trasferisce la proprietà dei bitcoin da uno o più input a uno o più output. Ogni transazione consuma come input gli Unspent Transaction Outputs (UTXO), che sono output di transazioni precedenti, e crea nuovi UTXO come output, che possono essere utilizzati come input in transazioni future.

Ogni input include un riferimento a un output esistente insieme a uno script di firma (`scriptSig`) che soddisfa le condizioni di spesa (`scriptPubKey`) stabilite dall'output a cui fa riferimento. Questo è ciò che permette di sbloccare i bitcoin. Le uscite definiscono nuove condizioni di spesa (`scriptPubKey`) per i bitcoin trasferiti, spesso sotto forma di una chiave pubblica o di un indirizzo a cui i bitcoin sono ora associati.