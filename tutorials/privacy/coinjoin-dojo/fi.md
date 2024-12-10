---
name: Coinjoin - Dojo
description: Kuinka suorittaa coinjoin omalla Dojollasi?
---
![cover](assets/cover.webp)

***VAROITUS:** Samourai Walletin perustajien pidätyksen ja heidän palvelimiensa takavarikoinnin jälkeen 24. huhtikuuta Whirlpool-työkalu ei enää toimi, edes niille henkilöille, joilla on oma Dojo tai jotka käyttävät Sparrow Walletia. On kuitenkin mahdollista, että tämä työkalu voidaan palauttaa käyttöön tulevina viikkoina tai käynnistää uudelleen eri tavalla. Lisäksi tämän artikkelin teoreettinen osa pysyy relevanttina ymmärtämään yleisesti coinjoinien periaatteita ja tavoitteita (ei pelkästään Whirlpool), sekä ymmärtämään Whirlpool-mallin tehokkuutta.*

_Seuraamme tiiviisti tämän tapauksen kehitystä sekä siihen liittyvien työkalujen kehitystä. Voitte olla varmoja, että päivitämme tämän oppaan uuden tiedon saataville tullessa._

_Tämä opas on tarkoitettu vain koulutus- ja tiedotustarkoituksiin. Emme kannusta tai hyväksy näiden työkalujen käyttöä rikollisiin tarkoituksiin. Jokaisen käyttäjän on noudatettava oman lainkäyttöalueensa lakeja._

---

Tässä oppaassa opit, mikä coinjoin on ja kuinka suorittaa sellainen käyttäen Samourai Wallet -ohjelmistoa ja Whirlpool-toteutusta, hyödyntäen omaa Dojoasi. Mielestäni tämä menetelmä on tällä hetkellä paras bitcoinsien sekoittamiseen.

## Mikä on coinjoin Bitcoinissa?
**Coinjoin on tekniikka, joka katkaisee bitcoinien jäljitettävyyden lohkoketjussa**. Se perustuu yhteistyöhön perustuvaan transaktioon, jolla on erityinen rakenne, nimeltään coinjoin-transaktio.

Coinjoinit parantavat Bitcoin-käyttäjien yksityisyyttä vaikeuttamalla ketjuanalyysia ulkopuolisille tarkkailijoille. Niiden rakenne mahdollistaa useiden eri käyttäjien kolikoiden yhdistämisen yhdeksi transaktioksi, mikä hämärtää jälkiä ja tekee vaikeaksi määrittää syöttö- ja vastaanotto-osoitteiden välisiä yhteyksiä.

Coinjoinin periaate perustuu yhteistyöhön: useat käyttäjät, jotka haluavat sekoittaa bitcoinejaan, tallettavat samansuuruisia määriä transaktion syötteinä. Nämä määrät jaetaan sitten tasasuuruisina palautuksina jokaiselle käyttäjälle. Transaktion lopussa on mahdotonta yhdistää tiettyä palautusta tunnettuun käyttäjään syötteessä. Syötteiden ja palautusten välillä ei ole suoraa yhteyttä, mikä katkaisee yhteyden käyttäjien ja heidän UTXO:nsa välillä sekä kunkin kolikon historian.
![coinjoin](assets/notext/1.webp)

Esimerkki coinjoin-transaktiosta (ei minulta): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

Jotta coinjoin voidaan suorittaa samalla kun varmistetaan, että jokainen käyttäjä säilyttää hallinnan varoistaan koko ajan, prosessi alkaa transaktion rakentamisella koordinaattorin toimesta, joka sitten lähettää sen osallistujille. Jokainen käyttäjä allekirjoittaa transaktion sen jälkeen, kun on varmistanut, että se sopii heille. Kaikki kerätyt allekirjoitukset integroidaan lopulta transaktioon. Jos käyttäjä tai koordinaattori yrittää ohjata varoja pois muuttamalla coinjoin-transaktion palautuksia, allekirjoitukset osoittautuvat kelvottomiksi, mikä johtaa transaktion hylkäämiseen solmujen toimesta.

Coinjoinin toteutuksia on useita, kuten Whirlpool, JoinMarket tai Wabisabi, joiden tavoitteena on hallita osallistujien koordinointia ja lisätä coinjoin-transaktioiden tehokkuutta.
Tässä oppaassa syvennymme **Whirlpool**-menetelmän toteutukseen, jonka pidän tehokkaimpana ratkaisuna coinjoinien suorittamiseen Bitcoinissa. Vaikka se on saatavilla useissa lompakoissa, tässä oppaassa tutkimme yksinomaan sen käyttöä Samourai Wallet -mobiilisovelluksen kanssa ilman Dojoa.
## Miksi suorittaa coinjoineja Bitcoinissa?
Yksi alkuperäisistä ongelmista missä tahansa vertaisverkkomaksujärjestelmässä on kaksinkertainen kulutus: miten estää pahantahtoisia henkilöitä kuluttamasta samoja rahayksiköitä useita kertoja ilman, että turvaudutaan keskusviranomaiseen välittäjänä?

Satoshi Nakamoto tarjosi ratkaisun tähän dilemmaan Bitcoin-protokollan kautta, vertaisverkkoelektronisen maksujärjestelmän, joka toimii riippumatta mistään keskusviranomaisesta. Hänen valkoisessa kirjassaan hän korostaa, että ainoa tapa todentaa kaksinkertaisen kulutuksen puuttuminen on varmistaa kaikkien maksujärjestelmän sisäisten transaktioiden näkyvyys.

Jotta jokainen osallistuja olisi tietoinen transaktioista, ne on julkaistava julkisesti. Siksi Bitcoinin toiminta perustuu läpinäkyvään ja hajautettuun infrastruktuuriin, joka mahdollistaa minkä tahansa solmuoperaattorin tarkistaa kaikkien elektronisten allekirjoitusten ketjut ja jokaisen kolikon historian sen luomisesta kaivostyöntekijän toimesta.

Bitcoinin lohkoketjun läpinäkyvä ja hajautettu luonne tarkoittaa, että verkon käyttäjä voi seurata ja analysoida kaikkien muiden osallistujien transaktioita. Tämän seurauksena nimettömyys transaktiotasolla on mahdotonta. Kuitenkin, yksilöiden tunnistamisen tasolla nimettömyys säilyy. Toisin kuin perinteisessä pankkijärjestelmässä, jossa jokainen tili on linkitetty henkilöllisyyteen, Bitcoinissa varat liittyvät kryptografisten avainparien kanssa, tarjoten käyttäjille pseudonyymiyden kryptografisten tunnisteiden takana.

