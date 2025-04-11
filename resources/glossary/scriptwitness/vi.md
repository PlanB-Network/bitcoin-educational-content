---
term: SCRIPTWITNESS

---
An element in SegWit transaction entries that contains the signatures and public keys necessary to unlock the bitcoins sent in the transaction. Similar to the `scriptSig` of Legacy transactions, the `scriptWitness` is, however, not placed in the same location. Indeed, it is this part, referred to as the "witness" (`*witness*` in English), which is moved to a separate database in order to solve the transaction malleability problem. Each SegWit input has its own `scriptWitness`, and all the `scriptWitness` elements together form the `Witness` field of the transaction.

> ► *Be careful not to confuse `scriptWitness` with `witnessScript`. While the `scriptWitness` contains the witness data for any SegWit input, the `witnessScript` defines the spending conditions of a P2WSH or P2SH-P2WSH UTXO and constitutes a script in its own right, similar to the `redeemScript` for a P2SH output.*