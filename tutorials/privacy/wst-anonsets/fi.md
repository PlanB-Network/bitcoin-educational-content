---
name: Whirlpool Stats Tools - Anonsets
description: Ymmärrä anonsetin käsite ja kuinka laskea se WST:n avulla
---
![cover](assets/cover.webp)

***VAROITUS:** Samourai Walletin perustajien pidätyksen ja heidän palvelimiensa takavarikoinnin jälkeen 24. huhtikuuta, Whirlpool Stats Tool ei ole enää ladattavissa, koska se oli isännöity Samourain Gitlabissa. Vaikka olisit aiemmin ladannut tämän työkalun paikallisesti koneellesi, tai se oli asennettu RoninDojo-noodiisi, WST ei toimi tällä hetkellä. Se nojasi OXT.me:n tarjoamiin tietoihin toimiakseen, ja tämä sivusto ei ole enää saavutettavissa. Tällä hetkellä WST ei ole erityisen hyödyllinen, koska Whirlpool-protokolla on passiivinen. On kuitenkin mahdollista, että nämä ohjelmistot saatetaan palauttaa käyttöön tulevina viikkoina. Lisäksi tämän artikkelin teoreettinen osa pysyy relevanttina ymmärtääksemme yleisesti coinjoinien periaatteita ja tavoitteita (ei vain Whirlpool), sekä Whirlpool-mallin tehokkuuden ymmärtämiseksi. Voit myös oppia, kuinka määrittää coinjoin-syklien tarjoama yksityisyys.*

_Seuraamme tarkasti tämän tapauksen kehitystä sekä siihen liittyvien työkalujen kehitystä. Voit olla varma, että päivitämme tämän oppaan, kun uutta tietoa tulee saataville._

_Tämä opas on tarkoitettu vain koulutus- ja tiedotustarkoituksiin. Emme tue tai kannusta näiden työkalujen käyttöä rikollisiin tarkoituksiin. Jokaisen käyttäjän on noudatettava oman lainkäyttöalueensa lakeja._

---

*"Katkaise linkki, jonka kolikkosi jättävät jälkeensä"*

Tässä oppaassa tutkimme anonsettien käsitettä, indikaattoreita, jotka mahdollistavat coinjoin-prosessin laadun arvioinnin Whirlpoolissa. Käymme läpi näiden indikaattoreiden laskentamenetelmän ja tulkinnan. Teoreettisen osan jälkeen siirrymme käytäntöön oppimalla laskemaan tietyn siirron anonsetit Python-työkalulla *Whirlpool Stats Tools* (WST).

## Mikä on coinjoin Bitcoinissa?
**Coinjoin on tekniikka, joka katkaisee bitcoinien jäljitettävyyden lohkoketjussa**. Se perustuu yhteistyöhön perustuvaan siirtoon, jolla on samanniminen erityinen rakenne: coinjoin-siirto.

Coinjoin-siirrot parantavat Bitcoin-käyttäjien yksityisyyttä vaikeuttamalla ketjuanalyysiä ulkopuolisille tarkkailijoille. Niiden rakenne mahdollistaa useiden eri käyttäjien kolikoiden yhdistämisen yhteen siirtoon, mikä hämärtää jälkiä ja tekee vaikeaksi määrittää syötteiden ja tulosteiden välisiä linkkejä.

Coinjoinin periaate perustuu yhteistyöhön: useat käyttäjät, jotka haluavat sekoittaa bitcoinejaan, tallettavat identtisiä määriä saman siirron syötteiksi. Nämä määrät jaetaan sitten vastaavan arvon tulosteina. Siirron lopussa on mahdotonta yhdistää tiettyä tulostetta tiettyyn käyttäjään. Syötteiden ja tulosteiden välillä ei ole suoraa linkkiä, mikä katkaisee yhteyden käyttäjien ja heidän UTXO:nsa välillä sekä kunkin kolikon historian.

![coinjoin](assets/notext/1.webp)

