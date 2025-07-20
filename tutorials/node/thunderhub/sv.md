---
name: ThunderHub
description: Interface Webb för hantering av blixtnoder LND
---
![cover](assets/cover.webp)



## Inledning



ThunderHub är en **hanterare med öppen källkod för Lightning-noder (LND)**, som erbjuder en intuitiv Interface som är tillgänglig från alla enheter eller webbläsare.



**Huvudfunktioner:**




- Övervakning**: Global vy över saldon, kanaler, transaktioner, routingstatistik
- Hantering**: Öppna/stänga kanaler, inkommande/utgående betalningar, kanalbalansering
- Integrationer**: LNURL-stöd, swappar via Boltz, Amboss backup
- Interface responsiv**: Kompatibel med mobiler, surfplattor och stationära enheter med mörka/ljusa teman



ThunderHub integreras enkelt med **Umbrel**, **Voltage**, **RaspiBlitz** och **MyNode**, vilket förenklar den dagliga hanteringen av din nod.



**ThunderHub är särskilt lämpad för operatörer som söker en ergonomisk Interface för att hantera sina kanaler, kontrollera likviditet (rebalansering), övervaka transaktioner och integrera tredjepartstjänster som Amboss. Säkerheten garanteras via en lokal eller Tor-anslutning.



Om du ännu inte har en Lightning-nod rekommenderar vi att du följer vår LND Umbrel-handledning:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Installation



ThunderHub kan installeras på ett antal olika sätt, beroende på din Lightning node hosting-miljö. Oavsett om du använder en nyckelfärdig lösning (Umbrel, Voltage, RaspiBlitz, MyNode, Start9, etc.) eller en manuell installation är ThunderHub ofta tillgänglig utan större ansträngning. Nedan beskriver vi två vanliga tillvägagångssätt: via Umbrel App Store och via manuell installation (tillämpligt på en server eller självhostad distribution).



### Installation via Umbrel



Umbrel integrerar ThunderHub i sin **App Store**, vilket gör installationen extremt enkel. Inget behov av en kommandorad eller manuell konfiguration: allt görs via Interface Umbrel. Följ bara dessa steg:





- Öppna Umbrels instrumentpanel**: Anslut till Interface-webben för din Umbrel-nod (t.ex. `http://umbrel.local` på ditt lokala nätverk, eller via dess `.onion` Address om du använder Tor).
- Gå till App Store**: I Umbrels huvudmeny klickar du på "App Store" (eller "App"). Sök efter **ThunderHub** i listan över tillgängliga applikationer.



