---
name: Stonewall
description: Förstå och använda Stonewall-transaktioner
---
![cover stonewall](assets/cover.webp)


*** VARNING:** Efter arresteringen av grundarna av Samourai Wallet och beslagtagandet av deras servrar den 24 april, kräver nu användningen av Samourai Wallet-appen en anslutning till din egen Dojo för att fungera korrekt. Bortsett från detta påverkas inte Stonewall-transaktioner alls och kan fortfarande utföras utan problem. Faktum är att dessa typer av transaktioner utförs autonomt, utan behov av externt samarbete eller anslutning via Soroban.*


_Vi följer noga utvecklingen av detta fall och utvecklingen av de tillhörande verktygen. Du kan vara säker på att vi kommer att uppdatera denna handledning när ny information blir tillgänglig._


_Den här handledningen tillhandahålls endast i utbildnings- och informationssyfte. Vi varken stödjer eller uppmuntrar användning av dessa verktyg i kriminella syften. Det är varje användares ansvar att följa de lagar som gäller i deras jurisdiktion._


---

> *Bryt antagandena i Blockchain-analysen med matematiskt bevisbar tveksamhet mellan avsändare och mottagare av dina transaktioner*

## Vad är en Stonewall-transaktion?

Stonewall är en specifik form av Bitcoin-transaktion som syftar till att öka användarnas integritet under en transaktion genom att efterlikna en CoinJoin mellan två parter, utan att faktiskt vara en sådan. Faktum är att den här transaktionen inte är ett samarbete. En användare kan konstruera den ensam och bara använda sina egna UTXO:er som ingångar. Därför kan du skapa en Stonewall-transaktion för vilket tillfälle som helst utan att behöva samordna med en annan användare.


En Stonewall-transaktion fungerar på följande sätt: som input använder avsändaren 2 UTXO som tillhör dem. Som utdata ger transaktionen 4 utdata, varav 2 kommer att vara exakt samma belopp. De andra 2 kommer att vara förändring. Av de 2 utflödena med samma belopp kommer endast ett faktiskt att gå till betalningsmottagaren.


Det finns bara två roller i en Stonewall-transaktion:


- Avsändaren, som gör den faktiska betalningen;
- Mottagaren, som kanske inte är medveten om transaktionens specifika karaktär och helt enkelt förväntar sig en betalning från avsändaren.


Låt oss ta ett exempel för att förstå denna transaktionsstruktur. Alice är på bageriet för att köpa sin baguette, som kostar 4 000 Sats`. Hon vill betala i bitcoins och samtidigt upprätthålla en viss nivå av integritet i sin betalning. Därför beslutar hon sig för att skapa en Stonewall-transaktion för betalningen.

![transaction stonewall bakery](assets/en/1.webp)

Genom att analysera denna transaktion kan vi se att bagaren verkligen fick 4 000 Sats` som betalning för baguetten. Alice använde 2 UTXO:er som input: en på 10 000 Sats och en på 15 000 Sats. Som utgång fick hon 3 UTXO: en på 4 000 Sats`, en på 6 000 Sats` och en på 11 000 Sats`. Alice har ett nettosaldo på 4 000 Sats` i denna transaktion, vilket motsvarar priset på baguetten.


I det här exemplet har jag avsiktligt utelämnat Mining-avgifterna för att underlätta förståelsen. I verkligheten täcks transaktionsavgifter helt av avsändaren.


## Vad är skillnaden mellan Stonewall och Stonewall x2?

Stonewall-transaktionen fungerar på samma sätt som StonewallX2-transaktionen, med den enda skillnaden att den senare kräver samarbete, till skillnad från den klassiska Stonewall-transaktionen, därav beteckningen "x2". Stonewall-transaktionen kan faktiskt utföras utan att kräva externt samarbete: avsändaren kan utföra den utan hjälp av någon annan person. För en Stonewall x2-transaktion ansluter sig dock ytterligare en deltagare, kallad "kollaboratör", till processen. Samarbetspartnern bidrar med sina egna bitcoins som input, tillsammans med avsändarens, och får hela summan som output (minus Mining-avgifter).


