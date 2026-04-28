---
name: Programmering Bitcoin
goal: Een complete Bitcoin bibliotheek vanaf nul opbouwen en de cryptografische fundamenten van Bitcoin begrijpen
objectives: 

 - Eindige veldrekenkundige en elliptische krommebewerkingen implementeren in Python
 - Bitcoin transacties programmatisch opbouwen en parsen
 - Testnetadressen aanmaken en transacties uitzenden over het netwerk
 - De wiskundige fundamenten van het Bitcoin veiligheidsmodel onder de knie krijgen

---
# Een reis door de scripts en programma's van Bitcoin


Deze intensieve tweedaagse cursus, gegeven door Jimmy Song, neemt je mee in de technische fundamenten van Bitcoin door een complete Bitcoin bibliotheek vanaf de grond op te bouwen. Beginnend met de essentiële wiskunde van eindige velden en elliptische krommen, ga je verder met transactie parsing, script uitvoering en netwerk communicatie. Door middel van hands-on coderingsoefeningen in Jupyter notebooks, creëer je je eigen testnet adres, bouw je handmatig transacties op en zend je ze direct uit naar het netwerk - dit alles terwijl je een diepgaand begrip krijgt van de cryptografische principes die Bitcoin veilig en zonder vertrouwen maken.


Geniet van de reis!

Opmerking: De video's voor deze cursus zijn alleen beschikbaar in het Engels.

+++

# Inleiding


<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>


## Cursus Overzicht


<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>


Welkom bij de cursus PRO 202 _**Programmeren Bitcoin**_, een intensieve reis die je meeneemt van eindig veld rekenen tot het bouwen en uitzenden van echte transacties op Bitcoin's Testnet.


In deze cursus bouwt u stap voor stap een Bitcoin bibliotheek in Python, terwijl u de cryptografische, protocol- en softwarefundamenten verwerft die nodig zijn om nauwkeurig te redeneren over de veiligheid en innerlijke werking van Bitcoin. De PRO 202 aanpak is grondig hands-on: elk concept wordt onmiddellijk geïmplementeerd in Jupyter notebooks, zodat theorie en code elkaar versterken.


### Essentiële wiskundige concepten voor Bitcoin


Dit eerste deel legt de onmisbare wiskundige basis. Je zult eindige veldrekenkundige en elliptische kromme operaties (groepswet, optelling, verdubbeling, scalaire vermenigvuldiging...) implementeren - de eerste vereisten voor ECDSA. Het doel is tweeledig: het begrijpen van de algebraïsche structuur die cryptografische handtekeningen mogelijk maakt en het bouwen van betrouwbare Python gereedschappen om ze te manipuleren.


Vervolgens worden de componenten van ECDSA geformaliseerd: het genereren van sleutels, het formatteren van punten, hashing, het aanmaken van handtekeningen en verificatie. Dit gedeelte verbindt theorie direct met de praktijk, waarbij de nadruk ligt op implementatiedetails en de robuustheid van het onderliggende beveiligingsmodel.


### Bitcoin Transactie Binnenwerk


In het tweede deel zul je de structuur van een Bitcoin transactie ontleden: UTXO's, invoer/uitvoer, sequenties, scripts, coderingen en meer. Je zult code schrijven om transacties te construeren, ondertekenen en verifiëren, waarbij je een nauwkeurig begrip krijgt van wat er door de hash wordt vastgelegd en waarom.


Vervolgens implementeert u een minimale _Script_ executor, bekijkt u belangrijke opcodes en valideert u uitgavenpaden. Het doel is om u in staat te stellen transactiegedrag te controleren, validatiefouten te diagnosticeren en te redeneren over de veiligheid van uitgavenbeleid.


### Inwendige werking Bitcoin netwerk


In het derde deel zul je transacties plaatsen binnen het bredere systeem: blokstructuur, headers, moeilijkheden en het Proof-of-Work mechanisme. Je zult protocolberichten, blokheaders en Merkle bomen behandelen.


Tenslotte bestudeer je peer-to-peer knooppuntcommunicatie, berichtoptimalisatie en de introductie van SegWit.


Zoals bij elke cursus over Plan ₿ Academy, bevat het laatste deel een evaluatie om je begrip te consolideren. Klaar om de innerlijke werking van Bitcoin te ontdekken en de code te schrijven die het aandrijft? Laten we beginnen!










# Essentiële wiskundige concepten voor Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Wiskunde voor Bitcoin implementatie

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>


