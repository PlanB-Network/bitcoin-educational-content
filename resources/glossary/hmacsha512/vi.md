---
term: HMAC-SHA512

---
`HMAC-SHA512` stands for "Hash-based Message Authentication Code - Secure Hash Algorithm 512". It is a cryptographic algorithm used to verify the integrity and authenticity of messages exchanged between two parties. It combines the cryptographic hash function `SHA512` with a shared secret key to generate a unique Message Authentication Code (MAC) for each message.

In the context of Bitcoin, the natural use of `HMAC-SHA512` is slightly derived. This algorithm is used in the deterministic and hierarchical derivation process of the cryptographic key tree of a wallet. `HMAC-SHA512` is notably used to go from the seed to the master key, and then for each derivation from a parent pair to child pairs. This algorithm is also found within another derivation algorithm named `PBKDF2`, used to go from the recovery phrase and passphrase to the seed.