Näin ollen Bitcoinin luottamuksellisuus vaarantuu, kun ulkopuoliset tarkkailijat onnistuvat yhdistämään tiettyjä UTXO:ja tunnistettuihin käyttäjiin. Kun tämä yhdistäminen on vahvistettu, on mahdollista jäljittää heidän transaktionsa ja analysoida heidän bitcoinien historiaa. Coinjoin on juuri tekniikka, joka on kehitetty rikkomaan UTXO:jen jäljitettävyys, tarjoten siten tietyn luottamuksellisuuden tason Bitcoin-käyttäjille transaktiotasolla.

## Miten Whirlpool toimii?
Whirlpool erottuu muista coinjoin-menetelmistä käyttämällä "_ZeroLink_" -transaktioita, jotka varmistavat, että syötteiden ja tulosteiden välillä ei ole teknisesti mahdollista olla mitään yhteyttä. Tämä täydellinen sekoitus saavutetaan rakenteella, jossa jokainen osallistuja panostaa identtisen summan syötteenä (lukuun ottamatta kaivosmaksuja), tuottaen näin täydellisesti yhtä suuria tulosteita.
Tämä rajoittava lähestymistapa syötteisiin antaa Whirlpool-coinjoin-transaktioille ainutlaatuisen ominaisuuden: täydellisen determinististen linkkien puuttumisen syötteiden ja tulosteiden välillä. Toisin sanoen, jokaisella tulosteella on yhtä suuri todennäköisyys olla yhdistetty mihin tahansa osallistujaan verrattuna kaikkiin muihin transaktion tulosteisiin.
Alun perin Whirlpool-coinjoinin osallistujien määrä oli rajoitettu 5:een, jossa oli 2 uutta tulokasta ja 3 uudelleensekoittajaa (selitämme nämä käsitteet myöhemmin). Kuitenkin, on-chain transaktiomaksujen havaittu nousu vuonna 2023 sai Samourai-tiimit miettimään malliaan uudelleen parantaakseen yksityisyyttä samalla kun kustannuksia vähennettiin. Näin ollen ottaen huomioon maksujen markkinatilanteen ja osallistujien määrän, koordinaattori voi nyt järjestää coinjoineja, joihin sisältyy 6, 7 tai 8 osallistujaa. Näitä laajennettuja istuntoja kutsutaan "_Surge Cycles_" -nimellä. On tärkeää huomata, että riippumatta asetuksesta, Whirlpool-coinjoineissa on aina vain 2 uutta tulokasta.

Näin ollen Whirlpool-transaktiot ovat tunnusomaisia identtiselle määrälle syötteitä ja tulosteita, jotka voivat olla:
- 5 syötettä ja 5 tulostetta;
![coinjoin](assets/notext/2.webp)
- 6 syötettä ja 6 tulostetta;
![coinjoin](assets/notext/3.webp)
- 7 syötettä ja 7 tulostetta;
![coinjoin](assets/notext/4.webp) - 8 syötettä ja 8 tulostetta.
![coinjoin](assets/notext/5.webp)
Whirlpoolin ehdottama malli perustuu siis pieniin coinjoin-transaktioihin. Toisin kuin Wasabi ja JoinMarket, joissa anonsettien vahvuus perustuu yksittäisen syklin osallistujien määrään, Whirlpool panostaa useiden pienten syklien ketjuttamiseen.

Tässä mallissa käyttäjä maksaa maksut vain ensimmäisellä kerralla liittyessään altaaseen, mahdollistaen heidän osallistumisen lukuisiin uudelleensekoituksiin ilman lisämaksuja. Uudet tulokkaat kattavat kaivosmaksut uudelleensekoittajille.

Jokaisen lisäcoinjoinin, johon kolikko osallistuu yhdessä aiemmin kohdattujen vertaisten kanssa, anonsetit kasvavat eksponentiaalisesti. Tavoitteena on siis hyödyntää näitä ilmaisia uudelleensekoituksia, jotka jokaisella kerralla lisäävät sekoitettuun kolikkoon liittyvien anonsettien tiheyttä.

Whirlpool suunniteltiin ottaen huomioon kaksi tärkeää vaatimusta:
- Toteutuksen saatavuus mobiililaitteilla, ottaen huomioon, että Samourai Wallet on ensisijaisesti älypuhelinsovellus;
- Uudelleensekoitussyklien nopeus anonsettien merkittävän kasvun edistämiseksi.
Nämä imperatiivit ohjasivat Samourai Walletin kehittäjien valintoja Whirlpoolin suunnittelussa, johdattaen heidät rajoittamaan osallistujien määrää per sykli. Liian vähäinen osallistujamäärä olisi vaarantanut coinjoinin tehokkuuden, drastisesti vähentäen jokaisessa syklissä tuotettuja anonsetteja, kun taas liian suuri osallistujamäärä olisi aiheuttanut hallinnollisia ongelmia mobiilisovelluksissa ja hidastanut syklien kulkua.
**Lopulta Whirlpoolissa ei tarvita suurta osallistujamäärää per coinjoin, koska anonsetit saavutetaan kerryttämällä useita coinjoin-syklejä.**

