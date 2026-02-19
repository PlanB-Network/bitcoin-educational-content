---
name: Rust:n oppiminen Bitcoin:lla
goal: Kehitä Rust-kehitystaitojasi Bitcoin-koodauksen avulla
objectives: 

  - Totuttele Rust-kieleen
  - Ymmärtää, miksi Rust:n käyttö Bitcoin:n kehittämiseen on tarpeen
  - Hanki Lightning SDK:n perusta

---

# Rust-retkikunta Bitcoin-rakentajille



Tällä käytännönläheisellä kurssilla, joka kuvattiin Fulgur' Venturesin lokakuussa 2023 järjestämässä seminaarissa, kehität Rust-taitojasi rakentamalla oikeita Bitcoin-komponentteja ja miniprojekteja. Käsitellään Rust:n perusteita, miksi Rust:tä käytetään Bitcoin-kehityksessä (muistiturvallisuus, suorituskyky ja turvallinen rinnakkaisuus) ja miten pääset alkuun Lightning SDK:n kanssa maksuominaisuuksien rakentamisessa.


Luvuissa harjoitellaan Rust:n keskeisiä malleja (omistajuus, elinikä, piirteet, asynkkaus), työskennellään Bitcoin:n primitiivien kanssa (avaimet, transaktiot, skriptaaminen) ja integroidaan vähitellen Lightning-käsitteitä (solmut, kanavat, laskut).


Aiempaa Rust- tai Bitcoin-kehitystä ei ehdottomasti vaadita, mutta perusohjelmoinnin tuntemus auttaa. Kurssi on aloittelijoille sopiva, mutta riittävän käytännöllinen Bitcoin:een siirtyville insinööreille.


+++

# Johdanto

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>


## Kurssin yleiskatsaus

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>


**Esittely**


Tervetuloa tälle aloittelijoille suunnatulle SDK-ohjelmointikurssille. Tässä koulutuksessa opit Rust:n perusteet, sitten keskityt Rust:een sovellettuna Bitcoin-ohjelmointiin ja lopuksi esitellään joitakin käyttötapauksia SDK:iden avulla.


Koulutuksen videot ovat toistaiseksi saatavilla vain englanniksi, ja se oli osa Fulgure Venturen viime lokakuussa Toscanassa järjestämää live-seminaaria. Tässä koulutuksessa keskitytään vain ensimmäiseen viikkoon. Toinen puolisko oli suunnattu RGB:lle, ja se löytyy RGB-kurssista.


https://planb.academy/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

Tämä koulutus antaa sinulle mahdollisuuden kehittää ohjelmointitaitojasi Lightning Network:lla Rust:n ja eri SDK:iden avulla. Se on tarkoitettu kehittäjille, joilla on vankka ohjelmointitausta ja jotka haluavat syventyä Lightning Network-kohtaiseen kehitystyöhön. Opit Rust:n perusteet, miksi se soveltuu Bitcoin-kehitykseen, ja siirryt sitten käytännön toteutukseen erikoistuneiden SDK:iden avulla.


**Osio 2: Opi koodaamaan Rust**:n avulla

Tässä osiossa tutustut Rust:n perusteisiin asteittain etenevien lukujen avulla. Opit kirjoittamaan Rust-koodia, ymmärtämään sen erityispiirteitä ja hallitsemaan sen keskeiset ominaisuudet seitsemässä yksityiskohtaisessa osassa. Tämä moduuli on välttämätön, jotta ymmärrät, miksi Rust on Bitcoin-kehityksen suosikkikieli.


**Luku 3: Rust ja Bitcoin**

Seuraavassa tarkastelemme perusteellisesti, miksi Rust on relevantti valinta Bitcoin:n kehittämisen kannalta. Opit sen virhemallista, UniFFI-työkalusta ja asynkronisista piirteistä, jotka ovat kaikki keskeisiä tekijöitä vankkojen ja turvallisten ohjelmistojen rakentamisessa.


**Luku 4: LNP/BP-kehitys SDK:iden avulla**

Opit kehittämään LN-solmuja käyttämällä eri SDK:ta, kuten Breez SDK:ta ja Greenlight for Lipa:tä. Näet, miten Lightning Network-sovelluksia toteutetaan Bitcoin- ja Lightning-kehityksen yksinkertaistamiseen suunniteltujen kirjastojen avulla.


Oletko valmis kasvattamaan Lightning Network-taitojasi Rust:n avulla? Mennään!

# Opi koodaamaan ruostekirjan avulla

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>


## Johdanto Rust:een

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>


:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::

### Rust:n asentaminen ja hallinta Rustupin avulla


Kun aloitat matkasi Rust:n kanssa, ensimmäinen askel on kunnollisen kehitysympäristön luominen. Yleisimmin suositeltu lähestymistapa Rust:n asentamiseen on Rustup, työkaluketjun hallintajärjestelmä, joka hoitaa asennuksen ja päivitykset eri projekteissa ja alustoilla.


Rustup on muutakin kuin pelkkä asennusohjelma - se toimii Rust-kehitysympäristön kattavana hallintatyökaluna. Rustupin avulla voit helposti asentaa lisäkäännöskohteita eri alustoille, kuten ARM64 Android-kehitystä varten tai muita arkkitehtuureja, joita saatat tarvita. Työkalu käsittelee myös Rust-päivitykset saumattomasti, mikä on erityisen arvokasta, kun otetaan huomioon, että Rust julkaisee uuden vakaan version noin kuuden viikon välein. Kun haluat päivittää uusimpaan versioon, yksinkertainen `rustup update`-komento hoitaa kaiken automaattisesti.


Kun asennat Rustupia, kannattaa ymmärtää siihen liittyvä tietoturvamalli. Asennusprosessi lataa ja suorittaa skriptin Rust:n viralliselta verkkosivustolta HTTPS:n kautta, mikä tarjoaa kuljetuskerroksen salausturvan. Rustupin ja Cargon lataamat paketit tulevat luotettavista lähteistä (crates.io ja virallinen Rust-infrastruktuuri) ja hyötyvät HTTPS-salauksesta. Vaikka tämä lähestymistapa on turvallinen useimmissa kehitysskenaarioissa, jotkin organisaatiot, joilla on tiukat tietoturvakäytännöt, saattavat asentaa Rust:n mieluummin Linux-jakelunsa paketinhallinnan kautta, joka tarjoaa ylimääräisen luottamuksen jakelun oman pakettien allekirjoitusinfrastruktuurin kautta. Oppimiseen ja yleisiin kehitystarkoituksiin Rustup on vakiintunut ja laajalti luotettu työkalu Rust-ekosysteemissä.


Useimpiin kehitystilanteisiin voit asentaa Rustupin suorittamalla Rust:n virallisella verkkosivustolla olevan asennusskriptin. Asennusohjelma pyytää sinua valitsemaan eri työkaluketjuvaihtoehtojen välillä, ja useimmille käyttäjille suositellaan vakaata työkaluketjua. Asennus tapahtuu kotihakemistoosi, eikä vaadi järjestelmänvalvojan oikeuksia, ja se asettaa kaikki tarvittavat ympäristömuuttujat välitöntä käyttöä varten.


### Rust-työkaluketjujen ja komponenttien ymmärtäminen


Rust:n kehitysekosysteemi koostuu useista keskeisistä komponenteista, jotka toimivat yhdessä tarjoten täydellisen ohjelmointiympäristön. Näiden komponenttien ymmärtäminen auttaa sinua navigoimaan Rust:n kehitysprosessissa tehokkaammin ja ratkaisemaan ongelmia niiden ilmaantuessa.


Rust-kääntäjä, joka tunnetaan nimellä `rustc`, muodostaa Rust-työkaluketjun ytimen. Vaikka voisit teoriassa käyttää `rustc`:tä suoraan Rust-ohjelmien kääntämiseen, suurin osa kehitystyöstä perustuu Cargoon, Rust:n pakettihallinta- ja rakennusjärjestelmään. Cargo toimii samalla tavalla kuin npm JavaScript-ekosysteemissä: se hallitsee riippuvuuksia, koordinoi rakennuksia ja tarjoaa käteviä komentoja tavallisiin kehitystehtäviin. Kun suoritat komentoja kuten `cargo build` tai `cargo run`, Cargo organisoi kääntämisprosessin, hoitaa riippuvuuksien ratkaisemisen ja hallinnoi yleistä projektirakennetta.


Clippy on tulostin, joka analysoi koodisi ja antaa parannusehdotuksia. Toisin kuin yksinkertaiset syntaksin tarkistusohjelmat, Clippy ymmärtää Rust:n idiomeja ja voi suositella idiomaattisempia tapoja suorittaa tietyt tehtävät. Tämä työkalu auttaa Rust:n parhaiden käytäntöjen oppimisessa ja ylläpidettävämmän koodin kirjoittamisessa.


Rust-työkaluketju sisältää myös kattavat dokumentointityökalut ja standardikirjaston dokumentaation, joka on saatavilla Rust:n virallisella dokumentointisivustolla. Tämä dokumentaatio toimii korvaamattomana viitteenä kehitystyön aikana, sillä se tarjoaa yksityiskohtaista tietoa standardikirjaston funktioista, tyypeistä ja moduuleista. Dokumentaatio sisältää laajoja esimerkkejä ja selityksiä, jotka auttavat sinua ymmärtämään, mitä funktiot tekevät ja miten niitä käytetään tehokkaasti ohjelmissasi.


Rust tukee useita julkaisukanavia: vakaa, beta ja nightly. Vakaa kanava tarjoaa perusteellisesti testattuja julkaisuja, jotka soveltuvat tuotantokäyttöön. Beta-kanava tarjoaa esikatselun seuraavasta vakaasta julkaisusta, ja sitä käytetään ensisijaisesti lopulliseen testaukseen ennen virallista julkaisua. Nightly-kanava sisältää aktiivisessa kehityksessä olevia kokeellisia ominaisuuksia, joista voi olla hyötyä uusien Rust-ominaisuuksien kokeilemisessa, vaikka nämä ominaisuudet saattavat muuttua tai poistua tulevissa julkaisuissa.


### Rust-projektien luominen ja hallinta Cargolla


Nykyaikainen Rust-kehitys keskittyy Cargoon, joka tehostaa projektin luomista, riippuvuuksien hallintaa ja rakentamisprosessia. Manuaalisen hakemistojen ja tiedostojen luomisen sijaan Cargo tarjoaa komennon `cargo new`, jolla generate voi luoda täydellisen projektirakenteen järkevillä oletusasetuksilla.


Kun luot uuden projektin komennolla `cargo new project_name`, Cargo luo vakiomuotoisen hakemistorakenteen, luo perustiedoston `main.rs`, jossa on "Hello, world!"-ohjelma, alustaa Git-tietovaraston ja luo `Cargo.toml`-tiedoston projektin konfigurointia varten. `Cargo.toml`-tiedosto toimii projektisi keskeisenä konfigurointipisteenä, joka sisältää metatietoja projektistasi ja listaa kaikki koodisi vaatimat riippuvuudet.


Cargo tarjoaa useita tärkeitä komentoja päivittäiseen kehitystyöhön. Komento `cargo build` kääntää projektisi ja sen riippuvuudet ja luo suoritettavat tiedostot `target`-hakemistoon. Nopeaa iterointia varten kehitystyön aikana `cargo run` yhdistää rakentamisen ja suorituksen yhteen vaiheeseen. Komento `cargo check` suorittaa kaikki kääntämisen tarkistukset tuottamatta lopullista suoritettavaa tiedostoa, mikä tekee siitä huomattavasti nopeamman kuin täydellisestä buildista, kun haluat vain varmistaa, että koodisi kääntyy oikein.


Kun koodia valmistellaan tuotantokäyttöön, `--release`-lippu ottaa käyttöön optimoinnit ja poistaa virheenkorjausväitteet. Julkaisuversiot toimivat nopeammin ja tuottavat pienempiä suoritettavia tiedostoja, mutta niiden kääntäminen kestää kauemmin ja ne poistavat hyödyllisiä virheenkorjaustietoja. Kääntäjä käyttää erilaisia optimointeja julkaisukehitysten aikana ja poistaa käytöstä ajoaikaiset tarkistukset, kuten kokonaislukujen ylivuodon havaitsemisen, mikä parantaa suorituskykyä mutta poistaa joitakin debug-kehityksissä esiintyviä turvatakuita.


### Muuttujat, muunneltavuus ja Rust:n turvallisuusfilosofia


Rust:ssä käytetään muuttujien hallintaan erilaista lähestymistapaa kuin useimmissa kielissä. Oletusarvoisesti kaikki Rust:n muuttujat ovat muuttumattomia, mikä tarkoittaa, että niiden arvoja ei voi muuttaa alkuperäisen määrityksen jälkeen. Tällä suunnittelupäätöksellä pyritään ehkäisemään yleisiä ohjelmointivirheitä, jotka johtuvat odottamattomista tilamuutoksista.


Kun ilmoitat muuttujan käyttämällä `let x = 5`, muuttujasta tulee oletusarvoisesti muuttumaton. Jos sen arvoa yritetään muuttaa myöhemmin, syntyy käännösvirhe. Tämä muuttumattomuusvaatimus pakottaa kehittäjät miettimään tarkkaan, milloin tilamuutokset ovat todella tarpeen, ja tekee koodin käyttäytymisestä ennustettavampaa. Monet ohjelmointivirheet johtuvat muuttujien odottamattomista muutoksista, ja Rust:n oletusarvoinen muuttumattomuus auttaa ehkäisemään näitä ongelmia.


Kun muuttujan arvoa on todella muutettava, Rust vaatii muuttuvuuden nimenomaista ilmoittamista avainsanalla `mut`: `let mut x = 5`. Tämä eksplisiittinen ilmoitus on selkeä signaali sekä kääntäjälle että muille kehittäjille siitä, että muuttujan arvo voi muuttua ohjelman suorituksen aikana. Vaatimus nimenomaisesta muuttuvuuden ilmoittamisesta kannustaa harkitsemaan, onko muuttuvuus todella tarpeen kullekin muuttujalle.


Rust tukee myös varjostusta, jonka avulla voit ilmoittaa uuden muuttujan samalla nimellä kuin edellisen muuttujan. Toisin kuin mutaatio, varjostaminen luo täysin uuden muuttujan, jolla sattuu olemaan sama nimi, jolloin edellinen muuttuja piilotetaan. Tämä tekniikka on erityisen hyödyllinen, kun tietoja muunnetaan useiden vaiheiden kautta, esimerkiksi kun merkkijono jäsennetään numeroksi ja sitten käsitellään tätä numeroa edelleen. Varjostuksen avulla voit säilyttää muuttujan nimen johdonmukaisena koko muunnosprosessin ajan ja muuttaa muuttujan tyyppiä jokaisessa vaiheessa.


Varjostuksen ja mutaation erottaminen toisistaan on tärkeää, kun tarkastellaan tyyppimuutoksia. Varjostuksessa voit muuttaa sekä muuttujan arvoa että tyyppiä, koska luot uuden muuttujan. Mutaatiossa voit muuttaa vain muuttujan arvoa ja säilyttää samalla muuttujan tyypin, koska muokkaat olemassa olevaa muuttujaa etkä luo uutta muuttujaa.


```rust
// Shadowing: creating new variables with the same name
let amount = "100000";           // amount is a &str (string slice)
let amount = amount.parse::<u64>().unwrap();  // amount is now u64
let amount = amount * 100;       // amount is still u64, new value

// Mutation: modifying the same variable
let mut balance = 50000_u64;
balance = balance + amount;      // OK: same type, different value
// balance = "empty";            // ERROR: cannot change type with mutation

// Practical example: processing a Bitcoin amount input
let user_input = "  0.001 ";                    // &str with whitespace
let user_input = user_input.trim();            // &str, whitespace removed
let satoshis: u64 = (user_input.parse::<f64>().unwrap() * 100_000_000.0) as u64;
println!("Amount in satoshis: {}", satoshis);  // 100000
```


### Tietotyypit ja tyyppijärjestelmän perusteet


Rust toteuttaa vahvan, staattisen tyyppijärjestelmän, jossa jokaisella arvolla on oltava hyvin määritelty tyyppi, joka tunnetaan kääntämisaikana. Vaikka tämä saattaa tuntua rajoittavalta verrattuna dynaamisesti tyypitettyihin kieliin, Rust:n tyypin päättelyominaisuudet tarkoittavat, että tyyppejä tarvitsee harvoin määritellä eksplisiittisesti. Kääntäjä voi yleensä määrittää sopivan tyypin sen perusteella, miten arvoa käytetään.


Tietyissä tilanteissa tarvitaan kuitenkin nimenomaisia tyyppimerkintöjä. Kun käytetään yleisiä funktioita, kuten `parse()`, jotka voivat muuntaa merkkijonoja erilaisiksi numeerisiksi tyypeiksi, kääntäjän on tiedettävä, minkä tyypin haluat. Näissä tapauksissa annat tyyppimerkinnät kaksoispiste-syntaksilla: arvaa: u32 = "42".parse().expect("Ei ole luku!")`.


Rust:n skalaarityyppeihin kuuluvat kokonaisluvut, liukuluvut, booleanit ja merkit. Kokonaislukutyyppijärjestelmä tarjoaa tarkan kontrollin muistin käytön ja suorituskykyominaisuuksien suhteen. Kokonaislukutyypit nimetään systemaattisesti: `i8`, `i16`, `i32`, `i64` ja `i128` merkityille kokonaisluvuille ja `u8`, `u16`, `u32`, `u64` ja `u128` merkitsemättömille kokonaisluvuille. Numerot ilmaisevat bitin leveyden, jolloin muistin käyttö ja arvoalueet ovat heti selvillä.


Erityistä huomiota on kiinnitettävä `isize`- ja `usize`-tyyppeihin, sillä ne mukautuvat kohdearkkitehtuuriin. 64-bittisissä järjestelmissä nämä tyypit ovat 64 bitin levyisiä, kun taas 32-bittisissä järjestelmissä ne ovat 32 bitin levyisiä. Näitä tyyppejä käytetään yleisesti array-indeksointiin ja muistin offsetteihin, koska ne vastaavat kohdearkkitehtuurin luonnollista sanakokoa ja mahdollistavat tehokkaan osoitinaritmetiikan ja muistitoiminnot.


Rust tarjoaa useita tapoja kirjoittaa kokonaislukuja, mukaan lukien desimaali-, heksadesimaali- (`0x`), oktaali- (`0o`) ja binääriformaatit (`0b`). Voit myös käyttää alaviivoja missä tahansa numeerisissa literaaleissa luettavuuden parantamiseksi, kuten kirjoittamalla `1_000_000` `1000000`:n sijasta. Alleviivauksilla ei ole vaikutusta arvoon, mutta ne voivat tehdä suurista luvuista luettavampia.


Rust:n liukulukutyypit ovat suoraviivaisia: `f32` yksinkertaisille tarkkuusluvuille ja `f64` kaksoistarkkuuden liukuluvuille. `f64`-tyyppiä suositaan yleensä sen suuremman tarkkuuden ja sen vuoksi, että nykyaikaiset prosessorit pystyvät usein käsittelemään 64-bittisiä liukulukuoperaatioita yhtä tehokkaasti kuin 32-bittisiä operaatioita.


### Yhdistelmätyypit ja tietojen organisointi


Rust tarjoaa skalaarityyppien lisäksi yhdistelmätyyppejä, jotka ryhmittelevät useita arvoja yhteen. Tuplien avulla voit yhdistää eri tyyppisiä arvoja yhdeksi yhdistelmäarvoksi. Tuplet luodaan käyttämällä sulkuja ja voit määrittää kunkin elementin tyypin: `let tup: (i32, f64, u8) = (500, 6.4, 1)`.


Tuplet tukevat jäsentelyä, jonka avulla voit poimia yksittäisiä arvoja: `let (x, y, z) = tup`. Tämä syntaksi luo kolme erillistä muuttujaa tuplen osista. Vaihtoehtoisesti voit käyttää tuplen elementtejä suoraan käyttämällä pisteen merkintää elementin indeksin kanssa: `tup.0`, `tup.1`, `tup.2`.


```rust
// Creating a tuple with different types
let transaction: (&str, u64, bool) = ("abc123", 50000, true);

// Destructuring: extract all values at once
let (txid, amount, confirmed) = transaction;
println!("Transaction {} for {} sats", txid, amount);

// Dot notation: access individual elements by index
println!("Confirmed: {}", transaction.2);  // true

// Practical example: function returning multiple values
fn parse_utxo(data: &str) -> (String, u32, u64) {
// Returns (txid, output_index, value_in_sats)
("a]1b2c3".to_string(), 0, 100000)
}

