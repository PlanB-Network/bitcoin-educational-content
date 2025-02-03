---
term: BLK*.DAT

---
Navn på filene i Bitcoin Core som lagrer de rå blokkdataene i blokkjeden. Hver fil identifiseres med et unikt nummer i navnet. Blokkene registreres i kronologisk rekkefølge, og starter med filen blk00000.dat. Når denne filen når sin maksimale kapasitet, registreres de neste blokkene i blk00001.dat, deretter blk00002.dat, og så videre. Hver blk-fil har en maksimal kapasitet på 128 mebibyte (MiB), noe som tilsvarer litt over 134 megabyte (MB). Disse filene har blitt flyttet til mappen `/blocks` siden versjon 0.8.0.