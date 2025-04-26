---
term: PBKDF2

---
`PBKDF2` stands for *Password-Based Key Derivation Function 2*. It is a method for creating cryptographic keys from a password using a derivation function. It takes as input a password, a cryptographic salt, and iteratively applies a predetermined function (often a hash function like `SHA256` or an `HMAC`) to these data. This process is repeated many times to generate a cryptographic key.

In the context of Bitcoin, `PBKDF2` is used in conjunction with the `HMAC-SHA512` function to create the seed of a deterministic and hierarchical wallet (seed) from a recovery phrase of 12 or 24 words. The cryptographic salt used in this case is the BIP39 passphrase, and the number of iterations is `2048`.