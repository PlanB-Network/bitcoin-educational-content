---
term: PUTANJA IZVODJENJA
---

U kontekstu Hijerarhijski Determinističkih (HD) novčanika, put derivacije odnosi se na sekvencu indeksa korišćenih za derivaciju podključeva iz glavnog ključa. Opisan u BIP32, ovaj put identifikuje strukturu stabla za derivaciju podključeva. Put derivacije je predstavljen nizom indeksa odvojenih kosim crticama, i uvek počinje sa glavnim ključem (označenim kao `m/`). Na primer, tipičan put može biti `m/84'/0'/0'/0/0`. Svaki nivo derivacije je povezan sa specifičnom dubinom:


- `m /` označava glavni privatni ključ. On je jedinstven za Wallet i ne može imati "siblinge" na istom nivou. Glavni ključ se direktno izvodi iz seed;
- `m / purpose' /` označava svrhu derivacije koja pomaže u identifikaciji praćenog standarda. Ovo polje je opisano u BIP43. Na primer, ako Wallet prati BIP84 standard (SegWit V0), indeks bi tada bio `84'`;
- `m / purpose' / coin-type' /` označava tip kriptovalute. Ovo omogućava jasno razlikovanje između grana posvećenih jednoj kriptovaluti i onih posvećenih drugoj u multi-coin Wallet. Indeks posvećen Bitcoin je `0'`;
- `m / purpose' / coin-type' / account' /` označava broj računa. Ova dubina olakšava razlikovanje i organizaciju Wallet u različite račune. Ovi računi su numerisani počevši od `0'`. Prošireni ključevi (`xpub`, `xprv`...) se nalaze na ovom nivou dubine;
- `m / purpose' / coin-type' / account' / change /` označava putanju. Svaki nalog definisan na dubini 3 ima dve putanje na dubini 4: eksterni lanac i interni lanac (takođe nazvan "change"). Eksterni lanac izvodi adrese namenjene za javno deljenje, tj. adrese koje nam se nude kada kliknemo na "primi" u našem Wallet softveru. Interni lanac izvodi adrese koje nisu namenjene za javnu razmenu, uglavnom adrese za kusur. Eksterni lanac je identifikovan indeksom `0`, a interni lanac je identifikovan indeksom `1`. Primetićete da od ove dubine više ne vršimo ojačano izvođenje, već normalno izvođenje (nema apostrofa). Zahvaljujući ovom mehanizmu, u mogućnosti smo da izvedemo sve javne ključeve potomaka iz njihovog `xpub`;



- `m / purpose' / coin-type' / account' / change / Address-index` jednostavno označava broj primajućeg Address i njegov par ključeva, kako bi se razlikovao od svojih "srodnika" na istoj dubini na istoj grani. Na primer, prvi izvedeni Address ima indeks `0`, drugi Address ima indeks `1`, i tako dalje...


Na primer, ako moj prijemni Address ima put derivacije `m / 86' / 0' / 0' / 0 / 5`, možemo izvesti sledeće informacije:


- `86'` označava da pratimo standard derivacije BIP86 (Taproot / SegWit V1);
- `0'` označava da je to Bitcoin Address;
- `0'` označava da smo na prvom nalogu Wallet;
- `0` označava da je to eksterni Address;
- `5` označava da je to šesti eksterni Address ovog naloga.


![](../../dictionnaire/assets/18.webp)