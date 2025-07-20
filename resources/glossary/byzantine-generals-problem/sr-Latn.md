---
term: PROBLEM VIZANTIJSKIH GENERALA
---

Problem su prvi formulisali Leslie Lamport, Robert Shostak i Marshall Pease u specijalizovanom časopisu *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["The Byzantine Generals Problem"](https://lamport.azurewebsites.net/pubs/byz.pdf) u julu 1982. Danas se koristi za ilustrovanje izazova u donošenju odluka kada distribuirani sistem ne može verovati nijednom akteru.


U ovoj metafori, grupa vizantijskih generala i njihove odgovarajuće vojske kampuju oko grada koji žele napasti ili opsedati. Generali su geografski odvojeni jedni od drugih i moraju komunicirati putem glasnika kako bi koordinisali svoju strategiju. Da li će napasti ili se povući nije važno, sve dok svi generali postignu konsenzus.


Stoga možemo razmotriti sledeće zahteve:


- Svaki general mora doneti odluku: napad ili povlačenje (da ili ne);
- Jednom kada se odluka donese, ne može se promeniti;
- Svi generali moraju se složiti oko iste odluke i izvršiti je istovremeno.


Štaviše, general može komunicirati s drugim samo putem poruka koje prenosi kurir, a koje mogu biti odložene, uništene, izmenjene ili izgubljene. Čak i ako je poruka uspešno dostavljena, jedan ili više generala mogu odlučiti (iz bilo kog razloga) da iznevere uspostavljeno poverenje i pošalju lažnu poruku, sejući haos.


Primena dileme u kontekstu Bitcoin Blockchain, svaki general predstavlja čvor u mreži, koji treba da postigne konsenzus o stanju sistema. Drugim rečima, većina učesnika u distribuiranoj mreži mora se složiti i izvršiti istu akciju kako bi se izbegao potpuni neuspeh. Jedini način da se postigne konsenzus u ovom tipu distribuiranog sistema je da najmanje 2/3 čvorova mreže budu pouzdani i pošteni. Dakle, ako većina mreže odluči da deluje zlonamerno, sistem je ranjiv.


> ► *Ova dilema se ponekad naziva i "Problem pouzdanog emitovanja."*