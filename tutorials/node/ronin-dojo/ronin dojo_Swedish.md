# Installera och använda sin RoninDojo Bitcoin-nod.

Att köra och använda sin egen nod är avgörande för att verkligen delta i Bitcoin-nätverket. Även om att köra en Bitcoin-nod inte ger någon ekonomisk fördel för användaren, gör det det möjligt att bevara sin integritet, agera oberoende och ha kontroll över sitt förtroende för nätverket.

I den här artikeln kommer vi att titta närmare på RoninDojo, en utmärkt lösning för att köra sin egen Bitcoin-nod.

### Innehållsförteckning:

- Vad är RoninDojo?
- Vilken hårdvara ska man välja?
- Hur installerar man RoninDojo?
- Hur använder man RoninDojo?
- Slutsats

Om du inte är bekant med hur en Bitcoin-nod fungerar och vilken roll den spelar, rekommenderar jag att du börjar med att läsa den här artikeln: Bitcoin-noden - Del 1/2: Tekniska begrepp.

![Samourai](assets/1.png)

## Vad är RoninDojo?

Dojo är en komplett Bitcoin-nodserver utvecklad av Samouraï Wallet-teamet. Du kan installera den fritt på vilken maskin som helst.

RoninDojo är en installationsassistent och administrationsverktyg för Dojo och olika andra verktyg. RoninDojo använder den ursprungliga implementationen av Dojo och lägger till många andra verktyg samtidigt som det förenklar installationen och hanteringen.

De erbjuder också en "plug-and-play" hårdvara, RoninDojo Tanto, med förinstallerad RoninDojo på en maskin som monterats av deras team. Tanto är en betalningslösning som kan vara intressant för dem som inte vill krångla med installationen själva.

RoninDojo-koden är öppen källkod, så det är också möjligt att installera denna lösning på egen hårdvara. Detta alternativ är ekonomiskt men kräver lite mer arbete, vilket vi kommer att gå igenom i den här artikeln.

RoninDojo är en Dojo, vilket innebär att den enkelt kan integrera Whirlpool CLI med din Bitcoin-nod för att ge dig den bästa möjliga CoinJoin-upplevelsen. Med Whirlpool CLI kan du inte bara blanda dina bitcoins 24/7 utan att behöva ha din persondator igång, utan du kan också kraftigt förbättra din integritet.

RoninDojo har många andra verktyg som bygger på din Dojo, till exempel Boltzmann-kalkylatorn som används för att bestämma graden av integritet för en transaktion, Electrum-servern för att ansluta dina olika Bitcoin-plånböcker till din nod, och Mempool-servern för att privat observera dina transaktioner.
Jämfört med en annan nodlösning som Umbrel, som jag presenterade för er i den här artikeln, är RoninDojo starkt inriktad på "On Chain"-lösningar och verktyg som optimerar användarnas integritet. RoninDojo möjliggör därför inte interaktion med Lightning Network.
RoninDojo erbjuder färre verktyg jämfört med Umbrel, men de få essentiella funktionerna för en Bitcoin-användare som finns på Ronin är otroligt stabila.

Så om du inte behöver alla funktioner i en Umbrel-server och bara vill ha en enkel och stabil nod med några essentiella verktyg som Whirlpool eller Mempool, är RoninDojo förmodligen en bra lösning för dig.

Enligt min åsikt är Umbrels utvecklingsinriktning mycket inriktad på Lightning Network och mångsidiga verktyg. Det förblir en Bitcoin-nod, men man försöker göra den till en multitasking-mini-server. Å andra sidan närmar sig RoninDojos utvecklingslinje mer den hos Samourai Wallet-teamen och fokuserar på en Bitcoin-användares essentiella verktyg som ger fullständig självständighet och optimerad hantering av integritet på Bitcoin.

Observera att installationen av en RoninDojo-nod är något mer komplicerad än en Umbrel-nod.

Nu när vi har fått en bild av RoninDojo, låt oss se hur man installerar denna nod.

## Vilken hårdvara ska man välja?

För att välja den maskin som ska vara värd och köra RoninDojo har du flera alternativ.

Som tidigare förklarat är det enklaste valet att beställa Tanto, en plug-and-play-maskin som är speciellt utformad för detta ändamål. För att beställa din, gå till: https://shop.ronindojo.io/product-category/nodes/.

Eftersom RoninDojo-teamen producerar öppen källkod är det också möjligt att implementera RoninDojo på andra maskiner. Du kan hitta de senaste versionerna av installationsguiden på den här sidan: https://ronindojo.io/en/downloads.html, och de senaste versionerna av koden på den här sidan: https://code.samourai.io/ronindojo/RoninDojo.

Personligen har jag installerat det på en Raspberry Pi 4 med 8 GB RAM och allt fungerar perfekt.

Var dock uppmärksam på att RoninDojo-teamen informerar oss om att det ofta uppstår problem på grund av SSD-fodralet och adaptern. Det rekommenderas därför att inte använda ett fodral med en kabel för din maskins SSD. Det är bättre att använda en lagringsförlängningskort som är speciellt utformad för ditt moderkort, som detta: Lagringsförlängningskort för Raspberry Pi 4.

