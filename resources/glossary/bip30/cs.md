---
term: BIP30
---

Návrh na vylepšení zahrnující soft fork implementovaný 15. března 2012, který řešil problém duplicitních identifikátorů transakcí. Před BIP30 bylo technicky možné mít v blockchainu dvě různé transakce se stejným identifikátorem transakce (TXID). To se významně stalo dvakrát u coinbase transakcí: ta v bloku 91,880 má stejný TXID jako coinbase bloku 91,722 a ta v bloku 91,842 má stejný TXID jako coinbase bloku 91,812. BIP30 tento nedostatek vyřešil zavedením nového jednoduchého pravidla: žádná nová transakce nemůže mít stejný TXID jako dříve zaznamenaná transakce, pokud nebyla původní transakce zcela utracena (tj. všechny její výstupy byly použity). Tento soft fork byl aktivován pomocí metody flag day. Tím se stal jedním z prvních UASF.