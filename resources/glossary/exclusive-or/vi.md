---
term: EXCLUSIVE OR

---
A fundamental function of Boolean logic. The "Exclusive Or" or XOR ("*Exclusive or*") takes two Boolean operands, each being true or false, and produces a true output only when the two operands differ. In other words, the output of the `XOR` operation is true if exactly one (but not both) of the operands is true. For example, the `XOR` operation between `1` and `0` will result in `1`. We note: $1 \oplus 0 = 1$. Similarly, the `XOR` operation can be performed on longer sequences of bits. For example, $10110 \oplus 01110 = 11000$. Each bit of the sequence is compared to its counterpart, and the `XOR` operation is applied. Here is the truth table for the `XOR` operation:

<div align="center">

| $A$ | $B$ | $A \oplus B$ |

|:---:|:---:|:------------:|

| $0$ | $0$ |      $0$     |

| $0$ | $1$ |      $1$     |

| $1$ | $0$ |      $1$     |

| $1$ | $1$ |      $0$     |

</div>

The `XOR` operation is used in many areas of computer science, especially in cryptography, for its interesting attributes such as:


- Its commutativity: the order of the operands does not affect the result. For two given variables $D$ and $E$: $D \oplus E = E \oplus D$;
- Its associativity: the grouping of operands does not affect the result. For three given variables $A$, $B$, and $C$: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$;
- It has a neutral element `0`: an operand xored with 0 will always be equal to the operand. For a given variable $A$: $A \oplus 0 = A$;
- Each element is its own inverse. For a given variable $A$: $A \oplus A = 0$.

In the context of Bitcoin, the `XOR` operation is obviously used in many places. For example, `XOR` is massively used in the `SHA256` function, which is widely used in the Bitcoin protocol. Some protocols like Coldcard's *SeedXOR* also use this primitive for other applications. It is also found in BIP47 for encrypting the reusable payment code during its transmission.

In the broader field of cryptography, `XOR` can be used as is as a symmetric encryption algorithm. This algorithm is called the "One-Time Pad" or the "Vernam Cipher," named after its inventor. Although impractical due to the length of the key, this algorithm is one of the only encryption algorithms recognized as unconditionally secure.