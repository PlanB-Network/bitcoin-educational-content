---
name: Stonewall x2
description: Ymmärrys ja Stonewall x2 -transaktioiden käyttö
---
![cover stonewall x2](assets/cover.webp)

***VAROITUS:** Samourai Walletin perustajien pidätyksen ja heidän palvelimiensa takavarikoinnin jälkeen 24. huhtikuuta, Stonewallx2-transaktiot toimivat vain manuaalisesti vaihtamalla PSBT-tiedostoja asianomaisten osapuolten kesken, edellyttäen, että molemmat käyttäjät ovat yhdistettyinä omaan Dojoonsa. On kuitenkin mahdollista, että nämä työkalut saatetaan käynnistää uudelleen tulevina viikkoina. Siihen asti voit silti tutustua tähän artikkeliin ymmärtääksesi Stonewallx2:n teoreettisen toiminnan ja oppiaksesi tekemään ne manuaalisesti.*

_Jos harkitset Stonewallx2:n suorittamista manuaalisesti, menettely on hyvin samankaltainen kuin tässä opetusohjelmassa kuvattu. Pääero on Stonewallx2-transaktion tyypin valinnassa: `Online`-vaihtoehdon sijaan klikkaa `In Person / Manual`. Sen jälkeen sinun on vaihdettava PSBT-tiedostot manuaalisesti Stonewallx2-transaktion muodostamiseksi. Jos olet fyysisesti lähellä yhteistyökumppaniasi, voit skannata QR-koodeja peräkkäin. Jos olette etäällä, JSON-tiedostoja voidaan vaihtaa turvallisen viestintäkanavan kautta. Loput opetusohjelmasta pysyvät muuttumattomina._

_Seuraamme tiiviisti tämän tapauksen kehitystä sekä siihen liittyvien työkalujen kehitystä. Voit olla varma, että päivitämme tämän opetusohjelman, kun uutta tietoa tulee saataville._

_Tämä opetusohjelma on tarkoitettu vain koulutus- ja tiedotustarkoituksiin. Emme tue tai kannusta näiden työkalujen käyttöä rikollisiin tarkoituksiin. Jokaisen käyttäjän on noudatettava oman lainkäyttöalueensa lakeja._

---

> *Tee jokaisesta menosta coinjoin.*

## Mikä on Stonewall x2 -transaktio?

Stonewall x2 on tietty Bitcoin-transaktion muoto, jonka tavoitteena on lisätä käyttäjän yksityisyyttä maksun yhteydessä, tekemällä yhteistyötä kolmannen osapuolen kanssa, joka ei ole osallisena kyseisessä maksussa. Tämä menetelmä simuloii mini-coinjoinia kahden osallistujan välillä, samalla kun tehdään maksu kolmannelle osapuolelle. Stonewall x2 -transaktiot ovat saatavilla sekä Samourai Wallet -sovelluksessa että Sparrow Wallet -ohjelmistossa. Molemmat ovat yhteensopivia.

Sen toiminta on suhteellisen yksinkertaista: käytämme hallussamme olevaa UTXO:a maksun suorittamiseen ja pyydämme kolmannen osapuolen apua, joka myös osallistuu omalla UTXO:llaan. Transaktio tuottaa neljä lähtöä: kaksi niistä ovat samansuuruisia, toinen on tarkoitettu maksunsaajan osoitteeseen, toinen yhteistyökumppanin osoitteeseen. Kolmas UTXO palautetaan toiseen yhteistyökumppanin osoitteeseen, jolloin he voivat hakea alkuperäisen summan takaisin (neutraali toiminto heille, louhintamaksuja lukuun ottamatta), ja lopullinen UTXO palautuu osoitteeseemme, joka muodostaa maksun vaihtorahan.

Näin ollen Stonewall x2 -transaktioissa määritellään kolme eri roolia:
- Lähettäjä, joka suorittaa varsinaisen maksun;
- Yhteistyökumppani, joka tarjoaa bitcoineja parantaakseen transaktion kokonaisanonyymiyttä, samalla täysin palauttaen varansa lopussa (neutraali toiminto heille, louhintamaksuja lukuun ottamatta);
- Vastaanottaja, joka saattaa olla tietämätön transaktion erityisluonteesta ja yksinkertaisesti odottaa maksua lähettäjältä.

