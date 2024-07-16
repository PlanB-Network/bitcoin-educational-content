---
name: JoinBot
description: JoinBotin ymmärtäminen ja käyttäminen
---

![DALL·E – samurairobotti punaisessa metsässä, 3D-renderöinti](assets/cover.webp)

***VAROITUS:** Samourai Walletin perustajien pidätyksen ja heidän palvelimiensa takavarikoinnin jälkeen 24. huhtikuuta **JoinBot-palvelu ei ole enää saatavilla**. Tällä hetkellä tämän työkalun käyttö ei ole mahdollista. Voit kuitenkin edelleen suorittaa Stonewall X2 -toiminnon, mutta sinun on löydettävä yhteistyökumppani ja vaihdettava PSBT:t manuaalisesti. Tämä palvelu saatetaan käynnistää uudelleen tulevina kuukausina riippuen tapauksen etenemisestä.*

_Seuraamme tiiviisti tämän tapauksen kehitystä sekä siihen liittyvien työkalujen kehitystä. Voitte olla varmoja, että päivitämme tämän oppaan, kun uutta tietoa tulee saataville._

_Tämä opas on tarkoitettu vain koulutus- ja tiedotustarkoituksiin. Emme kannusta tai hyväksy näiden työkalujen käyttöä rikollisiin tarkoituksiin. Jokaisen käyttäjän on noudatettava oman lainkäyttöalueensa lakeja._

---

JoinBot on uusi työkalu, joka on lisätty Samourai Wallet -pakettiin viimeisimmässä 0.99.98f päivityksessä kuuluisaan Bitcoin-lompakko-ohjelmistoon. Se mahdollistaa yhteistyössä tehtävän transaktion helposti yksityisyytesi optimoimiseksi, ilman että sinun tarvitsee etsiä kumppania.

*Kiitokset erinomaiselle Fanis Michalakisille ideasta käyttää DALL-E:tä pikkukuvana!*

## Mikä on yhteistyössä tehtävä transaktio Bitcoinissa?

Bitcoin perustuu hajautettuun ja läpinäkyvään tilikirjaan. Kuka tahansa pystyy jäljittämään tämän elektronisen käteisjärjestelmän käyttäjien transaktioita. Tietyn tason yksityisyyden varmistamiseksi Bitcoin-käyttäjät voivat tehdä transaktioita erityisellä rakenteella lisätäkseen uskottavaa kiistämismahdollisuutta niiden tulkintaan.

Idea ei ole suoraan piilottaa tietoa, vaan sekoittaa se muiden joukkoon. Tätä tavoitetta käytetään Coinjoineissa, transaktioissa, jotka katkaisevat kolikon historian Bitcoinissa ja tekevät sen jäljittämisen monimutkaiseksi. Tämän tuloksen saavuttamiseksi transaktiossa on luotava useita samanarvoisia sisääntuloja ja ulostuloja.

Sisääntulot ovat Bitcoin-transaktion sisääntuloja, ja ulostulot edustavat ulostuloja. Transaktio kuluttaa sisääntulonsa luodakseen uusia ulostuloja muuttamalla kolikon käyttöehtoja. Tämä mekanismi mahdollistaa bitcoinien siirtämisen käyttäjien välillä.
Käsittelen tätä yksityiskohtaisesti tässä artikkelissa: Bitcoin-transaktiomekanismi: UTXO, sisääntulot ja ulostulot.

Yksi tapa hämärtää jälkiä Bitcoin-transaktiossa on tehdä yhteistyössä tehtävä transaktio. Kuten nimi viittaa, se sisältää sopimuksen useiden käyttäjien välillä, joista jokainen tallettaa summan bitcoineja sisääntulona samassa transaktiossa ja saa summan ulostulona.

Kuten aiemmin mainittiin, tunnetuin yhteistyössä tehtävän transaktion rakenne on Coinjoin. Esimerkiksi Coinjoin Whirlpool -protokollassa transaktiot sisältävät 5 osallistujaa sisääntuloina ja ulostuloina, jokaisella sama määrä bitcoineja.

![Kaavio Coinjoin-transaktiosta Whirlpoolissa](assets/1.webp)

