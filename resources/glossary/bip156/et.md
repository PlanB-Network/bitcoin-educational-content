---
term: BIP156

---
Ettepanek, tuntud kui Dandelion, mille eesmärk on parandada tehingu marsruutimise privaatsust Bitcoini võrgus, et võidelda deanonümiseerimise vastu. Bitcoini tavapärase toimimise puhul edastatakse tehingud kohe mitmele sõlmpunktile. Kui vaatleja saab näha iga tehingut, mida iga võrgusõlme edastab, võib ta eeldada, et esimene tehingu saatnud sõlm on ka selle tehingu algataja ja seega pärineb see tehing selle sõlme operaatorilt. See nähtus võib võimaldada vaatlejatel seostada tavaliselt anonüümseid tehinguid IP-aadressidega.

BIP156 eesmärk on selle probleemi lahendamine. Selleks võetakse ringhäälingus kasutusele täiendav etapp, et säilitada anonüümsus enne avalikku levitamist. Seega kasutab Dandelion kõigepealt "varre" faasi, kus tehing saadetakse läbi suvalise sõlmede tee, enne kui see "pehmendusfaasis" kogu võrku edastatakse. Tüvi ja pehmed viitavad tehingu võrgu kaudu levimise käitumisele, mis meenutab võilille kuju (*a dandelion* inglise keeles).

Selline marsruutimismeetod varjab jälgi, mis viivad tagasi lähtesõlme, mistõttu on raske jälgida tehingu liikumist läbi võrgu tagasi selle päritoluni. Dandelion parandab seega privaatsust, piirates vastaste võimet võrgu deanonüümseks muutmiseks. See meetod on veelgi tõhusam, kui tehing läbib "varre" faasis sõlme, mis krüpteerib oma võrgusuhtluse, näiteks Tor või *P2P Transport V2*. BIP156 ei ole veel Bitcoin Core'ile lisatud.

![](../../dictionnaire/assets/36.webp)