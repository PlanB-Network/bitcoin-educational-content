---
name: Linux Mint

description: Valmistele tietokone bitcoin-siirtoja varten
---

![kuva](assets/cover.webp)

## Mikä on vialla, jos käytät tavallista tietokonetta?

Bitcoin-siirtojen tekeminen on ihanteellista, jos tietokoneellasi ei ole haittaohjelmia. Ilmiselvästi.

Jos säilytät Bitcoin-siemenfraasiasi (yleensä 12 tai 24 sanaa) tietokoneen ulkopuolella allekirjoituslaitteessa (esim. laitteistokukkaro – sen pääasiallinen tarkoitus), saatat ajatella, että "puhtaan" tietokoneen omistaminen ei ole niin tärkeää – tämä ei pidä paikkaansa.

Haittaohjelmien saastuttama tietokone saattaa lukea Bitcoin-osoitteesi, paljastaen saldosi hyökkääjälle – he eivät voi ottaa bitcoineja pelkästään osoitteen tietämällä, mutta he voivat nähdä, kuinka paljon sinulla on, ja laskea siitä, oletko arvokas kohde. He saattavat myös jotenkin selvittää, missä asut, esimerkiksi, ja vaatia sinulta lunnaita uhkaamalla ottaa kynnet tai lapset.

## Mikä on ratkaisu?

Kannustan useimpia Bitcoin-käyttäjiä käyttämään omistettua, haittaohjelmista vapaata tietokonetta (internet-yhteydellä) Bitcoin-siirtojen tekemiseen. Ehdotan, että ihmiset käyttävät avoimen lähdekoodin käyttöjärjestelmää, kuten Linux Mint, mutta voit käyttää Windowsia tai Macia, jos on pakko – se on parempi kuin tavallisen, paljon käytetyn tietokoneen käyttö, jossa väistämättä on piilotettuja haittaohjelmia.

Yksi este, jonka ihmiset kohtaavat, on uuden käyttöjärjestelmän asentaminen tällaisiin tietokoneisiin. Tämä opas auttaa siinä.

Linuxin eri versioita on monia, ja olen kokeillut useita. Suositukseni Bitcoin-käyttäjille on Linux Mint, koska se on helppo asentaa, erittäin nopea (erityisesti käynnistyksessä ja sammutuksessa), ei turvonnut (jokainen ylimääräinen ohjelmisto on riski), ja on harvoin kaatunut minulle tai käyttäytynyt oudosti (verrattuna muihin versioihin, kuten Ubuntuun ja Debianiin).

Jotkut saattavat olla hyvin vastahakoisia uuden käyttöjärjestelmän suhteen, pitäen enemmän Windowsista tai Mac OS:sta. Ymmärrän, mutta Windowsin ja Applen käyttöjärjestelmät ovat suljettua lähdekoodia, joten meidän on luotettava siihen, mitä ne tekevät; en usko, että se on hyvä politiikka, mutta se ei ole kaikki tai ei mitään. Suosisin paljon mieluummin, että ihmiset käyttäisivät omistettua, vasta asennettua Windows- tai Mac OS -tietokonetta kuin paljon käytettyä tietokonetta (jossa kuka tietää, mitä haittaohjelmia on kertynyt). Yksi askel parempi on käyttää vasta asennettua Linux-tietokonetta, jota tulen esittelemään.

Jos olet hermostunut Linuxin käyttämisestä tuntemattoman vuoksi, se on luonnollista, mutta niin on myös ajan käyttäminen oppimiseen. Verkossa on saatavilla paljon tietoa. Tässä on erinomainen lyhyt video, joka esittelee komentorivin perusteet ja jonka suosittelen lämpimästi.
Valitse tietokone

Aloitan, mitä pidän parhaana vaihtoehtona. Sitten annan mielipiteeni vaihtoehdoista.

Ihanteellinen vaihtoehto:

Suositukseni, jos sinulla on varaa siihen, ja jos bitcoin-pinon koko sen oikeuttaa, on hankkia aivan uusi perustason kannettava tietokone. Nykyään valmistettu perusmalli on riittävän hyvä käyttötarkoitukseen. Prosessorin ja RAM-muistin tekniset tiedot eivät ole merkityksellisiä, koska ne kaikki ovat riittävän hyviä.

