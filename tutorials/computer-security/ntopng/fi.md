---
name: Ntopng
description: Seuraa verkkoasi ntopng:n avulla
---
![cover](assets/cover.webp)



___



*Tämä opetusohjelma perustuu Florian Ducheminin alkuperäiseen sisältöön, joka on julkaistu [IT-Connect](https://www.it-connect.fr/). Lisenssi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Alkuperäiseen tekstiin on saatettu tehdä muutoksia.*



___



## I. Esittely



**Verkon virtauksen valvonta on tärkeä osa yritysverkkoa, olipa kyse verkon sujuvuuden tarkistamisesta, selkeän kuvan saamisesta käytöstä tai suorituskykytilastojen laatimisesta**. Se auttaa ennakoimaan infrastruktuuriin tehtäviä muutoksia ja varmistamaan käyttäjille laadukkaan käytön (tunnetaan myös nimellä QoE, joka tarkoittaa *Quality of Experience*, toisin kuin QoS).



Tätä varten on olemassa monia tekniikoita ja ohjelmistoja/protokollia. Esimerkiksi Ciscon kehittämän Netflow-ohjelman avulla voidaan hakea IP-virtatilastoja Interface:sta, mutta sen käyttö on rajoitettu yhteensopiviin laitteisiin.



Siksi esittelen tässä oppaassa **Ntop**:n ja näytän, miten voit käyttää sitä infrastruktuurissasi pitämään silmällä verkon käyttöä.



Ntop on avoimen lähdekoodin ohjelmisto, joka voidaan asentaa mihin tahansa Linux-koneeseen. Se on ilmainen ja voi kerätä seuraavia tietoja:





- Kaistanleveyden käyttö
- Tärkeimmät asiakkaat
- Tärkeimmät kohteet
- Käytetyt pöytäkirjat
- Käytetyt sovellukset
- Käytetyt portit
- Jne.



Nyt nimetty uudelleen **Ntopng (New Generation)**, se tarjoaa monia perustoimintoja ilmaiseksi. Saatavilla on myös kaupallinen versio, joka mahdollistaa määritettyjen hälytysten viennin SIEM-tyyppisiin ohjelmistoihin tai liikenteen suodattamisen suoraan koettimesta määritetyillä säännöillä.



## II. Edellytykset



Ntop-anturin asennus vaihtelee laitteiston ja ympäristön mukaan. En siis aio antaa sinulle tässä askel askeleelta opasta, vaan hahmotan eri mahdollisuudet.



### A. Sisäinen tila



Jos sinulla on pfSense-, OPNSense- tai Endian-palomuuri tuotannossa tai jopa Linux-työasema, jossa on NFTables, hyviä uutisia! Voit asentaa Ntopng:n suoraan ja aloittaa rajapintojesi valvonnan.



Tämän tekniikan etuna on, että se ei vaadi lisälaitteita. Toisaalta se lisää resurssien käyttöä, joten varmista, että käytössäsi on riittävä laitteisto tai riittävän kokoinen VM (vähintään 2 ydintä ja 2BG RAM-muistia).



### B. TAP / SPAN-tila



**Hana** on **verkkolaite, joka kopioi sen läpi kulkevan liikenteen ja lähettää sen toiselle laitteelle.** Tämän laitteen etuna on, että se ei vaadi muutoksia olemassa olevaan infrastruktuuriin, ja se voidaan sijoittaa minne tahansa tarkkailemaan tiettyjä verkon osia tai ydinkytkimen ja reunareitittimen väliin analysoimaan Internetiin tai Internetistä tulevaa liikennettä.



Tämäntyyppisten laitteiden suuri haittapuoli on niiden hinta. Nykypäivän gigabitin verkoissa passiivinen kuuntelulaite ei pysty kunnolla sieppaamaan verkkoliikennettä, joten tarvitaan aktiivinen laite, joka maksaa noin 200 euroa (vähintään).



**SPAN**-tilaa, joka tunnetaan myös nimellä **porttipeilaus**, käytetään kytkimessä liikenteen välittämiseen yhdestä portista toiseen. Tämä on ylivoimaisesti suosikkimenetelmäni, koska se on helppo ottaa käyttöön ja koska sen avulla voit tapin tavoin valvoa osaa verkosta tai koko verkkoa haluamallasi tavalla. Siinä on kuitenkin kaksi haittaa: kytkimen on integroitava tämä toiminto, ja sen käyttö voi lisätä kytkimen prosessorikuormaa.



### C. Reititin-tila



On täysin mahdollista asentaa reititin Linuxissa ja asentaa ntopng siihen. Menetelmän ainoa haittapuoli on, että se muuttaa verkkoa, joko sen sisäistä osoitteistoa tai "oikean" reitittimesi ja lisättävän reitittimen välistä osoitteistoa.



Huomautus: lukijoille artikkelin [Luo Wifi reititin Raspberry Pi ja RaspAP](https://www.it-connect.fr/creer-un-routeur-wifi-avec-un-raspberry-pi-et-raspap/) se on täysin mahdollista asentaa ntopng teidän Rpi saada tarkkoja tilastoja!



### D. Siltatila



Mielenkiintoinen vaihtoehto on käyttää **Linux-konetta siltaustilassa.** Kahden laitteen väliin sijoitettu Linux-kone mahdollistaa kaiken liikenteen tallentamisen ilman, että infrastruktuurin tai sen laitteiden konfigurointiin tarvitsee puuttua. Koska vanhalla koneella voidaan hoitaa tämä tehtävä, myös tämän menetelmän kustannukset voivat olla houkuttelevat. Huomaa, että ollakseen optimaalinen laitteessa pitäisi olla kolme verkkokorttia, kaksi siltaustilassa ja yksi Interface:n ja SSH:n käyttöön. On mahdollista käyttää vain kahta korttia, mutta silloin myös laitteen hallintaliikenne kaapataan....



Aion siis käyttää **tätä viimeistä tilaa**. Käytännön syistä käytän esittelyssä virtuaalikoneita, mutta menetelmä on sama myös fyysisissä koneissa.



## III. Koettimen valmistelu Interface-sillan avulla



Valitsin koettimeksi **Debian 11** -koneen minimaalisessa asennuksessa.



Ensimmäinen askel, aina sama, päivitä :



```
apt-get update && apt-get upgrade
```



Asenna sitten **bridge-utils**-paketti, jonka avulla voimme luoda sillan:



```
apt-get install bridge-utils
```



Asennuksen jälkeen ensimmäinen huomioitava asia on verkkokorttien nykyinen nimi. Debianissa tämä nimi voi olla monessa eri muodossa, ja tarvitsemme sitä konfiguroinnissa.



Yksinkertainen **ip add**-komento palauttaa nämä tiedot:



![Image](assets/fr/016.webp)



Tässä näkyy 3 liitäntää:





- Lo**: tämä on loopback Interface; se on virtuaalinen Interface, joka "silmukoi" laitteiden yli. Periaatteessa tätä Interface:a, jonka Address on 127.0.0.1 (vaikka mikä tahansa Address 127.0.0.0.0/8:ssa kelpaa, koska tämä alue on varattu tätä tarkoitusta varten), käytetään yhteydenottoon itse laitteeseen. Jos olet asentanut web-sivuston työasemallesi (esimerkiksi WAMPP:n avulla), olet luultavasti käyttänyt "*localhost*"-osoitetta Address:ää jossain vaiheessa näyttääksesi omalla koneellasi isännöidyn sivuston. Tämä isäntänimi liittyy Address:n 127.0.0.0.1:een ja siten Interface:n silmukkaverkkoon.
- ens33**: tämä on ensimmäinen Interface:ni, joka sai Address:n DHCP:ltä
- ens36**: toinen Interface



Nyt kun minulla on kaikki tiedot, voin muuttaa */etc/network/interfaces*-tiedostoa luodakseni sillan. Tällä hetkellä se näyttää tältä (voi vaihdella):



```
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug ens33
iface ens33 inet dhcp
# This is an autoconfigured IPv6 interface
iface ens33 inet6 auto
```



Ensimmäinen osa koskee minun loopback Interface:a, johon en aio koskea, ja sen jälkeen Interface ens33. Muutokset koskevat toisen Interface:n (ens36) lisäämistä ja sillan konfigurointia näiden kahden liitännän avulla:



```
# The primary network interface
auto ens33
iface ens33 inet manual

#The secondary network interface
auto ens36
iface ens36 inet manual
```



Seuraavassa on joitakin selityksiä näistä ensimmäisistä muutoksista:





- auto *Interface***: käynnistää Interface:n automaattisesti järjestelmän käynnistyessä
- iface *Interface* inet manual** : Interface:n käyttö ilman IP Address:tä. Kuten avainsana "static" määrittää staattisen IP Address:n tai "dhcp" käyttää dynaamista osoitteistusta



Muutokset jatkuvat:



```
# Bridge interface
auto br0
iface br0 inet static
address 192.168.1.23
netmask 255.255.255.0
gateway 192.168.1.1
bridge_ports ens33 ens36
bridge_stp off
```



Seuraavassa on jälleen muutama selitys:





- iface br0 inet static**: Tässä olen määritellyt Interface-siltani (*br0*) staattisen Address:n kanssa.
- Address, verkkomassa, yhdyskäytävä**: piirilevyn osoitetiedot
- bridge_ports**: siltaan sisällytettävät rajapinnat
- bridge_stp**: Spanning Tree -protokollaa käytetään kytkimiä yhdistettäessä, jotta voidaan havaita redundantit linkit ja välttää silmukat. Koska silta voidaan asettaa kahden verkkopolun väliin, se voi olla silmukan lähde, minkä vuoksi tämä protokolla voidaan ottaa käyttöön. En tarvitse sitä täällä, joten poistan sen käytöstä.



Tallenna muutokset ja käynnistä verkko uudelleen:



```
systemctl restart networking
```



Tarkista muutokset näyttämällä komennon **ip** add tulos uudelleen:



![Image](assets/fr/021.webp)


Näet selvästi **uusi Interface:ni "*br0*" ja sille määrittämäni IP Address:n.** Näet muuten myös, että kaksi fyysistä liitäntää ovat tosiaan "UP", mutta niillä ei ole IP Address:ta.



## IV. NtopNG:n asentaminen



Nyt kun luotain pystyy nuuskimaan verkkoni ja reitittimen välistä liikennettä, jäljellä on enää ntopng-asennus. Tee tämä muuttamalla ensin */etc/apt/sources.list*-tiedostoa ja lisäämällä **contrib** jokaisen **deb**- tai **deb-src**-alkuisen rivin loppuun.



Oletusarvoisesti pakettilähteet sisältävät vain DFSG (*Debian Free Sotftware Guidelines*) -yhteensopivia paketteja, jotka tunnistetaan **main**-avainsanalla. Voit myös lisätä näitä lähteitä:





- contrib**: paketit, jotka sisältävät DFSG-yhteensopivia ohjelmistoja, mutta käyttävät riippuvuuksia, jotka eivät ole osa **main**-haaraa
- non-free**: sisältää paketteja, jotka eivät ole DFSG-yhteensopivia



Esimerkki rivistä tiedostossa /etc/apt/sources.list :



```
deb http://deb.debian.org/debian/ bullseye main
```



Lisään siis vain sanan **contrib** tällaisiin riveihin.



Loput vaiheet on lueteltu [NtopNG]-sivustolla (https://packages.ntop.org/apt/), jossa Debian 11:n osalta sinun on lisättävä Ntop-lähteet tulevaa asennusta varten. Tämä lisäys on automatisoitu käyttämällä :



```
wget https://packages.ntop.org/apt/bullseye/all/apt-ntop.deb
apt install ./apt-ntop.deb
```



Sitten tulee varsinainen asennusvaihe:



```
apt-get clean all
apt-get update
apt-get install ntopng
```



Ensimmäinen komento poistaa apt-paketinhallinnan välimuistin. Toinen päivittää pakettiluettelon ja kolmas asentaa NtopNG:n.



Asennuksen jälkeen **NtopNG-ohjelmisto on suoraan käytettävissä Debian-koneen portissa 3000**. Minulle se on siis `http://192.168.1.23:3000`



![Image](assets/fr/022.webp)



NtopNG:n kotisivu



Oletustunnus ja salasana näytetään, joten sinun tarvitsee vain syöttää ne!



## V. NtopNG:n käyttö



Kun kirjaudut sisään ensimmäisen kerran, sinua pyydetään ensimmäiseksi vaihtamaan oletusarvoinen ylläpitäjän salasana ja kieli. Valitettavasti ranska ei ole yksi niistä.



Sitten saavut kojelaudalle:



![Image](assets/fr/023.webp)



NtopNG kojelauta



Älä totu tähän! Jos huomaat keltaisen laatikon ruudun yläreunassa, näet lauseen: "*Lisenssi päättyy 04:57*". Oletusarvoisesti asennus käynnistää NtopNG:n täysversion kokeiluversion, mutta (hyvin) rajoitetuksi ajaksi. Kun tämä "lähtölaskenta" on saavutettu, *yhteisö*-versio aktivoituu ja kojelauta muuttuu:



![Image](assets/fr/024.webp)



Uusi NtopNG-yhteisön kojelauta



Ensimmäiseksi on **tarkistettava, että oikea Interface kuuntelee**. Vasemmassa yläkulmassa olevasta käytettävissä olevien liitäntöjen pudotusluettelosta voit valita Interface:n, josta olemme kiinnostuneita: br0



![Image](assets/fr/025.webp)



Interface valinta



Uudessa ikkunassa näkyvät "Top Flaw Talkers" eli laitteet, jotka kommunikoivat eniten. Tässä minulla on vain kaksi asemaa, jotka näkyvät:



![Image](assets/fr/026.webp)



**Lähde-isännät näkyvät vasemmalla, kohteet oikealla ** Näin voit havainnollistaa kunkin isännän käyttämän kaistanleveyden kokonaismäärän ja saada kokonaiskuvan verkkoliikenteestä. Tämä ei ole huono, mutta voimme mennä pidemmälle...



Jos napsautan esimerkiksi kohtaa "*Hosts*", saan näkyviin kuvaajan, jossa näkyy jokaisen verkkoni hostin lähetys- ja vastaanottovirrankulutus. Tästä näen esimerkiksi, että pelkästään 192.168.1.37 vastaa 80 prosentista liikennettä:



![Image](assets/fr/027.webp)



Jos napsautan kyseisen isännän IP Address:tä, minut ohjataan yhteenvetosivulle:



![Image](assets/fr/028.webp)



Näen esimerkiksi, että se on VMWare-kone (tunnistamalla MAC Address:n KYLLÄ), että sen nimi on DESKTOP-GHEBGV1 (joten se on varmasti Windows-isäntä) JA minulla on **tilastot vastaanotetuista ja lähetetyistä paketeista sekä datan määrästä**.



Huomaat myös uuden valikon tämän yhteenvedon yläosassa. Ehdotan, että klikkaat "**Sovellukset**" nähdäksesi, mikä aiheuttaa niin paljon liikennettä:



![Image](assets/fr/017.webp)


Ha, näyttää siltä, että meillä on vastaus! Vasemmalla olevasta kuvaajasta **näemme, että 76,6 prosenttia sen liikenteestä on peräisin ... Windows Update**, joten tämä isäntä lataa päivityksiä!



NtopNG käyttää teknologiaa nimeltä DPI eli *Deep Packet Inspection*, jonka avulla se pystyy luokittelemaan jokaisen verkkovirran ja määrittelemään sen taustalla olevan sovelluksen (tai sovellusten perheen).



Näytän, että käynnistän YouTube-videon isännälläni:



![Image](assets/fr/018.webp)



**Liikenne tunnistettiin ja luokiteltiin välittömästi!



Huomautus: ilmeisistä syistä tämäntyyppiset ohjelmistot voivat herättää yksityisyysongelmia, joten ole varovainen käyttäessäsi niitä oikeissa olosuhteissa. Huomaa myös, että on mahdollista **anonymisoida tuloksia**, vaihtoehto löytyy kohdasta **Asetukset > Asetukset > Asetukset > Muut** ja sen nimi on "**Mask Host IP Address**".



## VI. Havaintoja ja hälytyksiä



NtopNG pystyy myös antamaan turvallisuushälytyksiä tietyistä syötteistä. Nämä löytyvät **Hälytykset** -valikosta vasemmanpuoleisesta bannerista. Tässä esimerkiksi minulla on yhteensä 2851 hälytystä, jotka on jaettu eri vakavuusasteisiin: Ilmoitus, Varoitus ja Virhe.



![Image](assets/fr/019.webp)



Katsotaanpa korkean kriittisyyden hälytyksiä, niitä on 17!



Klikkaamalla tätä kuviota saat näkyviin hälytysten tiedot. Tässä ei ole mitään hälyttävää, vaan kyseessä on väärä positiivinen hälytys, sillä päivitysten lataus luokitellaan binääritiedoston siirroksi HTTP-virrassa, mikä voi todellakin tarkoittaa hyökkäystä.



![Image](assets/fr/020.webp)



Koska käytän kuitenkin ilmaisversiota, en voi sulkea pois verkkotunnuksia tai isäntiä, jotka ovat hälytysten lähde, joten sinun on pidettävä niitä silmällä, jotta et jää paitsi jostain paljon huolestuttavammasta. NtopNG tekee generate-hälytyksiä, jos :





- Binääritiedoston lataaminen HTTP:n kautta
- Epäilyttävä DNS-liikenne
- Epästandardin portin käyttäminen
- SQL-injektioiden havaitseminen
- Cross-Site Scripting (XSS)
- Jne.



## VII. Päätelmät



Tässä opetusohjelmassa olemme nähneet, **miten NtopNG:n avulla voidaan perustaa luotain**, jonka avulla voimme **analysoida verkkoliikennettämme** ja visualisoida protokollien käyttöä ja kunkin isännän käyttöastetta, mutta myös havaita epäilyttävää liikennettä.



Valitettavasti en voi käsitellä kaikkia ominaisuuksia ja mahdollisuuksia tässä artikkelissa, mutta tutustu vapaasti!



Tämä ratkaisu voidaan ottaa käyttöön pysyvästi yrityksen infrastruktuurissa. NtopNG voi myös viedä tulokset InfluxDB-tietokantaan, jolloin voit luoda omia kojelautoja kolmannen osapuolen työkalulla, kuten Graphanalla.