---
termine: P2WPKH
---

P2WPKH sta per *Pay to Witness Public Key Hash* (Pagare al Hash della Chiave Pubblica del Testimone). È un modello di script standard utilizzato per stabilire le condizioni di spesa su un UTXO. P2WPKH è stato introdotto con l'implementazione di SegWit nell'agosto 2017.

Questo script è simile a P2PKH (*Pay to Public Key Hash*, Pagare al Hash della Chiave Pubblica), in quanto anch'esso blocca i bitcoin basandosi sul hash di una chiave pubblica, ovvero un indirizzo di ricezione. La differenza risiede nel modo in cui le firme e gli script sono inclusi nella transazione. Nel caso di P2WPKH, le informazioni dello script di firma (`scriptSig`) vengono spostate dalla struttura tradizionale della transazione a una sezione separata chiamata `Witness` (Testimone). Questo spostamento è una caratteristica dell'aggiornamento SegWit (*Segregated Witness*, Testimone Separato) che aiuta a prevenire la malleabilità delle firme. Le transazioni P2WPKH generalmente hanno costi inferiori in termini di commissioni rispetto alle transazioni Legacy, poiché la parte nel testimone costa meno.

Gli indirizzi P2WPKH sono scritti utilizzando la codifica `Bech32` con un checksum sotto forma di codice BCH. Questi indirizzi iniziano sempre con `bc1q`. P2WPKH è un output SegWit versione 0.