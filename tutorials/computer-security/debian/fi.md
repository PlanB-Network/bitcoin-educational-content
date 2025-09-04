---
name: Debian
description: Linux-jakelu, joka on tunnettu vakaudestaan, kestävyydestään ja yhteensopivuudestaan.
---

![cover](assets/cover.webp)



Debian on vapaa GNU/Linux-jakelu, joka on tunnettu vankkuudestaan ja luotettavuudestaan. Sen Linux-ydin ja kaikki paketit on testattu tiukasti, jotta varmistetaan vankka vakaus ja korkea turvallisuustaso. Debian soveltuu sekä palvelimille että työasemille, ja se tarjoaa helppokäyttöisen käyttökokemuksen ja laajan ohjelmistoluettelon. Etsitpä sitten turvallista järjestelmää jokapäiväiseen käyttöön tai tuotantoympäristöön, Debian on oikea valinta.



## Miksi valita Debian?





- Ilmainen ja avoin**: Debian on täysin avoimen lähdekoodin järjestelmä, joka takaa avoimuuden eikä lisenssimaksuja.
- Vakaus ja turvallisuus**: Jokainen julkaisu käy läpi perusteellisen testausprosessin, mikä tekee Debianista yhden markkinoiden luotettavimmista ja turvallisimmista jakeluista.
- Aktiivinen yhteisö**: laaja yhteisö ja laaja dokumentaatio ovat käytettävissäsi tukemaan sinua aina kun tarvitset sitä.
- Kevyt ja skaalautuva**: voit asentaa Debianin koneisiin, joilla on vaatimattomat resurssit, ja säilyttää samalla hyvän suorituskyvyn.
- Laaja ohjelmistoluettelo**: yli 50 000 virallista pakettia on saatavilla arkistojen kautta.



## Valitse Interface-grafiikka



Debian tarjoaa useita työpöytäympäristöjä tarpeidesi mukaan:





- GNOME**: moderni, intuitiivinen Interface, ihanteellinen aloittelijoille. Se tarjoaa sujuvan, helppokäyttöisen graafisen valikon sovellusten käyttämiseen.
- XFCE**: kevyt ja nopea, täydellinen vähemmän tehokkaille koneille.
- KDE Plasma**: hyvin muokattavissa, Windows-tyyppinen ulkoasu.
- Cinnamon**: yksinkertainen, tyylikäs Interface, joka on saanut vaikutteita Windowsista.
- LXDE / LXQt**: erittäin kevyt, sopii vanhemmille tietokoneille.
- MATE**: yksinkertainen ja klassinen, lähellä vanhaa GNOMEa.



💡 Mukavan ja helppokäyttöisen käyttökokemuksen takaamiseksi **GNOME on erittäin suositeltava**.



## Debianin asentaminen ja konfigurointi


### Laitteistovaatimukset



Varmista ennen asennuksen aloittamista, että sinulla on seuraavat laitteet:





- USB-avain**: vähintään 8 GB käynnistettävän ISO-kuvan tallentamiseen.
- RAM-muisti (Random Access Memory)**: 4 GB sujuvan asennuksen ja käytön varmistamiseksi.
- Levytila**: vähintään 15 Gt vapaata tilaa järjestelmää ja päivityksiä varten.



### Lataa



Debian-kuvan valinta riippuu prosessoriarkkitehtuuristasi:





- AMD64**: lataa "live hybrid" -versio [download]-luettelosta (https://debian.obspm.fr/debian-cd/12.11.0-live/amd64/iso-hybrid/).
- ARM64**: hae DVD-kuva viralliselta [Debian]-sivustolta (https://debian.obspm.fr/debian-cd/12.11.0/arm64/iso-dvd/).
- Muut arkkitehtuurit**: löydä arkkitehtuuriasi vastaava ISO [täältä](https://debian.obspm.fr/debian-cd/12.11.0/).



![download](assets/fr/01.webp)



### Käynnistettävän USB-avaimen luominen



Kun olet ladannut sopivan ISO-kuvan, voit luoda asennusmedian:




- Lataa Balena Etcher** [viralliselta verkkosivustolta](https://etcher.balena.io/), hae sitten järjestelmääsi sopiva binääri ja asenna se.



![etcher](assets/fr/02.webp)





- Käynnistä Etcher**: avaa ohjelmisto ja valitse aiemmin ladattu Debian-ISO-kuva.
- Valitse USB-tietolevy**: määritä USB-tietolevy (8 Gt tai enemmän) kohteeksi.
- Käynnistä flash**: napsauta **Flash!** ja odota, kunnes prosessi on valmis.



![flash](assets/fr/03.webp)



USB-levysi on nyt valmis aloittamaan Debianin asentamisen.



## Debianin asentaminen järjestelmääsi



### Käynnistäminen USB-muistitikulta



Asennuksen käynnistäminen USB-muistitikulta:




- Sammuta** tietokone kokonaan.
- Käynnistä uudelleen** ja avaa BIOS/UEFI painamalla välittömästi `ESC`, `F2`, `F11` (tai erityistä näppäintä merkistä riippuen).
- Valitse käynnistysvalikosta **valitsemalla käynnistyslaitteeksi USB-levy**.
- Vahvista** Enter-näppäimellä käynnistääksesi Debian-kuvan: tämä vie sinut asennusohjelman tervetuloruutuun.



### Asennuksen käynnistäminen



Aloitusnäyttö:



![starting](assets/fr/04.webp)



Kun käynnistät USB-tikulta, Debianin tervetuliaisnäyttö tarjoaa useita vaihtoehtoja:




- Live System**: käynnistää Debianin asentamatta sitä, ihanteellinen ympäristön testaamiseen.
- Start Installer**: käynnistää asennuksen suoraan Hard-levylle.
- Lisäasennusasetukset**: antaa sinulle pääsyn mukautettuihin asennustiloihin.



Tutustu Debianiin live-tilassa valitsemalla **Live System** ja vahvistamalla **Enter**. Tämän jälkeen voit käynnistää asennuksen napsauttamalla **Asenna Debian** live-ympäristössä.



![system](assets/fr/05.webp)





- Kielen valinta** (valinnainen)



Valitse luettelosta Debian-järjestelmäsi pääkieli ja napsauta sitten OK.



![language](assets/fr/06.webp)





- Aikavyöhyke** (GMT)



Valitse maantieteellinen vyöhykkeesi, jotta päivämäärä ja kellonaika asetetaan automaattisesti.



![timezone](assets/fr/07.webp)





- Näppäimistön asettelu



Valitse näppäimistön kieli ja asettelu. Tarkista sisäänrakennetun testikentän avulla, että jokainen näppäin tuottaa odotetun merkin.



![keyboard](assets/fr/08.webp)



### Levyn osiointi





- Erase disk**: Jos sinulla on oma osio, tämä vaihtoehto poistaa sen koko sisällön.
- Manuaalinen osiointi**: Valitse tämä vaihtoehto, kun haluat luoda, muuttaa kokoa tai poistaa osioita tarpeen mukaan.



![disk](assets/fr/09.webp)





- Käyttäjätilin luominen



Kirjoita koko nimesi, tilisi nimi ja vahva salasana, jotta istuntosi on turvallinen.



![user](assets/fr/10.webp)





- Parametrien yhteenveto**



Näyttöön tulee yhteenveto valinnoistasi: tarkista jokainen kohta ja palaa tarvittaessa muuttamaan sitä.



![settings](assets/fr/11.webp)





- Asennuksen käynnistäminen



Napsauta **Asenna** aloittaaksesi tiedostojen kopioinnin ja järjestelmän määrityksen ja odota sitten, kunnes prosessi on valmis.



![install](assets/fr/12.webp)





- Uudelleenkäynnistys**



Kun asennus on valmis, käynnistä tietokone uudelleen soveltaaksesi kaikkia asetuksia ja käyttääksesi uutta Debian-järjestelmääsi.



![restart](assets/fr/13.webp)



Syötä käynnistyksen yhteydessä käyttäjätunnus ja salasana, joilla pääset järjestelmään.



![login](assets/fr/14.webp)



## Järjestelmäpäivitys



Ennen kuin alat käyttää järjestelmääsi, on tärkeää päivittää se. Näin voit hyödyntää uusimpia ohjelmistokorjauksia, ajantasaisia arkistoja ja joissakin tapauksissa itse käyttöjärjestelmän tietoturvakorjauksia.



### Vaihtoehto 1: Päivitys graafisen Interface:n (GNOME) kautta



Jos olet asentanut Debianin GNOME-työpöytäympäristön kanssa, voit tehdä päivitykset graafisesti. Avaa **Ohjelmisto**-sovellus ja siirry sitten **Päivitykset**-välilehdelle. Napsauta sitten **Uudelleenkäynnistä ja päivitä** käynnistääksesi prosessin.



### Vaihtoehto 2: Päivitä päätelaitteen kautta (suositellaan)



Tämä menetelmä tarjoaa täydellisemmän valvonnan. Sen avulla voit päivittää arkistoja, ohjelmistopaketteja ja tarvittaessa ytimen.




- Avaa terminaali pikanäppäimellä `Ctrl + Alt + T`.
- Päivitä saatavilla olevien pakettien luettelo seuraavalla komennolla:



```shell
sudo apt update
```



Kirjoita salasanasi pyydettäessä (huomaa, että merkkejä ei näytetä, kun kirjoitat - tämä on normaalia).





- Asenna käytettävissä olevat päivitykset:



```shell
sudo apt full-upgrade
```



## Tutustu perustehtäviin



### Internetin selaaminen



Debianin oletusverkkoselain on **Firefox**. Jos haluat mieluummin toisen selaimen, voit asentaa toisen, jos se on saatavilla Debianin arkistoista (kuten Chromium, Brave...).



### Tekstinkäsittely



**LibreOffice**-paketti on asennettu oletusarvoisesti Debianiin.





- Asiakirjojen kirjoittamiseen voit käyttää **LibreOffice Writeria**, joka vastaa Microsoft Wordia.
- Taulukkolaskentaa varten **LibreOffice Calc** toimii vaihtoehtona Excelille.
- Lopuksi **LibreOffice Impress** mahdollistaa esitysten luomisen PowerPointin tavoin.



## Sovellusten asentaminen



Sovellusten asentaminen Debianiin voi tapahtua kahdella tavalla:



### Graafinen menetelmä:



Voit etsiä ja asentaa sovelluksia helposti **ohjelmistohallinnan** avulla (graafisen Interface:n kautta).



### Komentorivin menetelmä:



Jos etsimäsi sovellus ei näy graafisessa Interface:ssa tai jos haluat käyttää mieluummin terminaalia, käytä seuraavaa komentoa:



```shell
sudo apt install <name>
```



Korvaa `<nimi>` paketin nimellä. Asenna esimerkiksi `curl`:



```shell
sudo apt install curl
```



### Manuaalisesti ladatun paketin asentaminen:



Jos olet ladannut `.deb`-tiedoston (Debian-paketti), voit asentaa sen seuraavalla komennolla:



```shell
sudo apt install ./name.deb
```



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af

Debian-järjestelmäsi on nyt asennettu ja valmis käytettäväksi päivittäisiin tehtäviisi.


**GNOME**-työpöytäympäristön ansiosta voit käyttää monenlaisia sovelluksia käyttäjäystävällisen graafisen Interface:n kautta, joka on ihanteellinen sekä aloittelijoille että edistyneille käyttäjille.



On myös mahdollista vaihtaa työpöytäympäristöä (esim. XFCE:hen, KDE:hen jne.) ilman, että sinun tarvitsee asentaa Debiania uudelleen. Voit tehdä tämän yksinkertaisesti käyttämällä terminaalia ja asentamalla uuden valitsemasi ympäristön.



Jos haluat oppia lisää Debianista ja yleisemmin GNU/Linux-jakeluista, suosittelen tutustumaan tähän kurssiin:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1