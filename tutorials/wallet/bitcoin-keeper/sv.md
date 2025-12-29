---
name: Bitcoin Keeper
description: Bitcoin mobil wallet för säkerhet och multi-sig
---

![cover](assets/cover.webp)



Den säkra hanteringen av bitcoins utgör en stor utmaning för alla innehavare som är medvetna om vad som står på spel när det gäller finansiell suveränitet. Mellan enkelheten hos en mobil wallet och robustheten hos en multi-sig-lösning kan det tekniska gapet verka skrämmande för många användare. Bitcoin Keeper är placerad precis i denna skärningspunkt och erbjuder en progressiv strategi för säkerhet som följer med användarna när de utvecklas.



Bitcoin Keeper är en mobilapplikation med öppen källkod som är exklusivt avsedd för Bitcoin och som utvecklats av BitHyve-teamet. Ambitionen är att göra avancerad portföljhantering tillgänglig, särskilt konfigurationer med flera signaturer, samtidigt som man behåller ett intuitivt gränssnitt för nybörjare. Applikationen har sloganen "Secure today, Plan for tomorrow", vilket återspeglar dess filosofi om långsiktigt stöd.



Till skillnad från generalistiska plånböcker som hanterar flera kryptovalutor har Bitcoin Keeper ett strikt fokus på Bitcoin. Detta tillvägagångssätt med enbart bitcoin minskar den potentiella attackytan och förenklar användarupplevelsen avsevärt. Applikationen utmärker sig också för sin inbyggda integration av de mest utbredda hårdvaruplånböckerna och sina avancerade UTXO-hanteringsfunktioner.



## Vad är Bitcoin Keeper?



### Filosofi och mål



Bitcoin Keeper utformades för att möta de specifika behoven hos bitcoiners som vill behålla full kontroll över sina privata nycklar. Projektet omfattar helt de grundläggande principerna i Bitcoin: öppen och granskningsbar källkod, respekt för integritet och användarsuveränitet. Ingen registrering eller personlig information krävs för att använda applikationen, och den kan till och med köras offline för signeringsoperationer.



Det centrala målet är att erbjuda ett flexibelt, framtidssäkert verktyg för lagring av BTC under flera år, och till och med flera generationer, tack vare arvsfunktionaliteten. Applikationen gör det möjligt för användare att börja med en mobil wallet och sedan gradvis utvecklas mot säkrare lösningar med flera signaturer.



### Applikationsarkitektur



Bitcoin Keeper organiserar fondförvaltningen kring två distinkta koncept. **Hot Wallet** är en enkel wallet med en nyckel, som lagras i telefonen och är utformad för dagliga utgifter och blygsamma belopp. Vaults** är kassaskåp med flera signaturer (Multi-Key) som kräver flera nycklar för att godkänna en utgift och är utformade för långsiktig säker förvaring.



### Huvudsakliga egenskaper



Bitcoin Keeper stöder nästan alla hårdvaruplånböcker på marknaden: Coldcard, Trezor, Ledger, Keystone, BitBox02, Jade, Seedsigner, Passport och Coinkites Tapsigner. Integrationen sker via olika metoder beroende på enhet: QR-kodskanning, NFC-anslutning eller filimport.



Programmet erbjuder också avancerad UTXO-hantering med transaktionsmärkning, myntkontroll för att manuellt välja inmatningar vid sändning och stöd för PSBT-format för delvis signerade transaktioner.



## Installation och inledande konfiguration



Bitcoin Keeper är tillgängligt gratis på Android via Google Play Store och på iOS via App Store. Den listade utgivaren är BitHyve. Innan du installerar, se till att din enhet är fri från skadlig kod, uppdaterad och inte rotad eller jailbreakad.



När programmet startas första gången ombeds du att skapa en PIN-kod för säkerhet. Den här koden skyddar åtkomsten till din wallet och krypterar känsliga data lokalt. Välj en stark kod och memorera den. Du kan sedan aktivera biometrisk autentisering (fingeravtryck eller Face ID) för snabbare upplåsning.



![Installation et configuration du PIN](assets/fr/01.webp)



Applikationen presenterar sedan flera introduktionsskärmar som förklarar dess tre pelare: wallet-skapande för att skicka och ta emot bitcoins, nyckelhantering med hårdvarukompatibilitet för wallet och planering av arv för att föra bitcoins vidare. Tryck på "Kom igång" och välj sedan "Starta nytt" för att skapa en ny konfiguration.



