---
name: Kali
description: Kali Linuxin asentaminen VirtualBoxiin, käynnistettävänä USB-tikkuna tai kaksoiskäynnistyksenä, askel askeleelta.
---

![cover-kali](assets/cover.webp)



## Johdanto



### Miksi Kali Linux?



**Kali Linux** on tietoturvaan erikoistunut Linux-jakelu.


Siksi käytämme Kali Linuxia:





- Se on valmiiksi konfiguroitu useilla pentesting-työkaluilla (järjestelmä- ja verkkoturvatestit).
- Se on **avoimen lähdekoodin ja ilmainen**, joten voit käyttää ja muokata sitä vapaasti.
- Se on **luotettava ja turvallinen**, ihanteellinen kyberturvallisuuden oppimiseen.
- Sen avulla voit oppia käyttämään Linuxia testausvalmiissa ympäristössä.
- Se voidaan asentaa eri tavoin: **VirtualBox**, **käynnistettävä USB-levy** tai **kaksoiskäynnistys**.



## Asennus ja konfigurointi



### 1. Edellytykset



**Tarvittavat laitteet:**





- 64-bittinen prosessori** (Intel tai AMD).
- vähintään 8 Gt RAM-muistia** (4 Gt voi riittää kevyessä asennuksessa tai VM:ssä).
- 50 Gt vapaata levytilaa** Kali Linuxin asentamista varten.
- Internet-yhteys** ISO-kuvan ja päivitysten lataamista varten.
- Vähintään 8 GB:n USB-levy** käynnistettävän median luomista varten (jos haluat asentaa Kali-ohjelman tietokoneelle tai testata sitä Live USB:llä).



On tärkeää varmuuskopioida tiedot ennen asennusta olemassa olevaan tietokoneeseen.



### 2. Lataa





