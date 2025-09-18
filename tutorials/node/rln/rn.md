---
name: RGB Lightning Node
description: Ni gute notanguza urudodo rw’umuravyo rujanye n’ivyo RGB rufise RLN?
---
![cover](assets/cover.webp)


Muri iyi nyigisho y’intambwe ku yindi, uzomenya ingene woshiraho urudodo rwa Lightning RGB ku bidukikije vya Regtest. Turabona ingene twokora ibimenyetso vya RGB tukabikwiragiza mu mihora.


## Umugambi wa RLN


Ishirahamwe rya Bitfinex rya RGB ryakoze kuva mu 2022 kugira ngo ritunganye ibidukikije vya RGB mu gutegura ikirundo c’ubuhinga bushitse. Aho gushimikira ku kintu kimwe c’ubudandaji, utwigoro twayo twibanze ku gutuma amatafari y’ubuhinga bufunguye aboneka, agatanga umusanzu ku mirongo ngenderwako y’amasezerano ya RGB no guhingura ibimenyetso vyo gushirwa mu ngiro.


Mu vyo Bitfinex yashizeko mu bijanye n’ibidukikije vya RGB harimwo [ububiko bw’ibitabu bwa *RGBlib*] (https://github.com/RGB-Tools/RGB-lib), bwanditswe muri Rust kandi bushobora gushikwako biciye ku gufatanya mu rurimi rwa Kotlin na Python, ivyo bikaba vyorosha cane gukoresha ubuhinga bwa RGB. uburyo bwo gukorana n’abandi.


Ishirahamwe rya Bitfinex ryakoze kandi telefone ngendanwa yitwa RGB, yitwa "[*Iris Wallet*](https://iriswallet.com/)", iboneka kuri Android. Iyi Wallet ikoresha ikoreshwa rya proxy server ya RGB kugira ngo ushobore gucunga neza amakuru ya off-chain (*ibirungikwa*) ku *Client-side Validation* kuri RGB.


Bitfinex kandi yarateguye umugambi wa `RGB-umuravyo-node` (RLN). Iyi ni Rust daemon ishingiye kuri Fork ya `Rust-umuravyo` (LDK), yahinduwe kugira ngo yitwararike ukubaho kw’itunga rya RGB mu muhora. Iyo umurongo ufunguwe, ukubaho kw’ibimenyetso vya RGB birashobora kugaragazwa, kandi igihe cose umurongo uvuguruwe, State Transition iraremwa yerekana ukuntu ibimenyetso bigabanywa mu bisohoka vya Lightning. Ibi bishoboza :




- Gufungura imirongo y’umuravyo mu USDT, nk’akarorero;
- Ivyo bimenyetso bica mu nzira, igihe cose inzira zo kubijana zifise amahera ahagije;
- Gukoresha igihano ca Lightning n'ubuhinga bwo gufunga igihe ataco uhinduye: gusa Anchor ihinduka rya RGB mu gisohoka c'inyongera ca Commitment Transaction.


Kode ya RLN iracari mu rwego rwayo rwa alpha: turahimiriza kuyikoresha muri **regtest** canke kuri **Testnet** gusa.


## RGB ivyibutsa


RGB ni porotokole ikora hejuru ya Bitcoin kandi yigana imikorere ya Smart contract n’ugucungera umutungo w’ubuhinga bwa none, ata kuremerera cane Blockchain ishingiyeko. Udakunze amasezerano asanzwe y'ubwenge ya On-Chain (nk'akarorero kuri Ethereum), RGB yizigiye uburyo bwa "*Client-side Validation*": amakuru menshi n'amateka y'ivy'ubuzima birahindurwa kandi bikabikwa gusa n'abaje mu nama, mu gihe Bitcoin Blockchain ikoresha gusa ubuhinga buto buto bw'ubuhinga bwa none ( *Guvuga*). Mu masezerano ya RGB, Bitcoin Blockchain rero ikora gusa nk’umurongo w’igihe n’uburyo bwo kurinda Double-spending.


RGB Contract itunganijwe nk’imashini y’igihugu y’iterambere. Bitangura na Genesis isobanura ivy'intango (idondora, nk'akarorero, Supply, ticker canke ibindi bimenyetso) hakurikijwe Schema yanditswe neza kandi ikoranijwe. Impinduka za Leta n’iyo bikenewe, Impinduka za Leta zica zikoreshwa kugira ngo zihindure canke zagure iyo Leta. Igikorwa kimwekimwe cose, haba mu kwimurira ibintu bishobora guhinduka (RGB20) canke mu kurema ibintu bidasanzwe (RGB21), birimwo *Ibimenyetso bikoreshwa rimwe*. Ivyo bihuza Bitcoin UTXOs n’intara za off-chain kandi bikabuza gukoresha amahera kabiri, mu gihe bituma habaho ibanga n’ugushobora gukoreshwa.