![Écrans d'introduction](assets/fr/02.webp)



## Upptäcka gränssnittet



Bitcoin Keeper:s gränssnitt är uppbyggt kring fyra huvudflikar som nås från det nedre navigeringsfältet:



![Les quatre onglets de l'application](assets/fr/03.webp)



Fliken **Wallets** visar dina plånböcker och deras saldon. Det är här du kommer åt dina plånböcker för att skicka och ta emot bitcoins. Taggarna "Hot Wallet" och "Single-Key" eller "Multi-Key" gör att du snabbt kan identifiera typen av varje wallet.



Fliken **Keys** centraliserar hanteringen av dina signaturnycklar. Här hittar du Mobile Key som genereras av applikationen, samt alla nycklar som importeras från hårdvaruplånböcker. Det är också här du lägger till nya signaturenheter.



På fliken **Concierge** finns supporttjänster: skicka frågor till supportteamet och kontakta Bitcoin-rådgivare för personlig hjälp.



Fliken **More** (More Options) ger tillgång till inställningar som personlig serveranslutning, säkerhetskopiering av nycklar, arvsdokument, visningsinställningar och wallet-hantering.



## Anslutning till din egen server



För att förstärka din sekretess kan du med Bitcoin Keeper ansluta programmet till din egen Electrum-server i stället för att använda de offentliga standardservrarna.



![Configuration du serveur Electrum](assets/fr/04.webp)



Bläddra nedåt på fliken More (Mer) för att hitta serverinställningarna. Tryck på "Add Server" för att konfigurera en ny anslutning. Du kan välja mellan "Public Server" (förkonfigurerade publika servrar) och "Private Electrum" (din egen server).



För en privat server anger du webbadressen (t.ex. umbrel.local för en Umbrel-nod) och portnumret (vanligtvis 50001). Aktivera SSL om din server stöder det. Du kan också skanna en QR-kod för konfigurationen. När du har angett parametrarna trycker du på "Connect to Server".



Om du ännu inte har din egen Bitcoin-knut kan du ta en titt på vår handledning om Umbrel, ett enkelt och prisvärt sätt att spinna din egen knut:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Ta emot bitcoins



På fliken Plånböcker väljer du den wallet som du vill ta emot pengar från genom att trycka på den. wallet-skärmen visar saldot och tre åtgärdsknappar: Skicka Bitcoin, Ta emot Bitcoin och Visa alla mynt.



![Réception de bitcoins](assets/fr/05.webp)



Tryck på "Ta emot Bitcoin". Bitcoin Keeper genererar en ny mottagningsadress i Bech32-format (börjar med bc1...), tillsammans med dess QR-kod. Du kan lägga till en etikett på den här adressen för att identifiera källan till pengarna. Dela adressen med avsändaren genom att visa QR-koden eller kopiera textadressen.



Programmet genererar automatiskt en ny adress för varje mottagning, vilket bevarar din integritet. Använd "Get New Address" för att få en tom adress om det behövs.



## UTXO-hantering



Bitcoin Keeper erbjuder fullständig synlighet av UTXO (Outnyttjade transaktionsutgångar) som utgör ditt saldo. Från en wallet-skärm trycker du på "View All Coins" för att komma till hörnhanteraren.



![Gestion des UTXO](assets/fr/06.webp)



Skärmen "Manage Coins" listar varje UTXO individuellt med belopp och etikett. Med den här vyn kan du spåra ursprunget till dina mynt och organisera dem. Du kan välja specifika UTXO:er via "Select to Send" för att skicka med myntkontroll och på så sätt undvika att blanda mynt från olika ursprung.



## Skicka bitcoins



För att skicka, välj källportföljen och tryck på "Skicka Bitcoin". Ange destinationsadressen (inklistrad eller skannad via QR-kod) och lägg eventuellt till en etikett för att identifiera mottagaren.



![Envoi de bitcoins](assets/fr/07.webp)



På nästa skärm kan du ange det belopp som ska skickas. Gränssnittet visar ditt tillgängliga saldo och omvandlingen av fiatvalutan. Välj laddningsprioritet: Låg (ekonomi, ~60 minuter), Medium eller Hög (prioritet). Beräknade avgifter i sats/vbyte visas i realtid. Tryck på "Skicka" för att fortsätta.



![Confirmation et envoi](assets/fr/08.webp)



En sammanfattningsskärm visar alla detaljer: wallet källa, destinationsadress, transaktionsprioritet, nätverksavgifter, skickat belopp och totalbelopp. Kontrollera denna information noggrant eftersom Bitcoin-transaktioner inte kan återkallas. Tryck på "Confirm & Send" för att skicka transaktionen.



En bekräftelse med texten "Send Successful" visas med en fullständig sammanfattning. Transaktionen syns i historiken "Senaste transaktioner" med sin etikett.



## Spara dina nycklar



Att säkerhetskopiera din återställningsnyckel är ett kritiskt steg. Från fliken Mer, gå till avsnittet "Säkerhetskopiering och återställning" och klicka på "Återställningsnyckel".



![Sauvegarde de la Recovery Key](assets/fr/09.webp)



På skärmen visas status för dina säkerhetskopior. För att verifiera din säkerhetskopia ber programmet dig att bekräfta ett specifikt ord i din fras (t.ex. det 7:e ordet). Denna verifiering säkerställer att du har skrivit ner din återställningsfras korrekt.



Från "Recovery Key Settings" kan du se din fullständiga fras via "View Recovery Key" och se undertecknarens fingeravtryck för din nyckel. Förvara din 12-ordsfras på papper, på en säker plats, borta från fukt och eld. Förvara den aldrig på en ansluten enhet.



## Lägg till en extern nyckel (wallet-hårdvara)



En av Bitcoin Keeper:s största tillgångar är integrationen av hårdvaruplånböcker. Tryck på "Lägg till nyckel" på fliken Nycklar för att lägga till en ny signaturenhet.



![Ajout d'une clé hardware](assets/fr/10.webp)



Välj "Lägg till nyckel från en maskinvara" för att ansluta en maskinvara wallet. Programmet stöder ett brett utbud av enheter: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner och Specter Solutions.



### Tapsigner-konfiguration



Tapsigner är ett NFC-kort från Coinkite som är särskilt lämpat för mobil användning. Om du vill lära dig mer har vi en dedikerad handledning :



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

Om du vill lägga till Tapsigner väljer du den i listan över hårdvaruplånböcker.



![Configuration du Tapsigner](assets/fr/11.webp)



Ange först den 6-32-siffriga PIN-kod som finns tryckt på baksidan av ditt kort (standard på nya kort), eller din PIN-kod om den redan är konfigurerad. Tryck på "Fortsätt" och för sedan din Tapsigner nära baksidan av telefonen när "Redo att skanna" visas. NFC-kommunikationen importerar automatiskt den publika nyckeln. Du kan sedan lägga till en beskrivning (t.ex. "Métro Card") för att identifiera denna nyckel.



## Skapa en multisig-portfölj



När du har konfigurerat dina nycklar kan du skapa en wallet med flera signaturer som kombinerar flera enheter. Från fliken Plånböcker klickar du på "Lägg till Wallet".



![Création d'un nouveau wallet](assets/fr/12.webp)



Du har tre alternativ: "Skapa Wallet" för en ny portfölj, "Importera Wallet" för att återställa en befintlig wallet eller "Samarbeta Wallet" för ett delat valv. Välj "Skapa Wallet" och sedan "Bitcoin Wallet".



![Sélection du type de wallet](assets/fr/13.webp)



På nästa skärm finns olika konfigurationer: "Enkelknapp", "2 av 3 flerknappar" eller "3 av 5 flerknappar". För en anpassad multi-sig, tryck på "Select custom setup". Välj t.ex. "1 av 2": en enda signatur krävs från två möjliga tangenter.



Välj sedan de nycklar som ska ingå i ditt Vault. I vårt exempel kombinerar vi "Mobile Key" (mjukvarunyckel till telefonen) med "TAPSIGNER" (tunnelbanekort). Denna konfiguration ger redundans: om en av nycklarna blir otillgänglig kan du alltid spendera dina pengar med den andra.



![Finalisation du wallet multisig](assets/fr/14.webp)



Namnge din wallet (t.ex. "Test PlanB"), lägg till en valfri beskrivning och kontrollera de valda tangenterna. Tryck på "Skapa din Wallet". Ett bekräftelsemeddelande "Wallet Created Successfully" visas och påminner dig om att spara återställningsfilen för wallet.



Din nya multisig wallet visas nu i fliken Plånböcker med taggen "Multi-key" och indikationen "1 av 2".



### Spara konfigurationsfil



**Till skillnad från en enkel wallet, där återställningsfrasen räcker för att återställa åtkomsten, kräver en wallet multisig också konfigurationsfilen som beskriver kassaskåpets struktur (vilka nycklar som deltar, hur många signaturer som krävs). Utan den här filen, även med alla återställningsfraser, kommer du inte att kunna bygga om din wallet.



![Export du fichier de configuration](assets/fr/15.webp)



För att exportera den här filen väljer du din wallet multisig på fliken Wallets och trycker sedan på ikonen Settings (kugghjulet) i det övre högra hörnet. I "Wallet-inställningar" klickar du på "Wallet-konfigurationsfil". Flera exportalternativ finns tillgängliga:





- Export PDF**: genererar ett PDF-dokument som innehåller all wallet-information
- Show QR**: visar en QR-kod som kan skannas för att importera konfigurationen till en annan enhet
- Airdrop / File Export**: exporterar filen via telefonens delningsalternativ
- NFC**: dela via NFC med en kompatibel enhet



Förvara den här konfigurationsfilen separat från dina återställningsfraser, helst på ett krypterat eller utskrivet medium. Om du förlorar din telefon kan du med hjälp av den här filen och återställningsfraserna för varje deltagande nyckel bygga upp din wallet multisig igen med Bitcoin Keeper eller annan kompatibel programvara.



## Bästa praxis



### Fondorganisation



Strukturera dina bitcoins efter deras användning: en het wallet Single-Key för löpande utgifter med begränsade belopp, och ett eller flera Vaults Multi-Key för långsiktigt sparande. Systematisk UTXO-taggning hjälper dig att hålla reda på var dina pengar kommer ifrån, vilket är särskilt användbart för att hantera konfidentialitet och undvika att blanda mynt av olika ursprung.



Håll din telefon säker: aktivera det biometriska låset, utför systemuppdateringar regelbundet och var vaksam på installerade program. Och håll Bitcoin Keeper uppdaterad med säkerhetsuppdateringar.



### Säkerhetskopiering



Förvara minst två kopior av varje återvinningsfras på papper på geografiskt åtskilda platser. För stora summor kan man överväga graverad, katastrofsäker metall. Förvara aldrig dessa fraser på en enhet som är ansluten till Internet och fotografera dem aldrig.



För multi-sig-valv ska du även spara konfigurationsfilen (Wallet Recovery File), som innehåller de deltagande offentliga nycklarna och valvstrukturen. Denna fil, i kombination med nyckelåterställningsfraserna, gör att wallet kan byggas om på vilken kompatibel programvara som helst, t.ex. Sparrow eller Specter.



## Fördelar och begränsningar



### Höjdpunkter





- Bitcoin-applikationen minskar komplexitet och risk
- Integrerad integration av multisig Vaults med steg-för-steg-vägledning
- Utökat stöd för wallet-hårdvara (Tapsigner, Coldcard, Ledger, Jade, etc.)
- Avancerad hantering av UTXO och myntkontroll
- Kan anslutas till en personlig Electrum-server
- Öppen, granskningsbar källkod



### Begränsningar att ta hänsyn till





- Interface huvudsakligen på engelska
- Vissa premiumfunktioner (Cloud Backup, Assisted Server) kräver en uppgradering
- Multisig-konfigurationen kräver inledande utbildning



## Slutsats



Bitcoin Keeper sticker ut som en skalbar lösning för att hantera dina bitcoins. Dess progressiva tillvägagångssätt, från den enkla heta wallet till Vaults med flera signaturer, innebär att säkerheten kan uppgraderas när behoven förändras. Möjligheten att enkelt integrera hårdvaruplånböcker som Tapsigner banar väg för robusta konfigurationer utan överdriven komplexitet.



Inriktningen på enbart bitcoin, den öppna källkoden och respekten för integritet gör det till ett val i linje med kärnvärdena i Bitcoin:s ekosystem.



Denna handledning täcker de viktigaste funktionerna i Bitcoin Keeper i dess gratisversion. Applikationen erbjuder också premiumfunktioner (Cloud Backup, Assisted Server Backup, Canary Wallets) som kommer att bli föremål för en dedikerad handledning. I en kommande guide kommer vi också att utforska funktionen Arvsplanering, som gör att du kan förbereda överföringen av dina bitcoins till dina nära och kära, tack vare de förbättrade valven och tillhörande dokument som är integrerade i applikationen.



## Resurser





- Officiell hemsida: [bitcoinkeeper.app](https://bitcoinkeeper.app)
- Hjälpcenter: [help.bitcoinkeeper.app] (https://help.bitcoinkeeper.app)
- Källkod: [github.com/bithyve/bitcoin-keeper] (https://github.com/bithyve/bitcoin-keeper)
- Telegram : [t.me/BitcoinKeeper] (https://t.me/BitcoinKeeper)
- Twitter/X: [@bitcoinkeeper_](https://x.com/bitcoinkeeper_)