Vältä:

- Kaikki tabletti-yhdistelmät, mukaan lukien Surface Pro
- Chromebookit – usein tallennuskapasiteetti on liian pieni
- Kaikki tietokoneet, joissa on eMMC-asema; Jos siinä on SSD-asema, se on täydellinen
- Macit – ne ovat kalliita, ja laitteisto ei sovi hyvin yhteen Linux-käyttöjärjestelmien kanssa kokemukseni mukaan
- Kaikki kunnostetut tai käytetyt (ei kuitenkaan ehdoton este)

Sen sijaan, etsi Windows 11 -kannettavaa tietokonetta (Tällä hetkellä Windows 11 on viimeisin julkaisu. Älä huoli, hankkiudumme eroon tuosta ohjelmistosta.). Etsin amazon.com-sivustolta "Windows 11 Laptop" ja löysin tämän hyvän esimerkin:
![kuva](assets/1.webp)
Tämän yllä olevan hinta on hyvä. Tekniset tiedot ovat riittävän hyvät. Siinä on sisäänrakennettu kamera, jota voimme käyttää QR-koodi PSBT -transaktioihin (muuten joutuisit ostamaan USB-kameran sitä varten). Älä huolehdi siitä, että se ei ole tunnettu merkki (se on halpa). Jos haluat paremman merkin, se maksaa sinulle, esim:

![kuva](assets/2.webp)

Jotkut halvemmista malleista tarjoavat vain 64 Gt:n aseman tilan; en ole testannut kannettavia, joissa on näin pieni asema – se saattaa olla OK, jos tilaa on 64 Gt, mutta se saattaa olla tiukkaa.

## Muut vaihtoehdot – Tails

Tails on käyttöjärjestelmä, joka käynnistyy USB-muistitikulta ja ottaa väliaikaisesti haltuunsa minkä tahansa tietokoneen laitteiston. Se käyttää vain Tor-yhteyksiä, joten sinun on oltava mukava käyttämään Toria. Mitään istuntosi aikana muistiin kirjoittamaasi tietoa ei tallenneta asemaan (se alkaa puhtaalta pöydältä joka kerta), ellet muokkaa asetuksia ja luo pysyvää tallennusvaihtoehtoa (USB-muistitikulle) – jonka lukitset salasanalla.

Se ei ole huono vaihtoehto ja se on ilmainen, mutta se on hieman kömpelö tarkoitukseemme. Uuden ohjelmiston asentaminen siihen ei ole helppoa. Yksi hyvä ominaisuus on, että siinä tulee mukana Electrum, mutta tämän haittapuolena on, että et asentanut sitä itse. Varmista, että käyttämäsi USB-asema on vähintään 8 Gt.

Joustavuutesi vähenee, jos käytät Tailsia. Et ehkä pysty seuraamaan erilaisia oppaita tarvitsemasi asettamiseksi ja saamaan sitä toimimaan kunnolla. Esimerkiksi, jos seuraat opastani Bitcoin Coren asentamiseen, tarvitaan muutoksia sen toimimiseksi. En usko tekeväni Tails-spesifistä opasta, joten sinun on kehitettävä taitojasi ja tehtävä se yksin.

En myöskään ole varma, miten hyvin laitteistolompakot toimivat tämän käyttöjärjestelmän kanssa.

Kaiken tämän sanottuani, Tails-tietokone Bitcoin-transaktioihin on mukava lisävaihtoehto, ja se varmasti auttaa parantamaan yleisiä yksityisyystaitojasi Tailsin käytön oppimisella.

## Muut vaihtoehdot – Live OS Boot

Tämä on hyvin samankaltainen kuin Tails, paitsi että käyttöjärjestelmä ei ole yksityisyyteen keskittynyt. Tämän perusidea on väläyttää USB-asema valitsemallasi Linux-käyttöjärjestelmällä ja saada tietokone käynnistymään siitä sisäisen aseman sijaan. Miten tämä tehdään, selitetään myöhemmin.

Etuna on, että olet vähemmän rajoittunut ja asiat toimivat ilman edistyneitä säätöjä.

