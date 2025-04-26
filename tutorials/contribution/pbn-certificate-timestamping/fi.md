---
name: Plan ₿ -verkon todistusten ja diplomien aikaleimaus
description: Ymmärrä, miten Plan ₿ -verkko myöntää vahvistettavissa olevan todistuksen sertifikaateillesi ja diplomeillesi
---

![kansi](assets/cover.webp)

Jos luet tätä, on suuri todennäköisyys, että olet saanut joko Bitcoin-sertifikaatin tai suoritustodistuksen joltakin Plan B -verkon kurssilta, joten onnittelut tästä saavutuksesta!

Tässä oppaassa käymme läpi, miten Plan B -verkko myöntää vahvistettavissa olevan todistuksen Bitcoin-sertifikaatistasi tai mistä tahansa kurssin suoritustodistuksesta. Toisessa osassa näemme, miten näiden todisteiden aitouden voi varmistaa.

# Plan B -verkon todistusmekanismi

Plan ₿ -verkossa tarjoamme sinulle sertifikaatteja ja diplomeja, jotka on kryptografisesti allekirjoitettu meidän toimestamme ja aikaleimattu Timechainiin (eli Bitcoin-lohkoketjuun). Tämän saavuttamiseksi meidän piti kehittää todistusmekanismi, joka perustuu kahteen kryptografiseen toimenpiteeseen:

1. GPG-allekirjoitus tekstiedostoon, joka tiivistää saavutuksesi
2. Allekirjoitetun tiedoston aikaleimaus [opentimestamps](https://opentimestamps.org/)-palvelun kautta.

Käytännössä ensimmäinen toimenpide mahdollistaa sen, että voit varmistaa, kuka on myöntänyt sertifikaatin (tai diplomin), kun taas toinen toimenpide mahdollistaa sen, että voit varmistaa, milloin se on myönnetty.
Uskomme, että tämä yksinkertainen todistusmekanismi mahdollistaa meidän myöntää sertifikaatteja ja diplomeja kiistattomin todistein, joita kuka tahansa voi itse varmistaa.

![image](./assets/proof-mechanism.webp)

Huomaa, että tämän todistusmekanismin ansiosta minkä tahansa sertifikaatin tai diplomin pieninkin yksityiskohdan muuttaminen luo täysin erilaisen sha256-tiivisteen allekirjoitetusta tiedostosta, mikä paljastaisi välittömästi manipuloinnin, koska allekirjoitus ja aikaleimaus eivät enää olisi päteviä. Lisäksi, jos joku yrittää pahantahtoisesti väärentää sertifikaatteja tai diplomeja Plan B -verkon nimissä, allekirjoituksen yksinkertainen varmistaminen paljastaisi petoksen.

## Miten GPG-allekirjoitus toimii?

GPG-allekirjoitus saadaan käyttämällä avoimen lähdekoodin ohjelmistoa nimeltä GNU Private Guard. Tämä ohjelmisto mahdollistaa kenen tahansa luoda helposti yksityisiä avaimia, allekirjoittaa ja varmistaa allekirjoituksia sekä salata ja purkaa tiedostojen salauksen. Tämän oppaan tarkoituksessa tiedä, että Plan B -verkko käyttää GPG:tä luodakseen oman yksityisen/julkisen avaimensa ja allekirjoittaakseen minkä tahansa Bitcoin-sertifikaatin tai kurssin suoritustodistuksen.

Toisaalta, jos joku haluaa varmistaa allekirjoitetun tiedoston aitouden, hän voi käyttää GPG:tä tuodakseen myöntäjän julkisen avaimen ja varmistaakseen sen. Oppaan toisessa osassa näemme, miten tämä tehdään terminaalissa.

Niille, jotka ovat uteliaita ja haluavat oppia lisää tästä fantastisesta ohjelmistosta, voitte viitata ["The GNU Privacy Handbook"](https://www.gnupg.org/gph/en/manual/x135.html)

## Miten aikaleimaus toimii?

Kuka tahansa voi käyttää OpenTimestampsia aikaleimatakseen tiedoston ja saadakseen vahvistettavissa olevan todistuksen tiedoston olemassaolosta. Toisin sanoen, se ei tarjoa sinulle todistusta siitä, milloin tiedosto on luotu, vaan todistuksen olemassaolosta viimeistään tiettynä hetkenä.
OpenTimestamps pystyy tarjoamaan tämän palvelun ilmaiseksi kiitos erittäin tehokkaan tavan tallentaa tällainen todiste Bitcoin-lohkoketjuun. Se käyttää tiedoston sha256-tiivistettä tiedoston yksilöllisenä tunnisteena ja rakentaa merkle-puun muiden käyttäjien toimittamien tiedostojen tiivisteistä ja ankkuroi vain Merkle-puun rakenteen tiivisteen OpReturn-transaktioon.
Kun tämä transaktio on jossakin lohkossa, kuka tahansa alkuperäisen tiedoston ja siihen liittyvän `.ots`-tiedoston kanssa voi varmistaa aikaleiman aitouden. Tutoriaalin toisessa osassa näemme, miten voit varmistaa Bitcoin-sertifikaattisi tai minkä tahansa kurssin suoritustodistuksen aitouden terminaalin kautta ja graafisen käyttöliittymän kautta OpenTimestamps-verkkosivustolla.
# Kuinka varmistaa Plan B Network -sertifikaatti tai -diplomi

## Vaihe 1. Lataa sertifikaattisi tai diplomi

Kirjaudu henkilökohtaiseen PBN-kojelautaasi.

![image](./assets/login.webp)

Siirry Todistukset-sivulle napsauttamalla vasemmanpuoleista valikkoa ja valitse tenttisi istunto tai suoritustodistuksesi.

![image](./assets/credential.webp)

Lataa zip-tiedosto.

![image](./assets/download.webp)

Pura sisältö napsauttamalla oikealla `.zip`-tiedostoa ja valitsemalla "Pura". Löydät sisältä kolme eri tiedostoa:

- Allekirjoitettu tekstiedosto (esim., certificate.txt)
- Avoin aikaleima (OTS) tiedosto (esim., certificate.txt.ots)
- PDF-sertifikaatti (esim., certificate.pdf)

## Vaihe 2: Tekstitiedoston allekirjoituksen varmistaminen

Avaa ensin terminaali kansiossa, jossa tiedostot ovat (napsauttamalla kansioiden ikkunaa oikealla ja valitsemalla "Avaa terminaalissa"). Seuraa sitten alla olevia ohjeita

1. Tuo Plan ₿ Networkin julkinen PGP-avain seuraavalla komennolla:

```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```

Jos PGP-avaimen tuonti onnistui, näet viestin kuten seuraava

```
gpg: key 8F12D0C63B1A606E: julkinen avain "PlanB Network (käytetään PBN-alustalla) <admin@planb.network>" tuotu
gpg: Käsitelty yhteensä: 1
gpg:               tuotu: 1
```

HUOM: jos näet, että 1 avain on käsitelty ja 0 tuotu, todennäköisesti olet jo aiemmin tuonut saman avaimen, ja se on kunnossa.

2. Varmista sertifikaatin tai diplomin allekirjoitus seuraavalla komennolla:

```bash
gpg --verify certificate.txt
```

Tämä komento näyttää sinulle yksityiskohdat allekirjoituksesta, mukaan lukien:

- Kuka sen allekirjoitti (Plan ₿ Network)
- Milloin se allekirjoitettiin
- Onko allekirjoitus voimassa

Tässä on esimerkki tuloksesta:

```
gpg: Allekirjoitus tehty ma 11 marras 2024, 00:39:04 CET
gpg:                käyttäen RSA-avainta 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                lähettäjä "admin@planb.network"
gpg: Hyvä allekirjoitus "PlanB Network (käytetään PBN-alustalla) <admin@planb.network>" [tuntematon]
```

Jos näet viestin kuten "HUONO allekirjoitus", se tarkoittaa, että tiedostoa on muutettu.

## Vaihe 3: Avoin aikaleiman varmistaminen

### Varmistaminen graafisen käyttöliittymän kautta

1. Vieraile OpenTimestamps-verkkosivustolla: https://opentimestamps.org/
2. Napsauta "Stamp & Verify" -välilehteä.
3. Vedä ja pudota OTS-tiedosto (esim., `certificate.txt.ots`) määritettyyn alueeseen.
4. Vedä ja pudota aikaleimattu tiedosto (esim. `certificate.txt`) määritettyyn alueeseen.
5. Verkkosivusto varmistaa automaattisesti avoimen aikaleiman ja näyttää tuloksen.

Jos näet viestin kuten seuraava, aikaleimasi on voimassa:
![cover](assets/opentimestamp_wegui_verified.webp)
### CLI-menetelmä

HUOM: tämä menettely **vaatii paikallisen Bitcoin-noden käynnissä olemisen**

1. Asenna OpenTimestamps-asiakasohjelma virallisesta repositoriosta: https://github.com/opentimestamps/opentimestamps-client suorittamalla seuraava komento:

```
pip install opentimestamps-client
```

2. Siirry hakemistoon, joka sisältää puretut sertifikaattitiedostot.

3. Suorita seuraava komento avoimen aikaleiman vahvistamiseksi:

```
ots verify certificate.txt.ots
```

Tämä komento:

- Tarkistaa aikaleiman Bitcoinin lohkoketjua vasten
- Näyttää sinulle, milloin tiedosto on tarkalleen aikaleimattu
- Vahvistaa aikaleiman aitouden

### Lopputulokset

Huomaa, että vahvistus on onnistunut, jos **molemmat** viestit näytetään:

1. GPG-allekirjoituksen kerrotaan olevan **"Hyvä allekirjoitus Plan ₿ Networkilta"**
2. OpenTimestamps-vahvistus näyttää tietyn Bitcoin-lohkon aikaleiman ja raportoi **"Onnistui! Bitcoin-lohko [lohkonkorkeus] todistaa, että data oli olemassa [aikaleima]"**

Nyt kun tiedät, miten Plan B Network myöntää vahvistettavissa olevan todistuksen mille tahansa Bitcoin-sertifikaatille ja kurssin suoritustodistukselle, voit helposti varmistaa sen eheyden.