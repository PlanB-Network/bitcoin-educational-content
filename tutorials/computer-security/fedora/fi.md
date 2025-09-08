---
name: Fedora
description: Linux-jakelu, joka tarjoaa sinulle ilmaisen, täydellisen ja turvallisen työtilan.
---


![cover](assets/cover.webp)





Fedora on vuonna 2003 lanseerattu ilmainen, avoimen lähdekoodin Linux-pohjainen käyttöjärjestelmä, jonka on kehittänyt **Fedora Project**-yhteisö ja jota tukee **Red Hat Linux**. Se on tunnettu vakaudestaan, hyvästä suorituskyvystään ja helppokäyttöisyydestään, mikä tekee siitä erinomaisen valinnan sekä aloittelijoille että edistyneille käyttäjille. Järjestelmä toimii useimmilla nykyaikaisilla prosessoriarkkitehtuureilla, joten se on helppo asentaa lähes mihin tahansa tietokoneeseen. Fedora on saatavilla myös useina valmiiksi konfiguroituina versioina, joita kutsutaan nimellä "Fedora Spins" tai "Fedora Editions" ja jotka on suunniteltu erityistarpeisiin (videopelit, tähtitiede, kehitys...).



## Fedora Linux -arkkitehtuuri



Kuten aiemmin luit, Fedora on ilmainen käyttöjärjestelmä, joka perustuu Linux-ytimeen. Linux-ydin on käyttöjärjestelmän osa, joka kommunikoi tietokonelaitteiston kanssa ja hallinnoi järjestelmän resursseja, kuten muistia ja prosessoritehoa.



Fedora Linux sisältää erilaisia ohjelmistotyökaluja ja sovelluksia, joita tarvitaan käyttöjärjestelmän käyttämiseen Linux-ytimen päällä. Fedoran modulaarinen arkkitehtuuri tarkoittaa, että se koostuu pääasiassa yksittäisistä komponenteista, joita voidaan helposti lisätä, poistaa tai korvata tarpeen mukaan. Näin voit muokata käyttöjärjestelmää käyttämällä vain tarvitsemiasi resursseja.



Fedora sisältää myös työpöytäympäristön, joka on Interface, jonka kautta käyttäjät suorittavat tehtäviä ja käyttävät sovelluksia. Fedoran oletusarvoinen työpöytäympäristö on GNOME, joka on käyttäjäystävällinen, helppokäyttöinen ja hyvin muokattavissa oleva työpöytäympäristö.



## Miksi valita Fedora?



Lukuisista saatavilla olevista Linux-jakeluista Fedora erottuu erityisesti:





- Modulaarisuus**: Fedora on yhteensopiva eri prosessoriarkkitehtuurien kanssa, joten se voidaan asentaa useimpiin tietokoneisiin, jopa pienitehoisiin, ja se mukautuu täydellisesti tarpeisiisi.





- Yksinkertainen, intuitiivinen Interface**: Fedora yhdistää nykyaikaisen graafisen Interface:n ja tehokkaan komentorivin Interface:n, mikä tekee siitä helppokäyttöisen kaikille profiileille.





- Ytimen vakaus**: Fedora on tunnettu Red Hatiin perustuvasta Fedora-ohjelmistosta, joka on tunnettu päivitystensä luotettavuudesta, erityisesti ytimen päivityksistä, jotka toteutetaan ilman suurempia virheitä laajan yhteisön ilmaisen panoksen ansiosta.





- Nopea ja helppo asennus**: vain 3 GB:n kuvakoko mahdollistaa nopean ja helpon asennuksen myös koneilla, joilla on rajalliset resurssit.



## Fedoran versiot



Profiilisi ja käyttötarkoituksesi mukaan Fedora tarjoaa tarpeisiisi sopivia versioita. Löydät pääasiassa:





- Fedora Workstation**: Tämä versio on ihanteellinen henkilökohtaiseen ja/tai ammatilliseen käyttöön tietokoneillasi, ja siihen on asennettu yleisiä apuohjelmia, kuten selaimia, toimistopaketti (tekstieditorit) ja median toisto-ohjelmisto.





- Fedora Server**: Tämä painos on omistettu palvelimen hallinnalle. Fedora Server sisältää erilaisia työkaluja, joiden avulla voit ottaa käyttöön ja hallita palvelimia omassa mittakaavassa.





- Fedora CoreOS**: Haluatko helposti ajaa ja ottaa käyttöön pilvisovelluksia? Fedora CoreOS on painos, joka antaa sinulle työkalut kuvien luomiseen ja hallintaan esimerkiksi Dockerin ja Kubernetin avulla.



