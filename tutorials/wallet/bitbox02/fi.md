---
name: BitBox02

description: BitBox02:n asennus ja käyttö
---

![cover](assets/cover.webp)

BitBox02 (https://bitbox.swiss/) on sveitsiläinen fyysinen lompakko, joka on suunniteltu erityisesti Bitcoinien turvaamiseen. Sen keskeisiä ominaisuuksia ovat helppo varmuuskopiointi ja palautus microSD-kortin avulla, minimalistinen ja huomaamaton muotoilu sekä kattava tuki Bitcoinille.

![device](assets/1.webp)

Se tarjoaa huippuluokan turvallisuuden, jonka ovat suunnitelleet asiantuntijat, ja sisältää kaksipiirisen suunnittelun, johon kuuluu turvapiiri. Sen lähdekoodi on täysin auditoitu turvallisuustutkijoiden toimesta ja se on täysin avoimen lähdekoodin. BitBox02 toimitetaan yksinkertaisen, mutta tehokkaan BitBoxAppin kanssa, joka mahdollistaa turvallisen hallinnan Bitcoineillesi. Se tukee täyttä solmua Bitcoinille ja varmistaa päästä päähän salatun viestinnän sovelluksen ja laitteen välillä. Sveitsissä valmistettu BitBox02 on saanut positiivisen maineen käyttäjiensä keskuudessa.

![video](https://youtu.be/sB4b2PbYaj0)

> Tekniset tiedot
>
> - Liitettävyys: USB-C
> - Yhteensopivuus: Windows 7 ja uudemmat, macOS 10.13 ja uudemmat, Linux, Android
> - Syöttö: Kapasitiiviset kosketussensorit
> - Mikrokontrolleri: ATSAMD51J20A; 120 MHz 32-bittinen Cortex-M4F; Todellinen satunnaislukugeneraattori
> - Turvapiiri: ATECC608B; Todellinen satunnaislukugeneraattori (NIST SP 800-90A/B/C)
> - Näyttö: 128 x 64 px valkoinen OLED
> - Materiaali: Polykarbonaatti
> - Koko: 54.5 x 25.4 x 9.6 mm sisältäen USB-C pistokkeen
> - Paino: Laite 12g; pakkaus ja tarvikkeet 160g

Lataa tietolehtisiä heidän verkkosivuiltaan https://bitbox.swiss/bitbox02/

## BitBox02 Hardware Walletin käyttö

### BitBox02:n asennus

BitBox02:ssa on USB-C-liitäntä kiinnitettynä kuoreen. Jos tietokoneessasi on tavallinen USB-portti, sinun on käytettävä laitteen mukana tulevaa sovitinta.

Yhdistä se tietokoneeseesi ja laite käynnistyy (älä tee sitä vielä).

Siinä on sensoreita ylä- ja alapuolella, ja se kehottaa sinua koskettamaan ylä- tai alaosaa näytön suuntaamiseksi haluamallasi tavalla.

![image](assets/2.webp)

### Lataa BitBox02-sovellus

Vieraile osoitteessa https://shiftcrypto.ch/ ja klikkaa sivun yläosassa olevaa “App”-linkkiä päästäksesi lataussivulle:

![image](assets/3.webp)

Klikkaa sinistä Lataa-painiketta:

![image](assets/4.webp)

Latauksen vahvistamiseksi (se lisää monimutkaisuutta, mutta suositeltavaa, erityisesti jos säilytät paljon bitcoineja), katso Liite A.

Latauksen jälkeen voit purkaa tiedoston. Macilla, vain kaksoisklikkaa ladattua tiedostoa, ja BitBox-sovelluksen kuvake ilmestyy latauskansioosi. Voit vetää sen työpöydällesi (tai minne tahansa) helposti saataville.

Kaksoisklikkaa sovellusta suorittaaksesi sen (sitä ei "asenneta").

Macilla, tietokoneesi vahtikoira antaa sinulle varoituksen. Ohita se vain ja klikkaa “avaa”:

![image](assets/5.webp)

Sitten näet tämän:

![image](assets/6.webp)

Mene eteenpäin ja yhdistä laite tietokoneeseen.

Näyttöön tulee paritus koodi. Tarkista, että ne täsmäävät, ja kosketa sitten sensoria valitaksesi rastin. Sitten takaisin näytölle, jatka-painike tulee saataville.

![image](assets/7.webp)
Sitten sinulla on mahdollisuus luoda uusi siemen (seed) tai palauttaa siemen. Esittelen uuden siemenen luomisen (On tärkeää myös palauttaa luomasi siemen testataksesi varmuuskopiosi laatua, ennen kuin lataat mitään bitcoineja lompakkoon).
![image](assets/8.webp)

Laite toimitettiin mikroSD-kortin kanssa. Mene eteenpäin ja aseta se paikalleen, jos et ole vielä tehnyt niin.

![image](assets/9.webp)

Nimeä laitteesi ja klikkaa jatka, sitten vahvista laitteessa.

![image](assets/10.webp)

Sinua pyydetään sen jälkeen asettamaan salasana laitteelle. Tämä ei ole osa siementäsi. Se ei myöskään ole salasana-lause (se on osa siementäsi). Se on yksinkertaisesti salasana laitteen lukitsemiseksi. Kun käynnistät laitteen, sinua pyydetään syöttämään tämä salasana joka kerta. Sinulla on 10 peräkkäistä yritystä ennen kuin laite pyyhkii itsensä kaikista muisteista, joten ole varovainen. Näytöllä oleva animaatio opettaa sinulle, miten käyttää laitteen ohjaimia salasanan asettamiseen.

![image](assets/11.webp)

Lue seuraava näyttö ja merkitse jokainen ruutu, sitten jatka.

![image](assets/12.webp)
![image](assets/13.webp)
![image](assets/14.webp)

Ja tältä lompakko näyttää, kun se on valmis käyttöön.

![image](assets/15.webp)

### EI NIIN NOPEASTI!!

On melko outoa, mutta BitBox02 kertoo meille, että laite on valmis käyttöön, mutta se ei ole kehottanut meitä kirjoittamaan alas siemen sanoja! AINOA varmuuskopiomme on tiedosto, joka on tallennettu mikroSD-kortille. Tämä ei riitä. Nämä tallennuslaitteet eivät kestä ikuisesti (johtuen "bittirotasta"). Tarvitsemme paperivarmuuskopion, ja kopiot, jotka säilytetään turvallisesti (kuten yleisessä ohjeessa laitteistolompakoiden käyttöön on selitetty)

Saadaksesi siemenlauseesi ja kirjoittaaksesi sen ylös, mene vasemmalla olevaan "manage device" -välilehteen ja klikkaa sitten "show recover words".

![image](assets/16.webp)

Voit sen jälkeen mennä läpi vahvistuksen, ja laite esittelee sinulle sanat. Kirjoita ne siististi ylös, äläkä anna kenenkään nähdä sanoja.

![image](assets/17.webp)

Sen jälkeen voit klikata vasemmalla olevaa Bitcoin-välilehteä saadaksesi vastaanotto-osoitteesi.

![image](assets/18.webp)

Se näyttää yhden kerrallaan, mutta ainakin se antaa sinun valita, minkä osoitteen ensimmäisestä 20:stä käytät:

![image](assets/19.webp)

Sinistä nappia klikkaamalla näytetään koko osoite, ja sinua pyydetään tarkistamaan, että osoite vastaa näytön näyttämää. Tämä on hyvä käytäntö varmistaa, ettei mikään haittaohjelma tietokoneellasi huijaa sinua lähettämään bitcoineja hyökkääjän osoitteeseen.

![image](assets/20.webp)

Lähettääksesi bitcoineja tähän lompakkoon, voit kopioida osoitteen ja liittää sen vaihdon sivustolla olevaan nostosivuun, jossa kolikkosi ovat. Suosittelen, että lähetät ensin pienen testisumman, sitten harjoittelet sen käyttämistä joko takaisin vaihtoon tai toiseen osoitteeseen lompakossasi.

Suurempia summia varten suosittelen, että luot salasana-lauseen (katso alla). Alkuperäistä lompakkoa (ei salasana-lausetta) voidaan käyttää harhautuslompakkonasi (siinä on oltava kohtuullinen summa, jotta se olisi uskottava harhautus).

### Yhdistä solmuun

BitBox02 yhdistää automaattisesti solmuun. Katsotaan, mihin se on yhdistämässä. Klikkaa vasemmalla olevaa asetukset-välilehteä ja sitten "connect your own full node".

![image](assets/21.webp)
Ja tässä näemme sen yhdistävän shiftcrypto:n solmuun. Ei hyvä. Olemme paljastaneet kaikki bitcoin-osoitteemme heille, sekä IP-osoitteemme (ei tietenkään siementä; he voivat nähdä osoitteemme/saldomme, mutta eivät voi käyttää niitä). Voimme syöttää omat solmutietomme tälle sivulle (tämän oppaan ulkopuolella), tai voimme käyttää parempaa ohjelmistoa kuten Sparrow Bitcoin Wallet, Electrum Desktop Wallet tai Specter Desktop. Esittelen Sparrow Bitcoin Walletin myöhemmin oppaassa.
![kuva](assets/22.webp)

Lisää salasana

Nyt kun olemme asettaneet laitteen BitBox02-sovelluksen avulla (ja paljastaneet osoitteemme, välttämätöntä tällä erityisellä laitteistolompakolla), voimme lisätä salasanan siemenlauseeseemme. Tämä mahdollistaa uuden lompakon luomisen samalla siemenellä, ja ShiftCrypto ei koskaan näe uusia osoitteitamme. Yhdistämme tämän lompakon vain omaan ohjelmistoohimme.

### Ota Salasana Käyttöön

Mene nyt eteenpäin ja "ota käyttöön" salasanaominaisuus (mutta emme aseta salasanaa vielä). Mene "hallitse laitetta" -välilehteen ja klikkaa "ota salasana käyttöön" (alla punainen ympyrä).

![kuva](assets/23.webp)

Lue läpi vaiheet...

![kuva](assets/24.webp)
![kuva](assets/25.webp)
![kuva](assets/26.webp)

Nyt irrota laite ja sulje BitBox02-sovellus

Bitbox02-osion loppu Parman toimesta.

Laitteesi on nyt täysin valmis käytettäväksi minkä tahansa desktop-ratkaisun kanssa, kuten specter, sparrow ja käyttäen bitbox-käyttöliittymää.