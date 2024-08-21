---
term: BIP118
---

Návrh na vylepšení Bitcoinu, který má za cíl zavést dva nové modifikátory SigHash Flag: `SIGHASH_ANYPREVOUT` a `SIGHASH_ANYPREVOUTANYSCRIPT`. Tyto funkce rozšiřují možnosti Bitcoinových transakcí, zejména z hlediska chytrých kontraktů a nadstavbových řešení jako je Lightning Network. BIP118 by významně umožnil použití Eltoo. Hlavní výhodou `SIGHASH_ANYPREVOUT` je umožnění opětovného použití podpisů v rámci více transakcí, což nabízí větší flexibilitu. Konkrétně tyto SigHashes umožňují podpis, který nezahrnuje žádné z vstupů transakce.