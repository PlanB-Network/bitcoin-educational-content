---
name: Johdanto Bitcoinin kryptografisiin algoritmeihin
goal: Ymmärrä Bitcoin-lompakon luominen kryptografisesta näkökulmasta
objectives:
  - Selkeytä Bitcoiniin liittyvää kryptografian terminologiaa.
  - Hallitse Bitcoin-lompakon luominen.
  - Ymmärrä Bitcoin-lompakon rakenne.
  - Ymmärrä osoitteet ja johdannaispolut.
---

# Matka kryptografian syövereihin

Oletko lumoutunut Bitcoinista? Mietitkö, miten Bitcoin-lompakko toimii? Valmistaudu kiehtovalle matkalle kryptografian maailmaan! Loïc, asiantuntijamme, johdattaa sinut Bitcoin-lompakon luomisen mutkikkaisiin yksityiskohtiin, selvittäen pelottavilta vaikuttavien teknisten termien, kuten hajautus, avainjohdannaiset ja elliptiset käyrät, mysteerit.

Tämä koulutus ei ainoastaan varusta sinua tietämyksellä ymmärtääksesi Bitcoin-lompakon rakenteen, vaan myös valmistaa sinut sukeltamaan syvemmälle kryptografian jännittävään maailmaan. Oletko valmis lähtemään tälle matkalle? Liity seuraamme ja muuta uteliaisuutesi asiantuntemukseksi!

+++

# Johdanto
<partId>32960669-d13a-592f-a053-37f70b997cbf</partId>

## Johdatus kryptografiaan
<chapterId>fb4e8857-ea35-5a8a-ae8a-5300234e0104</chapterId>

### Onko tämä koulutus sinua varten? KYLLÄ!

Olemme iloisia voidessamme toivottaa sinut tervetulleeksi uudelle kurssille nimeltä "Crypto 301: Johdatus kryptografiaan ja HD-lompakkoon", jonka pitää alansa asiantuntija Loïc Morel. Tämä kurssi vie sinut kryptografian kiehtovaan maailmaan, matematiikan perusalaan, joka varmistaa tietojesi salauksen ja turvallisuuden.

Päivittäisessä elämässämme, ja erityisesti Bitcoinin alueella, kryptografialla on ratkaiseva rooli. Kryptografiaan liittyvät käsitteet, kuten yksityiset avaimet, julkiset avaimet, osoitteet, johdannaispolut, siemen ja entropia, ovat keskeisiä Bitcoin-lompakon käytössä ja luomisessa. Kurssin aikana Loïc selittää yksityiskohtaisesti, miten yksityiset avaimet luodaan ja miten ne liittyvät osoitteisiin. Loïc omistaa myös tunnin elliptisten käyrien matemaattisten yksityiskohtien selittämiseen. Lisäksi ymmärrät, miksi HMAC SHA512:n käyttö on tärkeää lompakkosi turvaamisessa ja mikä ero on siemenen ja mnemonisen lauseen välillä.
Tämän koulutuksen lopullisena tavoitteena on mahdollistaa sinun ymmärtää tekniset prosessit, jotka ovat mukana HD-lompakon luomisessa, ja käytetyt kryptografiset menetelmät. Vuosien varrella Bitcoin-lompakot ovat kehittyneet helpommin käytettäviksi, turvallisemmiksi ja standardoiduiksi kiitos tiettyjen BIPien. Loïc auttaa sinua ymmärtämään nämä BIPit käsittääksesi Bitcoin-kehittäjien ja kryptografien tekemät valinnat. Kuten kaikki yliopistomme tarjoamat koulutukset, tämäkin on täysin ilmainen ja avoimen lähdekoodin. Tämä tarkoittaa, että voit ottaa sen ja käyttää sitä haluamallasi tavalla. Odotamme innolla palautettasi tämän jännittävän kurssin päätteeksi.

### Puheenvuoro on sinun, professori!

Hei kaikki, olen Loïc Morel, oppaanne tässä teknisessä tutkimusmatkassa Bitcoin-lompakoiden käyttämään kryptografiaan.

Matkamme alkaa sukelluksella kryptografisten hajautusfunktioiden syvyyksiin. Yhdessä pureudumme SHA256:n olennaiseen sisältöön ja tutkimme erilaisia johdannaisalgoritmeja.

Jatkamme seikkailuamme purkamalla digitaalisten allekirjoitusten mystisen maailman. Löydätte, miten elliptisten käyrien taika soveltuu näihin allekirjoituksiin, ja valaisemme, miten julkinen avain lasketaan yksityisestä avaimesta. Ja tietenkin, syvennymme digitaalisen allekirjoituksen prosessiin.
Seuraavaksi palaamme ajassa taaksepäin tutkiaksemme Bitcoin-lompakoiden kehitystä, ja sukellamme entropian ja satunnaislukujen käsitteisiin. Käymme läpi kuuluisan mnemonisen lauseen samalla kun kosketamme salasanaa. Sinulla on jopa mahdollisuus kokea jotain ainutlaatuista luomalla siemen 128 nopanheitosta!
Näiden vankkojen perusteiden avulla olemme valmiita ratkaisevaan osaan: Bitcoin-lompakon luomiseen. Siemenen syntymästä ja pääavaimesta, laajennettujen avainten tutkimiseen ja lapsiavainparien johdannaisiin, jokainen vaihe puretaan osiin. Keskustelemme myös lompakon rakenteesta ja johdannaispoluista.

Kaiken huipuksi päätämme matkamme tutkimalla Bitcoin-osoitteita. Selitämme, miten ne luodaan ja miten ne ovat olennaisen tärkeitä Bitcoin-lompakoiden toiminnassa.

Liity mukaan tälle kiehtovalle matkalle, ja valmistaudu tutkimaan kryptografian maailmaa aivan uudella tavalla. Jätä ennakkokäsityksesi oven ulkopuolelle ja avaa mielesi uudelle tavalle ymmärtää Bitcoin ja sen perusrakenne.

# Hajasfunktiot
<partId>3713fee1-2ec2-512e-9e97-b6da9e4d2f17</partId>

## Johdanto kryptografisiin hajasfunktioihin liittyen Bitcoiniin
<chapterId>dba011f5-1805-5a48-ac2b-4bd637c93703</chapterId>

Tervetuloa tämän päivän istuntoon, joka on omistettu syvälle sukeltamiselle kryptografian maailmaan hajasfunktioiden osalta, mikä on keskeinen kulmakivi Bitcoin-protokollan turvallisuudessa. Kuvittele hajasfunktio äärimmäisen tehokkaaksi kryptografiseksi dekoodausrobotiksi, joka muuntaa minkä tahansa kokoisen tiedon ainutlaatuiseksi ja kiinteän kokoiseksi digitaaliseksi sormenjäljeksi, jota kutsutaan "hashiksi", "digestiksi" tai "tarkistussummaksi".
Yhteenvetona, hajasfunktio ottaa syötteenä mielivaltaisen kokoisen viestin ja muuntaa sen kiinteän kokoiseksi ulostulosormenjäljeksi.

Kryptografisten hajasfunktioiden profiilin kuvaaminen vaatii kahden olennaisen ominaisuuden ymmärtämistä: niiden peruuttamattomuuden ja väärentämisen vastustuskyvyn.

Peruuttamattomuus, tai preimage-vastustuskyky, tarkoittaa sitä, että ulostulon laskeminen syötteen perusteella on helppoa, mutta syötteen laskeminen ulostulon perusteella on mahdotonta.
Se on yksisuuntainen funktio.

![image](assets/image/section1/0.webp)

Väärentämisen vastustuskyky johtuu siitä, että jopa pienin muutos syötteessä johtaa merkittävästi erilaiseen ulostuloon.
Nämä funktiot mahdollistavat ladatun ohjelmiston eheyden varmistamisen.

![image](assets/image/section1/1.webp)

Toinen niiden keskeinen ominaisuus on niiden vastustuskyky törmäyksille ja toisen preimageille. Törmäys tapahtuu, kun kaksi erillistä syötettä tuottaa saman ulostulon.
Todellakin, hajautusuniversumissa törmäykset ovat väistämättömiä, mutta erinomainen kryptografinen hajasfunktio minimoi ne merkittävästi. Riskin on oltava niin pieni, että sitä voidaan pitää merkityksettömänä. Se on kuin jokaisella hashilla olisi ainutlaatuinen osoite valtavassa kaupungissa; huolimatta valtavasta määrästä taloja, hyvä hajasfunktio varmistaa, että jokaisella talolla on ainutlaatuinen osoite.

Toisen preimagen vastustuskyky riippuu törmäysten vastustuskyvystä; jos on vastustuskyky törmäyksille, silloin on vastustuskyky toiselle preimagelle.
Annetaan syötetieto, joka on meille määrätty, meidän on löydettävä toinen syöte, erilainen kuin ensimmäinen, joka tuottaa törmäyksen funktion ulostulohashissa. Toisen preimagen vastustuskyky on samankaltainen kuin törmäysten vastustuskyky, paitsi että syöte on määrätty.
Käsitellään nyt vanhentuneiden hajautusfunktioiden myrskyisiä vesiä. SHA0, SHA1 ja MD5 pidetään nykyään ruosteisina kuorina kryptografisen hajautuksen valtameressä. Niitä suositellaan välttämään, koska ne ovat menettäneet vastustuskykynsä törmäyksille. Lokeroperiaate selittää, miksi törmäysten välttäminen on mahdotonta, huolimatta parhaista ponnisteluistamme, johtuen tuloksen koon rajoituksesta. Jotta hajautusfunktiota voidaan pitää turvallisena, sen on kestettävä törmäyksiä, toisen kuvan esikuvia ja esikuvia.

Bitcoin-protokollan keskeinen elementti, SHA-256 hajautusfunktio, on laivan kapteeni. Muita funktioita, kuten SHA-512, käytetään johdannaisiin HMAC:n ja PBKDF:n kanssa. Lisäksi RIPMD160:tä käytetään sormenjäljen pienentämiseen 160 bittiin. Kun viittaamme HASH256:een ja HASH160:een, tarkoitamme SHA-256:n ja RIPMD:n kaksinkertaista hajautusta.

HASH256:ssa on viestin kaksinkertainen hajautus käyttäen SHA256-funktiota.
$$
SHA256(SHA256(viesti))
$$
HASH160:ssa on viestin kaksinkertainen hajautus käyttäen ensin SHA256:ta, sitten RIPMD160:tä.
$$
RIPMD160(SHA256(viesti))
$$
HASH160:n käyttö on erityisen edullista, koska se mahdollistaa SHA-256:n turvallisuuden säilyttämisen samalla kun sormenjäljen kokoa pienennetään.

Yhteenvetona kryptografisen hajautusfunktion lopullinen tavoite on muuntaa mielivaltaisen kokoinen tieto kiinteän kokoiseksi sormenjäljeksi. Jotta sitä voidaan pitää turvallisena, sen on oltava useita vahvuuksia: peruuttamattomuus, väärentämisen kestävyys, törmäysten kestävyys ja toisen kuvan esikuvien kestävyys.

