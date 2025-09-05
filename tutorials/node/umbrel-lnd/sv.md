---
name: Paraply LND
description: Avancerad handledning om installation och konfiguration av Lightning Network Daemon (LND) på Umbrel
---
![cover](assets/cover.webp)




## Inledning



Denna avancerade handledning tar dig steg för steg genom installation, konfiguration och användning av Lightning Node (LND)-applikationen på din Umbrel-nod. Du får lära dig hur du öppnar kanaler, hanterar din likviditet och synkroniserar din nod med en mobilapplikation.



## 1. Förutsättning: fungerande Bitcoin Umbrel-nod



Innan du distribuerar Lightning måste du ha en fullt fungerande Bitcoin-nod på Umbrel. Detta innebär att du installerar Umbrel (på Raspberry Pi, NAS eller annan maskin) och synkroniserar Blockchain Bitcoin fullt ut.



För att installera Umbrel och konfigurera din Bitcoin-nod rekommenderar vi att du följer vår dedikerade handledning :



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Se till att din Bitcoin-nod är uppdaterad och fungerar korrekt, eftersom Lightning Network förlitar sig på den för alla off-chain-transaktioner.



## 2. Introduktion till Lightning Network



Lightning Network är ett andra Layer-protokoll som är utformat för att påskynda och minska kostnaden för Bitcoin-transaktioner genom att utföra dem utanför huvud-Blockchain.



Konkret använder Lightning ett nätverk av betalningskanaler mellan noder: två användare öppnar en kanal genom att blockera On-Chain BTC (initial transaktion), och kan sedan omedelbart göra Exchange-betalningar inom denna kanal. Dessa off-chain-transaktioner registreras inte på Blockchain, därav deras hastighet och praktiskt taget nollkostnad.



Betalningar kan dirigeras genom flera kanaler (tack vare mellanliggande noder) för att nå alla mottagare i nätverket, vilket möjliggör en nästan obegränsad skala av omedelbara transaktioner. Lightning erbjuder därmed mycket snabba transaktioner till låg kostnad, perfekt för vardagliga betalningar eller mikrotransaktioner, samtidigt som belastningen på Blockchain Bitcoin minskar.



För att fungera måste en Lightning-nod vara permanent ansluten till nätverket och interagera med andra Lightning-noder. Det finns olika programvaruimplementeringar (LND, Core Lightning, Eclair, etc.), som alla är kompatibla med varandra. Umbrel använder LND (Lightning Network Daemon) som en del av sin officiella Lightning Node-applikation. Denna handledning fokuserar på LND.



För en fullständig teoretisk introduktion till Lightning Network rekommenderar vi att du går vår dedikerade kurs :



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Den här kursen ger dig en grundlig genomgång av de grundläggande begreppen i Lightning Network, innan du går vidare till att öva med din LND-nod.



## 3. Varför självhosta LND?



Att driva din egen Lightning-nod (LND) på Umbrel ger dig total suveränitet över dina medel och kanaler, jämfört med förvaringslösningar eller halvförvaringslösningar.



### Jämförelse av blixtlösningar :



**Solutions custodiales (t.ex. Wallet av Satoshi)** :




- Dina Lightning bitcoins hanteras av en betrodd tredje part
- Enkel att använda, ingen teknisk komplexitet
- Operatören har dina pengar och kan spåra dina transaktioner
- Du offrar kontroll och integritet



**Plånböcker för konsumenter av andra varor än råvaror (t.ex. Phoenix, Breez)** :




- Användare behåller sina privata nycklar och därmed Ownership av sin BTC
- Ingen fullständig nodhantering - applikationen hanterar kanaler i bakgrunden
- Kompromiss mellan enkelhet och suveränitet
- Beroende av leverantörsinfrastruktur för likviditet
- Tekniska begränsningar (en smartphone kan inte förmedla betalningar för andra)



**Självhanterad LND-nod (Umbrel)** :




