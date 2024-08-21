---
termi: OBOE (OFF-BY-ONE ERROR)
---

Looginen virhe, jossa silmukka iteroi yhden kerran liikaa tai yhden kerran liian vähän, usein väärän vertailuoperaattorin käytön tai tietorakenteiden hallinnassa olevien indeksien virheellisen käytön vuoksi. Bitcoinin kontekstissa tämä bugi löytyy tapauksessa, jossa `OP_CHECKMULTISIG`-operaatiossa virheellisesti kulutetaan ylimääräinen elementti, jota kutsutaan "*dummy elementiksi*".

> ► *Suomeksi tämä termi voidaan kääntää "yhdellä viallinen virheeksi".*