![kuva](assets/image/section1/2.webp)

Tämän tutkimuksen lopussa olemme selvittäneet kryptografisten hajautusfunktioiden mysteerejä, korostaneet niiden käyttöä Bitcoin-protokollassa ja pureutuneet niiden tiettyihin tavoitteisiin. Olemme oppineet, että jotta hajautusfunktioita voidaan pitää turvallisina, niiden on kestettävä esikuvia, toisen kuvan esikuvia, törmäyksiä ja väärentämistä. Olemme myös käsitelleet Bitcoin-protokollassa käytettyjen eri hajautusfunktioiden valikoimaa. Seuraavassa istunnossamme syvennymme SHA256-hajautusfunktion ytimeen ja löydämme kiehtovan matematiikan, joka antaa sille sen ainutlaatuiset ominaisuudet.

## SHA256:n sisäinen toiminta
<chapterId>905eb320-f15b-5fb6-8d2d-5bb447337deb</chapterId>

Tervetuloa jatkamaan kiehtovaa matkaamme kryptografisten hajautusfunktioiden sokkeloissa. Tänään paljastamme SHA256:n mysteerit, monimutkaisen mutta nerokkaan prosessin, jonka esittelimme aiemmin.

Muistutuksena SHA256-hajautusfunktion tarkoitus on ottaa mikä tahansa kokoinen syöteviesti ja tuottaa 256-bittinen hajautus tuloksena.

### Esikäsittely

Mennään askel pidemmälle tässä labyrintissä aloittamalla SHA256:n esikäsittelyllä.

#### Täyttöbitit

Tämän ensimmäisen vaiheen tavoitteena on saada viesti tasattua 512 bitin monikertaiseksi. Tämän saavuttamiseksi lisäämme viestiin täyttöbittejä.

Olkoon M alkuperäisen viestin koko.
Olkoon 1 bitti varattu erotinmerkille.
Olkoon P täyttöbittien määrä ja 64 bittiä varattu toiseen esikäsittelyvaiheeseen.
Kokonaisuuden tulisi olla 512 bitin monikertainen, jota edustaa n.

![kuva](assets/image/section1/3.webp)

Esimerkki 950 bitin syöteviestillä:

```
Vaihe 1: Määritä koko; lopullinen haluttu bittien määrä.
Ensimmäinen 512:n monikerta, joka on suurempi kuin (M + 64 + 1) (missä M = 950), on 1024. 1024 = 2 * 512
Joten n = 2.

Vaihe 2: Määritä P, tarvittavien täyttöbittien määrä, jotta saavutetaan haluttu lopullinen bittien määrä.
-> M + 1 + P + 64 = n * 512
-> M + 1 + P + 64 = 2 * 512
-> 950 + 1 + P + 64 = 1024
-> P = 1024 - 1 - 64 - 950
-> P = 9

Näin ollen viestiin on lisättävä 9 täyttöbittiä, jotta viestin pituus saadaan tasattua 512:n monikertaiseksi.

Ja nyt?
Alkuperäisen viestin jälkeen lisätään erotin 1, jonka perään tulee P, tässä esimerkissä yhdeksän 0:aa.

```
viesti + 1 000 000 000
```

#### Koon Täyttö

Siirrymme nyt esikäsittelyn toiseen vaiheeseen, joka sisältää alkuperäisen viestin koon bittiesityksen lisäämisen.

Käydään läpi esimerkki 950 bitin syötteellä:

```
Luvun 950 binääriesitys on: 11 1011 0110

