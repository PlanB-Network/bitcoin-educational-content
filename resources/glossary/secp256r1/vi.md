---
term: SECP256R1

---
Name given to an elliptical curve defined by the NIST standard for public key cryptography. It uses a prime field of 256 bits and an elliptical curve equation $y^2 = x^3 + ax + b$ with the constants:

```text
a = -3
```

and

```text
b = 410583637251521421293261297800472684091144410159937255548542755610749322
77127
```

The curve `secp256r1` is widely used in many protocols, but it is not used in Bitcoin. Indeed, Satoshi Nakamoto opted for the curve `secp256k1`, which was then little known in 2009. The precise reason for this choice is unknown, but it may have been to minimize the risk of backdoors. The parameters of the $k1$ curve are indeed much simpler than those of the $r1$ curve, especially the constant $b$.

> ► *This curve is sometimes also named "P-256".*