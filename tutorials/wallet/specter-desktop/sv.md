---
name: Specter skrivbord
description: Hantera dina Bitcoin-portföljer med flera signaturer i total suveränitet med din egen nod
---

![cover](assets/cover.webp)



Specter Desktop är en öppen källkodsapplikation (MIT-licens) utvecklad av Cryptoadvance sedan 2019 som underlättar hanteringen av Bitcoin-plånböcker med dina hårdvaruplånböcker (Ledger, Trezor, Coldcard, BitBox02, Passport, etc.) och din egen Bitcoin-infrastruktur (Bitcoin core-nod eller Electrum Server). Programmet utmärker sig särskilt i konfigurationer med flera signaturer, vilket gör att du kan säkra stora summor genom att fördela signeringskraften mellan flera oberoende hårdvaruplånböcker.



**I den här handledningen lär du dig hur du:**




- Installera och konfigurera Specter Desktop på din dator (Windows, macOS eller Linux)
- Anslut Specter till en Electrum Server (vi använder Umbrel i det här exemplet)
- Skapa en enkel Wallet med en Hardware Wallet (Coldcard)
- Ta emot och skicka bitcoins med fullständig suveränitet
- Uppsättning av en 2-mot-3 multisignatur Wallet med flera hårdvaruplånböcker
- Installera Specter på en Umbrel-server (avancerad bonus)



Alla dina transaktioner kommer att valideras lokalt via din egen infrastruktur, utan att överföra någon information till externa servrar, vilket garanterar din sekretess och finansiella suveränitet. Kontrollera alltid transaktionerna på din Hardware Wallet-skärm innan du signerar.



## Nedladdning och installation



Besök webbplatsen RECOMENDED # för att ladda ner applikationen.