Käytämme edellisessä vaiheessa varattuja 64 bittiä. Lisäämme nollia, jotta saamme 64 bittiä täyteen tasattua syötettämme varten. Sen jälkeen yhdistämme alkuperäisen viestin, täyttöbitit ja koon täytön saadaksemme tasatun syötteen.
```

Tässä on tulos:

![kuva](assets/image/section1/4.webp)

### Käsittely

#### Ymmärryksen Edellytykset

##### Vakiot ja Alustusvektorit

Valmistaudumme nyt SHA-256 -funktion käsittelyn alkuvaiheisiin. Kuten hyvässä reseptissä, tarvitsemme joitakin perusaineosia, joita kutsutaan vakioiksi ja alustusvektoreiksi.

Alustusvektorit, A:sta H:een, ovat ensimmäisten 8 alkuluvun neliöjuurten desimaaliosien ensimmäiset 32 bittiä. Ne toimivat perusarvoina alkukäsittelyn vaiheissa. Niiden arvot ovat heksadesimaalimuodossa.

Vakiot K, 0:sta 63:een, edustavat ensimmäisten 64 alkuluvun kuutiojuurten desimaaliosien ensimmäiset 32 bittiä. Niitä käytetään jokaisella puristusfunktion kierroksella. Niiden arvot ovat myös heksadesimaalimuodossa.

![kuva](assets/image/section1/5.webp)

##### Käytetyt Operaatiot

Puristusfunktion sisällä käytämme tiettyjä operaattoreita kuten XOR, AND ja NOT. Käsittelemme bitit yksi kerrallaan niiden sijainnin mukaan käyttäen XOR-operaattoria ja totuustaulua. AND-operaattoria käytetään palauttamaan 1 vain, jos molemmat operandit ovat yhtä suuret kuin 1, ja NOT-operaattoria käytetään palauttamaan operandin vastakkainen arvo. Käytämme myös SHR-operaatiota siirtämään bittejä oikealle valitulla numerolla.

Totuustaulu:

![kuva](assets/image/section1/6.webp)

Bittisiirto-operaatiot:

![kuva](assets/image/section1/7.webp)

#### Puristusfunktio

Ennen puristusfunktion soveltamista jaamme syötteen 512 bitin lohkoihin. Jokaista lohkoa käsitellään riippumattomasti muista.

Jokainen 512 bitin lohko jaetaan edelleen 32 bitin paloiksi, joita kutsutaan W:ksi. Näin ollen W(0) edustaa 512 bitin lohkon ensimmäisiä 32 bittiä. W(1) edustaa seuraavia 32 bittiä, ja näin edelleen, kunnes saavutamme lohkon 512 bittiä.
Kun kaikki vakiot K ja lohkot W on määritelty, voimme suorittaa seuraavat laskelmat jokaiselle lohkolle W kussakin kierroksessa.
Suoritamme 64 laskentakierrosta tiivistysfunktiossa. Viimeisellä kierroksella, "funktion tulosteen" tasolla, meillä on väliaikainen tila, joka lisätään tiivistysfunktion alkutilaan.

Tämän jälkeen toistamme kaikki nämä tiivistysfunktion vaiheet seuraavassa 512-bittisessä lohkossa, kunnes viimeiseen lohkoon saakka.

Kaikki tiivistysfunktiossa suoritetut lisäykset ovat modulo 2^32 lisäyksiä, jotta summa pysyy aina 32-bittisenä.

![kuva](assets/image/section1/9.webp)

![kuva](assets/image/section1/8.webp)

##### Yksi tiivistysfunktion kierros

![kuva](assets/image/section1/11.webp)

![kuva](assets/image/section1/10.webp)

Tiivistysfunktiota suoritetaan 64 kertaa. Meillä on syötteinämme palaset W ja aiemmin määritellyt vakiot K.
Punaiset neliöt/ristit vastaavat modulo 2^32-bittistä lisäystä.

Syötteet A, B, C, D, E, F, G, H liitetään 32-bittiseen arvoon, jolloin yhteensä on 32 * 8 = 256 bittiä.
Meillä on myös uusi sekvenssi A, B, C, D, E, F, G, H tuloksena. Tätä tulosta käytetään sitten seuraavan kierroksen syötteenä ja näin edelleen, kunnes 64. kierros on päättynyt.

Syötteen arvot tiivistysfunktion ensimmäiselle kierrokselle vastaavat aiemmin mainittuja alustusvektoreita.
Muistutuksena, alustusvektorit edustavat ensimmäisten 8 alkuluvun neliöjuurten desimaaliosien ensimmäisiä 32 bittiä.

Tässä on esimerkki kierroksesta:

![kuva](assets/image/section1/12.1.webp)

##### Väliaikainen tila

Muistutuksena, viesti jaetaan 512-bittisiin lohkoihin, jotka jaetaan edelleen 32-bittisiin palasiin. Jokaiselle 512-bittiselle lohkolle sovelletaan 64 tiivistysfunktion kierrosta.
Väliaikainen tila vastaa lohkon 64 kierroksen loppua. Tämän 64. kierroksen tuloksena olevien sekvenssien arvoja käytetään seuraavan lohkon ensimmäisen kierroksen syötteen alkuarvoina.

![kuva](assets/image/section1/12.2.webp)

#### Tiivistysfunktion yleiskatsaus

![kuva](assets/image/section1/13.webp)

Huomaamme, että ensimmäisen 512-bittisen viestipalan tuloste vastaa alustusvektoreitamme syötteenä toiselle 512-bittiselle viestipalalle, ja niin edelleen.

Viimeisen kierroksen, viimeisen palan, tuloste vastaa SHA256-funktion lopputulosta.

Lopuksi haluamme korostaa CH, MAJ, σ0 ja σ1 -laatikoiden suorittamien laskelmien keskeistä roolia. Nämä toiminnot, muiden joukossa, ovat vartijoita, jotka varmistavat SHA256-tiivistysfunktion robustiuden hyökkäyksiä vastaan, tehden siitä suositun valinnan monien digitaalisten järjestelmien turvaamisessa, erityisesti Bitcoin-protokollassa. On selvää, että vaikka kompleksinen, SHA256:n kauneus piilee sen kyvyssä löytää syöte hashista, kun taas hashin varmistaminen annetulle syötteelle on mekaanisesti yksinkertainen toiminto.

## Käytetyt algoritmit johdannaisille
<chapterId>cc668121-7789-5e99-bf5e-1ba085f4f5f2</chapterId>
HMAC- ja PBKDF2-johdannaisalgoritmit ovat keskeisiä osia Bitcoin-protokollan turvamekanismissa. Ne estävät monenlaisia mahdollisia hyökkäyksiä ja takaavat Bitcoin-lompakoiden eheyden. HMAC ja PBKDF2 ovat kryptografisia työkaluja, joita käytetään erilaisiin tehtäviin Bitcoinissa. HMACia käytetään ensisijaisesti pituuslisäyshyökkäysten torjumiseen johdettaessa hierarkkisia deterministisiä (HD) lompakoita, kun taas PBKDF2:ta käytetään muuntamaan mnemoninen lause siemeneksi.

#### HMAC-SHA512

HMAC-SHA512-parilla on kaksi syötettä: viesti m (Syöte 1) ja käyttäjän mielivaltaisesti valitsema avain K (Syöte 2). Sen ulostulo on kiinteän kokoinen: 512 bittiä.

Huomioitakoon:
- m: käyttäjän valitsema mielivaltaisen kokoinen viesti (syöte 1)
- K: käyttäjän valitsema mielivaltainen avain (syöte 2)
- K': tasapainotettu avain K. Sitä on säädettu hash-funktion käyttämien lohkojen koon B mukaan.
- ||: yhdistämisoperaatio.
- opad: vakio, joka määritellään toistamalla tavua 0x5c B kertaa.
- ipad: vakio, joka määritellään toistamalla tavua 0x36 B kertaa.
- B: Käytetyn hash-funktion lohkojen koko.

![kuva](assets/image/section1/14.webp)

HMAC-SHA512, joka ottaa viestin ja avaimen syötteiksi, tuottaa kiinteän kokoisen ulostulon. Avain säädellään yhtenäiseksi hash-funktion käyttämien lohkojen koon perusteella. HD-lompakon johdannaisessa kontekstissa käytetään HMAC-SHA-512:ta. Se toimii 1024-bittisten (128-tavun) lohkojen kanssa ja säätää avaimen sen mukaisesti. Se käyttää vakioita OPAD (0x5c) ja IPAD (0x36), jotka toistetaan tarvittaessa turvallisuuden parantamiseksi.

HMAC-SHA-512-prosessi sisältää SHA-512:n tuloksen yhdistämisen avaimen XOR OPAD ja avaimen XOR IPAD kanssa viestiin. Kun käytetään 1024-bittisiä (128-tavun) lohkoja, tarvittaessa syöteavain täytetään nollilla, sitten XORataan IPAD:n ja OPAD:n kanssa. Muokattu avain yhdistetään sen jälkeen viestiin.

![kuva](assets/image/section1/15.webp)

Suolauksen lisääminen merkkijonokoodiin lisää johdettujen avainten turvallisuutta. Ilman sitä hyökkäys voisi vaarantaa koko lompakon ja varastaa kaikki bitcoinit.

PBKDF2:ta käytetään muuntamaan mnemoninen lause siemeneksi. Tämä algoritmi suorittaa 2048 kierrosta käyttäen HMAC SHA512:ta. Näiden johdannaisalgoritmien kautta erilaiset syötteet voivat tuottaa ainutlaatuisen ja kiinteän ulostulon, mikä lieventää mahdollisten pituuslisäyshyökkäysten ongelmaa SHA-2-perheen funktioissa.
Pituuslisäyshyökkäys hyödyntää tiettyjen kryptografisten hajautusfunktioiden erityisominaisuutta. Tällaisessa hyökkäyksessä hyökkääjä, joka jo omistaa tuntemattoman viestin hajautuksen, voi käyttää sitä laskemaan pidemmän viestin hajautuksen, joka on alkuperäisen viestin jatke. Tämä on usein mahdollista tietämättä alkuperäisen viestin sisältöä, mikä voi johtaa merkittäviin turvallisuusriskeihin, jos tätä tyyppistä hajautusfunktiota käytetään tehtäviin, kuten eheyden varmistamiseen.

![kuva](assets/image/section1/16.webp)

Yhteenvetona voidaan todeta, että HMAC- ja PBKDF2-algoritmit ovat olennaisia osia HD-lompakon johdannaisen turvallisuudessa Bitcoin-protokollassa. HMAC-SHA-512:ta käytetään suojaamaan pituuslisäyshyökkäyksiltä, kun taas PBKDF2 mahdollistaa mnemonisen lauseen muuntamisen siemeneksi. Merkkijonokoodi lisää ylimääräisen entropian lähteen avaimen johdannaisessa, varmistaen järjestelmän vahvuuden.

# Digitaaliset Allekirjoitukset
<partId>76b58a00-0c18-54b9-870d-6b7e34029db8</partId>
## Digitaaliset Allekirjoitukset ja Elliptiset Käyrät
<chapterId>c9dd9672-6da1-57f8-9871-8b28994d4c1a</chapterId>

Missä nämä kuuluisat bitcoinit säilytetään? Ei Bitcoin-lompakossa, kuten voisi luulla. Todellisuudessa Bitcoin-lompakko säilyttää yksityisiä avaimia, jotka ovat tarpeen bitcoinien omistajuuden todistamiseksi. Bitcoin itse on kirjattu lohkoketjuun, hajautettuun tietokantaan, joka arkistoi kaikki tapahtumat.

Bitcoin-järjestelmässä tilikirjan yksikkö on bitcoin (huomaa pieni "b"). Se on jaettavissa kahdeksaan desimaalipaikkaan, ja pienin yksikkö on satoshi. UTXO:t, eli "Käyttämättömät Tapahtuma-Outputit", edustavat julkiseen avaimiin liittyviä käyttämättömiä tapahtuma-outputteja, jotka ovat matemaattisesti linkittyneet yksityiseen avaimiin. Näiden bitcoinien käyttämiseksi henkilön on pystyttävä täyttämään tapahtuman käyttöehto. Tyypillinen käyttöehto sisältää todistuksen muulle verkostolle siitä, että käyttäjä on UTXO:hon liitetyn julkisen avaimen laillinen omistaja. Tämän tekemiseksi käyttäjän on osoitettava hallitsevansa yksityistä avainta, joka vastaa kutakin UTXO:hon liitettyä julkista avainta paljastamatta yksityistä avainta.

Tässä kohtaa digitaalinen allekirjoitus tulee mukaan. Se toimii matemaattisena todisteena yksityisen avaimen hallussapidosta, joka on liitetty tiettyyn julkiseen avaimiin. Tämä datan suojaustekniikka perustuu pääasiassa kiehtovaan kryptografian alaan nimeltä elliptinen käyräkryptografia (ECC).

Allekirjoitus voidaan matemaattisesti varmentaa Bitcoin-verkon muiden osallistujien toimesta.

![image](assets/image/section2/0.webp)

Transaktioiden turvallisuuden varmistamiseksi Bitcoin tukeutuu kahteen digitaalisen allekirjoituksen protokollaan: ECDSA (Elliptic Curve Digital Signature Algorithm) ja Schnorr. ECDSA on ollut allekirjoitusprotokolla, joka on integroitu Bitcoiniin sen käynnistyksestä lähtien vuonna 2009, kun taas Schnorr-allekirjoitukset lisättiin suhteellisen hiljattain marraskuussa 2021. Vaikka molemmat protokollat perustuvat elliptiseen käyräkryptografiaan ja käyttävät samankaltaisia matemaattisia mekanismeja, ne eroavat pääasiassa allekirjoituksen rakenteen osalta.

Tässä kurssissa esittelemme ECDSA-algoritmin.

### Mikä on elliptinen käyrä?

Elliptinen käyräkryptografia on algoritmien joukko, joka käyttää elliptistä käyrää sen erilaisten geometristen ja matemaattisten ominaisuuksien hyödyntämiseen kryptografisessa kontekstissa, turvallisuuden perustuessa diskreetin logaritmin laskemisen vaikeuteen.

Elliptiset käyrät ovat hyödyllisiä monenlaisissa kryptografisissa sovelluksissa Bitcoin-protokollassa, alkaen avaintenvaihdosta aina asymmetriseen salaukseen ja digitaalisiin allekirjoituksiin.

Elliptisillä käyrillä on mielenkiintoisia ominaisuuksia:

- Symmetria: Mikä tahansa ei-pystysuora viiva, joka leikkaa kaksi pistettä elliptisellä käyrällä, leikkaa käyrän kolmannessa pisteessä.
- Mikä tahansa ei-pystysuora tangenttiviiva käyrään pisteessä leikkaa aina käyrän yksilöllisessä toisessa pisteessä.

Bitcoin-protokolla käyttää kryptografisiin toimintoihinsa tiettyä elliptistä käyrää nimeltä Secp256k1.

Ennen kuin sukellamme syvemmälle näihin allekirjoitusmekanismeihin, on tärkeää ymmärtää, mikä elliptinen käyrä on. Elliptinen käyrä määritellään yhtälöllä y² = x³ + ax + b. Jokaisella tämän käyrän pisteellä on erottuva symmetria, joka on avainasemassa sen hyödyllisyydessä kryptografiassa.

![image](assets/image/section2/1.webp)

Lopulta erilaiset elliptiset käyrät tunnustetaan turvallisiksi kryptografiseen käyttöön. Tunnetuin saattaa olla secp256r1-käyrä. Bitcoinille Satoshi Nakamoto valitsi kuitenkin eri käyrän: secp256k1.
Tämä käyrä määritellään parametreilla a=0 ja b=7, ja sen yhtälö on y² = x³ + 7 modulo n, missä n edustaa alkulukua, joka määrittää käyrän järjestyksen.
![image](assets/image/section2/2.webp)

Ensimmäinen kuva esittää secp256k1-käyrää reaalikentän yli ja sen yhtälöä.
Toinen kuva on esitys secp256k1-käyrästä ZP-kentän yli, positiivisten luonnollisten lukujen kenttä, modulo p, missä p on alkuluku. Se näyttää pisteiden pilveltä. Käytämme tätä positiivisten luonnollisten lukujen kenttää välttääksemme likiarvoja.
p on alkuluku, ja se on käyrän järjestys, jota käytetään.
Lopulta, Bitcoin-protokollassa käytetty yhtälö on:$$
y^2 = (x^3 + 7) mod(p) $$
Bitcoinin elliptisen käyrän yhtälö vastaa viimeistä yhtälöä edellisessä kuvassa.

Seuraavassa kurssin osiossa käytämme käyriä, jotka ovat reaalikentällä yksinkertaisesti ymmärryksen helpottamiseksi.

## Julkisen avaimen laskeminen yksityisavaimesta
<chapterId>fcb2bd58-5dda-5ecf-bb8f-ad1a0561ab4a</chapterId>

Aloitetaan sukeltamalla Elliptisen Käyrän Digitaalisen Allekirjoitus Algoritmin (ECDSA) maailmaan. Bitcoin käyttää tätä digitaalista allekirjoitus algoritmia yhdistämään yksityiset ja julkiset avaimet. Tässä järjestelmässä yksityinen avain on satunnainen tai pseudo-satunnainen 256-bittinen numero. Yksityisen avaimen mahdollisuuksien teoreettinen määrä on 2^256, mutta todellisuudessa se on hieman vähemmän. Tarkalleen ottaen jotkut 256-bittiset yksityiset avaimet eivät kelpaa Bitcoinille.

Ollakseen yhteensopiva Bitcoinin kanssa, yksityisen avaimen on oltava välillä 1 ja n-1, missä n edustaa elliptisen käyrän järjestystä. Tämä tarkoittaa, että Bitcoinin yksityisen avaimen mahdollisuuksien määrä on lähes yhtä suuri kuin 1.158 x 10^77. Tämän asettaminen perspektiiviin, se on suunnilleen sama määrä atomeja havaittavissa olevassa universumissa.

![image](assets/image/section2/3.webp)

Uniikki yksityinen avain, merkitty k:lla, käytetään sitten julkisen avaimen määrittämiseen.

Julkisen avaimen, merkitty K:lla, on piste elliptisellä käyrällä, joka johdetaan yksityisestä avaimesta käyttämällä peruuttamattomia algoritmeja kuten ECDSA. Kun meillä on tiedossa yksityinen avain, julkisen avaimen saaminen on hyvin helppoa, mutta kun meillä on vain julkinen avain, yksityisen avaimen saaminen on mahdotonta. Tämä peruuttamattomuus on Bitcoin-lompakon turvallisuuden peruskivi.

Julkinen avain on 512 bittiä pitkä, koska se vastaa pistettä käyrällä, jolla on x-koordinaatti 256 bittiä ja y-koordinaatti 256 bittiä. Kuitenkin se voidaan tiivistää 264-bittiseksi numeroksi.

![image](assets/image/section2/4.webp)

Generaattoripiste (G) on piste käyrällä, josta kaikki julkiset avaimet Bitcoin-protokollassa generoidaan. Sillä on tiettyjä x- ja y-koordinaatteja, yleensä esitettyinä heksadesimaalina. Secp256k1:lle G:n koordinaatit ovat heksadesimaalina:

- `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
- `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8` Tämä piste on hyödyllinen kaikkien julkisten avainten johtamisessa. Julkisen avaimen K laskemiseksi kerrotaan vain piste G yksityisellä avaimella k, siten että: K = k.G

