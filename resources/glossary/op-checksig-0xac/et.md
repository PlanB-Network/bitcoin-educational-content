---
term: OP_CHECKSIG (0XAC)
---

Kontrollib allkirja kehtivust antud avaliku võtme suhtes. See võtab virna kahest ülemisest elemendist: allkirja ja avaliku võtme ning hindab, kas allkiri on õige tehingu räsi ja määratud avaliku võtme jaoks. Kui kontroll on edukas, lükkab see virnale väärtuse `1` (tõene), vastasel juhul `0` (väär). See operatsioonikood muudeti Tapscriptis, et kontrollida Schnorri allkirju.