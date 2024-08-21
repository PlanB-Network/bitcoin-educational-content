---
term: SIGHASH_ALL/SIGHASH_ACP
---

SigHash lipu (`0x81`) tüüp, mis on kombineeritud `SIGHASH_ANYONECANPAY` modifikaatoriga (`SIGHASH_ACP`), mida kasutatakse Bitcoin'i tehingute allkirjastamisel. See kombinatsioon täpsustab, et allkiri kehtib kõikide väljundite kohta ja ainult konkreetse sisendi kohta tehingus. `SIGHASH_ALL | SIGHASH_ANYONECANPAY` võimaldab teistel osalejatel pärast esialgset allkirjastamist tehingule täiendavaid sisendeid lisada. See on eriti kasulik koostööl põhinevates stsenaariumides, nagu ühisrahastamise tehingud, kus erinevad panustajad saavad oma sisendeid lisada, säilitades samal ajal esialgse allkirjastaja poolt kinnitatud väljundite terviklikkuse.