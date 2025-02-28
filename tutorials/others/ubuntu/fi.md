---
name: Ubuntu
description: Täydellinen opas Ubuntun asentamiseen ja käyttämiseen vaihtoehtona Windowsille
---
![cover](assets/cover.webp)

## Johdanto

Käyttöjärjestelmä (OS) on tärkein ohjelmisto, joka hallinnoi kaikkia tietokoneen resursseja. Vaihtoehtoisen käyttöjärjestelmän, kuten Ubuntun, valitseminen voi tarjota monia etuja turvallisuuden, kustannusten ja yksityisyyden kannalta.

### Miksi Ubuntu?


- Parannettu turvallisuus** : Linux-jakelut ovat tunnettuja turvallisuudestaan ja kestävyydestään
- Ei kustannuksia**: Ubuntu ja useimmat Linux-jakelut ovat maksuttomia
- Suuri yhteisö**: Käyttäjäyhteisö, joka on valmis auttamaan foorumeilla ja opetusohjelmissa
- Yksityisyyden kunnioittaminen**: Avoimen lähdekoodin järjestelmä lisää avoimuutta
- Yksinkertaisuus**: Käyttäjäystävällinen käyttöliittymä ja helppokäyttöisyys
- Rikas ekosysteemi** : Laaja avoimen lähdekoodin ohjelmistoluettelo
- Säännöllinen tuki**: Turvalliset päivitykset Canonicalilta

## Asennus ja konfigurointi

### 1. Edellytykset

**Tarvittavat laitteet:**


- Vähintään 12 GB:n USB-tikku
- Tietokone, jossa on vähintään 25 Gt käytettävissä

### 2. Lataa


