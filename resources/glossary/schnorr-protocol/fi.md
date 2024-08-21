---
termi: SCHNORR (PROTOKOLLA)
---

Schnorr-protokolla on elektroninen allekirjoitusmenetelmä, joka perustuu elliptiseen käyräkryptografiaan (ECC). Sitä käytetään Bitcoinissa julkisen avaimen johdattamiseen yksityisestä avaimesta sekä transaktion allekirjoittamiseen yksityisellä avaimella. Bitcoinissa, kuten ECDSA:ssa, Schnorr perustuu elliptisen käyrän `secp256k1` käyttöön, jota karakterisoi yhtälö: $y^2 = x^3 + 7$. Schnorrin allekirjoitusprotokolla on otettu käyttöön Bitcoin-protokollassa marraskuussa 2021 Taproot-päivityksen aktivoitumisen myötä.