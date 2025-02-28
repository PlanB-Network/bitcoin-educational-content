---
name: Boltzmann Calculator
description: Ymmärrä entropian käsite ja miten käyttää Boltzmannia
---
![kansi](assets/cover.webp)

***VAROITUS:** Samourai Walletin perustajien pidätyksen ja heidän palvelimiensa takavarikoinnin jälkeen 24. huhtikuuta KYCP.org-verkkosivusto on tällä hetkellä saavuttamattomissa. Myös Python Boltzmann-laskimen koodia isännöivä Gitlab on takavarikoitu. Tällä hetkellä työkalun lataaminen ei ole mahdollista. On kuitenkin mahdollista, että koodi voidaan julkaista uudelleen muiden toimesta tulevina viikkoina. Sillä välin voit hyötyä tästä oppaasta ymmärtääksesi Boltzmann-laskimen toimintaa. Tämän työkalun tarjoamat indikaattorit ovat sovellettavissa mihin tahansa Bitcoin-siirtoon ja ne voidaan myös laskea manuaalisesti. Tarjoan kaikki tarvittavat laskelmat tässä oppaassa. Jos olit jo ladannut Python-työkalun koneellesi tai käytät RoninDojoa, voit jatkaa työkalun käyttöä ja seurata tätä opasta kuten tavallisesti, se toimii edelleen.*

_Seuraamme tiiviisti tämän tapauksen kehitystä sekä siihen liittyvien työkalujen kehitystä. Voit olla varma, että päivitämme tämän oppaan, kun uutta tietoa tulee saataville._

_Tämä opas on tarkoitettu vain koulutus- ja tiedotustarkoituksiin. Emme tue tai kannusta näiden työkalujen käyttöä rikollisiin tarkoituksiin. Jokaisen käyttäjän on noudatettava oman lainkäyttöalueensa lakeja._

---

Boltzmann-laskin on työkalu Bitcoin-siirron analysointiin mittaamalla sen entropiatasoa sekä muita edistyneitä metriikoita. Se tarjoaa näkemyksiä siirron sisääntulojen ja ulostulojen välisistä yhteyksistä. Nämä indikaattorit tarjoavat kvantifioidun arvion siirron yksityisyydestä ja auttavat tunnistamaan mahdolliset virheet.

Tämän Python-työkalun kehittivät Samourai Walletin ja OXT:n tiimit, mutta sitä voidaan käyttää minkä tahansa Bitcoin-siirron analysointiin.

## Miten käyttää Boltzmann-laskinta?
Boltzmann-laskimen käyttämiseen on kaksi vaihtoehtoa. Ensimmäinen on asentaa Python-työkalu suoraan koneellesi. Vaihtoehtoisesti voit käyttää KYCP.org-sivustoa (_Know Your Coin Privacy_), joka tarjoaa yksinkertaistetun käyttöalustan. RoninDojo-käyttäjille huomioikaa, että tämä työkalu on jo integroitu solmuunne.

KYCP-sivuston käyttö on melko helppoa: syötä vain analysoitavan siirron tunniste (TXID) hakupalkkiin ja paina `ENTER`.
![KYCP](assets/1.webp)
Tämän jälkeen löydät eri tietoja siirrosta, mukaan lukien sisääntulojen ja ulostulojen väliset linkit. Klikkaa `deterministiset linkit`.
![KYCP](assets/2.webp)
Saatavillesi avautuu sivu, joka on omistettu Boltzmann-laskimen indikaattoreille.
![KYCP](assets/3.webp)
Niille, jotka haluavat käyttää työkalua suoraan RoninDojo-solmustaan, se on saavutettavissa `RoninCLI > Samourai Toolkit > Boltzmann-laskin`.

Kuten KYCP.org-sivustolla, kun Python-työkalu on asennettu, sinun tarvitsee vain liittää analysoitavan siirron TXID.

![KYCP](assets/7.webp)

Sen jälkeen paina `ENTER`-näppäintä saadaksesi tulokset.

![KYCP](assets/8.webp)

