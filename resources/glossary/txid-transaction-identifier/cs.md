---
term: TXID (IDENTIFIKÁTOR TRANSAKCE)

---
Jedinečný identifikátor spojený s každou transakcí Bitcoin. Generuje se výpočtem hashe `SHA256d` dat transakce. TXID slouží jako odkaz pro vyhledání konkrétní transakce v blockchainu. Používá se také k odkazu na UTXO, což je v podstatě součet TXID předchozí transakce a indexu určeného výstupu (nazývaného také "vout"). U transakcí po zavedení systému SegWit již TXID nebere v úvahu svědka transakce, což eliminuje zfalšovatelnost.