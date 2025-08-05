---
name: Blockstream Green - 2FA
description: Ställer upp en 2/2 Multisig på Green Wallet
---
![cover](assets/cover.webp)

___

***Observera:** Från och med maj 2025 kommer det inte längre vara möjligt att aktivera nya konton skyddade med tvåfaktorsautentisering (2FA). Denna funktion är endast tillgänglig för användare som tidigare har aktiverat denna typ av konto.*

___

En Software Wallet är en applikation som installeras på en dator, smartphone eller annan internetansluten enhet och som gör att du kan hantera och säkra dina Bitcoin Wallet-nycklar. Till skillnad från hårdvaruplånböcker, som isolerar privata nycklar, fungerar "Hot"-plånböcker därför i en miljö som potentiellt är utsatt för cyberattacker, vilket ökar risken för piratkopiering och stöld.

Mjukvaruplånböcker bör användas för att hantera rimliga mängder bitcoins, särskilt för vardagliga transaktioner. De kan också vara ett intressant alternativ för personer med begränsade Bitcoin-tillgångar, för vilka en investering i en Hardware Wallet kan verka oproportionerlig. Deras ständiga exponering mot internet gör dem dock mindre säkra för att lagra dina långsiktiga besparingar eller stora fonder. För det senare är det bäst att välja säkrare lösningar, till exempel hårdvaruplånböcker.

I den här handledningen visar jag hur du kan förbättra säkerheten för en Hot Wallet med hjälp av alternativet "*2FA*" på Blockstream Green.


![GREEN 2FA MULTISIG](assets/fr/01.webp)


## Introduktion av Blockstream Green


Blockstream Green är en Software Wallet som är tillgänglig på mobil och dator. Denna Wallet var tidigare känd som *Green Address* och blev ett Blockstream-projekt efter förvärvet 2016.


Green är en särskilt lättanvänd applikation, vilket gör den intressant för nybörjare. Den erbjuder alla viktiga funktioner i en bra Bitcoin Wallet, inklusive RBF (* Replace-by-fee*), ett Tor-anslutningsalternativ, möjligheten att ansluta din egen nod, SPV (* Enkel betalningsverifiering*), myntmärkning och kontroll.


Blockstream Green stöder också Liquid Network, en Bitcoin Sidechain utvecklad av Blockstream för snabb, Confidential Transactions utanför huvud Blockchain. I den här handledningen fokuserar vi uteslutande på Bitcoin, men jag har också gjort en annan handledning för att lära mig hur man använder Liquid på Green :


https://planb.network/tutorials/wallet/mobile/blockstream-green-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## 2/2 Multisig tillval (2FA)


På Green kan du skapa en klassisk "*singlesig*" Hot Wallet. Men du har också möjlighet att välja "*2FA Multisig*", vilket förbättrar säkerheten för din Hot Wallet utan att komplicera den dagliga hanteringen.


Så du kommer att sätta upp en 2/2 Multisig Wallet, vilket innebär att varje transaktion kommer att kräva signatur av två nycklar. Den första nyckeln, som härrör från din Mnemonic-fras på 12 eller 24 ord, säkras lokalt med en PIN-kod på din telefon. Du har full kontroll över den här nyckeln. Den andra nyckeln finns på Blockstreams servrar och dess användning för att signera kräver autentisering, vilket kan uppnås via en kod som tas emot via e-post, SMS, telefonsamtal eller, som vi kommer att se i den här handledningen, via en autentiseringsapplikation (Authy, Google Authenticator, etc.).


För att säkerställa din autonomi i händelse av Blockstream-fel (till exempel i händelse av företagskonkurs eller förstörelse av servrarna som håller den andra nyckeln) tillämpas en tidslåsmekanism på din Multisig. Denna mekanism omvandlar 2/2 Multisig till en 1/2 Multisig efter ungefär ett år (eller exakt 51 840 block, men detta värde är modifierbart), varefter din Wallet endast behöver din lokala nyckel för att spendera bitcoins. Så om du förlorar åtkomst till Blockstreams servrar eller 2FA-autentisering behöver du bara vänta högst ett år för att fritt kunna använda dina bitcoins med din applikation utan att vara beroende av Blockstream.


