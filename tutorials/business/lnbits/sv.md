---
name: LNbits

description: Plattform för redovisning för handlare
---

![presentation](assets/lnbits-intro.webp)

# Redovisningssystem


LNbits är fullpackat med massor av verktyg för att kontrollera och kanalisera dina inkommande och utgående medel, ansluta din webbutik eller till och med enheter som en Hardware Wallet eller en bankomat som du har byggt själv. Användartyper inkluderar:


- Wallet-ägare som vill använda LNbits som en Interface för sin penninghantering samt dess extrafunktioner.
- Online- och offlinehandlare eller tjänsteleverantörer som vill acceptera Bitcoin onchain- och Lightning Network-betalningar.
- Utvecklare som vill bygga Lightning Network-applikationer.
- Nodoperatörer som vill integrera sin nod med LNbits-systemet för bokföringsändamål.
- Alla dessa har olika behov. Vi bygger LNbits på ett modulärt sätt så att varje användare kan använda våra funktioner på det sätt som passar dig bäst.


# Wallet chef


LNbits är ett redovisningssystem med fri och öppen källkod - inte en nodhanterare. Kanalhantering är domänen för Lightning-noden som är ansluten till LNbits som en finansieringskälla som LND eller c-lightning. Superanvändaren eller administratörsanvändarna i LNbits-systemet ansvarar för att hantera den övergripande åtkomsten och konfigurationen av redovisningsfunktionerna och interna tillägg.


LNbits fungerar som en Interface mellan användaren och Lightning-noden, vilket ger ett enkelt och användarvänligt sätt att hantera och interagera med betalningsnätverket.


Tänk på LNbits som ett "modulärt Wordpress-ramverk" för din nod. En plattform som är enkel att hantera, baserad på tillägg som du kan kombinera för många olika användningsområden.


Tänk på LNbits som din egen banks programvara för finansiell hantering. Din nod erbjuder kanaler att betala genom och LNbits utökar din nod för att kunna köra mer än en blixt Wallet som din nod levereras med. Dessa plånböcker behöver inte nödvändigtvis tillhöra dig själv. Låt oss säga att du, som LN-nodkörare, redan har tillräckligt med kanallikviditet och medel och nu vill erbjuda några Bitcoin-banktjänster till dina vänner, familj, egen butik eller andra vanliga handlare.


Du kommer att erbjuda ett enkelt sätt för dem att öppna ett "bankkonto" på din nod utan att ha tillgång till andra plånböcker på din nod och till all din nodlikviditet, utan bara deras del. Din nod (banken) fungerar bara som en transportör för deras betalningar (in/ut).


OBS: alla medel som dina "kunder" sätter in på sina LNbits-bankkonton på din nod kommer att gå direkt in i din nods LN-kanaler. Det betyder att DU faktiskt är den verkliga ägaren av dessa medel. Du kommer att ha ett stort ansvar för deras medel. Var inte ond och spring iväg med pengarna, var inte ond och ta ut höga avgifter. Vi vill knulla fiat-banksterna, inte knulla varandra (Bitcoin-användare).


# Demo plattform


Demot finns på [https://legend.lnbits.com](https://legend.lnbits.com). Den är fullt funktionell och kan användas för att lära sig mer om Lightning Network och funktionerna i LNbits och LNURL i allmänhet. Även om vi inte kan hindra dig från det skulle vi vilja be dig att inte använda det för din produktionsinställning. Vi arbetar inte bara ofta på servrarna för att testa nya funktioner utan vi vill också uppmuntra dig att köra din egen nod och LNbits på ett suveränt sätt. Om du tycker att det är för mycket begärt att köra en nod för tillfället kan du ansluta LNbits till en förvaringsfinansieringstjänst i molnet som Opennode, Luna eller Votage eller till Lightning Tipbot på Telegram för att bara nämna några.


# LNbits flygblad


Vill du lämna över lite grundläggande information till en handlare eller en byggnadsvän till dig? Vi är mycket glada över att kunna presentera vår första flyer som alla kan använda. Storleken är ett globalt typiskt flyerformat med 6 sidor (2 vikningar) och en bredd på 3508 och en höjd på 2480px.


LNbits för handlare: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)


