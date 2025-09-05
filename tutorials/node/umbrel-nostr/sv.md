---
name: Paraply Nostr
description: Konfigurera och använda Nostr-applikationer på Umbrel
---

![cover](assets/cover.webp)



## Förutsättningar: Installation av Umbrel



Umbrel är en plattform med öppen källkod som gör att du enkelt kan vara värd för Bitcoin-applikationer och andra tjänster på din egen personliga server. Det är en allt-i-ett-lösning som i hög grad förenklar självhosting av Bitcoin-noder och decentraliserade applikationer.



Se till att du har installerat Umbrel genom att följa vår installationsguide:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Introduktion till Nostr



**Nostr** är ett öppet, decentraliserat nätverksprotokoll utformat för sociala nätverk. Dess namn står för _"Notes and Other Stuff Transmitted by Relays"_. Det gör det möjligt för vem som helst att publicera meddelanden (anteckningar), som hanteras som JSON-händelser, och sprida dem via reläservrar snarare än en centraliserad plattform. Varje användare har ett par kryptografiska nycklar (privata/offentliga) som fungerar som en identifierare: den offentliga nyckeln (npub) identifierar användaren och den privata nyckeln (nsec) gör det möjligt att signera meddelanden. Tack vare denna distribuerade arkitektur erbjuder **Nostr censurresistens** och stor flexibilitet: du kan använda flera klienter och ansluta till så många reläer som du vill, utan att vara beroende av en enda server.



Nostr är kort sagt ett decentraliserat kommunikationsprotokoll där **klienter** (användarprogram) skickar och tar emot händelser via **relayers** (servrar). Detta protokoll har varit särskilt populärt bland Bitcoin-gruppen sedan 2023, på grund av dess värden decentralisering och datasuveränitet.



**Note:** För att använda Nostr behöver du din privata nyckel (genererad av en Nostr-klient eller via ett dedikerat tillägg). **Dela aldrig din privata nyckel**, eftersom det skulle göra det möjligt för någon att utge sig för att vara du. Förvara den på ett säkert ställe och använd säkra verktyg för nyckelhantering (se tips nedan).



## Umbrel-ansökningar för Nostr



Umbrel erbjuder ett ekosystem av integrerade applikationer för att dra full nytta av Nostr på din personliga nod. Vi kommer att beskriva användningen av de viktigaste Nostr-relaterade apparna: **Nostr Relay**, **noStrudel**, **Snort** och **Nostr Wallet Connect**. Var och en uppfyller ett specifikt behov: _Nostr Relay_ är en **privat reläserver**, _noStrudel_ och _Snort_ är **Nostr-klienter** (gränssnitt för att läsa/publicera anteckningar), medan _Nostr Wallet Connect_ är ett verktyg för att länka din **Lightning Wallet** till Nostr.



### Nostr Relay - Ditt privata relä på Umbrel



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



**Nostr Relay** är Umbrels officiella applikation för att köra ditt **egna Nostr-relä** på din nod. Huvudsyftet är att ha ett **privat** och pålitligt relä för att **backupera all din Nostr**-aktivitet i realtid. Med andra ord, genom att använda detta personliga relä i tillägg till de publika reläerna, säkerställer du att alla dina anteckningar, meddelanden och reaktioner kopieras hem, säkra från censur eller dataförlust.



**Installation:** Från Umbrel App Store (kategori _Social_), installera _Nostr Relay_. När applikationen har startats körs den i bakgrunden (docker service).



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)



Du ser dess Interface-webb via Umbrel: den innehåller grundläggande information och framför allt URL:en till ditt relä (uppe till höger), som du måste kopiera för vidare användning. En synkroniseringsknapp (jordglobsikon) finns också tillgänglig.



** För att dra nytta av ditt Umbrel-relä ..:



**Lägg till reläet i din Nostr-klient:** I din klientapplikation (t.ex. Damus på iOS, Amethyst på Android, Snort eller noStrudel på Umbrel, etc.), lägg till URL:en för ditt privata relä som du kopierade tidigare. Som standard lyssnar Umbrel-reläet på port **4848**. Om du kommer åt det i det lokala nätverket ger detta en URL som: `ws://umbrel.local:4848` (eller använd Umbrels lokala IP).



