---
name: RGB Lightning Node
description: Kako naj zaženem RGB-kompatibilno Lightning vozlišče z RLN?
---
![cover](assets/cover.webp)


මෙම පියවරෙන් පියවර උපදේශනයේදී, ඔබට Regtest පරිසරයක Lightning RGB නියමක සකසන්නේ කෙසේද යන්න ඉගෙන ගන්නට ලැබේ. අපි RGB ටෝකන නිර්මාණය කර ඒවා නාලිකාවල ගමනාගමනය කරන ආකාරය බලමු.


## RLN ව්‍යාපෘතිය


Bitfinex හි RGB කණ්ඩායම 2022 සිට RGB පරිසර පද්ධතිය වර්ධනය කිරීම සඳහා සම්පූර්ණ තාක්ෂණික ගොනුවක් සංවර්ධනය කිරීමට කටයුතු කරමින් සිටී. එකම වාණිජ නිෂ්පාදනයක් අරමුණු කර ගැනීම වෙනුවට, එහි උත්සාහයන් විවෘත මූලාශ්‍ර මෘදුකාංග ගඩොල් ලබා දීමට, RGB ප්‍රොටෝකෝල විශේෂණයන්ට දායක වීමට සහ ක්‍රියාත්මක කිරීමේ යොමු සෑදීමට කේන්ද්‍රගත වේ.


