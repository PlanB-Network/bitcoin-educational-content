---
term: BÜTSANTSI KINDRALITE PROBLEEM

---
Probleemi sõnastasid esmakordselt Leslie Lamport, Robert Shostak ja Marshall Pease erialases ajakirjas *ACM Transactions on Programming Languages and Systems, vol 4, nr 3* ["The Byzantine Generals Problem"](https://lamport.azurewebsites.net/pubs/byz.pdf) 1982. aasta juulis. Seda kasutatakse tänapäeval, et illustreerida probleeme otsuste tegemisel, kui hajutatud süsteem ei saa usaldada ühtegi osalejat.

Selles metafooris on rühm Bütsantsi kindralid ja nende vastavad armeed laagrites linna ümber, mida nad soovivad rünnata või piirata. Kindralid on üksteisest geograafiliselt eraldatud ja peavad oma strateegia kooskõlastamiseks suhtlema sõnumitooja kaudu. See, kas nad ründavad või taganevad, ei ole oluline, kui kõik kindralid jõuavad üksmeelele.

Seetõttu võime arvestada järgmisi nõudeid:


- Iga kindral peab tegema otsuse: kas rünnata või taganeda (jah või ei);
- Kui otsus on tehtud, ei saa seda enam muuta;
- Kõik kindralid peavad kokku leppima ühes ja samas otsuses ning seda sünkroonselt täitma.

Pealegi saab kindral suhelda teise kindraliga ainult kulleri poolt edastatud sõnumite kaudu, mis võivad hilineda, hävida, muutuda või kaduma minna. Ja isegi kui sõnum on edukalt kohale toimetatud, võib üks või mitu kindralit otsustada (mis tahes põhjusel) usaldust petta ja saata võltsitud sõnumi, külvates sellega kaost.

Rakendades dilemmat Bitcoini plokiahela konteksti, esindab iga üldkasutatav võrgu sõlme, mis peab jõudma konsensusele süsteemi oleku osas. Teisisõnu peab enamik jaotatud võrgu osalejaid kokku leppima ja sooritama sama tegevuse, et vältida täielikku ebaõnnestumist. Ainus viis konsensuse saavutamiseks seda tüüpi hajutatud süsteemis on see, et vähemalt 2/3 võrgu sõlmedest on usaldusväärsed ja ausad. Seega, kui enamus võrgu osalejatest otsustab tegutseda pahatahtlikult, on süsteem haavatav.

> ► *Seda dilemmat nimetatakse mõnikord ka "Usaldusväärse ringhäälingu probleemiks "*