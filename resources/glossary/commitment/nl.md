---
term: Commitment
---

Een Commitment (in cryptografische zin) is een wiskundig object, aangeduid met $C$, dat deterministisch is afgeleid van een bewerking op gestructureerde gegevens $m$ (het bericht) en een willekeurige waarde $r$. We schrijven :


$$
C = \text{commit}(m, r)
$$


Dit mechanisme bestaat uit twee hoofdbewerkingen:




- Commit: we passen een cryptografische functie toe op een bericht $m$ en een willekeurige $r$ om $C$ te produceren;
- Verifiëren: we gebruiken $C$, het $m$ bericht en de $r$ waarde om te controleren of deze Commitment correct is. De functie retourneert `True` of `False`.


Een Commitment moet twee eigenschappen respecteren:




- Binding: het moet onmogelijk zijn om twee verschillende berichten te vinden die dezelfde $C$ produceren:


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


Zoals :


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- Verbergen: kennis van $C$ mag de inhoud van $m$ niet onthullen.


In het geval van het RGB protocol wordt een Commitment opgenomen in een Bitcoin transactie om het bestaan van een bepaald stuk informatie op een bepaald moment te bewijzen, zonder de informatie zelf vrij te geven.