Nyt tutkimme, miten pisteitä voidaan lisätä ja kertoa elliptisillä käyrillä.

#### Pisteiden lisäys ja kaksinkertaistaminen elliptisillä käyrillä

##### Kahden pisteen M + L lisääminen

Yksi elliptisten käyrien merkittävistä ominaisuuksista on, että ei-pystysuora viiva, joka leikkaa käyrän kahdessa pisteessä, leikkaa sen myös kolmannessa pisteessä, jota kutsutaan esimerkissämme pisteeksi O. Tätä ominaisuutta käytetään määrittämään piste U, joka on pisteen O vastakohta.

M + L = U

![kuva](assets/image/section2/5.webp)

##### Pisteen lisääminen itseensä = Pisteen kaksinkertaistaminen

Pisteen G lisääminen itseensä tapahtuu piirtämällä tangentti käyrälle kyseisessä pisteessä. Tämä tangentti, elliptisten käyrien ominaisuuksien mukaisesti, leikkaa käyrän toisessa yksilöllisessä pisteessä -J. Tämän pisteen, J, vastakohta on tuloksena, kun piste G lisätään itseensä.
G + G = J

Itse asiassa piste G on lähtökohta kaikkien Bitcoin-järjestelmän käyttäjien julkisten avainten laskemiselle.

![kuva](assets/image/section2/6.webp)

#### Skalaarikertolasku elliptisillä käyrillä

Pisteen kertominen skalaarilla n on yhtä kuin kyseisen pisteen lisääminen itseensä n kertaa.

Samankaltaisesti kuin pisteen kaksinkertaistaminen, pisteen G kertominen pisteellä n tapahtuu piirtämällä tangentti käyrälle pisteessä G. Tämä tangentti, elliptisten käyrien ominaisuuksien mukaisesti, leikkaa käyrän toisessa yksilöllisessä pisteessä -2G. Tämän pisteen, 2G, vastakohta on tuloksena, kun piste G lisätään itseensä.

Jos n = 4, toimenpide toistetaan kunnes saavutetaan 4G.

![kuva](assets/image/section2/7.webp)

Tässä on esimerkkilaskelma 3G:lle:

![kuva](assets/image/section2/8.webp)

Nämä toimenpiteet elliptisen käyrän pisteillä ovat perusta julkisten avainten laskemiselle. Julkisen avaimen johtaminen yksityisestä avaimesta on erittäin helppoa.
Julkisen avaimen K on piste elliptisellä käyrällä, se on tuloksena meidän lisäyksestämme ja pisteen G kaksinkertaistamisesta k kertaa. Missä k = yksityinen avain.

Tässä esimerkissä:

- Yksityinen avain k = 4
- Julkinen avain K = kG = 4G

![kuva](assets/image/section2/9.webp)

Yksityisen avaimen k tietäen, julkisen avaimen K laskeminen on helppoa. Kuitenkin yksityisen avaimen palauttaminen julkisen avaimen perusteella on mahdotonta. Onko tämä pisteiden lisäyksen vai kaksinkertaistamisen tulos?

Seuraavassa oppitunnissa tutkimme, miten digitaalinen allekirjoitus luodaan käyttäen ECDSA-algoritmia yksityisellä avaimella bitcoineja käytettäessä.

## Allekirjoittaminen yksityisellä avaimella
<chapterId>bb07826f-826e-5905-b307-3d82001fb778</chapterId>

Digitaalisen allekirjoituksen prosessi on keskeinen menetelmä todistaa, että olet yksityisen avaimen haltija paljastamatta sitä. Tämä saavutetaan käyttämällä ECDSA-algoritmia, joka sisältää ainutlaatuisen nonce-arvon määrittämisen, tietyn numeron V laskemisen ja digitaalisen allekirjoituksen luomisen, joka koostuu kahdesta osasta, S1 ja S2.
On erittäin tärkeää aina käyttää uniikkia nonce-arvoa turvallisuushyökkäysten välttämiseksi. Kuuluisa esimerkki siitä, mitä voi tapahtua kun tätä sääntöä ei noudateta, on PlayStation 3:n hakkerointi, joka vaarantui nonce-arvon uudelleenkäytön vuoksi.
![](assets/image/section2/10.webp)

Vaiheet:

- Määritä nonce-arvo v, joka on uniikki satunnaisluku.
  Nonce = Number Only Used Once.
  Sen määrittää allekirjoituksen suorittaja.
- Laske lisäämällä ja kaksinkertaistamalla pisteitä elliptisellä käyrällä lähtöpisteestä G, V:n sijainti elliptisellä käyrällä.
  Niin että V = v.G
  x ja y ovat V:n koordinaatit tasossa.
- Laske S1.
  S1 = x mod n, missä n = käyrän järjestys ja x V:n koordinaatti tasossa.
  Huom: Mahdollisten julkisten avainten määrä on suurempi kuin pisteiden määrä elliptisellä käyrällä positiivisten kokonaislukujen äärellisessä kentässä, jota käytetään Bitcoinissa.
  Käyrän järjestys vastaa vain mahdollisuuksia, joita julkinen avain voi ottaa käyrällä.
- Laske S2.
  H(Tx) = Transaktion hash
  k = yksityinen avain
- Laske allekirjoitus: S1 + S2 yhdistäminen.
- Laske P, allekirjoituksen varmennuslaskenta.
  K = julkinen avain

Esimerkiksi saadaksesi julkisen avaimen 3G, piirrät tangentin pisteeseen G, lasket vastakohdan -G saadaksesi 2G, ja sitten lisäät G:n ja 2G:n. Suorittaaksesi transaktion, sinun täytyy todistaa tietäväsi luvun 3 lukitsemalla bitcoinit, jotka on yhdistetty julkiseen avaimen 3G.

Luodaksesi digitaalisen allekirjoituksen ja todistaaksesi tietäväsi yksityisen avaimen, joka on yhdistetty julkiseen avaimen 3G, lasket ensin noncen, sitten piste V, joka on yhdistetty tähän nonceen (annetussa esimerkissä se on 4G). Sitten lasket pisteen T lisäämällä julkisen avaimen 3G ja pisteen V, mikä antaa 7G.

![image](assets/image/section2/11.webp)

Yksinkertaistetaan digitaalisen allekirjoituksen prosessia.
Edellisessä kuvassa yksityinen avain k = 3.
Voimme helposti laskea yksityiseen avaimen liittyvän julkisen avaimen K: K = 3G.
Sitten generoimme noncen pseudo-satunnaisesti: v = 4.
Tästä noncesta on mahdollista laskea V niin että: V = v.G = 4G.

Tästä pisteestä V, laskemme pisteen T niin että:
T = t.G = 7G (missä t = 7).

Nyt on aika edetä digitaalisen allekirjoituksen varmentamiseen.

Digitaalisen allekirjoituksen varmentaminen on kriittinen vaihe ECDSA-algoritmin käytössä, joka mahdollistaa allekirjoitetun viestin aitouden vahvistamisen tarvitsematta lähettäjän yksityistä avainta. Tässä on miten se toimii yksityiskohtaisesti:

Esimerkissämme meillä on kaksi tärkeää arvoa: t ja V.
t on numeerinen arvo (7 tässä esimerkissä), ja V on piste elliptisellä käyrällä (edustettuna tässä 4G:llä). Nämä arvot generoidaan digitaalisen allekirjoituksen luomisen aikana ja lähetetään sitten viestin mukana mahdollistaakseen varmentamisen.

Kun varmentaja vastaanottaa viestin, hän saa myös nämä kaksi arvoa, t ja V.

Tässä ovat askeleet, joita varmentaja seuraa allekirjoituksen vahvistamiseksi:

1. Ensin he laskevat viestin hashin, jota kutsutaan H:ksi.
2. Sitten he laskevat u1:n ja u2:n. Tätä varten he käyttävät seuraavia kaavoja:
- u1 = H /\* (S2)^-1 mod n   - u2 = T /\* (S2)^-1 mod n
     Missä S2 on digitaalisen allekirjoituksen toinen osa, n on elliptisen käyrän järjestys, ja (S2)^-1 on S2:n käänteisluku mod n.
3. Varmistaja laskee sitten pisteen P' elliptisellä käyrällä käyttäen kaavaa: P' = u1 _ G + u2 _ K
   - G on käyrän luoja piste
   - K on lähettäjän julkinen avain
4. Varmistaja laskee sitten I', joka on yksinkertaisesti pisteen P' x-koordinaatti modulo n.
5. Lopuksi varmistaja vahvistaa, että I' on yhtä suuri kuin t. Jos näin on, allekirjoitus katsotaan päteväksi. Jos ei, allekirjoitus on pätemätön.
Tämä menettely varmistaa, että vain lähettäjä, jolla on vastaava yksityinen avain, olisi voinut tuottaa allekirjoituksen, joka läpäisee tämän varmennusprosessin.

![kuva](assets/image/section2/12.webp)

Yksinkertaisemmin sanottuna:
Allekirjoituksen tuottava henkilö antaa numeron t (esimerkissämme t = 7) ja pisteen V henkilölle, joka varmentaa sen.

Julkista avainta tai yksityistä avainta ei ole mahdollista määrittää numerosta 7 ja pisteestä V.

Digitaalisen allekirjoituksen varmentamisen vaiheet ovat seuraavat:

- Käyrällä varmistaja lisää julkisen avaimen pisteen pisteeseen V saadakseen pisteen T'.
- Varmistaja laskee numeron t.G.
- Varmistaja tarkistaa, että t.G:n tulos on todellakin yhtä suuri kuin numero T'.

