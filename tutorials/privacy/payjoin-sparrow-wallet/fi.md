---
name: Payjoin - Sparrow Wallet
description: Miten tehdään Payjoin-siirto Sparrow Walletissa?
---
![opetusohjelman kansi kuva sparrow payjoin](assets/cover.webp)

***HUOMIO:** Samourai Walletin perustajien pidätyksen ja heidän palvelimiensa takavarikoinnin jälkeen 24. huhtikuuta, Payjoins Stowaway Samourai Walletissa toimii nyt vain manuaalisesti vaihtamalla PSBT osapuolten välillä, edellyttäen, että molemmat käyttäjät ovat yhteydessä omaan Dojoonsa. Sparrow'n osalta Payjoins BIP78 kautta toimivat edelleen. On kuitenkin mahdollista, että nämä työkalut käynnistetään uudelleen tulevina viikkoina. Sillä välin voit aina lukea tämän artikkelin ymmärtääksesi payjoinsin teoreettisen toiminnan.*

_Seuraamme tiiviisti tämän tapauksen kehitystä sekä siihen liittyvien työkalujen kehitystä. Voit olla varma, että päivitämme tämän opetusohjelman, kun uutta tietoa tulee saataville._

_Tämä opetusohjelma on tarkoitettu vain koulutus- ja tiedotustarkoituksiin. Emme kannusta tai hyväksy näiden työkalujen käyttöä rikollisiin tarkoituksiin. Jokaisen käyttäjän on noudatettava oman lainkäyttöalueensa lakeja._

---

> *"Pakota lohkoketjun vakoilijat miettimään uudelleen kaikkea mitä he luulevat tietävänsä."*

Payjoin on tietty Bitcoin-siirtorakenne, joka parantaa käyttäjän yksityisyyttä maksamisen yhteydessä yhteistyössä maksun vastaanottajan kanssa. On olemassa useita toteutuksia, jotka helpottavat PayJoinin asettamista ja automatisointia. Näiden toteutusten joukossa tunnetuin on Samourai Wallet -tiimin kehittämä Stowaway. Tämä opetusohjelma pyrkii opastamaan sinut Stowaway Payjoin -siirron tekemisessä käyttäen Sparrow Wallet -ohjelmistoa.

## Miten Stowaway toimii?

Kuten aiemmin mainittiin, Samourai Wallet tarjoaa PayJoin-työkalun nimeltä "Stowaway". Se on käytettävissä Sparrow Wallet -ohjelmistossa PC:llä tai Samourai Wallet -sovelluksessa Androidilla. Payjoinin suorittamiseksi vastaanottajan, joka toimii myös yhteistyökumppanina, on käytettävä Stowawayn kanssa yhteensopivaa ohjelmistoa, nimittäin Sparrow'ta tai Samourai Walletia. Nämä kaksi ohjelmistoa ovat yhteensopivia, mahdollistaen Stowaway-siirrot Sparrow-lompakon ja Samourai-lompakon välillä, ja päinvastoin.

Stowaway perustuu transaktiotyyppiin, jota Samourai kutsuu nimellä "Cahoots". Cahoot on käytännössä yhteistyössä tehty siirto useiden käyttäjien kesken, joka vaatii off-chain tietojenvaihtoa. Tällä hetkellä Samourai tarjoaa kaksi Cahoots-työkalua: Stowaway (Payjoinit) ja StonewallX2 (josta kerromme tulevassa artikkelissa).

Cahoots-siirrot sisältävät osittain allekirjoitettujen siirtojen vaihtamisen käyttäjien kesken. Tämä prosessi voi olla pitkä ja hankala, erityisesti kun se tehdään etänä. Se voidaan kuitenkin tehdä manuaalisesti toisen käyttäjän kanssa, mikä voi olla kätevää, jos yhteistyökumppanit ovat fyysisesti lähellä. Käytännössä tämä tarkoittaa viiden QR-koodin manuaalista vaihtamista, jotka on skannattava peräkkäin.

Etänä tehtynä tämä prosessi muuttuu liian monimutkaiseksi. Tämän ongelman ratkaisemiseksi Samourai on kehittänyt salatun viestintäprotokollan, joka perustuu Toriin, nimeltään "Soroban". Sorobanin avulla Payjoinin tarvittavat vaihdot automatisoidaan käyttäjäystävällisen käyttöliittymän taakse. Tämä on toinen menetelmä, jota tarkastelemme tässä artikkelissa.

