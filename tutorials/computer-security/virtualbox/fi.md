---
name: VirtualBox
description: Asenna VirtualBox Windows 11:een ja luo ensimmäinen VM:si
---
![cover](assets/cover.webp)



___



*Tämä opetusohjelma perustuu Florian Burnelin alkuperäiseen sisältöön, joka on julkaistu [IT-Connect](https://www.it-connect.fr/). Lisenssi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Alkuperäiseen tekstiin on saatettu tehdä muutoksia.*



___




## I. Esittely



Tässä opetusohjelmassa opimme, miten VirtualBox asennetaan Windows 11:een virtuaalikoneiden luomiseksi, olipa kyseessä sitten Windows 10, Windows 11, Windows Server tai Linux-jakelu (Debian, Ubuntu, Kali Linux jne.).



Tämä VirtualBoxin esittelyopas auttaa sinua pääsemään alkuun tämän Oraclen kehittämän avoimen lähdekoodin virtualisointiratkaisun kanssa, joka on täysin ilmainen. Myöhemmin verkkoon tulee muita opetusohjelmia, jotka vievät sinut syvemmälle aiheeseen.



Kun haluat virtualisoida työaseman, olipa kyse sitten projektin testaamisesta tai IT-opinnoista, VirtualBox on selvästi hyvä ratkaisu. Se on myös vaihtoehto muille ratkaisuille, kuten Hyper-V:lle, joka on integroitu Windows 10:een ja Windows 11:een (sekä Windows Serveriin), ja VMware Workstationille (maksullinen) / VMware Workstation Playerille (ilmainen henkilökohtaiseen käyttöön).



Minun kokoonpanoni: **mutta voit asentaa VirtualBoxin myös Windows 10:een (tai vanhempaan versioon) sekä Linuxiin. Virtuaalikoneiden osalta VirtualBox tukee monenlaisia järjestelmiä, kuten Windowsia (esim. Windows 10, Windows 11, Windows Server 2022 jne.), Linuxia (Debian, Rocky Linux, Ubuntu, Fedora jne.), BSD:tä (PfSense) ja macOS:ää.



## II. Lataa VirtualBox for Windows 11



Voit ladata VirtualBoxin asennettavaksi Windows-koneeseen vain yhdellä hyvällä Address:lla: [VirtualBoxin virallinen verkkosivusto](https://www.virtualbox.org/wiki/Downloads) "**Lataukset**"-osiossa. Klikkaa vain "Windows hosts" aloittaaksesi tämän suoritettavan tiedoston lataamisen, jonka koko on hieman yli 100 MB.



![Image](assets/fr/025.webp)



## III. VirtualBoxin asentaminen Windows 11:een



### A. VirtualBoxin asentaminen



VirtualBoxin** asentaminen on yksinkertaista, ja prosessi on sama kaikille Windows-versioille. Aloita käynnistämällä juuri lataamasi VirtualBoxin suoritusohjelma ja napsauta sitten "**Seuraava**".



![Image](assets/fr/026.webp)



Tämä asennus on muokattavissa, mutta suosittelen, että asennat kaikki ominaisuudet: mikä on oletusvalinta. Alla olevassa kuvassa näet erilaisia Elements, kuten:





- VirtualBoxin USB-tuki**, jotta VirtualBox tukee USB-laitteita
- VirtualBox Bridged Network** integroida verkkotuki "Bridge"-tilassa (virtuaalikone voi muodostaa yhteyden suoraan lähiverkkoon)
- VirtualBox Host-Only Network** verkkotuen integroimiseksi "Host-Only"-tilassa (virtuaalikone voi kommunikoida vain fyysisen Windows 11 -isäntäkoneen ja muiden virtuaalikoneiden kanssa tässä tilassa)



Jatka napsauttamalla "**Seuraava**".



![Image](assets/fr/001.webp)



Napsauta "**Kyllä**" ja pidä mielessä, että **verkko keskeytyy hetkeksi Windows 11 -koneessasi**, kun VirtualBox tekee verkkomuutoksia tukeakseen eri verkkotyyppejä, mukaan lukien Bridge-tila.



![Image](assets/fr/002.webp)



Kun olet vahvistanut, asennus alkaa... Ja näyttöön tulee ilmoitus "**Tahdotko asentaa tämän laiteohjelmiston?**". Valitse "**Luotan aina Oracle Corporationin ohjelmistoihin**" ja napsauta "**Asenna**". VirtualBoxin on itse asiassa asennettava useita ajureita tietokoneeseesi.



![Image](assets/fr/003.webp)



Asennus on nyt valmis! Valitse vaihtoehto "**Start Oracle VM VirtualBox 6.1.34 after installation**" ja käynnistä ohjelmisto napsauttamalla "**Click**".



![Image](assets/fr/004.webp)



### B. Lisää laajennuspaketti



Viralliselta VirtualBox-sivustolta (ks. edellinen linkki) voit edelleen ladata virallisen laajennuspaketin, joka on saatavilla "**VirtualBox 6.1.34 Oracle VM VirtualBox Extension Pack**" -osiosta klikkaamalla "**Kaikki tuetut alustat**" -linkkiä. Tämän paketin avulla voit lisätä VirtualBoxiin lisätoimintoja: sen lisääminen ei ole pakollista, mutta siitä voi olla hyötyä! Se sisältää esimerkiksi tuen USB 3.0:lle VM:ssä, webkameratuen ja levyn salauksen.



Avaa VirtualBox, napsauta valikosta "**Tiedosto**" ja sitten "**Asetukset**".



![Image](assets/fr/005.webp)



Napsauta vasemmalla puolella olevaa "**Laajennukset**" (1) ja sitten oikealla puolella olevaa "**+**"-painiketta (2) **ladataksesi juuri lataamasi VirtualBox**-laajennuspaketin (3).



![Image](assets/fr/006.webp)



Vahvista klikkaamalla "**Asennus**"-painiketta.



![Image](assets/fr/007.webp)



Napsauta "**OK**": virallinen laajennuspaketti on nyt asennettu VirtualBox-instanssiin!



![Image](assets/fr/008.webp)



Siirrytään ensimmäisen virtuaalikoneemme luomiseen.



## IV. Ensimmäisen VirtualBox VM:n luominen



Voit luoda uuden virtuaalikoneen VirtualBoxissa napsauttamalla "**Uusi**"-painiketta käynnistääksesi VM:n luontiohjattaren. Koska tämä on ensimmäinen kerta, kun käynnistät VirtualBoxin, haluaisin antaa sinulle muutaman lisätietoa Interface:sta ja muista painikkeista.





- Asetukset**: VirtualBoxin yleiset asetukset (VM:n oletuskansio, päivitysten hallinta, kieli, NAT-verkot, laajennukset jne.)
- Tuo**: tuo virtuaalilaite OVF-muodossa
- Vienti**: olemassa olevan virtuaalikoneen vieminen OVF-muodossa virtuaalilaitteen luomista varten
- Lisää**: Lisää olemassa oleva virtuaalikone VirtualBoxin luetteloon VirtualBoxin vakiomuodossa (.vbox) tai XML-muodossa



Vasemmalla "**Tools**"-osio antaa pääsyn **kehittyneisiin toimintoihin, erityisesti virtuaaliverkon hallintaan, mutta myös VM-tallennuksen hallintaan**. "**Tools**"-kohdan alle lisätään myöhemmin virtuaalikoneesi.



![Image](assets/fr/009.webp)



### A. VM:n luomisprosessi



** Muistutuksena mainittakoon, että VirtualBox tukee useita käyttöjärjestelmiä, kuten Windowsia, Linuxia ja BSD:tä. Tässä esimerkissä luon virtuaalikoneen Windows 11:lle. Useita kenttiä on täytettävä:





- Nimi**: virtuaalikoneen nimi (tämä on nimi, joka näytetään VirtualBoxissa)
- Konekansio**: mihin virtuaalikone tallennetaan, kun tiedetään, että tähän paikkaan luodaan VM:n nimellä varustettu alikansio
- Tyyppi**: käyttöjärjestelmän tyyppi riippuen siitä, minkä käyttöjärjestelmän haluat asentaa
- Versio**: järjestelmän versio, jonka haluat asentaa, tässä tapauksessa Windows 11, joten "**Windows11_64**"



Jatka napsauttamalla "**Seuraava**".



![Image](assets/fr/010.webp)



Riippuen edellisessä vaiheessa valitsemastasi käyttöjärjestelmästä **VirtualBox antaa suosituksia virtuaalikoneelle jaettavista resursseista**. Tässä puhutaan RAM-muistista, jonka haluat varata VM:lle. Oletetaan 4 Gt, koska sitä todellakin suositellaan Windows 11:lle, mutta jos resurssit ovat vähissä, määritä sen sijaan 2 Gt. **Jatka



**Huomaa**: Virtuaalikoneelle osoitettuja resursseja voidaan muuttaa myöhemmin.



![Image](assets/fr/011.webp)



Virtuaalisen Hard-levyn osalta aloitamme tyhjästä, joten meidän on valittava "**Luo virtuaalinen Hard-levy nyt**", jotta VM:llä on tallennustilaa käyttöjärjestelmän asentamista ja tietojen tallentamista varten. Napsauta "**Luo**".



![Image](assets/fr/012.webp)



VirtualBox tukee kolmea eri formaattia virtuaalisille Hard-levyille, mikä on merkittävä ero muihin ratkaisuihin, kuten VMwareen ja Hyper-V:hen, verrattuna. Valittavana on kolme formaattia:





- VDI**, virallinen VirtualBox-formaatti
- VHD**, joka on virallinen Hyper-V-formaatti, vaikka uutta VHDX-formaattia käytetään nykyään useammin
- VMDX** on virallinen VMware-formaatti sekä VMware Workstationille että VMware ESXille



Jos haluat luoda virtuaalikoneen, jota käytetään vain tässä VirtualBox-instanssissa, valitse "**VDI**". Toisaalta, jos virtuaalinen Hard-levy on tarkoitus liittää Hyper-V-isäntäkoneeseen myöhemmin, voi olla hyvä idea aloittaa VHD-muodossa, jotta sitä ei tarvitse muuntaa. Napsauta "**Next**".



![Image](assets/fr/013.webp)



**Virtuaalisen levyn koko voi olla joko dynaaminen tai kiinteä**. Dynaamisessa muodossa **virtuaalilevyä edustava tiedosto (tässä .vdi-tiedosto) kasvaa, kun levylle kirjoitetaan dataa**, kunnes se saavuttaa maksimikokonsa, mutta se ei pienene, jos dataa poistetaan. Kun tiedosto sen sijaan on kiinteäkokoinen, **kokonaistallennustila varataan välittömästi (ja siten varataan)**, mikä mahdollistaa hieman paremman suorituskyvyn, mutta kestää kauemmin, kun virtuaalilevy luodaan ensimmäistä kertaa.



Itse pidän VirtualBoxin testivirtuaalikoneita varten "**Dynaamisesti varattu**"-tilaa riittävänä.



![Image](assets/fr/014.webp)



** Seuraavassa vaiheessa määritetään virtuaalilevyn koko**, ja on muistettava, että oletusarvoisesti levy tallennetaan VM-hakemistoon (tämän voi muuttaa tässä vaiheessa). Olen ilmoittanut 64 Gt:n koon noudattaakseni Windows 11:n vaatimuksia, mutta tässäkin tapauksessa voidaan määrittää pienempi koko. Luo VM napsauttamalla "**Create**"!



![Image](assets/fr/015.webp)



Tässä vaiheessa VM on inventaariossamme, se on määritetty, mutta käyttöjärjestelmää ei ole asennettu. Meidän on viimeisteltävä VM:n kokoonpano ennen sen käynnistämistä.



### B. ISO-kuvan määrittäminen VirtualBox VM:lle



Windows 11:n tai minkä tahansa muun järjestelmän asentamiseen tarvitaan asennuslähteitä. Useimmiten käytämme ISO-muotoista levykuvaa käyttöjärjestelmän asentamiseen. **On tarpeen ladata Windows 11:n ISO-kuva VM:n virtuaaliseen DVD-asemaan



Napsauta VirtualBoxin inventaariossa olevaa VM:ää (1) ja sitten "**Konfiguraatio**"-painiketta (2), josta pääset tämän virtuaalikoneen yleisiin asetuksiin. Tätä valikkoa käytetään resurssien hallintaan (esim. RAM-muistin lisääminen, suorittimen määrittäminen jne.). Napsauta vasemmalla olevaa "**Storage**" (3), DVD-aseman kohdalla, jossa lukee toistaiseksi "**Empty**" (4), napsauta sitten DVD:n muotoista kuvaketta (5) ja "**Choose a disk file**".



![Image](assets/fr/016.webp)



Valitse sen käyttöjärjestelmän ISO-kuva, jonka haluat asentaa, ja napsauta sitten OK. Näen tämän:



![Image](assets/fr/017.webp)



Pysy VM:n "**Konfiguraatio**"-osiossa, minulla on vielä muutama asia selitettävänä.



### C. VM-verkkoyhteys



Siirry vasemmalla olevaan "**Verkko**"-osioon. Tässä osiossa voit hallita virtuaalikoneen verkkoa: virtuaalisten verkkoliitäntöjen määrä (enintään 4 per VM), MAC Address ja verkon käyttötapa (NAT, siltayhteys, sisäverkko jne.). **Jos haluat, että virtuaalikoneellasi on pääsy Internetiin, valitse "NAT" tai "Bridge Access "**, mutta tämä toinen tila edellyttää, että DHCP-palvelin on aktiivinen verkossa, tai sinun on määritettävä IP Address manuaalisesti.



Huomautus: palaan verkko-osioon tarkemmin erillisessä artikkelissa.



![Image](assets/fr/018.webp)



### D. Virtuaalisten prosessoreiden määrä



Kuten fyysinen tietokone, virtuaalikone tarvitsee toimiakseen RAM-muistia, Hard-levyn ja prosessorin. Kun loimme VM:n, olet ehkä huomannut, että ohjattu toiminto ei sisältänyt prosessorin määritystä. Tämä voidaan kuitenkin määrittää milloin tahansa "**System**"-välilehden ja sitten "**Processor**"-välilehden kautta, jossa voit valita virtuaaliprosessoreiden määrän.



Huomautus: "**Enable VT-x/AMD-v nested**" -vaihtoehto vaaditaan nested virtualisointia varten.



Minun tapauksessani virtuaalikoneessa on 2 virtuaalista prosessoria:



![Image](assets/fr/019.webp)



** Älä epäröi tutustua konfigurointivalikon muihin osioihin.



### E. Ensimmäinen käynnistys ja käyttöjärjestelmän asennus



Voit käynnistää virtuaalikoneen valitsemalla sen inventaariosta ja napsauttamalla "**Start**"-painiketta. Avautuu toinen ikkuna, joka antaa visuaalisen yleiskuvan VM:stä.



![Image](assets/fr/020.webp)



Auts, saan ikävän virheen, eikä virtuaalikoneeni käynnisty! Virhe on "Login failed for virtual machine..." seuraavin tiedoin:



```shell
Not in a hypervisor partition (HPV=0)
AMD-V is disabled in the BIOS (or by the host OS)
```



Itse asiassa tämä on normaalia, koska **virtualisointiominaisuus ei ole käytössä tietokoneessani**! Ongelman korjaamiseksi sinun on käynnistettävä tietokone uudelleen, jotta pääset BIOSiin ja voit ottaa virtualisoinnin käyttöön.



![Image](assets/fr/021.webp)



Odottamatta käynnistän tietokoneen uudelleen ja **painan "SUPPR"-näppäintä päästäkseni ASUS-emolevyn BIOSiin** (näppäin voi vaihdella koneesta riippuen, ja se voi olla esimerkiksi F2). Virtualisoinnin aktivoimiseksi minun tapauksessani "SVM Mode" on otettava käyttöön. Tässäkin tapauksessa emolevyltä toiselle, valmistajalta toiselle, nimi voi muuttua. Etsi toimintoa, jossa viitataan **AMD-V** (AMD-suorittimelle) tai **Intel VT-x** (Intel-suorittimelle).



![Image](assets/fr/022.webp)



Kun tämä on tehty, tallenna muutos ja käynnistä fyysinen kone uudelleen... Tällä kertaa **VirtualBox voi käynnistää virtuaalikoneen** ja ladata Windowsin ISO-kuvan asentaakseen käyttöjärjestelmän! 🙂 



![Image](assets/fr/023.webp)



Windows 11 -virtuaalikoneemme fyysisessä isäntätietokoneessa, johon VirtualBox on asennettu, näemme, että Windows 11 -virtuaalikoneen kansio sisältää useita tiedostoja.





- VBOX**-tiedosto (XML-muodossa), joka vastaa VM-konfiguraatiota (RAM-muisti, CPU jne.)
- VBOX-PREV**-tiedosto on varmuuskopio edellisestä kokoonpanosta
- VDI**-tiedosto vastaa virtuaalista Hard-levyä dynaamisessa tilassa, joten sen koko on tällä hetkellä vain 13 Gt, kun sen enimmäiskoko on 64 Gt
- NVRAM**-tiedosto sisältää virtuaalikoneen BIOS-tilan, joka vastaa fyysisen koneen haihtumatonta muistia



![Image](assets/fr/024.webp)



## V. Päätelmät



**VirtualBox on nyt toiminnassa fyysisessä Windows 11 -koneessamme! Jäljellä on enää sen hyödyntäminen ja virtuaalikoneiden luominen!** Palaan Windows 11:n asentamiseen VirtualBox VM:ään toisessa artikkelissa. Jos haluat Windows 10:n, Windows Serverin tai Linux-jakelun (Ubuntu, Debian jne.), anna meidän opastaa sinua!