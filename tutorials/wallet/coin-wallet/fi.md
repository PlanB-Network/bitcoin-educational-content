---
name: Coin Wallet
description: Coin Wallet:ta ja tapoja parantaa yksityisyyden suojaa ja turvallisuutta koskeva opetusohjelma
---

![cover](assets/cover.webp)


Tämä opetusohjelma käsittelee [Coin Wallet](https://coin.space/) - itsesäätelevää wallet-salausta mobiililaitteille ja sitä, miten turvallisuutta ja yksityisyyttä voidaan lisätä wallet-sovelluksia käytettäessä.



## Coin Wallet


**Coin Wallet** on Bitcoin-harrastajien vuonna 2015 luoma wallet, joka on avoimen lähdekoodin wallet, joka on itseohjautuva / ei-ohjautuva. Se aloitti verkkosovelluksena, jota seurasi iOS-sovellus vuonna 2017 ja Android-sovellus vuonna 2020 - saatavilla Google Play, Samsung Galaxy Store ja Huawei AppGallery.


Tärkeimmät edut:


- Muiden kuin huoltajien arkkitehtuuri
- Täysin [avoimen lähdekoodin koodi](https://github.com/CoinSpace/CoinSpace/blob/master/LICENSE)
- Yksinkertainen ja siisti muotoilu
- Keskittyy ydintarkoitukseen - kryptovaluutan turvalliseen tallentamiseen ilman turhia ominaisuuksia
- Ristikkäisten alustojen tuki: mobiili (iOS ja Android), työpöytä, web
- RBF (Replace-By-Fee) -tuki - nopeuta jumissa olevia tapahtumia milloin tahansa
- Laitteiston 2FA [YubiKey](https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/) / FIDO2-avaimella
- Sisäänrakennettu Tor-tuki - reititä kaikki liikenne Tor-verkon kautta maksimaalisen yksityisyyden varmistamiseksi



## 1️⃣ Asennus Coin Wallet

Coin Wallet on saatavilla kaikilla yleisimmillä alustoilla.



- [iOS App Store](https://apps.apple.com/app/coin-wallet-bitcoin-crypto/id980719434)



- [Android Google Play](https://play.google.com/store/apps/details?id=com.coinspace.app)



- [Android (Galaxy Store)](https://galaxystore.samsung.com/detail/com.coinspace.app)



- [Android (Huawei AppGallery)](https://appgallery.huawei.com/app/C112183767)



- [Android (Uptodown)](https://coin-wallet.en.uptodown.com/android)



- [Android APK](https://coin.space/api/v3/download/android-apk/any)



- [Kaikki julkaisulinkit](https://github.com/CoinSpace/CoinSpace/releases)


Saatavilla myös työpöydälle (Windows, Linux, macOS), verkkosovelluksena ja Torin kautta.


![image](assets/en/01.webp)


## 2️⃣ Wallet:n luominen ja PIN-koodin asettaminen


wallet luodaan käyttämällä passphrase:a - satunnaista 12 sanan sarjaa, jotka on erotettu välilyönneillä ja luotu [2048 sanan luettelosta](https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts).

Coin Wallet tukee 12-, 15-, 18-, 21- tai 24-sanaisia salasanoja, jotka tuodaan muista lompakoista.


passphrase on yksityisen pääavaimen ihmisen luettavissa oleva muoto. Se on tallennettava turvallisesti. passphrase on ainoa, mitä tarvitaan wallet:n käyttämiseen tai palauttamiseen. Jos passphrase menetetään, wallet ja kaikki varat menetetään pysyvästi. passphrase:ää ei saa koskaan jakaa. Coin Wallet ei tallenna avaimia mihinkään palvelimeen tai tietokantaan.


**Onko 12-sanainen passphrase turvallinen?**

Kun sanoja on 2048 per asema, on olemassa 2048¹² ≈ 10³⁹ yhdistelmää, mikä tarjoaa ~128 bitin tietoturvan, joka on verrattavissa Bitcoin:n yksityisiin avaimiin. Tätä tasoa pidetään yleisesti riittävänä.


![image](assets/en/02.webp)


Kun passphrase on kirjoitettu ylös ja vahvistettu, sovellus pyytää asettamaan **nelinumeroisen PIN-koodin** päivittäistä käyttöä varten. Lisämukavuuden lisäämiseksi voit ottaa käyttöön biometrisen todennuksen (sormenjälki- tai kasvojentunnistus) PIN-koodin käytön sijaan.


![image](assets/en/03.webp)



Ei ole tiliä, ei avaimen palautusta, ei passphrase:n nollausta eikä tapahtumien peruuttamista. Turvallisuus on täysin käyttäjän vastuulla.


Yksityiskohtaiset parhaat käytännöt muistilausekkeen tallentamiseen:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣ Salasana + PIN-koodi. Milloin ja miten niitä käytetään


**Milloin passphrase tarvitaan?**

Vain näissä harvoissa tapauksissa:


- wallet:n määrittäminen uuteen laitteeseen
- Coin Wallet -sovelluksen asentaminen uudelleen
- Sovelluksen/selaimen tietojen tyhjentäminen (paikallinen tallennus)
- Laiteavaimen poistaminen tililtä
- Väärän PIN-koodin syöttäminen kolme kertaa (sovellus lukitsee sovelluksen turvallisuuden vuoksi)


Jokapäiväisessä käytössä 4-numeroinen PIN-koodi riittää wallet:n lukituksen avaamiseen.


**Salasana + PIN-koodi: miten se toimii**

passphrase on todellinen yksityinen pääavain, ja se toimii millä tahansa laitteella.

Koska 12-24 sanan kirjoittaminen joka kerta olisi hankalaa, Coin Wallet käyttää nelinumeroista PIN-koodia nopeaa, jokapäiväistä käyttöä varten nykyisellä laitteella.

Pelkkä PIN-koodi ei ole riittävän turvallinen suojaamaan suoraan pääavainta, joten sitä ei koskaan käytetä salaukseen. Sen sijaan:



- PIN-koodi lähetetään palvelimelle ja vaihdetaan pitkään salattuun token-koodiin.
- Tämä token purkaa salatun pääavaimen, joka on tallennettu vain laitteeseen.


Jos PIN-koodi kirjoitetaan väärin kolme kertaa, palvelin poistaa token:n pysyvästi. Paikallisesti tallennetusta avaimesta tulee käyttökelvoton, ja ainoa tapa palauttaa wallet on syöttää alkuperäinen passphrase.

Tämä muotoilu tarjoaa sekä mukavuutta että vahvan varasuojauksen.



## 4️⃣ ₿itcoinin vastaanottaminen - Address Tyypit ja yksityisyys


Coin Wallet tukee kaikkia kolmea Bitcoin-osoiteformaattia:



- Native SegWit (Bech32)** - alkaa kirjaimella **bc1q** - alhaisimmat maksut, suositellaan
- Sisäkkäiset SegWit (P2SH)** - alkaa kirjaimella **3**
- Legacy (P2PKH)** - alkaa kirjaimella **1**


![image](assets/en/04.webp)


**Miksi osoite muuttuu jokaisen talletuksen jälkeen?**

Tämä on tarkoituksellista ja suojaa yksityisyyttä. Coin Wallet luo automaattisesti uuden käyttämättömän osoitteen aina, kun kolikoita vastaanotetaan. Jos samaa osoitetta käytettäisiin uudelleen (esimerkiksi kuukausipalkkaa varten), kuka tahansa voisi helposti laskea yhteen kaikki saapuvat transaktiot lohkoketju-selaimella ja tietää kokonaistulot.


Vanhat osoitteet pysyvät voimassa ikuisesti - voit edelleen vastaanottaa niihin - mutta uuden osoitteen käyttäminen joka kerta on suositeltava tietosuojaa koskeva paras käytäntö.


**Miten vastaanottaa Bitcoin:**

1. Avaa kolikko

2. Napauta **vastaanottaa**

3. Valitse haluamasi osoitetyyppi (mieluiten **bc1q** - `Native SegWit`)

4. Näytä QR-koodi tai kopioi osoite ja lähetä se maksajalle


**Vaihtoehtoinen - Mecto (henkilökohtaisia maksuja varten):**

Samassa vastaanottoruudussa on "Mecto"-painike.

Kun kytket sen päälle:


- Sinua pyydetään antamaan **nickname** (gravatar)
- Nykyinen sijaintisi + vastaanotto-osoitteesi jaetaan väliaikaisesti muiden Coin Wallet-käyttäjien kanssa, joilla on myös Mecto käytössä
- He voivat löytää sinut pieneltä kartalta ja lähettää kolikoita ilman kirjoittamista tai skannaamista


Tiedot näkyvät vain muille Mecton käyttäjille, ja ne poistetaan automaattisesti 1 tunnin kuluttua (tai heti, kun sammutat sen).

Mecto on täysin valinnainen - jätä se pois päältä, jos haluat mahdollisimman paljon yksityisyyttä.


![image](assets/en/05.webp)


## 5️⃣ Lähettäminen ₿itcoin


Bitcoin:n lähettäminen:


1. Avaa kolikko → napauta **lähettää**

2. Liitä osoite tai skannaa QR-koodi

3. Syötä summa (tai napauta **Max**)

4. Valitse tapahtuman nopeus:



| Nopeus   | Likimääräinen vahvistusaika | Maksujen taso     |
|---------|---------------------------|---------------|
| **Hidas**    | ~120 minuuttia              | Alin
| **Oletus** | ~60 minuuttia               | Keskitaso
| **Nopea**    | ~20 minuuttia               | Korkeampi

5. Vahvista 4-numeroisella PIN-koodillasi → maksutapahtuma lähetetään


### Kuinka nopeuttaa vireillä olevaa ₿itcoin-tapahtumaa (RBF)


Jos valitsit hitaan maksun ja maksutapahtuma on jumissa:


1. Siirry **Historia**-välilehdelle

2. Napauta vireillä olevaa tapahtumaa

3. Napauta **Kiihdytä** (korvaus maksua vastaan)

4. Vahvista → maksutapahtuma lähetetään uudelleen korkeammalla maksulla


RBF-kiihdytystä tuetaan tällä hetkellä seuraavissa tapauksissa:

Bitcoin - Avalanche - Binance Smart Chain - Ethereum - Ethereum Classic - Polygon


Lisätietoja Replace-by-fee:stä (RBF): https://bitcoinops.org/en/topics/replace-by-fee/


## 6️⃣ Yksityisten avainten vienti


**Milloin yksityistä avainta todella tarvitaan?**

(99 % käyttäjistä ei koskaan tee niin - 12-sanainen passphrase riittää)



| Tilanne                                      | Miksi tarvitset yksityisen avaimen                     |
|------------------------------------------------|--------------------------------------------------|
| Vanhan paperilompakkoon pyyhkiminen                   | Varojen siirtäminen nykyiseen lompakkoosi             |
| Tuonti laitteiston allekirjoittajaan (esim. Coldcard) | Offline-allekirjoitusta varten                              |
| Hätäpalautus (kadonnut siemen, mutta sovellus on vielä auki) | Kolikkotunteita ennen kuin sovellus katoaa           |
| Työkalujen käyttäminen, jotka eivät hyväksy siemenlausekkeita     | Joitakin vain valvonta- tai allekirjoitusapuohjelmat             |

### Yksityisten avainten vienti Coin:ssä Wallet:ssa


1. Avaa **Bitcoin (BTC)**

2. Vieritä sivun alareunaan - napauta **Vie yksityiset avaimet**

3. Sovellus näyttää jokaisen osoitteen saldon + sen yksityisen avaimen **WIF**-muodossa (alkaa 5:llä, K:lla tai L:llä) ja QR-koodin.


Vain ei-tyhjät osoitteet näkyvät.


**Esimerkki WIF-avaimesta**

`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k`


**Mitä tehdä seuraavaksi (suositellaan)**


- Avaa Electrum, Sparrow, BlueWallet tai mikä tahansa laitteisto wallet
- Yksityisen avaimen tuonti/pyyhkäisy
- Kaikki varat siirretään välittömästi uuteen turvalliseen osoitteeseen nykyisen seed:n alle


Älä koskaan säilytä yksityistä avainta digitaalisesti selkokielisenä. Pyyhkimisen jälkeen se voidaan turvallisesti poistaa.


Täydellinen opas yksityisistä avaimista ja derivaatiopoluista: [How to Work with Private Keys: The Ultimate Guide](https://coin.space/how-to-work-with-private-keys-the-ultimate-guide/)



## 7️⃣ Tekniset tiedot - BIP39, BIP32 ja johdannaispolut


Coin Wallet noudattaa tiukasti virallisia Bitcoin-standardeja, joita lähes kaikki vakavasti otettavat lompakot käyttävät.


"BIP39" - miten passphrase:sta tulee yksityinen pääavain


- Sanojen oletusmäärä: 12
- Valinnainen passphrase/salasana: ei mikään ("")
- Alkuperäinen entropia: 128 bittiä (12 sanaa) → 256 bittiä (24 sanaa)
- Avoimen lähdekoodin toteutus: https://github.com/paulmillr/scure-bip39
- Sanaluettelo: 2048 sanan englanninkielinen standardiluettelo
- Tukee 12-, 15-, 18-, 21- ja 24-sanaisen lauseen tuontia mistä tahansa muusta BIP39 wallet:stä


`BIP32 + BIP44/BIP49/BIP84` - kaikkien osoitteiden deterministinen generointi

Yhdestä pääavaimesta wallet voi generate generate miljardeja osoitteita tarkasti määritellyssä järjestyksessä. Tämän vuoksi Electrum:een, Sparrow:een, Trezoriin, Ledger:ään, BlueWalletiin jne. syötetyt samat 12 sanaa näyttävät täsmälleen samat osoitteet ja saldot.





**Coin Walletissa Bitcoinille käytetyt johtamispolut**

| Osoitteen tyyppi              | Standardi | Johtamisen polku       | Alkaa | Kommentti                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| Natiivi SegWit (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Moderni muoto, alhaisimmat maksut           |
| Sisäkkäinen SegWit (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Yhteensopivuusväli vanhoille palveluille |
| Perintö (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Vanhin muoto, korkeimmat maksut          |

Jokaisen polun sisällä:


- `/0` - ulkoinen ketju (osoitteet, jotka ilmoitat maksujen vastaanottamista varten)
- `/1` - sisäinen ketju (wallet:n itsensä käyttämien osoitteiden muuttaminen)


Koska Coin Wallet noudattaa näitä julkisia standardeja ilman muutoksia, varanne ovat edelleen käytettävissä missä tahansa muussa yhteensopivassa wallet:ssä jopa 10-20-30 vuoden kuluttua.


## 8️⃣ Anonymiteetin parantaminen Torin avulla


**Miksi käyttää Toria Coin:ssä Wallet:ssa**

Tor piilottaa todellisen IP-osoitteesi Bitcoin-solmuilta, vaihtopisteiltä ja tarkkailijoilta.

Kaikki liikenne (saldot, transaktiot, vaihdot) kulkee Tor-verkon kautta - ei suoria yhteyksiä, ei IP-vuotoja.

Tämä on toteutettu suoraan sovelluksen lähdekoodissa (katso [.env configuration](https://github.com/CoinSpace/CoinSpace/blob/master/web/.env#L31)).


Coin Wallet:lla on piilotettu .onion-osoite ja v6.6.3:sta (joulukuu 2024) lähtien **rakennettu Tor-tuki suoraan mobiilisovellukseen**.


### Kuinka ottaa Tor käyttöön Androidissa ja iOS:ssä


1. **Asenna Orbot** - virallinen Tor-projektin sovellus (ilmainen)


   - Android → [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android) / [F-Droid](https://orbot.app/en/)
   - iPhone / iPad → [App Store](https://apps.apple.com/us/app/orbot/id1609461599)


2. **Avaa Orbot → napauta Start**

Valitse luettelosta **Coin Wallet**, jotta vain wallet käyttää Toria (valinnainen mutta suositeltava)

Odota, kunnes se sanoo **"Connected "** (10-30 sekuntia)


3. **Avaa Coin Wallet → Asetukset → Verkko**

Ota käyttöön **Käytä Tor**


4. **Tarkista tila**

Yläpalkkiin ilmestyy **violetti Tor-sipulikuvake** → kaikki liikenne ohjataan nyt Torin kautta


![image](assets/en/06.webp)


Siinä kaikki - matkapuhelimesi Coin Wallet on täysin anonyymi.


Nauti yksityisestä kryptonhallinnasta!


## 📝 Päätelmät


[Coin Wallet](https://coin.space/) - yksi todellisista Bitcoin wallet-pioneereista, jolla on 10 vuoden kehityshistoria.

Se on tarkoituksellisen yksinkertainen ja keskittyy laserilla sen ydintehtävään: kryptovaluuttasi turvalliseen säilyttämiseen.

Ei mainoksia, uutissyötettä, tilauksia, sosiaalisia ominaisuuksia tai häiriötekijöitä - vain puhdas, nopea ja itsestään huolehtiva wallet, joka tekee juuri sen, mitä sen kuuluukin tehdä.

Coin Wallet asettaa yksinkertaisuuden ja turvallisuuden etusijalle - on aina ollut ja tulee aina olemaan.


## 📖 Resurssit


https://coin.space/


https://support.coin.space/hc/en-us


https://en.bitcoin.it/wiki/Wallet


https://bitcoinops.org/


https://github.com/CoinSpace/CoinSpace/


https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/


https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts


https://github.com/paulmillr/scure-bip39