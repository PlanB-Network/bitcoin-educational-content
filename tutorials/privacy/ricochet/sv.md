---
name: Ricochet
description: Förstå och använda Ricochet-transaktioner
---
![cover ricochet](assets/cover.webp)


*** VARNING:** Efter gripandet av grundarna av Samourai Wallet och beslagtagandet av deras servrar den 24 april är Ricochet-verktyget inte längre tillgängligt. Det är dock möjligt att detta verktyg kan återinföras under de kommande veckorna. Under tiden kan du bara utföra en Ricochet manuellt. Den teoretiska delen av denna artikel förblir relevant för att förstå dess funktion och lära sig hur man gör det manuellt.*


_Vi följer noga utvecklingen av detta fall och utvecklingen av de tillhörande verktygen. Du kan vara säker på att vi kommer att uppdatera denna handledning när ny information blir tillgänglig._


_Den här handledningen tillhandahålls endast i utbildnings- och informationssyfte. Vi varken stödjer eller uppmuntrar användning av dessa verktyg i kriminella syften. Det är varje användares ansvar att följa de lagar som gäller i deras jurisdiktion._


---

> Ett premiumverktyg som lägger till extra historik till din transaktion. Stoppa svartlistorna och hjälp till att skydda mot orättvisa konton som stängs av tredje part.

## Vad är Ricochet?


Ricochet är en teknik som innebär att man genomför flera fiktiva transaktioner till sig själv för att simulera en överföring av Bitcoin Ownership. Detta verktyg skiljer sig från andra Samourai-transaktioner eftersom det inte ger prospektiv anonymitet, utan snarare en form av retrospektiv anonymitet. Ricochet hjälper till att sudda ut de särdrag som skulle kunna äventyra fungibiliteten hos ett Bitcoin-mynt.


Om du t.ex. utför en CoinJoin kommer ditt mynt som kommer ut från mixen att identifieras som ett sådant. Verktyg för kedjeanalys kan upptäcka mönster av CoinJoin-transaktioner och märka mynten som kommer ut ur dem. CoinJoin syftar faktiskt till att bryta ett mynts historiska länkar, men dess passage genom coinjoins förblir detekterbar. För att göra en analogi kan detta fenomen liknas vid kryptering av en text: även om vi inte kan komma åt den ursprungliga klartexten är det lätt att identifiera att kryptering har tillämpats.


Just denna etikett "CoinJoin output coin" kan påverka fungibiliteten hos en UTXO. Reglerade enheter, såsom Exchange-plattformar, kan vägra att acceptera en UTXO som har genomgått en CoinJoin, eller till och med kräva förklaringar från dess ägare, med risk för att få sitt konto blockerat eller medel frysta. I vissa fall kan plattformen till och med rapportera ditt beteende till statliga myndigheter.


Det är här Ricochet-metoden kommer in i bilden. För att sudda ut fotavtrycket som lämnas av en CoinJoin utför Ricochet fyra på varandra följande transaktioner där användaren överför sina medel till sig själva på olika adresser. Efter denna sekvens av transaktioner dirigerar Ricochet-verktyget slutligen bitcoins till sin slutdestination, till exempel en Exchange-plattform. Målet är att skapa avstånd mellan den ursprungliga CoinJoin-transaktionen och den slutliga utgiftshandlingen. På så sätt kommer kedjeanalysverktyg att tro att det sannolikt har skett en överföring av Ownership efter CoinJoin, och att det därför är onödigt att vidta åtgärder mot avsändaren.


![ricochet diagram](assets/en/1.webp)


Mot bakgrund av Ricochet-metoden kan man tänka sig att program för kedjeanalys skulle fördjupa sin undersökning utöver fyra studsar. Dessa plattformar står dock inför ett dilemma när det gäller att optimera upptäcktströskeln. De måste fastställa en gräns för antalet hopp efter vilket de medger att en egenskapsförändring sannolikt har inträffat och att länken till en tidigare CoinJoin bör ignoreras. Att fastställa detta tröskelvärde är dock riskabelt: varje förlängning av det observerade antalet hopp ökar exponentiellt volymen av falska positiva resultat, dvs. individer som felaktigt markeras som deltagare i en CoinJoin, när operationen i själva verket utfördes av någon annan. Detta scenario utgör en stor risk för dessa företag, eftersom falska positiva resultat leder till missnöje, vilket kan driva berörda kunder mot konkurrenterna. På lång sikt leder ett alltför ambitiöst tröskelvärde till att en plattform förlorar fler kunder än sina konkurrenter, vilket kan hota dess lönsamhet. Det är därför komplicerat för dessa plattformar att öka antalet observerade studsar, och 4 är ofta ett tillräckligt antal för att motverka deras analyser.


Således uppstår **det vanligaste användningsfallet för Ricochet när det är nödvändigt att dölja ett tidigare deltagande i en CoinJoin på en UTXO som tillhör dig**. Helst är det bäst att undvika att överföra bitcoins som har genomgått en CoinJoin till reglerade enheter. Men i händelse av att det inte finns något annat alternativ, särskilt i brådskande fall att likvidera bitcoins till fiatvaluta, erbjuder Ricochet en effektiv lösning.


## Hur fungerar Ricochet på Samourai Wallet?

Ricochet är helt enkelt en metod där man skickar bitcoins till sig själv. Det är därför fullt möjligt att manuellt simulera en Ricochet utan att använda ett specialiserat verktyg. Men för dem som vill automatisera processen och samtidigt dra nytta av ett mer polerat resultat är Ricochet-verktyget som finns tillgängligt via Samourai Wallet-applikationen en bra lösning.


Eftersom tjänsten betalas på Samourai, medför en Ricochet en kostnad på 100 000 Sats` som en serviceavgift, utöver Mining avgifter. Det är därför mer rekommenderat att använda den för överföringar av betydande belopp.


Samourai-applikationen erbjuder två varianter av Ricochet:


- Reinforced Ricochet, eller "förskjuten leverans", erbjuder fördelen att Samourais serviceavgifter sprids över fem på varandra följande transaktioner. Detta alternativ säkerställer också att varje transaktion sänds vid en distinkt tidpunkt och registreras i ett annat block, vilket nära efterliknar beteendet hos en förändring av Ownership. Även om den här metoden är långsammare är den att föredra för dem som inte har bråttom, eftersom den maximerar Ricochets effektivitet genom att förbättra dess motståndskraft mot kedjeanalys.
- Classic Ricochet, som är utformad för att utföra operationen snabbt genom att sända ut alla transaktioner inom ett kortare tidsintervall. Denna metod erbjuder därför mindre integritet och lägre motståndskraft mot analys jämfört med den förstärkta metoden. Den bör endast användas för brådskande överföringar.


## Hur utför man en Ricochet på Samourai Wallet?

För att utföra en Ricochet-transaktion från Samourai Wallet-applikationen, följ vår videohandledning:

![Ricochet YouTube video tutorial](https://youtu.be/Gsz0zuVo3N4)


Om du vill studera Ricochet-transaktionerna som utfördes i den här handledningen, här är de:


- Den första Ricochet-transaktionen: [8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc](https://Mempool.space/fr/Testnet/tx/8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc)
- Den sista Ricochet-transaktionen: [27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777](https://Mempool.space/fr/Testnet/tx/27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777)


**Externa resurser:**


- https://docs.samourai.io/en/Wallet/features/ricochet