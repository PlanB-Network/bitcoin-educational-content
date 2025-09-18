---
name: RGB CLI
description: Ni gute nokora na Exchange amasezerano y’ubwenge kuri RGB?
---
![cover](assets/cover.webp)


Muri iyi nyigisho, tuzokurikira intambwe ku yindi inzira yo kwandika Contract, dukoresheje igikoresho c'umurongo w'amabwirizwa `RGB` cakozwe n'ishirahamwe LNP/BP. Intumbero ni ukwerekana ingene umuntu yoshiramwo no gukoresha CLI, gukoranya Schema, akazana Interface na Interface Implementation, hanyuma agatanga umutungo wa RGB. Turaza kuraba kandi ivyiyumviro bishingiyeko, harimwo n’ugukoranya n’ugushingira intahe. Mu mpera z’iyi nyigisho, ushobora gusubiramwo iyo nzira maze ugakora amasezerano yawe bwite ya RGB.


## RGB ivyibutsa


RGB ni porotokole ikora hejuru ya Bitcoin kandi yigana imikorere ya Smart contract n’ugucungera umutungo w’ubuhinga bwa none, ata kuremerera cane Blockchain ishingiyeko. Udakunze amasezerano asanzwe y'ubwenge ya On-Chain (nk'akarorero kuri Ethereum), RGB yizigira uburyo bwa "*Client-side Validation*": amakuru menshi n'amateka y'ivy'ubuzima birahindurwa kandi bikabikwa gusa n'abaje mu nama, mu gihe Bitcoin Blockchain ikoresha gusa ubuhinga buto buto ( *Guvuga*). Mu masezerano ya RGB, Bitcoin Blockchain rero ikora gusa nk’umurongo w’igihe n’uburyo bwo kurinda Double-spending.


RGB Contract itunganijwe nk’imashini y’igihugu y’iterambere. Bitangura na Genesis isobanura ivy'intango (idondora, nk'akarorero, Supply, ticker canke ibindi bimenyetso) hakurikijwe Schema yanditswe neza kandi ikoranijwe. Impinduka za Leta n’iyo bikenewe, Impinduka za Leta zica zikoreshwa kugira ngo zihindure canke zagure iyo Leta. Igikorwa kimwekimwe cose, haba mu kwimurira ibintu bishobora guhinduka (RGB20) canke mu kurema ibintu bidasanzwe (RGB21), birimwo *Ibimenyetso bikoreshwa rimwe*. Ivyo bihuza Bitcoin UTXOs n’intara za off-chain kandi bikabuza gukoresha amahera kabiri, mu gihe bituma habaho ibanga n’ugushobora gukoreshwa.


Kugira ngo umenye vyinshi ku bijanye n’ingene umurongo wa RGB ukora, ndagusavye gufata iyi nyigisho yuzuye:


https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

Intumbero y'imbere ya RGB ishingiye ku masomero ya Rust mwebwe nk'abahinguzi mushobora kwinjiza mu migambi yanyu kugira ngo mucunge igice ca *Client-side Validation*. Ikindi, umugwi wa LNP/BP uriko urakora ibijanye n’ugufatanya ibitabo vy’izindi ndimi, ariko ivyo ntibiraheza. Ikindi, ibindi bigo nka Bitfinex biriko birategura ibirundo vyavyo vy’ubufatanye, ariko ivyo tuzobivuga mu yindi nyigisho. Kugeza ubu, `RGB` CLI ni yo nzira yemewe, naho yoba iguma idasukuye cane.


## Gushiramwo no gushikiriza igikoresho ca RGB CLI


Itegeko nyamukuru ryitwa gusa `RGB`. Igenewe kwibutsa `git`, ifise amategeko mato mato yo gukoresha amasezerano, kuyahamagara, gutanga itunga n'ibindi. Bitcoin Wallet ubu ntabwo iriko irashirwamwo, ariko izoba iri muri verisiyo iri hafi (0.11). Iyi verisiyo ikurikira izotuma abakoresha bashobora gukora no gucunga amasakoshi yabo (biciye mu bisobanuro) bavuye kuri `RGB`, harimwo n'ivya PSBT, guhuza n'ibikoresho vyo hanze (nk'akarorero Hardware Wallet) vyo gusinya, no gukorana na porogarama nka Sparrow. Ivyo bizotuma igikorwa cose co gutanga no kwimurira umutungo coroha.


