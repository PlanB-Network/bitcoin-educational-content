---
name: RGB
description: Utangulizi na uundaji wa mali kwenye RGB
---

![RGB vs Ethereum](assets/0.webp)


## utangulizi


Mnamo Januari 3, 2009, Satoshi Nakamoto ilizindua nodi ya kwanza ya Bitcoin, kutoka wakati huo nodi mpya zilijiunga na Bitcoin kuanza kuishi kana kwamba ni aina mpya ya maisha, aina ya maisha ambayo haijaacha kubadilika, kidogo kidogo imekuwa mtandao salama zaidi ulimwenguni kama matokeo ya muundo wake wa kipekee, uliofikiriwa vizuri sana tangu na kampuni ya Satoshi inayoitwa kiuchumi katika wawekezaji. nishati na nguvu ya kompyuta ambayo inachangia usalama wa mtandao.


Bitcoin inapoendelea kukua na kupitishwa inakabiliwa na maswala ya kuongezeka, mtandao wa Bitcoin unaruhusu kizuizi kipya na miamala kuchimbwa kwa muda wa takriban dakika 10, ikizingatiwa kuwa tuna vitalu 144 kwa siku na viwango vya juu vya miamala 2700 kwa kila block, Bitcoin ingeruhusu kikomo cha 6.5 tu kwa sekunde 6. katika barua pepe1 iliyotumwa kwa Mike Hearn mnamo Machi 2011 ambapo anaeleza jinsi kile tunachojua leo kama njia ya malipo hufanya kazi. micropayments haraka na kwa usalama bila kusubiri uthibitisho. Hapa ndipo itifaki za off-chain zinapoingia.


Kulingana na itifaki za Christian Decker2 off-chain kwa kawaida ni mifumo ambayo watumiaji hutumia data kutoka kwa Blockchain na kuisimamia bila kugusa Blockchain yenyewe hadi dakika ya mwisho. Kulingana na dhana hii, Lightning Network ilizaliwa, mtandao unaotumia itifaki za off-chain kuruhusu malipo ya Bitcoin kufanywa karibu mara moja na kwa kuwa sio shughuli zote hizi zimeandikwa kwenye mlolongo wa kuzuia, inaruhusu maelfu ya shughuli kwa pili na kiwango cha Bitcoin.


Utafiti na maendeleo katika eneo la itifaki za off-chain kwenye Bitcoin imefungua kisanduku cha pandora, leo tunajua kuwa tunaweza kufikia zaidi ya uhamishaji wa thamani kwa njia iliyogawanywa, Jumuiya ya Viwango ya LNP/BP isiyo ya faida inazingatia uundaji wa itifaki za Layer 2 na 3 kwenye Bitcoin na Lightning Network-1, kati ya miradi hii ya GW-1, kati ya miradi hii.


## RGB ni nini?


RGB imeonekana kutoka kwa utafiti wa Peter Todd3 juu ya matumizi-mihuri moja na uthibitishaji wa upande wa mteja, ambao uliundwa mnamo 2016-2019 na Giacomo Zucco na jamii kuwa itifaki bora ya mali ya Bitcoin na Lightning Network. Mageuzi zaidi ya mawazo haya yalisababisha ukuzaji wa RGB kuwa mfumo kamili wa Smart contract na Maxim Orlovsky, ambaye anaongoza utekelezaji wake tangu 2019 kwa ushiriki wa jamii.


Tunaweza kufafanua RGB kama seti ya itifaki za chanzo huria zinazoturuhusu kutekeleza kandarasi changamano mahiri kwa njia kubwa na ya siri. Sio mtandao fulani (kama Bitcoin au Umeme); kila Smart contract ni seti tu ya washiriki wa Contract ambao wanaweza kuingiliana kwa kutumia njia tofauti za mawasiliano (chaguo-msingi hadi Lightning Network). RGB hutumia Bitcoin Blockchain kama Layer ya jimbo la Commitment na hudumisha msimbo wa Smart contract na data ya off-chain, ambayo huifanya iwe hatarini, inayotumia miamala ya Bitcoin (na Hati) kama mfumo wa udhibiti wa Ownership kwa mikataba mahiri; wakati mageuzi ya Smart contract inafafanuliwa na mpango wa off-chain, hatimaye ni muhimu kutambua kwamba kila kitu kinathibitishwa kwa upande wa mteja.