let (txid, vout, value) = parse_utxo("raw_data");
println!("UTXO {}:{} = {} sats", txid, vout, value);
```


Rust:n joukot eroavat merkittävästi monien muiden kielten joukoista tai listoista, koska niillä on kiinteä koko, josta tulee osa niiden tyyppiä. Viiden kokonaisluvun joukko on tyyppiä `[i32; 5]`, jossa puolipiste erottaa elementin tyypin ja joukon pituuden toisistaan. Tämän tyyppitason kokotiedon avulla kääntäjä voi suorittaa rajojen tarkistuksen ja varmistaa, että funktiot, jotka vastaanottavat matriiseja, tietävät tarkalleen, kuinka monta elementtiä on odotettavissa.


Voit alustaa matriisit listaamalla kaikki elementit nimenomaisesti: `[1, 2, 3, 4, 5]`, tai käyttämällä lyhennettyä syntaksia toistuvia arvoja sisältäville matriiseille: `[3; 5]` luo viidestä elementistä koostuvan joukon, jossa kaikilla on arvo 3. Tämä lyhennelmä on hyödyllinen puskureiden alustamisessa tai oletusarvoilla varustettujen matriisien luomisessa.


Array-käytössä käytetään hakasulkujen merkintää kuten useimmissa kielissä, mutta Rust tarjoaa sekä käännös- että suoritusaikaista rajojen tarkistusta. Kun käytät arraya vakioindeksillä, jonka kääntäjä voi tarkistaa, se havaitsee rajoja ylittävän käytön kääntämisaikana. Suoritusajassa määritettävien dynaamisten indeksien osalta Rust lisää rajatarkistukset, jotka aiheuttavat ohjelman paniikin, jos yrität käyttää virheellistä indeksiä, ja estävät näin muistiturvallisuusrikkomukset.



## Ownership ja Rust:n muistiturvallisuus

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>


:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::


### Rust:n ainutlaatuisen lähestymistavan ymmärtäminen muistinhallintaan


Tässä luvussa käsitellään yhtä Rust:n tärkeimmistä käsitteistä. Vaikka aiemmat käsitteet ovat saattaneet tuntua tutuilta muista kielistä tuleville ohjelmoijille, omistajuus on Rust:n lähestymistapa muistiturvallisuuden ratkaisemiseen ilman roskienkeruuta.


Rust:n perustavoitteena oli estää muistiin liittyvät virheet, jotka vaivaavat matalan tason kieliä, kuten C ja C++. Tällaisia ongelmia ovat esimerkiksi use-after-free-virheet, joissa muistia käytetään sen jälkeen, kun se on vapautettu, ja puskurin ylivuodot, joissa ohjelmat kirjoittavat osoitetun muistin rajojen ulkopuolelle. Perinteiset ratkaisut näihin ongelmiin ovat sisältäneet kompromisseja, jotka Rust pyrkii poistamaan. Korkeamman tason kielet, kuten Java ja Go, ratkaisevat muistin turvallisuuden roskienkeräyksellä, jossa automaattinen prosessi tunnistaa ja vapauttaa käyttämättömän muistin määräajoin. Roskienkerääjät aiheuttavat kuitenkin suorituskyvyn yleiskustannuksia ja voivat aiheuttaa arvaamattomia taukoja ohjelman suorituksen aikana, minkä vuoksi ne eivät sovellu järjestelmäohjelmointiin, jossa tasainen suorituskyky on kriittinen.


Rust saavuttaa muistiturvallisuuden ensisijaisesti staattisella analyysillä, joka suoritetaan kääntämisaikana. Kääntäjä tutkii lähdekoodin ja voi määrittää, ovatko useimmat muistitoiminnot turvallisia ilman roskienkeruuta. Tapauksiin, joita ei voida todentaa staattisesti - kuten joukkojen käyttö ajonaikaisesti lasketuilla indekseillä - Rust lisää rajatarkistuksia, jotka pikemminkin panikoivat kuin sallivat määrittelemättömän käyttäytymisen. Tämä lähestymistapa eroaa olennaisesti C:lle ja C++:lle saatavilla olevista staattisista analysaattoreista, jotka asennettiin jälkikäteen kieliin, joita ei alun perin suunniteltu kattavaa staattista analyysiä varten. Rust:n syntaksi ja kielisäännöt laadittiin alusta alkaen niin, että ne mahdollistavat laajan kääntämisen aikaisen tarkistuksen, jolla varmistetaan, että kun ohjelma on käännetty onnistuneesti, se joko toimii turvallisesti tai paniikissa ennakoitavasti eikä osoita määrittelemätöntä käyttäytymistä.


### Ownership-järjestelmä: Ownership: Säännöt ja periaatteet


Rust:n muistiturvallisuustakuiden kulmakivi on omistusjärjestelmä, joka säätelee muistinhallintaa ohjelman koko suorituksen ajan. Ownership:n toiminta perustuu kolmeen perussääntöön, joita kääntäjä noudattaa koko ajan:


1. Jokaisella Rust:n arvolla on omistaja (muuttuja, joka pitää arvoa)

2. Omistajia voi olla vain yksi kerrallaan

3. Kun omistaja poistuu soveltamisalan ulkopuolelle, arvo poistetaan


Rust:ssa laajuudet määritellään tyypillisesti sulkeissa, olipa kyse sitten funktiorungoista, ehdollisista lohkoista tai nimenomaisesti luoduista laajuuslohkoista. Kun muuttuja ilmoitetaan laajuuden sisällä, kyseisestä laajuudesta tulee muuttujan arvon omistaja. Muuttuja pysyy käytettävissä ja voimassa koko scope-alueen elinkaaren ajan, mutta heti kun suoritus poistuu scope-alueelta, kaikki omistetut muuttujat siivotaan automaattisesti prosessin nimeltä dropping avulla.


Tämä automaattinen siivous on toteutettu Rust:n pudotusmekanismilla, jossa kieli kutsuu epäsuorasti pudotusfunktiota, kun muuttuja poistuu toimialueeltaan. Perustyyppien osalta tämä tarkoittaa yksinkertaisesti sitä, että muisti merkitään uudelleen käytettäväksi. Monimutkaisemmissa resursseja hallinnoivissa tyypeissä mukautetut drop-toteutukset voivat suorittaa muita siivoustoimintoja, kuten tiedostokahvojen sulkemisen tai verkkoyhteyksien vapauttamisen. Tämä C++:n RAII:sta (Resource Acquisition Is Initialization) lainattu malli varmistaa, että resurssit vapautetaan aina asianmukaisesti ilman, että ohjelmoijalta vaaditaan nimenomaista siivouskoodia.


### Ownership:n siirtäminen ja muistin asettelu


Sen ymmärtäminen, miten omistusoikeus siirtyy muuttujien välillä, edellyttää yksinkertaisten ja monimutkaisten tyyppien eron tutkimista muistin asettelun ja kopiointikäyttäytymisen kannalta. Yksinkertaisilla tyypeillä, kuten kokonaisluvuilla, booleanseilla ja liukuluvuilla, on kiinteä, tunnettu koko kääntämishetkellä, ja niitä voidaan kopioida tehokkaasti. Kun osoitat yhden kokonaislukumuuttujan toiselle, Rust luo täydellisen, riippumattoman kopion arvosta, jolloin molemmat muuttujat voivat olla olemassa samanaikaisesti ilman omistusoikeuteen liittyviä ongelmia.


Monimutkaiset tyypit, kuten merkkijonot, ovat erilainen haaste, koska ne hallitsevat dynaamisesti varattua muistia. Rust:n merkkijono koostuu kolmesta pinoon tallennetusta komponentista: osoitin kasaan varattuun merkkidataan, merkkijonon nykyinen pituus ja varattuun puskuriin varattu kokonaiskapasiteetti. Tämän rakenteen ansiosta merkkijonot voivat kasvaa ja kutistua tehokkaasti säilyttäen samalla tiedon niiden rajoista. Kun osoitat yhden merkkijonomuuttujan toiselle, Rust:n on valittava: se voi kopioida vain pinoon perustuvan rakenteen (jolloin se luo kaksi osoitinta samaan kasan dataan) tai suorittaa koko kasan datan syväkopioinnin.


Rust:n oletuskäyttäytyminen on omistusoikeuden siirtäminen kopioinnin sijaan, jolloin kasan tiedot siirretään lähdemuuttujasta kohdemuuttujaan ja lähde mitätöidään. Tämä lähestymistapa estää vaarallisen skenaarion, jossa useat muuttujat voivat muokata samaa kasan muistia tai jossa sama muisti voidaan vapauttaa useita kertoja, kun muuttujat poistuvat soveltamisalan ulkopuolelle. Siirto-operaatio on tehokas, koska se kopioi vain pienen pinopohjaisen rakenteen, ei mahdollisesti suurta kasan dataa, ja säilyttää samalla muistiturvallisuuden varmistamalla yhden omistajan.


### Viitteet ja lainaaminen


Vaikka omistusoikeussiirrot tarjoavat turvallisuutta, ne voivat olla rajoittavia, kun arvoa on käytettävä useissa paikoissa ilman omistusoikeuden siirtoa. Rust ratkaisee tämän ongelman lainaamalla, jolloin funktiot ja muuttujat voivat käyttää tietoja väliaikaisesti ilman omistusoikeuden siirtoa. Viittaus, joka luodaan ampersand-operaattorilla, antaa vain lukuoikeuden arvoon, mutta jättää omistusoikeuden alkuperäiselle muuttujalle.


Viittausten avulla funktiot voivat toimia datan kanssa kuluttamatta sitä, jolloin samaa arvoa voidaan käyttää useaan kertaan ohjelmassa. Kun annat viitteen funktiolle, lainaat datan väliaikaisesti, ja funktion on palautettava viite, ennen kuin alkuperäinen omistaja voi saada täyden hallinnan takaisin. Tämä lainaamisen metafora kuvastaa käyttöoikeuden väliaikaista luonnetta: aivan kuten lainaat kirjan ystävällesi säilyttäen samalla omistusoikeuden, viittaukset mahdollistavat väliaikaisen käyttöoikeuden säilyttäen samalla alkuperäisen omistussuhteen.


Muuttuvat viittaukset laajentavat tätä konseptia siten, että lainattua tietoa voidaan muuttaa, mutta tiukkojen rajoitusten avulla, jotta turvallisuus säilyy. Rust sallii vain yhden muuttuvan viittauksen tietoon kerrallaan, mikä estää datakilpailut, joissa useat ohjelman osat voivat samanaikaisesti muokata samaa muistia. Lisäksi samaan dataan ei voi olla samanaikaisesti sekä muuttuvia että muuttumattomia viittauksia, koska tämä voi johtaa tilanteisiin, joissa koodi olettaa datan olevan vakaa, kun toinen koodi muuttaa sitä aktiivisesti. Nämä säännöt pannaan täytäntöön kääntämisen yhteydessä, mikä eliminoi kokonaisia luokkia rinnakkaisvirheitä, jotka vaivaavat muita järjestelmäohjelmointikieliä.


```rust
fn main() {
let mut wallet_balance: u64 = 100_000; // 100,000 satoshis

// Immutable borrow: read the balance
let balance_ref = &wallet_balance;
println!("Current balance: {} sats", balance_ref);
// balance_ref goes out of scope here

// Mutable borrow: update the balance
let balance_mut = &mut wallet_balance;
*balance_mut += 50_000; // Receive payment
println!("After deposit: {} sats", balance_mut);
// balance_mut goes out of scope here

// Function that borrows immutably
fn display_balance(balance: &u64) {
println!("Balance check: {} sats", balance);
}

// Function that borrows mutably
fn deduct_fee(balance: &mut u64, fee: u64) {
*balance -= fee;
}

display_balance(&wallet_balance);
deduct_fee(&mut wallet_balance, 1_000);
println!("After fee: {} sats", wallet_balance); // 149,000
}
```


### Merkkijonotyypit ja viipaleet


Rust:ssä erotetaan toisistaan merkkijonokirjaimet ja String-tyyppi, mikä heijastaa erilaisia muistinhallintastrategioita ja käyttötapauksia. String-litteraalit on upotettu suoraan käännettyyn binääritiedostoon, ja niiden tyyppi on &str (string slice), joka edustaa näkymää muuttumattomaan string-tietoon. Nämä litteraalit ovat tehokkaita, koska ne eivät vaadi suoritusaikaista allokointia, mutta niitä ei voi muuttaa, koska ne ovat osa ohjelman koodia.


String-tyyppi sen sijaan hallinnoi dynaamisesti varattua muistia, ja se voi kasvaa, kutistua ja muuttua ajon aikana. Voit luoda merkkijonon literaalista String::from():lla tai vastaavilla metodeilla, jotka varaavat kasan muistia ja kopioivat literaalin sisällön. Tämän eron ansiosta Rust optimoi sekä suorituskykyä (käyttämällä literaaleja, kun se on mahdollista) että joustavuutta (käyttämällä Stringiä, kun muokkausta tarvitaan).


Merkkijonoviipaleet (&str) tarjoavat tehokkaan abstraktion merkkijonojen osien käsittelyyn kopioimatta tietoja. Viipale sisältää osoittimen merkkijonodatan alkuun ja pituuden, jolloin voit viitata osajonoihin tehokkaasti. Slice-syntaksissa käytetään alueita (esim. &s[0..5]) sen määrittämiseksi, mihin merkkijonon osaan viitataan. Koska viipaleet ovat viittauksia, niihin sovelletaan lainaussääntöjä, jotka estävät taustalla olevan merkkijonon muuttamisen viipaleiden olemassaolon aikana. Tämä kääntämisen aikainen valvonta estää yleiset virheet, kuten pääsyn epäkelvoon muistiin sen jälkeen, kun alkuperäinen merkkijono on vapautettu tai sitä on muutettu.


### Asettelut, vektorit ja yleiset viipaleet (Generic Slices)


Slice-käsite ulottuu merkkijonojen lisäksi mihin tahansa elementtisarjaan, mikä tarjoaa yhtenäisen tavan työskennellä sekä kiinteän kokoisten matriisien että dynaamisten vektorien kanssa. Rust:n monisteiden pituus on koodattu niiden tyyppiin (esim. [i32; 5] viidestä 32-bittisestä kokonaisluvusta koostuvalle monisteelle), mikä tekee niistä sopivia tilanteisiin, joissa tarvitaan kokotakuita kääntämisaikana. Joukkoja hyväksyvät funktiot voivat asettaa täsmällisiä pituusvaatimuksia, mikä on hyödyllistä esimerkiksi salausfunktioissa, jotka tarvitsevat tarkan kokoisia syötteitä.


Viipaleet (&[T]) tarjoavat joustavamman vaihtoehdon, joka edustaa näkymää mihin tahansa elementtien peräkkäiseen sarjaan riippumatta taustalla olevasta tallennuksesta. Voit luoda viipaleita matriiseista, vektoreista tai muista viipaleista, ja sama viipale voi viitata eri dataosuuksiin koko elinkaarensa ajan. Tämä joustavuus tekee viipaleista ihanteellisia funktioille, joiden on käsiteltävä sekvenssejä välittämättä erityisestä tallennusmekanismista tai tarkasta koosta.


Omistettujen tyyppien (String, Vec<T>) ja niiden lainattujen viipaletyyppien (&str, &[T]) välinen suhde noudattaa johdonmukaista kaavaa koko Rust:ssa. Omistetut tyypit hallinnoivat muistiaan ja niitä voidaan muokata, kun taas viipaleet tarjoavat tehokkaan, vain lukukäyttöön tarkoitetun pääsyn datan osiin. Tämä rakenne mahdollistaa API:t, jotka ovat sekä joustavia (hyväksyvät erilaisia syöttötyyppejä viipaleiden avulla) että tehokkaita (välttävät tarpeetonta kopiointia), mutta säilyttävät samalla Rust:n turvatakuut lainausjärjestelmän avulla.



## Rakenteet, monimutkaisten tietotyyppien rakentaminen

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>


:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::

Rust:n rakenteet toimivat perustana monimutkaisten tietotyyppien luomiselle, kuten luokat muissa ohjelmointikielissä. Niiden avulla voit ryhmitellä toisiinsa liittyviä tietoja yhdeksi yhtenäiseksi kokonaisuudeksi, joka voi sisältää useita erityyppisiä kenttiä. Rakenteen määrittelyn syntaksi noudattaa suoraviivaista kaavaa: käytät `struct`-avainsanaa, jota seuraa rakenteen nimi, ja määrittelet sitten kentät sulkeiden sisällä kaksoispisteen syntaksia käyttäen kunkin kentän tyypin määrittämiseksi.


Rust noudattaa erityisiä rakenteiden nimeämiskäytäntöjä, joita kääntäjä valvoo varoitusten avulla. Rakenteiden nimissä on käytettävä CamelCase-kirjainta (tunnetaan myös nimellä PascalCase), kun taas rakenteen sisällä olevien kenttien nimissä on käytettävä snake_case-kirjainta ja alleviivauksia. Tämä konventio auttaa säilyttämään johdonmukaisuuden Rust:n koodikannoissa ja tekee koodista luettavampaa muille kehittäjille.


Rakenteiden instanssien luominen edellyttää, että määrität kaikkien kenttien arvot käyttämällä rakenteen nimeä, jota seuraavat kenttien määritykset sisältävät suljetut aaltosulkeet. Kun sinulla on rakenteen instanssi, voit käyttää ja muokata yksittäisiä kenttiä pisteen merkintätapaa käyttäen, jos instanssi on ilmoitettu muuttuvaksi. Tämä pisteen merkintätapa toimii johdonmukaisesti Rust:ssa, toisin kuin C++:n kaltaisissa kielissä, joissa saatetaan käyttää eri operaattoreita osoittimille ja suorille objekteille.


### Konstruktoritoiminnot ja kenttien pikakuvakkeet


Rust:ssä ei ole sisäänrakennettuja konstruktoreita, kuten joissakin oliokeskeisissä kielissä, mutta voit luoda funktioita, jotka palauttavat rakenteet samaan tarkoitukseen. Nämä konstruktorifunktiot ottavat tyypillisesti parametreja joillekin tai kaikille kentille ja voivat asettaa oletusarvoja muille kentille. Tällaisia funktioita kirjoitettaessa Rust tarjoaa kätevän lyhennelmän: jos parametrilla on sama nimi kuin rakenteen kentällä, voit kirjoittaa kentän nimen vain kerran sen sijaan, että toistaisit sen muodossa `kenttä: arvo`.


Rakenneinstansseja voidaan luoda myös kopioimalla arvoja olemassa olevista instansseista käyttämällä struct update -syntaksia. Tämän ominaisuuden avulla voit luoda uuden instanssin ja määrittää vain ne kentät, joita haluat muuttaa, ja kopioida kaikki muut kentät olemassa olevasta instanssista. Tämä operaatio noudattaa kuitenkin Rust:n omistussääntöjä, mikä tarkoittaa, että muut kuin kopiointityypit siirretään lähdeinstanssista, jolloin alkuperäisen instanssin osat saattavat olla myöhemmin käyttökelvottomia. Kääntäjä seuraa näitä osittaisia siirtoja älykkäästi, jolloin voit jatkaa niiden kenttien käyttöä, joita ei siirretty, mutta estää samalla pääsyn siirrettyihin kenttiin.


### Tuplurakenteet ja yksikkörakenteet


Rust tukee tuple-rakenteita, jotka ovat rakenteita, joissa on nimeämättömiä kenttiä, joita käytetään indeksin eikä nimen perusteella. Nämä ovat hyödyllisiä yksinkertaisissa kääretyypeissä tai silloin, kun tarvitset rakenteen, mutta et tarvitse nimettyjä kenttiä. Tuplarakenteen kenttiin pääsee käsiksi käyttämällä pisteen merkintää, jota seuraa kentän indeksi, esimerkiksi `.0` ensimmäiselle kentälle, `.1` toiselle kentälle ja niin edelleen. Tämä lähestymistapa toimii hyvin rakenteissa, jotka sisältävät vain yhden arvon tai vain muutaman läheisesti toisiinsa liittyvän arvon, jolloin nimet saattavat olla tarpeettomia.


Yksikkörakenteet ovat rakenteiden yksinkertaisin muoto - ne eivät sisällä lainkaan dataa. Vaikka tämä saattaa aluksi tuntua turhalta, yksikkörakenteista tulee arvokkaita, kun työskennellään Rust:n ominaisuusjärjestelmän kanssa, sillä niillä voidaan toteuttaa käyttäytymistä tallentamatta mitään tietoja. Näitä tyhjiä rakenteita käytetään merkkeinä tai sijoituspaikkoina edistyneemmissä Rust-malleissa.


### Menetelmät ja niihin liittyvät toiminnot


Rakenteet saavat lisätoiminnallisuutta, kun lisäät käyttäytymistä toteutuslohkojen avulla. Käyttämällä `impl`-avainsanaa, jota seuraa rakenteen nimi, voit määritellä metodeja, jotka toimivat rakenteesi instansseilla. Metodit ovat funktioita, jotka ottavat ensimmäisenä parametrinaan `self`, joka voi olla omistettu arvo (`self`), muuttumaton viittaus (`&self`) tai muuttuva viittaus (`&mut self`) riippuen siitä, mitä metodin täytyy tehdä instanssille.


Parametrityypin `self` valinta määrittää metodin käyttäytymisen omistajuuden suhteen. Metodit, jotka käyttävät `&self`-parametrityyppiä, voivat lukea instanssista ilman omistusoikeutta, joten ne soveltuvat operaatioihin, jotka eivät muuta rakennetta. Metodit, jotka ottavat `&mut self`, voivat muokata instanssia, mutta antavat silti kutsujan säilyttää omistusoikeuden. Metodit, jotka ottavat `self`-arvon, kuluttavat instanssin, mikä sopii operaatioihin, jotka muuttavat rakenteen joksikin muuksi, tai kun metodi on viimeinen operaatio kyseiselle instanssille.


Liitännäisfunktiot ovat funktioita, jotka on määritelty toteutuslohkossa ja jotka eivät ota `self`:iä parametrina. Ne ovat samanlaisia kuin muiden kielten staattiset metodit, ja niitä käytetään yleisesti konstruktoreina tai tyyppiin liittyvinä aputoimintoina. Liitännäisfunktioita kutsutaan kaksoispisteen syntaksilla (`Type::function_name()`), mikä erottaa ne selvästi metodeista, joita kutsutaan instansseille.


```rust
// Define a struct for a Lightning invoice
struct Invoice {
payment_hash: String,
amount_msat: u64,
description: String,
expiry_secs: u32,
}

impl Invoice {
// Associated function (constructor) - no self parameter
fn new(payment_hash: String, amount_msat: u64, description: String) -> Self {
Invoice {
payment_hash,
amount_msat,
description,
expiry_secs: 3600, // default 1 hour
}
}

// Method with &self - read-only access
fn amount_sats(&self) -> u64 {
self.amount_msat / 1000
}

// Method with &mut self - can modify the instance
fn extend_expiry(&mut self, additional_secs: u32) {
self.expiry_secs += additional_secs;
}

// Method with self - consumes the instance
fn into_payment_request(self) -> String {
format!("lnbc{}n1p{}", self.amount_msat, self.payment_hash)
}
}

