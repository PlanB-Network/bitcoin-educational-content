---
term: RASKUSTE EESMÄRK

---
Raskustegur, mida tuntakse ka kui raskuse eesmärki, on parameeter, mida kasutatakse Bitcoini konsensusmehhanismis töö tõestuse (Proof of Work, PoW) abil. Sihtmärk kujutab endast arvulist väärtust, mis määrab kaevurite jaoks konkreetse krüptograafilise probleemi, mida nimetatakse töötõendiks, lahendamise raskuse uue ploki loomisel plokiahelas.

Raskuse sihtmärk on reguleeritav 256-bitine (64 baiti) arv, mis määrab plokkide päiste hashimise vastuvõetavuse piiri. Teisisõnu, selleks, et plokk oleks kehtiv, peab selle päise häkkimine `SHA256d`-ga (topelt `SHA256`) olema numbriliselt väiksem või võrdne raskuse sihtarvuga. Töö tõestamine seisneb ploki päise või coinbase'i tehingu `nonce` välja muutmises, kuni saadud hash on sihtväärtusest väiksem.

Seda eesmärki kohandatakse iga 2016. aasta plokkide kaupa (umbes iga kahe nädala tagant), kui toimub sündmus, mida nimetatakse "kohandamiseks" Raskustegur arvutatakse uuesti, võttes aluseks aja, mis kulus eelmiste 2016. aasta plokkide kaevandamiseks. Kui koguaeg on vähem kui kaks nädalat, suureneb raskusaste, kohandades eesmärki allapoole. Kui koguaeg on üle kahe nädala, väheneb raskusaste, kohandades eesmärki ülespoole. Eesmärk on säilitada keskmine kaevandamisaeg 10 minutit ploki kohta. See aeg iga ploki vahel aitab vältida Bitcoini võrgu jagunemist, mille tulemuseks on arvutusvõimsuse raiskamine. Raskuse sihtmärk on iga ploki päises, väljal "nBits". Kuna see väli on vähendatud 32 bitini ja eesmärk on tegelikult 256 bitti, on eesmärk tihendatud vähem täpsesse teaduslikku formaati.

![](../../dictionnaire/assets/34.webp)

> ► *Ne raskusastme eesmärki nimetatakse mõnikord ka "raskusastmeteguriks" Laiendatult võib sellele viidata selle kodeeringuga plokkide päises terminiga "nBits" *