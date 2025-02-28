---
term: BIP380

---
A proposal for improvement that introduces a standard language for describing the collections of output scripts of HD Bitcoin wallets. This language is called "Output Script Descriptors." It aims to standardize the way to represent and manage output scripts, in order to facilitate the backup, export, and import of wallets. In addition to private data like the recovery phrase, the descriptors provide all the necessary information to retrieve the key pairs used in an HD wallet. BIP380 describes the general operation of descriptors, while BIP381, BIP382, BIP383, BIP384, BIP385, and BIP386 specify the expressions used. BIP380 was implemented along with all other descriptor-related BIPs (except BIP386) in version 0.17 of Bitcoin Core.