fn main() {
// Use associated function to create instance
let mut invoice = Invoice::new(
"abc123".to_string(),
100_000_000, // 100,000 sats in millisats
"Coffee payment".to_string(),
);

println!("Amount: {} sats", invoice.amount_sats());
invoice.extend_expiry(1800); // Add 30 minutes

let request = invoice.into_payment_request();
// invoice is now consumed, cannot be used anymore
println!("Payment request: {}", request);
}
```


#### Luettelot: Valintojen ja vaihtoehtojen mallintaminen


Rust:n luettelemilla on enemmän mahdollisuuksia kuin monien muiden kielten luettelemilla. Vaikka ne voivat edustaa yksinkertaisia nimettyjen vakioiden joukkoja, Rust-luettelot voivat myös sisältää dataa kunkin muunnoksen sisällä, joten ne soveltuvat sellaisten tilanteiden mallintamiseen, joissa arvo voi olla yksi useista eri tyypeistä tai tiloista. Kukin enum-muunnos voi sisältää erityyppistä ja -määräistä dataa, ei lainkaan dataa tai monimutkaisia rakenteita, joissa on nimettyjä kenttiä.


Mahdollisuus liittää tietoja enum-muunnoksiin poistaa monia muissa kielissä esiintyviä yleisiä ohjelmointivirheitä. Sen sijaan, että ylläpidettäisiin erillisiä muuttujia tyyppi-indikaattorille ja siihen liittyville tiedoille - jotka voivat helposti muuttua epäjohdonmukaisiksi - Rust:n enumit niputtavat tyyppitiedot itse tietoihin. Tämä rakenne varmistaa, että tiedot vastaavat aina muunnelmaa, mikä estää virheet, jotka voivat johtaa suoritusaikaisiin virheisiin.


Enum-muunnokset voivat sisältää dataa useissa eri muodoissa: ei dataa yksinkertaisten lippujen osalta, tuple-tyyppistä dataa nimeämättömien kenttien osalta tai struct-tyyppistä dataa nimettyjen kenttien kanssa. Voit jopa sekoittaa näitä tyylejä yhden enumin sisällä valitsemalla kullekin muunnokselle sopivimman muodon. Tämä joustavuus tekee enumeista sopivia monimutkaisten toimialueen käsitteiden mallintamiseen, kun eri tapaukset vaativat erilaista tietoa.


#### Vaihtoehtotyyppi: Poissaolojen turvallinen käsittely


Yksi Rust:n tärkeimmistä enumeista on `Option<T>`, joka edustaa arvoja, joita voi olla tai ei voi olla. Tällä enumilla on kaksi vaihtoehtoa: `Some(T)`, joka sisältää T-tyyppisen arvon, ja `None`, joka edustaa arvon puuttumista. Option-tyyppi toimii Rust:n ratkaisuna nollaosoitinongelmiin, jotka vaivaavat monia muita kieliä, pakottaen kehittäjät käsittelemään eksplisiittisesti tapauksia, joissa arvot saattavat puuttua.


Vaihtoehtotyyppien käyttäminen tekee koodistasi kestävämpää, koska kääntäjä vaatii sinua käsittelemään sekä arvojen olemassaoloa että niiden puuttumista. Et voi vahingossa käyttää mahdollisesti puuttuvaa arvoa tarkistamatta ensin, onko se olemassa. Tämä nimenomainen käsittely estää nollaosoitinpoikkeukset ja vastaavat ajonaikaiset virheet, jotka ovat yleisiä vikojen lähteitä muissa ohjelmointikielissä.


Vaihtoehtotyyppi integroituu Rust:n hahmontäsmäytysjärjestelmään, jolloin voit käsitellä molempia tapauksia. Metodit kuten `unwrap_or()` tarjoavat käteviä tapoja poimia arvoja, joilla on varasuunnitelmat, kun taas metodit kuten `map()` ja `and_then()` mahdollistavat funktionaalisen ohjelmoinnin mallit valinnaisten arvojen kanssa työskentelyyn.


### Kuvion täsmäytys Match-lausekkeilla


Hahmontäsmäytys `match`-lausekkeiden avulla tarjoaa tavan työskennellä enumien ja muiden tietotyyppien kanssa. Match-lauseke tutkii arvoa ja suorittaa eri koodia sen mukaan, mitä mallia arvo vastaa. Kukin kuvio voi jäsentää sovitetun arvon ja sitoa sen osia muuttujiin, joita voidaan käyttää vastaavassa koodilohkossa.


Täsmäyslausekkeiden on oltava tyhjentäviä, eli niiden on käsiteltävä kaikki mahdolliset täsmäytettävän tyypin tapaukset. Tämä vaatimus estää virheet, joita voisi syntyä, jos tietyt tapaukset jätettäisiin vahingossa käsittelemättä. Kun et halua käsitellä jokaista tapausta eksplisiittisesti, voit käyttää jokerimerkkikuviota (`_`) nappaamaan kaikki jäljellä olevat tapaukset tai sitoa käsittelemättömät tapaukset muuttujaan, jos tarvitset pääsyn arvoon.


Konstruktio `if let` tarjoaa tiiviimmän vaihtoehdon matchille, kun olet kiinnostunut vain yhdestä tietystä kuviosta. Tämä syntaksi on erityisen hyödyllinen, kun työskennellään Option-tyyppien kanssa tai kun halutaan suorittaa koodia vain, jos arvo vastaa tiettyä enum-muunnosta. Konstruktioon `if let` voidaan sisällyttää `else`-lauseke niitä tapauksia varten, joissa kuvio ei täsmää, mikä tekee siitä virtaviivaisen tavan käsitellä yksinkertaisia kuvion täsmäytysskenaarioita.


#### Kokoelmat: Tietoryhmien hallinta


Rust:n standardikirjasto tarjoaa useita kokoelmatyyppejä toisiinsa liittyvien tietoryhmien hallintaan. Nämä kokoelmat ovat yleisiä, eli niihin voidaan tallentaa minkä tahansa tyyppisiä elementtejä, ja ne hoitavat muistinhallinnan automaattisesti. Yleisimmin käytetyt kokoelmat ovat vektorit järjestettyjä luetteloita varten, hash maps avain-arvoassosiaatioita varten ja merkkijonot tekstidataa varten.


#### Vektorit: Dynamic Arrays


Vektorit edustavat kasvavia matriiseja, joiden koko voi muuttua ohjelman suorituksen aikana. Toisin kuin kiinteäkokoiset matriisit, vektorit varaavat muistia kasasta ja voivat laajentaa tai pienentää sitä tarpeen mukaan. Vektorin luominen vaatii usein nimenomaista tyyppimerkintää, kun aloitetaan tyhjällä vektorilla, koska kääntäjän on tiedettävä, minkä tyyppisiä elementtejä vektori tulee sisältämään.


Vektorit tarjoavat useita tapoja käyttää elementtejä, joilla kullakin on erilaiset turvallisuusominaisuudet. Indeksimerkintä (`vec[0]`) tarjoaa suoran pääsyn, mutta aiheuttaa paniikin, jos indeksi on rajojen ulkopuolella. Metodi `get()` palauttaa `Option`, jonka avulla voit käsitellä rajojen ulkopuolista pääsyä tyylikkäästi. Valinta näiden lähestymistapojen välillä riippuu siitä, voitko taata, että indeksi on kelvollinen, vai tarvitseeko sinun käsitellä mahdollisia virheitä.


Rust:n lainaussääntöjä sovelletaan vektoreihin, mikä estää yleiset muistiturvallisuusongelmat. Jos sinulla on viittaus vektorin elementtiin, et voi muuttaa vektoria ennen kuin viittaus poistuu soveltamisalan ulkopuolelle. Tämä estää tilanteet, joissa viittaukset saattavat osoittaa vapautuneeseen muistiin vektorin operaatioiden, kuten uusien elementtien lisäämisen tai vektorin tyhjentämisen, jälkeen.


#### Hash-kartat: Avainarvojen tallennus


Hash-kartat tarjoavat tehokkaan avain-arvosäilytyksen, josta voit nopeasti hakea arvoja niihin liittyvien avainten perusteella. Sekä avaimet että arvot voivat olla minkä tahansa tyyppisiä, mutta avainten on kuitenkin toteutettava tarvittavat ominaisuudet hashtausta ja tasa-arvovertailua varten. Hash-kartat ottavat omistusoikeuden lisättyihin arvoihin, elleivät arvot toteuta Copy-ominaisuutta.


Hash-kartat tarjoavat useita menetelmiä arvojen lisäämiseen ja päivittämiseen. Perusmenetelmä `insert()` korvaa olemassa olevat arvot, kun taas `entry()` tarjoaa joustavamman lisäyslogiikan. API:n entry-metodin avulla voit lisätä arvoja vain, jos niitä ei ole vielä olemassa, tai päivittää olemassa olevia arvoja niiden nykyisen tilan perusteella. Tämä API on käyttökelpoinen esimerkiksi esiintymien laskemisessa tai juoksevien kokonaislukujen ylläpitämisessä.


Kun haetaan arvoja hash-kartoista, metodi `get()` palauttaa `Option`, koska pyydettyä avainta ei välttämättä ole olemassa. Voit käyttää metodeja kuten `copied()` muuntamaan `Option<&T>`:stä `Option<T>`:ksi Copy-tyypeille ja `unwrap_or()` antamaan oletusarvoja, kun avaimia ei ole.


### Merkkijonojen käsittely ja Unicode


Rust:n merkkijonot ovat UTF-8-koodattuja, mikä tarjoaa täyden Unicode-tuen, mutta lisää monimutkaisuutta verrattuna yksinkertaisiin ASCII-merkkijonoihin. `String`-tyyppi edustaa omaa, kasvatettavaa tekstidataa, kun taas merkkijonoviipaleet (`&string`) tarjoavat lainattuja näkymiä merkkijonodataan. Voit muuntaa näiden tyyppien välillä tarpeen mukaan, ja merkkijonoviipaleita käytetään usein funktioiden parametreissa, jotta voidaan hyväksyä sekä omistettuja merkkijonoja että merkkijonojen kirjaimia.


Merkkijonojen käsittely sisältää menetelmiä tekstin liittämiseen, useiden arvojen muotoilemiseen yhdessä ja osajonojen poimimiseen. Metodi `push_str()` liittää merkkijonoviipaleet ilman omistusoikeutta, kun taas makro `format!` tarjoaa joustavan tavan muodostaa merkkijonoja useista komponenteista. Kun työskentelet merkkijonoindeksien kanssa, sinun on oltava varovainen UTF-8-merkkien rajojen noudattamisessa välttyäksesi suoritusaikapaniikilta.


Merkkikohtaista turvallista käsittelyä varten merkkijonot tarjoavat iteraattorimenetelmiä, kuten `chars()` Unicode-skalaariarvoille ja `bytes()` raa'an tavun käytölle. Nämä iteraattorit käsittelevät UTF-8-koodausta oikein, jolloin varmistetaan, ettet vahingossa jaa usean tavun merkkejä. Tämä lähestymistapa on turvallisempi ja luotettavampi kuin manuaalinen indeksointi, erityisesti kun työskennellään kansainvälisen tekstin kanssa, joka saattaa sisältää monimutkaisia Unicode-merkkejä.



## Rust:n kaksiluokkainen virheenkäsittelyjärjestelmä

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>


:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::

Rust:ssä virheenkäsittelyyn sovelletaan täysin erilaista lähestymistapaa kuin useimmissa ohjelmointikielissä. Monissa kielissä turvaudutaan ensisijaisesti poikkeuksiin, mutta Rust:ssä erotetaan kaksi erillistä virhetyyppiä toisistaan ja tarjotaan erityisiä mekanismeja kummankin tyypin käsittelyyn. Tässä luvussa tutustutaan Rust:n kattavaan virheenkäsittelyjärjestelmään, joka kattaa sekä korjaamattomat virheet, jotka keskeyttävät ohjelman suorituksen, että palautettavat virheet, joiden ansiosta ohjelmat voivat jatkaa toimintaansa.


### Korjaamattomat virheet ja paniikki


Korjaamattomat virheet ovat tilanteita, joissa ohjelma on joutunut epäjohdonmukaiseen tai odottamattomaan tilaan, josta se ei voi turvallisesti toipua. Tällaisia tilanteita ovat esimerkiksi rajaton käyttö, muistiturvallisuutta rikkovien operaatioiden yrittäminen tai olosuhteet, jotka viittaavat ohjelmalogiikan perusvirheisiin. Kun tällaisia virheitä ilmenee, asianmukainen reaktio on ohjelman lopettaminen välittömästi sen sijaan, että otettaisiin riski, että ohjelma vahingoittuu tai käyttäytyy määrittelemättömästi.


Rust:ssä korjaamattomat virheet aiheuttavat paniikkitilanteen, joka saa ohjelman kaatumaan hallitusti. Ennen lopettamista Rust suorittaa prosessin nimeltä unwinding, jossa se kävelee takaisin kutsupinon läpi tuottaakseen yksityiskohtaisen pinojäljen, josta näkyy tarkalleen, missä kohtaa paniikki tapahtui. Tämä purkuprosessi auttaa kehittäjiä tunnistamaan ongelman lähteen virheenkorjauksen aikana. Suorituskriittisissä sovelluksissa tai sulautetuissa järjestelmissä voit poistaa purkamisen käytöstä ja määrittää Rust:n keskeyttämään välittömästi paniikin sattuessa, mutta tällöin virheenkorjaustiedot menetetään nopeamman lopettamisen hyväksi.


Voit laukaista paniikin nimenomaisesti käyttämällä `panic!`-makroa ja mukautettua viestiä. Kun paniikki tapahtuu, näet tulosteen, joka kertoo, mikä säie joutui paniikkiin ja siihen liittyvän viestin. Ympäristömuuttujan `RUST_BACKTRACE` asettaminen antaa lisää virheenkorjaustietoa, sillä se näyttää koko kutsupinon, joka johti paniikkiin. Jos esimerkiksi yrität käyttää vain kolme elementtiä sisältävän vektorin elementtiä 99, generate aiheuttaa paniikin ja antaa "index out of bounds" -viestin sekä takautuman, joka näyttää virheeseen johtaneiden funktiokutsujen tarkan järjestyksen.


### Palautettavat virheet ja tulos


Palautettavat virheet edustavat odotettavissa olevia vikatilanteita, jotka ohjelmat voivat käsitellä hienovaraisesti ilman keskeytystä. Esimerkkeinä voidaan mainita yritys avata tiedosto, jota ei ole olemassa, verkkoyhteyden epäonnistuminen tai virheellinen käyttäjän syöttö. Näitä tilanteita varten Rust tarjoaa `Result`-luettelon, joka edustaa nimenomaisesti toimintoja, jotka voivat epäonnistua, ja pakottaa kehittäjät käsittelemään sekä onnistumis- että epäonnistumistapauksia.


`Tulos`-luettelo on määritelty kahdella muunnoksella: `Ok(T)` onnistuneille operaatioille, jotka sisältävät tyypin `T` arvon, ja `Err(E)` epäonnistumisille, jotka sisältävät tyypin `E` virheen. Tässä mallissa käytetään Rust:n tyyppijärjestelmää sen varmistamiseksi, että mahdollisia virheitä ei voida jättää huomiotta. Funktiot, jotka saattavat epäonnistua, palauttavat `Tuloksen`, ja kutsuvan koodin on nimenomaisesti käsiteltävä sekä onnistumis- että virhetapaukset, tyypillisesti käyttämällä mallien täsmäytystä `match`-lausekkeilla.


Tarkastellaan `File::open`-funktiota, joka palauttaa `Tulos<File, std::io::Error>`. Kun avaat tiedoston, saat joko `File`-olion, jos toiminto onnistuu, tai `std::io::Error`-olion, jos toiminto epäonnistuu. Voit verrata tätä tulosta käsittelemään kutakin tapausta asianmukaisesti. Onnistumistapauksessa voit jatkaa tiedosto-operaatioita, kun taas virhetapauksessa voit yrittää luoda tiedoston, kokeilla vaihtoehtoista lähestymistapaa tai välittää virheen kutsuvalle koodille. Tämä selkeä käsittely varmistaa, että ohjelma tekee tietoisia päätöksiä virheiden korjaamisesta eikä kaadu odottamatta.


### Virheenkäsittelymallit ja pikakuvakkeet


Vaikka nimenomainen kuvioiden täsmäytys antaa täydellisen hallinnan virheiden käsittelyyn, Rust tarjoaa useita helppokäyttöisiä menetelmiä yleisiä virheiden käsittelymalleja varten. Menetelmä `unwrap` poimii onnistumisarvon `Result`-menetelmästä, mutta hätääntyy, jos virhe tapahtuu, joten se on hyödyllinen nopeassa prototyyppien luomisessa tai tilanteissa, joissa olet varma, että operaatio onnistuu. `expect`-metodi toimii samalla tavalla, mutta sen avulla voit antaa mukautetun paniikkiviestin, mikä helpottaa virheiden korjaamista, kun jokin menee pieleen.


Joustavampaa virheenkäsittelyä varten metodit, kuten `unwrap_or_else`, mahdollistavat sen, että voit tarjota sulkemisen, joka suoritetaan virheen sattuessa, jolloin voit käyttää mukautettua palautuslogiikkaa. Voit ketjuttaa näitä toimintoja yhteen monimutkaisten skenaarioiden käsittelemiseksi, kuten tiedoston avausyritys ja tiedoston luominen, jos sitä ei ole olemassa, ja käyttää eri virheenkäsittelystrategioita kussakin vaiheessa.


Kysymysmerkkioperaattori (`?`) tarjoaa tiiviin syntaksin virheiden etenemistä varten, mikä on yleistä Rust-ohjelmissa. Kun liität `?`:n `Tulokseen`, se purkaa automaattisesti onnistuneet arvot ja palauttaa virheet välittömästi nykyisestä funktiosta. Tätä operaattoria voidaan käyttää vain funktioissa, jotka palauttavat `Result`-tyyppejä, mikä varmistaa, että virheet voidaan siirtää kunnolla ylöspäin kutsupinossa. `?`-operaattori tekee virheenkäsittelykoodista paljon luettavampaa, koska se eliminoi verbaaliset vastaavuuslausekkeet ja säilyttää samalla virheiden selvän etenemissemantiikan.


```rust
use std::fs::File;
use std::io::{self, Read};

// Custom error type for wallet operations
#[derive(Debug)]
enum WalletError {
FileNotFound,
InvalidFormat,
InsufficientFunds,
}

// Function returning Result for recoverable errors
fn load_wallet_balance(path: &str) -> Result<u64, WalletError> {
// Simulate reading from file
let balance_str = "150000"; // Would normally read from file
balance_str
.parse::<u64>()
.map_err(|_| WalletError::InvalidFormat)
}

// Using the ? operator for clean error propagation
fn send_payment(amount: u64) -> Result<String, WalletError> {
let balance = load_wallet_balance("wallet.dat")?; // Propagates error if it fails

if balance < amount {
return Err(WalletError::InsufficientFunds);
}

Ok(format!("Sent {} sats, remaining: {}", amount, balance - amount))
}

fn main() {
// Handle the Result explicitly
match send_payment(50_000) {
Ok(msg) => println!("Success: {}", msg),
Err(WalletError::InsufficientFunds) => println!("Error: Not enough funds"),
Err(WalletError::FileNotFound) => println!("Error: Wallet file not found"),
Err(WalletError::InvalidFormat) => println!("Error: Corrupted wallet file"),
}

// Or use unwrap_or_else for custom fallback
let result = send_payment(200_000)
.unwrap_or_else(|e| format!("Payment failed: {:?}", e));
println!("{}", result);
}
```


### Virheiden eteneminen ja toimintojen suunnittelu


Virheiden leviäminen on Rust:n virheenkäsittelyn peruskäsite, jonka avulla funktiot voivat siirtää virheet ylöspäin kutsupinossa sen sijaan, että ne käsiteltäisiin paikallisesti. Kun suunnitellaan funktioita, jotka saattavat epäonnistua, kannattaa palauttaa `Tulos`-tyyppejä, jotta kutsujat voivat joustavasti päättää, miten virheitä käsitellään. Tämä lähestymistapa edistää yhdistettävissä olevaa virheenkäsittelyä, jossa jokainen kutsuketjun funktio voi joko käsitellä virheet paikallisesti tai siirtää ne ylemmän tason koodille, jolla on enemmän kontekstia korjauspäätösten tekemistä varten.


Kysymysmerkkioperaattori yksinkertaistaa virheiden etenemistä. Sen sijaan, että kirjoittaisit yksityiskohtaisia vastaavuuslausekkeita jokaiselle mahdollisesti epäonnistuvalle operaatiolle, voit ketjuttaa operaatiot yhteen `?-operaattoreilla luoden luettavaa koodia, joka käsittelee onnistumispolun ja siirtää automaattisesti kaikki virheet. Tämä malli on niin yleinen, että monet Rust-funktiot on suunniteltu erityisesti toimimaan hyvin `?`-operaattorin kanssa, mikä mahdollistaa sujuvan virheenkäsittelyn koko koodipohjassasi.


Kun päätät, haluatko panikoida vai palauttaa virheitä, ota huomioon, voiko kutsuva koodi kohtuullisesti toipua virheestä. Jos vika on ohjelmointivirhe tai järjestelmätila, jota ei voida korjata, paniikkiin joutuminen on asianmukaista. Jos virhe on kuitenkin odotettu tila, jota kutsuva koodi voi käsitellä eri tavalla kontekstista riippuen, `Tuloksen` palauttaminen tarjoaa paremman joustavuuden ja kokoonpantavuuden.


### Parhaat käytännöt ja suunnitteluun liittyvät näkökohdat


Tehokas virheenkäsittely Rust:ssa edellyttää tarkkaa harkintaa siitä, milloin on syytä hätääntyä ja milloin palauttaa virheet. Käytä paniikkitilanteita tilanteissa, jotka edustavat ohjelmointivirheitä tai tiloja, joita ei pitäisi koskaan esiintyä oikeissa ohjelmissa, kuten kovakoodattujen tietojen käyttäminen, joiden tiedetään olevan kelvollisia. Esimerkiksi kovakoodatun IP-osoitejonon jäsentäminen, jonka oikeellisuuden olet varmistanut, voi turvallisesti käyttää `expect`-ohjelmaa, jossa on kuvaileva viesti, joka selittää, miksi operaation ei pitäisi koskaan epäonnistua.


Kun kyseessä on käyttäjän ohjaama syöttö tai ulkoisen järjestelmän vuorovaikutus, palauta aina mieluummin `Result`-tyyppejä kuin panikoi. Käyttäjät tekevät virheitä, tiedostoja poistetaan ja verkkoyhteydet katkeavat - nämä ovat normaaleja tilanteita, jotka hyvin suunniteltujen ohjelmien tulisi käsitellä hienovaraisesti. Palauttamalla virheet näissä tilanteissa annat kutsuvalle koodille mahdollisuuden toteuttaa asianmukaisia korjausstrategioita, olipa kyse sitten käyttäjän kehottamisesta antamaan eri syötteitä, oletusarvojen palauttamisesta tai avuliaiden virheilmoitusten näyttämisestä.


Harkitse sellaisten mukautettujen tyyppien luomista, jotka varmistavat validoinnin rakennusaikana, jotta virheelliset tilat eivät pääse leviämään ohjelmassasi. Jos ohjelmasi vaatii esimerkiksi numeroita tietyllä alueella, luo kietoutumistyyppi, joka validoi syötteen rakennusvaiheessa eikä anna mahdollisuutta luoda virheellisiä esiintymiä. Tämä lähestymistapa käyttää Rust:n tyyppijärjestelmää poistamaan kokonaisia virheluokkia tekemällä virheellisistä tiloista mahdottomia esittää, mikä vähentää tarvetta virheiden tarkistamiseen ajonaikana koko koodipohjassa.


## Funktionaalisen ohjelmoinnin ominaisuudet, sulkemiset ja älykkäät osoittimet


<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>


:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::

Vaikka Rust ei ole puhdas funktionaalinen ohjelmointikieli, se sisältää funktionaalisen ohjelmoinnin paradigmojen innoittamia ominaisuuksia. Näiden ominaisuuksien avulla kehittäjät voivat kirjoittaa tiivistä koodia hyödyntämällä sellaisia käsitteitä kuin sulkeumat ja iteraattorit. Rust sisältää näitä funktionaalisia elementtejä tarjotakseen joustavia työkaluja tietojenkäsittelyyn ja takaisinkutsumekanismeihin.


Rust:n funktionaaliset ohjelmointiominaisuudet säilyttävät kielen keskeiset periaatteet, jotka koskevat muistiturvallisuutta ja nollakustannusabstraktioita. Kun käytät sulkuja ja iteraattoreita, et uhraa suorituskykyä ilmaisuvoiman vuoksi - Rust-kääntäjä optimoi nämä rakenteet tuottaakseen tehokasta konekoodia, joka on verrattavissa perinteisiin silmukoihin perustuviin lähestymistapoihin.


### Sulkemisen ymmärtäminen


Rust:ssä sulkeutuvat funktiot ovat nimettömiä funktioita, jotka voivat kaapata muuttujia ympäristöstään. Muissa ohjelmointikielissä näitä kutsutaan usein lambda-funktioiksi. Sulkujen tärkein ominaisuus on niiden kyky "sulkea" ympäristönsä, mikä tarkoittaa, että ne voivat käyttää ja käyttää muuttujia, jotka ovat olemassa siinä laajuudessa, jossa sulku on määritelty.


Sulkujen syntaksissa käytetään sulkujen sijasta putkimerkkejä (`|`) parametrien määrittelyyn. Jos sulkeuma ei sisällä parametreja, kirjoitetaan `||`, ja jos sulkeuma sisältää parametreja, ne luetellaan putkien välissä kuten `|x, y|`. Jos sulkujen runko koostuu yhdestä lausekkeesta, voit jättää sulkeet pois, jolloin syntaksi on hyvin tiivis.


Käytännön esimerkkinä on t-paita-alan yritys, joka lahjoittaa yksinoikeudella paitoja asiakkaiden mieltymysten perusteella. Jos asiakas on määritellyt suosikkivärinsä, hän saa sen; muussa tapauksessa hän saa oletuksena eniten varastossa olevan värin. Sulkeumia käyttämällä tämä logiikka muuttuu seuraavasti: `user_preference.unwrap_or_else(|| self.most_stocked())`. Sulkeuma `||| self.most_stocked()` antaa oletusarvon vain tarvittaessa, ja se voi käyttää `self` ympäristöstään.


### Sulkutyypin päättely ja joustavuus


Yksi Rust:n kätevimmistä ominaisuuksista sulkujen kanssa on automaattinen tyypin päättely. Toisin kuin tavallisissa funktioissa, joissa parametrien ja paluutyyppien tyypit on määriteltävä eksplisiittisesti, sulkutoiminnot voivat usein päätellä nämä tyypit kontekstista. Kääntäjä analysoi, miten sulkeumaa käytetään, ja määrittää sopivat tyypit automaattisesti. Kun sulkeumaa kutsutaan tietyillä tyypeillä, nämä tyypit kuitenkin kiinnittyvät kyseiseen sulkeumaan.


Voit tallentaa sulkeumia muuttujiin aivan kuten mitä tahansa arvoja, mikä tekee niistä kielen ensimmäisen luokan kansalaisia. Kun osoitat sulkeuman muuttujaan, voit kutsua sitä myöhemmin sulkeilla: `let my_closure = |x| x + 1; let result = my_closure(5);`. Tämän joustavuuden ansiosta voit antaa sulkeumia argumentteina funktioille, palauttaa niitä funktioista ja käyttää niitä tietorakenteissa.


Jos kääntäjä ei pysty päättelemään tyyppejä tai jos haluat olla selkeä, voit merkitä sulkuparametrit ja paluutyypit funktioiden kaltaisella syntaksilla: `|x: i32| -> i32 { x + 1 }`. Tämä eksplisiittinen tyypitys on joskus tarpeen monimutkaisissa tilanteissa, joissa kääntäjä tarvitsee lisätietoja ratkaistakseen tyypit oikein.


### Ympäristömuuttujien kaappaaminen


Sulkeumat voivat kaapata muuttujia ympäristöstään kolmella eri tavalla: muuttumattomalla viittauksella, muuttuvalla viittauksella tai ottamalla omistusoikeuden. Rust-kääntäjä määrittää automaattisesti rajoittavimman kaappaustavan, joka tyydyttää sulkeutumisesi tarpeet, noudattaen vähiten etuoikeuksia koskevaa periaatetta.


Kun sulkeminen tarvitsee vain lukea arvoa, se kaappaa sen muuttumattomalla viittauksella. Näin alkuperäinen muuttuja pysyy käytettävissä sulkemisen määrittelyn ja kutsun jälkeen. Esimerkiksi suljin, joka tulostaa listan, lainaa listan muuttumattomasti, jolloin voit jatkaa listan käyttöä suljinohjelman suorittamisen jälkeen.


Jos sulkemisen on muutettava kaapattua muuttujaa, sen on kaapattava muuttuvalla viittauksella. Tällöin sekä kaapattu muuttuja että sulku on ilmoitettava muuttuvaksi. Sulkeuma voi tällöin muuttaa kaapattua muuttujaa, mutta lainaussäännöt ovat edelleen voimassa - muut viittaukset kyseiseen muuttujaan eivät ole mahdollisia, kun muuttuva sulkeuma on olemassa.


Rajoittavin kaappausmenetelmä on omistusoikeuden ottaminen, jolloin kaapatut muuttujat siirretään sulkemiseen. Tämä on tarpeen silloin, kun sulkeminen saattaa ylittää sen alueen, jossa muuttujat alun perin määriteltiin, kuten esimerkiksi säikeitä luotaessa. Voit pakottaa omistajuuden haltuunoton käyttämällä avainsanaa `move` ennen closure-parametreja: `move |x| { /* closure body */ }`. Tämä on välttämätöntä säikeiden turvallisuuden kannalta, koska säikeet eivät voi turvallisesti lainata toisilta säikeiltä, jotka saattavat lopettaa toimintansa ja pudottaa muuttujansa.


### Sulkemisominaisuudet ja funktiotyypit


Rust edustaa sulkeutumisia ominaisuusjärjestelmän avulla, jossa on kolme keskeistä ominaisuutta: `FnOnce`, `FnMut` ja `Fn`. Nämä piirteet muodostavat hierarkian, joka kuvaa, miten sulkeumia voidaan kutsua ja mitä ne voivat tehdä kaapatuille muuttujille.


`FnOnce` on perustavanlaatuisin ominaisuus, jonka kaikki sulkeumat toteuttavat. Se edustaa sulkuja, joita voidaan kutsua vähintään kerran. Joitakin sulkuja, erityisesti niitä, jotka siirtävät kaapattuja arvoja tai kuluttavat niitä jollakin tavalla, voidaan kutsua vain kerran, koska ne tuhoavat tai siirtävät kaapattuja tietojaan suorituksen aikana.


`FnMut` edustaa sulkuja, joita voidaan kutsua useita kertoja ja jotka voivat muuttaa kaapattua ympäristöään. Nämä sulkeumat kaappaavat muuttujia muuttuvalla viittauksella ja voivat muuttaa niitä useiden kutsujen aikana. Lainaussäännöt varmistavat, että kun `FnMut`-sulku on aktiivinen, sillä on yksinoikeus käyttää muuttuvia muuttujia.


`Fn` on kaikkein rajoittavin ominaisuus, joka edustaa sulkuja, joita voidaan kutsua useita kertoja ilman, että niiden kaapattu ympäristö muuttuu. Nämä sulkeumat kaapataan vain muuttumattomalla viittauksella, ja niitä voidaan kutsua samanaikaisesti rikkomatta Rust:n turvallisuustakeita. Jos sulkeuma toteuttaa `Fn`, se toteuttaa automaattisesti myös `FnMut` ja `FnOnce`, koska kutsuttavuus useita kertoja ilman mutaatiota edellyttää kutsuttavuutta mutaation kanssa ja kutsuttavuutta kerran.


### Iteraattoreiden kanssa työskentely


Rust:n iteraattorit tarjoavat tavan käsitellä tietosarjoja. Ne ovat laiskoja, eli ne eivät tee mitään työtä ennen kuin käytät niitä kutsumalla metodeja, jotka todella iteroivat datan läpi. Tämä laiska arviointi mahdollistaa operaatioiden tehokkaan ketjuttamisen ilman välikokoelmien luomista.


`Iterator`-ominaisuus määrittelee ydintoiminnallisuuden ja siihen liittyvän tyypin `Item`, joka edustaa sitä, mitä iteraattori tuottaa, sekä `next`-metodin, joka palauttaa `Option<Self::Item>`. Kun `next` palauttaa `None`, iteraattori on käytetty loppuun. Tämän rakenteen ansiosta iteraattorit voivat turvallisesti esittää sekä äärellisiä että mahdollisesti äärettömiä sarjoja.


Voit luoda iteraattoreita kokoelmista käyttämällä metodeja kuten `iter()` lainaavaa iteraatiota varten, `iter_mut()` muuttuvaa lainaavaa iteraatiota varten ja `into_iter()` kuluttavaa iteraatiota varten. Valinta näiden metodien välillä riippuu siitä, tarvitseeko elementtejä muuttaa ja haluaako alkuperäisen kokoelman kuluttaa.


### Iteraattorisovittimet ja kuluttajat


Iteraattorisovittimet ovat metodeja, jotka muuttavat yhden iteraattorin toiseksi ja mahdollistavat operaatioiden ketjuttamisen. Yleisiä sovittimia ovat `map` jokaisen elementin muuntamiseen, `filter` elementtien valitsemiseen predikaatin perusteella ja `enumerate` indeksien lisäämiseen. Nämä sovittimet ovat laiskoja - ne eivät tee mitään työtä ennen kuin ne käytetään.


Metodi `map` soveltaa sulkua jokaiseen elementtiin ja muuttaa sen joksikin muuksi. Esimerkiksi `numbers.iter().map(|x| x * 2)` luo iteraattorin, joka kaksinkertaistaa jokaisen luvun. Metodi `filter` säilyttää vain ne elementit, joiden osalta predikaatin sulkeminen palauttaa totuuden: `numbers.iter().filter(|&x| x > 10)` säilyttää vain luvut, jotka ovat suurempia kuin kymmenen.


Kuluttajamenetelmät todella käyvät läpi tiedot ja tuottavat lopputuloksen. Metodi `collect` kuluttaa iteraattorin ja luo siitä kokoelman. Usein on määritettävä kokoelman tyyppi: `let vec: Vec<_> = iterator.collect()`. Muita kuluttajia ovat `sum` numeeristen elementtien laskemiseen, `fold` arvojen keräämiseen mukautetulla operaatiolla ja `for_each` sivuvaikutusten suorittamiseen jokaiselle elementille.


### Edistyneet iteraattorikuviot


Muita iteraattorioperaatioita ovat `zip` kahden iteraattorin yhdistämiseen elementtiviisaasti, `chain` iteraattoreiden ketjuttamiseen ja `filter_map` suodatuksen ja kartoituksen yhdistämiseen samaan operaatioon. `zip`-metodi luo pareja kahden iteraattorin vastaavista elementeistä: `a.iter().zip(b.iter())` tuottaa tuplat `(a[0], b[0]), (a[1], b[1]), ...`.


Menetelmä `fold` on hyödyllinen arvojen keräämiseen. Se ottaa alkuarvon ja sulkeuman, joka yhdistää kertojan jokaiseen alkioon: `numbers.iter().fold(0, |acc, x| acc + x)` summaa kaikki luvut. Tällä mallilla voidaan toteuttaa monia muita operaatioita, kuten etsiä maksimiarvoja, muodostaa merkkijonoja tai luoda monimutkaisia tietorakenteita.


Iteraattoriketjuilla voidaan ilmaista monimutkaisia tietomuunnoksia tiiviisti. Esimerkiksi audiodatan käsittelyyn voi kuulua: kertoimet.iter().zip(buffer.iter()).map(|(c, b)| c * b).sum::<i32>() >> 12`. Näin kerrotaan vastaavat kertoimet ja puskuriarvot, summataan tulokset ja siirretään loppuarvo, kaikki yhdessä luettavassa lausekkeessa.


```rust
fn main() {
// Sample UTXOs: (txid_suffix, amount_sats)
let utxos = vec![
("a1b2", 50_000u64),
("c3d4", 15_000),
("e5f6", 100_000),
("g7h8", 3_000),
("i9j0", 75_000),
];

// Using closures and iterators to process UTXOs

// 1. Filter UTXOs above dust threshold (10,000 sats)
let spendable: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000)
.collect();
println!("Spendable UTXOs: {:?}", spendable);

// 2. Calculate total balance with fold
let total_balance: u64 = utxos
.iter()
.map(|(_, amount)| amount)
.fold(0, |acc, amount| acc + amount);
println!("Total balance: {} sats", total_balance);

// 3. Find UTXOs needed to cover a 120,000 sat payment
let target = 120_000u64;
let mut accumulated = 0u64;
let selected: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000) // Skip dust
.take_while(|(_, amount)| {
if accumulated >= target {
false
} else {
accumulated += amount;
true
}
})
.collect();
println!("Selected for payment: {:?}", selected);

// 4. Transform to display format using map and collect
let display_strings: Vec<String> = utxos
.iter()
.map(|(txid, amount)| format!("{}...:{} sats", txid, amount))
.collect();
println!("Display: {:?}", display_strings);
}
```


### Johdanto älykkäisiin osoittimiin


Älykkäät osoittimet ovat tietorakenteita, jotka toimivat kuten perinteiset osoittimet, mutta tarjoavat lisäominaisuuksia ja automaattisen muistinhallinnan. Toisin kuin yksinkertaiset viittaukset, älykkäät osoittimet omistavat datan, johon ne osoittavat, ja ne voivat toteuttaa mukautetun käyttäytymisen muistin varaamista, poistamista ja käyttötapoja varten. Ne ovat välttämättömiä välineitä kasaan osoitetun datan hallinnassa ja sellaisten monimutkaisten omistusmallien toteuttamisessa, jotka ylittävät Rust:n perusomistusjärjestelmän.


"Älykäs" ominaisuus johtuu niiden kyvystä hoitaa automaattisesti muistinhallintatehtäviä, jotka muuten vaatisivat manuaalista toimintaa. Kun älykäs osoitin poistuu käyttöalueen ulkopuolelle, se voi automaattisesti vapauttaa siihen liittyvää muistia, pienentää viitteiden lukumäärää tai suorittaa muita siivoustoimenpiteitä. Tämä automaatio auttaa estämään muistivuodot ja use-after-free-virheet ja tarjoaa samalla enemmän joustavuutta kuin pelkkä pinoallokaatio.


Älykkäät osoittimet toteuttavat yleensä kaksi keskeistä ominaisuutta: `Deref` ja `Drop`. `Deref`-ominaisuuden avulla älykästä osoitinta voidaan käyttää ikään kuin se olisi viittaus sen sisältämään dataan. `Drop`-ominaisuus mahdollistaa mukautetun siivouslogiikan, kun älykäs osoitin tuhotaan. Yhdessä nämä ominaisuudet mahdollistavat sen, että älykkäät osoittimet voivat hallita muistia automaattisesti.


### Laatikko Smart Pointer


`Box<T>` on yksinkertaisin älykäs osoitin, joka tarjoaa kasan varauksen mille tahansa tyypille `T`. Kun luot `Box`:n, sen sisältämä arvo tallennetaan kasaan eikä pinoon, ja itse `Box` (joka on vain osoitin) tallennetaan pinoon. Tämä ohjaaminen on hyödyllistä, kun haluat tallentaa suuria määriä dataa siirtämättä sitä, kun tarvitset tyyppiä, jonka kokoa ei tiedetä kääntämisaikana, tai kun haluat siirtää kasan datan omistajuutta tehokkaasti.


`Boxin` luominen on suoraviivaista: `let boxed_value = Box::new(42);` varaa kokonaisluvun kasaan. `Box` hallinnoi tätä muistia automaattisesti - kun `Box` poistuu toimialueeltaan, se poistaa automaattisesti kasan muistin. Tämä automaattinen siivous estää muistivuodot ilman manuaalista muistinhallintaa.


Yksi `Box`:n tärkeimmistä käyttötapauksista on rekursiivisten tietorakenteiden mahdollistaminen. Tarkastellaan linkitettyä listaa, jossa jokainen solmu sisältää arvon ja osoittimen seuraavaan solmuun. Ilman `Box`:ia et voi määritellä tällaista rakennetta, koska kääntäjä ei voi määrittää sellaisen tyypin kokoa, joka sisältää itsensä. Käyttämällä `Box<Node>` seuraavaa osoitinta varten, voit ratkaista rekursiivisen kokoongelman, koska `Box`illa` on tunnettu, kiinteä koko riippumatta siitä, mitä se sisältää.


### Deref-ominaisuuden toteuttaminen


`Deref`-ominaisuus sallii tyypin poistamisen `*`-operaattorin avulla, jolloin älykkäät osoittimet käyttäytyvät kuin viittaukset sisältämäänsä dataan. Kun toteutat `Deref`-ominaisuuden älykkäälle osoittimelle, otat käyttöön automaattisen dereferenssin, joka tekee älykkään osoittimen käytöstä läpinäkyvää. Tämä tarkoittaa, että voit kutsua sisältämän tyypin metodeja suoraan älykkään osoittimen kautta ilman nimenomaista dereferenssiä.


Piirre `Deref` määrittelee siihen liittyvän tyypin `Target`, joka määrittää, minkä tyyppisen viittauksen dereference-operaation tulisi tuottaa. Ominaisuus edellyttää sellaisen `deref`-metodin toteuttamista, joka palauttaa viittauksen kohdetyyppiin. Kun kyseessä on `Box<T>`, toteutus palauttaa viittauksen sisältämäänsä `T`-arvoon.


Rust suorittaa automaattisen deref-yhteensopivuuden, mikä tarkoittaa, että kääntäjä voi automaattisesti lisätä kutsuja `deref`:lle, kun se on tarpeen tyyppien yhteensopivuuden varmistamiseksi. Tämän vuoksi voit antaa `Stringin` funktiolle, joka odottaa `&str` - kääntäjä dereferoi `Stringin` automaattisesti saadakseen merkkijonoviipaleen. Tämä pakko-operaatio voi ketjuttaa useita tasoja, joten `Box<String>` voidaan muuntaa automaattisesti `&str`:ksi useiden deref-operaatioiden avulla.


### Mukautetun pudotuksen toteutus


`Drop`-ominaisuuden avulla voit määrittää mukautetun siivouskoodin, joka suoritetaan, kun arvo poistuu vaikutusalueen ulkopuolelle. Tämä on erityisen tärkeää älykkäille osoittimille, jotka hallinnoivat muitakin resursseja kuin pelkkää muistia, kuten tiedostokahvoja, verkkoyhteyksiä tai viittauslukuja. Piirteellä `Drop` on yksi metodi, `drop`, joka ottaa muuttuvan viittauksen `self`:iin ja suorittaa siivouksen.


Useimmat tyypit eivät tarvitse mukautettuja `Pudota`-toteutuksia, koska Rust hoitaa kenttien pudottamisen automaattisesti. Älykkäät osoittimet tarvitsevat kuitenkin usein mukautettua logiikkaa, jotta niiden hallinnoimat resurssit voidaan siivota asianmukaisesti. Esimerkiksi viittauslaskennan omaavan älykkään osoittimen on vähennettävä viittausten lukumäärää ja mahdollisesti poistettava jaettua dataa, kun viimeinen viittaus poistetaan.


Voit myös nimenomaisesti pudottaa arvon ennen kuin se poistuu toimialueelta käyttämällä `std::mem::drop()`. Tämä funktio ottaa arvon haltuunsa ja pudottaa sen välittömästi, mikä voi olla hyödyllistä, kun haluat vapauttaa resursseja aikaisin tai varmistaa, että siivous tapahtuu tietyssä vaiheessa ohjelmaa. Eksplisiittinen drop-funktio on vain identiteettifunktio, joka ottaa omistusoikeuden - todellinen työ tapahtuu, kun arvo pudotetaan funktion lopussa.


Tämä sulkujen, iteraattoreiden ja älykkäiden osoittimien perusta antaa Rust-kehittäjille työkalut, joiden avulla he voivat kirjoittaa ilmaisuvoimaista, turvallista ja tehokasta koodia. Nämä ominaisuudet mahdollistavat yhdessä yleiset ohjelmointimallit säilyttäen samalla Rust:n keskeiset takuut muistiturvallisuudesta ja suorituskyvystä.



## Viitteiden laskenta ja sisäinen muunneltavuus

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>


:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::

### Vertailulaskenta RC:llä


Viittauslaskenta on toinen Rust:n älykkään osoittimen perustyyppi, joka on suunniteltu erityisesti mahdollistamaan usean omistajan skenaariot. Toisin kuin Box, joka noudattaa perinteisiä yhden omistajan sääntöjä, joissa yksi yksikkö omistaa tiedot, RC (Reference Counter) mahdollistaa sen, että useat koodin osat voivat jakaa saman tiedon omistuksen samanaikaisesti. Tämä jaetun omistuksen malli toimii laskentamekanismin avulla, joka seuraa, kuinka monta viittausta tiettyyn tietoon on olemassa.


Vertailulaskentajärjestelmä toimii ylläpitämällä sisäistä laskuria, joka kasvaa joka kerta, kun kloonaat RC:n, ja pienenee, kun RC pudotetaan. Muisti vapautetaan vasta, kun laskuri saavuttaa nollan, mikä varmistaa, että tiedot pysyvät voimassa niin kauan kuin viittauksia on olemassa. Tämä lähestymistapa estää ennenaikaisen poistamisen ja mahdollistaa samalla joustavat tiedonjakomallit, jotka olisivat mahdottomia pelkällä laatikon omistajuudella.


Käytännön esimerkki, jossa RC on hyödyllinen, on jaettujen tietorakenteiden, kuten linkitettyjen listojen, luominen, kun useat listat saattavat viitata samaan loppuosaan. Ajatellaan, että yritetään luoda kaksi erillistä listaa, jotka molemmat viittaavat yhteiseen osajaksoon. Box-omistajuuden avulla tämä on mahdotonta, koska yhteisen osan siirtäminen ensimmäiseen listaan siirtää omistajuuden, mikä estää sen käytön toisessa listassa. RC ratkaisee tämän sallimalla viitteen kloonaamisen taustalla olevan datan sijasta, jolloin jaettu rakenne on mahdollinen ja muistiturvallisuus säilyy.


Kun kloonaat RC:n, et kopioi sisäisiä tietoja sen koosta tai monimutkaisuudesta riippumatta. Sen sijaan luot toisen viittauksen samaan muistipaikkaan ja kasvatat viittauslaskuria. Tämä tekee RC-instanssien kloonaamisesta tehokasta myös suurille tietorakenteille, koska vain itse viittaus kopioidaan, kun taas taustalla oleva data pysyy paikallaan.


### Sisätilojen muunneltavuus RefCellin avulla


RefCell ottaa käyttöön sisäisen muunneltavuuden, jonka avulla voit muunnella dataa, vaikka sinulla olisi vain muuttumaton viittaus siihen. Tämä kyky muuttaa perusteellisesti Rust:n lainaussääntöjen noudattamista siirtämällä tarkistukset kääntämisajalta suoritusaikaan. Kun tavalliset viittaukset luottavat kääntäjän varmistavan lainausturvallisuuden, RefCell suorittaa nämä tarkistukset ohjelman suorituksen aikana, mikä tarjoaa enemmän joustavuutta mahdollisen ajonaikaisen paniikin kustannuksella.


RefCellin ydinperiaatteena on säilyttää samat lainaussäännöt, joita Rust normaalisti noudattaa kääntämisaikana, mutta tarkistaa ne dynaamisesti. RefCellin sisällä oleviin tietoihin voi olla kullakin hetkellä joko yksi muuttuva viittaus tai mikä tahansa määrä muuttumattomia viittauksia. Jos koodisi yrittää rikkoa näitä sääntöjä luomalla ristiriitaisia lainauksia samanaikaisesti, ohjelma hätääntyy eikä tuota määrittelemätöntä käyttäytymistä.