![GREEN 2FA MULTISIG](assets/fr/02.webp)


Den här metoden ökar säkerheten för din Hot Wallet avsevärt, samtidigt som du har kontroll över dina bitcoins och underlättar den dagliga användningen av dem. Det krävs dock regelbundna uppdateringar av tidslåset för att upprätthålla säkerheten för 2FA. Nedräkningen på 360 dagar, under vilken dina medel skyddas av 2FA, börjar så snart du tar emot bitcoins. Om du 360 dagar efter detta mottagande inte har genomfört en transaktion med dessa medel kommer dina bitcoins endast att skyddas av din lokala nyckel, utan 2FA.


Denna begränsning gör 2FA-alternativet mer lämpligt för en Wallet som spenderar, där regelbundna transaktioner automatiskt förnyar tidslås. För en Wallet med långsiktigt sparande kan detta vara problematiskt, eftersom du måste tänka på att göra en sveptransaktion till dig själv varje år innan tidslåset löper ut.


En annan nackdel med den här säkerhetsmetoden är att du måste använda skriptmallar för minoriteter. Detta innebär att saker och ting blir mer komplicerade ur integritetssynpunkt: väldigt få personer använder samma typ av skript som du, vilket gör det lättare för en utomstående observatör att identifiera ditt Wallet-fingeravtryck. Dessutom kommer dessa skript att medföra högre transaktionskostnader på grund av deras större storlek.


Om du föredrar att inte använda 2FA-alternativet och helt enkelt vill ställa in en "*singlesig*" Wallet på Green, inbjuder jag dig att konsultera denna andra handledning :


https://planb.network/tutorials/wallet/mobile/blockstream-green-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## Installera och konfigurera Blockstream Green-programvara


Det första steget är naturligtvis att ladda ner Green-applikationen. Gå till din applikationsbutik:



- [För Android] (https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [For Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![GREEN 2FA MULTISIG](assets/fr/03.webp)


För Android-användare kan du också installera applikationen via filen `.apk` [tillgänglig på Blockstreams GitHub] (https://github.com/Blockstream/green_android/releases).


![GREEN 2FA MULTISIG](assets/fr/04.webp)


Starta programmet och kryssa sedan i rutan "Jag accepterar villkoren...*".


![GREEN 2FA MULTISIG](assets/fr/05.webp)


När du öppnar Green för första gången visas startskärmen utan en konfigurerad Wallet. Senare, om du skapar eller importerar plånböcker, kommer de att visas i denna Interface. Innan du går vidare och skapar en Wallet rekommenderar jag att du justerar applikationsinställningarna så att de passar dina behov. Klicka på "Applikationsinställningar".


![GREEN 2FA MULTISIG](assets/fr/06.webp)


Alternativet "*Enhanced Privacy*", som endast finns tillgängligt på Android, förbättrar integriteten genom att inaktivera skärmdumpar och dölja förhandsvisningar av applikationer. Det låser också automatiskt åtkomsten till applikationer så snart telefonen låses, vilket gör det svårare att komma åt dina data.


![GREEN 2FA MULTISIG](assets/fr/07.webp)


För den som vill stärka sin integritet erbjuder applikationen möjligheten att roota sin trafik via Tor, ett nätverk som krypterar alla dina anslutningar och gör det svårt att spåra dina aktiviteter. Även om det här alternativet kan göra applikationen något långsammare rekommenderas det starkt för att skydda din integritet, särskilt om du inte använder din egen kompletta nod.


![GREEN 2FA MULTISIG](assets/fr/08.webp)


För användare som har en egen komplett nod erbjuder Green Wallet möjligheten att ansluta till den via en Electrum-server, vilket garanterar total kontroll över Bitcoin nätverksinformation och distribution av transaktioner.


![GREEN 2FA MULTISIG](assets/fr/09.webp)


En annan alternativ funktion är alternativet "*SPV Verification*", som gör att du kan verifiera vissa Blockchain-data direkt och därmed minska behovet av att lita på Blockstreams standardnod, även om den här metoden inte ger alla garantier som en Full node.


![GREEN 2FA MULTISIG](assets/fr/10.webp)


När du har anpassat dessa inställningar till dina behov klickar du på knappen "*Save*" och startar om programmet.


![GREEN 2FA MULTISIG](assets/fr/11.webp)


## Skapa en Bitcoin Wallet på Blockstream Green


Du är nu redo att skapa en Bitcoin Wallet. Klicka på knappen "*Get Started*".


![GREEN 2FA MULTISIG](assets/fr/12.webp)


Du kan välja mellan att skapa en lokal Software Wallet eller att hantera en Cold Wallet via en Hardware Wallet. I den här handledningen koncentrerar vi oss på att skapa en Hot Wallet, så du måste välja alternativet "*På den här enheten*".


![GREEN 2FA MULTISIG](assets/fr/13.webp)


Du kan sedan välja att återställa en befintlig Bitcoin Wallet eller skapa en ny. I den här handledningen kommer vi att skapa en ny Wallet. Men om du behöver regenerera en befintlig Bitcoin Wallet från dess Mnemonic-fras, till exempel efter att du förlorat din gamla telefon, måste du välja det andra alternativet.


![GREEN 2FA MULTISIG](assets/fr/14.webp)


Du kan sedan välja mellan en Mnemonic-fras på 12 ord eller 24 ord. Denna fras gör att du kan återfå åtkomst till din Wallet från vilken kompatibel programvara som helst i händelse av problem med din telefon. Att välja en 24 ords fras erbjuder för närvarande inte mer säkerhet än en 12 ords fras. Jag rekommenderar därför att du väljer en Mnemonic-fras på 12 ord.


Green kommer sedan att ge dig din Mnemonic-fras. Innan du fortsätter, se till att du inte blir iakttagen. Klicka på "*Visa återhämtningsfras*" för att visa den på skärmen.


![GREEN 2FA MULTISIG](assets/fr/15.webp)


**Den här Mnemonic ger dig full, obegränsad tillgång till alla dina bitcoins**. Vem som helst som har den här frasen kan stjäla dina pengar, även utan fysisk tillgång till din telefon (med förbehåll för utgången tidslåsning eller 2FA i fallet med en 2/2 Wallet på Green).


Det gör att du kan återställa åtkomsten till dina lokala nycklar i händelse av förlust, stöld eller att din telefon går sönder. Det är därför mycket viktigt att säkerhetskopiera den noggrant **på ett fysiskt medium (inte digitalt)** och förvara den på en säker plats. Du kan skriva ner det på ett papper, eller för extra säkerhet, om det är en stor Wallet, rekommenderar jag att du graverar den på ett rostfritt stålstöd för att skydda den från risken för brand, översvämning eller kollaps (för en Hot Wallet som är utformad för att säkra en liten mängd bitcoins är en enkel pappersbackup förmodligen tillräcklig).


*Självklart får du aldrig dela dessa ord på Internet, vilket jag gör i den här handledningen. Detta prov Wallet kommer endast att användas på Testnet och kommer att raderas i slutet av handledningen.*


![GREEN 2FA MULTISIG](assets/fr/16.webp)


När du har spelat in din Mnemonic-fras korrekt på ett fysiskt medium klickar du på "*Fortsätt*". Green Wallet kommer sedan att be dig bekräfta några av orden i din Mnemonic-fras för att säkerställa att du har spelat in dem korrekt. Fyll i tomrummen med de ord som saknas.


![GREEN 2FA MULTISIG](assets/fr/17.webp)


Välj enhetens PIN-kod, som kommer att användas för att låsa upp din Green Wallet. Detta är ditt skydd mot obehörig fysisk åtkomst. Denna PIN-kod är inte inblandad i härledningen av din Wallet:s kryptografiska nycklar. Så även om du inte har tillgång till PIN-koden kan du få tillgång till dina lokala nycklar om du har din Mnemonic-fras på 12 eller 24 ord.


Vi rekommenderar att du väljer en 6-siffrig PIN-kod som är så slumpmässig som möjligt. Se till att spara den här koden så att du inte glömmer den, annars tvingas du hämta din Wallet från Mnemonic. Du kan sedan lägga till ett biometriskt blockeringsalternativ för att undvika att behöva ange PIN-koden varje gång du använder den. Generellt sett är biometri mycket mindre säkert än själva PIN-koden. Så som standard rekommenderar jag att du inte ställer in det här upplåsningsalternativet.


![GREEN 2FA MULTISIG](assets/fr/18.webp)


Ange din PIN-kod en gång till för att bekräfta den.


![GREEN 2FA MULTISIG](assets/fr/19.webp)


Vänta tills din Wallet har skapats och klicka sedan på knappen "*Create an account*".


![GREEN 2FA MULTISIG](assets/fr/20.webp)


Du kan sedan välja mellan en standard Wallet med en enda signatur eller en Wallet som skyddas av tvåfaktorsautentisering (2FA). I den här handledningen väljer vi det andra alternativet.


![GREEN 2FA MULTISIG](assets/fr/21.webp)


Din Bitcoin Multisig Wallet har nu skapats med hjälp av applikationen Green!


![GREEN 2FA MULTISIG](assets/fr/22.webp)


## Konfigurera 2FA


Klicka på ditt konto.


![GREEN 2FA MULTISIG](assets/fr/23.webp)


Klicka på Green-knappen "*Öka säkerheten för ditt konto genom att lägga till 2FA*".


![GREEN 2FA MULTISIG](assets/fr/24.webp)


Du kommer sedan att kunna välja autentiseringsmetod för att få tillgång till den andra nyckeln i din 2/2 Multisig. För denna handledning kommer vi att använda en autentiseringsapplikation. Om du inte är bekant med den här typen av applikationer rekommenderar jag att du läser vår handledning om Authy :


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Välj "*Authenticator Application*".


![GREEN 2FA MULTISIG](assets/fr/25.webp)


Green kommer då att visa en QR-kod och en återställningsnyckel. Med den här nyckeln kan du återställa åtkomsten till din 2FA om du skulle förlora din Authy-applikation. Det är tillrådligt att göra en säker säkerhetskopia av den här nyckeln, även om du fortfarande kan återställa åtkomsten till dina bitcoins efter att tidslåset har löpt ut, enligt vad som förklaras ovan.


Lägg till en ny kod i din autentiseringsapplikation och skanna sedan QR-koden som tillhandahålls av Green.


![GREEN 2FA MULTISIG](assets/fr/26.webp)


*Självklart får du aldrig dela denna nyckel och QR-kod på Internet, som jag gör i denna handledning. Detta prov Wallet kommer endast att användas på Testnet och kommer att raderas i slutet av handledningen.*


Klicka på knappen "*Fortsätt*".


![GREEN 2FA MULTISIG](assets/fr/27.webp)


Ange den 6-siffriga dynamiska koden som finns på din autentiseringsapplikation.


![GREEN 2FA MULTISIG](assets/fr/28.webp)


2-faktorautentisering är nu aktiverad.


![GREEN 2FA MULTISIG](assets/fr/29.webp)


Genom att bläddra i den här menyn kan du också ställa in tidslåsets varaktighet. Denna nedräkning startar så snart bitcoins tas emot, och när tidslåset har löpt ut kan dina pengar endast spenderas med din lokala nyckel, utan behov av 2FA. Standardvaraktigheten är inställd på 12 månader, men för en sparande Wallet kan det vara vettigt att välja 15 månader för att minimera frekvensen för förnyelse av tidslåset. Omvänt, för en Wallet för utgifter kan ett 6-månaders tidslås vara att föredra, eftersom det ofta kommer att förnyas med dina dagliga transaktioner, och ett kortare tidslås minskar väntan i händelse av ett problem med 2FA. Det är upp till dig att avgöra vilken tidslucka som passar dig bäst.


![GREEN 2FA MULTISIG](assets/fr/30.webp)


Du kan nu lämna denna meny. Din Multisig Wallet är klar!


![GREEN 2FA MULTISIG](assets/fr/31.webp)


## Konfigurera din Wallet på Blockstream Green


Om du vill göra din Wallet personlig klickar du på de tre små prickarna i det övre högra hörnet.


![GREEN 2FA MULTISIG](assets/fr/32.webp)


Med alternativet "*Rename*" kan du anpassa namnet på din Wallet, vilket är särskilt användbart om du hanterar flera plånböcker i samma applikation.


![GREEN 2FA MULTISIG](assets/fr/33.webp)


I menyn "*Unit*" kan du ändra basenheten för din Wallet. Du kan t.ex. välja att visa den i satoshis i stället för bitcoins.


![GREEN 2FA MULTISIG](assets/fr/34.webp)


Menyn "*Settings*" ger tillgång till de olika alternativen för din Bitcoin Wallet.


![GREEN 2FA MULTISIG](assets/fr/35.webp)


Här hittar du till exempel din utökade publika nyckel och dess *descriptor*, användbart om du planerar att konfigurera en Wallet i watch-only-läge från denna Wallet.


![GREEN 2FA MULTISIG](assets/fr/36.webp)


Du kan också ändra din Wallet PIN-kod och aktivera en biometrisk anslutning.


![GREEN 2FA MULTISIG](assets/fr/37.webp)


## Använda Blockstream Green


Nu när din Bitcoin Wallet är konfigurerad är du redo att ta emot din första Sats! Klicka bara på knappen "*Receive*".


![GREEN 2FA MULTISIG](assets/fr/38.webp)


Green kommer sedan att visa den första tomma mottagande Address i din Wallet. Du kan antingen skanna den tillhörande QR-koden eller kopiera Address direkt för att skicka bitcoins. Denna typ av Address specificerar inte beloppet som ska skickas av betalaren. Du kan dock generate en Address som begär ett specifikt belopp genom att klicka på de tre små prickarna i det övre högra hörnet, sedan på "*Begär belopp*" och ange önskat belopp.


![GREEN 2FA MULTISIG](assets/fr/39.webp)


När transaktionen sänds ut i nätverket kommer den att visas i din Wallet.


![GREEN 2FA MULTISIG](assets/fr/40.webp)


Vänta tills du har fått tillräckligt många bekräftelser för att betrakta transaktionen som slutgiltig.


![GREEN 2FA MULTISIG](assets/fr/41.webp)


Med bitcoins i din Wallet kan du nu också skicka bitcoins. Klicka på "*Sänd*".


![GREEN 2FA MULTISIG](assets/fr/42.webp)


På nästa sida anger du mottagarens Address. Du kan ange den manuellt eller skanna en QR-kod.


![GREEN 2FA MULTISIG](assets/fr/43.webp)


Välj betalningsbelopp.


![GREEN 2FA MULTISIG](assets/fr/44.webp)


Längst ner på skärmen kan du välja avgiftssats för den här transaktionen. Du kan välja mellan att följa programmets rekommendationer eller att anpassa dina avgifter. Ju högre avgift i förhållande till andra väntande transaktioner, desto snabbare kommer din transaktion att behandlas. För information om avgiftsmarknaden, besök [Mempool.space](https://Mempool.space/) i avsnittet "*Transaktionsavgifter*".


![GREEN 2FA MULTISIG](assets/fr/45.webp)


Klicka på "*Nästa*" för att komma till skärmen för transaktionsöversikt. Kontrollera att Address, belopp och avgifter är korrekta.


![GREEN 2FA MULTISIG](assets/fr/46.webp)


Om allt går bra skjuter du Green-knappen längst ned på skärmen åt höger för att signera och sända transaktionen i Bitcoin-nätverket.


![GREEN 2FA MULTISIG](assets/fr/47.webp)


Det är nu du måste ange din autentiseringskod för att låsa upp den andra Multisig-nyckeln som Blockstream har. Ange den 6-siffriga koden som visas på din autentiseringsapplikation.


![GREEN 2FA MULTISIG](assets/fr/48.webp)


Din transaktion kommer nu att visas på din Bitcoin Wallet instrumentpanel i väntan på bekräftelse.


![GREEN 2FA MULTISIG](assets/fr/49.webp)


Så nu vet du hur du enkelt kan ställa in en 2/2 Multisig Wallet med Blockstream Green: s 2FA-alternativ!


Om du tyckte att denna handledning var användbar skulle jag vara tacksam om du lämnar en Green tumme nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack så mycket!


Jag rekommenderar också att du kollar in den här andra omfattande handledningen om mobilapplikationen Blockstream Green för att konfigurera en Liquid Wallet :


https://planb.network/tutorials/wallet/mobile/blockstream-green-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a