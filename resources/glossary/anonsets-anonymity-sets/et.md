---
term: Anonsets (anonymity sets)

definition: Näitajad, mis mõõdavad UTXO privaatsuse astet, loendades mitteeristatavate UTXO-de arvu komplektis, tavaliselt pärast coinjoin.
---
Anonsetid toimivad indikaatoritena konkreetse UTXO privaatsuse taseme hindamisel. Täpsemalt mõõdavad need eristamatute UTXO-de arvu kogumis, mis hõlmab uuritavat münti. Kuna on vaja identsete UTXO-de rühma, arvutatakse anonsetid tavaliselt coinjoin’ide tsükli raames. Vajaduse korral võimaldavad need hinnata coinjoin’ide kvaliteeti. Suur anonset tähendab kõrgemat anonüümsuse taset, kuna konkreetset UTXO-d on kogumi sees keeruline eristada.

Anonsette on kahte tüüpi: forward anonset (forward-looking metrics); ja backward anonset (backward-looking metrics). Mõnikord kasutatakse anonsettide tähistamiseks ka terminit "*score*".

Esimene näitab selle rühma suurust, mille sees uuritav väljund-UTXO peitub, arvestades sisend-UTXO-d. See näitaja võimaldab mõõta mündi privaatsuse vastupidavust minevikust olevikku suunatud analüüsi suhtes (sisendist väljundisse). Teine näitab võimalike allikate arvu antud mündi jaoks, arvestades väljund-UTXO-d. See näitaja võimaldab mõõta mündi privaatsuse vastupidavust olevikust minevikku suunatud analüüsi suhtes (väljundist sisendisse).










