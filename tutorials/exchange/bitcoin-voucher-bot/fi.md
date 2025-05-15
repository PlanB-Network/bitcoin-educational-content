---
name: BitcoinVoucherBot
description: Telegram-robotti ostaa Bitcoin:n luottamuksellisesti
---
![image](assets/cover.webp)

_Tämän ohjeen on kirjoittanut_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)

# Johdanto

BitcoinVoucherBot on työkalu, jolla Bitcoineja voi ostaa Exchange:ssa euroja vastaan.

### KYC Light

Eurojen vaihtaminen Bitcoin:een on ensimmäinen ja perustavanlaatuisin askel tämän aiheen tutkimisen aloittamisessa, mutta se on ilmeisesti myös vaikein ja monimutkaisin. Vaihtoehtoja voi olla monia: Bitcoin:n tarjoaminen keskitettyjen vaihtopisteiden kautta, Bitcoin-aiheiset tapaamiset, ystävät, tuttavat ja muut. Liitymme Bitcoiner-yhteisöön ja **suositamme ehdottomasti keskitettyjen Exchangesin** käyttöä, jotta yksityisyydensuojaan voidaan kiinnittää enemmän huomiota.

Vaikka tämä vaihtoehto voi olla vähemmän kätevä, on tärkeää ymmärtää, että pörssit noudattavat Know Your Cutomer (KYC) -asetusta, joten jokaiselle niiltä ostetulle Satoshi:lle annetaan henkilöllisyys ja fyysinen sijainti. "Kätevyydellä" on joitakin silmiinpistäviä sivuvaikutuksia.

### Miten se tehdään?

