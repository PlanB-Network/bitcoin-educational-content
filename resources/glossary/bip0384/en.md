---
term: BIP0384
definition: combo() function for describing several types of scripts for the same public key in descriptors.
---

Introduces the `combo(KEY)` function for descriptors. This function describes a set of possible output scripts for a given public key, covering multiple script types simultaneously, including P2PK, P2PKH, P2WPKH, and P2SH‑P2WPKH. 
If the provided key is compressed, all four script types are tested; if it is uncompressed, only the two Legacy script types are tested. The goal is to simplify key representation in descriptors by providing a single method to generate various output script types from the same public key. BIP384 was implemented along with all other descriptor-related BIPs (except BIP386) in version 0.17 of Bitcoin Core.