[-> Lue lisää Whirlpoolin anonseteista.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

### Altaat ja coinjoin-maksut
Jotta nämä monet syklit voisivat tehokkaasti lisätä sekoitettujen kolikoiden anonsetteja, tietty kehys on määriteltävä käytettävien UTXO-määrien rajoittamiseksi. Whirlpool määrittelee siis erilaisia altaita.

Allas edustaa käyttäjäryhmää, joka haluaa sekoittua yhteen, ja he sopivat UTXO:n määrästä coinjoin-prosessin optimoimiseksi. Jokainen allas määrittelee kiinteän määrän UTXO:lle, jota käyttäjän on noudatettava osallistuakseen. Näin ollen coinjoineja suorittaaksesi Whirlpoolissa sinun on valittava allas. Tällä hetkellä saatavilla olevat altaat ovat seuraavat:
- 0,5 bitcoineja;
- 0,05 bitcoinia;
- 0,01 bitcoinia;
- 0,001 bitcoinia (= 100 000 sats).

Liittyessäsi altaaseen bitcoineillasi, ne jaetaan tuottamaan UTXO:ja, jotka ovat täysin homogeenisia altaan muiden osallistujien UTXO:jen kanssa. Jokaisella altaalla on maksimiraja; näin ollen, mikäli määrä ylittää tämän rajan, sinun on joko tehtävä kaksi erillistä sisääntuloa samassa altaassa tai siirryttävä toiseen altaaseen, jossa on suurempi määrä:

| Allas (bitcoin) | Maksimimäärä per sisääntulo (bitcoin) |
|----------------|------------------------------------|
| 0,5            | 35                                 |
| 0,05           | 3,5                                |
| 0,01           | 0,7                                |
| 0,001          | 0,025                              |
Kuten aiemmin mainittiin, UTXO katsotaan kuuluvaksi pooliin, kun se on valmis integroitavaksi coinjoiniin. Tämä ei kuitenkaan tarkoita, että käyttäjä menettäisi sen hallinnan. **Eri sekoituskiertojen aikana säilytät täyden kontrollin avaimiisi ja siten myös bitcoineihisi.** Tämä erottaa coinjoin-tekniikan muista keskitetyistä sekoitustekniikoista.

Coinjoin-pooliin liittyäkseen on maksettava palvelumaksut sekä louhintamaksut. Palvelumaksut ovat kiinteät jokaiselle poolille ja niiden tarkoituksena on korvata Whirlpoolin kehityksestä ja ylläpidosta vastaaville tiimeille.
Whirlpoolin käyttämisen palvelumaksut maksetaan vain kerran pooliin liityttäessä. Tämän vaiheen jälkeen sinulla on mahdollisuus osallistua rajattomaan määrään uudelleensekoituksia ilman lisämaksuja. Tässä ovat nykyiset kiinteät maksut kullekin poolille:

| Pooli (bitcoin) | Liittymismaksu (bitcoin) |
|-----------------|--------------------------|
| 0.5             | 0.0175                   |
| 0.05            | 0.00175                  |
| 0.01            | 0.0005 (50,000 sats)     |
| 0.001           | 0.00005 (5,000 sats)     |


Nämä maksut toimivat käytännössä sisäänpääsylippuna valittuun pooliin riippumatta siitä, kuinka paljon laitat coinjoiniin. Näin ollen, liityitpä 0.01 pooliin tasan 0.01 BTC:llä tai astuit sisään 0.5 BTC:llä, maksut pysyvät samoina absoluuttisina arvoina.

Ennen coinjoineihin siirtymistä käyttäjällä on siis valittavanaan kaksi strategiaa:
- Valita pienempi pooli palvelumaksujen minimoimiseksi, tietäen, että he saavat vastineeksi useita pieniä UTXOja;
- Tai valita suurempi pooli, suostuen maksamaan korkeampia maksuja saadakseen lopuksi vähemmän, mutta suuremman arvon UTXOja.

Yleensä ei suositella useiden sekoitettujen UTXOjen yhdistämistä coinjoin-kiertojen jälkeen, sillä tämä voisi vaarantaa hankitun luottamuksellisuuden, erityisesti Common-Input-Ownership Heuristic (CIOH) -heuristiikan vuoksi. Siksi voi olla viisasta valita suurempi pooli, vaikka se tarkoittaisikin enemmän maksamista, välttääkseen liian monta pientä arvon UTXOa tulosteessa. Käyttäjän on punnittava näitä vaihtoehtoja valitakseen mieluisan poolin.

Palvelumaksujen lisäksi on otettava huomioon myös kaikkiin Bitcoin-siirtoihin liittyvät louhintamaksut. Whirlpoolin käyttäjänä sinun on maksettava louhintamaksut valmistelutapahtumasta (`Tx0`) sekä ensimmäisestä coinjoinista. Kaikki sitä seuraavat uudelleensekoitukset ovat ilmaisia, kiitos Whirlpoolin mallin, joka perustuu uusien osallistujien maksuihin.

Todellakin, jokaisessa Whirlpool-coinjoinissa kaksi syötteistä on uusia osallistujia. Muut syötteet tulevat uudelleensekoittajilta. Tämän seurauksena kaikkien tapahtumaan osallistuvien louhintamaksut kattavat nämä kaksi uutta osallistujaa, jotka sitten myös hyötyvät ilmaisista uudelleensekoituksista:
![coinjoin](assets/en/6.webp)
Tämän maksujärjestelmän ansiosta Whirlpool erottuu todella muista coinjoin-palveluista, koska UTXOjen anonimiteettisarjat eivät ole suhteessa käyttäjän maksamaan hintaan. Näin on mahdollista saavuttaa huomattavan korkeat anonymiteettitasot maksamalla vain poolin sisäänpääsymaksu ja kahden siirron (valmistelutapahtuma `Tx0` ja alkuperäinen sekoitus) louhintamaksut.
On tärkeää huomata, että käyttäjän on myös katettava louhintamaksut, jotta hän voi nostaa UTXO:nsa poolista suoritettuaan useita coinjoineja, ellei hän ole valinnut `mix to` -vaihtoehtoa, josta keskustelemme alla olevassa oppaassa.
### Whirlpoolin käyttämät HD-lompakon tilit
Suorittaakseen coinjoinin Whirlpoolin kautta, lompakon on luotava useita erillisiä tilejä. Tili, HD (*Hierarkkinen Deterministinen*) lompakon kontekstissa, muodostaa osion, joka on täysin eristetty muista, tämä erottelu tapahtuu lompakon hierarkian kolmannella syvyyden tasolla, eli `xpub`-tasolla.

HD-lompakko voi teoriassa johtaa jopa `2^(32/2)` eri tiliin. Alkuperäinen tili, jota oletuksena käytetään kaikissa Bitcoin-lompakoissa, vastaa indeksiä `0'`.

Whirlpooliin sopeutetuissa lompakoissa, kuten Samourai tai Sparrow, käytetään 4 tiliä vastaamaan coinjoin-prosessin tarpeita:
- **Talletus**tili, joka on tunnistettu indeksillä `0'`;
- **Paha pankki** (tai doxxic change) tili, joka on tunnistettu indeksillä `2 147 483 644'`;
- **Premix**tili, joka on tunnistettu indeksillä `2 147 483 645'`;
- **Postmix**tili, joka on tunnistettu indeksillä `2 147 483 646'`.

Jokainen näistä tileistä täyttää tietyn toiminnon coinjoinissa.

Kaikki nämä tilit on linkitetty yhteen siemeneen, mikä mahdollistaa käyttäjän pääsyn palauttamisen kaikkiin heidän bitcoineihinsa käyttämällä heidän palautusfraasiaan ja tarvittaessa heidän salasanaansa. On kuitenkin tarpeen määrittää ohjelmistolle, tämän palautusoperaation aikana, käytetyt eri tili-indeksit.

Katsotaan nyt eri vaiheita Whirlpool coinjoinissa näillä tileillä.

### Coinjoinien eri vaiheet Whirlpoolissa
**Vaihe 1: Tx0**
Mikä tahansa Whirlpool coinjoinin lähtökohta on **talletus**tili. Tätä tiliä käytät automaattisesti, kun luot uuden Bitcoin-lompakon. Tälle tilille on hyvitettävä bitcoinit, jotka haluaa sekoittaa.
`Tx0` edustaa ensimmäistä askelta Whirlpoolin sekoitusprosessissa. Sen tavoitteena on valmistella ja tasapainottaa UTXO coinjoinia varten, jakamalla ne yksiköihin, jotka vastaavat valitun poolin määrää, varmistaakseen sekoituksen homogeenisuuden. Tasapainotetut UTXO lähetetään sitten **premix**tilille. Erotus, joka ei mahdu pooliin, erotetaan tiettyyn tiliin: **pahaan pankkiin** (tai "doxxic change").
Tämä alkuperäinen `Tx0`-transaktio palvelee myös sekoituskoordinaattorille maksettavien palvelumaksujen suorittamista. Toisin kuin seuraavat vaiheet, tämä transaktio ei ole yhteistyöllinen; käyttäjän on siis kannettava kaikki louhintamaksut:
![coinjoin](assets/en/7.webp)

Tässä `Tx0`-transaktion esimerkissä **talletus**tililtämme tuleva `372,000 sats` syöte jaetaan useisiin lähtö-UTXOihin, jotka jaetaan seuraavasti:
- Määrä `5,000 sats` on tarkoitettu koordinaattorille palvelumaksuina, vastaten pooliin sisäänpääsyä `100,000 sats`;
- Kolme UTXO:a valmisteltu sekoitusta varten, ohjattu **premix**tilillemme ja rekisteröity koordinaattorille. Nämä UTXO:t on tasapainotettu `108,000 sats` kuhunkin, kattaakseen niiden tulevat alkuperäiset sekoituslouhintamaksut;
- Ylijäämä, joka ei mahdu pooliin, koska se on liian pieni, katsotaan myrkylliseksi vaihdoksi. Se lähetetään sen erityiselle tilille. Tässä tapauksessa vaihdos on `40,000 sats`;
- Lopulta on `3,000 sats`, jotka eivät muodosta ulostuloa, mutta ovat louhintamaksuja, jotka ovat tarpeen `Tx0`:n vahvistamiseksi.

Esimerkiksi, tässä on todellinen Whirlpool Tx0 (ei minulta): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**Vaihe 2: Myrkyllinen vaihdos**
Ylijäämä, jota ei voitu integroida pooliin, tässä tapauksessa `40,000 sats`, ohjataan **pahaan pankkiin** tilille, jota kutsutaan myös "myrkylliseksi vaihdokseksi", varmistaakseen tiukan eron lompakon muista UTXO:ista.

Tämä UTXO on vaarallinen käyttäjän yksityisyydelle, koska se ei ainoastaan ole yhä kiinni menneisyydessään, ja siten mahdollisesti käyttäjän identiteettiin, mutta lisäksi se merkitään kuuluvaksi käyttäjälle, joka on suorittanut coinjoinin.
Jos tämä UTXO yhdistetään sekoitettuihin ulostuloihin, ne menettävät kaiken coinjoin-syklien aikana saavutetun luottamuksellisuuden, erityisesti Common-Input-Ownership-Heuristic (CIOH) vuoksi. Jos se yhdistetään muiden myrkyllisten vaihdosten kanssa, käyttäjä riskeeraa menettävänsä luottamuksellisuuden, koska tämä linkittää eri coinjoin-syklien syötteet. Siksi sitä on käsiteltävä varoen. Tämän myrkyllisen UTXO:n käsittelytapa tarkennetaan tämän artikkelin viimeisessä osassa, ja tulevat oppaat käsittelevät näitä menetelmiä tarkemmin PlanB Networkissa.

**Vaihe 3: Alkuperäinen sekoitus**
Kun `Tx0` on valmis, tasapainotetut UTXO:t lähetetään lompakkomme **premix**-tilille, valmiina esittelemään ensimmäiseen coinjoin-sykliinsä, jota kutsutaan myös "alkuperäiseksi sekoitukseksi". Jos, kuten esimerkissämme, `Tx0` tuottaa useita sekoitettavaksi tarkoitettuja UTXO:ja, kukin niistä integroidaan erilliseen alkuperäiseen coinjoiniin.

Näiden ensimmäisten sekoitusten jälkeen **premix**-tili tyhjenee, kun taas kolikkomme, maksettuaan louhintamaksut tästä ensimmäisestä coinjoinista, säädellään tarkalleen valitun poolin määrittelemään määrään. Esimerkissämme alkuperäiset UTXO:mme `108 000 sats` on vähennetty tarkalleen `100 000 sats`iin.
![coinjoin](assets/en/8.webp)
**Vaihe 4: Uudelleensekoitukset**
Alkuperäisen sekoituksen jälkeen UTXO:t siirretään **postmix**-tilille. Tämä tili kokoaa jo sekoitetut UTXO:t ja ne, jotka odottavat uudelleensekoitusta. Kun Whirlpool-asiakasohjelma on aktiivinen, **postmix**-tilillä olevat UTXO:t ovat automaattisesti saatavilla uudelleensekoitukseen ja ne valitaan satunnaisesti osallistumaan näihin uusiin sykleihin.

Muistutuksena, uudelleensekoitukset ovat sitten 100% ilmaisia: ei vaadita lisäpalvelumaksuja tai louhintamaksuja. UTXO:jen pitäminen **postmix**-tilillä säilyttää niiden arvon muuttumattomana ja parantaa samanaikaisesti niiden anonimiteettisettejä. Siksi on tärkeää sallia näiden kolikoiden osallistuminen useisiin coinjoin-sykleihin. Se ei maksa sinulle mitään, ja se lisää niiden anonymiteetin tasoa.
Kun päätät käyttää sekoitettuja UTXOja, voit tehdä sen suoraan tästä **postmix**-tilistä. On suositeltavaa pitää sekoitetut UTXOt tässä tilissä hyötyäksesi ilmaisista uudelleensekoituksista ja välttääksesi niiden poistumisen Whirlpool-sykliltä, mikä voisi vähentää niiden luottamuksellisuutta.
Kuten seuraavassa oppaassa näemme, on myös `mix to` -vaihtoehto, joka tarjoaa mahdollisuuden automaattisesti lähettää sekoitetut kolikkosi toiseen lompakkoon, kuten kylmälompakkoon, määritellyn määrän coinjoineja jälkeen.
Teorian käsittelyn jälkeen sukellamme käytäntöön oppaan avulla, joka käsittelee Whirlpoolin käyttöä Samourai Wallet Android-sovelluksen kautta, synkronoituna Whirlpool CLI:n ja GUI:n kanssa omassa Dojossasi!
## Opas: Coinjoin Whirlpool omalla Dojollasi
Whirlpoolin käyttöön on monia vaihtoehtoja. Haluan tässä esitellä Samourai Wallet -vaihtoehdon, avoimen lähdekoodin Bitcoin-lompakon hallintasovelluksen Androidille, mutta tällä kertaa **omalla Dojollasi**.

Coinjoinejen suorittaminen Samourai Walletin kautta käyttäen omaa Dojoasi on mielestäni tehokkain strategia Bitcoinin coinjoineihin tähän mennessä. Tämä lähestymistapa vaatii alkuinvestointia asetuksen suhteen, mutta kerran paikoillaan, se tarjoaa mahdollisuuden sekoittaa ja uudelleensekoittaa bitcoinejasi jatkuvasti, 24 tuntia vuorokaudessa, 7 päivää viikossa, ilman tarvetta pitää Samourai-sovellustasi aktiivisena koko ajan. Todellakin, kiitos Whirlpool CLI:n toiminnasta Bitcoin-nodessa, olet aina valmis osallistumaan coinjoineihin. Samourai-sovellus antaa sinulle sitten mahdollisuuden käyttää sekoitettuja varojasi milloin tahansa, missä tahansa, suoraan älypuhelimestasi. Lisäksi, tämä menetelmä tarjoaa edun, ettei sinua yhdistetä koskaan Samourai-tiimien hallinnoimiin palvelimiin, suojellen näin `xpub`iasi miltä tahansa ulkoiselta altistumiselta.

Tämä tekniikka on siis ihanteellinen niille, jotka etsivät maksimaalista yksityisyyttä ja korkealaatuisimpia coinjoin-syklejä. Se vaatii kuitenkin Bitcoin-noden käytettävissäsi ja, kuten myöhemmin näemme, vaatii jonkin verran asetusta. Se on siis paremmin soveltuva keskitason ja edistyneiden käyttäjien käyttöön. Aloittelijoille suosittelen tutustumista coinjoiniin näiden kahden muun oppaan kautta, jotka näyttävät, miten se tehdään Sparrow Walletista tai Samourai Walletista (ilman Dojoa):
- **[Sparrow Wallet coinjoin -opas](https://planb.network/en/tutorials/privacy/coinjoin-sparrow-wallet)**;
- **[Samourai Wallet coinjoin -opas (ilman Dojoa)](https://planb.network/en/tutorials/privacy/coinjoin-samourai-wallet)**.

### Asetuksen Ymmärtäminen
Aloittaaksesi tarvitset Dojon! Dojo on Bitcoin-noden toteutus, joka perustuu Bitcoin Coreen, ja sen on kehittänyt Samourai-tiimit.

Oman Dojosi käyttöönottamiseksi sinulla on mahdollisuus joko asentaa Dojo-nodi itsenäisesti tai hyödyntää Dojoa toisen "node-in-box" Bitcoin-noden ratkaisun päällä. Tällä hetkellä saatavilla olevat vaihtoehdot ovat:
- [RoninDojo](https://ronindojo.io/), joka on Dojo, jota on parannettu lisätyökaluilla, mukaan lukien asennusavustaja ja hallinta-avustaja. Yksityiskohtaisen menettelyn RoninDojon asettamiseksi ja käyttämiseksi kerron tässä toisessa oppaassa: [RONINDOJO V2](https://planb.network/en/tutorials/node/ronin-dojo-v2);
- [Umbrel](https://umbrel.com/) "Samourai Server" -sovelluksella;
- [MyNode](https://mynodebtc.com/) "Dojo" -sovelluksella;
- [Nodl](https://www.nodl.eu/) "Dojo" sovelluksella;
- [Citadel](https://runcitadel.space/) "Samourai" sovelluksella.
![coinjoin](assets/notext/9.webp)
Asetuksessamme tulemme käyttämään kolmea erillistä käyttöliittymää:
- **Samourai Wallet**, joka isännöi Bitcoin-lompakkoamme, joka on omistettu coinjoineille. Saatavilla ilmaiseksi Androidille, tämä FOSS-sovellus mahdollistaa sekoituslompakkosi hallinnan, erityisesti postmix-varojen käytön älypuhelimeltasi;
- **Whirlpool CLI** (_Command Line Interface_), joka toimii Dojoa isännöivällä solmulla. Tämä ohjelmisto pääsee käsiksi Samourai-lompakkosi avaimiin. Se vastaa koordinaattorin kanssa kommunikoinnista ja hallinnoi coinjoineja jatkuvasti. Se toimii kopiona Samourai-lompakostasi solmullasi, valmiina osallistumaan coinjoineihin milloin tahansa;
- **Whirlpool GUI** (_Graphical User Interface_), graafinen käyttöliittymä, jota käytämme Whirlpool CLI:n toiminnan seuraamiseen ja sekoituksen aloittamiseen etänä. Whirlpool GUI tarjoaa visuaalisen esityksen Whirlpool CLI:n suorittamista toiminnoista. Tämä ohjelmisto on asennettava erilliselle tietokoneelle kuin Dojo. Umbrel-, MyNode-, Nodl- ja Citadel-käyttäjille Whirlpool GUI on pakollinen. RoninDojo-käyttäjille Whirlpool GUI -käyttöliittymä on kuitenkin jo integroitu solmun verkkokäyttöliittymään `Whirlpool`-sovelluksen kautta. Täten sinun ei tarvitse asentaa sitä erilliselle PC:lle.

Mielestäni RoninDojon käyttäminen edustaa parasta ratkaisua coinjoinien suorittamiseen Dojon kanssa. Koska tämä solmu-boksi-ohjelmisto on suorassa yhteistyössä Samourai-tiimien kanssa, RoninDojo on paljon optimoidumpi tähän tarkoitukseen. Lisäksi Whirlpool GUI:n integrointi verkkokäyttöliittymään yksinkertaistaa asennusprosessia merkittävästi. Tässä oppaassa selitän silti, miten se tehdään muiden Dojoa integroivien ratkaisujen kanssa (Umbrel, Nodl, MyNode ja Citadel).

### Dojosi valmistelu
Aloittaaksesi sinun on asennettava Dojo ja saatava QR-koodi tai linkki, joka mahdollistaa etäyhteyden siihen. Tämä linkki on Tor-osoite, joka päättyy `.onion`-päätteeseen. Jos käytät RoninDojoa, siirry vain `Pairing`-valikkoon saadaksesi tämän tiedon.
![coinjoin](assets/notext/10.webp)

`Samourai Dojo`-kohdan alla klikkaa `Pair now`-painiketta.

![coinjoin](assets/notext/11.webp)

Yhteys-QR-koodisi ja vastaava linkki näytetään.

![coinjoin](assets/notext/12.webp)

Jos käytät Umbrelia, siirry App Storeen ja etsi `Samourai Server`-sovellus. Se sijaitsee `Bitcoin`-välilehdellä.

![coinjoin](assets/notext/13.webp)

Asenna sovellus.

![coinjoin](assets/notext/14.webp)

Sovelluksen avauduttua sinulla on pääsy QR-koodiin, jolla voit yhdistää Dojoosi.

![coinjoin](assets/notext/15.webp)

Jos käytät toista solmu-boksi-ohjelmistoa, kuten MyNodea, Citadelia tai Nodlia, prosessi on samankaltainen kuin Umbrelilla. Sinun on asennettava Samourai- tai Dojo-sovellus saadaksesi tarvittavat tiedot Dojoosi yhdistämiseksi.

![coinjoin](assets/notext/16.webp)

### Samourai-lompakkosi valmistelu
Kun olet hakenut yhteystiedot Dojoosi, on nyt aika asettaa lompakkosi coinjoineja varten. On kaksi skenaariota: jos sinulla ei vielä ole Samourai Walletia älypuhelimessasi, prosessi on yksinkertainen, luo vain uusi.
Toisaalta, jos sinulla on jo Samourai Wallet, sinun on asennettava sovellus uudelleen yhdistääksesi sen uuteen Dojoon. Tämä vaihe on tarpeellinen, koska Dojoon yhteyden voi muodostaa vain sovelluksen ensimmäisellä käynnistyskerralla. Kuitenkin, kiitos Samourain automaattisesti luoman salatun varmuuskopiotiedoston puhelimessasi, tämä menettely on yksinkertainen ja nopea.

*Jos et ole koskaan käyttänyt Samouraita, voit ohittaa nämä alustavat vaiheet ja siirtyä suoraan sovelluksen asennukseen.*

Ennen kaikkea, varmista että Samourai Wallet -sovelluksesi on ajan tasalla. Tehdäksesi tämän, tarkista Google Play Kauppa tai vertaa sovelluksesi versiota `Asetukset > Muut` siihen, mikä on saatavilla Samourain verkkosivustolla.

![coinjoin](assets/notext/17.webp)

Varmista, että sinulla on Samourai-lompakkosi palautuslause ja että se on luettavissa. Suorita sitten testi BIP39-salasanalauseellesi siirtymällä kohtaan `Asetukset > Vianmääritys > Salasanalauseen/Varakopion testi` vahvistaaksesi sen tarkkuuden.

![coinjoin](assets/notext/18.webp)
Syötä salasanalauseesi, sitten varmista, että Samourai vahvistaa sen pätevyyden.
![coinjoin](assets/notext/19.webp)

Jos salasanalauseesi on virheellinen, tai jos sinulla ei ole palautuslausetta, on ehdottoman tärkeää välittömästi pysäyttää menettely! **Riskinä on menettää bitcoinit tässä toimenpiteessä.** Tässä tapauksessa on suositeltavaa siirtää varasi toiseen lompakkoon ja aloittaa uudella tyhjällä Samourai-lompakolla. Seuraavia vaiheita tulisi noudattaa vain, jos olet varma, että sinulla on kaikki tarvittavat varmuuskopiotiedot ja että salasanalauseesi on pätevä.

Jatka sitten luomalla salattu varmuuskopio lompakostasi ja kopioi se leikepöydällesi. Suorittaaksesi tämän toimenpiteen, klikkaa kolmea pientä pistettä näytön oikeassa yläkulmassa, sitten valitse `Vie lompakon varmuuskopio`.

![coinjoin](assets/notext/20.webp)

**Tästä vaiheesta lähtien, älä kopioi mitään muuta leikepöydällesi!** On ehdottoman tärkeää, että pidät kopioimasi varmuuskopion tallessa.

Jos olet suorittanut edelliset vaiheet oikein, voit nyt turvallisesti poistaa Samourai-lompakkosi. Tehdäksesi tämän, mene kohtaan: `Asetukset > Lompakko > Turvallinen lompakon tyhjennys`.

![coinjoin](assets/notext/21.webp)

![coinjoin](assets/notext/22.webp)

*Jos et ole koskaan käyttänyt Samouraita ja asennat sovelluksen alusta, voit jatkaa opasta tästä vaiheesta.*

Samourai-sovelluksesi on nyt nollattu. Avaa sovellus ja jatka asennusvaiheita kuin käyttäisit sitä ensimmäistä kertaa.

![coinjoin](assets/notext/23.webp)

Seuraavassa vaiheessa pääset sivulle, joka on omistettu Dojosi konfiguroinnille. Valitse `Dojo`-vaihtoehto, sitten syötä Dojosi kirjautumistiedot. Tehdäksesi tämän, sinulla on mahdollisuus skannata tiedot painamalla `Skannaa QR`.

![coinjoin](assets/notext/24.webp)

*Uusille Samourain käyttäjille, on sitten tarpeen luoda lompakko alusta. Jos tarvitset apua, voit konsultoida ohjeita uuden Samourai-lompakon asettamiseksi [tässä oppaassa, erityisesti kohdassa "Luodaan ohjelmistolompakko"](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef)*
Jos jatkat jo olemassa olevan Samourai-lompakon palauttamista, valitse `Palauta olemassa oleva lompakko`, sitten valitse `Minulla on Samourai-varmuuskopiotiedosto`.
![coinjoin](assets/notext/25.webp)
Normaalisti sinulla tulisi aina olla palautustiedostosi leikepöydälläsi. Sen jälkeen klikkaa `LIITÄ` lisätäksesi tiedoston määrättyyn sijaintiin. Sen purkamiseksi sinun on myös tarpeen syöttää lompakkosi BIP39-salasana vastaavaan kenttään, joka sijaitsee juuri alla. Lopuksi, klikkaa `VALMIS`.
![coinjoin](assets/notext/26.webp)

Tämän jälkeen sinut ohjataan Samourai-lompakkoosi, joka tällä kertaa on yhdistetty omaan Dojoosi.

![coinjoin](assets/notext/27.webp)

### Whirlpool GUI:n asentaminen
Nyt on aika asentaa Whirlpool GUI, graafinen käyttöliittymä, joka mahdollistaa coinjoin-syklien hallinnan tavalliselta PC:ltäsi. RoninDojo-käyttäjien ei tarvitse suorittaa tätä vaihetta, koska coinjoinien hallinta voidaan tehdä suoraan verkkoliittymän kautta `Sovellukset > Whirlpool`. Jos kuitenkin käytät toista Bitcoin "node-in-box" -ratkaisua, on välttämätöntä suorittaa tämä asennus.
![coinjoin](assets/notext/28.webp)
Siirry henkilökohtaiselle tietokoneellesi ja lataa Whirlpool-ohjelmisto viralliselta Samourai Wallet -sivustolta, valitsemalla käyttöjärjestelmääsi vastaava versio.

![coinjoin](assets/notext/29.webp)

Ennen Whirlpool GUI:n käynnistämistä on tarpeen asentaa JAVA 8 tai uudempi versio koneellesi. Tätä varten [voit asentaa OpenJDK:n](https://adoptium.net/).
![coinjoin](assets/notext/30.webp)
On myös tarpeen, että Tor Daemon tai Tor-selain toimii taustalla tietokoneellasi. Varmista, että käynnistät Torin ennen jokaista Whirlpool GUI:n käyttökertaa. Jos Tor ei vielä ole asennettuna koneellasi, [voit ladata ja asentaa sen viralliselta projektisivustolta](https://www.torproject.org/download/), sitten varmista, että käynnistät sen taustalla.

![coinjoin](assets/notext/31.webp)

Kun JDK on asennettu järjestelmääsi ja Tor on käynnistetty taustalla, voit käynnistää Whirlpool GUI:n.

![coinjoin](assets/notext/32.webp)

Whirlpool GUI:sta, klikkaa `Edistynyt: Etä-CLI` yhdistääksesi Whirlpool CLI:n, joka on Dojossasi. Tarvitset Whirlpool CLI:n Tor-osoitteen.

![coinjoin](assets/notext/33.webp)

Tor-osoitteesi löytääksesi Umbrelissa ja muissa "node-in-box" -ratkaisuissa, käynnistä yksinkertaisesti Samourai Server tai Dojo-sovellus (nimi voi vaihdella käytetyn ohjelmiston mukaan). Tor-osoite näkyy suoraan sovelluksen sivulla.
![coinjoin](assets/notext/34.webp)
Whirlpool GUI:ssa, syötä aiemmin saamasi Tor-osoite `CLI-osoite` kenttään. Säilytä `http://` etuliite, mutta älä lisää `:8899` porttia loppuun. Liitä vain osoite sellaisenaan kuin se sinulle annettiin.
![coinjoin](assets/notext/35.webp)
Tor Proxy -kentässä, syötä `socks5://127.0.0.1:9050`, jos käytät Tor Daemonia, tai `socks5://127.0.0.1:9150`, jos käytössäsi on Tor-selain. Kun yhdistät ensimmäistä kertaa Whirlpool CLI:hin Whirlpool GUI:n kautta, API-avainkentän voi jättää tyhjäksi. Jos tämä ei ole ensimmäinen yhteytesi, ole hyvä ja syötä API-avaimesi sille varattuun tilaan. Tämä avain löytyy samalta sivulta kuin Tor-osoitteesi.
![coinjoin](assets/notext/36.webp)

Kun olet täyttänyt kaiken, klikkaa `Yhdistä`-painiketta. Odota, yhteyden muodostaminen voi kestää muutaman minuutin.

![coinjoin](assets/notext/37.webp)

### Samourai-lompakon parittaminen Whirlpool GUI:n kanssa
*RoninDojo-käyttäjät, voitte jatkaa opasta tästä.*

Nyt paritamme aiemmin määrittämämme Samourai-lompakon Whirlpool GUI -ohjelmiston kanssa, tai suoraan RoninDojon kanssa, jos käytät tätä ohjelmistoa. Olitpa käyttämässä Whirlpool GUI:ta tai RoninDojoa, sinua pyydetään liittämään tai skannaamaan Samourai-lompakkosi paritusinformaatio.

![coinjoin](assets/notext/38.webp)

Löytääksesi tämän tiedon, mene lompakkosi asetuksiin.

![coinjoin](assets/notext/39.webp)

Klikkaa `Tapahtumat`, sitten `Parita Whirlpool GUI:n kanssa`.

![coinjoin](assets/notext/40.webp)

Samourai antaa sinulle tarvittavat tiedot yhteyden muodostamiseksi. Ole varovainen, nämä tiedot ovat arkaluonteisia! Voit siirtää ne tietokoneellesi joko kopioimalla suoraan tai skannaamalla näytöllä näkyvän QR-koodin käyttämällä tietokoneesi web-kameraa klikkaamalla QR-koodisymbolia.

![coinjoin](assets/notext/41.webp)

Tämän toimenpiteen jälkeen, Whirlpool GUI:ssa, valitse `Alusta GUI`. Odota, sillä tämä vaihe voi kestää hetken.

![coinjoin](assets/notext/42.webp)

Olitpa käyttämässä Whirlpool GUI:ta tai RoninDojoa, sinua pyydetään syöttämään Samourai-lompakkosi salasana. Syötä se omistetussa kentässä, sitten paina `Kirjaudu sisään`-painiketta jatkaaksesi.

![coinjoin](assets/notext/43.webp)

Tämän jälkeen saavut Whirlpool CLI:n kotisivulle

![coinjoin](assets/notext/44.webp)

### Coinjoinien aloittaminen Whirlpool GUI:sta
*RoninDojo-käyttäjille, prosessi on identtinen. Whirlpool-sovelluksen käyttöliittymä, joka on integroitu RoninDojoon, tarjoaa samat vaihtoehdot ja toiminnot kuin Whirlpool GUI -ohjelmisto työpöydällä. Siksi voit seurata näitä ohjeita samalla tavalla.*
Nyt kun kaikki on valmista, olet valmis aloittamaan bitcoiniesi sekoittamisen. Tee tämä siirtämällä sekoitettavat bitcoinisi Samourai-lompakkosi **Talletus**-tilille. Tämä toimenpide voidaan suorittaa joko suoraan Samourai-lompakko-sovelluksen kautta tai Whirlpool GUI:ssa. Pääsivulta, klikkaa `+ Talletus`-painiketta, joka sijaitsee vasemmassa yläkulmassa.

![coinjoin](assets/notext/45.webp)
Whirlpool GUI luo vastaanotto-osoitteen. Se näyttää myös vähimmäismäärän, joka tarvitaan osallistumiseen kuhunkin coinjoin-altaaseen. Tämä määrä vaihtelee palkkiomarkkinan mukaan. On suositeltavaa tallettaa hieman suurempi summa kuin mitä vähimmäisvaatimus edellyttää, sillä jos louhinta maksut eivät laske, UTXO:si ei ehkä hyväksytä haluttuun altaaseen. Lähetä siis bitcoinit annettuun osoitteeseen. Saadaksesi uuden osoitteen, klikkaa yksinkertaisesti `Uusi osoite` -painiketta.
![coinjoin](assets/notext/46.webp)

Kun talletus on vahvistettu, näet sen ilmestyvän **Talletus**-tilille Whirlpool GUI:ssa.

![coinjoin](assets/notext/47.webp)

Aloittaaksesi coinjoin-syklien, valitse UTXO:t, jotka haluat sekoittaa, ja paina `Esisekoitus`-painiketta. Ole varovainen: jos valitset useita eri UTXO:ja samanaikaisesti, ne yhdistetään `TX0`-valmistelutapahtuman aikana. Tämä yhdistäminen voi johtaa yksityisyyden heikkenemiseen, erityisesti jos UTXO:t tulevat eri lähteistä, Common Input Ownership Heuristic (CIOH) -periaatteen vuoksi.

![coinjoin](assets/notext/48.webp)

Whirlpoolin konfiguraatiosivu avautuu. Voit valita altaan, johon haluat liittyä. Valitse myös louhintamaksut `TX0`:lle ja ensimmäisille coinjoineille. Tämän sivun alaosassa yhteenveto esittelee sinulle doxxic-vaihdon määrän sekä määrän ja UTXO:jen lukumäärän, jotka tasoitetaan ja sisällytetään coinjoin-sykleihin. Jos olet tyytyväinen tähän konfiguraatioon, paina `Esisekoitus`-painiketta aloittaaksesi coinjoin-syklit.
![coinjoin](assets/notext/49.webp)

Kun `TX0` on luotu, näet tasoitetut UTXO:si **Esisekoitus**-tilillä odottamassa vahvistusta. Jotta kolikkosi voivat sekoittua automaattisesti 24 tuntia vuorokaudessa, 7 päivää viikossa, suosittelen aktivoimaan `Sekoita automaattisesti esisekoitus & jälkisekoitus` -vaihtoehdon. Löydät tämän toiminnon `Konfiguraatio`-välilehdeltä, joka sijaitsee vasemmalla puolellasi Whirlpool GUI -ikkunassa.
![coinjoin](assets/notext/50.webp)
Coinjoinien aloittamisen jälkeen voit poistua Whirlpool GUI:sta sekä Samourai Walletista. Vain solmusi tarvitsee pysyä yhdistettynä voidakseen osallistua jatkuviin coinjoineihin. On kuitenkin suositeltavaa tarkistaa ajoittain coinjoin-syklien eteneminen. Jos huomaat, että UTXO:si eivät ole jonkin aikaa valikoituneet coinjoiniin, se saattaa viitata bugiin. Tässä tapauksessa siirry Whirlpool CLI:hin ja valitse `Aloita` uudelleenkäynnistääksesi saatavuutesi coinjoineihin.

![coinjoin](assets/notext/51.webp)

Sekoitetut UTXO:si ovat nähtävissä **Jälkisekoitus**-tilillä Whirlpool GUI:ssa. Lisäksi sinulla on mahdollisuus tarkastella ja käyttää niitä suoraan Whirlpoolin käyttöliittymän kautta Samourai Walletissasi. Päästäksesi tähän valikkoon, klikkaa sinistä `+`-merkkiä näytön alareunassa ja valitse `Whirlpool`.

![coinjoin](assets/notext/52.webp)

Whirlpool-tilit ovat helposti tunnistettavissa Samourai Walletissa niiden sinisen värin ansiosta. Tämä mahdollistaa sekoitettujen UTXO:jesi käyttämisen missä ja milloin tahansa, suoraan älypuhelimestasi.

![coinjoin](assets/notext/53.webp)
Jotta voit seurata automaattisia coinjoinejasi, suosittelen myös watch-only lompakon asettamista Sentinel-sovelluksen kautta. Lisää **Postmix**-tilisi ZPUB ja seuraa coinjoin-syklien etenemistä reaaliajassa. Jos haluat ymmärtää, miten Sentinelia käytetään, suosittelen tutustumaan tähän toiseen oppaaseen PlanB Networkissa: [**SENTINEL WATCH-ONLY**](https://planb.network/tutorials/wallet/mobile/sentinel-9876f960-e964-4d20-8a6e-36231de1f4d9)