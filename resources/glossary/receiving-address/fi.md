---
term: VASTAANOTTAVA OSOITE

---
Tiedot, joita käytetään bitcoinien vastaanottamiseen. Osoite muodostetaan tavallisesti hasshaalaamalla julkinen avain käyttäen `SHA256` ja `RIMPEMD160` ja lisäämällä metatietoja tähän digestiin. Vastaanottavan osoitteen rakentamiseen käytetyt julkiset avaimet ovat osa käyttäjän lompakkoa, joten ne on johdettu hänen siemenestään. Esimerkiksi SegWit-osoitteet koostuvat seuraavista tiedoista:


- HRP "bitcoinin" nimeämistä varten: `bc`;
- Erotin: `1`;
- Käytetty SegWit-versio: tai `p`;
- Hyötykuorma: julkisen avaimen digesti (tai suoraan julkinen avain, jos kyseessä on Taproot);
- Tarkistussumma: BCH-koodi.

Vastaanottava osoite voi kuitenkin edustaa myös jotain muuta käytetystä komentosarjamallista riippuen. Esimerkiksi P2SH-osoitteet muodostetaan komentosarjan hash:n avulla. Taproot-osoitteet taas sisältävät viritetyn julkisen avaimen suoraan ilman hash:ia.

Vastaanottava osoite voidaan esittää aakkosnumeerisena merkkijonona tai QR-koodina. Kutakin osoitetta voidaan käyttää useita kertoja, mutta tämä on erittäin varottava käytäntö. Tietyn yksityisyyden tason säilyttämiseksi on suositeltavaa käyttää kutakin Bitcoin-osoitetta vain kerran. Uusi osoite olisi luotava jokaista lompakkoon saapuvaa maksua varten. Osoite koodataan `Bech32`:lla SegWit V0 -osoitteiden osalta, `Bech32m`:llä SegWit V1 -osoitteiden osalta ja `Base58check`:llä Legacy-osoitteiden osalta. Teknisestä näkökulmasta bitcoinien vastaanottaminen tarkoittaa, että sinulla on julkiseen avaimeen (ja siten osoitteeseen) liittyvä yksityinen avain. Kun joku vastaanottaa bitcoineja, lähettäjä päivittää nykyiset rahankäyttöä koskevat rajoitukset niin, että vain vastaanottajalla voi nyt olla tämä valta.

![](../../dictionnaire/assets/23.webp)