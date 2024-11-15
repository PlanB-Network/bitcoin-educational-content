---
name: Johdatus formaaliin kryptografiaan
goal: Syvällinen johdatus kryptografian tieteeseen ja käytäntöön.
objectives:
  - Tutkia Beale-salakirjoituksia ja nykyaikaisia kryptografisia menetelmiä ymmärtääkseen kryptografian perus- ja historiallisia käsitteitä.
  - Syventyä lukuteoriaan, ryhmiin ja kenttiin hallitakseen kryptografian taustalla olevia keskeisiä matemaattisia käsitteitä.
  - Opiskella RC4-virtasalausta ja AES:ää 128-bittisellä avaimella oppiakseen symmetrisistä kryptografisista algoritmeista.
  - Tutkia RSA-kryptosysteemiä, avainten jakelua ja hajautusfunktioita tutustuakseen asymmetriseen kryptografiaan.

---
# Syväsukellus kryptografiaan

On vaikea löytää monia materiaaleja, jotka tarjoaisivat hyvän keskitien kryptografian opetuksessa.

Toisaalta on olemassa pitkiä, formaaleja käsitelmiä, jotka ovat todella saavutettavissa vain niille, joilla on vahva tausta matematiikassa, logiikassa tai jossakin muussa formaalissa tieteessä. Toisaalta on olemassa erittäin korkean tason johdantoja, jotka todella piilottavat liian monta yksityiskohtaa keneltäkään, joka on edes hieman utelias.

Tämä johdatus kryptografiaan pyrkii vangitsemaan keskitien. Vaikka sen tulisi olla suhteellisen haastava ja yksityiskohtainen kenelle tahansa, joka on uusi kryptografiassa, se ei ole tyypillisen perustavaa laatua olevan käsitelmän kaninkolo.

+++

# Johdanto
<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>

## Lyhyt kuvaus
<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

Tämä kirja tarjoaa syvällisen johdatuksen kryptografian tieteeseen ja käytäntöön. Missä mahdollista, se keskittyy käsitteelliseen, pikemminkin kuin formaaliin esitykseen materiaalista.

