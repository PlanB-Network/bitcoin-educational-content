---
name: RGB CLI
description: Miten luon ja vaihdan älykkäitä sopimuksia RGB:ssä?
---
![cover](assets/cover.webp)

Tässä opetusohjelmassa seuraamme sopimuksen kirjoittamista vaihe vaiheelta käyttäen LNP/BP-yhdistyksen luomaa komentorivityökalua `rgb`. Tarkoituksena on näyttää, miten CLI asennetaan ja miten sitä käsitellään, miten kootaan skeema, tuodaan rajapinta ja rajapintatoteutus, ja sitten annetaan RGB-varanto. Tarkastelemme myös taustalla olevaa logiikkaa, mukaan lukien kääntäminen ja tilan validointi. Tämän opetusohjelman lopussa sinun pitäisi pystyä toistamaan prosessi ja luomaan omat RGB-sopimuksesi.

## RGB-protokollan muistutus

RGB on protokolla, joka toimii Bitcoinin päällä ja jäljittelee älykkäiden sopimusten toimintoja ja digitaalisten omaisuuserien hallintaa kuormittamatta liikaa lohkoketjua, johon se perustuu. Toisin kuin perinteiset ketjussa olevat älykkäät sopimukset (kuten esimerkiksi Ethereumissa), RGB perustuu "*Client-side validation*" -järjestelmään: suurin osa tiedoista ja tilahistoriasta vaihdetaan ja tallennetaan yksinomaan osallistujien kesken, kun taas Bitcoinin lohkoketjussa on vain pieniä kryptografisia sitoumuksia (esimerkiksi *Tapretin* tai *Opretin* kaltaisten mekanismien avulla). RGB-protokollassa Bitcoin-lohkoketju toimii näin ollen vain aikaleimauspalvelimena ja kaksinkertaisen kulutuksen suojausjärjestelmänä.

RGB-sopimus on rakenteeltaan kuin evolutiivinen tilakone. Se alkaa Genesiksellä, jossa määritellään alkutila (jossa kuvataan esimerkiksi tarjonta, ticker tai muut metatiedot) tiukasti tyypitetyn ja kootun skeeman mukaisesti. Tämän jälkeen sovelletaan tilasiirtymiä ja tarvittaessa tilalaajennuksia tämän tilan muuttamiseksi tai laajentamiseksi. Jokaiseen operaatioon, olipa kyse sitten vaihdettavissa olevien omaisuuserien siirtämisestä (RGB20) tai ainutlaatuisten omaisuuserien luomisesta (RGB21), liittyy *Kertakäyttösinettejä*. Nämä yhdistävät Bitcoin UTXO:t ketjun ulkopuolisiin tiloihin ja estävät kaksinkertaisen kulutuksen varmistaen samalla luottamuksellisuuden ja skaalautuvuuden.

Jos haluat lisätietoja RGB-protokollan toiminnasta, suosittelen, että osallistut tälle kattavalle koulutuskurssille:

https://planb.network/courses/csv402
RGB:n sisäinen logiikka perustuu Rust-kirjastoihin, jotka voit kehittäjänä tuoda projekteihisi hallitsemaan *asiakaspuolen validointiosuutta*. Lisäksi LNP/BP-tiimi työstää sidoksia muille kielille, mutta tätä ei ole vielä viimeistelty. Lisäksi muut tahot, kuten Bitfinex, kehittävät omia integraatiopinojaan, mutta puhumme niistä toisessa opetusohjelmassa. Toistaiseksi `rgb` CLI on virallinen referenssi, vaikka se onkin vielä suhteellisen hiomaton.

## Rgb CLI -työkalun asennus ja esittely

Pääkomennon nimi on yksinkertaisesti `rgb`. Se on suunniteltu muistuttamaan `git`:iä, ja siinä on joukko alakomentoja sopimusten käsittelyyn, niiden kutsumiseen, varojen antamiseen ja niin edelleen. Bitcoin-lompakkoa ei ole tällä hetkellä integroitu, mutta se tulee olemaan tulevassa versiossa (0.11). Tämä seuraava versio antaa käyttäjille mahdollisuuden luoda ja hallita lompakoitaan (kuvaajien avulla) suoraan `rgb`:stä, mukaan lukien PSBT:n luominen, yhteensopivuus ulkoisen laitteiston (esim. laitteistolompakon) kanssa allekirjoittamista varten ja yhteentoimivuus Sparrow'n kaltaisten ohjelmistojen kanssa. Tämä yksinkertaistaa koko omaisuuserien liikkeeseenlasku- ja siirtoskenaariota.

