---
name: RoninDojo

description: Installera och använda din RoninDojo Bitcoin-nod.
---
***VARNING:** Efter gripandet av grundarna av Samourai Wallet och beslagtagandet av deras servrar den 24 april är vissa funktioner i RoninDojo, såsom Whirlpool, inte längre i drift. Det är dock möjligt att dessa verktyg kan återinföras eller återlanseras på olika sätt under de kommande veckorna. Eftersom RoninDojo-koden fanns på Samourais GitLab, som också beslagtogs, är det för närvarande inte möjligt att ladda ner koden på distans. RoninDojo-teamen arbetar sannolikt med att publicera koden på nytt.*


_Vi följer noga utvecklingen av detta fall och utvecklingen av de tillhörande verktygen. Du kan vara säker på att vi kommer att uppdatera denna handledning när ny information blir tillgänglig._


_Den här handledningen tillhandahålls endast i utbildnings- och informationssyfte. Vi varken stödjer eller uppmuntrar användning av dessa verktyg i kriminella syften. Det är varje användares ansvar att följa de lagar som gäller i deras jurisdiktion._


_Den här handledningen är avsedd för installation av RoninDojo v1. För att dra nytta av de senaste förbättringarna och funktionerna rekommenderar jag starkt att du läser vår handledning som är avsedd för direkt installation av RoninDojo v2 på din Raspberry Pi:_

https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

---

Att driva och använda sin egen nod är viktigt för att verkligen kunna delta i Bitcoin-nätverket. Att driva en Bitcoin-nod ger inga ekonomiska fördelar för användaren, men det gör det möjligt för dem att bevara sin integritet, agera självständigt och ha kontroll över sitt förtroende för nätverket.


I den här artikeln kommer vi att ta en detaljerad titt på RoninDojo, en bra lösning för att köra din egen Bitcoin-nod.


### Innehållsförteckning:



- Vad är RoninDojo?
- Vilken hårdvara ska man välja?
- Hur installerar jag RoninDojo?
- Hur använder man RoninDojo?
- Slutsats


Om du inte är bekant med hur en Bitcoin-nod fungerar och dess roll rekommenderar jag att du börjar med att läsa den här artikeln: Bitcoin-noden - Del 1/2: Tekniska begrepp.


![Samourai](assets/1.webp)


## Vad är RoninDojo?


Dojo är en fullständig Bitcoin-nodserver som utvecklats av Samourai Wallet-teamet. Du kan fritt installera den på vilken maskin som helst.


RoninDojo är en installationsassistent och ett administrationsverktyg för Dojo och olika andra verktyg. RoninDojo tar den ursprungliga implementeringen av Dojo och lägger till många andra verktyg till den, samtidigt som installationen och hanteringen blir enklare.


De erbjuder också en "plug-and-play"-hårdvara, RoninDojo Tanto, med RoninDojo förinstallerad på en maskin som monterats av deras team. Tanto är en betald lösning, lämplig för dem som inte vill smutsa ner sina händer.


Koden för RoninDojo är öppen källkod, så det är också möjligt att installera den här lösningen på din egen hårdvara. Det här alternativet är kostnadseffektivt men kräver lite mer manipulation, vilket är vad vi kommer att göra i den här artikeln.


RoninDojo är en Dojo, så det möjliggör enkel integrering av Whirlpool CLI i din Bitcoin-nod för att få bästa möjliga CoinJoin-upplevelse. Med Whirlpool CLI kan du inte bara låta dina bitcoins remixa 24/7 utan att behöva hålla din persondator påslagen, utan du kan också förbättra din integritet avsevärt.


RoninDojo integrerar många andra verktyg som är beroende av din Dojo, till exempel Boltzmann-kalkylatorn, som bestämmer sekretessnivån för en transaktion, Electrum-servern för att ansluta dina olika Bitcoin-plånböcker till din nod, eller Mempool-servern för att privat observera dina transaktioner.

Jämfört med en annan nodlösning som Umbrel, som jag presenterade för dig i den här artikeln, är RoninDojo djupt fokuserad på "on chain" -lösningar och verktyg som optimerar användarnas integritet. Därför tillåter RoninDojo inte interaktion med Lightning Network.

RoninDojo erbjuder färre verktyg jämfört med Umbrel, men de få viktiga funktionerna för en Bitcoiner som finns på Ronin är otroligt stabila.


Så om du inte behöver alla funktioner i en Umbrel-server och bara vill ha en enkel och stabil nod med några viktiga verktyg som Whirlpool eller Mempool, så är RoninDojo förmodligen en bra lösning för dig.


Enligt min mening är Umbrels utvecklingsfokus starkt på Lightning Network och mångsidiga verktyg. Det är fortfarande en Bitcoin-nod, men målet är att göra den till en multitasking-miniserver. Däremot är RoninDojos utvecklingsfokus mer anpassat till teamen på Samourai Wallet och fokuserar på de viktigaste verktygen för en Bitcoiner, vilket möjliggör full självständighet och optimerad hantering av integritet på Bitcoin.


