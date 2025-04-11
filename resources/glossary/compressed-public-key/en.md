---
term: COMPRESSED PUBLIC KEY
---

A public key is used in scripts (either directly in the form of a public key or as an address) to receive and secure bitcoins. A raw public key is represented by a point on an elliptical curve, consisting of two coordinates (`x, y`) each of 256 bits. In raw format, a public key therefore measures 512 bits, not counting the additional byte to identify the format. A compressed public key, on the other hand, is a more compact form of public key representation. It uses only the `x` coordinate and a prefix (`02` or `03`) which indicates the parity of the `y` coordinate (even or odd).

If we simplify this to the field of real numbers, given the elliptical curve is symmetrical with respect to the x-axis, for any point $P$ (`x, y`) on the curve, there exists a point $P'$ (`x, -y`) that will also be on this same curve. This means that for each `x`, there are only two possible values of `y`, positive and negative. For example, for a given abscissa `x`, there would be two points $P1$ and $P2$ on the elliptical curve, sharing the same abscissa but with opposite ordinates:

![](../../dictionnaire/assets/29.webp)
To choose between the two potential points on the curve, a prefix specifying which `y` to choose is added to `x`. This method allows reducing the size of a public key from 520 bits to only 264 bits (8 bits of prefix + 256 bits for `x`). This representation is known as the compressed form of the public key.

However, in the context of elliptical curve cryptography, we use not the real numbers, but a finite field of order `p` (a prime number). In this context, the "sign" of `y` is determined by its parity, that is, whether `y` is even or odd. The prefix `0x02` then indicates an even `y`, while `0x03` indicates an odd `y`.

Consider the following example of a raw public key (a point on the elliptical curve) in hexadecimal:
```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

We can isolate the prefix, `x`, and `y`:
```plaintext
Prefix = 04
To determine the parity of `y`, we examine the last hexadecimal character of `y`:
```plaintext
Base 16 (hexadecimal): f
Base 10 (decimal): 15
y is odd
```

The prefix for the compressed public key will be `03`. The compressed public key in hexadecimal becomes:
```plaintext
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```