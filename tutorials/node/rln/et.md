---
name: RGB välgussõlm
description: Kuidas käivitada RGB-ühilduv Lightning-sõlme RLNiga?
---
![cover](assets/cover.webp)

Selles samm-sammult õpetuses saate teada, kuidas seadistada Lightning RGB-sõlme Regtest-keskkonnas. Näeme, kuidas luua RGB-märke ja neid kanalites levitada.

## RLN projekt

Bitfinexi RGB meeskond on alates 2022. aastast töötanud RGB ökosüsteemi rikastamise nimel, arendades välja täieliku tehnoloogilise korpuse. Selle asemel, et seada eesmärgiks üks kaubanduslik toode, on selle jõupingutused keskendunud avatud lähtekoodiga tarkvaratoodete kättesaadavaks tegemisele, RGB-protokolli spetsifikatsioonidele kaasa aitamisele ja rakendusviidete loomisele.

Bitfinexi märkimisväärne panus RGB-ökosüsteemi on [*RGBlib* raamatukogu](https://github.com/RGB-Tools/rgb-lib), mis on kirjutatud Rustis ja millele on juurdepääs Kotlini ja Pythoni sidemete kaudu, mis lihtsustab oluliselt RGB-rakenduste arendamist, kapseldades keerulised valideerimis- ja kaasamismehhanismid.

Bitfinexi meeskond on loonud ka RGB mobiilse rahakoti nimega "[*Iris Wallet*](https://iriswallet.com/)", mis on saadaval Androidis. See rahakott integreerib RGB proxy-serveri kasutamise, et hõlpsasti hallata ahelaväliseid andmevahetusi (*consignments*) *Client-side Validation* jaoks RGB-s.

Bitfinex on välja töötanud ka projekti `rgb-lightning-node` (RLN). See on Rusti deemon, mis põhineb `rust-lightning` (LDK) hargnemisel, mida on muudetud, et võtta arvesse RGB varade olemasolu kanalis. Kui kanal avatakse, saab RGB-märkide olemasolu määrata ja iga kord, kui kanali olekut uuendatakse, luuakse oleku üleminek, mis kajastab märkide jaotust Lightning-väljundites. See võimaldab :


- Avatud Lightning-kanalid USDT-s, näiteks;
- Suunata need märgid läbi võrgu, tingimusel, et marsruutimisradadel on piisavalt likviidsust;
- Kasutage Lightning'i karistus- ja ajalukustusloogikat ilma muudatusteta: lihtsalt kinnistage RGB-üleminek täiendavasse kohustustehingu väljundisse.

RLN-kood on veel alfa-staadiumis: soovitame seda kasutada ainult **regtestis** või **testnetis**.

## RGB-protokolli meeldetuletus

RGB on protokoll, mis töötab Bitcoini peal ning jäljendab nutika lepingu funktsionaalsust ja digitaalse vara haldamist, ilma et see koormaks selle aluseks olevat plokiahelat üle. Erinevalt tavapärastest ahelasisestest nutikontrahenditest (nagu näiteks Ethereumis) tugineb RGB "*kliendipoolse valideerimise*" süsteemile: enamikku andmeid ja olekuhinnanguid vahetavad ja salvestavad ainult asjaomased osalejad, samas kui Bitcoini plokiahelas on ainult väikesed krüptograafilised kohustused (selliste mehhanismide kaudu nagu *Tapret* või *Opret*). RGB-protokollis toimib Bitcoini plokiahel seega ainult ajamärgistamise serveri ja topeltkulutuste kaitsesüsteemina.

RGB leping on üles ehitatud nagu evolutsiooniline riigimasin. See algab Genesis'iga, mis määratleb algse seisundi (kirjeldab näiteks pakkumist, jooksevust või muid metaandmeid) vastavalt rangelt tüpiseeritud ja kompileeritud skeemile. Seejärel rakendatakse oleku üleminekuid ja vajaduse korral oleku laiendusi selle oleku muutmiseks või laiendamiseks. Iga operatsioon, olgu see siis asendatavate varade ülekandmine (RGB20) või unikaalsete varade loomine (RGB21), hõlmab *Kaheksakordseid pitsatite* kasutamist. Need seovad Bitcoini UTXOd ahelavälise olekuga ja hoiavad ära topeltkulutused, tagades samas konfidentsiaalsuse ja skaleeritavuse.

Kui soovite rohkem teada saada, kuidas RGB-protokoll töötab, soovitan teil läbida selle põhjaliku koolituskursuse:

https://planb.network/courses/csv402
## RGB-ühilduv Lightning-sõlme paigaldus

Selleks, et kompileerida ja installeerida `rgb-lightning-node` binaarsüsteemi, alustame repositooriumi ja selle alammoodulite kloonimisest, seejärel käivitame :

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RLN](assets/fr/01.webp)


- Valik `--recurse-submodules` kloonib ka vajalikud alamseadmed (sealhulgas modifitseeritud versiooni `rust-lightning`);
- Valik `--shallow-submodules` piirab kloonimise sügavust, et kiirendada allalaadimist, pakkudes samal ajal juurdepääsu olulistele kommittidele.

