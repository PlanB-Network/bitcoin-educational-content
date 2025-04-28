---
term: Pedersen commitment
---

Pedersen commitment on krüptograafilise Commitment tüüp, millel on omadus olla homomorfne liitmisoperatsiooni suhtes. See tähendab, et kahe kohustuse summat on võimalik kinnitada ilma üksikuid väärtusi avaldamata.


Formaalselt, kui :


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


siis :


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


See omadus on kasulik näiteks selleks, et varjata krüptovaluutasüsteemides, näiteks RGB, vahetatud žetoonide summasid, kuid samas on võimalik kontrollida nende kogusummasid.