### Gushiramwo biciye ku mizigo


Dushiramwo igikoresho muri Rust na :


```bash
cargo install rgb-contracts --all-features
```


(Iciyumviro: iyo crate yitwa `RGB-contracts`, kandi itegeko ryashizweho rizokwitwa `RGB`. Iyo iyo crate yitwa `RGB` iba yaramaze kubaho, hariho ugutombora, ni co gituma iryo zina)


Ivyo bikoresho bikoranya umubare munini w'ibintu bishingiyeko (nk'ugusesangura amabwirizwa, gushiramwo Electrum, gucunga ibimenyamenya vy'ubumenyi zero, n'ibindi).


Igihe gushiramwo birangiye, :


```bash
rgb
```


Gukoresha `RGB` (ata mpamvu) yerekana urutonde rw'amabwirizwa mato ariho, nka `imirongo`, `Schema`, `kwinjiza`, `gusohora`, `ikibazo`, `Invoice`, `kwimurira`, n'ibindi. gushirwa mu ngiro), uhitemwo urubuga (Testnet, Mainnet) canke utunganye umukozi wawe wa Electrum.


![RGB-CLI](assets/fr/01.webp)


### Incamake ya mbere y'ibigenzura


Iyo ukoresheje itegeko rikurikira, uzobona ko `RGB20` Interface isanzwe yinjijwe:


```bash
rgb interfaces
```


Niba iyi Interface idashizwemwo, kora clone :


```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```


Bishire hamwe:


```bash
cargo run
```


Hanyuma ushiremwo Interface uhisemwo:


```bash
rgb import interfaces/RGB20.rgb
```


![RGB-CLI](assets/fr/02.webp)


Ariko rero, tubwirwa ko ata Schema irashirwa muri iyo porogarama. Eka mbere nta Contract iri muri Stash. Kugira ngo uyibone, koresha itegeko :


```bash
rgb schemata
```


Ushobora rero gukora clone y'ububiko kugira ngo ubone ibishushanyo bimwe bimwe:


```bash
git clone https://github.com/RGB-WG/rgb-schemata
```


![RGB-CLI](assets/fr/03.webp)


