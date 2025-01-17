---
term: BLOCK

---
Bitcoin-järjestelmän tietorakenne. Lohko sisältää joukon voimassa olevia transaktioita ja sen otsikkoon sisältyviä metatietoja. Kukin lohko liittyy seuraavaan lohkoon sen otsikon hash-tiedon avulla, mikä muodostaa lohkoketjun. Lohkoketju toimii aikaleimapalvelimena, jonka avulla jokainen käyttäjä voi tietää kaikki aiemmat transaktiot, jotta voidaan todentaa, ettei transaktiota ole ja estää kaksinkertainen rahankäyttö. Transaktiot järjestetään Merkle-puuhun. Tämä kryptografinen akkumulaattori mahdollistaa lohkon kaikkien transaktioiden digestin tuottamisen, jota kutsutaan "Merkle-juureksi" Lohkon otsikko sisältää 6 elementtiä:


- Lohkon versio;
- Edellisen lohkon jälki;
- Tapahtumien Merkle-puun juuri;
- Lohkon aikaleima;
- Vaikeuskohde;
- Nonce.

Jotta lohko olisi kelvollinen, siinä on oltava otsikko, joka tuottaa `SHA256d`:llä hajautetun version, joka on pienempi tai yhtä suuri kuin vaikeustavoite.