Esimerkki coinjoin-siirrosta:
[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)
Coinjoinin suorittaminen siten, että jokainen käyttäjä säilyttää hallinnan varoistaan koko ajan, alkaa transaktion rakentamisella koordinaattorin toimesta, joka sitten lähettää sen jokaiselle osallistujalle. Kukin käyttäjä allekirjoittaa transaktion sen jälkeen, kun on varmistanut, että se sopii heille. Kaikki kerätyt allekirjoitukset yhdistetään lopulta transaktioon. Jos käyttäjä tai koordinaattori yrittää ohjata varoja uudelleen muokkaamalla coinjoin-transaktion lähtöjä, allekirjoitukset todetaan mitättömiksi, mikä johtaa transaktion hylkäämiseen solmujen toimesta.
Coinjoinin toteutuksia on useita, kuten Whirlpool, JoinMarket tai Wabisabi, joiden tavoitteena on hallita osallistujien välistä koordinaatiota ja lisätä coinjoin-transaktioiden tehokkuutta.
Tässä oppaassa keskitymme suosikkiimplementaatiooni: Whirlpool, joka on saatavilla Samourai Walletissa ja Sparrow Walletissa. Mielestäni se on tehokkain toteutus coinjoineille Bitcoinissa.
## Mikä on coinjoinin hyöty Bitcoinissa?
Coinjoinin hyöty piilee sen kyvyssä tuottaa uskottavaa kiistettävyyttä, hukuttamalla kolikkosi joukkoon erottamattomia kolikoita. Tämän toimenpiteen tavoitteena on katkaista jäljitettävyyslinkit sekä menneisyydestä nykyhetkeen että nykyhetkestä menneisyyteen.

Toisin sanoen, analyytikko, joka tuntee alkuperäisen transaktiosi coinjoin-syklien alussa, ei pitäisi pystyä tunnistamaan varmuudella UTXO:tasi remix-syklien lopussa (analyysi syklin alusta loppuun).

![coinjoin](assets/en/2.webp)

Päinvastoin, analyytikko, joka tuntee UTXO:si coinjoin-syklien lopussa, ei pitäisi pystyä määrittämään alkuperäistä transaktiota syklien alussa (analyysi syklin lopusta alkuun).

![coinjoin](assets/en/3.webp)

Arvioidakseen analyysin vaikeutta yhdistää menneisyys nykyhetkeen ja päinvastoin, on tarpeen määrittää ryhmien koko, joiden sisällä kolikkosi on piilotettu. Tämä mittari kertoo meille analyysien määrän, joilla on identtinen todennäköisyys. Näin ollen, jos oikea analyysi on hukutettu kolmen muun yhtä todennäköisen analyysin joukkoon, peittelyn tasosi on hyvin matala. Toisaalta, jos oikea analyysi on 20 000 yhtä todennäköisen analyysin joukossa, kolikkosi on hyvin piilotettu.

Ja juuri näiden ryhmien koko edustaa indikaattoreita, joita kutsutaan "anonseteiksi".

## Anonsettien ymmärtäminen
Anonsetit toimivat indikaattoreina arvioitaessa tietyn UTXO:n yksityisyyden astetta. Tarkemmin sanottuna ne mittaavat erottamattomien UTXO:jen määrää joukossa, joka sisältää tutkittavan kolikon. Homogeenisen UTXO-joukon vaatimus tarkoittaa, että anonsetit lasketaan yleensä coinjoin-sykleissä. Näiden indikaattorien käyttö on erityisen relevanttia Whirlpool-coinjoineissa niiden yhtenäisyyden vuoksi.

Anonsetit mahdollistavat tarvittaessa coinjoinien laadun arvioinnin. Suuri anonsettikoko tarkoittaa lisääntynyttä nimettömyyden tasoa, sillä tietyn UTXO:n erottaminen joukosta muuttuu vaikeaksi.

Anonsetteja on kahta tyyppiä:
- **Tulevaisuuden anonymiteettijoukko;**
- **Menneisyyden anonymiteettijoukko.**
Ensimmäinen indikaattori näyttää ryhmän koon, jonka seassa tutkittu UTXO piilotetaan syklin lopussa, tietäen UTXO:n syklin alussa, eli ryhmässä läsnä olevien erottamattomien kolikoiden määrän. Tämä indikaattori mahdollistaa kolikon yksityisyyden kestävyyden mittaamisen analyysissä menneisyydestä nykyhetkeen (sisääntulosta ulostuloon). Englanniksi tämän indikaattorin nimi on "forward anonset" tai "forward-looking metrics".
![coinjoin](assets/en/4.webp)
Tämä mittari arvioi, missä määrin UTXO:si on suojattu yrityksiltä rakentaa sen historia uudelleen sen tulopisteestä sen poistopisteeseen coinjoin-prosessissa.

