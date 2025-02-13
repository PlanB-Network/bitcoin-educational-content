---
name: RGB CLI
description: Kuidas luua ja vahetada RGB-s nutikaid lepinguid?
---
![cover](assets/cover.webp)

Selles õpetuses jälgime lepingu kirjutamise protsessi samm-sammult, kasutades LNP/BP ühingu loodud käsurea tööriista `rgb`. Eesmärk on näidata, kuidas paigaldada ja manipuleerida CLI-d, koostada skeem, importida liides ja liidesete rakendus ning seejärel väljastada RGB vara. Samuti vaatleme aluseks olevat loogikat, sealhulgas kompileerimist ja oleku valideerimist. Selle õpetuse lõpus peaksite olema võimelised seda protsessi reprodutseerima ja looma oma RGB-lepinguid.

## RGB-protokolli meeldetuletus

RGB on protokoll, mis töötab Bitcoini peal ning jäljendab nutika lepingu funktsionaalsust ja digitaalse vara haldamist, ilma et see koormaks selle aluseks olevat plokiahelat üle. Erinevalt tavapärastest ahelasisestest nutikontrahenditest (nagu näiteks Ethereumis) tugineb RGB "*kliendipoolse valideerimise*" süsteemile: enamikku andmeid ja olekuhinnanguid vahetavad ja salvestavad ainult asjaomased osalejad, samas kui Bitcoini plokiahelas on ainult väikesed krüptograafilised kohustused (selliste mehhanismide kaudu nagu *Tapret* või *Opret*). RGB-protokollis toimib Bitcoini plokiahel seega ainult ajamärgistamise serveri ja topeltkulutuste kaitsesüsteemina.

RGB leping on üles ehitatud nagu evolutsiooniline riigimasin. See algab Genesis'iga, mis määratleb algse seisundi (kirjeldab näiteks pakkumist, jooksevust või muid metaandmeid) vastavalt rangelt tüpiseeritud ja kompileeritud skeemile. Seejärel rakendatakse oleku üleminekuid ja vajaduse korral oleku laiendusi selle oleku muutmiseks või laiendamiseks. Iga operatsioon, olgu see siis asendatavate varade ülekandmine (RGB20) või unikaalsete varade loomine (RGB21), hõlmab *Kaheksakordseid pitsatite* kasutamist. Need seovad Bitcoini UTXOd ahelavälise olekuga ja hoiavad ära topeltkulutused, tagades samas konfidentsiaalsuse ja skaleeritavuse.

Kui soovite rohkem teada saada, kuidas RGB-protokoll töötab, soovitan teil läbida selle põhjaliku koolituskursuse:

https://planb.network/courses/csv402
RGB sisemine loogika põhineb Rust-raamatukogudel, mida te arendajatena saate oma projektidesse importida, et hallata *kliendipoolset valideerimist*. Lisaks töötab LNP/BP meeskond teiste keelte jaoks mõeldud sidemete kallal, kuid see ei ole veel lõplikult välja töötatud. Lisaks arendavad teised üksused, nagu Bitfinex, oma integratsioonipakette, kuid nendest räägime teises õpetuses. Hetkel on `rgb` CLI ametlik viide, isegi kui see on veel suhteliselt viimistlemata.

## Tööriista rgb CLI paigaldamine ja tutvustamine

Peamine käsk on lihtsalt `rgb`. See on loodud nii, et see meenutab `git`i, koos alamkäskude komplektiga lepingute manipuleerimiseks, nende kutsumiseks, varade väljastamiseks ja nii edasi. Bitcoin Wallet ei ole praegu integreeritud, kuid see saab olema peatses versioonis (0.11). See järgmine versioon võimaldab kasutajatel luua ja hallata oma rahakotte (kirjelduste kaudu) otse `rgb`st, sealhulgas PSBT genereerimine, ühilduvus välise riistvara (nt riistvaraline rahakott) allkirjastamiseks ja koostalitlusvõime sellise tarkvaraga nagu Sparrow. See lihtsustab kogu varade väljastamise ja ülekandmise stsenaariumi.

### Paigaldamine Cargo kaudu

Me paigaldame tööriista Rust koos :

```bash
cargo install rgb-contracts --all-features
```

(Märkus: crate'i nimi on `rgb-contracts` ja installeeritud käsu nimi on `rgb`. Kui crate nimega `rgb` oli juba olemas, võis tekkida kokkupõrge, sellest ka nimi)

Paigaldus koostab suure hulga sõltuvusi (nt käskude parsimine, Electrumi integreerimine, nullteadmiste tõendite haldamine jne).

Kui paigaldus on lõpetatud, saab :

```bash
rgb
```

Käivitades `rgb` (ilma argumentideta), kuvatakse nimekiri olemasolevatest alamkäskudest, näiteks `liidesed`, `skeem`, `import`, `eksport`, `väljastus`, `arve`, `ülekanne` jne. Saate muuta lokaalset salvestuskataloogi (peidik, mis sisaldab kõiki logisid, skeeme ja rakendusi), valida võrgu (testnet, mainnet) või konfigureerida oma Electrumi serverit.

![RGB-CLI](assets/fr/01.webp)

### Esimene ülevaade kontrollide kohta

Kui käivitate järgmise käsu, näete, et `RGB20` liides on juba vaikimisi integreeritud:

```bash
rgb interfaces
```

Kui see liides ei ole integreeritud, kloonige :

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Koostage see:

```bash
cargo run
```

Seejärel importige valitud kasutajaliides:

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-CLI](assets/fr/02.webp)

