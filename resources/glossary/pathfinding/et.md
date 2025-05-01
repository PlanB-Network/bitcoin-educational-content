---
term: PATHFINDING
---

Protsess, mida sõlme kasutab makse optimaalse marsruudi määramiseks läbi välgukanali võrgu. Teekonna leidmine toimub maksja sõlme poolt, mis peab valima kõige sobivamad vahesõlmed, et jõuda saajani. See valik põhineb mitmel kriteeriumil, näiteks tasudel, kanali läbilaskevõimel ja ajamääradel.


Teeotsingu algoritmid koostavad võrgu topoloogia graafi kuulujuttude andmete põhjal ja hindavad erinevaid võimalikke marsruute maksja ja vastuvõtja sõlme vahel. Need marsruudid reastatakse erinevate kriteeriumide alusel parimatest halvimateni. Seejärel testib sõlm neid marsruute, kuni tal õnnestub ühel neist makse sooritada.