---
term: Transazione sweep

definition: Modello di transazione con un singolo input UTXO e un singolo output, caratteristico di un autotrasferimento.
---
Modello o modello di transazione utilizzato nell'analisi della catena per determinare la natura della transazione. Questo modello è caratterizzato dal consumo di un singolo UTXO come input e dalla produzione di un singolo UTXO come output. L'interpretazione di questo modello è che siamo in presenza di un auto-trasferimento. L'utente ha trasferito i propri bitcoin a se stesso, a un altro indirizzo di sua proprietà. Poiché la transazione non subisce variazioni, è molto improbabile che si tratti di un pagamento. Infatti, quando viene effettuato un pagamento, è quasi impossibile che il pagatore abbia un UTXO che corrisponda esattamente all'importo richiesto dal venditore, oltre alle spese di transazione. In genere, il pagatore è quindi costretto a produrre un output di modifica. Sappiamo quindi che l'utente osservato è probabilmente ancora in possesso di questo UTXO. Nel contesto di un'analisi a catena, se sappiamo che l'UTXO utilizzato come input nella transazione appartiene ad Alice, possiamo supporre che anche l'UTXO in output le appartenga.



