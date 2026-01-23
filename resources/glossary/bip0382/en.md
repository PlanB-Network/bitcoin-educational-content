---
term: BIP0382
definition: wpkh() and wsh() functions for describing SegWit scripts in descriptors.
---

Introduces the functions `wpkh(KEY)` (Pay-to-Witness-PubKey-Hash) and `wsh(SCRIPT)` (Pay-to-Witness-Script-Hash) for descriptors. These functions standardize how SegWit script types are represented within descriptors. BIP382 was implemented along with all other descriptor-related BIPs (except BIP386) in version 0.17 of Bitcoin Core.

