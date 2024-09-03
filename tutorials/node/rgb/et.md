---
name: RGB
description: Sissejuhatus ja varade loomine RGB kohta
---

![RGB vs Ethereum](assets/0.webp)

## sissejuhatus

3. jaanuaril 2009 käivitas Satoshi Nakamoto esimese Bitcoin'i sõlme, alates sellest hetkest liitusid uued sõlmed ja Bitcoin hakkas käituma nagu uus eluvorm, eluvorm, mis pole lakanud arenemast, vähehaaval on see saanud maailma turvalisemaks võrguks tänu oma unikaalsele disainile, mille Satoshi oli väga hästi läbi mõelnud, kuna majanduslike stiimulite kaudu meelitab see kasutajaid, keda tavaliselt nimetatakse kaevuriteks, investeerima energiasse ja arvutusvõimsusse, mis aitab kaasa võrgu turvalisusele.

Kuna Bitcoin jätkab oma kasvu ja omaksvõttu, seisab see silmitsi skaleeritavuse probleemidega. Bitcoin'i võrk lubab uue ploki koos tehingutega kaevandada ligikaudu 10 minuti jooksul, eeldades, et meil on päevas 144 plokki maksimaalsete väärtustega 2700 tehingut ploki kohta, oleks Bitcoin lubanud ainult 4,5 tehingut sekundis. Satoshi oli sellest piirangust teadlik, me võime seda näha e-kirjas1, mis saadeti Mike Hearnile märtsis 2011, kus ta selgitab, kuidas see, mida me täna teame kui maksekanalit, töötab. mikromaksed kiiresti ja turvaliselt ilma kinnituste ootamiseta. Siin tulevad mängu off-chain protokollid.

Christian Decker2 sõnul on off-chain protokollid tavaliselt süsteemid, milles kasutajad kasutavad plokiahela andmeid ja haldavad seda ilma plokiahelat ennast puudutamata kuni viimase minutini. Selle kontseptsiooni põhjal sündis Lightning Network, võrk, mis kasutab off-chain protokolle, et võimaldada Bitcoin'i makseid teha peaaegu koheselt ja kuna mitte kõik need toimingud ei ole kirjutatud plokiahelasse, võimaldab see tuhandeid tehinguid sekundis ja skaleerib Bitcoin'i.

Uurimis- ja arendustegevus Bitcoin'i off-chain protokollide valdkonnas on avanud Pandora laeka, täna teame, et me saame saavutada palju enamat kui väärtuse ülekanne detsentraliseeritud viisil, mittetulundusühing LNP/BP Standards Association keskendub Bitcoin'i ja Lightning Network'i 2. ja 3. kihi protokollide arendamisele, nende projektide seas paistab silma RGB.

## Mis on RGB?

RGB on tekkinud Peter Toddi3 uurimistööst ühekordsete pitserite ja kliendipoolse valideerimise kohta, mille 2016-2019 aastatel mõtestasid Giacomo Zucco ja kogukond paremaks varaprotokolliks Bitcoin'ile ja Lightning võrgule. Nende ideede edasiarendus viis RGB arenguni täisfunktsionaalseks nutilepingute süsteemiks, mida juhib alates 2019. aastast selle rakendamist Maxim Orlovsky koos kogukonna osalusega.

