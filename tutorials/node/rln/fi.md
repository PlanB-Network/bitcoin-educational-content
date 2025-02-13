---
name: RGB-salamasolmu
description: Miten käynnistän RGB-yhteensopivan Lightning-solmun RLN:llä?
---
![cover](assets/cover.webp)

Tässä vaiheittaisessa ohjeessa opit, miten Lightning RGB -solmu asetetaan Regtest-ympäristöön. Näemme, miten luodaan RGB-tunnuksia ja kierrätetään niitä kanavissa.

## RLN-hanke

Bitfinexin RGB-tiimi on työskennellyt vuodesta 2022 lähtien rikastuttaakseen RGB-ekosysteemiä kehittämällä täydellisen teknologiapinon. Yksittäisen kaupallisen tuotteen tavoittelun sijaan sen ponnistelut keskittyvät avoimen lähdekoodin ohjelmistotiilien saataville asettamiseen, RGB-protokollan määrittelyihin osallistumiseen ja toteutusreferenssien luomiseen.

Bitfinexin merkittävä panos RGB-ekosysteemiin on [*RGBlib*-kirjasto](https://github.com/RGB-Tools/rgb-lib), joka on kirjoitettu Rust-kielellä ja jota voidaan käyttää Kotlin- ja Python-kielisten sidosten kautta. Se yksinkertaistaa huomattavasti RGB-sovellusten kehittämistä kapseloimalla monimutkaiset validointi- ja sitoutumismekanismit.

Bitfinexin tiimi on myös suunnitellut RGB-mobiililompakon nimeltä "[*Iris Wallet*](https://iriswallet.com/)", joka on saatavilla Androidissa. Tähän lompakkoon on integroitu RGB-välityspalvelimen käyttö, jonka avulla voidaan helposti hallita ketjun ulkopuolisia tietojenvaihtoja (*lähetyksiä*) *Client-side Validation* varten RGB:ssä.

Bitfinex on myös kehittänyt `rgb-lightning-node` (RLN) -projektin. Kyseessä on Rust-demoni, joka perustuu `rust-lightning`:n (LDK) haarautumiseen ja jota on muokattu siten, että se ottaa huomioon RGB-varojen olemassaolon kanavassa. Kun kanava avataan, voidaan määrittää RGB-tunnisteiden olemassaolo, ja aina kun kanavan tila päivitetään, luodaan tilasiirtymä, joka heijastaa tunnisteiden jakautumista Lightning-ulostuloissa. Tämä mahdollistaa :


- Avaa Lightning-kanavat esimerkiksi USDT:ssä;
- Reititä nämä rahakkeet verkon kautta edellyttäen, että reitityspoluilla on riittävästi likviditeettiä;
- Hyödynnä Lightningin rangaistus- ja timelock-logiikkaa ilman muutoksia: ankkuroi RGB-siirtymä yksinkertaisesti sitoumustapahtuman ylimääräiseen ulostuloon.

RLN-koodi on vielä alfa-vaiheessa: suosittelemme sen käyttöä vain **regtestissä** tai **testnetissä**.

## RGB-protokollan muistutus

RGB on protokolla, joka toimii Bitcoinin päällä ja jäljittelee älykkäiden sopimusten toimintoja ja digitaalisten omaisuuserien hallintaa kuormittamatta liikaa lohkoketjua, johon se perustuu. Toisin kuin perinteiset ketjussa olevat älykkäät sopimukset (kuten esimerkiksi Ethereumissa), RGB perustuu "*Client-side validation*" -järjestelmään: suurin osa tiedoista ja tilahistoriasta vaihdetaan ja tallennetaan yksinomaan osallistujien kesken, kun taas Bitcoinin lohkoketjussa on vain pieniä kryptografisia sitoumuksia (esimerkiksi *Tapretin* tai *Opretin* kaltaisten mekanismien avulla). RGB-protokollassa Bitcoin-lohkoketju toimii näin ollen vain aikaleimauspalvelimena ja kaksinkertaisen kulutuksen suojausjärjestelmänä.

RGB-sopimus on rakenteeltaan kuin evolutiivinen tilakone. Se alkaa Genesiksellä, jossa määritellään alkutila (jossa kuvataan esimerkiksi tarjonta, ticker tai muut metatiedot) tiukasti tyypitetyn ja kootun skeeman mukaisesti. Tämän jälkeen sovelletaan tilasiirtymiä ja tarvittaessa tilalaajennuksia tämän tilan muuttamiseksi tai laajentamiseksi. Jokaiseen operaatioon, olipa kyse sitten vaihdettavissa olevien omaisuuserien siirtämisestä (RGB20) tai ainutlaatuisten omaisuuserien luomisesta (RGB21), liittyy *Kertakäyttösinettejä*. Nämä yhdistävät Bitcoin UTXO:t ketjun ulkopuolisiin tiloihin ja estävät kaksinkertaisen kulutuksen varmistaen samalla luottamuksellisuuden ja skaalautuvuuden.

Jos haluat lisätietoja RGB-protokollan toiminnasta, suosittelen, että osallistut tälle kattavalle koulutuskurssille:

https://planb.network/courses/csv402
## RGB-yhteensopiva Lightning-solmun asennus

Kääntääksemme ja asentaaksemme `rgb-lightning-node`-binäärin aloitamme kloonaamalla arkiston ja sen alamoduulit, sitten ajamme :

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RLN](assets/fr/01.webp)


