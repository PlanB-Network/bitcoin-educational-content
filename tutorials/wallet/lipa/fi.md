---
name: Lipa
description: Lipa lightning -mobiililompakon käyttöönotto ja käyttö
---
![cover](assets/cover.webp)

Bitcoin Lightning -lompakko on mobiilisovellus, joka mahdollistaa välittömät ja edulliset transaktiot Bitcoinin Lightning-verkossa. Toisin kuin päälohkoketjussa (on-chain) tapahtuvat maksut, Lightning-maksut ovat lähes välittömiä ja vaativat minimaaliset maksut, joten ne soveltuvat erityisen hyvin pieniin, jokapäiväisiin maksuihin.

Lightning-lompakoita, kuten kaikkia mobiililompakoita, pidetään "kuumina" lompakkoina, koska ne ovat yhteydessä Internetiin. Siksi ne on tarkoitettu ensisijaisesti pienten rahamäärien hallintaan päivittäisiä menoja varten. Suurempia summia varten on parempi käyttää turvallisempia tallennusratkaisuja, kuten laitteistolompakoita.

Jos haluat oppia lisää Lightning-verkosta ja ymmärtää, miten se toimii teknisesti, suosittelen osallistumaan tälle kurssille:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
Tässä oppaassa tutustumme **Lipaan**, yksinkertaiseen ja tehokkaaseen Sveitsissä kehitettyyn Lightning-lompakkoon.

## Esittelyssä Lipa

Lipa on ei-huolellinen Lightning-lompakko, joka erottuu helppokäyttöisyydellään ja selkeällä käyttöliittymällään. Sveitsiläisen tiimin kehittämässä Lipassa korostuu luottamuksellisuus ja helppokäyttöisyys aloittelijoille.

Tärkeimpiä ominaisuuksia ovat:


- Intuitiivinen käyttöliittymä
- Autonominen salamakanavan hallinta
- LNURL-protokollan tuki
- Mahdollisuus ostaa bitcoineja suoraan sovelluksessa

## Lipan asentaminen ja konfigurointi

Ensimmäinen askel on ladata Lipa-sovellus. Tällä hetkellä se on saatavilla vain iOS-käyttöjärjestelmässä:


