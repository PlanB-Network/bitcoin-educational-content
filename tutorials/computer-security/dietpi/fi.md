---
name: DietPi
description: Kevyt käyttöjärjestelmä, joka on optimoitu suorituskyvyltään heikommille koneille. Suositaan itse isännöintiä
---

![cover](assets/cover.webp)



Ei-teknisissä piireissä tuotemerkit, kuten `Odroid`, `Raspberry Pi`, `Orange Pi` tai `Radxa`, ovat vähän tunnettuja. Mutta tarvitsee vain katsoa tekniikkapiireihin, niin huomaa, että **SBC**-tietokoneista - jotka on rakennettu yhdelle emolevylle ja jotka ovat usein mikroskooppisen pieniä verrattuna yleisesti käytettyihin tietokoneisiin - on tullut välttämättömiä minkä tahansa henkilökohtaisen projektin tukena.



Näitä tietokoneita valmistetaan monenlaisia malleja. Niissä käytetään mieluiten Linux-jakeluja, jotka on usein mukautettu toimimaan sujuvasti näissä heikkotehoisissa koneissa.



**DietPi ei ole poikkeus**: se on Debian-pohjainen käyttöjärjestelmä, joka on optimoitu olemaan mahdollisimman kevyt ja tekemään suorituskyvyltään heikoimmastakin `SBC`:stä erittäin nopea. Vaihdettu Debian12 Bookwormista Debian13 Trixieen juuri kun tätä ohjetta kirjoitettiin, se tukee nyt myös avoimen lähdekoodin `RISC-V`-prosessoripohjaisia SBC:tä. DietPi on miellyttävä löytö, joka ansaitsee lisätutkimusta.



## Vahvuudet



Tämä ei ole Debianin "tavallinen kopio" pienille Raspberry-tyyppisille piirilevyille. DietPi on:




