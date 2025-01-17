---
term: INDEXES/TXINDEX/

---
Soubory v jádře bitcoinu, které jsou určeny k indexování všech transakcí přítomných v blockchainu. Toto indexování umožňuje rychlé vyhledávání podrobných informací o transakci pomocí jejího identifikátoru (TXID), aniž by bylo nutné procházet celý blockchain. Vytvoření těchto indexovacích souborů je možnost, která není v jádře Bitcoin Core ve výchozím nastavení povolena. Pokud tato funkce není povolena, váš uzel bude indexovat pouze transakce spojené s peněženkami připojenými k vašemu uzlu. Chcete-li povolit indexování všech transakcí, musíte v souboru `bitcoin.conf` nastavit parametr `-txindex=1`. Tato volba je užitečná zejména pro aplikace a služby, které často prohledávají historii transakcí Bitcoinu.