---
name: Sentinel Watch-Only
description: Mikä on Watch-Only lompakko ja miten sitä käytetään?
---
![kansi](assets/cover.webp)

---

***VAROITUS:** Samourai Walletin perustajien pidätyksen ja heidän palvelimiensa takavarikoinnin jälkeen 24. huhtikuuta, Sentinel-sovellus toimii edelleen, mutta **oman Dojon käyttö on pakollista** päästäksesi käsiksi lohkoketjun tietoihin ja suorittaaksesi siirtoja.*

_Seuraamme tiiviisti tämän tapauksen kehitystä sekä siihen liittyvien työkalujen kehitystä. Voit olla varma, että päivitämme tämän oppaan, kun uutta tietoa tulee saataville._

_Tämä opas on tarkoitettu vain koulutus- ja tiedotustarkoituksiin. Emme kannusta tai hyväksy näiden työkalujen käyttöä rikollisiin tarkoituksiin. Jokaisen käyttäjän on noudatettava oman lainkäyttöalueensa lakeja._

---

*"Pidä yksityiset avaimet yksityisinä."*

Tässä artikkelissa tutkimme kaiken, mitä sinun tarvitsee tietää Watch-Only lompakoista. Keskustelemme siitä, miten ne toimivat ja tarkastelemme markkinoilla saatavilla olevia eri sovelluksia. Lopuksi tarjoamme yksityiskohtaisen oppaan yhdestä suosituimmista Watch-Only lompakko sovelluksista: Sentinel.

## Mikä on Watch-Only Lompakko?
Watch-Only lompakko, tai vain-luku lompakko, on ohjelmistotyyppi, joka mahdollistaa käyttäjän seurata transaktioita, jotka liittyvät yhteen tai useampaan tiettyyn Bitcoinin julkiseen avaimiin, pääsemättä käsiksi vastaaviin yksityisiin avaimiin.

Tämän tyyppinen sovellus säilyttää vain tiedot, jotka ovat tarpeen Bitcoin-lompakon seurantaan, mukaan lukien sen saldon ja transaktiohistorian katselu, mutta sillä ei ole pääsyä yksityisiin avaimiin. Siksi on mahdotonta käyttää lompakossa olevia bitcoineja Watch-Only sovelluksessa.
![watch-only](assets/en/1.webp)
Watch-Onlya käytetään yleensä yhdessä laitteistolompakon kanssa. Tämä mahdollistaa lompakon yksityisten avainten "kylmän" säilytyksen, laitteella, joka ei ole yhteydessä internetiin, mikä minimoi hyökkäyspinnan eristäen yksityiset avaimet mahdollisesti haavoittuvilta ympäristöiltä. Toisaalta Watch-Only sovellus säilyttää yksinomaan Bitcoin-lompakon laajennetun julkisen avaimen (`xpub`, `zpub` jne.). Tämä vanhempi avain ei mahdollista yhdistettyjen yksityisten avainten löytämistä ja siten ei salli bitcoinien käyttöä. Se kuitenkin mahdollistaa lasten julkisten avainten ja vastaanotto-osoitteiden johdannaisen. Tietäen laitteistolompakon turvaamien osoitteiden tiedot, Watch-Only sovellus voi seurata näitä transaktioita Bitcoin-verkossa, tarjoten käyttäjälle mahdollisuuden seurata saldoaan ja luoda uusia vastaanotto-osoitteita, ilman että laitteistolompakkoa tarvitsee yhdistää joka kerta.

