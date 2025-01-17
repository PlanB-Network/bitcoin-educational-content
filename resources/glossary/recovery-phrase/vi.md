---
term: RECOVERY PHRASE

---
A recovery phrase, also sometimes called a mnemonic, seed phrase, or secret phrase, is a sequence usually composed of 12 or 24 words, which is generated in a pseudo-random manner from a source of entropy. The pseudo-random sequence is always completed with a checksum. The mnemonic phrase, along with an optional passphrase, is used to deterministically derive all the keys associated with an HD (Hierarchical Deterministic) wallet. This means that from this phrase, it is possible to deterministically generate and recreate all the private and public keys of the Bitcoin wallet, and consequently access the funds associated with it. The purpose of the recovery phrase is to provide a means of backup and recovery of bitcoins that is both secure and easy to use.

It is important to keep this phrase in a safe and secure location, as anyone in possession of the mnemonic would have access to the funds of the corresponding wallet. If used in the context of a traditional wallet, and without an optional passphrase, it often constitutes a SPOF (Single Point Of Failure). The recovery phrase is thus an encoding of the pseudo-random sequence and the checksum into everyday words to facilitate its notation and readability by humans. It is constructed according to the BIP39 standard, which defines and orders a list of 2048 words used for this encoding.

> ► *The list of 2048 words from BIP39 is available in several languages, however, it is advised to use only the English version, as it is the version most widely supported by wallet software.*