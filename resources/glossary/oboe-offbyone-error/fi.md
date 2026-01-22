---
term: Oboe (off-by-one-virhe)

---
Logiikkavirhe, jossa silmukka iteroi kerran liian monta tai kerran liian vähän, mikä johtuu usein vertailuoperaattoreiden virheellisestä käytöstä tai vääristä indekseistä tietorakenteiden hallinnassa. Bitcoinin yhteydessä tämä virhe esiintyy `OP_CHECKMULTISIG`:n "*dummy-elementin*" tapauksessa, jossa ylimääräinen elementti kulutetaan virheellisesti.

