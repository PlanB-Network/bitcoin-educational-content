---
term: OP_CHECKHASHVERIFY (CHV)
---

Nový operační kód navržený v roce 2012 v BIP17 Lukem Dashjrem, který by nabízel stejné funkce jako `OP_EVAL` nebo P2SH. Jeho účelem bylo zahashovat konec `scriptSig`, porovnat výsledek s vrcholem zásobníku a označit transakci za neplatnou, pokud se dva hashe neshodovaly. Tento operační kód nebyl nikdy implementován.