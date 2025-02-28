---
name: Nerdminer
description: Aloita bitcoinien louhinta mahdollisuudella voittaa lähes 0
---

![kansi](assets/cover.webp)

> NerdMiner_v2:n asennus

Tässä oppaassa opastamme sinut tarvittavien vaiheiden läpi NerdMiner_v2:n asettamisessa, joka on laitteisto (ESP-32 S3), joka on omistettu bitcoinien louhintaan.
Ilmiselvästi tällaisen laitteen laskentateho ei pysty kilpailemaan amatöörien tai ammattilaisten louhijoiden ASIC-laitteiden kanssa. Siitä huolimatta NerdMiner on täydellinen opetustyökalu tehdä bitcoinien louhinnasta konkreettista. Ja kuka tietää, (paljon) onnea myöten, saatat löytää lohkon ja siihen liittyvän palkkion. Uteliaita varten tarkastelemme [Voiton todennäköisyyden arviointi](#estimation-de-la-probabilite-de-gain) -osiossa. Tehonkulutuksen osalta NerdMiner kuluttaa 0,5W; vertailun vuoksi LED-lamppu kuluttaa keskimäärin 20 kertaa enemmän.

Ennen eri vaiheiden läpikäymistä, listataan tarvittavat välineet sen tekemiseen:

- [Lilygo T-display S3](https://lilygo.cc/products/t-display-s3)
- [USB-C virtalähde](https://amzn.eu/d/gIOot90)
- 3D-kotelo: jos sinulla on 3D-tulostin, voit ladata [3D-tiedoston](https://www.printables.com/model/501547-nerdminer-v2-click-case-w-buttons) muussa tapauksessa voit ostaa yhden [Silexperience-verkkokaupasta](https://silexperience.company.site/NerdMiner_V2-p544379757).
- PC, jossa on asennettuna Chrome-selain
- internet-yhteys
- bitcoin-osoite

Voit myös ostaa esiasennetun NerdMiner-paketin useilta jälleenmyyjiltä, kuten:

- [DécouvreBitcoin](https://shop.decouvrebitcoin.com/products/nerd-miner?_pos=1&_psq=nerd&_ss=e&_v=1.0)
- [BitMaker](https://bitronics.store/shop/)

Ensiksi näemme, miten ohjelmisto väläytetään ESP-32 S3:lle, ja sen jälkeen näemme, miten se käynnistetään uudelleen wifi-verkon vaihtamiseksi. Nämä vaiheet ovat Windows-käyttäjille, jos käytät Linux-käyttöjärjestelmää, suorita [alkutoimet](#etapes-preliminaires-pour-utilisateurs-linux) jotta järjestelmäsi tunnistaa ESP-32 S3:n.

# NerdMiner_v2-ohjelmiston asennus

Ohjelmiston asennus on suuresti yksinkertaistettu webflasherin käytön ansiosta.

## Vaihe 1: Webflasherin valmistelu

Ensimmäiseksi sinun täytyy mennä [verkossa olevaan NM2 flasheriin](https://bitmaker-hub.github.io/diyflasher/).

Valitse sitten firmware, joka vastaa ESP-32:tasi. Useimmiten se on oletusarvoinen: T-Display S3. Klikkaa sen jälkeen "Flash".

> ⚠️ On tärkeää, että käytät Chrome-selainta - koska se sallii oletuksena flashin käytön ja pääsyn USB-portteihisi.

![](assets/webflasher.webp)

## Vaihe 2: ESP-32:n yhdistäminen

Kun webflasher on käynnistetty, pop-up-ikkuna avautuu näyttäen eri USB-portit, jotka selain tunnistaa.
Voit sen jälkeen liittää ESP-32:si, ja näytölle ilmestyy uusi portti (tässä tapauksessa se on ttyACM0-portti). Sinun täytyy sitten valita se ja klikata "yhdistä".
![](assets/flasher-port-serial.webp)

Ohjelmisto ladataan sen jälkeen ESP32:lle muutamassa sekunnissa.

![](assets/NM2-sucessfully-installed.webp)

## Vaihe 3: NerdMiner-asetusten määrittäminen

NerdMinerin asetukset tehdään älypuhelimen tai tietokoneen kautta.
Ota WiFi käyttöön ja yhdistä paikalliseen NerdMinerAP-verkkoon. Jos käytät älypuhelinta, asetusportaali avautuu automaattisesti. Muussa tapauksessa kirjoita osoite 192.168.4.1 selaimen osoiteriville.
Valitse sen jälkeen "Configure WiFi".

Voit nyt määrittää NerdMinerisi.
Aloita yhdistämällä WiFi-verkkoon valitsemalla verkon nimi ja syöttämällä siihen liittyvä salasana.

Sen jälkeen voit valita louhintapoolin, johon haluat osallistua. Bitcoin-louhinnassa on yleistä yhdistää laskentatehoa louhintapoolien avulla, jotta mahdollisuudet löytää lohko kasvavat vastineeksi palkkion jakamisesta suhteessa tarjottuun hashrateen.
NerdMinereille voit valita yhdistämisen seuraaviin pooleihin:

| Pool URL          | Port  | URL                        | Status                                   |
| ----------------- | ----- | -------------------------- | ---------------------------------------- |
| public-pool.io    | 21496 | https://web.public-pool.io | Oletus, solo ja avoimen lähdekoodin louhintapool |
| pool.nerdminer.io | 3333  | https://nerdminer.io       | Ylläpitäjänä CHMEX                       |
| pool.vkbit.com    | 3333  | https://vkbit.com/         | Ylläpitäjänä djerfy                      |

Kun olet valinnut poolin, sinun täytyy syöttää bitcoin-osoitteesi, jotta voit vastaanottaa palkkion, jos (poikkeuksellisesti) lohko löytyy.

Valitse myös aikavyöhykkeesi, jotta NerdMiner näyttää ajan oikein.
Voit nyt klikata "tallenna".

![](assets/wifi-configuration.webp)

Onnittelut, olet nyt osa Bitcoin-louhintaverkkoa!

## NerdMinerin toiminta

NerdMinerv2-ohjelmistossa on 3 eri näyttöä, joihin pääset klikkaamalla näytön oikeassa yläkulmassa olevaa yläpainiketta:

- Päänäyttö tarjoaa pääsyn NerdMinerisi tilastoihin.
- Toinen näyttö tarjoaa pääsyn aikaan, hashrateesi, bitcoinin hintaan ja lohkon korkeuteen.
- Kolmas näyttö tarjoaa pääsyn tilastoihin globaalista bitcoin-louhintaverkosta.
  ![](assets/NM2-screens.webp)

Jos haluat käynnistää NerdMinerisi uudelleen, esimerkiksi vaihtaaksesi WiFi-verkkoa, sinun täytyy painaa yläpainiketta 5 sekunnin ajan.

Alapainikkeen painaminen kerran sammuttaa NerdMinerisi. Painamalla kahdesti voit kääntää näytön suuntaa.

### Alustavat vaiheet Linux-käyttäjille

Tässä ovat vaiheet, jotta Chrome tunnistaa sarjaporttisi Linuxissa.

1. Tunnista liitetty portti:

- Liitä ESP-32 tietokoneeseesi.
- Avaa terminaali.
- Anna seuraava komento listataksesi kaikki portit:
  - `dmesg | grep tty`
  - tai `ls /dev/tty*`
- Ollaksesi varma portista, voit edetä eliminoinnin kautta toistamalla komennon ilman, että ESP-32 on liitettynä.

2. Muuta liitetyn portin oikeuksia:
- Oletuksena sarjaporttien käyttö saattaa vaatia pääkäyttäjän oikeuksia, joten teemme ne saataville lisäämällä käyttäjäsi `dialout`-ryhmään.
  - `sudo usermod -a -G dialout KÄYTTÄJÄNIMESI`, korvaa `KÄYTTÄJÄNIMESI` omalla käyttäjänimelläsi.
  - kirjaudu sen jälkeen ulos ja takaisin sisään tällä käyttäjällä, tai käynnistä järjestelmä uudelleen varmistaaksesi, että ryhmämuutokset tulevat voimaan.

Nyt kun ESP-32 tunnistetaan järjestelmässäsi, voit palata takaisin [ensimmäiseen vaiheeseen](#etape-1-preparation-du-webflasher) ohjelmiston asentamiseksi.

## Yhteenveto

Ja siinä se on! NerdMiner_v2 on nyt määritetty ja valmis käytettäväksi.

Onnellista louhintaa ja onnea matkaan!

### Voittamisen todennäköisyyden arviointi

Kokeillaanpa arvioida hauskanpito mielessä lohkopalkinnon voittamisen todennäköisyyttä. Tämä arvio on karkea ja pyrkii vain saamaan todennäköisyyden suuruusluokan.
NerdMiner voi yhdistää vain "solo mining pool" -altaisiin, mikä tarkoittaa, että allas ei yhdistele kaikkien yhteenliitettyjen louhijoiden hashratea, vaan toimii yksinkertaisesti koordinaattorina.
Oletetaan nyt, että NerdMinerillamme on hashrate noin 45kH/s.

Kun tiedetään, että kokonaishashrate on noin 450 EH/s (tai 4,5 x 10^20 hashea sekunnissa), voimme olettaa, että seuraavan lohkon löytämisen todennäköisyys on 1 sadassa miljardissa miljardissa, mikä on erittäin, erittäin epätodennäköistä. Joten lisäksi, että se on opetustyökalu ja uteliaisuuden kohde, NerdMiner voi toimia lottokuponkina bitcoin-louhinnassa marginaalisella sähkönkulutuksella 0,5 W -- vaikka juuri näimme, että voittamisen todennäköisyys on naurettavan alhainen. Mutta miksi ei haastaisi onneaan?

### Lisätietoja

Tässä on joitakin linkkejä, jos haluat lukea aiheesta lisää:

- [NerdMiner_v2-projektisivu](http://github.com/BitMaker-hub/NerdMiner_v2)
- [NerdMinerien kattava dokumentaatio](https://docs.bitwater.ch/nerd-miner-v2/)