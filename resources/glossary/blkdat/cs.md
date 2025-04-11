---
term: BLK*.DAT

---
Název souborů v jádře bitcoinu, které ukládají surová data bloků blockchainu. Každý soubor je identifikován jedinečným číslem ve svém názvu. Bloky jsou tedy zaznamenávány v chronologickém pořadí, počínaje souborem blk00000.dat. Když tento soubor dosáhne své maximální kapacity, následující bloky se zaznamenávají do souboru blk00001.dat, pak blk00002.dat atd. Každý soubor blk má maximální kapacitu 128 megabajtů (MiB), což odpovídá o něco více než 134 megabajtům (MB). Tyto soubory byly od verze 0.8.0 přesunuty do složky `/blocks`.