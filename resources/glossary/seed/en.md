---
term: GRAIN
---

In the specific context of a Bitcoin hierarchical deterministic portfolio, a seed is a 512-bit piece of information derived from a random event. It is used to deterministically and hierarchically generate a set of private keys, and their corresponding public keys, for a Bitcoin portfolio. The seed is often confused with the recovery phrase itself. But it's not the same thing. The seed is obtained by applying the `PBKDF2` function to the mnemonic phrase and any passphrase.

The seed was invented with BIP32, which defined the foundations of the hierarchical deterministic portfolio. In this standard, the seed measured 128 bits. This allows all the keys in a portfolio to be derived from a single piece of information, unlike JBOK (*Just a Bunch Of Keys*) portfolios, which require new backups for every key generated. BIP39 then proposed an encoding of this seed, to simplify its reading by humans. This encoding takes the form of a phrase, generally referred to as a mnemonic phrase or recovery phrase. This standard avoids errors when saving the seed, thanks in particular to the use of a checksum.

Outside the context of Bitcoin, in cryptography in general, a seed is an initial value used to generate cryptographic keys, or more broadly, any type of data produced by a pseudo-random number generator. This initial value must be random and unpredictable to guarantee the security of the cryptographic system. Indeed, seed introduces entropy into the system, but the generation process that follows is deterministic.

> ► *In common parlance, the majority of bitcoiners refer to the mnemonic phrase when they speak of the "seed", and not to the intermediate derivation state that lies between the mnemonic phrase and the master key.*