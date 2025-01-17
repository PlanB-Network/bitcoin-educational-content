---
term: OP_CHECKSIGVERIFY (0XAD)

---
Teostab sama toimingu nagu `OP_CHECKSIG`, kuid kui allkirja kontrollimine ebaõnnestub, peatub skript kohe veaga ja tehing on seega kehtetu. Kui kontrollimine õnnestub, jätkab skript, ilma et stäkki oleks pandud väärtus `1` (true). Kokkuvõttes teostab `OP_CHECKSIGVERIFY` operatsiooni `OP_CHECKSIG`, millele järgneb `OP_VERIFY`. Seda opkoodi muudeti Tapscriptis, et kontrollida Schnorr'i allkirju.