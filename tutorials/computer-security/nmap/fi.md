---
name: Nmap
description: Master Nmap verkon kartoitusta ja haavoittuvuuksien skannausta varten
---

![cover](assets/cover.webp)



*Tämä opetusohjelma perustuu Mickael Dorignyn alkuperäiseen sisältöön, joka on julkaistu osoitteessa [IT-Connect](https://www.it-connect.fr/). Lisenssi [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Alkuperäiseen tekstiin on tehty muutoksia.*



___



Tervetuloa tähän Nmapin esittelyoppaaseen, joka on tarkoitettu kaikille, jotka haluavat hallita tätä tehokasta verkon skannaustyökalua. Tavoitteena on antaa sinulle perustiedot, joita tarvitset Nmapin tehokkaaseen päivittäiseen käyttöön.



Nmap on monipuolinen työkalu, jota IT-, verkko- ja kyberturva-alan ammattilaiset käyttävät laajalti diagnostiikkaan, verkon löytämiseen ja tietoturvatarkastuksiin. Tämä opetusohjelma on suunnattu niille, jotka ovat uusia näillä aloilla ja haluavat oppia Nmapin perusteet. Järjestelmän- ja verkonhallinnan perustiedot ovat suositeltavia.



Opit Nmapin perusteet, kuinka tehdä porttiskannauksia, tunnistaa verkon aktiiviset isännät, tunnistaa palveluversiot ja käyttöjärjestelmät, tehdä haavoittuvuusskannauksia ja paljon muuta. Jokainen osio sisältää yksityiskohtaisia selityksiä ja käytännön esimerkkejä, joiden avulla hallitset Nmapin käytön erilaisissa yhteyksissä.



Tämän ohjeen lopussa sinulla on vankka käsitys Nmapista ja pystyt käyttämään sitä tehokkaasti parantaaksesi verkkojesi turvallisuutta ja hallintaa. Nauti lukemisesta.



## 1 - Johdatus Nmapiin: Mikä on Nmap?



### I. Esittely



Tässä ensimmäisessä osassa tarkastelemme Nmap-verkon skannaustyökalua. Tarkastelemme keskeisiä Elements-tietoja, jotka sinun on tiedettävä tästä työkalusta ja siitä, miten se toimii yleisesti. Tämä auttaa meitä ymmärtämään paremmin loput opetusohjelmasta.



### II. Nmap-työkalun esittely



Nmap on ilmainen, avoimen lähdekoodin työkalu, jota käytetään **verkon löytämiseen, kartoittamiseen ja tietoturvatarkastukseen**. Sitä voidaan käyttää myös muihin tehtäviin, kuten **verkon inventointiin, diagnostiikkaan tai valvontaan**.



Se voi määrittää, ovatko kohteena olevan verkon isännät aktiivisia ja tavoitettavissa, mitkä verkkopalvelut ovat alttiina, mitkä versiot ja teknologiat ovat käytössä ja muita hyödyllisiä analyysitietoja. Nmapia voidaan käyttää yksittäisen palvelun skannaamiseen tietyllä koneella tai laajoilla verkkoalueilla, jopa koko Internetissä.



Nmapin vahvuuksia on monia:





- Tehokas ja joustava**: Nmap voi skannata suuria verkkoja ja käyttää kehittyneitä havaitsemistekniikoita. Se tukee UDP:tä, TCP:tä, ICMP:tä, IPv4:ää ja IPv6:ta, ja se voi suorittaa versiohavaintoja, haavoittuvuusskannauksia tai protokollakohtaisia vuorovaikutustoimenpiteitä. Sen arkkitehtuuri on modulaarinen erityisesti NSE-skriptien (Nmap Scripting Engine) ansiosta, joita tarkastelemme myöhemmin tässä oppaassa.
- Helppokäyttöisyys**: virallista dokumentaatiota on runsaasti ja se on korkealaatuista. Myös lukuisat yhteisön resurssit auttavat alkuun pääsemisessä.
- Suosio ja pitkäikäisyys**: Nmap on ollut alan referenssi vuodesta 1998. Tämän päivityksen aikaan nykyinen versio on 7.95. Vaikka erityistehtäviin on olemassa muitakin työkaluja, Nmap on edelleen välttämätön verkkokartoitukseen ja -analyysiin.



**Nmap elokuvissa**



Nmap on yksi niistä harvoista tietoturvatyökaluista, jotka ovat saavuttaneet tietynlaista mainetta suuren yleisön keskuudessa. Se esiintyy elokuvassa _Matrix Reloaded_, jossa Trinity käyttää sitä murtautuakseen järjestelmään:



![nmap-image](assets/fr/01.webp)



matriisi: Nmap



Hän esiintyy myös muissa elokuvissa.



**Palaute



Järjestelmänvalvojana ja myöhemmin kyberturvallisuuden tarkastajana ja viidentestarina **käytän Nmapia lähes päivittäin**, ja **suositan** sitä säännöllisesti järjestelmänvalvojille, jotka haluavat vahvistaa verkonhallintaansa ja parantaa diagnostiikkakykyään.



### III. Korkean tason toiminta



Nmap on saatavilla Linuxille, Windowsille ja macOS:lle. Se on kirjoitettu pääasiassa C:llä, C++:lla ja Lualla (NSE-skriptejä varten). Sitä käytetään pääasiassa komentorivillä, vaikka saatavilla on myös graafisia käyttöliittymiä, kuten Zenmap. Suosittelemme kuitenkin, että aloitat komentoriviltä, jotta ymmärrät paremmin, miten se toimii.



Yksinkertainen esimerkki:



```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```



Tämä komento selitetään yksityiskohtaisesti myöhemmin. Tässä ohjeessa käytämme Nmapia Linuxissa, mutta sen käyttö on samanlaista myös muissa järjestelmissä. Windowsissa Nmap luottaa **Npcap**-kirjastoon (joka korvaa nykyään vanhentuneen WinPcapin) verkkopakettien kaappaamiseen ja syöttämiseen.



Nmapia käytetään kuten tavanomaista binääriohjelmaa, kuten `ls` tai `ip`. Jotkin lisäominaisuudet saattavat vaatia korkeampia oikeuksia, koska työkalu manipuloi joskus paketteja epätavallisilla tavoilla provosoidakseen tiettyjä reaktioita kohdejärjestelmissä (erityisesti palvelun tai haavoittuvuuden havaitsemiseksi).



### IV. Nmapin käytön vaikutukset



Ennen Nmapin käyttöä on tärkeää olla tietoinen sen mahdollisista vaikutuksista verkkoihin ja järjestelmiin:





- Se voi lähettää **tuhansia tai jopa miljoonia paketteja** lyhyessä ajassa, mikä voi ylikuormittaa tietyt verkkoinfrastruktuurit.
- Se voi generate **väärennettyjä tai epätyypillisiä** paketteja, jotka todennäköisesti häiritsevät tiettyjä laitteita (erityisesti teollisuusjärjestelmiä).
- Se voi tuottaa **hyökkäyksen kaltaista käyttäytymistä**, mikä voi aiheuttaa hälytyksiä turvajärjestelmissä (palomuurit, IDS/IPS jne.).



Yleisesti ottaen **Nmap on hyvin puhelias työkalu**, sillä se tuottaa paljon liikennettä saadakseen mahdollisimman paljon tietoa. Siksi on suositeltavaa ymmärtää täysin, miten se toimii, ennen kuin sitä käytetään arkaluonteisissa tai tuotantoympäristöissä.



### V. Päätelmät



Tässä osassa esitellään Nmap ja sen tärkeimmät ominaisuudet. Olemme nähneet, että se on tärkeä, tehokas ja joustava verkkokartoitustyökalu. Olemme myös keskustelleet siitä, miten se toimii ja mitä varotoimia sitä käytettäessä on noudatettava, ja luoneet näin pohjan opetuksen seuraaville osille.



## 2 - Miksi käyttää Nmapia?



### I. Esittely



Tässä osassa tarkastelemme Nmap-verkon skannaustyökalun tärkeimpiä käyttötarkoituksia. Näemme, että sitä käytetään laajalti monissa yhteyksissä ja ammateissa, ja että sen hallitseminen on ehdottomasti hyödyllinen taito.



### II. Nmapin käyttö diagnostiikkaan ja valvontaan



Nmapia voidaan käyttää verkon diagnostiikkaan ja laajemmin valvontaan. Samalla tavalla kuin ping-mittauksen avulla voidaan määrittää, ovatko kaksi isäntäkohtaa yhteydessä toisiinsa, Nmapin avulla voidaan nopeasti määrittää, onko jokin isäntä aktiivinen tai onko jokin tietty palvelu toiminnassa. [Nmapin] (https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/ "Nmap") avulla voidaan saada tarkkoja tietoja isännän vasteajasta, pakettien kulkemasta reitistä, tietyn palvelun antamasta vastauksesta jne.



Seuraavaa komentoa ja tulosta voidaan käyttää esimerkiksi selvittämään nopeasti, onko isännän **192.168.1.18** verkkopalvelin aktiivinen ja vastaa oikein:



```
nmap --open -p 80 192.168.1.18
```



![nmap-image](assets/fr/02.webp)



*Käytä Nmapia verkkopalvelun tilan hakemiseen etäpalvelimelta.*



Nmapin käyttö on siis enemmän kuin kuuluisa "ping-testi" virheenkorjaus- tai diagnoosivaiheessa. Näemme myöhemmin, että Nmap käyttää useita menetelmiä, joilla se tunnistaa, mikä palvelu kuuntelee tiettyä porttia, mukaan lukien sen versio.



### III. Nmapin käyttäminen verkon kartoittamiseen



Verkkokartoittajana tämän työkalun päätavoitteena on verkon kartoitus. Sitä voidaan käyttää paikallisverkon sisällä tai useiden verkkojen, aliverkkojen ja VLANien välillä kaikkien tavoitettavissa olevien isäntien ja palvelujen luetteloimiseksi. Nmap tekee tästä tehtävästä paljon nopeamman ja tehokkaamman kuin mikään manuaalinen menetelmä.



Esimerkiksi seuraavaa komentoa voidaan käyttää tunnistamaan nopeasti aktiiviset isännät **192.168.1.0/24**-verkossa:



```
nmap -sn 192.168.1.0/24
```



*Huomautus: `-sP`-vaihtoehto on vanhentunut ja korvattu `-sn`-vaihtoehdolla.*



![nmap-image](assets/fr/03.webp)



*Nmapin käyttäminen tavoitettavien isäntien löytämiseen verkossa*



Myöhemmin näemme, että Nmap käyttää useita menetelmiä määrittääkseen, voidaanko isäntäkone pitää "aktiivisena", vaikka se ei a priori tarjoaisi mitään palveluja.



### IV. Nmapin käyttäminen suodatuskäytännön arviointiin



Nmapin etuna on se, että se on tosiasioihin perustuva: sen tuloksista voidaan tehdä konkreettisia havaintoja, toisin kuin mistä tahansa arkkitehtuuridokumentista tai suodatuskäytännöstä. Se on keskeinen väline arvioitaessa tietojärjestelmien lokeroimisen tehokkuutta, sillä sen avulla voidaan **tarkistaa, sovelletaanko suodatuskäytäntöä todella**.



Yritysverkossa parhaiden käytäntöjen mukaan järjestelmät on segmentoitava niiden roolin, kriittisyyden tai sijainnin mukaan. Suodatussäännöillä (jotka usein toteutetaan palomuurien avulla) on rajoitettava vyöhykkeiden välistä viestintää. Nämä määritykset ovat kuitenkin usein monimutkaisia ja alttiita virheille.



Mikään ei siis voita konkreettista testiä sen varmistamiseksi, että politiikkaa on noudatettu. Voit esimerkiksi tarkistaa, että arkaluontoisiin hallintapalveluihin (SSH, WinRM, MSSQL, MySQL jne.) ei pääse käsiksi käyttäjäalueelta.



**Nmapin käyttö suodatuskäytännön testaamiseen** olisi tehtävä järjestelmällisesti ennen kuin tällainen käytäntö otetaan tuotantoon. Valitettavasti tämä tarkastus jätetään usein tekemättä.



Kokemukseni mukaan monet konfigurointivirheet jäävät huomaamatta, jos validointitestejä ei ole. Yksinkertainen virhe IP-alueessa tai säännön virheellinen noudattaminen voi jättää oletettavasti eristetyn alueen haavoittuvaksi.



### V. Nmapin käyttö tietoturvatarkastukseen ja tunkeutumistestaukseen



Nmapissa on **paljon hyödyllisiä ominaisuuksia tietoturvan arviointia**, tunkeutumistestausta (pentestejä) ja valitettavasti myös hyökkääjiä varten.



Verkon etsintätoiminnot ovat ratkaisevan tärkeitä hyökkääjälle, jonka on ymmärrettävä verkon topologia ensimmäisen hyökkäyksen jälkeen. Nmap tarjoaa kuitenkin paljon muutakin: se integroi skriptausmoottorin, **joista monet on tarkoitettu haavoittuvuuksien havaitsemiseen**.



Tätä komentoa voidaan käyttää esimerkiksi sen tarkistamiseen, salliiko FTP-palvelu anonyymin yhteyden muodostamisen, ilman että yhteyden muodostamista tarvitsee tehdä manuaalisesti:



```
nmap --script ftp-anon -p 21 192.168.1.18
```



![nmap-image](assets/fr/04.webp)



*NSE-skriptin käyttäminen anonyymin FTP-todennuksen tarkistamiseen Nmap.*:n kautta



Nmap-haavoittuvuuksien havaitseminen on yksi tarkastuksen tai tunkeutumistestin ensimmäisistä vaiheista. Sen avulla voit nopeasti tunnistaa tietyt heikot kohdat ja optimoida analyysitoimesi.



Mutta varokaa: **haavoittuvuuksien skannaustyökaluilla on rajansa**. Nmap kattaa vain murto-osan uhkista, eikä se takaa, että järjestelmä on turvallinen, jos ongelmia ei havaita. Siksi on tärkeää **tietää, miten käytetyt skriptit toimivat**, eikä luottaa pelkästään niiden tuomioon.



### VI. Päätelmät



Olemme nähneet, että Nmapin hallitseminen voi kattaa monenlaisia käyttötapauksia diagnostiikasta ja seurannasta kartoitukseen, turvallisuuskäytäntöjen arviointiin ja haavoittuvuuksien skannaukseen. Seuraavassa osiossa siirrymme varsinaiseen asiaan ja asennamme Nmapin.




## 3 - Nmapin asentaminen ja konfigurointi



### I. Esittely



Tässä osiossa opimme, miten Nmap-verkonetsintätyökalu asennetaan Linux- ja Windows-käyttöjärjestelmiin. Tämän jakson lopussa meillä on kaikki tarvittava, jotta voimme alkaa käyttää Nmapia tulevissa moduuleissa. Lopuksi näemme, mitä oikeuksia se voi vaatia käytettäessä ja miksi.



### II. Nmapin asentaminen Linuxiin



Nmap suunniteltiin alun perin toimimaan GNU/Linux-käyttöjärjestelmissä. Sen pitkäikäisyyden ja suosion ansiosta se löytyy kaikkien tärkeimpien Unix-jakeluiden virallisista arkistoista. Tässä oppaassa käytän Debian-pohjaista käyttöjärjestelmää [Kali Linux](https://www.it-connect.fr/cours/debuter-avec-kali-linux/ "Kali Linux"). Mutta voit käyttää sitä aivan samalla tavalla klassisesta Debianista, CentOSista, Red Hatista tai mistä tahansa!



Debianissa voit tarkistaa, että Nmap on nykyisissä arkistoissa, käyttämällä seuraavaa komentoa:



```
# Debian and derivatives
$ sudo apt search ^nmap$
Sorting... Done
Full Text Search... Done
nmap/kali-rolling,now 7.94+git20230807.3be01efb1+dfsg-2+kali1 amd64
The Network Mapper

# Red Hat and derivatives
$ dnf search '^nmap$'
```



Vastaus osoittaa selvästi, että paketti "nmap" on olemassa arkistoissa (tässä tapauksessa Kali [Linuxin] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ "Linux")). Tästä eteenpäin voit asentaa Nmapin tavallisilla asennuskomennoilla, ei mitään aseistariisuvaa toistaiseksi 🙂:



```
# Debian and derivatives
sudo apt install nmap

# Red Hat and derivatives
sudo dnf install nmap
```



Tarkistaaksemme, että Nmap on asennettu oikein, näytämme sen version:



```
nmap --version
```



Tässä on odotettu tulos:



![nmap-image](assets/fr/05.webp)



nmapin nykyisen version näyttämisen tulos._



Huomaa, että tässä näytössä on "libpcap" (_Packet Capture Library_) -kirjasto ja sen versio. Nmap käyttää myös Wiresharkin käyttämää "libpcap"-kirjastoa pakettien luomiseen ja käsittelyyn sekä verkkoliikenteen kuunteluun.



### III Nmapin asentaminen Windowsiin



Asennus Windows-käyttöjärjestelmään aloitetaan lataamalla binääritiedosto viralliselta sivustolta (eikä mistään muualta!):





- Nmapin lataussivu virallisella verkkosivustolla: [https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)




Tämän jälkeen sinun on ladattava binääri nimeltä `nmap-<VERSIO>-setup.exe`:



![nmap-image](assets/fr/06.webp)



nmap for Windows -asennuksen binäärilataussivu



Kun olet saanut tämän binääritiedoston järjestelmääsi, voit asentaa Nmapin ajamalla sen. Asennus on suoraviivainen, ja voit jättää kaikki vaihtoehdot oletusasetuksiksi.



Minun refleksini on poistaa "zenmap (GUI Frontend)" -ruutu. Tämä on Nmapin graafinen Interface, jota en käytä enkä käsittele tässä oppaassa, mutta voit kokeilla sitä vapaasti, kun olet oppinut käyttämään Nmapin komentorivityökalua!



![nmap-image](assets/fr/07.webp)



zenmapin valinnaisen valinnan poistaminen, kun Nmap asennetaan Windowsissa



Nmapin asennuksen lopuksi ehdotetaan toista asennusta: "Npcap"-kirjaston asennusta:



![nmap-image](assets/fr/08.webp)



"Npcap"-kirjaston asennus, kun Nmap asennetaan Windowsissa



Tämä on kirjasto, johon Nmap tukeutuu hallitessaan verkkoviestintää, eli rakentaessaan, lähettäessään ja vastaanottaessaan verkkopaketteja. Olet luultavasti jo törmännyt tähän kirjastoon, jos käytät Wiresharkia Windowsissa, sillä myös se käyttää sitä ja vaatii asennuksen.



Kuten Linuxissa, voit varmistaa, että Nmap on asennettu avaamalla komentorivin tai [Powershell]-päätteellä (https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell") ja kirjoittamalla seuraavan komennon:



```
nmap --version
```



Tässä on odotettu tulos:



![nmap-image](assets/fr/09.webp)



nmapin nykyisen version näyttämisen tulos._



Nmap on nyt asennettu Windowsiin. Voit käyttää sitä täsmälleen samalla tavalla kuin Linuxissa noudattamalla tätä ohjetta.



### IV. Nmapin käyttöön tarvittavat paikalliset oikeudet



Mutta muuten, kun käytät Nmapia, **onko järjestelmällä oltava korkeammat paikalliset oikeudet?** Vastaus on: **Se riippuu**.



Perusmuodossaan, toisin sanoen ilman, että Nmapin vaihtoehtoja käytetään kovin pitkälle, se ei välttämättä vaadi etuoikeuksia. Huomaat kuitenkin pian, että on parempi käyttää Nmapia etuoikeutetussa ympäristössä ("root" Linuxissa, "administrator" tai vastaava Windowsissa), jotta voit käyttää sitä täysimääräisesti, vaikka vaarana on saada tämän kaltainen virheilmoitus:



![nmap-image](assets/fr/10.webp)



virheilmoitus Linuxissa, kun Nmapin asetukset vaativat pääkäyttäjän oikeuksia._



Olipa kyseessä sitten Linux tai Windows, Nmap pyytää sinulta monissa tapauksissa etuoikeutettuja käyttöoikeuksia. Tärkeimmät syyt ovat seuraavat (luettelo ei ole tyhjentävä):





- "Raakaverkkopakettien" muodostaminen**: Nmap pystyy käyttämään monenlaisia skannausmenetelmiä, mukaan lukien edistynyt pakettien manipulointi ja rakentaminen. Näin on esimerkiksi silloin, kun haluamme suorittaa TCP SYN-skannauksia, jotka eivät noudata TCP-vaihdon klassista _kolmitiekättelyä_. Tätä varten Nmapin on käytettävä muita kuin käyttöjärjestelmien omia funktioita, jotka osaavat vain kunnioittaa verkkoviestinnän hyviä käytäntöjä (se käyttää edellä mainittuja "Npcap"- ja "libcap"-kirjastoja). Koska Nmap ei tee asioita "tavanomaisella" tavalla, se pystyy päättelemään tiettyjä tietoja käyttöjärjestelmistä, palveluista ja tietyistä haavoittuvuuksista.





- Kuuntele verkkoliikennettä**: Jotkin Nmapin vaihtoehdoista edellyttävät, että se kuuntelee verkkoa saadakseen tiettyjä tietoja. Tätä toimintoa pidetään käyttöjärjestelmissä arkaluonteisena, koska sen avulla voit myös kuunnella järjestelmän muiden sovellusten viestintää. Aivan kuten Wireshark, myös Nmap tarvitsee tähän tiettyjä oikeuksia, jotka on helpompi saada olemalla suoraan etuoikeutetussa istunnossa.





- Kuuntelu etuoikeutetuissa porteissa**: käyttöjärjestelmissä portit 0-124 (TCP ja UDP) ovat etuoikeutettuja, eli ne on varattu jotenkin hyvin erityisiin käyttötarkoituksiin ja siksi suojattu. Vaikka tämä on nykyään hieman vanhentunut syy, on edelleen tarpeen saada tietyt oikeudet kuunnella näitä portteja, ja Nmapin on ehkä tehtävä se riippuen siitä, miten sitä käytetään.





- UDP-pakettien lähettäminen:** Vastaavasti verkkosovelluksen kuuntelu UDP-porteissa (tilaton protokolla) vaatii käyttöjärjestelmissä etuoikeudet. Siksi tarvitaan etuoikeutettu istunto, jos haluat suorittaa UDP-skannauksen, johon Nmapin on kuunneltava vastausta, jotta se voi analysoida vastauksia skannauksiinsa.




Tarkemmin sanottuna ainakin Linuxissa on mahdollista käyttää Nmapia kaikkine toimintoineen ja optioineen ilman, että olet itse pääkäyttäjä. Tämä saavutetaan antamalla oikeat _kapasiteetit_ binäärille. Tämä vaatii kuitenkin edistynyttä manipulointia eikä välttämättä ole yhtä käytännöllistä kuin Nmapin ajaminen suoraan oikeuksin. Tämä lähestymistapa on myös harvinaisempi ja voi aiheuttaa tietoturvaongelmia, jos se on konfiguroitu väärin.



Tämä poikkeaa kuitenkin hieman Nmap-oppaastamme, joten jätämme sen toistaiseksi pois.



Tämän ohjeen loppuosassa oletetaan, että Nmapia ajetaan aina "pääkäyttäjänä" (komentotulkista "root" tai komennolla "sudo") tai Windowsissa järjestelmänvalvojan päätelaitteessa, vaikka tätä ei olisi ilmoitettu. Muussa tapauksessa saatat kokea hienovaraisia, mutta havaittavia eroja opetusohjelmaan verrattuna.



### V. Päätelmät



Juuri noin! Nmap on nyt asennettu käyttöjärjestelmäämme ja valmis käytettäväksi, eikä se vaadi enää muita asetuksia. Tämä osio päättää Nmapin esittelyn ja esittelyn. Toivottavasti se sai suupielesi veteen ja olet innokas aloittamaan harjoittelun.



Vakavammasta näkökulmasta meillä on nyt parempi käsitys siitä, mikä Nmap-kartoitustyökalu on ja mitkä ovat sen yleisimmät käyttötarkoitukset sekä sen rajoitukset. Mennään eteenpäin!




## 4 - TCP- ja UDP-porttiskannaukset Nmapilla



### I. Esittely



Tässä osiossa opimme suorittamaan ensimmäiset porttiskannaukset Nmap-verkon skannaustyökalun avulla. Näemme, miten sen avulla voidaan koota luettelo isännän TCP- tai UDP-protokollia käyttävistä verkkopalveluista.



Muista tästä lähtien skannata vain valvotussa ympäristössä olevia isäntiä, joihin sinulla on nimenomainen valtuutus.





- Muistutuksena: [Rikoslaki: III luku: Hyökkäykset automaattisia tietojenkäsittelyjärjestelmiä vastaan](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




**Jos sinulla ei ole sellaista käsillä**, suosittelen seuraavia ilmaisia ratkaisuja, jotka ovat juuri sopivia!





- [Hack The Box](https://app.hackthebox.com/ "Hack The Box")**: Hacking-koulutusalusta Hack The Box tarjoaa jatkuvasti haavoittuvia järjestelmiä, joihin voit hyökätä parhaaksi katsomallasi tavalla. Käytettävissä on useita satoja järjestelmiä, mutta uudistettu 20 koneen pooli on tarjolla ilmaiseksi ympäri vuoden, ja siihen pääsee käsiksi OpenVPN VPN:n kautta.





- [Vulnhub](https://www.vulnhub.com/ "Vulnhub")**: Tämä alusta tarjoaa ladattavaksi lukuisia tarkoituksellisesti haavoittuvia järjestelmiä, joita voidaan käyttää VirtualBoxin (myös ilmainen ratkaisu) tai muiden keinojen avulla. Kun se on ladattu, VPN:ää ei tarvita - kaikki on paikallista.




Voit myös vapaasti **luoda virtuaalikoneen** suosikkikäyttöjärjestelmälläsi ja asentaa siihen erilaisia palveluita testikohteiksi. Etuna tässä on se, että voit myös nähdä, mitä palvelinpuolella tapahtuu skannauksen aikana, erityisesti Wiresharkilla, ja voit vaikuttaa paikalliseen palomuuriin, kun teemme edistyneempiä testejä.



Mennäänpäs käytännöllisiksi!



### II. Isännän TCP-porttien skannaaminen Nmapin avulla



#### A. Ensimmäinen TCP-porttiskannaus Nmapilla



Suoritamme nyt ensimmäiset skannaukset Nmapin avulla. Tavoitteenamme on yksinkertainen: haluamme selvittää, mitä palveluja juuri käyttöön ottamamme verkkopalvelin paljastaa, ja nähdäksemme, onko siinä jotain odottamatonta, kuten hallintapalvelu, johon ei pitäisi päästä käsiksi, tai sellaisen sovelluksen portin paljastuminen, jonka luulimme olevan poistettu käytöstä.



Esimerkissäni skannattavalla isännällä on IP Address "192.168.1.18":



```
nmap 192.168.1.18
```



Tässä on mahdollinen tulos. Näemme klassisen Nmap-palautteen, jossa on paljon tietoa:



![nmap-image](assets/fr/11.webp)



nmapilla suoritetun yksinkertaisen TCP-skannauksen tulokset._



Kun tarkastelemme tätä tulosta nopeasti, ymmärrämme, että portit TCP/22 ja TCP/80 ovat käytettävissä tällä isännällä.



Oletusarvoisesti Nmap skannaa vain TCP-portteja, jos et käske sitä tekemään niin.



#### B. Yksinkertaisen Nmap-skannauksen tulosten ymmärtäminen



Mennään kuitenkin askeleen pidemmälle tämän tulosteen ymmärtämiseksi: jokainen rivi on tärkeä, ensinnäkin siksi, että tiedämme, mitä juuri on tehty, ja toiseksi siksi, että voimme tulkita skannaustuloksia oikein.



Ensimmäinen rivi on lähinnä muistutus skannausversiosta ja -päivämäärästä (hyödyllinen kirjaamista ja arkistointia varten!):



```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```



Toisella rivillä näkyy skannaustulosten alku isännän "debian.home (192.168.1.19)" osalta. Tästä tiedosta on hyötyä, kun aloitamme useiden isäntien skannauksen samanaikaisesti:



```
Nmap scan report for debian.home (192.168.1.19)
```



Kolmas rivi kertoo, että kyseinen isäntä on "Up" eli aktiivinen:



```
Host is up (0.00022s latency).
```



Lopuksi Nmap ilmoittaa, että 998 suljettuna tunnistettua TCP-porttia ei näy:



```
Not shown: 998 closed tcp ports (conn-refused)
```



Näin säästämme lähes 1000 riviä tulostetta, joka näyttää seuraavalta:



```
1/tcp closed
2/tcp closed
3/tcp closed
…
```



Kiitos hänelle siitä, että hän on säästänyt meidät tältä!



Miksi 998 "suljettua" porttia? Kun lisätään 2 avointa porttia, saadaan 1000, ja se on porttien määrä, jonka Nmap skannaa oletuskokoonpanossaan, ei 65535 olemassa olevaa TCP-porttia! Näemme myöhemmin, että tämä on täysin ja helposti muokattavissa. Mutta jos kohteena olevalla isännällä on palvelu, joka kuuntelee melko eksoottista porttia, tämä "oletusskannaus" ei paljasta sitä.



Näiden tietojen jälkeen löydämme sen, mikä on kaikkein mielenkiintoisinta: taulukon, joka on järjestetty kolmen sarakkeen "PORT - STATE - SERVICE" mukaan:





- Ensimmäinen "PORT"-sarake osoittaa yksinkertaisesti kohteena olevan portin/protokollan, ja tässä yhteydessä on tärkeää katsoa, onko kyseessä TCP-portti (`<port>/tcp`) vai UDP (`<port>/udp`).





- STATE-sarakkeessa ilmoitetaan tämän portin havaitun verkkopalvelun tila, jonka Nmap on määritellyt saadun vastauksen perusteella. Tämä voi olla "avoin", "suljettu", "suodatettu" tai "tuntematon". Näemme myöhemmin, miten Nmap erottaa nämä eri tilat toisistaan.





- PALVELU-sarakkeessa ilmoitetaan, mikä palvelu on käytössä kyseisessä portissa. Huomaa kuitenkin, että emme ole käyttäneet tässä aktiivisia palveluhakuvaihtoehtoja. Nmap luottaa portin/protokollan ja oletettavasti osoitetun palvelun väliseen paikalliseen viittaukseen: tiedostoon "/etc/services"




Jos katsot Linux-järjestelmän tiedostoa "/etc/services", löydät "port/protocol - service" -linkin, joka on samanlainen kuin Nmapin näyttämä:



![nmap-image](assets/fr/12.webp)



poimii tiedoston "/etc/services" sisällön Linuxissa._



On tärkeää ymmärtää, että Nmap ei ole toistaiseksi suorittanut aktiivista palveluhakua. Se ei olisi esimerkiksi pystynyt tunnistamaan TCP/80-portin takana olevaa SSH-palvelua, jos näin olisi ollut. Siksi on tärkeää osata käyttää oikeita vaihtoehtoja - se on tulossa pian!



Nmapin tulosteiden tulkitseminen on tärkeä osa työkalun hallintaa. Hyvä uutinen on se, että tuloste on pitkälti samanlainen riippumatta siitä, mitä vaihtoehtoja käytät.



#### C. Konepellin alla: verkkoanalyysi Wiresharkilla



Jos katsot tarkkaan, mitä palvelinta tutkivan isännän Interface-verkossa tai palvelimen verkossa tapahtuu, Nmapin toiminta on paljon selkeämpää. Näin aiomme tehdä tässä.



Se, mitä voin näyttää tässä, on vain osa siitä, mitä Wiresharkissa näkyy. Jos haluat mennä pidemmälle, voit vapaasti tehdä verkkokaappauksen itse skannauksen aikana ja selata sitten kaapattuja tietoja.



Tässä testissä skanneri-isäntä (192.168.1.18) ja kohde-isäntä (192.168.1.19) ovat samassa paikallisverkossa.



Nmap aloittaa selvittämällä, onko kohde-isäntä aktiivinen paikallisverkossa lähettämällä ARP-pyynnön. Jos se saa vastauksen, se tietää, että isäntä on aktiivinen, ja aloittaa verkon skannauksen:



![nmap-image](assets/fr/13.webp)



_ARP-pyyntö, jonka Nmap lähettää määrittääkseen, onko kohdeisäntä läsnä paikallisverkossa._



Jos skannattava isäntä on etäverkossa, Nmap aloittaa lähettämällä ping-pyynnön ja yrittää tavoittaa joitakin yleisimmin altistuneita portteja (TCP/80, TCP/443):



![nmap-image](assets/fr/14.webp)



nmapin lähettämä ping-pyyntö, jolla määritetään, onko kohde-isäntä tavoitettavissa etäverkossa



Jos se saa vastauksen johonkin näistä testeistä, se pitää kohdetta aktiivisena.



Kun Nmap on todennut, että kohde on aktiivinen, se yrittää ratkaista sen verkkotunnuksen verkkokorttiin määritetyn DNS-palvelimen avulla:



![nmap-image](assets/fr/15.webp)



dNS-resoluutio Nmapin skannauskohteessa



Nyt kun Nmap on tunnistanut kohteensa ja tietää, että se on aktiivinen, se aloittaa TCP-porttiskannauksen:



![nmap-image](assets/fr/16.webp)



tCP SYN-paketin lähetys ja RST/ACK-vastaanotto Nmap-skannauksen aikana



Tätä varten se lähettää jokaisessa oletusalueen TCP-portissa **TCP SYN-paketteja ja odottaa vastausta**. Yllä olevassa kuvakaappauksessa se vastaanottaa TCP RST/ACK -paketteja skannatulta palvelimelta, mikä tarkoittaa, että "siirry eteenpäin, täällä ei ole mitään nähtävää" - toisin sanoen nämä portit on suljettu. Kuten näimme tuloksesta, näin on useimpien skannattujen porttien kohdalla. Kahta poikkeusta lukuun ottamatta:



![nmap-image](assets/fr/17.webp)



vastaus porttiin 22 lähetettyyn TCP SYN-pakettiin, joka on aktiivinen skannauskohteessa



Yllä olevassa kuvakaappauksessa näkyy kohdeisännän lähettämä TCP SYN/ACK-paketti**. Portti on aktiivinen ja tarjoaa palvelun. Nmap kuittaa vastauksen vastaanottamisen ja katkaisee yhteyden (TCP RST/ACK). **Siten se tiesi, että portti TCP/22 oli aktiivinen**.



Olemme nähneet tässä, että Nmap kunnioittaa "Three Way Handshake" -kättelyä skannatessaan TCP-verkkoa. Suorituskykysyistä on mahdollista pyytää sitä olemaan vastaamatta palvelimen vastaukseen, jolloin säästetään useita tuhansia paketteja, kun skannataan suurta verkkoa. Mutta tarkastelemme näitä vaihtoehtoja ja optimointeja myöhemmin opetusohjelmassa.



Nyt meillä on parempi käsitys siitä, miten TCP-skannaus tehdään ja mitä sen aikana oikeastaan tapahtuu. Olemme myös nähneet, että oletusarvoisesti Nmap suorittaa TCP-porttiskannauksen rajoitetulle määrälle portteja.



### III. UDP-porttien skannaaminen Nmapilla



#### A. Ensimmäinen UDP-porttiskannaus Nmapilla



Katsotaan nyt, miten isännän UDP-portit skannataan. Kuten olemme nähneet, Nmap skannaa oletusarvoisesti aina TCP-portit. Tämä voi tarkoittaa, että jää paljon tietoa saamatta, jos emme ole tietoisia siitä.



Muistutettakoon, että tässä testissä skanneri-isäntäni (192.168.1.18) ja kohde-isäntäni (192.168.1.19) ovat samassa lähiverkossa.



```
nmap -sU 192.168.1.19
```



Tässä tapauksessa saatu palautus on samassa muodossa kuin TCP-skannauksessa, mutta aktiiviset palvelut näytetään `<port>/UDP` -muodossa, kuten pyydetään!



![nmap-image](assets/fr/18.webp)



nmapilla suoritetun yksinkertaisen UDP-skannauksen tulos._



"-sU"-vaihtoehtoa käytetään kertomaan Nmapille, että haluat työskennellä UDP:llä, etkä TCP:llä, kuten oletusarvoisesti.



Muuten, huomaat varmaan, että Nmap vaatii "pääkäyttäjän" oikeudet UDP-skannauksiin, kuten aiemmin oppaassa mainittiin.



huomautus: Nmapin uusimmista versioista lähtien on aina suositeltavaa suorittaa UDP-skannaukset järjestelmänvalvojan oikeuksin luotettavien tulosten varmistamiseksi, koska jotkin ominaisuudet vaativat raakaa pääsyä verkkopistorasioihin._



UDP-skannaukset voivat kestää hyvin kauan (esimerkissäni 1100 sekuntia 1000 portin skannaamiseen), koska UDP:ssä ei ole "Three Way Handshake" -kättelyä, mikä tarkoittaa, että Nmap odottaa palautusta jokaisesta lähetetystä UDP-paketista ja määrittelee portin "suljetuksi" vain, jos palautusta ei tule tietyn ajan kuluttua (aikakatkaisu). Tämä skannattujen isäntien vastaus ei ole systemaattinen, ja usein vastausten määrä sekunnissa on rajoitettu tiettyjen vahvistushyökkäysten välttämiseksi. Toisin kuin TCP:ssä, jossa skannattu isäntä vastaa välittömästi riippumatta siitä, onko portti auki vai kiinni. Näemme myöhemmin, miten tätä voidaan optimoida.



Toinen UDP:n ongelma on se, että **palvelut eivät aina vastaa saapuviin paketteihin**, yksinkertaisesti siksi, että se ei ole aina tarpeen, ja se on UDP:n periaate. Kun näin on, eikä ICMP-ilmoitusta "port unreachable" vastaanoteta, Nmap merkitsee palvelun "open|filtered", kuten yllä olevassa kuvassa näkyy.



#### B. Konepellin alla: verkkoanalyysi Wiresharkilla



Kuten TCP-skannauksen yhteydessä, tarkastellaan tarkemmin, mitä verkkotasolla tapahtuu UDP-skannauksen aikana Wireshark-analyysin avulla. Nmapin käyttäytyminen määritettäessä, onko isäntä aktiivinen, on sama.



Ainoa todellinen ero UDP:tä skannattaessa on se, että Nmap ei odota "Three Way Handshakea", koska tätä mekanismia ei ole olemassa UDP:ssä (tilaton protokolla):



![nmap-image](assets/fr/19.webp)



uDP-pakettien lähetys ja ICMP-vastaanotto (portti ei tavoitettavissa) Nmap-skannauksen aikana



Yllä olevasta kuvakaappauksesta näemme, että Nmap lähettää suuren määrän UDP-paketteja ja vastaanottaa suurimmalle osalle niistä ICMP-paketin "Destination unreachable (Port unreachable)". Tämä on normaalia, sillä se on [RFC 1122] (https://www.freesoft.org/CIE/RFC/1122/41.htm "RFC 1122") määrittelemä asianmukainen vastaus, kun UDP-portti on saavuttamaton:



![nmap-image](assets/fr/20.webp)



ote RFC 1122._



Katsotaanpa tarkemmin tätä Wireshark-kaappausta, joka näyttää **kolme mahdollista skenaariota** UDP:ssä:



![nmap-image](assets/fr/21.webp)



verkkokaappaus UDP-skannauksen aikana eri porteissa Nmapilla._



Nämä kolme tapausta ovat seuraavat:





- Ensimmäinen Exchange koostuu paketeista nro. 3, 4 ja 8, 9. Nmap lähettää UDP-paketteja klassiseen SNMP-porttiin ja siksi **rakentaa protokollan mukaiset paketit etukäteen**. Sen jälkeen se saa palvelimelta vastauksen (paketit 8 ja 9). Tulos: Nmap on saanut vastauksen, palvelu on "auki".





- Toinen Exchange koostuu paketeista 6 ja 7. Nmap lähettää "tyhjän" UDP-paketin (jossa ei ole protokollarakennetta) porttiin UDP/165 ja saa vastauksena ICMP-paketin: "Destination unreachable (Port unreachable)". Tulos: Nmap on saanut (negatiivisen) vastauksen, isäntä on toiminnassa, mutta palvelu, jota se yritti tavoittaa, ei toimi tässä portissa, joka merkitään "suljetuksi".





- Viimeinen Exchange koostuu paketista nro 12: Nmap lähettää "tyhjän" UDP-paketin porttiin UDP/1235. Skannattu isäntä ei vastaa, eikä edes kieltäydy nimenomaisesti. Tulos: Nmap merkitsee portin "avoimeksi|suodatetuksi", koska se ei pysty päättelemään, johtuuko tämä palomuurista, joka on konfiguroitu vastaamattomaksi, vai aktiivisesta UDP-palvelusta, joka ei kuitenkaan palauta vastausta (UDP:ssä ei ole pakollista).




Tässä on Nmapin näyttämä tulos näiden kolmen tapauksen jälkeen:



![nmap-image](assets/fr/22.webp)



nmapin kautta suoritetun UDP-skannauksen mahdolliset tulokset._



Nyt meillä on parempi käsitys siitä, miten UDP-skannaus tehdään ja mitä sen aikana oikeastaan tapahtuu. Tähän asti olemme käyttäneet Nmapia hyvin yksinkertaisella tavalla päättämättä, mitkä portit skannataan, mutta tämä muuttuu pian!



### IV. Porttiskannauksen hienosäätö Nmapilla



#### A. Muistutus Nmapin oletuskäyttäytymisestä



Kuten olemme nähneet, Nmap valitsee itse skannattavien porttien määrän ja portit, jos et määritä mitään vaihtoehtoja. Tämä on Nmapin käyttämä "oletusasetus", kun et kerro sille tarkalleen, mitä tehdä. Näiden oletusasetusten tarkoituksena on antaa käsitys tärkeimmistä altistuneista porteista, jotka valitaan altistumisen tiheyden mukaan (yleisimmät tai yleisimmät portit) eikä numerojärjestyksessä (portti 1, 2, 3 jne.), ja myös välttää 65535 mahdollisen portin skannauksen aloittaminen, jos et määritä sopivia asetuksia, jotka olisivat liian pitkiä ja sanoja "oletusarvoiseen" käyttötilanteeseen.



**Miten nämä portit valitaan?



Oletustilassa skannatut 1000 porttia valitaan niiden esiintymistiheyden mukaan. Nmap ylläpitää näitä tilastoja ja päivittää niitä samalla tavalla kuin itse binääritietokonetta ja sen skriptejä (moduuleja). Voit itse tarkastella näitä tilastoja tiedostosta "/usr/shares/nmap/nmap-services":



![nmap-image](assets/fr/23.webp)



purettu tiedostosta "/usr/shares/nmap/nmap-services"._



Kolmannessa sarakkeessa on todennäköisyyksiä (0:n ja 1:n välillä) tai prosentuaalisia jakaumia. Tämä on kunkin portti/protokolla-parin esiintymistiheys. Näemme, että tunnetuimmilla porteilla (tässä otoksessa FTP, SSH, TELNET ja SMTP) on paljon suurempi arvo kuin muilla.



#### B. Määritä tarkasti Nmap-skannauksen kohdeportit



Todellisessa maailmassa meidän on kuitenkin ehkä skannattava vain tietty portti, useita portteja tai tietty porttialue. Nmapin avulla on helppo tehdä juuri tämä, ja se on yhdenmukainen sekä UDP- että TCP-skannausten osalta.



**Skannaa tietty portti Nmapin kautta**



Jos haluamme skannata vain yhden portin, emmekä 1000 porttia, voimme määrittää tämän portin Nmapin "-p"- tai "--port"-vaihtoehdolla:



```
# Scan a single TCP port with Nmap
nmap 192.168.1.19 -p 80

# Scan a single UDP port with Nmap
nmap -sU 192.168.1.19 -p 161
```



Tämän seurauksena skannaus on luonnollisesti paljon nopeampi, ja Nmap lähettää vain paketteja, joita tarvitaan sen havaitsemiseen, onko isäntä aktiivinen, ja sen jälkeen, onko määritetty portti tavoitettavissa. Tämä säästää aikaa, jos haluat vain suorittaa nopean testin ja tarkistaa, onko esittelysivustosi verkkopalvelu yhä toiminnassa.



**Tarkista useita portteja Nmapin kautta**



Samalla tavalla voimme määrittää Nmapille useita portteja käyttämällä samaa vaihtoehtoa ja yhdistämällä määritetyt portit pilkulla:



```

# Scan several TCP ports with Nmap

nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan several UDP ports with Nmap

nmap -sU 192.168.1.19 -p 161,23,69

```



Järjestyksestä riippumatta Nmap tarkistaa kaikki nämä portit ja vain ne, jotka ovat kohteena olevassa isännässä. Huomaat Nmapin tulosteessa, että se **selkeästi kertoo kaikki portit ja niiden tilan**, vaikka ne olisivatkin "suljettuja". Toisin kuin oletuskäyttäytymisessä, jossa tämä täydellinen tuloste olisi vienyt aivan liikaa tilaa:



![nmap-image](assets/fr/24.webp)



*Nmapin TCP-skannauksen tulos ilmoitetuissa porteissa.*



**Tarkista useita portteja



Jos skannattavien porttien määrä on liian suuri, voit määritellä ne alueittain, esimerkiksi:



```

# Scan TCP ports from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 1000-2000

# Scan UDP ports from 1000 to 2000 with Nmap

nmap -sU 192.168.1.19 -p 100-150

```



Voit tietysti yhdistellä ja yhdistellä esimerkiksi haluamallasi tavalla:



```

# Scan TCP ports 22,80, 3389 and from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 22,80,1000-2000,3389

```



**TCP- ja UDP-porttien skannaus



Voit myös suorittaa UDP- ja TCP-skannauksia samanaikaisesti valituille porteille:



```

# Scan the list of 1000 default ports, in TCP and UDP

sudo nmap 192.168.1.19 -sT -sU

# Scan only UDP/161 and TCP/22

sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```



Huomaat, että tässä viimeisessä esimerkissä UDP-portin merkkinä on "U:" ja TCP-portin merkkinä "T:". Tässä on tämäntyyppisen skannauksen mahdollinen tulos:



![nmap-image](assets/fr/25.webp)



*TCP- ja UDP-porttien skannauksen tulos Nmap.*:lla



Siinäpä mielenkiintoinen tapa muokata skannauksia!



**Tarkista kaikki portit



Lopuksi, Nmapille on mahdollista määrittää paljon suurempia tai pienempiä alueita. Olemme nähneet, että Nmapin valitsema oletusluettelo sisältää 1000 porttia. Voimme myös pyytää 100 yleisintä porttia tai 200 yleisintä porttia käyttämällä "--top-ports"-vaihtoehtoa:



```

# Scan the top 100 most common ports with Nmap

nmap 192.168.1.19 --top-ports 100

# Scan the top 200 most common ports with Nmap

nmap 192.168.1.19 --top-ports 200

```



Lopuksi voimme pyytää sitä skannaamaan kaikki mahdolliset portit (kaikki 65535) käyttämällä merkintää "-p-":



```

# Scan all TCP ports from 1 to 65535 with Nmap

nmap 192.168.1.19 -p-

```



Jälkimmäinen kestää kauemmin, erityisesti UDP:n kanssa, mutta et varmasti jätä yhtään avointa porttia käyttämättä.



*Huomautus: "-p-"-vaihtoehto on suositeltava menetelmä kaikkien TCP-porttien skannaamiseen. UDP-skannauksissa on suositeltavaa rajoittaa porttien määrää suorituskykysyistä, koska kaikkien UDP-porttien täydellinen skannaus voi kestää hyvin kauan.*



Myöhemmin tässä oppaassa katsotaan, miten Nmapin skannausnopeutta voidaan optimoida tarpeisiimme sopivaksi, mikä on erityisen hyödyllistä kaikkien TCP- ja UDP-porttien skannauksissa.



### V. Päätelmät



Tässä osiossa saimme vihdoin käytännön harjoitusta, joten nyt tiedämme **miten Nmapia käytetään perusmenetelmällä isännän TCP- ja UDP-porttien skannaamiseen**. Olemme myös tarkastelleet yksityiskohtaisesti, mitä verkkotasolla tapahtuu ja **miten Nmap määrittää, onko TCP- tai UDP-portti aktiivinen vai ei**. Lopuksi tiedämme, miten voimme valita hienovaraisesti portit, jotka haluamme skannata, ja **miten Nmapin oletusasetukset itse asiassa toimivat**. Seuraavaksi käytämme tätä tietoa uudelleen ja sovellamme sitä koko verkon skannaukseen, mukaan lukien globaalikartoitus ja verkon löytäminen.




## 5 - Verkon kartoitus ja löytäminen Nmapin avulla



### I. Esittely



Tässä osiossa opimme, miten Nmap-verkkoskannaustyökalulla kartoitetaan verkkoa. Näemme, kuinka tehokas se voi olla tässä tehtävässä sen eri vaihtoehtojen avulla. Lopuksi tarkastelemme eri tapoja määrittää skannauksen kohteet Nmapille.



Käytämme erityisesti sitä, mitä opimme edellisessä osassa siitä, miten Nmap määrittää, onko isäntä aktiivinen ja tavoitettavissa.



Kuten Nmapin esittelyssä mainittiin, kyseessä on verkkokartoittaja. Sellaisena se on täydellinen työkalu luettelon laatimiseen verkon käytettävissä olevista isännistä, olivatpa ne sitten paikallisia tai etäverkon isäntiä.



**Tekijän paluu:**



Itse asiassa kyberturvallisuuden tarkastajana ja viisiportaisena testaajana käytän Nmapia järjestelmällisesti sisäisten tunkeutumistestien yhteydessä saadakseni selville, missä olen, ketkä ovat naapureitani lähiverkossa ja mihin muihin verkkoihin pääsee, samoin kuin niissä oleviin järjestelmiin. Tavoitteeni on yksinkertainen: kartoittaa verkko, määrittää tietojärjestelmän koko ja erityisesti hahmotella sen hyökkäyspinta.



Verkkokartoituksesta voi olla hyötyä myös verkon diagnostiikassa, valvonnassa ja omaisuuserien kartoituksessa (oletko todella varma, että tietoverkkosi koostuu ainoastaan Active Directoryyn tai GLPI/OCS-luetteloon sisältyvistä tiedoista?)? Sitä voidaan käyttää myös havaitsemaan varjo-IT:n esiintyminen tietojärjestelmissäsi.



### II. Nmapin käyttäminen verkkoalueen skannaamiseen



#### A. Verkon löytäminen Nmap-skannauksella



Haluaisimme nyt vaihtaa vaihteen ylemmäs ja analysoida koko lähiverkkomme. Mikään ei voisi olla yksinkertaisempaa: meidän tarvitsee vain käyttää edellisessä jaksossa nähtyjä komentoja, mutta määritellä CIDR yksinkertaisen IP Address:n sijasta.



CIDR (**Classless Inter Domain Routing**) on "klassinen" merkintätapa verkkoalueen ja sen laajuuden määrittämiseksi (maskin avulla). Esimerkiksi "192.168.0.0/24" on "käännös" desimaalimaskin merkinnästä "255.255.255.255.0".



Jos haluat käyttää Nmapia määrittämällä CIDR:n, voimme käyttää sitä seuraavasti:



```
# Scan a CIDR
nmap 192.168.0.0/24
```



On myös mahdollista määrittää useita isäntiä, useita verkkoja tai alueita, kuten edellisessä kohdassa porttien kohdalla:



```
# Scan several networks at once via their CIDR
nmap 192.168.0.0/24 192.168.1.0/24

# Scan several hosts via their IP
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Mix of both
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```



Tässä on esimerkki tuloksista, joita saatamme saada, kun suoritamme verkon tarkistuksen:



![nmap-image](assets/fr/26.webp)



nmap-skannauksen tulokset useiden verkkojen kartoittamiseksi



Näemme erityisesti useita aktiivisia isäntiä, ja jokainen isäntäosa alkaa seuraavanlaisella rivillä:



```
Nmap scan report for <name> (<IP>)
```



Näin voimme selvästi nähdä, mihin isäntään seuraavat tulokset viittaavat. Viimeinen rivi on myös tärkeä:



```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```



Tiedämme, että Nmap löysi skannatuista verkoista 5 aktiivista isäntäkohtaa.



#### B. Konepellin alla: verkkoanalyysi Wiresharkilla



Seuraavaksi tarkastelemme tarkemmin, mitä verkkotasolla tapahtuu Nmapin avulla suoritettavan verkkotiedustelun aikana.



Kuten edellisessä kappaleessa todettiin, Nmap käyttää oletusarvoisesti ARP-protokollaa havaitakseen isäntien läsnäolon paikallisverkossa:



![nmap-image](assets/fr/27.webp)



aRP-paketit, jotka on kaapattu skannattaessa lähiverkkoa Nmapin ja sen oletusasetusten avulla



Näin se pystyy havaitsemaan käytännössä kaikki lähiverkon isännät, koska ARP-pyyntöön antavat yleensä vastauksen kaikki verkossa toimivat isännät, eivätkä ne näytä millään tavoin epäilyttäviltä.



Etäverkoissa Nmap käyttää tekniikoiden yhdistelmää:



![nmap-image](assets/fr/28.webp)



iCMP- ja TCP-paketit, jotka kaapataan skannattaessa etäverkkoa Nmapin ja sen oletusasetusten avulla



Tarkemmin sanottuna Nmap käyttää ICMP-echo-pakettia (klassinen pingaustapaus) ja ICMP Timestamp -pakettia, jota käytetään yleensä pakettien siirtoaikojen laskemiseen. Se toivoo saavansa vastauksen etäverkoissa olevilta isänniltä.



Mutta siinä on muutakin. Yllä olevasta Wireshark-kaappauksesta näkyy, että **TCP SYN** -paketteja lähetetään järjestelmällisesti TCP/443-portteihin jokaiselle potentiaaliselle isännälle skannattavissa verkoissa, samoin kuin **TCP ACK** -paketteja TCP/80-porttiin.



**Miksi lähettää TCP-paketteja portteihin osana verkon löytämistä?



Lähettämällä SYN-paketin tiettyyn porttiin Nmap voi **määrittää, kuunteleeko palvelu kyseistä porttia**. Jos isäntä vastaa SYN-pakettiin SYN/ACK-paketilla, tämä osoittaa, että se on aktiivinen ja että palvelu kuuntelee kyseistä porttia. Nmap yrittää siis onneaan kyseisessä palvelussa, **vaikka ping-vastausta ei olisikaan saatu**.



ACK-paketin lähettäminen tiettyyn porttiin antaa Nmapille mahdollisuuden **määrittää, onko kyseisellä isännällä palomuuri**. Jos isäntä vastaa ACK-pakettiin RST-paketilla (Reset), tämä osoittaa, että kyseisessä isännässä on todennäköisesti palomuuri, joka estää ei-toivotun liikenteen. Näin isäntä paljastaa läsnäolonsa verkossa, vaikka se ei olisikaan vastannut muihin pyyntöihin.



On kuitenkin tärkeää huomata, että palomuurin havaitseminen tällä tekniikalla ei välttämättä ole täysin luotettavaa kaikissa tapauksissa. Jotkin isännät voivat saada generate RST-vastauksia muista syistä kuin palomuurin olemassaolosta, kuten tietyn palvelun tai käyttöjärjestelmän kokoonpanon vuoksi. Lisäksi nykyaikaiset palomuurit voidaan konfiguroida niin, että ne eivät vastaa tämäntyyppisiin havaitsemisyrityksiin.



Olemme nyt päässeet pitkälle ja pystymme suorittamaan verkon perustutkimuksen. Tarkastelemme nyt muutamia muita vaihtoehtoja, jotka antavat meille paremman kontrollin Nmapin käyttäytymiseen.



### III. Verkon löytäminen ilman porttiskannausta Nmapin avulla



Kuten olet ehkä huomannut, oletusarvoisesti Nmap **suorittaa porttiskannauksen aktiivisen isännän löytämisen jälkeen**, mikä lisää valtavan määrän paketteja ja vastausten odottelua skannaukseen. Jos verkossasi on 5 isäntää, Nmap yrittää tarkistaa noin 5 000 portin tilan, mikä kestää kauemmin.



On kuitenkin mahdollista käyttää Nmapin asetuksia, joilla voidaan etsiä **vain verkossa olevat aktiiviset isännät**, mutta ei niiden palveluita.



Jos haluamme vain tietää, mitkä isännät ovat tavoitettavissa, mutta emme saa tietoa niiden tarjoamista palveluista ja porteista, voimme käyttää "-sn"-vaihtoehtoa suorittaaksemme **vain skannauksen ICMP Echo (ping) ja ARP-pyyntöjen avulla**. Toisin sanoen porttiskannaus voidaan poistaa kokonaan käytöstä:



```
# Scan a CIDR in Echo ICMP
nmap 192.168.1.0/24 -sn
```



Tässä on Nmap-verkkotutkimuksen tulos, joka on tehty ilman porttiskannausta:



![nmap-image](assets/fr/29.webp)



Verkon löytämisen tulos ilman porttiskannausta Nmapilla.



Olemme jo maininneet mahdolliset rajoitukset, jotka liittyvät pelkän ICMP:n käyttämiseen isännän löytämiseen (etäverkoissa). Siksi Nmap käyttää myös muutamia temppuja, jotka voivat paljastaa palomuurin tai tietyn palvelun läsnäolon isännissä. Asetusten avulla voimme käyttää näitä temppuja uudelleen ja jopa laajentaa niitä ilman, että meidän tarvitsee aloittaa uudelleen jokaisen löydetyn isännän täydellinen porttiskannaus.



Tätä varten käytämme vaihtoehtoja "-PS" (TCP SYN) ja "-PA" (TCP ACK), joiden avulla voimme määrittää portit, joihin haluamme liittyä osana isännän löytämistä, sekä "-PP"-vaihtoehtoa:



```
# Scan specific ports on a CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```



Tämä tarkistus varmistaa jo nyt, että isännän löytäminen on hieman täydellisempää kuin oletusasetuksilla.



Alamme saada melko kattavia komentoja, joissa käytetään useita vaihtoehtoja. Tämä johtuu siitä, että tiedämme, miten Nmap toimii ja sen "oletusasetusten" rajoitukset, jotka voivat joskus aiheuttaa ajan tuhlausta tai tärkeiden Elements:n ohittamista. Se on koko sen tarkoitus, että otamme aikaa sen hallitsemiseen!



Viimeisimmän tilauksemme vaihtoehdot yksityiskohtaisesti:





- "`-sn`: poistaa porttiskannauksen käytöstä jokaisen Nmapin löytämän aktiivisen isännän osalta.





- "`-PP`: mahdollistaa ICMP-kaiku (ping-skannaus) isännän löytämiseksi.





- "`-PS <PORT>`": lähetä TCP SYN-paketti ilmoitettuun porttiin (ilmoitettuihin portteihin) havaitakseen aktiivisen palvelun, joka paljastaa isännän, joka ei ole vastannut pingiin.





- "`-PA <PORT>`": lähetä TCP ACK-paketti ilmoitettuun porttiin (ilmoitettuihin portteihin) havaitaksesi aktiivisen palomuurin, joka paljastaa isännän, joka ei ole vastannut pingiin.




Yllä olevassa esimerkissä määrittelen "-PS"-vaihtoehtoa varten portit, joita pidän yleisimmin alttiina Nmap-konteksteissani. Näitä eri portteja testataan sitten jokaisella isännällä, ei sen selvittämiseksi, onko niiden isännöimä palvelu todella aktiivinen, vaan sen selvittämiseksi, voimmeko näin löytää isännän, joka ei ole vastannut ICMP-Echoon, vaikka se on edelleen aktiivinen (palvelun tai isännän palomuurin vastauksen kautta).



Seuraavassa on, mitä voidaan nähdä verkkokaappauksessa, joka on otettu tällaisen skannauksen aikana, tässä tapauksessa yksittäisen kohdeisännän otteessa:



![nmap-image](assets/fr/30.webp)



nmapin lähettämät paketit edistyneen verkon etsinnän aikana ilman porttiskannausta



Löydämme TCP SYN -pakettimme, TCP ACK -pakettimme portissa TCP/80 ja ICMP-kaiku. Nmap suorittaa kaikki nämä testit jokaiselle isännälle, johon verkkotutkimuksemme kohdistuu.



### IV. Nmapin kohteena olevan omaisuuserätiedoston käyttö



Kohteiden määrittäminen voi osoittautua nopeasti monimutkaiseksi todellisissa tietojärjestelmissä, jotka voivat joskus koostua kymmenistä tai sadoista verkoista, aliverkoista ja VLANeista. Siksi on helpompaa käyttää tiedostoa Nmapin lähteenä kuin määrittää ne yksi kerrallaan komentorivillä.



Luo aluksi yksinkertainen tiedosto, joka sisältää yhden merkinnän riviä kohti:



![nmap-image](assets/fr/31.webp)



tiedosto, joka sisältää yhden kohteen (isäntä tai verkko) per rivi



Seuraavaksi voimme käyttää kaikkia tähän mennessä nähtyjä Nmapin vaihtoehtoja ja määrittää vaihtoehdon "-iL <polku/tiedosto>":



```
# Scan a list of targets contained in a file
nmap -iL /tmp/mesCibles.txt
```



Tämän jälkeen Nmap sisällyttää skannaukseensa kaikki tiedostomme sisältämät kohteet.



Jos haluat olla varma, että kaikki kohteet otetaan huomioon, voit käyttää vaihtoehtoa "-sL -n". Nmap tulkitsee tällöin vain tiedostossa olevat CIDR:t ja isännät ja näyttää ne sinulle lähettämättä mitään paketteja verkon yli:



```
# Display targets contained in a file
nmap -iL /tmp/mesCibles.txt -sL -n

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-01 14:52 CEST
Nmap scan report for 192.168.0.0
Nmap scan report for 192.168.0.1
Nmap scan report for 192.168.0.2
Nmap scan report for 192.168.0.3
Nmap scan report for 192.168.0.4
Nmap scan report for 192.168.0.5
Nmap scan report for 192.168.0.6
Nmap scan report for 192.168.0.7
Nmap scan report for 192.168.0.8
Nmap scan report for 192.168.0.9
Nmap scan report for 192.168.0.10
Nmap scan report for 192.168.0.11
Nmap scan report for 192.168.0.12
```



Näin varmistetaan, että skannattavien isäntien luettelo on tarkka.



Viimeinen tärkeä vinkki, jonka haluan jakaa kanssasi, koskee **isännän tai verkon poissulkemista osana skannausta**. Tämä isännän poissulkeminen voi olla tarpeen useissa tapauksissa, erityisesti jos haluamme olla varmoja siitä, että **tietojärjestelmän arkaluonteinen osa ei häiriinny tai häiriinny skannauksestamme**.



Usein tällaisia tarpeita on esimerkiksi silloin, kun yritys omistaa teollisuus- (PLC) tai terveydenhuollon laitteita. Tällaiset laitteet ovat joskus huonosti suunniteltuja, eikä niitä ole lainkaan tarkoitettu vastaanottamaan huonosti muotoiltuja paketteja tai liikaa paketteja. Ilmeisistä saatavuuteen tai liiketoimintaan/henkilöstöön liittyviin riskeihin liittyvistä syistä ne on parempi jättää testauksen ulkopuolelle.



Jos haluamme sulkea IP-osoitteet tai verkot skannauksen ulkopuolelle, voimme käyttää Nmapin "--exclude"-vaihtoehtoa, esimerkiksi:



```
# Exclude an IP address in a CIDR scan
nmap 192.168.1.0/24 --exclude 192.168.1.140
```



Tässä esimerkissä skannaan verkon "192.168.1.0/24", mutta jätän pois siellä sijaitsevan isännän "192.168.1.140". Nmap ei lähetä paketteja tälle isännälle. Toinen esimerkki aliverkon poissulkemisesta:



```
# Exclude a subnet in a CIDR scan
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```



Samoin skannaan suuren verkon "10.0.0.0/16", mutta verkkoa "10.0.100.0/24" ei skannata. Suosittelen jälleen kerran käyttämään "-sL -n"-vaihtoehtoa saadaksesi hyvin selkeän kuvan siitä, mitkä isännät skannataan ja mitkä jätetään skannauksen ulkopuolelle, varsinkin jos toimit arkaluonteisessa ympäristössä.



### V. Verkon löytäminen ja porttiskannaus



Voimme nyt yhdistää tässä jaksossa oppimamme siihen, mitä opimme edellisessä jaksossa porttiskannausvaihtoehdoista. Oletusarvoisesti olemme nähneet, että Nmap skannaa 1000 yleisintä porttia jokaisesta aktiivisesta isännästä, jonka se havaitsee. Olemme nähneet, miten voimme estää tämän käyttäytymisen, jos emme halua sitä, mutta voimme hallita sitä täysin ja jopa laajentaa sitä, jos se sopii tarpeisiimme.



Esimerkiksi seuraava komento tarkistaa, onko jokaisessa skannatussa isännässä portissa TCP/22 kuunteleva palvelu:



```
# Scan TCP/22 on a CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```



Nmap tekee ensin verkonhaun listatakseen aktiiviset isännät ja tarkistaa jokaisen isännän osalta, että portissa TCP/22 on palvelu.



Samalla tavalla voimme suorittaa kaikkien TCP-porttien täydellisen skannauksen jokaisessa "192.168.0.0.0/24"-verkossa havaitussa isännässä, lukuun ottamatta esimerkiksi isäntää "192.168.0.4":



```
# Port scan of a CIDR with exclusion
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```



Voit vapaasti yhdistellä kaikkia tähän mennessä opittuja vaihtoehtoja omien tarpeidesi mukaan.



### VI. Päätelmät



Tässä osiossa olemme nähneet, miten Nmapin avulla voidaan kartoittaa verkko eri vaihtoehtojen avulla. Meillä on nyt hienosäädetty käsitys skannauksiemme kohteista sekä Nmapin porttiskannauskäyttäytymisestä ja isäntäkohteiden löytämismenetelmästä. Ja mikä tärkeintä, tiedämme, mitkä ovat Nmapin oletuskäyttäytyminen ja rajoitukset ja miten sen tärkeimpien vaihtoehtojen avulla päästään pidemmälle.



Seuraavassa osiossa tarkastelemme mekanismeja ja vaihtoehtoja Nmapin skannaamien palveluiden ja käyttöjärjestelmien versioiden selvittämiseksi.




## 6 - Palvelu- ja käyttöjärjestelmäversioiden tunnistaminen Nmapin avulla



### I. Esittely



Tässä osiossa opimme, miten Nmapin avulla voidaan löytää ja havaita tarkasti skannattujen isäntien käyttämien palveluiden ja käyttöjärjestelmien versiot. Tarkastelemme yksityiskohtaisesti, miten Nmap suorittaa tämän tehtävän, sekä työkalun rajoituksia, jotta voimme ymmärtää ja tulkita sen tuloksia paremmin.



Kuten olemme nähneet tämän ohjeen aiemmissa osioissa, Nmap ei oletusarvoisesti katso, mikä palvelu on alttiina portille, jonka se skannaa ja katsoo avoimeksi. Jos siis kuuntelet verkkopalvelua portissa TCP/22, Nmap ilmoittaa sen edelleen avoimeksi, mutta "SSH"-palveluna. Tämä johtuu siitä, että se käyttää järjestelmässäsi paikallista [tietokanta]a (https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) etsiessään portin/protokollan ja palvelun nimen välistä yhteyttä (tiedosto `/etc/services/`).



Useimmissa tapauksissa [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) antaa sinulle oikeat tiedot, sillä tuotantoympäristössä tällaisia tapauksia esiintyy harvoin. Loput tapaukset ovat kuitenkin tilanteita, joissa klassinen palvelu ([SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), HTTP jne.) on altistettu muulle kuin klassiselle portille (esim. 2022 SSH-palvelulle), jolloin Nmap ei löydä vastaavuutta paikallisesta tietokannastaan tai se ei vastaa todellisuutta, ja menetät tärkeää tietoa.



Onneksi Nmap tarjoaa erittäin tarkkoja vaihtoehtoja ja mekanismeja, joiden avulla voit selvittää, mikä palvelu on piilossa avoimen portin takana. Sillä on jopa tietokanta kyselyistä ja allekirjoituksista, joiden avulla voidaan tunnistaa tarkat teknologiat ja versiot. Palveluiden lisäksi Nmap voi tunnistaa myös käytetyn teknologian ja sen version.



Sitä tarkastelemme tässä jaksossa.



### II. Miten teknologia tai versio havaitaan



#### A. Muistutus siitä, miten teknologia tai versio tunnistetaan



Teknologian ja version tunnistaminen edellyttää palvelun, CMS:n, sovelluksen tai ohjelmiston nimen hakemista, joka kuuntelee kohdeporttia. Esimerkiksi verkkosivua hallinnoi CMS (`WordPress`), sitä käyttää verkkopalvelu (`Apache`, IIS, Nginx) ja sitä isännöi palvelin (Linux tai Windows). Mutta mistä tiedät, mikä verkkopalvelu on käynnissä?



Klassinen menetelmä näiden tietojen selvittämiseksi on _bannerin nappaaminen_, jossa yksinkertaisesti etsitään, missä kyseinen palvelu näyttää nämä tiedot, ja luetaan tiedot. Hyvin usein palvelut näyttävät oletuskonfiguraationsa tai -käsittelynsä perusteella nimensä ja jopa versionsa ensimmäisenä vastauksena yhteyden muodostamisen jälkeen.



![nmap-image](assets/fr/32.webp)



näyttää version heti, kun FTP-palvelu muodostaa TCP-yhteyden



Tässä nähdään, että yksinkertainen TCP-yhteys tähän palveluun `telnetin` kautta tuottaa TCP-paketin, joka sisältää sen teknologian ja version.



Kun olet saanut käsityksen siitä, minkä tyyppisen palvelun kanssa olet tekemisissä, voit myös lähettää kyseiselle palvelulle erityisiä komentoja tai pyyntöjä saadaksesi siitä tietoja. Näitä pyyntöjä/käskyjä voidaan lähettää myös sokeasti (varmistamatta, että kyseessä on oikeantyyppinen palvelu) siinä toivossa, että jokin niistä saa aikaan vastauksen kyseiseltä palvelulta.



Muissa, edistyneemmissä tapauksissa on tarpeen lähettää tiettyjä paketteja, jotta saadaan aikaan reaktio, kuten virhe, joka antaa yksityiskohtaista tietoa käytetystä versiosta tai tekniikasta.



Kuten voit kuvitella, Nmap käyttää kaikkia näitä tekniikoita yrittäessään tunnistaa portissa isännöidyn palvelun tarkan tyypin sekä sen teknologian nimen ja version.



#### B. Nmapin koettimien ja vastaavuuksien ymmärtäminen



Suorittaakseen kaikki nämä tarkistukset jokaiselle skannatulle portille Nmap käyttää paikallista tietokantaa, jota päivitetään usein (aivan kuten binääritiedostoa tai sen moduuleja). Kyseessä on useita tuhansia rivejä käsittävä tekstitiedosto: `/usr/share/nmap/nmap/nmap-service-probes`.



Tämä tiedosto koostuu lukuisista merkinnöistä, jotka kaikki on järjestetty kahden pääsuuntaviivan ympärille:





- `Probe`: tämä on sen paketin määritelmä, jonka Nmap lähettää yrittäessään saada aikaan reaktion tunnistettavasta palvelusta. Ajattele sitä sokeana yrityksenä, kuten _Hello? Guten Tag? Hello? Um... Buenos Dias ehkä?_. Heti kun kohteena oleva palvelu vastaanottaa koettimen, jonka se ymmärtää (eli puhuu oikeaa protokollaa), se vastaa Nmapille, joka saa näin vahvistuksen siitä, minkä tyyppisestä palvelusta on kyse.





- Match": Nämä ovat säännöllisiä lausekkeita, joita Nmap soveltaa saatuun vastaukseen. Jos HTTP GET -pyynnön lähettäminen on saanut palvelulta vastauksen, se soveltaa kymmeniä säännöllisiä lausekkeita tähän vastaukseen tunnistaakseen esimerkiksi sanan `Apache`, `Nginx`, `Microsoft IIS` jne. esiintymisen.




On olemassa muutama muukin ohje erityistapauksia varten, mutta tärkeimmät Nmapin toiminnan ymmärtämisen ja sen käytön mukauttamisen kannalta ovat nämä. Jotta tämä teoriaosuus olisi konkreettisempi, tässä on esimerkki:



![nmap-image](assets/fr/33.webp)



esimerkki koettimesta Nmapin `/usr/share/nmap/nmap-service-probes`-tiedostossa



Tämän esimerkin ensimmäisellä rivillä on helppotajuinen Probe nimeltä `GetRequest`. Kyseessä on TCP-paketti, joka sisältää tyhjän HTTP GET -pyynnön verkkopalvelun juurelle HTTP/1.0:aa käyttäen, jota seuraa rivinvaihto ja tyhjä rivi.



Rivillä `ports` kerrotaan Nmapille, mihin porttiin koetin lähetetään. Näin voit priorisoida testit ja säästää aikaa.



Lopuksi meillä on kaksi esimerkkiä `match`-ohjelmasta. Ensimmäinen esimerkiksi luokittelee skannatun verkkopalvelun `ajp13`:ksi, jos tämän rivin sisältämä säännöllinen lauseke vastaa vastaanotettua palveluvastausta.



Jotta ymmärtäisit paremmin, miltä koettimet voivat näyttää, tässä on luettelo joistakin koettimista, joita löydät tästä tiedostosta (tätä ohjetta kirjoitettaessa niitä oli yhteensä 188).



![nmap-image](assets/fr/34.webp)



esimerkki useista Nmapin käyttämistä koettimista, jotka ovat tiedostossa `/usr/share/nmap/nmap/nmap-service-probes`._



Kaksi ensimmäistä (nimeltään `NULL` ja `GenericLines`) ovat erityisen kiinnostavia, koska ne yksinkertaisesti lähettävät tyhjän TCP-paketin tai sellaisen, joka sisältää rivinvaihdon. Palvelinpalvelut ilmoittavat usein itsestään heti, kun yhteys vastaanotetaan, ilman mitään erityistä toimenpidettä, komentoa tai pyyntöä asiakkaalta.



Seuraavassa on hieman monimutkaisempi _match_:



```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```



Tarkka säännöllinen lauseke on tässä `m|` ja `|` välissä, mikä rajoittaa kaikki säännölliset lausekkeet tässä tiedostossa. Käytä aikaa tämän esimerkin lukemiseen kokonaisuudessaan. Huomaat säännönmukaisessa lausekkeessa valinnan: `([\d.]+)`, jota käytetään version erottamiseen. Tässä esimerkissä määritellään myös muita Elements:ta, kuten tuotteen nimi `p/nginx/`, haettu versio `v/$1/` ja CPE, jonka versio on `cpe:/a:igor_sysoev:nginx:$1/`.



CPE (Common Platform Enumeration) on standardoitu merkintäjärjestelmä, jota käytetään ohjelmistojen ja laitteistojen tunnistamiseen ja kuvaamiseen. Tämä muoto mahdollistaa haavoittuvuuksien ja turvamääritysten tehokkaamman hallinnan ja ennen kaikkea yhtenäisen tavan esittää ne, olipa kyseessä mikä tahansa tuote. Tässä on kaksi esimerkkiä CPE:stä: `cpe:/o:microsoft:windows_8.1:r1` ja `cpe:/a:apache:http_server:2.4.35`



Tässä tunnistamme selvästi niiden tyypit `o` käyttöjärjestelmälle, `a` sovellukselle, myyjälle, tuotteelle ja versiolle.



Jos jokin näistä säännöllisistä lausekkeista _täsmää_, saamme palvelun nimen lisäksi myös sen version ja tarkan CPE:n, mikä helpottaa kyseiseen versioon vaikuttavien CVE:iden löytämistä. Löydät nämä tiedot Nmapin vakiotulosteesta, ja tulet huomaamaan, että niistä on paljon hyötyä myös muihin tarkoituksiin, joita käsittelemme muutamassa kappaleessa.



_matches_:n ja yleisemmin `/usr/share/nmap/nmap/nmap-service-probes`-tiedoston direktiivien tarkka syntaksi ei lopu tähän, ja se voi vaikuttaa melko monimutkaiselta, jos et ole tottunut käsittelemään Nmapia ja sen tuloksia. Kannattaa kuitenkin ainakin pitää mielessä sen olemassaolo ja yleinen toiminta, mikä tulee myöhemmin tarpeeseen, kun haluat ymmärtää tai debugata tulosta, muokata skannausta tai jopa osallistua Nmapin kehitystyöhön.



### III. Nmapin käyttäminen versioiden havaitsemiseen



Nyt aiomme käyttää kaikkea tätä monimutkaista _Probe_- ja _Match_-mekaniikkaa yksinkertaisen vaihtoehdon avulla: `-sV`. Tämä yksinkertaisesti kertoo Nmapille: yritä selvittää tarkalleen, mitkä palvelut ja porttiversiot olet asettanut avoimiksi.



```
# Enable service and version detection
nmap 192.168.1.0/24 -sV
```



Tässä on täydellinen esimerkki tällaisen komennon tuloksesta:



![nmap-image](assets/fr/35.webp)



nmapin versiohavainnon tulokset sovelluksista, jotka ovat alttiina verkossa



Tässä näemme, että Nmap on onnistunut tunnistamaan kaikki tämän kohteen verkkopalvelujen versiot ja näyttää nämä tiedot uudessa "VERSIO"-sarakkeessa. On mahdollista nähdä melko tarkat tiedot, jopa käyttöjärjestelmää myöten, jos nämä tiedot ovat osa talteenotettua allekirjoitusta.



Jos haluat ymmärtää yksityiskohtaisesti, mitä haavoittuvuuden tarkistuksen aikana tapahtuu, voimme käyttää `--version-trace` -vaihtoehtoa. Tämä tarjoaa debug-tilanäkymän, jossa näytetään havaintoon johtanut _Probe_:



```
# Enable version detection debug
nmap 192.168.1.0/24 -sV --version-trace
```



Tämän seurauksena meillä on paljon tietoa selvitettävänä. Yritä tunnistaa rivit, jotka alkavat sanoilla `Service scan Hard match`. Tämän jälkeen näet tällaisia rivejä:



```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```



Näemme selvästi, mitä _Probeja_ käytettiin teknologian ja version havaitsemiseen (tässä tapauksessa `NULL` ja `GetRequest` _Probeja_), sekä haetut tiedot.



### IV. Testien hallinta ja havaintotarkkuus



Palataan nyt tiedostoon `/usr/share/nmap/nmap-service-probes`, jota emme tarkastelleet aiemmin:



![nmap-image](assets/fr/36.webp)



probes `rarity`-direktiivi tiedostossa `/usr/share/nmap/nmap-service-probes`._



Tätä direktiiviä käytetään ilmaisemaan _Probe_:iin liittyvä harvinaisuus (eli prioriteetti/todennäköisyys). Tämän 1:stä 9:ään vaihtelevan merkinnän avulla voit hallita Nmapin suorittaman analyysin täydellisyyttä, kun lähetät _Probe_-analyysejä. Nmapin "merkintäjärjestelmässä" harvinaisuus 1 antaa tietoa suurimmassa osassa tapauksia, kun taas harvinaisuus 8 tai 9 edustaa hyvin erikoistapausta, joka koskee harvoin esiintyvää kokoonpanoa tai palvelua.



Selkeämmin sanottuna oletustapauksessa Nmap lähettää kullekin tunnistettavalle palvelulle _Probes_, joiden harvinaisuus on välillä 1-7. Jotta saisit paremman käsityksen _Probes_:n jakautumisesta _rarity_:n mukaan, tässä on niiden lukumäärä:



```
$ grep -E "^rarity" nmap-service-probes |sort |uniq -c

6 rarity 1
1 rarity 2
3 rarity 3
8 rarity 4
9 rarity 5
13 rarity 6
8 rarity 7
81 rarity 8
54 rarity 9
```



Saattaa tuntua intuition vastaiselta, mutta harvinaisuuksia 8 ja 9 on enemmän kuin muita. Tämä johtuu nimenomaan siitä, että harvinaisuus 1 -luotaimet ovat yleisiä ja toimivat useimmissa tapauksissa palvelusta riippumatta (muista `NULL`-luotaimet, jotka yksinkertaisesti lähettävät tyhjän TCP-paketin). Sen sijaan monimutkaisemmat koettimet ovat lähes ainutlaatuisia palveluittain.



Jos haluamme manuaalisesti hallita koettimia, joita haluamme käyttää versioskannauksessa, voimme käyttää `--version-intensity`-vaihtoehtoa. Tässä on kaksi esimerkkiä:



```
# Less accurate version detection than default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Very deep detection, using all existing Probes
nmap 192.168.1.0/24 -sV --version-intensity 9
```



Lopuksi tässä on esimerkki _Probe_ 9:stä ja 8:sta:



![nmap-image](assets/fr/37.webp)



esimerkkejä Probe-luotaimista harvinaisuuksilla 8 ja 9 tiedostossa `/usr/share/nmap/nmap-service-probes`._



Nämä kaksi luotainta havaitsevat Quake1- ja Quake2-palvelimet (videopeli). Kiinnostavia nostalgian kannalta, mutta tuskin kovin hyödyllisiä jokapäiväisessä elämässä.



Riippuen tarkkuus- tai nopeustarpeistasi, muista, että tämä harvinaisuusperiaate on olemassa ja voi vaikuttaa tulokseen.



### V. Nmapin käyttäminen käyttöjärjestelmien havaitsemiseen



Tarkastelemme nyt, miten Nmap voi auttaa meitä havaitsemaan verkossa skannattujen ja havaittujen isäntien käyttöjärjestelmät. Tätä varten käytetään Nmapin `-O`-optiota (joka tarkoittaa `OS Scan`).



```
# Enable OS Scan
nmap -O 10.10.10.0/24
```



Tässä on esimerkki tuloksista. Tässä Nmap kertoo, että kyseessä on todennäköisesti Linux-käyttöjärjestelmä, ja tarjoaa erilaisia tilastoja sen tarkasta versiosta.



![nmap-image](assets/fr/38.webp)



käyttöjärjestelmän tunnistamisen todennäköisyyden havaitseminen Nmapin avulla



Tämän saavuttamiseksi Nmap käyttää useita tekniikoita, jotka toimivat hyvin samalla tavalla kuin _Probes_ ja _Matches_ teknologian ja version havaitsemisessa. Suurin ero on siinä, että Nmap käyttää ICMP-, TCP-, UDP- ja muiden protokollien melko "matalan tason" parametreja. Seuraavassa on kaksi testiesimerkkiä Microsoft Windows 11 -käyttöjärjestelmän havaitsemiseksi:



![nmap-image](assets/fr/39.webp)



esimerkkejä Nmapin suorittamista testeistä Windows 11 -käyttöjärjestelmän havaitsemiseksi



Myönnettäköön, että näitä testejä on hyvin vaikea tulkita, emmekä aio yrittää ymmärtää niitä syvällisesti Nmapin alkeisopetuksen yhteydessä. Jos haluat perehtyä aiheeseen syvällisemmin, näitä tietoja sisältävä tiedosto on `/usr/share/nmap/nmap/nmap-os-db`.



Sinun on kuitenkin oltava tietoinen siitä, että käyttöjärjestelmän havaitseminen on pikemminkin Nmapin määrittelemä todennäköisyys kuin varmuus.



### VI. Päätelmät



Tässä osiossa opimme käyttämään Nmapin vaihtoehtoja skannattujen isäntien ja palveluiden tekniikoiden, versioiden ja käyttöjärjestelmien havaitsemiseen. Nyt meillä on hyvä käsitys siitä, miten Nmap hankkii nämä tiedot etänä. Olemme myös tarkastelleet vaihtoehtoja sanamäärän ja testien tarkkuuden hallintaan sekä työkalun rajoituksia näissä asioissa.



Seuraavassa osassa opimme, miten Nmapin NSE-skriptejä käytetään tietojärjestelmämme turvallisuusanalyysin tekemiseen. Lue edelliset osiot tarvittaessa uudelleen, äläkä epäröi harjoitella ja syventyä itse työkalun uumeniin, jotta hallitset paremmin sen, mitä olemme tähän mennessä oppineet.




## 7 - Tietoturva-analyysi: haavoittuvuuksien havaitseminen



### I. Esittely



Tässä osiossa opimme käyttämään Nmap-verkkoskannaustyökalua skannauskohteiden haavoittuvuuksien havaitsemiseen ja analysointiin. Tarkastelemme erityisesti tämän tehtävän suorittamiseen käytettävissä olevia eri vaihtoehtoja ja tutkimme työkalun mahdollisuuksien rajoja, jotta voimme ymmärtää ja tulkita sen tuloksia paremmin.



Tässä ensimmäisessä osiossa tutustumme Nmapin haavoittuvuusskanneriin ja näemme, miten haavoittuvuuksien havaitsemisen perusvaihtoehtoja käytetään. Seuraavissa osioissa tarkastelemme tarkemmin, miten tämä ominaisuus toimii ja miten sitä voidaan mukauttaa.



### II. Nmapin käyttö haavoittuvuuksien havaitsemiseen



Haluamme nyt käyttää Nmap-verkkoskanneria tietojärjestelmämme palveluiden ja järjestelmien haavoittuvuuksien havaitsemiseen. Tämä tarkoittaa, että aktiivisten isäntien löytämisen, alttiina olevien palvelujen luetteloinnin sekä versioiden ja tekniikoiden havaitsemisen lisäksi Nmap etsii haavoittuvuuksia.



Tämän saavuttamiseksi Nmap luottaa NSE-skripteihin (_Nmap Scripting Engine_), joita voidaan pitää moduuleina, jotka mahdollistavat yksityiskohtaisen lähestymistavan testaukseen.



Oikeilla asetuksilla pyydämme Nmapia käyttämään erilaisia NSE-skriptejä jokaisessa löydetyssä palvelussa, jolloin voimme löytää:





- Konfigurointivirheet ;





- Lisä- ja kehittyneempi versio ja käyttöjärjestelmän löydöt ;





- Tunnetut haavoittuvuudet (CVE) ;





- Heikot tunnisteet ;





- Haittaohjelmatartunnan tyypillinen Elements ;





- Palvelunestomahdollisuudet ;





- Jne.




Kuten huomaat, NSE-skriptit laajentavat merkittävästi Nmapin mahdollisuuksia verkko-operaatioiden osalta. Ja tämä mahdollistaa paljon edistyneempien tehtävien suorittamisen kuin koskaan ennen. Hyvä uutinen on, että kuten tavallista, näitä ominaisuuksia voi käyttää yksinkertaisesti vaihtoehdon kautta ja oletusyhteydessä. Tämän näemme seuraavaksi.



### III. Esimerkki haavoittuvuuden tarkistuksesta



NSE-skriptejä voidaan käyttää, kun Nmapia käytetään isännän yksittäisen portin, isännän kaikkien palveluiden tai kaikkien useissa verkoissa havaittujen palveluiden skannaamiseen. Voimme siis käyttää tulevia vaihtoehtoja kaikissa tähän mennessä tutkimissamme yhteyksissä.



Jotta voimme ottaa haavoittuvuuksien skannauksen käyttöön Nmap-skannauksen kautta, meidän on käytettävä `-sC`-optiota:



```
# Enable vulnerability scanning during a scan
nmap -sC 10.10.10.152
```



Muista, että jos et määritä mitään, Nmap skannaa oletusarvoisesti vain 1000 yleisintä porttia. Se ei löydä haavoittuvuuksia eksoottisemmista porteista, joita kohteesi saattavat käyttää.



Ennen kuin käytät tätä toimintoa tuotantotietojärjestelmässä, pyydän sinua jatkamaan ohjeen lukemista. Seuraavissa osioissa tarkastelemme sitä, miten ajettavien testien vaikutusta ja tyyppejä voidaan hallita paremmin.



Käyttämällä uudelleen aiemmin oppimaamme, voimme esimerkiksi olla kattavampia ja skannata kaikki kohteen TCP-portit:



```
# Enable vulnerability scanning on all ports
nmap -sC -p- 10.10.10.152
```



Tässä on Nmap-skannauksen tulos NSE-skriptien avulla:



![nmap-image](assets/fr/40.webp)



esimerkki Nmapin kautta tehdyn haavoittuvuustarkastuksen tuloksista isäntäasemalla._



Tässä näkyvät haavoittuvuusanalyysin yhteydessä kiinnostavat lisätiedot:





- FTP-palvelua voi käyttää nimettömänä, eikä sitä ole suojattu todennuksella. Tästä todentamisesta vastaava NSE-skripti kertoo sen meille ja näyttää jopa osan FTP-palvelun puurakenteesta. Tässä näemme, että meillä on pääsy Windows-järjestelmän `C`-hakemistoon!





- Edistyneestä verkkopalvelun hausta vastaava NSE-skripti näyttää sivun otsikon, jolloin saamme paremman käsityksen siitä, mitä verkkopalvelu isännöi.





- Meillä on myös SMB-palvelun kokoonpanon minianalyysi (skriptit `smb2-time`, `smb-security-mode` ja `smb2-security-mode`). Tiedot näytetään hieman eri tavalla verkkotarkastustuloksen jälkeen, jotta niitä olisi helpompi lukea. Nämä tiedot osoittavat erityisesti SMB Exchange -allekirjoitusten puuttumisen. Tämä konfiguraation heikkous mahdollistaa kohteen käyttämisen SMB Relay -hyökkäyksessä, joka on huomattava tietoturva-aukko, jota käytetään usein hyväksi tunkeutumis- ja verkkohyökkäystesteissä.




Tämä on tietenkin vain yksi esimerkki. Nmapilla on NSE-skriptejä monille palveluille, jotka kohdistuvat monenlaisiin haavoittuvuuksiin. Tarkastelemme näitä mahdollisuuksia tarkemmin seuraavassa osiossa.



Haavoittuvuuksien skannauksen esittelyn päätteeksi tässä on täydellinen komento verkon löytämistä, TCP-porttien skannausta, versioiden ja haavoittuvuuksien havaitsemista varten:



```
# Complete and realistic vulnerability scan command
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```



Tässä komento, joka alkaa näyttää realistisemmalta Nmapin käyttötapauksilta!



### IV. Nmapin rajoitusten ymmärtäminen haavoittuvuuksien skannauksessa



Tehdään tämä selväksi: Nmap ei pysty suorittamaan täydellistä tietojärjestelmäsi tunkeutumistestiä tai simuloimaan Red Team -operaatiota. Sillä on useita rajoituksia, joista sinun on oltava tietoinen, jos et halua luoda väärää turvallisuuden tunnetta:





- Rajoitettu kattavuus**: Vaikka Nmapin NSE-skriptit ovat tehokkaita, niiden testien kattavuus voi olla rajallinen verrattuna muihin erikoistuneisiin haavoittuvuuksien etsintätyökaluihin. Käytettävissä olevat NSE-skriptit eivät välttämättä kata joitakin haavoittuvuuksia, kuten Active Directory -haavoittuvuuksia, arkaluonteisten tietojen paljastumista tai edistyneempiä haavoittuvia verkkosovelluksia.





- Haavoittuvuuden monimutkaisuus**: Tietyntyyppisiä haavoittuvuuksia voi olla vaikea havaita NSE-skriptien avulla niiden monimutkaisuuden vuoksi. Esimerkiksi haavoittuvuuksia, jotka edellyttävät monimutkaista vuorovaikutusta etäpalvelun kanssa, ei ehkä havaita tehokkaasti Nmapilla (kuten esimerkiksi liiallisia oikeuksia tiedostojen jakamisessa tai virheitä käyttöoikeuksien hallinnassa verkkosovelluksessa).





- Passiivinen havaitseminen**: Tämä tarkoittaa, että se ei välttämättä havaitse mahdollisia haavoittuvuuksia tehokkaasti ilman aktiivisen yhteyden muodostamista kohdeisäntäkoneisiin. Haavoittuvuudet, jotka eivät ilmene aktiivisen skannauksen aikana, voivat siksi jäädä huomaamatta (kuten verkkosovelluksen koodin injektio).





- Riippuvuus päivityksistä**: Nmapin [tietokanta](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) NSE-skripteistä kehittyy jatkuvasti, mutta uuden haavoittuvuuden löytymisen ja vastaavan skriptin lisäämisen Nmapiin voi kestää jonkin aikaa. Tämän seurauksena Nmap ei välttämättä ole aina ajan tasalla uusimpien haavoittuvuuksien suhteen.





- Vääriä positiivisia ja vääriä negatiivisia tuloksia**: Kuten mikä tahansa tietoturvatyökalu, Nmapin NSE-skriptit voivat tuottaa vääriä positiivisia tuloksia (vääriä haavoittuvuushälytyksiä) tai vääriä negatiivisia tuloksia (todellisia haavoittuvuuksia ei havaita). Tämä on syytä pitää mielessä Nmapin tuloksia analysoitaessa.




On siis tärkeää ymmärtää, mitä Nmap tekee ja mitä se ei tee, ja samoin tietää, miten sen tuloksia tulkitaan. Olemme nähneet tässä oppaassa, että oletusasetukset voivat johtaa siihen, että emme huomaa tärkeää Elements:ta, joka voidaan paljastaa huolellisella käytöllä.



Olitpa sitten verkon järjestelmänvalvoja, tietoturva-insinööri tai jopa CISO, Nmapin avulla saat yleiskuvan tietojärjestelmän tietoturvatilanteesta. Tämä on tärkeä ensimmäinen askel järjestelmän suojaamisessa, ja IT-tiimi voi suorittaa sen säännöllisesti. Sen ei kuitenkaan pitäisi korvata [kyberturvallisuuden] asiantuntijoiden (https://www.it-connect.fr/cours-tutoriels/securite-informatique/) väliintuloa ja neuvoja, sillä he pystyvät paljastamaan puutteet paljon Nmapia kattavammin.



### V. Päätelmät



Tässä moduulin 3 ensimmäisessä osassa esittelimme haavoittuvuuksien skannauksen Nmapin avulla. Tiedämme nyt, miten päävaihtoehtoa käytetään tämän tehtävän suorittamiseen, mutta tiedämme myös harjoituksen rajat. Seuraavassa jaksossa tarkastelemme tätä toimintoa lähemmin ja käytämme NSE-skriptejä, joilla Nmapin teho kymmenkertaistetaan.



## 8 - Nmapin NSE-skriptien käyttö



### I. Esittely



Tässä osassa tarkastelemme perusteellisesti NSE-skriptejä (_Nmap Scripting Engine_). Tarkastelemme erityisesti sitä, miksi ne ovat yksi tämän työkalun suurista vahvuuksista, miten ne toimivat ja miten selata ja käyttää monia olemassa olevia skriptejä.



Tämä osio on jatkoa edelliselle oppaalle, jossa opimme käyttämään Nmapin haavoittuvuuksien skannausominaisuuksia perustasolla. Tarkastelemme nyt tarkemmin, miten [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) toimii tässä suhteessa, jotta voimme jälleen kerran tehdä tarkempia ja hallitumpia skannauksia.



### II. Nmapin NSE-skriptien käsite



Nmapin NSE-skriptien avulla voit laajentaa sen ominaisuuksia erittäin joustavasti. Ne on kirjoitettu LUA-kielellä, joka on helpompi käsitellä ja käyttää kuin Nmapin käyttämä C- tai C#-kieli. LUA-skriptin käyttämisen etu Nmapin kanssa erillisen työkalun sijaan on se, että sen avulla voidaan hyödyntää Nmapin suoritusnopeutta ja vakio-ominaisuuksia (isäntä-, portti- ja versiohaku jne.).



Skriptit on järjestetty luokittain, ja yksi skripti voi kuulua useampaan kuin yhteen luokkaan:



| Catégorie       | Description |
|----------------|-------------|
| **auth**       | Contient les scripts relatifs à l’authentification sur des services, dont l’accès anonyme ou l’énumération des utilisateurs. Exemples: `oracle-enum-users`, `ftp-anon`. |
| **broadcast**  | Contient les scripts relatifs aux opérations de broadcast sur le réseau, notamment en vue d’exploiter et de découvrir certains services, hôtes ou protocoles reposant sur le broadcast (IPv6, wake on lan, IGMP, etc.). Exemples: `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute**      | Contient les scripts relatifs aux opérations de brute force de l’authentification sur les services (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, etc.). Exemples: `ssh-brute`, `vnc-brute`. |
| **default**    | Contient les scripts utilisés dans le cas par défaut (utilisation de `-sC`). Plusieurs critères sont utilisés afin de valider l’entrée d’un script dans cette catégorie dont la vitesse d’exécution, la structure de la sortie, la fiabilité du test, le caractère “intrusif” ou “risqué”, etc. |
| **discovery**  | Contient les scripts relatifs à la découverte avancée du réseau et des services. On y retrouve par exemple l’énumération du contenu d’un partage SMB, d’une version d’un service VNC, des requêtes SNMP, etc. Exemples: `mysql-info`, `http-security-headers`. |
| **dos**        | Contient les scripts pouvant causer un déni de service. Il peut s’agir de scripts créés pour exploiter une vulnérabilité de type déni de service ou alors de scripts ayant pour effet de bord un déni de service. Prudence donc (ils sont exclus de la catégorie `default`). Exemples: `http-slowloris`, `ipv6-ra-flood`. |
| **exploit**    | Contient les scripts créés pour exploiter de manière directe une vulnérabilité. Exemples: `http-shellsock`, `smb-vuln-ms08-067`. |
| **external**   | Contient les scripts qui nécessitent l’utilisation d’une ressource tierce, comme une base d’information en ligne. Cela indique notamment une tentative de connexion vers l’extérieur (attention à la confidentialité). Exemples: `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer**     | Contient les scripts conçus pour envoyer des trames, paquets ou paramètres inattendus par un service. Cela permet notamment de causer des erreurs ou dysfonctionnements afin d’obtenir des pistes de vulnérabilité ou des informations techniques. Exemples: `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive**  | Contient les scripts qui sont catégorisés comme “risqués” d’un point de vue disponibilité, ou détection. Ils peuvent provoquer un crash du système ou être détectés comme malveillant par une solution de sécurité. Il s’agit de la catégorie inverse de `safe`. Exemples: `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware**    | Contient les scripts conçus pour détecter la présence d’élément caractéristique d’un malware, tel qu’un port en écoute communément utilisé par une backdoor connue. Exemples: `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe**       | Contient les scripts qui sont considérés comme sûrs d’un point de vue détection ou stabilité. Il s’agit de la catégorie inverse de `intrusive` et elle contient en grande majorité des scripts avancés d’identification de version ou de relevé d’élément de configuration. Exemples: `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version**    | Contient les scripts qui permettent une détection avancée de version. Ils peuvent être utilisés en complément des Probes et Matchs étudiés précédemment quand la détection d’une version nécessite des opérations un peu plus complexes. Exemples: `http-php-version`, `vmware-version`. |
| **vuln**       | Contient les scripts conçus pour détecter la présence de vulnérabilité connue (CVE) sans pour autant les exploiter (à l’inverse de la catégorie `exploit`). Ils se contentent en général de rapporter le statut “vulnérable” ou non d’un service. Exemples: `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |


Teknisesti ottaen luokat, joihin skripti kuuluu, ilmoitetaan suoraan sen koodissa.



![nmap-image](assets/fr/41.webp)



nSE-skriptiluokat `ftp-anon`._



Tässä esimerkissä näytetään osa NSE-skriptin `ftp-anon.nse` koodista, jonka suorittamisen näimme edellisessä osassa.



### III. Luettelo nykyisistä NSE-skripteistä



Oletusarvoisesti Nmapin NSE-skriptit sijaitsevat hakemistossa `/usr/share/nmap/scripts/` ilman erityistä puurakennetta tai hierarkiaa. Seuraavassa on yleiskatsaus tämän hakemiston sisältöön:



![nmap-image](assets/fr/42.webp)



poimii NSE-skriptejä sisältävän hakemiston `/usr/share/nmap/scripts/` sisällön._



Tämä hakemisto sisältää yli 5 000 NSE-skriptiä. Useimmissa tapauksissa komentosarjan nimen alkuosa sisältää protokollan tai luokan, johon komentosarja kuuluu. Näin voimme lajitella luettelon, esimerkiksi jos haluamme listata kaikki FTP-palveluun kohdistuvat skriptit:



![nmap-image](assets/fr/43.webp)



luettelo NSE Nmap-skripteistä, joiden nimet alkavat `ftp-`._



Nmap ei oikeastaan tarjoa vaihtoehtoa NSE-skriptien selaamiseen ja listaamiseen; voit käyttää komentoa `--script-help`, jota seuraa luokan nimi tai sana:



```
# List all scripts whose name starts with "ftp-"
nmap --script-help=ftp-*

# List all scripts from the "discovery" category
nmap --script-help=discovery
```



Tuloksena on kuitenkin jokaisen skriptin nimi ja kuvaus, mikä ei ole optimaalista, jos haku tuo esiin useita kymmeniä skriptejä:



![nmap-image](assets/fr/44.webp)



nmapin `--script-help`-komennon käytön tulos



Mielestäni tehokkain tapa on käyttää klassisia Linux-komentoja hakemistossa `/usr/share/nmap/scripts/`:



```
# List scripts targeting the "ssh" service
ls -al /usr/share/nmap/scripts/ssh*

# List scripts from the "dos" category
grep -rl '"dos"' /usr/share/nmap/scripts/
```



Voit vapaasti selata sinua kiinnostavien moduulien koodia, jotta ymmärrät paremmin, miten NSE-skripti toimii.



### IV. Nmapin NSE-skriptien käyttö



Nyt opettelemme tekemään haavoittuvuustarkastuksia valitsemalla huolellisesti ne NSE-skriptit, joista olemme kiinnostuneita.



#### A. Valitse käsikirjoitukset luokittain



Aluksi voimme valita, haluammeko suorittaa kaikki tiettyyn luokkaan kuuluvat komentosarjat. Meidän on ilmoitettava tämä luokka tai nämä luokat Nmapille argumentilla `--script <category>`:



```
# Use default NSE scripts
nmap --script default 10.10.10.152
```



Tämä ensimmäinen komento vastaa komentoa `nmap -sC`. Oletusarvoisesti Nmap valitsee skriptit luokasta `default`, mutta se on vain väitteen vuoksi. Seuraava komento käyttää esimerkiksi kaikkia `discovery`-luokan skriptejä:



```
# Use NSE scripts from the "discovery" category
nmap --script discovery 10.10.10.152
```



Kuten olemme nähneet, joidenkin luokkien avulla voimme nopeasti tunnistaa, mitä asiaan liittyvät NSE-skriptit tekevät (`discovery`, `vuln`, `exploit`), kun taas toiset luokat määrittelevät suoritetun testin riskin, havaitsemisen tai vakauden tason. Jos olemme arkaluontoisessa tilanteessa eikä meillä ole hyvää käsitystä skriptivalintamme suorittamista eri toiminnoista, voimme yhdistää valinnat ja valita vain ne skriptit, jotka kuuluvat luokkiin `discovery` ja `safe`:



```
# Use scripts from multiple categories
nmap --script "discovery and safe" 10.10.10.152
```



Jos haluat ehdottomasti ja nimenomaisesti sulkea skriptit pois luokkien `dos` ja `intrusionive` piiristä, voit käyttää seuraavaa merkintätapaa:



```
# Exclude categories
nmap --script "not intrusive and not dos" 10.10.10.152
```



Huomaa, että jos määrittelet poissulkemisehdot edellä esitetyllä tavalla, kaikki muut luokat, joita ei ole nimenomaisesti suljettu pois, otetaan käyttöön. Oikeudenmukaisuuden vuoksi voisimme määritellä esimerkiksi:



```
# Include scripts from the "vuln" category except those that are too risky
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Same thing, but only targeting the HTTP protocol
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```



Seuraavassa on joitakin esimerkkejä siitä, miten NSE-skriptejä tulisi käsitellä luokittain, erityisesti silloin, kun Nmapia käytetään haavoittuvuusanalyyseihin todellisissa tilanteissa.



#### B. Valitse käsikirjoitukset yksikkönä



Voimme myös valita analyysin aikana yksittäisen testin, joka vastaa NSE-skriptiä. Tätä varten meidän on määritettävä skriptin nimi parametrissa `-script <name>`. Esimerkkinä on `ftp-anon.nse`-skripti:



```
# Use an NSE script and a specific port
nmap --script ftp-anon -p 21 10.10.10.152
```



Saamme siis erittäin tarkan tuloksen:



![nmap-image](assets/fr/45.webp)



tulos NSE:n `ftp-anon`-skriptin käytöstä FTP-porttiin Nmapin kautta._



Näemme tuloksen, kun `ftp-anon`-skripti ajetaan porttiin 21, eikä mihinkään muuhun porttiin, koska määrittelimme vaihtoehdon `-p 21`. Olisimme myös voineet suorittaa perusporttiskannauksen, jolloin `ftp-anon` NSE-skripti olisi suoritettu vain havaittuihin FTP-palveluihin:



```
# Use a specific NSE script
nmap --script ftp-anon 10.10.10.152
```



Nmap olisi siis suorittanut tämän nimettömän yhteyden testin myös, jos se olisi löytänyt FTP-palvelun toisesta portista.



Lyhyen kuvauksen siitä, mitä NSE-skripti tekee, saat edellä mainitulla `--script-help`-valinnalla:



![nmap-image](assets/fr/46.webp)



ohje näyttää NSE-skriptin `sshv1`._ tulokset



Lyhyesti sanottuna voimme jälleen kerran käyttää uudelleen kaikkia tähän asti käyttämiämme verkonhakuvaihtoehtoja, palveluja, versioita ja teknologioita!



#### C. Komentosarjan argumenttien hallinta



Nmapin käytön aikana törmäät tiettyihin NSE-skripteihin, jotka vaativat syöttöargumentteja toimiakseen oikein. Tarkastelemme nyt, miten näille skripteille voidaan antaa argumentteja Nmapin asetusten kautta.



Otetaan esimerkiksi `ssh-brute`-skripti, jonka avulla voit suorittaa SSH-palveluun brute force -hyökkäyksen.



Klassinen brute force -hyökkäys koostuu useiden salasanojen (joskus miljoonien) testaamisesta yrittäessä tunnistautua tietylle tilille. Kun hyökkääjä kokeilee niin monia salasanoja, hän lyö vetoa sen todennäköisyydestä, että käyttäjä on käyttänyt heikkoa salasanaa hyökkäyksessä käytetyssä salasanasanakirjassa.



Tässä komentosarjassa on "oletusasetukset", joita voimme muokata omaan asiayhteytemme sopiviksi. Tämän hyökkäyksen yhteydessä voimme esimerkiksi antaa Nmapille luettelon käyttäjistä ja käytettävän salasanasanakirjan. Tietääkseni skriptin vaatimia argumentteja ei ole mahdollista luetella helposti, joten luotettavin tapa on käydä Nmapin virallisella verkkosivustolla. Suoran linkin NSE-skriptin dokumentaatioon saa vastauksena `--script-help`-vaihtoehtoon:



![nmap-image](assets/fr/47.webp)



nSE `ssh-brute`-skriptin ohjeen näyttämisen tulos, jossa on linkki osoitteeseen nmap.org._



Napsauttamalla osoitettua linkkiä pääset tälle sivustolle [https://nmap.org](https://nmap.org/):



![nmap-image](assets/fr/48.webp)



luettelo argumenteista, jotka voidaan välittää Nmapin `ssh-brute` NSE-skriptille



Tässä on selkeä kuva käytettävistä argumenteista, joista tärkeimmät ovat `passdb` (tiedosto, joka sisältää luettelon salasanoista) ja `userdb` (tiedosto, joka sisältää luettelon käyttäjistä). Tässä dokumentaatiossa viitataan Nmapin sisäisiin kirjastoihin, sillä nämä brute force -mekanismit ja niihin liittyvät optiot on mutualisoitu, jotta niitä voidaan käyttää yhdenmukaisesti useissa skripteissä (`ssh-brute`, `mysql-brute`, `mssql-brute` jne.), ja siksi niillä on enemmän tai vähemmän samat argumentit:



```
# Create a file containing my user list
echo "root" > /tmp/userlist

# Create a file containing my password list
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Run an SSH brute force via Nmap network scan
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```



Kuten näet tässä viimeisessä komennossa, voimme määrittää Nmap-skriptille tarvittavat argumentit käyttämällä `--scripts-args key=value,key=value`-vaihtoehtoa. Tässä on mahdollinen tulos Nmapin tulosteesta, kun suoritetaan SSH-brute force -operaatio `ssh-brute` NSE-skriptin avulla:



![nmap-image](assets/fr/49.webp)



nmap._ kautta suoritetun SSH bruteforce -toteutuksen tulos



Kuten näet, NSE-skriptien tuottamat tiedot on merkitty interaktiivisessa tulosteessa (terminaalitulosteessa) etuliitteellä `NSE: [skriptin nimi]`, mikä helpottaa niiden löytämistä. Nmap-tulosten tavanomaisessa näytössä on vain yhteenveto, jossa ilmoitetaan, onko heikkoja tunnisteita löydetty (myös salasanoja, muista).



Ottaaksemme askeleen pidemmälle ja muistuttaaksemme siitä, että tätä kaikkea voidaan käyttää kaikkien jo tarkastelemiemme vaihtoehtojen lisäksi, tässä on komento, joka löytää `10.10.10.0/24`-verkon, skannaa 2000 yleisintä TCP-porttia ja suorittaa anonyymin pääsyn haun FTP-palveluihin ja raa'an voimakeinon kampanjan SSH-palveluihin:



```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```



Tämä on vain yksi esimerkki monista saatavilla olevista skripteistä ja niiden vaihtoehdoista. Nyt meillä on kuitenkin parempi käsitys siitä, miten NSE-skripteihin päästään käsiksi, vaativatko ne argumentteja ja miten nämä argumentit välitetään Nmapille.



### V. Päätelmät



Tässä osassa opimme, miten Nmapin NSE-skriptejä käytetään eri tehtävien suorittamiseen. Kehotan sinua tutustumaan eri skriptiluokkiin ja itse skripteihin, jotta näet, kuinka monta testiä niillä voidaan automatisoida.



Olemme jo useiden osien ajan keränneet enemmän tai vähemmän kehittyneitä löytö-, skannaus- ja luettelointivaihtoehtoja. Tähän mennessä sinun pitäisi olla tietoinen siitä, että Nmapin tulosteet ja tulosten näyttäminen alkaa muuttua melko laajaksi, joskus jopa liian laajaksi päätelaitteellemme. Seuraavassa osiossa opimme hallitsemaan tätä tulostetta, erityisesti tallentamalla sen eri muotoisiin tiedostoihin.






## 9 - Nmapin lähtötietojen hallinta




### I. Esittely



Tässä osiossa tarkastelemme Nmapin tuottamaa tulostetta ja erityisesti tulosteen eri muotoiluvaihtoehtoja. Näemme, että Nmap voi tuottaa useita eri tulostusmuotoja eri tarpeisiin, ja tämäkin on yksi tämän työkalun suurista vahvuuksista.



Oletusarvoisesti Nmap tarjoaa yksityiskohtaisen näkymän suorittamiensa tarkistusten ja testien tuloksista. Tämä sisältää skannatut isännät ja palvelut, ne, joihin on havaittu olevan pääsy, avoimien porttien yksityiskohdat, niiden tilan ja version. Lisäksi NSE-skriptien yksityiskohdat ovat saatavilla myös terminaalitulosteessa. Tämä tuloste voi kuitenkin kasvaa nopeasti laajaksi, vaikka tiedot olisivatkin selkeästi muotoiltuja, mikä voi vaikeuttaa tarkkojen tietojen löytämistä tuloksista.



### II. Nmapin tulostusformaattien hallinta



#### A. Tallenna skannaustulokset tekstitiedostoon



Asioiden helpottamiseksi [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) tekee tulosteiden tallentamisesta tekstitiedostoon erittäin helppoa. Tämä voi olla hyödyllistä arkistointia, vertailua muihin testeihin sekä tulosteen selaamista varten erikoistuneilla tekstinkäsittelytyökaluilla tai skriptikielillä, kuten Sublime text, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/), Python, grep, sed jne. Voit tallentaa Nmapin vakiotulosteen tekstitiedostoon käyttämällä `-oN <tiedostonimi>` -vaihtoehtoa ("N" sanasta "normal"):



```
# Save Nmap output to a file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```



Ei siis mikään yllätys, sillä Nmap näyttää tavanomaisen vakiotulosteensa päätelaitteessamme, mutta myös määritetyssä tiedostossa.



#### B. generate Nmapin tuloste tiivistetyssä muodossa



"Teksti"-tyylissä on myös toinen tulostusmuoto, jonka ihminen voi helposti tulkita: "greppable"-muoto.



Tämä muoto luotiin tarjoamaan "tiivistetty" näkymä Nmapin tulosteesta, joka on jäsennelty siten, että sen käsittely on helpompaa esimerkiksi `grep`-työkaluilla. Katsotaanpa esimerkkiä tämäntyyppisestä tulosteesta:



![nmap-image](assets/fr/50.webp)



nmap-verkkoskannaus ja tulostus "greppable"-muodossa._



Tässä olen suorittanut verkon etsinnän sekä porttiskannauksen ja analysoinut teknologioita ja versioita /24-verkossa ja tallentanut tulokset tiedostoon "greppable"-muodossa. Tuloksena on tiedosto, jossa on 2 riviä aktiivista isäntää kohti:





- Ensimmäinen rivi kertoo, että kyseinen isäntä on _Yllä_;





- Toisella rivillä kerrotaan, mitkä portit on skannattu, niiden tila sekä haetut teknologia- ja versiotiedot hyvin tarkassa muodossa: `<portti>/<status/<protokolla>//<palvelu>//<versio>/,`




Tämä muotoilu kiinteällä erottimella mahdollistaa nopean käsittelyn tekstinkäsittelyohjelmilla, kuten `grep`, tai skripti- ja ohjelmointikielillä. Esimerkiksi seuraavan komennon avulla voin helposti hakea tietoja isännästä `10.10.10.10.5`, kun kyseessä on Nmapin suorittama valtava skannaus, jonka tulosteita olisi vaikea selata:



```
# Filter by IP address in the Nmap "greppable" file
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```



Toisaalta voin myös helposti luetella kaikki isännät, joilla on portti 21 auki, koska portit ja IP-osoite ovat samalla rivillä:



```
# Filter by open port in the Nmap "greppable" file
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```



Jos haluat generate:n, meidän on käytettävä `-oG <tiedostonimi>.gnmap` -vaihtoehtoa ("grep"-sanan "G"). Käytän tottumukseni mukaan tällaisesta tiedostosta tiedostopäätettä `.gnmap`, mutta voit vapaasti käyttää haluamaasi tiedostopäätettä:



```
# Save Nmap output to a file in "greppable" format
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```



Tätä muotoa voidaan käyttää moniin eri tarkoituksiin, ja se on erityisen hyödyllinen nopeassa käsikirjoittamisessa/lajittelussa. Siitä huolimatta siitä ollaan luopumassa seuraavaksi tarkasteltavan formaatin hyväksi.



huomautus: `-oG` greppable -muoto on virallisesti poistettu käytöstä Nmap 7.90:stä lähtien. Sitä voidaan edelleen käyttää yhteensopivuuden vuoksi. Sitä voidaan edelleen käyttää yhteensopivuustarkoituksiin, mutta on suositeltavaa käyttää XML- tai normaalia muotoa kaikessa kehityksessä tai automaattisessa jäsentelyssä._ _



#### C. XML-muoto Nmap-tulostetta varten



Viimeinen mainitsemisen arvoinen muoto tässä oppaassa on XML. Toisin kuin kahta edellistä formaattia, tätä formaattia ei ole suunniteltu ihmisten luettavaksi, vaan muiden työkalujen tai skriptien luettavaksi.



XML (_eXtensible Markup Language_) on merkintäkieli, jota käytetään tietojen tallentamiseen ja siirtämiseen ja joka tarjoaa hierarkkisen rakenteen mukautettujen tunnisteiden avulla.



Nmapissa XML-muotoa käytetään generate:n yksityiskohtaisiin raportteihin suoritetuista tarkistuksista, mukaan lukien tiedot isännistä, porteista ja havaituista haavoittuvuuksista sekä lisätietoja, joita ei näytetä Nmapin vakiotulosteessa.



Jos haluat generate XML-muotoisen tulostiedoston, meidän on käytettävä `-oX`-optiota ("O" sanasta "XML"):



```
# Save Nmap output to a file in XML format
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```



Tuloksena on Nmapin vakiotuloste päätelaitteessasi sekä XML-muotoinen tiedosto nykyisessä hakemistossasi.



XML-muotoa ei tietenkään ole suunniteltu ihmisten luettavaksi ja tulkittavaksi. Jos kuitenkin haluat tehdä skriptejä tai automatisoituja analyysejä Nmapin tulosteiden tässä muodossa, sinun on silti oltava selvillä käytetyistä tunnisteista ja rakenteesta. Tässä on esimerkiksi osa Nmapin luoman XML-tiedoston sisällöstä, joka näyttää yhden isännän skannaustulokset:



![nmap-image](assets/fr/51.webp)



esimerkki XML-tietueesta 1 isännälle Nmap-skannauksen aikana



Tässä on paljon tietoa, ja meitä kiinnostaa erityisesti kaksi avointa porttia:



```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Ymmärrämme, että tämä muoto helpottaa tulosten automaattista analysointia, koska jokainen tieto on siististi järjestetty omaan, nimettyyn tagiin tai attribuuttiin. Löydämme erityisesti tiedon, johon emme ole aiemmin törmänneet: CPE.



```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Mainitsimme lyhyesti CPE:n moduulin 2 jaksossa 2, ja tämä tieto määritetään otteluissa version tunnistuksen aikana. Nmap käyttää palvelu-, teknologia- ja versiotunnistusmekanismejaan löytääkseen siihen liittyvän CPE:n.



Näin voimme käyttää näitä tietoja uudelleen niitä käyttävissä tietokannoissa ja sovelluksissa. Ajattelen erityisesti NVD-tietokantaa, jossa viitataan CVE-tietoihin. Se sisältää kunkin CVE:n osalta CPE:t, joihin haavoittuvuus vaikuttaa. Tässä on esimerkki CVE:stä, joka koskee `a:microsoft:internet_information_services:7.5` NVD-tietokannasta:



![nmap-image](assets/fr/52.webp)



cPE:n esiintyminen NVD-tietokannassa olevan CVE:n tiedoissa



Ymmärrämme nyt paremmin tämän muodon edut, sillä se tarjoaa hyvin selkeän tietorakenteen ja sisältää kaikki Nmapin keräämät tai käsittelemät tiedot.



Tallennan Nmap-skannaukseni järjestelmällisesti kaikissa kolmessa muodossa kerralla. Tämän mahdollistaa `-oA <nimi>` -vaihtoehto ("A" tarkoittaa "All"), joka luo `<nimi>.nmap`-tiedoston, `<nimi>.xml`-tiedoston ja `<nimi>.gnmap`-tiedoston. Näin olen varma, ettei minulta lopu mitään, kun minun täytyy palata tuloksiin.



Näillä kolmella formaatilla sinulla pitäisi olla kaikki, mitä tarvitset Nmap-tulosten tallentamiseen ja automaattiseen käsittelyyn. Käytämme XML-muotoa uudelleen seuraavassa osassa, kun tarkastelemme Nmapin käyttöä muiden tietoturvatyökalujen kanssa.



#### III. HTML-raportin luominen Nmap-skannauksesta



XML-muoto tarjoaa monia mahdollisuuksia, eikä vähiten sitä, että sen pohjalta voidaan luoda HTML-muotoinen raportti, joka on visuaalisesti miellyttävämpi selattavaksi.



XML-muotoisen Nmap-tiedoston muuttamiseksi verkkosivuksi käytämme `xsltproc`-työkalua, joka on ensin asennettava:



```
# Install the xsltproc tool
sudo apt install xsltproc
```



Kun tämä työkalu on asennettu, anna sille muunnettava XML-tiedosto ja luotavan HTML-raportin nimi:



```
# Create an Nmap HTML report from XML
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Open the .html file with Firefox
firefox "Nmap – rapport web 05-2024.html"
```



Tuloksena meillä on koko skannaus hienosti jäsenneltynä, jopa muutamalla värillä ja klikattavilla linkeillä sisällysluettelossa!



![nmap-image](assets/fr/53.webp)



ote Nmapin skannausraportista HTML-muodossa, jonka on luonut xsltproc._



Yleisesti ottaen Nmapin tallentama XML-tiedosto sisältää viittauksen toiseen XSL-muotoiseen tiedostoon:



```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```



Muunnos HTML:ksi on siis Nmapin tarjoama ja helpottama toiminto, `xsltproc` on yleinen ja tunnustettu työkalu tämän tehtävän suorittamiseen (joka ei kuulu Nmapin työkalupakettiin).



XSLT (_Extensible Stylesheet Language Transformations_) on XSL:n osajoukko, jonka avulla XML-tiedot voidaan näyttää verkkosivulla ja "muuntaa" XSL-tyylien avulla luettavaksi, muotoilluksi tiedoksi HTML-muodossa.



lähde: [helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_



Raportin tietotaso vastaa Nmapin XML-muotoa ja on korkeampi kuin vakioterminaalin ulostulo (_interaktiivinen ulostulo_).



### IV. Nmapin sanamäärätason hallinta



Seuraavaksi tarkastelemme muutamia vaihtoehtoja Debugger Nmapia varten tai sen edistymisen seuraamiseksi.



Ensimmäinen vaihtoehto, joka on syytä mainita, on `-v`-optio, joka lisää Nmapin sanamäärää. Tässä on esimerkki:



![nmap-image](assets/fr/54.webp)



nmapin sanallinen tuloste käyttämällä `-v`._ -vaihtoehtoa



Kun skannaus kohdistuu moniin isäntäasemiin ja portteihin, päätteen tulostetta on vaikea hyödyntää näytettävien tietojen määrän vuoksi. Tästä syystä tätä vaihtoehtoa tulisi käyttää yhdessä aiemmin nähtyjen vaihtoehtojen kanssa, joiden avulla voit tallentaa Nmapin vakiotulosteen tiedostoon. Tähän tulostiedostoon ei sisällytetä sanamäärän käyttöön liittyviä tietoja. Kuten yllä olevasta esimerkistä näkyy, tämän sanamuodon avulla voit seurata Nmapin toimia ja löytöjä selkeästi ja suoraan. Pidemmissä skannauksissa, joissa tietojen näyttäminen voi olla hidasta, tällä vältetään sokeutuminen Nmapin senhetkiselle toiminnalle ja tieto siitä, että asiat etenevät ja millä tahdilla. Jos haluat lisätä sanamäärää vielä yhdellä tasolla, voit käyttää `-vv`-optiota.



Voit seurata Nmapin toimintaa tarkemmin skannauksen aikana käyttämällä `--packet-trace`-vaihtoehtoa. Vaihtoehdolla `-v` saat suoran lokin kaikista Nmapin löytämistä avoimista porteista, kun taas tällä vaihtoehdolla saat lokirivin jokaisesta porttiin lähetetystä paketista. Tämä tuottaa luonnollisesti hyvin yksityiskohtaisen tulosteen, mutta mahdollistaa Nmapin toiminnan yksityiskohtaisen seurannan, tässä esimerkki:



![nmap-image](assets/fr/55.webp)



nmapin toiminnan yksityiskohtainen seuranta `--packet-trace`:n avulla._



Näitä tietoja ei myöskään tallenneta Nmapin tuottamaan tulostiedostoon, jos käytetään `-oN`, `-oG`, `-oX` tai `-oA` -vaihtoehtoja.



Lopuksi Nmap tarjoaa myös kaksi debug-vaihtoehtoa: `-d` ja `-ddd`. Nämä vaihtoehdot käyttäytyvät samalla tavalla kuin `-v` -vaihtoehto, mutta ne lisäävät teknistä lisätietoa, kuten yhteenvedon teknisistä parametreista skannauksen alussa:



![nmap-image](assets/fr/56.webp)



ajoitusvaihtoehdot näkyvät Nmapin debug-näkymässä



Seuraavissa kappaleissa tarkastelemme, mitä "Ajoitus"-vaihtoehdot ovat ja miksi ne kannattaa tuntea.



Jos haluat vain yksinkertaisen, synteettisen yleiskuvan Nmap-skannauksen edistymisestä, voit käyttää vaihtoehtoa `--stats-every 5s`. "5s" tarkoittaa tässä 5 sekuntia, ja sitä voidaan muuttaa tarpeidesi mukaan. Tällä taajuudella saamme Nmapilta palautetta sen edistymisestä:



![nmap-image](assets/fr/57.webp)



nmapin `--stats-every`-valinnalla näytettävät tiedot



Erityisesti voimme saada edistymisprosentin sekä merkinnän siitä, missä vaiheessa se on: isännän löytämisvaihe [ping](https://www.it-connect.fr/le-ping-pour-les-debutants/) kautta, avoimien TCP-porttien löytämisvaihe jne. Nämä tiedot saadaan myös terminaalin tulosteesta painamalla "Enter" skannauksen aikana.



Nmap ei kuitenkaan ole kovin hyvä arvioimaan, kuinka kauan tehtävä kestää, eikä vähiten siksi, että se ei tiedä etukäteen, kuinka monta isäntäkohtaa ja palvelua sen on skannattava.



### V. Päätelmät



Tässä osiossa olemme tarkastelleet useita vaihtoehtoja Nmap-skannaustulosten tallentamiseksi eri tiedostomuodoissa. Tämä on erittäin kätevää, sillä realistisissa yhteyksissä skannaustulokset voivat käsittää satoja tai jopa tuhansia rivejä! Olemme myös nähneet, miten Nmapin verbaalisuustasoa voidaan nostaa debuggausta varten tai skannauksen edistymisraportin saamiseksi.



XML-muodosta on hyötyä erityisesti seuraavassa osassa, jossa tarkastelemme muutamia työkaluja, jotka voivat työskennellä Nmapin tulosten kanssa.




## 10 - Nmapin käyttö muiden tietoturvatyökalujen kanssa



### I. Esittely



Tässä osiossa tarkastelemme joitakin Nmapin klassisia käyttötapoja yhdessä muiden ilmaisten ja avoimen lähdekoodin tietoturvatyökalujen kanssa. Käytämme erityisesti edellisissä osioissa oppimaamme, jotta voimme parantaa Nmapin tehoa ja tehokkuutta entisestään.



Mahdollisuus tallentaa Nmap-skannaustulokset XML-muodossa tekee tiedoista yhteensopivia monien muiden työkalujen kanssa. Koska lähes kaikissa ohjelmointi- ja skriptikielissä on nykyään kirjastoja, jotka pystyvät jäsentämään XML:ää, tämä helpottaa huomattavasti tietojen käsittelyä. Useissa, erityisesti hyökkäysturvallisuuteen suunnatuissa työkaluissa on toimintoja Nmapin tuottaman XML-muodon käsittelyyn. Katsotaanpa tarkemmin.



Mainitsen muutaman hyökkäystyökalun selostamatta kuitenkaan yksityiskohtaisesti, miten niitä käytetään tai miten ne toimivat. Oletan, että lukija tuntee niiden peruskäytön ja että ne ovat jo toiminnassa. Tämä osio kiinnostaa erityisesti [kyberturvallisuuden] ammattilaisia (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), koulutuksessa olevia henkilöitä tai niitä, jotka ovat päättäneet syventyä aiheeseen.



### II. Nmapin tulosten tuominen Metasploitiin



Ensimmäinen työkalu, jota tarkastelemme Nmapin tietojen uudelleenkäyttöä varten hyökkäävässä tietoturva- ja haavoittuvuustutkimuksessa, on Metasploit.



Metasploit on exploit- ja hyökkäyskehys. Se on ilmainen ratkaisu ja tunnustettu työkalu, joka sisältää suuren määrän Ruby- tai Python-kielellä kirjoitettuja moduuleja. Niiden avulla voidaan hyödyntää haavoittuvuuksia, suorittaa hyökkäyksiä, luoda takaovia, hallita takaisinkutsuja (C&C eli Communication and Control -toiminnot) ja käyttää kaikkea yhtenäisesti.



Erityisesti tämä tunnettu ja laajalti käytetty käyttöjärjestelmä voi toimia postgreSQL-tietokannan (https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) kanssa, johon tallennetaan muun muassa isännät, portit, palvelut ja todennustiedot.





- Virallinen Metasploit-dokumentaatio: [https://docs.metasploit.com/](https://docs.metasploit.com/)




Tässä kohtaa Nmap ja sen tuotokset tulevat mukaan peliin, sillä Nmapin tuotosten XML-muoto voidaan helposti tuoda Metasploitin tietokantaan ja täyttää sen tietokanta isännistä ja palveluista, jotka voidaan sitten nopeasti nimetä tämän tai tuon hyökkäyksen kohteiksi.



Kun olen päässyt Metasploitin interaktiiviseen komentotulkkiin, aloitan luomalla työtilan, eräänlaisen tilan, joka on omiaan kulloisenkin päivän ympäristölleni:



```
# Create a Metasploit workspace
msf6 > workspace -a SI_siege
```



Kun työtilani on luotu, meidän on varmistettava, että viestintä tietokannan kanssa toimii:



```
# Retrieve the database status
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```



Lopuksi voimme käyttää Metasploitin `db_import`-komentoa tuodaksemme Nmap-skannauksen XML-muodossa:



```
# Import a Nmap XML file into the database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```



Tässä on kaikkien näiden komentojen suorittamisen tulos:



![nmap-image](assets/fr/58.webp)



tuoda Nmap-skannaus XML-muodossa Metasploit-tietokantaan



Täältä näet, että jokainen isäntä on tuotu palveluineen. Nämä tiedot voidaan sitten näyttää komennolla `services` tai `services -p <port>` tietyn palvelun osalta:



![nmap-image](assets/fr/59.webp)



luettelo palveluista, jotka on tuotu XML-tiedostosta Metasploit-tietokantaan



Lopuksi voimme nopeasti ja helposti käyttää näitä tietoja uudelleen moduulissa `-R`-option ansiosta, joka "muuntaa" luettelon palveluista, jotka on saatu syötteenä `RHOSTS`-direktiiville, jota käytetään suoritettavan hyökkäyksen kohteiden määrittämiseen. Tässä on esimerkki `ssh_login`-moduulista, jonka avulla voit suorittaa raa'an hyökkäyksen [SSH]-palveluihin (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/):



![nmap-image](assets/fr/60.webp)



käytä `services -R` -vaihtoehtoa tuodaksesi hyökkäyksen kohteeksi määritetyt palvelut



Tämä on vain pieni esimerkki siitä, mitä Nmapin tiedoilla voidaan tehdä Metasploitissa, mutta se antaa sinulle pienen käsityksen siitä, miten nopeasti ja helposti näitä tietoja voidaan käyttää uudelleen osana tunkeutumistestiä, haavoittuvuusanalyysiä tai verkkohyökkäystä. Kannattaa myös mainita, että Nmapia voi ajaa suoraan Metasploitista ja tuoda tulokset tietokantaan (komento `db_nmap`), mikä on toinen mielenkiintoinen aihe!



### III. Nmapin käyttö Aquatone-verkkoskannerin kanssa



Toinen työkalu, jonka haluan esitellä tässä luvussa Nmapin tulosten uudelleenkäytöstä hyökkäävään tietoturva- ja haavoittuvuusanalyysiin, on Aquatone.



Aquatone on verkkoskanneri, joka on suunniteltu tutkimaan tehokkaasti verkkosovelluksia verkossa. Se tarjoaa kehittyneitä ominaisuuksia verkkopalvelujen löytämiseen, alatoimialueen tunnistamiseen, porttianalyysiin ja verkkosovellusten sormenjälkien määrittämiseen. Kaikki esitetään selkeästi ja ytimekkäästi HTML-, JSON- ja tekstiraportteina, jotta verkkoturva-analyysi on helppoa.



Kuten Metasploit, Aquatone voi käsitellä suoraan Nmapin XML-muotoa ja käyttää sitä skannauksen kohteena. Erityisesti se voi poimia vain kiinnostavat isännät ja palvelut (verkkopalvelut) kaikista Nmap-raportin sisältämistä tiedoista.





- Työkalulinkki: [Github - Michenriksen/aquatone](https://github.com/michenriksen/aquatone)




Jos haluat käyttää Nmapin XML-tulostetta Aquatonen kanssa, lähetä XML-tiedosto yksinkertaisesti putkeen, jota Aquatone käyttää. Tässä on esimerkki:



```
# Send the Nmap XML output to Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```



Kun Aquatone tavallisesti etsii isäntäasemien portteja verkkopalvelujen löytämiseksi, tässä yhteydessä se luottaa ainoastaan Nmapin tuloksiin, sillä Nmap on jo suorittanut tämän toiminnon, mikä säästää aikaa:



![nmap-image](assets/fr/61.webp)



nmapin tulosten käyttäminen XML-muodossa `aquatone`._ avulla



Tässä on ote Aquatonen laatimasta raportista:



![nmap-image](assets/fr/62.webp)



esimerkki akvatonikertomuksesta



Itse käytän Aquatonea usein saadakseni nopean yleiskuvan verkossa olevien verkkosivustojen tyypeistä, erityisesti sen kuvakaappaustoiminnon ansiosta.



Tässäkin tapauksessa täydellinen Nmap-raportti XML-muodossa säästää aikaa ja sitä on helppo käyttää uudelleen toisessa työkalussa.



### IV. Päätelmät



Nämä kaksi esimerkkiä osoittavat selvästi, että Nmapin XML-muoto helpottaa muiden työkalujen käyttöä, koska se on jäsennelty ja helppokäyttöinen dataformaatti. On olemassa monia muita työkaluja, jotka pystyvät käsittelemään näitä tuloksia, kuten automaattiset raportointityökalut, graafiset esitykset tai monimutkaisemmat, omat haavoittuvuusskannerit.



Voit tietysti myös kehittää omia skriptejä ja työkaluja Pythonilla, [PowerShellillä](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/) tai millä tahansa muulla kielellä, jossa on XML-parsing-kirjasto, jolla voit käsitellä ja käyttää Nmapin tulostietoja uudelleen parhaaksi katsomallasi tavalla.



Tässä osassa päädymme Nmapin edistyneempää käyttöä, erityisesti haavoittuvuuksien skannausta NSE-skriptien avulla, käsittelevän opetusmoduulin loppuun.



Ohjeen seuraavassa osassa keskitytään muun muassa joihinkin teknisempiin parhaisiin käytäntöihin ja vinkkeihin, jotka koskevat Nmapin suorittamia erityisiä skannauksia. Tarkastelemme myös skannauksen suorituskyvyn optimointivaihtoehtoja, jotka ovat erityisen hyödyllisiä, kun skannataan suuria verkkoja.




## 11 - Verkkoskannauksen suorituskyvyn parantaminen



### I. Esittely



Tässä luvussa opimme, miten voimme optimoida Nmapilla suoritettavien verkkotarkastusten nopeutta käyttämällä useita erityisiä vaihtoehtoja. Erityisesti opimme lisää Nmapin sisäisestä toiminnasta, aina _timeout_:n hallinnasta työkalun valmiiksi tallennettuihin määrityksiin.



Nyt kun olemme tutustuneet Nmapin ominaisuuksiin, tutustutaanpa petoon ja sen tehoon. Jos olet joskus käyttänyt työkalua suurissa verkoissa, olet luultavasti huomannut, että jotkin skannaukset voivat kestää kauan työkalun tehosta huolimatta. Ja hyvästä syystä: yksinkertainen `nmap`-komento, jossa on muutama vaihtoehto, voi generate:lla miljoonia paketteja, jotka kohdistuvat satoihin tuhansiin mahdollisiin järjestelmiin ja palveluihin.



Lisäksi jotkin verkkolaitteiden kokoonpanot saattavat tarkoituksella käyttää hitaampaa nopeutta (pakettien määrä sekunnissa), jolloin vaarana on pakettien hylkääminen tai IP Address:n kieltäminen turvallisuussyistä.



Asiayhteydestä riippuen voi olla kannattavaa yrittää optimoida kaikki tämä, kuten tässä luvussa nähdään.



Voit joka tapauksessa tarkistaa tarkasteltavien parametrien oletusarvot sekä sen, onko käyttämäsi asetukset otettu oikein huomioon, Nmapin debug-ohjelman avulla (edellisessä luvussa mainittu vaihtoehto `-d`):



![nmap-image](assets/fr/63.webp)



tarkastella ajoitusvaihtoehtoja Nmapin `-d`-vaihtoehdon avulla._



### II. Nmap-skannausten nopeuden hallinta



#### A. Rinnakkaistamisen hallinta



Oletusarvoisesti Nmap käyttää rinnakkaistamista skannauksissaan optimoidakseen ne, ja kaikkia sen käyttämiä parametreja voidaan muuttaa eri vaihtoehtojen avulla. Tapaukset, joissa näitä parametreja on todella tarpeen muuttaa, ovat kuitenkin melko harvinaisia, joten emme käsittele niitä yksityiskohtaisesti tässä ohjeessa:





- `--min-hostgroup/max-hostgroup <size>`: rinnakkaisten isäntäskannausryhmien koko.





- `--min-parallelism/max-parallelism <numprobes>`: koettimien rinnakkaistaminen.





- `--scan-delay/--max-scan-delay <time>`: säätää koettimien välistä viivettä.




Tiedä vain, että niitä on olemassa ja että niitä voidaan käyttää.



#### B. Pakettien määrän hallinta sekunnissa



Oletusarvoisesti Nmap säätää itse lähettämiensä pakettien lukumäärää sekunnissa verkon vasteen mukaan. Tätä asetusta on kuitenkin mahdollista pakottaa määrittelemällä pakettien lukumäärän sekunnissa suurimman ja/tai pienimmän arvon, jota on noudatettava. Tämä asetus tehdään käyttämällä asetuksia `--min-rate <number>` ja `--max-rate <number>`, jossa `number` edustaa pakettien lukumäärää sekunnissa. Esimerkki:



```
# Limit the scan speed to 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300
```



Näiden vaihtoehtojen avulla voit säätää skannausnopeutta omien tarpeidesi mukaan joko nopeuttaaksesi prosessia tai rajoittaaksesi käytettävää kaistanleveyttä. Jälkimmäinen tapaus (skannausnopeuden rajoittaminen) on se, joka todennäköisesti johtaa sinut näihin vaihtoehtoihin, varsinkin jos sinulla on verkkoviiveitä Nmapia käyttäessäsi (mikä on melko harvinaista).



### III. Yhteyshäiriöiden ja aikakatkaisujen hallinta



Toinen parametri, jonka avulla voimme optimoida Nmap-skannausten nopeutta (tai taata suuremman tarkkuuden), koskee _timeout_- ja _retry_-parametreja.



_timeouts_-kohdassa tämä on **ei vastausta -aikaraja**, jonka jälkeen Nmap lopettaa vastauksen odottamisen ja katsoo, että palvelua tai isäntäkohtaa ei ole saavutettavissa. Jos kyseessä on _retry_, tämä on **peräkkäisten operaatioyritysten määrä**, jonka Nmap suorittaa ennen kuin se jatkaa.



Rinnakkaistamisen tapaan _timeout_- ja _retry_-hallintaa voidaan soveltaa isännän tai palvelun löytämisvaiheisiin:





- `--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>`: määrittää Exchange:n kiertoaika. Tämäkin parametri lasketaan ja mukautetaan lennossa skannauksen aikana. On epätodennäköistä, että sinun tarvitsee käyttää sitä, koska Nmap laskee tämän ajan lennossa verkon reaktion mukaan.





- `--max-retries <number>`: rajoittaa paketin uudelleenlähetysten määrää porttiskannauksen aikana. Oletusarvoisesti Nmap voi tehdä jopa 10 uudelleenkäsittelyä yhdelle palvelulle, varsinkin jos se havaitsee viiveitä tai häviöitä verkkotasolla, mutta useimmissa tapauksissa tehdään vain yksi uudelleenkäsittely.





- `--host-timeout <time>`: määrittää enimmäisajan, jonka Nmap viettää isännällä kaikkien toimintojensa aikana, mukaan lukien porttien skannaus, palveluiden havaitseminen ja kaikki muut isäntään liittyvät toiminnot. Jos tämä aikaväli ylittyy ilman vastausta tai **toimintojen loppuunsaattamista**, Nmap hylkää kyseisen isännän näyttämättä mitään sitä koskevia tuloksia ja siirtyy seuraavaan isäntään luettelossaan. Näin voit hallita enimmäisaikaa, jonka Nmap käyttää tiettyyn isäntäkoneeseen, välttää jumittumisen vastahakoisille isännille ja optimoida skannauksen kokonaisajan.




Käytän päivittäisessä työssäni `--max-retries`- ja `--host-timeout`-asetuksia optimoidakseni skannaukseni:



```
# Optimization of a scan with 0 additional attempts and a timeout of 15 minutes per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```



Nämä parametrit tarjoavat lisäjoustavuutta skannauksen käyttäytymisen mukauttamiseksi erityistarpeisiin ja verkko-olosuhteisiin. Sinun on kuitenkin oltava tietoinen niiden vaikutuksista skannattavien isäntien kuormitukseen ja mahdolliseen tarkkuuden heikkenemiseen.



### IV. Valmisteltujen kokoonpanojen käyttö



Tässä luvussa esiteltyjä eri vaihtoehtoja voidaan käyttää erikseen tai osana Nmapin tarjoamia valmiita kokoonpanoja. Valinta, joka mahdollistaa näiden _templates_ (konfiguraatiomallien) käytön, on `-T <numero>` tai `-T <nimi>`. Käytettävissä on 5 _templates_-tasoa:



```
-T<0-5>: Set timing template (higher is faster)
```



Oletusarvoisesti Nmap käyttää _template_ 3 (_normal_), joka on yleensä riittävä.



Itse toimin yleensä tilanteissa, joissa minun on oltava melko nopea (ja samalla mahdollisimman täydellinen), ja käytän usein `-T4`-vaihtoehtoa.



```
# Use Nmap for a network scan with preset T4 (with debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```



Tämän tarkistuksen vianmääritystiedot osoittavat seuraavaa:



![nmap-image](assets/fr/64.webp)



`-T4`-asetusten käyttö Nmap-skannauksen aikana



### V. Päätelmät



Tässä luvussa olemme tarkastelleet erilaisia tekniikoita ja vaihtoehtoja, joilla voit hallita Nmapin tehoa, aggressiivisuutta ja suorituskykyä. Nämä vaihtoehdot ovat erityisen hyödyllisiä, kun skannataan suuria verkkoja ja harvemmin salakuvaustarkoituksessa.



Seuraavassa luvussa tarkastelemme muutamia parhaita käytäntöjä Nmapin käyttöön ja sen turvallisuuden varmistamiseen.




## 12 - Tietoturva ja luottamuksellisuus Nmapia käytettäessä



### I. Esittely



Tässä luvussa tarkastelemme eräitä hyviä käytäntöjä, joita on noudatettava Nmapin tuottamien, käsittelemien ja tallentamien tietojen turvallisuuden ja ennen kaikkea luottamuksellisuuden osalta.



Nmapin käyttö tietojärjestelmässä voidaan nopeasti luokitella hyökkäykseksi. Tämän vuoksi on toteutettava useita varotoimia, jotta voidaan toimia oikeudellisissa puitteissa ja samalla taata aiottujen kohteiden, kerättyjen tietojen ja skannauksessa käytettävän järjestelmän turvallisuus.



### II. Asianmukaisten lupien hankkiminen



Varmista ennen verkon tai järjestelmän skannausta, että sinulla on asianmukaiset valtuutukset. Järjestelmien skannaaminen haavoittuvuuksien varalta (NSE-skriptit) ilman lupaa voi olla laitonta, ja sillä voi olla oikeudellisia seurauksia, varsinkin jos tietojärjestelmien turvallisuus ei kuulu viralliseen toimenkuvaasi.





- Muistutuksena: [Rikoslaki: III luku: Hyökkäykset automaattisia tietojenkäsittelyjärjestelmiä vastaan](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




### III. Arkaluonteisten tietojen suojaaminen



Nmapin tuottamia tuloksia voidaan pitää arkaluonteisina erityisesti silloin, kun ne sisältävät tietoa tietojärjestelmän heikkouksista, joita hyökkääjä voi hyödyntää. Mutta myös silloin, kun ne koskevat järjestelmiä, jotka eivät ole kaikkien saatavilla (esim. arkaluonteiset, teolliset, terveydenhuollon tai [varmuuskopiointi]tietojärjestelmät (https://www.it-connect.fr/cours-tutoriels/administration-systemes/autres/sauvegarde/)).



Olemme myös nähneet, että käytetyistä NSE-skripteistä riippuen [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) NSE-skannaustulokset voivat sisältää myös tunnisteita.



Näin ollen pahantahtoinen henkilö, joka pääsee käsiksi näihin skannaustuloksiin, saa käyttöönsä tietojärjestelmän kartan ja runsaasti teknistä tietoa ilman, että hän on itse suorittanut näitä toimia, ja on vaarassa tulla havaituksi.



Siksi on tärkeää huolehtia siitä, ettei Nmapia käytettäessä kerätä tai tallenneta epäasianmukaisesti arkaluonteisia tietoja, mukaan lukien, mutta ei rajoittuen seuraaviin:





- Lähtötietojen salaaminen: Jos sinun on tallennettava tai lähetettävä Nmap-skannausten tulokset, muista salata ne tietojen luottamuksellisuuden suojaamiseksi. Tämä estää arkaluonteisten tietojen luvattoman sieppaamisen. Ihannetapauksessa tiedot olisi salattava heti, kun ne poistuvat skannauksen suorittamiseen käytetystä järjestelmästä (vahvalla salasanalla salattu ZIP-arkisto on erittäin hyvä alku).





- Aseta pääsynvalvonta: varmista, että vain valtuutetuilla henkilöillä on pääsy Nmap-skannausten tuloksiin, joihin ne tallennetaan. Aseta asianmukaiset käyttöoikeuksien valvontatoimet, jotta arkaluonteiset tiedot voidaan suojata luvattomalta käytöltä.





- Valppaus tietojen käsittelyssä: Kun siirrät, kopioit tai käsittelet skannattuja tietoja, varmista, että pidät tietoturvan tiukasti hallinnassa. Tämä tarkoittaa seuraavaa: älä jätä niitä lojumaan Internetiin liitetyn työaseman `Download`-hakemistoon, älä anna niiden kulkea sisäisen HTTP-tiedoston Exchange-sovelluksen kautta, älä jätä Notepadia auki lukitsematta työasemaa lounastauon aikana jne.




### IV. Aggressiivisten skannausten hallinta



Kuten olemme nähneet tämän oppikirjan aikana, Nmap voi olla hyvin yksityiskohtainen verkkotasolla. Se voi myös lähettää paketteja, jotka eivät ole oikein muotoiltuja ja jotka eivät noudata tiukasti sen tuottamien verkkokehysten ja -pakettien protokollarakennetta. Kaikki nämä toimet voivat vaikuttaa tiettyihin järjestelmiin ja palveluihin, joskus jopa niin paljon, että ne aiheuttavat toimintahäiriöitä tai järjestelmän ja verkon resurssien kyllästymistä.



Välttääksesi vaaratilanteet sinun on hallittava Nmapin käyttäytyminen ja osattava mukauttaa se käyttökontekstiinsa tässä oppaassa käsiteltyjen eri vaihtoehtojen avulla. Nmapia ei välttämättä käytetä samalla tavalla teollisuus [laitteistoa](https://www.it-connect.fr/actualites/actu-materiel/) sisältävässä tietojärjestelmässä kuin paikallisella palomuurilla suojatuista Windows-järjestelmistä koostuvassa käyttäjäverkossa tai verkon ytimessä.



Toivottavasti tämän oppikirjan eri oppitunnit ovat opettaneet sinua hallitsemaan ja analysoimaan Nmapin käyttäytymistä, mutta paras tapa oppia on tekemällä. Varmista siis, että tunnet käyttämäsi Nmapin vaihtoehdot.



### V. Skannausjärjestelmän suojaaminen



Ensimmäisessä luvussa näimme, että useimmissa tapauksissa Nmapia on käytettävä `root`- tai paikallisena järjestelmänvalvojana. Tämä johtuu siitä, että se suorittaa verkko-operaatioita, joskus melko matalalla tasolla, verkkokirjastojen avulla, jotka vaativat korkeat ja riskialttiit käyttöoikeudet järjestelmän vakauden tai muiden sovellusten luottamuksellisuuden kannalta.



Tämän vuoksi Nmapia voidaan pitää sen järjestelmän herkkänä komponenttina, johon se on asennettu. Varmista, että käytät Nmapin uusinta versiota, sillä vanhemmat versiot saattavat sisältää tunnettuja tietoturva-aukkoja. Käyttämällä ajantasaista versiota voit minimoida työkalun käyttöön liittyvät riskit.



Jos olet päättänyt käyttää Nmapia ei istunnon kautta `root`-käyttäjänä, vaan antamalla tietyt oikeudet etuoikeutetulle käyttäjälle niin, että hänellä on kaikki, mitä hän tarvitsee Nmapin käyttöön (`sudo` tai _capabilities_), ota huomioon, että Nmapia voidaan käyttää osana täydellistä etuoikeuksien korottamista:



![nmap-image](assets/fr/65.webp)



nmap-oikeuksien lisääminen `sudo`:n kautta._



Tässä käytän Nmap-komentoa `sudo`:n kautta, mutta tämä antaa minulle mahdollisuuden käyttää interaktiivista komentotulkkia `root`-käyttäjänä, mikä ei ollut alkuperäinen tavoite.



Nmapin asentaminen järjestelmiin, joita ei ole suunniteltu suorittamaan verkkotarkistuksia, on myös erittäin suositeltavaa. Tarkoitan erityisesti palvelimia tai työasemia. Toisaalta tämä lisäisi potentiaalisen vektorin etuoikeuksien korottamiseen, mutta ennen kaikkea se antaisi hyökkääjälle vaivattoman pääsyn hyökkäystyökaluun.



Lopuksi on varmistettava laajemmin skannaukseen käytettävän järjestelmän turvallisuus, jotta siitä ei itsestään tulisi tunkeutumisen tai tietovuodon välikappaletta. Järjestelmänvalvojana on parempi käyttää oman työaseman sijasta omaa järjestelmää, mieluiten rajoitetun käyttöiän omaavaa järjestelmää.



### VI. Päätelmät



Varmista siis, että hallitset Nmapin kunnolla, ennen kuin käytät sitä tosielämässä tai tuotanto-olosuhteissa, ja ole valppaana, kun käsittelet ja hallitset sen tuloksia. Olisi sääli aiheuttaa vahinkoa, vuotaa tietoja tai helpottaa kompromisseja, kun alkuperäisen lähestymistavan tarkoituksena on parantaa yrityksesi tietoturvaa.



## 13 - Porttiskannaukset TCP:n kautta: SYN, Connect ja FIN



### I. Esittely



Tässä ja seuraavassa luvussa tarkastelemme tarkemmin Nmapin käytettävissä olevia TCP-skannaustyyppejä, alkaen yleisimmin käytetyistä: SYN-, Connect- ja FIN-skannaukset.



Kuten olet ehkä huomannut, Nmap tarjoaa useita vaihtoehtoja TCP-skannauksia varten:



![nmap-image](assets/fr/66.webp)



nmap._:n käytettävissä olevat skannaustekniikat



Tässä on tarkoitus selittää joitakin näistä menetelmistä, jotta ymmärtäisit niiden erot, edut ja rajoitukset. Tulet huomaamaan, että riippuen asiayhteydestä tai siitä, mitä haluat tietää, on parempi valita jompikumpi vaihtoehto.



### II. TCP SYN-skannaus tai "Half Open -skannaus"



Ensimmäinen tarkastelemamme TCP-skannaustyyppi on "TCP SYN Scan", joka tunnetaan myös nimellä "Half Open Scan". Jos muistat ensimmäisten porttiskannausten jälkeen tekemämme verkkoskannaukset, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) käyttää oletusarvoisesti tätä skannaustyyppiä, kun se suoritetaan pääkäyttäjän oikeuksin.



Käännös auttaa sinua ymmärtämään, miten tämä skannaus toimii. Itse asiassa TCP SYN -tarkistus lähettää TCP SYN -paketin kuhunkin kohteena olevaan porttiin, joka on ensimmäinen paketti, jonka asiakas (joka pyytää yhteyden muodostamista) lähettää osana kuuluisaa _Three way handshake_ TCP:tä. Tavallisesti, jos portti on auki kohdepalvelimella ja sen takana on käynnissä palvelu, palvelin lähettää takaisin TCP SYN/ACK-paketin validoidakseen asiakkaan SYN:n ja aloittaakseen TCP-yhteyden. Vastaus on TCP-paketti, jonka SYN- ja ACK-lipukkeet on asetettu arvoon 1. Näin voimme varmistaa, että portti on auki ja johtaa palveluun.



Toisaalta, jos portti on suljettu, palvelin lähettää meille `TCP`-paketin, jonka RST- ja ACK-lipukkeet on asetettu arvoon 1 ja joka lopettaa yhteyspyynnön, joten tiedämme, että mikään palvelu ei näytä olevan aktiivinen tämän portin takana:



![nmap-image](assets/fr/67.webp)



tCP SYN Scan -käyttäytymiskaavio avoimille ja suljetuille porteille



Saadakseni konkreettisemman käsityksen `TCP SYN Scan` -toiminnosta suoritin TCP/80-portin skannauksen isäntäkoneelle, jolla oli aktiivinen verkkopalvelin kyseisessä portissa. Wiresharkilla suoritettu verkkoskannaus näyttää seuraavan virtauksen (skannauslähde: `10.10.14.84`):



![nmap-image](assets/fr/68.webp)



verkkokaappaus avoimen portin TCP SYN-skannauksen aikana



Ensimmäisellä rivillä näemme, että skannauksen lähde lähettää TCP-paketin isännälle `10.10.10.203` porttiin TCP/80. Tässä TCP-paketissa SYN-lippu on asetettu arvoon 1 osoittaakseen, että kyseessä on TCP-yhteyden alustuspyyntö.



Toisella rivillä näemme, että kohde vastaa `TCP SYN/ACK` -viestillä, mikä tarkoittaa, että se hyväksyy yhteyden muodostamisen ja siten TCP/80-portin virtojen vastaanottamisen. Voimme siis päätellä, että portti TCP/80 on auki ja että skannatussa palvelimessa on verkkopalvelin.



Tämän jälkeen isäntä lähettää takaisin RST-paketin yhteyden sulkemiseksi, jolloin skannattava isäntä ei voi pitää TCP-yhteyttä auki odottamassa vastausta. Jos skannaus kohdistuu moniin portteihin, TCP-yhteyksien sulkematta jättäminen voi johtaa palvelunestoon, koska palvelin voi ylläpitää vastausta odottavien yhteyksien määrän ylikuormittumisen vuoksi (ks. [Wikipedia - Syn flood](https://fr.wikipedia.org/wiki/SYN_flood))



Wiresharkissa voit nähdä TCP-lippujen tilan jokaisen suorittamamme testin osalta. Tämä näyttää, onko paketti SYN-, SYN/ACK-, ACK- jne. paketti:



![nmap-image](assets/fr/69.webp)



tarkastella paketin TCP-lippuja Wiresharkissa (TCP SYN tässä)



Toisaalta suoritin saman testin näiden kahden koneen välillä, mutta tällä kertaa skannasin TCP/81-porttia, jossa mikään palvelu ei ole aktiivinen (skannauslähde: `10.10.14.84`):



![nmap-image](assets/fr/70.webp)



verkkokaappaus suljetun portin TCP SYN-skannauksen aikana



Tutkittava isäntä palauttaa `TCP RST/ACK` vastauksena `TCP SYN` -viestiini, kun portti ei ole auki.



Kuten mainittu, kun Nmapia käytetään etuoikeutetusta päätelaitteesta, TCP SYN Scan on oletustila, ja sen voi pakottaa valitsemalla `-sS` (`scan SYN`):



```
# Execution of a TCP Syn Scan_
nmap -sS 192.168.1.15
```




TCP-SYN-tarkistus on nopeuden vuoksi yleisimmin käytetty tarkistus. Toisaalta asiakkaan epäonnistuminen _Three Way Handshake_:n loppuun saattamisessa (eli ACK:n lähettämättä jättäminen palvelimen SYN/ACK:n jälkeen) voi vaikuttaa epäilyttävältä, jos se havaitaan liian monta kertaa palvelimella tai samasta lähteestä verkossa. Asiakkaan normaali käyttäytyminen TCP SYN/ACK-paketin vastaanottamisen jälkeen vastauksena TCP SYN-pakettiin on nimittäin se, että se lähettää "kuittauksen" (ACK) ja aloittaa sitten Exchange:n. Tämän jälkeen asiakas lähettää TCP SYN-paketin.



Se tarjoaa kuitenkin hieman nopeamman skannauksen, koska se ei vaivaudu lähettämään ACK-viestiä jokaisesta positiivisesta vastauksesta. SYN-skannauksen etuna on sen nopeus, koska vain yksi paketti lähetetään jokaista skannattavaa porttia kohti, mutta sen kustannuksella havaitsemisen mahdollisuus on suurempi.



Lisäksi TCP SYN -tarkistus pystyy havaitsemaan, onko portti suodatettu (suojattu) palomuurilla. Itse asiassa kohde-isännän edessä oleva palomuuri voidaan havaita siitä, miten se käyttäytyy, kun se vastaanottaa TCP SYN -paketin porttiin, jonka sen on tarkoitus suojata. Se ei yksinkertaisesti vastaa. Kuten olemme kuitenkin nähneet, molemmissa tapauksissa (avoin tai suljettu portti) isäntä vastaa. Tämä kolmas käyttäytyminen paljastaa, että skannattavan isäntäkoneen ja skannauksen suorittavan koneen välillä on palomuuri. Tässä on tulos, jonka Nmap voi palauttaa, kun skannattu portti on palomuurin suodattama:



![nmap-image](assets/fr/71.webp)



nmap-näyttö suodatetun portin skannauksen yhteydessä



Kun suoritamme verkon kaappauksen skannauksen aikana, voimme itse asiassa nähdä, että mitään vastausta ei anneta:



![nmap-image](assets/fr/72.webp)



verkkokaappaus palomuurin suodattaman portin TCP SYN-skannauksen aikana



Suljetun portin ja suodatetun portin ero on seuraava: suodatettu portti on portti, joka on suojattu palomuurilla, kun taas suljettu portti on portti, jossa ei ole käynnissä mitään palvelua ja joka ei näin ollen pysty käsittelemään TCP-pakettejamme. Jotkin TCP-skannaustyypit, kuten TCP SYN-skannaus, pystyvät havaitsemaan, onko portti suodatettu, kun taas toiset skannaustyypit eivät pysty siihen.



### III. TCP Connect -skannaus tai Full Open -skannaus



Toinen TCP-skannaustyyppi on TCP Connect -skannaus, joka tunnetaan myös nimellä _Full Open Scan_. Se toimii samalla tavalla kuin TCP SYN-skannaus, mutta tällä kertaa se palauttaa `TCP ACK` -vastauksen palvelimen positiivisen vastauksen (SYN/ACK) jälkeen. Tämän vuoksi sitä kutsutaan `Full Open`, koska yhteys avataan kokonaan ja käynnistetään jokaiseen skannauksen aikana avattuun porttiin, jolloin noudatetaan TCP:n _Three Way Handshake_ -kättelyä:



![nmap-image](assets/fr/73.webp)



tCP Connect Scan -käyttäytymiskaavio avoimille ja suljetuille porteille



Seuraavassa näkyy, mitä verkon kautta kulkee avoimen portin kohdalla suoritetun TCP Connect -skannauksen aikana:



![nmap-image](assets/fr/74.webp)



verkon nuuskiminen TCP Connect -skannauksen aikana avoimen portin löytämiseksi



Näemme, että ensimmäinen lähetetty TCP-paketti on asiakkaan lähettämä `TCP SYN`, ja palvelin vastaa siihen `TCP SYN/ACK`, mikä osoittaa, että portti on avoinna ja että siellä on aktiivinen palvelu. Simuloidakseen laillista asiakasta koko matkan Nmap lähettää sitten `TCP ACK` -paketin takaisin palvelimelle. Päinvastoin, kun skannataan suljettua porttia:



![nmap-image](assets/fr/75.webp)



verkkokaappaus suljetun portin TCP Connect -skannauksen aikana



Huomaa, että palvelimen vastaus `SYN`-pakettiimme on jälleen kerran `TCP RST/ACK`-paketti, joten voimme päätellä, että portti on suljettu eikä siinä ole käynnissä mitään palveluja.



Nmapia käytettäessä TCP Connect Scan -skannauksen suorittamiseen käytetään `-sT` (`scan Connect`) -vaihtoehtoa. Huomaa, että kun Nmapia käytetään etuoikeudettomasta istunnosta, tämä on TCP-skannauksen oletustila:



```
# Execution of a TCP Connect Scan
nmap -sT 192.168.1.15
```



`TCP Connect Scan` simuloi laillisempaa yhteyspyyntöä, jonka käyttäytyminen muistuttaa eniten lambda-asiakkaan käyttäytymistä, joten on vaikeampi havaita skannausta pienemmällä määrällä portteja. Se on kuitenkin hitaampi, koska se alustaa kokonaan jokaisen TCP-yhteyden skannattavan koneen avoimissa porteissa.



10 000 portin Nmap-skannaus on silti helposti havaittavissa, jos verkon tunkeutumisen havaitsemis- ja suojauspalvelut (IDS, IPS, EDR) on asennettu. Kun hyökkääjä haluaa pitää matalaa profiilia, hän keskittyy yleensä pieneen määrään strategisesti valittuja portteja, kuten 445 (SMB) tai 80 (HTTP), jotka ovat usein auki palvelimissa ja joissa on yleisiä haavoittuvuuksia.



Koska TCP Connect Scan odottaa vastausta molemmissa tapauksissa, se voi myös havaita palomuurin, joka saattaa suodattaa kohdeisännän portteja.



### IV. TCP FIN -skannaus tai "Stealth Scan



TCP FIN Scan, joka tunnetaan myös nimellä _Stealth Scan_, käyttää TCP-yhteyden päättävän asiakkaan käyttäytymistä avoimen portin havaitsemiseen.



TCP:ssä istunnon päättyminen tarkoittaa TCP-paketin lähettämistä, jossa FIN-lippu on asetettu arvoon 1. Tavallisessa Exchange:ssä palvelin lopettaa kaiken viestinnän asiakkaan kanssa (ei vastausta). Jos palvelimella ei ole aktiivista TCP-yhteyttä asiakkaaseen, se lähettää `RST/ACK`. Voimme siis erottaa avoimet ja suljetut portit toisistaan lähettämällä `TCP FIN` -paketteja tiettyihin portteihin:



![nmap-image](assets/fr/76.webp)



tCP FIN-skannauksen käyttäytymiskaavio avoimille ja suljetuille porteille



Kuvasin jälleen verkon _Stealth-skannauksen_ aikana, ja tämä näkyy, kun skannattu portti on auki:



![nmap-image](assets/fr/77.webp)



verkkokaappaus TCP FIN-skannauksen aikana avoimen portin löytämiseksi



Näemme, että asiakas lähettää yhden tai kaksi pakettia lopettaakseen TCP-yhteyden ja että palvelin ei vastaa. Se vain hyväksyy yhteyden päättymisen ja lopettaa yhteydenpidon.



Seuraavanlainen kuva näkyy nyt, kun skannataan suljettua porttia:



![nmap-image](assets/fr/78.webp)



verkkokaappaus suljetun portin TCP FIN-skannauksen aikana



Näemme, että palvelin lähettää takaisin `TCP RST/ACK` -paketin, joten avoimen ja suljetun portin käyttäytymisessä on eroa, ja voimme luetella palvelimen avoimet portit lähettämällä TCP FIN -paketin. Nmapia käytettäessä TCP FIN -skannauksen suorittamiseen käytetään `-sF` (`scan FIN`) -vaihtoehtoa:



```
# Execution of a TCP Fin Scan
nmap -sF 192.168.1.15
```



TCP FIN Scan ei toimi Windows-isäntäkoneissa, koska käyttöjärjestelmällä on taipumus sivuuttaa TCP FIN -paketit, kun ne lähetetään portteihin, jotka eivät ole avoinna. Jos siis suoritat TCP FIN Scan -tarkistuksen Windows-isännällä, saat sen vaikutelman, että kaikki portit ovat suljettuja.



Siksi on tärkeää tuntea useita skannausmenetelmiä ja ymmärtää niiden väliset erot.



Koska TCP FIN ei kummassakaan tapauksessa odota vastausta, se ei pysty havaitsemaan, että kohdeisäntäkoneen ja skannauksen lähteen välillä on palomuuri.



Tässä on esimerkki Nmapin TCP FIN -skannaustuloksesta:



![nmap-image](assets/fr/79.webp)



nmapin tekemän TCP FIN-skannauksen tulokset._



Itse asiassa se, että isäntä ei vastaa tiettyyn porttiin, voi tarkoittaa, että portti on suodatettu, mutta myös sitä, että se on auki ja aktiivinen.



Tätä skannausta kutsutaan "stealth"-skannaukseksi, koska se ei aiheuta generate-liikennettä eikä yleensä aiheuta kirjautumista kohteena olevissa järjestelmissä. Sitä voidaan käyttää verkon porttien huomaamattomaan selvittämiseen ilman hälytyksiä. Kuten edellä mainittiin, sen tehokkuus voi kuitenkin vaihdella kohdejärjestelmästä riippuen, samoin kuin sen harkinnanvaraisuus riippuen tietoturvalaitteiden kokoonpanosta.



### V. Päätelmät



Se siitä ensimmäisestä kahdesta luvusta, jotka käsittelevät Nmapin tarjoamia eri TCP-skannaustyyppejä! Seuraavassa luvussa tarkastelemme XMAS-, Null- ja ACK-TCP-skannaustyyppejä, jotka toimivat eri tavoin havaitessaan isännän avoimia portteja.





## 14 - Porttiskannaukset TCP:n kautta: XMAS, Null ja ACK



### I. Esittely



Tässä osassa jatkamme Nmapin tarjoamien TCP-skannausmenetelmien tutkimista. Tässä tarkastelemme `XMAS`-, `Null`- ja `ACK`-menetelmiä, jotka käyttävät TCP-ominaisuuksia saadakseen tietoa tietyn kohteen avoimista porteista ja palveluista.



### II. TCP-XMAS-skannaus



XMAS Scan TCP on hieman epätavallinen siinä mielessä, että se ei simuloi lainkaan käyttäjän tai koneen normaalia käyttäytymistä verkossa. Itse asiassa XMAS Scan lähettää TCP-paketteja, joiden lippujen `URG` (Urgent), `PSH` (Push) ja `FIN` (Finish) arvoksi on asetettu 1, ohittaakseen tietyt palomuurit tai suodatusmekanismit.



Nimi XMAS tulee siitä, että näiden lippujen näkeminen on epätavallista. Kun kaikki kolme lippua asetetaan samanaikaisesti TCP-paketissa, se näyttää valaistulta joulukuuselta:



![nmap-image](assets/fr/80.webp)



xMAS-skannauksessa käytettävät tCP-lipukkeet



Menemättä tässä yksityiskohtaisesti näiden lippujen rooliin, on tärkeää tietää, että kun lähetät paketin, jossa nämä kolme lippua ovat käytössä, kohdeportin takana oleva aktiivinen palvelu ei palauta yhtään pakettia. Toisaalta, jos portti on suljettu, saamme TCP RST/ACK -paketin. Pystymme nyt erottamaan avoimen ja suljetun portin käyttäytymisen, kun listaamme koneen portteja:



![nmap-image](assets/fr/81.webp)



tCP XMAS Scan -käyttäytymiskaavio avoimille ja suljetuille porteille



Samaa logiikkaa noudattaen verkkotarkistus portissa TCP/80 isännässä, jossa on aktiivinen verkkopalvelin, näyttää seuraavan käyttäytymisen havaitessaan avoimen portin (skannauslähde `10.10.14.84`):



![nmap-image](assets/fr/82.webp)



verkkokaappaus TCP XMAS-skannauksen aikana avoimen portin löytämiseksi



Näemme, että skannauksen lähde lähettää kaksi TCP-XMAS-pakettia (joiden lippujen `FIN`, `PSH` ja `URG` arvoksi on asetettu 1) isännälle `10.10.10.203` ja että kohde ei vastaa, mikä osoittaa, että portti on auki. Sitä vastoin, kun suoritetaan `TCP XMAS Scan` suljetulle portille, havaitaan seuraava tulos:



![nmap-image](assets/fr/83.webp)



verkkokaappaus suljetun portin TCP XMAS-skannauksen aikana



Vastaus TCP-pakettiimme on tällöin `TCP RST/ACK`, joka osoittaa, että portti on suljettu. Voit käyttää tätä tekniikkaa Nmapin kanssa `-sX` (`scan XMAS`) -valinnalla voit suorittaa TCP XMAS -skannauksen:



```bash
# Execution of a TCP XMAS Scan
nmap -sX 192.168.1.15
```



On tärkeää huomata, että TCP XMAS -skannaus ei pysty havaitsemaan palomuureja, jotka voivat olla kohteen ja skannattavan koneen välissä, toisin kuin jotkut muut skannaustyypit, kuten TCP SYN tai Connect. Kahden isäntäkoneen välissä oleva aktiivinen palomuuri varmistaa, että TCP-palautusta ei tehdä, jos kohteena oleva portti on suodatettu (eli palomuuri suojaa sen). Jos vastausta ei tule, on mahdotonta tietää, onko portti palomuurin suojaama vai avoin ja aktiivinen. On myös syytä huomioida, että TCP FIN -tarkastuksen tavoin tietyt sovellukset tai käyttöjärjestelmät, kuten Windows, voivat vääristää tämäntyyppisen tarkastuksen tuloksia.



huomautus: tuki XMAS/FIN/NULL-skannauksille uusimmissa Windows-versioissa on edelleen rajallinen, ja tulokset voivat olla epäjohdonmukaisia tämäntyyppisissä kohteissa. (Päivitys 2025)_



### III. TCP-nollatarkistus



Toisin kuin TCP XMAS -skannaus, TCP Null -skannaus lähettää TCP-skannauspaketteja, joissa kaikki liput on asetettu 0:ksi. Tämäkin on käyttäytymistä, jota ei koskaan esiinny koneiden välisessä tavallisessa Exchange:ssä, sillä TCP-paketin lähettämistä ilman lippua ei ole määritelty TCP-protokollaa kuvaavassa RFC:ssä. Siksi se voidaan havaita helpommin.



Kuten TCP XMAS -tarkistus, tämäkin tarkistus voi häiritä tiettyjä palomuureja tai suodatusmoduuleja, jolloin paketit pääsevät läpi:



![nmap-image](assets/fr/84.webp)



tCP Null Scan -käyttäytymiskaavio avoimille ja suljetuille porteille



Seuraavassa on, mitä verkossa näkyy TCP-nollatarkistuksen aikana avoimessa portissa:



![nmap-image](assets/fr/85.webp)



verkkokaappaus avoimen portin TCP-nollatarkistuksen aikana



Skannauslaite lähettää liputtoman paketin (`[<None>]` Wiresharkissa) ilman palvelimen vastausta. Sitä vastoin, kun kohdeportti on suljettu:



![nmap-image](assets/fr/86.webp)



verkkokaappaus suljetun portin TCP-nollatarkistuksen aikana



Jos haluat suorittaa TCP-nollatarkistuksen Nmapilla, käytä yksinkertaisesti `-sN` (`scan Null`) -vaihtoehtoa:



```bash
# Execution of a TCP Null Scan
nmap -sN 192.168.1.15
```



Koska vastaus portin ollessa auki ja palomuurin ollessa aktiivinen (ei palautetta palvelimelta kummassakaan tapauksessa) on identtinen, TCP Null -skannaus ei pysty havaitsemaan palomuurin läsnäoloa. Lisäksi palomuuri voi jopa väärentää tuloksen antamalla ymmärtää, että portti on auki, koska se ei vastaa TCP-paketteihin, joissa ei ole lippuja, vaikka portti on suodatettu. Tämä on tärkeää tiedostaa, kun käytetään skannauksia, jotka eivät pysty erottamaan avointa ja suodatettua (palomuurilla suojattua) porttia toisistaan, kuten `TCP Null`-, `XMAS`- tai `FIN`-skannauksia, jotta saatujen tulosten tulkinta olisi johdonmukaista.



### IV. TCP ACK-skannaus



TCP ACK -skannausta käytetään havaitsemaan palomuurin olemassaolo kohdeisännässä tai kohdeisännän ja skannauksen lähteen välillä.



Toisin kuin muut skannaukset, TCP ACK -skannaus ei yritä tunnistaa, mitkä portit ovat auki isännällä, vaan pikemminkin sen, onko suodatusjärjestelmä aktiivinen, ja vastaa jokaisen portin kohdalla "suodatettu" tai "suodattamaton". Jotkin TCP-skannaukset, kuten `TCP SYN` tai `TCP Connect`, pystyvät tekemään molempia samanaikaisesti, kun taas toiset, kuten `TCP FIN` tai `TCP XMAS`, eivät pysty määrittämään suodatuksen olemassaoloa lainkaan. Tämän vuoksi TCP ACK -skannaus voi olla hyödyllinen:



![nmap-image](assets/fr/87.webp)



tCP ACK Scan -käyttäytymiskaavio suodatetuille ja suodattamattomille porteille



Käytämme Nmapin `-sA`-vaihtoehtoa tämän tyyppisen skannauksen suorittamiseen. Tässä on TCP ACK -skannauksen tulos, jos portti on suodatettu eli estetty ja suojattu palomuurilla:



![nmap-image](assets/fr/88.webp)



nmap-näyttö TCP ACK Scan._ aikana



Esimerkkitulos isännälle, jossa on palomuuri, ja isännälle, jossa ei ole palomuuria. Nmap palauttaa `filtered` isännän `10.10.10.203` porteissa TCP/80 ja TCP/81. Wiresharkilla suoritetussa verkkoanalyysissä käyttäytyminen on seuraava:



![nmap-image](assets/fr/89.webp)



verkkokaappaus TCP ACK-skannauksen aikana porttiin, jota palomuuri ei ole suodattanut



Kohdekone ei palauta mitään, jos käytössä on palomuuri.



Voit käynnistää tämän skannauksen Nmapilla käyttämällä `-sA` (`scan ACK`) -vaihtoehtoa:



```bash
# Execution of a TCP ACK Scan
nmap -sA 192.168.1.15
```



### V. Päätelmät



Olemme tarkastelleet kolmea erilaista TCP-skannausmenetelmää jo esiteltyjen menetelmien lisäksi. Näitä eri menetelmiä on tarkoitus käyttää hyvin erityisissä olosuhteissa ja yhteyksissä, erityisesti tunkeutumistestien tai Red Team -operaatioiden yhteydessä, joissa on kyse harkinnanvaraisuudesta.



## 15 - Nmap CheatSheet - Yhteenveto opetusohjelman komennoista



### I. Esittely



Tässä on lyhyt yhteenveto Nmapin monista komennoista ja käyttötapauksista, jotta löydät ne nopeasti ja voit käyttää niitä uudelleen jokapäiväisessä käytössä.



### II. Nmap: Nmap: CheatSheet IT-Connect



Tässä on esiteltyjen komentojen muistilista. Tämän sivun avulla on helppo löytää Nmapin yleisimmät käyttökohteet.





- Sataman skannaus




```bash
# Display installed Nmap version
nmap --version

# Scan for open specific ports on a single IP address
nmap --open -p 80 192.168.1.18

# Scan TCP ports on a selection of ports
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan UDP services on an IP address
nmap -sU 192.168.1.19

# Scan UDP services on specific ports
nmap -sU 192.168.1.19 -p 161,23

# Scan the 100 most commonly used TCP ports
nmap 192.168.1.19 --top-ports 100

# Scan all ports on an IP address
nmap 192.168.1.19 -p-

# Scan multiple subnets with specific ports
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan a subnet while excluding a specific IP address, scan all ports
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```





- Aktiivisten isäntien löytäminen




```bash
# Scan on CIDR or IP ranges
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# Host discovery scan (Ping Scan) on a network
nmap -sn 192.168.1.0/24
```



huomautus: `-sP`-vaihtoehto on ollut vanhentunut jo useita vuosia, ja se tulisi korvata `-sn`-vaihtoehdolla. (Päivitys 2025)_



```bash
# Host discovery scan without port scan
nmap 192.168.1.0/24 -sn

# Host discovery scan on a local network using various probe techniques
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan hosts listed in a text file
nmap -iL /tmp/mesCibles.txt

# Network scan with a specific IP excluded
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Subnet scan excluding another subnet
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```





- Versiotunnistus




```bash
# Enable version detection
nmap 192.168.1.0/24 -sV

# Version detection + advanced trace
nmap 192.168.1.0/24 -sV --version-trace

# Version detection with maximum probe rarity of 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Version detection with all probes
nmap 192.168.1.0/24 -sV --version-intensity 9

# Enable OS detection
nmap -O 10.10.10.0/24
```





- NSE-skriptit: haavoittuvuuksien etsiminen




```bash
# Run default NSE scripts
nmap -sC 10.10.10.152

# Scan all TCP ports with default NSE scripts
nmap -sC -p- 10.10.10.152

# Display help for script by name
nmap --script-help=ftp-*

# Display help for a category
nmap --script-help=discovery

# Use NSE scripts by category
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Inclusion/exclusion filter for NSE script categories
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Run a specific NSE script
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Pass arguments to an NSE script
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```





- Nmap-tulosten hallinta




```bash
# Save scan to text file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Save scan to condensed text file
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Save scan to XML file
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```





- Suorituskyvyn optimointi




```bash
# Version detection scan with max rate of 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300

# Version detection scan with default scripts, no retry, max host timeout 15min
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Version detection scan with the 2000 most common ports, aggressive scan speed (T4), debug output
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```





- TCP-skannaustyypit




```bash
# TCP SYN scan (fast, less stealthy)
nmap -sS 192.168.1.15

# TCP Connect scan (classic)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (detect firewall)
nmap -sA 192.168.1.15
```



Toivottavasti löydät nämä komennot hyödyllisiksi. Älä unohda mukauttaa skannauskohteesi kontekstisi mukaan ja tutustua viralliseen dokumentaatioon hallitaksesi suoritetut testit täysin.



### III. Päätelmät



Nmap-opetusohjelma on nyt valmis. Sinulla on nyt perusteet, joita tarvitset tämän kattavan ja tehokkaan työkalun käyttöön. Suosittelemme harjoittelemaan valvotuissa ympäristöissä (Hack The Box, VulnHub, virtuaalikoneet), ennen kuin käytät sitä tuotannossa.



Työkalun sisäisiä toimintoja ja lisäominaisuuksia on vielä paljon tutkittava. Tässä esiteltyjen komentojen ja käsitteiden hallitseminen antaa sinulle kuitenkin mahdollisuuden käyttää Nmapia luotettavasti ja tarkoituksenmukaisesti.