Yhteenvetona voidaan todeta, että digitaalisen allekirjoituksen varmentaminen on olennainen menettely Bitcoin-siirroissa. Se varmistaa, että allekirjoitettua viestiä ei ole muutettu lähetyksen aikana ja että lähettäjä on todellakin yksityisen avaimen haltija. Tämä digitaalinen todennustekniikka perustuu monimutkaisiin matemaattisiin periaatteisiin, mukaan lukien elliptisen käyrän aritmetiikka, samalla kun se säilyttää yksityisen avaimen luottamuksellisuuden. Se tarjoaa vankan turvallisuusperustan kryptografisille transaktioille.

Tämä sanottuna, näiden avainten hallinta sekä niiden luominen on toinen olennainen kysymys Bitcoinissa. Miten luoda uusi avainpari? Miten järjestää tehokkaasti ja turvallisesti lukuisia avaimia? Miten palauttaa ne tarvittaessa?

Näihin kysymyksiin vastaamiseksi ja kryptografian turvallisuuden ymmärtämisen syventämiseksi seuraava kurssimme keskittyy Hierarkkisten Determinististen Lompakoiden (HD-lompakot) konseptiin ja mnemonisten fraasien käyttöön. Nämä mekanismit tarjoavat tyylikkäitä tapoja hallita tehokkaasti kryptovaluutta-avaimiasi samalla kun parannat turvallisuutta.

# Mnemoninen fraasi
<partId>4070af16-c8a2-58b5-9871-a22c86c07458</partId>

## Bitcoin-lompakoiden kehitys
<chapterId>9d9acd5d-a0e5-5dfd-b544-f043fae8840f</chapterId>

Hierarkkinen Deterministinen Lompakko, joka tunnetaan paremmin nimellä HD-lompakko, on merkittävässä roolissa kryptovaluuttaekosysteemissä. Termi "lompakko" saattaa tuntua harhaanjohtavalta niille, jotka ovat uusia tällä alalla, sillä se ei sisällä rahan tai valuuttojen pitämistä. Sen sijaan se viittaa kokoelmaan kryptografisia yksityisiä avaimia.

Varhaiset lompakot olivat ohjelmistoja, jotka ryhmittivät yksityisesti määritettyjä avaimia satunnaisesti, mutta niillä ei ollut keskinäistä yhteyttä. Näitä lompakoita kutsutaan "Vain Joukko Avaimia" (JBOK).

Koska avaimilla ei ole keskinäistä yhteyttä, käyttäjän on luotava uusi varmuuskopio jokaiselle uudelle avainparille, jonka hän luo.
Olipa käyttäjä aina käyttämässä samaa avainparia ja vaarantamassa luottamuksellisuuden, tai luomassa uuden avainparin satunnaisesti ja siksi tarvitsemassa näiden avainten uuden varmuuskopion.
Kuitenkin näiden avainten hallinnan monimutkaisuus tasapainotetaan protokollasarjalla, jota kutsutaan Bitcoinin parannusehdotuksiksi (BIPs). Nämä päivitysehdotukset ovat HD-lompakoiden toiminnallisuuden ja turvallisuuden ytimessä. Esimerkiksi [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), joka julkaistiin vuonna 2012, mullisti näiden avainten luomisen ja tallentamisen tavan esittelemällä deterministisesti ja hierarkkisesti johdettujen avainten konseptin. Ajatuksena on johtaa kaikki avaimet deterministisesti ja hierarkkisesti yhdestä ainutlaatuisesta tiedosta: siemenestä. Tämä yksinkertaistaa merkittävästi näiden avainten varmuuskopiointiprosessia samalla kun niiden turvallisuustaso säilytetään.

Myöhemmin [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) esitteli merkittävän innovaation: 24-sanan muistilauseen. Tämä järjestelmä muutti monimutkaisen ja vaikeasti muistettavan numerosekvenssin sarjaksi tavallisia sanoja, mikä teki siitä paljon helpommin muistettavan ja tallennettavan. Lisäksi [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) ehdotti yksittäisten avainten turvallisuuden parantamiseksi lisäsalasanan lisäämistä. Nämä peräkkäiset parannukset johtivat BIP43- ja BIP44-standardien kehittämiseen, jotka standardisoivat HD-lompakoiden rakenteen ja hierarkian, tehden niistä yleisölle helpommin saavutettavia ja käyttäjäystävällisempiä.

Seuraavissa osioissa syvennymme HD-lompakoiden toimintaan tarkemmin. Keskustelemme avainten johdannon periaatteista ja tutkimme entropian ja satunnaislukugeneroinnin peruskäsitteitä, jotka ovat olennaisen tärkeitä HD-lompakkosi turvallisuuden varmistamiseksi.

Yhteenvetona on olennaista korostaa BIP32:n ja BIP39:n keskeistä roolia HD-lompakoiden suunnittelussa ja turvallisuudessa. Nämä protokollat mahdollistavat useiden avainten luomisen yhdestä siemenestä, joka on tarkoitus olla satunnainen tai pseudosatunnainen luku. Nykyään nämä standardit on hyväksytty useimpien kryptovaluuttalompakoiden toimesta, olivatpa ne omistettu yhdelle kryptovaluutalle tai tukevat useita eri valuuttoja.

## Entropia ja Satunnaisluku
<chapterId>b43c715d-affb-56d8-a697-ad5bc2fffd63</chapterId>

Bitcoin-ekosysteemin yksityisen avaimen turvallisuuden tärkeys on kiistaton. Ne ovat todellakin kulmakivi, joka varmistaa Bitcoin-siirtojen turvallisuuden. Jotta ennustettavuuteen liittyvältä haavoittuvuudelta vältyttäisiin, nämä avaimet on luotava todella satunnaisella tavalla, mikä voi nopeasti muodostua työlääksi harjoitukseksi. Ongelmana on, että tietojenkäsittelytieteessä on mahdotonta luoda todella satunnaista lukua, koska se on välttämättä johdettu deterministisesta prosessista; koodista. Siksi on olennaista oppia erilaisista Satunnaislukugeneraattoreista (RNG). RNG-tyypit vaihtelevat Pseudo-Satunnaislukugeneraattoreista (PRNG) Todellisiin Satunnaislukugeneraattoreihin (TRNG) sekä PRNG:eihin, jotka sisältävät entropian lähteen.

Entropia viittaa järjestelmän "epäjärjestyksen" tilaan. Ulkoisesta entropiasta, eli ulkoisesta tietolähteestä, on mahdollista käyttää satunnaislukugeneraattoria saadakseen satunnaisluvun.

![kuva](assets/image/section3/2.webp)

Katsotaanpa, miten Pseudo-Satunnaislukugeneraattori (PRNG) toimii.

Se ottaa syötteenä siemenen, joka vastaa sisäistä tilaa 0.
Tähän sisäiseen tilaan sovelletaan muunnosfunktiota, ja tulos, joka on pseudosatunnaisluku, vastaa sisäistä tilaa 1.
Tähän sisäiseen tilaan 1 sovelletaan jälleen muunnosfunktiota, mikä johtaa uuteen satunnaislukuun = sisäinen tila 2.
Ja niin edelleen.
Pääasiallinen haittapuoli on, että mikä tahansa identtinen siemen tuottaa aina saman tuloksen. Lisäksi, jos tiedämme alkuperäisten muunnosfunktioiden tuloksen, pystymme palauttamaan satunnaisluvun prosessin lopputuloksesta.
Esimerkki muunnosfunktiosta on PBKDF2-funktio.

**Yhteenvetona, kryptografisesti turvallisen satunnaislukugeneraattorin on:**

- oltava tilastollisesti satunnainen
- oltava ennustamaton
- oltava vastustuskykyinen, vaikka tulokset paljastettaisiin
- oltava riittävän pitkä jakso

![kuva](assets/image/section3/3.webp)

Bitcoinin tapauksessa yksityiset avaimet luodaan yhdestä tiedosta, joka on lompakon perustana. Tämä tieto mahdollistaa deterministisen ja hierarkkisen johdannaisen lapsiavainparien luomisen. Entropia on jokaisen HD-lompakon perusta, vaikka satunnaisluvun tuottamiselle ei olekaan standardia. Siksi satunnaislukujen generointi on suuri haaste Bitcoin-siirtojen turvaamisessa.

## Mnemoninen lause
<chapterId>8f9340c1-e6dc-5557-a2f2-26c9669987d5</chapterId>

Bitcoin-lompakon turvallisuus on suuri huolenaihe kaikille sen käyttäjille. Yksi olennainen tapa varmistaa lompakon varmuuskopiointi on generoida mnemoninen lause entropian ja tarkistussumman perusteella.

![kuva](assets/image/section3/5.webp)

Entropian muuntamiseksi mnemoniseksi lauseeksi, laske yksinkertaisesti entropian tarkistussumma ja yhdistä entropia ja tarkistussumma.

Kun entropia on generoitu, SHA256-funktiota käytetään entropiaan luomaan hajautus.
Hajautuksen ensimmäiset 8 bittiä otetaan, mikä on tarkistussumma.
Mnemoninen lause on entropian ja tarkistussumman tuloksen yhdistelmä.

Tarkistussumma varmistaa palautuslauseen tarkkuuden tarkistamisen. Ilman tätä tarkistussummaa virhe lauseessa voisi johtaa eri lompakon luomiseen ja siten varojen menetykseen. Tarkistussumma saadaan suorittamalla entropia SHA256-funktion läpi ja ottamalla hajautuksen ensimmäiset 8 bittiä.

![kuva](assets/image/section3/6.webp)

Mnemoniselle lauseelle on olemassa erilaisia standardeja riippuen entropian koosta. Yleisimmin käytetty standardi 24 sanan palautuslauseelle on 256 bitin entropia. Tarkistussumman koko määritetään jakamalla entropian koko 32:lla.

Esimerkiksi 256 bitin entropia tuottaa 8 bitin tarkistussumman. Entropian ja tarkistussumman yhdistäminen johtaa vastaavasti 128 bitin, 160 bitin jne. kokoihin. Entropian koosta riippuen palautuslause koostuu 12 sanasta 128 bitin kohdalla, 15 sanasta 160 bitin kohdalla ja 24 sanasta 256 bitin kohdalla.

**Mnemonisen lauseen koodaus:**

![kuva](assets/image/section3/7.webp)

Viimeiset 8 bittiä vastaavat tarkistussummaa.
Jokainen 11-bittinen segmentti muunnetaan desimaaliksi.
Jokainen desimaali vastaa sanaa 2048 sanan listalta BIP39:ssä. On tärkeää huomata, että yksikään sana ei ole samassa järjestyksessä ensimmäisten neljän kirjaimen osalta.

On olennaista varmuuskopioida 24 sanan palautuslause Bitcoin-lompakon eheyden säilyttämiseksi. Kaksi yleisimmin käytettyä standardia perustuvat 128 tai 256 bitin entropiaan ja 12 tai 24 sanan yhdistämiseen. Salasanan lisääminen on lisävaihtoehto lompakon turvallisuuden parantamiseksi.

Yhteenvetona, mnemonisen lauseen generointi Bitcoin-lompakon turvaamiseksi on kriittinen prosessi. On tärkeää noudattaa mnemonisen lauseen standardeja entropian koosta riippuen. 24 sanan palautuslauseen varmuuskopiointi on olennaista varojen menetyksen estämiseksi.

