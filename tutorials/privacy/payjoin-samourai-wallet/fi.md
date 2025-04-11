---
name: Payjoin - Samourai Wallet
description: Kuinka suorittaa Payjoin-maksutapahtuma Samourai Walletissa?
---
![samourai payjoin cover](assets/cover.webp)

***HUOMIO:** Samourai Walletin perustajien pidätyksen ja heidän palvelimiensa takavarikoinnin jälkeen 24. huhtikuuta, Payjoins Stowaway Samourai Walletissa toimii vain, kun PSBT:t vaihdetaan manuaalisesti asianomaisten osapuolten välillä, edellyttäen, että molemmat käyttäjät ovat yhteydessä omaan Dojoonsa. Sparrowin osalta Payjoins BIP78:n kautta toimivat edelleen. On kuitenkin mahdollista, että nämä työkalut käynnistetään uudelleen tulevien viikkojen aikana. Sillä välin voit lukea tämän artikkelin ymmärtääksesi Stowawayn teoreettisen toiminnan.*

_Jos aiot suorittaa Stowawayn manuaalisesti, menettely on hyvin samankaltainen kuin tässä oppaassa kuvattu. Pääero on Stowaway-maksutapahtuman tyypin valinnassa: sen sijaan, että valitsisit `Online`, klikkaa `In Person / Manual`. Sen jälkeen sinun tulee manuaalisesti vaihtaa PSBT-tiedostot Stowaway-maksutapahtuman rakentamiseksi. Jos olet fyysisesti lähellä yhteistyökumppaniasi, voit skannata QR-koodeja peräkkäin. Jos olet etäällä, JSON-tiedostoja voidaan vaihtaa turvallisen viestintäkanavan kautta. Loput oppaasta pysyvät muuttumattomina._

_Seuraamme tiiviisti tämän tapauksen kehitystä sekä siihen liittyvien työkalujen kehitystä. Voit olla varma, että päivitämme tämän oppaan uusien tietojen saataville tullessa._

_Tämä opas on tarkoitettu vain koulutus- ja tiedotustarkoituksiin. Emme kannusta tai hyväksy näiden työkalujen käyttöä rikollisiin tarkoituksiin. Jokaisen käyttäjän on noudatettava oman lainkäyttöalueensa lakeja._

---

> *"Pakota lohkoketjun vakoilijat miettimään uudelleen kaikkea, mitä he luulevat tietävänsä."*

Payjoin on tietty Bitcoin-maksutapahtuman rakenne, joka parantaa käyttäjän yksityisyyttä maksun aikana yhteistyössä maksun vastaanottajan kanssa. On olemassa useita toteutuksia, jotka helpottavat PayJoinin asennusta ja automatisointia. Näiden toteutusten joukossa tunnetuin on Stowaway, jonka Samourai Walletin tiimit ovat kehittäneet. Tämä opas selittää, kuinka suorittaa Stowaway Payjoin -maksutapahtuma käyttäen Samourai Wallet -sovellusta.

## Kuinka Stowaway toimii?

Kuten aiemmin mainittiin, Samourai Wallet tarjoaa PayJoin-työkalun nimeltä "Stowaway". Se on käytettävissä Sparrow Wallet -ohjelmiston kautta PC:llä tai Samourai Wallet -sovelluksen kautta Androidilla. Payjoinin suorittamiseksi vastaanottajan, joka toimii myös yhteistyökumppanina, on käytettävä Stowawayn kanssa yhteensopivaa ohjelmistoa, nimittäin Sparrow'ta tai Samouraita. Nämä kaksi ohjelmistoa ovat yhteensopivia, mahdollistaen Stowaway-maksutapahtuman Sparrow-lompakon ja Samourai-lompakon välillä, ja päinvastoin.

Stowaway perustuu transaktiotyyppiin, jota Samourai kutsuu "Cahootsiksi". Cahoot on olennaisesti yhteistyössä useiden käyttäjien välillä tapahtuva transaktio, joka vaatii off-chain-tietojen vaihtoa. Tähän mennessä Samourai tarjoaa kaksi Cahoots-työkalua: Stowaway (Payjoins) ja StonewallX2 (josta kerromme tulevassa artikkelissa).

Cahoots-maksutapahtumat sisältävät osittain allekirjoitettujen transaktioiden vaihtoja käyttäjien välillä. Tämä prosessi voi olla pitkä ja hankala, erityisesti kun se tehdään etänä. Se voidaan kuitenkin silti suorittaa manuaalisesti toisen käyttäjän kanssa, mikä voi olla kätevää, jos yhteistyökumppanit ovat fyysisesti lähellä. Käytännössä tämä tarkoittaa viiden QR-koodin manuaalista vaihtoa, jotka skannataan peräkkäin.