## Mitkä ovat Boltzmann-laskimen indikaattorit?
### Yhdistelmät / Tulkinnat:
Ensimmäinen indikaattori, jonka ohjelmisto laskee, on mahdollisten yhdistelmien kokonaismäärä, joka on merkitty `nb combinations` tai `interpretations` työkalussa.
Ottaen huomioon transaktiossa mukana olevien UTXO:iden arvot, tämä indikaattori laskee tapoja, joilla syötteet voidaan yhdistää tulosteisiin. Toisin sanoen se määrittää, kuinka monta uskottavaa tulkintaa transaktiosta voi saada ulkopuolisen tarkkailijan näkökulmasta sitä analysoitaessa. Esimerkiksi Whirlpool 5x5 -mallin mukaisesti rakennettu coinjoin tarjoaa `1,496` mahdollista yhdistelmää: ![KYCP](assets/4.webp)
Toisaalta Whirlpool Surge Cycle 8x8 coinjoin tarjoaa `9,934,563` mahdollista tulkintaa: ![KYCP](assets/5.webp)
Sen sijaan perinteisempi transaktio, jossa on 1 syöte ja 2 tulostetta, tarjoaa vain yhden tulkinnan: ![KYCP](assets/6.webp)

### Entropia:
Toinen laskettava indikaattori on transaktion entropia, joka on merkitty `Entropy`.

Yleisessä kryptografian ja tiedon kontekstissa entropia on kvantitatiivinen mittari epävarmuudelle tai ennustamattomuudelle, joka liittyy datalähteeseen tai satunnaiseen prosessiin. Toisin sanoen entropia on tapa mitata, kuinka vaikeaa tieto on ennustaa tai arvata.

Ketjuanalyysin erityiskontekstissa entropia on myös indikaattorin nimi, joka on johdettu Shannonin entropiasta ja [keksinyt LaurentMT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf), ja se lasketaan Boltzmann-työkalulla.

Kun transaktio esittää suuren määrän mahdollisia yhdistelmiä, on usein relevanttia viitata sen entropiaan. Tämä indikaattori mahdollistaa mittaamaan analyytikoiden tiedon puutetta transaktion tarkasta konfiguraatiosta. Toisin sanoen, mitä korkeampi entropia, sitä vaikeampi analyytikoiden tehtäväksi tulee tunnistaa bitcoinien liikkeitä syötteiden ja tulosteiden välillä.

Käytännössä entropia paljastaa, esittääkö transaktio ulkopuolisen tarkkailijan näkökulmasta useita mahdollisia tulkintoja, perustuen pelkästään syötteiden ja tulosteiden määriin, ottamatta huomioon muita ulkoisia tai sisäisiä malleja ja heuristiikkoja. Korkea entropia on siten synonyymi paremmalle transaktion luottamuksellisuudelle.

Entropia määritellään mahdollisten yhdistelmien lukumäärän binäärilogaritmiksi. Tässä on käytetty kaava:
```bash
E: transaktion entropia
C: transaktion mahdollisten yhdistelmien lukumäärä

E = log2(C)
```

Matematiikassa binäärilogaritmi (kantaluku-2 logaritmi) vastaa kahden eksponentoimisen käänteistoimintoa. Toisin sanoen `x`:n binäärilogaritmi on eksponentti, johon `2` on korotettava saadakseen `x`. Tämä indikaattori ilmaistaan siten bitteinä.

Otetaan esimerkki entropian laskemisesta Whirlpool 5x5 -mallin mukaisesti rakennetulle coinjoin-transaktiolle, joka, kuten aiemmin mainittiin, tarjoaa `1,496` mahdollista yhdistelmää:
```bash
C = 1,496
E = log2(1,496)
E = 10.5469 bittiä
```
Näin ollen tämä coinjoin-transaktio esittää entropian `10.5469 bittiä`, mikä on pidettävä erittäin tyydyttävänä. Mitä korkeampi tämä arvo, sitä enemmän erilaisia tulkintoja transaktio sallii, vahvistaen sen yksityisyyden tasoa.
8x8 coinjoin-transaktiolle, joka esittää `9,934,563` tulkintaa, entropia olisi:
```bash
C = 9,934,563
E = log2(9,934,563)
E = 23.244 bittiä
```
Käsitellään toista esimerkkiä perinteisemmästä transaktiosta, jossa on yksi sisääntulo ja kaksi ulostuloa: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce) Tässä tapauksessa ainoa mahdollinen tulkinta on: `(In.0) > (Out.0 ; Out.1)`. Täten sen entropia määritellään arvoon `0`:```bash
C = 1
E = log2(1)
E = 0 bittiä
```

