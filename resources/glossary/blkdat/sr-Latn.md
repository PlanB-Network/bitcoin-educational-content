---
term: BLK*.DAT
---

Ime datoteka u Bitcoin Core koje čuvaju sirove podatke blokova Blockchain. Svaka datoteka je identifikovana jedinstvenim brojem u svom imenu. Tako su blokovi zabeleženi hronološkim redom, počevši od datoteke blk00000.dat. Kada ova datoteka dostigne svoj maksimalni kapacitet, sledeći blokovi se beleže u blk00001.dat, zatim blk00002.dat, i tako dalje. Svaka blk datoteka ima maksimalni kapacitet od 128 mebibajta (MiB), što je ekvivalentno nešto više od 134 megabajta (MB). Ove datoteke su premeštene u folder `/blocks` od verzije 0.8.0.