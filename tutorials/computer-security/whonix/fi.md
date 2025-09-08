---
name: Whonix
description: Säilytä yksityisyytesi ja luottamuksellisuutesi.
---

![cover](assets/cover.webp)



**Whonix** on Linux-jakelu, joka perustuu **Debianiin** ja on suunniteltu tarjoamaan ympäristö, jossa yhdistyvät **turvallisuus**, **anonymiteetti** ja **yksityisyys**. Se on helppo oppia ja yhteensopiva eri käyttöliittymien kanssa (virtuaalikoneet, Qubes OS, Live-tila), ja se sisältää oletusarvoisesti verkkoliikenteen reitityksen **Torin** kautta, **kaksoispalomuurin** (yksi palomuuri yhdyskäytävässä ja toinen työasemassa), **täydellisen suojan IP/DNS-vuotoja vastaan** ja työkalut, joilla voit tehokkaasti peittää toimintasi verkon tarkkailijoilta, mukaan lukien Internet-palveluntarjoajalta. **Whonix** on enemmän kuin vain anonyymi järjestelmä, se on täydellinen turvallinen kehitysympäristö.



## Miksi valita Whonix?





- Ilmainen**: Whonix on avoimen lähdekoodin järjestelmä, joka on lisensoitu täysin ilmaiseksi, kuten useimmat Linux-jakelut. Sitä kehitetään avoimen lähdekoodin periaatteella, ja sillä on aktiivinen ja avoin yhteisö.
- Yksityisyys, turvallisuus ja anonymiteetti**: Whonixin päätavoitteena on tarjota erittäin turvallinen ympäristö, jossa kaikki tietosi on suojattu ja viestisi salattu Tor-verkon kautta.
- Helppokäyttöinen**: Whonix tarjoaa intuitiivisen, valmiiksi konfiguroidun graafisen Interface:n, joka sopii jopa aloitteleville käyttäjille. Sinun ei tarvitse olla asiantuntija voidaksesi hyötyä kehittyneestä suojauksesta.
- Ihanteellinen ympäristö turvalliselle kehitykselle**: Whonixin avulla voit kehittää, testata, tarkastaa tai suorittaa ohjelmia paljastamatta koskaan todellista IP Address:täsi tai paljastamatta selaus- tai verkkoviestintätottumuksiasi.
- Kertakäyttöistunnot ja Live-tila**: Whonix voidaan käynnistää Live-tilassa tai kertakäyttöisten koneiden kautta (esim. **Qubes OS**:n kautta), jolloin kriittiset tehtävät voidaan suorittaa jättämättä pysyviä jälkiä istunnon päätyttyä.
- Suhteellisen yksinkertainen asennus**: Valmiit kuvat toimitetaan nopeaa asennusta varten virtuaalikoneisiin (VirtualBox, KVM, Qubes). Järjestelmä on dokumentoitu ja sitä päivitetään säännöllisesti.



## Asennus ja konfigurointi



Ennen kuin siirryt Whonixin asennukseen, on tärkeää huomata, että tämä jakelu **ei ole vielä virallisesti saatavilla** pääjärjestelmänä, joka voidaan asentaa suoraan Hard -levylle (bare metal -tilassa). Toisin sanoen, et **voi vielä asentaa Whonixia klassisena pääkäyttöjärjestelmänä**, kuten Ubuntua tai tavallista Debiania.



Saatavilla on kuitenkin useita versioita, joiden avulla Whonixia voidaan käyttää **volatiivi** (Live-tila, tilapäiset istunnot) tai **persistentti** (virtuaalikoneiden tai Qubes OS:ään integroituna).



Pitkäkestoiseen ja vakaaseen käyttöön **virtualisointi on tällä hetkellä ainoa virallisesti suositeltu menetelmä**. Voit käyttää Whonixia käyttämällä **VirtualBoxia** (Whonix-Gateway ja Whonix-Workstation) tai integroida sen **Qubes OS**:n kaltaiseen järjestelmään. Tässä ohjeessa keskitymme VirtualBox-asennukseen.



