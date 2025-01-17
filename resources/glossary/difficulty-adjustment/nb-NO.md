---
term: VANSKELIGHETSJUSTERING

---
Vanskelighetsjustering er en periodisk prosess som omdefinerer vanskelighetsmålet for proof of work-mekanismen (utvinning) på Bitcoin. Denne hendelsen skjer hver 2016-blokk (omtrent annenhver uke). Den tjener til å øke eller redusere vanskelighetsfaktoren (også kalt vanskelighetsmålet), avhengig av hvor raskt de siste 2016-blokkene ble funnet. Justeringen har som mål å opprettholde en stabil og forutsigbar blokkproduksjonsrate, med en frekvens på én blokk hvert 10. minutt, til tross for variasjoner i utvinnernes datakraft. Endringen i vanskelighetsgrad under justeringen er begrenset til en faktor på 4. Formelen som nodene bruker for å beregne det nye målet, er som følger:

$$N = A \cdot \left(\frac{T}{1,209,600}\right)$$$

&nbsp;

Hvor?


- $N$: Det nye målet;
- $A$: Det gamle målet for de siste 2016-blokkene;
- $T$: Den totale faktiske tiden for de siste 2016 blokkene i sekunder;
- $1,209,600$: Måltiden i sekunder for å produsere 2016 blokker med 10 minutters intervall mellom hver.

> ► * På fransk brukes begrepet "reciblage" noen ganger også om justering. På engelsk kalles det "Difficulty Adjustment"