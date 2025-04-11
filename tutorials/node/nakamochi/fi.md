---
name: Nakamochi
description: Node Running Made Easy - Miten Nakamochi Bitcoin- ja Lightning-solmun perustaminen ja käyttö tehdään helpoksi.
---
Oman Bitcoin- ja Lightning-solmun pyörittämisen ei enää tarvitse olla monimutkainen tehtävä, joka rajoittuu teknisiin asiantuntijoihin. Perinteisesti solmujen perustaminen ja hallinta on vaatinut syvällistä tietämystä kryptografiasta, verkottumisesta ja ohjelmistokehityksestä. Nakamochi muuttaa tämän muuttamalla solmut kaikkien ulottuville teknisestä taustasta riippumatta.

Nakamochin avulla kuka tahansa voi perustaa solmun ja käyttää sitä kotoa käsin, mikä mahdollistaa täydellisen yksityisyyden ja taloudellisen riippumattomuuden. Täydellisen solmun pyörittäminen ei ainoastaan turvaa omia transaktioitasi, vaan myös edistää Bitcoin-verkon vahvuutta. Hajautettu ja kestävä Bitcoin-verkko nojaa solmujen laajaan jakautumiseen varmistaakseen turvallisuutensa ja riippumattomuutensa.

### Sisällysluettelo


- Mikä on Nakamochi ja miten se toimii?
- Nakamochin perustaminen
- Tietoja Lightning Networkista
- Kanavien avaaminen ja transaktioiden tekeminen Lightning-verkossa

## Mikä on Nakamochi ja miten se toimii?

Nakamochi on vain Bitcoinia käyttävä täysi solmu, joka tukee sekä Bitcoin- että Lightning-verkkoja. Se sisältää integroidun Bitcoin- ja Lightning-lompakon, jonka avulla käyttäjät voivat käyttää turvallista, itsesovereignia Bitcoin-solmua ja samalla hyötyä Lightning-verkon nopeudesta ja alhaisista transaktiokustannuksista.