Observera att det är något mer komplicerat att konfigurera en RoninDojo-nod än en Umbrel-nod.


Nu när vi har kunnat måla upp en bild av RoninDojo, låt oss se hur man sätter upp den här noden tillsammans.


## Vilken hårdvara ska man välja?


För att välja den maskin som är värd för och kör RoninDojo har du flera alternativ.


Som förklarats tidigare är det enklaste valet att beställa Tanto, en plug-and-play-maskin som utformats speciellt för detta ändamål. För att beställa din, gå hit: [länk](https://shop.ronindojo.io/product-category/nodes/).


Eftersom RoninDojo-teamen producerar kod med öppen källkod är det också möjligt att implementera RoninDojo på andra maskiner. Du kan hitta de senaste versionerna av installationsguiden på den här sidan: [länk](https://ronindojo.io/en/downloads.html), och de senaste versionerna av koden på den här sidan: [länk](https://code.samourai.io/ronindojo/RoninDojo).


Personligen installerade jag det på en Raspberry Pi 4 8GB och allt fungerar perfekt.


Observera dock att RoninDojo-teamen anger att det ofta finns problem med fodralet och SSD-adaptern. Det är därför inte rekommenderat att använda ett fodral med en kabel för maskinens SSD. Istället är det att föredra att använda ett lagringsexpansionskort som är särskilt utformat för ditt moderkort, till exempel detta: Raspberry Pi 4 Storage Expansion Card.


Här är ett exempel på hur du sätter upp din egen RoninDojo-nod:



- En Raspberry Pi 4.
- Ett fall med en fläkt.
- Ett kompatibelt kort för lagringsexpansion.
- En strömkabel.
- Ett industriellt micro SD-kort på 16 GB eller mer.
- En SSD på 1 TB eller större.
- En RJ45 Ethernet-kabel, kategori 8 rekommenderas.


## Hur installerar jag RoninDojo?


### Steg 1: Förbered det startbara micro SD-kortet.


När du har satt ihop din maskin kan du börja installera RoninDojo. För att göra detta, börja med att skapa ett startbart micro SD-kort genom att bränna den lämpliga diskavbildningen på det.


Sätt i ditt micro SD-kort i din dator och gå sedan till den officiella RoninDojo-webbplatsen för att ladda ner RoninOS-diskavbildningen: https://ronindojo.io/en/downloads.html.


Ladda ner den diskavbildning som motsvarar din maskinvara. I mitt fall laddade jag ner avbildningen "MANJARO-ARM-RONINOS-RPI4-22.03.IMG.XZ":


![Download RoninOS disk image](assets/2.webp)


När bilden har laddats ner kan du verifiera dess integritet med hjälp av motsvarande .SHA256-fil. Jag kommer att beskriva i detalj hur man gör detta i den här artikeln: Hur verifierar jag integriteten hos Bitcoin-programvaran på Windows?


Specifika instruktioner för att verifiera integriteten hos RoninOS finns också på denna sida: https://wiki.ronindojo.io/en/extras/verify.


För att bränna denna bild på ditt micro SD-kort kan du använda programvara som Balena Etcher, som du kan ladda ner här: https://www.balena.io/etcher/.


För att göra detta väljer du bilden i Etcher och flashar den till micro SD-kortet:


![Burn disk image with Etcher](assets/3.webp)


När operationen är klar kan du sätta in det startbara micro SD-kortet i Raspberry Pi och slå på maskinen.


### Steg 2: Konfigurera RoninOS.


RoninOS är operativsystemet för din RoninDojo-nod. Det är en modifierad version av Manjaro, en Linux-distribution. När du har startat din maskin och väntat några minuter kan du börja konfigurera den.


För att fjärransluta till den måste du hitta IP Address för din RoninDojo-maskin. För att göra detta kan du till exempel ansluta till administrationspanelen i din internetbox, eller så kan du också ladda ner programvara som https://angryip.org/ för att skanna ditt lokala nätverk och hitta maskinens IP.


När du har hittat IP-adressen kan du ta kontroll över din maskin från en annan dator som är ansluten till samma lokala nätverk med hjälp av SSH.


Från en dator som kör macOS eller Linux öppnar du helt enkelt terminalen. Från en dator som kör Windows kan du använda ett specialiserat verktyg som Putty eller direkt använda Windows PowerShell.


När terminalen är öppen skriver du följande kommando:

```
ssh root@192.168.?.?
```


Ersätt bara de två frågetecknen med IP-adressen till din tidigare hittade RoninDojo.

Tips: I ett Shell högerklickar du för att klistra in ett objekt.


Därefter kommer du till Manjaros kontrollpanel. Välj rätt tangentbordslayout med hjälp av pilarna för att ändra målet i rullgardinsmenyn.


![Manjaro Keyboard Configuration](assets/4.webp)


Välj ett användarnamn och lösenord för din session. Använd ett starkt lösenord och gör en säker säkerhetskopia. Du kan eventuellt använda ett svagt lösenord under installationen och senare enkelt ändra det genom att "kopiera och klistra in" det i RoninUI. Detta gör att du kan använda ett mycket starkt lösenord utan att spendera för mycket tid på att skriva det manuellt under installationen av Manjaro.


![Manjaro Username Configuration](assets/5.webp)


Därefter kommer du också att bli ombedd att välja ett rotlösenord. För rotlösenordet anger du ett starkt lösenord direkt. Du kommer inte att kunna ändra det från RoninUI. Kom också ihåg att säkerhetskopiera detta rotlösenord på ett säkert sätt.


Ange sedan din plats och tidszon.


![Manjaro Time Zone Configuration](assets/6.webp)


![Manjaro Location Configuration](assets/7.webp)


Välj sedan ett värdnamn.


![Manjaro Hostname Configuration](assets/8.webp)


Kontrollera slutligen konfigurationsinformationen för Manjaro och bekräfta.


![Verification of ManjaroOS Configuration Information](assets/9.webp)


### Steg 3: Ladda ner RoninDojo.


Den första konfigurationen av RoninOS kommer att göras. När det är klart, som visas i skärmdumpen ovan, kommer maskinen att starta om. Vänta några ögonblick och ange sedan följande kommando för att återansluta till din RoninDojo-maskin:

```
ssh username@192.168.?.?
```


Ersätt bara "username" med det användarnamn du tidigare valt och ersätt frågetecknen med IP:n för din RoninDojo.


Ange sedan ditt användarlösenord.


I terminalen kommer det att se ut så här:


![SSH Connection to RoninOS](assets/10.webp)


Du är nu ansluten till din maskin, som för närvarande bara har RoninOS. Nu måste du installera RoninDojo på den.


Ladda ner den senaste versionen av RoninDojo genom att ange följande kommando:

```
git clone https://code.samourai.io/ronindojo/RoninDojo
```


Nedladdningen kommer att gå snabbt. I terminalen kommer du att se detta:


![Cloning RoninDojo](assets/11.webp)


Vänta tills nedladdningen är klar och installera sedan och få åtkomst till RoninDojo-användaren Interface med följande kommando:

```
~/RoninDojo/ronin
```


Du kommer att bli ombedd att ange ditt användarlösenord:


![Bitcoin Node Password Verification](assets/12.webp)


Det här kommandot är bara nödvändigt första gången du öppnar din RoninDojo. Efteråt, för att komma åt RoninCLI via SSH, behöver du bara ange kommandot [SSH username@192.168.?.?] och ersätta "användarnamn" med ditt användarnamn och ange IP Address för din nod. Du kommer att bli ombedd att ange ditt användarlösenord.


Därefter kommer du att se denna magnifika animation:


![RoninCLI launch animation](assets/13.webp)


Sedan kommer du slutligen fram till RoninDojo CLI-användaren Interface.


### Steg 4: Installera RoninDojo.


Navigera till menyn "System" i huvudmenyn med hjälp av piltangenterna på tangentbordet. Tryck på Enter-knappen för att bekräfta ditt val.


![RoninCLI navigation menu to System](assets/14.webp)


Gå sedan till menyn "System Setup & Install".


![RoninCLI navigation menu to RoninDojo system installation](assets/15.webp)


Slutligen markerar du "System Setup" och "Install RoninDojo" med mellanslagstangenten och väljer sedan "Accept" för att starta installationen.


![RoninDojo installation confirmation](assets/16.webp)


Låt installationen fortskrida i lugn och ro. I mitt fall tog det cirka 2 timmar. Håll din terminal öppen under processen.


Kontrollera ibland din terminal, eftersom du kommer att bli ombedd att trycka på en knapp i vissa skeden av installationen, som till exempel här:


![RoninDojo installation in progress](assets/17.webp)


I slutet av installationen kommer du att se de olika behållarna starta:


![Node container startup](assets/18.webp)


Då kommer din nod att starta om. Anslut igen till RoninCLI för nästa steg.


![Bitcoin node restart](assets/19.webp)


### Steg 5: Ladda ner Proof-of-Work-kedjan och få tillgång till RoninUI.


När installationen är klar kommer din nod att börja ladda ner Bitcoin Proof-of-Work-kedjan. Detta kallas för Initial Block Download (IBD). Det tar vanligtvis mellan 2 och 14 dagar beroende på din internetanslutning och enhet.


Du kan följa hur nedladdningen av kedjan fortskrider genom att gå till RoninUI-webben Interface.


Om du vill komma åt den från ett lokalt nätverk skriver du följande i webbläsarens Address-fält:



- Ange antingen direkt IP Address för din maskin (192.168...?.?)
- Eller ange: ronindojo.local


Kom ihåg att inaktivera ditt VPN om du använder ett sådant.


### Möjlig vridning


Om du inte kan ansluta till RoninUI från din webbläsare kan du kontrollera att programmet fungerar korrekt från din terminal som är ansluten till din nod via SSH. Anslut till huvudmenyn genom att följa föregående steg:



- Typ: SSH username@192.168.?.? ersätter med dina autentiseringsuppgifter.



- Ange ditt användarlösenord.


När du är på huvudmenyn, gå till: **RoninUI > Omstart**


Om programmet startar om korrekt är det ett problem med anslutningen från din webbläsare. Kontrollera att du inte använder VPN och se till att du är ansluten till samma nätverk som din nod.


Om omstarten ger ett fel kan du prova att uppdatera operativsystemet och sedan installera om RoninUI. Så här uppdaterar du operativsystemet: **System > Programuppdateringar > Uppdatera operativsystemet**


När uppdateringen och omstarten är klar, återanslut till din nod via SSH och installera om RoninUI: **RoninUI > Installera om**


När du har laddat ner RoninUI igen kan du försöka ansluta till RoninUI via din webbläsare.


**Tips:** Om du av misstag lämnar RoninCLI och befinner dig i Manjaro-terminalen, ange bara kommandot "ronin" för att återgå direkt till huvudmenyn i RoninCLI.


### Webbinloggning


Du kan också logga in på RoninUI-webben Interface från vilket nätverk som helst med hjälp av Tor. För att göra detta hämtar du Tor Address för din RoninUI från RoninCLI: **Credentials > Ronin UI**


Hämta Tor Address som slutar på .onion och logga sedan in på Ronin UI genom att ange denna Address i din Tor-webbläsare. Var försiktig så att du inte läcker dina olika inloggningsuppgifter, eftersom de är känslig information.


![RoninUI web login interface](assets/20.webp)


När du har loggat in kommer du att bli ombedd att ange ditt användarlösenord. Det är samma lösenord som du använder för att logga in via SSH.


![RoninUI web interface management panel](assets/21.webp)


Vi kan se hur IBD (Initial Block Download) fortskrider här. Ha tålamod, du hämtar alla transaktioner som gjorts på Bitcoin sedan den 3 januari 2009.


Efter att ha laddat ner hela Blockchain komprimerar indexeraren databasen. Denna operation tar cirka 12 timmar. Du kan också följa dess framsteg under "Indexer" på RoninUI.


Din RoninDojo-nod kommer att vara fullt fungerande efter detta:


![Indexer synchronized at 100% functional node](assets/22.webp)


Om du vill ändra användarlösenordet till ett starkare kan du göra det nu från fliken "Inställningar". På RoninDojo finns det ingen ytterligare säkerhet Layer, så jag rekommenderar att du väljer ett riktigt starkt lösenord och tar hand om säkerhetskopian av det.


## Hur använder man RoninDojo?


När kedjan har laddats ner och komprimerats kan du börja använda de tjänster som erbjuds av din nya RoninDojo-nod. Låt oss se hur du använder dem.


### Anslutning av Wallet-programvara till elektriska apparater.


Det första verktyget för din nyligen installerade och synkroniserade nod kommer att vara att sända dina transaktioner till Bitcoin-nätverket. Därför kommer du sannolikt att vilja ansluta din olika Wallet-hanteringsprogramvara till den.


Du kan göra detta med hjälp av Electrum Rust Server (electrs). Programmet är normalt förinstallerat på din RoninDojo-nod. Om inte, kan du installera det manuellt från RoninCLI Interface.


Gå helt enkelt till: **Applikationer > Hantera applikationer > Installera Electrum Server**


För att hämta Tor Address för din Electrum-server, gå till från RoninCLI-menyn:

**Credentials > Electrs**


Du behöver bara ange .onion-länken i din Wallet-programvara. Till exempel, i Sparrow Wallet, gå till fliken:

**Fil > Inställningar > Server**


I servertypen väljer du `Private Electrum` och anger sedan Tor Address för din Electrum-server i motsvarande fält. Slutligen klickar du på "Test Connection" för att testa och spara din anslutning.


![Sparrow Wallet connection interface to an electrs](assets/23.webp)


### Anslutning av Wallet-programvara till Samourai Dojo.


Istället för att använda Electrs kan du också använda Samourai Dojo för att ansluta din kompatibla Software Wallet till din RoninDojo-nod. Till exempel erbjuder Samourai Wallet detta alternativ.


För att göra detta skannar du bara QR-koden för anslutningen till din Dojo. För att komma åt den från RoninUI, klicka på fliken "Dashboard" och sedan på knappen "Manage" i rutan för din Dojo. Du kommer då att kunna se QR-koderna för anslutningen mellan din Dojo och BTC-RPC Explorer. För att visa dem klickar du på "Display values".


![Retrieving the connection QR code to Dojo](assets/24.webp)


För att ansluta din Samourai Wallet till din Dojo måste du skanna den här QR-koden under installationen av programmet:


![Connecting to Dojo from the Samourai Wallet application](assets/25.webp)


### Använda din egen Mempool Explorer.


Utforskaren är ett viktigt verktyg för Bitcoinanvändare och gör det möjligt att kontrollera olika uppgifter om Bitcoin-kedjan. Med Mempool kan du t.ex. i realtid kontrollera de avgifter som andra användare tar ut för att kunna justera dina egna i enlighet med detta. Du kan också kontrollera bekräftelsestatus för en av dina transaktioner eller se saldot för en Address.


Dessa utforskande verktyg kan utsätta dig för integritetsrisker och kräver att du litar på en tredje parts databas. När du använder detta onlineverktyg utan att gå igenom din egen nod:



- Du riskerar att läcka information om din Wallet.



- Du litar på webbplatsansvarig för Proof-of-Work-kedjan som de är värd för.


För att undvika dessa risker kan du använda din egen Mempool-instans på din nod via Tor-nätverket. Med den här lösningen bevarar du inte bara din integritet när du använder tjänsten, utan du behöver inte heller längre lita på en leverantör eftersom du frågar din egen databas.


För att göra detta börjar du med att installera Mempool Space Visualizer från RoninCLI:


**Applikationer > Hantera applikationer > Installera Mempool Space Visualizer**


När du har installerat den hämtar du länken till din Mempool. Tor Address gör att du kan komma åt den från vilket nätverk som helst. På samma sätt hämtar vi den här länken via RoninCLI:


**Behörighet > Mempool**


![Retrieve Tor Mempool address](assets/26.webp)


Ange helt enkelt din Mempool Tor Address i Tor-webbläsaren för att njuta av din egen Mempool-instans, baserat på dina egna data. Jag rekommenderar att du lägger till denna Tor Address i dina favoriter för snabbare åtkomst. Du kan också skapa en genväg på skrivbordet.


![Mempool Space interface](assets/27.webp)


Om du inte har Tor-webbläsaren ännu kan du ladda ner den här: https://www.torproject.org/download/


Du kan också komma åt den från din smartphone genom att installera Tor Browser och ange samma Address. Var du än befinner dig kan du se tillståndet i Bitcoin-kedjan med hjälp av din egen nod.


### Använda Whirlpool CLI.


Din RoninDojo-nod innehåller också WhirlpoolCLI, en fjärrkommandorad Interface för automatisering av Whirlpool-mixar.


När du utför en CoinJoin med Whirlpool-implementeringen måste applikationen du använder förbli öppen för att kunna utföra mixar och remixar. Denna process kan vara tråkig för användare som vill ha höga anon-uppsättningar, eftersom enheten som är värd för applikationen med Whirlpool ständigt måste vara på. I praktiken innebär detta att om du vill engagera dina UTXO:er i remixer 24/7 måste du hålla din dator eller telefon ständigt påslagen med applikationen öppen.


En lösning på denna begränsning är att använda WhirlpoolCLI på en maskin som är avsedd att vara ständigt på, till exempel en Bitcoin-nod. Med detta kan våra UTXO:er omblandas 24/7 utan att behöva hålla någon annan maskin än vår Bitcoin-nod igång.

WhirlpoolCLI används med WhirlpoolGUI, ett grafiskt Interface som ska installeras på en persondator för enkel hantering av Coinjoins. Jag kommer att förklara i detalj hur man ställer in Whirlpool CLI med din egen dojo i den här artikeln: [länk](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=dans%20cette%20partie.-,Tutoriel%20%3A%20Whirpool%20CLI%20sur%20Dojo%20et%20Whirlpool%20GUI.,-Si%20vous%20souhaitez).


För att lära dig mer om CoinJoin i allmänhet förklarar jag allt i den här artikeln: [länk](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).


### Använda Whirlpool Stat Tool.


Efter att ha utfört CoinJoins med Whirlpool kanske du vill veta den faktiska sekretessnivån för dina blandade UTXO:er. Whirlpool Stat Tool låter dig enkelt göra detta. Med det här verktyget kan du beräkna den prospektiva poängen och den retrospektiva poängen för dina blandade UTXO:er. För att lära dig mer om hur du beräknar dessa Anon Sets och hur de fungerar rekommenderar jag att du läser det här avsnittet: [länk](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment).


Verktyget är förinstallerat på din RoninDojo. För närvarande är det bara tillgängligt från RoninCLI. För att starta det från huvudmenyn, gå till:

**Samourai Toolkit > Whirlpool Statistikverktyg**


Bruksanvisningen kommer att visas. När du är klar trycker du på valfri tangent för att komma till kommandoraderna:


![Whirlpool Stats Tool software home](assets/28.webp)


Terminalen kommer att visa:

**wst#/tmp>**


För att avsluta denna Interface och återgå till RoninCLI-menyn, ange bara kommandot:

```
quit
```


Till att börja med kommer vi att ställa in proxyen på Tor för att extrahera OXT-data med fullständig integritet. Ange kommandot:

```
socks5 127.0.0.1:9050
```


Ladda sedan ner data från den pool som innehåller din transaktion:

```
download 0001
```


**Anmärkning:** ersätt `0001` med den poolvalutakod som intresserar dig.


Valörkoderna är som följer på WST:



- Pool 0,5 bitcoins: 05
- Pool 0,05 bitcoins: 005
- Pool 0,01 bitcoins: 001
- Pool 0,001 bitcoins: 0001


![Downloading data from pool 0001 from OXT](assets/29.webp)


När datan har laddats ner laddar du den med kommandot:

```
load 0001
```


**Anmärkning:** ersätt `0001` med den poolvalutakod som intresserar dig.


![Loading data from pool 0001](assets/30.webp)

Låt laddningsprocessen pågå, det kan ta några minuter. När du har laddat data skriver du kommandot score följt av din txid (transaktionsidentifierare) för att få fram Anon Sets:

```
score TXID
```


**Anmärkning:** ersätt `txid` med identifieraren för din transaktion.


![Printing the prospective and retrospective scores of the given TXID](assets/31.webp)


WST kommer sedan att visa den retrospektiva poängen (bakåtblickande mätvärden) följt av den prospektiva poängen (framåtblickande mätvärden). Förutom poängen för Anon Sets ger WST dig också spridningshastigheten för din produktion i poolen baserat på Anon Set.


Observera att den prospektiva poängen för din UTXO beräknas baserat på txid för din initiala mix, inte din senaste mix. Omvänt beräknas den retrospektiva poängen för en UTXO baserat på txid för den senaste cykeln.


Återigen, om du inte förstår dessa begrepp med Anon Sets, rekommenderar jag att du läser den här delen av min artikel om CoinJoin där jag förklarar allt i detalj med diagram: [https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment)


### Använda Boltzmanns kalkylator.


Boltzmann-kalkylatorn är ett verktyg som gör att du enkelt kan beräkna olika avancerade mätvärden för en Bitcoin-transaktion, inklusive dess entropinivå. Alla dessa data gör det möjligt för dig att kvantifiera sekretessnivån för en transaktion och upptäcka eventuella fel. Det här verktyget är förinstallerat på din RoninDojo-nod.


För att komma åt den från RoninCLI ansluter du via SSH och går sedan till menyn:

**Samourai Toolkit > Boltzmann-kalkylator**


Innan jag förklarar hur man använder det på RoninDojo ska jag förklara vad dessa mätvärden representerar, hur de beräknas och vad de används till.


Dessa indikatorer kan användas för alla Bitcoin-transaktioner, men de är särskilt intressanta för att studera kvaliteten på en CoinJoin-transaktion.


1. Den första indikatorn som beräknas av denna programvara är antalet möjliga kombinationer. Den noteras på räknaren som "nb combinations". Med tanke på UTXO:ernas värden representerar denna indikator antalet möjliga mappningar från ingångar till utgångar.


**not:** om du inte känner till termen `UTXO` rekommenderar jag att du läser den här korta artikeln:


> Mekanism för en Bitcoin-transaktion: UTXO, inmatningar och utmatningar.

Med andra ord representerar denna indikator antalet möjliga tolkningar för en given transaktion. Till exempel kommer en Whirlpool 5x5 CoinJoin-struktur att ha ett antal möjliga kombinationer som är lika med 1496:


![Schema of a Coinjoin transaction on kycp.org](assets/32.webp)


Kredit: KYCP


2. Den andra beräknade indikatorn är entropin för en transaktion. Eftersom antalet möjliga kombinationer kan vara mycket högt för en transaktion kan man välja att använda entropi istället. Entropi representerar den binära logaritmen av antalet möjliga kombinationer. Dess formel är som följer:



- E: Transaktionens entropi.
- C: antal möjliga kombinationer för transaktionen.


**E = log2(C)**


Inom matematiken är den binära logaritmen (bas 2) den omvända funktionen till potensen av 2-funktionen. Med andra ord är den binära logaritmen för x den potens som talet 2 måste upphöjas till för att erhålla värdet x.


Så är det:


**E = log2(C)**


**C = 2^E**


Denna indikator uttrycks i bitar. Här är t.ex. beräkningen av entropin för en Whirlpool 5x5 CoinJoin-transaktion, med ett tidigare nämnt antal möjliga kombinationer som är lika med 1496:


**C = 1496**


**E = log2(1496)**


**E = 10,5469 bitar**


Därför har denna CoinJoin-transaktion en entropi på 10,5469 bitar, vilket är mycket bra.


Ju högre denna indikator är, desto fler olika tolkningar av transaktionen finns det och desto mer konfidentiell är därför transaktionen.


Låt oss ta ett annat exempel. Här är en "klassisk" transaktion som har en ingång och två utgångar:


![Bitcoin transaction schema on oxt.me](assets/34.webp)


Kredit: OXT


Denna transaktion har bara en möjlig tolkning:


**[(inp 0) > (Outp 0 ; Outp 1)]**


Så dess entropi kommer att vara lika med 0:


**C = 1**,

**E = log2(C)**,

**E = 0**


3. Den tredje indikatorn som Boltzmann-kalkylatorn returnerar är effektiviteten hos Tx, kallad "Wallet Efficiency". Denna indikator gör det helt enkelt möjligt att jämföra den ingående transaktionen med den bästa möjliga transaktionen i samma konfiguration.


Vi kommer nu att introducera begreppet maximal entropi, som representerar den högsta uppnåeliga entropin för en given transaktionsstruktur. Till exempel kommer en Whirlpool 5x5 CoinJoin-struktur att ha en maximal entropi på 10,5469. Effektivitetsindikatorn jämför denna maximala entropi med den faktiska entropin för den ingående transaktionen. Dess formel är som följer:



- ER: Faktisk entropi uttryckt i bitar.
- EM: Maximal entropi med samma struktur uttryckt i bitar.
- Ef: Effektivitet uttryckt i bitar.


**Ef = ER - EM**


**Ef = 10,5469 - 10,5469**


**Ef = 0 bitar**


Denna indikator uttrycks också som en procentsats, så formeln blir:



- CR: Faktiskt antal möjliga kombinationer.
- CM: Maximalt antal möjliga kombinationer med samma struktur.
- Ef: Effektivitet uttryckt i procent.


**Ef = CR/CM**


**Ef = 1496/1496**


**Ef = 100%**


En effektivitet på 100% innebär att den här transaktionen har högsta möjliga sekretess i förhållande till sin struktur.


4. Den fjärde beräknade indikatorn är entropitätheten. Den gör det möjligt för oss att relatera entropin till varje in- eller utdata. Denna indikator kan användas för att jämföra effektiviteten mellan transaktioner av olika storlek.


Beräkningen är mycket enkel: vi delar transaktionens entropi med antalet in- och utgångar som finns. Till exempel, för en Whirlpool 5x5 CoinJoin, skulle vi ha:


ED: Entropidensitet uttryckt i bitar.

E: Transaktionens entropi uttryckt i bitar.

T: Totalt antal inmatningar och utmatningar i transaktionen.


T = 5 + 5 = 10

ED = E / T

ED = 10,5469 / 10

ED = 1.054 bitar


Den femte informationen som Boltzmannkalkylatorn tillhandahåller är sannolikhetstabellen över länkar mellan in- och utdata. Denna tabell ger dig helt enkelt sannolikheten (Boltzmann-poängen) för att en given input motsvarar en given output.


Om vi tar vårt exempel med en Whirlpool CoinJoin, skulle sannolikhetstabellen vara:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


Här kan vi se att varje indata har lika stor sannolikhet att kopplas till varje utdata.


Men om vi tar ett exempel på en transaktion med en ingång och två utgångar, skulle det se ut så här:


| Input | Output 0 | Output 1 |
| ----- | -------- | -------- |
| 0     | 100%     | 100%     |

I det här exemplet kan vi se att sannolikheten för att varje utdata kommer från ingång 0 är 100%.


Ju lägre denna sannolikhet är, desto högre är sekretessnivån.


6. Den sjätte uppgiften som beräknas är antalet deterministiska länkar. Förhållandet mellan deterministiska länkar kommer också att tillhandahållas. Denna indikator visar antalet länkar mellan inputs och outputs i den aktuella transaktionen som har en sannolikhet på 100%, vilket innebär att de är obestridliga.


Förhållandet anger antalet deterministiska länkar i transaktionen jämfört med det totala antalet länkar.


En CoinJoin Whirlpool-transaktion har t.ex. inga deterministiska länkar mellan in- och utdata. Indikatorn blir noll och kvoten blir också 0%.


För den andra undersökta transaktionen (1 inmatning och 2 utmatningar) är indikatorn 2 och förhållandet 100%.


Om denna indikator är noll tyder det därför på god sekretess.


Nu när vi har studerat indikatorerna, låt oss se hur man beräknar dem med hjälp av denna programvara. Från RoninCLI, gå till menyn:

**Samourai Toolkit > Boltzmann-kalkylator**


![Boltzmann Calculator software homepage](assets/35.webp)


När programvaran har startats anger du den transaction ID som du vill studera. Du kan ange flera transaktioner samtidigt genom att skilja dem åt med ett kommatecken och sedan trycka på Enter:


![Enter a TXID to study on Boltzmann Calculator](assets/36.webp)


Kalkylatorn kommer då att returnera alla de indikatorer som vi har sett tidigare:


![Printing of Boltzmann Calculator data for this TXID](assets/37.webp)


Skriv kommandot "Quit" för att avsluta programmet och återgå till RoninCLI-menyn.


Om du vill veta mer om Boltzmanns kalkylator rekommenderar jag att du läser dessa artiklar:



- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159



- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf


### Ansluter Bisq.


Bisq är en peer-to-peer Exchange plattform som gör att du kan köpa och sälja bitcoins. Den används med en skrivbordsprogramvara som körs på Tor och låter dig Exchange bitcoins utan att behöva ange din identitet.

Bisq säkrar peer-to-peer-utbyten genom ett 2/2 multisignatursystem. Du kan använda denna programvara med din egen RoninDojo-nod för att optimera integriteten för dina utbyten och lita på data från din egen nods Blockchain.


För att ladda ner Bisq-programvaran, gå till deras officiella webbplats: https://bisq.network/


För att komma igång med programvaran rekommenderar jag att du läser den här sidan: https://bisq.network/getting-started/


För att hämta anslutningslänken från din RoninDojo behöver du ansluta till RoninCLI via SSH. Gå sedan till menyn:

**Applikationer > Hantera applikationer**


Ange ditt lösenord och markera sedan rutan med mellanslagstangenten:

**[ ] Aktivera Bisq-anslutning**


Bekräfta ditt val. Låt din nod installeras och hämta sedan Tor V3 Address från:

**Behörighetsuppgifter > bitcoind**


Kopiera Address under "Bitcoin daemon".


Du kan också hämta din bitcoind Tor V3 Address från RoninUI Interface genom att helt enkelt klicka på "Manage" i rutan "Bitcoin Core" på "Dashboard":


![Retrieve TorV3 Bitcoin Daemon address on RoninUI](assets/38.webp)


För att ansluta din nod från Bisq, gå till menyn:

**Inställningar > Nätverksinformation**


![Access the node connection interface from the Bisq software](assets/39.webp)


Klicka på bubblan "Använd anpassade Bitcoin Core-noder". Ange sedan din Bitcoin TorV3 Address i den angivna rutan, med ".onion" men utan "http://".


![Box to enter the TorV3 address of your node in the Bisq software](assets/40.webp)


Starta om Bisq-programvaran. Din nod är nu ansluten till din Bisq.


### Övriga funktioner.


Din RoninDojo-nod innehåller också andra grundläggande funktioner. Du har möjlighet att skanna specifik information för att säkerställa att den tas i beaktande.


Det är till exempel ibland möjligt att din Wallet som är ansluten till din RoninDojo inte hittar de bitcoins som tillhör dig. Saldot är 0 trots att du är säker på att du har Bitcoin i den här Wallet. Det finns många möjliga orsaker att överväga, inklusive ett fel i derivationsvägarna, och bland dem är det också möjligt att din nod inte observerar dina adresser.


För att åtgärda detta kan du kontrollera att din nod spårar din xpub med "xpub tool". För att komma åt det från RoninUI, gå till menyn:

**Underhåll > XPUB Tool**


Ange den problematiska xpuben och klicka på "Check" för att verifiera denna information.


![XPUB Tool from RoninUI](assets/41.webp)


Om din xpub spåras av noden kommer du att se detta visas:


![XPUB Tool result showing successful analysis](assets/42.webp)


Kontrollera att alla transaktioner visas korrekt. Kontrollera också att avledningstypen matchar den för din Wallet. Här kan vi se att noden tolkar denna xpub som en BIP44-avledning. Om denna avledningstyp inte matchar den som finns i din Wallet, klicka på knappen "Retype" och välj sedan BIP44/BIP49/BIP84 enligt ditt val:


![Change the derivation type of the studied xpub from RoninUI](assets/43.webp)


Om din xpub inte spåras av din nod kommer du att se denna skärm där du uppmanas att importera den:


![Import an xpub with XPUB Tool on RoninUI](assets/44.webp)


Du kan också använda andra underhållsverktyg:



- Transaktionsverktyg: Ger dig möjlighet att se detaljerna i en specifik transaktion.
- Address-verktyg: Gör det möjligt för dig att verifiera att en specifik Address spåras av din Dojo.
- Skanna om block: Tvingar noden att skanna om ett utvalt antal block.


Du hittar också verktyget "Push Tx" på RoninUI. Det gör att du kan sända en signerad transaktion till Bitcoin-nätverket. Den måste anges i hexadecimalt format:


![Tool for broadcasting a signed transaction from RoninUI](assets/45.webp)


## Slutsats.


Vi har sett hur man installerar och kommer igång med detta underbara verktyg som är RoninDojo. Det är ett utmärkt val för att köra din egen Bitcoin-nod. Det är en stabil lösning som integrerar och håller uppdaterade alla viktiga verktyg för en Bitcoiner.


Om du inte är rädd för att använda terminalen och om du inte behöver verktyg relaterade till Lightning Network, kan RoninDojo tilltala dig.


Om du kan, överväg att donera till de utvecklare som fritt producerar dessa program med öppen källkod åt dig: https://donate.ronindojo.io/


För att lära dig mer om RoninDojo rekommenderar jag att du kollar in länkarna i mina externa resurser nedan.


### Ytterligare läsning:



- Förstå och använda CoinJoin på Bitcoin.
- Hash funktioner - utdrag ur e-boken Bitcoin Démocratisé 1.
- Allt du behöver veta om Bitcoin passphrase.


### Externa resurser:



- https://ronindojo.io/index.html
- https://wiki.ronindojo.io/en/home
- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159
- https://en.wikipedia.org/wiki/Boltzmann_formula
- https://wiki.ronindojo.io/en/setup/bisq
- https://bisq.network/