Projekti juurest käivitage järgmine käsk, et kompileerida ja paigaldada binaarsüsteem :

```bash
cargo install --locked --debug --path .
```

![RLN](assets/fr/02.webp)


- `--locked` tagab, et sõltuvuste versiooni järgitakse;
- `--debug` ei ole kohustuslik, kuid võib aidata teil keskenduda (võite kasutada `--release`, kui soovite) ;
- `--path .` ütleb `cargo install`ile, et ta installiks praegusest kataloogist.

Selle käsu lõpus on teie `$CARGO_HOME/bin/` käsureale `$CARGO_HOME/bin/` saadaval käivitatav `rgb-lightning-node`. Veenduge, et see tee on teie `$PATH`-s, et te saaksite käsku käivitada mis tahes kataloogist.

## Eeltingimused

Toimimiseks vajab deemon `rgb-lightning-node` olemasolu ja konfiguratsiooni :


- Sõlm `bitcoind`**

Iga RLNi instants peab suhtlema "bitcoindiga", et edastada ja jälgida oma ahelasisesed tehingud. Daemonile tuleb esitada autentimine (sisselogimine/parool) ja URL (host/port).


- Indekseerija** (Electrum või Esplora)

Deemon peab suutma loetleda ja uurida ahelas toimuvaid tehinguid, eelkõige leida UTXO, millele vara on ankurdatud. Peate määrama oma Electrumi serveri või Esplora URL-i.


- RGB** proxy

Proxy server on komponent (valikuline, kuid väga soovitatav), mis lihtsustab RGB *signaalide* vahetamist Lightning-partnerite vahel. Jällegi tuleb määrata URL.

ID-d ja URL-id sisestatakse, kui deemon on API kaudu *avatud*.

## Regtest käivitamine

Lihtsaks kasutamiseks on olemas skript `regtest.sh`, mis käivitab automaatselt Dockeri kaudu hulga teenuseid: `bitcoind`, `electrs` (indexer), `rgb-proxy-server`.

![RLN](assets/fr/03.webp)

See võimaldab teil käivitada kohaliku, isoleeritud, eelnevalt konfigureeritud keskkonna. See loob ja hävitab konteinerid ja andmekataloogid igal taaskäivitamisel. Alustame käivitamisega :

```bash
./regtest.sh start
```

See skript on :


- Looge kataloog `docker/`, et salvestada ;
- Käivitage regtestis `bitcoind`, samuti indekseerija `electrs` ja `rgb-proxy-server` ;
- Oodake, kuni kõik on kasutusvalmis.

![RLN](assets/fr/04.webp)

Järgnevalt käivitame mitu RLN-sõlme. Käivitage eraldi kestades näiteks (3 RLN-sõlme käivitamiseks) :

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


- Parameeter `--network regtest` näitab regtest-konfiguratsiooni kasutamist;
- `--daemon-listening-port` näitab, millises REST-portis Lightning-sõlm hakkab API-kõnesid (JSON) kuulama;
- `---ldk-peer-listening-port` määrab, millist Lightning p2p porti kuulata;
- `dataldk0/`, `dataldk1/` on salvestuskataloogide teekonnad (iga sõlmpunkt salvestab oma andmed eraldi).

Tänu API-le saate nüüd oma RLN-sõlmede käske täita oma brauserist. Eelkõige on see koht, kus saate *avada* deemonid. Lihtsalt avage brauser samas arvutis, kus on teie sõlmed, ja sisestage URL :

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

Selleks, et sõlm saaks avada kanali, peab tal kõigepealt olema bitcoine aadressil, mis on loodud järgmise käsuga (näiteks sõlme nr 1 jaoks):

```bash
curl -X POST http://localhost:3001/address
```

Vastus annab teile aadressi.

![RLN](assets/fr/06.webp)

"Bitcoind"-reeglites kaevandame mõned bitcoinid. Käivita :

```bash
./regtest.sh mine 101
```

![RLN](assets/fr/07.webp)

Saatke raha eespool loodud sõlme aadressile:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RLN](assets/fr/08.webp)

Seejärel kaevandage plokk tehingu kinnitamiseks:

```bash
./regtest.sh mine 1
```

![RLN](assets/fr/09.webp)

## Testneti käivitamine (ilma Dockerita)

Kui soovite testida realistlikumat stsenaariumi, võite käivitada RLN-sõlmede pigem Testnetis kui Regtestis, osutades avalikele teenustele või teie poolt kontrollitavatele teenustele:

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

Vaikimisi, kui konfiguratsiooni ei leita, proovib deemon kasutada :


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- "bitcoind_rpc_port": "18332"
- indexer_url`: `ssl://electrum.iriswallet.com:50013`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