Nakamochi-solmua hallitaan mobiilisovelluksella [BitBanana (Android)](https://bitbanana.app) ja [Zeus (iOS)](https://bitbanana.app), jonka avulla voit hallita sitä kätevästi mistä tahansa. Nämä sovellukset toimivat solmusi kauko-ohjaimina, joiden avulla voit maksaa suoraan Bitcoinilla tai Lightningilla, hallita tapahtumia, avata tai sulkea kanavia, tarkistaa saldot ja seurata solmusi suorituskykyä helposti.

## Nakamochin käyttöönotto kestää vain 5 minuuttia

### Vaihe 1: Kytke ja aloita

1. Kytke Nakamochiin virta ja Wi-Fi.

2. Napsauta **"Setup New Wallet "** ja tallenna turvallisesti 24-sanainen palautuslauseesi.

3. Käytä solmujen hallintasovellusta (Zeus tai BitBanana) yhteyden muodostamiseen Nakamochiisi:

4. Avaa sovellus ja skannaa Nakamochissa näkyvä QR-koodi.

5. Lisäturvaksi voit asettaa laitteeseen PIN-koodin.

![image](assets/en/01.webp)

_Kytke virta ja kirjoita 24-sanainen siemenlauseesi_

![image](assets/en/02.webp)

odota, kunnes lohkoketju on saanut meidät kiinni_

![image](assets/en/03.webp)

_Uuden lompakon perustaminen Lightning-välilehdelle_

![image](assets/en/04.webp)

_Scannaa QR-koodi Node Management -sovelluksella_

![image](asset/en/05.webp)

_Lisäturvallisuuden lisäämiseksi aseta PIN-koodi_

**Huomautus:** _Salli Nakamochi-solmun synkronoitua lohkoketjun kanssa. Tämä prosessi voi kestää jonkin aikaa riippuen internetyhteydestäsi._

## Tietoja Lightning Networkista

Bitcoin Lightning Network mullistaa Bitcoin-tapahtumat tekemällä niistä nopeampia, halvempia ja tehokkaampia. Se sopii täydellisesti jokapäiväiseen käyttöön, sillä se mahdollistaa lähes välittömät maksut minimaalisilla maksuilla, mikä on ihanteellista mikrotransaktioihin, kuten kahvin ostamiseen tai usein toistuvien pienten ostosten hoitamiseen.

Koska Lightning toimii ketjun ulkopuolella, se on suunniteltu skaalautuvaksi ja tukee tuhansia transaktioita sekunnissa ylikuormittamatta Bitcoinin päälohkoketjua. Tämä tekee siitä keskeisen toimijan Bitcoinin kehittymisessä käytännölliseksi, globaaliksi maksujärjestelmäksi.

Toinen etu on yksityisyys, sillä Lightningissa tapahtuvat maksutapahtumat ohjataan yksityisten maksukanavien kautta sen sijaan, että ne kirjattaisiin suoraan lohkoketjuun. Tämä takaa hienovaraisemman tavan tehdä liiketoimia säilyttäen samalla Bitcoinin vankan turvallisuuden.

#### Maksukanavat selitetty

Lightning Network toimii maksukanavien kautta, jotka ovat kahden osapuolen välisiä yhteyksiä, jotka mahdollistavat useita transaktioita ilman suoraa vuorovaikutusta lohkoketjun kanssa. Kun kanava on avoinna, kahden osapuolen välinen saldo päivittyy tässä toisen tason Lightning-ratkaisussa jokaista transaktiota varten, mikä takaa nopeat ja edulliset maksut. Vain kanavan avaaminen ja sulkeminen kirjataan ketjuun, mikä vähentää Bitcoin-lohkoketjun ruuhkautumista.Tämä rakenne takaa skaalautuvuuden ja yksityisyyden, sillä yksittäisiä transaktioita ei kirjata julkiseen pääkirjaan.

**Esimerkki:** Alice ja Bob avaavat kanavan sitomalla siihen Bitcoinin. Alice lähettää Bitcoineja Bobille, ja heidän ketjun ulkopuoliset saldonsa päivittyvät välittömästi ilman ketjun sisäistä kirjausta. Jos Alice sitten maksaa Charlielle, eikä Alicella ole suoraa kanavaa Charlielle, maksu voidaan ohjata Bobin kanavan kautta Charlielle. Välityssolmujen kautta tapahtuva reititys varmistaa maksut myös ilman suoria yhteyksiä, mikä tekee verkosta erittäin tehokkaan.

## Kanavien avaaminen ja transaktioiden tekeminen Lightning-verkossa

Kun Nakamochi on asennettu ja yhdistetty solmunhallintasovellukseen, voit aloittaa Lightning Networkin käytön avaamalla kanavia ja tekemällä tapahtumia.

### Kanavien avaaminen Zeuksessa (iOS):

1. Siirry **"Kanavat "** -välilehdelle (alavalikko).

2. Klikkaa **"+"** avataksesi uuden kanavan.

3. Skannaa tai syötä sen solmun julkistusavain, johon haluat muodostaa yhteyden.

4. 

5. Napsauta **"Avaa kanava "**.

![image](asset/en/06.webp)

_ZEUS Kuvakaappaus_

Lisätietoja: [Channels | Zeus Documentation](https://docs.zeusln.app/)

### Kanavien avaaminen BitBanana (Android):

1. Avaa hampurilaisvalikko (vasemmalla).

2. Siirry kohtaan **"Kanavat "**.

3. Klikkaa **"+"** lisätäksesi/avataksesi uuden kanavan.

4. Skannaa tai liitä julkistusavain.

5. 

![image](asset/en/07.webp)

_Bitbanana Kuvakaappaus_

Lisätietoja: [BitBanana](https://bitbanana.com)

Kun kanavasi on avattu, maksut voidaan ohjata sen kautta muille verkoston osallistujille. Saldot mukautuvat ketjun ulkopuolella, joten maksutapahtumat ovat lähes välittömiä ja niistä peritään vain vähän maksuja.

Jos et enää tarvitse kanavaa, voit sulkea sen. Tämä toimenpide ratkaisee sinun ja vertaisesi välisen loppusaldon ja kirjaa sen ketjuun. 

Yleisesti ottaen suosittelemme kanavien jättämistä auki kustannusten vähentämiseksi ja verkon luotettavuuden ja tehokkuuden lisäämiseksi. Pitämällä kanavat auki minimoit ketjussa suoritettavien tapahtumien maksut, vältät kanavien uudelleenkytkentöjen aiheuttamat käyttökatkokset ja säilytät vakaan reitityskapasiteetin saumatonta maksujen käsittelyä varten. Tämä lähestymistapa edistää vankkaa ja joustavaa verkkoa ja parantaa samalla yleistä käyttäjäkokemusta ja vähentää operatiivisia kustannuksia.

### Hyödyllisiä linkkejä


- [Tietoa Nakamochista](https://nakamochi.io/)
- [Tilaa Nakamochin uutiskirje](https://90c7addc.sibforms.com/serve/MUIFAHG7H5YBPpm-kZ8G6TuS-nmL4uaq85rlpBfI__S79tZ5jheIJfF3kJYudycgs_6_RUdDBkt8Sd7OyNL_JDTTJvOb36ifF6vcQoabBXKp4cbefzh1DYqnok_jItexICcQL13ucd2aS581ngqy7jr0Q1H3HhxV3z2eWKE5-Z-YMasj-MMotQeDvdorMCSi0XgCWDqs8rEMQC7E)