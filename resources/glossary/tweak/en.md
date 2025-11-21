---
term: TWEAK
---

In cryptography, to "tweak" a public key is to modify it using an additive value called a "tweak", so that it remains usable with knowledge of both the original private key and the tweak. Technically, a tweak is a scalar value that is added to the original public key. If $P$ is the public key and $t$ is the tweak, the tweaked public key becomes :

$$
P' = P + tG
$$

Where $G$ is the generator of the elliptic curve used. This operation produces a new public key derived from the original, while retaining certain cryptographic properties that allow it to be used. For example, this method is used for Taproot (P2TR) addresses, to enable spending either by presenting a Schnorr signature in the traditional way, or by fulfilling one of the conditions set out in a Merkle tree, also known as a "MAST".