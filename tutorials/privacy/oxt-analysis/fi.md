---
name: OXT - Chain Analysis
description: Hallitse Bitcoinin ketjuanalyysin perusteet
---
![kansi](assets/cover.webp)

***VAROITUS:** Samourai Walletin perustajien pidätyksen ja heidän palvelimiensa takavarikoinnin jälkeen 24. huhtikuuta, **verkkosivusto OXT.me ei ole tällä hetkellä saavutettavissa**. On kuitenkin mahdollista, että tämä työkalu saatetaan käynnistää uudelleen tulevina viikkoina. Sillä välin voit silti hyötyä tästä oppaasta ymmärtääksesi Bitcoinin ketjuanalyysin perusteet. Kaikki tässä esitellyt heuristiikat ja mallit ovat sovellettavissa Bitcoin-transaktioihin. Vaikka nämä työkalut eivät ole yhtä optimoituja kuin OXT, voit väliaikaisesti käyttää [Mempool.space](https://mempool.space/) tai [Bitcoin Explorer](https://bitcoinexplorer.org/) -sivustoja soveltaaksesi tämän artikkelin teoreettisia käsitteitä käytäntöön.*

_Seuraamme tarkasti tämän tapauksen kehitystä sekä siihen liittyvien työkalujen kehitystä. Voit olla varma, että päivitämme tämän oppaan, kun uutta tietoa tulee saataville._

_Tämä opas on tarkoitettu vain koulutus- ja tiedotustarkoituksiin. Emme kannusta tai hyväksy näiden työkalujen käyttöä rikollisiin tarkoituksiin. Jokaisen käyttäjän on noudatettava oman lainkäyttöalueensa lakeja._

---

Tässä artikkelissa opit välttämättömät teoreettiset perusteet aloittaaksesi perustason ketjuanalyysejä Bitcoinissa ja tärkeämpää, ymmärtääksesi, miten sinua tarkkaillaan. Vaikka tämä artikkeli ei ole käytännön opas OXT-työkaluun (aihe, jota käsittelemme tulevassa oppaassa), se kokoaa joukon olennaista tietoa sen käyttöön. Jokaiselle esitetylle mallille, mittarille ja indikaattorille on annettu linkki esimerkkitransaktioon OXT:ssä, mikä mahdollistaa sen käytön paremman ymmärtämisen ja harjoittelun lukemisen ohessa.

## Johdanto
Rahan tehtäviin kuuluu kaksinkertaisen halun ongelman ratkaiseminen. Vaihtoon perustuvassa järjestelmässä vaihdon suorittaminen edellyttää paitsi henkilön löytämistä, joka tarjoaa tarpeitani vastaavan hyödykkeen, myös heille vastaavan arvon hyödykkeen tarjoamista, joka tyydyttää heidän tarpeensa. Tämän tasapainon löytäminen osoittautuu monimutkaiseksi. Siksi turvaudumme rahaan, joka mahdollistaa arvon siirtämisen sekä avaruudessa että ajassa.

Jotta raha voisi ratkaista tämän ongelman, on olennaista, että hyödykkeen tai palvelun tarjoaja on vakuuttunut kyvystään käyttää kyseistä summaa myöhemmin. Näin ollen jokainen rationaalinen henkilö, joka on valmis hyväksymään rahayksikön, olipa se digitaalinen tai fyysinen, varmistaa, että se täyttää kaksi perustavaa laatua olevaa kriteeriä:
- Kolikon on oltava ehjä ja aito;
- ja sitä ei saa olla käytetty kahdesti.

Fyysisen rahan käytössä ensimmäinen ominaisuus on monimutkaisin todentaa. Historian eri aikoina metallirahojen eheys on usein heikentynyt käytäntöjen, kuten leikkaamisen tai poraamisen, seurauksena. Esimerkiksi muinaisessa Roomassa oli yleistä, että kansalaiset raaputtivat kultakolikoiden reunoja kerätäkseen hieman arvokasta metallia, samalla säilyttäen ne tulevia transaktioita varten. Tämän vuoksi kolikoiden reunaan myöhemmin lyötiin uurteita. Aitous on myös vaikea ominaisuus todentaa fyysisessä rahavälineessä. Nykyään väärentämisen vastaiset tekniikat ovat yhä monimutkaisempia, pakottaen kauppiaat investoimaan kalliisiin varmennusjärjestelmiin.

Toisaalta fyysisten valuuttojen luonteen vuoksi kaksinkertainen kulutus ei ole ongelma. Jos annan sinulle 10 euron setelin, se siirtyy peruuttamattomasti omistuksestani sinun omistukseesi, sulkee pois mahdollisuuden kyseisen rahayksikön moninkertaiseen käyttöön.
Digitaalisen valuutan haaste on erilainen. Kolikon aitouden ja eheyden varmistaminen on usein yksinkertaisempaa, mutta kaksinkertaisen kulutuksen puuttumisen varmistaminen on monimutkaisempaa. Jokainen digitaalinen hyödyke on käytännössä tietoa. Toisin kuin fyysiset hyödykkeet, tieto ei jakaudu vaihdoissa vaan leviää monistumalla. Esimerkiksi, jos lähetän sinulle asiakirjan sähköpostitse, se sitten kopioidaan. Sinä et voi varmistaa varmuudella, että olen poistanut alkuperäisen asiakirjan.

Ainoa tapa välttää digitaalisen hyödykkeen kopiointi on olla tietoinen kaikista järjestelmän vaihdoista. Tällä tavoin voidaan tietää, kuka omistaa mitäkin ja päivittää kaikkien tilien tiedot tehtyjen transaktioiden perusteella. Näin tehdään esimerkiksi kirjanpidollisen rahan kanssa. Kun maksat 10 € kauppiaalle luottokortilla, pankki merkitsee tämän vaihdon ja päivittää kirjanpidon.

Bitcoinissa kaksinkertaisen kulutuksen estäminen tapahtuu samalla tavalla. Pyritään vahvistamaan, ettei kyseessä olevia kolikoita ole jo aiemmin käytetty. Jos näitä ei ole koskaan käytetty, voimme olla varmoja, että kaksinkertaista kulutusta ei tapahdu. Tämä on kuuluisa lause Satoshi Nakamotolta White Paperissa: "*Ainoa tapa vahvistaa transaktion puuttuminen on olla tietoinen kaikista transaktioista.*"

Toisin kuin pankkimallissa, Bitcoinissa emme halua luottaa keskitettyyn toimijaan. Siksi kaikkien käyttäjien on voitava vahvistaa tämä kaksinkertaisen kulutuksen puuttuminen, turvautumatta kolmanteen osapuoleen. Näin ollen kaikkien on oltava tietoisia kaikista Bitcoin-transaktioista.

Juuri tämä tiedon julkisen levittämisen tarve monimutkaistaa yksityisyyden suojaa Bitcoinissa. Perinteisessä pankkijärjestelmässä teoriassa vain rahoituslaitos tietää tehdyistä transaktioista. Bitcoinissa kaikki käyttäjät saavat tiedon kaikista transaktioista omien solmujensa kautta.

Tämän levittämisrajoituksen vuoksi Bitcoinin yksityisyyden suoja eroaa pankkijärjestelmän mallista. Jälkimmäisessä transaktiot liitetään käyttäjän henkilöllisyyteen, mutta tiedonkulku katkaistaan luotetun kolmannen osapuolen ja yleisön välillä. Toisin sanoen, pankkisi tietää, että ostat patongin joka aamu paikallisesta leipomosta, mutta naapurisi ei ole tietoinen kaikista näistä transaktioista. Bitcoinin tapauksessa, koska tiedonkulun katkaiseminen transaktioiden ja julkisen domainin välillä ei ole mahdollista, yksityisyyden malli perustuu käyttäjän henkilöllisyyden erottamiseen itse transaktioista.
![analyysi](assets/en/1.webp)
*Kaavio on innoittanut Satoshi Nakamoton White Paperista: Bitcoin: A Peer-to-Peer Electronic Cash System, osio 10 "Privacy".*
Koska Bitcoin-transaktiot ovat julkisia, on mahdollista luoda linkkejä niiden välille päätelläkseen tietoa osapuolista. Tämä toiminta on jopa itsessään erikoisala, jota yleisesti kutsutaan "ketjuanalyysiksi". Tässä artikkelissa kutsun sinut tutustumaan ketjuanalyysin perusteisiin ymmärtääksesi, miten bitcoinejasi seurataan.

Enemmistö ketjuanalyysiin erikoistuneista yrityksistä toimii mustina laatikoina eivätkä paljasta menetelmiään. Siksi on vaikeaa saada tietoa tästä käytännöstä. Tämän artikkelin kirjoittamiseen nojasin pääasiassa muutamiin saatavilla oleviin avoimiin resursseihin:
- Suurin osa artikkelistani on poimittu neljän artikkelin sarjasta nimeltä: [Understanding Bitcoin Privacy with OXT](https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923), jonka tuotti Samourai Wallet vuonna 2021;
- Käytin myös erilaisia raportteja [OXT Research](https://medium.com/oxt-research) -sivustolta, sekä heidän ilmaista ketjuanalyysityökaluaan.
- Laajemmin ottaen tietoni perustuvat eri twiitteihin ja sisältöihin käyttäjiltä [@LaurentMT](https://twitter.com/LaurentMT) ja [@ErgoBTC](https://twitter.com/ErgoBTC);
- Sain myös inspiraatiota [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) -podcastista, jossa osallistuin yhdessä [@louneskmt](https://twitter.com/louneskmt), [@TheoPantamis](https://twitter.com/TheoPantamis), [@Sosthene___](https://twitter.com/Sosthene___), ja [@LaurentMT](https://twitter.com/LaurentMT).

Haluaisin kiittää heidän tekijöitään, kehittäjiään ja tuottajiaan. Ilman heidän moninaisia sisältöjään ja ohjelmistojaan tämä artikkeli ei olisi olemassa. Kiitän myös arvostelijoita, jotka huolellisesti korjasivat tämän tekstin ja antoivat minulle asiantuntijaneuvojaan:
- [Gilles Cadignan](https://twitter.com/gillesCadignan);
- [Ludovic Lars](https://twitter.com/lugaxker) ([https://viresinnumeris.fr/](https://viresinnumeris.fr/)).

*Tiedoksesi, olen lisännyt artikkelin loppuun teknisen minisanaston tiettyjen termien määrittelemiseksi. Jos näet sanan, jota et ymmärrä ja siinä on asteriski, sen määritelmä on sivun alaosassa.*

## Mikä on ketjuanalyysi?
Ketjuanalyysi on käytäntö, joka kattaa kaikki menetelmät Bitcoin-virtojen seuraamiseksi lohkoketjussa. Yleisesti ottaen ketjuanalyysi perustuu aikaisempien transaktioiden otosten ominaisuuksien tarkkailuun. Sen jälkeen se sisältää näiden samojen ominaisuuksien tunnistamisen transaktiossa, jota halutaan analysoida, ja mahdollisten tulkintojen päättelemisen. Tämä ongelmanratkaisumenetelmä, joka perustuu käytännölliseen lähestymistapaan löytää riittävän hyvä ratkaisu, on sitä, mitä kutsutaan heuristiikaksi.

Yksinkertaistaen, ketjuanalyysi tehdään kahdessa päävaiheessa:
1. Tunnettujen ominaisuuksien tunnistaminen;
2. Hypoteesien päätteleminen.

Yksi ketjuanalyysin tavoitteista on ryhmitellä erilaisia toimintoja Bitcoinissa määrittääkseen käyttäjän yksilöllisyyden, joka ne suoritti. Tämän jälkeen on mahdollista yrittää yhdistää tämä toimintojen nippu todelliseen identiteettiin.

Muista johdantoni. Selitin, miksi Bitcoinin yksityisyysmalli alun perin perustui käyttäjän identiteetin erottamiseen heidän transaktioistaan. Siksi voisi olla houkuttelevaa ajatella, että ketjuanalyysi on tarpeetonta, koska vaikka onnistuisimme ryhmittelemään ketjutoimintoja, emme voi yhdistää niitä todelliseen identiteettiin. Teoriassa tämä väite on paikkansapitävä. Kryptografisia avainpareja käytetään määrittelemään ehdot UTXOille. Luonteeltaan nämä avainparit eivät paljasta mitään tietoa haltijoidensa identiteetistä. Näin ollen, vaikka onnistuisimme ryhmittelemään toimintoja, jotka liittyvät eri avainpareihin, tämä ei kerro meille mitään näiden toimintojen takana olevasta entiteetistä.
Käytännön todellisuus on kuitenkin huomattavasti monimutkaisempi. On olemassa lukuisia käyttäytymismalleja, jotka voivat yhdistää todellisen henkilöllisyyden lohkoketjuaktiviteettiin. Analyysissä tätä kutsutaan sisääntulopisteeksi, ja niitä on monia. Yleisin näistä on tietenkin KYC (Know Your Customer). Jos nostat bitcoinejasi säännellyltä alustalta yhdelle henkilökohtaisista vastaanotto-osoitteistasi, jotkut ihmiset voivat yhdistää henkilöllisyytesi tähän osoitteeseen. Laajemmin ottaen sisääntulopiste voi olla mikä tahansa vuorovaikutusmuoto todellisen elämäsi ja Bitcoin-siirron välillä. Esimerkiksi, jos julkaiset vastaanotto-osoitteen sosiaalisissa verkostoissasi, se voi olla analyysin sisääntulopiste. Jos maksat bitcoineilla leipurillesi, he voivat yhdistää kasvosi (joka on osa henkilöllisyyttäsi) Bitcoin-osoitteeseen. Nämä sisääntulopisteet ovat lähes väistämättömiä Bitcoinia käytettäessä. Vaikka niiden vaikutusalaa pyritäänkin rajoittamaan, ne säilyvät läsnä. Siksi on ratkaisevan tärkeää yhdistää menetelmiä, jotka tähtäävät yksityisyytesi säilyttämiseen. Vaikka todellisen henkilöllisyytesi ja transaktioidesi välisen hyväksyttävän erottelun ylläpitäminen on kiitettävä lähestymistapa, se on riittämätön. Todellakin, jos kaikki lohkoketjuaktiviteettisi voidaan ryhmitellä yhteen, jopa pienin sisääntulopiste voisi vaarantaa sen yksityisyyden kerroksen, jonka olit luonut.

Siksi on myös tarpeellista käsitellä ketjuanalyysiä Bitcoinin käytössämme. Näin voimme minimoida aktiviteettiemme aggregoinnin ja rajoittaa sisääntulopisteen vaikutusta yksityisyyteemme. Tarkemmin sanottuna, ketjuanalyysin vastatoimien paremmaksi ymmärtämiseksi, mikä parempi lähestymistapa kuin tutustua ketjuanalyysissä käytettyihin menetelmiin? Jos haluat tietää, miten parantaa yksityisyyttäsi Bitcoinissa, sinun on ymmärrettävä nämä menetelmät. Tämä mahdollistaa paremman käsityksen tekniikoista kuten [Coinjoin](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef) tai [Payjoin](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f) ja vähentää tekemiäsi virheitä.

Tässä voimme tehdä analogian kryptografian ja kryptoanalyyttien välillä. Hyvä kryptografi on ensisijaisesti hyvä kryptoanalyytikko. Uuden salausalgoritmin kuvitellakseen, on tiedettävä, minkälaisia hyökkäyksiä se kohtaa, ja tutkittava myös, miksi aiemmat algoritmit murrettiin. Sama periaate pätee Bitcoinin yksityisyyteen. Ketjuanalyysin menetelmien ymmärtäminen on avain sen vastustamiseen. Siksi tarjoan sinulle tämän artikkelin.

On tärkeää ymmärtää, että ketjuanalyysi ei ole eksakti tiede. Se perustuu heuristiikkoihin, jotka on johdettu aiemmista havainnoista tai loogisista tulkinnoista. Nämä säännöt mahdollistavat melko luotettavat tulokset, mutta eivät koskaan absoluuttisella tarkkuudella. Toisin sanoen, ketjuanalyysi sisältää aina todennäköisyysulottuvuuden päätelmissä. Voimme arvioida suuremmalla tai pienemmällä varmuudella, että kaksi osoitetta kuuluu samalle entiteetille, mutta täydellinen varmuus on aina saavuttamattomissa.

Ketjuanalyysin koko tavoite perustuu nimenomaan erilaisten heuristiikkojen aggregointiin virheriskin minimoimiseksi. Se on tavallaan todisteiden kumuloituminen, joka mahdollistaa meidät lähestymään todellisuutta.

Nämä kuuluisat heuristiikat voidaan ryhmitellä eri kategorioihin, joita käymme yhdessä läpi:
- Transaktiokuvioinnit (tai transaktiomallit);
- Transaktion sisäiset heuristiikat;
- Transaktion ulkopuoliset heuristiikat.

On huomionarvoista, että ensimmäiset kaksi Bitcoin-heuristiikkaa formuloitiin itse Satoshi Nakamoton toimesta. Hän käsittelee niitä White Paperin osassa 10. Kuten myöhemmin näemme, on mielenkiintoista havaita, että nämä kaksi heuristiikkaa säilyttävät edelleen etusijan ketjuanalyysissä tänä päivänä. Nämä ovat:
- yhteisen syötteen omistajuuden heuristiikka (CIOH);
- ja osoitteen uudelleenkäyttö.
Tutkitaan yhdessä havaittavia ominaisuuksia ja niistä tehtäviä tulkintoja analyysin suorittamiseksi.
## Transaktiokuvioita (tai transaktiomalleja)
Transaktiokuva on yksinkertaisesti tyypillinen transaktiomalli, joka löytyy lohkoketjusta, ja jonka tulkinta on todennäköisesti tunnettu. Kuvioita tutkiessamme keskitymme yksittäiseen transaktioon, jota analysoimme korkealla tasolla. Toisin sanoen, tarkastelemme vain syötteiden ja tulosteiden määrää, perehtymättä sen tarkempiin yksityiskohtiin tai sen ympäristöön. Havaitusta mallista pystymme tulkitsemaan transaktion luonteen. Sen jälkeen etsimme ominaisuuksia sen rakenteesta ja teemme tulkinnan.

### Yksinkertainen lähetys (tai yksinkertainen maksu)
Tätä mallia luonnehtii yhden tai useamman UTXO:n kulutus syötteenä ja kahden UTXO:n tuotanto tulosteena.

![analyysi](assets/en/2.webp)

Tämän mallin tulkinta on, että olemme lähetys- tai maksutransaktion läsnäolossa. Käyttäjä on kuluttanut omat UTXO:nsa syötteenä tyydyttääkseen tulosteessa maksu-UTXO:n ja vaihtorahan UTXO:n (vaihtoraha palautuu samalle käyttäjälle). Tiedämme siis, että havaittu käyttäjä ei todennäköisesti enää omista toista kahdesta tulosteessa olevasta UTXO:sta (maksu-UTXO), mutta on yhä toisen UTXO:n (vaihtoraha-UTXO) omistaja.

Tässä vaiheessa meidän on mahdotonta määrittää, kumpi tuloste edustaa kumpaa UTXO:ta, koska se ei ole tämän mallin tavoite. Voimme tehdä niin nojautumalla heuristiikkoihin, joita tutkimme seuraavassa osassa. Tässä vaiheessa tavoitteemme rajoittuu kyseessä olevan transaktion luonteen tunnistamiseen, joka tässä tapauksessa on yksinkertainen lähetys.

Esimerkiksi, tässä on Bitcoin-transaktio, joka noudattaa yksinkertaisen lähetyksen mallia:
### Haravointi ("sweep" englanniksi)
Tätä mallia luonnehtii yhden UTXO:n kulutus syötteenä ja yhden UTXO:n tuotanto tulosteena.

![analyysi](assets/en/3.webp)

Tämän mallin tulkinta on, että olemme itse-siirron läsnäolossa. Käyttäjä on siirtänyt bitcoinejaan itselleen, toiseen omistamaansa osoitteeseen. Koska transaktiossa ei ole vaihtorahaa, on hyvin epätodennäköistä, että kyseessä olisi maksu. Tiedämme siis, että havaittu käyttäjä todennäköisesti yhä omistaa tämän UTXO:n.

Esimerkiksi, tässä on Bitcoin-transaktio, joka noudattaa haravointimallia:
[35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d](https://mempool.space/tx/35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d)

Tämäntyyppinen kuvio voi kuitenkin paljastaa myös itse-siirron vaihtotilille (kryptovaluutan vaihtoalusta). Tunnettujen osoitteiden tutkiminen ja transaktion konteksti antavat meille mahdollisuuden tietää, onko kyseessä haravointi itsehallinnolliseen lompakkoon vai nosto alustalle.

### Konsolidointi
Tätä mallia luonnehtii useiden UTXO:jen kulutus syötteenä ja yhden UTXO:n tuotanto tulosteena.

![analyysi](assets/en/4.webp)
Tämän mallin tulkinta on, että olemme konsolidaation läsnäolossa. Tämä on yleinen käytäntö Bitcoin-käyttäjien keskuudessa, jonka tavoitteena on yhdistää useita UTXO:ja odotettaessa mahdollista siirtomaksujen nousua. Suorittamalla tämän toimenpiteen aikana, jolloin maksut ovat matalat, on mahdollista säästää tulevaisuuden maksuissa.
Voimme päätellä, että tämän siirron takana oleva käyttäjä oli todennäköisesti hallussaan kaikki syötteen UTXO:t ja on edelleen lähtökohtaisen UTXO:n hallussa. Siksi se on varmasti itse siirto.

Aivan kuten pyyhkäisy, tämäntyyppinen kaava voi myös paljastaa itse siirron vaihtotilille. Tunnettujen osoitteiden tutkiminen ja siirron konteksti mahdollistavat meidän tietää, onko kyseessä konsolidaatio itse säilytettävään lompakkoon vai nosto alustalle.

Esimerkiksi, tässä on Bitcoin-siirto, joka noudattaa konsolidaatiokaavaa:
[77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94](https://mempool.space/tx/77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94)
### Eräkulutusmalli
Tämä malli on tunnusomaista muutaman UTXO:n kulutukselle syötteenä (usein vain yksi) ja monien UTXO:jen tuottamiselle lähtökohtana.

![analysis](assets/en/5.webp)

Tämän mallin tulkinta on, että olemme eräkulutuksen läsnäolossa. Tämä on käytäntö, joka todennäköisesti paljastaa merkittävää taloudellista toimintaa, kuten esimerkiksi vaihdon. Eräkulutus mahdollistaa näiden yksiköiden säästää maksuissa yhdistämällä heidän menonsa yhteen siirtoon.

Voimme päätellä, että UTXO-syöte tulee yritykseltä, jolla on merkittävää taloudellista toimintaa ja että UTXO-lähdöt hajaantuvat. Jotkut kuuluvat yrityksen asiakkaille. Toiset saattavat mennä yhteistyökumppaneiden yrityksille. Lopulta, varmasti on muutos, joka palautuu liikkeellelaskijayritykselle.

Esimerkiksi, tässä on Bitcoin-siirto, joka noudattaa eräkulutuskaavaa:
[8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43](https://mempool.space/tx/8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43)

### Protokollakohtaiset Siirrot
Siirtokaavoissa voimme myös tunnistaa malleja, jotka paljastavat tietyn protokollan käytön. Esimerkiksi Whirlpool coinjoinit ovat helposti tunnistettavissa oleva rakenne, joka mahdollistaa niiden erottamisen muista klassisista siirroista.

![analysis](assets/en/6.webp)

Tämän kaavan analyysi viittaa siihen, että todennäköisesti olemme yhteistyössä tehdyn siirron läsnäolossa. On myös mahdollista havaita coinjoin. Jos tämä jälkimmäinen hypoteesi osoittautuu paikkansa pitäväksi, niin lähtöjen lukumäärä voisi antaa meille likimääräisen arvion osallistujien määrästä.

Esimerkiksi, tässä on Bitcoin-siirto, joka noudattaa yhteistyössä tehdyn siirtotyypin coinjoin-kaavaa:
[00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea](https://mempool.space/tx/00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea)
On olemassa monia muita protokollia, joilla on omat erityiset rakenteensa. Näin ollen voimme erottaa esimerkiksi Wabisabi-tyyppiset transaktiot tai Stamp-transaktiot.

## Sisäiset Transaktio-Heuristiikat
Sisäinen heuristiikka on tietty ominaisuus, joka on tunnistettu itse transaktiossa, ilman tarvetta tutkia sen ympäristöä, mikä mahdollistaa päätelmien tekemisen. Toisin kuin mallit, jotka keskittyvät transaktion kokonaisrakenteeseen, sisäiset heuristiikat perustuvat poimittavissa olevien tietojen joukkoon. Tähän sisältyy:
- Erilaisten UTXO:iden määrät sekä saapuvat että lähtevät;
- Kaikki, mikä liittyy skripteihin: vastaanotto-osoitteet, versionumerot, lukitusajat...

Yleisesti ottaen tämän tyyppinen heuristiikka mahdollistaa tietyn transaktion muutoksen tunnistamisen. Näin voimme jatkaa yksittäisen entiteetin jäljittämistä useiden eri transaktioiden läpi.

Muistutan jälleen, että nämä heuristiikat eivät ole täysin tarkkoja. Yksittäin otettuna ne mahdollistavat vain todennäköisten skenaarioiden tunnistamisen. Useiden heuristiikkojen kertyminen auttaa vähentämään epävarmuutta, vaikka se ei sitä koskaan täysin poistakaan.

### Sisäiset Yhtäläisyydet
Tämä heuristiikka perustuu saman transaktion sisääntulojen ja ulostulojen välillä havaittavien yhtäläisyyksien tutkimiseen. Jos sama ominaisuus havaitaan sisääntuloissa ja vain yhdessä transaktion ulostulossa, on todennäköistä, että tämä ulostulo muodostaa vaihdon.

Ilmeisin ominaisuus on vastaanotto-osoitteen uudelleenkäyttö samassa transaktiossa.

![analyysi](assets/en/7.webp)

Tämä heuristiikka jättää vähän tilaa epäilyksille. Ellei heidän yksityisavaintaan ole vaarantunut, sama vastaanotto-osoite paljastaa väistämättä yhden käyttäjän toiminnan. Tulkinta, joka seuraa, on, että transaktion vaihto on ulostulo, jolla on sama osoite kuin sisääntulossa. Tämä mahdollistaa yksilön jäljittämisen tästä vaihdosta lähtien.

Esimerkiksi tässä on transaktio, jossa tätä heuristiikkaa voidaan todennäköisesti soveltaa:
[54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0](https://mempool.space/tx/54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0)

Nämä yhtäläisyydet sisääntulojen ja ulostulojen välillä eivät pysähdy osoitteen uudelleenkäyttöön. Mikä tahansa samankaltaisuus skriptien käytössä voi mahdollistaa heuristiikan soveltamisen. Esimerkiksi joskus voidaan havaita sama versionumero sisääntulossa ja yhdessä transaktion ulostuloista.

![analyysi](assets/en/8.webp)
Tässä kaaviossa näemme, että sisääntulo numero 0 avaa P2WPKH-skriptin (SegWit V0 alkaen "bc1q"). Ulostulo numero 0 käyttää samaa tyyppistä skriptiä. Kuitenkin ulostulo numero 1 käyttää P2TR-skriptiä (SegWit V1 alkaen "bc1p"). Tämän ominaisuuden tulkinta on, että on todennäköistä, että samaa versionumeroa käyttävä osoite on vaihto-osoite. Se kuuluisi siis edelleen samalle käyttäjälle.
Tässä on transaktio, jossa tätä heuristiikkaa voidaan todennäköisesti soveltaa:
[db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578](https://mempool.space/tx/db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578)
Tässä transaktiossa voimme nähdä, että syötteen numero 0 ja tulosteen numero 1 käyttävät P2WPKH-skriptejä (SegWit V0), kun taas tulosteen numero 0 käyttää eri skriptityyppiä, P2PKH (Legacy).
### Pyöristettyjen Summien Maksut
Toinen sisäinen heuristiikka, joka voi auttaa meitä tunnistamaan vaihdon, on pyöristettyjen summien käyttö. Yleensä, kun kohdataan yksinkertainen maksukuvio (1 syöte ja 2 tulostetta), jos toinen tulosteista käyttää pyöristettyä summaa, se edustaa maksua.

![analyysi](assets/en/9.webp)

Poissulkemisen prosessin kautta, jos yksi tuloste edustaa maksua, toinen edustaa vaihtoa. Siksi voimme tulkita, että on todennäköistä, että syötteen käyttäjä yhä omistaa vaihtona tunnistetun tulosteen.

On huomattava, että tätä heuristiikkaa ei aina voida soveltaa, koska suurin osa maksuista tehdään edelleen fiat-valuutoissa. Todellakin, kun kauppias Ranskassa hyväksyy bitcoineja, yleensä he eivät näytä vakaita hintoja satseissa. He pikemminkin valitsevat hinnan muuntamisen euroista bitcoineiksi maksettavaan summaan. Siksi transaktion tulosteessa ei pitäisi olla pyöristettyä numeroa. Kuitenkin analyytikko voisi yrittää suorittaa tämän muunnoksen ottaen huomioon vaihtokurssin, joka oli voimassa, kun transaktio lähetettiin verkkoon.

Jos jonain päivänä bitcoinista tulee suosituin laskentayksikkö vaihdoissamme, tämä heuristiikka voisi muuttua vielä hyödyllisemmäksi analyysissä.

Esimerkiksi, tässä on transaktio, jossa tätä heuristiikkaa todennäköisesti voidaan soveltaa:
### Suuri Kulutus

Kun yksinkertaisessa maksu mallissa havaitaan riittävän suuri ero kahden transaktion tulosteen välillä, voidaan arvioida, että suurempi tuloste on todennäköisesti vaihto.

![analyysi](assets/en/10.webp)

Tämä suurimman tulosteen heuristiikka on todennäköisesti kaikista epätarkimpia. Jos se tunnistetaan yksinään, se on melko heikko. Kuitenkin, tämä ominaisuus voidaan yhdistää muiden heuristiikkojen kanssa vähentämään tulkintamme epävarmuutta.

Esimerkiksi, jos tarkastelemme transaktiota, jossa on tuloste pyöristetyllä summalla ja toinen tuloste suuremmalla summalla, pyöristettyjen maksujen heuristiikan ja suurimman tulosteen heuristiikan yhteiskäyttö mahdollistaa epävarmuustason vähentämisen.

Esimerkiksi, tässä on transaktio, jossa tätä heuristiikkaa todennäköisesti voidaan soveltaa:
[b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf](https://mempool.space/tx/b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf)

## Ulkoiset Heuristiikat Transaktioon
Ulkoisten heuristiikkojen tutkimus on samankaltaisuuksien, kaavojen ja tiettyjen elementtien ominaisuuksien analysointia, jotka eivät ole transaktion itsensä ominaisia. Toisin sanoen, jos aiemmin rajoituimme hyödyntämään transaktion sisäisiä elementtejä sisäisillä heuristiikoilla, laajennamme nyt analyysikenttäämme transaktion ympäristöön kiitos ulkoisten heuristiikkojen.

### Osoitteen Uudelleenkäyttö
Tämä on yksi tunnetuimmista heuristiikoista Bitcoin-käyttäjien keskuudessa. Osoitteen uudelleenkäyttö mahdollistaa linkin luomisen eri transaktioiden ja eri UTXOjen välille. Sitä havaitaan, kun Bitcoinin vastaanotto-osoitetta käytetään useita kertoja.

Osoitteen uudelleenkäytön tulkinta on, että kaikki tähän osoitteeseen lukitut UTXOt kuuluvat (tai ovat kuuluneet) samalle entiteetille. Tämä heuristiikka jättää vähän tilaa epävarmuudelle. Kun se tunnistetaan, seuraava tulkinta on suurella todennäköisyydellä vastaavuus todellisuuteen.
Kuten johdannossa selitettiin, tämän heuristiikan löysi itse Satoshi Nakamoto. White Paperissa hän mainitsee erityisesti ratkaisun estääkseen käyttäjiä tuottamasta sitä, mikä on yksinkertaisesti käyttää uutta osoitetta jokaiseen uuteen siirtoon: "*Lisäsuojana voitaisiin jokaiseen siirtoon käyttää uutta avainparia pitääkseen ne linkittymättöminä yhteiseen omistajaan.*"
Esimerkiksi, tässä on osoite, jota on käytetty uudelleen useissa siirroissa:
[bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0](https://mempool.space/address/bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0)

### Skriptien ja Lompakon Sormenjälkien Samankaltaisuus
Osoitteiden uudelleenkäytön lisäksi on monia muita heuristiikkoja, jotka voivat yhdistää toimintoja samaan lompakkoon tai osoitteiden ryhmään.

Ensinnäkin analyytikko voi käyttää samankaltaisuuksia skriptien käytössä. Esimerkiksi tiettyjä vähemmistöskriptejä, kuten multisig, voidaan havaita helpommin kuin SegWit V0 -skriptejä. Mitä suuremmassa ryhmässä piilemme, sitä vaikeampi meidät on havaita. Tämä on erityisesti syy, miksi Coinjoin Whirlpool -protokollassa kaikki osallistujat käyttävät täsmälleen samaa skriptityyppiä.

Laajemmin analyytikko voi myös keskittyä lompakon ominaisiin sormenjälkiin. Nämä ovat tiettyjä käyttöön liittyviä prosesseja, joita saatetaan pyrkiä tunnistamaan hyödyntääkseen niitä jäljitysheuristiikkoina. Toisin sanoen, jos havaitaan kertymä samoja sisäisiä ominaisuuksia siirroissa, jotka on attribuoitu jäljitettävälle entiteetille, voidaan yrittää tunnistaa nämä samat ominaisuudet muissa siirroissa.

Esimerkiksi voidaan tunnistaa, että jäljitettävä käyttäjä lähettää systemaattisesti vaihtorahansa P2TR*-osoitteisiin (bc1p…). Jos tämä prosessi toistuu, sitä voidaan käyttää heuristiikkana analyysimme jatkamiseen. Muita sormenjälkiä voidaan myös käyttää, kuten UTXOjen järjestys, vaihtorahan sijoittelu lähtöihin, RBF:n (Replace-by-Fee) merkitseminen tai jopa versionumero ja lukitusaika.
Kuten [@LaurentMT](https://twitter.com/LaurentMT) täsmentää [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) (frankofoninen podcast) -ohjelmassa, lompakon sormenjälkien hyödyllisyys ketjuanalyysissä kasvaa merkittävästi ajan myötä. Todellakin, skriptityyppien kasvava määrä ja näiden uusien ominaisuuksien asteittainen käyttöönotto lompakko-ohjelmistojen toimesta korostavat eroja. Jopa niin, että voidaan tarkasti tunnistaa jäljitettävän entiteetin käyttämä ohjelmisto. Siksi on tärkeää ymmärtää, että lompakon sormenjäljen tutkiminen on erityisen relevanttia viimeaikaisten siirtojen osalta, enemmän kuin niiden, jotka on aloitettu 2010-luvun alussa.
Yhteenvetona, sormenjälki voi olla mikä tahansa tietty käytäntö, jonka lompakko suorittaa automaattisesti tai käyttäjä manuaalisesti, ja joka voidaan löytää muista siirroista avustamaan analyysissämme.

### CIOH
CIOH, "Common Input Ownership Heuristic", joka voitaisiin kääntää "yhteisen omistajuuden heuristiikaksi syötteille" tai "yhteiskäyttöheuristiikaksi", on heuristiikka, joka toteaa, että kun siirrolla on useita syötteitä, ne todennäköisesti kaikki tulevat yhdeltä entiteetiltä. Täten niiden omistajuus on yhteinen.
CIOH:n soveltamiseksi tarkkaillaan ensin tapahtumaa, jolla on useita syötteitä. Tämä voi olla kaksi syötettä, mutta myös kolmekymmentä syötettä. Kun tämä ominaisuus on havaittu, tarkistetaan, ettei tapahtuma sovi mihinkään tunnettuun kaavaan. Esimerkiksi, jos sillä on 5 syötettä suunnilleen samalla määrällä ja 5 lähtöä täsmälleen samalla määrällä, tiedämme, että kyseessä on Coinjoin Whirlpoolin rakenne. Siksi CIOH:ta ei voida soveltaa.
Kuitenkin, jos tapahtuma ei sovi mihinkään tunnettuun yhteistyöllisen tapahtuman kaavaan, voidaan tulkita, että kaikki syötteet todennäköisesti tulevat samalta taholta. Tämä voi olla erittäin hyödyllistä laajennettaessa jo tunnettua klusteria tai jatkettaessa seurantaa.

![analyysi](assets/en/11.webp)

CIOH:n löysi Satoshi Nakamoto. Hän keskustelee siitä White Paperin osassa 10: "*[...] linkki on väistämätön usean syötteen tapahtumissa, jotka välttämättä paljastavat, että niiden syötteet kuuluivat samalle omistajalle. Riskinä on, että jos avaimen omistaja paljastetaan, linkit voivat paljastaa muita tapahtumia, jotka kuuluivat samalle omistajalle.*"
On erityisen mielenkiintoista huomata, että Satoshi Nakamoto oli jo ennen Bitcoinin virallista julkaisua tunnistanut kaksi pääasiallista yksityisyyden haavoittuvuutta käyttäjille, nimittäin CIOH:n ja osoitteen uudelleenkäytön. Tällainen ennakointikyky on melko merkittävää, sillä nämä kaksi heuristiikkaa ovat vielä tänäkin päivänä hyödyllisimpiä ketjuanalyysissä.

### Off-chain Data
Ilmeisesti ketjuanalyysi ei rajoitu vain on-chain dataan. Myös aiemmasta analyysistä tai Internetistä saatavilla olevaa dataa voidaan käyttää analyysin tarkentamiseen.

Esimerkiksi, jos havaitaan, että jäljitetyt tapahtumat lähetetään systemaattisesti samasta Bitcoin-nodesta ja sen IP-osoite voidaan tunnistaa, saattaa olla mahdollista löytää muita tapahtumia samalta taholta.

Analyytikolla on myös mahdollisuus nojautua aiemmin julkiseksi tehtyihin analyyseihin tai omiin aikaisempiin analyyseihinsa. Ehkä löytyy lähtö, joka osoittaa jo tunnistettuun osoitteiden klusteriin. Joskus on myös mahdollista nojautua lähtöihin, jotka osoittavat vaihtoon, näiden alustojen osoitteet kun ovat yleensä tunnettuja.

Samoin voidaan suorittaa analyysi poissulkemisen kautta. Esimerkiksi, jos tapahtuman analyysissä, jolla on kaksi lähtöä, toinen niistä on yhdistetty tunnettuun, mutta erilliseen osoitteiden klusteriin jäljitettävältä taholta, voidaan tulkita, että toinen lähtö todennäköisesti edustaa vaihtorahaa.

Ketjuanalyysi sisältää myös osan OSINT (Open Source Intelligence) -tiedustelusta, joka on hieman yleisluonteisempi internet-hakujen osalta. Tämän vuoksi on suositeltavaa välttää vastaanotto-osoitteiden suoraa julkaisemista sosiaalisessa mediassa tai verkkosivustolla, olipa kyseessä sitten pseudonyymi tai ei.

### Temporaaliset Mallit
Ei ehkä heti tule mieleen, mutta tietyt ihmisen käyttäytymismallit ovat tunnistettavissa on-chain. Hyödyllisin tutkimuksessa on unirytmi! Kyllä, kun nukut, et todennäköisesti lähetä Bitcoin-tapahtumia. Koska yleensä nukut suunnilleen samoilla tunneilla, on yleistä käyttää temporaalisia analyysejä ketjuanalyysissä. Se yksinkertaisesti sisältää tietyn tahon tapahtumien lähetysaikojen tallentamisen Bitcoin-verkkoon. Näiden temporaalisten mallien analysointi mahdollistaa lukuisien tietojen päättelemisen.
Ensinnäkin temporaalinen analyysi voi joskus tunnistaa jäljitettävän tahon luonteen. Jos havaitaan, että tapahtumia lähetetään johdonmukaisesti 24 tunnin ajan, tämä voi viitata vahvaan taloudelliseen toimintaan. Näiden tapahtumien takana oleva taho on todennäköisesti yritys, mahdollisesti kansainvälinen, ja ehkä sisäisesti automatisoiduilla menettelyillä.
Esimerkiksi olin tunnistanut tämän mallin muutama viikko sitten analysoimalla tapahtumaa, jossa oli virheellisesti kohdennettu 19 bitcoinia maksuina. Yksinkertainen ajallinen analyysi oli antanut minulle mahdollisuuden olettaa, että kyseessä oli automatisoitu palvelu, ja siksi todennäköisesti suuri toimija, kuten vaihtopalvelu: https://twitter.com/Loic_Pandul/status/1701127409712452072
Todellakin, muutama päivä myöhemmin selvisi, että varat kuuluivat PayPalille, Paxos-vaihdon kautta.

Päinvastoin, jos havaitaan, että ajallinen malli on pikemminkin levinnyt 16 tietyn tunnin yli, voidaan arvioida, että kyseessä on yksittäinen käyttäjä tai ehkä paikallinen yritys riippuen vaihdettujen volyymien määrästä.

Havaitun entiteetin luonteen lisäksi ajallinen malli voi myös antaa meille likimääräisen sijainnin käyttäjälle. Voimme siis korreloida muita tapahtumia ja käyttää näiden aikaleimoja lisäheuristiikkana, joka voidaan lisätä analyysiimme.

Esimerkiksi aiemmin mainitsemassani osoitteessa, jota on käytetty useita kertoja, voidaan havaita, että tapahtumat, olivatpa ne saapuvia tai lähteviä, keskittyvät 13 tunnin aikaväliin.
![analyysi](assets/notext/12.webp)
*Krediitti: OXT*

Tämä aikaväli vastaa todennäköisesti Eurooppaa, Afrikkaa tai Lähi-itää. Siksi voidaan tulkita, että näiden tapahtumien takana oleva käyttäjä asuu siellä.

Toisessa rekisterissä on myös tämän tyyppinen ajallinen analyysi, joka mahdollisti oletuksen, että Satoshi Nakamoto ei toiminut Japanista käsin, vaan todellakin Yhdysvalloista: [https://medium.com/@insearchofsatoshi/the-time-zones-of-satoshi-nakamoto-aa40f035178f](https://medium.com/@insearchofsatoshi/the-time-zones-of-satoshi-nakamoto-aa40f035178f)

### Volyymien Analyysi
Toinen ulkoinen heuristiikka, jota voidaan käyttää, on kaupankäynnin volyymien analyysi. Entiteetille kohdistettujen kunkin tapahtuman määrien perusteella tämä tieto voidaan käyttää lisäheuristiikkana loppuanalyysissä.
Tämä heuristiikka on ilmeisen heikko, mutta se voi auttaa vähentämään epävarmuutta, kun sitä käytetään muiden heuristiikkojen kanssa.

## Miten suojautua ketjuanalyysiltä?
Bitcoin-käyttäjänä sinulla on oikeus suojata yksityisyytesi. Tämä johtuu luonnollisista oikeuksistasi omistaa ja määrätä itsestäsi, jotka ovat jokaiselle yksilölle ominaisia, riippumatta mistään lainsäädännöllisestä rajoitteesta.

Tämä luonnollinen oikeus suojata omaa yksityisyyttään muuttuu myös vaatimus-oikeudeksi, joka on vahvistettu Ihmisoikeuksien yleismaailmallisen julistuksen artiklassa 12, jossa todetaan, että "*Ketään ei saa mielivaltaisesti häiritä hänen yksityisyydessään, perheessään, kodissaan tai kirjeenvaihdossaan, eikä kajota hänen kunniinsa tai maineeseensa. Jokaisella on oikeus lain suojaan tällaista häirintää tai hyökkäyksiä vastaan.*".

Kuitenkin yritysten, jotka erikoistuvat ketjuanalyysiin, ydinliiketoiminta koostuu nimenomaan yksityisyytesi loukkaamisesta, vaarantaen kirjeenvaihtosi luottamuksellisuuden. Vaikka voisi toivoa, että edellä mainitun vaatimus-oikeuden mukaisesti valtiot puolustaisivat voimakkaasti yksityisyyttämme, eivät ne ainoastaan laiminlyö tehdä niin, vaan myös rahoittavat merkittävästi näiden analyysiyhtiöiden toimintaa. Olisi myös turhaa toivoa tukea ala-associatioilta, jotka vaikuttavat olevan valmiita tekemään kaikki myönnytykset lainsäätäjän edessä.

Faktisesti tämä vaatimus-oikeus yksityisyyteen Bitcoinissa ei ole olemassa. Siksi sinun, käyttäjän, on itse vaadittava luonnollista oikeuttasi ja suojattava kirjeenvaihtosi luottamuksellisuus. Tämä edellyttää erilaisten tekniikoiden ja käyttötavojen omaksumista, jotka mahdollistavat ketjuanalyysiin käytettyjen heuristiikkojen estämisen tai harhauttamisen.

### Välttäen joutumasta heuristiikkojen ansaan
Ensinnäkin, ennen kuin harkitsemme radikaalimpia menetelmiä, on suositeltavaa rajoittaa altistumistamme ketjuanalyysissä käytetyille heuristiikoille mahdollisimman paljon. Kuten aiemmin mainittiin, kaksi tehokkainta heuristiikkaa ovat osoitteen uudelleenkäyttö ja COINJOIN.
Perusperiaate yksityisyytesi turvaamiseksi Bitcoinissa perustuu uuden, puhtaan osoitteen käyttämiseen jokaiselle lompakkoosi saapuvalle transaktiolle. Osoitteen uudelleenkäyttö on todellakin suurin uhka yksityisyydelle Bitcoinissa.
Yksittäiselle käyttäjälle uuden osoitteen generoiminen jokaiselle saapuvalle maksulle on erittäin yksinkertaista. Modernit lompakot tekevät tämän automaattisesti heti, kun klikkaat "Vastaanota". Joten, jos pidät edes vähäisessä määrin tärkeänä transaktioidesi yksityisyyttä, uusien osoitteiden käyttö edustaa ehdotonta minimiä. Jos tarvitset staattisen yhteyspisteen internetissä, voit käyttää ratkaisuja [kuten PayNym, joka implementoi BIP47](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093) vastaanotto-osoitteen sijaan.
Seuraavaksi, jos haluat toimia ketjuanalyysiä vastaan, vältä UTXO:iden yhdistämistä transaktion syötteessä. Minimissään, jos todella tarvitset yhdistää, suosi UTXO:ja, joilla on sama lähde. Tämä suositus edellyttää hyvää UTXO:idesi hallintaa. Ostaessasi bitcoinejasi, suosi siirtoja, jotka sisältävät suuria määriä maksimoidaksesi maksujen määrän ilman, että sinun tarvitsee yhdistää. Suosittelen myös merkitsemään UTXO:si ohjelmistossasi tunnistaaksesi niiden alkuperän ja välttääksesi yhdistämisen eri lähteistä.

Laajemmin kaikkien muiden heuristiikkojen osalta sinun tarvitsee tuntea ne yrittääksesi olla lankeamatta niihin:
- Älä käytä vähemmistöskriptejä. Suosi SegWit V0 tai mahdollisesti SegWit V1;
- Älä tee maksuja pyöreissä numeroissa. Esimerkiksi, jos tarvitset lähettää 100k satoshia ystävällesi, lähetä heille 114,486 satoshia. He ostavat sinulle juoman vastapalveluksena;
- Yritä olla aina saamatta vaihtorahaa, joka on paljon suurempi kuin maksutulos;
- Älä julkaise vastaanotto-osoitteitasi sosiaalisessa mediassa;
- Käytä omaa nodea Torin alla lähettääksesi transaktiosi;
- Yritä olla lähettämättä Bitcoin-transaktioitasi aina samaan aikaan…

### Yksityisyyden suojaamisen työkalujen käyttö
Voit myös kääntyä menetelmien puoleen, jotka tekevät Bitcoinin käytöstäsi epäselvää ketjuanalyysin estämiseksi tai harhauttamiseksi.

Suosituin tekniikka on varmasti Coinjoin, yhteistyössä toteutettu transaktiorakenne, joka mobilisoi useita samansuuruisia UTXO:ja. Tässä on tavoitteena rikkoa deterministiset linkit, estäen näin analyysit menneisyydestä nykyhetkeen ja nykyhetkestä menneisyyteen. Coinjoin mahdollistaa uskottavan kiistämisen piilottamalla kolikkosi suureen ryhmään erottamattomia kolikoita. Jos haluat oppia lisää Coinjoinista, sekä teknisesti että käytännöllisesti, suosittelen lukemaan nämä muut artikkelit ja tutoriaalit:
- [COINJOIN - SAMOURAI WALLET](https://planb.network/tutorials/privacy/on-chain/coinjoin-samourai-wallet-e566803d-ab3f-4d98-9136-5462009262ef);
- [COINJOIN - SPARROW WALLET](https://planb.network/tutorials/privacy/on-chain/coinjoin-sparrow-wallet-84def86d-faf5-4589-807a-83be60720c8b);
- [WHIRLPOOL STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375).
![analyysi](assets/en/13.webp)

CoinJoin on erinomainen työkalu kolikoiden uskottavan kiistämisen luomiseen, mutta se ei ole optimoitu kaikkiin käyttäjän yksityisyyden tarpeisiin. Erityisesti CoinJoin ei ole suunniteltu maksuvälineeksi. Se on hyvin jäykkä vaihdettavien määrien suhteen täydellisen uskottavan kiistämisen tuottamiseksi. Koska transaktion tulosteiden määrää ei voi vapaasti valita, CoinJoinia ei voi käyttää maksujen tekemiseen bitcoineilla.
Kuvittele esimerkiksi, että haluan maksaa patongistani bitcoineilla samalla kun optimoin yksityisyyttäni. CoinJoinin käyttöönoton mahdottomuuden vuoksi, joka ei salli tuloutuvan UTXO:n määrän valintaa, huomaisin olevani kykenemätön säätämään kulutukseni määrää leipurin asettaman hinnan mukaisesti. Siksi CoinJoin osoittautuu riittämättömäksi maksutapahtumiin.

Muita työkaluja on suunniteltu vastaamaan yksityisyyden tarpeisiin tarkemmissa käyttötapauksissa. Esimerkiksi meillä on [PayJoin](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f), eräänlainen mini-CoinJoin, johon osallistuu vain kaksi osapuolta ja joka perustuu rakenteeseen, joka mahdollistaa maksun.

PayJoinin ainutlaatuisuus piilee sen kyvyssä tuottaa tavalliselta näyttävä transaktio, vaikka todellisuudessa se onkin mini-CoinJoin kahden käyttäjän välillä. Tässä rakenteessa transaktion vastaanottaja osallistuu syötteisiin yhdessä varsinaisen lähettäjän kanssa. Näin ollen vastaanottaja lisää transaktioon maksun itselleen, mikä mahdollistaa varsinaisen maksun suorittamisen.

Esimerkiksi, jos ostat patongin leipuriltasi 6 000 satoshilla UTXO:sta, joka on 10 000 satoshia, ja haluat tehdä PayJoinin, leipurisi lisää 15 000 satoshin UTXO:n, joka kuuluu heille, alkuperäisen transaktiosi syötteeksi, jonka he täysin palauttavat tulosteena, jotta he voivat harhauttaa heuristiikkaa:

![analyysi](assets/en/14.webp)

Transaktiomaksut on jätetty huomiotta yksinkertaistamaan kaavion ymmärtämistä.

PayJoinin tavoitteet ovat kaksijakoiset. Ensinnäkin sen tavoitteena on harhauttaa ulkopuolista tarkkailijaa luomalla harhautus COH:n kautta. Todellisuudessa kun analyytikko tarkastelee tätä transaktiota, he saattavat ajatella voivansa soveltaa COH:ta ja siten olettaa yhteisen omistajuuden eri syötteille. Todellisuudessa tämä oletus on väärä, sillä yksi syöte kuuluu lähettäjälle, kun taas toinen on vastaanottajan omistuksessa. Näin ollen PayJoin turmelee ketjuanalyysin johtamalla analyytikon harhaan.
PayJoinin toinen tavoite on harhauttaa analyytikkoa todellisen transaktion määrästä, kiitos sen erityisen tulosterakenteen. Näin ollen PayJoin kuuluu steganografian alaan. Se mahdollistaa todellisen transaktion määrän salaamisen harhauttavan transaktion sisällä.

Todellisuudessa, jos palaamme esimerkkiimme PayJoinin käytöstä patongin ostamiseen, ulkopuolinen tarkkailija saattaisi ajatella, että kyseessä on 4 000 satoshin tai 21 000 satoshin maksu. Todellisuudessa patongin maksu on 6 000 satoshia: 21 000 - 15 000 = 6 000. Todellinen maksun arvo on siis piilotettu valemaksumaskun sisälle, joka toimii harhautuksena ketjuanalyysille.

PayJoinin ja CoinJoinin lisäksi on monia muita Bitcoin-transaktiorakenteita, jotka joko estävät ketjuanalyysin tai harhauttavat sitä. Näiden joukossa voisin mainita [Stonewall](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)- ja [StonewallX2](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)-transaktiot, jotka mahdollistavat joko joustavan mini Coinjoinin tekemisen tai joustavan mini Coinjoinin matkimisen. On myös [Ricochet](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589)-transaktioita, jotka simuloivat bitcoinien omistajuuden muutosta tekemällä lukuisia valetransfereita itselleen.

Kaikki nämä työkalut ovat saatavilla Samourai Walletissa mobiililaitteilla ja Sparrow Walletissa PC:llä. Jos haluat oppia lisää näistä erityisistä transaktiorakenteista, suosittelen tutustumaan opetusohjelmiini:
- [PAYJOIN](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f);
- [PAYJOIN - SAMOURAI WALLET](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab);
- [PAYJOIN - SPARROW WALLET](https://planb.network/tutorials/privacy/on-chain/payjoin-sparrow-wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62);
- [STONEWALL](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4);
- [STONEWALL X2](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b);
- [RICOCHET](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).

## Yhteenveto
Ketjuanalyysi on käytäntö, joka pyrkii jäljittämään bitcoinien virtausta lohkoketjussa. Tätä varten analyytikot etsivät kaavoja ja ominaisuuksia, jotta he voivat tehdä enemmän tai vähemmän uskottavia oletuksia ja tulkintoja.

Näiden heuristiikkojen tarkkuus vaihtelee: jotkut tarjoavat suuremman varmuuden kuin toiset, mutta mikään ei voi väittää olevansa erehtymätön. Kuitenkin useiden yhtenevien heuristiikkojen kertyminen voi lieventää tätä synnynnäistä epävarmuutta, vaikka sen täydellistä poistamista ei ole mahdollista.
Voimme luokitella nämä menetelmät kolmeen erilliseen pääkategoriaan:
- Kaavat, keskittyvät kunkin siirron kokonaisrakenteeseen;
- Sisäiset heuristiikat, jotka mahdollistavat kaikkien siirron yksityiskohtien perusteellisen tarkastelun, ulottumatta sen kontekstiin;
- Ulkoiset heuristiikat, jotka kattavat siirron analysoinnin sen ympäristössä sekä kaiken ulkoisen tiedon, joka voi tarjota näkemyksiä.

Bitcoinin käyttäjänä on olennaista hallita ketjuanalyysin perusperiaatteet tehokkaasti vastustaakseen sitä ja suojellakseen näin yksityisyyttään.

## Tekninen Mini-Sanasto:
**P2PKH:** lyhenne sanoista Pay to Public Key Hash. Se on standardi skriptimalli, jota käytetään UTXO:n käyttöehtojen määrittämiseen. Sen avulla voidaan lukita bitcoineja julkisen avaimen hashin, eli vastaanotto-osoitteen, päälle. Tämä skripti liittyy Legacy-standardiin ja se esiteltiin Bitcoinin ensimmäisissä versioissa Satoshi Nakamoton toimesta. Toisin kuin P2PK:ssa, jossa julkinen avain sisällytetään skriptiin eksplisiittisesti, P2PKH käyttää julkisen avaimen kryptografista jälkeä, jonka mukana tulee myös jotain metadataa, jota kutsutaan "vastaanotto-osoitteeksi". Tämä skripti sisältää julkisen avaimen SHA256:n RIPEMD160-hashin ja määrää, että varojen käyttämiseksi vastaanottajan on toimitettava tähän hashiin sopiva julkinen avain sekä voimassa oleva digitaalinen allekirjoitus, joka on luotu yhdistettyä yksityistä avainta käyttäen. P2PKH-osoitteet koodataan käyttäen Base58Check-formaattia, mikä antaa niille vastustuskyvyn kirjoitusvirheitä vastaan käyttämällä tarkistussummaa. Nämä osoitteet alkavat aina numerolla 1.
**P2TR:** lyhenne sanoista Pay to Taproot ("maksa juureen"). Se on standardi skriptimalli, jota käytetään UTXO:n kulutusehtojen määrittämiseen. P2TR otettiin käyttöön Taprootin toteutuksen yhteydessä marraskuussa 2021. Se hyödyntää Schnorr-protokollaa kryptografisten avainten aggregointiin sekä Merkle-puita vaihtoehtoisille skripteille, joita kutsutaan MAST:ksi (Merkelized Alternative Script Tree). Toisin kuin perinteisissä transaktioissa, joissa kulutusehdot ovat julkisesti nähtävillä (joskus vastaanotettaessa, joskus kuluttaessa), P2TR mahdollistaa monimutkaisten skriptien piilottamisen yhden näennäisen julkisen avaimen taakse. Teknisesti P2TR-skripti lukitsee bitcoinit yksilölliseen Schnorrin julkiseen avaimen, jota merkitään K:lla. Tämä K-avain on kuitenkin itse asiassa aggregaatti julkisesta avaimesta P ja julkisesta avaimesta M, jälkimmäinen lasketaan Merkle-juuresta, joka on lista ScriptPubKey:stä. Avainten aggregointi suoritetaan käyttäen Schnorrin allekirjoitusprotokollaa. P2TR-skriptillä lukitut bitcoinit voidaan kuluttaa kahdella erillisellä tavalla: joko julkaisemalla allekirjoitus julkiselle avaimelle P, tai täyttämällä yksi Merkle-puussa olevista skripteistä. Ensimmäistä vaihtoehtoa kutsutaan "avainpoluksi" ja toista "skriptipoluksi". Näin ollen P2TR mahdollistaa käyttäjille bitcoinien lähettämisen joko julkiseen avaimen tai heidän valitsemiinsa useisiin skripteihin. Tämän skriptin toinen etu on, että vaikka P2TR-tuloksen kuluttamiseen on useita tapoja, vain käytetty tapa tarvitsee paljastaa kuluttaessa, mikä mahdollistaa käyttämättömien vaihtoehtojen pysymisen yksityisinä. Esimerkiksi Schnorrin avainten aggregoinnin ansiosta julkinen avain P voi itsessään olla aggregoitu avain, mahdollisesti edustaen multisigia. P2TR on version 1 SegWit-tulos, mikä tarkoittaa, että P2TR-syötteiden allekirjoitukset tallennetaan transaktion todistajaosaan, eikä ScriptSig-osioon. P2TR-osoitteet käyttävät Bech32m-koodausta ja alkavat bc1p:llä.

**P2WPKH:** Lyhenne sanoista Pay to Witness Public Key Hash. Se on standardi skriptimalli, jota käytetään UTXO:n kulutusehtojen määrittämiseen. P2WPKH otettiin käyttöön SegWitin toteutuksen yhteydessä elokuussa 2017. Tämä skripti on samankaltainen kuin P2PKH (Pay to Public Key Hash), siinä mielessä, että se myös lukitsee bitcoinit julkisen avaimen hashin perusteella, eli vastaanotto-osoitteen perusteella. Ero on siinä, miten allekirjoitukset ja skriptit sisällytetään transaktioon. P2WPKH-tapauksessa allekirjoitusskriptin tiedot (ScriptSig) siirretään perinteisestä transaktiorakenteesta erilliseen osioon nimeltä Witness. Tämä siirto on SegWit-päivityksen (Segregated Witness) ominaisuus. Tällä tekniikalla on etuna transaktiodatan koon pienentäminen pääosassa, samalla kun tarvittavat skriptitiedot säilytetään validointia varten erillisessä osiossa. Tämän seurauksena P2WPKH-transaktiot ovat yleensä edullisempia maksujen suhteen verrattuna Legacy-transaktioihin. P2WPKH-osoitteet kirjoitetaan käyttäen Bech32-koodausta, mikä edistää tiiviimpää ja vähemmän virhealtista kirjoitusta BCH-tarkistussumman ansiosta. Nämä osoitteet alkavat aina bc1q:lla, mikä tekee niistä helposti erottuvia Legacy-vastaanotto-osoitteista. P2WPKH on version 0 SegWit-tulos.
**UTXO:** Lyhenne sanoista Unspent Transaction Output. UTXO on transaktioon liittyvä lähtö, jota ei ole vielä käytetty tai hyödynnetty uuden transaktion syötteenä. UTXO:t edustavat sitä bitcoinejen osuutta, joka käyttäjällä on omistuksessaan ja joka on tällä hetkellä käytettävissä. Jokaiseen UTXO:on liittyy tietty lähtöskripti, joka määrittelee ehdot bitcoinejen käyttämiseksi. Bitcoin-transaktiot kuluttavat näitä UTXO:ja syötteinä ja luovat uusia UTXO:ja lähtöinä. UTXO-malli on olennainen osa Bitcoinia, sillä se mahdollistaa transaktioiden helpon varmistamisen siinä mielessä, ettei yritetä käyttää olemattomia tai jo käytettyjä bitcoineja. Käytännössä UTXO on pala Bitcoinia.






