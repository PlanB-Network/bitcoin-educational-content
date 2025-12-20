---
name: Ashigaru - Ricochet
description: Förstå och använda Ricochet-transaktioner
---
![cover ricochet](assets/cover.webp)



> *Ett premiumverktyg som lägger till extra historik till din transaktion. Stävja svartlistorna och hjälp till att skydda mot orättvisa kontostängningar från tredje part.*

## Vad är en Ricochet?



Ricochet är en teknik som består i att utföra flera fiktiva transaktioner mot sig själv för att simulera en överföring av bitcoinägande. Detta verktyg skiljer sig från Ashigarus andra transaktioner (ärvda från Samurai Wallet) genom att det inte ger prospektiv anonymitet, utan snarare en form av retrospektiv anonymitet. Faktum är att Ricochet suddar ut de specifika egenskaper som kan äventyra fungibiliteten hos en Bitcoin-del.



Om du t.ex. gör en coinjoin kommer din del som kommer ut ur mixen att identifieras som sådan. Verktyg för kedjeanalys kan upptäcka paternerna i coinjoin-transaktioner och tilldela en etikett till de delar som kommer ut ur dem. I själva verket syftar coinjoin till att bryta ett mynts historiska länkar, men dess passage genom coinjoins förblir detekterbar. Analogt kan detta fenomen liknas vid kryptering av en text: även om det inte går att komma åt originaltexten i klartext är det lätt att identifiera att kryptering har tillämpats.



Märkningen "coinjoined" kan påverka en UTXO:s fungibilitet. Reglerade enheter, såsom utbytesplattformar, kan vägra att acceptera en coinjoined UTXO, eller till och med kräva förklaringar från dess ägare, med risk för att ditt konto blockeras eller dina medel fryses. I vissa fall kan plattformen till och med rapportera ditt beteende till statliga myndigheter.



Det är här Ricochet-metoden kommer in i bilden. För att blekna avtrycket som lämnas av en coinjoin utför Ricochet fyra på varandra följande transaktioner där användaren överför sina pengar till sig själv på olika adresser. Efter denna sekvens av transaktioner dirigerar Ricochet-verktyget slutligen bitcoins till sin slutdestination, till exempel en utbytesplattform. Syftet är att skapa avstånd mellan den ursprungliga coinjoin-transaktionen och den slutliga utgiftshandlingen. På detta sätt kommer blockkedjeanalysverktyg att anta att det förmodligen har skett en överföring av äganderätten efter coinjoin, och att det därför inte finns något behov av att vidta åtgärder mot emittenten.



![image](assets/fr/01.webp)



När man ställs inför Ricochet-metoden kan man tänka sig att program för kedjeanalys skulle fördjupa sin undersökning efter fyra studsar. Dessa plattformar står dock inför ett dilemma när det gäller att optimera upptäcktströskeln. De måste fastställa ett tröskelvärde för antalet hopp efter vilket de accepterar att ett ägarbyte sannolikt har inträffat och att länken till en tidigare coinjoin bör ignoreras. Att fastställa detta tröskelvärde är dock riskabelt: varje ökning av antalet hopp som observeras ökar exponentiellt antalet falska positiva resultat, dvs. personer som felaktigt markeras som deltagare i en coinjoin, när det i själva verket var någon annan som utförde operationen. Detta scenario utgör en stor risk för dessa företag, eftersom falska positiva resultat leder till missnöje, vilket kan driva berörda kunder till konkurrenterna. På lång sikt leder en överambitiös detektionströskel till att en plattform förlorar fler kunder än sina konkurrenter, vilket kan hota dess lönsamhet. Det är därför komplicerat för dessa plattformar att öka antalet observerade studsar, och 4 är ofta ett tillräckligt antal för att motverka deras analyser.



Således uppstår **det vanligaste användningsfallet för Ricochet när det är nödvändigt att dölja ett tidigare deltagande i en coinjoin på en UTXO som du äger.** Helst är det bäst att undvika att överföra bitcoins som har genomgått en coinjoin till reglerade enheter. Om man ändå inte har något annat alternativ, särskilt i det brådskande behovet av att likvidera bitcoins i statlig valuta, erbjuder Ricochet en effektiv lösning.



## Hur fungerar Ricochet på Ashigaru?



Ricochet är helt enkelt en metod för att skicka bitcoins till sig själv, som ursprungligen uppfanns av utvecklarna av Samurai Wallet. Det är därför fullt möjligt att simulera en Ricochet manuellt, utan behov av ett specialiserat verktyg. Men för dem som vill automatisera processen samtidigt som de njuter av ett mer polerat resultat, representerar Ricochet-verktyget som finns tillgängligt via Ashigaru-applikationen (som är en Samourai fork) en bra lösning.



Eftersom Ashigaru tar betalt för sin tjänst kostar en Ricochet 100 000 sats` som en serviceavgift, plus en mining avgift. Det rekommenderas därför att man använder det för överföringar av betydande belopp.



Ashigaru-applikationen erbjuder två Ricochet-varianter:





- Reinforced Ricochet, eller "förskjuten leverans", som ger fördelen att Ashigarus serviceavgifter sprids över de fem på varandra följande transaktionerna. Detta alternativ säkerställer också att varje transaktion sänds vid en separat tidpunkt och registreras i ett annat block, vilket så nära som möjligt efterliknar beteendet vid ett ägarbyte. Även om den här metoden är långsammare är den att föredra för dem som inte har bråttom, eftersom den maximerar Ricochets effektivitet genom att stärka dess motståndskraft mot kedjeanalys;





- Den klassiska Ricochet, som är utformad för att utföra operationen snabbt, sänder alla transaktioner inom ett reducerat tidsintervall. Denna metod erbjuder därför mindre sekretess och mindre motståndskraft mot analys än den förstärkta metoden. Den bör endast användas för brådskande försändelser.



## Hur gör man en Ricochet på Ashigaru?



Att göra en rikoschett på Ashigaru är mycket enkelt: aktivera bara motsvarande alternativ när du skapar en sändningstransaktion. För att börja, klicka på `+`-knappen, sedan på `Sänd` och välj det konto från vilket du vill skicka pengarna.



![Image](assets/fr/02.webp)



Fyll i transaktionsinformationen: beloppet som ska skickas och mottagarens slutliga adress efter Ricochet-hoppet. Markera sedan alternativet `Ricochet`.



![Image](assets/fr/03.webp)



Du kan sedan välja mellan de två Ricochet-lägen som diskuterades i teoriavsnittet: antingen klassisk Ricochet, där alla transaktioner ingår i samma block, eller förskjuten leverans, som förbättrar Ricochet-kvaliteten på bekostnad av en längre fördröjning.



När du har gjort ditt val trycker du på pilen längst ned på skärmen för att bekräfta.



![Image](assets/fr/04.webp)



På nästa skärm ser du en fullständig sammanfattning av din transaktion. Det är också här du kan justera avgiftssatsen för dina Ricochet-transaktioner enligt marknadsförhållandena. Om allt är till belåtenhet drar du den gröna pilen för att signera och distribuera Ricochet-transaktioner.



![Image](assets/fr/05.webp)



Vänta medan de olika hoppen körs automatiskt.



![Image](assets/fr/06.webp)



Dina transaktioner har skickats framgångsrikt.



![Image](assets/fr/07.webp)



Du är nu helt bekant med Ricochet-alternativet som finns i Ashigaru-applikationen. För att gå vidare rekommenderar jag att du tar min BTC 204-utbildningskurs, som kommer att lära dig i detalj hur du stärker din onchain-konfidentialitet.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c