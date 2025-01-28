---
term: P2P TRANSPORT V2

---
Bitcoini P2P transpordiprotokolli uus versioon, mis sisaldab oportunistlikku krüpteerimist, et suurendada sõlmedevahelise side privaatsust ja turvalisust. Selle täiustamise eesmärk on lahendada mitmeid P2P-protokolli põhiversiooniga seotud probleeme, eelkõige muutes vahetatavad andmed passiivse vaatleja (näiteks internetiteenuse pakkuja) jaoks eristamatuks, vähendades seeläbi tsensuuri ja rünnakute ohtu andmepakettides esinevate konkreetsete mustrite tuvastamise kaudu.

Rakendatud krüpteerimine ei sisalda autentimist, et vältida asjatu keerukuse lisamist ja mitte ohustada võrguühenduse loata olemust. See uus P2P-transpordiprotokoll pakub siiski paremat turvalisust passiivsete rünnakute vastu ning muudab aktiivsed rünnakud oluliselt kulukamaks ja avastatavamaks (eelkõige MITM-rünnakud). Pseudosituatsioonilise andmevoo kasutuselevõtt raskendab ründajate tööd, kes soovivad side tsenseerida või manipuleerida.

P2P Transport V2 lisati lisavõimalusena (vaikimisi välja lülitatud) Bitcoin Core'i versiooni 26.0, mis võeti kasutusele detsembris 2023. Seda saab aktiveerida konfiguratsioonifaili valikuga `v2transport=1`.