RGB-d võime defineerida kui avatud lähtekoodiga protokollide kogumit, mis võimaldab meil täita keerukaid nutilepinguid skaleeritaval ja konfidentsiaalsel viisil. See ei ole konkreetne võrk (nagu Bitcoin või Lightning); iga nutileping on lihtsalt lepingu osapoolte kogum, mis võivad suhelda erinevate suhtluskanalite kaudu (vaikimisi Lightning võrk). RGB kasutab Bitcoin'i plokiahelat kui oleku kinnitamise kihti ja hoiab nutilepingu koodi ja andmeid off-chain, mis muudab selle skaleeritavaks, kasutades Bitcoin'i tehinguid (ja Script'i) kui nutilepingute omandikontrolli süsteemi; samal ajal kui nutilepingu arengut määrab off-chain skeem, lõpuks on oluline märkida, et kõik valideeritakse kliendi poolel.

Lihtsustatult öeldes on RGB süsteem, mis võimaldab kasutajal auditeerida nutilepingut, seda täita ja igal ajal individuaalselt kontrollida ilma lisakuludeta, kuna selleks ei kasutata plokiahelat nagu "traditsioonilised" süsteemid teevad, keerukaid nutilepingute süsteeme tutvustas esmakordselt Ethereum, kuid kuna see nõuab kasutajalt iga toimingu jaoks märkimisväärseid gaasikoguseid, ei saavutanud nad kunagi lubatud skaleeritavust ja seetõttu ei olnud see kunagi võimalus pankadele, kes on jäänud praegusest finantssüsteemist välja.
Praegu propageerib plokiahela tööstus, et nii nutilepingute kood kui ka andmed peavad olema salvestatud plokiahelasse ja iga võrgu sõlme poolt täidetud, sõltumata liigsest suuruse kasvust või arvutusressursside väärkasutusest. RGB poolt välja pakutud skeem on palju intelligentsem ja efektiivsem, kuna see lõikab läbi plokiahela paradigma, hoides nutilepingud ja andmed plokiahelast eraldi ning vältides seeläbi võrgu ülekoormust, mida on nähtud teistel platvormidel. Samuti ei sunni see iga sõlme iga lepingut täitma, vaid pigem osapooli, mis lisab konfidentsiaalsust seninägematul tasemel.
![RGB vs Ethereum](assets/1.webp)

## Nutilepingud RGB-s

RGB nutilepingu arendaja määratleb skeemi, mis täpsustab reegleid, kuidas leping aja jooksul areneb. Skeem on RGB nutilepingute ehitamise standard ja nii emiteerija, kui ta määratleb emiteerimiseks lepingu, kui ka rahakott või vahetus peavad järgima kindlat skeemi, mille vastu nad peavad lepingut valideerima. Ainult kui valideerimine on korrektne, võib iga osapool taotlusi vastu võtta ja varaga töötada.

Nutileping RGB-s on suunatud atsükliline graaf (DAG) olekumuutustest, kus alati on teada ainult graafi osa ja ülejäänud osale puudub juurdepääs. RGB skeem on põhireeglite kogum, millest nutileping alguse saab. Iga lepingu osapool võib nendele reeglitele lisada (kui skeem seda lubab) ja tulemuseks olev graaf ehitatakse nende reeglite iteratiivsest rakendamisest.

## Vahetatavad varad

RGB-s vahetatavad varad järgivad LNPBP RGB-20 spetsifikatsiooni, kui RGB-20 on määratletud, levitatakse vara andmeid, mida tuntakse kui "genesis andmeid", läbi Lightning võrgu, mis sisaldab kõike, mida on vaja vara kasutamiseks. Kõige lihtsamad varad ei luba sekundaarset emiteerimist, tokenite põletamist, ümbernimetamist või asendamist.

Mõnikord peab emiteerija tulevikus rohkem tokeneid välja andma, nt stabiilrahad nagu USDT, mis hoiab iga tokeni väärtust seotuna inflatsioonilise valuutaga nagu USD. Selle saavutamiseks on olemas keerukamad RGB-20 skeemid ja lisaks genesis andmetele nõuavad need, et emiteerija toodaks saadetisi, mis liiguvad samuti läbi Lightning võrgu; selle teabega saame teada vara kogu ringluses oleva koguse. Sama kehtib varade põletamise või nende nime muutmise kohta.

Varaga seotud teave võib olla avalik või privaatne: kui emiteerija nõuab konfidentsiaalsust, võib ta valida mitte jagada teavet tokeni kohta ja teostada toiminguid absoluutses privaatsuses, kuid meil on ka vastupidine juhtum, kus emiteerija ja omanikud vajavad kogu protsessi läbipaistvust. See saavutatakse tokeni andmete jagamisega.

## RGB-20 protseduurid

Põletamise protseduur keelab tokenid, põletatud tokeneid ei saa enam kasutada.

Asendamise protseduur toimub, kui tokenid põletatakse ja luuakse uus kogus sama tokenit. See aitab vähendada vara ajalooliste andmete suurust, mis on oluline vara kiiruse säilitamiseks.

Toetamaks kasutusjuhtu, kus on võimalik varasid põletada ilma neid asendamata, kasutatakse RGB-20 alamskeemi, mis lubab ainult varade põletamist.

## Mittevahetatavad varad
Mittefungibelsed varad RGB-s järgivad LNPBP RGB-21 spetsifikatsiooni5, kui me töötame NFT-dega, on meil samuti peamine skeem ja alamskeem. Neil skeemidel on graveerimisprotseduur, mis võimaldab meil lisada kohandatud andmeid tokeni omaniku poolt, kõige tavalisem näide, mida me täna NFT-des näeme, on digitaalne kunst, mis on tokeniga seotud. Tokeni väljastaja võib selle andmete graveerimise keelata, kasutades RGB-21 alamskeemi. Erinevalt teistest NFT plokiahela süsteemidest võimaldab RGB suuremahulise meedia tokeni andmete jaotamist täielikult detsentraliseeritud ja tsensuurikindlal viisil, kasutades Lightning P2P võrgu laiendust nimega Bifrost, mida kasutatakse ka paljude teiste RGB-spetsiifiliste nutilepingute funktsionaalsuste loomiseks.
Lisaks fungibelsedele varadele ja NFT-dele saab RGB-d ja Bifrosti kasutada ka teiste nutilepingute vormide, sealhulgas DEXide, likviidsusfondide, algoritmiliste stabiilsete müntide jne tootmiseks, mida me käsitleme tulevastes artiklites.

## NFT RGB-st vs NFT teistelt platvormidelt

- Pole vaja kulukat plokiahela salvestusruumi
- Pole vaja IPFS-i, selle asemel kasutatakse Lightning võrgu laiendust (nimega Bifrost) (ja see on täielikult otsast lõpuni krüpteeritud)
- Pole vaja erilahendust andmehalduseks – jällegi, Bifrost võtab selle rolli
- Pole vaja usaldada veebisaite, et hoida andmeid NFT tokenite või välja antud varade / lepingute ABI-de kohta
- Sisseehitatud DRM krüpteering ja omandi haldamine
- Infrastruktuur varundamiseks kasutades Lightning võrku (Bifrost)
- Viisid sisu monetiseerimiseks (mitte ainult NFT ise müümine, vaid juurdepääs sisule, mitu korda)

## Järeldused

Alates Bitcoini käivitamisest peaaegu 13 aastat tagasi on selles valdkonnas toimunud palju uurimistööd ja katsetusi, nii edulood kui ka vead on võimaldanud meil veidi rohkem mõista, kuidas detsentraliseeritud süsteemid praktikas käituvad, mis teeb neist tõeliselt detsentraliseeritud ja millised tegevused kipuvad neid tsentraliseerima, kõik see on viinud meid järeldusele, et tõeline detsentraliseeritus on haruldane ja raskesti saavutatav nähtus, tõeline detsentraliseeritus on saavutatud ainult Bitcoiniga ja just seetõttu keskendume oma jõupingutustele sellele ehitamisele.

RGB-l on oma jäneseurg Bitcoini jäneseurgu sees, samal ajal kui ma nende kaudu alla kukun, postitan sellest õpitu, järgmises artiklis tutvustame LNP-d ja RGB sõlmi ning kuidas neid kasutada.

- 1 https://plan99.net/~mike/satoshi-emails/thread4.html
- 2 https://btctranscripts.com/chaincode-labs/chaincode-residency/2018-10-22-christian-decker-history-of-lightning/
- 3 https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2016-June/012773.html
- 4 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0020.md
- 5 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0021.md

# RGB-sõlme Õpetus

## Sissejuhatus

Selless õpetuses selgitame, kuidas kasutada RGB-sõlme fungibelse tokeni loomiseks ja selle ülekandmiseks, see dokument põhineb RGB-sõlme demol ja erineb selle poolest, et see õpetus kasutab reaalseid testneti andmeid ja selleks peame ehitama oma osaliselt allkirjastatud Bitcoin tehingu, edaspidi psbt.

## Nõuded

Soovitatav on kasutada Linuxi distributsiooni, see õpetus on kirjutatud kasutades Pop!OS-i, mis põhineb Ubuntul ja teil on vaja:

- cargo
- Bitcoin core
- git
Märkus: See õpetus näitab käskude täitmist Linuxi terminalis. Erinevuse tegemiseks selle vahel, mida kasutaja kirjutab, ja vastuse vahel, mida ta terminalis saab, kasutame $ sümbolit, mis tähistab bashi käsukihti.
Teil on vaja installida mõned sõltuvused:

```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```

Ehitamine & Käivitamine

RGB-node on töös olev projekt (WIP), seetõttu peame asetsema kindlas koodi muudatuses (3f3c520c19d84c66d430e76f0fc68c5a66d79c84), et seda korrektselt kompileerida ja kasutada, selleks täidame järgmised käsklused.

```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```

Nüüd kompileerime selle, ärge unustage kasutada --locked lippu, kuna clap'i versioonis on tehtud oluline muudatus.

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

Nagu Rusti kompilaator meile teatab, kopeeriti binaarid kausta $HOME/.cargo/bin, kui teie kompilaator kopeeris need teise kohta, peate veenduma, et see kaust oleks kaasatud $PATH-i.

Paigaldatud binaaride seas näeme kolme deemonit või teenust (failid, mis lõppevad d-ga) ja ühte CLI-d (käsurea liidest), CLI võimaldab meil suhelda peamise rgbd deemoniga. Kuna selles õpetuses käivitame kaks sõlme, vajame ka kahte klienti, igaüks peab ühenduma omaenda sõlmega, selleks loome kaks aliast.

```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```

Me võime lihtsalt käivitada aliased või lisada need $HOME/.bashrc faili lõppu ja käivitada source $HOME/.bashrc.
Eeldus

RGB-node ei tegele ühegi rahakotiga seotud funktsionaalsusega, see täidab ainult RGB-spetsiifilisi ülesandeid andmetel, mida pakub väline rahakott nagu bitcoin core. Eelkõige, et demonstreerida põhilist töövoogu emiteerimise ja ülekandega, vajame:

- Emiteerimise_utxo, millele rgb-node-0 seob uue välja antud vara
- Vastuvõtu_utxo, kuhu rgb-node-1 saab vara
- Muudatuse_utxo, kuhu rgb-node-0 saab vara muudatuse
- Osaliselt allkirjastatud bitcoin tehingu (tx.psbt), mille väljundi avalik võti kohandatakse, et lisada pühendumus ülekandele.

Me kasutame bitcoin core CLI-d, meil on vaja, et bitcoind deemon töötaks testnetis, see annab meile koostalitlusvõime ja lõpuks saame saata oma varasid teisele RGB kasutajale, kes järgis seda õpetust.
Lihtsuse huvides lisame selle aliase oma `~/.bashrc` faili lõppu.
```
alias bcli="bitcoin-cli -testnet"
```

Vaadelgem meie kulutamata väljundtehinguid ja valime kaks, üks saab olema issuance_utxo ja teine change_utxo, pole oluline, kumb on kumb, tähtis on, et väljaandjal on kontroll nende kahe UTXO üle.

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

Enne kui edasi läheme, peame rääkima väljundpunktidest, üks tehing võib sisaldada mitut väljundit, väljundpunkt hõlmab nii 32-baidist TXID-d kui ka 4-baidist väljundiindeksi numbrit (vout), et viidata konkreetsele väljundile, eraldatuna kooloniga :. Meie listunspent väljundis võime leida kaks UTXO-d, mõlemal näeme txid-d ja vout-i, need on meie issuance_utxo ja change_utxo väljundpunktid.

receive_utxo on UTXO, mida kontrollib vastuvõtja, sel juhul kasutame e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0, mis on väljundpunkt teisest rahakotist.
- issuance_utxo: 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
- change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- receive_utxo: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Nüüd hakkame looma osaliselt allkirjastatud tehingut (tx.psbt), mille väljundit kohandatakse, et see sisaldaks kohustust ülekande tegemiseks. Pea meeles asendada txid ja vout oma omadega, sihtkoha aadress ei ole oluline, see võib olla sinu oma või kellegi teise oma, pole tähtis, kuhu need satsid lähevad, tähtis on, et kasutame issuance_utxo.

```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
  "psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
  "fee": 0.00000280,
  "changepos": 0
}
```

Väljund andis meile psbt base64 kodeeringus, mida kasutame tx.psbt loomiseks.
```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt
```

Loome uue kataloogi nimega rgbdata, kus hoitakse iga sõlme andmekataloogi.

```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```

Olles juba asukohas $HOME/rgbdata, käivitame iga sõlme erinevates terminalides, kus ~/.cargo/bin on kataloog, kuhu cargo kopeeris kõik binaarid pärast rgb-node paigaldamist.

```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```

## Väljaandmine

Vara väljaandmiseks käivitame rgb0-cli koos fungible issue alamkäsklustega, seejärel argumendid, tiker USDT, nimi "USD Tether" ja jaotuses kasutame väljaandmise summat ja issuance_utxo nagu allpool näha:

```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```

Vara edukalt välja antud. Kasutage seda teavet jagamiseks:
Vara informatsioon:

```
genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
teadaolevRinglus: 1000
onVäljaAntudTeada: ~
väljaandmiseLimiiit: 0
kett: testnet
kümnendtäpsus: 0
kuupäev: "2022-02-23T20:53:26"
teadaolevadProbleemid:
  - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    summa: 1000
    päritolu: ~
teadaolevInflatsioon: {}
teadaolevadJaotused:
  - sõlmeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
    indeks: 0
    väljundpunkt: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
    avalikustatudSumma:
      väärtus: 1000
      varjamine: "0000000000000000000000000000000000000000000000000000000000000001"
Me saame vara ID, mida on vaja vara ülekandmiseks.

```
$ rgb0-cli fungible list

- name: USD Tether
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
```

## Genereeri pime UTXO

Selleks, et vastu võtta uut USDT-d, peab rgb-node-1 genereerima pimeda UTXO, mis vastab receive_utxo-le, et hoida vara.

```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Blinded outpoint: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Outpoint blinding secret: 1679197189805229975
```

Selleks, et olla võimeline aktsepteerima ülekandeid, mis on seotud selle UTXO-ga, vajame me algset receive_utxo ja blinding_factor.

## Ülekanne

Selleks, et üle kanda teatud summa varast rgb-node-1-le, peame me saatma selle pimedale UTXO-le, rgb-node-0 peab looma saatekirja ja avalikustuse ning kinnitama selle bitcoini tehingusse. Seejärel on meil vaja psbt-d, mida me muudame, et lisada kinnitus. Lisaks võimaldavad -i ja -a valikud meil pakkuda sisend väljundpunkti, mis oleks vara päritolu ja eraldise, kus me saame muutuse, me peame seda näitama järgmisel viisil @<change_utxo>.
$ rgb0-cli fungible transfer utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt saadetis.rgb avalikustamine.rgb tunnistaja.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
Ülekanne õnnestus, saadetised ja avalikustamine on kirjutatud faili "saadetis.rgb" ja "avalikustamine.rgb", osaliselt allkirjastatud tunnistaja tehing faili "tunnistaja.psbt"
Kahjuks on esitatud tekst liiga pikk ja keeruline, et seda ühe korraga tõlkida. Palun esitage lühem tekst või konkreetne lõik, mida soovite tõlkida.
See kirjutab kolm uut faili: saateleht, avalikustamine ja psbt koos täiendusega, seda psbt-d nimetatakse tunnistaja tehinguks, saateleht saadetakse rgb-node-1-le.

## Tunnistaja

Tunnistaja tehing tuleks allkirjastada ja edastada, selleks peame selle tagasi base64 kodeerima.

```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```

Allkirjasta see walletprocesspsbt alamkäsklusega.
```yaml
$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="
```
Kuna teie palve sisaldab spetsiifilist tehnilist sisu, mis on seotud krüptovaluutaga (täpsemalt Bitcoin'i PSBT ehk Partially Signed Bitcoin Transaction formaadiga), siis tõlge säilitab tehnilise sisu ja terminoloogia algkujul, kuna see on oluline tehnilise terviklikkuse ja täpsuse säilitamiseks. Siin on tõlgitud tekst:

```json
{
  "psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",  
  "complete": true
}
```

Nüüd viige protsess lõpule ja saage hex.

See tõlge säilitab tehnilise sisu ja struktuuri, tagades, et tehnilised detailid ja terminoloogia jäävad muutmata, mis on oluline tehnilise dokumendi tõlkimisel.
```bash
$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="{
  "hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
  "complete": true
}
```

## Saatmine

Saatke see kasutades `sendrawtransaction` alamkäsku, et see kinnitataks plokiahelasse.

```bash
## Nõustu

