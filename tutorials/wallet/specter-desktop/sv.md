---
name: Specter Desktop
description: Hantera dina Bitcoin-portföljer med flera signaturer i total suveränitet med din egen nod
---

![cover](assets/cover.webp)



Spectre Desktop är ett program med öppen källkod (MIT-licens) som utvecklats av Cryptoadvance sedan 2019 och som underlättar hanteringen av Bitcoin-plånböcker med dina hårdvaruplånböcker (Ledger, Trezor, Coldcard, BitBox02, Passport, etc.) och din egen Bitcoin-infrastruktur (Bitcoin Core-nod eller Electrum-server). Programmet utmärker sig särskilt i konfigurationer med flera signaturer, vilket gör att du kan säkra stora summor genom att fördela signeringskraften mellan flera oberoende hårdvaruplånböcker.



**I den här handledningen lär du dig hur du:**




- Installera och konfigurera Specter Desktop på din dator (Windows, macOS eller Linux)
- Anslut Specter till en Electrum-server (vi använder Umbrel i det här exemplet)
- Skapa en enkel wallet med wallet-hårdvara (Coldcard)
- Ta emot och skicka bitcoins med fullständig suveränitet
- Uppsättning av en 2-mot-3 multisignatur wallet med flera hårdvaruplånböcker
- Installera Specter på en Umbrel-server (avancerad bonus)



Alla dina transaktioner kommer att valideras lokalt via din egen infrastruktur, utan att överföra någon information till externa servrar, vilket garanterar din sekretess och finansiella suveränitet. Kontrollera alltid transaktionerna på skärmen på din wallet-hårdvara innan du signerar.



## Nedladdning och installation



Besök webbplatsen RECOMENDED # för att ladda ner applikationen.