- Maximal suveränitet: dina On-Chain och off-chain BTC:er är helt under din kontroll
- Ingen tredje part är inblandad i att öppna kanaler eller hantera dina betalningar
- Ökad integritet (dina kanaler och transaktioner är endast kända av dig och dina direkta kollegor)
- Användarfrihet: anslut till dina egna tjänster och plånböcker
- Möjlighet att dirigera transaktioner för andra (mikroavgiftsersättning)
- Ökat tekniskt ansvar (underhåll, likviditetshantering, säkerhetskopiering)



Kort sagt ger LND med självhosting dig maximal kontroll, men kräver mer teknisk skicklighet. Det är en avvägning mellan bekvämlighet och suveränitet.



## 4. Steg-för-steg-handledning



### 4.1 Installera och konfigurera Lightning Node-applikationen på Umbrel



När din Umbrel-nod (Bitcoin) har synkroniserats följer du dessa steg :



![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)



Installera Lightning Node-applikationen från avsnittet "App Store" i Interface Umbrel.



![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)



LND (Lightning Network Daemon) kommer att distribueras på din Umbrel som en applikation. När du först öppnar den kommer du att se ett varningsmeddelande som informerar dig om att Lightning är en experimentell teknik.



![Création ou restauration d'un nœud LND](assets/fr/03.webp)



Du kan välja mellan att skapa en ny nod eller att återställa en nod från en säkerhetskopia/seed. För en förstagångsinstallation väljer du att skapa en ny nod. Lightning Node-appen kommer att generate en 24 ord Mnemonic fras (din seed Lightning): skriv ner den mycket noggrant (helst offline, på papper), eftersom den kommer att användas för att återställa dina Lightning-fonder vid behov.



**Note: På de senaste versionerna av Umbrel ger installationen av Lightning-appen detta 24 ord seed (själva Umbrel-noden Bitcoin gör det inte).



![Interface principale de Lightning Node](assets/fr/04.webp)



Efter initialiseringen kommer du åt Lightning Node's huvud-Interface.



![Paramètres de l'application](assets/fr/05.webp)



I programinställningarna hittar du ett antal viktiga alternativ:




   - Ange ditt Node ID (din nods unika identifierare)
   - Ansluta en extern Wallet (Ansluta Wallet)
   - Visa hemliga ord
   - Åtkomst till avancerade inställningar
   - Återställ kanaler
   - Ladda ner kanalens backup-fil
   - Aktivera automatiska säkerhetskopior
   - Konfigurera säkerhetskopiering via Tor (Backup over Tor)



Dessa alternativ är viktiga för säkerheten och hanteringen av din Lightning-nod. Se till att du aktiverar automatiska säkerhetskopior och håller dina hemliga ord säkra.



**Användbara resurser:**




- [Umbrel Community](https://community.umbrel.com) - Diskussionsforum för användare som vill dela med sig av problem och lösningar som rör Umbrel och dess ekosystem


> - [Umbrel App Store - Lightning Node (LND)](https://apps.umbrel.com/app/lightning) - Beskrivning av Lightning Node-appens funktioner på Umbrel
> - [LND Docs - Quickstart](https://docs.lightning.engineering/lightning-network-tools/LND/run-LND) - Officiell dokumentation för LND

### 4.2 Öppna en Lightning-kanal



När LND är igång kan du öppna din första Lightning-kanal. För att hitta kvalitetsnoder att ansluta till:



![Page d'accueil Amboss.space](assets/fr/06.webp)



[Amboss.space](https://amboss.space/) är en utforskare som hittar pålitliga noder för att öppna kanaler.



![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)



Till exempel är [ACINQ-noden] (https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f) en erkänd nod med utmärkt tillgänglighets- och likviditetsstatistik.



![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)



För denna handledning öppnar vi en kanal med [Swiss Bitcoin Pay] (https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca). Informationen som krävs för anslutning (pubkey@ip:port) ges på deras Amboss sida.



För att öppna kanalen :



![Bouton d'ouverture de canal](assets/fr/09.webp)



På startsidan för Lightning Node klickar du på knappen "+ OPEN CHANNEL"



![Configuration du canal](assets/fr/10.webp)



På sidan för kanalkonfiguration :




   - Klistra in nod-ID:t som kopierats från Amboss (format: pubkey@ip:port)
   - Definiera mängden kanalkapacitet (vissa noder som ACINQ har minimikrav, t.ex. 400k Sats)
   - Justera öppningstransaktionsavgifter vid behov



![Canal en cours d'ouverture](assets/fr/11.webp)



När transaktionen har skickats kommer kanalen att visas som "öppning" på startsidan. Vänta på bekräftelse av On-Chain transaktionen.



![Détails du canal](assets/fr/12.webp)



Klicka på kanalen för att visa detaljer:




   - Nuvarande status
   - Total kapacitet
   - Fördelning av likvida medel (inkommande/utgående)
   - Fjärrnodens publika nyckel
   - Och annan teknisk information



### Använda Lightning Network+ för att erhålla inkommande likviditet



![Lightning Network+ dans l'App Store](assets/fr/13.webp)



Lightning Network+ finns tillgängligt i Umbrel App Store för att göra det enklare att få inkommande kontanter.



![Interface principale de LN+](assets/fr/14.webp)



Den huvudsakliga Interface erbjuder tre viktiga alternativ:




- "Likviditetsswappar: utforska de tillgängliga swap-erbjudandena
- "Open For Me": filtrera de swappar som du är berättigad till
- "To Docs": tillgång till dokumentation



![Message d'erreur LN+](assets/fr/15.webp)



Obs: Om du inte har någon kanal öppen ännu visas detta felmeddelande när du klickar på "Open For Me".



![Liste des swaps disponibles](assets/fr/16.webp)



På sidan "Liquidity Swaps" visas alla swap-erbjudanden som finns tillgängliga i nätverket.



![Swaps éligibles](assets/fr/17.webp)



"Open For Me" filtrerar endast de swappar för vilka din nod uppfyller de nödvändiga villkoren.



![Détails d'un swap](assets/fr/18.webp)



Exempel på swap-detaljer :




- Pentagonkonfiguration (5 deltagare)
- Kapacitet på 300k Sats per kanal
- Förutsättning: minst 10 öppna kanaler med 1M Sats total kapacitet
- Tillgängliga platser: 4/5



### 4.3 Synkronisering med en mobilapplikation (Zeus)



För att fjärrstyra din Lightning-nod (smartphone) kan du använda Zeus (applikation med öppen källkod som finns tillgänglig på iOS/Android).



**Zeus konfiguration med Umbrel :**



![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)



Se till att din Umbrel-nod är tillgänglig (som standard via Tor).


Öppna appen Lightning Node i Interface Umbrel och klicka sedan på knappen "Connect Wallet" som indikeras av pilen.



![Page de connexion avec QR code](assets/fr/20.webp)



En QR-kod visas som innehåller dina LND-åtkomstdata i lndconnect-format. Den här QR-koden är särskilt informationsrik, så tveka inte att förstora den för att underlätta läsningen.



![Configuration initiale de Zeus](assets/fr/21.webp)



På din telefon :




   - Öppna Zeus
   - På startsidan klickar du på "Advanced setup" för att ansluta din egen Lightning-nod
   - I parametrarna väljer du "Skapa eller anslut en Wallet"



![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)



I Zeus:




   - Välj "LND (REST)" som anslutningstyp
   - Du kan antingen skanna QR-koden (rekommenderad metod) eller mata in informationen manuellt. (Tveka inte att zooma in på Umbrel QR-koden, eftersom den är mycket tät)
   - Viktigt: aktivera alternativet "Använd Tor" om din Umbrel endast är tillgänglig via Tor (standard)
   - Spara konfiguration



Din Zeus är nu ansluten till din Umbrel-nod och låter dig göra Lightning-betalningar, se dina kanaler, saldon etc., samtidigt som du förblir helt självhanterad.



**Avancerade anslutningsalternativ: **



Som standard sker Zeus ↔ Umbrel-anslutningen via Tor. För en snabbare anslutning finns det två alternativ:



**Lightning Node Connect (LNC)** :




   - Lightning Labs mekanism för krypterad anslutning
   - Installera Lightning Terminal-appen på Umbrel (inkluderar LNC åtkomst)
   - generate en anslutning QR-kod i Lightning Terminal (Connect → Connect Zeus via LNC)
   - Skanna in den i Zeus (välj "LNC" som anslutningstyp)



**VPN Tailscale**:




   - Lätt att konfigurera mesh VPN
   - Installera Tailscale på Umbrel (App Store) och på din mobiltelefon
   - Anslut Zeus via Tailscales privata IP istället för Tor Address



Dessa alternativ är inte obligatoriska, och Tor + Zeus-lösningen fungerar bra i de flesta fall.



> **Användbara resurser:**
> - [Zeus Documentation - Umbrel Connection](https://community.umbrel.com/t/zeus-LN-mobile/7619) - Officiell guide för att ansluta Zeus till Umbrel
> - [Zeus GitHub](https://github.com/ZeusLN/zeus) - Zeus-projektet med öppen källkod
> - [Umbrel Community - Ansluta Zeus via Tailscale](https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - Guide för att ansluta Zeus till Umbrel med hjälp av Tailscale

## 5. Säkerhet och bästa praxis



Hantering av en självhostad Lightning-nod kräver särskild uppmärksamhet på säkerheten.



### Backup och säkerhet för din nod



**Viktiga typer av säkerhetskopior**



Din Lightning Umbrel-nod kräver två typer av säkerhetskopior:



**seed-meningen (24 ord)**




- Återvinner On-Chain-medel
- Nödvändigt för att återskapa din Wallet Lightning
- För extremt säker lagring (offline, på papper)



**Fil för säkerhetskopiering av statisk kanal (SCB)**




- Innehåller information om Lightning-kanalen
- Möjliggör tvingad stängning av kanalen i händelse av en krasch
- Viktigt:** Spara aldrig filen `channel.db` manuellt (risk för påföljder)



**Manuellt förfarande för säkerhetskopiering



Spara dina kanaler manuellt :


1. Öppna Lightning Node-menyn (tre prickar "⋮" bredvid "+ Öppna kanal")


2. Ladda ner kanalens backup-fil


3. Exportera en ny SCB efter varje kanalmodifiering


4. Förvara SCB på ett säkert sätt (krypterad media, kopia på annan plats)



**Umbärligt** automatiskt reservsystem



Umbrel har ett sofistikerat automatiskt backup-system som säkerställer :



*Dataskydd:*




- Kryptering på klientsidan före överföring
- Sändning via Tor-nätverket
- Data kompletterade med slumpmässig fyllning
- Krypteringsnyckel som är unik för din enhet



*Förbättrad säkerhet:*




- Omedelbar säkerhetskopiering vid statusändringar
- Säkerhetskopiering "på låtsas" med slumpmässiga intervall
- Dölj ändringar i säkerhetskopians storlek
- Skydd mot tidsanalys



*Restaureringsprocess:*




- Identifierare och nyckel härledd från din seed Umbrel
- Komplett restaurering möjlig endast med Mnemonic-fras
- Automatisk återställning av senaste säkerhetskopior
- Återställ kanalinställningar och data



### Restaurering av krockar



Om din nod går förlorad (hårdvarufel, skadat SD-kort) :




- Sätt tillbaka paraplyet
- Skriv in din 24 ord långa seed i Lightning-appen
- Importera filen SCB under restaurering



LND kommer att kontakta varje partner i dina gamla kanaler för att stänga dem och återkräva din andel av On-Chain-medel. Kanalerna kommer att stängas permanent (för att öppnas igen vid behov).



### Tillgänglighet och skydd mot bedrägerier



Helst ska du lämna din knut online så ofta som möjligt. I händelse av långvarig frånvaro:




- En illasinnad peer kan försöka sända ut ett gammalt kanaltillstånd
- Blixten ger en "protestperiod" (cirka 2 veckor på LND)
- Om du ska vara borta under en längre tid, sätt upp en Watchtower



**Watchtower konfiguration:**




- I avancerade inställningar för LND lägger du till URL:en för en betrodd Watchtower-server
- Du kan använda en offentlig tjänst eller installera din egen Watchtower




Om du vill veta mer om hur du konfigurerar och använder vakttorn rekommenderar vi att du läser vår dedikerade handledning :



https://planb.network/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### Andra bästa metoder





- Programuppdateringar:** Håll Umbrel och LND uppdaterade (säkerhetsfixar)
- Hårdvaruskydd:** Använd ett stabilt system (Raspberry Pi med SSD, mini-PC) och en UPS
- Nätverkssäkerhet:** Behåll standardkonfigurationen för Tor, ändra lösenordet för Umbrels administratör (standard: "moneyprintergobrrr")
- Kryptering:** Aktivera diskkryptering om möjligt



## 6. Ytterligare verktyg



Umbrels Lightning Node-app ger de viktigaste förutsättningarna för att hantera dina kanaler, men verktyg från tredje part erbjuder avancerad funktionalitet.



### ThunderHub



Interface modernt webbaserat Lightning-nodhanteringssystem som kan installeras via Umbrel App Store.



**Egenskaper:**




- Visualisering av kanaler i realtid (kapacitet, balans)
- Integrerade verktyg för ombalansering
- Stöd för multi-path billing (MPP)
- Generering av QR-kod LNURL
- Transaktionshantering On-Chain



ThunderHub är perfekt för att övervaka en aktiv routingnod och utföra enkel ombalansering.



### Ride The Lightning (RTL)



Interface är webbkompatibel med flera Lightning-implementationer (LND, Core Lightning, Eclair).



**Höjdpunkter:**




- Hantering av flera noder
- Kontextkänsliga instrumentpaneler
- Stöd för ubåtsbyten (Lightning Loop)
- 2-faktor autentisering
- Exportera/importera säkerhetskopior av kanaler



RTL är en komplett "schweizisk armékniv" för att administrera en Lightning-nod med ett mer expertorienterat tillvägagångssätt.



### Andra användbara verktyg





- Lightning Shell** : Kommandorad (lncli) via webbläsare
- BTC RPC Explorer & Mempool** : Övervakning Blockchain
- LNmetrics & Torq**: Analys av routningsprestanda
- Amboss & 1ML**: "Social" hantering av din nod (alias, kontakter, nätverksanalys)



Dessa verktyg kan installeras med bara några klick via Umbrel App Store, utan någon komplicerad konfiguration.



**Ytterligare verktygsresurser:**




- [ThunderHub.io - Funktioner](https://thunderhub.io) - Översikt över ThunderHubs funktioner
- [Ride The Lightning (RTL) info](https://www.ridethelightning.info/) - RTL-dokumentation
- [David Kaspar - Rebalance via ThunderHub](https://blog.davidkaspar.com) - En praktisk guide till ombalansering
- [Guide "Hantering av Lightning-noder"](https://github.com/openoms/lightning-node-management) - Avancerad dokumentation för strömanvändare



## Slutsats



Att köra din egen LND-nod på Umbrel är ett viktigt steg mot finansiell suveränitet. Även om det kräver mer tekniskt engagemang än en förvaringslösning, är fördelarna när det gäller kontroll, integritet och aktivt deltagande i Lightning Network betydande.



Genom att följa den här guiden bör du nu kunna installera LND, öppna kanaler, hantera din likviditet och få fjärråtkomst till din nod. Känn dig fri att gradvis utforska avancerade funktioner och ytterligare verktyg när du blir mer bekant med ekosystemet.



Kom ihåg att säkerheten för dina medel beror på dina skyddsåtgärder och rutiner. Ta dig tid att förstå alla aspekter innan du sätter in stora summor.