![Page d'accueil Specter](assets/fr/01.webp)



På nedladdningssidan väljer du den version som motsvarar ditt operativsystem: macOS, Windows eller Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



När du har laddat ner programmet installerar du det enligt de vanliga instruktionerna för ditt operativsystem. För macOS drar du ikonen till Program. För Windows, kör installationsprogrammet. För Linux följer du instruktionerna i paketet.



## Inledande konfiguration



Vid första lanseringen ber Spectre Desktop dig att välja anslutningstyp. Du kan ansluta till en Electrum Server eller till din egen Bitcoin core-nod.



![Choix du type de connexion](assets/fr/03.webp)



I det här exemplet använder vi en anslutning till en Electrum Server som körs på Umbrel.



För mer information, se vår Umbrel-handledning:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Detta alternativ erbjuder snabbare synkronisering än Bitcoin core. Om du föredrar det kan du välja "Bitcoin core" och konfigurera anslutningen till din lokala nod. Följande steg är desamma oavsett vilket val du gör.



Välj "Electrum Connection" och välj sedan "Enter my own" för att konfigurera din egen Electrum Server.



![Configuration Electrum](assets/fr/04.webp)



Ange Address för din Electrum Server. I vårt fall med Umbrel kommer Address att vara `umbrel.local` med port `50001`. Klicka på "Connect" för att upprätta anslutningen.



När du är ansluten visas välkomstskärmen med en checklista som hjälper dig att komma igång. Du måste nu lägga till dina hårdvaruplånböcker.



![Écran d'accueil](assets/fr/05.webp)



## Lägga till en Hardware Wallet



I menyn till vänster klickar du på "Lägg till enhet" för att lägga till din Hardware Wallet.



Specter Desktop stöder många hårdvaruplånböcker: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault och många andra.



Om du vill lära dig mer kan du ta en titt på våra Hardware Wallet-handledningar.



![Sélection du type de hardware wallet](assets/fr/06.webp)



Välj din Hardware Wallet. I det här exemplet använder vi en Coldcard MK4.



Nedan hittar du vår handledning för denna Hardware Wallet :



https://planb.network/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

För ett Coldcard måste du exportera de publika nycklarna från Hardware Wallet antingen via en USB-anslutning eller ett microSD-kort.



![Import des clés du Coldcard](assets/fr/07.webp)



Följ instruktionerna som visas för att exportera nycklarna från ditt Coldcard. Ge din Hardware Wallet ett namn (här "MK4 Tuto"). När nycklarna har importerats kan du skapa en Wallet med en enda nyckel, eller lägga till andra hårdvaruplånböcker för en Wallet med flera signaturer.



![Dispositif ajouté](assets/fr/08.webp)



## Skapande av portfölj



När du har lagt till din Hardware Wallet klickar du på "Create single key Wallet" för att skapa en Wallet med en enda signatur.



Ge din portfölj ett namn (t.ex. "Wallet för tuto") och välj typen Address. Välj "SegWit" för att använda inbyggda BECH32-adresser, vilket optimerar transaktionskostnaderna.



![Configuration du portefeuille](assets/fr/09.webp)



När din portfölj har skapats erbjuder Specter att spara en backup PDF-fil som innehåller all publik information som behövs för att återställa din portfölj (descriptors, extended public keys). Denna fil innehåller inte dina privata nycklar.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Ta emot bitcoins



För att ta emot bitcoins väljer du din Wallet i menyn till vänster och klickar sedan på fliken "Receive".



Specter genererar automatiskt en ny reception Address med en QR-kod.



![Génération d'une adresse de réception](assets/fr/11.webp)



Du kan kopiera Address eller skanna QR-koden. Kontrollera alltid Address på din Hardware Wallet-skärm innan du skickar den vidare till någon.



## Visa historik och adresser



När du har tagit emot bitcoins kan du se dina transaktioner på fliken "Transaktioner".



![Historique des transactions](assets/fr/12.webp)



På fliken "Adresser" kan du se alla adresser som genererats av din portfölj, med deras användningsstatus och tillhörande belopp.



![Liste des adresses](assets/fr/13.webp)



## Skicka bitcoins



För att skicka bitcoins klickar du på fliken "Skicka". Ange mottagarens Address, beloppet som ska skickas och kontrollera de avancerade alternativen om du vill välja UTXO:erna manuellt (Coin-kontroll).



![Création d'une transaction](assets/fr/14.webp)



Klicka på "Create Unsigned Transaction" för att skapa transaktionen. Specter kommer sedan att be dig att signera transaktionen med din Hardware Wallet.



![Signature de la transaction](assets/fr/15.webp)



Om du använder ett Coldcard kan du välja att signera via USB eller med microSD-kortet (air-gapped). Bekräfta transaktionen på din Hardware Wallet-skärm och kontrollera noggrant destinationen Address och beloppet.



När transaktionen har undertecknats kan du sända den i Bitcoin-nätverket.



![Options de diffusion](assets/fr/16.webp)



Klicka på "Skicka transaktion" för att skicka transaktionen. Specter kommer att bekräfta att din transaktion har skickats och du kan följa dess status under fliken Transaktioner.



![Diffusion de la transaction](assets/fr/17.webp)



## Skapa och använda en portfölj med flera signaturer



En av Specter Desktops största tillgångar är dess förmåga att förenkla hanteringen av portföljer med flera signaturer. En Multisig Wallet kräver flera signaturer för att godkänna en transaktion, vilket eliminerar den enda felkällan. En 2-on-3-konfiguration, till exempel, kräver två signaturer från tre separata hårdvaruplånböcker för att validera en utgift.



För att skapa en Multisig Wallet, börja med att lägga till alla undertecknande hårdvaruplånböcker via "Lägg till enhet". I det här exemplet kommer vi att använda tre olika hårdvaruplånböcker: ett Coldcard MK4 (redan tillagt tidigare), ett Passport och en Ledger. Denna diversifiering av tillverkare stärker säkerheten genom att undvika beroende av en enda Supply-kedja eller firmware.



Här är länkarna till Ledger och Passport tutorials:



https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Lägg till Passport genom att namnge Hardware Wallet (t.ex. "Passport multi") och importera dess nycklar via microSD-kort eller QR-kod. Klicka sedan på "Fortsätt" för att fortsätta.



![Ajout du Passport](assets/fr/23.webp)



Lägg sedan till Ledger genom att ansluta den via USB och öppna Bitcoin-programmet på Hardware Wallet. Ge den ett namn (t.ex. "Ledger multi") och klicka på "Hämta via USB" och sedan "Fortsätt" för att importera dess publika nycklar.



![Ajout du Ledger](assets/fr/24.webp)



När du har registrerat dina tre hårdvaruplånböcker i Specter klickar du på "Lägg till Wallet" och väljer alternativet "Flera signaturer" för att skapa en Wallet med flera signaturer.



![Choix du type de wallet](assets/fr/25.webp)



Välj de tre hårdvaruplånböcker som du vill inkludera i ditt multisignaturkvorum: MK4 Tuto, Passport multi och Ledger multi. Klicka på "Fortsätt" för att gå vidare till nästa steg.



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Välj din konfiguration för flera signaturer. Välj "SegWit" som Address-typ för att dra nytta av optimerade avgifter. Med parametern "Nödvändiga signaturer för att auktorisera transaktioner (m av 3)" kan du definiera tröskeln: för en 2-på-3-konfiguration krävs 2 signaturer. Varje Hardware Wallet visar sin motsvarande Multisig-nyckel. Klicka på "Skapa Wallet" för att slutföra skapandet.



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



Din multisignaturportfölj "Multi tuto" är nu skapad. Specter rekommenderar omedelbart att du sparar säkerhetskopian av PDF-filen som innehåller portföljen Descriptor. Klicka på "Save Backup PDF" för att ladda ner denna viktiga fil.



![Wallet multisig créé](assets/fr/28.webp)



Specter låter dig också exportera Wallet-information till var och en av dina hårdvaruplånböcker via QR-kod eller fil. Detta gör att vissa hårdvaruplånböcker (t.ex. Coldcard eller Passport) kan lagra Multisig-konfigurationen direkt i sitt minne.



För Passport låser du upp din enhet och går till "Manage Account" > "Connect Wallet" > "Specter" > "Multisig" > "QR Code" och skannar sedan QR-koden som genereras av Specter. Ditt Passport kommer sedan att be dig att skanna en mottagande Address från din Wallet för att validera Multisig-konfigurationen.



För MK4, anslut den till din PC och lås upp den. Klicka sedan på "Save MK4 Tuto file" och spara filen på din MK4. Nästa gång du signerar din Hardware Wallet kommer MK4 att använda den här filen för att slutföra konfigurationen av Multisig.



![Export vers les hardware wallets](assets/fr/29.webp)



För din information kan du när som helst komma åt säkerhetskopior från fliken "Inställningar" i din portfölj och sedan "Exportera":



![Accès au backup PDF](assets/fr/30.webp)



Den dagliga användningen förblir lik en enkel Wallet: du generate tar emot adresser som vanligt. För att skicka bitcoins, gå till fliken "Skicka", ange mottagarens Address och beloppet och klicka sedan på "Skapa osignerad transaktion".



![Création d'une transaction multisig](assets/fr/31.webp)



Specter bygger en PSBT (Partially Signed Bitcoin Transaction) och visar "Acquired 0 of 2 signatures". Du måste nu signera med minst två av dina tre hårdvaruplånböcker. Klicka på den första Hardware Wallet (t.ex. "MK4 Tuto") för att signera med ditt Coldcard, och sedan på den andra (t.ex. "Passport multi") för att få den andra signaturen som krävs.



![Signature de la transaction](assets/fr/32.webp)



När du har fått de 2 nödvändiga signaturerna (Interface visar "Acquired 2 of 2 signatures" och "Transaction is ready to send") klickar du på "Send Transaction" för att sända transaktionen i Bitcoin-nätverket.



![Transaction prête à être diffusée](assets/fr/33.webp)



Denna metod med flera signaturer lämpar sig särskilt väl för företag (flera chefer måste godkänna utgifter), familjer (skydd av ett arv i flera generationer) eller individer som hanterar stora summor (geografisk distribution av hårdvaruplånböcker för att motstå lokala katastrofer).



### Den avgörande betydelsen av säkerhetskopior med flera signaturer



**Observera**: säkerhetskopiering av en portfölj med flera signaturer skiljer sig fundamentalt från säkerhetskopiering av en enskild portfölj. Dina återställningsfraser (seed-fraser) är inte tillräckliga för att återställa en Multisig-portfölj. Du måste också säkerhetskopiera **output descriptor** (output descriptor), som innehåller konfigurationsinformationen för din multisignaturportfölj.



output descriptor innehåller viktiga data: de utökade publika nycklarna (xpubs) för varje medundertecknare, signaturtröskeln (2 mot 3 i vårt exempel), typen av skript som används (SegWit native, nested eller legacy) och härledningsvägarna för varje Hardware Wallet. Utan denna Descriptor kommer du, även om du har två av dina tre återställningsfraser, inte att kunna bygga om din Wallet eller komma åt dina bitcoins. Descriptor låter din programvara veta hur man kombinerar de publika nycklarna till generate Bitcoin-adresserna som motsvarar dina medel.



Specter Desktop genererar automatiskt en backup-PDF-fil när du skapar din Multisig-portfölj. Denna PDF innehåller den kompletta Descriptor, fingeravtrycken för varje Hardware Wallet och all offentlig information som krävs för återställning. **Den här filen innehåller inte dina privata nycklar** och tillåter dig därför inte i sig att spendera dina bitcoins, men den tillåter alla som får tillgång till den att se din fullständiga transaktionshistorik och saldo.



Gör så här för att säkerhetskopiera din multisignaturkonfiguration korrekt: När du har skapat din portfölj klickar du på fliken "Inställningar", sedan på "Exportera" och väljer "Spara säkerhetskopierad PDF". Skapa flera kopior av den här PDF-filen: skriv ut minst två kopior på papper och spara även en krypterad digital kopia. Förvara en kopia av PDF-filen med var och en av dina återställningsfraser på geografiskt åtskilda platser.



Bränn dina återställningsfraser på brandsäkra och vattentäta metallplattor för att garantera deras livslängd. Underskatta aldrig vikten av dessa säkerhetskopior: om du förlorar din dators `~/.specter`-mapp OCH du förlorar en av dina hårdvaruplånböcker utan en Descriptor-säkerhetskopia, kommer alla dina medel att vara oåterkalleligt förlorade, även med en 2-på-3-konfiguration. Redundans med flera signaturer skyddar mot förlust av en Hardware Wallet, men endast om du har säkerhetskopierat din Wallet:s Descriptor korrekt.



## Fördelar och begränsningar med Specter Desktop



**Fördelar**: Optimal sekretess med fullständig lokal validering utan tredjepartsservrar. Flexibilitet med flera signaturer för avancerade konfigurationer (företag, familj, individ). Omfattande Hardware Wallet-stöd med full interoperabilitet (USB och luftgap).



**Begränsningar**: Betydande inlärningskurva för avancerade Bitcoin-koncept (UTXO:er, deskriptorer, härledningsvägar).



## Bästa praxis



Kontrollera alltid adresser och belopp på din Hardware Wallet-skärm före validering för att skydda dig mot skadlig kod.



Håll PDF-säkerhetskopior åtskilda från dina frön. Dessa offentliga beskrivningar kan lagras i ett bankvalv eller krypterat moln, vilket underlättar återställning utan att avslöja dina privata nycklar.



Testa återställning på token-belopp innan du använder dina portföljer med stora fonder. Skapa, testa, ta bort och återställ för att validera dina rutiner.



Håll Specter och din firmware uppdaterade. Fördela dina medundertecknare med flera signaturer geografiskt (hem/kontor/närliggande) för att motstå lokala katastrofer. Använd beskrivande etiketter för att underlätta bokföring och skattedeklarationer.



## Bonus: Installation på en Bitcoin-server (Umbrel, RaspiBlitz, Start9)



Om du redan äger en Bitcoin-server som Umbrel, RaspiBlitz, MyNode eller Start9 kan du installera Specter Desktop direkt från deras applikationsbutik. Detta tillvägagångssätt erbjuder flera betydande fördelar: applikationen konfigurerar sig automatiskt med din lokala Bitcoin core-nod, den förblir tillgänglig 24/7 via en Interface-webb från vilken enhet som helst i ditt nätverk, och du kan till och med komma åt den säkert på distans via Tor. Hela din Bitcoin-infrastruktur är centraliserad på en enda dedikerad server, vilket förenklar hanteringen och stärker din suveränitet.



### Installation från Umbrel App Store



Från din Umbrel Interface, gå till App Store och sök efter Specter Desktop. Klicka på "Installera" för att starta installationen.



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



När installationen är klar öppnar du Specter Desktop på din Umbrel. Välkomstskärmen kommer att be dig att välja din anslutningstyp. Om du använder Specter på din Umbrel, klicka på "Uppdatera inställningar" för att konfigurera anslutningen.



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



Välj "Remote Specter USB connection" för att möjliggöra användning av USB-hårdvaruplånböcker som är anslutna till din lokala dator när du använder Specter på Umbrel-fjärrservern.



![Configuration Remote Specter USB](assets/fr/20.webp)



Följ instruktionerna som visas för att konfigurera HWI Bridge. Du måste komma åt enhetens brygginställningar och lägga till domänen `http://umbrel.local:25441` i vitlistan. Klicka på "Update" för att spara konfigurationen.



![HWI Bridge Settings](assets/fr/21.webp)



Om du också vill använda dina USB-hårdvaruplånböcker från din lokala dator, ladda ner Specter Desktop-programmet till din maskin och ställ in det på "Ja, jag kör Specter på distans". Klicka på "Save" för att slutföra konfigurationen.



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## Slutsats



Specter Desktop demokratiserar avancerade Bitcoin-konfigurationer och gör multisignaturer tillgängliga utan att göra avkall på suveränitet eller sekretess. För användare som hanterar betydande summor pengar omvandlas institutionella metoder till lösningar som kan användas av privatpersoner.



Även om applikationen kräver en initial investering i infrastruktur och utbildning erbjuder den fullständig suveränitet: kontroll över valideringsinfrastrukturen, fysisk Ownership av nycklar och transaktioner som är fria från övervakning från tredje part. Oavsett om du är en privatperson som skyddar dina besparingar, en familj som skapar ett bankfack för flera generationer eller ett företag som hanterar kassaflödet, är Specter Desktop referensverktyget för att förena maximal säkerhet och absolut suveränitet.



## Resurser



### Officiell dokumentation




- [Specter Desktop officiella webbplats](https://specter.solutions/desktop/)
- [GitHub-källkod] (https://github.com/cryptoadvance/specter-desktop)
- [Komplett dokumentation] (https://docs.specter.solutions/)



### Gemenskap och stöd




- [Telegram Specter Community Group] (https://t.me/spectersupport)
- [Reddit diskussionsforum](https://reddit.com/r/specterdesktop/)
- [GitHub buggrapporter] (https://github.com/cryptoadvance/specter-desktop/issues)