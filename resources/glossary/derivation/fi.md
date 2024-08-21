---
termi: DERIVATION
---

Viittaa prosessiin, jossa lapsiavainpareja (yksityinen avain ja julkinen avain) ja ketjukoodia tuotetaan vanhemmasta avainparista deterministisessä ja hierarkisessa (HD) lompakossa. Tämä prosessi mahdollistaa haarojen segmentoinnin ja lompakon järjestämisen eri tasoihin lukuisilla lapsiavainpareilla, jotka kaikki voidaan palauttaa tietämällä vain peruspalautustiedot (mnemoninen lause ja mahdollinen salasana). Lapsiavaimen johdannaisessa käytetään `HMAC-SHA512`-funktiota vanhemman ketjukoodin ja vanhemman avaimen sekä 32-bittisen indeksin yhdistelmän kanssa. On olemassa kaksi tyyppiä johdannaisille:
* Normaali johdannainen, joka käyttää vanhemman julkista avainta `HMAC-SHA512`-funktion perustana;
* Kovennettu johdannainen, joka käyttää vanhemman yksityistä avainta `HMAC-SHA512`-funktion perustana;

HMAC-SHA512:n tulos jaetaan kahteen osaan: ensimmäiset 256 bittiä muodostavat lapsiavaimen (yksityinen tai julkinen käsiteltyään ECDSA:n kautta), ja jäljelle jäävät 256 bittiä muodostavat lapsiketjukoodin.