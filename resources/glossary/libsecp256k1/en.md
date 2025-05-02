---
term: LIBSECP256K1
---

High-performance, high-security C library for digital signatures and other cryptographic primitives on the `secp256k1` elliptic curve. Since this curve has never been widely used outside Bitcoin (unlike the often-preferred `secp256r1` curve), this library aims to be the most comprehensive reference for its use. The development of libsecp256k1 was primarily geared towards the needs of Bitcoin, and features intended for other applications may be less tested or verified. Appropriate use of this library requires careful attention, to ensure that it is suitable for the specific purposes of applications other than Bitcoin.

The libsecp256k1 library offers a variety of features, including:


- ECDSA-secp256k1 signature and verification, and cryptographic key generation ;
- Additive and multiplicative operations on secret and public keys ;
- Serialization and analysis of secret keys, public keys and signatures ;
- Constant-time public key signing and generation with constant memory access;
- And a host of other cryptographic primitives.