![Page d'accueil Specter](assets/fr/01.webp)



På nedladdningssidan väljer du den version som motsvarar ditt operativsystem: macOS, Windows eller Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



När du har laddat ner programmet installerar du det enligt de vanliga instruktionerna för ditt operativsystem. För macOS drar du ikonen till Program. För Windows, kör installationsprogrammet. För Linux följer du instruktionerna i paketet.



## Inledande konfiguration



Vid första lanseringen ber Spectre Desktop dig att välja din anslutningstyp. Du kan ansluta till en Electrum-server eller till din egen Bitcoin Core-nod.



![Choix du type de connexion](assets/fr/03.webp)



I det här exemplet använder vi en anslutning till en Electrum-server som körs på Umbrel.



För mer information, se vår Umbrel-handledning:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Detta alternativ erbjuder snabbare synkronisering än Bitcoin Core. Om du föredrar det kan du välja "Bitcoin Core" och konfigurera anslutningen till din lokala nod. Följande steg är desamma oavsett vilket val du gör.



Välj "Electrum Connection" och välj sedan "Enter my own" för att konfigurera din egen Electrum-server.



![Configuration Electrum](assets/fr/04.webp)



Ange adressen till din Electrum-server. I vårt fall med Umbrel kommer adressen att vara `umbrel.local` med port `50001`. Klicka på "Connect" för att upprätta anslutningen.



När du är ansluten visas välkomstskärmen med en checklista som hjälper dig att komma igång. Du måste nu lägga till dina hårdvaruplånböcker.



![Écran d'accueil](assets/fr/05.webp)



## Lägga till wallet-hårdvara



I menyn till vänster klickar du på "Lägg till enhet" för att lägga till din wallet-hårdvara.



Specter Desktop stöder många hårdvaruplånböcker: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault och många andra.



Om du vill lära dig mer kan du ta en titt på våra handledningar för hårdvara wallet.



![Sélection du type de hardware wallet](assets/fr/06.webp)



Välj din wallet-hårdvara. I det här exemplet använder vi en Coldcard MK4.



Nedan hittar du vår handledning för denna wallet-hårdvara:



https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

För ett Coldcard måste du exportera de publika nycklarna från wallet-hårdvaran antingen via en USB-anslutning eller ett microSD-kort.



![Import des clés du Coldcard](assets/fr/07.webp)



Följ instruktionerna som visas för att exportera nycklarna från ditt Coldcard. Ge din wallet-hårdvara ett namn (här "MK4 Tuto"). När nycklarna har importerats kan du skapa en wallet med en enda nyckel, eller lägga till andra hårdvaruplånböcker för en wallet med flera signaturer.



![Dispositif ajouté](assets/fr/08.webp)



## Skapande av portfölj



När du har lagt till din wallet-hårdvara klickar du på "Create single key wallet" för att skapa en wallet med en enda signatur.



Ge din portfölj ett namn (t.ex. "Wallet for tuto") och välj adresstyp. Välj "Segwit" för att använda inbyggda bech32-adresser som optimerar transaktionskostnaderna.



![Configuration du portefeuille](assets/fr/09.webp)



När din portfölj har skapats erbjuder Specter att spara en backup PDF-fil som innehåller all publik information som behövs för att återställa din portfölj (descriptors, extended public keys). Denna fil innehåller inte dina privata nycklar.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Ta emot bitcoins



För att ta emot bitcoins väljer du din wallet i menyn till vänster och klickar sedan på fliken "Receive".



Specter genererar automatiskt en ny mottagningsadress med en QR-kod.



![Génération d'une adresse de réception](assets/fr/11.webp)



Du kan kopiera adressen eller skanna QR-koden. Kontrollera alltid adressen på skärmen på din wallet-maskinvara innan du skickar den vidare till någon.



## Visa historik och adresser



När du har tagit emot bitcoins kan du se dina transaktioner på fliken "Transaktioner".



![Historique des transactions](assets/fr/12.webp)



På fliken "Adresser" kan du se alla adresser som genererats av din portfölj, med deras användningsstatus och tillhörande belopp.



![Liste des adresses](assets/fr/13.webp)



## Skicka bitcoins



För att skicka bitcoins klickar du på fliken "Skicka". Ange mottagarens adress, beloppet som ska skickas och kontrollera de avancerade alternativen om du vill välja UTXO:erna manuellt (myntkontroll).



![Création d'une transaction](assets/fr/14.webp)



Klicka på "Create Unsigned Transaction" för att skapa transaktionen. Specter kommer sedan att be dig att signera transaktionen med din wallet-hårdvara.



![Signature de la transaction](assets/fr/15.webp)



Om du använder ett Coldcard kan du välja att signera via USB eller med microSD-kortet (air-gapped). Bekräfta transaktionen på skärmen på din wallet-maskinvara och kontrollera noggrant destinationsadressen och beloppet.



När transaktionen har undertecknats kan du sända den i Bitcoin-nätverket.



![Options de diffusion](assets/fr/16.webp)



Klicka på "Skicka transaktion" för att skicka transaktionen. Specter kommer att bekräfta att din transaktion har skickats och du kan följa dess status under fliken Transaktioner.



![Diffusion de la transaction](assets/fr/17.webp)



## Skapa och använda en portfölj med flera signaturer



En av Specter Desktops stora tillgångar är dess förmåga att förenkla hanteringen av portföljer med flera signaturer. En multisig wallet kräver flera signaturer för att auktorisera en transaktion, vilket eliminerar den enda felkällan. En 2-on-3-konfiguration kräver till exempel två signaturer från tre separata hårdvaruplånböcker för att validera en utgift.



För att skapa en multisig wallet börjar du med att lägga till alla signerande hårdvaruplånböcker via "Lägg till enhet". I det här exemplet kommer vi att använda tre olika hårdvaruplånböcker: ett Coldcard MK4 (redan tillagt tidigare), ett Passport och en Ledger. Denna diversifiering av tillverkare stärker säkerheten genom att undvika beroende av en enda leveranskedja eller firmware.



Här är länkarna till Ledger och Passport tutorials:



https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Lägg till Passport genom att namnge wallet-hårdvaran (t.ex. "Passport multi") och importera dess nycklar via microSD-kort eller QR-kod. Klicka sedan på "Fortsätt" för att fortsätta.



![Ajout du Passport](assets/fr/23.webp)



Lägg sedan till Ledger genom att ansluta den via USB och öppna Bitcoin-programmet på wallet-hårdvaran. Namnge den (t.ex. "ledger multi") och klicka på "Hämta via USB" och sedan på "Fortsätt" för att importera dess publika nycklar.



![Ajout du Ledger](assets/fr/24.webp)



När du har registrerat dina tre hårdvaruplånböcker i Specter klickar du på "Lägg till wallet" och väljer alternativet "Flera signaturer" för att skapa en wallet med flera signaturer.



![Choix du type de wallet](assets/fr/25.webp)



Välj de tre hårdvaruplånböcker som du vill inkludera i ditt multisignaturkvorum: MK4 Tuto, Passport multi och ledger multi. Klicka på "Fortsätt" för att gå vidare till nästa steg.



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Välj din konfiguration för flera signaturer. Välj "Segwit" som adresstyp för att dra nytta av optimerade avgifter. Med parametern "Nödvändiga signaturer för att auktorisera transaktioner (m av 3)" kan du definiera tröskeln: för en 2-på-3-konfiguration krävs 2 signaturer. Varje wallet-maskinvara visar sin motsvarande multisig-nyckel. Klicka på "Skapa wallet" för att slutföra skapandet.



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



Din multisignaturportfölj "Multi tuto" är nu skapad. Specter rekommenderar omedelbart att du sparar den säkerhetskopierade PDF-filen som innehåller portföljbeskrivningen. Klicka på "Save Backup PDF" för att ladda ner denna viktiga fil.



![Wallet multisig créé](assets/fr/28.webp)



Med Specter kan du också exportera wallet-information till var och en av dina hårdvaruplånböcker via QR-kod eller fil. Detta gör att vissa hårdvaruplånböcker (t.ex. Coldcard eller Passport) kan lagra multisigkonfiguration direkt i sitt minne.



För Passport, lås upp din enhet och gå sedan till "Hantera konto" > "Anslut Wallet" > "Specter" > "Multisig" > "QR-kod" och skanna sedan QR-koden som genereras av Specter. Ditt Passport kommer sedan att be dig att skanna en mottagningsadress från din wallet för att validera multisig-konfigurationen.



För MK4, anslut den till din PC och lås upp den. Klicka sedan på "Save MK4 Tuto file" och spara filen på din MK4. Nästa gång du signerar din wallet-maskinvara kommer MK4 att använda den här filen för att slutföra konfigurationen av multisig.



![Export vers les hardware wallets](assets/fr/29.webp)



För din information kan du när som helst komma åt säkerhetskopior från fliken "Inställningar" i din portfölj och sedan "Exportera":



![Accès au backup PDF](assets/fr/30.webp)



Den dagliga användningen förblir lik en enkel wallet: du generate mottagande adresser som normalt. För att skicka bitcoins, gå till fliken "Skicka", ange mottagarens adress och beloppet och klicka sedan på "Skapa osignerad transaktion".



![Création d'une transaction multisig](assets/fr/31.webp)



Specter bygger en PSBT (Partially Signed Bitcoin Transaction) och visar "Acquired 0 of 2 signatures". Du måste nu signera med minst två av dina tre hårdvaruplånböcker. Klicka på den första wallet-hårdvaran (t.ex. "MK4 Tuto") för att signera med ditt Coldcard, sedan på den andra (t.ex. "Passport multi") för att få den andra signaturen som krävs.



![Signature de la transaction](assets/fr/32.webp)



När du har fått de två nödvändiga signaturerna (gränssnittet visar "Acquired 2 of 2 signatures" och "Transaction is ready to send") klickar du på "Send Transaction" för att sända transaktionen i Bitcoin-nätverket.



![Transaction prête à être diffusée](assets/fr/33.webp)



Denna metod med flera signaturer lämpar sig särskilt väl för företag (flera chefer måste godkänna utgifter), familjer (skydd av ett arv i flera generationer) eller individer som hanterar stora summor (geografisk distribution av hårdvaruplånböcker för att motstå lokala katastrofer).



### Den avgörande betydelsen av säkerhetskopior med flera signaturer



**Observera**: säkerhetskopiering av en multisig-portfölj är fundamentalt annorlunda än säkerhetskopiering av en enskild portfölj. Dina återställningsfraser (seed-fraser) räcker inte ensamma för att återställa en multisig-portfölj. Du måste också säkerhetskopiera **output descriptor** (output descriptor), som innehåller konfigurationsinformationen för din multisig-portfölj.



output descriptor innehåller viktiga data: de utökade publika nycklarna (xpubs) för varje medundertecknare, signaturtröskeln (2 mot 3 i vårt exempel), typen av script som används (native, nested eller legacy Segwit) och förbikopplingsvägarna för varje wallet-hårdvara. Utan denna deskriptor kommer du inte att kunna återuppbygga din wallet eller komma åt dina bitcoins, även om du har två av dina tre återställningsfraser. Deskriptorn låter din programvara veta hur man kombinerar de publika nycklarna till generate Bitcoin-adresserna som motsvarar dina medel.



Specter Desktop genererar automatiskt en säkerhetskopierad PDF-fil när du skapar din multisig-portfölj. Denna PDF innehåller den fullständiga deskriptorn, fingeravtrycken för varje wallet-hårdvara och all offentlig information som krävs för återställning. **Den här filen innehåller inte dina privata nycklar** och tillåter dig därför inte i sig att spendera dina bitcoins, men den tillåter alla som får tillgång till den att se din fullständiga transaktionshistorik och saldo.



Gör så här för att säkerhetskopiera din multisignaturkonfiguration korrekt: När du har skapat din portfölj klickar du på fliken "Inställningar", sedan på "Exportera" och väljer "Spara säkerhetskopierad PDF". Skapa flera kopior av den här PDF-filen: skriv ut minst två kopior på papper och spara även en krypterad digital kopia. Förvara en kopia av PDF-filen med var och en av dina återställningsfraser på geografiskt åtskilda platser.



Gravera in dina återställningsfraser på brandsäkra och vattentäta metallplattor för att garantera deras livslängd. Underskatta aldrig vikten av dessa säkerhetskopior: om du förlorar mappen `~/.specter` på din dator OCH du förlorar en av dina hårdvaruplånböcker utan en säkerhetskopia av deskriptorn, kommer alla dina medel att vara oåterkalleligt förlorade, även med en 2-på-3-konfiguration. Redundans med flera signaturer skyddar mot förlust av wallet-hårdvara, men endast om du har säkerhetskopierat din wallet:s descriptor korrekt.



## Fördelar och begränsningar med Specter Desktop



**Fördelar**: Optimal sekretess med fullständig lokal validering utan tredjepartsservrar. Flexibilitet med flera signaturer för avancerade konfigurationer (företag, familj, individ). Omfattande stöd för wallet-hårdvara med full interoperabilitet (USB och luftgap).



**Begränsningar**: Betydande inlärningskurva för avancerade Bitcoin-koncept (UTXO:er, deskriptorer, härledningsvägar).



## Bästa praxis



Kontrollera alltid adresser och belopp på din hårdvara wallet-skärm före validering för att skydda dig mot skadlig kod.



Håll PDF-säkerhetskopior åtskilda från dina frön. Dessa offentliga beskrivningar kan lagras i ett bankvalv eller krypterat moln, vilket underlättar återställning utan att avslöja dina privata nycklar.



Testa återställning på token-belopp innan du använder dina portföljer med stora medel. Skapa, testa, ta bort och återställ för att validera dina rutiner.



Håll Specter och din firmware uppdaterade. Fördela dina medundertecknare med flera signaturer geografiskt (hem/kontor/närliggande) för att motstå lokala katastrofer. Använd beskrivande etiketter för att underlätta bokföring och skattedeklarationer.



## Bonus: Installation på en Bitcoin-server (Umbrel, RaspiBlitz, Start9)



Om du redan äger en Bitcoin-server som Umbrel, RaspiBlitz, MyNode eller Start9 kan du installera Specter Desktop direkt från deras applikationsbutik. Detta tillvägagångssätt erbjuder flera betydande fördelar: applikationen konfigurerar sig automatiskt med din lokala Bitcoin Core-nod, den förblir tillgänglig 24/7 via ett webbgränssnitt från vilken enhet som helst i ditt nätverk och du kan till och med komma åt den säkert på distans via Tor. Hela din Bitcoin-infrastruktur är centraliserad på en enda dedikerad server, vilket förenklar hanteringen och stärker din suveränitet.



### Installation från Umbrel App Store



Från ditt Umbrel-gränssnitt, gå till App Store och sök efter Specter Desktop. Klicka på "Installera" för att starta installationen.



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



Specter Desktop demokratiserar avancerade Bitcoin-konfigurationer och gör multisignatur tillgänglig utan att offra din suveränitet eller sekretess. För användare som hanterar betydande summor pengar omvandlas institutionella metoder till lösningar som kan användas av privatpersoner.



Även om applikationen kräver en initial investering i infrastruktur och utbildning, erbjuder den fullständig suveränitet: kontroll över valideringsinfrastrukturen, fysiskt ägande av nycklar och transaktioner som är fria från övervakning från tredje part. Oavsett om du är en privatperson som säkrar dina besparingar, en familj som skapar ett bankfack för flera generationer eller ett företag som hanterar kassaflödet, är Specter Desktop referensverktyget för att förena maximal säkerhet och absolut suveränitet.



## Resurser



### Officiell dokumentation




- [Specter Desktop officiella webbplats](https://specter.solutions/desktop/)
- [GitHub-källkod] (https://github.com/cryptoadvance/specter-desktop)
- [Komplett dokumentation] (https://docs.specter.solutions/)



### Gemenskap och stöd




- [Telegram Specter Community Group] (https://t.me/spectersupport)
- [Reddit diskussionsforum](https://reddit.com/r/specterdesktop/)
- [GitHub buggrapporter] (https://github.com/cryptoadvance/specter-desktop/issues)