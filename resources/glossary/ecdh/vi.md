---
term: ECDH

---
Method of cryptographic key exchange based on the principles of the Diffie-Hellman key exchange, but using elliptical curves to provide a high level of security with smaller key sizes. This protocol allows two parties to generate a shared secret using their public and private key pairs, without ever having to exchange the private keys themselves. The shared secret can then be used to encrypt subsequent communications. This algorithm is sometimes found in proposals to improve Bitcoin, notably BIP47 or BIP352 for deriving fresh receiving addresses from a static identifier.