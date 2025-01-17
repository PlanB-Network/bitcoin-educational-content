---
name: Ledger Nano S

description: Kuinka otat käyttöön Ledger Nano S -laitteesi
---

![kuva](assets/cover.webp)

Kylmä fyysinen lompakko – 60€ – Aloittelija – Turvaa 2 000€ - 50 000€

Ledger on ranskalainen ratkaisu bitcoinien turvaamiseen yksinkertaisella tavalla.

Tässä oppaassa keskustelemme myös salasanojen osiosta, joka on edistynyt turvaratkaisu suurten summien säilyttämiseen: 20 000€ – 100 000€.

https://www.youtube.com/watch?v=_vsHNTLi8MQ

# Yhdistä Ledger Sparrow Bitcoin -lompakkoon (kirjoitusopas)

Varmista, että olet käynyt läpi toisen osan “Bitcoin-laitelompakoiden käyttö” ensin. Tulen sivuuttamaan joitakin vaiheita ja keskittymään pääasiassa siihen, mikä on erityistä Ledgerille tässä.

## Laitteen asettaminen

Ledgerin mukana tulee oma USB-kaapeli. Varmista, että käytät sitä etkä mitä tahansa vanhaa kaapelia. Jotkut USB-kaapelit ovat vain virtaa varten. Tämä lähettää sekä dataa ETTÄ virtaa. Kun olen käyttänyt laitetta puhelimen latauskaapelilla, laite ei ole onnistunut yhdistämään.

Yhdistä se tietokoneeseesi ja laite käynnistyy.

![kuva](assets/1.webp)

Käy läpi vaihtoehdot. Näet

1. Aseta uutena laitteena
2. Palauta palautuslauseesta

Käytännössä se kysyy, haluatko laitteen luovan sinulle siemenen vai onko sinulla jo sellainen, jota haluaisit käyttää. On parasta käytäntöä luoda oma siemenesi, mutta sen turvallinen tekeminen on hyvin edistynyttä ja tämän artikkelin ulkopuolella. Valitse “Aseta uutena laitteena”

Sinua pyydetään sitten valitsemaan PIN-koodi. Tämä ei ole osa Bitcoin-siementäsi ja on spesifinen vain tälle laitteelle. Se lukitsee laitteen.

Sen jälkeen se esittelee sinulle 24 sanaa, jotka sinun täytyy käydä läpi ja kirjoittaa ylös.

Kummallisesti, kun pääset loppuun, se sanoo “painamalla vasemmalle voit tarkistaa sanasi”. Se ei kuvaile, miten vahvistat jatkamisen, se vain tarkoittaa, että voit palata katsomaan sanoja uudelleen. Paina sen sijaan oikealle ja vahvista painamalla vasenta ja oikeaa samanaikaisesti.

Seuraava osa on todella ärsyttävä. Se sekoittaa 24 sanaa ja sinun täytyy vahvistaa jokainen, 1:stä 24:ään, käymällä läpi kaikki sanat kunkin valinnan kohdalla. Kun olet valmis, se sallii sinun vahvistaa kahden painikkeen painalluksella ja jatkaa.

![kuva](assets/2.webp)

Näet kojelaudallasi, että sinulla on asetuspainike ja plus-merkkipainike, joka sallii sovellusten asentamisen. Mutta sinun täytyy ensin yhdistää Ledger Liveen. Teemme sen seuraavaksi…

## Lataa Ledger Live

Voisit ladata Ledger Liven heidän verkkosivultaan, mutta parempi on hankkia se GitHubista, missä lähdekoodi sijaitsee.

Google “ledger live GitHub” tai klikkaa tätä linkkiä https://github.com/LedgerHQ/ledger-live-desktop

![kuva](assets/3.webp)

Vieritä alas, kunnes näet otsikon, “Lataukset”…

![kuva](assets/4.webp)

