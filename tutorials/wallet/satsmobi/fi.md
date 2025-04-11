---
name: Sats.mobi
description: Wallet (huoltaja) Telegramin ulottuvilla
---
![cover](assets/cover.webp)

_Tämän ohjeen on kirjoittanut_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)

# Sats.Mobi

SatsMobi on Telegramissa toimiva Wallet, jolla on kaikki Wallet Lightning Network:n (custodial) toiminnot ja joka tarjoaa lisäksi useita erittäin hauskoja ominaisuuksia. Se juontaa juurensa LightningTipBotin Fork:sta, joka on nyt lakkautettu, ja se perii kaikki sen ominaisuudet samalla kun se lisää nykyaikaisempia ominaisuuksia, mikä tekee siitä nykyaikaisemman. LNTipBotin Sats.Mobi jäljittää myös avoimen lähdekoodin filosofiaa. Wallet voidaan itse asiassa konfiguroida ja hallita itse kloonaamalla se tästä [repository](https://github.com/massmux/SatsMobiBot).

Jos taas haluat käyttää sitä mieluummin yksinkertaisella tavalla, käynnistä vain keskustelu Telegramissa ja huomaat, että kyseessä on botti.

# Asetukset

Etsi Telegramin hakupalkista "satsmobi", ja linkki [bottiin] (@SatsMobiBot) tulee näkyviin.

**Varoitus**: Jos et ole varma hausta Telegramin kautta, pääset bottiin turvallisesti seuraavan [linkin](https://t.me/SatsMobiBot) kautta

![image](assets/it/01.webp)

Käynnistääksesi sen sinun tarvitsee vain painaa _START_

![image](assets/it/02.webp)

Voit tutustua Wallet:aan valitsemalla vasemmasta alakulmasta _Menu_.

![image](assets/it/03.webp)

Valitse nyt _/help_ pääkomentojen joukosta.

![image](assets/it/04.webp)

Sats.Mobi toivottaa meidät tervetulleeksi näyttämällä viestin, jossa luetellaan kaikki tärkeimmät ominaisuudet. Käynnistyksen yhteydessä botti on myös luonut LN Address:n, joka on linkitetty Telegramissa valittuun kahvaan (joka on oletusarvoisesti yksilöllinen). Komennot Sats:n lähettämiseen ja vastaanottamiseen tämän Wallet:n kanssa ovat näkyvissä, samoin kuin muut toiminnot, jotka näemme myöhemmin. On myös mielenkiintoista vilkaista heti aluksi _/lisävalikkoa_

![image](assets/it/05.webp)

On käynyt ilmi, että Sats.Mobi on luonut myös nimettömän LN Address:n, jota voidaan käyttää yksityisyyden suojaamiseen. Botti toimii komennoilla: klikkaa vain vastaavaa sanaa tai kirjoita viestipalkkiin vinoviiva "/" ja sen jälkeen komento, jonka haluat suorittaa. Vaikka Wallet olisi juuri luotu, valitse esimerkiksi _/transaktiot_

![cimageover](assets/it/06.webp)

Tämä komento näyttää luettelon viimeisimmistä tapahtumista, tässä tapauksessa nollasta.

![image](assets/it/07.webp)

# Vastaanottava Sats

Komento Invoice:n luomiseksi ja Sats:n vastaanottamiseksi on _/invoice_. Sats.Mobi syitä yksinomaan Satoshi:ssä, joka on Bitconin pienin yksikkö; siksi Invoice:n luomiseksi on tarpeen kirjoittaa summa Sats:ssä viestipalkkiin ja lähettää se myöhemmin chatissa botin kanssa.

![image](assets/it/08.webp)

Seuraavassa esimerkissä valittiin vastaanotettavaksi 210 Sats:n määrä.

![cover](assets/it/09.webp)

Kun Invoice:n valmistelua on odotettu hetki, se on saatavilla tekstinä ja QR-koodina. Kun maksat Invoice:n, Wallet näyttää saldon. Jos loppusumma on jostain syystä vanhentunut, kirjoita _/saldo_ ja paina `send`-näppäintä.

![image](assets/it/10.webp)

# Lähetä Sats

Vaikka Satss on korvaamaton voimavara, josta ei pitäisi erota pintapuolisesti, Sats.Mobi tekee tästä osasta houkuttelevan, joidenkin lyhyiden testien suorittaminen (eli pari testitapahtumaa) ei ole ongelma.

## Invoice:n maksaminen

Helpoin tapa maksaa Invoice:lle on kopioida viestiketju `lnbc1xxxxxxx` ja liittää se viestipalkkiin sen jälkeen, kun olet kirjoittanut komennon _/pay_. **Korrektiin syntaksiin** kuuluu välilyönnin jättäminen komennon jälkeen.

![image](assets/it/11.webp)

Wallet lähettää viestin, jossa pyydetään vahvistusta. Napsauttamalla _Pay_ Invoice maksetaan.

![image](assets/it/12.webp)

Sats.Mobi voi luottaa tehokkaaseen ja hyvin yhdistettyyn Lightning-solmuun, harvoin maksut epäonnistuvat, koska se löytää aina oikean reitityksen.

## Maksa kätevästi matkapuhelimella

Sats.Mobi on saatavilla myös matkapuhelimissa. Kätevin toiminto mobiilimaksamiseen on QR-koodin kehystäminen, mutta tästä Wallet:sta tämä puuttuu jo lähtökohtaisesti, koska se ei ole erillinen sovellus vaan sisältyy sosiaaliseen. Sats.Mobi on siksi ohjelmoitu niin, että se tekee mobiilimaksamisesta mahdollisimman helppoa: se voi itse asiassa purkaa kuvan, esimerkiksi sen Invoice:n QR-koodista otetun valokuvan, jonka haluat maksaa.

Oletetaan esimerkiksi, että haluamme maksaa Invoice:lle 50 Sats.

![image](assets/it/20.webp)

Kun tämä näytetään meille, voimme ottaa kuvan kyseisestä QR-koodista.

![image](assets/it/21.webp)

Sitten avaamme Telegramin matkapuhelimessa ja liitämme juuri ottamamme valokuvan QR-koodiin Sats.Mobin kanssa käytävässä keskustelussa

![cover](assets/it/22.webp)

Kun se on valittu, lähetämme sen botille:

![image](assets/it/23.webp)

Sats.Mobi purkaa kuvan ja **esittää maksupyynnön** välittömästi oikean kuvauksen kanssa. Keskustelu pyytää vahvistusta, jatkaaksesi sinun on painettava _/pay_

![image](assets/it/24.webp)

Odotamme muutaman hetken, jotta maksu voidaan käsitellä.

![image](assets/it/25.webp)

Invoice:n ja 50 Sats:n välillä maksettiin, ja tämä tulos saavutettiin ilman kameraa ja sen sisäänrakennettua skannaustoimintoa.

## Sats.Mobi Telegram-ryhmissä

![image](assets/it/27.webp)

LNTipBotista kuuluisaksi tehneistä ominaisuuksista, jotka Sats.Mobi tuo takaisin Telegramiin, on se, joka tekee ryhmän jäsenten kokemuksesta hauskan ja vuorovaikutteisen.

Omistajat voivat kutsua botin liittymään ryhmäkeskusteluun ja nimetä Sats.Mobin ylläpitäjäksi. Siitä eteenpäin hauskuus alkaa, sillä jäsenet voivat alkaa palkita muita käyttäjiä heidän panoksestaan ryhmässä.


- _/tip_ lisää vinkin vastaamalla viestiin;
- _/send_ lähettää varoja määrittämällä vastaanottajaksi LN Address tai Telegram-kahvan;
- _/hana_ (valikossa _/edistyneet_) voit luoda joukon vinkkejä, joita nopeimmat ryhmän jäsenet voivat kerätä napsauttamalla _/kerätä_;
- _/tipjar_ (valikossa _/advanced_) luo toisenlaisen jakelun, joka voidaan lähettää ryhmän käyttäjille.

Kullakin näistä komennoista on oma syntaksinsa, joka selitetään komentojen päävalikossa.

Entä jos emme ole ryhmän omistaja? Ei hätää: pyydä vain perustajalta kutsua Sats.Mobi, lisää hänet ryhmän ylläpitäjäksi ja olet valmis!

# Myyntipiste (POS)

Kun Sats.Mobi käynnistetään ensimmäistä kertaa, robotti luo käyttäjälle myös toisen ominaisuuden: **POS**. Käyttäjä aktivoi "laitteen" komennolla _/pos_ tai napsauttamalla oikeassa alakulmassa olevan konsolin vastaavaa painiketta. Itse asiassa POS on web-sovellus, joka avautuu ponnahdusikkunana Telegram-keskustelussa

![image](assets/it/14.webp)

Interface:ssä on Telegramin henkilökohtainen kahva vasemmassa yläkulmassa, ja sitä käytetään yksinkertaisesti kuten kaikkia POS-kassoja: näppäilemällä summa näppäimistöllä. Oletetaan nyt, että haluamme kerätä 21 senttiä palvelusta. Koska tiedämme, että Sats.Mobi käsittelee natiivisti vain Satssia, muuntamista ei ole helppo tehdä päässämme. Sen sijaan kassakone näyttää laskentayksikkönä euroa, kun taas Satoshi:n vastaava arvo näkyy.

![image](assets/it/15.webp)

Napsauttamalla _/OK_-painiketta saat esiin Invoice:n, joka voidaan näyttää asiakkaalle QR-koodilla tai lähettää merkkijonona pikaviestillä, jotta se voidaan maksaa

![image](assets/it/16.webp)

![image](assets/it/17.webp)

Kassapalvelu on luonnollisesti käytettävissä myös matkapuhelimessa, kun siihen soitetaan edellä esitetyllä tavalla.

![image](assets/it/18.webp)

Se on myös hyvin nähtävissä matkapuhelimen näytöltä:

![image](assets/it/19.webp)

# Lisäominaisuudet

Wallet Sats.Mobi -tarjontaa täydentävät muut ominaisuudet, jotka, kuten olemme nähneet, laajentavat Wallet-konseptia maksujen vastaanotto- ja lähetystoimintojen ulkopuolelle:


- _/nostr_: Wallet:n yhdistäminen käyttäjän Nostr:iin zapien vastaanottamista varten;
- _/cashback_: näyttää koodin, jonka voit näyttää kauppiaalle saadaksesi käteispalautuksen kulusta;
- _/buy_: käynnistää botin sisällä ohjatun toiminnon, jonka avulla voit ostaa Sats:n eurolla:
- _/activatecard_: pyytää aktivoimaan NFC-pankkikortin, joka voidaan ladata uudelleen Wallet Sats.Mobin kautta ja jonka ilmoitukset voidaan aktivoida;
- _/link_: luo linkin omalle Wallet Zeukselle tai Blue Wallet:lle, joita voit käyttää tämän Wallet:n kauko-ohjaimina.

# Päätelmä

Sats.Mobi on Wallet, jota on miellyttävä ja hauska käyttää, ja se tuo takaisin LNTipBotilla saadut kokemukset LNBitsin kehittyneempien ominaisuuksien avulla. On kuitenkin tärkeää muistaa, että **se on huoltajapalvelu**. Siksi sitä on tarkoitus käyttää hyvin harvojen Satssin säilyttämiseen; se ei ole Wallet-pääoma omille Lightning Network-varoilleen. Myös kapasiteettiraja on 500 000 Satssia, jota ei suositella ylitettäväksi.

Jos etsit Wallet Lightning Network:tä, joka ei ole huostaanotettava, sinun on ehdottomasti tutustuttava muihin tuotteisiin.

---
### Dokumentaatio


- [Github](https://github.com/massmux/SatsMobiBot)
- Soittolista [video](https://www.youtube.com/results?search_query=Sats.mobi) demoista