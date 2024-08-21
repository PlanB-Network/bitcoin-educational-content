---
term: NULLDUMMY
---

Konsensuse reegel, mis tutvustati BIP147-ga SegWiti pehmes lõhestuses, nõuab, et dummy element, mida kasutatakse `OP_CHECKMULTISIG` ja `OP_CHECKMULTISIGVERIFY` opkoodides, peab olema tühi baitide massiiv (`OP_0`). See meede rakendati, et kõrvaldada muudetavuse vektor, keelates mis tahes muu väärtuse peale `OP_0` selle elemendi jaoks.