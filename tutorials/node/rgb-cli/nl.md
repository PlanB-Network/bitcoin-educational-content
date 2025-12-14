---
name: RGB CLI
description: Hoe maak ik Exchange slimme contracten aan op RGB?
---
![cover](assets/cover.webp)


In deze tutorial volgen we het stap-voor-stap proces van het schrijven van een Contract, met behulp van het commandoregeltool `RGB`, gemaakt door de LNP/BP associatie. Het doel is om te laten zien hoe je de CLI installeert en manipuleert, een Schema compileert, de Interface en Interface Implementation importeert en vervolgens een RGB asset uitbrengt. We bekijken ook de onderliggende logica, inclusief compilatie en toestandsvalidatie. Aan het einde van deze tutorial moet je het proces kunnen reproduceren en je eigen RGB contracten kunnen maken.


## Herinnering RGB protocol


RGB is een protocol dat bovenop Bitcoin draait en Smart contract functionaliteit en digitaal activabeheer emuleert, zonder de Blockchain waarop het gebaseerd is te overbelasten. In tegenstelling tot conventionele On-Chain smart contracts (zoals bijvoorbeeld op Ethereum), vertrouwt RGB op een "*Client-side Validation*" systeem: de meeste gegevens en statusgeschiedenissen worden uitsluitend uitgewisseld en opgeslagen door de betrokken deelnemers, terwijl de Bitcoin Blockchain alleen kleine cryptografische verbintenissen herbergt (via mechanismen zoals *Tapret* of *Opret*). In het RGB protocol dient de Bitcoin Blockchain daarom alleen als tijdstempelserver en Double-spending beveiligingssysteem.


Een RGB Contract is gestructureerd als een evolutionaire toestandsmachine. Het begint met een Genesis die de begintoestand definieert (die bijvoorbeeld de Supply, ticker of andere metadata beschrijft) volgens een strikt getypeerde en gecompileerde Schema. Vervolgens worden toestandsovergangen en, indien nodig, toestandsuitbreidingen toegepast om deze toestand te wijzigen of uit te breiden. Toestandsovergangen en, indien nodig, toestandsuitbreidingen worden dan toegepast om deze toestand te wijzigen of uit te breiden. Elke bewerking, of het nu gaat om het overbrengen van fungibele activa (RGB20) of het creëren van unieke activa (RGB21), heeft te maken met *eenmalige verzegelingen*. Deze verbinden Bitcoin UTXO's met off-chain staten en voorkomen dubbele uitgaven, terwijl ze vertrouwelijkheid en schaalbaarheid garanderen.


Om meer te leren over hoe het RGB protocol werkt, raad ik je aan deze uitgebreide training te volgen:


https://planb.academy/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

De interne logica van RGB is gebaseerd op Rust bibliotheken die je als ontwikkelaar kunt importeren in je projecten om het *Client-side Validation* deel te beheren. Daarnaast werkt het LNP/BP team aan bindingen voor andere talen, maar dit is nog niet afgerond. Daarnaast ontwikkelen andere entiteiten zoals Bitfinex hun eigen integratiestacks, maar daar zullen we het in een andere tutorial over hebben. Voorlopig is de `RGB` CLI de officiële referentie, ook al is deze nog relatief ongepolijst.


## Installatie en presentatie van het RGB CLI gereedschap


Het hoofdcommando heet simpelweg `RGB`. Het is ontworpen om te lijken op `git`, met een set sub-commando's voor het manipuleren van contracten, het aanroepen ervan, het uitgeven van activa enzovoort. Bitcoin Wallet is momenteel nog niet geïntegreerd, maar dat zal wel gebeuren in een volgende versie (0.11). Deze volgende versie zal gebruikers in staat stellen hun wallets te creëren en te beheren (via descriptors) direct vanuit `RGB`, inclusief PSBT generatie, compatibiliteit met externe hardware (bijv. een Hardware Wallet) voor ondertekening, en interoperabiliteit met software zoals Sparrow. Dit zal de gehele uitgifte van activa vereenvoudigen. Dit zal het hele scenario van uitgifte en overdracht van activa vereenvoudigen.