- Siirry osoitteeseen [ubuntu.com/download](https://ubuntu.com/download)
- Valitse vakaa versio (LTS suositellaan)
- Lataa ISO-kuva

![Page de téléchargement Ubuntu](assets/fr/01.webp)

![Sélection de la version Ubuntu](assets/fr/02.webp)

### 3. Luo käynnistettävä USB-levy

Voit käyttää useita työkaluja, kuten Balena Etcher :


- Lataa ja asenna [Balena Etcher](https://etcher.balena.io/)

![Page de téléchargement Balena Etcher](assets/fr/03.webp)

![Installation de Balena Etcher](assets/fr/04.webp)


- Avaa Balena Etcher ja valitse Ubuntu ISO-kuva
- Valitse USB-muistitikku kohdevälineeksi
- Napsauta Flash ja odota, että prosessi päättyy

![Utilisation de Balena Etcher](assets/fr/05.webp)

### 4. Ubuntun asentaminen ja suojaaminen

**4.1 Käynnistys USB-muistitikulta** (ranskaksi)


- Sammuta tietokone
- Kytke USB-tikku (joka sisältää Ubuntun) paikalleen
- Käynnistä tietokone. Uusimmissa tietokoneissa järjestelmän pitäisi tunnistaa USB-käynnistysavain automaattisesti. Jos näin ei tapahdu, käynnistä järjestelmä uudelleen pitämällä BIOS/UEFI-käyttönäppäintä painettuna (yleensä F2, F12 tai Delete, merkistä riippuen)
 - Valitse BIOS/UEFI-valikossa USB-levy käynnistyslaitteeksi
 - Tallenna ja käynnistä uudelleen

**4.2 Asennuksen käynnistäminen** (ranskaksi)

**Käynnistysnäyttö**

Kun käynnistät USB-muistista, näet tämän näytön, josta voit käynnistää Ubuntun.

![Écran de démarrage Ubuntu](assets/fr/06.webp)

**Kielen valinta

Valitse haluamasi kieli asennusta ja järjestelmää varten.

![Sélection de la langue](assets/fr/07.webp)

**Saavutettavuusvaihtoehdot

Määritä tarvittaessa saavutettavuusasetukset (ruudunlukuohjelma, suuri kontrasti jne.).

![Options d'accessibilité](assets/fr/08.webp)

**Näppäimistön konfigurointi

Valitse näppäimistöasettelu. Käytettävissä on testikenttä, jolla voit tarkistaa, että näppäimet vastaavat kokoonpanoasi.

![Configuration du clavier](assets/fr/09.webp)

**Verkkoyhteys**

Muodosta yhteys Wi-Fi- tai langalliseen verkkoon päivitysten lataamiseksi asennuksen aikana.

![Configuration réseau](assets/fr/10.webp)

**Asennustyyppi

Valitse joko "Kokeile Ubuntua" (testaa ilman asennusta) tai "Asenna Ubuntu".

![Choix du type d'installation](assets/fr/11.webp)

**Asennusmenetelmä

Valitse interaktiivinen asennus.

![Mode d'installation](assets/fr/12.webp)

**Hakemuksen valinta

Voit valita oletusasennuksen tai laajennetun sovellusvalikoiman.

![Sélection des applications](assets/fr/13.webp)

**Kolmannen osapuolen sovellukset

Päätä, asennatko lisäajureita ja omia ohjelmistoja vai et.

![Installation applications tierces](assets/fr/14.webp)

**Tyyppinen osiointi

Sinulla on kaksi päävaihtoehtoa:


- "Poista levy ja asenna Ubuntu": käyttää koko levyn Ubuntua varten
- " Manuaalinen asennus: luo kaksoiskäynnistys Windowsin kanssa tai muokkaa osioita

![Choix du partitionnement](assets/fr/15.webp)

**Käyttäjätilin luominen

Aseta Ubuntu-tilisi käyttäjätunnus ja salasana.

![Création du compte](assets/fr/16.webp)

**Aikavyöhyke

Valitse maantieteellinen alue järjestelmän kellonajan asettamista varten.

![Sélection du fuseau horaire](assets/fr/17.webp)

**Asennuksen yhteenveto**

Tarkista kaikki valintasi ennen lopullisen asennuksen aloittamista. Kun napsautat "Asenna", prosessi alkaa.

![Résumé de l'installation](assets/fr/18.webp)

**4.3 Ubuntun päivittäminen asennuksen jälkeen** (ranskaksi)

Järjestelmän päivittäminen on tärkeä vaihe uuden asennuksen jälkeen. Sinulla on kaksi vaihtoehtoa:

**Vaihtoehto 1: Graafisen käyttöliittymän kautta**


- Etsi sovellusvalikosta "Ohjelmistot ja päivitykset"
- Sovellus tarkistaa automaattisesti saatavilla olevat päivitykset
- Asenna päivitykset noudattamalla näytön ohjeita

**Vaihtoehto 2: Päätelaitteen kautta


- Avaa pääte (Ctrl + Alt + T)
- Tarkista saatavilla olevat päivitykset kirjoittamalla seuraava komento:

```bash
sudo apt update
```


- Syötä salasanasi pyydettäessä
- Asenna päivitykset kirjoittamalla :

```bash
sudo apt upgrade
```


- Vahvista asennus kirjoittamalla 'Y' ja Enter

### 5. Perustehtävien löytäminen

**5.1 Internetin selaaminen

Oletusarvoisesti Firefox löytyy usein käynnistyspalkista.

Käynnistä Firefox ja aloita selailu.

Muut selaimet (Chrome, Brave jne.) voidaan asentaa Software Managerin tai .deb-pakettien kautta.

**5.2 Tekstinkäsittely

Ubuntun mukana tulee LibreOffice-paketti (Writer tekstinkäsittelyyn).

Sen avaaminen : Toiminnot > Etsi "LibreOffice Writer" tai napsauta kuvaketta, jos se näkyy palkissa.

Voit luoda, muokata ja tallentaa asiakirjoja eri muodoissa (myös .docx-muodossa).

**5.3 Sovellusten asentaminen

Ohjelmistohallinta (nimeltään "Ubuntu Software"): graafinen käyttöliittymä sovellusten etsimiseen ja asentamiseen.

Käytä päätteestä komentoa :

```bash
sudo apt install nom-du-paquet
```

Esimerkki:

```bash
sudo apt install vlc
```

### 6. Johtopäätökset ja lisäresurssit

Nyt olet valmis käyttämään Ubuntua päivittäin: suojaa järjestelmäsi, selaa, tee toimistotöitä, asenna ohjelmistoja ja pidä käyttöjärjestelmäsi ajan tasalla!

Jos haluat viedä digitaalisen elämäsi turvallisuuden askeleen pidemmälle, suosittelemme tutustumaan salattuun viestipalveluumme, joka sopii täydellisesti yksityisyytesi suojaamiseen ja täydentää Ubuntu-asennustasi:

https://planb.network/tutorials/others/proton-mail