Här är ett exempel på hur du kan installera din egen RoninDojo-nod:

- En Raspberry Pi 4.
- Ett fodral med en fläkt.
- Ett kompatibelt lagringsutvidgningskort.
- En strömkabel.
- Ett industriellt micro SD-kort på 16GB eller mer.
- En SSD på 1TB eller mer.
- En Ethernet RJ45-kabel, kategori 8 rekommenderas.

## Hur installerar man RoninDojo?

### Steg 1: Förbered den bootbara micro SD-kortet.

När du har monterat din maskin kan du börja installera RoninDojo. Börja med att skapa en bootbar micro SD-kort genom att bränna rätt diskavbildning på den.

Sätt in ditt micro SD-kort i din persondator och gå sedan till RoninDojos officiella webbplats för att hämta RoninOS-diskavbildningen: https://ronindojo.io/en/downloads.html.

Ladda ner den diskavbildning som passar din maskin. I mitt fall laddade jag ner "MANJARO-ARM-RONINOS-RPI4-22.03.IMG.XZ"-avbildningen:

![Ladda ner RoninOS-diskavbildning](assets/2.png)

När avbildningen är nedladdad, kontrollera dess integritet med hjälp av den motsvarande .SHA256-filen. Jag beskriver i detalj hur du gör detta i den här artikeln: Hur kontrollerar man integriteten hos Bitcoin-programvara på Windows?

Specifika instruktioner för att kontrollera integriteten hos RoninOS finns också tillgängliga på denna sida på engelska: https://wiki.ronindojo.io/en/extras/verify.

För att bränna denna avbildning på ditt micro SD-kort kan du använda programvara som Balena Etcher, som du kan ladda ner här: https://www.balena.io/etcher/.

Välj avbildningen i Etcher och bränn den på micro SD-kortet:

![Bränn diskavbildning med Etcher](assets/3.png)

När operationen är klar kan du sätta in det bootbara micro SD-kortet i Raspberry Pi och starta maskinen.

### Steg 2: Konfigurera RoninOS.

RoninOS är operativsystemet för din RoninDojo-nod, det är en modifierad version av Manjaro, en Linux-distribution. Efter att ha startat din maskin och väntat några minuter kan du börja konfigurera den.

För att ansluta till den på distans måste du hitta IP-adressen för din RoninDojo-maskin. Du kan till exempel ansluta till din internetbox administrationspanel eller använda programvara som https://angryip.org/ för att skanna ditt lokala nätverk och hitta maskinens IP-adress.

När du har hittat IP-adressen kan du ta kontroll över din maskin från en annan dator som är ansluten till samma lokala nätverk genom att använda SSH.

Från en dator med MacOS eller Linux, öppna bara terminalen. Från en dator med Windows kan du använda ett specialiserat verktyg som Putty eller direkt Windows PowerShell.

När terminalen är öppen, skriv följande kommando:

> ssh root@192.168.?.?

Ersätt bara frågetecknen med IP-adressen för din tidigare hittade RoninDojo.
Tips: I en Shell, högerklicka för att klistra in ett element.

Därefter kommer du att komma till Manjaros kontrollpanel. Välj rätt tangentbordslayout genom att använda pilarna för att ändra målet i rullgardinsmenyn.

![Manjaros tangentbordskonfiguration](assets/4.png)

Välj ett användarnamn och ett lösenord för din session. Använd ett starkt lösenord och gör en säkerhetskopia av det. Du kan eventuellt använda ett svagt lösenord under installationen och sedan enkelt ändra lösenordet med möjligheten att "kopiera och klistra in" det i RoninUI. Detta gör att du kan använda ett mycket starkt lösenord utan att behöva spendera för mycket tid på att skriva det manuellt vid installationen av Manjaro.

![Manjaros användarnamnskonfiguration](assets/5.png)

Därefter kommer du också att bli ombedd att välja ett root-lösenord. Ange direkt ett starkt lösenord för root. Du kommer inte att kunna ändra det från RoninUI. Kom också ihåg att säkerhetskopiera detta root-lösenord ordentligt.

Ange sedan din plats och tidszon.

![Manjaros tidszonkonfiguration](assets/6.png)

![Manjaros platskonfiguration](assets/7.png)

Välj sedan ett värdnamn.

![Manjaros värdnamnskonfiguration](assets/8.png)

Slutligen, kontrollera Manjaros konfigurationsinformation och bekräfta.

![Verifiering av ManjaroOS konfigurationsinformation](assets/9.png)

### Steg 3: Ladda ner RoninDojo.

Den initiala konfigurationen av RoninOS kommer att göras. När den är klar, som på skärmdumpen ovan, kommer maskinen att starta om. Vänta sedan några ögonblick och ange följande kommando för att ansluta till din RoninDojo-maskin igen:

> ssh användarnamn@192.168.?.?

