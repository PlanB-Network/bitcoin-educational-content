---
name: RGB CLI
description: Je, ninawezaje kuunda na mikataba mahiri ya Exchange kwenye RGB?
---
![cover](assets/cover.webp)


Katika somo hili, tutafuata mchakato wa hatua kwa hatua wa kuandika Contract, kwa kutumia zana ya mstari wa amri `RGB` iliyoundwa na muungano wa LNP/BP. Lengo ni kuonyesha jinsi ya kusakinisha na kuendesha CLI, kukusanya Schema, kuagiza Interface na Interface Implementation, na kisha kutoa mali ya RGB. Pia tutaangalia mantiki ya msingi, ikiwa ni pamoja na mkusanyiko na uthibitishaji wa hali. Mwishoni mwa mafunzo haya, unapaswa kuwa na uwezo wa kuzaliana mchakato na kuunda kandarasi zako za RGB.


## Kikumbusho cha itifaki ya RGB


RGB ni itifaki inayoendesha juu ya Bitcoin na kuiga utendaji wa Smart contract na usimamizi wa mali dijitali, bila kupakia Blockchain ambayo msingi wake ni. Tofauti na mikataba mahiri ya On-Chain ya kawaida (kama ilivyo kwa Ethereum, kwa mfano), RGB inategemea mfumo wa "*Client-side Validation*": data na historia nyingi za hali hubadilishwa na kuhifadhiwa na washiriki wanaohusika pekee, ilhali Bitcoin Blockchain huandaa tu ahadi ndogo za kriptografia (kupitia mbinu kama vile *OTapret*). Katika itifaki ya RGB, Bitcoin Blockchain kwa hivyo hutumika tu kama seva ya kukanyaga wakati na mfumo wa ulinzi wa Double-spending.


RGB Contract imeundwa kama mashine ya hali ya mabadiliko. Huanza na Genesis inayofafanua hali ya awali (inayoelezea, kwa mfano, Supply, ticker au metadata nyingine) kulingana na Schema iliyochapwa kwa ukali na iliyokusanywa. Mpito wa Jimbo na, ikihitajika, Viendelezi vya Jimbo basi hutumika kurekebisha au kupanua hali hii. Kila operesheni, iwe ni kuhamisha vipengee vinavyoweza kuvutwa (RGB20) au kuunda vipengee vya kipekee (RGB21), huhusisha *Mihuri ya Matumizi Moja*. Hizi huunganisha Bitcoin UTXOs kwenye majimbo ya off-chain na kuzuia matumizi maradufu, huku zikihakikisha usiri na hatari.


Ili kujifunza zaidi kuhusu jinsi itifaki ya RGB inavyofanya kazi, ninapendekeza uchukue kozi hii ya kina ya mafunzo:


https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

Mantiki ya ndani ya RGB inategemea maktaba za Rust ambazo wewe, kama wasanidi, unaweza kuingiza katika miradi yako ili kudhibiti sehemu ya *Client-side Validation*. Zaidi ya hayo, timu ya LNP/BP inashughulikia masuala ya kuunganisha lugha nyingine, lakini hili bado halijakamilika. Kwa kuongezea, huluki zingine kama Bitfinex zinatengeneza safu zao za ujumuishaji, lakini tutazungumza juu ya haya katika mafunzo mengine. Kwa sasa, `RGB` CLI ndiyo marejeleo rasmi, hata kama imesalia kuwa haijapolishwa.


## Ufungaji na uwasilishaji wa chombo cha RGB CLI


Amri kuu inaitwa tu `RGB`. Imeundwa ili kukumbusha `git`, ikiwa na seti ya amri ndogo za kuchezea kandarasi, kuzivutia, kutoa mali na kadhalika. Bitcoin Wallet haijaunganishwa kwa sasa, lakini itakuwa katika toleo la karibu (0.11). Toleo hili linalofuata litawawezesha watumiaji kuunda na kudhibiti pochi zao (kupitia vifafanuzi) moja kwa moja kutoka kwa `RGB`, ikijumuisha kizazi cha PSBT, uoanifu na maunzi ya nje (k.m. Hardware Wallet) ya kutia sahihi, na ushirikiano na programu kama vile Sparrow. Hii itarahisisha utoaji na uhamishaji wa kipengee kizima.