Esimerkiksi, jos transaktiosi osallistui ensimmäiseen coinjoin-sykliin ja kaksi muuta jälkeläissykliä saatiin päätökseen, kolikkosi mahdollinen anonset olisi `13`:

![coinjoin](assets/en/5.webp)

Toinen indikaattori näyttää mahdollisten lähteiden määrän tietylle kolikolle, tietäen UTXO:n syklin lopussa. Tämä indikaattori mittaa kolikon luottamuksellisuuden vastustuskykyä analyysiä vastaan nykyhetkestä menneisyyteen (poistosta tulopisteeseen), eli kuinka vaikeaa analyytikolle on jäljittää kolikkosi alkuperä ennen coinjoin-syklejä. Englanniksi tämän indikaattorin nimi on "*backward anonset*" tai "*backward-looking metrics*".

![coinjoin](assets/en/6.webp)

Tietäen UTXO:si syklien poistopisteessä, retrospektiivinen anonset määrittää mahdollisten Tx0-transaktioiden määrän, jotka olisivat voineet muodostaa sisääntulosi coinjoin-sykleihin. Alla olevassa kaaviossa tämä vastaa kaikkien oranssien kuplien summaa.

![coinjoin](assets/en/7.webp)

## Anonsettien laskeminen Whirlpool Stats Tools (WST) avulla
Voit laskea nämä indikaattorit omille kolikoillesi, jotka ovat käyneet läpi coinjoin-syklejä, käyttämällä Samourai Walletin erityisesti kehittämää työkalua: *Whirlpool Stats Tools*.

Jos sinulla on RoninDojo, WST on esiasennettu solmuusi. Voit siis jättää asennusvaiheet väliin ja suoraan seurata käyttöohjeita. Niille, joilla ei ole RoninDojo-solmua, katsotaan miten tämän työkalun asennus tietokoneelle suoritetaan.

Tarvitset: Tor-selaimen (tai Tor), Python 3.4.4:n tai uudemman, gitin ja pipin. Avaa terminaali. Tarkistaaksesi näiden ohjelmistojen läsnäolon ja version järjestelmässäsi, syötä seuraavat komennot:
```bash
python --version
git --version
pip --version
```

Tarvittaessa voit ladata ne niiden omilta verkkosivuilta:
- https://www.python.org/downloads/ (pip tulee suoraan Pythonin mukana versiosta 3.4 lähtien);
- https://www.torproject.org/download/;
- https://git-scm.com/downloads.
Kun kaikki nämä ohjelmistot on asennettu, kloonaa WST-repositorio terminaalista:
```bash
git clone https://code.samourai.io/whirlpool/whirlpool_stats.git
```

![WST](assets/notext/8.webp)

Siirry WST-hakemistoon:
```bash
cd whirlpool_stats
```

Asenna riippuvuudet:
```bash
pip3 install -r ./requirements.txt
```

![WST](assets/notext/9.webp)

Voit myös asentaa ne manuaalisesti (valinnainen):
```bash
pip install PySocks
pip install requests[socks]
pip install plotly
pip install datasketch
pip install numpy
pip install python-bitcoinrpc
```

Siirry `/whirlpool_stats`-alihakemistoon:
```bash
cd whirlpool_stats
```

Käynnistä WST:
```bash
python3 wst.py
```

![WST](assets/notext/10.webp)

Käynnistä Tor tai Tor-selain taustalla.

**-> RoninDojo-käyttäjät voivat jatkaa opasta suoraan tästä.**

Aseta proxy Torille (RoninDojo),
```bash
socks5 127.0.0.1:9050
```
tai Tor-selaimeen riippuen siitä, mitä käytät:```bash
socks5 127.0.0.1:9150
```