En ole varma, miten hyvin tällainen järjestelmä eristää olemassa olevan tietokoneen haittaohjelmat käyttämästäsi USB-käynnistysasemasta, joka sisältää uuden käyttöjärjestelmän. Se todennäköisesti tekee hyvää työtä ja ei todennäköisesti ole yhtä hyvä kuin Tails. Koska en tiedä, mieluummin suosin omistettua kannettavaa tietokonetta.
Muut vaihtoehdot – Oma käytetty kannettava tai pöytätietokone

Käytetyn tietokoneen käyttö ei ole ihanteellista, pääasiassa siksi, että en tunne monimutkaisten haittaohjelmien sisäistä toimintaa, enkä tiedä, riittääkö aseman pyyhkiminen niistä eroon pääsemiseksi. Se todennäköisesti riittää, mutta en halua aliarvioida pahantahtoisten hakkerien kekseliäisyyttä. Voit päättää, en halua sitoutua.

Jos päätät käyttää vanhaa pöytäkonetta vanhan kannettavan sijaan, se on hienoa, paitsi että se vie pysyvästi tilaa todennäköisesti harvinaisille bitcoin-transaktioillesi; sinun ei pitäisi käyttää sitä mihinkään muuhun. Kannettavan tietokoneen kanssa voit sen sijaan vain laittaa sen pois ja jopa piilottaa sen lisäturvallisuuden vuoksi.

## Linux Mintin asentaminen mihin tahansa tietokoneeseen
Nämä ovat ohjeita poistaa mikä tahansa käyttöjärjestelmä uudesta kannettavasta tietokoneestasi ja asentaa Linux Mint, mutta voit mukauttaa näitä ohjeita asentaaksesi melkein minkä tahansa Linux-version melkein mihin tahansa tietokoneeseen.
Aiomme käyttää mitä tahansa tietokonetta väläyttämään käyttöjärjestelmän jonkinlaiseen muistitikkuun. Ei ole väliä minkä muistitikun valitset, kunhan se on yhteensopiva USB-portin kanssa, ja suosittelen vähintään 16 Gt:n kokoa.

Hanki jokin näistä:

![kuva](assets/3.webp)

Tai voit käyttää jotakin tällaista:

![kuva](assets/4.webp)

Seuraavaksi, siirry osoitteeseen linuxmint.com

![kuva](assets/5.webp)

Vie hiiri Lataa-valikon päälle sivun yläreunassa ja sitten klikkaa linkkiä, “Linux Mint 20.3” tai mikä tahansa on viimeisin suositeltu versio sinun tehdessäsi tämän.

![kuva](assets/6.webp)

Tarjolla on muutama eri “maku”. Valitse “Cinnamon” seurataksesi tätä opasta. Klikkaa Lataa-painiketta.

![kuva](assets/7.webp)

Seuraavalla sivulla voit vierittää alas nähdäksesi peilit (Peilit ovat eri palvelimia, jotka sisältävät haluamamme tiedoston kopion). Voit varmistaa latauksen käyttäen SHA256:ta ja gpg:tä (suositeltavaa), mutta jätän sen selittämisen tässä väliin, koska olen jo kirjoittanut oppaita tästä.

![kuva](assets/8.webp)

Valitse sinua lähinnä oleva peili ja klikkaa sen linkkiä (vihreä teksti peilisarakkeessa). Tiedosto alkaa latautua – lataamani version koko on 2,1 gigatavua.

Kun se on ladattu, voit väläyttää tiedoston kannettavaan muistilaitteeseen ja tehdä siitä käynnistettävän. Helpoin tapa tehdä tämä on käyttää Balena Etcheria. Lataa ja asenna se, jos sinulla ei sitä vielä ole.

Sitten suorita se:

![kuva](assets/9.webp)

Klikkaa väläytä tiedostosta, ja valitse ladattu LinuxMint-tiedosto.

Sen jälkeen klikkaa Valitse kohde. Varmista, että muistilaite on kytketty ja että valitset oikean aseman, muuten saatat tuhota väärän aseman sisällön!

Tämän jälkeen valitse Väläytä! Saatat joutua syöttämään salasanasi. Kun se on valmis, asema ei todennäköisesti ole luettavissa Windows- tai Mac-tietokoneellasi, koska se on muunnettu Linux-laitteeksi. Vedä se vain ulos.
Valmistele kohdetietokone

