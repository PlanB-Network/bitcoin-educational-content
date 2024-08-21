---
term: SIGHASH_ANYPREVOUT
---

Návrh na implementaci nového modifikátoru SigHash Flag v Bitcoinu, představený s BIP118. `SIGHASH_ANYPREVOUT` umožňuje větší flexibilitu v řízení transakcí, zejména pro pokročilé aplikace jako jsou platební kanály na Lightning Network a aktualizace Eltoo. `SIGHASH_ANYPREVOUT` umožňuje, aby podpis nebyl vázán na žádný konkrétní předchozí UTXO (*Jakýkoliv Předchozí Výstup*). Použití v kombinaci s `SIGHASH_ALL` by umožnilo podepsat všechny výstupy transakce, ale žádné z vstupů. To by umožnilo opětovné použití podpisu pro různé transakce, pokud jsou splněny určité specifikované podmínky.

> ► *Tento modifikátor SigHash SIGHASH_ANYPREVOUT je odvozen z myšlenky SIGHASH_NOINPUT, kterou původně navrhl Joseph Poon v roce 2016, aby rozšířil svůj koncept Lightning Network.*