---
name: Payjoin
description: Mikä on Payjoin Bitcoinissa?
---
![Payjoin-esikatselukuva - steganografia](assets/cover.webp)

***HUOMIO:** Samourai Walletin perustajien pidätyksen ja heidän palvelimiensa takavarikoinnin jälkeen 24. huhtikuuta, Payjoins Stowaway Samourai Walletissa toimii vain, kun PSBT:t vaihdetaan manuaalisesti asianomaisten osapuolten välillä, edellyttäen, että molemmat käyttäjät ovat yhteydessä omaan Dojoonsa. Sparrowin osalta Payjoins BIP78:n kautta toimivat edelleen. On kuitenkin mahdollista, että nämä työkalut käynnistetään uudelleen tulevien viikkojen aikana. Sillä välin voit lukea tämän artikkelin ymmärtääksesi payjoinien teoreettisen toiminnan.*

_Seuraamme tiiviisti tämän tapauksen kehitystä sekä siihen liittyvien työkalujen kehitystä. Voit olla varma, että päivitämme tämän oppaan, kun uutta tietoa tulee saataville._

_Tämä opas on tarkoitettu vain koulutus- ja tiedotustarkoituksiin. Emme kannusta tai hyväksy näiden työkalujen käyttöä rikollisiin tarkoituksiin. Jokaisen käyttäjän on noudatettava oman lainkäyttöalueensa lakeja._

---
## Payjoin-transaktioiden ymmärtäminen Bitcoinissa

Payjoin on erityinen Bitcoin-transaktiorakenne, joka parantaa käyttäjän yksityisyyttä maksun aikana yhteistyössä maksun vastaanottajan kanssa.

