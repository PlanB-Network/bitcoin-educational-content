---
name: Johdatus kryptografiaan
goal: Ymmärtää Bitcoin-lompakon luominen kryptografisesta näkökulmasta
objectives:
  - Selkeyttää Bitcoinin kryptografiaan liittyvää terminologiaa.
  - Hallita Bitcoin-lompakon luomisen.
  - Ymmärtää Bitcoin-lompakon rakenne.
  - Ymmärtää osoitteet ja johdannaispolut.
---

# Matka kryptografian maailmaan

Oletko lumoutunut Bitcoinista? Mietitkö, miten Bitcoin-lompakko toimii? Valmistaudu kiehtovalle matkalle kryptografian syövereihin! Loïc, asiantuntijamme, johdattaa sinut Bitcoin-lompakon luomisen monimutkaisuuksiin, paljastaen pelottavilta vaikuttavien teknisten termien, kuten hajautus, avainjohdannaiset ja elliptiset käyrät, mysteerit.

Tämä koulutus ei ainoastaan varusta sinua tiedolla Bitcoin-lompakon rakenteesta, vaan myös valmistaa sinut sukeltamaan syvemmälle kryptografian jännittävään maailmaan. Oletko valmis tälle matkalle? Liity seuraamme ja muuta uteliaisuutesi asiantuntemukseksi!

+++

# Johdanto

## Johdatus kryptografiaan

### Onko tämä koulutus sinulle? KYLLÄ!

