---
term: BLOCKS/REV*.DAT
---

Název souborů v Bitcoin Core, které uchovávají informace potřebné k potenciálnímu vrácení změn provedených v UTXO setu přidanými bloky. Každý soubor je identifikován unikátním číslem, které odpovídá souboru blk*.dat, ke kterému náleží. Soubory rev*.dat obsahují data pro vrácení změn odpovídající blokům uloženým v souborech blk*.dat. Tato data jsou v podstatě seznamem všech UTXO vynaložených jako vstupy v bloku. Tyto soubory pro vrácení změn umožňují uzlu vrátit se do předchozího stavu v případě reorganizace blockchainu, která způsobí, že dříve ověřené bloky budou zavrženy.