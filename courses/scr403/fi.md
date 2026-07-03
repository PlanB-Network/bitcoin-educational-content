---
name: Sukellus Simplicityn yksinkertaisuuteen
goal: Hallitse Simplicityn suunnittelufilosofia, tyyppijärjestelmä ja koko elinkaari
objectives:
  - Ymmärtää kolme perustavanlaatuista kompositiomenetelmää ja yhdeksän kombinaattoria, jotka muodostavat täydellisen kielen
  - Rakentaa Boolen logiikka, aritmetiikka ja SHA-256 Simplicityn minimaalisesta tyyppijärjestelmästä
  - Käsittää, miten Failure- ja Reader-sivuvaikutukset mahdollistavat todellisen vuorovaikutuksen blockchainin kanssa
  - Oppia, miten Simplicity-ohjelmista tulee Taproot-osoitteita ja miten ne lunastetaan witness-datalla
---

# Sukellus Simplicityn yksinkertaisuuteen

Syväsukellus Simplicity-kielen taustalla olevaan teoriaan ja suunnittelupäätöksiin. Kurssi perustuu Simplicityn Blockstream Researchilla luoneen [Dr. Russell O'Connorin](https://r6.ca/) viisiosaiseen ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) -artikkelisarjaan. Tämä kurssi selittää, *miksi* Simplicity suunniteltiin niin kuin se suunniteltiin, ei miten sitä kirjoitetaan.

Kurssi seuraa Dr. O'Connorin artikkeleita kolmen perustavanlaatuisen laskentojen yhdistämistavan, minimaalisen tyyppijärjestelmän ja sen täydellisyyslauseen, käytännöllisten tietotyyppien ja aritmetiikan rakentamisen ensimmäisistä periaatteista, blockchain-vuorovaikutukseen tarvittavien sivuvaikutusten varovaisen käyttöönoton sekä lopuksi sen läpi, miten ohjelmiin sitoudutaan osoitteissa ja miten ne lunastetaan on-chain.

+++

# Johdanto

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Kurssin yleiskatsaus

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

Tervetuloa kurssille SCR403 — Sukellus Simplicityn yksinkertaisuuteen!

Tämä kurssi perustuu **"Delving Simplicity"** -artikkelisarjaan, jonka on kirjoittanut [Dr. Russell O'Connor](https://r6.ca/), [Blockstreamin](https://blockstream.com/) Infrastructure Tech Developer ja Simplicityn luoja. Alkuperäiset artikkelit julkaistiin [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) -foorumilla ja ne muodostavat tämän kurssin ensisijaisen lähdemateriaalin. Olemme kiitollisia hänen uraauurtavasta työstään, joka teki tämän opetussisällön mahdolliseksi.

### Mitä opit

Tämä kurssi tutkii Simplicityn, heinäkuussa 2025 [Liquid Networkissa](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) aktivoidun seuraavan sukupolven skriptauskielen, suunnittelufilosofiaa ja matemaattisia perusteita. Se seuraa täydellistä viisiosaista artikkelisarjaa ja on jäsennetty kahteen pääsisältöosioon:

1. **Simplicityn perusteet** — Miksi blockchain-laskenta vaatii perustavanlaatuisesti erilaisen kielen, kolme tapaa yhdistää operaatioita (peräkkäinen, rinnakkainen, ehdollinen) ja yhdeksän ydinkombinaattoria, jotka muodostavat matemaattisesti täydellisen kielen
2. **Tietotyypeistä ohjelmiin** — Boolen logiikan, aritmetiikan ja SHA-256:n rakentaminen ensimmäisistä periaatteista; blockchain-vuorovaikutuksen mahdollistavien Failure- ja Reader-sivuvaikutusten ymmärtäminen; sekä sen oppiminen, miten ohjelmiin sitoudutaan Taproot-osoitteissa Commitment Merkle Rootien kautta ja miten ne lunastetaan witness-datalla

### Esivaatimukset

Tämä on **asiantuntijatason** kurssi (noin 10 tuntia). Sinun tulisi olla sinut seuraavien kanssa:
- Bitcoinin skriptauksen peruskäsitteet (mitä transaktion validointi tekee)
- Ohjelmoinnin peruskäsitteet (tyypit, funktiot, kompositio)
- Jonkinlainen matemaattisen notaation tuntemus on hyödyksi mutta ei pakollista. Esittelemme kaiken matkan varrella

### Keskeiset resurssit

- **Alkuperäiset artikkelit**: ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary), Dr. Russell O'Connor, Delving Bitcoinissa
- **Simplicity-repositorio**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — lähdekoodi ja Rocqin formaalit todistukset
- **Virallinen verkkosivusto**: [simplicity-lang.org](https://simplicity-lang.org/) — dokumentaatio ja SimplicityHL-viite
- **Blockstreamin blogi**: [Simplicity GitHubissa](https://blog.blockstream.com/en-simplicity-github/) — tekninen yleiskatsaus

Valmis sukeltamaan yhteen Bitcoin-insinöörityön eleganteimmista kokonaisuuksista? Mennään!

## Mitä Simplicity on?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

Jos tulet tälle kurssille ilman taustaa Simplicitystä, tämä luku asemoi sinut ennen kuin sukellamme syvään päähän.

### Simplicity pähkinänkuoressa

Simplicity on **Bitcoin-natiivi älysopimuskieli**, joka on käytössä Liquid Networkissa tänään. Dr. Russell O'Connor hahmotteli sen ensimmäisen kerran noin vuonna 2012 ja kuvasi sen yksityiskohtaisesti vuoden 2017 artikkelissaan *Simplicity: A New Language for Blockchains*. Se aktivoitiin Liquid Networkissa heinäkuussa 2025 vuosien formaalin verifioinnin ja kehitystyön jälkeen.

Toisin kuin Ethereumin Solidity, joka on Turing-täydellinen korkean tason sopimuskieli, Simplicity on tarkoituksella minimaalinen. Siinä on:
- **Kolme tyypinmuodostajaa** (yksikkö, summa, tulo)
- **Yhdeksän kombinaattoria** (perusoperaatiot ja kompositiosäännöt)
- **Ei silmukoita, ei rekursiota, ei dynaamista muistia**

Pelkästään näistä primitiiveistä voidaan rakentaa mikä tahansa transaktion validointiin tarvittava laskenta Boolen logiikasta täyteen SHA-256-hajautukseen.

### Mitä Simplicityllä voi tehdä tänään?

Simplicity pyörittää jo todellisia sovelluksia Liquid Networkissa. Merkittävin niistä on [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/), oraakkeliton optiomarkkinapaikka, jossa käyttäjät käyvät kauppaa L-BTC:n call-optioilla käyttäen USDt:tä vakuutena (taustalla oleva sopimus tukee myös put-optioita). Muita toimivia Simplicity-projekteja ovat SideSwapin [Swaption](https://swaption.io/) (optiot) ja Resolvrin avoimen lähdekoodin [Deadcat](https://github.com/Resolvr-io/deadcat) (ennustemarkkinat). DeFin lisäksi Simplicity mahdollistaa edistyneet käyttöehdot, kuten holvit, covenantit ja monimutkaiset multisig-järjestelyt, jotka olisivat mahdottomia tai turvattomia Bitcoin Scriptissä.

### Mitä tämä kurssi on — ja mitä se ei ole

Tämä **ei** ole käytännönläheinen koodaustutoriaali. Et kirjoita täällä Simplicity-ohjelmia. Jos etsit sitä, katso:
- [simplicity-lang.org](https://simplicity-lang.org/) — virallinen dokumentaatio ja korkean tason SimplicityHL-kieli
- [Simplicityn GitHub-repositorio](https://github.com/BlockstreamResearch/simplicity) — viitetoteutus, esimerkit ja Rocq-todistukset
- [Blockstreamin blogikirjoitus](https://blog.blockstream.com/en-simplicity-github/) alkuun pääsemisestä

Se, mistä tämä kurssi **kertoo**, on Simplicityn suunnittelun taustalla olevat **filosofiset ja tekniset valinnat**. Miksi tämä kieli luotiin tällä tavalla? Miksi vain yhdeksän kombinaattoria? Miksi ei rekursiota? Miksi sillä on väliä, että tyyppijärjestelmä liittyy Gentzenin sekventtikalkyyliin?

Ajattele sitä pikemminkin sen ymmärtämisenä, **miksi moottori rakennettiin tällä tavalla**, kuin auton ajamisen opetteluna.

### Kenelle tämä on tarkoitettu?

Tämä kurssi sopii ihanteellisesti:
- **Protokollakehittäjille**, jotka haluavat ymmärtää Simplicityn perusteet ennen koodin kirjoittamista
- **Bitcoin-tutkijoille**, joita kiinnostavat formaali verifiointi ja tyyppiteoreettinen lähestymistapa
- **Tietojenkäsittelytieteilijöille**, joita kiinnostaa sekventtikalkyylin ja blockchain-laskennan välinen yhteys
- **Edistyneille bitcoinereille**, jotka haluavat mennä Liquidin skriptauskyvykkyyksien pintatason ymmärrystä pidemmälle

Jos termit kuten "summatyypit", "kombinaattorit" tai "sekventtikalkyyli" ovat sinulle täysin uusia, älä huoli, selitämme kaiken alusta. Varaudu kuitenkin tiiviiseen, matemaattiseen matkaan.

### Artikkeleista kurssiksi

Dr. O'Connorin alkuperäinen "Delving Simplicity" -sarja on jäsennetty viideksi tekniseksi artikkeliksi. Tämä kurssi järjestää ja kommentoi kyseisen materiaalin uudelleen progressiiviseksi oppimispoluksi, jonka varrella on visoja ymmärryksesi testaamiseksi. Ideat, määritelmät ja todistukset ovat hänen, ja olemme mukauttaneet formaatin rakenteelliseen opetukseen.

# Simplicityn perusteet

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Laskentojen yhdistämisen perustavat tavat

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

Nyt kun Simplicity on aktivoitu Liquid Networkissa, haluaisin tehdä perusteellisen sukelluksen Simplicity-kielen filosofiaan ja suunnitteluun.

Bitcoinin transaktioiden validointi on huomattavasti erilainen sovellus kuin tavallinen ohjelmointikielen suunnittelu. Lohkotila on kallista, joten ohjelmien täytyy olla kompakteja. Bitcoin-transaktioiden ohjelmat suoritetaan aina vain yhdelle syötteelle, ja kaikki suorittavat ohjelman samalla syötteellä. Lisäksi transaktion valtuuttava toimija tietää laskennan tuloksen jo etukäteen: transaktio on kelvollinen.

Tyypillisesti valtuuttava toimija ajaa paljon kalliimpia laskentoja johtaakseen witness-datan, joka todistaa transaktion kelvollisuuden, kun taas blockchainissa ajettavien ohjelmien tarvitsee tarkistaa witness-datan kelvollisuus. Kelvollisuuden tarkistaminen on usein paljon halvempaa kuin kelvollisuuden todistaminen.

Olemme suunnitelleet Simplicityn nämä ainutlaatuiset kielensuunnittelun haasteet mielessä. Esimerkiksi Simplicity vaatii, että suorittamattomat haarat karsitaan niin, etteivät ne näy blockchainissa. Esikäsittelyvaiheet on suunniteltu huolellisesti ilmentämään (kvasi-)lineaarista aikavaativuutta Simplicity-ohjelman kokoon nähden. Staattista analyysia käytetään "gasin" sijasta, koska gasia ei voida laskea suorittamatta koodia määrätyllä tavalla, jotta suoritusmallin yksityiskohdista ei tule konsensuskriittisiä. Ei dynaamista muistivarausta suorituksen aikana. Ja niin edelleen.

Ennen kuin sukellamme Simplicityn suunnitteluyksityiskohtiin, haluan aloittaa tämän sarjan ohjelmointifilosofialla siitä, millä yleisillä tavoilla perusrakennuspalikoita yhdistetään uuden toiminnallisuuden luomiseksi.

### Kompositio

Oletetaan, että suunnitellaan ohjelmoitavien transaktioiden kieltä Bitcoinin kaltaiselle blockchainille. Erityisesti ohjelmilla on pääsy vain transaktiodataan ja syötteiden UTXO-dataan, ja suoritus määrittää vain transaktion kelvollisuuden (mikä mahdollistaa suoritustuloksen välimuistiin tallentamisen). Sanotaan, että aloitetaan joukosta perusoperaatioita, jotka voivat tehdä erilaisia tehtäviä, kuten peruslaskentaa, datan lukemista ja/tai käsittelyä transaktiosta sekä allekirjoituksen verifiointia. Jokainen operaatio kuluttaa jonkin tyyppisen syötteen (mahdollisesti tyhjän) ja palauttaa jonkin tyyppisen tulosteen. Millä tavoilla voimme yhdistää nämä perusoperaatiot monimutkaisemmiksi operaatioiksi?

### Peräkkäinen kompositio

![Peräkkäinen kompositio](assets/en/001.webp)

Perustavin kompositiomenetelmä on peräkkäinen kompositio. Jos meillä on kaksi perusoperaatiota, joista toisen tulosteen tietotyyppi vastaa toisen syötteen tietotyyppiä, voimme yhdistää nämä kaksi operaatiota uudeksi yhdistelmäoperaatioksi. Tämä uusi operaatio ajaa nämä kaksi perusoperaatiota peräkkäin, ottaa syötteekseen ensimmäisen operaation syötteen, välittää ensimmäisen operaation tulosteen toisen operaation syötteeksi ja palauttaa lopulta toisen operaation tulosteen.

Emme tietenkään tarvitse rajoittua vain perusoperaatioiden yhdistämiseen. Nyt kun meillä on joitakin yhdistelmäoperaatioita, voimme yhdistää myös niitä funktionaalisen komposition avulla.

Matematiikassa tätä peräkkäistä kompositiota kutsutaan usein vain "kompositioksi", ja voisi ajatella, että tämä on ainoa tapa koostaa asioita. Operaatioiden koostamiseen on kuitenkin muitakin tapoja.

### Rinnakkainen kompositio

![Rinnakkainen kompositio](assets/en/002.webp)

Oletetaan, että meillä on kaksi operaatiota; ne voivat olla perusoperaatioita tai monimutkaisia operaatioita, ja molemmat ottavat saman tyyppisen syötteen. Toinen perustava tapa koostaa nämä kaksi operaatiota on suorittaa ne molemmat samalla syötteellä. Tätä kutsutaan rinnakkaiseksi kompositioksi, ja tulosteen tyyppi on alkuperäisten operaatioiden tulostetyyppien "tulo" ja sisältää näiden kahden tulosteen parin.

Vaikka tätä kutsutaan "rinnakkaiseksi" kompositioksi, ja nämä kaksi operaatiota voitaisiin periaatteessa suorittaa rinnakkain, rinnakkainen suoritus ei ole toiminnallinen vaatimus. Voimme toteuttaa rinnakkaisen komposition "peräkkäisesti" suorittamalla ensin yhden operaation ja sitten toisen operaation. Emme välitä siitä, miten rinnakkainen kompositio toteutetaan, kunhan tuloste on sama.

### Ehdollinen kompositio

![Ehdollinen kompositio](assets/en/003.webp)

Ehdollinen kompositio on rinnakkaisen komposition duaali. Tässä tapauksessa meillä on kaksi operaatiota, jotka tuottavat saman tulosteen, ja koostamme ne valitsemalla toisen suoritettavaksi. Tämän yhdistelmäoperaation syöte on alkuperäisten operaatioiden syötetyyppien "summa" tai "tagged union". Tässä tapauksessa tagi, "Left" tai "Right", on yksittäinen bitti syötteen datassa, joka määrittää, minkä tyyppistä dataa kuljetetaan, ja siten kumpi kahdesta operaatiosta voidaan suorittaa.

Ehdollinen kompositio toimii samalla tavalla myös silloin, kun syöte on kahden identtisen tyypin summa. Summatyyppi sisältää silti tagin, ja tagin arvo määrittää, kumpi kahdesta operaatiosta suoritetaan.

### Kompositio Bitcoin Scriptissä

Näiden kolmen komposition lajin toteuttamiseen eri ohjelmointikielissä on monia tapoja. Bitcoin Scriptissä peräkkäinen kompositio toteutuu (likimain) kahden rutiinin konkatenoimisella (siksi Bitcoin Scriptiä kutsutaan konkatenatiiviseksi ohjelmointikieleksi), koska yhden rutiinin tuloste jätetään pinoon myöhemmän rutiinin kulutettavaksi. Rinnakkainen kompositio saavutetaan duplicate- ja swap-operaatioilla, joilla pinoa manipuloidaan niin, että kaksi rutiinia voidaan ajaa samalla syötteellä. Asiat eivät ole täysin suoraviivaisia, sillä se, mitä kutsumme tyyppien "tuloksi", toteutetaan tyypillisesti hyödyntämällä useita pinoalkioita. Toivottavasti näet yleisen idean.

Ehdollinen kompositio toteutetaan tietenkin `OP_IF`:llä, joka haarautuu pinossa olevan arvon perusteella. Tässä tapauksessa pinon ylin alkio toimii tagin roolissa, ja yleensä seuraava alkio tai seuraavat alkiot pinossa ovat eri "tyyppejä", jotka riippuvat tagin arvosta. Kussakin tapauksessa pinoalkioiden tyypit voivat soveltua käsiteltäviksi vain yhdessä `OP_IF`:n haaroista. Kun kuitenkin saavumme `OP_ENDIF`:iin, pinoalkioiden täytyy olla yhdenmukaista "tyyppiä", jotta jäljellä oleva skripti pystyy jatkamaan riippumatta siitä, mikä haara aiemmin valittiin.

### Kompositio Simplicityssä

Suunnittelimme Simplicityn kombinaattoreilla, jotka toteuttavat nämä kolme komposition muotoa suoraan. Muutaman muun tulo- ja summatyyppeihin liittyviä perusoperaatioita tukevan kombinaattorin kanssa Simplicityn ydinkieli koostuu lopulta yhdeksästä kombinaattorista, jotka riittävät ilmaisemaan minkä tahansa äärellisen laskennan. Keskustelemme tästä tarkemmin seuraavassa luvussa.

### Neljäs komposition laji

Ennen lopettamista pitäisi mainita, että tietojenkäsittelytieteessä on ainakin yksi muukin komposition laji, nimittäin "rekursiivinen kompositio". Rekursiivisessa kompositiossa yhtä operaatiota iteroidaan useita kertoja.

Huomaa, että Bitcoin Script ei tue rekursiivista kompositiota, ja vastaavasti olemme nimenomaisesti sulkeneet rajoittamattoman rekursion pois Simplicityn suunnittelusta. Teesimme on, että rajoittamaton iteratiivinen laskenta toteutetaan paremmin rekursiivisilla covenanteilla, jotka laskevat useiden transaktioiden yli. Tämä antaa käyttäjien välttää lohkotilan ja standardness-sääntöjen rajoitteita ja ennustaa transaktiokustannuksia paremmin.

Tästä huolimatta on tapoja käyttää Simplicityn delegointiominaisuutta väärin, jotta saadaan aikaan jotain rajoittamatonta rekursiivista kompositiota muistuttavaa; tästä saatamme keskustella myöhemmin tässä sarjassa.

### Yhteenveto

Kävimme läpi kolme pääasiallista komposition muotoa, joilla perusoperaatiot muunnetaan monimutkaisiksi operaatioiksi:

- peräkkäinen kompositio
- rinnakkainen kompositio
- ehdollinen kompositio

Keskustelimme siitä, miten nämä komposition muodot toteutetaan Bitcoin Scriptissä, ja vihjasimme, miten ne ovat vaikuttaneet Simplicity-kielen suunnitteluun. Huomasimme, että neljäs komposition laji, rekursiivinen kompositio, on erikseen suljettu pois sekä Simplicitystä että Bitcoin Scriptistä.

Seuraavassa luvussa kuvaamme Simplicityn ydinkielen muodostavat yhdeksän kombinaattoria, miten ne toteuttavat suoraan nämä kolme komposition muotoa, ja miten tästä muodostuu täydellinen kieli minkä tahansa äärellisen laskennan kuvaamiseen.

## Simplicityn kombinaattorien täydellisyys

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

Tässä luvussa esittelemme Simplicityn ydinkielen ja näytämme, että kieli on täydellinen, mikä tarkoittaa, että mikä tahansa äärellinen laskenta voidaan ilmaista siinä.

### Simplicity-tyypit

Simplicity tukee kolmea perustavaa tyyppikonstruktoria. Tulotyyppi `A × B` edustaa rinnakkaisen komposition tulosteita, kun taas summatyyppi `A + B` (tagged union) käsittelee ehdollisen komposition syötteitä. Kolmas tyyppi on yksikkötyyppi.

### Yksikkötyyppi

Yksikkötyyppi, merkittynä `𝟙` tai `ONE`, sisältää täsmälleen yhden arvon: tyhjän tuplen `⟨⟩` tai `()`. Tämä nollabitin tietotyyppi ei kanna mitään informaatiota.

### Summatyyppi

Summatyyppi `A + B` yhdistää kaksi tyyppiä tageilla, jotka ilmaisevat "vasen" tai "oikea". Arvot kirjoitetaan muodossa `σᴸ(a)` tai `inl(a)` vasemmalla tagatuista arvoista ja `σᴿ(b)` tai `inr(b)` oikealla tagatuista arvoista. Tagit pysyvät erillisinä myös identtisiä tyyppejä yhdistettäessä.

#### Boolen tyyppi

Tyyppi `𝟙 + 𝟙`, merkittynä `𝟚` tai `TWO`, edustaa yhden bitin tyyppiä, jolla on kaksi arvoa. Konvention mukaan `σᴸ⟨⟩` edustaa epätotta/nollaa, kun taas `σᴿ⟨⟩` edustaa totta/ykköstä.

### Tulotyyppi

Tulotyypit `A × B` sisältävät arvopareja, jotka kirjoitetaan muodossa `⟨a, b⟩` tai `(a, b)`. Tyypillä `𝟚 × 𝟚` on neljä arvoa, jotka ovat erillisiä tyypin `𝟚 + 𝟚` neljästä arvosta.

### Simplicityn ydilausekkeet

Operaatiot merkitään muodossa `f : A ⊢ B`, mikä tarkoittaa syötetyyppiä `A` ja tulostetyyppiä `B`. Simplicity on "ensimmäisen kertaluvun" kieli — siitä puuttuvat funktiotyypit.

### Kaksi perusoperaatiota

Ydinkieli tarjoaa kaksi perusoperaatiota:

**Identiteetti (`iden`).** Identiteettioperaatio välittää syötteensä muuttumattomana läpi:

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Yksikkö (`unit`).** Yksikköoperaatio hylkää syötteensä ja palauttaa tyhjän tuplen:

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

Nämä muodostavat perheitä, joissa on yksi operaatio jokaista tyyppiä kohden.

### Kolme kompositiokombinaattoria

Peräkkäinen kompositio käyttää `comp f g`:tä (kirjoitettuna `f ⨾ g` tai `f >>> g`):

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

Rinnakkainen kompositio käyttää `pair f g`:tä (kirjoitettuna `f ▵ g` tai `f &&& g`):

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

Ehdollinen kompositio käyttää `case f g : (A + B) × C ⊢ D`:tä, tarjoten haaroille pääsyn jaettuun ympäristöön `C`:

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

Miksi ehdollinen kompositio saa tämän muodon — summa paritettuna jaetun ympäristön `C` kanssa — eikä yksinkertaisempaa muotoa `copair f g : A + B ⊢ C`, joka vain valitsee haaran? Koska pelkkä `copair` ei voi ilmaista **distribuutiota**: funktiota `dist : (A + B) × C ⊢ A × C + B × C`, joka työntää jaetun syötteen siihen haaraan, joka valitaan. Rakentamalla ympäristön `C` suoraan `case`:en Simplicity saa ehdollisen komposition *ja* distribuution yhdestä kombinaattorista — yhden keskeisistä suunnittelupäätöksistä, joka pitää ydinkielen yhdeksässä kombinaattorissa.

### Neljä muuta kombinaattoria

Tulon kuluttaminen käyttää `take` ja `drop`:

**take** poimii vasemman alkion:

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** poimii oikean alkion:

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

Summan tuottaminen käyttää `injl` ja `injr`:

**injl** käärii vasemmalla tagilla:

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** käärii oikealla tagilla:

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### Yhdeksän ydinkombinaattoria

Yhteensä Simplicityssä on täsmälleen yhdeksän ydinkombinaattoria:

| Kombinaattori | Tarkoitus |
|---|---|
| `iden` | Välitä syöte läpi |
| `unit` | Hylkää syöte |
| `comp` | Peräkkäinen kompositio |
| `pair` | Rinnakkainen kompositio |
| `case` | Ehdollinen kompositio |
| `take` | Poimi tulon vasen puoli |
| `drop` | Poimi tulon oikea puoli |
| `injl` | Injektoi summan vasempaan puoleen |
| `injr` | Injektoi summan oikeaan puoleen |

### Simplicity ja sekventtikalkyyli

Simplicityn suunnittelu juontuu Gentzenin sekventtikalkyylin konjunktiivis-disjunktiivisesta fragmentista. Tarkemmin sanottuna se on sekventtikalkyylin *funktionaalisen interpretaation* muunnelma, joka itsessään on analoginen luonnollisen päättelyn ja lambdakalkyylin välisen Curry-Howard-vastaavuuden kanssa. Kombinaattorisäännöissä on "premisseissä pienemmät tyypit kuin johtopäätöksissä", mikä mahdollistaa Bit Machinelle — Simplicityn abstraktille pinokoneinterpretaattorille — datan kopioinnin minimoimisen suorituksen aikana.

### Arvot eivät ole lausekkeita

Simplicity-lausekkeet merkitsevät operaatioita, eivät arvoja. Notaatio `scribe b : A ⊢ B` edustaa ainutlaatuista lauseketta, joka palauttaa aina arvon `b`, ja toimii notaatioapuna eikä kombinaattorina. Tämä peilaa Bitcoin Scriptiä, jossa operaatiot kuten `OP_1` työntävät arvoja eivätkä ilmaise niitä suoraan.

### Simplicityn täydellisyyslause

Kun kaikki yhdeksän kombinaattoria ovat käsillä, mistä tiedämme, ettei meiltä puutu jotakin — että nämä yhdeksän todella riittävät? Simplicityn täydellisyyslause vastaa tähän: mille tahansa funktiolle (äärellisten) Simplicity-tyyppien välillä jokin Simplicity-lauseke ilmaisee sen. Todistus on konstruktiivinen — se näyttää, miten lauseke rakennetaan:

1. **Hajota syöte**: Käyttämällä sisäkkäisiä `case`-lausekkeita hajota minkä tahansa tyypin mikä tahansa syöte täysin sen osabitteihin
2. **Rakenna hakutaulu**: Käytä jokaista mahdollista syötettä kohden `scribe`:ä vastaavan tulosteen tuottamiseen
3. **Kokoa**: Sisäkkäiset caset ja scribet muodostavat yhdessä jättimäisen hakutaulun, joka toteuttaa funktion

Tämä lause on formaalisti verifioitu Rocq-todistusavustimessa (aiemmin Coq). Todistus on osa virallista Simplicity-repositoriota, ja sen oikeellisuus on tarkistettu koneellisesti.

Vaikka täydellisyyslause takaa, että Simplicityn yhdeksän kombinaattoria voivat ilmaista minkä tahansa funktion (äärellisten) Simplicity-tyyppien välillä, hakutaulukonstruktiosta syntyvät lausekkeet ovat epäkäytännöllisen suuria. 256-bittisillä syötteillä toimiva funktio vaatisi hakutaulun, jossa on 2²⁵⁶ alkiota. Siksi seuraavat luvut keskittyvät rakentamaan tehokkaita lausekkeita, jotka hyödyntävät laskentojen rakennetta sen sijaan, että kaikki pakotettaisiin raakana hakutaulujen läpi.

### Yhteenveto

Simplicityn ydinkieli sisältää tyyppijärjestelmän ja kombinaattorit, jotka mahdollistavat minkä tahansa äärellisen laskennan. Vaikka täydellisyyslause takaa ilmaisuvoiman, geneerisestä konstruktiosta syntyvät lausekkeet ovat epäkäytännöllisen suuria. Käytännön Simplicity-kehitys edellyttää laskennallisen rakenteen hyödyntämistä tiiviiden lausekkeiden aikaansaamiseksi. Seuraavat luvut tutkivat tietorakenteita, transaktiovuorovaikutuksia ja lisäkombinaattoreita.

# Tietotyypeistä ohjelmiin

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Tietotyyppien rakentaminen

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

Edellisissä luvuissa näytimme, miten Simplicityn ydinkombinaattorien joukko riittää toteuttamaan minkä tahansa äärellisen puhtaan laskennan. Tämä luku näyttää, miten näistä primitiiveistä rakennetaan käytännöllisiä tietorakenteita ja laskentoja — samalla tavalla kuin tietokoneet rakennetaan logiikkaporteista.

### Boolen logiikka

Boolen tyyppi, merkittynä `𝟚`, on yhtä kuin `𝟙 + 𝟙` ja sillä on kaksi arvoa: `σᴸ⟨⟩` (epätosi) ja `σᴿ⟨⟩` (tosi). Ydinkombinaattoreilla voidaan rakentaa Boolen logiikkaoperaattoreita.

#### And-operaatio

Looginen `and : 𝟚 × 𝟚 ⊢ 𝟚` -operaatio ottaa kaksi bittiä ja palauttaa yhden bitin. Toteutus haarautuu ensimmäisen bitin perusteella: jos epätosi, palauta epätosi; muuten palauta toinen bitti.

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

Testaus syötteellä `⟨false, false⟩`:

```
⟦and⟧⟨false, false⟩
 = {expand the notation for false}
⟦and⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {expand the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {evaluate case for σᴸ}
⟦injl unit⟧⟨⟨⟩, σᴸ⟨⟩⟩
 = {evaluate injl}
σᴸ(⟦unit⟧⟨⟨⟩, σᴸ⟨⟩⟩)
 = {evaluate unit}
σᴸ⟨⟩
 = {by the notation for false}
false
```

Testaus syötteellä `⟨true, true⟩`:

```
⟦and⟧⟨true, true⟩
 = {expand the notation for true and the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴿ⟨⟩, σᴿ⟨⟩⟩
 = {evaluate case for σᴿ}
⟦drop iden⟧⟨⟨⟩, σᴿ⟨⟩⟩
 = {evaluate drop}
⟦iden⟧(σᴿ⟨⟩)
 = {evaluate iden}
σᴿ⟨⟩
 = {by the notation for true}
true
```

#### Muut logiikkaoperaatiot

`not`-operaatio vaatii apukombinaattorin:

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

Alkuperäinen `iden ▵ unit : A ⊢ A × 𝟙` lisää tyhjän "ympäristön" syötteeseen, mikä mahdollistaa `case`-kombinaattorin soveltamisen. `take`:n käyttö kahdessa haarassa pudottaa tämän tyhjän ympäristön ja suorittaa `f`:n tai `g`:n.

Muita Boolen loogisia operaatioita:

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Bittisummaimet

"Puolisummain" ottaa kaksi bittiä ja lisää ne yhteen tuottaen kaksibittisen tulosteen: siirtobitin ja summabitin.

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

"Kokosummain" lisää kolme bittiä ja tuottaa kaksibittisen tulosteen. Syöte käyttää sisäkkäistä tuplea `(𝟚 × 𝟚) × 𝟚`.

Sisäkkäisille tupleille käytetään kompaktia notaatiota:

- `O f` merkitsee `take f`
- `I f` merkitsee `drop f`
- `H` merkitsee `iden`

Esimerkiksi `I O H` tarkoittaa `drop (take iden) : A × (B × C) ⊢ B`, eli se poimii keskimmäisen arvon. Notaatio tuo mieleen binäärinumerot: kun sisäkkäisiä tupleja ajatellaan binääripuina, notaatio edustaa puun sijaintien käännettyjä binäärinumeroita. Nämä lausekkeet muodostavat De Bruijn -indeksejä Simplicitylle.

**Huomautus:** `I`-, `O`- ja `H`-notaatio koskee vain alilausekkeita, jotka koostuvat pelkästään `take`:sta, `drop`:sta ja `iden`:stä.

Kokosummain koostaa kaksi puolisummainta ja ottaa carry-bittien loogisen `or`:n:

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

Ensimmäisellä rivillä `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` ajaa puolisummaimen kahdelle ensimmäiselle bitille ja säilyttää viimeisen bitin.

Toisella rivillä `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` säilyttää ensimmäisen bitin (ensimmäisen puolisummaimen carry-outin) ja ajaa puolisummaimen kahdelle viimeiselle bitille.

Viimeisellä rivillä `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` ottaa kahden ensimmäisen bitin loogisen OR:n (molempien puolisummainten carry-outit) ja palauttaa toisen puolisummaimen sum-out-bitin.

Tämä havainnollistaa Simplicity-ohjelmointia: `I`-, `O`- ja `H`-notaatiolla viitataan databitteihin, muodostetaan sopivia "ympäristöjä" muiden funktioiden kutsumiseen peräkkäisen komposition kautta.

Käyttäjät eivät määrittele matalan tason operaatioita suoraan. Myöhemmin tässä sarjassa käsitellään standardikirjaston jettejä, jotka toteuttavat yleisiä funktioita. Loppukäyttäjien ei odoteta ohjelmoivan suoraan Simplicityssä, samaan tapaan kuin Bitcoin Scriptissä. Sen sijaan korkeamman tason kielet kuten SimplicityHL tuottavat Simplicity-koodia, hallitsevat alilausekkeiden "ympäristöjä" ja kääntävät nimetyt muuttujat sopiviksi `take`- ja `drop`-sekvensseiksi.

### Vektorit

Kiinteän pituiset vektorit määritellään muodostamalla tyypin `A` iteroituja tuloja:

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

Nämä voidaan kirjoittaa muodossa `A^2`, `A^4`, `A^8` jne.

Vektorit määritellään vain pituuksille, jotka ovat kahden potensseja. Muut potenssit vaativat sulutuskäytäntöjen valitsemista.

Kun annettu lauseke on `f : A ⊢ B`, toistuva paritus "kuvaa" sen kiinteän pituuden vektoreiden yli:

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

Kun annettu funktio on `f : A × B ⊢ B`, iteraatio tai "foldaus" kiinteän pituuden vektoreiden yli:

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

Monia variaatioita on olemassa. Kun annettu `f : A × B ⊢ C`, "zip" paritettujen vektorien yli muodossa `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ`. Kun annettu `f : (A × B) × C ⊢ C`, foldaus paritettujen vektorien yli muodossa `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C`. `map`:in ja `fold-right`:in yhdistäminen luo akkumuloivia kombinaattoreita: `f : A × C ⊢ C × B` tuottaa `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ`. Monia muitakin variantteja on mahdollisia.

#### Monibittiset sanat

Bittivektori tuottaa monibittisiä kokonaislukuja. Esimerkiksi `𝟚³²` on 32-bittinen sanatyyppi. `𝟚²⁵⁶` on 256-bittinen sanatyyppi, joka soveltuu hasheille ja kryptografisille operaatioille.

Käyttämällä kokosummainta vektorioperaatioiden muunnelma määrittelee "ripple carry adderin" monibittisten sanojen yli:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` ottaa kaksi n-bittistä binäärilukua ja yhden bitin carry-inputin ja palauttaa yhden bitin carry-out-lipun ja n-bittisen summan.

#### SHA-256

Määrittelemällä monibittisille sanoille rekursiivisesti aritmeettisia operaatioita — vähennys, kertolasku, jakolasku — sekä bittikohtaisia loogisia operaatioita kuten looginen AND, OR, XOR, ja yhdistämällä näitä toistuvasti, voidaan rakentaa jopa SHA-256:n lohkopakkausfunktio:

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

SHA-256-kompressio on formaalisti määritelty Simplicityllä Rocq-todistusavustimessa (aiemmin Coq), ja sillä on formaali todistus siitä, että `sha256-hash-block`-toteutus on oikea.

Kompressio toimii liian hitaasti raakana Simplicitynä. Jetit suorittavat yleisiä funktioita, kuten SHA-256-kompression, natiivisti. Puhtaat Simplicity-toteutukset toimivat jettien formaaleina spesifikaatioina.

### Optiotyypit

Optiotyypit syntyvät ottamalla summa yksikkötyypin kanssa:

```
Option A ≔ 𝟙 + A
```

Tyyppi `Option A` voidaan kirjoittaa muodossa `A?` tai `𝕊 A` (missä `𝕊` tarkoittaa "seuraajaa"). Funktiot mapataan optiotyyppien yli:

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

Monadisia kombinaattoreita, kuten bind, voidaan määritellä:

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Vaihtuvan pituiset puskurit

"Puskurit" ovat tyyppejä osittain täytetyille vektoreille:

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

Tyyppi `Xᑉ⁸` laajenee muotoon `(1 + X⁴) × ((1 + X²) × (1 + X))`. Kun tätä käsitellään polynomina ja laajennetaan, saadaan `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`. Tyyppinä tulkittuna se edustaa kaikkien mahdollisten X:n tuplejen summaa pituuteen 7 asti, tyhjä tuple mukaan lukien. Tämä on täsmälleen alle 8 pituisien listojen tyyppi.

Vektorien tapaan myös puskureille voidaan määritellä map- ja fold-operaatioita. Pino-operaatioihin kuuluvat `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` ja `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`. `push-<n` lisää alkion puskuriin ja palauttaa täyden vektorin, jos ylivuoto tapahtuu. `pop-<n` poistaa alkion ja palauttaa pienemmän puskurin sekä poistetun alkion, tai valinnaisesti ei mitään, jos alkuperäinen puskuri oli tyhjä.

`push-<n`-määritelmä rekursiivisesti:

```
push-<2 ≔ case (drop (injr (injr iden))) (injl iden)

push-<4 ≔ ((O I H ▵ IH) ⨾ push-<2) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ injl unit)) (injl iden))
               (injr (I H ▵ O H))

push-<8 ≔ ((O I H ▵ IH) ⨾ push-<4) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ (injl unit ▵ injl unit))) (injl iden))
               (injr (I H ▵ O H))

…
```

Raaka Simplicity muuttuu tiettyjen monimutkaisuustasojen jälkeen vaikeaksi seurata. Loppukäyttäjät käyttävät korkeamman tason kieliä, kuten SimplicityHL:ää, jotka tuottavat nämä idiomaattiset lausekkeet.

### Yhteenveto

Tämä luku näytti, miten biteistä rakennetaan loogisia operaatioita. Näistä syntyi bittitason aritmetiikka, joka mahdollistaa suorituksesta päättelyn. Vektorityypit kehitettiin, mikä havainnollisti iterointia monibittisten sanojen yli aritmetiikan määrittämistä varten. Jatkaen kryptografiset operaatiot, kuten SHA-256 ja Schnorr-allekirjoituksen validointi, voidaan määritellä pelkillä Simplicity-kombinaattoreilla — ja ne on kaikki todella määritelty Simplicityllä.

Tämä luku ei ole kattava opas kaikkiin mahdollisiin tietotyyppeihin ja operaatioihin, jotka Simplicityssä voidaan rakentaa, vaan se havainnollistaa käytännöllisen toiminnallisuuden saavuttamista Simplicityn rajoitteiden sisällä. Äärellisesti rajatuista tyypeistä huolimatta voidaan määritellä hyödyllisiä vektoreita, puskurityyppejä ja näiden rakenteiden yli iteroivia operaatioita.

Todellisen standardikirjaston operaatiospesifikaatiot poikkeavat hieman tässä olevista määritelmistä. Esimerkiksi kokosummain käyttää 3-suuntaista XOR:ia ja "enemmistö"-logiikkafunktiota kahden puolisummaimen sijaan.

Käytännössä Simplicity-ohjelmat käyttävät jettejä aritmeettisiin ja kryptografisiin operaatioihin. Jetit kuitenkin korvaavat vain lausekkeita. Puskureiden ja vektorien yli iteroivia kombinaattoreita ei voida korvata jeteillä, ja niitä esiintyy todellisissa Simplicity-ohjelmissa. Vaikka loppukäyttäjät eivät käytä näitä suoraan, he käyttävät korkeamman tason kieliä kuten SimplicityHL:ää, jotka tuottavat tällaisia lausekkeita.

Rekursiivisesti määritellyt kombinaattorit näyttävät kasvavan lausekekooltaan eksponentiaalisesti. Tämä ei ole ongelmallista. Serialisoinnin aikana lausekkeet koodataan DAGeina (suunnattuina syklittöminä graafeina) puiden sijasta. Todellinen esitys kasvaa vain lineaarisesti.

Tähän asti on tarkasteltu vain puhtaita laskentoja. Vuorovaikutus transaktiodatan kanssa, esimerkiksi transaktioiden allekirjoittamista varten, vaatii jonkin tavan saada ohjelmat epäonnistumaan, jos allekirjoitukset ovat virheellisiä. Seuraava luku käsittelee Simplicityn sivuvaikutuksia.

## Kaksi sivuvaikutusta

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

Edellisissä luvuissa näytimme, miten Simplicityn ydinkombinaattorien joukolla rakennetaan joitakin tietorakenteita ja laskentoja. Kuten totesimme, ydinkombinaattorit riittävät toteuttamaan minkä tahansa äärellisen puhtaan laskennan. Tämä herättää kysymyksen: mitä muuta voidaan saavuttaa? Voimme lisätä lausekkeisiimme lisäsivuvaikutuksia.

Lausekkeille on erilaisia mahdollisia sivuvaikutuksia: tilapäivitys, lokiin kirjoittaminen, poikkeuksen heittäminen, ympäristöstä lukeminen, jatkeen kutsuminen jne. Simplicityssä käytettävissä olevat sivuvaikutukset riippuvat sovelluksesta.

Bitcoin- ja Liquid-sovelluksissa meillä on tällä hetkellä kaksi sivuvaikutusta: Failure-vaikutus, joka on poikkeusvaikutus, jossa poikkeuksen tyyppi on `𝟙`, ja Reader-vaikutus, joka mahdollistaa datan lukemisen transaktioympäristöstä. Ydinkombinaattorimme ovat "puhtaita"; niillä ei ole sivuvaikutuksia. Jetit voivat kuitenkin tuoda uusia primitiivejä, joilla on sivuvaikutuksia.

### Jetit vaikutuksilla

Puhumme jeteistä myöhemmin tällä kurssilla lisää, mutta tässä esittelemme muutamia esimerkkijettejä niiden sivuvaikutusten havainnollistamiseksi.

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` on jetti lausekkeelle, joka ottaa x-only-julkisen avaimen, 256-bittisen viestin ja Schnorr-allekirjoituksen, eikä palauta mitään! Tyyppinsä mukaan sen pitäisi käyttäytyä samoin kuin `unit`. Ero on jetin sivuvaikutuksessa: jos allekirjoituksen validointi epäonnistuu, koko laskenta keskeytetään heittämällä poikkeus (yksikkötyyppiä). Tämä on Failure-vaikutus.

#### Verify

`verify : 𝟚 ⊢ 𝟙` on pelkistetty jetti Failure-vaikutuksen ilmaisemiseen. Jos `verify`:n syöte on `false`, koko laskenta keskeytetään heittämällä poikkeus. Jos syöte on `true`, mitään ei palauteta, mutta laskenta voi jatkua.

#### Transaktiohashit

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` näyttää olevan vakiofunktio, koska mahdollisia syötearvoja on vain yksi: tyhjä tuple. Tämä jetti kuitenkin lukee transaktioympäristöstä ja tuottaa transaktiodatasta hashin, joka vastaa Bitcoin Scriptin allekirjoituksen verifioinnissa käytettävää `SIGHASH_ALL`-viestitiivistettä. Tämä on esimerkki Reader-vaikutuksesta: palautettu arvo riippuu transaktioympäristöstä, jossa jetti suoritetaan. On useita muitakin hajautusjettejä, jotka hajauttavat transaktioympäristön datan eri osajoukkoja auttaakseen rakentamaan mukautettuja viestitiivisteitä allekirjoituksia varten.

#### Introspection-jetit

`input-sequence : 𝟚³² ⊢ 𝟚³²?` on funktio, joka ottaa syöteindeksin ja palauttaa transaktion sequence-numeron kyseiselle syötteelle, tai valinnaisesti ei mitään, jos indeksi on rajojen ulkopuolella. Jälleen tulostearvo ei ole puhdas funktio syöteindeksistä, vaan operaatio käyttää Reader-vaikutusta päästäkseen transaktioympäristöön tulostearvon määrittämistä varten. On useita muitakin introspection-jettejä, jotka palauttavat transaktioympäristön datan eri fragmentteja.

### Vaikutusten luokittelu

Kaikki sivuvaikutukset eivät ole samanlaisia. Jotkin sivuvaikutukset käyttäytyvät paremmin kuin toiset. Voimme luokitella vaikutuksia sen mukaan, kuinka hyvin ne soveltuvat ohjelmamuunnoksiin.

#### Kommutatiiviset vaikutukset

Kommutatiivinen vaikutus on sellainen, jossa jos vaihdat kahden lausekkeen tulosteet, voit turvallisesti vaihtaa itse lausekkeet ilman, että lausekkeen vaikutus muuttuu. Tarkastellaan `swap = I H ▵ O H : A × B ⊢ B × A`. Jos `f ▵ g ⨾ swap = g ▵ f` jokaiselle sivuvaikutuksia sisältävälle lausekkeelle `f` ja `g`, vaikutukset ovat kommutatiivisia.

Transaktiodatan lukeminen ympäristöstä on kommutatiivinen vaikutus, koska ympäristöstä lukemisen tulos on sama riippumatta siitä, missä järjestyksessä lukeminen suoritetaan.

Yleisesti poikkeuksen heittäminen ei ole kommutatiivinen vaikutus. Jos `f` heittää jonkin poikkeuksen `e₁` ja `g` heittää jonkin toisen poikkeuksen `e₂`, se, mikä poikkeus `f`:n ja `g`:n parista heitetään, riippuu niiden suoritusjärjestyksestä.

Failure-vaikutuksen erityistapauksessa, jossa voidaan heittää vain yksikkötyyppinen poikkeus, vaikutus on kuitenkin kommutatiivinen. Riippumatta siitä, kumpi `f`:stä tai `g`:stä heittää poikkeuksen, syntyvä poikkeus on sama, koska mahdollisia poikkeusarvoja on vain yksi.

#### Idempotentit vaikutukset

Idempotentti vaikutus on sellainen, jossa jos monistat lausekkeen tulosteen, voit turvallisesti monistaa itse lausekkeen ilman, että lausekkeen vaikutus muuttuu. Tarkastellaan `dup = iden ▵ iden : A ⊢ A × A`. Jos `f ⨾ dup = dup ⨾ f ▵ f` jokaiselle sivuvaikutuksia sisältävälle `f`:lle, vaikutukset ovat idempotentteja.

Transaktiodatan lukeminen ympäristöstä on idempotentti vaikutus. Poikkeuksen heittäminen on myös idempotentti vaikutus. Vaikka vain toinen kahdesta monistetusta lausekkeesta suoritetaan, mikä tahansa `dup ⨾ f ▵ f`:n heittämä poikkeus on sama kuin poikkeus, jonka `f ⨾ dup` heittää.

Lokiin kirjoittaminen ei kuitenkaan välttämättä ole idempotenttia, koska vaikutuksen monistaminen saisi lokiviestin näkymään kahdesti. Jos loki kuitenkin koostuu viestien _joukosta_ eikä viestien _listasta_, vaikutus olisi idempotentti (ja kommutatiivinen), koska joukkoon lisääminen on itsessään idempotentti operaatio.

#### Unitaariset vaikutukset

Unitaarinen vaikutus on sellainen, jossa jos hylkäät lausekkeen tulosteen, voit turvallisesti hylätä itse lausekkeen ilman, että lausekkeen vaikutukset muuttuvat. Jos aina pätee, että `f ⨾ unit = unit` jokaiselle sivuvaikutuksia sisältävälle `f`:lle, vaikutuksesi ovat unitaarisia.

Datan lukeminen ympäristöstä on yksi harvoista unitaaristen vaikutusten tyypeistä. Jos transaktiodatan lukemisen tulos ympäristöstä hylätään, koko lukemisen suorittava lauseke voidaan hylätä.

Failure-vaikutus ei ole unitaarinen. Jos `f` heittää poikkeuksen, niin tekee myös `f ⨾ unit`; suoritus ei edes ehdi `unit`-kombinaattoriin ennen kuin laskenta keskeytetään. Toisaalta `unit` ei ilmeisesti heittäisi mitään poikkeusta, joten `f ⨾ unit`:n ja `unit`:in vaikutukset olisivat erilaisia.

Yhteenvetona tässä on, miten yllä käsitellyt vaikutukset pärjäävät näiden kolmen ominaisuuden suhteen:

| Vaikutus | Kommutatiivinen | Idempotentti | Unitaarinen |
| --- | :---: | :---: | :---: |
| Reader (transaktioympäristö) | ✓ | ✓ | ✓ |
| Failure (yksikkötyyppinen poikkeus) | ✓ | ✓ | ✗ |
| Writer (loki joukkona) | ✓ | ✓ | ✗ |
| Yleiset poikkeukset (mielivaltainen tyyppi) | ✗ | ✓ | ✗ |

### Simplicityssä sallitut vaikutukset

Mitä paremmin käyttäytyviä ominaisuuksia vaikutustyypillä on, sitä enemmän tilaa Simplicity-optimoijalla on muuntaa ohjelmia, jotka käyttävät kyseisiä vaikutuksia. Ihanteellisesti sallisimme vain vaikutuksia, joilla on kaikki kolme ominaisuutta: kommutatiivisuus, idempotenttius ja unitaarisuus. Tämä antaisi optimoijan tehdä millaisia ohjelmamuunnoksia tahansa. Ympäristöstä lukeminen on kuitenkin ainoa vaikutus, joka täyttää kaikki kolme ominaisuutta.

Sen sijaan vaadimme, että Simplicity-vaikutukset ovat kommutatiivisia ja idempotentteja. Molemmat Simplicityssä käyttämämme vaikutukset, Failure-vaikutus ja Reader-vaikutus, ovat kommutatiivisia ja idempotentteja. Tämä mahdollistaa suuren joukon optimointeja Simplicity-koodille.

Edellä kuvattu "hylkää"-muunnos, jossa yritetään korvata `f ⨾ unit` `unit`:lla, tai mikään vastaava muunnos, ei kuitenkaan ole sallittu, jos `f` voi tuottaa Failure-vaikutuksen. Kuvittele esimerkiksi, että `f` sisältäisi `bip0340-verify`-väitteen. Olisi katastrofaalista yrittää optimoida tuo tarkistus pois.

### Miksi sallia sivuvaikutuksia lainkaan?

Miksi Simplicity edes sallii sivuvaikutuksia lainkaan? Eikö olisi parempi, jos jokainen ohjelma ottaisi koko transaktion syötteeksi ja palauttaisi Boolen tulosteen, joka päättää, onko transaktio kelvollinen vai ei?

#### Erävalidointi

Yksi syy Failure-vaikutukselle on tukea Schnorr-allekirjoitusten [erävalidointia](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification). Erävalidoinnissa monet yksittäiset Schnorr-allekirjoitustarkistukset yhdistetään niin, että jos yksikin allekirjoitustarkistus epäonnistuu, koko erä epäonnistuu.

Tämä erämenettely parantaa tehokkuutta verrattuna kunkin allekirjoituksen erilliseen verifiointiin. Haittapuoli on, että jos erävalidointi epäonnistuu, emme saa tietää, mikä nimenomainen allekirjoitustarkistus tai mitkä tarkistukset epäonnistuivat.

Käyttämällä failure-sivuvaikutusta `bip0340-verify` varmistaa, että jos allekirjoitustarkistus epäonnistuu, koko transaktio epäonnistuu. Jos `bip0340-verify` sen sijaan palauttaisi onnistumista tai epäonnistumista varten `𝟚`:n, Boolen tyypin, epäonnistunut allekirjoitustarkistus voisi silti johtaa haaraan, jossa skripti onnistuu. Tällaisessa tapauksessa meidän pitäisi tietää, onko kyseinen allekirjoitus kelvollinen vai ei, emmekä siten voisi hyödyntää erävalidointia.

#### Esilaskettu transaktiodata

Varhaisen Bitcoin Scriptin ongelma oli, että allekirjoitusten viestitiivisteiden luomiseen käytetty hajautusfunktio oli lineaarinen transaktion koon suhteen. Tyypillisesti jokainen syöte luo vähintään yhden viestitiivisteen allekirjoituksen verifiointia varten, joten hajautuksen kokonaismäärä oli kvadraattinen transaktion koon suhteen.

Tämä ongelma korjattiin Segwitissä ja Bitcoin Scriptin myöhemmissä iteraatioissa määrittelemällä viestitiivisteet uudelleen niin, että ne voitiin laskea vakioajassa allekirjoitustarkistusta kohden. Tämä nojaa `PrecomputedTransactionData`:an, joka esilaskee transaktiodatan hashit kerran ja jaetaan sitten kunkin syötteen sighash-laskennoille. Simplicityn transaktiohajautusjetit nojaavat samanlaiseen esilaskettuun transaktiodataan varmistaakseen, että jetit toimivat vakioajassa.

Oletetaan, ettei `sig-all-hash` käyttäisi Reader-vaikutusta. Oletetaan, että jotenkin onnistuisimme rakentamaan Simplicity-tyypin transaktioympäristölle. Kutsutaan sitä `TxEnv`:ksi, jolloin jetin tyyppi olisi `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶`. Tällainen määritelmä vaatisi, että `sig-all-hash`-jetti pystyisi laskemaan minkä tahansa transaktion hashin, ei vain sen transaktion, johon se osallistuu. Simplicity-ohjelmat voisivat kopioida annetun `TxEnv`:n ja välittää muokatun kopion siitä `sig-all-hash`:lle. Tällöin `sig-all-hash` ei voisi nojata `PrecomputedTransactionData`:an, ja olisimme taas tilanteessa, jossa vaaditaan lineaarinen aika suhteessa mihin tahansa transaktiodataan, joka välitetään tälle `sig-all-hash`:n versiolle.

Koska `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` käyttää Reader-vaikutusta päästäkseen transaktiodataan, se saa pääsyn _vain_ kiinteään transaktioympäristöön. Tästä syystä jetin toteutus voi turvallisesti käyttää `PrecomputedTransactionData`:a ja toimia vakioajassa.

### Cross-input signature aggregation

Vaikka Liquid eikä Bitcoin tue tällä hetkellä [cross-input signature aggregationia](https://hrf.org/latest/cisa-research-paper/), haluamme tarkistaa, että Simplicity voi olla yhteensopiva sen kanssa, kun aika tulee.

Vaikka yksityiskohtia ei ole vielä selvitetty, kuvittelemme half-aggregationin toteutettavan Writer-vaikutuksella. Toisin sanoen uusi jetti, jonka tyyppi olisi esimerkiksi `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙`, ottaisi julkisen avaimen, viestitiivisteen ja Schnorr-allekirjoituksen `r`-komponentin (Schnorr-allekirjoitus koostuu `r`-komponentista ja `s`-komponentista) ja kirjoittaisi sen transaktiolokiin ennen suorituksen jatkamista. Sitten muualla transaktiossa tai transaktion mukana tarjottaisiin aggregoitu `s`-komponentti kaikille puoliksi aggregoiduille Schnorr-allekirjoituksille. Transaktio olisi kelvollinen vain silloin, kun tällainen aggregoitu `s`-komponentti tarjotaan kaikille lokitetuille avaimille, viesteille ja `r`-komponenteille.

Täyttääkseen Simplicityn vaatimukset tämän Writer-vaikutuksen täytyy olla idempotentti ja kommutatiivinen. Tämä voidaan varmistaa käsittelemällä writer-lokia avaimen, viestin ja `r`-komponentin tuplejen joukkona. Tämä toimii, koska joukko-operaatiot ovat idempotentteja ja kommutatiivisia. Lokin käsitteleminen arvojen joukkona olisi yhteensopivaa half-aggregation-verifiointialgoritmin kanssa.

### Yhteenveto

Tässä luvussa tarkastelimme sivuvaikutusten lisäämistä laskentoihin, joita Simplicity voi tehdä. Luokittelimme erilaisia vaikutuksia sen mukaan, kuinka hyvin ne käyttäytyvät erilaisten ohjelmamuunnosten suhteen. Päätimme rajoittaa Simplicityn vaikutukset niihin, jotka ovat kommutatiivisia ja idempotentteja.

Bitcoin- ja Liquid-sovelluksissa käytämme kahta vaikutusta: Reader-vaikutusta transaktioympäristöön pääsemiseen ja Failure-vaikutusta ohjelman keskeyttämiseen ja epäonnistuttamiseen. Jotkin jetit käyttävät primitiivioperaatioita, joissa tällaisia sivuvaikutuksia voi esiintyä.

Failure-vaikutus määrittää Simplicity-ohjelman tulosteen: ohjelma joko epäonnistuu, jolloin transaktio on virheellinen, tai ohjelma onnistuu. Reader-vaikutus tarjoaa yhdenlaisen syötteen Simplicity-ohjelmalle: transaktiodataa sisältävän ympäristön. Mutta meidän täytyy tarjota Simplicity-ohjelmille myös muita syötteitä, kuten digitaalisia allekirjoituksia.

Seuraavassa luvussa tarkastelemme, mitä Simplicity-ohjelmat ovat, miten ne muutetaan osoitteiksi ja miten lisäämme Simplicity-ohjelmiin muita syötteitä, kuten allekirjoituksia.

## Ohjelmat ja osoitteet

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

Edellisessä luvussa kuvasimme kaksi Simplicityssä käytettyä sivuvaikutusta: Failure-vaikutuksen, joka määrittää ohjelman onnistumisen tai epäonnistumisen, ja Reader-vaikutuksen, joka tarjoaa pääsyn transaktioympäristöön. Nyt siirrymme käytännön kysymykseen: mikä tarkalleen on Simplicity-ohjelma, ja miten siitä tulee osoite blockchainissa?

### Simplicity-ohjelmat

Simplicity-ohjelma määritellään Simplicity-lausekkeeksi, jonka tyyppi on `𝟙 ⊢ 𝟙`. Tämä tyyppisignatuuri tarkoittaa, että ohjelma ei ota merkityksellistä syötettä (vain yksikköarvon) eikä tuota merkityksellistä tulostetta (vain yksikköarvon). Reader-vaikutus kaappaa transaktioympäristön syötteen, kun taas Failure-vaikutus osoittaa onnistumisen tai epäonnistumisen. Nämä vaikutukset käsittelevät I/O:ta eivätkä itse Simplicity-tyyppejä.

### Commitment Merkle Root

Sen sijaan, että täydellisiä ohjelmia tallennettaisiin on-chain, Bitcoin käyttää sitoumuksia — käytäntöä, joka ulottuu Pay-to-Script-Hashista (P2SH). Simplicity käyttää Commitment Merkle Rootia (CMR).

Jokainen kombinaattori saa SHA-256-tagin, joka johdetaan mallista: `Simplicity␟Commitment␟[identifier]`, missä `␟` edustaa ASCII-koodia 31 (yksikköerotin).

Jokainen tagi on alla luetellun vastaavan esikuvamerkkijonon SHA-256-hash:

| Kombinaattori | Tagin esikuva (ASCII-merkkijono) |
|---|---|
| `iden` | `Simplicity␟Commitment␟iden` |
| `unit` | `Simplicity␟Commitment␟unit` |
| `comp` | `Simplicity␟Commitment␟comp` |
| `pair` | `Simplicity␟Commitment␟pair` |
| `case` | `Simplicity␟Commitment␟case` |
| `take` | `Simplicity␟Commitment␟take` |
| `drop` | `Simplicity␟Commitment␟drop` |
| `injl` | `Simplicity␟Commitment␟injl` |
| `injr` | `Simplicity␟Commitment␟injr` |

Simplicity-lauseke hajautetaan sitten rekursiivisesti 256-bittiseksi CMR:ksi laskemalla tagattu SHA-256-midstate kullekin kombinaattorille yhdessä sen argumenttien CMR:ien kanssa (kirjoitetaan `#ᶜ(e)` lausekkeen `e` CMR:lle ja `∥` tavukonkatenoinnille):

| Kombinaattori | CMR-sääntö |
|---|---|
| `iden` | `#ᶜ(iden) = SHA-256-midstate(tag_iden ∥ tag_iden)` |
| `unit` | `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)` |
| `comp f g` | `#ᶜ(comp f g) = SHA-256-midstate(tag_comp ∥ tag_comp ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `pair f g` | `#ᶜ(pair f g) = SHA-256-midstate(tag_pair ∥ tag_pair ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `case f g` | `#ᶜ(case f g) = SHA-256-midstate(tag_case ∥ tag_case ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `take f` | `#ᶜ(take f) = SHA-256-midstate(tag_take ∥ tag_take ∥ 32·0x00 ∥ #ᶜ(f))` |
| `drop f` | `#ᶜ(drop f) = SHA-256-midstate(tag_drop ∥ tag_drop ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injl f` | `#ᶜ(injl f) = SHA-256-midstate(tag_injl ∥ tag_injl ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injr f` | `#ᶜ(injr f) = SHA-256-midstate(tag_injr ∥ tag_injr ∥ 32·0x00 ∥ #ᶜ(f))` |

Binääriset kombinaattorit (`comp`, `pair`, `case`) konkatenoivat molempien lasten CMR:t; unaariset kombinaattorit (`take`, `drop`, `injl`, `injr`) konkatenoivat ainoan lapsensa CMR:n 32 tavun `0x00`-täytteen jälkeen; ja nolla-ariteettiset lehdet (`iden`, `unit`) hajauttavat pelkän taginsa. Kaksi käytäntöä pitää tämän halpana laskea: SHA-256-midstateja käytetään niin, että **jokainen lauseke vaatii enintään yhden kutsun SHA-256-kompressiofunktioon** (olettaen, että vakio tageihin asti oleva midstate on esilaskettu), ja yhden argumentin konstruktorit prefiksoivat argumenttinsa 32 tavulla `0x00`-täytettä, mikä mahdollistaa hieman lisäesilaskentaa toteutuksille, jotka sitä haluavat.

`unit`-kombinaattorille — nolla-ariteettiselle konstruktorille, jolla ei ole argumenttialilausekkeita — tämä sääntö erikoistuu muotoon `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`, missä `tag_unit = SHA-256(Simplicity␟Commitment␟unit)` (tagi syötetään kahdesti). Triviaalin `unit`-ohjelman tuloksena oleva CMR on:

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

Kriittisesti CMR ei sitoudu Simplicity-lausekkeiden tyyppeihin, vaan luottaa tyyppipäättelyyn lunastuksen aikana.

### Osoitteet

Osoitteet käyttävät BIP-0341:n Taproot-mekanismia, jossa CMR:t sitoutetaan TapLeaf-version `0xbe` alle. Prosessi sisältää:

1. TapLeaf-tagatun hashin laskemisen yhdistämällä versiotavu, CMR:n pituus ja CMR itse
2. Sisäisen julkisen avaimen tweakkaamisen (käyttäen NUMS-pistettä, kun key-spend-polku ei ole toivottu)
3. Muuntamisen bech32m-muotoon
4. Asianmukaisten tarkistussummien lisäämisen

Kun key-spend-polkua ei haluta, sisäinen julkinen avain asetetaan **NUMS** ("Nothing-Up-My-Sleeve") -pisteeksi: käyräpisteeksi, joka on tarkoituksella valittu niin, ettei kukaan tiedä sen diskreettiä logaritmia — toisin sanoen pisteeksi, jolla ei ole vastaavaa yksityistä avainta. Koska kukaan ei voi koskaan tuottaa sille allekirjoitusta, key-spend-polku on todistettavasti käyttökelvoton, ja output voidaan käyttää *vain* sitoutetun Simplicity-skriptipolun kautta. Todellisessa sovelluksessa tämä NUMS-piste pitäisi satunnaistaa BIP-0341:n suosituksen mukaisesti, jotta outputit ilman key-spend-polkua ovat erottamattomia tavallisista Taproot-outputeista (yksityisyyshyöty).

#### Simplicitystä osoitteeksi

Käydään läpi koko johto yksinkertaisimmalle mahdolliselle ohjelmalle: `unit : 𝟙 ⊢ 𝟙`, no-op, joka aina onnistuu.

**1. Kombinaattoritagi.** Laske ensin `unit`-tagi:

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Syötä tagi kahdesti saadaksesi ohjelman CMR:n:

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. TapLeaf-hash.** Prefiksoi CMR Simplicityn TapLeaf-versiolla `0xbe` ja CMR-pituudella `0x20` (32 tavua), ja ota sitten Elements TapLeaf -tagattu hash (tagattu hash on `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`):

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

Kun lehtiä on vain tämä yksi, TapBrancheja ei ole, joten tämä hash on jo TapTree-juuri.

**4. TapTweak.** Koska emme halua key-spend-polkua, käytämme BIP-0341 NUMS -pistettä sisäisenä avaimena ja tweakkaamme sitä TapTree-juurella:

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Output-avain.** Tweakkaa sisäistä avainta käyrällä, `output_pk = lift_x(internal_pk) ⊕ t·G` (elliptisen käyrän aritmetiikka on tässä tiivistetty), jolloin saadaan x-only-output-avain `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09`.

**6. Bech32m-osoite.** Koodaa x-only-output-avain, prefiksoi `p` (SegWit v1 -witness-version merkki), lisää Liquid-testnetin ihmisen luettava prefiksi `tex1` ja liitä Bech32m-tarkistussumma. Lopullinen osoite on:

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

Siinä oli paljon työtä — mutta suuri osa siitä on Taprootin itsensä vaatimaa, ei Simplicityn.

### Witness-lausekkeet

Uusi kombinaattorityyppi vastaa Simplicity-ohjelmien syötteen puuttumiseen: witness-lauseke. `witness`-kombinaattori sallii allekirjoitusdatan ja muun witness-materiaalin integroinnin ohjelmiin.

```
      w : B
-----------------
witness w : A ⊢ B
```

Witness-lausekkeen semantiikka on suoraviivainen: se ohittaa syötteensä ja palauttaa yksinkertaisesti arvon `w` (joka voi olla mitä tahansa Simplicity-tyyppiä), eli `⟦witness w⟧(a) = w`. Tämä ei lisää **mitään uutta ilmaisuvoimaa** — täydellisyyslauseen mukaan Simplicity voi jo rakentaa minkä tahansa tällaisen vakiofunktion (muista edellisten lukujen `scribe`-makro). `witness`-kombinaattorin pointti on kokonaan sen **CMR:ssä**: arvo `w` **suljetaan pois** lausekkeen CMR:stä, joten osoite voidaan laskea ennen kuin `w` tunnetaan, ja `w` annetaan lunastushetkellä.

Tämä suunnitteluvalinta tukee karsimista — suorittamattomia ehdollisia haaroja ei tarvitse paljastaa on-chain, mukaan lukien niihin liittyvät witness-lausekkeet. Kun haara karsitaan, verifioija tarvitsee vain karsitun alipuun CMR:n, ei sen todellista sisältöä.

### Witness-arvot

Voi vaikuttaa rajoitukselta, että witness-lauseke voi sisältää vain *arvon*, eikä yleisempää Simplicity-lauseketta. Mutta UTXO-pohjaisten blockchainien ohjelmat suoritetaan vain kerran. Kokonaista alilauseketta ei tarvitse välittää witness-solmuun: käyttäjä voi yksinkertaisesti ajaa kyseisen alilausekkeen itse off-chain ja transkriboida sen tulosteen witness-arvoksi saadakseen täsmälleen saman tuloksen.

(Myöhemmin tällä kurssilla kohtaamme `disconnect`-kombinaattorin, joka käyttäytyy paljon kuin witness-lauseke, joka *todella* ottaa kokonaisen Simplicity-lausekkeen argumentikseen.)

Vaihtoehtoinen suunnittelu syöttäisi kaiken witness-datan argumenttina ylätason Simplicity-ohjelmaan. Witness-lausekkeita suositaan kahdesta syystä. Ensinnäkin **karsiminen**: `case`-lausekkeiden suorittamattomia haaroja ei koskaan paljasteta on-chain, ja kaikki näiden haarojen sisällä olevat witness-lausekkeet karsitaan pois niiden mukana. Toiseksi **paikallisuus**: witness-lausekkeet antavat sijoittaa kunkin witness-arvon täsmälleen sinne, missä sitä käytetään, sen sijaan että sitä pujotettaisiin alas ohjelman ylätason syötteestä.

### Tyyppipäättely

Koska CMR:t eivät sitoudu tyyppeihin, tyyppijärjestelmä rakennetaan uudelleen lunastuksen aikana. Simplicityn tyyppipäättelyalgoritmi määrittää minimaaliset tyypit kullekin alilausekkeelle kombinaattorirakenteen perusteella. Tarkemmin sanottuna päättely laskee jokaisen alilausekkeen *päätyypin* (yleisimmän tyypin); jäljelle jäävät vapaat tyyppimuuttujat instansioidaan sitten yksikkötyypiksi `𝟙`, mikä tuottaa ohjelmalle yksikäsitteisen, minimaalisen tyypin.

### Yhteenveto

Tässä luvussa vahvistimme, että Simplicity-ohjelmat ovat tyypin `𝟙 ⊢ 𝟙` lausekkeita, selitimme, miten Commitment Merkle Rootit rakennetaan kunkin kombinaattorin tagatuista SHA-256-hasheista, ja näytimme, miten CMR:t muutetaan on-chain-osoitteiksi BIP-0341 Taprootin kautta. Esittelimme witness-lausekkeet mekanismina allekirjoitusdatan ja muiden syötteiden tarjoamiseen käyttöhetkellä ilman, että niiden arvoihin sitoudutaan osoitteen luontihetkellä.

# Loppuosio

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## Arvostelut ja arviot

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## Loppukoe

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## Yhteenveto

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>
