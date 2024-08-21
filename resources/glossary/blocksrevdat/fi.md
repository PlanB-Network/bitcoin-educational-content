---
termi: BLOCKS/REV*.DAT
---

Tiedostojen nimi Bitcoin Core:ssa, jotka tallentavat tarvittavat tiedot mahdollisesti aiemmin lisättyjen lohkojen UTXO-joukon muutosten kumoamiseen. Jokainen tiedosto on yksilöity uniikilla numerolla, joka vastaa sitä blk*.dat-tiedostoa, johon se liittyy. Rev*.dat-tiedostot sisältävät kumoamistiedot, jotka vastaavat blk*.dat-tiedostoissa tallennettuja lohkoja. Tämä data on käytännössä lista kaikista UTXO:ista, jotka on käytetty syötteinä lohkossa. Nämä kumoamistiedostot mahdollistavat noden paluun aikaisempaan tilaan, jos lohkoketjun uudelleenjärjestely aiheuttaa aiemmin vahvistettujen lohkojen hylkäämisen.