Kwa maneno rahisi, RGB ni mfumo unaomruhusu mtumiaji kukagua Smart contract, kuitekeleza na kuithibitisha kibinafsi wakati wowote bila kuwa na gharama ya ziada kwani kwa hili haitumii Blockchain kama mifumo ya "jadi", mifumo tata ya mikataba ya smart ilianzishwa na Ethereum lakini kwa sababu hiyo inahitaji mtumiaji kutumia kiasi kikubwa cha gesi ambayo hawakuwahi kuahidi kwa kila kazi ambayo hawakuwahi kupata. chaguo la kuweka benki watumiaji waliotengwa na mfumo wa sasa wa kifedha.


Hivi sasa, sekta ya Blockchain inakuza kwamba kanuni zote mbili za mikataba mahiri na data lazima zihifadhiwe katika Blockchain na kutekelezwa na kila nodi ya mtandao, bila kujali ongezeko kubwa la ukubwa au matumizi mabaya ya rasilimali za hesabu. Mpango uliopendekezwa na RGB ni wa akili na ufanisi zaidi kwani unapunguza kwa dhana ya Blockchain kwa kuwa na mikataba mahiri na data iliyotenganishwa na Blockchain na hivyo kuzuia kueneza kwa mtandao unaoonekana kwenye majukwaa mengine, kwa upande wake hailazimishi kila nodi kutekeleza kila Contract lakini badala yake wahusika wanaohusika ambao huongeza usiri ambao haujawahi kuonekana hapo awali.


![RGB vs Ethereum](assets/1.webp)


## Mikataba mahiri katika RGB


Katika RGB Smart contract msanidi anafafanua mpango unaobainisha sheria jinsi Contract inavyobadilika baada ya muda. Mpango huo ndio kiwango cha ujenzi wa kandarasi mahiri katika RGB, na mtoaji anapofafanua Contract kwa ajili ya utoaji na Wallet au Exchange lazima wafuate mpango mahususi ambao ni lazima waidhinishe Contract. Ni ikiwa tu uthibitishaji ni sahihi ndipo kila mhusika anaweza kukubali maombi na kufanya kazi na kipengee.


Smart contract katika RGB ni Directed Acyclic Graph (DAG) ya mabadiliko ya hali, ambapo ni sehemu tu ya grafu inayojulikana kila wakati na hakuna ufikiaji wa zingine. Mpango wa RGB ni seti ya msingi ya sheria za mageuzi ya grafu hii Smart contract huanza nayo. Kila Contract Participant inaweza kuongeza kwa sheria hizo (ikiwa hii inaruhusiwa na Schema) na grafu inayotokana imejengwa kutokana na matumizi ya mara kwa mara ya sheria hizo.


## Mali ya kuvu


Vipengee vinavyoweza kuvuliwa katika RGB vinafuata vipimo vya LNPBP RGB-204, wakati RGB-20 inafafanuliwa, data ya kipengee inayojulikana kama "data ya Genesis'' inasambazwa kupitia Lightning Network, ambayo ina kile kinachohitajika ili kutumia kipengee. Njia ya msingi zaidi ya mali hairuhusu uondoaji wa ziada, utoaji wa ziada, uondoaji wa ziada.


Wakati mwingine mtoaji atahitaji kutoa tokeni zaidi katika siku zijazo, yaani, sarafu za kudumu kama vile USDT, ambazo huweka thamani ya kila tokeni ikiambatana na thamani ya sarafu ya mfumuko wa bei kama vile USD. Ili kufikia schemata hii ngumu zaidi ya RGB-20 ipo, na pamoja na data ya Genesis wanahitaji mtoaji kuzalisha mizigo, ambayo pia itazunguka katika Lightning Network; kwa maelezo haya tunaweza kujua jumla ya Supply inayozunguka ya mali. Vile vile hutumika kwa kuchoma mali, au kubadilisha jina lake.


