---
term: BIP12
---

Ettepanek Gavin Andresenilt, et suurendada Bitcoin'i tehinguskriptide paindlikkust ja privaatsust. See BIP pakub välja uue skripti operaatori, nimega `OP_EVAL`, mis võimaldab skripti sisu hinnata `scriptSig` andmetes tehingu valideerimise protsessi ajal. BIP12 peamine muudatus on võimaldada ühe skripti lisamist teise skripti sisse. See tehnika võimaldab luua keerukamaid tingimusi, mida saab kulutamise hetkel kontrollida, ilma et oleks vaja neid kasutajatele, kes bitcoine saadetud aadressile saadavad, avalikustada. BIP12 asendati hiljem turvalisemate ettepanekutega, eriti BIP16 (P2SH)ga, mis pakub erinevat meetodit samade eesmärkide saavutamiseks nagu `OP_EVAL`.