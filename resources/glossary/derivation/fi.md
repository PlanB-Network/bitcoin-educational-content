---
term: DERIVATION

---
Tarkoittaa prosessia, jossa vanhemman avainparin (yksityinen avain ja julkinen avain) ja ketjukoodin avulla luodaan lapsiavainpareja deterministisessä ja hierarkkisessa (HD) lompakossa. Tämä prosessi mahdollistaa haarojen segmentoinnin ja lompakon organisoinnin eri tasoihin, joissa on lukuisia lapsiavainpareja, jotka kaikki voidaan palauttaa tuntemalla vain palautuksen perustiedot (muistilauseke ja mahdollinen salasana). Lapsiavaimen johtamiseksi käytetään `HMAC-SHA512`-funktiota, jossa on vanhemman ketjun koodi ja vanhemman avaimen ja 32-bittisen indeksin ketjutus. Johdannaisia on kahdenlaisia:


- Normaali derivointi, jossa käytetään vanhempien julkista avainta `HMAC-SHA512`-funktion perustana;
- Kovennettu derivointi, joka käyttää vanhemman yksityistä avainta `HMAC-SHA512`-funktion perustana;

HMAC-SHA512:n tulos jaetaan kahteen osaan: ensimmäiset 256 bittiä ovat lapsiavain (yksityinen tai julkinen ECDSA:n käsittelyn jälkeen) ja loput 256 bittiä ovat lapsen ketjukoodi.