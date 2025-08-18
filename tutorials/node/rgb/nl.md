---
name: RGB
description: Inleiding en aanmaken van activa op RGB
---

![RGB vs Ethereum](assets/0.webp)


## inleiding


Op 3 januari 2009 lanceerde Satoshi Nakamoto de eerste Bitcoin node, vanaf dat moment sloten nieuwe nodes zich aan en begon Bitcoin zich te gedragen alsof het een nieuwe levensvorm was, een levensvorm die niet gestopt is met evolueren, beetje bij beetje is het het veiligste netwerk ter wereld geworden als gevolg van het unieke ontwerp, zeer goed uitgedacht door Satoshi, omdat het door middel van economische prikkels gebruikers, gewoonlijk miners genoemd, aantrekt om te investeren in energie en rekenkracht, wat bijdraagt aan de veiligheid van het netwerk.


Naarmate Bitcoin verder groeit en wordt overgenomen, krijgt het te maken met schaalbaarheidsproblemen, het Bitcoin netwerk staat toe dat een nieuw blok met transacties wordt gedolven in een tijd van ongeveer 10 minuten, ervan uitgaande dat we 144 blokken op een dag hebben met maximale waarden van 2700 transacties per blok, zou Bitcoin slechts 4,5 transacties per seconde hebben toegestaan, Satoshi was zich bewust van deze beperking, we kunnen het zien in een e-mail1 gestuurd naar Mike Hearn in maart 2011 waarin hij uitlegt hoe wat we vandaag kennen als een betalingskanaal werkt. microbetalingen snel en veilig zonder te wachten op bevestigingen. Dit is waar off-chain protocollen om de hoek komen kijken.


Volgens Christian Decker2 zijn off-chain protocollen meestal systemen waarin gebruikers gegevens van een Blockchain gebruiken en beheren zonder de Blockchain zelf tot het laatste moment aan te raken. Gebaseerd op dit concept werd de Lightning Network geboren, een netwerk dat off-chain protocollen gebruikt om Bitcoin betalingen bijna ogenblikkelijk uit te voeren en omdat niet al deze operaties op de blokketen worden geschreven, kunnen er duizenden transacties per seconde worden gedaan en kan Bitcoin worden opgeschaald.


Onderzoek en ontwikkeling op het gebied van off-chain protocollen op Bitcoin heeft een doos van Pandora geopend, vandaag de dag weten we dat we veel meer kunnen bereiken dan waardeoverdracht op een gedecentraliseerde manier, de non-profit LNP/BP Standards Association richt zich op de ontwikkeling van Layer 2 en 3 protocollen op Bitcoin en de Lightning Network, onder deze projecten valt RGB op.


## Wat is RGB?


RGB is ontstaan uit het onderzoek van Peter Todd3 naar single-use-seals en client-side-validatie, dat in 2016-2019 door Giacomo Zucco en de gemeenschap werd omgevormd tot een beter asset-protocol voor Bitcoin en Lightning Network. Verdere evolutie van deze ideeën leidde tot de ontwikkeling van RGB tot een volwaardig Smart contract systeem door Maxim Orlovsky, die de implementatie ervan leidt sinds 2019 met deelname van de gemeenschap.


We kunnen RGB definiëren als een set open source protocollen waarmee we complexe slimme contracten kunnen uitvoeren op een schaalbare en vertrouwelijke manier. Het is geen specifiek netwerk (zoals Bitcoin of Lightning); elke Smart contract is slechts een verzameling Contract deelnemers die met elkaar kunnen communiceren via verschillende communicatiekanalen (standaard Lightning Network). RGB gebruikt Bitcoin Blockchain als een Layer van toestand Commitment en onderhoudt de code van de Smart contract en de gegevens off-chain, wat het schaalbaar maakt, gebruikmakend van Bitcoin transacties (en Script) als een Ownership besturingssysteem voor slimme contracten; terwijl de evolutie van de Smart contract wordt gedefinieerd door een off-chain schema, is het ten slotte belangrijk op te merken dat alles aan de cliëntkant wordt gevalideerd.