Tämä ajonaikainen tarkistus mahdollistaa tietyt ohjelmointimallit, jotka kääntäjä saattaa hylätä, vaikka ne olisivat oikeasti turvallisia. Kääntäjän staattinen analyysi ei voi aina todistaa, että monimutkaiset lainausmallit ovat oikeita, mikä saa sen valitsemaan varovaisuuden puolelle. RefCellin avulla voit ohittaa nämä konservatiiviset rajoitukset, kun olet varma koodisi oikeellisuudesta, mutta tämä luottamus tuo mukanaan vastuun oikeasta käytöstä, jotta vältetään ajonaikaiset kaatumiset.


RefCellin yleinen käyttötapaus sisältää mock-objekteja testausskenaarioissa. Kun toteutetaan ominaisuus, joka tarjoaa vain muuttumattoman pääsyn itseensä, mutta pilkkuobjektin toteutuksen on seurattava tilamuutoksia sisäisesti, RefCell mahdollistaa tämän mallin. Voit kietoa sisäisen tilan RefCellin sisään, jolloin mock voi muuttaa seurantatietojaan jopa muuttumattoman rajapinnan kautta.


### RC:n ja RefCellin yhdistäminen jaettua muuttuvaa tilaa varten


RC:n ja RefCellin yhdistelmä luo mallin jaetulle muuttuvalle tilalle, jossa useat omistajat voivat mahdollisesti muokata samaa dataa. RC tarjoaa jaetun omistajuuden, kun taas RefCell mahdollistaa mutation muuttumattomien viittausten avulla. Tämä yhdistelmä on käyttökelpoinen esimerkiksi graafirakenteissa, välimuisteissa tai missä tahansa tilanteessa, jossa useat ohjelman osat tarvitsevat sekä luku- että kirjoitusoikeuksia jaettuun dataan.


Kun kietot RefCellin RC:n sisälle, luot rakenteen, jota voidaan kloonata ja jakaa koko ohjelmaan, ja jokainen klooni tarjoaa pääsyn samaan taustalla olevaan muuttuvaan dataan. Kaikki omistajat voivat mahdollisesti muokata dataa RefCellin borrow_mut-metodilla, mutta niiden on silti noudatettava lainaussääntöjä ajonaikana. Tämä malli mahdollistaa monimutkaiset tiedonjakoskenaariot säilyttäen samalla Rust:n turvatakuut ajonaikaisten tarkistusten avulla.


Tähän joustavuuteen liittyy kuitenkin tärkeitä varoituksia muistivuodoista ja viittaussykleistä. Kun RC:tä käytetään RefCellin kanssa, on mahdollista luoda vahingossa ympyräviittauksia, joissa tietorakenteet viittaavat itseensä joko suoraan tai viittausketjun kautta. Nämä syklit estävät viitteiden lukumäärän koskaan pääsemästä nollaan, mikä aiheuttaa muistivuotoja, koska datalla näyttää olevan aina aktiivisia viitteitä, vaikka se ei ole enää käytettävissä muualta ohjelmasta.


Ratkaisu viittaussykleihin on käyttää heikkoja viittauksia, jotka eivät vaikuta muistinhallintapäätöksissä käytettävään viittausmäärään. Heikkojen viittausten avulla voit ylläpitää tietorakenteiden välisiä yhteyksiä pitämättä niitä elossa, mikä katkaisee mahdolliset syklit ja säilyttää samalla mahdollisuuden käyttää niihin liittyviä tietoja, kun ne ovat vielä olemassa.


```rust
use std::rc::Rc;
use std::cell::RefCell;

// Simulating a channel state that multiple components need to access and modify
#[derive(Debug)]
struct ChannelState {
channel_id: String,
local_balance_msat: u64,
remote_balance_msat: u64,
is_active: bool,
}

fn main() {
// Rc<RefCell<T>> allows multiple owners with interior mutability
let channel = Rc::new(RefCell::new(ChannelState {
channel_id: "abc123".to_string(),
local_balance_msat: 1_000_000_000,  // 1M sats in msats
remote_balance_msat: 500_000_000,
is_active: true,
}));

// Clone Rc to share ownership (cheap - only increments counter)
let channel_for_ui = Rc::clone(&channel);
let channel_for_router = Rc::clone(&channel);

// Reference count is now 3
println!("Reference count: {}", Rc::strong_count(&channel));

// UI component reads the state (immutable borrow)
{
let state = channel_for_ui.borrow();
println!("UI shows balance: {} msats", state.local_balance_msat);
} // borrow ends here

// Router updates the state after a payment (mutable borrow)
{
let mut state = channel_for_router.borrow_mut();
state.local_balance_msat -= 100_000_000; // Sent 100k sats
state.remote_balance_msat += 100_000_000;
println!("Router updated balances");
} // mutable borrow ends here

// Original reference can still read the updated state
let state = channel.borrow();
println!("New local balance: {} msats", state.local_balance_msat);

// WARNING: This would panic at runtime!
// let borrow1 = channel.borrow();
// let borrow2 = channel.borrow_mut(); // PANIC: already borrowed
}
```


### Säikeiden turvallisuuden ja samanaikaisuuden perusteet


Rust:n lähestymistapa samanaikaisuuteen keskittyy datakilpailujen ja muistiturvallisuusongelmien estämiseen kääntämisaikana. Tyyppijärjestelmä varmistaa säikeiden turvallisuuden sellaisten ominaisuuksien kuten `Send` ja `Sync` avulla, jotka merkitsevät tyypit turvallisiksi säikeiden välistä siirtoa varten tai turvallisiksi samanaikaista käyttöä varten. Tämä kääntämisen aikainen varmistus havaitsee monia samanaikaisuusvirheitä, jotka ilmenisivät muissa järjestelmäohjelmointikielissä vasta ajonaikana.


Säikeiden luominen Rust:ssa noudattaa suoraviivaista kaavaa käyttäen thread::spawnia, joka ottaa uudessa säikeessä suoritettavan sulkemisen ja palauttaa kahvan säikeen elinkaaren hallintaa varten. Kylvetty säie toimii samanaikaisesti pääsäikeen kanssa, ja voit käyttää kahvan join-metodia odottaaksesi valmistumista. Ilman nimenomaista liittämistä luodut säikeet saatetaan lopettaa, kun pääsäie poistuu, jolloin keskeneräinen työ saattaa jäädä kesken.


Move-avainsanasta tulee ratkaisevan tärkeä säikeiden kanssa työskenneltäessä, koska synnytetyille säikeille välitettyjen sulkujen on usein omistettava datansa sen sijaan, että ne lainaisivat sitä. Koska kätketyt säikeet voivat elää kauemmin kuin niiden luonut alue, lainaaminen vanhemmasta alueesta voi aiheuttaa mahdollisia elinaikarikkomuksia. Tietojen siirtäminen säikeen sulkemiseen siirtää omistusoikeuden, jolloin varmistetaan, että tiedot pysyvät voimassa koko säikeen elinkaaren ajan, mutta estetään pääsy alkuperäisestä laajuudesta.


Viestien välitys tarjoaa vaihtoehdon jaetun tilan rinnakkaisuudelle kanavien avulla, joiden avulla säikeet voivat kommunikoida lähettämällä dataa sen sijaan, että jakaisivat muistia. Rust:n standardikirjasto tarjoaa Multiple Producer Single Consumer (MPSC) -kanavia, joissa useat säikeet voivat lähettää viestejä yhdelle vastaanottavalle säikeelle. Tämä malli poistaa monia synkronointiongelmia välttämällä jaettua muuttuvaa tilaa kokonaan ja luottamalla sen sijaan viestinvaihtoon koordinoinnissa.


### Jaetun tilan samanaikaisuus Mutexin ja Arcin avulla


Kun viestien välitys ei sovellu, Rust tarjoaa perinteisen jaetun tilan samanaikaisuuden Mutexin (keskinäinen poissulkeminen) ja Arcin (Atomic Reference Counter) avulla. Mutex varmistaa, että vain yksi säie voi käyttää suojattua dataa kerrallaan vaatimalla säikeitä hankkimaan lukituksen ennen datan käyttöä. Lukko vapautuu automaattisesti, kun lukitusoperaation palauttama vartijaobjekti poistuu soveltamisalan ulkopuolelle, mikä estää lukituksen unohtamisen aiheuttamat yleiset lukkiutumisskenaariot.


Arc toimii RC:n säikeenkestävänä vastineena, joka käyttää atomisia operaatioita viitteiden lukumäärän turvalliseen hallintaan useiden säikeiden välillä. Vaikka RC toimii täydellisesti yhden säikeen skenaarioissa, sen ei-atominen viittauslaskenta aiheuttaa kilpailutilanteita, kun sitä käytetään useista säikeistä. Arcin atomiset laskurit varmistavat, että viittauslaskennan muutokset tapahtuvat turvallisesti myös samanaikaisessa käytössä, joten se soveltuu tietojen jakamiseen yli säikiorajojen.


Arc- ja Mutex-ominaisuuksien yhdistelmä luo mallin rinnakkaisohjelmien jaettua muuttuvaa tilaa varten. Käärimällä Mutex Arciin voit kloonata Arcin ja jakaa pääsyn samaan mutexiin useille säikeille, jolloin jokainen säie voi hankkia lukituksen ja muokata suojattua dataa turvallisesti. Tämä malli tarjoaa jaetun tilan joustavuuden säilyttäen samalla Rust:n turvatakuut kääntämisaikaisen verifioinnin ja ajonaikaisen lukituksen avulla.


Send- ja Sync-ominaisuudet toimivat kulissien takana varmistaakseen säikeiden turvallisuuden kääntämisaikana. Send osoittaa, että tyyppi voidaan siirtää turvallisesti toiseen säikeeseen, kun taas Sync osoittaa, että viittaukset tyyppiin voidaan jakaa turvallisesti säikeiden välillä. Useimmat tyypit toteuttavat nämä piirteet automaattisesti, kun niiden komponentit ovat säikeenkestäviä, mutta jotkin tyypit, kuten RC ja RefCell, eivät nimenomaisesti toteuta niitä, koska niitä ei ole suunniteltu yhtäaikaiseen käyttöön. Tämä automaattinen ominaisuuksien toteutus estää säikeistöturvallisuuden loukkaukset vahingossa ja sallii samalla turvallisten tyyppien saumattoman toiminnan samanaikaisissa yhteyksissä.


## Rust-makrojen ymmärtäminen

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>


:::video id=5e96914d-df02-4781-ae54-b06008952301:::

### Johdanto makroihin Rust:ssä


Rust:n makrot ovat metaohjelmointiominaisuus, jonka avulla kehittäjät voivat kirjoittaa koodia, joka tuottaa toista koodia käännösaikana. Toisin kuin funktioita, joita kutsutaan suoritusaikana, makrot laajennetaan varhaisessa vaiheessa kääntämisprosessia, ennen tyypintarkistusta ja myöhempiä vaiheita. Tämä perustavanlaatuinen ero tekee makroista erityisen hyödyllisiä koodin toistamisen vähentämisessä ja Rust-ohjelmissa käytettävien aluespesifisten kielten luomisessa.


Makrokutsun tunnistettavin merkki on makron nimen perässä oleva huutomerkki (!). Kun esimerkiksi käytät `println!("Hello, world!")`, et kutsu funktiota vaan makroa. Tämä makro laajenee monimutkaisemmaksi koodiksi, joka käsittelee muotoilu- ja tulostustoimintoja. Huutomerkki toimii visuaalisena merkkinä kehittäjille siitä, että kyseessä on käännöksen aikainen koodin luominen eikä tavallinen funktiokutsu.


Rust tarjoaa kolme erilaista makrotyyppiä, joilla kullakin on erilaiset tarkoitukset kielen ekosysteemissä:



- Funktion kaltaiset makrot**: Muistuttavat funktiokutsuja, mutta toimivat kääntämisaikana (esim. `vec!`, `println!`)
- Makrojen johtaminen**: Toteuta automaattisesti tyyppien ominaisuudet (esim. `#[derive(Debug, Clone)]`)
- Attribuutin kaltaiset makrot**: Muuttaa niiden koodielementtien käyttäytymistä, joihin niitä sovelletaan (esim. `#[test]`, `#[tokio::main]`)


Näiden eri makrotyyppien ymmärtäminen on olennaista tehokkaan Rust-ohjelmoinnin kannalta, sillä kukin makrotyyppi on tarkoitettu tiettyihin käyttötapauksiin ja ohjelmointimalleihin.


### Makrotyypit ja niiden sovellukset


Funktion kaltaiset makrot ovat Rust-ohjelmoinnissa yleisimmin käytetty makrotyyppi. Nämä makrot käyttävät samankaltaista syntaksia kuin funktiokutsut, mutta ne sovittavat syötteensä kuvioihin generate soveltuvaan koodiin. Makro `vec!` on yleinen esimerkki tästä luokasta, ja sen avulla kehittäjät voivat luoda ja alustaa vektoreita tiiviillä syntaksilla. Kun kirjoitat `vec![1, 2, 3, 4]`, makro muuntaa tämän koodiksi, joka luo uuden vektorin, työntää jokaisen elementin erikseen ja palauttaa valmiin vektorin.


Derive-makrot tarjoavat automaattisia ominaisuustoteutuksia mukautetuille tyypeille, mikä vähentää huomattavasti plasmakoodia. Kun lisäät `#[derive(Debug)]` struct- tai enum-määritelmään, käsket kääntäjää tekemään generate:lle täydellisen toteutuksen Debug-ominaisuudesta kyseiselle tyypille. Tämä generoitu toteutus käsittelee muotoilulogiikan, joka on tarpeen tyypin sisällön näyttämiseksi ihmisen luettavassa muodossa. Derive-mekanismi tukee lukuisia kirjaston vakio-ominaisuuksia, kuten Clone, PartialEq, joten se on yleisesti käytetty työkalu boilerplate-luonnosten vähentämiseen.


Attribuutin kaltaiset makrot muuttavat niiden koodielementtien käyttäytymistä, joita ne kommentoivat, ja tarjoavat tavan lisätä metatietoja tai muuttaa kääntämisen käyttäytymistä. Nämä makrot näkyvät attribuutteina, jotka on sijoitettu tyyppimääritelmien, funktioiden tai muiden koodirakenteiden yläpuolelle. Esimerkiksi enumin attribuutti `#[non_exhaustive]` ilmaisee, että tulevissa versioissa voidaan lisätä lisämuunnoksia, jolloin täsmääviin lausekkeisiin on sisällytettävä oletustapaus. Tämä mekanismi varmistaa yhteensopivuuden eteenpäin ja tarjoaa samalla selkeän dokumentaation tyypin kehitysmahdollisuuksista.


### Mukautettujen funktioiden kaltaisten makrojen luominen


Mukautettujen funktioiden kaltaisten makrojen kirjoittaminen edellyttää Rust:n makromäärittelyjen mallien vastaavuussyntaksin ymmärtämistä. Makromäärittelyssä käytetään deklaratiivista lähestymistapaa, jossa määritetään kuvioita, jotka sopivat erilaisiin syöttölomakkeisiin ja vastaaviin koodin generointimalleihin. Kukin makro voi sisältää useita haaroja, jolloin se voi käsitellä erilaisia syötemalleja ja generate asianmukaista koodia jokaista tapausta varten.


Harkitse mukautetun vektorimakron luomista, joka demonstroi makron rakentamisen perusperiaatteita. Makron määrittely alkaa sanalla `macro_rules!`, jota seuraa makron nimi ja sarja kuvioita yhdistäviä haaroja. Kukin haara koostuu kuvioista, jotka vastaavat tiettyä syöttösyntaksia, ja koodimallista, joka tuottaa vastaavan Rust-koodin. Yksinkertainen haara voi esimerkiksi vastata tyhjiä sulkuja `[]` ja generate-koodia tyhjän vektorin luomiseksi, kun taas toinen haara vastaa yksittäistä lauseketta ja luo koodin, jolla luodaan vektori, jossa on yksi elementti.


Makroista on hyötyä erityisesti silloin, kun käytetään muuttujan argumenttikuvioita toistosyntaksia käyttäen. Kuvio `$($x:expr),*` vastaa nollaa tai useampaa pilkulla erotettua lauseketta, jolloin makro voi käsitellä mielivaltaista määrää argumentteja. Vastaava koodinmuodostusmalli käyttää `$(vec.push($x);)*` kaikkien sovitettujen lausekkeiden läpikäymiseen ja generate:n yksittäisiä push-lausekkeita kullekin lausekkeelle. Tämän toistomekanismin avulla makroilla voidaan generate kirjoittaa koodia, jonka kirjoittaminen manuaalisesti olisi mahdotonta tai erittäin työlästä.


```rust
// A macro to create a HashMap with Bitcoin-related data
macro_rules! btc_map {
// Empty case
() => {
std::collections::HashMap::new()
};
// Key-value pairs case
($($key:expr => $value:expr),+ $(,)?) => {
{
let mut map = std::collections::HashMap::new();
$(
map.insert($key, $value);
)+
map
}
};
}

// A macro for logging with context (simulating a derive-like pattern)
macro_rules! log_payment {
($level:ident, $($arg:tt)*) => {
println!(
"[{}] [PAYMENT] {}",
stringify!($level).to_uppercase(),
format!($($arg)*)
)
};
}

fn main() {
// Using the btc_map! macro
let fee_rates = btc_map! {
"high_priority" => 50_u64,    // sats/vbyte
"medium" => 25_u64,
"low" => 10_u64,
};

println!("Fee rates: {:?}", fee_rates);

// Using the log_payment! macro
log_payment!(info, "Sending {} sats to {}", 100_000, "bc1q...");
log_payment!(warn, "Fee rate {} sats/vB is above average", 75);
log_payment!(error, "Payment failed: insufficient funds");

// Standard vec! macro usage comparison
let utxos = vec![50_000_u64, 30_000, 20_000];
let total: u64 = utxos.iter().sum();
println!("Total UTXOs: {} sats", total);
}
```


Käännösprosessi muuttaa makrokutsut laajennetuksi koodiksi ennen tyypintarkistusta ja optimointia. Kun kääntäjä kohtaa makrokutsun, se vertaa syötettä määriteltyihin malleihin ja korvaa makrokutsun generoidulla koodilla. Tämä laajennettu koodi käy sitten läpi normaalit kääntämisprosessit, mukaan lukien tyypintarkistus ja optimointi. Työkalujen, kuten `cargo expand`, avulla kehittäjät voivat tarkastaa tuotetun koodin, mikä tarjoaa arvokkaita virheenkorjausmahdollisuuksia kehitettäessä monimutkaisia makroja.


### Edistyneet makrokäsitteet ja virheenkorjaus


Makrojen kehittäminen edellyttää, että ymmärrät käännöksen ja suoritusajan välisen eron. Makrot suoritetaan kääntämisen aikana, jolloin syntyy koodia, joka suoritetaan suoritusaikana. Tämä ajallinen erottelu tarkoittaa, että makron logiikka ei voi olla riippuvainen ajonaikaisista arvoista, mutta se mahdollistaa myös optimoinnit, joissa monimutkaiset laskutoimitukset voidaan suorittaa kerran kääntämisen aikana eikä toistuvasti suorituksen aikana.


Makrojen hahmontäsmäytysjärjestelmä tukee erilaisia fragmenttimääritteitä, jotka määrittelevät, millaisia koodielementtejä voidaan sovittaa. `expr`-määrittely vastaa lausekkeita, `ty` vastaa tyyppejä, `ident` vastaa tunnisteita ja useat muut määrittelyt tarjoavat hienojakoista valvontaa syötteen validointiin. Nämä määritteet varmistavat, että makrot saavat syntaktisesti kelvollisen syötteen ja antavat selkeät virheilmoitukset, kun virheellinen syntaksi havaitaan.


Makrojen virheenkorjaus asettaa ainutlaatuisia haasteita niiden kääntämisaikaisen luonteen vuoksi. Komento `cargo expand` on hyödyllinen makrojen kehityksessä, sillä se näyttää makrojen kutsujen tuottaman täysin laajennetun koodin. Tämän työkalun avulla kehittäjät voivat tarkistaa, että heidän makrojensa generate vastaa aiottua koodia, ja tunnistaa laajentamislogiikassa esiintyviä ongelmia. Kun makron tuottama koodi sisältää virheitä, laajennettu tuloste auttaa määrittämään, onko ongelma makron määritelmässä vai tuotetussa koodirakenteessa.


Monimutkaiset makrot voivat toteuttaa rekursiivisia malleja, joissa makro kutsuu itseään muuttuneilla argumenteilla, jotta voidaan käsitellä sisäkkäistä tai iteratiivista koodin tuottamista. Rekursiiviset makrot vaativat kuitenkin huolellista suunnittelua, jotta vältetään ääretön laajeneminen ja kääntämisen suorituskykyongelmat. Makrojen laajenemisen kääntämisaikainen luonne tarkoittaa, että tehottomatkin makrototeutukset vaikuttavat vain kääntämisnopeuteen, eivät suoritusajan suorituskykyyn, mutta liian monimutkaiset makrot voivat hidastaa rakentamisprosessia merkittävästi.



# Rust & Bitcoin

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>


## Miksi Rust Bitcoin-kehitystä varten

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>


:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::