Vuonna 2015 [LaurentMT](https://twitter.com/LaurentMT) mainitsi ensimmäisen kerran tämän menetelmän "steganografisina transaktioina" dokumentissa, joka on saatavilla [täällä](https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt). Myöhemmin Samourai Wallet otti tämän tekniikan käyttöön ja tuli ensimmäiseksi asiakkaaksi, joka toteutti sen Stowaway-työkalulla vuonna 2018. Payjoin-konsepti löytyy myös [BIP79](https://github.com/bitcoin/bips/blob/master/bip-0079.mediawiki) ja [BIP78](https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki) -ehdotuksista. Payjoiniin viitataan useilla termeillä:
- Payjoin
- Stowaway
- P2EP (Pay-to-End-Point)
- Steganografinen transaktio

Payjoinin ainutlaatuisuus piilee sen kyvyssä luoda transaktio, joka ensi silmäyksellä vaikuttaa tavalliselta, mutta on itse asiassa mini Coinjoin kahden osapuolen välillä. Tämän saavuttamiseksi transaktiorakenne sisältää maksun vastaanottajan mukana tulevat syötteet itse lähettäjän lisäksi. Vastaanottaja sisällyttää maksun itselleen transaktion keskelle, mikä mahdollistaa heidän maksamisensa.

Otetaan konkreettinen esimerkki: jos ostat patongin `4000 satoshilla` käyttäen UTXO:a, joka on `10 000 satoshia` ja valitset Payjoinin, leipurisi lisää `15 000 satoshin` UTXO:n, joka kuuluu heille syötteenä, jonka he saavat kokonaisuudessaan ulostulona, lisäksi sinun `4000 satoshiasi`:
![Payjoin-transaktiokaavio](assets/en/1.webp)

Tässä esimerkissä leipuri tuo `15 000 satoshia` syötteenä ja lähtee `19 000 satoshilla`, erotuksena tasan `4000 satoshia`, mikä on patongin hinta. Sinun puoleltasi tulet `10 000 satoshilla` ja päädyt `6 000 satoshin` ulostulona, mikä edustaa `-4000 satoshin` tasapainoa, eli patongin hintaa. Yksinkertaistaakseni esimerkkiä, jätin tarkoituksella louhintamaksut pois tästä transaktiosta.
## Mikä on Payjoin-tapahtuman tarkoitus?
Payjoin-tapahtuma palvelee kahta tavoitetta, jotka mahdollistavat käyttäjien maksujen yksityisyyden parantamisen.
Ensinnäkin, Payjoin pyrkii harhauttamaan ulkopuolista tarkkailijaa luomalla väärän jäljen ketjuanalyysiin. Tämä on mahdollista Common Input Ownership Heuristic (CIOH) -periaatteen avulla. Yleensä, kun lohkoketjussa olevalla tapahtumalla on useita syötteitä, oletetaan, että kaikki nämä syötteet kuuluvat todennäköisesti samalle entiteetille tai käyttäjälle. Näin ollen, kun analyytikko tutkii Payjoin-tapahtumaa, hänet johdetaan uskomaan, että kaikki syötteet ovat saman henkilön. Tämä käsitys on kuitenkin väärä, koska maksun vastaanottaja myös lisää syötteitä yhdessä varsinaisen maksajan kanssa. Siksi ketjuanalyysi ohjautuu tulkintaan, joka osoittautuu vääräksi.

Lisäksi Payjoin mahdollistaa myös ulkopuolisen tarkkailijan harhauttamisen maksun todellisesta määrästä. Tapahtuman rakennetta tutkiessa analyytikko saattaa uskoa, että maksu vastaa yhden ulostulon määrää. Todellisuudessa maksun määrä ei kuitenkaan vastaa mitään ulostuloista. Se on itse asiassa ero vastaanottajan ulostulo-UTXO:n ja vastaanottajan sisääntulo-UTXO:n välillä. Tässä mielessä Payjoin-tapahtuma kuuluu steganografian alueelle. Se mahdollistaa todellisen tapahtuman määrän piilottamisen väärennetyn tapahtuman sisään, joka toimii harhautuksena.

> Steganografia on tekniikka, jolla tietoa piilotetaan muiden tietojen tai esineiden sisään siten, että piilotetun tiedon läsnäolo ei ole havaittavissa. Esimerkiksi salainen viesti voidaan piilottaa tekstin pisteen sisään, jolla ei ole mitään tekemistä sen kanssa, tehden siitä havaitsemattoman paljaalla silmällä (tämä on mikropistetekniikan menetelmä). Toisin kuin salaus, joka tekee tiedosta käsittämättömän ilman purkuavainta, steganografia ei muuta tietoa. Se pysyy näkyvissä avoimesti. Sen tavoitteena on pikemminkin piilottaa salaisen viestin olemassaolo, kun taas salaus selvästi paljastaa piilotetun tiedon läsnäolon, vaikkakin saavuttamattomissa ilman avainta.

Palataan esimerkkiimme Payjoin-tapahtumasta patongin maksamiseksi.
![Payjoin-tapahtuman kaavio ulkopuolelta](assets/en/2.webp)
Tätä tapahtumaa lohkoketjussa nähdessään ulkopuolinen tarkkailija, joka noudattaa ketjuanalyysin tavanomaisia heuristiikkoja, tulkitsee sen seuraavasti: "*Alice yhdisti 2 UTXO:a syötteiksi tapahtumaan maksaa `19,000 sats` Bobille*."
![Väärä tulkinta Payjoin-tapahtumasta ulkopuolelta](assets/en/3.webp)
Tämä tulkinta on ilmeisen väärä, koska, kuten jo tiedät, kaksi syöttö-UTXO:a eivät kuulu samalle henkilölle. Lisäksi maksun todellinen arvo ei ole `19,000 sats`, vaan pikemminkin `4,000 sats`. Ulkopuolisen tarkkailijan analyysi ohjataan siis virheelliseen johtopäätökseen, varmistaen sidosryhmien luottamuksellisuuden säilymisen.![payjoin-tapahtuman kaavio](assets/en/1.webp)
Jos haluat analysoida todellisen Payjoin-tapahtuman, tässä on yksi, jonka suoritin testnetissä: [8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c](https://mempool.space/fr/testnet/tx/8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c)
[**-> Tutustu oppaaseemme, kuinka tehdä Payjoin Samourai Walletilla**](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)  
[**-> Tutustu oppaaseemme, kuinka tehdä Payjoin Sparrow Walletilla**](https://planb.network/tutorials/privacy/on-chain/payjoin-sparrow-wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62)

**Ulkopuoliset resurssit:**
- https://docs.samourai.io/en/spend-tools#stowaway;
- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt;
- https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki.