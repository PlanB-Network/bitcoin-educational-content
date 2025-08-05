---
name: Blockstream Green - Liquid
description: Konfigurera en Wallet på Liquid Network Sidechain
---
![cover](assets/cover.webp)


Bitcoin-protokollet har avsiktliga tekniska begränsningar som bidrar till att upprätthålla nätverkets decentralisering och säkerställa att säkerheten fördelas mellan alla användare. Dessa begränsningar kan dock ibland frustrera användarna, särskilt under överbelastning på grund av en hög volym av samtidiga transaktioner. Debatten om Bitcoin:s skalbarhet har länge delat gemenskapen, särskilt under Blocksize War. Sedan denna episod är det allmänt erkänt inom Bitcoin-communityn att skalbarhet måste säkerställas genom off-chain-lösningar på andra Layer-system. Dessa lösningar inkluderar sidokedjor, som fortfarande är relativt okända och lite använda jämfört med andra system som Lightning Network.


En Sidechain är en oberoende Blockchain som fungerar parallellt med den huvudsakliga Bitcoin Blockchain. Den använder Bitcoin som en kontoenhet, tack vare en mekanism som kallas "*two-way peg*". Detta system gör det möjligt att låsa bitcoins på huvudkedjan för att reproducera deras värde på Sidechain, där de cirkulerar i form av tokens som backas upp av de ursprungliga bitcoins. Dessa tokens behåller normalt samma värde som de bitcoins som är låsta på huvudkedjan, och processen kan vändas för att återfå medel på Bitcoin.


Syftet med sidokedjor är att erbjuda ytterligare funktioner eller tekniska förbättringar, t.ex. snabbare transaktioner, lägre avgifter eller stöd för smarta kontrakt. Dessa innovationer kan inte alltid implementeras direkt på Bitcoin Blockchain utan att äventyra dess decentralisering eller säkerhet. Sidokedjor gör det därför möjligt att testa och utforska nya lösningar samtidigt som Bitcoin:s integritet bevaras. Dessa protokoll kräver dock ofta kompromisser, särskilt när det gäller decentralisering och säkerhet, beroende på vilken styrmodell och konsensusmekanism som väljs.


Idag är den mest kända Sidechain förmodligen Liquid. I den här handledningen berättar jag först vad Liquid är och guidar dig sedan genom hur du enkelt kan börja använda det med Blockstream Green-applikationen, så att du kan njuta av alla dess fördelar.


![LIQUID GREEN](assets/fr/01.webp)


## Vad är Liquid Network?


Liquid är ett federerat Sidechain-överlägg för Bitcoin, utvecklat av Blockstream för att förbättra transaktionshastighet, integritet och funktionalitet. Den använder en bilateral förankringsmekanism etablerad på en federation för att låsa bitcoins på huvudkedjan och skapa Liquid-bitcoins (L-BTC) i gengäld, tokens som cirkulerar på Liquid medan de fortfarande backas upp av de ursprungliga bitcoins.


![LIQUID GREEN](assets/fr/02.webp)


Liquid Network förlitar sig på en federation av deltagare, bestående av erkända enheter från Bitcoin-ekosystemet, som validerar block och hanterar bilateral pegging. Förutom L-BTC möjliggör Liquid även utgivning av andra digitala tillgångar, såsom stablecoins och andra kryptovalutor.


![LIQUID GREEN](assets/fr/03.webp)


## Vi presenterar Blockstream Green


Blockstream Green är en Software Wallet som är tillgänglig på mobil och dator. Denna Wallet var tidigare känd som *Green Address* och blev ett Blockstream-projekt efter förvärvet 2016.


Green är en särskilt lättanvänd applikation, vilket gör den intressant för nybörjare. Den erbjuder alla viktiga funktioner i en bra Bitcoin Wallet, inklusive RBF (* Replace-by-fee*), ett Tor-anslutningsalternativ, möjligheten att ansluta din egen nod, SPV (* Enkel betalningsverifiering*), myntmärkning och kontroll.


Blockstream Green stöder också Liquid Network, och det är vad vi kommer att ta reda på i den här handledningen. Om du vill använda Green för andra applikationer rekommenderar jag att du också tar en titt på dessa andra handledningar:


https://planb.network/tutorials/wallet/desktop/blockstream-green-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da

https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

https://planb.network/tutorials/wallet/mobile/blockstream-green-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

## Installera och konfigurera Blockstream Green-applikationen


Det första steget är naturligtvis att ladda ner Green-applikationen. Gå till din applikationsbutik:



- [För Android] (https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [For Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![LIQUID GREEN](assets/fr/04.webp)


För Android-användare kan du också installera applikationen via filen `.apk` [tillgänglig på Blockstreams GitHub] (https://github.com/Blockstream/green_android/releases).


![LIQUID GREEN](assets/fr/05.webp)


Starta programmet och kryssa sedan i rutan "Jag accepterar villkoren...*".


![LIQUID GREEN](assets/fr/06.webp)


När du öppnar Green för första gången visas startskärmen utan en konfigurerad Wallet. Om du senare skapar eller importerar plånböcker kommer de att visas i denna Interface. Innan du går vidare och skapar en Wallet rekommenderar jag att du justerar applikationsinställningarna så att de passar dina behov. Klicka på "Applikationsinställningar".


![LIQUID GREEN](assets/fr/07.webp)


Alternativet "*Enhanced Privacy*", som endast finns tillgängligt på Android, förbättrar integriteten genom att inaktivera skärmdumpar och dölja förhandsvisningar av applikationer. Det låser också automatiskt åtkomsten till applikationer så snart telefonen låses, vilket gör det svårare att komma åt dina data.


![LIQUID GREEN](assets/fr/08.webp)


För den som vill stärka sin integritet erbjuder applikationen möjligheten att roota sin trafik via Tor, ett nätverk som krypterar alla dina anslutningar och gör det svårt att spåra dina aktiviteter. Även om det här alternativet kan göra applikationen något långsammare rekommenderas det starkt för att skydda din integritet, särskilt om du inte använder din egen kompletta nod.


![LIQUID GREEN](assets/fr/09.webp)


För användare som har sin egen kompletta nod erbjuder Green Wallet möjligheten att ansluta till den via en Electrum-server, vilket garanterar total kontroll över Bitcoin-nätverksinformation och transaktionsspridning. Men den här funktionen är för klassiska Bitcoin-plånböcker, så du behöver inte den om du använder Liquid.


![LIQUID GREEN](assets/fr/10.webp)


En annan alternativ funktion är alternativet "*SPV Verification*", som gör att du kan verifiera vissa Blockchain-data direkt och därmed minska behovet av att lita på Blockstreams standardnod, även om den här metoden inte ger alla garantier för en Full node. Återigen kommer detta bara att påverka dina onchain Bitcoin plånböcker, inte Liquid.


![LIQUID GREEN](assets/fr/11.webp)


När du har anpassat dessa inställningar till dina behov klickar du på knappen "*Save*" och startar om programmet.


![LIQUID GREEN](assets/fr/12.webp)


## Skapa en Liquid Wallet på Blockstream Green


Du är nu redo att skapa en Liquid Wallet. Klicka på knappen "*Get Started*".


![LIQUID GREEN](assets/fr/13.webp)


Du kan välja mellan att skapa en lokal Software Wallet eller att hantera en Cold Wallet via en Hardware Wallet. I den här handledningen fokuserar vi på att skapa en Hot Wallet på Liquid, så du måste välja alternativet "*På den här enheten*". Du kan också använda en kompatibel Hardware Wallet, till exempel Blockstream Jade, för att säkra din Liquid Wallet.


![LIQUID GREEN](assets/fr/14.webp)


Du kan sedan välja att återställa en befintlig Bitcoin Wallet eller skapa en ny. I den här handledningen kommer vi att skapa en ny Wallet. Men om du behöver regenerera en befintlig Liquid Wallet från dess Mnemonic-fras, till exempel efter förlusten av din Hardware Wallet, måste du välja det andra alternativet.


![LIQUID GREEN](assets/fr/15.webp)


Du kan sedan välja mellan en Mnemonic-fras på 12 ord eller 24 ord. Denna fras gör att du kan återfå åtkomst till din Wallet från vilken kompatibel programvara som helst i händelse av problem med din telefon. För närvarande erbjuder valet av en 24 ords fras inte mer säkerhet än en 12 ords fras. Jag rekommenderar därför att du väljer en Mnemonic-fras på 12 ord.


Green kommer sedan att ge dig din Mnemonic-fras. Innan du fortsätter, se till att du inte blir iakttagen. Klicka på "*Visa återhämtningsfras*" för att visa den på skärmen.


![LIQUID GREEN](assets/fr/16.webp)


**Den här Mnemonic ger dig full, obegränsad tillgång till alla dina bitcoins ** Vem som helst som har den här Mnemonic kan stjäla dina pengar, även utan fysisk tillgång till din telefon.


Den återställer åtkomsten till dina bitcoins i händelse av förlust, stöld eller att din telefon går sönder. Så det är mycket viktigt att säkerhetskopiera den noggrant **på ett fysiskt medium (inte digitalt)** och förvara den på en säker plats. Du kan skriva ner det på ett papper, eller för extra säkerhet, om detta är en stor Wallet, rekommenderar jag att du graverar den på ett rostfritt stålstöd för att skydda den från risken för brand, översvämning eller kollaps (för en Hot Wallet som är utformad för att säkra en liten mängd bitcoins är en enkel pappersbackup förmodligen tillräcklig).


*Självklart får du aldrig dela dessa ord på Internet, vilket jag gör i den här handledningen. Detta exempel Wallet kommer endast att användas på Liquid:s Testnet och kommer att raderas i slutet av handledningen.*


![LIQUID GREEN](assets/fr/17.webp)


När du har spelat in din Mnemonic-fras korrekt på ett fysiskt medium klickar du på "*Fortsätt*". Green Wallet kommer sedan att be dig bekräfta några av orden i din Mnemonic-fras för att säkerställa att du har spelat in dem korrekt. Fyll i tomrummen med de ord som saknas.


![LIQUID GREEN](assets/fr/18.webp)


Välj enhetens PIN-kod, som kommer att användas för att låsa upp din Green Wallet. Detta är ditt skydd mot obehörig fysisk åtkomst. Denna PIN-kod är inte inblandad i härledningen av din Wallet:s kryptografiska nycklar. Så även om du inte har tillgång till PIN-koden kan du få tillgång till dina bitcoins om du har din Mnemonic-fras på 12 eller 24 ord.


Vi rekommenderar att du väljer en 6-siffrig PIN-kod som är så slumpmässig som möjligt. Var noga med att spara den här koden så att du inte glömmer den, annars tvingas du hämta din Wallet från Mnemonic. Du kan sedan lägga till ett biometriskt blockeringsalternativ för att undvika att behöva ange PIN-koden varje gång du använder den. Generellt sett är biometri mycket mindre säker än själva PIN-koden. Så som standard rekommenderar jag att du inte ställer in det här upplåsningsalternativet.


![LIQUID GREEN](assets/fr/19.webp)


Ange din PIN-kod en gång till för att bekräfta den.


![LIQUID GREEN](assets/fr/20.webp)


Vänta tills din Wallet har skapats och klicka sedan på knappen "*Create an account*".


![LIQUID GREEN](assets/fr/21.webp)


I rutan "*Active*" väljer du "*Liquid Bitcoin*". Du kan sedan välja mellan en standard Wallet med en enda signatur, som vi kommer att använda i den här handledningen, eller en Wallet som skyddas av tvåfaktorsautentisering (2FA).


![LIQUID GREEN](assets/fr/22.webp)


Och det är det, din Liquid Wallet har skapats med hjälp av Green-applikationen!


![LIQUID GREEN](assets/fr/23.webp)


Innan du får dina första bitcoins på din Liquid Wallet, ** rekommenderar jag starkt att du utför ett tomt återställningstest**. Anteckna viss referensinformation, till exempel din xpub eller första mottagande Address, och ta sedan bort din Wallet i Green-appen medan den fortfarande är tom. Försök sedan återställa din Wallet på Green med hjälp av dina pappersbackuper. Kontrollera att cookieinformationen som genereras efter återställningen matchar den som du ursprungligen skrev ner. Om den gör det kan du vara säker på att dina pappersbackuper är tillförlitliga. Om du vill veta mer om hur du utför en teståterställning kan du läsa den här andra handledningen:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Konfigurera din Liquid Wallet


Om du vill göra din Wallet personlig klickar du på de tre små prickarna i det övre högra hörnet.


![LIQUID GREEN](assets/fr/24.webp)


Med alternativet "*Rename*" kan du anpassa namnet på din Wallet, vilket är särskilt användbart om du hanterar flera plånböcker i samma applikation.


![LIQUID GREEN](assets/fr/25.webp)


I menyn "*Unit*" kan du ändra basenheten för din Wallet. Du kan t.ex. välja att visa den i satoshis i stället för bitcoins.


![LIQUID GREEN](assets/fr/26.webp)


Menyn "*Settings*" ger tillgång till de olika alternativen för din Bitcoin Wallet.


![LIQUID GREEN](assets/fr/27.webp)


Här hittar du till exempel din *descriptor*, som kan komma väl till pass om du planerar att sätta upp en Watch-only wallet från denna Liquid Wallet.


![LIQUID GREEN](assets/fr/28.webp)


Du kan också ändra din Wallet PIN-kod och aktivera en biometrisk anslutning.


![LIQUID GREEN](assets/fr/29.webp)


## Använda din Liquid Wallet


Nu när din Liquid Wallet är konfigurerad är du redo att ta emot din första L-Sats!


Om du ännu inte har L-BTC har du flera alternativ. Det första är att få några skickade direkt till dig. Om någon vill betala dig i bitcoins på Liquid, ger du dem helt enkelt en mottagande Address. Det andra alternativet är att Exchange dina bitcoins på kedjan eller på Lightning Network för L-BTC. För att göra detta kan du använda [en brygga som Boltz] (https://boltz.Exchange/). Ange helt enkelt din Liquid Address på webbplatsen och gör sedan betalningen antingen via Lightning Network eller onchain.


![LIQUID GREEN](assets/fr/30.webp)


För att generate en Liquid Address, klicka på knappen "*Receive*".


![LIQUID GREEN](assets/fr/31.webp)


Green kommer sedan att visa den första tomma mottagande Address i din Wallet. Du kan antingen skanna den tillhörande QR-koden eller kopiera Address direkt för att skicka L-BTC.


![LIQUID GREEN](assets/fr/32.webp)


När transaktionen sänds ut i nätverket kommer den att visas i din Wallet.


![LIQUID GREEN](assets/fr/33.webp)


Vänta tills du har fått tillräckligt många bekräftelser för att betrakta transaktionen som slutgiltig. På Liquid bör bekräftelserna vara snabba, eftersom ett block publiceras varje minut.


![LIQUID GREEN](assets/fr/34.webp)


Med L-Sats i din Liquid Wallet kan du nu också skicka dem. Klicka på "*Sänd*".


![LIQUID GREEN](assets/fr/35.webp)


På nästa sida anger du mottagarens Liquid Address. Du kan ange den manuellt eller skanna dess QR-kod.


![LIQUID GREEN](assets/fr/36.webp)


Välj betalningsbelopp.


![LIQUID GREEN](assets/fr/37.webp)


Klicka på "*Nästa*" för att komma till skärmen för transaktionsöversikt. Kontrollera att Address, belopp och avgifter är korrekta.


![LIQUID GREEN](assets/fr/38.webp)


Om allt går bra skjuter du Green-knappen längst ned på skärmen åt höger för att signera och sända transaktionen i Bitcoin-nätverket.


![LIQUID GREEN](assets/fr/39.webp)


Din transaktion kommer nu att visas på din Bitcoin Wallet instrumentpanel i väntan på bekräftelse.


![LIQUID GREEN](assets/fr/40.webp)


Och nu vet du hur du enkelt kan använda Liquid Sidechain med Blockstream Green-applikationen!


Om du tyckte att denna handledning var användbar skulle jag vara tacksam om du lämnar en Green tumme nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack så mycket!


Jag rekommenderar också att du kollar in den här andra omfattande handledningen om Blockstream Green-mobilappen för att ställa in en onchain Bitcoin Hot Wallet :


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143
