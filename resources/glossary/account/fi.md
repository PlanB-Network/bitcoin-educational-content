---
termi: TILI
---

HD (Hierarkkisesti Deterministisissä) lompakoissa tili edustaa johdannaiskerrosta syvyydessä 3 BIP32:n mukaisesti. Jokainen tili on järjestetty peräkkäin alkaen `/0'/` (kovennettu johdannainen, joten todellisuudessa `/2^31/` tai `/2 147 483 648/`). Juuri tässä johdannaisyvyydessä sijaitsevat tunnetut `xpubit`. Nykyään HD-lompakossa käytetään tyypillisesti vain yhtä tiliä. Alun perin ne oli kuitenkin suunniteltu erottamaan erilaiset käyttöluokat saman lompakon sisällä. Esimerkiksi, jos otamme standardin johdannaispolun ulkoiselle Taproot (P2TR) vastaanotto-osoitteelle: `m/86'/0'/0'/0/0`, tilin indeksi on toinen `/0'/`.

![](../../dictionnaire/assets/17.png)