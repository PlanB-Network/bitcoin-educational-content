---
term: Pedersen commitment
---

Pedersen commitment 是一种加密 Commitment，具有与加法运算同构的特性。这意味着，可以在不泄露单个值的情况下验证两个承诺的总和。


形式上，如果 ：


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


然后


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


举例来说，这一特性在隐藏加密货币系统（如 RGB）中交换的代币数量方面非常有用，同时还能验证总量。