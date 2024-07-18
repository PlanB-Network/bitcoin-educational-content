---
name: Phoenix

description: Phoenix-lompakon käyttöönotto
---

![phoenix](assets/cover.webp)

## Johdanto

Phoenix on Acinq-tiimin, Lightning Eclair -toteutuksen takana olevan tiimin, luoma ei-holhottava lightning-lompakko.

Muista, että Phoenix on mobiilisovellus, joka keskittyy Lightning-maksuihin, mutta tukee silti on-chain-maksuja integroitujen vaihtojen kautta. Tämä tarkoittaa, että kaikki on-chain-talletukset Phoenixiin vaihdetaan välittömästi Lightning-kanavaksi.

Jos haluat lähettää on-chain-osoitteeseen, Phoenix suorittaa vaihdon sisäisesti LN-kanavaltasi on-chain-kohteeseen. Ole tietoinen, että kaikilla näillä vaihdoilla on kustannuksensa, koska ne sisältävät on-chain-maksun.

Alla "Aloitusoppaan" osiossa käymme läpi asennusprosessin ja selitämme lisää siitä, miten hallita lightning-likviditeettiä Phoenixissa.

## Tärkeät resurssit
- Phoenixin virallinen verkkosivu - [https://phoenix.acinq.co](https://phoenix.acinq.co)
- Dokumentaatio / UKK-sivu - [https://phoenix.acinq.co/faq](https://phoenix.acinq.co/faq)
- [Github-sivu](https://github.com/ACINQ/phoenix/) | [Githubin julkaisusivu](https://github.com/ACINQ/phoenix/releases) (lataa apk suoraan)
- [Tuki ja keskustelut](https://github.com/ACINQ/phoenix/discussions)
- [Acinq-blogi](https://acinq.co/blog) - ilmoitukset

## Video-ohje

![Phoenix: Bitcoin Lightning Wallet Tutorial](https://youtu.be/cbtAmevYpdM?si=zctujxtI0hI-jKpC)

## Aloitusopas

Tässä on vaiheittainen opas Phoenixin aloittamiseen, asennukseen, maksujen tekemiseen/vastaanottamiseen, likviditeetin hallintaan, varmuuskopioinnin/palauttamisen prosessiin.

### Lataa & Asenna
Voit ladata ja asentaa Phoenixin: [App Store](https://apps.apple.com/us/app/phoenix-wallet/id1544097028) | [Google Play Store](https://play.google.com/store/apps/details?id=fr.acinq.phoenix.mainnet) | [Suora apk-lataus](https://github.com/ACINQ/phoenix/releases)

Noudata ohjeita alkaen Tervetuloa-näytöstä, vaihe vaiheelta.

![](assets/screenshot2.webp)

Sinulle kerrotaan automaattisesta lightning-kanavien luomisesta.
Aloittaen versiosta 2.0 on merkittävä päivitys, joka tuo "splicing"-ominaisuuden Phoenixiin:
- yksi dynaaminen kanava,
- ei enää 1% maksua sisääntulevasta likviditeetistä
- parempi ennustettavuus ja hallinta
- luottamuksettomat vaihdot

Tarkista [Phoenixin blogikirjoitus](https://acinq.co/blog/phoenix-splicing-update) lisätietoja varten, erityisesti uusi maksu malli.

![](assets/screenshot3.webp)

### Likviditeetin pikakatsaus

Joten kun vastaanotat / talletat satseja tähän lompakkoon, se automaattisesti avaa kanavia ACINQ-noden kanssa. Yleensä kanavien koko on hieman suurempi kuin tallettamasi summa. Joten sinulla on aina uusi kanava jokaiselle talletukselle, paitsi kun sinulla on vielä käyttämätöntä kanavaa ja vastaanotat pienemmän maksun, se täytetään uudelleen.

Phoenix Lightning -likviditeetin osalta ehdottaisimme seuraavaa skenaariota:

Uudella versiolla v0.2.0 uusi LN-ominaisuus splicing tarkoittaa, että sinun ei enää tarvitse käsitellä monia uusia pieniä kanavia jokaisesta vastaanotetusta maksusta.

Jos sisääntuleva likviditeetti ei ole riittävä, Phoenix kasvattaa alkuperäisen kanavasi kokoa, mutta se edellyttää silti onchain-maksua. Voit asettaa tämän maksun joka tapauksessa Phoenixin asetuksissa, maksuvaihtoehdoissa ja maksuissa.
Joten ehdotamme aloittamaan Phoenixin käytön suurella kanavalla, kuten 1-3-5M sats. Sitoutumismaksusi ovat merkityksettömiä verrattuna kanavan kokoon, eivätkä ne vaikuta sinuun liikaa. Sen sijaan, että maksaisit 4-5 kertaa (tai kuinka monta kertaa talletat pieniä määriä) vähintään 3000 satsin maksun jokaisesta talletuksesta, maksat vain kerran kanavan avaamismaksun.
Jos aloitat kuluttamisen kyseiseltä kanavalta, älä kuluta kaikkea, sillä Phoenix sulkee sen.

Jos jätät joitakin satseja kanavalle ja teet toisen täydennyksen toisesta LN-lompakosta / talletuslähteestä, meillä on kaksi tilannetta harkittavana:
- uudella talletussummalla, joka on suurempi kuin kanavasi kapasiteetti, Phoenix muuttaa kanavan kokoa ja sinun on maksettava ylimääräinen maksu.
- uudella talletussummalla, joka on pienempi kuin kanavasi kapasiteetti, ei tule maksuja.

Yritä siis mitoittaa alkuperäinen kanavasi kapasiteetti henkilökohtaisiin kulutustarpeisiisi. Kuluttaminen ja korvaaminen kanavan rajoissa ei aiheuta enää maksuja ja kokemus tämän lompakko-sovelluksen käytöstä on sujuva.

### Varmuuskopio
Seuraavalla näytöllä sinulle ilmoitetaan, että Phoenix-sovellus luo siemenlauseen lompakkosi varmuuskopioksi. Myöhemmin nämä siemen sanat ON tallennettava turvalliseen paikkaan!

![](assets/screenshot4.webp)

Seuraava näyttö ilmoittaa, haluatko luoda uuden lompakon vai palauttaa aiemman lompakon siemenlauseesta.

![](assets/screenshot5.webp)

Kun uusi lompakko on luotu, sinulle ilmoitetaan, että sinun pitäisi tehdä varmuuskopio siemenlauseesta. Klikkaa "Varmuuskopioi lompakko" -painiketta.

![](assets/screenshot6.webp)

Sinulle ilmoitetaan, että nämä siemen sanat ovat erittäin tärkeitä ja arkaluonteisia ja sinun pitäisi pitää ne yksityisinä.

![](assets/screenshot7.webp)

Nämä siemen sanat SINUN ON tallennettava turvalliseen paikkaan, kuten salasanojen hallintaohjelmaan ([KeePass](https://keepass.info/) tai [Bitwarden](https://bitwarden.com/)), pitäen tämän salasanojen hallintaohjelman tietokannan offline USB-salatussa tikussa täydellisen turvallisuuden varmistamiseksi.

![](assets/screenshot8.webp)

### Maksujen vastaanottaminen

Ennen kuin aloitat vastaanottamisen, lue edellä oleva luku "Liquidity Quick Guide".

Nyt olet valmis vastaanottamaan satseja Phoenix-lompakkoosi!

![](assets/screenshot9.webp)

Maksun vastaanottamiseksi Phoenixissa sinulla on seuraavat vaihtoehdot:
- käyttämällä näytöllä olevaa QR-koodia, joka edustaa "tyhjää" Lightning-laskua
- muokkaamalla Lightning-laskua (katso muokkauspainike QR-koodin alla), jossa voit lisätä satseja, lisätä kommentin maksajalle näkyviin
- käyttämällä / skannaamalla LNURL-withdraw QR-koodia
- luomalla on-chain Bitcoin-osoitteen Phoenix-lompakostasi. Muista, että tämä maksu "muunnetaan" uudeksi Lightning-kanavaksi (jos et ole vielä avannut yhtä) tai muuttaa olemassa olevan Lightning-kanavan kokoa.

![](assets/screenshot10.webp)

Näyttö, joka näytetään uuden Lightning-laskun muokkaamiseksi ja uuden QR-koodin luomiseksi sille:

![](assets/screenshot11.webp)

Tämä on näyttö, jossa voit luoda on-chain BTC-osoitteen ja sinulle ilmoitetaan, että maksu tähän osoitteeseen "muunnetaan" lightning-likviditeetiksi ja siihen liittyy joitakin maksuja.

![](assets/screenshot12.webp)

Kun maksu on suoritettu, näytetään vahvistusnäyttö, kaikki tehty!

![](assets/screenshot13.webp)
Voit halutessasi lisätä henkilökohtaisen huomautuksen jokaiseen vastaanotettuun maksuun. Nämä huomautukset eivät tallennu mihinkään muualle, vaan säilyvät ainoastaan laitteessasi. Jos palautat Phoenix-lompakkosi, näitä huomautuksia ei palauteta. Tämä on hyödyllinen ominaisuus pitääksesi kirjaa lähettämistäsi ja vastaanottamistasi maksuista.
![](assets/screenshot14.webp)

### Maksujen lähettäminen

Maksujen lähettäminen on melko yksinkertainen prosessi, klikkaa vain päänäytön "Lähetä"-painiketta

![](assets/screenshot15.webp)

Sinua pyydetään sallimaan Phoenix-sovelluksen pääsy laitteen kameraan, jotta voit skannata QR-koodeja.

![](assets/screenshot16.webp)

Maksunäytössä on 3 vaihtoehtoa:
- skannaa QR-koodi vastaanottajan Lightning-laskusta / LNURL-osoitteesta
- syötä manuaalisesti (liitä), Lightning-osoitteen syöttö tai LNURL-pay koodi
- lataa QR-kuva paikalliselta levyltä

![](assets/screenshot17.webp)

Kuten tässä näytössä näet, maksupyyntö on skannattu ja tiedot on jo täytetty. Sinun tarvitsee vain painaa "Maksa"-painiketta.

![](assets/screenshot18.webp)

Kun maksu on lähetetty ja vahvistettu, näytölle tulee vahvistusnäyttö, jossa on maksun lyhyet tiedot, mukaan lukien maksettu palkkio. Jos haluat nähdä lisää maksutietoja, klikkaa "Tiedot"-painiketta.

![](assets/screenshot19.webp)

Tiedot-näytössä voit nähdä maksun tekniset tiedot, mukaan lukien: maksun hash ja pyyntö, preimage, kohdesolmu ja kesto. Joskus nämä tiedot ovat hyödyllisiä maksujen seuraamisessa, vianmäärityksessä tai tietyn maksun tunnistamisessa vastaanottajan kanssa.

![](assets/screenshot20.webp)

### Asetukset

Asetusvalikossa ei ole paljoa tehtävää, Phoenix panostaa yksinkertaisuuteen. Mutta yksi tärkeä kohta täällä on valikko maksukanavien ja palkkioiden hallintaan, jossa voit asettaa haluamasi palkkiotason. Muista, että korkean palkkion mempool-ympäristössä sinun ei pitäisi käyttää erittäin matalia palkkioita, muuten maksusi ja kanavien avaamiset voivat häiriintyä ja/tai epäonnistua.

Muita asetusvalikon vaihtoehtoja:
- Näyttö - vaihda eri väriteemoihin
- Electrum-palvelin - tarkista yhteydessä olevan Electrum-palvelimen tila tai määritä yksi
- Tor - jos haluat käyttää Phoenixia Tor-verkon takana
- Sovelluksen käyttöoikeusasetukset - aseta Phoenixille tietyt laitepalvelujen käyttöoikeudet
- Palautuslause - jos haluat tarkistaa siemenlauseet ja/tai tehdä uuden varmuuskopion
- Kanavien lista - näytä Lightning-kanaviesi tila ja saatavilla oleva likviditeetti (sisään/ulos)
- Lokit - näytä vianmäärityslokit
- Sulje kaikki kanavat - Vaarallinen vaihtoehto, jota tulisi käyttää VAIN, jos haluat pysäyttää Phoenix-solmusi lopullisesti ja palauttaa varat onchain-osoitteeseesi. Kyseisen osoitteen voi myöhemmin hakea käyttämällä Electrum-lompakkoa ja Phoenix-siemenlausetta.

![](assets/screenshot21.webp)

### Nollaus

Jos olet tilanteessa, jossa Phoneix-sovelluksesi on ongelmissa (ei tee maksuja, ei yhdistä Electrum-palvelimiin, ei voi vastaanottaa maksuja) tai haluat yksinkertaisesti siirtää sen toiseen laitteeseen, sinun TÄYTYY olla varma kahdesta asiasta:
- sinulla on varmuuskopio siemenlauseestasi
- pysäytä sovellus laitteessasi - mene sovelluksen tietoihin ja pakota palvelu pysähtymään
- poista se vanhasta laitteesta, jos haluat siirtää sen uuteen
- ÄLÄ aja samaa Phoenix-lompakkoa useilla laitteilla!

![](assets/screenshot22.webp)

Kun asennat sen uudelleen tai uuteen laitteeseen, klikkaa "Palauta"-painiketta ja noudata ohjeita

![](assets/screenshot23.webp)
Et voi käyttää toisen tyyppistä siementä, joka on luotu muilla lompakko-sovelluksilla. [Lue lisää täältä](https://walletsrecovery.org/) eri lompakkotyypeistä ja niiden siementyypeistä sekä johdannaispoluista. Kaikki eivät ole yhteensopivia!
![](assets/screenshot24.webp)

Sinun on syötettävä aiemmin tallennetut siemensanat yksi kerrallaan, tietyssä järjestyksessä. Kun olet lopettanut 12 sanan syöttämisen, klikkaa "Tuo" -painiketta ja valmis.

![](assets/screenshot25.webp)

Muutamassa hetkessä näet aiemman saldosi näytöllä. Saat myös ilmoituksen siemenen varmuuskopioinnista. Voit vain mennä valikkoon ja valita "Olen tallentanut varmuuskopion", jos olet jo tehnyt sen.

![](assets/screenshot26.webp)

Valmista! Iloista Lightning-käyttöä!