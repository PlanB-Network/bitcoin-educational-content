---
term: P2SH-P2WSH

---
P2SH-P2WSH sta per *Pay to Script Hash - Pay to Witness Script Hash*. Si tratta di un modello di script standard utilizzato per stabilire le condizioni di spesa su un UTXO, noto anche come "Nested SegWit".

P2SH-P2WSH è stato introdotto con l'implementazione di SegWit nell'agosto 2017. Questo script descrive un P2WSH avvolto in un P2SH. Blocca i bitcoin in base all'hash di uno script. La differenza rispetto a un P2WSH classico è che lo script è avvolto nel `redeemScript` di un P2SH classico.

Questo script è stato creato al momento del lancio di SegWit per facilitarne l'adozione. Permette di utilizzare questo nuovo standard anche con servizi o portafogli non ancora nativamente compatibili con SegWit. Oggi, quindi, non è più molto rilevante utilizzare questi tipi di script SegWit avvolti, poiché la maggior parte dei portafogli ha implementato SegWit nativo. Gli indirizzi P2SH-P2WSH sono scritti utilizzando la codifica `Base58Check` e iniziano sempre con `3`, come qualsiasi indirizzo P2SH.