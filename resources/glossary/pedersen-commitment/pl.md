---
term: Pedersen commitment
---

Pedersen commitment jest rodzajem kryptograficznego Commitment z właściwością bycia homomorficznym do operacji dodawania. Oznacza to, że możliwe jest zweryfikowanie sumy dwóch zobowiązań bez ujawniania poszczególnych wartości.


Formalnie, jeśli :


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


następnie :


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


Właściwość ta staje się przydatna na przykład do ukrywania kwot tokenów wymienianych w systemach kryptowalutowych, takich jak RGB, przy jednoczesnym zachowaniu możliwości weryfikacji sum.