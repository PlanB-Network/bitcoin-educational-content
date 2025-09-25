---
name: Tailscale
description: Avancerad handledning för Tailscale
---
![cover](assets/cover.webp)



## 1. Inledning



Tailscale är nästa generations VPN som skapar ett krypterat mesh-nätverk mellan dina enheter. Det låter dig ansluta fjärrmaskiner som om de vore i samma lokala nätverk, utan komplex konfiguration eller portöppning.



För självhosting tilldelar Tailscale varje enhet en fast privat IP i ett virtuellt nätverk, vilket ger stabil åtkomst till dina tjänster även när din publika IP ändras. Det innebär att du kan hantera dina servrar på distans utan att exponera dina tjänster direkt mot internet.



**Huvudsakliga tillämpningar:**




- Hantera en personlig server från utsidan
- Hantera Umbrel/Lightning-noder snabbare än Tor
- Säker åtkomst till en Raspberry Pi eller NAS
- Anslut till dina tjänster via SSH eller HTTP utan komplex nätverkskonfiguration



Detta enkla tillvägagångssätt gör det möjligt för självhanterare att komma åt sina tjänster på ett säkert sätt och undvika fallgroparna med traditionella VPN-tjänster.



## 2. Hur Tailscale fungerar



Till skillnad från traditionella VPN, som dirigerar all trafik genom en central server, skapar Tailscale ett mesh-nätverk där enheterna kommunicerar direkt med varandra. Den centrala servern hanterar endast autentisering och nyckeldistribution, utan att se användardata.



![VPN traditionnel (hub-and-spoke)](assets/fr/01.webp)


*Figur 1: Traditionellt VPN med hub-and-spoke-arkitektur där all trafik går via en central server*



Baserat på WireGuard genererar varje enhet sina egna kryptografiska nycklar. Koordinationsservern distribuerar de publika nycklarna till noderna, som sedan upprättar krypterade tunnlar direkt mellan varandra. För att ta sig igenom brandväggar använder Tailscale NAT-traversal och, som en sista utväg, DERP-reläer som upprätthåller kryptering.



![VPN maillé (mesh)](assets/fr/02.webp)


*Figur 2: Tailscale mesh-nätverk där enheter kommunicerar direkt med varandra*



All kommunikation är krypterad med WireGuard. Tailscale ser bara metadata (anslutningar) men aldrig innehållet i utbytena. För större suveränitet gör Headscale det möjligt för samordningsservern att vara självhostad.



**Säkerhet och sekretess:** Tack vare WireGuard är all kommunikation på Tailscale krypterad från början till slut. Tailscale kan inte läsa din trafik - endast dina enheter har de nödvändiga privata nycklarna. Tjänsten ser bara metadata: IP-adresser, enhetsnamn, tidsstämplar för anslutningar och peer-to-peer-anslutningsloggar (utan innehåll).



Denna arkitektur är dock beroende av Tailscale Inc. för nätverkskoordinering. För att eliminera detta beroende erbjuder Headscale ett alternativ med öppen källkod som gör att du själv kan vara värd för kontrollservern samtidigt som du använder de officiella Tailscale-klienterna, vilket garanterar fullständig suveränitet över din nätverksinfrastruktur, till priset av en mer teknisk konfiguration.