Låt oss återgå till vårt exempel med Alice på bageriet. Om hon hade velat göra en Stonewall x2-transaktion skulle Alice ha behövt samarbeta med Bob (en tredje part) när hon skapade transaktionen. De skulle var och en ha tillhandahållit en inmatning UTXO. Bob skulle sedan ha fått hela beloppet av sin insats som output. Bagaren skulle ha fått betalt för sin baguette på samma sätt som i Stonewall-transaktionen, medan Alice skulle ha fått tillbaka sitt ursprungliga saldo, minus kostnaden för baguetten.

![transaction stonewall x2](assets/en/2.webp)


Ur ett externt perspektiv skulle transaktionsmönstret ha förblivit exakt detsamma.

![Stonewall or Stonewall x2 ?](assets/en/3.webp)


Sammanfattningsvis har transaktionerna Stonewall och Stonewall x2 en identisk struktur. Skillnaden mellan de två ligger i deras samarbetskaraktär. Stonewall-transaktionen utvecklas individuellt, utan behov av samarbete. Stonewall x2-transaktionen är däremot beroende av samarbete mellan två individer för att kunna genomföras.


[**-> Läs mer om Stonewall x2-transaktioner**](https://planb.network/tutorials/privacy/On-Chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)


## Vad är syftet med en Stonewall-transaktion?

Stonewall-strukturen tillför en betydande mängd entropi till transaktionen och skymmer kedjeanalysen. Från ett externt perspektiv kan en sådan transaktion tolkas som en liten CoinJoin mellan två personer. Men i verkligheten är det, precis som Stonewall x2-transaktionen, en betalning. Denna metod skapar därför osäkerheter i kedjeanalysen och kan till och med leda till falska ledtrådar.


Låt oss återgå till Alices exempel på bageriet. Transaktionen på Blockchain skulle se ut på följande sätt:

![Stonewall or Stonewall x2 ?](assets/en/4.webp)

En extern observatör som förlitar sig på vanlig heuristik för kedjeanalys kan felaktigt dra slutsatsen att "*två personer har utfört en liten CoinJoin, med en UTXO vardera som input och två UTXO vardera som output*".

![Stonewall or Stonewall x2 ?](assets/en/5.webp)

Denna tolkning är felaktig eftersom, som du vet, en UTXO skickades till bagaren, de 2 UTXO:erna i inmatningen kommer från Alice och hon fick 3 förändringsutmatningar.


![transaction stonewall baker](assets/en/1.webp)

Även om en utomstående observatör lyckas identifiera mönstret i Stonewall-transaktionen kommer denne inte att ha tillgång till all information. De kommer inte att kunna avgöra vilken av de två UTXO:erna med samma belopp som motsvarar betalningen. Dessutom kommer de inte att kunna avgöra om de två UTXO:erna i inbetalningen kommer från två olika personer eller om de tillhör en enda person som slog samman dem. Den sista punkten beror på att Stonewall x2-transaktioner, som vi talade om ovan, följer exakt samma mönster som Stonewall-transaktioner. Från utsidan och utan ytterligare information om sammanhanget är det omöjligt att skilja en Stonewall-transaktion från en Stonewall x2-transaktion. De förra är dock inte samarbetstransaktioner, medan de senare är det. Detta bidrar till ännu mer tvivel om denna utgift.

![Stonewall or Stonewall x2 ?](assets/en/3.webp)

## Hur gör man en Stonewall-transaktion på Samourai Wallet?

Till skillnad från transaktioner med Stowaway eller Stonewall x2 (cahoots) kräver Stonewall-transaktionen inte att Paynyms används. Den kan göras direkt, utan några förberedande steg. För att göra detta, följ vår videohandledning på Samourai Wallet:

![Stonewall Tutorial - Samourai Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)


## Hur gör man en Stonewall-transaktion på Sparrow Wallet?

Till skillnad från transaktioner med Stowaway eller Stonewall x2 (cahoots) kräver Stonewall-transaktionen inte att Paynyms används. Den kan göras direkt, utan några förberedande steg. För att göra detta, följ vår videohandledning på Sparrow Wallet:

![Stonewall Tutorial - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)



**Externa resurser:**


- https://docs.samourai.io/en/spend-tools#stonewall.