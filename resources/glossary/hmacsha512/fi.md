---
term: HMAC-SHA512

---
"HMAC-SHA512" tarkoittaa "Hash-based Message Authentication Code - Secure Hash Algorithm 512". Se on salausalgoritmi, jota käytetään kahden osapuolen välillä vaihdettujen viestien eheyden ja aitouden todentamiseen. Siinä yhdistetään kryptografinen hash-funktio `SHA512` ja jaettu salainen avain, jotta jokaiselle viestille voidaan luoda yksilöllinen Message Authentication Code (MAC).

Bitcoinin yhteydessä `HMAC-SHA512`:n luonnollinen käyttö on hieman johdettu. Tätä algoritmia käytetään lompakon salausavainpuun deterministisessä ja hierarkkisessa johdatusprosessissa. `HMAC-SHA512`:ta käytetään erityisesti siirryttäessä siemenestä pääavaimeen ja sen jälkeen jokaisessa johdannaisessa vanhemmista pareista lapsipareihin. Tätä algoritmia käytetään myös toisessa derivointialgoritmissa nimeltä PBKDF2, jota käytetään siirryttäessä palautuslauseesta ja salasanasta siemeneen.