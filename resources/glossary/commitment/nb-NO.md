---
term: Commitment
---

En Commitment (i kryptografisk forstand) er et matematisk objekt, betegnet $C$, som er avledet deterministisk fra en operasjon på strukturerte data $m$ (meldingen) og en tilfeldig verdi $r$. Vi skriver :


$$
C = \text{commit}(m, r)
$$


Denne mekanismen består av to hovedoperasjoner:




- Commit: Vi bruker en kryptografisk funksjon på en melding $m$ og en tilfeldig $r$ for å produsere $C$ ;
- Verify: Vi bruker $C$, $m$-meldingen og $r$-verdien til å kontrollere at denne Commitment er korrekt. Funksjonen returnerer `True` eller `False`.


En Commitment må respektere to egenskaper:




- Binding: Det må være umulig å finne to forskjellige meldinger som produserer samme $C$ :


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


Som for eksempel :


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- Skjult: Kunnskap om $C$ må ikke avsløre innholdet i $m$.


I RGB-protokollen inkluderes en Commitment i en Bitcoin-transaksjon for å bevise eksistensen av en viss informasjon på et gitt tidspunkt, uten å avsløre selve informasjonen.