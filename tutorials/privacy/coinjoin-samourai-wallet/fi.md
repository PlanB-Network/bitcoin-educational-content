---
name: Coinjoin - Samourai Wallet
description: Miten suorittaa coinjoin Samourai Walletissa?
---
![cover](assets/cover.webp)

***VAROITUS:** Samourai Walletin perustajien pidätyksen ja heidän palvelimiensa takavarikoinnin jälkeen 24. huhtikuuta Whirlpool-työkalu ei enää toimi, edes niille henkilöille, jotka käyttävät omaa Dojoaan tai käyttävät Sparrow Walletia. On kuitenkin mahdollista, että tämä työkalu voidaan palauttaa käyttöön tulevina viikkoina tai käynnistää uudelleen eri tavalla. Lisäksi tämän artikkelin teoreettinen osa pysyy relevanttina ymmärtämään yleisesti coinjoinien periaatteita ja tavoitteita (ei vain Whirlpool), sekä ymmärtämään Whirlpool-mallin tehokkuutta.*

_Seuraamme tiiviisti tämän tapauksen kehitystä sekä siihen liittyvien työkalujen kehitystä. Voitte olla varmoja, että päivitämme tämän oppaan uuden tiedon saataville tullessa._

_Tämä opas on tarkoitettu vain koulutus- ja tiedotustarkoituksiin. Emme kannusta tai hyväksy näiden työkalujen käyttöä rikollisiin tarkoituksiin. Jokaisen käyttäjän on noudatettava oman lainkäyttöalueensa lakeja._

---

"*bitcoin-lompakko kaduille*"

Tässä oppaassa opit, mikä coinjoin on ja miten suorittaa sellainen käyttäen Samourai Wallet -ohjelmistoa ja Whirlpool-toteutusta.

## Mikä on coinjoin Bitcoinissa?
**Coinjoin on tekniikka, joka katkaisee bitcoinien jäljitettävyyden lohkoketjussa**. Se perustuu yhteistyöhön perustuvaan transaktioon, jolla on erityinen samaa nimeä kantava rakenne: coinjoin-transaktio.

Coinjoinit parantavat Bitcoin-käyttäjien yksityisyyttä vaikeuttamalla ketjuanalyysiä ulkopuolisille tarkkailijoille. Niiden rakenne mahdollistaa useiden eri käyttäjien kolikoiden yhdistämisen yhteen transaktioon, hämärtäen jälkiä ja vaikeuttaen sisään- ja ulostulo-osoitteiden välisen yhteyden määrittämistä.

Coinjoinin periaate perustuu yhteistyöhön: useat käyttäjät, jotka haluavat sekoittaa bitcoinejaan, tallettavat samanarvoisia määriä transaktion sisääntuloina. Nämä määrät jaetaan sitten ulostuloina samanarvoisina jokaiselle käyttäjälle. Transaktion lopussa on mahdotonta yhdistää tiettyä ulostuloa tunnettuun käyttäjään sisääntulossa. Sisääntulojen ja ulostulojen välillä ei ole suoraa yhteyttä, mikä katkaisee yhteyden käyttäjien ja heidän UTXO:nsa välillä sekä kunkin kolikon historian.
![coinjoin](assets/notext/1.webp)

Esimerkki coinjoin-transaktiosta (ei minulta): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

Jotta coinjoin voidaan suorittaa samalla kun varmistetaan, että jokainen käyttäjä säilyttää hallinnan varoistaan koko ajan, prosessi alkaa transaktion rakentamisella koordinaattorin toimesta, joka sitten lähettää sen osallistujille. Jokainen käyttäjä allekirjoittaa transaktion sen jälkeen, kun on varmistanut, että se sopii heille. Kaikki kerätyt allekirjoitukset integroidaan lopulta transaktioon. Jos käyttäjä tai koordinaattori yrittää ohjata varoja muuttamalla coinjoin-transaktion ulostuloja, allekirjoitukset osoittautuvat kelvottomiksi, mikä johtaa transaktion hylkäämiseen solmujen toimesta.

Coinjoinin toteutuksia on useita, kuten Whirlpool, JoinMarket tai Wabisabi, joiden tavoitteena on hallita osallistujien koordinointia ja lisätä coinjoin-transaktioiden tehokkuutta.
Tässä oppaassa syvennymme **Whirlpool**-menetelmän toteutukseen, jonka pidän tehokkaimpana ratkaisuna coinjoinien suorittamiseen Bitcoinissa. Vaikka se on saatavilla useissa lompakoissa, tässä oppaassa tutkimme yksinomaan sen käyttöä Samourai Wallet -mobiilisovelluksen kanssa ilman Dojoa.
## Miksi suorittaa coinjoineja Bitcoinissa?
Yksi alkuperäisistä ongelmista minkä tahansa vertaisverkkomaksujärjestelmän kanssa on kaksinkertainen kulutus: miten estää pahantahtoisia henkilöitä kuluttamasta samoja rahayksiköitä useita kertoja ilman, että turvaudutaan keskusviranomaiseen välittäjänä?

Satoshi Nakamoto tarjosi ratkaisun tähän dilemmaan Bitcoin-protokollan kautta, vertaisverkkoon perustuvan elektronisen maksujärjestelmän, joka toimii riippumatta mistään keskusviranomaisesta. Hänen valkoisessa kirjassaan hän korostaa, että ainoa tapa todistaa kaksinkertaisen kulutuksen puuttuminen on varmistaa kaikkien maksujärjestelmän sisällä olevien transaktioiden näkyvyys.

Jotta jokainen osallistuja olisi tietoinen transaktioista, ne on julkaistava julkisesti. Siksi Bitcoinin toiminta perustuu läpinäkyvään ja hajautettuun infrastruktuuriin, joka mahdollistaa minkä tahansa solmuoperaattorin tarkistaa koko elektronisten allekirjoitusten ketjun ja jokaisen kolikon historian sen luomisesta kaivostyöntekijän toimesta.

Bitcoinin lohkoketjun läpinäkyvä ja hajautettu luonne tarkoittaa, että mikä tahansa verkon käyttäjä voi seurata ja analysoida kaikkien muiden osallistujien transaktioita. Tämän seurauksena nimettömyys transaktiotasolla on mahdotonta. Kuitenkin, yksilöiden tunnistamisen tasolla nimettömyys säilyy. Toisin kuin perinteisessä pankkijärjestelmässä, jossa jokainen tili on yhdistetty henkilöllisyyteen, Bitcoinissa varat liittyvät kryptografisten avainparien kanssa, tarjoten siten käyttäjille pseudonyymisyyttä kryptografisten tunnisteiden takana.

