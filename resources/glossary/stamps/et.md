---
term: STAMPS

---
Protokoll, mis võimaldab vormindatud pildiandmete integreerimist otse Bitcoini plokiahelasse töötlemata mitme allkirjaga tehingute kaudu (P2MS). Stamps kodeerib pildi binaarse sisu baasil 64 ja lisab selle 1/3 P2MSi võtmetele. Üks võti on reaalne ja seda kasutatakse raha kulutamiseks, teised kaks on fiktiivsed võtmed (nendega seotud privaatne võti on teadmata), mis salvestavad andmeid. Kuna andmed kodeeritakse otse avalike võtmetena, mitte ei kasutata `OP_RETURN` väljundeid, on Stamps-protokolliga salvestatud kujutised sõlmede jaoks eriti töömahukad. See meetod loob eelkõige mitu UTXO-d, mis suurendab UTXO-de kogumi suurust ja tekitab probleeme täis sõlmedele.