Meile on aga öeldud, et ühtegi skeemi ei ole veel tarkvarasse imporditud. Samuti ei ole lepingut kätkesse pandud. Et seda näha, käivitage käsk :

```bash
rgb schemata
```

Seejärel saate kloonida repositooriumi teatud skeemide saamiseks:

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-CLI](assets/fr/03.webp)

See repositoorium sisaldab oma kataloogis `src/` mitmeid Rust-faile (näiteks `nia.rs`), mis määratlevad skeemid (NIA nagu "*Non Inflatable Asset*", UDA nagu "*Unique Digital Asset*" jne). Kompileerimiseks saab seejärel käivitada :

```bash
cd rgb-schemata
cargo run
```

See genereerib mitu faili `.rgb` ja `.rgba`, mis vastavad kompileeritud skeemidele. Näiteks leiad `NonInflatableAsset.rgb`.

### Skeemi ja liidese rakendamise importimine

Nüüd saab skeemi importida `rgb`-sse:

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-CLI](assets/fr/04.webp)

See lisab selle kohalikku varandusse. Kui käivitame järgmise käsu, näeme, et skeem ilmub nüüd:

```bash
rgb schemata
```

## Lepingu loomine (väljastamine)

Uue vara loomiseks on kaks lähenemisviisi:


- Kas me kasutame skripti või koodi Rustis, mis koostab lepingu, täites skeemi väljad (globaalne olek, omandatud olekud jne) ja toodab `.rgb` või `.rgba` faili;
- Või kasutage otse alamkäsklust `issue` koos YAML (või TOML) failiga, mis kirjeldab sümboli omadusi.

Rustis leiate näiteid kaustast `examples`, mis illustreerivad, kuidas ehitada `ContractBuilder`, täita `globaalne olek` (vara nimi, ticker, pakkumine, kuupäev jne), määrata Owned State (millisele UTXO-le see on määratud), seejärel koostada kõik see *lepingu saadetiseks*, mida saab eksportida, valideerida ja importida stash'ile.

Teine võimalus on käsitsi muuta YAML-faili, et kohandada `ticker`, `name`, `supply` jne. Oletame, et faili nimi on `RGB20-demo.yaml`. Saate määrata :


- `spec`: ticker, nimi, täpsus ;
- `terms`: väli juriidiliste teadete jaoks ;
- `issuedSupply` : väljastatud märgise kogus ;
- `assignments`: näitab ühekordselt kasutatavat pitserit (*pitseri määratlus*) ja lukustamata kogust.

Siin on näide YAML-faili loomiseks:

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

Seejärel käivitage lihtsalt käsk :

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-CLI](assets/fr/06.webp)

Minu puhul on unikaalne skeemi identifikaator (mis tuleb sulgeda jutumärkidesse) `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` ja ma ei ole sisestanud ühtegi väljastajat. Nii et minu tellimus on :

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

Kui te ei tea skeemi ID-d, käivitage käsk :

```bash
rgb schemata
```

CLI vastab, et uus leping on väljastatud ja lisatud varandusse. Kui me sisestame järgmise käsu, näeme, et nüüd on olemas täiendav leping, mis vastab äsja väljastatud lepingule:

```bash
rgb contracts
```

![RGB-CLI](assets/fr/07.webp)

Seejärel kuvatakse järgmise käsuga globaalsed olekud (nimi, ticker, pakkumine...) ja nimekiri Owned States, st eraldised (näiteks 1 miljon `PBN` tokenit, mis on määratletud UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).

```bash
rgb state '<ContractId>'
```

![RGB-CLI](assets/fr/08.webp)

## Eksport, import ja valideerimine

Et jagada seda lepingut teiste kasutajatega, saab selle eksportida peidikust :

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-CLI](assets/fr/09.webp)

Faili `myContractPBN.rgb` saab edasi anda teisele kasutajale, kes saab selle lisada oma varamusse käsuga :

```bash
rgb import myContractPBN.rgb
```

Kui tegemist on lihtsa *lepingulise kaubasaadetisega*, saame importimisel teate "`Importing consignment rgb`" (kaubasaadetise importimine rgb). Kui tegemist on suurema *riigi ülemineku saadetisega*, on käsk teistsugune (`rgb accept`).

Kehtivuse tagamiseks võite kasutada ka kohalikku valideerimisfunktsiooni. Näiteks võite käivitada :

```bash
rgb validate myContract.rgb
```

### Varamu kasutamine, kontrollimine ja kuvamine

