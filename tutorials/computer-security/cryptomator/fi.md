---
name: Cryptomator
description: Salaa tiedostosi pilvipalvelussa
---
![cover](assets/cover.webp)



___



*Tämä opetusohjelma perustuu Florian BURNELin alkuperäiseen sisältöön, joka on julkaistu osoitteessa [IT-Connect](https://www.it-connect.fr/). Lisenssi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Alkuperäiseen tekstiin on saatettu tehdä muutoksia.*



___



## I. Esittely



Tässä ohjeessa käytämme Cryptomator-sovellusta pilvipalveluun tallennettujen tietojen salaamiseen, olipa kyseessä sitten Microsoft OneDrive, Google Drive, Dropbox, Box tai jopa iCloud.



Drive-tietokannan kaltaisiin verkkotallennusratkaisuihin tallentamiesi tietojen salaaminen on paras tapa suojata tiedostojasi ja yksityisyyttäsi. Salauksen ansiosta vain sinä voit purkaa salauksen ja lukea tietosi, vaikka ne olisi tallennettu palvelimelle Yhdysvalloissa tai jossakin muussa maassa ympäri maailmaa.



Tässä esittelyssä käytetään Windows 11 22H2 -konetta, jossa on OneDrive, mutta menettely on samanlainen muissa Windows-versioissa ja muissa tallennuspalveluissa. Sinun tarvitsee vain asentaa synkronointiasiakasohjelma ja lisätä tilisi. Näin Cryptomator voi tallentaa tietonsa holviin.



![Image](assets/fr/020.webp)



Cryptomator on vaihtoehto muille sovelluksille, erityisesti toisessa artikkelissa esitellylle Picocryptille, joka näyttää erilaiselta, mutta on yhtä helppokäyttöinen. Cryptomator on myös **avoin lähdekoodi**, RGPD-yhteensopiva ja **salaa tiedot AES-256-bittisellä salausalgoritmilla**. Picocrypt sen sijaan luottaa nopeampaan XChaCha20-algoritmiin (myös 256-bittinen).



https://planb.network/tutorials/computer-security/data/picocrypt-98c213bd-9ace-425b-b012-bea71ce6b38f

Cryptomator-sovellus on saatavilla **Windows** (exe / msi), **Linux**, **macOS,** mutta myös **Android** ja **iOS**. Muuten, kaikki sovellukset ovat ilmaisia, paitsi Android-sovellus, josta on maksettava (14,99 euroa).



**Cryptomator luo koneellesi kansion, johon se luo kassakaapin**. Holvissa, joka voidaan tallentaa OneDriveen, Google Driveen tai vastaavaan, tietosi salataan. Jos siis tallennat kaikki tietosi Drive-tallennustilassasi sijaitsevaan kassakaappiin, ne ovat suojattuja (koska ne on salattu).



**Huomautus**: Tässä artikkelissa käytetään esimerkkinä verkkotallennuspalveluja, mutta Cryptomatoria voidaan käyttää paikallisen levyn, ulkoisen levyn tai jopa NAS:n tietojen salaamiseen. Rajoituksia ei itse asiassa ole.



## II. Cryptomatorin asentaminen



Aloittaaksesi sinun on **ladattava** ja **asennettava** **Cryptomator**. Kun lataus on valmis, asennus voidaan suorittaa loppuun muutamalla napsautuksella. Kuten [Rclone](https://www.it-connect.fr/rclone-un-outil-gratuit-pour-synchroniser-vos-donnees-dans-le-cloud/), Cryptomator käyttää WinFsp:tä **virtuaalisen aseman asentamiseen Windows-koneeseesi**.





- [Lataa Cryptomator virallisilta sivuilta](https://cryptomator.org/downloads/)



![Image](assets/fr/025.webp)



## III. Cryptomatorin käyttö Windowsissa



### A. Luo uusi kassakaappi



Voit luoda uuden kassakaapin napsauttamalla "**Lisää**"-painiketta ja valitsemalla "**Uusi kassakaappi...**". Tämän jälkeen koneen nykyiset ja tunnetut kassakaapit näkyvät Interface:ssa vasemmalla. **Koneella A luotua kassakaappia voidaan avata ja muokata koneella B**, jos koneessa on Cryptomator (ja salausavain on tiedossa).



![Image](assets/fr/015.webp)



Aloita antamalla holville nimi, esimerkiksi "**IT-Connect**". Tämä luo OneDriveen hakemiston nimeltä "**IT-Connect**".



![Image](assets/fr/011.webp)



Seuraavassa vaiheessa Cryptomator todennäköisesti **havaitsee koneellasi olevan "aseman "**: Google Drive, OneDrive, Dropbox jne..... Jotta voit valita palveluntarjoajan suoraan. Kokeilin tätä kahdessa eri Windows 11 -koneessa, joissa oli useita Driveja, eikä sitä havaittu. Se ei ole ongelma, määritä vain "**Custom location**" ja valitse tallennustilasi juuri. Esim: **Käyttäjänimi>\OneDrive**.



![Image](assets/fr/018.webp)



Seuraavaksi voit säätää vaihtoehtoa asiantuntija-asetuksissa.



![Image](assets/fr/021.webp)



Seuraavaksi sinun on määritettävä **salasana, joka vastaa salausavainta**. Tämän salasanan avulla voit **avata Cryptomator-kaapin lukituksen** ja päästä käsiksi sen tietoihin. **Jos kadotat sen, menetät pääsyn tietoihin**. Lopuksi sinulla on vielä mahdollisuus **luoda vara-avain** valitsemalla vaihtoehto "**Kyllä, parempi katsoa kuin katua**", samassa hengessä kuin [BitLocker] palautusavain (https://www.it-connect.fr/comment-activer-bitlocker-sur-windows-11-pour-chiffrer-son-disque/). Tämä on suositeltavaa, mutta älä säilytä tätä varmuuskopioavainta OneDriven juureen!



Napsauta "**Luo kassakaappi**".



![Image](assets/fr/019.webp)



Kopioi palautusavain ja tallenna se suosikkisalasanahallintaasi. Napsauta "**Seuraava**".



![Image](assets/fr/013.webp)



Siinä kaikki, uusi runkosi on luotu ja valmis käytettäväksi!



![Image](assets/fr/014.webp)



### B. Pääsyluvut



Jos haluat käyttää kassakaappia ja sen tietoja joko **lukea olemassa olevia tietoja tai lisätä uusia tietoja**, sinun on **avata** sen lukitus. Cryptomator luettelee tunnetut kassakaapit: IT-Connect-kassakaappi tulee näkyviin, joten valitse se ja napsauta "**Poista lukitus**".



![Image](assets/fr/016.webp)



Kassakaapin lukituksen avaaminen edellyttää salasanan syöttämistä. Napsauta sitten "**Vapauta asema**".



![Image](assets/fr/022.webp)



**Kassakaappisi on asennettu Windows-koneeseen virtuaalisena asemana.** Tämä asema, joka tässä tapauksessa perii kirjaimen E, antaa sinulle pääsyn tietoihin (selväkielisenä tekstinä, koska kassakaappi on avattu).



![Image](assets/fr/017.webp)



OneDriven puolella emme voi selata Cryptomatorin holvia suoraan. Emme näe tietoja (emme tiedostojen nimiä emmekä sisältöä). Tämä tarkoittaa, että sinun ei tarvitse lisätä tietoja Cryptomator-holviin tavallisen OneDrive-pikakuvakkeen kautta. **Tietosi on lisättävä Cryptomatorin virtuaalisen aseman kautta



![Image](assets/fr/012.webp)



### C. Runkovaihtoehdot



Kassakaapin asetuksiin pääsee käsiksi "**Salatun äänenvoimakkuuden asetukset**"-painikkeella (kun se on lukittu), ja ne mahdollistavat automaattisen lukituksen, jos se ei ole käytössä, aivan kuten salasanaturvassakin. "**Poista salatun aseman lukitus käynnistyksen yhteydessä**"-vaihtoehto, kuten nimikin kertoo, avaa aseman lukituksen ilman mitään toimenpiteitä ja asentaa virtuaalisen aseman. Turvallisuussyistä tämän vaihtoehdon aktivointia kannattaa välttää.



"**Mounting**"-välilehdellä voit myös päättää, haluatko liittää sen vain lukukäyttöön tai määrittää tietyn kirjaimen.



![Image](assets/fr/024.webp)



Lisäksi Cryptomatorin asetuksissa voit **aktivoida sovelluksen automaattisen käynnistyksen**.



## IV. Päätelmät



**Cryptomatorin** avulla voit **luoda salatun kassakaapin** muutamassa minuutissa suojaamaan tiedot, jotka haluat tallentaa OneDriveen ja kumppaneihin. Se on erittäin helppokäyttöinen, kun se "paritetaan" aseman kanssa: tähän tarkoitukseen se on suosikkini Picocryptin sijaan.