Kugira ngo umenye vyinshi ku bijanye n’ingene umurongo wa RGB ukora, ndagusavye gufata iyi nyigisho yuzuye:


https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

## RGB-ihuye n'umuravyo gushirwaho


Kugira ngo dukoreshe kandi dushiremwo `RGB-lightning-node` binary, dutangura dukora clone y'ububiko n'ibice vyabwo, hanyuma tugakoresha :


```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```


![RLN](assets/fr/01.webp)




- Ihitamwo rya `--recurse-submodules` na ryo nyene rikora ibikoresho bikenewe (harimwo n'ivyo `Rust-lightning` vyahinduwe);
- Ihitamwo rya `--shallow-submodules` rigabanya uburebure bw'iyi clone kugira ngo ryihute gukuraho, mu gihe riguma ritanga uburyo bwo gushika ku bikorwa vy'ingenzi.


Kuva ku muzi w'umugambi, koresha itegeko rikurikira kugira ngo ukoreshe kandi ushiremwo ibice bibiri :


```bash
cargo install --locked --debug --path .
```


![RLN](assets/fr/02.webp)




- `--locked` ikora neza ko verisiyo y'ibiva ku bindi yubahirizwa;
- `--debug` si ngombwa, ariko ishobora kugufasha kwibanda (ushobora gukoresha `--release` niba ushaka) ;
- `--inzira .` ibwira `cargo install` gushiramwo kuva mu bubiko buriho.


Ku mpera y'iri tegeko, `RGB-umuravyo-node` izoboneka mu `$CARGO_HOME/bin/` yawe. Raba neza ko iyi nzira iri muri `$PATH` yawe kugira ngo ushobore guhamagara itegeko rivuye mu bubiko bwose.


## Ibisabwa


Kugira ngo ikore, `RGB-umuravyo-node` daemon ikeneye kubaho n'imiterere ya :




- Urudodo bitcoind


Instance yose ya RLN izokenera kuvugana na `bitcoind` kugira ngo itangaze kandi ikurikirane ibikorwa vyayo vya On-Chain. Ivyemezo (kwinjira/ijambobanga) na URL (umushitsi/icuma) bizokenerwa gutangwa kuri daemon.




- **Index** (Electrum canke Esplora)


daemon itegerezwa kuba ishoboye gutanga urutonde no gutohoza ibikorwa vya On-Chain, cane cane kugira ngo ironke UTXO umutungo washizweko. Uzokenera gutanga URL ya server yawe ya Electrum canke Esplora.




- Uwuserukira **RGB**


Serveri ya proxy ni igice (kidasanzwe, ariko kiraremeshwa cane) co kworohereza Exchange ya RGB *ibirungikwa* hagati y'abagenzi ba Lightning. Na none, URL itegerezwa gusobanurwa.


IDs na URLs zishirwamwo iyo daemon *ifunguwe* biciye kuri API.


## Gusubiramwo igerageza


Kugira ngo ukoreshe neza, hariho inyandiko `regtest.sh` itangura ubwayo, biciye kuri Docker, urutonde rw'ibikorwa: `bitcoind`, `amashanyarazi` (indexer), `RGB-umukozi-w'ubutumwa`.


![RLN](assets/fr/03.webp)


Ivyo bigufasha gutanguza ibidukikije vyo mu karere, biri ukwavyo, vyatunganijwe imbere y’igihe. Irema kandi igasenyura ibikoresho n’ububiko bw’amakuru ku gusubira gutangura kwose. Tuzotangura dutangura :


```bash
./regtest.sh start
```


Iyi nyandiko izo :




- Rema `docker/` ububiko bwo kubika ;
- Gukoresha `bitcoind` mu regtest, hamwe n'urutonde `amashanyarazi` na `RGB-umukozi-w'ubutumwa` ;
- Rindira gushika vyose biteguye gukoreshwa.


![RLN](assets/fr/04.webp)


Igikurikira, tuzotanguza ama node menshi ya RLN. Mu bice bitandukanye, genda, nk'akarorero (kugira ngo utangure 3 RLN nodes) :


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




- Igikoresho `--network regtest` kigaragaza ikoreshwa ry'imiterere ya regtest;
- `--daemon-kwumviriza-icuma` yerekana ku cyuho ca REST urudodo rw'umuravyo ruzokwumviriza amahamagara ya API (JSON);
- `--ldk-urunganwe-rutega yompi` igaragaza icuma ca Lightning P2P co kwumvirizako;
- `dataldk0/`, `dataldk1/` ni inzira zija mu bubiko (buri nzira ibika amakuru yayo ukwayo).


Ubu ushobora gushitsa amabwirizwa ku nzira zawe za RLN ukoresheje umucukumbuzi wawe, ushimira API. Cane cane, aha niho ushobora *gufungura* amadayimoni. Gufungura gusa umucukumbuzi kuri mudasobwa imwe n'ibice vyawe, hanyuma winjize URL :


```url
https://rgb-tools.github.io/rgb-lightning-node/
```


Kugira ngo node ifungure umurongo, itegerezwa kubanza kugira bitcoins kuri Address yashizweho n’itegeko rikurikira (ku node n°1, nk’akarorero):


```bash
curl -X POST http://localhost:3001/address
```


Inyishu izoguha Address.


![RLN](assets/fr/06.webp)


Ku kigeragezo ca `bitcoind`, tugiye gucukura amafaranga makeyi. Kwiruka :


```bash
./regtest.sh mine 101
```


![RLN](assets/fr/07.webp)


Wohereze amafaranga kuri node Address yavutse haruguru:


```bash
./regtest.sh sendtoaddress <address> <amount>
```


![RLN](assets/fr/08.webp)


Hanyuma ukore ububiko bwo kwemeza ugucuruza:


```bash
./regtest.sh mine 1
```


![RLN](assets/fr/09.webp)


## Testnet gutangura (ata Docker)


Niba ushaka kugerageza ikintu gishoboka, ushobora gutanguza amanode ya RLN kuri Testnet aho gutanguza muri Regtest, yerekana ibikorwa vya Leta, canke ibikorwa ugenzura:


```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```


Ku mburabuzi, iyo ata ntunganyo ibonetse, daemon izogerageza gukoresha :




- `ibikoni_rpc_umushitsi`: `umuyagankuba.isakoshi.com`
- `Ikivuko_cy'amafaranga_rpc`: `18332`
- urutonde_url`: `ssl://umuyagankuba.isakoshi.com:50013`
- `iherezo_ry'umuserukira`: `rpcs: umuserukira.


Na kwinjira :




- `izina_ry'ukoresha_rpc`: 'ukoresha`
- `izina_ry'ukoresha_rpc`: 'ijambobanga'


Ushobora kandi guhindura izo Elements biciye ku `init`/`ugufungura` API.


## Gutanga urupapuro rwa RGB rwa token


Kugira ngo dusohore token, tuzotangura dukoreshe "amabara" UTXOs:


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


Birumvikana ko ushobora guhindura urutonde rw’ibintu. Kugira ngo twemeze ibikorwa, ducukura :


```bash
./regtest.sh mine 1
```


Ubu turashobora kurema umutungo wa RGB. Itegeko rizovana n'ubwoko bw'umutungo wipfuza kurema n'imirongo yawo. Aha ndiko ndakora NIA (*Itunga Ridashobora Gufutwa*) token ryitwa "PBN" rifise Supply y'ibice 1000. `Ugushikama` bigufasha gusobanura ukuntu ibice bishobora kugabanywa.


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


Inyishu irimwo ID y’umutungo mushasha waremwe. Ibuka kwandika iki kimenyetso. Mu vyerekeye jewe, ni :


```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```


![RLN](assets/fr/12.webp)


Ushobora rero kuyirungika On-Chain, canke ukayishira mu muhora w’umuravyo. Ivyo nyene ni vyo tuzokora mu gice gikurikira.


## Gufungura umurongo no gutanga umutungo wa RGB


Utegerezwa kubanza gufatanya urudodo rwawe n'umugenzi kuri Lightning Network ukoresheje itegeko `/connectpeer`. Mu karorero kanje, ndagenzura izo node zompi. Rero nzogarura urufunguzo rwa bose rw'umurongo wanje wa kabiri w'umuravyo nkoresheje iri tegeko:


```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```


Itegeko rigarura urufunguzo rwa bose rw'uruzitiro rwanje n°2 :


```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```


![RLN](assets/fr/13.webp)


Ibikurikira, tuzofungura umurongo mu kugaragaza umutungo ubereye (`PBN`). Itegeko `/openchannel` rigufasha gusobanura ubunini bw'umurongo mu satoshis no guhitamwo gushiramwo umutungo wa RGB. Bivana n'ico ushaka kurema, ariko muri jewe, itegeko ni :


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


Ibindi ubimenye hano:




- `peer_pubkey_and_opt_addr`: Ikimenyetso c'umugenzi twipfuza gufatanya (urufunguzo rwa bose twabonye mbere);
- `ubushobozi_sat`: Ubushobozi bwose bw'umurongo mu satoshis ;
- `push_msat`: Amahera mu millisatoshis mu ntango yimuriwe ku mugenzi igihe umurongo ufunguwe (aha nca nshira 10.000 Sats kugira ngo ashobore gukora RGB yimuriwe mu nyuma) ;
- `asset_amount`: Umubare w'itunga rya RGB rizoshikirizwa umurongo ;
- `asset_id` : Ikimenyetso kidasanzwe c'umutungo wa RGB ukora mu muhora;
- `public`: Igaragaza nimba umurongo ukwiye gushikirizwa abantu bose kugira ngo ukoreshe umurongo ku rubuga.


![RLN](assets/fr/14.webp)


Kugira ngo bemeze ko ivyo bigurishwa, amabuye 6 aracukurwa:


```bash
./regtest.sh mine 6
```


![RLN](assets/fr/15.webp)


Umurongo w'umuravyo ubu warafunguye kandi urimwo n'ibimenyetso 500 vya `PBN` ku ruhande rwa node n°1. Niba urudodo n°2 rushaka kwakira ibimenyetso vya `PBN`, rutegerezwa kuba generate na Invoice. Ehe ingene wobikora:


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


Hamwe :




- `amt_msat`: Igitigiri c'ama Invoice mu milisatoshi (nibura 3000 Sats) ;
- `igihe_c'iherezo` : Invoice igihe c'iherezo mu masegonda ;
- `asset_id` : Ikimenyetso c'umutungo wa RGB ufitaniye isano na Invoice ;
- `umutungo_umubare`: Umubare w'umutungo wa RGB uzokwimurirwa n'iyi Invoice.


Mu kwishura, uzoronka RGB Invoice:


```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```


![RLN](assets/fr/16.webp)


Ubu tuzoriha iyi Invoice kuva ku nzira ya mbere, ifise amahera akenewe n'iyi `PBN` token:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```


![RLN](assets/fr/17.webp)


Ukwishurwa kwarakozwe. Ivyo bishobora kugenzurwa mu gushitsa itegeko :


```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```


![RLN](assets/fr/18.webp)


Ehe ingene woshiraho urudodo rwa Lightning rwahinduwe kugira ngo rutware itunga rya RGB. Iryo yerekanwa rishingiye kuri :




- Ibidukikije vy'igerageza (biciye muri `./igerageza.sh`) canke Testnet ;
- Igikoresho c'umuravyo (`RGB-igikoresho-c'umuravyo`) gishingiye kuri `bitcoind`, urutonde n'umurongo w'umuravyo` ;
- Urutonde rwa JSON REST APIs zo gufungura/gufunga imirongo, gutanga ibimenyetso, gutanga itunga biciye ku muravyo, n'ibindi.


Urakoze kuri iyi nzira :




- Ivy’ugukorana n’umuravyo birimwo igisohoka c’inyongera (OP_RETURN canke Taproot) n’ugushinga intahe kw’ihinduka rya RGB;
- Ivyo kwimurira amahera bikorwa mu buryo bumwe nyene n’ubw’amahera ya kera y’umuravyo, ariko hakongerwako RGB token;
- Ivyiyumviro vyinshi vya RLN birashobora guhuzwa n’inzira no kugerageza kwishura mu vyiyumviro vyinshi, igihe cose hariho amahera ahagije mu bitcoins no mu mutungo RGB ku nzira.


Niwaba wabonye ko iyi nyigisho ari ngirakamaro, noshima cane woshira urukumu rwa Green aha hepfo. Turabinginze ntimwitinye gusangira iyi nkuru ku mbuga ngurukanabumenyi zanyu. Murakoze cane!


Ndasaba kandi iyi yindi nyigisho aho ndasigura ingene wokoresha igikoresho ca RGB CLI cakozwe n’ishirahamwe LNP/BP kugira ngo ukore RGB Contract:


https://planb.network/tutorials/node/others/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4