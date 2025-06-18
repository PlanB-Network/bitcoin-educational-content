---
term: Commitment
---

Commitment (kryptografisessa merkityksessä) on matemaattinen objekti, jota merkitään $C$ ja joka saadaan deterministisesti strukturoituun dataan $m$ (viesti) kohdistuvasta operaatiosta ja satunnaisarvosta $r$. Kirjoitamme :


$$
C = \text{commit}(m, r)
$$


Tämä mekanismi koostuu kahdesta päätoiminnosta:




- Sitoutuminen: Sovellamme salausfunktiota viestiin $m$ ja satunnaiseen $r$ ja saamme tulokseksi $C$ ;
- Tarkista: käytämme $C$:tä, $m$-viestiä ja $r$-arvoa tarkistaaksemme, että tämä Commitment on oikein. Funktio palauttaa `True` tai `False`.


Commitment:n on noudatettava kahta ominaisuutta:




- Sitovuus: on oltava mahdotonta löytää kahta eri viestiä, jotka tuottavat saman $C$ :


$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$


Kuten :


$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$




- Piilottelu: $C$:n tietäminen ei saa paljastaa $m$:n sisältöä.


RGB-protokollan tapauksessa Commitment sisältyy Bitcoin-tapahtumaan, jotta voidaan todistaa tietyn tiedon olemassaolo tiettynä ajankohtana paljastamatta itse tietoa.