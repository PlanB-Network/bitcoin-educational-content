---
name: RGB CLI
description: Hur skapar jag och Exchange smarta kontrakt på RGB?
---
![cover](assets/cover.webp)


I den här handledningen följer vi steg-för-steg-processen för att skriva en Contract med hjälp av kommandoradsverktyget `RGB` som skapats av LNP/BP-föreningen. Syftet är att visa hur man installerar och manipulerar CLI, kompilerar en Schema, importerar Interface och Interface Implementation och sedan utfärdar en RGB-tillgång. Vi tittar också på den underliggande logiken, inklusive kompilering och validering av tillstånd. I slutet av denna handledning ska du kunna reproducera processen och skapa dina egna RGB-kontrakt.


## Påminnelse om RGB-protokoll


RGB är ett protokoll som körs ovanpå Bitcoin och emulerar Smart contract-funktionalitet och digital tillgångshantering, utan att överbelasta Blockchain som det är baserat på. Till skillnad från konventionella On-Chain smarta kontrakt (som till exempel på Ethereum) förlitar sig RGB på ett "* Client-side Validation*"-system: majoriteten av data och statushistorik utbyts och lagras uteslutande av de inblandade deltagarna, medan Bitcoin Blockchain endast är värd för små kryptografiska åtaganden (via mekanismer som *Tapret* eller *Opret*). I RGB-protokollet fungerar Bitcoin Blockchain därför endast som en tidsstämplingsserver och Double-spending-skyddssystem.


En RGB Contract är strukturerad som en evolutionär tillståndsmaskin. Den börjar med en Genesis som definierar det initiala tillståndet (som t.ex. beskriver Supply, ticker eller andra metadata) enligt en strikt typad och kompilerad Schema. Tillståndsövergångar och, vid behov, tillståndsutvidgningar tillämpas sedan för att ändra eller utöka detta tillstånd. Varje operation, oavsett om det gäller överföring av fungibla tillgångar (RGB20) eller skapande av unika tillgångar (RGB21), omfattar *Single-use Seals*. Dessa länkar Bitcoin UTXO:er till off-chain-stater och förhindrar dubbla utgifter, samtidigt som de säkerställer sekretess och skalbarhet.


Om du vill lära dig mer om hur RGB-protokollet fungerar rekommenderar jag att du går den här omfattande utbildningen:


https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

Den interna logiken i RGB är baserad på Rust-bibliotek som du som utvecklare kan importera till dina projekt för att hantera *Client-side Validation*-delen. Dessutom arbetar LNP/BP-teamet med bindningar för andra språk, men detta har ännu inte slutförts. Dessutom utvecklar andra enheter som Bitfinex sina egna integrationsstackar, men vi kommer att prata om dessa i en annan handledning. För närvarande är `RGB` CLI den officiella referensen, även om den förblir relativt opolerad.


## Installation och presentation av RGB CLI-verktyget


Huvudkommandot kallas helt enkelt `RGB`. Det är utformat för att påminna om `git`, med en uppsättning underkommandon för att manipulera kontrakt, åberopa dem, utfärda tillgångar och så vidare. Bitcoin Wallet är för närvarande inte integrerat, men kommer att vara det i en kommande version (0.11). Denna nästa version kommer att göra det möjligt för användare att skapa och hantera sina plånböcker (via deskriptorer) direkt från `RGB`, inklusive PSBT-generering, kompatibilitet med extern hårdvara (t.ex. en Hardware Wallet) för signering och interoperabilitet med programvara som Sparrow. Detta kommer att förenkla hela scenariot för utfärdande och överföring av tillgångar.


### Installation via Cargo


Vi installerar verktyget i Rust med :


```bash
cargo install rgb-contracts --all-features
```


(Notera: lådan heter `RGB-contracts`, och det installerade kommandot kommer att heta `RGB`. Om en crate med namnet `RGB` redan existerade, kan det ha skett en kollision, därav namnet)


Installationen sammanställer ett stort antal beroenden (t.ex. kommandoparsning, Electrum-integrering, hantering av nollkunskapsbevis etc.)


När installationen är slutförd kommer :


```bash
rgb
```


Om du kör `RGB` (utan argument) visas en lista över tillgängliga underkommandon, t.ex. `interfaces`, `Schema`, `import`, `export`, `issue`, `Invoice`, `transfer`, etc. Du kan ändra den lokala lagringskatalogen (en Stash som innehåller alla loggar, scheman och implementeringar), välja nätverk (Testnet, Mainnet) eller konfigurera din Electrum-server.


![RGB-CLI](assets/fr/01.webp)


### Första översikten över kontroller


När du kör följande kommando kommer du att se att en `RGB20` Interface redan är integrerad som standard:


```bash
rgb interfaces
```


Om denna Interface inte är integrerad, klona :


```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```


Kompilera den:


```bash
cargo run
```


Importera sedan den Interface som du vill ha:


```bash
rgb import interfaces/RGB20.rgb
```


![RGB-CLI](assets/fr/02.webp)


Vi har dock fått veta att ingen Schema ännu har importerats till programvaran. Inte heller finns det en Contract i Stash. För att se det, kör kommandot :


```bash
rgb schemata
```


Du kan sedan klona arkivet för att hämta vissa scheman:


```bash
git clone https://github.com/RGB-WG/rgb-schemata
```


![RGB-CLI](assets/fr/03.webp)


Detta arkiv innehåller, i katalogen `src/`, flera Rust-filer (till exempel `nia.rs`) som definierar scheman (NIA för "*Non Inflatable Asset*", UDA för "*Unique Digital Asset*", etc.). För att kompilera kan du sedan köra :


```bash
cd rgb-schemata
cargo run
```


Detta genererar flera `.RGB`- och `.rgba`-filer som motsvarar de sammanställda schemana. Till exempel hittar du `NonInflatableAsset.RGB`.


### Import av Schema och Interface Implementation


Du kan nu importera schemat till `RGB` :


```bash
rgb import schemata/NonInflatableAssets.rgb
```


![RGB-CLI](assets/fr/04.webp)


Detta lägger till den till den lokala Stash. Om vi kör följande kommando ser vi att Schema nu visas:


```bash
rgb schemata
```


## Contract skapande (utgivning)


Det finns två sätt att skapa en ny tillgång:




- Antingen använder vi ett skript eller en kod i Rust som bygger en Contract genom att fylla i Schema-fält (Global State, Owned States, etc.) och producerar en `.RGB` eller `.rgba`-fil;
- Du kan också använda underkommandot `issue` direkt, med en YAML-fil (eller TOML-fil) som beskriver tokenens egenskaper.


Du kan hitta exempel i Rust i mappen `examples`, som illustrerar hur du bygger en `ContractBuilder`, fyller i `Global State` (tillgångsnamn, ticker, Supply, datum, etc.), definierar Owned State (till vilken UTXO den är tilldelad) och sedan sammanställer allt detta till en *Contract Consignment* som du kan exportera, validera och importera till en Stash.


Det andra sättet är att manuellt redigera en YAML-fil för att anpassa `ticker`, `name`, `Supply` och så vidare. Anta att filen heter `RGB20-demo.yaml`. Du kan ange :




- `spec`: ticker, namn, precision ;
- "Termer": ett fält för juridiska meddelanden ;
- `issuedSupply` : mängden utgivna token ;
- `assignments`: anger Single-Use Seal (*Seal Definition*) och den mängd som är upplåst.


Här är ett exempel på en YAML-fil som kan skapas:


```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
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


Kör sedan helt enkelt kommandot :


```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```


![RGB-CLI](assets/fr/06.webp)


I mitt fall är den unika Schema-identifieraren (som ska omslutas av enkla citattecken) `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` och jag har inte angett någon emittent. Så min order är :


```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```


Om du inte känner till Schema-ID:t kör du kommandot :


```bash
rgb schemata
```


CLI svarar att en ny Contract har utfärdats och lagts till Stash. Om vi skriver följande kommando ser vi att det nu finns ytterligare en Contract, motsvarande den som just utfärdats:


```bash
rgb contracts
```


![RGB-CLI](assets/fr/07.webp)


Därefter visar nästa kommando de globala staterna (namn, ticker, Supply...) och listan över Owned States, dvs. tilldelningar (till exempel 1 miljon `PBN` tokens definierade i UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).


```bash
rgb state '<ContractId>'
```


![RGB-CLI](assets/fr/08.webp)


## Export, import och validering


För att dela denna Contract med andra användare kan den exporteras från Stash till en :


```bash
rgb export '<ContractId>' myContractPBN.rgb
```


![RGB-CLI](assets/fr/09.webp)


Filen `myContractPBN.RGB` kan överlåtas till en annan användare, som kan lägga till den i sin Stash med kommandot :


```bash
rgb import myContractPBN.rgb
```


Vid import, om det är en enkel *Contract Consignment*, får vi ett "`Importing Consignment RGB`"-meddelande. Om det är en större *State Transition Consignment* kommer kommandot att vara annorlunda (`RGB accept`).


För att säkerställa giltigheten kan du också använda den lokala valideringsfunktionen. Du kan t.ex. köra :


```bash
rgb validate myContract.rgb
```


### Användning, verifiering och visning av Stash


Som en påminnelse är Stash en lokal inventering av scheman, gränssnitt, implementeringar och kontrakt (Genesis + övergångar). Varje gång du kör "import" lägger du till ett element i Stash. Denna Stash kan ses i detalj med kommandot :


```bash
rgb dump
```


![RGB-CLI](assets/fr/10.webp)


Detta kommer generate en mapp med detaljer om hela Stash.


## Överföring och PSBT


För att genomföra en överföring måste du manipulera en lokal Bitcoin Wallet för att hantera åtagandena `Tapret` eller `Opret`.


### generate och Invoice


I de flesta fall sker interaktionen mellan deltagarna i en Contract (t.ex. Alice och Bob) via genereringen av en Invoice. Om Alice vill att Bob ska utföra något (en tokenöverföring, en återutgivning, en åtgärd i en DAO, etc.), skapar Alice en Invoice som beskriver hennes instruktioner till Bob. Så vi har :




- Alice** (utgivaren av Invoice) ;
- Bob** (som tar emot och verkställer Invoice).


Till skillnad från andra ekosystem är en RGB Invoice inte begränsad till begreppet betalning. Den kan bädda in vilken begäran som helst som är kopplad till Contract: återkalla en nyckel, rösta, skapa en gravyr (*gravyr*) på en NFT, etc. Motsvarande operation kan beskrivas i Contract Interface. Motsvarande operation kan beskrivas i Contract Interface.


Följande kommando genererar en RGB Invoice:


```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```


Med :




- `$Contract`: Contract identifierare (*ContractId*) ;
- `$Interface`: den Interface som ska användas (t.ex. `RGB20`) ;
- `$ACTION`: namnet på den åtgärd som anges i Interface (för en enkel överföring av fungibla token kan detta vara "Transfer"). Om Interface redan innehåller en standardåtgärd behöver du inte ange den igen här;
- `$STATE`: de statusdata som ska överföras (t.ex. ett antal tokens om en fungibel token överförs);
- `$Seal`: mottagarens (Alices) Single-Use Seal, dvs. en uttrycklig hänvisning till en UTXO. Bob kommer att använda denna information för att bygga Witness Transaction, och motsvarande utdata kommer då att tillhöra Alice (i *blinded UTXO* eller okrypterad form).


Till exempel med följande kommandon


```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```


CLI kommer att generate och Invoice som :


```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```


Den kan överföras till Bob via valfri kanal (text, QR-kod etc.).


### Att göra en överföring


För att överföra från denna Invoice :




- Bob (som har polletterna i sin Stash) har en Bitcoin Wallet. Han måste förbereda en Bitcoin-transaktion (i form av en PSBT, t.ex. `tx.PSBT`) som spenderar UTXO:erna där de nödvändiga RGB-tokens finns, plus en UTXO för valuta (Exchange) ;
- Bob utför följande kommando:


```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```




- Detta genererar filen `Consignment.RGB` som innehåller :
 - Övergångshistorien bevisar för Alice att polletterna är äkta;
 - Den nya övergången som överför polletter till Alices Single-Use Seal ;
 - A Witness Transaction (osignerad).
- Bob skickar filen `Consignment.RGB` till Alice (via e-post, en delningsserver eller ett RGB-RPC-protokoll, Storm, etc.);
- Alice tar emot `Consignment.RGB` och accepterar den i sin egen Stash :


```bash
alice$ rgb accept consignment.rgb
```




- CLI kontrollerar giltigheten av övergången och lägger till den i Alices Stash. Om kommandot är ogiltigt misslyckas det med detaljerade felmeddelanden. I annat fall lyckas det och rapporterar att exempeltransaktionen ännu inte har sänts ut i Bitcoin-nätverket (Bob väntar på Alices Green light);
- Som bekräftelse returnerar kommandot `accept` en signatur (*payslip*) som Alice kan skicka till Bob för att visa honom att hon har validerat *Consignment* ;
- Bob kan sedan signera och publicera (`--publish`) sin Bitcoin-transaktion:


```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```




- Så snart denna transaktion bekräftas On-Chain, anses Ownership av tillgången ha överförts till Alice. Alices Wallet, som övervakar transaktionens Mining, ser den nya Owned State visas i dess Stash.


Du vet nu hur man utfärdar och överför en RGB Contract. Om du tyckte att den här handledningen var användbar skulle jag vara mycket tacksam om du satte en Green-tumme nedan. Du får gärna dela den här artikeln på dina sociala nätverk. Tack så mycket!


Jag rekommenderar också den här andra handledningen där jag förklarar hur man startar en RGB-kompatibel Lightning-nod till Exchange-tokens nästan omedelbart:


https://planb.network/tutorials/node/others/rln-ffc02528-329b-4e16-bd83-873d0299feea