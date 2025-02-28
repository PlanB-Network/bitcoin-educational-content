---
term: TWEAK (PUBLIC KEY)
---

In the field of cryptography, "tweaking" a public key involves modifying this key by using an additive value called the "tweak" so that it remains usable with the knowledge of the original private key and the tweak. Technically, a tweak is a scalar value that is added to the initial public key. If $P$ is the public key and $t$ is the tweak, the tweaked public key becomes:

$$
P' = P + tG
$$

Where $G$ is the generator of the elliptic curve used. This operation allows for obtaining a new public key derived from the original key while retaining certain cryptographic properties that make it usable. For example, this method is used for Taproot addresses (P2TR) to allow spending either by presenting a Schnorr signature in the traditional way or by fulfilling one of the conditions stated in a Merkle tree, also called "MAST".

![](../../dictionnaire/assets/26.webp)