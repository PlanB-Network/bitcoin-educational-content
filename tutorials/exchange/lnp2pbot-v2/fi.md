---
name: LNP2PBot
description: Täydellinen opas LNP2PBot ja P2P Bitcoin kaupankäynnin
---
![cover](assets/cover.webp)

## Johdanto

KYC-vapaat P2P-pörssit ovat olennaisen tärkeitä käyttäjien luottamuksellisuuden ja taloudellisen riippumattomuuden säilyttämiseksi. Ne mahdollistavat suorat transaktiot yksityishenkilöiden välillä ilman henkilöllisyyden todentamista, mikä on ratkaisevan tärkeää yksityisyyttä arvostaville. Jos haluat syvällisemmän käsityksen teoreettisista käsitteistä, tutustu BTC204-kurssiin:

https://planb.network/courses/btc204
Bitcoinien ostaminen ja myyminen vertaisverkossa (P2P) on yksi yksityisimmistä tavoista hankkia tai luovuttaa bitcoineja. LNP2PBot on avoimen lähdekoodin Telegram-botti, joka helpottaa P2P-vaihtoja Lightning-verkossa ja mahdollistaa nopeat, edulliset ja KYC-vapaat transaktiot.

### Miksi käyttää Lnp2pbotia?


- KYC ei vaadita
- Nopeat transaktiot Lightning-verkossa
- Alhaiset kustannukset
- Yksinkertainen käyttöliittymä Telegramin kautta, joka on suosittu viestisovellus, jota voi käyttää mistä tahansa päin maailmaa
- Integroitu mainejärjestelmä
- Automaattinen escrow turvalliseen kaupankäyntiin
- Monivaluuttatuki
- Aktiivinen ja kasvava yhteisö

### Edellytykset

Jotta voit käyttää Lnp2pbotia, tarvitset :

1. Lightning Network -lompakko (Breez, Phoenix tai Blixt suositeltava)