Tämä manipulaatio mahdollistaa datan lataamisen OXT:n kautta Torin avulla, jotta transaktioistasi ei vuoda tietoja. Jos olet aloittelija ja tämä vaihe vaikuttaa monimutkaiselta, tiedä, että se yksinkertaisesti tarkoittaa internet-liikenteesi ohjaamista Torin kautta. Yksinkertaisin menetelmä koostuu Tor-selaimen käynnistämisestä taustalla tietokoneellasi, ja sen jälkeen suoritat vain toisen komennon yhdistääksesi tämän selaimen kautta (`socks5 127.0.0.1:9150`).

![WST](assets/notext/11.webp)

Seuraavaksi siirry työhakemistoon, josta aiot ladata WST-datan käyttäen `workdir`-komentoa. Tämä kansio toimii säilönä transaktiodatalle, jonka noudat OXT:stä `.csv`-tiedostojen muodossa. Tämä tieto on olennaista haluamiesi indikaattorien laskemiseksi. Voit vapaasti valita tämän hakemiston sijainnin. Voisi olla viisasta luoda kansio erityisesti WST-datalle. Esimerkkinä valitkaamme latauskansio. Jos käytät RoninDojoa, tämä vaihe ei ole tarpeellinen:
```bash
workdir path/to/your/directory
```

Komentokehotteen tulisi sen jälkeen muuttua näyttämään työhakemistosi.

![WST](assets/notext/12.webp)

Lataa sitten data altaasta, joka sisältää transaktiosi. Esimerkiksi, jos olen `100,000 sats`-altaassa, komento on:
```bash
download 0001
```

![WST](assets/notext/13.webp)

WST:n nimikoodit ovat seuraavat:
- Allas 0.5 bitcoinit: `05`
- Allas 0.05 bitcoinit: `005`
- Allas 0.01 bitcoinit: `001`
- Allas 0.001 bitcoinit: `0001`
Kun data on ladattu, lataa se. Esimerkiksi, jos olen `100,000 sats`-altaassa, komento on:
```bash
load 0001
```

Tämä vaihe kestää muutaman minuutin riippuen tietokoneestasi. Nyt on hyvä hetki tehdä itsellesi kahvia! :)

![WST](assets/notext/14.webp)

Datan lataamisen jälkeen kirjoita `score`-komento seurattuna TXID:lläsi (transaktiotunniste) saadaksesi sen anonsetit:
```bash
score TXID
```

**Huomio**, TXID:n valinta vaihtelee riippuen siitä, mitä anonsettia haluat laskea. Tulevaisuuden anonsetin arvioimiseksi on tarpeen syöttää `score`-komennon kautta TXID, joka vastaa sen ensimmäistä coinjoinia, mikä on alkuperäinen sekoitus tällä UTXO:lla. Toisaalta, menneisyyden anonsetin määrittämiseksi sinun on syötettävä TXID viimeisimmästä suoritetusta coinjoinista. Yhteenvetona, tulevaisuuden anonsetti lasketaan ensimmäisen sekoituksen TXID:stä, kun taas menneisyyden anonsetti lasketaan viimeisen sekoituksen TXID:stä.

WST näyttää sitten menneisyyden pistemäärän (*Backward-looking metrics*) ja tulevaisuuden pistemäärän (*Forward-looking metrics*). Esimerkiksi otin TXID:n satunnaisesta kolikosta Whirlpoolissa, joka ei kuulu minulle.

