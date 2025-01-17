---
term: UTXO SET

---
Vztahuje se ke kolekci všech existujících UTXO v daném okamžiku. Jinými slovy, je to velký seznam všech různých kusů bitcoinů, které čekají na utracení. Pokud sečteme částky všech UTXO v souboru UTXO, získáme celkovou peněžní masu bitcoinů v oběhu. Každý uzel v síti bitcoinů udržuje svou vlastní sadu UTXO v reálném čase. Aktualizuje ji, jakmile jsou potvrzeny nové platné bloky s transakcemi, které obsahují a které spotřebovávají některé UTXO ze sady UTXO a vytvářejí na oplátku nové.

Tuto sadu UTXO si uchovává každý uzel, aby mohl rychle ověřit, zda jsou UTXO použité v transakcích skutečně legitimní. To jim umožňuje odhalit a odmítnout pokusy o dvojí utrácení. Sada UTXO je často jádrem obav z decentralizace Bitcoinu, protože její velikost se přirozeně velmi rychle zvyšuje. Vzhledem k tomu, že její část musí být uchovávána v paměti RAM, aby bylo možné v rozumném čase ověřit transakce, mohla by sada UTXO postupně způsobit, že provoz celého uzlu bude příliš nákladný. Sada UTXO má také významný dopad na IBD (*Initial Block Download*). Čím více sady UTXO lze umístit do paměti RAM, tím rychlejší je IBD. V jádře bitcoinu je sada UTXO uložena ve složce s názvem `/chainstate`.

> ► V angličtině by se "UTXO set" dalo přeložit jako "UTXO set".*