Byt helt enkelt ut "användarnamn" mot det användarnamn du tidigare valt, och frågetecknen mot din RoninDojos IP-adress.

Ange sedan ditt användarlösenord.

I terminalen ser det ut så här:

![SSH-anslutning till RoninOS](assets/10.png)

Du är nu ansluten till din maskin som för tillfället bara har RoninOS installerat. Nu måste du installera RoninDojo på den.

Ladda ner den senaste versionen av RoninDojo genom att ange följande kommando:

> git clone https://code.samourai.io/ronindojo/RoninDojo

Nedladdningen går snabbt. Det kommer att se ut så här i terminalen:

![Kloning av RoninDojo](assets/11.png)

Vänta tills nedladdningen är klar och installera och kom åt RoninDojos användargränssnitt med följande kommando:

> ~/RoninDojo/ronin

Du kommer då att bli ombedd att ange ditt användarlösenord:

![Verifiering av Bitcoin-nodens lösenord](assets/12.png)
Denna kommando är endast nödvändig första gången du får åtkomst till din RoninDojo. Därefter, för att få åtkomst till RoninCLI via SSH, behöver du bara ange kommandot [SSH användarnamn@192.168.?.?] och ersätta "användarnamn" med ditt användarnamn och ange din nodens IP-adress. Du kommer att bli ombedd att ange ditt användarlösenord.

Därefter kommer du att se denna fantastiska animation:

![RoninCLI startanimation](assets/13.png)

Sedan kommer du äntligen att komma till RoninDojos CLI-gränssnitt.

### Steg 4: Installera RoninDojo.

Från huvudmenyn, gå till "System" genom att använda piltangenterna på tangentbordet. Använd Enter-tangenten för att bekräfta ditt val.

![Navigering i RoninCLI-meny till System](assets/14.png)

Gå sedan till menyn "System Setup & Install".

![Navigering i RoninCLI-meny till installation av RoninDojo-system](assets/15.png)

Markera "System Setup" och "Install RoninDojo" genom att använda mellanslagstangenten och välj sedan "Accept" för att starta installationen.

![Bekräftelse av installation av RoninDojo](assets/16.png)

Låt installationen slutföras i lugn och ro. I mitt fall tog det cirka 2 timmar. Håll terminalen öppen under processen.

Titta ibland på terminalen, du kommer att bli ombedd att trycka på en tangent vid vissa steg i installationen, som här till exempel:

![Installation av RoninDojo pågår](assets/17.png)

När installationen är klar kommer du att se de olika behållarna starta:

![Start av nodens behållare](assets/18.png)

Sedan kommer din nod att starta om. Anslut igen till RoninCLI för nästa steg.

![Bitcoin-nodens omstart](assets/19.png)

### Steg 5: Ladda ner arbetsbeviskedjan och få åtkomst till RoninUI.

När installationen är klar kommer din nod att börja ladda ner Bitcoin-arbetsbeviskedjan. Detta kallas IBD (Initial Block Download). Det tar vanligtvis mellan 2 och 14 dagar beroende på din internetanslutning och enhet.

Du kan följa nedladdningsframstegen för kedjan genom att ansluta till RoninUI:s webbgränssnitt.

För att komma åt det från ett lokalt nätverk, skriv följande i webbläsarens adressfält:

- Antingen direkt din enhets IP-adress (192.168.?.?)

- Eller: ronindojo.local

Kom ihåg att stänga av din VPN om du använder en.

### Möjlig twist

Om du inte kan ansluta till RoninUI från din webbläsare, kontrollera att applikationen fungerar korrekt från ditt terminalfönster som är anslutet till din nod via SSH. Anslut till huvudmenyn genom att följa samma steg som tidigare:

- Skriv: SSH användarnamn@192.168.?.? och ersätt med dina egna uppgifter.

- Ange ditt användarlösenord.
  När du är på huvudmenyn, gå till:
  > RoninUI > Starta om

Om applikationen startar om korrekt är problemet med anslutningen från din webbläsare. Kontrollera att du inte använder en VPN och se till att du är ansluten till samma nätverk som din nod.

Om omstarten ger ett fel, försök att uppdatera operativsystemet och sedan installera om RoninUI. För att uppdatera OS:

> System > Programuppdateringar > Uppdatera operativsystemet

När uppdateringen och omstarten är klara, anslut till din nod via SSH och installera om RoninUI:

> RoninUI > Installera om

Efter att ha laddat ner RoninUI på nytt, försök att ansluta till RoninUI via din webbläsare.

> Tips: Om du av misstag lämnar RoninCLI och hamnar i Manjaro-terminalen, skriv bara in kommandot "ronin" för att direkt återgå till RoninCLI:s huvudmeny.

### Webbinloggning

Du kan också ansluta till RoninUI:s webbgränssnitt från vilket nätverk som helst med hjälp av Tor. För att göra detta, hämta Tor-adressen för din RoninUI från RoninCLI:

> Användaruppgifter > Ronin UI

