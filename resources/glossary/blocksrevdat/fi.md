---
term: DAT

---
Niiden tiedostojen nimi Bitcoin Coressa, jotka tallentavat tiedot, joita tarvitaan aiemmin lisättyjen lohkojen UTXO-joukkoon tekemien muutosten mahdolliseen kumoamiseen. Kukin tiedosto tunnistetaan yksilöllisellä numerolla, joka on sama kuin blk*.dat-tiedosto, jota se vastaa. Rev*.dat-tiedostot sisältävät blk*.dat-tiedostoihin tallennettuja lohkoja vastaavat peruutustiedot. Nämä tiedot ovat lähinnä luettelo kaikista UTXO:ista, joita käytetään lohkon tuloina. Näiden käänteistiedostojen avulla solmu voi palata aiempaan tilaan, jos lohkoketjun uudelleenjärjestely aiheuttaa aiemmin validoitujen lohkojen hylkäämisen.