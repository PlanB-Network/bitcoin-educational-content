---
name: Stonewall x2
description: Förstå och använda Stonewall x2-transaktioner
---
![cover stonewall x2](assets/cover.webp)


*** VARNING:** Efter gripandet av grundarna av Samourai Wallet och beslagtagandet av deras servrar den 24 april fungerar Stonewallx2-transaktioner endast genom att manuellt utbyta PSBT mellan de berörda parterna, förutsatt att båda användarna är anslutna till sin egen Dojo. Det är dock möjligt att dessa verktyg kan återlanseras under de kommande veckorna. Under tiden kan du fortfarande konsultera den här artikeln för att förstå den teoretiska driften av Stonewallx2 och lära dig hur du gör dem manuellt.*


om du funderar på att utföra en Stonewallx2 manuellt är proceduren mycket lik den som beskrivs i denna handledning. Den största skillnaden ligger i valet av typ av Stonewallx2-transaktion: istället för att välja `Online`, klicka på `In Person / Manual`. Sedan måste du manuellt Exchange PSBT:erna för att konstruera Stonewallx2-transaktionen. Om du är fysiskt nära din samarbetspartner kan du skanna QR-koderna successivt. Om ni befinner er på avstånd kan JSON-filer utbytas via en säker kommunikationskanal. Resten av handledningen förblir oförändrad


_Vi följer noga utvecklingen av detta fall och utvecklingen av de tillhörande verktygen. Du kan vara säker på att vi kommer att uppdatera denna handledning när ny information blir tillgänglig._


_Den här handledningen tillhandahålls endast i utbildnings- och informationssyfte. Vi varken stödjer eller uppmuntrar användning av dessa verktyg i kriminella syften. Det är varje användares ansvar att följa de lagar som gäller i deras jurisdiktion._


---

> *Gör varje utgift till en CoinJoin.*

## Vad är en Stonewall x2-transaktion?


Stonewall x2 är en specifik form av Bitcoin-transaktion som syftar till att öka användarens integritet under en utgift genom att samarbeta med en tredje part som inte är involverad i den utgiften. Denna metod simulerar en mini-CoinJoin mellan två deltagare, samtidigt som en betalning görs till en tredje part. Stonewall x2-transaktioner är tillgängliga i både Samourais Wallet-applikation och Sparrow wallet-programvaran. Båda är driftskompatibla.


Dess funktion är relativt enkel: vi använder en UTXO i vår ägo för att göra betalningen och ber om hjälp från en tredje part som också bidrar med en egen UTXO. Transaktionen resulterar i fyra utgångar: två av dem med lika stora belopp, en avsedd för betalningsmottagarens Address, den andra till en Address som tillhör samarbetspartnern. En tredje UTXO returneras till en annan Address som tillhör samarbetspartnern, så att de kan hämta det ursprungliga beloppet (en neutral åtgärd för dem, modulo Mining-avgifter), och en sista UTXO returneras till en Address som tillhör oss, vilket utgör förändringen från betalningen.


Således definieras tre olika roller i Stonewall x2-transaktioner:


- Avsändaren, som gör den faktiska betalningen;
- Samarbetspartnern, som tillhandahåller bitcoins för att förbättra den övergripande anonymiteten i transaktionen, samtidigt som de återfår sina medel i slutet (en neutral åtgärd för dem, modulo Mining-avgifter);
- Mottagaren, som kanske inte är medveten om transaktionens specifika karaktär och helt enkelt förväntar sig en betalning från avsändaren.


