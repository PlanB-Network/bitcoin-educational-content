---
name: Elementaarinen käyttöjärjestelmä
description: Ihanteellinen korvaaja Windowsille ja MacOS:lle
---

![cover](assets/cover.webp)



Elementary OS on Ubuntuun perustuva käyttöjärjestelmä, joka on suunniteltu yksinkertaiseksi, nopeaksi ja vakaaksi moniin arkikäyttöihin. Se on tasapainoinen Linux-vaihtoehto MacOS:lle ja Windowsille. Sen sujuva, intuitiivinen ja selkeä graafinen Interface tekee siitä helposti opittavan myös aloittelijoille. Se keskittyy myös ergonomiaan, turvallisuuteen ja suorituskykyyn.



https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

## Miksi valita Elementary OS





- Yksinkertaisuus ja helppokäyttöisyys**: Elementary OS:n graafinen Interface on MacO:n ja Windowsin välissä. Tämä tuttuus tekee siitä helposti omaksuttavan myös kokemattomille käyttäjille.





- Turvallisuus**: Kuten useimmat Linux-jakelut, Elementary OS hyötyy korkeasta turvallisuustasosta. Säännölliset päivitykset, oikeuksien hallinta ja yleisten virusten puuttuminen tekevät siitä luotettavan järjestelmän.





- Nopeus**: Elementary OS on kevytjakelu. Se vaatii vain vähän resursseja, joten se on nopea ja sopii vaatimattomilla kokoonpanoilla varustettuihin tietokoneisiin.





- Vapaa**: Järjestelmä on täysin ilmainen. Kun lataat sen, voit kuitenkin tehdä lahjoituksen kehittäjien tukemiseksi.





- Aktiivinen yhteisö**: Elementary OS:n ympärillä oleva yhteisö on monipuolinen ja reagoiva. Jos kohtaat vaikeuksia, löydät helposti apua foorumeilta tai sosiaalisista verkostoista.



## Asennus ja konfigurointi


### Laitteiston ennakkoedellytykset



Varmista ennen asennuksen aloittamista, että sinulla on seuraavat laitteet:





- **USB-avain**, jonka koko on vähintään 12 Gt
- RAM**-muistia vähintään 4 Gt
- **Hard -levy, jonka koko on vähintään 20 Gt** ja joka on tarkoitettu mukavaan käyttöön



## Lataa ISO-kuva