Tämän transaktion ulkopuolinen tarkkailija ei pysty tietämään, mikä ulostulo kuuluu millekin käyttäjälle sisääntulona. Jos otamme esimerkiksi käyttäjän #4 (violetti), voimme tunnistaa heidän sisääntulon UTXO:nsa, mutta emme tiedä, mikä viidestä ulostulosta on todellisuudessa heidän. Alkuperäinen tieto ei ole piilotettu, vaan pikemminkin sekoitettu ryhmän sisällä.
Käyttäjä pystyy kiistämään tietyn UTXO:n omistuksen ulostulona. Tätä ilmiötä kutsutaan "uskottavaksi kiistämismahdollisuudeksi", ja se mahdollistaa luottamuksellisuuden läpinäkyvässä Bitcoin-transaktiossa.

Lisätietoja Coinjoinista selitän KAIKEN tässä pitkässä artikkelissa: CoinJoinin ymmärtäminen ja käyttäminen Bitcoinissa.
Vaikka Coinjoin on erittäin tehokas UTXO:n jäljityksen katkaisemisessa, se ei sovellu suoraan maksamiseen. Sen rakenne edellyttää nimittäin tietyn määrän sisääntulojen ja saman arvon ulostulojen (kaivosmaksuja lukuun ottamatta) käyttöä. Bitcoinin käyttötransaktio on kuitenkin yksityisyyden kannalta kriittinen hetki, koska se usein luo fyysisen yhteyden käyttäjän ja heidän ketjutoimintansa välille. Näyttää siis olennaiselta käyttää yksityisyyden suojaamisen työkaluja maksamiseen. On olemassa muita yhteistyöllisiä transaktiorakenteita, jotka on suunniteltu nimenomaan todellisiin maksutransaktioihin.

## StonewallX2-transaktio

Samourai Walletin tarjoamien maksutyökalujen joukossa on yhteistyöllinen transaktio StonewallX2. Se on mini-Coinjoin kahden käyttäjän välillä, joka on suunniteltu maksamiseen. Ulkopuolelta katsottuna tämä transaktio voi johtaa useisiin mahdollisiin tulkintoihin. Se tarjoaa näin uskottavan kiistämisen mahdollisuuden ja siten, luottamuksellisuuden käyttäjälle.

Tämä StonewallX2 yhteistyöllinen transaktioasetus on saatavilla Samourai Walletissa ja Sparrow Walletissa. Tämä työkalu on yhteensopiva näiden kahden ohjelmiston välillä.

Sen mekanismi on melko yksinkertainen ymmärtää. Näin se toimii käytännössä:

> - Käyttäjä haluaa tehdä maksun bitcoineilla (esimerkiksi kauppiaalle).
> - He hakevat varsinaisen maksunsaajan (kauppiaan) vastaanotto-osoitteen.
> - He rakentavat erityisen transaktion, jossa on useita sisääntuloja: ainakin yksi kuuluu heille ja yksi ulkopuoliselle yhteistyökumppanille.
> - Transaktiossa on 4 ulostuloa, mukaan lukien 2 samaa määrää: yksi kauppiaan osoitteeseen maksua varten, yksi vaihtorahana, joka palautuu käyttäjälle, yksi samaa arvoa oleva ulostulo, joka menee yhteistyökumppanille, ja toinen ulostulo, joka myös palautuu yhteistyökumppanille.

Esimerkiksi, tässä on tyypillinen StonewallX2-transaktio, jossa tein maksun 50,125 satoshia. Ensimmäinen sisääntulo 102,588 satoshia tulee Samourai-lompakostani. Toinen sisääntulo 104,255 satoshia tulee yhteistyökumppanini lompakosta:

![StonewallX2 transaktion kaavio](assets/2.webp)

Voimme havaita 4 ulostuloa, mukaan lukien 2 samaa määrää hämärtämään jälkiä:

> - 50,125 satoshia, jotka menevät maksuni varsinaiselle vastaanottajalle.
> - 52,306 satoshia, jotka edustavat vaihtorahaani ja siis palautuvat osoitteeseen lompakossani.
> - 50,125 satoshia, jotka palautuvat yhteistyökumppanilleni.
> - 53,973 satoshia, jotka palautuvat yhteistyökumppanilleni.
>   Toimenpiteen lopussa yhteistyökumppanilla on alkuperäinen saldonsa palautettu (kaivosmaksuja lukuun ottamatta), ja käyttäjä on maksanut kauppiaalle. Tämä lisää merkittävän määrän entropiaa transaktioon ja katkaisee kiistattomat yhteydet maksun lähettäjän ja vastaanottajan välillä.

