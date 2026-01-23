---
term: BIP0322
definition: New message signing standard compatible with all script types, replacing BIP137.
---

Proposes a new standard to replace BIP137 for signing messages with Bitcoin private keys and their associated addresses, in order to prove address ownership. These signatures are useful for various applications such as proof of funds, auditing, and other scenarios requiring  authentication of an address via its private key. 
Compared to BIP137, BIP322 extends the message‑signing standard beyond traditional addresses by using a script‑based approach. This allows wallet software to sign messages for any script that they could otherwise unlock to spend bitcoins.
The method involves signing the message by producing a signature for a virtual Bitcoin transaction. For traditional P2PKH addresses, BIP322 remains compatible with the traditional signature format.