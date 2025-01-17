---
name: Braiins Pool

description: Johdanto Braiins Pooliin
---

![signup](assets/cover.webp)

Braiins Pool, joka tunnettiin aiemmin nimellä Slush Pool, on kaikkein ensimmäinen Bitcoin-louhintapooli. Perustettu marraskuussa 2010, se louhi ensimmäisen lohkonsa 16. joulukuuta 2010, lohko 97834.

Toukokuuhun 2024 mennessä Braiins Poolin laskentateho on 13 EH/s, mikä edustaa noin 1,8% koko Bitcoinin hashratesta. Se on louhinut yhteensä 1 307 188 bitcoinia, mikä on suunnilleen 6% maksimimäärästä 21 miljoonaa bitcoinia, jotka koskaan tulevat olemaan olemassa.

### Korvausjärjestelmä

Vuoden 2023 lopusta lähtien Braiins Pool on muuttanut korvausjärjestelmäänsä ottaakseen käyttöön FPPS (Full Pay Per Share) -järjestelmän. Tämä tarkoittaa, että louhijat saavat palkkioita joka päivä edellisen päivän työstään, vaikka pooli ei löytäisikään lohkoa. Tämä eroaa vanhasta järjestelmästä, jossa louhijat saivat palkkion vain silloin, kun pooli löysi lohkon.

