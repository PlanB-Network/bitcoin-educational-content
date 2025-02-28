---
term: MERKLE ROOT

---
Sammendrag eller "topphash" av et Merkle-tre, som representerer en oppsummering av all informasjonen som finnes i treet. Et Merkle-tre er en kryptografisk akkumulatorstruktur, noen ganger også kalt et "hash-tre". I Bitcoin-sammenheng brukes Merkle-treet til å organisere transaksjoner i en blokk og til å gjøre det enklere å raskt verifisere at en spesifikk transaksjon er inkludert. I Bitcoin-blokker oppnås Merkle-roten ved å hashe transaksjoner parvis til bare én hash gjenstår (Merkle-roten). Denne inkluderes deretter i overskriften til den tilsvarende blokken. Dette hashtreet finnes også i UTREEXO, en struktur som gjør det mulig å kondensere UTXO-nodesettet, og i MAST Taproot.