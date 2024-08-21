---
termi: PBKDF2
---

`PBKDF2` tarkoittaa *Password-Based Key Derivation Function 2*:ta. Se on menetelmä kryptografisten avainten luomiseksi salasanasta käyttäen johdannaisfunktiota. Se ottaa syötteenä salasanan, kryptografisen suolan ja soveltaa iteratiivisesti ennalta määrättyä funktiota (usein hash-funktiota kuten `SHA256` tai `HMAC`) näihin tietoihin. Tätä prosessia toistetaan monta kertaa kryptografisen avaimen tuottamiseksi.

Bitcoinin kontekstissa `PBKDF2`:ta käytetään yhdessä `HMAC-SHA512` funktion kanssa luomaan deterministisen ja hierarkisen lompakon (siemen) siemen 12 tai 24 sanan palautusfraasista. Tässä tapauksessa käytetty kryptografinen suola on BIP39-salasana, ja iteraatioiden määrä on `2048`.