Kun tämä prosessi tehdään etänä, se muuttuu liian monimutkaiseksi. Tämän ongelman ratkaisemiseksi Samourai on kehittänyt Toriin perustuvan salatun viestintäprotokollan, nimeltään "Soroban". Sorobanin avulla Payjoinin vaatimat vaihdot automatisoidaan käyttäjäystävällisen käyttöliittymän taakse. Tämä on toinen menetelmä, jota tutkimme tässä artikkelissa.
Nämä salatut vaihdot vaativat yhteyden ja autentikoinnin luomisen Cahoots-osallistujien välille. Soroban-viestintä perustuu siis käyttäjien Paynym-tunnisteisiin. Jos et ole tuttu Paynymien kanssa, suosittelen tutustumaan tähän artikkeliin saadaksesi lisätietoja: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)

 Yksinkertaistaen, Paynym on uniikki tunniste, joka on linkitetty lompakkoosi ja mahdollistaa useita toimintoja, mukaan lukien salatun viestinnän. Paynym esitetään tunnisteen ja robotin kuvaa esittävän kuvituksen muodossa. Tässä on esimerkki omastani Testnetissä: ![paynym samourai wallet](assets/en/1.webp)

**Yhteenvetona:**
- _Payjoin_ = Yhteistyöllisten transaktioiden tietty rakenne;
- _Stowaway_ = Payjoin-toteutus, joka on saatavilla Samourai ja Sparrow Wallet -lompakoissa;
- _Cahoots_ = Nimi, jonka Samourai on antanut kaikille heidän yhteistyöllisten transaktioidensa tyypeille, mukaan lukien Payjoin Stowaway;
- _Soroban_ = Salattu viestintäprotokolla, joka on perustettu Tor-verkkoon, mahdollistaen yhteistyön muiden käyttäjien kanssa Cahoots-transaktion yhteydessä;
- _Paynym_ = Lompakon uniikki tunniste, joka mahdollistaa viestinnän toisen käyttäjän kanssa Sorobanissa, Cahoots-transaktion suorittamiseksi.

[**-> Lue lisää Payjoin-transaktioista ja niiden hyödyistä**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)

## Miten yhteys Paynymien välille luodaan?

Kaukaisen Cahoots-transaktion, erityisesti PayJoinin (Stowaway) suorittamiseksi Samourain kautta, on tarpeen "Seurata" käyttäjää, jonka kanssa aiot tehdä yhteistyötä, käyttäen heidän Paynymiaan. Stowawayn tapauksessa tämä tarkoittaa henkilön seuraamista, jolle haluat lähettää bitcoineja.

**Tässä on menettely yhteyden luomiseksi:**

Aloittaaksesi, sinun on saatava vastaanottajan Paynymin maksukoodi Payjoinia varten. Samourai Wallet -sovelluksessa vastaanottajan on napautettava heidän Paynym-kuvakettaan (pieni robotti) näytön vasemmassa yläkulmassa ja sitten klikattava heidän Paynym-lempinimeään, joka alkaa `+...`. Esimerkiksi omani on `+namelessmode0aF`. Jos yhteistyökumppanisi käyttää Sparrow Walletia, suosittelen tutustumaan omistettuun opastukseemme klikkaamalla tästä.

![connexion paynym samourai](assets/notext/2.webp)

Yhteistyökumppanisi ohjataan sitten heidän Paynym-sivulleen. Sieltä he voivat joko jakaa Paynym-tietonsa kanssasi tai jakaa QR-koodinsa, jonka voit skannata. Tämän tekemiseksi heidän on klikattava pientä "jaa" -kuvaketta näytön oikeassa yläkulmassa.
![partager paynym samourai](assets/en/1.webp)

Omalta osaltasi, käynnistä Samourai Wallet -sovelluksesi ja siirry "PayNyms"-valikkoon samalla tavalla. Jos käytät Paynymiasi ensimmäistä kertaa, sinun on hankittava tunniste.

![demander un paynym](assets/notext/3.webp)

Sen jälkeen klikkaa sinistä "+" -painiketta näytön oikeassa alakulmassa.
![ajouter paynym collaborateur](assets/notext/4.webp)
Voit sitten liittää yhteistyökumppanisi maksukoodin valitsemalla `COLLER LE CODE PAIEMENT`, tai avata kameran skannataksesi heidän QR-koodinsa painamalla `SCANNEZ LE CODE QR`.![paste paynym identifier](assets/notext/5.webp)

Klikkaa `SUIVRE`-painiketta.
![seuraa paynymiä](assets/notext/6.webp)Vahvista klikkaamalla `KYLLÄ`.
![vahvista seuraaminen paynym](assets/notext/7.webp)
Tämän jälkeen ohjelmisto tarjoaa sinulle `SE CONNECTER` -painiketta. Tämän painikkeen klikkaaminen ei ole tarpeellista tässä oppaassa. Tämä vaihe on tarpeen vain, jos aiot tehdä maksuja toiselle Paynymille osana BIP47, mikä ei liity oppaaseemme.
![yhdistä paynym](assets/notext/8.webp)
Kun vastaanottajan Paynym on seurannut omaa Paynymiäsi, toista tämä toimenpide toisinpäin, jotta vastaanottaja myös seuraa sinua. Sen jälkeen voit suorittaa Payjoinin.

## Miten suorittaa Payjoin Samourai Walletissa?

Jos olet suorittanut nämä alustavat vaiheet, olet viimein valmis suorittamaan Payjoin-tapahtuman! Tee tämä seuraamalla videotutoriaaliamme:

![Payjoin Video Tutorial - Samourai Wallet](https://youtu.be/FXW6XZim0ww?si=EXalYwK1t9DT48aE)

**Ulkopuoliset resurssit:**
- https://docs.samourai.io/en/spend-tools#stowaway.