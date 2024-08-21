---
term: SIGHASH_SINGLE/SIGHASH_ACP
---

SigHash lipu tüüp (`0x83`), mis on kombineeritud `SIGHASH_ANYONECANPAY` modifikaatoriga (`SIGHASH_ACP`), mida kasutatakse Bitcoin'i tehingute allkirjastamisel. See kombinatsioon määratleb, et allkiri kehtib ainult konkreetse üksiku sisendi kohta ja ainult väljundi suhtes, mille indeks on sama mis sellel sisendil. Teisi sisendeid ja väljundeid võivad lisada või muuta teised osapooled. See konfiguratsioon on kasulik koostööpõhistes tehingutes, kus osalejad saavad lisada oma sisendeid, et rahastada konkreetset väljundit.