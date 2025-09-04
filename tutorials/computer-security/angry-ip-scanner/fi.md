---
name: Vihainen IP-skanneri
description: Yksinkertainen tapa skannata verkko
---
![cover](assets/cover.webp)



___



*Tämä opetusohjelma perustuu Florian BURNELin alkuperäiseen sisältöön, joka on julkaistu osoitteessa [IT-Connect](https://www.it-connect.fr/). Lisenssi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Alkuperäiseen tekstiin on saatettu tehdä muutoksia.*



___



## I. Esittely



Miten Windows-verkossa olevat koneet voidaan skannata nopeasti ja helposti? Vastaus on Angry IP Scanner. Tämän avoimen lähdekoodin projektin avulla voit skannata verkon helposti helppokäyttöisen graafisen Interface:n avulla.



Yksityishenkilöt voivat käyttää tätä työkalua **skannaamaan lähiverkkoa**, mutta myös IT-ammattilaiset voivat käyttää sitä samaan tarkoitukseen. Todisteena siitä, että **työkalu on erittäin käytännöllinen**, on se, että **jotkut tietoverkkorikollisryhmät** ovat jo käyttäneet sitä yritysverkkojen skannaamiseen (samalla tavalla kuin Nmap). Hyvä esimerkki on [ransomware-ryhmä RansomHub](https://www.it-connect.fr/deja-210-victimes-pour-le-groupe-de-ransomware-ransomhub-lance-en-fevrier-2024/). Se on edelleen hyvä ohjelmisto, mutta kuten muitakin verkko- ja tietoturvapainotteisia työkaluja, sen käyttöä voidaan käyttää väärin.



Tässä käytämme sitä **Windows 11**:ssä, mutta sitä on täysin mahdollista käyttää myös muissa **Windows-versioissa** sekä **Linuxissa** ja **macOS:ssä**.



**Angry IP** Scanner ei ole yhtä kattava kuin Nmap, mutta se on silti mielenkiintoinen nopean perusverkkoanalyysin kannalta, mutta myös siksi, että se on kaikkien ulottuvilla. Se **havaitsee verkkoon liitetyt isännät** ja tunnistaa **isännän nimet** ja **avoimet portit**.



Jos haluat mennä pidemmälle, katso Nmapin opetusohjelma:



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

## II. Angry IP Scannerin käytön aloittaminen



### A. Lataa ja asenna Angry IP Scanner



Voit ladata Angry IP Scannerin uusimman version sovelluksen viralliselta verkkosivustolta tai GitHubista. Käytämme jälkimmäistä vaihtoehtoa. Klikkaa alla olevaa linkkiä ja lataa EXE-versio: "**ipscan-3.9.1-setup.exe**".





- [Angry IP Scanner GitHub](https://github.com/angryip/ipscan/releases/latest)



![Image](assets/fr/016.webp)



Suorita suoritettava ohjelma jatkaaksesi asennusta. Asennuksen aikana ei ole mitään erityistä tehtävää.



![Image](assets/fr/013.webp)



### B. Suorita alustava verkkotarkistus



Kun käynnistät työkalun ensimmäistä kertaa, lue ohjeet "**Aloittaminen**"-ikkunassa, jotta saat lisätietoja työkalun toiminnasta. Muuten, on useita termejä, jotka on otettava huomioon:





- Feeder**: moduuli, joka vastaa skannattavien IP-osoitteiden luetteloiden luomisesta satunnaisesta IP-alueesta tai IP-osoitteiden luettelon sisältävästä tiedostosta.
- Fetcher**: joukko moduuleja, joilla haetaan tietoa verkossa olevista isännistä. On esimerkiksi noutajia MAC-osoitteiden havaitsemiseen, porttien skannaamiseen, isännän nimien havaitsemiseen tai HTTP-pyyntöjen lähettämiseen.



![Image](assets/fr/018.webp)



Jos haluat skannata IP-aliverkon, kirjoita **alku IP Address** ja **loppu IP Address** kenttään "**IP-alue**" (muutoin vaihda tyyppi oikealla). Napsauta sitten "**Start**"-painiketta.



![Image](assets/fr/019.webp)



Muutamia kymmeniä sekunteja myöhemmin tulos näkyy ohjelmiston Interface:ssa. **Kunkin analysoidun alueen IP Address:n kohdalla näet, onko Angry IP Scanner havainnut isännän vai ei.** Näytöllä näkyy myös yhteenveto, jossa ilmoitetaan aktiivisten isäntien määrä (tässä tapauksessa 6) ja niiden isäntien määrä, joilla on avoimet portit.



![Image](assets/fr/020.webp)



Tässä näkyy isäntä nimeltä "**OPNsense.local.domain**", joka on liitetty IP Address:ään "**192.168.10.1**" ja johon pääsee **porttien 80** ja **443** kautta (HTTP ja HTTPS). Napsauttamalla isäntää hiiren kakkospainikkeella pääsee käyttämään lisäkomentoja, kuten pingausta, reitin jäljittämistä ja selaimen avaamista tämän IP Address:n kautta.



![Image](assets/fr/012.webp)



### C. Lisää skannausportteja



Oletusarvoisesti **Angry IP Scanner** skannaa 3 porttia: **80** (HTTP), **443** (HTTPS) ja **8080**. Voit lisätä lisää skannattavia portteja sovelluksen asetuksista. Napsauta "**Tools**"-valikkoa ja sitten "**Ports**"-välilehteä.



Täällä voit muokata porttiluetteloa "**Portin valinta**"-vaihtoehdon avulla. Voit **ilmoittaa tietyt, pilkulla erotetut porttinumerot tai porttialueet**. Alla olevassa esimerkissä lisätään kaksi porttia: **445** (SMB) ja **389** (LDAP). Jos haluat skannata portteja 1-1000, kirjoita "**1-1000**". Ei määritetä, suoritetaanko porttiskannaus TCP:ssä, UDP:ssä vai molemmissa.



![Image](assets/fr/021.webp)



Jos suoritat tarkistuksen uudelleen, saat todennäköisesti uusia tietoja. Alla olevassa esimerkissä Angry IP Scanner kertoo, että portit 389 ja 445 ovat avoinna isännillä "**SRV-ADDS-01**" ja "**SRV-ADDS-02**", kiitos tarkistettavien porttien uuden määrityksen.



![Image](assets/fr/022.webp)



**Huomautus**: voit viedä skannaustulokset tekstitiedostoon "**Skanneri**"-valikosta.



Jos haluat viedä skannausta pidemmälle, napsauta "**Työkalut**"-valikkoa ja napsauta sitten "**Noutajat**". Tämä lisää skannaukseen "ominaisuuksia". Valitse noutaja ja siirrä se vasemmalle aktivoidaksesi sen. Tämä lisää ylimääräisen sarakkeen skannaustulokseen.



![Image](assets/fr/014.webp)



Alla olevassa esimerkissä näytetään toiminnot "**NetBIOS info**" ja "**Web detection**". Edellinen antaa lisätietoja, kuten koneen MAC Address ja verkkotunnus, kun taas jälkimmäinen näyttää verkkosivun otsikon (joka voi antaa viitteitä verkkopalvelimen tai -sovelluksen tyypistä).



![Image](assets/fr/011.webp)



Lopuksi voit myös muuttaa asetuksista "**ping**"-menetelmää, eli sitä, onko isäntä aktiivinen vai ei. Koska jotkin isännät eivät vastaa pingauksiin, voit kokeilla muita menetelmiä (UDP-paketti, TCP-porttiprobe, ARP, UDP + TCP -yhdistelmä jne.).



## III. Päätelmät



Yksinkertainen ja tehokas: Angry IP Scanner havaitsee verkkoon liitetyt isännät, ja voit määrittää porttiskannaukset. Vaihtoehtojen osalta se ei ole yhtä joustava kuin Nmap, eikä se mene yhtä pitkälle, mutta se on hyvä alku nopeaan skannaukseen.



Jos haluat käyttää **Nmapia** graafisella Interface:lla, voit käyttää **Zenmap-sovellusta** (katso yleiskatsaus alla).



![Image](assets/fr/015.webp)



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d