### Installatie via Cargo


We installeren de tool in Rust met :


```bash
cargo install rgb-contracts --all-features
```


(Opmerking: het krat heet `RGB-contracten` en het geïnstalleerde commando zal `RGB` heten. Als er al een krat met de naam `RGB` bestond, kan er een botsing zijn geweest, vandaar de naam)


De installatie compileert een groot aantal afhankelijkheden (bijv. commandoparsing, Electrum-integratie, beheer van zero-knowledge bewijzen, enz.)


Zodra de installatie is voltooid, wordt de :


```bash
rgb
```


Het uitvoeren van `RGB` (zonder argumenten) toont een lijst met beschikbare sub-commando's, zoals `interfaces`, `Schema`, `import`, `export`, `issue`, `Invoice`, `transfer`, enz. Je kunt de lokale opslagmap wijzigen (een Stash die alle logs, schema's en implementaties bevat), het netwerk kiezen (Testnet, Mainnet) of je Electrum-server configureren.


![RGB-CLI](assets/fr/01.webp)


### Eerste overzicht van controles


Als je het volgende commando uitvoert, zul je zien dat er standaard al een `RGB20` Interface geïntegreerd is:


```bash
rgb interfaces
```


Als deze Interface niet geïntegreerd is, kloon dan de :


```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```


Compileer het:


```bash
cargo run
```


Importeer dan de Interface van je keuze:


```bash
rgb import interfaces/RGB20.rgb
```


![RGB-CLI](assets/fr/02.webp)


Er is ons echter verteld dat er nog geen Schema in de software is geïmporteerd. Er is ook geen Contract in de Stash. Om het te zien, voer je het commando :


```bash
rgb schemata
```


Je kunt dan het archief klonen om bepaalde schema's op te halen:


```bash
git clone https://github.com/RGB-WG/rgb-schemata
```


![RGB-CLI](assets/fr/03.webp)


Dit archief bevat in zijn `src/` map verschillende Rust bestanden (bijvoorbeeld `nia.rs`) die schema's definiëren (NIA voor "*Non Inflatable Asset*", UDA voor "*Unique Digital Asset*", enz.) Om te compileren kun je vervolgens :


```bash
cd rgb-schemata
cargo run
```


Dit genereert verschillende `.RGB` en `.rgba` bestanden die overeenkomen met de gecompileerde schema's. Je vindt hier bijvoorbeeld `NonInflatableAsset.RGB`.


### Schema en Interface Implementation importeren


Je kunt nu het schema importeren in `RGB`:


```bash
rgb import schemata/NonInflatableAssets.rgb
```


![RGB-CLI](assets/fr/04.webp)


Dit voegt het toe aan de lokale Stash. Als we het volgende commando uitvoeren, zien we dat de Schema nu verschijnt:


```bash
rgb schemata
```


## Contract creatie (uitgifte)


Er zijn twee manieren om een nieuw bedrijfsmiddel te maken:




- Of we gebruiken een script of code in Rust die een Contract opbouwt door Schema velden in te vullen (Global State, Owned States, enz.) en een `.RGB` of `.rgba` bestand produceert;
- Of gebruik het `issue` subcommando direct, met een YAML (of TOML) bestand dat de eigenschappen van de token beschrijft.


Je kunt voorbeelden vinden in Rust in de `examples` map, die illustreren hoe je een `ContractBuilder` bouwt, de `Global State` invult (activanaam, ticker, Supply, datum, etc.), de Owned State definieert (aan welke UTXO het wordt toegewezen) en dit alles vervolgens compileert in een *Contract Consignment* die je kunt exporteren, valideren en importeren in een Stash.


De andere manier is om handmatig een YAML-bestand te bewerken om de `ticker`, de `naam`, de `Supply`, enzovoort aan te passen. Stel dat het bestand `RGB20-demo.yaml` heet. Je kunt :