- Siirry osoitteeseen [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- Valitse sovelluksen ISO-kuva:
  - Asennuskuva** : PC-asennusta varten.
  - Virtual Image**: Kali asennetaan VirtualBoxiin tai VMwareen.
- Lataa ISO-kuva.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. Luo käynnistettävä USB-levy



Voit käyttää useita työkaluja, kuten Balena Etcher :





- Lataa ja asenna [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Avaa Balena Etcher ja valitse sitten Kali-ISO-kuva.
- Valitse USB-muistitikku kohdevälineeksi.
- Napsauta Flash ja odota, että prosessi päättyy.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. Kali Linuxin asentaminen ja suojaaminen



#### 4.1 Käynnistäminen USB-muistitikulta





- Sammuta tietokone.
- Kytke USB-tikku (joka sisältää Kali Linuxin).
- Käynnistä tietokone. Uusimmissa tietokoneissa järjestelmän pitäisi tunnistaa USB-käynnistysavain automaattisesti. Jos näin ei tapahdu, käynnistä järjestelmä uudelleen pitämällä BIOS/UEFI-käyttönäppäintä painettuna (yleensä F2, F12 tai Delete, merkistä riippuen).
  - Valitse BIOS/UEFI-valikossa USB-levy käynnistyslaitteeksi.
  - Tallenna ja käynnistä uudelleen.



#### 4.2 Asennuksen käynnistäminen



##### Käynnistysnäyttö



Kun käynnistät USB-muistitikulta, Kali Linuxin käynnistysnäytön pitäisi tulla näkyviin. Valitse **grafinen asennus** ja **tekstiasennus**. Tässä esimerkissä valitsimme graafisen asennuksen.



![capture](assets/fr/06.webp)



Jos käytät **Live**-kuvaa, näet toisen tilan, **Live**, joka on myös oletuskäynnistysvaihtoehto.



![Mode Live](assets/fr/07.webp)



##### Kielen valinta



Valitse haluamasi kieli asennusta ja järjestelmää varten.



![Sélection de la langue](assets/fr/08.webp)



Ilmoita maantieteellinen sijaintisi.



![Options d'accessibilité](assets/fr/09.webp)



##### Näppäimistön kokoonpano



Valitse näppäimistöasettelu. Käytettävissä on testikenttä, jolla voit tarkistaa, että näppäimet vastaavat kokoonpanoasi.



![Configuration du clavier](assets/fr/10.webp)



##### Verkkoyhteys



Asennus skannaa nyt verkkoliitännät, etsii DHCP-palvelun ja pyytää sinua antamaan järjestelmän isäntänimen. Alla olevassa esimerkissä olemme antaneet isäntänimeksi **"kali "**.



![Configuration réseau](assets/fr/11.webp)



Voit antaa valinnaisesti oletusarvoisen toimialuenimen, jota tämä järjestelmä käyttää (arvot voidaan hakea DHCP:stä tai jos käytössä on jo olemassa oleva käyttöjärjestelmä).



![Choix du type d'installation](assets/fr/12.webp)



##### Käyttäjätilit



Luo seuraavaksi käyttäjätili järjestelmää varten (koko nimi, käyttäjänimi ja vahva salasana).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### Aikavyöhyke



Valitse maantieteellinen alue järjestelmän kellonajan asettamista varten.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### Osioinnin tyyppi



Tämän jälkeen asennusohjelma skannaa levyt ja näyttää useita vaihtoehtoja kokoonpanostasi riippuen.



Tässä oppaassa aloitetaan **tyhjästä levystä**, jolloin on **neljä mahdollista vaihtoehtoa**.


Valitaan **Ohjattu - käytä koko levyä**, koska tässä tehdään Kali Linuxin kerta-asennus (yksittäinen käynnistys). Tämä tarkoittaa, että mitään muuta käyttöjärjestelmää ei säilytetä, ja koko levy voidaan poistaa.



Jos levylläsi on jo tietoja, näyttöön voi tulla lisävaihtoehto **Ohjattu - käytä suurinta yhtenäistä vapaata tilaa**.



Tämän vaihtoehdon avulla voit asentaa Kali Linuxin poistamatta olemassa olevia tietoja, mikä tekee siitä ihanteellisen kaksoiskäynnistyksen toisen järjestelmän kanssa.



Meidän tapauksessamme levy on tyhjä, joten tämä vaihtoehto ei näy.



![Choix du partitionnement](assets/fr/17.webp)



Valitse osioitava levy.



![capture](assets/fr/18.webp)



Tarpeidesi mukaan voit valita, haluatko pitää kaikki tiedostot yhdessä osiossa (oletusasetus) vai haluatko erilliset osiot yhdelle tai useammalle ylimmän tason hakemistolle.



Jos et ole varma, mitä haluat, valitse vaihtoehto **Kaikki tiedostot yhdessä osiossa**.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



Tämän jälkeen sinulla on vielä viimeinen tilaisuus tarkistaa levyn kokoonpano ennen kuin asennusohjelma tekee peruuttamattomia muutoksia. Kun olet napsauttanut Jatka_, asennusohjelma käynnistyy ja asennus on lähes valmis.



![capture](assets/fr/21.webp)



##### Salattu LVM



Jos tämä vaihtoehto otettiin käyttöön edellisessä vaiheessa, Kali Linux suorittaa nyt turvallisen kiintolevyn poiston ennen kuin se kysyy LVM-salasanaa.



Käytä vahvaa salasanaa, muuten näyttöön tulee varoitus heikosta passphrase:sta.



##### Valtakirjan tiedot



Kali Linux käyttää arkistoja sovellusten jakeluun. Sinun on annettava tarvittavat välityspalvelimen tiedot, jos ympäristösi käyttää sellaista.



Jos et ole varma, haluatko käyttää välityspalvelinta, jätä tyhjäksi**. Väärien tietojen antaminen estää yhteyden arkistoihin.



![capture](assets/fr/22.webp)



##### Metapets



Jos verkkoyhteyttä ei ole määritetty, sinun on pyydettäessä **määritettävä**.



Jos käytät **Live**-kuvaa, seuraavaa vaihetta ei näytetä.



Voit sitten valita [metapaketit](https://www.kali.org/docs/general-use/metapackages/), jotka haluat asentaa. Oletusasetukset asentavat tavallisen Kali Linux -järjestelmän, joten sinun ei tarvitse muuttaa mitään.



![capture](assets/fr/23.webp)



#### Aloitustiedot



Vahvista sitten GRUB-käynnistyslatausohjelman asennus.



![capture](assets/fr/24.webp)



##### Käynnistä uudelleen



Napsauta lopuksi Jatka käynnistääksesi uuden Kali Linux -asennuksen uudelleen.



![capture](assets/fr/25.webp)



#### 4.3 Kali Linuxin päivittäminen ja konfigurointi asennuksen jälkeen



Järjestelmän päivittäminen on tärkeä vaihe uuden asennuksen jälkeen. Sinulla on kaksi vaihtoehtoa:



##### Vaihtoehto 1: Graafisen käyttöliittymän (GUI) kautta



Kali, kuten Debian/Ubuntu, tarjoaa integroidun graafisen päivityshallinnan.



1. Napsauta **päävalikkoa** (vasemmassa ylä- tai alareunassa työpöydästäsi riippuen).


2. Avaa **"Software Updater "**.


3. Työkalu :




    - Tarkista päivitettävät paketit.
    - Näet luettelon (koot ja versiot).
    - Voit käynnistää päivityksen yhdellä napsautuksella.


4. Kirjoita järjestelmänvalvojan salasana (`sudo`), kun sitä pyydetään.


5. Anna sen asentua ja käynnistä se tarvittaessa uudelleen.



##### Vaihtoehto 2: Päätelaitteen kautta



Avaa terminaali ja suorita :



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



Ei ole suositeltavaa käyttää **root**-tiliä päivittäiseen työhön; luo sen sijaan muu kuin root-käyttäjä.



Kirjoita päätelaitteeseen nämä komennot:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



Kirjaudu ulos ja kirjaudu takaisin sisään uudella käyttäjällä.



Tiivistetään joitakin Kali Linuxin perustehtäviä taulukkoon.



### Perustehtävät Kali Linuxissa




| **Kategoria** | **Perustehtävä** | **Kuvaus / Tavoite** | **Pääasiallinen menetelmä** |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Järjestelmässä navigointi** | Avaa terminaali | Pääsy Kalin komentoriville | Napsauta terminaalin kuvaketta tai käytä `Ctrl + Alt + T` |
| | Selaa kansioita | Liikkuminen järjestelmän hakemistorakenteessa | `cd /polku/kansioon`, `ls` tiedostojen listaamiseen |
| | Luo / poista kansio | Tiedostojen järjestäminen | `mkdir kansion_nimi`, `rm -r kansion_nimi` |
| **Tiedostojen hallinta** | Kopioi / siirrä tiedosto | Tiedostojen käsittely terminaalissa | `cp tiedosto kohde`, `mv tiedosto kohde` |
| | Poista tiedosto | Levytilan vapauttaminen | `rm tiedoston_nimi` |
| | Näytä tekstitiedoston sisältö | Tiedoston nopea lukeminen | `cat tiedosto.txt`, `less tiedosto.txt` |
| **Järjestelmän hallinta** | Päivitä Kali Linux | Uusimpien versioiden ja tietoturvapaikkausten asennus | `sudo apt update && sudo apt full-upgrade -y` |
| | Asenna ohjelmisto | Uuden työkalun tai apuohjelman lisääminen | `sudo apt install paketin_nimi` |
| | Poista ohjelmisto | Järjestelmän puhdistaminen | `sudo apt remove paketin_nimi` |
| | Puhdista tarpeettomat riippuvuudet | Levytilan säästäminen | `sudo apt autoremove` |
| **Verkko ja internet** | Tarkista verkkoyhteys | Internet-yhteyden testaaminen | `ping google.com` |
| | Tunnista IP-osoite | Verkkokonfiguraation selvittäminen | `ip a` tai `ifconfig` |
| | Vaihda Wi-Fi-verkkoa | Yhdistäminen toiseen tukiasemaan | Verkkokuvake → Valitse haluttu Wi-Fi |
| **Tilit ja käyttöoikeudet** | Suorita järjestelmänvalvojan komento | Root-oikeuksien hankkiminen tilapäisesti | `sudo komento` |
| | Luo uusi käyttäjä | Paikallisen tilin lisääminen | `sudo adduser käyttäjänimi` |
| | Vaihda salasana | Tilin suojaaminen | `passwd` |
| **Ulkoasu ja mukavuus** | Vaihda taustakuva | Työpöydän personointi | Napsauta hiiren kakkospainikkeella työpöytää → **Työpöydän asetukset** |
| | Muuta teemaa / kuvakkeita | Luettavuuden ja estetiikan parantaminen | Asetukset → Ulkoasu / Teemat |
| **Kali-työkalut** | Avaa työkalunäkymä | Testaus- ja tietoturvatyökalujen tutkiminen | Valikko **Applications → Kali Linux** |
| | Käynnistä työkalu (esim: nmap, wireshark) | Tietoturvatyökalujen käytännön kokeilu | `sudo nmap`, `wireshark` jne. |
| **Apu ja dokumentaatio** | Hae apua komennolle | Komennon ymmärtäminen ennen käyttöä | `man komento` tai `komento --help` |

## Päätelmä



Kali Linuxin asentaminen on vain ensimmäinen askel tämän tehokkaan, kyberturvallisuudelle omistetun ympäristön löytämiseksi. Hallitsemalla perustehtävät ja järjestelmänhallinnan jokainen voi alkaa tutkia sisäänrakennettuja työkaluja ja ymmärtää Linux-järjestelmän sisäistä toimintaa. Kali tarjoaa erinomaisen oppimisalustan sekä teknisten taitojen vahvistamiseen että aidon tietoturvakulttuurin kehittämiseen.