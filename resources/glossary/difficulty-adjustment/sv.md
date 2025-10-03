---
term: SVÅRIGHETSJUSTERING
---

Svårighetsjustering är en periodisk process som omdefinierar svårighetsmålet för Proof of Work-mekanismen (Mining) på Bitcoin. Denna händelse inträffar vart 2016:e block (ungefär varannan vecka). Den används för att öka eller minska svårighetsfaktorn (även kallat svårighetsmålet), beroende på hur snabbt de senaste 2016 blocken hittades. Justeringen syftar till att upprätthålla en stabil och förutsägbar blockproduktionshastighet, med en frekvens på ett block var 10:e minut, trots variationer i den beräkningskraft som används av miners. Förändringen i svårighetsgrad under justeringen är begränsad till en faktor 4. Formeln som utförs av noderna för att beräkna det nya målet är följande:

$$N = A \cdot \left(\frac{T}{1 209 600}\right)$$$


Var?


- $N$: Det nya målet;
- $A$: Det gamla målet för de senaste 2016 blocken;
- $T$: Den totala faktiska tiden för de senaste 2016 blocken i sekunder;
- $1,209,600$: Måltiden i sekunder för att producera 2016 block med 10 minuters intervall mellan varje block.


> ► *På franska används ibland termen "reciblage" för att hänvisa till justering. På engelska kallas det "Difficulty Adjustment" (svårighetsjustering)*