Vastuvõtmiseks peaks rgb-node-1 olema saanud konsignatsioonifaili rgb-node-0-lt, omama receive_utxo ja vastavat blinding_factor, mis genereeriti UTXO varjamise ajal.

```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975

Vara ülekanne edukalt aktsepteeritud.
```

Nüüd saame näha (knownAllocations väljal) uut jaotust 100 varaühikut <receive_utxo> käivitades:

```
$ rgb1-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
```
```yaml
name: USD Tether
description: ~
  teadaolevRinglus: 1000
  onVäljastatudTeada: ~
  väljastusLimiiit: 0
  ahel: testnet
  kümnendTäpsus: 0
  kuupäev: "2022-02-23T20:53:26"
  teadaolevadProbleemid:
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      summa: 1000
      päritolu: ~
  teadaolevInflatsioon: {}
  teadaolevadJaotused:
    - sõlmeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      indeks: 0
      väljundpunkt: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      avalikustatudSumma:
        väärtus: 1000
        pimestamine: "0000000000000000000000000000000000000000000000000000000000000001"
    - sõlmeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
      indeks: 1
      väljundpunkt: "e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0"
      avalikustatudSumma:
        väärtus: 100
        pimestamine: 224561f10229eb9ebbdf05f497132d2b8344d70971c80510eddc607d615ee2a0
```

