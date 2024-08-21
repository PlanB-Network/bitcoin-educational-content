---
term: BLK*.DAT
---

Failide nimetus Bitcoin Core'is, mis salvestavad toorandmed blockchaini blokkidest. Iga fail on identifitseeritud unikaalse numbriga oma nimes. Seega salvestatakse blokid kronoloogilises järjekorras, alustades failiga blk00000.dat. Kui see fail saavutab oma maksimaalse mahutavuse, salvestatakse järgnevad blokid faili blk00001.dat, seejärel blk00002.dat jne. Igal blk failil on maksimaalne mahutavus 128 mebibaiti (MiB), mis on võrdne natuke rohkem kui 134 megabaiti (MB). Need failid on alates versioonist 0.8.0 viidud kausta `/blocks`.