![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


### Bitcoin Programmeerfundamenten: Wiskundige kernstructuren


Deze cursus vat de essentiële wiskunde achter de cryptografische systemen van Bitcoin samen in een zeer praktische workflow. Concepten worden uitgelegd, gedemonstreerd met voorbeelden en vervolgens geïmplementeerd in Jupyter Notebook. Het idee is eenvoudig: je begrijpt een cryptografische primitieve pas echt als je hem codeert. Tijdens de tweedaagse structuur generate testnetadressen, bouwen en broadcasten studenten [transacties](https://planb.academy/resources/glossary/transaction-tx) en uiteindelijk interageren ze met het netwerk zonder block explorers. Dit alles vereist een stevige basis in eindige velden en elliptische krommen.


### Eindige velden: De rekenmachine van cryptografie


Een eindig veld F(p) is een rekenkundig systeem gedefinieerd door een priemgetal p, dat elementen 0 tot en met p-1 bevat. Priemvelden zorgen ervoor dat elk element zonder nul een inverse heeft en dat alle bewerkingen binnen het veld blijven. Rekenkundige bewerkingen zijn modulo p voor optellen, aftrekken en vermenigvuldigen. Python's `pow(base, exp, mod)` maakt efficiënte modulaire exponentiatie mogelijk, cruciaal voor grote exponenten die gebruikt worden in echte cryptografische bewerkingen.


#### Multiplicatief gedrag

Vermenigvuldiging van een willekeurig niet-nul element k met alle elementen van een priemveld levert een permutatie van het veld op. Deze eigenschap garandeert uniformiteit en voorkomt structurele zwakheden, waardoor priemvelden ideaal zijn voor het veilig genereren van sleutels en [digitale handtekeningen](https://planb.academy/resources/glossary/digital-signature).


#### Delen en de kleine stelling van Fermat

Delen wordt geïmplementeerd via multiplicatieve inverses. De kleine stelling van Fermat stelt dat

n^(p-1) ≡ 1 (mod p),

dus de inverse is n^(p-2). Python ondersteunt dit direct met `pow(n, -1, p)`. Deze operaties komen voortdurend voor in de onderliggende cryptografische routines van [ECDSA](https://planb.academy/resources/glossary/ecdsa) en Bitcoin.


### Elliptische krommen: Niet-lineaire structuren voor beveiliging van publieke sleutels


Elliptische krommen volgen de vergelijking y² = x³ + ax + b. Bitcoin gebruikt secp256k1, gedefinieerd als y² = x³ + 7 over een eindig veld. Punten op een elliptische kromme vormen een wiskundige groep onder puntentelling. Een lijn getrokken door twee punten P en Q snijdt de kromme in een derde punt R; spiegeling van R over de x-as geeft P + Q. Dit systeem is associatief en bevat een identiteitselement: het oneigenlijke punt.


Het verdubbelen van een punt gebruikt een raaklijn in plaats van een secanslijn, waarbij de helling wordt afgeleid van de afgeleide van de kromme. Hoewel deze formules berekeningen over reële getallen bevatten, worden ze volledig discreet en exact wanneer de kromme gedefinieerd is over een eindig veld - de context die gebruikt wordt in Bitcoin.


### Van wiskunde naar Bitcoin cryptografie


Eindige velden bieden deterministische, inverteerbare rekenkunde; elliptische krommen bieden een niet-lineaire structuur waarbij het berekenen van k-P eenvoudig is, maar het omkeren ervan rekenkundig onuitvoerbaar. De combinatie van beide levert de basis voor Bitcoin's publieke/private sleutels, ECDSA-handtekeningen en transactiebeveiliging. Inzicht in deze fundamenten bereidt studenten voor op het direct implementeren van sleutels, transacties en handtekeningen, zonder abstracties of externe hulpmiddelen.


## Elliptische kromme cryptografie

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>


![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


Dit hoofdstuk introduceert elliptische krommen gedefinieerd over eindige velden en legt uit waarom ze de wiskundige ruggengraat vormen van de Bitcoin [cryptografie](https://planb.academy/resources/glossary/cryptography). Terwijl elliptische krommen over reële getallen glad en continu lijken, creëert het toepassen van dezelfde vergelijkingen over een eindig veld een discrete, verspreide verzameling punten. Ondanks het visuele verschil gedragen alle formules voor puntentelling, hellingen en algebraïsche regels zich precies hetzelfde, alleen het rekenen verandert in modulair rekenen. Bitcoin gebruikt de kromme y² = x³ + 7 (secp256k1), die symmetrie en niet-lineair gedrag behoudt, wat essentieel is voor cryptografische veiligheid.


### Punten verifiëren en eindige veldimplementatie


Een punt ligt op een eindig-veld elliptische kromme als zijn coördinaten voldoen aan de krommevergelijking onder modulo p. Het verifiëren van een punt zoals (73,128) op F₁₃₇ vereist het controleren dat y² mod p gelijk is aan x³ + 7 mod p. Om dit in code te implementeren moeten klassen gemaakt worden voor eindig-veld elementen en kromme punten. Operator overloading zorgt ervoor dat alle rekenkunde - optellen, vermenigvuldigen, exponentiëren, delen - automatisch modulo p wordt uitgevoerd. Zodra deze abstracties bestaan, worden meer geavanceerde cryptografische operaties eenvoudig om te schrijven en over te redeneren.


#### Groepseigenschappen en puntentelling

Elliptische kromme punten vormen een wiskundige groep onder optelling. De groep voldoet aan closure, associativiteit, identiteit (het punt op oneindig) en inverses (spiegeling over de x-as). Geometrische constructies bevestigen deze eigenschappen, waardoor scalaire vermenigvuldiging (P herhaaldelijk opgeteld bij zichzelf) goed gedefinieerd is. Deze groepsregels maken elliptische krommecryptografie mogelijk en zorgen voor consistent, voorspelbaar gedrag bij herhaalde puntbewerkingen.


### Cyclische groepen en het discrete logaritme probleem


Door een generatorpunt G op een kromme te kiezen kunnen we generate een cyclische groep maken: G, 2G, 3G, ..., nG = 0. De punten lijken niet-lineair en onvoorspelbaar, zelfs als ze opeenvolgend gegenereerd worden. Deze onvoorspelbaarheid creëert de basis voor het discrete logaritmeprobleem: het berekenen van P = sG is eenvoudig, maar het bepalen van s uit P is rekenkundig onuitvoerbaar voor grote groepen. Deze eenrichtingsfunctie maakt cryptografie met openbare sleutels veilig. Scalars (private sleutels) worden in kleine letters geschreven; punten ([publieke sleutels](https://planb.academy/resources/glossary/public-key)) in hoofdletters.


#### Efficiënte scalaire vermenigvuldiging

Om sG efficiënt te berekenen, gebruiken implementaties het dubbel-en-toevoegen-algoritme: scan de binaire representatie van de scalar, verdubbel het punt elke stap en voeg G alleen toe als de bit 1 is. Dit vermindert de berekening van O(n) toevoegingen naar O(log n), wat praktische cryptografische bewerkingen mogelijk maakt, zelfs met 256-bits scalars.


#### De secp256k1-curve in Bitcoin


Bitcoin gebruikt de kromme secp256k1, gedefinieerd door y² = x³ + 7 over een priemveld waar p = 2²⁵⁶ - 2³² - 977. Het generatorpunt G heeft vaste coördinaten gekozen met een deterministische NUMS ("nothing up my sleeve") procedure. De groepsvolgorde n is een grote priem in de buurt van 2²⁵⁶, zodat elk niet-nul punt dezelfde groep genereert. De grootte van 2²⁵⁶ (~10⁷⁷) is astronomisch groot, waardoor het brute-forcen van private sleutels fysiek onmogelijk is. Zelfs een triljoen supercomputers die een triljoen jaar draaien zouden de sleutelruimte niet noemenswaardig verkleinen.


### Openbare sleutels, privésleutels en SEC serialisatie


Een private sleutel is een willekeurige scalair s; de publieke sleutel is P = sG. Omdat het oplossen van het discrete logprobleem niet uitvoerbaar is, kan P gedeeld worden zonder s te onthullen. Publieke sleutels moeten geserialiseerd worden voor verzending met het SEC-formaat. Het ongecomprimeerde SEC formaat gebruikt 65 bytes: prefix 0x04 + x-coördinaat + y-coördinaat. Het gecomprimeerde formaat gebruikt slechts 33 bytes: prefix 0x02 of 0x03 (afhankelijk van y's pariteit) + x-coördinaat. Bitcoin gebruikte oorspronkelijk ongecomprimeerde sleutels, maar geeft nu de voorkeur aan gecomprimeerde omwille van de efficiëntie.


#### Bitcoin Address Schepping


Bitcoin adressen zijn hashes van publieke sleutels, niet de ruwe sleutels zelf. Om een generate adres te maken, seriëert u de openbare sleutel in SEC formaat, berekent u hash160 ([SHA-256](https://planb.academy/resources/glossary/sha256) dan RIPEMD-160), voegt u het netwerkvoorvoegsel toe (0x00 voor mainnet, 0x6F voor testnet), berekent u een controlesom met dubbele SHA-256, voegt u de eerste vier bytes van de controlesom toe en codeert u het resultaat met Base58. Deze codering verwijdert dubbelzinnige tekens en bevat de controlesom om transcriptiefouten te voorkomen. De meerstappenpijplijn verbergt de openbare sleutel totdat een uitgave plaatsvindt, voegt netwerkidentificatie toe en zorgt voor door mensen leesbare, foutbestendige adressen.


# Bitcoin Transactie Binnenwerk

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Transactie parsing en ECDSA-handtekeningen

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>


![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


### ECDSA begrijpen: Bitcoin's Stichting Digitale Handtekening


Bitcoin vertrouwt op ECDSA, een handtekeningschema gebaseerd op elliptische krommen dat sterke beveiliging biedt met veel kleinere sleutelgroottes dan RSA. De veiligheid komt van het elliptische discrete logaritmeprobleem: gegeven P = eG, is het berekenen van P eenvoudig, maar het afleiden van e uit P is rekenkundig onuitvoerbaar. Deze asymmetrie maakt cryptografie met een openbare sleutel mogelijk terwijl de privésleutels veilig blijven.


#### DER-codering van ECDSA-handtekeningen


Bitcoin codeert ECDSA-handtekeningen met het DER-formaat:


- 0x30 (sequentiemarkering)
- lengte byte
- 0x02 + lengte + R bytes
- 0x02 + lengte + S bytes


Dit voegt overhead toe, waardoor een handtekening van 64 bytes wordt uitgebreid tot ~71-72 bytes. [Taproot](https://planb.academy/resources/glossary/taproot) elimineert deze inefficiëntie door [Schnorr](https://planb.academy/resources/glossary/schnorr-protocol)-handtekeningen van vaste grootte te gebruiken.


### Ondertekeningsverbintenissen en het ondertekeningsproces


ECDSA-handtekeningen zijn gebaseerd op een verbintenisvergelijking: UG + VP = KG. De ondertekenaar selecteert U- en V-waarden die niet gelijk zijn aan nul en een willekeurige [nonce](https://planb.academy/resources/glossary/nonce) K, waarmee kennis van de privésleutel wordt bewezen zonder deze te onthullen. Het bericht wordt gehasht in Z, een willekeurige K wordt gegenereerd, R is de x-coördinaat van KG en S = (Z + RE)/K. De handtekening is het paar (R, S). De veiligheid hangt kritisch af van het gebruik van een unieke, onvoorspelbare K. Als K wordt hergebruikt of uitlekt, is de privésleutel gecompromitteerd. Moderne implementaties gebruiken deterministische K generatie (RFC 6979) om RNG fouten te voorkomen.


#### Handtekening Verificatie

Gegeven Z, (R, S) en de openbare sleutel P, berekent de verificateur U = Z/S en V = R/S en controleert dan of de x-coördinaat van UG + VP gelijk is aan R. Dit werkt omdat de verificatiealgebra KG reconstrueert zonder de privésleutel nodig te hebben. Voor het vervalsen van handtekeningen zou het oplossen van het discrete logprobleem of het breken van de hashfunctie nodig zijn.


#### Schnorr-handtekeningen en historische context


Schnorr-handtekeningen zijn wiskundig schoner en ondersteunen aggregatiefuncties, maar waren gepatenteerd toen Bitcoin werd gelanceerd. ECDSA bood een gratis alternatief, maar met meer complexiteit en grotere handtekeningen. Toen de patenten verlopen waren, voegde Bitcoin Schnorr-handtekeningen toe via Taproot, met vaste handtekeningen van 64 bytes en verbeterde privacy. ECDSA blijft ondersteund voor oude compatibiliteit.



### Transactiestructuur en invoer/uitvoer


Een Bitcoin transactie bestaat uit:


- versie (4 bytes, little-endian)
- invoerlijst
- uitvoerlijst
- locktime (4 bytes)


Ingangen verwijzen naar eerdere [UTXO](https://planb.academy/resources/glossary/utxo)'s door hun transactiehash en uitvoerindex, en bevatten een ontgrendelingsscript (scriptSig) en een volgnummer dat wordt gebruikt voor tijdsloten of RBF. Uitgangen specificeren het bedrag (8 bytes) en het vergrendelingsscript (scriptPubKey), die de bestedingsvoorwaarden definiëren. Bitcoin adressen zijn representaties van deze [scripts](https://planb.academy/resources/glossary/script).


#### Het UTXO model

Bitcoin houdt onbestede uitgaven bij in plaats van rekeningsaldi. UTXO's moeten volledig worden uitgegeven - gedeeltelijke uitgaven zijn onmogelijk. Om 1 BTC van een UTXO van 100 BTC uit te geven, moet een transactie een wisseluitvoer bevatten. Het vergeten van de wisseluitvoer verandert het restant in een mijnwerkersvergoeding.


#### Serialisatie en parsing van transacties


Transacties gebruiken een compact binair formaat. Na het versieveld codeert een varint het aantal ingangen. De ingangen omvatten:


- vorige tx hash (32 bytes)
- uitvoerindex (4 bytes)
- scriptSig (varstr)
- reeks (4 bytes)


De uitvoer bevat een bedrag van 8 bytes en scriptPubKey (varstr). Locktime bepaalt wanneer de transactie geldig wordt. Serialisatie gebruikt little-endian ordening voor de meeste gehele getallen. Parsers verbruiken bytes opeenvolgend en delegeren naar gespecialiseerde klassen voor invoer, uitvoer en scripts.


### Vergoedingen, verandering en plooibaarheid


Vergoedingen zijn impliciet:

vergoeding = som(invoerwaarden) - som(uitvoerwaarden).

Elke niet-toegewezen waarde wordt de vergoeding, waardoor een correcte constructie van de uitvoer essentieel is. Vóór [SegWit](https://planb.academy/resources/glossary/segwit) waren handtekeningen vervormbaar - S veranderen in N-S produceerde een nieuwe geldige transactie met een andere ID. Bitcoin dwingt nu een lage-S-regel af en SegWit isoleert handtekeningen van de txid-berekening, waardoor ID's stabiel worden en tweedelaagsprotocollen zoals [Lightning](https://planb.academy/resources/glossary/lightning-network) mogelijk worden.


## Bitcoin Script- en transactievalidatie

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>


![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


Bitcoin Script is een kleine, stackgebaseerde slimme contracttaal die bepaalt hoe munten kunnen worden uitgegeven. Elke uitvoer draagt een scriptPubKey (vergrendelingsscript) en elke invoer draagt een scriptSig (ontgrendelingsscript). Samen vormen ze een programma dat moet evalueren naar "waar" om de uitgave geldig te laten zijn. Het script is opzettelijk niet Turing-compleet zodat alle uitvoeringspaden voorspelbaar zijn en gemakkelijk te valideren over het netwerk.


### Scriptbewerkingen en uitvoeringsmodel


Een script is een opeenvolging van gegevenselementen en opcodes. Data pushes (handtekeningen, publieke sleutels, hashes) worden op de stack geplaatst, terwijl opcodes die beginnen met `OP_` de stack transformeren. Na uitvoering moet het bovenste stackelement niet nul zijn voor succes. Voorbeelden: `OP_DUP` dupliceert het bovenste element, `OP_HASH160` past SHA256 toe en vervolgens RIPEMD160, en `OP_CHECKSIG` verifieert een handtekening tegen de sighash van de transactie en een publieke sleutel, waarbij 1 wordt gezet voor geldig, 0 voor ongeldig. Parsingregels maken onderscheid tussen ruwe data (lengte-gefixeerd) en opcodes (opgezocht op waarde) en een kleine virtuele machine voert ze deterministisch uit op elk [knooppunt](https://planb.academy/resources/glossary/node).


### P2PK en P2PKH: Kernbetalingspatronen


Het vroegste patroon, Pay-to-Public-Key (P2PK), vergrendelde munten direct aan een volledige openbare sleutel: de scriptPubKey is `<pubkey> OP_CHECKSIG`, en de scriptSig is slechts een handtekening. Het is eenvoudig maar ruimte-inefficiënt en onthult de openbare sleutel voordat de munten zijn uitgegeven.


#### P2PKH en adressen

Pay-to-Public-Key-Hash (P2PKH) verbetert dit door te locken naar een 20-byte hash van de publieke sleutel. Het scriptPubKey is `OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG`, en het scriptSig geeft `<signature> <pubkey>`. De uitvoering controleert of de verstrekte openbare sleutel hasht naar de vastgelegde waarde en verifieert dan de handtekening. Dit verbergt de publieke sleutel tot het moment van uitgeven, verkleint de grootte en komt overeen met het bekende "1..." mainnet adres formaat.


### Transactievalidatie en handtekeninghashen


Een knooppunt dat een transactie valideert moet ervoor zorgen:

1) Elke ingang verwijst naar een bestaande, ongebruikte uitgang.

2) Totale inputwaarde ≥ totale outputwaarde (het verschil is de vergoeding).

3) Elke scriptSig ontgrendelt correct de scriptPubKey waarnaar verwezen wordt.


Handtekening verificatie vereist het construeren van het exacte bericht dat werd ondertekend, genaamd de sighash. Voor legacy ECDSA maakt de validatie alle scriptSigs leeg, vervangt de scriptSig van de huidige invoer door de overeenkomstige scriptPubKey, voegt een hash-type van 4 bytes toe (meestal `SIGHASH_ALL`) en double-hasht het resultaat. Die 256-bit waarde is wat `OP_CHECKSIG` gebruikt. Alternatieve hash types (bijvoorbeeld `SINGLE`, `NONE`, met of zonder `ANYONECANPAY`) veranderen welke delen van de transactie worden vastgelegd, waardoor niche gebruikssituaties zoals gezamenlijke financiering of gedeeltelijk gespecificeerde transacties mogelijk worden, maar ze worden in de praktijk zelden gebruikt.


#### Kwadratisch Hashing en SegWit

Omdat elke ingang in een legacy transactie zijn eigen sighash berekening vereist over een structuur die alle ingangen omvat, kan de validatietijd kwadratisch toenemen met het aantal ingangen. Grote transacties met meerdere ingangen veroorzaakten ooit merkbare validatievertragingen. SegWit heeft de sighash berekening herontworpen om gedeelde delen in de cache te plaatsen en de complexiteit te reduceren tot lineaire tijd, waardoor de schaalbaarheid verbeterd is en denial-of-service aanvallen moeilijker worden.


### Scriptraadsels en beveiligingslessen


Scripts kunnen veel meer uitdrukken dan alleen "één handtekening ontgrendelt deze munten" Scriptpuzzels laten dit zien door willekeurige voorwaarden te coderen - wiskundige problemen, hash preimage uitdagingen of zelfs botsingspremies - waarbij iedereen die de juiste gegevens levert de munten kan uitgeven. Uitvoeringen die alleen vertrouwen op openbare gegevens (geen handtekeningen) zijn echter kwetsbaar voor [miner](https://planb.academy/resources/glossary/miner)-running: zodra een geldige oplossing in de [mempool](https://planb.academy/resources/glossary/mempool) verschijnt, kan elke miner deze kopiëren en de uitbetaling naar zichzelf omleiden.


De praktische les is dat contracten in de echte wereld bijna altijd handtekeningcontroles bevatten, zelfs als ze complexere logica bevatten zoals multisig, timelocks of hashlocks. Handtekeningen binden de oplossing aan een specifieke partij, waardoor prikkels behouden blijven en voorkomen wordt dat anderen de uitbetaling stelen. Het begrijpen van Script's stack model, standaard patronen en subtiele valkuilen is essentieel voor het ontwerpen van veilige Bitcoin smart contracts en voor het redeneren over hoe transacties daadwerkelijk gevalideerd worden op het netwerk.


## Transactieconstructie en Pay-to-Script Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>


![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


### Bitcoin Transacties en P2SH bouwen


Bitcoin transactieconstructie overbrugt theoretische protocolkennis met praktische implementatie. Een transactie selecteert UTXO's om uit te geven, bouwt uitgangen met vergrendelingsscripts, maakt handtekeningen voor elke invoer en serialiseert alles in het exacte formaat dat knooppunten verwachten. Het proces vereist inzicht in het genereren van sighash, Script-gedrag en de juiste afhandeling van vergoedingen en wijzigingen.


### Basis transactieconstructie


Elke transactie-invoer verwijst naar een vorige uitvoer door txid en index. Uitgangen specificeren bedragen in satoshi's en sluitscripts. Het verschil tussen de totale invoer en de totale uitvoer is de vergoeding. Om een input te ondertekenen wordt een aangepaste versie van de transactie geserialiseerd, de sighash ervan wordt berekend en de private sleutel ondertekent het. De resulterende handtekening en openbare sleutel vormen de ScriptSig. Zodra elke invoer is ondertekend, kan de ruwe transactie worden uitgezonden naar het netwerk.


### Transacties met meerdere handtekeningen


Bare multisig gebruikt `OP_CHECKMULTISIG` om m-of-n handtekeningen te vereisen. Door een vroege off-by-one bug verbruikt OP_CHECKMULTISIG een extra stackelement, waardoor een initiële `OP_0` in de ScriptSig nodig is. Bare multisig is functioneel maar inefficiënt: alle publieke sleutels verschijnen on-chain, waardoor scriptPubKeys groot, duur en moeilijk te coderen zijn als adressen. Deze beperkingen motiveerden de introductie van pay-to-script-hash.


#### Architectuur P2SH

P2SH verbergt complexe scripts achter een 20-byte HASH160. De scriptPubKey staat vast: `OP_HASH160 <20-byte hash> OP_EQUAL`. Het onderliggende redeem script - dat multisig, timelocks of andere condities bevat - wordt alleen onthuld en uitgevoerd als het uitgegeven wordt. De verzender ziet alleen de hash, terwijl de ontvanger het script privé beheert. Dit ontwerp vermindert de grootte van on-chain, verbetert de privacy en maakt complexe contracten mogelijk zonder de verzenders te belasten.


### P2SH Uitgaven en implementatie


Om een P2SH uitvoer uit te geven, moet de ScriptSig de benodigde ontgrendelingsgegevens *plus* het aflossingsscript zelf bevatten. Validatie vindt plaats in twee stappen:

1) HASH160(redeem_script) moet overeenkomen met de hash van de scriptPubKey.

2) Na verificatie wordt het redeemscript uitgevoerd met de verstrekte gegevens.


Bij het genereren van handtekeningen voor een P2SH invoer, gebruikt het sighash proces het redeem script in plaats van de scriptPubKey. Elke ondertekenaar moet het volledige redeem script bezitten om generate geldige handtekeningen te genereren. P2SH adressen gebruiken versiebyte 0x05 op mainnet ("3..." adressen) en 0xC4 op testnet ("2..." adressen).


#### Praktische beveiligingsoverwegingen


Het verliezen van een afkoopscript betekent het verliezen van geld: voor het uitgeven zijn zowel de publieke sleutels als het afkoopscript zelf nodig. Multisig deelnemers moeten controleren of hun publieke sleutels correct zijn opgenomen voordat ze stortingen accepteren. P2SH ondersteunt geavanceerde constructies zoals multisig, timelocks en hashlocks, maar fouten in scriptlogica kunnen fondsen permanent blokkeren, dus testen op testnet is essentieel.


P2SH verbetert de privacy door de bestedingsvoorwaarden te verbergen tot de eerste besteding, maar zodra het inwisselscript on-chain verschijnt, wordt het permanent zichtbaar. Desondanks maakten de voordelen van kleinere afmetingen, achterwaartse compatibiliteit en flexibele contractondersteuning P2SH tot een belangrijke mijlpaal, die latere upgrades zoals SegWit en Taproot beïnvloedde.


# Inwendige werking Bitcoin netwerk

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin Blokken en Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>


![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


Bitcoin [blokken](https://planb.academy/resources/glossary/block) groeperen transacties en beveiligen ze met [proof of work](https://planb.academy/resources/glossary/proof-of-work). Elk blok bevat een [header](https://planb.academy/resources/glossary/block-header) van 80 bytes plus een lijst van transacties. Ondanks de hoge energiekosten voor het produceren van een geldig blok, is het verifiëren ervan goedkoop: voor het opslaan van alle ~900k headers is slechts ~72 MB nodig, waardoor zelfs kleine apparaten proof of work van de keten efficiënt kunnen verifiëren.


### Coinbase-transacties en blokbeloningen


Elk blok begint met precies één [Coinbase transactie](https://planb.academy/resources/glossary/coinbase-transaction) - de enige manier waarop nieuwe bitcoin in omloop komen. Het heeft een zero prev-tx hash en een index van 0xffffffff, die het uniek identificeert. De subsidie begon bij 50 BTC en halveert elke 210.000 blokken (50, 25, 12,5, 6,25, 3,125, ...). Miners rekenen ook transactiekosten. Omdat de 4-byte nonce te klein is voor moderne ASIC's, wijzigen miners gegevens in de Coinbase transactie om de [Merkle](https://planb.academy/resources/glossary/merkle-tree) root te wijzigen en extra zoekruimte te creëren. BIP34 vereist het insluiten van de blokhoogte in de Coinbase scriptSig om ervoor te zorgen dat elke Coinbase txid uniek is.


### Blokkopvelden en Soft Fork signalering


De header van 80 bytes bevat:


- versie (4 bytes)
- vorige blok hash (32 bytes)
- Merkle wortel (32 bytes)
- tijdstempel (4 bytes)
- bits (moeilijkheidsdoel, 4 bytes)
- nonce (4 bytes)


Versienummers evolueerden naar een bitveldsignaleringssysteem via [BIP9](https://planb.academy/resources/glossary/bip), waardoor mijners de gereedheid van [soft-fork](https://planb.academy/resources/glossary/soft-fork) konden coördineren. De tijdstempel is een 32-bits Unix-tijdwaarde en moet rond het jaar 2106 worden bijgewerkt.


#### Bits Veld en Doelen

Het veld bits codeert het doel in compacte vorm: doel = coëfficiënt × 256^(exponent-3). Geldige blok-hashes moeten numeriek onder dit doel liggen. Omdat hashes worden geïnterpreteerd als little-endian gehele getallen, verschijnen geldige hashes vaak met veel achterliggende nullen als ze worden weergegeven in hex.


### Moeilijkheid, validatie en aanpassingen


Moeilijkheid is gedefinieerd als laagste_doel / huidig_doel, wat uitdrukt hoeveel moeilijker mining nu is vergeleken met de makkelijkst mogelijke moeilijkheid. Validatie vereist alleen het vergelijken van de hash van de header met het doel - extreem goedkoop ten opzichte van mining.


Elke 2016-blok past Bitcoin de [moeilijkheidsgraad](https://planb.academy/resources/glossary/difficulty) aan om blokintervallen van ~10 minuten na te streven. De aanpassing vergelijkt de werkelijke tijd voor de vorige 2016-blokken met de verwachte twee weken. Limieten beperken de aanpassingen tot een factor vier. Grote gebeurtenissen in de echte wereld, zoals China's mining verbod, demonstreerden de veerkracht van dit mechanisme toen de hash rate sterk daalde en de moeilijkheidsgraad naar beneden werd bijgesteld om te compenseren.


### Groepssubsidie en totaal Supply


De subsidie op hoogte h wordt als volgt berekend: subsidie = 5_000_000_000 >> (h // 210_000). Dit levert het halveringsschema op dat convergeert naar een totaal aanbod van ~21 miljoen BTC. Het sommeren van de geometrische reeks (50 + 25 + 12.5 + ...) × 210.000 verklaart de limiet. Miners kunnen minder dan de toegestane subsidie opeisen, maar nooit meer, of het blok wordt ongeldig. Naarmate de subsidies afnemen in opeenvolgende halvings, worden de transactievergoedingen een steeds belangrijker onderdeel van de inkomsten van de mijnwerkers en de veiligheid op lange termijn van het netwerk.


## Netwerkcommunicatie en Merklebomen

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>


![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


### Bitcoin Netwerkarchitectuur


Bitcoin's [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p) netwerk werkt als een gedecentraliseerd roddel systeem waar nodes transacties en blokken doorgeven zonder elkaar te vertrouwen. Nieuwe nodes starten op door contact op te nemen met hardgecodeerde DNS seeds die worden onderhouden door de kernontwikkelaars. Deze DNS seeds geven IP's van actieve peers terug, waardoor nodes het netwerk kunnen ontdekken en dan extra peers kunnen aanvragen via getaddr. Netwerken is opzettelijk niet [consensus](https://planb.academy/resources/glossary/consensus)-kritisch, dus implementaties kunnen verschillen zolang de consensusregels ongewijzigd blijven.


### Berichtstructuur en handdruk


Alle Bitcoin P2P berichten gebruiken een vaste envelop: een magische waarde van 4 bytes (F9BEB4D9 voor mainnet), een ASCII commando van 12 bytes, een payloadlengte van 4 bytes little-endian, een checksum van 4 bytes (eerste 4 bytes van hash256) en de payload. Veel voorkomende commando's zijn version, verack, inv, getdata, tx, block, getheaders, headers, ping en pong.


De handdruk begint wanneer een verbindend knooppunt een versiebericht stuurt. De ontvanger antwoordt met verack en zijn eigen versie. Zodra beide partijen deze twee berichten hebben uitgewisseld, is de verbinding actief en kunnen knooppunten beginnen met het doorgeven van voorraden en gegevens.


### Merkle Bomen en Merkle Wortels


Bitcoin slaat een enkele 32-byte Merkle root op in elke blokkop als een verplichting voor alle transacties in het blok. Transacties worden gehasht (hash256), gekoppeld, samengevoegd en herhaaldelijk gehasht totdat er één hash overblijft. Als een niveau een oneven aantal heeft, wordt de laatste hash gedupliceerd. Intern zijn [hashes](https://planb.academy/resources/glossary/hash-function) big-endian, terwijl geserialiseerde blokgegevens little-endian gebruiken, waardoor omkeringen voor en na de boomconstructie nodig zijn.


#### Merkle bewijzen en SPV

Merkle bewijzen maken het mogelijk om te verifiëren dat een transactie in een blok zit zonder het hele blok te downloaden. Het bewijs bestaat uit sibling hashes langs het pad naar de root. Lichtgewicht SPV-cliënten slaan alleen blokkoppen op en vragen deze bewijzen op bij [volledige knooppunten](https://planb.academy/resources/glossary/full-node). Omdat een Merkle tree logaritmisch groeit, vereist het bewijzen van inclusie in een blok met duizenden transacties slechts een paar honderd bytes.


Taproot breidt dit concept uit door de bestedingsvoorwaarden vast te leggen in een Merklized script tree (MAST), waarbij alleen de uitgevoerde tak wordt onthuld, samen met een Merkle bewijs. Dit verbetert zowel de efficiëntie als de privacy.


### Netwerkbewerkingen en bloksynchronisatie


Knooppunten gebruiken getdata om transacties of blokken op te vragen, waarbij ze een type ID specificeren (1=tx, 2=block, 3=filtered block, 4=compact block) plus een 32-byte identifier. Voor ketensynchronisatie sturen knooppunten getheaders met een startblokhash, en ontvangen tot 2000 headers als antwoord. Elke geretourneerde header is 80 bytes gevolgd door een dummy transactietelling van nul.


Volledige verificatie van ontvangen blokken vereist twee controles:

1. De hash van het blok moet onder het doel liggen dat gecodeerd is in het bits-veld.

2. De Merkle root die uit alle transacties wordt berekend (met de juiste endianness handling) moet overeenkomen met de root van de header.


Alleen als beide voorwaarden slagen, accepteert een knooppunt het blok, wat het Bitcoin principe "vertrouw niet, verifieer" weerspiegelt.


## Geavanceerde knooppuntcommunicatie en gescheiden getuigenissen

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>


![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)


Deze sessie verenigt geavanceerde P2P netwerken met Segregated Witness, en laat zien hoe moderne Bitcoin software direct communiceert met nodes terwijl SegWit-bewuste transactiestructuren gebruikt worden. Ontwikkelaars leren blokken op te halen, te scannen naar relevante transacties en transacties te construeren door alleen ruwe netwerkcommunicatie te gebruiken - geen blokverkenners nodig.


### Blokgebaseerd transactieherstel en privacy


[Portemonnees](https://planb.academy/resources/glossary/wallet) moeten binnenkomende betalingen detecteren door blokken te scannen op uitgangen die overeenkomen met hun scriptPubKey. Het ophalen van hele blokken beschermt de privacy beter dan het opvragen van individuele transacties, wat sterke signalen over gebruikersactiviteit lekt. Zelfs blokverzoeken kunnen informatie lekken over ketens met een laag volume, waardoor compacte blokfilters (BIP158) essentieel zijn voor privacy-beschermende light clients. Filters kunnen valse positieven produceren maar nooit valse negatieven, waardoor cliënten alleen potentieel relevante blokken kunnen downloaden zonder specifieke adressen te onthullen.


### Trustless Netwerkinteractie


De `get_block` workflow demonstreert het juiste netwerkgebruik: stuur getdata, ontvang een blok, verifieer dan onafhankelijk de Merkle root en proof of work. Een blok wordt alleen geaccepteerd als de ontvangen hash overeenkomt met de gevraagde hash en de berekende Merkle root overeenkomt met de header. Een blok wordt alleen geaccepteerd als de ontvangen hash van de header overeenkomt met de gevraagde hash en de berekende Merkle root overeenkomt met de header. Dit belichaamt "niet vertrouwen, verifiëren" en zorgt ervoor dat zelfs kwaadwillende peers knooppunten niet kunnen misleiden om gewijzigde gegevens te accepteren.


#### Transacties ophalen uit blokken

De transacties van een blok kunnen worden gescand op overeenkomende scriptPubKeys met behulp van eenvoudige iteratie. Productiewallets voeren dit continu uit als er nieuwe blokken binnenkomen en bewijzen het eigendom van de uitvoer strikt door cryptografische validatie in plaats van te vertrouwen op API's van derden.


### SegWit Doelstellingen en ontwerp


Gesegregeerde Getuige (SegWit) repareerde de vervalsbaarheid van transacties door handtekeninggegevens uit de txid berekening te halen. Dit maakte betrouwbare vooraf ondertekende transactieketens mogelijk en maakte Lightning Network praktisch. SegWit verhoogde ook de blokcapaciteit door "blokgewicht" te gebruiken: oude knooppunten zien nog steeds ≤1 MB blokken, terwijl geüpgradede knooppunten tot 4 MB valideren, inclusief getuigegegevens. Vernieuwde getuigenprogramma's (v0-v1 tot nu toe) creëren een gestructureerd upgradepad voor toekomstige scripttypes.


#### P2WPKH (oorspronkelijk SegWit)


P2WPKH vervangt de oude P2PKH structuur door een script van 22 bytes: OP_0 + push20 + hash160(pubkey). Spending verplaatst de handtekening en pubkey naar een apart getuige veld.


- Pre-SegWit knooppunten: zie "iedereen kan uitgeven", behandel het als geldig.
- Post-SegWit knooppunten: herkennen OP_0 + 20-byte hash en valideren met behulp van getuigegegevens.


Deze scheiding verhelpt vervormbaarheid en verlaagt de kosten. De getuige gebruikt een varintelling gevolgd door de handtekening en pubkey.


#### P2SH-P2WPKH (Achterwaarts compatibel SegWit)


Om oude portemonnees naar SegWit adressen te laten sturen, kunnen P2WPKH scripts in P2SH gewikkeld worden.


- scriptPubKey: standaard P2SH hash160(redeemScript)
- scriptSig: het redeemScript (het P2WPKH programma)
- getuige: handtekening + pubkey


Validatielagen:

1. Pre-BIP16 knooppunten accepteren het redeemScript als geldig.

2. Post-BIP16 knooppunten evalueren het, waardoor OP_0 + hash op de stack achterblijft.

3. SegWit knooppunten voeren volledige getuigenvalidatie uit.


#### P2WSH voor complexe scripts


P2WSH veralgemeent SegWit voor multisig en geavanceerde scripts door te committen naar SHA256(script) in plaats van hash160. Een typische 2-van-3 multisig getuigenstapel:


- leeg element (CHECKMULTISIG bug)
- sig1
- sig2
- getuigenscript (het multisig script)


SegWit knooppunten controleren of SHA256(witnessScript) overeenkomt met de hash van de scriptPubKey en voeren het dan uit. Door SHA256 en een hash van 32 bytes te gebruiken, kan P2WSH onderscheiden worden van P2WPKH en wordt de beveiliging versterkt.


#### P2SH-P2WSH (Maximale compatibiliteit)


Complexe SegWit scripts kunnen ook in P2SH verpakt worden:


- scriptSig: redeemScript (OP_0 + 32-byte hash)
- getuige: handtekeningen + getuigeScript


De validatie doorloopt drie generaties regels, precies zoals bij P2SH-P2WPKH. Deze wrapper was essentieel voor vroege Lightning implementaties die multisig nodig hadden zonder kneedbaarheid. Hoewel de voorkeur tegenwoordig uitgaat naar native P2WSH, zorgt de omhulde vorm voor compatibiliteit met oudere wallet systemen.


### De impact van SegWit


SegWit verstrekt:


- stabiele transactie-ID's
- lagere vergoedingen via gedisconteerde getuigegegevens
- hogere blokdoorvoer via blokgewicht
- compatibiliteit voor oude knooppunten
- een schoon upgradepad voor Taproot en toekomstige uitbreidingen


Samen met vertrouwensloze netwerkinteractie vormen deze tools de ruggengraat van de moderne Bitcoin ontwikkeling.



# Laatste Sectie


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Beoordelingen


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Eindexamen


<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>



<isCourseExam>true</isCourseExam>

## Conclusie



<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>


<isCourseConclusion>true</isCourseConclusion>