Maelezo yanayohusiana na kipengee yanaweza kuwa ya umma au ya faragha: ikiwa mtoaji anahitaji usiri, anaweza kuchagua kutoshiriki maelezo kuhusu tokeni na kutekeleza shughuli kwa faragha kabisa, lakini pia tuna hali tofauti ambayo mtoaji na wamiliki wanahitaji mchakato mzima uwe wazi. Hii inafanikiwa kwa kushiriki data ya ishara.


## Taratibu za RGB-20


Utaratibu wa kuchoma huzima ishara, tokeni zilizochomwa haziwezi kutumika tena.


Utaratibu wa uingizwaji hutokea wakati ishara zinachomwa moto na kiasi kipya cha ishara sawa huundwa. Hii husaidia kupunguza ukubwa wa data ya kihistoria ya kipengee, ambayo ni muhimu kudumisha kasi ya kipengee.


Ili kusaidia kesi ya utumiaji ambapo inawezekana kuchoma mali bila kuzibadilisha, mpango mdogo wa RGB-20 hutumiwa ambao unaruhusu tu kuchoma mali.


## Vipengee visivyoweza kuvumbuliwa


Vipengee visivyoweza kuvu katika RGB vinafuata vipimo vya LNPBP RGB-215, tunapofanya kazi na NFTs pia tunakuwa na mpango mkuu na mpango mdogo. Miradi hii ina utaratibu wa kuchonga, ambayo huturuhusu kuambatisha data maalum na sehemu ya mmiliki wa ishara, mfano wa kawaida tunaoona katika NFTs leo ni sanaa ya dijiti iliyounganishwa na tokeni. Mtoa tokeni anaweza kuzuia data hii kuchorwa kwa kutumia mpango mdogo wa RGB-21. Tofauti na mifumo mingine ya NFT Blockchain, RGB inaruhusu kusambaza data ya tokeni ya vyombo vya habari vya ukubwa mkubwa kwa njia kamili iliyogatuliwa na inayostahimili udhibiti, kwa kutumia upanuzi wa mtandao wa Lightning P2P uitwao Bifrost, ambao pia hutumika kujenga aina nyingine nyingi za utendaji mahususi wa RGB-Smart contract.


Zaidi ya hayo, mali zinazoweza kuvuliwa na NFTs, RGB na Bifrost zinaweza kutumika kutengeneza aina nyingine za mikataba mahiri, ikiwa ni pamoja na DEXes, dimbwi la ukwasi, sarafu thabiti za algoriti n.k, ambazo tutashughulikia katika makala zijazo.


## NFT kutoka RGB dhidi ya NFT kutoka mifumo mingine



- Hakuna haja ya kuhifadhi ghali ya Blockchain
- Sio haja ya IPFS, kiendelezi cha Lightning Network (kinachoitwa Bifrost) kinatumika badala yake (na kimesimbwa kabisa kutoka mwisho hadi mwisho)
- Hakuna haja ya ufumbuzi maalum wa usimamizi wa data - tena, Bifrost inachukua jukumu hilo
- Hakuna haja ya kuamini tovuti ili kudumisha data ya tokeni za NFT au kuhusu masuala ya mali / Contract ABI
- Usimbaji fiche wa DRM uliojengewa ndani na usimamizi wa Ownership
- Miundombinu ya chelezo kwa kutumia Lightning Network (Bifrost)
- Njia za kuchuma mapato ya yaliyomo (sio tu kuuza NFT yenyewe, lakini ufikiaji wa yaliyomo, mara kadhaa)


## Hitimisho


