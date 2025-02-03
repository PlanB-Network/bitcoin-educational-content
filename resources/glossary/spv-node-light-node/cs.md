---
term: SPV UZEL (SVĚTELNÝ UZEL)

---
Uzel SPV (*Simple Payment Verification*), někdy nazývaný "light node", je odlehčený klient uzlu Bitcoin, který umožňuje uživatelům ověřovat transakce bez nutnosti ukládat celý blockchain. Místo toho uzel SPV ukládá pouze hlavičky bloků a v případě potřeby získává informace o konkrétních transakcích dotazem na plné uzly. Tento princip ověřování je umožněn strukturou transakcí v blocích Bitcoinu, které jsou uspořádány v kryptografickém akumulátoru (Merkleho strom).

Tento přístup je výhodný pro zařízení s omezenými zdroji, jako jsou mobilní telefony. Uzly SPV se však spoléhají na plnohodnotné uzly, pokud jde o dostupnost informací, což znamená další úroveň důvěryhodnosti, a tudíž nižší bezpečnost ve srovnání s plnohodnotnými uzly. Uzly SPV nemohou samostatně ověřovat transakce, ale mohou ověřit, zda je transakce zahrnuta do bloku, nahlédnutím do Merkleho důkazů.