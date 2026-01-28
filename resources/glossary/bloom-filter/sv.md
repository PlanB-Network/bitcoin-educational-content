---
term: Bloom-filter
definition: Probabilistisk datastruktur som möjliggör snabb testning av medlemskap i en mängd, används i SPV-plånböcker.
---

En probabilistisk datastruktur som används för att testa om ett element är en del av en uppsättning. Bloomfilter gör det möjligt att snabbt kontrollera medlemskap utan att testa hela datasetet. De är särskilt användbara i sammanhang där utrymme och hastighet är kritiska, men där en låg och kontrollerad felfrekvens är acceptabel. Bloom-filter producerar inte falska negativa resultat, men de ger generate en viss mängd falska positiva resultat. När ett element läggs till i filtret positioneras flera Hash-funktioner generate i en bitmatris. För att kontrollera medlemskap används samma Hash-funktioner. Om alla motsvarande bitar är inställda är elementet troligen i uppsättningen, men med risk för falska positiva resultat. Bloomfilter används ofta inom databaser och nätverk. Det är särskilt känt att Google använder dem för sitt komprimerade databashanteringssystem *BigTable*. I Bitcoin-protokollet används de särskilt för SPV-plånböcker enligt BIP37.


> när man specifikt talar om användningen av Bloomfilter i samband med Bitcoin-transaktioner förekommer ibland termen "Transaction Bloom Filtering"