Tangu kuzinduliwa kwa Bitcoin, karibu miaka 13 iliyopita kumekuwa na utafiti na majaribio mengi katika eneo hilo, mafanikio na makosa yote yameturuhusu kuelewa zaidi jinsi mifumo ya ugatuzi inavyofanya kazi, ni nini inaifanya kuwa ya ugatuzi na ni hatua gani zinazoelekea kuwaongoza kwa ujumuishaji, yote haya yametufanya kuhitimisha kuwa ugatuaji wa kweli ni jambo la kawaida na ngumu kufikiwa na ugumu tu. Bitcoin na ni kwa sababu hii kwamba tunaelekeza juhudi zetu kujenga juu yake.


RGB ina shimo lake la sungura ndani ya shimo la sungura la Bitcoin, wakati nikianguka chini kupitia kwao nitachapisha nilichojifunza, katika makala inayofuata tutakuwa na utangulizi wa nodes za LNP na RGB na jinsi ya kuzitumia.



- 1 https://plan99.net/~mike/Satoshi-emails/thread4.html
- 2 https://btctranscripts.com/chaincode-labs/chaincode-residency/2018-10-22-christian-decker-history-of-lightning/
- 3 https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2016-June/012773.html
- 4 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0020.md
- 5 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0021.md


# Mafunzo ya RGB-nodi


## Utangulizi


Katika somo hili tunaeleza jinsi ya kutumia RGB-nodi kuunda tokeni inayoweza kuvu na jinsi ya kuihamisha, hati hii inategemea onyesho la nodi za RGB na inatofautiana kwa kuwa somo hili linatumia data halisi ya Testnet na kwa hilo, ni lazima tujenge Partially Signed Bitcoin Transaction, PSBT yetu wenyewe kuanzia sasa.


## Mahitaji


Matumizi ya usambazaji wa Linux yanapendekezwa, mafunzo haya yaliandikwa kwa kutumia Pop!OS, ambayo inategemea Ubuntu na utahitaji:



- mizigo
- Msingi wa Bitcoin
- git


Kumbuka: Mafunzo haya yanaonyesha utekelezaji wa amri katika terminal ya Linux, ili kutofautisha kile mtumiaji anachoandika na jibu analopata kwenye terminal, tunajumuisha $ inayoashiria upesi wa bash.


Utahitaji kusakinisha baadhi ya tegemezi:


```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```


Jenga na Ukimbie


RGB-nodi inaendelea kufanya kazi (WIP), ndiyo sababu ni lazima tujiweke katika ahadi mahususi (3f3c520c19d84c66d430e76f0fc68c5a66d79c84) ili kuweza kuikusanya na kuitumia kwa usahihi, kwa hili tunatekeleza amri zifuatazo.


```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```


Sasa tunaikusanya, usisahau kutumia --bendera iliyofungwa kwa sababu kuna badiliko kubwa lililoletwa kwenye toleo la kupiga makofi.


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


Kama mkusanyaji wa Rust anavyotuambia, jozi zilinakiliwa kwenye saraka ya $HOME/.cargo/bin, ikiwa mkusanyaji wako alizinakili mahali tofauti lazima uhakikishe kwamba saraka lazima ijumuishwe katika $PATH.


Kati ya jozi zilizosanikishwa tunaweza kuona daemoni tatu au huduma (faili zinazoisha kwa d) na CLI (mstari wa amri Interface), CLI inaturuhusu kuingiliana na rgbd kuu daemon. Kama katika somo hili tutaendesha nodi mbili, tutahitaji pia wateja wawili, kila mmoja lazima aunganishe na nodi yake, kwa hiyo tunaunda lakabu mbili.


```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```


Tunaweza tu kuendesha lakabu au kuziongeza hadi mwisho wa faili ya $HOME/.bashrc na kuendesha chanzo $HOME/.bashrc.

Nguzo


RGB-nodi haishughulikii aina yoyote ya utendaji unaohusiana na Wallet, hufanya tu kazi mahususi za RGB kwenye data ambayo itatolewa na Wallet ya nje kama msingi wa Bitcoin. Hasa, ili kuonyesha mtiririko wa msingi wa kazi na utoaji na uhamisho, tutahitaji:



- Utoaji_utxo ambao RGB-node-0 itafunga kipengee kipya kilichotolewa.
- receive_utxo ambapo RGB-node-1 inapokea kipengee
- Change_utxo ambapo RGB-node-0 inapokea mabadiliko ya kipengee
- Partially Signed Bitcoin Transaction (tx.PSBT), ambayo ufunguo wake wa kutoa matokeo utabadilishwa ili kujumuisha Commitment kwenye uhamishaji.


Tutatumia Bitcoin core CLI, tunahitaji kuwa na bitcoind daemon inayotumia Testnet, hii itatupa ushirikiano na mwisho tutaweza kutuma mali zetu wenyewe kwa mtumiaji mwingine wa RGB ambaye alifuata mafunzo haya.


Kwa ajili ya unyenyekevu tutaongeza lakabu hii mwishoni mwa ~/.bashrc faili yetu.


```
alias bcli="bitcoin-cli -testnet"
```


Wacha tuorodheshe miamala yetu ya pato ambayo haijatumika na uchague mbili, moja itakuwa issuance_utxo na nyingine change_utxo, haijalishi ni ipi, jambo muhimu ni kwamba mtoaji ana udhibiti wa UTXO hizi mbili.


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


Kabla ya kwenda mbali zaidi tunahitaji kuzungumza juu ya vidokezo, muamala mmoja unaweza kujumuisha matokeo mengi, maoni ni pamoja na 32-byte txid na nambari ya pato ya 4-byte (vout) kurejelea pato maalum lililotenganishwa na koloni :. Katika matokeo yetu ya orodha ya matumizi tunaweza kupata UTXO mbili, kwa kila moja tunaweza kuona txid na vout, hizo ni nje za utoaji_utxo na mabadiliko_utxo.


receive_utxo ni UTXO inayodhibitiwa na mpokeaji, kwa hali hii tutatumia e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 ambayo ni muhtasari kutoka kwa Wallet nyingine.



- utoaji_utxo: 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
- change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- kupokea_utxo: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0


Sasa tutaunda shughuli iliyotiwa saini kwa sehemu (tx.PSBT) ambayo matokeo yake yatarekebishwa ili kujumuisha ahadi ya kuhamisha, kumbuka kuchukua nafasi ya txid na uweke yako mwenyewe, unakoenda Address haijalishi kabisa, inaweza kuwa yako au inaweza kutoka kwa mtu mwingine, haijalishi ni wapi hizo GW-10 zinakwenda.


```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
"psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
"fee": 0.00000280,
"changepos": 0
}
```


Toleo lilitupa PSBT katika usimbaji wa base64 ambayo tutatumia kuunda tx.PSBT.


```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt
```


Wacha tuunde saraka mpya inayoitwa rgbdata ambayo saraka ya data ya kila nodi huhifadhiwa.


```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```


Tayari iko katika $HOME/rgbdata tunaanzisha kila nodi katika vituo tofauti, ambapo ~/.cargo/bin ni saraka ambapo shehena ilinakili jozi zote baada ya usakinishaji wa RGB-nodi.


```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```


## Utoaji


Ili kutoa kipengee tunaendesha rgb0-CLI na amri ndogo za suala linaloweza kugunduliwa, kisha hoja, ticker USDT, jina "USD Tether" na katika mgao tutatumia kiasi kilichotolewa na issuance_utxo kama tunavyoona hapa chini:


```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```


Kipengee kimetolewa. Tumia habari hii kushiriki:

Taarifa ya mali:


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


Tunapata kitambulisho cha mali, tunakihitaji ili kuhamisha kipengee.


```
$ rgb0-cli fungible list

- name: USD Tether
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
```


## generate blinded UTXO


Ili kupokea USDT mpya, RGB-node-1 inahitaji generate blinded UTXO inayolingana na receive_utxo ili kushikilia kipengee.


```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Blinded outpoint: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Outpoint blinding secret: 1679197189805229975
```


