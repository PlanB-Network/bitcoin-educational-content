---
term: STAMPS
---

Protokoll, mis võimaldab vormindatud pildiandmete otsest integreerimist Bitcoin'i plokiahelasse läbi toormultisignatuuritehingute (P2MS). Stamps kodeerib pildi binaarsisu base 64 formaadis ja lisab selle 1/3 P2MS-i võtmete hulka. Üks võti on reaalne ja seda kasutatakse vahendite kulutamiseks, samas kui kaks ülejäänud on näilised võtmed (nende vastav privaatvõti on teadmata), mis talletavad andmeid. Andmete kodeerimine otse avalike võtmetena, mitte `OP_RETURN` väljundite kasutamisega, muudab Stamps protokolli abil salvestatud pildid eriti töömahukaks sõlmede jaoks. See meetod loob märkimisväärselt mitu UTXO-d, mis suurendab UTXO kogumi suurust ja tekitab probleeme täissõlmedele.