### Asennus Cargon kautta

Asennamme työkalun Rustiin :

```bash
cargo install rgb-contracts --all-features
```

(Huomaa: crate on nimeltään `rgb-contracts`, ja asennetun komennon nimi on `rgb`.) Jos `rgb`-niminen crate oli jo olemassa, on voinut tapahtua törmäys, siksi nimi)

Asennus kokoaa suuren määrän riippuvuuksia (esim. komentojen jäsentely, Electrumin integrointi, nollatietotodistusten hallinta jne.).

Kun asennus on valmis, :

```bash
rgb
```

Käynnistämällä `rgb` (ilman argumentteja) saat näkyviin luettelon käytettävissä olevista alakomennoista, kuten `interfaces`, `schema`, `import`, `export`, `issue`, `invoice`, `transfer` jne. Voit vaihtaa paikallisen tallennushakemiston (kätkö, jossa säilytetään kaikki lokit, kaaviot ja toteutukset), valita verkon (testnet, mainnet) tai konfiguroida Electrum-palvelimen.

![RGB-CLI](assets/fr/01.webp)

### Ensimmäinen yleiskatsaus valvontaan

Kun suoritat seuraavan komennon, näet, että `RGB20`-rajapinta on jo oletusarvoisesti integroitu:

```bash
rgb interfaces
```

Jos tätä käyttöliittymää ei ole integroitu, kloonaa :

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Kokoa se:

```bash
cargo run
```

Tuo sitten haluamasi käyttöliittymä:

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-CLI](assets/fr/02.webp)

Meille on kuitenkin kerrottu, että mitään skeemaa ei ole vielä tuotu ohjelmistoon. Kätköissä ei myöskään ole sopimusta. Voit nähdä sen suorittamalla komennon :

```bash
rgb schemata
```

Voit sitten kloonata arkiston hakeaksesi tiettyjä kaavioita:

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-CLI](assets/fr/03.webp)

Tämä arkisto sisältää hakemistossaan `src/` useita Rust-tiedostoja (esimerkiksi `nia.rs`), jotka määrittelevät skeemat (NIA tarkoittaa "*Non Inflatable Asset*", UDA tarkoittaa "*Unique Digital Asset*" jne.). Kääntääksesi voit sitten ajaa :

```bash
cd rgb-schemata
cargo run
```

Tämä tuottaa useita `.rgb`- ja `.rgba`-tiedostoja, jotka vastaavat koottuja kaavioita. Löydät esimerkiksi tiedoston `NonInflatableAsset.rgb`.

### Skeeman ja rajapinnan toteutuksen tuominen

Voit nyt tuoda kaavion `rgb` -ohjelmaan:

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-CLI](assets/fr/04.webp)

Tämä lisää sen paikalliseen kätköön. Jos suoritamme seuraavan komennon, näemme, että skeema näkyy nyt:

```bash
rgb schemata
```

## Sopimuksen luominen (myöntäminen)

Uuden omaisuuserän luomiseen on kaksi lähestymistapaa:


- Käytämme joko skriptiä tai Rust-koodia, joka luo sopimuksen täyttämällä skeeman kentät (globaali tila, omistetut tilat jne.) ja tuottaa `.rgb`- tai `.rgba`-tiedoston;
- Tai käytä suoraan `issue`-alikomentoa ja YAML- (tai TOML-) tiedostoa, jossa kuvataan tunnuksen ominaisuudet.

Löydät esimerkkejä Rustista kansiosta `examples`, jotka havainnollistavat, miten rakennat `ContractBuilderin`, täytät `globaalin tilan` (omaisuuserän nimi, ticker, tarjonta, päivämäärä jne.), määrittelet Owned State (mihin UTXO:han se on osoitettu), ja sitten kokoat kaiken tämän *sopimuslähetykseksi*, jonka voit viedä, validoida ja tuoda kätköön.

