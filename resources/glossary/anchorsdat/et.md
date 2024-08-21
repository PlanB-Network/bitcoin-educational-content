---
term: ANCHORS.DAT
---

Fail, mida kasutatakse Bitcoin Core kliendis, et salvestada väljuvate sõlmede IP-aadresse, millega klient oli ühendatud enne väljalülitamist. Seega luuakse anchors.dat iga kord, kui sõlm peatatakse, ja kustutatakse, kui see taaskäivitatakse. Selle faili sisaldavate sõlmede IP-aadresse kasutatakse, et aidata kiiresti luua ühendusi, kui sõlm taaskäivitatakse.