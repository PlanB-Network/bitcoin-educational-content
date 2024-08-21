---
termi: ELLIPTINEN KÄYRÄ
---

Kryptografian kontekstissa elliptinen käyrä on algebrallinen käyrä, joka määritellään yhtälöllä $y^2 = x^3 + ax + b$. Näitä käyriä käytetään elliptisen käyrän kryptografiassa (ECC), joka on julkinen avainkryptografian menetelmä, jonka avulla voidaan luoda salausalgoritmeja, digitaalisia allekirjoituksia ja avaintenvaihtomekanismeja. Bitcoinin yhteydessä käytetään ECDSA:ta (*Elliptic Curve Digital Signature Algorithm*) tai Schnorr-protokollaa `secp256k1` käyrän kanssa. Tämä käyrä valittiin sen suorituskyvyn ja turvallisuusominaisuuksien vuoksi. Näitä algoritmeja käytetään julkisten avainten generoimiseen yksityisistä avaimista sekä transaktioiden allekirjoittamiseen, mikä mahdollistaa bitcoinien lukituksen avaamisen.