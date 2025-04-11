---
name: Jade

description: Kuinka asennat JADE-laitteesi
---

![kuva](assets/cover.webp)

## Tutoriaalivideo

![video](https://www.youtube.com/watch?v=_U1jsTeqbTw)
Blockstream Jade - Mobiili Bitcoin-laitteistolompakko KOKO OPAS BTCsessionin toimesta

## Koko kirjoitusopas

![kuva](assets/cover2.webp)

### Esivaatimukset

1. Lataa Blockstream Greenin uusin versio.

2. Asenna tämä ajuri varmistaaksesi, että tietokoneesi tunnistaa Jaden.

### Työpöytäasetus

![täysi opas](https://youtu.be/0fPVzsyL360)

Avaa Blockstream Green ja klikkaa Blockstream-logoa Laitteet-osiosta.

![kuva](assets/1.webp)

Yhdistä Jade tietokoneeseesi mukana toimitetulla USB-kaapelilla.

> Huomio: Jos Jadea ei tunnisteta tietokoneellasi, varmista että olet ladannut ajurin, joka löytyy tästä oppaasta.

Kun Jadesi ilmestyy Greeniin, päivitä Jade klikkaamalla Tarkista päivitykset ja valitse uusin laiteohjelmiston versio. Käytä Jaden rullaa tai vaihtokytkintä vahvistaaksesi ja jatkaaksesi päivityksen kanssa. Varmista, että Jadesi näyttää edelleen "Alusta" -painikkeen, muuten sinun on odotettava Jaden asetuksen jälkeen päivittääksesi sen. Käytä tarvittaessa takaisin-painiketta päästäksesi tähän näyttöön.

![kuva](assets/2.webp)

Kun olet päivittänyt Jaden laiteohjelmiston, valitse Aseta Jade käyttöön valitsemallasi verkko- ja turvallisuuspolitiikalla.

> Vinkki: Turvallisuuspolitiikka on lueteltu Tyypin alla kirjautumisnäytössä alla. Jos et ole varma, valitsetko Singlesig vai Multisig Shield, tutustu oppaaseemme täällä. (https://help.blockstream.com/hc/en-us/articles/4403642609433)

![kuva](assets/3.webp)

Seuraavaksi valitse luoda Uusi lompakko ja valitse 12 sanaa luodaksesi palautusfraasisi. Klikkaamalla Lisäasetukset saat vaihtoehdon 12 ja 24 sanan palautusfraasille.

![kuva](assets/4.webp)

Kirjaa palautusfraasi paperille offline-tilassa (tai käyttämällä erillistä palautusfraasin varmuuskopiointilaitetta lisäturvallisuuden vuoksi). Käytä sitten Jaden rullaa tai vaihtokytkintä varmistaaksesi palautusfraasisi. Tämä vaihe varmistaa, että olet kirjoittanut sen oikein.

![kuva](assets/5.webp)

Aseta ja vahvista kuusinumeroinen PIN-koodisi. Tätä käytetään Blockstream Jaden lukituksen avaamiseen joka kerta, kun kirjaudut lompakkoosi.

![kuva](assets/6.webp)

Nyt valitse vain Siirry lompakkoon Greenin työpöytäsovelluksessa ja näet lompakkosi avautuvan Blockstream Greenissä. Blockstream Jade näyttää myös, että se on Valmis! Voit nyt käyttää Jadeasi lähettääksesi ja vastaanottaaksesi Bitcoin-siirtoja.

![kuva](assets/7.webp)

Kun olet lopettanut lompakkosi käytön, irrota Blockstream Jadesi laitteestasi. Kun haluat käyttää lompakkoa Blockstream Jadessa seuraavan kerran, yhdistä laitteesi uudelleen ja noudata kehotteita.

lähde: https://help.blockstream.com/hc/en-us/articles/17478506300825

### Liite A - Green-lompakon lataustiedoston varmentaminen

Latauksen varmentaminen tarkoittaa tarkistamista, että ladattu tiedosto ei ole muuttunut kehittäjän julkaisemisen jälkeen.

Teemme tämän tarkistamalla, että kehittäjän yksityisellä avaimella tuotettu allekirjoitus yhdessä ladatun tiedoston ja kehittäjän julkisen avaimen kanssa palauttaa TOTTA-tuloksen suoritettaessa gpg –verify -toimintoa. Näytän sinulle, miten tehdä se seuraavaksi. Jos haluat oppia tämän taustat, minulla on tämä opas ja tämä.

Ensimmäiseksi, hankimme allekirjoitusavaimen:
Linuxille, avaa terminaali ja suorita tämä komento (sinun tulisi vain kopioida ja liittää teksti, ja sisällyttää lainausmerkit):
```bash
gpg --keyserver keyserver.ubuntu.com --recv-keys "04BE BF2E 35A2 AF2F FDF1 FA5D E7F0 54AA 2E76 E792"
```

Macille, tee sama asia, paitsi sinun täytyy ensin ladata ja asentaa GPG Suite.

Windowsille, tee sama asia, paitsi sinun täytyy ensin ladata ja asentaa GPG4Win.

Saat tulosteen, joka kertoo julkisen avaimen tuodun.

![kuva](assets/9.webp)

Tämän kuvan alt-attribuutti on tyhjä; sen tiedostonimi on image-3-1024x162.webp

Seuraavaksi meidän tarvitsee hankkia tiedosto, joka sisältää ohjelmiston hash-arvon. Se on tallennettu Blockstreamin GitHub-sivulle. Mene ensin heidän info-sivulleen täällä, ja klikkaa linkkiä "desktop". Se vie sinut GitHubin viimeisimmän version sivulle, ja siellä näet linkin SHA256SUMS.asc-tiedostoon, joka on tekstidokumentti sisältäen Blockstreamin julkaiseman ohjelman hash-arvon, jonka latasimme.

![kuva](assets/10.webp)

GitHub:

![kuva](assets/11.webp)

Ei ole välttämätöntä, mutta tallennuksen jälkeen nimesin "SHA256SUMS.asc" uudelleen muotoon "SHA256.txt", jotta tiedoston voisi helpommin avata Macilla tekstieditorilla. Tämä oli tiedoston sisältö:

![kuva](assets/12.webp)

Etsimämme teksti on ylhäällä. Riippuen siitä, minkä tiedoston latasimme, on olemassa vastaava hash-tuloste, jota vertaamme myöhemmin.

Dokumentin alaosa sisältää viestin yläpuolella tehdyn allekirjoituksen – se on kaksi yhdessä tiedostossa.

Järjestyksellä ei ole väliä, mutta ennen hashin tarkistamista, aiomme varmistaa, että hash-viesti on aito (eli sitä ei ole manipuloitu).

Avaa terminaali. Sinun täytyy olla oikeassa hakemistossa, johon SHA256SUMS.asc-tiedosto ladattiin. Olettaen, että latasit sen "Lataukset"-hakemistoon, Linuxille ja Macille, vaihda hakemistoon näin (kirjainkoko on merkityksellinen):

```bash
cd Downloads
```

Tietenkin sinun täytyy painaa <enter> näiden komentojen jälkeen. Windowsille, avaa CMD (komentokehote), ja kirjoita sama asia (vaikka kirjainkoko ei ole merkityksellinen).

Windowsille ja Macille, sinun olisi jo pitänyt ladata GPG4Win ja GPG Suite, kuten aiemmin ohjeistettiin. Linuxille, gpg tulee käyttöjärjestelmän mukana. Terminaalista (tai CMD:stä Windowsille), kirjoita tämä komento:

```bash
gpg --verify SHA256SUMS.asc
```

Tiedostonimen tarkka kirjoitusasu (punaisella) voi olla erilainen sinä päivänä, kun haet tiedoston, joten varmista, että komento vastaa ladattua tiedostonimeä. Sinun pitäisi saada tämä tuloste, ja voit jättää huomiotta varoituksen luotetusta allekirjoituksesta – se vain tarkoittaa, että et ole manuaalisesti ilmoittanut tietokoneelle luottavasi aiemmin tuotuun julkiseen avaimeseen.

![kuva](assets/13.webp)

Tämä kuva vahvistaa allekirjoituksen olevan hyvä, ja voimme olla varmoja, että yksityinen avain "info@greenaddress.it" on allekirjoittanut tiedot (hash-raportin).
Nyt meidän tulisi tiivistää ladattu zip-tiedosto ja verrata tulosta julkaistuun. Huomaa, että SHA256SUMS.asc-tiedostossa on tekstinpätkä, joka sanoo "Hash: SHA512", mikä hämmentää minua, sillä tiedosto sisältää selvästi SHA256-tulosteita, joten aion jättää sen huomiotta.
Macille ja Linuxille, avaa terminaali, siirry siihen kansioon, johon zip-tiedosto on ladattu (todennäköisesti sinun täytyy kirjoittaa "cd Downloads" uudelleen, ellet ole sulkenut terminaalia siitä). Muuten voit aina tarkistaa, missä hakemistossa olet kirjoittamalla PWD ("print working directory"), ja jos tämä kaikki on sinulle vierasta, on hyödyllistä katsoa nopea YouTube-video hakemalla "how to navigate the Linux/Mac/Windows file system".

Tiedoston tiivistämiseksi, kirjoita tämä:

```bash
shasum -a 256 BlockstreamGreen_MacOS_x86_64.zip
```

Sinun tulisi tarkistaa, mitä tiedostoasi kutsutaan tarkalleen, ja muuttaa yllä olevaa sinisellä merkittyä tekstiä tarvittaessa.

Saat tuloksen kuten tämä (sinun tuloksesi eroaa, jos tiedosto on erilainen kuin minun):

![kuva](assets/14.webp)

Vertaa seuraavaksi visuaalisesti tiivisteen tulostetta siihen, mitä SHA256SUMS.asc-tiedostossa on. Jos ne täsmäävät, silloin –> ONNISTUMINEN! Onneksi olkoon.

lähde: https://armantheparman.com/jade/

### Käyttäen sitä Sparrow'ssa

Jos tiedät jo, miten Sparrow'ta käytetään, niin se on kuten aina:

> Huom: prosessi on sama esimerkiksi Specter'n kanssa

Lataa Sparrow käyttäen tässä annettua linkkiä.

![kuva](assets/14.5.webp)

Klikkaa Seuraava seurataksesi asennusopasta ja oppiaksesi eri yhteysvaihtoehdoista.

![kuva](assets/15.webp)

Valitse haluamasi palvelin ja valitse Luo Uusi Lompakko.

![kuva](assets/16.webp)

Anna lompakollesi nimi ja klikkaa Luo Lompakko.

![kuva](assets/17.webp)

Valitse haluamasi politiikka ja skriptityypit ja valitse Yhdistetty Laitteistolompakko.

> Huom: Jos olet aiemmin käyttänyt Blockstream Jadea Singlesig-lompakkona Blockstream Greenin kanssa ja haluaisit nähdä tapahtumasi Sparrow'ssa, varmista, että skriptityyppi vastaa Greenissä olevien varojesi tilin tyyppiä. Sinun on myös varmistettava, että johdannaispolku täsmää.

![kuva](assets/18.webp)

Kytke Blockstream Jade ja klikkaa Skannaa. Sinua pyydetään sen jälkeen syöttämään PIN-koodisi Jadeen.

> Vinkki: Ennen kuin yhdistät Jaden, varmista, että Blockstream Green -sovellus ei ole avoinna. Jos Green on avoinna, se saattaa aiheuttaa ongelmia Jaden tunnistamisessa Sparrow'ssa.

![kuva](assets/19.webp)

Valitse Tuo Avainvarasto tuodaksesi oletustilin julkisen avaimen, tai valitse nuoli manuaalisesti valitaksesi haluamasi johdannaispolun.

![kuva](assets/20.webp)

Kun haluamasi avain on tuotu, klikkaa Käytä.

![kuva](assets/21.webp)

Olet nyt onnistuneesti asettanut lompakkosi ja voit aloittaa bitcoinien vastaanottamisen, säilyttämisen ja käyttämisen Sparrow'n ja Blockstream Jaden avulla.

> Huom: Jos olit aiemmin käyttänyt Jadea Blockstream Greenin kanssa Multisig Shield -lompakkona, älä odota, että uusi Sparrow-lompakkosi näyttäisi saman saldon - nämä ovat eri lompakoita. Päästäksesi käsiksi Multisig Shield -lompakkoosi uudelleen, yhdistä Jade vain takaisin Blockstream Greeniin.

![kuva](assets/22.webp)

lähde: https://help.blockstream.com/hc/en-us/articles/7559912660761-How-do-I-use-Blockstream-Jade-with-Sparrow-

### green app
Jos olet enemmän mobiiliopas, voit käyttää sitä yhdessä Blockstream Greenin kanssa
- Kuinka ottaa käyttöön Blockstream Jade Greenin kanssa | Blockstream Jade - https://youtu.be/7aacxnc6DHg

- Kuinka vastaanottaa bitcoineja Jade-lompakkoon | Blockstream Jade - https://youtu.be/CVtcDdiPqLA