Om du använder Tailscale (se nedan) kan du till och med använda MagicDNS DNS alias (vanligtvis `umbrel` eller ett autogenererat namn) för att komma åt det från var som helst, alltid på port 4848.



Om du föredrar Tor, hämta din Umbrels .onion Address och använd den med port 4848 via en Tor-kompatibel webbläsare eller klient (se Tor-avsnittet)



När URL:en har lagts till i Nostr-klientens Relay-konfiguration, anslut till detta relä. Du bör se i din klient att Umbrel-reläet är anslutet (vanligtvis indikerat med en Green-punkt eller liknande).



**Synkronisera historik (valfritt)**: I Interface webben för _Nostr Relay_ på Umbrel, klicka på **globen** 🌐 ikonen (högst upp på sidan). Denna åtgärd kommer att tvinga ditt Umbrel-relä att ansluta till dina andra reläer (de som är konfigurerade i din klient) för att **importera dina gamla offentliga** aktiviteter. Detta innebär att tidigare anteckningar som du har publicerat eller läst via offentliga reläer också kommer att laddas ner och lagras på ditt privata relä. Vänligen vänta på att synkroniseringen ska ske.



**Använd Nostr som vanligt:** Från och med nu kommer alla nya aktiviteter (publicerade anteckningar, reaktioner, krypterade privata meddelanden etc.) som du utför på Nostr att vidarebefordras som vanligt till de offentliga reläerna **och parallellt till ditt Umbrel-relä**. Om din Nostr-klient är korrekt konfigurerad kommer den att skicka varje händelse till alla reläer (inklusive ditt). Ditt privata relä kommer att fungera som en realtidsbackup. Även i händelse av en tillfällig frånkoppling kommer dina kunder att kunna återsynkronisera saknade data senare tack vare detta relä. detta ger dig fullständig kontroll över dina Nostr-data



I bakgrunden finns Umbrels _Nostr Relay_ som är baserat på open-source-projektet **nostr-rs-relay** (Rust-protokollimplementering). Det stöder hela Nostr-protokollet och många standard-NIP (NIP-01, 02, 03, 09, 11, 12, 15, 16, 20, 22, 26, 28, 33, etc.), vilket garanterar maximal kompatibilitet med kunderna.



### noStrudel - Nostr-klient för upptäcktsresande



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



**noStrudel** är en kraftanvändarorienterad Nostr-webbklient, perfekt för att förstå och utforska Nostr-nätverket i detalj. Det är en slags sandlåda för att inspektera händelser och reläer och för att experimentera med protokollets avancerade funktioner. Interface är på engelska och relativt teknisk, vilket gör den idealisk för erfarna användare som är nyfikna på hur Nostr fungerar.



**Installation:** Installera _noStrudel_ från Umbrel App Store (kategori _Social_). När den har startats kan den nås via din webbläsare på din Umbrels Address (t.ex. `http://umbrel.local` eller via dess .onion/Tailscale, se avsnittet om extern åtkomst).



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**Konfigurera reläer:** När du öppnar noStrudel ser du en "Setup Relays"-knapp i det övre högra hörnet. Klicka på den för att konfigurera dina reläer.



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



På den här sidan klistrar du in webbadressen till ditt Umbrel-relä som du kopierade tidigare. Du kan också lägga till andra reläer som föreslås som standard av applikationen. När du har konfigurerat dina reläer klickar du på "Logga in" längst ner till vänster för att fortsätta.



![Options de connexion dans noStrudel](assets/fr/06.webp)



