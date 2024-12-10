---
name: Samourai Wallet - Palautus
description: Kuinka palauttaa bitcoinit, jotka ovat jumissa Samourai Walletissa?
---
![kansi](assets/cover.webp)

Samourai Walletin perustajien pidätyksen ja heidän palvelimiensa takavarikoinnin jälkeen 24. huhtikuuta, jotkin sovelluksen toiminnoista ovat nyt toimimattomia, ja käyttäjät, joilla ei ole omaa Dojoa, eivät enää voi lähettää transaktioita.

Useiden käyttäjien auttamisen jälkeen bitcoiniensa palauttamisessa viime päivinä, uskon kohdanneeni suurimman osan ongelmista, jotka voivat ilmetä Samourai Walletin palautuksen aikana. Tämän vuoksi tämä opas alkaa tilannekatsauksella tunnistaaksemme toiminnot, jotka ovat edelleen käytettävissä ja ne, jotka eivät enää ole saatavilla Samourai Walletin ekosysteemissä ja tämän tapahtuman vaikutuksesta kärsineessä ohjelmistossa. Seuraavaksi etenemme askel askeleelta palauttamaan Samourai Walletin käyttäen Sparrow Wallet -ohjelmistoa. Tarkastelemme kaikkia mahdollisia esteitä, jotka kohtaamme tässä prosessissa ja näemme ratkaisuja niiden selvittämiseen. Lopuksi viimeisessä osassa saat tietää mahdollisista riskeistä yksityisyydellesi palvelimien takavarikon seurauksena.

