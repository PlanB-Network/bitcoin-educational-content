---
term: Utreexo

definition: Protocolo ihunganya ingano ya UTXO set muri Bitcoin nodes ikoresheje uburyo bushingiye kuri Merkle trees.
---

Itegeko ryakozwe na Tadge Dryja ryo gukoranya ivyuma vya Bitcoin vy’ivyuma vya UTXO hakoreshejwe igikoresho co gukoranya ibintu gishingiye ku biti vya Merkle. Udakunze UTXO ya kera isaba umwanya munini wo kubika, Utreexo igabanya cane ubwonko bukenewe mu kubika gusa imizi y’igiti ca Merkle. Ivyo bituma node ishobora kugenzura ukubaho kw’ama UTXO akoreshwa mu kwinjira mu bikorwa, ataco akeneye kubika umugwi wose w’ama UTXO. Mu gukoresha Utreexo, buri node igumya gusa urutoke rw’ibanga rwitwa umuzi wa Merkle. Iyo hakozwe ugucuruza, uwukoresha atanga ibimenyamenya vy’uko ari we afise ama UTXO n’inzira za Merkle zihuye. Gutyo, iyo node irashobora kugenzura amafaranga ata kubika umugwi wose wa UTXO. Reka dufate akarorero n'ikigereranyo kugira ngo dutahure ubu buryo:





Muri aka karorero, nagabanyije n’ibigirankana igitigiri ca UTXO ku UTXO 4 kugira ngo bishobore gutahura. Mu vy’ukuri, birahambaye kwiyumvira ko hari hafi imiliyoni 140 z’ama UTXO kuri Bitcoin igihe twandika iyi mirongo. Muri iki kigereranyo, urudodo rwa Utreexo rwokenera gusa kugumiza Merkle Root muri RAM. Iyo ironse amahera y’ugucuruza akoresheje UTXO No. 3 (mu mwijima), ikimenyamenya coba gifise ibi bikurikira:

*UTXO 3*;

*IBIBAZO 4;*

**IBIBAZO 1-2.**


Aya makuru arungitswe n’uwurungitse amafaranga, urudodo rwa Utreexo rukora ibi bikurikira:


- Ibara igicapo ca UTXO 3, kikayiha HASH 3;
- Ifatanya HASH 3 na HASH 4;

*Ibara igicapo cabo, kikayiha HASH 3-4;*


- Ifatanya HASH 3-4 na HASH 1-2;

*Ibara igicapo cabo, kikayiha umuzi wa Merkle.*


Nimba umuzi wa Merkle ironka biciye mu nzira yayo ari umwe n’umuzi wa Merkle yabitse muri RAM yayo, rero iravyemera ko UTXO No. 3 ari igice c’umugwi wa UTXO vy’ukuri.

Ubwo buryo buragabanya RAM ikenewe ku bakoresha full node. Ariko rero, Utreexo irafise aho igarukira, harimwo n’ukwiyongera kw’ubunini bw’amabuye kubera ibimenyamenya vy’inyongera be n’ubushobozi bwo kwizigira ama node ya Utreexo ku ma node y’ikiraro kugira ngo aronke ibimenyamenya bibuze. Bridge Nodes ni nodes zuzuye za kera zitanga ibimenyamenya bikenewe ku nodes za Utreexo, gutyo zikaba zituma habaho ukugenzura kwose. Ubwo buryo buratanga ugusenyera ku mugozi umwe hagati y’ubushobozi n’ugusenyura, bigatuma kwemeza ibikorwa vy’ubudandaji bishobora gushikirwa n’abakoresha bafise uburyo buke.