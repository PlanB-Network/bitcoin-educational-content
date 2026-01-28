---
term: Blk*.dat
definition: Filer i Bitcoin Core som lagrar rådata för blockkedjans block.
---

Namn på filerna i Bitcoin Core som lagrar Blockchain:s råa blockdata. Varje fil identifieras med ett unikt nummer i sitt namn. Blocken registreras alltså i kronologisk ordning, med början i filen blk00000.dat. När denna fil når sin maximala kapacitet registreras följande block i blk00001.dat, sedan blk00002.dat och så vidare. Varje blk-fil har en maximal kapacitet på 128 mebibytes (MiB), vilket motsvarar drygt 134 megabytes (MB). Dessa filer har flyttats till mappen `/blocks` sedan version 0.8.0.