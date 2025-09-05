---
name: RGB Blixtnod
description: Hur startar jag en RGB-kompatibel Lightning-nod med RLN?
---
![cover](assets/cover.webp)


I denna steg-för-steg-handledning lär du dig hur du ställer in en Lightning RGB-nod i en Regtest-miljö. Vi kommer att se hur man skapar RGB-tokens och cirkulerar dem i kanaler.


## RLN-projektet


Bitfinex RGB-team har arbetat sedan 2022 för att berika RGB-ekosystemet genom att utveckla en komplett teknikstack. I stället för att sikta på en enda kommersiell produkt fokuserar man på att göra programvarublock med öppen källkod tillgängliga, bidra till RGB-protokollspecifikationer och skapa implementeringsreferenser.


Bland Bitfinex anmärkningsvärda bidrag till RGB-ekosystemet är [the *RGBlib* library] (https://github.com/RGB-Tools/RGB-lib), skrivet i Rust och tillgängligt via bindningar i Kotlin och Python, vilket förenklar utvecklingen av RGB-applikationer genom att kapsla in komplexa validerings- och engagemangsmekanismer.


Bitfinex-teamet har också utformat en RGB mobil Wallet, kallad "[*Iris Wallet*] (https://iriswallet.com/)", tillgänglig på Android. Denna Wallet integrerar användningen av en RGB-proxyserver för att enkelt hantera off-chain-datautbyten (*sändningar*) för *Client-side Validation* på RGB.


Bitfinex har också utvecklat projektet `RGB-lightning-node` (RLN). Detta är en Rust daemon baserad på en Fork av `Rust-lightning` (LDK), modifierad för att ta hänsyn till förekomsten av RGB-tillgångar i en kanal. När en kanal öppnas kan förekomsten av RGB-tokens specificeras, och varje gång kanaltillståndet uppdateras skapas en State Transition som återspeglar fördelningen av tokens i Lightning-utgångar. Detta möjliggör :




- Öppna blixtkanaler i USDT, till exempel;
- Dirigera dessa tokens genom nätverket, förutsatt att dirigeringsvägarna har tillräcklig likviditet;
- Utnyttja Lightnings bestraffnings- och tidslåsningslogik utan modifiering: helt enkelt Anchor RGB-övergången i en extra utgång från Commitment Transaction.


RLN-koden är fortfarande i sitt alfa-stadium: vi rekommenderar att du endast använder den i **regtest** eller på **Testnet**.


## Påminnelse om RGB-protokollet


RGB är ett protokoll som körs ovanpå Bitcoin och emulerar Smart contract-funktionalitet och digital tillgångshantering, utan att överbelasta Blockchain som det är baserat på. Till skillnad från konventionella On-Chain smarta kontrakt (som till exempel på Ethereum) förlitar sig RGB på ett "* Client-side Validation*"-system: majoriteten av data och statushistorik utbyts och lagras uteslutande av de inblandade deltagarna, medan Bitcoin Blockchain endast är värd för små kryptografiska åtaganden (via mekanismer som *Tapret* eller *Opret*). I RGB-protokollet fungerar Bitcoin Blockchain därför endast som en tidsstämplingsserver och Double-spending-skyddssystem.


En RGB Contract är strukturerad som en evolutionär tillståndsmaskin. Den börjar med en Genesis som definierar det initiala tillståndet (som t.ex. beskriver Supply, ticker eller andra metadata) enligt en strikt typad och sammanställd Schema. Tillståndsövergångar och, om nödvändigt, tillståndsutvidgningar tillämpas sedan för att modifiera eller utöka detta tillstånd. Varje operation, oavsett om det gäller överföring av fungibla tillgångar (RGB20) eller skapande av unika tillgångar (RGB21), omfattar *Single-use Seals*. Dessa länkar Bitcoin UTXO:er till off-chain-stater och förhindrar dubbla utgifter, samtidigt som de säkerställer sekretess och skalbarhet.


Om du vill lära dig mer om hur RGB-protokollet fungerar rekommenderar jag att du går den här omfattande utbildningen:


https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

## RGB-kompatibel installation av blixtnod


För att kompilera och installera binärfilen `RGB-lightning-node` börjar vi med att klona förvaret och dess undermoduler, sedan kör vi :


```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```


![RLN](assets/fr/01.webp)




- Alternativet `--recurse-submodules` klonar också de nödvändiga underenheterna (inklusive den modifierade versionen av `Rust-lightning`);
- Alternativet `--shallow-submodules` begränsar klonens djup för att påskynda nedladdningen, samtidigt som det ger tillgång till viktiga åtaganden.


Från projektets rot kör du följande kommando för att kompilera och installera den binära :


```bash
cargo install --locked --debug --path .
```


![RLN](assets/fr/02.webp)




- `--locked` säkerställer att versionen av beroenden respekteras;
- `--debug` är inte obligatoriskt, men kan hjälpa dig att fokusera (du kan använda `--release` om du föredrar det) ;
- `--path .` säger till `cargo install` att installera från den aktuella katalogen.


I slutet av detta kommando kommer en körbar `RGB-lightning-node` att finnas tillgänglig i din `$CARGO_HOME/bin/`. Se till att den här sökvägen finns i din `$PATH` så att du kan anropa kommandot från vilken katalog som helst.


## Förkunskapskrav


För att fungera behöver `RGB-lightning-node` daemon närvaro och konfiguration av :




- En `bitcoind`** nod


Varje RLN-instans kommer att behöva kommunicera med `bitcoind` för att sända och övervaka sina On-Chain-transaktioner. Autentisering (inloggning/lösenord) och URL (host/port) måste tillhandahållas till daemon.




- En indexerare** (Electrum eller Esplora)


daemon måste kunna lista och utforska On-Chain-transaktioner, i synnerhet för att hitta den UTXO som en tillgång har förankrats på. Du måste ange webbadressen till din Electrum-server eller Esplora.




- En proxy RGB**


Proxyservern är en komponent (valfri, men rekommenderas starkt) för att förenkla Exchange av RGB *sändningar* mellan Lightning-peers. Återigen måste en URL anges.


ID:n och URL:er anges när daemon *låser upp* via API:et.


## Regtest lansering


För enkel användning finns det ett skript `regtest.sh` som automatiskt startar, via Docker, en uppsättning tjänster: `bitcoind`, `electrs` (indexerare), `RGB-proxy-server`.


![RLN](assets/fr/03.webp)


Detta gör att du kan starta en lokal, isolerad och förkonfigurerad miljö. Den skapar och förstör behållare och datakataloger vid varje omstart. Vi börjar med att starta :


```bash
./regtest.sh start
```


Detta skript kommer att :




- Skapa en `docker/`-katalog för att lagra ;
- Kör `bitcoind` i regtest, liksom indexeraren `electrs` och `RGB-proxy-servern` ;
- Vänta tills allt är klart att använda.


![RLN](assets/fr/04.webp)


Nu ska vi starta flera RLN-noder. I separata skal kör du till exempel (för att starta 3 RLN-noder) :


```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```


![RLN](assets/fr/05.webp)




- Parametern `--network regtest` anger att konfigurationen regtest ska användas;
- `--daemon-listening-port` anger på vilken REST-port Lightning-noden kommer att lyssna på API-anrop (JSON);
- `--ldk-peer-listening-port` anger vilken Lightning P2P-port som ska lyssna på;
- `dataldk0/`, `dataldk1/` är sökvägarna till lagringskatalogerna (varje nod lagrar sin information separat).


Du kan nu utföra kommandon på dina RLN-noder från din webbläsare, tack vare API:et. I synnerhet är det här du kan *låsa upp* daemons. Öppna helt enkelt en webbläsare på samma dator som dina noder och ange URL:en :


```url
https://rgb-tools.github.io/rgb-lightning-node/
```


För att en nod ska kunna öppna en kanal måste den först ha bitcoins på en Address som genererats med följande kommando (till exempel för nod nr 1):


```bash
curl -X POST http://localhost:3001/address
```


Svaret kommer att ge dig en Address.


![RLN](assets/fr/06.webp)


På `bitcoind` Regtest, kommer vi att bryta några bitcoins. Kör :


```bash
./regtest.sh mine 101
```


![RLN](assets/fr/07.webp)


Skicka pengar till noden Address som genererats ovan:


```bash
./regtest.sh sendtoaddress <address> <amount>
```


![RLN](assets/fr/08.webp)


Minera sedan ett block för att bekräfta transaktionen:


```bash
./regtest.sh mine 1
```


![RLN](assets/fr/09.webp)


## Lansering av Testnet (utan Docker)


Om du vill testa ett mer realistiskt scenario kan du starta RLN-noder på Testnet i stället för i Regtest och peka på offentliga tjänster eller tjänster som du kontrollerar:


```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```


Om ingen konfiguration hittas kommer daemon som standard att försöka använda :




- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332``
- indexer_url`: `ssl://electrum.iriswallet.com:50013``
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-RPC``


Med inloggning :




- `bitcoind_rpc_username`: `användare`
- `bitcoind_rpc_username`: `lösenord`


Du kan också anpassa dessa Elements via API:et `init`/`unlock`.


## Utfärdande av en RGB token


För att utfärda en token börjar vi med att skapa "färgbara" UTXO: er:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```


![RLN](assets/fr/10.webp)


Du kan naturligtvis anpassa beställningen. För att bekräfta transaktionen, min vi en :


```bash
./regtest.sh mine 1
```


Vi kan nu skapa en RGB-tillgång. Kommandot beror på vilken typ av tillgång du vill skapa och dess parametrar. Här skapar jag en NIA (*Non Inflatable Asset*) token med namnet "PBN" med en Supply på 1000 enheter. Med `precision` kan du definiera enheternas delbarhet.


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```


![RLN](assets/fr/11.webp)


Svaret innehåller ID för den nyligen skapade tillgången. Kom ihåg att notera denna identifierare. I mitt fall är det :


```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```


![RLN](assets/fr/12.webp)


Du kan sedan överföra den On-Chain, eller allokera den i en Lightning-kanal. Det är precis vad vi ska göra i nästa avsnitt.


## Öppna en kanal och överföra en RGB-tillgång


Du måste först ansluta din nod till en peer på Lightning Network med hjälp av kommandot `/connectpeer`. I mitt exempel kontrollerar jag båda noderna. Så jag hämtar den publika nyckeln för min andra Lightning-nod med det här kommandot:


```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```


Kommandot returnerar den publika nyckeln för min nod nr 2 :


```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```


![RLN](assets/fr/13.webp)


Därefter öppnar vi kanalen genom att ange den relevanta tillgången (`PBN`). Med kommandot `/openchannel` kan du definiera storleken på kanalen i satoshis och välja att inkludera RGB-tillgången. Det beror på vad du vill skapa, men i mitt fall är kommandot :


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```


Läs mer om detta här:




- `peer_pubkey_och_opt_addr`: Identifierare för den peer som vi vill ansluta till (den publika nyckel som vi hittade tidigare);
- kapacitet i sat: Total kanalkapacitet i satoshis ;
- `push_msat`: Belopp i millisatoshis som initialt överförs till motparten när kanalen öppnas (här överför jag omedelbart 10 000 Sats så att han kan göra en RGB-överföring senare) ;
- `tillgång_belopp`: Mängden RGB-tillgångar som ska överföras till kanalen ;
- `asset_id` : Unik identifierare för den RGB-tillgång som är engagerad i kanalen;
- "Offentlig": Anger om kanalen ska göras offentlig för routing i nätverket.


![RLN](assets/fr/14.webp)


För att bekräfta transaktionen bryts 6 block:


```bash
./regtest.sh mine 6
```


![RLN](assets/fr/15.webp)


Lightning-kanalen är nu öppen och innehåller också 500 `PBN`-tokens på nod n°1:s sida. Om nod n°2 vill ta emot `PBN`-tokens måste den generate och Invoice. Så här gör du för att göra det:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```


Med :




- `amt_msat`: Invoice-belopp i millisatoshis (minst 3000 Sats) ;
- `expiry_sec` : Invoice utgångstid i sekunder ;
- `asset_id` : Identifierare för den RGB-tillgång som är associerad med Invoice ;
- `tillgång_belopp`: Beloppet för den RGB-tillgång som ska överföras med denna Invoice.


Som svar får du en RGB Invoice:


```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```


![RLN](assets/fr/16.webp)


Vi kommer nu att betala denna Invoice från den första noden, som har de nödvändiga kontanterna med `PBN` token:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```


![RLN](assets/fr/17.webp)


Betalning har gjorts. Detta kan verifieras genom att köra kommandot :


```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```


![RLN](assets/fr/18.webp)


Så här sätter du in en Lightning-nod som modifierats för att bära RGB-tillgångar. Denna demonstration är baserad på :




- En regtest-miljö (via `./regtest.sh`) eller Testnet ;
- En Lightning-nod (`RGB-lightning-node`) baserad på en `bitcoind`, en indexerare och en `RGB-proxy-server` ;
- En serie JSON REST API:er för att öppna/stänga kanaler, utfärda tokens, överföra tillgångar via Lightning etc.


Tack vare denna process :




- Lightning engagement-transaktioner inkluderar en ytterligare utgång (OP_RETURN eller Taproot) med förankring av en RGB-övergång;
- Överföringar görs på exakt samma sätt som traditionella Lightning-betalningar, men med tillägg av en RGB token;
- Flera RLN-noder kan kopplas samman för att dirigera och experimentera med betalningar över flera noder, förutsatt att det finns tillräcklig likviditet i både bitcoins och tillgången RGB på vägen.


Om du tyckte att denna handledning var användbar skulle jag vara mycket tacksam om du sätter en Green-tumme nedan. Du är välkommen att dela den här artikeln på dina sociala nätverk. Tack så mycket!


Jag rekommenderar också den här andra handledningen där jag förklarar hur man använder RGB CLI-verktyget som utvecklats av LNP/BP-föreningen för att skapa en RGB Contract:


https://planb.network/tutorials/node/others/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4