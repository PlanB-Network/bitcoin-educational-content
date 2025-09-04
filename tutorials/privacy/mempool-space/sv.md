---
name: Mempool
description: Utforska hela Bitcoin:s ekosystem.
---

![cover](assets/cover.webp)



Bitcoin-protokollet är ett pseudonymt, decentraliserat nätverk som är öppet för konsultation. Medlemmar (noder), dvs. datorer med en instans av Bitcoin-programvaran, har obegränsad tillgång till alla data som publiceras på Bitcoin. Under Bitcoin:s första år var protokollet dock inte lika allmänt tillgängligt som det är idag.


I början av Bitcoin var det nödvändigt att köra en Bitcoin-nod för att få tillgång till lämpliga verktyg (bitcoin-cli) för att undersöka nätverket från kommandorader.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Projekt har därför startats för att utöka Bitcoin-communityn och göra den mer tillgänglig för alla som inte äger en nod och/eller inte har de tekniska färdigheter som krävs.



I den här handledningen tittar vi på **Mempool.space**-projektet, dess funktioner och den inverkan det har haft på Bitcoin-ekosystemet.



## Vad är Mempool.space?



**Mempool.space** är en utforskare med öppen källkod som ger användbar information om transaktioner, transaktionsavgifter, block och utvinnare på de olika Bitcoin-protokollnätverken. Den lanserades 2020 och innebär en betydande förbättring av användarupplevelsen genom representativ grafik, smidiga animationer och tydliga gränssnitt.



För att förstå projektet är en Mempool (minnespool) ett virtuellt utrymme där alla transaktioner som väntar på bekräftelse i Bitcoin-nätverket lagras. En Mempool är som ett "väntrum" där Bitcoin-transaktioner väntar på att bli bekräftade. Varje dator i nätverket (nod) har sitt eget väntrum, vilket förklarar varför inte alla transaktioner är synliga för alla samtidigt.



Plattformens huvudsakliga inverkan på Bitcoin:s ekosystem är att den ger dig tillgång till den varierande informationen i minnesområdena på de flesta noder som finns på Bitcoin utan att du behöver köra en. Mempool.space är en lagringsplats för visning och sökning av Bitcoin protokollnätverk.



En alltmer utbredd användning i ekosystemet och det faktum att Mempool.space är öppen källkod har gjort det möjligt att integrera det i fler och fler personliga värdsystem. Du kan nu ha din egen instans av Mempool.space direkt på din personliga nod. Se vår handledning om hur du konfigurerar Mempool.space på din Umbrel-nod nedan.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Grunderna i Mempool.space