Eenvoudig gezegd is RGB een systeem dat de gebruiker in staat stelt om een Smart contract te controleren, uit te voeren en individueel te verifiëren op elk moment zonder extra kosten, omdat het hiervoor geen Blockchain gebruikt zoals "traditionele" systemen doen. Complexe slimme contractsystemen werden gepionierd door Ethereum, maar omdat het vereist dat de gebruiker aanzienlijke hoeveelheden gas uitgeeft voor elke bewerking, hebben ze nooit de schaalbaarheid bereikt die ze beloofden.


Momenteel promoot de Blockchain industrie dat zowel de code van slimme contracten als de data moeten worden opgeslagen in de Blockchain en uitgevoerd door elk knooppunt van het netwerk, ongeacht de excessieve toename in grootte of het misbruik van computationele bronnen. Het schema voorgesteld door RGB is veel intelligenter en efficiënter omdat het snijdt met het Blockchain paradigma door slimme contracten en data gescheiden te hebben van de Blockchain en zo de verzadiging van het netwerk vermijdt zoals gezien in andere platformen, op zijn beurt dwingt het niet elk knooppunt om elke Contract uit te voeren, maar eerder de betrokken partijen, wat vertrouwelijkheid toevoegt tot een niveau dat nog nooit eerder gezien is.


![RGB vs Ethereum](assets/1.webp)


## Slimme contracten in RGB


In RGB definieert Smart contract ontwikkelaar een schema met regels hoe de Contract in de tijd evolueert. Het schema is de standaard voor de constructie van slimme contracten in RGB, en zowel een emittent bij het definiëren van een Contract voor uitgifte als een Wallet of Exchange moeten zich houden aan een bepaald schema waartegen ze de Contract moeten valideren. Alleen als de validatie correct is, kan elke partij verzoeken accepteren en met het actief werken.


Een Smart contract in RGB is een Directed Acyclic Graph (DAG) van toestandsveranderingen, waarbij slechts een deel van de grafiek altijd bekend is en er geen toegang is tot de rest. Het RGB schema is een kernset van regels voor de evolutie van deze grafiek waarmee de Smart contract begint. Elke Contract Participant mag die regels aanvullen (als de Schema dat toestaat) en de resulterende grafiek wordt opgebouwd uit de iteratieve toepassing van die regels.


## Vlottende activa


De fungibele activa in RGB volgen de LNPBP RGB-20 specificatie4, wanneer een RGB-20 is gedefinieerd, worden de activagegevens, bekend als "Genesis data'', gedistribueerd via de Lightning Network, die bevat wat nodig is om het activum te gebruiken. De meest elementaire vorm van activa staat geen secundaire uitgifte, token verbranding, hernominatie of vervanging toe.


Soms zal de uitgever in de toekomst meer tokens moeten uitgeven, d.w.z. stablecoins zoals USDT, waardoor de waarde van elke token gebonden blijft aan de waarde van een inflatoire valuta zoals de USD. Om dit te bereiken bestaan er complexere RGB-20 schema's, en naast de Genesis gegevens vereisen ze dat de emittent zendingen produceert, die ook in de Lightning Network circuleren; met deze informatie kunnen we de totale circulerende Supply van het activum kennen. Hetzelfde geldt voor het verbranden van activa of het veranderen van de naam.


De informatie met betrekking tot het activum kan openbaar of privé zijn: als de emittent vertrouwelijkheid vereist, kan hij ervoor kiezen om geen informatie over de token te delen en handelingen in absolute privacy uit te voeren, maar we hebben ook het tegenovergestelde geval waarin de emittent en de houders willen dat het hele proces transparant is. Dit wordt bereikt door de token gegevens te delen.


## RGB-20 procedures


De verbrandingsprocedure schakelt tokens uit, verbrande tokens kunnen niet meer worden gebruikt.


