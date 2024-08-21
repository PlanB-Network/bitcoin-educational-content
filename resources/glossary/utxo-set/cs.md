---
term: UTXO SET
---

Odkazuje na sbírku všech existujících UTXO v daném okamžiku. Jinými slovy, jedná se o velký seznam všech různých kusů bitcoinů, které čekají na utracení. Pokud sečtete částky všech UTXO v UTXO setu, dostanete celkovou peněžní hmotu bitcoinů v oběhu. Každý uzel v síti Bitcoin udržuje svůj vlastní UTXO set v reálném čase. Aktualizuje ho, jakmile jsou potvrzeny nové platné bloky s transakcemi, které spotřebují některé UTXO z UTXO setu a na oplátku vytvoří nové.

Tento UTXO set je udržován každým uzlem, aby rychle ověřil, zda jsou UTXO utracené v transakcích skutečně legitimní. To jim umožňuje detekovat a odmítnout pokusy o dvojí utrácení. UTXO set je často v centru pozornosti, pokud jde o decentralizaci Bitcoinu, protože jeho velikost se přirozeně velmi rychle zvyšuje. Jelikož část z něj musí být udržována v RAM pro ověření transakcí v rozumném čase, UTXO set by postupně mohl způsobit, že provoz plnohodnotného uzlu bude příliš nákladný. UTXO set má také významný dopad na IBD (*Initial Block Download*). Čím více UTXO setu může být umístěno v RAM, tím rychlejší je IBD. V Bitcoin Core je UTXO set uložen ve složce pojmenované `/chainstate`.

> ► *V angličtině se "UTXO set" může přeložit jako "UTXO set".*