2. Telegram-sovellus asennettu (https://telegram.org/)

3. Telegram-tili, jolla on määritelty käyttäjätunnus

## Asennus ja konfigurointi

### 1. Lightning-lompakon määrittäminen

Aloita asentamalla yhteensopiva Lightning-lompakko. Tässä ovat yksityiskohtaiset suosituksemme:

**Suositellut salkut**


- [Breez](https://breez.technology)**:
  - Erinomainen aloittelijoille
  - Intuitiivinen, moderni käyttöliittymä
  - Ei-puolustajuus (säilytät varojen hallinnan)
  - Täysin yhteensopiva Lnp2pbotin kanssa
  - Saatavilla iOS:ssä ja Androidissa

Alla on linkki tämän lompakon ohjeeseen:

https://planb.network/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06

- [Phoenix](https://phoenix.acinq.co)** :
  - Yksinkertainen ja luotettava
  - Automaattinen kanavakonfigurointi
  - Natiivituki BOLT11-laskuille
  - Erinomainen jokapäiväisiin liiketoimiin
  - Saatavilla iOS:ssä ja Androidissa

Alla on linkki tämän lompakon ohjeeseen:

https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

- [Blixt](https://blixtwallet.github.io)** :
  - Teknisempi, mutta erittäin täydellinen
  - Laajennetut konfigurointivaihtoehdot
  - Täydellinen kokeneille käyttäjille
  - Avoin lähdekoodi
  - Saatavana Androidissa

Alla on linkki tämän lompakon ohjeeseen:

https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f
**Tärkeitä huomautuksia muista salkuista**

⚠️ **Tärkeää**: Varmista ennen satsin myyntiä, että salkkusi tukee "hold"-laskuja, joita botti käyttää escrow-järjestelmänä.


- Satoshin lompakko**: Toimii hyvin satsin vastaanottamiseen, mutta saldon päivittäminen voi viivästyä, jos myynti peruutetaan.
- Muun**: Ei suositella, koska maksut voivat epäonnistua bottien reititysmaksurajoitusten vuoksi (enintään 0,2 %).
- Aqua**: Toimii satelliittien vastaanottamiseen, mutta saldopäivitykset voivat viivästyä (jopa 48 tuntia), jos myynti peruutetaan.

💡 **Vinkki**: Valitse suositellut salkut (Breez, Phoenix tai Blixt) optimaalisen kokemuksen saamiseksi.

⚠️ **Tärkeää**: Älä unohda tallentaa palautuslauseita turvalliseen paikkaan.

### 2. Aloittaminen Lnp2pbotin kanssa

1. Klikkaa tätä linkkiä päästäksesi bottiin: [@lnp2pBot](https://t.me/lnp2pbot)

2. Telegram avautuu automaattisesti

3. Napsauta "Start" tai lähetä komento "/start"

4. Botti pyytää sinua luomaan käyttäjätunnuksen, jos sinulla ei vielä ole sellaista

5. Botti opastaa sinut alkukonfiguroinnin läpi

### 3. Liity yhteisöön


- Liity pääkanavalle: [@p2plightning](https://t.me/p2plightning)
- Tuki: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)

## Bitcoinien ostaminen ja myyminen

On olemassa kaksi pääasiallista tapaa vaihtaa bitcoineja Lnp2pbotissa:

1. Selaa markkinoilla olevia tarjouksia ja vastaa niihin

2. Luo oma osto- tai myyntitarjous

Tässä oppaassa tarkastelemme yksityiskohtaisesti, miten :


- Osta bitcoineja olemassa olevasta tarjouksesta
- Myy bitcoineja luomalla oman tarjouksen

### Miten ostaa Bitcoineja

**1. Etsi ja valitse tarjous**

![Sélection d'une offre de vente](assets/fr/01.webp)

Selaa tarjouksia osoitteessa [@p2plightning](https://t.me/p2plightning) ja klikkaa "Osta satoshis" -painiketta kiinnostavan ilmoituksen alla.

**2. Vahvista tarjous ja määrä**

![Validation de l'offre](assets/fr/02.webp)

1. Palaa bot-keskusteluun

2. Vahvista tarjouksen valinta

3. Kirjoita summa fiat-valuutassa, jonka haluat ostaa

4. Botti pyytää sinua toimittamaan Lightning-laskun, jossa summa on satosheina

**3. Ota yhteyttä myyjään**

![Mise en relation](assets/fr/03.webp)

Kun lasku on lähetetty, robotti ottaa sinuun yhteyttä myyjään.

**4. Viestintä myyjän kanssa**

![Chat privé](assets/fr/04.webp)

Klikkaa myyjän lempinimeä avataksesi yksityisen keskustelukanavan, jossa voit vaihtaa fiat-maksutietoja.

**5. Maksuvahvistus

![Confirmation du paiement](assets/fr/05.webp)

Kun olet suorittanut fiat-maksun, käytä komentoa `/fiatsent` botin chatissa. Kun maksutapahtuma on valmis, voit antaa myyjälle arvosanan ja maksutapahtuma suljetaan.

### Kuinka myydä Bitcoineja

**1. Luo myyntitarjous**

![Création d'une offre de vente](assets/fr/06.webp)

Voit luoda myyntitarjouksen käyttämällä komentoa :

`/sell`

Botti opastaa sinua sitten askel askeleelta:

1. Valitse valuutta

2. Ilmoita myytävien satoshien määrä

3. Hinnan osalta sinulla on kaksi vaihtoehtoa:


   - Aseta kiinteä hinta satoshien määrälle
   - Markkinahinnan käyttäminen ja mahdollisuus soveltaa (positiivista tai negatiivista) preemiota

💡 **Vinkki**: Palkkion avulla voit mukauttaa hintaasi suhteessa markkinahintaan. Esimerkiksi preemio -1 % tarkoittaa, että myyt 1 % markkinahintaa halvemmalla.

**2. Vahvistus tilauksen luomisesta**

![Confirmation de l'ordre de vente](assets/fr/07.webp)

Kun tilaus on luotu, saat vahvistuksen, jossa on mahdollisuus peruuttaa tilaus komennolla `/cancel`.

**3. Hallitse myyntiä**

![Prise de l'ordre par un acheteur](assets/fr/08.webp)


- Kun ostaja vastaa tarjoukseesi, saat ilmoituksen, jossa on QR-koodi ja maksettava lasku.
- Tarkista ostajan profiili ja maine.

![Mise en relation avec l'acheteur](assets/fr/09.webp)


- Klikkaa ostajan lempinimeä avataksesi yksityisen keskustelukanavan.
- Ilmoita fiat-maksun tiedot ostajalle.
- Odota ostajan vahvistusta fiat-maksusta.
- Tarkista, että maksu on vastaanotettu tilillesi.

![Confirmation de la fin de l'ordre](assets/fr/10.webp)


- Vahvista maksutapahtuma `/release` ja viimeistele tilaus. Sinulla on mahdollisuus arvioida ostajaa.

## Hyvät käytännöt ja turvallisuus

### Turvallisuusvinkkejä


- Aloita pienillä määrillä
- Tarkista aina käyttäjien maine
- Käytä vain ehdotettuja maksutapoja
- Pidä kaikki viestintä bot-chatissa
- Älä koskaan jaa arkaluonteisia tietoja

### Mainejärjestelmä


- Jokaisella käyttäjällä on mainepisteet
- Onnistuneet maksutapahtumat nostavat pistemäärääsi
- Valitse käyttäjät, joilla on hyvä maine
- Ilmoita epäilyttävästä käytöksestä moderaattoreille

### Riitojen ratkaiseminen

1. Kun ongelmia ilmenee, pysy rauhallisena ja ammattimaisena

2. Käytä komentoa `/dispute` avataksesi tiketin

3. Toimita kaikki tarvittavat todisteet

4. Odota moderaattoria

## Vertailu muihin ratkaisuihin

Lnp2pbotilla on useita etuja ja haittoja verrattuna muihin P2P-vaihtoratkaisuihin, kuten Peach, Bisq, HodlHodl ja Robosat:

### Lnp2pbotin edut


- KYC:tä ei tarvita** : Toisin kuin jotkut alustat, Lnp2pbot ei vaadi henkilöllisyyden tarkistamista, mikä säilyttää käyttäjän luottamuksellisuuden.
- Nopeat tapahtumat**: Lightning-verkon ansiosta maksutapahtumat ovat lähes välittömiä.
- Alhaiset maksut** : Transaktiokustannukset ovat alhaisemmat kuin perinteisissä pörsseissä.
- Mobiilikäytettävyys**: LNP2PBot on käytettävissä Telegramin kautta, joten sitä on helppo käyttää mobiililaitteilla.
- Helppo käyttää** : Lnp2pbotin intuitiivinen käyttöliittymä tekee siitä helppokäyttöisen myös vähemmän kokeneille käyttäjille.

### Lnp2pbotin haitat


- Telegram-riippuvuus**: Lnp2pbotin käyttö edellyttää Telegram-tiliä, joka ei välttämättä sovi kaikille käyttäjille.
- Vähemmän likviditeettiä**: Verrattuna vakiintuneempiin alustoihin, kuten Bisqiin, likviditeetti voi olla rajoitetumpi.

Sen sijaan Bisqin kaltaiset ratkaisut tarjoavat enemmän likviditeettiä ja työpöytäliittymän, mutta niihin saattaa liittyä korkeampia maksuja ja pidempiä transaktioaikoja. HodlHodl ja Robosat puolestaan tarjoavat myös KYC-vapaata kaupankäyntiä, mutta niillä on erilaiset maksurakenteet ja käyttöliittymät.

## Hyödyllisiä resursseja


- Virallinen verkkosivusto: https://lnp2pbot.com/
- Dokumentaatio: https://lnp2pbot.com/learn/
- GitHub: https://github.com/lnp2pBot/bot
- Tuki: [@lnp2pbotHelp](https://t.me/lnp2pbotHelp)