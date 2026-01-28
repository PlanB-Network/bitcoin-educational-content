---
term: Temporal modell
definition: Analys av sändningstider för transaktioner för att härleda karaktären eller platsen för en on-chain-entitet.
---

Vissa mänskliga beteenden är igenkännbara On-Chain. Det kanske mest användbara i kedjeanalys är ditt sömnmönster! Ja, när du sover sänder du antagligen inte Bitcoin-transaktioner. I allmänhet sover du ungefär samma timmar. Därför används temporala analyser ofta i kedjeanalys. Det handlar helt enkelt om att registrera de tidpunkter då en viss enhets transaktioner sänds till Bitcoin-nätverket. Genom att analysera dessa tidsmönster kan vi härleda många olika typer av information.


För det första kan en tidsanalys ibland identifiera den spårade enhetens karaktär. Om vi observerar att transaktioner sänds konsekvent under 24 timmar kan detta tyda på betydande ekonomisk aktivitet. Den enhet som ligger bakom dessa transaktioner är sannolikt ett företag, eventuellt internationellt och kanske med automatiserade förfaranden internt. Om vi däremot ser att det tidsmässiga mönstret är mer utspritt över 16 specifika timmar, kan vi anta att vi har att göra med en enskild användare, eller kanske ett lokalt företag beroende på de volymer som utväxlas.


Utöver den observerade enhetens natur kan det temporala mönstret också ge en ungefärlig indikation på användarens plats genom tidszoner. Detta gör att vi kan korrelera andra transaktioner och använda Timestamp för dessa som en ytterligare heuristik som kan ingå i en kedjeanalys.


I ett annat register är det också denna typ av tidsanalys som ledde till hypotesen att Satoshi Nakamoto inte opererade från Japan, utan faktiskt från USA: [_The Time Zones of Satoshi Nakamoto_](https://medium.com/@insearchofsatoshi/the-time-zones-of-Satoshi-nakamoto-aa40f035178f).