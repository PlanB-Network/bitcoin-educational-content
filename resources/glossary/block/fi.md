---
termi: BLOCK
---

Tietorakenne Bitcoin-järjestelmässä. Lohko sisältää joukon validoitavia transaktioita ja metadataa, joka on sisällytetty sen otsikkoon. Jokainen lohko on linkitetty seuraavaan sen otsikon hashin kautta, muodostaen näin lohkoketjun. Lohkoketju toimii aikaleimaa antavana palvelimena, joka mahdollistaa jokaisen käyttäjän tietää kaikki menneet transaktiot, jotta voidaan varmistaa transaktion olemattomuus ja estää kaksinkertainen kulutus. Transaktiot on järjestetty Merkle-puuhun. Tämä kryptografinen kumulaattori mahdollistaa kaikkien lohkon transaktioiden tiivisteen tuottamisen, jota kutsutaan "Merkle-juureksi". Lohkon otsikko sisältää 6 elementtiä:
* Lohkon versio;
* Edellisen lohkon jäljennös;
* Transaktioiden Merkle-puun juuri;
* Lohkon aikaleima;
* Vaikeustavoite;
* Nonce.

Jotta lohko olisi validi, sen täytyy olla otsikko, joka, kun se hashataan `SHA256d`-algoritmilla, tuottaa tiivisteen, joka on pienempi tai yhtä suuri kuin vaikeustavoite.