Hämta Tor-adressen som slutar med .onion och anslut till Ronin UI genom att ange denna adress i din Tor-webbläsare. Var försiktig så att du inte läcker dina autentiseringsuppgifter, eftersom de är känslig information.

![Webbgränssnitt för inloggning till RoninUI](assets/20.png)

När du är ansluten kommer du att bli ombedd att ange ditt användarlösenord. Det är samma lösenord som du använder för att ansluta via SSH.

![Hanteringspanel för RoninUI:s webbgränssnitt](assets/21.png)

Vi kan se framsteg för IBD (Initial Block Download) här. Var tålmodig, du håller på att hämta alla transaktioner som har gjorts på Bitcoin sedan den 3 januari 2009.

Efter att ha laddat ner hela blockkedjan kommer indexeringen att komprimera databasen. Detta tar cirka 12 timmar. Du kan också följa framstegen under "Indexer" på RoninUI.

Din RoninDojo-nod kommer att vara helt fungerande efter detta:

![Indexer synkroniserad till 100% - fungerande nod](assets/22.png)

Om du vill ändra användarlösenordet till ett starkare kan du göra det nu från fliken "Inställningar". På RoninDojo finns det ingen extra säkerhetsnivå, så jag rekommenderar att du väljer ett riktigt starkt lösenord och ser till att det är ordentligt säkerhetskopierat.

## Hur använder man RoninDojo?

När kedjan har laddats ner och komprimerats kan du börja använda de tjänster som din nya RoninDojo-nod erbjuder. Låt oss titta på hur du använder dem.

### Ansluta dina plånboksprogram till electrs.

Det första användningsområdet för din nyinstallerade och synkroniserade nod kommer att vara att sprida dina transaktioner till Bitcoin-nätverket. Du kommer därför förmodligen vilja ansluta dina olika plånboksprogram till den.

Du kan göra detta med hjälp av Electrum Rust Server (electrs). Applikationen är normalt förinstallerad på din RoninDojo-nod. Om så inte är fallet kan du installera den manuellt från RoninCLI-gränssnittet.

Gå bara till:

> Applications > Manage Applications > Install Electrum Server

För att få Tor-adressen till din Electrum Server, gå till:

> Credentials > Electrs

Du behöver bara ange .onion-länken i din plånboksprogramvara. Till exempel i Sparrow Wallet, gå bara till fliken:

> File > Preferences > Server

Välj "Private Electrum" som servertyp och ange sedan Tor-adressen till din Electrum Server i det motsvarande fältet. Klicka slutligen på "Test Connection" för att testa och spara din anslutning.

![Anslutningsgränssnitt för Sparrow Wallet till en electrs](assets/23.png)

### Ansluta dina plånboksprogram till Samourai Dojo.

Istället för att använda Electrs kan du också använda Samourai Dojo för att ansluta din kompatibla plånboksprogramvara till din RoninDojo-nod. Till exempel erbjuder Samourai Wallet detta alternativ.

För att göra detta behöver du bara skanna QR-koden för anslutning till din Dojo. För att komma åt den från RoninUI, klicka på fliken "Dashboard" och sedan på knappen "Manage" i rutan för din Dojo. Du kan sedan se QR-koderna för anslutning till din Dojo och BTC-RPC Explorer. Klicka på "Display values" för att visa dem tydligt.

![Återställning av QR-kod för anslutning till Dojo](assets/24.png)

För att ansluta din Samourai Wallet till din Dojo måste du skanna denna QR-kod vid installationen av applikationen:

![Anslutning till Dojo från Samourai Wallet-applikationen](assets/25.png)

### Använda din egen Mempool Explorer.

Som en viktig verktyg för Bitcoin-användare kan en explorer användas för att kontrollera olika information om Bitcoin-kedjan. Med Mempool kan du till exempel kontrollera de avgifter som tillämpas av andra användare i realtid för att justera dina egna. Du kan också kontrollera statusen för bekräftelse av en av dina transaktioner eller titta på saldot för en adress.

Dessa explorer-verktyg kan utsätta dig för sekretessrisker och tvingar dig att lita på en tredjepartsdatabas. När du använder detta onlineverktyg utan att gå via din egen nod:

- Du riskerar att läcka information om din plånbok.

- Du litar på webbplatsens förvaltare för den arbetsbeviskedja som de värdar.
  För att undvika dessa risker kan du använda din egen Mempool-instans på din nod via Tor-nätverket. Med denna lösning bevarar du inte bara din integritet när du använder tjänsten, utan du behöver heller inte längre lita på en leverantör eftersom du frågar din egen databas.

För att göra detta, börja med att installera Mempool Space Visualizer från RoninCLI:

> Applikationer > Hantera applikationer > Installera Mempool Space Visualizer

När det är installerat, hämta länken till din Mempool. Tor-adressen gör att du kan komma åt den från vilket nätverk som helst. På samma sätt hämtar vi denna länk via RoninCLI:

> Inloggningsuppgifter > Mempool

