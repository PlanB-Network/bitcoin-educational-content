---
name: Robosats

description: Hur man använder Robosats
---

![cover](assets/cover.webp)


RoboSats (https://learn.robosats.com/) är ett enkelt sätt att privat Exchange Bitcoin för nationella valutor Det förenklar peer-to-peer-upplevelsen och använder sig av blixthållningsfakturor för att minimera kraven på förvaring och förtroende.


![video](https://youtu.be/XW_wzRz_BDI)


## Guide


** Notera:** Den här guiden är från Bitocin Q&A (https://bitcoiner.guide/robosats/). All kredit till honom, du kan stödja honom [här](https://bitcoiner.guide/contribute); BitcoinQ&A är också en Bitcoin-mentor. Kontakta honom för mentorskap!


![image](assets/0.webp)


RoboSats - En enkel och privat blixtbaserad P2P Exchange


## Innan du börjar


### Saker du behöver veta


| Jargon       | Definition                                                                                                                                                                                     |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Robot        | Your automatically generated private trade identity. Do not re-use the same robot more than once as this can degrade your privacy.                                                             |
| Token        | A string of random characters used to generate your unique robot.                                                                                                                              |
| Maker        | A user who creates an offer to buy or sell Bitcoin.                                                                                                                                            |
| Taker        | A user who takes another user up on their offer to buy or sell Bitcoin.                                                                                                                        |
| Bond         | An amount of Bitcoin locked up by both peers as a pledge to play fair and complete their part of the trade. Bonds are typically 3% of the total trade amount and are powered by Hodl Invoices. |
| Trade Escrow | Used by the seller as a method of holding the trade amount of Bitcoin, again using Hodl Invoices.                                                                                              |
| Fees         | RoboSats charges 0.2% of the trade amount, which is split between both maker and taker. The taker pays 0.175% and the maker pays 0.025%.                                                       |

## Saker du behöver ha


### En blixt Wallet


RoboSats är Lightning native, så du kommer att behöva en Lightning Wallet för att finansiera obligationen och ta emot den köpta Sats som köpare. Du bör vara försiktig när du väljer din Wallet, på grund av den teknik som används för att få RoboSats att fungera är inte alla kompatibla.


Om du är en node runner är Zeus det absolut bästa alternativet. Om du inte har en egen nod rekommenderar jag starkt Phoenix, en plattformsoberoende mobil Wallet med enkel installation och tillgång till Lightning. Phoenix användes vid produktionen av den här guiden.


### Några Bitcoin


Köpare och säljare måste finansiera en obligation innan någon handel kan äga rum. Detta är vanligtvis ett mycket litet belopp (~3% av handelsbeloppet), men är ändå en förutsättning.


Använda RoboSats för att köpa din första Sats? Varför inte få en vän att låna dig det lilla belopp som krävs för att komma igång? Om du flyger solo finns det några andra bra alternativ för att få lite noKYC Sats för att komma igång.


### Tillgång till RoboSats


Självklart måste du ha tillgång till RoboSats! Det finns fyra huvudsakliga sätt att göra detta på:


1. Via Tor Browser (rekommenderas!)

2. Via en vanlig webbläsare (rekommenderas inte!)

3. Via APK för Android

4. Din egen kund


Om du inte känner till Tor-webbläsaren tidigare kan du läsa mer och ladda ner den [här] (https://www.torproject.org/download/).


En snabb notering för iOS-användare som vill komma åt RoboSats via Tor från sina telefoner. "Onion Browser" är inte Tor Browser. Använd istället Orbot + Safari och Orbot + DuckDuckGo.


## Köp av Bitcoin


Följande steg genomfördes i maj 2023 med version 0.5.0, åtkommen via Tor-webbläsaren. Stegen bör vara identiska för användare som får tillgång till RoboSats via Android APK.


I skrivande stund är RoboSats fortfarande under aktiv utveckling, så Interface kan förändras lite i framtiden, men de grundläggande stegen som krävs för att slutföra handeln bör förbli i stort sett oförändrade.


**När du först laddar RoboSats kommer du att mötas av den här målsidan. Klicka på Start.


![image](assets/2.webp)


generate din token och förvara den på ett säkert ställe, t.ex. i en krypterad anteckningsapp eller lösenordshanterare. Denna token kan användas för att återställa ditt tillfälliga Robot-ID i händelse av att din webbläsare eller app stängs mitt under en handel.


![image](assets/3.webp)


Träffa din nya robotidentitet och klicka sedan på Fortsätt.


![image](assets/4.webp)


Klicka på Erbjudanden för att bläddra i orderboken. Längst upp på sidan kan du sedan filtrera efter dina preferenser. Var noga med att notera obligationsprocenten och premien jämfört med den genomsnittliga Exchange-räntan.



- Välj taggen "Köp
- Välj din valuta
- Välj din(a) betalningsmetod(er)


![image](assets/5.webp)


**Anmärkning:** klicka på det erbjudande du vill ta. Ange det belopp (i din valda fiatvaluta) som du vill köpa från säljaren, gör en sista kontroll av detaljerna och klicka på "Ta order".


Om säljaren inte är online (markerad med en röd prick på profilbilden) ser du en varning om att affären kan ta längre tid än vanligt. Om du fortsätter och säljaren inte gör affären i tid får du 50 % av obligationssumman i ersättning för den tid du har slösat bort.


![image](assets/6.webp)


Därefter måste du låsa upp din handelsobligation genom att betala Invoice på skärmen. Detta är en håll-Invoice som fryser i din Wallet. Den kommer endast att debiteras om du misslyckas med att slutföra din del av handeln.


![image](assets/7.webp)


I din blixt Wallet, skanna QR-koden och betala Invoice.


![image](assets/8.webp)


Därefter i din blixt Wallet generate en Invoice för det belopp som visas och klistra in i det utrymme som tillhandahålls.


![image](assets/9.webp)


Vänta på att säljaren låser sitt handelsbelopp. När detta sker kommer RoboSats automatiskt att gå vidare till nästa steg där chattfönstret öppnas. Säg hej och be säljaren om deras fiat-betalningsinformation. När du har fått informationen skickar du betalningen via den valda metoden och bekräftar sedan detta i RoboSats. All chatt i RoboSats är PGP-krypterad, vilket innebär att endast du och din handelspartner kan läsa meddelandena.


![image](assets/10.webp)


När säljaren har bekräftat mottagandet av betalningen frigör RoboSats automatiskt betalningen med hjälp av Invoice som angavs tidigare.


![image](assets/11.webp)


När Invoice är betald är affären avslutad och din obligation är upplåst. Du kommer sedan att se en handelssammanfattning.


![image](assets/12.webp)


Kontrollera din Lightning Wallet för bekräftelse på att Sats har anlänt.


![image](assets/13.webp)


## Ytterligare funktioner


Förutom det uppenbara köpet och försäljningen av Bitcoin har RoboSats några andra funktioner som du bör känna till.

Robot Garage


Vill du ha flera affärer igång samtidigt, men vill inte dela samma identitet mellan dem? Det är inget problem! Klicka på fliken Robot, generate en ytterligare robot och skapa eller ta din nästa order.


![image](assets/14.webp)


### Skapa beställningar


Förutom att ta någon annans erbjudande kan du skapa ditt eget och vänta på att en annan robot ska komma till dig.



- Öppna sidan Skapa.
- Definiera om din order är att köpa eller sälja Bitcoin.
- Ange det belopp och den valuta som du vill köpa/sälja med.
- Ange den eller de betalningsmetoder som du är villig att använda.
- Ange den % för "Premie över marknadspris" som du är villig att acceptera. Observera att detta kan vara en negativ siffra för att bjuda med rabatt jämfört med det aktuella marknadspriset.
- Klicka på Skapa order.
- Betala Lightning Invoice för att låsa din Maker Bond.
- Din order är nu i realtid. Luta dig tillbaka och vänta på att någon ska acceptera den.


![image](assets/15.webp)


### On-Chain-utbetalningar


RoboSats är Lightning-fokuserad, men köpare har möjlighet att få sin Sats till en On-Chain Bitcoin Address. Köpare kan välja detta alternativ efter att ha låst upp sin obligation. Efter att ha valt On-Chain kommer köparen att se en översikt över avgifterna. De extra avgifterna för denna tjänst inkluderar:



- En swap-avgift som samlas in av RoboSats - Denna avgift är dynamisk och rör sig beroende på hur upptaget Bitcoin-nätverket är.
- En Mining-avgift för utbetalningstransaktionen - Detta kan konfigureras av köparen.


![image](assets/16.webp)


### P2P Swappar


RoboSats tillåter användare att byta Sats till eller från sin Lightning Wallet. Klicka bara på bytesknappen högst upp på erbjudandesidan för att se de aktuella byteserbjudandena.


Som köpare av ett "Swap In"-erbjudande skickar du On-Chain Bitcoin till motparten och får tillbaka Sats, minus de annonserade avgifterna och/eller premierna, till din Lightning Wallet. Som köpare av ett "Swap Out"-erbjudande skickar du Sats via Lightning och får Bitcoin, minus eventuella avgifter och/eller premier, till din On-Chain Address. Samourai- eller Sparrow Wallet-användare kan också utnyttja Stowaway-funktionen för att slutföra ett byte.


RoboSats byteserbjudanden kan också innehålla peggade alternativ till Bitcoin som inkluderar RBTC, LBTC och WBTC. Du bör vara extremt försiktig om du interagerar med dessa tokens eftersom de alla kommer med olika avvägningar. Pegged Bitcoin är inte Bitcoin!


![image](assets/17.webp)


### Kör din egen RoboSats-klient


Umbrel-, Citadel- och Start9-nodlöpare kan installera sin egen RoboSats-klient direkt på sin nod. Fördelarna med att göra detta är följande:



- Dramatiskt snabbare laddningstider.
- Säkrare: du kontrollerar vilken RoboSats-klientapp du kör.
- Få säker åtkomst till RoboSats från alla webbläsare/enheter. Du behöver inte använda TOR om du är på ditt lokala nätverk eller använder VPN: din nodbackend hanterar den torifiering som behövs för anonymisering.
- Tillåter kontroll över vilken P2P-marknadskoordinator du ansluter till (standard är robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion)


![image](assets/18.webp)


## VANLIGA FRÅGOR


### Kan jag bli lurad?


Om du som köpare har skickat de fiat som krävs för din del av affären, men säljaren inte släpper Sats till dig, kan du öppna en tvist. Om du under denna tvistprocess kan bevisa för RoboSats skiljedomare att du skickade fiat, kommer säljarens spärrade medel och deras handelsgaranti att frigöras till dig.

Hur avbryter jag en affär?


Du kan avbryta en handel efter att du har lagt upp din obligation genom att klicka på knappen Collaborative Cancel i handelsmenyn. Om din handelspartner är nöjd med att avbryta kommer du inte att ådra dig några avgifter. Men om din handelspartner vill slutföra affären och du ändå avbryter, förlorar du din handelsgaranti.


### Fungerar RoboSats med "X" betalningsmetod?


Det finns inga begränsningar för betalningsmetoder i RoboSats. Om du inte ser några erbjudanden med den metod du vill använda kan du skapa ett eget erbjudande med den!


![image](assets/19.webp)


### Vad lär sig RoboSats om mig när jag använder den?


Om du använder RoboSats via Tor eller Android-appen behöver du inte göra någonting alls! Läs mer här.



- Tor skyddar din nätverksintegritet.
- PGP-kryptering håller din handelschatt privat.
- Inga konton innebär en robot per handel. Detta innebär att RoboSats inte kan korrelera flera affärer till en enda enhet.


Det finns dock några förbehåll! Lightning är ganska privat som avsändare, men inte som mottagare. Om du tar emot till din egen Lightning-nod delas ditt nod-ID i dina fakturor. Detta nod-ID ger alla som känner till det en utgångspunkt för att försöka länka din On-Chain-aktivitet. Detta gäller även om en användare väljer att ta emot sin handel via en On-Chain-utbetalning.


För att mildra detta kan användare välja att använda en lösning som en proxy Wallet för Lightning eller CoinJoin för On-Chain.


### Federation


Just nu finns det en enda RoboSats-koordinator som drivs av RoboSats-utvecklargruppen. I Bitcoin gör alla former av centralisering det lättare för regeringar eller tillsynsmyndigheter som kanske inte ser med blida ögon på en specifik tjänst.


Eftersom RoboSats är ett projekt med öppen källkod kan vem som helst ta koden och börja köra sin egen koordinator. Även om detta i viss mån decentraliserar risken bort från ett enda mål, fragmenterar det också en redan tunn likviditetsmarknad.


RoboSats-teamet inser detta och har påbörjat arbetet med en federerad modell. Som slutanvändare bör detta inte förändra handelsflödet som visas ovan särskilt mycket, men det kommer att finnas extra vyer eller skärmar för att du ska kunna lägga till eller ta bort olika koordinatorer som uppstår.


Slut på guiden

https://bitcoiner.guide/robosats/