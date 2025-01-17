---
term: P2WSH

---
P2WSH stands for *Pay to Witness Script Hash*. It is a standard script model used to establish spending conditions on a UTXO. P2WSH was introduced with the implementation of SegWit in August 2017.

This script is similar to P2SH (*Pay to Public Script Hash*), as it also locks bitcoins based on the hash of a script. The difference lies in how signatures and scripts are included in the transaction. To spend the bitcoins on this type of script, the recipient must provide the original script, called `witnessScript` (equivalent to `redeemScript`), along with the required signatures. This mechanism allows for the implementation of more sophisticated spending conditions, such as multisigs.

In the context of P2WSH, the signature script information (the `scriptWitness`, equivalent to `scriptSig`) is moved from the traditional transaction structure to a separate section called `Witness`. This move is a feature of the SegWit (*Segregated Witness*) update that helps to prevent signature malleability. P2WSH transactions are generally less expensive in terms of fees compared to Legacy transactions, as the part in the witness costs less.

P2WSH addresses are written using `Bech32` encoding with a checksum in the form of BCH code. These addresses always start with `bc1q`. P2WSH is a version 0 SegWit output.