---
term: PEDERSEN COMMITMENT
---

Un Pedersen commitment est un type d'engagement cryptographique présentant la propriété d’être homomorphique vis-à-vis de l’opération d’addition. Cela signifie qu’il est possible de valider la somme de deux engagements sans dévoiler les valeurs individuelles.
Formellement, si :
$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$
alors :
$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$
Cette propriété devient utile, par exemple, pour dissimuler les montants de tokens échangés dans des système de cryptomonnaies, comme par exemple RGB, tout en pouvant vérifier les totaux.
