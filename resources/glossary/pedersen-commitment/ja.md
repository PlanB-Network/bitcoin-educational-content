---
term: Pedersen commitment
---

Pedersen commitmentは暗号Commitmentの一種であり、加算演算に対して同型であるという性質を持つ。つまり、個々の値を明らかにすることなく、2つのコミットメントの和を検証することが可能である。


形式的には、もし：


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


その時


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


この性質は、例えば、RGBのような暗号通貨システムで交換されたトークンの量を隠しつつ、その合計を検証するのに役立つ。