De vervangingsprocedure vindt plaats wanneer tokens worden verbrand en een nieuwe hoeveelheid van hetzelfde token wordt aangemaakt. Dit helpt de omvang van de historische gegevens van het actief te verminderen, wat belangrijk is om de snelheid van het actief te behouden.


Om het gebruik te ondersteunen waarbij het mogelijk is om activa te verbranden zonder ze te vervangen, wordt een subregeling van RGB-20 gebruikt die alleen het verbranden van activa toestaat.


## Niet fungibele activa


De non-fungible assets in RGB volgen de LNPBP RGB-21 specificatie5, wanneer we met NFT's werken hebben we ook een hoofdschema en een subschema. Deze schema's hebben een graveerprocedure, waarmee we aangepaste gegevens kunnen toevoegen door een deel van de token eigenaar, het meest voorkomende voorbeeld dat we tegenwoordig zien in NFT's is digitale kunst gekoppeld aan de token. De token uitgever kan het graveren van deze gegevens verbieden door gebruik te maken van het RGB-21 subschema. In tegenstelling tot andere NFT Blockchain systemen, maakt RGB het mogelijk om grote media token data te distribueren op een volledig gedecentraliseerde en censuurbestendige manier, door gebruik te maken van uitbreiding op het Lightning P2P netwerk genaamd Bifrost, dat ook gebruikt wordt voor het bouwen van vele andere vormen van RGB specifieke Smart contract functionaliteiten.


Naast fungibele activa en NFT's kunnen RGB en Bifrost worden gebruikt om andere vormen van slimme contracten te produceren, waaronder DEXes, liquiditeitspools, algoritmische stabiele munten enzovoort, die we in toekomstige artikelen zullen behandelen.


## NFT van RGB vs NFT van andere platforms



- Geen dure Blockchain opslag nodig
- IPFS is niet nodig, in plaats daarvan wordt een Lightning Network extensie (genaamd Bifrost) gebruikt (en het is volledig end-to-end versleuteld)
- Geen speciale oplossing voor gegevensbeheer nodig - ook hier neemt Bifrost die rol op zich
- Je hoeft niet te vertrouwen op websites om gegevens bij te houden voor NFT tokens of over emissies activa / Contract ABI's
- Ingebouwde DRM-codering en Ownership beheer
- Infrastructuur voor back-ups met behulp van de Lightning Network (Bifrost)
- Manieren om inhoud te gelde te maken (niet alleen de NFT zelf verkopen, maar ook toegang tot de inhoud, meerdere keren)


## Conclusies


Sinds de lancering van Bitcoin, bijna 13 jaar geleden, is er veel onderzoek gedaan en geëxperimenteerd op dit gebied, zowel de successen als de fouten hebben ons een beetje meer inzicht gegeven in hoe gedecentraliseerde systemen zich in de praktijk gedragen, wat ze echt gedecentraliseerd maakt en welke acties de neiging hebben om ze naar centralisatie te leiden, dit alles heeft ons doen concluderen dat echte decentralisatie een zeldzaam en moeilijk te bereiken fenomeen is, echte decentralisatie is alleen bereikt door Bitcoin en het is om deze reden dat we onze inspanningen richten om er bovenop te bouwen.


RGB heeft zijn eigen konijnenhol binnen het Bitcoin konijnenhol, terwijl ik er doorheen val zal ik posten wat ik geleerd heb, in het volgende artikel zullen we een introductie hebben tot de LNP en RGB nodes en hoe ze te gebruiken.



- 1 https://plan99.net/~mike/Satoshi-emails/thread4.html
- 2 https://btctranscripts.com/chaincode-labs/chaincode-residency/2018-10-22-christian-decker-history-of-lightning/
- 3 https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2016-June/012773.html
- 4 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0020.md
- 5 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0021.md


# Handleiding RGB-node


## Inleiding


