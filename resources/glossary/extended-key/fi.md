---
termi: LAJENNETTU AVAIN
---

Merkkijono, joka yhdistää avaimen (julkinen tai yksityinen), siihen liittyvän ketjukoodin ja joukon metatietoja. Lajennettu avain kokoaa kaikki lapsiavainten johdannaisiin tarvittavat elementit yhteen tunnisteeseen. Niitä käytetään deterministisissä ja hierarkkisissa lompakoissa ja ne voivat olla kahta tyyppiä: laajennettu julkinen avain (käytetään johdannaisten julkisten avainten johtamiseen) tai laajennettu yksityinen avain (käytetään sekä johdannaisten yksityisten että julkisten avainten johtamiseen). Lajennettu avain sisältää siis useita erilaisia tietoja, jotka on kuvattu BIP32:ssa, seuraavassa järjestyksessä:
* Etuliite: `prv` ja `pub` ovat HRP:tä (Human Readable Part), jotka osoittavat, onko kyseessä laajennettu yksityinen avain (`prv`) vai laajennettu julkinen avain (`pub`). Etuliitteen ensimmäinen kirjain määrittää laajennetun avaimen version: `x` Legacylle tai SegWit V1:lle Bitcoinissa, `t` Legacylle tai SegWit V1:lle Bitcoin Testnetissä, `y` Nested SegWitille Bitcoinissa, `u` Nested SegWitille Bitcoin Testnetissä, `z` SegWit V0:lle Bitcoinissa, `v` SegWit V0:lle Bitcoin Testnetissä.
* Syvyys, joka osoittaa johdannaisten määrän pääavaimesta laajennettuun avaimen saavuttamiseksi;
* Vanhemman sormenjälki. Tämä edustaa vanhemman julkisen avaimen `HASH160`:n ensimmäisiä 4 tavua;
* Indeksi. Tämä on parin numero sen sisarusten joukossa, josta laajennettu avain on johdettu;
* Ketjukoodi;
* Täytebitti, jos kyseessä on yksityinen avain `0x00`;
* Yksityinen tai julkinen avain;
* Tarkistussumma. Se edustaa laajennetun avaimen lopun `HASH256`:n ensimmäisiä 4 tavua.

Käytännössä laajennettua julkista avainta käytetään vastaanotto-osoitteiden luomiseen ja tilin tapahtumien tarkkailuun ilman, että siihen liittyviä yksityisiä avaimia paljastetaan. Tämä voi mahdollistaa esimerkiksi niin kutsutun "vain katselu" -lompakon luomisen. On kuitenkin tärkeää huomata, että laajennettu julkinen avain on käyttäjän yksityisyyden kannalta arkaluonteista tietoa, sillä sen paljastaminen voi sallia kolmansien osapuolien seurata tapahtumia ja nähdä liitetyn tilin saldon.