LNbits för byggare: [EN](/assets/lnbits-builders-en.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)


# Några grunder


LNbits arbetar baserat på LNURL-protokollet, vilket innebär att förfrågningar är giltiga i två former: antingen som https:// clearnet-länk (inga självsignerade certifikat tillåtna) eller som http:// v2/v3 onion-länk. För att erbjuda LNbits-tjänster som LNURLp/w QR-koder eller NFC-kort, som kan användas i naturen, måste du öppna LNbits för clearnet (https).


Innan du installerar LNbits ska du se till att du har läst och förstått följande allmänna guider om vad LNbits är och vilka möjligheter det ger dig.



- [LND Guide] (https://docs.lightning.engineering/) | Installera LND
- [LND konfigurationsexempel](https://github.com/lightningnetwork/LND/blob/master/sample-LND.conf) | LND inställningar
- [CLN-guide](https://docs.corelightning.org/docs/installation) | Installera CLN
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips) Nostr Spec
- [Kör en Watchtower] (https://docs.lightning.engineering/lightning-network-tools/LND/Watchtower) | Mycket viktigt!


Mer detaljerade guider för användning av LNbits i specifika användningsscenarier här:



- [Komma igång med LNbits] (https://darthcoin.substack.com/p/getting-started-lnbits) | Substack-guide
- [ToDos för din säkerhet med LNbits](https://youtu.be/i5FQf96e6zg) | Youtube Video
- [Privata banker på Lightning Network] (https://darthcoin.substack.com/p/Bitcoin-private-banks-over-lightning) | Substack guide
- [Kör depåplånböcker för dina vänner och familj] (https://darthcoin.substack.com/p/the-bank-of-lnbits) | Substack guide
- [LNbits för en liten restaurang / hotell](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | Substack guide
- [Använda LNbits Streamer copilot](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Substack guide
- [Starta din NOSTR-marknad med LNbits](https://darthcoin.substack.com/p/lnbits-nostr-market) | Substack-guide
- [Använda LNbits för skolprojekt eller festivalevenemang] (https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) Substack-guide



# Installera LNbits


## Grundläggande installationsguide


LNbits kan installeras på vilken Linux OS-maskin som helst. Det kräver inte en kraftfull maskin eller server, bara tillräckligt med RAM-minne och lite diskutrymme för databasen. Det kan köras separat från en BTC/LN-nod (lokal PC eller fjärr-VPS) eller tillsammans på samma maskin som noden eller redan installerat i en mjukvarumaskin med nodpaket.


Du kan välja mellan de vanligaste pakethanterarna som poetry och nix. Som standard kommer LNbits att använda SQLite som sin databas. Du kan också använda PostgreSQL, vilket rekommenderas för applikationer med hög belastning. [Här är en guide för grundläggande installation med hjälp av poetry eller nix](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).


För dig som är nybörjare hittar du mer detaljerade steg-för-steg-guider för att få dina LNbits att fungera i specifika miljöer:


- [LNbits på clearnet](https://ereignishorizont.xyz/lnbits-server/en/) av Axel
- [LNbits på en VPS](https://github.com/TrezorHannes/vps-lnbits) av Hannes
- [LNbits på cloudflare] (https://www.nodeacademy.org/lnbits) av Leo


Du kan också hitta en video på [dockerised Setup on a VPS with PostgreSQ, LightningTipBot as a funding source using nginx] (https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/).


[Fler installationsscenarier här] (https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).


För programvarunoder i paket hänvisas till deras specifika dokumentation om LNbits: [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)


## LNbits SaaS


När du inte är intresserad av tekniska saker och varken vill vara värd för din finansieringskälla eller dina LNbits själv finns det en [LNbits SaaS-version](https://saas.lnbits.com) (Software-as-a-service) som du kan använda. Det är i princip som LNbits i ett moln men du kan definiera finansieringskällan (t.ex. din nod, en LNbits Wallet, LNtipbot, fakewallet etc.) och miljövariablerna själv - vilket oftast inte är fallet med andra molnlösningar.


[Här är en detaljerad guide om hur du använder LNbits SaaS för specifika användningsfall] (https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).


## Finansieringskällor


LNbits är inte en programvara för nodhantering utan ett LN-fokuserat redovisningssystem ovanpå en LND- eller CLN-finansieringskälla. Efter den första installationen kan du besöka din LNbits på http://localhost:5000/.


För att ändra finansieringskällan, gå till din superanvändar-URL och välj en finansieringskälla i "Manage Server" eller redigera .env-filen genom att ändra `LNBITS_BACKEND_WALLET_CLASS` till den källa du behöver om du ställer in `adminUI=TRUE` i `.env`.


Du hittar .env-filen i din lnbits/ eller lnbits/apps/data-mapp genom att utöka kommandot till att lista filer i din katalog med `ls -a`.


Du kan också behöva installera ytterligare paket eller utföra ytterligare installationssteg och välja önskad finansieringskälla. Efter en omstart kommer din nya installation att vara aktiv.


Vilka finansieringskällor kan jag använda för LNbits?


LNbits kan köras på toppen av många finansieringskällor för lightning-nätverk. För närvarande finns det stöd för CoreLightning, LND, LNbits, LNPay, OpenNode, och fler läggs till regelbundet.

Det är viktigt att välja en källa som har god likviditet och bra peers anslutna. Om du använder LNbits för offentliga tjänster kan dina användares betalningar bara flöda lyckligt i båda riktningarna.


En backend Wallet (finansieringskälla) kan konfigureras med hjälp av följande LNbits-miljövariabler i filen `.env` eller i ditt superanvändarkonto under avsnittet Manage-Server.

Om du vill använda .env-versionen kan du hitta parametrarna här:



### CoreLightning


- CLN
  - `LNBITS_BACKEND_WALLET_CLASS`: **CoreLightningWallet**
  - `CORELIGHTNING_RPC`: /fil/väg/blixtnedslag-RPC
- Gnista (c-blixt)
  - `LNBITS_BACKEND_WALLET_CLASS`: **Sparkplånbok**
  - `SPARK_URL`: http://10.147.17.230:9737/RPC
   - `SPARK_TOKEN`: hemlig_accessnyckel

### Lightning Network Daemon


- LND (REST)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `LND_REST_CERT`: /file/path/tls.cert
  - `LND_REST_MACAROON`: /file/path/admin.macaroon eller Bech64/Hex
  - `LND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - `LNBITS_BACKEND_WALLET_CLASS`: **Lnd plånbok**
  - `LND_GRPC_ENDPOINT`: ip_adress
  - `LND_GRPC_PORT`: port
  - `LND_GRPC_CERT`: /file/path/tls.cert
  - `LND_GRPC_MACAROON`: /file/path/admin.macaroon eller Bech64/Hex

Du kan också använda en AES-krypterad macaroon (mer info) istället genom att använda


  - `LND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

För att kryptera din macaroon, kör `./venv/bin/python lnbits/wallets/macaroon/macaroon.py`.


### LNbits (en annan LNbits-instans)



- LNbits-instans på en molnserver eller din egen hemserver
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbits plånbok**
  - `LNBITS_ENDPOINT`: https://lnbits.mydomain.com
  - `LNBITS_KEY`: my-lnbits-AdminKey
- LNbits Legend Demo Server (!! Använd INTE den här för produktion / kommersiella ändamål, endast för testning !!)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbits plånbok**
  - `LNBITS_ENDPOINT`: https://legend.lnbits.com
  - `LNBITS_KEY`: legend-lnbits-AdminKey

### Blixt TipBot


För att ansluta din [Lightning Tipbot] (https://t.me/LightningTipBot) från Telegram måste du ställa in följande parameter:


  - `LNBITS_BACKEND_WALLET_CLASS`: **LnTipsPlånbok**
  - `LNBITS_ENDPOINT`: https://LN.tips
  - `LNBITS_KEY`: För att få nyckeln måste du köra /api i en privat chatt med LightningTipbot på Telegram en gång.


Se även denna handledning hur man installerar [LNbits med LightningTipBot via vps] (https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)


### IBEX HUB


Registrera dig [här] (https://ibexpay.ibexmercado.com/onboard) och hämta sedan dina nycklar/tokens därifrån, slutpunkt är https://ibexpay-api.ibexmercado.com.

Mer information finns i [IBEX API-Dokumentation] (https://ibexpay-api.readme.io/reference/getting-started-with-your-api).


### LNPay

För att Invoice-lyssnaren ska fungera har du en allmänt tillgänglig URL i din LNbits och måste ställa in en [LNPay webhook] (https://dashboard.lnpay.co/webhook/) som pekar på `<your LNbits host>/Wallet/webhook` med händelsen "Wallet Receive" och ingen hemlighet angiven. Inställningen `https://mylnbits/Wallet/webhook` kommer att vara slutpunktens url som får meddelande om alla betalningar.


  - `LNBITS_BACKEND_WALLET_CLASS`: **LNPayWallet**
  - `LNPAY_API_ENDPOINT`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - `LNPAY_WALLET_KEY`: waka_apiKey


### OpenNode

För att Invoice ska fungera måste du ha en allmänt tillgänglig URL i dina LNbits. Webhook-inställningen är valfri.


  - `LNBITS_BACKEND_WALLET_CLASS`: **OpenNodeplånbok**
  - `OPENNODE_API_ENDPOINT`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey


### Alby


Alby är ett webbläsartillägg med LN Wallet-funktioner och ett LNDHUB-konto som kan användas som finansieringskälla för LNbits. [Mer information här](https://getalby.com/).


För att Invoice ska fungera måste du ha en allmänt tillgänglig URL i dina LNbits. Ingen manuell webhook-inställning är nödvändig. Du kan generate en Alby-åtkomst token här: https://getalby.com/developer/access_tokens/new



- `LNBITS_BACKEND_WALLET_CLASS`: Alby Plånbok
- `ALBY_API_ENDPOINT`: https://api.getalby.com/
- `ALBY_ACCESS_TOKEN`: AlbyAccessToken


## Ytterligare / Felsökningsguider


Här är några ytterligare instruktioner ifall du skulle behöva dem. Klicka på pilen för att expandera beskrivningen.


### The Killswitch 🚨


Det har varit så många farliga buggar på sistone, inte bara i hela rymden utan även i LNbits, att vi bestämde oss för att göra något åt det. Du kan nu välja att få varningar och/eller vidta direkta åtgärder när en sårbarhet eller en bugg som kan leda till förlust av pengar inträffar igen.


![killswitchn](assets/lnbits-killswitch.webp)


Om du byter till void-Wallet kommer alla användartyper på instansen att se en gul banner där du normalt skulle hitta meddelandet "LNbits är i Beta" bredvid tema-/språkområdet uppe till höger - och det är den mest uppenbara ledtråden till att något har hänt. Ta en titt på din nya serverflik som är markerad med Green i den vänstra delen av fönstret.


Hur fungerar det här? När killswitch är aktiverad kommer ett hemligt github-arkiv som endast är tillgängligt för LNbits kärnteam att kontrolleras med ett intervall på X minuter (som kan anges). Om en sårbar bugg publiceras i detta arkiv fungerar det som en signal som utlöser killswitch på alla installationer som prenumererade och övergår din lnbits-instans för att använda void Wallet. Om molnen har skingrats och du har installerat säkerhetsuppdateringen kan du ställa in din finansieringskälla till din nod, Wallet eller vad du nu använder igen, även via avsnittet Manage Server. Denna wiki har ett avsnitt om att byta finansieringskällor om du inte vet vad du ska konfigurera.



### Skillnad mellan administratör och superanvändare


Med LNbits Admin UI kan du ändra LNbits-inställningar via LNbits frontend. Det är inaktiverat som standard och första gången du anger miljövariabeln `LNBITS_ADMIN_UI=true` i filen `.env` initieras inställningarna och kommer att användas. Från och med då används de motsvarande inställningarna från databasen istället för de i .env-filen.


### Superanvändare


Med Admin UI introducerade vi superanvändaren som har tillgång till servern så att den kan ändra inställningar som kan krascha servern eller göra att den inte svarar via frontend och api, som t.ex. att ändra finansieringskällan. Superanvändaren lagras endast i inställningstabellen i databasen. Efter att inställningarna har "återställts till standardvärdena" och startats om skapas en ny superanvändare. Vi har också lagt till en dekorator för API-vägarna för att kontrollera om det finns en superanvändare. Dess ID skickas aldrig över api och frontend och tar bara emot en bool (ja / nej) om du är superanvändare eller inte.


Endast superanvändaren får brrrrrr satoshis till olika plånböcker via avsnittet "Top Up".


Du kan också skicka superanvändaren via webhook till en annan tjänst när den skapas. Mer info här https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`


I frontend hittar du också möjligheten att ändra den butiksbild som visas på sidan "skapa Wallet" genom att öppna avsnittet Hantera server och välja Tema -> Anpassad logotyp.


### Admin användare


Miljövariabel: `LNBITS_ADMIN_USERS`, kommaseparerad lista med användar-ID. Admin-användare kan ändra inställningar i admin-användargränssnittet - med undantag för inställningar för finansieringskälla, eftersom detta skulle kräva en omstart av servern och potentiellt skulle kunna göra servern oåtkomlig. De har också tillgång till alla tillägg som är dedikerade till dem i `LNBITS_ADMIN_EXTENSIONS`.


### Tillåtna användare


Miljövariabel: `LNBITS_ALLOWED_USERS`, kommaseparerad lista med användar-ID. Genom att definiera dessa användare kommer LNbits inte längre att kunna användas av allmänheten. Endast definierade användare och administratörer kan då komma åt LNbits frontend.




#### Uppdatera LNbits

En normal uppdatering av din lokala LNbits-instans sker helt enkelt genom att kopiera och klistra in följande CLI-kommandon:


```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```


Om du kör Raspiblitz eller MyNode kan du dessutom behöva en

```
sudo systemctl restart lnbits
```

i slutet, eftersom det driver LNbits som en tjänst.


På Umbrel/Citadel skulle kommandona vara

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```


#### SQLite till PostgreSQL-migrering


Om du redan har LNbits installerat och kört på en SQLite-databas rekommenderar vi starkt att du migrerar till postgres om du planerar att köra LNbits i stor skala.


Det ingår ett skript som kan göra migreringen enkelt. Du måste redan ha Postgres installerat och det bör finnas ett lösenord för användaren (se installationsguiden för Postgres ovan). Dessutom måste din LNbits-instans köras en gång på postgres för att implementera databasen Schema innan migreringen kan fungera:


```
# STOP LNbits

# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit

# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

Förhoppningsvis fungerar nu allt och blir migrerat... Starta LNbits igen och kontrollera att allt fungerar som det ska.



#### Säkerhetskopiering och återställning av databasen


Se [denna mycket detaljerade guide om processen för säkerhetskopiering och återställning] (https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore).



#### Att finansiera min LNbits Wallet från min nod fungerar inte


Om du vill skicka Sats från samma nod som är finansieringskällan för dina LNbits måste du redigera filen LND.conf.


De parametrar som ska inkluderas är: `tillåt cirkulär rutt=1`


Gör det i avsnittet Application options i din LND.conf. På vissa bundle-noder kan starten av LND misslyckas annars.


OBS: Vi rekommenderar att du istället använder det nya adminUI-tillägget med alternativet "TopUp" för att lägga till pengar på ett LNbits-konto.


#### Fel 426

Jag fick felet: "lnurl måste levereras över offentligt tillgänglig https-domän eller tor. 426 uppgradering krävs"</summary>


Detta fel beror vanligtvis på att din LNbits bakom en ngnix-tunnel inte vidarebefordrar LNURL Address korrekt. Stoppa din LNbits och redigera .env-filen genom att lägga till denna rad:

`FORWARDED_ALLOW_IPS=*`


Om du använder en ngnix-installation måste du också se till att du har dessa rubriker i ngnix-konfigurationen:


```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```


#### Fel i nätverket

Jag fick "https-fel", nätverksfel" eller andra när jag skannade en QR</summary>


Dåliga nyheter, det här är ett routningsfel som kan ha ganska många orsaker. Kontrollera först QR: s LNURL med [Lightning Decoder] (https://lightningdecoder.com/) om du kan hitta något konstigt där. Låt oss prova några av de mest möjliga problemen och deras lösningar.


LNbits körs endast via Tor, du kan inte öppna den på en offentlig domän som lnbits.yourdomain.com



- Med tanke på att du vill att din inställning ska förbli så här öppnar du din LNbits Wallet med hjälp av .onion URI och skapar den igen. På detta sätt genereras QR för att vara tillgänglig via denna .onion URI så endast via tor. Gör inte generate den QR från en .local URI, eftersom den inte kommer att kunna nås via internet - bara från ditt hem-LAN.
- Öppna din LN Wallet-app som du använde för att skanna QR-koden och den här gången med hjälp av tor (se Wallet-appens inställningar). Om appen inte erbjuder tor kan du använda Orbot (Android) istället. Se installationsavsnittet för detaljerade instruktioner om hur du öppnar din LNbits för clearnet/https.



#### Förhindra andra från att generera plånböcker på mina LNbits


När du kör dina LNbits i clearnet kan i princip alla generate en Wallet på den. Eftersom pengarna i din nod är bundna till dessa plånböcker kanske du vill förhindra det. Det finns två sätt att göra det:


Konfigurera tillåtna användare och tillägg i filen `.env` ([se env-exemplet här](https://github.com/lnbits/lnbits/blob/main/.env.example)). Det här fungerar bara om du använder inställningen `adminUI=FALSE` i .env, annars måste du göra det i avsnittet Manage Server -> Users -> Allowed Users. Alla andra kommer inte att tillåtas efteråt.




#### Anpassa tidsramen för Invoice-utgången


Nu kan du generate-fakturor med ett anpassat utgångsdatum. Kompatibel med backends: LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet än så länge!


Du kan ställa in `LIGHTNING_INVOICE_EXPIRY` i din .env-fil eller använda AdminUI för att ändra standardvärdet för alla fakturor. Det finns också ett nytt fält i slutpunkten /api/v1/payments där du kan ange utgångsdatum i JSON-data.




## Wallet-URL raderad


### Wallet på demo-server legend.lnbits


Spara alltid en kopia av din Wallet-URL, Export2phone-QR eller LNDhub för dina egna plånböcker på en säker plats. LNbits kan INTE hjälpa dig att återfå dem om du förlorar dem.


### Wallet på egen finansieringskälla/nod

Spara alltid en kopia av din Wallet-URL, Export2phone-QR eller LNDhub för dina egna plånböcker på en säker plats. Du kan hitta alla LNbits-användare och Wallet-ID:n i ditt LNbits-tillägg för användarhanterare eller i din sqlite-databas. För att redigera eller läsa LNbits-databasen, gå till mappen LNbits /data och leta efter filen som heter sqlite.db. Du kan öppna och redigera den med Excel eller med en dedikerad SQL-Editor som [SQLite browser] (https://sqlitebrowser.org/).


Du kan också dumpa plånböckerna via CLI och visa alla Wallet i din databas.


```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```


Utdata kommer att se ut ungefär så här


```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

och du vill lägga in dessa värden i en webbadress så här


```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```


Därmed ersätter du f8a43fc363ea428db5c53b3559935f1f med det värde som kommer före namnet (i vårt exempel f8a43fc363ea428db5c53b3559935f1f) och 1280ff5910a9c485a782a2376f338b6c är din användare och bör bli det värde som visas efter namnet. För att avsluta sqlite3 skriv in


```
.quit
```

#### LNURL för en blixt-Address vice versa


Prova den här [encoder](https://lnurl-codec.netlify.app/) från fiatjaf eller [den här](https://lightningdecoder.com/). För att betala eller kontrollera en LNURLp kan du lika gärna använda [LNurlpay](https://wwww.lnurlpay.com/). Det ska stå HTTPS INTE HTTP.



#### Konfigurera en kommentar som folk ser när de betalar till min LNURLp QR

När du skapar en LNURL-p är kommentarsfältet som standard inte ifyllt. Det betyder att kommentarer inte får bifogas till betalningar.


För att tillåta kommentarer lägger du till teckenlängden på rutan, från 1 till 250. När du har lagt till en siffra där kommer kommentarrutan att visas i betalningsprocessen. Du kan också redigera en LNURL-p som redan skapats och lägga till det numret.


![lnbits comments](assets/lnbits-comments.webp)


#### Sätt in onchain BTC till LNbits

Det finns två sätt att Exchange Sats från onchain BTC till LN BTC (respektive till LNbits).


##### Via en extern bytestjänst.


Andra användare som inte har tillgång till din LNbits-instans kan använda en swapptjänst som [Boltz](https://boltz.Exchange/), [FixedFloat](https://fixedfloat.com/), [DiamondHands](https://swap.diamondhands.technology/) eller [ZigZag](https://zigzag.io/). Detta är användbart om du endast tillhandahåller LNURL/LN-fakturor från din LNbits-instans, men en betalare endast har Sats i kedjan, så de måste byta dessa Sats först på sin sida. Förfarandet är enkelt: användaren skickar onchain btc till swap-tjänsten och tillhandahåller LNURL / LN Invoice från LNbits som destination för swapet.


##### Med hjälp av Onchain och Boltz LNbits-tillägget.


Tänk på att detta är en separat Wallet, inte den LN btc som representeras av LNbits som "din Wallet" på din LN-finansieringskälla. Denna Wallet på kedjan kan också användas för att växla LN btc till (t.ex. din hårdvaruplånbok) genom att använda LNbits Boltz- eller Deezy-tillägget. Om du driver en webbshop som är länkad till din LNbits för LN-betalningar, är det mycket praktiskt att regelbundet tömma alla Sats från LN till onchain. Detta leder till mer utrymme i dina LN-kanaler för att kunna ta emot nya färska Sats.


Procedur för dem som inte har en Bitcoin Hardware Wallet:



- Använd Electrum eller Sparrow wallet för att skapa en ny onchain Wallet och spara säkerhetskopian seed på en säker plats.
- Gå till Wallet information och kopiera xpuben.
- Gå till LNbits - Onchain-tillägg och skapa en ny Watch-only wallet med den xpuben.
- Gå till LNbits - Tipjar-tillägg och skapa en ny Tipjar. Välj också onchain-alternativet förutom LN Wallet.
- Valfritt - Gå till LNbits - SatsPay-tillägget och skapa en ny avgift för onchain btc. Du kan välja mellan onchain och LN eller båda. Det kommer då att skapa en Invoice som kan delas.
- Valfritt - Om du använder dina LNbits länkade till en Wordpress + Woocommerce-sida, när du skapar / länkar en Watch-only wallet till din LN btc-butik Wallet, kommer kunden att ha båda alternativen att betala på samma skärm.


När du tar emot en betalning i LNbits kommer transaktionsloggen endast att visa en återupptagen typ av transaktion.


![lnbits payment details](assets/lnbits-payment-details.webp)


I din transaktionsöversikt hittar du en liten Green-pil för mottagna och en röd pil för de medel som skickas.


Om du klickar på pilarna visas bifogade meddelanden och avsändarens namn om det finns angivet.


För att konfigurera ett namn som ska visas i betalningar är det för närvarande inte möjligt att göra detta i LNbits - men att ta emot det. Detta är endast möjligt om avsändarens LN Wallet stöder [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) som [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents).


Du kommer då att se ett alias/pseudonym i detaljavsnittet för dina LNbits-transaktioner (klicka på pilarna). Observera att du kan ange vilket namn som helst där och att det kanske inte är relaterat till den verkliga avsändarens namn om du får ett sådant.


![lnbits namedesc](assets/lnbits-namedesc.webp)


För att importera ditt LNbits-konto i en Wallet-app, öppna din LNbits med det konto/Wallet du vill använda, gå till "hantera tillägg" och aktivera LNDHUB-tillägget. Öppna LNDHUB-tillägget, välj den Wallet som du vill använda och skanna antingen QR:n "admin" eller "endast Invoice", beroende på vilken säkerhetsnivå du vill ha för den Wallet.


Du kan använda [Zeus](https://zeusln.app/) eller [Bluewallet](https://bluewallet.io/) som Wallet-appar för ett lndhub-konto där BW stöder mer än en sådan Wallet.


När du gör detta rekommenderar vi att du också ställer in LN-nätverkets URI till den för din egen nod. Om din LNbits-instans endast är Tor måste du också använda dessa appar med Tor aktiverat. Även i detta fall måste du öppna LNbits-sidan via din Tor .onion Address.


Om du har ett fel "unsupported Hash type" när du använder en ypub i On-Chain-tillägget, kontrollera om din LNbits-instans använder python 3.10, det kan påverkas av [detta problem] (https://stackoverflow.com/questions/72409563/unsupported-Hash-type-ripemd160-with-hashlib-in-python). Redigera openssl.cnf enligt beskrivningen i stackoverflow-svaret och starta om LNbits.



## Verktyg och konstruktion med LNbits


LNbits har alla möjliga [öppna API:er] (https://legend.lnbits.com/docs) och verktyg för att programmera och ansluta till en mängd olika enheter för en miljard olika användningsområden.


Om du är nybörjare kan du börja med denna [MakerBits-presentationer] (https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) från Ben Arc om att bygga prylar baserade på LNbits.


### VIKTIGT:


- LNbits fungerar baserat på LNURL-protokollet, där förfrågningar är giltiga i två former: antingen som https:// clearnet-länk (inga självsignerade certifikat tillåtna) eller som http:// v2/v3 onion-länk. För att erbjuda LNbits-tjänster som LNURLp/w QR-koder eller NFC-kort, som kan användas i naturen, måste du öppna LNbits för clearnet (https).
- Använd endast DATA-kablar för att driva din esp32. Inte alla kablar stöder data utöver att driva esp. Du skulle inte vara den första om kabeln som följde med esp är en endast ström
- Se till att inte använda en USB-hubb med andra enheter anslutna. Detta kan leda till konstiga effekter som är Hard svåra att felsöka (t.ex. att enheten inte startar eller stannar).
- För att realisera esp-projekt med MacOS behöver du en UART Bridge-drivrutin. Om du har problem med drivrutinen på Mac- eller Linux-system kan du hitta dem här eller, om en TTGO-skärm är inblandad, den här. Om du är på Windows och har problem med att ansluta, se till att ladda ner den OLD-versionen 11.1.0 eftersom den nyare inte fungerar! Du kan också hitta en seriell terminal här för att kontrollera din anslutning - inställd på baudrate 115200.
- Även om det är mycket bekvämare att använda Platform.io (t.ex. installeras beroenden automatiskt) rekommenderar vi att du använder Arduino för alla som är nya inom byggbranschen.
- TT-Go Display S3: Färgen på fliken på skärmskyddsfilmen berättar exakt vilken styrenhet (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ...) som har använts för att bygga den. Behåll den för att kunna felsöka om du programmerar dig själv och skärmen inte visar grafik korrekt, t.ex. fel färger, spegelvända bilder eller pixlar i kanterna. Om du någonsin behöver göra detta finns det en episk guide om hur du justerar för olika skärmar
- Använd alltid små bokstäver lnurl239xx istället för LNURLl239xx
- Genom att lägga till lightning:lnurl1234xyz skapas en QR som begär att öppna användarens Wallet för denna Invoice vid skanning (senast installerade lightning-app på iOS, inställning i Android)
- Om du flashar en esp32 via webben fungerar det bara med dessa webbläsare (TL:DR Chrome, Edge & Opera).
- Observera denna PIN-OUT-referens för esp
- När du använder FOSSoftware eller FOSGuides, vänligen länka alltid författaren. Alla älskar att se sitt barn växa och det initierar också en byggkedja som är ganska fantastisk att se :)


Kom till [Makerbits Telegram Group] (https://t.me/makerbits) om du behöver hjälp med ett projekt - vi har dig!


![lnbits hackathlon](assets/lnbits-hackathlon.webp)


Här är några projektkategorier som du kan bygga med LNbits:



- [Nostr Signing Device](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Archade Machine] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Nostr Zap Lamp] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Lightning Piggy] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Hardware Wallet] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-Wallet)
- [Bitcoin Switch] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Bitcoin-switch)
- [Varuautomat] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin Ticker] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Bitcoin-ticker)
- [BTClock] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [Lora and Mesh Networking] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)



- [HJÄLPMEDEL & RESURSER](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [Fler exempel på projekt "Powered by LNbits" här] (https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits).
- [Användningsfall för LNbits] (https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)