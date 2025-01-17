---
term: ENTROOPIA (ANALÜÜS)

---
Konkreetses ahelanalüüsi kontekstis on entroopia ka LaurentMT poolt leiutatud Shannoni entroopiast tuletatud näitaja nimi. See näitaja võimaldab mõõta analüütikute teadmatust Bitcoini tehingu täpse konfiguratsiooni kohta. Teisisõnu, mida suurem on tehingu entroopia, seda raskem on analüütikutel tuvastada bitcoinide liikumist sisendite ja väljundite vahel.

Praktikas näitab entroopia, kas välise vaatleja seisukohast on tehingul mitu võimalikku tõlgendust, mis põhinevad üksnes sisendite ja väljundite kogusel, arvestamata muid väliseid või sisemisi mustreid ja heuristikat. Kõrge entroopia on siis sünonüümiks tehingu paremale konfidentsiaalsusele.

Entroopia on defineeritud kui võimalike kombinatsioonide arvu binaarne logaritm. Siin on kasutatud valemit, kus $E$ tähistab tehingu entroopiat ja $C$ võimalike tõlgenduste arvu:

$$
E = \log_2(C)
$$

Võttes arvesse tehinguga seotud UTXOde väärtusi, kujutab tõlgenduste arv $C$ endast sisendite ja väljundite seostamise võimaluste arvu. Teisisõnu, see määrab kindlaks tõlgenduste arvu, mida tehing võib esile kutsuda seda analüüsiva välise vaatleja seisukohast.