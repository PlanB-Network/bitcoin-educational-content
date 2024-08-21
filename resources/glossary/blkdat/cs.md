---
term: BLK*.DAT
---

Název souborů v Bitcoin Core, které ukládají surová data bloků blockchainu. Každý soubor je identifikován unikátním číslem ve svém názvu. Bloky jsou tak zaznamenávány v chronologickém pořadí, začínající souborem blk00000.dat. Když tento soubor dosáhne své maximální kapacity, následující bloky jsou zaznamenány v blk00001.dat, poté blk00002.dat a tak dále. Každý blk soubor má maximální kapacitu 128 mebibytů (MiB), což je ekvivalentní trochu více než 134 megabytů (MB). Tyto soubory byly od verze 0.8.0 přesunuty do složky `/blocks`.