---
termi: HMAC-SHA512
---

`HMAC-SHA512` tarkoittaa "Hash-based Message Authentication Code - Secure Hash Algorithm 512". Se on kryptografinen algoritmi, jota käytetään viestien eheyden ja aitouden varmistamiseen kahden osapuolen välillä. Se yhdistää kryptografisen tiivistefunktion `SHA512` jaetun salaisen avaimen kanssa luodakseen ainutlaatuisen viestin autentikointikoodin (MAC) jokaiselle viestille.

Bitcoinin kontekstissa `HMAC-SHA512`:n käyttö on hieman erilaista. Tätä algoritmia käytetään lompakon kryptografisen avainpuun deterministisessä ja hierarkkisessa johdatusprosessissa. `HMAC-SHA512` on erityisesti käytössä siirryttäessä siemenestä pääavaimen luomiseen ja sitten jokaisessa johdannaisessa vanhemmasta parista lapsipareihin. Tämä algoritmi löytyy myös toisesta johdatusalgoritmista nimeltä `PBKDF2`, jota käytetään siirtymään palautuslausekkeesta ja salasanasta siemeneen.