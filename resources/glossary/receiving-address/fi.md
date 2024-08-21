---
termi: VASTAANOTTO-OSOITE
---

Tieto, jota käytetään bitcoinien vastaanottamiseen. Osoite luodaan yleensä hashaamalla julkinen avain käyttäen `SHA256` ja `RIPEMD160`, ja lisäämällä metadata tähän tiivisteeseen. Vastaanotto-osoitteen luomiseen käytetyt julkiset avaimet ovat osa käyttäjän lompakkoa ja siksi johdettu heidän siemenestään. Esimerkiksi SegWit-osoitteet koostuvat seuraavista tiedoista:
* HRP merkitsemään "bitcoin": `bc`;
* Erotin: `1`;
* Käytetyn SegWitin versio: `q` tai `p`;
* Payload: julkisen avaimen tiiviste (tai suoraan julkinen avain Taprootin tapauksessa);
* Tarkistussumma: BCH-koodi.

Vastaanotto-osoite voi kuitenkin edustaa myös jotain muuta riippuen käytetystä skriptimallista. Esimerkiksi P2SH-osoitteet rakennetaan käyttäen skriptin hashaa. Taproot-osoitteet sisältävät toisaalta muokatun julkisen avaimen suoraan hashaamatta sitä.

Vastaanotto-osoite voidaan esittää joko alfanumeerisena merkkijonona tai QR-koodina. Jokaista osoitetta voidaan käyttää useita kertoja, mutta tämä käytäntö on erittäin suositeltavaa välttää. Yksityisyyden tason ylläpitämiseksi on suositeltavaa käyttää kutakin Bitcoin-osoitetta vain kerran. Jokaiseen saapuvaan maksuun lompakkoon tulisi luoda uusi osoite. Osoite koodataan `Bech32`:lla SegWit V0 -osoitteille, `Bech32m`:llä SegWit V1 -osoitteille ja `Base58check`:lla Legacy-osoitteille. Teknisestä näkökulmasta bitcoinien vastaanottaminen tarkoittaa yksityisen avaimen omistamista, joka liittyy julkiseen avaimeseen (ja siten osoitteeseen). Kun joku vastaanottaa bitcoineja, lähettäjä päivittää olemassa olevan rajoituksen heidän kulutuksestaan niin, että nyt vain vastaanottajalla on tämä valta.

![](../../dictionnaire/assets/23.png)