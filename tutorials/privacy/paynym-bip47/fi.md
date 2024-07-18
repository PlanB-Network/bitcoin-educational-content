---
name: BIP47 - PayNym

description: Miten PayNymit toimivat
---
***VAROITUS:** Samourai Walletin perustajien pidätyksen ja heidän palvelimiensa takavarikoinnin jälkeen 24. huhtikuuta, sovellusta ei enää voi käyttää käyttäjät, joilla ei ole omaa Dojoa. BIP47 pysyy käytettävissä Sparrow Walletissa kaikille käyttäjille ja **Samourai Walletissa vain käyttäjille, joilla on Dojo**.*

_Seuraamme tiiviisti tämän tapauksen kehitystä sekä siihen liittyvien työkalujen kehitystä. Voitte olla varmoja, että päivitämme tämän oppaan uuden tiedon saataville tullessa._

_Tämä opas on tarkoitettu vain koulutus- ja tiedotustarkoituksiin. Emme tue tai kannusta näiden työkalujen käyttöä rikollisiin tarkoituksiin. Jokaisen käyttäjän on noudatettava oman lainkäyttöalueensa lakeja._

---

> "Hän on liian suuri," kaikki sanoivat, ja kalkkuna, joka oli syntynyt kannuksilla ja luuli olevansa keisari, paisui kuin laiva kaikki purjeet levitettyinä, ja marssi suoraan häntä kohti suuressa raivossa, silmät punaisina kuin tuli. Parka pieni ankka ei tiennyt, pitäisikö sen seistä paikallaan vai paeta, ja oli hyvin onneton, koska kaikki pihan ankat halveksivat sitä.

![BIP47, ruma ankanpoikanen -kuvitus](assets/1.webp)

Yksi merkittävimmistä ongelmista Bitcoin-protokollassa on osoitteen uudelleenkäyttö. Verkon läpinäkyvyys ja jakautuminen tekevät tästä käytännöstä vaarallisen käyttäjän yksityisyydelle. Ongelmien välttämiseksi suositellaan uuden tyhjän vastaanotto-osoitteen käyttöä jokaiselle uudelle saapuvalle maksulle lompakkoon, mikä voi olla joissakin tapauksissa hankalaa saavuttaa.

Tämä kompromissi on yhtä vanha kuin White Paper. Satoshi jo varoitti meitä tästä riskistä työssään, joka julkaistiin loppuvuodesta 2008:

> "Lisäpalomuurina tulisi käyttää uutta avainparia jokaiselle transaktiolle, jotta ne eivät liittyisi yhteiseen omistajaan."

Monia ratkaisuja on saatavilla useiden maksujen vastaanottamiseksi ilman osoitteen uudelleenkäyttöä. Jokaisella niistä on omat kompromissinsa ja haittansa. Kaikkien näiden ratkaisujen joukossa on [BIP47](https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki), ehdotus, jonka kehitti Justus Ranvier ja julkaisi vuonna 2015, joka mahdollistaa uudelleenkäytettävien maksukoodien luomisen. Sen tavoitteena on mahdollistaa useiden transaktioiden tekeminen samalle henkilölle ilman osoitteen uudelleenkäyttöä.

