---
name: Bitfinex - Yritys
description: Yritystilin luominen ja hallinta Bitfinexissä
---
![cover](assets/cover.webp)

Vuonna 2012 perustettu Bitfinex on yksi ensimmäisistä bitcoin- ja altcoin-vaihtofoorumeista. Alun perin se keskittyi P2P-bitcoin-pörsseihin, mutta laajensi nopeasti palveluitaan kattamaan marginaalikaupan, P2P-rahoituksen, johdannaiskaupan ja OTC-markkinat ("*over-the-counter*") suurten volyymien transaktioita varten.

Nykyään Bitfinex on täydellinen alusta, joka mahdollistaa sekä yksinkertaiset bitcoinien ostot että kehittyneiden kaupankäyntitoimintojen (perinteinen kaupankäynti, johdannaiset, OTC, lainaaminen jne.) ja riskinhallintatyökalujen käytön. Se on saatavilla verkkoversiona, ja yksinkertaisia liiketoimia varten on saatavilla myös helppokäyttöinen mobiilisovellus.

Tässä oppaassa käsittelemme yritystilin luomista Bitfinexiin, bitcoinien ostamista ja myymistä, transaktioiden hallintaa kirjanpitoa varten sekä eurojen ja bitcoinien tallettamista ja nostamista. Tavoitteena on antaa sinulle perustiedot, suunnittelitpa sitten Bitcoinin sisällyttämistä kassavirtaasi tai Bitcoinin hyväksymistä maksuvälineenä.

Jos olet kiinnostunut bitcoinin integroimisesta yritykseesi, suosittelen myös tutustumaan täydelliseen teoreettiseen koulutuskurssiimme aiheesta:

https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a
## 1 - Bitfinex-tilin luominen

