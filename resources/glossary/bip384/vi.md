---
term: BIP384

---
Introduces the `combo(KEY)` function for descriptors. This function describes a set of possible output scripts for a given public key. It thus covers multiple types of scripts at the same time, including P2PK, P2PKH, P2WPKH, and P2SH-P2WPKH. If the given key is compressed, all 4 types of scripts are tested, and if it is not, only the 2 Legacy script types are tested. The goal is to simplify the representation of keys in descriptors by providing a single method to generate different variants of output scripts based on the same public key. BIP384 was implemented along with all other descriptor-related BIPs (except BIP386) in version 0.17 of Bitcoin Core.