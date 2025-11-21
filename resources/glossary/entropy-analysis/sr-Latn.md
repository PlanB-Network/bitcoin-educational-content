---
term: ENTROPIJA (ANALIZA)
---

U specifičnom kontekstu analize lanca, entropija je takođe naziv indikatora, izvedenog iz Shannonove entropije, koji je izumeo LaurentMT. Ovaj indikator omogućava merenje nedostatka znanja koje analitičari imaju o tačnoj konfiguraciji Bitcoin transakcije. Drugim rečima, što je veća entropija transakcije, to postaje teže za analitičare da identifikuju kretanja bitkoina između ulaza i izlaza.


U praksi, entropija otkriva da li, iz perspektive spoljnog posmatrača, transakcija predstavlja više mogućih interpretacija, zasnovanih isključivo na iznosima ulaza i izlaza, bez razmatranja drugih spoljašnjih ili unutrašnjih obrazaca i heuristika. Visoka entropija je tada sinonim za bolju poverljivost transakcije.


Entropija je definisana kao binarni logaritam broja mogućih kombinacija. Ovde je formula koja se koristi sa $E$ koja predstavlja entropiju transakcije i $C$ broj mogućih interpretacija:


$$
E = \log_2(C)
$$


Uzimajući u obzir vrednosti UTXO-a uključenih u transakciju, broj interpretacija $C$ predstavlja broj načina na koje se ulazi mogu povezati sa izlazima. Drugim rečima, određuje broj interpretacija koje transakcija može izazvati sa stanovišta spoljnog posmatrača koji je analizira.