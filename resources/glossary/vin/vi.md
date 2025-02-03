---
term: VIN

---
A specific element of a Bitcoin transaction that specifies the source of funds used to satisfy the outputs. Each `vin` refers to an unspent output (UTXO) from a previous transaction. A transaction can contain multiple inputs, each identified by a combination of the `txid` (the identifier of the original transaction) and the `vout` (the index of the output in that transaction).

Each `vin` includes the following information:


- `txid`: the identifier of the previous transaction containing the output used here as input;
- `vout`: the index of the output in the previous transaction;
- `scriptSig` or `scriptWitness`: an unlocking script that provides the necessary data to satisfy the conditions posed by the `scriptPubKey` of the previous transaction whose funds are being spent, usually by providing a cryptographic signature;
- `nSequence`: a specific field used to indicate how this input is time-locked, as well as other options like RBF.