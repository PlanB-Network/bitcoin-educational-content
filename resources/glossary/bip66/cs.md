---
term: BIP66
---

Zavedl standardizaci formátu podpisu v transakcích. Tento BIP byl navržen jako reakce na rozdíly v způsobu, jakým OpenSSL zpracovávalo kódování podpisů na různých systémech. Tato heterogenita představovala riziko rozdělení blockchainu. BIP66 standardizoval formát podpisu pro všechny transakce používající striktní DER kódování (*Distinguished Encoding Rules*). Tato změna vyžadovala soft fork. Pro jeho aktivaci BIP66 použil stejný mechanismus jako BIP34, vyžadující zvýšení pole `nVersion` na verzi 3 a odmítání všech bloků verze 2 nebo nižší, jakmile byl dosažen 95% práh těžařů. Tento práh byl překročen u bloku číslo 363,725 dne 4. července 2015.