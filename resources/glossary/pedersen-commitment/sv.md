---
term: Pedersen-åtagande
definition: Homomorfiskt kryptografiskt åtagande som möjliggör verifiering av summor utan att avslöja värden.
---

En Pedersen commitment är en typ av kryptografisk Commitment med egenskapen att den är homomorf mot additionsoperationen. Detta innebär att det är möjligt att validera summan av två åtaganden utan att avslöja de enskilda värdena.


Formellt sett, om :


$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$


sedan :


$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$


Denna egenskap är till exempel användbar för att dölja mängden tokens som byts ut i kryptovalutasystem, som RGB, samtidigt som totalsummorna kan verifieras.