### Ufungaji kupitia Cargo


Tunasanikisha zana katika Rust na:


```bash
cargo install rgb-contracts --all-features
```


(Kumbuka: kreti inaitwa `RGB-contracts`, na amri iliyosakinishwa itaitwa `RGB`. Ikiwa kreti inayoitwa `RGB` tayari ilikuwepo, kunaweza kuwa na mgongano, kwa hivyo jina)


Usakinishaji unajumuisha idadi kubwa ya vitegemezi (k.m. uchanganuzi wa amri, ujumuishaji wa Electrum, udhibiti wa uthibitisho usio na maarifa, n.k.).


Mara baada ya ufungaji kukamilika,:


```bash
rgb
```


Uendeshaji `RGB` (bila hoja) huonyesha orodha ya amri ndogo zinazopatikana, kama vile `violesura`, `Schema`, `import`, `hamisha`, `tole`, `Invoice`, `transfer`, n.k. Unaweza kubadilisha saraka ya hifadhi ya ndani (Stash ambayo inashikilia kumbukumbu zote, 4G-W) Mainnet) au usanidi seva yako ya Electrum.


![RGB-CLI](assets/fr/01.webp)


### Muhtasari wa kwanza wa vidhibiti


Unapoendesha amri ifuatayo, utaona kwamba `RGB20` Interface tayari imeunganishwa na chaguo-msingi:


```bash
rgb interfaces
```


Ikiwa Interface hii haijaunganishwa, linganisha :


```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```


Tunga:


```bash
cargo run
```


Kisha ingiza Interface ya chaguo lako:


```bash
rgb import interfaces/RGB20.rgb
```


![RGB-CLI](assets/fr/02.webp)


Hata hivyo, tunaambiwa kwamba hakuna Schema ambayo bado imeingizwa kwenye programu. Wala hakuna Contract katika Stash. Ili kuiona, endesha amri:


```bash
rgb schemata
```


Kisha unaweza kuiga hazina ili kupata schematics fulani:


```bash
git clone https://github.com/RGB-WG/rgb-schemata
```


![RGB-CLI](assets/fr/03.webp)


Hazina hii ina, katika saraka yake ya `src/`, faili kadhaa za Rust (kwa mfano `nia.rs`) ambazo hufafanua miundo (NIA ya "*Asset isiyoweza Kuingiliwa*", UDA ya "*Unique Digital Asset*", n.k.). Ili kukusanya, basi unaweza kukimbia:


```bash
cd rgb-schemata
cargo run
```


Hii huzalisha faili kadhaa za `.RGB` na `.rgba` zinazolingana na taratibu zilizokusanywa. Kwa mfano, utapata `NonInflatableAsset.RGB`.


### Inaagiza Schema na Interface Implementation


Sasa unaweza kuleta mpangilio katika `RGB` :


```bash
rgb import schemata/NonInflatableAssets.rgb
```


![RGB-CLI](assets/fr/04.webp)


Hii inaiongeza kwa Stash ya ndani. Ikiwa tunaendesha amri ifuatayo, tunaona kwamba Schema sasa inaonekana:


```bash
rgb schemata
```


## Uundaji wa Contract (inatoa)


Kuna njia mbili za kuunda mali mpya:




- Tunaweza kutumia hati au msimbo katika Rust ambayo huunda Contract kwa kujaza sehemu za Schema (Global State, Nchi Zinazomilikiwa, n.k.) na kutoa faili ya `.RGB` au `.rgba`;
- Au tumia amri ndogo ya `suala` moja kwa moja, ukiwa na faili ya YAML (au TOML) inayoelezea sifa za tokeni.


Unaweza kupata mifano katika Rust kwenye folda ya `mifano`, ambayo inaonyesha jinsi unavyounda `ContractBuilder`, jaza `Global State` (jina la kipengee, tiki, Supply, tarehe, n.k.), fafanua Owned State (ambayo UTXO imekabidhiwa), kisha ujumuishe yote haya kwenye 67 inaweza kuleta *GW - halali, na GW6 inaweza kusafirisha na kusafirisha, na GW6 kuhalalisha. Stash.