Käynnistä uusi kannettava tietokone, ja kun se on käynnistymässä, pidä BIOS-näppäintä alhaalla. Tämä on tyypillisesti F2, mutta se voi olla myös F1, F8, F10, F11, F12 tai Delete. Kokeile jokaista, kunnes löydät oikean, tai etsi internetistä tietokoneesi mallia ja kysy oikea kysymys.

Esimerkiksi “BIOS-näppäin Dell kannettavat”.

Jokaisella tietokoneella on erilainen BIOS-valikko. Tutki ja löydä, mikä valikko antaa sinun konfiguroida käynnistysjärjestyksen. Tarkoituksemme mukaan haluamme tietokoneen yrittävän käynnistyä USB-liitetystä laitteesta (jos sellainen on liitetty), ennen kuin yrittää käynnistyä sisäiseltä kiintolevyltä (muuten Windows latautuu). Kun olet asettanut tämän, saatat joutua tallentamaan ennen poistumista tai se saattaa tallentua automaattisesti.

Käynnistä tietokone uudelleen ja sen pitäisi ladata USB-muistilaitteelta. Voimme nyt asentaa Linuxin sisäiselle asemalle ja Windows poistetaan lopullisesti.

Kun pääset seuraavaan näyttöön, valitse “OEM-asennus (valmistajille)”. Jos sen sijaan valitset “Käynnistä Linux Mint”, saat Linux Mint -istunnon ladattua muistilaitteelta, mutta kun sammutat tietokoneen, mikään tietosi ei tallennu – se on käytännössä väliaikainen istunto, jotta voit kokeilla sitä.
Sinut johdatetaan graafisen asennusohjelman läpi, joka esittää sinulle joukon kysymyksiä, jotka pitäisi olla suoraviivaisia. Yksi kysymys koskee kieliasetuksia, toinen koti-internetverkon yhteyttä ja salasanaa. Jos sinua pyydetään asentamaan lisäohjelmistoja, hylkää pyyntö. Kun saavut asennustyypin valintaan, jotkut saattavat epäröidä – sinun tulee valita "Tyhjennä levy ja asenna Linux Mint". Älä myöskään salaa asemaa äläkä valitse LVM:ää.

Lopulta päädyt työpöydälle. Tässä vaiheessa et ole vielä valmis. Toimit itse asiassa valmistajan tavoin (eli henkilönä, joka rakentaa tietokoneen ja asentaa Linuxin asiakkaalle). Sinun on kaksoisnapsautettava työpöydän kuvaketta, "Asenna Linux Mint", viimeistelläksesi asennuksen.

Muista poistaa muistitikku ja sitten käynnistä tietokone uudelleen. Uudelleenkäynnistyksen jälkeen käytät käyttöjärjestelmää ensimmäistä kertaa uutena käyttäjänä. Onnittelut.

Yksi ensimmäisistä asioista, jotka sinun tulisi tehdä (ja tehdä säännöllisesti), on pitää järjestelmä ajan tasalla.

Avaa Terminaali-sovellus ja kirjoita seuraava:

```bash
sudo apt-get update
```

painamalla <enter>, vahvista valintasi, ja sitten tämä komento:

```bash
sudo apt-get upgrade
```

painamalla <enter> ja vahvista valintasi.

Anna sen tehdä tehtävänsä, se saattaa kestää useita minuutteja.

Seuraavaksi pidän Torin (kirjainkoko on merkityksellinen) asentamisesta:

```bash
sudo apt-get install tor
```

> _LISÄYS: Voit myös käynnistää Linux Mintin "OEM-asennuksesta" (Varmista, että olet yhteydessä internetiin, muuten saatat saada virheitä). Jos teet näin, sinun tulee myöhemmin napsauttaa työpöydällä olevaa "toimita loppukäyttäjälle" -kuvaketta. Sen jälkeen käynnistät käyttöjärjestelmän uudelleen ikään kuin avaisit tietokoneen ensimmäistä kertaa._

Tämä opas selitti, miksi saatat tarvita erillisen tietokoneen Bitcoin-siirtoihin, ja miten asentaa tuore Linux Mint -käyttöjärjestelmä sille.