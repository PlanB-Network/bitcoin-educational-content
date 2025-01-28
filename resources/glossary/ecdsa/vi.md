---
term: ECDSA

---
Acronym for "Elliptic Curve Digital Signature Algorithm." It is a digital signature algorithm based on elliptic curve cryptography (ECC). It is a variant of the DSA (Digital Signature Algorithm). ECDSA utilizes the properties of elliptic curves to provide levels of security comparable to those of traditional public key algorithms, such as RSA, while using significantly smaller key sizes. ECDSA allows for the generation of key pairs (public and private keys) as well as the creation and verification of digital signatures.

In the context of Bitcoin, ECDSA is used to derive public keys from private keys. It is also used to sign transactions, in order to satisfy a script to unlock bitcoins and spend them. The elliptic curve used in Bitcoin's ECDSA is `secp256k1`, defined by the equation $y^2 = x^3 + 7$. This algorithm has been used since the inception of Bitcoin in 2009. Today, it shares its place with the Schnorr protocol, another digital signature algorithm introduced with Taproot in 2021.