**För en detaljerad förklaring av Tailscales inre funktioner, inklusive kontrollplanshantering, NAT-traversering och DERP-reläer, rekommenderar vi den utmärkta artikeln [How Tailscale Works] (https://tailscale.com/blog/how-tailscale-works) på den officiella bloggen. Artikeln förklarar på djupet de tekniska begrepp som gör Tailscale så kraftfullt.**



## 3. Installera Tailscale



Tailscale körs på de **vanligaste** operativsystemen (Windows, macOS, Linux, iOS, Android). Installationen sägs vara "snabb och enkel" på alla plattformar. Låt oss börja med att ta en titt på Interface och hur man skapar ett konto, och sedan gå vidare till installationsprocedurerna för olika miljöer.



### 3.1 Skapande av konto i Tailscale



Gå till [https://tailscale.com/](https://tailscale.com/) och klicka på knappen "Get Started" längst upp till höger på sidan.




![Page d'accueil Tailscale](assets/fr/03.webp)


*Tailscale-hemsidan förklarar konceptet och erbjuder en gratis start*



För att använda Tailscale måste du först skapa ett konto via en identitetsleverantör:



![Page de connexion Tailscale](assets/fr/04.webp)


*Val av identitetsleverantör för anslutning till Tailscale (Google, Microsoft, GitHub, Apple etc.)*



När du har loggat in kommer Tailscale att be dig om lite information om din avsedda användning:



![Questionnaire d'utilisation](assets/fr/05.webp)


*Formulär för att bättre förstå ditt användningsfall (privat eller professionellt)*



När du har skapat ditt konto kan du installera Tailscale på dina enheter:



![Ajout du premier appareil](assets/fr/07.webp)


*Med Tailscale kan du installera applikationen på olika system*



### 3.2 Installation på olika plattformar





- På Windows och macOS: Ladda bara ner den grafiska applikationen från Tailscales officiella webbplats och installera den (.msi-fil på Windows, .dmg-fil på Mac). När applikationen har installerats startar en grafisk Interface som låter dig ansluta (via en webbläsare) till ditt Tailscale-konto för att autentisera maskinen.



![Connexion d'un appareil macOS](assets/fr/08.webp)


*Anslut en MacBook till bakluckan*



![Connexion réussie](assets/fr/09.webp)


*Bekräftelse på att enheten är ansluten till Tailscale*-nätverket





- På Linux (Debian, Ubuntu, etc.): Du har flera alternativ. Den enklaste metoden är att köra det officiella installationsskriptet: till exempel på Debian/Ubuntu:



```bash
curl -fsSL https://tailscale.com/install.sh | sh
```



Detta skript lägger till det officiella Tailscale-förvaret och installerar paketet. Du kan också [manuellt lägga till APT-förvaret](https://pkgs.tailscale.com) eller använda vanliga Snap- eller apt-paket. När det är installerat kommer daemon `tailscaled` att köras i bakgrunden. Du kommer då att behöva **autentisera noden** (se Interface CLI vs web nedan). På andra distributioner (Fedora, Arch ...) finns paketet också tillgängligt via standardförvar eller det universella installationsskriptet. För en huvudlös server, använd CLI: till exempel `sudo tailscale up --auth-key <key>` om du använder en förgenererad autentiseringsnyckel, eller helt enkelt `tailscale up` för en interaktiv inloggning (som kommer att ge en URL att besöka för att autentisera enheten).





- På ARM-baserade system (Raspberry Pi, etc.): Vi använder i allmänhet Linux, så samma tillvägagångssätt som ovan (skript eller paket). Observera att Tailscale stöder ARM32/ARM64-arkitektur utan problem. Många användare installerar Tailscale på Raspberry Pi OS via apt eller på lättviktsdistributioner (DietPi, etc.) för att komma åt sin Pi överallt.





- På iOS och Android: **Tailscale tillhandahåller officiella mobilapplikationer.** Installera bara *Tailscale* från [App Store] (https://apps.apple.com/us/app/tailscale/id1470499037?ls=1) (iOS) eller [Play Store] (https://play.google.com/store/apps/details?id=com.tailscale.ipn) (Android).



![Installation sur iPhone](assets/fr/11.webp)


*Steg för att installera Tailscale på iPhone: välkomst, integritet, meddelanden, VPN *



![Connexion sur iPhone](assets/fr/12.webp)


*Anslut till tailnet, välj konto och validera på iPhone*



När appen är installerad kommer den vid första lanseringen att be dig att autentisera dig via den valda leverantören (Google, Apple ID, Microsoft etc., beroende på vad du använder för Tailscale) - det är samma procedur som på andra plattformar, vanligtvis en omdirigering till en OAuth-webbsida. Därefter skapar mobilappen VPN (på iOS måste du acceptera tillägget för VPN-konfiguration). Appen kan sedan köras i bakgrunden, vilket ger dig tillgång till ditt tailnet var du än befinner dig. *Observera:* på mobilen kan du bara ha **ett aktivt VPN åt gången** - så se till att du inte har ett annat VPN anslutet samtidigt, annars kan Tailscale inte upprätta sitt eget. På Android kan du ställa in en separat arbetsprofil om du vill isolera vissa användningsområden (t.ex. en profil med Tailscale aktiv för en viss app).



### 3.3 Lägga till flera enheter och validering



När din första enhet är ansluten uppmanar Tailscale dig att lägga till andra enheter i ditt nätverk:



![Ajout d'appareils supplémentaires](assets/fr/10.webp)


*Interface visar den första enheten som är ansluten och väntar på andra enheter*



När du har lagt till flera enheter kan du kontrollera att de kan kommunicera med varandra:



![Test de connectivité entre appareils](assets/fr/13.webp)


*Bekräftelse på att enheterna kan kommunicera med varandra via ping*



Tailscale föreslår sedan ytterligare konfigurationer för att förbättra din upplevelse:



![Suggestions de configuration](assets/fr/14.webp)


*Förslag på hur du konfigurerar DNS, delar enheter och hanterar åtkomst*



### 3.4 Kontrollpanel för administration



Med webbadministrationskonsolen kan du visa och hantera alla dina anslutna enheter:



![Tableau de bord des machines](assets/fr/15.webp)


*Lista över anslutna enheter med deras egenskaper och status*



**Interface Web vs Interface CLI:** Tailscale erbjuder två kompletterande sätt att interagera med nätverket: **Interface webbadministration** och **kommandoradsklienten (CLI)**.





- **Interface Web (Admin Console)**: tillgänglig på [https://login.tailscale.com](https://login.tailscale.com), är denna webbkonsol den centrala instrumentpanelen för ditt Tailscale-nätverk. Den listar alla enheter (*Maskiner*), deras online-/offlinestatus, deras Tailscale-IP-adresser med mera. Här kan du **hantera enheter** (byta namn, utgångna nycklar, auktorisera rutter, inaktivera en nod), **hantera användare** (i ett organisatoriskt sammanhang) och definiera säkerhetsregler (ACL). Det är också här du konfigurerar globala alternativ som MagicDNS, taggar eller auth-nycklar (auth-nycklar före generate för automatiserat tillägg av enheter). Interface web är mycket praktiskt för att få en överblick och tillämpa ändringar som kommer att spridas via samordningsservern till alla noder. *Exempel:* Aktivering av en **subnet route** eller en **exit node** görs med ett enda klick i konsolen, när noden i fråga har meddelat sig själv som sådan.





- **Interface kommandorad (CLI):** Kommandot `tailscale` är tillgängligt i CLI på alla enheter där Tailscale är installerat. Med denna CLI kan du göra allt lokalt: ansluta (`tailscale up`), inspektera status (`tailscale status` för att se vilka peers som är anslutna), felsöka (`tailscale ping <ip>`) och så vidare. Vissa funktioner är till och med **exklusiva för CLI** eller mer avancerade, till exempel:





  - `tailscale up --advertise-routes=192.168.0.0/24` för att annonsera en subnätväg,
  - `tailscale up --advertise-exit-node` för att föreslå din maskin som en exit-nod,
  - `tailscale set --accept-routes=true` (eller `--exit-node=<IP>`) för att konsumera en rutt eller använda en utgångsnod,
  - `tailscale ip -4` för att visa enhetens Tailscale IP,
  - `tailcale lock/unlock` (om du använder *tailnet-lock*, avancerad säkerhetsfunktion),
  - eller `tailscale file send <node>` för att använda **Taildrop** (filöverföring mellan enheter).


CLI är mycket användbart på servrar utan Interface-grafik och för skriptning av vissa åtgärder. **Skillnader i användning:** De flesta grundläggande konfigurationer kan göras antingen via webben eller via CLI. Att lägga till en enhet görs till exempel antingen genom en uppmaning via konsolen eller genom att köra `tailscale up` på enheten och validera via webben. På samma sätt kan man byta namn på en enhet via konsolen eller med `tailscale set --hostname`. **Sammanfattningsvis** är webbkonsolen idealisk för global nätverksadministration (särskilt med flera maskiner/användare), medan CLI är praktiskt för finkornig kontroll över en viss maskin, automatiseringsskript eller användning på ett system utan GUI.



## 4. Använda Tailscale på Umbrel



Umbrel är en populär plattform för självhosting (används särskilt för Bitcoin/Lightning-noder och andra självhosting-tjänster, via dess App Store). För att installera och konfigurera Umbrel rekommenderar vi att du följer vår dedikerade handledning:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Att använda Umbrel och Tailscale tillsammans är ett särskilt intressant användningsfall, eftersom Umbrel integrerar en Tailscale-modul som är lätt att distribuera. Här är hur Tailscale integreras med Umbrel och vad det ger:



### 4.1 Installation och konfiguration av paraplyet





- **Installera Tailscale på Umbrel:** Umbrel har en officiell Tailscale-applikation i sin App Store. Installationen kunde inte vara enklare:



![Interface Umbrel avec l'application Tailscale](assets/fr/16.webp)


*Applikationssida för Tailscale i Umbrel App Store*



Från Interface Web Umbrel, öppna App Store, sök efter **Tailscale** och klicka på *Install*. Några sekunder senare är applikationen installerad på Umbrel. När du öppnar den visar Umbrel en sida där du kan länka din nod till Tailscale.



![Écran de login Tailscale dans Umbrel](assets/fr/17.webp)


*Tailscale anslutningsskärm i Umbrels Interface*



Klicka bara på **"Logga in"**, som kommer att omdirigera dig till Tailscale-autentiseringssidan:



![Page d'authentification Tailscale](assets/fr/18.webp)


*Anslut till Tailscale via en identitetsleverantör*



Du kan autentisera dig via ditt Tailscale-konto (Google/GitHub/etc.) eller ange din e-postadress. På Umbrel ber Interface dig vanligtvis att besöka [https://login.tailscale.com](https://login.tailscale.com) och logga in - detta autentiserar Umbrel Tailscale-appen.



![Confirmation de connexion réussie](assets/fr/19.webp)


*Bekräftelse på att Umbrel-enheten är ansluten till Tailscale-nätverket*



När du har gjort det är din Umbrel "i" ditt Tailscale-nätverk och visas på din konsol med ett namn (t.ex. *umbrel*). Du kan sedan klicka på IP Address på dina enheter för att kopiera den, hämta IPv6 Address eller din MagicDNS som är associerad med din enhet.



![Console Tailscale avec appareils connectés](assets/fr/20.webp)


*Tailscales administrationskonsol visar flera anslutna enheter, inklusive Umbrel*




### 4.2 Fjärråtkomst till Umbrel-tjänster



När Umbrel är ansluten till Tailscale kan du komma åt Interface Umbrel och de applikationer som körs på den, var du än befinner dig, som om du vore på det lokala nätverket. Detta är en av de största fördelarna jämfört med Tor.



Åtkomst är anmärkningsvärt enkelt: istället för att använda `umbrel.local` (som bara fungerar på ditt lokala nätverk), använder du din Umbrel's Tailscale IP Address (`http://100.x.y.z`) direkt från vilken enhet som helst som är ansluten till ditt tailnet. Detta fungerar oavsett var du befinner dig eller vilken internetanslutning du använder (4G, offentligt Wi-Fi, företagsnätverk).



**Exempel på Umbrel-hostade applikationer som är tillgängliga via Tailscale:**





- **Interface huvud Umbrel**: Få tillgång till din Umbrel-instrumentpanel genom att helt enkelt skriva `http://100.x.y.z` i din webbläsare
- **Bitcoin-nod**: Hantera din Bitcoin-nod utan fördröjning, visa synkronisering och statistik
- **Lightning-nod**: Använd ThunderHub, RTL eller andra Lightning-hanteringsgränssnitt med omedelbar respons
- **Mempool**: Visa Bitcoin-transaktioner och Mempool utan Tor-fördröjningar
- **ingenStrudel**: Få tillgång till dina Nostr-tjänster som finns på Umbrel



** Anslut externa plånböcker till dina Bitcoin- eller blixtnoder via Tailscale:**



Tailscale gör det också möjligt för dina Bitcoin- och Lightning-plånböcker installerade på andra enheter att ansluta direkt till din Umbrel-nod:





- **Sparrow wallet (Bitcoin)**: Denna externa Wallet Bitcoin kan ansluta direkt till din Umbrel's Electrum-server med hjälp av Tailscale IP Address:



![Configuration Electrum dans Sparrow](assets/fr/21.webp)


*Konfigurera en privat Electrum-server i Sparrow wallet med hjälp av Umbrels Tailscale IP Address*



![Liste des serveurs Electrum dans Sparrow](assets/fr/22.webp)


*Lista över Electrum-serveralias i Sparrow med Umbrel Tailscale IP Address*



Läs vår kompletta guide till hur du konfigurerar Sparrow wallet med din Bitcoin-nod:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d




- **Zeus (Blixt)**: Denna Wallet mobila Lightning kan ansluta till din Lightning-nod på Umbrel. Istället för att konfigurera slutpunkten som `.onion', ställ helt enkelt in Tailscale IP för din Umbrel och Lightning API-porten. Anslutningen kommer att vara omedelbar jämfört med Tor.



![Configuration Zeus avec IP Tailscale](assets/fr/23.webp)


*Konfigurera Zeus för att ansluta till Lightning-noden via Tailscale* IP Address



För att konfigurera Zeus med din Lightning-nod, se vår detaljerade handledning:



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

För att ta reda på mer om Lightning Network och hur den fungerar på Umbrel, besök:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16



### 4.3 Fördelar jämfört med Tor



Umbrel erbjuder fjärråtkomst via Tor (genom att tillhandahålla `.onion`-adresser för sina webbtjänster). Även om Tor har fördelen med konfidentialitet (anonymitet) och inte kräver någon registrering, tycker många användare att **Tor är långsamt och instabilt** för daglig användning (sidor laddas långsamt, timeouts, etc.) - *"Umbrel via Tor är så långsamt"* klagar vissa.



Tailscale erbjuder en generellt **snabbare anslutning med låg latens**, eftersom trafiken passerar direkt (eller via ett snabbt relä) istället för att studsa genom 3 Tor-noder. Dessutom ger Tailscale en upplevelse av ett "lokalt nätverk": privata IP-adresser används och applikationer kan mappas direkt (t.ex. SMB-nätverksenhet på \100.x.y.z).



Med detta sagt har Tor fördelen av att vara decentraliserad och "out of the box" på Umbrel, medan Tailscale innebär att man måste lita på en tredje part (eller vara värd för headscale). Tor är också användbart för klientlös åtkomst (från vilken Tor-webbläsare som helst kan du konsultera Umbrel-gränssnittet, medan Tailscale kräver att klienten installeras på åtkomstenheten).



**Sammanfattningsvis**, för interaktiv användning (Lightning wallets, frekventa webbgränssnitt) erbjuder Tailscale märkbar komfort och hastighet jämfört med Tor, till priset av ett litet externt beroende. Många väljer att använda *båda*: Tailscale i vardagen och Tor som en reservlösning eller för att dela åtkomst med någon utan att bjuda in dem till sitt VPN.



### 4.4 Säkerhet



Genom att använda Tailscale med Umbrel undviker du att exponera Umbrel mot Internet. Umbrel-noden är endast tillgänglig för dina andra autentiserade enheter i tailnet, vilket avsevärt minskar attackytan (ingen port öppen för främlingar, ingen risk för attack på webbtjänsten via Internet).



Kommunikationen är krypterad (WireGuard) utöver den kryptering som dina tjänster redan gör (t.ex. även intern HTTP i tunneln). Du kan fortfarande tillämpa Tailscale ACL:er för att t.ex. förhindra att en viss tailnet-enhet får åtkomst till Umbrel om du vill partitionera nätverket. Umbrel själv ser inte skillnaden - den tror att den serverar lokalt.



---

För att avsluta detta avsnitt, att integrera Tailscale på Umbrel tar bara några få klick och **förbättrar tillgängligheten** för din självhostade nod avsevärt. Du kommer att kunna administrera Umbrel och dess tjänster från var som helst, säkert och effektivt, precis som om du var hemma. Detta är en särskilt användbar lösning för realtidsapplikationer (Lightning) som lider av Tor-latens, eller mer allmänt för alla självhostare som letar efter en enkel privat anslutning. Allt utan att exponera en enda port på din box, och utan komplicerad nätverkskonfiguration.



## 5. Avancerad hantering och användningsområden



### 5.1 Tailscale avancerade funktioner



**Nätverkshantering:** Med administrationskonsolen (login.tailscale.com) kan du hantera dina enheter, visa anslutningar och konfigurera åtkomstregler.



**MagicDNS:** Löser automatiskt enhetsnamn (t.ex. `raspberrypi.tailnet.ts.net`) för att undvika att memorera IP-adresser.



**ACL och åtkomstkontroll:** Definiera exakt vem som kan komma åt vad i ditt nätverk via JSON-regler, perfekt för att isolera vissa enheter eller begränsa åtkomsten till specifika tjänster.



**Med Device Sharing kan du bjuda in någon att komma åt en specifik maskin utan att ge dem tillgång till hela nätverket.**



**Subnet Router:** En Tailscale-maskin kan fungera som en gateway för ett helt subnät, vilket möjliggör åtkomst till icke-Tailscale-enheter (IoT, skrivare etc.) via en enda konfigurerad maskin.



**Exit Node:** Använd en maskin som en Internet-gateway för att avsluta med dess IP. Användbart för offentligt Wi-Fi eller för att kringgå geografiska begränsningar.



**Taildrop:** Ett säkert alternativ till AirDrop, som låter dig överföra filer mellan dina Tailscale-enheter, oavsett plattform eller plats. Till skillnad från AirDrop, som är begränsat till Apples ekosystem och fysisk närhet, fungerar Taildrop mellan alla dina enheter (Windows, Mac, Linux, Android, iOS), även om de befinner sig i olika länder. Filer överförs direkt mellan enheterna med end-to-end-kryptering, utan att passera en central server. Använd kommandoraden `tailscale file cp` eller den grafiska applikationen Interface beroende på ditt system.



### 5.2 Jämförelse med andra lösningar



**Vs OpenVPN:** Tailscale är mycket enklare att konfigurera (inga portar att öppna, ingen certifikathantering) men innebär beroende av en tredjepartstjänst. OpenVPN är fullt kontrollerbart, men kräver mer expertis.



**Som en direkt konkurrent arbetar ZeroTier på Layer 2 (Ethernet), vilket möjliggör broadcast/multicast, medan Tailscale arbetar på Layer 3 (IP). ZeroTier erbjuder större flexibilitet i nätverket, medan Tailscale föredrar enkelhet i användningen.**



**Vs Tor:** Tor erbjuder anonymitet som Tailscale inte gör, men är mycket långsammare. Tor är decentraliserat och kräver inget konto, medan Tailscale är snabbare och erbjuder en LAN-liknande upplevelse.



**Vs WireGuard manual:** Tailscale automatiserar all nyckel- och anslutningshantering som WireGuard raw kräver att du hanterar manuellt. Det är i huvudsak WireGuard + en förenklad hantering Layer.



Sammanfattningsvis positionerar sig Tailscale som en modern, enkelhetsorienterad lösning som är idealisk för personligt bruk och små team. För purister som vill ha total kontroll erbjuder Headscale ett alternativ för självhosting.



## 6. Slutsats



**Tailscale fördelar:** Tailscale erbjuder flera fördelar för självhosting:





- **Enkelhet och prestanda** - Snabb installation på alla plattformar utan komplicerad nätverkskonfiguration. Trafiken följer den mest direkta vägen mellan dina maskiner (P2P mesh), med WireGuard-protokollets prestanda och ingen central server som begränsar genomströmningen.
- **Säkerhet och flexibilitet** - End-to-end-kryptering, minskad attackyta och avancerade funktioner (ACL, SSO/MFA-autentisering). Fungerar även bakom NAT eller på resande fot, med subnet-routrar och exit-noder för att anpassa nätverket till dina behov.



**Begränsningar:** Tänk också på:





- **Externt beroende** - I standardversionen är tjänsten beroende av Tailscale Inc:s infrastruktur. Detta beroende kan kringgås via Headscale (alternativ med egen hosting).
- **Övriga begränsningar** - Delvis sluten källkod, begränsningar i gratisversionen för vissa avancerade användningsområden, inget stöd för Layer 2 (broadcast/multicast) och behov av internetåtkomst för att upprätta anslutningar.



**Tailscale är idealisk för enskilda värdar och små team, utvecklare som behöver tillgång till spridda resurser, VPN-nybörjare och mobila användare. För företag som kräver total kontroll kan andra lösningar som Headscale eller WireGuard direkt vara att föredra.**



**Utforska Headscale för fullständig självhosting, API- och DevOps-integrationer (Terraform), eller alternativ som Innernet (liknande men helt självhostad) och Netmaker.**



Tailscale är ett viktigt verktyg för självhosting tack vare sin enkelhet och effektivitet, vilket gör din privata infrastruktur lika tillgänglig som om den vore i molnet, samtidigt som du behåller kontrollen hemma.



## 7. Användbara resurser



### Officiell dokumentation





- **Tailscale Dokumentationscenter**: [docs.tailscale.com](https://docs.tailscale.com) - Fullständig engelsk dokumentation, installationsguider, handledning och tekniska referenser.
- **Hur Tailscale fungerar**: [Hur Tailscale fungerar](https://tailscale.com/blog/how-tailscale-works) - Detaljerad artikel som förklarar det inre arbetet i Tailscale.
- **Changelog**: [tailscale.com/changelog](https://tailscale.com/changelog) - Spårning av uppdateringar och nya funktioner.



### Praktiska guider





- **Homelab** handledning: [tailscale.com/kb/1310/homelab](https://tailscale.com/kb/1310/homelab) - Specifika guider för självhosting.
- **Konfigurera en Exit Node**: [tailscale.com/kb/1103/exit-nodes](https://tailscale.com/kb/1103/exit-nodes) - Detaljerad guide till konfiguration av Exit-noder.
- Använd **Taildrop**: [tailscale.com/kb/1106/taildrop](https://tailscale.com/kb/1106/taildrop) - Överför filer mellan Tailscale-enheter.



### Jämförelser





- **Tailscale vs. andra lösningar**: [tailscale.com/compare](https://tailscale.com/compare) - Detaljerade jämförelser med andra VPN- och nätverkslösningar (ZeroTier, OpenVPN, etc.).



### Gemenskap





- **Reddit**: [r/Tailscale](https://www.reddit.com/r/tailscale/) - Diskussioner, frågor och feedback.
- **GitHub**: [github.com/tailscale/tailscale](https://github.com/tailscale/tailscale) - Kundens källkod, där man kan följa utvecklingen och rapportera problem.
- **Discord**: [discord.gg/tailscale](https://discord.gg/tailscale) - Gemenskap för användare och utvecklare.



Tailscale tillhandahåller regelbundet nytt innehåll och nya funktioner. Kolla in deras [officiella blogg] (https://tailscale.com/blog/) för de senaste nyheterna och fallstudierna.