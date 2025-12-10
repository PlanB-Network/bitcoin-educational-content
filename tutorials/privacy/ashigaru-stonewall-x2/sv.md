---
name: Ashigaru - Stonewall x2
description: Förstå och använda Stonewall x2-transaktioner på Ashigaru
---
![cover stonewall x2](assets/cover.webp)



> *Gör varje utgift till en coinjoin

## Vad är en Stonewall x2-transaktion?



Stonewall x2 är en specifik form av Bitcoin-transaktion som är utformad för att öka användarnas konfidentialitet när de spenderar genom att samarbeta med en tredje part som inte är involverad i utgifterna. Den här metoden simulerar en mini-coinjoin mellan två deltagare, samtidigt som en betalning görs till en tredje part. Stonewall x2-transaktioner finns tillgängliga i Ashigaru-applikationen, en fork från Samourai Wallet (teamet bakom skapandet av denna typ av transaktion).



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Hur det fungerar är relativt enkelt: du använder en UTXO i din ägo för att göra betalningen och tar hjälp av en tredje part som också bidrar med en egen UTXO. Transaktionen slutar med fyra utgångar: två av dem i lika stora belopp, den ena avsedd för betalningsmottagarens adress, den andra för en adress som tillhör samarbetspartnern. En tredje UTXO returneras till en annan adress som tillhör samarbetspartnern, vilket gör det möjligt för honom att återfå det ursprungliga beloppet (en neutral åtgärd för honom, utöver mining-kostnaderna), och en sista UTXO returneras till en adress som tillhör oss, vilket utgör betalningsutbytet.



Tre olika roller definieras således i Stonewall x2 transaktioner:




- Utfärdaren, som gör den faktiska betalningen;
- Samarbetspartnern, som gör bitcoins tillgängliga för att förbättra transaktionens anonymitet, samtidigt som han får tillbaka sina pengar i sin helhet i slutet (en neutral åtgärd för honom, utöver mining-kostnaderna);
- Mottagaren, som kanske inte är medveten om transaktionens specifika karaktär och helt enkelt förväntar sig betalning från avsändaren.



Låt oss ta ett exempel. Alice är hos bagaren för att köpa sin baguette, som kostar 4 000 sats. Hon vill betala i bitcoins, samtidigt som hon vill behålla viss sekretess kring sin betalning. Så hon ringer sin vän Bob, som hjälper henne med detta.



![image](assets/fr/01.webp)



Genom att analysera denna transaktion kan vi se att bagaren faktiskt fick 4 000 sats` som betalning för baguetten. Alice använde 10 000 sats` i insatsvaror och fick tillbaka 6 000 sats` i utdata, vilket gav ett nettobalans på 4 000 sats`, vilket motsvarar priset på baguetten. Bob använde 15 000 gw-10 i insatsvaror och fick två utdata: en på 4 000 gw-10 och en på 11 000 gw-10, vilket ger ett saldo på 0 gw-10.



I det här exemplet har jag avsiktligt utelämnat mining-avgifterna för att göra det lättare att förstå. I själva verket delas transaktionsavgifterna lika mellan betalningsutgivaren och samarbetspartnern.



## Vad är skillnaden mellan Stonewall och Stonewall x2?



En Stonewall X2-transaktion fungerar på exakt samma sätt som en Stonewall-transaktion, förutom att den förra är kollaborativ, medan den senare inte är det. Som vi har sett innebär en Stonewall x2-transaktion att en tredje part deltar, som är extern till betalningen, och som kommer att göra sina bitcoins tillgängliga för att förbättra transaktionens konfidentialitet. I en klassisk Stonewall-transaktion är det avsändaren som tar på sig rollen som samarbetspartner.



Låt oss gå tillbaka till vårt exempel med Alice på bageriet. Om hon inte hade kunnat hitta någon som Bob att följa med henne på sin utgiftsresa, kunde hon ha gjort en Stonewall på egen hand. På så sätt skulle de två UTXO:erna på vägen in ha varit hennes, och hon skulle ha plockat upp 3 på vägen ut.



![image](assets/fr/02.webp)




Ur en utomståendes synvinkel skulle transaktionen ha förblivit densamma.



![image](assets/fr/05.webp)



Logiken bör därför vara som följer när du vill använda ett Ashigaru-utgiftsverktyg:




- Om handlaren inte stöder Payjoin Stowaway kan du göra en samarbetstransaktion med en annan person utanför betalningen tack vare Stonewall x2 ;
- Om du inte kan hitta någon som vill göra en Stonewall x2-transaktion kan du göra en Stonewall only-transaktion, som kommer att efterlikna beteendet hos en Stonewall x2-transaktion.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-033daa45-d42c-40e1-9511-cea89751c3d4

## Vad är poängen med en Stonewall x2-transaktion?



Stonewall x2-strukturen tillför en enorm mängd entropi till transaktionen, vilket förvirrar kedjeanalysen. Sett från utsidan kan en sådan transaktion tolkas som en liten Coinjoin mellan två personer. Men i själva verket är det en betalning. Denna metod skapar därför osäkerheter i kedjeanalysen, eller leder till och med till falska ledtrådar.



Låt oss ta exemplet med Alice, Bob och Boulanger. Transaktionen på blockkedjan skulle se ut så här:



![image](assets/fr/03.webp)



En utomstående observatör som förlitar sig på vanlig kedjeanalysheuristik kan felaktigt dra slutsatsen att "*Alice och Bob har gjort en liten coinjoin, med en UTXO vardera in och två UTXO vardera ut*".



![image](assets/fr/04.webp)



Denna tolkning är felaktig eftersom, som ni vet, en UTXO skickades till Boulanger, Alice har bara en växelutgång och Bob har två.



![image](assets/fr/01.webp)



Även om den utomstående observatören lyckas identifiera paterne för Stonewall x2-transaktionen kommer han inte att ha all information. Han kommer inte att kunna avgöra vilken av de två UTXO:erna med samma belopp som motsvarar betalningen. Han kommer inte heller att kunna avgöra om Alice eller Bob gjorde betalningen. Slutligen kommer han inte att kunna avgöra om de två UTXO:erna som registrerats kommer från två olika personer eller om de tillhör en enda person som har slagit ihop dem. Denna sista punkt beror på att de klassiska Stonewall-transaktionerna, som diskuterats ovan, följer exakt samma mönster som Stonewall x2-transaktionerna. Sett från utsidan och utan ytterligare kontextuell information är det omöjligt att skilja en Stonewall-transaktion från en Stonewall x2-transaktion. De förra är inte samarbetstransaktioner, medan de senare är det. Detta gör att kostnaden blir ännu mer tveksam.



![image](assets/fr/05.webp)




## Hur skapar jag en förbindelse mellan Paynyms?



Som med andra samarbetstransaktioner på Ashigaru (*Cahoots*) innebär Stonewall x2 utbyte av delvis signerade transaktioner mellan avsändaren och samarbetspartnern. Utbytet kan ske manuellt, om du är fysiskt närvarande hos din samarbetspartner, eller automatiskt med hjälp av Sorobans kommunikationsprotokoll.



Om du väljer det andra alternativet måste du upprätta en förbindelse mellan Paynyms innan du kan utföra en Stonewall x2. För att göra detta måste din Paynym "*följa*" din samarbetspartners Paynym, och vice versa. För att ta reda på hur du gör detta kan du följa början av denna andra handledning:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Hur gör jag en Stonewall x2-transaktion på Ashigaru?



För att genomföra en Stonewall x2-transaktion klickar du på bilden av din Paynym i det övre vänstra hörnet av skärmen och öppnar sedan menyn "Samarbeta". Den person som deltar i transaktionen med dig måste göra samma sak, såvida ni inte utbyter QR-koder personligen.



![Image](assets/fr/06.webp)



Du har två alternativ: välj "Initiera" om du är avsändare av betalningen, eller "Delta" om du är den person som samarbetar i transaktionen men varken är betalare eller mottagare.



![Image](assets/fr/07.webp)



Om du har rollen som samarbetspartner är proceduren mycket enkel. För samarbete på distans via Soroban-nätverket klickar du på `Participate`, väljer det konto du vill använda och trycker sedan på `LISTEN FOR CAHOOTS REQUESTS` för att invänta den begäran som betalaren skickar.



![Image](assets/fr/08.webp)



För personligt samarbete via QR-kodskanning går du till startsidan för din wallet, trycker på QR-kodsikonen högst upp på skärmen och skannar sedan QR-koden som tillhandahålls av betalaren som initierar transaktionen.