Mene käyttöjärjestelmän viralliselle verkkosivustolle [elementaarinen](https://elementary.io/) ja valitse summa, jolla voit tukea hanketta. Tämä vaihe on vapaaehtoinen.


Jos haluat ladata ISO-kuvan ilmaiseksi, kirjoita 0 kenttään **"Muu "** ja aloita järjestelmän ISO-kuvan lataaminen.



![0_01](assets/fr/01.webp)



## Käynnistettävän USB-avaimen luominen



Kun olet ladannut ISO-kuvan, sinun on saatava se käynnistettäväksi USB-muistitikulle, jotta voit jatkaa asennusta.



Lataa ohjelmisto, kuten [Balena Etcher](https://etcher.balena.io/) tai vastaava työkalu, ja käynnistä ohjelmisto.


Valitse aiemmin ladattu **Elementary OS** ISO-kuva ja aseta USB-levy kohteeksi.



Aloita prosessi napsauttamalla **flash**-painiketta ja odota, että prosessi on valmis, ennen kuin poistat USB-tietolevyn.



![0_02](assets/fr/02.webp)



## Käynnistys näppäimillä ja BIOSin käyttö



Sammuta tietokone, johon haluat asentaa Elementary OS -käyttöjärjestelmän, ja liitä sitten USB-muisti.


Kun tietokone käynnistyy, avaa BIOS (`ESC`, `F9` tai `F11` merkistä riippuen) ja valitse USB-levy käynnistyslaitteeksi ja käynnistä käynnistysprosessi painamalla `Enter`.



## Elementary OS:n asentaminen



Asennus käynnistyy automaattisesti, jos USB-avain on määritetty oikein.



### Kielen valinta



Valitse kieli, jolla haluat asentaa järjestelmän. Voit myös valita alueellisen vaihtoehdon.



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



### Näppäimistön asettelu



Valitse näppäimistöäsi vastaava asettelu. Kenttä on käytettävissä sen tarkistamiseksi, että näppäimet tuottavat oikeat merkit.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)



### Testitila



Elementary OS:n avulla voit testata järjestelmää ennen sen asentamista. Tässä tilassa voit tutustua Interface:een muuttamatta mitään Hard-levyllä olevaa.



### Asennuksen käynnistäminen





- Napsauta **"Poista levy ja asenna "** asentaaksesi suoraan koko levylle.
- Napsauta **"Mukautettu asennus "**, jos haluat hallita osioita manuaalisesti.



![0_07](assets/fr/07.webp)



### Levyn valinta



Valitse levyke, jolle Elementary OS asennetaan, ja napsauta sitten Jatka-painiketta.



![0_08](assets/fr/08.webp)



### Levyn salaus



Vaihtoehdon avulla voit salata levyn **suojata tietosi**. Sinun on asetettava vahva salasana tämän suojauksen aktivoimiseksi. Se on kuitenkin valinnainen.



![0_09](assets/fr/09.webp)



![0_10](assets/fr/10.webp)



### Asennuksen käynnistäminen



Ennen asennuksen käynnistämistä voit sallia laitteiston yhteensopivuudesta riippuen lisälaiteajurien automaattisen asennuksen.





- Aloita asennus valitsemalla "Poista ja asenna".
- Odota, kunnes prosessi on valmis.



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



### Käynnistä uudelleen



Kun olet valmis, käynnistä asennus uudelleen napsauttamalla **enter**-painiketta ja poista USB-avain sopivalla hetkellä, jotta asennus ei käynnistyisi uudelleen.



![0_13](assets/fr/13.webp)



## Konfigurointi asennuksen jälkeen



Uudelleenkäynnistyksen jälkeen tarvitaan muutama lisätoimenpide.



![0_14](assets/fr/14.webp)



### Kielen valinta



Vahvista tai vaihda järjestelmän kieli kirjautumisen yhteydessä.



![0_15](assets/fr/15.webp)



### Näppäimistön asettelu



Varmista, että näppäimistöasettelu on haluamasi.



![0_16](assets/fr/05.webp)



### Käyttäjätilin luominen



Liitä käyttäjätili käyttöjärjestelmään määrittelemällä käyttäjänimi ja suojaamalla sitten pääsy tietoihin aakkosnumeerisella salasanalla, jossa on vähintään 20 merkkiä ja symboleja.



![0_17](assets/fr/17.webp)



### Ensimmäinen yhteys



Kun kirjaudut sisään ensimmäistä kertaa, Elementary OS antaa sinun muokata ympäristöäsi muutamalla perusasetuksella.



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



## Järjestelmäpäivitys



Ennen pitkäaikaista käyttöä on tärkeää päivittää järjestelmään uusimmat korjaukset.


### Vaihtoehto 1: Päivitys Interface-grafiikan kautta



Siirry **AppCenteriin** ja napsauta oikeassa yläkulmassa olevaa päivityskuvaketta. Odota, että päivitykset luetellaan, ja käynnistä asennus napsauttamalla **"Päivitä kaikki "**.



![0_20](assets/fr/20.webp)



![0_21](assets/fr/21.webp)



### Vaihtoehto 2: Päivitys päätelaitteen kautta



Voit suorittaa päivityksen myös komentoriviltä päätelaitteen kautta: tämä on suositeltava vaihtoehto sen tarkkuuden vuoksi.



```shell
sudo apt update
```



```shell
sudo apt full-upgrade
```



Ensimmäisiä päivityksiä varten käyttöjärjestelmä vaatii käyttäjän salasanan ja vahvistuksen ohjelmistopakettien päivittämiseen, jopa Elementary-ytimen osalta.



## Työympäristön kokoonpano



Elementary OS sisältää vain välttämättömät työkalut. Jos haluat mukauttaa ympäristöäsi tarpeisiisi, erityisesti jos olet kehittäjä, suosittelemme asentamaan lisätyökaluja.





- Voit lisätä hyödyllisiä riippuvuuksia seuraavalla komennolla (mukautetaan tarpeidesi mukaan):



```shell
sudo apt update && sudo apt install -y git python3 python3-pip build-essential wget curl zsh make snapd && sudo snap install code --classic
```



Tämä komento asentaa **Git**, **Python 3**, **pip**, **kääntäjätyökalut**, **wget**, **curl**, **zsh**, **make**, **snapd** ja **vscode** valmistellakseen peruskehitysympäristön.



Elementary OS on nyt käytössä koneellasi. Sen yksinkertaisuuden, keveyden ja tyylikkyyden filosofia tekee siitä erinomaisen valinnan sekä henkilökohtaiseen että ammattikäyttöön. Saat vakaan, sujuvan ja selkeän järjestelmän, joka on valmis muokattavaksi mieltymystesi mukaan. Olipa kyse sitten kehitystyöstä, toimistokäytöstä tai päivittäisestä selaamisesta, kaikki on valmiina tehokkaan, intuitiivisen ja miellyttävän työympäristön rakentamiseen. Tutustu myös Fedora-oppaaseemme, joka on yhtä yksinkertainen, vankka ja modulaarinen Linux-jakelu.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0