Njia nyingine ni kuhariri mwenyewe faili ya YAML ili kubinafsisha `tika`, `jina`, `Supply`, na kadhalika. Tuseme faili inaitwa `RGB20-demo.yaml`. Unaweza kubainisha:




- `spec`: ticker, jina, usahihi;
- `masharti`: uwanja wa notisi za kisheria;
- `issuedSupply`: kiasi cha tokeni iliyotolewa;
- `Kazi`: inaonyesha Single-Use Seal (*Seal Definition*) na idadi iliyofunguliwa.


Hapa kuna mfano wa faili ya YAML kuunda:


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


Kisha endesha tu amri:


```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```


![RGB-CLI](assets/fr/06.webp)


Kwa upande wangu, kitambulishi cha kipekee cha Schema (kitakachoambatanishwa katika nukuu moja) ni `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` na sijaweka mtoaji yeyote. Kwa hivyo agizo langu ni:


```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```


Ikiwa hujui kitambulisho cha Schema, endesha amri:


```bash
rgb schemata
```


CLI inajibu kuwa Contract mpya imetolewa na kuongezwa kwa Stash. Ikiwa tutaandika amri ifuatayo, tunaona kwamba sasa kuna Contract ya ziada, inayolingana na ile iliyotolewa hivi karibuni:


```bash
rgb contracts
```


![RGB-CLI](assets/fr/07.webp)


