---
term: DIFFIE-HELLMAN

---
Cryptographic method that allows two parties to generate a shared secret over an unsecured communication channel. This secret can then be used to encrypt communication between the two parties. Diffie-Hellman uses modular arithmetic so that, even if an attacker can observe the exchanges, they cannot deduce the shared secret without solving a difficult mathematical problem: the discrete logarithm. In Bitcoin, a variant of DH called ECDH that uses an elliptical curve is sometimes used, especially for static address protocols like Silent Payments or BIP47.