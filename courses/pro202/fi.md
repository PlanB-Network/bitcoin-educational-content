---
name: Ohjelmointi Bitcoin
goal: Rakenna täydellinen Bitcoin-kirjasto tyhjästä ja ymmärrä Bitcoin:n kryptografisia perusteita
objectives: 

 - Toteuta äärellisten kenttien aritmetiikkaa ja elliptisten käyrien operaatioita Pythonissa
 - Bitcoin-transaktioiden rakentaminen ja jäsentäminen ohjelmallisesti
 - Luo testiverkko-osoitteita ja lähetä transaktioita verkon kautta
 - Bitcoin:n turvallisuusmallin perustana olevien matemaattisten perusteiden hallitseminen

---
# Matka Bitcoin:n käsikirjoituksiin ja ohjelmiin


Tämä intensiivinen kaksipäiväinen kurssi, jonka opettajana toimii Jimmy Song, vie sinut syvälle Bitcoin:n teknisiin perusteisiin rakentamalla täydellisen Bitcoin-kirjaston alusta alkaen. Aloitat äärellisten kenttien ja elliptisten käyrien keskeisestä matematiikasta ja etenet transaktioiden jäsentämisen, skriptien suorittamisen ja verkkokommunikoinnin kautta. Jupyter-vihkoissa tehtävien käytännön koodausharjoitusten avulla luot oman testiverkko-osoitteesi, rakennat transaktioita manuaalisesti ja lähetät ne suoraan verkkoon - ja samalla saat syvällisen ymmärryksen kryptografisista periaatteista, jotka tekevät Bitcoin:stä turvallisen ja luotettavan.


Nauti matkasta!

Huomio: Tämän kurssin videot ovat saatavilla vain englanniksi.

+++

# Johdanto


<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>


## Kurssin yleiskatsaus


<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>


Tervetuloa kurssille PRO 202 _**Bitcoin:n ohjelmointi**_, intensiiviselle matkalle, joka vie sinut äärellisestä kenttäaritmiikasta aina todellisten transaktioiden rakentamiseen ja lähettämiseen Bitcoin:n Testnet:llä.


Tällä kurssilla rakennat asteittain Bitcoin-kirjaston Pythonilla ja hankit samalla kryptografiset, protokolla- ja ohjelmistoperusteet, joita tarvitaan Bitcoin:n turvallisuuden ja sisäisen toiminnan tarkkaan ymmärtämiseen. PRO 202 -lähestymistapa on läpikotaisin käytännönläheinen: jokainen käsite toteutetaan välittömästi Jupyter-vihkoissa, jolloin varmistetaan, että teoria ja koodi vahvistavat toisiaan.


### Bitcoin:n keskeiset matemaattiset käsitteet


Tässä ensimmäisessä jaksossa luodaan välttämätön matemaattinen perusta. Toteutat äärellisten kenttien aritmetiikan ja elliptisten käyrien operaatiot (ryhmälaki, yhteenlasku, kaksinkertaistaminen, skalaarikertolasku...) - ECDSA:n edellytykset. Tavoitteena on kaksi asiaa: ymmärtää algebrallinen rakenne, joka mahdollistaa kryptografiset allekirjoitukset, ja rakentaa luotettavia Python-työkaluja niiden käsittelyyn.


Tämän jälkeen formalisoit ECDSA:n osat: avaimen luominen, pisteiden muotoilu, hajauttaminen, allekirjoituksen luominen ja todentaminen. Tässä osiossa yhdistetään teoria suoraan käytäntöön ja korostetaan toteutuksen yksityiskohtia ja taustalla olevan turvallisuusmallin kestävyyttä.


### Bitcoin-transaktion sisäiset toiminnot


Toisessa osassa analysoidaan Bitcoin-tapahtuman rakenne: UTXO:t, tulot/lähtö, sekvenssit, skriptit, koodaukset ja paljon muuta. Kirjoitat koodia transaktioiden rakentamiseen, allekirjoittamiseen ja todentamiseen ja saat tarkan käsityksen siitä, mitä hash-tietueella sitoutuu ja miksi.


Seuraavaksi toteutat minimaalisen _Script_-toteuttajan, tarkastelet keskeisiä opkoodeja ja validoit menopolut. Tavoitteena on, että pystyt tarkastamaan tapahtumien käyttäytymisen, diagnosoimaan validointivirheitä ja päättelemään kulutuskäytäntöjen turvallisuutta.


### Bitcoin-verkon sisäinen toiminta


Kolmannessa osiossa sijoitat transaktiot laajempaan järjestelmään: lohkorakenne, otsikot, vaikeusasteet ja Proof-of-Work-mekanismi. Käsittelet protokollaviestejä, lohkootsikoita ja Merkle-puita.


Lopuksi opiskelet solmujen välistä vertaisverkkoviestintää, viestien optimointia ja SegWit:n käyttöönottoa.


Kuten jokaisella Plan ₿ Academy:n kurssilla, loppuosassa on arviointi, jonka tarkoituksena on lujittaa ymmärrystäsi. Oletko valmis paljastamaan Bitcoin:n sisäisen toiminnan ja kirjoittamaan sen käyttökoodin? Aloitetaan!










# Bitcoin:n keskeiset matemaattiset käsitteet

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Matematiikka Bitcoin:n täytäntöönpanoa varten

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>


