---
name: Tails

description: Asenna Tails USB-tikulle
---

![kuva](assets/cover.webp)

Kannettava ja amneesinen käyttöjärjestelmä, joka suojaa sinua valvonnalta ja sensuurilta.

## Miksi asentaa Tails USB-tikulle?

Tails (https://tails.net/) on helpoin tapa pitää aina mukanasi turvallista tietokonetta, joka ei jätä jälkiä käyttämääsi tietokoneeseen.

Tailsin käyttämiseksi sammuta käytössäsi oleva tietokone (vanhempiesi luona, ystäväsi luona, internetkahvilassa...) ja käynnistä se Tails USB-tikulla Windowsin, macOS:n tai Linuxin sijaan.

Tämän jälkeen sinulla on työtila ja viestintäympäristö, joka on riippumaton tavallisesta käyttöjärjestelmästä eikä koskaan käytä kiintolevyä.

Tails ei kirjoita kiintolevylle ja käyttää toimiakseen vain tietokoneen RAM-muistia. Tämä muisti tyhjennetään kokonaan, kun Tails sammutetaan, poistaen siten kaikki mahdolliset jäljet.

## Joitakin konkreettisia käyttötapauksia

Jotta saat konkreettisia ideoita Tails USB-tikun jatkuvan mukana pitämisen hyödyistä, tässä on pieni, ei-tyhjentävä lista, jonka Agora256-tiimi on koonnut:

- Yhdistä Internetiin ja Toriin sensuroimattomalla ja nimettömällä tavalla selataksesi verkkosivustoja jättämättä jälkiä;
- Avaa PDF epäilyttävältä verkkosivustolta;
- Testaa Bitcoin yksityisen avaimen varmuuskopiointi Electrum-lompakolla;
- Käytä toimisto-ohjelmistoa (LibreOffice) ja työskentele tietokoneella, joka ei kuulu sinulle;
- Ota ensiaskeleesi Linux-ympäristössä oppiaksesi, miten pääset eroon Microsoftin ja Applen maailmasta.

## Miten luottaa Tailsiin?

Ohjelmiston käyttämisessä on aina luottamuselementti, mutta sen ei tarvitse olla sokeaa. Työkalun, kuten Tailsin, on pyrittävä tarjoamaan käyttäjilleen keinoja olla luotettava. Tailsille tämä tarkoittaa:

- Julkinen lähdekoodi: https://gitlab.tails.boum.org/;
- Projekti perustuu arvostettuihin projekteihin: Tor ja Debian;
- Todennettavissa ja toistettavissa olevat lataukset;
- Eri yksilöiden ja organisaatioiden suositukset.

## Asennus- ja käyttöopas

Tämän asennusoppaan tarkoituksena on ohjata sinut läpi jokaisen asennusvaiheen. Emme kuvaile toimenpiteitä enempää kuin virallinen opas, mutta osoitamme sinut oikeaan suuntaan antaen samalla vinkkejä ja niksejä.

Käytännön kokemuksen vuoksi nämä vinkit keskittyvät macOS- ja Linux-alustoihin.
🛠️
Ennen tämän menettelyn aloittamista varmista, että sinulla on USB-tikku, jonka lukunopeus on vähintään 150 MB/s ja kapasiteetti vähintään 8 GB, ihanteellisesti USB 3.0.

Edellytykset:

- 1 USB-tikku, vain Tailsia varten, kapasiteetiltaan vähintään 8 GB
- Internetiin yhdistetty tietokone, jossa on Linux, macOS, (tai Windows)
- Noin tunnin verran vapaa-aikaa, riippuen Internet-yhteytesi nopeudesta, mukaan lukien ½ tuntia asennukseen (1.3 GB tiedoston lataus)

## Vaihe 1: Lataa Tails tietokoneellesi

![kuva](assets/1.webp)

> 🔗 Virallinen Tails-osio: https://tails.net/install/linux/index.fr.html#download

Asennustiedoston .img-päätteisen tiedoston lataaminen saattaa kestää jonkin aikaa riippuen Internet-latausnopeudestasi, joten suunnittele etukäteen. Nykyaikaisella ja tehokkaalla yhteydellä se vie alle 5 minuuttia.

Tallenna tiedosto tunnettuun kansioon, kuten Lataukset, sillä se on tarpeen seuraavassa vaiheessa.

## Vaihe 2: Varmista latauksesi

![kuva](assets/2.webp)
> 🔗 Virallinen Tails-osio: https://tails.net/install/linux/index.fr.html#verify
Latauksen tarkistaminen varmistaa, että se on peräisin Tails-kehittäjiltä eikä sitä ole vioittunut tai kaapattu latauksen aikana.

On mahdollista manuaalisesti tarkistaa, että juuri lataamasi tiedosto on odotettu käyttäen PGP:tä, mutta ilman edistyneitä tietoja, tämä tarkistus tarjoaa saman turvallisuustason kuin JavaScript-tarkistus lataussivulla, ollen kuitenkin paljon monimutkaisempi ja virhealttiimpi.

Tiedoston tarkistamiseen käytä virallisessa osiossa tarjottua "Valitse latauksesi..." -painiketta!

## Vaihe 3: Asenna Tails USB-tikullesi

![kuva](assets/3.webp)

> 🔗 Virallinen Tails-osio:
>
> - Linux: https://tails.net/install/linux/index.fr.html#install
> - macOS: https://tails.net/install/mac/index.fr.html#etcher ja https://tails.net/install/mac/index.fr.html#install

Tämä Tailsin asentamisen vaihe USB-tikullesi on koko oppaan vaikein, erityisesti jos et ole tehnyt sitä aiemmin. Tärkeintä on valita käyttöjärjestelmäsi mukainen oikea menettely virallisessa osiossa: Linux tai macOS.

Kun työkalut on asennettu ja valmisteltu suositellusti, tiedosto, jolla on .img-laajennus, voidaan kopioida tikullesi (poistaen kaikki olemassa olevat tiedot) tehdäksesi siitä itsenäisesti "käynnistettävän".

Onnea matkaan! ja nähdään vaiheessa 4.

## Vaihe 4: Käynnistä Tails USB-tikultasi

![kuva](assets/4.webp)

> 🔗 Virallinen Tails-osio: https://tails.net/install/linux/index.en.html#restart
> On aika käynnistää yksi tietokoneistasi uudelleen käyttäen uutta USB-tikkua. Työnnä se yhteen sen USB-porteista ja käynnistä uudelleen!

> 💡 Useimmat tietokoneet eivät automaattisesti käynnisty Tails USB-tikulta, mutta voit painaa käynnistysvalikon näppäintä näyttääksesi listan mahdollisista laitteista, joilta voit käynnistää.

Määrittääksesi, mitä näppäintä sinun tulisi painaa varmistaaksesi, että sinulla on käynnistysvalikko, joka sallii sinun valita USB-tikun tavallisen kiintolevysi sijaan, tässä on ei-tyhjentävä lista valmistajittain:

| Valmistaja | Näppäin          |
| ---------- | ---------------- |
| Acer       | F12, F9, F2, Esc |
| Apple      | Option           |
| Asus       | Esc              |
| Clevo      | F7               |
| Dell       | F12              |
| Fujitsu    | F12, Esc         |
| HP         | F9               |
| Huawei     | F12              |
| Intel      | F10              |
| Lenovo     | F12              |
| MSI        | F11              |
| Samsung    | Esc, F12, F2     |
| Sony       | F11, Esc, F10    |
| Toshiba    | F12              |
| muut...    | F12, Esc         |

Kun USB-tikku on valittu, sinun pitäisi nähdä tämä uusi käynnistysnäyttö, mikä on erittäin hyvä merkki, joten anna tietokoneen jatkaa käynnistymistä...

![kuva](assets/5.webp)

## Vaihe 5: Tervetuloa Tailsiin!

![kuva](assets/6.webp)

> 🔗 Virallinen Tails-osio: https://tails.net/install/linux/index.en.html#tails

Yhden tai kahden minuutin kuluttua käynnistyslataimesta ja latausnäytöstä, Tervetuloa-näyttö ilmestyy.

![kuva](assets/7.webp)

Tervetuloa-näytössä, valitse kielesi ja näppäimistöasettelusi Kielialue-osiosta. Klikkaa Aloita Tails.

![kuva](assets/8.webp)
Jos tietokoneesi ei ole kytketty verkkoon kaapelilla, katso viralliset Tails-ohjeet, jotka auttavat sinua yhdistämään verkkoon ilman Wi-Fiä (osio "Testaa Wi-Fi").
Kun olet yhdistänyt paikalliseen verkkoon, Tor-yhteysvelho avautuu auttaakseen sinua yhdistämään Tor-verkkoon.

![kuva](assets/9.webp)

Voit aloittaa nimettömän selaamisen, tutkia Tailsiin sisältyviä vaihtoehtoja ja ohjelmistoja. Nauti, sinulla on runsaasti tilaa virheille, sillä USB-tikulle ei tehdä muutoksia... Seuraava uudelleenkäynnistyksesi unohtaa kaikki kokemuksesi!

## Tulevassa oppaassa...

Kun olet kokeillut hieman enemmän omaa Tails USB-tikkua, tutkimme toisessa artikkelissa muita edistyneempiä aiheita, kuten:

> Päivitä avain Tailsin uusimpaan versioon; Määritä ja käytä pysyvää tallennustilaa; Asenna lisäohjelmistoja.
> Siihen asti, kuten aina, jos sinulla on kysyttävää, voit jakaa ne Agora256-yhteisön kanssa. Opimme yhdessä olemaan huomenna parempia kuin tänään!