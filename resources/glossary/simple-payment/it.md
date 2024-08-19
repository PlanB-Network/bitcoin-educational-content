---
termine: SIMPLE PAYMENT
---

Modello di transazione (o schema) utilizzato nell'analisi delle catene caratterizzato dal consumo di uno o più UTXO negli input e dalla produzione di 2 UTXO negli output. Questo modello si presenterà quindi in questo modo:

![](../../dictionnaire/assets/5.png)

Questo semplice modello di pagamento indica che siamo probabilmente in presenza di una transazione di invio o pagamento. L'utente ha consumato il proprio UTXO negli input per soddisfare negli output un UTXO di pagamento e un UTXO di resto (resto restituito allo stesso utente). Sappiamo quindi che l'utente osservato probabilmente non è più in possesso di uno dei due UTXO negli output (quello di pagamento), ma è ancora in possesso dell'altro UTXO (quello di resto).