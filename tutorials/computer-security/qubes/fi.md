---
name: Qubes
description: Kohtuullisen turvallinen käyttöjärjestelmä.
---

![cover](assets/cover.webp)



Qubes OS on ilmainen, avoimen lähdekoodin käyttöjärjestelmä, joka on suunniteltu käyttäjille, joille turvallisuus on tärkeintä. Sen erityispiirre perustuu yksinkertaiseen mutta radikaaliin ajatukseen: sen sijaan, että tietokonetta pidettäisiin kokonaisuutena, sen käyttö jaetaan itsenäisiin lokeroihin, joita kutsutaan **_qubes_**.



Kukin qube toimii **eristettynä virtuaaliympäristönä**, jolla on tietty luottamustaso ja toiminto. Joten vaikka sovellus vaarantuisi, hyökkäys pysyy rajoitettuna sen qubeen vaikuttamatta muuhun järjestelmään.



> Jos suhtaudut vakavasti tietoturvaan, Qubes OS on paras tällä hetkellä saatavilla oleva käyttöjärjestelmä. - **Edward Snowden**.

Qubes OS:n asentaminen vaatii kuitenkin enemmän valmisteluja kuin perinteisen käyttöjärjestelmän asentaminen. Siihen kuuluu tiettyjen laitteistovaatimusten tarkistaminen, virtualisoinnin perusteiden ymmärtäminen ja erilaisen kokemuksen hyväksyminen, jossa jokainen päivittäinen tehtävä ajatellaan erillisenä. Mutta kun Qubes OS on otettu käyttöön, se tarjoaa vankan kehyksen, joka määrittelee uudelleen tavan, jolla olet päivittäin vuorovaikutuksessa tietokoneesi kanssa. Tässä opetusohjelmassa selitämme, miten Qubes OS toimii ja miten se asennetaan helposti järjestelmääsi.



## Miten Qubes OS toimii?



Qubes OS perustuu lokerointiperiaatteeseen. Yhden järjestelmän sijaan se luottaa **Xen**-hypervisoriin luodakseen eristettyjä virtuaalikoneita, joita kutsutaan qubesiksi. Kukin qube on omistettu tietylle tehtävälle tai luottamustasolle (työ, henkilökohtainen selailu, pankkiasiointi jne.). Tämä erottelu varmistaa, että yhden quben vaarantuminen ei voi levitä muihin qubeihin, vaan se toimii kuin useita itsenäisiä tietokoneita yhdessä koneessa.



Käyttäjää Interface hallinnoi keskitetty, suojattu verkkotunnus nimeltä **dom0**. Tämä verkkotunnus on täysin eristetty Internetistä, joten se on järjestelmän sydän. Vaikka ikkunat ja valikot näkyvät dom0:ssa, sovellusten varsinainen suoritus tapahtuu niiden omissa qubeissa.



## Erilaiset qubetyypit



Dom0:n ympärillä pyörii erityyppisiä qubeja, joilla kullakin on hyvin erityinen tehtävä.





- **AppVM**:ää käytetään jokapäiväisten sovellusten suorittamiseen: käyttäjä voi näin erottaa ammatilliset sähköpostiviestinsä verkkoselailusta tai pankkitoiminnoista siten, että kumpikin ympäristö on täysin riippumaton toisistaan.





- Nämä AppVM:t perustuvat **TemplateVM:iin**, jotka toimivat keskitettyinä malleina ohjelmistojen asentamista ja päivittämistä varten, jolloin jokaista qubea ei tarvitse hallita erikseen.



Qubes OS integroi myös virtuaalikoneita, jotka ovat erikoistuneet **järjestelmäpalveluihin**.





- **NetVM** hallinnoi suoraan **verkkolaitteita** ja varmistaa yhteyden Internetiin. Ne liittyvät usein **FirewallVM:iin**, jotka toimivat **suodattavat liikennettä** ja rajoittavat muiden qubien altistumista.





- ServiceVM:illä on samanlainen rooli esimerkiksi USB-laitteiden hallinnassa, ja niiden logiikka on aina sama: eristetään riskialttiimmat komponentit hyökkäyspinnan pienentämiseksi.



Satunnaisia tai riskialttiita tehtäviä varten Qubes OS tarjoaa **DisposableVM**. Nämä hetkelliset qubit luodaan lennossa **avata epäilyttävä asiakirja** tai **vierailla epäilyttävällä sivustolla**, ja ne katoavat kokonaan, kun ne suljetaan, jolloin kaikki jäljet häviävät ja pysyvät hyökkäykset estetään.



