---
term: SCHNORR (PROTOKOLLA)

---
Schnorr-protokolla on sähköisen allekirjoituksen algoritmi, joka perustuu elliptisen käyrän salaukseen (ECC). Sitä käytetään Bitcoinissa julkisen avaimen johtamiseen yksityisestä avaimesta ja transaktion allekirjoittamiseen yksityisellä avaimella. Bitcoinissa Schnorr perustuu ECDSA:n tavoin elliptisen käyrän `secp256k1` käyttöön, jota luonnehtii yhtälö: $y^2 = x^3 + 7$. Schnorr-allekirjoitusprotokolla on toteutettu Bitcoin-protokollassa marraskuusta 2021 lähtien Taproot-päivityksen aktivoinnin myötä.