> Tämä kurssi perustuu [JWBurgersin repoon](https://github.com/JWBurgers/An_Introduction_to_Cryptography). Kaikki oikeudet hänelle. Sisältö ei ole vielä valmis ja on täällä vain esimerkkinä siitä, miten voisimme integroida sen, jos JWburger suostuu.

### Motivaatio ja tavoitteet

On vaikea löytää monia materiaaleja, jotka tarjoaisivat hyvän keskitien kryptografian opetuksessa.

Toisaalta on olemassa pitkiä, formaaleja käsitelmiä, jotka ovat todella saavutettavissa vain niille, joilla on vahva tausta matematiikassa, logiikassa tai jossakin muussa formaalissa tieteessä. Toisaalta on olemassa erittäin korkean tason johdantoja, jotka todella piilottavat liian monta yksityiskohtaa keneltäkään, joka on edes hieman utelias.

Tämä johdatus kryptografiaan pyrkii vangitsemaan keskitien. Vaikka sen tulisi olla suhteellisen haastava ja yksityiskohtainen kenelle tahansa, joka on uusi kryptografiassa, se ei ole tyypillisen perustavaa laatua olevan käsitelmän kaninkolo.

### Kohderyhmä

Kehittäjistä älyllisesti uteliaisiin, tämä kirja on hyödyllinen kenelle tahansa, joka haluaa enemmän kuin pinnallisen ymmärryksen kryptografiasta. Jos tavoitteenasi on hallita kryptografian alaa, tämä kirja on myös hyvä lähtökohta.

### Lukusuositukset

Kirja sisältää tällä hetkellä seitsemän lukua: "Mikä on kryptografia?" (Luku 1), "Kryptografian matemaattiset perusteet I" (Luku 2), "Kryptografian matemaattiset perusteet II" (Luku 3), "Symmetrinen kryptografia" (Luku 4), "RC4 ja AES" (Luku 5), "Asymmetrinen kryptografia" (Luku 6) ja "RSA-kryptosysteemi" (Luku 7). Vielä lisättävä viimeinen luku, "Kryptografia käytännössä", keskittyy erilaisiin kryptografisiin sovelluksiin, mukaan lukien kuljetuskerroksen turvallisuus, sipulireititys ja Bitcoinin arvonvaihtojärjestelmä.
Ellet ole vahvasti perehtynyt matematiikkaan, lukuteoria on todennäköisesti tämän kirjan vaikein aihe. Tarjoan siitä yleiskatsauksen luvussa 3, ja se esiintyy myös AES:n esittelyssä luvussa 5 ja RSA-salakirjoitusjärjestelmässä luvussa 7.
Jos kamppailet todella näiden kirjan osien muodollisten yksityiskohtien kanssa, suosittelen, että tyydyt ensimmäisellä kerralla niiden korkean tason lukemiseen.

### Kiitokset

Vaikuttavin kirja tämän teoksen muotoutumisessa on ollut Jonathan Katz ja Yehuda Lindellin _Johdatus moderniin kryptografiaan_, CRC Press (Boca Raton, FL), 2015. Siihen liittyvä kurssi on saatavilla Courserassa nimellä "Kryptografia."

Tärkeimmät lisälähteet, jotka ovat olleet hyödyllisiä tämän kirjan yleiskatsauksen luomisessa, ovat Simon Singh, _Koodikirja_, Fourth Estate (Lontoo, 1999); Christof Paar ja Jan Pelzl, _Ymmärrä kryptografiaa_, Springer (Heidelberg, 2010) ja [Paarin kirjaan perustuva kurssi nimeltä “Johdatus kryptografiaan”](https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); sekä Bruce Schneier, Sovellettu kryptografia, 2. painos, 2015 (Indianapolis, IN: John Wiley & Sons).

Viittaan vain erittäin spesifeihin tietoihin ja tuloksiin, jotka otan näistä lähteistä, mutta haluan tässä yhteydessä tunnustaa yleisen velkani niille.

Niille lukijoille, jotka haluavat etsiä edistyneempää tietoa kryptografiasta tämän johdannon jälkeen, suosittelen lämpimästi Katzin ja Lindellin kirjaa. Katzin kurssi Courserassa on hieman kirjaa helpommin lähestyttävä.

### Osallistumiset

Ole hyvä ja tutustu [projektin osallistumistiedostoon repertuaarissa](https://github.com/JWBurgers/An_Introduction_to_Cryptography/blob/master/Contributions.md) saadaksesi ohjeita siitä, miten voit tukea projektia.

### Notaatio

**Avainkäsitteet:**

Avainkäsitteet esitellään tekemällä ne lihavoiduiksi. Esimerkiksi Rijndael-salauksen esittely avainkäsitteenä näyttäisi seuraavalta: **Rijndael-salakirjoitus**.

Avainkäsitteet määritellään nimenomaisesti, elleivät ne ole omia nimiä tai niiden merkitys on ilmeinen keskustelusta.

Määritelmä annetaan yleensä avainkäsitteen esittelyn yhteydessä, vaikka joskus määritelmän antaminen myöhemmässä vaiheessa on kätevämpää.

**Korostetut sanat ja lauseet:**

Sanat ja lauseet korostetaan kursiivilla. Esimerkiksi lause "Muista salasanasi" näyttäisi seuraavalta: *Muista salasanasi*.

**Formaali notaatio:**

Formaali notaatio koskee pääasiassa muuttujia, satunnaismuuttujia ja joukkoja.

* Muuttujat: Nämä on yleensä vain merkitty pienellä kirjaimella (esim. "x" tai "y"). Joskus ne kirjoitetaan isolla kirjaimella selkeyden vuoksi (esim. "M" tai "K").
* Satunnaismuuttujat: Nämä on aina merkitty isolla kirjaimella (esim. "X" tai "Y")
* Joukot: Nämä on aina merkitty lihavoiduilla, isoilla kirjaimilla (esim. **S**)

# Mikä on kryptografia?
<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>

## Bealen koodit
<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>
Aloitetaan tutkimusmatkamme kryptografian alalle yhdellä sen historian viehättävimmistä ja viihdyttävimmistä jaksoista: Bealen kirjoitusten tarinalla. [1]
Mielestäni Bealen kirjoitusten tarina on todennäköisemmin fiktiota kuin todellisuutta. Mutta sen kerrotaan tapahtuneen seuraavasti.

Sekä vuoden 1820 että 1822 talvella mies nimeltä Thomas J. Beale majoittui Robert Morrissin omistamaan majataloon Lynchburgissa (Virginia). Bealen toisen vierailun päätteeksi hän antoi Morrissille rautalaatikon, jossa oli arvokkaita papereita säilytettäväksi.

Muutama kuukausi myöhemmin Morriss sai Bealelta kirjeen, päivätty 9. toukokuuta 1822. Siinä korostettiin rautalaatikon sisällön suurta arvoa ja annettiin Morrissille joitakin ohjeita: jos Beale tai kukaan hänen yhteistyökumppaneistaan ei koskaan tulisi vaatimaan laatikkoa, hänen tulisi avata se tarkalleen kymmenen vuotta kirjeen päiväyksestä (eli 9. toukokuuta 1832). Osa papereista sisällä olisi kirjoitettu tavallisella tekstillä. Useat muut kuitenkin olisivat "käsittämättömiä ilman avaimen apua". Tämä "avain" toimitettaisiin sitten Morrissille Bealen nimettömän ystävän toimesta kesäkuussa 1832.

Selkeistä ohjeista huolimatta Morriss ei avannut laatikkoa toukokuussa 1832, eikä Bealen salaperäinen ystävä ilmaantunut kesäkuussa kyseisenä vuonna. Vasta 1845 majatalonpitäjä päätti lopulta avata laatikon. Sieltä Morriss löysi muistiinpanon, jossa selitettiin, miten Beale ja hänen yhteistyökumppaninsa löysivät kultaa ja hopeaa lännestä ja hautasivat sen, yhdessä jonkin verran koruja, turvaan. Lisäksi laatikko sisälsi kolme **salakirjoitusta**: tekstejä, jotka on kirjoitettu koodilla ja jotka vaativat **kryptografisen avaimen**, tai salaisuuden, ja siihen liittyvän algoritmin avatakseen. Tämän prosessin, jossa salakirjoitus avataan, tunnetaan **dekrptointina**, kun taas lukitsemisprosessi tunnetaan **enkryptointina**. (Kuten luvussa 3 selitetään, termillä salakirjoitus voi olla erilaisia merkityksiä. Nimityksessä "Bealen kirjoitukset" se tarkoittaa salakirjoituksia.)

Kolme salakirjoitusta, jotka Morriss löysi rautalaatikosta, koostuvat sarjasta numeroita, jotka on erotettu toisistaan pilkuilla. Bealen muistiinpanon mukaan nämä salakirjoitukset antavat erikseen aarteen sijainnin, aarteen sisällön ja luettelon nimistä oikeutettuine perillisineen aarteen osuuksineen (jälkimmäinen tieto on relevantti, jos Beale ja hänen yhteistyökumppaninsa eivät koskaan tulisi vaatimaan laatikkoa).

Morris yritti dekryptoida kolme salakirjoitusta kaksikymmentä vuotta. Tämä olisi ollut helppoa avaimen kanssa. Mutta Morrissilla ei ollut avainta, eikä hän onnistunut yrityksissään palauttaa alkuperäisiä tekstejä, tai **selkotekstejä** kuten niitä tyypillisesti kutsutaan kryptografiassa.

Elämänsä loppupuolella Morriss siirsi laatikon ystävälleen vuonna 1862. Tämä ystävä julkaisi myöhemmin pamfletin vuonna 1885, salanimellä J.B. Ward. Se sisälsi kuvauksen (väitetystä) laatikon historiasta, kolmesta salakirjoituksesta ja ratkaisusta, jonka hän oli löytänyt toiselle salakirjoitukselle. (Ilmeisesti jokaiselle salakirjoitukselle on oma avaimensa, eikä yhtä avainta, joka toimisi kaikilla kolmella salakirjoituksella, kuten Beale alun perin näyttää ehdottaneen kirjeessään Morrissille.)

Toisen salakirjoituksen voit nähdä *Kuvassa 2* alla. [2] Tämän salakirjoituksen avain on Yhdysvaltain itsenäisyysjulistus. Dekryptointimenettely perustuu seuraavien kahden säännön soveltamiseen:
* Etsi salatekstistä mikä tahansa numero n ja etsi Yhdysvaltain itsenäisyysjulistuksen n:s sana
* Korvaa numero n löytämäsi sanan ensimmäisellä kirjaimella

*Kuva 1: Beale-salakirjoitus nro 2*

![Kuva 1: Beale-salakirjoitus nro 2.](assets/Figure1-1.webp "Kuva 1: Beale-salakirjoitus nro 2")

Esimerkiksi toisen salatekstin ensimmäinen numero on 115. Itsenäisyysjulistuksen 115. sana on “instituted”, joten tekstin ensimmäinen kirjain on “i”. Salateksti ei suoraan osoita sanojen välejä ja isoja alkukirjaimia. Mutta ensimmäisten muutamien sanojen purkamisen jälkeen voidaan loogisesti päätellä, että tekstin ensimmäinen sana oli yksinkertaisesti “I.” (Teksti alkaa lauseella “I have deposited in the county of Bedford.”)

Purkamisen jälkeen toinen viesti tarjoaa yksityiskohtaiset tiedot aarteesta (kulta, hopea ja jalokivet) ja ehdottaa, että se oli haudattu rautapatoihin ja peitetty kivillä Bedfordin piirikunnassa (Virginia). Ihmiset rakastavat hyviä mysteerejä, joten suuria ponnistuksia on käytetty muiden kahden Beale-salakirjoituksen purkamiseen, erityisesti sen, joka kuvailee aarteen sijaintia. Jopa useat merkittävät kryptografit ovat yrittäneet niitä ratkaista. Kuitenkaan kukaan ei ole vielä onnistunut purkamaan kahta muuta salatekstiä.

**Huomautuksia:**

[1] Hyvä yhteenveto tarinasta löytyy Simon Singhin teoksesta *The Code Book*, Fourth Estate (Lontoo, 1999), sivut 82-99. Tarinasta tehtiin lyhytelokuva Andrew Allenin toimesta vuonna 2010. Elokuvan, “The Thomas Beale Cipher,” löydät sen verkkosivustolta [täältä](http://www.thomasbealecipher.com/).

[2] Tämä kuva on saatavilla Beale-salakirjoitusten Wikipedia-sivulla.

## Moderni kryptografia
<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>

Värikkäät tarinat, kuten Beale-salakirjoitusten tarina, ovat sitä, mitä useimmat meistä yhdistävät kryptografiaan. Kuitenkin moderni kryptografia eroaa ainakin neljällä tärkeällä tavalla näistä historiallisista esimerkeistä.

Ensinnäkin, historiallisesti kryptografia on keskittynyt vain **salaisuuteen** (tai luottamuksellisuuteen). [3] Salatekstejä luotiin varmistamaan, että vain tietyt osapuolet voivat olla perillä avotekstien tiedoista, kuten Beale-salakirjoitusten tapauksessa. Jotta salausjärjestelmä palvelisi tätä tarkoitusta hyvin, salatekstin purkaminen tulisi olla mahdollista vain, jos sinulla on avain.

Moderni kryptografia keskittyy laajempaan teemojen kirjoon kuin pelkkä salaisuus. Nämä teemat sisältävät ensisijaisesti (1) **viestin eheyden**—eli varmistamisen, että viestiä ei ole muutettu; (2) **viestin aitouden**—eli varmistamisen, että viesti on todella tullut tietyltä lähettäjältä; ja (3) **kiistämättömyyden**—eli varmistamisen, että lähettäjä ei voi myöhemmin väärin perustein kieltää lähettäneensä viestiä. [4]

Tärkeä ero, joka tulee pitää mielessä, on siis **salausjärjestelmän** ja **kryptografisen järjestelmän** välillä. Salausjärjestelmä keskittyy vain salaisuuteen. Vaikka salausjärjestelmä on kryptografinen järjestelmä, päinvastainen ei pidä paikkaansa. Kryptografinen järjestelmä voi myös palvella kryptografian muita pääteemoja, mukaan lukien eheys, aitous ja kiistämättömyys.
Eheyden ja aitouden teemat ovat yhtä tärkeitä kuin salassapito. Nykyaikaiset viestintäjärjestelmämme eivät voisi toimia ilman takeita viestinnän eheydestä ja aitoudesta. Kiistämättömyys on myös tärkeä huolenaihe, kuten digitaalisissa sopimuksissa, mutta se ei ole yhtä laajalti tarpeellinen kryptografisissa sovelluksissa kuin salassapito, eheys ja aitous.

Toiseksi, klassiset salausjärjestelmät, kuten Beale-salakirjoitukset, sisälsivät aina yhden avaimen, joka jaettiin kaikkien asiaankuuluvien osapuolten kesken. Monet nykyaikaiset kryptografiset järjestelmät kuitenkin sisältävät ei vain yhden, vaan kaksi avainta: **yksityisen** ja **julkisen avaimen**. Vaikka edellisen tulisi pysyä yksityisenä kaikissa sovelluksissa, jälkimmäinen on tyypillisesti julkista tietoa (siitä niiden nimet). Salausalalla julkinen avain voidaan käyttää viestin salaamiseen, kun taas yksityistä avainta voidaan käyttää salauksen purkamiseen.

Kryptografian haara, joka käsittelee järjestelmiä, joissa kaikki osapuolet jakavat yhden avaimen, tunnetaan nimellä **symmetrinen kryptografia**. Tällaisen järjestelmän yksittäistä avainta kutsutaan yleensä **yksityiseksi avaimiksi** (tai salaiseksi avaimiksi). Kryptografian haara, joka käsittelee järjestelmiä, jotka vaativat yksityisen-julkisen avainparin, tunnetaan nimellä **asymmetrinen kryptografia**. Näitä haaroja kutsutaan joskus myös **yksityisen avaimen kryptografiaksi** ja **julkisen avaimen kryptografiaksi**, vastaavasti (vaikka tämä voi aiheuttaa sekaannusta, koska julkisen avaimen kryptografisissa järjestelmissä on myös yksityisiä avaimia).

Asymmetrisen kryptografian tulo 1970-luvun lopulla on ollut yksi kryptografian historian tärkeimmistä tapahtumista. Ilman sitä useimmat nykyaikaiset viestintäjärjestelmämme, mukaan lukien Bitcoin, eivät olisi mahdollisia tai ainakin hyvin epäkäytännöllisiä.

Tärkeää on, että nykyaikainen kryptografia ei ole yksinomaan symmetristen ja asymmetristen avainkryptografisten järjestelmien tutkimusta (vaikka se kattaa suuren osan alasta). Esimerkiksi kryptografia käsittelee myös hajautusfunktioita ja pseudosatunnaislukugeneraattoreita, ja näiden primitiivien pohjalta voidaan rakentaa sovelluksia, jotka eivät liity symmetriseen tai asymmetriseen avainkryptografiaan.

Kolmanneksi, klassiset salausjärjestelmät, kuten Beale-salakirjoituksissa käytetyt, olivat enemmän taidetta kuin tiedettä. Niiden koettu turvallisuus perustui suurelta osin intuitioihin niiden monimutkaisuudesta. Ne tyypillisesti paikattiin, kun niiden haavoittuvuus uusille hyökkäyksille opittiin, tai hylättiin kokonaan, jos hyökkäys oli erityisen vakava. Nykyaikainen kryptografia on kuitenkin tiukka tiede, jolla on muodollinen, matemaattinen lähestymistapa sekä kryptografisten järjestelmien kehittämiseen että analysointiin.

Erityisesti nykyaikainen kryptografia keskittyy muodollisiin **turvallisuustodistuksiin**. Kryptografisen järjestelmän turvallisuustodistus etenee kolmessa vaiheessa:

1. **Kryptografisen turvallisuuden määritelmän** lausunto, eli turvallisuustavoitteiden joukko ja hyökkääjän aiheuttama uhka.
2. Matemaattisten oletusten lausunto järjestelmän laskennallisen monimutkaisuuden suhteen. Esimerkiksi kryptografisessa järjestelmässä voi olla pseudosatunnaislukugeneraattori. Vaikka emme voi todistaa niiden olemassaoloa, voimme olettaa, että ne ovat olemassa.
3. Matemaattisen **turvallisuustodistuksen** esittäminen järjestelmän turvallisuudesta muodollisen turvallisuuskäsitteen ja kaikkien matemaattisten oletusten perusteella.

Neljänneksi, vaikka historiallisesti kryptografiaa käytettiin ensisijaisesti sotilasympäristöissä, se on tullut tunkeutumaan päivittäisiin toimiimme digitaalisella aikakaudella. Olitpa sitten pankkiasioissa verkossa, postaamassa sosiaalisessa mediassa, ostamassa tuotetta Amazonista luottokortillasi tai antamassa kaverille bitcoineja, kryptografia on digitaalisen aikakautemme välttämättömyys.

Näiden neljän näkökulman perusteella voimme luonnehtia nykyaikaista **kryptografiaa** tieteenalaksi, joka keskittyy kryptografisten järjestelmien muodolliseen kehittämiseen ja analysointiin digitaalisen tiedon suojaamiseksi vihamielisiltä hyökkäyksiltä. Turvallisuus tässä yhteydessä tulisi ymmärtää laajasti hyökkäysten estämisenä, jotka vahingoittavat salassapitoa, eheyttä, autentikointia ja/tai kiistämättömyyttä viestinnässä.
Kryptografiaa pidetään parhaiten kyberturvallisuuden aladisipliinina, joka keskittyy tietokonejärjestelmien varkauden, vahingoittumisen ja väärinkäytön estämiseen. On huomattava, että monet kyberturvallisuushuolet ovat vain vähän tai osittain yhteydessä kryptografiaan. 
Esimerkiksi, jos yritys sijoittaa kalliita palvelimia paikallisesti, he saattavat olla huolissaan tämän laitteiston suojaamisesta varkauksilta ja vahingoilta. Vaikka tämä on kyberturvallisuushuoli, sillä on vähän tekemistä kryptografian kanssa.

Toisena esimerkkinä, **phishing-hyökkäykset** ovat yleinen ongelma nykyaikana. Nämä hyökkäykset pyrkivät huijaamaan ihmisiä sähköpostitse tai jonkin muun viestintävälineen kautta luovuttamaan arkaluonteisia tietoja, kuten salasanoja tai luottokorttinumeroita. Vaikka kryptografia voi auttaa torjumaan phishing-hyökkäyksiä tietyssä määrin, kattava lähestymistapa vaatii enemmän kuin vain jonkin kryptografian käyttöä.

**Huomautuksia:**

[3] Tarkalleen ottaen, kryptografisten järjestelmien tärkeät sovellukset ovat liittyneet salassapitoon. Lapset esimerkiksi käyttävät usein yksinkertaisia kryptografisia järjestelmiä "huvin vuoksi". Salassapito ei todellakaan ole huolenaihe näissä tapauksissa.

[4] Bruce Schneier, *Applied Cryptography*, 2. painos, 2015 (Indianapolis, IN: John Wiley & Sons), s. 2.

[5] Katso Jonathan Katz ja Yehuda Lindell, *Introduction to Modern Cryptography*, CRC Press (Boca Raton, FL: 2015), erit. s. 16–23, hyvä kuvaus.

[6] Vrt. Katz ja Lindell, ibid., s. 3. Mielestäni heidän karakterisointinsa on joissakin kohdissa ongelmallinen, joten esitän tässä hieman erilaisen version heidän lausunnostaan.

## Avoin viestintä

<chapterId>cb23d0a6-ba9a-5dc6-a55a-258405ae4117</chapterId>

Nykyajan kryptografia on suunniteltu tarjoamaan turvallisuusvakuutuksia avoimessa viestintäympäristössä. Jos viestintäkanavamme on niin hyvin suojattu, että salakuuntelijoilla ei ole mahdollisuutta manipuloida tai edes tarkkailla viestejämme, silloin kryptografia on tarpeetonta. Suurin osa viestintäkanavistamme ei kuitenkaan ole läheskään näin hyvin suojattu.

Nykyisen maailman viestinnän selkäranka on valtava kuituoptisten kaapeleiden verkosto. Puheluiden soittaminen, television katselu ja verkkoselailu nykyaikaisessa kotitaloudessa yleensä nojaa tähän kuituoptisten kaapeleiden verkkoon (pieni prosenttiosuus saattaa nojata puhtaasti satelliitteihin). On totta, että kotona saattaa olla erilaisia datayhteyksiä, kuten koaksiaalikaapeli, (epäsymmetrinen) digitaalinen tilaajayhteys ja kuituoptinen kaapeli. Mutta ainakin kehittyneessä maailmassa nämä erilaiset datavälineet liittyvät nopeasti talosi ulkopuolella solmuun valtavassa kuituoptisten kaapeleiden verkostossa, joka yhdistää koko maapallon. Poikkeuksia ovat jotkin kehittyneen maailman syrjäiset alueet, kuten Yhdysvalloissa ja Australiassa, missä dataliikenne saattaa silti matkata huomattavia etäisyyksiä perinteisten kuparipuhelinjohtojen kautta.

Olisi mahdotonta estää potentiaalisia hyökkääjiä fyysisesti pääsemästä käsiksi tähän kaapeliverkkoon ja sen tukirakenteisiin. Itse asiassa tiedämme jo, että suurin osa tiedoistamme on eri kansallisten tiedusteluvirastojen kaappaamaa tärkeissä internetin risteyskohdissa.[7] Tämä sisältää kaiken Facebook-viesteistä verkkosivujen osoitteisiin, joita vierailet.

Vaikka datan valvonta massiivisessa mittakaavassa vaatii voimakkaan vastustajan, kuten kansallisen tiedusteluviraston, vähäisin resurssein varustetut hyökkääjät voivat helposti yrittää vakoilla paikallisemmalla tasolla. Vaikka tämä voi tapahtua johdot kuuntelemalla, langattoman viestinnän kaappaaminen on paljon helpompaa.
Suurin osa paikallisesta verkkodatamme — olipa kyseessä kotona, toimistossa tai kahvilassa — kulkee nykyään radioaaltojen kautta langattomiin yhteyspisteisiin monitoimireitittimissä fyysisten kaapelien sijaan. Joten hyökkääjän tarvitsee käyttää vain vähän resursseja paikallisen liikenteesi kaappaamiseen. Tämä on erityisen huolestuttavaa, koska useimmat ihmiset tekevät hyvin vähän suojellakseen tietoja, jotka kulkevat heidän paikallisissa verkoissaan. Lisäksi mahdolliset hyökkääjät voivat myös kohdistaa iskujaan mobiililaajakaistayhteyksiimme, kuten 3G, 4G ja 5G. Kaikki nämä langattomat viestintätavat ovat helppoja kohteita hyökkääjille.
Tästä syystä viestinnän salassapidon idea suojatun viestintäkanavan kautta on toivottoman harhainen pyrkimys suuressa osassa nykymaailmaa. Kaikki mitä tiedämme, edellyttää vakavaa paranoiaa: sinun tulisi aina olettaa, että joku kuuntelee. Ja kryptografia on päätyökalumme minkäänlaisen turvallisuuden saavuttamiseksi tässä modernissa ympäristössä.

**Huomautukset:**

[7] Katso esimerkiksi Olga Khazan, “The creepy, long-standing practice of undersea cable tapping”, *The Atlantic*, 16. heinäkuuta 2013 (saatavilla osoitteessa [The Atlantic](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)).


# Kryptografian matemaattiset perusteet 1
<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>


## Satunnaismuuttujat
<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>

Kryptografia perustuu matematiikkaan. Ja jos haluat ymmärtää kryptografian enemmän kuin pinnallisesti, sinun on oltava mukava sen matematiikan kanssa.

Tämä luku esittelee suurimman osan perusmatematiikasta, johon törmäät opetellessasi kryptografiaa. Aiheisiin kuuluvat satunnaismuuttujat, modulo-operaatiot, XOR-operaatiot ja pseudosatunnaisuus. Sinun tulisi hallita näiden osioiden materiaali saadaksesi muuta kuin pinnallisen ymmärryksen kryptografiasta.

Seuraava osio käsittelee lukuteoriaa, joka on paljon haastavampi.

### Satunnaismuuttujat

Satunnaismuuttuja merkitään tyypillisesti lihavoimattomalla, isolla kirjaimella. Joten esimerkiksi voimme puhua satunnaismuuttujasta $X$, satunnaismuuttujasta $Y$ tai satunnaismuuttujasta $Z$. Tätä notaatiota tulen myös käyttämään jatkossa.

**Satunnaismuuttuja** voi saada kaksi tai useampia mahdollisia arvoja, joista kullakin on tietty positiivinen todennäköisyys. Mahdolliset arvot luetellaan **tulossarjassa**.

Joka kerta kun **otat näytteen** satunnaismuuttujasta, vedät tietyn arvon sen tulossarjasta määriteltyjen todennäköisyyksien mukaisesti.

Käännymme yksinkertaisen esimerkin puoleen. Oletetaan muuttuja $X$, joka on määritelty seuraavasti:

- $X$:llä on tulossarja $\{1,2\}$

$$
Pr[X = 1] = 0.5
$$

$$
Pr[X = 2] = 0.5
$$

On helppo nähdä, että $X$ on satunnaismuuttuja. Ensinnäkin, $X$ voi saada kaksi tai useampia mahdollisia arvoja, nimittäin $1$ ja $2$. Toiseksi, kullakin mahdollisella arvolla on positiivinen todennäköisyys esiintyä aina kun otat näytteen $X$:stä, nimittäin $0.5$.
Kaikki mitä satunnaismuuttuja vaatii, on tulossarja, jossa on kaksi tai useampi mahdollisuus, joista jokaisella on positiivinen todennäköisyys tapahtua otannassa. Periaatteessa satunnaismuuttuja voidaan siis määritellä abstraktisti, ilman mitään kontekstia. Tässä tapauksessa voit ajatella "otantaa" suorittamalla jonkin luonnollisen kokeen määrittääksesi satunnaismuuttujan arvon.
Muuttuja $X$ yllä määriteltiin abstraktisti. Voit siis ajatella muuttujan $X$ otantaa heittämällä reilua kolikkoa ja osoittamalla "2" jos tulee kruuna ja "1" jos tulee klaava. Jokaista $X$:n otosta varten heität kolikon uudelleen.

Vaihtoehtoisesti voit myös ajatella $X$:n otantaa heittämällä reilua noppaa ja osoittamalla "2" jos noppa näyttää $1$, $3$, tai $4$, ja osoittamalla "1" jos noppa näyttää $2$, $5$, tai $6$. Joka kerta kun otat $X$:n, heität noppaa uudelleen.

Todellisuudessa mikä tahansa luonnollinen koe, joka mahdollistaisi $X$:n mahdollisten arvojen todennäköisyyksien määrittämisen, voidaan kuvitella suhteessa piirrokseen.

Usein kuitenkin satunnaismuuttujat eivät ole vain abstraktisti esiteltyjä. Sen sijaan mahdollisten tulosten joukolla on eksplisiittinen todellisen maailman merkitys (eikä vain numeroina). Lisäksi nämä tulokset saattavat olla määriteltyjä jonkin tietyn tyyppistä kokeilua vasten (eikä vain mitä tahansa luonnollista kokeilua näiden arvojen kanssa).

Katsotaan nyt esimerkkiä muuttujasta $X$, joka ei ole määritelty abstraktisti. X määritellään seuraavasti määrittämään, kumpi kahdesta joukkueesta aloittaa jalkapallo-ottelun:

- $X$:n tulossarja on {punainen aloittaa, sininen aloittaa}
- Heitä tietty kolikko $C$: klaava = "punainen aloittaa"; kruuna = "sininen aloittaa"

$$
Pr [X = \text{punainen aloittaa}] = 0.5
$$

$$
Pr [X = \text{sininen aloittaa}] = 0.5
$$

Tässä tapauksessa X:n tulossarjalle on annettu konkreettinen merkitys, nimittäin kumpi joukkue aloittaa jalkapallo-ottelun. Lisäksi mahdolliset tulokset ja niiden todennäköisyydet määritetään konkreettisella kokeilulla, nimittäin heittämällä tiettyä kolikkoa $C$.

Kryptografian keskusteluissa satunnaismuuttujat esitellään yleensä tulossarjalla, jolla on todellisen maailman merkitys. Se voi olla kaikkien viestien joukko, joita voidaan salata, tunnetaan viestitilana, tai kaikkien avainten joukko, joita salauksen käyttäjät voivat valita, tunnetaan avaintilana.

Kryptografian keskusteluissa satunnaismuuttujat eivät kuitenkaan yleensä ole määriteltyjä jonkin tietyn luonnollisen kokeen perusteella, vaan minkä tahansa kokeen perusteella, joka saattaisi tuottaa oikeat todennäköisyysjakaumat.

Satunnaismuuttujilla voi olla diskreettejä tai jatkuvia todennäköisyysjakaumia. **Diskreetillä todennäköisyysjakaumalla** olevat satunnaismuuttujat — toisin sanoen diskreetit satunnaismuuttujat — ovat rajallinen määrä mahdollisia tuloksia. Satunnaismuuttuja $X$ molemmissa tähän mennessä annetuissa esimerkeissä oli diskreetti.

**Jatkuvat satunnaismuuttujat** voivat sen sijaan saada arvoja yhdessä tai useammassa välissä. Voisit esimerkiksi sanoa, että satunnaismuuttuja otannassa saa minkä tahansa todellisen arvon välillä 0 ja 1, ja että jokainen todellinen luku tässä välissä on yhtä todennäköinen. Tässä välissä on äärettömästi mahdollisia arvoja.

Kryptografian keskusteluissa sinun tarvitsee vain ymmärtää diskreetit satunnaismuuttujat. Kaikki tästä eteenpäin olevat satunnaismuuttujia koskevat keskustelut tulisi siis ymmärtää viittaavan diskreetteihin satunnaismuuttujiin, ellei toisin ole nimenomaisesti mainittu.

Satunnaismuuttujan mahdolliset arvot ja niihin liittyvät todennäköisyydet voidaan helposti visualisoida graafin avulla. Esimerkiksi, otetaan huomioon edellisessä osiossa mainittu satunnaismuuttuja $X$, jonka tulosten joukko on $\{1, 2\}$, ja $Pr [X = 1] = 0.5$ sekä $Pr [X = 2] = 0.5$. Tällainen satunnaismuuttuja esitetään tyypillisesti pylväsdiagrammina kuten *Kuva 1:ssä*.
*Kuva 1: Satunnaismuuttuja X*

![Kuva 1: Satunnaismuuttuja X.](assets/Figure2-1.webp)

*Kuva 1:ssä* olevat leveät palkit eivät tietenkään tarkoita, että satunnaismuuttuja $X$ olisi jatkuvasti muuttuva. Sen sijaan palkit on tehty leveiksi, jotta ne olisivat visuaalisesti houkuttelevampia (pelkkä suora viiva ylöspäin tarjoaisi vähemmän intuitiivisen visualisoinnin).

### Tasajakaumat

Ilmaisussa “satunnaismuuttuja” termi “satunnainen” tarkoittaa vain “todennäköisyysperusteista”. Toisin sanoen, se tarkoittaa vain, että kaksi tai useampi mahdollinen muuttujan tulos tapahtuu tietyillä todennäköisyyksillä. Nämä tulokset eivät kuitenkaan *välttämättä* ole yhtä todennäköisiä (vaikka termi “satunnainen” voi tosiaan tarkoittaa sitä muissa yhteyksissä).

**Tasajakauma** on erityistapaus satunnaismuuttujasta. Se voi saada kaksi tai useampia arvoja, joilla kaikilla on yhtä suuri todennäköisyys. *Kuvassa 1* esitetty satunnaismuuttuja $X$ on selvästi tasajakauma, sillä molemmat mahdolliset tulokset tapahtuvat todennäköisyydellä $0.5$. On kuitenkin monia satunnaismuuttujia, jotka eivät ole tasajakaumia.

Harkitse esimerkiksi satunnaismuuttujaa $Y$. Sen tulosten joukko on $\{1, 2, 3, 8, 10\}$ ja seuraava todennäköisyysjakauma:

$$
\Pr[Y = 1] = 0.25
$$

$$
\Pr[Y = 2] = 0.35
$$

$$
\Pr[Y = 3] = 0.1
$$

$$
\Pr[Y = 8] = 0.25
$$

$$
\Pr[Y = 10] = 0.05
$$

Vaikka kaksi mahdollista tulosta todellakin tapahtuvat yhtä todennäköisesti, nimittäin $1$ ja $8$, $Y$ voi myös saada tiettyjä arvoja eri todennäköisyyksillä kuin $0.25$ näytteistössä. Siksi, vaikka $Y$ onkin satunnaismuuttuja, se ei ole tasajakauma.

Satunnaismuuttujan $Y$ graafinen esitys on annettu *Kuvassa 2*.

*Kuva 2: Satunnaismuuttuja Y*

![Kuva 2: Satunnaismuuttuja Y.](assets/Figure2-2.webp "Kuva 2: Satunnaismuuttuja Y")

Lopullisena esimerkkinä, harkitse satunnaismuuttujaa Z. Sen tulosten joukko on {1,3,7,11,12} ja seuraava todennäköisyysjakauma:

$$
\Pr[Z = 2] = 0.2
$$

$$
\Pr[Z = 3] = 0.2
$$

$$
\Pr[Z = 9] = 0.2
$$

$$
\Pr[Z = 11] = 0.2
$$

$$
\Pr[Z = 12] = 0.2
$$

Voit nähdä sen esitettynä *Kuvassa 3*. Satunnaismuuttuja Z on, toisin kuin Y, tasajakauma, sillä kaikkien mahdollisten arvojen todennäköisyydet näytteistössä ovat yhtä suuret.

*Kuva 3: Satunnaismuuttuja Z*
![Kuva 3: Satunnaismuuttuja Z.](assets/Figure2-3.webp "Kuva 3: Satunnaismuuttuja Z")

### Ehdollinen todennäköisyys

Oletetaan, että Bob aikoo valita tasaisesti jakautuneesti päivän viimeiseltä kalenterivuodelta. Mitä meidän tulisi päätellä todennäköisyydestä, että valittu päivä on kesällä?

Niin kauan kuin ajattelemme Bobin prosessin todella olevan täysin tasainen, meidän tulisi päätellä, että todennäköisyys Bobin valitsemalle päivälle osua kesään on 1/4. Tämä on **ehdoton todennäköisyys** sattumanvaraisesti valitun päivän osumisesta kesään.

Oletetaan nyt, että Bobin sijaan valitsemasta kalenteripäivää tasaisesti, hän valitsee vain tasaisesti niiden päivien joukosta, joina keskipäivän lämpötila Crystal Lakessa (New Jersey) oli 21 astetta Celsius tai korkeampi. Ottaen huomioon tämän lisätiedon, mitä voimme päätellä todennäköisyydestä, että Bob valitsee päivän kesältä?

Meidän tulisi todella tehdä erilainen johtopäätös kuin aiemmin, vaikka meillä ei olisikaan enempää tiettyä tietoa (esim. keskipäivän lämpötila jokaisena päivänä viime kalenterivuonna).

Tietäen, että Crystal Lake sijaitsee New Jerseyssä, emme varmasti odottaisi keskipäivän lämpötilan olevan 21 astetta Celsius tai korkeampi talvella. Sen sijaan on paljon todennäköisempää, että kyseessä olisi lämmin päivä keväällä tai syksyllä, tai päivä jossakin kesän aikana. Siksi tietäen, että keskipäivän lämpötila Crystal Lakessa valittuna päivänä oli 21 astetta Celsius tai korkeampi, todennäköisyys, että Bobin valitsema päivä on kesällä, kasvaa huomattavasti. Tämä on **ehdollinen todennäköisyys** sattumanvaraisesti valitun päivän osumisesta kesään, ottaen huomioon, että keskipäivän lämpötila Crystal Lakessa oli 21 astetta Celsius tai korkeampi.

Toisin kuin edellisessä esimerkissä, kahden tapahtuman todennäköisyydet voivat myös olla täysin riippumattomia. Tässä tapauksessa sanomme, että ne ovat **riippumattomia**.

Oletetaan esimerkiksi, että tietty reilu kolikko on laskeutunut kruunalle. Ottaen huomioon tämän seikan, mikä sitten on todennäköisyys, että huomenna sataa? Ehdollisen todennäköisyyden tässä tapauksessa tulisi olla sama kuin ehdottoman todennäköisyyden, että huomenna sataa, koska kolikon heitto ei yleensä vaikuta säähän.

Käytämme "|" -symbolia kirjoittaessamme ehdollisia todennäköisyyslauseita. Esimerkiksi tapahtuman $A$ todennäköisyys sillä edellytyksellä, että tapahtuma $B$ on tapahtunut, voidaan kirjoittaa seuraavasti:

$$
Pr[A|B]
$$

Joten, kun kaksi tapahtumaa, $A$ ja $B$, ovat riippumattomia, silloin:

$$
Pr[A|B] = Pr[A] \text{ ja } Pr[B|A] = Pr[B]
$$

Riippumattomuuden ehto voidaan yksinkertaistaa seuraavasti:

$$
Pr[A, B] = Pr[A] \cdot Pr[B]
$$

Todennäköisyysteorian keskeinen tulos tunnetaan nimellä **Bayesin teoreema**. Se käytännössä toteaa, että $Pr[A|B]$ voidaan kirjoittaa uudelleen seuraavasti:

$$
Pr[A|B] = \frac{Pr[B|A] \cdot Pr[A]}{Pr[B]}
$$

Ehdollisten todennäköisyyksien käyttämisen sijaan tiettyjen tapahtumien kanssa, voimme myös tarkastella ehdollisia todennäköisyyksiä, jotka liittyvät kahteen tai useampaan satunnaismuuttujaan joukossa mahdollisia tapahtumia. Oletetaan kaksi satunnaismuuttujaa, $X$ ja $Y$. Voimme merkitä minkä tahansa mahdollisen arvon $X$:lle $x$:llä, ja minkä tahansa mahdollisen arvon $Y$:lle $y$:llä. Voisimme sanoa, että kaksi satunnaismuuttujaa ovat riippumattomia, jos seuraava lausunto pitää paikkansa:

$$
Pr[X = x, Y = y] = Pr[X = x] \cdot Pr[Y = y]
$$

kaikille $x$:lle ja $y$:lle.

Olkoon tämä lausunto hieman selkeämmin ilmaistu.
Oletetaan, että tulosten joukot $X$ ja $Y$ on määritelty seuraavasti: **X** = $\{x_1, x_2, \ldots, x_i, \ldots, x_n\}$ ja **Y** = $\{y_1, y_2, \ldots, y_i, \ldots, y_m\}$. (On tyypillistä ilmaista arvojen joukot lihavoituna, isoilla kirjaimilla.)
Kuvittele nyt, että otat näytteen $Y$:stä ja havaitset $y_1$. Edellä oleva lausunto kertoo meille, että todennäköisyys saada nyt $x_1$ otettaessa näyte $X$:stä on täsmälleen sama kuin emme olisi koskaan havainneet $y_1$:tä. Tämä pätee mihin tahansa $y_i$:hin, jonka olisimme voineet vetää alun perin otetusta näytteestä $Y$:stä. Lopuksi, tämä pitää paikkansa ei vain $x_1$:lle. Minkä tahansa $x_i$:n esiintymisen todennäköisyys ei ole vaikuttunut $Y$:n näytteenoton tuloksesta. Kaikki tämä pätee myös tapauksessa, jossa $X$ otetaan näytteeksi ensin.

Lopetetaan keskustelumme hieman filosofisemmalla huomiolla. Missä tahansa todellisessa tilanteessa, jonkin tapahtuman todennäköisyyttä arvioidaan aina tiettyä tietojoukkoa vasten. Ei ole olemassa mitään "ehdotonta todennäköisyyttä" sanan hyvin tiukassa merkityksessä.

Esimerkiksi, jos kysyisin sinulta todennäköisyyttä sille, että siat lentävät vuoteen 2030 mennessä. Vaikka en anna sinulle lisätietoja, tiedät selvästi paljon maailmasta, joka voi vaikuttaa arvioosi. Et ole koskaan nähnyt sikoja lentävän. Tiedät, että useimmat ihmiset eivät odota niiden lentävän. Tiedät, että ne eivät ole oikeastaan rakennettu lentämään. Ja niin edelleen.

Siksi, kun puhumme jonkin tapahtuman "ehdottomasta todennäköisyydestä" todellisessa maailman kontekstissa, tuo termi voi todella saada merkityksen vain, jos otamme sen tarkoittavan jotakin sellaista kuin "todennäköisyys ilman mitään lisätietoja". Mikä tahansa "ehdollisen todennäköisyyden" ymmärtäminen pitäisi sitten aina ymmärtää jotakin tiettyä tietoa vasten.

Voisin esimerkiksi kysyä sinulta todennäköisyyttä sille, että siat lentävät vuoteen 2030 mennessä, annettuani sinulle todisteita siitä, että jotkut Uuden-Seelannin vuohet ovat oppineet lentämään muutaman vuoden koulutuksen jälkeen. Tässä tapauksessa todennäköisesti säätäisit arviotasi siitä, että siat lentävät vuoteen 2030 mennessä. Joten todennäköisyys, että siat lentävät vuoteen 2030 mennessä, on ehdollinen tälle todisteelle vuohista Uudessa-Seelannissa.

## Modulo-operaatio
<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>

### Modulo

Yksinkertaisin ilmaisu **modulo-operaatiolle** on seuraavanlainen: $x \mod y$.

Muuttujaa $x$ kutsutaan jakolausekkeeksi ja muuttujaa $y$ jakajaksi. Suorittaaksesi modulo-operaation positiivisella jakolausekkeella ja positiivisella jakajalla, määrität vain jakolaskun jäännöksen.

Esimerkiksi, harkitse ilmaisua $25 \mod 4$. Luku 4 menee lukuun 25 yhteensä 6 kertaa. Jakolaskun jäännös on 1. Siksi $25 \mod 4$ on yhtä kuin 1. Samalla tavalla voimme arvioida alla olevat ilmaisut:

* $29 \mod 30 = 29$ (koska 30 menee 29:ään yhteensä 0 kertaa ja jäännös on 29)
* $42 \mod 2 = 0$ (koska 2 menee 42:een yhteensä 21 kertaa ja jäännös on 0)
* $12 \mod 5 = 2$ (koska 5 menee 12:een yhteensä 2 kertaa ja jäännös on 2)
* $20 \mod 8 = 4$ (koska 8 menee 20:een yhteensä 2 kertaa ja jäännös on 4)

Kun jakaja tai jaettava on negatiivinen, modulo-operaatioita voidaan käsitellä eri tavoin ohjelmointikielissä.

Kryptografiassa tulee varmasti vastaan tapauksia, joissa jaettava on negatiivinen. Näissä tapauksissa tyypillinen lähestymistapa on seuraava:

* Määritä ensin lähin arvo *pienempi tai yhtä suuri kuin* jaettava, johon jakaja jakautuu jäännöksettä. Kutsutaan tätä arvoa $p$:ksi.
* Jos jaettava on $x$, niin modulo-operaation tulos on arvon $x – p$ arvo.

Esimerkiksi, oletetaan että jaettava on $–20$ ja jakaja 3. Lähin arvo pienempi tai yhtä suuri kuin $–20$, johon 3 jakautuu tasaisesti, on $–21$. Arvon $x – p$ arvo tässä tapauksessa on $–20 – (–21)$. Tämä on yhtä kuin 1 ja siis $–20 \mod 3$ on yhtä kuin 1. Samalla tavalla voimme arvioida seuraavat lausekkeet:

* $–8 \mod 5 = 2$
* $–19 \mod 16 = 13$
* $–14 \mod 6 = 4$

Notaatiossa näet tyypillisesti seuraavanlaisia ilmaisuja: $x = [y \mod z]$. Hakasulkujen vuoksi modulo-operaatio tässä tapauksessa koskee vain lausekkeen oikeaa puolta. Jos esimerkiksi $y$ on 25 ja $z$ on 4, niin $x$ arvoksi saadaan 1.

Ilman hakasulkuja modulo-operaatio vaikuttaa *molempiin* lausekkeen osiin. Oletetaan esimerkiksi seuraava lauseke: $x = y \mod z$. Jos $y$ on 25 ja $z$ on 4, niin tiedämme vain, että $x \mod 4$ arvoksi saadaan 1. Tämä on yhdenmukaista minkä tahansa arvon kanssa joukosta $\{\ldots,–7, –3, 1, 5, 9,\ldots\}$.

Matematiikan haara, joka sisältää modulo-operaatioita numeroilla ja lausekkeilla, viitataan **modulaariaritmetiikkana**. Voit ajatella tätä haaraa aritmetiikkana tapauksissa, joissa lukusuora ei ole äärettömän pitkä. Vaikka tyypillisesti kohtaamme modulo-operaatioita (positiivisille) kokonaisluvuille kryptografiassa, voit suorittaa modulo-operaatioita myös millä tahansa reaaliluvuilla.

### Siirtosala

Modulo-operaatio on usein kohdattu kryptografiassa. Havainnollistaaksemme, tarkastellaan yhtä kuuluisimmista historiallisista salausjärjestelmistä: siirtosalaa.

Määritellään se ensin. Oletetaan sanakirja *D*, joka yhdistää kaikki englannin aakkosten kirjaimet, järjestyksessä, numeroiden joukkoon $\{0, 1, 2, \ldots, 25\}$. Oletetaan viestitila **M**. **Siirtosala** on sitten salausjärjestelmä, joka on määritelty seuraavasti:

- Valitse tasaisesti avain $k$ avainavaruudesta **K**, missä **K** = $\{0, 1, 2, \ldots, 25\}$ [1]
- Salaa viesti $m \in \mathbf{M}$ seuraavasti:
    - Jaa $m$ sen yksittäisiin kirjaimiin $m_0, m_1, \ldots, m_i, \ldots, m_l$
- Muunna jokainen $m_i$ numeroksi *D*:n mukaan
    - Jokaiselle $m_i$:lle, $c_i = [(m_i + k) \mod 26]$
    - Muunna jokainen $c_i$ kirjaimeksi *D*:n mukaan
    - Yhdistä sitten $c_0, c_1, \ldots, c_l$ saadaksesi salatun viestin $c$
- Purkaa salattu viesti $c$ seuraavasti:
    - Muunna jokainen $c_i$ numeroksi *D*:n mukaan
    - Jokaiselle $c_i$:lle, $m_i = [(c_i – k) \mod 26]$
    - Muunna jokainen $m_i$ kirjaimeksi *D*:n mukaan
    - Yhdistä sitten $m_0, m_1, \ldots, m_l$ saadaksesi alkuperäisen viestin $m$

Modulo-operaattori siirtosalauksessa varmistaa, että kirjaimet kiertävät, jotta kaikki salatut kirjaimet määritellään. Esimerkiksi, harkitse siirtosalauksen soveltamista sanaan “DOG”.

Oletetaan, että olet valinnut avaimen arvoksi 17. Kirjain “O” vastaa 15:tä. Ilman modulo-operaatiota, tämän alkuperäisen numeron ja avaimen summa olisi salatun viestin numero 32. Kuitenkaan tätä salattua viestin numeroa ei voisi muuntaa salatuksi kirjaimeksi, koska englannin aakkostossa on vain 26 kirjainta. Modulo-operaatio varmistaa, että salatun viestin numero on itse asiassa 6 (tuloksena $32 \mod 26$), mikä vastaa salattua kirjainta “G”.

Koko sanan “DOG” salaaminen avaimen arvolla 17 on seuraava:

* Viesti = DOG = D,O,G = 3,15,6
* $c_0 = [(3 + 17) \mod 26] = [(20) \mod 26] = 20 = U$
* $c_1 = [(15 + 17) \mod 26] = [(32) \mod 26] = 6 = G$
* $c_2 = [(6 + 17) \mod 26] = [(23) \mod 26] = 23 = X$
* $c = UGX$

Jokainen voi intuitiivisesti ymmärtää, miten siirtosalakirjoitus toimii ja todennäköisesti käyttää sitä itse. Kryptografian tiedon syventämiseksi on kuitenkin tärkeää alkaa tulla mukavammaksi formalisoinnin kanssa, koska järjestelmät muuttuvat paljon vaikeammiksi. Siksi siirtosalakirjoituksen vaiheet formalisoitiin.

**Huomautuksia:**

[1] Voimme määritellä tämän lausunnon tarkasti, käyttäen edellisestä osiosta terminologiaa. Olkoon yhtenäinen muuttuja $K$ sillä $K$ on sen mahdollisten tulosten joukko. Joten:

$$
Pr[K = 0] = \frac{1}{26}
$$

$$
Pr[K = 1] = \frac{1}{26}
$$

...ja niin edelleen. Näytä yhtenäinen muuttuja $K$ kerran saadaksesi tietyn avaimen.

## XOR-operaatio
<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>

Kaikki tietokoneiden tiedot käsitellään, tallennetaan ja lähetetään verkkojen yli bittitasolla. Kaikki tietokoneiden tietoihin sovelletut kryptografiset järjestelmät toimivat myös bittitasolla.

Esimerkiksi, oletetaan että olet kirjoittanut sähköpostiviestin sähköpostisovellukseesi. Kaikki soveltamasi salaaminen ei tapahdu suoraan sähköpostisi ASCII-merkeissä. Sen sijaan se sovelletaan kirjainten ja muiden symbolien bittiesitykseen sähköpostissasi.
Nykyisen kryptografian ymmärtämisen kannalta keskeinen matemaattinen operaatio modulo-operaation lisäksi on **XOR-operaatio**, tai "yksinomainen tai" -operaatio. Tämä operaatio ottaa syötteiksi kaksi bittiä ja tuottaa tulokseksi toisen bitin. XOR-operaatio merkitään yksinkertaisesti "XOR". Se tuottaa 0, jos kaksi bittiä ovat samat ja 1, jos kaksi bittiä ovat erilaiset. Alla näet neljä mahdollisuutta. Symboli $\oplus$ edustaa "XOR":
* $0 \oplus 0 = 0$
* $0 \oplus 1 = 1$
* $1 \oplus 0 = 1$
* $1 \oplus 1 = 0$

Kuvitellaan esimerkiksi, että sinulla on viesti $m_1$ (01111001) ja viesti $m_2$ (01011001). Näiden kahden viestin XOR-operaatio näkyy alla.

* $m_1 \oplus m_2 = 01111001 \oplus 01011001 = 00100000$

Prosessi on suoraviivainen. Ensin suoritat XOR-operaation $m_1$:n ja $m_2$:n vasemmanpuoleisimmille biteille. Tässä tapauksessa se on $0 \oplus 0 = 0$. Sitten suoritat XOR-operaation toiselle parille biteistä vasemmalta. Tässä tapauksessa se on $1 \oplus 1 = 0$. Jatkat tätä prosessia, kunnes olet suorittanut XOR-operaation oikeanpuoleisimmille biteille.

On helppo nähdä, että XOR-operaatio on kommutatiivinen, eli $m_1 \oplus m_2 = m_2 \oplus m_1$. Lisäksi XOR-operaatio on myös assosiatiivinen. Eli, $(m_1 \oplus m_2) \oplus m_3 = m_1 \oplus (m_2 \oplus m_3)$.

XOR-operaatio kahdelle eri pituiselle merkkijonolle voi saada erilaisia tulkintoja riippuen kontekstista. Emme tässä yhteydessä käsittele eri pituisten merkkijonojen XOR-operaatioita.

XOR-operaatio on yhtä kuin erikoistapaus modulo-operaation suorittamisesta bittien summalle, kun jakaja on 2. Voit nähdä yhtäläisyyden seuraavissa tuloksissa:

* $(0 + 0) \mod 2 = 0 \oplus 0 = 0$
* $(1 + 0) \mod 2 = 1 \oplus 0 = 1$
* $(0 + 1) \mod 2 = 0 \oplus 1 = 1$
* $(1 + 1) \mod 2 = 1 \oplus 1 = 0$

## Pseudosatunnaisuus
<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>

Keskustellessamme satunnaisista ja tasajakaumaisista muuttujista, teimme tietyn eron "satunnaisen" ja "tasajakaumaisen" välillä. Käytännössä tämä ero yleensä säilytetään kuvaamaan satunnaismuuttujia. Kuitenkin nykyisessä kontekstissamme tämä ero on hylättävä ja "satunnainen" sekä "tasajakaumainen" käytetään synonyymeinä. Selitän miksi osion lopussa.

Aloitetaan, voimme kutsua binääristä merkkijonoa pituudeltaan $n$ **satunnaiseksi** (tai **tasajakaumaiseksi**), jos se oli tulosta tasajakaumaisen muuttujan $S$ näytteestä, joka antaa jokaiselle tällaisen pituuden $n$ binääriselle merkkijonolle yhtä suuren todennäköisyyden valikoitua.
Kuvitellaan esimerkiksi kaikkien 8-bittisten binäärijonojen joukko: $\{0000\ 0000, 0000\ 0001, \ldots, 1111\ 1111\}$. (On tyypillistä kirjoittaa 8-bittinen jono kahtena nelikon ryhmänä, joista kumpaakin kutsutaan **nibbleksi**.) Kutsutaan tätä jonoryhmää **$S_8$**:ksi.
Määritelmän mukaan voimme sitten kutsua tiettyä 8-bittistä binäärijonoa satunnaiseksi (tai tasajakaumaiseksi), jos se on valittu tasajakaumaisen muuttujan $S$ tuloksena, joka antaa jokaiselle jonolle ryhmässä **$S_8$** yhtä suuren valintatodennäköisyyden. Ottaen huomioon, että joukko **$S_8$** sisältää $2^8$ elementtiä, valinnan todennäköisyyden näytteistössä tulisi olla $1/2^8$ jokaiselle jonolle joukossa.

Binäärijonon satunnaisuuden keskeinen näkökohta on, että se määritellään viittaamalla prosessiin, jonka kautta se on valittu. Tietyn binäärijonon muoto itsessään ei siis paljasta mitään sen satunnaisuudesta valinnassa.

Esimerkiksi monet ihmiset intuitiivisesti ajattelevat, että jono kuten $1111\ 1111$ ei olisi voitu valita satunnaisesti. Mutta tämä on selvästi väärin.

Määriteltäessä tasajakaumainen muuttuja $S$ kaikille 8-bittisille binäärijonoille, jonon $1111\ 1111$ valitseminen joukosta **$S_8$** on yhtä todennäköistä kuin jonon kuten $0111\ 0100$ valitseminen. Näin ollen et voi päätellä mitään jonon satunnaisuudesta pelkästään analysoimalla jonoa itseään.

Voimme myös puhua satunnaisista jonoista ilman, että tarkoitamme nimenomaan binäärijonoja. Saatamme esimerkiksi puhua satunnaisesta heksajonosta $AF\ 02\ 82$. Tässä tapauksessa jono olisi valittu satunnaisesti kaikkien 6-merkkisten heksajonojen joukosta. Tämä vastaa 24-bittisen binäärijonon satunnaista valintaa, sillä jokainen heksamerkki edustaa 4 bittiä.

Tyypillisesti ilmaisu “satunnainen jono”, ilman tarkennusta, viittaa jonoon, joka on satunnaisesti valittu kaikkien saman pituisten jonoiden joukosta. Näin olen kuvaillut sitä yllä. Jonon pituus $n$ voi tietysti myös olla satunnaisesti valittu eri joukosta. Yksi, esimerkiksi, joka muodostuu vain osajoukosta kaikista $n$ pituisten jonoiden joukosta, tai ehkä joukosta, joka sisältää eri pituisia jonoja. Näissä tapauksissa emme kuitenkaan viittaisi siihen “satunnaisena jonona”, vaan pikemminkin “jonona, joka on satunnaisesti valittu jostakin joukosta **S**”.

Keskeinen käsite kryptografiassa on pseudosatunnaisuus. **Pseudosatunnainen jono** pituudeltaan $n$ näyttää *siltä kuin* se olisi valittu tasajakaumaisen muuttujan $S$ tuloksena, joka antaa jokaiselle jonolle joukossa **$S_n$** yhtä suuren valintatodennäköisyyden. Itse asiassa kuitenkin jono on valittu tasajakaumaisen muuttujan $S'$ tuloksena, joka määrittelee vain todennäköisyysjakauman – ei välttämättä sellaisen, jossa kaikilla mahdollisilla tuloksilla on yhtä suuri todennäköisyys – osajoukolle **$S_n$**:sta. Ratkaiseva seikka tässä on, että kukaan ei todellisuudessa voi erottaa näytteitä $S$:stä ja $S'$:stä, vaikka ottaisit niitä monta.
Oletetaan esimerkiksi satunnaismuuttuja $S$. Sen tulosten joukko on **$S_{256}$**, eli kaikkien 256-bittisten binäärijonojen joukko. Tällä joukolla on $2^{256}$ elementtiä. Jokaisella elementillä on yhtä suuri todennäköisyys tulla valituksi, $1/2^{256}$, otannassa.
Lisäksi oletetaan satunnaismuuttuja $S'$. Sen tulosten joukko sisältää vain $2^{128}$ 256-bittistä binäärijonoa. Sillä on jokin todennäköisyysjakauma näiden jonojen yli, mutta tämä jakauma ei välttämättä ole tasainen.

Oletetaan, että otan nyt 1000 otosta $S$:stä ja 1000 otosta $S'$:stä ja annan sinulle molemmat tulosten joukot. Kerron sinulle, kumpi tulosten joukko liittyy kumpaan satunnaismuuttujaan. Seuraavaksi otan näytteen jommasta kummasta kahdesta satunnaismuuttujasta. Mutta tällä kertaa en kerro sinulle, kummasta satunnaismuuttujasta otoksen otan. Jos $S'$ olisi pseudosatunnainen, ajatuksena on, että todennäköisyytesi arvata oikein, kummasta satunnaismuuttujasta otoksen otin, on käytännössä tuskin parempi kuin $1/2$.

Tyypillisesti pseudosatunnainen jono pituudeltaan $n$ tuotetaan valitsemalla satunnaisesti jono kooltaan $n – x$, missä $x$ on positiivinen kokonaisluku, ja käyttämällä sitä laajentavan algoritmin syötteenä. Tämä satunnainen jono kooltaan $n – x$ tunnetaan nimellä **siemen**.

Pseudosatunnaiset jonot ovat keskeinen käsite kryptografian käytännöllisyyden kannalta. Harkitse esimerkiksi virtasalauksia. Virtasalauksessa satunnaisesti valittu avain syötetään laajentavaan algoritmiin tuottamaan paljon suurempi pseudosatunnainen jono. Tämä pseudosatunnainen jono yhdistetään sitten avoimen tekstin kanssa XOR-operaatiolla tuottamaan salateksti.

Jos emme pystyisi tuottamaan tällaista pseudosatunnaista jonoa virtasalaukselle, tarvitsisimme avaimen, joka on yhtä pitkä kuin viesti sen turvallisuuden takaamiseksi. Tämä ei ole kovin käytännöllinen vaihtoehto useimmissa tapauksissa.

Tässä osiossa käsitelty pseudosatunnaisuuden käsite voidaan määritellä muodollisemmin. Se ulottuu myös muihin yhteyksiin. Mutta meidän ei tarvitse syventyä tähän keskusteluun tässä. Kaiken, mitä sinun todella tarvitsee intuitiivisesti ymmärtää suurimmasta osasta kryptografiaa, on ero satunnaisen ja pseudosatunnaisen jonon välillä. [2]

Syy siihen, miksi hylkäämme eron "satunnaisen" ja "tasaisen" välillä keskustelussamme, pitäisi nyt myös olla selvä. Käytännössä kaikki käyttävät termiä pseudosatunnainen osoittamaan jonoa, joka vaikuttaa **kuin** se olisi tulosta tasaisen muuttujan $S$ otannasta. Tarkkaan ottaen meidän pitäisi kutsua tällaista jonoa "pseudo-tasaiseksi", ottaen käyttöön aiemman kielenkäyttömme. Koska termi "pseudo-tasainen" on sekä kömpelö että kenenkään käyttämätön, emme ota sitä käyttöön tässä selkeyden vuoksi. Sen sijaan jätämme vain eron "satunnaisen" ja "tasaisen" välillä nykyisessä kontekstissa.

**Huomautukset**

[2] Jos olet kiinnostunut tutustumaan näihin asioihin muodollisemmin, voit konsultoida Katz ja Lindellin teosta *Introduction to Modern Cryptography*, erityisesti luku 3.


# Kryptografian matemaattiset perusteet 2
<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>




## Mikä on lukuteoria?
<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>
Tämä luku käsittelee edistyneempää aihetta kryptografian matemaattisissa perusteissa: lukuteoriaa. Vaikka lukuteoria on tärkeä symmetrisessä kryptografiassa (kuten Rijndael-salauksessa), se on erityisen tärkeää julkisen avaimen kryptografisessa ympäristössä.
Jos lukuteorian yksityiskohdat tuntuvat sinusta hankalilta, suosittelen ensimmäisellä kerralla korkean tason lukemista. Voit aina palata siihen myöhemmin.

___

Voit kuvailla **lukuteoriaa** tutkimuksena kokonaislukujen ominaisuuksista ja matemaattisista funktioista, jotka toimivat kokonaislukujen kanssa.

Harkitse esimerkiksi, että mitkä tahansa kaksi lukua $a$ ja $N$ ovat **keskenään jaottomia** (tai **suhteellisia alkulukuja**), jos niiden suurin yhteinen tekijä on 1. Oletetaan nyt tietty kokonaisluku $N$. Kuinka monta kokonaislukua, jotka ovat pienempiä kuin $N$, ovat keskenään jaottomia $N$:n kanssa? Voimmeko tehdä yleisiä lausuntoja tämän kysymyksen vastauksista? Nämä ovat tyypillisiä kysymyksiä, joihin lukuteoria pyrkii vastaamaan.

Nykyajan lukuteoria nojaa abstraktin algebran työkaluihin. **Abstrakti algebra** on matematiikan aladisipliini, jonka pääanalyysikohteet ovat abstrakteja objekteja, joita kutsutaan algebrallisiksi rakenteiksi. **Algebrallinen rakenne** on elementtien joukko, joka on yhdistetty yhden tai useamman operaation kanssa, ja joka täyttää tietyt aksioomat. Algebrallisten rakenteiden kautta matemaatikot voivat saada oivalluksia tiettyihin matemaattisiin ongelmiin abstrahoimalla pois niiden yksityiskohdista.

Abstraktin algebran alaa kutsutaan joskus myös moderniksi algebraksi. Saatat myös törmätä käsitteeseen **abstrakti matematiikka** (tai **puhdas matematiikka**). Tämä jälkimmäinen termi ei viittaa abstraktiin algebraan, vaan tarkoittaa matematiikan tutkimista sen itsensä vuoksi, ei vain potentiaalisten sovellusten näkökulmasta.

Abstraktin algebran joukot voivat käsitellä monenlaisia objekteja, tasasivuisen kolmion muotoa säilyttävistä muunnoksista tapettikuvioihin. Lukuteorialle me tarkastelemme vain joukkoja, jotka sisältävät kokonaislukuja tai funktioita, jotka toimivat kokonaislukujen kanssa.

## Ryhmät
<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>

Peruskäsite matematiikassa on elementtien joukko. Joukko merkitään yleensä aaltosulkeilla, ja elementit erotetaan toisistaan pilkuilla.

Esimerkiksi kaikkien kokonaislukujen joukko on $\{…, -2, -1, 0, 1, 2, …\}$. Ellipsit tässä tarkoittavat, että tietty kuvio jatkuu tietyssä suunnassa. Joten kaikkien kokonaislukujen joukko sisältää myös $3, 4, 5, 6$ ja niin edelleen, sekä $-3, -4, -5, -6$ ja niin edelleen. Tätä kaikkien kokonaislukujen joukkoa merkitään yleensä $\mathbb{Z}$:llä.

Toinen esimerkki joukosta on $\mathbb{Z} \mod 11$, eli kaikkien kokonaislukujen modulo 11 joukko. Toisin kuin koko joukko $\mathbb{Z}$, tämä joukko sisältää vain rajallisen määrän elementtejä, nimittäin $\{0, 1, \ldots, 9, 10\}$.
Yleinen virhe on ajatella, että joukko $\mathbb{Z} \mod 11$ on itse asiassa $\{-10, -9, \ldots, 0, \ldots, 9, 10\}$. Mutta näin ei ole, ottaen huomioon aiemmin määrittelemämme modulo-operaation tavan. Kaikki negatiiviset kokonaisluvut, jotka on pienennetty modulo 11 mukaan, kääriytyvät joukkoon $\{0, 1, \ldots, 9, 10\}$. Esimerkiksi lauseke $-2 \mod 11$ kääriytyy arvoon $9$, kun taas lauseke $-27 \mod 11$ kääriytyy arvoon $5$.
Toinen peruskäsite matematiikassa on binäärinen operaatio. Tämä on mikä tahansa operaatio, joka ottaa kaksi alkiota tuottaakseen kolmannen. Esimerkiksi perusaritmetiikasta ja algebrasta tuttuja neljää perusbinäärioperaatiota ovat yhteenlasku, vähennyslasku, kertolasku ja jakolasku.

Nämä kaksi perusmatemaattista käsitettä, joukot ja binäärioperaatiot, käytetään abstraktin algebran keskeisimmän rakenteen, ryhmän, määrittelemiseen.

Erityisesti, oletetaan jonkin binäärioperaation $\circ$. Lisäksi, oletetaan jonkin alkioiden joukko **S**, joka on varustettu kyseisellä operaatiolla. Kaikki mitä “varustettu” tässä tarkoittaa, on että operaatio $\circ$ voidaan suorittaa minkä tahansa kahden joukon **S** alkion välillä.

Yhdistelmä $\langle \mathbf{S}, \circ \rangle$ on sitten **ryhmä**, jos se täyttää neljä tiettyä ehtoa, jotka tunnetaan ryhmäaksioomina.

1. Mille tahansa $a$:lle ja $b$:lle, jotka ovat alkiota joukossa $\mathbf{S}$, $a \circ b$ on myös alkiota joukossa $\mathbf{S}$. Tätä kutsutaan **sulkeutumisehdoiksi**.
2. Mille tahansa $a$:lle, $b$:lle ja $c$:lle, jotka ovat alkiota joukossa $\mathbf{S}$, pätee, että $(a \circ b) \circ c = a \circ (b \circ c)$. Tätä kutsutaan **assosiatiivisuusehdoiksi**.
3. Joukossa $\mathbf{S}$ on yksikäsitteinen alkio $e$, siten, että jokaiselle alkiolle $a$ joukossa $\mathbf{S}$ pätee seuraava yhtälö: $e \circ a = a \circ e = a$. Koska tällainen alkio $e$ on vain yksi, sitä kutsutaan **identiteettialkioksi**. Tätä ehtoa kutsutaan **identiteettiehdoiksi**.
4. Jokaiselle alkiolle $a$ joukossa $\mathbf{S}$ on olemassa alkio $b$ joukossa $\mathbf{S}$, siten, että seuraava yhtälö pätee: $a \circ b = b \circ a = e$, missä $e$ on identiteettialkio. Alkiota $b$ tässä kutsutaan **käänteisalkioksi**, ja sitä merkitään yleisesti $a^{-1}$. Tätä ehtoa kutsutaan **käänteisehdoiksi** tai **kääntyvyys-ehdoksi**.

Tutkitaan ryhmiä hieman lisää. Merkitään kaikkien kokonaislukujen joukkoa $\mathbb{Z}$. Tämä joukko yhdistettynä standardiin yhteenlaskuun, eli $\langle \mathbb{Z}, + \rangle$, sopii selvästi ryhmän määritelmään, sillä se täyttää yllä mainitut neljä aksiomia.

1. Mille tahansa $x$:lle ja $y$:lle, jotka ovat alkiota joukossa $\mathbb{Z}$, $x + y$ on myös alkiota joukossa $\mathbb{Z}$. Joten $\langle \mathbb{Z}, + \rangle$ täyttää sulkeutumisehdon.
2. Kaikille $x$, $y$ ja $z$, jotka ovat joukon $\mathbb{Z}$ alkioita, pätee $(x + y) + z = x + (y + z)$. Joten $\langle \mathbb{Z}, + \rangle$ täyttää assosiatiivisuusehdon.

3. Joukossa $\langle \mathbb{Z}, + \rangle$ on neutraalialkio, nimittäin 0. Mille tahansa $x$:lle joukossa $\mathbb{Z}$ pätee, että: $0 + x = x + 0 = x$. Joten $\langle \mathbb{Z}, + \rangle$ täyttää neutraalialkion ehdon.

4. Lopuksi, jokaiselle alkiolle $x$ joukossa $\mathbb{Z}$, löytyy $y$ siten, että $x + y = y + x = 0$. Jos $x$ olisi 10, esimerkiksi, $y$ olisi $-10$ (jos $x$ on 0, $y$ on myös 0). Joten $\langle \mathbb{Z}, + \rangle$ täyttää käänteisalkion ehdon.

Tärkeää on, että kokonaislukujen joukko yhteenlaskun kanssa muodostaa ryhmän, mutta se ei tarkoita, että se muodostaisi ryhmän kertolaskun kanssa. Voit varmistaa tämän testaamalla $\langle \mathbb{Z}, \cdot \rangle$ neljää ryhmäaksioomaa vasten (missä $\cdot$ tarkoittaa tavallista kertolaskua).

Ensimmäiset kaksi aksiomia pätevät ilmeisesti. Lisäksi kertolaskussa alkio 1 toimii neutraalialkiona. Mikä tahansa kokonaisluku $x$ kerrottuna 1:llä tuottaa nimittäin $x$. Kuitenkaan $\langle \mathbb{Z}, \cdot \rangle$ ei täytä käänteisalkion ehtoa. Eli ei ole olemassa yksikäsitteistä alkiota $y$ joukossa $\mathbb{Z}$ jokaiselle $x$:lle joukossa $\mathbb{Z}$, siten että $x \cdot y = 1$.

Oletetaan esimerkiksi, että $x = 22$. Mikä arvo $y$ joukosta $\mathbb{Z}$ kerrottuna $x$:llä tuottaisi neutraalialkion 1? Arvo $1/22$ toimisi, mutta se ei ole joukon $\mathbb{Z}$ alkioiden joukossa. Itse asiassa kohtaat tämän ongelman minkä tahansa kokonaisluvun $x$ kanssa, paitsi arvojen 1 ja -1 kohdalla (missä $y$:n tulisi olla 1 ja -1 vastaavasti).

Jos sallisimme reaaliluvut joukkoomme, ongelmamme suurelta osin katoaisivat. Mille tahansa alkiolle $x$ joukossa, kertominen $1/x$:llä tuottaa 1. Koska murtoluvut sisältyvät reaalilukujen joukkoon, käänteisalkio löytyy jokaiselle reaaliluvulle. Poikkeus on nolla, sillä mikään kertominen nollalla ei koskaan tuota neutraalialkiota 1. Siksi nollasta poikkeavien reaalilukujen joukko varustettuna kertolaskulla on todellakin ryhmä.

Jotkut ryhmät täyttävät viidennen yleisen ehdon, joka tunnetaan **kommutatiivisuusehtona**. Tämä ehto on seuraava:

* Oletetaan ryhmä $G$ joukolla **S** ja binäärioperaattorilla $\circ$. Oletetaan, että $a$ ja $b$ ovat joukon **S** alkioita. Jos on niin, että $a \circ b = b \circ a$ mille tahansa kahdelle alkiolle $a$ ja $b$ joukossa **S**, silloin $G$ täyttää kommutatiivisuusehdon.
Ryhmää, joka täyttää vaihdannaisuusehdon, kutsutaan **kommutatiiviseksi ryhmäksi** tai **Abelin ryhmäksi** (Niels Henrik Abelin mukaan). On helppo todentaa, että sekä reaalilukujen joukko yhteenlaskun suhteen että kokonaislukujen joukko yhteenlaskun suhteen ovat Abelin ryhmiä. Kokonaislukujen joukko kertolaskun suhteen ei ole lainkaan ryhmä, joten se ei voi olla Abelin ryhmä. Sen sijaan nollasta poikkeavien reaalilukujen joukko kertolaskun suhteen on myös Abelin ryhmä.

Sinun tulisi kiinnittää huomiota kahteen tärkeään notaatiota koskevaan konventioon. Ensinnäkin merkkejä “+” tai “×” käytetään usein kuvaamaan ryhmäoperaatioita, vaikka elementit eivät tosiasiassa olisikaan numeroita. Näissä tapauksissa sinun ei tulisi tulkita näitä merkkejä standardin aritmeettisen yhteen- tai kertolaskun mukaisesti. Sen sijaan ne ovat operaatioita, joilla on vain abstrakti yhtäläisyys näiden aritmeettisten operaatioiden kanssa.

Ellet erityisesti viittaa aritmeettiseen yhteen- tai kertolaskuun, on helpompaa käyttää symboleja kuten $\circ$ ja $\diamond$ ryhmäoperaatioihin, sillä näillä ei ole kulttuurisesti syvään juurtuneita merkityksiä.

Toiseksi, samasta syystä kuin “+” ja “×” ovat usein käytössä ei-aritmeettisten operaatioiden ilmaisemiseen, ryhmien identiteettialkiot symbolisoidaan usein “0”:lla ja “1”:llä, vaikka näiden ryhmien elementit eivät olisi numeroita. Ellet viittaa ryhmän identiteettialkioon, jossa on numeroita, on helpompaa käyttää neutraalimpaa symbolia kuten “$e$” identiteettialkion ilmaisemiseen.

Monet erilaiset ja erittäin tärkeät arvojoukot matematiikassa, jotka on varustettu tietyillä binäärioperaatioilla, ovat ryhmiä. Kryptografiset sovellukset toimivat kuitenkin vain kokonaislukujen joukoilla tai ainakin elementeillä, jotka kuvataan kokonaisluvuilla, eli lukuteorian alueella. Siksi reaalilukujen joukkoja, jotka eivät ole kokonaislukuja, ei käytetä kryptografisissa sovelluksissa.

Lopetetaan antamalla esimerkki elementeistä, jotka voidaan “kuvailla kokonaisluvuilla”, vaikka ne eivät olekaan kokonaislukuja. Hyvä esimerkki on elliptisten käyrien pisteet. Vaikka mikään elliptisen käyrän piste ei selvästikään ole kokonaisluku, sellainen piste kuvataan todellakin kahdella kokonaisluvulla.

Elliptiset käyrät ovat esimerkiksi olennaisen tärkeitä Bitcoinille. Mikä tahansa standardi Bitcoinin yksityinen ja julkinen avainpari valitaan pisteiden joukosta, joka määritellään seuraavalla elliptisellä käyrällä:

$$
x^3 + 7 = y^2 \mod 2^{256} – 2^{32} – 29 – 28 – 27 – 26 - 24 - 1
$$

(suurin alkuluku, joka on pienempi kuin $2^{256}$). $x$-koordinaatti on yksityinen avain ja $y$-koordinaatti on julkinen avain.

Bitcoin-siirrot tyypillisesti sisältävät lukituksia yhteen tai useampaan julkiseen avaimiin jollakin tavalla. Näiden siirtojen arvo voidaan sitten vapauttaa tekemällä digitaalisia allekirjoituksia vastaavilla yksityisillä avaimilla.

## Sykliset ryhmät
<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>

Yksi merkittävä ero, jonka voimme tehdä, on **äärellisen** ja **äärettömän ryhmän** välillä. Edellisellä on äärellinen määrä elementtejä, kun taas jälkimmäisellä on ääretön määrä elementtejä. Mikä tahansa äärellisen ryhmän elementtien määrä tunnetaan ryhmän **järjestyksenä**. Kaikki käytännön kryptografia, joka sisältää ryhmien käytön, perustuu äärellisiin (lukuteoreettisiin) ryhmiin.

Julkisen avaimen kryptografiassa tietty luokka äärellisiä Abelin ryhmiä, tunnettuina syklisinä ryhminä, on erityisen tärkeä. Jotta ymmärtäisimme sykliset ryhmät, meidän ensin täytyy ymmärtää ryhmäelementtien eksponentiaation käsite.
Oletetaan ryhmä $G$ ryhmäoperaatiolla $\circ$, ja että $a$ on elementti ryhmässä $G$. Ilmaisu $a^n$ tulisi tällöin tulkita elementtinä $a$ yhdistettynä itsensä kanssa yhteensä $n – 1$ kertaa. Esimerkiksi, $a^2$ tarkoittaa $a \circ a$, $a^3$ tarkoittaa $a \circ a \circ a$, ja niin edelleen. (Huomaa, että eksponentiaatio tässä ei välttämättä ole eksponentiaatio tavallisessa aritmeettisessa mielessä.)

Käännymme esimerkin puoleen. Oletetaan, että $G = \langle \mathbb{Z} \mod 7, + \rangle$, ja että arvomme $a$ on 4. Tässä tapauksessa, $a^2 = [4 + 4 \mod 7] = [8 \mod 7] = 1 \mod 7$. Vaihtoehtoisesti, $a^4$ edustaisi $[4 + 4 + 4 + 4 \mod 7] = [16 \mod 7] = 2 \mod 7$.

Jotkut Abelian-ryhmät sisältävät yhden tai useamman elementin, jotka voivat tuottaa kaikki muut ryhmän elementit jatkuvan eksponentiaation kautta. Näitä elementtejä kutsutaan **generaattoreiksi** tai **primitiivielementeiksi**.

Tärkeä luokka tällaisia ryhmiä on $\langle \mathbb{Z}^* \mod N, \cdot \rangle$, missä $N$ on alkuluku. Notaatio $\mathbb{Z}^*$ tässä tarkoittaa, että ryhmä sisältää kaikki nollasta poikkeavat, positiiviset kokonaisluvut, jotka ovat pienempiä kuin $N$. Tällainen ryhmä sisältää siis aina $N – 1$ elementtiä.

Harkitse esimerkiksi $G = \langle \mathbb{Z}^* \mod 11, \cdot \rangle$. Tällä ryhmällä on seuraavat elementit: $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. Tämän ryhmän järjestys on 10 (mikä todellakin on yhtä suuri kuin $11 – 1$).

Tutkitaan elementin 2 eksponentiaatiota tästä ryhmästä. Laskelmat aina $2^{12}$ asti on näytetty alla. Huomaa, että yhtälön vasemmalla puolella oleva eksponentti viittaa ryhmäelementin eksponentiaatioon. Erityisessä esimerkissämme tämä todellakin sisältää aritmeettisen eksponentiaation yhtälön oikealla puolella (mutta se olisi voinut myös sisältää esimerkiksi yhteenlaskua). Selventääkseni, olen kirjoittanut toistetun operaation, sen sijaan että käyttäisin eksponenttimuotoa oikealla puolella.

* $2^1 = 2 \mod 11$
* $2^2 = 2 \cdot 2 \mod 11 = 4 \mod 11$
* $2^3 = 2 \cdot 2 \cdot 2 \mod 11 = 8 \mod 11$
* $2^4 = 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 16 \mod 11 = 5 \mod 11$
* $2^5 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 32 \mod 11 = 10 \mod 11$
* $2^6 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 64 \mod 11 = 9 \mod 11$
* $2^7 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 128 \mod 11 = 7 \mod 11$
* $2^8 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 256 \mod 11 = 3 \mod 11$
* $2^9 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 512 \mod 11 = 6 \mod 11$
* $2^{10} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 1024 \mod 11 = 1 \mod 11$
* $2^{11} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 2048 \mod 11 = 2 \mod 11$
* $2^{12} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 4096 \mod 11 = 4 \mod 11$

Jos tarkastelet huolellisesti, voit nähdä, että eksponentiaalifunktion suorittaminen elementille 2 kiertää kaikki $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ ryhmän elementit seuraavassa järjestyksessä: 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. $2^{10}$ jälkeen elementin 2 eksponentiaalifunktion jatkaminen kiertää kaikki elementit uudelleen ja samassa järjestyksessä. Näin ollen elementti 2 on generaattori ryhmässä $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$.

Vaikka $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ ryhmällä on useita generaattoreita, eivät kaikki tämän ryhmän elementit ole generaattoreita. Harkitse esimerkiksi elementtiä 3. Ensimmäisten 10 eksponentiaation läpikäynti, ilman työläiden laskelmien näyttämistä, tuottaa seuraavat tulokset:

* $3^1 = 3 \mod 11$
* $3^2 = 9 \mod 11$
* $3^3 = 5 \mod 11$
* $3^4 = 4 \mod 11$
* $3^5 = 1 \mod 11$
* $3^6 = 3 \mod 11$
* $3^7 = 9 \mod 11$
* $3^8 = 5 \mod 11$
* $3^9 = 4 \mod 11$
* $3^{10} = 1 \mod 11$
Pyöräilyn sijaan kaikkien arvojen läpi $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, alkion 3 eksponentointi johtaa vain osajoukkoon näistä arvoista: 3, 9, 5, 4 ja 1. Viidennen eksponentoinnin jälkeen nämä arvot alkavat toistua.
Voimme nyt määritellä **syklisen ryhmän** minä tahansa ryhmänä, jolla on ainakin yksi generaattori. Toisin sanoen, on olemassa ainakin yksi ryhmän alkio, josta voit tuottaa kaikki muut ryhmän alkiot eksponentoinnin kautta.

Olet ehkä huomannut yllä olevassa esimerkissämme, että sekä $2^{10}$ että $3^{10}$ ovat yhtä suuria kuin $1 \mod 11$. Itse asiassa, vaikka emme suoritakaan laskelmia, minkä tahansa ryhmän $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ alkion eksponentointi 10:llä tuottaa $1 \mod 11$. Miksi näin on?

Tämä on tärkeä kysymys, mutta sen vastaamiseen tarvitaan jonkin verran työtä.

Aloitetaan olettamalla kaksi positiivista kokonaislukua $a$ ja $N$. Eräs tärkeä lukuteorian teoreema toteaa, että $a$:lla on kertolaskun käänteisalkio modulo $N$ (eli kokonaisluku $b$ siten, että $a \cdot b = 1 \mod N$) jos ja vain jos suurin yhteinen tekijä $a$:n ja $N$:n välillä on 1. Toisin sanoen, jos $a$ ja $N$ ovat keskenään jaottomia.

Joten, mille tahansa kokonaislukujen ryhmälle, joka on varustettu kertolaskulla modulo $N$, vain pienemmät keskenään jaottomat $N$:n kanssa sisältyvät joukkoon. Voimme merkitä tämän joukon $\mathbb{Z}^c \mod N$.

Esimerkiksi, oletetaan että $N$ on 10. Vain kokonaisluvut 1, 3, 7 ja 9 ovat keskenään jaottomia 10:n kanssa. Joten joukko $\mathbb{Z}^c \mod 10$ sisältää vain $\{1, 3, 7, 9\}$. Et voi luoda ryhmää kokonaislukujen kertolaskulla modulo 10 käyttäen mitään muita kokonaislukuja välillä 1 ja 10. Tälle erityiselle ryhmälle käänteisparit ovat 1 ja 9, sekä 3 ja 7.

Tapauksessa, jossa $N$ itsessään on alkuluku, kaikki kokonaisluvut 1:stä $N – 1$:een ovat keskenään jaottomia $N$:n kanssa. Tällainen ryhmä, siis, on järjestykseltään $N – 1$. Käyttäen aiempaa merkintäämme, $\mathbb{Z}^c \mod N$ on yhtä suuri kuin $\mathbb{Z}^* \mod N$, kun $N$ on alkuluku. Valitsemamme ryhmä aikaisemmassa esimerkissämme, $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, on tietty esimerkki tästä ryhmäluokasta.

Seuraavaksi, funktio $\phi(N)$ laskee keskenään jaottomien lukumäärän aina lukuun $N$ asti, ja sitä kutsutaan **Eulerin Phi-funktioksi**. [1] **Eulerin teoreeman** mukaan, aina kun kaksi kokonaislukua $a$ ja $N$ ovat keskenään jaottomia, seuraava pätee:

* $a^{\phi(N)} \mod N = 1 \mod N$
Tällä on tärkeä merkitys ryhmien $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ luokalle, missä $N$ on alkuluku. Näissä ryhmissä ryhmäelementin eksponentiaatio edustaa aritmeettista eksponentiaatiota. Toisin sanoen, $a^{\phi(N)} \mod N$ edustaa aritmeettista operaatiota $a^{\phi(N)} \mod N$. Koska mikä tahansa elementti $a$ näissä kertolaskullisissa ryhmissä on keskenään jaottomissa suhteissa $N$:n kanssa, se tarkoittaa, että $a^{\phi(N)} \mod N = a^{N – 1} \mod N = 1 \mod N$.

Eulerin teoreema on todella tärkeä tulos. Aluksi se tarkoittaa, että kaikki elementit ryhmässä $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ voivat vain kiertää läpi joukon arvoja eksponentiaation avulla, jotka jakautuvat $N – 1$:llä. Esimerkiksi ryhmässä $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ tämä tarkoittaa, että jokainen elementti voi vain kiertää läpi 2, 5 tai 10 elementtiä. Ryhmän arvot, joiden kautta mikä tahansa elementti kiertää eksponentiaation yhteydessä, tunnetaan **elementin järjestyksenä**. Elementti, jonka järjestys vastaa ryhmän järjestystä, on generaattori.

Lisäksi Eulerin teoreema tarkoittaa, että voimme aina tietää tuloksen $a^{N – 1} \mod N$ mistä tahansa ryhmästä $\langle \mathbb{Z}^* \mod N, \cdot \rangle$, missä $N$ on alkuluku. Näin on riippumatta siitä, kuinka monimutkaisia todelliset laskelmat saattavat olla.

Esimerkiksi, oletetaan että ryhmämme on $\mathbb{Z}^* \mod 160,481,182$ (missä 160,481,182 on todellakin alkuluku). Tiedämme, että kaikki kokonaisluvut 1 läpi 160,481,181 täytyy olla tämän ryhmän elementtejä, ja että $\phi(n) = 160,481,181$. Vaikka emme voi tehdä kaikkia laskutoimituksia, tiedämme, että lausekkeet kuten $514^{160,481,181}$, $2,005^{160,481,181}$, ja $256,212^{160,481,181}$ täytyy kaikkien arvioida $1 \mod 160,481,182$.

**Huomautuksia:**

[1] Funktio toimii seuraavasti. Mikä tahansa kokonaisluku $N$ voidaan jakaa alkulukujen tuloksi. Oletetaan, että tietty $N$ on jaettu seuraavasti: $p_1^{e1} \cdot p_2^{e2} \cdot \ldots \cdot p_m^{em}$, missä kaikki $p$:t ovat alkulukuja ja kaikki $e$:t ovat kokonaislukuja, jotka ovat suurempia tai yhtä suuria kuin 1. Sitten:

$$
\phi(N) = \sum_{i=1}^m \left[p_i^{e_i} - p_i^{e_i - 1}\right]
$$

Eulerin Phi-funktion kaava $N$:n alkulukuhajotelmaan.

## Kentät
<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>

Ryhmä on perus algebraallinen rakenne abstraktissa algebrassa, mutta on olemassa monia muita. Ainoa toinen algebraallinen rakenne, jonka kanssa sinun tarvitsee olla tuttu, on **kenttä**, erityisesti **äärellinen kenttä**. Tätä algebraallista rakennetta käytetään usein kryptografiassa, kuten Advanced Encryption Standardissa. Jälkimmäinen on pääasiallinen symmetrinen salausjärjestelmä, johon törmäät käytännössä.
Kenttä on johdettu ryhmän käsitteestä. Erityisesti **kenttä** on alkioiden joukko **S**, joka on varustettu kahdella binäärioperaattorilla $\circ$ ja $\diamond$, ja joka täyttää seuraavat ehdot:
1. Joukko **S** varustettuna $\circ$:lla on Abelin ryhmä.
2. Joukko **S** varustettuna $\diamond$:lla on Abelin ryhmä "nollasta eroaville" alkiolle.
3. Joukko **S** varustettuna kahdella operaattorilla täyttää niin kutsutun distributiivisen ehdon: Oletetaan, että $a$, $b$ ja $c$ ovat joukon **S** alkioita. Silloin **S** varustettuna kahdella operaattorilla täyttää distributiivisen ominaisuuden, kun $a \circ (b \diamond c) = (a \circ b) \diamond (a \circ c)$.

Huomaa, että kuten ryhmien kohdalla, kentän määritelmä on hyvin abstrakti. Se ei tee oletuksia **S**:n alkioiden tyypeistä tai operaatioista $\circ$ ja $\diamond$. Se vain toteaa, että kenttä on mikä tahansa alkioiden joukko, jossa on kaksi operaatiota, joille kolme yllä mainittua ehtoa pätevät. (Toisen Abelin ryhmän "nolla"-alkio voidaan tulkita abstraktisti.)

Mikä voisi olla esimerkki kentästä? Hyvä esimerkki on joukko $\mathbb{Z} \mod 7$, tai $\{0, 1, \ldots, 7\}$ määriteltynä standardisummalla (sijasta $\circ$ yllä) ja standardikertolaskulla (sijasta $\diamond$ yllä).

Ensinnäkin, $\mathbb{Z} \mod 7$ täyttää ehdon olemisesta Abelin ryhmä yhteenlaskun suhteen, ja se täyttää ehdon olemisesta Abelin ryhmä kertolaskun suhteen, jos otetaan huomioon vain nollasta eroavat alkiot. Toiseksi, joukon ja kahden operaattorin yhdistelmä täyttää distributiivisen ehdon.

On didaktisesti arvokasta tutkia näitä väitteitä käyttämällä joitakin tiettyjä arvoja. Otetaan kokeelliset arvot 5, 2 ja 3, joitakin satunnaisesti valittuja alkioita joukosta $\mathbb{Z} \mod 7$, tarkastellaksemme kenttää $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$. Käytämme näitä kolmea arvoa järjestyksessä, tarpeen mukaan tutkiaksemme tiettyjä ehtoja.

Tutkitaan ensin, onko $\mathbb{Z} \mod 7$ varustettuna yhteenlaskulla Abelin ryhmä.

1. **Sulkeutumisehto**: Otetaan arvot 5 ja 2. Tässä tapauksessa $[5 + 2] \mod 7 = 7 \mod 7 = 0$. Tämä on todellakin elementti joukossa $\mathbb{Z} \mod 7$, joten tulos on johdonmukainen sulkeutumisehdon kanssa.
2. **Assosiatiivisuusehto**: Otetaan arvot 5, 2 ja 3. Tässä tapauksessa $[(5 + 2) + 3] \mod 7 = [5 + (2 + 3)] \mod 7 = 10 \mod 7 = 3$. Tämä on johdonmukaista assosiatiivisuusehdon kanssa.
3. **Identiteettiehto**: Otetaan arvo 5. Tässä tapauksessa $[5 + 0] \mod 7 = [0 + 5] \mod 7 = 5$. Joten 0 näyttää olevan identiteettialkio yhteenlaskulle.
4. **Käänteisehto**: Tarkastellaan luvun 5 käänteisarvoa. On täytettävä ehto, että $[5 + d] \mod 7 = 0$ jollakin arvolla $d$. Tässä tapauksessa yksilöllinen arvo joukosta $\mathbb{Z} \mod 7$, joka täyttää tämän ehdon, on 2. **Vaihdannaisuusehto**: Otetaan arvot 5 ja 3. Tässä tapauksessa $[5 + 3] \mod 7 = [3 + 5] \mod 7 = 1$. Tämä on yhdenmukaista vaihdannaisuusehdon kanssa.

Joukko $\mathbb{Z} \mod 7$ varustettuna yhteenlaskulla vaikuttaa selvästi olevan Abelin ryhmä. Tutkitaan nyt, onko $\mathbb{Z} \mod 7$ varustettuna kertolaskulla Abelin ryhmä kaikille nollasta poikkeaville alkiolle.

1. **Sulkeutumisehto**: Otetaan arvot 5 ja 2. Tässä tapauksessa $[5 \cdot 2] \mod 7 = 10 \mod 7 = 3$. Tämä on myös elementti joukosta $\mathbb{Z} \mod 7$, joten tulos on yhdenmukainen sulkeutumisehdon kanssa.
2. **Liitännäisyys**: Otetaan arvot 5, 2 ja 3. Tässä tapauksessa $[(5 \cdot 2) \cdot 3] \mod 7 = [5 \cdot (2 \cdot 3)] \mod 7 = 30 \mod 7 = 2$. Tämä on yhdenmukaista liitännäisyyskäsitteen kanssa.
3. **Neutraaliehto**: Otetaan arvo 5. Tässä tapauksessa $[5 \cdot 1] \mod 7 = [1 \cdot 5] \mod 7 = 5$. Joten 1 vaikuttaa olevan neutraalialkio kertolaskulle.
4. **Käänteisehto**: Tarkastellaan luvun 5 käänteisarvoa. On täytettävä ehto, että $[5 \cdot d] \mod 7 = 1$ jollakin arvolla $d$. Joukosta $\mathbb{Z} \mod 7$ löytyvä yksilöllinen arvo, joka täyttää tämän ehdon, on 3. Tämä on yhdenmukaista käänteisehdon kanssa.
5. **Vaihdannaisuusehto**: Otetaan arvot 5 ja 3. Tässä tapauksessa $[5 \cdot 3] \mod 7 = [3 \cdot 5] \mod 7 = 15 \mod 7 = 1$. Tämä on yhdenmukaista vaihdannaisuusehdon kanssa.

Joukko $\mathbb{Z} \mod 7$ vaikuttaa selvästi täyttävän Abelin ryhmän säännöt, kun sitä käytetään joko yhteen- tai kertolaskun kanssa nollasta poikkeaville alkiolle.

Lopuksi, tämä joukko yhdistettynä molempiin operaatioihin vaikuttaa täyttävän jakautumisehdon. Otetaan arvot 5, 2 ja 3. Voimme nähdä, että $[5 \cdot (2 + 3)] \mod 7 = [5 \cdot 2 + 5 \cdot 3] \mod 7 = 25 \mod 7 = 4$.

Olemme nyt nähneet, että $\mathbb{Z} \mod 7$ varustettuna sekä yhteen- että kertolaskulla täyttää äärellisen kentän aksioomat, kun testataan tietyillä arvoilla. Tietenkin voimme myös osoittaa tämän yleisesti, mutta emme tee sitä tässä.

Keskeinen ero on kahden tyyppisten kenttien välillä: äärelliset ja äärettömät kentät.
**Ääretön kenttä** viittaa kenttään, jossa joukko **S** on äärettömän suuri. Reaalilukujen joukko $\mathbb{R}$ yhdessä yhteen- ja kertolaskun kanssa on esimerkki äärettömästä kentästä. **Äärellinen kenttä**, joka tunnetaan myös nimellä **Galois'n kenttä**, on kenttä, jossa joukko **S** on äärellinen. Yllä mainittu esimerkkimme $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$ on äärellinen kenttä.
Kryptografiassa olemme ensisijaisesti kiinnostuneita äärellisistä kentistä. Yleisesti voidaan osoittaa, että äärellinen kenttä on olemassa jollekin elementtien joukolle **S** jos ja vain jos sillä on $p^m$ elementtiä, missä $p$ on alkuluku ja $m$ positiivinen kokonaisluku, joka on suurempi tai yhtä suuri kuin yksi. Toisin sanoen, jos jonkin joukon **S** järjestys on alkuluku ($p^m$, missä $m = 1$) tai jonkin alkuluvun potenssi ($p^m$, missä $m > 1$), niin voit löytää kaksi operaattoria $\circ$ ja $\diamond$ siten, että kentän ehdot täyttyvät.

Jos jollakin äärellisellä kentällä on alkuluvun verran elementtejä, sitä kutsutaan **alkukentäksi**. Jos äärellisen kentän elementtien määrä on alkuluvun potenssi, kenttää kutsutaan **laajennuskentäksi**. Kryptografiassa olemme kiinnostuneita sekä alkukentistä että laajennuskentistä. [2]

Kryptografiassa ensisijaisen kiinnostuksen kohteena olevat alkukentät ovat niitä, joissa kaikkien kokonaislukujen joukko moduloituu jonkin alkuluvun mukaan, ja operaattorit ovat tavallinen yhteen- ja kertolasku. Tämä äärellisten kenttien luokka sisältäisi $\mathbb{Z} \mod 2$, $\mathbb{Z} \mod 3$, $\mathbb{Z} \mod 5$, $\mathbb{Z} \mod 7$, $\mathbb{Z} \mod 11$, $\mathbb{Z} \mod 13$, ja niin edelleen. Mille tahansa alkukentälle $\mathbb{Z} \mod p$, kentän kokonaislukujen joukko on seuraava: $\{0, 1, \ldots, p – 2, p – 1\}$.

Kryptografiassa olemme myös kiinnostuneita laajennuskentistä, erityisesti mistä tahansa kentästä, jolla on $2^m$ elementtiä, missä $m > 1$. Tällaisia äärellisiä kenttiä käytetään esimerkiksi Rijndael-salauksessa, joka muodostaa Advanced Encryption Standardin perustan. Vaikka alkukentät ovat suhteellisen intuitiivisia, nämä kakkosen potenssiin perustuvat laajennuskentät eivät todennäköisesti ole tuttuja kenellekään, joka ei ole perehtynyt abstraktiin algebraan.

Aluksi, on todellakin totta, että mille tahansa kokonaislukujen joukolle, jolla on $2^m$ elementtiä, voidaan määrittää kaksi operaattoria, jotka tekisivät niiden yhdistelmästä kentän (kunhan $m$ on positiivinen kokonaisluku). Kuitenkaan pelkästään se, että kenttä on olemassa, ei välttämättä tarkoita, että se on helppo löytää tai erityisen käytännöllinen tietyissä sovelluksissa.

Käy ilmi, että erityisen soveltuvia laajennuskenttiä $2^m$ kryptografiassa ovat ne, jotka on määritelty erityisten polynomilausekkeiden joukkojen yli, eikä jonkin kokonaislukujen joukon yli.

Oletetaan esimerkiksi, että haluaisimme laajennuskentän, jolla on $2^3$ (eli 8) elementtiä joukossa. Vaikka monia erilaisia joukkoja voidaan käyttää tällaisen koon kenttiin, yksi tällainen joukko sisältää kaikki uniikit polynomit muotoa $a_2x^2 + a_1x + a_0$, missä jokainen kerroin $a_i$ on joko 0 tai 1. Näin ollen tämä joukko **S** sisältää seuraavat elementit:
1. $0$: Tapaus, jossa $a_2 = 0$, $a_1 = 0$ ja $a_0 = 0$.
2. $1$: Tapaus, jossa $a_2 = 0$, $a_1 = 0$ ja $a_0 = 1$.
3. $x$: Tapaus, jossa $a_2 = 0$, $a_1 = 1$ ja $a_0 = 0$.
4. $x + 1$: Tapaus, jossa $a_2 = 0$, $a_1 = 1$ ja $a_0 = 1$.
5. $x^2$: Tapaus, jossa $a_2 = 1$, $a_1 = 0$ ja $a_0 = 0$.
6. $x^2 + 1$: Tapaus, jossa $a_2 = 1$, $a_1 = 0$ ja $a_0 = 1$.
7. $x^2 + x$: Tapaus, jossa $a_2 = 1$, $a_1 = 1$ ja $a_0 = 0$.
8. $x^2 + x + 1$: Tapaus, jossa $a_2 = 1$, $a_1 = 1$ ja $a_0 = 1$.

Joten **S** olisi joukko $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$. Mitkä kaksi operaatiota voidaan määritellä tämän elementtien joukon yli varmistaakseen, että niiden yhdistelmä muodostaa kentän?

Ensimmäinen operaatio joukolle **S** ($\circ$) voidaan määritellä standardina polynomien lisäyksenä modulo 2. Sinun tarvitsee vain lisätä polynomit kuten tavallisesti, ja sitten soveltaa modulo 2 kunkin tuloksena olevan polynomin kertoimiin. Tässä on joitakin esimerkkejä:

* $[(x^2) + (x^2 + x + 1)] \mod 2 = [2x^2 + x + 1] \mod 2 = x + 1$
* $[(x^2 + x) + (x)] \mod 2 = [x^2 + 2x] \mod 2 = x^2$
* $[(x + 1) + (x^2 + x + 1)] \mod 2 = [x^2 + 2x + 2] \mod 2 = x^2 + 1$

Toinen operaatio joukolle **S** ($\diamond$), joka tarvitaan kentän luomiseksi, on monimutkaisempi. Se on eräänlainen kertolasku, mutta ei standardi aritmeettinen kertolasku. Sen sijaan sinun täytyy nähdä jokainen elementti vektorina ja ymmärtää operaatio näiden kahden vektorin kertolaskuna modulo reduusoimaton polynomi.

Kääntykäämme ensin reduusoimattoman polynomin käsitteeseen. **Reduusoimaton polynomi** on sellainen, jota ei voida faktorisoida (aivan kuten alkulukua ei voida faktorisoida muihin komponentteihin kuin 1 ja itse alkuluku). Tarkoituksemme kannalta olemme kiinnostuneita polynomeista, jotka ovat reduusoimattomia kaikkien kokonaislukujen joukossa. (Huomaa, että saatat pystyä faktorisoimaan tiettyjä polynomeja esimerkiksi reaaliluvuilla tai kompleksiluvuilla, vaikka et pystyisikään faktorisoimaan niitä käyttäen kokonaislukuja.)
Esimerkiksi, harkitse polynomia $x^2 - 3x + 2$. Tämä voidaan kirjoittaa uudelleen muodossa $(x – 1)(x – 2)$. Täten, tämä ei ole redusoimaton. Nyt harkitse polynomia $x^2 + 1$. Käyttäen ainoastaan kokonaislukuja, tälle lausekkeelle ei löydy edelleen faktorointia. Täten, tämä on redusoimaton polynomi kokonaislukujen suhteen.

Seuraavaksi, käännämme huomiomme vektorikertolaskun konseptiin. Emme tutki tätä aihetta syvällisesti, mutta sinun tarvitsee ymmärtää perussääntö: Mikä tahansa vektorijako on mahdollinen, kunhan jakaja on asteen suhteen korkeampi tai yhtä suuri kuin jakaja. Jos jakajan aste on matalampi kuin jakajan, jakajaa ei enää voida jakaa jakajalla.

Esimerkiksi, harkitse lauseketta $x^6 + x + 1 \mod x^5 + x^2$. Tämä selvästi redukoituu edelleen, koska jakajan aste, 6, on korkeampi kuin jakajan aste, 5. Nyt harkitse lauseketta $x^5 + x + 1 \mod x^5 + x^2$. Tämä myös redukoituu edelleen, koska jakajan aste, 5, ja jakajan aste, 5, ovat yhtä suuret.

Kuitenkin, nyt harkitse lauseketta $x^4 + x + 1 \mod x^5 + x^2$. Tämä ei redukoidu edelleen, koska jakajan aste, 4, on matalampi kuin jakajan aste, 5.

Tämän tiedon perusteella olemme nyt valmiita löytämään toisen operaation joukolle $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.

Olen jo sanonut, että toisen operaation tulisi ymmärtää vektorikertolaskuna modulo jonkin redusoimattoman polynomin. Tämän redusoimattoman polynomin tulisi varmistaa, että toinen operaatio määrittelee Abelian ryhmän yli **S** ja on yhdenmukainen distributiivisen ehdon kanssa. Mikä siis tämän redusoimattoman polynomin tulisi olla?

Koska kaikki vektorit joukossa ovat asteen 2 tai matalampia, redusoimattoman polynomin tulisi olla asteen 3. Jos kahden vektorin kertolasku joukossa tuottaa asteen 3 tai korkeamman polynomin, tiedämme, että modulo asteen 3 polynomi tuottaa aina asteen 2 tai matalamman polynomin. Tämä johtuu siitä, että mikä tahansa asteen 3 tai korkeampi polynomi on aina jaettavissa asteen 3 polynomilla. Lisäksi, polynomin, joka toimii jakajana, on oltava redusoimaton.

Käy ilmi, että on olemassa useita asteen 3 redusoimattomia polynomeja, joita voisimme käyttää jakajanamme. Jokainen näistä polynomeista määrittelee eri kentän yhdessä joukkomme **S** ja modulo 2 lisäyksen kanssa. Tämä tarkoittaa, että sinulla on useita vaihtoehtoja, kun käytät laajennuskenttiä $2^m$ kryptografiassa.

Esimerkiksemme, oletetaan, että valitsemme polynomin $x^3 + x + 1$. Tämä on todellakin redusoimaton, koska et voi faktoroida sitä käyttäen kokonaislukuja. Lisäksi, se varmistaa, että kahden elementin kertolasku tuottaa aina asteen 2 tai matalamman polynomin.
Käydään läpi esimerkki toisesta operaatiosta käyttäen jakajana polynomia $x^3 + x + 1$ havainnollistaaksemme, miten se toimii. Oletetaan, että kertotat alkiot $x^2 + 1$ ja $x^2 + x$ joukossamme **S**. Meidän on sitten laskettava lauseke $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1$. Tämä voidaan yksinkertaistaa seuraavasti:
* $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1 =$
* $[x^2 \cdot x^2 + x^2 \cdot x + 1 \cdot x^2 + 1 \cdot x] \mod x^3 + x + 1 =$
* $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$

Tiedämme, että $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$ voidaan pienentää, koska jakajan aste (4) on suurempi kuin jakajan aste (3).

Aloitetaan, näet, että lauseke $x^3 + x + 1$ menee $x^4 + x^3 + x^2 + x$:ään yhteensä $x$ kertaa. Voit varmistaa tämän kertomalla $x^3 + x + 1$:n $x$:llä, joka on $x^4 + x^2 + x$. Koska jälkimmäinen termi on samaa astetta kuin jakaja, nimittäin 4, tiedämme tämän toimivan. Voit laskea tämän jakamisen jäännöksen $x$:llä seuraavasti:

* $[(x^4 + x^3 + x^2 + x) - (x^4 + x^2 + x)] \mod x^3 + x + 1 =$
* $[x^3] \mod x^3 + x + 1 =$
* $x^3$

Joten jaettuamme $x^4 + x^3 + x^2 + x$:n $x^3 + x + 1$:llä yhteensä $x$ kertaa, meillä on jäännöksenä $x^3$. Voiko tämä vielä jakaa $x^3 + x + 1$:llä?

Intuitiivisesti voisi tuntua houkuttelevalta sanoa, että $x^3$ ei enää voida jakaa $x^3 + x + 1$:llä, koska jälkimmäinen termi vaikuttaa suuremmalta. Muista kuitenkin aiempi keskustelumme vektorijaosta. Niin kauan kuin jakajalla on suurempi tai yhtä suuri aste kuin jakajalla, lauseketta voidaan edelleen pienentää. Erityisesti lauseke $x^3 + x + 1$ voi mennä $x^3$:een täsmälleen 1 kerran. Jäännös lasketaan seuraavasti:

$$
[(x^3) - (x^3 + x + 1)] \mod x^3 + x + 1 = [x + 1] \mod x^3 + x + 1 = x + 1
$$

Saatat ihmetellä, miksi $(x^3) - (x^3 + x + 1)$ arvioituu $x + 1$:ksi eikä $-x - 1$:ksi. Muista, että kenttämme ensimmäinen operaatio määritellään modulo 2 mukaan. Siksi kahden vektorin vähennys tuottaa täsmälleen saman tuloksen kuin kahden vektorin yhteenlasku.
Yhteenvetona $x^2 + 1$ ja $x^2 + x$ kertolaskusta: Kun kerrot nämä kaksi termiä, saat neljännen asteen polynomin, $x^4 + x^3 + x^2 + x$, joka tulee supistaa modulo $x^3 + x + 1$. Neljännen asteen polynomi on jaollinen $x^3 + x + 1$:llä tasan $x + 1$ kertaa. Jakojäännös, kun $x^4 + x^3 + x^2 + x$ jaetaan $x^3 + x + 1$:llä tasan $x + 1$ kertaa, on $x + 1$. Tämä on todellakin elementti joukossamme $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.

Miksi laajennuskentät, jotka perustuvat kakkosen potenssiin polynomijoukoissa, kuten yllä olevassa esimerkissä, ovat hyödyllisiä kryptografiassa? Syy on se, että voit tarkastella polynomien kertoimia tällaisissa joukoissa, joko 0 tai 1, binäärijonojen elementteinä tietyn pituuden kanssa. Esimerkkimme joukko **S** voitaisiin sen sijaan nähdä joukkona **S**, joka sisältää kaikki kolmen pituiset binäärijonot (000 - 111). **S**-joukon operaatioita voidaan sitten käyttää suorittamaan operaatioita näille binäärijonoille ja tuottamaan samanpituisia binäärijonoja.

**Huomautuksia:**

[2] Laajennuskentät ovat hyvin vastenintuitiivisia. Niiden elementit eivät ole kokonaislukuja, vaan polynomijoukkoja. Lisäksi kaikki operaatiot suoritetaan modulo jonkin redusoimattoman polynomin suhteen.

## Abstrakti algebra käytännössä
<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>

Huolimatta muodollisesta kielestä ja keskustelun abstraktiudesta, ryhmän käsite ei pitäisi olla liian vaikea ymmärtää. Se on vain joukko elementtejä yhdessä binäärioperaation kanssa, jossa tämän binäärioperaation suorittaminen näille elementeille täyttää neljä yleistä ehtoa. Abelin ryhmässä on vain yksi lisäehto, jota kutsutaan vaihdannaisuudeksi. Syklinen ryhmä puolestaan on erityinen Abelin ryhmä, nimittäin sellainen, jolla on generaattori. Kenttä on vain monimutkaisempi rakenne perusryhmän käsitteestä.

Mutta jos olet käytännöllisesti ajatteleva henkilö, saatat tässä vaiheessa miettiä: Ketä kiinnostaa? Onko merkitystä sillä, että jokin elementtien joukko operaattorin kanssa on ryhmä, tai edes Abelin tai syklinen ryhmä? Entä onko merkitystä sillä, että jokin on kenttä?

Menemättä liian yksityiskohtaisuuksiin, vastaus on "kyllä". Ryhmät keksittiin ensimmäisen kerran 1800-luvulla ranskalaisen matemaatikon Evariste Galois'n toimesta. Hän käytti niitä vetämään johtopäätöksiä yli viidennen asteen polynomiyhtälöiden ratkaisemisesta.

Siitä lähtien ryhmän käsite on auttanut valaisemaan useita ongelmia matematiikassa ja muualla. Esimerkiksi fyysikko Murray-Gellman pystyi ennustamaan hiukkasen olemassaolon ennen kuin sitä havaittiin kokeissa. [3] Toisena esimerkkinä kemistit käyttävät ryhmäteoriaa molekyylien muotojen luokitteluun. Matemaatikot ovat jopa käyttäneet ryhmän käsitettä vetämään johtopäätöksiä jostakin niin konkreettisesta kuin tapetista!
Osoittaminen, että joukko elementtejä jonkin operaattorin kanssa muodostaa ryhmän, tarkoittaa, että kuvailemasi asia omaa tietynlaisen symmetrian. Ei symmetriaa tavallisessa merkityksessä, vaan abstraktimmassa muodossa. Ja tämä voi tarjota merkittäviä oivalluksia tiettyihin järjestelmiin ja ongelmiin. Abstraktin algebran monimutkaisemmat käsitteet antavat meille lisätietoa.
Erityisen tärkeää on nähdä lukuteoreettisten ryhmien ja kenttien merkitys käytännössä niiden sovellusten kautta kryptografiassa, erityisesti julkisen avaimen kryptografiassa. Olemme jo keskustelleet esimerkiksi siitä, kuinka laajennuskenttiä käytetään Rijndael-salauksessa. Käsittelemme tätä esimerkkiä tarkemmin *lukussa 5*.

Lisäkeskusteluun abstraktista algebrasta suosittelen Socratican erinomaista videosarjaa abstraktista algebrasta. [4] Suosittelisin erityisesti seuraavia videoita: “What is abstract algebra?”, “Group definition (expanded)”, “Ring definition (expanded)”, ja “Field definition (expanded).” Nämä neljä videota antavat sinulle lisäoivalluksia yllä olevaan keskusteluun. (Emme keskustelleet renkaista, mutta kenttä on vain erityinen tyyppi renkaasta.)

Lisäkeskusteluun modernista lukuteoriasta voit tutustua moniin edistyneisiin keskusteluihin kryptografiasta. Ehdotuksina tarjoaisin Jonathan Katz ja Yehuda Lindellin Introduction to Modern Cryptography tai Christof Paar ja Jan Pelzlin Understanding Cryptography lisäkeskusteluun. [5]

**Muistiinpanot:**

[3] Katso [YouTube-video](https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be)

[4] Socratica, [Abstract Algebra](https://www.socratica.com/subject/abstract-algebra)

[5] Katz ja Lindell, *Introduction to Modern Cryptography*, 2. painos, 2015 (CRC Press: Boca Raton, FL). Paar ja Pelzl, *Understanding Cryptography*, 2010 (Springer-Verlag: Berlin).

# Symmetrinen kryptografia
<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>

## Alice ja Bob
<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>

Yksi kryptografian kahdesta päähaarasta on symmetrinen kryptografia. Se käsittää salausjärjestelmät sekä järjestelmät, jotka liittyvät autentikointiin ja eheyteen. 1970-luvulle asti kaikki kryptografia olisi koostunut symmetrisistä salausjärjestelmistä.

Pääkeskustelu alkaa tarkastelemalla symmetrisiä salausjärjestelmiä ja tekemällä ratkaiseva ero virtasalausten ja lohkosalausten välillä. Tämän jälkeen käännytään viestien autentikointikoodeihin, jotka ovat järjestelmiä viestien eheyden ja aitouden varmistamiseksi. Lopuksi tutkimme, miten symmetrisiä salausjärjestelmiä ja viestien autentikointikoodeja voidaan yhdistää turvallisen viestinnän takaamiseksi.

Tässä luvussa käsitellään ohimennen erilaisia symmetrisen kryptografian järjestelmiä käytännöstä. Seuraava luku tarjoaa yksityiskohtaisen esityksen salauksesta käytännön virta- ja lohkosalausmenetelmillä, nimittäin RC4:llä ja AES:llä.

Ennen kuin aloitamme keskustelun symmetrisestä kryptografiasta, haluan lyhyesti mainita muutaman huomion Alicen ja Bobin kuvituksista tässä ja seuraavissa luvuissa.

___

Kryptografian periaatteiden havainnollistamisessa ihmiset turvautuvat usein esimerkkeihin, jotka liittyvät Aliceen ja Bobiin. Aion tehdä niin myös. 

Erityisesti jos olet uusi kryptografiassa, on tärkeää ymmärtää, että nämä Alicen ja Bobin esimerkit on tarkoitettu vain kryptografian periaatteiden ja rakenteiden havainnollistamiseen yksinkertaistetussa ympäristössä. Periaatteet ja rakenteet ovat kuitenkin sovellettavissa paljon laajemmassa todellisen elämän kontekstissa.
Seuraavassa on viisi keskeistä seikkaa, jotka tulee pitää mielessä esimerkeissä, jotka koskevat Alicea ja Bobia kryptografiassa:
1. Ne voidaan helposti kääntää esimerkeiksi, joissa toimijoina ovat muun tyyppiset tahot, kuten yritykset tai hallitusorganisaatiot.
2. Ne voidaan helposti laajentaa sisältämään kolme tai useampia toimijoita.
3. Esimerkeissä Bob ja Alice ovat tyypillisesti aktiivisia osallistujia luomassa kutakin viestiä ja soveltamassa kryptografisia järjestelmiä kyseiseen viestiin. Mutta todellisuudessa elektroninen viestintä on pitkälti automatisoitua. Esimerkiksi kun vierailet verkkosivustolla, joka käyttää kuljetuskerroksen turvallisuutta, kryptografia hoidetaan tyypillisesti kokonaan tietokoneellasi ja web-palvelimella.
4. Elektronisen viestinnän kontekstissa "viestit", jotka lähetetään viestintäkanavan kautta, ovat yleensä TCP/IP-paketteja. Nämä voivat kuulua sähköpostiin, Facebook-viestiin, puhelinkeskusteluun, tiedostonsiirtoon, verkkosivustoon, ohjelmiston lataukseen ja niin edelleen. Ne eivät ole viestejä perinteisessä mielessä. Siitä huolimatta kryptografian asiantuntijat usein yksinkertaistavat tätä todellisuutta toteamalla, että viesti on esimerkiksi sähköposti.
5. Esimerkit keskittyvät tyypillisesti elektroniseen viestintään, mutta niitä voidaan myös laajentaa perinteisiin viestintämuotoihin, kuten kirjeisiin.

## Symmetriset salausjärjestelmät
<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>

Voimme määritellä **symmetrisen salausjärjestelmän** löyhästi minä tahansa kryptografisena järjestelmänä, joka sisältää kolme algoritmia:

1. **Avaimen generointialgoritmi**, joka luo yksityisen avaimen.
2. **Salausalgoritmi**, joka ottaa yksityisen avaimen ja avoimen tekstin syötteiksi ja tuottaa salatun tekstin.
3. **Salauksen purkualgoritmi**, joka ottaa yksityisen avaimen ja salatun tekstin syötteiksi ja tuottaa alkuperäisen avoimen tekstin.

Tyypillisesti salausjärjestelmä—oli se sitten symmetrinen tai asymmetrinen—tarjoaa mallin salaukselle perustuen ydin algoritmiin, eikä tarkkaan määrittelyyn.

Esimerkiksi harkitse Salsa20:ta, symmetristä salausjärjestelmää. Sitä voidaan käyttää sekä 128- että 256-bittisen avaimen pituuksilla. Avaimen pituuden valinta vaikuttaa joitakin pieniä yksityiskohtia algoritmissa (tarkalleen ottaen algoritmin kierrosten määrään).

Mutta ei sanoisi, että Salsa20:n käyttäminen 128-bittisellä avaimella on eri salausjärjestelmä kuin Salsa20 256-bittisellä avaimella. Ydin algoritmi pysyy samana. Vain kun ydin algoritmi muuttuu, puhuisimme todella kahdesta eri salausjärjestelmästä.

Symmetriset salausjärjestelmät ovat tyypillisesti hyödyllisiä kahdenlaisissa tapauksissa: (1) Niissä, joissa kaksi tai useampi agentti viestii etäältä ja haluaa pitää viestintänsä sisällön salassa; ja (2) niissä, joissa yksi agentti haluaa pitää viestin sisällön salassa ajan yli.

Voit nähdä tilanteen (1) kuvauksen *Kuvassa 1* alla. Bob haluaa lähettää viestin $M$ Alicelle etäisyyden yli, mutta ei halua muiden pystyvän lukemaan kyseistä viestiä.

Bob ensin salaa viestin $M$ yksityisellä avaimella $K$. Sitten hän lähettää salatun tekstin $C$ Alicelle. Kun Alice on vastaanottanut salatun tekstin, hän voi purkaa sen käyttäen avainta $K$ ja lukea avoimen tekstin. Hyvän salausjärjestelmän avulla mikään hyökkääjä, joka keskeyttää salatun tekstin $C$, ei pitäisi pystyä oppimaan mitään todellista merkitystä viestistä $M$.

Voit nähdä tilanteen (2) kuvauksen *Kuvassa 2* alla. Bob haluaa estää muita näkemästä tiettyjä tietoja. Tyypillinen tilanne voisi olla, että Bob on työntekijä, joka tallentaa arkaluonteisia tietoja tietokoneelleen, joita ei ole tarkoitettu ulkopuolisten eikä hänen kollegoidensa luettavaksi.
Bob salaa viestin $M$ ajankohtana $T_0$ avaimella $K$, jotta saadaan salattu teksti $C$. Ajankohtana $T_1$ hän tarvitsee viestin uudelleen ja purkaa salatun tekstin $C$ avaimella $K$. Mikään hyökkääjä, joka olisi saattanut saada salatun tekstin $C$ käsiinsä sillä välin, ei olisi pitänyt pystyä päättelemään mitään merkittävää viestistä $M$ sen perusteella.

*Kuva 1: Salaisuus tilan yli*

![Kuva 1: Salaisuus tilan yli](assets/Figure4-1.webp "Kuva 1: Salaisuus tilan yli")

*Kuva 2: Salaisuus ajan yli*

![Kuva 2: Salaisuus ajan yli](assets/Figure4-2.webp "Kuva 2: Salaisuus ajan yli")

## Esimerkki: Siirtosalaus
<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>

Luvussa 2 kohtasimme siirtosalauksen, joka on esimerkki hyvin yksinkertaisesta symmetrisestä salausmenetelmästä. Katsotaan sitä uudelleen tässä.

Oletetaan sanakirja *D*, joka yhdistää kaikki englannin kielen aakkoset, järjestyksessä, numeroiden joukkoon $\{0,1,2,\dots,25\}$. Oletetaan joukko mahdollisia viestejä **M**. Siirtosalaus on sitten salausmenetelmä, joka määritellään seuraavasti:

- Valitse satunnaisesti avain $k$ mahdollisten avainten joukosta **K**, missä **K** = $\{0,1,2,\dots,25\}$
- Salaus viestille $m \in$ **M**, seuraavasti:
    - Erota $m$ sen yksittäisiin kirjaimiin $m_0, m_1,\dots, m_i, \dots, m_l$
    - Muunna jokainen $m_i$ numeroksi sanakirjan *D* mukaan
    - Jokaiselle $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Muunna jokainen $c_i$ kirjaimeksi sanakirjan *D* mukaan
    - Yhdistä sitten $c_0, c_1,\dots, c_l$ saadaksesi salatun tekstin $c$
- Salatun tekstin $c$ purkaminen seuraavasti:
    - Muunna jokainen $c_i$ numeroksi sanakirjan *D* mukaan
    - Jokaiselle $c_i$, $m_i = [(c_i - k) \mod 26]$
    - Muunna jokainen $m_i$ kirjaimeksi sanakirjan *D* mukaan
    - Yhdistä sitten $m_0, m_1,\dots, m_l$ saadaksesi alkuperäisen viestin $m$

Siirtosalauksen olemus symmetrisenä salausmenetelmänä on, että samaa avainta käytetään sekä salaukseen että salauksen purkuun. Oletetaan esimerkiksi, että haluat salata viestin “DOG” käyttäen siirtosalausta, ja olet satunnaisesti valinnut avaimen "24". Viestin salaaminen tällä avaimella tuottaisi “BME”. Ainoa tapa saada alkuperäinen viesti takaisin on käyttämällä samaa avainta, "24", salauksen purkuprosessissa.

Tämä siirtosalaus on esimerkki **monoalfabeettisesta substituutiosalauksesta**: salausmenetelmästä, jossa salatun tekstin aakkosto on kiinteä (eli käytetään vain yhtä aakkostoa). Olettaen, että salauksen purkualgoritmi on deterministinen, jokainen substituutiosalatun tekstin symboli voi korkeintaan vastata yhtä symbolia alkuperäisessä tekstissä.
1700-luvulle asti monet salauksen sovellukset nojasivat vahvasti monoalfabeettisiin substituutiosalakirjoituksiin, vaikka usein nämä olivat paljon monimutkaisempia kuin Shift-salakirjoitus. Voisit esimerkiksi satunnaisesti valita kirjaimen aakkosista jokaiselle alkuperäisen tekstin kirjaimelle sillä ehdolla, että jokainen kirjain esiintyy vain kerran salatekstin aakkostossa. Tämä tarkoittaa, että sinulla olisi faktoriaali 26 mahdollista yksityistä avainta, mikä oli valtava määrä ennen tietokoneaikaa.
Huomaa, että tulet kohtaamaan termin **salakirjoitus** usein kryptografiassa. Ole tietoinen siitä, että tällä termillä on useita merkityksiä. Itse asiassa tiedän ainakin viisi erillistä merkitystä termille kryptografian sisällä.

Joissakin tapauksissa se viittaa salausjärjestelmään, kuten se tekee Shift-salakirjoituksessa ja monoalfabeettisessa substituutiosalakirjoituksessa. Kuitenkin termi voi myös viitata nimenomaan salausalgoritmiin, yksityiseen avaimen, tai vain mihin tahansa tällaisen salausjärjestelmän salatekstiin.

Lopuksi, termi salakirjoitus voi myös viitata ydin algoritmiin, josta voit rakentaa kryptografisia järjestelmiä. Näihin voivat sisältyä erilaiset salausalgoritmit, mutta myös muuntyyppiset kryptografiset järjestelmät. Tämä merkitys tulee relevantiksi lohkosalausten yhteydessä (katso osio "Lohkosalaus" alla).

Saatat myös kohdata termit **salata** tai **purkaa salaus**. Nämä termit ovat vain synonyymejä salaukselle ja salauksen purkamiselle.

## Brute force -hyökkäykset ja Kerckhoffs'in periaate
<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>

Shift-salakirjoitus on hyvin turvaton symmetrinen salausjärjestelmä, ainakin nykymaailmassa. [1] Hyökkääjä voisi vain yrittää purkaa minkä tahansa salatekstin kaikilla 26 mahdollisella avaimella nähdäkseen, mikä tulos on järkevä. Tämäntyyppistä hyökkäystä, jossa hyökkääjä vain kiertää avaimia nähdäkseen mikä toimii, tunnetaan nimellä **brute force -hyökkäys** tai **kaikenkattava avainhaku**.

Jotta salausjärjestelmä täyttäisi vähimmäisvaatimuksen turvallisuudesta, sillä on oltava joukko mahdollisia avaimia, tai **avainavaruus**, joka on niin suuri, että brute force -hyökkäykset ovat käytännössä mahdottomia. Kaikki nykyaikaiset salausjärjestelmät täyttävät tämän standardin. Tätä kutsutaan **riittävän avainavaruuden periaatteeksi**. Samankaltainen periaate pätee tyypillisesti erilaisissa kryptografisissa järjestelmissä.

Saadaksesi käsityksen modernien salausjärjestelmien massiivisesta avainavaruuden koosta, oletetaan, että tiedosto on salattu 128-bittisellä avaimella käyttäen edistynyttä salausstandardia. Tämä tarkoittaa, että hyökkääjällä on joukko $2^{128}$ avainta, joiden läpi hänen on kierrettävä brute force -hyökkäyksessä. 0,78 %:n onnistumismahdollisuus tällä strategialla vaatisi hyökkääjältä noin $2.65 \times 10^{36}$ avaimen läpikäymistä.

Oletetaan optimistisesti, että hyökkääjä voi yrittää $10^{16}$ avainta sekunnissa (eli 10 biljoonaa avainta sekunnissa). Testatakseen 0,78 % kaikista avainavaruuden avaimista, hänen hyökkäyksensä kestäisi $2.65 \times 10^{20}$ sekuntia. Tämä on noin 8,4 biljoonaa vuotta. Joten edes brute force -hyökkäys äärimmäisen tehokkaalta vastustajalta ei ole realistinen nykyaikaisella 128-bittisellä salausjärjestelmällä. Tämä on riittävän avainavaruuden periaatteen mukainen toiminta.

Onko Shift-salakirjoitus turvallisempi, jos hyökkääjä ei tiedä salausalgoritmia? Ehkä, mutta ei paljoa.
Joka tapauksessa nykyaikainen kryptografia olettaa aina, että minkä tahansa symmetrisen salausjärjestelmän turvallisuus perustuu yksinomaan yksityisen avaimen salassapitoon. Hyökkääjän oletetaan aina tietävän kaikki muut yksityiskohdat, mukaan lukien viestialue, avainalue, salattu teksti -alue, avaimen valinta -algoritmi, salausalgoritmi ja purkualgoritmi.
Ajatus siitä, että symmetrisen salausjärjestelmän turvallisuus voi perustua vain yksityisen avaimen salaisuuteen, tunnetaan **Kerckhoffs’in periaatteena**.

Alun perin Kerckhoffs’in tarkoittamana periaate koskee vain symmetrisiä salausjärjestelmiä. Yleisempi versio periaatteesta kuitenkin koskee myös kaikkia muita nykyaikaisia kryptografisia järjestelmiä: Mikään kryptografisen järjestelmän suunnittelu ei saa vaatia olla salainen, jotta se olisi turvallinen; salaisuus voi ulottua vain joihinkin tietostringeihin, tyypillisesti yksityiseen avaimen.

Kerckhoffs’in periaate on keskeinen nykyaikaiselle kryptografialle neljästä syystä. [2] Ensinnäkin, tietyntyyppisiin sovelluksiin on vain rajoitettu määrä kryptografisia järjestelmiä. Esimerkiksi useimmat nykyaikaiset symmetrisen salauksen sovellukset käyttävät Rijndael-salausalgoritmia. Joten salaisuutesi järjestelmän suunnittelun suhteen on vain hyvin rajoitettu. Rijndael-salausalgoritmin jonkin yksityisen avaimen salassapitämisessä on kuitenkin paljon enemmän joustavuutta.

Toiseksi, jonkin tietostringin korvaaminen on helpompaa kuin koko kryptografisen järjestelmän korvaaminen. Oletetaan, että yrityksen kaikilla työntekijöillä on sama salausohjelmisto, ja että jokaisella kahdella työntekijällä on yksityinen avain luottamukselliseen viestintään. Avainten kompromissit ovat tässä skenaariossa hankalia, mutta ainakin yritys voisi säilyttää ohjelmiston tällaisten turvallisuusrikkomusten kanssa. Jos yritys luottaisi järjestelmän salaisuuteen, mikä tahansa sen salaisuuden rikkominen vaatisi kaiken ohjelmiston vaihtamista.

Kolmanneksi, Kerckhoffs’in periaate mahdollistaa standardoinnin ja yhteensopivuuden kryptografisten järjestelmien käyttäjien välillä. Tällä on valtavia etuja tehokkuuden kannalta. Esimerkiksi on vaikea kuvitella, kuinka miljoonat ihmiset voisivat turvallisesti yhdistää Google:n verkkopalvelimiin joka päivä, jos turvallisuus vaatisi kryptografisten järjestelmien salassapidon.

Neljänneksi, Kerckhoffin periaate mahdollistaa kryptografisten järjestelmien julkisen tarkastelun. Tämän tyyppinen tarkastelu on ehdottoman välttämätöntä turvallisten kryptografisten järjestelmien saavuttamiseksi. Havainnollistavasti, symmetrisen kryptografian pääalgoritmi, Rijndael-salausalgoritmi, oli kilpailun tulos, jonka järjesti National Institute of Standards and Technology vuosien 1997 ja 2000 välillä.

Mikä tahansa järjestelmä, joka yrittää saavuttaa **turvallisuutta obskuurisuuden avulla**, on sellainen, joka perustuu sen suunnittelun ja/tai toteutuksen yksityiskohtien salassapitoon. Kryptografiassa tämä olisi nimenomaan järjestelmä, joka perustuu kryptografisen järjestelmän suunnittelun yksityiskohtien salassapitoon. Joten turvallisuus obskuurisuuden avulla on suorassa ristiriidassa Kerckhoffs’in periaatteen kanssa.

Avoimuuden kyky vahvistaa laatua ja turvallisuutta ulottuu myös laajemmin digitaaliseen maailmaan kuin vain kryptografiaan. Vapaat ja avoimen lähdekoodin Linux-jakelut, kuten Debian, ovat yleensä useita etuja Windowsin ja MacOS:n vastineisiinsa nähden yksityisyyden, vakauden, turvallisuuden ja joustavuuden suhteen. Vaikka tähän voi olla useita syitä, tärkein periaate on todennäköisesti, kuten Eric Raymond ilmaisi kuuluisassa esseessään "The Cathedral and the Bazaar", että "tarpeeksi monilla silmillä kaikki bugit ovat matalia.” [3] Se on tämä joukon viisaus -tyyppinen periaate, joka antoi Linuxille sen merkittävimmän menestyksen.
Kryptografista järjestelmää ei voi koskaan yksiselitteisesti julistaa "turvalliseksi" tai "turvattomaksi". Sen sijaan on olemassa erilaisia turvallisuuden käsitteitä kryptografisille järjestelmille. Jokaisen **kryptografisen turvallisuuden määritelmän** on määriteltävä (1) turvallisuustavoitteet sekä (2) hyökkääjän kyvyt. Kryptografisten järjestelmien analysointi yhtä tai useampaa tiettyä turvallisuuskäsitettä vasten tarjoaa näkemyksiä niiden sovelluksista ja rajoituksista.
Vaikka emme syvenny kaikkien erilaisten kryptografisen turvallisuuden käsitteiden yksityiskohtiin, sinun tulisi tietää, että kaksi oletusta on kaikkialla läsnä kaikissa moderneissa kryptografisen turvallisuuden käsitteissä, jotka liittyvät symmetrisiin ja asymmetrisiin järjestelmiin (ja jossain muodossa myös muihin kryptografisiin primitiiveihin):

* Hyökkääjän tietämys järjestelmästä noudattaa Kerckhoffs’in periaatetta.
* Hyökkääjä ei voi käytännössä suorittaa brute force -hyökkäystä järjestelmään. Erityisesti kryptografisen turvallisuuden uhkamallit eivät tyypillisesti edes salli brute force -hyökkäyksiä, koska oletetaan, että ne eivät ole relevantti huolenaihe.

**Huomautuksia:**

[1] Seutoniuksen mukaan Julius Caesar käytti sotilasviestinnässään siirtosalakirjoitusta, jossa avaimen vakioarvo oli 3. Joten A muuttui aina D:ksi, B aina E:ksi, C aina F:ksi, ja niin edelleen. Tämä siirtosalakirjoituksen versio on siten tullut tunnetuksi **Caesarin salakirjoituksena** (vaikka se ei modernissa merkityksessä olekaan oikeastaan salakirjoitus, koska avaimen arvo on vakio). Caesarin salakirjoitus saattoi olla turvallinen ensimmäisellä vuosisadalla eaa., jos Rooman viholliset olivat hyvin epätietoisia salakirjoituksesta. Mutta se ei selvästikään olisi kovin turvallinen järjestelmä nykyaikana.

[2] Jonathan Katz ja Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), s. 7f.

[3] Eric Raymond, “The Cathedral and the Bazaar,” esitelmä pidettiin Linux Kongressissa, Würzburg, Saksa (27. toukokuuta 1997). Saatavilla on useita myöhempiä versioita sekä kirja. Lainaukseni ovat kirjan sivulta 30: Eric Raymond, _The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary_, uudistettu painos (2001), O’Reilly: Sebastopol, CA.

## Virtasalakirjoitukset
<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>

Symmetriset salausjärjestelmät jaetaan yleensä kahteen tyyppiin: **virtasalakirjoitukset** ja **lohkosalakirjoitukset**. Tämä erottelu on kuitenkin hieman ongelmallinen, koska ihmiset käyttävät näitä termejä epäjohdonmukaisesti. Seuraavissa osioissa esitän erottelun tavalla, joka mielestäni on paras. Sinun tulisi kuitenkin olla tietoinen siitä, että monet ihmiset käyttävät näitä termejä eri tavalla kuin minä esitän.

Katsotaan ensin virtasalakirjoituksia. **Virtasalakirjoitus** on symmetrinen salausjärjestelmä, jossa salaus koostuu kahdesta vaiheesta.

Ensinnäkin, yksityisen avaimen avulla tuotetaan merkkijono, joka on yhtä pitkä kuin alkuperäinen teksti. Tätä merkkijonoa kutsutaan **avainvirraksi**.

Seuraavaksi avainvirta yhdistetään matemaattisesti alkuperäiseen tekstiin tuottaakseen salatun tekstin. Tämä yhdistäminen on tyypillisesti XOR-operaatio. Salaamisen purkamiseksi voit vain kääntää operaation. (Huomaa, että $A \oplus B = B \oplus A$, tapauksessa $A$ ja $B$ ovat bittijonoja. Joten XOR-operaation järjestyksellä ei ole merkitystä tuloksen kannalta. Tätä ominaisuutta kutsutaan **vaihdannaisuudeksi**.)
Tyypillinen XOR-virtasalaus on esitetty *Kuvassa 3*. Ensin otat yksityisen avaimen $K$ ja käytät sitä avainvirran luomiseen. Avainvirta yhdistetään sitten avoimen tekstin kanssa XOR-operaation avulla tuottaen salatun tekstin. Mikä tahansa agentti, joka vastaanottaa salatun tekstin, voi helposti purkaa sen, jos hänellä on avain $K$. Kaiken mitä hänen tarvitsee tehdä, on luoda avainvirta yhtä pitkä kuin salattu teksti noudattaen kaavan määriteltyä menettelyä ja XORata se salatun tekstin kanssa.

*Kuva 3: XOR-virtasalaus*

![Kuva 3: XOR-virtasalaus](assets/Figure4-3.webp "Kuva 3: XOR-virtasalaus")

Muistutuksena, salauskaava on tyypillisesti malli salaukselle samalla ydinalgoritmilla, eikä tarkka määrittely. Laajennettuna, virtasalaus on tyypillisesti malli salaukselle, jossa voit käyttää eri pituisia avaimia. Vaikka avaimen pituus voi vaikuttaa joihinkin kaavan pieniin yksityiskohtiin, se ei vaikuta sen olennaiseen muotoon.

Siirtosalaus on esimerkki hyvin yksinkertaisesta ja turvattomasta virtasalauksesta. Käyttämällä yhtä kirjainta (yksityinen avain), voit tuottaa kirjainjonon viestin pituuden mukaisesti (avainvirta). Tämä avainvirta yhdistetään sitten avoimen tekstin kanssa modulo-operaation avulla tuottaen salatun tekstin. (Tämä modulo-operaatio voidaan yksinkertaistaa XOR-operaatioksi, kun esitetään kirjaimet bitteinä).

Toinen kuuluisa esimerkki virtasalauksesta on **Vigenèren salaus**, joka on nimetty Blaise de Vigenèren mukaan, joka kehitti sen loppuun 1500-luvun lopulla (vaikka muut olivat tehneet paljon ennakkotyötä). Se on esimerkki **polyalfabeettisesta substituutiosalauksesta**: salauskaavasta, jossa salatun tekstin aakkosto muuttuu avoimen tekstin symbolin sijainnin mukaan tekstissä. Toisin kuin monoalfabeettisessa substituutiosalauksessa, salatun tekstin symbolit voidaan yhdistää useampaan kuin yhteen avoimen tekstin symboliin.

Kun salaus alkoi yleistyä renessanssin Euroopassa, myös **kryptanalyysi**—eli salattujen tekstien murtaminen—erityisesti käyttäen **taajuusanalyysiä**, tuli suosituksi. Jälkimmäinen hyödyntää kielellisiä tilastollisia säännönmukaisuuksia salattujen tekstien murtamiseen, ja sen keksivät arabialaiset tutkijat jo yhdeksännellä vuosisadalla. Se on tekniikka, joka toimii erityisen hyvin pitkien tekstien kanssa. Ja jopa kaikkein kehittyneimmät monoalfabeettiset substituutiosalaukset eivät enää olleet riittäviä taajuusanalyysiä vastaan 1700-luvulla Euroopassa, erityisesti sotilaallisissa ja turvallisuusympäristöissä. Koska Vigenèren salaus tarjosi merkittävän edistysaskeleen turvallisuudessa, se tuli suosituksi tällä aikakaudella ja oli laajalle levinnyt 1700-luvun loppuun mennessä.

Epämuodollisesti puhuen, salauskaava toimii seuraavasti:

1. Valitse monikirjaiminen sana yksityiseksi avaineksi.
2. Sovella jokaiseen viestin kirjaimeen siirtosalausta käyttäen vastaavaa avainsanan kirjainta siirtona.
3. Jos olet käynyt läpi avainsanan, mutta et ole vielä täysin salannut avointa tekstiä, sovella uudelleen avainsanan kirjaimia siirtosalauksena vastaaviin kirjaimiin tekstissä.
4. Jatka tätä prosessia, kunnes koko viesti on salattu.

Kuvitellaan, että yksityinen avain on "GOLD" ja haluat salata viestin "CRYPTOGRAPHY". Tässä tapauksessa edetään seuraavasti Vigenèren salauksen mukaisesti:

- $c_0  = [(2 + 6) \mod 26] = 8 = I$
- $c_1  = [(17 + 14) \mod 26] = 5 = F$
- $c_2  = [(24 + 11) \mod 26] = 9 = J$
- $c_3 = [(15 + 3) \mod 26] = 18 = S$
- $c_4 = [(19 + 6) \mod 26] = 25 = Z$
- $c_5 = [(14 + 14) \mod 26] = 2 = C$
- $c_6 = [(6 + 11) \mod 26] = 17 = R$
- $c_7 = [(17 + 3) \mod 26] = 20 = U$
- $c_8 = [(0 + 6) \mod 26] = 6 = G$
- $c_9 = [(15 + 14) \mod 26] = 3 = D$
- $c_{10} = [(7 + 11) \mod 26] = 18 = S$
- $c_{11} = [(24 + 3) \mod 26] = 1 = B$

Näin ollen salakirjoitus $c$ = "IFJSZCRUGDSB".

Toinen kuuluisa esimerkki virtasalauksesta on **kertakäyttöavain**. Kertakäyttöavaimen kanssa luot vain satunnaisbittejä sisältävän merkkijonon, joka on yhtä pitkä kuin alkuperäinen viesti, ja tuotat salakirjoituksen XOR-operaation avulla. Näin ollen yksityinen avain ja avainvirta ovat samat kertakäyttöavaimessa.

Vaikka siirtosalakirjoitus ja Vigenèren salakirjoitukset ovat hyvin turvattomia nykyaikana, kertakäyttöavain on erittäin turvallinen, jos sitä käytetään oikein. Todennäköisesti kuuluisin kertakäyttöavaimen sovellus oli, ainakin 1980-luvulle asti, **Washingtonin ja Moskovan suora yhteys**.

Yhteys on suora viestintälinkki Washingtonin ja Moskovan välillä kiireellisiä asioita varten, joka asennettiin Kuuban ohjuskriisin jälkeen. Teknologia yhteydelle on muuttunut vuosien varrella. Nykyään se sisältää suoran kuituoptisen kaapelin sekä kaksi satelliittilinkkiä (redundanssin vuoksi), jotka mahdollistavat sähköpostin ja tekstiviestien lähettämisen. Linkki päättyy eri paikkoihin Yhdysvalloissa. Pentagon, Valkoinen talo ja Raven Rock Mountain ovat tunnettuja päätepisteitä. Toisin kuin yleisesti luullaan, yhteys ei ole koskaan sisältänyt puhelimia.

Kertakäyttöavainjärjestelmä toimi periaatteessa seuraavasti. Sekä Washingtonilla että Moskovalla oli kaksi sarjaa satunnaislukuja. Yksi satunnaislukujen sarja, jonka venäläiset loivat, liittyi minkä tahansa viestin salaamiseen ja purkamiseen venäjän kielellä. Toinen satunnaislukujen sarja, jonka amerikkalaiset loivat, liittyi minkä tahansa viestin salaamiseen ja purkamiseen englannin kielellä. Ajoittain lisää satunnaislukuja toimitettiin toiselle puolelle luotettujen lähettien kautta.

Washington ja Moskova pystyivät sitten kommunikoimaan salaisesti käyttämällä näitä satunnaislukuja luomaan kertakäyttöavaimia. Joka kerta, kun tarvitsit kommunikoida, käyttäisit seuraavaa satunnaislukujen osaa viestillesi.

Vaikka kertakäyttöavain on erittäin turvallinen, sillä on merkittäviä käytännön rajoituksia: avaimen on oltava yhtä pitkä kuin viesti, eikä kertakäyttöavaimen osaa voi käyttää uudelleen. Tämä tarkoittaa, että sinun on pidettävä kirjaa siitä, missä kohtaa kertakäyttöavainta olet, säilytettävä valtava määrä bittejä ja vaihdettava satunnaisbittejä vastapuoliesi kanssa ajoittain. Seurauksena kertakäyttöavainta ei usein käytetä käytännössä.

Sen sijaan käytännössä yleisesti käytetyt virtasalaukset ovat **pseudosatunnaisia virtasalauksia**. Salsa20 ja sen läheinen variantti ChaCha ovat esimerkkejä yleisesti käytetyistä pseudosatunnaisista virtasalauksista.
Näissä pseudosatunnaisissa virtasalauksissa valitset ensin satunnaisesti avaimen $K$, joka on lyhyempi kuin avoimen tekstin pituus. Tällainen satunnainen avain $K$ luodaan yleensä tietokoneellamme ennakoimattomien tietojen perusteella, joita se kerää ajan mittaan, kuten verkko-viestien väliset ajat, hiiren liikkeet ja niin edelleen.
Tämä satunnainen avain $K$ syötetään sitten laajennusalgoritmiin, joka luo pseudosatunnaisen avainvirran yhtä pitkänä kuin viesti. Voit määrittää tarkalleen, kuinka pitkän avainvirran tarvitset (esim. 500 bittiä, 1000 bittiä, 1200 bittiä, 29 117 bittiä ja niin edelleen).

Pseudosatunnainen avainvirta vaikuttaa *siltä kuin* se olisi valittu täysin satunnaisesti kaikkien saman pituisten merkkijonojen joukosta. Siksi salaus pseudosatunnaisella avainvirralla näyttää siltä, kuin se olisi tehty kertakäyttöisellä salasanalla. Mutta näin ei tietenkään ole.

Koska yksityinen avaimemme on lyhyempi kuin avainvirta ja laajennusalgoritmimme on oltava deterministinen, jotta salaus/purku-prosessi toimisi, kaikki kyseisen pituiset avainvirrat eivät olisi voineet syntyä laajennustoimintomme tuloksena.

Oletetaan esimerkiksi, että yksityisellä avaimellamme on pituus 128 bittiä ja että voimme syöttää sen laajennusalgoritmiin luodaksemme paljon pidemmän avainvirran, sanokaamme 2 500 bittiä. Koska laajennusalgoritmimme on oltava deterministinen, algoritmimme voi korkeintaan valita $1/2^{128}$ merkkijonoa, joiden pituus on 2 500 bittiä. Joten tällainen avainvirta ei voisi koskaan valita täysin satunnaisesti kaikista saman pituisista merkkijonoista.

Virtasalauksen määritelmässämme on kaksi näkökohtaa: (1) yksityisen avaimen avulla luodaan avainvirta, joka on yhtä pitkä kuin avoin teksti; ja (2) tämä avainvirta yhdistetään avoimeen tekstiin, tyypillisesti XOR-operaation kautta, tuottaen salatun tekstin.

Joskus ihmiset määrittelevät ehtoa (1) tiukemmin, väittäen, että avainvirran on nimenomaan oltava pseudosatunnainen. Tämä tarkoittaa, että ei sekä siirtosalauksia että kertakäyttöisiä salasanoja pidettäisi virtasalauksina.

Mielestäni ehdolle (1) antaminen laajempi määritelmä tarjoaa helpomman tavan järjestää salausjärjestelmiä. Lisäksi se tarkoittaa, että meidän ei tarvitse lopettaa tietyn salausjärjestelmän kutsumista virtasalaukseksi vain siksi, että opimme sen ei itse asiassa perustuvan pseudosatunnaisiin avainvirtoihin.

**Huomautukset:**

[4] Crypto Museum, "Washington-Moscow hotline," 2013, saatavilla osoitteessa [https://www.cryptomuseum.com/crypto/hotline/index.htm](https://www.cryptomuseum.com/crypto/hotline/index.htm).

## Lohkosalaus
<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>

Ensimmäinen tapa, jolla **lohkosalausta** yleisesti ymmärretään, on jotain primitiivisempää kuin virtasalaus: Perusalgoritmi, joka suorittaa pituutta säilyttävän muunnoksen sopivan pituiselle merkkijonolle avaimen avulla. Tätä algoritmia voidaan käyttää luomaan salausjärjestelmiä ja ehkä muita kryptografisia järjestelmiä.
Usein lohkosalaus voi ottaa syötteenä eri pituisia merkkijonoja, kuten 64, 128 tai 256 bittiä, sekä eri pituisia avaimia, kuten 128, 192 tai 256 bittiä. Vaikka algoritmin jotkin yksityiskohdat saattavat muuttua näiden muuttujien mukaan, ydin algoritmi ei muutu. Jos se muuttuisi, puhuisimme kahdesta eri lohkosalauksesta. Huomaa, että ydin algoritmin terminologiaa käytetään tässä samalla tavalla kuin salausjärjestelmissä.

Kuvaus siitä, miten lohkosalaus toimii, voidaan nähdä alla olevassa *Kuva 4:ssä*. Viesti $M$ pituudeltaan $L$ ja avain $K$ toimivat syötteinä lohkosalaukselle. Se tuottaa viestin $M'$ pituudeltaan $L$. Avaimen ei välttämättä tarvitse olla samaa pituutta kuin $M$ ja $M'$ useimmissa lohkosalausmenetelmissä.

*Kuva 4: Lohkosalaus*

![Kuva 4: Lohkosalaus](assets/Figure4-4.webp "Kuva 4: Lohkosalaus")

Lohkosalaus itsessään ei ole salausjärjestelmä. Mutta lohkosalausta voidaan käyttää erilaisten **toimintatapojen** kanssa tuottamaan erilaisia salausjärjestelmiä. Toimintatapa lisää vain joitakin lisäoperaatioita lohkosalauksen ulkopuolelle.

Kuvitellaan, että lohkosalaus (BC), joka vaatii 128-bittisen syötteen ja 128-bittisen yksityisen avaimen. Alla oleva kuva 5 näyttää, miten kyseistä lohkosalausta voidaan käyttää **elektronisen koodikirjan tilassa** (**ECB-tila**) luomaan salausjärjestelmä. (Oikealla olevat ellipsit osoittavat, että voit toistaa tämän kaavan tarpeen mukaan).

*Kuva 5: Lohkosalaus ECB-tilassa*

![Kuva 5: Lohkosalaus ECB-tilassa](assets/Figure4-5.webp "Kuva 5: Lohkosalaus ECB-tilassa")

Elektronisen koodikirjan salauksen prosessi lohkosalauksen kanssa on seuraava. Katso, voitko jakaa tekstimuotoisen viestisi 128-bittisiin lohkoihin. Jos et, lisää **täytettä** viestiin, jotta tulos voidaan jakaa tasaisesti 128 bitin lohkokokoon. Tämä on tietosi, jota käytetään salausprosessissa.

Jaa nyt tiedot 128-bittisiin merkkijonoihin ($M_1$, $M_2$, $M_3$, ja niin edelleen). Aja jokainen 128-bittinen merkkijono lohkosalauksen läpi 128-bittisellä avaimellasi tuottaaksesi 128-bittisiä salatun tekstin paloja ($C_1$, $C_2$, $C_3$, ja niin edelleen). Nämä palaset, kun ne yhdistetään uudelleen, muodostavat koko salatun tekstin.

Salauksen purku on vain käänteinen prosessi, vaikka vastaanottajan on löydettävä tunnistettava tapa poistaa mahdollinen täyte salatusta datasta tuottaakseen alkuperäisen tekstimuotoisen viestin.

Vaikka suhteellisen yksinkertainen, lohkosalaus elektronisen koodikirjan tilassa puuttuu turvallisuudesta. Tämä johtuu siitä, että se johtaa **deterministiseen salaukseen**. Kaksi identtistä 128-bittistä datan palasta salataan täsmälleen samalla tavalla. Tätä tietoa voidaan hyödyntää.

Sen sijaan, mikä tahansa lohkosalauksesta rakennettu salausjärjestelmä tulisi olla **probabilistinen**: eli minkä tahansa viestin $M$, tai minkä tahansa tietyn $M$:n palan, salauksen tulisi yleensä tuottaa erilainen tulos joka kerta. [5]

**Lohkoketjutila** (**CBC-tila**) on todennäköisesti yleisin tila, jota käytetään lohkosalauksen kanssa. Yhdistelmä, jos se tehdään oikein, tuottaa probabilistisen salausjärjestelmän. Voit nähdä tämän toimintatavan kuvauksen alla olevassa *Kuvassa 6*.

*Kuva 6: Lohkosalaus CBC-tilassa*
![Kuva 6: Lohkosalaus CBC-tilassa](assets/Figure4-6.webp "Kuva 6: Lohkosalaus CBC-tilassa")
Oletetaan, että lohkon koko on jälleen 128 bittiä. Aloittaaksesi tarvitset jälleen varmistaa, että alkuperäinen selkotekstiviestisi saa tarvittavan täytteen.

Sitten XORaat ensimmäisen 128-bittisen osan selkotekstistäsi **alkuarvovektorin** kanssa, joka on 128 bittiä. Tulos asetetaan lohkosalaukseen tuottaakseen salatun tekstin ensimmäiselle lohkolle. Toiselle 128-bittiselle lohkolle XORaat ensin selkotekstin ensimmäisen lohkon salatun tekstin kanssa, ennen kuin syötät sen lohkosalaukseen. Jatkat tätä prosessia, kunnes olet salannut koko selkotekstiviestisi.

Kun olet valmis, lähetät salatun viestin yhdessä salaamattoman alkuarvovektorin kanssa vastaanottajalle. Vastaanottajan on tiedettävä alkuarvovektori, muuten hän ei voi purkaa salattua tekstiä.

Tämä rakenne on paljon turvallisempi kuin elektroninen koodikirja-tila, kun sitä käytetään oikein. Sinun tulisi ensin varmistaa, että alkuarvovektori on satunnainen tai pseudosatunnainen merkkijono. Lisäksi sinun tulisi käyttää eri alkuarvovektoria joka kerta, kun käytät tätä salausskeemaa.

Toisin sanoen, alkuarvovektorisi tulisi olla satunnainen tai pseudosatunnainen kertakäyttönumero, missä **kertakäyttönumero** tarkoittaa "numeroa, jota käytetään vain kerran". Jos pidät kiinni tästä käytännöstä, niin CBC-tila lohkosalauksessa varmistaa, että samat identtiset selkotekstilohkot salataan yleensä eri tavoin joka kerta.

Lopuksi kiinnitetään huomiota **lähtötiedon palautetilaan** (**OFB-tila**). Voit nähdä tämän tilan esityksen *Kuvassa 7*.

*Kuva 7: Lohkosalaus OFB-tilassa*

![Kuva 7: Lohkosalaus OFB-tilassa](assets/Figure4-7.webp "Kuva 7: Lohkosalaus OFB-tilassa")

OFB-tilassa valitset myös alkuarvovektorin. Mutta tässä, ensimmäiselle lohkolle, alkuarvovektori syötetään suoraan lohkosalaukseen avaimellasi. Tuloksena olevat 128 bittiä käsitellään sitten avainvirrana. Tämä avainvirta XORataan selkotekstin kanssa tuottaakseen salatun tekstin lohkolle. Seuraaville lohkoille käytät edellisen lohkon avainvirtaa syötteenä lohkosalaukseen ja toistat vaiheet.

Jos tarkastelet huolellisesti, mitä OFB-tilassa lohkosalauksella on itse asiassa luotu, on virtasalaus. Generoit avainvirran osia 128 bittiä kerrallaan, kunnes sinulla on selkotekstin pituus (hyläten tarpeettomat bitit viimeisestä 128-bittisestä avainvirran osasta). Sitten XORaat avainvirran selkotekstiviestisi kanssa saadaksesi salatun tekstin.

Edellisessä osiossa virtasalauksista mainitsin, että avainvirta tuotetaan yksityisen avaimen avulla. Tarkalleen ottaen, sitä ei tarvitse luoda vain yksityisellä avaimella. Kuten OFB-tilassa näet, avainvirta tuotetaan sekä yksityisen avaimen että alkuarvovektorin tuella.

Huomaa, että kuten CBC-tilassa, on tärkeää valita pseudosatunnainen tai satunnainen kertakäyttönumero alkuarvovektoriksi joka kerta, kun käytät lohkosalauksessa OFB-tilaa. Muuten sama 128-bittinen viestijono lähetettynä eri viestinnöissä salataan samalla tavalla. Tämä on yksi tapa luoda todennäköisyyspohjainen salaus virtasalauksella.
Jotkin virtasalaukset käyttävät vain yksityistä avainta luodakseen avainvirran. Näiden virtasalauksien kohdalla on tärkeää, että käytät satunnaista nonce-arvoa valitaksesi yksityisen avaimen jokaiseen kommunikaatioinstanssiin. Muuten näiden virtasalauksien salauksen tulokset ovat myös deterministisiä, mikä johtaa turvallisuusongelmiin.
Suosituin nykyaikainen lohkosalaus on **Rijndael-salaus**. Se oli voittaja viidestätoista ehdotuksesta kilpailussa, jonka National Institute of Standards and Technology (NIST) järjesti vuosien 1997 ja 2000 välillä korvaamaan vanhemman salausstandardin, **data encryption standard** (**DES**).

Rijndael-salausta voidaan käyttää eri määrittelyillä avainten pituuksille ja lohkokooille, sekä eri toimintatiloissa. NIST-kilpailun komitea hyväksyi rajoitetun version Rijndael-salauksesta—nimittäin sellaisen, joka vaatii 128-bittiset lohkokoot ja avainten pituudet joko 128 bittiä, 192 bittiä tai 256 bittiä—osana **advanced encryption standard** (**AES**). Tämä on todella päästandardi symmetrisille salaussovelluksille. Se on niin turvallinen, että jopa NSA on ilmeisesti valmis käyttämään sitä 256-bittisillä avaimilla huippusalaisiin asiakirjoihin. [6]

AES-lohkosalauksesta kerrotaan yksityiskohtaisesti *Luvussa 5*.

**Huomautukset:**

[5] Probabilistisen salauksen tärkeys korostettiin ensimmäisen kerran Shafi Goldwasserin ja Silvio Micalin toimesta, “Probabilistic encryption,” _Journal of Computer and System Sciences_, 28 (1984), 270–99.

[6] Katso NSA, "Commercial National Security Algorithm Suite", [https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm](https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm).

## Selventämässä sekaannusta
<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>

Sekaannus lohko- ja virtasalauksien välillä syntyy, koska joskus ihmiset ymmärtävät termiä lohkosalauksen viittaavan nimenomaan *lohkosalausmenetelmään, jossa käytetään lohkomoodin salausta*.

Harkitse edellisessä osiossa mainittuja ECB- ja CBC-moodeja. Nämä nimenomaan vaativat, että salattavan datan on oltava jaollinen lohkon koon mukaan (tämä saattaa tarkoittaa, että alkuperäiseen viestiin on käytettävä täytettä). Lisäksi näissä moodeissa dataa käsitellään suoraan lohkosalauksella (eikä vain yhdistetä lohkosalauksen tulokseen kuten OFB-moodissa).

Vaihtoehtoisesti voit määritellä **lohkosalauksen** minä tahansa salausjärjestelmänä, joka käsittelee kiinteän pituisia viestin lohkoja kerrallaan (missä mikä tahansa lohko on pidempi kuin tavu, muuten se muuttuu virtasalaukseksi). Sekä salattavan datan että salatun tekstin on jaettava tasaisesti tähän lohkokokoon. Tyypillisesti lohkon koko on 64, 128, 192 tai 256 bittiä pitkä. Sen sijaan virtasalauksella voidaan salata viestejä yhden bitin tai tavun kokoisissa paloissa kerrallaan.

Tällä tarkemmalla lohkosalauksen ymmärtämisellä voit todellakin väittää, että nykyaikaiset salausjärjestelmät ovat joko virta- tai lohkosalauksia. Tästä lähtien käytän termiä lohkosalauksen yleisemmässä merkityksessä, ellei toisin mainita.
Edellisessä osiossa käyty keskustelu OFB-tilasta nosti esiin myös toisen mielenkiintoisen seikan. Jotkut virtasalaukset on rakennettu lohkosalausten pohjalta, kuten Rijndael OFB:n kanssa. Toiset, kuten Salsa20 ja ChaCha, eivät ole lohkosalausten pohjalta luotuja. Jälkimmäisiä voitaisiin kutsua **primitiivisiksi virtasalauksiksi**. (Tälle virtasalausten tyypille ei oikeastaan ole vakiintunutta termiä.)

Kun ihmiset puhuvat virta- ja lohkosalausten eduista ja haitoista, he vertaavat tyypillisesti primitiivisiä virtasalauksia lohkosalausten pohjalta luotuihin salausjärjestelmiin.

Vaikka virtasalauksen voi aina helposti rakentaa lohkosalausta käyttäen, on tyypillisesti erittäin vaikeaa rakentaa jonkinlainen rakenne lohkosalaustilan (kuten CBC-tilan) avulla primitiivisestä virtasalauksesta.

Tästä keskustelusta sinun tulisi nyt ymmärtää *Kuva 8*. Se tarjoaa yleiskatsauksen symmetrisistä salausjärjestelmistä. Käytämme kolmea salausjärjestelmän tyyppiä: primitiiviset virtasalaukset, lohkosalaus virtasalaukset ja lohkosalaustilassa olevat lohkosalaukset (kutsutaan myös "lohkosalauksiksi" kaaviossa).

*Kuva 8: Yleiskatsaus symmetrisistä salausjärjestelmistä*

![Kuva 8: Yleiskatsaus symmetrisistä salausjärjestelmistä](assets/Figure4-8.webp "Kuva 8: Yleiskatsaus symmetrisistä salausjärjestelmistä")


## Viestien autentikointikoodit
<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>

Salaus liittyy salaisuuden säilyttämiseen. Mutta kryptografia käsittelee myös laajempia teemoja, kuten viestin eheys, aitouden ja kiistämättömyyden. Niin sanotut **viestien autentikointikoodit** (MAC) ovat symmetrisiä kryptografisia järjestelmiä, jotka tukevat aitoutta ja eheyttä viestinnässä.

Miksi pelkkä salaisuus ei riitä viestinnässä? Oletetaan, että Bob lähettää Alicelle viestin käyttäen käytännössä murtamatonta salausta. Mikä tahansa hyökkääjä, joka keskeyttää tämän viestin, ei pysty saamaan merkittäviä oivalluksia sisällöstä. Kuitenkin hyökkääjällä on edelleen ainakin kaksi muuta hyökkäysvektoria käytettävissään:

1. Hän voisi keskeyttää salatun viestin, muuttaa sen sisältöä ja lähettää muutetun salatun viestin Alicelle.
2. Hän voisi estää Bobin viestin kokonaan ja lähettää oman luomansa salatun viestin.

Molemmissa tapauksissa hyökkääjällä ei ehkä ole mitään käsitystä salattujen viestien (1) ja (2) sisällöstä. Mutta hän voisi silti aiheuttaa merkittävää vahinkoa tällä tavalla. Tässä kohtaa viestien autentikointikoodit tulevat tärkeiksi.

Viestien autentikointikoodit määritellään löyhästi symmetrisiksi kryptografisiksi järjestelmiksi, joilla on kolme algoritmia: avaimen luontialgoritmi, tagin luontialgoritmi ja varmennusalgoritmi. Turvallinen MAC varmistaa, että tagit ovat **eksistentiaalisesti väärentämättömiä** mille tahansa hyökkääjälle – toisin sanoen, he eivät voi onnistuneesti luoda tagia viestiin, joka varmennetaan, elleivät he omaa yksityistä avainta.

Bob ja Alice voivat torjua tietyn viestin manipuloinnin käyttämällä MACia. Oletetaan hetkeksi, että he eivät välitä salaisuudesta. He haluavat vain varmistaa, että Alicen vastaanottama viesti oli todellakin Bobilta eikä sitä ole muutettu millään tavalla.

Prosessi on kuvattu *Kuvassa 9*. Käyttääkseen **MACia** (Message Authentication Code), heidän tulisi ensin luoda yksityinen avain $K$, joka on jaettu heidän kesken. Bob luo tagin $T$ viestille käyttäen yksityistä avainta $K$. Hän lähettää sitten viestin sekä viestitagin Alicelle. Hän voi sitten varmistaa, että Bob todella teki tagin, suorittamalla yksityisen avaimen, viestin ja tagin läpi varmennusalgoritmin.

*Kuva 9: Yleiskatsaus symmetrisistä salausjärjestelmistä*
![Kuva 9: Yleiskatsaus symmetrisiin salausjärjestelmiin](assets/Figure4-9.webp "Kuva 9: Yleiskatsaus symmetrisiin salausjärjestelmiin")
Johtuen **eksistentiaalisesta väärentämättömyydestä**, hyökkääjä ei voi muuttaa viestiä $M$ millään tavalla tai luoda omaa viestiään kelvollisella tagilla. Näin on, vaikka hyökkääjä havainnoisi monien viestien tageja Bobin ja Alicen välillä, jotka käyttävät samaa yksityistä avainta. Korkeintaan hyökkääjä voisi estää Alicen vastaanottamasta viestiä $M$ (ongelma, johon kryptografia ei voi puuttua).

MAC takaa, että viesti on todellakin luotu Bobin toimesta. Tämä aitouden takaaminen merkitsee automaattisesti viestin eheyttä—eli, jos Bob on luonut jonkin viestin, niin, ipso facto, sitä ei ole millään tavalla muutettu hyökkääjän toimesta. Joten tästä eteenpäin, kaikki huoli autentikoinnista tulisi automaattisesti ymmärtää huoleksi eheydestä.

Vaikka olen tehnyt eron viestin aitouden ja eheyden välillä keskustelussani, on myös yleistä käyttää näitä termejä synonyymeinä. Ne viittaavat silloin ajatukseen viesteistä, jotka on sekä luotu tietyn lähettäjän toimesta että eivät ole millään tavalla muuttuneet. Tässä hengessä viestien autentikointikoodeja kutsutaan usein myös **viestien eheyskoodeiksi**.


## Autentikoitu salaus
<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>

Tyypillisesti haluaisit taata sekä salaisuuden että aitouden viestinnässä ja siksi salausjärjestelmiä ja MAC-järjestelmiä käytetään yleensä yhdessä.

**Autentikoitu salausjärjestelmä** on järjestelmä, joka yhdistää salauksen MAC:iin erittäin turvallisella tavalla. Erityisesti sen on täytettävä standardit eksistentiaaliselle väärentämättömyydelle sekä erittäin vahvalle salaisuuden käsitteelle, nimittäin sellaiselle, joka on vastustuskykyinen **valittuun salakirjoitushyökkäykseen**. [7]

Jotta salausjärjestelmä olisi vastustuskykyinen valittuun salakirjoitushyökkäykseen, sen on täytettävä **muuttumattomuuden** standardit: eli mikä tahansa salakirjoitetun tekstin muokkaus hyökkääjän toimesta pitäisi johtaa joko kelvottomaan salakirjoitukseen tai sellaiseen, joka purkautuu alkuperäiseen nähden merkityksettömään selväkieliseen tekstiin. [8]

Koska autentikoitu salausjärjestelmä varmistaa, että hyökkääjän luoma salakirjoitus on aina kelvoton (koska tagia ei vahvisteta), se täyttää standardit vastustuskyvylle valittuja salakirjoitushyökkäyksiä vastaan. Mielenkiintoisesti voidaan todistaa, että autentikoitu salausjärjestelmä voidaan aina luoda yhdistämällä eksistentiaalisesti väärentämätön MAC ja salausjärjestelmä, joka täyttää vähemmän vahvan turvallisuuden käsitteen, tunnettu nimellä **valittu-tekstihyökkäyksen turvallisuus**.

Emme syvenny kaikkiin yksityiskohtiin autentikoitujen salausjärjestelmien rakentamisesta. Mutta on tärkeää tietää kaksi yksityiskohtaa niiden rakenteesta.

Ensinnäkin, autentikoitu salausjärjestelmä käsittelee ensin salauksen ja luo sitten viestitagin salakirjoitukseen. Käy ilmi, että muut lähestymistavat—kuten salakirjoituksen yhdistäminen tagiin selväkielisessä tekstissä, tai ensin tagin luominen ja sitten sekä selväkielisen tekstin että tagin salaaminen—ovat turvattomia. Lisäksi, molemmilla toiminnoilla on oma satunnaisesti valittu yksityinen avaimensa, muuten turvallisuutesi on vakavasti vaarantunut.

Edellä mainittu periaate pätee yleisemmin: *sinun tulisi aina käyttää erillisiä avaimia yhdistäessäsi perus kryptografisia järjestelmiä*.

Autentikoitu salausjärjestelmä on esitetty *Kuvassa 10*. Bob luo ensin salakirjoituksen $C$ viestistä $M$ käyttäen satunnaisesti valittua avainta $K_C$. Hän luo sitten viestitagin $T$ ajamalla salakirjoituksen ja toisen satunnaisesti valitun avaimen $K_T$ läpi tagin generointialgoritmin. Sekä salakirjoitus että viestitag lähetetään Alicelle.
Alice tarkistaa ensin, onko tunniste kelvollinen annetun salatun viestin $C$ ja avaimen $K_T$ kanssa. Jos se on kelvollinen, hän voi sitten purkaa viestin käyttäen avainta $K_C$. Hän ei ainoastaan ole varma viestinnän erittäin vahvasta salassapidon tasosta, mutta hän myös tietää, että viestin on luonut Bob.
*Kuva 10: Todennettu salausjärjestelmä*

![Kuva 10: Todennettu salausjärjestelmä](assets/Figure4-10.webp "Kuva 10: Todennettu salausjärjestelmä")

Miten MAC:t luodaan? Vaikka MAC:eja voidaan luoda useilla menetelmillä, yleinen ja tehokas tapa luoda ne on käyttämällä **kryptografisia hajautusfunktioita**.

Esittelemme kryptografiset hajautusfunktiot tarkemmin *Luvussa 6*. Toistaiseksi riittää tietää, että **hajautusfunktio** on tehokkaasti laskettava funktio, joka ottaa syötteitä mielivaltaisesta koosta ja tuottaa kiinteän pituisia tulosteita. Esimerkiksi suosittu hajautusfunktio **SHA-256** (secure hash algorithm 256) tuottaa aina 256-bittisen tulosteen riippumatta syötteen koosta. Jotkin hajautusfunktiot, kuten SHA-256, ovat hyödyllisiä kryptografiassa.

Yleisin kryptografisen hajautusfunktion avulla tuotettu tunniste on **hajautusperusteinen viestin todennuskoodi** (HMAC). Prosessi on esitetty *Kuvassa 11*. Osapuoli tuottaa kaksi erillistä avainta yksityisestä avaimesta $K$, sisäisen avaimen $K_1$ ja ulkoisen avaimen $K_2$. Klarteksti $M$ tai salattu viesti $C$ hajautetaan yhdessä sisäisen avaimen kanssa. Tuloksena oleva $T'$ hajautetaan sitten ulkoisen avaimen kanssa tuottamaan viestin tunniste $T$.

HMAC:n luomiseen voidaan käyttää useita hajautusfunktioita. Yleisimmin käytetty hajautusfunktio on SHA-256.

*Kuva 11: HMAC*

![Kuva 11: HMAC](assets/Figure4-11.webp "Kuva 11: HMAC")

**Huomautukset:**

[7] Tässä osiossa käsitellyt tarkat tulokset ovat peräisin Katzista ja Lindellistä, sivut 131–47.

[8] Teknisesti valittujen salakirjoitustekstihyökkäysten määritelmä eroaa muokkaamattomuuden käsitteestä. Mutta voidaan osoittaa, että nämä kaksi turvallisuuden käsitettä ovat yhtäpitäviä.

## Turvalliset viestintäistunnot
<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>

Oletetaan, että kaksi osapuolta on viestintäistunnossa, joten he lähettävät useita viestejä edestakaisin.

Todennettu salausjärjestelmä mahdollistaa viestin vastaanottajan varmistaa, että viesti on luotu hänen kumppaninsa toimesta viestintäistunnossa (kunhan yksityinen avain ei ole vuotanut). Tämä toimii hyvin yksittäisen viestin kohdalla. Tyypillisesti kuitenkin kaksi osapuolta lähettää viestejä edestakaisin viestintäistunnossa. Ja tässä ympäristössä pelkkä todennettu salausjärjestelmä, kuten edellä kuvattu, jää lyhyeksi tarjoamaan turvallisuutta.

Pääsyy on, että todennettu salausjärjestelmä ei tarjoa mitään takeita siitä, että viesti oli todella myös lähetetty agentin toimesta viestintäistunnon aikana. Harkitse seuraavia kolmea hyökkäysvektoria:

1. **Toistohyökkäys**: Hyökkääjä lähettää uudelleen salatun viestin ja tunnisteen, jonka hän on kaapannut kahden osapuolen välillä aiemmin.
2. **Järjestyksen muuttamisen hyökkäys**: Hyökkääjä kaappaa kaksi viestiä eri aikoina ja lähettää ne vastaanottajalle käänteisessä järjestyksessä.
3. **Heijastushyökkäys**: Hyökkääjä havaitsee viestin, joka on lähetetty A:sta B:hen, ja lähettää myös sen viestin A:lle.

Vaikka hyökkääjällä ei ole tietoa salatusta viestistä eikä hän voi luoda väärennettyjä salattuja viestejä, yllä mainitut hyökkäykset voivat silti aiheuttaa merkittävää vahinkoa viestinnässä.
Oletetaan esimerkiksi, että tietty viesti kahden osapuolen välillä sisältää rahoitusvarojen siirron. Uudelleentoistohyökkäys saattaisi siirtää varat toisen kerran. Perusmuotoinen todennettu salausjärjestelmä ei tarjoa puolustusta tällaisia hyökkäyksiä vastaan.
Onneksi tällaiset hyökkäykset voidaan helposti estää viestintäistunnossa käyttämällä **tunnisteita** ja **suhteellisia aikaindikaattoreita**.

Tunnisteet voidaan lisätä salaamattomaan viestiin ennen salauksen lisäämistä. Tämä estäisi kaikki peilaushyökkäykset. Suhteellinen aikaindikaattori voi esimerkiksi olla sekvenssinumero tietyssä viestintäistunnossa. Kumpikin osapuoli lisää sekvenssinumeron viestiin ennen salauksen lisäämistä, joten vastaanottaja tietää, missä järjestyksessä viestit on lähetetty. Tämä poistaa viestien uudelleenjärjestelyn mahdollisuuden. Se myös eliminoi uudelleentoistohyökkäykset. Mikä tahansa viesti, jonka hyökkääjä lähettää linjan kautta, sisältää vanhan sekvenssinumeron, ja vastaanottaja tietää olla käsittelemättä viestiä uudelleen.

Kuvataksemme, miten turvalliset viestintäistunnot toimivat, oletetaan taas Alica ja Bob. He lähettävät yhteensä neljä viestiä edestakaisin. Voit nähdä, miten todennettu salausjärjestelmä tunnisteiden ja sekvenssinumeroiden kanssa toimisi alla *Kuvassa 11*.

Viestintäistunto alkaa Bobin lähettäessä salatun tekstin $C_{0,B}$ Alicelle viestitunnisteella $T_{0,B}$. Salattu teksti sisältää viestin sekä tunnisteen (BOB) että sekvenssinumeron (0). Tunniste $T_{0,B}$ on tehty koko salatun tekstin yli. Seuraavissa viestinnöissään Alice ja Bob ylläpitävät tätä protokollaa, päivittäen kenttiä tarpeen mukaan.

*Kuva 12: Turvallinen viestintäistunto*

![Kuva 12: Turvallinen viestintäistunto](assets/Figure4-12.webp "Kuva 12: Turvallinen viestintäistunto")

# RC4 ja AES
<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>

## RC4-virtasalaus
<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>

Tässä luvussa keskustelemme salausjärjestelmän yksityiskohdista, jossa käytetään modernia primitiivistä virtasalausta, RC4 (tai "Rivest cipher 4"), ja modernia lohkosalausta, AES. Vaikka RC4-salaus on menettänyt suosionsa salausmenetelmänä, AES on nykyaikaisen symmetrisen salauksen standardi. Nämä kaksi esimerkkiä antavat paremman käsityksen siitä, miten symmetrinen salaus toimii kulissien takana.

___

Jotta ymmärtäisimme, miten modernit pseudosatunnaiset virtasalaukset toimivat, keskityn RC4-virtasalaukseen. Se on pseudosatunnainen virtasalaus, jota on käytetty WEP- ja WAP-langattomien tukiasemien turvaprotokollissa sekä TLS:ssä. Koska RC4:llä on monia todistettuja heikkouksia, se on menettänyt suosionsa. Itse asiassa Internet Engineering Task Force kieltää nyt RC4-sarjojen käytön asiakas- ja palvelinsovelluksissa kaikissa TLS:n tapauksissa. Siitä huolimatta se toimii hyvin esimerkkinä siitä, miten primitiivinen virtasalaus toimii.

Aloitetaan ensin näyttämällä, miten salaamaton viesti salataan baby RC4 -salauksella. Oletetaan, että salaamaton viestimme on “SOUP.” Salaus baby RC4 -salauksellamme etenee sitten neljässä vaiheessa.

### Vaihe 1
Ensin määritellään taulukko **S** siten, että $S[0] = 0$ ja $S[7] = 7$. Tässä yhteydessä taulukko tarkoittaa muutettavissa olevaa arvojen kokoelmaa, joka on järjestetty indeksin mukaan, ja sitä kutsutaan joissakin ohjelmointikielissä (esim. Python) listaksi. Tässä tapauksessa indeksi kulkee 0:sta 7:ään, ja arvot kulkevat myös 0:sta 7:ään. Joten **S** on seuraavanlainen:
- $S = [0, 1, 2, 3, 4, 5, 6, 7]$

Tässä esitetyt arvot eivät ole ASCII-numeroita, vaan 1 tavun merkkijonojen desimaaliarvojen esityksiä. Joten arvo 2 olisi $0000 \ 0011$. Taulukon **S** pituus on siis 8 tavua.

### Vaihe 2

Toiseksi, määritellään avaintaulukko **K**, jonka pituus on 8 tavua valitsemalla avain 1:n ja 8 tavun väliltä (tavun murto-osia ei sallita). Koska jokainen tavu on 8 bittiä, voit valita minkä tahansa numeron väliltä 0 ja 255 kullekin avaimen tavulle.

Oletetaan, että valitsemme avaimemme **k** muodossa $[14, 48, 9]$, jolloin sen pituus on 3 tavua. Jokainen avaintaulukon indeksi asetetaan sitten kyseisen avainelementin desimaaliarvon mukaisesti järjestyksessä. Jos käyt läpi koko avaimen, aloita alusta, kunnes olet täyttänyt avaintaulukon 8 paikkaa. Näin ollen avaintaulukkomme on seuraavanlainen:

- $K = [14, 48, 9, 14, 48, 9, 14, 48]$

### Vaihe 3

Kolmanneksi muunnamme taulukon **S** käyttäen avaintaulukkoa **K** prosessissa, jota kutsutaan **avainohjelmoinniksi**. Prosessi on seuraavanlainen pseudokoodina:

- Luo muuttujat **j** ja **i**
- Aseta muuttuja $j = 0$
- Jokaiselle $i$:lle 0:sta 7:ään:
    - Aseta $j = (j + S[i] + K[i]) \mod 8$
    - Vaihda $S[i]$ ja $S[j]$

Taulukon **S** muunnos on esitetty *Taulukossa 1*.

Aloitettaessa näet **S**-taulukon alkutilan $[0, 1, 2, 3, 4, 5, 6, 7]$ ja **j**:n alkuarvon 0. Tämä muunnetaan käyttäen avaintaulukkoa $[14, 48, 9, 14, 48, 9, 14, 48]$.

For-silmukka alkaa $i = 0$:sta. Edellä mainitun pseudokoodin mukaan uusi **j**:n arvo tulee 6 ($j = (j + S[0] + K[0]) \mod 8 = (0 + 0 + 14) \mod 8 = 6 \mod 8$). Vaihdettaessa $S[0]$ ja $S[6]$, **S**-taulukon tila 1 kierroksen jälkeen tulee $[6, 1, 2, 3, 4, 5, 0, 7]$.
Seuraavalla rivillä, $i = 1$. Käydessämme for-silmukan läpi uudelleen, **j** saa arvon 7 ($j = (j + S[1] + K[1]) \mod 8 = (6 + 1 + 48) \mod 8 = 55 \mod 8 = 7 \mod 8$). Vaihtamalla $S[1]$ ja $S[7]$ nykyisestä **S**-tilasta, $[6, 1, 2, 3, 4, 5, 0, 7]$, saadaan tulokseksi $[6, 7, 2, 3, 4, 5, 0, 1]$ toisen kierroksen jälkeen.
Jatkamme tätä prosessia, kunnes tuotamme lopullisen rivin alimmaiseksi **S**-taulukkoon, $[6, 4, 1, 0, 3, 7, 5, 2]$.

*Table 1: Key scheduling table*

| Kierros | i   | j   |     | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| ------- | --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|         |     |     |     |      |      |      |      |      |      |      |      |
| Alkutila|     | 0   |     | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
| 1       | 0   | 6   |     | 6    | 1    | 2    | 3    | 4    | 5    | 0    | 7    |
| 2       | 1   | 7   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 3       | 2   | 2   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 4       | 3   | 3   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 5       | 4   | 3   |     | 6    | 7    | 2    | 0    | 3    | 5    | 4    | 1    |
| 6       | 5   | 6   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 1    |
| 7       | 6   | 1   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 2    |
| 8       | 7   | 2   |     | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    |

### Vaihe 4
Neljäntenä vaiheena tuotamme **avainvirran**. Tämä on pseudosatunnainen merkkijono, jonka pituus on yhtä suuri kuin lähetettävä viesti. Tätä käytetään alkuperäisen viestin "SOUP" salaamiseen. Koska avainvirran on oltava yhtä pitkä kuin viesti, tarvitsemme sellaisen, jossa on 4 tavua.
Avainvirta tuotetaan seuraavan pseudokoodin mukaisesti:

- Luo muuttujat **j**, **i** ja **t**.
- Aseta $j = 0$.
- Käy läpi jokainen $i$ tavutekstistä, alkaen $i = 1$ ja jatkaen $i = 4$:ään, jolloin jokainen avainvirran tavu tuotetaan seuraavasti:
    - $j = (j + S[i]) \mod 8$
    - Vaihda $S[i]$ ja $S[j]$.
    - $t = (S[i] + S[j]) \mod 8$
    - $i^{nnen}$ tavun avainvirta = $S[t]$

Voit seurata laskelmia *Taulukossa 2*.

**S**-taulukon alkutila on $S = [6, 4, 1, 0, 3, 7, 5, 2]$. Asetettaessa $i = 1$, **j**:n arvoksi tulee 4 ($j = (j + S[i]) \mod 8 = (0 + 4) \mod 8 = 4$). Vaihdamme sitten $S[1]$ ja $S[4]$ tuottaaksemme **S**-taulukon muutoksen toisella rivillä, $[6, 3, 1, 0, 4, 7, 5, 2]$. **t**:n arvoksi tulee sitten 7 ($t = (S[i] + S[j]) \mod 8 = (3 + 4) \mod 8 = 7$). Lopulta avainvirran tavu on $S[7]$, eli 2.

Jatkamme muiden tavujen tuottamista, kunnes meillä on seuraavat neljä tavua: 2, 6, 3 ja 7. Jokaista näistä tavuista voidaan sitten käyttää salaamaan jokainen tavutekstin kirjain, "SOUP".

Aloitettaessa, käyttäen ASCII-taulukkoa, voimme nähdä, että "SOUP" salattuna perustavien tavujonojen desimaaliarvoilla on "83 79 85 80". Yhdistettynä avainvirtaan "2 6 3 7" saadaan "85 85 88 87", mikä pysyy samana modulo 256 -operaation jälkeen. ASCII:ssa salattu teksti "85 85 88 87" on "UUXW".

Mitä tapahtuu, jos salattava sana olisi pidempi kuin **S**-taulukko? Tässä tapauksessa **S**-taulukko vain muuttuu yllä esitetyllä tavalla jokaista tavutekstin tavua **i** varten, kunnes meillä on avainvirran tavujen määrä yhtä suuri kuin tavutekstin kirjainten määrä.

*Taulukko 2: Avainvirran tuottaminen*

| i   | j   | t   | Avainvirta | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| --- | --- | --- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|     | 0   |     |           | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    || 1   | 4   | 7   | 2         | 6    | 3    | 1    | 0    | 4    | 7    | 5    | 2    |
| 2   | 5   | 0   | 6         | 6    | 3    | 7    | 0    | 4    | 1    | 5    | 2    |
| 3   | 5   | 1   | 3         | 6    | 3    | 7    | 1    | 4    | 0    | 5    | 2    |
| 4   | 1   | 7   | 2         | 6    | 4    | 7    | 1    | 3    | 0    | 5    | 2    |

Esimerkki, josta juuri keskustelimme, on vain laimennettu versio **RC4-virtasalauksesta**. Todellisessa RC4-virtasalauksessa on **S**-taulukko, joka on 256 tavua pitkä, ei 8 tavua, ja avain, joka voi olla 1 ja 256 tavun välillä, ei 1 ja 8 tavun välillä. Avaintaulukko ja avainvirrat tuotetaan sitten ottaen huomioon **S**-taulukon 256 tavun pituus. Laskelmat muuttuvat huomattavasti monimutkaisemmiksi, mutta periaatteet pysyvät samoina. Käyttämällä samaa avainta, [14,48,9], standardin RC4-salauksen kanssa, tavallinen viesti "SOUP" salataan heksadesimaalimuodossa 67 02 ed df.

Virtasalauksessa, jossa avainvirta päivittyy riippumatta tavallisesta viestistä tai salatusta viestistä, on kyse **synkronisesta virtasalauksesta**. Avainvirta riippuu vain avaimesta. Selvästi, RC4 on esimerkki synkronisesta virtasalauksesta, koska avainvirralla ei ole suhdetta tavalliseen viestiin tai salattuun viestiin. Kaikki edellisessä luvussa mainitut primitiiviset virtasalauksemme, mukaan lukien siirtosalakirjoitus, Vigenèren salakirjoitus ja kertakäyttösalasana, olivat myös synkronisen tyypin mukaisia.

Sen sijaan **asynkronisessa virtasalauksessa** avainvirta tuotetaan sekä avaimen että salatun viestin aiempien elementtien perusteella. Tätä salakirjoitustyyppiä kutsutaan myös **itse-synkronoivaksi salakirjoitukseksi**.

Tärkeää on, että RC4:llä tuotettua avainvirtaa tulisi käsitellä kertakäyttösalasanana, eikä avainvirtaa voi tuottaa täsmälleen samalla tavalla seuraavalla kerralla. Käytännöllinen ratkaisu avaimen vaihtamisen sijaan on yhdistää avain **nonce**-arvoon bytestreamin tuottamiseksi.

## AES 128-bittisellä avaimella
<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>

Kuten edellisessä luvussa mainittiin, Kansallinen standardi- ja teknologiainstituutti (NIST) järjesti kilpailun vuosina 1997–2000 määrittääkseen uuden symmetrisen salausstandardin. **Rijndael-salakirjoitus** osoittautui voittajaksi. Nimi on sanaleikki belgialaisten kehittäjien, Vincent Rijmenin ja Joan Daemenin, nimistä.
Rijndael-salakirjoitus on **lohkosalaus**, mikä tarkoittaa, että on olemassa ydin algoritmi, jota voidaan käyttää eri määrittelyillä avainten pituuksille ja lohkokooille. Voit sitten käyttää sitä eri toimintatilojen kanssa salausjärjestelmien rakentamiseen.
NIST-kilpailun komitea hyväksyi rajoitetun version Rijndael-salakirjoituksesta—nimittäin sellaisen, joka vaatii 128-bittiset lohkokoot ja avainten pituudet joko 128 bittiä, 192 bittiä tai 256 bittiä—osana **Advanced Encryption Standard (AES)** -standardia. Tämä rajoitettu versio Rijndael-salakirjoituksesta voidaan myös käyttää useiden toimintatilojen alla. Standardin määrittely on tunnettu nimellä **Advanced Encryption Standard (AES)**.

Näyttääkseni, miten Rijndael-salakirjoitus toimii, AES:n ydin, esitän salausprosessin 128-bittisellä avaimella. Avaimen koko vaikuttaa kierrosten määrään, joita kullekin salauslohkolle pidetään. 128-bittisille avaimille tarvitaan 10 kierrosta. 192 ja 256 bitin kohdalla olisi tarvittu vastaavasti 12 ja 14 kierrosta.

Lisäksi oletan, että AES käytetään **ECB-tilassa**. Tämä tekee esityksestä hieman helpomman eikä vaikuta Rijndael-algoritmiin. On kuitenkin varmaa, että ECB-tila ei ole turvallinen käytännössä, koska se johtaa deterministiseen salaukseen. Yleisimmin käytetty turvallinen tila AES:n kanssa on **CBC** (Cipher Block Chaining).

Kutsutaan avainta $K_0$. Rakennelma yllä mainituilla parametreilla näyttää sitten kuvassa *Figure 1*, missä $M_i$ tarkoittaa 128-bittistä osaa selkotekstiviestistä ja $C_i$ 128-bittistä osaa salatusta tekstistä. Selkotekstin viimeiseen lohkoon lisätään täyte, jos selkotekstiä ei voida jakaa tasaisesti lohkokoon mukaan.

*Kuva 1: AES-ECB 128-bittisellä avaimella*

![Kuva 1: AES-ECB 128-bittisellä avaimella](assets/Figure5-1.webp "Kuva 1: AES-ECB 128-bittisellä avaimella")

Jokainen 128-bittinen tekstilohko käy läpi kymmenen kierrosta Rijndael-salakirjoituskaavassa. Tämä vaatii erillisen kierrosavaimen jokaiselle kierrokselle ($K_1$ läpi $K_{10}$). Nämä tuotetaan jokaiselle kierrokselle alkuperäisestä 128-bittisestä avaimesta $K_0$ käyttäen **avaimen laajennusalgoritmia**. Näin ollen jokaista salattavaa tekstilohkoa varten käytämme alkuperäistä avainta $K_0$ sekä kymmentä erillistä kierrosavainta. Huomaa, että näitä samoja 11 avainta käytetään jokaiselle 128-bittiselle selkotekstilohkolle, joka vaatii salausta.

Avaimen laajennusalgoritmi on pitkä ja monimutkainen. Sen läpikäyminen ei tarjoa opetuksellista hyötyä. Voit tutustua avaimen laajennusalgoritmiin omatoimisesti, jos haluat. Kun kierrosavaimet on tuotettu, Rijndael-salakirjoitus manipuloi ensimmäistä 128-bittistä selkotekstilohkoa, $M_1$, kuten näkyy *Kuvassa 2*. Käymme nyt läpi nämä vaiheet.

*Kuva 2: $M_1$:n manipulointi Rijndael-salakirjoituksella:*

**Kierros 0:**
- XOR $M_1$ ja $K_0$ tuottavat $S_0$

---

**Kierros n n = {1,...,9}:**
- XOR $S_{n-1}$ ja $K_n$
- Tavun Substituutio
- Rivien Siirto
- Sarakkeiden Sekoitus
- XOR $S$ ja $K_n$ tuottavat $S_n$

---

**Kierros 10:**
- XOR $S_9$ ja $K_{10}$ - Tavun korvaus
- Rivien siirto
- XOR $S$ ja $K_{10}$ tuottaakseen $S_{10}$
- $S_{10}$ = $C_1$

### Kierros 0

Rijndael-salauksen kierros 0 on suoraviivainen. Taulukko $S_0$ tuotetaan XOR-operaatiolla 128-bittisen avaintekstin ja yksityisen avaimen välillä. Eli,

- $S_0 = M_1 \oplus K_0$

### Kierros 1

Ensimmäisellä kierroksella taulukko $S_0$ yhdistetään ensin kierrosavaimen $K_1$ kanssa käyttäen XOR-operaatiota. Tämä tuottaa uuden tilan $S$.

Toiseksi, suoritetaan **tavun korvaus**-operaatio nykyiselle $S$-tilalle. Se toimii ottamalla jokaisen 16-tavun $S$-taulukon tavun ja korvaamalla sen tavulla taulukosta, jota kutsutaan **Rijndaelin S-laatikoksi**. Jokaisella tavulla on ainutlaatuinen muunnos, ja tuloksena syntyy uusi $S$-tila. Rijndaelin S-laatikko on esitetty *Kuvassa 3*.

*Kuva 3: Rijndaelin S-laatikko*

|     | 00  | 01  | 02  | 03  | 04  | 05  | 06  | 07  | 08  | 09  | 0A  | 0B  | 0C  | 0D  | 0E  | 0F  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00  | 63  | 7C  | 77  | 7B  | F2  | 6B  | 6F  | C5  | 30  | 01  | 67  | 2B  | FE  | D7  | AB  | 76  |
| 10  | CA  | 82  | C9  | 7D  | FA  | 59  | 47  | F0  | AD  | D4  | A2  | AF  | 9C  | A4  | 72  | C0  |
| 20  | B7  | FD  | 93  | 26  | 36  | 3F  | F7  | CC  | 34  | A5  | E5  | F1  | 71  | D8  | 31  | 15  |
| 30  | 04  | C7  | 23  | C3  | 18  | 96  | 05  | 9A  | 07  | 12  | 80  | E2  | EB  | 27  | B2  | 75  |
| 40  | 09  | 83  | 2C  | 1A  | 1B  | 6E  | 5A  | A0  | 52  | 3B  | D6  | B3  | 29  | E3  | 2F  | 84  |
Tämän tekstin kääntäminen suoraan suomeksi ei ole mielekästä, koska se koostuu hexadesimaaliluvuista, jotka ovat yleensä osa ohjelmointiin, kryptografiaan tai tekniseen dokumentaatioon liittyvää sisältöä. Hexadesimaaliluvut (kuten 00, AF, B1 jne.) ovat numeerisia esityksiä, jotka käyttävät perustanaan lukua 16, ja ne sisältävät numeroita 0-9 sekä kirjaimia A-F. Tällaiset luvut ovat standardimuodossa ja ymmärrettäviä teknisen alan ammattilaisille sellaisenaan, joten niiden "kääntäminen" ei ole tarpeellista eikä toivottavaa. Ne ovat universaaleja eivätkä muutu kielestä toiseen.
| F0  | 8C  | A1  | 89  | 0D  | BF  | E6  | 42  | 68  | 41  | 99  | 2D  | 0F  | B0  | 54  | BB  | 16  |

Tämä S-Box on yksi esimerkki siitä, miten abstrakti algebra tulee mukaan Rijndael-salauksessa, erityisesti **Galois-kentät**.

Aloitetaan määrittelemällä jokainen mahdollinen tavuelementti 00:sta FF:ään 8-bittisenä vektorina. Jokainen tällainen vektori on elementti **Galois-kentässä GF(2^8)**, jossa modulo-operaation vähentämätön polynomi on $x^8 + x^4 + x^3 + x + 1$. Galois-kenttä näillä määrittelyillä tunnetaan myös nimellä **Rijndaelin äärellinen kenttä**.

Seuraavaksi luomme jokaiselle mahdolliselle kentän elementille niin kutsutun **Nybergin S-Boxin**. Tässä laatikossa jokainen tavu kuvataan sen **kertolaskun käänteisarvoon** (eli niin, että niiden tulo on 1). Sitten kartoitamme nämä arvot Nybergin S-laatikosta Rijndaelin S-laatikkoon käyttäen **affiinimuunnosta**.

Kolmas operaatio **S**-taulukossa on **rivien siirto** -operaatio. Se ottaa **S**-tilan ja listaa kaikki kuusitoista tavua matriisissa. Matriisin täyttö alkaa vasemmasta yläkulmasta ja etenee ylhäältä alas ja sitten, joka kerta kun sarake on täytetty, siirtyy yhden sarakkeen oikealle ja ylös.

Kun **S**-matriisi on rakennettu, neljä riviä siirretään. Ensimmäinen rivi pysyy samana. Toinen rivi siirtyy yhden vasemmalle. Kolmas siirtyy kaksi vasemmalle. Neljäs siirtyy kolme vasemmalle. Prosessista on esimerkki *Kuvassa 4*. **S**-tilan alkuperäinen tila on näytetty ylhäällä, ja siirtojen jälkeinen tila alhaalla.

*Kuva 4: Rivien siirto -operaatio*

| F1   | A0   | B1   | 23   |
|------|------|------|------|
| 59   | EF   | 09   | 82   |
| 97   | 01   | B0   | CC   |
| D4   | 72   | 04   | 21   |

| F1   | A0   | B1   | 23   |
|------|------|------|------|
| EF   | 09   | 82   | 59   |
| B0   | CC   | 97   | 01   |
| 21   | D4   | 72   | 04   |


Neljännessä vaiheessa **Galois-kentät** tulevat jälleen esiin. Aluksi jokainen **S**-matriisin sarake kerrotaan *Kuvan 5* 4 x 4 -matriisin sarakkeella. Mutta kyseessä ei ole tavallinen matriisikertolasku, vaan vektorikertolasku **vähentämättömän polynomin modulo**, $x^8 + x^4 + x^3 + x + 1$. Tuloksena olevat vektorikertoimet edustavat tavun yksittäisiä bittejä.

*Kuva 5: Sarakkeiden sekoitus -matriisi*

| 02   | 03   | 01   | 01   |
|------|------|------|------|
| 01   | 02   | 03   | 01   |
| 01   | 01   | 02   | 03   || 03   | 01   | 01   | 02   |

Ensimmäisen sarakkeen kertominen **S** matriisin kanssa 4 x 4 matriisin yllä tuottaa tuloksen *Kuvassa 6*.

*Kuva 6: Ensimmäisen sarakkeen kertolasku:*

$$
\begin{matrix}
02 \cdot F1 + 03 \cdot EF + 01 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 02 \cdot EF + 03 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 01 \cdot EF + 02 \cdot B0 + 03 \cdot 21 \\
03 \cdot F1 + 01 \cdot EF + 01 \cdot B0 + 02 \cdot 21
\end{matrix}
$$

Seuraavaksi kaikki matriisin termit on muutettava polynomeiksi. Esimerkiksi F1 edustaa 1 tavua ja muuttuu muotoon $x^7 + x^6 + x^5 + x^4 + 1$, ja 03 edustaa 1 tavua ja muuttuu muotoon $x + 1$.

Kaikki kertolaskut suoritetaan sitten **modulo** $x^8 + x^4 + x^3 + x + 1$. Tämä johtaa neljän polynomin lisäämiseen kunkin sarakkeen neljässä solussa. Nämä lisäykset suoritetaan **modulo 2**, ja lopputuloksena saadaan neljä polynomia. Jokainen näistä polynomeista edustaa 8-bittistä merkkijonoa eli 1 tavua **S**:ssä. Emme suorita kaikkia näitä laskelmia tässä *Kuvassa 6*, koska ne ovat laajoja.

Kun ensimmäinen sarake on käsitelty, **S** matriisin muut kolme saraketta käsitellään samalla tavalla. Lopulta tämä tuottaa matriisin, jossa on kuusitoista tavua, jotka voidaan muuttaa taulukoksi.

Viimeisessä vaiheessa taulukko **S** yhdistetään uudelleen kierrosavaimen kanssa **XOR**-operaatiossa. Tämä tuottaa tilan $S_1$. Eli,

- $S_1 = S \oplus K_0$

### Kierrokset 2–10

Kierrokset 2–9 ovat vain toiston kierros 1, *mutatis mutandis*. Viimeinen kierros on hyvin samankaltainen kuin edelliset kierrokset, paitsi että **sekoita sarakkeet** -vaihe jätetään pois. Eli, kierros 10 suoritetaan seuraavasti:

- $S_9 \oplus K_{10}$
- Tavun Substituutio
- Rivien Siirto
- $S_{10} = S \oplus K_{10}$

Tila $S_{10}$ on nyt asetettu $C_1$:ksi, ensimmäiseksi 128 bitiksi salatusta tekstistä. Jatkamalla loput 128-bittiset tavutekstilohkot tuottaa koko salatun tekstin **C**.

### Rijndael-salauksen toiminnot

Mikä on eri toimintojen taustalla Rijndael-salauksessa?

Yksityiskohtiin menemättä, salausjärjestelmiä arvioidaan sen perusteella, missä määrin ne luovat sekaannusta ja diffuusiota. Jos salausjärjestelmällä on korkea **sekaannuksen** aste, se tarkoittaa, että salattu teksti näyttää radikaalisti erilaiselta kuin alkuperäinen teksti. Jos salausjärjestelmällä on korkea **diffuusion** aste, se tarkoittaa, että mikä tahansa pieni muutos alkuperäisessä tekstissä tuottaa radikaalisti erilaisen salatun tekstin.
Rijndael-salauksen toimintojen taustalla oleva perustelu on, että ne tuottavat sekä korkean asteen sekaannusta että diffuusiota. Sekaannus syntyy tavun korvaus -toiminnosta, kun taas diffuusio syntyy riviensiirto- ja sarakkeidensekoitus -toiminnoista.
# Asymmetrinen kryptografia
<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>

## Avainten jakelun ja hallinnan ongelma
<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>

Kuten symmetrisessä kryptografiassa, asymmetrisiä järjestelmiä voidaan käyttää sekä salassapidon että todentamisen varmistamiseen. Toisin kuin symmetriset järjestelmät, nämä järjestelmät käyttävät kuitenkin kahta avainta yhden sijaan: yksityistä ja julkista avainta.

Aloitamme tutkimuksemme asymmetrisen kryptografian löytämisestä, erityisesti niistä ongelmista, jotka saivat sen aikaan. Seuraavaksi keskustelemme siitä, miten asymmetriset järjestelmät salauksen ja todentamisen osalta toimivat korkealla tasolla. Esittelemme sitten hajautusfunktioita, jotka ovat avainasemassa ymmärtäessämme asymmetrisia todentamisjärjestelmiä, ja joilla on myös merkitystä muissa kryptografisissa yhteyksissä, kuten luvussa 4 käsitellyissä hajautusperusteisissa viestintodennuskoodissa.

___

Kuvitellaan, että Bob haluaa ostaa uuden sadetakin Jim’s Sporting Goods -verkkourheiluvälinekaupasta, jolla on miljoonia asiakkaita Pohjois-Amerikassa. Tämä olisi hänen ensimmäinen ostoksensa heiltä, ja hän haluaa käyttää luottokorttiaan. Joten Bobin on ensin luotava tili Jim’s Sporting Goodsille, mikä edellyttää henkilökohtaisten tietojen, kuten osoitteen ja luottokorttitietojen, lähettämistä. Sen jälkeen hän voi suorittaa tarvittavat vaiheet sadetakin ostamiseksi.

Bob ja Jim’s Sporting Goods haluavat varmistaa, että heidän viestintänsä on turvallista koko tämän prosessin ajan, ottaen huomioon, että Internet on avoin viestintäjärjestelmä. He haluavat esimerkiksi varmistaa, että mahdolliset hyökkääjät eivät voi selvittää Bobin luottokortin ja osoitetietoja, eivätkä toistaa hänen ostoksiaan tai luoda väärennettyjä hänen nimissään.

Edellisessä luvussa käsitelty kehittynyt todennettu salausjärjestelmä voisi varmasti tehdä Bobin ja Jim’s Sporting Goods välisen viestinnän turvalliseksi. Mutta käytännön esteitä tällaisen järjestelmän toteuttamiselle on selvästi olemassa.

Kuvitellaan käytännön esteiden havainnollistamiseksi, että eläisimme maailmassa, jossa olisi olemassa vain symmetrisen kryptografian työkalut. Mitä Jim’s Sporting Goods ja Bob voisivat silloin tehdä varmistaakseen turvallisen viestinnän?

Tällaisissa olosuhteissa he kohtaisivat merkittäviä kustannuksia turvallisen viestinnän varmistamisessa. Koska Internet on avoin viestintäjärjestelmä, he eivät voi vain vaihtaa avainjoukkoa sen kautta. Siksi Bobin ja Jim’s Sporting Goods edustajan on tehtävä avaintenvaihto henkilökohtaisesti.

Yksi mahdollisuus on, että Jim’s Sporting Goods luo erityisiä avaintenvaihtopaikkoja, josta Bob ja muut uudet asiakkaat voivat noutaa avainjoukon turvallista viestintää varten. Tämä tulisi ilmeisesti merkittäviin organisatorisiin kustannuksiin ja vähentäisi huomattavasti uusien asiakkaiden mahdollisuuksia tehdä ostoksia tehokkaasti.

Vaihtoehtoisesti Jim’s Sporting Goods voi lähettää Bobille avainparin erittäin luotettavan lähettipalvelun kautta. Tämä on todennäköisesti tehokkaampaa kuin avaintenvaihtopaikkojen järjestäminen. Mutta tämäkin tulisi merkittäviin kustannuksiin, erityisesti jos monet asiakkaat tekevät vain yhden tai muutaman ostoksen.

Seuraavaksi, symmetrinen järjestelmä todennettuun salaukseen pakottaa myös Jim’s Sporting Goods säilyttämään erilliset avainjoukot kaikille asiakkailleen. Tämä olisi merkittävä käytännön haaste tuhansille asiakkaille, saati sitten miljoonille.
Ymmärtääksemme tämän viimeisen kohdan, kuvitellaan, että Jimin Urheiluvälineet antaa jokaiselle asiakkaalle saman avainparin. Tämä sallisi jokaisen asiakkaan – tai kenen tahansa muun, joka voisi saada tämän avainparin – lukea ja jopa manipuloida kaikkia viestintää Jimin Urheiluvälineiden ja sen asiakkaiden välillä. Voisi siis yhtä hyvin olla käyttämättä kryptografiaa lainkaan viestinnässäsi.
Jopa avainparin toistaminen vain joillekin asiakkaille on kauhea turvallisuuskäytäntö. Mikä tahansa potentiaalinen hyökkääjä voisi yrittää hyödyntää tätä järjestelmän ominaisuutta (muista, että hyökkääjien oletetaan tietävän kaiken järjestelmästä paitsi avaimet, Kerckhoffsin periaatteen mukaisesti.)

Joten, Jimin Urheiluvälineiden olisi säilytettävä avainpari jokaiselle asiakkaalle, riippumatta siitä, miten nämä avainparit jaetaan. Tämä esittää selvästi useita käytännön ongelmia.

- Jimin Urheiluvälineiden olisi säilytettävä miljoonia avainpareja, yksi sarja jokaista asiakasta varten.
- Näiden avainten olisi oltava asianmukaisesti suojattuja, sillä ne olisivat varma kohde hakkerien hyökkäyksille. Turvallisuusloukkaukset vaatisivat kalliiden avainvaihtojen toistamista, joko erityisissä avainvaihtopaikoissa tai kuriirin kautta.
- Jokaisen Jimin Urheiluvälineiden asiakkaan olisi säilytettävä avainparia turvallisesti kotona. Häviämisiä ja varkauksia tapahtuu, mikä vaatisi avainvaihtojen toistamista. Asiakkaiden olisi myös käytävä läpi tämä prosessi minkä tahansa muun verkkokaupan tai muiden entiteettien kanssa, joiden kanssa he haluavat kommunikoida ja tehdä transaktioita Internetin välityksellä.

Nämä kaksi päähaastetta, jotka juuri kuvailtiin, olivat hyvin perustavanlaatuisia huolenaiheita aina 1970-luvulle asti. Ne tunnettiin **avainten jakeluongelmana** ja **avainten hallintaongelmana**.

Nämä ongelmat olivat aina olleet olemassa, tietenkin, ja usein aiheuttaneet päänsärkyä menneisyydessä. Esimerkiksi sotilasvoimat joutuisivat jatkuvasti jakamaan kirjoja avaimilla turvallista viestintää varten kenttähenkilöstölle suurin riskein ja kustannuksin. Mutta nämä ongelmat pahenivat, kun maailma siirtyi yhä enemmän pitkän matkan digitaaliseen viestintään, erityisesti ei-valtiollisille toimijoille.

Jos näitä ongelmia ei olisi ratkaistu 1970-luvulla, tehokas ja turvallinen ostaminen Jimin Urheiluvälineissä ei todennäköisesti olisi ollut olemassa. Itse asiassa suurin osa nykymaailmastamme, jossa on käytännöllistä ja turvallista sähköpostia, verkkopankkitoimintaa ja ostamista, olisi todennäköisesti vain kaukainen fantasia. Mikään, mikä edes muistuttaisi Bitcoinia, ei olisi voinut ollenkaan olla olemassa.

Joten, mitä tapahtui 1970-luvulla? Miten on mahdollista, että voimme hetkessä tehdä ostoksia verkossa ja selata Maailmanlaajuista verkkoa turvallisesti? Miten on mahdollista, että voimme välittömästi lähettää Bitcoineja ympäri maailmaa älypuhelimistamme?

## Uudet suunnat kryptografiassa
<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>

1970-luvulla avainten jakelun ja hallinnan ongelmat herättivät huomiota ryhmässä amerikkalaisia akateemisia kryptografeja: Whitfield Diffie, Martin Hellman ja Ralph Merkle. Vakavasta skeptisyydestä valtaosan kollegoidensa taholta huolimatta he ryhtyivät kehittämään ratkaisua siihen.

Ainakin yksi heidän yrityksensä päämotivaatioista oli näkemys, että avoin tietokoneviestintä vaikuttaisi syvästi maailmaamme. Kuten Diffie ja Hellman huomauttavat vuonna 1976,
Tietokoneohjattujen viestintäverkkojen kehitys lupaa vaivatonta ja edullista yhteydenpitoa ihmisten tai tietokoneiden välillä maailman eri puolilla, korvaten suurimman osan postista ja monia matkoja telekommunikaatiolla. Monissa sovelluksissa nämä yhteydet on tehtävä turvallisiksi sekä salakuuntelua että luvattomien viestien injektointia vastaan. Tällä hetkellä turvallisuusongelmien ratkaisu kuitenkin laahaa kaukana muiden viestintäteknologioiden alueiden takana. *Nykyinen kryptografia ei kykene täyttämään vaatimuksia, sillä sen käyttö aiheuttaisi niin vakavia hankaluuksia järjestelmän käyttäjille, että se poistaisi monia teleprosessoinnin hyötyjä.* [1]

Diffien, Hellmanin ja Merklen sinnikkyys palkittiin. Heidän tulostensa ensimmäinen julkaisu oli Diffien ja Hellmanin vuonna 1976 kirjoittama artikkeli "New Directions in Cryptography". Siinä he esittelivät kaksi alkuperäistä tapaa käsitellä avainten jakelun ja avainten hallinnan ongelmia.

Ensimmäinen tarjoamansa ratkaisu oli etäinen *avaintenvaihtoprotokolla*, eli sääntöjoukko yhden tai useamman symmetrisen avaimen vaihtamiseksi turvattomalla viestintäkanavalla. Tätä protokollaa kutsutaan nykyään *Diffie-Hellman avaintenvaihdoksi* tai *Diffie-Hellman-Merkle avaintenvaihdoksi*. [2]

Diffie-Hellman avaintenvaihdossa kaksi osapuolta vaihtaa ensin julkisesti tietoa turvattomalla kanavalla, kuten Internetissä. Tämän tiedon perusteella he sitten itsenäisesti luovat symmetrisen avaimen (tai pari symmetrisiä avaimia) turvallista viestintää varten. Vaikka molemmat osapuolet luovat avaimensa itsenäisesti, julkisesti jaetun tiedon ansiosta tämä avainten luontiprosessi tuottaa molemmille saman tuloksen.

Tärkeää on, että vaikka kuka tahansa voi havainnoida osapuolten julkisesti vaihtamaa tietoa turvattomalla kanavalla, vain nämä kaksi osapuolta, jotka osallistuvat tiedonvaihtoon, voivat luoda symmetrisiä avaimia siitä.

Tämä kuulostaa tietenkin täysin vasten intuitiiviselta. Miten kaksi osapuolta voisi vaihtaa julkisesti tietoa, joka sallisi vain heidän luoda symmetrisiä avaimia siitä? Miksi kukaan muu tietoa vaihtoa havainnoiva ei pystyisi luomaan samoja avaimia?

Se perustuu tietenkin kauniiseen matematiikkaan. Diffie-Hellman avaintenvaihto toimii yksisuuntaisen funktion avulla, jossa on ansaluukku. Keskustellaanpa näistä kahdesta termistä vuorollaan.

Oletetaan, että sinulle on annettu jokin funktio $f(x)$ ja tulos $f(a) = y$, missä $a$ on tietty arvo $x$:lle. Sanomme, että $f(x)$ on **yksisuuntainen funktio**, jos arvon $y$ laskeminen annetusta $a$:sta ja $f(x)$:stä on helppoa, mutta arvon $a$ laskeminen annetusta $y$:stä ja $f(x)$:stä on laskennallisesti mahdotonta. Nimi **yksisuuntainen funktio** juontuu tietenkin siitä, että tällaisen funktion laskeminen on käytännöllistä vain yhteen suuntaan.

Joillakin yksisuuntaisilla funktioilla on niin kutsuttu **ansaluukku**. Vaikka $a$:n laskeminen pelkästään $y$:n ja $f(x)$:n perusteella on käytännössä mahdotonta, on olemassa tietty tieto $Z$, joka tekee $a$:n laskemisen $y$:stä laskennallisesti mahdolliseksi. Tätä tietoa $Z$ kutsutaan **ansaluukuksi**. Yksisuuntaiset funktiot, joilla on ansaluukku, tunnetaan **ansaluukkufunktioina**.
Emme syvenny tässä yksityiskohtiin Diffie-Hellman avainvaihdosta. Mutta periaatteessa jokainen osallistuja luo tietoa, jonka osa jaetaan julkisesti ja jonka osa pysyy salaisena. Kumpikin osapuoli ottaa sitten salaisen tietonsa ja toisen osapuolen julkisesti jakaman tiedon luodakseen yksityisen avaimen. Ja jokseenkin ihmeellisesti molemmat osapuolet päätyvät saman yksityisen avaimen omistajiksi.
Kuka tahansa osapuoli, joka tarkkailee vain kahden osapuolen välillä julkisesti jaettua tietoa Diffie-Hellman avainvaihdossa, ei pysty toistamaan näitä laskelmia. He tarvitsisivat yksityistä tietoa jommaltakummalta kahdesta osapuolesta tehdäkseen niin.

Vaikka Diffie-Hellman avainvaihdon perusversio, joka esiteltiin vuoden 1976 paperissa, ei ole kovin turvallinen, sen kehittyneemmät versiot ovat ehdottomasti edelleen käytössä tänään. Tärkeintä on, että jokainen avainvaihtoprotokolla kuljetuskerroksen turvallisuusprotokollan viimeisimmässä versiossa (versio 1.3) on käytännössä rikastettu versio protokollasta, jonka Diffie ja Hellman esittelivät vuonna 1976. Kuljetuskerroksen turvallisuusprotokolla on hallitseva protokolla tietojen turvalliseen vaihtoon, jotka on muotoiltu hypertext transfer protocol (http) mukaisesti, joka on Web-sisällön vaihtamisen standardi.

Tärkeää on, että Diffie-Hellman avainvaihto ei ole epäsymmetrinen järjestelmä. Tarkkaan ottaen se kuuluu pikemminkin symmetrisen avainkryptografian alueelle. Mutta koska sekä Diffie-Hellman avainvaihto että epäsymmetrinen kryptografia perustuvat yksisuuntaisiin numero-teoreettisiin funktioihin, joissa on ansaluukkuja, niitä käsitellään tyypillisesti yhdessä.

Toinen tapa, jonka Diffie ja Hellman tarjosivat avainten jakelun ja hallinnan ongelman ratkaisemiseksi vuoden 1976 paperissaan, oli tietenkin epäsymmetrisen kryptografian kautta.

Toisin kuin heidän esityksensä Diffie-Hellman avainvaihdosta, he tarjosivat vain yleiset ääriviivat siitä, miten epäsymmetriset kryptografiset järjestelmät voisivat mahdollisesti olla rakennettuja. He eivät tarjonneet mitään yksisuuntaista funktiota, joka voisi erityisesti täyttää kohtuullisen turvallisuuden ehdot tällaisissa järjestelmissä.

Käytännön toteutus epäsymmetrisestä järjestelmästä löydettiin kuitenkin vuotta myöhemmin kolmelta eri akateemiselta kryptografialta ja matemaatikolta: Ronald Rivest, Adi Shamir ja Leonard Adleman. [3] Heidän esittelemänsä kryptosysteemi tunnetaan **RSA kryptosysteeminä** (heidän sukunimiensä mukaan).

Epäsymmetrisessä kryptografiassa (ja Diffie-Hellman avainvaihdossa) käytetyt ansaluukkufunktiot liittyvät kaikki kahteen pääasialliseen **laskennallisesti vaikeaan ongelmaan**: alkulukujen tekijöihin jakaminen ja diskreettien logaritmien laskeminen.

**Alkulukujen tekijöihin jakaminen** vaatii, kuten nimi vihjaa, kokonaisluvun jakamisen sen alkutekijöihin. RSA-ongelma on ehdottomasti tunnetuin esimerkki kryptosysteemistä, joka liittyy alkulukujen tekijöihin jakamiseen.

**Diskreetin logaritmin ongelma** on ongelma, joka esiintyy syklisissä ryhmissä. Annetaan generaattori tietyssä syklisessä ryhmässä, se vaatii yksilöllisen eksponentin laskemisen, joka tarvitaan toisen elementin tuottamiseen ryhmässä generaattorista.

Diskreettiin logaritmiin perustuvat järjestelmät nojaavat kahteen päätyyppiin syklisiä ryhmiä: kokonaislukujen kertolaskullisiin ryhmiin ja ryhmiin, jotka sisältävät pisteitä elliptisillä käyrillä. Alkuperäinen Diffie-Hellman avainvaihto, kuten esiteltiin "New Directions in Cryptography" -julkaisussa, toimii kokonaislukujen syklisen kertolaskullisen ryhmän kanssa. Bitcoinin digitaalinen allekirjoitus algoritmi ja äskettäin esitelty Schnorr allekirjoitusjärjestelmä (2021) perustuvat molemmat diskreetin logaritmin ongelmaan tietyssä elliptisen käyrän syklisessä ryhmässä.

Seuraavaksi käymme läpi korkean tason yleiskatsauksen salassapidosta ja autentikoinnista epäsymmetrisessä asetuksessa. Ennen kuin teemme niin, meidän on kuitenkin tehtävä lyhyt historiallinen huomautus.
Nyt vaikuttaa uskottavalta, että joukko brittiläisiä kryptologeja ja matemaatikkoja, jotka työskentelivät Government Communications Headquarters (GCHQ) -organisaatiossa, oli itsenäisesti tehnyt yllä mainitut löydöt muutamaa vuotta aiemmin. Tämä ryhmä koostui James Ellisistä, Clifford Cocksista ja Malcolm Williamsonista.

Heidän omien kertomustensa ja GCHQ:n mukaan James Ellis oli ensimmäisenä keksinyt julkisen avaimen kryptografian konseptin vuonna 1969. Clifford Cocks puolestaan löysi RSA-kryptografisen järjestelmän vuonna 1973, ja Malcolm Williamson Diffie-Hellmanin avainvaihdon konseptin vuonna 1974. [4] Heidän löytönsä julkaistiin kuitenkin väitetysti vasta vuonna 1997, ottaen huomioon GCHQ:ssa tehdyn työn salaisen luonteen.

**Huomautuksia:**

[1] Whitfield Diffie ja Martin Hellman, “New directions in cryptography,” _IEEE Transactions on Information Theory_ IT-22 (1976), s. 644–654, s. 644.

[2] Ralph Merkle myös käsittelee avainvaihtoprotokollaa artikkelissaan “Secure communications over insecure channels”, _Communications of the Association for Computing Machinery_, 21 (1978), 294–99. Vaikka Merkle toimitti tämän paperin ennen Diffie'n ja Hellmanin paperia, se julkaistiin myöhemmin. Merklen ratkaisu ei ole eksponentiaalisesti turvallinen, toisin kuin Diffie-Hellmanin.

[3] Ron Rivest, Adi Shamir ja Leonard Adleman, “A method for obtaining digital signatures and public-key cryptosystems”, _Communications of the Association for Computing Machinery_, 21 (1978), s. 120–26.

[4] Hyvän historian näistä löydöistä tarjoaa Simon Singh, _The Code Book_, Fourth Estate (Lontoo, 1999), Luku 6.

## Asymmetrinen salaus ja autentikointi
<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>

Yleiskatsaus **asymmetriseen salaukseen** Bobin ja Alicen avulla on esitetty *Kuvassa 1*.

Alice luo ensin avainparin, joka koostuu yhdestä julkisesta avaimesta ($K_P$) ja yhdestä yksityisestä avaimesta ($K_S$), missä “P” $K_P$:ssä tarkoittaa “public” (julkinen) ja “S” $K_S$:ssä “secret” (salainen). Hän jakaa tämän julkisen avaimen vapaasti muiden kanssa. Palataan tämän jakoprosessin yksityiskohtiin hieman myöhemmin. Mutta toistaiseksi oletetaan, että kuka tahansa, mukaan lukien Bob, voi turvallisesti hankkia Alicen julkisen avaimen $K_P$.

Myöhemmässä vaiheessa Bob haluaa kirjoittaa viestin $M$ Alicelle. Koska se sisältää arkaluonteista tietoa, hän haluaa sisällön pysyvän salassa kaikilta paitsi Alicelta. Joten Bob ensin salaa viestinsä $M$ käyttäen $K_P$:tä. Hän sitten lähettää tuloksena syntyneen salatun tekstin $C$ Alicelle, joka purkaa $C$:n $K_S$:llä tuottaakseen alkuperäisen viestin $M$.

*Kuva 1: Asymmetrinen salaus*

![Kuva 1: Asymmetrinen salaus](assets/Figure6-1.webp "Kuva 1: Asymmetrinen salaus")



Kaikki viholliset, jotka kuuntelevat Bobin ja Alicen kommunikaatiota, voivat havaita $C$:n. He tietävät myös $K_P$:n ja salausalgoritmin $E(\cdot)$. Tärkeää kuitenkin on, että tämä tieto ei mahdollista salatun tekstin $C$ purkamista käytännössä. Salatun tekstin purkaminen vaatii nimenomaan $K_S$:n, jota hyökkääjällä ei ole.
Symmetriset salausjärjestelmät on yleensä suunniteltu olemaan turvallisia hyökkääjää vastaan, joka voi validisti salata avoimen tekstin viestejä (tunnetaan valitun salakirjoituksen hyökkäyksen turvallisuutena). Niitä ei kuitenkaan ole suunniteltu nimenomaan sallimaan tällaisten validien salakirjoitusten luomista hyökkääjän tai kenenkään muun toimesta. Tämä on täysin vastakkainen lähestymistapa asymmetriseen salausjärjestelmään verrattuna, jonka koko tarkoitus on sallia kenen tahansa, mukaan lukien hyökkääjien, tuottaa valideja salakirjoituksia. Asymmetriset salausjärjestelmät voidaan siis merkitä **monen käyttäjän salauksiksi**.

Ymmärtääksemme paremmin, mitä tapahtuu, kuvittele, että Bob haluaisi lähettää salaisen kirjeen fyysisesti sen sijaan, että lähettäisi viestin sähköisesti. Yksi tapa varmistaa salaisuus olisi, että Alice lähettäisi Bobille turvallisen riippulukon, mutta pitäisi avaimen itsellään. Kirjoitettuaan kirjeensä Bob voisi laittaa kirjeen laatikkoon ja lukita sen Alicen riippulukolla. Sen jälkeen hän voisi lähettää lukitun laatikon viestin kanssa Alicelle, jolla on avain sen avaamiseen.

Vaikka Bob pystyy lukitsemaan riippulukon, ei hän eikä kukaan muu, joka saa laatikon käsiinsä, voi avata riippulukkoa, jos se todella on turvallinen. Vain Alice voi avata sen ja nähdä Bobin kirjeen sisällön, koska hänellä on avain.

Karkeasti sanottuna asymmetrinen salausjärjestelmä on digitaalinen versio tästä prosessista. Riippulukko vastaa julkista avainta ja riippulukon avain vastaa yksityistä avainta. Koska riippulukko on digitaalinen, on Alicen paljon helpompi ja vähemmän kallista jakaa se kenelle tahansa, joka haluaisi lähettää hänelle salaisia viestejä.

Asymmetrisessa ympäristössä autentikointiin käytämme **digitaalisia allekirjoituksia**. Nämä toimivat siis samalla tavalla kuin viestien autentikointikoodit symmetrisessä ympäristössä. Digitaalisista allekirjoituksista on yleiskatsaus *Kuvassa 2*.

Bob luo ensin avainparin, joka koostuu julkisesta avaimesta ($K_P$) ja yksityisestä avaimesta ($K_S$), ja jakaa julkisen avaimensa. Kun hän haluaa lähettää autentikoidun viestin Alicelle, hän ottaa ensin viestinsä $M$ ja yksityisen avaimensa luodakseen **digitaalisen allekirjoituksen** $D$. Bob lähettää sitten Alicelle viestinsä yhdessä digitaalisen allekirjoituksen kanssa.

Alice syöttää viestin, julkisen avaimen ja digitaalisen allekirjoituksen **varmennusalgoritmiin**. Tämä algoritmi tuottaa joko **true** validille allekirjoitukselle tai **false** epävalidille allekirjoitukselle.

Digitaalinen allekirjoitus on, kuten nimi selvästi ilmaisee, kirjoitettujen allekirjoitusten digitaalinen vastine kirjeissä, sopimuksissa ja niin edelleen. Itse asiassa digitaalinen allekirjoitus on yleensä paljon turvallisempi. Kirjoitetun allekirjoituksen voi väärentää jonkin verran ponnistellen; prosessi, joka on helpompaa, koska kirjoitettuja allekirjoituksia ei usein tarkisteta huolellisesti. Turvallinen digitaalinen allekirjoitus on kuitenkin, kuten turvallinen viestien autentikointikoodi, **eksistentiaalisesti väärentämätön**: turvallisella digitaalisella allekirjoitusskeemalla kukaan ei voi käytännössä luoda allekirjoitusta viestille, joka läpäisee varmennusmenettelyn, ellei hänellä ole yksityistä avainta.

*Kuva 2: Asymmetrinen autentikointi*

![Kuva 2: Asymmetrinen autentikointi](assets/Figure6-2.webp "Kuva 2: Asymmetrinen autentikointi")


Kuten asymmetrisessa salauksessa, näemme mielenkiintoisen kontrastin digitaalisten allekirjoitusten ja viestien autentikointikoodien välillä. Jälkimmäisen varmennusalgoritmia voi käyttää vain yksi osapuoli, joka on osallisena turvallisessa viestinnässä. Tämä johtuu siitä, että se vaatii yksityisen avaimen. Asymmetrisessa ympäristössä kuitenkin kuka tahansa voi varmentaa Bobin tekemän digitaalisen allekirjoituksen $S$.
Kaikki tämä tekee digitaalisista allekirjoituksista erittäin tehokkaan työkalun. Se muodostaa perustan esimerkiksi sopimusten allekirjoitusten luomiselle, joita voidaan tarkistaa oikeudellisissa tarkoituksissa. Jos Bob olisi tehnyt allekirjoituksen sopimukseen yllä olevassa vaihdossa, Alice voi näyttää viestin $M$, sopimuksen ja allekirjoituksen $S$ oikeusistuimelle. Oikeusistuin voi sitten tarkistaa allekirjoituksen käyttäen Bobin julkista avainta. [5]
Toisena esimerkkinä, digitaaliset allekirjoitukset ovat tärkeä osa turvallista ohjelmistojen ja ohjelmistopäivitysten jakelua. Tällaista julkista todennettavuutta ei voisi koskaan luoda pelkästään viestien todennuskoodien avulla.

Viimeisenä esimerkkinä digitaalisten allekirjoitusten voimasta, harkitse Bitcoinia. Yksi yleisimmistä väärinkäsityksistä Bitcoinista, erityisesti mediassa, on se, että transaktiot ovat salattuja: ne eivät ole. Sen sijaan, Bitcoin-transaktiot toimivat digitaalisten allekirjoitusten avulla turvallisuuden takaamiseksi.

Bitcoinit ovat olemassa erissä, joita kutsutaan käyttämättömiksi transaktiotuotoksiksi (tai **UTXOiksi**). Oletetaan, että saat kolme maksua tietylle Bitcoin-osoitteelle, jokainen kaksi bitcoinia. Teknisesti sinulla ei nyt ole kuutta bitcoinia tuossa osoitteessa. Sen sijaan, sinulla on kolme erää kaksi bitcoinia, jotka on lukittu kryptografisella ongelmalla, joka liittyy kyseiseen osoitteeseen. Minkä tahansa maksun tekemiseksi voit käyttää yhtä, kahta tai kaikkia kolmea näistä eristä, riippuen siitä, kuinka paljon tarvitset transaktioon.

Omistusoikeuden todistus käyttämättömistä transaktiotuotoksista näytetään yleensä yhden tai useamman digitaalisen allekirjoituksen kautta. Bitcoin toimii juuri siksi, että voimassa olevien digitaalisten allekirjoitusten tekeminen käyttämättömiin transaktiotuotoksiin on laskennallisesti mahdotonta, ellet omista salaisia tietoja, jotka vaaditaan niiden tekemiseen.

Tällä hetkellä Bitcoin-transaktiot sisältävät läpinäkyvästi kaiken tiedon, joka on vahvistettava verkon osallistujien toimesta, kuten käyttämättömien transaktiotuotosten alkuperän, joita käytetään transaktiossa. Vaikka on mahdollista piilottaa osa tästä tiedosta ja silti sallia vahvistaminen (kuten jotkin vaihtoehtoiset kryptovaluutat, kuten Monero, tekevät), tämä luo myös erityisiä turvallisuusriskejä.

Sekavuus joskus nousee esiin digitaalisten allekirjoitusten ja digitaalisesti tallennettujen kirjallisten allekirjoitusten välillä. Jälkimmäisessä tapauksessa tallennat kuvan kirjallisesta allekirjoituksestasi ja liität sen sähköiseen asiakirjaan, kuten työsopimukseen. Tämä kuitenkaan ei ole digitaalinen allekirjoitus kryptografisessa mielessä. Jälkimmäinen on vain pitkä numero, joka voidaan tuottaa vain, jos omistaa yksityisen avaimen.

Kuten symmetrisessä avainasetuksessa, voit myös käyttää asymmetristä salausta ja todennusskeemoja yhdessä. Samat periaatteet pätevät. Ensinnäkin, sinun tulisi käyttää eri yksityisiä-julkisia avainpareja salaukseen ja digitaalisten allekirjoitusten tekemiseen. Lisäksi, sinun tulisi ensin salata viesti ja sitten todentaa se.

Tärkeää on, että monissa sovelluksissa asymmetristä kryptografiaa ei käytetä koko viestintäprosessin ajan. Sen sijaan, sitä käytetään tyypillisesti vain *symmetristen avainten vaihtamiseen* osapuolten välillä, joilla he todellisuudessa kommunikoivat.

Tämä on tapaus esimerkiksi, kun ostat tavaroita verkossa. Tuntien myyjän julkisen avaimen, hän voi lähettää sinulle digitaalisesti allekirjoitettuja viestejä, joiden aitouden voit varmistaa. Tämän perusteella voit noudattaa yhtä monista protokollista symmetristen avainten vaihtamiseksi turvallisesti kommunikoidaksesi.

Pääsyy edellä mainitun lähestymistavan yleisyydelle on, että asymmetrinen kryptografia on paljon vähemmän tehokasta kuin symmetrinen kryptografia tuottamaan tietyn turvallisuustason. Tämä on yksi syy, miksi tarvitsemme edelleen symmetristä avainkryptografiaa julkisen kryptografian rinnalla. Lisäksi, symmetrinen avainkryptografia on paljon luonnollisempi erityisissä sovelluksissa, kuten tietokoneen käyttäjä salatessaan omia tietojaan.

Joten miten tarkalleen digitaaliset allekirjoitukset ja julkinen avainsalaus ratkaisevat avainten jakelun ja avainhallinnan ongelmat?
Tässä ei ole yhtä ainoaa vastausta. Asymmetrinen kryptografia on työkalu, eikä ole olemassa vain yhtä tapaa käyttää tätä työkalua. Mutta otetaan esimerkkimme Jimin Urheiluvälineistä näyttääksemme, miten ongelmat tyypillisesti ratkaistaisiin tässä esimerkissä.
Aluksi Jimin Urheiluvälineet ottaisi todennäköisesti yhteyttä **sertifikaattiviranomaiseen**, organisaatioon, joka tukee julkisen avaimen jakelua. Sertifikaattiviranomainen rekisteröisi joitakin tietoja Jimin Urheiluvälineistä ja myöntäisi sille julkisen avaimen. Sen jälkeen se lähettäisi Jimin Urheiluvälineille sertifikaatin, joka tunnetaan **TLS/SSL-sertifikaattina**, ja jossa Jimin Urheiluvälineiden julkinen avain on digitaalisesti allekirjoitettu käyttäen sertifikaattiviranomaisen omaa julkista avainta. Näin sertifikaattiviranomainen vahvistaa, että tietty julkinen avain todella kuuluu Jimin Urheiluvälineille.

Tämän prosessin ymmärtämisen avain TLS/SSL-sertifikaattien kanssa on, että vaikka et yleensä säilytä Jimin Urheiluvälineiden julkista avainta missään tietokoneellasi, tunnustettujen sertifikaattiviranomaisten julkiset avaimet ovat todellakin tallennettu selaimeesi tai käyttöjärjestelmääsi. Nämä on tallennettu niin kutsuttuihin **juurisertifikaatteihin**.

Näin ollen, kun Jimin Urheiluvälineet toimittaa sinulle TLS/SSL-sertifikaattinsa, voit tarkistaa sertifikaattiviranomaisen digitaalisen allekirjoituksen juurisertifikaatin kautta selaimessasi tai käyttöjärjestelmässäsi. Jos allekirjoitus on pätevä, voit olla suhteellisen varma, että sertifikaatissa oleva julkinen avain todella kuuluu Jimin Urheiluvälineille. Tällä perusteella on helppo perustaa protokolla turvalliseen viestintään Jimin Urheiluvälineiden kanssa.

Avainten jakelu on nyt tullut huomattavasti yksinkertaisemmaksi Jimin Urheiluvälineille. Ei ole vaikea nähdä, että myös avainten hallinta on huomattavasti yksinkertaistunut. Sen sijaan, että joutuisi säilyttämään tuhansia avaimia, Jimin Urheiluvälineiden tarvitsee vain säilyttää yksityinen avain, joka mahdollistaa allekirjoitusten tekemisen julkiselle avaimelle sen SSL-sertifikaatissa. Joka kerta, kun asiakas tulee Jimin Urheiluvälineiden sivustolle, he voivat perustaa turvallisen viestintäistunnon tästä julkisesta avaimesta. Asiakkaiden ei myöskään tarvitse säilyttää mitään tietoja (muuta kuin tunnustettujen sertifikaattiviranomaisten julkiset avaimet heidän käyttöjärjestelmässään ja selaimessaan).

**Huomautuksia:**

[5] Kaikki yritykset saavuttaa kiistämättömyys, toinen teema, josta keskustelimme luvussa 1, perustuvat perustaltaan digitaalisiin allekirjoituksiin.

## Hahmofunktiot
<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>

Hahmofunktiot ovat kaikkialla kryptografiassa. Ne eivät ole symmetrisiä eivätkä asymmetrisiä järjestelmiä, vaan kuuluvat omaan kryptografiseen kategoriaansa.

Törmäsimme jo hahmofunktioihin luvussa 4, kun loimme hahmoon perustuvia todennusviestejä. Ne ovat myös tärkeitä digitaalisten allekirjoitusten yhteydessä, joskin hieman eri syystä: Digitaaliset allekirjoitukset tehdään nimittäin tyypillisesti jonkin (salatun) viestin hahmoarvon yli, eikä itse (salatun) viestin yli. Tässä osiossa tarjoan perusteellisemman johdannon hahmofunktioihin.

Aloitetaan määrittelemällä hahmofunktio. **Hahmofunktio** on mikä tahansa tehokkaasti laskettava funktio, joka ottaa syötteitä mielivaltaisesta koosta ja tuottaa kiinteän pituisia tulosteita.

**Kryptografinen hahmofunktio** on vain hahmofunktio, joka on hyödyllinen sovelluksissa kryptografiassa. Kryptografisen hahmofunktion tulosta kutsutaan tyypillisesti **hahmoksi**, **hahmoarvoksi** tai **viestitiivistelmäksi**.

Kryptografian kontekstissa "hahmofunktio" viittaa tyypillisesti kryptografiseen hahmofunktioon. Aion noudattaa tätä käytäntöä tästä eteenpäin.
Esimerkkinä suositusta hajautusfunktiosta on **SHA-256** (secure hash algorithm 256). Riippumatta syötteen koosta (esim. 15 bittiä, 100 bittiä tai 10 000 bittiä), tämä funktio tuottaa 256-bittisen hajautusarvon. Alla näet muutaman esimerkin SHA-256 funktion tuloksista.
“Hello”: `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`

“52398”: `a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90`

“Kryptografia on hauskaa”: `3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c`

Kaikki tulokset ovat tarkalleen 256 bittiä esitettyinä heksadesimaalimuodossa (jokainen heksadesimaalinumero voidaan esittää neljällä binäärinumerolla). Joten vaikka olisit syöttänyt SHA-256 funktioon Tolkienin *Tarun Sormusten Herrasta* kirjan, tuloksena olisi silti 256 bittiä.

Hajautusfunktioita, kuten SHA-256, käytetään moniin tarkoituksiin kryptografiassa. Hajautusfunktiolta vaadittavat ominaisuudet riippuvat todella sovelluksen kontekstista. Kryptografiassa hajautusfunktioilta yleisesti toivottuja pääominaisuuksia ovat: [6]

1.	Yhteentörmäyksenkestävyys
2.	Piilottaminen

Hajautusfunktio $H$ sanotaan **yhteentörmäyksenkestäväksi**, jos on käytännössä mahdotonta löytää kahta arvoa, $x$ ja $y$, siten, että $x \neq y$, mutta $H(x) = H(y)$.

Yhteentörmäyksenkestävät hajautusfunktiot ovat tärkeitä esimerkiksi ohjelmistojen vahvistamisessa. Oletetaan, että haluaisit ladata Bitcoin Core 0.21.0 Windows-version (palvelinsovellus Bitcoin-verkon liikenteen käsittelyyn). Pääaskeleet, jotka sinun tulisi ottaa ohjelmiston aitouden varmistamiseksi, ovat seuraavat:

1.	Sinun on ensin ladattava ja tuotava yhden tai useamman Bitcoin Coren avustajan julkiset avaimet ohjelmistoon, joka pystyy varmentamaan digitaalisia allekirjoituksia (esim. Kleopetra). Voit löytää nämä julkiset avaimet [täältä](https://github.com/bitcoin/bitcoin/blob/master/contrib/builder-keys/keys.txt). On suositeltavaa, että varmistat Bitcoin Core -ohjelmiston useiden avustajien julkisilla avaimilla.
2.	Seuraavaksi sinun on varmennettava tuodut julkiset avaimet. Yksi askel, jonka sinun tulisi ottaa, on varmistaa, että löytämäsi julkiset avaimet ovat samat kuin eri paikoissa julkaistut. Voisit esimerkiksi konsultoida henkilöiden henkilökohtaisia verkkosivuja, Twitter-sivuja tai Github-sivuja, joiden julkisia avaimia olet tuonut. Tyypillisesti tämä julkisten avainten vertailu tehdään vertaamalla julkisen avaimen lyhyttä hajautusarvoa, jota kutsutaan sormenjäljeksi.
3.	Seuraavaksi sinun on ladattava Bitcoin Coren suoritettava tiedosto heidän [verkkosivustoltaan](www.bitcoincore.org). Saatavilla on paketteja Linux-, Windows- ja MAC-käyttöjärjestelmiin.
4.	Seuraavaksi sinun on löydettävä kaksi julkaisutiedostoa. Ensimmäinen sisältää virallisen SHA-256 hajautuksen lataamallesi suoritettavalle tiedostolle yhdessä kaikkien muiden julkaistujen pakettien hajautusten kanssa. Toinen julkaisutiedosto sisältää eri avustajien allekirjoitukset julkaisutiedostosta, joka sisältää pakettien hajautukset. Molemmat julkaisutiedostot tulisi sijaita Bitcoin Coren verkkosivustolla.
5. Seuraavaksi sinun tarvitsee laskea ladatun suoritettavan tiedoston SHA-256-tiiviste omalla tietokoneellasi Bitcoin Core -verkkosivustolta. Sen jälkeen vertaat tätä tulosta virallisen paketin tiivisteen kanssa. Ne tulisi olla samat.  
6. Lopuksi sinun on varmistettava, että yksi tai useampi julkaisutiedoston digitaalinen allekirjoitus, joka vastaa virallisia pakettien tiivisteitä, todella vastaa yhtä tai useampaa julkista avainta, jonka olet tuonut (Bitcoin Coren julkaisuja ei aina allekirjoita kaikki). Voit tehdä tämän sovelluksella, kuten Kleopetra.

Tämän ohjelmiston varmennusprosessin kahdella päähyödyllä. Ensinnäkin se varmistaa, että latauksessa Bitcoin Coren verkkosivustolta ei ole tapahtunut virheitä. Toiseksi se varmistaa, että hyökkääjä ei ole saanut sinua lataamaan muokattua, haitallista koodia, joko hakkeroinnin kautta Bitcoin Coren verkkosivustolla tai liikenteen kaappaamisen kautta.

Miten tarkalleen ottaen yllä kuvattu ohjelmiston varmennusprosessi suojaa näiltä ongelmilta?

Jos olet huolellisesti varmentanut tuomasi julkiset avaimet, voit olla melko varma, että nämä avaimet ovat todella heidän ja ettei niitä ole kompromisoitu. Koska digitaalisilla allekirjoituksilla on eksistentiaalinen väärentämättömyys, tiedät, että vain nämä avustajat olisivat voineet tehdä digitaalisen allekirjoituksen virallisten pakettien tiivisteiden päälle julkaisutiedostossa.

Oletetaan, että julkaisutiedostosi allekirjoitukset tarkistuvat. Voit nyt verrata paikallisesti laskemaasi tiivistearvoa ladatulle Windows-suoritettavalle tiedostolle siihen, joka sisältyy asianmukaisesti allekirjoitettuun julkaisutiedostoon. Koska tiedät, että SHA-256-tiivistefunktio on törmäyskestävä, vastaavuus tarkoittaa, että suoritettavasi tiedosto on täsmälleen sama kuin virallinen suoritettava tiedosto.

Käännämme nyt huomiomme toiseen yleiseen tiivistefunktioiden ominaisuuteen: **piilottaminen**. Mitä tahansa tiivistefunktiota $H$ sanotaan piilottamisominaisuudeksi, jos satunnaisesti valitun $x$:n kohdalla erittäin suuresta joukosta on käytännössä mahdotonta löytää $x$, kun annettuna on vain $H(x)$.

Alla näet SHA-256-tiivisteen viestistä, jonka kirjoitin. Riittävän satunnaisuuden varmistamiseksi viestiin sisältyi lopussa satunnaisesti generoitu merkkijono. Koska SHA-256:lla on piilottamisominaisuus, kukaan ei pystyisi selvittämään tätä viestiä.

- `b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded`

Mutta en jätä sinua jännitykseen siihen asti, kunnes SHA-256 heikkenee. Alkuperäinen viestini oli seuraava:

* “Tämä on hyvin satunnainen viesti, tai no melko satunnainen. Tämä alkuosa ei ole, mutta päättelen joillakin suhteellisen satunnaisilla merkeillä varmistaakseni hyvin arvaamattoman viestin. XLWz4dVG3BxUWm7zQ9qS”.

Yleinen tapa, jolla piilottamisominaisuutta omaavia tiivistefunktioita käytetään, on salasanojen hallinnassa (törmäyskestävyys on myös tärkeää tähän sovellukseen). Mikä tahansa kunnollinen online-tilipohjainen palvelu, kuten Facebook tai Google, ei tallenna salasanojasi suoraan päästäkseen käsiksi tilillesi. Sen sijaan ne tallentavat vain salasanan tiivisteen. Joka kerta, kun syötät salasanasi selaimessa, tiiviste lasketaan ensin. Vain tämä tiiviste lähetetään palveluntarjoajan palvelimelle ja verrataan tietokannan taustalla olevaan tiivisteeseen. Piilottamisominaisuus voi auttaa varmistamaan, että hyökkääjät eivät voi palauttaa sitä tiivistearvosta.
Salasanojen hallinta hajautusarvojen kautta toimii tietenkin vain, jos käyttäjät todella valitsevat vaikeita salasanoja. Piilottamisominaisuus olettaa, että x on valittu satunnaisesti erittäin suuresta joukosta. Salasanojen, kuten "1234", "mypassword" tai syntymäpäiväsi, valitseminen ei tarjoa mitään todellista turvallisuutta. Pitkiä listoja yleisistä salasanoista ja niiden hajautusarvoista on olemassa, joita hyökkääjät voivat hyödyntää, jos he saavat käsiinsä salasanasi hajautusarvon. Tällaisia hyökkäyksiä kutsutaan **sanakirjahyökkäyksiksi**. Jos hyökkääjät tietävät joitakin henkilökohtaisia tietojasi, he saattavat myös yrittää joitakin perusteltuja arvauksia. Siksi tarvitset aina pitkiä, turvallisia salasanoja (mieluiten pitkiä, satunnaisia merkkijonoja salasananhallintaohjelmasta).

Joskus sovellus saattaa tarvita hajautusfunktiota, jolla on sekä törmäyskestävyys että piilottaminen. Mutta varmasti ei aina. Esimerkiksi keskustelemamme ohjelmiston varmennusprosessi vaatii vain, että hajautusfunktio osoittaa törmäyskestävyyttä, piilottaminen ei ole tärkeää.

Vaikka törmäyskestävyys ja piilottaminen ovatkin hajautusfunktioiden pääominaisuuksia kryptografiassa, tietyissä sovelluksissa saattaa olla toivottavaa myös muita ominaisuuksia.

**Huomautukset:**

[6] "Piilottaminen"-terminologia ei ole yleiskieltä, vaan se on otettu erityisesti Arvind Narayananin, Joseph Bonneaun, Edward Feltenin, Andrew Millerin ja Steven Goldfederin teoksesta *Bitcoin and Cryptocurrency Technologies*, Princeton University Press (Princeton, 2016), Luku 1.

# RSA-kryptosysteemi
<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>

## Tekijöihin jakamisen ongelma
<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>

Vaikka symmetrinen kryptografia on yleensä melko intuitiivista useimmille ihmisille, näin ei yleensä ole epäsymmetrisen kryptografian kanssa. Vaikka olet todennäköisesti mukava korkean tason kuvauksen kanssa, joka tarjottiin edellisissä osioissa, mietit todennäköisesti, mitä yksisuuntaiset funktiot tarkalleen ottaen ovat ja miten niitä käytetään epäsymmetristen järjestelmien rakentamiseen.

Tässä luvussa poistan joitakin mysteerejä epäsymmetrisen kryptografian ympäriltä tutkimalla tarkemmin erityistä esimerkkiä, nimittäin RSA-kryptosysteemiä. Ensimmäisessä osiossa esittelen tekijöihin jakamisen ongelman, johon RSA-ongelma perustuu. Käsittelen sitten useita avainkohtia lukuteoriasta. Viimeisessä osiossa yhdistämme nämä tiedot selittääksemme RSA-ongelman ja miten sitä voidaan käyttää epäsymmetristen kryptografisten järjestelmien luomiseen.

Tämän syvyyden lisääminen keskusteluun ei ole helppoa. Se vaatii melkoisen määrän lukuteoreettisia teoreemoja ja väitteitä. Mutta älä anna matematiikan lannistaa sinua. Tämän keskustelun läpikäyminen parantaa merkittävästi ymmärrystäsi siitä, mikä on epäsymmetrisen kryptografian perustana, ja on arvokas sijoitus.

Käännämme nyt katseemme tekijöihin jakamisen ongelmaan.

___

Kun kerrot kaksi lukua, sanotaan $a$ ja $b$, kutsumme lukuja $a$ ja $b$ **tekijöiksi** ja tulosta **tulokseksi**. Yritystä kirjoittaa luku $N$ kahden tai useamman tekijän kertolaskuna kutsutaan **tekijöihin jakamiseksi** tai **tekijöintiksi**. [1] Voit kutsua mitä tahansa tällaista vaativaa ongelmaa **tekijöihin jakamisen ongelmaksi**.

Noin 2 500 vuotta sitten kreikkalainen matemaatikko Eukleides Aleksandrialainen löysi avainlauseen kokonaislukujen tekijöihin jakamisesta. Sitä kutsutaan yleisesti **yksikäsitteisen tekijöihin jakamisen teoreemaksi** ja se toteaa seuraavaa:

**Teoreema 1**. Jokainen kokonaisluku $N$, joka on suurempi kuin 1, on joko alkuluku tai voidaan ilmaista alkutekijöiden tulona.
Tämän lausunnon jälkimmäinen osa tarkoittaa vain sitä, että voit ottaa minkä tahansa ei-alkuluvun $N$, joka on suurempi kuin 1, ja kirjoittaa sen alkulukujen kertolaskuna. Alla on useita esimerkkejä ei-alkuluvuista kirjoitettuna alkulukujen tuloina.
* $18 = 2 \cdot 3 \cdot 3 = 2 \cdot 3^2$
* $84 = 2 \cdot 2 \cdot 3 \cdot 7 = 2^2 \cdot 3 \cdot 7$
* $144 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 = 2^4 \cdot 3^2$

Kaikille yllä mainituille kokonaisluvuille niiden alkutekijöiden laskeminen on suhteellisen helppoa, vaikka sinulle annettaisiin vain $N$. Aloitat pienimmästä alkuluvusta, eli 2:sta, ja tarkistat, kuinka monta kertaa kokonaisluku $N$ on jaollinen sillä. Sitten siirryt tarkistamaan $N$:n jaollisuutta 3:lla, 5:llä, 7:llä ja niin edelleen. Jatkat tätä prosessia, kunnes kokonaislukusi $N$ on kirjoitettu vain alkulukujen tulona.

Ota esimerkiksi kokonaisluku 84. Alla näet prosessin sen alkutekijöiden määrittämiseksi. Jokaisessa vaiheessa otamme pienimmän jäljellä olevan alkutekijän (vasemmalla) ja määritämme jäljelle jäävän termin, joka on tekijöitävä. Jatkamme, kunnes jäljelle jäävä termi on myös alkuluku. Jokaisessa vaiheessa 84:n nykyinen tekijöinti näytetään oikealla puolella.

* Alkutekijä = 2: jäljelle jäävä termi = 42 	($84 = 2 \cdot 42$)
* Alkutekijä = 2: jäljelle jäävä termi = 21 	($84 = 2 \cdot 2 \cdot 21$)
* Alkutekijä = 3: jäljelle jäävä termi = 7 	($84 = 2 \cdot 2 \cdot 3 \cdot 7$)
* Koska 7 on alkuluku, tulos on $2 \cdot 2 \cdot 3 \cdot 7$, eli $2^2 \cdot 3 \cdot 7$.

Oletetaan nyt, että $N$ on erittäin suuri. Kuinka vaikeaa olisi jakaa $N$ sen alkutekijöihin?

Se todella riippuu $N$:stä. Oletetaan esimerkiksi, että $N$ on 50,450,400. Vaikka tämä luku näyttää pelottavalta, laskelmat eivät ole niin monimutkaisia ja ne voidaan helposti tehdä käsin. Kuten yllä, aloitat vain 2:sta ja jatkat eteenpäin. Alla näet tämän prosessin tuloksen samalla tavalla kuin yllä.

* 2: 25,225,200 	($50,450,400 = 2 \cdot 25,225,200$)  
* 2: 12,612,600 	($50,450,400 = 2^2 \cdot 12,612,600$)  
* 2: 6,306,300 	($50,450,400 = 2^3 \cdot 6,306,300$)  
* 2: 3,153,150 	($50,450,400 = 2^4 \cdot 3,153,150$)  
* 2: 1,576,575 	($50,450,400 = 2^5 \cdot 1,576,575$)
* 3: 525,525 ($50,450,400 = 2^5 \cdot 3 \cdot 525,525$)
* 3: 175,175 ($50,450,400 = 2^5 \cdot 3^2 \cdot 175,175$)
* 5: 35,035 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5 \cdot 35,035$)
* 5: 7,007 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7,007$)
* 7: 1,001 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7 \cdot 1,001$)
* 7: 143 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 143$)
* 11: 13 ($50,450,400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$)
* Koska 13 on alkuluku, tulos on $2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$.

Tämän ongelman ratkaiseminen käsin vie jonkin aikaa. Tietokone, tietenkin, voisi tehdä kaiken tämän murto-osassa sekunnista. Itse asiassa tietokone voi usein jopa tekijöidä erittäin suuret kokonaisluvut murto-osassa sekunnista.

On kuitenkin tiettyjä poikkeuksia. Oletetaan, että valitsemme ensin kaksi hyvin suurta alkulukua satunnaisesti. On tyypillistä merkitä nämä $p$ ja $q$, ja minä noudatan tätä käytäntöä tässä.

Konkreettisesti sanottuna, oletetaan että $p$ ja $q$ ovat molemmat 1024-bittisiä alkulukuja, ja että ne todellakin vaativat vähintään 1024 bittiä voidakseen olla esitettyinä (joten ensimmäisen bitin täytyy olla 1). Joten esimerkiksi 37 ei voisi olla yksi alkuluvuista. Voit varmasti esittää 37:n 1024 bitillä. Mutta selvästi *et tarvitse* näin monta bittiä sen esittämiseen. Voit esittää 37:n millä tahansa merkkijonolla, jossa on 6 bittiä tai enemmän. (6 bitissä 37 esitettäisiin muodossa $100101$).

On tärkeää ymmärtää, kuinka suuria $p$ ja $q$ ovat, jos ne valitaan yllä mainituin ehdoin. Esimerkkinä olen valinnut satunnaisen alkuluvun, joka vaatii vähintään 1024 bittiä esitykseen alla.
* 14 752 173 874 503 595 484 930 006 383 670 759 559 764 562 721 397 166 747 289 220 945 457 932 666 751 048 198 854 920 097 085 690 793 755 254 946 188 163 753 506 778 089 706 699 671 722 089 715 624 760 049 594 106 189 662 669 156 149 028 900 805 928 183 585 427 782 974 951 355 515 394 807 209 836 870 484 558 332 897 443 152 653 214 483 870 992 618 171 825 921 582 253 023 974 514 209 142 520 026 807 636 589

Oletetaan nyt, että satunnaisesti valitsemme alkuluvut $p$ ja $q$, ja kerromme ne saadaksemme kokonaisluvun $N$. Tämä jälkimmäinen kokonaisluku on siis 2048-bittinen numero, joka vaatii vähintään 2048 bittiä esittääkseen. Se on paljon, paljon suurempi kuin kumpikaan $p$ tai $q$.

Oletetaan, että annat tietokoneelle vain $N$:n ja pyydät sitä löytämään $N$:n kaksi 1024-bittistä alkulukutekijää. Todennäköisyys, että tietokone löytää $p$:n ja $q$:n, on äärimmäisen pieni. Voit sanoa, että se on käytännössä mahdotonta. Näin on, vaikka käyttäisit superkonetta tai jopa superkoneiden verkostoa.

Aloitetaan siitä, että tietokone yrittää ratkaista ongelman kiertämällä 1024-bittisiä numeroita, testaten jokaisessa tapauksessa, ovatko ne alkulukuja ja ovatko ne $N$:n tekijöitä. Testattavien alkulukujen joukko on sitten suunnilleen $1.265 \cdot 10^{305}$. [2]

Vaikka ottaisit kaikki maapallon tietokoneet ja antaisit niiden yrittää löytää ja testata 1024-bittisiä alkulukuja tällä tavalla, miljardissa yhden mahdollisuus onnistuneesti löytää alkulukutekijä $N$:lle vaatisi laskenta-aikaa, joka on paljon pitempi kuin maailmankaikkeuden ikä.

Käytännössä tietokone voi kuitenkin toimia paremmin kuin juuri kuvattu karkea menetelmä. On olemassa useita algoritmeja, joita tietokone voi soveltaa päästäkseen tekijöihin nopeammin. Pointti kuitenkin on, että jopa näitä tehokkaampia algoritmeja käyttäen tietokoneen tehtävä on edelleen laskennallisesti mahdoton. [3]

Tärkeää on, että tekijöihin jakamisen vaikeus juuri kuvatuissa olosuhteissa perustuu oletukseen, että ei ole laskennallisesti tehokkaita algoritmeja alkulukutekijöiden laskemiseen. Emme voi todellisuudessa todistaa, että tehokasta algoritmia ei ole olemassa. Siitä huolimatta tämä oletus on hyvin uskottava: huolimatta satoja vuosia kestäneistä laajoista ponnisteluista, emme ole vielä löytäneet tällaista laskennallisesti tehokasta algoritmia.

Siksi tekijöihin jakamisen ongelma, tietyissä olosuhteissa, voidaan uskottavasti olettaa olevan vaikea ongelma. Erityisesti, kun $p$ ja $q$ ovat hyvin suuria alkulukuja, niiden tulo $N$ ei ole vaikea laskea; mutta tekijöihin jakaminen pelkästään annetulla $N$:llä on käytännössä mahdotonta.

**Huomautukset:**

[1] Tekijöihin jakaminen voi olla myös tärkeää muiden kuin numeroiden matemaattisten objektien kanssa työskentelyssä. Esimerkiksi polynomilausekkeiden, kuten $x^2 - 2x + 1$, tekijöihin jakaminen voi olla hyödyllistä. Keskustelussamme keskitymme kuitenkin vain numeroiden, erityisesti kokonaislukujen, tekijöihin jakamiseen.
[2] **Alkulukuteoreeman** mukaan alkulukujen määrä, jotka ovat pienempiä tai yhtä suuria kuin $N$, on suunnilleen $N/\ln(N)$. Tämä tarkoittaa, että voit arvioida 1024-bittisten alkulukujen määrän kaavalla: 
$$ \frac{2^{1024}}{\ln(2^{1024})} - \frac{2^{1023}}{\ln(2^{1023})} $$

...mikä on suunnilleen $1.265 \times 10^{305}$.

[3] Sama pätee diskreetin logaritmin ongelmiin. Tästä syystä asymmetriset rakenteet toimivat paljon suuremmilla avaimilla kuin symmetriset kryptografiset rakenteet.

## Lukuteorian tulokset
<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>

Valitettavasti tekijöihin jakamisen ongelmaa ei voida käyttää suoraan asymmetrisissä kryptografisissa järjestelmissä. Voimme kuitenkin käyttää monimutkaisempaa, mutta siihen liittyvää ongelmaa tähän tarkoitukseen: RSA-ongelmaa.

RSA-ongelman ymmärtämiseksi meidän on tunnettava useita lukuteorian teoreemoja ja väitteitä. Nämä esitetään tässä osiossa kolmessa alaosiossa: (1) N:n järjestys, (2) kääntyvyys modulo N ja (3) Eulerin teoreema.

Osa tässä kolmessa alaosiossa esitellystä materiaalista on jo esitelty *Luvussa 3*. Mutta esitän tässä materiaalin uudelleen mukavuuden vuoksi.

### N:n järjestys

Kokonaisluku $a$ on **keskenään jaoton** tai **suhteellinen alkuluku** kokonaisluvun $N$ kanssa, jos niiden suurin yhteinen tekijä on 1. Vaikka 1 ei perinteisesti ole alkuluku, se on jokaisen kokonaisluvun keskenään jaoton (kuten myös $-1$).

Esimerkiksi, kun $a = 18$ ja $N = 37$, ne ovat selvästi keskenään jaottomia. Suurin kokonaisluku, joka jakaa sekä 18 että 37, on 1. Sen sijaan, kun $a = 42$ ja $N = 16$, ne eivät selvästi ole keskenään jaottomia. Molemmat luvut ovat jaollisia 2:lla, joka on suurempi kuin 1.

Voimme nyt määritellä $N$:n järjestyksen seuraavasti. Oletetaan, että $N$ on kokonaisluku, joka on suurempi kuin 1. **N:n järjestys** on silloin kaikkien $N$:n kanssa keskenään jaottomien lukumäärä siten, että jokaiselle keskenään jaottomalle $a$ pätee seuraava ehto: $1 \leq a < N$.

Esimerkiksi, jos $N = 12$, niin 1, 5, 7 ja 11 ovat ainoat keskenään jaottomat, jotka täyttävät yllä olevan vaatimuksen. Siksi 12:n järjestys on yhtä suuri kuin 4.

Oletetaan, että $N$ on alkuluku. Silloin mikä tahansa kokonaisluku, joka on pienempi kuin $N$ mutta suurempi tai yhtä suuri kuin 1, on keskenään jaoton sen kanssa. Tämä sisältää kaikki seuraavan joukon alkiot: $\{1,2,3,….,N - 1\}$. Siksi, kun $N$ on alkuluku, $N$:n järjestys on $N - 1$. Tämä on esitetty väitteessä 1, jossa $\phi(N)$ merkitsee $N$:n järjestystä.

**Väite 1**. $\phi(N) = N - 1$ kun $N$ on alkuluku
Oletetaan, että $N$ ei ole alkuluku. Voit silloin laskea sen järjestyksen käyttäen **Eulerin Phi-funktiota**. Vaikka pienen kokonaisluvun järjestyksen laskeminen on suhteellisen yksinkertaista, Eulerin Phi-funktio muuttuu erityisen tärkeäksi suurten kokonaislukujen kohdalla. Eulerin Phi-funktion ehdotus on esitetty alla.

**Lause 2**. Olkoon $N = p_1^{e_1} \cdot p_2^{e_2} \cdot \ldots \cdot p_i^{e_i} \cdot \ldots \cdot p_n^{e_n}$, missä joukko $\{p_i\}$ koostuu kaikista $N$:n erillisistä alkutekijöistä ja jokainen $e_i$ ilmaisee, kuinka monta kertaa alkutekijä $p_i$ esiintyy $N$:ssä. Silloin,

$$\phi(N) = p_1^{e_1 - 1} \cdot (p_1 - 1) \cdot p_2^{e_2 - 1} \cdot (p_2 - 1) \cdot \ldots \cdot p_n^{e_n - 1} \cdot (p_n - 1)$$

**Lause 2** osoittaa, että kun olet jakauttanut minkä tahansa ei-alkuluvun $N$ sen erillisiin alkutekijöihin, on helppoa laskea $N$:n järjestys.

Esimerkiksi, oletetaan että $N = 270$. Tämä ei selvästikään ole alkuluku. Jakamalla $N$ sen alkutekijöihin saadaan lauseke: $2 \cdot 3^3 \cdot 5$. Eulerin Phi-funktion mukaan $N$:n järjestys on silloin seuraava:

$$\phi(N) = 2^{1 - 1} \cdot (2 - 1) + 3^{3 - 1} \cdot (3 - 1) + 5^{1 - 1} \cdot (5 - 1) = 1 \cdot 1 + 9 \cdot 2 + 1 \cdot 4 = 1 + 18 + 4 = 23$$

Oletetaan seuraavaksi, että $N$ on kahden alkuluvun, $p$ ja $q$, tulo. **Lause 2** yllä, silloin, toteaa, että $N$:n järjestys on seuraava:

$$p^{1 - 1} \cdot (p - 1) \cdot q^{1 - 1} \cdot (q - 1) = (p - 1) \cdot (q - 1)$$

Tämä on keskeinen tulos erityisesti RSA-ongelmassa, ja se on esitetty **Ehdotuksessa 2** alla.

**Ehdotus 2**. Jos $N$ on kahden alkuluvun, $p$ ja $q$, tulo, $N$:n järjestys on tulo $(p - 1) \cdot (q - 1)$.

Havainnollistaaksemme, oletetaan, että $N = 119$. Tämä kokonaisluku voidaan jakaa kahteen alkulukuun, nimittäin 7 ja 17. Siksi Eulerin Phi-funktio ehdottaa, että 119:n järjestys on seuraava:

$$\phi(119) = (7 - 1) \cdot (17 - 1) = 6 \cdot 16 = 96$$

Toisin sanoen, kokonaisluvulla 119 on 96 koprimiä välillä 1–119. Itse asiassa, tämä joukko sisältää kaikki kokonaisluvut 1–119, jotka eivät ole jommankumman 7 tai 17 kertoimia.
Tästä eteenpäin merkitkäämme joukkoa, joka määrittää $N$:n järjestyksen, koprimiluvuilla $C_N$. Esimerkiksemme, kun $N = 119$, joukko $C_{119}$ on aivan liian suuri lueteltavaksi kokonaan. Mutta jotkin elementit ovat seuraavat:
$$C_{119} = \{1, 2, \dots 6, 8 \dots 13, 15, 16, 18, \dots 33, 35 \dots 96\}$$

### Kääntyvyys modulo N

Voimme sanoa, että kokonaisluku $a$ on **kääntyvä modulo N**, jos olemassa on ainakin yksi kokonaisluku $b$ siten, että $a \cdot b \mod N = 1 \mod N$. Mitä tahansa tällaista kokonaislukua $b$ kutsutaan $a$:n **käänteisluvuksi** (tai **kertolaskun käänteisluvuksi**) modulo $N$ suhteen.

Oletetaan esimerkiksi, että $a = 5$ ja $N = 11$. On monia kokonaislukuja, joilla voit kertoa 5:n, niin että $5 \cdot b \mod 11 = 1 \mod 11$. Harkitse esimerkiksi kokonaislukuja 20 ja 31. On helppo nähdä, että molemmat nämä kokonaisluvut ovat 5:n käänteislukuja modulo 11 suhteen.

* $5 \cdot 20 \mod 11 = 100 \mod 11 = 1 \mod 11$
* $5 \cdot 31 \mod 11 = 155 \mod 11 = 1 \mod 11$

Vaikka 5:llä on monta käänteislukua modulo 11 suhteen, voit osoittaa, että vain yksi positiivinen käänteisluku 5:lle on olemassa, joka on pienempi kuin 11. Itse asiassa, tämä ei ole ainutlaatuista meidän erityiselle esimerkillemme, vaan yleinen tulos.

**Väite 3**. Jos kokonaisluku $a$ on kääntyvä modulo $N$, täytyy olla niin, että tarkalleen yksi positiivinen käänteisluku $a$:lle on pienempi kuin $N$. (Joten, tämä ainutlaatuinen käänteisluku $a$:lle täytyy tulla joukosta $\{1, \dots, N - 1\}$).

Merkitkäämme **Väite 3**:n ainutlaatuista käänteislukua $a$:lle $a^{-1}$. Tapauksessa, kun $a = 5$ ja $N = 11$, voit nähdä, että $a^{-1} = 9$, ottaen huomioon, että $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$.

Huomaa, että voit myös saada arvon 9 $a^{-1}$:lle esimerkissämme yksinkertaisesti vähentämällä mitä tahansa muuta $a$:n käänteislukua modulo 11. Esimerkiksi, $20 \mod 11 = 31 \mod 11 = 9 \mod 11$. Joten aina kun kokonaisluku $a > N$ on kääntyvä modulo $N$, silloin $a \mod N$ täytyy myös olla kääntyvä modulo $N$.

Ei ole välttämättä niin, että $a$:n käänteisluku on olemassa modulo $N$ suhteen. Oletetaan esimerkiksi, että $a = 2$ ja $N = 8$. Ei ole olemassa $b$:tä, tai mitään $a^{-1}$:ä erityisesti, siten, että $2 \cdot b \mod 8 = 1 \mod 8$. Tämä johtuu siitä, että mikä tahansa $b$:n arvo tuottaa aina 2:n kertoman, joten jaolla 8:lla ei koskaan voi saada jäännöstä, joka olisi yhtä suuri kuin 1.
Miten tarkalleen ottaen voimme tietää, onko jollakin kokonaisluvulla $a$ käänteisalkio annetulle $N$:lle? Kuten ehkä huomasit yllä olevassa esimerkissä, suurin yhteinen tekijä 2:n ja 8:n välillä on suurempi kuin 1, nimittäin 2. Ja tämä on itse asiassa esimerkki seuraavasta yleisestä tuloksesta:
**Propositio 4**. Käänteisalkio kokonaisluvulle $a$ modulo $N$ -reduktiossa, ja erityisesti yksikäsitteinen positiivinen käänteisalkio, joka on pienempi kuin $N$, on olemassa vain ja ainoastaan, jos suurin yhteinen tekijä $a$:n ja $N$:n välillä on 1 (eli jos ne ovat keskenään alkulukuja).

Tapauksessa, kun $a = 5$ ja $N = 11$, tulimme siihen tulokseen, että $a^{-1} = 9$, koska $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$. On tärkeää huomata, että päinvastainenkin pätee. Eli kun $a = 9$ ja $N = 11$, pätee, että $a^{-1} = 5$.

### Eulerin teoreema

Ennen kuin siirrymme RSA-ongelmaan, meidän on ymmärrettävä vielä yksi ratkaiseva teoreema, nimittäin **Eulerin teoreema**. Se toteaa seuraavaa:

**Teoreema 3**. Oletetaan, että kaksi kokonaislukua $a$ ja $N$ ovat keskenään alkulukuja. Silloin $a^{\phi(N)} \mod N = 1 \mod N$.

Tämä on merkittävä tulos, mutta hieman hämmentävä ensi alkuun. Käännymme esimerkin puoleen ymmärtääksemme sen.

Oletetaan, että $a = 5$ ja $N = 7$. Nämä ovat todellakin keskenään alkulukuja, kuten Eulerin teoreema vaatii. Tiedämme, että 7:n järjestys on 6, koska 7 on alkuluku (katso **Propositio 1**).

Mitä Eulerin teoreema nyt toteaa, on, että $5^6 \mod 7$ täytyy olla yhtä kuin $1 \mod 7$. Alla olevat laskelmat osoittavat, että näin todellakin on.

* $5^6 \mod 7 = 15,625 \mod 7 = 1 \mod N$

Kokonaisluku 7 jakautuu 15,624:ään yhteensä 2,233 kertaa. Näin ollen, jakojäännös, kun 16,625 jaetaan 7:llä, on 1.

Seuraavaksi, käyttäen Eulerin Phi-funktiota, **Teoreema 2**, voit johtaa alla olevan **Proposition 5**.

**Propositio 5**. $\phi(a \cdot b) = \phi(a) \cdot \phi(b)$ mille tahansa positiivisille kokonaisluvuille $a$ ja $b$.

Emme näytä, miksi näin on. Mutta huomaa vain, että olet jo nähnyt todisteita tästä propositiosta tosiasian perusteella, että $\phi(p \cdot q) = \phi(p) \cdot \phi(q) = (p - 1) \cdot (q - 1)$, kun $p$ ja $q$ ovat alkulukuja, kuten **Propositio 2** toteaa.

Eulerin teoreeman yhdessä **Proposition 5**:n kanssa on tärkeitä seurauksia. Katso, mitä tapahtuu esimerkiksi alla olevissa lausekkeissa, joissa $a$ ja $N$ ovat keskenään alkulukuja.

* $a^{2 \cdot \phi(N)} \mod N = a^{\phi(N)} \cdot a^{\phi(N)} \mod N = 1 \cdot 1 \mod N = 1 \mod N$
* $a^{\phi(N) + 1} \mod N = a^{\phi(N)} \cdot a^1 \mod N = 1 \cdot a^1 \mod N = a \mod N$
* $a^{8 \cdot \phi(N) + 3} \mod N = a^{8 \cdot \phi(N)} \cdot a^3 \mod N = 1 \cdot a^3 \mod N = a^3 \mod N$

Näin ollen Eulerin teoreeman ja **Proposition 5** yhdistelmä mahdollistaa useiden lausekkeiden yksinkertaisen laskemisen. Yleisesti voimme tiivistää oivalluksen **Proposition 6** mukaisesti.

**Proposition 6**. $a^x \mod N = a^{x \mod \phi(N)}$

Nyt meidän täytyy koota kaikki yhteen viimeisessä hankalassa vaiheessa.

Aivan kuten $N$:llä on järjestys $\phi(N)$, joka sisältää joukon $C_N$ elementit, tiedämme, että kokonaisluvulla $\phi(N)$ täytyy vuorostaan myös olla järjestys ja koprimien joukko. Asetetaan $\phi(N) = R$. Sitten tiedämme, että on olemassa myös arvo $\phi(R)$ ja koprimien joukko $C_R$.

Oletetaan, että nyt valitsemme kokonaisluvun $e$ joukosta $C_R$. Tiedämme **Proposition 3** perusteella, että tällä kokonaisluvulla $e$ on vain yksi uniikki positiivinen käänteisluku, joka on pienempi kuin $R$. Toisin sanoen, $e$:llä on yksi uniikki käänteisluku joukosta $C_R$. Kutsutaan tätä käänteislukua $d$:ksi. Käänteisluvun määritelmän perusteella tämä tarkoittaa, että $e \cdot d = 1 \mod R$.

Voimme käyttää tätä tulosta tekemään lausunnon alkuperäisestä kokonaisluvustamme $N$. Tämä on tiivistetty **Proposition 7**.

**Proposition 7**. Oletetaan, että $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Silloin minkä tahansa elementin $a$ joukosta $C_N$ täytyy olla niin, että $a^{e \cdot d \mod \phi(N)} = a^{1 \mod \phi(N)} = a \mod N$.

Nyt meillä on kaikki lukuteoreettiset tulokset, jotka tarvitaan RSA-ongelman selkeään esittämiseen.

## RSA-salakirjoitusjärjestelmä
<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>

Olemme nyt valmiita esittämään RSA-ongelman. Oletetaan, että luot muuttujien joukon, joka koostuu $p$:stä, $q$:sta, $N$:stä, $\phi(N)$:stä, $e$:stä, $d$:stä ja $y$:stä. Kutsu tätä joukkoa $\Pi$. Se luodaan seuraavasti:

1. Generoi kaksi satunnaista alkulukua $p$ ja $q$ samasta suuruusluokasta ja laske niiden tulo $N$.
2. Laske $N$:n järjestys, $\phi(N)$, seuraavan tulon avulla: $(p - 1) \cdot (q - 1)$.
3. Valitse $e > 2$ siten, että se on pienempi ja koprimi $\phi(N)$:n kanssa.
4. Laske $d$ asettamalla $e \cdot d \mod \phi(N) = 1$.
5. Valitse satunnainen arvo $y$, joka on pienempi ja koprimi $N$:n kanssa.
RSA-ongelma koostuu $x$:n löytämisestä siten, että $x^e = y$, kun annettuna on vain osajoukko tietoa $\Pi$:stä, nimittäin muuttujat $N$, $e$ ja $y$. Kun $p$ ja $q$ ovat hyvin suuria, tyypillisesti suositellaan, että ne ovat 1024 bittiä kooltaan, RSA-ongelman ajatellaan olevan vaikea. Nyt voit nähdä, miksi näin on edellä käydyn keskustelun perusteella.

Helppo tapa laskea $x$, kun $x^e \mod N = y \mod N$, on yksinkertaisesti laskemalla $y^d \mod N$. Tiedämme, että $y^d \mod N = x \mod N$ seuraavien laskutoimitusten perusteella:

$$ y^d \mod N = x^{e \cdot d} \mod N = x^{e \cdot d \mod \phi(N)} \mod N = x^{1 \mod \phi(N)} \mod N = x \mod N. $$

Ongelmana on, että emme tiedä arvoa $d$, koska sitä ei anneta ongelmassa. Siksi emme voi suoraan laskea $y^d \mod N$ tuottaaksemme $x \mod N$.

Saattaisimme kuitenkin pystyä epäsuorasti laskemaan $d$:n $N$:n järjestyksestä, $\phi(N)$, koska tiedämme, että $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Mutta oletuksen mukaan ongelma ei anna arvoa $\phi(N)$:lle myöskään.

Lopulta järjestyksen voisi laskea epäsuorasti alkulukujen $p$ ja $q$ avulla, jotta lopulta voisimme laskea $d$:n. Mutta oletuksen mukaan arvot $p$ ja $q$ eivät myöskään olleet meille annettuja.

Tiukasti ottaen, vaikka faktorointiongelma RSA-ongelman sisällä on vaikea, emme voi todistaa, että RSA-ongelma itsessään on myös vaikea. Saattaa nimittäin olla muita tapoja ratkaista RSA-ongelma kuin faktoroinnin kautta. Kuitenkin yleisesti hyväksytään ja oletetaan, että jos faktorointiongelma RSA-ongelman sisällä on vaikea, myös RSA-ongelma itsessään on vaikea.

Jos RSA-ongelma todella on vaikea, se tuottaa yksisuuntaisen funktion ansaluukulla. Tässä funktio on $f(g) = g^e \mod N$. Tietäen $f(g)$, kuka tahansa voisi helposti laskea arvon $y$ tietylle $g = x$. Kuitenkin on käytännössä mahdotonta laskea tiettyä arvoa $x$ vain tietäen arvon $y$ ja funktion $f(g)$. Poikkeus on, kun sinulle annetaan tieto $d$, ansaluukku. Tässä tapauksessa voit yksinkertaisesti laskea $y^d$ antaaksesi $x$.

Käydään läpi tietty esimerkki havainnollistaaksemme RSA-ongelmaa. En voi valita RSA-ongelmaa, jota pidettäisiin vaikeana yllä olevien ehtojen mukaisesti, koska numerot olisivat hankalia käsitellä. Sen sijaan tämä esimerkki on vain havainnollistamaan, miten RSA-ongelma yleisesti toimii.

Aloitetaan olettamalla, että valitset kaksi satunnaista alkulukua 13 ja 31. Joten $p = 13$ ja $q = 31$. Näiden kahden alkuluvun tulo $N$ on 403. Voimme helposti laskea 403:n järjestyksen. Se vastaa $(13 - 1) \cdot (31 - 1) = 360$.
Seuraavaksi, kuten RSA-ongelman vaihe 3 määrää, meidän on valittava 360:lle suhteellinen alkuluku, joka on suurempi kuin 2 ja pienempi kuin 360. Meidän ei tarvitse valita tätä arvoa satunnaisesti. Oletetaan, että valitsemme 103. Tämä on 360:n suhteellinen alkuluku, koska sen suurin yhteinen jakaja 103:n kanssa on 1.
Vaihe 4 vaatii nyt, että laskemme arvon $d$ siten, että $103 \cdot d \mod 360 = 1$. Tämä ei ole helppo tehtävä käsin, kun arvo $N$ on suuri. Se vaatii menetelmän käyttöä, jota kutsutaan **laajennetuksi Eukleidekseksi algoritmiksi**.

Vaikka en näytä menettelyä tässä, se tuottaa arvon 7, kun $e = 103$. Voit varmistaa, että arvopari 103 ja 7 todellakin täyttää yleisen ehdon $e \cdot d \mod \phi(n) = 1$ alla olevien laskelmien kautta.

* $103 \cdot 7 \mod 360 = 721 \mod 360 = 1 \mod 360$

Tärkeää on, että *Proposition 4*:n perusteella tiedämme, että mikään muu kokonaisluku välillä 1 ja 360 arvolle $d$ ei tuota tulosta, että $103 \cdot d = 1 \mod 360$. Lisäksi ehdotus viittaa siihen, että eri arvon valitseminen $e$:lle, tuottaa eri yksilöllisen arvon $d$:lle.

RSA-ongelman vaiheessa 5 meidän on valittava jokin positiivinen kokonaisluku $y$, joka on 403:n pienempi suhteellinen alkuluku. Oletetaan, että asetamme $y = 2^{103}$. Kahden eksponentointi 103:lla tuottaa alla olevan tuloksen.

* $2^{103} \mod 403 = 10,141,204,801,825,835,211,973,625,643,008 \mod 403 = 349 \mod 403$

RSA-ongelma tässä erityisesimerkissä on nyt seuraava: Sinulle annetaan $N = 403$, $e = 103$, ja $y = 349 \mod 403$. Sinun on nyt laskettava $x$ siten, että $x^{103} = 349 \mod 403$. Toisin sanoen, sinun on löydettävä alkuperäinen arvo ennen eksponentointia 103:lla, joka oli 2.

Olisi helppoa (ainakin tietokoneelle) laskea $x$, jos tietäisimme, että $d = 7$. Tässä tapauksessa voisit vain määrittää $x$:n alla olevan mukaisesti.

* $x = y^7 \mod 403 = 349^7 \mod 403 = 630,634,881,591,804,949 \mod 403 = 2 \mod 403$

Ongelmana on, että sinulle ei ole annettu tietoa, että $d = 7$. Voisit tietenkin laskea $d$:n siitä tosiasiasta, että $103 \cdot d = 1 \mod 360$. Ongelmana on, että sinulle ei myöskään ole annettu tietoa, että $N$:n järjestys on 360. Lopuksi, voisit myös laskea 403:n järjestyksen laskemalla seuraavan tulon: $(p - 1) \cdot (q - 1)$. Mutta sinulle ei myöskään kerrota, että $p = 13$ ja $q = 31$.

Tietysti tietokone voisi silti suhteellisen helposti ratkaista RSA-ongelman tässä esimerkissä, koska mukana olevat alkuluvut eivät ole suuria. Mutta kun alkuluvut muuttuvat hyvin suuriksi, se kohtaa käytännössä mahdottoman tehtävän.
Olemme nyt esitelleet RSA-ongelman, joukon ehtoja, joiden vallitessa ongelma on vaikea, sekä taustalla olevan matematiikan. Miten mikään tästä auttaa epäsymmetrisen kryptografian kanssa? Erityisesti, miten voimme muuttaa RSA-ongelman vaikeuden tietyissä olosuhteissa salausjärjestelmäksi tai digitaaliseksi allekirjoitusjärjestelmäksi?
Yksi lähestymistapa on ottaa RSA-ongelma ja rakentaa järjestelmiä suoraviivaisella tavalla. Kuvitellaan esimerkiksi, että loit muuttujajoukon $\Pi$ kuten RSA-ongelmassa on kuvattu, ja varmistat, että $p$ ja $q$ ovat riittävän suuria. Asetat julkisen avaimen arvoksi $(N, e)$ ja jaat tämän tiedon maailmalle. Kuten yllä on kuvattu, pidät $p$:n, $q$:n, $\phi(n)$:n ja $d$:n arvot salaisina. Itse asiassa $d$ on yksityinen avaimesi.

Kuka tahansa, joka haluaa lähettää sinulle viestin $m$, joka on elementti $C_N$:ssä, voisi yksinkertaisesti salata sen seuraavasti: $c = m^e \mod N$. (Tässä salattu teksti $c$ vastaa arvoa $y$ RSA-ongelmassa.) Voit helposti purkaa tämän viestin vain laskemalla $c^d \mod N$.

Saatat myös yrittää luoda digitaalisen allekirjoitusjärjestelmän samalla tavalla. Kuvitellaan, että haluat lähettää jollekulle viestin $m$ digitaalisella allekirjoituksella $S$. Voisit asettaa $S = m^d \mod N$ ja lähettää parin $(m,S)$ vastaanottajalle. Kuka tahansa voi varmistaa digitaalisen allekirjoituksen vain tarkistamalla, vastaako $S^e \mod N = m \mod N$. Hyökkääjällä olisi kuitenkin todella vaikea aika luoda kelvollinen $S$ viestille, koska he eivät omista $d$:tä.

Valitettavasti RSA-ongelman, joka itsessään on vaikea ongelma, muuttaminen kryptografiseksi järjestelmäksi ei ole näin suoraviivaista. Suoraviivaisessa salausjärjestelmässä voit valita vain $N$:n koprimiluvut viesteiksesi. Tämä ei jätä meille montaa mahdollista viestiä, varmasti ei tarpeeksi standardiviestintään. Lisäksi nämä viestit on valittava satunnaisesti. Tämä vaikuttaa jokseenkin epäkäytännölliseltä. Lopuksi, mikä tahansa viesti, joka valitaan kahdesti, tuottaa täsmälleen saman salatun tekstin. Tämä on erittäin epätoivottavaa missä tahansa salausjärjestelmässä eikä täytä mitään tiukkaa nykyaikaista turvallisuuden standardikäsitystä salauksessa.

Ongelmat pahenevat entisestään suoraviivaisessa digitaalisessa allekirjoitusjärjestelmässämme. Nykyisellään mikä tahansa hyökkääjä voi helposti väärentää digitaalisia allekirjoituksia valitsemalla ensin $N$:n koprimiluvun allekirjoitukseksi ja sitten laskemalla vastaavan alkuperäisen viestin. Tämä selvästi rikkoo eksistentiaalisen väärentämättömyyden vaatimusta.

Siitä huolimatta, lisäämällä hieman ovelaa monimutkaisuutta, RSA-ongelmaa voidaan käyttää luomaan turvallinen julkinen avain salausjärjestelmä sekä turvallinen digitaalinen allekirjoitusjärjestelmä. Emme syvenny näiden rakenteiden yksityiskohtiin tässä. [4] Tärkeää on kuitenkin, että tämä lisämonimutkaisuus ei muuta perustavanlaatuista taustalla olevaa RSA-ongelmaa, johon nämä järjestelmät perustuvat.

**Huomautukset:**

[4] Katso esimerkiksi Jonathan Katz ja Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), s. 410–32 RSA-salauksesta ja s. 444–41 RSA-digitaalisista allekirjoituksista.