Ubu bubiko burimwo, mu bubiko bwayo bwa `src/`, amadosiye menshi ya Rust (nk'akarorero `nia.rs`) asobanura imirongo (NIA ku "*Itunga Ridashobora Gufutwa*", UDA ku "*Itunga ry'Igihugu*", n'ibindi). Kugira ngo ukoreshe, ushobora gukoresha :


```bash
cd rgb-schemata
cargo run
```


Ivyo bituma habaho amadosiye menshi `.RGB` na `.rgba` ahuye n'ibishushanyo vyakozwe. Nk'akarorero, uzosanga `Itunga Ridashobora Gufuka.RGB`.


### Kuzana Schema na Interface Implementation


Ubu ushobora kwinjiza igishushanyo muri `RGB` :


```bash
rgb import schemata/NonInflatableAssets.rgb
```


![RGB-CLI](assets/fr/04.webp)


Ivyo bica biyongera kuri Stash yo mu karere. Nitwakoresha itegeko rikurikira, turabona ko Schema ubu iboneka:


```bash
rgb schemata
```


## Contract iremwa (gusohora)


Hari uburyo bubiri bwo kurema umutungo mushasha:




- Canke dukoreshe inyandiko canke kode muri Rust yubaka Contract mu gushiramwo ivyicaro vya Schema (Global State, Ibihugu vy'Umutungo, n'ibindi) maze igatanga dosiye `.RGB` canke `.rgba`;
- Canke ukoreshe itegeko rito `ikibazo` ataco uhinduye, ufise dosiye ya YAML (canke TOML) idondora imiterere ya token.


Ushobora gusanga ingero muri Rust muri dosiye `ingero`, zigaragaza ingene wubaka `Uwukora Amasezerano`, wuzuze `Global State` (izina ry'umutungo, ikimenyetso, Supply, itariki, n'ibindi), usobanure Owned State (aho UTXO a compile muri *G Consignment* ushobora kwohereza hanze, kwemeza no kwinjiza muri Stash.


Ubundi buryo ni uguhindura n'amaboko dosiye ya YAML kugira ngo uhindure `ticker`, `izina`, `Supply`, n'ibindi. Twibaze ko dosiye yitwa `RGB20-demo.yaml`. Ushobora gusobanura :




- `spec`: ikimenyetso, izina, ukuri ;
- `amajambo`: umwanya w'amatangazo y'amategeko ;
- `Itanga` : umubare w'ama token yasohowe ;
- `ibikorwa`: vyerekana Single-Use Seal (*Seal Definition*) n'ingero zifunguwe.


Aha ni akarorero ka dosiye ya YAML yo kurema:


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


Hanyuma ukoreshe itegeko :


```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```


![RGB-CLI](assets/fr/06.webp)


Mu gihe canje, ikimenyetso kidasanzwe ca Schema (kizoshirwa mu bimenyetso bimwe bimwe) ni `RDYhMTR! Rero itegeko ryanje ni :


```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```


Niba utazi ID ya Schema, koresha itegeko :


```bash
rgb schemata
```


CLI yishura ko hariho Contract nshasha yasohotse yongewe kuri Stash. Nitwandika itegeko rikurikira, turabona ko ubu hariho Contract y’inyongera, ihuye n’iyiherutse gusohoka:


```bash
rgb contracts
```


![RGB-CLI](assets/fr/07.webp)


Hanyuma, itegeko rikurikira ryerekana ibihugu vyo kw’isi yose (izina, ikimenyetso, Supply...) n’urutonde rw’ibihugu vy’ubutunzi, ni ukuvuga ivy’ugutanga (nk’akarorero, ibimenyetso vy’imiliyoni 1 `PBN` bisobanuwe muri UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).


```bash
rgb state '<ContractId>'
```


![RGB-CLI](assets/fr/08.webp)


## Gusohora hanze, kwinjiza mu gihugu no kwemeza


Kugira ngo usangire iyi Contract n'abandi bakoresha, ishobora gusohoka kuva kuri Stash ikaja muri :


```bash
rgb export '<ContractId>' myContractPBN.rgb
```


![RGB-CLI](assets/fr/09.webp)


Dosiye `myContractPBN.RGB` ishobora gushikirizwa uwundi mukozi, ashobora kuyishira kuri Stash yiwe n'itegeko :


```bash
rgb import myContractPBN.rgb
```


Ku bijanye no kwinjiza, nimba ari *Contract Consignment* yoroshe, tuzoronka ubutumwa buvuga ngo "`Kuzana Consignment RGB`". Niba ari *State Transition Consignment* nini, itegeko rizoba ritandukanye (`RGB yemera`).


Kugira ngo ubone ko ari ukuri, ushobora kandi gukoresha igikorwa co kwemeza co mu karere. Nk'akarorero, ushobora kwiruka :


```bash
rgb validate myContract.rgb
```


### Stash ikoreshwa, kugenzura no kugaragaza


Nk’ukwibutsa, Stash ni urutonde rw’ibintu vyo mu karere vy’imirongo, imirongo, ugushirwa mu ngiro n’amasezerano (Genesis + transitions). Igihe cose ukoresheje "import", wongerako ikintu kuri Stash. Iyi Stash ishobora kurabwa mu buryo burambuye n'itegeko :


```bash
rgb dump
```


![RGB-CLI](assets/fr/10.webp)


Ivyo bizotuma generate igira dosiye irimwo amakuru yose ya Stash.


## Kwimurira na PSBT


Kugira ngo ukore ukwimurira, uzokenera gukoresha Bitcoin Wallet yo mu karere kugira ngo ucungere amasezerano ya `Tapret` canke `Opret`.


### generate na Invoice


Akenshi, ugukorana hagati y'abaje mu nama muri Contract (nk'akarorero Alice na Bob) bishika biciye mu guhingura Invoice. Iyo Alice ishaka ko Bob ikora ikintu (uguhindura token, gusubira gusohora, igikorwa muri DAO, n'ibindi), Alice irema Invoice idondora amabwirizwa yiwe kuri Bob. Rero dufise :




- Alice** (uwatanze iyo Invoice) ;
- Bob** (ni we yakira kandi agashitsa Invoice).


Mu buryo butandukanye n’ibindi bidukikije, RGB Invoice ntigarukira ku ciyumviro co kwishura gusa. Ishobora gushiramwo igisabwa cose gifitaniye isano na Contract: gukuraho urufunguzo, gutora, gukora igicapo (*igicapo*) kuri NFT, n'ibindi. Ivyo bishobora gusobanurwa muri Contract Interface.


Itegeko rikurikira ritanga RGB Invoice:


```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```


Hamwe :




- `$Contract`: Ikimenyetso ca Contract (*Id y'Isezerano*) ;
- `$Interface`: Interface izokoreshwa (nk'akarorero `RGB20`) ;
- `$ACTION`: izina ry'igikorwa kigaragazwa muri Interface (ku bijanye n'uguhindura token, ivyo bishobora kuba "Ukwimurira"). Niba Interface isanzwe itanga igikorwa c’imbere, ntukeneye kugisubiramwo hano;
- `$STATE`: amakuru y'imimerere azokwimurirwa (nk'akarorero, umubare w'ibimenyetso iyo token ishobora guhinduka irungitswe);
- `$Seal`: Single-Use Seal y'uwuronka inyungu (Alice), ni ukuvuga ivyerekeye UTXO. Bob izokoresha aya makuru kugira ngo yubake Witness Transaction, kandi igisubizo gihuye kizoba ica Alice (mu *blinded UTXO* canke mu buryo butagiramwo amakuru).


Nk’akarorero, n’amabwirizwa akurikira .


```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```


CLI izogira generate na Invoice nka :


```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```


Ishobora gushikirizwa Bob biciye ku nzira iyo ari yo yose (inyandiko, kode ya QR, n’ibindi).


### Kwimurira


Kugira ngo ushiremwo iyi Invoice :




- Bob (uwufise ibimenyetso muri Stash yiwe) afise Bitcoin Wallet. Arakeneye gutegura igikorwa co gucuruza Bitcoin (mu buryo bwa PSBT, nk’akarorero `tx.PSBT`) gikoresha ama UTXO aho ibimenyetso vya RGB bisabwa biri, yongerako UTXO imwe y’amahera (Exchange) ;
- Bob ikora itegeko rikurikira:


```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```




- Ibi bitanga dosiye `Consignment.RGB` irimwo :
 - Amateka y’ihinduka yerekana Alice ko ivyo bimenyetso ari ivy’ukuri;
 - Ihinduka rishasha ryimurira ibimenyetso ku Single-Use Seal ya Single-Use Seal ;
 - Igitabo ca Witness Transaction (kitashizweko umukono).
- Bob yohereza iyi dosiye `Consignment.RGB` kuri Alice (biciye kuri e-mail, kuri server yo gusangira canke ku nzira ya RGB-RPC, Igihuhusi, n’ibindi);
- Alice yakira `Consignment.RGB` ikayemera muri Stash yayo bwite :


```bash
alice$ rgb accept consignment.rgb
```




- CLI isuzuma ko iyo mpinduka ari nziza maze ikayongera ku Stash ya Alice. Iyo ataco bimaze, itegeko rirananirwa n'ubutumwa bw'ikosa burambuye. Ahandi ho, biraroranirwa, kandi bikavuga ko iyo nzira y’ugucuruza y’akarorero itaratangazwa ku rubuga rwa Bitcoin (Bob irindiriye umuco wa Alice wa Green);
- Mu buryo bwo kwemeza, itegeko `kwemera` rigarura umukono (*payslip*) Alice ashobora kohereza kuri Bob kugira ngo amwereke ko yemeje *Consignment* ;
- Bob ashobora rero gusinya no gutangaza (`--gutangaza`) ibikorwa vyiwe vya Bitcoin:


```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```




- Igihe iyo nzira yemejwe ko ari On-Chain, Ownership y’umutungo ifatwa ko yimuriwe kuri Alice. Wallet ya Alice, ikurikirana Mining y'isoko, ibona Owned State nshasha iboneka mu Stash yayo.


Ubu urazi gutanga no gutanga RGB Contract. Iyo ubonye iyi nyigisho ari ngirakamaro, noshima cane iyo ushira urukumu rwa Green aha hepfo. Turagusavye ntimwitinye gusangiza abandi iyi nkuru ku mbuga ngurukanabumenyi zanyu. Murakoze cane!


Ndasaba kandi iyi yindi nyigisho aho ndasigura ingene wotanguza urudodo rw’umuravyo ruhuye na RGB ku bimenyetso vya Exchange hafi mu kanya nk’ako gukubita:


https://planb.network/tutorials/node/others/rln-ffc02528-329b-4e16-bd83-873d0299feea