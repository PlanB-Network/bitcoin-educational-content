---
term: Lukustus (.lock)

definition: Fail, mis takistab mitmel Bitcoin Core'i instantsil samale kataloogile üheaegselt juurde pääsemast.
---
Fail, mida kasutatakse Bitcoin Core'is andmete kataloogi lukustamiseks. See luuakse bitcoindi või Bitcoin-qt käivitamisel, et vältida mitme tarkvarainstantsi samaaegset juurdepääsu samale andmekataloogile. Eesmärk on vältida konflikte ja andmete kahjustamist. Kui tarkvara ootamatult peatub, võib .lock-fail jääda ja see tuleb enne Bitcoin Core'i taaskäivitamist käsitsi kustutada.