## Salasana
<chapterId>6a51b397-f3b5-5084-b151-cef94bc9b93f</chapterId>
Salasana on lisäsalasana, joka voidaan integroida Bitcoin-lompakkoon sen turvallisuuden lisäämiseksi. Sen käyttö on valinnaista ja käyttäjän harkinnan mukaan. Lisäämällä mielivaltaista tietoa, joka yhdessä muistilauseen kanssa mahdollistaa lompakon siemenen laskennan, salasana parantaa sen turvallisuutta.

![image](assets/image/section3/8.webp)

Salasana on valinnainen kryptografinen suola, jonka koon käyttäjä valitsee. Se parantaa HD-lompakon turvallisuutta lisäämällä mielivaltaista tietoa, joka yhdistettynä muistilauseeseen mahdollistaa siemenen laskennan.

Kun se on perustettu lompakon luomisen yhteydessä, se on välttämätön kaikkien lompakon avainten johdannaisille. Pbkdf2-funktiota käytetään siemenen generoimiseen salasanasta. Tämä siemen mahdollistaa kaikkien lompakon lasten avainparien johdannaiset. Jos salasanaa muutetaan, Bitcoin-lompakko muuttuu täysin erilaiseksi.

Salasana on olennainen työkalu Bitcoin-lompakoiden turvallisuuden parantamiseen. Sen avulla voidaan toteuttaa erilaisia turvallisuusstrategioita. Esimerkiksi sitä voidaan käyttää luomaan duplikaatteja ja helpottamaan muistilauseen varmuuskopioita. Se voi myös parantaa lompakon turvallisuutta vähentämällä muistilauseen satunnaisen generoinnin riskejä.

Tehokkaan salasanan tulisi olla pitkä (20–40 merkkiä) ja monipuolinen (käyttäen isoja kirjaimia, pieniä kirjaimia, numeroita ja symboleita). Sen ei tulisi olla suoraan yhteydessä käyttäjään tai heidän ympäristöönsä. Satunnaisen merkkijonon käyttäminen on turvallisempaa kuin yksinkertaisen sanan käyttäminen salasanana.

![image](assets/image/section3/9.webp)

Salasana on turvallisempi kuin yksinkertainen salasana. Ihanteellinen salasana on pitkä, monipuolinen ja satunnainen. Se voi parantaa lompakon tai kuuman ohjelmiston turvallisuutta. Sitä voidaan myös käyttää luomaan redundanteja ja turvallisia varmuuskopioita.

On tärkeää huolehtia salasanan varmuuskopioista, jotta vältetään pääsyn menettäminen lompakkoon. Salasana on vaihtoehto HD-lompakolle. Sen voi generoida satunnaisesti nopilla tai muulla pseudo-satunnaislukugeneraattorilla. Salasanan tai muistilauseen muistaminen ei ole suositeltavaa.

Seuraavassa oppitunnissamme tarkastelemme yksityiskohtaisesti siemenen toimintaa ja siitä generoitua ensimmäistä avainparia. Jatka kurssin seuraamista oppimisesi jatkamiseksi. Odotamme innolla näkevämme sinut taas hyvin pian.

# Bitcoin-lompakoiden luominen
<partId>9c25e767-7eae-50b8-8c5f-679d8fc83bab</partId>

## Siemenen ja pääavaimen luominen
<chapterId>63093760-2010-5691-8d0e-9a04732ae557</chapterId>

Tässä kurssin osassa tutkimme Hierarkkisen Deterministisen Lompakon (HD Wallet) johdannaisten vaiheita, jotka mahdollistavat yksityisten ja julkisten avainten hierarkkisen ja deterministisen luomisen ja hallinnan.

![image](assets/image/section4/0.webp)

HD-lompakon perusta nojaa kahteen olennaiseen elementtiin: muistilauseeseen ja salasanaan (valinnainen lisäsalasana). Yhdessä ne muodostavat siemenen, 512-bittisen alfanumeerisen sekvenssin, joka toimii perustana lompakon avainten johdannaisille. Tästä siemenestä on mahdollista johtaa kaikki Bitcoin-lompakon lasten avainparit. Siemen on avain, joka antaa pääsyn kaikkiin lompakkoon liittyviin bitcoineihin, käytitpä salasanaa tai et.

![image](assets/image/section4/1.webp)
Siemenen saamiseksi käytetään pbkdf2-funktiota (Password-Based Key Derivation Function 2) yhdessä muistilauseen ja salasanan kanssa. pbkdf2:n tuloksena on 512-bittinen siemen.
Siemenestä on mahdollista määrittää pääyksityisavain ja ketjukoodi käyttämällä HMAC SHA-512 (Hash-based Message Authentication Code Secure Hash Algorithm 512) -algoritmia. Tämä algoritmi vaatii viestin ja avaimen syötteenä tuottaakseen tuloksen. Pääyksityisavain lasketaan siemenestä ja lauseesta "Bitcoin SEED". Tämä lause on identtinen kaikissa HD-lompakoiden johdannaisissa, mikä varmistaa yhdenmukaisuuden lompakoiden välillä.

Alun perin SHA-512-funktiota ei ollut toteutettu Bitcoin-protokollassa, minkä vuoksi käytetään HMAC SHA-512:ta. HMAC SHA-512:n käyttö lauseen "Bitcoin SEED" kanssa rajoittaa käyttäjän luomaan lompakon, joka on spesifinen Bitcoinille. HMAC SHA-512:n tulos on 512-bittinen numero, joka jaetaan kahteen osaan: vasemmanpuoleiset 256 bittiä edustavat pääyksityisavainta, kun taas oikeanpuoleiset 256 bittiä edustavat pääketjukoodia.

![kuva](assets/image/section4/2.webp)

Pääyksityisavain on kaikkien tulevien avainten vanhempi avain lompakossa, kun taas pääketjukoodi on mukana lapsiavainten johdannaisissa. On tärkeää huomata, että lapsiavainparia on mahdotonta johtaa tietämättä vastaavan vanhemman parin ketjukoodia.

Avainpari lompakossa koostuu yksityisavaimesta, julkisesta avaimesta ja ketjukoodista. Ketjukoodi tuo satunnaisuuden lähteen lapsiavainten johdannaisiin ja eristää jokaisen avainparin estäen tietovuodon.
On tärkeää huomata, että pääyksityisavain on ensimmäinen siemenestä johdettu yksityisavain eikä sillä ole yhteyttä lompakon laajennettuihin avaimiin.

Seuraavassa oppitunnissa tutkimme tarkemmin laajennettuja avaimia, kuten xPub, xPRV, zPub, ja ymmärrämme miksi niitä käytetään ja miten ne rakennetaan.

## Laajennetut Avaimet
<chapterId>8dcffce1-31bd-5e0b-965b-735f5f9e4602</chapterId>

Tässä osassa oppituntia tutkimme laajennettuja avaimia (xPub, zPub, yPub) ja niiden etuliitteitä, jotka ovat tärkeässä roolissa lapsiavainten johdannaisissa Hierarkkisesti Deterministisessä Lompakossa (HD Lompakko).

![kuva](assets/image/section4/3.webp)

Laajennetut avaimet eroavat pääavaimista. HD-lompakko luo muistilauseen ja siemenen saadakseen pääavaimen ja pääketjukoodin. Laajennettuja avaimia käytetään lapsiavainten johdannaisiin ja ne vaativat sekä vanhemman avaimen että vastaavan ketjukoodin. Laajennettu avain yhdistää nämä kaksi tietoa yksinkertaistaakseen johdannaisprosessia.

![kuva](assets/image/section4/4.webp)

Laajennetut julkiset avaimet voivat johtaa vain normaaleja lapsijulkisia avaimia, kun taas laajennetut yksityisavaimet voivat johtaa sekä lapsijulkisia että yksityisiä avaimia, olipa kyseessä sitten normaali tai kova johdannainen. Kovassa johdannaisessa käytetään vanhemman yksityisavainta, kun taas normaali johdannainen vastaa johdannaista vanhemman julkisesta avaimesta.

Laajennettujen avainten käyttö XPUB-etuliitteen kanssa mahdollistaa uusien osoitteiden johdannaisen palaamatta vastaaviin yksityisavaimiin, tarjoten siten paremman turvallisuuden. Laajennettujen avainten metadata tarjoaa tärkeää tietoa niiden roolista ja asemasta avainhierarkiassa.
Laajennetut avaimet tunnistetaan erityisillä etuliitteillä (XPRV, XPUB, YPUB, ZPUB), jotka ilmaisevat, onko kyseessä laajennettu yksityinen vai julkinen avain, sekä sen tarkoituksen. Laajennetun avaimen metadataan kuuluu versio (etuliite), syvyys, vanhemman avaimen sormenjälki, indeksi ja kuorma (ketjukoodi ja vanhempi avain).
![image](assets/image/section4/5.webp)

Versio vastaa avaimen tyyppiä: xpub, xprv, ...

Syvyys vastaa johdannaisten määrää vanhemman ja lapsiavaimen välillä alkaen pääavaimesta.

Vanhemman sormenjälki on vanhemman avaimen hash 160:n ensimmäiset 4 tavua.
Indeksi on parin numero, jota käytetään laajennetun avaimen generoimiseen sen sisarusten joukosta. (sisarukset = saman syvyyden avaimet) Esimerkiksi, jos haluamme johtaa kolmannen tilimme xpubin, sen indeksi on 2 (koska indeksointi alkaa nollasta).

Kuorma koostuu ketjukoodista (32 tavua) ja vanhemmasta avaimesta (33 tavua).

Pakatut julkiset avaimet ovat 33 tavun kokoisia, kun taas raakajulkiset avaimet ovat 512 bittiä. Pakatut julkiset avaimet säilyttävät saman tiedon kuin raaka-avaimet, mutta pienemmässä koossa. Laajennetuilla avaimilla on 82 tavun koko ja niiden etuliite esitetään base 58:ssa muuntamalla se heksadesimaaliksi. Tarkistussumma lasketaan käyttäen HASH256-hajautusfunktiota.

![image](assets/image/section4/6.webp)

Parannetut johdannaiset alkavat indekseistä, jotka ovat kahden potensseja (2^31). On mielenkiintoista huomata, että yleisimmin käytetyt etuliitteet ovat xpub ja zpub, jotka vastaavat vastaavasti perinteisiä standardeja ja segwit v1 ja segwit v0.

Seuraavassa oppitunnissamme keskitymme lapsiavainparien johdantoon käyttäen hyväksi tietoa laajennetuista avaimista ja lompakon pääavaimesta.

## Lapsiavainparien johdanto
<chapterId>61c0807c-845b-5076-ad06-7f395b36adfd</chapterId>

