---
term: Tidsstempel

definition: Mekanisme som knytter en tidsmarkør til en hendelse for å etablere kronologien for transaksjoner og blokker.
---

Tidsstempling, eller "Timestamp" på engelsk, er en mekanisme for å knytte et nøyaktig tidsmerke til en hendelse, data eller melding. I datasystemer brukes tidsstempling generelt til å fastslå den kronologiske rekkefølgen av operasjoner og til å verifisere dataintegriteten over tid.


I Bitcoin brukes tidsstempler til å etablere kronologien til transaksjoner og blokker. Hver blokk i Blockchain inneholder et tidsstempel som angir det omtrentlige tidspunktet da den ble opprettet. Satoshi Nakamoto snakker til og med om en "tidsstempelserver" i hvitboken sin for å beskrive det vi i dag ville kalt "Blockchain". Tidsstemplingens rolle på Bitcoin er å bestemme transaksjonenes kronologi, slik at det uten innblanding fra en sentral myndighet kan fastslås hvilken transaksjon som kom først. Denne mekanismen gjør det mulig for hver bruker å verifisere at en transaksjon ikke har funnet sted tidligere, og dermed forhindre at en ondsinnet bruker foretar en dobbeltutgift. Denne mekanismen begrunnes av Satoshi Nakamoto i hvitboken hans med den berømte setningen: "*Denne standarden er basert på Unix-tiden, som representerer det totale antallet sekunder som har gått siden 1. januar 1970.*"


> tidsstemplene for blokkene er relativt fleksible på Bitcoin, siden et tidsstempel bare må være større enn mediantiden for de 11 foregående blokkene (MTP) og mindre enn medianen av tidene som returneres av nodene (nettverksjustert tid) pluss 2 timer for at det skal anses som gyldig