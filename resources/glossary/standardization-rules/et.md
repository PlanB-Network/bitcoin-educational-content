---
term: STANDARDISEERIMISE REEGLID

---
Iga Bitcoini sõlmpunkt võtab lisaks konsensusreeglitele individuaalselt vastu standardimisreeglid, et määratleda kinnitamata tehingute struktuuri, mida ta võtab vastu oma mempool'i ja edastab oma eakaaslastele. Neid reegleid konfigureerib ja täidab seega iga sõlmpunkt lokaalselt ning need võivad erineda eri sõlmedes. Neid kohaldatakse ainult kinnitamata tehingute suhtes. Seega võtab sõlmpunkt vastu tehingu, mida ta peab mittestandardseks, ainult siis, kui see on juba lisatud kehtivasse plokki.

Märgitakse, et enamik sõlmi jätab vaikimisi konfiguratsioonid, nagu need on kehtestatud Bitcoin Core'is, luues seega standardimisreeglite ühtsuse kogu võrgus. Tehing, mis on küll konsensusreeglitele vastav, kuid ei järgi neid standardimisreegleid, on raskendatud kogu võrgus edastamisega. Siiski võib see ikkagi sisalduda kehtivas plokis, kui see jõuab kaevandajani. Praktikas edastatakse need tehingud, mida nimetatakse "mittestandardseteks", sageli otse kaevandajale välise vahendiga väljaspool Bitcoini võrdõigusvõrku. See on sageli ainus viis seda tüüpi tehingu kinnitamiseks.

Näiteks tehing, mis ei eralda mingeid tasusid, on konsensusreeglite kohaselt kehtiv ja mittestandardne, sest Bitcoin Core'i vaikimisi poliitika parameetri `minRelayTxFee` jaoks on `0.00001` (BTC/kB).

> ► * Mõnikord kasutatakse standardimisreeglite kohta ka terminit "mempoolreeglid"