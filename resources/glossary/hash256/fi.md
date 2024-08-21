---
termi: HASH256
---

Kryptografinen funktio, jota käytetään eri sovelluksissa Bitcoinissa. Se sisältää SHA256-funktion soveltamisen kahdesti syötetietoihin. Viesti kulkee SHA256:n läpi kerran, ja tämän toimenpiteen tulos käytetään syötteenä toiselle läpikäynnille SHA256:ssa. Tämän funktion tuloksena on siis 256 bittiä.

$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$