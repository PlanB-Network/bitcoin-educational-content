---
name: Jade Plus - Green
description: Konfigurera enkelt Jade Plus med Green
---
![cover](assets/cover.webp)


![video](https://youtu.be/rv_cN7F7-TM)


Jade Plus är en Hardware Wallet för endast Bitcoin som designats av Blockstream. Det är efterföljaren till den klassiska Jade, med mjukvaruförbättringar, fler alternativ och omdesignad ergonomi för mer intuitiv användning. Den här nya versionen har en magnifik 1,9-tums LCD-skärm med ett bredare färgomfång än föregångaren. Knappar och menynavigering har också optimerats.


Jade Plus kan användas på flera olika sätt: via en kabelanslutning via USB-C, i "*Air-Gap*"-läge med ett micro SD-kort (adapter krävs), via Bluetooth eller till och med genom att utbyta QR-koder tack vare den integrerade kameran. Denna Hardware Wallet är batteridriven.


Den finns tillgänglig från 149,99 USD i den svarta grundversionen, och priset kan stiga med upp till 20 USD för versionerna "*Genesis Grey*" eller "*Lunar Silver*". Jade Plus är därför ett intressant val, med avancerade funktioner som kan jämföras med avancerade hårdvaruplånböcker som Coldcard Q eller Passport V2, men till ett ganska lågt pris, nära mellanklassmodeller.


![JADE-PLUS-GREEN](assets/fr/01.webp)


Jade Plus är kompatibelt med de flesta programvaror för Wallet-hantering. Här är en sammanfattning av kompatibiliteten i skrivande stund (januari 2025):


| Management Software  | Desktop | Mobile | USB | Bluetooth   | QR  | JadeLink |
| -------------------- | ------- | ------ | --- | ----------- | --- | -------- |
| Blockstream Green    | 🟢      | 🟢     | 🟢  | 🟢 (Mobile) | 🟢  | 🔴       |
| Liana                | 🟢      | 🔴     | 🟢  | 🔴          | 🔴  | 🔴       |
| Sparrow              | 🟢      | 🔴     | 🟢  | 🔴          | 🟢  | 🟢       |
| Nunchuk              | 🟢      | 🟢     | 🔴  | 🔴          | 🟢  | 🟢       |
| Specter              | 🟢      | 🔴     | 🔴  | 🔴          | 🟢  | 🟢       |
| BlueWallet           | 🟢      | 🟢     | 🔴  | 🔴          | 🟢  | 🟢       |
| Electrum             | 🟢      | 🔴     | 🟢  | 🔴          | 🔴  | 🔴       |
| Keeper               | 🔴      | 🟢     | 🔴  | 🔴          | 🟢  | 🔴       |

I denna handledning kommer vi att konfigurera och använda Jade Plus med Blockstreams mobilapp Green Wallet via en Bluetooth-anslutning. Den här installationen är idealisk för nybörjare. Om du letar efter ett mer avancerat tillvägagångssätt rekommenderar jag att du tar en titt på den här handledningen där vi använder Jade Plus med Sparrow wallet i QR-kodläge:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

## Säkerhetsmodellen Jade Plus


Jade Plus använder en säkerhetsmodell som bygger på ett "virtuellt säkert element", materialiserat av ett "blint orakel". I konkreta termer kombinerar denna mekanism den PIN-kod som användaren valt, en hemlighet som finns på Jade och en hemlighet som finns hos oraklet (en server som drivs av Blockstream) för att skapa en AES-256-nyckel som distribueras över två enheter. Under initieringen säkrar en ECDH Exchange kommunikationen med oraklet och krypterar återställningsfrasen på Hardware Wallet. I praktiken, när du vill komma åt seed för att signera transaktioner, behöver du tillgång till :




- Till själva Jade Plus-enheten;
- PIN-kod för att låsa upp enheten ;
- Och till oraklets hemlighet.


Den stora fördelen med detta tillvägagångssätt är att det inte finns någon "single point of failure" på hårdvarunivå, eftersom en angripare som får tillgång till din Jade måste kompromettera både Jade och oraklet för att få ut nycklarna. Den här modellen innebär också att Jade Plus är helt öppen källkod, vilket gör att man undviker de begränsningar som är förknippade med användningen av verkligt fysiskt säkra Elements, som till exempel Ledger.


Nackdelen med detta system är att användningen av Jade Plus är beroende av det orakel som Blockstream upprätthåller. Om detta orakel blir oåtkomligt är det inte längre möjligt att använda Hardware Wallet direkt med PIN-koden. Detta innebär dock inte att dina bitcoins går förlorade, eftersom de fortfarande kan återvinnas med hjälp av din återställningsfras, som du kan ange i Jade Plus i "*stateless*"-läge. För att komma runt det här beroendet kan du också konfigurera och hantera din egen oracle-server.


## Uppackning av Jade Plus


När du får din Jade Plus, kontrollera att lådan och Seal är i gott skick för att säkerställa att ditt paket inte har öppnats.


![JADE-PLUS-GREEN](assets/fr/02.webp)


I lådan hittar du :




- Le Jade Plus;
- USB-C-kabel;
- Kort för att spela in din Mnemonic-fras som ord eller som "*CompactSeedQR*";
- Några instruktioner för användning ;
- En sladd;
- Några klistermärken.


![JADE-PLUS-GREEN](assets/fr/03.webp)


Enheten har 4 navigeringsknappar:




- Knappen längst ned till höger sätter på Jade;
- Den stora knappen på enhetens framsida används för att välja ett objekt;
- Med de två små knapparna längst upp kan du navigera till vänster och höger;
- Du kan också välja ett objekt genom att samtidigt klicka på de två knapparna längst upp på enheten.


![JADE-PLUS-GREEN](assets/fr/04.webp)


## Uppsättning av en ny Bitcoin Wallet


Klicka på startknappen.


![JADE-PLUS-GREEN](assets/fr/05.webp)


Klicka på "*Setup Jade*".


![JADE-PLUS-GREEN](assets/fr/06.webp)


Välj "Begin Setup". Alternativet "*Advanced Setup*" gör samma sak, men med tillgång till avancerade inställningar.


![JADE-PLUS-GREEN](assets/fr/07.webp)


Klicka sedan på "*Create a New Wallet*" för att skapa en ny generate seed.


![JADE-PLUS-GREEN](assets/fr/08.webp)


Klicka på knappen "*Continue*" för att visa din nya återställningsfras.


![JADE-PLUS-GREEN](assets/fr/09.webp)


Din Jade Plus visar din Mnemonic-fras med 12 ord. **Den här Mnemonic ger dig full, obegränsad tillgång till alla dina bitcoins. Vem som helst som har tillgång till denna fras kan stjäla dina pengar, även utan fysisk tillgång till din Jade Plus. Den 12 ord långa frasen återställer åtkomsten till dina bitcoins i händelse av förlust, stöld eller brott på din Jade. Det är därför mycket viktigt att spara den noggrant och förvara den på en säker plats.


Du kan skriva den på kartongen som medföljer i lådan, eller för extra säkerhet rekommenderar jag att du graverar den på en bas av rostfritt stål för att skydda den mot brand, översvämning eller kollaps.


![JADE-PLUS-GREEN](assets/fr/10.webp)


För mer information om det rätta sättet att spara och hantera din Mnemonic-fras rekommenderar jag starkt att du följer den här andra handledningen, särskilt om du är nybörjare:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

***Du får naturligtvis aldrig dela med dig av dessa ord på Internet, vilket jag gör i den här handledningen. Detta prov Wallet kommer endast att användas på Testnet och kommer att raderas i slutet av handledningen


Klicka på pilen till höger på skärmen för att visa följande ord.


![JADE-PLUS-GREEN](assets/fr/11.webp)


När du har sparat din fras ber Jade Plus dig att bekräfta den. Välj rätt ord enligt ordningen med hjälp av knapparna längst upp på enheten och klicka på mittknappen för att gå vidare till nästa ord.


![JADE-PLUS-GREEN](assets/fr/12.webp)


## Anslutning av Jade Plus till Green Wallet


I den här handledningen använder vi applikationen Green Wallet för att hantera Wallet som finns på Jade Plus. Den här metoden är särskilt lämplig för nybörjare. Om du vill hantera din Bitcoin Wallet mer i detalj kan du också använda Sparrow wallet, som vi kommer att behandla i en separat handledning:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

För instruktioner om hur du installerar och konfigurerar Blockstream Green-programmet, se första delen av denna andra handledning:


https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

När du är i applikationen Blockstream Green klickar du på knappen "*Konfigurera en ny Wallet*".


![JADE-PLUS-GREEN](assets/fr/13.webp)


Välj "*På Hardware Wallet*".


![JADE-PLUS-GREEN](assets/fr/14.webp)


Aktivera Bluetooth på din smartphone och klicka sedan på knappen "*Connect your Jade*".


![JADE-PLUS-GREEN](assets/fr/15.webp)


Auktorisera Green-programmet att få tillgång till Bluetooth-anslutningar.


![JADE-PLUS-GREEN](assets/fr/16.webp)


Applikationen söker efter din Jade Plus.


![JADE-PLUS-GREEN](assets/fr/17.webp)


På Jade Plus klickar du på menyn "*Bluetooth*".


![JADE-PLUS-GREEN](assets/fr/18.webp)


Välj din enhet i Green-applikationen.


![JADE-PLUS-GREEN](assets/fr/19.webp)


Bekräfta parkopplingskoden på din Jade Plus.


![JADE-PLUS-GREEN](assets/fr/20.webp)


Green erbjuder dig ett test för att säkerställa att din Jade är äkta. Klicka på knappen för att göra det.


![JADE-PLUS-GREEN](assets/fr/21.webp)


Bekräfta på Jade.


![JADE-PLUS-GREEN](assets/fr/22.webp)


Green bekräftar att din enhet är äkta.


![JADE-PLUS-GREEN](assets/fr/23.webp)


## Ställa in PIN-koden


Klicka på knappen "*Continue*" för att välja PIN-koden för din Jade.


![JADE-PLUS-GREEN](assets/fr/24.webp)


PIN-koden låser upp din Jade. Den utgör därför ett skydd mot obehörig fysisk åtkomst. Denna PIN-kod är inte inblandad i härledningen av din Wallet:s kryptografiska nycklar. Så även om du inte har tillgång till PIN-koden kan du få tillgång till dina bitcoins om du har tillgång till din Mnemonic-fras med 12 ord. Vi rekommenderar att du väljer en PIN-kod som är så slumpmässig som möjligt. Och se till att spara den här koden på en annan plats än där din Jade lagras (t.ex. i en lösenordshanterare).


Välj den 6-siffriga PIN-koden på din Jade genom att använda höger- och vänsterknapparna för att bläddra igenom siffrorna och mittknappen för att bekräfta inmatningen av en siffra.


![JADE-PLUS-GREEN](assets/fr/25.webp)


Bekräfta din PIN-kod en gång till.


![JADE-PLUS-GREEN](assets/fr/26.webp)


Din Bitcoin Wallet har skapats.


![JADE-PLUS-GREEN](assets/fr/27.webp)


## Skapa ett Bitcoin-konto


Du måste nu skapa ett konto i din Wallet. Klicka på knappen "*Create an account*" (*skapa ett konto*).


![JADE-PLUS-GREEN](assets/fr/28.webp)


Välj "*Standard*" om du vill skapa en klassisk Wallet med en enda signering.


![JADE-PLUS-GREEN](assets/fr/29.webp)


För mer information om alternativet "*2FA*" kan du följa denna andra handledning:


https://planb.network/tutorials/wallet/mobile/blockstream-green-2fa-37397d5c-5c27-44ad-a27a-c9ceac8c9df9

Ditt konto har skapats.


![JADE-PLUS-GREEN](assets/fr/30.webp)


Om du vill göra din Green Wallet personlig klickar du på de tre små prickarna längst upp till höger.


![JADE-PLUS-GREEN](assets/fr/31.webp)


Med alternativet "*Rename*" kan du anpassa namnet på din Wallet, vilket är särskilt användbart om du hanterar flera plånböcker i samma applikation. I menyn "*Unit*" kan du ändra grundenheten för din Wallet. Du kan t.ex. välja att visa den i satoshis i stället för bitcoins. Slutligen ger menyn "*Parameters*" dig tillgång till andra alternativ. Här hittar du till exempel din utökade publika nyckel och dess deskriptor, vilket är användbart om du planerar att konfigurera en Watch-only wallet från din Jade.


![JADE-PLUS-GREEN](assets/fr/32.webp)


För att återansluta till din Jade efter att ha stängt av den, tryck på på/av-knappen längst ned på enheten. I Green applikationen, välj din enhet från startsidan:


![JADE-PLUS-GREEN](assets/fr/33.webp)


Ange sedan PIN-koden på din Jade, så är du ansluten igen.


![JADE-PLUS-GREEN](assets/fr/34.webp)


Din Jade låses upp via Blockstreams "virtuella säkra element" (se första avsnittet i denna handledning). Detta kräver en Bluetooth-anslutning med Green-applikationen. Om du stöter på problem med Bluetooth-anslutningen under upplåsningen kan du prova att koppla bort och koppla ihop de två enheterna igen. Om problemet kvarstår kan du fortfarande låsa upp din Jade genom att välja alternativet "*QR Scan*" och följa instruktionerna som finns tillgängliga [på Blockstreams webbplats] (https://jadefw.blockstream.com/pinqr/index.html).


Innan du får dina första bitcoins i din Wallet, ** rekommenderar jag starkt att du utför ett tomt återställningstest**. Anteckna viss referensinformation, till exempel din xpub eller första mottagande Address, radera sedan din Wallet i Green-appen och på Jade Plus medan den fortfarande är tom (`Optioner -> Enhet -> Fabriksåterställning`). Försök sedan återställa din Wallet med hjälp av dina pappersbackuper av Mnemonic frasen. Kontrollera att cookieinformationen som genereras efter återställningen matchar den som du ursprungligen skrev ner. Om den gör det kan du vara säker på att dina pappersbackuper är tillförlitliga. Om du vill veta mer om hur du utför en teståterställning kan du läsa den här andra handledningen :


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Ta emot bitcoins


Nu när din Bitcoin Wallet är konfigurerad är du redo att ta emot din första Sats! Klicka bara på knappen "*Receive*" på Green-applikationen.


![JADE-PLUS-GREEN](assets/fr/35.webp)


Green visar en mottagning Address, men innan du använder den är det viktigt att kontrollera den på Jade för att bekräfta att den faktiskt tillhör vår Wallet. För att göra detta, klicka på knappen "*Verifiera på enheten*".


![JADE-PLUS-GREEN](assets/fr/36.webp)


Kontrollera på Jade att Address är samma som på Green och klicka sedan på knappen för att bekräfta.


![JADE-PLUS-GREEN](assets/fr/37.webp)


Du kan nu dela Address med betalaren för att ta emot bitcoins i din Wallet. När transaktionen sänds ut i nätverket kommer den att visas i din Wallet. Vänta tills du har fått tillräckligt många bekräftelser för att betrakta transaktionen som slutgiltig.


![JADE-PLUS-GREEN](assets/fr/38.webp)


## Skicka bitcoins


Med bitcoins i din Wallet kan du nu också skicka bitcoins. Klicka på "*Sänd*".


![JADE-PLUS-GREEN](assets/fr/39.webp)


På nästa sida anger du mottagarens Address. Du kan ange den manuellt eller skanna en QR-kod.


![JADE-PLUS-GREEN](assets/fr/40.webp)


Välj betalningsbelopp.


![JADE-PLUS-GREEN](assets/fr/41.webp)


Längst ner på skärmen kan du välja avgiftssats för den här transaktionen. Du kan välja att följa programmets rekommendationer eller anpassa dina avgifter. Ju högre avgift i förhållande till andra väntande transaktioner, desto snabbare kommer din transaktion att behandlas. För information om avgiftsmarknaden, besök [Mempool.space](https://Mempool.space/) i avsnittet "*Transaktionsavgifter*".


![JADE-PLUS-GREEN](assets/fr/42.webp)


Klicka på "*Nästa*" för att komma till skärmen för transaktionsöversikt. Kontrollera att Address, belopp och avgifter är korrekta.


![JADE-PLUS-GREEN](assets/fr/43.webp)


Om allt går bra skjuter du Green-knappen längst ned på skärmen åt höger för att signera och sända transaktionen i Bitcoin-nätverket.


![JADE-PLUS-GREEN](assets/fr/44.webp)


Du ombeds nu att bekräfta transaktionen på Jade.


![JADE-PLUS-GREEN](assets/fr/45.webp)


Kontrollera att mottagarens Address är korrekt. Klicka på bocken för att bekräfta.


![JADE-PLUS-GREEN](assets/fr/46.webp)


Kontrollera att debiteringsbeloppet är korrekt och validera sedan.


![JADE-PLUS-GREEN](assets/fr/47.webp)


Din transaktion har signerats och sänts från Green.


![JADE-PLUS-GREEN](assets/fr/48.webp)


Grattis, du vet nu hur du ställer in och använder Jade Plus med Blockstream Green mobilapplikation, via Bluetooth-anslutning. Om du tyckte att denna handledning var användbar skulle jag vara tacksam om du lämnade en Green-tumme nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack för att du delar med dig!


För att ta saker ett steg längre rekommenderar jag denna handledning om Jade Plus, där vi konfigurerar den med Sparrow wallet-programvaran i QR-läge. Du får också lära dig hur du använder de avancerade inställningarna för din Hardware Wallet:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262
