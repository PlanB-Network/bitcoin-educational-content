---
term: SEED (BITCOIN)
---

In the context of Bitcoin, a seed is a 512-bit value used to derive all the private and public keys associated with an HD (Hierarchical Deterministic) wallet. Technically, the seed is a different value from the recovery phrase (or mnemonic). The phrase, which is typically composed of 12 or 24 words, is generated in a pseudo-random manner from a source of entropy and completed by a checksum. This phrase facilitates human backup by providing a textual representation of the value at the base of the wallet.

To obtain the actual seed, the recovery phrase, possibly accompanied by an optional passphrase, is processed through the PBKDF2 algorithm (*Password-Based Key Derivation Function 2*). The result of this calculation is a 512-bit seed. It is this seed that is used to deterministically generate the master key, and then the entire set of keys for the HD wallet, in accordance with BIP32.

![](../../dictionnaire/assets/31.webp)

> ► *However, in common language, the majority of bitcoiners refer to the mnemonic phrase when they talk about the "seed," and not to the intermediate state of derivation that lies between the mnemonic phrase and the master key.*