- Optimoitu nopeuteen ja keveyteen**: [vertailu muihin Debian-jakeluihin SBC:tä varten](https://dietpi.com/blog/?p=888), DietPi on kevyempi kaikessa. DietPi-ISO-kuva painaa alle 1 Gt, mikä on ylivoimaisesti pienin vanhemmille Raspberry- tai Orange PI -malleille (esimerkiksi) omistetuista. RAM- ja CPU-resurssien kysyntä on hyvin vähäistä, joten se saa aina parhaan mahdollisen hyödyn irti myös vanhemmista piirilevyistä.
- Sisäänrakennetut automaatiot ja asentajat**: Erilliset komennot auttavat käyttäjiä valvomaan järjestelmän resursseja sekä automatisoimaan tehtäviä ohjelmien asentamiseksi ja käynnistämiseksi, versioiden päivittämiseksi, varmuuskopioiden tekemiseksi ja kaikkien lokien tarkistamiseksi.
- Vahva, kokeilunhaluinen yhteisö**: [tutorials](https://dietpi.com/forum/c/community-tutorials/8) ja DietPi-yhteisön projektit ovat ihanteellisia, kun haluat inspiroitua ohjelmistoista, jotka voit asentaa yhdellä klikkauksella DietPin ansiosta.



**Ei ole koskaan ollut helpompaa puristaa kaikkea irti SBC:stäsi**.



## Automatisoinnit itse isännöintiä varten


Haluatko kokeilla omalla palvelimellasi kehittyneitä verkkoratkaisuja tai työkaluja Bitcoin-osaamisesi kehittämiseksi? DietPi voi olla etsimäsi ratkaisu. Vaikka monet osaavat hallita omaa infrastruktuuriaan ja käyttää täydellisesti konfiguroituja ja suojattuja palvelimia, DietPi on sopiva askel niille, jotka haluavat aloittaa tyhjästä.



Sen sijaan, että suorittaisit manuaalisesti kaikki monimutkaiset tehtävät, joita tällainen tehtävä vaatii, DietPi antaa sinulle mahdollisuuden rakentaa ne ohjatulla ohjelmalla ja omalla komentorivillään. Täällä voit kokeilla omaa henkilökohtaista pilveä, _älykkään kodin_ laitehallintaa, automaattisia varmuuskopioita ja crontabia sekä edistyneempiä ratkaisuja.



![img](assets/en/01.webp)



## Asennus



### Lataa



DietPi tarjoaa lukemattoman määrän ISO-kuvia, joiden avulla voit polttaa käyttöjärjestelmän monille eri laitteille. Osa on vain tuettuja: esimerkiksi Raspberry PI5:lle tarkoitettu ISO-levy on vielä testauksessa, mutta löydät varmasti omalle levyllesi sopivan.



Tässä oppaassa päätin asentaa sen ohuelle asiakkaalle, joten valinta meni kohtaan _PC/VM_ ja sitten kohtaan _Native PC_. Näille laitteille on kaksi ISO-kuvaa, jotka eroavat toisistaan käynnistyslataimen sukupolven suhteen. Oppaassa käytetty kone on melko vanha, joten valinta osui _BIOS/CSM_-versioon. Jos sinulla on uudempi kone, oikea versio saattaa olla `UEFI`.



![img](assets/en/02.webp)



Päädyt sivulle, joka sisältää `asennusohjelman kuvan`, `sha256` ja `Allekirjoitukset`.



![img](assets/en/03.webp)



Valmistele hakemisto `home`-kotitietokoneellesi, jotta voit ladata tarvittavat tiedostot `wget`-ohjelmalla.



![img](assets/en/04.webp)



Kehittäjän julkinen avain vaati hieman tutkimustyötä, mutta löydät sen tästä linkistä: https://github.com/MichaIng.gpg.



![img](assets/en/05.webp)



Tarkista hakemiston sisältö komennolla `ls -la` ja tuo MichaIng-avain avainkokoelmaasi komennolla `gpg --import`.



### Tarkastus ja salama



Lopuksi se osa, jota suosittelen eniten: varmista ladatun ja SBC:hen asennettavan käyttöjärjestelmän aitous.



![img](assets/en/06.webp)



Jos sait myös tuloksen `Hyvä allekirjoitus` ja saman Hash-ohjauksen sha256sum-komennolla, voit jatkaa ISO-tiedoston flashaamista USB-tikulle. Käytä tähän sovelluksia kuten Whale Etcher.



![img](assets/en/07.webp)



## DietPi asennus



![img](assets/en/09.webp)



Siirrä muistitikku laitteeseen, jossa DietPi sijaitsee, ja aloita lime Green -käyttöjärjestelmän asennus. Tässä harjoituksessa käytämme ohutta asiakasta, jossa on 16 Gt RAM-muistia, 128 Gt SSD-levy käyttöjärjestelmää varten ja toinen 1 TB:n datalevy. Asennus kesti alle 30 minuuttia, mutta jos käytät esimerkiksi Raspberryä, resurssit voivat olla pienemmät ja kestää kauemmin. Sinulle näytetään asennuksen eteneminen asennuksen aikana.



![img](assets/en/08.webp)



Koska DietPi on suunniteltu Raspberryjä ja vastaavia varten, sen todellinen luonne on niin sanottu `headless`-asennus, ilman graafista ympäristöä ja natiivilla `shsh'-yhteydellä. Oppaassa sen sijaan näet graafisen ympäristön, tarkemmin sanottuna LXDE:n.



Tässä vaiheessa sinua pyydetään myös päättämään, mitä verkkoselainta haluat käyttää oletusarvoisesti, joko Chromiumia tai Firefoxia. Molemmat toimivat hyvin; kummallekaan ei ole erityisiä vasta-aiheita, paitsi henkilökohtainen mieltymyksesi.



Loppua kohti asennusohjelma saattaa kysyä, haluatko asentaa jo valmiiksi ohjelmia, mutta tässä vaiheessa **neuvon sinua olemaan lataamatta mitään valmiiksi**. Sinun on hyvä tietää, että tämän vaiheen jälkeen sinua pyydetään muuttamaan kahden käyttäjän oletussalasanat turvallisuussyistä. Tärkeintä on, että sinun on **asennettava `Global Software Password (GSP)`**, jolla varmistetaan pääsy eri ohjelmistoihin valvotusti. **Jos lataat ohjelmia käyttöjärjestelmän asennuksen aikana ilman asetettua GSP-salasanaa, niihin ei pääse käsiksi käytännössä ollenkaan**. Sinun on poistettava ja asennettava ne uudelleen sen jälkeen, kun olet asettanut `Global Software Password` -salasanan: siksi **en laita mitään, jotta vältät kaksinkertaisen työn**. (Epämukavuus on todennäköistä, ei 100 % varmaa).



Asennus päättyy pyyntöön aktivoida DietPi-Survey, automaattinen tiedonkeruupalvelu, jota käytetään tukemaan käyttöjärjestelmän kehittämistä. Verkkosivuston mukaan tiedonkeruu aktivoituu, kun lataat minkä tahansa ohjelmiston DietPin tarjoamasta automaatiosta tai kun päivität seuraavaan versioon. Jokaisella on mahdollisuus osallistua (_Opt IN_) tai kieltäytyä (_Opt OUT_).



![img](assets/en/23.webp)



Asennuksen päätyttyä ja sen jälkeen tapahtuneen uudelleenkäynnistyksen jälkeen DietPi näkyy näytöllä, kuten olet sen asettanut. Kuten mainittiin, valitsin opetusohjelmaan `LXDE`-grafiikkaympäristön. Työpöydältä löysin pikakuvakkeen `htop` käynnistämiseen ja terminaalin avaamiseen.



![img](assets/en/10.webp)



### "Työkalut" käyttöjärjestelmästä



Unohda useimmat Linux-jakelussasi käyttämäsi ohjelmat - DietPi on niin optimoitu, että olet jättänyt monet niistä pois. Sinun pitäisi periaatteessa asentaa monet komennot manuaalisesti, mutta jos olet vasta kokeilemassa, vastusta kiusausta ja kokeile DietPin automaatioiden testaamista.



Se on ehdottomasti pääteasema, joka on ensimmäinen hyödyllinen työkalu uuden käyttöjärjestelmän käyttöönotossa, ja se avautuu automaattisesti aina, kun käynnistät sen.



![img](assets/en/11.webp)



Terminaalin näytöllä on lueteltu joukko komentoja, joiden edessä on `dietpi-` ja jotka edustavat tämän käyttöjärjestelmän [työkaluja](https://dietpi.com/docs/dietpi_tools/):




- `dietpi-launcher`: käyttöjärjestelmän, tiedostojenhallinnan jne. käyttäminen
- `dietpi-Software`: tämä on työkalu, jonka avulla voit asentaa kaikki paketissa jo olevat ohjelmistot
- `dietpi-config`: päästä käsiksi järjestelmän asetuksiin, jopa kaikkein edistyneimpiin.



![img](assets/en/14.webp)



### Varmuuskopiointi



Palvelimen varmuuskopiointi on rutiini, joka järjestelmänvalvojan olisi ennakoitava heti ensimmäisestä käynnistyksestä lähtien.



DietPi:ssä on komento `dietpi-Backup`, jota suosittelen tutkimaan ihanteellisen ratkaisun löytämiseksi: sen avulla voit määrittää säännöllisen varmuuskopioinnin, inkrementaalisen tai ei-inkrementaalisen riippuen käytetyistä sovelluksista, ja kaikki vaihtoehdot rutiinin mukauttamiseksi.



![img](assets/en/22.webp)



Valitse varmuuskopion määränpää, esimerkiksi toinen levy, käynnistämällä `dietpi-Drive_Manager`, jotta voit liittää määränpääaseman ja käyttää sitä tässä toiminnossa.



## Konfigurointi



Itse isännöinti on suositeltavaa kaikille, olivatpa he sitten uteliaita tai vain innostuneita. Palvelimen pystyttämiseen ja konfigurointiin liittyy kuitenkin joitakin huomattavia teknisiä haasteita. Tässä kohtaa ** DietPi**:n yksinkertaisuus tulee kuvaan, sillä sen avulla voit konfiguroida tarpeisiisi räätälöidyn järjestelmän muutamalla yksinkertaisella askeleella.



![img](assets/en/24.webp)



Perus- ja lisäasetukset, kaikki käytettävissäsi yhdellä Interface:lla, joka on käytettävissä komennon kanssa:



```dietpi-config


sudo dietpi-config


```

Che cosa si può fare ora? Automatizzare i processi da avviare all'accensione del server, configurare il `Locale` e tutte le impostazioni correlate alla Time Zone, impostare le schede di rete, le password e le periferiche audio/video, ad esempio.

## I Pacchetti Software

Tra le caratteristiche di semplicità di DietPi, vi è anche la dettagliata pagina dei Software che - oltre all'elenco delle applicazioni - mostra i primi passi da compiere per installarli e interagire con loro. Prendiamo ad esempio il caso di **Docker**:

![img](assets/en/15.webp)

Cliccando sulla sua "icona" compare in alto una finestra, dove è possibile cliccare i link che portano a una spiegazione di massima. La finestra mostra dove si trovano i file più importanti, come accedere all'interfaccia web e tanti altri suggerimenti per un'installazione fluida.

![img](assets/en/16.webp)

Le applicazioni che prevedono l'interazione dell'utente hanno un'interfaccia web pensata per questo scopo, accessibile all'indirizzo IP che va sempre sotto la sintassi `indirizzo-IP-localhost:porta`. Anche l'URL dell'interfaccia web la trovi se hai cliccato _View_.

Tutti [i software disponibili con DietPi](https://dietpi.com/dietpi-software.html), si installano da terminale, digitando:

```


sudo dietpi-ohjelmisto


```