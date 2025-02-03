---
term: P2SH-P2WSH

---
P2SH-P2WSH stands for *Pay to Script Hash - Pay to Witness Script Hash*. It is a standard script model used to establish spending conditions on a UTXO, also known as "Nested SegWit".

P2SH-P2WSH was introduced with the implementation of SegWit in August 2017. This script describes a P2WSH wrapped within a P2SH. It locks bitcoins based on the hash of a script. The difference from a classic P2WSH is that the script is wrapped in the `redeemScript` of a classic P2SH.

This script was created at the launch of SegWit to facilitate its adoption. It allows the use of this new standard, even with services or wallets not yet natively compatible with SegWit. Today, it is therefore no longer very relevant to use these types of wrapped SegWit scripts, since most wallets have implemented native SegWit. P2SH-P2WSH addresses are written using `Base58Check` encoding and always start with `3`, like any P2SH address.