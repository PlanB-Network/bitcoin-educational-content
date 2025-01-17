---
term: P2WPKH

---
P2WPKH sta per *Pay to Witness Public Key Hash*. Si tratta di un modello di script standard utilizzato per stabilire le condizioni di spesa su un UTXO. P2WPKH è stato introdotto con l'implementazione di SegWit nell'agosto 2017.

Questo script è simile al P2PKH (*Pay to Public Key Hash*), in quanto anch'esso blocca i bitcoin in base all'hash di una chiave pubblica, ovvero un indirizzo di ricezione. La differenza sta nel modo in cui le firme e gli script sono inclusi nella transazione. Nel caso del P2WPKH, le informazioni relative allo script della firma (`scriptSig`) vengono spostate dalla struttura tradizionale della transazione a una sezione separata chiamata `Witness`. Questo spostamento è una caratteristica dell'aggiornamento SegWit (*Segregated Witness*) che aiuta a prevenire la malleabilità della firma. Le transazioni P2WPKH sono generalmente meno costose in termini di commissioni rispetto alle transazioni Legacy, poiché la parte del testimone costa meno.

Gli indirizzi P2WPKH sono scritti utilizzando la codifica `Bech32` con un checksum sotto forma di codice BCH. Questi indirizzi iniziano sempre con `bc1q`. P2WPKH è un'uscita SegWit versione 0.