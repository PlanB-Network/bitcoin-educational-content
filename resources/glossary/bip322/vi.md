---
term: BIP322

---
Proposes a new standard to replace BIP137 for signing messages with Bitcoin private keys and their associated addresses, in order to prove ownership of an address. These signatures are useful for various applications such as proof of funds, auditing, and other uses requiring authentication of an address via its private key. Compared to BIP137, BIP322 extends the message signing standard beyond traditional addresses, using an approach based on scripts. It allows wallet software to sign a message for any script that they could unlock to spend bitcoins. To do this, the method involves signing a text by producing a signature for a virtual Bitcoin transaction. For traditional P2PKH addresses, BIP322 remains compatible with the traditional signature format.