Ili kuweza kukubali uhamishaji unaohusiana na UTXO hii, tutahitaji receive_utxo asili na blinding_factor.


## Uhamisho


Ili kuhamisha baadhi ya kiasi cha mali hadi RGB-nodi-1 tunahitaji kuituma kwa blinded UTXO, RGB-node-0 inahitaji kuunda Consignment na ufichuzi, na kuiweka katika shughuli ya Bitcoin. Kisha tutahitaji PSBT ambayo tutarekebisha ili kujumuisha ahadi. Kwa kuongeza, chaguo -i na -a huturuhusu kutoa maoni ya pembejeo ambayo yatakuwa asili ya mali na mgao ambapo tutapokea mabadiliko, lazima tuonyeshe kwa njia ifuatayo @<change_utxo>.


```
$ rgb0-cli fungible transfer utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1

Transfer succeeded, consignments and disclosure are written to "consignment.rgb" and "disclosure.rgb", partially signed witness transaction to "witness.psbt"
Consignment data to share:consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e
```


Hii itaandika faili tatu mpya, Consignment, ufichuzi na PSBT ikiwa ni pamoja na tweak, hii PSBT inaitwa Witness Transaction, Consignment inatumwa kwa RGB-node-1.


## Shahidi


Witness Transaction inapaswa kusainiwa na kutangazwa, kwa hili tunahitaji kuisimba tena.


```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```


Itie saini kwa amri ndogo ya walletprocesspsbt.


```
$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="
{
"psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",
"complete": true
}
```


Sasa malizia na upate hex.


```
$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="
{
"hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
"complete": true
}
```


## Tangaza


Itangaze kwa kutumia amri ndogo ya kutuma pesa ili ithibitishwe kwenye Blockchain.


```
$ bcli sendrawtransaction "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000"
8e3787fe40b5feb3044f892e739bdb4043e10de384255a915a37725811abc3fe
```


## Kubali


Ili kukubali uhamisho unaoingia wa RGB-node-1 inapaswa kupokea faili ya Consignment kutoka kwa RGB-node-0, kuwa na receive_utxo na blinding_factor sambamba kuzalishwa wakati wa kupofusha kizazi cha UTXO.


```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975

Asset transfer successfully accepted.
```


Sasa tunaweza kuona (katika sehemu inayojulikana ya Allocations) mgao mpya wa vitengo 100 vya mali katika <receive_utxo> kwa kutekeleza:


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


Kwa kuwa receive_utxo ilikuwa blinded uhamishaji ulipofanywa, mlipaji RGB-node-0 hana taarifa kuhusu mahali ambapo 100 USDT ilitumwa, kwa hivyo eneo halionyeshwi katika knownAllocations .


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


Lakini kama unavyoona RGB-node-0 haiwezi kuona mabadiliko ya mali 900 ambayo tulipeana kwa amri ya uhamishaji na -a hoja. Ili kusajili mabadiliko RGB-node-0 inahitaji kukubali ufumbuzi.


```
$ rgb0-cli fungible enclose disclosure.rgb

Disclosure data successfully enclosed.
```


Ikiwa RGB-node-0 ilifanikiwa unaweza kuona mabadiliko kwa kuorodhesha kipengee.


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


## Hitimisho


Tumeweza kuunda kipengee kinachoweza kuvuliwa na kuihamisha kutoka kwa shughuli moja hadi nyingine kwa njia ya faragha, ikiwa tutaangalia shughuli iliyothibitishwa katika Block explorer hatutapata chochote tofauti na shughuli za kawaida, hii ni kutokana na ukweli kwamba RGB hutumia mihuri ya matumizi moja ili kurekebisha shughuli, Katika chapisho hili, ninafanya utangulizi wa jinsi RGB inavyofanya kazi.


Chapisho hili linaweza kuwa na hitilafu, ukipata kitu tafadhali nijulishe ili kuboresha mwongozo huu, mapendekezo, na ukosoaji pia unakaribishwa, utapeli wa furaha! 🖖