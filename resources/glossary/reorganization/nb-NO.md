---
term: REORGANISERING

---
Refererer til et fenomen der blokkjeden gjennomgår en endring av strukturen på grunn av eksistensen av konkurrerende blokker i samme høyde. Dette skjer når en del av blokkjeden erstattes av en annen kjede som har en større mengde akkumulert arbeid.

Disse omorganiseringene er en del av Bitcoins naturlige funksjon, der forskjellige utvinnere kan finne nye blokker nesten samtidig, og dermed dele Bitcoin-nettverket i to. I slike tilfeller kan nettverket midlertidig dele seg i konkurrerende kjeder. Når en av disse kjedene akkumulerer mer arbeid, blir de andre kjedene etter hvert forlatt av nodene, og blokkene deres blir det som kalles "foreldede blokker" eller "orphan blocks" Denne prosessen med å erstatte en kjede med en annen kalles reorganisering.

![](../../dictionnaire/assets/9.webp)

Omorganiseringer kan ha ulike konsekvenser. For det første, hvis en bruker har fått en transaksjon bekreftet i en blokk som viser seg å være forlatt, men denne transaksjonen ikke vises i den til slutt gyldige kjeden, blir transaksjonen ubekreftet igjen. Derfor anbefales det alltid å vente på minst seks bekreftelser før en transaksjon anses som virkelig uforanderlig. Etter seks blokker er omorganiseringer så usannsynlige at sjansen for at det skal skje en omorganisering, kan betraktes som tilnærmet lik null.

På globalt systemnivå innebærer omorganiseringer dessuten sløsing med utvinnernes regnekraft. Når en splitt skjer, vil noen utvinnere befinne seg på kjede A og andre på kjede B. Hvis kjede `B` til slutt forlates under en omorganisering, er all beregningskraften som utvinnerne har brukt på denne kjeden, per definisjon bortkastet. Hvis det er for mange omorganiseringer i Bitcoin-nettverket, reduseres dermed den generelle sikkerheten i nettverket. Dette er noe av grunnen til at det kan være farlig å øke blokkstørrelsen eller redusere intervallet mellom hver blokk (10 minutter).

> noen bitcoinere foretrekker å bruke "orphan block" om en utløpt blokk. I vanlig språkbruk brukes også "reorg" om en "omorganisering" Begrepet "omorganisering" er en anglikisme. For å være mer nøyaktig kan man snakke om en "resynkronisering"