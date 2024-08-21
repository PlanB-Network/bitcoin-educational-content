---
term: TXID (TRANSACTION IDENTIFIER)
---

Unikátní identifikátor spojený s každou Bitcoinovou transakcí. Je generován výpočtem hash `SHA256d` transakčních dat. TXID slouží jako odkaz pro nalezení konkrétní transakce v blockchainu. Používá se také pro odkazování na UTXO, což je v podstatě spojení TXID předchozí transakce a indexu určeného výstupu (také nazývaného "vout"). Pro transakce po zavedení SegWit již TXID nezahrnuje svědectví transakce, což eliminuje možnost změny.