Sisselogimisega :


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`

Neid elemente saab kohandada ka `init`/`unlock` API kaudu.

## RGB-märkide väljastamine

Tokeni väljastamiseks alustame "värvitavate" UTXOde loomisest:

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

Loomulikult saate järjekorda kohandada. Tehingu kinnitamiseks kaevandame :

```bash
./regtest.sh mine 1
```

Nüüd saame luua RGB vara. Käsk sõltub sellest, millist tüüpi vara soovite luua ja millised on selle parameetrid. Siinkohal loome NIA (*Non Inflatable Asset*) tokeni nimega "PBN", mille varu on 1000 ühikut. `precision` võimaldab teil määrata ühikute jagatavuse.

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

Vastus sisaldab äsja loodud vara ID-d. Ärge unustage seda identifikaatorit. Minu puhul on see :

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RLN](assets/fr/12.webp)

Seejärel saate selle üle kanda ahelas või eraldada selle Lightning-kanalis. Just seda teeme järgmises jaotises.

## Kanali avamine ja RGB-vara ülekandmine

Kõigepealt peate oma sõlme ühendama Lightning-võrgus oleva partneriga, kasutades käsku `/connectpeer`. Minu näites juhin ma mõlemat sõlme. Nii et ma hangin oma teise Lightning-sõlme avaliku võtme selle käsuga:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

Käsk tagastab minu sõlme nr 2 avaliku võtme:

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RLN](assets/fr/13.webp)

Järgmisena avame kanali, määrates vastava vara (`PBN`). Käsk `/openchannel` võimaldab määrata kanali suuruse satoshis ja valida, kas lisada RGB-vara. See sõltub sellest, mida soovite luua, kuid minu puhul on käsk :

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

Lisateavet leiate siit:


- `peer_pubkey_and_opt_addr`: Selle partneri identifikaator, kellega soovime ühendust luua (avalik võti, mille leidsime varem);
- `capacity_sat`: Kanali koguvõimsus satelliidides ;
- `push_msat`: Kogus millisatossides, mis kanali avamisel algselt partnerile edastatakse (siinkohal edastan kohe 10 000 sati, et ta saaks hiljem RGB ülekande teha) ;
- "varade summa": Kanalile pühendatavate RGB varade summa ;
- `asset_id` : kanaliga seotud RGB-vara unikaalne identifikaator;
- "avalik": Näitab, kas kanal peaks olema avalikustatud võrgus marsruutimiseks.

![RLN](assets/fr/14.webp)

Tehingu kinnitamiseks kaevandatakse 6 plokki:

```bash
./regtest.sh mine 6
```

![RLN](assets/fr/15.webp)

Lightning-kanal on nüüd avatud ja sisaldab ka 500 "PBN"-märki sõlme nr 1 poolel. Kui sõlm nr 2 soovib saada PBN-märke, peab ta looma arve. Seda saab teha järgmiselt:

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

Koos :


- `amt_msat`: Arve summa millisatoosides (vähemalt 3000 sats) ;
- `expiry_sec` : Arve aegumise aeg sekundites ;
- `asset_id` : arvega seotud RGB vara identifikaator ;
- "varade summa": Selle arvega ülekantava RGB vara summa.

Vastuseks saate RGB-arve:

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RLN](assets/fr/16.webp)

Nüüd maksame selle arve esimesest sõlmest, kus on vajalik raha "PBN" sümboliga:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RLN](assets/fr/17.webp)

Makse on tehtud. Seda saab kontrollida käsuga :

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RLN](assets/fr/18.webp)

Siin on kirjeldatud, kuidas võtta kasutusele Lightning-sõlm, mida on muudetud RGB-vara kandmiseks. See demonstratsioon põhineb :


- Regtest keskkond (läbi `./regtest.sh`) või testnet ;
- Lightning-sõlm (`rgb-lightning-node`), mis põhineb `bitcoind`il, indekseerijal ja `rgb-proxy-server`il;
- JSON REST APId kanalite avamiseks/sulgemiseks, märgiste väljastamiseks, varade ülekandmiseks Lightning'i kaudu jne.

Tänu sellele protsessile :


- Lightning engagement tehingud sisaldavad täiendavat väljundit (OP_RETURN või Taproot) koos RGB ülemineku ankurdamisega;
- Ülekandeid tehakse täpselt samamoodi nagu traditsioonilisi Lightning-makseid, kuid lisaks on lisatud RGB-märk;
- Mitut RLN-sõlme saab ühendada, et suunata ja katsetada makseid mitme sõlme vahel, tingimusel, et teel on piisavalt likviidsust nii bitcoinide kui ka vara RGB osas.

Kui leidsid selle õpetuse kasulikuks, oleksin väga tänulik, kui paneksid alla rohelise pöidla. Palun jagage seda artiklit julgelt oma sotsiaalvõrgustikes. Tänan teid väga!

Soovitan ka seda teist õpetust, kus ma selgitan, kuidas kasutada LNP/BP ühingu poolt välja töötatud RGB CLI tööriista RGB lepingu loomiseks:

https://planb.network/tutorials/node/rgb/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4