Som nämnts ovan är [Mempool.space](https://Mempool.space) en Bitcoin-protokollutforskare som låter dig övervaka dina transaktioner och deras spridning i det valda Bitcoin-nätverket i realtid, från en grafisk Interface.



Mempool.space stöder många nätverk med Bitcoin-protokoll.


I menyfältet hittar du följande nätverk:




- Mainnet** : Det huvudsakliga Bitcoin-nätverket där verkliga Bitcoin-transaktioner äger rum.
- Signet**: Ett testnätverk som använder digitala signaturer för att validera block utan att kräva de resurser som krävs av huvudnätverket.
- Testnet 3**: Ett riskfritt test- och utvecklingsnätverk på Bitcoin-protokollet.
- Testnet 4** : Den nya versionen av Testnet 3 ger större stabilitet och nya samförståndsregler i testmiljön.



![reseaux](assets/fr/01.webp)



På startsidan, till vänster i Green, ser du de möjliga framtida blocken (grupper av transaktioner) som är redo att valideras och integreras (minas) i Bitcoin-nätverket. I genomsnitt bryts ett block var tionde minut: spara den här informationen, eftersom den kommer att vara till nytta senare i vår utveckling.


I lila, på höger sida, hittar du de senaste blocken som utvunnits på Bitcoin, där numret på det senast utvunna blocket representerar nätverkets nuvarande höjd.



![blocs](assets/fr/02.webp)



Avsnittet **Transaktionsavgifter** är en uppskattning av transaktionsavgifter. Ju högre avgifter som tilldelas din transaktion, desto mer sannolikt är det att din transaktion kommer att läggas till i nästa block som är redo att brytas.


Transaktionsavgifter representerar den kostnad en Miner tar från dig för att infoga din transaktion i ett kandidatblock för Mining. Den definieras av förhållandet sat/vB (Satoshi/Virtual Bytes) som representerar antalet satoshis som du betalar för det utrymme som din transaktion kommer att uppta i kandidatblocket.



⚠️ VIKTIGT: I händelse av Mempool-mättnad prioriterar miners transaktioner som erbjuder det bästa Satoshi/vByte-förhållandet. Ju tyngre (större) din transaktion är, desto fler satoshis kommer den att behöva för att inkluderas snabbt.



![fees-visualizer](assets/fr/03.webp)



I avsnittet **Mempool Goggles** kan du visualisera det utrymme som upptas av en transaktion.



![mempool](assets/fr/04.webp)



Ett block bryts ungefär var tionde minut på grund av svårighetsgraden på Proof of Work som brytarna måste tillhandahålla för att lägga till sitt kandidatblock i kedjan av brytade block. Denna svårighetsgrad varierar var **2016:e block**, vilket motsvarar ungefär **2 veckor**. Du kan se utvecklingen av denna svårighet här.



![difficulty](assets/fr/05.webp)



När ett nytt block läggs till i huvudkedjan får Miner i det validerade blocket rätt till en belöning som består av en fast del (halveras vart 210 000:e block**, vilket motsvarar cirka 4 år** under halveringstiden) och transaktionsavgifter.



![halving](assets/fr/06.webp)



## Få tillgång till dina transaktionsuppgifter



I sökfältet Mempool.space kan du skriva in din Bitcoin Address eller din transaction ID för att ta reda på mer om din historia.



![search](assets/fr/07.webp)



På sidan med transaktionsdetaljer hittar du allmän information om din transaktion:




- Status**: Bekräftad när den läggs till i ett block, obekräftad när den väntar i en Mempool.
- Transaktionsavgifter**.
- Beräknad ankomsttid (ETA)** :  Den ungefärliga tid det tar för din transaktion att läggas till i ett block. Den beräknas enligt det förhållande som utgör de avgifter som är förknippade med den här transaktionen.



![general-txinfo](assets/fr/08.webp)



Avsnittet **Flow** visar en graf över transaktionens komponenter.



Ingångar (tidigare UTXO), som används för din transaktion, och utgångar som ger mottagarna rätt att använda bitcoins från varje utgång genom att presentera den signatur som krävs för deras utgifter.



![flow](assets/fr/09.webp)



Mer information om de adresser som används finns i avsnittet **Inputs & Outputs**.



![address](assets/fr/10.webp)



Upptäck de olika Bitcoin-transaktionssystemen för att förbättra din sekretess.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Snabba upp dina transaktioner



I Bitcoin:s ekosystem är aspekten av transaktionsvalidering av miners intimt kopplad till de transaktionsavgifter som är associerade med den transaktionen. Miners prioriterar transaktioner med ett högre avgiftsförhållande (satoshis/vBytes), vilket kan påverka giltigheten av din transaktion om du inte betalar rimliga avgifter som accepteras av miners. Din transaktion skulle fastna i Mempool i väntan på ett block som accepterar dess avgiftsförhållande.



Lyckligtvis finns det två metoder tillgängliga i Bitcoin-nätverket för att påskynda bekräftelsen av din transaktion.





- RBF** - Ersättning med avgift: En metod som gör att du kan använda samma poster som din transaktion med låg avgift, men den här gången genom att höja transaktionsavgiften för att påskynda valideringen. Din nya transaktion kommer att valideras snabbare och inkluderas i ett block, vilket ogiltigförklarar transaktionen med låg avgift.



Du kan utföra en avgiftsersättningsåtgärd med plånböcker som accepterar denna mekanism. Se t.ex. vår artikel om Blue Wallet Wallet.



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- CPFP** - Child pay for parent: Ett tillvägagångssätt inspirerat av RBF, men på mottagarens sida. När den transaktion som du är mottagare av blockeras i en Mempool har du möjlighet att spendera utgifterna (UTXO) för denna transaktion, trots att den ännu inte har bekräftats, genom att tilldela fler avgifter till denna nya transaktion så att de genomsnittliga avgifterna - för den transaktion som du är mottagare av och den initierade transaktionen - uppmuntrar miners att inkludera båda transaktionerna i ett block.



⚠️ Den första transaktionen måste ingå i ett block för att den andra transaktionen ska kunna bekräftas.



Om alla dessa termer verkar lite för tekniska rekommenderar jag att du [konsulterar vår ordlista](https://planb.network/resources/glossary), som innehåller definitioner av alla tekniska termer relaterade till Bitcoin och dess ekosystem.



Utöver dessa metoder kan du med Mempool.space, tack vare dess anslutningar till över 80 % av de gruvarbetare som finns i Bitcoin-nätverket, också påskynda alla dina **obekräftade** transaktioner, även de som inte aktiverar RBF, genom att betala en ersättning till gruvarbetarna i Exchange för att infoga din lågkostnadstransaktion i nästa block som är redo att brytas.



Klicka på knappen **Accelerate** på sidan med transaktionsdetaljer och fortsätt sedan att betala din motpart till gruvarbetarna.



![accelerate-section](assets/fr/11.webp)


## Minderåriga



En Miner avser en person som hanterar en gruva, dvs. en dator som är engagerad i Mining-processen, som består av att delta i Proof-of-Work. Miner grupperar de väntande transaktionerna i sin Mempool för att bilda ett kandidatblock. Den söker sedan efter en giltig Hash, mindre än eller lika med målet, för rubriken på detta block genom att modifiera de olika noncesen. Om han hittar en giltig Hash sänder han sitt block till Bitcoin-nätverket och inkasserar den tillhörande ekonomiska belöningen, som består av blocksubventionen (skapande av nya bitcoins ex-nihilo) och transaktionsavgiften.



https://planb.network/courses/ce272232-0d97-4482-884a-0f77a2ebc036

❗Miners är som "validatorer" som verifierar och grupperar transaktioner i block. För att lägga till ett nytt block i Bitcoin-nätverket måste de lösa ett komplext matematiskt pussel (Proof-of-Work). Den första Miner som löser pusslet vinner en Bitcoin-belöning (blockbidrag + avgifter för transaktioner som ingår i blocket).



Svårighetsgraden för denna Proof of Work övervakas, vilket gör att du kan visualisera utvecklingen av den datorkraft som krävs för gruvarbetare. Du kommer att hitta i avsnitten nedan :





- En uppskattning av de totala belöningarna som gruvarbetarna fick under den senaste svårighetsjusteringen, samt uppskattningar av nästa Halving av blockbidraget, som inträffar vart 210 000:e block (ca 04 år).



![rewards](assets/fr/12.webp)



Denna svårighet justeras varje 2016 block (cirka två veckor). Den är omvänt proportionell mot den genomsnittliga tid som gruvarbetare tar för Miner varje 2016 block.


När den genomsnittliga tidsåtgången för miners är mindre än 10 minuter ökar svårighetsgraden, vilket visar att det var lättare för miners att validera Miner-block. Omvänt, när den genomsnittliga tidsåtgången är större än 10 minuter, minskar svårigheten.



![mining-pool](assets/fr/13.webp)





- Grupper av gruvarbetare: Med tanke på svårighetsgraden samarbetar en grupp miners för att hjälpa till att hitta Proof of Work på Bitcoin, i vad vi kallar en **pool**. När ett block bryts av gruppen fördelas den erhållna belöningen enligt den procentuella framgången i varje Miner:s partiella lösningssökning, dvs. bidraget i datorkraft i sökandet efter Proof-of-Work, eller enligt den ersättningsmetod som överenskommits i samarbetet.





![mining](assets/fr/14.webp)



## Lightning Network infrastruktur



Mempool tillhandahåller inte bara information om Bitcoin:s nätverksinfrastruktur (huvudkedja). Den integrerar också visualiserings- och utforskningsverktyg för Bitcoin:s Lightning-overlay.



I avsnittet **Lightning** kan du se alla befintliga kopplingar mellan Lightning-noder.



![network-stats](assets/fr/15.webp)



Denna Interface innehåller information om :





- Lightning Network statistik.



![distribution](assets/fr/16.webp)




⚠️ **VIKTIGT**: Kapaciteten för en betalningskanal anger det maximala belopp som en nod kan skicka till en annan nod under en Lightning-transaktion.





- Lightning-noderna fördelas enligt internetleverantör (hostingtjänst) och eventuellt enligt betalningskanalens kapacitet.



![distribution](assets/fr/17.webp)





- Historien om Lightning Network:s totala kapacitet.


Du hittar också en rangordning av dessa noder enligt kapaciteten hos deras betalningskanaler.



![ranking](assets/fr/18.webp)



## Mer grafik



Mempool.space är den perfekta plattformen för att njuta av interaktion med Bitcoin-protokollnätverk. Graferna ger inte bara visuella data som hjälper dig att bestämma när du ska göra transaktioner, utan också exakta parametrar som gör att du i realtid kan visualisera styrkan och hälsan hos Bitcoin-nätverket och tillhörande Lightning-infrastrukturer.



I avsnittet **Graphics** kan du se viktiga data om Bitcoin-nätet:




- Mempool:s storleksutveckling: Du kan se hur storleken på Mempool fluktuerar, vilket kan indikera perioder med hög eller låg aktivitet i nätverket.



![graphs](assets/fr/19.webp)






- Utvecklingen av transaktioner och transaktionsavgifter i det valda nätverket: Genom att spåra variationer i transaktioner per sekund kan du förutse perioder med överbelastning eller låg aktivitet och optimera dina transaktionsavgifter. Den här grafen ger dig ett perspektiv på nätverkets kapacitet att hantera transaktionsvolymen.



![graphs](assets/fr/20.webp)



Nu när du har nått slutet på din resa på Mempool.space kan du bli din egen utforskare och spåra dina transaktioner i realtid. Nedan hittar du vår artikel om utforskaren Bitcoin **Public Pool**.



https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1