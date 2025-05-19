---
term: RBF (Replace-by-fee)
---

Transakcioni mehanizam koji omogućava pošiljaocu da zameni jednu transakciju drugom plaćanjem viših naknada, kako bi ubrzao njeno potvrđivanje. Ako se transakcija sa preniskim naknadama zaglavi, pošiljalac može koristiti *Replace-by-fee* da poveća naknade i prioritizuje njihovu zamensku transakciju u mempool-ovima.


RBF je primenljiv sve dok je transakcija u mempoolovima; jednom kada je u bloku, više ne može biti zamenjena. Prilikom početnog slanja, transakcija mora navesti svoju dostupnost za zamenu podešavanjem vrednosti `nSequence` na broj manji od `0xfffffffe`. Ovo je poznato kao RBF "zastavica". Ovo podešavanje signalizira mogućnost ažuriranja transakcije nakon što je emitovana, što naknadno omogućava RBF. Međutim, ponekad je moguće zameniti transakciju koja nije signalizirala RBF. Čvorovi koji koriste konfiguracioni parametar `mempoolfullrbf=1` prihvataju ovu zamenu čak i ako RBF nije bio inicijalno signaliziran.


Za razliku od CPFP (*Dete Plaća Za Roditelja*), gde primalac može delovati kako bi ubrzao transakciju, RBF (*Replace-by-fee*) omogućava pošiljaocu da preuzme inicijativu i ubrza sopstvenu transakciju povećanjem naknada.