Alhaalla näet linkin: Ohjeet asennuspakettien hashin ja allekirjoitusten tarkistamiseen löytyvät tältä sivulta. Klikkaa tuota linkkiä.(https://live.ledger.tools/lld-signatures)

![kuva](assets/5.webp)

Ylhäällä on linkkivaihtoehtoja tarvitsemallesi ohjelmistopaketille riippuen käyttöjärjestelmästäsi. Klikkaa sopivaa ladataksesi.

Seuraavaksi haluamme varmistaa latauksen hashin, lisäturvallisuuden vuoksi.
Ledger julkaisee kunkin tällä sivulla saatavilla olevan tiedoston hash-arvon. Aiomme nyt hashata latauksen ja verrata tulosta. Sen on oltava identtinen varmistaaksemme, että tiedostoa ei ole manipuloitu.

Avaa terminaali Macissa tai CMD Windowsissa. Noudata näitä komentoja...

cd Downloads

<Enter>

```bash
shasum -a 512 ledger-live-desktop-2.32.2-mac.dmg # <--- Macille
certutil -hashfile ledger-live-desktop-2.32.2-win.exe SHA512 # <--- Windowsille
```

<Enter>

Toivottavasti on ilmeistä, että komennot alkavat nuolien jälkeen. Varmista, että jos tämä artikkeli on vanhentunut, vaihdat komentojen tiedostonimen täsmälleen lataamasi tiedostonimeen. Sinun on painettava <Enter>-näppäintä jokaisen komennon jälkeen. Kuten tässä näkyy, komennot eivät ehkä mahdu yhdelle riville verkkoselaimessasi. Huomaa, että kaikki on kirjoitettu yhdelle riville.

Katso hashin tulostetta ja varmista, että se on identtinen GitHubissa julkaistun kanssa.

Ihanteellisesti haluat mennä vielä pidemmälle ja varmistaa, että julkaistut hashit eivät ole väärennettyjä. Teemme tämän gpg-allekirjoitusten avulla, mutta se on tämän artikkelin ulkopuolella. Jos haluat oppia siitä (ja ehdotan, että opit lopulta), tutustu tähän artikkeliin.

## Yhdistä Ledger Liveen

Ennen kuin käynnistät Ledger Liven, yksityisyytesi kannalta on hyödyllistä kytkeä VPN päälle. Ledger saa edelleen kaikki osoitteesi, mutta he eivät tiedä IP-osoitettasi, joka paljastaa kotiosoitteesi. Mullvad VPN on erinomainen VPN-palvelu eikä se ole kovin kallis (en mainosta, se on vain mitä käytän).

Asenna ohjelmisto tietokoneellesi ja käynnistä se.

![kuva](assets/6.webp)

Valitse laitteesi ja valitse "Ensimmäistä kertaa käytössä..."

![kuva](assets/7.webp)

Sinut viedään läpi asennusvelhon, mutta olemme jo tehneet kaikki nämä vaiheet, joten voit vain seurata.

![kuva](assets/8.webp)

Monen vaiheen ja tietovisan jälkeen se tarkistaa laitteen aitouden. Sinun on varmistettava, että olet yhdistetty ja syöttänyt PIN-koodin, ja sitten laite kysyy, salliiko se Ledger Liven yhdistämisen. Sinun on vahvistettava se, tietenkin.

![kuva](assets/9.webp)

Seuraavassa ponnahdusikkunassa oli jonkin verran shitcoin-mainontaa naamioituna "julkaisutiedotteiksi". Ohita se, ja sitten sinun pitäisi päästä tähän näyttöön.

![kuva](assets/10.webp)

Sinun on napsautettava "Lisää tili" saadaksesi Bitcoin-lompakon.

![kuva](assets/11.webp)

Varmista, että valitset Bitcoinin, etkä Bitcoin Cashia tai mitään muuta shitcoinia. Se tarkistaa laitteen, ja sinun on vahvistettava jatkaminen LAITTEESSA. Se laskee osoitteita pari minuuttia. Sitten klikkaa VALMIS.

![kuva](assets/12.webp)
![kuva](assets/13.webp)

Hienoa. Nyt sinulla on shitcoin-lompakonhallintaohjelma, joka sisältää Bitcoin-lompakon tietokoneellasi. Itse asiassa et tarvitse tätä enää ja voit hankkiutua eroon siitä. Todellinen tarkoitus oli saada Bitcoin-sovellus itse laitteeseen, ja tämä oli ainoa tapa, lyhyesti sanottuna suorittamatta joitakin äärimmäisiä ohjelmistosuunnittelutekniikoita.

Muista, että aiemmin laitteessa oli asetuspainike ja plus-merkkipainike. Nyt meillä on ylimääräinen painike – Bitcoin-sovelluspainike.

Voit sammuttaa Ledger Liven nyt.

## Lisää salasana
Nyt kun meillä on Bitcoin-sovellus, voimme lisätä salasanan siemenlauseeseemme. Emme voineet tehdä sitä aiemmin, kun siemen oli ensin luotu, koska alussa meillä ei ollut Bitcoin-sovellusta, ja meidän piti yhdistää Ledger Liveen saadaksemme sen.

Siirry laitteen "asetukset"-valikkoon, sitten alavalikkoon "turvallisuus". Valitse sitten salasana. Näet "Edistynyt ominaisuus". Klikkaa oikeaa painiketta, näet "lue manuaali..." ja sitten oikean painikkeen klikkauksen jälkeen, näet "takaisin". Mutta se ei ole loppu. Vaistomaisesti ajattelisit niin, mutta klikkaa oikeaa painiketta uudelleen. Näet "asettaa salasanan".

Voit päättää "liittää PIN-koodiin" tai "Asettaa väliaikaisesti". Suosittelen "liittämistä PIN-koodiin". Näin voit päästä käsiksi eri lompakoihin riippuen siitä, minkä PIN-koodin syötät laitteen ensimmäisessä käynnistyksessä. Jos "asetat väliaikaisesti", sinun on syötettävä salasana joka kerta, kun haluat päästä käsiksi kyseiseen lompakkoon, mutta se on aina oletus-PIN-koodista.

Syötä salasana ja vahvista se.

Se pyytää sinulta "Nykyistä PIN-koodia". Tämä ei ole PIN-koodi, jonka liität uuteen salasanaan. Se on PIN-koodi, jonka syötit laitteen käynnistyessä tähän istuntoon.

Voit nyt poistua päävalikkoon valitsemalla takaisin-vaihtoehdon muutaman kerran.

## Lompakon seuranta

Aiemmissa artikkeleissa selitin, miten ladata ja varmistaa Sparrow-lompakko, ja miten yhdistää se omaan solmuun tai julkiseen solmuun. Sinun tulisi seurata näitä ohjeita:

- Asenna Bitcoin Core (https://armantheparman.com/bitcoincore/)

- Asenna Sparrow Bitcoin Wallet (https://armantheparman.com/download-sparrow/)

- Yhdistä Sparrow Bitcoin Wallet Bitcoin Coreen (https://armantheparman.com/sparrowcore/)

Vaihtoehto Sparrow Bitcoin Walletin käytölle on Electrum Desktop Wallet, mutta jatkan Sparrow Bitcoin Walletin selittämistä, koska pidän sitä parhaana useimmille ihmisille. Edistyneet käyttäjät saattavat pitää Electrumia vaihtoehtona.

Ladataan se nyt ja yhdistetään Ledger, jossa on lompakko, joka sisältää salasanan. Tätä lompakkoa ei ole koskaan altistettu Ledger Livelle, koska se luotiin SEN JÄLKEEN, kun laite oli yhdistetty Ledger Liveen. Varmista, ettet koskaan yhdistä sitä Ledger Liveen uudelleen, jotta et altista uutta yksityistä lompakkoasi.

Luo uusi lompakko:

![kuva](assets/14.webp)

Nimeä se joksikin kauniiksi

![kuva](assets/15.webp)

Huomaa valintaruutu, "On olemassa olevia tapahtumia". Jos tämä on lompakko, jota olet käyttänyt aiemmin, niin valitse tämä, muuten saldosi näkyy virheellisesti nollana. Tämän ruudun valitseminen pyytää Sparrow'ta tutkimaan Bitcoin Coren tietokantaa (lohkoketjua) aiemmista tapahtumista. Tätä opasta varten käytämme upouutta lompakkoa, joten voit jättää ruudun valitsematta.

Klikkaa "Yhdistetty laitteistolompakko" ja varmista, että laite on todella yhdistetty, päällä, PIN-koodi syötetty, ja olet avannut Bitcoin-sovelluksen.

Klikkaa "Skannaa" ja sitten "Tuo avainvarasto" seuraavalla näytöllä.

![kuva](assets/18.webp)

Seuraavalla näytöllä ei ole mitään muokattavaa, Ledger on täyttänyt sen puolestasi. Klikkaa "Käytä"

![kuva](assets/19.webp)
Seuraava näyttö mahdollistaa salasanan lisäämisen. Älä sekoita tätä "salalauseeseen"; monet ihmiset tekevät niin. Nimeäminen on valitettavaa. Salasana mahdollistaa tämän lompakon lukitsemisen tietokoneellasi. Se on spesifinen tälle ohjelmistolle tällä tietokoneella. Se ei ole osa Bitcoinin yksityisavaintasi.
![kuva](assets/20.webp)

Tauon jälkeen, kun tietokone miettii, näet vasemmalla olevien painikkeiden vaihtuvan harmaasta siniseksi. Onnittelut, lompakkosi on nyt valmis käytettäväksi. Tee ja lähetä transaktioita sydämesi kyllyydestä.

![kuva](assets/21.webp)

## Vastaanottaminen

Vastaanottaaksesi joitakin bitcoineja, mene Vasemmalla olevaan Osoitteet-välilehteen ja valitse yksi osoitteista vastaanottamiseen. Klikkaa oikealla osoitetta, jonka haluat, ja valitse "kopioi osoite". Mene sitten vaihtopalveluun, josta raha lähetetään, ja liitä se sinne. Tai voit antaa osoitteen asiakkaalle, joka voi käyttää sitä maksamiseen sinulle.

Kun käytät lompakkoa ensimmäistä kertaa, sinun pitäisi vastaanottaa hyvin pieni määrä, harjoitella sen lähettämistä toiseen osoitteeseen, joko lompakon sisällä tai takaisin vaihtoon, todistaaksesi, että lompakko toimii odotetusti.

Kun olet tehnyt sen, sinun on varmuuskopioitava sanat, jotka kirjoitit ylös. Yksi kopio ei riitä. Pidä vähintään kaksi paperikopiota (metalli on parempi), ja säilytä ne kahdessa eri, hyvin turvatussa paikassa. Tämä vähentää luonnonkatastrofin riskiä tuhota HWW ja paperivarmuuskopio yhdessä tapahtumassa. Katso "Bitcoinin laitteistolompakoiden käyttö" täydellistä keskustelua varten.

## Lähettäminen

![kuva](assets/22.webp)

Maksua tehdessäsi sinun on liitettävä osoite, johon maksat, "Maksa" -kenttään. Et voi jättää Tunniste-kenttää tyhjäksi, se on vain omien lompakkojesi kirjanpitoa varten, mutta Sparrow ei salli sitä - kirjoita vain jotain (vain sinä näet sen). Syötä summa ja voit myös manuaalisesti säätää haluamaasi maksua.

Lompakko ei voi allekirjoittaa transaktiota, ellei HWW ole yhdistetty. Se on HWW:n tehtävä - vastaanottaa transaktio, allekirjoittaa se ja antaa sen takaisin allekirjoitettuna. Varmista, kun allekirjoitat laitteella, että visuaalisesti tarkistat maksamasi osoitteen olevan sama laitteessa ja tietokoneen näytöllä, sekä saamasi laskun (esim. saatat olla saanut sähköpostin maksamaan tiettyyn osoitteeseen).

Kiinnitä myös huomiota siihen, että jos valitset maksun määrää suuremman kolikon, loput lähetetään takaisin yhteen lompakkojesi vaihto-osoitteista. Jotkut ihmiset eivät ole tienneet tätä ja ovat tarkistaneet transaktionsa julkisessa lohkoketjussa, ja luulleet, että jotkin bitcoinit on lähetetty hyökkääjän osoitteeseen, mutta itse asiassa se oli heidän oma vaihto-osoitteensa.

## Firmware

Firmwaren päivittämiseksi sinun on yhdistettävä Ledger Liveen. Jos haluat tehdä tämän, sinun pitäisi pyyhkiä laite ensin ja varmistaa, että sinulla on varmuuskopiosanasi ja salalauseesi saatavilla laitteen palauttamiseksi. Syy, miksi haluan pyyhkiä laitteen ensin, on se, että sinun on yhdistettävä laitteesi Ledger Liveen firmwaren päivittämiseksi, ja mieluummin en altista uutta lompakkoani (se, jossa on salalause) Ledger Livelle koskaan. En vain luota, että Ledger ei poimi julkista avaintietoani laitteesta, kun yhdistän sen Ledger Liveen. He väittävät, etteivät tee niin, mutta en voi varmistaa sitä itse, ellei lue koodia ja ymmärrä sisäistä laitteistoa.

## Yhteenveto
Tämä artikkeli näytti sinulle, miten käyttää Ledger HWW:tä turvallisemmin ja yksityisemmin kuin mainostetaan – mutta pelkkä tämä artikkeli ei riitä. Kuten sanoin alussa, sinun tulisi yhdistää se tietoihin, jotka on annettu artikkelissa "Bitcoin-laitelompakoiden käyttö". Vinkkejä:

Staattinen Lightning-osoite: dandysack84@walletofsatoshi.com
https://armantheparman.com/ledgersparrow/


Syventääksesi tätä aihetta ja vahvistaaksesi lompakkosi turvallisuutta Ledger Nano -laitteessa BIP39 passphrase:lla, suosittelen tutustumaan tähän kattavaan oppaaseen:

https://planb.network/tutorials/wallet/hardware/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49