Kuna receive_utxo oli pimestatud, kui ülekanne tehti, ei oma maksja rgb-node-0 teavet selle kohta, kuhu 100 USDT saadeti, seega ei kuvata asukohta teadaolevates jaotustes.

```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
```
```yaml
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6  ticker: USDT
  name: USD Tether
  description: ~
  teadaolevRinglus: 1000
  onVäljaAntudTeada: ~
  väljaAndmiseLimiiit: 0
  ahel: testnet
  kümnendTäpsus: 0
  kuupäev: "2022-02-23T20:53:26"
  teadaolevadProbleemid:
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      summa: 1000
      päritolu: ~
  teadaolevInflatsioon: {}
  teadaolevadJaotused:
    - sõlmeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      indeks: 0
      väljundpunkt: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      avalikustatudSumma:
        väärtus: 1000
        pimestamine: "0000000000000000000000000000000000000000000000000000000000000001"
```

Aga nagu näete, ei suuda rgb-node-0 näha 900 vara muutust, mida me edastuskäsklusele -a argumendiga lisasime. Muutuse registreerimiseks peab rgb-node-0 aktsepteerima avalikustamise.

```
$ rgb0-cli fungible enclose disclosure.rgb

Avalikustamise andmed edukalt lisatud.
```

Kui rgb-node-0 oli edukas, saate vara muutust näha, kui loetlete vara.

