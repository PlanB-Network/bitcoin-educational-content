---
term: BCH-kod
definition: Felkorrigerande koder som används i Bech32- och Bech32m-adresser för att upptäcka inmatningsfel.
---

En klass av felkorrigeringskoder som används för att upptäcka och korrigera fel i en datasekvens. Med andra ord används BCH-felkorrigeringskoder för att hitta och korrigera slumpmässiga fel i överförd information, för att säkerställa att den anländer intakt till sin destination. Akronymen "BCH" står för initialerna i namnen på uppfinnarna av dessa koder: Bose, Ray-Chaudhuri och Hocquenghem.


Detta verktyg används inom många områden av databehandling, inklusive SSD-enheter, DVD-skivor och QR-koder. Tack vare dessa felkorrigerande koder är det till exempel fortfarande möjligt att hämta den information som QR-koden kodar, även om den är delvis täckt.


Som en del av Bitcoin används BCH-koder för kontrollsumman i Bech32 och Bech32m (post-SegWit) Address-format. De utgör en bättre kompromiss mellan kontrollsummans storlek och feldetekteringsmöjligheterna än de enkla Hash-funktioner som tidigare användes på Legacy-adresser. I samband med Bitcoin används BCH-koder endast för feldetektering, inte för felkorrigering. Programvaran i Bitcoin-portföljen identifierar och rapporterar till användaren eventuella fel i en mottagande Address, men ändrar inte den felaktiga Address automatiskt. Detta val motiveras av det faktum att integrering av felkorrigering oundvikligen påverkar algoritmens feldetekteringsförmåga.