---
term: BIP0016
definition: Introduction of P2SH (Pay-to-Script-Hash) allowing payment to a script hash, simplifying the use of complex transactions like multisig.
---

BIP16 introduced the concept of *Pay-to-Script-Hash* (P2SH), which means to "pay to the script's hash". Initially proposed in 2012 and activated in 2013, BIP16 simplified the use of complex transaction scripts, such as multisignature transactions, by allowing users to pay to the hash of a redeem script rather than including the full script in the output. 
This innovation reduced the amount of data needed in the initial transaction, shifting the burden of providing the complete script to the party spending the bitcoins. It also improved privacy by revealing the actual script only when the bitcoins were spent, rather than at the time of receipt.
BIP16 is historically significant as one of the first major changes to the Bitcoin protocol after Satoshi Nakamoto's withdrawal in 2011. The proposal sparked intense debate that even led Gavin Andresen, Satoshi's successor as the lead maintainer, to temporarily step back from his role. Several competing proposals existed, and some came close to being adopted instead of BIP16.