```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
  id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
  ticker: USDT
  name: USD Tether
```
description: ~  teadaolevRinglus: 1000
  isIssuedKnown: ~
  väljaandmiseLimiiit: 0
  ahel: testnet
  kümnendtäpsus: 0
  kuupäev: "2022-02-23T20:53:26"
  teadaolevadProbleemid:
    - id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      kogus: 1000
      päritolu: ~
  teadaolevInflatsioon: {}
  teadaolevadJaotused:
    - sõlmeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
      indeks: 0
      väljundpunkt: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
      avalikustatudKogus:
        väärtus: 1000
        varjamine: "0000000000000000000000000000000000000000000000000000000000000001"
    - sõlmeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
      indeks: 0
      väljundpunkt: "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1"
      avalikustatudKogus:
        väärtus: 900
        varjamine: ddba9e0efdd614614420fa0b68ecd2d3376a05dd3d809b2ad1f5fe0f6ed75ea2

## Järeldused

Oleme suutnud luua vahetatava vara ja liigutada seda ühest tehingust teise privaatsel viisil, kui me kontrollime kinnitatud tehingut plokiahelas, ei leia me midagi erinevat tavalisest tehingust, see on tänu asjaolule, et RGB kasutab ühekordseid pitseid tehingute kohandamiseks. Selles postituses teen sissejuhatuse selle kohta, kuidas RGB töötab.

See postitus võib sisaldada vigu, kui leiate midagi, palun andke mulle teada, et saaksin seda juhendit parandada, ettepanekud ja kriitika on samuti teretulnud, rõõmsat häkkimist! 🖖