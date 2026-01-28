---
term: Blinde handtekening
definition: Digitale handtekening waarbij de ondertekenaar de ondertekende inhoud niet kent, gebruikt in Chaumian CoinJoins en ecash.
---

Chaum's blinde handtekeningen zijn een vorm van digitale handtekening waarbij de uitgever van de handtekening de inhoud van het bericht dat hij ondertekent niet kent. De handtekening kan later echter worden geverifieerd met het originele bericht. Deze techniek werd in 1983 ontwikkeld door cryptograaf David Chaum.


Neem het voorbeeld van een bedrijf dat een vertrouwelijk document, zoals een Contract, wil verifiëren zonder de inhoud te onthullen. Het bedrijf past een maskeerproces toe dat het originele document cryptografisch omvormt op een omkeerbare manier. Dit gewijzigde document wordt naar een certificeringsinstantie gestuurd die een blinde handtekening toepast zonder de onderliggende inhoud te kennen. Na ontvangst van het gemaskeerde ondertekende document, ontmaskert het bedrijf de handtekening. Het resultaat is een origineel document dat is geverifieerd door de handtekening van de certificeringsinstantie, zonder dat deze ooit de originele inhoud heeft gezien.


Chaum's blinde handtekeningen maken het dus mogelijk om de authenticiteit van een document te certificeren zonder de inhoud ervan te kennen, waardoor zowel de vertrouwelijkheid van de gegevens van de gebruiker als de integriteit van het ondertekende document wordt gewaarborgd.


In Bitcoin wordt dit protocol gebruikt in systemen van Chaumiaanse banken als een overlay (Cashu, Fedimint, etc.), maar vooral in Chaumiaanse CoinJoin protocollen, om ervoor te zorgen dat de coördinator niet in staat is om een input aan een output te koppelen.