---
term: P2SH-P2WPKH

---
P2SH-P2WPKH stands for *Pay to Script Hash - Pay to Witness Public Key Hash*. It is a standard script model used to establish spending conditions on a UTXO, also known as "Nested SegWit".

P2SH-P2WPKH was introduced with the implementation of SegWit in August 2017. This script is a P2WPKH wrapped within a P2SH. It locks bitcoins based on the hash of a public key. The difference from the classic P2WPKH is that the script is wrapped in the `redeemScript` of a classic P2SH.

This script was created at the launch of SegWit to facilitate its adoption. It allows the use of this new standard, even with services or wallets not yet natively compatible with SegWit. It's a kind of transition script towards the new standard. Today, it is therefore no longer very relevant to use these types of wrapped SegWit scripts, since most wallets have implemented native SegWit. P2SH-P2WPKH addresses are written using `Base58Check` encoding and always start with `3`, like any P2SH address.

> ► *`P2SH-P2WPKH` is also sometimes called `P2WPKH-nested-in-P2SH`.*