*Suuri kiitos [@Louferlou](https://twitter.com/Louferlou), joka on auttanut useita käyttäjiä heidän palautuksessaan ja jakanut kokemuksiaan minulle, ja joka on myös osallistunut testaukseen määrittääkseen mikä on vielä toiminnassa.*

## Toimiiko Samourai Wallet vielä?

Kyllä, **Samourai Wallet -sovellus toimii yhä**, mutta tietyin ehdoin.

Ensinnäkin on välttämätöntä, että sovellus oli aiemmin asennettu älypuhelimeesi. Google Play Store on poistanut sovelluksen, ja APK oli isännöity takavarikoidulla verkkosivustolla. Siksi Samourain asentaminen on tällä hetkellä monimutkaista. Saatat löytää APK-tiedostoja verkosta, mutta neuvon olemaan lataamatta niitä, ellet ole varma lähteestä.

Koska Samourai Wallet -sivua ei enää ole saatavilla Google Play Storessa, automaattisia päivityksiä ei ole mahdollista poistaa käytöstä. Jos sovellus palaa latausalustoille, olisi viisasta **poistaa automaattiset päivitykset käytöstä** kunnes lisätietoja tapauksen kehittymisestä on saatavilla.

Jos Samourai Wallet on jo asennettu älypuhelimeesi, sinun pitäisi edelleen pystyä käyttämään sovellusta. Samourai-lompakon toimintojen käyttämiseksi on olennaista yhdistää Dojo. Aiemmin käyttäjät ilman henkilökohtaista Dojoa riippuivat Samourain palvelimista päästäkseen käsiksi Bitcoin-lohkoketjun tietoihin ja lähettääkseen transaktioita. Näiden palvelimien takavarikon myötä sovellus ei enää pääse käsiksi näihin tietoihin.
Jos sinulla ei ollut yhdistettyä Dojoa aiemmin, mutta sinulla on se nyt, voit asettaa sen käyttöön uudelleen käyttääksesi Samourai-sovellustasi. Tämä edellyttää varmuuskopioidesi tarkistamista, lompakon poistamista (lompakko, ei sovellus) ja lompakon palauttamista yhdistämällä Dojosi sovellukseen. Lisätietoja näistä vaiheista löydät [tästä oppaasta, osiossa "_Valmistele Samourai Walletisi_": COINJOIN - DOJO](https://planb.network/en/tutorials/privacy/coinjoin-dojo).
Jos Samourai-sovelluksesi oli jo yhdistetty omaan Dojoosi, lompakon osa toimii sinulle täydellisesti. Voit edelleen nähdä saldosi ja lähettää transaktioita. Huolimatta kaikesta tapahtuneesta, uskon, että Samourai Wallet pysyy parhaana mobiililompakko-ohjelmistona tällä hetkellä. Henkilökohtaisesti aion jatkaa sen käyttöä.
Pääongelma, jonka saatat kohdata, on Whirlpool-tilien saavuttamattomuus sovelluksesta. Yleensä Samourai yrittää luoda yhteyden Whirlpool CLI:si ja aloittaa coinjoin-syklit ennen kuin se antaa sinulle pääsyn näihin tileihin. Koska tämä yhteys ei kuitenkaan ole enää mahdollinen, sovellus jatkaa loputtomasti etsintää antamatta koskaan pääsyä Whirlpool-tilisiin. Tässä tapauksessa voit palauttaa nämä tilit toisella lompakko-ohjelmistolla pitäen samalla vain talletustilin Samouraissa.

### Mitkä työkalut ovat edelleen käytettävissä Samouraissa?

Toisaalta jotkut työkalut ovat joko kärsineet palvelimen sulkemisesta tai eivät ole lainkaan saatavilla.

Yksittäisten kulutustyökalujen osalta kaikki toimii normaalisti, edellyttäen tietysti, että sinulla on oma Dojo. Normaalit Stonewall-siirrot (ei Stonewall x2) toimivat ilman ongelmia.

Twitter-kommenteissa on korostettu, että Stonewall-siirron tarjoama yksityisyys saattaa nyt olla vähentynyt. Stonewall-siirron lisäarvo piilee siinä, että sen rakenne on erottamaton Stonewall x2 -siirrosta. Kun analyytikko kohtaa tämän tietyn mallin, hän ei voi määrittää, onko kyseessä tavallinen Stonewall yhdellä käyttäjällä vai Stonewall x2 kahdella käyttäjällä. Kuitenkin, kuten seuraavissa kappaleissa näemme, Stonewall x2 -siirtojen suorittaminen on muuttunut monimutkaisemmaksi Sorobanin saatavuuden puuttuessa. Jotkut siis ajattelevat, että analyytikko saattaisi nyt olettaa, että mikä tahansa tällaisen rakenteen siirto on normaali Stonewall. Henkilökohtaisesti en jaa tätä oletusta. Vaikka Stonewall x2 -siirrot saattavat olla harvinaisempia (ja luulen, että ne olivat jo ennen tätä tapausta), se, että ne ovat edelleen mahdollisia, voi mitätöidä koko analyysin, joka perustuu oletukseen, että ne eivät ole.
**[-> Lue lisää Stonewall-siirroista.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)**
Ricochetin osalta en ole pystynyt varmistamaan, onko palvelu edelleen toiminnassa, koska minulla ei ole Dojoa Testnetissä, ja haluan välttää riskin käyttää `100 000 satsia` lompakkoon, jota viranomaiset saattavat hallita. Jos sinulla on ollut mahdollisuus testata tätä työkalua äskettäin, pyydän sinua ottamaan yhteyttä minuun, jotta voimme päivittää tämän artikkelin.

Jos tarvitset Ricochetia, muista, että voit aina suorittaa tämän toimenpiteen manuaalisesti millä tahansa lompakko-ohjelmistolla. Jos haluat oppia suorittamaan eri hyppyjä manuaalisesti oikein, suosittelen tutustumaan tähän toiseen artikkeliin: [**RICOCHET**](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).

JoinBot-työkalu ei ole enää toiminnassa, koska se riippui täysin Samourain hallinnoiman lompakon osallistumisesta.

Muiden yhteistyöllisten siirtojen osalta, joita usein kutsutaan "cahoots"-siirroiksi, ne ovat edelleen mahdollisia, mutta vain manuaalisesti. Ennen palvelimen sulkemista sinulla oli kaksi vaihtoehtoa suorittaa Stonewall x2 tai Stowaway (PayJoin) -siirtoja:
- Käytä Soroban-verkkoa vaihtaaksesi PSBT:t automaattisesti ja etänä;
- Tai suorita nämä vaihdot manuaalisesti skannaamalla useita QR-koodeja.

Useiden testien jälkeen vaikuttaa siltä, että Soroban ei enää toimi. Näiden yhteistyöllisten siirtojen suorittamiseksi datan vaihto on siis tehtävä manuaalisesti. Tässä on kaksi vaihtoehtoa tämän vaihdon suorittamiseksi:
- Jos olet fyysisesti lähellä yhteistyökumppaniasi, voit skannata QR-koodeja peräkkäin;
- Jos olet kaukana yhteistyökumppanistasi, voit vaihtaa PSBT:t ulkoisen viestintäkanavan kautta sovelluksen ulkopuolella. Ole kuitenkin varovainen, sillä näissä PSBT:ssä olevat tiedot ovat yksityisyyden kannalta arkaluonteisia. Suosittelen salatun viestipalvelun käyttöä vaihdon luottamuksellisuuden varmistamiseksi.
**[-> Lue lisää Stonewall x2 -transaktioista.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4-x2)**

**[-> Lue lisää Stowaway-transaktioista.](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)**

Mitä tulee Whirlpooliin, protokolla ei näytä enää toimivan, edes käyttäjille, joilla on oma Dojo. Olen seurannut RoninDojoani viime päivinä ja yrittänyt joitakin perusmanipulaatioita, mutta Whirlpool CLI ei ole kyennyt muodostamaan yhteyttä palvelimen sulkemisen jälkeen.

Toivon kuitenkin, että tämä protokolla voidaan aktivoida uudelleen tai ehkä kuvitella eri tavalla tulevina viikkoina, riippuen siitä, miten tilanne kehittyy. Tämä tauko voisi olla mahdollisuus tutkia uusia lähestymistapoja tai mahdollisia parannuksia tähän järjestelmään.
### Mitkä ulkoiset työkalut ovat edelleen saatavilla?
Samourai-ympäristöön liittyvistä muista työkaluista jotkut ovat edelleen saatavilla, kun taas toiset eivät.

Ilmainen ketjuanalyysin verkkosivusto OXT.me ei valitettavasti ole toistaiseksi saatavilla.

Whirlpool Stats Tool ei ole enää ladattavissa, koska se oli isännöity Samourain GitLabiin. Vaikka olisit aiemmin ladannut tämän Python-työkalun paikallisesti koneellesi tai jos se oli asennettu RoninDojo-noodiisi, WST ei toimi toistaiseksi. Se riippui OXT.me:n tarjoamista tiedoista toimiakseen, ja tämä sivusto ei ole enää saatavilla. Tällä hetkellä WST ei ole erityisen hyödyllinen, koska Whirlpool-protokolla on passiivinen.

KYCP.org-sivusto ei ole tällä hetkellä enää saatavilla.

Myös Boltzmann Calculator Python-työkalun koodin isännöinyt GitLab on takavarikoitu. Tällä hetkellä ei siis ole mahdollista ladata tätä työkalua. Mutta jos sinulla on RoninDojo, voit jatkaa Boltzmann Calculatorin käyttöä kuten ennenkin.

RoninDojon osalta, tämä node-in-box -ohjelmisto toimii edelleen oikein, huolimatta tiettyjen erityistyökalujen, kuten Whirlpool CLI:n ja WST:n, saatavuuden puutteesta. Sitä voidaan edelleen käyttää muiden lompakko-ohjelmistojen kanssa kiitos Fulcrumin tai Electrsin. Jos haluat saada lisätietoja RoninDojosta tai sinulla on erityisiä kysymyksiä, suosittelen liittymään [heidän Telegram-ryhmäänsä](https://t.me/RoninDojoNode).

RoninDojon lähdekoodi ei kuitenkaan ole tällä hetkellä saatavilla, koska se oli isännöity Samourain GitLabiin. Tästä syystä manuaalinen asennus Raspberry Pi:lle ei ole mahdollista tällä hetkellä.

Mitä tulee vain seurantaan käytettävään lompakko-ohjelmistoon Sentinel, tilanne on samankaltainen kuin Samourai-sovelluksessa. Jos sinulla on oma Dojo, voit jatkaa Sentinelin käyttöä ilman ongelmia. Jos sinulla ei kuitenkaan ole Dojoa, et pysty muodostamaan yhteyttä. Toisin kuin Samourai, Sentinel-verkkosivusto on edelleen saatavilla verkossa. Ole kuitenkin varovainen tämän sivuston ja siellä tarjotun APK:n kanssa, sillä ei ole selvää, kuka tällä hetkellä hallitsee näitä resursseja.

### Onko Sparrow Wallet vaikuttunut?
Sparrow Wallet toimii edelleen normaalisti, lukuun ottamatta Samourai-työkaluja, jotka eivät ole enää saatavilla. Tällä hetkellä coinjoineja ei ole mahdollista suorittaa Sparrow'n kautta. Samoin yhteistyössä tapahtuva kuluttaminen ei ole enää mahdollista, sillä Sparrow ei tarjoa mahdollisuutta PSBT:iden manuaaliseen vaihtoon toisin kuin Samourai. Kaikkien muiden toimintojen osalta Sparrow toimii ilman ongelmia. Voit myös käyttää tätä ohjelmistoa Samourai-lompakon palauttamiseen tarvittaessa.

## Kuinka palauttaa Samourai-lompakko?
Kuten aiemmissa osioissa näimme, jos omistat oman Dojon, ei ole välttämättä tarpeen vaihtaa ohjelmistoa. **Samourai on edelleen erinomainen valinta kuumaksi lompakoksi** päivittäisiin menoihisi. Jos sinulla ei kuitenkaan ole Dojoa tai jos haluat valita toisen ohjelmiston, selitän koko palautusprosessin, yksityiskohtaisesti mahdolliset esteet, joita saatat kohdata.

Joka tapauksessa on tärkeää ottaa aikaa ja varmistaa, ettei tee virheitä. Muista, että kiirettä ei ole, sillä sinulla on yksityiset avaimet hallussasi, eikä Samourain palvelimien takavarikointi vaikuta tähän millään tavalla. Mitä tahansa tapahtuukin, he eivät ilmeisesti voi päästä käsiksi yksityisiin avaimiisi.

### Vahvista salasana

Lompakon palauttamiseksi sinulla on oltava salasanasi, vaikka valitsisitkin palautuksen varmuuskopiotiedoston kautta. Aloita tarkistamalla tämän salasanan pätevyys. Avaa Samourai Wallet -sovelluksesi, klikkaa Paynym-kuvakettasi vasemmassa yläkulmassa ja valitse `Asetukset`.

![samourai](assets/1.webp)

Seuraavaksi klikkaa `Vianmääritys` ja sitten `Salasana/varmuuskopiotesti`.

![samourai](assets/2.webp)

Syötä salasanasi ja klikkaa `Ok`. Jos se on oikein, Samourai vahvistaa sen. Sinulla on myös mahdollisuus tarkistaa varmuuskopiotiedosto, jos aiot käyttää sitä myöhemmin.

![samourai](assets/3.webp)

Tämä vaihe on valinnainen, mutta suositeltava. Se vahvistaa, että salasana on oikein, poistaen mahdollisen ongelman lähteen myöhemmin. Jos Samourai ilmoittaa tässä vaiheessa, että salasana on väärin, palautus ei ole mahdollista. Varmista, että olet syöttänyt salasanan oikein ja tarkista se uudelleen.

### Vaihtoehto 1: Palauta lompakko Sparrow'lla varmuuskopiotiedoston avulla

Sparrow Walletin version 1.8.6 alkaen on mahdollista suoraan tuoda Samourai-lompakkosi käyttäen varmuuskopiotekstitiedostoa nimeltä `samourai.txt`, jonka sovelluksesi automaattisesti luo. Tämä tiedosto sisältää kaikki tarvittavat tiedot lompakkosi palauttamiseen ja se on salattu salasanallasi turvallisuuden vuoksi.

Jos valitset tämän vaihtoehdon, tarvitset ajan tasalla olevan `samourai.txt` tiedoston ja salasanasi. Tämän tiedoston luomiseksi Samourai Walletissa, klikkaa kolmea pientä pistettä oikeassa yläkulmassa ja valitse `Vie lompakon varmuuskopio`.

![samourai](assets/4.webp)
Seuraavaksi valitse `Vie leikepöydälle`. Sen jälkeen sinun täytyy siirtää tämä tiedosto turvallisesti PC:lle. Koska tiedosto on salattu, mutta pelkkä salasana riittää sen purkamiseen, on tärkeää olla varovainen sen siirron aikana. Jos valitset suoran siirron tekstitiedostona, sinun on luotava `samourai.txt` tiedosto PC:lläsi ja liitettävä leikepöydän sisältö siihen. Vaihtoehtoisesti voit suoraan hakea `samourai.txt` tiedoston puhelimesi tallennetuista tiedostoista.
Kun sinulla on pääsy tiedostoon PC:lläsi, avaa Sparrow Wallet, klikkaa `Tiedosto`-välilehteä ja valitse `Tuo lompakko` aloittaaksesi lompakkosi tuonnin.

![samourai](assets/5.webp)
Vieritä alas kohtaan `Samourai Backup`, klikkaa `Import File` ja valitse sitten `samourai.txt`-tiedostosi.
![samourai](assets/6.webp)

Sparrow pyytää sinulta salasanaa tiedoston purkamiseen. Tämä salasana on itse asiassa sinun salalauseesi. Syötä se vastaavaan kenttään ja klikkaa `Import`.

![samourai](assets/7.webp)

Jos tässä vaiheessa lompakkosi ei ilmesty, on mahdollista, että teit virheen kopioimalla `samourai.txt`-tiedoston tai syöttäessäsi salalauseen. Voit konsultoida vianmääritysosioita saadaksesi lisäapua.

![samourai](assets/8.webp)

Skriptityypin osalta, jos et ole määrittänyt muita skriptejä Samouraissa, sinun tulisi normaalisti käyttää vain SegWit V0:tä (Native SegWit / P2WPKH). Säilytä tämä oletusskripti ja klikkaa `Import`.

![samourai](assets/9.webp)

Nimeä lompakkosi, esimerkiksi "Samourai Recovery", ja klikkaa sitten `Create Wallet`.

![samourai](assets/10.webp)

Sparrow pyytää sinua valitsemaan salasanan. Tämä salasana suojaa vain pääsyä lompakkoosi tällä PC:llä eikä liity lompakkosi avainten johdannaiseen. Varmista, että valitset vahvan salasanan, merkitse se muistiin muistaaksesi sen ja klikkaa `Set Password`.

![samourai](assets/11.webp)

Sparrow johdattaa sitten lompakkosi avaimet ja etsii vastaavat transaktiot.

![samourai](assets/12.webp)

Toistaiseksi vain talletustilisi on käytettävissä. Jos käytit Samouraita vain tälle tilille, sinun pitäisi nähdä kaikki varasi. Jos kuitenkin käytit myös Whirlpoolia, sinun on johdettava `premix`, `postmix` ja `badbank`-tilit. Sparrow'ssa, klikkaa vain `Settings`-välilehteä, sitten `Add Accounts...`.

![samourai](assets/13.webp)
Avautuvassa ikkunassa valitse pudotusvalikosta `Whirlpool Accounts` ja klikkaa `OK`.
![samourai](assets/14.webp)

Näet sitten eri Whirlpool-tilisi ilmestyvän, ja Sparrow johdattaa tarvittavat avaimet käyttääksesi niihin liittyviä bitcoineja.

![samourai](assets/15.webp)

Jos käytät eri ohjelmistoa kuin Sparrow, kuten Electrum, Samourai-lompakkosi palauttamiseen, tässä ovat Whirlpool-tili-indeksit manuaalista palautusta varten:
- Deposit: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`

Nyt sinulla on pääsy bitcoineihisi Sparrow'ssa. Jos tarvitset apua Sparrow Walletin käyttöön, voit myös tutustua [omistettuun opastukseemme](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607).

Suosittelen myös manuaalisesti tuomaan Samouraissa UTXO:ihisi liitetyt nimikkeet. Tämä mahdollistaa tehokkaan kolikoiden hallinnan Sparrow'ssa myöhemmin.

### Vaihtoehto 2: Palauta lompakko Sparrow'ssa mnemonisen lauseen avulla

Jos et halua suorittaa palautusta varmuuskopiotiedoston avulla, voit valita perinteisemmän menetelmän käyttämällä yksinkertaisesti 12-sanaisen palautuslauseesi ja salalauseesi. Tämä toinen vaihtoehto on usein yksinkertaisempi.
Aloittaaksesi, varmista, että sinulla on palautusfraasisi ja salasanasi saatavilla. Avaa sitten Sparrow Wallet -ohjelmisto, napsauta `File`-välilehteä ja valitse `Import Wallet` aloittaaksesi lompakkosi tuonnin.
![samourai](assets/16.webp)

Valitse `Mnemonic Words (BIP39)` ja pudotusvalikosta klikkaa `Use 12 Words`.

![samourai](assets/17.webp)

Syötä 12 sanaa palautusfraasistasi oikeassa järjestyksessä.

![samourai](assets/18.webp)

Jos Sparrow näyttää `Invalid Checksum` -viestin, se tarkoittaa, että palautusfraasin tarkistussumma ei ole kelvollinen, mikä todennäköisesti tarkoittaa, että teit virheen sanoja syöttäessäsi.

![samourai](assets/19.webp)

Jos fraasisi on oikein, valitse `Use Passphrase?` -ruutu ja syötä salasanasi omistettuun kenttään. Lopuksi, jos kaikki vaikuttaa oikealta, klikkaa `Discover Wallet` -painiketta.

![samourai](assets/20.webp)

Nimeä lompakkosi, esimerkiksi "Samourai Recovery", ja klikkaa sitten `Create Wallet`.

![samourai](assets/21.webp)
Sparrow pyytää sinua valitsemaan salasanan. Tämä salasana suojaa vain pääsyä lompakkoosi tällä PC:llä eikä liity lompakkosi avainten johdannaiseen. Varmista, että valitset vahvan salasanan, kirjoita se muistiin muistaaksesi sen, ja klikkaa `Set Password`.
![samourai](assets/22.webp)

Sparrow johdattaa sitten lompakkosi avaimet ja etsii vastaavia siirtoja.

![samourai](assets/23.webp)

Jos tässä vaiheessa lompakkosi ei ilmesty, on mahdollista, että teit virheen syöttäessäsi salasanan tai palautusfraasin. Voit konsultoida omistettua vianmääritysosaa saadaksesi lisäapua.

Toistaiseksi vain talletustilisi on käytettävissä. Jos käytit Samouraita vain tälle tilille, sinun pitäisi nähdä kaikki varasi. Jos kuitenkin käytit myös Whirlpoolia, sinun on johdettava `premix`, `postmix` ja `badbank` -tilit. Sparrow'ssa, klikkaa vain `Settings`-välilehteä, sitten `Add Accounts...`.

![samourai](assets/24.webp)

Avautuvassa ikkunassa valitse pudotusvalikosta `Whirlpool Accounts`, sitten klikkaa `OK`.

![samourai](assets/25.webp)

Näet sitten eri Whirlpool-tilisi ilmestyvän, ja Sparrow johdattaa tarvittavat avaimet käyttääksesi liittyviä bitcoineja.

![samourai](assets/26.webp)

Jos käytät toista ohjelmistoa, kuten Electrumia, palauttaaksesi Samourai-lompakkosi, tässä ovat Whirlpool-tilien indeksit manuaalista palautusta varten:
- Deposit: `m/84'/0'/0'`
- Bad Bank: `m/84'/0'/2147483644'`
- Premix: `m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`

Sinulla on nyt pääsy bitcoineihisi Sparrow'ssa. Jos tarvitset apua Sparrow Walletin käytössä, voit myös konsultoida [omistettua opastamme](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607).

Suosittelen myös manuaalisesti tuomaan Samouraissa UTXO:ihisi liittyneet etiketit. Tämä mahdollistaa tehokkaan kolikoiden hallinnan Sparrow'ssa myöhemmin.

### Mitkä ovat yleisiä ongelmia?
Autettuani useita ihmisiä viime päivinä uskon kohdanneeni suurimman osan ongelmista, jotka voivat estää lompakkosi palauttamisen. Jos et silti pääse käsiksi lompakkoosi aiempien opastusten jälkeen, tässä on joitakin lisäsuosituksia. Ensinnäkin, jotta palautus toimisi, on ehdottoman tärkeää, että palautuslause on oikein. Jos et löydä 12-sanaisen lauseesi, voit käyttää *vaihtoehto 1*:ä palauttaaksesi Samourain varmuuskopiotiedostosta. Voit myös päästä käsiksi palautuslauseeseesi suoraan Samourai Lompakossa siirtymällä kohtaan `Asetukset`, sitten `Lompakko`, ja lopuksi valitsemalla `Näytä 12-sanainen palautuslause`.

Seuraavaksi, kirjoitusvirhe salasanassasi palautuksen aikana johtaa virheellisiin johdettuihin avaimiin, mikä estää lompakkosi palauttamisen Sparrow'ssa. **Salasanan on oltava täydellisen tarkka!**

Ratkaisuna suosittelen ensin tarkistamaan salasanasi pätevyyden Samourai-sovelluksessa, kuten tämän artikkelin "_Vahvista salasana_" -osiossa on kuvattu:
1. **Vahvistus Samouraissa:** Jos Samourai vahvistaa, että salasana on oikein, yritä palautusta uudelleen alusta, varmistaen, että kirjoitat salasanan Sparrow'ssa virheettömästi;
2. **Salasanan Virhe:** Jos Samourai ilmoittaa, että salasana on väärin, Sparrow'ssa jatkaminen on turhaa. Niin kauan kuin oikeaa salasanaa ei löydy, lompakkosi palauttaminen on mahdotonta. Jos olet menettänyt salasanasi pysyvästi, pidä Samourai-sovelluksesi turvassa. Kaikki mitä voit tehdä, on toivoa, että palvelimet käynnistetään uudelleen, jotta voit tehdä maksuja suoraan sovelluksesta ilman palautustarvetta. **Älä yritä yhdistää Dojoon tässä tapauksessa**, sillä se tarkoittaisi lompakkosi nollaamista Samouraissa, mikä vaatii pääsyn salasanaan.

Muiden kohdattujen virheiden joukossa monet liittyvät Sparrow'n verkkokonfiguraatioon.

Ensinnäkin, varmista, että Sparrow on oikein konfiguroitu `mainnet`-tilaan eikä `testnet`-tilaan. Todellakin, jos Sparrow etsii transaktioitasi Testnetistä, se ei löydä mitään, koska lompakkosi on Mainnetissä. Testnet on Bitcoinin vaihtoehtoinen versio, jota käytetään ainoastaan testaamiseen ja kehittämiseen, ja se toimii erillisessä verkossa pääverkosta (Mainnet), omilla lohkoillaan ja transaktioillaan. Tarkistaaksesi, missä verkossa olet, klikkaa `Työkalut`-välilehteä, sitten `Käynnistä uudelleen`. Jos `Mainnet`-vaihtoehto näkyy, et ole pääverkossa. Valitse se käynnistääksesi Sparrow'n uudelleen Mainnetissä, ja aloita sitten palautusprosessisi uudelleen.

![samourai](assets/27.webp)
Jotkut ovat kohdanneet vaikeuksia yhdistäessään Sparrow'n omaan solmuunsa. Sparrow'n oikeassa alakulmassa oleva värillinen kytkin osoittaa, onko ohjelmistosi oikein yhdistetty Bitcoin-solmuun. Samourai-transaktioidesi noutamiseksi on olennaista, että ohjelmisto on hyvin yhdistetty. Tarkista, että kytkin on aktivoitu, kuten alla olevassa kuvassani (keltainen julkiselle solmulle, vihreä Bitcoin Corelle ja sininen Electrum-palvelimelle).
![samourai](assets/28.webp)

Jos kytkin ei ole aktivoitu, klikkaa sitä aktivoidaksesi yhteyden uudelleen.

![samourai](assets/29.webp)

Jos ongelma jatkuu, tässä on joitakin mahdollisia ratkaisuja:
- Jos yrität yhdistää omaan Electrum-palvelimeesi (sininen) tai Bitcoin Coreesi (vihreä) ja Sparrow ei voi yhdistää, tarkista yhteystiedot kohdasta `Tiedosto > Asetukset... > Palvelin`;

![samourai](assets/30.webp)
- Jos yhteysongelma jatkuu, se saattaa johtua solmusi puutteellisesta synkronoinnista. Varmista, että solmusi ja indeksoijasi ovat 100% synkronoituja. Tarvittaessa viimeisenä keinona, irrota solmusi Sparrow'sta ja yhdistä julkiseen solmuun; - Jos olit jo yhdistänyt julkiseen solmuun ja yhteys epäonnistuu, yritä vaihtaa solmua valitsemalla toinen pudotusvalikosta.

![samourai](assets/31.webp)

Jos olet onnistuneesti palauttanut lompakkosi, mutta se vaikuttaa puutteelliselta, ongelma saattaa liittyä johdannaisuuteen.

Ongelma voi ilmetä, jos olet käyttänyt Samourai-talletustiliäsi eri skriptityypillä kuin `P2WPKH`. Oletuksena Samourai käyttää tätä skriptityyppiä, mutta jos olet manuaalisesti muuttanut sitä, sinun on säädettävä tätä myös palauttaessasi Sparrow'ssa.

Jotta voit johtaa haaroja muille skriptityypeille, sinun on toistettava palautusprosessi kullekin käytetylle skriptityypille. Tätä varten mene kohtaan `File > New Wallet` Sparrow'ssa, valitse toinen skriptityyppi pudotusvalikosta, klikkaa `New or Imported Software Wallet`, ja noudata samoja vaiheita kuin alkuperäisessä oppaassa.

![samourai](assets/32.webp)

Toinen kohtaamani johdannaisuusongelma liittyy Gap Limit -arvoon. Tämä arvo kertoo Sparrow'lle, kuinka monen tyhjän osoitteen jälkeen sen tulisi lopettaa uusien osoitteiden johtaminen. Jos palautuksen jälkeen huomaat, että joitakin transaktioita puuttuu, tämä saattaa johtua liian alhaisesta Gap Limit -arvosta. Ongelman ratkaisemiseksi mene ongelmaa aiheuttavaan tiliin, esimerkiksi postmix-tiliin (jos useampi tili on kyseessä, toista tämä toimenpide kullekin).

![samourai](assets/33.webp)

Klikkaa `Settings`-välilehteä ja sitten `Advanced...`-painiketta.
![samourai](assets/34.webp)
Lisää Gap Limit -arvon arvoa asteittain, esimerkiksi asetin sen tässä `400`:aan. Sen jälkeen klikkaa `Close`-painiketta.

![samourai](assets/35.webp)

Klikkaa `Apply` viimeistelläksesi. Sparrow johtaa suuremman määrän osoitteita ja etsii niistä varoja, mikä auttaisi palauttamaan kaikki transaktiosi.

![samourai](assets/36.webp)

Tämä kattaa erilaiset palautusongelmat, joita olen kohdannut viime päivinä. Jos kokeiltuasi kaikkia näitä ratkaisuja sinulla on edelleen ongelmia, kutsun sinut liittymään [Discover Bitcoin Discordiin](https://discord.gg/xKKm29XGBb) pyytämään apua. Käyn säännöllisesti tässä Discordissa ja olisin iloinen voidessani auttaa, jos minulla on ratkaisu. Myös muut bitcoin-käyttäjät voivat jakaa kokemuksiaan ja tarjota apuaan. **Joka tapauksessa on olennaista pitää palautuslauseesi, varmuuskopiotiedostosi ja salasanasi luottamuksellisina**. Älä jaa niitä kenenkään kanssa, sillä se saattaisi mahdollistaa bitcoiniesi varastamisen.

Kun palautus on valmis, sinulla on nyt pääsy bitcoineihisi. Se on hyvä asia, mutta se ei ehkä riitä. Todellakin, palvelimien takavarikointi nostaa esiin uusia mahdollisia riskejä yksityisyydellesi. Seuraavassa osiossa tarkastelemme näitä riskejä yksityiskohtaisesti ja hahmottelemme varotoimenpiteitä yksityisyytesi suojelemiseksi.

## Mitkä ovat seuraukset transaktioidesi yksityisyydelle?

### Samourai-käyttäjänä ilman Dojoa

Jos käytit Samourai-lompakkoa yhdistämättä omaa Dojoasi, xpubisi oli kommunikoitava Samourain palvelimille, jotta sovellus toimisi. Näiden palvelimien takavarikoinnin myötä on mahdollista, että viranomaisilla on nyt pääsy näihin xpubseihin.
Tämä skenaario pysyy hypoteettisena. Emme tiedä, onko näitä xpub-osoitteita tallennettu, onko mahdollinen tallennusväline tuhottu, ovatko viranomaiset saaneet ne takaisin, ja aikovatko he käyttää niitä ketjuanalyysiin. Kuitenkin tällaisessa tilanteessa on järkevää ottaa huomioon pahin mahdollinen skenaario, jossa viranomaisilla on käyttäjien xpub-osoitteet, jotka eivät ole yhdistäneet omaa Dojoaan. Viitteeksi, xpub on merkkijono, joka sisältää kaikki tarvittavat elementit lapsi julkisten avainten (julkinen avain + ketjukoodi) luomiseen. Sitä käytetään hierarkkisesti määräytyvissä lompakoissa vastaanotto-osoitteiden luomiseen ja tilin transaktioiden tarkkailuun paljastamatta yhdistettyjä yksityisiä avaimia. Tämä mahdollistaa esimerkiksi "vain katselu" -lompakon luomisen. Kuitenkin xpub-osoitteiden paljastaminen voi vaarantaa käyttäjän yksityisyyden, sillä ne mahdollistavat kolmansien osapuolien transaktioiden seuraamisen ja liitännäistilien saldojen näkemisen.
Kuka tahansa, joka tietää xpub-osoitteesi, voi siis nähdä kaikki lompakkosi vastaanotto-osoitteet, ne, joita on käytetty menneisyydessä, ja ne, jotka luodaan tulevaisuudessa.

Käyttäjille, joilla ei ole Dojoa, mahdollisella xpub-osoitteidesi vuodolla on kaksi merkittävää seurausta:
- Tekemäsi coinjoinit muuttuvat tehottomiksi yksityisyyden kannalta kenelle tahansa, joka tietää xpub-osoitteesi, jolloin kolikkosi menettävät kaiken anonsetin;
- Tämä henkilö voi myös seurata kaikkia Samourai-lompakkosi vastaanotto-osoitteita.

On siis tärkeää ottaa huomioon pahin mahdollinen skenaario ja luopua tästä mahdollisesti yksityisyyden suhteen vaarantuneesta lompakosta. Tee tämä luomalla uusi lompakko alusta alkaen toisella ohjelmistolla, kuten Sparrow Wallet. Varmistettuasi varmuuskopioidesi pätevyyden, siirrä kaikki varasi tekemällä transaktioita. Vaikka tämä toimenpide ei katkaise kolikkojesi jäljitettävyyssidettä, se estää viranomaisia tietämästä varmuudella uuden lompakkosi osoitteita.

Tämän siirto-operaation aikana suosittelen välttämään kolikkojesi konsolidointia. Jos oletetaan, että xpub-osoitteesi ovat vaarantuneet, konsolidoinnilla ei ole vaikutusta henkilön näkökulmasta, jolla on pääsy näihin xpub-osoitteisiin, koska yksityisyytesi on jo vaarantunut niiden kanssa. Kuitenkin neuvon sinua olemaan konsolidoimatta kolikkojasi liikaa pääasiassa muiden ihmisten yksityisyyden suojelemiseksi. Pahimmassa tapauksessa vain viranomaisilla saattaa olla pääsy xpub-osoitteisiisi, mutta muu maailma ei tiedä niistä. Näin ollen muiden näkökulmasta kolikkojesi konsolidointi voisi merkittävästi vahingoittaa yksityisyyttäsi Common Input Ownership Heuristic (CIOH) -periaatteen vuoksi.

Lopuksi, jäljittämisen lopulliseksi katkaisemiseksi harkitse myös coinjoinien suorittamista tästä uudesta lompakosta.
**Varoitus:** Pelkkä Samourai-lompakkosi siirtäminen Sparrow Walletiin ei riitä. On tarpeen luoda täysin uusi lompakko uudella palautusfraasilla, jos haluat välttää mahdollisesti vuotaneiden xpub-osoitteiden käyttöä. Jos tuot olemassa olevan siemenesi Sparrow'hun, vaihdat vain lompakonhallintaohjelmiston, mutta lompakko pysyy samana.

### Sparrow'n tai Samourain käyttäjänä Dojon kanssa

Jos lompakkosi hallinnoidaan vain Sparrow Walletissa, xpub-osoitteesi eivät ole voineet vuotaa, käytitpä sitten julkista solmua tai omaa Bitcoin-solmuasi. Samoin, jos käytät Samourai-sovellusta ja olet aina yhdistänyt tämän sovelluksen omaan Dojoosi lompakon luomisesta lähtien, xpub-osoitteesi ovat myös turvassa.
Kuitenkin, jos olet käyttänyt samaa lompakkoa aikana **ilman omaa Dojoasi** ja sen jälkeen omalla Dojollasi, on mahdollista, että Samourain palvelimet ovat saattaneet päästä käsiksi xpub-avaimiisi, ja siksi viranomaiset saattavat tietää ne. Jos olet tässä erityistilanteessa, suosittelen noudattamaan edellisen osion suosituksia ja pitämään xpub-avaimiasi kompromissoituneina.
Niille, jotka ovat aina käyttäneet Sparrow'ta tai Samouraita omalla Dojollaan, pääasiallinen riski on, että kolikoidesi anonimiteettijoukot (anonsets) saattavat potentiaalisesti pienentyä. Oletetaan pahimmassa tapauksessa, että kaikkien ilman Dojoa olevien käyttäjien xpub-avaimet ovat viranomaisten hallussa, silloin näiden kolikoiden polku coinjoin-sykleissä voitaisiin jäljittää näiden viranomaisten toimesta.

Havainnollistaaksemme tätä, otetaan konkreettinen esimerkki. Kuvittele, että osallistuit ensimmäiseen coinjoin-sykliin, jota seurasivat kaksi lisäalajuoksun coinjoin-sykliä. Jos ilman Dojoa olevien käyttäjien xpub-avaimet eivät ole vuotaneet, silloin kolikkosi tuleva anonimiteettijoukko olisi 13.

![samourai](assets/37.webp)

Kuitenkin, jos otamme huomioon, että xpub-avaimet ovat vuotaneet ja että kohtasit käyttäjän ilman dojoa alkuperäisessä coinjoinissa, ja sitten 2 ensimmäisessä alajuoksun coinjoinissa, silloin kolikkosi tuleva anonimiteettijoukko olisi vain 10 sijaan 13 viranomaisen näkökulmasta.

![samourai](assets/38.webp)
Tämän mahdollisen anonimiteettijoukon pienentymisen määrää on monimutkaista arvioida, sillä se riippuu lukuisista tekijöistä, ja jokainen kolikko on eri tavalla vaikuttunut. Esimerkiksi ilman Dojoa olevan käyttäjän kohtaaminen alkuvaiheen sykleissä vaikuttaa tulevaan anonimiteettijoukkoon paljon enemmän kuin myöhemmissä sykleissä kohdattu. Antaaksesi kuvan tilanteesta, joka on kuitenkin hypoteettinen, viimeisimmät Samourain tarjoamat tilastot osoittivat, että 85%–90% coinjoineihin osallistuneista kolikoista tuli käyttäjiltä, joilla oli Dojo, Sparrow tai Bitcoin Keeper, eli käyttäjiltä, jotka, jopa pahimmassa tapauksessa, eivät olisi nähneet xpub-avaimiensa vuotavan.
Vaikka näitä lukuja on vaikea varmistaa, ne vaikuttavat minusta johdonmukaisilta kahdesta syystä:
- Sparrow Wallet on laajalti käytössä;
- Useimmat node-in-box -ohjelmistot tarjoavat Dojo-toteutuksia, ja nämä päävirran ohjelmistot kuten Umbrel ovat nykyään erittäin suosittuja.

Näin ollen useita näkökohtia on harkittava. Jos kolikoidesi yksityisyys viranomaisia kohtaan on sinulle erittäin tärkeää, olisi viisasta varautua pahimpaan skenaarioon, eikä voida taata 100%:sti, että Whirlpool-coinjoin-syklisi eivät voisi joutua jäljitetyiksi mahdollisen xpub-avainten vuodon vuoksi käyttäjiltä ilman Dojoa. Vaikka tämä oletus on erittäin epätodennäköinen, se ei ole mahdoton.

Toisaalta, jos kolikoidesi yksityisyys viranomaisia kohtaan, jotka mahdollisesti hallussaan nämä xpub-avaimet, ei ole sinulle ratkaisevan tärkeää, tilannetta voidaan tarkastella eri tavalla.

Mainitsen "viranomaisia kohtaan", koska on tärkeää muistaa, että vain viranomaiset, jotka takavarikoivat palvelimet, ovat mahdollisesti tietoisia näistä xpub-avaimista. Jos tavoitteenasi coinjoinin käytössä oli estää leipuriasi seuraamasta varojasi, hän ei ole paremmin informoitu kuin ennen palvelimien takavarikointia.
Lopuksi on olennaista harkita kolikkosi alkuperäistä anonsettiä ennen palvelimen takavarikointia. Otetaan esimerkiksi kolikko, jolla oli potentiaalinen anonsetti 40 000; tämän anonsetin mahdollinen väheneminen on todennäköisesti merkityksetön. Todellakin, jo erittäin korkean perusanonsetin ollessa kyseessä, on epätodennäköistä, että muutaman käyttäjän, joilla ei ole Dojoa, läsnäolo radikaalisti muuttaisi tilannetta. Kuitenkin, jos kolikkosi anonsetti oli 40, tämä potentiaalinen vuoto voisi vakavasti vaikuttaa anonsetteihisi ja mahdollisesti sallia jäljityksen. WST-työkalun ollessa nyt poissa käytöstä OXT.me:n sulkemisen jälkeen, voit vain arvioida näitä anonsettejä. Retrospektiivisen anonsetin osalta ei ole paljoa huolta, sillä Whirlpool-malli varmistaa, että se on erittäin korkea ensimmäisestä coinjoinista lähtien, kiitos vertaistesi perinnön. Ainoa tilanne, jossa tämä voisi aiheuttaa ongelman, on jos kolikkoasi ei ole sekoitettu uudelleen useaan vuoteen ja se oli sekoitettu altaan käynnistyksen alussa. Tulevaisuuden anonsetin osalta voit tutkia, kuinka kauan kolikkosi on ollut saatavilla coinjoineihin. Jos siitä on useita kuukausia, sillä on todennäköisesti erittäin korkea tulevaisuuden anonsetti. Päinvastoin, jos se lisättiin altaaseen vain muutama tunti ennen palvelimien takavarikointia, sen tulevaisuuden anonsetti on todennäköisesti hyvin matala.
[**-> Lisätietoja anonseteistä ja niiden laskentamenetelmästä.**](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

Toinen huomioon otettava seikka on konsolidaatioiden vaikutus sekoitettujen kolikoiden anonsetteihin. Koska Whirlpool-tilit eivät ole enää saatavilla Samourai-sovelluksen kautta, on todennäköistä, että monet käyttäjät ovat siirtäneet lompakkonsa toiseen ohjelmistoon ja yrittäneet nostaa varojaan Whirlpoolista. Erityisesti viime viikonloppuna, kun Bitcoin-verkon transaktiomaksut olivat suhteellisen korkeat, oli vahva tekninen ja taloudellinen kannustin konsolidoida post-mix-kolikoita. Tämä tarkoittaa, että on todennäköistä, että monet käyttäjät ovat tehneet merkittäviä konsolidaatioita.

Näiden post-mix-konsolidaatioiden ongelma on, että ne aina vähentävät anonsetteja, ei ainoastaan suorittavalle käyttäjälle, vaan myös käyttäjille, joihin he ovat törmänneet coinjoin-sykleissään. Vaikka en olekaan pystynyt tarkistamaan tai kvantifioimaan tätä ilmiötä tarkasti, tuolloin vallinneet taloudelliset kannustimet transaktiomaksuihin liittyen voivat johtaa meidät olettamaan, että anonsetit ovat mahdollisesti matalampia.

### Sentinel-käyttäjänä

Watch-only lompakko-sovelluksen Sentinel verkkotoiminta on samankaltaista kuin Samouraissa. Päästäksesi käsiksi lompakkotietoihisi, sovelluksen on lähetettävä antamasi xpubit, julkiset avaimet ja osoitteet Dojoon. Jos olet aina käyttänyt omaa Dojoasi Sentinelissä, ei ole ongelmaa, ja voit jatkaa sovelluksen käyttöä huoletta. Kuitenkin, jos olit riippuvainen Samourain palvelimista Sentinelissäsi, on mahdollista, että xpubisi on paljastettu. Tässä tapauksessa on suositeltavaa noudattaa samaa lompakon vaihtoprosessia, jota suositellaan Samourai Walletille, kun se on yhdistetty Samourain palvelimiin.

Epätodennäköisessä tapauksessa, että käytit Dojoasi Samourain kanssa mutta et Sentinelin kanssa, olisi viisaampaa olettaa, että xpubisi ovat vaarantuneet.

## Yhteenveto
Kiitos, että luit tämän artikkelin loppuun. Jos mielestäsi tiedoista puuttuu jotain tai sinulla on ehdotuksia, älä epäröi ottaa yhteyttä minuun jakamaan ajatuksiasi. Lisäksi, jos tarvitset lisäapua Samourai Walletin palauttamisessa tämän oppaan huolimatta, kutsun sinut liittymään [Discover Bitcoin Discordiin](https://discord.gg/xKKm29XGBb) pyytämään apua. Käyn säännöllisesti tässä Discordissa ja olisin iloinen voidessani auttaa sinua, mikäli minulla on ratkaisu. Myös muut bitcoin-käyttäjät voivat jakaa kokemuksiaan ja tarjota tukeaan. **Joka tapauksessa on olennaista pitää palautusfraasisi, varmuuskopiotiedostosi ja salasanasi luottamuksellisina**. Älä jaa niitä kenenkään kanssa, sillä se voisi mahdollistaa bitcoiniesi varastamisen.