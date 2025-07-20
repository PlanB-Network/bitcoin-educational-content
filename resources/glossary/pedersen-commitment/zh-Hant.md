---
term: Pedersen commitment
---

Pedersen commitment 是加密 Commitment 的一種，具有與加法運算同態的特性。這表示可以在不透露個別值的情況下驗證兩個承諾的總和。


形式上，如果 ：


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


然後


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


舉例來說，這個屬性在隱藏加密貨幣系統（例如 RGB）中交換的代幣數量，同時仍能驗證總數，就變得非常有用。