Bitfinexගේ RGB පරිසර පද්ධතියට ඇති විශේෂ දායකත්වයන් අතර [*RGBlib* පුස්තකාලය](https://github.com/RGB-Tools/RGB-lib) වේ, Rust භාෂාවෙන් ලියන ලද සහ Kotlin සහ Python හි බැඳීම් මඟින් ප්‍රවේශ විය හැකි, RGB යෙදුම් සංවර්ධනය සංකීර්ණ වලංගුකරණ සහ නිරත වීමේ යාන්ත්‍රණ ආවරණය කිරීමෙන් බොහෝ පහසු කරයි.


Bitfinex කණ්ඩායම Android හි ලබා ගත හැකි "[*Iris Wallet*](https://iriswallet.com/)" නම් RGB ජංගම Wallet එකක් ද නිර්මාණය කර ඇත. මෙම Wallet, RGB මාර්ගකිරීම් සේවාදායකයක භාවිතය ඒකාබද්ධ කර RGB හි *Client-side Validation* සඳහා off-chain දත්ත හුවමාරු (*කප්පාදු*) පහසුවෙන් කළමනාකරණය කරයි.


Bitfinex je razvil tudi projekt `RGB-lightning-node` (RLN). To je Rust daemon, ki temelji na Fork `Rust-lightning` (LDK), prilagojen za upoštevanje obstoja RGB sredstev v kanalu. Ko je kanal odprt, je mogoče določiti prisotnost RGB žetonov, in vsakič, ko se stanje kanala posodobi, se ustvari State Transition, ki odraža razporeditev žetonov v Lightning izhodih. To omogoča :




- USDT සඳහා විදුලි නාලිකා විවෘත කරන්න, උදාහරණයක් ලෙස;
- මෙම ටෝකන මාර්ගය හරහා මාර්ගගත කරන්න, සපයන ලද මාර්ග මාර්ගවල ප්‍රමාණවත් ද්‍රවතාවය තිබේ නම්;
- විදුලි කුණාටුවේ දඬුවම සහ කාල අගුල තර්කය වෙනස්කම් නොකර ප්‍රයෝජනයට ගන්න: Commitment Transaction හි අමතර ප්‍රතිදානයක Anchor සිට RGB මාරුව සරලව කරන්න.


RLN කේතය තවමත් එහි ඇල්ෆා අවධියේ පවතී: අපි එය **regtest** හෝ **Testnet** මත පමණක් භාවිතා කිරීමට නිර්දේශ කරමු.


## RGB ප්‍රොටෝකෝලය මතක් කිරීම


RGB je protokol, ki deluje na vrhu Bitcoin in emulira funkcionalnost Smart contract ter upravljanje digitalnih sredstev, ne da bi preobremenil Blockchain, na katerem temelji. Za razliko od konvencionalnih pametnih pogodb On-Chain (kot na primer na Ethereumu), RGB temelji na sistemu "*Client-side Validation*": večina podatkov in zgodovin statusov se izmenjuje in shranjuje izključno pri vpletenih udeležencih, medtem ko Bitcoin Blockchain gosti le majhne kriptografske zaveze (prek mehanizmov, kot sta *Tapret* ali *Opret*). V protokolu RGB Bitcoin Blockchain zato služi le kot strežnik za časovno žigosanje in sistem zaščite Double-spending.


RGB Contract je strukturiran kot evolucijski stroj stanj. Začne se z Genesis, ki določa začetno stanje (opisuje na primer Supply, oznako ali druge metapodatke) v skladu s strogo tipiziranim in prevedenim Schema. Nato se uporabijo prehodi stanj in, če je potrebno, razširitve stanj za spreminjanje ali razširitev tega stanja. Vsaka operacija, bodisi prenos zamenljivih sredstev (RGB20) ali ustvarjanje edinstvenih sredstev (RGB21), vključuje *enkratno uporabo pečatov*. Ti povezujejo Bitcoin UTXO-je z off-chain stanji in preprečujejo dvojno porabo, hkrati pa zagotavljajo zaupnost in razširljivost.


RGB ප්‍රොටෝකෝලය කෙසේ ක්‍රියා කරන්නේද යන්න පිළිබඳව වැඩිදුර දැන ගැනීමට, මම ඔබට මෙම සම්පූර්ණ පුහුණු පාඨමාලාව අනුමත කරනවා:


https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

## RGB-අනුකූල Lightning නියුඩ් ස්ථාපනය


`RGB-lightning-node` බයිනරි එක සංග්‍රහය සහ ස්ථාපනය කිරීමට, අපි ගබඩාව සහ එහි උප-මොඩියුල පිටපත් කිරීමෙන් ආරම්භ කර, පසුව :


```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```


![RLN](assets/fr/01.webp)




- `--recurse-submodules` විකල්පය අවශ්‍ය උප-උපාංග (සංශෝධිත `Rust-lightning` සංස්කරණය ඇතුළුව) ද පරිපූරකව පිටපත් කරයි;
- `--shallow-submodules` විකල්පය බාගත කිරීම වේගවත් කිරීමට ක්ලෝනයේ ගැඹුර සීමා කරයි, එහෙත් මූලික කමිටු වෙත ප්‍රවේශය ලබා දේ.


ප්‍රජා ව්‍යාපෘතියේ මූලිකයෙන්, ද්වීකය සංග්‍රහය සහ ස්ථාපනය කිරීම සඳහා පහත විධානය ක්‍රියාත්මක කරන්න :


```bash
cargo install --locked --debug --path .
```


![RLN](assets/fr/02.webp)




- `--locked` යනු අනුයෝජිතයන්ගේ අනුවාදය ගරු කිරීම සහතික කරයි;
- `--debug` අනිවාර්ය නොවේ, නමුත් ඔබට අවධානය යොමු කිරීමට උපකාරී විය හැක (ඔබ කැමති නම් `--release` භාවිතා කළ හැක) ;
- `--path .` `cargo install` කර්මාන්තය වත්මන් නාමාවලියෙන් ස්ථාපනය කිරීමට කියයි.


මෙම විධානයේ අවසානයේ, `RGB-lightning-node` ක්‍රියාත්මක කළ හැකි ගොනුව ඔබේ `$CARGO_HOME/bin/` හි ලබා ගත හැකි වේ. ඔබට ඕනෑම නාමාවලියකින් විධානය ක්‍රියාත්මක කළ හැකි වන පරිදි මෙම මාර්ගය ඔබේ `$PATH` තුළ ඇති බවට වග බලා ගන්න.


## ප්‍රාථමික අවශ්‍යතා


RGB-lightning-node` daemon delovati, potrebuje prisotnost in konfiguracijo:




- `bitcoind`** නියමකය


प्रत्येक RLN उदाहरणले यसको On-Chain लेनदेन प्रसारण र अनुगमन गर्न `bitcoind` सँग सञ्चार गर्न आवश्यक छ। प्रमाणीकरण (लगइन/पासवर्ड) र URL (होस्ट/पोर्ट) daemon लाई प्रदान गर्न आवश्यक हुनेछ।




- සූචිකාරක** (Electrum හෝ Esplora)


daemon යන්ත්‍රය On-Chain ගනුදෙනු ලැයිස්තුගත කිරීම සහ විමසුම සඳහා හැකියාවක් තිබිය යුතු අතර, විශේෂයෙන්ම වත්කමක් සම්බන්ධ කර ඇති UTXO සොයා ගැනීම සඳහා. ඔබේ Electrum සේවාදායකය හෝ Esplora හි URL එක විශේෂිත කිරීමට ඔබට අවශ්‍ය වේ.




- RGB** ප්‍රොක්සි


ප්‍රොක්සි සේවාදායකය යනු කොම්පොනන්තුවකි (විකල්ප, නමුත් ඉතාමත් නිර්දේශිත) Lightning සමකයන් අතර Exchange සහ RGB *කප්පාදු* සරල කිරීම සඳහා. නැවතත්, URL එකක් විශේෂිත කළ යුතුය.


daemon API හරහා *අගුළු ඇරිය* විට හැඳුනුම්පත් සහ URL ඇතුළත් වේ.


## Regtest lansiranje


සරල භාවිතය සඳහා, Docker හරහා ස්වයංක්‍රීයව සේවා කට්ටලයක් ආරම්භ කරන `regtest.sh` ස්ක්‍රිප්ටයක් ඇත: `bitcoind`, `electrs` (සූචිකාරකය), `RGB-proxy-server`.


![RLN](assets/fr/03.webp)


මෙය ඔබට ස්ථානීය, වෙන්වූ, පෙර-වින්‍යාස කළ පරිසරයක් ආරම්භ කිරීමට ඉඩ සලසයි. එය කන්ටේනර් සහ දත්ත නාමාවලියන් සෑදීම සහ විනාශ කිරීම සෑම නැවත ආරම්භයකදීම සිදු කරයි. අපි ආරම්භ කරමින් පටන් ගනිමු:


```bash
./regtest.sh start
```


මෙම ස්ක්‍රිප්ටය :




- `docker/` නාමාවලියක් තනන්න ;
- Zaženite `bitcoind` v načinu regtest, kot tudi indeksator `electrs` in `RGB-proxy-server` ;
- බවිතා කිරීමට සියල්ල සූදානම් වන තුරු රැඳී සිටින්න.


![RLN](assets/fr/04.webp)


අපි ඊළඟට RLN නියුඩ් කිහිපයක් ආරම්භ කරන්නෙමු. වෙන වෙනම ශෙල් වල, උදාහරණයක් ලෙස ධාවනය කරන්න (RLN නියුඩ් 3ක් ආරම්භ කිරීමට) :


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




- `--network regtest` පරාමිතිය regtest වින්‍යාසය භාවිතා කිරීම පෙන්වයි;
- `--daemon-listening-port` REST පෝර්ට් එක මත Lightning node එක API ඇමතුම් (JSON) සඳහා ඇහුම්කම් දෙන ආකාරය සදහන් කරයි;
- `--ldk-peer-listening-port` LW-57 වරාය කුමන විදුලි කුණාටුවක් අසන්නාහී යන්න විශේෂිත කරයි;
- `dataldk0/`, `dataldk1/` යනවා සංග්‍රහ නාමාවලියන් වෙත මාර්ග වේ (සෑම නෝඩයකම එහි තොරතුරු වෙනම සංග්‍රහ කරයි).


Zdaj lahko iz brskalnika izvajate ukaze na svojih RLN vozliščih, zahvaljujoč API-ju. Tukaj lahko še posebej *odklenete* demone. Preprosto odprite brskalnik na istem računalniku kot vaša vozlišča in vnesite URL:


```url
https://rgb-tools.github.io/rgb-lightning-node/
```


නෝඩයක් නාලිකාවක් විවෘත කිරීමට, එය පළමුව bitcoins තිබිය යුතුය Address මගින් ජනනය කරන ලද පහත විධානය (උදාහරණයක් ලෙස, නෝඩය අංක 1 සඳහා) සමඟ:


```bash
curl -X POST http://localhost:3001/address
```


පිළිතුර ඔබට Address ලබා දෙනු ඇත.


![RLN](assets/fr/06.webp)


`bitcoind` Regtest මත, අපි බිට්කොයින් කිහිපයක් මයින් කිරීමට යන්නේ. ධාවනය කරන්න :


```bash
./regtest.sh mine 101
```


![RLN](assets/fr/07.webp)


මීට ඉහත නිපදවා ඇති Address නියැදියට මුදල් යවන්න:


```bash
./regtest.sh sendtoaddress <address> <amount>
```


![RLN](assets/fr/08.webp)


پوءِ ٽرانزيڪشن جي تصديق لاءِ هڪ بلاڪ مائن ڪريو:


```bash
./regtest.sh mine 1
```


![RLN](assets/fr/09.webp)


## Testnet ප්‍රේක්ෂප්තය (Docker නොමැතිව)


Če želite preizkusiti bolj realističen scenarij, lahko zaženete RLN vozlišča na Testnet namesto v Regtest, usmerjena na javne storitve ali storitve, ki jih nadzorujete:


```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```


දෞලින්, කිසිදු වින්‍යාසයක් සොයා නොමැති නම්, daemon උත්සාහ කරනු ඇත :




- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-RPC`


Z vpisom :




- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`


ඔබට මෙම Elements `init`/`unlock` API හරහා අභිරුචිකරණය කළ හැක.


## RGB ටෝකනය නිකුත් කිරීම


žetona izdati, bomo začeli z ustvarjanjem "barvljivih" UTXO-jev:


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


ඔබට, නියත වශයෙන්ම, අනුපිළිවෙල අනුකූල කළ හැක. ගනුදෙනුව තහවුරු කිරීමට, අපි :


```bash
./regtest.sh mine 1
```


Zdaj lahko ustvarimo sredstvo RGB. Ukaz bo odvisen od vrste sredstva, ki ga želite ustvariti, in njegovih parametrov. Tukaj ustvarjam žeton NIA (*Non Inflatable Asset*) z imenom "PBN" z Supply v višini 1000 enot. `precision` vam omogoča, da določite deljivost enot.


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


Odgovor vključuje ID na novo ustvarjenega sredstva. Ne pozabite zabeležiti tega identifikatorja. V mojem primeru je:


```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```


![RLN](assets/fr/12.webp)


Nato ga lahko prenesete na On-Chain ali pa ga dodelite v Lightning kanal. Točno to bomo storili v naslednjem razdelku.


## චැනලයක් විවෘත කිරීම සහ RGB සම්පතක් මාරු කිරීම


Najpre morate povezati svoj vozel s vrstnikom na Lightning Network z uporabo ukaza `/connectpeer`. V mojem primeru nadzorujem oba vozlišča. Zato bom pridobil javni ključ svojega drugega Lightning vozlišča s tem ukazom:


```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```


කමාන්ඩ් එකෙන් මගේ නෝඩ් අංක 2 හි පොදු යතුර ලබා දේ:


```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```


![RLN](assets/fr/13.webp)


Nato bomo odprli kanal z določitvijo ustreznega sredstva (`PBN`). Ukaz `/openchannel` vam omogoča, da določite velikost kanala v satoshijih in se odločite za vključitev sredstva RGB. Odvisno je od tega, kaj želite ustvariti, vendar je v mojem primeru ukaz:


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


මෙහි වැඩිදුර තොරතුරු ලබා ගන්න:




- `peer_pubkey_and_opt_addr`: අපි සම්බන්ධ වීමට කැමති සමකයගේ හඳුනාගැනීමක් (අපි කලින් සොයාගත් මහජන යතුර);
- `capacity_sat`: සම්පූර්ණ නාලිකා ධාරිතාවය සතෝෂි වලින් ;
- `push_msat`: චැනලය විවෘත කරන විට ආරම්භකව සමාන පාර්ශවයට මියිලිසටෝෂිස් වලින් මාරු කරන මුදල (මෙහි මම වහාම 10,000 Sats මාරු කරමි, එවිට ඔහු පසුව RGB මාරු කිරීමක් කළ හැක) ;
- `asset_amount`: RGB සම්පත් නාලිකාවට කැප කිරීමට ඇති ප්‍රමාණය ;
- `asset_id` : RGB සම්පත්ය නාලිකාවේ නිරත වන විශේෂ අනන්‍යකාරකය;
- `public`: පාරිභෝගික ජාලයේ මාර්ගගත කිරීම සඳහා නාලිකාව මහජනතාවට විවෘත කළ යුතුද යන්න සලකුණු කරයි.


![RLN](assets/fr/14.webp)


ගනුදෙනුව තහවුරු කිරීමට, කොටස් 6ක් පතල් ගසයි:


```bash
./regtest.sh mine 6
```


![RLN](assets/fr/15.webp)


ලයිට්නින් නාලිකාව දැන් විවෘත වී ඇති අතර node n°1 පැත්තේ 500 `PBN` ටෝකන ද අඩංගු වේ. node n°2 ට `PBN` ටෝකන ලබා ගැනීමට අවශ්‍ය නම්, එය generate සහ Invoice කළ යුතුය. මෙන්න එය කරන ආකාරය:


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


සමඟ :




- `amt_msat`: Invoice කාචයේ මිලියම් සටෝෂි වලින් ප්‍රමාණය (අවම 3000 Sats) ;
- `expiry_sec` : Invoice කල් ඉකුත් වීමේ කාලය තත්පර වලින්;
- `asset_id` : Invoice සමඟ සම්බන්ධ RGB වත්කමගේ හඳුනාගැනීමකරු ;
- `asset_amount`: Invoice සමඟ මාරු කිරීමට ඇති RGB සම්පත් ප්‍රමාණය.


ප්‍රතිචාරයක් ලෙස, ඔබට RGB Invoice ලැබෙනු ඇත:


```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```


![RLN](assets/fr/16.webp)


Zdaj bomo plačali ta Invoice iz prvega vozlišča, ki ima potrebno gotovino z žetonom `PBN`:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```


![RLN](assets/fr/17.webp)


ගෙවීම සිදු කර ඇත. මෙය විධානය ක්‍රියාත්මක කිරීමෙන් තහවුරු කළ හැක:


```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```


![RLN](assets/fr/18.webp)


මෙන්න RGB සම්පත් රැගෙන යාමට වෙනස් කළ ලයිට්නින් නියමකය යොදවන්නේ කෙසේද යන්න. මෙම දර්ශනය පදනම්ව ඇත්තේ :




- regtest පරිසරයක් (`./regtest.sh` හරහා) හෝ Testnet ;
- `RGB-lightning-node` මිනිත්තුවක් `bitcoind` මත පදනම් වූ, දර්ශකයක් සහ `RGB-proxy-server` ;
- JSON REST API-jev za odpiranje/zapiranje kanalov, izdajo žetonov, prenos sredstev prek Lightninga itd.


මෙම ක්‍රියාවලියට ස්තුතියි :




- විදුලි ආකර්ෂණ ගනුදෙනු වල RGB මාරු කිරීමේ ඇන්කරින් සමඟ අමතර ප්‍රතිදානයක් (OP_RETURN හෝ Taproot) ඇතුළත් වේ;
- ස්ථාන මාරු සම්ප්‍රදායික Lightning ගෙවීම් මෙන්ම සම්පූර්ණයෙන්ම සමාන ආකාරයෙන් සිදු කෙරේ, නමුත් RGB ටෝකනයක් එක් කිරීමෙන්;
- බහු RLN නියමිතයන් සම්බන්ධ කර, බහු නියමිතයන් හරහා ගෙවීම් මාර්ගගත කිරීම සහ පරීක්ෂා කිරීම කළ හැක, මාර්ගයේ බිට්කොයින් සහ RGB වත්කම සඳහා ප්‍රමාණවත් ද්‍රවශීලතාවයක් තිබේ නම්.


ඔබට මෙම උපකාරිකාව ප්‍රයෝජනවත් වූවා නම්, පහත Green අඟුලක් දමන්නට මම ඉතාමත්ම කෘතඥ වෙමි. කරුණාකර මෙම ලිපිය ඔබේ සමාජ ජාලවල බෙදා ගැනීමට නිදහස් වන්න. ඉතාමත්ම ස්තූතියි!


මම මෙම වෙනත් උපකාරකයද නිර්දේශ කරමි, එහිදී මම RGB CLI මෙවලම භාවිතා කරන ආකාරය පැහැදිලි කරමි, LNP/BP සංගමය විසින් සංවර්ධනය කරන ලද RGB Contract එකක් නිර්මාණය කිරීමට:


https://planb.network/tutorials/node/others/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4