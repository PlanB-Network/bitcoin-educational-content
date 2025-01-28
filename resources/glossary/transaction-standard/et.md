---
term: TEHINGUSTANDARD

---
Bitcoini tehing, mis lisaks konsensusreeglite järgimisele kuulub ka Bitcoin Core'i sõlmedes vaikimisi kehtestatud standardimisreeglitesse. Need standardimisreeglid kehtestab iga Bitcoini sõlmpunkt lisaks konsensusreeglitele eraldi, et määratleda kinnitamata tehingute struktuuri, mida ta oma mempoolis aktsepteerib ja mida ta oma eakaaslastele edastab.

Need reeglid konfigureeritakse ja täidetakse seega iga sõlme poolt lokaalselt ning need võivad olla eri sõlmedes erinevad. Neid kohaldatakse ainult kinnitamata tehingute suhtes. Seega võtab sõlmpunkt vastu tehingu, mida ta peab ebastandardseks, ainult siis, kui see on juba lisatud kehtivasse plokki.

Märgitakse, et enamik sõlmi jätab vaikimisi konfiguratsioonid, nagu need on kehtestatud Bitcoin Core'is, luues seega standardimisreeglite ühtsuse kogu võrgus. Tehingul, mis on küll konsensusreeglitele vastav, kuid ei järgi neid standardimisreegleid, on raskusi võrgu kaudu levimisel. Siiski võib see ikkagi sisalduda kehtivas plokis, kui see jõuab kaevandajani. Praktikas edastatakse need mittestandardseteks kvalifitseeritud tehingud sageli otse kaevandajale Bitcoini võrdõigusvõrgustiku välise vahendiga. See on sageli ainus viis sellise tehingu kinnitamiseks. Näiteks tehing, mis ei eralda tasu, on konsensuseeskirjade kohaselt kehtiv ja mittestandardne, sest Bitcoin Core'i vaikimisi poliitika parameetri `minRelayTxFee` jaoks on `0,00001` (BTC/kB).