**On huomionarvoista, [Mononautin twiitin mukaan](https://x.com/mononautical/status/1777686545715089605), joka analysoi Bitcoin TimeChainia, että monet FPPS-järjestelmää käyttävät louhintapoolit lähettäisivät louhitut bitcoinit AntPoolin osoitteeseen, mikä tarkoittaisi, että AntPool hallitsee kaikkien näiden poolien hashratea, noin 47% globaalista Bitcoinin hashratesta. Tämä on erittäin huono uutinen verkon hajauttamisen kannalta.**

### Poolin Maksut

Braiins Poolin maksut ovat 2,5%, mutta jos käytät BraiinsOS:ää koneillasi, maksut ovat 0%

### Nostot

**Lightning Nostot**
Lightning-nostot mahdollistavat palkkioidesi nostamisen ilman minimimäärää kerran päivässä Lightning-osoitteen kautta.
Tätä menetelmää käyttääksesi sinulla täytyy olla lompakko, joka on yhteensopiva Lightning-osoitteiden kanssa.

**On-Chain Nostot**
On-Chain-nostot ovat rajattuja minimimäärään ja niihin voi liittyä maksuja.
Minimimäärä: 20 000 sats
Maksut: 10 000 sats määrille, jotka ovat alle 500 000 sats
Ilmaiset määrille, jotka ovat yli 500 000 sats
Nostot voidaan laukaista aikavälin tai määrän perusteella.

## Tilin Luominen

Aloittaaksesi Braiins Poolin käytön [mene heidän verkkosivuilleen](https://braiins.com/pool) ja klikkaa "SIGN UP" yläoikealla


![signup](assets/3.webp)

Syötä tietosi ja vahvista, sen jälkeen saat sähköpostin, jossa pyydetään vahvistamaan osoitteesi. Vahvista linkillä, jonka sait sähköpostiisi ja kirjaudu sen jälkeen alustalle

![signup](assets/4.webp)


## "Workerin" lisääminen
Worker on louhija, jonka yhdistät pooliin. Lisätäksesi uuden louhijan, klikkaa "Workers" vasemmassa sivupalkin valikossa.
![signup](assets/7.webp)

Klikkaa sen jälkeen violettiä "Connect Workers +" -nappia.

Tässä ikkunassa valitse maantieteellinen alueesi.

Jos haluat yhdistää louhijan, joka käyttää BraiinsOS:ää, valitse "Stratum V2" -protokolla. Muussa tapauksessa valitse "Stratum V1".

![signup](assets/8.webp)

Saat tiedot, jotka sinun tulee syöttää louhijasi verkkosivulle (katso louhijasi dokumentaatiosta, mihin nämä tiedot tulee syöttää).

Tässä, **"stratum+tcp://eu.stratum.braiins.com:3333"** on poolin URL.
**JimZap.workerName** on tunnisteesi ja louhijasi nimi, missä JimZap on tunniste ja .workerName on louhijan nimi. Jos sinulla on useita louhijoita, voit joko antaa niille saman nimen, jolloin niiden laskentateho lasketaan yhteen hallintapaneelissa, tai antaa niille eri nimet niiden yksilölliseen seurantaan.
Ja salasana on aina sama **"anything123"**

Kun olet syöttänyt tämän tiedon louhijasi verkkosivulle ja se on aloittanut louhinnan, näet sen muutaman minuutin kuluttua Braiins Poolin hallintapaneelissa.

## Hallintapaneelin Yleiskatsaus

![signup](assets/9.webp)

Yläbannerissa näet kaikkien louhijoittesi keskimääräisen kokonaislaskentatehon viiden minuutin, yhden tunnin ja 24 tunnin aikana. Ja yhteenvedon verkossa tai offline-tilassa olevien louhijoiden määrästä.
Alla oleva kaavio mahdollistaa laskentatehosi kehityksen seuraamisen.

![signup](assets/10.webp)

Tämän kaavion alapuolella on useita tietoja palkkioistasi satseina.

**"Tämän Päivän Louhintapalkkiot"** Ilmoittaa kuinka monta satsia olet louhinut tänään. Päivän päättyessä tämä arvo nollataan ja satseja siirretään tilillesi.

**"Eilisen Kokonaispalkkio"** Kuinka monta satsia louhit edellisenä päivänä

**"Arvioitu Kannattavuus (1 TH/s)"** On arvio siitä, kuinka monta satsia ansaitset päivässä 1 TH/s laskentateholla. Esimerkiksi, jos arvo on 77 satsia, ja sinulla on 10 TH/s laskentatehoa koko päivän ajan, teoriassa ansaitsisit 77 x 10 = 770 satsia päivässä.

**"Kaikkien Aikojen Palkkio"** Kokonaismäärä satseja, jotka olet louhinut Braiins Poolissa

**"Palkkiojärjestelmä"** Poolin soveltama palkkioprosentti

**"Seuraavan Maksun ETA"** Arvio siitä, kuinka kauan kestää ennen kuin voit nostaa satseja alustalta. Tässä arvio näyttää tyhjää, koska louhinta on ollut käynnissä vasta muutaman minuutin.

**"Tilin Saldo"** Tililläsi olevien satsejen määrä, jotka voit sen jälkeen nostaa.
## Nostojen Asettaminen
Voit nostaa palkkiosi joko on-chain tai lightning-osoitteella.

Yläosassa, klikkaa "Funds". Oletuksena sinulla on "Bitcoin Account". Voit luoda muita jakamaan palkkiot. Palaamme tähän seuraavassa osiossa.

Toistaiseksi, klikkaa "Set up".

![signup](assets/17.webp)

Tässä uudessa ikkunassa voit valita "Onchain payout".

Nimeä tämä lompakko, anna BTC-osoite ja valitse haluamasi laukaisutyyppi. "Threshold" tarkoittaa, että maksu laukaistaan, kun olet kumuloinut määritellyn määrän BTC:tä, ja "Time interval" tarkoittaa, että maksu laukaistaan säännöllisin väliajoin (päivä/viikot/kuukaudet).

Huomaa, että minimimäärä on 0.0002 BTC ja että alle 0.005 BTC:n kohdalla sovelletaan 0.0001 BTC:n maksua.

![signup](assets/18.webp)

Jos haluat käyttää Lightning-nostoja, tarvitset lompakon, joka tarjoaa Lightning-osoitteen. Esimerkiksi voit käyttää getAlbya.

Klikkaa ikkunan yläosassa "Lightning payout".

Anna Lightning-osoitteesi ja merkitse ruutu "I understand..." sitten vahvista.

Tällä nostomenetelmällä palkkiosi lähetetään lompakkoosi joka päivä.

![signup](assets/14.webp)
Kun olet vahvistanut maksuasetuksesi, saat vahvistussähköpostin.
![signup](assets/15.webp)

## Palkkioiden Jakaminen

Braiins Pool mahdollistaa myös palkkioidesi jakamisen useiden lompakoiden kesken.

Tehdäksesi tämän, klikkaa yläosassa "Mining" ja sen jälkeen vasemmalla "Settings".

![signup](assets/19.webp)

Tällä sivulla voit lisätä toisen "Financial Account" klikkaamalla "Add Another Financial Account" ja jakaa palkkiosi % mukaan näiden eri tilien kesken, joihin sinun tulee liittää lompakko. Liittääksesi uuden lompakon Financial Accountiin, viittaa edelliseen osioon.