Låt oss ta ett exempel för att bättre förstå. Alice är på bageriet för att köpa sin baguette, som kostar 4 000 Sats`. Hon vill betala i bitcoins och samtidigt behålla en viss nivå av integritet för sin betalning. Hon vänder sig därför till sin vän Bob, som hjälper henne med detta.

![schema stonewall x2](assets/en/1.webp)

Genom att analysera denna transaktion kan vi se att bagaren verkligen fick 4 000 Sats` som betalning för baguetten. Alice använde 10 000 Sats` som input och fick 6 000 Sats` som output, vilket resulterade i ett nettosaldo på 4 000 Sats`, vilket motsvarar priset på baguetten. Bob använde 15 000 Sats som input och erhöll två outputs: en på 4 000 Sats och en på 11 000 Sats, vilket resulterade i ett saldo på 0.

I det här exemplet har jag avsiktligt utelämnat Mining-avgifterna för att underlätta förståelsen. I själva verket delas transaktionsavgifterna lika mellan betalaren och medarbetaren.


## Vad är skillnaden mellan Stonewall och Stonewall x2?


En Stonewall X2-transaktion fungerar precis som en Stonewall-transaktion, förutom att den förra är kollaborativ medan den senare inte är det. Som vi har sett innebär en Stonewall X2-transaktion att en tredje part deltar, som är extern till betalningen, och som tillhandahåller sina bitcoins för att förbättra transaktionens integritet. I en typisk Stonewall-transaktion är det avsändaren som tar rollen som samarbetspartner.


Låt oss återgå till vårt exempel med Alice på bageriet. Om hon inte kunde hitta någon som Bob för att följa med henne i hennes utgift, kunde hon ha gjort en Stonewall-transaktion ensam. Således skulle de två ingående UTXO:erna ha varit hennes, och hon skulle ha fått 3 vid utgången.

![transaction stonewall](assets/en/2.webp)


Från en extern synvinkel skulle transaktionsmönstret ha förblivit detsamma.

![Stonewall or Stonewall x2?](assets/en/5.webp)

Därför bör logiken vara som följer när man använder ett Samourai-utgiftsverktyg:


- Om handlaren inte stöder PayJoin Stowaway kan en samarbetstransaktion göras med en annan person som är extern till betalningen med hjälp av Stonewall x2.
- Om det inte går att hitta någon som kan göra en Stonewall x2-transaktion kan en Stonewall-transaktion göras ensam, vilket efterliknar beteendet hos en Stonewall x2-transaktion.
- Det sista alternativet är att göra en transaktion med JoinBot, en server som underhålls av Samourai, som på begäran kan agera som samarbetspartner i en Stonewall x2-transaktion.


Om du vill hitta en samarbetspartner som är villig att hjälpa dig i en Stonewall X2-transaktion kan du också besöka denna Telegram-grupp (inofficiell) som underhålls av Samourai-användare för att ansluta avsändare och samarbetspartners: [Make Every Spend a CoinJoin] (https://t.me/EverySpendACoinjoin).


[**-> Läs mer om Stonewall-transaktioner**](https://planb.network/tutorials/privacy/On-Chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


## Vad är syftet med en Stonewall x2-transaktion?


Stonewall x2-strukturen tillför en betydande mängd entropi till transaktionen och förvirrar kedjeanalysen. Från utsidan kan en sådan transaktion tolkas som en liten CoinJoin mellan två individer. Men i själva verket är det en betalning. Denna metod skapar osäkerheter i kedjeanalysen och leder till och med till falska ledtrådar.


Låt oss gå tillbaka till exemplet med Alice, Bob och Baker. Transaktionen på Blockchain skulle se ut så här:

![stonewall x2 public](assets/en/3.webp)

En extern observatör som förlitar sig på heuristik för analys av vanliga kedjor kan felaktigt dra slutsatsen att "Alice och Bob utförde en liten CoinJoin, med en UTXO vardera som ingång och två UTXO vardera som utgång."![misstolkning stonewall x2](assets/en/4.webp)

Denna tolkning är felaktig eftersom, som ni vet, en UTXO skickades till bagaren, Alice endast har en ändringsutgång och Bob har två.

![transaction stonewall x2](assets/en/1.webp)

Även om den externa observatören lyckas identifiera mönstret för Stonewall x2-transaktionen kommer han eller hon inte att ha all information. De kommer inte att kunna avgöra vilken av de två UTXO:erna med samma belopp som motsvarar betalningen. Vidare kommer de inte att kunna veta om det är Alice eller Bob som har gjort betalningen. Slutligen kommer de inte att kunna avgöra om de två inmatade UTXO:erna kommer från två olika personer eller om de tillhör en enda person som slog samman dem. Den sista punkten beror på att klassiska Stonewall-transaktioner, som vi diskuterade ovan, följer exakt samma mönster som Stonewall x2-transaktioner. Från utsidan och utan ytterligare information om sammanhanget är det omöjligt att skilja en Stonewall-transaktion från en Stonewall x2-transaktion. De förra är dock inte samarbetstransaktioner, medan de senare är det. Detta bidrar till ännu mer tvivel om denna kostnad.

![Stonewall or Stonewall x2 ?](assets/en/5.webp)



## Hur skapar man en koppling mellan Paynyms för att kunna samarbeta via Soroban?


Precis som med andra samarbetstransaktioner på Samourai (*Cahoots*) innebär utförandet av en Stonewall x2 Exchange av delvis signerade transaktioner mellan avsändaren och samarbetspartnern. Denna Exchange kan göras manuellt, om du befinner dig fysiskt hos din samarbetspartner, eller automatiskt genom Sorobans kommunikationsprotokoll.


Om du väljer det andra alternativet måste du upprätta en förbindelse mellan Paynyms innan du kan utföra en Stonewall x2. För att göra detta måste din Paynym "följa" din samarbetspartners Paynym, och vice versa.


**Tillgång till medarbetarens Paynym:**


För att börja är det nödvändigt att få betalningskoden för din medarbetares Paynym. I Samourai Wallet-applikationen måste din medarbetare trycka på ikonen för sin Paynym (den lilla roboten) längst upp till vänster på skärmen och sedan klicka på sitt Paynym-smeknamn, som börjar med `+...`. Till exempel är mitt `+namelessmode0aF`.


![samourai paynym](assets/notext/6.webp)

Om din medarbetare använder Sparrow wallet ska hen klicka på fliken "Verktyg" och sedan på "Visa PayNym".![paynym Sparrow](assets/notext/7.webp)

**Följande din medarbetares PayNym från Samourai Wallet:**


Om du använder Samourai Wallet startar du programmet och öppnar menyn "PayNyms" på samma sätt. Om det är första gången du använder ditt PayNym måste du få fram dess identifierare.


![request paynym samourai](assets/notext/8.webp)


Klicka sedan på det blå "+" längst ner till höger på skärmen.

![add collaborator paynym](assets/notext/9.webp)

Du kan sedan klistra in din medarbetares betalningskod genom att välja "PASTE PAYMENT CODE", eller öppna kameran för att skanna deras QR-kod genom att trycka på "SCAN QR CODE".

![paste paynym identifier](assets/notext/10.webp)


Klicka på knappen "FOLLOW".

![follow paynym](assets/notext/11.webp)

Bekräfta genom att klicka på "YES".

![confirm follow paynym](assets/notext/12.webp)

Programvaran kommer sedan att erbjuda dig en "CONNECT"-knapp. Det är inte nödvändigt att klicka på den här knappen för vår handledning. Detta steg krävs endast om du planerar att göra betalningar till den andra PayNym som en del av BIP47, vilket inte är relaterat till vår handledning.

![connect paynym](assets/notext/13.webp)

När ditt PayNym följer din medarbetares PayNym upprepar du processen i motsatt riktning så att din medarbetares PayNym också kan följa dig. Du kan sedan utföra en Stonewall x2-transaktion.


**Följer din medarbetares PayNym från Sparrow wallet:**


Om du använder Sparrow wallet, öppna din Wallet och gå till menyn "Show PayNym". Om du använder ditt PayNym för första gången måste du skaffa en identifierare genom att klicka på "Retrieve PayNym".

![request paynym sparrow](assets/notext/14.webp)

Ange sedan din medarbetares PayNym-identifierare (antingen smeknamnet "+..." eller betalningskoden "PM...") i rutan "Find Contact" och klicka på knappen "Add Contact".

![add contact paynym](assets/notext/15.webp)

Programvaran kommer då att erbjuda dig en "Link Contact" -knapp. Det är inte nödvändigt att klicka på den här knappen för vår handledning. Detta steg krävs endast om du planerar att göra betalningar till den angivna PayNym som en del av BIP47, vilket inte är relaterat till vår handledning.


När ditt PayNym följer din medarbetares PayNym upprepar du processen i motsatt riktning så att din medarbetares PayNym också kan följa dig. Du kan sedan utföra en Stonewall x2-transaktion.

## Hur gör man en Stonewall x2-transaktion på Samourai Wallet?


Om du har slutfört de tidigare stegen för att ansluta Paynyms är du äntligen redo att göra Stonewall x2-transaktionen! För att göra detta, följ vår videohandledning på Samourai Wallet:

![Stonewall x2 Tutorial - Samourai Wallet](https://youtu.be/89oYE1Hw3Fk?si=QTqUZ6IypiR6PPMr)


## Hur gör man en Stonewall x2-transaktion på Sparrow wallet?


Om du har slutfört de tidigare stegen för att ansluta Paynyms är du äntligen redo att göra Stonewall x2-transaktionen! För att göra detta, följ vår videohandledning på Sparrow wallet:

![Stonewall x2 Tutorial - Sparrow Wallet](https://youtu.be/mO3Xpp34Hhk?si=bfYiTl0Gxjs9sNQq)


**Externa resurser:**


- https://sparrowwallet.com/docs/spending-privately.html;
- https://docs.samourai.io/en/spend-tools#stonewallx2.