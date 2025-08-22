---
term: BIP0072
---

Vult BIP70 en BIP71 aan door de uitbreiding van Bitcoin URI (BIP21) te definiëren met een extra parameter `r`. Deze parameter maakt het mogelijk een link op te nemen naar een beveiligd betalingsverzoek, ondertekend door het SSL-certificaat van de verkoper. Wanneer een klant op deze uitgebreide URI klikt, neemt zijn Wallet contact op met de server van de verkoper om de betalingsgegevens op te vragen. Deze gegevens worden automatisch ingevuld in de Interface transactie van de Wallet, en de klant kan worden geïnformeerd dat hij betaalt aan de domeineigenaar die overeenkomt met het ondertekende certificaat (bijvoorbeeld "pandul.fr"). Aangezien deze uitbreiding gebundeld is met BIP70, is deze nooit op grote schaal toegepast.