---
termi: BIP143
---

Esittelee uuden tavan transaktion hashaukseen allekirjoituksen varmentamiseksi post-SegWit-skripteissä. Tavoitteena on vähentää toistuvia operaatioita varmennuksen aikana ja sisällyttää UTXOjen arvo sisääntulossa allekirjoitukseen. Tämä ratkaisee kaksi merkittävää ongelmaa alkuperäisessä transaktion hashausalgoritmssa:
* Datan hashauksen neliöllinen kasvu allekirjoitusten määrän myötä;
* Sisääntulon arvon puuttuminen allekirjoituksesta, mikä aiheutti riskin laitteistolompakoille, erityisesti transaktiomaksuihin liittyvän tiedon osalta.
Koska SegWit-päivitys, joka selitetään BIP141:ssä, esittelee uuden tyyppisiä transaktioita, joiden skriptiä vanhat solmut eivät varmenna, BIP143 käyttää tätä tilaisuutta hyväkseen käsitelläkseen tätä ongelmaa vaatimatta kovaa haarukkaa. Siksi BIP143 on osa SegWit-ohjelmistopäivitystä.