Mene [Bitfinexin viralliselle verkkosivustolle](https://www.bitfinex.com/). Etsi etusivulta "*Sign Up*"-vaihtoehto ja napsauta sitä aloittaaksesi tilin luomisen. Aluksi luot tavallisen tilin kuin yksityishenkilöille, "*Corporate*"-vaihtoehto valitaan myöhemmin vahvistusprosessin aikana.

![BITFINEX](assets/fr/01.webp)

Täytä vaaditut tiedot: anna yrityksesi sähköpostiosoite ja yrityksesi kotimaa. Valitse turvallinen käyttäjätunnus ja salasana ja vahvista rekisteröinti napsauttamalla "*Tilaa*".

![BITFINEX](assets/fr/02.webp)

Vinkkejä vahvojen ja yksilöllisten salasanojen käyttöön ja suojaamiseen on myös tässä oppaassa :

https://planb.network/tutorials/others/general/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9
Määritämme nyt 2FA:n tilin suojaamiseksi. Käytä älypuhelimessa olevaa todennussovellusta, kuten esimerkiksi Google Authenticatoria tai Authyta. Löydät ohjeen tästä työkalusta täältä :

https://planb.network/tutorials/others/general/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7
Skannaa QR-koodi sovelluksellasi ja syötä annetut 6 numeroa.

![BITFINEX](assets/fr/03.webp)

Rekisteröinti on suoritettu.

![BITFINEX](assets/fr/04.webp)

Tarkista postilaatikkosi ja klikkaa Bitfinexin lähettämää linkkiä vahvistaaksesi rekisteröitymisesi.

![BITFINEX](assets/fr/05.webp)

Tilisi on nyt luotu. Klikkaa "*Log in*" päästäksesi alustalle.

![BITFINEX](assets/fr/06.webp)

## 2 - Yritystilin vahvistaminen

Bitfinex soveltaa nykyisten säännösten mukaista todentamisprosessia (KYC). "Basic"-tilassa on mahdotonta tehdä talletuksia, joten on välttämätöntä hankkia vähintään "Intermediate"-varmistustaso tai tarvittaessa jopa "Full"-varmistustaso.

Kun tilisi on luotu, ponnahdusikkunan pitäisi ehdottaa, että vahvistat tilisi. Napsauta "*Varmenna*".

![BITFINEX](assets/fr/07.webp)

Jos tämä ikkuna ei tule näkyviin, siirry profiiliisi käyttöliittymän oikeassa yläkulmassa ja napsauta sitten "*Verification*".

![BITFINEX](assets/fr/08.webp)

Valitse "*Tilityyppi*" -kohdasta "*Yritys*". Omassa tapauksessani päivitän tilini "*Intermediate*" -tasolle, joten valitsen "*Upgrade to Intermediate*".

![BITFINEX](assets/fr/09.webp)

Suorita vaiheet loppuun antamalla :


- Yrityksen tiedot (yrityksen nimi, yhteystiedot, toimiala jne.) ;
- Oikeudelliset asiakirjat (yhtiöjärjestys, Kbis-ote, luettelo johtajista ja osakkeenomistajista);
- KYC-tiedot kustakin tosiasiallisesta edunsaajasta tai johtajasta (henkilöllisyysasiakirjat, osoitetodistus jne.).

Kun hakemuksesi on täytetty ja lähetetty, voi kestää useita päiviä, ennen kuin foorumi vahvistaa sen yritystodennusta varten. Tänä aikana talletukset ovat tilapäisesti estettyinä.

![BITFINEX](assets/fr/10.webp)

## 3 - Pikaesittely Bitfinexin käyttöliittymään

Kun olet kirjautunut sisään, näet käyttöliittymän yläosassa navigointipalkin, jossa on: "*Trading*", "*Derivatives*", "*Funding*", "*OTC*", "*P2P*", "*Wallet*", jne. Bitfinex tarjoaa laajan valikoiman toimintoja, kuten :


- Kaupankäynti**: "*klassinen*" markkina, jossa voit tehdä tilauksia ostaa ja myydä kryptovaluuttoja (mukaan lukien bitcoin) ;
- OTC**: Over-The-Counter-palvelu, jossa suurilla volyymeillä käydään kauppaa suoraan toisen toimijan kanssa julkisten tilauskirjojen ulkopuolella;
- Rahoitus**: Luotonantoon ja marginaalirahoitukseen tarkoitettu alue;
- Johdannaiset**: Johdannaisia (futuurit jne.) käsittelevä osio, joka on tarkoitettu kokeneille kauppiaille;
- P2P**: Mahdollistaa kryptojen ostamisen tai myymisen muilta käyttäjiltä vertaisverkkopohjaisesti.

Tavalliseen käyttöön (bitcoinien osto/myynti, talletukset/nostot ja käteisvarojen hallinta) käytät pääasiassa "*Trading*"-välilehteä sekä "*Wallet*"-, "*Deposit*"- ja "*Withdraw*"-osioita.

![BITFINEX](assets/fr/11.webp)

Yrityskaavan toinen etu on mahdollisuus luoda alatilejä. Tämä tarkoittaa, että voit antaa useille käyttäjille pääsyn näihin alatileihin, ja jokaisella käyttäjällä on tietyt oikeudet (vain luku, kaupankäynti, vain talletus jne.).

## 4 - Eurojen tallettaminen ja nostaminen (fiat)

Jos haluat tallettaa euroja Bitfinex Corporate -tilillesi, avaa "*Talletus*"-alavalikko, joka sijaitsee käyttöliittymän yläreunan "*Lompakko*"-valikossa.

![BITFINEX](assets/fr/12.webp)

Valitse "*Pankkisiirto*" tai "*Luotto-/pankkikortti*" tehdessäsi talletuksen euroissa (tai muussa valuutassa).

![BITFINEX](assets/fr/13.webp)

Valitse lähetettävä fiat-valuutta, esim. euro. Jos käytät vain "*Trading*"-perustoimintoja, valitse "*Exchange*". Ilmoita myös summa, jonka haluat tallettaa, ja liiketilipankkisi maa.

![BITFINEX](assets/fr/14.webp)

Tee siirto yrityksen pankkitililtäsi Bitfinexin ilmoittamalle pankkitilille.

Jos haluat nostaa varoja, menettely on samanlainen: siirry "*Nosto*"-alavalikkoon.

![BITFINEX](assets/fr/15.webp)

Klikkaa "*Pankkisiirto*".

![BITFINEX](assets/fr/16.webp)

Valitse fiat-valuutta, jonka haluat nostaa, Bitfinexissä veloitettava tili ("*Exchange*", jos käytät vain perusominaisuuksia) ja nostettava summa.

![BITFINEX](assets/fr/17.webp)

Bitfinex voi vaatia pankkitilisi vahvistamista ennen siirron hyväksymistä sääntöjenmukaisuussyistä.

![BITFINEX](assets/fr/18.webp)

Kun menettely on aloitettu, Bitfinex siirtää varat pankkitilillesi.

## 5 - Bitcoinien tallettaminen ja nostaminen

Jos haluat tallettaa bitcoineja Bitfinexiin, siirry "*Talletus*"-alavalikkoon.

![BITFINEX](assets/fr/19.webp)

Napsauta "*Cryptocurrency*".

![BITFINEX](assets/fr/13.webp)

Valitse "*BTC*". Vastaanottava osoite tulee näkyviin. Kopioi tämä osoite ja käytä sitä omasta lompakostasi tai jostain muusta alustasta BTC:n lähettämiseen.

![BITFINEX](assets/fr/20.webp)

Jos haluat nostaa bitcoineja, siirry "*Nosto*"-alavalikkoon.

![BITFINEX](assets/fr/21.webp)

Napsauta "*Cryptocurrency*".

![BITFINEX](assets/fr/22.webp)

Valitse "*BTC*". Valitse Bitfinex-tili, jota veloitetaan kotiutusta varten ("*Exchange*" perustoiminnoille). Anna summa ja bitcoinien määränpääosoite. Muista tarkistaa nosto-osoite virheiden välttämiseksi.

![BITFINEX](assets/fr/23.webp)

Vahvistuksen jälkeen bitcoinisi siirretään. Huomaa, että maksut ja viiveet voivat vaihdella mempoolin ruuhkautumisesta riippuen.

Bitfinex tarjoaa myös talletus- ja nostovaihtoehtoja Lightning-verkon kautta, mikä mahdollistaa nopeammat ja halvemmat transaktiot.

![BITFINEX](assets/fr/24.webp)

Jos olet kiinnostunut Lightning-verkosta, meillä on myös täydellinen koulutus, jonka avulla voit ymmärtää, miten se toimii:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
## 6 - Bitcoinien ostaminen ja myyminen Bitfinexissä

Bitfinex tarjoaa erilaisia kaupankäyntitapoja. Jos haluat helppokäyttöisyyttä, valitse klassiset spot-markkinat, jotka tunnetaan myös nimellä "*Trading*" tai "*Exchange*". Täällä voit antaa osto- tai myyntitoimeksiantoja markkinahintaan tai asettaa rajahinnan.

Napsauta ylävalikossa kohtaa "*Trading*".

![BITFINEX](assets/fr/25.webp)

Valitse pari "*BTC/EUR*", jos haluat ostaa tai myydä BTC:tä esimerkiksi euroja vastaan.

![BITFINEX](assets/fr/26.webp)

Käyttöliittymässä näkyy keskellä hintakaavio, alhaalla tilauskirja ja vasemmalla puolella toimeksiantojen syöttömoduuli. Toimeksiantojen syöttöosiossa voit valita joko "*Market*"-toimeksiannon (toteutetaan välittömästi parhaaseen saatavilla olevaan hintaan) tai "*Limit*"-toimeksiannon (määrittelet itse hinnan). Ilmoita ostettavan tai myytävän BTC:n määrä tai valitse prosenttiosuus saldostasi. Klikkaa sitten "*Osta*" ostaaksesi tai "*Myydä*" myydäksesi.

![BITFINEX](assets/fr/27.webp)

Voit tarkastella suoritettujen toimeksiantojen historiaa käyttöliittymän alaosassa.

![BITFINEX](assets/fr/28.webp)

## 7 - Tapahtumahistorian vienti ja kirjanpito

Kirjanpitoa varten sinun on vietävä tiedot tapahtumista (ostot, myynnit, talletukset, nostot). Bitfinex tarjoaa kattavan raportointityökalun. Napsauta profiilikuvaketta käyttöliittymän oikeassa yläkulmassa ja valitse sitten "*Raportit*"-valikko.

![BITFINEX](assets/fr/29.webp)

Vasemmalla voit valita vietävien tietojen tyypin. Valitsemalla esimerkiksi "*Trades*" pääset käsiksi kaikkiin kauppoihisi.

![BITFINEX](assets/fr/30.webp)

Määritä haluamasi ajanjakso "*Date*"-kentässä ja tarvittaessa rajoita haku yhteen tai useampaan tiettyyn pariin "*Symbol*"-kentässä.

![BITFINEX](assets/fr/31.webp)

Voit viedä nämä tiedot napsauttamalla "*Vie*"-painiketta.

![BITFINEX](assets/fr/32.webp)

Tarkista parametrit ja vahvista vienti.

![BITFINEX](assets/fr/33.webp)

Raportti lähetetään sähköpostitse CSV-tiedostona Bitfinex-tiliin liitettyyn osoitteeseen.

![BITFINEX](assets/fr/34.webp)

Kun tiedosto on viety, voit liittää sen kirjanpito-ohjelmistoosi tai lähettää sen tilintarkastajalle.

## 9 - Yrityksen käyttötapaukset

Bitfinexin käyttö voi vaihdella yrityksesi tavoitteista ja rakenteesta riippuen.

### Bitcoinien ostaminen käteisellä

**Tavoite:** Monipuolistaa yrityksen kassavirtaa sijoittamalla bitcoiniin.

**Seuraavat vaiheet:**


- Talleta euroja Bitfinexiin yrityksen pankkitililtä;
- Käytä näitä euroja bitcoinin ostamiseen;
- Pidä bitcoineja alustalla tai vedä ne pois turvataksesi ne omassa säilytyksessä;
- Vie tapahtumahistoriat tarpeen mukaan.

### Bitcoinin hyväksyminen maksuvälineeksi

**Tavoite:** Tarjoa yrityksellesi mahdollisuus hyväksyä bitcoinia maksuvälineenä tuotteillesi tai palveluillesi.

**Seuraavat vaiheet:**


- Integroi bitcoin-maksujärjestelmä. Pienille yrityksille voi riittää yksinkertainen lompakko-ohjelmisto, tai voit valita erikoistuneita ratkaisuja, kuten Swiss Bitcoin Pay tai BTCPay Server, jotta voit integroida bitcoinin maksuvaihtoehtona verkkosivustollesi tai myyntipisteeseen;
- Siirrä bitcoineina vastaanotetut maksut Bitfinex-tilillesi;
- Rahoitusstrategiastasi riippuen voit myydä saamasi bitcoinit euroiksi, säilyttää ne mahdollista tulevaa arvonnousua varten tai valita molempien yhdistelmän;
- Pidä bitcoineja alustalla tai nosta ne itsesäilytystä varten. Voit myös nostaa euroja pankkitilillesi;
- Vie tapahtumahistoriat tarpeen mukaan.

Jos haluat syvällisemmin tarkastella tätä aihetta, Suosittelen tätä kattavaa koulutusta integrointiin Bitcoin yrityksiin, joka kattaa yksityiskohtaisesti lisäämällä kassavirran, hyväksymällä Bitcoin maksut, ja kirjanpito :

https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a