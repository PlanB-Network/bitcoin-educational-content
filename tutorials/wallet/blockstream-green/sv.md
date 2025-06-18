---
name: Blockstream Green - Mobil
description: Konfigurera en mobil Software Wallet
---
![cover](assets/cover.webp)


En Software Wallet är en applikation som installeras på en dator, smartphone eller annan internetansluten enhet och som gör att du kan hantera och säkra dina Bitcoin Wallet-nycklar. Till skillnad från hårdvaruplånböcker, som isolerar privata nycklar, fungerar "Hot"-plånböcker därför i en miljö som potentiellt är utsatt för cyberattacker, vilket ökar risken för piratkopiering och stöld.


Mjukvaruplånböcker bör användas för att hantera rimliga mängder bitcoins, särskilt för vardagliga transaktioner. De kan också vara ett intressant alternativ för personer med begränsade Bitcoin-tillgångar, för vilka en investering i en Hardware Wallet kan verka oproportionerlig. Deras ständiga exponering mot internet gör dem dock mindre säkra för att lagra dina långsiktiga besparingar eller stora fonder. För det senare är det bäst att välja säkrare lösningar, till exempel hårdvaruplånböcker.


I den här handledningen vill jag presentera dig för en av de bästa mobila Software Wallet-lösningarna: **Blockstream Green**.


![GREEN](assets/fr/01.webp)


Om du vill veta mer om hur du använder Blockstream Green på din dator kan du läsa den här andra handledningen:


https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da

## Introduktion av Blockstream Green


Blockstream Green är en Software Wallet som är tillgänglig på mobil och dator. Denna Wallet var tidigare känd som *Green Address* och blev ett Blockstream-projekt efter förvärvet 2016.


Green är en särskilt lättanvänd applikation, vilket gör den intressant för nybörjare. Den erbjuder alla viktiga funktioner i en bra Bitcoin Wallet, inklusive RBF (* Replace-by-fee*), ett Tor-anslutningsalternativ, möjligheten att ansluta din egen nod, SPV (* Enkel betalningsverifiering*), myntmärkning och kontroll.


Blockstream Green stöder också Liquid Network, en Bitcoin Sidechain utvecklad av Blockstream för snabb, Confidential Transactions utanför huvud Blockchain. Denna handledning fokuserar uteslutande på Bitcoin, men en senare kommer att täcka användningen av Liquid.


## Installera och konfigurera Blockstream Green-applikationen


Det första steget är naturligtvis att ladda ner Green-applikationen. Gå till din applikationsbutik:



- [För Android] (https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [For Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![GREEN](assets/fr/02.webp)


För Android-användare kan du också installera applikationen via filen `.apk` [tillgänglig på Blockstreams GitHub] (https://github.com/Blockstream/green_android/releases).


![GREEN](assets/fr/03.webp)


Starta programmet och kryssa sedan i rutan "Jag accepterar villkoren...*".


![GREEN](assets/fr/04.webp)


När du öppnar Green för första gången visas startskärmen utan en konfigurerad Wallet. Senare, om du skapar eller importerar plånböcker, kommer de att visas i denna Interface. Innan du fortsätter att skapa en Wallet rekommenderar jag att du justerar applikationsinställningarna så att de passar dina behov. Klicka på "Applikationsinställningar".


![GREEN](assets/fr/05.webp)


Alternativet "*Enhanced Privacy*", som endast finns tillgängligt på Android, förbättrar integriteten genom att inaktivera skärmdumpar och dölja förhandsvisningar av applikationer. Det låser också automatiskt åtkomsten till applikationer så snart telefonen låses, vilket gör det svårare att komma åt dina data.


![GREEN](assets/fr/06.webp)


För den som vill stärka sin integritet erbjuder applikationen möjligheten att roota sin trafik via Tor, ett nätverk som krypterar alla dina anslutningar och gör det svårt att spåra dina aktiviteter. Även om det här alternativet kan göra applikationen något långsammare rekommenderas det starkt för att skydda din integritet, särskilt om du inte använder din egen kompletta nod.


![GREEN](assets/fr/07.webp)


För användare som har sin egen kompletta nod erbjuder Green Wallet möjligheten att ansluta till den via en Electrum-server, vilket garanterar total kontroll över Bitcoin nätverksinformation och distribution av transaktioner.


![GREEN](assets/fr/08.webp)


En annan alternativ funktion är alternativet "*SPV Verification*", som gör att du kan verifiera vissa Blockchain-data direkt och därmed minska behovet av att lita på Blockstreams standardnod, även om den här metoden inte ger alla garantier som en Full node.


![GREEN](assets/fr/09.webp)


När du har anpassat dessa inställningar till dina behov klickar du på knappen "*Save*" och startar om programmet.


![GREEN](assets/fr/10.webp)


## Skapa en Bitcoin Wallet på Blockstream Green


Du är nu redo att skapa en Bitcoin Wallet. Klicka på knappen "*Get Started*".


![GREEN](assets/fr/11.webp)


Du kan välja mellan att skapa en lokal Software Wallet eller att hantera en Cold Wallet via en Hardware Wallet. I den här handledningen koncentrerar vi oss på att skapa en Hot Wallet, så du måste välja alternativet "*På den här enheten*". I en framtida handledning visar jag hur du använder det andra alternativet.


Med alternativet "*Watch-only*" kan du importera en utökad publik nyckel (`xpub`) för att se en Wallet:s transaktioner utan att kunna spendera de tillhörande pengarna, vilket är praktiskt för att spåra en Wallet på en Hardware Wallet, till exempel.


![GREEN](assets/fr/12.webp)


Du kan sedan välja att återställa en befintlig Bitcoin Wallet eller skapa en ny. I den här handledningen kommer vi att skapa en ny Wallet. Men om du behöver regenerera en befintlig Bitcoin Wallet från dess Mnemonic-fras, till exempel efter förlusten av din Hardware Wallet, måste du välja det andra alternativet.


![GREEN](assets/fr/13.webp)


Du kan sedan välja mellan en Mnemonic-fras på 12 ord eller 24 ord. Denna fras gör det möjligt för dig att återfå åtkomst till din Wallet från vilken kompatibel programvara som helst i händelse av problem med din telefon. För närvarande erbjuder valet av en 24 ords fras inte mer säkerhet än en 12 ords fras. Jag rekommenderar därför att du väljer en Mnemonic-fras på 12 ord.


Green kommer sedan att ge dig din Mnemonic-fras. Innan du fortsätter, se till att du inte blir iakttagen. Klicka på "*Visa återhämtningsfras*" för att visa den på skärmen.


![GREEN](assets/fr/14.webp)


**Den här Mnemonic:an ger dig full, obegränsad tillgång till alla dina bitcoins ** Alla som har den här Mnemonic:an kan stjäla dina pengar, även utan fysisk tillgång till din telefon.


Den återställer åtkomsten till dina bitcoins i händelse av förlust, stöld eller att din telefon går sönder. Så det är mycket viktigt att säkerhetskopiera den noggrant ** på ett fysiskt medium (inte digitalt)** och förvara den på en säker plats. Du kan skriva ner det på ett papper, eller för extra säkerhet, om detta är en stor Wallet, rekommenderar jag att du graverar den på ett rostfritt stålstöd för att skydda den från risken för brand, översvämning eller kollaps (för en Hot Wallet som är utformad för att säkra en liten mängd bitcoins är en enkel pappersbackup förmodligen tillräcklig).


*Självklart får du aldrig dela dessa ord på Internet, som jag gör i den här handledningen. Detta exempel Wallet kommer endast att användas på Testnet och kommer att raderas i slutet av handledningen.*


![GREEN](assets/fr/15.webp)


När du har spelat in din Mnemonic-fras korrekt på ett fysiskt medium klickar du på "*Fortsätt*". Green Wallet kommer sedan att be dig att bekräfta några av orden i din Mnemonic-fras för att säkerställa att du har spelat in dem korrekt. Fyll i tomrummen med de ord som saknas.


![GREEN](assets/fr/16.webp)


Välj enhetens PIN-kod, som kommer att användas för att låsa upp din Green Wallet. Detta är ditt skydd mot obehörig fysisk åtkomst. Denna PIN-kod är inte inblandad i härledningen av din Wallet:s kryptografiska nycklar. Så även om du inte har tillgång till PIN-koden kan du få tillgång till dina bitcoins om du har din Mnemonic-fras på 12 eller 24 ord.


Vi rekommenderar att du väljer en 6-siffrig PIN-kod som är så slumpmässig som möjligt. Se till att spara den här koden så att du inte glömmer den, annars tvingas du hämta din Wallet från Mnemonic. Du kan sedan lägga till ett biometriskt blockeringsalternativ för att undvika att behöva ange PIN-koden varje gång du använder den. Generellt sett är biometri mycket mindre säkert än själva PIN-koden. Så som standard rekommenderar jag att du inte ställer in det här upplåsningsalternativet.


![GREEN](assets/fr/17.webp)


Ange din PIN-kod en gång till för att bekräfta den.


![GREEN](assets/fr/18.webp)


Vänta tills din Wallet har skapats och klicka sedan på knappen "*Create an account*".


![GREEN](assets/fr/19.webp)


Du kan sedan välja mellan en standard Wallet med en enda signatur, som vi använder i den här handledningen, eller en Wallet som skyddas av tvåfaktorsautentisering (2FA).


![GREEN](assets/fr/20.webp)


2FA-alternativet på Green skapar en 2/2 multisignatur Wallet, med en nyckel som innehas av Blockstream. Detta innebär att båda nycklarna krävs för att genomföra en transaktion: en lokal nyckel som skyddas av din PIN-kod på din telefon och en fjärrnyckel som skyddas av 2FA på Blockstreams servrar. I händelse av förlust av åtkomst till 2FA eller otillgänglighet av Blockstreams tjänster säkerställer återställningsmekanismer baserade på tidslåsskript att dina medel kan återställas autonomt. Även om denna konfiguration avsevärt minskar risken för stöld av dina bitcoins, är den mer komplex att hantera och delvis beroende av Blockstream. För denna handledning väljer vi en klassisk Wallet med en enda signatur, där nycklarna lagras lokalt på telefonen.


Din Bitcoin Wallet har nu skapats med hjälp av applikationen Green!


![GREEN](assets/fr/21.webp)


Innan du tar emot dina första bitcoins i din Wallet, ** rekommenderar jag starkt att du utför ett tomt återställningstest**. Anteckna viss referensinformation, till exempel din xpub eller första mottagande Address, och radera sedan din Wallet i Green-appen medan den fortfarande är tom. Försök sedan att återställa din Wallet på Green med hjälp av dina pappersbackuper. Kontrollera att cookieinformationen som genereras efter återställningen matchar den som du ursprungligen skrev ner. Om den gör det kan du vara säker på att dina pappersbackuper är tillförlitliga. Om du vill veta mer om hur du utför en teståterställning kan du läsa den här andra handledningen:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Konfigurera din Wallet på Blockstream Green


Om du vill göra din Wallet personlig klickar du på de tre små prickarna i det övre högra hörnet.


![GREEN](assets/fr/22.webp)


Med alternativet "*Rename*" kan du anpassa namnet på din Wallet, vilket är särskilt användbart om du hanterar flera plånböcker i samma program.


![GREEN](assets/fr/23.webp)


I menyn "*Unit*" kan du ändra basenheten för din Wallet. Du kan t.ex. välja att visa den i satoshis i stället för bitcoins.


![GREEN](assets/fr/24.webp)


Menyn "*Settings*" ger tillgång till olika alternativ för din Bitcoin Wallet.


![GREEN](assets/fr/25.webp)


Här hittar du till exempel din utökade publika nyckel och dess *descriptor*, vilket är användbart om du planerar att konfigurera en Wallet i watch-only-läge från den här Wallet.


![GREEN](assets/fr/26.webp)


Du kan också ändra din Wallet PIN-kod och aktivera en biometrisk anslutning.


![GREEN](assets/fr/27.webp)


## Använda Blockstream Green


Nu när din Bitcoin Wallet är konfigurerad är du redo att ta emot din första Sats! Klicka bara på knappen "*Receive*".


![GREEN](assets/fr/28.webp)


Green kommer sedan att visa den första tomma mottagande Address i din Wallet. Du kan antingen skanna den tillhörande QR-koden eller kopiera Address direkt för att skicka bitcoins. Denna typ av Address specificerar inte det belopp som ska skickas av betalaren. Du kan dock skicka en generate med en Address som begär ett specifikt belopp genom att klicka på de tre små prickarna i det övre högra hörnet, sedan på "*Begära belopp*" och ange önskat belopp.


Eftersom du använder ett SegWit v0-konto (BIP84) kommer din Address att börja med `bc1q...`. I mitt exempel använder jag en Testnet Wallet, så prefixet är något annorlunda.


![GREEN](assets/fr/29.webp)


När transaktionen sänds ut i nätverket kommer den att visas i din Wallet.


![GREEN](assets/fr/30.webp)


Vänta tills du har fått tillräckligt många bekräftelser för att betrakta transaktionen som slutgiltig.


![GREEN](assets/fr/31.webp)


Med bitcoins i din Wallet kan du nu också skicka bitcoins. Klicka på "*Sänd*".


![GREEN](assets/fr/32.webp)


På nästa sida anger du mottagarens Address. Du kan ange den manuellt eller skanna en QR-kod.


![GREEN](assets/fr/33.webp)


Välj betalningsbelopp.


![GREEN](assets/fr/34.webp)


Längst ner på skärmen kan du välja avgiftssats för den här transaktionen. Du kan välja att följa programmets rekommendationer eller anpassa dina avgifter. Ju högre avgift i förhållande till andra väntande transaktioner, desto snabbare kommer din transaktion att behandlas. För information om avgiftsmarknaden, besök [Mempool.space](https://Mempool.space/) i avsnittet "*Transaktionsavgifter*".


![GREEN](assets/fr/35.webp)


Klicka på "*Nästa*" för att komma till skärmen för transaktionsöversikt. Kontrollera att Address, belopp och avgifter är korrekta.


![GREEN](assets/fr/36.webp)


Om allt går bra skjuter du Green-knappen längst ned på skärmen åt höger för att signera och sända transaktionen i Bitcoin-nätverket.


![GREEN](assets/fr/37.webp)


Din transaktion kommer nu att visas på din Bitcoin Wallet instrumentpanel i väntan på bekräftelse.


![GREEN](assets/fr/38.webp)


*Denna handledning är baserad på [en originalversion som tillhör Bitstack] (https://www.bitstack-app.com/blog/installer-portefeuille-Bitcoin-Green-Wallet) skriven av Loïc Morel. Bitstack är en fransk Bitcoin neo-bank som erbjuder möjligheten att spara i bitcoins, antingen i DCA (Dollar Cost Averaging) eller via ett automatiskt avrundningssystem för dagliga utgifter.* Bitstack är en fransk Bitcoin neo-bank som erbjuder möjligheten att spara i bitcoins, antingen i DCA (Dollar Cost Averaging) eller via ett automatiskt avrundningssystem för dagliga utgifter