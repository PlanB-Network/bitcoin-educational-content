---
term: BIP0145

definition: Aktualizace volání JSON-RPC getblocktemplate pro integraci podpory SegWit a výpočet váhy transakcí.
---
Aktualizuje volání JSON-RPC `getblocktemplate` tak, aby obsahovalo podporu pro SegWit v souladu s BIP141. Tato aktualizace umožňuje těžařům sestavovat bloky s ohledem na nové měření "váhy" transakcí a bloků zavedené systémem SegWit a další parametry, jako je výpočet limitu sigops.