Toinen tapa on muokata manuaalisesti YAML-tiedostoa, jotta voit mukauttaa `ticker`, `name`, `supply` ja niin edelleen. Oletetaan, että tiedoston nimi on `RGB20-demo.yaml`. Voit määrittää :


- `spec`: ticker, name, precision ;
- `terms`: kenttä oikeudellisia huomautuksia varten ;
- `issuedSupply` : liikkeeseen laskettujen kuponkien määrä ;
- `assignments`: ilmoittaa kertakäyttöisen sinetin (*sinetin määritelmä*) ja lukitsemattoman määrän.

Tässä on esimerkki luotavasta YAML-tiedostosta:

```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-CLI](assets/fr/05.webp)

Suorita sitten komento :

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-CLI](assets/fr/06.webp)

Minun tapauksessani yksilöllinen skeematunniste (joka suljetaan lainausmerkkien sisään) on `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k`, enkä ole laittanut mitään myöntäjää. Tilaukseni on siis :

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

Jos et tiedä skeematunnusta, suorita komento :

```bash
rgb schemata
```

CLI vastaa, että uusi sopimus on tehty ja lisätty kätköön. Jos kirjoitamme seuraavan komennon, näemme, että nyt on olemassa uusi sopimus, joka vastaa juuri tehtyä sopimusta:

```bash
rgb contracts
```

![RGB-CLI](assets/fr/07.webp)

Seuraavalla komennolla näytetään sitten globaalit tilat (nimi, ticker, tarjonta...) ja luettelo Owned States eli allokaatiot (esimerkiksi 1 miljoona `PBN`-merkkiä, jotka on määritelty UTXO:ssa `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).

```bash
rgb state '<ContractId>'
```

![RGB-CLI](assets/fr/08.webp)

## Vienti, tuonti ja validointi

Jos haluat jakaa tämän sopimuksen muiden käyttäjien kanssa, se voidaan viedä kätköstä :

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-CLI](assets/fr/09.webp)

Tiedosto `myContractPBN.rgb` voidaan siirtää toiselle käyttäjälle, joka voi lisätä sen kätköönsä komennolla :

```bash
rgb import myContractPBN.rgb
```

Jos kyseessä on yksinkertainen *sopimuslähetys*, saamme tuonnin yhteydessä viestin "`Importing consignment rgb`". Jos kyseessä on laajempi *tilasiirtolähetys*, komento on erilainen (`rgb accept`).

Voit varmistaa validiteetin myös käyttämällä paikallista validointitoimintoa. Voit esimerkiksi suorittaa :

```bash
rgb validate myContract.rgb
```

### Kätkön käyttö, todentaminen ja näyttäminen

Muistutettakoon, että kätkö on paikallinen inventaario skeemoista, rajapinnoista, toteutuksista ja sopimuksista (Genesis + siirtymät). Joka kerta kun suoritat "import", lisäät elementin kätköön. Tätä kätköä voi tarkastella yksityiskohtaisesti komennolla :

```bash
rgb dump
```

![RGB-CLI](assets/fr/10.webp)

Tämä luo kansion, jossa on tiedot koko kätköstä.

## Siirto ja PSBT

Jotta voit suorittaa siirron, sinun on manipuloitava paikallista Bitcoin-lompakkoa `Tapret`- tai `Opret`-sitoumusten hallitsemiseksi.

### Luo lasku

Useimmissa tapauksissa sopimuksen osapuolten (esim. Alice ja Bob) välinen vuorovaikutus tapahtuu laskun laatimisen kautta. Jos Alice haluaa Bobin suorittavan jotakin (tokenin siirto, uudelleenjulkaisu, toiminta DAO:ssa jne.), Alice luo laskun, jossa hän antaa yksityiskohtaiset ohjeet Bobille. Meillä on siis :


- Alice** (laskun laatija) ;
- Bob** (joka vastaanottaa ja suorittaa laskun).

Toisin kuin muissa ekosysteemeissä, RGB-lasku ei rajoitu maksun käsitteeseen. Siihen voidaan sisällyttää mikä tahansa sopimukseen liittyvä pyyntö: avaimen peruuttaminen, äänestäminen, kaiverruksen (*kaiverrus*) luominen NFT:hen jne. Vastaava toiminto voidaan kuvata sopimuksen käyttöliittymässä. Vastaava toiminto voidaan kuvata sopimuksen käyttöliittymässä.

