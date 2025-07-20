---
term: LIBSECP256K1
---

Suorituskykyinen ja erittäin turvallinen C-kirjasto digitaalisia allekirjoituksia ja muita kryptografisia alkutekijöitä varten `secp256k1` elliptisellä käyrällä. Koska tätä käyrää ei ole koskaan käytetty laajasti Bitcoin:n ulkopuolella (toisin kuin usein suosittua `secp256r1`-käyrää), tämän kirjaston tarkoituksena on olla kattavin viite sen käytöstä. Libsecp256k1:n kehitys suunnattiin ensisijaisesti Bitcoin:n tarpeisiin, ja muihin sovelluksiin tarkoitettuja ominaisuuksia saatetaan testata tai todentaa vähemmän. Tämän kirjaston asianmukainen käyttö vaatii huolellista huomiota, jotta voidaan varmistaa, että se soveltuu muidenkin sovellusten kuin Bitcoin:n erityistarkoituksiin.


Libsecp256k1-kirjasto tarjoaa useita ominaisuuksia, kuten:




- ECDSA-secp256k1 allekirjoitus ja todentaminen sekä salausavaimen luominen ;
- Additiiviset ja multiplikatiiviset operaatiot salaisille ja julkisille avaimille ;
- Salaisten avainten, julkisten avainten ja allekirjoitusten sarjallistaminen ja analysointi ;
- Julkisen avaimen allekirjoittaminen ja tuottaminen jatkuvassa ajassa ja jatkuvalla muistin käytöllä;
- Ja monia muita salausmenetelmiä.