Otetaan esimerkki paremman ymmärryksen saavuttamiseksi. Alice on leipomossa ostamassa patonkiaan, joka maksaa `4,000 satsia`. Hän haluaa maksaa bitcoineilla säilyttäen tietyn yksityisyyden tason maksussaan. Siksi hän pyytää apua ystävältään Bobilta, joka auttaa häntä tässä prosessissa.
![schema stonewall x2](assets/en/1.webp)
Tämän transaktion analysoinnin perusteella voimme nähdä, että leipuri todellakin sai `4,000 sats` maksuna patongista. Alice käytti `10,000 sats` sisääntulona ja sai `6,000 sats` ulostulona, mikä johti nettotaseeseen `-4,000 sats`, mikä vastaa patongin hintaa. Mitä tulee Bobiin, hän antoi `15,000 sats` sisääntulona ja sai kaksi ulostuloa: toisen `4,000 sats` ja toisen `11,000 sats`, mikä johti tasapainoon `0`. Tässä esimerkissä jätin tarkoituksella huomiotta louhintapalkkiot ymmärryksen helpottamiseksi. Todellisuudessa transaktiomaksut jaetaan tasan maksun lähettäjän ja yhteistyökumppanin kesken.

## Mikä on ero Stonewallin ja Stonewall x2:n välillä?

StonewallX2-transaktio toimii täsmälleen kuten Stonewall-transaktio, paitsi että edellinen on yhteistyöllinen kun taas jälkimmäinen ei ole. Kuten olemme nähneet, Stonewall x2 -transaktioon osallistuu kolmas osapuoli, joka on ulkopuolinen maksuun nähden, ja joka tarjoaa bitcoinejaan transaktion yksityisyyden lisäämiseksi. Tyypillisessä Stonewall-transaktiossa yhteistyökumppanin roolin ottaa lähettäjä.

Palatkaamme esimerkkiimme Alicesta leipomossa. Jos hän ei olisi löytänyt ketään kuten Bobia saattamaan häntä hänen menossaan, hän olisi voinut tehdä Stonewall-transaktion yksin. Näin ollen molemmat sisääntulon UTXO:t olisivat olleet hänen, ja hän olisi saanut 3 ulostulossa.
![transaction stonewall](assets/en/2.webp)

Ulkopuolisen näkökulmasta transaktiokuvio olisi pysynyt samana.
![Stonewall vai Stonewall x2?](assets/en/5.webp)
Joten logiikan tulisi olla seuraava, kun käytetään Samourain maksutyökalua:
- Jos kauppias ei tue Payjoin Stowawayta, yhteistyöllinen transaktio voidaan tehdä toisen henkilön kanssa, joka on ulkopuolinen maksuun nähden, käyttäen Stonewall x2:ta.
- Jos ketään ei löydy tekemään Stonewall x2 -transaktiota, Stonewall-transaktio voidaan tehdä yksin, matkien Stonewall x2 -transaktion käyttäytymistä.
- Lopulta viimeinen vaihtoehto olisi tehdä transaktio JoinBotin kanssa, palvelimen, jota ylläpitää Samourai, joka pyynnöstä voi toimia yhteistyökumppanina Stonewall x2 -transaktiossa.