Seuraava komento luo RGB-laskun:

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

Kanssa :


- `$CONTRACT`: Sopimuksen tunniste (*ContractId*) ;
- `$INTERFACE`: käytettävä rajapinta (esim. `RGB20`) ;
- `$ACTION`: käyttöliittymässä määritellyn toiminnon nimi (yksinkertaisessa vaihdettavissa olevan tokenin siirrossa tämä voi olla "Transfer"). Jos rajapinta tarjoaa jo oletustoiminnon, sitä ei tarvitse syöttää tähän uudelleen;
- `$STATE`: siirrettävä tilatieto (esimerkiksi polettien määrä, jos siirretään vaihdettava poletti);
- `$SEAL`: edunsaajan (Alicen) kertakäyttösinetti eli nimenomainen viittaus UTXO:hon. Bob käyttää tätä tietoa todistajan transaktion rakentamiseen, ja vastaava tuloste kuuluu sitten Alicelle (*sokeassa UTXO:ssa* tai salaamattomassa muodossa).

Esimerkiksi seuraavilla komennoilla

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

CLI luo laskun kuten :

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

Se voidaan lähettää Bobille mitä tahansa kanavaa (tekstiä, QR-koodia jne.) pitkin.

### Siirron tekeminen

Siirtääksesi tästä laskusta :


- Bobilla (joka pitää rahakkeita kätköissään) on Bitcoin-lompakko. Hänen on valmisteltava Bitcoin-tapahtuma (PSBT:n muodossa, esim. `tx.psbt`), jossa kulutetaan UTXO:t, joissa tarvittavat RGB-tavaramerkit sijaitsevat, sekä yksi UTXO valuuttaa (vaihtoa) varten;
- Bob suorittaa seuraavan komennon:

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- Tämä tuottaa tiedoston `consignment.rgb`, joka sisältää :
 - Siirtymähistoria todistaa Alicelle, että merkit ovat aitoja;
 - Uusi siirtymä, joka siirtää merkkejä Alicen kertakäyttöiseen sinettiin ;
 - Todistajatapahtuma (allekirjoittamaton).
- Bob lähettää tämän `consignment.rgb`-tiedoston Alicelle (sähköpostitse, jakopalvelimella tai RGB-RPC-protokollalla, Stormilla jne.);
- Alice vastaanottaa `consignment.rgb` ja hyväksyy sen omaan kätköönsä :

```bash
alice$ rgb accept consignment.rgb
```


- CLI tarkistaa siirtymän pätevyyden ja lisää sen Alicen kätköön. Jos se on virheellinen, komento epäonnistuu yksityiskohtaisten virheilmoitusten kera. Muussa tapauksessa se onnistuu ja ilmoittaa, että esimerkkitransaktiota ei ole vielä lähetetty Bitcoin-verkkoon (Bob odottaa Alicen vihreää valoa);
- Vahvistukseksi komento "Accept" palauttaa allekirjoituksen (*maksulappu*), jonka Alice voi lähettää Bobille osoittaakseen, että hän on vahvistanut *lähetyksen* ;
- Bob voi sitten allekirjoittaa ja julkaista (`--julkaista`) Bitcoin-tapahtumansa:

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- Heti kun tämä transaktio on vahvistettu ketjussa, omaisuuserän omistusoikeus katsotaan siirtyneen Alicelle. Alicen lompakko, joka valvoo transaktion louhintaa, näkee uuden Owned State -tilan ilmestyvän kätköönsä.

Tiedät nyt, miten RGB-sopimus tehdään ja siirretään. Jos löysit tämän opetusohjelman hyödylliseksi, olisin hyvin kiitollinen, jos laittaisit vihreän peukalon alle. Voit myös vapaasti jakaa tämän artikkelin sosiaalisissa verkostoissa. Kiitos paljon!

Suosittelen myös tätä toista opetusohjelmaa, jossa selitän, miten RGB-yhteensopiva Lightning-solmu käynnistetään, jotta voit vaihtaa rahakkeita lähes välittömästi:

https://planb.network/tutorials/node/rgb/rln-ffc02528-329b-4e16-bd83-873d0299feea