![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


### Bitcoin Ohjelmoinnin perusteet: Matemaattiset perusrakenteet


Tällä kurssilla tiivistetään Bitcoin:n salausjärjestelmien taustalla oleva olennainen matematiikka erittäin käytännönläheiseksi työtavaksi. Käsitteet selitetään, havainnollistetaan esimerkkien avulla ja toteutetaan sitten Jupyter Notebookissa. Johtoajatus on yksinkertainen: kryptografisen primitiivin ymmärtää kunnolla vasta, kun se on koodattu. Kahden päivän aikana opiskelijat generate-testiverkon osoitteita, rakentavat ja lähettävät [transaktioita](https://planb.academy/resources/glossary/transaction-tx) ja ovat lopulta vuorovaikutuksessa verkon kanssa ilman lohko-etsintäohjelmia. Kaikki tämä edellyttää vankkaa pohjaa äärellisistä kentistä ja elliptisistä käyristä.


### Äärelliset kentät: Kryptografian aritmeettinen moottori


Äärellinen kenttä F(p) on alkuluvun p määrittelemä aritmeettinen järjestelmä, joka sisältää alkioita 0-p-1. Prime-kentät takaavat, että jokaisella nollasta poikkeavalla alkioilla on käänteisluku ja että kaikki operaatiot pysyvät kentän sisällä. Aritmeettinen laskutoimitus kietoutuu yhteen-, vähennys- ja kertolaskun modulo p -menetelmiin. Pythonin `pow(base, exp, mod)` mahdollistaa tehokkaan modulaarisen potensoinnin, joka on ratkaisevan tärkeää suurille eksponenteille, joita käytetään todellisissa salausoperaatioissa.


#### Multiplikatiivinen käyttäytyminen

Kun mikä tahansa nollasta poikkeava alkio k kerrotaan kaikilla alkulukukentän alkioilla, saadaan aikaan kentän permutaatio. Tämä ominaisuus takaa yhdenmukaisuuden ja estää rakenteelliset heikkoudet, minkä vuoksi prime-kentät soveltuvat erinomaisesti turvalliseen avainten tuottamiseen ja [digitaalisiin allekirjoituksiin](https://planb.academy/resources/glossary/digital-signature).


#### Jakaminen ja Fermat'n pieni lause

Jakaminen toteutetaan multiplikatiivisten käänteislukujen avulla. Fermat'n pieni lause sanoo, että

n^(p-1) ≡ 1 (mod p),

joten käänteisluku on n^(p-2). Python tukee tätä suoraan komennolla `pow(n, -1, p)`. Nämä operaatiot esiintyvät jatkuvasti [ECDSA](https://planb.academy/resources/glossary/ecdsa):n ja Bitcoin:n taustalla olevissa kryptografisissa rutiineissa.


### Elliptiset käyrät: Epälineaariset rakenteet julkisen avaimen turvallisuuteen


Elliptiset käyrät noudattavat yhtälöä y² = x³ + ax + b. Bitcoin käyttää secp256k1-käyrää, joka on määritelty muodossa y² = x³ + 7 äärellisessä kentässä. Elliptisen käyrän pisteet muodostavat matemaattisen ryhmän pisteiden yhteenlaskussa. Kahden pisteen P ja Q kautta piirretty viiva leikkaa käyrän kolmannessa pisteessä R; R:n heijastaminen x-akselin poikki antaa tulokseksi P + Q. Tämä järjestelmä on assosiatiivinen ja sisältää identiteettielementin: piste äärettömyydessä.


Pisteen kaksinkertaistamisessa käytetään sekanttiviivan sijasta tangenttiviivaa, jonka kaltevuus saadaan käyrän derivaatasta. Vaikka näihin kaavoihin liittyy reaalukulaskentaa, niistä tulee täysin diskreettejä ja eksakteja, kun käyrä määritellään äärellisessä kentässä - kuten Bitcoin:ssä.


### Matematiikasta Bitcoin-salaukseen


Lopulliset kentät tarjoavat determinististä, käänteistä aritmetiikkaa; elliptiset käyrät tarjoavat epälineaarisen rakenteen, jossa k-P:n laskeminen on helppoa mutta sen kääntäminen on laskennallisesti mahdotonta. Molemmat yhdistämällä saadaan perusta Bitcoin:n julkisille/yksityisille avaimille, ECDSA-allekirjoituksille ja transaktioiden turvallisuudelle. Näiden perusteiden ymmärtäminen valmistaa opiskelijat toteuttamaan avaimet, transaktiot ja allekirjoitukset suoraan - ilman abstraktioita tai ulkoisia työkaluja.


## Elliptisen käyrän salaus

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>


![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


Tässä luvussa esitellään äärellisten kenttien yli määritellyt elliptiset käyrät ja selitetään, miksi ne muodostavat Bitcoin:n salauksen matemaattisen selkärangan. Vaikka elliptiset käyrät reaalukujen yli näyttävät sileiltä ja jatkuvilta, samojen yhtälöiden soveltaminen äärelliseen kenttään luo diskreetin, hajanaisen pistejoukon. Visuaalisesta erosta huolimatta kaikki pisteiden yhteenlaskukaavat, kaltevuudet ja algebralliset säännöt käyttäytyvät täsmälleen samalla tavalla - ainoastaan aritmetiikka muuttuu modulaariseksi aritmiaksi. Bitcoin käyttää käyrää y² = x³ + 7 (secp256k1), joka säilyttää symmetrian ja epälineaarisen käyttäytymisen, jotka ovat välttämättömiä salauksen turvallisuuden kannalta.


### Pisteiden tarkistaminen ja äärellisen kentän toteutus


Piste sijaitsee äärellisen kentän elliptisellä käyrällä, jos sen koordinaatit täyttävät käyrän yhtälön modulo p. Pisteen, kuten (73,128) F₁₃₇:llä, tarkistaminen vaatii sen tarkistamista, että y² mod p on yhtä suuri kuin x³ + 7 mod p. Tämän toteuttaminen koodissa edellyttää luokkien luomista äärellisen kentän elementeille ja käyrän pisteille. Operaattoreiden ylikuormitus varmistaa, että kaikki aritmeettinen laskutoimitus - yhteenlasku, kertolasku, potensointi ja jakaminen - suoritetaan automaattisesti modulo p:n suhteen. Kun nämä abstraktiot ovat olemassa, edistyneempiä kryptografisia operaatioita on helppo kirjoittaa ja järkeillä.


#### Ryhmän ominaisuudet ja pisteiden lisääminen

Elliptisen käyrän pisteet muodostavat matemaattisen ryhmän yhteenlaskussa. Ryhmä täyttää sulkeutuneisuuden, assosiatiivisuuden, identiteetin (piste äärettömyydessä) ja inversiot (heijastus x-akselin yli). Geometriset konstruktiot vahvistavat nämä ominaisuudet ja tekevät skalaarisesta kertolaskusta (P lisätään itseensä toistuvasti) hyvin määritellyn. Nämä ryhmäsäännöt mahdollistavat elliptisten käyrien [kryptografian](https://planb.academy/resources/glossary/cryptography) ja varmistavat johdonmukaisen, ennustettavan käyttäytymisen toistuvissa pisteoperaatioissa.


### Sykliset ryhmät ja diskreetin logaritmin ongelma


Kun valitsemme generaattoripisteen G käyrällä, voimme generate:n avulla muodostaa syklisen ryhmän: G, 2G, 3G, ..., nG = 0. Pisteet näyttävät epälineaarisilta ja arvaamattomilta, vaikka ne olisi generoitu peräkkäin. Tämä arvaamattomuus luo perustan diskreetin logaritmin ongelmalle: P = sG:n laskeminen on helppoa, mutta s:n määrittäminen P:stä on laskennallisesti mahdotonta suurille ryhmille. Tämä yksisuuntainen funktio tekee julkisen avaimen salauksesta turvallisen. Asteikot ([yksityiset avaimet](https://planb.academy/resources/glossary/private-key)) kirjoitetaan pienillä kirjaimilla ja pisteet ([julkiset avaimet](https://planb.academy/resources/glossary/public-key)) isoilla kirjaimilla.


#### Tehokas skalaarikertolasku

Toteutukset käyttävät sG:n tehokkaaseen laskemiseen double-and-add-algoritmia: skannaamalla skalaarin binääriesitys, kaksinkertaistamalla pisteen jokaisella askeleella ja lisäämällä G:n vain silloin, kun bitti on 1. Tämä vähentää laskennan O(n)-lisäyksistä O(log n)-laskentaan, mikä mahdollistaa käytännön kryptografiset operaatiot jopa 256-bittisillä skalaareilla.


#### Secp256k1-käyrä Bitcoin:ssä


Bitcoin käyttää käyrää secp256k1, joka on määritelty seuraavasti: y² = x³ + 7 prime-kentässä, jossa p = 2²⁵⁶ - 2³² - 977. Generaattoripisteellä G on kiinteät koordinaatit, jotka valitaan deterministisellä NUMS-menettelyllä ("nothing up my sleeve"). Ryhmän järjestys n on suuri alkuluku lähellä 2²⁵⁶, mikä takaa, että jokainen nollasta poikkeava piste tuottaa saman ryhmän. Koko 2²⁵⁶ (~10⁷⁷) on tähtitieteellisen suuri, mikä tekee yksityisten avainten murtamisesta fyysisesti mahdotonta. Edes triljoona supertietokonetta, joita käytetään triljoona vuotta, ei pienentäisi avainavaruutta merkittävästi.


### Julkiset avaimet, yksityiset avaimet ja SEC-sarjalointi


Yksityinen avain on satunnainen skalaari s; julkinen avain on P = sG. Koska diskreetin lokiongelman ratkaiseminen ei ole mahdollista, P voidaan jakaa paljastamatta s:ää. Julkiset avaimet on sarjoitettava SEC-muodossa lähetystä varten. Pakkaamaton SEC-muoto käyttää 65 tavua: etuliite 0x04 + x-koordinaatti + y-koordinaatti. Pakattu muoto käyttää vain 33 tavua: etuliite 0x02 tai 0x03 (riippuen y:n pariteetista) + x-koordinaatti. Bitcoin käytti alun perin pakkaamattomia avaimia, mutta suosii nyt pakattuja avaimia tehokkuuden vuoksi.


#### Bitcoin Address Luominen


Bitcoin-osoitteet ovat julkisten avainten hasheja, eivät itse avaimia. generate-osoitteen saamiseksi julkinen avain sarjallistetaan SEC-muodossa, lasketaan hash160 ([SHA-256](https://planb.academy/resources/glossary/sha256), sitten RIPEMD-160), lisätään verkko-etuliite (0x00 mainnet:lle, 0x6F testnetille), lasketaan tarkistussumma käyttämällä kaksinkertaista SHA-256:ta, lisätään neljä ensimmäistä tarkistussumman tavua ja koodataan tulos Base58:lla. Tämä koodaus poistaa moniselitteiset merkit ja sisältää tarkistussumman kirjoitusvirheiden välttämiseksi. Monivaiheinen putki kätkee julkisen avaimen, kunnes käytetään, lisää verkon tunnisteen ja varmistaa ihmisen luettavissa olevat, virheitä kestävät osoitteet.


# Bitcoin-transaktion sisäiset toiminnot

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Tapahtumien analysointi ja ECDSA-allekirjoitukset

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>


![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


### ECDSA:n ymmärtäminen: Bitcoin:n digitaalisen allekirjoituksen perusta


Bitcoin perustuu ECDSA:han, elliptiseen käyrään perustuvaan allekirjoitusjärjestelmään, joka tarjoaa vahvan turvallisuuden paljon pienemmillä avainkokoluokilla kuin RSA. Sen turvallisuus perustuu elliptisen käyrän diskreetin logaritmin ongelmaan: kun P = eG, P:n laskeminen on helppoa, mutta e:n johtaminen P:stä on laskennallisesti mahdotonta. Tämä epäsymmetria mahdollistaa julkisen avaimen salauksen ja pitää samalla yksityiset avaimet turvassa.


#### ECDSA-allekirjoitusten DER-koodaus


Bitcoin koodaa ECDSA-allekirjoitukset DER-muodossa:


- 0x30 (sekvenssimerkki)
- pituus tavu
- 0x02 + pituus + R tavua
- 0x02 + pituus + S tavua


Tämä lisää yleiskustannuksia, sillä 64 tavun allekirjoitus kasvaa ~71-72 tavuun. [Taproot](https://planb.academy/resources/glossary/taproot) poistaa tämän tehottomuuden ottamalla käyttöön kiinteän kokoiset [Schnorr](https://planb.academy/resources/glossary/schnorr-protocol)-allekirjoitukset.


### Allekirjoitussitoumukset ja allekirjoitusprosessi


ECDSA-allekirjoitukset perustuvat sitoutumisyhtälöön: UG + VP = KG. Allekirjoittaja valitsee nollasta poikkeavat U- ja V-arvot sekä satunnaisen [nonce](https://planb.academy/resources/glossary/nonce)-koodin K, jolla hän todistaa tietävänsä yksityisen avaimen paljastamatta sitä. Viesti hakataan Z:hen, luodaan satunnainen K, R on KG:n x-koordinaatti ja S = (Z + RE)/K. Allekirjoitus on pari (R, S). Turvallisuus riippuu ratkaisevasti siitä, että käytetään ainutlaatuista, arvaamatonta K:ta - jos K:ta käytetään uudelleen tai se vuotaa, yksityinen avain on vaarassa. Nykyaikaisissa toteutuksissa käytetään determinististä K:n generointia (RFC 6979), jotta vältytään RNG:n virheiltä.


#### Allekirjoituksen todentaminen

Kun Z, (R, S) ja julkinen avain P on annettu, todentaja laskee U = Z/S ja V = R/S ja tarkistaa sitten, onko UG + VP:n x-koordinaatti yhtä suuri kuin R. Tämä toimii, koska todentamisalgebra rekonstruoi KG:n tarvitsematta yksityistä avainta. Allekirjoitusten väärentäminen edellyttäisi diskreetin lokiongelman ratkaisemista tai hash-funktion murtamista.


#### Schnorrin allekirjoitukset ja historiallinen konteksti


Schnorr-allekirjoitukset ovat matemaattisesti puhtaampia ja tukevat aggregointiominaisuuksia, mutta ne oli patentoitu Bitcoin:n käynnistyessä. ECDSA tarjosi ilmaisen vaihtoehdon, mutta se oli monimutkaisempi ja allekirjoitukset olivat suurempia. Kun patenttien voimassaolo päättyi, Bitcoin lisäsi Schnorr-allekirjoitukset Taproot:n kautta, mikä tarjosi kiinteät 64 tavun allekirjoitukset ja paransi yksityisyyttä. ECDSA:ta tuetaan edelleen vanhan yhteensopivuuden vuoksi.



### Transaktiorakenne ja tulot/lähtötiedot


Bitcoin-tapahtuma koostuu seuraavista osista:


- versio (4 tavua, little-endian)
- syöttöluettelo
- tulostusluettelo
- locktime (4 tavua)


Sisäänmenot viittaavat edellisiin [UTXO](https://planb.academy/resources/glossary/utxo)-operaatioihin niiden tapahtumahashin ja lähtöindeksin avulla, ja ne sisältävät lukituksen avausskriptin (scriptSig) ja sekvenssinumeron, jota käytetään aikalukituksissa tai RBF:ssä. Tuotokset määrittelevät summan (8 tavua) ja lukitusskriptin (scriptPubKey), jotka määrittelevät käyttöehdot. Bitcoin-osoitteet ovat näiden skriptien esityksiä.


#### UTXO-malli

Bitcoin seuraa käyttämättömiä tuotoksia eikä tilien saldoja. UTXO:t on käytettävä kokonaan - osittainen käyttö on mahdotonta. Jos haluat käyttää 1 BTC 100 BTC:n UTXO:stä, transaktioon on sisällyttävä muutostulos. Vaihtotuloksen unohtaminen muuttaa loput louhintamaksuksi.


#### Transaktioiden sarjallistaminen ja jäsennys


Tapahtumissa käytetään kompaktia binäärimuotoa. Versiokentän jälkeen varint-kenttä koodaa syötteiden lukumäärän. Syötteitä ovat:


- edellisen lähetyksen hash (32 tavua)
- lähtöindeksi (4 tavua)
- scriptSig (varstr)
- sekvenssi (4 tavua)


Tulosteet sisältävät 8 tavun määrän ja scriptPubKey (varstr). Locktime ohjaa, milloin tapahtuma tulee voimaan. Serialisointi käyttää little-endian järjestystä useimmille kokonaisluvuille. Parserit kuluttavat tavuja peräkkäin ja delegoivat erikoistuneille luokille tuloja, lähtöjä ja skriptejä varten.


### Maksut, muutos ja muokattavuus


Maksut ovat epäsuoria:

maksu = summa(tuloarvot) - summa(lähtöarvot).

Kaikista määrittämättömistä arvoista tulee maksu, joten oikea muutoslaskenta on olennaisen tärkeää. Ennen [SegWit](https://planb.academy/resources/glossary/segwit):ta allekirjoitukset mahdollistivat muokattavuuden - S:n muuttaminen N-S:ksi tuotti uuden voimassa olevan tapahtuman eri tunnuksella. Bitcoin panee nyt täytäntöön low-S-säännön, ja SegWit eristää allekirjoitukset txid-laskennasta, mikä tekee tunnuksista vakaita ja mahdollistaa [Lightningin](https://planb.academy/resources/glossary/lightning-network) kaltaiset toisen tason protokollat.


## Bitcoin Skriptien ja tapahtumien validointi

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>


![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


Bitcoin Script on pieni, pinoihin perustuva älykäs sopimuskieli, joka määrittelee, miten kolikoita voidaan käyttää. Jokaisessa ulostulossa on scriptPubKey (lukitusskripti) ja jokaisessa sisääntulossa on scriptSig (lukituksen avausskripti). Yhdessä ne muodostavat ohjelman, jonka on arvotettava "true", jotta rahankäyttö olisi pätevä. Script ei ole tarkoituksella Turing-pääteinen, jotta kaikki suoritusreitit ovat ennakoitavissa ja helposti validoitavissa koko verkossa.


### Skriptioperaatiot ja suoritusmalli


Skripti on dataelementtien ja opkoodien sarja. Datatykit (allekirjoitukset, julkiset avaimet, hasheet) sijoitetaan pinoon, kun taas `OP_`-alkuiset op-koodit muuttavat pinoa. Suorittamisen jälkeen pinon ylimmän elementin on oltava nollasta poikkeava, jotta se onnistuisi. Esimerkkejä: `OP_DUP` kopioi ylimmän elementin, `OP_HASH160` soveltaa SHA256:ta ja sen jälkeen RIPEMD160:tä ja `OP_CHECKSIG` tarkistaa allekirjoituksen transaktion sighashia ja julkista avainta vastaan, ja jos allekirjoitus on kelvollinen, siirretään 1, jos se on kelvoton, 0 jos se on virheellinen. Parsing-säännöt erottavat toisistaan raakadatan (pituusennuste) ja opcodit (etsitään tavuarvon mukaan), ja pieni virtuaalikone suorittaa ne deterministisesti jokaisessa [solmussa](https://planb.academy/resources/glossary/node).


### P2PK ja P2PKH: keskeiset maksumallit


Varhaisin malli, Pay-to-Public-Key (P2PK), lukitsi kolikot suoraan täydelliseen julkiseen avaimeen: scriptPubKey on `<pubkey> OP_CHECKSIG`, ja scriptSig on vain allekirjoitus. Se on yksinkertainen mutta tilantarpeen kannalta tehoton ja paljastaa julkisen avaimen ennen kolikoiden käyttämistä.


#### P2PKH ja osoitteet

Pay-to-Public-Key-Hash (P2PKH) parantaa tätä lukitsemalla julkisen avaimen 20 tavun hashiin. ScriptPubKey on `OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG`, ja scriptSig tarjoaa `<signature> <pubkey>`. Suoritus tarkistaa, että annettu julkinen avain on hashattu sitoutuneeseen arvoon, ja tarkistaa sitten allekirjoituksen. Tämä piilottaa julkisen avaimen siihen asti, kunnes kuluttaa aikaa, pienentää kokoa ja vastaa tuttua "1..." mainnet-osoitteen muotoa.


### Tapahtuman validointi ja allekirjoituksen häivytys


Tapahtumaa validoivan solmun on varmistettava:

1) Kukin tulo viittaa olemassa olevaan, käyttämättömään lähtöön.

2) Kokonaispanosarvo ≥ kokonaistuotosarvo (erotus on maksu).

3) Kukin scriptSig avaa oikein sen viitteenä olevan scriptPubKey-avaimen lukituksen.


Allekirjoituksen todentaminen edellyttää tarkan allekirjoitetun viestin, niin sanotun sighashin, rakentamista. Vanhassa ECDSA:ssa validointi tyhjentää kaikki scriptSig:t, korvaa nykyisen syötteen scriptSig:n vastaavalla scriptPubKey:llä, lisää 4 tavun hash-tyypin (yleensä `SIGHASH_ALL`) ja kaksinkertaistaa tuloksen. Tätä 256-bittistä arvoa käyttää `OP_CHECKSIG`. Vaihtoehtoiset hash-tyypit (esim. `SINGLE`, `NONE`, `ANYONECANPAY`:n kanssa tai ilman sitä) muuttavat sitä, mihin transaktion osiin sitoudutaan, ja mahdollistavat kapeat käyttötapaukset, kuten yhteisrahoituksen tai osittain määritellyt transaktiot, mutta niitä käytetään käytännössä harvoin.


#### Kvadrattinen häivytys ja SegWit

Koska jokainen perintötapahtuman syöttö vaatii oman sighash-laskentansa rakenteessa, joka sisältää kaikki syötteet, validointiaika voi kasvaa nelinkertaisesti syötteiden määrän myötä. Suuret monisyöttöiset tapahtumat aiheuttivat aikoinaan huomattavia validointiviiveitä. SegWit:ssä sighash-laskenta suunniteltiin uudelleen siten, että jaetut osat tallennetaan välimuistiin ja monimutkaisuus vähennetään lineaariseen aikaan, mikä parantaa skaalautuvuutta ja vaikeuttaa palvelunestohyökkäyksiä.


### Skriptiarvoitukset ja tietoturvatunnit


Skripti voi ilmaista paljon enemmän kuin pelkkä "yksi allekirjoitus avaa nämä kolikot" Script-arvoitukset osoittavat tämän koodaamalla mielivaltaisia ehtoja - matemaattisia ongelmia, hash-esikuvahaasteita tai jopa törmäyspalkkioita - joissa kuka tahansa, joka antaa oikeat tiedot, voi käyttää kolikot. Pelkkiin julkisiin tietoihin (ei allekirjoituksia) perustuvat tuotokset ovat kuitenkin alttiita louhijoiden etukäteisjohtamiselle: kun kelvollinen ratkaisu ilmestyy [mempooliin](https://planb.academy/resources/glossary/mempool), kuka tahansa [louhija](https://planb.academy/resources/glossary/miner) voi kopioida sen ja ohjata voiton itselleen.


Käytännön opetus on se, että reaalimaailman sopimukset sisältävät lähes aina allekirjoitusten tarkistuksia, vaikka ne sisältäisivätkin monimutkaisempaa logiikkaa, kuten multisig-, timelock- tai hashlock-menetelmiä. Allekirjoitukset sitovat ratkaisun tiettyyn osapuoleen, mikä säilyttää kannustimet ja estää muita varastamasta voittoa. Skriptin pinomallin, vakiomallien ja hienovaraisten sudenkuoppien ymmärtäminen on olennaista turvallisten Bitcoin-älykkäiden sopimusten suunnittelussa ja päättelyssä siitä, miten transaktiot todella validoidaan verkossa.


## Tapahtumien rakentaminen ja Pay-to-Script Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>


![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


### Bitcoin- ja P2SH-tapahtumien rakentaminen


Bitcoin-tapahtumien rakentaminen yhdistää teoreettisen protokollatiedon ja käytännön toteutuksen. Transaktio valitsee UTXO:t käytettäväksi, rakentaa ulostulot lukitusskripteillä, luo allekirjoitukset jokaiselle syötteelle ja serialisoi kaiken täsmälleen solmujen odottamassa muodossa. Prosessi edellyttää sighashin tuottamisen ymmärtämistä, skriptien käyttäytymistä ja oikeaa maksujen ja muutosten käsittelyä.


### Transaktioiden perusrakenne


Jokainen tapahtuman tulo viittaa edelliseen tulosteeseen txid:n ja indeksin avulla. Tuloksissa määritetään määrät satosheina ja lukitusskripteinä. Tulojen ja lähtöjen kokonaismäärän erotus on maksu. Syötteen allekirjoittamiseksi muunnettu versio transaktiosta sarjallistetaan, sen sighash lasketaan ja yksityinen avain allekirjoittaa sen. Näin saatu allekirjoitus ja julkinen avain muodostavat ScriptSigin. Kun jokainen panos on allekirjoitettu, raaka transaktio voidaan lähettää verkkoon.


### Usean allekirjoituksen tapahtumat


Paljas multisig käyttää `OP_CHECKMULTISIG`:ta vaatia m-of-n allekirjoituksia. Varhaisen off-by-one-virheen vuoksi OP_CHECKMULTISIG kuluttaa ylimääräisen pinoelementin ja vaatii ScriptSigin alkuperäisen `OP_0`:n. Paljas multisig on toimiva mutta tehoton: kaikki julkiset avaimet ovat on-chain, mikä tekee scriptPubKeys-avaimista suuria, kalliita ja vaikeasti osoitteiksi koodattavia. Näiden rajoitusten vuoksi otettiin käyttöön pay-to-script-hash.


#### P2SH Arkkitehtuuri

P2SH piilottaa monimutkaiset skriptit 20 tavun HASH160-koodin taakse. ScriptPubKey on korjattu: `OP_HASH160 <20-byte hash> OP_EQUAL`. Taustalla oleva lunastusskripti - joka sisältää multisig-, timelock- tai muita ehtoja - paljastuu ja suoritetaan vain, kun se käytetään. Lähettäjä näkee vain hash-tunnisteen, kun taas vastaanottaja hallinnoi lunastusskriptiä yksityisesti. Tämä rakenne pienentää on-chain:n kokoa, parantaa yksityisyyttä ja mahdollistaa monimutkaiset sopimukset kuormittamatta lähettäjiä.


### P2SH Menot ja täytäntöönpano


P2SH-tulosteen käyttämiseksi ScriptSigin on sisällettävä tarvittavat lukituksen avaamistiedot * sekä* itse lunastusskripti. Validointi tapahtuu kahdessa vaiheessa:

1) HASH160(redeem_script):n on vastattava scriptPubKey-hashia.

2) Tarkastuksen jälkeen lunastusskripti suoritetaan annetuilla tiedoilla.


Kun allekirjoituksia luodaan P2SH-syötteelle, sighash-prosessi käyttää lunastuskäsikirjoitusta scriptPubKey-avaimen sijasta. Kullakin allekirjoittajalla on oltava koko redeem-skripti, jotta generate voi antaa kelvollisia allekirjoituksia. P2SH-osoitteissa käytetään mainnet:ssa versiotietoa 0x05 ("3..."-osoitteet) ja testnetissä 0xC4 ("2..."-osoitteet).


#### Käytännön turvallisuusnäkökohdat


Lunastuskäsikirjoituksen menettäminen tarkoittaa varojen menettämistä: rahankäyttö edellyttää sekä yksityisiä avaimia että itse lunastuskäsikirjoitusta. Multisig-osallistujien on tarkistettava, että heidän julkiset avaimensa ovat oikein mukana, ennen kuin he hyväksyvät talletuksia. P2SH tukee kehittyneitä rakenteita, kuten multisig-, timelock- ja hashlock-menetelmiä, mutta virheet skriptilogiikassa voivat lukita varat pysyvästi, joten testaus testiverkossa on välttämätöntä.


P2SH parantaa yksityisyyttä piilottamalla käyttöehdot ensimmäiseen käyttökertaan asti, mutta kun lunastuskomentosarja ilmestyy on-chain:een, se tulee pysyvästi näkyviin. Tästä huolimatta pienemmän koon, taaksepäin yhteensopivuuden ja joustavan sopimustuen tuomat edut tekivät P2SH:sta merkittävän virstanpylvään, joka vaikutti myöhempiin päivityksiin, kuten SegWit:een ja Taproot:een.


# Bitcoin-verkon sisäinen toiminta

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin-lohkot ja Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>


![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


Bitcoin estää ryhmätapahtumat ja suojaa ne [proof of work](https://planb.academy/resources/glossary/proof-of-work):n avulla. Kukin [lohko](https://planb.academy/resources/glossary/block) sisältää 80 tavun [otsikon](https://planb.academy/resources/glossary/block-header) ja luettelon tapahtumista. Huolimatta kelvollisen lohkon tuottamisen suurista energiakustannuksista lohkon todentaminen on halpaa: kaikkien ~900k otsikoiden tallentaminen vaatii vain ~72 Mt, joten pienetkin laitteet voivat todentaa ketjun proof of work:n tehokkaasti.


### Coinbase-transaktiot ja lohkopalkkiot


Jokainen lohko alkaa täsmälleen yhdellä [Coinbase-tapahtumalla](https://planb.academy/resources/glossary/coinbase-transaction) - tämä on ainoa tapa, jolla uusia bitcoineja tulee liikkeeseen. Sillä on nollattu prev-tx-hash ja 0xffffffffff-indeksi, joka yksilöi sen yksiselitteisesti. Tuki alkoi 50 BTC:stä, ja se puolittuu 210 000 lohkon välein (50, 25, 12,5, 6,25, 3,125, ...). Louhijat sisällyttävät myös transaktiomaksut. Koska neljän tavun nonce on liian pieni nykyaikaisille ASIC-piireille, louhijat muokkaavat Coinbase-transaktion tietoja muuttaakseen [Merkle](https://planb.academy/resources/glossary/merkle-tree)-juurta ja luodakseen lisää hakutilaa. [BIP](https://planb.academy/resources/glossary/bip)34 edellyttää lohkon korkeuden upottamista Coinbase scriptSigiin, jotta varmistetaan, että jokainen Coinbase txid on ainutlaatuinen.


### Lohkon otsikkokentät ja Soft Fork-signalointi


80 tavun otsikko sisältää:


- versio (4 tavua)
- edellisen lohkon hash (32 tavua)
- Merkle-juuri (32 tavua)
- aikaleima (4 tavua)
- bittiä (vaikeuskohde, 4 tavua)
- nonce (4 tavua)


Versionumerot kehittyivät BIP9:n kautta bittikenttämerkintäjärjestelmäksi, jonka avulla kaivostyöntekijät voivat koordinoida [soft-fork](https://planb.academy/resources/glossary/soft-fork)-valmiutta. Aikaleima on 32-bittinen Unix-aika, ja se on päivitettävä vuoden 2106 tienoilla.


#### Bittien kenttä ja kohteet

Bitti-kenttä koodaa kohteen kompaktissa muodossa: kohde = kerroin × 256^(eksponentti-3). Kelvollisten lohko-hashien on oltava numeerisesti tämän tavoitteen alapuolella. Koska hasheja tulkitaan pieninä kokonaislukuina, kelvollisissa hasheissa on usein monta nollaa perässä, kun ne näytetään heksadesimaalina.


### Vaikeus, validointi ja mukautukset


Vaikeus määritellään muodossa lowest_target / current_target, mikä ilmaisee, kuinka paljon vaikeampi mining on nykyään verrattuna helpoimpaan mahdolliseen vaikeusasteeseen. Validointi edellyttää vain otsikon hash-arvon vertaamista tavoitteeseen - tämä on erittäin halpaa mining:een verrattuna.


Bitcoin säätää [vaikeusastetta](https://planb.academy/resources/glossary/difficulty) vuoden 2016 lohkojen välein siten, että se kohdistuu ~10 minuutin lohkoväleihin. Mukautuksessa verrataan edellisen vuoden 2016 lohkojen todellista aikaa odotettuihin kahteen viikkoon. Rajoitukset rajoittavat säätöjä neljän kertoimen sisällä. Suuret reaalimaailman tapahtumat - kuten Kiinan mining-kielto - osoittivat tämän mekanismin kestävyyden, kun hash-aste laski jyrkästi ja vaikeusaste mukautui alaspäin kompensoidakseen sen.


### Ryhmätuki ja kokonaismäärä Supply


Tuki korkeudella h lasketaan seuraavasti: tuki = 5_000_000_000 >> (h // 210_000). Näin saadaan puolittamisaikataulu, joka konvergoi kohti ~21 miljoonan BTC:n kokonaistarjontaa. Geometrisen sarjan (50 + 25 + 12,5 + ...) × 210 000 summaaminen selittää ylärajan. Louhijat voivat vaatia vähemmän kuin sallittu tuki, mutta eivät koskaan enempää, tai lohkosta tulee mitätön. Kun tukipalkkiot pienenevät peräkkäisten puolikkaiden aikana, transaktiomaksuista tulee yhä tärkeämpi osa louhijoiden tuloja ja verkon pitkän aikavälin turvallisuutta.


## Verkkoviestintä ja Merkle-puut

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>


![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


### Bitcoin Verkkoarkkitehtuuri


Bitcoin:n [vertaisverkko](https://planb.academy/resources/glossary/peertopeer-p2p) toimii hajautettuna juoru-järjestelmänä, jossa solmut välittävät transaktioita ja lohkoja toisilleen luottamatta toisiinsa. Uudet solmut käynnistyvät ottamalla yhteyttä ydinkehittäjien ylläpitämiin kovakoodattuihin DNS-siemeniin. Nämä DNS-siemenet palauttavat aktiivisten vertaisverkkojen IP-osoitteet, minkä ansiosta solmut voivat löytää verkon ja pyytää uusia vertaisverkkoja getaddr-ohjelman avulla. Verkko ei tarkoituksella ole konsensuskriittinen, joten toteutukset voivat poiketa toisistaan, kunhan [konsensussäännöt](https://planb.academy/resources/glossary/consensus) pysyvät muuttumattomina.


### Viestin rakenne ja kättely


Kaikissa Bitcoin P2P-viesteissä käytetään kiinteää kirjekuorta: 4 tavun maaginen arvo (F9BEB4D9 mainnet:ssä), 12 tavun ASCII-komento, 4 tavun little-endian hyötykuorman pituus, 4 tavun tarkistussumma ([hash](https://planb.academy/resources/glossary/hash-function)256:n 4 ensimmäistä tavua) ja hyötykuorma. Yleisiä komentoja ovat version, verack, inv, getdata, tx, block, getheaders, headers, ping ja pong.


Kättely alkaa, kun yhdistävä solmu lähettää versioviestin. Vastaanottaja vastaa verackilla ja omalla versiollaan. Kun molemmat osapuolet ovat vaihtaneet nämä kaksi viestiä, yhteys on aktiivinen ja solmut voivat aloittaa inventaarioiden ja tietojen välittämisen.


### Merkle-puut ja Merkle-juuret


Bitcoin tallentaa jokaisen lohkon otsikkoon yhden 32 tavun Merkle-juuren, joka on sitoumus kaikkiin lohkon tapahtumiin. Tapahtumat hakkeroidaan (hash256), paritetaan, yhdistetään ja hakkeroidaan toistuvasti, kunnes jäljelle jää yksi hakkerointi. Kun tasossa on pariton määrä, viimeinen hash kopioidaan. Sisäisesti hashit ovat big-endian, kun taas sarjallistetut lohkotiedot ovat little-endian, mikä edellyttää käänteislukuja ennen ja jälkeen puun rakentamisen.


#### Merkle-todistukset ja SPV

Merkle-todistusten avulla voidaan todentaa, että transaktio sisältyy lohkoon lataamatta koko lohkoa. Todiste koostuu sisarhasheista, jotka kulkevat polkua pitkin juureen. Kevyet SPV-asiakkaat tallentavat vain lohkojen otsikot ja pyytävät näitä todisteita [täysiltä solmuilta](https://planb.academy/resources/glossary/full-node). Koska Merkle-puu kasvaa logaritmisesti, tuhansia transaktioita sisältävään lohkoon kuulumisen todistaminen vaatii vain muutamia satoja tavuja.


Taproot laajentaa tätä konseptia sitomalla menoehdot Merklized script tree (MAST) -käsikirjoituspuuhun, joka paljastaa vain suoritetun haaran ja Merkle-todistuksen. Tämä parantaa sekä tehokkuutta että yksityisyyttä.


### Verkkotoiminnot ja lohkojen synkronointi


Solmut käyttävät getdata-toimintoa pyytääkseen transaktioita tai lohkoja ja ilmoittavat tyyppitunnuksen (1=tx, 2=lohko, 3=suodatettu lohko, 4=kompakti lohko) sekä 32 tavun tunnisteen. Ketjusynkronointia varten solmut lähettävät getheaders-tiedot, joissa on alkulohkon hash, ja saavat vastauksena enintään 2000 otsikkoa. Kukin palautettu otsikko on 80 tavua, jonka jälkeen on nollan suuruinen tyhjä transaktioluku.


Vastaanotettujen lohkojen täydellinen todentaminen edellyttää kahta tarkistusta:

1. Lohkon hashin on oltava bits-kenttään koodatun tavoitteen alapuolella.

2. Kaikkien tapahtumien perusteella lasketun Merkle-juuren (asianmukainen endianness-käsittely) on vastattava otsikon juurta.


Vain jos molemmat ehdot täyttyvät, solmu hyväksyy lohkon, mikä vastaa Bitcoin:n "älä luota, tarkista" -periaatetta.


## Kehittynyt solmuviestintä ja erotettu todistaja

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>


![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)


Tässä istunnossa yhdistetään kehittynyt P2P-verkko ja Segregated Witness ja näytetään, miten nykyaikaiset Bitcoin-ohjelmistot ovat suoraan vuorovaikutuksessa solmujen kanssa ja käyttävät SegWit-tietoisia transaktiorakenteita. Kehittäjät oppivat hakemaan lohkoja, etsimään asiaankuuluvia transaktioita ja rakentamaan transaktioita käyttämällä vain raakaa verkkoviestintää - lohkoetsintäohjelmia ei tarvita.


### Lohkopohjainen tapahtumien haku ja yksityisyys


[Lompakoiden](https://planb.academy/resources/glossary/wallet) on havaittava saapuvat maksut skannaamalla lohkot niiden scriptPubKey-avaimen mukaisten tuotosten varalta. Kokonaislohkojen hakeminen suojaa yksityisyyttä paremmin kuin yksittäisten transaktioiden pyytäminen, joka antaa voimakkaita signaaleja käyttäjän toiminnasta. Jopa lohkopyynnöt voivat vuotaa tietoja vähäliikenteisistä ketjuista, minkä vuoksi kompaktit lohkosuodattimet (BIP158) ovat välttämättömiä yksityisyyden suojaavia kevytasiakkaita varten. Suodattimet voivat tuottaa vääriä positiivisia mutta eivät koskaan vääriä negatiivisia tuloksia, jolloin asiakkaat voivat ladata vain mahdollisesti merkityksellisiä lohkoja paljastamatta tiettyjä osoitteita.


### Trustless Verkon vuorovaikutus


Get_block-työnkulku osoittaa verkon oikean käytön: lähetetään getdata, vastaanotetaan lohko ja tarkistetaan sen jälkeen itsenäisesti sen Merkle-juuri ja proof of work. Lohko hyväksytään vain, jos vastaanotetun otsikon hash vastaa pyydettyä hashia ja sen laskettu Merkle-juuresta vastaa otsikkoa. 


#### Tapahtumien hakeminen lohkoista

Lohkon transaktiot voidaan skannata yhteensopivien scriptPubKeys-avainten löytämiseksi yksinkertaisella iteraatiolla. Tuotantolompakot suorittavat tämän jatkuvasti uusien lohkojen saapuessa ja todistavat tuotosten omistajuuden tiukasti kryptografisella validoinnilla sen sijaan, että tukeuduttaisiin kolmannen osapuolen API-rajapintoihin.


### SegWit Tavoitteet ja suunnittelu


Erillinen todistaja (SegWit) korjasi tapahtumien vääristettävyyden poistamalla allekirjoitustiedot txid-laskennasta. Tämä mahdollisti luotettavat ennalta allekirjoitetut tapahtumaketjut ja teki Lightning Network:stä käytännöllisen. SegWit lisäsi myös lohkokapasiteettia "lohkopainon" avulla: vanhat solmut näkevät edelleen ≤1 MB:n lohkoja, kun taas päivitetyt solmut validoivat jopa 4 MB:n lohkoja, mukaan lukien todistajatiedot. Versionoidut todentajaohjelmat (toistaiseksi v0-v1) luovat jäsennellyn päivityspolun tulevia skriptityyppejä varten.


#### P2WPKH (alkuperäinen SegWit)


P2WPKH korvaa perinteisen P2PKH-rakenteen 22 tavun käsikirjoituksella: OP_0 + push20 + hash160(pubkey). Spending siirtää allekirjoituksen ja pubkey:n erilliseen todistajakenttään.


- Ennen SegWit:ää syntyneet solmut: katso "kuka tahansa voi käyttää", käsittele sitä pätevänä.
- SegWit:n jälkeiset solmut: tunnistavat OP_0 + 20 tavun hash ja validoivat todistajatietojen avulla.


Tämä erottelu korjaa muokattavuutta ja vähentää maksuja. Todistaja käyttää varint-lukua, jota seuraa allekirjoitus ja julkinen avain.


#### P2SH-P2WPKH (taaksepäin yhteensopiva SegWit)


Jotta vanhat lompakot voivat lähettää SegWit-osoitteisiin, P2WPKH-skriptit voidaan kääriä P2SH:ään.


- scriptPubKey: standardi P2SH hash160(redeemScript)
- scriptSig: lunastusskripti (P2WPKH-ohjelma)
- todistaja: allekirjoitus + julkinen avain


Validointikerrokset:

1. Pre-BIP16-solmut hyväksyvät redeemScriptin kelvolliseksi.

2. BIP16:n jälkeiset solmut arvioivat sen, jolloin OP_0 + hash jää pinoon.

3. SegWit-solmut suorittavat täydellisen todistajan validoinnin.


#### P2WSH monimutkaisia skriptejä varten


P2WSH yleistää SegWit:n monimerkkisiä ja kehittyneitä skriptejä varten sitoutumalla SHA256(script):iin hash160:n sijasta. Tyypillinen 2:3 multisig-todistajapino:


- tyhjä elementti (CHECKMULTISIG-virhe)
- sig1
- sig2
- todistajakäsikirjoitus (multisig-käsikirjoitus)


SegWit-solmut tarkistavat, että SHA256(witnessScript) vastaa scriptPubKey-hashia, ja suorittavat sen sitten. SHA256:n ja 32 tavun hashin käyttö mahdollistaa P2WSH:n erottamisen P2WPKH:stä ja vahvistaa turvallisuutta.


#### P2SH-P2WSH (suurin yhteensopivuus)


Monimutkaiset SegWit-skriptit voidaan myös paketoida P2SH-kääreellä:


- scriptSig: redeemScript (OP_0 + 32 tavun hash)
- todistaja: allekirjoitukset + witnessScript


Validointi käy läpi kolme sääntösukupolvea täsmälleen samoin kuin P2SH-P2WPKH:ssä. Tämä kääre oli välttämätön varhaisissa Lightning-käyttöönotoissa, joissa tarvittiin monisignaalisuutta ilman muokattavuutta. Vaikka nykyään suositaan natiivia P2WSH:ta, kääritty muoto takaa yhteensopivuuden vanhempien wallet-järjestelmien kanssa.


### SegWit:n vaikutus


SegWit toimitti:


- vakaat tapahtumatunnukset
- alhaisemmat palkkiot alennettujen todistajatietojen avulla
- suurempi lohkojen läpimeno lohkojen painon avulla
- yhteensopivuus vanhojen solmujen kanssa
- puhdas päivityspolku Taproot:lle ja tuleville laajennuksille


Yhdessä luotettavan verkkovuorovaikutuksen kanssa nämä työkalut muodostavat nykyaikaisen Bitcoin-kehityksen selkärangan.



# Viimeinen jakso


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Arvostelut & arvostelut


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Loppukoe


<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>



<isCourseExam>true</isCourseExam>

## Päätelmä



<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>


<isCourseConclusion>true</isCourseConclusion>