![Image](assets/fr/09.webp)



Om du har rollen som betalare, dvs. den som initierar transaktionen, går du till menyn "Collaborate" och väljer sedan "Initiate".



![Image](assets/fr/10.webp)



För transaktionstyp, eftersom vi vill utföra en Stonewall x2, väljer du detta alternativ.



![Image](assets/fr/11.webp)



Du kan sedan välja mellan samarbete online (*Cahoots* via *Soroban*) eller samarbete ansikte mot ansikte, med QR-kodutbyte.



![Image](assets/fr/12.webp)



### Cahoots online



Om du har valt alternativet `Online` väljer du din medarbetare från de Paynyms du följer.



![Image](assets/fr/13.webp)



Klicka på `Set up transaction` och välj sedan det konto från vilket du vill göra utlägget.



![Image](assets/fr/14.webp)



På nästa sida anger du transaktionsuppgifterna: adressen till den faktiska mottagaren av betalningen, beloppet som ska skickas och avgiftssatsen. Klicka sedan på "Granska transaktionsinställningarna".



![Image](assets/fr/15.webp)



Kontrollera informationen noggrant, se till att din samarbetspartner lyssnar på *Cahoots*-förfrågningarna och klicka sedan på den gröna knappen `BEGIN TRANSACTION` för att inleda utbytet av PSBTs via Soroban.



![Image](assets/fr/16.webp)



Vänta tills båda deltagarna har signerat transaktionen och sänd den sedan i Bitcoin-nätverket.



![Image](assets/fr/17.webp)



### Diskussioner ansikte mot ansikte



Om du vill utföra växlingen personligen väljer du transaktionstypen `STONEWALL X2` och sedan alternativet `In Person / Manual`.



![Image](assets/fr/18.webp)



Klicka på `Set up transaction` och välj sedan det konto från vilket du vill göra utlägget.



![Image](assets/fr/19.webp)



På nästa sida anger du transaktionsuppgifterna: adressen till den faktiska mottagaren av betalningen, beloppet som ska skickas och avgiftssatsen. Klicka sedan på "Granska transaktionsinställningarna".



![Image](assets/fr/20.webp)



Kontrollera detaljerna och tryck sedan på den gröna knappen `BEGIN TRANSACTION` för att börja växla PSBTs via QR-kodskanning.



![Image](assets/fr/21.webp)



Utbytet sker genom att skanningen växlar med medarbetaren: klicka på "Visa QR-kod" för att visa din QR-kod för din medarbetare, som skannar den. Han klickar sedan på "Visa QR-kod" för att visa sin, och du skannar den med "Starta QR-skanner". Upprepa denna process tills alla fem utbytesstegen har slutförts.



![Image](assets/fr/22.webp)



När alla utbyten har slutförts kontrollerar du transaktionsinformationen och frigör den genom att dra i den gröna pilen längst ned på skärmen.



![Image](assets/fr/23.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/9082f3d989728aacd290535a1ac374ab8c04a241a1d798b378db626dabea7a24). Dess struktur är som följer:



![Image](assets/fr/24.webp)



*Kredit: [mempool.space](https://mempool.space/)*



Vi kan observera två inmatningar från min portfölj, respektive 91 869 sats och 64 823 sats, medan de andra två inmatningarna kommer från min samarbetspartners wallet. På utmatningssidan skickas en UTXO på 100 000 sats` till den faktiska betalningsmottagaren och två UTXO:er på 100 000 sats` och 159 578 sats` återvänder till min samarbetspartners portfölj. För honom är transaktionen neutral, eftersom han återfår hela beloppet av de medel han hade investerat i inmatningen (exklusive kostnaderna för mining som han bidrog till). Slutligen får jag ett utbyte UTXO på 56 270 sats`, vilket motsvarar skillnaden mellan mina totala insatser och betalningen på 100 000 sats` som skickats till mottagaren.



Självklart kan jag beskriva denna struktur eftersom jag själv byggt upp transaktionen. Men för en utomstående observatör är det i allmänhet omöjligt att avgöra vilka UTXO:er som tillhör vilken deltagare, varken i inmatningar eller utmatningar.



För att fördjupa din kunskap om onchain-sekretesshantering på Bitcoin rekommenderar jag att du tar min BTC 204-utbildning på Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c