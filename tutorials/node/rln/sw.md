---
name: RGB Lightning Node
description: Je, ninawezaje kuzindua nodi ya Umeme inayoendana na RGB na RLN?
---
![cover](assets/cover.webp)


Katika mafunzo haya ya hatua kwa hatua, utajifunza jinsi ya kusanidi nodi ya Umeme ya RGB kwenye mazingira ya Regtest. Tutaona jinsi ya kuunda tokeni za RGB na kuzisambaza kwenye chaneli.


## Mradi wa RLN


Timu ya RGB ya Bitfinex imekuwa ikifanya kazi tangu 2022 ili kuimarisha mfumo ikolojia wa RGB kwa kutengeneza rundo kamili la teknolojia. Badala ya kulenga bidhaa moja ya kibiashara, juhudi zake zinalenga kufanya matofali ya programu huria kupatikana, kuchangia vipimo vya itifaki ya RGB na kuunda marejeleo ya utekelezaji.


Miongoni mwa michango mashuhuri ya Bitfinex kwa mfumo ikolojia wa RGB ni [maktaba ya *RGBlib*](https://github.com/RGB-Tools/RGB-lib), iliyoandikwa katika Rust na kufikiwa kupitia miunganisho katika Kotlin na Python, ambayo hurahisisha sana uundaji wa mifumo ya ujumuishaji ya RGB kwa ujumuishaji wa ujumuishaji.


Timu ya Bitfinex pia imeunda RGB ya simu ya mkononi ya Wallet, inayoitwa "[*Iris Wallet*](https://iriswallet.com/)", inayopatikana kwenye Android. Wallet hii inaunganisha matumizi ya seva mbadala ya RGB ili kudhibiti kwa urahisi ubadilishanaji wa data wa off-chain (*shehena*) ya *Client-side Validation* kwenye RGB.


Bitfinex pia imeanzisha mradi wa `RGB-lightning-node` (RLN). Hii ni Rust daemon kulingana na Fork ya `Rust-umeme` (LDK), iliyorekebishwa ili kuzingatia kuwepo kwa mali ya RGB katika chaneli. Wakati kituo kinafunguliwa, kuwepo kwa ishara za RGB kunaweza kutajwa, na kila wakati hali ya kituo inasasishwa, State Transition inaundwa ambayo inaonyesha usambazaji wa ishara katika matokeo ya Umeme. Hii inawezesha:




- Fungua njia za umeme katika USDT, kwa mfano;
- Elekeza tokeni hizi kupitia mtandao, mradi tu njia za uelekezaji ziwe na ukwasi wa kutosha;
- Tumia adhabu ya Umeme na mantiki ya kufunga saa bila marekebisho: kwa urahisi Anchor mpito wa RGB katika matokeo ya ziada ya Commitment Transaction.


Msimbo wa RLN bado uko katika hatua yake ya alpha: tunapendekeza uitumie katika **regtest** au kwenye **Testnet** pekee.


## Kikumbusho cha itifaki ya RGB


RGB ni itifaki inayoendesha juu ya Bitcoin na kuiga utendaji wa Smart contract na usimamizi wa mali dijitali, bila kupakia Blockchain ambayo msingi wake ni. Tofauti na mikataba mahiri ya On-Chain ya kawaida (kama ilivyo kwa Ethereum, kwa mfano), RGB inategemea mfumo wa "*Client-side Validation*": data na historia nyingi za hali hubadilishwa na kuhifadhiwa na washiriki wanaohusika pekee, ilhali Bitcoin Blockchain huandaa tu ahadi ndogo za kriptografia (kupitia mbinu kama vile *OTapret*). Katika itifaki ya RGB, Bitcoin Blockchain kwa hivyo hutumika tu kama seva ya kukanyaga wakati na mfumo wa ulinzi wa Double-spending.


RGB Contract imeundwa kama mashine ya hali ya mabadiliko. Huanza na Genesis inayofafanua hali ya awali (inayoelezea, kwa mfano, Supply, ticker au metadata nyingine) kulingana na Schema iliyochapwa kwa ukali na iliyokusanywa. Mpito wa Jimbo na, ikihitajika, Viendelezi vya Jimbo basi hutumika kurekebisha au kupanua hali hii. Kila operesheni, iwe ni kuhamisha vipengee vinavyoweza kuvutwa (RGB20) au kuunda vipengee vya kipekee (RGB21), huhusisha *Mihuri ya Matumizi Moja*. Hizi huunganisha Bitcoin UTXOs kwenye majimbo ya off-chain na kuzuia matumizi maradufu, huku zikihakikisha usiri na hatari.


Ili kujifunza zaidi kuhusu jinsi itifaki ya RGB inavyofanya kazi, ninapendekeza uchukue kozi hii ya kina ya mafunzo:


https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

## Ufungaji wa nodi ya umeme inayoendana na RGB


Kukusanya na kusakinisha binary `RGB-umeme-nodi`, tunaanza kwa kutengeneza hazina na moduli zake ndogo, kisha tunaendesha :


```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```


![RLN](assets/fr/01.webp)




- Chaguo la `--recurse-submodules` pia huiga vifaa vidogo vinavyohitajika (pamoja na toleo lililobadilishwa la `Rust-umeme`);
- Chaguo la `--shallow-submodules` huzuia kina cha clone ili kuharakisha upakuaji, huku ikiendelea kutoa ufikiaji wa ahadi muhimu.


Kutoka kwa mzizi wa mradi, endesha amri ifuatayo ya kuunda na kusakinisha binary :


```bash
cargo install --locked --debug --path .
```


![RLN](assets/fr/02.webp)




- `--imefungwa` inahakikisha kwamba toleo la vitegemezi linaheshimiwa;
- `--debug` si lazima, lakini inaweza kukusaidia kuzingatia (unaweza kutumia `--release` ukipenda);
- `--path .` inaambia `cargo install` kusakinisha kutoka kwenye saraka ya sasa.


Mwishoni mwa amri hii, `RGB-nodi-umeme` inayoweza kutekelezeka itapatikana katika `$CARGO_HOME/bin/` yako. Hakikisha njia hii iko kwenye `$PATH` yako ili uweze kuomba amri kutoka kwa saraka yoyote.


## Masharti


Ili kufanya kazi, nodi ya `RGB-umeme` daemon inahitaji uwepo na usanidi wa :




- Nodi ya `bitcoind`


Kila mfano wa RLN utahitaji kuwasiliana na `bitcoind` ili kutangaza na kufuatilia miamala yake ya On-Chain. Uthibitishaji (kuingia/nenosiri) na URL (mwenyeji/mlango) utahitaji kutolewa kwa daemon.




- **Kielelezo** (Electrum au Esplora)


daemon lazima iweze kuorodhesha na kuchunguza miamala ya On-Chain, hasa kupata UTXO ambayo mali imewekewa nanga. Utahitaji kubainisha URL ya seva yako ya Electrum au Esplora.




- **Wakala wa RGB**


Seva ya proksi ni sehemu (ya hiari, lakini inapendekezwa sana) ili kurahisisha Exchange ya RGB *shehena* kati ya programu zingine za Lightning. Kwa mara nyingine tena, ni lazima URL ibainishwe.


Vitambulisho na URL huwekwa wakati daemon *imefunguliwa* kupitia API.


## Uzinduzi wa regt


Kwa matumizi rahisi, kuna hati `regtest.sh` ambayo huanza kiotomatiki, kupitia Docker, seti ya huduma: `bitcoind`, `electrs` (indexer), `RGB-proxy-server`.


![RLN](assets/fr/03.webp)


Hii hukuruhusu kuzindua mazingira ya ndani, ya pekee, yaliyosanidiwa mapema. Inaunda na kuharibu vyombo na saraka za data kwenye kila kuwasha upya. Tutaanza kwa kuanzisha:


```bash
./regtest.sh start
```


Hati hii itakuwa:




- Unda saraka ya `docker/` kuhifadhi;
- Endesha `bitcoind` kwa regtest, pamoja na kiashiria `electrs` na `RGB-proxy-server` ;
- Subiri hadi kila kitu kiko tayari kutumika.


![RLN](assets/fr/04.webp)


Ifuatayo, tutazindua nodi kadhaa za RLN. Katika ganda tofauti, endesha, kwa mfano (kuzindua nodi 3 za RLN) :


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




- Kigezo cha `--network regtest` kinaonyesha matumizi ya usanidi wa regtest;
- `--daemon-kusikiliza-bandari` inaonyesha ni kwenye mlango gani wa REST ambapo nodi ya Umeme itasikiliza kwa simu za API (JSON);
- `--ldk-peer-listening-port` inabainisha ni mlango gani wa Umeme wa P2P wa kusikiliza;
- `dataldk0/`, `dataldk1/` ni njia za saraka za hifadhi (kila nodi huhifadhi maelezo yake kivyake).


Sasa unaweza kutekeleza maagizo kwenye nodi zako za RLN kutoka kwa kivinjari chako, shukrani kwa API. Hasa, hapa ndipo unaweza *kufungua* damoni. Fungua tu kivinjari kwenye kompyuta sawa na nodi zako, na uweke URL :


```url
https://rgb-tools.github.io/rgb-lightning-node/
```


Ili nodi ifungue chaneli, lazima kwanza iwe na bitcoins kwenye Address inayotokana na amri ifuatayo (kwa nodi n ° 1, kwa mfano):


```bash
curl -X POST http://localhost:3001/address
```


Jibu litakupa Address.


![RLN](assets/fr/06.webp)


Kwenye Regtest ya `bitcoind`, tutachimba bitcoins chache. Endesha:


```bash
./regtest.sh mine 101
```


![RLN](assets/fr/07.webp)


Tuma pesa kwa nodi ya Address iliyozalishwa hapo juu:


```bash
./regtest.sh sendtoaddress <address> <amount>
```


![RLN](assets/fr/08.webp)


Kisha piga block ili kudhibitisha shughuli:


```bash
./regtest.sh mine 1
```


![RLN](assets/fr/09.webp)


## Uzinduzi wa Testnet (bila Docker)


Ikiwa unataka kujaribu hali halisi zaidi, unaweza kuzindua nodi za RLN kwenye Testnet badala ya Regtest, ukielekeza kwenye huduma za umma, au huduma unazodhibiti:


```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```


Kwa chaguo-msingi, ikiwa hakuna usanidi unaopatikana, daemon itajaribu kutumia :




- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-RPC`


Kwa kuingia:




- `bitcoind_rpc_jina_la_mtumiaji`: `mtumiaji`
- `bitcoind_rpc_jina_la_mtumiaji`: `nenosiri`


Unaweza pia kubinafsisha Elements hizi kupitia `init`/`fungua` API.


## Kutoa tokeni ya RGB


Ili kutoa ishara, tutaanza kwa kuunda UTXO "za rangi":


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


Unaweza, bila shaka, kurekebisha utaratibu. Ili kuthibitisha muamala, tunachimba:


```bash
./regtest.sh mine 1
```


Sasa tunaweza kuunda kipengee cha RGB. Amri itategemea aina ya mali unayotaka kuunda na vigezo vyake. Hapa ninaunda tokeni ya NIA (*Non Inflatable Asset*) inayoitwa "PBN" yenye Supply ya vitengo 1000. `usahihi` hukuruhusu kufafanua mgawanyiko wa vitengo.


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


Jibu linajumuisha kitambulisho cha kipengee kipya kilichoundwa. Kumbuka kutambua kitambulisho hiki. Katika kesi yangu, ni:


```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```


![RLN](assets/fr/12.webp)


Kisha unaweza kuihamisha On-Chain, au kuitenga katika kituo cha Umeme. Hivyo ndivyo tutakavyofanya katika sehemu inayofuata.


## Kufungua kituo na kuhamisha mali ya RGB


Lazima kwanza uunganishe nodi yako kwa rika kwenye Lightning Network kwa kutumia `/connectpeer` amri. Katika mfano wangu, ninadhibiti nodi zote mbili. Kwa hivyo nitapata ufunguo wa umma wa nodi yangu ya pili ya Umeme na amri hii:


```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```


Amri inarudisha ufunguo wa umma wa nodi yangu n°2 :


```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```


![RLN](assets/fr/13.webp)


Kisha, tutafungua kituo kwa kubainisha kipengee husika (`PBN`). Amri ya `/openchannel` hukuruhusu kufafanua ukubwa wa kituo katika satoshis na uchague kujumuisha kipengee cha RGB. Inategemea kile unachotaka kuunda, lakini kwa upande wangu, amri ni:


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


Pata maelezo zaidi hapa:




- `peer_pubkey_and_opt_addr`: Kitambulisho cha programu rika tunayotaka kuunganisha kwake (ufunguo wa umma tuliopata hapo awali);
- `capacity_sat`: Jumla ya uwezo wa chaneli katika satoshi;
- `push_msat`: Kiasi katika millisatoshis kilichohamishwa awali kwa rika wakati kituo kinafunguliwa (hapa mara moja ninahamisha 10,000 Sats ili aweze kufanya uhamisho wa RGB baadaye);
- `kiasi_cha_mali`: Kiasi cha mali za RGB kitakachowekwa kwenye kituo ;
- `asset_id` : Kitambulisho cha kipekee cha kipengee cha RGB kinachohusika katika kituo;
- `umma`: Inaonyesha kama kituo kinapaswa kuwekwa hadharani kwa kuelekeza kwenye mtandao.


![RLN](assets/fr/14.webp)


Ili kudhibitisha shughuli hiyo, vitalu 6 vinachimbwa:


```bash
./regtest.sh mine 6
```


![RLN](assets/fr/15.webp)


Kituo cha Umeme sasa kimefunguliwa na pia kina tokeni 500 za `PBN` kwenye upande wa nodi n°1. Ikiwa nodi n°2 inataka kupokea tokeni za `PBN`, ni lazima generate iwe Invoice. Hapa ni jinsi ya kufanya hivyo:


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


Na:




- `amt_msat`: Kiasi cha Invoice katika millisatoshis (kiwango cha chini 3000 Sats);
- `expiry_sec` : muda wa kuisha kwa Invoice kwa sekunde ;
- `asset_id` : Kitambulisho cha kipengee cha RGB kinachohusishwa na Invoice ;
- `asset_amount`: Kiasi cha mali ya RGB kitakachohamishwa kwa Invoice hii.


Kwa kujibu, utapata RGB Invoice:


```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```


![RLN](assets/fr/16.webp)


Sasa tutalipa Invoice hii kutoka nodi ya kwanza, ambayo inashikilia pesa taslimu zinazohitajika kwa ishara `PBN`:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```


![RLN](assets/fr/17.webp)


Malipo yamefanywa. Hii inaweza kuthibitishwa kwa kutekeleza amri:


```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```


![RLN](assets/fr/18.webp)


Hivi ndivyo jinsi ya kupeleka nodi ya Umeme iliyorekebishwa ili kubeba vipengee vya RGB. Maonyesho haya yanatokana na:




- Mazingira ya regtest (kupitia `./regtest.sh`) au Testnet ;
- Nodi ya Umeme (`RGB-nodi-umeme`) kulingana na `bitcoind`, faharasa na `seva-badala ya RGB` ;
- Msururu wa API za JSON REST za kufungua/kufunga chaneli, kutoa tokeni, kuhamisha mali kupitia Umeme, n.k.


Shukrani kwa mchakato huu:




- Shughuli za ushiriki wa umeme ni pamoja na pato la ziada (OP_RETURN au Taproot) kwa kuunga mkono mpito wa RGB;
- Uhamisho unafanywa kwa njia sawa kabisa na malipo ya jadi ya Umeme, lakini kwa kuongeza ishara ya RGB;
- Nodi nyingi za RLN zinaweza kuunganishwa kwenye njia na kufanya majaribio ya malipo kwenye nodi nyingi, mradi tu kuna ukwasi wa kutosha katika bitcoins na mali ya RGB kwenye njia.


Ikiwa umepata mafunzo haya kuwa ya manufaa, ningeshukuru sana ukiweka kidole gumba cha Green hapa chini. Tafadhali jisikie huru kushiriki nakala hii kwenye mitandao yako ya kijamii. Asante sana!


Pia ninapendekeza somo hili lingine ambalo ninaeleza jinsi ya kutumia zana ya RGB CLI iliyotengenezwa na chama cha LNP/BP kuunda RGB Contract:


https://planb.network/tutorials/node/others/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4