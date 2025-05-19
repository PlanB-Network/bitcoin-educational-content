---
term: Pedersen commitment
---

A Pedersen commitment is a type of cryptographic commitment with the property of being homomorphic to the addition operation. This means that it is possible to validate the sum of two commitments without revealing the individual values.

Formally, if :

$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$

then :

$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$

This property becomes useful, for example, to conceal the amounts of tokens exchanged in cryptocurrency systems, such as RGB, while still being able to verify the totals.