Näin ollen Bitcoinin luottamuksellisuus vaarantuu, kun ulkopuoliset tarkkailijat onnistuvat yhdistämään tiettyjä UTXOja tunnistettuihin käyttäjiin. Kun tämä yhdistäminen on vahvistettu, on mahdollista jäljittää heidän transaktionsa ja analysoida heidän bitcoinien historiaansa. Coinjoin on nimenomaan kehitetty tekniikka rikkomaan UTXOjen jäljitettävyys, tarjoten siten tietyn luottamuksellisuuden tason Bitcoin-käyttäjille transaktiotasolla.

## Miten Whirlpool toimii?
Whirlpool erottuu muista coinjoin-menetelmistä käyttämällä "_ZeroLink_" -transaktioita, jotka varmistavat, että kaikkien syötteiden ja kaikkien tuotosten välillä ei ole teknisesti mahdollista olla mitään yhteyttä. Tämä täydellinen sekoitus saavutetaan rakenteella, jossa jokainen osallistuja panostaa identtisen määrän syötteenä (lukuun ottamatta kaivosmaksuja), tuottaen näin täydellisen yhtä suuria määriä olevia tuotoksia.
Tämä rajoittava lähestymistapa syötteisiin antaa Whirlpool-coinjoin-transaktioille ainutlaatuisen ominaisuuden: täydellisen puuttuvan deterministisen yhteyden syötteiden ja tuotosten välillä. Toisin sanoen, jokaisella tuotoksella on yhtä suuri todennäköisyys olla kenen tahansa osallistujan, verrattuna kaikkiin muihin transaktion tuotoksiin.
Alun perin Whirlpool-coinjoinin osallistujien määrä oli rajoitettu 5:een, jossa oli 2 uutta tulokasta ja 3 remiksaajaa (selitämme nämä käsitteet myöhemmin). Kuitenkin, on-chain transaktiomaksujen havaittu nousu vuonna 2023 sai Samourai-tiimit miettimään malliaan uudelleen parantaakseen yksityisyyttä samalla kun kustannuksia vähennetään. Näin ollen ottaen huomioon maksujen markkinatilanteen ja osallistujien määrän, koordinaattori voi nyt järjestää coinjoineja, joihin sisältyy 6, 7 tai 8 osallistujaa. Näitä parannettuja istuntoja kutsutaan "_Surge Cycles_" -nimellä. On tärkeää huomata, että riippumatta konfiguraatiosta, Whirlpool-coinjoineissa on aina vain 2 uutta tulokasta.

Näin ollen Whirlpool-transaktiot ovat luonteeltaan samanlaisia syötteiden ja tuotosten määrältä, jotka voivat olla:
- 5 syötettä ja 5 tuotosta;
![coinjoin](assets/notext/2.webp)
- 6 syötettä ja 6 tuotosta;
![coinjoin](assets/notext/3.webp)
- 7 syötettä ja 7 tuotosta;
![coinjoin](assets/notext/4.webp)- 8 syötettä ja 8 lähtöä.
![coinjoin](assets/notext/5.webp)
Whirlpoolin ehdottama malli perustuu näin ollen pieniin coinjoin-transaktioihin. Toisin kuin Wasabi ja JoinMarket, joissa anonsettien vahvuus perustuu osallistujien määrään yhdessä syklissä, Whirlpool panostaa useiden pienten syklien ketjuttamiseen.

Tässä mallissa käyttäjä maksaa maksut vain ensimmäisellä kerralla liittyessään altaaseen, mahdollistaen heidän osallistumisen lukuisiin uudelleensekoituksiin ilman lisämaksuja. Uudet tulokkaat kattavat kaivosmaksut uudelleensekoittajille.

Jokaisen lisäcoinjoinin myötä, johon kolikko osallistuu yhdessä aiemmin kohdattujen vertaistensa kanssa, anonsetit kasvavat eksponentiaalisesti. Tavoitteena on siis hyödyntää näitä ilmaisia uudelleensekoituksia, jotka jokaisella kerralla vahvistavat kunkin sekoitetun kolikon anonsettien tiheyttä.

Whirlpool suunniteltiin ottaen huomioon kaksi tärkeää vaatimusta:
- Toteutuksen saavutettavuus mobiililaitteilla, ottaen huomioon, että Samourai Wallet on ensisijaisesti älypuhelinsovellus;
- Uudelleensekoitussyklien nopeus anonsettien merkittävän kasvun edistämiseksi.
Nämä imperatiivit ohjasivat Samourai Walletin kehittäjiä Whirlpoolin suunnittelussa, johdattaen heidät rajoittamaan osallistujien määrää per sykli. Liian vähäinen osallistujamäärä olisi vaarantanut coinjoinin tehokkuuden, drastisesti vähentäen jokaisessa syklissä tuotettuja anonsetteja, kun taas liian suuri osallistujamäärä olisi aiheuttanut hallinnollisia ongelmia mobiilisovelluksissa ja hidastanut syklien kulkua.
**Lopulta Whirlpoolissa ei tarvita suurta osallistujamäärää per coinjoin, koska anonsetit saavutetaan kerryttämällä useita coinjoin-syklejä.**

