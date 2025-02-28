---
term: NULLDUMMY

---
Konsensussääntö, joka otettiin käyttöön BIP147:n kanssa SegWit soft forkissa ja joka vaatii, että `OP_CHECKMULTISIG`- ja `OP_CHECKMULTISIGVERIFY`-opcodeissa käytettävän dummy-elementin on oltava tyhjä tavujoukko (`OP_0`). Tämä toimenpide otettiin käyttöön muokattavuusvektorin eliminoimiseksi kieltämällä kaikki muut arvot kuin `OP_0` tälle elementille.