---
term: SEED

---
Within the specific context of a hierarchical deterministic Bitcoin wallet, a seed is a 512-bit piece of information derived from randomness. It is used to deterministically and hierarchically generate a set of private keys, and their corresponding public keys, for a Bitcoin wallet. The seed is often confused with the recovery phrase itself. However, it is different information. The seed is obtained by applying the `PBKDF2` function to the mnemonic phrase and any potential passphrase.

The seed was invented with the introduction of BIP32, which defines the foundations of the hierarchical deterministic wallet. In this standard, the seed was 128 bits. This allows for the derivation of all the keys in a wallet from a single piece of information, unlike JBOK (*Just a Bunch Of Keys*) wallets, which require new backups for every generated key. BIP39 later introduced an encoding of this seed to simplify its readability by humans. This encoding is done in the form of a phrase, commonly referred to as a mnemonic phrase or recovery phrase. This standard helps to avoid errors in the backup of the seed, notably through the use of a checksum.

More generally, in cryptography, a seed is a piece of random data used as a starting point to generate cryptographic keys, encryptions, or pseudo-random sequences. The quality and security of many cryptographic processes depend on the randomness and confidentiality of the seed.

> ► *The English translation of "graine" is "seed". In French, many directly use the English word to refer to the seed.*