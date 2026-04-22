---
name: Zorin OS
description: Täydellinen opas Zorin OS:n asentamiseen ja käyttämiseen nykyaikaisena vaihtoehtona Windowsille
---

![cover](assets/cover.webp)



## Johdanto



Käyttöjärjestelmä on perusohjelmisto, joka mahdollistaa tietokoneen toiminnan: se hallinnoi laitteistoa, ohjelmistoja, tietoturvaa ja käyttöliittymää.


Zorin OS on Linux-jakelu, joka on suunniteltu erityisesti helpottamaan siirtymistä Windowsista ja tarjoamaan samalla avoimen lähdekoodin ohjelmistojen etuja: turvallisuutta, vakautta, yksityisyyttä ja suorituskykyä.



Ubuntu LTS:ään perustuvassa Zorin OS:ssä yhdistyvät korkea ohjelmistoyhteensopivuus ja tuttu, muokattava käyttöliittymä, mikä tekee siitä uskottavan ja helppokäyttöisen vaihtoehdon Windowsille.



## Miksi Zorin OS?





- Interface tuttu**: Windows-tyyppinen ulkoasu (käynnistysvalikko, tehtäväpalkki)
- Helppo siirtyminen**: suunniteltu käyttäjille, jotka tulevat Windowsista
- Parannettu turvallisuus**: Linux-arkkitehtuuri, vähemmän alttiina viruksille
- Yksityisyyden kunnioittaminen**: ei tungettelevaa tiedonkeruuta
- Optimoitu suorituskyky**: toimii hyvin vaatimattomilla koneilla
- Ubuntu LTS** -pohja: vakaus, säännölliset päivitykset ja laaja yhteensopivuus
- Kehittynyt personointi**: Zorin Appearance -työkalun avulla.



## Asennus ja konfigurointi



### 1. Edellytykset



**Tarvittavat laitteet:**





- Vähintään **8 Gt:n** (suositellaan 12 Gt:n) USB-levy;
- Tietokone, jossa on vähintään **25 Gt vapaata levytilaa**
- Internet-yhteys (suositeltava).



### 2. Lataa Zorin OS