Kisha, amri inayofuata inaonyesha mataifa ya kimataifa (jina, tiki, Supply...) na orodha ya Nchi Zinazomilikiwa, yaani mgao (kwa mfano, tokeni za `PBN` milioni 1 zilizofafanuliwa katika UTXO. `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).


```bash
rgb state '<ContractId>'
```


![RGB-CLI](assets/fr/08.webp)


## Hamisha, ingiza na uthibitishaji


Ili kushiriki Contract hii na watumiaji wengine, inaweza kusafirishwa kutoka Stash hadi :


```bash
rgb export '<ContractId>' myContractPBN.rgb
```


![RGB-CLI](assets/fr/09.webp)


Faili ya `myContractPBN.RGB` inaweza kupitishwa kwa mtumiaji mwingine, ambaye anaweza kuiongeza kwenye Stash yake kwa amri :


```bash
rgb import myContractPBN.rgb
```


Inapoagiza, ikiwa ni *Contract Consignment* rahisi, tutapata ujumbe wa "`Inaagiza Consignment RGB`". Ikiwa ni *State Transition Consignment* kubwa zaidi, amri itakuwa tofauti (`RGB kubali`).


Ili kuhakikisha uhalali, unaweza pia kutumia kitendakazi cha uthibitishaji wa ndani. Kwa mfano, unaweza kukimbia:


```bash
rgb validate myContract.rgb
```


### Matumizi, uthibitishaji na maonyesho ya Stash


Kama ukumbusho, Stash ni orodha ya ndani ya michoro, miingiliano, utekelezaji na mikataba (Genesis + mabadiliko). Kila wakati unapoendesha "kuagiza", unaongeza kipengee kwenye Stash. Stash hii inaweza kutazamwa kwa undani na amri:


```bash
rgb dump
```


![RGB-CLI](assets/fr/10.webp)


Hii itakuwa generate folda yenye maelezo ya Stash nzima.


## Uhamisho na PSBT


Ili kutekeleza uhamisho, utahitaji kudanganya Bitcoin Wallet ya ndani ili kudhibiti ahadi za `Tapret` au `Opret`.


### generate na Invoice


Mara nyingi, mwingiliano kati ya washiriki katika Contract (k.m. Alice na Bob) hufanyika kupitia kizazi cha Invoice. Ikiwa Alice anataka Bob atekeleze jambo fulani (uhamisho wa ishara, utoaji upya, kitendo katika DAO, n.k.), Alice huunda Invoice inayoelezea maagizo yake kwa Bob. Kwa hivyo tunayo:




- Alice** (mtoaji wa Invoice);
- Bob** (ambaye anapokea na kutekeleza Invoice).


Tofauti na mifumo ikolojia mingine, RGB Invoice haizuiliwi na wazo la malipo. Inaweza kupachika ombi lolote lililounganishwa na Contract: kubatilisha ufunguo, kupiga kura, kuunda maandishi (*engraving*) kwenye NFT, nk. Operesheni inayolingana inaweza kuelezewa katika Contract Interface. Operesheni inayolingana inaweza kuelezewa katika Contract Interface.


Amri ifuatayo inazalisha RGB Invoice:


```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```


Na:




- `$Contract`: Kitambulishi cha Contract (*ContractId*) ;
- `$Interface`: Interface itatumika (k.m. `RGB20`);
- `$ACTION`: jina la operesheni iliyobainishwa katika Interface (kwa uhamishaji rahisi wa tokeni, hii inaweza kuwa "Hamisha"). Ikiwa Interface tayari inatoa kitendo chaguo-msingi, huhitaji kukiingiza tena hapa;
- `$STATE`: data ya hali ya kuhamishwa (kwa mfano, kiasi cha tokeni ikiwa tokeni inayoweza kuvu itahamishwa);
- `$Seal`: mnufaika (Alice's) Single-Use Seal, yaani marejeleo dhahiri ya UTXO. Bob atatumia maelezo haya kuunda Witness Transaction, na matokeo yanayolingana yatakuwa ya Alice (katika *blinded UTXO* au fomu ambayo haijasimbwa).


Kwa mfano, na amri zifuatazo


```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```


CLI itakuwa generate na Invoice kama:


```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```


Inaweza kupitishwa kwa Bob kupitia chaneli yoyote (maandishi, msimbo wa QR, nk).


### Kufanya uhamisho


Kuhamisha kutoka Invoice :




- Bob (ambaye ana ishara katika Stash yake) ana Bitcoin Wallet. Anahitaji kuandaa shughuli ya Bitcoin (katika mfumo wa PSBT, k.m. `tx.PSBT`) ambayo hutumia UTXO ambapo tokeni zinazohitajika za RGB ziko, pamoja na UTXO moja kwa sarafu (Exchange) ;
- Bob anatoa amri ifuatayo:


```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```




- Hii inazalisha `Consignment.RGB` faili ambayo ina :
 - Historia ya mpito inayothibitisha kwa Alice kwamba ishara ni za kweli;
 - Mpito mpya unaohamisha ishara kwa Single-Use Seal ya Alice;
 - Witness Transaction (isiyo na saini).
- Bob hutuma faili hii ya `Consignment.RGB` kwa Alice (kwa barua pepe, seva inayoshiriki au itifaki ya RGB-RPC, Storm, n.k.);
- Alice anapokea `Consignment.RGB` na anaikubali katika Stash yake yenyewe:


```bash
alice$ rgb accept consignment.rgb
```




- CLI hukagua uhalali wa mpito na kuiongeza kwenye Stash ya Alice. Ikiwa si sahihi, amri itashindwa na ujumbe wa makosa ya kina. Vinginevyo, inafanikiwa, na inaripoti kwamba shughuli ya sampuli bado haijatangazwa kwenye mtandao wa Bitcoin (Bob anasubiri mwanga wa Green wa Alice);
- Kwa njia ya uthibitisho, amri ya `kukubali` inarejesha saini (*karatasi ya malipo*) ambayo Alice anaweza kutuma kwa Bob ili kumuonyesha kwamba ameidhinisha *Consignment* ;
- Kisha Bob anaweza kusaini na kuchapisha (`--publish`) muamala wake wa Bitcoin:


```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```




- Mara tu shughuli hii inapothibitishwa On-Chain, Ownership ya mali inachukuliwa kuhamishiwa kwa Alice. Wallet ya Alice, ikifuatilia shughuli ya Mining, inaona Owned State mpya ikionekana kwenye Stash yake.


Sasa unajua jinsi ya kutoa na kuhamisha RGB Contract. Ikiwa umepata mafunzo haya kuwa ya manufaa, ningeshukuru sana ikiwa utaweka kidole gumba cha Green hapa chini. Tafadhali jisikie huru kushiriki nakala hii kwenye mitandao yako ya kijamii. Asante sana!


Pia ninapendekeza somo hili lingine ambalo ninaelezea jinsi ya kuzindua nodi ya Umeme inayoendana na RGB kwa tokeni za Exchange karibu mara moja:


https://planb.network/tutorials/node/others/rln-ffc02528-329b-4e16-bd83-873d0299feea