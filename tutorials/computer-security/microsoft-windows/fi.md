---
name: Windows 11
description: Microsoft Windows 11:n automaattinen asennus asetustiedoston kautta
---
![cover](assets/cover.webp)


Tässä oppaassa opimme, miten Windows 11 asennetaan automaattisesti käyttämällä muuta menetelmää kuin Windowsin tavallista asennusprosessia.


## Lataa!


Ensimmäiseksi tarvitset asennustiedoston. Turvallisin ja luotettavin paikka ladata se on suoraan Microsoftin viralliselta verkkosivustolta.


Käy alla olevasta linkistä ja seuraa ohjeita ladataksesi [Windows 11 ISO-tiedoston](https://www.microsoft.com/en-us/software-download/windows11)


![Image](assets/en/02.webp)


Kun olet lataussivulla, selaa alaspäin ISO-tiedoston lataamista koskevaan osioon.


![Image](assets/en/01.webp)


َJa valitse oikea versio.


![Image](assets/en/03.webp)


Kun olet valinnut Windows 11:n, napsauta Vahvista-painiketta.


Tässä vaiheessa pyynnön käsittely voi kestää muutaman sekunnin, minkä jälkeen näet seuraavan sivun:


![Image](assets/en/04.webp)


Kun olet vahvistanut pyynnön, sinun on valittava haluamasi kieli.


![Image](assets/en/05.webp)


Kun olet valinnut kielen ja napsauttanut Vahvista-painiketta, pyyntö käsitellään. Tämä vaihe voi kestää muutaman sekunnin.


Kun pyyntö on käsitelty onnistuneesti, näet sivun, jossa on .iso-tiedoston latauslinkki. Aloita lataus napsauttamalla 64-bittisen version latauspainiketta.


Tiedoston koko on noin 5,5 Gt, ja luotu linkki on voimassa 24 tuntia.


## Automaatio!


Tässä vaiheessa meidän on tehtävä muutoksia Windowsin vakioasennukseen. Tässä vaiheessa määrittelemme valvomattoman asennuksen avulla, mitkä kohteet asennetaan, ilman että käyttäjä antaa jälkikäteen tietoja. Itse asiassa tässä menetelmässä käytetään XML-tiedostoa, jolla määritetään asennusvaiheet ja Windowsiin asennettavat palvelut. Toisin sanoen Unattended.xml-tiedoston käyttö luo automaatioprosessin asennuksen aikana, jolloin ei tarvitse valita useita vaihtoehtoja ja vältytään ikäviltä vaiheilta, joita yleensä vaaditaan asennuksen aikana. Tämä menetelmä on epätavallinen, mutta Microsoftin käyttöön ottama vakiomenetelmä. Lisätietoja on saatavilla [Microsoftin virallisella verkkosivustolla](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11).


Internetissä on saatavilla erilaisia työkaluja valvomattomien tiedostojen luomiseen. Jotkut niistä ovat verkossa, kun taas toiset ovat offline-tilassa. Yksi online-työkalu tämän tiedoston luomiseen on [tämä verkkosivusto](https://schneegans.de/windows/unattend-generator). Kun avaamme sen, meille avautuu seuraava sivu:


![Image](assets/en/06.webp)


Kuten sivun yläosassa mainittiin, tätä menetelmää voidaan käyttää Windows 10:n ja 11:n asentamiseen. Ensimmäisessä vaiheessa valitaan Windowsin kieli. Jos haluamme lisätä toisen tai jopa kolmannen kielen Windowsin näyttö- ja näppäimistökielten luetteloon, voimme käyttää alla olevaa laatikkoa:


![Image](assets/en/07.webp)


Seuraavassa vaiheessa valitsemme halutun sijainnin.


![Image](assets/en/08.webp)


Tässä vaiheessa voimme myös määrittää tietokoneen prosessoriarkkitehtuurin. Tässä vaiheessa voimme:

1. Päätä, jätätkö huomiotta Windowsin tietoturvaominaisuudet, kuten TPM ja Secure Boot. Secure Boot -ominaisuus varmistaa, että jos Windowsin ydintiedostoja peukaloidaan käynnistysprosessin aikana, ongelma havaitaan ja niiden suorittaminen estetään. Tämä ominaisuus auttaa myös suojaamaan järjestelmää Windowsin haitallisten päivitysten asentamiselta. Näiden ominaisuuksien ohitusmahdollisuuden ottaminen käyttöön on joskus väistämätöntä tietyissä tietokoneissa, erityisesti vanhemmissa malleissa. Yleensä on kuitenkin suositeltavaa pitää Secure Bootin kaltaiset ominaisuudet käytössä.

2. Älä välitä vaatimuksesta, jonka mukaan prosessin suorittaminen edellyttää internet-yhteyttä. Tämä on hyödyllistä tilanteissa, joissa langallista lähiverkkoyhteyttä ei ole käytettävissä, koska useimmissa tapauksissa langatonta korttia ei vielä tunnisteta Windowsin asennuksen aikana, ja Internet-yhteys kaapelin kautta on tarpeen. Tämän vaihtoehdon aktivoiminen ratkaisee tähän vaiheeseen liittyvät ongelmat.


Seuraavassa vaiheessa voimme valita tietokoneelle nimen.


![Image](assets/en/09.webp)


Voimme myös antaa Windowsin valita järjestelmän nimen. Tässä vaiheessa voimme valita Windowsin tyypin, pakatun tai pakkaamattoman, tai antaa Windowsin määrittää sopivan version tietokoneen ominaisuuksien perusteella. Myös aikavyöhyke voidaan asettaa tässä vaiheessa.


Seuraava vaihe koskee osioiden asetuksia:


![Image](assets/en/10.webp)


Tässä vaiheessa voimme määrittää Windowsin asennuksessa käytettävän osiotyypin sekä Windows Recovery Environment -ympäristön asentamiseen tarvittavat asetukset. Valitsemalla ensimmäisen vaihtoehdon osion valinta ja osioiden määrittäminen siirretään Windowsin asennuksen ajaksi, ja asennuksen aikana nämä kysymykset kysytään aivan kuten normaalissa asennusmenetelmässä.


Tässä vaiheessa valitaan asennettava Windows-versio:


![Image](assets/en/11.webp)


Jos tuoteavain on käytettävissä, se voidaan syöttää myös tässä vaiheessa.


Seuraavassa vaiheessa määritetään Windows-kirjautumistili:


![Image](assets/en/12.webp)


## Tilitapaamiset


Tässä vaiheessa:


1. Voimme määritellä nimen ja salasanan admin-tilille. On myös mahdollista luoda useita käyttäjä- tai hallintatilejä.

2. Tässä määritetään, mille tilille kirjaudutaan ensimmäisen kerran Windowsin asennuksen jälkeen. Tämän osion eri vaihtoehdot näkyvät kuvassa.

3. Jos et halua, että mitään tilejä luodaan, tyhjennä kaikki tilit ja valitse tämä vaihtoehto. Tällöin Windows-asennuksen jälkeen kirjaudut automaattisesti Windowsin järjestelmänvalvojatilille.


Seuraavassa vaiheessa määritetään salasanan ja isäntätiedoston asetukset:


![Image](assets/en/13.webp)


Tässä vaiheessa määritetään, pitäisikö salasanoilla olla voimassaoloaika. Lisäksi tämä osio sisältää epäonnistuneita kirjautumisyrityksiä koskevat suojausasetukset, jotka voidaan ottaa käyttöön tai poistaa käytöstä tarpeiden mukaan.


Tämän osion alareunassa on asetukset tiedostojen näyttämistä varten. Mikään näistä asetuksista ei ole käytettävissä tavallisen Windows-asennuksen aikana, vaan ne on määritettävä asennuksen jälkeen. Sen sijaan valvomattoman asennuksen menetelmässä nämä asetukset ovat helposti käytettävissä.


Seuraavassa vaiheessa määritetään Windowsin suojausasetukset:


![Image](assets/en/14.webp)


## Turvallisuusasetukset


Tässä vaiheessa:


1. Windows Defender voidaan ottaa käyttöön tai poistaa käytöstä. Tämä ominaisuus toimii Windowsissa tietoturvaohjelmiston tavoin ja auttaa estämään haitallisten tiedostojen suorittamisen, tietyt verkkohyökkäykset ja paljon muuta.

2. Automaattiset Windows-päivitykset voidaan poistaa käytöstä. Tämä on yksi Windows-käyttäjien yleisimmistä haasteista!

3. Tässä osassa voit ottaa käyttöön tai poistaa käytöstä UAC:n (User Account Control). Tämä ominaisuus estää epäilyttäviä sovelluksia toimimasta korkeammilla luku- ja kirjoitusoikeuksilla.

4. Windows käyttää tätä ominaisuutta havaitakseen mahdollisesti haitalliset ohjelmistot.

5. Ota käyttöön tai poista käytöstä pitkien polkujen tuki Windows-sovelluksissa, kuten PowerShellissä ja muissa sovelluksissa.

6. Ota etätyöpöytä käyttöön tai poista se käytöstä järjestelmän etäkäyttöä varten.


Käytössä olevasta Windows-versiosta riippuen jotkin näistä ominaisuuksista voivat olla tuettuja tai niitä ei välttämättä tueta.


Seuraava vaihe on kuvakkeiden määrittäminen:


![Image](assets/en/15.webp)


Tässä jaksossa:


1. Työpöydän kuvakkeet luetellaan, ja niitä voidaan lisätä tai poistaa tarpeen mukaan.

2. Käynnistä-valikon kuvakkeet on lueteltu, ja niitä voidaan myös lisätä tai poistaa vaatimusten mukaan.

3. Tässä osassa voidaan määrittää, asennetaanko virtualisointiin liittyvät työkalut vai ei. Tämä asetus koskee vain Windows 11:tä, eikä sitä sovelleta Windows 10:een.


Seuraava vaihe on Wi-Fi-asetusten määrittäminen:


![Image](assets/en/16.webp)


Tässä osassa voidaan määrittää Wi-Fi-verkkoasetukset. Kuten aiemmin mainittiin, useimmissa tapauksissa Wi-Fi-korttia ei tunnisteta Windowsin asennuksen aikana, joten yhteyden muodostaminen asennuksen aikana ei yleensä ole mahdollista. Jos langaton kortti kuitenkin tunnistetaan, järjestelmä voi muodostaa yhteyden Internetiin määrittämällä tämän osion asetukset.


Seuraava vaihe sisältää tärkeän asetuksen:


![Image](assets/en/17.webp)


Tässä osassa määritetään, lähetetäänkö järjestelmäongelmatiedot Microsoftille vai ei.


Seuraavassa vaiheessa määritetään oletussovellukset:


![Image](assets/en/18.webp)


## Ohjelmiston oletusarvoinen käyttöönotto/poiskytkentä


Tässä osassa voimme valita sovellukset, joita emme halua asentaa oletusarvoisesti. Voimme esimerkiksi valita, ettemme asenna Cortanaa tai Copilotia.


Seuraava vaihe koskee sovelluksen suorittamiseen liittyviä suojausasetuksia:


![Image](assets/en/19.webp)


Soveltamalla WDAC-asetuksia voidaan estää tiettyjen sovellusten suorittaminen.


Lopuksi, kun olet soveltanut haluttuja asetuksia, luotu XML-tiedosto voidaan ladata:


![Image](assets/en/20.webp)


Kun napsautat Lataa XML-tiedosto, autounattend.xml-tiedosto ladataan. Jos haluat käyttää tätä tiedostoa, asenna ladattu ISO-tiedosto USB-asemaan, aseta autounattend.xml-tiedosto juurihakemistoon ja jatka sitten Windows-asennusta.


Yksi käynnistettävän USB-aseman luomiseen käytettävissä olevista työkaluista on Rufus. Rufus voi tehdä käynnistyskelpoisen Windows-asennusmuistitikun tietyllä Windows-ISO-tiedostolla. Se on nopea ja yksinkertainen, voit ladata sen [täältä](https://rufus.ie/en/#download)


![Image](assets/en/21.webp)


Tässä ohjelmistossa, kun olet valinnut halutun USB-aseman ja sopivan ISO-tiedoston, napsautamme Start.


![Image](assets/en/22.webp)


Tässä vaiheessa poistamme kaikki vaihtoehdot käytöstä, koska niiden käyttäminen voi aiheuttaa ristiriitoja, kun luotua Unattend-tiedostoa käytetään. Kun tiedostot on kopioitu USB-asemalle, asetamme autounattend.xml-tiedoston juurihakemistoon:


![Image](assets/en/23.webp)


Tässä vaiheessa USB-asema on valmis käytettäväksi Windowsin automaattista asennusta varten, ja asennus voidaan aloittaa aseman avulla.


## ISO-editointi


Jos sinun on asennettava Windows virtuaalikoneeseen, voit käyttää ohjelmistoa ISO-tiedostojen luomiseen ja muokkaamiseen. Yksi tällainen ohjelmisto on AnyBurn. Kun olet purkanut Microsoftin verkkosivustolta ladatun ISO-tiedoston sisällön, aseta autounattend.xml-tiedosto juurihakemistoon. Luo sitten AnyBurnin avulla uusi ISO-tiedosto, jonka sisältö on päivitetty.


AnyBurn on monikäyttöinen ohjelmisto ISO-tiedostojen käsittelyyn. Se tarjoaa erilaisia ominaisuuksia ISO-tiedostojen käsittelyyn, joista yksi on boottauskelpoisten ISO-kuvien luominen; [tässä](https://www.anyburn.com/download.php) on alkuperäinen verkkosivusto.


Valitse ohjelmiston pääsivulla "Luo kuva tiedostosta/kansiosta":


![Image](assets/en/24.webp)


Valitse seuraavalla sivulla kaikki ISO-tiedostosta poimitut tiedostot sekä autounattend.xml-tiedosto.


![Image](assets/en/25.webp)


Tässä vaiheessa määritetään asetukset, joilla ISO-tiedostosta tehdään käynnistyskelpoinen:


![Image](assets/en/26.webp)


Tässä vaiheessa on määritettävä bootfix.bin-tiedoston polku, jotta ISO-tiedosto voidaan käynnistää. Tämä tiedosto sijaitsee ISO-tiedoston juuressa, käynnistyskansiossa. On myös suositeltavaa ottaa käyttöön sekä ISO9660- että UDF-asetukset Ominaisuudet-osiossa.


![Image](assets/en/27.webp)


Tämän vaiheen jälkeen ISO-tiedosto luodaan napsauttamalla Seuraava. Tätä tiedostoa voidaan käyttää virtualisointiohjelmistoissa, kuten Oracle VirtualBox:ssa. Alla on VirtualBox:ta koskeva opetusohjelma:


https://planb.academy/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65