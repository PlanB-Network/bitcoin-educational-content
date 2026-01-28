---
term: SIGHASH_ALL/SIGHASH_ACP

definition: SigHashi kombinatsioon, mis võimaldab lisada sisendeid pärast esialgset allkirjastamist.
---
SigHashi lipu tüüp (`0x81`) koos modifikaatoriga `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`), mida kasutatakse Bitcoini tehingu allkirjades. See kombinatsioon määrab, et allkiri kehtib kõigi väljundite ja ainult konkreetse tehingu sisendi suhtes. `SIGHASH_ALL | SIGHASH_ANYONECANPAY` võimaldab teistel osalejatel lisada tehingule täiendavaid sisendeid pärast selle esialgset allkirjastamist. See on eriti kasulik koostööstsenaariumides, näiteks ühisrahastustehingutes, kus erinevad osalejad saavad lisada oma sisendeid, säilitades samal ajal esialgse allkirjastaja poolt kinnitatud väljundite terviklikkuse.