![Écran d'installation de ThunderHub via Umbrel](assets/fr/01.webp)





- Installera ThunderHub**: Klicka på ThunderHub-applikationen och sedan på installationsknappen. Bekräfta om det behövs. Umbrel kommer automatiskt att ladda ner och distribuera ThunderHub på din nod.





- Starta applikationen**: När installationen är klar (några tiotals sekunder) visas ThunderHub på din startsida. Klicka på ikonen för att öppna den. ThunderHub startas i din webbläsare.



![Identifiants par défaut pour ThunderHub](assets/fr/02.webp)



**Viktigt:** När ThunderHub öppnas första gången visas automatiskt det **standardlösenord** som krävs för att logga in. Med alternativet "Visa inte det här igen" kan du dölja den här visningen för framtida anslutningar. **Vi rekommenderar starkt att du:**




- Spara detta lösenord omedelbart** i din lösenordshanterare
- Kopiera den** för användning i nästa steg
- Markera "Visa inte detta igen" när lösenordet har sparats



![Page de connexion de ThunderHub](assets/fr/03.webp)



Du kommer då till inloggningssidan, där du måste ange lösenordet som du kopierade i föregående steg för att låsa upp Interface.



![Interface de connexion complète à ThunderHub](assets/fr/04.webp)



Umbrel tar hand om att förse ThunderHub med LND-anslutningsinformation (TLS-certifikat, administration macaroon, etc.) i bakgrunden, så du behöver inte göra någon ytterligare konfiguration. Med bara några klick kommer du att ha ThunderHub igång på din Umbrel-nod.



### Manuell installation (självhanterande, exklusive Umbrel)



För användare utanför Umbrel (t.ex. på en personlig server, en Raspberry Pi med RaspiBlitz eller en *stand-alone* installation) kräver installationen av ThunderHub några extra steg. Nedan beskriver vi installationen från källan och konfigurationen, enligt den [officiella ThunderHub-dokumentationen] (https://docs.thunderhub.io).



#### Installation



**Förutsättningar:** Se till att ditt system uppfyller minimikraven enligt [documentation setup] (https://docs.thunderhub.io/setup):




- Node.js** version 18 eller högre
- npm** installerad
- Tillgång till LND-autentiseringsfiler :
  - LND TLS-certifikat (`tls.cert`)
  - LND macaroon för administration (`admin.macaroon`)
  - LND gRPC-tjänst Address (värdnamn:port) (standard `127.0.0.1:10009` lokalt)



**1. Hämta ThunderHub-kod:** Klona projektets GitHub-repository enligt beskrivningen i [installationsdokumentationen] (https://docs.thunderhub.io/installation):



```bash
git clone https://github.com/apotdevin/thunderhub.git
cd thunderhub
```



**2. installera beroenden och bygga applikationen:**



```bash
npm install
npm run build
```



Dessa kommandon installerar alla nödvändiga moduler och kompilerar sedan applikationen (ThunderHub är skriven i TypeScript/React).



**3. Uppdatera senare:** ThunderHub erbjuder flera metoder för framtida uppdateringar:



```bash
# Méthode rapide
npm run update

# Ou méthode manuelle
git pull
npm install
npm run build
```



#### Konfiguration (Setup)



**1. Huvudkonfigurationsfil:** Skapa en `.env.local`-fil i roten av ThunderHub-mappen för att anpassa konfigurationen (detta förhindrar att dina inställningar skrivs över under uppdateringar). Huvudvariabler enligt [setup documentation] (https://docs.thunderhub.io/setup):



```bash
# -----------
# Server Configs
# -----------
LOG_LEVEL='info' # 'error' | 'warn' | 'info' | 'http' | 'verbose' | 'debug' | 'silly'
PORT=3000
NODE_ENV=production

# -----------
# Interface Configs
# -----------
THEME='dark' # 'dark' | 'light' | 'night'
CURRENCY='sat' # 'sat' | 'btc' | 'fiat'

# -----------
# Privacy Configs
# -----------
FETCH_PRICES=true # Récupération des prix BTC/fiat depuis Blockchain.com
FETCH_FEES=true # Récupération des frais on-chain depuis Earn.com
DISABLE_LINKS=false # Liens vers 1ml.com et Blockchain.com
NO_VERSION_CHECK=false # Vérification de version depuis GitHub

# -----------
# TOR (optionnel)
# -----------
TOR_PROXY_SERVER='socks://127.0.0.1:9050' # Pour proxifier via TOR

# -----------
# Account Configs
# -----------
ACCOUNT_CONFIG_PATH='/chemin/vers/thubConfig.yaml' # Fichier de comptes
```



**2. Konfiguration av serverkonton:** Skapa den YAML-fil som anges i `ACCOUNT_CONFIG_PATH` :



```yaml
masterPassword: 'votre_mot_de_passe_principal'
accounts:
- name: 'Mon Nœud LND'
serverUrl: '127.0.0.1:10009'
macaroonPath: '/home/user/.lnd/data/chain/bitcoin/mainnet/admin.macaroon'
certificatePath: '/home/user/.lnd/tls.cert'
password: 'mot_de_passe_compte_specifique'
# Optionnel : compte avec macaroon en hexadécimal
- name: 'Nœud Distant'
serverUrl: 'ip.distante:10009'
macaroon: '0201056c6e6402f8...' # Macaroon en HEX ou Base64
certificate: '0202045c7365...' # Certificat en HEX ou Base64
```



**3. Fjärråtkomst:** För att ansluta till en avlägsen LND-nod, lägg till i `LND.conf` :



```bash
# Option 1 : accès par IP
tlsextraip=<ip-externe-accessible>
rpclisten=0.0.0.0:10009

# Option 2 : accès par domaine
tlsextradomain=<domaine-externe-accessible>
rpclisten=0.0.0.0:10009
```



**4. Säkerhet:** Vid första uppstarten döljer ThunderHub **automatiskt** `masterPassword` och alla kontolösenord i YAML-filen för att undvika att lösenord finns i klartext på servern.



**5. Starta ThunderHub:**



```bash
npm start
```



Som standard lyssnar servern på port 3000. Gå till `http://localhost:3000` (eller `http://ip-serveur:3000` från det lokala nätverket).



**6. Docker-alternativ:** ThunderHub tillhandahåller officiella Docker-bilder:



```bash
# Image standard
docker pull apotdevin/thunderhub:latest
docker run --rm -it -p 3000:3000/tcp apotdevin/thunderhub:latest

# Image avec base path /thub
docker pull apotdevin/thunderhub:base-v0.11.1
```



Inloggningssidan för ThunderHub visas. Välj det konfigurerade kontot och ange lösenordet för att komma åt instrumentpanelen.



**Installation på andra distributioner:** Färdigpaketerade noddistributioner (RaspiBlitz, MyNode, Start9, etc.) erbjuder i allmänhet inbyggt ThunderHub-stöd via sina respektive administrationsgränssnitt.



**För mer information:** Se den fullständiga officiella dokumentationen :




- Installation:** [docs.thunderhub.io/installation](https://docs.thunderhub.io/installation)
- Konfiguration:** [docs.thunderhub.io/setup](https://docs.thunderhub.io/setup)



Dessa resurser beskriver avancerade alternativ som SSO-konton, krypterade macaroons, TOR-konfiguration och mycket mer.



När ThunderHub är installerat och tillgängligt är du redo att utnyttja alla dess funktioner. I följande avsnitt tar vi en titt på Interface ThunderHub och dess olika flikar, för att guida dig genom dess användning.



## Interface presentation



Interface ThunderHub är strukturerad kring en huvudmeny (visas vanligtvis i den vänstra sidokolumnen) som består av flera viktiga avsnitt. Var och en motsvarar en aspekt av hanteringen av din Lightning-nod. Låt oss gå igenom dem en efter en:





- Start** - Startflik med allmän instrumentpanel (översikt över din nod och snabba åtgärder).
- Instrumentpanel** - Anpassningsbar instrumentpanel med widgetar och avancerade mätvärden.
- Peers** - Lightning peer management (anslutningar till andra noder).
- Channels** - Detaljerad hantering av Lightning-kanaler.
- Rebalance** - Verktyg för balansering av kanaler (cirkulära betalningar).
- Transaktioner** - Betalningshistorik för blixtar (LN-transaktioner).
- Forwards** - Routing-statistik (betalningar som vidarebefordrats av din nod).
- Chain** - Node's On-Chain Wallet (On-Chain BTC: UTXOs, transaktioner).
- Amboss** - Integration med Amboss (nodövervakning, säkerhetskopiering etc.).
- Tools** - Diverse verktyg (säkerhetskopior, signerade meddelanden, macaroons, rapporter etc.).
- Swap** - On-Chain/Lightning swapfunktioner via Boltz.
- Stats** - Avancerad statistik och mätvärden för nodprestanda.



*(Obs: Beroende på ThunderHub-versionen kan vissa avsnitt ha något annorlunda rubriker eller ytterligare funktioner, men de allmänna principerna förblir desamma)*



### Home (Allmän kontrollpanel)



ThunderHubs flik **Home** är den startsida som visas när du loggar in. Den innehåller **General Dashboard**, som ger en **global översikt** över statusen för din Lightning-nod och föreslår **snabba åtgärder** för rutinoperationer. Det här är vad du vanligtvis hittar:



![Tableau de bord principal de ThunderHub](assets/fr/05.webp)





- Saldon och kapacitet:** Högst upp på sidan visar ThunderHub dina tillgängliga saldon. Här ser du vanligtvis On-Chain-saldot (Bitcoin On-Chain i nodens Wallet, symboliserat av en Anchor ⚓) och Lightning-saldot (dina kanalers kapacitet, symboliserat av en blixt Bolt ⚡). Detta ger dig en omedelbar uppfattning om hur mycket pengar du har i On-Chain och Lightning. Om du har flera konton eller kanaler, se till att du är på rätt (t.ex. Mainnet vs Testnet).





- Nyckelstatistik:** Instrumentpanelen kan visa vissa globala mätvärden för din nod - t.ex. antal öppna kanaler, antal anslutna peers, intjänade routingavgifter (om tillämpligt) osv. Det är en sammanfattning av nodens senaste aktivitet och hälsa.





- Snabbåtgärder:** Instrumentpanelen innehåller knappar för att snabbt utföra de vanligaste uppgifterna utan att behöva navigera genom menyer. Dessa snabba åtgärder inkluderar :





  - Ghost**: Ställde in en anpassad Lightning Address via Amboss.
  - Donera**: Gör en donation via Lightning.
  - Logga in/Gå till**: Anslut till ditt Amboss-konto (Quick Connect) och gå direkt till Amboss.space för att se information om din nod.
  - Address** : Ange en Lightning Address för att göra en betalning.
  - Öppna**: Öppna en ny Lightning-kanal. Om du klickar öppnas ett formulär där du kan ange URI för den fjärrnod som kanalen ska öppnas till, beloppet och, om tillämpligt, den maximala On-Chain-avgiften som ska användas.
  - Avkoda**: Avkoda en Lightning Invoice eller LNURL för att se detaljer före betalning.
  - LNURL**: Behandla LNURL:er för Lightning-betalningar eller uttag.
  - LnMarkets inloggning**: Logga in på LnMarkets för handel.



Dessa snabbåtgärder gör att du kan utföra de vanligaste åtgärderna direkt från startsidan utan att behöva navigera genom Interface:s olika flikar.



Kort sagt, ThunderHubs instrumentpanel ger dig en **snabb titt** på din nod och låter dig utföra de vanligaste operationerna (skicka/motta, öppna en kanal) med ett enda klick. Det är den perfekta utgångspunkten för den dagliga administrationen.



### Instrumentpanel



Avsnittet **Dashboard** är skilt från fliken Home och erbjuder en mer avancerad, anpassningsbar instrumentpanel. I det här avsnittet kan du skapa en anpassad vy med specifika widgetar efter dina behov som nodoperatör.





- Anpassningsbara widgets:** Till skillnad från startsidan, som har en fast layout, kan du i Dashboard välja exakt vilka Elements som ska visas och hur de ska organiseras.



![Dashboard sans widgets activés](assets/fr/06.webp)



Om inga widgetar är aktiverade visas meddelandet "No Widgets Enabled!" med en "Settings"-knapp för att komma åt anpassningsparametrarna.



![Paramètres des widgets du Dashboard](assets/fr/07.webp)



I inställningarna kan du välja mellan ett brett utbud av widgets som är organiserade i kategorier: "Lightning - Info", "Lightning - Table", "Lightning - Graph", och så vidare. Varje widget kan aktiveras eller avaktiveras individuellt med knapparna "Show/Hide".



![Bas de la page des paramètres](assets/fr/08.webp)



Längst ned i inställningarna hittar du knappen "To Dashboard" för att återgå till instrumentpanelen och knappen "Reset Widgets" för att återställa standardvisningen.



![Dashboard personnalisé avec widgets](assets/fr/09.webp)



När du har konfigurerat din instrumentpanel kan du visa olika grafer och mätvärden: Grafer för Lightning-betalningar, antal utställda fakturor, statistik för forwards, detaljerade saldon osv.





- Avancerade mätvärden:** Få tillgång till mer detaljerad statistik om din nods prestanda, med grafer och realtidsdata.





- Konfigurerbar översikt:** Skräddarsy displayen så att den passar oavsett om du är en vanlig användare eller en professionell operatör som hanterar flera routingkanaler.





- Modular Interface:** Lägg till eller ta bort widgets efter behov: framåtdiagram, likviditetsmått, nodernas hälsovarningar etc.



Detta avsnitt är särskilt användbart för avancerade användare som vill övervaka specifika mätvärden eller få en mer teknisk översikt över sin Lightning-nod. Det kompletterar avsnittet Hem genom att erbjuda större flexibilitet och kontroll över hur informationen visas.



### Kollegor



I avsnittet **Peers** listas alla Lightning-noder som för närvarande är anslutna till din som peers. En **peer** är en direkt nod-till-nod-anslutning på Lightning Network. Din nod kan vara ansluten till peers även utan en öppen kanal (t.ex. bara för Exchange-skvallerinformation i nätverket), eller så innebär naturligtvis varje öppen kanal automatiskt en ansluten peer.



![Vue de l'onglet Peers avec les pairs connectés](assets/fr/10.webp)



På fliken Peers ser du :





- Informationskolumner:** Interface visar användbara detaljer som synkroniseringsstatus, anslutningstyp (clearnet eller Tor), ping, mottagna/sända satoshis och mängden data som utbyts.
- Lägg till en peer:** ThunderHub låter dig manuellt ansluta till en ny peer via **"Add"**-knappen i det övre högra hörnet. Du måste ange nodens URI (format `<public_key>@<socket>`). När den har validerats skickar ThunderHub motsvarande `lncli connect`-kommando. Om noden är online och tillgänglig kommer den att läggas till i din lista över peers.



### Kanaler



Fliken **Channels** är hjärtat i Lightnings kanalhantering. Det är förmodligen det avsnitt du kommer att konsultera oftast. Här presenteras **alla dina Lightning-kanaler** med information om dem, och du kan utföra hanteringsåtgärder på dessa kanaler.



![Vue d'ensemble des channels ouverts](assets/fr/11.webp)



Det här är vad du hittar på sidan Kanaler:





- Kanallistvy:** Varje öppen (eller öppnande/stängande) kanal listas, vanligtvis med fjärrnodens alias, den totala kanalkapaciteten och en färgad stapel som illustrerar fördelningen av lokal kontra fjärrlikviditet. ThunderHub använder en färgkod (ofta blå/Green) eller en procentsats för att ange kanalbalans: till exempel blå för din lokala andel, Green för fjärrandelen. Om en kanal är perfekt balanserad (50/50) kommer stapeln att vara hälften av varje färg. På så sätt kan du snabbt se vilka kanaler som är obalanserade (alla blå = nästan alla lokala, alla Green = nästan alla fjärrkanaler).





- Informationskolumner:** Interface visar detaljerade kolumner inklusive Status, Tillgängliga åtgärder, Peer Info, Kanal-ID, Kapacitet, Aktivitet, Avgifter och Saldo med grafisk likviditetsvisning.





- Displaykonfiguration:** Ett kugghjul i det övre högra hörnet gör att du kan anpassa kanalvisningen efter dina önskemål.





- Status:** Du kommer också att se statusindikatorer - t.ex. `Active` (kanalen är öppen och i drift), `Offline` (peer är frånkopplad, så kanalen är tillfälligt oanvändbar), `Pending` (för öppningar eller stängningar som väntar på bekräftelse från On-Chain).





- Åtgärder på en kanal:** För varje kanal tillhandahåller ThunderHub åtgärdsknappar (ofta i form av ikoner):



![Actions de gestion des canaux - Modifier et Fermer](assets/fr/12.webp)





  - Redigera avgifter:** Med Interface "Uppdatera kanalpolicy" kan du justera alla kanalparametrar: Grundavgift, Avgiftssats (i ppm), CLTV Delta, Max HTLC och Min HTLC. Detta gör att du kan justera dina avgiftspolicyer individuellt per kanal, i syfte att locka (eller avskräcka) routningstrafik. *(Obs: ThunderHub är inte en ersättning för ett automatiskt verktyg för avgiftshantering, men för manuell justering är det mycket effektivt)*
  - Stäng kanal (*Close*)**: Interface "Close Channel" ger dig möjlighet att välja mellan en **cooperative close** (standard) eller en **forced close** (*Force Close*) genom att definiera avgifterna (i Sats/vByte). **Viktigt:** föredra alltid cooperative close när det är möjligt, för att undvika On-Chain avvecklingsförseningar och högre avgifter. ThunderHub kommer att tala om för dig om peer är online (cooperative possible) eller inte. I händelse av force close, var noga med att bekräfta eftersom detta är irreversibelt och kommer att utlösa en svepande transaktion med en tidslåsning (vanligtvis 144 block eller ~ 1 dag på Bitcoin Mainnet).
  - Öppna en ny kanal:** Du öppnar en ny kanal genom att klicka på kugghjulet längst upp till höger på sidan Channels och sedan välja "Open". Du kan sedan starta en kanal till en ny eller befintlig peer. Fördelen med att använda den här sidan är att du har en lista över dina befintliga kanaler framför dig, vilket kan hjälpa dig att bestämma var du ska öppna en ny kanal.



Kort sagt ger avsnittet Channels dig **fin kontroll över varje kanal**. Det är här du driver likviditetsallokering, bestämmer vilka kanaler som ska behållas eller stängas och ställer in dina routningsparametrar per kanal. ThunderHub erbjuder en tydlig Interface för dessa viktiga nodhanteringsoperationer.



### Ombalansering



Fliken **Rebalansering** är avsedd för **kanalbalansering**. Balansering (eller *ombalansering*) innebär att du justerar fördelningen av medel mellan dina utgående och inkommande kanaler genom att göra en **cirkulär betalning** från en av dina kanaler till en annan av dina kanaler via Lightning Network. Detta gör att du, utan att föra in nya medel, kan flytta likviditet från en kanal som är för full till en som är för tom, vilket gör dina kanaler mer användbara (en balanserad kanal kan både skicka och ta emot betalningar).



![Interface de rebalance des canaux](assets/fr/13.webp)



ThunderHub underlättar i hög grad denna operation, som annars skulle vara tråkig på kommandoraden. Så här använder du Rebalance-avsnittet:





- Initial kanalvy:** När du går in i Rebalance visar ThunderHub en lista över dina kanaler, med en balansindikator för varje (liknande den på sidan Channels). Du kan direkt se vilka kanaler som är i obalans. ThunderHub kan sortera kanalerna i ordning efter ökande balans, så att de mest obalanserade kanalerna sticker ut högst upp i listan (0.0 betyder helt lokal eller fjärr).





- Peer-val:** Interface gör det enkelt att välja utgående och inkommande peers för ombalansering.





- Parameterinställningar:** Du kan ställa in :
  - Den **maximala avgift** (i Sats och ppm) som du är villig att betala
  - Det **belopp som ska ombalanseras** med alternativet "Fast" eller "Mål"
  - Noder som ska undvikas** vid routning
  - Maximal provtid** för vägvisning





- Välj **källa**** kanal: Välj först den **utgående (käll)** kanalen, dvs. den kanal från vilken du har för mycket lokal likviditet för att flytta. I praktiken är detta en kanal där din lokala andel är hög (> 50 %). Låt oss föreställa oss en A-kanal med 1.000.000 Satss, varav 900.000 är lokala - en bra kandidat för att skicka Satss någon annanstans. Genom att klicka på denna A-kanal som "utgående" markerar ThunderHub den som en källa.





- Välj **målkanal****: Välj sedan den **inkommande (mål)** kanalen som behöver ta emot likviditet. Vanligtvis kommer detta att vara en kanal där det är tvärtom - de flesta medel är på bortre sidan (t.ex. endast 100 000 lokala Satss av 1 000 000). ThunderHub kommer, när källkanalen har valts, att sortera de andra kanalerna i omvänd ordning (minskande balans) för att hjälpa till att identifiera de mest kompletterande kanalerna. Välj en B-kanal som har plats på den lokala sidan. ThunderHub kommer då att tydligt visa vilka två kanaler som har valts (källa A och mål B).





- Ange avgiftsbelopp och tolerans:** Ett formulär gör att du kan ange :





  - Det **belopp** som ska ombalanseras (i Sats). Ofta väljer vi ett belopp som är lika med vad som skulle balansera båda kanalerna vid \~50/50. ThunderHub kan till exempel förfylla hälften av källkanalens överkapacitet.
  - Den **maximala avgift** som du är villig att betala för denna åtgärd (valfritt). Denna avgift uttrycks i Sats (total kostnad för cirkulär routing). Om du lämnar den tom kommer ThunderHub att söka efter en väg oavsett kostnad, vilket i allmänhet inte är tillrådligt (det är bättre att ange en gräns, t.ex. 10 Sats för en liten ombalansering, eller en maximal ppm).





- Hitta rutt:** Klicka på knappen för att hitta en rutt. ThunderHub frågar LND för att beräkna en rutt från din källkanal genom nätverket till din egen målkanal. Om den hittar en möjlig rutt som uppfyller dina avgiftskriterier visar den den med information om hoppen och avgiftskostnaden. Den kan till exempel indikera att den har hittat en 3-hopsväg med totalt 2 Sats i avgifter.





- Starta ombalansering:** Om du är nöjd med den föreslagna rutten, klicka på **Balance Channel**. ThunderHub kommer då att initiera cirkulär betalning via LND. Om betalningen lyckas kommer du att se ett meddelande om framgång, och kanalerna A och B kommer att få sina saldon ändrade i realtid. ThunderHub kommer att uppdatera balansindikatorn för dessa kanaler (helst kommer de att vara grönare än tidigare, vilket indikerar bättre balans).





- Justeringar och iterationer:** Om ingen rutt hittas på första försöket (eller om den är för dyr) kan du justera parametrarna :





  - Prova med ett mindre belopp (ibland går en partiell ombalansering igenom medan en stor mängd misslyckas).
  - Höj den högsta avgiften gradvis, men var försiktig så att du inte betalar mer i avgifter än vad det är värt.
  - Använd knappen **Get Another Route**, om den är tillgänglig, för att prova ett alternativ.
  - Försök med ett annat par kanaler om det verkligen blir besvärligt.



ThunderHub gör processen mycket **intuitiv och visuell**. I bara fyra steg (välj utgående kanal, välj inkommande kanal, belopp, validera) kan du göra det som tidigare krävde komplexa manuella kommandon. Verktyget är ovärderligt för att upprätthålla en välbalanserad nod, förbättra din routingprestanda och upplevelse (lättare att skicka och ta emot betalningar över alla dina kanaler).



Observera slutligen att en ombalansering förbrukar routingkostnader (som betalas till mellanliggande noder), så det är en **investering** för att göra din nod mer flytande. Använd den klokt, till exempel för att stödja en kanal till en tjänst som du använder ofta (inkommande likviditet) eller för att balansera en stor routningskanal. ThunderHub låter dig göra detta **enkelt och effektivt**.



### Transaktioner



Avsnittet **Transactions** i ThunderHub motsvarar din nods **Lightning** transaktionshistorik, dvs. betalningar och fakturor som betalats eller mottagits via kanalerna. Det är ett slags kontoutdrag för din LN-verksamhet.



![Historique des transactions Lightning](assets/fr/14.webp)



I den här fliken hittar du :





- Invoice graf:** I det övre högra hörnet visar en graf utvecklingen av mottagna fakturor över tid, vilket gör att du kan visualisera din nods aktivitet.





- En kronologisk lista över alla Lightning-transaktioner som gjorts *från* eller *till* din nod. Varje post kan visa :





  - Typ av operation: **sent payment** (utgående betalning) eller **received payment** (inbound, via en betald Invoice).
  - Beloppet i Sats.
  - Datum/tid.
  - Betalnings-ID (Hash eller RHash pre-image) eller kommentar (om du lagt till ett memo i Invoice).
  - Status: **fullbordad**, eller möjligen **pågående**/*misslyckad* (t.ex. en betalning som väntar på lösning, men i allmänhet behandlar LND detta snabbt, så det finns lite "väntande" här jämfört med On-Chain-transaktioner).



Kort sagt, avsnittet Transaktioner fungerar som din ** LN aktivitetslogg **. Det är mycket användbart för att kontrollera att en betalning har gått igenom, hur många avgifter den kostade eller spåra historiken för dina Lightning-utbyten. I kombination med avsnittet Framåt (beskrivs nästa) har du en fullständig bild av de pengar som har passerat genom din nod.



### Framåt



Fliken **Forwards** är avsedd för din nods **routing**-aktivitet, dvs. betalningar som **transiteras** genom dina kanaler (när du fungerar som en mellanliggande nod på Lightning Network). Om du driver din nod som en routing-nod är detta ett viktigt avsnitt för att spåra dina resultat.



![Statistiques de routage Lightning](assets/fr/15.webp)



I Forwards presenterar ThunderHub :





- Filter och visningsalternativ:** Längst upp till höger finns filter som gör att du kan sortera data efter dag/vecka/månad/år och välja mellan grafisk visning eller tabellvisning.





- Aktivitetsmeddelande:** Om ingen routing har utförts under den valda perioden visar Interface "Inga forwards för denna period", som visas i detta exempel.





- En **tabell över de senaste vidarebefordringarna**: varje post motsvarar en betalning som har **vidarebefordrats** via din nod. För varje forward ser vi i allmänhet :





  - Timestamp,
  - det belopp som dirigeras (i Sats),
  - den **avgift som tjänats** på denna forward (i Sats är detta skillnaden mellan vad du fick på den inkommande kanalen och skickade på den utgående),
  - de inkommande och utgående kanaler som används (identifieras ofta av peer-alias eller kanal-ID).
  - status (normalt *completed*, eller failure om en forward misslyckades på vägen).





- Aggregerad statistik**: ThunderHub beräknar och visar högst upp på sidan totaler och statistik över en viss period (t.ex. de senaste 24 timmarna, eller 7 dagar, etc., ibland konfigurerbar).



Kort sagt, avsnittet Forwards erbjuder en **översikt i realtid över din Lightning-nods routingaktivitet**. Tillsammans med avsnitten Channels och Rebalance utgör detta ett komplett paket för att optimera din nod: Channels/Rebalance för likviditet, Forwards för att observera resultat (flöden och vinster).



### Kedja



Avsnittet **Chain** motsvarar Bitcoin On-Chain Wallet-hanteringen av din LND-nod. Med denna Interface kan du visa och hantera Bitcoin-medel, som används för att öppna kanaler eller ta emot medel från stängda kanaler.



![Gestion du portefeuille on-chain](assets/fr/16.webp)



I Chain hittar du :





- Balance On-Chain :** Visar det totala BTC-saldot som finns tillgängligt i Wallet LND.





- Lista över UTXO:** Visa alla outnyttjade utgångar (UTXO) med belopp, bekräftelser, Address och format för varje utgång.





- Transaktionshistorik:** Detaljerad tabell över alla Bitcoin-transaktioner med typ (in/ut), datum, belopp, avgifter, bekräftelser, inkluderingsblock, adresser och txid.



### Amboss



ThunderHub integreras med **Amboss**-plattformen (amboss.space), som erbjuder detaljerad information om Lightning-noder, en likviditetsmarknadsplats och användbara funktioner som krypterad kanalbackup och tillgänglighetsövervakning.



![Intégration Amboss avec ses options](assets/fr/17.webp)



I ThunderHub kan du i Amboss-avsnittet **länka** din nod till ditt Amboss-konto:





- Ghost Address:** Sätt upp en **personlig Lightning Address** för din nod, vilket underlättar inkommande betalningar.





- Automatisk säkerhetskopiering av kanaler:** Flaggskeppsfunktion för krypterad säkerhetskopiering av kanaler** (SCB-filer) på Amboss. Aktivera **Amboss Auto Backup = Yes** i inställningarna för att automatiskt skicka krypterade backup-uppdateringar varje gång du byter kanal. I händelse av ett fel kommer du att kunna återställa dina pengar tack vare denna externa säkerhetskopia.





- Hälsokontroller:** Aktivera **Amboss Healthcheck = Yes** för att få din nod att skicka regelbundna pingar till Amboss. Du kommer att få varningar om din nod verkar vara offline.





- Andra funktioner:** Automatisk saldopostering, **Magma/Hydro**-integration (likviditetsmarknadsplats) och tillgång till detaljerad prestationsstatistik.



Amboss integration lägger till en viktig **säkerhet Layer** med automatisk extern säkerhetskopiering och tillgänglighetsövervakning, tillgänglig direkt från ThunderHub.



### Verktyg



Avsnittet **Tools** samlar olika avancerade verktyg för hantering av din nod. Här är de viktigaste Elements:



![Interface des outils disponibles](assets/fr/18.webp)





- Backups:** Manuellt hantera dina kanalbackups (SCB). ThunderHub låter dig ** ladda ner den kompletta säkerhetskopian** av dina kanaler (alternativ "Säkerhetskopiera alla kanaler -> Ladda ner"). Förvara den här filen `channel-all.bak` på ett säkert ställe - den är viktig för att återställa dina medel i händelse av en krasch. Du kan också **importera** en säkerhetskopia när du omplacerar en nod.





- Redovisning:** Exportverktyg för finansiella rapporter, inklusive intjänade/betalda arvoden och volymer som förmedlats under en viss period.
- Signerade meddelanden:** **Signera eller verifiera meddelanden** med din nod för att bevisa Ownership för din Lightning-nod via kryptografisk signatur.
- Makroner (bageriavsnitt):** Hantera LND** makroner för att skapa anpassad åtkomst. Interface "Bageri" gör att du kan välja exakt varje behörighet: "Lägg till eller ta bort kamrater", "Skapa kedjeadresser", "Skapa fakturor", "Skapa makroner", "Härled nycklar", "Hämta åtkomstnycklar", "Hämta kedjetransaktioner", "Hämta fakturor", "Hämta Wallet-information", "Get Payments", "Get Peers", "Pay Invoices", "Revoke Access Ids", "Send to Chain Addresses", "Sign bytes", "Sign Messages", "Stop daemon", "Verify bytes signature", "Verify messages", och så vidare. Varje behörighet kan aktiveras individuellt med "Ja/Nej"-knapparna för att skapa en skräddarsydd macaroon.
- Systeminformation:** Visning av Wallet-version och aktiverade RPC:er.



Kort sagt samlar Tools-avsnittet avancerade administrationsfunktioner - säkerhetskopiering, redovisning, säkerhet och åtkomsthantering - i en enhetlig Interface.



### Byta



ThunderHubs **Swap**-flik låter dig byta Lightning satoshis till Bitcoin On-Chain via Boltz-tjänsten. Denna funktion är användbar för att "dumpa" överflödig Lightning-likviditet till kanalen utan att stänga en kanal.



![Interface de swap via Boltz](assets/fr/19.webp)



Processen är enkel:





- Belopp**: Ange det belopp som ska växlas
- Address** : Ange Bitcoin mottagning Address
- Utförande**: ThunderHub kommunicerar med Boltz för att automatiskt behandla Exchange



**Förmåner:**




- Icke-förvaltande tjänst (ingen kontantförvaring)
- Bevara dina befintliga kanaler
- Lättanvänd integrerad Interface



Boltz tar ut en liten provision och du betalar den vanliga Bitcoin transaktionsavgiften. ThunderHub visar alla kostnader före bekräftelse.



### Statistik



ThunderHubs **Stats**-avsnitt erbjuder **avancerad statistik** på din Lightning-nod för att analysera prestanda och optimera routing.



![Statistiques du nœud via Amboss](assets/fr/20.webp)



Detta avsnitt är viktigt för att optimera dina kostnader, identifiera framgångsrika kanaler och planera expansionen av din nod.



## Slutsats



**ThunderHub** har etablerat sig som det viktigaste verktyget för enkel administration av en Lightning **LND**-nod. Denna moderna Interface erbjuder alla viktiga funktioner: kanalhantering, betalningar, övervakning, med avancerade funktioner som automatiserad ombalansering och Amboss-integration.



**Viktiga fördelar:**




- Interface elegant och intuitiv
- Kraftfulla verktyg (ombalansering, Boltz-swappar, automatiska säkerhetskopior)
- Kompatibel med Umbrel, Voltage, RaspiBlitz och andra distributioner



ThunderHub demokratiserar avancerad Lightning-nodhantering och gör tillgängligt det som tidigare krävde komplexa tekniska kommandon. Oavsett om du är nybörjare eller en erfaren operatör låter ThunderHub dig effektivt hantera din Lightning-nod via en modern, omfattande Interface.



## Resurser



**Officiella länkar: **




- Officiell webbplats:** [thunderhub.io](https://thunderhub.io)
- Dokumentation:** [docs.thunderhub.io](https://docs.thunderhub.io)
- Källkod på GitHub:** [github.com/apotdevin/thunderhub] (https://github.com/apotdevin/thunderhub)