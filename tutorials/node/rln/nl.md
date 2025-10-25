---
name: RGB Lightning Node
description: Hoe lanceer ik een RGB-compatibel Lightning-knooppunt met RLN?
---
![cover](assets/cover.webp)


In deze stap-voor-stap tutorial leer je hoe je een Lightning RGB node opzet op een Regtest omgeving. We zullen zien hoe je RGB tokens aanmaakt en laat circuleren in kanalen.


## Het RLN-project


Het RGB-team van Bitfinex werkt sinds 2022 aan de verrijking van het RGB-ecosysteem door een complete technologiestack te ontwikkelen. In plaats van te streven naar één commercieel product, zijn de inspanningen gericht op het beschikbaar maken van open-source softwarebricks, het bijdragen aan RGB protocol specificaties en het creëren van implementatiereferenties.


Een van de opmerkelijke bijdragen van Bitfinex aan het RGB ecosysteem is [de *RGBlib* bibliotheek](https://github.com/RGB-Tools/RGB-lib), geschreven in Rust en toegankelijk via bindingen in Kotlin en Python, die de ontwikkeling van RGB toepassingen sterk vereenvoudigt door complexe validatie- en engagementmechanismen in te kapselen.


Het Bitfinex-team heeft ook een RGB mobiele Wallet ontworpen, genaamd "[*Iris Wallet*](https://iriswallet.com/)", beschikbaar op Android. Deze Wallet integreert het gebruik van een RGB proxyserver om eenvoudig off-chain gegevensuitwisselingen (*consignments*) te beheren voor *Client-side Validation* op RGB.


Bitfinex heeft ook het `RGB-lightning-node` (RLN) project ontwikkeld. Dit is een Rust daemon gebaseerd op een Fork van `Rust-lightning` (LDK), aangepast om rekening te houden met het bestaan van RGB activa in een kanaal. Wanneer een kanaal wordt geopend, kan de aanwezigheid van RGB tokens worden gespecificeerd, en elke keer als de toestand van het kanaal wordt bijgewerkt, wordt een State Transition aangemaakt die de verdeling van tokens in Lightning-uitgangen weergeeft. Dit maakt :




- Open bijvoorbeeld Lightning-kanalen in USDT;
- Routeer deze tokens door het netwerk, op voorwaarde dat de routepaden voldoende liquiditeit hebben;
- Gebruik de straf- en tijdslotlogica van Lightning zonder wijzigingen: gewoon Anchor de RGB overgang in een extra uitgang van de Commitment Transaction.


De RLN code is nog in het alfa stadium: we raden aan om het alleen te gebruiken in **regtest** of op de **Testnet**.


## Herinnering RGB protocol


RGB is een protocol dat bovenop Bitcoin draait en Smart contract functionaliteit en digitaal activabeheer emuleert, zonder Blockchain waarop het gebaseerd is te overbelasten. In tegenstelling tot conventionele On-Chain smart contracts (zoals bijvoorbeeld op Ethereum), vertrouwt RGB op een "*Client-side Validation*" systeem: de meeste gegevens en statusgeschiedenissen worden uitsluitend uitgewisseld en opgeslagen door de betrokken deelnemers, terwijl Bitcoin Blockchain alleen kleine cryptografische verbintenissen herbergt (via mechanismen zoals *Tapret* of *Opret*). In het RGB protocol dient Bitcoin Blockchain daarom alleen als tijdstempelserver en Double-spending beveiligingssysteem.


Een RGB Contract is gestructureerd als een evolutionaire toestandsmachine. Het begint met een Genesis die de begintoestand definieert (die bijvoorbeeld de Supply, ticker of andere metadata beschrijft) volgens een strikt getypeerde en gecompileerde Schema. Toestandsovergangen en, indien nodig, toestandsuitbreidingen worden dan toegepast om deze toestand te wijzigen of uit te breiden. Elke bewerking, of het nu gaat om het overbrengen van fungibele activa (RGB20) of het creëren van unieke activa (RGB21), heeft te maken met *eenmalige verzegelingen*. Deze verbinden Bitcoin UTXO's met off-chain staten en voorkomen dubbele uitgaven, terwijl ze vertrouwelijkheid en schaalbaarheid garanderen.


Om meer te leren over hoe het RGB protocol werkt, raad ik je aan deze uitgebreide training te volgen:


https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

## RGB-compatibele installatie van Lightning-knooppunten


Om de `RGB-lightning-node` binary te compileren en installeren, beginnen we met het klonen van het archief en de submodules, daarna draaien we de :


```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```


![RLN](assets/fr/01.webp)




- De `--recurse-submodules` optie kloont ook de benodigde sub-devices (inclusief de gewijzigde versie van `Rust-lightning`);
- De `--shallow-submodules` optie beperkt de diepte van de kloon om het downloaden te versnellen, terwijl het nog steeds toegang geeft tot essentiële commits.


Voer vanuit de project root het volgende commando uit om de binary :


```bash
cargo install --locked --debug --path .
```


![RLN](assets/fr/02.webp)




- `--locked` zorgt ervoor dat de versie van afhankelijkheden wordt gerespecteerd;
- `--debug` is niet verplicht, maar kan je helpen focussen (je kunt `--release` gebruiken als je dat liever hebt) ;
- `--path .` vertelt `cargo install` om te installeren vanuit de huidige map.


Aan het einde van dit commando zal een `RGB-lightning-node` executable beschikbaar zijn in je `$CARGO_HOME/bin/`. Zorg ervoor dat dit pad in je `$PATH` staat zodat je het commando vanuit elke map kunt aanroepen.


## Vereisten


Om te kunnen functioneren, heeft de `RGB-lightning-node` daemon de aanwezigheid en configuratie nodig van :




- Een `bitcoind`** knooppunt


Elke RLN instantie moet communiceren met `bitcoind` om zijn On-Chain transacties uit te zenden en te monitoren. Authenticatie (login/wachtwoord) en URL (host/poort) moeten aan de daemon worden verstrekt.




- Een indexer** (Electrum of Esplora)


De daemon moet On-Chain transacties kunnen weergeven en onderzoeken, in het bijzonder om de UTXO te vinden waarop een activum is verankerd. Je moet de URL van je Electrum server of Esplora specificeren.




- Een RGB** proxy


De proxyserver is een component (optioneel, maar ten zeerste aanbevolen) om de Exchange van RGB *opdrachten* tussen Lightning peers te vereenvoudigen. Ook hier moet een URL worden opgegeven.


ID's en URL's worden ingevoerd wanneer de daemon wordt *ontgrendeld* via de API.


## Start Regtest


Voor eenvoudig gebruik is er een `regtest.sh` script dat automatisch, via Docker, een set services start: `bitcoind`, `electrs` (indexer), `RGB-proxy-server`.


![RLN](assets/fr/03.webp)


Hiermee kun je een lokale, geïsoleerde, vooraf geconfigureerde omgeving starten. Het creëert en vernietigt containers en datamappen bij elke herstart. We beginnen met het starten van de :


```bash
./regtest.sh start
```


Dit script zal :




- Maak een `docker/` map om ;
- Voer `bitcoind` uit in regtest, evenals de indexer `electrs` en de `RGB-proxy-server` ;
- Wacht tot alles klaar is voor gebruik.


![RLN](assets/fr/04.webp)


Vervolgens zullen we verschillende RLN nodes starten. Voer in aparte shells bijvoorbeeld (om 3 RLN nodes te starten) :


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




- De `--netwerk regtest` parameter geeft het gebruik van de regtest configuratie aan;
- `--daemon-luisteren-poort` geeft aan op welke REST-poort het Lightning knooppunt zal luisteren voor API-aanroepen (JSON);
- `--ldk-peer-listening-port` specificeert op welke Lightning P2P poort geluisterd moet worden;
- `dataldk0/`, `dataldk1/` zijn de paden naar de opslagmappen (elk knooppunt slaat zijn info apart op).


Je kunt nu commando's uitvoeren op je RLN nodes vanuit je browser, dankzij de API. Dit is in het bijzonder waar je daemons kunt *unlocken*. Open gewoon een browser op dezelfde computer als je nodes en voer de URL :


```url
https://rgb-tools.github.io/rgb-lightning-node/
```


Om een kanaal te kunnen openen, moet een node eerst bitcoins hebben op een Address die met het volgende commando is gegenereerd (bijvoorbeeld voor node n°1):


```bash
curl -X POST http://localhost:3001/address
```


Het antwoord geeft je een Address.


![RLN](assets/fr/06.webp)


Op de `bitcoind` Regtest gaan we een paar bitcoins delven. Uitvoeren :


```bash
./regtest.sh mine 101
```


![RLN](assets/fr/07.webp)


Stuur fondsen naar het hierboven gegenereerde knooppunt Address:


```bash
./regtest.sh sendtoaddress <address> <amount>
```


![RLN](assets/fr/08.webp)


Mijn dan een blok om de transactie te bevestigen:


```bash
./regtest.sh mine 1
```


![RLN](assets/fr/09.webp)


## Testnet lancering (zonder Docker)


Als je een realistischer scenario wilt testen, kun je RLN nodes lanceren op de Testnet in plaats van in Regtest, wijzend naar publieke diensten of diensten die je beheert:


```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```


Als er standaard geen configuratie wordt gevonden, probeert de daemon de :




- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-RPC`


Met login :




- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `wachtwoord`


Je kunt deze Elements ook aanpassen via de `init`/`unlock` API.


## Uitgifte van een RGB token


Om een token uit te geven, beginnen we met het maken van "kleurbare" UTXO's:


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


Je kunt de bestelling natuurlijk aanpassen. Om de transactie te bevestigen, mijnen we een :


```bash
./regtest.sh mine 1
```


We kunnen nu een RGB bron aanmaken. Het commando hangt af van het type asset dat je wilt maken en de parameters. Hier maak ik een NIA (*Non Inflatable Asset*) token genaamd "PBN" met een Supply van 1000 eenheden. Met `precision` kun je de deelbaarheid van de eenheden bepalen.


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


Het antwoord bevat de ID van het nieuw aangemaakte onderdeel. Vergeet niet om deze identificatie te noteren. In mijn geval is het :


```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```


![RLN](assets/fr/12.webp)


Je kunt het dan On-Chain overbrengen, of toewijzen in een Lightning-kanaal. Dat is precies wat we gaan doen in de volgende sectie.


## Een kanaal openen en een RGB bedrijfsmiddel overdragen


Je moet eerst je knooppunt verbinden met een peer op de Lightning Network met het `/connectpeer` commando. In mijn voorbeeld bestuur ik beide knooppunten. Dus ik vraag de openbare sleutel op van mijn tweede Lightning-knooppunt met dit commando:


```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```


Het commando geeft de openbare sleutel van mijn knooppunt nr. 2 :


```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```


![RLN](assets/fr/13.webp)


Vervolgens openen we het kanaal door de relevante asset (`PBN`) te specificeren. Met het `/openkanaal` commando kun je de grootte van het kanaal in satoshis definiëren en ervoor kiezen om het RGB asset toe te voegen. Het hangt af van wat je wilt maken, maar in mijn geval is het commando :


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


Lees hier meer:




- `peer_pubkey_en_opt_addr`: Identificatie van de peer waarmee we willen verbinden (de publieke sleutel die we eerder hebben gevonden);
- capaciteit_sat`: Totale kanaalcapaciteit in satoshis ;
- `push_msat`: Bedrag in millisatoshis dat in eerste instantie wordt overgemaakt naar de peer wanneer het kanaal wordt geopend (hier maak ik direct 10.000 Sats over zodat hij later RGB kan overmaken) ;
- `asset_amount`: Bedrag aan RGB activa dat moet worden toegewezen aan het kanaal ;
- `asset_id` : Unieke identificatie van het RGB activum dat betrokken is bij het kanaal;
- `public`: Geeft aan of het kanaal openbaar moet worden gemaakt voor routering op het netwerk.


![RLN](assets/fr/14.webp)


Om de transactie te bevestigen, worden 6 blokken gedolven:


```bash
./regtest.sh mine 6
```


![RLN](assets/fr/15.webp)


Het Lightning-kanaal is nu open en bevat ook 500 `PBN`-tokens aan de kant van knooppunt n°1. Als knooppunt n°2 `PBN` tokens wil ontvangen, moet het generate en Invoice. Zo doe je dat:


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


Met :




- `amt_msat`: Invoice hoeveelheid in millisatoshis (minimaal 3000 Sats) ;
- `expiry_sec` : Invoice vervaltijd in seconden ;
- `asset_id` : Identificatie van het RGB activum geassocieerd met de Invoice ;
- `asset_amount`: Bedrag aan RGB activa dat moet worden overgedragen met deze Invoice.


Als antwoord krijg je een RGB Invoice:


```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```


![RLN](assets/fr/16.webp)


We zullen deze Invoice nu betalen vanaf het eerste knooppunt, dat het benodigde geld heeft met de `PBN` token:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```


![RLN](assets/fr/17.webp)


De betaling is uitgevoerd. Dit kan worden geverifieerd door het commando :


```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```


![RLN](assets/fr/18.webp)


Dit is hoe je een Lightning-knooppunt kunt inzetten dat is aangepast om RGB goederen te vervoeren. Deze demonstratie is gebaseerd op :




- Een regtest-omgeving (via `./regtest.sh`) of Testnet ;
- Een Lightning-node (`RGB-lightning-node`) gebaseerd op een `bitcoind`, een indexer en een `RGB-proxy-server` ;
- Een reeks JSON REST API's voor het openen/sluiten van kanalen, het uitgeven van tokens, het overdragen van activa via Lightning, enz.


Dankzij dit proces :




- Lightning engagement transacties bevatten een extra uitgang (OP_RETURN of Taproot) met de verankering van een RGB overgang;
- Overschrijvingen gebeuren op precies dezelfde manier als traditionele Lightning-betalingen, maar met de toevoeging van een RGB token;
- Meerdere RLN-knooppunten kunnen worden gekoppeld om betalingen over meerdere knooppunten te routeren en ermee te experimenteren, op voorwaarde dat er voldoende liquiditeit is in zowel bitcoins als activa RGB op het pad.


Als je deze tutorial nuttig vond, zou ik je erg dankbaar zijn als je hieronder een Green duim plaatst. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!


Ik raad ook deze andere tutorial aan waarin ik uitleg hoe je de RGB CLI tool, ontwikkeld door de LNP/BP vereniging, kunt gebruiken om een RGB Contract te maken:


https://planb.network/tutorials/node/others/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4