### Tehokkuus:
Kolmas Boltzmann-laskurin tarjoama indikaattori on nimeltään `Lompakon Tehokkuus`. Tämä indikaattori arvioi transaktion tehokkuutta vertaamalla sitä optimaaliseen transaktioon samassa konfiguraatiossa.

Tämä johtaa meidät keskustelemaan maksimaalisen entropian käsitteestä, joka vastaa korkeinta entropiaa, jonka tietty transaktiorakenne voisi teoreettisesti saavuttaa. Transaktion tehokkuus lasketaan sitten vertaamalla tätä maksimaalista entropiaa analysoitavan transaktion todelliseen entropiaan.

Käytetty kaava on seuraava:
```bash
ER: transaktion todellinen entropia bittienä
EM: tietyn transaktiorakenteen maksimaalinen mahdollinen entropia bittienä
Ef: transaktion tehokkuus bitteinä

Ef = ER - EM
```

Esimerkiksi Whirlpool 5x5 -tyyppisen coinjoin-rakenteen maksimaalinen entropia on asetettu arvoon `10.5469`:
```bash
ER = 10.5469
EM = 10.5469
Ef = 10.5469 - 10.5469 = 0 bittiä
```

Tämä indikaattori ilmaistaan myös prosentteina, sen kaava on silloin:
```bash
CR: todellinen mahdollisten yhdistelmien määrä
CM: maksimaalinen mahdollisten yhdistelmien määrä samalla rakenteella
Ef: tehokkuus ilmaistuna prosentteina

Ef = CR / CM
Ef = 1,496 / 1,496
Ef = 100%
```

Tehokkuus `100%` siis osoittaa, että transaktio maksimoi yksityisyytensä potentiaalin sen rakenteen mukaisesti.

### Entropian Tiheys:
Neljäs indikaattori on entropian tiheys, merkitty työkalussa `Entropian Tiheys`. Se tarjoaa näkökulman entropiasta suhteessa kunkin transaktion sisääntuloon tai ulostuloon. Tämä indikaattori on hyödyllinen transaktioiden tehokkuuden arvioimiseksi ja vertaamiseksi eri kokoisissa transaktioissa. Sen laskemiseksi jaetaan yksinkertaisesti transaktion kokonaisentropia transaktion sisääntulojen ja ulostulojen kokonaismäärällä:
```bash
ED: entropian tiheys bitteinä
E: transaktion entropia bitteinä
T: transaktion sisääntulojen ja ulostulojen kokonaismäärä

ED = E / T
```

Käytetään esimerkkinä Whirlpool 5x5 coinjoinia:
```bash
T = 5 + 5 = 10
E = 10.5469
ED = 10.5469 / 10 = 1.054 bittiä
```

Lasketaan myös entropian tiheys Whirlpool 8x8 coinjoinille:
```bash
T = 8 + 8 = 16
E = 23.244
ED = 23.244 / 16 = 1.453 bittiä
```
Boltzmann-laskimen viides tiedonanto on taulukko syötteiden ja tulosteiden vastaavuustodennäköisyyksistä. Tämä taulukko osoittaa Boltzmann-pisteytyksen kautta ehdollisen todennäköisyyden, että tietty syöte liittyy annettuun tulosteeseen.
Se on siis kvantitatiivinen mittari ehdolliselle todennäköisyydelle, että syötteen ja tulosteen välinen yhteys tapahtumassa esiintyy, perustuen suotuisten tapahtumien määrän suhteeseen kaikkien mahdollisten tapahtumien määrään tulkintojen joukossa.

Ottaen esimerkiksi jälleen Whirlpool-coinjoinin, ehdollisten todennäköisyyksien taulukko korostaisi kunkin syötteen ja tulosteen välisen yhteyden mahdollisuuksia, tarjoten kvantitatiivisen mittarin tapahtuman yhteyksien epäselvyydelle:

| %       | Tuloste 0 | Tuloste 1 | Tuloste 2 | Tuloste 3 | Tuloste 4 |
| ------- | --------- | --------- | --------- | --------- | --------- |
| Syöte 0 | 34%       | 34%       | 34%       | 34%       | 34%       |
| Syöte 1 | 34%       | 34%       | 34%       | 34%       | 34%       |
| Syöte 2 | 34%       | 34%       | 34%       | 34%       | 34%       |
| Syöte 3 | 34%       | 34%       | 34%       | 34%       | 34%       |
| Syöte 4 | 34%       | 34%       | 34%       | 34%       | 34%       |

Tässä voimme selvästi nähdä, että jokaisella syötteellä on yhtä suuri mahdollisuus liittyä mihin tahansa tulosteeseen, mikä lisää tapahtuman luottamuksellisuutta.
Boltzmann-pisteytyksen laskeminen sisältää tietyn tapahtuman esiintymien määrän jakamisen saatavilla olevien tulkintojen kokonaismäärällä. Näin ollen määrittääkseen pisteytyksen, joka yhdistää syötteen nro 0 tulosteeseen nro 3 (`512` tulkintaa), käytetään seuraavaa menettelyä:
```bash
Tulkinnat (IN.0 > OUT.3) = 512
Kokonaistulkinnat = 1496
Pisteytys = 512 / 1496 = 34%
```

Ottaen esimerkiksi Whirlpool 8x8 -coinjoinin (surge-sykli), Boltzmann-taulukko näyttäisi tältä:

|       | OUT.0 | OUT.1 | OUT.2 | OUT.3 | OUT.4 | OUT.5 | OUT.6 | OUT.7 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| IN.0  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.1  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.2  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.3  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.4  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.5  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.6  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.7  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |

Kuitenkin yksinkertaisessa siirrossa, jossa on yksi lähtö ja kaksi tulosta, tilanne on erilainen:

| %       | Tuloste 0 | Tuloste 1 |
|---------|-----------|-----------|
| Lähtö 0 | 100%      | 100%      |

Tässä havaitaan, että todennäköisyys kullekin tulosteelle olla peräisin lähdöstä numero 0 on `100%`. Alempi todennäköisyys siis tarkoittaa suurempaa yksityisyyttä laimentamalla suoria yhteyksiä lähtöjen ja tulosteiden välillä.

### Deterministiset Linkit:
Kuudes annettu tieto on determinististen linkkien lukumäärä, täydennettynä näiden linkkien suhteella. Tämä indikaattori paljastaa, kuinka monta kiistatonta yhteyttä analysoitavassa siirrossa on lähtöjen ja tulosteiden välillä, todennäköisyydellä `100%`. Toisaalta suhde tarjoaa näkökulman näiden determinististen linkkien painoarvoon koko siirron linkkien joukossa.
Esimerkiksi Whirlpool-tyyppisessä coinjoin-siirrossa ei ole deterministisiä linkkejä, ja siksi näyttää indikaattorin ja suhteen `0%`. Päinvastoin toisessa tarkastellussa yksinkertaisessa siirrossa (yhdellä lähdöllä ja kahdella tulosteella) indikaattori on asetettu arvoon `2` ja suhde saavuttaa `100%`. Näin ollen nolla-indikaattori signaloi erinomaista luottamuksellisuutta johtuen suorien ja kiistattomien linkkien puuttumisesta lähtöjen ja tulosteiden välillä.

**Ulkoiset Resurssit:**

- Boltzmann-koodi Samourailla
- [Bitcoin-siirrot & Yksityisyys (Osa I) kirjoittanut Laurent MT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [Bitcoin-siirrot & Yksityisyys (Osa II) kirjoittanut Laurent MT](https://gist.github.com/LaurentMT/d361bca6dc52868573a2)
- [Bitcoin-siirrot & Yksityisyys (Osa III) kirjoittanut Laurent MT](https://gist.github.com/LaurentMT/e8644d5bc903f02613c6)
- KYCP-verkkosivusto
- [Medium-artikkeli Boltzmann-skriptin esittelystä kirjoittanut Laurent MT](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)