Nämä salatut vaihdot vaativat yhteyden ja autentikoinnin perustamisen Cahoots-osallistujien välille. Soroban-viestintä perustuu käyttäjien Paynymsiin. Jos et ole tuttu Paynymsien kanssa, suosittelen tutustumaan tähän artikkeliin saadaksesi lisätietoja: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)
Yksinkertaisesti sanottuna Paynym on uniikki tunniste, joka on linkitetty lompakkoosi ja mahdollistaa erilaisia toimintoja, mukaan lukien salatun viestinnän. Paynym esitetään tunnisteen ja robotin kuvaa esittävän kuvituksen muodossa. Tässä on esimerkki omastani Testnetissä: ![Paynym Sparrow](assets/en/1.webp)
**Yhteenvetona:**
- *Payjoin* = Erityinen yhteistyöllisen siirron rakenne;
- *Stowaway* = Payjoin-toteutus, joka on saatavilla Samourai- ja Sparrow-lompakoissa;
- *Cahoots* = Nimi, jonka Samourai on antanut kaikille heidän yhteistyöllisten siirtojensa tyypeille, mukaan lukien Payjoin Stowaway;
- *Soroban* = Tor-verkossa perustettu salattu viestintäprotokolla, joka mahdollistaa yhteistyön muiden käyttäjien kanssa Cahoots-siirron yhteydessä.
- *Paynym* = Lompakon uniikki tunniste, joka mahdollistaa viestinnän toisen käyttäjän kanssa Sorobanissa, jotta voidaan suorittaa Cahoots-siirto.

[**-> Lisätietoja Payjoin-siirroista ja niiden hyödyistä**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)

## Miten muodostetaan yhteys Paynymien välille?

Kaukaisen Cahoots-siirron suorittamiseksi, erityisesti PayJoin (Stowaway) Samourain tai Sparrow'n kautta, on tarpeen "Seurata" käyttäjää, jonka kanssa aiot tehdä yhteistyötä, käyttämällä heidän Paynymiaan. Stowawayn tapauksessa tämä tarkoittaa henkilön seuraamista, jolle haluat lähettää bitcoineja.

**Tässä on menettely tämän yhteyden muodostamiseksi:**

Ensimmäiseksi sinun on saatava vastaanottajan Paynym-tunniste. Tämä voidaan tehdä käyttämällä heidän lempinimeään tai maksukoodiaan. Tee tämä valitsemalla vastaanottajan Sparrow-lompakosta `Tools`-välilehti ja sitten klikkaamalla `Show PayNym`.
![Show Paynym](assets/notext/2.webp)
![Paynym Sparrow](assets/en/1.webp)
Omalta osaltasi, avaa Sparrow-lompakkosi ja pääse samaan `Show PayNym`-valikkoon. Jos käytät Paynymiasi ensimmäistä kertaa, sinun on saatava tunniste klikkaamalla `Retrieve PayNym`.
![Retrieve paynym](assets/notext/3.webp)
Seuraavaksi, syötä yhteistyökumppanisi Paynym-tunniste (joko heidän lempinimensä `+...` tai heidän maksukoodinsa `PM...`) `Find Contact`-laatikkoon, ja sitten klikkaa `Add Contact`-painiketta.
![add contact](assets/notext/4.webp)
Ohjelmisto tarjoaa sinulle sitten `Link Contact`-painiketta. Tämän painikkeen klikkaaminen ei ole tarpeellista tässä oppaassa. Tämä vaihe on tarpeellinen vain, jos aiot tehdä maksuja Paynymille BIP47 yhteydessä, mikä ei liity tähän oppaaseen.

Kun vastaanottajan Paynym on seurannut Paynymiasi, toista tämä toimenpide toisinpäin, jotta vastaanottajasi seuraa sinua myös. Sen jälkeen voit suorittaa Payjoin-siirron.

## Miten suoritetaan Payjoin Sparrow-lompakossa?
Jos olet suorittanut nämä alustavat vaiheet, olet viimein valmis suorittamaan Payjoin-siirron! Tee tämä seuraamalla videomme ohjeita:
![Payjoin Tutorial - Sparrow Wallet](https://youtu.be/ZQxKod3e0Mg)

**Ulkoiset resurssit:**
- https://docs.samourai.io/en/spend-tools#stowaway ;
- https://sparrowwallet.com/docs/spending-privately.html.