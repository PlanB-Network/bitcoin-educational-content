---
term: ELLIPTIC CURVE

---
Kryptografiassa elliptinen käyrä on algebrallinen käyrä, joka on määritelty yhtälöllä muodossa $y^2 = x^3 + ax + b$. Näitä käppyröitä käytetään elliptisen käyrän kryptografiassa (Elliptic Curve Cryptography, ECC), joka on julkisen avaimen kryptografiamenetelmä, jonka avulla voidaan luoda salausalgoritmeja, digitaalisia allekirjoituksia ja avaintenvaihtomekanismeja. Bitcoinin yhteydessä ECDSA:ta (*Elliptic Curve Digital Signature Algorithm*) tai Schnorr-protokollaa käytetään `secp256k1`-käyrän kanssa. Tämä käyrä valittiin sen suorituskyvyn ja turvallisuusominaisuuksien vuoksi. Näitä algoritmeja käytetään julkisten avainten tuottamiseen yksityisistä avaimista sekä transaktioiden allekirjoittamiseen ja siten bitcoinien avaamiseen.