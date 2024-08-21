---
termi: MTP (MEDIAN TIME PAST)
---

Tätä käsitettä käytetään Bitcoin-protokollassa verkon konsensusajan leveyden määrittämiseen. MTP määritellään viimeksi louhittujen 11 lohkon aikaleimojen mediaanina. Tämän indikaattorin käyttö auttaa välttämään erimielisyyksiä solmujen välillä tarkan ajan suhteen, jos esiintyy eroavaisuuksia. MTP:tä käytettiin alun perin lohkojen aikaleimojen validiteetin varmistamiseen menneisyyteen nähden. BIP113:n myötä sitä on myös käytetty verkon ajan viitearvona aikalukko-transaktioiden validiteetin varmistamiseen (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence`, ja `OP_CHECKSEQUENCEVERIFY`).