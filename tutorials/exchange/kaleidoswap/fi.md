---
name: KaleidoSwap
description: Edistynyt opas RGB-varojen kaupankäyntiin Lightning Network:lla KaleidoSwapin avulla
---

![cover](assets/cover.webp)


KaleidoSwap on kehittynyt avoimen lähdekoodin työpöytäsovellus, joka kuroo umpeen RGB-protokollan ja Lightning Network:n välisen kuilun. Se toimii kattavana käyttöliittymänä RGB Lightning Nodes -solmujen hallintaan, vuorovaikutukseen RGB Lightning Service Providers (LSP) -palveluntarjoajien kanssa LSPS1-määrittelyn avulla ja RGB-varojen atomivaihtojen suorittamiseen.


Koska KaleidoSwap ei ole säilytysratkaisu, käyttäjät voivat säilyttää avaintensa ja tietojensa täyden hallinnan. Hyödyntämällä RGB:n asiakaspuolen validointiparadigmaa se mahdollistaa yksityiset ja skaalautuvat älykkäät sopimukset Bitcoin:n päällä. Tämä opetusohjelma sukeltaa KaleidoSwapin edistyneisiin ominaisuuksiin ja opastaa sinut "värillisen" UTXO:n hallinnan, tiettyjen omaisuuserien kanavalikviditeetin ja ottaja-tekijä-kaupankäyntimallin koukeroihin varmistaen, että voit hyödyntää tätä tehokasta hajautettua vaihtoprotokollaa täysimääräisesti.


## Asennus


KaleidoSwap tarjoaa valmiita binäärejä tärkeimpiä käyttöjärjestelmiä varten, mutta edistyneille käyttäjille lähdekoodista rakentaminen takaa, että käytät uusinta koodia omilla kokoonpanoillasi.


### Lataa binäärit


