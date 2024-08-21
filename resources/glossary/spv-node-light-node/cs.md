---
term: SPV NODE (LIGHT NODE)
---

SPV (*Simple Payment Verification*) uzel, někdy nazývaný "light node", je lehký klient Bitcoin uzlu, který umožňuje uživatelům ověřovat transakce bez nutnosti uchovávat celý blockchain. Místo toho SPV uzel uchovává pouze hlavičky bloků a získává informace o konkrétních transakcích dotazováním plných uzlů, když je to nutné. Tento princip ověřování je umožněn strukturou transakcí v blocích Bitcoinu, které jsou organizovány v rámci kryptografického akumulátoru (Merkle Tree).

Tento přístup je výhodný pro zařízení s omezenými zdroji, jako jsou mobilní telefony. Nicméně, SPV uzly se spoléhají na plné uzly pro dostupnost informací, což znamená dodatečnou úroveň důvěry a tím pádem menší bezpečnost ve srovnání s plnými uzly. SPV uzly nemohou ověřovat transakce autonomně, ale mohou ověřit, zda je transakce zahrnuta v bloku konzultací Merkle důkazů.