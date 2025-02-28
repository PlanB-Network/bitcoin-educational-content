---
term: ELLIPTIC CURVE

---
In the context of cryptography, an elliptic curve is an algebraic curve defined by an equation of the form $y^2 = x^3 + ax + b$. These curves are used in Elliptic Curve Cryptography (ECC), which is a method of public key cryptography that enables the creation of encryption algorithms, digital signatures, and key exchange mechanisms. In the context of Bitcoin, the ECDSA (*Elliptic Curve Digital Signature Algorithm*) or the Schnorr protocol are utilized with the `secp256k1` curve. This curve was selected for its performance and security properties. These algorithms are employed to generate public keys from private keys, as well as to sign transactions, thereby unlocking bitcoins.