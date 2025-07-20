---
term: Commitment
---

A Commitment (in the cryptographic sense) is a mathematical object, denoted $C$, derived deterministically from an operation on structured data $m$ (the message) and a random value $r$. We write :

$$
C = \text{commit}(m, r)
$$

This mechanism comprises two main operations:


- Commit: we apply a cryptographic function to a message $m$ and a random $r$ to produce $C$ ;
- Verify: we use $C$, the $m$ message and the $r$ value to check that this Commitment is correct. The function returns `True` or `False`.

A Commitment must respect two properties:


- Binding: it must be impossible to find two different messages producing the same $C$ :

$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$

Such as :

$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$


- Hiding: knowledge of $C$ must not reveal the contents of $m$.

In the case of the RGB protocol, a Commitment is included in a Bitcoin transaction in order to prove the existence of a certain piece of information at a given time, without disclosing the information itself.