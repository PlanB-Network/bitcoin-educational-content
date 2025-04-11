---
term: REDEMSCRIPT

---
Uno script che definisce le condizioni specifiche che gli input devono soddisfare per sbloccare i fondi associati a un'uscita P2SH. In un UTXO P2SH, la `scriptPubKey` contiene l'hash del `redeemScript`. Quando una transazione desidera spendere questo UTXO come input, deve fornire il `redeemScript` chiaro che corrisponde all'hash contenuto nella `scriptPubKey`. Il `redeemScript` viene quindi fornito nel `scriptSig` dell'input, insieme ad altri elementi necessari a soddisfare le condizioni dello script, come firme o chiavi pubbliche. Questa struttura incapsulata assicura che i dettagli delle condizioni di spesa rimangano nascosti finché i bitcoin non vengono effettivamente spesi. È utilizzata in particolare per i portafogli Legacy P2SH a firma multipla.