StonewallX2-transaktion vahvuus on, että se täysin kumoaa yhden ketjuanalyytikoiden käyttämistä empiirisistä säännöistä: monen sisääntulon transaktiossa sisääntulojen yhteisomistus. Toisin sanoen useimmissa tapauksissa, jos havaitsemme Bitcoin-transaktion, jossa on useita sisääntuloja, voimme olettaa, että kaikki nämä sisääntulot kuuluvat samalle henkilölle. Satoshi Nakamoto oli jo tunnistanut tämän ongelman käyttäjän yksityisyydelle hänen White Paperissaan:

> "Lisäsuojana voitaisiin käyttää uutta avainparia jokaisessa transaktiossa, jotta niitä ei voitaisi yhdistää yhteiseen omistajaan. Kuitenkin, yhteys on väistämätön monen sisääntulon transaktioissa, jotka välttämättä paljastavat, että niiden sisääntulot kuuluivat samalle omistajalle."

Tämä on yksi monista empiirisistä säännöistä, joita käytetään ketjuanalyysissä osoiteklustereiden rakentamiseen. Lisätietoja näistä heuristiikoista suosittelen lukemaan tämän neljän artikkelin sarjan Samourailta, joka esittelee aiheen ihailtavasti.
StonewallX2-tapahtuman vahvuus piilee siinä, että ulkopuolinen tarkkailija luulee tapahtuman eri syötteiden kuuluvan yhteiselle omistajalle. Todellisuudessa ne ovat kaksi eri käyttäjää, jotka tekevät yhteistyötä. Maksun analyysi johdetaan näin harhautukseen, ja käyttäjän yksityisyys säilyy.

Ulkopuolelta katsottuna StonewallX2-tapahtumaa ei voi erottaa Stonewall-tapahtumasta. Ainoa todellinen ero niiden välillä on, että Stonewall ei ole yhteistyöllinen. Se käyttää vain yhden käyttäjän UTXO:ja. Kuitenkin niiden rakenteet tilikirjassa ovat täysin identtiset. Tämä mahdollistaa vielä useampia tulkintoja tästä tapahtumarakenteesta, koska ulkopuolinen tarkkailija ei pysty sanomaan, tulevatko syötteet samalta henkilöltä vai kahdelta yhteistyökumppanilta.

Lisäksi StonewallX2:n etu Stowaway-tyyppiseen PayJoiniin verrattuna on, että sitä voidaan käyttää missä tahansa tilanteessa. Todellinen maksun vastaanottaja ei anna mitään syötteitä tapahtumaan. Näin ollen StonewallX2:ta voidaan käyttää maksamiseen missä tahansa kauppiaalla, joka hyväksyy Bitcoinin, vaikka kauppias ei käyttäisikään Samourai- tai Sparrow-sovellusta.
Toisaalta tämän tapahtumarakenteen päähaitta on, että se vaatii yhteistyökumppanin, joka on valmis käyttämään bitcoinejaan osallistuakseen maksuusi. Jos sinulla on bitcoin-ystäviä, jotka ovat valmiita auttamaan sinua missä tahansa tilanteessa, tämä ei ole ongelma. Jos et kuitenkaan tunne muita Samourai Walletin käyttäjiä, tai jos kukaan ei ole saatavilla yhteistyöhön, olet jumissa.

Tämän ongelman ratkaisemiseksi Samourai-tiimi lisäsi äskettäin uuden ominaisuuden sovellukseensa: JoinBot.

# Mikä on JoinBot?

JoinBotin periaate on yksinkertainen. Jos et löydä ketään, jonka kanssa tehdä yhteistyötä StonewallX2-tapahtumassa, voit tehdä yhteistyötä JoinBotin kanssa. Käytännössä teet itse asiassa yhteistyöllisen tapahtuman suoraan Samourai Walletin kanssa.

Tämä palvelu on erittäin kätevä, erityisesti aloittelijoille, koska se on saatavilla 24/7. Jos sinun tarvitsee tehdä kiireellinen maksu ja haluat tehdä StonewallX2:n, sinun ei enää tarvitse ottaa yhteyttä ystävään tai etsiä verkosta yhteistyökumppania. JoinBot auttaa sinua.

Toinen JoinBotin etu on, että se tarjoaa syötteinä käytettävät UTXO:t ovat yksinomaan postmix Whirlpoolista, mikä parantaa maksusi yksityisyyttä. Lisäksi, koska JoinBot on aina verkossa, sinun tulisi tehdä yhteistyötä UTXO:jen kanssa, joilla on suuret mahdolliset Anonsetit.

