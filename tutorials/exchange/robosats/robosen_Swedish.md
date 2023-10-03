namn: Robosats

beskrivning: Hur man använder Robosats

![omslag](assets/cover.jpeg)

# Robosats

RoboSats (https://learn.robosats.com/) är ett enkelt sätt att privat utbyta Bitcoin mot nationella valutor. Det förenklar peer-to-peer-upplevelsen och använder blixtfakturor för att minimera förvarings- och förtroendekrav.

![video](https://youtu.be/XW_wzRz_BDI)

## Guide

> Denna guide kommer från Bitocin Q&A (https://bitcoiner.guide/robosats/). Allt beröm till honom, stöd honom där (https://bitcoiner.guide/contribute); BitcoinQ&A är också en bitcoin-mentor. Kontakta honom för handledning!

![bild](assets/0.png)

RoboSats - En enkel och privat P2P-utbyte baserat på Lightning

## Innan du börjar

### Saker du behöver veta

| Jargong          | Definition                                                                                                                                                                                                  |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Robot            | Din automatiskt genererade privata handelsidentitet. Använd inte samma robot mer än en gång eftersom detta kan försämra din integritet.                                                                     |
| Token            | En sträng av slumpmässiga tecken som används för att generera din unika robot.                                                                                                                              |
| Skapare          | En användare som skapar ett erbjudande att köpa eller sälja Bitcoin.                                                                                                                                        |
| Köpare           | En användare som accepterar en annan användares erbjudande att köpa eller sälja Bitcoin.                                                                                                                    |
| Bindning         | En mängd Bitcoin som låses av båda parter som en försäkran om att spela rättvist och fullfölja sin del av handeln. Bindningar utgör vanligtvis 3% av det totala handelsbeloppet och drivs av Hodl-fakturor. |
| Handelsförvaring | Används av säljaren som en metod för att hålla handelsbeloppet i Bitcoin, igen med hjälp av Hodl-fakturor.                                                                                                  |
| Avgifter         | RoboSats tar ut 0,2% av handelsbeloppet, vilket delas mellan både skapare och köpare. Köparen betalar 0,175% och skaparen betalar 0,025%.                                                                   |

## Saker du behöver ha

### En Lightning-plånbok

RoboSats är Lightning-kompatibel, så du kommer att behöva en Lightning-plånbok för att finansiera bindningen och ta emot de köpta sats som köpare. Du bör vara försiktig när du väljer din plånbok, eftersom inte alla är kompatibla med den teknik som används för att göra RoboSats funktionell.

Om du kör en nod är Zeus det bästa alternativet. Om du inte har en egen nod rekommenderar jag starkt Phoenix, en mobil plattformsoberoende plånbok med enkel installation och tillgång till Lightning. Phoenix användes i produktionen av denna guide.

### Lite Bitcoin

Köpare och säljare måste finansiera en bindning innan någon handel kan äga rum. Detta är vanligtvis en mycket liten summa (~3% av handelsbeloppet), men är en förutsättning ändå.

Använder du RoboSats för att köpa dina första sats? Varför inte be en vän att låna dig den lilla summa som krävs för att komma igång!? Om du är på egen hand finns här några andra bra alternativ för att få tag på några noKYC-sats för att komma igång.

### Tillgång till RoboSats

Självklart kommer du att behöva få tillgång till RoboSats! Det finns fyra huvudsakliga sätt att göra detta på:

1. Via Tor-webbläsaren (rekommenderas!)
2. Via en vanlig webbläsare (rekommenderas inte!)
3. Via Android APK
4. Din egen klient

Om du är ny på Tor-webbläsaren kan du lära dig mer och ladda ner den [här](https://www.torproject.org/download/).
En snabb anteckning för iOS-användare som vill komma åt RoboSats via Tor från sina telefoner. "Onion Browser" är inte Tor Browser. Använd istället Orbot + Safari och Orbot + DuckDuckGo.

## Köpa Bitcoin

Följande steg utfördes i maj 2023 med version 0.5.0, åtkomst via Tor-webbläsaren. Stegen bör vara identiska för användare som använder RoboSats via Android APK.

Vid skrivandet av detta genomgår RoboSats fortfarande aktiv utveckling, så gränssnittet kan ändras lite i framtiden, men de grundläggande stegen som krävs för att slutföra handeln bör förbli i stort sett oförändrade.

> När du först laddar RoboSats möts du av denna startsida. Klicka på Start.

![image](assets/2.png)

Generera din token och spara den på en säker plats, som en krypterad anteckningsapp eller lösenordshanterare. Denna token kan användas för att återställa ditt tillfälliga robot-ID om din webbläsare eller app stängs mitt i en handel.

![image](assets/3.png)

Träffa din nya robotidentitet och klicka sedan på Fortsätt.

![image](assets/4.png)

Klicka på Erbjudanden för att bläddra i orderboken. Högst upp på sidan kan du sedan filtrera efter dina preferenser. Se till att notera bindningsprocenten och premien över genomsnittlig växelkurs.

- Välj Köp
- Välj din valuta
- Välj dina betalningsmetoder

![image](assets/5.png)

> Klicka på det erbjudande du vill ta. Ange beloppet (i din valda fiatvaluta) som du vill köpa från säljaren, kontrollera sedan detaljerna en sista gång och klicka på Ta order.

Om säljaren inte är online (markerat med en röd prick på deras profilbild) kommer du att se en varning om att handeln kan ta längre tid än vanligt. Om du fortsätter och säljaren inte agerar i tid kommer du att kompenseras med 50% av deras bindningsbelopp för din bortkastade tid.

![image](assets/6.png)

Nästa steg är att låsa upp din handelsbindning genom att betala fakturan på skärmen. Detta är en hållfaktura som fryser i din plånbok. Den kommer bara att debiteras om du inte slutför din del av handeln.

![image](assets/7.png)

I din Lightning Wallet, skanna QR-koden och betala fakturan.

![image](assets/8.png)

Generera sedan en faktura för det angivna beloppet i din Lightning Wallet och klistra in den i det angivna utrymmet.

![image](assets/9.png)

Vänta på att säljaren låser upp sitt handelsbelopp. När detta sker kommer RoboSats automatiskt att gå vidare till nästa steg där chattfönstret öppnas. Säg hej och be säljaren om deras betalningsinformation för fiat. När den har lämnats, skicka betalningen via den valda metoden och bekräfta detta i RoboSats. All chatt i RoboSats är PGP-krypterad, vilket innebär att bara du och din handelspartner kan läsa meddelandena.

![image](assets/10.png)

När säljaren bekräftar att betalningen har mottagits, släpper RoboSats automatiskt betalningen med hjälp av den tidigare tillhandahållna fakturan.

![image](assets/11.png)

När fakturan är betald är handeln klar och din bindning låses upp. Du kommer sedan att se en sammanfattning av handeln.

![image](assets/12.png)

Kontrollera din Lightning Wallet för bekräftelse på att sats har kommit fram.

![image](assets/13.png)

## Ytterligare funktioner

Förutom att köpa och sälja Bitcoin har RoboSats några andra funktioner som du bör känna till.
Robotgarage
Vill du ha flera affärer igång samtidigt, men vill inte dela samma identitet mellan dem? Inga problem! Klicka på fliken Robot, generera en ytterligare robot och skapa eller ta din nästa order.
![image](assets/14.png)

### Skapa order

Förutom att ta emot någon annans erbjudande kan du skapa ditt eget och vänta på att en annan robot kommer till dig.

- Öppna skaparsidan.
- Ange om din order är att köpa eller sälja Bitcoin.
- Ange beloppet och valutan du vill köpa/sälja med.
- Ange betalningsmetod(er) du är villig att använda.
- Ange det procentuella "premium över marknaden" du är villig att acceptera. Observera att detta kan vara en negativ siffra för att bjuda till ett lägre pris än det nuvarande marknadspriset.
- Klicka på Skapa order.
- Betala Lightning-fakturan för att låsa din Maker Bond.
- Din order är nu aktiv. Luta dig tillbaka och vänta på att någon accepterar den.

![image](assets/15.png)

### Utbetalningar på kedjan

RoboSats fokuserar på Lightning, men köpare har möjlighet att få sina sats till en Bitcoin-adress på kedjan. Köpare kan välja detta alternativ efter att ha låst sin bond. Efter att ha valt på kedjan kommer köparen att se en översikt över avgifterna. De extra avgifterna för denna tjänst inkluderar:

- En bytesavgift som samlas in av RoboSats - Denna avgift är dynamisk och varierar beroende på hur upptagen Bitcoin-nätverket är.
- En gruvavgift för utbetalningstransaktionen - Denna kan konfigureras av köparen.

![image](assets/16.png)

### P2P-byten

RoboSats tillåter användare att byta sats till eller från sin Lightning-plånbok. Klicka helt enkelt på byt-knappen längst upp på erbjudandesidan för att se de aktuella byterbjudandena.

Som köpare av ett "Byt in"-erbjudande skickar du Bitcoin på kedjan till den andra parten och får sats tillbaka, minus de annonserade avgifterna och/eller premierna, till din Lightning-plånbok. Som köpare av ett "Byt ut"-erbjudande skickar du sats via Lightning och får Bitcoin, minus eventuella avgifter och/eller premie, till din adress på kedjan. Användare av Samourai- eller Sparrow-plånboken kan också dra nytta av Stowaway-funktionen för att slutföra ett byte.

RoboSats byterbjudanden kan också inkludera kopplade alternativ till Bitcoin som inkluderar RBTC, LBTC och WBTC. Du bör vara mycket försiktig om du interagerar med dessa tokens eftersom de alla har olika kompromisser. Kopplad Bitcoin är inte Bitcoin!

![image](assets/17.png)

### Kör din egen RoboSats-klient

Umbrel, Citadel och Start9-nodkörare kan installera sin egen RoboSats-klient direkt på sin nod. Fördelarna med att göra det listas som:

- Dramatiskt snabbare laddningstider.
- Säkrare: du kontrollerar vilken RoboSats-klientapp du kör.
- Tillgång till RoboSats säkert från vilken webbläsare/enhet som helst. Ingen anledning att använda TOR om du är på ditt lokala nätverk eller använder VPN: din nodbackend hanterar torifieringen som behövs för anonymisering.
- Möjliggör kontroll över vilken P2P-marknadskoordinator du ansluter till (standard är robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion)

![image](assets/18.png)

## FAQ

### Kan jag bli lurad?

Som köpare kan du öppna en tvist om säljaren inte frigör sats till dig trots att du har skickat det fiat-belopp som krävs för din del av handeln. Om du kan bevisa för RoboSats-arbitratorerna att du faktiskt skickade fiat-beloppet kommer säljarens escrow-fonder och deras handelsgaranti att frigöras till dig. Hur avbryter jag en handel?

Du kan avbryta en handel efter att ha lagt upp din handelsgaranti genom att klicka på knappen "Collaborative Cancel" i handelsmenyn. Om din handelspartner är villig att avbryta kommer du inte att debiteras några avgifter. Men om din handelspartner vill slutföra handeln och du ändå avbryter kommer du att förlora din handelsgaranti.

Fungerar RoboSats med "X" betalningsmetod?

Det finns inga begränsningar för betalningsmetoder i RoboSats. Om du inte ser några erbjudanden i din önskade metod kan du skapa ditt eget erbjudande med den!

Vad lär RoboSats om mig när jag använder det?

Om du använder RoboSats via Tor eller Android-appen lär det sig ingenting alls! Läs mer här.

- Tor skyddar din nätverksintegritet.
- PGP-kryptering håller din handelschatt privat.
- Inga konton innebär en robot per handel. Det betyder att RoboSats inte kan koppla flera affärer till en enda enhet.

Det finns dock vissa förbehåll! Lightning är ganska privat som avsändare, men inte som mottagare. Om du tar emot till din egen Lightning-nod delas din nod-ID i dina fakturor. Detta nod-ID ger alla som känner till det en utgångspunkt för att försöka koppla samman din aktivitet på kedjan. Detta gäller också om en användare väljer att ta emot sin handel via en utbetalning på kedjan.

För att mildra detta kan användare välja att använda en lösning som en Proxy Wallet för Lightning eller Coinjoin för på-kedjan.

Federation

För närvarande finns det en enda RoboSats-koordinator som drivs av RoboSats-utvecklingsteamet. Inom Bitcoin gör varje form av centralisering det lättare för regeringar eller regleringsorgan som kanske inte ser med blida ögon på en specifik tjänst.

Eftersom RoboSats är ett öppen källkodsprojekt kan vem som helst ta koden och börja köra sin egen koordinator. Även om detta i viss utsträckning decentraliserar risken från ett enskilt mål fragmenterar det också en redan tunn likviditetsmarknad.

RoboSats-teamet inser detta och har börjat arbeta med en federerad modell. Som slutanvändare bör detta inte förändra handelsflödet som visas ovan mycket, men det kommer att finnas extra vyer eller skärmar där du kan lägga till eller ta bort olika koordinatorer som dyker upp.

SLUT på guiden
