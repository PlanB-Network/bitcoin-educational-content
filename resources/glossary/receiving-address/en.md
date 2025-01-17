---
term: RECEIVING ADDRESS
---

Information used to receive bitcoins. An address is usually constructed by hashing a public key, using `SHA256` and `RIMPEMD160`, and adding metadata to this digest. The public keys used to construct a receiving address are part of the user's wallet and are therefore derived from their seed. For example, SegWit addresses are composed of the following information:
* An HRP to designate "bitcoin": `bc`;
* A separator: `1`;
* The version of SegWit used: `q` or `p`;
* The payload: the digest of the public key (or directly the public key in the case of Taproot);
* The checksum: a BCH code.

However, a receiving address can also represent something else depending on the script model used. For example, P2SH addresses are constructed using the script's hash. Taproot addresses, on the other hand, contain the tweaked public key directly without hashing it.

A receiving address can be represented in the form of an alphanumeric string or as a QR code. Each address can be used multiple times, but this is a highly discouraged practice. Indeed, in order to maintain a certain level of privacy, it is advised to use each Bitcoin address only once. A new address should be generated for every incoming payment to one's wallet. An address is encoded in `Bech32` for SegWit V0 addresses, in `Bech32m` for SegWit V1 addresses, and in `Base58check` for Legacy addresses. From a technical standpoint, receiving bitcoin translates to possessing the private key associated with a public key (and thus an address). When someone receives bitcoins, the sender updates the existing constraint on their spending so that only the recipient can now have this power.

![](../../dictionnaire/assets/23.webp)