![Hämta Tor-adress för Mempool](assets/26.png)

Skriv bara in din Mempool Tor-adress i Tor-webbläsaren för att använda din egen Mempool-instans, baserad på dina egna data. Jag rekommenderar att du lägger till denna Tor-adress i dina bokmärken för att snabbt kunna komma åt den. Du kan också skapa en genväg på skrivbordet.

![Mempool Space-gränssnitt](assets/27.png)

Om du ännu inte har Tor-webbläsaren kan du ladda ner den här: https://www.torproject.org/download/

Du kan också komma åt den från din smartphone genom att installera Tor Browser och ange samma adress. Var som helst kan du övervaka tillståndet för Bitcoin-kedjan genom att använda din egen nod.

### Använda Whirlpool CLI.

Din RoninDojo-nod inkluderar också WhirlpoolCLI, ett fjärrstyrt kommandoradsgränssnitt som automatiserar Whirlpool-mixar.

När du gör en CoinJoin med Whirlpool-implementeringen måste applikationen du använder vara öppen för att kunna utföra mixar och remixar. Detta kan vara besvärligt för användare som vill ha höga anonyma uppsättningar, eftersom enheten som rymmer applikationen med Whirlpool måste vara påslagen hela tiden. I praktiken innebär detta att om du vill engagera dina UTXO i remixar 24/7 måste du lämna din persondator eller telefon påslagen med applikationen öppen.

En lösning på detta problem är att använda WhirlpoolCLI på en maskin som är avsedd att vara påslagen hela tiden, som till exempel en Bitcoin-nod. På så sätt kan våra UTXO remixas 24/7 utan att vi behöver ha en annan maskin än vår Bitcoin-nod igång.
WhirlpoolCLI används tillsammans med WhirlpoolGUI, en grafisk användargränssnitt som installeras på en persondator för att enkelt hantera Coinjoins. Jag förklarar i detalj hur du installerar Whirlpool CLI med din egen dojo i den här artikeln: https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=dans%20cette%20partie.-,Tutoriel%20%3A%20Whirpool%20CLI%20sur%20Dojo%20et%20Whirlpool%20GUI.,-Si%20vous%20souhaitez
För att lära dig mer om Coinjoin generellt, förklarar jag allt i den här artikeln: https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin

### Använda Whirlpool Stat Tool.

Efter att ha genomfört CoinJoin med Whirlpool vill du kanske veta konkret vilken sekretessnivå dina mixade UTXO har. Whirlpool Stat Tool gör det enkelt att göra det. Med detta verktyg kan du beräkna prospektiv och retrospektiv poäng för dina mixade UTXO. För att lära dig mer om beräkningen av dessa Anon Sets och hur de fungerar, rekommenderar jag att du läser den här delen: https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment

Verktyget är förinstallerat på din RoninDojo. För tillfället är det endast tillgängligt från RoninCLI. För att starta det från huvudmenyn, gå till:

> Samourai Toolkit > Whirlpool Stat Tool

Användningsinstruktionerna kommer att visas. När det är klart, tryck på vilken tangent som helst för att komma åt kommandoraderna:

![Whirlpool Stats Tool-programmets startsida](assets/28.png)

Du kommer att se terminalen visas:

> wst#/tmp>

För att avsluta gränssnittet och återgå till RoninCLI-menyn, skriv bara in kommandot:

> quit

För att börja, ska vi ställa in proxy på Tor för att kunna extrahera OXT-data i fullständig sekretess. Skriv in kommandot:

> socks5 127.0.0.1:9050

Ladda sedan ner data från poolen som innehåller din transaktion:

> download 0001
>
> Ersätt 0001 med den poolens beteckningskod som du är intresserad av.

Följande är beteckningskoderna för WST:

- Pool 0,5 bitcoins: 05

- Pool 0,05 bitcoins: 005

- Pool 0,01 bitcoins: 001

- Pool 0,001 bitcoins: 0001

![Ladda ner data från poolen 0001 från OXT](assets/29.png)

När data har laddats ner, ladda in den med kommandot:

> load 0001
>
> Ersätt 0001 med den poolens beteckningskod som du är intresserad av.
> ![Laddar data för pool 0001](assets/30.png)
> Låt laddningen ske, det kan ta några minuter. Efter att data har laddats, skriv in kommandot "score" följt av din TXID (transaktions-ID) för att få dess Anon Sets:

> score TXID
>
> Ersätt TXID med din transaktions-ID.

![Utskrift av prospektiva och retrospektiva poäng för den givna TXID](assets/31.png)

WST visar då den retrospektiva poängen (Backward-looking metrics) och sedan den prospektiva poängen (Forward-looking metrics). Förutom poängen för Anon Sets ger WST också spridningsgraden för din output i poolen baserat på anon set.

Observera att den prospektiva poängen för din UTXO beräknas utifrån TXID för din initiala mixning, inte från din senaste mixning. Å andra sidan beräknas den retrospektiva poängen för en UTXO utifrån TXID för den senaste cykeln.