- [Applen puolesta](https://apps.apple.com/app/lipa-bitcoin-lightning/id1602180066)

Android-versio on parhaillaan kehitteillä, ja se on pian saatavilla.

![Installation de Lipa](assets/fr/01.webp)

Kun olet käynnistänyt sovelluksen, pääset aloitusnäyttöön, jossa on kaksi vaihtoehtoa:


- Luo uusi salkku
- Palauta olemassa oleva salkku varmuuskopiosta

Kun olet valinnut vaihtoehdon, sovellus pyytää sinua ottamaan ilmoitukset käyttöön. Tämä vaihe on tärkeä, sillä ilmoitukset ovat välttämättömiä :


- Saat ilmoituksia maksujen saapumisesta, vaikka sovellus olisi suljettu
- Saat tietoa vaiheista, jotka liittyvät bitcoinin ostamiseen integroidun ratkaisun kautta

Tämän jälkeen sovellus esittelee tärkeimmät toimintonsa useiden esittelynäyttöjen avulla:


- Saumaton maksun vastaanotto**: Käyttäjät voivat vastaanottaa Bitcoin-maksuja, vaikka sovellus olisi suljettu, mikä takaa luotettavuuden ja mukavuuden.
- Muiden kuin huoltajien salamaosoitteet**: Tämä parantaa yksityisyyttä ja turvallisuutta antamalla käyttäjille täyden hallinnan bitcoineistaan.
- Analyyttisten tietojen valvonta** : Läpinäkyvyys ja luottamuksellisuus ovat etusijalla, joten käyttäjät voivat tarkastella kerättyjen tietojen tyyppejä ja valita jakamisasetukset.
- Lähetä puhelinnumeron kautta**: Valitse yhteyshenkilö, syötä summa ja lähetä bitcoineja suoraan hänen puhelinnumeroonsa.

Sovellus hyötyy myös jatkuvista parannuksista vakauden, turvallisuuden ja luotettavuuden osalta, jotta voidaan taata optimaalinen käyttökokemus.

## Sovelluksen navigointi

Lipan käyttöliittymä on järjestetty neljän päävälilehden ympärille, joihin pääsee näytön alareunassa olevan navigointipalkin kautta:

![Navigation principale](assets/fr/02.webp)


- Koti**: Näyttää nykyisen saldon ja tapahtumahistorian
- Skanneri**: Mahdollistaa QR-koodien skannaamisen maksujen suorittamiseksi
- Kartta**: Näyttää interaktiivisen kartan Bitcoinin hyväksyvistä yrityksistä alueellasi
- Asetukset**: Pääsy sovelluksen asetuksiin, varmuuskopiointiin ja asetuksiin

Lisävalikkoon pääsee vetämällä aloitusnäyttöä alaspäin:

![Menu supplémentaire](assets/fr/03.webp)

Tämä ele paljastaa lisätoimintoja, kuten :


- Bitcoinien ostaminen
- Bitcoin-talletus ketjussa
- Lightning-laskujen luominen bitcoinien vastaanottamiseksi
- Lightning-laskun maksu

## Tallenna salkkusi

Jos haluat varmuuskopioida lompakkosi, siirry "Asetukset"-välilehdelle ja valitse "Elvytyslauseke". Lipa käyttää palautuslausetta, joka on tärkeää kirjoittaa huolellisesti fyysiselle välineelle (paperi, metalli). Tämä lause on ainoa tapa palauttaa rahasi, jos puhelimesi katoaa tai varastetaan. Varmistaaksesi varmuuskopiosi sovellus pyytää sinua vahvistamaan 3 satunnaista sanaa lauseestasi.

![Backup](assets/fr/04.webp)

Jos haluat lisätietoja siitä, miten varmuuskopioida ja hallita palautuslausetta oikein, suosittelen seuraamaan tätä toista opetusohjelmaa, varsinkin jos olet aloittelija:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
## Vastaanottaa bitcoineja

Voit vastaanottaa bitcoineja kahdella tavalla. Pääset näihin vaihtoehtoihin palaamalla aloitusnäyttöön ja vetämällä näyttöä alaspäin. Sitten voit joko :


- Valitse "Siirrä BTC" saadaksesi bitcoineja ketjussa. Skannaa sitten yksinkertaisesti QR-koodi toisella lompakollasi ja suorita maksutapahtuma loppuun.
- Valitse "Pyyntö" saadaksesi maksun Lightning-verkon kautta ja syötä haluamasi summa.

Molemmissa tapauksissa sinun on maksettava maksu, joka vastaa 0,4 % summasta tai noin 2 500 satsia, jos hakemuksen on avattava uusi maksukanava (mikä on väistämättä tilanne ensimmäisen maksun kohdalla).

![Recevoir des bitcoins on chain](assets/fr/05.webp)

![Recevoir des bitcoins lightning](assets/fr/06.webp)

## Lähetä bitcoineja

Jos haluat lähettää bitcoineja, siirry aloitusnäyttöön, vedä näyttöä alaspäin ja valitse "Maksa". Sitten yksinkertaisesti joko :


- anna salaman LNURL-osoite
- skannaa salaman QR-koodi maksaaksesi.

Voit myös siirtyä näytön alareunan toiseen välilehteen skannataksesi QR-koodin suoraan.

![Envoi de bitcoins](assets/fr/07.webp)

## Osta bitcoineja

Lipa tarjoaa mahdollisuuden ostaa bitcoineja suoraan sovelluksessa 1,5 prosentin maksua vastaan. Voit tehdä ostoksen siirtymällä aloitusnäyttöön ja vetämällä alaspäin näyttääksesi valikon. Valitse sitten "Osta BTC". Kolme esittelynäyttöä opastaa sinut ostoprosessin läpi.

![Menu d'achat](assets/fr/08.webp)

Syötä sitten vain sen tilin pankkitiedot, jota aiot käyttää ostoksen tekemiseen. Valitse valuutta ja anna sähköpostiosoitteesi.

Latausnäytön jälkeen näet viitenumeron, joka sisällytetään tulevaan siirtoon, sekä pankkitiedot vaihtoa varten.

![Sélection du montant](assets/fr/09.webp)

Sinun tarvitsee vain siirtää haluamasi summa pankkisi kautta, määrittää siirto ilmoittamalla aiemmin haettu RIB ja ilmoittaa viite tapahtuman aikana, jotta Lipa voi yhdistää tämän pankkiliikkeen Lipa-lompakkoosi.

![Confirmation d'achat](assets/fr/10.webp)

## Edut ja haitat

### Edut


- Intuitiivinen käyttöliittymä
- Oikeat palvelumaksut
- Muu kuin huoltajuus
- Integroitu bitcoin-ostoratkaisu
- BTCmap-integraatio
- NFC-tuki

### Haitat


- Ei ole mahdollista lähettää bitcoineja ketjussa
- Hieman keskimääräistä pidempi maksu

Lipa on erinomainen valinta Lightning-verkon käytön aloittamiseen, ja se sopii erityisesti käyttäjille, jotka etsivät yksinkertaista ratkaisua jokapäiväisiin maksuihin. Sen helppokäyttöisyys ja selkeä käyttöliittymä tekevät siitä ihanteellisen lompakon aloittelijoille, mutta se tarjoaa samalla olennaiset ominaisuudet Lightningin jokapäiväiseen käyttöön.

## Resurssit


- [Lipan virallinen verkkosivusto](https://lipa.swiss/)
- [Lipa-tuki](https://getlipa.atlassian.net/servicedesk/customer/portal/1)