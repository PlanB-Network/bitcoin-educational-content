---
term: FORCE CLOSE
---

Ikke-samarbeidende mekanisme for stenging av Lightning-kanaler. Når to brukere åpner en kanal med en Multisig 2/2, kan hver av dem ensidig stenge kanalen ved å kringkaste den siste Commitment Transaction som allerede har blitt signert, for å få tilbake sine bitcoins i kjeden. Dette er kjent som "force close".


Denne metoden brukes vanligvis hvis en av deltakerne ikke lenger svarer, eller hvis det ikke er mulig å samarbeide om å stenge kanalen. Hvis tvangsstenging kan unngås, er det best å bruke denne metoden, ettersom det tar lengre tid å få tilbake midler i kjeden, og det kan være mye dyrere i form av gebyrer.


I en force close sender en av de to brukerne ut Commitment Transaction, som gjenspeiler den siste kjente tilstanden til Lightning-kanalen. Deretter er det en tidslås før bitcoinsene kan hentes i kjeden, noe som gir den andre parten tid til å verifisere at transaksjonen samsvarer med den siste kanaltilstanden. Hvis en bruker prøver å jukse ved å publisere en utdatert Commitment Transaction, kan den andre parten bruke tilbakekallingshemmeligheten til å straffe juksemakeren og gjenopprette alle midlene i kanalen.