---
term: BIP12

---
Gavin Andreseni ettepanek suurendada Bitcoini tehingute skriptide paindlikkust ja privaatsust. Selles veebisaidil tehakse ettepanek rakendada uus skripti opkood nimega "OP_EVAL", mis võimaldab tehingu valideerimise käigus hinnata skripti "scriptSig" andmetes sisalduvat skripti. BIP12 peamine muudatus on võimaldada ühe skripti lisamist teise skripti sisse. See tehnika võimaldab luua keerulisemaid tingimusi, mida saab kontrollida kulutamise ajal, ilma et neid oleks vaja avaldada kasutajatele, kes saadavad bitcoine kasutatud aadressile. BIP12 asendati hiljem turvalisemate ettepanekutega, eelkõige BIP16 (P2SH), mis pakub teistsugust meetodit samade eesmärkide saavutamiseks kui "OP_EVAL".