Jos haluat löytää yhteistyökumppanin, joka on valmis auttamaan sinua Stonewall X2 -transaktiossa, voit myös vierailla tässä Telegram-ryhmässä (epävirallinen), jota ylläpitävät Samourain käyttäjät yhdistääkseen lähettäjiä ja yhteistyökumppaneita: [Make Every Spend a Coinjoin](https://t.me/EverySpendACoinjoin).

[**-> Lisätietoja Stonewall-transaktioista**](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

## Mikä on Stonewall x2 -transaktion tarkoitus?

Stonewall x2 -rakenne lisää merkittävän määrän entropiaa transaktioon ja sekoittaa ketjuanalyysiä. Ulkopuolelta katsottuna tällainen transaktio voidaan tulkita pienenä Coinjoinina kahden henkilön välillä. Mutta todellisuudessa se on maksu. Tämä menetelmä luo epävarmuuksia ketjuanalyysiin ja johtaa jopa vääriin johtopäätöksiin.

Palatkaamme esimerkkiin Alicesta, Bobista ja leipurista. Transaktio lohkoketjussa näyttäisi tältä:
![stonewall x2 public](assets/en/3.webp)
Ulkopuolinen tarkkailija, joka nojaa yleisiin ketjuanalyysin heuristiikkoihin, saattaisi virheellisesti päätellä, että "Alice ja Bob suorittivat pienen coinjoinin, jossa kummallakin oli yksi UTXO sisääntulona ja kaksi UTXOa kummallakin lähtönä."![väärinkäsitys stonewall x2](assets/en/4.webp)Tämä tulkinta on väärä, koska kuten tiedät, UTXO lähetettiin Bakerille, Alicella on vain yksi vaihtoraha lähtö, ja Bobilla on kaksi.
![transaktio stonewall x2](assets/en/1.webp)
Vaikka ulkopuolinen tarkkailija onnistuisikin tunnistamaan Stonewall x2 -transaktion kaavan, hänellä ei ole kaikkea tietoa. Hän ei pysty määrittämään, kumpi kahdesta samansuuruisesta UTXOsta vastaa maksua. Lisäksi hän ei voi tietää, oliko maksun suorittaja Alice vai Bob. Lopuksi hän ei pysty määrittämään, tulivatko kaksi sisääntulo-UTXOa kahdelta eri henkilöltä vai kuuluivatko ne yhdelle henkilölle, joka yhdisti ne. Viimeinen kohta johtuu siitä, että klassiset Stonewall-transaktiot, joista yllä keskustelimme, noudattavat täsmälleen samaa kaavaa kuin Stonewall x2 -transaktiot. Ulkopuolelta ja ilman lisätietoja kontekstista on mahdotonta erottaa Stonewall-transaktiota Stonewall x2 -transaktiosta. Kuitenkin edelliset eivät ole yhteistyötransaktioita, kun taas jälkimmäiset ovat. Tämä lisää vielä enemmän epäilyksiä tästä menosta.
![Stonewall vai Stonewall x2 ?](assets/en/5.webp)

## Miten muodostaa yhteys Paynymien välille, jotta voi tehdä yhteistyötä Sorobanin kautta?

Kuten muidenkin Samourain (*Cahoots*) yhteistyötransaktioiden kohdalla, Stonewall x2:n suorittaminen edellyttää osittain allekirjoitettujen transaktioiden vaihtoa lähettäjän ja yhteistyökumppanin välillä. Tämä vaihto voidaan tehdä manuaalisesti, jos olet fyysisesti yhteistyökumppanisi kanssa, tai automaattisesti Soroban-viestintäprotokollan kautta.

Jos valitset jälkimmäisen vaihtoehdon, sinun on muodostettava yhteys Paynymien välille ennen kuin voit suorittaa Stonewall x2:n. Tätä varten Paynymisi on "seurattava" yhteistyökumppanisi Paynymiä, ja päinvastoin.

**Pääsy yhteistyökumppanin Paynymiin:**

Aloittaaksesi, on tarpeen saada yhteistyökumppanisi Paynymin maksukoodi. Samourai Wallet -sovelluksessa yhteistyökumppanisi tulee painaa heidän Paynyminsa kuvaketta (pieni robotti), joka sijaitsee näytön vasemmassa yläkulmassa, sitten klikata heidän Paynym-lempinimeään, joka alkaa `+...`. Esimerkiksi minun on `+namelessmode0aF`.

![samourai paynym](assets/notext/6.webp)
Jos yhteistyökumppanisi käyttää Sparrow Walletia, hänen tulisi klikata 'Tools'-välilehteä, sitten 'Show PayNym'.![paynym sparrow](assets/notext/7.webp)
**Seuraamassa yhteistyökumppanisi PayNymiä Samourai Walletista:**

Jos käytät Samourai Walletia, käynnistä sovellus ja pääse 'PayNyms'-valikkoon samalla tavalla. Jos käytät PayNymiäsi ensimmäistä kertaa, sinun on saatava sen tunniste.

![pyyntö paynym samourai](assets/notext/8.webp)

Sitten klikkaa sinistä '+'-merkkiä näytön oikeassa alakulmassa.
![lisää yhteistyökumppani paynym](assets/notext/9.webp)
Voit sen jälkeen liittää yhteistyökumppanisi maksukoodin valitsemalla 'PASTE PAYMENT CODE', tai avata kameran skannataksesi heidän QR-koodinsa painamalla 'SCAN QR CODE'.
![liitä paynym-tunniste](assets/notext/10.webp)
Klikkaa 'SEURAA' -painiketta.
![seuraa paynymia](assets/notext/11.webp)
Vahvista klikkaamalla 'KYLLÄ'.
![vahvista seuraaminen paynym](assets/notext/12.webp)
Ohjelmisto tarjoaa sinulle sen jälkeen 'YHDISTÄ' -painiketta. Tämän painikkeen klikkaaminen ei ole tarpeellista tässä oppaassa. Tämä vaihe on tarpeellinen vain, jos aiot tehdä maksuja toiselle PayNymille osana BIP47, mikä ei liity tähän oppaaseen.
![yhdistä paynym](assets/notext/13.webp)
Kun PayNymisi seuraa yhteistyökumppanisi PayNymia, toista tämä prosessi päinvastaisessa järjestyksessä, jotta yhteistyökumppanisi voi myös seurata sinua. Sen jälkeen voitte suorittaa Stonewall x2 -siirron.

**Seuraa yhteistyökumppanisi PayNymia Sparrow Walletissa:**

Jos käytät Sparrow Walletia, avaa lompakkosi ja siirry 'Näytä PayNym' -valikkoon. Jos käytät PayNymiasi ensimmäistä kertaa, sinun on hankittava tunniste klikkaamalla 'Hae PayNym'.
![pyydä paynym sparrow](assets/notext/14.webp)
Syötä sen jälkeen yhteistyökumppanisi PayNym-tunniste (joko heidän lempinimensä '+...' tai heidän maksukoodinsa 'PM...') 'Etsi Yhteystieto' -kenttään ja klikkaa 'Lisää Yhteystieto' -painiketta.
![lisää yhteystieto paynym](assets/notext/15.webp)
Ohjelmisto tarjoaa sinulle sen jälkeen 'Linkitä Yhteystieto' -painiketta. Tämän painikkeen klikkaaminen ei ole tarpeellista tässä oppaassa. Tämä vaihe on tarpeellinen vain, jos aiot tehdä maksuja ilmoitetulle PayNymille osana BIP47, mikä ei liity tähän oppaaseen.

Kun PayNymisi seuraa yhteistyökumppanisi PayNymia, toista tämä prosessi päinvastaisessa järjestyksessä, jotta yhteistyökumppanisi voi myös seurata sinua. Sen jälkeen voitte suorittaa Stonewall x2 -siirron.
## Kuinka tehdä Stonewall x2 -siirto Samourai Walletissa?

Jos olet suorittanut edelliset vaiheet Paynymien yhdistämiseksi, olet viimein valmis tekemään Stonewall x2 -siirron! Noudata tätä varten videomme ohjeita Samourai Walletissa:
![Stonewall x2 -opas - Samourai Wallet](https://youtu.be/89oYE1Hw3Fk?si=QTqUZ6IypiR6PPMr)

## Kuinka tehdä Stonewall x2 -siirto Sparrow Walletissa?

Jos olet suorittanut edelliset vaiheet Paynymien yhdistämiseksi, olet viimein valmis tekemään Stonewall x2 -siirron! Noudata tätä varten videomme ohjeita Sparrow Walletissa:
![Stonewall x2 -opas - Sparrow Wallet](https://youtu.be/mO3Xpp34Hhk?si=bfYiTl0Gxjs9sNQq)

**Ulkoiset resurssit:**
- https://sparrowwallet.com/docs/spending-privately.html;
- https://docs.samourai.io/en/spend-tools#stonewallx2.