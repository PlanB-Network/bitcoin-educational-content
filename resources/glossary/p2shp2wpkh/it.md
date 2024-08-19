P2SH-P2WPKH sta per *Pay to Script Hash - Pay to Witness Public Key Hash*. Si tratta di un modello di script standard utilizzato per stabilire le condizioni di spesa su un UTXO, noto anche come "Nested SegWit".

P2SH-P2WPKH è stato introdotto con l'implementazione di SegWit nell'agosto 2017. Questo script è un P2WPKH avvolto all'interno di un P2SH. Blocca i bitcoin basandosi sull'hash di una chiave pubblica. La differenza rispetto al classico P2WPKH è che lo script è avvolto nello `redeemScript` di un classico P2SH.

Questo script è stato creato al lancio di SegWit per facilitarne l'adozione. Permette l'uso di questo nuovo standard, anche con servizi o portafogli non ancora nativamente compatibili con SegWit. È una sorta di script di transizione verso il nuovo standard. Oggi, quindi, non è più molto rilevante utilizzare questi tipi di script SegWit avvolti, poiché la maggior parte dei portafogli ha implementato SegWit nativo. Gli indirizzi P2SH-P2WPKH sono scritti utilizzando la codifica `Base58Check` e iniziano sempre con `3`, come qualsiasi indirizzo P2SH.

> ► *`P2SH-P2WPKH` è talvolta chiamato anche `P2WPKH-nested-in-P2SH`.*