## Mikä Watch-Only Lompakko kannattaa käyttää?
Tällä hetkellä kattavin Watch-Only sovellus on [Sentinel](https://sentinel.watch/), jonka ovat kehittäneet Samourai Walletin tiimit. Se kattaa kaikki hyvän Watch-Only lompakon olennaiset ominaisuudet:
- Tuki laajennetuille avaimille, julkisille avaimille ja osoitteille;
- Mahdollisuus järjestää useita tilejä tai lompakoita kokoelmiin;
- Osoitteiden luominen bitcoineja vastaanottamaan omalle laitteistolompakolle ilman sen suoraa käyttöä;
- Mahdollisuus rakentaa ja lähettää transaktioita offline-tilassa;
- Vaihtoehto yhdistää omaan Bitcoin-noodiin;
- Tor-integraatio parannetun yksityisyyden vuoksi.
Sentinelin ainutlaatuiset haitat ovat siinä, että sovellus on saatavilla vain Androidille eikä se tue moniallekirjoituslompakoita. Siksi, jos omistat Android-laitteen ja lompakkosi on klassinen yksiallekirjoitus, suosittelen Sentinelia.
Niille, jotka haluavat seurata moniallekirjoituslompakkoa, Blue Wallet on ainoa sovellus, jonka tiedän tarjoavan Watch-Only tilan näille lompakkotyypeille, ja se on saatavilla sekä Androidille että iOS:lle.
iOS-käyttäjille, jotka etsivät vaihtoehtoa Sentinelille, [Green Wallet](https://blockstream.com/green/) tai [Blue Wallet](https://bluewallet.io/watch-only/) saattavat olla vaihtoehtoja, vaikka niiden watch-only -toiminnallisuus ei olekaan yhtä kattava kuin Sentinelin.![watch-only](assets/notext/2.webp)
## Kuinka käyttää Sentinel Watch-Only -lompakkoa?
### Asennus ja asetukset
Aloita asentamalla Sentinel-sovellus. Voit tehdä tämän joko Google Play Kaupasta tai käyttämällä [virallisella verkkosivustolla ladattavissa olevaa APK-tiedostoa](https://sentinel.watch/download/).

![watch-only](assets/notext/3.webp)

Sovelluksen ensimmäisellä avaamiskerralla sinulle annetaan valinta:
- `Yhdistä Dojoon`;
- `Yhdistä Samourain palvelimeen`.

Dojo, jonka Samourai-tiimi on kehittänyt, on täysi Bitcoin-solmun versio, jonka voi asentaa itsenäisesti tai lisätä yhdellä klikkauksella node-in-box -ratkaisuihin, kuten [Umbrel](https://umbrel.com/) ja [RoninDojo](https://ronindojo.io/).

[**-> Tutustu, kuinka asentaa RoninDojo v2 Raspberry Pi:lle.**](https://planb.network/fr/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8)

Jos sinulla on oma Dojo, voit yhdistää sen tässä vaiheessa. Näin tehdessäsi hyödyt korkeimmasta yksityisyyden tasosta tarkistaessasi Bitcoin-verkon transaktiotietojasi.

![watch-only](assets/notext/4.webp)

Muussa tapauksessa on mahdollista valita Samourain oletuspalvelin. Voit myös valita, haluatko yhdistää Torin kautta vai ei.

![watch-only](assets/notext/5.webp)

Tämän jälkeen saavut Sentinelin pääsivulle.

![watch-only](assets/notext/6.webp)

Aloittaaksesi, voit asettaa sovelluksen. Napsauta kolmea pientä pistettä oikeassa yläkulmassa, sitten `Asetukset`.

![watch-only](assets/notext/7.webp)
Valitsemalla `Käyttäjän PIN-koodi`, sinulla on mahdollisuus asettaa salasana watch-only -lompakkosi pääsyn suojaamiseksi. Sinulla on myös mahdollisuus vaihtaa viitevaluuttaa muuntaaksesi saldosi fiat-valuutaksi tai jopa piilottaa fiat-arvot aktivoimalla `Piilota fiat-arvot` -vaihtoehdon. Lisäturvallisuuden vuoksi voit aktivoida `Ota kuvakaappaukset pois käytöstä`, mikä estää kaikki kuvakaappaukset Sentinel-sovelluksestasi ja näin ollen välttää tietojen paljastumisen ulkoisella näytöllä.
![watch-only](assets/notext/8.webp)

Tässä asetusvalikossa sinulla on myös mahdollisuus varmuuskopioida Sentinelisi.

### Watch-Only -lompakon käyttö
Kotisivulta paina sinistä `UUSI` -nappia lisätäksesi uuden laajennetun julkisen avaimen seurantaan. Sinulla on sitten mahdollisuus skannata avaimen QR-koodi tai suoraan liittää avain (`xpub`, `zpub`...) valitsemalla `Liitä Pubkey`.

![watch-only](assets/notext/9.webp)

Yleensä lompakkosi `xpub` on suoraan saatavilla käyttämäsi lompakonhallintaohjelmiston kautta. Esimerkiksi, jos hallinnoit laitteistolompakkoasi Sparrow'n avulla, tämä tieto löytyy `Asetukset`-välilehdeltä, `Keystore`-osion alta.

![watch-only](assets/notext/10.webp)
Kun olet syöttänyt laajennetun julkisen avaimen Sentinel-sovellukseen, sovellus tarjoaa sinulle mahdollisuuden luoda uuden kokoelman. Kokoelma edustaa yhdessä järjestettyä joukkoa laajennettuja julkisia avaimia. Tämä vaihtoehto antaa sinulle mahdollisuuden ei vain listata kaikkia `xpub`-avaimiasi, vaan myös luokitella ne järjestyksessä. Esimerkiksi, jos sinulla on Samourai Wallet, jossa on useita tilejä (talletus, premix, postmix...), voit koota kaikki nämä tilit `Samourai`-kokoelman alle. Lompakoille, joita hallinnoit perheellesi, saatat luoda kokoelman nimeltä `Perhe`.
Valitse `Luo uusi kokoelma`. Kirjoita sitten nimi juuri integroidulle laajennetulle avaimelle. Esimerkiksi, jos skannaisin Samourai-lompakkoni talletustilin, nimeäisin tämän avaimen `Talletus`. Klikkaa `TALLENNA` viimeistelläksesi.

![watch-only](assets/notext/11.webp)

Seuraavaksi, anna nimi tälle kokoelmalle ja paina vahvistuskuvaketta näytön oikeassa yläkulmassa tallentaaksesi kokoelman. Kokoelmasi on nyt näkyvissä Sentinelin kotinäytöllä.

![watch-only](assets/notext/12.webp)

Jos haluat lisätä toisen laajennetun julkisen avaimen, klikkaa `UUSI` uudelleen ja syötä avain.

![watch-only](assets/notext/13.webp)
Sinua pyydetään sitten valitsemaan kokoelma, johon haluat integroida tämän avaimen, tai luomaan uuden. Esimerkiksi omassa tapauksessani olen perustanut kokoelman erityisesti Ledger-lompakolleni.
![watch-only](assets/notext/14.webp)

Nähdäksesi kokoelman laajennetut avaimet yksityiskohtaisesti, klikkaa vain sitä. Voit sitten navigoida eri välilehtien kautta tarkastellaksesi tapahtumahistoriaa.

![watch-only](assets/notext/15.webp)

Kokoelmasta voit napauttamalla kolmea pientä pistettä oikeassa yläkulmassa ja sitten `Näytä käyttämättömät lähdöt`, päästä käsiksi listaukseen seuratun lompakon hallussa olevista UTXO:ista.

![watch-only](assets/notext/16.webp)

### Bitcoinien lähettäminen ja vastaanottaminen Sentinelin kautta
Kuten mikä tahansa hyvä vain-luku lompakko, Sentinel mahdollistaa vastaanotto-osoitteiden luomisen bitcoinien vastaanottamiseksi seuratulle lompakolle. Mutta Sentinel tarjoaa myös toisen edistyneen ominaisuuden: osittain allekirjoitetun Bitcoin-siirron (PSBT) luomisen ja lähettämisen. Näin ollen lompakko, joka hallitsee yksityisiä avaimia, voi allekirjoittaa tämän siirron, joka kerran allekirjoitettuna voidaan lähettää Bitcoin-verkkoon Sentinelin kautta. Katsotaan, miten tämä kaikki tehdään.

**Varoitus, vastaanotto-osoitteiden käyttöä ei suositella, jos lompakko itse ei ole vahvistanut osoitetta.** Jos lompakko, joka hallitsee yksityisiä avaimia, kuten laitteistolompakko, ei ole nimenomaisesti vahvistanut, että tietty osoite kuuluu sille, bitcoinien lähettäminen tähän osoitteeseen on riskialtista. Todellakin, ilman tätä vahvistusta, ei ole takeita siitä, että osoite todella kuuluu lompakollesi. Siksi vain-luku lompakon vastaanotto-ominaisuutta tulisi käyttää varoen, pitäen mielessä, että lähetetyt varat saattavat mahdollisesti kadota.

Vastaanottaaksesi bitcoineja Sentinelin kautta, valitse kiinnostuksen kohde kokoelma, sitten klikkaa välilehteä, joka vastaa laajennettua julkista avainta, johon haluat siirtää varoja.

![watch-only](assets/notext/17.webp)

Lopuksi, klikkaa nuolikuvaketta näytön alavasemmalla. Sentinel luo sinulle tyhjän vastaanotto-osoitteen. Voit kopioida sen tai skannata käyttäen QR-koodia.

![watch-only](assets/notext/18.webp)
PSBT:n luominen Sentinelista ja siten maksutapahtuman aloittaminen tapahtuu menemällä lompakon laajennettuun avaimistoon, josta haluat suorittaa maksun. Otetaan esimerkiksi talletustilini Samourai-lompakossani. Klikkaa sitten oikean alakulman nuolikuvaketta.

![watch-only](assets/notext/19.webp)

Syötä kaikki tapahtumaasi liittyvät parametrit:
- Syötä vastaanottajan osoite (klikkaamalla QR-koodikuvaketta, voit skannata tämän osoitteen);
- Määritä lähetettävä summa tähän osoitteeseen;
- Määritä tapahtumamaksut.

Kun olet täyttänyt kaikki tarvittavat kentät tapahtumallesi, paina `COMPOSE UNSIGNED TRANSACTION` -nappia.

![watch-only](assets/notext/20.webp)

Tämän jälkeen pääset käsiksi PSBT:hen, joka edustaa rakennettua mutta allekirjoittamatonta Bitcoin-tapahtumaa, koska Sentinelillä ei ole pääsyä yksityisiin avaimiisi. Sinulla on mahdollisuus kopioida tämä tapahtuma, viedä se `.psbt`-tiedostona tai skannata se animoidun QR-koodin kautta.

![watch-only](assets/notext/21.webp)

Mene sitten lompakkoosi, jolla on yksityiset avaimet tapahtuman allekirjoittamiseen (Samourai, laitteistolompakko...).

![watch-only](assets/notext/22.webp)

Kun tapahtuma on allekirjoitettu, voit palata Sentinelille lähettämään sen. Tee tämä klikkaamalla kotivalikossa oikeassa yläkulmassa olevia kolmea pientä pistettä ja sitten `Broadcast transaction`.

![watch-only](assets/notext/23.webp)

Voit syöttää allekirjoitetun PSBT:n kolmella eri tavalla:
- Liittämällä sen suoraan leikepöydältäsi;
- Tuomalla sen `.psbt`-tiedostosta;
- Skannaamalla sen QR-koodin kautta.

![watch-only](assets/notext/24.webp)

Kun allekirjoitettu tapahtuma on syötetty harmaaseen kehykseen, voit klikata vihreää `BROADCAST TRANSACTION` -nappia lähettääksesi sen Bitcoin-verkkoon. Sentinel antaa sinulle sen TXID:n.

![watch-only](assets/notext/25.webp)

