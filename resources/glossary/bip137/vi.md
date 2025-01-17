---
term: BIP137

---
Proposes a standardized format for signing messages with Bitcoin private keys and their associated addresses, in order to prove ownership of an address. This BIP aims to resolve the ambiguity related to the different types of Bitcoin addresses (P2PKH, P2SH, P2WPKH...) when signing a message. It introduces a method for explicitly distinguishing these address formats through signatures. These signatures are useful for various applications such as proof of funds, auditing, and other uses requiring authentication of an address via its private key. BIP322 has since introduced a new signature format that allows for extending this standard and generalizing it for any type of script.