- Vaihtoehto `--recurse-submodules` kloonaa myös tarvittavat alalaitteet (mukaan lukien muunnetun version `rust-lightning`:sta);
- Valinta `--shallow-submodules` rajoittaa kloonin syvyyttä latauksen nopeuttamiseksi, mutta tarjoaa silti pääsyn tärkeimpiin komituksiin.

Suorita projektin juuresta seuraava komento kääntääksesi ja asentaaksesi binäärin :

```bash
cargo install --locked --debug --path .
```

![RLN](assets/fr/02.webp)


- `--locked` varmistaa, että riippuvuuksien versiota noudatetaan;
- `--debug` ei ole pakollinen, mutta se voi auttaa sinua keskittymään (voit käyttää `--release` jos haluat) ;
- `--polku .` käskee `cargo install` asentamaan nykyisestä hakemistosta.

Tämän komennon jälkeen `rgb-lightning-node` on käytettävissäsi `$CARGO_HOME/bin/`-tietokannassasi. Varmista, että tämä polku on `$PATH` -hakemistossasi, jotta voit kutsua komennon mistä tahansa hakemistosta.

## Edellytykset

Toimiakseen `rgb-lightning-node` -demoni tarvitsee :


- `bitcoind`**-solmu

Jokaisen RLN-instanssin on kommunikoitava `bitcoind`:n kanssa, jotta se voi lähettää ja seurata ketjussa tapahtuvia transaktioitaan. Demonille on annettava tunnistautuminen (käyttäjätunnus/salasana) ja URL-osoite (host/portti).


- Indeksilaite** (Electrum tai Esplora)

Daemonilla on voitava luetella ja tutkia ketjussa tapahtuvia transaktioita ja erityisesti löytää UTXO, johon omaisuuserä on ankkuroitu. Sinun on määritettävä Electrum-palvelimesi tai Esploran URL-osoite.


- RGB**-välityspalvelin

Välityspalvelin on komponentti (valinnainen, mutta erittäin suositeltava), joka yksinkertaistaa RGB-luokitusten vaihtoa Lightning-vertaisverkon välillä. Jälleen kerran URL-osoite on määritettävä.

Tunnukset ja URL-osoitteet syötetään, kun palvelimen lukitus *avautetaan* API:n kautta.

## Regtestin käynnistäminen

Yksinkertaista käyttöä varten on olemassa `regtest.sh`-skripti, joka käynnistää automaattisesti Dockerin kautta joukon palveluita: `Bitcoind`, `electrs` (indeksoija), `rgb-proxy-server`.

![RLN](assets/fr/03.webp)

