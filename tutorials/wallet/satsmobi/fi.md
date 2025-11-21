---
name: Sats.mobi

description: A Telegram-yhteydellä varustettu huoltaja Wallet
---

![cover](assets/cover.webp)


_Tämän ohjeen on kirjoittanut_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


## Sats.Mobi

SatsMobi on Wallet, joka toimii Telegramissa, ja siinä on kaikki Lightning Network:n (custodial) Wallet:n toiminnot sekä joukko erittäin viihdyttäviä ominaisuuksia. Se sai alkunsa nykyään lakkautetun LightningTipBotin Fork:sta, ja se peri kaikki sen ominaisuudet, mutta lisäsi samalla nykyaikaisempia ominaisuuksia, mikä teki siitä nykyaikaisemman. Kuten LNTipBot, myös Sats.Mobi noudattaa avoimen lähdekoodin filosofiaa. Wallet voidaan konfiguroida ja hallita itsenäisesti kloonaamalla se tästä [repository](https://github.com/massmux/SatsMobiBot).


Jos haluat käyttää sitä yksinkertaisesti, keskustelun aloittaminen Telegramissa paljastaa, että kyseessä on botti.


## Asetukset

Etsi Telegramin hakupalkista "satsmobi" ja linkki [bottiin] (@SatsMobiBot) ilmestyy näkyviin.


**Huomio**: Jos et ole varma hakemisesta Telegramin kautta, pääset bottiin turvallisesti seuraavan [linkin](https://t.me/SatsMobiBot) kautta


![image](assets/it/01.webp)


Aloittaaksesi sinun tarvitsee vain painaa _START_


![image](assets/it/02.webp)


Voit tutkia Wallet:a valitsemalla vasemmasta alareunasta _Menu_.


![image](assets/it/03.webp)


Valitse nyt _/help_ pääkomentojen joukosta.


![image](assets/it/04.webp)


Sats.Mobi toivottaa meidät tervetulleeksi näyttämällä viestin, jossa luetellaan kaikki tärkeimmät toiminnot. Käynnistyksen yhteydessä botti loi myös LN Address:n, joka on linkitetty Telegramissa valittuun kahvaan (joka on oletusarvoisesti yksilöllinen). Komennot Sats:n lähettämiseen ja vastaanottamiseen tämän Wallet:n kanssa ovat näkyvissä, samoin kuin muut toiminnot, jotka näemme myöhemmin. On mielenkiintoista vilkaista myös valikkoa _/advanced_


![image](assets/it/05.webp)


On huomattavaa, että Sats.Mobi loi myös anonyymin LN Address:n, jota käytetään yksityisyyden suojaamiseksi. Botti toimii komennoilla: klikkaa vain vastaavaa sanaa tai kirjoita viestipalkkiin vinoviiva "/" ja sen jälkeen komento, jonka haluat suorittaa. Vaikka Wallet olisi juuri luotu, valitse esimerkiksi _/transaktiot_


![image](assets/it/06.webp)


Tämä komento näyttää luettelon viimeisimmistä tapahtumista, tässä tapauksessa nollasta.


![image](assets/it/07.webp)


## Vastaanottava Sats

Komento Invoice:n luomiseksi ja Sats:n vastaanottamiseksi on _/invoice_. Sats.Mobi toimii yksinomaan Satoshi:ssä, joka on Bitcoin:n pienin yksikkö; siksi Invoice:n luomiseksi on tarpeen kirjoittaa summa Sats:ssä viestipalkkiin ja lähettää se sitten chatissa botin kanssa.

![image](assets/it/08.webp)


Seuraavassa esimerkissä valittiin 210 Sats.


![cover](assets/it/09.webp)


Kun olet odottanut hetken Invoice:n valmistumista, se on saatavilla tekstinä ja QR-koodina. Kun maksat Invoice:n, Wallet näyttää saldon. Jos summa ei jostain syystä päivity, kirjoita _/saldo_ ja paina `enter`-näppäintä.


![image](assets/it/10.webp)


## Sats:n lähettäminen


Vaikka Sats on erittäin arvokas omaisuuserä, josta ei pidä luopua kevyesti, Sats.Mobi tekee tästä osasta houkuttelevan, joidenkin lyhyiden testien (eli parin koetapahtuman) suorittaminen ei ole ongelma.


### Invoice:n maksaminen


Yksinkertaisin tapa maksaa Invoice:lle on kopioida viestiketju `lnbc1xxxxxxx` ja liittää se viestipalkkiin sen jälkeen, kun olet kirjoittanut komennon _/pay_. **Oikea syntaksi** edellyttää, että komennon jälkeen jätetään välilyönti.


![image](assets/it/11.webp)


Wallet lähettää viestin, jossa pyydetään vahvistusta. Invoice:lle maksetaan klikkaamalla _Pay_.


![image](assets/it/12.webp)


Sats.Mobi voi luottaa tehokkaaseen ja hyvien yhteyksien omaavaan Lightning-solmuun, harvoin maksut epäonnistuvat, koska se onnistuu aina löytämään oikean reitityksen.


### Maksaminen mukavasti matkapuhelimella


Selailu Telegramissa, Sats.Mobi on saatavilla myös mobiilissa. Kätevin toiminto maksamiseen mobiililla on QR-koodin skannaaminen, mutta tästä Wallet:sta se puuttuu jo lähtökohtaisesti, koska se ei ole itsenäinen sovellus vaan sisältyy sosiaaliseen verkostoon. Sats.Mobi on siksi ohjelmoitu helpottamaan mobiilikokemusta mahdollisimman paljon: se voi todellakin purkaa kuvan, kuten sen Invoice:n QR-koodista otetun valokuvan, jonka haluat maksaa.


Oletetaan esimerkiksi, että haluat maksaa Invoice:lle 50 Sats.


![image](assets/it/20.webp)


Kun tämä näytetään meille, voimme ottaa kuvan siihen liittyvästä QR-koodista.


![image](assets/it/21.webp)


Sitten avaamme Telegramin matkapuhelimessa ja liitämme Sats.Mobin kanssa käytävään keskusteluun QR-koodista otetun valokuvan


![cover](assets/it/22.webp)


Kun se on valittu, lähetämme sen botille:


![image](assets/it/23.webp)

Sats.Mobi purkaa valokuvan ja **antaa välittömästi maksupyynnön** oikean kuvauksen kanssa. Keskustelu pyytää vahvistusta, ja jatkaaksesi sinun on painettava _/pay_

![image](assets/it/24.webp)


Odota hetki, jotta maksu voidaan käsitellä.


![image](assets/it/25.webp)


Invoice 50 Sats:lle on maksettu, mikä on saavutettu ilman kameraa ja sen integroitua skannaustoimintoa.


### Sats.Mobi Telegram-ryhmissä


![image](assets/it/27.webp)


LNTipBotin tunnetuksi tehneiden ja Sats.Mobin Telegramiin tuomien ominaisuuksien joukossa on ominaisuus, joka tekee kokemuksesta hauskan ja vuorovaikutteisen ryhmän jäsenille.

Omistajat voivat kutsua botin liittymään ryhmäkeskusteluun ja nimetä Sats.Mobin ylläpitäjäksi. Siitä hetkestä lähtien hauskuus alkaa, sillä jäsenet voivat alkaa palkita muita käyttäjiä heidän panoksestaan ryhmään.


- _/tip_ lisää vinkin vastaamalla viestiin;
- _/send_ lähettää varoja määrittämällä vastaanottajaksi LN Address tai Telegram-kahvan;
- _/hana_ (valikossa _/edistyneet_) mahdollistaa vinkkisarjojen luomisen, joita ryhmän nopeimmat jäsenet voivat kerätä klikkaamalla _/kerää_;
- _/tipjar_ (valikossa _/advanced_) luo toisenlaisen jakelun, joka voidaan lähettää ryhmän käyttäjille.


Jokaisella komennolla on oma syntaksinsa, joka selitetään komentojen päävalikossa.


Entä jos emme ole ryhmän omistaja? Ei hätää: pyydä vain perustajaa kutsumaan Sats.Mobi, lisää se ryhmän ylläpitäjäksi ja olet valmis!


## Myyntipiste (POS)


Kun Sats.Mobi käynnistetään ensimmäistä kertaa, robotti luo myös toisen ominaisuuden käyttäjälle: **POS**. Käyttäjä aktivoi "laitteen" komennolla _/pos_ tai napsauttamalla siihen liittyvää painiketta oikeassa alakulmassa olevasta konsolista. Itse asiassa POS on web-sovellus, joka avautuu ponnahdusikkunana Telegram-keskustelussa


![image](assets/it/14.webp)


Interface näyttää käyttäjän henkilökohtaisen Telegram-kahvan vasemmassa yläkulmassa, ja sitä käytetään yksinkertaisesti kuten kaikkia kassakoneita käytetään: kirjoittamalla summa näppäimistöllä. Oletetaan nyt, että haluamme kerätä 21 eurosenttiä palvelusta. Koska tiedämme, että Sats.Mobi hallitsee vain Sats:tä, muuntaminen ei ole helppoa tehdä päässämme. Sitä vastoin kassakone näyttää laskentayksikkönä euron ja näyttää samalla vastineen Satoshi:nä.


![image](assets/it/15.webp)

Napsauttamalla _/OK_-painiketta näytetään Invoice, joka voidaan näyttää asiakkaalle QR-koodin avulla tai lähettää merkkijonona pikaviestimellä, jotta se voidaan maksaa.

![image](assets/it/16.webp)

![image](assets/it/17.webp)


Kassapalvelu on luonnollisesti käytettävissä myös matkapuhelimissa, ja sitä käytetään samalla tavalla kuin aiemmin on esitetty.


![image](assets/it/18.webp)


Se näkyy hyvin myös matkapuhelimen näytöllä:


![image](assets/it/19.webp)


## Lisäominaisuudet


On muitakin ominaisuuksia, jotka täydentävät Sats.Mobi Wallet:n tarjontaa, joka, kuten olemme nähneet, laajentaa Wallet:n käsitettä maksujen vastaanotto- ja lähetystoimintojen ulkopuolelle:


- _/nostr_: Wallet:n liittäminen omaan Nostr-käyttäjääsi zapien vastaanottamiseksi;
- _/cashback_: näyttää koodin, jonka voi esittää kauppiaalle saadakseen käteispalautuksen ostoksesta;
- _/buy_: käynnistää botin sisäisen ohjatun menettelyn, jonka avulla Sats voidaan ostaa eurolla;
- _/activatecard_: pyytää aktivoimaan NFC-pankkikortin, joka voidaan ladata Sats.Mobi Wallet:n kautta ja jonka ilmoitukset voidaan aktivoida;
- _/link_: luo linkin omalle Zeus- tai Blue Wallet:lle, joita voidaan käyttää tämän Wallet:n kauko-ohjaimina.


## Päätelmä

Sats.Mobi on miellyttävä ja hauska Wallet, joka tuo takaisin LNTipBotista saadut kokemukset käyttämällä LNBitsin kehittyneempiä toimintoja. On kuitenkin tärkeää muistaa, että **se on huoltajapalvelu**. Siksi sitä tulisi käyttää hyvin harvojen Sats:ien hallussapitoon, se ei ole pääasiallinen Wallet Lightning Network-varoillesi. Siihen liittyy myös sisäinen kapasiteettiraja, joka on 500 000 Sats:tä, ja sitä ei kannata ylittää.


Jos etsit Lightning Network-lompakoita, jotka eivät ole henkilökohtaisia, kannattaa ehdottomasti tutustua muihin tuotteisiin.


---
### Dokumentaatio


- [Github](https://github.com/massmux/SatsMobiBot)
- Soittolista [videoita](https://www.youtube.com/results?search_query=Sats.mobi) demo