---
term: NULLDUMMY
---

Konsensus-sääntö, joka otettiin käyttöön BIP147:n yhteydessä SegWit-ohjelmistopäivityksessä ja joka vaatii, että `OP_CHECKMULTISIG` ja `OP_CHECKMULTISIGVERIFY` operaatiokoodeissa käytetty tyhjäelementti on tyhjä tavutaulukko (`OP_0`). Tämä toimenpide toteutettiin poistamaan muunneltavuusvektori kieltämällä mikä tahansa arvo paitsi `OP_0` tälle elementille.