Återigen, om du inte förstår dessa begrepp om Anon Sets, rekommenderar jag att du läser den här delen av min artikel om Coinjoin där jag förklarar allt i detalj med diagram: https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment

### Använda Boltzmann-kalkylatorn.

Boltzmann-kalkylatorn är ett verktyg som gör det enkelt att beräkna olika avancerade metriker för en Bitcoin-transaktion, inklusive dess entropinivå. Alla dessa data hjälper dig att sätta siffror på konfidentialitetsnivån för en transaktion och upptäcka eventuella fel. Det här verktyget är förinstallerat på din RoninDojo-nod.

För att komma åt det från RoninCLI, anslut via SSH och gå sedan till menyn:

> Samourai Toolkit > Boltzmann Calculator

Innan jag förklarar hur du använder det på RoninDojo, ska jag förklara vad dessa metriker representerar, hur de beräknas och vad de används till.

Dessa indikatorer kan användas för vilken Bitcoin-transaktion som helst, men de är särskilt intressanta för att studera kvaliteten på en Coinjoin-transaktion.

1. Den första indikatorn som beräknas av denna programvara är antalet möjliga kombinationer. Den anges i kalkylatorn som "nb combinations". Med hänsyn till UTXO-värdena representerar denna indikator antalet möjliga kartläggningar av ingångar till utgångar.

> Om du inte är bekant med termen "UTXO" rekommenderar jag att du läser denna korta artikel: Mekanismen för en Bitcoin-transaktion: UTXO, inputs och outputs.
> Med andra ord representerar denna indikator antalet möjliga tolkningar för en given transaktion. Till exempel: en Coinjoin med Whirlpool 5x5-struktur kommer att ha ett antal möjliga kombinationer lika med 1496:
> ![Schema för en Coinjoin-transaktion på kycp.org](assets/32.png)

Kredit: https://kycp.org/#/fe5e5abab7ea452f87603f7ebc2fa4e77380eafcc927e1cb51e1a72401ab073d

2. Den andra beräknade indikatorn är entropin för en transaktion ("Entropy"). Eftersom antalet möjliga kombinationer kan vara mycket högt för en transaktion kan man välja att använda entropi istället. Entropin representerar den binära logaritmen av antalet möjliga kombinationer. Formeln är följande för:

- E: transaktionens entropi.

- C: antalet möjliga kombinationer för transaktionen.

> E = log2(C)

I matematik är den binära logaritmen (med bas 2) den omvända funktionen till exponentieringsfunktionen med bas 2. Med andra ord är den binära logaritmen av x den exponent som 2 måste upphöjas till för att få värdet x.

Således:

> E = log2(C)
> C = 2^E

Denna indikator uttrycks därför i bitar. Till exempel, här är beräkningen av entropin för en Coinjoin-transaktion med Whirlpool 5x5-struktur, med som tidigare nämnts, ett antal möjliga kombinationer lika med 1496:

> C = 1496
>
> E = log2(1496)
>
> E = 10.5469 bitar

Denna Coinjoin-transaktion har alltså en entropi på 10.5469 bitar, vilket är mycket bra.

Ju högre denna indikator är, desto fler olika tolkningar av transaktionen finns det, och därmed desto mer konfidentiell är transaktionen.

Låt oss ta ett annat exempel. Här är en "vanlig" transaktion som har en ingång och två utgångar:

![Bitcoin-transaktionsschema på oxt.me](assets/34.png)

Kredit: https://oxt.me/graph/transaction/tiid/9815286

Denna transaktion har endast en möjlig tolkning:

> [(inp 0) > (Outp 0 ; Outp 1)]

Därför kommer dess entropi att vara lika med 0:

> C = 1
>
> E = log2(C)
>
> E = 0

3. Den tredje indikatorn som beräkningsverktyget Boltzmann ger är effektiviteten för Tx som kallas "Wallet Efficiency". Denna indikator gör det enkelt att jämföra den inmatade transaktionen med den bästa möjliga transaktionen i samma konfiguration.
   Vi kommer nu att introducera konceptet maximal entropi, vilket representerar den högsta uppnåeliga entropin för en given transaktionsstruktur. Till exempel kommer en Coinjoin-struktur av typen Whirlpool 5x5 att ha en maximal entropi på 10.5469. Effektivitetsindikatorn jämför sedan denna maximala entropi med den faktiska entropin för den inkommande transaktionen. Formeln är följande för:

- ER: Faktisk entropi uttryckt i bitar.

- EM: Maximal entropi med samma struktur uttryckt i bitar.

- Ef: Effektivitet uttryckt i bitar.

> Ef = ER - EM
>
> Ef = 10.5469 - 10.5469
>
> Ef = 0 bitar

Denna indikator uttrycks också i procent, och formeln blir då:

- CR: Antal möjliga faktiska kombinationer.

- CM: Antal möjliga kombinationer maximalt med samma struktur.

- Ef: Effektivitet uttryckt i procent.

> Ef = CR/CM
>
> Ef = 1496/1496
>
> Ef = 100%

