---
term: PUBLIC KEY

---
The public key is an element used in asymmetric cryptography. It is generated from a private key using an irreversible mathematical function. On Bitcoin, public keys are derived from their associated private key through the digital signature algorithms of elliptic curve ECDSA or Schnorr. Unlike the private key, the public key can be freely shared without compromising the security of the funds. Within the Bitcoin protocol, the public key serves as the basis for creating a Bitcoin address, which is then used to create spending conditions on a UTXO using a `scriptPubKey`. Public keys are often confused with the master key or with extended keys (xpub...). However, these elements are quite different.

> ► *In English, a public key is called "public key." This term is sometimes abbreviated as "pubkey," or "PK."*