Meeldetuletuseks, et varamu on skeemide, liideste, rakenduste ja lepingute (Genesis + üleminekud) kohalik inventar. Iga kord, kui te käivitate "import", lisate elemendi varamusse. Seda varandust saab üksikasjalikult vaadata käsuga :

```bash
rgb dump
```

![RGB-CLI](assets/fr/10.webp)

See loob kausta kogu varanduse üksikasjadega.

## Ülekanne ja PSBT

Ülekande teostamiseks peate manipuleerima kohalikku Bitcoini rahakotti, et hallata "Tapret" või "Opret" kohustusi.

### Loo arve

Enamasti toimub lepingus osalejate (nt Alice ja Bob) vaheline suhtlus arve koostamise kaudu. Kui Alice soovib, et Bob täidaks midagi (sümboolika ülekandmine, uuesti väljastamine, tegevus DAOs jne), loob Alice arve, milles kirjeldatakse üksikasjalikult tema juhiseid Bobile. Seega on meil :


- Alice** (arve väljastaja) ;
- Bob** (kes võtab arve vastu ja täidab selle).

Erinevalt teistest ökosüsteemidest ei ole RGB-arve piiratud makse mõistega. Sellesse võib sisse põimida mis tahes lepinguga seotud taotluse: võtme tühistamine, hääletamine, NFT-le graveeringu (*graveeringu*) loomine jne. Vastavat toimingut saab kirjeldada lepingu liideses. Vastavat toimingut saab kirjeldada lepingu liideses.

Järgmine käsk genereerib RGB-arve:

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

Koos :


- `$CONTRACT`: Lepingu identifikaator (*ContractId*) ;
- `$INTERFACE`: kasutatav liides (nt `RGB20`) ;
- `$ACTION`: liideses määratud operatsiooni nimi (lihtsa asendatava sümboli ülekande puhul võib see olla "Transfer"). Kui liides juba pakub vaikimisi tegevust, ei ole vaja seda siin uuesti sisestada;
- `$STATE`: üleantavad olekute andmed (näiteks žetoonide hulk, kui üle kantakse asendatav žetoon);
- `$SEAL`: abisaaja (Alice'i) ühekordselt kasutatav pitsat, st selgesõnaline viide UTXO-le. Bob kasutab seda infot tunnistustehingu koostamiseks ja vastav väljund kuulub seejärel Alice'ile (*pimedas UTXO* või krüpteerimata kujul).

Näiteks järgmiste käskudega

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

CLI genereerib arve nagu :

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

Seda saab edastada Bobile mis tahes kanali kaudu (tekst, QR-kood jne).

### Ülekande tegemine

Sellest arvest ülekandmiseks :


- Bobil (kes hoiab žetoonid oma peidus) on Bitcoini rahakott. Ta peab ette valmistama Bitcoini tehingu (PSBT kujul, nt `tx.psbt`), mis kulutab UTXO-d, kus asuvad vajalikud RGB-märgid, pluss üks UTXO valuuta jaoks (vahetus) ;
- Bob täidab järgmise käsu:

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- See genereerib faili `consignment.rgb`, mis sisaldab :
 - Ülemineku ajalugu, mis tõestab Alice'ile, et märgid on ehtsad;
 - Uus üleminek, mis kannab märgid üle Alice'i ühekordselt kasutatavale pitserile ;
 - Tunnistaja tehing (allkirjastamata).
- Bob saadab selle faili `consignment.rgb` Alice'ile (e-posti, jagamisserveri või RGB-RPC-protokolli, Stormi jne kaudu);
- Alice saab `consignment.rgb` ja võtab selle oma peidikusse:

```bash
alice$ rgb accept consignment.rgb
```


- CLI kontrollib ülemineku kehtivust ja lisab selle Alice'i varandusse. Kui käsk on kehtetu, ebaõnnestub see koos üksikasjalike veateadetega. Vastasel juhul õnnestub see ja teatab, et näidistehingut ei ole veel Bitcoini võrgus edastatud (Bob ootab Alice'i rohelist tuld);
- Kinnituseks saadab käsk `accept` allkirja (*maksekviitung*), mille Alice saab saata Bobile, et näidata talle, et ta on *saatekirja* kinnitanud;
- Seejärel saab Bob allkirjastada ja avaldada (--- avaldada) oma Bitcoini tehingu:

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- Niipea, kui see tehing on ahelas kinnitatud, loetakse vara omandiõigus Alice'ile üle läinud. Alice'i rahakott, mis jälgib tehingu kaevandamist, näeb, et tema varakambrisse ilmub uus Owned State.

Te teate nüüd, kuidas RGB-lepingut sõlmida ja üle kanda. Kui leidsite selle õpetuse kasulikuks, oleksin väga tänulik, kui paneksite alla rohelise pöidla. Palun jagage seda artiklit julgelt oma sotsiaalvõrgustikes. Tänan teid väga!

Soovitan ka seda teist õpetust, kus ma selgitan, kuidas käivitada RGB-ühilduv Lightning-sõlm, et vahetada märgid peaaegu koheselt:

https://planb.network/tutorials/node/rgb/rln-ffc02528-329b-4e16-bd83-873d0299feea