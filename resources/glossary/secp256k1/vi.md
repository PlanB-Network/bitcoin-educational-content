---
term: SECP256K1

---
Name given to a specific elliptical curve used in the Bitcoin protocol for the implementation of the ECDSA (*Elliptic Curve Digital Signature Algorithm*) and Schnorr digital signature algorithms. The `secp256k1` curve was chosen by the inventor of Bitcoin, Satoshi Nakamoto. It has some interesting properties, notably performance benefits.

The use of `secp256k1` in Bitcoin means that each private key (a random 256-bit number) is mapped to a corresponding public key through addition and doubling of the private key's point by the `secp256k1` curve's generator point. This operation is easy to perform in one direction but practically impossible to reverse, which forms the basis of the security of digital signatures on Bitcoin.

The `secp256k1` curve is specified by the elliptical curve equation $y^2 = x^3 + 7$, meaning it has coefficients $a$ equal to $0$ and $b$ equal to $7$ in the general form of an elliptical curve equation $y^2 = x^3 + ax + b$. `secp256k1` is defined over a finite field whose order is a very large prime number, specifically $p = 2^{256} - 2^{32} - 977$. The curve also has a group order, which is the number of distinct points on the curve, a predefined generator point (or point $G$), which is used in cryptographic operations to generate key pairs, and a cofactor equal to $1$.

> ► *“SEC” stands for “Standards for Efficient Cryptography”. “P256” indicates that the curve is defined over a field $\mathbb{Z}_p$ where $p$ is a 256-bit prime number. “K” refers to the name of its inventor, Neal Koblitz. Finally, “1” indicates that this is the first version of this curve.*