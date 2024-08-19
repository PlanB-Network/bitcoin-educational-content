---
termine: SWEEP TRANSACTION
---

Modello di transazione o pattern utilizzato nell'analisi delle catene per determinare la natura della transazione. Questo modello è caratterizzato dal consumo di un singolo UTXO come input e dalla produzione di un singolo UTXO come output. L'interpretazione di questo modello è che ci troviamo di fronte a un auto-trasferimento. L'utente ha trasferito i propri bitcoin a se stesso, su un altro indirizzo di sua proprietà. Poiché non c'è cambio nella transazione, è molto improbabile che ci troviamo di fronte a un pagamento. Infatti, quando viene effettuato un pagamento, è quasi impossibile per il pagante avere un UTXO che corrisponda esattamente all'importo richiesto dal venditore, oltre alle commissioni di transazione. Generalmente, il pagante è quindi costretto a produrre un output di resto. Sappiamo quindi che l'utente osservato è probabilmente ancora in possesso di questo UTXO. Nel contesto di un'analisi della catena, se sappiamo che l'UTXO utilizzato come input nella transazione appartiene ad Alice, possiamo assumere che l'UTXO in output appartenga anche a lei.

![](../../dictionnaire/assets/6.png)

> ► *In francese, "sweep transaction" potrebbe essere tradotto come "transaction de balayage".*