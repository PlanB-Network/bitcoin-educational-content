---
term: BÜTSANTSIGENERAALIDE PROBLEEM
---

Probleemi formuleerisid esmakordselt Leslie Lamport, Robert Shostak ja Marshall Pease spetsialiseeritud ajakirjas *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["Bütsantsi generaali probleem"](https://lamport.azurewebsites.net/pubs/byz.pdf) juulis 1982. Tänapäeval kasutatakse seda näitamaks väljakutseid otsuste tegemisel, kui hajutatud süsteem ei saa ühelegi osalejale usaldada.

Selles metafooris on rühm Bütsantsi generaale ja nende vastavad armeed laagris ümber linna, mida nad soovivad rünnata või piirata. Generaalid on geograafiliselt üksteisest eraldatud ja peavad oma strateegia koordineerimiseks suhtlema läbi sõnumitooja. Pole oluline, kas nad ründavad või taanduvad, peaasi, et kõik generaale jõuavad konsensusele.

Seega võime kaaluda järgmisi nõudeid:
* Iga general peab tegema otsuse: rünnata või taanduda (jah või ei);
* Kui otsus on tehtud, ei saa seda muuta;
* Kõik generaale peavad nõustuma sama otsusega ja täitma seda sünkroonselt.

Lisaks saab general suhelda teisega ainult sõnumite kaudu, mida kuller edastab, mis võivad hilineda, hävida, muutuda või kaduda. Ja isegi kui sõnum edukalt kohale jõuab, võib üks või mitu generalit (ükskõik millisel põhjusel) reetlikult käituda ja saata petliku sõnumi, külvates kaost.

Dilemma rakendamine Bitcoini plokiahela kontekstis tähendab, et iga general esindab võrgusõlme, mis peab jõudma süsteemi oleku osas konsensusele. Teisisõnu, hajutatud võrgu enamik osalejaid peab nõustuma ja täitma sama tegevust, et vältida täielikku ebaõnnestumist. Ainus viis sellises hajutatud süsteemis konsensusele jõuda on, kui vähemalt 2/3 võrgu sõlmedest on usaldusväärsed ja ausad. Seega, kui võrgu enamus otsustab pahatahtlikult tegutseda, on süsteem haavatav.

> ► *Seda dilemmat nimetatakse mõnikord ka "Usaldusväärse ringhäälingu probleemiks".*