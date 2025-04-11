---
term: P2WSH

---
P2WSH sta per *Pay to Witness Script Hash*. Si tratta di un modello di script standard utilizzato per stabilire le condizioni di spesa su un UTXO. P2WSH è stato introdotto con l'implementazione di SegWit nell'agosto 2017.

Questo script è simile a P2SH (*Pay to Public Script Hash*), poiché anch'esso blocca i bitcoin in base all'hash di uno script. La differenza sta nel modo in cui le firme e gli script sono inclusi nella transazione. Per spendere i bitcoin su questo tipo di script, il destinatario deve fornire lo script originale, chiamato `witnessScript` (equivalente a `redeemScript`), insieme alle firme richieste. Questo meccanismo consente l'implementazione di condizioni di spesa più sofisticate, come i multisig.

Nel contesto di P2WSH, le informazioni sullo script della firma (lo `scriptWitness`, equivalente a `scriptSig`) vengono spostate dalla struttura tradizionale della transazione a una sezione separata chiamata `Witness`. Questo spostamento è una caratteristica dell'aggiornamento SegWit (*Segregated Witness*) che aiuta a prevenire la malleabilità della firma. Le transazioni P2WSH sono generalmente meno costose in termini di commissioni rispetto alle transazioni Legacy, poiché la parte del testimone costa meno.

Gli indirizzi P2WSH sono scritti utilizzando la codifica `Bech32` con un checksum sotto forma di codice BCH. Questi indirizzi iniziano sempre con `bc1q`. P2WSH è un'uscita SegWit versione 0.