![WST](assets/notext/15.webp)
Kyseessä oleva transaktio: [7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be](https://mempool.space/tx/7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be)
Jos tarkastelemme tätä transaktiota kyseisen kolikon ensimmäisenä coinjoin-toimintona, se hyötyy tulevaisuudessa anonset-arvosta `86,871`. Tämä tarkoittaa, että se on piilotettu `86,871` erottamattoman kolikon joukkoon. Ulkopuolinen tarkkailija, joka tuntee tämän kolikon coinjoin-syklien alussa ja yrittää jäljittää sen tulosteen, kohtaa `86,871` mahdollista UTXO:a, joista jokaisella on identtinen todennäköisyys olla etsitty kolikko.

Jos tarkastelemme tätä transaktiota kolikon viimeisenä coinjoin-toimintona, sillä on silloin takautuva anonset-arvo `42,185`. Tämä tarkoittaa, että on olemassa `42,185` potentiaalista lähdettä tälle UTXO:lle. Jos ulkopuolinen tarkkailija tunnistaa tämän kolikon syklien lopussa ja pyrkii jäljittämään sen alkuperän, hän kohtaa `42,185` mahdollista lähdettä, joilla kaikilla on yhtäläinen todennäköisyys olla etsitty alkuperä.

Anonset-arvojen lisäksi WST tarjoaa sinulle myös tietoa tulosteesi diffuusioasteesta altaassa anonset-arvon perusteella. Tämä toinen indikaattori yksinkertaisesti mahdollistaa arvioida parannuspotentiaalisi. Tämä aste on erityisen hyödyllinen tulevaisuuden anonset-arvolle. Todellakin, jos palasi diffuusioaste on 15%, se tarkoittaa, että se voidaan sekoittaa altaan 15%:n kanssa. Se on hyvä, mutta sinulla on silti suuri parannusvara jatkamalla remixauksen. Toisaalta, jos palasi diffuusioaste on 95%, olet lähestymässä altaan rajoja. Voit jatkaa remixauksen, mutta anonset-arvosi ei kasva paljoa.

On tärkeää huomata, että WST:n laskemat anonset-arvot eivät ole täysin tarkkoja. Valtaisan datamäärän käsittelyn vuoksi WST käyttää *HyperLogLogPlusPlus*-algoritmia vähentämään merkittävästi paikallisen datan käsittelyn ja tarvittavan muistin taakkaa. Tämä on algoritmi, joka mahdollistaa erittäin suurten datamäärien ainutlaatuisten arvojen määrän arvioinnin säilyttäen korkean tarkkuuden tuloksessa. Siksi tarjotut arvot ovat riittävän hyviä käytettäväksi analyyseissäsi, koska ne ovat hyvin lähellä todellisuutta, mutta niitä ei tulisi tulkita tarkoiksi arvoiksi yksikköön.

Yhteenvetona pidä mielessä, että ei ole välttämätöntä järjestelmällisesti laskea anonset-arvoja jokaiselle palallesi coinjoineissa. Whirlpoolin suunnittelu itsessään tarjoaa takeita. Todellakin, takautuva anonset on harvoin huolenaihe. Alkuperäisestä sekoituksestasi saat erityisen korkean takautuvan arvon kiitos aiempien sekoitusten perinnön aina Genesis coinjoinista lähtien. Mitä tulevaisuuden anonset-arvoon, riittää, että pidät palasi post-mix-tilillä riittävän pitkän ajanjakson.
Tämän vuoksi pidän Whirlpoolin käyttöä erityisen relevanttina *Hodl -> Mix -> Spend -> Replace* -strategiassa. Mielestäni loogisin lähestymistapa on säilyttää suurin osa bitcoin-säästöistä kylmässä lompakossa, samalla kun ylläpidetään jatkuvasti tietty määrä kolikoita coinjoineissa Samourailla päivittäisten menojen kattamiseksi. Kun bitcoinit coinjoineista on kulutettu, ne korvataan uusilla, jotta palataan määriteltyyn sekoitettujen palasten kynnysarvoon. Tämä menetelmä mahdollistaa vapautumisen UTXO-anonsettien huolesta, samalla kun coinjoineiden tehokkuuden kannalta tarvittava aika muuttuu paljon vähemmän rajoittavaksi.
**Ulkoiset Resurssit:**

- [Podcast ranskaksi ketjuanalyysistä](https://fountain.fm/episode/6nNoQEUHBCQR8hAXAkEx)
- [Wikipedia-artikkeli HyperLogLogista](https://en.wikipedia.org/wiki/HyperLogLog)
- Samourain repositorio Whirlpool Statsille
- Whirlpoolin verkkosivusto Samourailta
- [Medium-artikkeli englanniksi yksityisyydestä ja Bitcoinista Samourailta](https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923)
- [Medium-artikkeli englanniksi anonymiteettisettien konseptista Samourailta](https://medium.com/samourai-wallet/diving-head-first-into-whirlpool-anonymity-sets-4156a54b0bc7)