Näin voit käynnistää paikallisen, eristetyn, valmiiksi konfiguroidun ympäristön. Se luo ja tuhoaa kontit ja datahakemistot jokaisen uudelleenkäynnistyksen yhteydessä. Aloitamme käynnistämällä :

```bash
./regtest.sh start
```

Tämä skripti :


- Luo `docker/`-hakemisto tallentamaan ;
- Suorita `bitcoind` regtestissä, samoin kuin indeksoija `electrs` ja `rgb-proxy-server` ;
- Odota, kunnes kaikki on valmista.

![RLN](assets/fr/04.webp)

Seuraavaksi käynnistämme useita RLN-solmuja. Suorita erillisissä kuorissa esimerkiksi (käynnistääksesi 3 RLN-solmua) :

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


- Parametri `--network regtest` ilmaisee regtest-konfiguraation käytön;
- `--daemon-listening-port` osoittaa, mitä REST-porttia Lightning-solmu kuuntelee API-kutsuja (JSON);
- `----ldk-peer-listening-port` määrittää, mitä Lightning p2p-porttia kuunnellaan;
- `dataldk0/`, `dataldk1/` ovat polut tallennushakemistoihin (kukin solmu tallentaa tietonsa erikseen).

Voit nyt suorittaa komentoja RLN-solmuissasi selaimesta API:n ansiosta. Täällä voit erityisesti *avata* daemonien lukituksen. Avaa vain selain samalla tietokoneella kuin solmusi ja syötä URL-osoite :

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

Jotta solmu voi avata kanavan, sillä on ensin oltava bitcoineja osoitteessa, joka on luotu seuraavalla komennolla (esimerkiksi solmulle nro 1):

```bash
curl -X POST http://localhost:3001/address
```

Vastauksesta saat osoitteen.

![RLN](assets/fr/06.webp)

`bitcoind`-testissä louhimme muutaman bitcoinin. Suorita :

```bash
./regtest.sh mine 101
```

![RLN](assets/fr/07.webp)

Lähetä varat edellä luotuun solmuosoitteeseen:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RLN](assets/fr/08.webp)

Sen jälkeen louhi lohko vahvistamaan transaktio:

```bash
./regtest.sh mine 1
```

![RLN](assets/fr/09.webp)

## Testnetin käynnistäminen (ilman Dockeria)

Jos haluat testata realistisempaa skenaariota, voit käynnistää RLN-solmuja Regtestin sijasta Testnetissä osoittamalla julkisiin palveluihin tai hallitsemiinne palveluihin:

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

Oletusarvoisesti, jos konfiguraatiota ei löydy, daemon yrittää käyttää :


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

Kirjautumalla sisään :


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `salasana`

Voit myös muokata näitä elementtejä `init`/`unlock` API:n kautta.

## RGB-tunnisteen antaminen

Merkin antaminen aloitetaan luomalla "väritettäviä" UTXO:ita:

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

Voit tietenkin mukauttaa järjestystä. Vahvistaaksemme tapahtuman, me kaivamme :

```bash
./regtest.sh mine 1
```

Voimme nyt luoda RGB-varannon. Komento riippuu siitä, minkä tyyppisen assetin haluat luoda ja sen parametreista. Tässä luon NIA-merkin (*Non Inflatable Asset*) nimeltä "PBN", jonka tarjonta on 1000 yksikköä. `precision`:n avulla voit määrittää yksiköiden jaettavuuden.

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

Vastaus sisältää äskettäin luodun omaisuuserän ID:n. Muista merkitä tämä tunniste muistiin. Minun tapauksessani se on :

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RLN](assets/fr/12.webp)

Voit sitten siirtää sen ketjussa tai jakaa sen Lightning-kanavassa. Juuri näin teemme seuraavassa osiossa.

## Kanavan avaaminen ja RGB-varannon siirtäminen

Sinun on ensin yhdistettävä solmusi Lightning-verkon vertaisverkkoon komennolla `/connectpeer`. Esimerkissäni hallitsen molempia solmuja. Haen siis toisen Lightning-solmuni julkisen avaimen tällä komennolla:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

