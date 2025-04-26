---
term: WITNESSSCRIPT

---
A script that specifies the conditions under which bitcoins can be spent from P2WSH or P2SH-P2WSH UTXOs. Typically, `witnessScript` determines the conditions of a multisignature wallet under the SegWit standard. In these script standards, the `scriptPubKey` of the UTXO (the output) contains a hash of the `witnessScript`. To use this UTXO as an input in a new transaction, the holder must reveal the original `witnessScript`, in order to prove its match with the fingerprint in the `scriptPubKey`. The `witnessScript` must then be included in the transaction's `scriptWitness`, which also contains the elements necessary to validate the script, such as signatures. Therefore, the `witnessScript` is the equivalent for SegWit of the `redeemScript` in a P2SH transaction, with the difference that it is placed in the transaction's witness, and not in the `scriptSig`.

> ► *Caution, the `witnessScript` should not be confused with the `scriptWitness`. While the `witnessScript` defines the spending conditions of a P2WSH or P2SH-P2WSH UTXO and constitutes a script in its own right, the `scriptWitness` contains the witness data of any SegWit input.*