### Edellytykset



Ennen kuin voit asentaa Whonixin virtuaalitilaan, varmista, että koneesi täyttää tekniset vähimmäisvaatimukset. Virtualisointi vaatii tiettyjä resursseja, joita kaikki tietokoneet eivät pysty tarjoamaan. Siksi on tärkeää, että prosessorisi tukee virtualisointitekniikkaa (Intel VT-x tai AMD-V) ja että tämä vaihtoehto on otettu käyttöön BIOS/UEFI:ssä.



Tässä ovat suositellut tekniset tiedot, jotta Whonixin käyttö olisi sujuvaa ja vakaata:





- RAM-muisti (Random Access Memory) **: vähintään **8 Gt** on erittäin suositeltava. Mitä enemmän RAM-muistia sinulla on, sitä enemmän resursseja voit jakaa virtuaalikoneille (Gateway ja Workstation), mikä parantaa suorituskykyä.
- Käytettävissä oleva levytila**: varaa vähintään 30 Gt vapaata levytilaa**. Tämä sisältää kahden virtuaalikoneen, järjestelmätiedostojen ja mahdollisten tietojen tai tilannekuvien tarvitseman tilan.
- Prosessori**: Suositellaan prosessoria, jossa on vähintään **4 fyysistä ydintä** (8 loogista säiettä), erityisesti jos haluat käyttää muita palveluja tai työkaluja rinnakkain.



### Lataa Whonix



Whonix on saatavana useissa eri versioissa sen mukaan, millaisessa ympäristössä haluat sitä käyttää. Useimmille käyttäjille (Windows, Linux tai MacOs) VirtualBox-versio on helpoin asentaa. Voit ladata kuvan suoraan [virallisilta verkkosivuilta](https://www.whonix.org/wiki/VirtualBox).



⚠️ Whonix **ei ole yhteensopiva** MacBookien kanssa, joissa käytetään Apple Silicon -prosessoreita (ARM-arkkitehtuuri).



## VirtualBoxin asentaminen



Whonixin käyttämiseen tarvitaan **hypervisor**, kuten VirtualBox, Qubes tai KVM.



Kun olet ladannut tiedoston, asenna se kuten mikä tahansa muu ohjelmisto. Hyväksy oletusasetukset, ellei sinulla ole erityisiä vaatimuksia. Oletko eksynyt? Tutustu VirtualBoxin käyttöoppaaseen.



https://planb.network/tutorials/computer-security/operating-system/virtualbox-6472f5be-10ce-4a07-8b24-097bfbcedd65
### Whonixin tuominen



Kun VirtualBox on asennettu, voit tuoda aiemmin lataamasi Whonixin `.ova`-tiedostot (`Whonix-Gateway-Xfce.ova` ja `Whonix-Workstation-Xfce.ova`).



Avaa VirtualBox ja napsauta sitten **Tiedosto → Tuo sovellus**.


Valitse vastaava `.ova`-tiedosto (aloita Gatewaystä).



![0_03](assets/fr/03.webp)



Valitse sijainti, johon Whonix-virtuaalikoneen tiedostot tallennetaan.



![0_04](assets/fr/04.webp)



Hyväksy käyttöehdot, käynnistä tuonti ja odota, että prosessi päättyy.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)


### Whonix-konfiguraatio



Ennen Whonixin käynnistämistä on tärkeää säätää joitakin **järjestelmäasetuksia** paremman suorituskyvyn varmistamiseksi:



Valitse **Whonix-Workstation-Xfce**-virtuaalikone ja napsauta sitten **Configuration**.



![0_06](assets/fr/07.webp)



Siirry **System**-välilehdelle, jossa RAM-muistin oletusarvoinen varaus on 2048 Mt. Suosittelemme, että **nostat sen 4096 MB:iin (4 GB)** sujuvuuden parantamiseksi, varsinkin jos aiot avata useita sovelluksia tai työskennellä pitkiä istuntoja. Gateway voi pysyä 2048 Mt:ssä, ellet käytä useita Tor-yhteyksiä rinnakkain.



