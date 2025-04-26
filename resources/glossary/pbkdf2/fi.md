---
term: PBKDF2

---
`PBKDF2` tarkoittaa *Password-Based Key Derivation Function 2*. Se on menetelmä, jolla salausavaimia luodaan salasanasta käyttäen johdannaisfunktiota. Se ottaa syötteenä salasanan, salakirjoitussuolan ja soveltaa iteratiivisesti ennalta määritettyä funktiota (usein hash-funktiota kuten `SHA256` tai `HMAC`) näihin tietoihin. Tämä prosessi toistetaan useita kertoja salausavaimen luomiseksi.

Bitcoinin yhteydessä `PBKDF2`:ta käytetään yhdessä `HMAC-SHA512`-funktion kanssa luomaan deterministisen ja hierarkkisen lompakon siemen (siemen) 12 tai 24 sanan palautuslauseesta. Tässä tapauksessa käytetty salakirjoitussuola on BIP39-salasana, ja iteraatioiden määrä on `2048`.