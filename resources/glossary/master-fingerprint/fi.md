---
termi: PÄÄSORMENJÄLKI
---

4 tavun (32-bittinen) sormenjälki pääyksityisavaimesta Hierarkkisessa Deterministisessä (HD) lompakossa. Se saadaan laskemalla `SHA256`-tiiviste pääyksityisavaimesta, minkä jälkeen seuraa `RIPEMD160`-tiiviste, prosessi jota kutsutaan `HASH160`:ksi Bitcoinissa. Pääsormenjälkeä käytetään HD-lompakon tunnistamiseen, riippumatta johdannaispoluista, mutta ottaen huomioon salasanan läsnäolon tai puuttumisen. Se on tiivis tieto, joka mahdollistaa avainjoukon alkuperän viittaamisen paljastamatta arkaluonteisia tietoja lompakosta.