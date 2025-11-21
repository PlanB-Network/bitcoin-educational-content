---
term: BIP0119
---

Uvodi novi opcode nazvan `OP_CHECKTEMPLATEVERIFY` (CTV). CTV bi omogućio kreiranje nerekurzivnih zaveta u transakcijama, kako bi se nametnuli specifični uslovi o tome kako određeni novčić može biti potrošen, uključujući i u budućim transakcijama. Konkretno, omogućio bi definisanje uslova na `scriptPubKey` izlaza transakcije na osnovu `scriptPubKey` UTXO potrošenog kao ulaz. CheckTemplateVerify je dizajniran da bude jednostavan i bez dinamičkog stanja. Njegova implementacija ima za cilj proširenje skriptnih mogućnosti Bitcoin kako bi se olakšale razne primene kao što su kontrola zagušenja transakcija, kreiranje neinteraktivnih platnih kanala, DLC-ova, platnih bazena... Ovaj novi opcode bi bio uveden kao zamena za `OP_NOP4`. Ova promena bi podrazumevala Soft Fork.