Voit ladata käyttöjärjestelmäsi uusimman version [viralliselta verkkosivustolta](https://kaleidoswap.com/) tai [GitHubin julkaisusivulta](https://github.com/kaleidoswap/desktop-app/releases).


### Asennusmenetelmät


1.  **Windows**: Lataa `.exe`-asennusohjelma ja suorita se.

2.  **macOS**: Lataa `.dmg`-tiedosto, avaa se ja vedä KaleidoSwap Sovellukset-kansioon.

3.  **Linux**: AppImage` tai `.deb`-tiedosto ja asenna/käynnistä se.



## Solmun asetukset


Kun käynnistät KaleidoSwapin ensimmäisen kerran, sinulle näytetään **Yhteysnäyttö**. Tämä on ensimmäinen vaihe ympäristön määrittämisessä.


![Node Selection Screen](assets/en/01.webp)


Sinun on valittava, miten yhteys RGB Lightning Network:ään muodostetaan. Tämä valinta vaikuttaa hallinnan ja yksityisyyden suojaan.


### Vaihtoehto 1: Paikallinen solmu (suositellaan omaan säilytykseen)


**Jos haluat täydellisen hallinnan ja yksityisyyden**, voit käyttää solmua suoraan koneellasi, katso alla olevat edut:


- Omahuoltajuus**: Sinulla on avaimet. Kukaan kolmas osapuoli ei voi jäädyttää varojasi tai sensuroida transaktioitasi.
- Yksityisyys**: Tietosi pysyvät laitteessasi.
- Itsenäisyys**: Ei riippuvuutta ulkopuolisista palveluntarjoajista.


Jos valitset **Lokaali solmu**, pääset asetusnäyttöön, jossa voit luoda uuden wallet:n tai palauttaa olemassa olevan.


![Local Node Setup Screen](assets/en/02.webp)


### Vaihtoehto 2: Etäsolmu


Muodosta yhteys etä-RGB Lightning Node:een (itse isännöity VPS:ssä tai isännöidyssä palvelimessa).


- Edut**: Ei paikallisten resurssien käyttöä, saatavuus 24/7.
- Vaihtokauppa**: Vaatii luottamusta isäntään tai etäpalvelimen hallintaa.


![Remote Node Setup Screen](assets/en/03.webp)


**KaleidoSwap on suunniteltu mahdollistamaan itsesuojaus.** Suosittelemme vahvasti oman solmun käyttämistä - joko paikallisesti (vaihtoehto 1) tai itse isännöimällä etäsolmua - jotta voit hyödyntää Bitcoin:n ja RGB:n sensuuria kestäviä ominaisuuksia täysimääräisesti.


## Wallet:n luominen


KaleidoSwap hallinnoi sekä Bitcoin- että RGB-varoja. wallet:n luomisprosessi alustaa avainsäilön, joka turvaa on-chain-varasi ja Lightning-kanavasi tilat.


Tässä on yksityiskohtainen prosessi:

1. Avaa KaleidoSwap ja valitse **Lokaali solmu**.

2. Napsauta **Luo uusi Wallet**.

3. **Tilin käyttöönotto**: Kirjoita **Tilin nimi** ja valitse **Verkko** (esim. Bitcoin Mainnet, Testnet, Signet).

4. **Lisäkokoonpano** (valinnainen): Jos olet tehokäyttäjä, voit määrittää mukautettuja RPC-päätepisteitä, indeksoijan URL-osoitteita tai välityspalvelimen asetuksia kohdassa "Lisäasetukset".

5. Klikkaa **Jatka**.

6. **Salasana**: Aseta vahva salasana wallet-tiedoston salaamiseksi paikallisesti.

7. **Palautuslause**: Kirjoita seed-lauseesi ylös ja säilytä se turvallisesti.


    - Kriittinen**: Tätä lausetta tarvitaan on-chain-varojesi ja solmun identiteetin palauttamiseksi.
    - Varoitus**: **Salamakanavan tiloja ei voida täysin palauttaa pelkästään seed:n avulla**. Sinun on myös ylläpidettävä staattisia kanavavarmuuskopioita (SCB), jotta voit palauttaa kanaviin lukitut varat.


![Wallet Creation Screen](assets/en/04.webp)



## Kojelaudan yleiskatsaus


Kun wallet on luotu, sinut ohjataan **Dashboard**-pääikkunaan.


![KaleidoSwap Dashboard](assets/en/05.webp)


_Huomaa: Yllä olevassa kuvakaappauksessa näkyy wallet, joka on jo rahoitettu ja jolla on aktiivisia kanavia. Uuden wallet:n saldot ovat nolla, eikä sillä ole aktiivisia kanavia, ennen kuin se on rahoitettu._ _


## Wallet:n rahoittaminen


RGB-varoilla toimiminen edellyttää wallet-varojen rahoittamista. KaleidoSwap tukee sekä Bitcoin- että RGB-varojen tallettamista on-chain-tapahtumien tai Lightning Network:n kautta.


### Bitcoin:n tallettaminen


1. Napsauta Pikatoiminnot-valikosta **Talletus**.

2. Valitse **BTC** omaisuusluettelosta.


![Select BTC Asset](assets/en/06.webp)


3. Valitse talletustapa: **On-chain** tai **Lightning**.


![BTC Deposit Options](assets/en/07.webp)



- Ketjussa**: Skannaa QR-koodi tai kopioi osoite lähettääksesi Bitcoin toisesta wallet:stä.
- Salama**: Luo lasku halutusta summasta.


![BTC On-chain Deposit](assets/en/08.webp)


### RGB-varojen ja värillisten UTXO:iden tallettaminen


Jotta voit vastaanottaa RGB-varoja (kuten USDT), tarvitset tiettyjä UTXO-varoja, jotka ovat käytettävissä "värjättäviksi" (joille on osoitettu omaisuuserä).


1. Napsauta **Talletus** ja valitse RGB omaisuuserä (esim. USDT). **Tärkeää**: Jos tämä on **ensimmäinen kerta**, kun solmusi vastaanottaa tämän tietyn omaisuuserän, ** jätä omaisuuserän ID-kenttä tyhjäksi**. Tuntemattoman omaisuuserän ID:n syöttäminen saa solmun palauttamaan virheilmoituksen, koska se ei vielä tunnista sitä.

2. Valitse **Ketjussa** tai **Valossa**.


![USDT Deposit Options](assets/en/09.webp)


#### Ketjussa olevat vastaanottotilat: Blinded


Kun vastaanotat RGB-varoja on-chain, sinulla on kaksi yksityisyydensuojatilaa:



- Blinded Receive (Suositellaan yksityisyyden suojaamiseksi)**: blinded" UTXO lähettäjälle. Pyydät lähettäjää lähettämään varoja omistamallesi UTXO:lle, mutta salaat todellisen UTXO-tunnisteen. Tämä tarjoaa paremman yksityisyyden suojan.
- Todistaja vastaanottaa**: Annat tavallisen Bitcoin-osoitteen. Pyydät lähettäjää luomaan sinulle *uusi* UTXO lähettämällä varat tähän osoitteeseen. Näin RGB-varat voidaan liittää suoraan uuteen UTXO:een, joka on luotu tapahtumalla.


#### Salaman talletus


Lightning-talletuksia varten riittää, että lähetät generate-laskun. RGB omaisuuserä ohjataan sinulle avointen kanavien kautta.


![USDT Lightning Invoice](assets/en/10.webp)



## Kanavien avaaminen RGB-varoilla


RGB-varojen ohjaaminen Lightning Network:n kautta edellyttää kanavaa, jolla on riittävä likviditeetti ja varojen kohdentaminen. Helpoin tapa päästä alkuun on **Ostaa kanava** LSP:ltä (Lightning Service Provider).


### Kanavan ostaminen Kaleido LSP:ltä


1. Siirry **Kanavat**-välilehdelle. Näet vaihtoehdot "Avaa kanava" (manuaalinen) tai "Osta kanava" (LSP).

2. Klikkaa **Osta kanava**.


![Channels Dashboard](assets/en/11.webp)


3. **Yhteys LSP:hen**: Sovellus muodostaa yhteyden Kaleidon oletusarvoiseen LSP:hen. Tämä palveluntarjoaja tarjoaa saapuvaa likviditeettiä ja tukee RGB-varojen reititystä.


![Connect to LSP](assets/en/12.webp)


4. **Konfiguroi kanava**:


    - Kapasiteetti**: Valitse kanavan kokonaiskapasiteetti Bitcoin.
    - RGB jako**: Valitse RGB-varallisuus (esim. USDT), jonka haluat vastaanottaa tai lähettää. LSP varmistaa, että kanava on konfiguroitu tukemaan tätä omaisuuserää.


![Configure Channel](assets/en/13.webp)



    - RGB Allokaatio**: Valitse RGB-varallisuus (esim. USDT), jonka haluat vastaanottaa tai lähettää. LSP varmistaa, että kanava on konfiguroitu tukemaan tätä omaisuuserää.


![RGB Allocation](assets/en/14.webp)


5.  **Maksu**: Maksu: Sinun on maksettava LSP:lle maksu kanavan avaamisesta ja likviditeetin tarjoamisesta. Voit maksaa käyttämällä **Lightning**- tai **On-chain** Bitcoin:ää. Maksu voidaan suorittaa sisäisestä KaleidoSwap wallet:sta tai ulkoisesta wallet:sta.


![Complete Payment](assets/en/15.webp)


6. Kun maksu on vahvistettu, LSP käynnistää kanavan avaamistapahtuman. Näyttöön ilmestyy **Tilaus suoritettu**.


![Order Completed](assets/en/16.webp)


7. Lohkoketjun vahvistuksen jälkeen kanavasi on aktiivinen ja valmis RGB-siirtoja varten.



## Kaupankäynti: Taker-Maker-malli


KaleidoSwapin kaupankäyntimoottori toimii **Taker-Maker-mallilla**. Voit vaihtaa omaisuuseriä manuaalisesti vertaisen kanssa tai käyttää markkinatakaajia (LSP).


### Vaihtaminen markkinatakaajan kanssa (LSP)


Tämä on yleisin tapa käydä kauppaa. Toimit **Takerina** ja toteutat toimeksiannot LSP:n (**Maker**) tarjoamaa likviditeettiä vastaan.


1. Siirry **Trade**-välilehdelle ja valitse **Market Maker**.

2. **Kirjoita summa**: Syötä Bitcoin:n määrä, jonka haluat lähettää (tai omaisuuserän, jonka haluat vastaanottaa). Käyttöliittymä näyttää arvioidun vaihtokurssin ja maksut.


![Market Maker Swap](assets/en/17.webp)


3. **Vahvista vaihto**: Tarkista yksityiskohdat, mukaan lukien vaihtokurssi ja tarkka summa, jonka saat. Napsauta **Vahvista vaihto**.


![Confirm Swap](assets/en/18.webp)


4. **Käsittely**: Lightning Network:ssä swap suoritetaan atomisesti. Näet tilaruudun, jossa ilmoitetaan, että swap-toiminto on käynnissä.


![Swap Pending](assets/en/19.webp)


5. **Menestys**: Kun HTLC:t on maksettu, swap on valmis ja varat ovat kanavassasi.


![Swap Success](assets/en/20.webp)



## Kehittäjä API


KaleidoSwapin päälle rakentaville kehittäjille sovellus tarjoaa API:n, joka tukee:



- RGB LSPS1**: Automaattisia likviditeettipalveluja varten.
- Vaihda API**: Ohjelmallista kaupankäyntiä ja markkinatakausta varten.
- WebSocket**: Reaaliaikaisia markkinatietotilauksia varten.


Katso [API Documentation](https://docs.kaleidoswap.com/api/introduction) täydelliset päätepisteet ja tekniset tiedot.


## Päätelmä


KaleidoSwapin avulla voit hyödyntää RGB-varojen yksityisyyttä ja skaalautuvuutta Lightning Network:ssä. Ymmärtämällä värillisiä UTXO:ita ja kanavavarojen jakamista voit hyödyntää tätä tehokasta hajautettua vaihtoprotokollaa täysimääräisesti.