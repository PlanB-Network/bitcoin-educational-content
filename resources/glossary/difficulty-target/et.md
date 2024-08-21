---
term: RASKUSTASEME SIHT
---

Raskustegur, tuntud ka kui raskustaseme siht, on parameeter, mida kasutatakse konsensusmehhanismis töötõendiga (Proof of Work, PoW) Bitcoinis. Siht esindab numbrilist väärtust, mis määrab raskuse kaevuritele lahendada kindel krüptograafiline probleem, mida nimetatakse töötõendiks, luues uue ploki plokiahelas.

Raskustaseme siht on reguleeritav 256-bitine (64 baiti) number, mis määrab aktsepteeritavuse piiri ploki päiste räsimiseks. Teisisõnu, et plokk oleks kehtiv, peab selle päise räsi `SHA256d` (kahekordne `SHA256`) olema numbriliselt väiksem või võrdne raskustaseme sihiga. Töötõend seisneb ploki päise või coinbase tehingu `nonce` välja muutmises, kuni tulemuseks olev räsi on sihtväärtusest madalam.

See siht kohandatakse iga 2016 ploki järel (umbes iga kahe nädala tagant), sündmuse käigus, mida nimetatakse "kohandamiseks". Raskustegur arvutatakse ümber lähtudes ajast, mis kulus eelmise 2016 ploki kaevandamiseks. Kui koguaeg on vähem kui kaks nädalat, suureneb raskus, kohandades sihti allapoole. Kui koguaeg on rohkem kui kaks nädalat, väheneb raskus, kohandades sihti ülespoole. Eesmärk on hoida keskmist kaevandamisaega 10 minutit ploki kohta. See aeg iga ploki vahel aitab vältida Bitcoin võrgu jagunemist, mis toob kaasa arvutusvõimsuse raiskamise. Raskustaseme siht leidub igas ploki päises, `nBits` väljal. Kuna see väli on vähendatud 32 bitini ja siht on tegelikult 256 biti suurune, on siht kokku surutud vähem täpseks teaduslikuks formaadiks.

![](../../dictionnaire/assets/34.png)

> ► *Raskustaseme sihti nimetatakse mõnikord ka "raskusteguriks". Laiendatult võib seda nimetada selle kodeeringuga ploki päistes terminiga "nBits".*