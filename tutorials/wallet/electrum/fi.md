---
name: Electrum

description: Kattava Electrum-opas alusta sankariksi
---

![kansi](assets/cover.webp)

Kuvaus Electrumista

https://twitter.com/ElectrumWallet
https://electrum.org/
https://electrum.readthedocs.io/

> "Minun täytyy sanoa, että kun törmäsin tähän oppaaseen, olin järkyttynyt. Onnittelut Arman the Parmanille tästä. Olisi ollut sääli, jos tätä ei olisi isännöity täällä ja käännetty mahdollisimman monelle kielelle. Rehellisesti, kippis sille kaverille." Rogzy

Alkuperäinen julkaisu:

![Electrum Desktop Wallet (Mac / Linux) - lataa, varmista, yhdistä solmuusi.](https://youtu.be/wHmQNcRWdHM)

![Bitcoin-siirron tekeminen Electrumin avulla](https://youtu.be/-d_Zd7VcAfQ)

## Miksi Electrum?

Tämä on yksityiskohtainen opas Electrum Bitcoin -lompakon käyttöön, ratkaisuineen kaikkiin sen ansaan ja kummallisuuksiin - jotain, jonka olen kehittänyt useiden käyttövuosien ja Bitcoinin turvallisuuden/yksityisyyden opettamisen jälkeen. Electrum ei ole paras Bitcoin-lompakko henkilölle, joka haluaa pitää kaiken mahdollisimman yksinkertaisena ja pysyä aloittelijatasolla. Sen sijaan se on tarkoitettu henkilölle, joka on, tai pyrkii olemaan, "tehokäyttäjä".

Uudelle Bitcoin-käyttäjälle se on erinomainen vain kokeneen käyttäjän valvonnassa näyttämässä tietä. Jos opettelee käyttämään sitä yksin, se olisi turvallista, kunhan he ottavat aikansa ja käyttävät sitä testiympäristössä vain pienellä määrällä satosheja aluksi. Tämä opas tukee sitä pyrkimystä, mutta se on myös hyvä viite kenelle tahansa muulle.

> Varoitus: Tämä opas on suuri. Älä yritä tehdä kaikkea yhdessä päivässä. On parasta tallentaa opas ja edetä vähitellen ajan kanssa.

## Electrumin lataaminen

Ihanteellisesti käytä omistettua Bitcoin-tietokonetta Bitcoin-siirtoihisi (Oma oppaani tähän https://armantheparman.com/mint/) _(SAATAVILLA myös yksityisyysosiossa)_. On ihan ok harjoitella pienillä määrillä "likaisella" tietokoneella, kun vasta opettelet (kuka tietää, kuinka paljon piilotettua haittaohjelmaa tavallinen tietokoneesi on kerryttänyt vuosien varrella - et halua altistaa Bitcoin-lompakoitasi niille).

Hanki Electrum osoitteesta https://electrum.org/.

Napsauta Lataa-välilehteä yläosassa.

Napsauta latauslinkkiä, joka vastaa tietokonettasi. Mikä tahansa Linux- tai Mac-tietokone voi käyttää Python-linkkiä (punainen ympyrä). Linux-tietokone, jossa on Intel- tai AMD-piiri, voi käyttää Appimagea (vihreä ympyrä; tämä on kuin Windowsin suoritettava tiedosto). Raspberry Pi -laite käyttää ARM-mikroprosessoria ja voi käyttää vain Python-versiota (punainen ympyrä), ei Appimagea, vaikka Pi:t ajavat Linuxia. Sininen ympyrä on Windowsille ja musta ympyrä Macille.

![kuva](assets/1.webp)

## Electrumin varmentaminen

Latauksen "varmentamisen" tarkoitus on varmistaa, ettei yksikään datan bitti ole muuttunut. Se estää sinua käyttämästä "hakkeroidun" pahantahtoisen version ohjelmistosta. On ihan ok jättää tämä väliin, jos käytät ladattua kopiota vain harjoitteluun, ts. älä käytä lompakoita, jotka sisältävät merkittäviä summia rahaa. Sitten, kun olet valmis käyttämään Electrumia oikeille varoillesi, sinun tulisi poistaa kopiosi ja aloittaa alusta, tällä kertaa varmistaen latauksesi.
Tätä varten käytämme julkisen ja yksityisen avaimen kryptografiatyökaluja – gpg, josta olemme kirjoittaneet oppaan täällä (https://armantheparman.com/gpg/). Gpg-työkalu sisältyy kaikkiin Linux-käyttöjärjestelmiin. Macille ja Windowsille, katso gpg-linkistä latausohjeet.
Electrum-ohjelmiston lataamisen lisäksi turvallisuussyistä tarvitset myös ohjelmiston digitaalisen ALLEKIRJOITUKSEN. Tämä on tekstijono (se on itse asiassa numero, joka on koodattu käyttäen tekstiä), jonka kehittäjä on tuottanut yksityisellä gpg-avaimellaan. Käyttämällä gpg-ohjelmaa voimme sitten "testata" ALLEKIRJOITUSTA hänen JULKISTA avaintaan vasten (luotu kehittäjän yksityisestä avaimesta), johon kaikilla on pääsy, verrattuna lataustiedostoon.

Toisin sanoen, kolmella syötteellä (allekirjoitus, julkinen avain ja datatiedosto) saamme tosi tai epätosi tuloksen vahvistaaksemme, että tiedostoa ei ole manipuloitu.

Allekirjoituksen saamiseksi, klikkaa linkkiä, joka vastaa lataamaasi tiedostoa (katso värikkäät nuolet):

![kuva](assets/2.webp)

Linkkiä klikkaamalla tiedosto voi latautua automaattisesti latauskansioosi, tai se voi avautua selaimessa. Jos se avautuu selaimessa, sinun täytyy tallentaa tiedosto. Voit klikata oikealla ja valita "tallenna nimellä". Käyttöjärjestelmästä tai selaimesta riippuen saatat joutua klikkaamaan oikealla tyhjässä tilassa, ei tekstissä.

Alla on, miltä ladattu teksti näyttää. Voit nähdä, että on useita allekirjoituksia – nämä ovat eri ihmisten allekirjoituksia. Voit tarkistaa jokaisen tai minkä tahansa. Näytän sinulle, miten voit tarkistaa vain kehittäjän.

![kuva](assets/3.webp)

Seuraavaksi sinun täytyy saada ThomasV:n julkinen avain – hän on pääkehittäjä. Voit saada sen suoraan häneltä, hänen Keybase-tililtään, Githubista, tai joltakulta muulta, avainpalvelimelta, tai Electrumin verkkosivustolta.

Sen saaminen Electrumin verkkosivustolta on itse asiassa vähiten turvallinen tapa, koska jos tämä verkkosivusto on pahantahtoinen (juuri se, mitä me tarkistamme), miksi me saamme julkisen avaimen sieltä (julkinen avain voisi olla väärennös)?

Pitäen sen yksinkertaisena toistaiseksi, näytän sinulle, miten saada se verkkosivustolta joka tapauksessa, mutta pidä tämä mielessäsi. Tässä on kopio (https://github.com/spesmilo/electrum/blob/master/pubkeys/ThomasV.asc) GitHubissa, johon voit verrata sitä.

Vieritä sivua hieman alaspäin löytääksesi linkin ThomasV:n julkiseen avaimen (punainen ympyrä alla). Klikkaa sitä ja lataa se, tai jos se avaa tekstiä selaimessa, klikkaa oikealla tallentaaksesi.

![kuva](assets/4.webp)

Sinulla on nyt 3 uutta tiedostoa, todennäköisesti kaikki latauskansiossa. Ei ole väliä missä ne ovat, mutta prosessi helpottuu, jos laitat ne kaikki samaan kansioon.

Kolme tiedostoa:

1. Electrumin lataus
2. Allekirjoitustiedosto (yleensä se on sama tiedostonimi kuin Electrumin latauksella, lisänä “.asc”)
3. ThomasV:n julkinen avain.

Avaa terminaali Macissa tai Linuxissa, tai komentokehote (CMD) Windowsissa.

Siirry Lataukset-kansioon (tai minne tahansa laitoit nuo kolme tiedostoa). Jos et tiedä, mitä tämä tarkoittaa, opi tästä lyhyestä videosta Linuxille/Macille (https://www.youtube.com/watch?v=AO0jzD1hpXc) ja tästä toisesta Windowsille (https://www.youtube.com/watch?v=9zMWXD-xoxc). Muista, että Linux-tietokoneissa hakemistonimet ovat kirjainkoosta riippuvaisia.
Terminaalissa kirjoita tämä tuodaksesi ThomasV:n julkisen avaimen tietokoneesi "avainnippuun" (avainnippu on abstrakti käsite – se on itse asiassa vain tiedosto tietokoneellasi):
```bash
gpg --import ThomasV.asc
```

Varmista, että tiedostonimi vastaa ladattuaasi. Huomaa, että käytössä on kaksoisviiva, ei yksittäinen viiva. Huomaa myös, että ennen ja jälkeen "--import" on välilyönti. Paina sitten <enter>.

Tiedoston pitäisi tuoda. Jos saat virheilmoituksen, tarkista oletko hakemistossa, jossa tiedosto todella on. Tarkistaaksesi, missä hakemistossa olet (Macissa tai Linuxissa), kirjoita pwd. Nähdäksesi, mitä tiedostoja hakemistossasi on (Macissa tai Linuxissa), kirjoita ls. Sinun pitäisi nähdä "ThomasV.asc" tekstitiedosto listattuna, mahdollisesti muiden tiedostojen joukossa.

Sitten suoritamme komennon allekirjoituksen tarkistamiseksi.

```bash
gpg --verify Electrum-4.1.5.tar.gz.asc Electrum-4.1.5.tar.gz
```

Huomaa, että tässä on 4 "elementtiä", jotka on erotettu välilyönnillä. Olen vaihtoehtoisesti lihavoinut tekstin auttaakseni sinua näkemään. Neljä elementtiä ovat:

1. gpg-ohjelma
2. --verify-vaihtoehto
3. allekirjoituksen tiedostonimi
4. ohjelman tiedostonimi

Mielenkiintoista on, että joskus voit jättää pois 4. elementin ja tietokone arvaa, mitä tarkoitat. En ole varma, mutta uskon, että se toimii vain, jos tiedostonimet eroavat vain "asc"-päätteestä.

Älä vain kopioi tässä näyttämiäni tiedostonimiä – varmista, että ne vastaavat järjestelmässäsi olevan tiedoston nimeä.

Paina <enter> suorittaaksesi komennon. Sinun pitäisi nähdä "hyvä allekirjoitus ThomasV:lta" osoittamaan onnistumista. Tulee joitakin virheitä, koska meillä ei ole muiden ihmisten allekirjoitusten julkisia avaimia, jotka sisältyvät allekirjoitustiedostoon (tämä allekirjoitusten yhdistämisen järjestelmä saattaa muuttua myöhemmissä versioissa). Lisäksi alareunassa on varoitus, jonka voimme jättää huomiotta (tämä varoittaa meitä siitä, että emme ole nimenomaisesti ilmoittaneet tietokoneelle luottavamme ThomasV:n julkiseen avaimiin).

Nyt meillä on vahvistettu kopio Electrumista, jota on turvallista käyttää.

## Electrumin käyttäminen

### Electrumin käyttäminen Pythonin kanssa

Jos latasit Python-version, näin se toimii. Näet lataussivulla tämän:

![kuva](assets/5.webp)

Linuxille on hyvä idea ensin päivittää järjestelmäsi:

```bash
sudo apt-get update
sudo apt-get upgrade
```

Kopioi keltaisella korostettu teksti, liitä se terminaaliin ja paina <enter>. Sinulta kysytään salasanaasi, mahdollisesti vahvistusta jatkamiseen, ja sitten se asentaa nuo tiedostot ("riippuvuudet").

Sinun on myös purettava pakattu tiedosto haluamaasi hakemistoon. Voit tehdä tämän graafisen käyttöliittymän kautta tai komentoriviltä (vaaleanpunaisella korostettu komento) – muista, että tiedostonimesi voivat erota. (Huomaa, että kun vahvistimme latauksen edellisessä osiossa, vahvistimme zip-tiedoston, ei purettua hakemistoa.)

On olemassa vaihtoehto "asentaa" käyttäen PIP-ohjelmaa, mutta tämä on tarpeetonta ja lisää ylimääräisiä vaiheita sekä tiedostojen asennusta. Käytä ohjelmaa suoraan terminaalista ohittaaksesi kaiken tämän.

Vaiheet (Linux) ovat:

1. siirry hakemistoon, jossa tiedostot on purettu
2. kirjoita: ./run_electrum

Macissa vaiheet ovat samat, mutta saatat ensin tarvita Python3:n asennuksen, ja käytä tätä komentoa suorittaaksesi:

```bash
```python3 ./run_electrum```

Kun Electrum on käynnissä, terminaali-ikkuna pysyy avoinna. Jos suljet sen, Electrum-ohjelma lopettaa toimintansa. Pienennä se vain käyttäessäsi Electrumia.

### Electrumin käyttäminen Appimagen kanssa

Tämä on hieman helpompaa, mutta ei yhtä helppoa kuin Windowsin suoritettava tiedosto. Riippuen Linux-version oletusasetuksista, Appimage-tiedostoilla voi olla attribuutteja asetettu niin, että suoritus on järjestelmän toimesta estetty. Meidän täytyy muuttaa tätä. Jos Appimages toimii, voit ohittaa tämän vaiheen. Siirry terminaalissa tiedoston sijaintiin, ja suorita tämä komento:

```bash
sudo chmod ug+x Electrum-4.1.5-x86_64.AppImage
```

“sudo” antaa superkäyttäjän oikeudet; “chmod” on komento muuttaa tilaa, muokaten kuka voi lukea, kirjoittaa tai suorittaa; “ug+x” tarkoittaa, että muokkaamme käyttäjää ja ryhmää sallimaan suorituksen.

Säädä tiedostonimeä vastaamaan versiotasi.

Sen jälkeen Electrum käynnistyy kaksoisklikkaamalla Appimage-kuvaketta.

### Electrumin käyttäminen Macilla

Kaksoisklikkaa vain ladattua tiedostoa (se on “asema”). Ikkuna avautuu. Vedä Electrumin kuvake ikkunassa työpöydällesi tai minne haluat säilyttää ohjelman. Voit sen jälkeen “poistaa” aseman ja poistaa aseman (ladatun tiedoston).

Ohjelman suorittamiseksi kaksoisklikkaa sitä vain. Saatat saada joitakin Mac-spesifisiä “hoitaja” virheitä, jotka on ohitettava.

### Electrumin käyttäminen Windowsilla

Vaikka inhoankin Windowsia eniten kaikista, tämä on yksinkertaisin menetelmä. Kaksoisklikkaa vain suoritettavaa tiedostoa suorittaaksesi sen.

## Aloita kokeilulompakolla

Kun ensimmäisen kerran lataat Electrumin, ikkuna avautuu näin:

![kuva](assets/6.webp)

Valitsemme myöhemmin palvelimesi manuaalisesti, mutta toistaiseksi jätä oletus ja auto-yhdistä.

Luo seuraavaksi kokeilulompakko – älä koskaan laita varoja tähän lompakkoon. Tämän kokeilulompakon tarkoitus on edetä ohjelmiston läpi ja varmistaa, että kaikki toimii hyvin ennen kuin lataat oikean lompakkosi. Yritämme välttää todellisen lompakon yksityisyyden vahingossa luovuttamista. Jos harjoittelet vain, luomasi lompakko voidaan pitää joka tapauksessa kokeilulompakkona.

Voit jättää nimen “default_wallet” tai muuttaa sen mieleiseksesi ja klikkaa seuraava. Myöhemmin, jos sinulla on useita lompakoita, voit löytää ja avata ne tässä vaiheessa ensin klikkaamalla “Valitse…”

![kuva](assets/7.webp)

Valitse “Standard wallet” ja <Seuraava>:

![kuva](assets/8.webp)

Valitse sitten “Minulla on jo siemen”. En halua sinun tottuvan luomaan Electrumin siementä, koska se käyttää omaa protokollaansa, joka ei ole yhteensopiva muiden lompakoiden kanssa – tämän vuoksi emme klikkaa “uusi siemen”.

![kuva](assets/9.webp)

Mene osoitteeseen https://iancoleman.io/bip39/ ja luo kokeilusiemen. Vaihda ensin sanamäärä 12:ksi (joka on yleinen käytäntö), sitten klikkaa “generoi” ja kopioi sanat laatikosta leikepöydällesi.

![kuva](assets/10.webp)

Liitä sitten sanat Electrumiin. Tässä on esimerkki:

![kuva](assets/11.webp)

Electrum etsii sanoja, jotka vastaavat omaa protokollaansa. Meidän täytyy ohittaa tämä. Klikkaa asetuksia ja valitse BIP39 Siemen:

![kuva](assets/12.webp)
Siemen muuttuu täten kelvolliseksi. (Ennen tätä, Electrum odotti Electrumin siementä, joten tämä siemen nähtiin kelvottomana). Ennen kuin klikkaat seuraavaa, huomaa teksti, joka sanoo "Checksum OK". On tärkeää (oikeaa lompakkoa myöhemmin käytettäessä), että näet tämän ennen jatkamista, sillä se vahvistaa syöttämäsi siemenen kelvollisuuden. Varoitus alareunassa voidaan jättää huomiotta, se on Electrumin kehittäjien valitusta BIP39:stä ja heidän "FUD'maisista" väitteistään, että heidän versionsa (joka ei ole yhteensopiva muiden lompakoiden kanssa) on parempi.

> Nopea kiertotie tärkeään varoitukseen. Tarkoituksena tarkistussumman kanssa on varmistaa, että olet syöttänyt siemenesi ilman kirjoitusvirheitä. Tarkistussumma on siemenen viimeinen osa (12. sana on tarkistussumman sana), joka matemaattisesti määräytyy siemenen ensimmäisen osan (11 sanaa) perusteella. Jos kirjoittaisit jotain väärin alussa, tarkistussumman sana ei matemaattisesti täsmäisi, ja lompakko-ohjelmisto varoittaisi sinua varoituksella. Tämä ei tarkoita, että siementä ei voisi käyttää toimivan Bitcoin-lompakon luomiseen. Kuvittele luovasi lompakon kirjoitusvirheellä, lataavasi lompakon bitcoineilla, sitten eräänä päivänä saatat tarvita palauttaa lompakon, mutta kun teet niin, et toista kirjoitusvirhettä – palautat väärän lompakon! On melko vaarallista, että Electrum antaa sinun jatkaa lompakon tekemistä, jos tarkistussummasi on virheellinen, joten ole varoitettu, se on sinun vastuullasi varmistaa. Muut lompakot eivät anna sinun jatkaa, mikä on paljon turvallisempaa. Tämä on yksi niistä asioista, joita tarkoitan kun sanon, että Electrumin käyttö on ok, kunhan opit käyttämään sitä oikein (Electrumin kehittäjien pitäisi korjata tämä).

Huomaa, että jos haluaisit lisätä salasanan, mahdollisuus valita se on tässä vaihtoehtoikkunassa, aivan yläosassa.

OK:n klikkaamisen jälkeen sinut viedään takaisin kohtaan, jossa kirjoitit siemenlauseen. Jos valitsit salasana-vaihtoehdon, ET syötä sitä siemensanojen kanssa (kehotus tähän tulee seuraavaksi).

Jos et pyytänyt salasanaa, näet seuraavaksi tämän näytön – lisää vaihtoehtoja lompakkosi skriptityypille ja johdannaispolulle, joista voit oppia täällä (https://armantheparman.com/public-and-private-keys/), mutta jätä vain oletusarvot ja jatka.

![kuva](assets/13.webp)

> Lisätietoja varten: Ensimmäinen vaihtoehto antaa sinun valita legacy (osoitteet alkavat "1"), pay-to-script-hash (osoitteet alkavat "3") tai bech32/native segwit (osoitteet alkavat "bc1q") välillä. Kirjoitushetkellä Electrum ei vielä tue taprootia (osoitteet alkavat "bc1p"). Toinen vaihtoehto tässä ikkunassa antaa sinun muokata johdannaispolkua. Ehdotan, että et koskaan muokkaa tätä, erityisesti ennen kuin ymmärrät, mitä se tarkoittaa. Ihmiset korostavat johdannaispolun kirjaamisen tärkeyttä, jotta voit palauttaa lompakkosi tarvittaessa, mutta jos jätät sen oletusarvoon, todennäköisesti pärjäät hyvin, joten älä paniikoi – mutta on silti hyvä käytäntö kirjata johdannaispolku ylös.

Seuraavaksi sinulle annetaan mahdollisuus lisätä SALASANA. Tätä ei pidä sekoittaa "SALASANAAN". Salasana lukitsee tiedoston tietokoneellasi. Salasana on osa yksityisen avaimen muodostusta. Koska tämä on kuvitteellinen lompakko, voit jättää salasanan tyhjäksi ja jatkaa.

![kuva](assets/14.webp)
Saat ilmoituksen uudesta versiosta (suosittelen, että valitset ei). Lompakko luo itsensä ja on käyttövalmis (mutta muista, että tämä lompakko on tarkoitettu poistettavaksi, se on vain harjoituslompakko).
![kuva](assets/15.webp)

On joitakin asioita, joita suosittelen tekemään ohjelmistoympäristön asettamiseksi (vaaditaan vain kerran):

### Vaihda yksiköt BTC:ksi

Mene ylävalikkoon, työkalut –> electrum asetukset, ja siellä yleiset-välilehdellä, löydät vaihtoehdon vaihtaa “perusyksikkö” BTC:ksi.
Ota käyttöön Osoitteet ja Kolikot -välilehti

Mene ylävalikkoon, näkymä, ja valitse “näytä osoitteet”. Mene sitten takaisin näkymään ja valitse “näytä kolikot”.

### Ota käyttöön Oneserver

Oletuksena Electrum yhdistää satunnaiseen solmuun. Se myös yhdistää moniin muihin toissijaisiin solmuihin. En ole varma, mitä tietoja näiden toissijaisten solmujen kanssa vaihdetaan, mutta emme halua sen tapahtuvan yksityisyyden vuoksi. Vaikka määrittelisit solmun, esim. oman solmusi, näihin muihin moniin solmuihin yhdistetään silti, enkä ole varma, mitä tietoja jaetaan. Joka tapauksessa, sen estäminen on helppoa. Ennen kuin näytän, miten määritellä oma solmusi, pakotamme Electrumin yhdistämään vain yhteen palvelimeen kerrallaan.

> Tämän voi tehdä määrittelemällä “oneserver” komentoriviltä, mutta en suosittele tätä tapaa. Näytän vaihtoehtoisen tavan, joka mielestäni on helpompi pitkällä aikavälillä, ja todennäköisemmin estää sinua yhdistämästä vahingossa muihin solmuihin.

Syy siihen, miksi käytämme harjoituslompakkoa, on se, että jos olisimme ladanneet oikean lompakkomme, jossa on oikeat bitcoinimme, olisimme jo vahingossa yhdistäneet satunnaiseen solmuun (vaikka olisimme valinneet “asettaa palvelimen manuaalisesti” alussa, se silti yhdistää näihin muihin toissijaisiin solmuihin jostain syystä (hei Electrum-kehittäjät, teidän pitäisi korjata tämä). Jos lompakkomme olisi yksityinen, tämä olisi katastrofi.

Emme myöskään voi tehdä alla näyttämiäni vaiheita lataamatta ensin jonkinlaista lompakkoa. (Aiomme muokata konfiguraatiotiedostoa, joka täyttyy ja valmistuu muokattavaksi vasta, kun lompakko on ladattu).

**Sulje Electrum (TÄRKEÄÄ, jos et tee tätä, seuraavat tekemäsi muutokset poistetaan).**

### LINUX/MAC Konfiguraatiotiedosto

Avaa terminaali Linuxissa tai Macissa (Windows-ohjeet myöhemmin):

Sinun pitäisi automaattisesti olla kotikansiossa. Sieltä, siirry piilotettuun electrum asetuskansioon (tämä eroaa sovelluksen sijainnista).

```bash
cd .electrum
```

Huomaa piste “electrum” edessä, mikä osoittaa sen olevan piilotettu kansio.

Toinen tapa päästä sinne on kirjoittaa:

```bash
cd ~/.electrum
```

missä “~” edustaa kotihakemistosi polkua. Voit nähdä nykyisen hakemistosi täyden polun komennolla “pwd“.

Kun olet “.electrum”-hakemistossa, kirjoita “nano config” ja paina <enter>.

Tekstieditori avautuu (kutsutaan nano) config-tiedoston kanssa avoinna. Hiiri ei toimi täällä paljoa. Käytä nuolinäppäimiä päästäksesi riviin, joka sanoo:

```json
"oneserver": false,
```

Muuta “false” “true”:ksi; äläkä häiritse syntaksia (älä poista pilkkua tai puolipistettä).

Paina <ctrl> x, poistuaksesi, sitten “y” tallentaaksesi, sitten <enter> vahvistaaksesi muutoksen muokkaamatta tiedostonimeä.
Käynnistä Electrum uudelleen. Klikkaa sitten alaoikealla olevaa ympyrää, joka avaa verkon asetukset. Sitten, yläosassa yleiskatsaus-välilehdellä, näet "yhteydessä 1 solmuun" - tämä osoittaa onnistumista.
Juuri sen alapuolella näet tekstikentän ja palvelimen osoite on siinä. Olet tällä hetkellä yhteydessä tuohon satunnaiseen solmuun. Lisää solmuun yhdistämisestä seuraavassa osiossa.

### Windowsin konfiguraatiotiedosto

Windowsin konfiguraatiotiedoston löytäminen on hieman vaikeampaa. Hakemisto on: `C:/Users/Parman/AppData/Roaming/Electrum`

Ilmeisesti sinun täytyy vaihtaa "Parman" omaksi käyttäjänimeksesi tietokoneella.

Tässä kansiossa löydät konfiguraatiotiedoston. Avaa se tekstieditorilla ja muokkaa riviä:

```json
"oneserver": false,
```

Muuta "false" "true":ksi; älä häiritse syntaksia (älä poista pilkkua tai puolipistettä).

Tallenna sitten tiedosto ja poistu.

## Yhdistä Electrum solmuun

Seuraavaksi haluamme yhdistää dummy-lompakkomme valitsemaamme solmuun. Jos et ole valmis pyörittämään solmua, voit tehdä yhden seuraavista:

1. Yhdistä ystäväsi henkilökohtaiseen solmuun (vaatii Torin)
2. Yhdistä luotettavan yrityksen solmuun
3. Yhdistä satunnaiseen solmuun (ei suositella).

Muuten, tässä ovat ohjeet oman solmun pyörittämiseen, ja nämä ovat syyt miksi sinun pitäisi. (kaikki tutoriaalit Solmu-osiossa tai ilmaisilla kursseillamme)

### Yhdistä ystävän solmuun Torin kautta (Opas tulossa pian.)

### Yhdistä luotettavan yrityksen solmuun

Ainoa syy tehdä tämä olisi, jos sinun on päästävä käsiksi lohkoketjuun eikä sinulla ole omaa solmua käytettävissä (tai ystävän).

Yhdistetään Bitaroon solmuun - meille on kerrottu, että he eivät kerää tietoja. He ovat Bitcoin Only -vaihto, jonka pyörittää intohimoinen Bitcoin-harrastaja. Heihin yhdistäminen vaatii hieman luottamusta, mutta se on parempi kuin yhdistäminen satunnaiseen solmuun, joka voisi olla valvontayritys.

Siirry Verkon Asetuksiin klikkaamalla ympyrää lompakon ikkunan alaoikeassa osassa (punainen osoittaa, ettei ole yhteydessä, vihreä osoittaa yhteydessä olemista ja sininen osoittaa yhteydessä olemista Torin kautta).

![image](assets/16.webp)

Kun klikkaat ympyräkuvaketta, ponnahdusikkuna ilmestyy: Lompakkosi näyttää "yhteydessä 1 solmuun", koska pakotimme sen aikaisemmin.

Poista valinta "valitse palvelin automaattisesti" -ruudusta, ja sitten Palvelin-kentässä, kirjoita Bitaroon tiedot kuten näytetään:

![image](assets/17.webp)

Sulje ikkuna, ja nyt meidän pitäisi olla yhteydessä Bitaroon solmuun. Vahvistaaksesi, ympyrän tulisi olla vihreä. Klikkaa sitä uudelleen ja tarkista, etteivät palvelimen tiedot ole vaihtuneet takaisin satunnaiseen solmuun.

### Yhdistä omaan solmuusi

Jos sinulla on oma solmusi, se on hienoa. Jos sinulla on vain Bitcoin Core, eikä Electrum SERVERIÄ, et vielä pysty yhdistämään Electrum LOMPAKKOA solmuusi.

> Huom: Electrum Server ja Electrum Lompakko ovat eri asioita. Palvelin on ohjelmisto, joka vaaditaan, jotta Electrum Lompakko pystyy kommunikoimaan Bitcoin-lohkoketjun kanssa - en tiedä miksi se on suunniteltu näin - mahdollisesti nopeuden vuoksi, mutta saatan olla väärässä.
Jos käytät solmuohjelmistopakettia, kuten MyNode (jonka suosittelen aloittelijoille), Raspiblitz (suositeltava, kun taidot kehittyvät) tai Umbrel (henkilökohtaisesti en vielä suosittele, koska olen kohdannut liikaa ongelmia), pystyt yhdistämään lompakkosi yksinkertaisesti syöttämällä tietokoneen (Raspberry Pi) IP-osoitteen, jossa solmu on käynnissä, plus kaksoispisteen ja 50002, kuten edellisessä osiossa olevassa kuvassa näytetään. (Myöhemmin näytän, miten löydät solmusi IP-osoitteen).
Avaa Verkkoasetukset (napsauta vihreää tai punaista ympyrää oikeassa alakulmassa). Poista valinta "valitse palvelin automaattisesti" -ruudusta, syötä sitten IP-osoitteesi kuten minä olen tehnyt; sinun osoitteesi on erilainen, mutta kaksoispiste ja "50002" tulisi olla samat.

![kuva](assets/18.webp)

Sulje ikkuna, ja nyt meidän pitäisi olla yhdistetty solmuusi. Vahvistaaksesi, napsauta ympyrää uudelleen ja tarkista, etteivät palvelimen tiedot ole vaihtuneet takaisin satunnaiseen solmuun.

Joskus, vaikka kaikki tehtäisiin oikein, yhteys ei vain toimi. Tässä muutamia kokeiltavia asioita...

- Päivitä uudempaan versioon Electrumista ja solmuohjelmistostasi
- Kokeile poistaa välimuistikansio ".electrum"-hakemistossa
- Kokeile vaihtaa portti 50002:sta 50001:een verkkoasetuksissa
- Käytä tätä opasta yhdistääksesi käyttäen Toria vaihtoehtona (https://armantheparman.com/tor/)
- Asenna Electrum Server uudelleen solmullesi

## SOLMUSI IP-OSOITTEEN LÖYTÄMINEN

IP-osoite ei ole jotain, mitä tavallinen käyttäjä yleensä tietää etsiä ja käyttää. Olen auttanut monia ihmisiä käyttämään solmua ja sitten yhdistämään heidän lompakkonsa solmuun – usein kompastuskivenä näyttää olevan sen IP-osoitteen löytäminen.

MyNodea varten voit kirjoittaa selaimen ikkunaan: `mynode.local`

Joskus "mynode.local" ei toimi (varmista, ettet kirjoita sitä Google-hakupalkkiin. Pakottaaksesi navigointipalkin tunnistamaan tekstisi osoitteeksi eikä haun kohteeksi, aloita teksti `http://` näin: `http://mynode.local`. Jos se ei toimi, kokeile lisätä "s", näin: `https://mynode.local`.

Tämä avaa laitteen, ja voit napsauttaa asetusten linkkiä (katso sininen "ympyräni" alla) näyttääksesi tämän näytön, jossa IP-osoite sijaitsee:

![kuva](assets/19.webp)

Tämä sivu latautuu ja näet solmun IP:n (sininen "ympyrä")

![kuva](assets/20.webp)

Tulevaisuudessa voit kirjoittaa 192.168.0.150 tai http://192.168.0.150 selaimeesi.

Raspiblitzille (kun et yhdistä näyttöä), tarvitset eri menetelmän (joka toimii myös MyNodella):

Kirjaudu reitittimesi verkkosivulle – täältä löydämme kaikkien yhdistettyjen laitteidesi IP-osoitteet. Reitittimen verkkosivu on IP-osoite, jonka syötät verkkoselaimeen. Omani näyttää tältä:

    http://192.168.0.1

Reitittimen kirjautumistiedot löydät käyttöohjeesta tai joskus jopa reitittimen itseensä kiinnitetystä tarrasta. Etsi käyttäjätunnus ja salasana. Jos et löydä sitä, kokeile Käyttäjä: "admin" Salasana: "password"

Jos pääset kirjautumaan sisään, näet yhdistetyt laitteesi ja niiden nimistä saattaa olla selvää, mikä on solmusi. IP-osoite on siellä.
### Jos kaksi ensimmäistä menetelmää epäonnistuvat, viimeinen toimii, mutta se on työläs:
Ensiksi, löydä minkä tahansa laitteen IP-osoite verkossasi (nykyinen tietokoneesi käy).

Mac-käyttäjänä löydät sen Verkkoasetuksista:

![kuva](assets/21.webp)

Olemme kiinnostuneita ensimmäisistä 4 elementistä (192.168.0), ei neljännestä elementistä, "166", jonka näet kuvassa (sinun on erilainen).

Linuxille, käytä komentoriviä:

```bash
ifconfig | grep inet
```

Tuo pystyviiva on "putki" symboli ja löydät sen <delete> näppäimen alta. Näet jotain tulostetta ja IP-osoitteen. (Jätä huomiotta 127.0.0.1, se ei ole se, ja jätä huomiotta myös verkkopeite)

Windowsille, avaa komentokehote (cmd) ja kirjoita:

```bash
ipconfig/all
```

ja paina Enter. IP-osoitteen löydät tulosteesta.

Tuo oli helppo osa. Vaikea osa on nyt löytää solmusi IP-osoite – meidän täytyy arvailla voimakeinolla. Sanotaan esimerkiksi, että tietokoneesi IP-osoite alkaa 192.168.0.xxx, sitten solmullesi, selaimessa, kokeile: `https://192.168.0.2`

Pienin mahdollinen numero on 2 (0 tarkoittaa mitä tahansa laitetta, ja 1 kuuluu reitittimelle) ja suurin, uskoakseni on 255 (tämä sattuu olemaan 11111111 binäärinä, suurin numero, jonka 1 tavu voi sisältää).

Työskentele yksi kerrallaan kohti 255. Lopulta pysähdyt oikeaan numeroon, joka lataa MyNode-sivusi (tai RaspiBlitz-sivusi). Sitten tiedät, minkä numeron syöttää Electrum-verkkoasetuksiisi yhdistääksesi solmuusi.

Se näyttää jotakuinkin tältä (muista sisällyttää kaksoispiste ja numero sen jälkeen):

![kuva](assets/22.webp)

> On hyödyllistä tietää, että nämä IP-osoitteet ovat SISÄISIÄ kotiverkossasi. Kukaan ulkopuolinen ei voi nähdä niitä, eivätkä ne ole arkaluonteisia. Ne ovat kuin puhelinjatkeet suuressa organisaatiossa ohjaten sinut eri puhelimiin.

## Poista teko-lompakko

Nyt olemme onnistuneesti yhdistäneet yhteen ja ainoaan solmuun. Näin Electrum latautuu oletuksena tästä lähtien. Sinun tulisi nyt poistaa teko-lompakko (Valikko: tiedosto –> poista), jotta et vahingossa lähetä varoja tähän turvattomaan lompakkoon (Se on turvaton, koska emme luoneet sitä turvallisella tavalla).

## Tee harjoituslompakko

Teko-lompakon poistamisen jälkeen aloita alusta ja tee uusi samalla tavalla, vain tällä kertaa, kirjoita ylös siemenlauseet ja säilytä ne melko turvallisesti.

On hyvä idea oppia, miten Electrum toimii tällä harjoituslompakolla, ilman hankalaa laitteistolompakkoa (tarvitaan korkeaan turvallisuuteen). Laita vain pieni määrä bitcoineja tähän lompakkoon – Oleta, että menetät nämä rahat. Kun olet taitava, opettele käyttämään Electrumia laitteistolompakon kanssa.

Uudessa lompakossasi, jonka olet luonut, näet listan osoitteista. Vihreitä kutsutaan "vastaanotto-osoitteiksi". Ne ovat kolmen asian tuote:

- Siemenlause
- Salasana
- Johdannaispolku

Uudella lompakollasi on joukko vastaanotto-osoitteita, jotka voidaan matemaattisesti ja toistettavasti luoda millä tahansa ohjelmistolompakolla, jolla on siemen, salasana ja johdannaispolku. Niitä on 4,3 miljardia! Enemmän kuin tarvitset. Electrum näyttää vain ensimmäiset 20, ja sitten lisää, kun käytät ensimmäisiä.
Lisätietoja Bitcoinin yksityisavaimista löytyy tästä oppaasta.
![kuva](assets/23.webp)

Tämä eroaa huomattavasti joistakin muista lompakoista, jotka esittävät kerrallaan vain yhden osoitteen.

Koska syötit siemenlauseen tämän lompakon luomisen yhteydessä, Electrumilla on yksityisavain jokaiseen osoitteeseen, ja näistä osoitteista on mahdollista käyttää varoja.

Huomaa myös, että on olemassa keltaisia osoitteita, joita kutsutaan "vaihto-osoitteiksi" – Nämä ovat vain toinen joukko osoitteita eri matemaattisesta haarasta (näitä on olemassa toiset 4,3 miljardia). Lompakko käyttää näitä automaattisesti lähettämään ylimääräiset varat takaisin lompakkoon vaihtorahana. Esimerkiksi, jos otat 1,5 bitcoinia ja käytät 0,5 kauppiaalle, 1,0 jäännöksen on mentävä jonnekin. Lompakkosi käyttää seuraavaa tyhjää keltaista vaihto-osoitetta – muussa tapauksessa se menee louhijalle! Lisätietoja tästä (UTXOista) löytyy tästä oppaasta. (https://armantheparman.com/utxo/)

Seuraavaksi, palaa takaisin Ian Colmanin yksityisavain-sivustolle ja syötä siemen (sen sijaan, että generoisit uuden). Näet alla, että yksityisen ja julkisen avaimen tiedot muuttuvat; kaikki alla riippuu yläpuolella sivulla olevista asioista.

> Muista, että sinun ei pitäisi "koskaan" syöttää siementä tietokoneelle oikealle Bitcoin-lompakollesi – haittaohjelma voi varastaa sen. Käytämme vain harjoituslompakkoa, oppimistarkoituksiin, joten se on toistaiseksi kunnossa.

Vieritä alas ja vaihda johdannaispolku BIP84:ään (segwit) vastaamaan Electrum-lompakkoasi napsauttamalla BIP84-välilehteä.

![kuva](assets/24.webp)

Alla näet tilin laajennetun yksityisavaimen ja tilin laajennetun julkisen avaimen:

![kuva](assets/25.webp)

Mene Electrumiin ja vertaa, että ne täsmäävät. Ylävalikossa on kohta, lompakko ->tiedot:

![kuva](assets/26.webp)

Tämä ponnahdusikkuna tulee näkyviin:

![kuva](assets/27.webp)

Huomaa, että kaksi julkista avainta täsmäävät.

Seuraavaksi, vertaa osoitteita. Palaa takaisin Ian Colemanin sivustolle ja vieritä alas:

![kuva](assets/28.webp)

Huomaa, että ne täsmäävät Electrumin osoitteiden kanssa.

Nyt tarkistamme vaihto-osoitteet. Vieritä hieman ylös johdannaispolkuun ja vaihda viimeinen 0 ykköseksi:

![kuva](assets/29.webp)

Nyt vieritä alas ja vertaa, että osoitteet täsmäävät Electrumin keltaisten osoitteiden kanssa

Miksi teimme kaiken tämän?

Otimme siemensanat ja syötämme ne kahteen eri riippumattomaan ohjelmistoon varmistaaksemme, että ne antavat meille samat tiedot. Tämä vähentää merkittävästi riskiä, että sisällä piileskelee pahantahtoista koodia antamassa meille vääriä yksityisiä tai julkisia avaimia tai osoitteita.

Seuraava askel on vastaanottaa pieni testi ja käyttää sitä lompakossa osoitteesta toiseen.

## Lompakon testaaminen (Opi käyttämään sitä)

Tässä näytän, miten vastaanottaa UTXO lompakkoosi ja sitten siirtää se (käyttää sitä) toiseen osoitteeseen lompakon sisällä. Kyseessä on hyvin pieni määrä, jonka menettämistä emme pane pahaksemme.

Tällä on useita tarkoituksia.

- Se todistaa, että sinulla on valta käyttää kolikoita uudessa lompakossa.
- Se näyttää, miten käyttää Electrum-ohjelmistoa suorittamaan maksun (ja joitakin ominaisuuksia), ennen kuin lisäämme lisää monimutkaisuutta turvallisuuden vuoksi (käyttämällä laitteistolompakkoa tai ilmaraollista tietokonetta)
- Se vahvistaa ajatuksen, että sinulla on monia osoitteita valittavana vastaanottamiseen ja käyttämiseen samassa lompakossa.
Avaa testi Electrum Lompakkosi ja klikkaa Osoitteet-välilehteä, sitten oikea-klikkaa ensimmäistä osoitetta ja valitse Kopioi –> Osoite:
![kuva](assets/30.webp)

Osoite on nyt tietokoneesi muistissa.

Mene nyt pörssiin, jossa sinulla on hieman bitcoineja, ja nostetaan pieni määrä tähän osoitteeseen, sanotaan 50 000 satoshia. Käytän esimerkkinä Coinbasea, koska se on yleisimmin käytetty pörssi, vaikka he ovatkin Bitcoinin vihollisia, ja minua inhottaa kirjautua vanhaan hylättyyn tiliini tätä tarkoitusta varten.

Kirjaudu sisään ja klikkaa Lähetä/Vastaanota -painiketta, joka tänään on verkkosivun oikeassa yläkulmassa.

![kuva](assets/31.webp)

Minulla ei ilmeisesti ole varoja Coinbasessa, mutta kuvittele, että täällä on varoja ja seuraa mukana: Liitä osoite Electrumista "Vastaanottaja" -kenttään, kuten olen tehnyt. Sinun täytyy myös valita summa (ehdotan noin 50 000 satoshia). Älä laita "valinnaista viestiä" – Coinbase kerää tarpeeksi tietojasi (ja myy niitä), ei ole tarvetta auttaa heitä. Lopuksi klikkaa "Jatka". Sen jälkeen en tiedä, mitä muita ponnahdusikkunoita saat, olet omillasi, mutta menetelmä on samankaltainen kaikissa pörsseissä.

![kuva](assets/32.webp)

Riippuen pörssistä, saatat nähdä satoshit lompakossasi välittömästi tai viiveellä tunteja/päiviä.

Huomaa, että Electrum näyttää vastaanotetut kolikot, vaikka niitä ei olisi vahvistettu lohkoketjussa. Sinulla olevat kolikot luetaan Bitcoin Noden odotuslistalta, eli "mempoolista". Kun se siirtyy lohkoon, näet varat vahvistettuina.

Nyt kun meillä on UTXO lompakossamme, meidän pitäisi merkitä se. Vain me voimme nähdä tämän merkinnän, sillä sillä ei ole mitään tekemistä julkisen kirjanpidon kanssa. Kaikki Electrum-merkintämme ovat näkyvissä vain käyttämällämme tietokoneella. Voimme itse asiassa tallentaa tiedoston ja käyttää sitä palauttaaksemme kaikki merkintämme toiselle tietokoneelle, jossa on sama lompakko.

### Tee merkintä UTXO:lle

Tarvitsin lahjoituksen tähän testilompakkoon, kiitos @Sathoarderille, joka tarjosi minulle elävän UTXO:n (10 000 satoshia), ja toinen henkilö (nimetön) lahjoitti samaan osoitteeseen (5000 satoshia). Huomaa, että ensimmäisen osoitteen saldossa on 15 000 satoshia ja yhteensä 2 siirtoa (oikeassa sarakkeessa). Alhaalla saldo on 10 000 satoshia vahvistettuna ja toiset 5 000 satoshia ovat vahvistamattomia (vielä mempoolissa).

![kuva](assets/33.webp)

Nyt, jos menemme Kolikot-välilehdelle, voimme nähdä kaksi "vastaanotettua kolikkoa" eli UTXO:ta. Ne ovat molemmat samassa osoitteessa.

![kuva](assets/34.webp)

Palatessamme osoitevälilehteen, jos tuplaklikkaat "merkinnät" -aluetta osoitteen vieressä, voit syöttää tekstiä, sitten paina <enter> tallentaaksesi:

![kuva](assets/35.webp)

Tämä on hyvä käytäntö, jotta voit seurata, mistä kolikkosi ovat tulleet, ovatko ne KYC-vapaita vai eivät, ja paljonko jokainen UTXO maksoi sinulle (jos sinun tarvitsee myydä ja laskea vero, joka sinulta varastetaan hallituksesi toimesta).
Ideaalitilanteessa sinun tulisi välttää useiden kolikoiden kasaantumista samaan osoitteeseen. Jos kuitenkin päätät tehdä niin (älä tee niin), voit nimetä jokaisen kolikon erikseen sen sijaan, että käyttäisit samaa nimeä kaikille käyttämällä osoitemenetelmää. Et voi itse asiassa mennä "kolikot"-välilehteen ja muokata nimiä siellä (ei, se olisi liian intuitiivista!). Sinun on mentävä Historia-välilehteen, löydettävä transaktio, nimettävä se, ja sitten näet nimet kolikko-osiossa. Kaikki kolikko-osiossa näkemäsi nimet ovat joko Osoitenimistä TAI historian nimiä, mutta mikä tahansa historian nimi ohittaa osoitenimen. Nimien varmuuskopioimiseksi tiedostoon voit viedä ne ylävalikosta, lompakko–>nimet–>vie.

Seuraavaksi, käytetään kolikoita ensimmäisestä osoitteesta toiseen osoitteeseen. Napsauta ensimmäistä osoitetta hiiren kakkospainikkeella ja valitse "käytä tästä" (Tämä ei itse asiassa ole tarpeellista tässä skenaariossa, mutta kuvittele, että meillä on monta kolikkoa monissa osoitteissa; käyttämällä tätä toimintoa, voimme pakottaa lompakon käyttämään vain niitä kolikoita, joita haluamme. Jos haluamme valita useita kolikoita useissa osoitteissa, voimme valita osoitteet vasemmalla hiiren painikkeella pitäen komento-näppäintä alhaalla, sitten napsauttaa hiiren kakkospainikkeella ja valita "käytä tästä":

![kuva](assets/36.webp)

Kun teet niin, lompakon alareunassa näkyy vihreä palkki, joka osoittaa valittujen kolikoiden määrän ja kokonaismäärän, joka on käytettävissä.

Voit myös käyttää yksittäisiä kolikoita osoitteessa ja jättää muita käyttämättä samassa osoitteessa, mutta tätä ei suositella, koska jätät kolikoita osoitteeseen, joka on kryptografisesti heikentynyt yhden kolikon käytön vuoksi (toinen syy olla laittamatta useita kolikoita yhteen osoitteeseen, yksityisyyssyiden lisäksi, on se, että jos käytät yhden, sinun pitäisi käyttää ne kaikki, mikä tulee tarpeettoman kalliiksi). Näin valitset yksittäisen kolikon jaetusta osoitteesta, mutta älä tee sitä:

![kuva](assets/37.webp)

Nyt meillä on kaksi kolikkoa valittuna käytettäväksi. Seuraavaksi päätämme, mihin ne käytetään. Lähetetään ne toiseen osoitteeseen. Meidän on kopioitava osoite näin:

![kuva](assets/38.webp)

Sitten siirry "Lähetä"-välilehteen ja liitä toinen osoite "maksa"-kenttään. Kuvausta ei tarvitse lisätä; voisit, mutta voit tehdä sen myöhemmin muokkaamalla nimiä. Määräksi valitse "Max" käyttääksesi kaikki valitut kolikot. Sitten klikkaa "Maksa", ja sitten klikkaa "edistynyt"-painiketta, joka ilmestyy ponnahdusikkunaan.

![kuva](assets/39.webp)

Klikkaa aina "edistynyt" tässä vaiheessa, jotta voimme saada tarkan hallinnan ja tarkistaa tarkalleen, mitä transaktiossa on. Tässä on transaktio:

![kuva](assets/40.webp)

Näemme kaksi sisäistä valkoista ikkunaa. Ylempi on syötteiden ikkuna (mitkä kolikot käytetään), ja alempi on tulosteet (minne kolikot menevät).

Huomaa, että tila (ylävasemmalla) on "allekirjoittamaton" toistaiseksi. "Lähetetty määrä" on 0, koska kolikot siirretään lompakon sisällä. Maksu on 481 sats. Huomaa, että jos se olisi 480 sats, viimeinen nolla putoaisi pois, näin, 0.0000048 ja väsyneelle silmälle tämä voi näyttää 48 satsilta – ole varovainen (jotain, minkä Electrum-kehittäjien pitäisi korjata).
Transaktioon liittyvän datan koko viittaa tavujen määrään, ei bitcoinien määrään. "Korvaa maksulla" -toiminto on oletuksena päällä, ja se mahdollistaa transaktion uudelleenlähettämisen korkeammalla maksulla tarvittaessa. LockTime mahdollistaa transaktion voimassaoloajan säätämisen – en ole vielä kokeillut sitä, mutta neuvon olemaan käyttämättä sitä, ellet täysin ymmärrä mitä olet tekemässä ja ole harjoitellut pienillä määrillä.

Alaosassa meillä on joitakin hienoja kaivosmaksun säätötyökaluja. Kaiken mitä sinun tarvitsee tehdä sisäisissä siirroissa, on asettaa se minimimaksuksi 1 sat/byte. Kirjoita vain numero manuaalisesti Kohdemaksu-kenttään. Sopivan maksun tarkistamiseksi ulkoista maksua varten voit konsultoida https://mempool.space nähdäksesi, kuinka kiireinen mempool on, ja jotkin ehdotetut maksut näytetään.

![kuva](assets/41.webp)

Olen valinnut 1 sat/byte.

Syöttöikkunassa näemme kaksi merkintää. Ensimmäinen on 5000 sat lahjoitus. Näemme vasemmalla sen transaktiohashin (jonka voimme tarkistaa lohkoketjusta). Sen vieressä on "21" – tämä osoittaa, että se on kyseisen transaktion ulostulo numero 21 (se on itse asiassa 22. ulostulo, koska ensimmäinen on merkitty nollaksi).

Tässä on huomionarvoista: UTXO:t ovat olemassa vain transaktion sisällä. UTXO:n käyttämiseksi meidän on viitattava siihen ja laitettava se viite uuden transaktion syötteeseen. Ulostulot muuttuvat sitten uusiksi UTXO:iksi ja vanha UTXO muuttuu STXO:ksi (Käytetty transaktioulostulo).

Toinen rivi on 10 000 sat lahjoitus. Sen vieressä on "0" transaktiohashin vieressä, josta se on peräisin, koska se on kyseisen transaktion ensimmäinen (ja mahdollisesti ainoa) ulostulo.

Alaikkunassa näemme osoitteemme. Huomaa, että syötteiden bitcoinien kokonaismäärä ei aivan vastaa ulostulojen kokonaismäärää. Erotus menee kaivostyöläiselle. Kaivostyöläinen katsoo kaikkien lohkoa yrittäessään louhia olevien transaktioiden eroavaisuudet ja lisää sen numeron palkkioonsa. (Kaivosmaksut toimivat näin täysin irrallaan transaktioketjusta ja aloittavat uuden elämän).

Jos säädämme kaivosmaksua, ulostuloarvo muuttuu automaattisesti.

> On syytä huomauttaa tässä: Huomaa osoitteiden väri transaktioikkunassa. Muista, että vihreät osoitteet on lueteltu osoitevälilehdelläsi. Jos osoite on korostettu vihreänä (tai keltaisena) transaktioikkunassa, Electrum on tunnistanut osoitteen omakseen. Jos osoitteella ei ole korostusta, se on ulkoinen osoite (avoinna olevan lompakon ulkopuolella), ja sinun tulisi tarkistaa se erityisen huolellisesti.

Kun olet tarkistanut kaiken transaktiossa ja olet varma, että olet tyytyväinen siihen, mitä kolikoita käytät, ja minne kolikot menevät, voit klikata "finalise".

![kuva](assets/42.webp)

Kun olet klikannut "finalise", et voi enää tehdä muokkauksia – Jos tarvitset, sinun on suljettava tämä ja aloitettava alusta. Huomaa, että "finalise"-painike on vaihtunut "export"-painikkeeksi, ja uusia painikkeita on ilmestynyt: "save", "combine", "sign" ja "broadcast". "Broadcast"-painike on harmaana, koska transaktio on allekirjoittamaton ja siten tässä vaiheessa kelpaamaton.

Kun klikkaat allekirjoita, jos sinulla on lompakolle salasana, sinua pyydetään antamaan se, ja sitten tila (oikeassa yläkulmassa) muuttuu "Unsigned" (Allekirjoittamaton) -tilasta "Signed" (Allekirjoitettu) -tilaan. Sitten "Broadcast"-painike tulee käytettäväksi.
Kun olet lähettänyt viestin, voit sulkea tapahtumaikkunan. Jos menet osoitevälilehdelle, näet nyt, että ensimmäinen osoite on tyhjä ja toisessa osoitteessa on 1 UTXO.
Huomaa: Näet kaikki nämä muutokset jo ennen kuin tapahtuma on louhittu lohkoon eli "vahvistettu". Tämä johtuu siitä, että Electrum päivittää saldot/tapahtumat perustuen ei vain lohkoketjun tietoihin, vaan myös mempoolin tietoihin. Kaikki lompakot eivät tee näin.

Yksi huomionarvoinen seikka on, että lähettämisen sijaan voimme tallentaa tapahtuman myöhempää käyttöä varten. Sen voi tallentaa joko allekirjoittamattomana tai allekirjoitettuna.

Napsauta "export" painiketta (paradoksaalisesti, ÄLÄ napsauta "save" painiketta), ja näet useita vaihtoehtoja. Tapahtuma on koodattu tekstinä, ja sen vuoksi sen voi tallentaa monella tavalla.

![kuva](assets/43.webp)

Tallentaminen QR-koodina on erittäin mielenkiintoista. Jos valitset tämän, QR-koodi ilmestyy:

![kuva](assets/44.webp)

Voit sitten ottaa kuvan QR-koodista. Tämän kanssa voi tehdä monia asioita, mutta toistaiseksi sanotaan, että lataat sen myöhemmin takaisin lompakkoon. Voit sulkea Electrumin, ladata lompakon uudelleen ja mennä valikkoon Työkalut:

![kuva](assets/45.webp)

Tämä lataa tietokoneesi kameran. Näytät sitten kameran edessä puhelimesi kuvan QR-koodista, ja tämä lataa tapahtuman takaisin juuri sellaisena kuin jätit sen.

Tallennettujen tapahtumien lataaminen ei ole intuitiivista, joten ota erityisesti huomioon. Tapahtuman lataaminen ei ole "työkalu", vaan vaihtoehto on piilotettu työkaluvalikkoon (toinen asia, jonka Electrum-kehittäjien tulisi korjata).

Samankaltainen prosessi on mahdollinen myös tiedostona tallennetun tapahtuman kanssa. Kokeile harjoitella kummallakin menetelmällä samassa lompakossa. En käy läpi sitä tässä, mutta voit käyttää tätä toimintoa siirtääksesi tapahtumia saman lompakon eri tietokoneiden välillä, multisignature-lompakoiden välillä ja laitteistolompakoihin ja niistä pois. Tässä on joitakin ohjeita.

Palatakseni nyt "save" painikkeeseen – tämä ei ole tapa tallentaa tapahtuman tekstiä. Mitä tämä todellisuudessa tekee, on käskee Electrum-lompakkoa tunnistamaan tämän tapahtuman paikallisella tietokoneella maksettuna maksuna. Jos teet tämän vahingossa, näet tapahtuman pienen tietokoneikonin kanssa. Voit napsauttaa oikealla ja poistaa tapahtuman – älä huoli, et voi tällä tavalla poistaa bitcoineja. Electrum unohtaa sitten, että tämä tapahtuma on koskaan tapahtunut, ja "palauttaa" satoshit takaisin ja näyttää satoshit oikeassa paikassa, missä ne todellisuudessa ovat.

### Vaihto-osoitteet

Vaihto-osoitteet ovat mielenkiintoisia. Sinun on ymmärrettävä UTXO:t ymmärtääksesi tämän selityksen. Jos lähetät osoitteeseen summan, joka on pienempi kuin UTXO, jäljelle jäävä bitcoin menee louhijalle, ellei vaihtotulostetta ole määritelty.

Sinulla saattaa olla 6.15 bitcoinin UTXO ja haluat käyttää 0.15 bitcoinia lahjoittaaksesi joillekin sortoa vastustaville mielenosoittajille tyrannisen "demokraattisen" hallituksen alla jossain päin maailmaa. Ottaisit silloin 6.15 bitcoinia (käyttäen "spend from" toimintoa Electrumissa), ja laittaisit sen tapahtumaan.

Liittäisit mielenosoittajien osoitteen "pay to" kenttään, ehkä laittaisit "EndTheFed & WEF" "description" kenttään, ja summan kohdalle laittaisit 0.15 bitcoinia ja klikkaisit "pay", sitten "advanced".
Siirtoikkunassa, syöttöikkunassa, näet 6.15 bitcoinin UTXO:n. Lähtöikkunassa näet osoitteen, jossa ei ole korostusta (tämä on protestoijien osoite) 0.15 bitcoinin kanssa vieressään. Näet myös keltaisen osoitteen, jossa on hieman alle 6.0 bitcoinia. Tämä on vaihto-osoite, jonka lompakko on automaattisesti valinnut yhdestä omista keltaisista vaihto-osoitteistaan. Vaihto-osoitteen tarkoitus on, että lompakko voi laittaa vaihtorahat niihin sotkematta vastaanotto-osoitteiden saatavuutta, joille saatat olla suunnitellut käyttöä, tai lähettänyt laskuja. Jos niitä tullaan käyttämään myöhemmin asiakkaiden toimesta, esimerkiksi, et halua lompakkosi automaattisesti käyttävän niitä ja täyttävän niitä. Se on sotkuista ja huonoa yksityisyyden kannalta.
Huomaa, että kun säädät louhintapalkkiota, vaihtorahan määrä säätää automaattisesti, ei maksun määrä.

### Manuaalinen vaihto tai maksu monille

Tämä on todella mielenkiintoinen Electrumin ominaisuus. Pääset siihen näin.

![kuva](assets/46.webp)

Voit sitten syöttää useita kohteita UTXO-saldolle, jonka olet käyttämässä, näin:

![kuva](assets/47.webp)

Liitä osoite, kirjoita pilkku, sitten välilyönti, sitten määrä, sitten <enter>, ja tee se uudelleen. ÄLÄ SYÖTÄ MÄÄRIÄ “MÄÄRÄ”-IKKUNOIHIN – Electrum täyttää kokonaismäärän tähän, kun kirjoitat yksittäiset määrät “Maksa”-ikkunaan.

Tämä mahdollistaa manuaalisen määrittelyn, minne vaihtoraha menee (esim. tietty osoite lompakossasi tai toiseen lompakkoon), tai voit maksaa monille ihmisille kerralla. Jos kokonaismääräsi ei ole tarpeeksi suuri vastaamaan UTXO:n kokoa, Electrum luo silti lisävaihtorahan ulostulon sinulle.

Maksa monille -ominaisuus mahdollistaa myös oman “PayJoins” tai “CoinJoins” luomisen – tämän artikkelin ulkopuolella, mutta minulla on opas täällä. (https://armantheparman.com/cj/)

## Lompakot

Haluan esitellä Vain katselu -lompakon käyttämällä Electrumia. Tehdäkseni sen, minun täytyy ensin määritellä “lompakko”. Bitcoinissa “lompakko”-sanaa käytetään kahdella tavalla:

- Tyyppi A, “lompakko” – viittaa ohjelmistoon, joka näyttää sinulle osoitteesi ja saldosi, esim. Electrum, Blue Wallet, Sparrow Wallet jne.

- Tyyppi B, “lompakko” – viittaa ainutlaatuiseen osoitekokoelmaan, joka on yhdistetty siemenlauseesi/salasanasi/johdatuspolkusi yhdistelmään. Missä tahansa lompakossa on 8,6 miljardia osoitetta (4,3 miljardia vastaanotto-osoitetta ja 4,3 miljardia vaihto-osoitetta). Jos muutat mitään siemenlauseessa, salasanassa tai johdatuspolussa, saat käyttämättömän lompakon uusilla, kaikki ainutlaatuisilla, 8,6 miljardilla tyhjällä osoitteella.

Kumpaa tyyppiä kuka tahansa tarkoittaa käyttäessään sanaa “lompakko”, on ilmeistä kontekstista.

## Vain katselu -lompakko – harjoitus

Ei ole täysin ilmeistä, mihin vain katselu -lompakkoa käytetään, mutta aloitan selittämällä, mikä se on, miten tehdä harjoitusyksi, ja palaamme sen tarkoitukseen myöhemmin, kun selitän enemmän laitteistolompakoista. (Syvällisempää tarkastelua laitteistolompakon käytöstä ja eri merkeistä, katso täältä.)
Aiomme luoda kuvitteellisen tavallisen lompakon (tällä kertaa lisäten hieman monimutkaisuutta salasanalla), ja sitten vastaavan seurantalompakon. Halutessasi voit kopioida juuri sellaisen, jonka itse tein, tai luoda oman – tämä lompakko on tarkoitettu hylättäväksi; älä oikeasti käytä sitä. Aloita luomalla 12 sanan siemen Ian Colemanin verkkosivustolla.

Huomaa alla olevassa kuvakaappauksessa 12 satunnaista sanaa, ja että olen syöttänyt salasanan salasana-kenttään:

SALASANA: “Craig Wright on valehtelija ja huijari ja kuuluu vankilaan. Lisäksi, Ross Ulbricht tulisi vapauttaa vankilasta välittömästi.”

Salasana voi olla jopa 100 merkkiä pitkä, ja ihanteellisesti sen tulisi olla yksiselitteinen eikä liian lyhyt – Käyttämäni on vain huvin vuoksi – Yleensä suosittelen välttämään isoja kirjaimia ja symboleita vain stressin vähentämiseksi, jos koskaan unohdat salasanasi.

![kuva](assets/48.webp)

Seuraavaksi, Electrumissa, mene valikkoon tiedosto–>uusi/palauta. Kirjoita uniikki nimi luodaksesi uuden lompakon ja klikkaa “seuraava”.

![kuva](assets/49.webp)

Seuraavat askeleet ovat sinulle jo tuttuja, joten listaan ne ilman kuvia:

- Tavallinen lompakko
- Minulla on jo siemen
- Kopioi ja liitä 12 sanaa ruutuun, tai kirjoita ne käsin.
- Klikkaa asetukset ja valitse BIP39, ja klikkaa myös salasanan valintaruutu (“laajenna tätä siementä mukautetuilla sanoilla”)
- Syötä salasanasi täsmälleen kuten teit Ian Colemanin sivulla
- Jätä oletusskriptin semantiikka ja johdannaispolku
- Ei tarvetta lisätä salasanaa (lukitsee lompakon)

Palaa nyt Ian Colemanin sivustolle, alas “johdannaispolku”-osioon, ja klikkaa “BIP 84”-välilehteä valitaksesi saman skriptin semantiikan kuin Electrumin oletusarvot (Native Segwit).

![kuva](assets/50.webp)

Laajennetut yksityiset ja julkiset avaimet ovat juuri alla, ja ne muuttuvat, kun teet muutoksia johdannaispolkuun (tai mihin tahansa muuhun ylempänä sivulla).

![kuva](assets/51.webp)

Näet myös “BIP32 laajennetut yksityiset/julkiset” avaimet – näitä ei huomioida nyt.

Tilin laajennettua yksityistä avainta voidaan käyttää lompakkosi täydelliseen uudelleenluomiseen. Tilin laajennettu julkinen avain voi kuitenkin tuottaa vain rajoitetun version samasta lompakosta (seurantalompakko) – Jos laitat tämän avaimen Electrumiin, se tuottaa silti kaikki 8,6 miljardia osoitetta, jotka siemen tai laajennettu yksityinen avain olisi tuottanut, mutta Electrumille ei ole saatavilla yksityisiä avaimia, joten maksujen suorittaminen ei ole mahdollista. Tehdään se nyt havainnollistaaksemme asiaa:

Kopioi “tilin laajennettu julkinen avain” leikepöydälle.

Mene sitten Electrumiin, jätä nykyinen tekemämme lompakko auki, ja mene tiedosto–>uusi/palauta. Lompakon tekoprosessi on hieman erilainen kuin aiemmin:

- Tavallinen lompakko
- Käytä pääavainta
- Liitä laajennettu julkinen avain ruutuun ja jatka
- Ei tarvetta syöttää salasanaa; se on jo osa laajennettua julkista avainta
- Ei tarvetta syöttää skriptin semantiikkaa ja johdannaispolkua
- Ei tarvetta lisätä salasanaa (lukitsee lompakon)

Kun lompakko latautuu, sinun pitäisi huomata, että täsmälleen samat osoitteet latautuvat kuin aiemmin, kun siemen syötettiin. Sinun pitäisi myös huomata otsikkopalkissa yläreunassa, että siinä sanotaan “seurantalompakko”. Tämä lompakko voi näyttää sinulle osoitteesi ja saldosi (tarkistamalla saldot solmun kautta), mutta et pysty ALLEKIRJOITTAMAAN transaktioita (koska seurantalompakolla ei ole yksityisiä avaimia).
Mikä siis on sen tarkoitus?
Yksi syy, eikä suinkaan päasyy, on se, että voit mahdollisesti tarkkailla lompakkoasi ja sen saldoa tietokoneella paljastamatta yksityisiä avaimiasi mahdolliselle tietokoneen haittaohjelmalle.

Toinen syy on, että se on VAADITTU maksujen tekemiseen, jos päätät pitää yksityiset avaimet pois tietokoneelta; selitän:

> Laitelompakot (HWW) luotiin, jotta laite voi turvallisesti säilyttää yksityiset avaimet (suojattuna PIN-koodilla), olematta paljastamatta avaimia tietokoneelle (jopa kun se on yhdistetty tietokoneeseen kaapelilla), eivätkä ne itse kykene muodostamaan yhteyttä internetiin. Tällainen laite ei voi tehdä transaktioita itsenäisesti, koska kaikki bitcoin-transaktiot alkavat viittaamalla UTXO(s) lohkoketjussa (joka on nodessa). Lompakon on määriteltävä, missä transaktio-ID:ssä UTXO on, ja mikä transaktion ulostulo on käytettävä. Vasta ulostulon määrittelyn jälkeen uusi transaktio voidaan luoda alun perin, saati allekirjoittaa. Laitelompakot eivät voi luoda transaktioita, koska niillä ei ole pääsyä mihinkään UTXOihin – ne eivät ole yhteydessä mihinkään! Laajennettu julkinen avain yleensä poimitaan HWW:stä, ja osoitteet näytetään sitten tietokoneella – monet ihmiset tuntevat Ledger-ohjelmiston tai Trezor Suiten, jotka näyttävät osoitteita ja saldoja tietokoneellaan – tämä on seuraavalompakko. Nämä ohjelmat voivat luoda transaktioita, mutta ne eivät voi allekirjoittaa. Ne voivat ainoastaan saada transaktiot allekirjoitettua HWW:llä, joka on yhdistetty niihin. HWW ottaa vastaan uuden transaktion seuraavalompakosta, allekirjoittaa sen ja lähettää sen takaisin tietokoneelle lähetettäväksi nodeen. HWW ei voi lähettää itse, sen liitännäinen seuraavalompakko tekee sen. Näin kaksi lompakkoa (julkinen avainlompakko tietokoneella ja yksityinen avainlompakko HWW:ssä) tekevät yhteistyötä luodakseen, allekirjoittaakseen ja lähettääkseen, samalla varmistaen, että yksityiset avaimet pysyvät erillään ja poissa internetiin yhdistetystä laitteesta.

## Osittain Allekirjoitetut Bitcoin Transaktiot (PSBT)

On mahdollista, että transaktio luodaan ja tallennetaan tiedostoon, myöhemmin ladattu uudelleen, allekirjoitettu, tallennettu, myöhemmin ladattu uudelleen ja lopulta lähetetty – en sano, että kukaan tarvitsisi tehdä näin; se on vain jotain, mikä on mahdollista.

Harkitse 3 viidestä moniallekirjoituslompakkoa – viisi yksityistä avainta luo lompakon, ja kolmea tarvitaan transaktion täydelliseen allekirjoittamiseen (Katso täältä lisätietoja moniallekirjoituslompakon avaimista). On mahdollista, että viidellä eri tietokoneella on kukin yksi viidestä yksityisestä avaimesta.

Tietokone yksi voisi luoda transaktion ja allekirjoittaa sen. Se voisi sitten tallentaa sen tiedostoon ja lähettää sen sähköpostitse Tietokoneelle 2. Tietokone 2 voi sitten allekirjoittaa, ja mahdollisesti tallentaa tiedoston QR-koodiin, ja lähettää QR:n Zoom-puhelun kautta Tietokoneelle 3 toisella puolella maailmaa. Tietokone 3 voi kaapata QR:n, ladata transaktion electrumiin ja allekirjoittaa transaktion. Ensimmäisten kahden allekirjoituksen jälkeen transaktio oli PSBT (osittain allekirjoitettu bitcoin transaktio). Kolmannen allekirjoituksen jälkeen transaktio oli täysin allekirjoitettu ja voimassa, valmis lähetettäväksi.

Lisätietoja PSBT:stä, katso tämä opas. (https://armantheparman.com/psbt/)

## Laitelompakoiden käyttö Electrumin kanssa

Minulla on opas yleisesti laitelompakoiden käytöstä, jonka lukemisen uskon olevan tärkeää ihmisille, jotka ovat uusia HWW:ien kanssa. (https://armantheparman.com/using-hwws/)
Löydät myös oppaita eri merkkisten HWW-laitteiden yhdistämisestä Sparrow Bitcoin Walletiin täältä. (https://armantheparman.com/hwws/)
Tämä on ensimmäinen oppaani, jossa näytän, miten käyttää laitteistolompakkoa Electrumin kanssa – aion käyttää ColdCard-laitteistolompakkoa esimerkkinä. Tämä ei ole tarkoitettu yksityiskohtaiseksi oppaaksi ColdCardista itsestään, se opas löytyy täältä. Esittelen vain Electrumiin liittyviä seikkoja. (https://armantheparman.com/cc/)

### Yhdistäminen micro SD -kortin kautta (ilma-aukkoyhteys)

Ennen kuin yhdistät oikean lompakkosi ColdCardin kautta, toivon, että olet suorittanut aiemmat vaiheet, jotka sisältävät Electrumin harjoituslompakon lataamisen ja verkon parametrien asettamisen.

Sen jälkeen, kun olet ColdCardissa, aseta SD-kortti paikalleen. Oletan, että olet jo luonut siemenesi. Jos käytät lompakkoa salasanalla, käytä sitä nyt. Vieritä alas ja valitse valikosta Advanced/Tools –> Export Wallet –> Electrum Wallet.

Voit vierittää alas ja lukea viestin. Se tarjoaa aina mahdollisuuden valita “1” syöttääksesi ei-nollan tilinumeron (jotain, mikä kuuluu johdannaispolkuun), mutta jos olet noudattanut neuvoani, et ole sekaantunut oletusjohdannaispolkuihin, joten et halua ei-nollan tilinumeroa; paina vain valintamerkkiä jatkaaksesi.

Valitse sitten skriptin semantiikka. Useimmat ihmiset valitsevat “Native Segwit”.

Näyttöön tulee “Electrum wallet file written”, ja se näyttää tiedoston nimen. Tee siitä henkinen muistiinpano.

Ota sitten micro SD -kortti ulos ja laita se tietokoneeseen, jossa on Electrum.

Jotkut käyttöjärjestelmät avaa automaattisesti tiedostonhallinnan, kun asetat microSD:n. Monet ihmiset näkevät uuden lompakkotiedoston ja kaksoisklikkaavat sitä, ihmetellen miksi se ei toimi. Se ei ole kovin hyvä suunnittelu. Sinun täytyy itse asiassa jättää tiedostonhallinta huomiotta (sulje se) ja avata lompakkotiedosto käyttäen Electrumia:

Avaa Electrum. Jos se on jo avoinna jonkin toisen lompakon kanssa, valitse tiedosto –> uusi. Etsimme tätä ikkunaa:

![kuva](assets/52.webp)

Tässä on niksi, se ei ole intuitiivinen. Klikkaa “valitse”. Navigoi sitten tiedostojärjestelmässä microSD-kortilla ja löydä lompakkotiedosto ja avaa se.

Nyt olet avannut laitteistolompakkoasi vastaavan seurantalompakon. Hienoa.

### Yhdistäminen USB-kaapelin kautta.

Tämän pitäisi olla helpompaa, mutta Linux-tietokoneilla se on paljon vaikeampaa. Tarvitaan jotain, jota kutsutaan “Udev-säännöiksi” päivitettäväksi. Näin se tapahtuu (yksityiskohtainen opas https://armantheparman.com/gpg-articles/ ), ja lyhyesti:

On hyvä idea varmistaa, että järjestelmä on ajan tasalla. Sitten:

```bash
sudo apt-get install libusb-1.0-0-dev libudev-dev
```

sitten...

```bash
python3 -m pip install ckcc-protocol
```

Jos saat virheilmoituksen, varmista että pip on asennettu. Voit tarkistaa sen komennolla (pip –version), ja voit asentaa sen komennolla (sudo apt install python3-pip)

Luo tai muokkaa olemassa olevaa tiedostoa, /etc/udev/rules.d/

Näin:

```bash
sudo nano /etc/udev/rules.d
```

Tekstieditori avautuu. Kopioi teksti täältä ja liitä se rules.d-tiedostoon, tallenna ja poistu.

![kuva](assets/53.webp)

Suorita sitten nämä komennot peräkkäin:

```bash
sudo groupadd plugdev
sudo usermod -aG plugdev $(whoami)
sudo udevadm control –reload-rules && sudo udevadm trigger
```
Jos saat viestin "ryhmä plugdev on jo olemassa", se on kunnossa, jatka. Toisen komennon jälkeen et saa palautetta/vastausta, jatka vain kolmanteen komentoon.
Saatat joutua irrottamaan ColdCardin tietokoneesta ja yhdistämään sen uudelleen.

Jos kaiken tämän jälkeen et edelleenkään pysty yhdistämään ColdCardia, yrittäisin päivittää laiteohjelmiston (opas tulossa, mutta toistaiseksi löydät ohjeet valmistajan verkkosivustolta).

Seuraavaksi, luo uusi lompakko:

- Tavallinen lompakko
- Käytä laitteistolaite
- Se skannaa ja tunnistaa ColdCardisi. Jatka.
- Valitse skriptin semantiikka ja johdannaispolku
- Päätä, tulisiko lompakkotiedoston olla salattu (suositeltavaa)

### Transaktiot käyttäen ColdCardia

Kaapelin ollessa yhdistettynä, transaktiot ovat helppoja. Transaktioiden allekirjoittaminen on saumatonta.

Jos käytät laitetta ilman verkkoyhteyttä, sinun täytyy manuaalisesti siirtää tallennettu transaktio laitteiden välillä käyttäen microSD-korttia. On joitakin niksejä.

Transaktion luomisen ja viimeistelyn jälkeen sinun on napsautettava vientipainiketta vasemmassa alakulmassa. Näet "tallenna tiedostoon", mikä vastoin intuitiota, ei ole se mitä haluamme. Sinun on itse asiassa ensin mentävä aivan viimeiseen valikkovaihtoehtoon, joka sanoo "laitteistolompakoille", ja sitten, sen valinnan sisällä, löydä toinen "tallenna tiedostoon" ja valitse se. Tallenna sitten tiedosto microSD-kortille, ota kortti ulos ja laita se ColdCardiin. Muista, että saatat joutua käyttämään salasanaa valitaksesi oikean lompakon. Näyttö sanoo valmis allekirjoitettavaksi. Napsauta valintamerkkiä, tarkastele transaktiota ja jatka vahvistamalla valintamerkillä. Kun olet valmis, ota kortti ulos ja laita se takaisin tietokoneeseen.

Sitten meidän on avattava transaktio käyttäen Electrumia. Toiminto on piilotettu valikkoon työkalut –> lataa transaktio. Navigoi tiedostojärjestelmässä ja löydä tiedosto. Joka kerta kun allekirjoitat, tulee kolme tiedostoa. Alkuperäinen tallennettu tiedosto, jonka Watching Wallet teki, ja kaksi, jotka ColdCard teki (en tiedä miksi se tekee näin). Yksi sanoo "allekirjoitettu" ja toinen sanoo "loppullinen". Se ei ole intuitiivista, mutta "allekirjoitettu" ei ole hyödyllinen, meidän on avattava "loppullinen" transaktio.

Kun olet ladannut sen, voit napsauttaa "lähetä" ja maksu suoritetaan.

## Electrumin päivittäminen ja piilotettu ".electrum"-hakemisto

Electrum elää tietokoneellasi kahdessa paikassa. On itse sovellus, ja on piilotettu konfiguraatiohakemisto. Tämä hakemisto sijaitsee eri paikoissa riippuen käyttöjärjestelmästäsi:

Windows:

> C:/Users/käyttäjänimesi_tähän/AppData/Roaming/Electrum

Mac:

> /Users/käyttäjänimesi_tähän/.electrum

Linux:

> /home/käyttäjänimesi_tähän/.electrum

Huomaa, että "." ennen "electrum" Linuxissa ja Macissa – se osoittaa, että hakemisto on piilotettu. Huomaa myös, että tämä hakemisto luodaan (automaattisesti) vasta kun käynnistät Electrumin ensimmäisen kerran. Hakemisto sisältää Electrumin konfiguraatiotiedoston sekä myös hakemiston, joka pitää sisällään kaikki tallentamasi lompakot.

Jos poistat Electrumin ohjelman tietokoneeltasi, piilotettu hakemisto pysyy, ellet aktiivisesti poista sitä myös.
Electrumin päivittäminen tapahtuu samalla menetelmällä kuin alussa kuvasin lataamisen ja varmentamisen osalta. Tämän jälkeen tietokoneellasi on kaksi ohjelmakopiota, ja voit ajaa kumpaa tahansa – kumpikin ohjelma käyttää samaa piilotettua Electrum-kansiota konfiguraationsa ja lompakon pääsyn osalta. Kaikki tallentamamme asiat, kuten perusyksikkö, oletusyhteyspiste, muut asetukset ja pääsy lompakoihin, säilyvät, koska kaikki tämä tallennetaan kyseiseen kansioon.
### Electrumin ja lompakoiden siirtäminen toiselle tietokoneelle

Tämän tekemiseksi voit kopioida ohjelmatiedostot USB-asemalle ja myös kopioida .electrum-kansion. Kopioi tai siirrä ne sitten uudelle tietokoneelle. Sinun ei tarvitse varmentaa ohjelmaa uudelleen. Varmista, että kopioit .electrum-kansion oletussijaintiin (muista kopioida se ENNEN Electrumin ensimmäistä käynnistystä kyseisellä tietokoneella, muuten tyhjä oletus .electrum-kansio täytetään, ja saatat hämmentyä).

## Tunnisteet

Kuten aiemmin selitin, osoitevälilehdellä on tunnistespalta. Voit kaksoisnapsauttaa siellä ja kirjoittaa itsellesi muistiinpanoja (ne ovat vain tietokoneellasi, eivät julkisia eivätkä lohkoketjussa).

![kuva](assets/54.webp)

Siirtäessäsi Electrum-lompakkoasi toiselle tietokoneelle, saatat haluta säilyttää kaikki nämä muistiinpanot. Voit varmuuskopioida ne tiedostoon valikon kautta, lompakko–> tunnisteet –> vie, ja sitten uudella tietokoneella, käytä lompakko–>tunnisteet–>tuo.

## Vinkkejä:

Jos pidät tätä resurssia hyödyllisenä ja haluaisit tukea sitä, mitä teen Bitcoinin eteen, voit lahjoittaa joitakin satseja täällä:

Staattinen Lightning-osoite: dandysack84@walletofsatoshi.com
https://armantheparman.com/electrum/