Muistutuksena olemme keskustelleet siemenen ja pääavaimen laskennasta, jotka ovat ensimmäiset olennaiset elementit HD (Hierarkkinen Deterministinen) lompakon hierarkkisen organisaation ja johdannon kannalta. Siemen, jonka pituus on 128-256 bittiä, generoidaan satunnaisesti tai salaisesta fraasista. Se toimii deterministisessä roolissa kaikkien muiden avainten johdannossa. Pääavain on ensimmäinen siemenestä johdettu avain, ja se mahdollistaa kaikkien muiden lapsiavainparien johdannon.

Pääketjukoodilla on tärkeä rooli lompakon palauttamisessa siemenestä. On huomattava, että kaikki samasta siemenestä johdetut avaimet omaavat saman pääketjukoodin.

![image](assets/image/section4/7.webp)

HD-lompakon hierarkkinen organisaatio ja johdanto tarjoavat tehokkaamman avainten ja lompakon rakenteiden hallinnan. Laajennetut avaimet mahdollistavat lapsiavainparin johdannon vanhemmasta avainparista käyttäen matemaattisia laskelmia ja tiettyjä algoritmeja.
On olemassa erilaisia lapsiavainpareja, mukaan lukien vahvistetut avaimet ja normaalit avaimet. Laajennettu julkinen avain sallii vain normaalien lapsijulkisten avainten johdannon, kun taas laajennettu yksityinen avain mahdollistaa kaikkien lapsiavainten, sekä julkisten että yksityisten, johdannon, olivatpa ne normaalissa tai vahvistetussa tilassa. Jokaisella avainparilla on indeksi, joka mahdollistaa niiden erottamisen toisistaan.

![image](assets/image/section4/8.webp)
Lasten avainten johdannassa käytetään HMAC-SHA512-funktiota käyttäen vanhemman avainta yhdistettynä indeksiin ja avainpariin liitettyyn ketjukoodiin. Normaaleilla lapsiavaimilla on indeksi välillä 0 - 2 potenssiin 31 miinus 1, kun taas vahvistetuilla lapsiavaimilla on indeksi välillä 2 potenssiin 31 - 2 potenssiin 32 miinus 1.
![image](assets/image/section4/9.webp)

![image](assets/image/section4/10.webp)

On olemassa kaksi tyyppiä lapsiavainpareja: vahvistetut parit ja normaalit parit. Lapsiavainten johdannan prosessi käyttää julkisia avaimia kulutusehtojen luomiseen, kun taas yksityisiä avaimia käytetään allekirjoittamiseen. Laajennettu julkinen avain sallii vain normaalien lapsi julkisten avainten johdannon, kun taas laajennettu yksityinen avain mahdollistaa kaikkien lapsiavainten, sekä julkisten että yksityisten, johdannon normaalissa tai vahvistetussa tilassa.

![image](assets/image/section4/11.webp)
![image](assets/image/section4/12.webp)

Vahvistettu johdanto käyttää vanhemman yksityistä avainta, kun taas normaali johdanto käyttää vanhemman julkista avainta. HMAC-SHA512-funktiota käytetään vahvistetussa johdannossa, kun taas normaali johdanto käyttää 512-bittistä tiivistettä. Lapsi julkinen avain saadaan kertomalla lapsi yksityinen avain elliptisen käyrän generaattorilla.

![image](assets/image/section4/13.webp)
![image](assets/image/section4/14.webp)

Hierarkkisesti johdettaessa ja määrittämällä monia avainpareja deterministisesti mahdollistetaan hierarkkisen johdannon puurakenteen luominen. Seuraavassa oppitunnissa tässä koulutuksessa tutkimme HD-lompakon rakennetta sekä johdannon polkuja, erityisesti keskittyen johdannon polkunotaatioihin.

## Lompakon Rakenne ja Johdannon Polut
<chapterId>34e1bbda-67de-5493-b268-1fded8d67689</chapterId>

Tässä luvussa tutkimme Hierarkkisen Deterministisen Lompakon (HD Wallet) johdannon puun rakennetta. Olemme jo tutkineet siemenlaskentaa, pääavainta ja lasten avainparien johdantoa. Nyt keskitymme avainten järjestämiseen lompakossa.

HD-lompakko käyttää syvyystasoja avainten järjestämiseen. Jokainen johdanto vanhemmasta parista lapsipariin vastaa syvyystasoa.

![image](assets/image/section4/15.webp)

- Syvyys 0 vastaa pääavainta ja pääketjukoodia.

- Syvyys 1:llä johdetaan lapsiavaimia tiettyyn tarkoitukseen, joka määräytyy indeksin perusteella. Tarkoitukset noudattavat BIP 84 ja Segwit v0/v1 standardeja.

- Syvyys 2 mahdollistaa eri kryptovaluuttojen tai verkkojen tilien erottelun. Tämä mahdollistaa lompakon järjestämisen eri rahoituslähteiden perusteella. Bitcoinille indeksi on 0.

- Syvyys 3:lla järjestetään lompakko eri tileihin, tarjoten selkeämmän ja järjestäytyneemmän rakenteen.

- Syvyys 4 vastaa ulkoisia ja sisäisiä ketjuja, joita käytetään julkisesti kommunikoitaviksi tarkoitettuihin osoitteisiin. Indeksi 0 liittyy ulkoiseen ketjuun, kun taas indeksi 1 liittyy sisäiseen ketjuun. Jokaisella tilillä on kaksi ketjua: ulkoinen ketju (0) ja sisäinen ketju (1). Syvyys 4:ää käytetään myös käsikirjoitustyyppien hallintaan moniallekirjoituslompakoissa.

- Syvyys 5:llä käytetään vastaanotto-osoitteita standardilompakossa. Seuraavassa osiossa tutkimme lasten avainparien johdantoa yksityiskohtaisemmin.

![image](assets/image/section4/16.webp)

Jokaisella syvyystasolla käytämme indeksejä lasten avainparien erottamiseen.
Indeksi ilman heittomerkkiä vastaa todellista käytettyä indeksiä, kun taas indeksi heittomerkin kanssa vastaa todellista indeksiä + 2^31. Kovetetut johdannaiset käyttävät indeksejä väliltä 2^31 - 2^32-1. Esimerkiksi indeksi 44' vastaa todellista indeksiä 2^31 + 44.
Erityisen vastaanotto-osoitteen luomiseksi johdamme lapsiavainparin pääavaimesta ja pääketjukoodista. Sitten käytämme indeksiä erottamaan eri lapsiavainparit samalla syvyydellä.

Laajennetut avaimet, kuten XPUB, mahdollistavat lompakon jakamisen useiden ihmisten kanssa. Johdannaispolkua käytetään erottamaan ulkoinen ketju (osoitteet, jotka on tarkoitettu jaettaviksi) ja sisäinen ketju (vaihto-osoitteet).

Seuraavassa luvussa tutkimme vastaanotto-osoitteita, niiden käytön etuja ja niiden rakentamiseen liittyviä vaiheita.

# Mikä on Bitcoin-osoite?
<partId>81ec8d17-f8ee-5aeb-8035-d370866f4281</partId>

## Bitcoin-osoitteet
<chapterId>0a887ed8-3424-5a52-98e1-e4b406150475</chapterId>

Tässä luvussa tutkimme vastaanotto-osoitteita, jotka ovat keskeisessä roolissa Bitcoin-järjestelmässä. Ne mahdollistavat varojen vastaanottamisen siirrossa ja ne luodaan yksityisten ja julkisten avainten pareista. Vaikka on olemassa skriptityyppi nimeltä Pay2PublicKey, joka mahdollistaa bitcoinien lukitsemisen julkiseen avaimen, käyttäjät suosivat yleensä vastaanotto-osoitteita tämän skriptin sijaan.

![image](assets/image/section5/0.webp)

Kun vastaanottaja haluaa vastaanottaa bitcoineja, he tarjoavat vastaanotto-osoitteen lähettäjälle sen sijaan, että tarjoaisivat julkisen avaimensa. Osoite on itse asiassa julkisen avaimen tiiviste, jolla on tietty muoto. Julkinen avain johdetaan lapsen yksityisestä avaimesta käyttäen matemaattisia operaatioita, kuten pisteen lisäystä ja kaksinkertaistamista elliptisillä käyrillä.

![image](assets/image/section5/1.webp)

On tärkeää huomata, että osoitteesta ei ole mahdollista palauttaa julkista avainta, eikä julkisesta avaimesta yksityiseen avaimen. Osoitteen käyttö pienentää julkisen avaimen tiedon kokoa, joka alun perin on 512 bittiä.

Bitcoin-osoitteiden kokoa on pienennetty helpottamaan niiden käyttöä. Niissä on tarkistussumma, joka mahdollistaa kirjoitusvirheiden havaitsemisen ja vähentää bitcoinien menettämisen riskiä. Toisaalta julkisilla avaimilla ei ole tarkistussummaa, mikä tarkoittaa, että kirjoitusvirheet voivat johtaa vastaavien varojen menetykseen.

Osoitteet tarjoavat myös toisen turvallisuustason julkisen ja yksityisen tiedon välille, mikä tekee yksityisen avaimen hallinnan vaikeammaksi.

On olennaista korostaa, että jokaista osoitetta tulisi käyttää vain kerran. Saman osoitteen uudelleenkäyttö aiheuttaa yksityisyyteen liittyviä ongelmia ja sitä tulisi välttää.

Bitcoin-osoitteille käytetään erilaisia etuliitteitä. Esimerkiksi BC1Q vastaa Segwit V0 -osoitetta, BC1P Taproot/Segwit V1 -osoitetta, ja etuliitteet 1 ja 3 liittyvät Pay2PublicKeyH/Pay2ScriptH (legacy) -osoitteisiin. Seuraavassa oppitunnissa selitämme vaihe vaiheelta, miten osoite johdetaan julkisesta avaimesta.

## Kuinka luoda Bitcoin-osoite?
<chapterId>6dee7bf3-7767-5f8d-a01b-659b95cfe0a5</chapterId>

Tässä luvussa keskustelemme Bitcoin-siirtojen vastaanotto-osoitteen rakentamisesta. Vastaanotto-osoite on tiivistetty julkisen avaimen alfanumeerinen esitys. Julkisen avaimen muuntaminen vastaanotto-osoitteeksi sisältää useita vaiheita.

### Vaihe 1: Julkisen avaimen tiivistäminen
Osoite johdetaan lapsen julkisesta avaimesta.

Julkinen avain on piste elliptisellä käyrällä. Elliptisen käyrän symmetrian ansiosta käyrällä olevalla pisteellä on x-koordinaatti, johon liittyy vain kaksi mahdollista arvoa y:lle: positiivinen tai negatiivinen.
Bitcoin-protokollassa työskentelemme kuitenkin äärellisen positiivisten kokonaislukujen joukon kanssa, ei reaalilukujen joukon kanssa. Erottaaksemme kaksi mahdollista y:n arvoa riittää ilmoittaa, onko y parillinen vai pariton.

Julkisen avaimen tiivistäminen vähentää sen kokoa 520 bitistä 264 bittiin.

Käytämme etuliitettä 0x02 parilliselle y:lle ja 0x03 parittomalle y:lle. Tämä on julkisen avaimen tiivistetty muoto.