![johdanto Rogzyn toimesta](https://youtu.be/ul8zU5QWIXg)

Olemme iloisia voidessamme toivottaa sinut tervetulleeksi uudelle koulutuskurssille nimeltä "Crypto 301: Johdatus kryptografiaan ja HD-lompakkoon", jonka on orkestroinut asiantuntija itse, Loïc Morel. Tämä kurssi vie sinut kryptografian kiehtovaan maailmaan, matematiikan perusalaan, joka varmistaa tietojesi salauksen ja turvallisuuden.

Päivittäisessä elämässämme, ja erityisesti Bitcoinin alueella, kryptografialla on ratkaiseva rooli. Kryptografiaan liittyvät käsitteet, kuten yksityiset avaimet, julkiset avaimet, osoitteet, johdannaispolut, siemen ja entropia, ovat keskeisiä Bitcoin-lompakon käytössä ja luomisessa. Kurssin aikana Loïc selittää yksityiskohtaisesti, miten yksityiset avaimet luodaan ja miten ne liittyvät osoitteisiin. Loïc käyttää myös tunnin elliptisten käyrien matemaattisten yksityiskohtien selittämiseen, tämä monimutkainen matemaattinen käyrä. Lisäksi ymmärrät, miksi HMAC SHA512:n käyttö on tärkeää lompakkosi turvaamisessa ja mikä ero on siemenen ja mnemonisen lauseen välillä.

Tämän koulutuksen lopullisena tavoitteena on mahdollistaa sinun ymmärtää HD-lompakon luomisen tekniset prosessit ja käytetyt kryptografiset menetelmät. Vuosien varrella Bitcoin-lompakot ovat kehittyneet helpommin käytettäviksi, turvallisemmiksi ja standardoiduiksi kiitos tiettyjen BIPien. Loïc auttaa sinua ymmärtämään nämä BIPit käsittääksesi Bitcoin-kehittäjien ja kryptografien tekemät valinnat. Kuten kaikki yliopistomme tarjoamat koulutukset, tämäkin on täysin ilmainen ja avoimen lähdekoodin. Tämä tarkoittaa, että voit vapaasti ottaa sen ja käyttää sitä haluamallasi tavalla. Odotamme innolla palautettasi tämän jännittävän kurssin päätteeksi.

### Puheenvuoro on sinun, professori!

![johdanto Loïcin toimesta](https://youtu.be/mwuxXLk4Kws)

Hei kaikki, olen Loïc Morel, oppaanne tässä teknisessä tutkimusmatkassa Bitcoin-lompakoiden käyttämään kryptografiaan.

Matkamme alkaa syväsukelluksella kryptografisten hajautusfunktioiden syvyyksiin. Yhdessä pureudumme SHA256:n olennaiseen sisältöön ja tutkimme erilaisia johdannaisalgoritmeja.

Jatkamme seikkailuamme purkamalla digitaalisten allekirjoitusten mystisen maailman. Löydätte, miten elliptisten käyrien taika soveltuu näihin allekirjoituksiin, ja valaisemme, miten julkinen avain lasketaan yksityisestä avaimesta. Ja tietenkin käsittelemme yksityisellä avaimella allekirjoittamista.
Seuraavaksi palaamme ajassa taaksepäin nähdäksemme Bitcoin-lompakoiden kehityksen, ja sukellamme entropian ja satunnaislukujen käsitteisiin. Käymme läpi kuuluisan mnemonisen lauseen, samalla syventyen salasanojen aiheeseen. Sinulla on jopa mahdollisuus kokea jotain ainutlaatuista luomalla siemen 128 nopanheitosta!

Näiden vankkojen perusteiden myötä olemme valmiita ratkaisevaan osaan: Bitcoin-lompakon luomiseen. Siemenen syntymästä ja pääavaimesta, laajennettujen avainten tutkimiseen, ja lasten avainparien johdannaisiin, jokainen vaihe puretaan osiin. Keskustelemme myös lompakon rakenteesta ja johdannaispoluista.

Kaiken huipuksi päätämme matkamme tutkimalla Bitcoin-osoitteita. Selitämme, miten ne luodaan ja miten ne ovat olennaisessa roolissa Bitcoin-lompakoiden toiminnassa.

Liity mukaan tälle kiehtovalle matkalle, ja valmistaudu tutkimaan kryptografian maailmaa aivan uudella tavalla. Jätä ennakkokäsityksesi oven ulkopuolelle ja avaa mielesi uudelle tavalle ymmärtää Bitcoin ja sen perusrakenne.

# Hajasfunktiot

## Johdanto kryptografisiin hajasfunktioihin liittyen Bitcoiniin

![2.1 - Kryptografiset Hajasfunktiot](https://youtu.be/dvnGArYvVr8)

Tervetuloa tämän päivän istuntoon, joka on omistettu syvälle sukeltamiselle kryptografian maailmaan hajasfunktioista, jotka ovat olennainen kulmakivi Bitcoin-protokollan turvallisuudessa. Kuvittele hajasfunktio erittäin tehokkaaksi kryptografiseksi purkurobotiksi, joka muuntaa kaikenkokoisen tiedon ainutlaatuiseksi ja kiinteän kokoiseksi digitaaliseksi sormenjäljeksi, kutsutuksi "hashiksi". Tutkimusmatkamme aikana hahmottelemme kryptografisten hajasfunktioiden profiilia, korostaen niiden käyttöä Bitcoin-protokollassa, ja määrittelemme erityiset tavoitteet, jotka näiden kryptografisten funktioiden on saavutettava.

![kuva](assets/image/section1/0.JPG)

Kryptografisten hajasfunktioiden profiilin hahmottaminen vaatii kahden olennaisen ominaisuuden ymmärtämistä: niiden peruuttamattomuutta ja väärentämisen vastustuskykyä. Jokainen kryptografinen hajasfunktio on kuin ainutlaatuinen taiteilija, tuottaen erillisen "hashin" jokaiselle syötteelle. Jopa hieman poikkeava siveltimen veto muuttaa merkittävästi lopputulosta, eli hashia. Nämä funktiot toimivat digitaalisina vartijoina, varmistaen ladatun ohjelmiston eheyden. Toinen niiden keskeinen ominaisuus on niiden vastustuskyky törmäyksille. Törmäykset ovat väistämättömiä hashimaailmassa, mutta erinomainen kryptografinen hajasfunktio vähentää niitä merkittävästi. Se on kuin jokainen hash olisi talo valtavassa kaupungissa; huolimatta valtavasta talojen määrästä, hyvä hajasfunktio varmistaa, että jokaisella talolla on ainutlaatuinen osoite.

![kuva](assets/image/section1/1.JPG)

Navigoidaan nyt vanhentuneiden hajasfunktioiden myrskyisillä vesillä. SHA0, SHA1 ja MD5 katsotaan nyt ruosteisiksi reliikeiksi kryptografisen hashauksen valtameressä. Niitä usein vältetään, koska ne ovat menettäneet vastustuskykynsä törmäyksille. Laatikoiden periaate selittää, miksi törmäysten välttäminen on mahdotonta ulostulokoon rajoituksen vuoksi. On myös tärkeää huomata, että vastustuskyky toista esikuvaa vastaan riippuu vastustuskyvystä törmäyksiä vastaan. Ollakseen todella turvallinen, hajasfunktion on vastustettava törmäyksiä, toista esikuvaa ja esikuvaa.

Avainelementtinä Bitcoin-protokollassa, SHA-256 hajasfunktio on laivan kapteeni. Muita funktioita, kuten SHA-512, käytetään johdannaisiin HMAC:n ja PBKDF:n kanssa. Lisäksi RIPMD160:tä käytetään sormenjäljen pienentämiseen 160 bittiin. Kun puhumme HASH256:sta ja HASH160:sta, viittaamme SHA-256:n ja RIPMD:n kaksoishashauksen käyttöön. HASH160:n käyttö on erityisen edullista, koska se mahdollistaa SHA-256:n turvallisuuden säilyttämisen samalla kun sormenjäljen kokoa pienennetään.
Yhteenvetona voidaan sanoa, että kryptografisen hajautusfunktion päätavoite on muuntaa mielivaltaisen kokoiset tiedot kiinteän kokoiseksi sormenjäljeksi. Jotta sitä voidaan pitää turvallisena, sen on oltava useiden vahvuuksien omaava: peruuttamattomuus, väärentämisen kestävyys, törmäysten kestävyys ja toisen esikuvan kestävyys.
![kuva](assets/image/section1/2.JPG)

Tämän tutkimusmatkan päätteeksi olemme selvittäneet kryptografisten hajautusfunktioiden mysteerit, korostaneet niiden käyttöä Bitcoin-protokollassa ja pureutuneet niiden erityisiin tavoitteisiin. Olemme oppineet, että jotta hajautusfunktioita voidaan pitää turvallisina, niiden on oltava kestäviä esikuvaa, toista esikuvaa, törmäyksiä ja väärentämistä vastaan. Olemme myös käsitelleet erilaisia hajautusfunktioita, joita käytetään Bitcoin-protokollassa. Seuraavassa istunnossamme syvennymme SHA256-hajautusfunktion ytimeen ja löydämme sen ainutlaatuiset ominaisuudet mahdollistavan kiehtovan matematiikan.

## SHA256:n sisäinen toiminta

![SHA256:n sisäinen toiminta](https://youtu.be/74SWg_ZbUj4)

Tervetuloa jatkamaan kiehtovaa matkaamme kryptografisten hajautusfunktioiden sokkeloissa. Tänään paljastamme SHA256:n mysteerit, monimutkaisen mutta nerokkaan prosessin, jonka esittelimme edellisessä keskustelussamme hajautusfunktioista. Otetaan toinen askel tässä sokkelossa, aloittaen SHA256:n esikäsittelystä. Kuvittele esikäsittely herkullisen ruokalajin valmisteluna, jossa lisäämme "täytebittejä" saadaksemme pääraaka-aineemme, syötteen, koon täydelliseksi 512 bitin monikertaiseksi. Kaiken tämän lopullisena tavoitteena on tuottaa herkullinen 256-bittinen hajautus muuttuvankokoisesta ainesosasta.

![kuva](assets/image/section1/3.JPG)
![kuva](assets/image/section1/4.JPG)

Tässä kryptografisessa reseptissä leikimme bitteillä, joilla on alkuviestin koko, jonka kutsumme M:ksi. Yksi bitti on varattu erotinmerkille, kun taas P bittejä käytetään täytteeseen. Lisäksi varataan 64 bittiä toista esikäsittelyvaihetta varten. Kokonaisuuden on oltava 512 bitin monikertainen. Se on vähän kuin varmistaisimme, että kaikki ainekset sekoittuvat täydellisesti ruokalajissamme.

![kuva](assets/image/section1/5.JPG)

Siirrymme nyt esikäsittelyn toiseen vaiheeseen, joka sisältää alkuperäisen viestin koon binääriesityksen lisäämisen bitteinä. Tätä varten käytämme edellisessä vaiheessa varaamiamme 64 bittiä. Lisäämme nollia pyöristääksemme 64 bittimme tasapainoiseen syötteeseen. Sitten yhdistämme alkuperäisen viestin, täytebitit ja koon täytteen kuin ainekset tehosekoittimessa, saadaksemme tasapainoisen syötteen.

![kuva](assets/image/section1/6.JPG)

Nyt valmistaudumme SHA-256 -funktion käsittelyn ensimmäisiin vaiheisiin. Kuten missä tahansa hyvässä reseptissä, tarvitsemme joitakin perusraaka-aineita, joita kutsumme vakioiksi ja alustusvektoreiksi. Alustusvektorit, A:sta H:hen, ovat ensimmäisten 8 alkuluvun neliöjuurten desimaaliosien ensimmäiset 32 bittiä. Vakiot K, 0:sta 63:een, edustavat ensimmäisten 64 alkuluvun kuutiojuurten desimaaliosien ensimmäisiä 32 bittiä.

![kuva](assets/image/section1/7.JPG)

Puristustoiminnossa käytämme tiettyjä operaattoreita, kuten XOR, AND ja NOT. Käsittelemme bitit yksi kerrallaan niiden järjestyksen mukaan käyttäen XOR-operaattoria ja totuustaulukkoa. AND-operaattoria käytetään palauttamaan 1 vain, jos molemmat operandit ovat yhtä suuret kuin 1, ja NOT-operaattoria palauttamaan operandin vastakkainen arvo. Käytämme myös SHR-toimintoa siirtämään bittejä oikealle valitulla numerolla.

![kuva](assets/image/section1/8.JPG)
![kuva](assets/image/section1/9.JPG)
Lopuksi, kun tasapainotettu syöte on jaettu eri 512-bittisiin viestilohkoihin, suoritamme 64 laskentakierrosta tiivistysfunktiossa. Kuin pyöräilykilpailussa, jokainen kierros parantaa asemaamme. Lisäämme modulo 2^32 väliaikaisen tilan alkuperäiseen tiivistysfunktion tilaan. Tiivistysfunktion lisäykset ovat modulo 2^32 lisäyksiä, jotta summien koko pysyy 32 bittinä.

![kuva](assets/image/section1/10.JPG)
![kuva](assets/image/section1/11.JPG)
![kuva](assets/image/section1/12.JPG)
![kuva](assets/image/section1/13.JPG)

Lopuksi haluaisimme korostaa CH, MAJ, σ0 ja σ1 -laatikoiden suorittamien laskentojen ratkaisevaa roolia. Nämä toiminnot, muiden joukossa, ovat vartijoita, jotka varmistavat SHA256-tiivistysfunktion robustiuden hyökkäyksiä vastaan, tehden siitä suositun valinnan lukuisien digitaalisten järjestelmien turvaamisessa, erityisesti Bitcoin-protokollan yhteydessä. On selvää, että vaikka monimutkainen, SHA256:n kauneus piilee sen kyvyssä löytää syöte hashista, kun taas hashin varmentaminen annetulle syötteelle on mekaanisesti yksinkertainen toiminto.

## Käytetyt algoritmit johdannaisille

![Käytetyt algoritmit johdannaisille](https://youtu.be/ZF1_BMsOJXc)

HMAC ja PBKDF2 johdannaisalgoritmit ovat keskeisiä komponentteja Bitcoin-protokollan turvamekanismissa. Ne estävät monenlaisia potentiaalisia hyökkäyksiä ja varmistavat Bitcoin-lompakoiden eheyden.

HMAC ja PBKDF2 ovat kryptografisia työkaluja, joita käytetään eri tehtäviin Bitcoinissa. HMAC:ia käytetään ensisijaisesti pituuden laajennushyökkäysten torjumiseen hierarkkisesti determinististen (HD) lompakoiden johdannaisissa, kun taas PBKDF2:ta käytetään muuntamaan mnemoninen lause siemeneksi.

![kuva](assets/image/section1/14.JPG)

HMAC, joka ottaa syötteinä viestin ja avaimen, tuottaa kiinteän kokoisen tulosteen. Avaimen yhtenäisyyden varmistamiseksi sitä säädellään hash-funktion käyttämän lohkokoon mukaan. HD-lompakoiden johdannaisissa käytetään HMAC-SHA-512:ta. Jälkimmäinen toimii 1024-bittisillä (128-tavuisilla) lohkoilla ja säätää avainta vastaavasti. Se käyttää vakioita OPAD (0x5c) ja IPAD (0x36), jotka toistetaan tarvittaessa turvallisuuden parantamiseksi.

HMAC-SHA-512 -prosessi sisältää SHA-512:n tuloksen yhdistämisen avaimen XOR OPAD ja avaimen XOR IPAD kanssa viestiin. Kun käytetään 1024-bittisiä (128-tavuisia) lohkoja, syöteavain täytetään tarvittaessa nollilla, sitten XORataan IPAD:n ja OPAD:n kanssa. Muokattu avain yhdistetään sitten viestiin.

![kuva](assets/image/section1/15.JPG)

Suolan käyttö, lisäämällä ylimääräinen entropian lähde, lisää johdettujen avainten turvallisuutta. Ilman sitä hyökkäys voisi vaarantaa koko lompakon ja varastaa kaikki bitcoinit.
PBKDF2:tä käytetään muuntamaan mnemoninen lause siemeneksi. Tämä algoritmi suorittaa 2048 kierrosta käyttäen HMAC SHA512:ta. Kiitos näiden johdannaisalgoritmien, kaksi eri syötettä voi tuottaa yksilöllisen ja kiinteän tuloksen, mikä lieventää mahdollisten pituuslaajennushyökkäysten ongelmaa SHA-2 perheen funktioissa. Pituuslaajennushyökkäys hyödyntää tiettyjen kryptografisten hajautusfunktioiden erityisominaisuutta. Tällaisessa hyökkäyksessä hyökkääjä, jolla on jo tuntemattoman viestin hajautus, voi käyttää sitä laskemaan pidemmän viestin hajautuksen, joka on alkuperäisen viestin laajennus. Tämä on usein mahdollista tietämättä alkuperäisen viestin sisältöä, mikä voi johtaa merkittäviin turvallisuusriskeihin, jos tätä tyyppistä hajautusfunktiota käytetään tehtäviin, kuten eheyden varmistamiseen.
![kuva](assets/image/section1/16.JPG)

Yhteenvetona voidaan todeta, että HMAC- ja PBKDF2-algoritmit ovat olennaisia rooleja HD-lompakon johdannan turvallisuudessa Bitcoin-protokollassa. HMAC-SHA-512:tä käytetään suojaamaan pituuslaajennushyökkäyksiltä, kun taas PBKDF2 mahdollistaa mnemonisen lauseen muuntamisen siemeneksi. Ketjukoodi lisää ylimääräisen entropian lähteen avainjohdannassa, varmistaen järjestelmän vankkuuden.

# Digitaaliset Allekirjoitukset

## Digitaaliset Allekirjoitukset ja Elliptiset Käyrät

![Digitaaliset Allekirjoitukset ja Elliptiset Käyrät](https://youtu.be/gOjYiPkx4z8)

Kryptovaluuttojen maailmassa transaktioiden turvallisuus on ensiarvoisen tärkeää. Bitcoin-protokollan ytimessä digitaalisia allekirjoituksia käytetään matemaattisina todisteina, jotka osoittavat yksityisen avaimen hallinnan, joka liittyy tiettyyn julkiseen avaimen. Tämä datan suojaustekniikka perustuu olennaisesti kiehtovaan kryptografian alaan, jota kutsutaan elliptisen käyrän kryptografiaksi (ECC).

![kuva](assets/image/section2/0.JPG)

Elliptinen käyräkryptografia on Bitcoin-transaktioiden turvallisuuden selkäranka. Nämä elliptiset käyrät, jotka muistuttavat koulussa opiskelemiamme matemaattisia käyriä, ovat hyödyllisiä monenlaisissa kryptografisissa sovelluksissa, alkaen avaintenvaihdosta aina asymmetriseen salaukseen ja digitaalisten allekirjoitusten luomiseen. Mielenkiintoinen yksityiskohta, joka erottaa elliptiset käyrät, on niiden symmetria: mikä tahansa ei-pystysuora viiva, joka leikkaa kaksi pistettä käyrällä, leikkaa kolmannen pisteen.

Nyt kaivetaan hieman syvemmälle: Bitcoin-protokolla käyttää tiettyä elliptistä käyrää nimeltä SecP256K1 suorittamaan kryptografiset operaationsa. Tämä käyrä, joka on määritelty positiivisten kokonaislukujen äärellisessä joukossa modulo 256-bittinen alkuluku, voidaan visualisoida pistepilvenä pikemminkin kuin perinteisenä käyränä. Juuri tämä ainutlaatuinen suunnittelu mahdollistaa Bitcoinin transaktioiden tehokkaan turvaamisen.

![kuva](assets/image/section2/1.JPG)

Mitä tulee secp256k1-käyrän valintaan Bitcoinille, on mielenkiintoista huomata, että se valittiin secp256r1-käyrän sijaan. Tämä käyrä on määritelty parametreilla a=0 ja b=7, ja sen yhtälö on y² = x³ + 7 modulo n, missä n edustaa alkulukua, joka määrittää käyrän järjestyksen.

Kun puhumme Bitcoin-järjestelmässä käytetyistä vakioista, viittaamme yleensä tiettyihin Elliptisen Käyrän Digitaalisen Allekirjoituksen Algoritmin (ECDSA) ja Bitcoinin käyttämän elliptisen käyräjärjestelmän, joka on secp256k1-käyrä, parametreihin. Tässä ovat nämä parametrit:
- alkulukualue (p): Bitcoin käyttää käyrää alkulukualueen yli, joten p on ensimmäinen numero, jolla tämä alue määritellään. secp256k1-käyrälle p on yhtä suuri kuin `p = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE FFFFFC2F` heksadesimaalilukuna tai p = 2^256 - 2^32 - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 -1 desimaalilukuna.
- käyrän järjestys (n): Tämä on pisteiden määrä käyrällä, mukaan lukien äärettömyydessä oleva piste. secp256k1:lle n on yhtä suuri kuin `n = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE BAAEDCE6 AF48A03B BFD25E8C D0364141` heksadesimaalilukuna tai n = 2^256 - 432420386565659656852420866394968145599 desimaalilukuna.
- generaattoripiste (G): Peruspiste eli generaattori on piste käyrällä, josta kaikki muut julkiset avaimet generoidaan. Sillä on tiettyjä x- ja y-koordinaatteja, jotka yleensä esitetään heksadesimaalilukuna. secp256k1:lle koordinaatit G ovat heksadesimaalilukuna:
  - `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
  - `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

Huomaa, että kaikki heksadesimaaliarvot esitetään yleensä 16-järjestelmässä, kun taas desimaaliarvot ovat 10-järjestelmässä. Lisäksi kaikki näihin vakioihin kohdistuvat operaatiot suoritetaan modulo p pisteiden koordinaattien osalta käyrällä ja modulo n avain- ja allekirjoitusoperaatioiden osalta.

Joten missä nämä kuuluisat bitcoinit säilytetään? Ei Bitcoin-lompakossa, kuten voisi luulla. Todellisuudessa Bitcoin-lompakko säilyttää yksityisiä avaimia, jotka ovat tarpeen bitcoinien omistajuuden todistamiseksi. Bitcoinit itsessään kirjataan lohkoketjuun, hajautettuun tietokantaan, joka arkistoi kaikki tapahtumat.

Bitcoin-järjestelmässä tilin yksikkö on bitcoin (huomaa pieni "b"). Se on jaettavissa kahdeksaan desimaalipaikkaan, ja pienin yksikkö on satoshi. UTXO:t eli "Käyttämättömät Tapahtuma-Outputit" edustavat käyttäjän käyttämättömiä tapahtuma-outputteja. Näiden bitcoinien käyttämiseksi on osoitettava omistajuus yksityisavaimella, joka vastaa kutakin UTXO:ta linkitettyä julkista avainta.

Tapahtumaturvallisuuden varmistamiseksi Bitcoin nojaa kahteen digitaalisen allekirjoituksen protokollaan: ECDSA (Elliptic Curve Digital Signature Algorithm) ja Schnorr. ECDSA on allekirjoitusprotokolla, joka on integroitu Bitcoiniin sen käynnistyksestä lähtien vuonna 2009, kun taas Schnorr-allekirjoitukset lisättiin hiljattain marraskuussa 2021. Vaikka molemmat protokollat perustuvat elliptiseen käyräkryptografiaan ja käyttävät samankaltaisia matemaattisia mekanismeja, ne eroavat pääasiassa allekirjoituksen rakenteen osalta.

Ennen kuin syvennytään näihin allekirjoitusmekanismeihin, on tärkeää ymmärtää, mikä elliptinen käyrä on. Elliptinen käyrä määritellään yhtälöllä y² = x³ + ax + b. Jokaisella tämän käyrän pisteellä on erottuva symmetria, joka on avainasemassa sen hyödyllisyydessä kryptografiassa.
Lopulta erilaiset elliptiset käyrät tunnustetaan turvallisiksi kryptografiseen käyttöön. Ehkä tunnetuin näistä on secp256r1-käyrä. Bitcoinin kohdalla Satoshi Nakamoto kuitenkin valitsi eri käyrän: secp256k1.

Seuraavassa osassa tätä kurssia tarkastelemme tarkemmin julkista avainta ja yksityistä avainta, jotta ymmärrämme perusteellisesti kryptografian elliptisillä käyrillä ja digitaalisen allekirjoituksen algoritmin. Tämä on aika vahvistaa tietosi ja ymmärtää, miten kaikki tämä tieto yhdistyy varmistaakseen Bitcoin-protokollan turvallisuuden.

## Julkisen avaimen laskeminen yksityisestä avaimesta

![Julkisen avaimen laskeminen yksityisestä avaimesta](https://youtu.be/NJENwFU889Y)

Seuraavassa osassa tätä kurssia syvennymme julkisten ja yksityisten avainten mekanismeihin, jotka ovat kaksi Bitcoin-protokollan keskeistä elementtiä. Nämä avaimet ovat olennaisesti yhteydessä toisiinsa Elliptisen Käyrän Digitaalisen Allekirjoituksen Algoritmin (ECDSA) kautta. Niiden ymmärtäminen antaa meille syvällisen käsityksen siitä, miten Bitcoin turvaa transaktioita alustallaan.

![kuva](assets/image/section2/3.JPG)
![kuva](assets/image/section2/4.JPG)

Aloitetaan sukeltamalla ECDSA-algoritmin maailmaan. Bitcoin käyttää tätä digitaalista allekirjoitusalgoritmia yhdistämään yksityiset ja julkiset avaimet. Tässä järjestelmässä yksityinen avain on satunnainen tai pseudosatunnainen 256-bittinen numero. Yksityisen avaimen mahdollisuuksien teoreettinen määrä on 2^256, mutta todellisuudessa se on hieman vähemmän. Tarkemmin sanottuna jotkut 256-bittiset yksityiset avaimet eivät kelpaa Bitcoinille.

![kuva](assets/image/section2/5.JPG)

Jotta yksityinen avain olisi yhteensopiva Bitcoinin kanssa, sen on oltava välillä 1 ja n-1, missä n edustaa elliptisen käyrän järjestystä. Tämä tarkoittaa, että Bitcoinin yksityisen avaimen mahdollisuuksien kokonaismäärä on lähes yhtä suuri kuin 1.158 x 10^77. Perspektiivin antamiseksi, tämä on suunnilleen sama määrä atomeja havaittavissa universumissa. Ainutlaatuinen yksityinen avain käytetään sitten johdattamaan 512-bittinen julkinen avain.

![kuva](assets/image/section2/6.JPG)

Julkinen avain, merkitty K:lla, on piste elliptisellä käyrällä, joka johdetaan yksityisestä avaimesta käyttäen pisteoperaatioita käyrällä. On tärkeää huomata, että ECDSA-toiminto on peruuttamaton, mikä tarkoittaa, että yksityistä avainta ei ole mahdollista palauttaa julkisesta avaimesta. Tämä peruuttamattomuus on Bitcoin-lompakon turvallisuuden kulmakivi.

Julkinen avain koostuu kahdesta 256-bittisestä pisteestä, yhteensä 512 bittiä. Se voidaan kuitenkin tiivistää 264-bittiseksi numeroksi. Piste G on lähtökohta kaikkien järjestelmän käyttäjien julkisten avainten laskemiselle.

![kuva](assets/image/section2/7.JPG)

Yksi elliptisten käyrien huomattava ominaisuus on, että käyrää kahdessa pisteessä leikkaava viiva leikkaa myös kolmannen pisteen, jota kutsutaan pisteeksi O. Tätä ominaisuutta käytetään määrittämään piste U, joka on pisteen O vastakohta. Pisteen lisääminen itseensä tapahtuu piirtämällä tangentti käyrälle kyseisessä pisteessä, mikä johtaa uuteen ainutlaatuiseen pisteeseen nimeltä j. Pisteen skalaarikertolasku n:llä vastaa kyseisen pisteen lisäämistä itseensä n kertaa.

![kuva](assets/image/section2/8.JPG)
Nämä operaatiot elliptisen käyrän pisteillä ovat perusta julkisten avainten laskemiselle. Yksityisen avaimen tietäen on helppoa laskea julkinen avain. Kuitenkaan julkisen avaimen tietäminen ei mahdollista yksityisen avaimen laskemista, mikä varmistaa Bitcoin-järjestelmän turvallisuuden. Itse asiassa julkisten ja yksityisten avainten turvallisuus perustuu diskreetin logaritmin ongelmaan, joka on monimutkainen matemaattinen kysymys.
![image](assets/image/section2/9.JPG)

Seuraavassa oppitunnissamme tutkimme, miten digitaalinen allekirjoitus saavutetaan käyttämällä ECDSA-algoritmia yksityisen avaimen kanssa bitcoineja avatakseen. Pysy kuulolla tämän jännittävän kryptovaluuttojen ja kryptografian maailman tutkimusmatkalle.

## Allekirjoittaminen yksityisellä avaimella

![Allekirjoittaminen yksityisellä avaimella](https://youtu.be/h2hIyGgPqkM)

Digitaalisen allekirjoituksen prosessi on keskeinen menetelmä todistaa, että olet yksityisen avaimen haltija paljastamatta sitä. Tämä saavutetaan käyttämällä ECDSA-algoritmia, joka sisältää ainutlaatuisen nonce-arvon määrittämisen, tietyn numeron V laskemisen ja kahdesta osasta, S1 ja S2, koostuvan digitaalisen allekirjoituksen luomisen. On ratkaisevan tärkeää aina käyttää ainutlaatuista nonce-arvoa turvallisuushyökkäysten välttämiseksi. Kuuluisa esimerkki siitä, mitä voi tapahtua, kun tätä sääntöä ei noudateta, on PlayStation 3 -hakkerointi, joka vaarantui nonce-arvon uudelleenkäytön vuoksi.

Erityisesti digitaalisen allekirjoituksen validointiin ECDSA (Elliptic Curve Digital Signature Algorithm) -algoritmilla tyypillisesti sisältyvät seuraavat vaiheet:

1. Varmista, että allekirjoitusarvot, S1 ja S2, ovat välillä [1, n-1]. Jos ei, allekirjoitus on mitätön.
2. Laske S2:n käänteisarvo mod n. Kutsutaan tätä u:ksi. Se lasketaan usein seuraavasti: u = (S2)^-1 mod n.
3. Laske H, joka on allekirjoitetun viestin hajautusarvo.
4. Laske u1 = H _ u mod n ja u2 = S1 _ u mod n.
5. Laske piste P elliptisellä käyrällä käyttäen u1, u2 ja julkista avainta K: P = u1*G + u2*K, missä G on käyrän generaattoripiste.
6. Jos P on äärettömyyden piste, allekirjoitus on mitätön.
7. Laske I = P:n x-koordinaatti mod n.
8. Allekirjoitus on pätevä, jos I on yhtä suuri kuin S1.

![image](assets/image/section2/10.JPG)
![image](assets/image/section2/11.JPG)

On tärkeää huomata, että eri ohjelmistot voivat käyttää erilaisia notaatioita ja joitakin vaiheita voidaan yhdistää tai järjestellä uudelleen, mutta peruslogiikka pysyy samana. Huomaa myös, että kaikki aritmeettiset operaatiot suoritetaan elliptisen käyrän määrittelemässä äärellisessä kentässä (mod n, missä n on käyrän järjestys). Muistutuksena, secp256k1-käyrä (käytössä Bitcoinissa) on n = 2^256 - 432420386565659656852420866394968145599.
Julkisten ja yksityisten avainten generoinnissa on olennaista tutustua elliptiseen käyrään ja generaattoripisteeseen. Julkisen avaimen saamiseksi on valittava satunnainen numero yksityiseksi avaimen, usein kutsuttu `nonce`, ja käytettävä sitä elliptisen käyrän yhtälössä.
Elliptinen käyrä on tehokas työkalu turvallisten julkisten ja yksityisten avainten luomiseen. Esimerkiksi julkisen avaimen 3G saamiseksi piirrät tangentin pisteeseen G, lasket vastakohdan -G saadaksesi 2G, ja sitten lisäät G:n ja 2G:n. Transaktion suorittamiseksi sinun on todistettava tietäväsi luku 3 avaamalla bitcoinit, jotka on yhdistetty julkiseen avaimen 3G.
Digitaalisen allekirjoituksen luomiseksi ja yksityisen avaimen tuntemisen todistamiseksi, joka on yhdistetty julkiseen avaimen 3G, lasket ensin nonce-arvon, sitten pisteen V, joka on yhdistetty tähän nonce-arvoon (annetussa esimerkissä se on 4G). Sitten lasket pisteen T lisäämällä julkinen avain 3G ja piste V, mikä antaa 7G.

![kuva](assets/image/section2/12.JPG)

Digitaalisen allekirjoituksen vahvistaminen on ratkaiseva vaihe ECDSA-algoritmin käytössä, joka mahdollistaa allekirjoitetun viestin aitouden vahvistamisen ilman lähettäjän yksityistä avainta. Tässä on, miten se toimii yksityiskohtaisesti:

Esimerkissämme meillä on kaksi tärkeää arvoa: T ja V. T on numeerinen arvo (7 tässä esimerkissä), ja V on piste elliptisellä käyrällä (tässä edustettuna 4G:llä). Nämä arvot tuotetaan digitaalisen allekirjoituksen luomisen aikana ja lähetetään sitten viestin mukana mahdollistamaan vahvistaminen.

Kun vahvistaja vastaanottaa viestin, hän saa myös nämä kaksi arvoa, T:n ja V:n.

Tässä ovat askeleet, joita vahvistaja seuraa allekirjoituksen vahvistamiseksi:

1. He laskevat ensin viestin hajautusarvon, jota kutsutaan H:ksi.
2. Sitten he laskevat u1:n ja u2:n. Tämän tekemiseksi he käyttävät seuraavia kaavoja:
   - u1 = H \* (S2)^-1 mod n
   - u2 = T \* (S2)^-1 mod n'

# Mnemoninen lause

## Bitcoin-lompakoiden kehitys

![Bitcoin-lompakoiden kehitys](https://youtu.be/6tmu1R9cXyk)

Hierarkkinen Deterministinen Lompakko, tai yleisemmin tunnettu HD-lompakkona, näyttelee merkittävää roolia kryptovaluuttaekosysteemissä. Termi "lompakko" voi olla harhaanjohtava niille, jotka ovat uusia alalla, sillä se ei viittaa rahan tai valuutan pitämiseen. Pikemminkin se viittaa yksityisten kryptografisten avainten kokoelmaan, jotka on johdettu yhdestä pääavaimesta, kiitos nerokkaan algoritmisen aritmetiikan prosessin. Nämä yksityiset avaimet, jotka ovat kiinteän pituisia 256 bittiä, ovat kryptovaluutan omistuksen ydin, ja niitä kutsutaan joskus karkeammalla nimellä "Vain Joukko Avaimia" (JBOC).

![kuva](assets/image/section3/0.JPG)

Kuitenkin näiden avainten hallinnan monimutkaisuus tasapainotetaan protokollasarjalla, joka tunnetaan Bitcoinin Parannusehdotuksina (BIPs). Nämä päivitysehdotukset ovat HD-lompakoiden toiminnallisuuden ja turvallisuuden ytimessä. Esimerkiksi [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), joka julkaistiin vuonna 2012, mullisti näiden avainten luomisen ja tallentamisen tavan, esitellen deterministisesti ja hierarkkisesti johdettujen avainten konseptin. Tämä yksinkertaistaa suuresti näiden avainten tallentamisen prosessia, samalla ylläpitäen niiden turvallisuustasoa.

![kuva](assets/image/section3/1.JPG)
Seuraavaksi [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) esitteli merkittävän innovaation: 24 sanan muistilauseen. Tämä järjestelmä mahdollisti monimutkaisen, vaikeasti muistettavan numerosekvenssin muuttamisen sarjaksi tavallisia sanoja, jotka ovat paljon helpompia muistaa ja säilyttää. Lisäksi [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) ehdotti lisäsalasanan lisäämistä yksittäisten avainten turvallisuuden vahvistamiseksi. Nämä peräkkäiset parannukset johtivat BIP43:n ja BIP44:n kehittämiseen, jotka standardisoivat HD-lompakoiden rakenteen ja hierarkian, tehden niistä yleisölle helpommin saavutettavia ja käytettäviä.

Seuraavissa osioissa syvennymme tarkemmin siihen, miten HD-portfolio toimii. Käsittelemme avainten johdannan periaatteita ja tutkimme entropian ja satunnaislukugeneraation peruskäsitteitä, jotka ovat olennaisen tärkeitä HD-portfoliosi turvallisuuden takaamiseksi.

Hierarkkinen Deterministinen Lompakko, tai yleisemmin tunnettu HD-lompakkona, näyttelee merkittävää roolia kryptovaluuttaekosysteemissä. Termi "lompakko" saattaa olla harhaanjohtava niille, jotka ovat uusia alalla, sillä se ei viittaa rahan tai valuutan säilyttämiseen. Sen sijaan se viittaa yksityisten kryptografisten avainten kokoelmaan, jotka on johdettu yhdestä pääavaimesta nerokkaan algoritmisen aritmetiikan prosessin ansiosta. Nämä yksityiset avaimet, jotka ovat kiinteän pituisia, 256 bittiä, ovat kryptovaluutan omistuksen ydin ja niitä kutsutaan joskus karkeammalla nimellä "Vain Joukko Avaimia" (JBOC).

![kuva](assets/image/section3/0.JPG)

Kuitenkin näiden avainten hallinnan monimutkaisuus tasapainotetaan protokollasarjalla, joka tunnetaan Bitcoinin Parannusehdotuksina (BIPs). Nämä päivitysehdotukset ovat HD-lompakoiden toiminnallisuuden ja turvallisuuden ytimessä. Esimerkiksi [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), joka julkaistiin vuonna 2012, mullisti näiden avainten generoinnin ja tallennuksen tavan, esitellen deterministisesti ja hierarkkisesti johdettujen avainten konseptin. Tämä yksinkertaistaa huomattavasti näiden avainten tallennusprosessia, samalla ylläpitäen niiden turvallisuustasoa.

![kuva](assets/image/section3/1.JPG)

Yhteenvetona on olennaista korostaa BIP32:n ja BIP39:n keskeistä roolia HD-lompakoiden suunnittelussa ja turvallisuudessa. Nämä protokollat mahdollistavat useiden avainten generoinnin yhdestä siemenestä, joka on oletettavasti satunnainen tai pseudosatunnainen numero. Nykyään nämä standardit on omaksuttu valtaosassa kryptovaluuttalompakoita, olivatpa ne omistettu yhdelle kryptovaluutalle tai tukivat useita valuuttoja.

Toivon, että tämä johdanto on auttanut sinua ymmärtämään paremmin HD-lompakoiden perusteita ja niiden erilaisia ominaisuuksia. Tavoitteenamme on auttaa sinua hallitsemaan nämä olennaiset käsitteet ja navigoimaan tehokkaammin kryptovaluuttojen monimutkaisessa maailmassa. Joten pysy kanssamme, kun jatkamme tämän kiehtovan maailman monimutkaisuuksien ja vivahteiden tutkimista tulevissa oppitunneissa.

## Entropia ja Satunnaisluku

![Entropia ja Satunnaisluku](https://youtu.be/k18yH18w2TE)
Bitcoin-ekosysteemin yksityisavainten turvallisuuden merkitys on kiistaton. Ne ovat todellakin kulmakivi, joka varmistaa Bitcoin-siirtojen turvallisuuden. Jotta ennustettavuuteen liittyvät haavoittuvuudet voidaan välttää, nämä avaimet on luotava todella satunnaisella tavalla, mikä voi nopeasti muodostua työlääksi tehtäväksi käyttäjälle. Yksi ratkaisu tähän pulmaan on Hierarkkinen Deterministinen Lompakko, eli HD-lompakko. Tämä menetelmä mahdollistaa lapsiavainparien deterministisen ja hierarkkisen tuottamisen yhdestä tietoalkiosta lompakon pohjalla. Tässä kohtaa satunnaisuus muuttuu olennaiseksi turvatakseen johdettujen avainten turvallisuuden.

Satunnaislukujen tuottaminen on todellakin kriittinen elementti kryptografiassa, jotta voidaan varmistaa yksityisavainten eheys. Ennustettavuuteen liittyvien haavoittuvuuksien estämiseksi yksityisavain on tuotettava satunnaisesti. Uuden avainparin käyttö jokaisessa siirrossa lisää turvallisuutta, vaikka se monimutkaistaakin niiden varmuuskopiointia ja säilyttää vain osittain luottamuksellisuuden. Yhteenvetona voidaan sanoa, että yksityisavainten turvallisuus on ehdoton prioriteetti, joka vaatii huolellista ja satunnaista tuottamista. HD-lompakot tarjoavat ratkaisun avainten tuottamisen ja hallinnan helpottamiseen samalla kun ylläpidetään korkeaa turvallisuustasoa.

Kuitenkin satunnaislukujen tuottaminen tietokoneilla asettaa merkittävän haasteen, sillä saadut tulokset eivät ole todella satunnaisia. Siksi on olennaista käyttää Satunnaislukugeneraattoria (RNG). RNG-tyypit vaihtelevat Pseudo-Satunnaislukugeneraattoreista (PRNG) Todellisiin Satunnaislukugeneraattoreihin (TRNG) sekä PRNG:ihin, jotka sisältävät entropialähteen.

Bitcoinin tapauksessa yksityisavaimet tuotetaan yhdestä tietoalkiosta lompakon pohjalla. Tämä tieto mahdollistaa lapsiavainparien deterministisen ja hierarkkisen johdannan. Entropia on minkä tahansa HD-lompakon perusta, vaikka satunnaisluvun tuottamiselle ei olekaan standardia. Siksi satunnaislukujen tuottaminen on merkittävä huolenaihe Bitcoin-siirtojen turvaamisessa.

Avainten tuottamisen varmistusvaihe on ratkaisevan tärkeä turvallisuuden ja satunnaislukujen tuottamisen aitouden varmistamiseksi, mikä on perustavanlaatuinen askel ennustettavuuteen liittyvien haavoittuvuuksien estämisessä. On vahvasti suositeltavaa käyttää avoimen lähdekoodin lompakoita tämän varmistuksen mahdollistamiseksi.

On kuitenkin tärkeää huomata, että jotkin laitteistolompakot saattavat olla "suljettuja lähdekoodiltaan", mikä tekee satunnaisluvun tuottamisen varmistamisen mahdottomaksi. Mahdollinen kiertotapa voisi olla oman muistisarjan tuottaminen nopanheitolla, vaikka tämä lähestymistapa saattaa sisältää tiettyjä riskejä.

Satunnaisesti tuotetun salasanan käyttäminen voi auttaa lieventämään näitä riskejä.

Esimerkki tämän menetelmän soveltamisesta on CoinKitin tarjoama "nopanheitto"-vaihtoehto muistisarjojen tuottamiseen. Toinen mahdollisuus olisi käyttää hyvin suurta alkuperäistä tietoalkiota ja pienentää tämä tieto 256 bittiin SHA-256 -hash-funktiolla, joka pystyy tuottamaan hyvän satunnaisluvun. On tärkeää mainita, että SHA-256 -hash-funktio kestää törmäykset, väärentämisen sekä ensimmäisen ja toisen kuvan hyökkäykset.

Lopulta satunnaisuudella on keskeinen rooli kryptografiassa ja tietojenkäsittelytieteessä, ja kyky tuottaa satunnaisuutta turvallisesti on ratkaisevan tärkeää yksityisavainten ja Bitcoin-siirtojen turvallisuuden varmistamiseksi. Entropia, joka on Bitcoinin HD-lompakon ytimessä, on olennainen sen turvallisuudelle. Seuraavassa oppitunnissamme jatkamme tämän aiheen tutkimista, syventyen siihen, miten entropia edistää HD-lompakoiden turvallisuutta.

## Muistisarja

![Muistisarja](https://youtu.be/uJERqH9Xp7I)

Bitcoin-lompakon turvallisuus on suuri huolenaihe kaikille sen käyttäjille. Olennainen tapa varmistaa lompakon varmuuskopiointi on tuottaa muistisarja entropian ja tarkistussumman perusteella.
![kuva](assets/image/section3/5.JPG)
Entropia on HD-lompakon turvallisuuden kulmakivi. Useita menetelmiä on olemassa tämän entropian tuottamiseksi, mukaan lukien pseudo-satunnaislukugeneraattorit (PRNGs), todelliset satunnaislukugeneraattorit (TRNGs) tai manuaalisesti. On ratkaisevan tärkeää, että tämä entropia on satunnaista tai pseudo-satunnaista lompakon turvallisuuden takaamiseksi.

![kuva](assets/image/section3/6.JPG)

Toisaalta tarkistussumma varmistaa palautuslausekkeen tarkkuuden tarkistamisen. Ilman tätä tarkistussummaa virhe lausekkeessa voisi johtaa erilaisen lompakon luomiseen ja siten varojen menetykseen. Tarkistussumma saadaan syöttämällä entropia SHA256-funktion läpi ja noutamalla hashin ensimmäiset 8 bittiä.

Eri standardeja on olemassa mnemoniselle lausekkeelle riippuen entropian koosta. Yleisimmin käytetty standardi 24 sanan palautuslausekkeelle on 256 bitin entropia. Tarkistussumman koko määräytyy jakamalla entropian koko 32:lla.

Esimerkiksi 256 bitin entropia tuottaa 8 bitin tarkistussumman. Entropian ja tarkistussumman yhdistäminen johtaa sitten vastaaviin kokoihin 128 bittiä, 160 bittiä jne. Entropian koosta riippuen palautuslauseke koostuu 12 sanasta 128 bitille, 15 sanasta 160 bitille ja 24 sanasta 256 bitille.

![kuva](assets/image/section3/7.JPG)

Bittien muuntamiseksi lauseiksi, jokainen segmentti yhdistetään sanaan 2048 sanan listalta. On tärkeää huomata, että yksikään sana ei ole samassa järjestyksessä ensimmäisten neljän kirjaimen osalta.

On olennaista varmuuskopioida 24 sanan palautuslauseke Bitcoin-lompakon eheyden säilyttämiseksi. Kaksi yleisimmin käytettyä standardia perustuvat 128 tai 256 bitin entropiaan ja 12 tai 24 sanan yhdistämiseen. Salasanan lisääminen on lisävaihtoehto lompakon turvallisuuden parantamiseksi.

Yhteenvetona, mnemonisen lausekkeen luominen Bitcoin-lompakon turvaamiseksi on ratkaiseva prosessi. On tärkeää noudattaa mnemonisen lausekkeen standardeja riippuen entropian koosta. 24 sanan palautuslausekkeen varmuuskopiointi on olennaista varojen menetyksen estämiseksi. Kiitos huomiostanne ja odotamme innolla seuraavaa kryptovaluuttakurssiamme.

## Salasana

![Salasana](https://youtu.be/dZkOYO7MXwc)

Salasana on lisäsuojaus, joka voidaan integroida Bitcoin-lompakkoon sen turvallisuuden lisäämiseksi. Sen käyttö on valinnaista ja käyttäjän harkinnan mukaan. Lisäämällä mielivaltaista tietoa, joka yhdessä mnemonisen lausekkeen kanssa mahdollistaa lompakon siemenen laskennan, salasana parantaa sen turvallisuutta.

![kuva](assets/image/section3/8.JPG)

HD-lompakon avainten johdannassa tarvitaan sekä mnemoninen lauseke että salasana. Salasana on vapaa ja voi saavuttaa lähes äärettömän koon. Sitä ei sisällytetä mnemoniseen lausekkeeseen, joka on standardoitu ja sen on noudatettava tiettyjä koko-, tarkistussumma- ja koodausrajoituksia. Hyökkääjä ei voi päästä käsiksi käyttäjän bitcoineihin tietämättä salasanaa. Salasana on roolissa kaikkien lompakon avainten rakentamisessa ja laskennassa.

pbkdf2-funktiota käytetään siemenen tuottamiseen salasanasta. Tämä siemen mahdollistaa kaikkien lompakon lasten avainparien johdannan. Jos salasanaa muutetaan, Bitcoin-lompakko muuttuu täysin erilaiseksi.
Salasana on olennainen työkalu Bitcoin-lompakoiden turvallisuuden parantamiseksi. Se mahdollistaa erilaisten turvallisuusstrategioiden käytön. Esimerkiksi sitä voidaan käyttää luomaan duplikaatteja ja helpottamaan mnemonic-lauseen varmuuskopiointia. Se voi myös parantaa lompakon turvallisuutta vähentämällä satunnaisen mnemonic-lauseen tuottamiseen liittyviä riskejä.
Tehokkaan salasanan tulisi olla pitkä (20–40 merkkiä) ja monipuolinen (käyttäen isoja kirjaimia, pieniä kirjaimia, numeroita ja symboleita). Sen ei tulisi olla suoraan yhteydessä käyttäjään tai heidän ympäristöönsä. Satunnaisen merkkijonon käyttäminen on turvallisempaa kuin yksinkertaisen sanan käyttäminen salasanana.

![kuva](assets/image/section3/9.JPG)

Salasana on turvallisempi kuin yksinkertainen salasana. Ihanteellinen salasana on pitkä, vaihteleva ja satunnainen. Se voi parantaa lompakon tai hot softwaren turvallisuutta. Sitä voidaan myös käyttää luomaan redundanteja ja turvallisia varmuuskopioita.

On tärkeää huolehtia salasanan varmuuskopioinnista, jotta lompakkoon pääsyä ei menetetä. Salasana on vaihtoehto HD-lompakolle. Sen voi luoda satunnaisesti nopilla tai muulla pseudo-satunnaislukugeneraattorilla. Salasanan tai mnemonic-lauseen muistaminen ei ole suositeltavaa.

Seuraavassa oppitunnissamme tarkastelemme yksityiskohtaisesti siemenen toimintaa ja siitä johdettua ensimmäistä avainparia. Seuraa tätä kurssia jatkaaksesi oppimista. Odotamme innolla näkevämme sinut hyvin pian.

# Bitcoin-lompakoiden luominen

## Siemenen ja pääavaimen luominen

![Siemenen ja pääavaimen luominen](https://youtu.be/56yAt_JDWhY)

Tässä kurssin osassa tutkimme Hierarkkisen Deterministisen Lompakon (HD Wallet) johdannaisen vaiheita, joka mahdollistaa yksityisten ja julkisten avainten luomisen ja hallinnan hierarkkisella tavalla.

![kuva](assets/image/section4/0.JPG)

HD-lompakon perusta nojaa kahteen olennaiseen elementtiin: mnemonic-lauseeseen ja salasanaan (valinnainen lisäsalasana). Yhdessä ne muodostavat siemenen, 512-bittisen alfanumeerisen sekvenssin, joka toimii perustana lompakon avainten johdannaiselle. Tästä siemenestä on mahdollista johtaa kaikki Bitcoin-lompakon lapsiavainparit. Siemen on avain, joka antaa pääsyn kaikkiin lompakkoon liittyviin bitcoineihin, käytitpä salasanaa tai et.

Siemenen saamiseksi käytetään pbkdf2-funktiota (Password-Based Key Derivation Function 2) mnemonic-lauseen ja salasanan kanssa. pbkdf2:n tuloste on 512-bittinen siemen. Pääyksityisavain ja pääketjukoodi määritetään käyttämällä HMAC SHA-512 (Hash-based Message Authentication Code Secure Hash Algorithm 512) -algoritmia. Tämä algoritmi vaatii viestin ja avaimen tuloksen tuottamiseksi. Pääyksityisavain lasketaan siemenestä ja lauseesta "Bitcoin SEED". Tämä lause on identtinen kaikissa HD-lompakon johdannaisissa, varmistaen johdonmukaisuuden lompakoiden välillä.

![kuva](assets/image/section4/1.JPG)

Alun perin SHA-512-funktiota ei ollut toteutettu Bitcoin-protokollassa, minkä vuoksi käytetään HMAC SHA-512:ta. HMAC SHA-512:n käyttö lauseen "Bitcoin SEED" kanssa rajoittaa käyttäjän luomaan nimenomaan Bitcoinille spesifin lompakon. HMAC SHA-512:n tuloksena on 512-bittinen numero, joka jaetaan kahteen osaan: vasemmanpuoleiset 256 bittiä edustavat pääyksityisavainta, kun taas oikeanpuoleiset 256 bittiä edustavat pääketjukoodia.
Päämestariavain on kaikkien tulevien avainten vanhempi avain lompakossa, kun taas pääketjukoodi on mukana johdettaessa lapsiavaimia. On tärkeää huomata, että lapsiavainparia on mahdotonta johtaa tietämättä vastaavan vanhemman parin ketjukoodia. Ketjukoodi lisää entropian lähteen johdatusprosessiin.
Lompakon avainpari koostuu yksityisestä avaimesta, julkisesta avaimesta ja ketjukoodista. Ketjukoodi mahdollistaa satunnaisuuden tuomisen lapsiavainten johdannaisiin ja eristää jokaisen avainparin estäen minkä tahansa tiedon vuotamisen.

![kuva](assets/image/section4/2.JPG)

On tärkeää korostaa, että päämestariavain on ensimmäinen siemenestä johdettu yksityinen avain, eikä sillä ole yhteyttä lompakon laajennettuihin avaimiin. Siksi siemen on perustava elementti kaikkien lompakon avainten johdattamiseen. Se eroaa muistilauseesta ja salasanasta, joita käytetään siemenen luomiseen.

Seuraavassa oppitunnissa tutkimme yksityiskohtaisesti laajennettuja avaimia, kuten xPub, xPRV, zPub, ja ymmärrämme miksi niitä käytetään ja miten ne on rakennettu.

## Laajennetut Avaimet

![Laajennetut Avaimet](https://youtu.be/TRz760E_zUY)

Tässä oppitunnin osassa tutkimme laajennettuja avaimia (xPub, zPub, yPub) ja niiden etuliitteitä, jotka ovat tärkeässä roolissa lapsiavainten johdattamisessa HD (Hierarkkinen Deterministinen Lompakko) -lompakossa.

![kuva](assets/image/section4/3.JPG)

Laajennetut avaimet eroavat mestariavaimista. HD-lompakko luo muistilauseen ja siemenen saadakseen mestariavaimen ja pääketjukoodin. Laajennettuja avaimia käytetään lapsiavainten johdattamiseen ja ne vaativat sekä vanhemman avaimen että vastaavan ketjukoodin. Laajennettu avain yhdistää nämä kaksi tietoa yksinkertaistaakseen johdatusprosessia.

Laajennetut avaimet tunnistetaan erityisillä etuliitteillä (XPRV, XPUB, YPUB, ZPUB), jotka ilmaisevat, onko kyseessä laajennettu yksityinen vai julkinen avain, sekä sen erityisen tarkoituksen. Laajennetun avaimen metatietoihin kuuluu versio (etuliite), syvyys, julkisen avaimen sormenjälki, indeksi ja kuorma (ketjukoodi ja vanhempi avain).

![kuva](assets/image/section4/4.JPG)

Kuorma koostuu ketjukoodista (32 tavua) ja vanhemmasta avaimesta (33 tavua). Nämä elementit ovat olennaisia lapsiavainten johdattamisessa. Yksityinen avain luodaan satunnaisesta tai pseudosatunnaisesta numerosta, kun taas julkinen avain luodaan käyttäen ECDSA (Elliptic Curve Digital Signature Algorithm) -algoritmia.

Jokaiseen laajennettuun avainpariin liittyy ainutlaatuinen ketjukoodi, joka mahdollistaa tiettyjen johdannaisten luomisen. Yhdistämällä vanhempi avain ketjukoodin kanssa saadaan laajennettu yksityinen tai julkinen avain.

![kuva](assets/image/section4/5.JPG)

Laajennettuja julkisia avaimia voidaan johtaa vain normaaleista lapsi julkisista avaimista, kun taas laajennettuja yksityisiä avaimia voidaan johtaa sekä julkisista että yksityisistä lapsiavaimista, olipa kyseessä sitten normaali tai kovennettu johdannainen. Käyttämällä laajennettuja avaimia XPUB-etuliitteellä mahdollistetaan uusien osoitteiden johdattaminen palaamatta vastaaviin yksityisiin avaimiin, mikä tarjoaa paremman turvallisuuden. Laajennettujen avainten metatiedot tarjoavat tärkeää tietoa niiden roolista ja asemasta avainhierarkiassa.

Pakatut julkiset avaimet ovat 33 tavun kokoisia, kun taas pakkaamattomat julkiset avaimet ovat 512 bittiä. Pakatut julkiset avaimet säilyttävät saman tiedon kuin pakkaamattomat avaimet, mutta pienemmässä koossa. Laajennettujen avainten koko on 82 tavua ja niiden etuliite esitetään base 58:ssa heksadesimaalimuunnoksen kautta. Tarkistussumma lasketaan käyttäen HASH256-hajautusfunktiota.

![kuva](assets/image/section4/6.JPG)
Kovennetut johdannaiset alkavat indekseistä, jotka ovat kahden potensseja (2^31). Laajennetut julkiset avaimet sallivat vain normaalien lasten julkisten avainten johdannaisen, kun taas laajennetut yksityiset avaimet mahdollistavat minkä tahansa lapsiavaimen johdannaisen. On huomionarvoista, että yleisimmin käytetyt etuliitteet ovat xpub ja zpub, jotka vastaavat perintö- ja segwit v1 sekä segwit v0 standardeja vastaavasti.
Seuraavassa oppitunnissamme tutkimme lapsiavainparien johdannaista käyttäen hyväksi tietoa laajennetuista avaimista ja lompakon pääavaimesta.

Yhteenvetona voidaan todeta, että laajennetut avaimet ovat olennaisessa roolissa kryptografiassa ja HD-lompakoiden toiminnassa. Niiden käytön ja laskennan ymmärtäminen on ratkaisevan tärkeää varmistaaksemme transaktioiden turvallisuuden ja digitaalisten omaisuuksien suojan. Laajennettuihin avaimiin liittyvät etuliitteet ja metadata mahdollistavat niiden tehokkaan käytön ja tarvittavien lasten avainten tarkan johdannaisen.

## Lapsiavainparien Johdannainen

![Lapsiavainparien Johdannainen](https://youtu.be/FXhI-GmE9Aw)

Seuraavaksi keskustelemme siemenen ja pääavaimen laskennasta, jotka ovat ensimmäiset olennaiset elementit hierarkkisen organisaation ja HD-lompakon (Hierarkkinen Deterministinen Lompakko) johdannaiselle. Siemen, jonka pituus on 128-256 bittiä, luodaan satunnaisesti tai salaisesta lauseesta. Se toimii deterministisessä roolissa kaikkien muiden avainten johdannaisessa. Pääavain on ensimmäinen siemenestä johdettu avain, ja se mahdollistaa kaikkien muiden lasten avainparien johdannaisen.

Pääketjukoodilla on tärkeä rooli portfolion palauttamisessa siemenestä. On huomattava, että kaikki samasta siemenestä johdetut avaimet omaavat saman pääketjukoodin.

![kuva](assets/image/section4/7.JPG)

Hierarkkinen ja deterministinen lompakko (HD-lompakko) tarjoaa tehokkaamman avainten ja lompakon rakenteiden hallinnan. Laajennetut avaimet mahdollistavat lapsiavainparin johdannaisen vanhemmasta avainparista matemaattisten laskelmien ja tiettyjen algoritmien avulla.

On olemassa erilaisia lapsiavainpareja, mukaan lukien kovennetut avaimet ja normaalit avaimet. Laajennettu julkinen avain sallii vain normaalien lasten julkisten avainten johdannaisen, kun taas laajennettu yksityinen avain mahdollistaa kaikkien lasten avainten, sekä julkisten että yksityisten, johdannaisen normaalissa tai kovennetussa tilassa. Jokaisella avainparilla on indeksi, joka erottaa ne toisistaan.

![kuva](assets/image/section4/8.JPG)

Lasten avainten johdannainen käyttää HMAC-SHA512-funktiota käyttäen vanhemman avainta yhdistettynä indeksiin ja avainpariin liittyvään ketjukoodiin. Normaalien lasten avaimilla on indeksi, joka vaihtelee 0:sta 2 potenssiin 31 miinus 1, kun taas kovennetuilla lasten avaimilla on indeksi, joka vaihtelee 2 potenssiin 31:stä 2 potenssiin 32 miinus 1.

![kuva](assets/image/section4/9.JPG)
![kuva](assets/image/section4/10.JPG)

On olemassa kaksi tyyppiä lapsiavainpareja: kovennetut parit ja normaalit parit. Lasten avainten johdannaisprosessi käyttää julkisia avaimia luomaan kulutusehdot, kun taas yksityisiä avaimia käytetään allekirjoittamiseen. Laajennettu julkinen avain sallii vain normaalien lasten julkisten avainten johdannaisen, kun taas laajennettu yksityinen avain mahdollistaa kaikkien lasten avainten, sekä julkisten että yksityisten, johdannaisen normaalissa tai kovennetussa tilassa.

![kuva](assets/image/section4/11.JPG)
![kuva](assets/image/section4/12.JPG)

Kovennettu johdannainen käyttää vanhemman yksityistä avainta, kun taas normaali johdannainen käyttää vanhemman julkista avainta. HMAC-SHA512-funktiota käytetään kovennetussa johdannaisessa, kun taas normaalissa johdannaisessa käytetään 512-bittistä hajautusta. Lasten julkinen avain saadaan kertomalla lasten yksityinen avain elliptisen käyrän generaattorilla.

![kuva](assets/image/section4/13.JPG)
![kuva](assets/image/section4/14.JPG)
## Lompakon Rakenne ja Johdannaispolut

![Lompakon Rakenne ja Johdannaispolut](https://youtu.be/etO9UxwyE2I)

Tässä luvussa tutkimme Hierarkkisen Deterministisen Lompakon (HD Lompakko) johdannaispuun rakennetta. Olemme jo tutkineet siemenen laskentaa, pääavainta ja lasten avainpareja. Nyt keskitymme avainten järjestämiseen lompakossa.

HD Lompakko käyttää syvyystasoja avainten järjestämiseen. Jokainen johdannainen vanhemmasta parista lapseen vastaa syvyystasoa. Syvyys 0 vastaa pääavainta ja pääketjukoodia.

![kuva](assets/image/section4/15.JPG)

- Syvyys 1 käytetään lasten avainten johtamiseen tiettyyn tarkoitukseen, joka määräytyy indeksin perusteella. Tarkoitukset ovat BIP 84:n ja Segwit v0/v1 -standardien mukaisia.

- Syvyys 2 mahdollistaa eri kryptovaluuttojen tai verkkojen tilien erottelun. Tämä mahdollistaa lompakon järjestämisen eri varojen lähteiden perusteella.

- Syvyys 3 käytetään lompakon järjestämiseen eri tileihin, tarjoten selkeämmän ja järjestäytyneemmän rakenteen.

- Syvyys 4 vastaa ulkoisia ja sisäisiä ketjuja, joita käytetään julkisesti kommunikoitaviksi tarkoitettuihin osoitteisiin. Indeksi 0 liittyy ulkoiseen ketjuun, kun taas indeksi 1 sisäiseen ketjuun. Jokaisella tilillä on kaksi ketjua: ulkoinen ketju (0) ja sisäinen ketju (1). Syvyys 4 käytetään myös skriptityyppien hallintaan moniallekirjoituslompakoissa.

- Syvyys 5 käytetään vastaanotto-osoitteisiin standardilompakossa. Seuraavassa osiossa tutkimme lasten avainparien johdannaista tarkemmin.

![kuva](assets/image/section4/16.JPG)

Jokaisella syvyystasolla käytämme indeksejä lasten avainparien erottamiseen. Kovennettuja indeksejä käytetään apostrofin kanssa tietyissä johdannaisissa. Julkinen avain vuodessa käytetään HMAC-funktion syötteenä. Johdannaispolun indeksi ilmaisee HMAC-funktiossa käytetyn arvon.
Indeksi ilman apostrofia vastaa todellista käytettyä indeksiä, kun taas indeksi apostrofin kanssa vastaa todellista indeksiä + 2^31. Vahvistetut johdannaiset käyttävät indeksejä 2^31:stä 2^32-1:een. Esimerkiksi indeksi 44' vastaa todellista indeksiä 2^31 + 44.
Erityisen vastaanotto-osoitteen luomiseksi johdamme lasten avainparin pääavaimesta ja pääketjukoodista. Sitten käytämme indeksiä erottamaan eri lasten avainparit samalla syvyystasolla.

Laajennetut avaimet, kuten XPUB, mahdollistavat lompakkosi jakamisen useiden ihmisten kanssa. Johdannaispolkua käytetään erottamaan ulkoinen ketju (osoitteet, jotka on tarkoitettu kommunikoitaviksi) ja sisäinen ketju (vaihto-osoitteet).

On tärkeää huomata, että HD-lompakossa käytetään eri syvyyksiä riippuen eri standardeista. Vanhempien avainten johtaminen lasten avaimiin mahdollistaa siirtymisen yhdestä syvyydestä toiseen. HD-lompakon eri haarojen käyttö osoittaa noudatettuja eri standardeja.

Seuraavassa luvussa tutkimme vastaanotto-osoitteita, niiden käytön etuja ja niiden rakentamiseen liittyviä vaiheita.

# Mikä on Bitcoin-osoite?

## Bitcoin-osoitteet

![Bitcoin-osoitteet](https://youtu.be/nqGBMjPtFNI)
Tässä luvussa tutkimme vastaanotto-osoitteita, jotka ovat keskeisessä roolissa Bitcoin-järjestelmässä. Ne mahdollistavat varojen vastaanottamisen kolikolle ja ne luodaan yksityisten ja julkisten avainten pareista. Vaikka on olemassa skriptityyppi nimeltä Pay2PublicKey, joka mahdollistaa bitcoinien lukitsemisen julkiseen avaimen, käyttäjät suosivat yleensä vastaanotto-osoitteiden käyttöä tämän skriptin sijaan.
![image](assets/image/section5/0.JPG)

Kun vastaanottaja haluaa vastaanottaa bitcoineja, hän antaa lähettäjälle vastaanotto-osoitteen julkisen avaimensa sijaan. Osoite on itse asiassa julkisen avaimen hajautus, tietyssä muodossa. Julkinen avain johdetaan lapsen yksityisestä avaimesta käyttäen matemaattisia operaatioita, kuten pisteen lisäystä ja kaksinkertaistamista elliptisillä käyrillä.

![image](assets/image/section5/1.JPG)

On tärkeää huomata, että osoitteesta ei ole mahdollista palauttaa julkista avainta, eikä julkisesta avaimesta yksityiseen avaimen. Osoitteen käyttö auttaa vähentämään julkisen avaimen tiedon kokoa, joka alun perin on 512 bittiä. Julkisen avaimen on mahdollista tiivistää säilyttämällä vain x-arvo ja lisäämällä etuliite, mutta tätä tekniikkaa ei tunnettu Bitcoinin luomisen aikaan. Siksi osoitteen käyttö ei säästä tilaa lohkoissa.

## Kuinka luoda Bitcoin-osoite?

![Kuinka luoda Bitcoin-osoite?](https://youtu.be/ewMGTN8dKjI)

Tässä luvussa keskustelemme Bitcoin-siirtojen vastaanotto-osoitteen rakentamisesta. Vastaanotto-osoite on kompressoidun julkisen avaimen alfanumeerinen esitys. Julkisen avaimen muuntaminen vastaanotto-osoitteeksi käy läpi useita vaiheita.

![image](assets/image/section5/3.JPG)

Yksi vastaanotto-osoitteiden hyödyllisistä ominaisuuksista on tarkistussumman läsnäolo, joka mahdollistaa virheiden havaitsemisen. Tätä varten käytämme BCH (Bose-Chaudhuri-Hocquenghem) tarkistussummateknologiaa, joka varmistaa tarkan virheentunnistuksen. Tämä teknologia myös auttaa vähentämään tarvittavien merkkien määrää osoitteen esittämiseen, mikä tekee sen käytöstä helpompaa.

Aloittaaksemme osoitteen rakentamisen, meidän on tiivistettävä vastaava julkinen avain. Raaka julkinen avain vie 520 bittiä, mutta käytetyn elliptisen käyrän symmetrian ansiosta, elliptisellä käyrällä voi olla x-koordinaatti, johon liittyy kaksi mahdollista y-arvoa: positiivinen tai negatiivinen. Bitcoin-verkossa työskentelemme äärellisen positiivisten kokonaislukujen joukon kanssa reaalilukujen joukon sijaan. Esittääksemme julkisen avaimen x:stä, lisäämme etuliitteen, joka osoittaa y:n arvon (parillinen tai pariton). Julkisen avaimen tiivistäminen vähentää sen kokoa 520 bitistä 264 bittiin. Y:n pariteetti äärellisessä positiivisten kokonaislukujen joukossa vastaa y:n pariteettia reaalilukujen joukossa.

![image](assets/image/section5/4.JPG)
![image](assets/image/section5/5.JPG)

Otetaan esimerkiksi Satoshi Nakamoton julkinen avain, jossa etuliite 0,3 osoittaa y:n parittoman arvon. Voimme sitten siirtyä toiseen vaiheeseen kompressoiduista julkisista avaimista osoitteen rakentamisessa. Kullekin julkiselle avaimelle on mahdollista laskea kaksi osoitetta. Tätä varten käytämme SHA256-funktiota saadaksemme julkisen avaimen hajautuksen. Sitten sovellamme ripemd160-funktiota SHA256:n tulokseen saadaksemme merkkijonon. Tämä merkkijono sitten koodataan binäärimuodossa 5 bitin ryhmissä, joihin lisätään metadata tarkistussumman laskemiseksi BCH-ohjelmalla.

![image](assets/image/section5/6.JPG)
Perintöosoitteiden tapauksessa käytämme kaksinkertaista SHA256-tiivistystä osoitteen tarkistussumman luomiseen. Segwit V0 ja V1 -osoitteiden osalta luotamme kuitenkin BCH-tarkistussummateknologiaan virheentunnistuksen varmistamiseksi. BCH-ohjelma pystyy ehdottamaan ja korjaamaan virheitä erittäin pienen virhetodennäköisyyden kanssa. Tällä hetkellä BCH-ohjelmaa käytetään havaitsemaan ja ehdottamaan muutoksia, mutta se ei automaattisesti tee niitä käyttäjän puolesta. Tarkistussumman laskenta BCH-koodilla perustuu polynomiseen Chien-Chauffage-aritmetiikkaan.
![kuva](assets/image/section5/7.JPG)

BCH-ohjelma vaatii useita syöttötietoja, mukaan lukien HRP (Human Readable Part), joka on laajennettava. HRP:n laajentaminen sisältää jokaisen kirjaimen koodaamisen 2-kantaiseksi, ottamalla kunkin merkin ensimmäiset kolme bittiä erottimen 0 avulla ja sitten yhdistämällä kunkin merkin viimeiset viisi bittiä. Sinisiksi merkeiksi muunnetut 10-kantaiset merkit vastaavat 3 ja 3 desimaalissa, kun taas viisi muuta oranssia merkkiä vastaavat 2 ja 3 10-kantaisessa. HRP:n laajennus 10-kantaisessa mahdollistaa kunkin merkin viimeisten viiden bitin eristämisen, vahvistaen näin tarkistussumman.

![kuva](assets/image/section5/8.JPG)

Segwit V0 -versio on edustettuna koodilla 00 ja "payload" on mustana, 10-kantaisena. Tämän jälkeen seuraa kuusi tarkistussummaan varattua merkkiä. Metadataa sisältävä syöte toimitetaan sitten BCH-ohjelmalle tarkistussumman saamiseksi 10-kantaisena. Version, payloadin ja tarkistussumman yhdistäminen mahdollistaa osoitteen rakentamisen. 10-kantaiset merkit muunnetaan sitten bech32-merkeiksi käyttäen vastaavuustaulukkoa. Bech32-aakkostoon kuuluu kaikki alfanumeeriset merkit, paitsi 1, b, i ja o, välttääkseen sekaannusta.

![kuva](assets/image/section5/9.JPG)
![kuva](assets/image/section5/10.JPG)

Osoitteen rakentamiseksi, joka alkaa bc1q:lla, meidän on sovellettava hajautusfunktiota (H160) tiivistettyyn julkiseen avaimen, lisättävä sitten tarkistussumma, versio (q), HRP (bc) ja erotin (1). Toisaalta Taproot-osoitteet alkavat bc1p:llä, koska niiden versio (Segwit V1) vastaa 0+1=1, siksi käytetään merkkiä p. Kaikki nämä elementit muunnetaan sitten BCH32:ksi, Bitcoinille spesifiseksi 32-kantaiseksi variantiksi.

Näin olemme käyneet läpi vaiheet vastaanotto-osoitteen rakentamiseksi, BCH-tarkistussummateknologian käytön sekä osoitteen rakentamisen alkaen bc1q tai bc1p käyttäen Bitcoinille spesifistä BCH32 32-kantaista varianttia.

## Yhteenveto kryptografiasta Bitcoin-lompakoille

![koulutuksen yhteenveto](https://youtu.be/NkAYoVUMvOs)

Tämän koulutuksen aikana olemme tutkineet syvällisesti Hierarkkista Determinististä (HD) lompakkoa BIP32:n kanssa. Entropialla on keskeinen rooli tässä lompakkotyypissä, sillä sitä käytetään generoimaan mnemoninen lause satunnaisluvusta. BIP39:ssä tarjotun 2048 sanan listan avulla tämä mnemoninen lause voidaan koodata sarjaksi helposti muistettavia sanoja. Mnemoninen lause yhdessä valinnaisen salasanan kanssa on tarpeen lompakon siemenen generoimiseksi. Salasana toimii kryptografisena suolana, joka lisää ylimääräisen suojakerroksen lompakkoon.

![kuva](assets/image/section5/11.JPG)
Pbkdf2-funktio käytetään siemenen luomiseen mnemonisesta fraasista ja salasanasta, käyttäen hmacha512:ta ja 2048 iteraatiota. Pääavain ja pääketjukoodi johdetaan tästä siemenestä käyttäen uudelleen hmacha512-funktiota fraasin "bitcoin seed" kanssa. Pääyksityisavain ja pääketjukoodi ovat korkeimmat elementit HD-lompakon hierarkiassa.
![kuva](assets/image/section5/12.JPG)

Ala-avaimen johdannainen riippuu useista tekijöistä, mukaan lukien vanhempi avain ja vastaava ketjukoodi. Laajennettu avain saadaan yhdistämällä vanhempi avain sen ketjukoodin kanssa, kun taas pääavain on erillinen avain. Osoitteen johdannaisessa ensin tiivistetään julkinen avain käyttäen SHA256:ta ja RIPMD160:ta, ja sitten lasketaan tarkistussumma. Kahden SHA256-tiivisteen laskemista käytetään tarkistussumman laskemiseen perinteisen standardin tapauksessa, kun taas BCH (Bose-Chaudhuri-Hocquenghem) -ohjelmaa käytetään tarkistussumman laskemiseen segwit-standardin tapauksessa. Sitten käytetään base 58 -muotoista esitystä perinteisen standardin tapauksessa, kun taas bech32-muotoa käytetään segwit-standardin tapauksessa HD-lompakon osoitteen saamiseksi.

![kuva](assets/image/section5/13.JPG)

Yhteenvetona olemme tutkineet yksityiskohtaisesti hajautusfunktioita ja niiden ominaisuuksia, sekä digitaalisia allekirjoituksia ja elliptisiä käyriä. Sen jälkeen sukelsimme Hierarkkisten Determinististen (HD) lompakoiden maailmaan BIP32:n avulla, käyttäen entropiaa ja salasanaa lompakon siemenen luomiseen. Opimme myös, miten johdetaan ala-avaimia ja saadaan HD-lompakon osoite. Toivon, että tämä tieto on ollut hyödyllistä sinulle, ja kannustan sinua nyt etenemään arviointiin testataksesi kurssin Crypto 301 aikana saavuttamaasi tietämystä. Kiitos huomiostasi.

# Mene pidemmälle

## Siemenen luominen 128 nopanheitosta!

![Siemenen luominen 128 nopanheitosta!](https://youtu.be/lUw-1kk75Ok)

Mnemonisen fraasin luominen on ratkaisevan tärkeää kryptovaluuttaportfoliosi turvaamisessa. On olemassa useita menetelmiä mnemonisen fraasin luomiseen, mutta keskitymme manuaaliseen luontimenetelmään käyttäen noppaa. On tärkeää huomata, että tämä menetelmä ei sovellu suuren arvon lompakolle. On suositeltavaa käyttää avoimen lähdekoodin ohjelmistoa tai laitteistolompakkoa mnemonisen fraasin luomiseen. Mnemonisen fraasin luomiseksi käytämme noppaa binääritiedon tuottamiseen. Tavoitteena on ymmärtää mnemonisen fraasin luomisprosessi.

**Vaihe 1 - Valmistelu:**
Varmista, että sinulla on amneesinen Linux-jakelu, kuten Tails OS, asennettuna USB-asemaan lisäturvallisuuden vuoksi. Huomaa, että tätä opasta ei tulisi käyttää pääasiallisen lompakon luomiseen.

**Vaihe 2 - Satunnaisen binääriluvun generointi:**
Käytämme noppaa binääritiedon tuottamiseen. Heitä noppaa 128 kertaa ja merkitse jokainen tulos (1 parittomille, 0 parillisille).

**Vaihe 3 - Binäärilukujen järjestäminen:**
Järjestä saadut binääriluvut 11 numeron riveihin helpottaaksesi jatkuvia laskelmia. Kahdennentoista rivin tulisi sisältää vain 7 numeroa.

**Vaihe 4 - Tarkistussumman laskeminen:**
Viimeiset 4 numeroa kahdennentoista rivin kohdalla vastaavat tarkistussummaa. Tarkistussumman laskemiseksi meidän on käytettävä terminaalia Linux-jakelusta. On suositeltavaa käyttää [TailOs](https://tails.boum.org/index.fr.html), joka on muistiton jakelu, jonka voi käynnistää USB-asemalta. Kun olet terminaalissasi, syötä komento `echo <binääriluku> | shasum -a 254 -0`. Korvaa `<binääriluku>` 128 nollasi ja ykköselläsi. Tuloksena on heksadesimaalinen hajautus. Ota huomioon tämän hajautuksen ensimmäinen merkki ja muunna se binääriksi. Voit käyttää tätä [taulukkoa](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table) apunasi. Lisää binäärinen tarkistussumma (4 numeroa) lomakkeesi kahdennentoista rivin kohtaan.
**Vaihe 5 - Muuntaminen desimaaliksi:**
Löytääksesi jokaiselle rivillesi liittyvät sanat, sinun on ensin muunnettava jokainen 11 bitin sarja desimaaliksi. Tässä et voi käyttää verkossa olevaa muunninta, koska nämä bitit edustavat muistisanaasi. Joten sinun on muunnettava käyttäen laskinta ja seuraavaa niksiä: jokainen bitti liittyy 2:n potenssiin, joten vasemmalta oikealle meillä on 11 arvoa, jotka vastaavat 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1. Muuntaaksesi 11 bitin sarjasi desimaaliksi, sinun tarvitsee vain laskea yhteen ne arvot, jotka sisältävät ykkösen. Esimerkiksi sarjalle 00110111011, tämä vastaa seuraavaa yhteenlaskua: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. Nyt voit muuntaa jokaisen rivin desimaaliksi. Ja ennen kuin siirryt koodaamaan sanoiksi, sinun on lisättävä +1 kaikkiin riveihin, koska BIP39-sanaluettelon indeksi alkaa 1:stä eikä 0:sta.

**Vaihe 8 - Muistisanan luominen:**
Aloita tulostamalla [2048 sanan luettelo](https://seedxor.com/files/wordlist.pdf) muuntaaksesi desimaalinumerosi BIP39-sanoiksi. Tämän luettelon erikoisuus on, että yksikään sana ei jaa samoja ensimmäisiä 4 kirjainta kaikkien muiden tässä sanakirjassa olevien sanojen kanssa. Etsi sitten jokaiselle rivillesi desimaalinumeron mukainen sana.

**Vaihe 9 - Muistisanan testaaminen:**
Testaa muistisanasi välittömästi Sparrow Walletissa luomalla lompakko siitä. Jos saat virheilmoituksen virheellisestä tarkistussummasta, on todennäköistä, että teit laskuvirheen. Korjaa tämä virhe palaamalla vaiheeseen 4 ja testaa uudelleen Sparrow Walletissa. Siinä se! Olet juuri luonut uuden Bitcoin-lompakon 128 nopanheiton perusteella.

Muistisanan luominen on tärkeä prosessi kryptovaluuttalompakkosi turvaamiseksi. On suositeltavaa käyttää turvallisempia menetelmiä, kuten avoimen lähdekoodin ohjelmistojen tai laitteistolompakoiden käyttöä muistisanan luomiseen. Tämän työpajan suorittaminen auttaa kuitenkin ymmärtämään paremmin, miten voimme luoda Bitcoin-lompakon satunnaisesta numerosta.

## Yhteenveto ja loppu

### Kiitokset ja jatka tutkimista

Haluamme vilpittömästi kiittää sinua Crypto 301 -koulutukseen osallistumisesta. Toivomme, että tämä kokemus on ollut rikastuttava ja opettavainen sinulle. Olemme käsitelleet monia jännittäviä aiheita, jotka vaihtelevat matematiikasta kryptografiaan ja Bitcoin-protokollan toimintaan.
Jos haluat syventyä aiheeseen vielä enemmän, meillä on tarjota sinulle lisäresurssi. Olemme tehneet yksinoikeudella haastattelun Théo Pantamisin ja Loïc Morelin kanssa, jotka ovat kaksi tunnettua asiantuntijaa kryptografian alalla. Tässä haastattelussa syvennytään aiheen eri näkökulmiin ja tarjotaan mielenkiintoisia perspektiivejä.
Voit vapaasti katsoa tämän haastattelun jatkaaksesi kryptografian kiehtovan alan tutkimista. Toivomme, että se on hyödyllinen ja inspiroiva matkallasi. Kiitämme sinua vielä kerran osallistumisestasi ja sitoutumisestasi koko tämän koulutuksen ajan.

### Tue Meitä

Tämä kurssi, yhdessä kaiken tämän yliopiston tarjoaman sisällön kanssa, on tarjottu sinulle ilmaiseksi yhteisömme toimesta. Voit tukea meitä jakamalla sen muiden kanssa, liittymällä yliopiston jäseneksi ja jopa osallistumalla sen kehittämiseen GitHubin kautta. Koko tiimin puolesta, kiitos!

### Arvioi Koulutus

Koulutuksen arviointijärjestelmä integroidaan pian tähän uuteen E-oppimisalustaan! Siihen asti, suurkiitokset kurssin suorittamisesta, ja jos pidit siitä, harkitse sen jakamista muiden kanssa.