- `spec`: ticker, naam, precisie ;
- `terms`: een veld voor juridische kennisgevingen ;
- `issuedSupply` : de hoeveelheid token uitgegeven ;
- `toewijzingen`: geeft de Single-Use Seal (*Seal Definition*) en de ontgrendelde hoeveelheid aan.


Hier is een voorbeeld van een YAML-bestand om aan te maken:


```yaml
interface: RGB20Fixed
globals:
spec:
ticker: Plan ₿ Academy
name: Plan ₿ Academy
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```


![RGB-CLI](assets/fr/05.webp)


Voer dan gewoon het commando :


```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```


![RGB-CLI](assets/fr/06.webp)


In mijn geval is de unieke Schema identifier (tussen enkele aanhalingstekens) `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` en ik heb geen emittent opgegeven. Dus mijn bestelling is :


```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```


Als je de Schema ID niet weet, voer dan het commando :


```bash
rgb schemata
```


De CLI antwoordt dat er een nieuwe Contract is uitgegeven en toegevoegd aan de Stash. Als we het volgende commando intypen, zien we dat er nu een extra Contract is, die overeenkomt met de zojuist uitgegeven Contract:


```bash
rgb contracts
```


![RGB-CLI](assets/fr/07.webp)


Dan toont het volgende commando de globale toestanden (naam, ticker, Supply...) en de lijst van Owned States, d.w.z. toewijzingen (bijvoorbeeld 1 miljoen `Plan ₿ Academy` tokens gedefinieerd in UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).


```bash
rgb state '<ContractId>'
```


![RGB-CLI](assets/fr/08.webp)


## Exporteren, importeren en valideren


Om deze Contract te delen met andere gebruikers, kan deze worden geëxporteerd van de Stash naar een :


```bash
rgb export '<ContractId>' myContractPBN.rgb
```


![RGB-CLI](assets/fr/09.webp)


Het `myContractPBN.RGB` bestand kan worden doorgegeven aan een andere gebruiker, die het kan toevoegen aan zijn Stash met het commando :


```bash
rgb import myContractPBN.rgb
```


Bij het importeren, als het een eenvoudige *Contract Consignment* is, krijgen we een "`Importing Consignment RGB`" bericht. Als het een grotere *State Transition Consignment* is, zal het commando anders zijn (`RGB accepteren`).


Om de geldigheid te garanderen, kun je ook de lokale validatiefunctie gebruiken. Je zou bijvoorbeeld :


```bash
rgb validate myContract.rgb
```


### Stash gebruik, verificatie en weergave


Ter herinnering, het Stash is een lokale inventaris van schema's, interfaces, implementaties en contracten (Genesis + overgangen). Elke keer dat je "import" uitvoert, voeg je een element toe aan het Stash. Dit Stash kan in detail bekeken worden met het commando :


```bash
rgb dump
```


![RGB-CLI](assets/fr/10.webp)


Dit zal generate een map met details van de hele Stash.


## Overdracht en PSBT


Om een overdracht uit te voeren, moet je een lokale Bitcoin Wallet manipuleren om de `Tapret` of `Opret` verplichtingen te beheren.


### generate en Invoice