Tässä oppaassa otamme vastuullemme Fedora Workstation -painoksen. Jäljempänä kuvatut prosessit ovat kuitenkin samanlaisia myös muissa versioissa.



## Fedora Workstationin asentaminen ja konfigurointi



Fedora Workstationin asentaminen edellyttää seuraavia laitteistokokoonpanoja:




- Vähintään **8 Gt:n** USB-levy käyttöjärjestelmän käynnistämistä varten.
- Vähintään **40 Gt vapaata tilaa** tietokoneen Hard -levyllä.
- 4 Gt RAM-muistia** sujuvaan käyttökokemukseen.



### Lataa Fedora Workstation



Voit ladata [Fedora Workstation] -version (https://fedoraproject.org/fr/workstation/download) Fedora-projektin virallisilta verkkosivuilta. Valitse sitten prosessoriarkkitehtuuriasi vastaava versio (32-bittinen - 64-bittinen) ja napsauta **Lataus**-kuvaketta.



![download](assets/fr/01.webp)



![telecharger](assets/fr/02.webp)


### Luo käynnistettävä USB-levy



Fedoran asentamista varten sinun on luotava käynnistettävä USB-levy esimerkiksi [Balena Etcher](https://etcher.balena.io/) -ohjelmalla.



![flashOs](assets/fr/03.webp)



![flash](assets/fr/04.webp)



Kun olet saanut Balena Etcherin asennuksen valmiiksi, avaa sovellus ja valitse ladattu Fedora Workspace ISO-kuva. Valitse USB-levyke kohdevälineeksi ja napsauta **Flash**-painiketta aloittaaksesi käynnistettävän avaimen luomisen.



![boot](assets/fr/05.webp)


### Fedoran asentaminen



Kun olet käynnistänyt USB-tietolevyn, sammuta tietokone.


Käynnistä tietokone ja avaa BIOS käynnistyksen aikana painamalla F2-, F12- tai ESC-näppäintä tietokoneesta riippuen.



Valitse käynnistysvaihtoehdoissa USB-levy ensisijaiseksi käynnistyslaitteeksi. Kun vahvistat tämän valinnan, tietokone käynnistyy uudelleen ja käynnistää automaattisesti USB-tikulla olevan Fedora-asennusohjelman**.



Kun tietokone on käynnistetty USB-tikulta, **GRUB-näyttö** tulee näkyviin.



Tässä vaiheessa sinulla on seuraavat vaihtoehdot:




- Testivälineet**: Tämän vaihtoehdon avulla voit tarkistaa USB-tikun eheyden ja varmistaa, että kaikki oikean asennuksen edellyttämät riippuvuudet ovat mukana. Tämä on valinnainen vaihe, mutta sitä suositellaan, jos sinulla on epäilyksiä USB-tikun suhteen.



![install](assets/fr/06.webp)



![testing](assets/fr/07.webp)





- Käynnistä Fedora**: Tämä käynnistää Fedoran "live"-tilassa ilman asennusta.



Napsauta Fedoran työpöydällä (live-tilassa) **Asenna Fedora** (tai Asenna Hard-levylle) käynnistääksesi asennusprosessin. Voit valita asennuksen myöhemmin ja testata Fedoraa ilman asennusta.



![install-live](assets/fr/08.webp)



Ensimmäinen vaihe on Fedoran **asennuskielen** ja **näppäimistön asettelun** valitseminen



![language](assets/fr/10.webp)





- Asennuslevyn valitseminen:



Valitse Hard-levy, jolle haluat asentaa Fedoran.



Jos levy on tyhjä, Fedora käyttää automaattisesti kaiken käytettävissä olevan tilan. Muussa tapauksessa voit muokata osiointia (manuaalisesti tai automaattisesti).



![disk](assets/fr/11.webp)





- Salaus:



Tässä vaiheessa Fedora ehdottaa levyn salaamista lisäturvaksi Layer. Näin varmistetaan, että tietojasi voi lukea vain Fedora-järjestelmäsi.



![chiffrement](assets/fr/12.webp)



Ennen asennuksen käynnistämistä Fedora näyttää yhteenvedon valinnoistasi. Vahvista ja napsauta asennuspainiketta Fedoran asennuksen käynnistämiseksi.



![resume](assets/fr/13.webp)



Asennuksen aikana Fedora kopioi tiedostoja ja konfiguroi järjestelmän. Kun asennus on valmis, tietokone käynnistyy automaattisesti uudelleen.



![installation](assets/fr/14.webp)



### Peruskonfiguraatio


Ensimmäisellä käyttökerralla sinun on viimeisteltävä muutama asetus:




- Vaihda tarvittaessa järjestelmän kieltä.



![language](assets/fr/15.webp)





- Valitse haluamasi näppäimistöasettelu.



![keyboard](assets/fr/16.webp)





- Valitse aikavyöhykkeesi kirjoittamalla kaupunkisi nimi hakupalkkiin ja napsauta sitten vastaavaa ehdotusta.



![timezone](assets/fr/17.webp)





 - Ota käyttöön tai poista käytöstä sijaintisi käyttöoikeus sitä tarvitseville sovelluksille sekä vikailmoitusten automaattinen lähettäminen.



![location](assets/fr/18.webp)





- Päätä, haluatko ottaa käyttöön kolmannen osapuolen ohjelmistovarastot.



![logs](assets/fr/19.webp)





- Kirjoita koko nimesi ja määritä käyttäjätunnus tilillesi.



![name](assets/fr/20.webp)





- Luo istuntoa varten turvallinen salasana: mahdollisimman pitkä (vähintään 20 merkkiä), mahdollisimman satunnainen ja erilaisia merkkejä sisältävä (pienet ja isot kirjaimet, numerot ja symbolit). Muista tallentaa salasanasi.



![mdp](assets/fr/21.webp)



Kun kaikki nämä vaiheet on suoritettu, käynnistä Fedora ja aloita sen käyttö välittömästi ilman uudelleenkäynnistystä.



![welcome](assets/fr/22.webp)



![start](assets/fr/23.webp)



Kun asennus on valmis, voit konsultoida Interface-kotia muutamalla esiasennetulla apuohjelmalla.



![install-now](assets/fr/09.webp)



## Tutustu perustehtäviin



### Internetin selaaminen


Fedoran oletusselain on **Firefox**. Se on helppokäyttöinen ja sopii useimpiin tarpeisiin.


Jos haluat toisen selaimen, voit asentaa sen **ohjelmistohallinnasta** tai **päätteestä**.


### Tekstinkäsittely


Fedora sisältää oletuksena **LibreOffice**-toimistopaketin, joka tarjoaa useita hyödyllisiä työkaluja:




- Writer** tekstinkäsittelyä varten.
- Calc** taulukkolaskentaa varten.
- Impress** esitysten luomiseen.


## Sovellusten asentaminen


Uusien sovellusten asentamiseen voit käyttää Fedoran **ohjelmistohallintaohjelmaa** (nimeltään _Software_), joka tekee asennuksesta helppoa ja visuaalista.  **terminaalin** käyttäminen on kuitenkin usein nopeampaa ja tarkempaa.



Ennen kuin asennat ohjelmistoja, muista aina päivittää **tietovarastot**, jotta voit varmistaa, että käytössäsi on uusimmat saatavilla olevat versiot.



Käynnistä sitten haluamasi sovelluksen asennus seuraavalla komennolla:


sudo dnf install ohjelmisto_nimi`


## Käyttöjärjestelmän päivittäminen


Asennuksen jälkeen on tärkeää päivittää Fedora, jotta voit hyödyntää uusimpia tietoturvakorjauksia ja ohjelmistopäivityksiä.


### Vaihtoehto 1: Interface-grafiikan kautta




- Avaa Fedoran **Asetukset** ja siirry sitten kohtaan **Järjestelmä**.
- Napsauta **Ohjelmistopäivitys**.
- Aloita päivitysten lataaminen ja odota, kunnes prosessi on valmis.



Päivitysten asentamisen jälkeen saatetaan tarvita **pysäytys**.


### Vaihtoehto 2: Päätelaitteen kautta




- Avaa terminaali ja aloita päivittämällä **repositoryt** varmistaaksesi, että sinulla on uusimmat versiot:



```shell
sudo dnf check-update
```





- Päivitä seuraavaksi kaikki asennetut ohjelmistot seuraavalla komennolla:



```shell
sudo dnf upgrade
```



Nyt Fedora-järjestelmäsi on ajan tasalla ja valmis käytettäväksi kaikkiin jokapäiväisiin tehtäviisi. Tutustu oppaaseemme Linux Mintistä, toisesta Linux-jakelusta, ja siihen, miten voit luoda terveen ja turvallisen ympäristön Bitcoin-tapahtumillesi.



https://planb.network/tutorials/computer-security/operating-system/linux-mint-da44852e-513f-4004-949a-8fde60c1bca5