En effektivitet på 100% innebär att denna transaktion har maximal möjlig sekretess med avseende på sin struktur.

4. Den fjärde beräknade indikatorn är entropitätheten ("Entropy Density"). Den gör det möjligt att relatera entropin till varje inmatning eller utmatning. På så sätt kan denna indikator användas för att jämföra effektiviteten mellan flera transaktioner av olika storlekar.

Beräkningen är mycket enkel, vi delar entropin för transaktionen med antalet inmatningar och utmatningar som finns där. Till exempel för en Coinjoin av typen Whirlpool 5x5 har vi:

    ED: Entropitäthet uttryckt i bitar.

    E: Entropi för transaktionen uttryckt i bitar.

    T: totalt antal inmatningar och utmatningar i transaktionen.

T = 5 + 5 = 10
ED = E / T
ED = 10.5469 / 10
ED = 1.054 bitar

Den femte informationen som tillhandahålls av Boltzmann-kalkylatorn är sannolikhetstabellen för länkar mellan inmatningar och utmatningar. Denna tabell ger dig helt enkelt sannolikheten (Boltzmann-poängen) att en given inmatning motsvarar en given utmatning.

Om vi tar vårt exempel med en Whirlpool Coinjoin kommer sannolikhetstabellen att vara:

| Inmatning | Utmatning 0 | Utmatning 1 | Utmatning 2 | Utmatning 3 | Utmatning 4 |
| --------- | ----------- | ----------- | ----------- | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| 0         | 34%         | 34%         | 34%         | 34%         | 34%         |
| 1         | 34%         | 34%         | 34%         | 34%         | 34%         |
| 2         | 34%         | 34%         | 34%         | 34%         | 34%         |
| 3         | 34%         | 34%         | 34%         | 34%         | 34%         |     | 4   | 34% | 34% | 34% | 34% | 34% |

Här kan vi tydligt se att varje input har lika stor sannolikhet att vara kopplad till varje output.

Om vi istället tar exemplet med en transaktion med en input och två output, ser det ut så här:

| Input | Output 0 | Output 1 |
| ----- | -------- | -------- |
| 0     | 100%     | 100%     |

I det här exemplet kan vi se att sannolikheten för varje output att komma från input 0 är 100%.

Ju lägre denna sannolikhet är, desto högre är sekretessen.

6. Den sjätte informationen som beräknas är antalet deterministiska länkar. Vi kommer också att tillhandahålla förhållandet av deterministiska länkar. Denna indikator visar antalet länkar mellan inputs och outputs i den givna transaktionen som har en sannolikhet på 100%, det vill säga att de är obestridliga.

Förhållandet indikerar sedan antalet deterministiska länkar i transaktionen i förhållande till det totala antalet länkar.

Till exempel har en Coinjoin Whirlpool-transaktion inga deterministiska länkar mellan inmatningar och utmatningar. Indikatorn kommer därför att vara noll och förhållandet kommer också att vara 0%.

Däremot, för den andra studerade transaktionen (1 input och 2 outputs), är indikatorn 2 och förhållandet är 100%.

Så om denna indikator är noll, indikerar det en god sekretess.

Nu när vi har studerat indikatorerna, låt oss se hur vi beräknar dem med hjälp av denna programvara. Gå till menyn från RoninCLI:

> Samourai Toolkit > Boltzmann Calculator

![Boltzmann Calculator-programmets startsida](assets/35.png)

När programvaran har startats, ange ID för transaktionen du vill studera. Du kan ange flera transaktioner samtidigt genom att separera dem med ett kommatecken och trycka på Enter:

![Ange en TXID att studera i Boltzmann Calculator](assets/36.png)

Beräknaren returnerar sedan alla indikatorer vi tidigare har sett:

![Utskrift av data från Boltzmann Calculator för denna TXID](assets/37.png)

Skriv "Quit" för att avsluta programmet och återgå till RoninCLI-menyn.

För mer information om Boltzmann-kalkylatorn rekommenderar jag att du läser dessa artiklar:

- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159

- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf

### Ansluta till Bisq.

Bisq är en handelsplattform som gör det möjligt att köpa och sälja bitcoins peer-to-peer. Den används med en skrivbordsprogramvara som körs via Tor och möjliggör utbyte av bitcoins utan att behöva ange sin identitet.
Bisq säkrar peer-to-peer-utbyten med hjälp av ett 2/2 multi-signature-system. Du kan använda denna programvara med din egen RoninDojo-nod för att optimera sekretessen för dina utbyten och lita på data från din egen nodens blockchain.
För att ladda ner Bisq-programvaran, gå till deras officiella webbplats: https://bisq.network/

För att komma igång med programvaran rekommenderar jag att du läser den här sidan: https://bisq.network/getting-started/

För att hämta anslutningslänken från din RoninDojo måste du ansluta till RoninCLI via SSH. Gå sedan till menyn:

> Applikationer > Hantera applikationer

Ange ditt lösenord och markera rutan med mellanslag:

> [ ] Aktivera Bisq-anslutning

Bekräfta ditt val. Låt din nod installera och hämta sedan Tor V3-adressen från:

> Anslutningsuppgifter > Bitcoind

Kopiera adressen under "Bitcoin Daemon".

Du kan också hämta din Bitcoind Tor V3-adress från RoninUI-gränssnittet genom att helt enkelt klicka på "Hantera" i rutan "Bitcoin Core" från "Instrumentpanelen":

![Hämta TorV3 Bitcoin Daemon-adress på RoninUI](assets/38.png)

För att ansluta din nod från Bisq, gå till menyn:

> Inställningar > Nätverksinformation

![Komma åt nodanslutningsgränssnittet från Bisq-programvaran](assets/39.png)

Klicka på bubblan "Använd anpassade Bitcoin Core-noder". Ange sedan din Bitcoin TorV3-adress i det angivna fältet, med ".onion" men utan "http://".

![Fält för att ange nodens TorV3-adress i Bisq-programvaran](assets/40.png)

Starta om Bisq-programvaran. Din nod är nu ansluten till din Bisq.

### Andra funktioner.

Din RoninDojo-nod har också andra grundläggande funktioner. Du har möjlighet att skanna specifik information för att se till att den beaktas.

Till exempel kan det ibland hända att din plånbok som är ansluten till din RoninDojo inte hittar de bitcoins som tillhör dig. Saldot är 0 trots att du är övertygad om att du har bitcoin i den här plånboken. Det finns många möjliga orsaker att ta hänsyn till, inklusive fel i avledningsvägarna, och en av dem är att din nod inte observerar dina adresser.

För att åtgärda detta kan du kontrollera att din nod spårar din xpub med verktyget "xpub tool". För att komma åt det från RoninUI, gå till menyn:

> Underhåll > XPUB-verktyg

Ange den xpub som orsakar problemet och klicka på "Kontrollera" för att verifiera denna information.

![XPUB-verktyg från RoninUI](assets/41.png)

Om din xpub spåras korrekt av noden kommer du att se följande:

![XPUB-verktyg, positivt resultat av analysen](assets/42.png)
Kontrollera att alla transaktioner visas korrekt. Kontrollera också att härledningstypen matchar din plånbok. Här kan vi se att noden tolkar denna xpub som en BIP44-härledning. Om denna härledningstyp inte matchar din plånbok, klicka på "Retype"-knappen och välj sedan BIP44/BIP49/BIP84 beroende på ditt val:
![Ändra härledningstyp för den undersökta xpuben från RoninUI](assets/43.png)

Om din xpub inte spåras av din nod kommer du att se den här skärmen som uppmanar dig att importera den:
![Importera en xpub med XPUB Tool på RoninUI](assets/44.png)

Du kan också använda andra underhållsverktyg:

- Transaktionsverktyg: Låter dig observera detaljerna i en specifik transaktion.

- Adressverktyg: Låter dig kontrollera att en specifik adress spåras korrekt av din Dojo.

- Skanna om block: Tvingar din nod att skanna om en vald blockintervall.

Du hittar också verktyget "Push Tx" på RoninUI. Det låter dig sända en signerad transaktion till Bitcoin-nätverket. Den måste anges i hexadecimalt format:
![Verktyg för att sända en signerad transaktion från RoninUI](assets/45.png)

## Slutsats.

Vi har sett hur man installerar och använder denna fantastiska verktyg som RoninDojo är. Det är ett utmärkt val för att köra sin egen Bitcoin-nod. Det är en stabil lösning som integrerar och håller alla nödvändiga verktyg uppdaterade för en Bitcoin-användare.

Om du inte är rädd för att använda terminalen och om du inte behöver verktyg relaterade till Lightning Network kan RoninDojo vara något för dig.

Om du kan, överväg att donera till utvecklarna som gratis producerar dessa fria och öppna programvaror för dig: https://donate.ronindojo.io/

För att lära dig mer om RoninDojo rekommenderar jag att du tittar på länkarna i mina externa resurser nedan.

### För att gå djupare:

- Förstå och använda CoinJoin på Bitcoin.

- Hashfunktioner - utdrag från e-boken Bitcoin Démocratisé 1.

- Allt du behöver veta om Bitcoin-passfrasen.

### Externa resurser:

    https://samouraiwallet.com/dojo

    https://ronindojo.io/index.html

    https://wiki.ronindojo.io/en/home

    https://code.samourai.io/ronindojo/RoninDojo

    https://gist.github.com/LaurentMT/e758767ca4038ac40aaf

    https://medium.com/@laurentmt/introducing-boltzmann-85930984a159

    https://oxt.me/

    https://kycp.org/#/

    https://fr.wikipedia.org/wiki/Formule_de_Boltzmann

    https://wiki.ronindojo.io/en/setup/bisq

    https://bisq.network/

https://www.pandul.fr/post/installer-et-utiliser-son-n%C5%93ud-bitcoin-ronindojo