In deze tutorial leggen we uit hoe je RGB-node gebruikt om een fungibele token te maken en hoe je die overzet. Dit document is gebaseerd op de RGB-node demo en verschilt in zoverre dat deze tutorial echte Testnet data gebruikt en daarvoor moeten we vanaf nu onze eigen Partially Signed Bitcoin Transaction, PSBT bouwen.


## Vereisten


Het gebruik van een Linux-distributie wordt aanbevolen. Deze tutorial is geschreven met Pop!OS, dat is gebaseerd op Ubuntu en je hebt het volgende nodig:



- lading
- Bitcoin core
- git


Opmerking: Deze tutorial toont het uitvoeren van commando's in een Linux terminal, om onderscheid te maken tussen wat de gebruiker schrijft en het antwoord dat hij krijgt in de terminal, voegen we de $ toe die de bash prompt symboliseert.


U moet een aantal afhankelijkheden installeren:


```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```


Bouwen en uitvoeren


RGB-node is werk in uitvoering (WIP), daarom moeten we onszelf lokaliseren in een specifieke commit (3f3c520c19d84c66d430e76f0fc68c5a66d79c84) om het correct te kunnen compileren en gebruiken, hiervoor voeren we de volgende commando's uit.


```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```


Nu gaan we het compileren, vergeet niet om de --locked vlag te gebruiken omdat er een brekende verandering is geïntroduceerd op een versie van clap.


```
$ cargo install --path . --all-features --locked

....
....
Finished release [optimized] target(s) in 2m 14s
Installing /home/user/.cargo/bin/fungibled
Installing /home/user/.cargo/bin/rgb-cli
Installing /home/user/.cargo/bin/rgbd
Installing /home/user/.cargo/bin/stashd
Installed package `rgb_node v0.4.2 (/home/user/dev/rgb-node)` (executables `fungibled`, `rgb-cli`, `rgbd`, `stashd`)

```


Zoals de Rust compiler ons vertelt, werden de binaries gekopieerd naar de $HOME/.cargo/bin directory, als jouw compiler ze naar een andere plaats heeft gekopieerd, moet je ervoor zorgen dat die directory wordt opgenomen in $PATH.


Onder de geïnstalleerde binaries zien we drie daemons of services (de bestanden die eindigen op d) en een CLI (command line Interface), de CLI staat ons toe te communiceren met de hoofd rgbd daemon. Omdat we in deze tutorial twee nodes gaan draaien, hebben we ook twee clients nodig, elk moet verbinding maken met zijn eigen node, daarvoor maken we twee aliassen aan.


```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```


We kunnen de aliassen gewoon uitvoeren of ze toevoegen aan het einde van het bestand $HOME/.bashrc en als bron $HOME/.bashrc uitvoeren.

Premisse


RGB-node behandelt geen enkele Wallet-gerelateerde functionaliteit, het voert alleen RGB-specifieke taken uit op de gegevens die door een externe Wallet zoals Bitcoin core worden geleverd. Om een basisworkflow met uitgifte en overdracht te demonstreren, hebben we het volgende nodig:



- Een issuance_utxo waaraan RGB-node-0 het nieuw uitgegeven vermogen zal binden
- Een receive_utxo waarbij RGB-node-1 het vermogen ontvangt
- Een change_utxo waarbij RGB-node-0 de activabewijziging ontvangt
- Een Partially Signed Bitcoin Transaction (tx.PSBT), waarvan de uitvoer publieke sleutel zal worden getweakt om een Commitment aan de overdracht toe te voegen.


We gaan de Bitcoin core CLI gebruiken, we moeten de bitcoind daemon op Testnet hebben draaien, dit geeft ons interoperabiliteit en aan het eind kunnen we onze eigen assets naar andere RGB gebruikers sturen die deze tutorial hebben gevolgd.


Voor de eenvoud voegen we deze alias toe aan het einde van ons ~/.bashrc bestand.


```
alias bcli="bitcoin-cli -testnet"
```