In de meeste gevallen vindt interactie tussen de deelnemers aan een Contract (bijv. Alice en Bob) plaats via het genereren van een Invoice. Als Alice wil dat Bob iets uitvoert (een token overdracht, een heruitgifte, een actie in een DAO, enz. Als Alice wil dat Bob iets uitvoert (een token overdracht, een heruitgifte, een actie in een DAO, etc.), dan creëert Alice een Invoice met haar instructies aan Bob. Dus we hebben :




- **Alice** (de emittent van de Invoice) ;
- **Bob** (die de Invoice ontvangt en uitvoert).


In tegenstelling tot andere ecosystemen is een RGB Invoice niet beperkt tot het begrip betaling. Het kan elk verzoek bevatten dat gekoppeld is aan de Contract: een sleutel intrekken, stemmen, een gravure (*gravure*) maken op een NFT, enz. De overeenkomstige bewerking kan worden beschreven in de Contract Interface. De overeenkomstige bewerking kan beschreven worden in Contract Interface.


Het volgende commando genereert een RGB Invoice:


```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```


Met :




- `$Contract`: Contract identificator (*ContractId*) ;
- `$Interface`: de Interface die moet worden gebruikt (bijv. `RGB20`) ;
- `$ACTIE`: de naam van de operatie die in de Interface is gespecificeerd (voor een eenvoudige fungibele token overdracht kan dit "Transfer" zijn). Als de Interface al een standaardactie geeft, hoef je die hier niet opnieuw in te voeren;
- `$STATE`: de statusgegevens die moeten worden overgedragen (bijvoorbeeld een aantal tokens als een fungibele token wordt overgedragen);
- `$Seal`: de Single-Use Seal van de begunstigde (Alice), dus een expliciete verwijzing naar een UTXO. Bob zal deze info gebruiken om de Witness Transaction te bouwen, en de overeenkomstige uitvoer zal dan toebehoren aan Alice (in *blinded UTXO* of ongecodeerde vorm).


Bijvoorbeeld met de volgende commando's


```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```


De CLI zal generate en Invoice zoals :


```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```


Het kan via elk kanaal (tekst, QR-code, enz.) naar de Bob worden verzonden.


### Een overdracht doen


Om van deze Invoice :




- Bob (die de tokens in zijn Stash heeft) heeft een Bitcoin Wallet. Hij moet een Bitcoin transactie voorbereiden (in de vorm van een PSBT, bijvoorbeeld `tx.PSBT`) die de UTXO's uitgeeft waar de benodigde RGB tokens zich bevinden, plus één UTXO voor valuta (Exchange);
- Bob voert het volgende commando uit:


```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```




- Dit genereert een `Consignment.RGB` bestand dat :
 - De transitiegeschiedenis bewijst Alice dat de penningen echt zijn;
 - De nieuwe overgang die lopers overbrengt naar Alice's Single-Use Seal ;
 - A Witness Transaction (niet ondertekend).
- Bob stuurt dit `Consignment.RGB` bestand naar Alice (via e-mail, een sharing server of een RGB-RPC protocol, Storm, etc.);
- Alice ontvangt `Consignment.RGB` en accepteert het in zijn eigen Stash :


```bash
alice$ rgb accept consignment.rgb
```




- De CLI controleert de geldigheid van de overgang en voegt deze toe aan de Stash van de Alice. Als het commando ongeldig is, mislukt het met gedetailleerde foutmeldingen. Anders slaagt het en meldt dat de voorbeeldtransactie nog niet is uitgezonden op het Bitcoin netwerk (Bob wacht op Alice's Green licht);
- Ter bevestiging retourneert het `accept` commando een handtekening (*betaalbrief*) die Alice naar Bob kan sturen om hem te laten zien dat ze de *Consignment* heeft gevalideerd;
- Bob kan dan zijn Bitcoin transactie ondertekenen en publiceren (`--publiceren`):


```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```




- Zodra deze transactie is bevestigd On-Chain, wordt Ownership van het actief beschouwd als overgedragen aan Alice. Wallet van Alice, die de Mining van de transactie controleert, ziet de nieuwe Owned State verschijnen in zijn Stash.


Je weet nu hoe je een RGB Contract moet uitgeven en overzetten. Als je deze tutorial nuttig vond, zou ik je erg dankbaar zijn als je hieronder een Green duim plaatst. Voel je vrij om dit artikel te delen op je sociale netwerken. Hartelijk dank!


Ik raad ook deze andere tutorial aan, waarin ik uitleg hoe je een RGB-compatibel Lightning knooppunt bijna ogenblikkelijk naar Exchange tokens kunt lanceren:


https://planb.academy/tutorials/node/others/rln-ffc02528-329b-4e16-bd83-873d0299feea