---
term: PRIVATE KEY

---
A private key is a fundamental element of asymmetric cryptography. It is a number (256 bits in the context of Bitcoin) that represents a cryptographic secret. This key is used to digitally sign transactions and prove the ownership of a Bitcoin public key (and by extension, a receiving address) by satisfying a `scriptPubKey`. Therefore, private keys allow spending bitcoins by unlocking the UTXOs associated with the corresponding public key. Private keys must be kept strictly confidential, as their disclosure could enable malicious third parties to take control of the associated funds.

In the Bitcoin system, the private key is linked to a public key through a digital signature algorithm using elliptical curves (ECDSA or Schnorr). The public key is derived from the private key, but the reverse is practically impossible to achieve due to the computational difficulty inherent in solving the underlying mathematical problem (the discrete logarithm problem). The public key is generally used to generate a Bitcoin address, which is used to lock bitcoins using a script. In cryptography, private keys are often random or pseudo-random numbers. In the specific context of Bitcoin deterministic and hierarchical wallets, private keys are deterministically derived from the seed. Private keys are frequently confused with the seed or with the recovery phrase (mnemonic). However, these elements are distinct.

> ► *In English, a private key is called "private key." This term is sometimes abbreviated as "privkey," or "PV."*