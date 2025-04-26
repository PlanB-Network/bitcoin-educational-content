---
term: P2MS

---
P2MS stands for *Pay to Multisig*, which translates to "pay to multiple signatures". It is a standard script model used to establish spending conditions on a UTXO. It allows for the locking of bitcoins with multiple public keys. To spend these bitcoins, a signature with a predefined number of associated private keys is required. For example, a `P2MS 2/3` involves `3` public keys with `3` associated secret private keys. To spend the bitcoins locked with this P2MS script, a signature with at least `2` out of the `3` private keys is needed. This is a threshold security system.

This script was invented in 2011 by Gavin Andresen when he took over the maintenance of the main Bitcoin client. Today, P2MS is only marginally used by some applications. The vast majority of modern multisignatures use other scripts like P2SH or P2WSH. Compared to these, P2MS is extremely trivial. The public keys it consists of are revealed upon receiving the transaction. Using a P2MS is also more expensive than other multisignature scripts.

> ► *P2MS are often called "bare-multisig", which could be translated as "naked multisignature" or "raw multisignature". At the beginning of 2023, P2MS scripts were at the center of a controversy due to their misused within the Stamps protocol. Their impact on the UTXO set was notably pointed out.*