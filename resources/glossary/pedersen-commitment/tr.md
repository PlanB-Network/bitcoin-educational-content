---
term: Pedersen taahhüdü
definition: Değerleri açıklamadan toplamların doğrulanmasına izin veren homomorfik kriptografik taahhüt.
---

Bir Pedersen commitment, toplama işlemine homomorfik olma özelliğine sahip bir kriptografik Commitment türüdür. Bu, iki taahhüdün toplamını tek tek değerleri ortaya çıkarmadan doğrulamanın mümkün olduğu anlamına gelir.


Resmi olarak, eğer :


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


sonra:


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


Bu özellik, örneğin RGB gibi kripto para sistemlerinde takas edilen token miktarlarını gizlemek ve yine de toplamları doğrulayabilmek için kullanışlı hale gelir.