### Turvallinen kopiointimekanismi (qrexec)



Qubien välinen vaihto perustuu **qrexeciin**, joka on VM:ien välinen viestintäjärjestelmä, joka on suunniteltu turvallisuussyistä. Sen sijaan, että qubien annettaisiin kommunikoida vapaasti, qrexec asettaa **kohtaisia käytäntöjä**: AppVM:stä toiseen kopioitu tiedosto tai leikepöydän kautta siirretty teksti kulkee aina järjestelmän valvoman ja validoiman kanavan kautta. Tällä tavoin jopa yksinkertaista kopiointia ja liittämistä valvotaan haittaohjelmien leviämisen estämiseksi.



### Levynhallinta



Qubes OS käyttää nerokasta tallennuksenhallintajärjestelmää. TemplateVM:t sisältävät yhteisen ohjelmistopohjan, kun taas AppVM:t lisäävät vain henkilökohtaisia tietojaan ja erityistiedostojaan. Tämä vähentää levytilan käyttöä ja helpottaa maailmanlaajuisia päivityksiä. DisposableVM:t puolestaan käyttävät tilapäisiä volyymeja, jotka häviävät kokonaan, kun ne suljetaan. Tämä malli takaa paitsi paremman turvallisuuden myös tehokkaan resurssienhallinnan.



## Miksi valita Qubes OS?



Qubes OS:n edut ovat ennen kaikkea sen ainutlaatuisessa turvallisuusmallissa. Tämän lähestymistavan ytimessä on lokerointi, joka suojaa käyttäjää eristämällä kukin tehtävä erillisiin virtuaalikoneisiin. Käytännössä saastunut sähköposti tai haitallinen verkkosivusto voi vaarantaa vain yhden qubesin, jolloin muu järjestelmä ja henkilökohtaiset tiedot ovat täysin suojattuja. Tämä arkkitehtuuri rajoittaa huomattavasti monimutkaisia hyökkäyksiä, jotka perinteisessä järjestelmässä voisivat levitä vapaasti.



Qubes OS tarjoaa myös täydellisen läpinäkyvyyden ja digitaalisen ympäristön hallinnan. Tiedät tarkalleen, millä ohjelmistolla on pääsy mihinkin resurssiin, olipa kyseessä sitten verkko, USB-laite tai muut arkaluonteiset komponentit. Järjestelmä integroi oletuksena kehittyneet tietoturvaominaisuudet, kuten täyden levyn salauksen, ja helpottaa Whonix-käyttöjärjestelmän kaltaisten anonymisointipalvelujen käyttöä.



https://planb.network/tutorials/computer-security/operating-system/whonix-06f9172c-2962-412e-9487-b665d8ca9f59

Sen sijaan, että Qubes OS pyrkisi luomaan läpäisemättömän järjestelmän, se keskittyy joustavuuteen: se koteloi vahingot, jos järjestelmä vaarantuu, ja vähentää näin muuhun järjestelmään kohdistuvaa riskiä. Tämän käytännönläheisen lähestymistavan ansiosta Qubes OS on ensisijainen valinta käyttäjille, joilla on korkeat turvallisuustarpeet tai jotka haluavat säilyttää digitaalisen elämänsä mahdollisimman hyvin hallinnassa.



## Qubes OS:n asentaminen



Ennen Qubes OS:n asentamista on tärkeää varmistaa, että laitteistosi täyttää vähimmäisvaatimukset, sillä järjestelmä perustuu virtualisointiin qubesin eristämiseksi. Tärkeimmät tarkistettavat komponentit ovat :




- **Prosessori**: 64-bittinen prosessori, joka on yhteensopiva laitteistovirtualisoinnin kanssa (Intel VT-x tai AMD-V).
- RAM-muisti: vähintään 8 Gt vaaditaan, mutta suosittelemme vähintään 16 Gt:n RAM-muistia, jotta voit käyttää useita qubeja samanaikaisesti.
- **Tallennustila**: vähintään 36 Gt, mieluiten 128 Gt SSD-levyllä optimaalisen suorituskyvyn varmistamiseksi.



