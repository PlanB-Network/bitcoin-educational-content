---
name: Bitcoin Core -solmu (mac & windows)
description: Asenna Bitcoin Core Macille tai Windowsille
---

Bitcoin Coren asentaminen tavalliselle tietokoneelle on mahdollista, mutta se ei ole ihanteellista. Jos et pane pahaksesi tietokoneesi jättämistä päälle 24/7, silloin tämä toimii hyvin. Jos tarvitset sammuttaa tietokoneen, ohjelmiston synkronoinnin odottaminen joka kerta kun käynnistät sen uudelleen, voi olla ärsyttävää.

Nämä ohjeet ovat Macin tai Windowsin käyttäjille. Linuxin käyttäjät eivät todennäköisesti tarvitse apuani, mutta Linuxille ohjeet ovat hyvin samankaltaiset kuin Macille.

## Aloita puhtaalta pöydältä

Ihanteellisesti haluat käyttää puhdasta tietokonetta, yhtä ilman haittaohjelmia. Vaikka käyttäisit laitteistolompakkoa, haittaohjelmat voivat huijata sinut eroon kolikoistasi.

Voit joko pyyhkiä vanhan tietokoneen puhtaaksi ja käyttää sitä omistautuneena Bitcoin-tietokoneena, tai ostaa omistautuneen tietokoneen/läppärin.

## Kovalevy

Bitcoin Core vie noin 400 gigatavua dataa levytilastasi ja jatkaa kasvamistaan. Voit käyttää sisäistä asemaasi, mutta voit myös liittää ulkoisen kovalevyn. Selitän molemmat vaihtoehdot. Ihanteellisesti sinun tulisi käyttää kiintolevyä (SSD). Jos sinulla on vanha tietokone, siinä todennäköisesti ei ole tällaista sisäisesti. Osta vain 1 tai 2 teratavun ulkoinen SSD ja käytä sitä. Tavallinen asema todennäköisesti toimii, mutta saatat kohdata ongelmia ja se on paljon hitaampi.

![kuva](assets/1.webp)

## Lataa Bitcoin Core

Mene osoitteeseen bitcoin.org (varmista, ettet mene osoitteeseen bitcoin.com, joka on shitcoin-sivusto, jonka omistaa Roger Ver, huijaten ihmisiä ostamaan Bitcoin Cashia Bitcoinin sijaan)

Kun olet siellä, ei ole oudosti ilmeistä, mistä saa ohjelmiston. Mene resurssivalikkoon ja klikkaa "Bitcoin Core", kuten alla näytetään:

![kuva](assets/2.webp)

Tämä vie sinut lataussivulle:

![kuva](assets/3.webp)

Klikkaa Lataa Bitcoin Core -oranssia painiketta:

![kuva](assets/4.webp)

Valittavanasi on useita vaihtoehtoja riippuen tietokoneestasi. Ensimmäiset kaksi ovat relevantteja tähän oppaaseen; valitse vasemmalta palkista Windows tai Mac. Lataus alkaa klikkaamisen jälkeen, todennäköisesti Lataukset-kansioosi.

## Vahvista lataus (osa 1)

Tarvitset tiedoston, joka sisältää eri julkaisujen hashit. Tämä tiedosto oli aiemmin bitcoin.org:n lataussivulla, mutta on nyt siirtynyt osoitteeseen bitcoincore.org/en/download:

![kuva](assets/5.webp)

Tarvitset SHA256 binäärihashien tiedoston. Tämä tiedosto sisältää Bitcoin Coren eri latauspakettien SHA256-hashit.

Seuraavaksi meidän täytyy hashata Bitcoin Core -lataus ja verrata sitä siihen, mitä tiedostossa sanotaan hashin olevan. Silloin tiedämme latauksen olevan identtinen odotetun mukaisesti, bitcoincore.org:n mukaan.

Siirry uudelleen Lataukset-kansioon ja suorita tämä komento (korvaa X:t tarkalla Bitcoin-solmun lataustiedoston nimellä):

```bash
shasum -a 256 XXXXXXXXXXXX # <--- MACILLE
certutil -hashfile XXXXXXXXXXX SHA256 # <--- WINDOWSILLE
```

Saat hash-tulosteen. Tee siitä muistiinpano ja vertaa sitä SHA256SUMS-tiedostossa olevaan hashiin.

Jos tulosteet ovat identtiset, olet vahvistanut, että yksikään bitti tiedoista ei ole muutettu... melkein. Meidän on vielä varmistettava, ettei SHA256SUMS-tiedosto ole pahantahtoinen.

