---
term: Pedersen commitment
---

Een Pedersen commitment is een type cryptografische Commitment met de eigenschap homomorf te zijn voor de opteloperatie. Dit betekent dat het mogelijk is om de som van twee toezeggingen te valideren zonder de individuele waarden te onthullen.


Formeel, als :


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


dan :


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


Deze eigenschap is bijvoorbeeld handig om de hoeveelheden uitgewisselde tokens te verbergen in cryptocurrency systemen, zoals RGB, terwijl de totalen nog steeds kunnen worden geverifieerd.