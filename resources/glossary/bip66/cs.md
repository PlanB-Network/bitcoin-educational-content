---
term: BIP66

---
Zavedla standardizaci formátu podpisu v transakcích. Tento BIP byl navržen v reakci na rozdílný způsob, jakým OpenSSL řeší kódování podpisu v různých systémech. Tato nejednotnost představovala riziko rozdělení blockchainu. BIP66 standardizoval formát podpisu pro všechny transakce pomocí přísného kódování DER (*Rozlišená pravidla kódování*). Tato změna si vyžádala měkký fork. Pro svou aktivaci pak BIP66 použil stejný mechanismus jako BIP34, vyžadoval zvýšení pole `nVersion` na verzi 3 a odmítal všechny bloky verze 2 nebo nižší, jakmile bylo dosaženo hranice 95 % těžařů. Tato hranice byla překročena u bloku číslo 363 725 dne 4. července 2015.