Alun perin tämä ehdotus kohtasi osan yhteisöstä halveksuntaa, eikä sitä koskaan lisätty Bitcoin Coreen. Kuitenkin jotkut ohjelmistot päättivät silti toteuttaa sen omatoimisesti. Esimerkiksi Samourai Wallet kehitti oman toteutuksensa BIP47:stä: PayNym. Tänään tämä toteutus on saatavilla Samourai Walletissa älypuhelimille sekä [Sparrow Walletissa](https://sparrowwallet.com/) PC:lle.

Ajan myötä Samourai on ohjelmoinut uusia ominaisuuksia, jotka liittyvät suoraan PayNymiin. Nyt on olemassa kokonainen työkalujen ekosysteemi, joka on saatavilla käyttäjän yksityisyyden optimoimiseksi PayNym- ja BIP47-perusteella.
Tässä artikkelissa tutustut BIP47:n ja PayNym:n periaatteisiin, näiden protokollien mekanismeihin ja niistä seuraaviin käytännön sovelluksiin. Käsittelen vain BIP47:n ensimmäistä versiota, jota tällä hetkellä käytetään PayNymille, mutta versiot 2, 3 ja 4 toimivat käytännössä samalla tavalla.
Ainoa merkittävä ero löytyy ilmoitustransaktiosta. Versio 1 käyttää yksinkertaista osoitetta OP_RETURN-komennon kanssa ilmoituksiin, versio 2 käyttää moniallekirjoitusskriptiä (bloom-multisig) OP_RETURN-komennon kanssa, ja versiot 3 ja 4 käyttävät suoraan moniallekirjoitusskriptiä (cfilter-multisig). Tässä artikkelissa käsitellyt mekanismit, mukaan lukien tutkitut kryptografiset menetelmät, ovat siis sovellettavissa kaikkiin neljään versioon. Tähän mennessä Samourai Walletin ja Sparrow'n PayNym-toteutus käyttää BIP47:n ensimmäistä versiota.

## Yhteenveto:

1- Osoitteen uudelleenkäytön ongelma.

2- BIP47:n ja PayNym:n periaatteet.

3- Oppaat: PayNym:n käyttö.

- BIP47-transaktion rakentaminen Samourai Walletilla.
- BIP47-transaktion rakentaminen Sparrow Walletilla.

4- BIP47:n toimintaperiaate.

- Uudelleenkäytettävä maksukoodi.
- Kryptografinen menetelmä: Diffie-Hellmanin avainvaihto perustuu elliptisiin käyriin (ECDH).
- Ilmoitustransaktio.
- Ilmoitustransaktion rakentaminen.
- Ilmoitustransaktion vastaanottaminen.
- BIP47-maksutransaktio.
- BIP47-maksun vastaanottaminen ja yksityisen avaimen johdannainen.
- BIP47-maksun palauttaminen.

5- PayNym:n johdannaiset käyttötarkoitukset.

6- Henkilökohtainen mielipiteeni BIP47:stä.

## Osoitteen uudelleenkäytön ongelma.

Vastaanotto-osoitetta käytetään bitcoinien vastaanottamiseen. Se luodaan julkisesta avaimesta hashaamalla se ja soveltamalla tiettyä formaattia. Näin ollen se mahdollistaa uuden kulutusehdon luomisen kolikolle sen omistajan vaihtamiseksi.

> Jos haluat oppia lisää vastaanotto-osoitteen luomisesta, suosittelen lukemaan tämän artikkelin viimeisen osan: Bitcoin-lompakko - ote [ebook Bitcoin Démocratisé 2](https://www.pandul.fr/post/le-portefeuille-bitcoin-extrait-ebook-bitcoin-d%C3%A9mocratis%C3%A9-2#viewer-epio7).

Lisäksi olet todennäköisesti jo kuullut tietävältä bitcoin-käyttäjältä, että vastaanotto-osoitteita tulisi käyttää vain kerran, ja että sinun tulisi luoda uusi osoite jokaiselle uudelle saapuvalle maksulle lompakkoosi. Mutta miksi?
Perustavanlaatuisesti osoitteen uudelleenkäyttö ei suoraan vaaranna varojasi. Elliptisten käyrien kryptografian käyttö mahdollistaa sen, että voit todistaa verkostolle yksityisen avaimen hallinnan paljastamatta kyseistä avainta. Näin ollen voit lukita useita eri UTXOja (Käyttämättömät Transaktiotulosteet) samalle osoitteelle ja kuluttaa ne eri aikoina. Jos et paljasta kyseisen osoitteen yksityistä avainta, kukaan ei pääse käsiksi varoihisi. Osoitteen uudelleenkäytön ongelma liittyy enemmän yksityisyyteen.

Kuten johdannossa mainittiin, Bitcoin-verkon läpinäkyvyys ja jakelu tarkoittavat, että mikä tahansa solmua käyttävä käyttäjä voi tarkkailla maksujärjestelmän transaktioita. Tämän seurauksena he voivat nähdä eri osoitteiden saldot. Satoshi Nakamoto mainitsi sitten mahdollisuuden luoda uusia avainpareja, ja siten uusia osoitteita, jokaiselle uudelle saapuvalle maksulle lompakkoon. Tavoitteena olisi olla lisäpalomuuri tapauksessa, jossa käyttäjän henkilöllisyys yhdistetään johonkin heidän avainpareistaan.

Nykyään, kun ketjuanalyysiyhtiöt ovat läsnä ja KYC (Know Your Customer) kehittyy, tyhjien osoitteiden käyttö ei ole enää lisäpalomuuri, vaan velvollisuus kenelle tahansa, joka välittää edes hieman yksityisyydestään.

Yksityisyyden tavoittelu ei ole mukavuutta tai maksimalististen Bitcoin-käyttäjien fantasiaa. Se on tietty parametri, joka vaikuttaa suoraan henkilökohtaiseen turvallisuuteesi ja varojesi turvallisuuteen. Auttaaksesi ymmärtämään tätä, tässä on hyvin konkreettinen esimerkki:
- Bob ostaa Bitcoinia Dollar Cost Averaging (DCA) -menetelmällä, mikä tarkoittaa, että hän hankkii pienen määrän Bitcoinia säännöllisin väliajoin keskihintaansa tasatakseen. Bob lähettää systemaattisesti ostetut varat samaan vastaanotto-osoitteeseen. Hän ostaa 0,01 Bitcoinia joka viikko ja lähettää sen tähän samaan osoitteeseen. Kahden vuoden jälkeen Bob on kerryttänyt kokonaisen Bitcoinin tähän osoitteeseen.
- Kulman leipuri hyväksyy Bitcoin-maksut. Innostuneena mahdollisuudesta käyttää Bitcoinia, Bob menee ostamaan patonkinsa satosheina. Maksuun hän käyttää osoitteeseensa lukittuja varoja. Hänen leipurinsa nyt tietää, että hänellä on Bitcoin. Tämä merkittävä summa voisi herättää kateutta, ja Bob saattaa tulevaisuudessa olla fyysisen hyökkäyksen riskissä.

Osoitteen uudelleenkäyttö mahdollistaa tarkkailijan tehdä kiistattoman yhteyden eri UTXO:idesi välillä ja joskus myös henkilöllisyytesi ja koko lompakkosi välillä.
Tämän vuoksi suurin osa Bitcoin-lompakko-ohjelmistoista luo automaattisesti uuden vastaanotto-osoitteen, kun klikkaat "Vastaanota" -painiketta. Tavallisille käyttäjille uusien osoitteiden käyttöön tottuminen ei ole suuri haitta. Kuitenkin verkkoliiketoiminnalle, pörssille tai lahjoituskampanjalle tämä rajoitus voi nopeasti muodostua hallitsemattomaksi.
Näille organisaatioille on monia ratkaisuja. Jokaisella niistä on etunsa ja haittansa, mutta tähän mennessä, ja kuten myöhemmin näemme, BIP47 todella erottuu muista.

Tämä osoitteen uudelleenkäytön ongelma ei ole vähäpätöinen Bitcoinissa. Kuten alla olevasta oxt.me -sivuston kaaviosta näet, Bitcoin-käyttäjien kokonaisosoitteen uudelleenkäyttöaste on tällä hetkellä 52%:
Kaavio OXT.me:stä näyttää Bitcoin-verkon kokonaisosoitteen uudelleenkäyttöasteen kehityksen.

![kuva](assets/2.webp)

Luotto: OXT

Suurin osa näistä uudelleenkäytöistä tulee pörsseistä, jotka tehokkuuden ja mukavuuden vuoksi käyttävät samaa osoitetta monta kertaa. Tähän mennessä BIP47 olisi paras ratkaisu tämän ilmiön hillitsemiseksi pörsseissä. Tämä auttaisi vähentämään kokonaisosoitteen uudelleenkäyttöastetta aiheuttamatta liikaa hankaluuksia näille tahoille.

Tämä koko verkon kattava toimenpide on erityisen merkittävä tässä tapauksessa. Todellakin, osoitteen uudelleenkäyttö ei ole ongelma vain henkilölle, joka harjoittaa tätä käytäntöä, vaan myös kenelle tahansa, joka tekee transaktioita heidän kanssaan. Yksityisyyden menetys Bitcoinissa toimii kuin virus, leviäen käyttäjästä käyttäjään. Koko verkoston transaktioiden globaalin mittauksen tutkiminen mahdollistaa tämän ilmiön laajuuden ymmärtämisen.

## BIP47:n ja PayNym:n periaatteet.

BIP47 pyrkii tarjoamaan yksinkertaisen tavan vastaanottaa useita maksuja ilman osoitteen uudelleenkäyttöä. Sen toiminta perustuu uudelleenkäytettävän maksukoodin käyttöön.

Näin ollen useat lähettäjät voivat lähettää useita maksuja yhdelle uudelleenkäytettävälle maksukoodille toiselle käyttäjälle, ilman että vastaanottajan tarvitsee tarjota uutta tyhjää osoitetta jokaiselle uudelle transaktiolle.

Käyttäjä voi vapaasti jakaa maksukoodinsa (sosiaalisissa verkostoissa, verkkosivuillaan...) ilman yksityisyyden menetyksen riskiä, toisin kuin tavallisen vastaanotto-osoitteen tai julkisen avaimen kanssa.
Vaihdon suorittamiseksi molemmilla käyttäjillä on oltava Bitcoin-lompakko, jossa on BIP47-toteutus, kuten PayNym Samourai Walletissa tai Sparrow Walletissa. Käyttäjien maksukoodien yhdistäminen luo salaisen kanavan heidän välilleen. Tämän kanavan asianmukaiseksi perustamiseksi lähettäjän on tehtävä transaktio Bitcoin-lohkoketjussa: ilmoitustransaktio (selitän tästä lisää myöhemmin).

Käyttäjien maksukoodien yhdistäminen tuottaa jaettuja salaisuuksia, jotka puolestaan tuottavat suuren määrän ainutlaatuisia Bitcoin-vastaanotto-osoitteita (tarkalleen 2^32). Näin ollen todellisuudessa BIP47-maksu ei lähetetä maksukoodiin, vaan täysin normaaleihin osoitteisiin, jotka on johdettu osapuolten maksukoodeista.
Maksukoodi toimii virtuaalisena tunnisteena, joka on johdettu lompakon siemenestä. HD-lompakon johdannaisrakenteessa maksukoodi sijaitsee syvyydessä 3, lompakon tilin tasolla.
![image](assets/3.webp)

Sen johdannaisen tarkoitus on merkitty numerolla 47' (0x8000002F) viitaten BIP47:ään. Esimerkiksi uudelleenkäytettävän maksukoodin johdannaispolku olisi:

> m/47'/0'/0'/

Jotta saat käsityksen siitä, miltä maksukoodi näyttää, tässä on omani:

> PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5

Sitä voidaan myös koodata QR-koodiksi helpottamaan viestintää:

![image](assets/4.webp)

PayNym Boteista, noista Twitterissä näkyvistä roboteista, ne ovat yksinkertaisesti visuaalisia esityksiä maksukoodistasi, jotka on luonut Samourai Wallet. Ne luodaan käyttäen hajautusfunktiota, mikä tekee niistä lähes uniikkeja. Tässä on omani tunnuksellaan:

> +throbbingpond8B1

![image](assets/5.webp)

Näillä Boteilla ei ole mitään todellista teknistä hyötyä. Sen sijaan ne helpottavat käyttäjien välisiä vuorovaikutuksia luomalla virtuaalisen visuaalisen identiteetin.

Käyttäjälle BIP47-maksun tekeminen PayNym-toteutuksella on erittäin yksinkertaista. Kuvitellaan, että Alice haluaa lähettää maksuja Bobille:

1. Bob jakaa QR-koodinsa tai suoraan uudelleenkäytettävän maksukoodinsa. Hän voi sijoittaa sen verkkosivustolleen, eri julkisiin sosiaalisen median kanaviinsa tai lähettää sen Alicelle toisen viestintäkeinon kautta.
2. Alice avaa Samourai- tai Sparrow-ohjelmistonsa ja skannaa tai liittää Bobin maksukoodin.
3. Alice yhdistää PayNyminsä Bobin kanssa ("Follow" englanniksi). Tämä toimenpide tehdään off-chain ja on täysin ilmainen.

4. Alice yhdistää PayNyminsä Bobin kanssa ("Connect" englanniksi). Tämä toimenpide tehdään "on-chain". Alicen on maksettava transaktion louhintamaksut sekä kiinteä maksu 15 000 satsia palvelusta Samourailla. Palvelumaksut ovat ilmaisia Sparrow'ssa. Tätä vaihetta kutsutaan ilmoitustransaktioksi.

5. Kun ilmoitustransaktio on vahvistettu, Alice voi luoda BIP47-maksutransaktion Bobille. Hänen lompakkonsa luo automaattisesti uuden tyhjän vastaanotto-osoitteen, jolle vain Bobilla on yksityisavain.

Ilmoitustransaktion suorittaminen, eli PayNyminsä yhdistäminen, on pakollinen edellytys BIP47-maksujen tekemiselle. Kuitenkin, kun tämä on tehty, lähettäjä voi tehdä useita maksuja vastaanottajalle (tarkalleen 2^32) tarvitsematta suorittaa uutta ilmoitustransaktiota.

Olet ehkä huomannut, että PayNymien yhdistämisessä on kaksi eri toimenpidettä: "follow" ja "connect". Yhdistämistoimenpide ("connect") vastaa BIP47-ilmoitustransaktiota, joka on yksinkertaisesti Bitcoin-transaktio, jossa tiettyjä tietoja välitetään OP_RETURN-lähdön kautta. Näin se auttaa perustamaan salatun viestinnän kahden käyttäjän välille tuottaakseen jaetut salaisuudet, jotka ovat tarpeen uusien tyhjien vastaanotto-osoitteiden luomiseksi.

Toisaalta, linkitystoimenpide ("follow" tai "relier") mahdollistaa linkin Sorobanissa, salatussa viestintäprotokollassa, joka perustuu Toriin ja on erityisesti kehitetty Samourai-tiimeissä.
- Kahden PayNym-yhteyden muodostaminen ("seuraaminen") on täysin ilmaista. Se auttaa luomaan off-chain salattuja viestintäyhteyksiä, erityisesti Samourain yhteistyössä toteutettavien transaktiotyökalujen (Stowaway tai StonewallX2) käyttöön. Tämä toiminto on erityinen PayNymille eikä sitä kuvata BIP47:ssä.
- Kahden PayNym-yhteyden muodostaminen aiheuttaa kustannuksia. Tämä sisältää ilmoitustransaktion suorittamisen yhteyden aloittamiseksi. Kustannukset koostuvat mahdollisista palvelumaksuista, transaktion louhintamaksuista ja 546 satoshin lähettämisestä vastaanottajan ilmoitusosoitteeseen ilmoittaakseen tunnelin avautumisesta. Tämä toiminto liittyy BIP47:ään. Kun se on suoritettu, lähettäjä voi tehdä useita BIP47-maksuja vastaanottajalle.

Jotta kaksi PayNymia voidaan yhdistää, niiden on oltava jo linkitettyjä.

## Oppaat: PayNym käyttö.

Nyt kun olemme nähneet teorian, tutkitaan käytäntöä yhdessä. Alla olevien oppaiden idea on linkittää PayNymini Sparrow-lompakossani PayNymiini Samourai-lompakossani. Ensimmäinen opas näyttää, miten tehdä transaktio käyttäen uudelleenkäytettävää maksukoodia Samouraista Sparrow'hun, ja toinen opas kuvailee samaa mekanismia Sparrow'sta Samouraihin.

> Suoritin nämä oppaat Testnetissä. Nämä eivät ole oikeita bitcoineja.

### BIP47-transaktion rakentaminen Samourai Walletilla.

Aloittaaksesi tarvitset selvästi Samourai Wallet -sovelluksen. Voit ladata sen suoraan Google Play Kaupasta tai APK-tiedoston kautta viralliselta Samourai-sivustolta.

Kun lompakko on alustettu, jos et ole vielä tehnyt niin, pyydä PayNymiasi napsauttamalla plus (+) -kuvaketta oikeassa alakulmassa, sitten "PayNym".

Ensimmäinen askel BIP47-maksun tekemiseksi on hankkia uudelleenkäytettävä maksukoodi vastaanottajaltamme. Sen jälkeen voimme muodostaa yhteyden heihin ja siten linkittää:

![video](assets/6.mp4)

Kun ilmoitustransaktio on vahvistettu, voin lähettää useita maksuja vastaanottajalleni. Jokainen transaktio tehdään automaattisesti uudella tyhjällä osoitteella, jonka avaimet vastaanottajalla on. Vastaanottajan ei tarvitse tehdä mitään, kaikki lasketaan puoleltani.

Näin teet BIP47-transaktion Samourai Walletilla:

![video](assets/7.mp4)

### BIP47-transaktion rakentaminen Sparrow Walletilla.

Kuten Samourain kanssa, sinun täytyy selvästi olla Sparrow-ohjelmisto. Se on saatavilla tietokoneellesi. Voit ladata sen heidän [viralliselta verkkosivustoltaan](https://sparrowwallet.com/).

Varmista, että tarkistat kehittäjän allekirjoituksen ja ladatun ohjelmiston eheyden ennen sen asentamista koneellesi.

Luo lompakko ja pyydä PayNymiasi napsauttamalla "Näytä PayNym" "Työkalu"-valikosta yläpalkissa:

![image](assets/8.webp)

Sen jälkeen sinun täytyy linkittää ja yhdistää PayNymisi vastaanottajan PayNymiin. Tee tämä syöttämällä heidän uudelleenkäytettävä maksukoodinsa "Etsi kontakti" -ikkunaan, seuraa heitä ja suorita sitten ilmoitustransaktio napsauttamalla "Linkitä kontakti":

![image](assets/9.webp)

Kun ilmoitustransaktio on vahvistettu, voit lähettää maksuja uudelleenkäytettävään maksukoodiin. Näin se tehdään:

![video](assets/10.mp4)

Nyt kun olemme voineet tutkia käytännön näkökulmasta PayNym-implementointia BIP47:ssä, katsotaan, miten kaikki nämä mekanismit toimivat ja mitä kryptografisia menetelmiä käytetään.
BIP47:n mekanismien tutkimiseksi on olennaista ymmärtää hierarkkisen deterministisen (HD) lompakon rakenne, lasten avainparien johdannaiset mekanismit sekä elliptisen käyrän kryptografian periaatteet. Onneksi voit löytää kaiken tarvittavan tiedon tämän osan ymmärtämiseksi blogistani:
- [Bitcoin-lompakon johdannaispolkujen ymmärtäminen](https://www.pandul.fr/post/comprendre-les-chemins-de-d%C3%A9rivation-d-un-portefeuille-bitcoin)

- [Bitcoin-lompakko - ote e-kirjasta Bitcoin Democratized 2](https://www.pandul.fr/post/le-portefeuille-bitcoin-extrait-ebook-bitcoin-d%C3%A9mocratis%C3%A9-2)

### Uudelleenkäytettävä maksukoodi.

Kuten tämän paperin toisessa osassa selitetään, uudelleenkäytettävä maksukoodi sijaitsee HD-lompakon kolmannella tasolla. Se on jossain määrin verrattavissa xpubiin, sekä sijoittelunsa että rakenteensa, sekä roolinsa puolesta.

Tässä ovat eri osat, jotka muodostavat 80-tavuisen maksukoodin:

- Tavu 0: Versio. Jos käytetään BIP47:n ensimmäistä versiota, tämä tavu on yhtä kuin 0x01.

- Tavu 1: Bittikenttä. Tämä tila on varattu lisäohjeiden antamiseen erityiskäytön tapauksessa. Jos käytetään yksinkertaisesti PayNymia, tämä tavu on yhtä kuin 0x00.

- Tavu 2: Y-pariteetti. Tämä tavu ilmaisee 0x02 tai 0x03 riippuen julkisen avaimemme y-koordinaatin arvon pariteetista (parillinen tai pariton luku). Lisätietoja tästä käytännöstä löytyy tämän artikkelin "osoitteen johdannais" -osion vaiheesta 1.

- Tavusta 3 tavuun 34: X-arvo. Nämä tavut ilmaisevat julkisen avaimemme x-koordinaatin. X:n ja y-pariteetin yhdistäminen antaa meille tiivistetyn julkisen avaimemme.

- Tavusta 35 tavuun 66: Ketjukoodi. Tämä tila on varattu edellä mainitun julkisen avaimen yhteydessä olevaan ketjukoodiin.

- Tavusta 67 tavuun 79: Täyttö. Tämä tila on varattu mahdollisia tulevia kehityksiä varten. Versiolle 1 täytämme sen yksinkertaisesti nollilla saavuttaaksemme 80 tavua, mikä on OP_RETURN-tulosteen datan koko.

Tässä on heksadesimaalinen esitys uudelleenkäytettävästä maksukoodistani, joka esitettiin edellisessä osiossa, väreillä vastaten yllä esitettyjä tavuja:
Seuraavaksi sinun on myös lisättävä etuliite tavu "P" tunnistaaksesi nopeasti, että käsittelemme maksukoodia. Tämä tavu on 0x47.

> 0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000

Lopuksi laskemme tämän maksukoodin tarkistussumman käyttämällä HASH256:ta, mikä tarkoittaa kaksinkertaista hajautusta SHA256-toiminnolla. Otamme tästä tiivisteestä ensimmäiset neljä tavua ja liitämme ne loppuun (vaaleanpunaisella).
Maksukoodi on valmis, nyt meidän tarvitsee vain muuntaa se Base 58 -muotoon:

> PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5

Kuten näet, tämä rakenne muistuttaa läheisesti laajennetun julkisen avaimen "xpub" rakennetta.

Tämän maksukoodin saamiseksi prosessissa käytimme tiivistettyä julkista avainta ja ketjukoodia. Nämä kaksi elementtiä ovat deterministisen ja hierarkisen johdannon tulosta lompakon siemenestä, seuraten seuraavaa johdannon polkua: m/47'/0'/0'/
Konkreettisesti, saadaksemme julkisen avaimen ja ketjukoodin uudelleenkäytettävälle maksukoodille, laskemme ensin pääyksityisavaimen siemenestä, sitten johdamme lapsiparin indeksillä 47 + 2^31 (kovennettu johdanto). Sen jälkeen johdamme kaksi lisää lapsiparia indeksillä 2^31 (kovennettu johdanto).

> Jos haluat oppia lisää lapsiavainparien johdannosta hierarkisessa deterministisessä Bitcoin-lompakossa, suosittelen tutustumaan CRYPTO301-kurssiin.

### Kryptografinen menetelmä: Elliptinen käyrä Diffie-Hellman avainvaihto (ECDH).

Kryptografinen menetelmä, jota käytetään BIP47:n ytimessä, on ECDH (Elliptic-Curve Diffie-Hellman). Tämä protokolla on klassisen Diffie-Hellman avainvaihdon variantti.

Diffie-Hellman, sen ensimmäisessä versiossa, on avainsopimusprotokolla, joka esiteltiin vuonna 1976 ja mahdollistaa kahden osapuolen, joilla kummallakin on julkinen ja yksityinen avainpari, määrittää jaetun salaisuuden vaihtamalla tietoja turvattoman viestintäkanavan yli.

![kuva](assets/11.webp)

Tämä jaettu salaisuus (punainen avain) voidaan sitten käyttää muihin tehtäviin. Tyypillisesti tätä jaettua salaisuutta voidaan käyttää viestinnän salaamiseen ja purkamiseen turvattoman verkon yli:

![kuva](assets/12.webp)

Tämän vaihdon saavuttamiseksi Diffie-Hellman käyttää modulaarista aritmetiikkaa jaetun salaisuuden laskemiseen. Tässä on yksinkertaistettu selitys siitä, miten se toimii:

- Alice ja Bob sopivat yhteisestä väristä, tässä tapauksessa keltaisesta. Tämä väri on kaikkien tiedossa. Se on julkista tietoa.

- Alice valitsee salaisen värin, tässä tapauksessa punaisen. Hän sekoittaa kaksi väriä, tuloksena on oranssi.

- Bob valitsee salaisen värin, tässä tapauksessa turkoosinsinisen. Hän sekoittaa kaksi väriä, tuloksena on taivaansininen.

- Alice ja Bob voivat vaihtaa saamansa värit: oranssin ja taivaansinisen. Tämä vaihto voi tapahtua turvattoman verkon yli ja sitä voivat tarkkailla hyökkääjät.

- Alice sekoittaa Bobilta saamansa taivaansinisen värin omaan salaiseen väriinsä (punainen). Hän saa ruskean.

- Bob sekoittaa Alicelta saamansa oranssin värin omaan salaiseen väriinsä (turkoosi). Hän saa myös ruskean.

![kuva](assets/13.webp)
> Lähde: Alkuperäinen idea: A.J. Han Vinck
Vektoriversio: Flugaal
Käännös: Dereckson, Public domain, Wikimedia Commonsin kautta. https://commons.wikimedia.org/wiki/File:Diffie-Hellman_Key_Exchange_(fr).svg
Tässä yksinkertaistuksessa ruskea väri edustaa salaisuutta, joka on jaettu Alicen ja Bobin kesken. Todellisuudessa on mahdotonta, että hyökkääjä voisi erottaa oranssin ja taivaansinisen värin saadakseen selville Alicen tai Bobin salaiset värit.

Tutkitaan nyt sen todellista toimintaa. Ensivilkaisulla Diffie-Hellman saattaa vaikuttaa monimutkaiselta ymmärtää. Todellisuudessa sen toimintaperiaate on melkein lapsellisen yksinkertainen. Ennen sen mekanismien yksityiskohtien läpikäyntiä, muistutan nopeasti kahta matemaattista käsitettä, joita tarvitsemme (ja joita sattumoisin käytetään monissa muissakin kryptografisissa menetelmissä).

1. Alkuluku on luonnollinen luku, jolla on vain kaksi jakajaa: 1 ja itse luku. Esimerkiksi luku 7 on alkuluku, koska sen voi jakaa vain luvuilla 1 ja 7 (itse). Toisaalta luku 8 ei ole alkuluku, koska sen voi jakaa luvuilla 1, 2, 4 ja 8. Sillä on siis ei ainoastaan kaksi jakajaa, vaan neljä kokonaislukua ja positiivista jakajaa.

2. "Modulo" (merkitään "mod" tai "%") on matemaattinen toimitus, joka antaa kahden kokonaisluvun jakojäännöksen Eukleideen jaon ensimmäisestä luvusta toisella luvulla. Esimerkiksi 16 mod 5 on yhtä kuin 1.

Diffie-Hellmanin avainvaihto Alicen ja Bobin välillä toimii seuraavasti:

- Alice ja Bob määrittävät kaksi yhteistä lukua: p ja g. p on alkuluku. Mitä suurempi tämä luku p on, sitä turvallisempi Diffie-Hellman on. g on p:n primitiivijuuri. Nämä kaksi lukua voidaan kommunikoida avoimesti epävarman verkon yli, ne ovat vastineita yllä olevassa yksinkertaistuksessa olevaan keltaiseen väriin. Alicen ja Bobin tarvitsee vain varmistaa, että p:n ja g:n arvot ovat täsmälleen samat.

- Kun parametrit on valittu, Alice ja Bob määrittävät kumpikin oman salaisen satunnaisluvun. Alicen saama satunnaisluku nimetään a:ksi (vastaa punaista väriä) ja Bobin saama satunnaisluku nimetään b:ksi (vastaa turkoosia väriä). Nämä kaksi lukua on pidettävä salassa.

- Sen sijaan, että vaihtaisivat nämä luvut a ja b, kumpikin osapuoli laskee A:n (isolla kirjaimella) ja B:n (isolla kirjaimella) siten, että:

> A on yhtä kuin g korotettuna a:n potenssiin modulo p:
> A = g^a % p

> B on yhtä kuin g korotettuna b:n potenssiin modulo p:
> B = g^b % p

- Nämä luvut A (vastaa oranssia väriä) ja B (vastaa taivaansinistä väriä) vaihdetaan kahden osapuolen välillä. Vaihto voidaan tehdä avoimesti epävarman verkon yli.

- Alice, joka nyt tietää B:n, laskee arvon z siten, että:

> z on yhtä kuin B korotettuna a:n potenssiin modulo p:
> z = B^a % p

- Muistutuksena, B = g^b % p. Siksi:

  > z = B^a % p
  > z = (g^b)^a % p
  >
  > Eksponenttisääntöjen mukaan:
  >
  > (x^n)^m = x^nm
  >
  > Siksi:
  >
  > z = g^ba % p

- Bob, joka nyt tietää A:n, laskee myös arvon z seuraavasti:
> z on yhtä suuri kuin A korotettuna b:n potenssiin modulo p:
>
> z = A^b % p
>
> Siksi:
>
> z = (g^a)^b % p
> z = g^ab % p
> z = g^ba % p

Modulo-operaattorin jakautuvuuden ansiosta Alice ja Bob löytävät täsmälleen saman arvon z:lle. Tämä luku edustaa heidän jaettua salaisuuttaan, joka vastaa edellisessä selityksessä mainittua ruskeaa väriä. He voivat käyttää tätä jaettua salaisuutta salatakseen kommunikaation keskenään turvattomassa verkossa.

![Diffie-Hellmanin tekninen toimintakaavio](assets/14.webp)

Hyökkääjä, joka hallussaan p, g, A ja B, ei pysty laskemaan a, b tai z. Tämän operaation suorittaminen vaatisi eksponentiaation kääntämistä, mikä on mahdotonta tehdä muuten kuin kokeilemalla kaikkia mahdollisuuksia yksi kerrallaan, koska työskentelemme äärellisessä kentässä. Tämä olisi vastaavaa kuin diskreetin logaritmin laskeminen, joka on eksponentiaation käänteisoperaatio syklisessä äärellisessä ryhmässä.

Siksi, kunhan valitsemme riittävän suuret arvot a:lle, b:lle ja p:lle, Diffie-Hellman on turvallinen. Tyypillisesti 2,048 bitin parametreilla (numero, jossa on 600 numeroa desimaalimuodossa), kaikkien mahdollisuuksien testaaminen a:lle ja b:lle olisi epäkäytännöllistä. Tähän mennessä näin suurilla numeroilla algoritmi katsotaan turvalliseksi.

Tässä on juuri Diffie-Hellman-protokollan pääasiallinen haittapuoli. Ollakseen turvallinen, algoritmin on käytettävä suuria numeroita. Tämän seurauksena ECDH-algoritmi on nyt suositumpi, joka on Diffie-Hellmanin variantti, joka käyttää algebrallista käyrää, erityisesti elliptistä käyrää. Tämä mahdollistaa paljon pienempien numeroiden käytön säilyttäen samalla vastaavan turvallisuuden, vähentäen näin laskenta- ja tallennusresurssien tarvetta.

Algoritmin yleinen periaate pysyy samana. Kuitenkin, sen sijaan, että käyttäisimme satunnaista numeroa a ja numeroa A, joka on laskettu a:sta käyttäen modulaarista eksponentiaatiota, käytämme avainparia, joka on perustettu elliptiselle käyrälle. Modulo-operaattorin jakautuvuuden sijaan käytämme ryhmälakia elliptisillä käyrillä, erityisesti tämän lain assosiatiivisuutta.
Jos sinulla ei ole tietoa siitä, miten yksityiset ja julkiset avaimet toimivat elliptisellä käyrällä, selitän tämän menetelmän perusteet tämän artikkelin ensimmäisessä kuudessa osassa.

Yksinkertaistaen, yksityinen avain on satunnainen luku välillä 1 ja n-1 (missä n on käyrän järjestys), ja julkinen avain on yksilöllinen piste käyrällä, joka määräytyy yksityisen avaimen kautta pisteiden lisäyksen ja kaksinkertaistamisen avulla lähtöpisteestä, seuraavasti:

> K = k·G

Missä K on julkinen avain, k on yksityinen avain, ja G on lähtöpiste.

Yksi tämän avainparin ominaisuuksista on, että K:n määrittäminen on erittäin helppoa, jos tiedät k:n ja G:n, mutta k:n määrittäminen on tällä hetkellä mahdotonta, jos tiedät K:n ja G:n. Se on yksisuuntainen funktio.

Toisin sanoen, voit helposti laskea julkisen avaimen, jos tiedät yksityisen avaimen, mutta on mahdotonta laskea yksityistä avainta, jos tiedät julkisen avaimen. Tämä turvallisuus perustuu jälleen kerran diskreetin logaritmin laskemisen mahdottomuuteen.

Käytämme tätä ominaisuutta mukauttaaksemme Diffie-Hellman-algoritmimme. Näin ollen ECDH:n toimintaperiaate on seuraava:

- Alice ja Bob sopivat kryptografisesti turvallisesta elliptisestä käyrästä ja sen parametreista. Tämä tieto on julkinen.
- Alice luo satunnaisen numeron ka, joka on hänen yksityinen avaimensa. Tämän yksityisen avaimen on pysyttävä salassa. Hän määrittää julkisen avaimensa Ka lisäämällä ja kaksinkertaistamalla pisteitä valitulla elliptisellä käyrällä.
> Ka = ka·G

- Bob luo myös satunnaisen numeron kb, joka on hänen yksityinen avaimensa. Hän laskee siihen liittyvän julkisen avaimen Kb.

> Kb = kb·G

- Alice ja Bob vaihtavat julkiset avaimensa Ka ja Kb epävarman julkisen verkon yli.

- Alice laskee pisteen (x, y) käyrällä soveltamalla yksityistä avaintaan ka Bobin julkiseen avaimen Kb.

> (x, y) = ka·Kb

- Bob laskee pisteen (x, y) käyrällä soveltamalla omaa yksityistä avaintaan kb Alicen julkiseen avaimen Ka.

> (x, y) = kb·Ka

- Alice ja Bob saavat saman pisteen elliptisellä käyrällä. Jaettu salaisuus on tämän pisteen x-koordinaatti.

He saavat saman jaetun salaisuuden, koska:

> (x, y) = ka·Kb = ka·kb·G = kb·ka·G = kb·Ka

Mahdollinen hyökkääjä, joka tarkkailee epävarmaa julkista verkkoa, voi saada vain osapuolten julkiset avaimet ja valitut käyrän parametrit. Kuten aiemmin selitettiin, nämä kaksi tietoa yksinään eivät mahdollista yksityisten avainten määrittämistä, joten hyökkääjä ei pääse käsiksi salaisuuteen.
ECDH on algoritmi, joka mahdollistaa avainten vaihdon. Sitä käytetään usein muiden kryptografisten menetelmien rinnalla protokollan määrittämiseen. Esimerkiksi ECDH on käytössä TLS:n (Transport Layer Security) ytimessä, joka on internetin siirtokerroksen salaus- ja autentikointiprotokolla. TLS käyttää avaintenvaihtoon ECDHE:ta, ECDH:n varianttia, jossa avaimet ovat kertakäyttöisiä tarjoten pysyvää luottamuksellisuutta. ECDHE:n lisäksi TLS käyttää autentikointialgoritmia kuten ECDSA, salausalgoritmia kuten AES ja hajautusfunktiota kuten SHA256.

TLS määrittelee "s":n "https":ssä ja pienen lukon kuvakkeen, jonka näet internet-selaimessasi vasemmassa yläkulmassa, mikä takaa salatun viestinnän. Joten käytät tällä hetkellä ECDH:ta lukiessasi tätä artikkelia, ja todennäköisesti käytät sitä päivittäin tietämättäsi.

### Ilmoitustransaktio.

Kuten edellisessä osiossa havaitsimme, ECDH on Diffie-Hellmanin vaihdon variantti, joka sisältää elliptiselle käyrälle perustuvia avainpareja. Onneksi meillä on runsaasti tällaisia avainpareja Bitcoin-lompakoissamme!

Ajatuksena on käyttää molempien osapuolten hierarkkisista deterministisista Bitcoin-lompakoista peräisin olevia avainpareja jaettujen ja kertakäyttöisten salaisuuksien luomiseen heidän välilleen. BIP47:ssä käytetään sen sijaan ECDHE:tä (Elliptic Curve Diffie-Hellman Ephemeral).

ECDHE:tä käytetään alun perin BIP47:ssä lähettäjän maksukoodin välittämiseen vastaanottajalle. Tämä on kuuluisa ilmoitustransaktio. Jotta BIP47:tä voidaan käyttää, molempien osapuolten (maksuja lähettävän lähettäjän ja maksuja vastaanottavan vastaanottajan) on tiedettävä toistensa maksukoodit. Tämä on tarpeen kertakäyttöisten julkisten avainten ja siten omistettujen vastaanotto-osoitteiden johdannaisen määrittämiseksi.
Ennen tätä vaihtoa lähettäjä on loogisesti jo tietoinen vastaanottajan maksukoodista, sillä hän on voinut saada sen off-chain, esimerkiksi heidän verkkosivustoltaan tai sosiaalisen median kautta. Vastaanottaja ei kuitenkaan välttämättä tiedä lähettäjän maksukoodia. Sen on oltava välitetty heille, muuten he eivät kykene johdattamaan heidän efemääriavaimiaan ja siten eivät kykene tietämään, missä heidän bitcoinit ovat ja avaamaan varojaan. Se voitaisiin välittää heille off-chain käyttäen toista viestintäjärjestelmää, mutta tämä aiheuttaisi ongelman, jos lompakko palautetaan siemenestä. Todellakin, kuten olen jo maininnut, BIP47-osoitteet eivät johda vastaanottajan siemenestä (muuten olisi parempi käyttää suoraan yhtä heidän xpub-osoitteistaan), vaan ovat tulosta laskelmasta, joka sisältää sekä vastaanottajan maksukoodin että lähettäjän maksukoodin. Siksi, jos vastaanottaja menettää lompakkonsa ja yrittää palauttaa sen siemenestään, heidän on välttämättä saatava kaikkien ihmisten maksukoodit, jotka ovat lähettäneet heille bitcoineja BIP47:n kautta.

BIP47:n käyttö ilman tätä ilmoitustransaktiota olisi mahdollista, mutta jokaisen käyttäjän tarvitsisi varmuuskopioida vertaistensa maksukoodit. Tämä tilanne pysyy hallitsemattomana kunnes löydetään yksinkertainen ja kestävä tapa luoda, säilyttää ja päivittää näitä varmuuskopioita. Ilmoitustransaktio on siksi lähes pakollinen nykytilanteessa.

Lisäksi sen rooliin maksukoodien varmuuskopioinnissa, kuten sen nimi ehdottaa, tämä transaktio toimii myös ilmoituksena vastaanottajalle. Se informoi heidän asiakasohjelmaansa, että tunneli on juuri avattu.

Ennen kuin selitän tarkemmin ilmoitustransaktion teknistä toimintaa, haluaisin puhua hieman yksityisyyden mallista. Todellakin, BIP47:n yksityisyyden malli perustelee tiettyjä varotoimia, jotka otetaan huomioon tämän alkuperäisen transaktion rakentamisessa.

Maksukoodi itsessään ei suoraan aiheuta riskiä yksityisyydelle. Toisin kuin klassinen Bitcoin-malli, joka mahdollistaa tiedonkulun katkaisemisen käyttäjän identiteetin ja transaktioiden välillä, erityisesti pitämällä julkiset avaimet anonyymeinä, maksukoodi voidaan suoraan yhdistää identiteettiin. Tämä ei ole pakollista, mutta tämä linkki ei ole vaarallinen.

Todellakin, maksukoodi ei suoraan johda osoitteita, joita käytetään vastaanottamaan BIP47-maksuja. Sen sijaan osoitteet saadaan soveltamalla ECDHE:tä molempien osapuolten maksukoodien lapsiavainten välillä.

Siksi maksukoodi yksinään ei aiheuta suoraa riskiä yksityisyydelle, koska vain ilmoitusosoite johdetaan siitä. Siitä voidaan päätellä tiettyä tietoa, mutta normaalisti ei voi tietää, kenen kanssa olet tekemisissä.

On siis olennaista ylläpitää tiukkaa erottelua käyttäjien maksukoodien välillä. Tässä suhteessa koodin alkuperäinen viestintävaihe on kriittinen hetki maksuyksityisyydelle, ja kuitenkin se on välttämätön protokollan asianmukaisen toiminnan kannalta. Jos toisen maksukoodin voi julkisesti hankkia (esimerkiksi verkkosivustolta), toista koodia, eli lähettäjän koodia, ei tulisi yhdistää ensimmäiseen.

Esimerkiksi kuvitellaan, että haluan tehdä lahjoituksen BIP47:llä rauhanomaiselle protestiliikkeelle Kanadassa:

- Tämä järjestö on julkaissut maksukoodinsa suoraan verkkosivustollaan tai sosiaalisen median alustoilla.
- Tämä koodi on siis yhdistetty liikkeeseen.

- Haen tämän maksukoodin.

- Ennen kuin voin lähettää heille transaktion, minun on varmistettava, että he ovat tietoisia henkilökohtaisesta maksukoodistani, joka on myös yhdistetty identiteettiini, koska käytän sitä vastaanottaakseni transaktioita sosiaalisista verkostoistani.

Miten voin välittää sen heille? Jos lähetän sen heille käyttäen perinteistä viestintäkeinoa, tiedot saattavat vuotaa, ja minut voidaan tunnistaa henkilöksi, joka tukee rauhanomaisia liikkeitä.
Ilmoitustransaktio ei varmasti ole ainoa ratkaisu lähettäjän maksukoodin salaiseen välittämiseen, mutta se täyttää tämän roolin tällä hetkellä täydellisesti soveltamalla useita turvallisuustasoja.
Alla olevassa kaaviossa punaiset viivat edustavat hetkeä, jolloin tiedonkulun on katkettava, ja mustat nuolet edustavat kiistattomia yhteyksiä, jotka ulkopuolinen tarkkailija voi muodostaa:

![Yksityisyyden mallikaavio uudelleenkäytettävälle maksukoodille](assets/15.webp)

Todellisuudessa Bitcoinin klassisen yksityisyysmallin kohdalla on usein vaikeaa täysin katkaista tiedonkulku avainparin ja käyttäjän välillä, erityisesti suoritettaessa etätransaktioita. Esimerkiksi lahjoituskampanjan tapauksessa vastaanottajan on paljastettava osoite tai julkinen avain verkkosivustollaan tai sosiaalisen median alustoilla. BIP47:n asianmukainen käyttö, eli ilmoitustransaktion avulla, ratkaisee tämän ongelman ECDHE:n ja tutkittavan salauskerroksen avulla.

Ilmeisesti Bitcoinin klassista yksityisyysmallia noudatetaan edelleen kahden maksukoodin yhdistyksestä johdettujen ohimenevien julkisten avainten tasolla. Molemmat mallit ovat toisistaan riippuvaisia. Haluan vain tässä korostaa, että toisin kuin klassisessa julkisen avaimen käytössä bitcoinien vastaanottamiseen, maksukoodi voidaan yhdistää identiteettiin, koska tiedon "Bob tekee transaktion Alicen kanssa" katkaisu tapahtuu toisessa hetkessä. Maksukoodia käytetään maksuosoitteiden generoimiseen, mutta pelkästään lohkoketjua tarkkailemalla on mahdotonta yhdistää BIP47-maksutransaktiota käytettyihin maksukoodeihin.

### Ilmoitustransaktion rakentaminen.

Katsotaan nyt, miten tämä ilmoitustransaktio toimii. Kuvitellaan, että Alice haluaa lähettää varoja Bobille käyttäen BIP47:ää. Esimerkissäni Alice toimii lähettäjänä ja Bob vastaanottajana. Bob on jo julkaissut maksukoodinsa verkkosivustollaan, joten Alice tietää jo Bobin maksukoodin.

1. Alice laskee jaetun salaisuuden ECDH:n avulla:

- Hän valitsee avainparin HD-lompakostaan eri haarasta kuin hänen maksukoodinsa. Huomaa, että tätä paria ei pitäisi olla helppo yhdistää Alicen ilmoitusosoitteeseen tai Alicen identiteettiin (katso edellinen osio).
- Alice valitsee tästä parista yksityisen avaimen. Kutsutaan sitä "a":ksi (pieni kirjain).

> a

- Alice hakee julkisen avaimen, joka on yhdistetty Bobin ilmoitusosoitteeseen. Tämä avain on ensimmäinen lapsi, joka on johdettu Bobin maksukoodista (indeksi 0). Kutsutaan tätä julkista avainta "B":ksi (iso kirjain). Tähän julkiseen avaimen liittyvää yksityistä avainta kutsutaan "b":ksi (pieni kirjain). "B" määritetään pisteen lisäyksellä ja kaksinkertaistamisella elliptisellä käyrällä "G":stä (generaattoripiste) käyttäen "b":tä (yksityinen avain).

> B = b·G

- Alice laskee salaisen pisteen "S" (iso kirjain) elliptisellä käyrällä pisteen lisäyksellä ja kaksinkertaistamisella, soveltaen omaa yksityistä avaintaan "a" Bobin julkiseen avaimeseen "B".

> S = a·B

- Alice laskee sokaisukertoimen "f", jota käytetään hänen maksukoodinsa salaamiseen. Tätä varten hän generoi pseudo-satunnaisluvun käyttäen HMAC-SHA512-funktiota. Tämän funktion toisena syötteenä hän käyttää arvoa, jonka vain Bob pystyy noutamaan: (x), joka on aiemmin lasketun salaisen pisteen x-koordinaatti. Ensimmäinen syöte on (o), joka on tässä transaktiossa kulutettu UTXO (outpoint).

> f = HMAC-SHA512(o, x)

2. Alice muuntaa henkilökohtaisen maksukoodinsa kantaluvuksi 2 (binääriksi).
3. Hän käyttää tätä häikäisytekijää avaimena suorittaakseen symmetrisen salauksen maksukoodinsa kuormatiedolle. Käytetty salausalgoritmi on yksinkertaisesti XOR. Suoritettu toiminto on samankaltainen kuin Vernam-salakirjoitus, joka tunnetaan myös nimellä "kertakäyttöavain":
- Alice jakaa ensin häikäisytekijänsä kahteen osaan: ensimmäiset 32 tavua kutsutaan "f1":ksi ja viimeiset 32 tavua kutsutaan "f2":ksi. Joten meillä on:

> f = f1 || f2

- Alice laskee julkisen avaimensa x-koordinaatin (x) salatun tekstin (x') ja erikseen laskee ketjukoodinsa (c) salatun tekstin (c'). "f1" ja "f2" toimivat salausavaimina, ja XOR-operaatiota käytetään.

> x' = x XOR f1
>
> c' = c XOR f2

- Alice korvaa maksukoodissaan julkisen avaimen abskissan (x) ja ketjukoodin (c) todelliset arvot salattuilla arvoilla (x') ja (c').

Ennen kuin jatkamme tämän ilmoitustransaktion teknisen kuvauksen kanssa, käydään hetki läpi XOR-operaatio. XOR on bittikohtainen looginen operaattori, joka perustuu Boolen algebraan. Kahdelle bittioperaattorille annettuna se palauttaa 1, jos vastaavat bitit ovat erilaiset, ja se palauttaa 0, jos vastaavat bitit ovat samat. Tässä on totuustaulukko XOR:lle operandien D ja E arvojen perusteella:

| D   | E   | D XOR E |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

Esimerkiksi:

> 0110 XOR 1110 = 1000

Tai:

> 010011 XOR 110110 = 100101

ECDH:n kanssa XOR:n käyttö salauskerroksena on erityisen johdonmukaista. Ensinnäkin tämän operaattorin ansiosta salaus on symmetrinen. Tämä mahdollistaa vastaanottajan maksukoodin purkamisen samalla avaimella, jota käytettiin salaukseen. Salaus- ja purkuavain lasketaan jaetusta salaisuudesta käyttäen ECDH:ta.

Tämä symmetria mahdollistuu XOR-operaattorin vaihdannaisuuden ja liitännäisyyden ominaisuuksien ansiosta:

- Muut ominaisuudet:
  -> D ⊕ D = 0
  -> D ⊕ 0 = D

- Vaihdannaisuus:
  D ⊕ E = E ⊕ D

- Liitännäisyys:
  D ⊕ (E ⊕ Z) = (D ⊕ E) ⊕ Z = D ⊕ E ⊕ Z

- Symmetria:
  Jos: D ⊕ E = L
  Sitten: D ⊕ L = D ⊕ (D ⊕ E) = D ⊕ D ⊕ E = 0 ⊕ E = E
  -> D ⊕ L = E
Seuraavaksi tämä salausmenetelmä on hyvin samankaltainen kuin Vernam-salakirjoitus (One-Time Pad), ainoa tähän mennessä tunnettu salausalgoritmi, jolla on ehdoton (tai absoluuttinen) turvallisuus. Jotta Vernam-salakirjoituksella olisi tämä ominaisuus, salausavaimen on oltava täysin satunnainen, oltava samankokoinen kuin viesti ja sitä saa käyttää vain kerran. BIP47:ssä käytetyssä salausmenetelmässä avain on todellakin samankokoinen kuin viesti, sokaisutekijä on täsmälleen samaa kokoa kuin julkisen avaimen x-koordinaatin ja maksukoodiketjun koodin yhdistelmä. Tätä salausavainta käytetään todellakin vain kerran. Tämä avain ei kuitenkaan ole peräisin täydellisestä satunnaislähteestä, koska se on HMAC. Se on pikemminkin pseudosatunnainen. Siksi se ei ole Vernam-salakirjoitus, mutta menetelmä on samankaltainen.
Palataan takaisin ilmoitustransaktiomme rakentamiseen:

4. Alicella on tällä hetkellä maksukoodinsa salatun kuorman kanssa. Hän rakentaa ja lähettää transaktion, jossa hänen julkista avaintaan "A" käytetään syötteenä, lähtönä on Bobin ilmoitusosoite ja OP_RETURN-lähtö, joka koostuu hänen maksukoodistaan salatun kuorman kanssa. Tämä transaktio on ilmoitustransaktio.

OP_RETURN on Opcode, joka on skripti, joka merkitsee Bitcoin-transaktion lähdön mitättömäksi. Nykyään sitä käytetään tiedon lähettämiseen tai ankkurointiin Bitcoin-lohkoketjussa. Se voi tallentaa jopa 80 tavua dataa, jotka kirjataan ketjuun ja ovat siten näkyvissä kaikille muille käyttäjille.

Kuten edellisessä osiossa näimme, Diffie-Hellmania käytetään jaetun salaisuuden luomiseen kahden käyttäjän välillä, jotka kommunikoivat turvattomassa verkossa, mahdollisesti hyökkääjien tarkkailtavina. BIP47:ssä ECDH:ta käytetään kommunikointiin Bitcoin-verkossa, joka luonteensa vuoksi on läpinäkyvä kommunikaatioverkko, jota monet hyökkääjät tarkkailevat. Elliptisellä käyrällä Diffie-Hellmanin avainvaihdon kautta laskettua jaettua salaisuutta käytetään sitten salaisen tiedon salaamiseen lähetettäväksi: lähettäjän (Alicen) maksukoodi.

Tässä on kaavio BIP47:stä, joka havainnollistaa juuri kuvailemaamme:

![Kaavio Alice lähettää naamioimansa maksukoodin Bobin ilmoitusosoitteeseen](assets/16.webp)

Lähde: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Jos yhdistämme tämän kaavion siihen, mitä aiemmin kuvasin:

- "Wallet Priv-Key" Alicen puolella vastaa: a.

- "Child Pub-Key 0" Bobin puolella vastaa: B.
- "Notification Shared Secret" vastaa: f.
- "Masked Payment Code" vastaa salattua maksukoodia, eli salatun kuorman kanssa: x' ja c'.

- "Notification Transaction" on transaktio, joka sisältää OP_RETURN:n.

Kerrataanpa juuri käymämme vaiheet ilmoitustransaktion suorittamiseksi:

- Alice hakee Bobin maksukoodin ja ilmoitusosoitteen.

- Alice valitsee HD-lompakostaan UTXO:n, joka kuuluu hänelle ja jolla on vastaava avainpari.

- Hän laskee salaisen pisteen elliptisellä käyrällä käyttäen ECDH:ta.

- Hän käyttää tätä salaisuuspistettä HMAC:n laskemiseen, joka on sokaisutekijä.

- Hän käyttää tätä sokaisutekijää henkilökohtaisen maksukoodinsa kuorman salaamiseen.

- Hän käyttää OP_RETURN-transaktiolähtöä siirtääkseen naamioimansa maksukoodin Bobille.

Ymmärtääksemme sen toimintaa paremmin, erityisesti OP_RETURN:n käyttöä, tutkikaamme yhdessä todellista ilmoitustransaktiota. Suoritin tällaisen transaktion Testnetissä, jonka voit löytää klikkaamalla tästä:
Tarkastellessamme tätä transaktiota voimme jo nähdä, että sillä on yksi sisääntulo ja neljä ulostuloa:

- Ensimmäinen ulostulo on OP_RETURN, joka sisältää naamioitun maksukoodini.

- Toinen ulostulo, 546 satsia, osoittaa vastaanottajan ilmoitusosoitteeseen.

- Kolmas ulostulo, 15 000 satsia, edustaa palvelumaksua, sillä käytin Samourai Walletia tämän transaktion rakentamiseen.

- Neljäs ulostulo, kaksi miljoonaa satsia, edustaa vaihtorahaa, eli jäljelle jäävää erotusta sisääntulostani, joka menee takaisin toiseen minulle kuuluvaan osoitteeseen.

Mielenkiintoisin tutkittava on selvästi ulostulo 0, joka käyttää OP_RETURNia. Katsotaanpa tarkemmin, mitä se sisältää:

Löydämme ulostulon heksadesimaalisen skriptin:

> 6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d800000000000000000000000000

Tässä skriptissä voimme erottaa useita osia:
Opcodesien joukosta tunnistamme 0x6a:n, joka viittaa OP_RETURNiin, ja 0x4c:n, joka viittaa OP_PUSHDATA1:een. Tätä opcodea seuraava tavu ilmoittaa seuraavan kuorman koon. Se ilmoittaa 0x50:n, mikä on 80 tavua.

Seuraavaksi tulee maksukoodi salatun kuorman kanssa.

Tässä on maksukoodini, jota käytin tässä transaktiossa:

> Base 58 -muodossa:
>
> PM8TJQCyt6ovbozreUCBrfKqmSVmTzJ5vjqse58LnBzKFFZTwny3KfCDdwTqAEYVasn11tTMPc2FJsFygFd3YzsHvwNXLEQNADgxeGnMK8Ugmin62TZU
>
> Base 16 (HEX) -muodossa:
> 4701000277507c9c17a89cfca2d3af554745d6c2db0e7f6b2721a3941a504933103cc42add94881210d6e752a9abc8a9fa0070e85184993c4f643f1121dd807dd556d1dc000000000000000000000000008604e4db

Jos vertaamme maksukoodiani OP_RETURNiin, voimme nähdä, että HRP (ruskealla) ja tarkistussumma (pinkillä) eivät välity. Tämä on normaalia, sillä nämä tiedot on tarkoitettu ihmisille.
Seuraavaksi voimme tunnistaa (vihreällä) version (0x01), bittikentän (0x00) ja julkisen avaimen pariteetin (0x02). Ja maksukoodin lopussa tyhjät tavut mustana (0x00), jotka mahdollistavat täytteen lisäämisen, jotta kokonaisuus saavuttaa 80 tavua. Kaikki tämä metadata lähetetään avoimesti (salaamattomana). Lopuksi voimme havaita, että julkisen avaimen x-koordinaatti (sinisellä) ja ketjukoodi (punaisella) on salattu. Tämä muodostaa maksukoodin kuorman.

### Ilmoitustransaktion vastaanottaminen.

Nyt kun Alice on lähettänyt ilmoitustransaktion Bobille, katsotaan, miten hän tulkitsee sen.

Muistutuksena Bobin täytyy pystyä pääsemään käsiksi Alicen maksukoodiin. Ilman tätä tietoa, kuten seuraavassa osiossa näemme, hän ei pysty johdattamaan Alicen luomia avainpareja, eikä siten pääse käsiksi hänen BIP47:n kautta vastaanottamiinsa bitcoineihin. Toistaiseksi Alicen maksukoodin kuorma on salattu. Katsotaan yhdessä, miten Bob purkaa sen salauksen.

1. Bob seuraa transaktioita, jotka luovat ulostuloja hänen ilmoitusosoitteeseensa.

2. Kun transaktiossa on ulostulo hänen ilmoitusosoitteeseensa, Bob analysoi sen nähdäkseen, sisältääkö se OP_RETURN-ulostulon, joka noudattaa BIP47-standardia.

3. Jos OP_RETURN-kuorman ensimmäinen tavu on 0x01, Bob aloittaa mahdollisen jaetun salaisuuden etsinnän ECDH:n avulla:

- Bob valitsee transaktion syötteessä olevan julkisen avaimen. Toisin sanoen Alicen julkisen avaimen nimeltä "A":

> A = a·G

- Bob valitsee yksityisen avaimen "b", joka on yhdistetty hänen henkilökohtaiseen ilmoitusosoitteeseensa:

> b

- Bob laskee salaisen pisteen "S" (ECDH:n jaetun salaisuuden) elliptisellä käyrällä lisäämällä ja kaksinkertaistamalla pisteitä, soveltamalla yksityistä avaintaan "b" Alicen julkiseen avaimen "A":

> S = b·A

- Bob määrittää hämärtävän tekijän "f", joka mahdollistaa Alicen maksukoodin kuorman salauksen purkamisen. Samalla tavalla kuin Alice laski sen aiemmin, Bob löytää "f":n soveltamalla HMAC-SHA512:ta (x) salaisen pisteen "S" x-koordinaatin arvoon, ja (o) tässä ilmoitustransaktiossa käytettyyn UTXO:n syötteeseen:

> f = HMAC-SHA512(o, x)

4. Bob tulkitsee ilmoitustransaktion OP_RETURN:n tiedot maksukoodina. Hän yksinkertaisesti purkaa tämän mahdollisen maksukoodin kuorman salauksen käyttämällä hämärtävää tekijää "f".

- Bob jakaa hämärtävän tekijän "f" kahteen osaan: "f":n ensimmäiset 32 tavua ovat "f1" ja viimeiset 32 tavua ovat "f2".
- Bob purkaa salatun x-koordinaatin arvon (x') Alicen maksukoodin julkisesta avaimesta:

> x = x' XOR f1

- Bob purkaa salatun ketjukoodin arvon (c') Alicen maksukoodista:

> c = c' XOR f2

5. Bob tarkistaa, kuuluuko Alicen maksukoodin julkinen avain secp256k1-ryhmään. Jos kuuluu, hän tulkitsee sen kelvolliseksi maksukoodiksi. Muussa tapauksessa hän jättää transaktion huomiotta.

Nyt kun Bob tietää Alicen maksukoodin, hän voi lähettää hänelle jopa 2^32 maksua tarvitsematta suorittaa tällaista ilmoitustransaktiota uudelleen.

Miksi tämä toimii? Miten Bob voi määrittää saman hämärtävän tekijän kuin Alice ja purkaa hänen maksukoodinsa salauksen? Tutkitaan ECDH-prosessia tarkemmin sen perusteella, mitä juuri kuvasimme.
Aluksi käsittelemme symmetristä salakirjoitusta. Tämä tarkoittaa, että salausavain ja purkuavain ovat sama arvo. Tässä tapauksessa ilmoitustransaktion avain on häivyttävä tekijä (f = f1 || f2). Alicen ja Bobin on saatava sama arvo f:lle lähettämättä sitä suoraan, sillä hyökkääjä voisi siepata sen ja purkaa salaisen tiedon.

Tämä häivyttävä tekijä saadaan soveltamalla HMAC-SHA512:ta kahteen arvoon: salaisen pisteen x-koordinaattiin ja transaktion syötteenä käytettyyn kulutettuun UTXO:oon. Siksi Bobin on tiedettävä nämä kaksi tietoa purkaakseen Alicen maksukoodin kuorman.

Syötteen UTXO:n osalta Bob voi yksinkertaisesti hankkia sen tarkkailemalla ilmoitustransaktiota. Salaisen pisteen osalta Bobin on käytettävä ECDH:ta.

Kuten Diffie-Hellmanin osiossa nähtiin, vaihtamalla keskenään julkiset avaimensa ja salaa soveltamalla omia yksityisiä avaimiaan toisen julkiseen avaimeseen, Alice ja Bob voivat löytää tietyn ja salaisen pisteen elliptisellä käyrällä. Ilmoitustransaktio perustuu tähän mekanismiin:

> Bobin avainpari:
>
> B = b·G
>
> Alicen avainpari:
>
> A = a·G
>
> Salaiselle pisteelle S (x,y):
>
> S = a·B = a·b·G = b·a·G = b·A

![Kaavio jaetun salaisuuden luomisesta ECDHE:llä](assets/19.webp)
Nyt kun Bob tietää Alicen maksukoodin, hän pystyy havaitsemaan hänen BIP47-maksunsa ja johdattamaan yksityiset avaimet, jotka estävät saadut bitcoinit.
![Bob tulkitsee Alicen ilmoitustransaktion](assets/20.webp)

Lähde: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Jos yhdistämme tämän kaavion siihen, mitä kuvasin sinulle aiemmin:

- "Wallet Pub-Key" Alicen puolella vastaa: A.

- "Child Priv-Key 0" Bobin puolella vastaa: b.

- "Notification Shared Secret" vastaa: f.

- "Masked Payment Code" vastaa Alicen naamioitua maksukoodia, eli salatulla kuormalla: x' ja c'.

- "Notification Transaction" on transaktio, joka sisältää OP_RETURN:n.

Kerrataanpa yhdessä näkemämme vaiheet ilmoitustransaktion vastaanottamiseksi ja tulkitsemiseksi:

- Bob tarkkailee transaktiotulosteita hänen ilmoitusosoitteeseensa.

- Kun hän havaitsee yhden, hän hankkii OP_RETURN:ssa olevan tiedon.

- Bob valitsee syötteen julkisen avaimen ja laskee salaisen pisteen käyttäen ECDH:ta.

- Hän käyttää tätä salaisuutta laskemaan HMAC:n, joka on häivyttävä tekijä.

- Hän käyttää tätä häivyttävää tekijää purkaakseen Alicen maksukoodin kuorman, joka sisältyy OP_RETURN:iin.

### BIP47-maksutransaktio.

Käsitellään nyt maksuprosessia BIP47:n kanssa. Muistuttaakseni sinua nykyisestä tilanteesta:

- Alice tietää Bobin maksukoodin, jonka hän yksinkertaisesti hankki hänen verkkosivustoltaan.

- Bob tietää Alicen maksukoodin kiitos ilmoitustransaktion.

- Alice tekee alustavan maksun Bobille. Hän voi tehdä monta lisää samalla tavalla.

Ennen kuin selitän tämän prosessin sinulle, pidän tärkeänä muistuttaa sinua, millä indekseillä tällä hetkellä työskentelemme:

Kuvaamme maksukoodin johdatuspolun seuraavasti: m/47'/0'/0'/.

Seuraava syvyys jakaa indeksit seuraavasti:
- Ensimmäistä normaalia (ei-kovennettua) lapsiparia käytetään luomaan ilmoitusosoite, josta keskustelimme edellisessä osiossa: m/47'/0'/0'/0/.
- Normaaleja lapsiavainpareja käytetään ECDH:ssa BIP47-maksun vastaanotto-osoitteiden luomiseen, kuten näemme tässä osiossa: m/47'/0'/0'/ alkaen 0:sta 2 147 483 647:ään.

- Kovennetut lapsiavainparit ovat ohimeneviä maksukoodeja: m/47'/0'/0'/ alkaen 0':sta 2 147 483 647':ään.
  Aina kun Alice haluaa lähettää maksun Bobille, hän johtaa uuden uniikin tyhjän osoitteen, jälleen kerran kiitos ECDH-protokollan:
- Alice valitsee ensimmäisen yksityisen avaimen, joka on johdettu hänen henkilökohtaisesta uudelleenkäytettävästä maksukoodistaan:

> a

- Alice valitsee ensimmäisen käyttämättömän julkisen avaimen, joka on johdettu Bobin maksukoodista. Tätä julkista avainta kutsutaan "B":ksi. Se liittyy yksityiseen avaimen "b", jonka vain Bob tietää.

> B = b·G

- Alice laskee salaisen pisteen "S" elliptisellä käyrällä lisäämällä ja kaksinkertaistamalla pisteitä, soveltamalla omaa yksityistä avaintaan "a" Bobin julkiseen avaimen "B":

> S = a·B

- Tästä salaisesta pisteestä Alice laskee jaetun salaisuuden "s" (pienet kirjaimet). Tehdäkseen tämän, hän valitsee salaisen pisteen "S" x-koordinaatin, jota kutsutaan "Sx":ksi, ja syöttää tämän arvon SHA256-hajautusfunktioon.

> s = SHA256(Sx)

Älä luota. Varmista! Jos haluat ymmärtää hajautusfunktion perusperiaatteet, löydät tarvitsemasi tästä artikkelista. Ja jos et luota NIST:iin (olet oikeassa), ja haluat pystyä ymmärtämään yksityiskohtaisesti, miten SHA256 toimii, selitän kaiken tässä artikkelissa ranskaksi.

- Alice käyttää tätä jaettua salaisuutta "s" laskeakseen Bitcoin-maksun vastaanotto-osoitteen. Ensinnäkin hän tarkistaa, että "s" on secp256k1-käyrän järjestyksen sisällä. Jos ei, hän kasvattaa Bobin julkisen avaimen indeksiä johdtaakseen toisen jaetun salaisuuden.

- Toiseksi hän laskee julkisen avaimen "K0" lisäämällä pisteet "B" ja "s·G" elliptisellä käyrällä. Toisin sanoen, Alice lisää julkisen avaimen, joka on johdettu Bobin maksukoodista "B", toisen pisteen kanssa, joka on laskettu elliptisellä käyrällä lisäämällä ja kaksinkertaistamalla pisteitä jaetulla salaisuudella "s" secp256k1-käyrän generaattoripisteestä "G". Tämä uusi piste edustaa julkista avainta, ja kutsumme sitä "K0":

> K0 = B + s·G

- Tällä julkisella avaimella "K0" Alice voi johtaa tyhjän vastaanotto-osoitteen standarditavalla (esimerkiksi SegWit V0 Bech32:ssa).

Kun Alicella on tämä vastaanotto-osoite "K0", joka kuuluu Bobille, hän voi rakentaa standardin Bitcoin-siirron valitsemalla UTXO:n, joka kuuluu hänelle toisella haaralla hänen HD-lompakossaan, ja käyttämällä sitä Bobin "K0" osoitteeseen.

![Alice lähettää bitcoineja BIP47:n avulla Bobille](assets/21.webp)

Lähde: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki
Jos yhdistämme tämän kaavion siihen, mitä kuvasin sinulle aiemmin:

- "Child Priv-Key" Alicen puolella vastaa: a.
- "Child Pub-Key 0" Bobin puolella vastaa: B.
- "Payment Secret 0" vastaa: s.
- "Maksun Julkinen Avain 0" vastaa: K0.
Kerrataanpa yhdessä läpi käymämme vaiheet BIP47-maksun lähettämiseksi:

- Alice valitsee ensimmäisen johdetun lapsen yksityisen avaimen henkilökohtaisesta maksukoodistaan.
- Hän laskee salaisen pisteen elliptisellä käyrällä käyttäen ECDH:ta ensimmäisestä käyttämättömästä johdetusta lapsen julkisesta avaimesta Bobin maksukoodista.
- Hän käyttää tätä salaisen pistettä laskeakseen jaetun salaisuuden SHA256:n avulla.
- Hän käyttää tätä jaettua salaisuutta laskemaan uuden salaisen pisteen elliptisellä käyrällä.
- Hän lisää tämän uuden salaisen pisteen Bobin julkiseen avaimen.
- Hän saa uuden efemeraalisen julkisen avaimen, johon vain Bobilla on yhdistetty yksityinen avain.
- Alice voi lähettää tavallisen siirron Bobille johdetulla efemeraalisella vastaanotto-osoitteella.

Jos hän haluaa tehdä toisen maksun, hän toistaa yllä olevat vaiheet, paitsi että hän valitsee toisen johdetun julkisen avaimen Bobin maksukoodista. Eli seuraavan käyttämättömän avaimen. Hänellä on silloin toinen vastaanotto-osoite, joka kuuluu Bobille, "K1".

![Alice johtaa kolme BIP47-vastaanotto-osoitetta Bobille](assets/22.webp)

Lähde: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Hän voi jatkaa näin ja johtaa jopa 2^32 tyhjää osoitetta, jotka kuuluvat Bobille.

Ulkopuolisen näkökulmasta, Bitcoin-lohkoketjua tarkkailemalla, on teoriassa mahdotonta erottaa BIP47-maksua tavallisesta maksusta. Tässä on esimerkki BIP47-maksutapahtumasta Testnetissä:

https://blockstream.info/testnet/tx/94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254

TXID:

> 94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254

Se näyttää tavalliselta tapahtumalta, jossa on käytetty syöte, maksutulos 210 000 satsia ja vaihtoraha.

![Bitcoin-maksutapahtuma BIP47:llä](assets/23.webp)

Lähde: https://blockstream.info/

### BIP47-maksun vastaanottaminen ja yksityisen avaimen johtaminen.

Alice on juuri tehnyt ensimmäisen maksunsa tyhjään BIP47-osoitteeseen, joka kuuluu Bobille. Katsotaan nyt, miten Bob vastaanottaa tämän maksun. Näemme myös, miksi Alicella ei ole pääsyä juuri luomansa osoitteen yksityiseen avaimen, ja miten Bob hakee tämän avaimen käyttääkseen juuri vastaanottamiaan bitcoineja.

Kun Bob vastaanottaa ilmoitustapahtuman Alicelta, hän johtaa BIP47-julkisen avaimen "K0" ennen kuin Alice lähettää siihen mitään maksua. Hän siis tarkkailee mahdollisia maksuja kyseiseen osoitteeseen. Itse asiassa hän johtaa välittömästi useita osoitteita, joita hän tulee tarkkailemaan (K0, K1, K2, K3...). Tässä on, miten hän johtaa tämän julkisen avaimen "K0":

- Bob valitsee ensimmäisen lapsen yksityisen avaimen, joka on johdettu hänen maksukoodistaan. Tätä yksityistä avainta kutsutaan "b":ksi. Se liittyy julkiseen avaimen "B", jota Alice käytti edellisessä vaiheessa:

> b

- Bob valitsee Alicen ensimmäisen johdetun julkisen avaimen hänen maksukoodistaan. Tätä avainta kutsutaan "A":ksi. Se liittyy yksityiseen avaimen "a", jota Alice käytti laskelmissaan, ja josta vain Alice on tietoinen. Bob voi suorittaa tämän prosessin, koska hän tuntee Alicen maksukoodin, joka lähetettiin hänelle ilmoitustapahtumassa.

> A = a·G
- Bob laskee salaisen pisteen "S" lisäämällä ja kaksinkertaistamalla pisteitä elliptisellä käyrällä, soveltaen omaa yksityistä avaintaan "b" Alicen julkiseen avaimen "A". Tässä käytämme ECDH:ta, joka takaa, että tämä piste "S" on sama sekä Bobille että Alicelle.
> S = b·A

- Aivan kuten Alice teki, Bob eristää tämän pisteen "S" x-koordinaatin. Olemme nimenneet tämän arvon "Sx". Hän syöttää tämän arvon SHA256-funktioon löytääkseen jaetun salaisuuden "s" (pienet kirjaimet).

> s = SHA256(Sx)

- Samalla tavalla kuin Alice, Bob laskee pisteen "s·G" elliptisellä käyrällä. Sen jälkeen hän lisää tämän salaisen pisteen julkiseen avaimensa "B". Hän saa näin uuden pisteen elliptisellä käyrällä, jonka hän tulkitsee julkiseksi avaimiksi "K0":

> K0 = B + s·G

Kun Bob on saanut tämän julkisen avaimen "K0", hän voi johtaa siihen liittyvän yksityisen avaimen käyttääkseen bitcoinejaan. Hän on ainoa, joka voi generoida tämän numeron.

- Bob lisää johdetun lapsi-yksityisavaimensa "b" henkilökohtaisesta maksukoodistaan. Hän on ainoa, joka voi saada "b":n arvon. Sen jälkeen hän lisää "b":n jaetun salaisuuden "s" kanssa saadakseen k0:n, K0:n yksityisen avaimen:

> k0 = b + s
> Kiitos elliptisen käyrän ryhmälain, Bob saa täsmälleen sen yksityisen avaimen, joka vastaa Alicen käyttämää julkista avainta. Joten meillä on:
> K0 = k0·G

![Bob generoi BIP47 vastaanotto-osoitteensa](assets/24.webp)

Lähde: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Jos yhdistämme tämän kaavion siihen, mitä aiemmin kuvailin:

- "Child Priv-Key 0" Bobin puolella vastaa: b.

- "Child Pub-Key 0" Alicen puolella vastaa: A.

- "Payment Secret 0" vastaa: s.

- "Payment Pub-Key 0" vastaa: K0.

- "Payment Priv-Key 0" vastaa: k0.

Tiivistetään yhdessä näkemämme vaiheet BIP47 maksun vastaanottamiseksi ja vastaavan yksityisen avaimen laskemiseksi:

- Bob valitsee ensimmäisen johdetun lapsi-yksityisavaimen henkilökohtaisesta maksukoodistaan.

- Hän laskee salaisen pisteen elliptisellä käyrällä käyttäen ECDH:ta ensimmäisestä johdetusta lapsi-julkisesta avaimesta Alicen ketjukoodista.

- Hän käyttää tätä salaista pistettä laskemaan jaetun salaisuuden SHA256:n avulla.

- Hän käyttää tätä jaettua salaisuutta laskemaan uuden salaisen pisteen elliptisellä käyrällä.

- Hän lisää tämän uuden salaisen pisteen henkilökohtaiseen julkiseen avaimensa.

- Hän saa uuden efemeraalisen julkisen avaimen, johon Alice lähettää ensimmäisen maksunsa.

- Bob laskee efemeraalisen julkisen avaimen yhdistetyn yksityisen avaimen lisäämällä johdetun lapsi-yksityisavaimensa maksukoodistaan ja jaetun salaisuuden.

Koska Alice ei voi saada "b":tä, Bobin yksityistä avainta, hän ei pysty määrittämään k0:aa, yksityistä avainta, joka liittyy Bobin BIP47 vastaanotto-osoitteeseen.

Kaaviona voimme esittää jaetun salaisuuden "S" laskennan seuraavasti:

![Jaetun salaisuuden laskenta ECDHE:n avulla](assets/25.webp)

Kun jaettu salaisuus on löydetty ECDH:n avulla, Alice ja Bob laskevat BIP47 maksun julkisen avaimen "K0", ja Bob laskee myös liittyvän yksityisen avaimen "k0":
![BIP47:n vastaanotto-osoitteen johdannaisuus jaetusta salaisuudesta](assets/26.webp)
### BIP47-maksun palauttaminen.

Koska Bob tietää Alicen uudelleenkäytettävän maksukoodin, hänellä on jo kaikki tarvittavat tiedot lähettääkseen hänelle hyvityksen. Hänen ei tarvitse ottaa yhteyttä Aliceen pyytääkseen mitään tietoja. Hän ilmoittaa hänelle yksinkertaisesti ilmoitustransaktiolla, erityisesti jotta Alice voi palauttaa BIP47-osoitteensa siemenensä avulla, ja sitten hän voi myös lähettää hänelle jopa 2^32 maksua.
Bob voi sitten hyvittää Alicen samalla tavalla kuin Alice lähetti hänelle maksuja. Roolit vaihtuvat:

![Bob lähettää hyvityksen Alicelle BIP47:n avulla](assets/27.webp)

Lähde: Uudelleenkäytettävät Maksukoodit Hierarkkisille Deterministisille Lompakoille, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Nyt tiedät kaikki tämän upean ratkaisun, jonka BIP47 edustaa, yksityiskohdat.

## PayNymien johdannaiskäytöt.

Tämän BIP47:n toteutus Samourai Walletissa on johtanut PayNymeihin, tunnisteisiin, jotka on laskettu käyttäjien maksukoodien perusteella. Tänään niiden hyödyllisyys menee paljon pidemmälle kuin pelkkä BIP47:n käyttö.

Samourai-tiimi kehittää vähitellen kokonaista työkalujen ja palveluiden ekosysteemiä käyttäjän PayNymien perusteella. Näiden joukossa on tietenkin kaikki kulutustyökalut, jotka mahdollistavat käyttäjän yksityisyyden optimoinnin lisäämällä entropiaa transaktioon ja siten lisäämällä uskottavaa kiistämättömyyttä.

Sorobanin, Toriin perustuvan salatun viestintäverkon, ja PayNymien yhdistetty käyttö on suuresti optimoinut käyttäjäkokemusta yhteistyöllisten transaktioiden rakentamisessa, samalla kun turvallisuustaso on säilytetty hyvänä. Näin ollen on helppoa suorittaa Stowaway (PayJoin) ja StonewallX2 -transaktioita ilman, että tarvitsee manuaalisesti suorittaa lukuisia allekirjoittamattomien transaktioiden vaihtoja tällaisen yhteistyöllisen transaktion perustamiseksi.

Toisin kuin BIP47:n käytössä, koska nämä yhteistyölliset transaktiot eivät vaadi ilmoitustransaktiota, riittää, että PayNymit linkitetään näiden työkalujen käyttöön. Niitä ei tarvitse yhdistää.

Jos haluat oppia lisää yhteistyöllisistä transaktioista ja laajemmin kaikista Samourai Walletin kulutustyökaluista, voit lukea artikkelin "Spending Tools" -osion. Löydät teknisen selityksen ja yksityiskohtaisen opastuksen kullekin työkalulle.

Näiden yhteistyöllisten transaktioiden lisäksi on äskettäin havaittu, että Samourai-tiimi työskentelee PayNymiin liittyvän todennusprotokollan parissa: Auth47. Tämä työkalu on jo toteutettu ja mahdollistaa esimerkiksi todentamisen PayNymillä verkkosivustolla, joka hyväksyy tämän menetelmän. Tulevaisuudessa uskon, että tämän verkkotodennuksen mahdollisuuden lisäksi Auth47 on osa suurempaa projektia BIP47/PayNym/Samourai-ekosysteemin ympärillä. Ehkä tätä protokollaa käytetään edelleen optimoimaan Samourai Walletin käyttäjäkokemusta, erityisesti kulutustyökalujen käytössä. Jää nähtäväksi...

## Henkilökohtainen mielipiteeni BIP47:stä.

Ilmeisesti BIP47:n päähaitta on ilmoitustransaktio. Se johtaa siihen, että käyttäjän on maksettava sen louhinnasta aiheutuvat maksut, mikä voi olla ärsyttävää joillekin. Kuitenkin väite "spämmistä" Bitcoin-lohkoketjussa on täysin hyväksymätön. Jokaisen, joka maksaa transaktionsa maksut, tulee pystyä kirjaamaan se lohkoketjuun, riippumatta sen tarkoituksesta. Väittää muuta on sensuurin kannattamista.

On mahdollista, että tulevaisuudessa löydetään muita vähemmän kalliita ratkaisuja lähettäjän maksukoodin kommunikoimiseksi vastaanottajalle ja vastaanottajan turvalliseen tallentamiseen. Mutta toistaiseksi ilmoitustransaktio on vähiten kompromisseja sisältävä ratkaisu.
Tämä haitta on merkityksetön, kun otetaan huomioon kaikki BIP47:n edut. Kaikista olemassa olevista ehdotuksista osoitteen uudelleenkäytön ongelman ratkaisemiseksi se vaikuttaa minusta parhaalta ratkaisulta.
Kuten aiemmin selitin, suurin osa osoitteen uudelleenkäytöstä johtuu vaihdoista. BIP47 on ainoa järkevä ratkaisu, joka todella ratkaisee tämän ongelman sen alkulähteillä. Kaikkien ehdotusten, jotka pyrkivät vähentämään osoitteen uudelleenkäytön määrää, tulisi keskittyä tähän näkökohtaan ja mukauttaa ratkaisu ongelman päälähteeseen.

Käytettävyyden osalta, vaikka sen sisäinen toiminta onkin melko monimutkaista, BIP47:n maksuproseduuri on suoraviivainen. Uudelleenkäytettävät maksukoodit voidaan siis helposti ottaa käyttöön, jopa aloittelijoiden toimesta.

Yksityisyyden kannalta BIP47 on erittäin mielenkiintoinen. Kuten selitin ilmoitustransaktiota käsittelevässä osiossa, maksukoodi ei paljasta mitään tietoa johdetuista ohimenevistä osoitteista. Se katkaisee siis tiedonkulun Bitcoin-transaktion ja vastaanottajan tunnisteen välillä, toisin kuin perinteisen vastaanotto-osoitteen käyttö.

Ja ennen kaikkea, BIP47:n PayNym-toteutus toimii! Sitä on ollut saatavilla Samourai Walletissa vuodesta 2016 ja Sparrow Walletissa tämän vuoden alusta. Se ei ole tieteellinen projekti, vaan ratkaisu, joka on testattu eilen ja on täysin toimiva tänään.

Toivottavasti tulevaisuudessa nämä uudelleenkäytettävät maksukoodit otetaan käyttöön ekosysteemin toimijoiden toimesta, toteutetaan lompakko-ohjelmistoihin ja niitä käyttävät Bitcoin-käyttäjät.

Kaikki todella positiiviset ratkaisut käyttäjän yksityisyyden kannalta on keskusteltava, edistettävä ja puolustettava, jotta Bitcoin ei muutu CA:iden leikkikentäksi ja hallitusten valvontatyökaluksi.
Hän mietti, kuinka häntä oli vainottu ja loukattu kaikkialla, ja nyt hän kuuli kaikkien sanovan, että hän oli kaikista kaunein näistä kauniista linnuista! Ja jopa selja taivutti oksansa häntä kohti, ja aurinko levitti niin lämmintä ja hyväntahtoista valoa! Silloin hänen höyhenensä pörhistyivät, hänen hoikka kaulansa suoristui, ja hän huudahti koko sydämestään, "Kuinka olisin voinut unelmoida näin suuresta onnesta ollessani vain ruma pieni ankanpoikanen."

## Edetäkseen pidemmälle:

- CoinJoinin ymmärtäminen ja käyttäminen Bitcoinissa.

- Bitcoin-lompakon johdannaispolkujen ymmärtäminen.

- RoninDojo Bitcoin-noodin asentaminen ja käyttäminen.

### Ulkoiset resurssit ja kiitokset:

Kiitos LaurentMT:lle ja Théo Pantamisille lukuisista konsepteista, joita he selittivät minulle ja joita käytin tässä artikkelissa. Toivon, että olen välittänyt ne tarkasti.

Kiitos Fanis Michalakisille tekstin oikoluvusta ja asiantuntijaneuvoista.

- https://bitcoiner.guide/paynym/
- https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman_bas%C3%A9_sur_les_courbes_elliptiques
- https://security.stackexchange.com/questions/46802/what-is-the-difference-between-dhe-and-ecdh#:~:text=The%20difference%20between%20DHE%20and%20ECDH%20in%20two%20bullet%20points,a%20type%20of%20algebraic%20curve).
- https://commandlinefanatic.com/cgi-bin/showarticle.cgi?article=art060
- https://ee.stanford.edu/~hellman/publications/24.pdf
- https://www.researchgate.net/publication/317339928_A_study_on_diffie-hellman_key_exchange_protocols