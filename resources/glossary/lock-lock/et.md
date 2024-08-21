---
term: LOCK (.LOCK)
---

Faili kasutatakse Bitcoin Core'is andmekataloogi lukustamiseks. See luuakse, kui bitcoind või Bitcoin-qt käivitub, et vältida tarkvara mitme eksemplari samaaegset juurdepääsu samale andmekataloogile. Eesmärk on vältida konflikte ja andmete rikkumist. Kui tarkvara peatub ootamatult, võib .lock fail jääda ja enne Bitcoin Core'i taaskäivitamist tuleb see käsitsi kustutada.