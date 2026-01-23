---
term: BIP0137
definition: Standardized format for signing messages with a Bitcoin private key to prove ownership of an address.
---

BIP137 proposes a standardized format for signing messages with Bitcoin private keys and their associated addresses, providing a way to prove ownership of an address.
It aims to resolve ambiguity between different Bitcoin address types (P2PKH, P2SH, P2WPKH, etc.) when signing messages by introducing a method to explicitly distinguish these formats through signatures.
These signatures are useful for various applications such as proof of funds, auditing, and other uses requiring authentication of an address via its private key. 
BIP322 has since introduced a new signature format, extending and generalizing this concept to support any type of script.