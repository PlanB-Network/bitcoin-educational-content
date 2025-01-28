---
term: PAGAMENTO A ROTONDO

---
Un'euristica interna per l'analisi della catena su Bitcoin che consente di formulare un'ipotesi sulla natura delle uscite di una transazione in base agli importi tondi. In genere, di fronte a uno schema di pagamento semplice (1 ingresso e 2 uscite), se una delle uscite spende un importo rotondo, allora rappresenta il pagamento. Per eliminazione, se un'uscita rappresenta il pagamento, l'altra rappresenta la variazione. Si può quindi interpretare che è probabile che l'utente che inserisce la transazione possieda ancora l'uscita identificata come il resto.

Va notato che questa euristica non è sempre applicabile, poiché la maggior parte dei pagamenti viene ancora effettuata in unità di valuta fiat. Infatti, quando un commerciante in Francia accetta bitcoin, in genere non mostra prezzi stabili in sats. Preferiscono piuttosto optare per una conversione tra il prezzo in euro e l'importo in bitcoin da pagare tramite il loro POS (come il server BTCPay, ad esempio). Pertanto, non dovrebbe esserci un numero tondo nell'output della transazione. Tuttavia, un analista potrebbe tentare di effettuare questa conversione tenendo conto del tasso di cambio in vigore al momento della trasmissione della transazione sulla rete. Se un giorno il bitcoin diventerà l'unità di conto preferita nei nostri scambi, questa euristica potrebbe diventare ancora più utile per le analisi.

![](../../dictionnaire/assets/11.webp)