Asenna Qubes OS lataamalla virallinen ISO-kuva Qubes OS:n [viralliselta sivustolta](https://www.qubes-os.org/downloads/). On tärkeää tarkistaa ISO-tiedoston eheys käyttämällä annettuja GPG-allekirjoituksia, jotta voidaan varmistaa, että tiedostoa ei ole peukaloitu ja että lataus on turvallinen.



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

![0_01](assets/fr/01.webp)



Kun ISO on vahvistettu, sinun on luotava käynnistettävä asennusväline, yleensä USB-tikku. Lataa ja asenna tätä varten ohjelmisto, kuten **Rufus** Windowsissa tai **Etcher** Windowsissa, Linuxissa tai macOS:ssä. Näiden työkalujen avulla voit kopioida ISO-tiedoston USB-tikulle niin, että se on käynnistettävissä.



Ennen asennuksen aloittamista tietokoneen **BIOS tai UEFI** on määritettävä siten, että **virtualisointi** otetaan käyttöön ja käynnistys USB:ltä sallitaan. Koneen mallista riippuen saattaa olla tarpeen **poistaa Secure Boot** käytöstä, sillä Qubes OS ei ehkä käynnisty, jos tämä vaihtoehto on käytössä.



![0_02](assets/fr/02.webp)



Kun nämä edellytykset täyttyvät, käynnistä tietokone uudelleen ja avaa BIOS/UEFI painamalla välittömästi **Esc**, **Del**, **F9**, **F10**, **F11** tai **F12** (valmistajasta riippuen). Valitse käynnistysvalikossa USB-levy käynnistyslaitteeksi, jotta Qubes OS -asennus käynnistyy.



**Käynnistysnäyttö**


Kun käynnistät USB-muistitikulta, pääset suoraan **GRUB**-valikkoon, jossa voit valita suoritettavan toiminnon. Valitse näppäimistön nuolinäppäimillä "Install Qubes OS" ja paina "Enter".



![0_03](assets/fr/03.webp)



**Kielen valinta** :



Kun asennus käynnistyy, ensimmäinen vaihe on **valita kieli** ja **alueellinen vaihtoehto**, jotka sopivat kokoonpanoosi. Näin varmistetaan, että järjestelmä ja asennusvaihtoehdot näytetään oikein haluamallasi kielellä.



![0_04](assets/fr/04.webp)



**Parametrien konfigurointi** :



Tässä vaiheessa sinun on määritettävä joukko Elements:tä ennen asennuksen käynnistämistä koneellesi.



![0_05](assets/fr/05.webp)



**Näppäimistön asettelu** :



Napsauta **Näppäimistö** -vaihtoehtoa ja valitse sitten tietokoneellesi **sopiva asettelu**. Kun olet tehnyt valintasi, siirry seuraavaan vaiheeseen napsauttamalla **Päätetty**.



**Kohteen valinta** :



Valitse "Asennuskohde" -vaihtoehto valitaksesi levykkeen, jolle haluat asentaa Qubes OS:n. Oletusarvoisesti osiointi tapahtuu automaattisesti, jolloin voit poistaa kaikki tiedot levyltä ja asentaa järjestelmän sille. Voit kuitenkin valita vaihtoehdon **Räätälöity** tai **Edistynyt räätälöinti**, jos haluat tehdä mukautetun osioinnin. Napsauta sitten "Valmis". Järjestelmä pyytää sinua asettamaan **salasanan**, joka toimii tietoturva Layer:na tietojesi salaamiseksi. Muista valita monimutkainen ja ainutlaatuinen salasana.



![0_06](assets/fr/06.webp)



![0_07](assets/fr/07.webp)



**Valitse päivämäärän ja kellonajan muoto** :


Napsauta Aika ja päivämäärä -vaihtoehtoa ja valitse sitten maantieteellinen vyöhykkeesi. Voit myös valita haluamasi aikaformaatin: 24h tai 12h.



![0_08](assets/fr/08.webp)



**Käyttäjätilin luominen** :


Klikkaa **Luo käyttäjä** luodaksesi **ensimmäisen käyttäjätilisi**, jonka avulla voit kirjautua Qubes OS:ään.



![0_09](assets/fr/09.webp)



**Activate root account** :


Voit myös **aktivoida pääkäyttäjätilin** asettamalla erillisen salasanan ylläpidolle.



![0_10](assets/fr/10.webp)



Kun nämä asetukset on tehty, napsauta **Aloita asennus** käynnistääksesi prosessin.



![0_11](assets/fr/11.webp)



Odota, että **asennus päättyy**, ja napsauta sitten **käynnistä järjestelmä uudelleen** viimeistelläksesi asennuksen ja käynnistääksesi Qubes OS:n.



![0_12](assets/fr/12.webp)



**Lisäkokoonpano** :


Uudelleenkäynnistyksen jälkeen Qubes OS pyytää sinua viimeistelemään **default templates and qubes configuration**. Syötä levyn salausta varten määritetty salasana.



![0_13](assets/fr/13.webp)



Valitse seuraavaksi **TemplateVM**, jonka haluat asentaa. Yleisiä vaihtoehtoja ovat **Debian 12 Xfce**, **Fedora 41 Xfce** ja **Whonix 17**, joista jälkimmäistä suositellaan käyttötarkoituksiin, joissa vaaditaan **anonymiteettiä ja verkkoturvallisuutta**. Voit myös määritellä **default template**, joka toimii uusien **AppVM:ien** luomisen perustana.



![0_14](assets/fr/14.webp)



**Pääasetukset**-osiossa voit valita, luodaanko järjestelmän keskeiset qubit, kuten **sys-net**, **sys-firewall** ja **default DisposableVM**, automaattisesti. On suositeltavaa ottaa käyttöön vaihtoehto, jossa **sys-firewall ja sys-usb ovat kertakäyttöisiä**, jotta laitteen ja verkon altistumista voidaan rajoittaa, jos laite vaarantuu. Voit myös luoda oletusarvoisia **AppVM:iä**, kuten **personal**, **work**, **untrusted** ja **vault**, jotta voit järjestää toimintosi niiden luotettavuustasojen mukaan.



![0_15](assets/fr/15.webp)



Qubes OS:n avulla voit myös luoda USB-laitteille omistetun **quben** (sys-usb) ja konfiguroida **Whonix Gateway- ja Workstation-qubet**, jotta voit suojata viestinnän Tor-verkon kautta. Edistyneemmille käyttäjille voit luoda **LVM thin pool** -osion avulla **LVM thin pool**, jonka avulla voit hallita tehokkaasti levytilaa qubien välillä.



Kun kaikki nämä asetukset on määritetty, napsauta **Täydellinen** ja sitten **Kokoonpanon viimeistely**. Odota, että järjestelmä ottaa nämä asetukset käyttöön. Sinua pyydetään sitten **kirjautumaan käyttäjätilillesi**, ja Qubes OS -ympäristösi on käyttövalmis, turvallinen ja asianmukaisesti eristetty eri toimintojasi varten.



![0_17](assets/fr/17.webp)



Käyttöjärjestelmäsi on nyt asennettu ja käyttövalmis.



![0_18](assets/fr/18.webp)



## Luo qube järjestelmään



Qubea luotaessa prosessia hallitaan **Qube Manager**-työkalulla, joka on käytettävissä Käynnistä-valikosta. Napsauta työkaluikkunassa yksinkertaisesti **Create qube** -kuvaketta avataksesi uuden määritysikkunan. Kirjoita ensin qubelle nimi, kuten "perso-web" tai "work", jotta sen käyttötarkoitus voidaan tunnistaa.



Seuraavaksi valitset sen **Tyypin**, yleensä **AppVM** rutiinitehtäviä varten tai **DisposableVM** tilapäistä käyttöä varten. On tärkeää valita **Template**, johon qube perustuu, kuten "fedora-39" tai "debian-12", koska se tarjoaa käyttöjärjestelmän ja ohjelmistot. Määrität myös **NetVM**:n, joka on qube, joka vastaa Internet-yhteyksistä, oletuksena **sys-firewall**.



Kun olet tarvittaessa säätänyt tallennuskokoa ja RAM-muistia, luomisprosessi käynnistyy napsauttamalla **OK**. Kun prosessi on valmis, uusi qube näkyy luettelossa ja on valmis käytettäväksi.



Yhteenvetona voidaan todeta, että Qubes OS ei ole tavallinen käyttöjärjestelmä, vaan huippuluokan tietoturvaratkaisu, joka ajattelee uudelleen henkilökohtaisen tietokoneen arkkitehtuurin. Sen lähestymistapa, joka perustuu lokerointiin ja eristämiseen virtualisoinnin avulla, tarjoaa vertaansa vailla olevan suojan kaikkein kehittyneimpiä uhkia vastaan. Segmentoimalla työympäristön kutakin tehtävää varten erikoistuneisiin qubiin se varmistaa, että haittaohjelmat eivät voi levitä ja vaarantaa koko järjestelmää.



Qubes OS tarjoaa joustavan ja läpinäkyvän kehyksen riippumatta siitä, onko sinun tarpeen surffata verkossa turvallisesti, suojata arkaluonteisia tietoja tai työskennellä eri luottamustasoilla. Kun otat käyttöön hyvät käytännöt ja hyödynnät sen ominaisuuksia täysimääräisesti, sinulla on **digitaalinen linnoitus**, joka on mukautettu nykyaikaisiin uhkiin. Lue lisää tietojen ja yksityisyyden suojaamisesta.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1