[-> Lue lisää Whirlpoolin anonseteista.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

### Altaat ja coinjoin-maksut
Jotta nämä monet syklit voisivat tehokkaasti lisätä sekoitettujen kolikoiden anonsetteja, tietty kehys on määriteltävä käytettävien UTXO-määrien rajoittamiseksi. Whirlpool määrittelee siis erilaisia altaita.

Allas edustaa ryhmää käyttäjiä, jotka haluavat sekoittua yhteen, ja jotka sopivat UTXO:n käyttämästä määrästä coinjoin-prosessin optimoimiseksi. Jokainen allas määrittelee kiinteän määrän UTXO:lle, jota käyttäjän on noudatettava osallistuakseen. Näin ollen coinjoineja suorittaaksesi Whirlpoolissa, sinun on valittava allas. Tällä hetkellä saatavilla olevat altaat ovat seuraavat:
- 0,5 bitcoineja;
- 0,05 bitcoinia;
- 0,01 bitcoinia;
- 0,001 bitcoinia (= 100 000 sats).

Liittyessäsi altaaseen bitcoineillasi, ne jaetaan tuottamaan UTXO:ja, jotka ovat täysin homogeenisia altaan muiden osallistujien UTXO:jen kanssa. Jokaisella altaalla on maksimiraja; näin ollen, mikäli määrä ylittää tämän rajan, sinun on joko tehtävä kaksi erillistä sisääntuloa samassa altaassa tai suunnattava toiseen altaaseen, jossa on suurempi määrä:

| Allas (bitcoin) | Maksimimäärä per sisääntulo (bitcoin) |
|----------------|--------------------------------------|
| 0,5            | 35                                   |
| 0,05           | 3,5                                  |
| 0,01           | 0,7                                  |
| 0,001          | 0,025                                |
Kuten aiemmin mainittiin, UTXO katsotaan kuuluvaksi pooliin, kun se on valmis integroitavaksi coinjoiniin. Tämä ei kuitenkaan tarkoita, että käyttäjä menettäisi sen hallinnan. **Eri sekoituskiertojen aikana säilytät täyden kontrollin avaimiisi ja siten myös bitcoineihisi.** Tämä erottaa coinjoin-tekniikan muista keskitetyistä sekoitustekniikoista.
Coinjoin-pooliin liittyäkseen on maksettava palvelumaksut sekä louhintamaksut. Palvelumaksut ovat kiinteät jokaiselle poolille ja niiden tarkoituksena on korvata Whirlpoolin kehityksestä ja ylläpidosta vastaavat tiimit.
Whirlpoolin käytöstä maksettavat palvelumaksut on maksettava vain kerran pooliin liittyessä. Tämän jälkeen sinulla on mahdollisuus osallistua rajattomaan määrään uudelleensekoituksia ilman lisämaksuja. Tässä ovat nykyiset kiinteät maksut kullekin poolille:

| Pooli (bitcoin) | Sisäänpääsymaksu (bitcoin) |
|-----------------|----------------------------|
| 0.5             | 0.0175                     |
| 0.05            | 0.00175                    |
| 0.01            | 0.0005 (50,000 sats)       |
| 0.001           | 0.00005 (5,000 sats)       |


Nämä maksut toimivat käytännössä sisäänpääsylippuna valittuun pooliin riippumatta siitä, kuinka paljon laitat coinjoiniin. Näin ollen, liityitpä 0.01 pooliin tasan 0.01 BTC:llä tai astuit sisään 0.5 BTC:llä, maksut pysyvät samoina absoluuttisina arvoina.

Ennen coinjoineihin siirtymistä käyttäjällä on siis valittavanaan kaksi strategiaa:
- Valita pienempi pooli minimoidakseen palvelumaksut, tietäen, että he saavat vastineeksi useita pieniä UTXOja;
- Tai valita suurempi pooli, suostuen maksamaan korkeampia maksuja saadakseen lopputuloksena vähemmän UTXOja, mutta suurempaa arvoa.

Yleensä ei suositella useiden sekoitettujen UTXOjen yhdistämistä coinjoin-kiertojen jälkeen, koska se voisi vaarantaa saavutetun luottamuksellisuuden, erityisesti Common-Input-Ownership Heuristic (CIOH) -heuristiikan vuoksi. Siksi voi olla viisasta valita suurempi pooli, vaikka se tarkoittaisikin enemmän maksamista, välttääkseen liian monta pientä arvoa olevaa UTXOa tuloksena. Käyttäjän on punnittava näitä kompromisseja valitakseen mieluisan poolin.

Palvelumaksujen lisäksi on otettava huomioon myös kaikkiin Bitcoin-siirtoihin liittyvät louhintamaksut. Whirlpoolin käyttäjänä sinun on maksettava louhintamaksut valmistelutapahtumasta (`Tx0`) sekä ensimmäisestä coinjoinista. Kaikki sitä seuraavat uudelleensekoitukset ovat ilmaisia, kiitos Whirlpoolin mallin, joka perustuu uusien osallistujien maksuihin.

Todellakin, jokaisessa Whirlpool-coinjoinissa kaksi sisääntulijaa ovat uusia osallistujia. Muut sisääntulot tulevat uudelleensekoittajilta. Tuloksena louhintamaksut kaikille tapahtuman osallistujille kattavat nämä kaksi uutta osallistujaa, jotka sitten myös hyötyvät ilmaisista uudelleensekoituksista:
![coinjoin](assets/en/6.webp)
Tämän maksujärjestelmän ansiosta Whirlpool erottuu todella muista coinjoin-palveluista, koska UTXOjen anonimiteettisarjat eivät ole suhteessa käyttäjän maksamaan hintaan. Näin on mahdollista saavuttaa huomattavan korkeat anonymiteettitasot maksamalla vain poolin sisäänpääsymaksu ja kahden siirron (Tx0 ja alkuperäinen sekoitus) louhintamaksut.
On tärkeää huomata, että käyttäjän on myös katettava louhintamaksut, jotta hän voi nostaa UTXO:nsa poolista suoritettuaan useita coinjoineja, ellei hän ole valinnut `mix to` -vaihtoehtoa, josta keskustelemme alla olevassa oppaassa.

### Whirlpoolin käyttämät HD-lompakon tilit
Suorittaakseen coinjoinin Whirlpoolin kautta, lompakon on luotava useita erillisiä tilejä. Tilillä, HD (*Hierarkkinen Deterministinen*) lompakon kontekstissa, tarkoitetaan osiota, joka on täysin eristetty muista, tämä erottelu tapahtuu lompakon hierarkian kolmannella syvyystasolla, eli `xpub`-tasolla.

HD-lompakko voi teoriassa johtaa jopa `2^(32/2)` eri tiliin. Alkuperäinen tili, jota oletusarvoisesti käytetään kaikissa Bitcoin-lompakoissa, vastaa indeksiä `0'`.

Whirlpooliin sopeutetuissa lompakoissa, kuten Samourai tai Sparrow, käytetään neljää tiliä vastaamaan coinjoin-prosessin tarpeita:
- **Talletus**-tili, joka on tunnistettu indeksillä `0'`;
- **Paha pankki** (tai doxxic change) -tili, joka on tunnistettu indeksillä `2 147 483 644'`;
- **Premix**-tili, joka on tunnistettu indeksillä `2 147 483 645'`;
- **Postmix**-tili, joka on tunnistettu indeksillä `2 147 483 646'`.

Jokainen näistä tileistä täyttää tietyn toiminnon coinjoin-prosessissa.

Kaikki nämä tilit on linkitetty yhteen siemeneen, mikä mahdollistaa käyttäjän pääsyn palauttamisen kaikkiin heidän bitcoineihinsa käyttämällä heidän palautusfraasiaan ja tarvittaessa heidän salasanaansa. On kuitenkin tarpeen määrittää ohjelmistolle, tämän palautustoiminnon aikana, käytetyt eri tili-indeksit.

Katsotaan nyt Whirlpoolin coinjoinin eri vaiheita näillä tileillä.

### Coinjoinien eri vaiheet Whirlpoolissa
**Vaihe 1: Tx0**
Mikä tahansa Whirlpool-coinjoinin lähtökohta on **talletus**-tili. Tätä tiliä käytät automaattisesti, kun luot uuden Bitcoin-lompakon. Tälle tilille on hyvitettävä bitcoinit, jotka haluaa sekoittaa.
`Tx0` edustaa ensimmäistä askelta Whirlpool-sekoitusprosessissa. Sen tavoitteena on valmistella ja tasapainottaa UTXO coinjoinia varten, jakamalla ne yksiköihin, jotka vastaavat valitun poolin määrää, varmistaakseen sekoituksen homogeenisuuden. Tasapainotetut UTXO lähetetään sitten **premix**-tilille. Ero, joka ei mahdu pooliin, erotetaan tiettyyn tiliin: **pahaan pankkiin** (tai "doxxic change").
Tämä alkuperäinen `Tx0`-transaktio palvelee myös sekoituskoordinaattorille maksettavien palvelumaksujen suorittamista. Toisin kuin seuraavat vaiheet, tämä transaktio ei ole yhteistyöllinen; käyttäjän on siis katettava kaikki louhintamaksut:
![coinjoin](assets/en/7.webp)

Tässä `Tx0`-transaktion esimerkissä **talletus**-tililtämme tuleva `372,000 sats` sisääntulo jaetaan useisiin ulostulo UTXOihin, jotka jaetaan seuraavasti:
- Määrä `5,000 sats` tarkoitettu koordinaattorille palvelumaksuina, vastaten pooliin sisäänpääsyä `100,000 sats`;
- Kolme UTXOa valmisteltu sekoitusta varten, ohjattu **premix**-tilillemme ja rekisteröity koordinaattorille. Nämä UTXO:t on tasapainotettu `108,000 sats` kuhunkin, kattaakseen niiden tulevat alkuperäiset sekoituslouhintamaksut;
- Ylijäämä, joka ei mahdu pooliin, koska se on liian pieni, katsotaan myrkylliseksi vaihdoksi. Se lähetetään sen erityiselle tilille. Tässä tapauksessa vaihdos on `40,000 sats`;
- Lopulta on `3,000 sats`, jotka eivät muodosta ulostuloa, mutta ovat louhintamaksuja, jotka ovat tarpeen `Tx0`:n vahvistamiseksi.

Esimerkiksi, tässä on todellinen Whirlpool Tx0 (ei minulta): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**Vaihe 2: Myrkyllinen vaihdos**
Ylijäämä, jota ei voitu integroida pooliin, tässä tapauksessa vastaten `40,000 sats`, ohjataan **pahaan pankkiin** tilille, jota kutsutaan myös "myrkylliseksi vaihdokseksi", varmistaakseen tiukan eron lompakon muista UTXO:ista.

Tämä UTXO on vaarallinen käyttäjän yksityisyydelle, sillä se ei ainoastaan ole yhä kiinni menneisyydessään, ja siten mahdollisesti käyttäjän identiteetissä, mutta lisäksi se merkitään kuuluvaksi käyttäjälle, joka on suorittanut coinjoinin.
Jos tämä UTXO yhdistetään sekoitettuihin ulostuloihin, ne menettävät kaiken coinjoin-syklien aikana saavutetun luottamuksellisuuden, erityisesti Common-Input-Ownership-Heuristic (CIOH) vuoksi. Jos se yhdistetään muihin myrkyllisiin vaihdoksiin, käyttäjä riskeeraa menettävänsä luottamuksellisuuden, koska tämä linkittää eri coinjoin-syklien syötteet. Siksi sitä on käsiteltävä varoen. Tämän myrkyllisen UTXO:n hallinnointitapa tarkennetaan tämän artikkelin viimeisessä osassa, ja tulevat oppaat käsittelevät näitä menetelmiä syvällisemmin PlanB Networkissa.

**Vaihe 3: Alkuperäinen sekoitus**
Kun `Tx0` on valmis, tasapainotetut UTXO:t lähetetään lompakkomme **esisekoitus**-tilille, valmiina esiteltäväksi ensimmäiseen coinjoin-sykliinsä, jota kutsutaan myös "alkuperäiseksi sekoitukseksi". Jos, kuten esimerkissämme, `Tx0` tuottaa useita UTXO:ja sekoitusta varten, kukin niistä integroidaan erilliseen alkuperäiseen coinjoiniin.

Näiden ensimmäisten sekoitusten jälkeen **esisekoitus**-tili tyhjenee, kun taas kolikkomme, maksettuaan louhintamaksut tästä ensimmäisestä coinjoinista, säädellään tarkalleen valitun poolin määrittelemään määrään. Esimerkissämme alkuperäiset UTXO:mme `108 000 sats` on vähennetty tarkalleen `100 000 sats`iin.
![coinjoin](assets/en/8.webp)
**Vaihe 4: Uudelleensekoitukset**
Alkuperäisen sekoituksen jälkeen UTXO:t siirretään **jälkisekoitus**-tilille. Tämä tili kokoaa jo sekoitetut UTXO:t ja ne, jotka odottavat uudelleensekoitusta. Kun Whirlpool-asiakasohjelma on aktiivinen, **jälkisekoitus**-tilin UTXO:t ovat automaattisesti saatavilla uudelleensekoitukseen ja ne valitaan satunnaisesti osallistumaan näihin uusiin sykleihin.

Muistutuksena, uudelleensekoitukset ovat sitten 100% ilmaisia: ei vaadita lisäpalvelumaksuja tai louhintamaksuja. UTXO:jen pitäminen **jälkisekoitus**-tilillä säilyttää niiden arvon muuttumattomana ja samanaikaisesti parantaa niiden anonimiteettisettejä. Siksi on tärkeää sallia näiden kolikoiden osallistuminen useisiin coinjoin-sykleihin. Se ei maksa sinulle mitään, ja se lisää niiden anonymiteetin tasoa.
Kun päätät käyttää sekoitettuja UTXOja, voit tehdä sen suoraan tästä **postmix**-tilistä. On suositeltavaa pitää sekoitetut UTXOt tässä tilissä hyötyäksesi ilmaisista uudelleensekoituksista ja välttääksesi niiden poistumisen Whirlpool-sykliltä, mikä voisi vähentää niiden luottamuksellisuutta.
Kuten seuraavassa oppaassa näemme, on myös `mix to` -vaihtoehto, joka tarjoaa mahdollisuuden automaattisesti lähettää sekoitetut kolikkosi toiseen lompakkoon, kuten kylmälompakkoon, määritellyn määrän coinjoineja jälkeen.
Teorian käsittelyn jälkeen sukellamme käytäntöön oppaan avulla, joka käsittelee Whirlpoolin käyttöä Samourai Wallet Android-sovelluksen kautta!
## Opas: Coinjoin Whirlpool Samourai Walletissa
Whirlpoolin käyttöön on lukuisia vaihtoehtoja. Haluan tässä esitellä Samourai Wallet -vaihtoehdon (ilman Dojoa), avoimen lähdekoodin Bitcoin-lompakonhallintasovelluksen Androidille.

Sekoitusten tekeminen Samouraissa ilman Dojoa on melko helppoa, nopeaa pystyttää, eikä vaadi muuta laitetta kuin Android-puhelimen ja internet-yhteyden.

Tällä menetelmällä on kuitenkin kaksi merkittävää haittapuolta:
- Coinjoinit tapahtuvat vain, kun Samourai on taustalla käynnissä ja yhdistettynä. Tämä tarkoittaa, että jos haluat sekoittaa ja uudelleensekoittaa bitcoinejasi 24/7, sinun on pidettävä Samourai jatkuvasti päällä;
- Jos käytät Whirlpoolia Samourai Walletin kanssa ottamatta yhteyttä omaan Dojoosi, sovelluksesi on yhdistettävä Samourai-tiimien ylläpitämään palvelimeen, ja paljastat heille lompakkosi `xpub`-tiedon. Nämä nimettömät tiedot ovat tarpeen, jotta sovelluksesi löytää transaktiosi.

Ihanteellinen ratkaisu näiden rajoitusten voittamiseen on oman Dojon käyttöönotto yhdistettynä Whirlpool CLI -instanssiin henkilökohtaisessa Bitcoin-nodessasi. Näin vältät kaiken tietovuodon ja saavutat täydellisen riippumattomuuden. Vaikka alla esitetty opas on hyödyllinen tietyille tavoitteille tai aloittelijoille, todellisen coinjoin-istunnon optimoimiseksi suositellaan oman Dojon käyttöä. Yksityiskohtainen opas tämän konfiguraation pystyttämiseen on pian saatavilla PlanB Networkissa.

### Samourai Walletin asentaminen
Aloittaaksesi tarvitset tietenkin Samourai Wallet -sovelluksen. Voit ladata sen suoraan viralliselta verkkosivustolta APK:n kautta, heidän GitLabistaan tai Google Play Kaupasta.

### Ohjelmistolompakon luominen
Ohjelmiston asentamisen jälkeen sinun on edettävä luomaan Bitcoin-lompakko Samouraissa. Jos sinulla on jo yksi, voit siirtyä suoraan seuraavaan vaiheeseen.

Sovelluksen avauduttua paina sinistä `Start`-painiketta. Sinua pyydetään valitsemaan sijainti puhelimesi tiedostoissa, johon uuden lompakkosi salattu varmuuskopio tallennetaan.

![samourai](assets/notext/9.webp)
Aktivoi Tor napsauttamalla vastaavaa kohtaa. Tässä vaiheessa sinulla on myös mahdollisuus valita tietty Dojo. Tässä oppaassa jatkamme kuitenkin oletus-Dojon kanssa; joten voit jättää vaihtoehdon pois käytöstä. Kun Tor on yhdistetty, paina `Luo uusi lompakko` -painiketta.
![samourai](assets/notext/10.webp)

Samourai Wallet kehottaa sinua asettamaan BIP39-salasanan. Tämä lisäsalasana on erittäin tärkeä, sillä se vaikuttaa suoraan yksityisavaimiesi johdannaisuuteen. Tämän salasanan mahdollinen menetys johtaisi kyvyttömyyteen päästä käsiksi bitcoineihisi, mikä tekisi niistä peruuttamattomasti menetettyjä. Samourai-lompakkosi palauttamiseksi on ehdottoman tärkeää, että sinulla on sekä 12 sanan palautuslauseesi että salasana.
On siis olennaista valita vahva salalause ja tehdä yksi tai useampi fyysinen kopio, paperille tai metalliselle alustalle, bitcoinsien turvallisuuden varmistamiseksi. Näiden tehtävien suorittamisen jälkeen, merkitse ruutu `Olen tietoinen, että kadotustapauksessa...`, sitten paina `SEURAAVA`-painiketta.
![samourai](assets/notext/11.webp)

Sinun tulee sen jälkeen määrittää PIN-koodi, joka koostuu 5-8 numerosta. Tämä koodi turvaa pääsyn lompakkoosi puhelimellasi. Sitä pyydetään joka kerta, kun haluat avata Samourai-sovelluksen. Valitse vahva PIN-koodi ja varmista, että teet siitä varmuuskopion. Sen jälkeen voit painaa `SEURAAVA`-painiketta.

![samourai](assets/notext/12.webp)

Samourai pyytää sinua syöttämään PIN-koodisi uudelleen vahvistusta varten. Syötä se, sitten paina `VIIMEISTELE`.

![samourai](assets/notext/13.webp)

Tämän jälkeen pääset käsiksi palautusfraasiisi, joka koostuu 12 sanasta. Tämä fraasi mahdollistaa lompakkosi palauttamisen aiemmin syötetyn salalauseen avulla. On erittäin suositeltavaa tehdä yksi tai useampi kopio tästä fraasista fyysiselle medialle, kuten paperille tai metallimateriaalille, bitcoinsiesi turvallisuuden varmistamiseksi ongelmatilanteessa.

Näiden varmuuskopioiden tekemisen jälkeen sinut ohjataan uuden Samourai-lompakkosi käyttöliittymään.

![samourai](assets/notext/14.webp)

Sinulle tarjotaan mahdollisuutta hankkia PayNym Bot. Voit pyytää sitä, jos haluat, vaikka se ei olekaan välttämätön tässä oppaassa.

![samourai](assets/notext/15.webp)
Ennen kuin jatkat bitcoinsien vastaanottamista tähän uuteen lompakkoon, on erittäin suositeltavaa tarkistaa uudelleen lompakkosi varmuuskopioiden (salalause ja palautusfraasi) pätevyys. Salalauseen tarkistamiseksi voit valita PayNym Bot -kuvakkeen, joka sijaitsee näytön vasemmassa yläkulmassa, ja seurata polkua:
```bash
Asetukset > Vianmääritys > Salalause/varmuuskopiotesti
```

Syötä salalauseesi suorittaaksesi tarkistuksen.

![samourai](assets/notext/16.webp)

Samourai vahvistaa sen olevan pätevä.

![samourai](assets/notext/17.webp)

Palautusfraasin varmuuskopion tarkistamiseksi, pääset käsiksi PayNym Bot -kuvakkeeseen, joka sijaitsee näytön vasemmassa yläkulmassa, ja seuraa tätä polkua:
```bash
Asetukset > Lompakko > Näytä 12 sanan palautusfraasi
```

Samourai näyttää ikkunan, jossa on palautusfraasisi. Varmista, että se vastaa täsmälleen fyysistä varmuuskopiotasi.

Mennäksesi pidemmälle ja suorittaaksesi täydellisen palautustestin, merkitse muistiin lompakkosi todistuselementti, kuten yksi `xpubs`, ja jatka sitten lompakkosi poistamiseen (edellyttäen, että se on vielä tyhjä). Tavoitteena on yrittää palauttaa tämä tyhjä lompakko käyttäen ainoastaan fyysisiä varmuuskopioitasi. Jos palautus onnistuu, tämä osoittaa, että varmuuskopiosi ovat päteviä ja luotettavia.

### Bitcoinsien vastaanottaminen
Lompakon luomisen jälkeen aloitat yhdellä tilillä, joka on tunnistettu indeksillä `0'`. Tämä on **talletus**tili, josta puhuimme aiemmissa osissa. Tälle tilille sinun tulee siirtää bitcoinsit, jotka on tarkoitettu coinjoinsille.

Tehdäksesi tämän, klikkaa sinistä `+` symbolia, joka sijaitsee näytön oikeassa alakulmassa.

![samourai](assets/notext/18.webp)

Klikkaa sitten vihreää `Vastaanota`-painiketta.

![samourai](assets/notext/19.webp)

Samourai luo automaattisesti uuden tyhjän osoitteen bitcoinsien vastaanottamiseksi.

![samourai](assets/notext/20.webp)
Voit lähettää bitcoinit sekoitettavaksi sinne.
![samourai](assets/notext/21.webp)

### Tx0:n tekeminen
Kun transaktio on vahvistettu, voimme aloittaa coinjoin-prosessin. Tehdäksesi tämän, klikkaa sinistä `+` painiketta näytön oikeassa alakulmassa.

![samourai](assets/notext/22.webp)

Klikkaa sitten sinisellä `Whirlpool`.

![samourai](assets/notext/23.webp)

Odota, kunnes Whirlpool alustaa ja Samourai luo tarvittavat tilit.

![samourai](assets/notext/24.webp)

Sitten saavut Whirlpoolin kotisivulle. Klikkaa `Start`.
![samourai](assets/notext/25.webp)
Valitse UTXO **talletus**-tililtä, jonka haluat lähettää coinjoin-kiertoihin, ja klikkaa `Next`.

![samourai](assets/notext/26.webp)

Seuraavassa vaiheessa sinun on valittava maksutaso `Tx0`:lle sekä ensimmäiselle sekoituksellesi. Tämä asetus määrittää, kuinka nopeasti `Tx0` ja ensimmäinen coinjoin (tai ensimmäiset coinjoinit) vahvistetaan. Muista, että `Tx0`:n ja ensimmäisen sekoituksen louhintamaksut ovat sinun vastuullasi, mutta sinun ei tarvitse maksaa louhintamaksuja myöhemmistä uudelleensekoituksista. Voit valita vaihtoehdoista `Low`, `Normal` tai `High`.

![samourai](assets/notext/27.webp)

Samassa ikkunassa sinulla on mahdollisuus valita allas, johon liityt. Koska alun perin valitsin UTXO:n, joka oli `454,258 sats`, ainoa mahdollinen valintani on `100,000 sats` allas. Tällä sivulla esitetään myös altaan palvelumaksut louhintamaksujen lisäksi, mikä mahdollistaa sinun tietää kokonaiskustannukset tälle coinjoin-kiertolle. Jos kaikki sopii sinulle, valitse sopiva allas ja jatka klikkaamalla sinistä `VERIFY CYCLE DETAILS` painiketta.

![samourai](assets/notext/28.webp)

Voit sitten nähdä kaikki coinjoin-kiertosyklisi yksityiskohdat:
- UTXO:jen määrä, jotka tulevat altaaseen;
- aiheutuneet erilaiset maksut;
- doxxic-vaihdon määrä...

Vahvista tiedot, ja klikkaa sitten vihreää `START CYCLE` painiketta.

![samourai](assets/notext/29.webp)

Ikkuna ilmestyy tarjoten sinulle mahdollisuuden merkitä coinjoin-kiertoon tulostasi aiheutuva myrkyllinen vaihto "ei-kulutettavaksi". Valitsemalla `YES`, tämä UTXO ei näy lompakossasi eikä sitä voida valita tuleviin transaktioihin. Se kuitenkin pysyy saavutettavissa lompakkosi UTXO-listassa, jossa voit manuaalisesti muuttaa sen tilaa. On suositeltavaa valita tämä vaihtoehto välttääksesi mahdolliset käsittelyvirheet, jotka voisivat vaarantaa yksityisyytesi myöhemmin. Jos valitset `NO`, myrkyllinen vaihto pysyy käytettävissä lompakossasi. Jos haluat oppia lisää tämän myrkyllisen vaihdon hallinnasta ja käytöstä, suosittelen lukemaan tämän oppaan viimeisen osan.

![samourai](assets/notext/30.webp)

Samourai lähettää sitten Tx0:si.

![samourai](assets/notext/31.webp)

### Coinjoinien tekeminen
Kun Tx0 on lähetetty, löydät sen `Transactions`-välilehdeltä Whirlpool-valikosta.

![samourai](assets/notext/32.webp)
Sinun UTXO:si, jotka ovat valmiita sekoitettaviksi, löytyvät välilehdeltä `Mixing in progress...`, joka vastaa **Premix**-tiliä. ![samourai](assets/notext/33.webp)

Kun `Tx0` on vahvistettu, UTXO:si rekisteröidään automaattisesti koordinaattorille, ja alkuperäiset sekoitukset alkavat peräkkäin automaattisesti.

![samourai](assets/notext/34.webp)

Tarkistamalla `Remixing`-välilehden, joka vastaa **Postmix**-tiliä, näet alkuperäisistä sekoituksista saadut UTXO:t. Nämä kolikot pysyvät valmiina seuraaviin uudelleensekoituksiin, jotka eivät aiheuta lisämaksuja. Suosittelen tutustumaan tähän toiseen artikkeliin oppiaksesi lisää uudelleensekoitusprosessista ja coinjoin-syklin tehokkuudesta: [REMIX - WHIRLPOOL](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)

![samourai](assets/notext/35.webp)

UTXO:n uudelleensekoituksen voi väliaikaisesti keskeyttää painamalla sen oikealla puolella olevaa taukopainiketta. Tehdäksesi sen jälleen uudelleensekoituskelpoiseksi, klikkaa vain samaa painiketta uudelleen. On tärkeää huomata, että yhdellä käyttäjällä ja altaalla voi olla käynnissä vain yksi coinjoin kerrallaan. Näin ollen, jos sinulla on 6 UTXO:a `100 000 sats` valmiina coinjoiniin, vain yksi niistä voidaan sekoittaa. UTXO:n sekoittamisen jälkeen Samourai Wallet valitsee satunnaisesti uuden UTXO:n saatavuudestasi, jotta jokaisen kolikon uudelleensekoitus monipuolistuu ja tasapainottuu.

![samourai](assets/notext/36.webp)

Jotta UTXO:si pysyisivät jatkuvasti saatavilla uudelleensekoitusta varten, on välttämätöntä pitää Samourai-sovellus aktiivisena taustalla. Puhelimeesi pitäisi ilmestyä ilmoitus, joka vahvistaa Whirlpoolin olevan käynnissä. Sovelluksen sulkeminen tai puhelimen sammuttaminen keskeyttää coinjoinit.

### Coinjoinien suorittaminen loppuun
Käyttääksesi sekoitettuja bitcoinejasi, siirry **Postmix**-tiliin, joka on merkitty `Remixing` Whirlpool-valikkojen välilehdissä.

![samourai](assets/notext/37.webp)

Klikkaa sinistä Whirlpool-logoa, joka sijaitsee oikeassa alakulmassa.

![samourai](assets/notext/38.webp)

Sen jälkeen klikkaa `Spend Mixed UTXOs`.

![samourai](assets/notext/39.webp)

Voit sen jälkeen syöttää vastaanottajan osoitteen ja lähetettävän summan, samalla tavalla kuin minkä tahansa muun Samourai Walletilla tehdyn transaktion yhteydessä. Sininen tausta osoittaa, että varoja käytetään Whirlpool-tililtä, eikä **talletus**-tililtä.

![samourai](assets/notext/40.webp)

Klikkaamalla kolmea pientä pistettä oikeassa yläkulmassa, voit valita tiettyjä UTXO:ja.
![samourai](assets/notext/41.webp)
Klikkaamalla valkoista neliötä ikkunan oikeassa yläkulmassa voit skannata vastaanottajan osoitteen QR-koodin kamerallasi.

![samourai](assets/notext/42.webp)

Syötä tarvittavat tiedot maksutapahtumaasi varten, ja klikkaa sen jälkeen sinistä `VERIFY TRANSACTION`-painiketta.

![samourai](assets/notext/43.webp)
Seuraavassa vaiheessa sinulla on mahdollisuus muuttaa maksutapahtumasi palkkiotasoa. Voit myös ottaa käyttöön Stonewall-vaihtoehdon valitsemalla vastaavan ruudun. Jos Stonewall-vaihtoehto ei ole valittavissa, se tarkoittaa, että **Postmix**-tilisi ei sisällä riittävän suurta UTXO:ta tukemaan tätä tiettyä tapahtumarakennetta.
[-> Lue lisää Stonewall-tapahtumista.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

Jos kaikki on mielestäsi kunnossa, klikkaa vihreää `SEND ... BTC` -painiketta.

![samourai](assets/notext/44.webp)

Samourai ryhtyy sitten allekirjoittamaan maksutapahtumasi ennen sen lähettämistä verkkoon. Sinun tarvitsee vain odottaa, kunnes se lisätään lohkoon louhijan toimesta.

![samourai](assets/notext/45.webp)

### SCODEn käyttäminen
Joskus Samourai Wallet -tiimit tarjoavat "SCODEja". SCODE on promokoodi, joka tarjoaa alennuksen altaan palvelumaksuista. Samourai Wallet tarjoaa ajoittain tällaisia koodeja käyttäjilleen erityistapahtumien aikana. Neuvon sinua [seuraamaan Samourai Walletia](https://twitter.com/SamouraiWallet) sosiaalisessa mediassa, jotta et jää paitsi tulevista SCODEista.

SCODEn käyttämiseksi Samouraissa, ennen uuden coinjoin-syklin aloittamista, mene Whirlpool-valikkoon ja valitse kolme pientä pistettä näytön oikeassa yläkulmassa.

![samourai](assets/notext/46.webp)

Klikkaa `SCODE (promo code) Whirlpool`.

![samourai](assets/notext/47.webp)

Syötä SCODE avautuneeseen ikkunaan, ja vahvista klikkaamalla `OK`.

![samourai](assets/notext/48.webp)

Whirlpool sulkeutuu automaattisesti. Odota, että Samourai on valmis latautumaan, ja avaa sitten Whirlpool-valikko uudelleen.

![samourai](assets/notext/49.webp)

Varmista, että SCODEsi on rekisteröity oikein klikkaamalla vielä kerran kolmea pientä pistettä ja valitsemalla `SCODE (promo code) Whirlpool`. Jos kaikki on kunnossa, olet valmis aloittamaan uuden Whirlpool-syklin alennetulla palvelumaksulla. On tärkeää huomata, että nämä SCODEt ovat väliaikaisia: ne pysyvät voimassa muutaman päivän ajan ennen kuin muuttuvat vanhentuneiksi.

## Miten tietää coinjoin-sykliemme laatu?
Jotta coinjoin olisi todella tehokas, on olennaista, että syötteiden ja tuottojen määrissä on hyvä yhtenäisyys. Tämä yhtenäisyys lisää mahdollisten tulkintojen määrää ulkopuolisen tarkkailijan silmissä, lisäten näin epävarmuutta tapahtuman ympärillä. Tämän coinjoinin tuottaman epävarmuuden määrää voidaan arvioida laskemalla tapahtuman entropia. Näiden indikaattorien syvällisempään tutkimiseen viittaan sinut oppaaseen: [BOLTZMANN CALCULATOR](https://planb.network/en/tutorials/privacy/boltzmann-entropy). Whirlpool-malli tunnustetaan sellaiseksi, joka tuo eniten yhtenäisyyttä coinjoineihin.
Seuraavaksi arvioidaan useiden coinjoin-syklien suorituskykyä ryhmien laajuuden perusteella, joihin kolikko on piilotettu. Näiden ryhmien koko määrittelee niin kutsutut anonsetit. Anonsetteja on kahta tyyppiä: ensimmäinen arvioi saavutetun yksityisyyden retrospektiivisen analyysin (nykyhetkestä menneisyyteen) perusteella ja toinen, prospektiivisen analyysin (menneisyydestä nykyhetkeen) perusteella. Näiden kahden indikaattorin tarkempaa selitystä varten kutsun sinut tutustumaan oppaaseen: [WHIRLPOOL STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)
## Miten hallita postmixiä?
Coinjoin-syklien suorittamisen jälkeen paras strategia on pitää UTXO:si **postmix**-tilillä odottamassa tulevaa käyttöä. On jopa suositeltavaa antaa niiden remixautua loputtomiin, kunnes tarvitset käyttää niitä.

Jotkut käyttäjät saattavat harkita sekoitettujen bitcoinien siirtämistä lompakkoon, joka on suojattu laitteistolompakolla. Tämä on mahdollista, mutta on tärkeää noudattaa tarkasti Samourai Walletin suosituksia, jotta hankittu luottamuksellisuus ei vaarannu.

UTXO:iden yhdistäminen on yleisin virhe. On välttämätöntä välttää sekoitettujen UTXO:iden yhdistämistä sekoittamattomien UTXO:iden kanssa samassa siirrossa, jotta vältetään CIOH (*Common-Input-Ownership-Heuristic*). Tämä vaatii huolellista UTXO:idesi hallintaa lompakossasi, erityisesti merkinnöissä. Coinjoinin ulkopuolella UTXO:iden yhdistäminen on yleensä huono käytäntö, joka usein johtaa luottamuksellisuuden menetykseen, jos sitä ei hallita asianmukaisesti.
Sinun tulisi myös olla valppaana sekoitettujen UTXO:iden konsolidoinnin suhteen keskenään. Kohtuulliset konsolidoinnit ovat mahdollisia, jos sekoitetuilla UTXO:illasi on merkittäviä anonsetteja, mutta tämä vähentää väistämättä kolikoidesi yksityisyyttä. Varmista, että konsolidoinnit eivät ole liian suuria eikä niitä suoriteta riittämättömän määrän remixien jälkeen, sillä tämä riskeeraa dedusoitavien linkkien luomisen UTXO:idesi välille ennen ja jälkeen coinjoin-syklien. Epävarmuuden vallitessa näiden toimintojen suhteen paras käytäntö on olla konsolidoimatta postmix-UTXO:ita ja siirtää ne yksitellen laitteistolompakkoosi, luoden joka kerta uuden tyhjän osoitteen. Muista jälleen kerran merkitä asianmukaisesti jokainen vastaanotettu UTXO.

On myös suositeltavaa välttää postmix-UTXO:idesi siirtämistä lompakkoon, joka käyttää epätavallisia skriptejä. Esimerkiksi, jos tulet Whirlpooliin multisig-lompakosta, joka käyttää `P2WSH`-skriptejä, on vähän mahdollisuuksia, että sekoitut muiden samantyyppistä lompakkoa alun perin käyttävien käyttäjien kanssa. Jos poistut postmixistä tähän samaan multisig-lompakkoon, sekoitettujen bitcoiniesi yksityisyystaso heikkenee merkittävästi. Skriptien lisäksi on monia muita lompakon jälkiä, jotka voivat johtaa harhaan.

Kuten minkä tahansa Bitcoin-siirron yhteydessä, on myös sopivaa olla uudelleenkäyttämättä vastaanotto-osoitteita. Jokainen uusi siirto on vastaanotettava uudella tyhjällä osoitteella.

Yksinkertaisin ja turvallisin ratkaisu on antaa sekoitettujen UTXO:idesi levätä **postmix**-tilillään, antaa niiden remixautua ja koskea niihin vain kuluttaaksesi. Samourai- ja Sparrow-lompakoissa on lisäsuojauksia kaikkia näitä ketjuanalyysiin liittyviä riskejä vastaan. Nämä suojaukset auttavat välttämään virheitä.

## Miten hallita doxxic-muutosta?
Seuraavaksi sinun on oltava varovainen doxxic-muutoksen hallinnassa, muutoksen, joka ei voinut päästä coinjoin-altaaseen. Nämä myrkylliset UTXO:t, jotka ovat seurausta Whirlpoolin käytöstä, aiheuttavat riskin yksityisyydellesi, koska ne luovat linkin sinun ja coinjoinin käytön välille. On siis ehdottoman tärkeää käsitellä niitä varoen eikä yhdistää niitä muiden UTXO:iden kanssa, erityisesti sekoitettujen UTXO:iden kanssa. Tässä erilaisia strategioita niiden käyttöön:
- **Sekoita ne pienempiin allasosiin:** Jos myrkyllinen UTXO:si on tarpeeksi suuri päästäkseen yksin pienempään altaaseen, harkitse sen sekoittamista. Tämä on usein paras vaihtoehto. On kuitenkin ratkaisevan tärkeää, ettei useita myrkyllisiä UTXO:ja yhdistetä päästäkseen altaaseen, sillä tämä voisi yhdistää eri merkintäsi.
- **Merkitse ne "ei-kulutettaviksi":** Toinen lähestymistapa on lopettaa niiden käyttö, merkitä ne "ei-kulutettaviksi" niille omistetussa tilissä ja vain Hodl. Tämä varmistaa, ettet vahingossa käytä niitä. Jos bitcoinin arvo nousee, voi ilmestyä uusia altaita, jotka sopivat paremmin myrkyllisille UTXO:illesi;
- **Tee lahjoituksia:** Harkitse lahjoitusten tekemistä, vaikka vaatimattomia, kehittäjille, jotka työskentelevät Bitcoinin ja sen liittyvän ohjelmiston parissa. Voit myös lahjoittaa järjestöille, jotka hyväksyvät BTC:tä. Jos myrkyllisten UTXO:idesi hallinta tuntuu liian monimutkaiselta, voit yksinkertaisesti päästä eroon niistä tekemällä lahjoituksen;
- **Osta lahjakortteja:** Alustat, kuten [Bitrefill](https://www.bitrefill.com/), mahdollistavat bitcoinien vaihtamisen lahjakortteihin, joita voidaan käyttää eri kauppiailla. Tämä voi olla tapa päästä eroon myrkyllisistä UTXO:istasi menettämättä niihin liittyvää arvoa;
- **Yhdistä ne Moneroon:** Samourai Wallet tarjoaa nyt atomivaihtopalvelun BTC:n ja XMR:n välillä. Tämä on ihanteellinen tapa hallita myrkyllisiä UTXO:ja yhdistämällä ne Moneroon, vaarantamatta yksityisyyttäsi KYC:n kautta, ennen niiden lähettämistä takaisin Bitcoiniin. Tämä vaihtoehto voi kuitenkin olla kallis louhintamaksujen ja likviditeettirajoitteiden vuoksi maksettavan preemion suhteen;
- **Lähetä ne Lightning-verkkoon:** Näiden UTXO:jen siirtäminen Lightning-verkkoon hyödyntääkseen pienempiä transaktiomaksuja on vaihtoehto, joka voi olla mielenkiintoinen. Tämä menetelmä voi kuitenkin paljastaa tiettyjä tietoja riippuen Lightningin käytöstäsi ja siksi sitä tulisi harjoittaa varoen.

Yksityiskohtaisia ohjeita näiden eri tekniikoiden toteuttamiseen tarjotaan pian PlanB Networkissa.

**Lisäresurssit:**
[Samourai Walletin video-opas](https://planb.network/tutorials/wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)
- [Samourai Walletin dokumentaatio - Whirlpool](https://docs.samourai.io/whirlpool/basic-concepts);
- [Twitter-ketju coinjoineista](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Blogikirjoitus coinjoineista](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).