Laten we een lijst maken van onze niet-uitgegeven uitvoertransacties en er twee selecteren, één wordt de issuance_utxo en de andere change_utxo, het maakt niet uit welke welke is, het belangrijkste is dat de uitgever controle heeft over deze twee UTXO.


```
$ bcli listunspent
[
{
"txid": "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893",
"vout": 1,
"address": "tb1qn4w9u5x0hxgm30hx6q2rhdwz58xr4ekqdq0vgm",
"label": "",
"scriptPubKey": "00149d5c5e50cfb991b8bee6d0143bb5c2a1cc3ae6c0",
"amount": 0.01703963,
"confirmations": 62432,
"spendable": true,
"solvable": true,
"desc": "wpkh([ec924f82/0'/0'/5']031e0fc9a03e69326c3deeabfd749a7f7b094e3151ada90cd13019efac663c5663)#dj7rhpdt",
"safe": true
},
{
"txid": "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f",
"vout": 1,
"address": "tb1qyd537gf0xmm9ehmhaf3nv0a230crg56mhp9ap3",
"scriptPubKey": "001423691f212f36f65cdf77ea63363faa8bf034535b",
"amount": 0.02877504,
"confirmations": 189184,
"spendable": true,
"solvable": true,
"desc": "wpkh([ec924f82/0'/1'/0']03ae333417e86840145e95ab2852c8f7ca8b8f82cd910883f7ce0c69649403cef2)#jlcj23vw",
"safe": true
}
]
```


Voordat we verder gaan moeten we het hebben over outpoints, een enkele transactie kan meerdere outputs bevatten, het outpoint bevat zowel een 32-byte txid als een 4-byte output index nummer (vout) om te verwijzen naar een specifieke output, gescheiden door een dubbele punt :. In onze listunspent uitvoer vinden we twee UTXO's, op elk daarvan zien we txid en vout, dat zijn de outpoints issuance_utxo en change_utxo.


receive_utxo is een UTXO die bestuurd wordt door de ontvanger, in dit geval gebruiken we e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 wat een outpoint is van een andere Wallet.



- uitgifte_utxo: 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
- change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- receive_utxo: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0


We gaan nu een gedeeltelijk ondertekende transactie maken (tx.PSBT) waarvan de uitvoer getweakt zal worden om een commit tot overdracht te bevatten, vergeet niet om de txid en vout te vervangen door je eigen, de bestemming Address doet er niet echt toe, het kan de jouwe zijn of het kan van iemand anders zijn, het maakt niet uit waar die Sats heengaat, waar het om gaat is dat we issuance_utxo gebruiken.


```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
"psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
"fee": 0.00000280,
"changepos": 0
}
```


De uitvoer gaf ons een PSBT in base64 codering die we zullen gebruiken om tx.PSBT te maken.


```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt
```


Laten we een nieuwe map aanmaken met de naam rgbdata waarin de gegevensmap van elk knooppunt wordt opgeslagen.


```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```


Al in $HOME/rgbdata starten we elke node in verschillende terminals, waar ~/.cargo/bin de map is waar cargo alle binaries heeft gekopieerd na de installatie van RGB-node.


```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```


## Uitgifte


Om een activum uit te geven draaien we rgb0-CLI met de fungibele uitgifte subcommando's, dan de argumenten, de ticker USDT, de naam "USD Tether" en in de toewijzing gebruiken we het uitgiftebedrag en de issuance_utxo zoals we hieronder zien:


```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```


Activa met succes uitgegeven. Gebruik deze informatie om te delen:

Vermogensinformatie:


```
genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"


genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
```


We krijgen de assetId, die hebben we nodig om de asset over te dragen.


```
$ rgb0-cli fungible list

- name: USD Tether
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
```


## generate blinded UTXO


Om de nieuwe USDT te ontvangen, moet RGB-knooppunt-1 generate een blinded UTXO die overeenkomt met receive_utxo om het activum vast te houden.


```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Blinded outpoint: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Outpoint blinding secret: 1679197189805229975
```