Jatkaaksemme seuraavaan vaiheeseen, meillä täytyy olla gpg asennettuna tietokoneellemme.
Tehdäksesi tämän, katso SHA256/gpg-opas ja vieritä noin puoliväliin kohtaan "Download gpg" ja etsi käyttöjärjestelmäsi alaotsikko. Palaa sitten tänne.
## Hanki julkinen avain

Takaisin lataussivulla, hanki SHA256 hash allekirjoitustiedosto

![kuva](assets/6.webp)

Klikkaa sitä ja tallenna tiedosto levylle, mieluiten Lataukset-kansioon.

Tämä tiedosto sisältää eri ihmisten allekirjoituksia SHA256SUMS-tiedostosta.

Haluamme pääkehittäjän julkisen avaimen, Wladimir J. van der Laanin, tietokoneemme avainnippuun. Hänen julkisen avaimensa ID on:
1 - 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964

Kopioi tuo teksti seuraavaan komentoon:

```bash
gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 01EA5486DE18A882D4C2684590C8019E36C2E964
```

Kiinnostuksen vuoksi, milloin tahansa, voit nähdä, mitä avaimia on tietokoneen avainnipussa tällä komennolla:

```bash
gpg --list-keys
```

## Vahvista lataus (osa 2)

Meillä on julkinen avain, joten voimme nyt vahvistaa SHA256SUMS-tiedoston, joka sisältää Bitcoin Core -latauksen hashit ja näiden hashien allekirjoituksen.

Avaa Terminaali tai CMD uudelleen ja varmista, että olet Lataukset-kansiossa. Sieltä suorita tämä komento:

```bash
gpg –verify SHA256SUMS.asc SHA256SUMS
```

Ensimmäinen listattu tiedosto on allekirjoitustiedoston tarkka kirjoitusasu. Toinen listattu tiedosto pitäisi olla tarkka kirjoitusasu tekstiedostosta, joka sisältää hashit. Molempien tiedostojen tulisi olla samassa hakemistossa ja sinun on oltava tiedostojen hakemistossa, muuten sinun on kirjoitettava koko polku kummallekin tiedostolle.

Tämä on tuloste, jonka pitäisi tulla

![kuva](assets/7.webp)

VAROITUS-viestin voi jättää huomiotta – se vain muistuttaa, että et ole tavannut Wladimiria avainosassa henkilökohtaisesti ja kysynyt häneltä, mikä hänen julkinen avaimensa on, ja sitten kertonut tietokoneellesi luottamaan tähän avaimen täysin.

Jos sait tämän viestin, tiedät nyt, että SHA256SUMS.asc-tiedostoa ei ole manipuloitu sen jälkeen, kun Wladimir allekirjoitti sen.

## Asenna Bitcoin Core

Sinun ei pitäisi tarvita yksityiskohtaisia ohjeita ohjelman asentamiseen.

![kuva](assets/8.webp)

## Käynnistä Bitcoin Core

Macilla saatat saada varoituksen (Apple on edelleen anti-Bitcoin)

![kuva](assets/9.webp)

Klikkaa OK ja avaa sitten Järjestelmäasetukset

![kuva](assets/10.webp)

Klikkaa Turvallisuus ja yksityisyys -kuvaketta:

![kuva](assets/11.webp)

Klikkaa sitten "avaa joka tapauksessa":

![kuva](assets/12.webp)

Virhe ilmestyy uudelleen, mutta tällä kertaa sinulla on käytettävissä AVAA-painike. Klikkaa sitä.

![kuva](assets/13.webp)

Bitcoin Coren pitäisi latautua ja sinulle esitetään joitakin vaihtoehtoja:

![kuva](assets/14.webp)

Tässä voit valita käyttääkö oletusreittiä, johon lohkoketju ladataan, vai voit valita ulkoisen aseman. Suosittelen, että et muuta oletuspolkua, jos aiot käyttää sisäistä asemaa, se tekee asioista helpompia asennettaessa muita ohjelmistoja kommunikoimaan Bitcoin Coren kanssa.
Voit päättää käyttää karsittua solmua, mikä säästää tilaa, mutta rajoittaa sitä, mitä voit tehdä solmullasi. Joka tapauksessa lataat koko lohkoketjun ja varmistat sen, joten jos sinulla on tilaa, säilytä ladattu aineisto äläkä karsi, jos voit välttää sen.
Kun vahvistat, lohkoketju alkaa ladata. Sen lataaminen kestää monta päivää.

![kuva](assets/15.webp)

Voit sammuttaa tietokoneen ja palata lataamaan halutessasi, se ei aiheuta vahinkoa.