Ilmeisesti JoinBotissa on joitakin kompromisseja, jotka tulisi huomioida:

> Kuten klassisessa StonewallX2:ssa, yhteistyökumppanisi on välttämättä tietoinen käytetyistä UTXO:ista ja niiden määränpäästä. JoinBotin tapauksessa Samourai tietää tämän tapahtuman yksityiskohdat. Tämä ei välttämättä ole huono asia, mutta se tulisi pitää mielessä.
> Roskapostin välttämiseksi Samourai veloittaa 3,5% palvelumaksun todellisen tapahtuman määrästä, enimmäismäärän ollessa 0,01 BTC. Esimerkiksi, jos lähetän todellisen maksun 100 kilosatsia JoinBotin kanssa, palvelumaksun määrä on 3 500 satsia.
> JoinBotin käyttämiseksi sinulla on oltava lompakossasi vähintään kaksi toisiinsa liittymätöntä ja saatavilla olevaa UTXO:a.
> Klassisessa StonewallX2:ssa louhintamaksut jaetaan tasan kahden yhteistyökumppanin kesken. JoinBotin kanssa sinun on luonnollisesti maksettava koko louhintamaksu.
Jotta JoinBot-transaktio olisi täsmälleen sama kuin klassinen StonewallX2 tai Stonewall -transaktio, palvelumaksujen maksu suoritetaan täysin erillisellä transaktiolla. Samourain alun perin maksamien louhintamaksujen puolikkaan palautus tehdään tämän toisen transaktion aikana. Yksityisyytesi optimoimiseksi loppuun asti, maksujen selvittäminen suoritetaan käyttäen Stowaway (PayJoin) -rakenteista transaktiota.

## Kuinka käyttää JoinBotia?

JoinBot-transaktion suorittamiseksi sinulla täytyy olla Samourai Wallet. Voit ladata sen täältä tai Google Playstoresta.

Toisin kuin useimmat Samourain kehittämät työkalut, Sparrow Wallet ei ole vielä ilmoittanut JoinBotin käyttöönotosta. Tämä työkalu on siis saatavilla vain Samouraissa.

Opi askel askeleelta, kuinka suorittaa StonewallX2-transaktio JoinBotin avulla tässä videossa:

![Kuinka käyttää Joinbotia](https://youtu.be/80MoMz2Ne5g)

Tässä on transaktiokaavio, jonka juuri suoritimme videolla:

![Kaavio StonewallX2-transaktiostani JoinBotin kanssa.](assets/3.webp)

Voimme nähdä 5 syötettä:

> - 3 syötettä 100 kilosatsia Samouraista (JoinBot).
> - 2 syötettä henkilökohtaisesta lompakostani, 3,524 satsia ja 1.8 megasat.

Transaktion 4 lähtöä ovat seuraavat:

> - 1, 212,452 satsia todelliselle maksunsaajalle.
> - Toinen saman suuruinen määrä, joka palautuu Samourain osoitteeseen.
> - 1 vaihtoraha, joka myös palautuu Samouraille 87,302 satsia. Tämä edustaa eroa heidän syötteidensä kokonaismäärän (300,000 sats) ja hämärtävän lähdön (212,452 sats) välillä miinus louhintamaksut.
> - 1 vaihtoraha, joka palautuu toiseen osoitteeseen lompakossani. Se edustaa eroa syötteideni kokonaismäärän ja todellisen maksun välillä, miinus louhintamaksut.

Muistutuksena, louhintamaksut eivät edusta transaktion lähtöjä. Ne yksinkertaisesti edustavat eroa kokonaissyötteiden ja kokonaislähtöjen välillä.

## Yhteenveto

JoinBot on lisätyökalu, joka tarjoaa lisää valintoja ja vapautta Samourain käyttäjille. Se mahdollistaa yhteistyössä tehtävän StonewallX2-transaktion suoraan Samourain kanssa yhteistyökumppanina. Tämän tyyppinen transaktio auttaa parantamaan käyttäjän yksityisyyttä.

Jos voit suorittaa klassisen StonewallX2:n ystävän kanssa, suosittelen silti tämän työkalun käyttöä. Jos kuitenkin olet jumissa etkä löydä yhteistyökumppaneita maksun suorittamiseen, tiedät, että JoinBot on saatavilla 24/7 yhteistyöhön kanssasi.

**Ulkoiset resurssit:**
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin