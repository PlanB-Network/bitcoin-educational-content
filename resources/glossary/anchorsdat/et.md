---
term: Anchors.dat

definition: Bitcoin Core fail, mis salvestab IP aadresse sõlmede jaoks, millega klient enne väljalülitamist ühendatud oli, et hõlbustada uuesti ühendamist taaskäivitamisel.
---
Fail, mida kasutatakse Bitcoin Core'i kliendis, et salvestada väljuvate sõlmede IP-aadressid, millega klient oli enne sulgemist ühendatud. Anchors.dat luuakse seega iga kord, kui sõlme peatatakse ja kustutatakse selle taaskäivitamisel. Sõlmed, mille IP-aadressid selles failis sisalduvad, kasutatakse selleks, et aidata sõlme taaskäivitamisel kiiresti ühendusi luua.