Rust:n valinta Bitcoin:n ja Lightning-kehityksen tilalle ei ole sattumaa. Bitcoin:n kehittämiseen liittyy ainutlaatuisia vastuita, jotka erottavat sen tavanomaisesta ohjelmistokehityksestä. Bitcoin:n parissa työskennellessään kehittäjät käsittelevät usein käyttäjien varoja ympäristössä, jossa virheet voivat olla peruuttamattomia. Toisin kuin perinteisissä rahoitusjärjestelmissä, joissa on lainsäädännöllinen suoja ja takaisinkantomekanismit, Bitcoin:n hajautettu luonne tarkoittaa, että kun [transaktio](https://planb.academy/resources/glossary/transaction-tx) on lähetetty, ei ole mitään viranomaista, jonka puoleen kääntyä varojen takaisinperimiseksi. Tämä todellisuus edellyttää ohjelmistokehitykseltä suurempaa vastuullisuutta ja tarkkuutta.


Monilla teknologia-aloilla toimiva "etene nopeasti ja hajota asioita" -filosofia ei yksinkertaisesti sovellu Bitcoin:n kehitykseen. Sen sijaan ekosysteemi vaatii kieliä ja työkaluja, jotka auttavat kehittäjiä luomaan vankkoja ja turvallisia ohjelmistoja, joissa virheet joko estetään tai käsitellään sujuvasti. Tämän vuoksi monet merkittävät Bitcoin-projektit ovat siirtyneet Rust:ään, kuten Bitcoin Development Kit (BDK), Lightning Development Kit (LDK) ja BreezSDK.


Rust tarjoaa kolme olennaista ominaisuutta, jotka tekevät siitä erityisen sopivan Bitcoin-kehitykseen: staattinen vahva tyyppijärjestelmä, monipuolinen moderni työkalupaketti ja alustarajat ylittävä yhteensopivuus. Jokainen näistä ominaisuuksista edistää kielen kykyä auttaa kehittäjiä kirjoittamaan turvallisempaa ja luotettavampaa koodia [kryptovaluuttaoperaatioiden](https://planb.academy/resources/glossary/cryptocurrency) käsittelyyn.


### Rust:n staattinen vahva tyyppijärjestelmä


Rust:n tyyppijärjestelmä tarjoaa sekä staattisen että vahvan tyypittelyn ominaisuudet, jotka toimivat yhdessä virheiden havaitsemiseksi ennen kuin ne voivat vaikuttaa käyttäjiin. Staattinen luonne tarkoittaa, että tyypin tarkistus tapahtuu kääntämisen aikana, jolloin kehittäjien on ratkaistava tyyppivirheet ennen kuin ohjelmaa voidaan edes rakentaa. Tämä eroaa dynaamisesti tyypitetyistä kielistä, joissa tyyppivirheet tulevat esiin vasta ajon aikana, mahdollisesti sen jälkeen, kun ohjelmisto on otettu käyttöön ja se käsittelee todellisia käyttäjävaroja.


Rust:n tyyppijärjestelmän vahvuus on sen ilmaisuvoima ja tarkkuus ongelmien mallintamisessa. Toisin kuin kielissä, joissa on heikommat tyyppijärjestelmät, kuten C:ssä, jossa kehittäjät rajoittuvat perustyyppeihin, kuten numeroihin ja structeihin, Rust mahdollistaa monipuolisen tyyppimallinnuksen, jolla voidaan esittää monimutkaisia toimialan käsitteitä tarkasti. Voit esimerkiksi luoda tyyppejä, jotka erottavat toisistaan erityyppiset luettelot, tai vaatia, että tietyt operaatiot suoritetaan vain tietyille objektityypeille.


Rust:n tyyppijärjestelmä on Bitcoin:n kehityksen kannalta merkityksellinen sen lähestymistavan vuoksi, joka koskee muistin turvallisuutta. Sama tyyppijärjestelmä, joka mallintaa liiketoimintalogiikkaa, käsittelee myös muistin omistajuutta ja jaetun käytön valvontaa. Tämä kaksoisvastuu tarkoittaa sitä, että kääntäjä eliminoi kokonaan yleiset haavoittuvuusluokat, kuten muistivuodot, kaksoisvapaat virheet ja kilpailuolosuhteet. Tyyppijärjestelmä varmistaa nämä turvatakuut omistajuuden, lainaamisen ja viitteiden laskennan kaltaisilla käsitteillä, joten on erittäin vaikeaa ottaa käyttöön muistiin liittyviä virheitä, jotka voisivat vaarantaa turvallisuuden tai vakauden.


```rust
// Example: Type-safe Bitcoin amount handling
// Using newtypes to prevent mixing up satoshis and other values

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct Satoshis(u64);

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct FeeRate(u64); // sats per vbyte

impl Satoshis {
fn from_btc(btc: f64) -> Self {
Satoshis((btc * 100_000_000.0) as u64)
}

fn as_btc(&self) -> f64 {
self.0 as f64 / 100_000_000.0
}
}

// Calculate fee given tx size - type system ensures we can't mix up values
fn calculate_fee(tx_size_vbytes: u32, rate: FeeRate) -> Satoshis {
Satoshis(tx_size_vbytes as u64 * rate.0)
}

fn main() {
let payment = Satoshis::from_btc(0.001); // 100,000 sats
let fee_rate = FeeRate(25);              // 25 sats/vbyte
let tx_size = 250_u32;                   // vbytes

let fee = calculate_fee(tx_size, fee_rate);
println!("Payment: {:?} ({} BTC)", payment, payment.as_btc());
println!("Fee: {:?}", fee);

// This would NOT compile - type safety prevents mixing values:
// let bad_fee = calculate_fee(tx_size, payment); // ERROR: expected FeeRate, found Satoshis
}
```


### Nykyaikaiset työkalut ja cross-platform-tuki


Rust:n työkaluekosysteemi tarjoaa kehittäjille työkaluja, jotka auttavat tuottavuudessa ja koodin laadussa. Itse Rust-kääntäjä ei ole suunniteltu vain kääntämään koodia binäärimuotoon, vaan se toimii myös opetusvälineenä, joka auttaa kehittäjiä oppimaan ja kehittymään. Kun kääntämisvirheitä ilmenee, kääntäjä antaa yksityiskohtaisen selityksen siitä, mikä meni pieleen, ja ehdottaa usein erityisiä korjauksia. Tämä lähestymistapa on erityisen arvokas Rust:ta vasta-alkajille, sillä kääntäjä opettaa tehokkaasti hyviä käytäntöjä ja auttaa ehkäisemään yleisiä virheitä.


Kieli sisältää Cargon, yhtenäisen paketinhallintaohjelman, joka huolehtii riippuvuuksien hallinnasta, rakentamisesta, testauksesta ja dokumentaation tuottamisesta. Tämä standardointi poistaa vanhoissa kielissä, kuten C++:ssa, havaitun pirstaleisuuden, jossa useat kilpailevat työkalut aiheuttavat epäjohdonmukaisuutta eri projekteissa. Cargo tukee myös laajennuksia, kuten rustfmt koodin muotoiluun ja Clippy staattiseen analyysiin, mikä varmistaa, että koodi noudattaa johdonmukaisia tyyliohjeita ja havaitsee mahdolliset ongelmat ennen kuin niistä tulee ongelmia.


Rust:n cross-platform-ominaisuudet ulottuvat perinteisiä käyttöjärjestelmiä laajemmalle ja kattavat Androidin ja iOS:n kaltaiset mobiilialustat sekä WebAssemblyn selainpohjaisia sovelluksia varten. Tämä alustarajat ylittävä tuki on hyödyllinen Bitcoin-sovelluksille, joita on käytettävä erilaisissa ympäristöissä. Esimerkiksi Mutinyn Wallet kaltaisissa projekteissa hyödynnetään Rust WebAssembly-käännöstoimintoa, jotta voidaan luoda Lightning-[lompakoita](https://planb.academy/resources/glossary/wallet), jotka toimivat suoraan verkkoselaimissa, mikä ei olisi käytännössä mahdollista pelkästään perinteisillä verkkotekniikoilla.


### Virhetyyppien ja niiden vaikutusten ymmärtäminen


Tehokas virheenkäsittely alkaa ymmärtämällä eri virhetyypit, joita voi esiintyä ohjelman suorituksen aikana. Tarkastellaan yksinkertaista reitityssovellusta, joka laskee maantieteellisten pisteiden välisiä reittejä. Tämä esimerkki havainnollistaa kolme perustyyppistä virhetyyppiä, jotka kehittäjien on käsiteltävä: virheelliset syöttövirheet, suoritusajan resurssivirheet ja logiikkavirheet.


Virheellisiä syöttövirheitä esiintyy, kun funktio vastaanottaa parametreja, jotka eivät täytä sen vaatimuksia. Jos esimerkiksi maantieteellinen koordinaattijärjestelmä käyttää pituusasteena kokonaislukuja, mutta vastaanottaa negatiivisen arvon, vaikka vain positiiviset arvot ovat sallittuja, funktio ei voi jatkaa mielekkäästi. Tällaiset virheet merkitsevät sopimusrikkomusta kutsujan ja funktion välillä, ja asianmukainen vastaus on yleensä syötteen hylkääminen ja virheilmoituksen palauttaminen.


Suoritusaikaresurssivirheitä tapahtuu, kun ulkoiset riippuvuudet eivät ole käytettävissä tai niitä ei voida käyttää. Karttatiedoston lukeminen saattaa epäonnistua, koska tiedostoa ei ole olemassa, sovelluksella ei ole asianmukaisia käyttöoikeuksia tai tallennuslaite ei ole käytettävissä. Nämä virheet ovat ohjelmalogiikan ulkopuolisia ja vaativat usein pikemminkin ympäristökorjauksia kuin koodimuutoksia. Vankkojen sovellusten on kuitenkin ennakoitava ja käsiteltävä nämä skenaariot sujuvasti.


Logiikkavirheet ovat virheitä ohjelman toteutuksessa tai väärinkäsityksiä komponenttien vuorovaikutuksesta. Jos reititysalgoritmi palauttaa tyhjän polun, vaikka sille annetaan kelvolliset alku- ja loppupisteet, tämä osoittaa loogisen virheen, joka on korjattava itse koodissa. Toisin kuin muut virhetyypit, loogiset virheet vaativat yleensä virheenkorjausta ja koodin muuttamista.


### Vankat virheidenhallintastrategiat


Luotettavien ohjelmistojen rakentaminen edellyttää ennakoivia strategioita, joilla minimoidaan virhemahdollisuudet ja käsitellään väistämättömät virheet tyylikkäästi. Ensimmäiseen strategiaan kuuluu mahdollisten virheiden rajoittaminen huolellisella tyyppisuunnittelulla. Valitsemalla tyypit, jotka voivat edustaa vain kelvollisia arvoja, kehittäjät voivat poistaa kokonaisia virheellisten syötteiden luokkia. Esimerkiksi käyttämällä merkitsemättömiä kokonaislukuja arvoille, jotka eivät voi olla negatiivisia, estetään negatiivisten arvojen virheet kääntämisaikana.


Väitteet tarjoavat toisen suojauskerroksen tarkistamalla nimenomaisesti, että odotetut ehdot pitävät paikkansa ohjelman suorituksen aikana. Näillä tarkistuksilla on useita tarkoituksia: ne havaitsevat virheitä testauksen aikana, aiheuttavat ohjelmien epäonnistumisen varhaisessa vaiheessa ongelmien ilmetessä (mikä helpottaa virheenkorjausta) ja toimivat suoritettavana dokumentaationa, joka kuvaa ohjelmoijan oletuksia. Kun väittämä epäonnistuu, se osoittaa, että jokin ohjelman tilaa koskeva perusolettamus on rikottu, mikä yleensä viittaa logiikkavirheeseen, joka on tutkittava.


Kerroksellisten abstraktioiden periaate auttaa hallitsemaan monimutkaisuutta varmistamalla, että virheet käsitellään järjestelmän asianmukaisilla tasoilla. Sisäiset toteutuksen yksityiskohdat, mukaan lukien alemman tason kirjastojen erityiset virhetyypit, eivät saisi levitä osajärjestelmän rajojen ulkopuolelle. Sen sijaan jokaisen tason pitäisi kääntää virheet termeiksi, jotka ovat merkityksellisiä kyseisellä abstraktiotasolla. Esimerkiksi wallet-sovelluksen, joka käyttää Bitcoin-kirjastoa, pitäisi kääntää alemman tason kuvaajien jäsentämisvirheet korkeamman tason viesteiksi, kuten "virheellinen wallet-konfiguraatio", jotka antavat käyttäjille tai kutsuvalle koodille toimintakelpoista tietoa.


Tämä lähestymistapa virheiden käsittelyyn yhdistettynä Rust:n tyyppijärjestelmään ja työkaluihin auttaa havaitsemaan mahdolliset ongelmat kehitysprosessin alkuvaiheessa, ennen kuin ne voivat vaikuttaa käyttäjiin tai vaarantaa Bitcoin-sovellusten turvallisuuden.



## Virhemalli

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>


:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::

Rust tarjoaa kattavan lähestymistavan virheiden käsittelyyn, jossa turvallisuus ja käytännöllisyys ovat tasapainossa. Vaikka yleiset virhemallin käsitteet soveltuvat kaikkiin ohjelmointikieliin, Rust tarjoaa erityisiä työkaluja ja malleja, jotka tekevät virheiden käsittelystä sekä selkeää että hallittavaa. Näiden mekanismien ymmärtäminen on ratkaisevan tärkeää, jotta voidaan kirjoittaa vankkoja Rust-sovelluksia, jotka pystyvät käsittelemään odottamattomia tilanteita sujuvasti ja säilyttämään samalla suorituskyvyn ja turvallisuuden.


### Paniikki ja sen tarkoituksenmukainen käyttö


Rust:n paniikkimekanismi on suorin tapa käsitellä korjaamattomia virheitä. Kun kutsut `panic!`-makroa, ohjelma pysäyttää suorituksen välittömästi joko keskeyttämällä tai purkamalla sen asetuksista riippuen. Paniikkimakro hyväksyy merkkijonoviestin, joka kuvaa, mikä meni pieleen, ja tarjoaa kontekstin virheenkorjausta varten. Lisäksi metodit kuten `unwrap()` ja `expect()` Result- ja Option-tyypeille toimivat oikotienä paniikkiin, kun nämä tyypit sisältävät virhearvoja tai None-arvoja. `expect()`-metodin avulla voit antaa mukautetun viestin, mikä tekee siitä hieman informatiivisemman kuin `unwrap()`-metodista virheitä debugattaessa.


Yksinkertaisuudestaan huolimatta panicia tulisi käyttää harkiten tuotantokoodissa. On useita tilanteita, joissa paniikki on paitsi hyväksyttävää myös suositeltavaa. Esimerkkejä tai prototyyppejä kirjoitettaessa panic tarjoaa selkeän tavan keskittyä ydintoimintoihin ilman, että koodia sotketaan kattavalla virheenkäsittelyllä. Testausympäristöissä paniikki on usein toivottu käyttäytymistapa, kun väittämät epäonnistuvat, koska se osoittaa selvästi, että jotain odottamatonta tapahtui. Rust-yhteisö tunnustaa myös tilanteet, joissa kehittäjillä on enemmän tietoa kuin kääntäjällä, kuten esimerkiksi kun analysoidaan kovakoodattuja IP-osoitteita, joiden tiedetään olevan kelvollisia.


"Kääntäjän varmentamien" paniikkien näennäinen turvallisuus voi kuitenkin olla harhaanjohtavaa. Ajattele skenaariota, jossa IP-osoite on kovakoodattu ja käytät `expect()`-ohjelmaa, koska tiedät sen olevan kelvollinen. Ajan mittaan, kun koodi kehittyy, tuo kovakoodattu arvo saatetaan muuttaa vakioksi, ja myöhemmin vakio saatetaan muuttaa esimerkiksi muotoon "localhost" paremman käyttökokemuksen vuoksi. Yhtäkkiä "turvallisesta" paniikistasi tulee suoritusaikainen virhe. Tämä kehitys osoittaa, miksi on yleensä parempi välttää paniikkia tuotantokoodissa ja sen sijaan palauttaa sopivia virhetyyppejä, joita voidaan käsitellä hienovaraisesti.


Yksi huomattava poikkeus "vältä paniikkia" -sääntöön koskee mutex-operaatioita. Kun kutsut `lock()` mutexille, se palauttaa tuloksen Result, koska lukitus voi epäonnistua, jos toinen säie joutuu paniikkiin pitäessään mutexia hallussaan. Tämä aiheuttaa hämmentävän tilanteen, jossa paikallinen koodisi saa virheilmoituksen jostain, joka tapahtui täysin eri kontekstissa. Koska et voi järkevästi käsitellä virhettä, joka on peräisin toisen säikeen paniikista, monet kehittäjät pitävät mutex-lukkojen purkamista hyväksyttävänä, varsinkin jos ylläpidät muualla paniikittomia koodipohjia.


### Tulos- ja vaihtoehtotyyppien kanssa työskentely


Result-tyyppi muodostaa Rust:n virheenkäsittelyjärjestelmän selkärangan. Koska Result on enum, joka voi sisältää joko `Ok(arvo)` tai `Err(virhe)`, se pakottaa sinut tunnustamaan nimenomaisesti, että toiminnot voivat epäonnistua. Option-tyyppi palvelee vastaavaa tarkoitusta tapauksissa, joissa arvo saattaa yksinkertaisesti puuttua, sisältäen joko `Some(arvo)` tai `None`. Vaikka Option ei anna yksityiskohtaista virhetietoa, se sopii täydellisesti tilanteisiin, joissa arvon puuttuminen on merkityksellistä ja odotettua.


Sekä Result että Option tarjoavat useita apumenetelmiä, jotka tekevät virheiden käsittelystä ergonomisempaa. Metodi `unwrap_or()` palauttaa sisältämänsä arvon, jos se on olemassa, tai oletusarvon, jos on virhe tai None. Tämä malli on erityisen hyödyllinen, kun sinulla on järkevä varajärjestely, kuten käyttäjän syötteen jäsentäminen järkevällä oletusarvolla, kun jäsentäminen epäonnistuu. Metodi `unwrap_or_default()` toimii samalla tavalla, mutta se käyttää tyypin oletusarvoa sen sijaan, että sinun tarvitsisi määrittää sellainen. Vaikka nämä metodit eivät teknisesti käsittele virheitä perinteisessä mielessä, ne tarjoavat tavan vähentää toiminnallisuutta ongelmien ilmetessä.


Kysymysmerkkioperaattori (`?`) on ytimekäs syntaksi virheiden etenemistä varten. Kun sitä sovelletaan Result- tai Option-funktioon, se poimii onnistumisarvon, jos se on olemassa, tai palauttaa välittömästi virheen nykyisestä funktiosta, jos ongelma on olemassa. Tämä operaattori eliminoi Go:n kaltaisissa kielissä yleiset laajamittaiset virheentarkistusmallit, joissa virheet on tarkistettava ja palautettava manuaalisesti jokaisessa vaiheessa. Kysymysmerkkioperaattori tarjoaa lähinnä syntaktista sokeria varhaisia palautuksia varten, jolloin voit kirjoittaa puhdasta, lineaarista koodia, joka keskittyy onnelliseen polkuun ja käsittelee virheiden etenemisen automaattisesti.


### Edistyneet virheenkäsittelymallit


Result- ja Option-tyyppien `map()`-metodi mahdollistaa funktionaalisen tyylin virheenkäsittelyn, joka voi tehdä koodista ilmaisuvoimaisempaa ja sommiteltavampaa. Kun kutsut `map()` -toimintoa Result-tyypille, annettua funktiota sovelletaan menestysarvoon, jos se on olemassa, kun taas virheet siirretään automaattisesti ilman muutoksia. Tämä malli on hyödyllinen, kun operaatioita ketjutetaan, sillä voit keskittyä arvojen muuttamiseen ilman toistuvaa virhetapausten käsittelyä. Metodi `map_err()` tarjoaa käänteisen toiminnallisuuden, jolloin voit muuntaa virhetyyppejä ja jättää onnistumisarvot ennalleen.


Virheiden muuntaminen on ratkaisevan tärkeää, kun rakennetaan monikerroksisia sovelluksia, joissa eri komponentit tarvitsevat erilaisia virhetyyppejä. Tarkastellaan funktiota, joka jäsentää käyttäjän syötettä ja jonka on muunnettava matalan tason jäsentämisvirheet toimialuekohtaisiksi virheiksi. Käyttämällä `map_err()` voit helposti muuntaa yleisen "invalid number format" -virheen kontekstisidonnaisemmaksi "invalid age" -virheeksi, joka on järkevä sovelluksesi toimialueella. Tämä muunnos tapahtuu juuri siinä vaiheessa, kun virhe tapahtuu, mikä tekee koodista luettavampaa ja helpommin ylläpidettävää kuin perinteiset try-catch-lohkot, joissa virheiden käsittely on erotettu toiminnoista, jotka voivat epäonnistua.


Kysymysmerkkioperaattorin ja virhekartoituksen yhdistelmä luo tiiviitä virheenkäsittelymalleja. Voit ketjuttaa operaatioita, muuntaa virheet tarpeen mukaan ja siirtää ne ylöspäin kutsupinossa mahdollisimman pienellä määrittelyllä. Tämä lähestymistapa pitää virheenkäsittelyn lähellä operaatioita, jotka voivat epäonnistua, mutta säilyttää samalla onnistumis- ja virhepolkujen selkeän erottelun.


```rust
use std::fmt;

// Layered error types for a wallet application
#[derive(Debug)]
enum NetworkError {
ConnectionFailed(String),
Timeout,
}

#[derive(Debug)]
enum WalletError {
Network(NetworkError),
InvalidAddress(String),
InsufficientFunds { required: u64, available: u64 },
}

// Implement Display for user-friendly messages
impl fmt::Display for WalletError {
fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
match self {
WalletError::Network(e) => write!(f, "Network error: {:?}", e),
WalletError::InvalidAddress(addr) => write!(f, "Invalid address: {}", addr),
WalletError::InsufficientFunds { required, available } =>
write!(f, "Need {} sats but only have {} available", required, available),
}
}
}

// Convert from lower-level error to domain error
impl From<NetworkError> for WalletError {
fn from(err: NetworkError) -> Self {
WalletError::Network(err)
}
}

// Simulated network call
fn fetch_balance(address: &str) -> Result<u64, NetworkError> {
if address.starts_with("bc1") {
Ok(500_000) // 500k sats
} else {
Err(NetworkError::ConnectionFailed("Invalid endpoint".into()))
}
}

// Higher-level function using ? with automatic error conversion
fn send_payment(from: &str, amount: u64) -> Result<String, WalletError> {
let balance = fetch_balance(from)?; // NetworkError auto-converts to WalletError

if balance < amount {
return Err(WalletError::InsufficientFunds {
required: amount,
available: balance,
});
}

Ok(format!("Sent {} sats", amount))
}

fn main() {
match send_payment("bc1qtest...", 100_000) {
Ok(msg) => println!("Success: {}", msg),
Err(e) => println!("Failed: {}", e), // User-friendly message
}
}
```


### Ulkoiset kirjastot ja virheenkäsittely-ekosysteemit


Rust-ekosysteemi sisältää useita suosittuja kirjastoja, jotka laajentavat standardikirjaston virheenkäsittelyominaisuuksia. `anyhow`-kirjasto tarjoaa yksinkertaistetun lähestymistavan virheenkäsittelyyn tarjoamalla universaalin virhetyypin, joka voi automaattisesti muuntaa minkä tahansa virhetyypin, joka toteuttaa standardin Error-ominaisuuden. Tämän automaattisen muuntamisen ansiosta voit käyttää kysymysmerkkioperaattoria eri virhetyyppien kanssa ilman manuaalista muuntamista, mikä tekee siitä erityisen hyödyllisen sovelluksissa, joissa eri virhetyyppejä ei tarvitse erottaa ohjelmallisesti toisistaan.


Vaikka `anyhow` on erinomainen yksinkertaistamaan virheiden käsittelyä sovelluksissa, joissa virheet näytetään ensisijaisesti käyttäjille, sillä on rajoituksia kirjastokehityksessä. Koska `anyhow` muuttaa kaikki virheet merkkijonoviesteiksi, kirjastosi käyttäjät eivät voi helposti reagoida ohjelmallisesti erilaisiin virhetilanteisiin. Tämä rajoitus tekee `anyhow`:sta sopivamman loppukäyttäjäsovelluksiin kuin kirjastoihin, joiden on annettava jäsenneltyä virhetietoa kuluttajilleen.


Edistyneemmissä virheenkäsittelymenetelmissä luodaan mukautettuja virhetyyppejä, jotka mallintavat sovelluksen tai kirjaston erityisiä virhetiloja. Hyvin suunniteltu virhemalli voi erottaa toisistaan virheellisen syötteen (jonka soittaja voi korjata), suoritusaikavirheet (joita voi yrittää uudelleen) ja pysyvät virheet (jotka viittaavat vikoihin tai korjaamattomiin olosuhteisiin). Tämän jäsennellyn lähestymistavan ansiosta koodin käyttäjät voivat tehdä älykkäitä päätöksiä siitä, miten reagoida erityyppisiin virheisiin, olipa kyse sitten toimintojen uudelleen yrittämisestä, käyttäjien kehottamisesta antamaan eri syötteitä tai vikailmoituksista kehittäjille.


## UniFFI, Rust-kirjastojen yhdistäminen useisiin kieliin


<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>


:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::

### Johdatus UniFFI:hen ja alustarajat ylittävään kehitykseen


UniFFI on työkalu, jonka avulla Rust-kirjastoja voidaan käyttää useilla eri ohjelmointikielillä ja alustoilla. Mozillan kehittämä työkalu vastaa nykyaikaisen ohjelmistokehityksen perustavanlaatuiseen haasteeseen: miten hyödyntää Rust:n suorituskyky- ja turvallisuushyötyjä ja säilyttää samalla yhteensopivuus erilaisten kehitysekosysteemien kanssa. Työkalu luo automaattisesti kielisidoksia Rust-kirjastoille, jolloin kehittäjien ei tarvitse luoda manuaalisesti rajapintakoodia kullekin kohdekielelle.


UniFFI:n keskeinen ongelma johtuu Rust:n luonteesta käännettynä kielenä. Kun Rust-koodi käännetään, se tuottaa binääritulosteen, jossa on Foreign Function Interface (FFI), joka tarjoaa matalan tason rajapinnan, jota voi olla haastavaa käyttää suoraan korkeamman tason kielistä, kuten Pythonista, Swiftistä tai Kotlinista. Perinteisesti jokaisen kirjaston kehittäjän olisi pitänyt kirjoittaa mukautettua sidontakoodia jokaiselle kohdekielelle, mikä olisi muodostanut merkittävän esteen alustarajat ylittävälle käyttöönotolle. UniFFI poistaa tämän tarpeettomuuden tarjoamalla standardoidun lähestymistavan näiden sidosten automaattiseen tuottamiseen.


Työkalun suunnittelufilosofia keskittyy siihen, että Rust-kehittäjät voivat keskittyä ydinliiketoimintalogiikkaan ja samalla tehdä kirjastot muilla kielillä työskentelevien kehittäjien ulottuville. Esimerkiksi Swiftiä käyttävä iOS-kehittäjä voi käyttää Rust-kirjastoa UniFFI:n luomien sidosten kautta, jotka esittävät täysin natiivin Swift-käyttöliittymän ilman mitään merkkejä siitä, että taustalla oleva toteutus on kirjoitettu Rust-kielellä. Tämän saumattoman integroinnin ansiosta tiimit voivat hyödyntää Rust:n suorituskykyetuja ilman, että kaikkien tiimin jäsenten on opittava Rust:aa.


### UniFFI-arkkitehtuurin ja työnkulun ymmärtäminen


UniFFI toimii hyvin määritellyn työnkulun avulla, joka muuntaa Rust-kirjastot monikielisiksi yhteensopiviksi paketeiksi. Prosessi alkaa UDL-tiedoston (Unified Definition Language) luomisella, joka toimii rajapintamäärittelynä, jossa kuvataan, mitkä osat Rust-kirjastosta on esitettävä muille kielille. Tämä UDL-tiedosto toimii sopimuksena Rust-toteutuksen ja luotujen kielisidosten välillä.


Arkkitehtuurissa noudatetaan selkeää huolenaiheiden erottelua. Kehittäjät ylläpitävät Rust-kirjastoaan Rust-standardin mukaisilla idiomeilla ja malleilla ja luovat sitten erillisen UDL-tiedoston, joka kuvaa julkisen rajapinnan UniFFI-tyyppijärjestelmään. UniFFI-sidontageneraattori käsittelee sekä Rust-kirjastoa että UDL-määrittelyä tuottaakseen natiivikielisiä sidoksia halutuille kohdealustoille. Nämä luodut sidokset hoitavat kaiken monimutkaisen tietojen siirtämisen ja poistamisen vieraan kielen ajoajan ja Rust-koodin välillä.


Suoritusaikana arkkitehtuuri luo kerroksittaisen lähestymistavan, jossa kohdekielellä (esimerkiksi Kotlin for Android) kirjoitettu sovelluskoodi on vuorovaikutuksessa luodun sidontakoodin kanssa, joka näyttää täysin natiivilta kyseiselle kielelle. Tämä sidontakerros huolehtii kielikohtaisten tyyppien ja Rust-tyyppien välisestä kääntämisestä, hallitsee muistia turvallisesti yli kielirajojen ja tarjoaa virheenkäsittelyn, joka noudattaa kohdekielen konventioita. Taustalla oleva Rust:n liiketoimintalogiikka säilyy muuttumattomana, eikä se ole tietoinen sen päälle rakennetuista monikielisistä rajapinnoista.


### Työskentely UDL:n kanssa: Interface:n määritelmä ja tyyppikartoitus


UniFFI:n toiminnallisuuden kulmakivenä toimii Unified Definition Language, joka tarjoaa deklaratiivisen tavan määritellä, mitkä Rust-kirjaston osat on esitettävä ja miten ne esitetään kohdekielissä. UDL-tiedostojen on sisällettävä vähintään yksi nimiavaruus, joka toimii säiliönä funktioille, joita voidaan kutsua suoraan ilman, että objekteja tarvitsee instantioida. Nämä nimiavaruusfunktiot käsittelevät tyypillisesti yksinkertaisia operaatioita, jotka ottavat parametreina arvoja ja palauttavat tuloksia.


UDL tukee kattavaa joukkoa sisäänrakennettuja tyyppejä, jotka vastaavat luontevasti vastaavia Rust-tyyppejä. Perustyyppeihin kuuluvat vakiomuotoiset primitiivit, kuten booleanit, eri kokoiset kokonaisluvut (u8, u32 jne.), liukuluvut ja merkkijonot. Monimutkaisempiin tyyppeihin kuuluvat vektorit, hash-kartat ja Rust-kohtaiset käsitteet, kuten Option-tyypit (jotka esitetään kysymysmerkkisyntaksilla) ja Result-tyypit virheiden käsittelyä varten. Tyyppijärjestelmä tukee myös enumerointeja, sekä yksinkertaisia arvoihin perustuvia enumeita että monimutkaisia enumeita, jotka sisältävät niihin liittyviä tietoja, mikä mahdollistaa kielirajat ylittävän tietomallinnuksen.


Rust:n rakenteet käännetään UDL:n sanakirjoiksi, jolloin vastaavuus säilyy lähes yksi yhteen ja mukautuu UDL:n syntaksikonventioihin. Kun Rust-rakenteisiin liittyy metodeja, ne voidaan esittää UDL:ssä rajapintoina, jotka generate ovat luokkia metodeineen oliosuuntautuneissa kohdekielissä, kuten Kotlinissa tai Swiftissä. Tämä kartoitus säilyttää objektiorientoituneet suunnittelumallit, joita kehittäjät odottavat näissä kielissä, ja säilyttää samalla taustalla olevan Rust-toteutuksen rakenteen ja käyttäytymisen.


```
// Example UDL file for a Bitcoin wallet library (wallet.udl)
namespace wallet {
// Namespace functions - called directly without object
string generate_mnemonic();
Wallet create_wallet(string mnemonic);
};

// Dictionary (struct) - becomes data class in Kotlin, struct in Swift
dictionary Balance {
u64 confirmed_sats;
u64 pending_sats;
};

// Interface (class with methods) - becomes class with methods
interface Wallet {
// Constructor
constructor(string mnemonic);

// Methods
Balance get_balance();
string get_new_address();
string send_to_address(string address, u64 amount_sats);
};

// Enum with data - maps to sealed class (Kotlin) or enum with associated values (Swift)
[Enum]
interface TransactionStatus {
Pending(u32 confirmations_needed);
Confirmed(u32 block_height);
Failed(string reason);
};

// Error enum for Result types
[Error]
enum WalletError {
"InsufficientFunds",
"InvalidAddress",
"NetworkError",
};

// Function that can fail - throws in target language
interface Wallet {
[Throws=WalletError]
string send_to_address(string address, u64 amount_sats);
};
```


Vastaava Rust-toteutus määrittelisi nämä tyypit ja toteuttaisi `uniffi::export`-attribuutin Kotlinin, Swiftin, Pythonin ja muiden tuettujen kielten generate-sidoksiin.


### Virheiden käsittely ja lisäominaisuudet


UniFFI tarjoaa virheenkäsittelyn, joka säilyttää Rust:n tulospohjaisen virhemallin ja kääntää sen kohdekielille sopivaksi. Rust:n Result-tyyppejä palauttavat funktiot voidaan merkitä UDL:ssä "throws"-avainsanalla, mikä määrittää, mitä virhetyyppejä ne voivat tuottaa. Nämä virheet on määriteltävä UDL-tiedostossa error enumeina, ja niiden on toteutettava Rust:n vakiomuotoinen Error-ominaisuus taustalla olevassa Rust-koodissa. Thiserror-luokka tarjoaa kätevän makron tämän ominaisuuden toteuttamiseen, mikä vähentää huomattavasti virhekoodia.


Virheenkäsittelykäännös osoittaa UniFFIn kielitietoisen lähestymistavan. Kotlinissa UDL generate:ssä heittäviksi merkityt funktiot ovat menetelmiä, jotka heittävät poikkeuksia Javan/Kotlinin konventioiden mukaisesti. Python-sidoksissa käytetään vastaavasti Pythonin poikkeusmallia. Tällä käännöksellä varmistetaan, että virheenkäsittely tuntuu luonnolliselta ja idiomaattiselta kullakin kohdekielellä säilyttäen samalla alkuperäisten Rust-virhetyyppien semanttisen merkityksen.


Takaisinkutsurajapinnat ovat toinen edistyksellinen ominaisuus, joka mahdollistaa kaksisuuntaisen viestinnän Rust-kirjastojen ja käyttösovellusten välillä. Kun Rust-kirjaston on kutsuttava takaisin sovelluskoodiin, kehittäjät voivat määritellä Rust:ssä piirteitä ja merkitä ne UDL:ssä takaisinkutsurajapinnoiksi. Käyttösovellus toteuttaa nämä rajapinnat omalla äidinkielellään, ja UniFFI hoitaa monimutkaisen marshaloinnin, jota tarvitaan näiden takaisinkutsujen kutsumiseen Rust-koodista. Tämä malli edellyttää säikeiden turvallisuuden huolellista tarkastelua, koska takaisinkutsut voivat ylittää säierajat, mikä edellyttää Send- ja Sync-rajojen käyttöä Rust:n puolella.


### Todelliset sovellukset ja nykyiset rajoitukset


UniFFI on otettu käyttöön kryptovaluutta- ja lohkoketjukehitysyhteisössä, ja suuret hankkeet, kuten BDK (Bitcoin Development Kit), LDK (Lightning Development Kit) ja erilaiset wallet-toteutukset, käyttävät sitä mobiilien SDK:iden tarjoamiseen. Nämä hankkeet osoittavat UniFFI:n käytön tuotantoympäristöissä.


Tarkastelemalla näiden hankkeiden todellisia UDL-tiedostoja saadaan selville käytännöllisessä käytössä esiin tulleita malleja ja parhaita käytäntöjä. Esimerkiksi BDK:n UDL-tiedosto osoittaa, miten monimutkaiset toimialuemallit, joissa on useita enumeja, structteja ja rajapintoja, voidaan kartoittaa tehokkaasti kattavien mobiilisovellusten SDK:iden luomiseksi. UDL-syntaksin yhdenmukaisuus eri projekteissa tarkoittaa, että kehittäjät, jotka tuntevat yhden UniFFI:n tukeman kirjaston, voivat nopeasti ymmärtää ja työskennellä muiden kanssa, mikä luo verkostovaikutuksen, joka hyödyttää koko ekosysteemiä.


UniFFI:llä on kuitenkin huomattavia rajoituksia, jotka kehittäjien on otettava huomioon. Merkittävin niistä on asynkronisten rajapintojen tuen puute. Kaikki luodut sidokset ovat synkronisia, joten kehittäjien on käsiteltävä asynkronisia operaatioita Rust-koodissaan ja esitettävä synkroniset rajapinnat kuluttaville sovelluksille. Lisäksi dokumentaation sijoittaminen on haasteellista: Rust-koodiin kirjoitettu dokumentaatio ei siirry luotuihin sidoksiin, kun taas UDL-tiedostoissa oleva dokumentaatio ei ole kirjaston suorien Rust-käyttäjien saatavilla. Vaikka näitä rajoituksia pyritään parhaillaan poistamaan automaattisen jäsentelyn ja tuottamisen avulla, ne ovat edelleen nykyisten toteutusten kannalta ongelmallisia. UniFFI tuottaa kielisidoksia, mutta ei hoida alustakohtaista pakkaamista ja jakelua, joten kehittäjien on itse huolehdittava jakelukelpoisten pakettien luomisesta kullekin kohdealustalle.


# LNP/BP:n kehittäminen SDK:n avulla

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>


## LN-solmu SDK:ssa

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>


:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::

### LDK:n modulaarisen arkkitehtuurin ymmärtäminen


Lightning Development Kit (LDK) lähestyy [Lightning Network](https://planb.academy/resources/glossary/lightning-network):n toteutusta eri tavalla kuin perinteiset solmuohjelmistot, kuten CLightning tai LND. Kun perinteiset Lightning-[solmut](https://planb.academy/resources/glossary/node) toimivat täydellisinä daemon-sovelluksina, jotka toimivat jatkuvasti koneella, LDK toimii modulaarisena Rust-kirjastona, joka tarjoaa alkeiskomponentteja mukautettujen Lightning-ratkaisujen rakentamiseen. Tämä arkkitehtoninen ero tekee LDK:sta joustavan, jolloin kehittäjät voivat koota Lightning-toiminnallisuutta tavalla, joka palvelee heidän erityisiä projektivaatimuksiaan.


LDK:n keskeinen filosofia on modulaarisuus ja mukautuvuus. Monoliittisen ratkaisun sijaan LDK tarjoaa yksittäisiä komponentteja, joita voidaan yhdistellä, mukauttaa tai korvata kokonaan. Jokaisen komponentin mukana toimitetaan oletustoteutukset, jotka toimivat heti, mutta kehittäjät voivat tarvittaessa korvata ne omilla toteutuksillaan. LDK sisältää esimerkiksi oletustoteutukset lohkoketjun seurantaa, transaktioiden allekirjoittamista ja verkkoviestintää varten, mutta mikä tahansa näistä voidaan korvata mukautetuilla ratkaisuilla, jotka on räätälöity tiettyihin käyttötapauksiin tai ympäristöihin.


Tämän modulaarisen rakenteen ansiosta LDK voi toimia erilaisilla alustoilla ja skenaarioissa, jotka olisivat haasteellisia perinteisille Lightning-solmuille. Mobiilisovellukset, verkkoselaimet, sulautetut laitteet ja erikoislaitteistot voivat kaikki hyödyntää LDK:n komponentteja tavalla, joka sopii niiden ainutlaatuisiin rajoituksiin ja vaatimuksiin. Kirjaston arkkitehtuuri varmistaa, että kehittäjät voivat luoda Lightning-yhteensopivia sovelluksia lukkiutumatta ennalta määrättyihin toimintamalleihin tai järjestelmäriippuvuuksiin.


### LDK:n käyttötapaukset ja alustan joustavuus


LDK:n arkkitehtuurin joustavuus avaa lukuisia käyttötapauksia, jotka ulottuvat paljon perinteisiä Lightning-solmujen käyttöönottoja laajemmalle. Mobiilin wallet-kehitys on yksi kiinnostavimmista sovelluksista, jossa LDK mahdollistaa Phoenix wallet:n kaltaisten, ei-hallinnollisten Lightning-lompakoiden luomisen. Nämä mobiilitoteutukset voivat säilyttää [yksityisten avainten](https://planb.academy/resources/glossary/private-key) hallinnan käyttäjällä ja synkronoida Lightning-palveluntarjoajien (LSP) kanssa, kun ne tulevat verkkoon, mikä mahdollistaa saumattoman maksujen vastaanoton ja kanavanhallinnan myös katkonaisilla yhteyksillä.


Laitteiston turvamoduulin (HSM) integrointi on toinen LDK:n tehokas käyttötapaus. Poistamalla vain tapahtuman allekirjoitus- ja varmennuskomponentit kehittäjät voivat luoda Lightning-tietoisia allekirjoituslaitteita, jotka ymmärtävät Lightning-tapahtumien kontekstin ja vaikutukset. Tämä kyky menee pelkkää tapahtuman allekirjoittamista pidemmälle ja sisältää älykkään analyysin maksujen välittämisestä, kanavatoiminnoista ja turvallisuuskriittisistä päätöksistä. HSM voi arvioida, onko transaktio laillinen maksu, reititysoperaatio vai mahdollisesti haitallinen yritys, ja tarjota käyttäjille merkityksellisiä tietoturvaominaisuuksia.


Web-pohjaiset Lightning-sovellukset hyötyvät merkittävästi LDK:n järjestelmäkutsuttomasta suunnittelufilosofiasta. Koska WebAssembly-ympäristöissä ei ole suoraa pääsyä järjestelmäresursseihin, kuten tiedostojärjestelmiin, verkkopistorasioihin tai entropialähteisiin, LDK:n puhdas lähestymistapa mahdollistaa Lightning-toimintojen saumattoman toiminnan selainympäristöissä. Kehittäjät voivat toteuttaa mukautettuja verkkokerroksia WebSocketsin avulla ja tarjota selainyhteensopivia pysyvyys- ja satunnaislähteitä säilyttäen samalla Lightning-protokollan täyden yhteensopivuuden.


### Ydinkomponentit ja tapahtumapohjainen arkkitehtuuri


LDK:n sisäinen arkkitehtuuri perustuu useisiin keskeisiin komponentteihin, jotka toimivat yhdessä tapahtumapohjaisen järjestelmän avulla. Vertaishallintajärjestelmä huolehtii kaikesta viestinnästä muiden Lightning-solmujen kanssa, toteuttaa salausprotokollaa koskevan meluprotokollan ja hallinnoi viestirakenteita Lightning-protokollan noudattamiseksi. Tämä komponentti toimii taustalla olevasta siirtomekanismista riippumatta, joten kehittäjät voivat toteuttaa verkottumisen TCP-sokettien, WebSockettien, USB-sarjaliitäntöjen tai minkä tahansa muun kaksisuuntaisen viestintäkanavan kautta.


Kanavapäällikkö toimii Lightning-kanavatoimintojen keskuskoordinaattorina, joka tekee tiivistä yhteistyötä vertaispäällikön kanssa [kanavan](https://planb.academy/resources/glossary/payment-channel) avaamis-, sulkemis- ja maksutoimintojen toteuttamiseksi. Kun kehittäjä käynnistää kanavan avaamisen, kanavahallinta luo tarvittavat protokollaviestit ja koordinoi vertaishallinnan kanssa monivaiheisen neuvotteluprosessin. Tämä huolenaiheiden erottelu mahdollistaa selkeän abstraktion Lightning-protokollan logiikan ja verkkoviestinnän yksityiskohtien välillä.


LDK:n tapahtumajärjestelmä tarjoaa asynkronisia ilmoituksia kaikista merkittävistä toiminnoista ja tilamuutoksista. Tapahtumat kattavat koko Lightning-toimintojen kirjon, vertaisverkon yhteyksistä ja irrotuksista maksujen onnistumisiin ja epäonnistumisiin, kanavan tilan muutoksiin ja lohkoketjun vahvistuksiin. Tämän tapahtumapohjaisen lähestymistavan ansiosta sovellukset voivat reagoida asianmukaisesti Lightning-verkon toimintaan säilyttäen samalla LDK:n ydintoiminnallisuuden ja sovelluskohtaisen logiikan selkeän erottelun. Kehittäjät voivat toteuttaa mukautettuja tapahtumankäsittelijöitä, jotka päivittävät käyttöliittymiä, laukaisevat ilmoituksia tai käynnistävät jatkotoimia Lightning-verkon tapahtumien perusteella.


### Blockchain Integrointi ja tiedonhallinta


Blockchain-tiedon integrointi on yksi LDK:n abstraktiokerroksista, joka on suunniteltu niin, että siihen voidaan sisällyttää kaikki täydellisistä Bitcoin-solmuista kevyisiin mobiiliasiakkaisiin. LDK tukee kahta ensisijaista lohkoketjujen vuorovaikutustapaa, joista kumpikin on optimoitu erilaisiin resurssirajoituksiin ja toimintavaatimuksiin. Täydellinen lohkotila antaa sovelluksille, joilla on pääsy täydellisiin lohkoketjutietoihin, mahdollisuuden välittää kokonaisia lohkoja LDK:lle, mikä mahdollistaa kattavan transaktioiden seurannan ja välittömän reagoinnin asiaankuuluviin lohkoketjutapahtumiin.


Resurssirajoitteisiin ympäristöihin LDK tarjoaa suodatukseen perustuvan lähestymistavan, joka vähentää kaistanleveys- ja tallennustilavaatimuksia. Tässä tilassa LDK välittää valvontaintressinsä abstraktien rajapintojen kautta ja pyytää tiettyjen tapahtumatunnusten, [UTXO](https://planb.academy/resources/glossary/utxo):iden tai komentosarjamallien valvontaa. Sovelluskerros voi sitten toteuttaa tämän seurannan Electrum-palvelimien, lohko-eksploraattoreiden tai muiden kevyiden lohkoketjujen tietolähteiden avulla. Tämä lähestymistapa mahdollistaa sen, että mobiililompakot ja verkkosovellukset voivat ylläpitää Lightning-toiminnallisuutta vaatimatta täydellistä lohkoketjun synkronointia.


LDK:n pysyvyyskerros noudattaa samoja abstraktioperiaatteita, ja se tarjoaa sovelluksille binäärisiä datakimpaleita, jotka on tallennettava ja haettava luotettavasti. LDK käsittelee kaiken monimutkaisen sarjallistamisen ja deserialisoinnin Lightning-kanavan tilat, verkon juorutiedot ja muut kriittiset tiedot. Sovellusten on vain toteutettava luotettavat tallennusmekanismit, olipa kyseessä sitten paikalliset tiedostojärjestelmät, pilvitallennuspalvelut tai erikoistuneet tietokantajärjestelmät. Tällä suunnittelulla varmistetaan, että Lightningin tilanhallinta pysyy vankkana, mutta samalla sovellukset voivat valita tallennusratkaisut, jotka vastaavat niiden toiminnallisia vaatimuksia ja turvallisuusmalleja.


### Lisäominaisuudet ja integrointikuviot


LDK:n ominaisuudet ulottuvat Lightning Network:n ominaisuuksiin, kuten monipolkumaksuihin, reitin optimointiin ja verkon juorujen hallintaan. Reititysjärjestelmä ylläpitää kattavaa näkymää Lightning Network:n topologiasta juoruprotokollan osallistumisen kautta, mikä mahdollistaa älykkään reitin löytämisen maksuja varten. Sovellukset voivat vaikuttaa reitityspäätöksiin konfigurointiparametrien avulla, ja ne voivat jopa toteuttaa mukautetun reitityslogiikan erikoistuneita käyttötapauksia varten.


Kirjaston kielisidontajärjestelmä mahdollistaa LDK:n integroinnin useisiin ohjelmointiympäristöihin tukemalla Javaa, Kotlinia, Swiftiä, TypeScriptiä, JavaScriptiä ja C++:ta. Tämän alustarajat ylittävän yhteensopivuuden ansiosta natiivikielillä kirjoitetut mobiilisovellukset voivat sisällyttää Lightning-toiminnallisuuden säilyttäen samalla optimaaliset suorituskykyominaisuudet. Sidontajärjestelmä säilyttää LDK:n tapahtumapohjaisen arkkitehtuurin ja modulaarisen suunnittelun kaikissa tuetuissa kielissä, mikä takaa yhdenmukaisen kehittäjäkokemuksen kohdealustasta riippumatta.


Palkkioiden estimointi ja transaktiolähetykset ovat muita alueita, joilla LDK tarjoaa joustavuutta. Sovellukset voivat ottaa käyttöön mukautettuja maksujen estimointistrategioita, joissa otetaan huomioon niiden erityiset toimintamallit ja käyttäjien vaatimukset. Vastaavasti tapahtumien lähetys voidaan mukauttaa toimimaan eri Bitcoin-verkkoliitäntöjen kanssa, suorista full node-yhteyksistä kolmansien osapuolten lähetyspalveluihin. Tämä joustavuus varmistaa, että LDK-pohjaiset sovellukset voivat optimoida lohkoketjuvuorovaikutuksensa tiettyihin käyttötapauksiinsa säilyttäen samalla Lightning-protokollan noudattamisen ja turvallisuusstandardit.


## Breez sdk

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>


:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::

### Salamakehityksen haaste


Lightning-maksuja integroivien sovellusten kehittäminen on merkittävä este useimmille kehittäjille. Jotta kehittäjät voisivat luoda sovelluksen, jossa on Lightning-maksutoiminnot, heidän on oltava Lightning-asiantuntijoita ja ymmärrettävä monimutkaisia käsitteitä, kuten kanavien hallinta, likviditeetin tasapainottaminen ja verkkotopologia. Tämä asiantuntemusta koskeva vaatimus luo perustavanlaatuisen ongelman Lightningin käyttöönotolle: vaikka Lightning-verkko itsessään on toimiva ja maksut ovat luotettavia, tekninen monimutkaisuus estää laajamittaisen integroinnin jokapäiväisiin sovelluksiin.


Keskeinen haaste on kuilu sen välillä, mitä kehittäjät tarvitsevat ja mitä he haluavat toimittaa. Kehittäjät työskentelevät yleensä tiukkojen määräaikojen puitteissa ja haluavat yksinkertaisia ratkaisuja, joiden avulla he voivat keskittyä sovelluksensa ydintoimintoihin sen sijaan, että heistä tulisi maksuinfrastruktuurin asiantuntijoita. Kun Lightning-integraatio on vaikeaa, kehittäjät luonnollisesti hakeutuvat säilytysratkaisuihin, koska ne tarjoavat pienimmän vastarinnan tien. Tämä taipumus kohti säilytyspalveluja kuitenkin heikentää Bitcoin:n perustavaa laatua olevaa arvolupausta, joka perustuu muuhun kuin säilytyspalveluihin perustuvaan taloudelliseen riippumattomuuteen.


### Breez:n visio, salama kaikkialla


Breez syntyi yksinkertaisesta mutta kunnianhimoisesta visiosta: saada kaikki liittymään Lightning-verkkoon Lightning-talouden intuitiivisten käyttöliittymien avulla. Yrityksen lähestymistavassa tunnustetaan, että vaikka Lightning-verkko toimii teknisesti hyvin, se tarvitsee kipeästi käyttäjien hyväksyntää saavuttaakseen täyden potentiaalinsa. Tämä hyväksyntähaaste ulottuu yksittäisten käyttäjien lisäksi koko niiden sovellusten ja palvelujen ekosysteemiin, jotka voisivat hyötyä Lightning-integraatiosta.


Alkuperäinen Breez-sovellus osoitti tämän vision tarjoamalla käyttäjille suoraan matkapuhelimessa toimivan Lightning-solmun, joka ei ole riippuvainen huoltajuudesta. Sovellus esitteli Lightning-ominaisuuksia, kuten mikromaksujen suoratoistoa podcasteille ja myyntipistetoimintoja. Breez-sovellus paljasti kuitenkin myös kriittisen arkkitehtuurirajoituksen: mobiilisovellusten ekosysteemi ei helpota helppoa kommunikointia sovellusten välillä, mikä pakottaa kehittäjät rakentamaan kaikki Lightningiin liittyvät ominaisuudet yhteen sovellukseen sen sijaan, että erikoistuneet sovellukset voisivat hyödyntää jaettua Lightning-infrastruktuuria.


Breez-sovelluksesta saadut kokemukset johtivat ratkaisevaan oivallukseen: Lightningin käyttöönoton tulevaisuus riippuu kehittäjien voittamisesta. Jos ei-huolellisesta Lightning-integraatiosta tulee helpoin vaihtoehto kehittäjille, siitä tulee oletusvalinta. Tämä lähestymistapa tarjoaa myös lainsäädännöllisiä etuja, sillä ei-säilytettäviin ohjelmistoihin kohdistuu vähemmän lainsäädännöllisiä esteitä kuin säilytyspalveluihin, joten kehittäjien on helpompi toimittaa sovelluksiaan maailmanlaajuisesti.


### Breez SDK-arkkitehtuuri


Breez SDK tarjoaa vaihtoehtoisen lähestymistavan Lightning-toimintojen integroimiseen sovelluksiin. Sen sijaan, että jokaisen sovelluksen pitäisi käyttää omaa Lightning-solmua, SDK tarjoaa arkkitehtuurin, jossa säilytetään ei-hallinnolliset periaatteet ja yksinkertaistetaan samalla kehittäjäkokemusta. Ytimeltään SDK antaa jokaiselle loppukäyttäjälle oman henkilökohtaisen Lightning-solmun, joka toimii Greenlight-infrastruktuurissa, Blockstreamin pilvipohjaisessa Lightning-solmun hosting-palvelussa.


Tämä arkkitehtuuri ratkaisee useita kriittisiä ongelmia samanaikaisesti. Käyttäjien ei tarvitse huolehtia tietokantojen hallinnasta, palvelimen käytettävyydestä tai infrastruktuurin ylläpidosta - se olisi liian raskasta tavallisille kuluttajille. Toisin kuin perinteiset säilytysratkaisut, Greenlight ei kuitenkaan koskaan pääse käsiksi käyttäjän avaimiin. Lightning-solmu pilvessä ei voi suorittaa mitään toimintoja ilman aktiivisesti yhdistettyä sovellusta, joka voi allekirjoittaa tapahtumia ja viestejä. Tämä rakenne säilyttää itsesäilytyksen turvallisuushyödyt ja poistaa samalla toiminnallisen monimutkaisuuden.


SDK tukee myös yhteentoimivuutta. Useat sovellukset voivat muodostaa yhteyden saman käyttäjän Lightning-solmuun käyttämällä samaa seed-lauseketta, jolloin käyttäjät voivat ylläpitää yhtä Lightning-saldoa eri erikoissovelluksissa. Käyttäjällä voi esimerkiksi olla sekä yleinen Lightning wallet -sovellus että erikoistunut podcasting-sovellus, jotka molemmat käyttävät samoja varoja ja Lightning-kanavia. Tämä arkkitehtuuri mahdollistaa kohdennettujen, erikoistuneiden sovellusten kehittämisen samalla kun säilytetään yhtenäinen rahoitusinfrastruktuuri.


### Salamapalveluntarjoajat ja Just-in-Time likviditeetti


Kriittinen osa Breez SDK:ta on sen integrointi Lightning-palveluntarjoajiin (LSP), jotka toimivat analogisesti Internet-palveluntarjoajien kanssa, mutta Lightning-verkossa. LSP:t ratkaisevat yhden Lightningin monimutkaisimmista haasteista: likviditeetinhallinnan. Lightning-kanavissa varat voivat virrata vain niihin suuntiin, joissa on likviditeettiä, kuten abakuksen helmet, jotka voivat liikkua vain siellä, missä on tilaa.


SDK toteuttaa "just-in-time"-kanavat LSP:iden kautta, jolloin likviditeettiä hallitaan automaattisesti ilman käyttäjän toimenpiteitä. Kun käyttäjän on saatava maksu, mutta hänellä ei ole riittävästi likviditeettiä, LSP avaa automaattisesti uuden Lightning-kanavan heti, kun maksu saapuu. Tämä prosessi tapahtuu saumattomasti taustalla, mikä varmistaa, että käyttäjät voivat aina vastaanottaa maksuja ymmärtämättä taustalla olevia kanavamekanismeja.


Tämä LSP-integraatio ulottuu pelkkää likviditeetinhallintaa pidemmälle. SDK sisältää kattavan Lightning-toiminnallisuuden: sisäänrakennetut vartiotornipalvelut turvallisuuden takaamiseksi, on-chain-yhteentoimivuuden submarine swapien avulla, fiat-asemat MoonPayn kaltaisten palveluiden kautta ja tuen LNURL-protokollille. Järjestelmä tarjoaa myös saumattoman varmuuskopioinnin ja palautuksen, mikä varmistaa, että käyttäjät eivät koskaan menetä pääsyä varoihinsa, vaikka infrastruktuurin tarjoajat vaihtuisivat tai eivät olisi käytettävissä.


### Toteutus ja kehittäjäkokemus


Breez SDK:ssa kehittäjäkokemus on etusijalla kattavan, akut sisältävän lähestymistavan ansiosta. SDK tarjoaa sidoksia useille ohjelmointikielille, kuten Rust, Swift, Kotlin, Python, Go, React Native, Flutter ja C#, jotta kehittäjät voivat integroida Lightning-maksuja haluamillaan kehitystyökaluilla. Arkkitehtuuri abstrahoi Lightningin monimutkaisuuden API:iden avulla säilyttäen samalla Lightning-verkon turvallisuuden.


Keskeiset osat toimivat yhdessä tämän yksinkertaistetun kokemuksen tarjoamiseksi. Syötteen jäsentäjä käsittelee automaattisesti eri maksumuodot ja määrittää, onko merkkijono [lasku](https://planb.academy/resources/glossary/invoice-lightning), LNURL tai muu maksutapa, ja ohjaa sen asianmukaiseen käsittelytoimintoon. Integroitu allekirjoittaja hallinnoi kaikkia salausoperaatioita taustalla, kun taas swapper käsittelee on-chain-vuorovaikutukset läpinäkyvästi. Tämän rakenteen ansiosta kehittäjät voivat keskittyä sovelluksensa ainutlaatuiseen arvolupaukseen sen sijaan, että heistä tulisi Lightning-infrastruktuurin asiantuntijoita.


SDK:n luotettava arkkitehtuuri varmistaa, että vaikka Greenlight voi tarkkailla kanavan tiloja ja reititystietoja, se ei voi käyttää käyttäjän varoja tai suorittaa luvattomia toimintoja. Käyttäjät säilyttävät täydellisen määräysvallan yksityisiin avaimiinsa, jotka eivät koskaan poistu heidän laitteistaan. Tämä lähestymistapa edustaa tarkkaan harkittua kompromissia toiminnan yksinkertaisuuden ja yksityisyydensuojan välillä, ja se tarjoaa käytännöllisen väylän Lightningin valtavirtaistamiselle säilyttäen samalla Bitcoin:n keskeiset periaatteet, jotka koskevat taloudellista riippumattomuutta.


## LDK vs. Breez SDK

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>


:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::

### Lightning Development Kitin (LDK) rajoitusten ymmärtäminen


Lightning Development Kit on kokoelma Rust-kirjastoja, jotka on suunniteltu tarjoamaan kehittäjille joustavuutta Lightning Network-sovelluksia rakennettaessa. Tähän joustavuuteen liittyy kuitenkin merkittäviä toteutushaasteita, jotka tulivat ilmi Lipa:n reaalimaailman kehitystyön aikana. LDK:n matalan tason luonne tarkoittaa, että kehittäjien on käsiteltävä itsenäisesti lukuisia monimutkaisia tehtäviä, verkkograafin synkronoinnista maksujen reitityksen optimointiin. Vaikka tämä lähestymistapa tarjoaa täydellisen hallinnan Lightning-toteutukseen, se vaatii huomattavia kehitysresursseja ja syvällistä teknistä asiantuntemusta, jotta saavutetaan tuotantokelpoinen luotettavuus.


Yksi kriittisimmistä LDK:sta puuttuvista ominaisuuksista oli tuki LNURL:lle, laajalti hyväksytylle standardille, joka yksinkertaistaa Lightning Network-vuorovaikutusta loppukäyttäjille. Lisäksi ankkurilähtöjen puuttuminen aiheutti vakavia toiminnallisia haasteita erityisesti korkeiden maksujen ympäristöissä. Anchor-ulostulot ratkaisevat Lightning-kanavien pakkosulkemiseen liittyvän perusongelman: kun verkkomaksut nousevat dramaattisesti, kanavia, joissa on ennalta määritetyt maksut, voi olla mahdotonta sulkea yksipuolisesti, koska ennalta asetettu maksu ei enää riitä tapahtuman vahvistamiseen. Tämä rajoitus osoittautui erityisen ongelmalliseksi mobiilissa wallet-sovelluksissa, joissa käyttäjät saattavat hylätä wallet:n koordinoimatta yhteistoiminnallisia kanavasulkemisia, jolloin varat saattavat jäädä maksuhuippujen aikana jumiin.


LDK:n suhteellinen kypsymättömyys ilmeni myös epäluotettavana maksujen reitityksenä, mikä on kriittinen ongelma kaikille Lightning-sovelluksille. Vaikka LDK on teknisesti hyvä toteutus, LDK:n laaja soveltamisala yleisenä ratkaisuna teki yksittäisten ongelmien nopeasta ratkaisemisesta haastavaa. Kehitystiimi huomasi käyttävänsä huomattavan paljon aikaa reititysongelmien vianmääritykseen ja sellaisten ominaisuuksien toteuttamiseen, jotka ihanteellisimmassa tapauksessa olisi käsiteltävä kirjastotasolla, mikä vaikutti viime kädessä kehitystyön nopeuteen ja käyttäjäkokemuksen laatuun.


### Breez SDK:n ja Greenlightin etujen löytäminen


Siirtyminen Breez SDK:hon merkitsi muutosta arkkitehtuurisessa lähestymistavassa, kun siirryttiin itse hallinnoitavasta Lightning-solmusta pilvipohjaiseen ratkaisuun, joka perustuu Blockstreamin Greenlight-palveluun. Tämä muutos ratkaisi välittömästi useita LDK-toteutuksessa havaittuja kriittisiä ongelmakohtia. Merkittävin parannus tapahtui maksujen luotettavuudessa, mikä johtui ensisijaisesti Greenlightin kyvystä ylläpitää aina ajantasaista verkon kuvaajaa. Toisin kuin perinteisissä mobiilissa Lightning-toteutuksissa, joissa verkkotiedot on synkronoitava sovelluksen käynnistyessä, Greenlight-solmut toimivat jatkuvasti pilvessä, ylläpitävät reaaliaikaista verkkotietoisuutta ja toimittavat välittömästi täydelliset graafitiedot, kun käyttäjät muodostavat yhteyden.


Tässä arkkitehtuurissa hyödynnetään taistelussa testattua Core Lightning (CLN) -toteutusta, joka on reitittänyt maksuja menestyksekkäästi jo vuosia yhtenä alkuperäisistä Lightning Network-toteutuksista. CLN:n kertyneen kokemuksen ja todistetun luotettavuuden ansiosta vakaus parani välittömästi verrattuna nuorempaan LDK-hankkeeseen. Kun käyttäjät aktivoivat Greenlight-käyttöön tarkoitetun wallet:nsa, ne perivät välittömästi jatkuvasti toimivan Lightning-solmun täyden verkkotuntemuksen ja reititysominaisuudet, mikä poistaa synkronointiviiveet ja reititykseen liittyvät epävarmuustekijät, jotka vaivasivat aiempaa toteutusta.


Breez SDK:n mielipidekeskeinen suunnittelufilosofia oli hyödyllinen wallet:n kehityksessä. Yleisen Lightning-työkalupaketin sijaan Breez keskittyy erityisesti wallet-loppukäyttäjien wallet-sovelluksiin, jolloin kehitystiimi voi keskittyä luomaan kattavia ratkaisuja tähän erityiseen käyttötarkoitukseen. Tämä kohdennettu lähestymistapa mahdollisti sen, että Breez integroi keskeiset palvelut suoraan SDK:hon, mukaan lukien Lightning Service Provider (LSP) -toiminnot, joiden avulla käyttäjät voivat vastaanottaa maksuja heti wallet:n asennuksen jälkeen ilman manuaalisia kanavien avaamismenettelyjä.


### Kattavat ominaisuudet ja käyttäjäkokemuksen parannukset


Breez SDK:n integroitu lähestymistapa ulottuu Lightningin perustoimintoja pidemmälle ja sisältää käyttäjäkokemusta parantavia ominaisuuksia. Sisäänrakennettu LSP-integraatio poistaa perinteisen esteen, joka edellyttää käyttäjiltä kanavanhallinnan ymmärtämistä, ja mahdollistaa uusien wallet-asennusten välittömän maksujen vastaanoton. Tämä käyttöönottoprosessi auttaa valtavirran omaksumisessa, sillä käyttäjät voivat aloittaa Lightning-maksujen vastaanottamisen ilman teknistä osaamista tai käyttöönottomenettelyjä.


Ketjussa tapahtuva swap-toiminto tarjoaa toisen kerroksen käyttäjäkokemuksen optimointiin mahdollistamalla yhtenäisen saldon esittämisen käyttäjille. Sen sijaan, että käyttäjät joutuisivat ymmärtämään Lightningin ja on-chain Bitcoin:n välisen eron, swap-palvelu mahdollistaa automaattisen muuntamisen näiden kerrosten välillä tarpeen mukaan. Kun käyttäjien on suoritettava on-chain-maksuja, järjestelmä voi vaihtaa Lightning-varat saumattomasti on-chain Bitcoin-varoiksi kulissien takana, jolloin illuusio yhdestä, likvidistä saldosta säilyy, mutta tekninen monimutkaisuus hoidetaan sisäisesti.


SDK:n tuki nollakanavavarauksille ratkaisee merkittävän käyttäjäkokemuksen haasteen perinteisissä Lightning-toteutuksissa. Kanavavaraukset estävät yleensä käyttäjiä käyttämästä koko näytettyä saldoaan, mikä aiheuttaa hämmennystä, kun maksut epäonnistuvat, vaikka varoja on näennäisesti riittävästi. Poistamalla nämä varaukset Breez mahdollistaa sen, että käyttäjät voivat käyttää koko näytetyn saldonsa, vaikka tämä edellyttääkin LSP:ltä lisäriskin ottamista. Tämä kompromissi on esimerkki Breez:n käyttäjäkeskeisestä lähestymistavasta, jossa palveluntarjoajat ottavat vastatakseen teknisestä monimutkaisuudesta ja riskistä luodakseen intuitiivisen käyttäjäkokemuksen.


Lisäominaisuudet, kuten LNURL-tuki, valuuttakurssipalvelut ja usean laitteen synkronointi, osoittavat SDK:n kattavan lähestymistavan wallet-kehitykseen. Pilvipohjaisen arkkitehtuurin ansiosta käyttäjät voivat käyttää Lightning-solmua useista laitteista tai sovelluksista, ja Breez hoitaa tilan synkronoinnin näiden eri yhteyspisteiden välillä. Tulevaisuuden etenemissuunnitelman kohtiin kuuluvat spend-all-toiminnallisuus wallet:n täydellistä tyhjennystä varten, dynaamisen kanavanhallinnan liittäminen ja kilpailevien LSP-palvelujen markkinapaikka terveen kilpailun aikaansaamiseksi palveluntarjonnassa.


### Kompromissien ja keskittämiseen liittyvien huolenaiheiden arviointi


Siirtyminen Breez SDK:hon ja Greenlightiin tuo mukanaan tärkeitä keskittämisvaihtoehtoja, joita on harkittava huolellisesti Bitcoin:n hajautusperiaatteiden yhteydessä. Pilvipohjainen arkkitehtuuri tarkoittaa, että käyttäjien Lightning-solmut toimivat Blockstreamin infrastruktuurissa, mikä luo riippuvuuksia sekä Greenlightin jatkuvasta toiminnasta että Breez:n jatkuvasta kehityksestä. Tämä keskittäminen ulottuu pelkkää mukavuutta pidemmälle, sillä se saattaa vaikuttaa käyttäjien kykyyn saada varoja takaisin, jos palvelut eivät ole käytettävissä tai jos sensuuria esiintyy.


Elvytysskenaariot aiheuttavat erityisiä haasteita tässä arkkitehtuurissa. Vaikka käyttäjät säilyttävät yksityisten avaintensa hallinnan, varojen käyttäminen ilman Greenlightin infrastruktuuria vaatisi teknistä asiantuntemusta riippumattomien Core Lightning -solmujen käynnistämiseksi ja kanavien tilojen palauttamiseksi. Yksittäisille käyttäjille tämä palautusprosessi osoittautuisi todennäköisesti liian monimutkaiseksi, ja jopa wallet-palveluntarjoajilla olisi huomattavia haasteita siirtää kokonaisia käyttäjäkuntia vaihtoehtoiseen infrastruktuuriin, jos Greenlight-palvelut lopetettaisiin.


Arkkitehtuurimuutoksen myötä myös yksityisyysnäkökohdat muuttuvat. Pilvipohjainen reititys tarkoittaa, että Greenlight saa mahdollisesti näkyvyyttä maksujen kohteisiin, kun taas aiemmat vain LSP-arkkitehtuurit rajoittivat tietovuodon maksujen määriin ja ajoitukseen. Invoice:n tuottaminen pilvipalvelussa laajentaa entisestään potentiaalista tietojen paljastumista, sillä käyttämättömät laskut, jotka aiemmin pysyivät yksityisinä käyttäjän laitteissa, kulkevat nyt Blockstreamin infrastruktuurin kautta.


Näistä keskittämiseen liittyvistä huolenaiheista huolimatta käytännön hyödyt ovat usein teoreettisia riskejä suuremmat monissa käyttötapauksissa. Parempi luotettavuus, kattava ominaisuusvalikoima ja parempi käyttäjäkokemus antavat wallet-kehittäjille mahdollisuuden keskittyä sovelluskerroksen innovaatioihin salamainfrastruktuurin hallinnan sijaan. Tämä työnjako kuvastaa kypsyvää ekosysteemiä, jossa erikoistuneet palveluntarjoajat hoitavat monimutkaisia teknisiä haasteita, jolloin sovelluskehittäjät voivat keskittyä käyttäjäkokemukseen ja liiketoimintalogiikkaan. Tärkeintä on ymmärtää nämä kompromissit selkeästi ja tehdä tietoon perustuvia päätöksiä, jotka perustuvat tiettyihin käyttötapausten vaatimuksiin ja riskinsietokykyyn.




# Viimeinen jakso

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>



## Arvostelut & arvostelut

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>

## Päätelmä

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>