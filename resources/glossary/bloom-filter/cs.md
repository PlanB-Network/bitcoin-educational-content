---
term: BLOOM FILTER
---

Bloomův filtr je pravděpodobnostní datová struktura používaná k testování, zda je prvek součástí množiny. Bloomovy filtry umožňují rychlé kontroly členství bez nutnosti testovat celý dataset. Jsou zvláště užitečné v kontextech, kde jsou kritické prostor a rychlost, ale nízká a kontrolovaná míra chybovosti je přijatelná. Bloomovy filtry skutečně nevytvářejí falešné negativy, ale generují určité množství falešných pozitiv. Když je prvek přidán do filtru, několik hašovacích funkcí generuje pozice v bitovém poli. Pro kontrolu členství se používají stejné hašovací funkce. Pokud jsou všechny odpovídající bity nastaveny, prvek je pravděpodobně v množině, ale s rizikem falešných pozitiv. Bloomovy filtry jsou široce používány v oblastech databází a sítí. Je známo, že je Google používá pro svůj komprimovaný systém správy databází *BigTable*. V protokolu Bitcoinu jsou používány zejména pro SPV peněženky podle BIP37.

> ► *Když se konkrétně mluví o použití Bloomových filtrů v kontextu Bitcoinových transakcí, někdy se setkáme s termínem "Transaction Bloom Filtering".*