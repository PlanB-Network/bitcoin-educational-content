---
term: Blk*.dat

definition: Bitcoin Core'i failid, mis salvestavad plokiahela plokkide toorandmeid.
---
Bitcoin Core'i failide nimi, mis salvestavad plokiahela toorseid plokkide andmeid. Iga fail on identifitseeritud unikaalse numbriga selle nimes. Seega salvestatakse plokid kronoloogilises järjekorras, alustades failist blk00000.dat. Kui see fail saavutab oma maksimaalse mahu, salvestatakse järgmised plokid faili blk00001.dat, seejärel blk00002.dat jne. Iga blk-faili maksimaalne maht on 128 megabaiti (MiB), mis vastab veidi üle 134 megabaidi (MB). Need failid on alates versioonist 0.8.0 viidud kausta `/blocks`.