Komento palauttaa solmuni nro 2 julkisen avaimen:

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RLN](assets/fr/13.webp)

Seuraavaksi avaamme kanavan määrittämällä kyseisen omaisuuserän (`PBN`). `/openchannel`-komennolla voit määrittää kanavan koon satoshina ja valita, otatko mukaan RGB-varannon. Se riippuu siitä, mitä haluat luoda, mutta minun tapauksessani komento on :

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

Lue lisää täältä:


- `peer_pubkey_and_opt_addr`: Sen vertaisverkon tunniste, johon haluamme muodostaa yhteyden (julkinen avain, jonka löysimme aiemmin);
- `capacity_sat`: Kanavan kokonaiskapasiteetti satelliitteina ;
- `push_msat`: 
- `asset_amount`: Kanavalle sidottavien RGB-varojen määrä ;
- `asset_id` : Kanavaan osallistuvan RGB-varannon yksilöllinen tunniste;
- `julkinen`: '```: Ilmaisee, onko kanavasta tehtävä julkinen verkossa tapahtuvaa reititystä varten.

![RLN](assets/fr/14.webp)

Tapahtuman vahvistamiseksi louhitaan 6 lohkoa:

```bash
./regtest.sh mine 6
```

![RLN](assets/fr/15.webp)

Lightning-kanava on nyt auki, ja se sisältää myös 500 `PBN`-tunnusta solmun nro 1 puolella. Jos solmu nro 2 haluaa vastaanottaa `PBN`-tunnuksia, sen on luotava lasku. Näin se tehdään:

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

Kanssa :


- `amt_msat`: Laskun määrä millisatoseina (vähintään 3000 satsia) ;
- `expiry_sec` : Laskun voimassaoloaika sekunteina ;
- `asset_id` : Laskuun liittyvän RGB-varan tunniste ;
- `asset_amount`: Tällä laskulla siirrettävän RGB-varan määrä.

Vastauksena saat RGB-laskun:

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RLN](assets/fr/16.webp)

Maksamme nyt tämän laskun ensimmäisestä solmusta, jossa on tarvittava käteisvaratunnus "PBN":

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RLN](assets/fr/17.webp)

Maksu on suoritettu. Tämä voidaan tarkistaa suorittamalla komento :

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RLN](assets/fr/18.webp)

Näin otat käyttöön Lightning-solmun, joka on muutettu kuljettamaan RGB-varoja. Tämä esittely perustuu :


- Regtest-ympäristö (kautta `./regtest.sh`) tai testnet ;
- Lightning-solmu (`rgb-lightning-node`), joka perustuu `bitcoind`-, indeksointi- ja `rgb-proxy-palvelimeen`;
- Joukko JSON REST -rajapintoja kanavien avaamiseen/sulkemiseen, tunnisteiden myöntämiseen, varojen siirtämiseen Lightningin kautta jne.

Tämän prosessin ansiosta :


- Lightning engagement -tapahtumat sisältävät ylimääräisen ulostulon (OP_RETURN tai Taproot), jossa on RGB-siirtymän ankkurointi;
- Siirrot tehdään täsmälleen samalla tavalla kuin perinteiset Lightning-maksut, mutta niihin lisätään RGB-token;
- Useita RLN-solmuja voidaan yhdistää reitittämään ja kokeilemaan maksuja useiden solmujen välillä edellyttäen, että reitillä on riittävästi likviditeettiä sekä bitcoineina että omaisuuseränä RGB.

Jos löysit tämän ohjeen hyödylliseksi, olisin hyvin kiitollinen, jos laittaisit vihreän peukalon alle. Voit vapaasti jakaa tämän artikkelin sosiaalisissa verkostoissa. Kiitos paljon!

Suosittelen myös tätä toista opetusohjelmaa, jossa selitän, miten LNP/BP-yhdistyksen kehittämää RGB CLI -työkalua käytetään RGB-sopimuksen luomiseen:

https://planb.network/tutorials/node/rgb/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4