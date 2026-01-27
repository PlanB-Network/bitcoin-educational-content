---
name: Bitcoin Keeper - Arvsplan
description: Planera din bitcoinöverföring med Bitcoin Keeper
---

![cover](assets/cover.webp)



Överföringen av Bitcoin-tillgångar är en av de utmaningar som innehavarna underskattar mest. Till skillnad från ett bankkonto, där finansinstitutet kan överföra medlen till de rättmätiga arvingarna, är Bitcoin helt beroende av privata nycklar. En helt legitim laglig arvinge kommer aldrig att kunna komma åt pengarna utan dessa nycklar, medan en illvillig individ som har hemligheterna kommer att kunna spendera dem utan någon formalitet.



I denna andra Bitcoin Keeper-handledning utforskar vi de premiumfunktioner som är avsedda för fastighetsplanering. Programmet erbjuder avancerade verktyg för att skapa Enhanced Vaults, med tidsinställda skyddsmekanismer tack vare Miniscript, samt medföljande dokument för att vägleda dina nära och kära.



Den här guiden förutsätter att du redan har lärt dig grunderna i Bitcoin Keeper (portföljskapande, klassisk multisig, lägga till hårdvarunycklar) som förklaras i vår första handledning :



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

![video](https://youtu.be/tCld_-n2d30)



## Bitcoin Keeper abonnemangsplaner



Bitcoin Keeper fungerar enligt en freemium-modell med tre prenumerationsnivåer som erbjuder progressiv funktionalitet. För att komma åt planerna, gå till fliken **Mera** och tryck sedan på din nuvarande plan (standard är "Pleb") för att öppna skärmen **Hantera prenumeration**.



![Plans d'abonnement](assets/fr/01.webp)



**Pleb-planen** (gratis) ger tillgång till det viktigaste: obegränsat skapande av plånböcker med en nyckel och flera nycklar, kompatibilitet med alla större hårdvaruplånböcker (Coldcard, Trezor, Ledger, Jade, Tapsigner ...), myntkontroll, märkning och anslutning till en personlig Electrum-server. Denna plan är tillräcklig för standardanvändning och till och med för klassiska multi-sig-konfigurationer.



**Hodler-planen** (9,99 €/månad, med 1 månad gratis vid årlig betalning) innehåller alla Pleb-funktioner och lägger till krypterade säkerhetskopior till molnet (iCloud eller Google Drive) för att återställa dina kassaskåp på vilken enhet som helst, Server Key för att lägga till automatiska utgiftspolicyer och 2FA över en viss tröskel, och Canary Wallets för att upptäcka obehörig åtkomst till dina nycklar.



**Diamond Hands plan** (29,99 €/månad, med 1 månad gratis vid årsvis betalning) är det kompletta paketet för arvsplanering. Det inkluderar hela Hodler-planen och låser upp Inheritance Key (uppskjuten aktivering), Emergency Key (nödnyckel för återställning vid förlust), verktyg och dokument för arvsplanering och ett supportsamtal med Concierge-teamet för att validera din konfiguration. Det här är erbjudandet för bitcoiners som vill föra vidare sitt arv över flera generationer.



Viktigt: de valv du har skapat kommer att förbli tillgängliga även om du byter tillbaka till den kostnadsfria planen. Dina konfigurationer är baserade på öppna standarder (BSMS, Miniscript) och fungerar oberoende av din prenumeration.



## Arvshandlingar



När du har aktiverat din Diamond Hands-prenumeration öppnar du avsnittet ** Arvsdokument** från fliken Mer. Bitcoin Keeper tillhandahåller fem exempeldokument för att strukturera din fastighetsplan, samt ett tipsavsnitt:



![Documents d'héritage](assets/fr/02.webp)





- Seed Words Template**: en mall för att skriva ner dina återhämtningsfraser på ett organiserat sätt
- Betrodda kontakter**: en mall för att lista kontaktuppgifter till betrodda personer som är involverade i din plan (notarie, advokat, arvingar, nyckelförvaltare)
- Additional Share Key**: ett dokument som innehåller teknisk information för varje nyckel: PIN-kod, härledningsväg, fysisk plats, enhetstyp och all annan information som är användbar för att identifiera och använda nyckeln
- Återvinningsinstruktioner**: steg-för-steg-instruktioner för arvtagaren eller förmånstagaren för att återvinna medel
- Brev till advokat**: ett förifyllt brev som kan anpassas till din advokat eller notarie



I avsnittet **Arvstips** finns praktiska råd om hur du säkrar nycklar för arvingar och optimerar din arvsplan.



Anpassa dessa dokument så att de passar din situation och förvara dem på en säker plats, åtskilda från själva nycklarna.



## Konfigurera molnbaserad säkerhetskopiering



Innan du skapar ditt äldre valv ska du aktivera molnbackup för att skydda dina konfigurationsfiler. På fliken More (Mer) trycker du på **Personal Cloud Backup**.



![Configuration Cloud Backup](assets/fr/03.webp)



Välj ett starkt lösenord för att kryptera dina säkerhetskopior. Detta lösenord skyddar endast konfigurationsfilerna för wallet (inte dina privata nycklar). Bekräfta lösenordet och tryck på **Confirm**. Dina säkerhetskopior kommer att lagras på iCloud eller Google Drive beroende på din enhet. Tryck på **Backup Now** för att starta din första säkerhetskopia.



## Importera dina hårdvarunycklar



I vårt exempel skapar vi ett 2-av-3 kassaskåp med ytterligare två nycklar (Inheritance och Emergency). Låt oss börja med att importera alla nödvändiga nycklar till fliken **Keys**.



![Import des clés hardware](assets/fr/04.webp)



Tryck på **Add key** och välj sedan **Add key from a hardware** för att ansluta en hårdvara wallet. Bitcoin Keeper stöder många enheter: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner och Specter Solutions.



I vår konfiguration importerar vi :




- 2 **Kortnycklar** (MK4SP och MK4)
- 2 nycklar **Tapsigner** (Metro och Genesis)



Om du vill lägga till ett Coldcard väljer du det i listan och följer instruktionerna på skärmen för att exportera den publika nyckeln via QR-kod, fil, USB eller NFC. Mer information om hur du använder ett Coldcard eller Tapsigner finns i våra särskilda handledningar:



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/tutorials/wallet/hardware/coldcard-mk4-5d44dd94-423d-4e37-9a8c-3fc38b45ce59


När alla nycklar har importerats hittar du dem under fliken Keys med deras egna namn.



## Skapa ett arv wallet



Låt oss gå vidare till skapandet av en trunk. Från fliken **Wallets** trycker du på **Add Wallet**, väljer **Bitcoin Wallet** och sedan **Create Wallet**.



![Création du wallet](assets/fr/05.webp)



Välj typ av wallet. För vår äldre plan, välj **2 av 3 multi-key**. Längst ner på skärmen aktiverar du **Avancerade säkerhetsalternativ** och trycker sedan på **Fortsätt**.



![Options de sécurité avancées](assets/fr/06.webp)



I popup-fönstret Enhanced Security Options markerar du :




- Inheritance Key**: en ytterligare nyckel som läggs till i quorum efter en viss tidsperiod
- Emergency Key**: en nyckel med uppskjuten total kontroll för att återfå medel i händelse av nyckelförlust



Tryck på **Spara ändringar**. Välj sedan de 3 tangenter som ska utgöra din wallet från de importerade (t.ex. Seed Key, Coldcard MK4SP och Tapsigner Metro).



## Fastställande av särskilda deadlines



På nästa skärm kan du konfigurera Emergency Key och Inheritance Key. Det är här du definierar de fördröjningar som styr aktiveringen av dessa specialnycklar.



![Configuration des délais](assets/fr/07.webp)



För **Emergency Key** väljer du den hårdvarunyckel som ska fungera som den ultimata säkerhetskopian (här Coldcard MK4) och väljer aktiveringsfördröjningen (i vårt exempel: 2 år). Till skillnad från Inheritance Key bidrar Emergency Key inte till quorum: den gör att du kan **bypassa multisig** helt och hållet och ger dig total kontroll över pengarna efter att tidsgränsen har löpt ut. Det är din sista utväg: om flera nycklar försvinner eller förstörs kan du med denna enda nyckel återställa allt. Den måste därför skyddas med största noggrannhet.



För **Inheritance Key** väljer du den nyckel som är avsedd för arvtagaren (här Coldcard MK4SP) och väljer fördröjningen (i vårt exempel: 1 år). Efter ett år utan rörelse kommer den här nyckeln **att läggas till i signaturkvorumet**. I praktiken kommer din wallet 2-of-3 att bli en wallet 2-of-4 när denna period har löpt ut, vilket gör det möjligt för arvtagaren att delta i signeringen tillsammans med befintliga nycklar.



### Hur fungerar tidslås?



Bitcoin Keeper använder **absoluta tidslås** (CLTV - CheckLockTimeVerify), vilket möjliggörs av Miniscript. Till skillnad från relativa tidslås (CSV), som startar när varje UTXO tas emot, arbetar absoluta tidslås med ett **fastställt utgångsdatum** som definieras när wallet skapas.



Om du skapar en wallet i dag med en 1-årig arvsnyckel kommer aktiveringsdatumet att vara "i dag + 1 år". Alla medel som deponeras i denna wallet, oavsett deponeringsdatum, kommer att vara tillgängliga via arvsnyckeln på samma datum.



Fördelen med absoluta tidslås är att de tillåter ledtider på över 15 månader (gränsen för relativa CSV-tidslås), vilket förklarar varför Bitcoin Keeper kan erbjuda alternativ som 2 år.



### Mekanismen för uppdatering



För att förhindra aktivering av specialnycklar under din livstid måste du regelbundet "uppdatera" din wallet. Med absoluta tidslås innebär detta att **skapa wallet med ett nytt utgångsdatum** som skjuts in i framtiden, och sedan överföra dina pengar till denna nya wallet.



Bitcoin Keeper förenklar denna process med en integrerad uppdateringsfunktion. Applikationen hanterar automatiskt komplexiteten i bakgrunden: du följer helt enkelt de guidade stegen, utan att manuellt behöva skapa en ny wallet eller överföra pengarna själv. Planera denna operation regelbundet, i god tid före utgången av den kortaste tidsram som konfigurerats. Till exempel, med en 1-årig arvsnyckel, uppdatera var 9-10 månader för att upprätthålla en säkerhetsmarginal.



## Spara och exportera konfiguration



När wallet har skapats påminner programmet dig om att spara konfigurationsfilen. **Detta steg är avgörande**: utan denna fil kommer dina arvingar inte att kunna återskapa wallet multisig.



![Export de la configuration](assets/fr/08.webp)



Tryck på **Backup Wallet Recovery File**. Flera exportalternativ finns tillgängliga:




- PDF-export**: genererar ett komplett dokument med all wallet-information
- Show QR**: visar en QR-kod för att importera konfigurationen på en annan enhet
- Airdrop / File Export**: exporterar filen via delningsalternativen
- NFC**: dela via NFC med en kompatibel enhet



Multiplicera kopiorna: en hos din notarie, en i ett bankfack, en krypterad digital version. Din nya wallet visas nu i fliken Plånböcker med taggarna "Multi-key", "2 av 3", "Inheritance key" och "Emergency key".



## Skapa en Wallet-kanariefågel



Canary Wallet är ett system för tidig varning. Idén: varje nyckel som används i en wallet multi-nyckel kan också användas i en separat wallet single-key. Genom att deponera en liten summa på denna wallet "kanariefågel" signalerar varje obehörig rörelse att nyckeln har äventyrats.



![Canary Wallets](assets/fr/09.webp)



Det finns två sätt att konfigurera en Wallet Canary. Från fliken **More** trycker du på **Canary Wallets** i avsnittet "Keys and Wallets". På skärmen förklaras principen: om någon kommer åt en av dina nycklar och hittar pengar i den tillhörande wallet-nyckeln, kommer de att försöka ta bort dem, vilket kommer att varna dig.



![Configuration Canary depuis une clé](assets/fr/10.webp)



Du kan också konfigurera Canary direkt från en nyckel. På fliken **Keys** väljer du en nyckel (t.ex. Tapsigner Genesis), trycker på ikonen **Settings** (kugghjul) och sedan på **Canary Wallet**. Den tillhörande wallet-kanariefågeln öppnas, redo att ta emot några övervakningssatoshis.



Sätt in en liten summa (några tusen satoshis) på varje Canary Wallet. Om dessa medel flyttas utan ditt samtycke, ta omedelbart bort den komprometterade nyckeln från dina multisig-kassaskåp.



## Bästa praxis



**Testa din konfiguration** med en liten summa pengar innan du sätter in en stor summa i den. Skicka några tusen satoshis till valvet och prova sedan en utgående utgift för att kontrollera att du behärskar signeringsprocessen med varje enhet. Testa också att importera konfigurationsfilen på en annan telefon för att se till att säkerhetskopian fungerar.



**Distribuera nycklar på ett intelligent sätt**. För Tapsigners, lämna över dem i ett förseglat kuvert med PIN-koden kommunicerad separat (t.ex. i Recovery Instructions-brevet som lagras någon annanstans). För klassiska hårdvaruplånböcker, förvara enheten hos en betrodd tredje part och seed på papper eller metall hos dig eller en annan tredje part. Notera fingeravtrycket för varje nyckel och dess namn i konfigurationsfilen för att undvika förvirring.



**Planera regelbundna tester** (brandövningar). Kontrollera varje år att du kan bygga upp kassaskåpet igen från säkerhetskopior på en tom telefon. Testa Canary-varningar genom att kontrollera saldon. Simulera förlustscenarier ("tänk om jag tappar bort Coldcard?") för att bekräfta att de återstående nyckelkombinationerna är tillräckliga.



**Glöm inte uppdateringen**. Om du har ställt in din Inheritance Key på 1 år ska du uppdatera dig var 9-10 månad. Detta är det pris du betalar för automatisk överföring utan ingripande från tredje part.



**Håll planen uppdaterad**. Alla ändringar (ersättning av en nyckel, ändring av arvingar, ändring av tidsfrist) måste återspeglas i alla säkerhetskopior och dokument. Regenerera PDF-filer efter varje ändring och distribuera nya versioner.



## Gränser och överväganden



Trots att dessa verktyg är kraftfulla är det viktigt att känna till deras begränsningar för att kunna hantera dem så effektivt som möjligt.



**Komplexiteten** hos ett multisig-safe med tidslås kan vara en risk i sig: felkonfiguration, missförstånd från arvingar, förlust av ett kritiskt element bland de många komponenterna. Bitcoin Keeper förenklar upplevelsen så mycket som möjligt, men det är fortfarande en teknisk operation. Använd endast denna plan om det belopp som ska skyddas motiverar det. För små belopp kan det räcka med en enklare plan.



**Applikationsberoendet** är värt att tänka på. Även om koden är öppen källkod och baserad på öppna standarder (Miniscript, BSMS), är vissa funktioner beroende av Keeper-ekosystemet. Förvara en kopia av applikationen (Android APK eller iOS IPA) och dokumentera i dina brev till arvingar möjligheten att använda andra Miniscript-kompatibla plånböcker (t.ex. Liana) för att återvinna medel.



Betrodda mäklare** innebär en mänsklig risk. Vad händer om en illasinnad släkting använder den nyckel som anförtrotts honom/henne innan tidsfristen löper ut? Eller om advokaten tappar bort dina dokument? Välj dessa personer med omsorg, förklara deras ansvarsområden tydligt och ha en plan B. Canary Wallets, redundanta säkerhetskopior och själva strukturen i multisig är fortfarande ditt bästa skydd mot dessa faror.



## Slutsats



Bitcoin Keeper, med sin Diamond Hands plan, erbjuder en komplett verktygslåda för fastighetsplanering: Förbättrade valv med tidsinställda nycklar, medföljande dokument, Canary Wallets och personligt stöd.



Det är mer än bara en teknisk fråga: det handlar om att utforma arkitekturen för din egendom, fördela nycklar och kunskap på ett intelligent sätt och regelbundet testa systemet. En väl utformad Bitcoin-arvsplan förvandlar dina satoshis till ett verkligt, överförbart arv.