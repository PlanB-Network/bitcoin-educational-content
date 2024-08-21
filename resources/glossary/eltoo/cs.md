---
term: ELTOO
---

Obecný protokol pro druhé vrstvy Bitcoinu, který definuje, jak společně spravovat vlastnictví UTXO. Eltoo bylo navrženo Christianem Deckerem, Rustym Russellem a Olaoluwa Osuntokunem, zejména za účelem řešení problémů spojených s mechanismy vyjednávání stavů Lightning kanálů, tedy mezi otevřením a uzavřením. Architektura Eltoo zjednodušuje proces vyjednávání zavedením lineárního systému správy stavů, který nahrazuje zavedený postihový přístup flexibilnější a méně trestnou metodou aktualizace. Tento protokol vyžaduje použití nového typu SigHash, který umožňuje ignorovat všechny vstupy v podpisu transakce. Tento SigHash byl původně nazván `SIGHASH_NOINPUT`, poté `SIGHASH_ANYPREVOUT` (*Jakýkoliv Předchozí Výstup*). Jeho implementace je plánována v BIP118.

> ► *Eltoo je někdy také označováno jako "LN-Symmetry".*