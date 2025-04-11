---
term: LAAJENNETTU AVAIN

---
Merkkisarja, jossa yhdistyvät avain (julkinen tai yksityinen), siihen liittyvä ketjukoodi ja joukko metatietoja. Laajennettu avain kokoaa kaikki lapsiavainten johtamiseen tarvittavat elementit yhdeksi tunnisteeksi. Niitä käytetään deterministisissä ja hierarkkisissa lompakoissa, ja niitä voi olla kahta tyyppiä: laajennettu julkinen avain (jota käytetään julkisten lapsiavainten johtamiseen) tai laajennettu yksityinen avain (jota käytetään sekä yksityisten että julkisten lapsiavainten johtamiseen). Laajennettu avain sisältää siis useita eri tietoja, jotka on kuvattu BIP32:ssa seuraavassa järjestyksessä:


- Etuliite: `prv` ja `pub` ovat HRP (Human Readable Part, ihmisen luettavissa oleva osa), joka osoittaa, onko kyseessä laajennettu yksityinen avain (`prv`) vai laajennettu julkinen avain (`pub`). Etuliitteen ensimmäinen kirjain ilmaisee laajennetun avaimen version: `x` Legacy- tai SegWit V1 -versiolle Bitcoinissa, `t` Legacy- tai SegWit V1 -versiolle Bitcoin Testnetissä, `y` Nested SegWit -versiolle Bitcoinissa, `u` Nested SegWit -versiolle Bitcoin Testnetissä, `z` SegWit V0 -versiolle Bitcoinissa, `v` SegWit V0 -versiolle Bitcoin Testnetissä.
- Syvyys, joka ilmaisee, kuinka monta johdannaista pääavaimesta on tehtävä laajennettuun avaimeen pääsemiseksi;
- Vanhemman sormenjälki. Tämä edustaa vanhemman julkisen avaimen `HASH160`:n 4 ensimmäistä tavua;
- Indeksi. Tämä on sen parin numero sisarustensa joukossa, josta laajennettu avain on johdettu;
- Ketjukoodi;
- Pehmustetahti, jos kyseessä on yksityinen avain `0x00`;
- Yksityinen tai julkinen avain;
- Tarkistussumma. Se edustaa laajennetun avaimen loppuosan `HASH256`:n 4 ensimmäistä tavua.

Käytännössä laajennettua julkista avainta käytetään vastaanotto-osoitteiden luomiseen ja tilin tapahtumien tarkkailuun paljastamatta siihen liittyviä yksityisiä avaimia. Näin voidaan esimerkiksi luoda niin sanottu "watch-only"-lompakko. On kuitenkin tärkeää huomata, että laajennettu julkinen avain on käyttäjän yksityisyyden kannalta arkaluonteista tietoa, sillä sen paljastuminen voi antaa kolmansille osapuolille mahdollisuuden jäljittää tapahtumia ja nähdä siihen liittyvän tilin saldon.