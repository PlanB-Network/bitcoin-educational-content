---
name: IP-verkot teoriasta käytäntöön
goal: Hallitse IP-verkkojen perusteet, jotta voit määrittää ja korjata niitä paremmin.
objectives: 


  - Ymmärtää TCP/IP-protokollan arkkitehtuurin ja toiminnan
  - Selitä IPv4:n ja IPv6:n erot, edut ja rajoitukset
  - Tunnistetaan ja erotetaan toisistaan erityyppiset IP Address:t
  - IP-osoitteiden määrittäminen ja tarkistaminen Unix/Linux-järjestelmissä
  - Käytä tärkeimpiä diagnostiikkatyökaluja verkko-ongelmien analysointiin ja ratkaisemiseen


---

# Olennaiset taidot IP-maailmassa liikkumiseen


Sukella IP-maailman ytimeen ja hanki itsellesi tiedot, joiden avulla voit ymmärtää ja hallita verkkoja tehokkaasti. Tällä kurssilla opit kaiken tarvittavan tietoverkoista selkeällä ja käytännönläheisellä tavalla.


Opit, miten verkot ja IP-osoitteet toimivat, miten IPv4 ja IPv6 erotetaan toisistaan, miten eri Address-luokat tunnistetaan ja käytetään ja miten TCP/IP-protokollan ja sen luomien IP-osoitteiden, fyysisten osoitteiden ja DNS-nimien välisten yhteyksien merkitys ymmärretään.


NET 302 on suunnattu lähinnä opiskelijoille, Linux-käyttäjille tai yksinkertaisesti uteliaille, jotka haluavat ymmärtää verkkoyhteyksien perusteita ja vahvistaa itsenäisyyttään infrastruktuurien hallinnassa, vianmäärityksessä ja optimoinnissa.


Liity joukkoomme ja muuta tietosi todelliseksi toiminnalliseksi asiantuntemukseksi!


___


