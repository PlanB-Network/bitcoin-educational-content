---
term: ASICBOOST
---

ASICBOOST on algoritminen optimointimenetelmä, joka keksittiin vuonna 2016. Se on suunniteltu lisäämään Bitcoin-louhinnan tehokkuutta noin 20 % vähentämällä laskentaa, jota tarvitaan kunkin otsikon hash-yrityksen suorittamiseen. Tämä tekniikka hyödyntää SHA256-hashfunktion ominaisuutta, jota käytetään louhinnassa, ja joka jakaa datan lohkoihin ennen niiden käsittelyä. ASICBOOST säilyttää yhden näistä lohkoista muuttumattomana useiden hash-yritysten ajan, mahdollistaen louhijan suorittaa vain osan tämän lohkon työstä useiden yritysten aikana. Tämä datan jakaminen mahdollistaa aiempien laskelmien tulosten uudelleenkäytön, vähentäen siten kokonaislaskentamäärää, joka tarvitaan kelvollisen hashin löytämiseen.

ASICBOOST voidaan käyttää kahdessa muodossa: Avoimessa ASICBOOSTissa ja Piilotetussa ASICBOOSTissa. Avoimessa ASICBOOST-muodossa se on kaikkien nähtävissä, koska se sisältää `nVersion`-kentän käyttämisen noncena, muuttamatta todellista `Nonce`-arvoa. Piilotettu muoto pyrkii piilottamaan nämä muutokset käyttämällä Merkle-puita. Tämä toinen menetelmä on kuitenkin muuttunut vähemmän tehokkaaksi SegWitin käyttöönoton jälkeen toisen Merkle-puun vuoksi, mikä lisää laskentamäärää, jota sen käyttö vaatii.

Yhteenvetona, ASICBOOST mahdollistaa louhijoiden olla suorittamatta todellista täydellistä SHA256-laskentaa kaikille hash-yrityksille, koska osa tuloksesta pysyy muuttumattomana, mikä nopeuttaa louhijoiden työtä.