![0_08](assets/fr/08.webp)



### Whonixin käytön aloittaminen



Jotta Whonix toimisi kunnolla ja turvallisesti, **sinun on noudatettava tätä käynnistysjärjestystä**:



Käynnistä ensin **Whonix-Gateway-Xfce**-kone. Tämä kone vastaa kaiken liikenteen reitittämisestä **Tor**-verkon kautta. Jos yhdyskäytävä ei ole käynnissä, mikään liikenne ei ohjaudu Torin kautta ja menetät anonymiteettisi.



![0_09](assets/fr/09.webp)



Kun yhdyskäytävä on täysin käynnistetty (näet Torin yhdistettynä), voit käynnistää **Whonix-Workstation-Xfce**:n, joka muodostaa automaattisesti yhteyden yhdyskäytävän kautta.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



### Järjestelmäpäivitys



Syötä terminaaliin seuraava komento päivittääksesi pakettiluettelon:



```shell
sudo apt update
```



Asenna saatavilla olevat päivitykset seuraavalla komennolla:



```shell
sudo apt full-upgrade
```



## Tutustu Whonixiin



**Whonix** on järjestelmä, joka on suunniteltu tarjoamaan **turvallisen**, **anonyymin** ja **luottamuksellisen** tietojenkäsittely-ympäristön, joka on ihanteellinen Internetissä surffailuun vaarantamatta henkilöllisyyttäsi tai tietojasi. Tämän saavuttamiseksi se sisältää useita hyödyllisiä jokapäiväisiä sovelluksia, jotka on suunniteltu vahvistamaan digitaalista tietoturvaasi heti alusta alkaen.


### KeepassXC



**KeePassXC** on Whonixin integroitu salasanahallinta. Sen avulla voit **luoda, tallentaa ja hallita** salasanojasi turvallisesti ilman, että sinun tarvitsee muistaa niitä kaikkia manuaalisesti. Salasanat tallennetaan **salattuun tietokantaan**, joka on suojattu pääsalasanalla.



### Tor-selain



**Tor Browser** on Whonixin oletusarvoinen verkkoselain. Se perustuu **Tor**-verkkoon, joka ohjaa tietoliikenteesi useiden eri puolilla maailmaa sijaitsevien releiden kautta, jolloin todellisen IP Address:n tunnistaminen on käytännössä mahdotonta.



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

### Electrum Bitcoin Wallet



**Electrum** on kevyt ja nopea Bitcoin Wallet, joka on esiasennettu Whonixiin ja jonka avulla voit hallita **kryptovaluuttatransaktioita** anonyymisti. Se ei lataa koko Blockchain:ta, vaan käyttää etäpalvelimia tarvittavien tietojen hankkimiseen, joten se on paljon kevyempi kuin täysi Wallet.



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

Whonix on enemmän kuin pelkkä käyttöjärjestelmä: se on todellinen **turvallinen ympäristö**, joka on suunniteltu suojaamaan anonymiteettiäsi, yksityisyyttäsi ja arkaluonteisia toimintojasi. Tor-pohjaisen arkkitehtuurin, Gatewayn ja työaseman välisen älykkään osioinnin sekä esiasennettujen työkalujen, kuten Tor Browserin, KeePassXC:n ja Electrumin, ansiosta se tarjoaa avaimet käteen -ratkaisun kaikille, jotka haluavat **selata nimettömänä**, **työskennellä turvallisesti** tai **käsitellä luottamuksellisia tietoja**.



Jos haluat vahvistaa Unix-järjestelmän tietoturvaa, tutustu koneen tarkastamista koskevaan oppaaseemme: tarkista, onko käyttöjärjestelmässäsi tietoturva-aukkoja, ja varmista, että tietosi eivät ole vaarassa.



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af