Tämä NET 302 -kurssi on mukautettu kirjasta *Les bases du réseau: TCP/IP, IPv4 et IPv6*, jonka on kirjoittanut Philippe Pierre ranskaksi ja joka on julkaistu osoitteessa [IT-Connect](https://www.it-connect.fr/cours/les-bases-du-reseau-tcpip-ipv4-et-ipv6/), Creative Commons Attribution - ShareAlike 4.0 International ([CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)).



Loïc Morelin alkuperäiseen versioon on tehty huomattavia muutoksia: teksti on kirjoitettu kokonaan uudelleen, laajennettu ja rikastettu, jotta se tarjoaisi ajantasaista ja syvällistä sisältöä säilyttäen samalla Philippe Pierren alkuperäisen teoksen opettavaisen hengen. Myös kaaviot on tarkistettu.


+++


# Johdanto


<partId>a52b996d-1e23-470f-a9df-7ad88790099a</partId>



## Kurssin yleiskatsaus


<chapterId>9f238ecd-c9bb-4886-a205-2beba609fb13</chapterId>


Tämä kurssi tarjoaa täydellisen johdannon IP-verkkojen perusteisiin. Kurssi jakautuu neljään pääjaksoon, joista kukin käsittelee jotakin olennaista tietokoneverkon ymmärtämisen, konfiguroinnin ja diagnosoinnin kannalta.


### TCP/IP-protokolla


Tässä ensimmäisessä osassa luomme pohjatyön tutustumalla verkottumisen käsitteeseen ja TCP/IP-protokollan historiaan. Tutkimme sen pääkomponentteja: IP, TCP sekä lyhyt katsaus IPv5 QoS -protokollaan. Käsitellään myös palvelun alkeistapoja, jotta voidaan ymmärtää paremmin datan Exchange:n logiikkaa.


### IPv4-osoitteet


Sen jälkeen siirrytään IPv4-osoitteita käsittelevään moduuliin. Opit, miten IPv4:ää käytetään käytännössä, sen eri Address-tyypit (yksityinen, julkinen, broadcast jne.), DNS:n perustavanlaatuisen roolin sekä miten Ethernet-osoitteet ja ARP-protokolla toimivat. Tutustut myös NAT:iin (Network Address Translation) ja verkon konfiguroinnin perusteisiin.


### IPv6-osoitteet


Kolmannessa osassa keskitytään IPv6-osoitteistoon, joka on tarpeen IPv4:n rajoitusten poistamiseksi. Käymme läpi sen standardit ja määritelmät, Address Assignment paikallisverkossa, Address lohkojen hallinnan ja IPv6:n ja DNS:n välisen suhteen.


### Verkon diagnostiikkatyökalut


Lopuksi esittelemme tärkeimmät verkkodiagnostiikkatyökalut. Niiden avulla voit analysoida, valvoa ja korjata toimintahäiriöitä. Tämä osa on jäsennelty kerroksittain: Verkkoyhteys-, verkko-, siirto- ja ylemmät kerrokset.


Tämän kurssin lopussa sinulla on perustiedot, joiden avulla voit tehokkaasti hallinnoida verkkoinfrastruktuuria ja diagnosoida mahdollisia ongelmia.


Oletko valmis sukeltamaan tietokoneverkkojen maailmaan? Mennään!


**HUOMAUTUS**: Kuvaukset perustuvat GNU/Linux CentOS 7 -järjestelmään. Verkkokokoonpanot ovat kuitenkin suurelta osin samat, kun verrataan Debian- ja CentOS-järjestelmiä. Emme siis tee mitään eroa. Jos on, liitämme siihen erityisen logon.


**N.B.**: Jos törmäät kurssin aikana tuntemattomiin termeihin, katso määritelmät [sanastosta] (https://planb.network/resources/glossary).



# TCP/IP-protokollat


<partId>53fd4b73-cdf1-4865-ba29-1ac8ec3e9e9a</partId>



## Mikä on verkko?


<chapterId>7370904f-f8f5-4ad4-a63a-5931d94c3b3b</chapterId>



Tässä ensimmäisessä moduulissa tarkastelemme perusteellisesti TCP/IP-protokollaa, joka on nykyaikaisen digitaalisen viestinnän kulmakivi. Keskustelemme sen alkuperästä, perusperiaatteista ja sen käyttämästä osoitejärjestelmästä, joka on välttämätön tiedonkulun varmistamiseksi liitettyjen laitteiden välillä.


Kerromme myös yksityiskohtaisesti, mitkä ovat tämän mallin pääkomponentit, ja selitämme, miten ne vaikuttavat toisiinsa muodostaen toimivan, luotettavan ja skaalautuvan verkon. Ensin on kuitenkin tärkeää palata verkon käsitteeseen.


Etymologisesti verkko tarkoittaa joukkoa toisiinsa liitettyjä pisteitä, jotka muodostavat toisiinsa kytketyn rakenteen. Tietoliikenteessä ja tietojenkäsittelyssä tämä määritelmä tarkoittaa ryhmää laitteita (tietokoneita, reitittimiä, kytkimiä, liityntäpisteitä jne.), jotka pystyvät vaihtamaan tietoja fyysisten tai langattomien välineiden kautta. Verkko mahdollistaa siis jatkuvan tai katkonaisen tiedonkulun, joka riippuu vaatimuksista, käytetyistä protokollista ja käytetyn arkkitehtuurin luonteesta.


Ajan mittaan on kehitetty useita klassisia topologioita, jotka vastaavat erilaisiin kustannuksiin, suorituskykyyn, häiriönsietokykyyn ja huollon helppouteen liittyviin tarpeisiin. Näitä ovat mm:


- rengasverkko,
- puiden verkosto,
- linja-autoverkko,
- tähtiverkko,
- mesh-verkko.



### Rengasverkko


Rengastopologiassa laitteet on kytketty suljettuun silmukkaan: jokainen asema on yhteydessä seuraavaan, ja viimeinen asema on yhteydessä takaisin ensimmäiseen. Tässä kokoonpanossa jokainen laite toimii releenä, joka välittää tietoja seuraavalle linkille. Verkkotyypistä riippuen tieto voi kiertää vain yhteen suuntaan tai molempiin.


Tämän järjestelyn etuna on sen kaapeloinnin yksinkertaisuus ja se, että se ei ole riippuvainen mistään keskuslaitteista. Koko verkon jatkuvuus riippuu kuitenkin jokaisen yksittäisen elementin kunnosta: yksittäisen aseman vikaantuminen voi keskeyttää koko viestintäjärjestelmän. Tämän vuoksi käytetään usein redundanssia tai ohitusmekanismeja.



![Image](assets/fr/001.webp)



### Puiden verkosto


Puuverkko eli hierarkkinen topologia on mallinnettu sukupuun rakenteen mukaan. Se koostuu peräkkäisistä tasoista: huipulla sijaitseva juurisolmu yhdistää useita alemman tason solmuja, jotka voivat puolestaan muodostaa yhteyksiä muihin solmuihin ja niin edelleen.


Tämä hierarkkinen rakenne toimii erityisen hyvin suurissa verkoissa, joissa tarvitaan selkeää vastuunjakoa ja segmentoitua hallintaa. Se tekee verkosta kuitenkin myös haavoittuvaisen ylemmän tason solmujen vikaantumiselle: juuren tai päähaaran menettäminen voi katkaista kokonaisia infrastruktuurin osia.



![Image](assets/fr/002.webp)



### Linja-autoverkko


Väylätopologiassa kaikki laitteet käyttävät samaa siirtovälinettä, tyypillisesti koaksiaalijohtoa tai optista kuitua. Kukin laite on passiivisesti kytketty, eli se ei aktiivisesti muuta signaalia, ja se voi lähettää tai vastaanottaa tietoja tätä jaettua kanavaa pitkin.


Väylätopologian tärkein etu on alhaiset asennuskustannukset yksinkertaisen kaapeloinnin ansiosta.  Vanhemmissa koaksiaalipohjaisissa toteutuksissa (Ethernet 10BASE2/10BASE5) yksittäisen aseman katkaiseminen tai häviäminen saattoi kuitenkin häiritä tai jopa pysäyttää koko liikenteen, koska väylän sähköinen jatkuvuus ja päättymisimpedanssi eivät enää säilyneet. Yhden fyysisen väliaineen käyttö on myös kriittinen heikkous: mikä tahansa katkos tai vika pysäyttää koko verkon tiedonsiirron.



![Image](assets/fr/003.webp)



### Tähtiverkko


Tähtitopologia, joka tunnetaan myös nimellä "hub and spoke", on nykyään yleisin, erityisesti koti- ja toimisto-Ethernet-verkoissa. Siinä kaikki laitteet ovat yhteydessä yhteen keskuslaitteeseen.


Tämä rakenne tekee hallinnasta ja ylläpidosta helppoa: jos yksi oheislaite vikaantuu, muu verkko ei vaikuta siihen. Huonona puolena on se, että keskuslaite on yksittäinen vikapiste: jos se kaatuu, tiedonsiirto katkeaa kaikkialla. Kaapeleiden laatu ja linkkien pituudet on myös harkittava huolellisesti, jotta suorituskyky säilyy hyvänä.



![Image](assets/fr/004.webp)



**Huomautus**: On edelleen olemassa verkkoja, jotka on järjestetty lineaariseen, väylän kaltaiseen topologiaan, jossa laitteet on kytketty peräkkäin. Vaikka tämä ratkaisu on edullinen ottaa käyttöön, sillä on kuitenkin se suuri haittapuoli, että yksittäinen katkos eristää osan isännistä ja jakaa verkon itsenäisiin osajoukkoihin.


### Verkkoverkko


Mesh-verkko on suunniteltu mahdollisimman redundantiksi: jokainen laite on suoraan yhteydessä jokaiseen toiseen laitteeseen. Tämä takaa palvelun jatkuvuuden, vaikka useat linkit tai laitteet vioittuisivat, koska liikenne voidaan ohjata uudelleen vaihtoehtoisia reittejä pitkin.


Tämä merkitsee sitä, että muodostettavien yhteyksien määrä kasvaa nopeasti päätelaitteiden määrän kasvaessa. Kun yhteyspisteitä on `N`, tarvitaan `N × (N-1) / 2` erillistä linkkiä, mikä tekee tästä topologiasta kalliin ja monimutkaisen ottaa käyttöön. Siksi sitä käytetään pääasiassa kriittisissä verkoissa, joissa vaaditaan erittäin korkeaa käytettävyyttä, kuten Internetin tietyissä osissa tai herkissä teollisuusjärjestelmissä.



![Image](assets/fr/005.webp)



On olemassa muitakin muunnelmia, kuten grid- tai hyperkuutioverkot, jotka on suunniteltu hajautetun tietojenkäsittelyn tai rinnakkaisprosessoinnin erityistarpeisiin.


Maailmanlaajuisessa mittakaavassa Internet on massiivinen verkkojen yhteenliittäminen, jossa käytetään erilaisia topologioita, joita yhdistävät yhteinen osoite (IPv4 ja IPv6) ja kokoelma IETF:n (*Internet Engineering Task Force*) määrittelemiä standardoituja protokollia. Tämä monimuotoisuus tarkoittaa, että Internet ei noudata yhtä ainoaa topologiaa: sen rakenne on joustava, skaalautuva ja riippumaton loogisesta osoitusjärjestelmästä, joka tekee siitä käyttökelpoisen.



## TCP/IP:n alkuperä


<chapterId>266b6864-8789-48d7-bc85-001cb9f1651f</chapterId>



TCP-protokollan juuret ovat **ARPA:ssa** (*Advanced Research Projects Agency*, jonka nimi muutettiin DARPA:ksi vuonna 1972), joka käynnisti **ARPANET**-projektin vuonna 1966. Ensimmäinen ARPANET-segmentti otettiin käyttöön lokakuussa 1969, ja se yhdisti UCLA:n ja Stanfordin yliopistot toisiinsa. Tavoitteena oli yhdistää tutkimuskeskukset pakettikytkentäisen verkon avulla, joka pystyi pitämään yhteydenpidon käynnissä myös infrastruktuurin osittaisen vikaantumisen sattuessa.


Osana tätä dynamiikkaa ARPA rahoitti Berkeleyn yliopistoa integroimaan ensimmäiset TCP/IP-protokollat BSD Unix -järjestelmäänsä. Tällä oli suuri merkitys protokollan leviämisessä ja standardoinnissa ensin akateemisessa maailmassa ja myöhemmin teollisuudessa.


**Huomautus**: tuohon aikaan tietotekniikan tutkijoilla ei ollut vielä Linuxia (joka ilmestyi vasta 1990-luvun alussa) eikä Minixiä, Andrew Tanenbaumin suunnittelemaa opetusjärjestelmää.  Tärkeimmät vaihtoehdot olivat Unix tai joskus OpenVMS:n kaltaiset patentoidut suurtietokoneet. Joustavuutensa ja avoimuutensa ansiosta Unix oli tärkeä tekijä ensimmäisten verkkokäsitteiden levittämisessä.


Tarkkaan ottaen TCP/IP ei ole yksittäinen protokolla, vaan TCP:n ja IP:n ympärille rakennettu protokollasarja. Se tuli tunnetuksi, koska se tarjosi standardoidun ohjelmointikäytännön Interface samassa verkossa olevien koneiden väliseen tiedonvaihtoon. Tämä Interface, joka perustuu "sockets"-nimisiin alkeisiin, mahdollisti luotettavien ja joustavien yhteyksien luomisen ja samalla keskeisten sovellusprotokollien integroinnin.


ARPANET on siis nykyisen Internetin historiallinen perusta. Internet onkin pakettikytkentäperiaatteeseen perustuva maailmanlaajuinen verkko, jossa tiedot liikkuvat käyttäen standardoituja protokollia, joilla varmistetaan heterogeenisten järjestelmien yhteensopivuus ja yhteentoimivuus. Tämä avoin arkkitehtuuri on mahdollistanut lukemattomien palveluiden ja sovellusten kehittämisen ja käyttöönoton, mukaan lukien


- sähköpostit,
- world Wide Web (www),
- tiedostojen siirto ja jakaminen...


Protokollien hallintoa ja kehitystä valvoo ***Internet Architecture Board*** (IAB).

Tämä organisaatio koordinoi teknisiä suuntauksia kahden päärakenteen kautta:


- IRTF** (_Internet Research Task Force_), joka tekee pitkäaikaista tutkimusta protokollien kehityksestä ja parantamisesta.
- IETF** (_Internet Engineering Task Force_), joka kehittää, standardoi ja dokumentoi Internetissä käytettäviä toimintaprotokollia


Verkkoresurssien (IP Address -alueet, autonomisten järjestelmien numerot, verkkotunnukset jne.) jakelua koordinoi kansainvälisesti **IANA/ICANN**. Operatiivinen hallinnointi perustuu: **RIR** (*Regional Internet Registries*): **RIPE NCC** (Eurooppa, Lähi-itä, Keski-Aasia), **ARIN**, **APNIC**, **LACNIC** ja **AFRINIC**.


Kaikki TCP/IP-protokollan määrittelyt on kirjattu asiakirjoihin nimeltä **RFC** (_Request For Comments_), jotka toimivat arvovaltaisina teknisinä viitteinä. RFC:t päivitetään ja numeroidaan jatkuvasti protokollapaketin jatkuvan kehityksen mukaisesti.


TCP/IP-pino esitetään usein neljän toiminnallisen kerroksen pinona, ja sitä verrataan usein **ISO:n** (_International Standards Organization_) kehittämään seitsemän Layer:n **OSI** (_Open Systems Interconnection_) -malliin, jota käytetään käsitteellisenä viitekehyksenä verkoissa.


TCP/IP-mallin neljä kerrosta ovat:


- nETWORK ACCESS Layer, joka tarjoaa fyysisen linkin ja mediakäytön valvontaprotokollat;
- iNTERNET Layer, joka huolehtii reitityksestä ja IP-osoitteista;
- tRANSPORT Layer, joka takaa TCP:n tai UDP:n kaltaisia protokollia käyttävien tietovirtojen luotettavuuden ja hallinnan;
- aPPLICATION Layer, joka kokoaa yhteen käyttäjä- ja ohjelmistoprotokollat, kuten HTTP, FTP, SMTP ja DNS.



![Image](assets/fr/006.webp)



Nykyään IP:n yleisimmin käytetty versio on IPv4, mutta sen 32-bittiseen Address-avaruuteen liittyy selviä rajoituksia. Tämä johti IPv6:n luomiseen, jossa käytetään 128-bittistä osoitteistusta ja joka tarjoaa käytännössä rajoittamattoman kapasiteetin: tämä on välttämätöntä, jotta voidaan tukea liitettyjen laitteiden räjähdysmäistä kasvua ja vastata esineiden internetin, liikkuvuuden ja turvallisuuden haasteisiin.


Jokainen TCP/IP-pinon Layer tarjoaa tiettyjä palveluja, mikä mahdollistaa Address erilaisten verkkotarpeiden modulaarisen täyttämisen: fyysinen siirto, looginen osoitteistus, tietojen eheys ja sovellustason palvelut.


| Device example    | Description                                                                               | 	TCP/IP layer |
| ---------------------- | ----------------------------------------------------------------------------------------- | ----------------------- |
| Web server            | Application services closest to end users                                      | Application             |
| Gateway or proxy    | 	Encodes, encrypts, compresses useful data                                              | Application             |
| Session switch | Establishes sessions between applications                                               | Application             |
| Firewall or L4 router | Establishes, maintains, and terminates sessions between endpoint devices                  | Transport               |
| Router                | Globally addresses interfaces and determines optimal paths through a network | Network                  |
| Switch   | Locally addresses interfaces and forwards traffic via MAC                            | Network Access         |
| Network Interface Card (NIC)     | Signal encoding, cabling, connectors, physical specifications                        | Network Access         |

https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864

## IPv5 QoS-protokolla


<chapterId>570ded19-be61-4005-844e-9490570a6455</chapterId>



IP-paketin otsikko on olennainen tietorakenne, joka on jaettu useisiin kenttiin, joilla kullakin on oma tehtävänsä sen varmistamiseksi, että paketit lähetetään ja käsitellään oikein, kun ne kulkevat verkon läpi. Näihin kenttiin kuuluvat kohde-IP Address (jota tarvitaan paketin reitittämiseen aiotulle vastaanottajalle), IHL-kentän (*Internet Header Length*) osoittama otsikon pituus, *Total Length-kenttään* kirjattu paketin kokonaispituus, ohjaus- ja varmennustiedot sekä muita parametreja tiedonsiirron sujuvuuden ja laadun hallintaa varten.


Otsikon ensimmäinen kenttä on nimeltään Version. Tämä 4-bittinen arvo määrittää, mitä IP-protokollan versiota paketti noudattaa. Se on tärkeä, koska se kertoo kullekin reitittimelle tai välilaitteelle, miten kapseloitua dataa on tulkittava ja käsiteltävä.


**Huomaa: IP-protokollaversioiden hallinnoinnista ja Assignment:stä huolehtii **IANA**. 4-bittinen kenttä mahdollistaa 16 binääriyhdistelmää (arvot 0-15). Niiden nykyiset Assignment ovat:



| Version Number | Protocol   | Version Description         | Reference               |
| -------------- | ---------- | --------------------------- | ----------------------- |
| 0–1            | Reserved   | Reserved                    |                         |
| 2–3            | Unassigned | Unassigned                  |                         |
| 4              | IP         | Internet Protocol           | RFC 791                 |
| **5**          | **ST**     | **ST Datagram mode**        | **RFC 1190** / RFC 1819 |
| 6              | IPv6       | Internet Protocol version 6 | RFC 8200                |
| 7              | TP/IX      | The Next Internet           | RFC 1475                |
| 8              | PIP        | The P Internet Protocol     | RFC 1621                |
| 9              | TUBA       | Tuba                        | RFC 1347                |
| 10–14          | Unassigned | Unassigned                  |                         |
| 15             | Reserved   | Reserved                    |                         |

Näihin kuuluu IPv5, joka oli olemassa ST-protokollana (_Stream Protocol_), vaikka se on suurelta osin tuntematon yleisölle. IPv5 kehitettiin 1980-luvulla, ja se suunniteltiin Address:n tuohon aikaan kasvavaan tarpeeseen: palvelun laadun (QoS) tarjoamiseen tietyille tietovirroille, jotka vaativat jatkuvaa ja vakaata siirtoa, kuten Voice over IP tai multimediavirrat. Sen tavoitteena oli taata päästä päähän ulottuva kaistanleveys ja prioriteetti, mikä on samankaltainen käsite kuin RSVP (_Resource Reservation Protocol_), jonka avulla verkkoresursseja voidaan nykyään varata dynaamisesti nykyaikaisissa reitittimissä.


IPv5 jäi kuitenkin kokeiluluonteiseksi, ja se otettiin käyttöön vain harvoissa verkkolaitteissa. Sen vähäinen käyttöönotto yhdistettynä nopeasti kasvavaan Address:n tilantarpeeseen johti siihen, että Internetin suunnittelijat siirtyivät suoraan IPv4:stä IPv6:een. Näin vältettiin sekä IPv4:n Address-rajoitteet että sekaannuksen tai yhteensopimattomuuden riski IPv5:n kokeellisten määritysten kanssa.


Vaikka IPv5:tä ei koskaan käytetty laajalti, sillä oli tärkeä rooli QoS:ää ja liikenteen hallintaa koskevan varhaisen ajattelun muokkaamisessa. Nykyään se on enemmänkin historiallinen merkki kuin toimiva standardi.


**Muistutus** - Protokolla on joukko viestintäsääntöjä: tietorakenteita, algoritmeja, pakettimuotoja ja konventioita, joiden avulla eri laitteet voivat Exchange:n avulla välittää tietoa luotettavasti ja ymmärrettävästi. Palvelu on protokollan konkreettinen toteutus erityisten ohjelmien (asiakkaiden ja palvelimien) avulla, jotka noudattavat näitä sääntöjä ja antavat toiminnallisuuden käyttäjien ja sovellusten käyttöön.


Voimme nyt tarkastella lähemmin IP-protokollan rakennetta ja toimintaa, joka on kaiken verkkoviestinnän olennainen perusta.



## IP-protokolla


<chapterId>758fddbd-b652-4c18-bd1e-d038bd2e4d05</chapterId>



### Määritelmät ja yleistä tietoa


IP-protokolla eli "***Internet Protocol***" on TCP/IP-mallin selkäranka. Se kuljettaa datapaketteja isännältä toiselle verkossa, olipa se sitten paikallinen tai maailmanlaajuinen. Sillä on kaksi keskeistä tehtävää: se hallinnoi laitteiden loogista osoitteistusta ja varmistaa pakettien reitityksen usein heterogeenisten ja toisiinsa kytkettyjen verkkojen välillä.


Fyysisellä tasolla tiedonsiirto perustuu laitteistoliitäntöihin, joilla solmujen välille luodaan pisteestä pisteeseen -yhteydet. IP-protokolla mahdollistaa kuitenkin päästä päähän -tiedonsiirron, sillä se antaa kullekin paketille tiedot, joita se tarvitsee kulkeakseen useita mahdollisia reittejä määränpäähänsä.


Kolme verkkokonfiguraatiota Elements määrittää, miten paketti lähetetään matkalleen:


- IP Address**: yksilöi kohdeisännän verkossa.
- Aliverkon peite**: määrittää, mikä osa Address:sta yksilöi verkon ja mikä osa isännän, mikä mahdollistaa loogisen jakamisen aliverkkoihin.
- Yhdyskäytävä**: osoittaa välireitittimen, jonka kautta paketin on kuljettava päästäkseen ulkoiseen verkkoon tai lähiverkon toiseen segmenttiin.


Internetissä tieto ei kulje yhtenä jatkuvana virtana, vaan se lähetetään **datagrammeina**: itsenäisinä tietolohkoina, joista jokainen sisältää kaikki toimitukseen tarvittavat tiedot. Tämä on periaate **pakettikytkennässä**, jossa tieto jaetaan itsenäisiin yksiköihin, jotka voivat kulkea eri reittejä saavuttaakseen saman vastaanottajan.


Hyötykuorman (*payload*) lisäksi jokainen IP-datagrammi sisältää rakenteisen otsikon, jossa on kenttiä, kuten kohde Address, lähde Address, palvelun tyyppi, protokollan versionumero ja muita lähetyksen hallintaan tarvittavia ohjaustietoja.


IP-datagrammin teoreettinen enimmäiskoko on **65 536 oktettia**, jonka rajoittaa otsikon kokonaispituuskenttä. Käytännössä tämä koko saavutetaan harvoin, koska paketteja kuljettavat fyysiset verkot (Ethernet, Wi-Fi, valokuitu...) asettavat yleensä tiukemmat rajat, jotka tunnetaan nimellä **MTU** (_Maximum Transmission Unit_). Jos datagrammi ylittää fyysisen linkin MTU:n, se on jaettava pienempiin paketteihin, jotka lähetetään erikseen ja kootaan uudelleen saapuessaan.


Tämä mukautuvuus tekee IP-protokollasta vankan ja joustavan protokollan, joka pystyy toimimaan monenlaisten taustalla olevien tekniikoiden kanssa säilyttäen samalla heterogeenisten järjestelmien ja verkkojen yleisen yhteensopivuuden.



### IP-datagrammeiden pirstoutuminen


Kun IP-datagrammin on kuljettava verkon läpi, jonka siirtokapasiteetti on pienempi kuin datagrammin kapasiteetti, se on **pirstottava**, jotta se voi kulkea ongelmitta. Tätä fyysisen koon rajaa kutsutaan **MTU**:ksi (Maximum Transmission Unit): suurin kehyksen koko, joka voi kulkea tietyn verkon läpi ilman jakamista.


Kukin verkkotekniikka asettaa oman MTU:nsa, joka määräytyy sen laitteiston ja protokollan ominaisuuksien mukaan. Yleisiä arvoja ovat mm:


- ARPANET**: 1000 tavua
- Ethernet**: 1500 tavua
- FDDI**: 4470 tavua


Kun datagrammi ylittää sen verkon segmentin MTU:n, jonka se on kuljettava, reitityslaitteet jakavat sen pienempiin **palasiin**, jotka noudattavat rajaa. Tämä tapahtuu tyypillisesti siirryttäessä suurella MTU:lla varustetusta verkosta verkkoon, jonka kapasiteetti on pienempi. Esimerkiksi FDDI-verkosta tuleva datagrammi voidaan joutua pirstomaan ennen sen lähettämistä Ethernet-segmentin kautta.



![Image](assets/fr/008.webp)



Pirstoutumisprosessi toimii seuraavasti:


- Reititin jakaa datagrammin pätkiin, jotka eivät ole suurempia kuin kohdeverkon MTU.
- Kunkin fragmentin koko on 8 tavun monikerta, koska IP-protokolla käyttää tätä yksikköä uudelleenkokoamisoffsetin koodaamiseen.
- Jokainen fragmentti saa oman IP-otsakkeen, joka sisältää tiedot, joita lopullinen vastaanottaja tarvitsee kootakseen fragmentit uudelleen oikeassa järjestyksessä.


Kun palaset on pirstottu, ne kulkevat itsenäisesti verkon kautta. Ne voivat kulkea eri reittejä reititystaulukoiden, linkkien kuormituksen tai katkosten mukaan. Ei ole mitään takeita siitä, että ne saapuvat perille samassa järjestyksessä kuin ne on lähetetty.


Saapumisen jälkeen vastaanottava kone huolehtii **kokoamisesta**. Otsikoissa olevien tietojen (jaettu tunniste, siirto ja fragmentointiliput) avulla se asettaa fragmentit takaisin oikeaan järjestykseen ja muodostaa alkuperäisen datagrammin uudelleen ennen sen lähettämistä seuraavalle Layer:lle. Jos yksikin fragmentti katoaa tai on vioittunut, koko datagrammi yleensä hylätään, sillä ilman jokaista fragmenttia tulos olisi epätäydellinen tai käyttökelvoton.


Vaikka pirstominen ja uudelleenkokoaminen ovat tehokkaita, niillä on haittapuolensa: reitittimille ja isännille aiheutuu ylimääräistä käsittelyä ja pakettihäviöiden mahdollisuus kasvaa, mikä voi lisätä uudelleenlähetyksiä. Siksi huolellinen MTU:n hallinta ja pakettikoon optimointi ovat tärkeitä sujuvan ja tehokkaan IP-viestinnän kannalta.



### Tiedon kapselointi


Jotta varmistetaan, että tiedot ohjautuvat oikein TCP/IP-mallin kerrosten läpi, **kapselointi** on avainasemassa. Jokaisessa vaiheessa, kun viesti kulkee lähettäjän sovelluksesta vastaanottajan koneelle, siihen lisätään lisätietoa, niin sanottuja otsikoita. Nämä otsikot antavat välissä oleville laitteille ja ohjelmistokerroksille ohjeet, joita ne tarvitsevat tiedon käsittelyyn, toimittamiseen ja tarvittaessa uudelleen kokoamiseen.


Kun viesti lähetetään, se kulkee TCP/IP-pinon neljän kerroksen läpi. Jokaisessa Layer:ssa olemassa olevan datan eteen lisätään uusi otsikko: kukin otsikko sisältää erityisiä metatietoja, kuten loogisia tai fyysisiä osoitteita, viestintäportteja, järjestysnumeroita, virheidenvalvontalippuja ja muita tietoja, joita tarvitaan lähetyksen ja reitityksen hallintaan.


Toimitus noudattaa siten jäsenneltyä prosessia:


- Application Layer luo alkuperäisen **viestin**, joka sisältää raakatiedot.
- Transport Layer kapseloi sen **segmentiksi** ja lisää lähde- ja kohdeportit, sekvenssinumerot ja virranohjausmekanismit.
- Internet Layer lisää segmenttiin IP-otsikon, joka muodostaa **datagrammin**, jossa on lähde- ja kohde-IP-osoitteet.
- Network Access Layer kietoo datagrammin **kehykseen** ja lisää siihen MAC-osoitteet ja eheyden tarkistuskoodit (CRC).



![Image](assets/fr/009.webp)



Tämä kapselointiprosessi varmistaa sekä tiedon eheyden ja jäljitettävyyden että sen mukautuvuuden: kun siirrytään verkosta toiseen, otsikot antavat laitteille tiedot, joita tarvitaan reitin valintaan, validiteetin tarkistamiseen tai tarvittaessa pirstomiseen.


Saapumisen jälkeen prosessi on päinvastainen: vastaanottava laite saa kehyksen Network Access Layer:ssä, joka lukee ja poistaa vastaavan otsikon. Tämän jälkeen datagrammi siirretään Internet Layer:lle, joka lukee IP-otsikon ja poistaa sen vuorostaan toimittaakseen segmentin Transport Layer:lle. Kuljetus-Layer käsittelee kuljetusotsikot, tarkistaa virran eheyden ja toimittaa lopulta **viestin** alkuperäisessä muodossaan kohdesovellukselle.



![Image](assets/fr/010.webp)



Tietojen muuntaminen kussakin Layer:ssa voidaan tiivistää seuraavasti:


- Viesti**: Application Layer:n tietolohko.
- Segmentti**: datayksikkö sen jälkeen, kun Transport Layer on kapseloinut sen.
- Datagrammi**: Internet Layer:n IP-otsikon lisäämisen jälkeen ottama muoto.
- Kehys**: viimeinen lohko, joka on valmis lähetettäväksi fyysisen väliaineen välityksellä Network Access Layer:n toimesta.



![Image](assets/fr/011.webp)



Tämä Internet-viestinnän luotettavuuden ja yleismaailmallisuuden kannalta olennainen prosessi varmistaa, että kaikki tiedot, olivatpa ne kuinka hajanaisia tai monimutkaisia tahansa, voidaan siirtää päästä päähän ja että vastaanottava laite voi ymmärtää ja käyttää niitä.



### IP-osoitteet


Vaikka pakettikytkentä, fragmentointi ja kapselointi olisivat käytössä, verkko ei silti voisi toimia ilman luotettavaa osoitejärjestelmää. Varmistaakseen, että jokainen datapaketti saavuttaa oikean vastaanottajan, Internet Layer käyttää yksilöllistä tunnusta: **IP Address**.

IPv4:ssä IP Address on koodattu **32 bitillä** ja kirjoitettu neljänä desimaalilukuna, jotka on erotettu toisistaan pisteillä, tutussa N1.N2.N3.N4-muodossa (esimerkiksi: 192.168.1.12).


IP Address:ssä on kaksi osaa:


- _netid_**: yksilöi verkon, johon isäntä kuuluu
- _hostid_**: yksilöi tietyn isäntäkoneen kyseisessä verkossa

Tämän erottelun ansiosta maailmanlaajuinen Internet voidaan loogisesti jäsentää moniin toisiinsa liitettyihin verkkoihin.


Aikaisemmin IPv4-järjestelmä perustui luokkapohjaiseen järjestelmään, joka oli merkitty A:sta E:hen ja jossa määriteltiin Address:n valikoima ja niiden käyttötarkoitus. Kukin luokka osoitti tietyn määrän bittejä _netid_- ja _hostid_-luokille, mikä vaikutti suoraan verkkojen ja isäntien mahdolliseen määrään.



| **Class** | **IPv4 Address Range**            | **Usage**                    |
| --------- | --------------------------------- | ---------------------------- |
| A         | 1.x.x.x to 126.x.x.x              | Unicast addresses            |
|           | (127.x.x.x reserved for loopback) | Local loopback               |
| B         | 128.0.x.x to 191.255.x.x          | Unicast addresses            |
| C         | 192.0.0.x to 223.255.255.x        | Unicast addresses            |
| D         | 224.0.0.0 to 239.255.255.255      | IP Multicast                 |
| E         | 240.0.0.0 to 255.255.255.255      | Reserved for experimentation |

Kaikkia mahdollisia arvoja ei voida määrittää isännille. Esimerkiksi **luokan C** Address:ssa viimeinen tavu tarjoaa 8 bittiä (256 arvoa). Näistä kaksi on kuitenkin varattu:


- 0: tunnistaa itse verkon
- 255: on **broadcast** Address, jota käytetään paketin lähettämiseen kaikille verkon isännille kerralla.

Jäljelle jää 254 käyttökelpoista osoitetta laitteille.


Käytettävissä olevien osoitteiden määrä vaihtelee suuresti eri luokkien välillä: luokan A suurista yleisistä verkoista luokan B yritysverkkoihin ja luokan C pienempiin paikallisverkkoihin.



![Image](assets/fr/013.webp)



Jotkin Address-alueet on varattu yksityiskäyttöön, eikä niitä koskaan reititetä suoraan Internetiin. Näitä kutsutaan **yksityisosoitteiksi**, ja niitä käytetään organisaatioiden, yritysten tai kotien sisällä, ja ne vaativat Address-käännöksen, tyypillisesti NAT:n (*Network Address Translation*), jotta ne pääsevät julkiseen Internetiin. Nämä ovat:


- Luokka A**: 10.0.0.0 - 10.255.255.255.255
- Luokka B**: 172.16.0.0 - 172.31.255.255
- Luokka C**: 192.168.0.0 - 192.168.255.255


Kun laite, jolla on yksityinen Address, käyttää Internetiä, NAT-yhteensopiva reititin tai yhdyskäytävä korvaa sen voimassa olevalla julkisella Address:llä.


Esimerkki: Jos isännän Address on **192.168.7.5**, voimme päätellä:


- 192.168.7.0: verkko Address
- 192.168.7.1: usein paikallinen reititin
- 192.168.7.5: itse isäntä


Toinen erikoistapaus on **127.0.0.1**, joka tunnetaan nimellä "***loopback***".

Linux-järjestelmissä se liittyy Interface **lo**. Tämän Address:n avulla kone voi käyttää Address:ää itseään paikallista testausta tai diagnostiikkaa varten ilman fyysisen Interface:n kautta kulkemista. Koko alue **127.0.0.0/8** on varattu tätä tarkoitusta varten.


Address:n käytön optimoinnissa ja monimutkaisten verkkojen suunnittelussa **aliverkkomaskin** (_netmask_) käyttö on välttämätöntä. Tämä binäärinen maski erottaa IP Address:n _netid_:n ja _hostid_:n toisistaan.

Jokaisella luokalla on oletusmaski:


- 255.0,0,0** luokan A osalta,
- 255.255.0.0.0** luokan B osalta,
- 255.255.255.0** luokan C osalta.


Hyvän verkon suunnittelussa noudatetaan perussääntöä: laitteiden, joiden on kommunikoitava suoraan, on oltava samassa verkossa tai aliverkossa. Verkon segmentoimiseksi käytetään aliverkkoa, jossa verkko jaetaan pienempiin aliverkkoihin käyttämällä tarkempaa maskia.


Esimerkki aliverkon määrittämisestä:

**luokan C** verkko: 192.255.255.255.255.0 on oletusmaski 255.255.255.0.

Haluamme 4 aliverkkoa, joissa kussakin voi olla enintään 60 isäntää.


**Vaihe 1**: Tarvittavien osoitteiden määrä aliverkkoa kohti = 60 + 2 varattua osoitetta (verkko + broadcast) = 62.


**Vaihe 2**: Etsi lähin potenssi 2 ≥ 62. -> 2⁶ = 64.


**Vaihe 3: Säädä maski. Pidä _netid_-bitit ja varaa tarvittavat _hostid_-bitit. Saamme binäärisen maskin, joka muunnettuna antaa tulokseksi **255.255.255.255.192**.


```
11111111 11111111 11111111 11000000
```


**Vaihe 4**: Laske Address-alueet kullekin aliverkolle vaihtelemalla isännälle varattuja bittejä.



| Subnet ID (bits) | Subnet Address   | Subnet Mask     | Address Range                 | Broadcast Address |
| ---------------- | ---------------- | --------------- | ----------------------------- | ----------------- |
| 00               | 192.168.1.0/26   | 255.255.255.192 | 192.168.1.1 – 192.168.1.62    | 192.168.1.63      |
| 01               | 192.168.1.64/26  | 255.255.255.192 | 192.168.1.65 – 192.168.1.126  | 192.168.1.127     |
| 10               | 192.168.1.128/26 | 255.255.255.192 | 192.168.1.129 – 192.168.1.190 | 192.168.1.191     |
| 11               | 192.168.1.192/26 | 255.255.255.192 | 192.168.1.193 – 192.168.1.254 | 192.168.1.255     |


**Vaihe 5**: Tämä luo neljä aliverkkoa, joista kukin tukee enintään 62 konetta, mutta pitää samalla yleisen osoitusjärjestelmän tehokkaana. _hostid_-osio jaetaan _subnetid_-osioon ja host-osioon.



![Image](assets/fr/016.webp)



Tämä aliverkon jakamisen perusperiaate on edelleen välttämätön nykyaikaisessa verkkotekniikassa, sillä se mahdollistaa tarkan IP-osoituksen, paremman liikenteen hallinnan, vahvan segmenttien eristämisen ja skaalautuvan verkonhallinnan.



### CIDR-osoitteet


1990-luvun alussa, kun Internet levisi nopeasti yrityksissä ja organisaatioissa, perinteinen IP-osoitejärjestelmä, joka perustui luokkiin (A, B, C), alkoi osoittaa rajansa.

Sen jäykkä rakenne johti IP-osoitteiden huomattavaan tuhlaamiseen ja teki reititystaulukoista yhä suurempia, monimutkaisempia ja vaikeammin ylläpidettäviä.

Näiden ongelmien ratkaisemiseksi otettiin käyttöön joustavampi ja tehokkaampi menetelmä: **CIDR** (_Classless Inter-Domain Routing_). CIDR:stä on vähitellen tullut standardi, joka on suurelta osin korvannut vanhan luokkapohjaisen järjestelmän.


CIDR:n ydinajatus on kyky ryhmitellä useita vierekkäisiä verkkoja, erityisesti C-luokan lohkoja, yhdeksi loogiseksi yksiköksi, jota kutsutaan **supernetiksi** (_supernet_). Tämän yhdistelyn ansiosta yksi merkintä reititystaulussa voi edustaa useita aliverkkoja, mikä vähentää reitittimien käsiteltävien reittien määrää ja parantaa niiden suorituskykyä.


Vaikka C-luokan verkoissa oli alun perin suurin tarve aggregointiin niiden pienemmän kapasiteetin vuoksi, periaatetta on sovellettu myös B-luokan ja teoriassa jopa A-luokan verkkoihin, vaikka jälkimmäiset eivät olekaan niin suurten Address-alueidensa vuoksi niin suuressa vaarassa.


CIDR:n avulla kiinteiden luokkien käsite katoaa. Address-avaruutta käsitellään jatkuvana alueena, joka voidaan jakaa tai yhdistää tarpeen mukaan. CIDR-lohkot määritellään aliverkkomaskien avulla, joita ei ole rajoitettu A-, B- tai C-luokkien oletusarvoihin. CIDR-lohko voi edustaa joko yhtä verkkoa tai samaa etuliitettä käyttävien aliverkkojen yhtenäistä joukkoa.


CIDR-lohko kirjoitetaan muodossa "Address/prefix", jossa vinoviivan jälkeinen numero osoittaa, kuinka monta bittiä verkko-osuus on. Esimerkiksi /17 tarkoittaa, että ensimmäiset 17 bittiä yksilöivät verkon, kun taas loput 15 bittiä yksilöivät isännät.


Esimerkki:

/17-lohko sisältää 2^(32-17) osoitetta, joten 2^15 = 32 768 osoitetta yhteensä. Kun vähennetään kaksi varattua osoitetta (verkko- ja lähetysosoite), jäljelle jää 32 766 käyttökelpoista isäntäosoitetta. Näin verkon ylläpitäjät voivat mitoittaa aliverkkonsa tarkasti todellisia tarpeita vastaaviksi ja välttää turhaa tuhlausta.


Jotta CIDR:n mitoituksen ymmärtäminen olisi helpompaa, tässä on taulukko yleisimmistä etuliitteistä ja niitä vastaavista aliverkkomaskista ja käyttökelpoisista osoitteista:


| CIDR Prefix | Available Host Bits | Subnet Mask     | Usable Host Addresses         |
| ----------- | ------------------- | --------------- | ----------------------------- |
| /8          | 24                  | 255.0.0.0       | 2^24 - 2 = 16,777,214         |
| /12         | 20                  | 255.240.0.0     | 2^20 - 2 = 1,048,574          |
| /16         | 16                  | 255.255.0.0     | 2^16 - 2 = 65,534             |
| /20         | 12                  | 255.255.240.0   | 2^12 - 2 = 4,094              |
| /24         | 8                   | 255.255.255.0   | 2^8 - 2 = 254                 |
| /26         | 6                   | 255.255.255.192 | 2^6 - 2 = 62                  |
| /27         | 5                   | 255.255.255.224 | 2^5 - 2 = 30                  |
| /28         | 4                   | 255.255.255.240 | 2^4 - 2 = 14                  |
| /29         | 3                   | 255.255.255.248 | 2^3 - 2 = 6                   |
| /30         | 2                   | 255.255.255.252 | 2^2 - 2 = 2                   |
| /31         | 1                   | 255.255.255.254 | 2^1 = 2 (point-to-point only) |
| /32         | 0                   | 255.255.255.255 | 1 (host address only)         |


**HUOMAUTUS**: RFC 950:ssä on aiemmin kehotettu käyttämään aliverkon nollaa, lähinnä reitityksen sekaannusten välttämiseksi.  Tämä rajoitus poistui käytöstä RFC 1878:n myötä, joka sallii sen käytön täysin. Vanha rajoitus johtui lähinnä yhteensopimattomuudesta vanhempien laitteistojen kanssa, jotka eivät pystyneet käsittelemään CIDR:ää oikein. Nykyaikaisilla laitteilla ei ole tällaista ongelmaa.


Esimerkiksi aliverkko **1.0.0.0.0**, jonka aliverkon peite on **255.255.0.0.0** ja joka oli aiemmin moniselitteinen A-luokan verkkotunnuksen kanssa, on nyt täysin pätevä ja käyttökelpoinen.


**TIP**: virheettömiin aliverkkolaskelmiin ja osoitteiden nopeaan muuntamiseen CIDR-merkintämuotoon on olemassa käteviä työkaluja, kuten ***ipcalc***. Tämä "verkkolaskin" näyttää selvästi Address-jakautumat, käytettävissä olevat alueet ja niihin liittyvät maskit, mikä on ihanteellinen apuväline sekä ylläpitäjille että CIDR:ää opetteleville opiskelijoille.


```shell
sudo apt install ipcalc
```


https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d

## TCP-protokolla


<chapterId>860bf7d5-a502-4d10-a12c-9827f6c2d393</chapterId>



**TCP-protokolla** (_Transmission Control Protocol_) on keskeisessä asemassa TCP/IP-mallin TRANSPORT Layer:ssä. Se toimii siltana sovellusten ja Internet Layer:n välillä ja varmistaa luotettavan tiedonsiirron kahden kaukana olevan koneen välillä.

Kun IP-protokolla vain lähettää paketteja takaamatta niiden toimitusta tai järjestystä, TCP varmistaa tietovirran eheyden ja johdonmukaisuuden, toimittamalla sen häviöttömästi, oikeassa järjestyksessä ja ilman päällekkäisyyksiä.


TCP:n päävastuualueisiin kuuluvat:


- Vastaanotettujen segmenttien uudelleenjärjestäminen;
- Tietovirran seuranta ruuhkien välttämiseksi;
- Tietolohkojen jakaminen tai kokoaminen uudelleen sopiviksi yksiköiksi (segmenteiksi);
- Yhteyksien luomisen ja lopettamisen hallinta viestinnän molempien päiden välillä.


TCP on yhteyspainotteinen protokolla, mikä tarkoittaa, että se luo selkeän, jatkuvan suhteen asiakkaan ja palvelimen välille. Tätä varten se käyttää **sarjanumeroita** ja **vahvistuksia**: jokaiselle lähetetylle segmentille annetaan yksilöllinen tunniste, jotta vastaanottava kone voi tarkistaa sekä datan järjestyksen että eheyden. Vastaanottaja lähettää sitten kuittaussegmentin, jonka **ACK-lippu** on asetettu arvoon 1, mikä vahvistaa vastaanoton ja osoittaa seuraavan odotetun järjestysnumeron.



![Image](assets/fr/018.webp)



Luotettavuuden parantamiseksi TCP käyttää ajastinta: kun segmentti lähetetään, alkaa lähtölaskenta. Jos kuittaus ei saavu aikakatkaisun aikana, lähettäjä lähettää segmentin automaattisesti uudelleen olettaen, että se on kadonnut kuljetuksen aikana. Tämä automaattinen uudelleenlähetysmekanismi kompensoi IP-verkoille ominaisia menetyksiä, joita voi esiintyä ruuhkautumisen, reititysvirheiden tai laitteistovikojen yhteydessä.



![Image](assets/fr/019.webp)



TCP pystyy havaitsemaan ja käsittelemään kaksoiskappaleet. Jos uudelleenlähetetty segmentti saapuu, mutta myös alkuperäinen segmentti näkyy, vastaanotin käyttää järjestysnumeroita tunnistamaan kaksoiskappaleen ja säilyttää vain oikean kopion, jolloin kaikki epäselvyydet poistuvat.


Jotta tämä prosessi toimisi, molemmilla koneilla on oltava yhteinen käsitys alkuperäisistä järjestysnumeroista. Tämä varmistetaan noudattamalla tiukkaa yhteysmenettelyä: toisaalta **palvelin** kuuntelee tietyssä portissa ja odottaa saapuvaa pyyntöä (passiivinen tila); toisaalta **asiakas** aloittaa yhteyden aktiivisesti lähettämällä pyynnön palvelimelle samaan palveluporttiin.


**HUOMAUTUS**: Portti on tietokoneen verkkosovellukselle annettu numeerinen tunniste (0-65 535). Sitä käytetään erottamaan toisistaan useita palveluja, jotka toimivat samanaikaisesti samalla IP Address:lla. Kun asiakas lähettää tietoja, se määrittää porttinumeron, jotta palvelimen käyttöjärjestelmä tietää, minkä ohjelman pitäisi vastaanottaa tiedot (esim. 80 HTTP:lle, 443 HTTPS:lle, 25 SMTP:lle). Portit toimivat kuin omat ovet, jotka ohjaavat liikennettä sisään ja ulos, estävät sekaannukset palveluiden välillä ja mahdollistavat hienojakoisen pääsynvalvonnan palomuurien tai suodatussääntöjen avulla.


Exchange:n sekvenssisynkronointi perustuu kuuluisaan **"*kolmitoimiseen kädenpuristukseen*"**, joka on samanlainen kuin tapa, jolla kaksi ihmistä tervehtii toisiaan kontaktin luomiseksi. Tämä TCP:n luotettavuuden varmistava alustusvaihe tapahtuu kolmessa vaiheessa:

1. **SYN:** Asiakas lähettää alustavan synkronointisegmentin (**SYN**), jossa on asetettu asianmukainen lippu ja alustava sekvenssinumero (esim. C);

2. **SYN-ACK:** Vastaanottava palvelin vastaa kuittaussegmentillä (**SYN-ACK**), se kuittaa asiakkaan sekvenssinumeron ja antaa oman alkuperäisen sekvenssinumeronsa;

3. **ACK:** Asiakas lähettää lopullisen kuittauksen (**ACK**), jolla vahvistetaan palvelimen sekvenssinumeron vastaanottaminen ja synkronointi viimeistellään. SYN-lippu on nyt poistettu käytöstä ja ACK-lippu pysyy asetettuna osoittaen, että yhteys on muodostettu.



![Image](assets/fr/020.webp)



Tämä Exchange-protokolla varmistaa, että molemmat osapuolet käyttävät samaa numerointipohjaa ennen hyötykuorman tietojen lähettämistä. Kun tämä synkronointi on suoritettu, istunto avataan: segmentit voivat nyt kulkea molempiin suuntiin, ja kukin segmentti kuitataan vastaanoton yhteydessä, mikä takaa tietovirran maksimaalisen luotettavuuden.


Tämä ***kolmensuuntainen kättely*** koskee vain yhteyden muodostamista. Sulkeutumiseen TCP käyttää *neljänsuuntaista kättelyä*: FIN → ACK → FIN → ACK, joka takaa, että yhtään kulkevaa segmenttiä ei menetetä ennen kuin yhteys on kokonaan purettu.


Vaikka tämä prosessi on suunniteltu kestäväksi ja luotettavaksi, se on myös aiheuttanut haavoittuvuuksia, joita voidaan käyttää hyväksi. Esimerkiksi hyökkäyksillä, kuten **IP Spoofing**, pyritään ohittamaan tai turmelemaan tämä luottamussuhde esiintymällä valtuutettuna koneena väärennettyjen sekvenssinumeroiden avulla, jolloin syntyy tietoturva-aukko, joka mahdollistaa tietovirran sieppaamisen tai manipuloinnin.


Sekvenssin synkronoinnin kaappaamisen riskien rajoittamiseksi ja verkon kuormituksen hallitsemiseksi TCP-protokolla käyttää virranhallintatekniikkaa, joka tunnetaan nimellä "**_Sliding Window_**". Tämä järjestelmä säätelee, kuinka paljon dataa voidaan lähettää ilman, että jokaisesta segmentistä vaaditaan välitön kuittaus, mikä vähentää verkon tarpeetonta ylikuormitusta ja säilyttää samalla hyvän luotettavuuden.


Käytännössä liukuva ikkuna määrittelee sekvenssinumeroiden alueen, joka voi kiertää vapaasti lähettäjän ja vastaanottajan välillä ilman, että jokaista yksittäistä segmenttiä kuitataan. Kun lähettävä järjestelmä vastaanottaa kuittauksia, ikkuna "liukuu": se liukuu oikealle ja tekee tilaa uusille lähetettäville segmenteille. Tämän ikkunan koko (joka on ratkaisevan tärkeä läpäisykyvyn optimoimiseksi ja ruuhkien välttämiseksi) määritetään TCP-otsikon "*Window*"-kentässä.


**Esimerkki**: jos alkuperäinen järjestysnumero on 3 ja ikkuna ulottuu järjestykseen 5, voidaan lähettää segmentit numeroilla 3-5 odottamatta yksittäisiä kuittauksia.



![Image](assets/fr/021.webp)



Liukuikkunan koko ei ole kiinteä, vaan se mukautuu dynaamisesti verkko-olosuhteiden ja vastaanottimen käsittelykapasiteetin mukaan.  Jos vastaanotin pystyy käsittelemään suuremman tietomäärän, se ilmoittaa siitä Window-kentän kautta, jolloin lähettäjä voi laajentaa ikkunaansa. Jos taas ylikuormituksessa tai kyllästymisvaarassa vastaanotin voi pyytää pienentämistä, lähettäjä odottaa, että ikkuna siirtyy eteenpäin, ja lähettää lisää segmenttejä.


Protokolla tarjoaa symmetrisen menettelyn TCP-yhteyden sulkemiseen, jotta varmistetaan puhdas ja asianmukainen sulkeminen. Kumpikin kone voi aloittaa yhteyden sulkemisen lähettämällä segmentin, jonka **FIN**-lippu on asetettu arvoon 1, mikä ilmaisee aikomuksensa lopettaa yhteys. Tämän jälkeen se odottaa, kunnes kaikki siirtosegmentit on vastaanotettu, ja jättää kaikki muut tiedot huomiotta.


Vastaanotettuaan tämän segmentin toinen kone lähettää kuittauksen, jossa on myös FIN-merkki. Tämän jälkeen se lähettää loputkin tiedot ennen kuin se ilmoittaa paikalliselle sovellukselle, että yhteistoiminta on suljettu. Tämä kaksinkertainen vahvistus varmistaa järjestelmällisen sulkemisen ja minimoi tietojen häviämisen riskin.


Tätä tarkkaa hallintaa, jossa yhdistyvät IP:n joustava reititys ja TCP:n tiukka valvonta, havainnollistetaan usein kaaviolla, jossa vastakkain asetetaan IP-protokollan nopeus (joka toimii **"best effort "** -periaatteella ilman toimitustakuuta) ja TCP-protokollan luotettavuus (joka hallinnoi siirtoa kuittausten ja neuvoteltujen sekvenssien avulla).



![Image](assets/fr/022.webp)



Joissakin tapauksissa absoluuttinen luotettavuus ei kuitenkaan ole etusijalla, vaan nopeus ja yksinkertaisuus. Tämä pätee esimerkiksi suoratoiston tai VoIP:n kaltaisiin sovelluksiin, jotka voivat sietää jonkin verran pakettihäviöitä ilman, että se vaikuttaa vakavasti käyttökokemukseen. Tällaisissa tapauksissa **UDP** (_User Datagram Protocol_) on parempi vaihtoehto.


UDP:n toimintaperiaate eroaa olennaisesti TCP:stä: se on **yhteydetön**, mikä tarkoittaa, että lähettäjän ja vastaanottajan välille ei ole luotu mitään edeltävää suhdetta. Kun kone lähettää paketteja UDP:n kautta, ne lähetetään vain yhteen suuntaan; vastaanottaja ei lähetä kuittauksia, eikä lähettäjä saa vahvistusta viestin saapumisesta. UDP-otsikko on tarkoituksellisesti minimaalinen, sillä se sisältää vain lähdeportin, kohdeportin, segmentin pituuden ja tarkistussumman, eikä siinä ole sisäänrakennettua kuittaus- tai tilanvalvontamekanismia. Kuten aina, IP-osoitteet sisältyvät taustalla olevaan IP-otsikkoon.


Yleinen vertaus on, että TCP on kuin **puhelu**, jossa virtapiiri muodostetaan, sitä seurataan ja valvotaan koko keskustelun ajan. UDP-protokolla taas on kuin **postin lähettäminen**, jossa lähettäjä sujauttaa kirjeen postilaatikkoon ilman välitöntä todistetta toimituksesta tai järjestelmällistä palautetta.


TCP:n ja UDP:n keskinäinen täydentävyys mahdollistaa sen, että nykyaikaiset verkot voivat mukautua erilaisiin tarpeisiin ja valita sovelluksesta riippuen joko maksimaalisen luotettavuuden tai nopeuden.



## Palvelun alkutekijät


<chapterId>4480afb7-e950-4ccb-88fa-d132f9dc3479</chapterId>



### Kerrosarkkitehtuuri ja Exchange-organisaatio


Kuten olemme nähneet, **palvelut** ovat tähän mennessä kuvaamiemme protokollien konkreettinen toteutus. Vaikka TCP/IP-malli eroaa **OSI**-mallista, siinä käytetään samaa kerroksittaista lähestymistapaa: jokainen Layer on suunniteltu suorittamaan tietty toiminto ja tarjoamaan **palveluita** suoraan sen yläpuolella olevalle Layer:lle, mikä johtaa modulaariseen, vankkaan ja helposti ylläpidettävään arkkitehtuuriin.


Kukin Layer rakentuu sen alapuolella olevan Layer:n ominaisuuksien varaan, ja se puolestaan tarjoaa yläpuolella olevalle Layer:lle johdonmukaisen Interface:n tietojen hallintaa varten. Tässä arkkitehtuurissa jokaisella Layer:llä on omat **tietorakenteensa**, jotka on määritelty huolellisesti täydellisen yhteensopivuuden varmistamiseksi muiden kerrosten kanssa. Yhteensopivuus on olennaisen tärkeää sujuvan, luotettavan ja selkeän viestinnän kannalta päätepisteestä toiseen.


Vaihtoa ohjaavat kaksi keskeistä näkökohtaa:


- Pystysuunta**: yhden Layer:n ja sen ylä- tai alapuolella olevan Layer:n välinen suhde (Layer N:stä Layer N+1:ään ja päinvastoin).



![Image](assets/fr/023.webp)




- Horisontaalinen näkökulma**: etäsovellusten välinen vuorovaikutus eli **asiakkaan** ja **palvelimen** välinen vuoropuhelu kumpaankin suuntaan.



![Image](assets/fr/024.webp)



Kerrosarkkitehtuurissa noudatetaan periaatetta, jonka mukaan kukin Layer käsittelee vain sen toimialueeseen kuuluvia tietoja: tietorakenteet, otsikot ja valvontamekanismit vaihtelevat Layer:sta toiseen, mutta yhdessä ne muodostavat yhtenäisen järjestelmän, joka varmistaa, että tiedot ohjautuvat asteittain lopulliseen määränpäähänsä.


**Muistutus**: Käytetään erityistä terminologiaa kuvaamaan kerrosten välillä vaihdettavia tietoyksiköitä:


- gW-67-sovelluksen viesti**,
- segmentti** Transport Layer:lle (TCP),
- datagrammi** Internet Layer:lle (IP),
- kehys** Network Access Layer:lle.


Alla olevassa taulukossa on yhteenveto TCP- ja UDP-yhteyksien termeistä:


| TCP/IP Layer         | Unit Name (TCP) | Unit Name (UDP) |
|----------------------|------------------|------------------|
| Application Layer    | Stream           | Message          |
| Transport Layer      | Segment          | Packet           |
| Internet Layer       | Datagram         | Datagram         |
| Network Access Layer | Frame            | Frame            |

### Palvelun alkuosat ja datayksiköt


Järjestelmän ytimessä ovat **palveluprimitiivit**, jotka toimivat viestintärajapintoina. Nämä alkuosat toimivat kuin palvelupisteet, jotka kuuntelevat varattuja erityisiä **portteja** ja antavat prosesseille mahdollisuuden luoda, ylläpitää ja lopettaa verkkoyhteyksiä hallitusti. Vaikka protokollat järjestävät datan muodon ja siirron verkon yli, **palvelut ja niiden alkuosat** muodostavat vertikaalisen linkin kerrosten välille.


Yhdistämällä horisontaalinen näkökulma (hajautettujen sovellusten välinen viestintä) ja vertikaalinen näkökulma (kerrosten välinen sisäinen vuorovaikutus) TCP/IP-malli tarjoaa täydellisen, skaalautuvan arkkitehtuurin. Näiden kahden näkökulman päällekkäisyys antaa selkeän yleiskuvan siitä, miten tietoja vaihdetaan strukturoidussa verkkoviestinnässä.



![Image](assets/fr/026.webp)



### Osan yhteenveto


Tässä ensimmäisessä pääjaksossa tarkastelimme keskeistä arkkitehtuuria, joka ohjaa nykyisten Internetiin yhdistettyjen verkkojen konfigurointia ja toimintaa. Tämä arkkitehtuuri perustuu **neljän Layer:n malliin**, joka on saanut vaikutteita OSI-mallista, ja se on rakennettu **TCP/IP**-protokollapaketin ympärille, joka on nykyaikaisen tietoliikenteen selkäranka. Näimme, että TCP varmistaa yhteyskeskeisellä lähestymistavallaan luotettavan siirron, kun taas UDP on kevyempi ja nopeampi ja sitä suositaan silloin, kun nopeus on tärkeämpää kuin luotettavuus.


Tämän mallin moitteeton toiminta perustuu protokollien toteuttamiseen **palvelun alkuosien** avulla. Nämä varmistavat kerrosten välisen yhteyden, jonka avulla tietojenkäsittely voidaan mukauttaa kunkin tason erityisvaatimuksiin kuljetuksesta sovellukseen, mukaan lukien Internet- ja verkkoyhteydet. Tämä modulaarinen lähestymistapa tekee järjestelmästä sekä joustavan että kestävän.


IP-osoitteet ovat tämän infrastruktuurin toinen kulmakivi. Jokainen liitetty laite tunnistetaan **yksilöllisellä Address-IP-tunnuksella**, joka otetaan Address-avaruudesta, joka on järjestetty **luokkiin** (A:sta E:hen). Jotkin näistä osoitteista on varattu erityistarkoituksiin, kuten paikalliseen loopback- tai multicast-osoitteeseen, kun taas toisia, niin sanottuja "yksityisiä osoitteita", ei reititetä Internetissä ilman kääntämistä (NAT). Tämä luokittelu mahdollistaa verkkojen loogisen, hierarkkisen organisoinnin.


Tutustuimme myös **alaverkkojen** käsitteeseen, joka mahdollistaa verkon segmenttien jakamisen IP-resurssien paremman hallinnan ja tietovirran optimoinnin varmistamiseksi. Vaikka manuaalinen aliverkon jakaminen aliverkkomaskien avulla on edelleen tärkeä periaate, se on suurelta osin nykyaikaistettu **CIDR**:n (_Classless Inter-Domain Routing_) ansiosta. Tämä menetelmä on muuttanut Address:n hallintaa mahdollistamalla IP-alueiden joustavamman ja järkevämmän jakamisen ja vähentämällä samalla reititystaulukoiden kokoa.


Kun hallitset nämä käsitteet - kerrokset, protokollat, palvelun alkuosat, osoitteet ja aliverkot - saat vankan perustan nykyaikaisten verkkojen teknisen toiminnan ymmärtämiselle ja verkkoinfrastruktuurin tehokkaalle konfiguroinnille nykypäivän tarpeita varten.


Seuraavassa jaksossa tarkastelemme IPv4-osoitteita lähemmin.



# IPv4-osoitteet


<partId>83f3c3e5-378c-440f-a095-df210842efde</partId>



## IPv4:n käyttö


<chapterId>79e4dd18-446a-435b-9f25-c88a00f8bec6</chapterId>



Tässä jaksossa menemme syvemmälle ja tarkastelemme, miten **IPv4**-osoitteet todella toteutetaan todellisessa verkossa. Analysoimme niiden muodon, niiden taustalla olevan logiikan ja sen, miten ne liittyvät muihin tärkeimpiin verkon Elements:ään, kuten **DNS-nimiin**, **MAC-osoitteisiin**, **alaverkkoihin** ja **kääntämistekniikoihin**.


IP Address on yksilöllinen numeerinen tunniste, joka on osoitettu jokaiselle **verkon Interface** laitteelle. Sen avulla laite voidaan paikantaa verkossa ja tavoittaa se tietojen lähettämistä varten. Esimerkiksi reitittimellä, palvelimella, työasemalla, verkkotulostimella tai jopa valvontakameralla on vähintään yksi oma IP Address. IP Address mahdollistaa **reitityksen** eli pakettien siirtämisen pisteestä A pisteeseen B, vaikka ne olisivat fyysisesti kaukana toisistaan.


IP-osoitteita voidaan määrittää kahdella tavalla:


- Staattinen**: Manuaalisesti asetettu laitteeseen.
- Dynaaminen**: DHCP-palvelin (_Dynamic Host Configuration Protocol_) määrittää automaattisesti pyydettäessä. DHCP yksinkertaistaa verkonhallintaa, sillä se poistaa manuaalisen konfiguroinnin tarpeen ja mahdollistaa tarkan hallinnan varausten ja vuokrasopimusten keston avulla.


**IPv4**-osoitteet kirjoitetaan **32-bittisessä** muodossa, joka on jaettu **neljään tavuun**. Kukin tavu sisältää 8 bittiä ja edustaa desimaalilukua 0-255. Neljä tavua erotetaan toisistaan pisteillä selkeän ja luettavan merkintätavan muodostamiseksi.


esimerkki: Address 172.16.254.1_



![Image](assets/fr/027.webp)



Jokaisella tavun bitillä on arvo (tai "painoarvo"): vasemmanpuoleinen bitti (eniten merkitsevä bitti) on arvoltaan 128, seuraava 64, sitten 32, 16, 8, 4, 2 ja 1 oikeanpuoleinen bitti (vähiten merkitsevä bitti). Tällä tavoin binäärikirjoitus muunnetaan desimaalilukuun yksinkertaisesti laskemalla yhteen asetetut painot.


Seuraavassa taulukossa esitetään tämä vastaavuus:



| Binary Code | Activated Bit Values          | Decimal Value |
|-------------|-------------------------------|---------------|
| 00000000    | 0                             | 0             |
| 00000001    | 1                             | 1             |
| 00000011    | 1 + 2                         | 3             |
| 00000111    | 1 + 2 + 4                     | 7             |
| 00001111    | 1 + 2 + 4 + 8                 | 15            |
| 00011111    | 1 + 2 + 4 + 8 + 16            | 31            |
| 00111111    | 1 + 2 + 4 + 8 + 16 + 32       | 63            |
| 01111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64  | 127           |
| 11111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 | 255      |

Kun haluat muuntaa binäärin desimaaliluvuksi, lisää niiden bittien painot, jotka on asetettu arvoon 1.


| Binary     | Decimal Value |
| ---------- | ------------- |
| `10101100` | 172           |
| `00010000` | 16            |
| `11111110` | 254           |
| `00000001` | 1             |

IP Address yksilöi yksittäisen **verkon Interface**, ei koko laitetta. Moniporttisessa reitittimessä tai palomuurissa on useita liitäntöjä, joista jokaisella on oma IP Address. Yhdellä Interface:lla voi olla jopa useita IP-osoitteita (esimerkiksi useiden virtuaaliverkkojen tai -palveluiden palvelemiseksi).


Jokaisen IP-paketin otsikossa on kaksi IP-osoitetta:


- Lähde Address (**lähettäjä**)
- Määränpää Address (**vastaanotin**)

Reitittimet lukevat näitä osoitteita selvittääkseen parhaan reitin paketin lähettämiseksi määränpäähän asti. Ilman tiukkoja osoitesääntöjä verkkoliikennettä ei voitaisi reitittää oikein, ja verkkojen maailmanlaajuinen yhteenliittäminen olisi mahdotonta.


IPv4 Address:ssa on kaksi osaa:


- NetID**: tunnistaa verkon
- HostID**: yksilöi laitteen kyseisessä verkossa

Aliverkon peite** määrittää, mihin NetID päättyy ja mistä HostID alkaa, ja määrittää, kuinka monta bittiä kuhunkin osaan kuuluu. Mitä pidempi NetID on, sitä suurempi on mahdollisten aliverkkojen määrä, mutta isäntien määrä aliverkkoa kohti vähenee vastaavasti.


Alun perin IPv4-verkot jaettiin viiteen **luokkaan**: (A, B, C, D ja E). Kukin luokka vastaa tiettyä NetID-aluetta ja määrittelee kiinteän rakeisuuden:


- Luokka A: erittäin suuret verkot, joissa on suuri määrä isäntiä
- Luokka B: keskisuuret verkot
- Luokka C: pienet verkot
- Luokka D: monilähetystä varten varatut osoitteet (_multicast_)
- Luokka E: kokeelliset osoitteet, joita ei käytetä tavanomaisessa osoitteistuksessa



| Class | Leading Bits | First Byte Range | Default Subnet Mask | Purpose                          |
| ----- | ------------ | ---------------- | ------------------- | -------------------------------- |
| A     | 0            | 0 – 127          | 255.0.0.0           | Very large networks              |
| B     | 10           | 128 – 191        | 255.255.0.0         | Medium-sized networks            |
| C     | 110          | 192 – 223        | 255.255.255.0       | Small networks                   |
| D     | 1110         | 224 – 239        | N/A                 | Multicast addresses              |
| E     | 1111         | 240 – 255        | N/A                 | Experimental (not publicly used) |

Erityispuheenvuorot:


- Verkko Address**: Tunnistaa itse verkon (käytetään reititystaulukoissa).
- Lähetys Address**: Lähettää tietoja kaikille aliverkon laitteille kerralla (kaikki HostID-bitit asetettu arvoon 1).


Seuraavat alueet on varattu sisäiseen käyttöön:


- 10.0.0.0/8** (yksityinen A-luokka)
- 127.0.0.0/8** (paikallinen loopback tai _loopback_)
- 172.16.0.0 - 172.31.255.255** (yksityinen luokka B)
- 192.168.0.0 - 192.168.255.255** (yksityinen luokka C)


Osoitteita **127.0.0.1** ja yleisemmin koko 127.0.0.0/8-aluetta käytetään sisäiseen testaukseen: kaikki niihin lähetetyt pyynnöt eivät koskaan poistu koneelta. Tämä on hyödyllistä, kun halutaan tarkistaa, että paikallinen verkkopalvelu toimii ilman, että laajempi verkko on mukana.


Jotta Address-avaruutta voitaisiin hyödyntää paremmin, järjestelmänvalvojat jakavat verkot usein **alaverkkoihin** käyttämällä aliverkkomaskkeja tai **CIDR**-merkintää (__Classless Inter-Domain Routing_). CIDR mahdollistaa tarkemman hallinnan ja auttaa välttämään osoitteiden tuhlaamista. Nykyään CIDR on välttämätön IP-alueiden hienosäätämisessä ja reititystaulujen koon pienentämisessä.


Nykyaikaisissa verkoissa IP-osoite on yleensä yhdistetty muihin tunnisteisiin:



- verkkotunnus**, joka on rekisteröity **DNS:ään** (_Domain Name System_): Se yhdistää numeerisen IP Address:n ihmisystävälliseen nimeen.
- MAC Address**: verkkokorttiin kaiverrettu fyysinen tunniste, jota käytetään paikalliseen siirtoon (_Ethernet_). Kun IP-paketti on lähetettävä fyysisesti, ARP-taulukko vertaa IP Address:ää määränpään MAC Address:ään.


IPv4 Address -vajeesta selviytymiseksi ja Layer -turvan lisäämiseksi verkot käyttävät usein Address-kääntämistä (_NAT_). NAT mahdollistaa sen, että monet yksityiset laitteet voivat käyttää yhtä julkista Address IP-osoitetta, kun ne käyttävät Internetiä.


**Huomautus**: Verkkotyökalut ja käyttöjärjestelmän sisäänrakennetut työkalut, kuten [Grenoblen CRIC-laskin](http://cric.grenoble.cnrs.fr/Administrateurs/Outils/CalculMasque/), helpottavat aliverkon ja maskin laskentaa huomattavasti.

Nämä apuohjelmat auttavat suunnittelemaan verkon jakamisen tehokkaasti.


Yhteenvetona voidaan todeta, että broadcast Address on edelleen käytännöllinen toiminto saman viestin lähettämiseksi kaikille segmenttiin liitetyille laitteille: tämä saavutetaan asettamalla kaikki HostID-osan bitit arvoon 1, jolloin kaikki isännät ovat kohteena.



## IPv4 Address:n eri tyypit


<chapterId>2adfad24-a90d-45b5-b808-3d2f6598bebf</chapterId>



IPv4-osoitteet jaetaan kahteen pääluokkaan: julkisiin osoitteisiin, jotka ovat suoraan saatavilla Internetissä, ja yksityisiin osoitteisiin, jotka on tarkoitettu sisäiseen käyttöön paikallisverkossa.


Julkinen IPv4 Address on maailmanlaajuisesti yksilöllinen ja reititettävissä koko Internetissä. Viranomaiset myöntävät sen, ja sitä tarvitaan julkisiin palveluihin, kuten verkkosivustoihin, sähköpostipalvelimiin tai pilvipalveluihin.

Näiden osoitteiden maailmanlaajuinen ainutlaatuisuus on välttämätöntä reititysristiriitojen tai törmäysten välttämiseksi.


**ICANNin** (_Internet Corporation for Assigned Names and Numbers_) alaisuudessa toimiva **IANA** (_Internet Association for Assigned Names and Numbers_) hallinnoi näiden IP-alueiden jakelua. Konkreettisesti IANA jakaa IPv4-alueen 256 lohkoon, joiden koko on /8, CIDR-notaation mukaisesti. Kukin lohko edustaa hieman yli 16,7 miljoonaa osoitetta (2³² / 2⁸).


IANA on antanut nämä unicast Address -lohkot **alueellisten Internet-rekisterien** (RIR) käyttöön. Nämä RIR:t vastaavat osoitteiden uudelleenjakelusta alueellisella tasolla liittymäpalvelujen tarjoajien, yritysten tai hallintojen todellisten tarpeiden mukaan. Unicast Address -alue ulottuu lohkoista **1/8-223/8**, ja osa siitä on joko varattu erityiskäyttöön (tutkimus, dokumentointi, testaus) tai jaettu suoraan verkolle tai RIR:lle uudelleenjakelua varten.


Voit tarkistaa, kuka omistaa julkisen IP Address -osoitteen, käyttämällä RIR-tietokantoja komennolla **whois** tai kunkin rekisterin tarjoamia web-käyttöliittymiä. Näiden työkalujen avulla Address voidaan jäljittää sen ilmoittaneeseen organisaatioon tai palveluntarjoajaan.


Toisaalta on olemassa yksityisiä IPv4-osoitteita, jotka ovat käytännön vastaus julkisten osoitteiden puutteeseen. Nämä osoitteet, jotka eivät ole reititettävissä Internetissä, on varattu paikallisiin ympäristöihin: yritysverkkoihin, kotien lähiverkkoihin, datakeskuksiin tai tietokoneklustereihin. Ne eivät ole ainutlaatuisia maailmanlaajuisesti: monet yksityiset verkot voivat käyttää samoja IP-alueita ilman häiriöitä, kunhan ne pysyvät eristyksissä tai käyttävät Address-verkkokääntäjälaitetta Internetiin pääsemiseksi.


Jotta laite, jolla on yksityinen IP Address, voi käyttää Internetiä, verkot käyttävät NAT:ia (Network Address Translation). NAT toimii siten, että yksityinen Address korvataan dynaamisesti julkisella Address:lla, jolloin kymmenet (tai jopa sadat) laitteet voivat jakaa yhden julkisen IP Address:n. Tämä menetelmä optimoi IPv4-tilan käytön ja lisää myös Layer-turvallisuutta piilottamalla sisäisen verkon rakenteen.


Toinen erityisluokka on **määrittelemättömät** osoitteet. IPv4-merkintä **0.0.0.0.0** tai sen IPv6-versio **::/128** tarkoittaa "ei erityistä Address". Tällainen Address ei kelpaa verkon Address-kohteeksi, mutta isäntä voi käyttää sitä paikallisesti ilmaisemaan "kaikki rajapinnat" tai "ei vielä määritettyä Address:ää". Tämä on yleistä DHCP:n dynaamisessa Assignment:ssa tai kaikkien palvelinrajapintojen kuuntelussa.


IPv6 tukee myös yksityistä osoitteistusta, mutta standardi suosittelee yleensä julkista osoitteistusta, jotta vältetään useiden NAT-kerrosten pinoaminen. Lohkon **fec0::/10** **sivuston paikalliset osoitteet** (_site-local_) poistettiin käytöstä **RFC 3879**:ssä** johdonmukaisuuteen ja turvallisuuteen liittyvistä syistä. Ne korvattiin **yksilöllisillä paikallisilla osoitteilla** (_ULA_), jotka sijaitsevat **fc00::/7**-lohkossa. ULA:t mahdollistavat yksityisten IPv6-verkkojen luomisen, joissa on puhdas sisäinen reititys ja joissa käytetään satunnaisesti luotua 40-bittistä tunnusta paikallisen ainutlaatuisuuden varmistamiseksi.


IPv4:n loppuminen vahvistettiin virallisesti vuonna 2011. Internet-yhteisö on ottanut käyttöön useita strategioita pidentääkseen IPv4:n käyttöikää:


- Asteittainen siirtyminen **IPv6:een**
- **NAT**:n laaja käyttö
- RIR:ien tiukemmat jakopolitiikat, jotka edellyttävät tarkkaa perustelua ja Address-tarpeiden hallintaa
- Yritysten käyttämättömien tai vapaaehtoisesti palauttamien Address-lohkojen takaisinperintä


Nämä toimenpiteet osoittavat, että IP-osoitteet eivät ole vain tekninen haaste vaan myös maailmanlaajuinen hallintoasia, joka on keskeinen Internetin jatkuvan laajentumisen kannalta.



## DNS, Address-hakemisto


<chapterId>511244ec-ba43-44ac-b4c3-b41579a15cff</chapterId>



Olkaamme rehellisiä, ihmiset eivät ole hyviä muistamaan pitkiä numerosarjoja, olivatpa ne sitten binääri- tai desimaalimuodossa. Tämä haaste kasvaa entisestään IP-osoitteiden kohdalla, sillä ne voivat olla monimutkaisia, ja yksi IP Address voi joskus peittää useita osoitteita, varsinkin kun mukana on NAT:n tai virtuaalisen isännöinnin kaltaisia tekniikoita.


Asioiden helpottamiseksi Application Layer käyttää järjestelmää, joka yhdistää IP Address:n loogiseen, ihmisen luettavissa olevaan nimeen. Tämä on **DNS** (*Domain Name System*), massiivinen, hierarkkinen, hajautettu hakemisto, joka yhdistää luettavat verkkotunnukset IP-osoitteisiin. Järjestelmä perustuu protokolliin ja palveluihin. Yleisimmin käytetty DNS-palvelinohjelmisto on **BIND** (_Berkeley Internet Name Domain_), avoimen lähdekoodin ohjelmistopaketti, jossa viitataan suurimpaan osaan Internetin DNS-infrastruktuurista.


DNS:n perusajatus on yksinkertainen: jokaiselle yhdistetylle palvelulle, olipa kyseessä verkkosivusto, sähköpostipalvelin tai muu verkkopalvelu, on olemassa tietue, joka yhdistää verkkotunnuksen nimen yhteen tai useampaan IP-osoitteeseen. Tämä toimii kahteen suuntaan:


- Forward resolution: nimen muuntaminen IP-osoitteeksi Address.
- Käänteinen resoluutio: tiettyyn IP-osoitteeseen liittyvän verkkotunnuksen löytäminen Address.

Tämä tekee verkko-osoitteistosta käyttökelpoisen ihmisille ja säilyttää samalla reitittimien tarkkuuden, jota ne tarvitsevat tietojen siirtämiseen oikein.


Verkkotunnus on aina hierarkkinen, ja jokainen taso erotetaan pisteellä: koko nimeä kutsutaan **FQDN** (_Fully Qualified Domain Name_). Oikeanpuoleisin osa on **TLD** (_Top Level Domain_), kuten `.com`, `.org` tai `.fr`. Vasemmanpuoleisin osa tarkoittaa isäntäkonetta eli tiettyä konetta tai palvelua, joka on yhdistetty IP Address:aan.


DNS-järjestelmä on suunniteltu **vyöhykkeiden puuksi**. **Vyöhyke** on tietyn DNS-palvelimen hallinnoima osa verkkotunnuksen nimiavaruudesta. Yksittäinen vyöhyke voi sisältää useita **alivyöhykkeitä**, jotka voidaan delegoida toisille vyöhykkeille, joita eri palvelimet hallinnoivat. Järjestelmänvalvojat ovat vastuussa vyöhykkeidensä ylläpidosta: päivityksistä, delegoinnista ja yleisestä hallinnasta.


Tämän rakenteen avulla voidaan paitsi osoittaa pääverkkotunnukseen (esim. `example.com`), myös hienosäätää tietueita yksittäisille isännöintiasemille (`www`, `mail`, `ftp` jne.). Verkkoverkkojen alkuaikoina tämä kartoitus hoidettiin staattisilla tiedostoilla (`/etc/hosts` Unix-järjestelmissä), mutta tällainen menetelmä muuttui nopeasti epäkäytännölliseksi nopeasti kasvavassa, toisiinsa yhteydessä olevassa Internetissä.


On tärkeää ymmärtää, että **DNS-palvelin** voi palvella vain rajoitettua aluetta. Esimerkiksi yrityksen sisäinen DNS-palvelin ei välttämättä ole suoraan käytettävissä Internetistä. Jos tätä DNS-palvelinta ei ole määritetty välittämään kyselyitä tai sillä ei ole luotettavaa suhdetta muihin palvelimiin, jotkin kyselyt epäonnistuvat: silloin nimeä tai IP Address:ää ei voida ratkaista määritetyn vyöhykkeen ulkopuolella.


DNS:llä on merkitystä myös sähköpostin reitityksessä. Esimerkiksi **MX** (_Mail Exchange_) -tietue määrittää sähköpostipalvelimet, jotka vastaavat tietyn verkkotunnuksen sähköpostien vastaanottamisesta. Nämä tietueet määrittelevät prioriteetit (painotuskerroin) ja vikasietoratkaisut. DNS-palvelimen vyöhyketiedoston on sisällettävä **SOA** (_Start Of Authority_) -tietue, joka määrittää palvelimen kyseisen vyöhykkeen viralliseksi tietolähteeksi.


Hierarkkisen, hajautetun rakenteensa ansiosta DNS on edelleen Internetin kulmakivi, jonka ansiosta käyttäjät voivat käyttää palveluja selkeiden, mieleenpainuvien verkkotunnusten kautta pitkien, teknisten IP-osoitteiden sijaan.


Seuraavassa luvussa tarkastelemme toista peruskäsitettä: **Ethernet-osoitteet**, jotka tunnetaan myös nimellä **MAC-osoitteet**, jotka varmistavat tietojen toimittamisen lähiverkkojen fyysisessä Layer:ssä.



## Ethernet-osoitteiden ja ARP:n löytäminen


<chapterId>d02109f6-9bf9-4261-a8f9-e1aa4398b949</chapterId>



### Määritelmät


Jotta tiedonsiirtoprotokolla toimisi luotettavasti ja johdonmukaisesti, yksi keskeinen komponentti on välttämätön. Ihmisinä voimme helposti tunnistaa koneen sen IP-osoitteen Address tai DNS:n kautta haetun nimen perusteella. Koneen on kuitenkin kyettävä yksiselitteisesti tunnistamaan kohdelaite pakettien toimittamista varten. Tätä varten se luottaa erityiseen laitteistotunnisteeseen, jota sen verkko Interface käyttää suoraan: MAC Address (_Media Access Control_).


**Huomautus**: Tämä ei liity mitenkään "fyysiseen Address:een" muistiarkkitehtuurissa. Tietojenkäsittelyssä fyysinen muisti Address viittaa tiettyyn paikkaan muistiväylällä, toisin kuin käyttöjärjestelmän hallinnoima virtuaalinen Address. MAC Address sen sijaan liittyy yksinomaan verkkolaitteistoon.


MAC Address on laitteen valmistajan pysyvä ja yksilöllinen osoitus. MAC Address tunnistaa yksiselitteisesti verkkokortin, olipa kyseessä tietokone, älypuhelin, tulostin tai mikä tahansa muu liitetty laite. Toisin kuin IP Address, joka voi muuttua dynaamisesti (DHCP-palvelimen tai manuaalisen konfiguroinnin kautta), MAC Address pysyy yleensä samana koko laitteen käyttöiän ajan, ellei sitä tarkoituksellisesti muuteta.


Jokaisella Interface-verkolla, langallisella tai langattomalla, on oma MAC Address. Tätä Address:ta käytetään datayhteyden Layer:ssä (OSI-mallin Layer 2) laitteiston Address:n lisäämiseen ja hallintaan jokaisessa vaihdetussa verkkokehyksessä. Tähän viitataan joskus nimellä _Ethernet-osoite_ tai _UAA_ (_Universally Administered Address_). Sen pituus on vakiintuneesti 48 bittiä eli 6 tavua, ja se kirjoitetaan heksadesimaalimerkinnöin, yleensä tavuina, jotka erotetaan toisistaan `:` tai `-`.


Esimerkiksi: "5A:BC:17:A2:AF:15"


Tässä rakenteessa kolme ensimmäistä tavua yksilöivät verkkokortin valmistajan: tämä tunnetaan nimellä **OUI** (*Organisationally Unique Identifier*). Näitä IEEE:n antamia etuliitteitä käytetään myös muissa laitteiston osoitusjärjestelmissä, kuten Bluetoothissa ja LLDP:ssä, maailmanlaajuisen yksikäsitteisyyden takaamiseksi.


### MAC-koodin muuttaminen Address (MAC-spoofing)


Teoriassa MAC Address on suunniteltu pysymään kiinteänä, mutta sitä voidaan muuttaa erityisesti erityistarpeiden täyttämiseksi tai tiettyjen rajoitusten kiertämiseksi. Tämä usein _spoofing MAC_ -nimellä kutsuttu toiminto tarkoittaa alkuperäisen laitteiston Address:n korvaamista eri arvolla, joka määritellään ohjelmistotasolla. Jotkin käyttöjärjestelmät helpottavat tätä muokkausta erityisesti silloin, kun ohjain ei suoraan käytä varsinaista Ethernet Address:ää.


Syyt tällaiseen muutokseen ovat moninaiset. Syynä voi olla esimerkiksi se, että tietty sovellus tarvitsee tietyn Ethernet Address:n toimiakseen oikein, tai se, että kahden samaa lähiverkkoa käyttävän laitteen väliset identtiset osoitteet ovat ristiriidassa.


MAC Address:n vaihtaminen voi johtua myös yksityisyyden suojaan liittyvistä näkökohdista: piilottamalla korttiin kaiverretun yksilöllisen tunnisteen käyttäjät vähentävät mahdollisuutta, että verkot tai valvontapalvelut voivat jäljittää heidän laitteensa. Tämä käytäntö ei kuitenkaan ole seurauksitta. MAC Address -kortin vaihtaminen voi häiritä tiettyjä suodatuslaitteita tai vaatia palomuurien uudelleenmäärittämistä, jotta uusi laitteisto voidaan hyväksyä.


Joissakin verkoissa, erityisesti Wi-Fi-verkoissa, käytetään MAC Address -suodatusta, joka sallii vain sellaisten laitteiden käytön, joilla on hyväksytty osoite. Vaikka tämä lisää valvonnan perustason, se ei ole yksinään turvallinen. Hyökkääjä voi kaapata verkossa jo hyväksytyn MAC Address -osoitteen ja kloonata sen rajoitusten kiertämiseksi. Tästä syystä MAC-suodatus on aina yhdistettävä vahvempiin turvatoimiin.


### MAC/IP-kirjeenvaihto


Jotta lähiverkko toimisi tehokkaasti, fyysisten osoitteiden (MAC-osoitteet) ja loogisten osoitteiden (IP-osoitteet) välillä on oltava selkeä vastaavuus. Ilman tätä yhteyttä tietokone saattaa tietää kohteen IP Address -osoitteen, mutta ei tiedä, miten fyysisesti lähettää siihen tietoja lähiverkossa.

ARP (_Address Resolution Protocol_) hoitaa tämän yhdistämisen automaattisesti.


Käytännössä, kun käyttäjä haluaa tietää tiettyä IP Address:ää vastaavan MAC Address:n, hän voi käyttää "arp"-apuohjelmaa. Tämä työkalu tarkistaa koneen paikallisen ARP-taulukon näyttääkseen IP-osoitteiden ja MAC-osoitteiden väliset tunnetut vastaavuudet lähiverkossa. Näin voidaan nopeasti tarkistaa loogisen ja fyysisen kerroksen välinen yhteys.


Käytännön esimerkki: jos haluat tarkistaa, mikä verkkokortti vastaa IP Address `192.168.1.5`, käytä seuraavaa komentoa:


```bash
arp –a 192.168.1.5
```


Tulosteessa näytetään siihen liittyvä fyysinen Address (MAC), syötteen luonne (staattinen tai dynaaminen) ja kyseinen Interface.


```
Interface: 192.168.1.5 --- 0x5
IP Address            MAC Address                Type
192.168.1.5           00:54:BC:17:14:6E          D
```


On tärkeää muistaa, että MAC Address ja IP Address ovat kaksi täysin erilaista tunnistetta, jotka kuitenkin täydentävät toisiaan. Valmistaja kaivertaa MAC Address:n ainutlaatuisesti jokaiseen Interface-verkkoon, ja sitä käytetään laitteen fyysiseen tunnistamiseen paikallisverkossa. IP Address on sitä vastoin looginen Address, joka annetaan joko dynaamisesti tai staattisesti ja jonka avulla laite voi liittyä IP-verkkoon ja Exchange-paketteja lähiverkon ulkopuolelle.



- Visuaalinen esimerkki MAC Address:stä:


![Image](assets/fr/032.webp)




- Visuaalinen esimerkki IP Address:sta:


![Image](assets/fr/027.webp)



Yritysympäristössä nämä kaksi osoitetasoa eivät voi toimia erillään toisistaan. Esimerkiksi kun DHCP-palvelin määrittää automaattisesti IP Address:n, lähtökohtana käytetään laitteen MAC Address:a. Tietokone lähettää DHCP-lähetyspyynnön, joka sisältää sen MAC Address:n, jotta palvelin voi määrittää käytettävissä olevan IP Address:n oikealle laitteelle. Ilman tätä laitteistotunnistusta DHCP-palvelin ei tietäisi, mille laitteelle Address olisi toimitettava.


ARP-protokolla on siis perustavanlaatuinen: se muodostaa yhteyden IP-osoitteiden ja fyysisten osoitteiden välille, jolloin koneet voivat muuntaa loogisen määränpään todelliseksi fyysiseksi määränpääksi. Kun tietokoneen on lähetettävä paketti samassa verkossa olevalle koneelle, se tarkistaa ensin ARP-taulukosta, onko vastaanottajan MAC Address jo tiedossa. Jos näin ei ole, se lähettää ARP-pyynnön kaikille lähiverkon isännille. Kone, joka tunnistaa IP Address-kohteen tässä pyynnössä, vastaa määrittämällä MAC Address:nsä. Tämän jälkeen lähettäjä kirjoittaa tämän IP/MAC-parin ARP-välimuistiinsa, jotta operaatiota ei tarvitse toistaa joka kerta, kun pyyntö lähetetään.


Tämä ARP-taulukko toimii minikartoitushakemistona, jota päivitetään dynaamisesti samalla tavalla kuin DNS yhdistää verkkotunnukset IP-osoitteisiin. Ilman ARP:tä ei olisi mahdollista käyttää paikallista Exchange:tä, koska datayhteyden Layer:n on tunnettava MAC Address, jotta Ethernet-kehykset voidaan kapseloida oikein.


Sitä vastoin RARP-protokolla (_Reverse Address Resolution Protocol_) on suunniteltu päinvastaiseen tilanteeseen: kone, joka tuntee vain MAC Address:nsa, voi löytää IP Address:nsa. Tämä oli yleistä vanhemmissa työasemissa, joissa ei ollut paikallista Hard-levyä ja joiden oli käynnistyttävä verkon kautta ja pyydettävä IP Address. RARP korvattiin lopulta **BOOTP**:llä ja sitten **DHCP:llä**, jotka ovat joustavampia ja automaattisempia.


Näillä yhdistelmäprotokollilla on tärkeä rooli reitityksessä. Reititin on pohjimmiltaan kone, jossa on useita verkkoliitäntöjä, jotka yhdistävät eri segmentit toisiinsa. Kun reititin vastaanottaa kehyksen, se käsittelee sen IP-datagrammin ja tutkii IP-otsikon määränpään määrittämiseksi. Jos kohde on suoraan liitetyssä verkossa, datagrammi toimitetaan suoraan otsikon päivittämisen jälkeen. Jos kohde kuuluu toiseen verkkoon, reititin käyttää reititystaulukkoa selvittääkseen parhaan reitin eli _next hop_, joka johtaa kohteeseen.


Tämä jakaa reitin lyhyempiin, helpommin hallittaviin osiin. Kukin välireititin tietää vain seuraavan vaiheen, ei välttämättä lopullista määränpäätä.


**Muistutus:** Suora toimitus tapahtuu, kun lähettäjä ja vastaanottaja ovat samassa fyysisessä verkossa. Muussa tapauksessa toimitus on epäsuoraa ja kulkee yhden tai useamman reitittimen kautta.


Reititystaulukko, jota hallinnoidaan joko manuaalisesti (staattinen reititys) tai dynaamisesti (dynaaminen reititys), sisältää tiedot, joita tarvitaan reitin valintaan. Pienissä verkoissa riittää staattinen määritys. Suuremmissa infrastruktuureissa dynaaminen reititys on välttämätön, jotta reittejä voidaan mukauttaa automaattisesti, kun topologia muuttuu tai jokin linkki katkeaa.


Reititystaulukko toimii kartoitustaulukkona kohde-IP-osoitteiden ja seuraavien yhdyskäytävien välillä. Siihen tallennetaan yleensä verkkotunnukset (_network ID_) eikä jokaista yksittäistä isäntää Address, mikä pienentää sen kokoa huomattavasti.


| Destination Address | Next-Hop Router Address | Interface |
| ------------------- | ----------------------- | --------- |

Näiden merkintöjen avulla reititin voi nopeasti määrittää, minkä Interface:n kautta ja mihin solmuun kukin datagrammi on lähetettävä. Yhdessä ARP:n kanssa, joka ratkaisee vastaavat MAC-osoitteet, tämä takaa tehokkaan ja luotettavan tiedonsiirron verkossa.


Dynaamisiin reititysprotokolliin kuuluvat standardit, kuten etäisyysalgoritmiin perustuva RIP (_Routing Information Protocol_) ja OSPF (_Open Shortest Path First_), joka laskee lyhimmät reitit monimutkaisessa topologiassa. Nämä protokollat Exchange päivittävät jatkuvasti reittejä optimoidakseen, vähentääkseen siirtokustannuksia ja parantaakseen kestävyyttä katkoksia tai ruuhkia vastaan.



## NAT: Address-käännös


<chapterId>4f984d5d-f2e0-4faf-b703-ff315f32cef4</chapterId>



### Määritelmä


Network Address Translation_ (NAT) on tekniikka, joka on kehitetty Address käytettävissä olevien IPv4-osoitteiden asteittaiseen loppumiseen. NAT on suunniteltu väliaikaiseksi ratkaisuksi ennen IPv6:n laajaa käyttöönottoa, ja sen avulla yritykset ja yksityishenkilöt voivat edelleen yhdistää suuren määrän koneita ja käyttää vain rajoitettua joukkoa julkisia IP-osoitteita.


**Tärkeä muistutus:** Siirtyminen IPv4:stä IPv6:een ratkaisee teoreettisesti uupumisongelman laajentamalla Address-avaruutta 32 bitistä 128 bittiin, jolloin osoitteita on lähes rajattomasti (2^128). Käytännössä siirtyminen on kuitenkin vielä epätäydellinen, ja NAT on edelleen laajalti käytössä.


NAT:n periaate on yksinkertainen mutta erittäin tehokas: sen sijaan, että jokaiselle sisäverkon laitteelle määritettäisiin yksilöllinen julkinen IP-osoite Address, kaikille yksityisille laitteille käytetään yhtä reititettävää Address-osoitetta (tai pientä osoitepoolia). NAT-yhdyskäytävä, joka on usein integroitu reitittimeen tai palomuuriin, kääntää dynaamisesti sisäisen IP-osoitteen Address sekä tiedot, joita tarvitaan liikenteen oikeaan reitittämiseen ulkomaailmaan, ja varmistaa, että vastaukset palautetaan alkuperäiselle lähettäjälle.


Tästä lähestymistavasta on välitön hyöty: se piilottaa sisäisen verkkoarkkitehtuurin kokonaan. Ulkopuolisen silmin kaikki työasemien, palvelimien tai tulostimien pyynnöt näyttävät tulevan samasta julkisesta identiteetistä. Yksityiset osoitteet, jotka on yleensä otettu varatuista alueista (esim. 192.168.x.x tai 10.x.x.x.x), pysyvät näkymättömissä Internetistä.


Sen lisäksi, että NAT korjaa IPv4:n niukkuutta, se vahvistaa myös turvallisuutta luomalla ensimmäisen loogisen esteen sisäisten ja julkisten verkkojen välille. Pyytämättä saapuva viestintä on luonnollisesti estetty, koska vain verkon sisältä käynnistetyt yhteydet hyötyvät vastausten saamiseksi tarvittavasta kääntämisestä.



![Image](assets/fr/035.webp)



### Käännöstyypit


NAT voidaan toteuttaa eri tavoin erityistarpeiden mukaan. Kaksi tärkeintä toimintatapaa ovat staattinen ja dynaaminen kääntäminen.


** Staattinen käännös** luo kiinteän yhdistelmän yksityisen IP Address:n ja julkisen IP Address:n välille. Kukin sisäinen kone on pysyvästi yhdistetty omaan julkiseen Address:äänsä. Esimerkiksi sisäinen laite, jonka osoite on 192.168.20.1, voidaan yhdistää reititettävään Address 157.54.130.1:ään. Kun lähtevä paketti lähtee paikallisverkosta, reititin korvaa paketin lähde-Address:n julkisella Address:llä ja tekee päinvastaisen operaation saapuvalle liikenteelle. Tämä kaksisuuntainen käännös on käyttäjälle läpinäkyvä.


**Varoitus:** Vaikka tämä menetelmä eristää sisäverkon, se ei ratkaise julkisten IP-osoitteiden puutetta, sillä tarvitset edelleen niin monta julkista osoitetta kuin on koneita, jotka haluat paljastaa. Staattista kääntämistä käytetään siis lähinnä silloin, kun tiettyjen sisäisten resurssien on pysyttävä tavoitettavissa ulkopuolelta (verkkopalvelin, sähköpostipalvelin...).


**Dynaaminen kääntäminen** puolestaan käyttää julkisten IP-osoitteiden joukkoa. Kun sisäinen isäntä aloittaa yhteyden, reititin määrittää tilapäisesti yhden näistä julkisista osoitteista isännän yksityiselle Address:lle istunnon ajaksi. Yhteys on 1:1, mutta väliaikainen: kun yhteys päättyy, julkinen Address tulee toisen laitteen käyttöön. Dynaaminen NAT vähentää siis tarvittavien julkisten osoitteiden määrää, kun kaikki koneet eivät ole verkossa samanaikaisesti, mutta se vaatii silti ulkoisten osoitteiden lohkon, joka on vähintään yhtä suuri kuin samanaikaisten yhteyksien enimmäismäärä.


**Port translation** (PAT), joka tunnetaan myös nimellä *NAT overload* tai *IP masquerading*, menee askeleen pidemmälle: kaikki yksityiset laitteet jakavat yhden julkisen IP Address:n (tai hyvin pienen numeron). Erottaakseen istunnot toisistaan yhdyskäytävä muuttaa lähteen Address:n lisäksi myös lähdeporttia. Se pitää yllä taulukkoa, joka yhdistää jokaisen *(yksityinen Address, yksityinen portti)* -parin yksilölliseen *(julkinen Address, julkinen portti)* -pariin. Tätä NAT-muotoa käytetään lähes kaikissa kotireitittimissä, jolloin kymmenet laitteet (tietokoneet, älypuhelimet, liitetyt esineet jne.) voivat käyttää samaa julkista IP Address:ää ja säilyttää samalla sujuvan viestinnän.


NAT siis pidentää IPv4:n käyttöikää ja lisää samalla arvokkaan Layer:n segmentoinnin ja turvallisuuden. Kun IPv6:n yleistyminen ja sen laaja Address -avaruus yleistyvät, NAT:n rooli todennäköisesti vähenee, vaikka sitä käytetäänkin edelleen joissakin ympäristöissä yhteensopivuus- ja valvontatarkoituksiin liikenteen segmentointiin ja suodattamiseen.


### NAT-toteutus


Address-käännöksen asianmukaisen toiminnan varmistamiseksi NAT-reitittimen tai -yhdyskäytävän on pidettävä tarkkaa kirjaa kunkin sisäverkon yksityisen Address:n ja sen ulkomaailman kanssa kommunikointiin käytettävän julkisen Address:n välille tehdyistä kartoituksista. Nämä tiedot tallennetaan niin sanottuun NAT-käännöstaulukkoon, jolla on keskeinen rooli verkkoliikenteen hallinnassa.


Kukin taulukon merkintä yhdistää vähintään yhden parin: lähettävän koneen sisäisen IP Address:n ja ulkoisen IP Address:n, joka näkyy Internetissä. Kun paketti lähetetään yksityisestä verkosta julkiseen kohteeseen, NAT-reititin sieppaa kehyksen, analysoi IP- ja TCP/UDP-otsikot ja korvaa sitten yksityisen lähteen Address:n portin julkisella Address:lla. Paluupolulla sama yhdyskäytävä sieppaa saapuvan paketin, tarkistaa yhdistämistaulukon ja suorittaa käänteisen operaation ohjatakseen virran alkuperäiseen sisäiseen IP Address:een.


Tämä dynaamisen käännöksen periaate perustuu tarkkaan taulukon hallintaan: jokainen merkintä pysyy voimassa niin kauan kuin on aktiivista liikennettä, joka oikeuttaa sen. Määritettävissä olevan käyttämättömän ajanjakson jälkeen merkintä tyhjennetään ja sitä voidaan käyttää uudelleen uusiin yhteyksiin.


_Esimerkki yksinkertaistetusta NAT-käännöstaulukosta:_


| Internal IP   | External IP    | Duration (sec) | Reusable? |
| ------------- | -------------- | -------------- | --------- |
| 10.101.10.20  | 193.48.100.174 | 1,200          | no        |
| 10.100.54.251 | 193.48.101.8   | 3,601          | yes       |
| 10.100.0.89   | 193.48.100.46  | 0              | no        |

Tässä esimerkissä, jos yksikään paketti ei ole kulkenut toisen merkinnän kautta yli tuntiin (3600 sekuntiin), se merkitään uudelleenkäytettäväksi. Sitä vastoin kesto nolla osoittaa aktiivista viestintää, jolloin kartoitus on lukittu.


Vaikka NAT toimii läpinäkyvästi useimmissa tavallisissa käyttötarkoituksissa (verkkoselaaminen, sähköposti, tiedostojen siirto jne.), se voi aiheuttaa lisähaasteita tietyille verkkosovelluksille. Jotkin tekniikat perustuvat IP-osoitteiden tai porttien nimenomaiseen vaihtamiseen paketin hyötykuorman sisällä. NAT-yhdyskäytävän läpi kuljettuaan nämä tiedot muuttuvat epäjohdonmukaisiksi.


Tyypillisiä esimerkkejä rajoituksista ovat:


- Vertaisverkkoprotokollia (P2P), jotka edellyttävät suoria yhteyksiä laitteiden välillä, haittaa NAT-este, koska kaikki sisäiset koneet käyttävät samaa ulkoista IP-osoitetta Address, eikä niitä voi tavoittaa suoraan ilman erityisiä asetuksia (kuten *port forwarding* tai UPnP);
- IPSec-protokolla, jota käytetään verkkoviestinnän suojaamiseen, salaa pakettien otsikot. Koska NAT:n on muutettava näitä otsikoita IP-osoitteiden korvaamiseksi, salaus tekee tämän mahdottomaksi ilman NAT-T:n (*NAT Traversal*) kaltaisia mukautusmekanismeja;
- X Window -protokolla, joka mahdollistaa graafisten sovellusten etänäyttämisen Unix/Linuxissa, toimii siten, että X-palvelin lähettää aktiivisesti TCP-yhteyksiä asiakkaille. Tämä yhteyksien tavanomaisen suunnan kääntäminen voidaan estää NAT:lla.


Yleisesti ottaen kaikki protokollat, jotka sisältävät nimenomaisesti sisäisen IP Address:n paketin hyötykuormaan, kärsivät tästä, koska kyseinen Address ei enää käännöksen jälkeen vastaa todellista, internetissä näkyvää Address:ta.


**Tärkeä huomautus:** Address:n näiden ongelmien ratkaisemiseksi jotkin NAT-reitittimet tarjoavat _Deep Packet Inspection_ (DPI) tai _Protocol Helpers_ -ohjelmia, jotka tarkastavat pakettien sisällön ja tunnistavat ja korvaavat dynaamisesti osoitteet tai porttinumerot sovellustiedoissa. Tämä edellyttää protokollamuodon syvällistä tuntemusta ja voi aiheuttaa tietoturva-aukkoja tai lisätä resurssien käyttöä.


**Varoitus:** Vaikka NAT auttaa piilottamaan sisäverkon ja valvomaan saapuvaa liikennettä, se ei korvaa omaa palomuuria. Pelkkä kääntäminen ei ole täydellinen suojauseste: sitä on aina täydennettävä selkeillä suodatussäännöillä, joilla estetään ei-toivottu tai ei-toivottu liikenne.


_Katsotaanpa seuraavaa esimerkkiä havainnollistaaksemme, miten tämä toimii käytännössä:_



![Image](assets/fr/037.webp)



Tässä skenaariossa sisäinen työasema voi käyttää sisäistä verkkopalvelinta yksinkertaisesti kutsumalla URL-osoitetta "http://192.168.1.20:80". Portin määrittäminen on tässä yhteydessä valinnaista, sillä `80` on tavallinen HTTP-portti.Jos taas pyyntö tehdään ulkopuolelta, käyttäjä syöttää julkisen Address:n `http://85.152.44.14:80`. NAT-reititin vastaanottaa pyynnön, käyttää kartoitustaulukkoa ja muuttaa julkisen Address:n automaattisesti yksityiseksi ja ohjaa yhteyden osoitteeseen `http://192.168.1.20:80`.


Sama periaate pätee kaikkiin muihin palvelimiin, joilla on lupa vastaanottaa Internet-yhteyksiä, kuten Extranet-palvelimeen (sininen piiri kuvassa).


**Käytännöllinen huomautus:** Virtualisoiduissa ympäristöissä käytetään yleisesti verkkoliitäntöjä nimeltä _virbrX_ (_Virtual Bridge X_). Nämä virtuaaliset sillat, joita tarjoavat erityisesti libvirt-kirjasto tai Xen-hypervisor, yhdistävät vieraskoneiden virtuaalisen sisäverkon fyysiseen verkkoon soveltaen samalla NAT:ia. Ne konfiguroidaan yleensä skriptien avulla kohdassa `/etc/sysconfig/network-scripts/`, kuten alla on esitetty `virbr0`:lle:


```ini
NAME=""
BOOTPROTO=none
MACADDR=""
TYPE=Bridge
DEVICE=virbr0
NETMASK=255.255.255.0
MTU=""
BROADCAST=192.168.0.255
IPADDR=192.168.0.1
NETWORK=192.168.0.0
ONBOOT=yes
```


Kun virtuaalinen silta on käytössä, sinun on otettava käyttöön IP-reititys ja määritettävä porttikäännös "iptables"-ohjelmalla:


```shell
echo 1 > /proc/sys/net/ipv4/ip_forward
```


```shell
iptables -t nat -A POSTROUTING -o <WAN> -s 192.168.0.0/24 -j MASQUERADE
```


Tässä kokoonpanossa lähtevä liikenne reititetään ja NAT-käännös otetaan käyttöön, jolloin virtuaalikoneet voivat kommunikoida ulkomaailman kanssa paljastamatta suoraan sisäisiä IP-osoitteitaan.


Seuraavassa luvussa tarkastelemme yksityiskohtaisesti IP Address:n konfigurointia Linuxissa ja käsittelemme sekä yksinkertaisia että edistyneempiä menetelmiä, jotka soveltuvat erilaisiin hallintatilanteisiin.



https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864


## Miten konfiguroin verkon `ip`:n avulla?


<chapterId>8ba7e946-d2a0-4841-8d54-e85ba96baa25</chapterId>



### Vakiokokoonpano


Kun olet käsitellyt verkkojen teoreettisia perusteita ja ymmärtänyt, miten IP-osoitteet, maskit, reititys ja kääntäminen toimivat yhdessä, on aika siirtyä käytännön konfigurointiin. GNU/Linuxissa verkon asetukset hoidetaan nyt komennolla **`ip`** (_iproute2_-paketti), joka korvaa vanhemman `ifconfig`-komennon.


`ip` avulla voit määrittää tai muuttaa IP Address:n, muuttaa maskia, käynnistää tai pysäyttää Interface:n tai tarkistaa sen tilan milloin tahansa.


**TIPS:** näyttääksesi kaikki liitännät (aktiiviset tai ei): `ip addr show`


Esimerkki: staattisen Address:n määrittäminen ja Interface:n aktivointi


Lisää Address `192.168.1.2/24` Interface `eth0`:een:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Aktivoi Interface:


```shell
ip link set dev eth0 up
```


Deaktivoi sama Interface:


```shell
ip link set dev eth0 down
```


Näytä tietyn Interface:n tila:


```shell
ip addr show dev eth2
```


**Käytännön vinkki:** `ip`:n avulla Address:n lisääminen Interface:ään ei enää vaadi `:1`-loppuliitettä. Lisää vain toinen `ip addr add ...`-rivi:


```shell
ip addr add 172.18.2.39/24 dev eth2
```


### Aktivointiskriptit: ifup / ifdown


Apuohjelmat `ifup` ja `ifdown` lukevat staattisia konfiguraatiotiedostoja tiedostosta `/etc/sysconfig/network-scripts/` (RHEL, CentOS, Rocky Linux, AlmaLinux...) tai tiedostosta `/etc/network/interfaces` (Debian/Ubuntu), jotta rajapinnat voidaan ottaa käyttöön tai poistaa käytöstä siististi.


```shell
ifup eth1
ifdown eth2
```


Konfiguraatiotiedostot (RHEL:n kaltaiset):


- /etc/sysconfig/network**: yleiset asetukset (NETWORKING, HOSTNAME, GATEWAY...).
- ifcfg-**: kunkin Interface:n omat asetukset.


Staattinen esimerkki (ifcfg-eth0):


```ini
DEVICE=eth0
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.2.5
NETMASK=255.255.255.0
GATEWAY=192.168.2.1
```


DHCP-esimerkki:


```ini
DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes
```


Tämä modulaarinen rakenne on edelleen voimassa, ja se voidaan helposti automatisoida nykyisissä järjestelmissä.


### Edistynyt konfigurointi: liimaus


Ammattikäyttöön tarkoitetuissa ympäristöissä tavoitteena on taata palvelun jatkuvuus ja/tai aggregoida kaistanleveyttä. *Bonding* (tai *teaming* _teamd_:n kanssa) -mekanismit vastaavat näihin tarpeisiin: useat fyysiset liitännät toimivat yhtenä loogisena Interface:na, jota kutsutaan usein nimellä "bond0" tai "team0".



![Image](assets/fr/039.webp)



Edellytykset:


- Lataa `bonding`-moduuli (tai käytä `teamd`) ;
- Käytettävissä on oltava vähintään kaksi fyysistä liitäntää.


#### Erilaiset yleiset liimausmenetelmät:


|Mode|Name|Principle|
|---|---|---|
|0|balance-rr|Round-robin, cyclic distribution of frames|
|1|active-backup|Single active interface with hot failover |
|2|balance-xor|Selection based on XOR of src/dst MAC addresses|
|3|broadcast|Broadcast simultaneously on all interfaces   |
|4|802.3ad (LACP)|Standardized dynamic aggregation; requires compatible switch|
|5|tlb (Transmit Load Balancing)|Balancing based on transmit load|
|6|alb (Adaptive Load Balancing)|Adaptive balancing; also balances receive via ARP|

#### Asettaminen `ip-linkin avulla



- Poista fyysiset liitännät käytöstä:


```shell
ip link set eth0 down
ip link set eth1 down
```



- Luo liimattu Interface:


```shell
ip link add bond0 type bond mode balance-alb
```



- Määritä asetukset luomisen jälkeen


```shell
ip link set bond0 type bond miimon 100
```



- Määritä MAC- ja IP-osoitteet:


```shell
ip link set dev bond0 address 00:17:56:BC:02:3A
ip addr add 192.168.2.3/24 dev bond0
ip route add default via 192.168.2.1
```



- Kiinnitä orjapiirejä:


```shell
ip link set eth0 master bond0
ip link set eth1 master bond0
```



- Tuo kaikki takaisin ylös:


```shell
ip link set bond0 up
ip link set eth0 up
ip link set eth1 up
```


**Vinkki:** Voit irrottaa orjan ilman, että yhteys katkeaa: `ip link set eth1 nomaster`


#### Pysyvä kokoonpano (RHEL:n kaltainen)


Luo kolme tiedostoa tiedostoon `/etc/sysconfig/network-scripts`:


_ifcfg-bond0_


```ini
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=none
IPADDR=192.168.2.3
NETMASK=255.255.255.0
BROADCAST=192.168.2.255
GATEWAY=192.168.2.1
BONDING_OPTS="mode=balance-alb miimon=100"
```


_ifcfg-eth0_


```ini
DEVICE=eth0
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```


_ifcfg-eth1_


```ini
DEVICE=eth1
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```


Sitten:


```shell
systemctl restart network
```


#### Lisä-IP Address (nykyaikainen peitenimi)


Kun käytät `ip`, voit yksinkertaisesti lisätä toisen Address:n samaan laitteeseen:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Jos haluat tämän aliaksen pysyväksi uudelleenkäynnistyksen jälkeen, lisää joko toinen `IPADDR2=...` / `PREFIX2=...`-lohko `ifcfg-eth0`:een tai luo uusi *NetworkManager*-yhteys `nmcli`:llä.


`ip`:n ja siihen liittyvien komentojen (`ip link`, `ip addr`, `ip route`) ansiosta verkon konfigurointi on johdonmukaisempaa, skriptattavampaa ja selkeämpää. Bonding on keskeinen osa korkean käytettävyyden arkkitehtuuria, ja useiden osoitteiden määrittäminen yhdelle Interface:lle on tullut paljon yksinkertaisemmaksi.


Seuraavassa luvussa tarkastelemme IPv6-osoitteiden erityispiirteitä ja toteutusta.


# IPv6-osoitteet


<partId>9b1d87f1-2a68-496e-b5dd-76cf74fb8cde</partId>


## IPv6: standardit ja määritelmät


<chapterId>d1f16f0a-1104-460d-8d67-f725665f8e3f</chapterId>



Nyt siirrytään IP-osoitteiden seuraavaan sukupolveen: IPv6-protokollaan, joka alun perin tunnettiin nimellä IPng (_IP Next Generation_). IPv4:n rakenteellisten rajoitusten poistamiseksi suunniteltu protokolla tarjoaa huomattavasti laajennetun osoitearkkitehtuurin sekä lukuisia teknisiä optimointeja.


IPv6:n käyttöönoton taustalla on monenlaisia motiiveja, ja Address:llä on kriittisiä tarpeita Internetin kehityksen kannalta. Ensinnäkin IPv6:n tehtävänä on tukea liitettyjen laitteiden määrän räjähdysmäistä kasvua (tavoite, jota ei voida saavuttaa IPv4:n rajallisella Address tilalla). Toiseksi protokollan tavoitteena on pienentää reititystaulujen kokoa, mikä tehostaa tiedonvaihtoa ja vähentää reitittimien työmäärää pitkällä aikavälillä.


IPv6 pyrkii myös yksinkertaistamaan tiettyjä pakettien käsittelyyn liittyviä näkökohtia, parantamaan datagrammien kulkua ja optimoimaan siirtonopeuksia verkkojen välillä. Tietoturvan kannalta *IPsec*-protokollan AH/ESP-otsikot sisältyvät perusmäärittelyyn, ja kaikkien IPv6-solmujen on pystyttävä tukemaan niitä (RFC 6434). Niiden käyttö on kuitenkin edelleen valinnaista: järjestelmänvalvojan tehtävänä on ottaa ne käyttöön asiayhteyden mukaan.


Muihin tavoitteisiin kuuluu palvelutyyppien tarkempi käsittely, erityisesti reaaliaikaisten sovellusten (VoIP, videoneuvottelut jne.) laadun parantaminen. IPv6:n tarkoituksena on myös mahdollistaa joustavampi liikkuvuuden hallinta: laite voi vaihtaa liityntäpistettä muuttamatta Address:aa tavalla, joka näkyy sen vertaislaitteille.


IPv6 on suunniteltu toimimaan rinnakkain vanhojen protokollien kanssa. Vaikka se ei ole suoraan binääriyhteensopiva IPv4:n kanssa, se on täysin yhteentoimiva korkeamman Layer-protokollan, kuten TCP:n, UDP:n, ICMPv6:n ja DNS:n, sekä reititysprotokollien, kuten OSPF:n ja BGP:n, kanssa tietyin mukautuksin. Monilähetysten hallintaan IPv6 käyttää MLD-protokollaa (*Multicast Listener Discovery*), joka vastaa toiminnallisesti IGMP:tä IPv4-ympäristössä.


### Merkintäsäännöt


Yksi IPv6:n merkittävimmistä muutoksista on itse IP Address:n muoto. IPv4-osoitteiden kroonisen puutteen vuoksi Address:n pituutta on kasvatettu 32 bitistä 128 bittiin eli 16 tavuun. Teoriassa tämä antaa Address:n mahdollisen tilan:


$$3.4 \ kertaa 10^{38}$$$


Tämä takaa lähes rajattoman kapasiteetin kaikille nykyisille ja tuleville laitteille.


IPv6-osoitteet kirjoitetaan hyvin eri tavalla kuin tutussa pistemäisessä desimaalimerkinnässä. IPv6 Address koostuu kahdeksasta 16-bittisestä ryhmästä, jotka kirjoitetaan heksadesimaalilukuna ja erotetaan toisistaan kaksoispisteillä `:`.


Esimerkiksi:


```
1987:0c02:0000:84c2:0000:0000:cf2a:9077
```


Merkintätavan yksinkertaistamiseksi kunkin ryhmän etunollat voidaan jättää pois. Yllä oleva esimerkki muuttuu tällöin seuraavasti:


```
1987:c02:0:84c2:0:0:cf2a:9077
```


Lisäksi yksi jatkuva nollaryhmien sarja voidaan korvata:::lla, mikä lyhentää Address:ta entisestään:


```
1987:c02:0:84c2::cf2a:9077
```


**Varoitus:** tämä sääntö on tiukka: vain yksi peräkkäisten nollien sarja voidaan korvata `::`:llä. Jos Address sisältää useita nollasarjoja, vain pisin niistä tiivistetään. Näin varmistetaan sekä yksikäsitteisyys että luettavuus.


**Tärkeä yksityiskohta:** Heksadesimaalilohkojen erottamiseen käytetty `:`-merkki voi aiheuttaa epäselvyyksiä URL-osoitteissa, koska `:`-merkkiä käytetään myös palveluportin osoittamiseen. Sekaannusten välttämiseksi URL-osoitteissa olevat IPv6-osoitteet on suljettava hakasulkeisiin `[ ]`.


Esimerkki HTTP-yhteydestä tiettyyn porttiin Address:lle `2002:400:2A41:378::34A2:36`:


```
http://[2002:400:2A41:378::34A2:36]:8080
```


Kun edustat IPv4 Address:tä IPv6-kontekstissa, voit käyttää sekamerkintää pistemäisessä desimaalimuodossa, jota edeltää `::`:


```
::192.168.1.5
```


Tämä yhteensopivuus helpottaa siirtymistä näiden kahden protokollan välillä, koska IPv4-lohkot voidaan sisällyttää IPv6 Address -tilaan.


**Huomautus:** Osoitteiden kirjoittamisen standardoimiseksi RFC 5952 määrittelee kanonisen muodon ja lyhennesäännöt, joilla vältetään saman Address:n useat esitystavat. Näiden suositusten noudattaminen auttaa vähentämään väärintulkintoja ja varmistaa johdonmukaiset verkkokokoonpanot.


### IPv6 Address-tyypit


IPv6 eroaa edeltäjistään monilla Address-luokilla, jotka on suunniteltu erityisiin käyttötarkoituksiin ja jotka mahdollistavat joustavan reitityksen ja verkonhallinnan. Kuten IPv4:ssä, osoitteet voivat olla maailmanlaajuisia, paikallisia, varattuja tai tiettyihin siirtymämekanismeihin liittyviä.


Määrittelemätöntä IPv6 Address:tä edustaa `::` tai tarkemmin sanottuna `::0.0.0.0.0`. Tätä erikoismuotoa käytetään Address:n hankinnan aikana tai oletusarvona ilmaisemaan Address:n puuttumista.



| IPv6 Address Prefix | Description                                 |
| ------------------- | ------------------------------------------- |
|::/8                | Reserved addresses                          |
| 2000::/3            | Unicast addresses, routable on the Internet |
| fc00::/7            | Unique local addresses (1)                  |
| fe80::/10           | Link-local addresses                        |
| ff00::/8            | Multicast addresses                         |

(1): *Etuliite `fd00::/8` on suositeltavampi yksityisessä lähiverkossa sellaisten sisäisten osoitteiden osoittamisessa, jotka eivät ole reititettävissä Internetiin.*


#### Varatut osoitteet


Tietyt IPv6-alueet on nimenomaisesti varattu, eikä niitä saa käyttää globaaleina osoitteina. Niillä on erityisiä teknisiä tarkoituksia:


- `::/128`**: määrittelemätön Address, jota ei ole koskaan määritetty pysyvästi laitteelle, mutta jota konfigurointia odottava kone käyttää lähde-Address:nä.
- `::1/128`**: _loopback_ Address, joka vastaa suoraan IPv4:n `127.0.0.0.1`:tä ja jonka avulla kone voi käyttää Address:ta itseään.
- `64:ff9b::/96`**: Varattu protokollan kääntäjille, jotka mahdollistavat IPv4/IPv6-yhteyden RFC 6052:ssa määritellyllä tavalla.
- `::ffff:0:0/96`**: Yhteensopivuuslohko IPv4 Address:n esittämiseksi tietyssä IPv6-rakenteessa, jota sovellukset käyttävät usein sisäisesti.


Nämä lohkot takaavat yhteentoimivuuden ja helpottavat siirtymistä kahden protokollaversion välillä.


#### Globaalit unicast-osoitteet


Globaalit unicast-osoitteet muodostavat suurimman osan julkisesti reititettävissä olevasta IPv6-avaruudesta, noin 1/8 Address-avaruudesta. Vuodesta 1999 lähtien IANA on jakanut nämä lohkot, kuten etuliitteen `2001::/16`, CIDR-lohkoina (23:sta 12:een) alueellisille rekistereille, jotka jakavat ne edelleen palveluntarjoajille ja organisaatioille.


Joillakin alueilla on dokumentoituja käyttötarkoituksia:


- `2001:2::/48`**: Varattu suorituskyvyn ja yhteentoimivuuden testausta varten (RFC 5180).
- `2001:db8::/32`**: Varattu dokumentaatiota ja esimerkkejä varten (RFC 3849).
- `2002::/16`**: Käytetään 6to4-mekanismia varten, jonka avulla IPv6-liikenne voi kulkea IPv4-infrastruktuurin kautta (hyödyllinen siirtymävaiheessa näiden kahden protokollan välillä).


**Huomautus:** suuri osa maailmanlaajuisista osoitteista jää käyttämättä, ja ne toimivat varantona Internetin tulevaa kasvua varten.


#### Yksilölliset paikalliset osoitteet (ULA)


Yksilölliset paikalliset osoitteet (`fc00::/7`) ovat IPv6:n vastine IPv4:n yksityisille osoitteille (RFC1918). Ne mahdollistavat eristettyjen sisäisten verkkojen luomisen vaarantamatta ristiriitoja julkisten osoitteiden kanssa. Käytännössä todellinen etuliite on `fd00::/8`, jossa kahdeksas bitti on 1 paikallisen käytön osoittamiseksi. Jokainen ULA-lohko sisältää 40-bittisen pseudosattumanvaraisen tunnisteen, joka minimoi Address-kolarit, kun erillisiä yksityisiä verkkoja yhdistetään.


#### Linkin paikalliset osoitteet


Linkin paikallisia osoitteita (fe80::/64) käytetään ainoastaan saman Layer 2-segmentin (sama VLAN tai kytkin) sisäiseen viestintään. Niitä ei koskaan reititetä paikallisen linkin ulkopuolelle. Kukin verkon Interface luo automaattisesti linkin paikallisen Address-osoitteen, joka usein johdetaan sen MAC Address -osoitteesta EUI-64-järjestelmän avulla.


**Erikoisominaisuus**: sama kone voi käyttää samaa linkin paikallista Address:a useissa liitännöissä, mutta Interface on määriteltävä viestinnän yhteydessä epäselvyyksien välttämiseksi.


#### Multicast-osoitteet


IPv6:ssa broadcast on korvattu multicastilla, joka on tehokkaampi tapa toimittaa paketteja määritellylle vastaanottajaryhmälle. Monilähetysalueen etuliite on `ff00::/8`. Näihin kuuluvat osoitteet, kuten `ff02::1`, joka on suunnattu kaikille paikallisen linkin solmuille. Vaikka tämä Address on kätevä, sitä ei enää suositella sovelluksiin, koska se voi generate:n mukaan aiheuttaa hallitsemattomia lähetyksiä.


Monilähetysten yleinen käyttötapa on _Neighbor Discovery Protocol_ (NDP), joka korvaa ARP:n IPv6:ssa. NDP käyttää tiettyjä monilähetysosoitteita, kuten `ff02::1:ff00:0/104`, löytääkseen automaattisesti muita samaan linkkiin liitettyjä isäntiä.


Yhdistämällä nämä Address-tyypit IPv6 tarjoaa täydellisen valikoiman vaihtoehtoja maailmanlaajuisen reitityksen, paikallisen viestinnän, IPv4/IPv6-siirtymisen ja automaattisen laitekonfiguroinnin tarpeisiin ja parantaa samalla siirtotehokkuutta.


### Address soveltamisala


IPv6 Address:n laajuus määrittelee tarkan toimialueen, jolla se on voimassa ja ainutlaatuinen. Tämän käsitteen ymmärtäminen on avainasemassa pakettireitityksen ja IPv6-verkon loogisen organisoinnin hallinnassa. IPv6-osoitteet ryhmitellään yleensä kolmeen pääluokkaan niiden laajuuden ja käytön perusteella: unicast, anycast ja multicast.


**Unicast-osoitteet** ovat yleisimpiä, ja niihin kuuluu useita eri alatyyppejä.

Näihin kuuluu _loopback_ (`::1`) Address, jonka toiminta-alue rajoittuu sitä käyttävään isäntäkoneeseen ja jota käytetään verkkopinon sisäiseen testaamiseen lähettämättä liikennettä fyysisen verkon yli.

Lisäksi on olemassa linkin paikalliset osoitteet (_link-local_), joiden käyttöalue rajoittuu yhteen verkkosegmenttiin: niitä käytetään suorassa viestinnässä saman fyysisen tai loogisen linkin (esim. yhden kytkimen tai VLANin) laitteiden välillä.

Yksilölliset paikalliset osoitteet (_ULA_, lyhenne sanoista _Unique Local Addresses_) ovat yksityisen verkon sisäisiä osoitteita. Niitä voidaan reitittää useiden yksityisten segmenttien välillä, mutta ne eivät koskaan näy Internetissä.


Käsitteellisesti IPv6-osoitteet esitetään usein binäärirakenteena, jonka ensimmäinen puolikas (ensimmäiset 64 bittiä) yksilöi verkon etuliitteen ja toinen puolikas (myös 64 bittiä) yksilöi laitteen Interface:n kyseisessä verkossa. Tämä jako helpottaa Address automaattista konfigurointia SLAAC:n (_Stateless Address Autoconfiguration_) kaltaisten mekanismien avulla, joiden avulla koneet voivat automaattisesti generate valita vakaan Address MAC Address:n tai pseudosattumanvaraisen tunnisteen perusteella.


| Field     | Prefix | L | Global ID | Subnet | Interface ID |
|-----------|--------|---|-----------|--------|---------------|
| Bits      | 7      | 1 | 40        | 16     | 64            |

IPv6-arkkitehtuuri noudattaa nykyisen Internetin hierarkkista globaalia reititysmallia. Prefiksien jakamisen avulla alueelliset rekisterit ja verkko-operaattorit voivat hallita Address:n jakamista hajautetusti ja varmistaa samalla maailmanlaajuisen yksikäsitteisyyden. Tässä järjestelmässä sama isäntä voi samanaikaisesti pitää hallussaan maailmanlaajuista yksilähetys Address:tä Internet-viestintää varten ja linkkilokaalista Address:tä paikallista vuorovaikutusta varten, esimerkiksi välittömien naapurien kanssa tai reitittimen etsintäviestejä varten.


| Field     | Prefix | Zero | Interface ID |
|-----------|--------|------|--------------|
| Bits      | 10     | 54   | 64           |

**Anycast-osoitteet** ovat välikäsite, joka perustuu unicast-malliin mutta voi tietyissä tapauksissa käyttäytyä kuten multicast. Anycast Address on pohjimmiltaan unicast Address, joka on osoitettu useille eri verkkosolmujen välille jaetuille liitännöille. Kun paketti lähetetään anycast Address:lle, IPv6-protokolla pyrkii toimittamaan sen jollekin kyseisen Address:n jakavista isännistä, yleensä reititystopologialtaan lähimmälle. Tämä lähestymistapa optimoi kyselyjen käsittelynopeuden ja parantaa hajautettujen palvelujen häiriönsietokykyä. Klassinen esimerkki tästä ovat DNS-palvelimet, joissa anycast-osoitteet ohjaavat kyselyt automaattisesti lähimpään läsnäolopisteeseen.



| Field     | Prefix | Subnet | Interface ID |
|-----------|--------|--------|--------------|
| Bits      | 48     | 16     | 64           |

IPv6:ssa **monilähetysosoitteet** korvaavat broadcast-mekanismin, jota pidettiin liian kalliina ja sopimattomana maailmanlaajuiseen verkkoon. Monilähetys Address yksilöi ryhmän liitäntöjä, tyypillisesti useita isäntiä, jotka haluavat vastaanottaa samoja paketteja samanaikaisesti.

Jokainen monilähetys Address sisältää erityisen 4-bittisen _scope_-kentän, joka määrittelee lähetyksen maantieteellisen tai loogisen rajan:


- Laajuus "1" tarkoittaa, että paketti on tarkoitettu vain paikalliselle laitteelle.
- Laajuus "2" rajoittaa paketin paikalliseen linkkiin: kaikki saman fyysisen tai virtuaalisen segmentin laitteet voivat vastaanottaa sen.
- Laajuusalue "5" laajentaa sivuston, yleensä koko yritysverkon, kattavaksi.
- Laajuusalue "8" laajentaa organisaation kattavuutta, mikä mahdollistaa toimituksen kaikissa saman yksikön aliverkoissa.
- Laajuus "e" (14 heksadesimaalilukuna) tarkoittaa maailmanlaajuista ulottuvuutta, jolloin monilähetysryhmää voi käyttää mistä tahansa Internetissä, jos reititysinfrastruktuuri tukee sitä.


IPv6-multicast Address:n rakenne sisältää seuraavat osat:


- _Flag_-kenttä (4 bittiä) määrittää, onko ryhmä pysyvä vai väliaikainen,
- _Scope_-kenttä (4 bittiä) määrittelee laajuuden,
- tunnistekenttä (112 bittiä), joka yksilöi monilähetysryhmän numeron.


| Field      | Prefix | Flags | Scope | Group ID |
|------------|--------|--------|--------|----------|
| Bits       | 8      | 4      | 4      | 112      |

Tunnettu esimerkki IPv6-monilähetysten käytöstä on _Neighbor Discovery Protocol_ (NDP). Sen sijaan, että NDP käyttäisi ARP:tä kuten IPv4:ssä, se käyttää monilähetysosoitteita, kuten `ff02::1:ff00:0/104`, naapurien löytämispyyntöjen lähettämiseen, ja se kohdistuu vain samalla linkillä oleviin isäntäkoneisiin.


Määrittelemällä Address-alueet niin tarkasti IPv6 jäsentää, miten tietovirtoja lähetetään, vastaanotetaan ja reititetään. Tämä rakeisuus tekee protokollasta joustavamman ja tehokkaamman sekä paikallisen että globaalin viestinnän hallinnassa, ja samalla vältetään yleisradioinnin haitat.


## Address Assignment paikallisessa verkossa


<chapterId>4c9c3e52-59bc-499a-af0a-6dd369a9e029</chapterId>


Tässä luvussa tarkastelemme yhtä IPv6:n käyttöönoton käytännöllisimmistä näkökohdista: IP-osoitteiden osoittamista lähiverkon isännille. IPv6-arkkitehtuuri on suunniteltu joustavaksi, ja sen avulla jokainen laite voi generate Address automaattisesti, mutta se sallii silti tarvittaessa täysin manuaalisen konfiguroinnin.


IPv6-lähiverkko jakaa Address:n järjestelmällisesti kahteen osaan:


- ensimmäiset 64 bittiä edustavat aliverkon etuliitettä, jonka yleensä antaa reititin tai Address-viranomainen;
- isäntä käyttää loput 64 bittiä yksilöimään itsensä kyseisessä segmentissä.

Tämä malli yksinkertaistaa huomattavasti reittien yhdistämistä ja Address-lohkojen hallintaa.


Osoitteiden osoittamiseen laitteille käytetään kahta pääasiallista lähestymistapaa:


- Manuaalinen konfigurointi, jossa järjestelmänvalvoja määrittää kunkin Interface:n tarkan Address:n;
- Automaattinen konfigurointi, jossa laitteet generate tai saavat omat osoitteensa dynaamisesti.


Manuaalisessa konfiguroinnissa järjestelmänvalvoja määrittää jokaiselle Interface:lle täydellisen IPv6 Address:n. Tietyt arvot jäävät varatuiksi:


- `::/128`: määrittelemätön Address, jota ei ole koskaan määritetty pysyvästi ;
- `::1/128`: loopback Address (_loopback_), IPv4-vastaava: `127.0.0.0.1`.


Toisin kuin IPv4:ssä, tässä ei ole _broadcast_-käsitettä; "kaikki nollat" tai "kaikki ykköset" -yhdistelmillä isäntäosassa ei ole erityistä merkitystä.

Manuaalinen konfigurointi on edelleen hyödyllistä valvotuissa ympäristöissä, mutta sitä on vaikea ylläpitää mittakaavassa.


Automaattista konfigurointia varten on olemassa useita menetelmiä:


- RFC4862:n määrittelemä **NDP** (_Neighbor Discovery Protocol_) -protokolla mahdollistaa *tilasta riippumattoman* automaattisen konfiguroinnin. Tässä tilassa isäntä vastaanottaa verkon etuliitteen paikalliselta reitittimeltä ja täydentää itse Address:n MAC Address:een perustuvalla tunnisteella. Tämä menetelmä on helppo ottaa käyttöön, eikä se vaadi keskitettyä palvelinta.
- Windowsin kaltaiset toteutukset voivat generate isäntäosan pseudosattumanvaraisesti parantaa yksityisyyttä välttämällä MAC Address:n suoraa paljastumista. MAC Address:n paljastaminen IPv6-paketeissa voi herättää huolta yksityisyydestä, koska se mahdollistaa laitteen jäljittämisen eri verkoissa.
- DHCPv6-protokolla: Se on määritelty RFC3315:ssä ja on samanlainen kuin IPv4:ssä käytetty DHCP, mutta se mahdollistaa hallitumman ja keskitetymmän konfiguroinnin, mukaan lukien vuokrasopimusten hallinta, lisäoptiot (DNS, MTU...) ja tietokantojen rekisteröinti. DHCPv6 voi toimia yksin tai yhdessä tilattoman konfiguroinnin kanssa lisäparametrien tarjoamiseksi ilman, että Address määrittää itse IP-osoitteen.


**Tärkeä huomautus:** MAC-pohjaisessa menetelmässä MAC Address muunnetaan 64-bittiseksi tunnisteeksi EUI-64-muodossa. Tämä mekanismi lisää tavut `FF:FE` alkuperäisen MAC Address:n (48-bittisen) keskelle ja kääntää 7. bitin käänteiseksi osoittaakseen globaalin ainutkertaisuuden. Tuloksena on vakaa Interface-tunniste, jota käytetään täydellisessä IPv6 Address:ssä.


Tässä on esimerkki siitä, miten MAC Address muunnetaan EUI-64:ksi:


![Image](assets/fr/045.webp)



Laitteiden seurantaan liittyvien kasvavien huolenaiheiden vuoksi nykyaikaiset käyttöjärjestelmät (erityisesti Linux, Windows 10+, macOS ja Android) ottavat nyt kuitenkin oletusarvoisesti käyttöön yksityisyyslaajennukset. Nämä käyttävät satunnaisesti luotuja Interface-tunnisteita, jotka uusitaan säännöllisesti lähteviä yhteyksiä varten, mutta sisäisessä viestinnässä (kuten DNS tai DHCPv6) käytetään vakaata tunnistetta.


Kuten IPv4:n DHCP:ssä, automaattisesti osoitetuilla IPv6-osoitteilla voi olla kaksi DHCPv6-reitittimien tai -palvelimien määrittelemää käyttöikää:


- Suositeltava käyttöikä*: tämän ajanjakson jälkeen Address pysyy voimassa, mutta sitä ei enää käytetä uusien yhteyksien muodostamiseen;
- Voimassaoloaika*: kun tämä aika päättyy, Address poistetaan kokonaan Interface-kokoonpanosta.


Järjestelmän avulla voidaan hallita verkkomuutoksia dynaamisesti, esimerkiksi varmistaa sujuva siirtyminen palveluntarjoajalta toiselle. IPv6-siirtyminen voidaan toteuttaa ilman havaittavia palvelukatkoksia päivittämällä reitittimien ilmoittama etuliite ja mukauttamalla DNS-tietueita samanaikaisesti.


**Vinkki:** Address:n ja DNS:n elinkaarien yhdistetty käyttö mahdollistaa asteittaisen siirtymisstrategian toteuttamisen, jossa uudet yhteydet siirtyvät uuteen topologiaan, kun taas olemassa olevat yhteydet jatkavat luonnolliseen loppumiseensa asti.


Lyhyesti sanottuna IPv6 tarjoaa Address Assignment:lle laajan valikoiman joustavuutta: manuaalinen konfigurointi, tilaton tai tilatietoinen automaattinen konfigurointi, DHCPv6 tai satunnainen generointi. Kullakin lähestymistavalla on omat etunsa ja rajoituksensa, ja sitä voidaan mukauttaa vaaditun valvontatason, verkon koon tai yksityisyyden suojaa koskevien tarpeiden mukaan.


## IPv6 Address-lohkojen määrittäminen


<chapterId>45cce866-1b58-4888-b3fe-15c922180839</chapterId>


### Address jakelu


IPv6 Address:n jakojärjestelmä on suunniteltu täyttämään kaksi tavoitetta: takaamaan maailmanlaajuinen Address:n ainutkertaisuus ja mahdollistamaan looginen hierarkia, joka suosii reititystaulujen yhdistämistä ja yksinkertaistamista.

Kuten IPv4:n kohdalla, IANA (Internet Assigned Numbers Authority) on tämän hierarkian huipulla. Se hallinnoi maailmanlaajuista unicast Address -aluetta ja delegoi Address-lohkoja viidelle alueelliselle Internet-rekisterille (_RIR_).


Viisi nykyistä RIR:ää ovat:


- ARIN (Pohjois-Amerikka),
- RIPE NCC (Eurooppa, Lähi-itä, Keski-Aasia),
- APNIC (Aasian ja Tyynenmeren alue),
- AFRINIC (Afrikka),
- LACNIC (Latinalainen Amerikka ja Karibia).


IANA jakaa kullekin RIR-alueelle erikokoisia IPv6-lohkoja, yleensä välillä /23 ja /12. Tämä lähestymistapa tarjoaa joustavuutta ja varmistaa samalla pitkän aikavälin skaalautuvuuden. RIR:t puolestaan jakavat nämä lohkot Internet-palveluntarjoajille (ISP), suuryrityksille ja julkisille laitoksille.


Vuodesta 2006 lähtien kukin RIR on saanut IANA:lta IPv6 /12-lohkon, jonka kiinteä koko on suunniteltu varmistamaan vakaa ja riittävän suuri varanto tulevaa kasvua varten. RIR:t jakavat nämä yleensä /23-, /26- tai /29-lohkoihin. Internet-palveluntarjoajat saavat useimmiten /32-lohkoja, vaikka tämä koko voi vaihdella palveluntarjoajan koon ja maantieteellisen alueen mukaan. Ne jakavat yleensä /48-lohkoja asiakkaille. Kukin /48-lohko tarjoaa 65 536 erillistä /64-alaverkkoa (valtava kapasiteetti verrattuna IPv4:ään).


**Tärkeä huomautus:** /32-lohko sisältää täsmälleen 65,536 /48-alalohkoa. Tämä tarkoittaa, että jokainen Internet-palveluntarjoaja voi palvella kymmeniätuhansia asiakkaita käyttämättä varaustaan loppuun. /48-lohkonsa ansiosta jokaisella asiakkaalla on sitten jättimäinen määrä tilaa jäsentää oma sisäverkkonsa niin monella /64-segmentillä kuin se haluaa.


Tyypillinen jakohierarkia näyttää seuraavalta:


| IANA | RIR | LIR | Customer | Subnet | Interface |
|------|-----|-----|----------|--------|-----------|
|  3   | 20  |  9  |    16    |   16   |     64    |

Kun osoitteita on näin runsaasti, NAT (*Network Address Translation*), joka oli aikoinaan IPv4:ssä välttämätön Address-pulan ratkaisemiseksi, ei ole enää tarpeen. Jokaisella isännällä voi olla yksilöllinen, globaalisti reititettävissä oleva julkinen Address, mikä yksinkertaistaa päästä päähän -yhteyttä ja helpottaa IPSecin, VoIP:n tai saapuvien yhteyksien kaltaisten protokollien käyttöä.


Voit tarkistaa, mihin organisaatioon IPv6 Address kuuluu, käyttämällä `whois`-komentoa julkisten RIR-tietokantojen kyselyyn. Tämä avoimuus mahdollistaa etuliitteen omistavan organisaation tunnistamisen, mikä voi olla hyödyllistä verkko-, analyysi- tai tietoturvatarkoituksiin.


### PA vs. PI-osoittaminen


Alun perin IPv6:n jakomalli perustui yksinomaan PA-lohkoihin (*Provider Aggregatable*), eli ISP:hen sidottuihin lohkoihin. Tässä mallissa organisaatio saa etuliitteensä ISP:ltä, mikä tarkoittaa, että palveluntarjoajan vaihtaminen edellyttää koko infrastruktuurin uudelleennumerointia.


Vaikka IPv6:n automaattiset konfigurointiominaisuudet ja Address:n käyttöikä helpottavat uudelleennumerointia, se on edelleen hankalaa organisaatioille, joilla on kriittinen infrastruktuuri tai useita palveluntarjoajien yhteyksiä redundanssivaatimuksia varten.


Vuodesta 2009 lähtien jakopolitiikat ovat sallineet PI-lohkot (*Provider Independent*). Nämä lohkot (yleensä kooltaan /48) RIR jakaa suoraan yritykselle tai laitokselle ISP:stä riippumatta. Tämä malli soveltuu erityisen hyvin organisaatioille, jotka harjoittavat *multihomingia* (eli ovat yhteydessä useaan operaattoriin samanaikaisesti). Esimerkiksi Euroopassa RIPE-512:ssa esitetään PI:n jakamista koskevat periaatteet.


### Aliverkon maskin merkintätapa


IPv4:n tapaan IPv6 käyttää CIDR:ää (*Classless Inter-Domain Routing*). Siinä ilmoitetaan etuliitteen muodostavien bittien määrä Address:n jälkeen käyttämällä `/`-merkkiä.


Otetaan seuraava esimerkki:


```
2001:db8:1:1a0::/59
```


Tämä tarkoittaa, että ensimmäiset 59 bittiä ovat kiinteitä ja tunnistavat verkon. Kaikkia jäljellä olevia bittejä (tässä 69 bittiä) voidaan käyttää aliverkkojen tai isäntien tunnistamiseen.


Tämä merkintätapa kattaa siis osoitteet välillä `2001:db8:1:1a0:0:0:0:0:0:0` ja `2001:db8:1:1bf:ffff:ffff:ffff:ffff:ffff`.


Tämä lohko kattaa siis 8 /64-aliverkkoa, joista jokainen voi sisältää valtavan määrän laitteita.


CIDR-merkintätapa mahdollistaa tarkan Address-tilan suunnittelun suurista verkoista kotikäyttöön ja virtualisoituihin ympäristöihin, ja se kannustaa reitittimien yhdistämiseen, mikä vähentää reitittimen kuormitusta ja parantaa skaalautuvuutta.


### IPv6-paketit ja otsikot


IPv6-pakettimuoto eroaa IPv4:stä siten, että se on sekä yksinkertaisempi että laajennettavissa. IPv6-datagrammi alkaa aina kiinteän kokoisella 40 tavun otsikolla, joka sisältää kaikki olennaiset reititystiedot. Tämä virtaviivainen lähestymistapa verrattuna IPv4:n vaihtelevan pituiseen otsikkoon (20-60 tavua) mahdollistaa reitittimien nopeamman ja tehokkaamman pakettien käsittelyn.


IPv6 ei kuitenkaan poista toiminnallisuutta: sen sijaan, että se sisällyttäisi lukuisia valinnaisia kenttiä pääotsikkoon, se ottaa käyttöön lisäotsikoiden järjestelmän, joka sijoitetaan välittömästi perusotsikon jälkeen. Näiden valinnaisten otsakkeiden avulla voidaan lisätä tiettyihin toimintoihin liittyviä tietoja tai ohjeita ilman, että tavallisia paketteja kuormitetaan tarpeettomasti.


Joissakin lisäotsikoissa on kiinteä rakenne, kun taas toisissa voi olla vaihteleva määrä vaihtoehtoja. Näissä vaihtoehdot koodataan `{Type, Length, Value}` kolmioina:


- Tyyppi'-kenttä (1 tavu) ilmaisee vaihtoehdon luonteen;
- Tyypin kaksi ensimmäistä bittiä määrittelevät, mitä reitittimien on tehtävä, jos vaihtoehtoa ei tunnisteta:
 - Jätä vaihtoehto huomiotta ja jatka hoitoa,
 - Pudota datagrammi,
 - Pudota ja lähetä ICMP-virheilmoitus lähteelle.
 - Pudottaa datagrammin ilman ilmoitusta (kun kyseessä ovat multicast-paketit).
- Pituus-kenttä (1 tavu) määrittää arvo-kentän koon, joka on 0-255 tavua;
- Arvo-kenttä sisältää vaihtoehtoon liittyvät tiedot.


Seuraavassa on yleiskatsaus IPv6:ssa määriteltyihin erilaisiin lisäotsikkotyyppeihin.


#### Hop-by-Hop-otsikko


Tämä otsikko, jos se on olemassa, sijoitetaan aina heti perusotsikon jälkeen. Se sisältää tietoja, jotka jokaisen paketin reitittimen on käsiteltävä paketin reitityspolulla, toisin kuin useimmat muut otsikot, joita yleensä käsittelee vain kohdesolmu. Tyypillisiä käyttökohteita ovat yleisten parametrien ilmoittaminen tai tiettyjen käsittelyvaiheiden pyytäminen paketin kulkiessa verkon läpi.


![Image](assets/fr/047.webp)


#### Reititysotsikko


Reititysotsikossa määritetään luettelo väliosoitteista, joiden kautta paketin on kuljettava. Reititystapoja on kaksi:


- Tiukka reititys: tarkka reitti on ennalta määritelty
- Löyhä reititys: vain tietyt pakolliset vaiheet on määritelty.


Tämän juurrutusotsikon neljä ensimmäistä kenttää ovat:


- Seuraava otsikko**: määrittää seuraavan otsikon tyypin;
- Reititystyyppi**: Määrittää reititysmenetelmän (yleensä "0");
- Jäljellä olevat segmentit**: jäljellä olevien segmenttien määrä ;
- Address[n]**: luettelo väliosoitteista.


Kenttä "Segmenttejä jäljellä" alkaa jäljellä olevien segmenttien kokonaismäärällä, ja sitä vähennetään yhdellä jokaisella siirtymäkerralla.


![Image](assets/fr/048.webp)


#### Pirstoutumisotsikko


IPv6:ssa vain lähdeisäntä saa pirstoa datagrammin, toisin kuin IPv4:ssä, jossa myös reitittimet saattoivat tehdä niin. Kaikkien IPv6-solmujen on pystyttävä käsittelemään vähintään 1280 tavun paketteja. Jos reititin kohtaa seuraavan linkin MTU:ta suuremman paketin, se lähettää *ICMPv6 Packet Too Big* -viestin takaisin lähteelle, joka sitten mukauttaa lähetystensä kokoa.


Pirstoutumisotsikko sisältää seuraavat kentät:


- Identification**: Yksilöllinen datagrammin tunniste uudelleenkokoamista varten.
- Fragment Offset**: fragmentin sijainti alkuperäisessä datagrammissa.
- M-merkki**: osoittaa, seuraako lisää fragmentteja.


![Image](assets/fr/049.webp)


#### Todennusotsikko (AH)


Tämä otsake on suunniteltu turvaamaan viestintä varmistamalla sekä lähettäjän aitous että tietojen eheys. Sitä käytetään yleisesti IPsec-protokollan kanssa. Todennuskoodin avulla vastaanottaja voi vahvistaa, että viesti on todella peräisin odotetulta lähettäjältä ja että sitä ei ole muutettu kuljetuksen aikana.


Jos kyseessä on vilpillinen muutosyritys, todennuskoodi ei enää täsmää, ja datagrammi voidaan hylätä. Tämä mekanismi suojaa myös toistohyökkäyksiltä havaitsemalla luvattomat kopiot.


![Image](assets/fr/050.webp)


#### Kohdeasetusten otsikko


Tämä otsake on tarkoitettu vain datagrammin lopulliselle vastaanottajalle. Sitä voidaan käyttää lisäämään sovelluskohtaisia vaihtoehtoja tai metatietoja, joita välireitittimet eivät ota huomioon.


Alun perin pöytäkirjassa ei määritelty tällaista vaihtoehtoa. Tämä otsake otettiin kuitenkin käyttöön IPv6:n suunnittelun yhteydessä, jotta siihen voitaisiin lisätä tulevia laajennuksia muuttamatta paketin yleistä rakennetta. Esimerkiksi nolla-optiota käytetään vain otsikon pehmustamiseen 8 tavun kerrannaisiksi muistin kohdistamista varten.


![Image](assets/fr/051.webp)


IPv6-pakettien suunnittelu perustuu selkeään erotteluun minimaalisen perusotsikon ja modulaaristen lisäotsikoiden välillä. Tämä arkkitehtuuri takaa sekä vakiokäsittelyn suorituskyvyn että joustavuuden, jota tarvitaan protokollan kehittämiseksi ja tietoturvan, monimutkaisten reititys- tai palvelunlaatumekanismien integroimiseksi, säilyttäen samalla yhteensopivuuden tulevien infrastruktuurien kanssa.


## IPv6:n ja DNS:n välinen suhde


<chapterId>421eacb8-b80b-4aee-910f-e069ed805f00</chapterId>


Nykyaikaisissa verkoissa DNS (*Domain Name System*) muuntaa verkkotunnukset IP-osoitteiksi, joita koneet voivat käyttää. IPv6:n käyttöönoton myötä DNS:n oli sopeuduttava tukemaan 128-bittisiä osoitteita ja säilytettävä samalla yhteensopivuus IPv4:n kanssa. Tämä rinnakkaiselo on erityisen tärkeää dual-stack-ympäristöissä, joissa molemmat IP-versiot toimivat samanaikaisesti.


### IPv6-kohtaiset DNS-tietueet


DNS käyttää verkkotunnuksen yhdistämiseen IPv6 Address:ään AAAA (*quad-A*) -tietuetta, joka vastaa IPv4-osoitteiden A-tietuetta. AAAA-tietue yhdistää verkkotunnuksen nimenomaisesti IPv6 Address:ään.

Esimerkki:


```shell
ipv6.mydmn.org.         IN      AAAA    2001:66c:2a8:22::c100:68b
```


Tämä tietue osoittaa, että verkkotunnus `ipv6.mydmn.org` ratkaisee IPv6 Address:lle `2001:66c:2a8:22::c100:68b`. Samaan verkkotunnukseen voi liittää useita IP-osoitteita, joko IPv4- (A-tunnisteen kautta) tai IPv6-osoitteita (AAAA-tunnisteen kautta), ja se on jopa suositeltavaa parhaan mahdollisen yhteensopivuuden vuoksi. Näin IPv6-yhteensopivat asiakkaat voivat suosia IPv6:ta, mutta vain IPv4-yhteensopivia asiakkaita tuetaan edelleen.


Lisäksi DNS tukee käänteisresoluutiota, mikä tarkoittaa, että se voi etsiä tiettyyn IP Address:een liittyvän verkkotunnuksen. IPv6:n tapauksessa tämä toiminto käyttää PTR-tietueita, jotka on sijoitettu "ip6.arpa"-vyöhykkeelle. Tämä vyöhyke on varattu erityisesti IPv6:n käänteistä resoluutiota varten. IPv4:n tapauksessa se on `in-addr.arpa`-vyöhyke.


### Käänteinen resoluutio


IPv6 Address:n käänteinen resoluutio noudattaa tiukkaa prosessia:

1) Laajenna Address täyteen heksadesimaalimerkintään (16 tavua, eli 32 heksadesimaalilukua).

Esimerkki:


```shell
2001:66c:2a8:22::c100:68b
```


Tulee:


```shell
2001:066c:02a8:0022:0000:0000:c100:068b
```


2) Käännä jokaisen heksadesimaaliluvun (nibble) järjestys toisinpäin, erota ne toisistaan pisteillä ja liitä `ip6.arpa`:


```shell
b.8.6.0.0.0.1.c.0.0.0.0.0.0.0.0.2.2.0.0.8.a.2.0.c.6.6.0.1.0.0.2.ip6.arpa  IN PTR  ipv6.mydmn.org
```


Tämä rakenne takaa standardoidut, yksilölliset käänteiset hakutoiminnot IPv6 Address -avaruudessa.


**Huomaa**: DNS-kyselyt voivat kulkea joko IPv4- tai IPv6-verkon kautta. Käytetty siirtoprotokolla ei vaikuta palautettavien tietueiden tyyppiin.

Esimerkiksi:


- IPv6-yhteyden kautta yhdistetty asiakas voi pyytää IPv4-tietuetta.
- IPv4-yhteyden kautta yhdistetty asiakas voi pyytää IPv6-tietuetta.

DNS-palvelin vastaa yksinkertaisesti tietueilla, jotka sillä on, riippumatta kyselyn siirtoprotokollasta.


Kun isäntänimi on yhdistetty sekä IPv4- että IPv6-verkkoon, Address:n valinta määräytyy RFC 6724:n mukaan, jossa määritellään Address:n valinta-algoritmi, joka perustuu muun muassa etuliitteen etusijaan, laajuuteen ja tavoitettavuuteen. Oletusarvoisesti IPv6 on yleensä ensisijainen, ellei järjestelmä- tai verkkokonfiguraatioita ole kumottu.


**Tärkeä muistutus**: Kun IPv6 Address upotetaan URL-osoitteeseen (*Uniform Resource Locator*), se on suljettava hakasulkeisiin (`[]`). Näin vältetään sekaannukset IPv6 Address:n sisällä olevan kaksoispisteen (`:`) ja URL-osoitteessa isäntänimen ja portin erottelevan kaksoispisteen välillä.


Kelvollinen esimerkki:


```shell
http://[2001:db8::1]:8080
```


Näin varmistetaan, että sekä selaimet että verkkopalvelimet käsittelevät URL-osoitteen oikein.


IPv6:n integroiminen DNS-järjestelmään edellyttää näin ollen uusia tietuetyyppejä, tiukkaa käänteisratkaisumenetelmää sekä tarkkoja valinta- ja muotoilusääntöjä reitityksen yhteensopivuuden ja johdonmukaisuuden varmistamiseksi.


### Osan yhteenveto


Tässä jaksossa tarkasteltiin IPv6-osoitteiden perusperiaatteita. Aloitimme tarkastelemalla IPv6 Address:n rakennetta: sen 128-bittistä pituutta, heksadesimaalista merkintätapaa ja yksinkertaistamissääntöjä, joita käytetään toistuvien nollasarjojen lyhentämiseen. Tämän rakenteen ansiosta IPv6 pystyy voittamaan IPv4:n Address-avaruuden rajoitukset ja takaamaan samalla skaalautuvuuden ja tehokkaan hierarkian.


Tämän jälkeen tarkasteltiin IPv6-osoitteiden eri luokkia: unicast-, anycast- ja multicast-osoitteita, ja selvitettiin yksityiskohtaisesti niiden soveltamisalaa, tyypillistä käyttöä ja edustusta Address-avaruudessa.


Seuraavaksi tarkasteltiin IPv6-osoitteiden määritysmenetelmiä paikallisverkossa joko manuaalisesti, DHCPv6-protokollan avulla tai käyttämällä tilattomia automaattisia konfigurointimekanismeja, kuten NDP:n tarjoamia. Näiden lähestymistapojen avulla laitteet voivat automaattisesti generate oman Address:nsä tarjotusta etuliitteestä ja MAC Address:stä (EUI-64:n kautta), ja ne tarjoavat samalla joustavuutta käyttöiän hallinnan ja yksityisyyden suojan suhteen.


Olemme myös kertoneet yksityiskohtaisesti, miten Address-lohkot jaetaan, alkaen IANA:sta, joka jakaa ne viidelle RIR:lle (*Registered Internet Regions*) ja sitten ISP:ille, jotka jakavat ne edelleen asiakkailleen aliverkoina (usein /48, mikä mahdollistaa 65536 /64-aliverkkoa). Erottelu _Provider Aggregatable_ (PA) ja _Provider Independent_ (PI) -lohkoihin auttaa hallitsemaan _multihoming_- tai palveluntarjoajanvaihtoskenaarioita.


Näimme, että DNS on mukautunut IPv6:een AAAA-tunnisteen käyttöönoton myötä ja että käänteisresoluutiomekanismit tukeutuvat nyt "ip6.arpa"-vyöhykkeeseen. Tärkeää on, että DNS pysyy riippumattomana käytetystä siirtoprotokollasta (IPv4 tai IPv6), mikä takaa saumattoman yhteentoimivuuden kaksivaiheisessa ympäristössä.


IPv6 ei siis ole vain asteittainen parannus IPv4:ään verrattuna, vaan osoitinjärjestelmän täydellinen uudelleensuunnittelu, joka on suunniteltu vastaamaan sekä nykyisiin että tuleviin maailmanlaajuisen Internetin haasteisiin.


Tämän NET 302 -kurssin viimeisessä osassa siirrytään käytäntöön ja keskitytään verkon diagnostiikkatyökaluihin.



# Verkon diagnostiikkatyökalut


<partId>368a5c6f-ec48-4b28-970f-3a770788ad37</partId>


## Verkkoyhteys Layer-työkalut


<chapterId>1d25a21d-6900-4fbe-a438-e06c8afb9e02</chapterId>


Tässä verkkodiagnostiikkaa käsittelevän viimeisen jakson ensimmäisessä luvussa keskitytään TCP/IP-mallin Layer-verkkoon pääsyn analysointiin tarkoitettuihin työkaluihin. Tämä Layer vastaa samassa fyysisessä verkossa olevien laitteiden välisestä suorasta viestinnästä erityisesti MAC-osoitteiden ja fyysisten verkkoliitäntöjen, kuten Ethernet-korttien tai Wi-Fi-liitäntöjen, avulla.


Tarkoituksena on tarjota ylläpitäjille käytännön työkaluja, joiden avulla he voivat tarkastaa, testata ja optimoida tämän tärkeän Layer:n matalan tason yhteyden. Näiden työkalujen avulla voidaan tarkistaa liitäntöjen moitteeton toiminta, korjata verkkokortin konfigurointiin liittyviä ongelmia tai havaita poikkeamia, kuten törmäyksiä, pakettihäviöitä tai linkkivirheitä.


### IP/MAC naapuruston apuohjelmat


#### `Arp` työkalu


Yksi Network Access Layer:n vanhimmista diagnostiikkatyökaluista on `arp`-komento. Vaikka se onkin yhä useammin korvattu nykyaikaisilla vaihtoehdoilla, kuten `ip neigh` (jonka me tulemme pian löytämään). `Arp` on edelleen monissa järjestelmissä ARP (*Address Resolution Protocol*) -välimuistin tarkastelemiseksi tai käsittelemiseksi. Tämä välimuisti tallentaa IP-osoitteiden ja koneen paikallisesti tunnettujen MAC-osoitteiden väliset yhdistelmät. Toisin sanoen sen avulla voidaan määrittää, mikä fyysinen (MAC) Address vastaa tiettyä IP Address:tä paikallisverkossa.


Käytännössä, kun isäntä haluaa lähettää paketin samassa aliverkossa olevalle IP Address:lle, sen on ensin tiedettävä kohdekoneen MAC Address. Tämä yhdistäminen hoidetaan ARP:llä, joka lähettää pyynnön paikallisverkkoon ja saa vastauksen, joka sisältää vastaavan MAC Address:n. Tämän jälkeen ARP:n avulla on mahdollista saada vastaus, joka sisältää MAC Address:n. Tulos tallennetaan sitten väliaikaisesti paikalliseen taulukkoon, jota kutsutaan "ARP-välimuistiksi", jotta pyyntöjä ei tarvitsisi toistaa jokaista uutta pakettia varten.


Voit tarkastella tämän välimuistin sisältöä ja tarkistaa koneen tällä hetkellä tuntemat merkinnät seuraavasti:


```bash
arp -a
```


Tämä komento listaa kaikki paikallisesti rekisteröidyt IP/MAC-kuvioinnit kaikissa liitännöissä. Kullakin rivillä ilmoitetaan isäntänimi (jos se on ratkaistavissa), IP Address, vastaava MAC Address ja Interface, jossa yhdistäminen on havaittu.


Jos haluat suodattaa näytön tiettyyn IP Address:een, määritä se yksinkertaisesti:


```bash
arp -a 192.168.1.5
```


Näin on helppo tarkistaa, onko välimuistissa tietty IP Address, mikä voi auttaa diagnosoimaan samassa verkossa olevien kahden isäntäkoneen välisiä yhteyshäiriöitä.


Vastaavasti voit näyttää vain tiettyyn verkkoon Interface (esimerkiksi Ethernet-kortti nimeltä `eth0`) liittyvät ARP-merkinnät käyttämällä:


```bash
arp -a -i eth0
```


Tämä on erityisen hyödyllistä useissa Interface-ympäristöissä (langallinen, langaton, VPN jne.), joissa yhdellä isännällä voi olla useita verkkosovittimia.


`arp`-komentoa ei ole rajoitettu vain lukukäyttöön. Sitä voidaan käyttää myös ARP-välimuistin manuaaliseen muokkaamiseen, mikä on korvaamaton ominaisuus tietyissä edistyneissä vianmääritysskenaarioissa tai simuloitaessa tiettyjä olosuhteita. Voit esimerkiksi lisätä manuaalisesti IP/MAC-kuvion:


```bash
arp -s 192.168.1.7 00:17:BC:56:4F:25 -i eth2
```


Tämä komento luo paikalliseen ARP-taulukkoon staattisen merkinnän, joka yhdistää IP Address `192.168.1.7` ja MAC Address `00:17:BC:56:4F:25` Interface `eth2`:ssa.Jos Interface:ää ei ole määritetty, järjestelmä käyttää automaattisesti ensimmäistä mahdollista Interface:ää.


Voit myös poistaa merkinnän ARP-välimuistista joko korjataksesi virheen tai pakottaaksesi uudelleenhaun:


```bash
arp -d 192.168.1.7
```


Tämä poistaa merkinnän ja varmistaa, että seuraava viestintäyritys käynnistää uuden ARP-pyynnön.


**HUOMAUTUS**: Poisto-vaihtoehto hyväksyy myös Interface-nimen, jolloin voit kohdistaa tietyn merkinnän poistamisen tarkemmin.


Yhteenvetona voidaan todeta, että arp-työkalu tarjoaa matalan tason diagnostiikkaa, joka on erityisen hyödyllinen paikallisverkoissa, joissa yhteysongelmat voidaan usein jäljittää virheelliseen tai vanhentuneeseen Address-resoluutioon. Viimeaikaisissa järjestelmissä, erityisesti nykyaikaisissa Linux-jakeluissa, tämä työkalu on kuitenkin yhä useammin korvattu `iproute2`-työkalupaketin `ip neigh`-komennolla, joka tarjoaa samanlaisia toimintoja yhtenäisemmissä puitteissa.


#### `Ip neigh`-työkalu


Nykyaikaisissa järjestelmissä, erityisesti uusimmissa Linux-jakeluissa, komento `ip neigh` on oikea työkalu IP- ja MAC-osoitteiden välisten yhdistelmien tarkasteluun ja hallintaan. Tämä komento on osa `iproute2`-pakettia, joka korvaa vähitellen vanhemmat työkalut, kuten `arp`, ja tarjoaa johdonmukaisemmat ja joustavammat puitteet datayhteyden Layer-diagnostiikkaan.


Komento `ip neigh` kysyy paikallista IP-nuorten välimuistia, joka vastaa IPv4:n ARP-välimuistia ja IPv6:n NDP-välimuistia (_Neighbor Discovery Protocol_). Tähän välimuistiin tallennetaan tunnetut IP-osoitteiden (v4 tai v6) ja MAC-osoitteiden väliset yhteydet sekä niiden tila (voimassa, odottava, vanhentunut...).


Peruskomento välimuistin näyttämiseksi on:


```bash
ip neigh
```


Tämä tuottaa luettelon merkinnöistä, joissa näkyy kohde-IP Address, asianomainen verkko Interface, siihen liittyvä MAC Address (jos saatavilla) ja merkinnän tila (esim. "SAAVUTETTAVISSSA", "PYSÄYTYNYT", "VIIVÄSTYNYT", "Epäonnistunut"...).


Esimerkkitulos:


```bash
192.168.1.5 dev eth0 lladdr 00:17:BC:56:4F:25 REACHABLE
```


Tämä rivi osoittaa, että kone tietää kelvollisen yhdistelmän IP Address `192.168.1.5` ja MAC Address `00:17:BC:56:4F:25` välillä Interface `eth0` kautta.


Voit myös suodattaa merkintöjä kriteerien, kuten IP Address, Interface tai tila, perusteella. Voit esimerkiksi kysyä vain Address `192.168.1.7`:


```bash
ip neigh show 192.168.1.7
```


Tai näyttääksesi kaikki Interface:n `eth1` merkinnät:


```bash
ip neigh show dev eth1
```


Kuulemisen lisäksi `ip neigh`:llä voidaan myös muokata välimuistia manuaalisesti. Esimerkiksi staattisen merkinnän lisäämiseen:


```bash
ip neigh add 192.168.1.7 lladdr 00:17:BC:56:4F:25 dev eth1 nud permanent
```


Tämä yhdistää pysyvästi IP Address:n `192.168.1.7` määritettyyn MAC Address:een Interface:ssä `eth1`. Vaihtoehto `nud permanent` (_Neighbor Unreachability Detection_) varmistaa, että merkintää ei mitätöidä automaattisesti.


Käänteisesti, jos haluat poistaa välimuistitietueen:


```bash
ip neigh del 192.168.1.7 dev eth1
```


Tämä pakottaa järjestelmän ratkaisemaan kartoituksen uudelleen, kun se seuraavan kerran kommunikoi kyseisen Address:n kanssa.


**HUOMAUTUS**: `ip neigh`-työkalu toimii sekä IPv4:lle että IPv6:lle. IPv4:ssä se toimii ARP:n kanssa ja IPv6:ssa NDP:n kanssa. Tämä tarjoaa yhtenäisen, johdonmukaisen lähestymistavan IP/MAC-suhteiden hallintaan eri protokollaperheissä, mikä tekee `ip neigh`:stä nykyaikaisen standardin naapureiden hallintaan Linux-järjestelmissä.


### Pakettianalyysityökalut


Jotta ylläpitäjät voivat analysoida perusteellisesti, mitä tietokoneverkossa tapahtuu, he tarvitsevat työkaluja, joilla voidaan kaapata koneiden välillä vaihdetut paketit. Kaksi apuohjelmaa erottuu vertailukohteiksi: `tcpdump` ja `Wireshark`. Nämä työkalut ovat välttämättömiä epänormaalin käyttäytymisen diagnosoinnissa, protokollanvaihdon tarkastamisessa tai verkon turvallisuuden tutkimisessa tarkastelemalla kehysten sisältöä.


#### `ttcpdump`: komentorivianalyysi


`tcpdump` on erittäin tehokas komentorivityökalu, joka on suunniteltu kaappaamaan ja näyttämään verkon kautta kulkevia paketteja Interface. Se toimii reaaliajassa, ja kevyen rakenteensa ansiosta sitä voidaan käyttää järjestelmissä, joissa ei ole graafista Interface:ää tai joiden resurssit ovat rajalliset. Se perustuu `libpcap`-kirjastoon, joka tarjoaa laitteistoriippumattomia matalan tason kaappaustoimintoja.


Yleinen käyttötapa `tcpdumpille` on seurata koneen tai verkkosegmentin verkkotoimintaa suodattamalla paketteja tiettyjen kriteerien mukaan. Tulokset voidaan ohjata tiedostoon, jolloin liikenne voidaan arkistoida myöhempää analysointia varten tai toistaa toisella työkalulla, kuten Wiresharkilla.


Komennon yleinen syntaksi on:


```bash
tcpdump -w <file.cap> -i <interface> -s <snapshot_length> -n <filters>
```



- `-w` kirjoittaa kaapatut paketit tiedostoon `libpcap`-muodossa (tiedostopääte `.cap` tai `.pcap`);
- `-i` määrittää Interface-verkon, jota tarkkaillaan (esim. `eth0`, `wlan0`);
- `-s` asettaa pakettia kohden kaapattavan tiedon enimmäismäärän. Määrittämällä `0` kaikki paketit otetaan talteen;
- `-n` poistaa DNS:n ja palveluiden nimien resoluution käytöstä, mikä parantaa suorituskykyä.


Komennon lopussa olevien lausekesuodattimien avulla voit rajoittaa kaappaukset tiettyyn osajoukkoon liikennettä. Voit yhdistää avainsanoja `host`, `port`, `src`, `dst` jne. valinnan tarkentamiseksi.


Esimerkki: HTTP-pakettien (portti 80) kaappaaminen palvelimelle tai palvelimelta `192.168.25.24` ja niiden tallentaminen tiedostoon `fichier.cap`:


```bash
tcpdump -w fichier.cap -i eth0 -s 0 -n port 80 and host 192.168.25.24
```


Tuloksena syntyvä tiedosto voidaan myöhemmin analysoida graafisella työkalulla tai toistaa toisessa järjestelmässä.


#### Wireshark: kehittynyt visuaalinen analyysi


Wireshark, joka tunnettiin aiemmin nimellä *Ethereal*, on täydellinen verkkoanalyysiohjelma, jossa on graafinen Interface. Toisin kuin `tcpdump`, se tarjoaa pakettien jäsennellyn, yksityiskohtaisen visualisoinnin, mukaan lukien protokollan analysointi, virtauskaaviot, liikennetilastot ja interaktiiviset suodattimet. Se perustuu myös `libpcap`:iin, mikä tarkoittaa, että se voi avata ja käsitellä `tcpdump`:n tuottamia kaappaustiedostoja.


Wireshark on saatavilla moniin käyttöjärjestelmiin, kuten Linuxiin ja Windowsiin. Sen asentaminen edellyttää järjestelmänvalvojan oikeuksia, jotta kaappauskäyttöliittymiä voidaan käyttää. Kun se on käynnistetty, voit valita verkon Interface *Capture*-valikosta. Napsauttamalla *Start* aloitetaan reaaliaikainen pakettitallennus. Näyttö on jaettu kolmeen ruutuun:


- luettelo kaapatuista kuvista ;
- protokollaan dekoodatut tiedot,
- raa'at heksadesimaaliset tiedot.



![Image](assets/fr/052.webp)



Wireshark on erinomainen skenaarioissa, joissa sinun on tarkkailtava monimutkaista protokollakäyttäytymistä, rekonstruoitava sovellusdialogit (kuten HTTP- tai DNS-istunto) tai tutkittava palvelun vasteaikoja. Se tukee myös erittäin tarkkoja näyttösuodattimia, joissa käytetään erityistä syntaksia (joka eroaa `tcpdump`:n syntaksista), jotta voidaan keskittyä vain olennaisiin paketteihin.


#### Täydentävät välineet


On tärkeää huomata, että `tcpdump` ja Wireshark eivät ole keskenään vaihdettavissa: kummallakin on omat vahvuutensa. `tcpdump` soveltuu paremmin komentoriviympäristöihin, automatisoituihin skripteihin ja etäpalvelimiin puuttumiseen, kun taas Wireshark on ihanteellinen yksityiskohtaiseen, vuorovaikutteiseen ja opettavaiseen liikenteen analysointiin.


Nämä kaksi työkalua voidaan yhdistää: kaappaus voidaan tehdä etäjärjestelmässä `tcpdump`-ohjelmalla, jonka jälkeen `.cap`-tiedosto siirretään analysoitavaksi Wiresharkilla paikallisella koneella. Tätä lähestymistapaa käytetään käytännössä laajalti.


### Interface-analyysityökalut


Network Access Layer:ssa on usein tarpeen kysyä ja määrittää fyysisiä verkkoliitäntöjä toimintahäiriöiden diagnosoimiseksi, suorituskyvyn optimoimiseksi tai yhteyden eheyden tarkistamiseksi. Yksi tehokkaimmista Linuxissa käytettävissä olevista työkaluista tähän tarkoitukseen on `ethtool`, komentorivin apuohjelma, joka antaa yksityiskohtaisia teknisiä tietoja Ethernet Interface:stä ja jonka avulla voit myös säätää joitakin sen parametreja reaaliajassa.


#### Katso Interface:n tekniset tiedot


`ethtoolin` keskeinen ominaisuus on sen kyky kysyä Interface:lta ja näyttää sen nykyiset ominaisuudet. Näin voit tarkistaa:


- linkin nopeus (esim. 100 Mbit/s, 1 Gbit/s tai 10 Gbit/s) ;
- neuvottelutila (half duplex tai full duplex) ;
- onko autonegotiation käytössä;
- portin tyyppi (kupari, kuitu jne.) ;
- linkin tila (aktiivinen vai ei) ;
- tuki lisäominaisuuksille, kuten *Wake-on-LAN*.


Nämä tiedot ovat erityisen hyödyllisiä diagnosoitaessa ongelmia, jotka liittyvät fyysiseen liitettävyyteen tai epäsopiviin neuvotteluasetuksiin isäntäverkkokortin ja sen liitettävän laitteen (kytkin, reititin jne.) välillä.


Saat nämä tiedot yksinkertaisesti suorittamalla:


```bash
ethtool enp0s3
```


Tämä komento antaa yksityiskohtaisen raportin `enp0s3` Interface:sta, joka on yleinen nimityskäytäntö CentOS- tai RHEL-pohjaisissa järjestelmissä.



![Image](assets/fr/053.webp)



#### Interface:n parametrien dynaaminen muokkaaminen


`ethtool` ei rajoitu vain havainnointiin: sen avulla voit myös säätää tiettyjä Interface:n parametreja käynnistämättä konetta uudelleen. Näin voidaan esimerkiksi pakottaa tietty yhteysnopeus tai ottaa käyttöön ominaisuuksia lähiverkon tarpeiden mukaan.


Option `-s` avulla voidaan määrittää dynaamisesti parametrit, kuten:


- linkin nopeus (`speed`), joka asetetaan yksiselitteisesti (esim. 1000 1 Gbit/s:lle) ;
- duplex-tila (`duplex`), joko `half` tai `full`;
- autonegotiation (`autoneg`) ottaminen käyttöön tai poistaminen käytöstä ;
- *Wake-on-LAN* (`wol`) käyttöönotto ;
- porttityyppi.


Esimerkki 1: ota autonegotiation käyttöön Interface:ssa:


```bash
ethtool -s enp0s3 autoneg on
```


Esimerkki 2: Ota käyttöön *Wake-on-LAN*-ominaisuus (jotta kone voi herätä etänä magic-paketin avulla):


```bash
ethtool -s enp0s3 wol p
```


Tässä esimerkissä optio `p` määrittää, että herätys tapahtuu heti, kun *Wake-on-LAN*-paketti havaitaan. Tätä asetusta käytetään usein yritysympäristöissä yön yli tapahtuviin päivityksiin tai etähuoltoon.


#### Työkalun asennus


On tärkeää huomata, että `ethtool` ei ole aina oletusarvoisesti asennettuna. Red Hat/CentOS-jakeluissa se voidaan asentaa komennolla:


```bash
yum install -y ethtool
```


Debianissa ja Ubuntussa vastaava komento on:


```bash
sudo apt install ethtool
```


**VAROITUS**: Kaikissa `ethtool`-komennoissa Interface-verkon nimi on ilmoitettava heti vaihtoehdon jälkeen (kuten `-s`). Mikä tahansa syntaksivirhe parametrien sijoittelussa tekee komennosta pätemättömän tai tehottoman.



## Verkko Layer-työkalut


<chapterId>d2c5bf35-4284-4af8-8e8b-049c696a511b</chapterId>


### Liikenneanalyysityökalut


Verkkodiagnostiikassa `ping`-komento on edelleen yksi yksinkertaisimmista mutta tehokkaimmista työkaluista kahden koneen välisen yhteyden testaamiseen. Se tarkistaa, onko etäisäntä tavoitettavissa tiettynä ajankohtana, ja antaa samalla tietoa latenssista, linkin vakaudesta ja DNS-ratkaisusta.


`ping`-komento perustuu ICMP-protokollaan (*Internet Control Message Protocol*). Kun käyttäjä lähettää `ping`-pyynnön, järjestelmä lähettää ICMP "Echo Request" -paketin IP Address:lle tai isäntänimelle. Jos kohdekone on verkossa ja verkkopolku on kelvollinen, se vastaa ICMP-"Echo Reply"-paketilla. Tätä yksinkertaista mekanismia voidaan käyttää viiveen mittaamiseen ja yhteys- tai nimenratkaisuongelmien havaitsemiseen.


Esimerkki klassisesta komennosta:


```bash
ping 172.17.18.19
```


Tyypillinen vastaus:


```bash
mydmn.org (172.17.18.19): 56 data bytes
64 bytes from 172.17.18.19: icmp_seq=0 ttl=56 time=7.7 ms
64 bytes from 172.17.18.19: icmp_seq=1 ttl=56 time=6.0 ms
64 bytes from 172.17.18.19: icmp_seq=2 ttl=56 time=5.5 ms
```


Tässä esimerkissä nimenmääritys on suoritettu automaattisesti: verkkotunnus `mydmn.org` on yhdistetty IP Address:een `172.17.18.19`, mikä vahvistaa, että DNS-ratkaisu toimii oikein. Komento antaa myös teknisiä tietoja, kuten:


- iCMP-järjestysnumero (`icmp_seq`), joka on hyödyllinen vastausten järjestyksen tarkistamisessa;
- TTL (*Time-To-Live*), joka ilmaisee jäljellä olevien siirtymisten määrän ennen paketin hylkäämistä;
- meno-paluuaika/viive (`time`) millisekunteina ilmaistuna, joka antaa arvion linkin viiveestä.


#### ICMP-parametrien yksityiskohtaisempi analyysi


TTL on IP-protokollan kriittinen kenttä. Lähettäjä alustaa jokaisen datagrammin TTL-arvolla (usein 64, 128 tai 255). Jos TTL-arvo saavuttaa arvon 0 ennen määränpään saavuttamista, paketti hylätään ja lähettäjälle lähetetään ICMP-virheilmoitus. Tämä mekanismi estää loputtomat reitityssilmukat.


Etenemisaika (*kierrosviive/aika*) mittaa viiveen, jolla paketti lähtee lähettäjältä, saapuu kohteeseen ja palaa takaisin. Käytännössä alle 200 ms:n viivettä pidetään hyväksyttävänä vakaan linkin osalta. Poikkeuksellisen suuret viiveet voivat olla merkki verkon ruuhkautumisesta, tehottomasta reitityksestä tai linkin huonosta laadusta.


#### Edistynyt `ping` käyttö


`ping` tarjoaa vaihtoehtoja testien tarkentamiseen ja erityisten verkkokäyttäytymistapojen tarkkailuun.


Lähetyspyyntöjen lähettämiseen voit käyttää `-b`-vaihtoehtoa, joka kohdistuu kaikkiin aliverkon isäntäkoneisiin:

```bash
ping -b 192.168.1.255
```


Tämä on hyödyllistä paikallisverkoissa aktiivisten isäntien nopeaan havaitsemiseen tai sen testaamiseen, miten verkko käsittelee lähetyspyyntöjä. Monissa kokoonpanoissa reitittimet ja palomuurit kuitenkin estävät lähetyspingit estääkseen vahvistushyökkäykset.


Voit myös määrittää mukautetun aikavälin pyyntöjen välille `-i`-valinnalla (oletus: 1 sekunti):


```bash
ping -i 0.2 -c 10 192.168.1.7
```


Tämä lähettää 10 ICMP-pyyntöä 0,2 sekunnin välein. Tällainen testaus on hyödyllinen, kun halutaan havaita latenssivaihtelut lyhyellä aikavälillä tai kun linkkiä rasitetaan kevyesti sen vakauden arvioimiseksi.


### Reititystaulukon analysointityökalut


Komento `ip route`, joka on osa `iproute2`-sarjaa, on nykyaikaisissa Linux-järjestelmissä suositeltava ja vakiovarusteinen työkalu ytimen IP-reititystaulukon tarkasteluun ja hallintaan. Se korvaa vanhentuneen `route`-komennon ja tarjoaa selkeämmän syntaksin, suuremman johdonmukaisuuden ja laajennetun tuen nykyaikaisille ominaisuuksille (IPv6, useat taulut, nimiavaruudet jne.).


#### Reititystaulukon näyttäminen


Nykyisen reititystaulukon näyttäminen:


```bash
ip route show
```


Tässä tulosteessa luetellaan kaikki ytimen tuntemat reitit eli lähtevien pakettien reitit määränpään mukaan.


Esimerkkitulos:


```bash
default via 192.168.1.1 dev eth0 proto dhcp metric 100
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```


Jokainen viiva edustaa reittiä. Keskeisiä kenttiä ovat mm:


- default**: oletusreitti, jota käytetään, kun mitään tarkempaa reittiä ei löydy.
- via**: yhdyskäytävä, jota käytetään määränpäähän pääsemiseksi.
- dev**: käytetty Interface-verkko.
- proto**: miten reitti luotiin (manuaalinen, DHCP, kernel jne.).
- metric**: reitin kustannukset, joita käytetään useiden mahdollisten reittien priorisointiin.
- scope**: reitin laajuus (esim. `link` suoraan yhdistetylle reitille).
- src**: lähde-IP Address, jota käytetään tämän Interface:n lähtevissä paketeissa.


#### Reittien lisääminen ja poistaminen


Reititystaulukkoa voi muokata myös dynaamisesti, esimerkiksi lisäämällä tai poistamalla staattisia reittejä.


Staattisen reitin lisääminen:


```bash
ip route add 192.168.1.0/24 via 192.168.1.1 dev eth0
```


Tämä määrittää reitin verkkoon 192.168.1.0/24 Interface:n "eth0"-yhdyskäytävän 192.168.1.1 kautta.


Poista tämä reitti:


```bash
ip route del 192.168.1.0/24
```


Tämä komento poistaa aiemmin määritetyn reitin.


#### Hyödyllisiä komentoja


Seuraavassa on muutamia hyödyllisiä muunnelmia analyysejä tai skriptausta varten:


- `ip -4 route`: näyttää vain IPv4-reitit;
- `ip -6 route`: näyttää vain IPv6-reitit;
- `ip route list table main`: näyttää pääreititystaulukon (oletusarvo) ;
- `ip route get <Address>`: näyttää, mitä Interface:tä ja yhdyskäytävää tiettyyn Address:een lähetettävä paketti käyttäisi.


Esimerkki:


```bash
ip route get 8.8.8.8
```


Tämä näyttää tarkan reitin, jonka paketti kulkisi saavuttaakseen kohdan `8.8.8.8.8`.


### Jäljitystyökalut


Yksi tehokkaimmista työkaluista IP-pakettien kulkeman reitin analysointiin lähdeaseman ja määränpään välillä on `traceroute`-komento. Se näyttää askel askeleelta pakettien kulkeman reitin ja yksilöi niiden kulkemat välireitittimet. Jos verkkoyhteydessä on toimintahäiriö tai palvelukatkos, `traceroute` auttaa määrittämään ongelman tarkan sijainnin.


Kuten `ping`-komennon kohdalla, kohde voidaan määrittää joko sen FQDN-nimen (fully qualified domain name) tai IP Address:n avulla. Esimerkiksi:


```bash
traceroute mydmn.org
```


#### Toimintaperiaate


`traceroute` luottaa IP-pakettien otsikon TTL-kenttään (*Time To Live*). Kuten aiemmin selitettiin, tämä kenttä on laskuri, jonka jokainen reititin vähentää polun varrella. Kun TTL saavuttaa nollan, paketti hylätään, ja reititin lähettää lähettäjälle ICMP-viestin "Time Exceeded". Tämä mekanismi estää loputtomat silmukat väärän reitityksen sattuessa.


`traceroute` hyödyntää tätä käyttäytymistä kartoittaakseen lähettäjän ja vastaanottajan väliset reitittimet:


- Se lähettää ensin sarjan UDP-paketteja (yleensä kolme), joiden TTL on 1. Ensimmäinen reititin saa TTL:ksi 0, joten se hylkää paketin ja vastaa ICMP-viestillä, jossa se ilmoittaa IP Address:nsa ja vastausajan.
- Seuraavaksi se lähettää toisen sarjan paketteja, joiden TTL on 2, ja paljastaa toisen reitittimen.
- Prosessi toistuu, kunnes määränpää on saavutettu, jolloin isäntä vastaa ICMP Port Unreachable -viestillä osoittaen, että päätepiste on saavutettu.


Oletusarvoisesti `traceroute` käyttää UDP-paketteja, jotka lähetetään käyttämättömiin portteihin (tyypillisesti alkaen 33434), mutta se voidaan myös määrittää käyttämään ICMP:tä (kuten `ping`) tai jopa TCP:tä järjestelmästä tai komentomuunnoksesta riippuen.


Esimerkkitulos:


```bash
traceroute to www.google.fr (216.58.210.35), 64 hops max, 52 byte packets

1  par81-024.ff.avast.com (62.210.189.205)   25.107 ms  24.235 ms  24.383 ms
2  62-210-189-1.rev.poneytelecom.eu (62.210.189.1)  27.341 ms  27.119 ms  28.184 ms
3  a9k1-45x-s43-1.dc3.poneytelecom.eu (195.154.1.92)  25.910 ms  25.040 ms  25.558 ms
4  72.14.218.182 (72.14.218.182)  36.234 ms  39.907 ms  38.130 ms
5  108.170.244.177 (108.170.244.177)  25.880 ms
108.170.244.240 (108.170.244.240)  25.791 ms
108.170.244.177 (108.170.244.177)  26.449 ms
6  216.239.62.143 (216.239.62.143)  26.491 ms
216.239.43.157 (216.239.43.157)  26.414 ms
216.239.62.139 (216.239.62.139)  26.400 ms
...
9  108.170.246.161 (108.170.246.161)  33.174 ms
108.170.246.129 (108.170.246.129)  34.342 ms
108.170.246.161 (108.170.246.161)  33.707 ms
10  108.170.232.105 (108.170.232.105)  33.845 ms  33.846 ms
108.170.232.103 (108.170.232.103)  34.206 ms
11  lhr25s11-in-f35.1e100.net (216.58.210.35)  34.094 ms  33.353 ms  33.718 ms
```


Kukin rivi vastaa reititintä, jonka kautta kuljetaan, ja enintään kolme aikamittausta (millisekunneissa) osoittaa reitittimen edestakaisen matkan viiveen. Nämä arvot auttavat arvioimaan kunkin verkkosegmentin suorituskykyä.


#### Tulosten tulkinta


Jos reititin ei vastaa tai suodattaa ICMP-viestejä, vastausajan sijasta näytetään tähtimerkit `*`. Tämä voi merkitä seuraavaa:


- palomuuri, joka estää ICMP-vastaukset,
- laite, joka on konfiguroitu vastaamattomaksi, tai
- tilapäinen yhteysongelma reitillä.


Traceroute" ei siis ainoastaan tunnista käytettyä reittiä, vaan se myös korostaa epänormaalin viiveen tai katkosten kohtia.


Joissakin järjestelmissä voidaan käyttää vastaavaa komentoa `tracepath`, joka ei vaadi pääkäyttäjän oikeuksia. IPv6:n tapauksessa käytä `traceroute6` tai `tracepath6`.


Esimerkki IPv6-seurannasta:


```bash
traceroute6 ipv6.google.com
```


### Työkalut aktiivisten yhteyksien tarkistamiseen


Aktiivisten verkkoyhteyksien diagnosoimiseksi ja verkon toiminnan seuraamiseksi Linux-järjestelmässä komento `ss` (lyhenne sanoista _socket statistics_) on nykyaikainen vertailutyökalu. Se on osa `iproute2`-pakettia, ja se korvaa nykyään poistuneen `netstat`:n. Se tarjoaa paremman suorituskyvyn ja tarkemmat tulokset.


`ss` näyttää aktiiviset TCP- ja UDP-yhteydet, kuuntelevat portit, paikalliset ja etäosoitteet, yhteyksien tilat ja niihin liittyvät prosessit.


#### Yleinen käyttö


Kun komento `ss` ajetaan ilman asetuksia, se näyttää aktiiviset TCP-yhteydet. Perussyntaksi:


```bash
ss [options]
```


Joitakin yleisiä vaihtoehtoja analyysin tarkentamiseksi:


- `-t`: näyttää vain TCP-yhteydet;
- `-u`: näyttää vain UDP-yhteydet;
- `-l`: näyttää vain kuuntelevat pistorasiat;
- `-n`: nimierotuksen poistaminen käytöstä (raa'at IP-osoitteet ja porttinumerot) ;
- `-p`: näyttää jokaisen pistorasiaan liittyvän prosessin (PID ja ohjelman nimi),
- `-a`: näytä kaikki yhteydet, myös inaktiiviset,
- `-s`: näyttää korkean tason socket-tilastot.


#### Tapaustutkimukset


Kaikkien TCP-porttia 80 (HTTP) käyttävien aktiivisten yhteyksien näyttäminen:


```bash
ss -ant | grep ':80'
```


Tämä näyttää aktiiviset TCP-yhteydet, joihin liittyy portti 80. Tilat, kuten `LISTEN`, `ESTABLISHED` ja `TIME-WAIT`, osoittavat kunkin Exchange:n nykyisen tilan.


Esimerkkitulos:

```
ESTAB 0 0 192.168.1.10:54321  93.184.216.34:80
```


Voit näyttää kaikki verkkoyhteydet ja niihin liittyvät prosessit:


```bash
ss -tulnp
```


Voit saada yleisen pistorasian käyttöyhteenvedon:

```bash
ss -s
```


Suodattaa vain UDP-yhteyksiä:

```bash
ss -unp
```


Nämä komennot ovat erityisen hyödyllisiä epäilyttävien yhteyksien ja odottamattomien kuunteluporttien havaitsemisessa tai tietyn palvelun toiminnan valvonnassa.


## Layer-työkalujen kuljettaminen ja huipulle asettaminen


<chapterId>bce47931-930e-4288-b0fd-666c9a1066b5</chapterId>


### DNS-kyselytyökalut


TCP/IP-mallin ylemmillä kerroksilla, erityisesti sovellus-Layer:ssa, on tärkeää ymmärtää, miten nimien resoluutio toimii. DNS-kyselytyökalujen avulla voit tarkistaa, liittyykö verkkotunnus oikein IP-osoitteeseen Address, ja ne auttavat myös diagnosoimaan DNS-palvelinongelmia, kuten vääränlaista konfigurointia, leviämisviiveitä tai käyttämättömyyttä. Nämä työkalut ovat välttämättömiä kaikille verkonvalvojille tai käyttäjille, jotka haluavat ymmärtää DNS-vaihtoja IP-ympäristössä.


#### Komento `nslookup`


Yksinkertaisin DNS-kyselytyökalu on `nslookup`. Se lähettää kyselyn DNS-palvelimelle ja palauttaa verkkotunnukseen liittyvän IP Address:n (tai päinvastoin). Oletusarvoisesti se kysyy järjestelmän määritettyä DNS-palvelinta, mutta voit myös määrittää palvelimen suoraan komennossa.


Esimerkki suorasta hausta:

```bash
nslookup mydmn.org
```


Tietyn DNS-palvelimen kysely:

```bash
nslookup mydmn.org 192.6.23.4
```


Pyyntö pyytää DNS-palvelinta osoitteessa `192.6.23.4` ratkaisemaan nimen `mydmn.org`. Tämä on erityisen hyödyllinen, kun halutaan tarkistaa, tunnistaako tietty DNS-palvelin verkkotunnuksen nimen, tai tarkistaa, että palvelin toimii oikein.


#### Komento `dig`


`dig` (*Domain Information Groper*) on nykyaikaisempi, täydellisempi ja joustavampi työkalu kuin `nslookup`. Se tukee monimutkaisia kyselyjä ja antaa yksityiskohtaista tietoa ratkaisuprosessista, mukana olleiden palvelimien hierarkiasta, palautetun tietueen tyypistä (A, AAAA, MX, TXT jne.) ja mahdollisista virheistä.


Esimerkki peruskyselystä:

```bash
dig mydmn.org
```


Tietyn DNS-palvelimen kysely:

```bash
dig @192.6.23.4 mydmn.org
```


Tämä komento tarkistaa DNS-tietueen saatavuuden tietyllä palvelimella.

Yksi `dig`:n tärkeimmistä eduista on se, että se näyttää DNS-vastauksen yksityiskohdat, mikä tekee siitä erittäin hyödyllisen konfiguraatiovirheiden diagnosoinnissa.


#### DNS-resolverien manuaalinen konfigurointi


Joskus on tarpeen ohittaa paikallisesti käytettävät DNS-palvelimet, esimerkiksi testiympäristöissä tai pakottaa käyttämään tiettyjä palvelimia. Tämä voidaan tehdä muokkaamalla `/etc/resolv.conf`-tiedostoa, jossa määritellään järjestelmän DNS-resoluutioasetukset.


Esimerkkikokoonpano:


```bash
vi /etc/resolv.conf

search mydmn.org
nameserver 192.168.1.10
nameserver 192.168.1.11
```



- Haku-kentässä määritetään verkkotunnus, joka liitetään automaattisesti, kun lyhyitä nimiä ratkaistaan.
- `nameserver`-merkinnät määrittelevät käytettävät DNS-palvelimet tärkeysjärjestyksessä.


Monissa nykyaikaisissa jakeluissa (erityisesti niissä, jotka käyttävät `systemd-resolved`-ohjelmaa) muutokset `/etc/resolv.conf`-tiedostoon ovat väliaikaisia, ja ne saatetaan korvata uudelleenkäynnistyksen tai verkon uudelleenkytkennän yhteydessä. Pysyvämpiä menetelmiä ovat esimerkiksi `resolvconf`:n, `systemd-resolved`:n tai *NetworkManager*-konfiguraatioiden muuttaminen.


#### Komento `host`


Toinen yksinkertainen mutta tehokas DNS-työkalu on `host`. Se ratkaisee verkkotunnukset IP-osoitteiksi (tai päinvastoin) ja voi auttaa diagnosoimaan DNS-vikoja tai -virheitä verkossa Interface.


Esimerkkejä:

```bash
host mydmn.org
```


Käänteinen haku:

```bash
host 192.6.23.4
```


`host` on erityisen kätevä nopeisiin tarkistuksiin, varsinkin kun sitä käytetään komentoriviskripteissä.


Toistuvat tai intensiiviset kyselyt kolmannen osapuolen DNS-palvelimille ilman lupaa voidaan tulkita tunkeutumisyrityksiksi tai haitalliseksi toiminnaksi. Väärin käytettynä tai sellaisia verkkoja vastaan, joita et hallitse, nämä komennot voivat muistuttaa tiedustelutarkistuksia, jotka ovat usein hyökkäyksen ensimmäinen vaihe. Rajoita niiden käyttö aina ympäristöihin, joita hallinnoit tai joihin sinulla on nimenomainen valtuutus.


### Verkon skannaustyökalut


Paikallis- tai laajakaistaverkkoa valvottaessa tai suojattaessa on tärkeää tunnistaa aktiiviset laitteet ja niiden tarjoamat palvelut. Juuri tätä tekee `nmap` (*Network Mapper*) -työkalu.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

#### Esittelyssä `nmap`


`nmap` mahdollistaa yhden tai useamman isäntäkoneen kohdennetun skannauksen avoimien porttien, käytettävissä olevien palveluiden (HTTP, SSH, DNS jne.) ja joskus jopa käytössä olevan käyttöjärjestelmän tunnistamiseksi. Monien vaihtoehtojensa ansiosta `nmap` antaa tarkan yleiskuvan verkon altistumisrajasta, mikä on välttämätöntä infrastruktuurin hallinnan auditointi- tai koventamisvaiheissa.


Aivan kuten komentoa `host`, komentoa `nmap` ei saa koskaan käyttää verkoissa tai infrastruktuureissa, joita et omista, tai ilman nimenomaista lupaa. Luvattomat porttiskannaukset voidaan merkitä pahantahtoisiksi tiedusteluyrityksiksi, ne havaitaan usein tietoturvajärjestelmissä (palomuurit, IDS/IPS), ja ne voivat johtaa jopa oikeudellisiin seurauksiin.


#### Peruskäyttö


Voit skannata tietyn isäntäkoneen ja tarkastella sen avoimia portteja:

```bash
nmap 192.168.0.1
```


Tämä komento skannaa isännän `192.168.0.1` 1000 yleisintä porttia ja näyttää käytetyt palvelut ja protokollat. Jos DNS-resoluutio on määritetty, voit käyttää myös isäntänimeä IP Address:n sijasta.


#### Täydellinen verkon skannaus


Yksi `nmap`:n eduista on sen kyky skannata koko osoitealue yhdellä komennolla. Näin on esimerkiksi helppo inventoida nopeasti kaikki verkon aktiiviset koneet:


```bash
nmap 192.168.0.0/24
```


Tässä tapauksessa kysytään kaikkia isäntiä alueella `192.168.0.0` - `192.168.0.255`. Tuloksissa luetellaan kunkin IP Address:n osalta avoimet portit, niiden tila (avoin, suodatettu jne.) ja mahdollisuuksien mukaan vastaavan palvelun nimi.



![Image](assets/fr/055.webp)



Järjestelmänvalvoja voi luottaa `nmap`:iin useissa tehtävissä:


- Aktiivisten isäntien havaitseminen**: tunnistaa, mitkä koneet vastaavat aliverkossa;
- Palveluinventaario**: varmista, että vain välttämättömiin portteihin on pääsy (vähiten etuoikeuksia koskeva periaate);
- Vaatimustenmukaisuuden tarkistus**: vertaa avoimia portteja organisaation tietoturvakäytäntöihin;
- Haavoittuvuuksien estäminen**: havaitse kriittisillä koneilla toimivat epävarmat tai vanhentuneet palvelut.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

### Prosessikyselytyökalut


Linuxin ylläpitäjät käyttävät usein komentoa `lsof` (*List Open Files*) analysoidakseen syvällisesti aktiivisia prosesseja ja avoimia tiedostoja, erityisesti verkkoympäristössä. Nimestään huolimatta `lsof` ei rajoitu vain perinteisiin tiedostoihin: UNIX-järjestelmissä tiedostona pidetään kaikkea, myös verkkopistorasioita, laitteita ja viestintäkanavia.


Työkalu tarjoaa siis järjestelmän läpileikkausnäkymän, jossa aktiiviset prosessit, avoimet verkkoportit, käytetyt tiedostot ja käyttäjät ovat yhteydessä toisiinsa.


#### Verkkoanalyysi `lsof`-ohjelmalla


Valinta `-i` rajoittaa tulostuksen verkkoyhteyksiin (TCP, UDP, IPv4 tai IPv6). Näin on helppo nähdä, mitkä prosessit kommunikoivat verkon kautta:


```bash
lsof -i
```


Tämä komento listaa kaikki käynnissä olevat prosessit, jotka käyttävät verkkoliitäntää, ja näyttää käytettävän portin, protokollan (TCP/UDP), yhteyden tilan sekä PID-tunnuksen ja siihen liittyvän käyttäjän.


#### Suodatus IP Address:n tai portin mukaan


Voit tarkentaa hakuja määrittämällä IP Address:n ja portin, jolloin voit eristää tietyn verkkovirran. Voit esimerkiksi tarkistaa SMTP-istunnon (portti 25) tietyn isännän kanssa:


```bash
lsof -n -i @192.168.2.1:25
```


Tämä näyttää vain aktiiviset verkkoyhteydet isäntään `192.168.2.1` portissa 25, mikä on hyödyllistä epäilyttävän toiminnan tai SMTP-virtausongelmien diagnosoimiseksi.


#### Laitteen käytön seuranta


Toinen `lsof`:n vahvuus on erikoistiedostojen, kuten levyosioiden, seuranta. Voit esimerkiksi tarkistaa, mitkä prosessit ovat avanneet tiedostoja levyllä `/dev/sda1`:


```bash
lsof /dev/sda1
```


Tämä on kätevää, kun irrotusyritys epäonnistuu, koska laite on edelleen käytössä, tai kun tutkitaan, mitkä sovellukset käyttävät osiota.


#### Ristiinanalyysi: prosessi ja verkosto


Vaihtoehtoja voidaan yhdistellä tarkkojen tietojen saamiseksi. Voit esimerkiksi nähdä kaikki verkkoportit, jotka on avannut prosessi, jonka PID on 1521:


```bash
lsof -i -a -p 1521
```


Vaihtoehto `-a` risteyttää kriteerit (`-i` ja `-p`), jolloin tuloste rajoitetaan koskemaan vain kyseisen prosessin verkkoyhteyksiä.


#### Monen käyttäjän seuranta


`lsof`:ia voidaan käyttää myös tiettyjen käyttäjien toiminnan analysointiin, jolloin kaikki heidän avaamansa tiedostot listataan, valinnaisesti PID:n mukaan suodatettuina:


```bash
lsof -p 1521 -u 500,phil
```


Tämä näyttää tiedostot tai verkkoyhteydet, joita käyttäjä `phil` tai UID 500 käyttää, rajoittuen prosessiin 1521.


### Jakson yhteenveto


Tässä viimeisessä osassa olemme tutustuneet moniin välttämättömiin työkaluihin, joita tarvitaan tietokoneverkkojen diagnosointiin, analysointiin ja hallintaan. Tämä TCP/IP-mallin kerrosten ympärille jäsennelty tutkimus selventää, miten verkkoviestintä toimii, ja luo myös tiukan menetelmän mahdollisten ongelmien tunnistamiseen, eristämiseen ja ratkaisemiseen.


Nämä työkalut antavat ylläpitäjille yhtenäisen joukon teknisiä vipuja, joiden avulla he voivat valvoa verkon kuntoa, analysoida liikennettä, tarkastaa yhteyksiä ja puuttua nopeasti viallisiin laitteisiin tai palveluihin.


#### Verkkoyhteys Layer


Työkalut, jotka tarjoavat suoran näkyvyyden rajapintoihin ja kehyksiin:


- arp / ip neigh**: tarkastaa ja muuttaa ARP/NDP-välimuistia IP-MAC-yhteyksien tarkistamiseksi tai korjaamiseksi;
- tcpdump**: komentorivin pakettikaappaus, suodatettavissa ja vietävissä;
- Wireshark**: graafinen pakettianalyysi ja syvällinen protokollan purku;
- ethtool**: Ethernet-kortin fyysisten parametrien (nopeus, duplex, WoL jne.) kysely ja säätö.


#### Verkko Layer


Työkalut IP-yhteyksien, reitityksen ja pakettiliikenteen arviointiin:


- ping**: testaa tavoitettavuutta ja mittaa viive ICMP:llä;
- ip route**: tarkastaa ja muuttaa reititystaulukkoa pakettien reitityksen hallitsemiseksi;
- traceroute**: reitittimien tunnistaminen hop-by-hop reitillä määränpäähän;
- ss**: yksityiskohtainen luettelo TCP/UDP-pistorasioista ja niihin liittyvistä prosesseista (netstatin seuraaja).


#### Liikenne- ja sovelluskerrokset


Työkalut palvelujen ja prosessien diagnosointiin:


- nslookup / dig / host**: DNS-kyselyt nimenmäärityksen vahvistamiseksi ja tietueiden analysoimiseksi;
- nmap**: tutki avoimia portteja ja avoimia palveluja hyökkäyspinnan arvioimiseksi;
- lsof**: listaa prosessien avaamat tiedostot ja socketit, korreloi järjestelmän ja verkon toimintaa.


Näiden TCP/IP-mallin tiettyä vaihetta vastaavien työkalujen hallitseminen mahdollistaa metodisen lähestymistavan: alkaen fyysisestä Layer:stä, siirtyen reitityksen kautta sovelluspalveluihin. Tämä asiantuntemuksen ketju antaa ylläpitäjille valmiudet diagnosoida, suojata ja optimoida infrastruktuuria ja varmistaa näin sekä verkon suorituskyvyn että käytettävyyden.


# Viimeinen osa


<partId>09d5393c-63bc-42fc-bf79-c65e380211bd</partId>


## Arvostelut & arvostelut


<chapterId>114c33c0-9831-4d74-affd-f5d37adc53c3</chapterId>


<isCourseReview>true</isCourseReview>

## Loppukoe


<chapterId>b99e005e-8dd0-4fa4-b302-f940c27a30ac</chapterId>


<isCourseExam>true</isCourseExam>

## Päätelmä


<chapterId>3b449814-78f3-41c0-8138-0a04f3682719</chapterId>


<isCourseConclusion>true</isCourseConclusion>