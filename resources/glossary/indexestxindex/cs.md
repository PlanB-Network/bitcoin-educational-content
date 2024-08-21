---
term: INDEXES/TXINDEX/
---

Soubory v Bitcoin Core, které jsou určeny k indexaci všech transakcí přítomných v blockchainu. Tato indexace umožňuje rychlé vyhledávání detailních informací o transakci pomocí jejího identifikátoru (TXID), aniž by bylo nutné procházet celý blockchain. Vytváření těchto indexových souborů není ve výchozím nastavení v Bitcoin Core povoleno. Pokud tato funkce není povolena, váš uzel bude indexovat pouze transakce spojené s peněženkami připojenými k vašemu uzlu. Pro povolení indexace všech transakcí musíte nastavit parametr `-txindex=1` v souboru `bitcoin.conf`. Tato možnost je zvláště užitečná pro aplikace a služby, které často prohledávají historii transakcí Bitcoinu.