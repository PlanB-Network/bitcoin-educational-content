---
term: P2WPKH

---
P2WPKH stands for *Pay to Witness Public Key Hash*. It is a standard script model used to establish spending conditions on a UTXO. P2WPKH was introduced with the implementation of SegWit in August 2017.

This script is similar to P2PKH (*Pay to Public Key Hash*), as it also locks bitcoins based on the hash of a public key, that is, a receiving address. The difference lies in how signatures and scripts are included in the transaction. In the case of P2WPKH, the signature script information (`scriptSig`) is moved from the traditional transaction structure to a separate section called `Witness`. This move is a feature of the SegWit (*Segregated Witness*) update that helps to prevent signature malleability. P2WPKH transactions are generally less expensive in terms of fees compared to Legacy transactions, as the part in the witness costs less.

P2WPKH addresses are written using `Bech32` encoding with a checksum in the form of BCH code. These addresses always start with `bc1q`. P2WPKH is a version 0 SegWit output.