Om overboekingen gerelateerd aan deze UTXO te kunnen accepteren, hebben we de originele receive_utxo en de blinding_factor nodig.


## Overdracht


Om een deel van het activum naar RGB-node-1 over te dragen, moeten we het naar blinded UTXO sturen, RGB-node-0 moet een Consignment en een openbaarmaking aanmaken, en het vastleggen in een Bitcoin transactie. Dan hebben we een PSBT nodig, die we aanpassen om de commit op te nemen. Daarnaast staan de -i en -a opties ons toe om een input outpoint op te geven dat de oorsprong van het actief zou zijn en een toewijzing waar we de verandering zullen ontvangen, we moeten het op de volgende manier aangeven @<change_utxo>.


```
$ rgb0-cli fungible transfer utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1

Transfer succeeded, consignments and disclosure are written to "consignment.rgb" and "disclosure.rgb", partially signed witness transaction to "witness.psbt"
Consignment data to share:consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e
```


Dit zal drie nieuwe bestanden schrijven, Consignment, openbaarmaking en de PSBT inclusief de tweak, deze PSBT wordt Witness Transaction genoemd, de Consignment wordt naar RGB-node-1 gestuurd.


## Getuige


De Witness Transaction moet ondertekend en uitgezonden worden, hiervoor moeten we het terug base64 coderen.


```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```


Onderteken het met het subcommando walletprocesspsbt.


```
$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="
{
"psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",
"complete": true
}
```


Maak het nu af en krijg de hex.


```
$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="
{
"hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
"complete": true
}
```


## Uitzending


Zend het uit met het subcommando sendrawtransaction om het bevestigd te krijgen in de Blockchain.


```
$ bcli sendrawtransaction "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000"
8e3787fe40b5feb3044f892e739bdb4043e10de384255a915a37725811abc3fe
```


## Accepteer


Om een inkomende overdracht te accepteren, moet RGB-knooppunt-1 het Consignment bestand ontvangen hebben van RGB-knooppunt-0, de receive_utxo en de bijbehorende blinderingsfactor gegenereerd hebben tijdens het blinderen van UTXO.


```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975

Asset transfer successfully accepted.
```


We kunnen nu (in het veld knownAllocations) de nieuwe toewijzing van 100 vermogenseenheden in <receive_utxo> zien door uit te voeren:


```
$ rgb1-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
index: 1
outpoint: "e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0"
revealedAmount:
value: 100
blinding: 224561f10229eb9ebbdf05f497132d2b8344d70971c80510eddc607d615ee2a0
```


Aangezien receive_utxo blinded was toen de overdracht werd gemaakt, heeft de betaler RGB-node-0 geen informatie over waar de 100 USDT werd verzonden, dus de locatie wordt niet getoond in knownAllocations .


```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
```


Maar zoals je kunt zien kan RGB-node-0 de 900 asset wijziging niet zien die we aan het transfer commando gaven met het -a argument. Om de wijziging te registreren moet RGB-node-0 de openbaarmaking accepteren.


```
$ rgb0-cli fungible enclose disclosure.rgb

Disclosure data successfully enclosed.
```


Als RGB-node-0 succesvol was, kun je de verandering zien door het actief op te sommen.


```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
index: 0
outpoint: "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1"
revealedAmount:
value: 900
blinding: ddba9e0efdd614614420fa0b68ecd2d3376a05dd3d809b2ad1f5fe0f6ed75ea2
```


## Conclusies


We zijn in staat geweest om een fungibel activum te creëren en het van de ene transactie naar de andere te verplaatsen op een privé manier, als we de bevestigde transactie in een Block explorer controleren zouden we niets anders vinden dan een gewone transactie, dit is te danken aan het feit dat RGB zegels voor eenmalig gebruik gebruikt om de transacties te tweaken, In deze post doe ik een intro over hoe RGB werkt.


Deze post kan bugs bevatten, als je iets vindt laat het me dan weten om deze gids te verbeteren, suggesties en kritiek zijn ook welkom, happy hacking! 🖖