- Käy virallisella verkkosivustolla: [https://zorin.com/os](https://zorin.com/os)



![Page de téléchargement Balena Etcher](assets/fr/03.webp)





- Valitse **Zorin OS Core** (suositellaan ilmaista versiota)



![Page de téléchargement Balena Etcher](assets/fr/04.webp)





- Lataa ISO-kuva



Zorin OS tarjoaa myös :





- Zorin OS Lite** (vanhemmat tietokoneet)
- Zorin OS Pro** (maksullinen, lisäominaisuudet ja tuki)



## Käynnistettävän USB-avaimen luominen



Voit käyttää useita työkaluja, kuten Balena Etcher :





- Lataa ja asenna [Balena Etcher](https://etcher.balena.io/).
- Avaa Balena Etcher ja valitse sitten Zorin-ISO-kuva.
- Valitse USB-muistitikku kohdevälineeksi.
- Napsauta Flash ja odota, että prosessi päättyy.



![Utilisation de Balena Etcher](assets/fr/05.webp)



## Käynnistys näppäimillä ja BIOSin käyttö



Sammuta tietokone, johon haluat asentaa Zorin OS:n, ja liitä sitten USB-muisti.


Kun tietokone käynnistyy, avaa BIOS (`ESC`, `F9` tai `F11` merkistä riippuen) ja valitse USB-levy käynnistyslaitteeksi ja käynnistä käynnistysprosessi painamalla `Enter`.





- Valitse käynnistyksen yhteydessä **Kokeile tai asenna Zorin OS**.



![capture](assets/fr/08.webp)





- Jos sinulla on NVIDIA-näytönohjain, valitse **Yritä tai asenna Zorin OS (nykyaikaiset NVIDIA-ajurit)**.
- Odota, kun tiedostot tarkistetaan.



![capture](assets/fr/09.webp)





- Valitse Zorin OS -asennusohjelmassa kieli **ranska** ja napsauta sitten Asenna **Zorin OS**.



![capture](assets/fr/10.webp)





- Valitse näppäimistöasettelu.



![capture](assets/fr/11.webp)





- Merkitse valintaruudut **Lataa päivitykset Zorin OS -käyttöjärjestelmän asennuksen aikana** ja **Asenna kolmannen osapuolen ohjelmistot grafiikka- ja Wi-Fi-laitteistoja ja muita mediaformaatteja varten**.



![capture](assets/fr/12.webp)





- Jos haluat asentaa Zorin OS:n koko levylle: valitse **Poista levy ja asenna Zorin OS**.



![capture](assets/fr/14.webp)



Zorin OS:n asentaminen Windowsin rinnalle (kaksoiskäynnistys) :





- Valitse **Asenna Zorin OS Windowsin käynnistyksenhallinnan vierestä**.



![capture](assets/fr/15.webp)





- Jos et ole osioinut levyasi, valitse levytila, jonka haluat varata Zorin OS:lle, ja napsauta sitten **Asenna nyt**.



![capture](assets/fr/16.webp)





- Vahvista muutokset levyllä kahdesti.



![capture](assets/fr/16.webp)



![capture](assets/fr/17.webp)





- Valitse maantieteellinen alue **Pariisi**.



![capture](assets/fr/18.webp)





- Luo käyttäjätili ja anna tietokoneelle nimi.



![capture](assets/fr/19.webp)





- Odota, kun Zorin OS asentuu.



![capture](assets/fr/20.webp)





- Kun asennus on valmis, napsauta **Restart Now**.



![capture](assets/fr/21.webp)





- Poista USB-asennusavain ja paina Enter-näppäintä.



![capture](assets/fr/22.webp)



## Zorin OS:n löytäminen ja käyttö



### Ensimmäinen käynnistys



Kun käynnistät tietokoneen, pääset GRUB-käynnistysohjelmaan, joka on Linuxin käynnistyksenhallintaohjelma. Oletuksena on valittu **Zorin OS**, joka käynnistyy automaattisesti 30 sekunnin kuluttua.



![capture](assets/fr/23.webp)



Jos olet asentanut Zorin OS:n kaksoiskäynnistyksen Windowsin kanssa, voit käynnistää Windowsin valitsemalla **Windows Boot Manager**.



Kirjaudu sisään käyttäjätililläsi :



![capture](assets/fr/24.webp)



Ensimmäisen käynnistyksen yhteydessä käynnistyy **Tervetuloa Zorin OS:ään** -sovellus, joka auttaa sinua tutustumaan uuteen käyttöjärjestelmään.



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



![capture](assets/fr/27.webp)



![capture](assets/fr/28.webp)



![capture](assets/fr/29.webp)



![capture](assets/fr/30.webp)



![capture](assets/fr/31.webp)



![capture](assets/fr/32.webp)





### Päivitä järjestelmä



Päivityksenhallinta avautuu pian ja ilmoittaa, että päivitykset ovat saatavilla. Asenna ne napsauttamalla **Asenna nyt**-painiketta.



![capture](assets/fr/33.webp)



Voit tarkistaa päivitykset manuaalisesti **Software** > Päivitykset -sovelluksesta:



![capture](assets/fr/34.webp)



### Personointi



Ensimmäiseksi Zorin OS:ssä kannattaa valita **työpöydän ulkoasu**, joka on sinulle mieluisin. Löydät samanlaisia asetteluja kuin Windowsissa (ja vielä enemmän Pro-versiossa).



Voit tehdä tämän avaamalla **Zorin Appareance** > **Type** :



![capture](assets/fr/35.webp)



Avaa sitten **Asetukset** muokataksesi järjestelmääsi:


**Ääni - Asetukset - Zorin OS



![capture](assets/fr/36.webp)



**Online-tilit - Asetukset - Zorin OS



![capture](assets/fr/37.webp)



### Sovellukset



Sovelluksia voi asentaa usealla eri tavalla:





- Software**, Zorin OS -sovelluskauppa. Sovellukset tulevat useista lähteistä: apt, Flatpak ja Snap.



![capture](assets/fr/38.webp)



![capture](assets/fr/39.webp)





- apt** install (komentorivi) :



```bash
sudo apt install gparted
```



![capture](assets/fr/40.webp)



Lisätietoja sovellusten asentamisesta Zorin OS:ään on tällä sivulla: [Sovellusten asentaminen (zorin.com)](https://zorin.com/help/install-apps/).



### Windows-sovellukset



Windows-sovellusten asentaminen aloitetaan asentamalla **zorin-windows-sovellustuki** -paketti terminaalin kautta:



```bash
sudo apt install zorin-windows-app-support
```



Luettelo yhteensopivista Windows-sovelluksista ja niiden yhteensopivuustasoista on sivulla [Wine Application Database] (https://appdb.winehq.org/). Sieltä löydät seuraavat merkit, jotka vastaavat yhteensopivuustasoa (parhaasta huonoimpaan): Platinum, Gold, Silver, Bronze ja Garbage.



Windows .exe- tai .msi-sovelluksen asentamiseen on kaksi vaihtoehtoa:





- Avaa **PlayOnLinux** ja napsauta **Asenna**-painiketta selataksesi yhteensopivia sovelluksia ja pelejä.



![capture](assets/fr/41.webp)





- Kaksoisnapsauta sovelluksen **.exe- tai .msi**-tiedostoa ja anna asennusohjelman opastaa sinua.



![capture](assets/fr/42.webp)



![capture](assets/fr/43.webp)



## Johtopäätökset ja lisäresurssit



Zorin OS on vankka ja edullinen vaihtoehto Windowsille, jossa yhdistyvät yksinkertaisuus, turvallisuus ja yksityisyys.



Se mahdollistaa sujuvan siirtymisen Linuxiin mukavuudesta tai tuottavuudesta tinkimättä.



Jos haluat suojata digitaalista elämääsi entisestään, suosittelemme käyttämään yksityisyyden suojaa tukevia palveluja, erityisesti salattua viestintää varten:



https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2