---
term: Pedersen commitment
---

Pedersen commitment je tip kriptografskog Commitment sa svojstvom da je homomorfan prema operaciji sabiranja. To znači da je moguće validirati zbir dve obaveze bez otkrivanja pojedinačnih vrednosti.


Formalno, ako :


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


onda :


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


Ovo svojstvo postaje korisno, na primer, za prikrivanje iznosa tokena razmenjenih u kriptovalutnim sistemima, kao što je RGB, dok je i dalje moguće verifikovati ukupne iznose.