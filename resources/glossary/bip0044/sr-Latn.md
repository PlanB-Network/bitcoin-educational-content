---
term: BIP0044
---

Predlog za poboljšanje koji uvodi standardnu hijerarhijsku strukturu derivacije za HD novčanike. BIP44 se nadovezuje na principe uspostavljene BIP32 za derivaciju ključeva i na BIP43 za korišćenje polja “purpose”. Uvodi strukturu derivacije sa pet nivoa: `m / purpose' / coin_type' / account' / change / address_index`. Ovde su detalji za svaku dubinu:


- `m /` označava glavni privatni ključ. On je jedinstven za Wallet i ne može imati "siblinge" na istom nivou. Glavni ključ je direktno izveden iz Wallet-ovog seed;
- `m / purpose' /` označava svrhu derivacije koja pomaže u identifikaciji praćenog standarda. Ovo polje je opisano u BIP43. Na primer, ako Wallet prati BIP84 (SegWit V0) standard, indeks bi tada bio `84'`;
- `m / purpose' / coin-type' /` označava tip kriptovalute. Ovo omogućava jasno razlikovanje između grana posvećenih jednoj kriptovaluti i onih posvećenih drugoj kriptovaluti u multi-coin Wallet. Indeks posvećen Bitcoin je `0'`;
- `m / purpose' / coin-type' / account' /` označava broj računa. Ova dubina omogućava lako razlikovanje i organizaciju Wallet u različite račune. Ovi računi su numerisani počevši od `0'`. Prošireni ključevi (`xpub`, `xprv`...) se nalaze na ovoj dubini;
- `m / purpose' / coin-type' / account' / change /` označava lanac. Svaki nalog definisan na dubini 3 ima dva lanca na dubini 4: eksterni lanac i interni lanac (takođe nazvan "change"). Eksterni lanac izvodi adrese namenjene za javnu komunikaciju, tj. adrese koje nam se nude kada kliknemo na "primi" u našem Wallet softveru. Interni lanac izvodi adrese koje nisu namenjene za javnu razmenu, tj. prvenstveno adrese za kusur. Eksterni lanac je identifikovan indeksom `0`, a interni lanac je identifikovan indeksom `1`. Primetićete da od ove dubine više ne vršimo ojačanu derivaciju, već normalnu derivaciju (nema apostrofa). Zahvaljujući ovom mehanizmu, sposobni smo da izvedemo sve javne ključeve potomaka iz njihovog `xpub`;
- `m / purpose' / coin-type' / account' / change / Address-index` jednostavno označava broj primajućeg Address i njegov par ključeva, kako bi se razlikovao od svojih "srodnika" na istoj dubini na istoj grani. Na primer, prvi izvedeni Address ima indeks `0`, drugi Address ima indeks `1`, i tako dalje...

Na primer, ako moj prijemni Address ima put derivacije `m / 86' / 0' / 0' / 0 / 5`, možemo izvesti sledeće informacije:


- `86'` označava da pratimo standard derivacije BIP86 (Taproot ili SegWitV1);
- `0'` označava da je to Bitcoin Address;
- `0'` označava da smo na prvom nalogu Wallet;
- `0` označava da je to eksterni Address;
- `5` označava da je to šesti eksterni Address ovog naloga.