**Anslutning:** noStrudel erbjuder dig flera anslutningsalternativ. I vårt fall väljer vi "Private Key" och klistrar in din tidigare genererade Nostr privata nyckel. Om du ännu inte har någon nyckel kan du installera tillägget [Nostr Connect] (https://chromewebstore.google.com/detail/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj) för att skapa och/eller spara dina Nostr-nycklar och på så sätt kommunicera säkrare med de olika Nostr-applikationerna.



![Interface principale de noStrudel](assets/fr/07.webp)



När du är ansluten kan du använda noStrudel för att dela dina anteckningar via Nostr. Interface ger dig tillgång till :





- Komplett instrumentpanel för Nostr med tidslinje för anteckningar, notiser, meddelanden, profilsökning
- Relähantering och anslutningsstatus
- Avancerade verktyg för granskning av händelser och deras JSON-innehåll
- Konfigurationsalternativ för tidslinjefilter och PIN-koder



**Tips:** På _noStrudel_ kan du sätta upp _timeline filter_ eller testa olika _NIPs (Nostr Implementation Possibilities)_. Kontrollera t.ex. stöd för NIP-05 (decentraliserade identifierare) eller nyare funktioner. Detta gör _noStrudel_ till ett utmärkt verktyg för att experimentera i en kontrollerad miljö.



### Snort - Modern Nostr-kund på Umbrel



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort** är en annan Nostr-webbklient tillgänglig på Umbrel, som erbjuder en modern, snabb och snygg **Interface** för att interagera med det decentraliserade sociala nätverket. Till skillnad från noStrudel, som riktar sig till kraftanvändare, syftar _Snort_ till enkel användning utan att offra funktionalitet. Den är byggd i React och erbjuder ett snyggt UX som påminner om klassiska sociala nätverk, vilket gör den lämplig för daglig användning.



**Installation:** Installera _Snort_ från Umbrel App Store (kategori _Social_).



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



När du öppnar Snort ser du en "Registrera"-knapp i det nedre vänstra hörnet.



![Options de connexion dans Snort](assets/fr/10.webp)



Du kan välja att registrera dig eller ansluta till ett befintligt konto (vilket är vad vi kommer att göra i den här handledningen).



![Méthodes de connexion dans Snort](assets/fr/11.webp)



Snort erbjuder flera anslutningsmetoder. Du kan använda det tidigare installerade Nostr Connect-tillägget eller andra tillgängliga metoder. När du är ansluten kan du använda programmet till fullo.



Interface från _Snort_ erbjuder :





- En **Posts/Conversations/Global**-display för att navigera mellan dina anteckningar, trådade diskussioner eller det globala flödet
- Flikar för **Notifications**, **Messages** (DM), **Search**, **Profile**, etc.
- En **+**- eller _Write_-knapp för att publicera en ny anteckning
- Hantering av **prenumerationer (följande)** och **listor**
- Relähanteringsmeny för att lägga till/ta bort reläer och spåra deras tillgänglighet



**Rekommenderad reläkonfiguration:** För att lägga till ditt Umbrel-relä, gå till Inställningar - Reläer. Ange URL:en till ditt relä (`ws://umbrel:4848` eller annan URL beroende på din konfiguration) i Snorts lista över reläer. På så sätt kommer Snort att publicera dina anteckningar på ditt privata relä utöver de offentliga.



### Nostr Wallet Connect - Koppla din Lightning Wallet till Nostr



**Nostr Wallet Connect (NWC)** är en applikation som **ansluter din Umbrel (Lightning)**-nod till kompatibla Nostr-applikationer för att göra Lightning-betalningar (till exempel skicka _zaps_, dessa mikrobetalningar för att "gilla" innehåll). I denna handledning tittar vi på hur du ansluter noStrudel till din Lightning-nod för att göra betalningar direkt från Interface.



**Installation och konfiguration:**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



Installera _Nostr Wallet Connect_ från Alby-butiken på Umbrel.



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



I noStrudel klickar du på din profil i det övre högra hörnet och sedan på knappen "hantera".



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



Klicka på "Lightning" och sedan på "connect Wallet".



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



Bland de tillgängliga anslutningsalternativen väljer du "Umbrel".



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



Klicka på "Connect" för att automatiskt omdirigeras till din Umbrel Nostr Wallet Connect-session.



![Page de configuration des autorisations NWC](assets/fr/17.webp)



På Nostr Wallet Connect-sidan kan du :




   - Definiera din maximala budget
   - Validera behörigheter
   - Ange en utgångstid för anslutningen


Klicka på "connect" för att slutföra.



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



Du omdirigeras till noStrudel med ett bekräftelsemeddelande: du kan nu zappa hela världen från din Wallet/LND-nod!



Tack vare NWC startar dina **Lightning-betalningar via Nostr** (zappar för att belöna inlägg, _Value for Value_-betalningar, etc.) från **din egen nod**. Du behöver inte längre dirigera dina transaktioner genom externa tjänster eller skanna en QR från din telefon varje gång. Användarupplevelsen förbättras avsevärt, samtidigt som den förblir _icke-förvaltande_ och integritetsvänlig.



Om du vill veta hur du sätter upp din egen Lightning-nod på Umbrel rekommenderar jag att du kollar in den här andra omfattande handledningen:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Avancerad konfiguration och säkerhet



Att använda Umbrel och Nostr tillsammans på en avancerad nivå kräver särskild uppmärksamhet på **säkerhet** och **konnektivitet**. Här är några tips om hur du skyddar din konfiguration och får tillgång till den på bästa sätt, var du än befinner dig.



### Säker extern åtkomst: Tor och Tailscale



Av säkerhetsskäl är din Umbrel som standard endast tillgänglig i ditt lokala nätverk (och via Tor). För att interagera med Nostr utanför hemmet har du två föredragna lösningar: **Tor** (anonym åtkomst via löknätverk) och **Tailscale** (privat VPN-mesh).





- Åtkomst via Tor:** Umbrel konfigurerar automatiskt en **Tor-tjänst (.onion)** för sin Interface-webb och applikationer. Detta innebär att du kan komma åt Interface Umbrel (inklusive _noStrudel_ eller _Snort_) var som helst, med hjälp av Tor-webbläsaren, utan att exponera din offentliga IP. _Tor används för att komma åt dina Umbrel-tjänster från utanför ditt lokala nätverk, utan att exponera din enhet för Internet ([Installera Tor på ditt system - Guider - Umbrel Community](https://community.umbrel.com/t/setup-tor-on-your-system/7509#:~:text=Official%20website%3A%20https%3A%2F%2Fwww))._ För att använda detta alternativ, gå till Umbrel-inställningar och hämta din Umbrels .onion URL (eller skanna den QR-kod som tillhandahålls). I en Tor-webbläsare, gå till denna .onion Address: du får samma Interface som lokalt. Du kan sedan använda dina Nostr-appar precis som hemma.


**Nostr relä via Tor:** Om du vill att ditt Nostr relä ska vara nåbart via Tor för dina kunder (eller auktoriserade vänner) är detta möjligt. Umbrel tillhandahåller inte reläets .onion Address direkt, men eftersom det körs på port 4848 kan du antingen :





    - Använd UI Umbrels .onion Address och konfigurera din klient för att ansluta via denna Interface (opraktiskt för WebSocket),





    - Eller** exponera port 4848 som en separat löktjänst. Detta kräver att man pillar med Tor-konfigurationen på Umbrel (reserverat för avancerade användare som är bekväma med SSH). Alternativt kan du överväga en **Tor-tunnel** på en annan server som omdirigerar till Umbrel: för personligt bruk är det dock enklast att använda Tailscale.





- Åtkomst via Tailscale:** [Tailscale](https://tailscale.com/) är en mesh VPN-lösning som skapar ett virtuellt privat nätverk mellan dina enheter och Umbrel. Fördelen: det fungerar som om du var på ett LAN, men över Internet, krypterat och utan komplex konfiguration. **Tailscale tilldelar din Umbrel en fast IP och ett privat domännamn, oavsett var den befinner sig i nätverket ([Tailscale | Umbrel App Store](https://apps.umbrel.com/app/tailscale#:~:text=Tailscale%20is%20zero%20config%20VPN,reviewed%20and%20trusted%20standard))**. I praktiken, när du har installerat Tailscale på Umbrel (från Umbrel App Store, kategori _Networking_) **och** på dina enheter (mobil, PC ...), kommer du att kunna nå Umbrel via en Address som `100.x.y.z` (Tailscale IP) eller ett namn som `umbrel.tailnet123.ts.net`.


för Nostr_ är Tailscale extremt användbart: din mobil, om den har Tailscale aktiv, kommer att kunna ansluta till `ws://umbrel:4848` (tack vare MagicDNS) eller direkt till Tailscale IP och port 4848 för att använda reläet. Klienter som Damus eller Amethyst kommer att se din Umbrel som om den var på samma lokala nätverk. **Tips:** Aktivera alternativet **MagicDNS** i Tailscale för att använda värdnamnet `umbrel` istället för att memorera IP:n. Detta säkerställer en smidig anslutning till ditt relä även när du är på resande fot ([Nostr Relay | Umbrel App Store](https://apps.umbrel.com/app/nostr-relay#:~:text=client%20%28e,That%27s%20it%21%20Your%20past)).


Med Tailscale kan du dessutom komma åt Interface Umbrel (och därmed webbklienterna _noStrudel/Snort_) via en enkel webbläsare med hjälp av den privata IP-adressen eller det tilldelade domännamnet. Det finns inget behov av en Tor-webbläsare, och dataöverföringshastigheterna är i allmänhet bättre än via Tor-nätverket.




**Tor och Tailscale är inte ömsesidigt uteslutande. Du kan hålla Tor aktivt för anonymiserad åtkomst eller specifika tjänster, och använda Tailscale dagligen för dess enkelhet. I båda fallen behöver du inte öppna en port på din router, vilket stärker säkerheten.



### Säkra ditt Nostr-relä (rekommenderade metoder)



Om du är värd för ett Nostr-relä på Umbrel, särskilt i ett avancerat sammanhang, se till att tillämpa några goda metoder:





- Privat eller begränsat relä:** Som standard är ditt Umbrel-relä privat (inte offentligt tillkännagivet) och om du bara kommer åt det via Tailscale eller ditt LAN kommer det att förbli otillgängligt för främlingar. **Håll länken konfidentiell ** Sänd den inte på offentliga Nostr-nätverk om du inte frivilligt vill vara värd för andra användare, vilket är en helt annan fråga (moderering, bandbredd etc.). För personligt bruk rekommenderar vi att du begränsar åtkomsten till dig själv och, om det behövs, till några få betrodda vänner och familj.





- Vitlista / Auth**: Nostr-rs-relay-implementeringen stöder en **NIP-42** autentiseringsmekanism samt _vitlistor_ över publika nycklar. Genom att aktivera dessa alternativ kan du begränsa ditt relä så att det **bara accepterar händelser signerade av vissa nycklar (dina)**, eller att klienter måste autentisera sig för att publicera. att ställa in detta kräver redigering av reläets `config.toml`-konfigurationsfil i Umbrel (via SSH i Docker-containern)._ Det är en avancerad manipulation, men till exempel kan du lista de annonser som tillåts (`pubkey_whitelist`). På så sätt, även om någon upptäcker ditt relä, kommer de inte att kunna publicera något där om de inte finns på listan.





- Uppdateringar och underhåll:** Håll din Umbrel och _Nostr Relay_-appen uppdaterade. Uppdateringar kan innehålla prestandaförbättringar (t.ex. bättre skräpposthantering) och säkerhetsfixar. På Umbrel, kontrollera App Store regelbundet för uppdateringar till _Nostr Relay_, och tillämpa dem vid behov.





- Övervakning och begränsningar:** Håll ett öga på hur ditt relä används. Om du öppnar upp det för andra bör du hålla ett öga på belastningen (CPU/RAM-lagring) på din Umbrel, eftersom ett relä snabbt kan samla på sig mycket data. nostr-rs-relay erbjuder konfigurerbara **hastighets- och lagringsgränser** (`gränser` i konfigurationen, t.ex. antal händelser per sekund, max händelsestorlek, rensning av gamla händelser ...). För privat bruk behöver du förmodligen inte röra dessa, men var medveten om att dessa parametrar finns om du behöver dem ([nostr-rs-relay/config.toml at master - scsibug/nostr-rs-relay - GitHub](https://github.com/scsibug/nostr-rs-relay/blob/master/config.toml#:~:text=)).





- Säkra Nostr-nycklar:** Den här punkten har redan nämnts, men den är avgörande: ange aldrig dina privata Nostr-nycklar i en Interface som du inte litar helt på. Använd istället webbläsartillägg eller externa enheter (t.ex. Nostr _signers_ på separata telefoner) för att signera känsliga åtgärder. På Umbrel kan dina webbklienter som _Snort_ och _noStrudel_ fungera utan att känna till din hemliga nyckel, via NIP-07. Utnyttja denna möjlighet att kombinera komfort och säkerhet.




Genom att följa dessa tips kommer din integration av en Umbrel-nod med Nostr att vara både kraftfull **och** säker. Du kommer att ha en komplett miljö: en Bitcoin-nod för Lightning-betalningar, ett privat Nostr-relä för datasuveränitet och högpresterande Nostr-webbklienter för att navigera i detta nya decentraliserade sociala nätverk. Njut av att utforska Nostr med Umbrel!