---
term: MEMPOOL
---

Kontrakce termínů "memory" (paměť) a "pool" (skupina). Odkazuje na virtuální prostor, ve kterém jsou Bitcoinové transakce čekající na zařazení do bloku seskupeny dohromady. Když je transakce vytvořena a vysílána v Bitcoinové síti, je nejprve ověřena uzly sítě. Pokud je považována za platnou, je poté umístěna do Mempoolu každého uzlu, kde zůstává, dokud si ji těžař nevybere k zařazení do bloku.

Je důležité si uvědomit, že každý uzel v Bitcoinové síti udržuje svůj vlastní Mempool, a proto může obsah Mempoolu mezi různými uzly v daném okamžiku kolísat. Pozoruhodné je, že parametr `maxmempool` v souboru `bitcoin.conf` každého uzlu umožňuje operátorům ovládat množství RAM (operační paměti), kterou jejich uzel použije pro ukládání čekajících transakcí v Mempoolu. Omezením velikosti Mempoolu mohou operátoři uzlů zabránit jeho nadměrné spotřebě zdrojů na jejich systému. Tento parametr je specifikován v megabytech (MB). Výchozí hodnota pro Bitcoin Core je dosud 300 MB.

Transakce přítomné v Mempoolu jsou provizorní. Neměly by být považovány za neměnné, dokud nejsou zařazeny do bloku a po určitém počtu potvrzení. Často mohou být nahrazeny nebo odstraněny.