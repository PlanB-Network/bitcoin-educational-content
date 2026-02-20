---
term: SIGHASH_NONE/SIGHASH_ACP

definition: SigHashi kombinatsioon, mis allkirjastab ühe konkreetse sisendi, sidumata end ühegi väljundiga.
---
SigHashi lipu tüüp (`0x82`) koos modifikaatoriga `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`), mida kasutatakse Bitcoini tehingu allkirjades. See kombinatsioon näitab, et allkiri kehtib ainult konkreetse sisendi suhtes, ilma et see kohustaks mis tahes väljundit. See võimaldab teistel osalejatel vabalt lisada täiendavaid sisendeid ja muuta kõiki tehingu väljundeid.