### Vaihe 2: Tiivistetyn julkisen avaimen hajauttaminen

Tiivistetyn julkisen avaimen hajautus suoritetaan käyttäen SHA256-funktiota. Sen jälkeen sovelletaan RIPEMD160-funktiota tiivisteeseen.

### Vaihe 3: Kuorma = Osoitteen kuorma

RIPEMD160(SHA256(K)):n binääritiiviste käytetään muodostamaan 5 bitin ryhmiä. Jokainen ryhmä muunnetaan base16:ksi (heksadesimaaliksi) ja/tai base 10:ksi.

### Vaihe 4: Metatiedon lisääminen tarkistussumman laskemiseksi BCH-ohjelman kanssa

Perinteisissä osoitteissa käytämme kaksinkertaista SHA256-hajautusta osoitteen tarkistussumman tuottamiseksi. Segwit V0 ja V1 osoitteissa luotamme kuitenkin BCH-tarkistussummateknologiaan virheentunnistuksen varmistamiseksi. BCH-ohjelma kykenee ehdottamaan ja korjaamaan virheitä erittäin pienen virhetodennäköisyyden kanssa. Tällä hetkellä BCH-ohjelmaa käytetään havaitsemaan ja ehdottamaan tehtäviä muutoksia, mutta se ei automaattisesti suorita niitä käyttäjän puolesta.

BCH-ohjelma vaatii useita syöttötietoja, mukaan lukien HRP (Human Readable Part), joka on laajennettava. HRP:n laajentaminen sisältää jokaisen kirjaimen koodaamisen base 2:ksi niiden ASCII-koodin mukaan. Sitten otetaan kunkin kirjaimen tuloksen ensimmäiset 3 bittiä ja muunnetaan ne base 10:ksi (kuvassa sinisellä). Lisää erotin 0. Sitten yhdistetään seuraavat 5 bittiä kustakin aiemmin base 10:ksi muunnetusta kirjaimesta (kuvassa keltaisella).

HRP:n laajentaminen base 10:ksi mahdollistaa jokaisen merkin viimeisen viiden bitin eristämisen, vahvistaen näin tarkistussumman.

Segwit V0 -versio on edustettuna koodilla 00 ja "kuorma" on mustana, base 10:ssä. Tämän jälkeen seuraa kuusi varattua merkkiä tarkistussummaa varten.

### Vaihe 5: Tarkistussumman laskeminen BCH-ohjelman avulla

Metatietoa sisältävä syöte toimitetaan sitten BCH-ohjelmalle tarkistussumman saamiseksi base 10:ssä.

Tässä meillä on tarkistussumma.

### Vaihe 6: Osoitteen rakentaminen ja muuntaminen Bech32:ksi

Version, kuorman ja tarkistussumman yhdistäminen mahdollistaa osoitteen rakentamisen. Base 10 merkit muunnetaan sitten Bech32 merkeiksi käyttäen vastaavuustaulukkoa. Bech32 aakkostoon kuuluu kaikki alfanumeeriset merkit, paitsi 1, b, i ja o, välttääkseen mahdollisen sekaannuksen.

### Vaihe 7: HRP:n ja erotinmerkin lisääminen

Pinkillä, tarkistussumma.
Mustassa, kuorma = julkisen avaimen hajautus. Sinisessä, versio.

Kaikki muunnetaan Bech32-muotoon, sitten lisätään 'bc' bitcoinille ja '1' erottimeksi, ja tässä on osoite.

# Mene pidemmälle
<partId>58111408-b734-54db-9ea7-0d5b67f99f99</partId>

## Luodaan siemen 128 nopanheitosta!
<chapterId>0f4d40a7-cf0e-5faf-bc4d-691486771ac1</chapterId>

Mnemonisen lauseen luominen on ratkaiseva askel kryptovaluuttalompakkosi turvaamisessa. On olemassa useita menetelmiä mnemonisen lauseen luomiseksi, mutta keskitymme manuaaliseen menetelmään käyttäen noppaa. On tärkeää huomata, että tämä menetelmä ei sovellu korkean arvon lompakolle. On suositeltavaa käyttää avoimen lähdekoodin ohjelmistoa tai laitteistolompakkoa mnemonisen lauseen luomiseen. Luodaksemme mnemonisen lauseen, käytämme noppaa binääritiedon tuottamiseen. Tavoitteena on ymmärtää mnemonisen lauseen luomisprosessi.

**Vaihe 1 - Valmistelu:**
Varmista, että sinulla on amneesinen Linux-jakelu, kuten Tails OS, asennettuna USB-tikulle lisäturvallisuuden vuoksi. Huomaa, että tätä opasta ei tulisi käyttää pääasiallisen lompakon luomiseen.
**Vaihe 2 - Satunnaisen binääriluvun luominen:**
Käytämme noppaa binääritiedon tuottamiseen. Heitä noppaa 128 kertaa ja kirjaa jokainen tulos (1 parittomille, 0 parillisille).

**Vaihe 3 - Binäärilukujen järjestäminen:**
Järjestä saadut binääriluvut 11 numeron riveihin helpottaaksesi laskelmia. Kahdennentoista rivin tulee sisältää vain 7 numeroa.

**Vaihe 4 - Tarkistussumman laskeminen:**
Kahdennentoista rivin viimeiset 4 numeroa vastaavat tarkistussummaa. Tarkistussumman laskemiseksi tarvitsemme Linux-jakelun terminaalin. On suositeltavaa käyttää [TailOs](https://tails.boum.org/index.fr.html), joka on käynnistettävä muistiton jakelu USB-tikulta. Kun olet terminaalissa, syötä komento `echo <binääriluku> | shasum -a 254 -0`. Korvaa `<binääriluku>` 128 nollallasi ja ykköselläsi. Tuloksena on heksadesimaalinen hajautus. Ota huomioon tämän hajautuksen ensimmäinen merkki ja muunna se binääriksi. Voit käyttää tätä [taulukkoa](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table) apuna. Lisää binäärinen tarkistussumma (4 numeroa) kahdennentoista rivisi loppuun.

**Vaihe 5 - Muunnos desimaaliksi:**
Löytääksesi sanat, jotka liittyvät kuhunkin riviisi, sinun on ensin muunnettava jokainen 11 bitin sarja desimaaliluvuksi. Tässä et voi käyttää verkossa olevaa muunninta, koska nämä bitit edustavat muistisanaasi. Siksi sinun on muunnettava käyttäen laskinta ja seuraavaa niksiä: jokainen bitti vastaa 2:n potenssia, joten vasemmalta oikealle meillä on 11 arvoa, jotka vastaavat 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1. Muuntaaksesi 11 bitin sarjasi desimaaliluvuksi, lisää yksinkertaisesti vain ne arvot, jotka sisältävät ykkösen. Esimerkiksi sarjalle 00110111011, tämä vastaa seuraavaa summaa: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. Voit nyt muuntaa jokaisen rivin desimaaliluvuksi. Ja ennen siirtymistä sanojen koodaamiseen, lisää +1 kaikkiin riveihin, koska BIP39-sanalistan indeksi alkaa 1:stä, ei 0:sta.
**Vaihe 8 - Muistisanan luominen:**
Aloita tulostamalla [2048 sanan lista](https://seedxor.com/files/wordlist.pdf) muuntaaksesi desimaalinumerosi BIP39-sanoiksi. Tämän listan ainutlaatuisuus on, että yksikään sana ei jaa ensimmäisiä 4 kirjainta minkään toisen sanan kanssa tässä sanakirjassa. Etsi sitten sana, joka liittyy kunkin rivisi desimaalinumeroon.
**Vaihe 9 - Muistisanan testaus:**
Testaa välittömästi muistisanasi Sparrow Walletissa luomalla lompakko siitä. Jos saat virheilmoituksen virheellisestä tarkistussummasta, on todennäköistä, että teit laskuvirheen. Korjaa tämä virhe palaamalla vaiheeseen 4 ja testaa uudelleen Sparrow Walletissa. Kas näin! Olet juuri luonut uuden Bitcoin-lompakon 128 nopanheiton perusteella.

Muistisanan luominen on tärkeä prosessi kryptovaluuttalompakkosi turvaamiseksi. On suositeltavaa käyttää turvallisempia menetelmiä, kuten avoimen lähdekoodin ohjelmistoa tai laitteistolompakkoa, muistisanan luomiseen. Tämän työpajan suorittaminen auttaa kuitenkin paremmin ymmärtämään, miten voimme luoda Bitcoin-lompakon satunnaisesta numerosta.

## BONUS: Haastattelu Théo Pantamisin kanssa
<chapterId>39f0ec5a-e258-55cb-9789-bc46d314d816</chapterId>

Toinen laajalti käytetty kryptografinen menetelmä Bitcoin-protokollassa on digitaalisten allekirjoitusten menetelmä.

![video](https://youtu.be/c9MvtGJsEvY?si=bQ1N5NCd6op0G6nW)



## Arvioi kurssi
<chapterId>0cd71541-a7fd-53db-b66a-8611b6a28b04</chapterId>
<isCourseReview>true</isCourseReview>

## Loppukoe
<chapterId>a53ea27d-0f84-56cd-b37c-a66210a4b31d</chapterId>
<isCourseExam>true</isCourseExam>


## Yhteenveto ja loppu
<chapterId>d291428b-3cfa-5394-930e-4b514be82d5a</chapterId>

### Kiitokset ja jatka kaninkolon tutkimista

Haluamme vilpittömästi kiittää sinua Crypto 301 -kurssin suorittamisesta. Toivomme, että kokemus on ollut rikastuttava ja opettavainen sinulle. Olemme käsitelleet monia jännittäviä aiheita, jotka ulottuvat matematiikasta kryptografiaan ja Bitcoin-protokollan toimintaan.

Jos haluat syventyä aiheeseen, meillä on tarjota sinulle lisäresurssi. Teimme eksklusiivisen haastattelun Théo Pantamisin ja Loïc Morelin kanssa, jotka ovat tunnettuja asiantuntijoita kryptografian alalla. Tämä haastattelu tutkii aihetta syvällisesti ja tarjoaa mielenkiintoisia näkökulmia.

Katso tämä haastattelu jatkaaksesi kryptografian kiehtovan alueen tutkimista. Toivomme, että se on hyödyllinen ja inspiroiva matkallasi. Kiitämme vielä kerran osallistumisestasi ja sitoutumisestasi kurssin aikana.

### Tukemme
Tämä kurssi, kuten kaikki tämän yliopiston sisältö, on tarjottu sinulle ilmaiseksi yhteisömme toimesta. Voit tukea meitä jakamalla sen muiden kanssa, liittymällä yliopiston jäseneksi ja jopa osallistumalla sen kehittämiseen GitHubin kautta. Koko tiimin puolesta, kiitos!
### Arvioi kurssi
Koulutuksen arvostelujärjestelmä integroidaan pian tähän uuteen E-oppimisalustaan! Siihen asti, suurkiitokset kurssin suorittamisesta, ja jos pidit siitä, harkitse sen jakamista muiden kanssa.