Tässä tulee [BitcoinVoucherBot:](https://t.me/BitcoinVoucherBot) -palvelu, Telegram-botti, joka toimii SEPA-siirtojen ja Sats-ostojen välittäjänä.

### Edellytykset

BitcoinVoucherBotin käytön aloittamiseksi ei tarvitse luovuttaa arkaluonteisia henkilökohtaisia tietoja Botin henkilökunnalle. **Lupaa ei tarvita**.

Tarvitaan vain jo aktiivinen Telegram-tili ja pankkitili. **Huomautus**: Poste Italiane -yhtiössä avattu tili (italialaisille asiakkaille) tai yleisemmin ladattava kortti ei sovellu.

Telegram-keskustelussa valmistelemme tilauksen, maksamme sen pankkisiirrolla, ja lopuksi saamme botin kautta tositteen, jonka on myöntänyt kolmas osapuoli, joka ei tiedä ostoksen kohdetta.

### Botin aktivointi ja valikko

Aktivointi on yksinkertainen kertatoiminto. Etsi Telegramista _@BitcoinVoucherBot_ ja heti kun pääset botin chattiin, alareunassa erottuu suuri _Start/Start_-painike. Toiminto saa botin vastaamaan, jolloin se esittää valikon tärkeimmistä käytettävissä olevista komennoista. Myös ensimmäiset tervetuliaisviestit tulevat näkyviin, jotka kannattaa lukea huolellisesti.

**Varoitus**: on olemassa useita huijareita, jotka esiintyvät alkuperäisenä VoucherBotina. Jos et ole varma hausta Telegramin kautta, käytä BitcoinVoucherBot-linkkiä [virallisilla verkkosivuilla](https://www.bitcoinvoucherbot.com/)

![image](assets/it/01.webp)

Vaihtoehdot tulevat näkyviin napsauttamalla vasemmassa alakulmassa olevaa _Menu_-painiketta: voit napsauttaa komentoa vastaavaa sanaa tai kirjoittaa viestikenttään vinoviivan `/`, jota seuraa kirjoitettu komento.

![image](assets/it/02.webp)

Tärkeimpiä toimintoja ovat:


- _/purchase_: on varsinainen ostomenettely. Kun ostotapahtuma on suoritettu, robotti luo automaattisesti QR-koodin, joka on valmis lunastettavaksi.
- _/refill_: käytettävissä tämän ohjeen kirjoittamishetkellä, mutta emme käsittele sitä, koska teknisistä syistä tämä vaihtoehto saatetaan poistaa myöhemmin.
- _/swap_: avaa swap-menettelyn, joka on käytettävissä joko kätevän Telegram-botin avulla tai webin kautta.
- _/ap_: kertymäsuunnitelma, jonka avulla voit perustaa **Kiinteän kertymäsuunnitelman (CAP)**.
- _/lnaddress_: jonka kanssa meitä pyydetään yhdistämään oma LN Address, jota varten on tietty menettely, jonka näemme myöhemmin.
- _/credits_: Tarkistaa, kuinka paljon luottoa generate-seteliin on jäljellä.
- _/myorders_: näyttää botilla tehdyt tilaukset (**varoitus** järjestelmä seuraa vain 10 viimeisintä tilausta, ei koko historiaa).
- _/fees_: komento verkkomaksujen tarkistamiseksi. Niiden arvioimiseksi on aina parasta luottaa Mempool.spaceen.
- _/support_: tarvittaessa avautuu yhteystietoja, joiden kautta voit ilmoittaa ongelmista tukitiimille.

# Bitcoin hankintamenettely

## Tilauksen valmistelu

Napsauta komentovalikosta _/purchase_

![image](assets/it/03.webp)

Useita mahdollisuuksia ilmestyy, mutta me valitsemme _BTC-setelit_

![image](assets/it/04.webp)

BitcoinVoucherBotin avulla voit ostaa Bitcoin onchain, Lightning ja Liquid.

Valitse tässä vaiheessa _Onchain & Lightning 🔗⚡️_

![image](assets/it/05.webp)

Näyttö vaihtuu nopeasti ja VoucherBot ehdottaa ostosnimikkeitä. Ne alkavat vähintään 100,00 eurosta aina 900,00 euroon asti.

Ensimmäisen oston yhteydessä tarjotaan vain 100,00 €, Onchain ja Lightning -nimellisarvoja. Luottamuksellisuuden lisäämiseksi suosittelemme valitsemaan _Lightning ⚡️_

![image](assets/it/06.webp)

VoucherBot ilmoittaa meille, että ensimmäinen valinta on tehty ja että sen vahvistamiseksi meidän on valittava _Proceed_

![image](assets/it/07.webp)

Nyt on kyse maksutavan valinnasta. Siirto tapahtuu tilisiirtona **(hyväksytään vain SEPA)**. VoucherBot ehdottaa vastaanottajaksi yritystä, joka tarjoaa kaksi pankkitiliä, toisen Yhdistyneessä kuningaskunnassa ja toisen Sveitsissä. Sveitsiläinen pankki valittiin toteuttamaan tämä opetusohjelma

![image](assets/it/08.webp)

Tässä vaiheessa meitä pyydetään syöttämään IBAN-tilinumeromme, josta siirto valittuun pankkiin alkaa. Nämä tiedot muodostavat palapelin, jonka avulla robotti, eli kone, voi koota yhteen joitakin tietoja, jotta ostoprosessi sujuu ilman ihmisen puuttumista asiaan.

IBAN on kirjoitettava viestipalkkiin, tarkistettava ja lähetettävä botille.

![image](assets/it/09.webp)

Valvontaviesti näkyy nyt keskustelussa VoucherBotin kanssa.

Jos kaikki on oikein, jatka valitsemalla _Proceed_.

![image](assets/it/10.webp)

## Maksu

Muutaman hetken kuluttua, joka on tarpeen tietojen käsittelemiseksi, VoucherBot vastaa viestillä, joka sisältää kaikki tilauksen loppuunsaattamiseen tarvittavat tiedot. Riippuen siitä, mitä pankkisi vaatii, asiaankuuluvat tiedot ovat:


- `IBAN`, joka on välttämätön talletukselle, sekä vastaanottajan Address;
- `valittu summa` aiemmin raja-arvon kautta, jonka on täytyttävä, jotta VoucherBot voi tunnistaa tilauksen, kun maksu vastaanotetaan;
- `Maksun syy`, joka on maksun syy. **On kopioitava ja lisättävä poistamatta tai lisäämättä mitään siirtosi asianmukaiseen kenttään. Maksusyyn "." tai "-" voidaan korvata valkoisella välilyönnillä **.
- yksilöllinen `OrderID`, johon viitataan apua pyydettäessä.

Tämän jälkeen voit suorittaa maksun sovelluksen tai pankin kautta. Kun pankki on hyväksynyt maksun, on tärkeää muistaa painaa _ilmoita maksusta_ VoucherBotin chatissa. Tämä yksinkertainen toiminto ilmoittaa sinulle, että maksu on tulossa.

![image](assets/it/11.webp)

VoucherBot vastaa viestillä, joka sisältää erittäin tärkeän varoituksen: **Älä poista keskustelua**, ainakaan ennen kuin voucher on vastaanotettu, koska se on ainoa keino rakentaa tilaus uudelleen ja pitää se käynnissä.

![image](assets/it/12.webp)

---
Huom:


- vain SEPA-tilisiirrot hyväksytään;
- odotusajat liittyvät yksinomaan siihen, miten pankit (jotka eivät toimi 24/7/365 kuten Bitcoin) käsittelevät tositteen. Tositteen saaminen voi kestää muutamasta tunnista jopa 3 työpäivään;
- kaikkiin tarpeisiin, Bitcoin VoucherBotilla on erinomainen [tuki](https://t.me/BitcoinVoucherGroup) palvelu Telegramissa.

---
## Lunastus

Heti kun maksu on onnistunut, Bitcoin VoucherBot lähettää kupongin suoraan chattiin. Salamakuponki on QR-koodin muodossa, joka on painettu oranssille taustalle.

![image](assets/it/31.webp)

Siellä on kaikki tarvittavat tiedot sen lunastamiseksi:


- gW-17:ssä oleva summa, joka vastaa tilisiirtona lähetettyä summaa ilman palvelumaksuja ja verkkomaksuja;
- tositteen viitetunnus;
- päivämäärä, johon mennessä tosite on lunastettava tai varat menetetään, eli 25 päivää sen myöntämisestä.

Voit lunastaa kupongin kehystämällä QR-koodin yhteensopivan Wallet Lightning Network -laitteen skannaustoiminnolla tai LNURL:n kautta, joka näkyy myös QR-koodin alla.

Tässä opetusohjelmassa käytimme Wallet:tä Satoshi:stä käyttäen skannaustoimintoa, joka aktivoitiin _Send_-näppäimellä

![image](assets/it/32.webp)

Kun kännykkäkamera on aktivoitu, kehystä QR-koodi chatissa, avaa Telegram tietokoneelta

![image](assets/it/34.webp)

Ennen kuin jatkat, Wallet Of Satoshi alkaen todentamisnäyttö, joka sisältää määrän, joka täsmälleen vastaa summaa ilmaistu tositteen ja, kuvauksena, BitcoinVoucherBot. Voit lunastaa kupongin yksinkertaisesti klikkaamalla _Receive_

![image](assets/it/35.webp)

Wallet:n ja Satoshi:n prosessit kestävät muutaman hetken

![image](assets/it/36.webp)

ja lopuksi keräys ilmoitetaan ja se on välittömästi käytettävissä Wallet:n saldossa.

** Satoshi:n Wallet on säilytyssovellus: heti tositteen lunastamisen jälkeen on suositeltavaa siirtää Sats ei-huoltosovellukseen Wallet. **

![image](assets/it/37.webp)

### Kuinka lunastaa onchain-seteli

Kuten näimme tilauksen valmistelussa, VoucherBot mahdollistaa Sats:n ostamisen suoraan ketjussa, kun valitaan samanniminen kuponki.

**Huomautus**: Tilauksen valmistelu ja maksu eivät muutu, ne ovat aina samat. Se, mikä muuttuu, on se, miten ketjussa oleva tosite lunastetaan.

Kun olet suorittanut tilauksen, suorittanut maksun, painanut _ilmoita maksusta_ ja odottanut pankkien teknistä aikaa siirron siirtämiseen, VoucherBot vastaa lähettämällä kupongin suoraan chattiin.

Myös tämä kuponki on QR-koodin muodossa, mutta sen pääväri on kanarinkeltainen, ja - mikä tärkeintä - kuvauksessa on hyvin selitetty, että kyseessä on onchain-seteli, jonka lunastat suoraan Wallet onchain-ketjussasi, ja aloittaaksesi lunastusmenettelyn sinun on napsautettava _Redeem on Telegram_. Onchain-seteli sisältää myös salaman kohdalla jo nähdyt tiedot:


- gW-32:ssa oleva summa, joka vastaa tilisiirtona lähetettyä summaa ilman palvelumaksuja ja verkkomaksuja;
- kuponkikoodi;
- tositteen viitetunnus;
- päivämäärä, johon mennessä tosite on lunastettava tai varat menetetään, eli 25 päivää sen myöntämisestä.

![image](assets/it/22.webp)

**VAROITUS ⚠️:** napsautettuasi selityksen mukaisesti, avautuu toisen botin ponnahdusikkuna: **Voucher RedeemBot.**

Voucher RedeemBot on tätä tarkoitusta varten käytettävissä oleva työkalu. Olipa kyseessä ensimmäinen käyttö tai aiempia tilauksia, joka kerta kun uusi lunastus tehdään, on aina napsautettava _START_.

![image](assets/it/23.webp)

Tässä vaiheessa RedeemBot lataa ketjussa olevan kupongin, joka on helppo tunnistaa kuponkikoodista ja viitetunnuksesta. Se avaa myös palkin viestien kirjoittamiseen ja chattailun aloittamiseen botin kanssa, joka itse asiassa kehottaa meitä kertomaan sille onchain Address:n Wallet:stämme.

**Huomautus**: Tämän Address:n on oltava tyyppiä SegWit.

![image](assets/it/24.webp)

Avaamme Wallet:n tässä vaiheessa ja generate:n ja SegWit:n ja Address:n

![image](assets/it/25.webp)

me kopioimme sen

![image](assets/it/26.webp)

ja liitä se RedeemBotin kanssa käytävään keskusteluun

![image](assets/it/27.webp)

Meillä on nyt tarkistusnäyttö, jolla voimme tarkistaa, että kuponkikoodi on oikea, sekä Address, jonka olemme ilmoittaneet RedeemBotille. Tarkistetaan se hyvin, koska klikkaamalla _Proceed_, tapahtuma alkaa, eikä sitä voi enää mitenkään löytää, jos olemme esimerkiksi ilmoittaneet väärän Address:n.

![image](assets/it/28.webp)

Tapahtuma on alkanut, ja ketjusetelin Redeem-menettely päättyy.

![image](assets/it/29.webp)

kun taas Wallet:n historiassa voidaan nähdä, että se on tulossa.

![image](assets/it/30.webp)