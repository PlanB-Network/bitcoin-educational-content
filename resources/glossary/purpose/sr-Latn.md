---
term: CILJ
---

U determinističkim i hijerarhijskim (HD) portfolijima, svrha, definisana BIP43, predstavlja specifičan nivo derivacije. Ovaj indeks, smešten na prvom nivou dubine derivacionog stabla (`m / purpose' /`), identifikuje derivacioni standard usvojen od strane portfolija, kako bi se olakšala kompatibilnost između različitih softvera za upravljanje portfolijima. Na primer, u slučaju SegWit adresa (BIP84), svrha je zabeležena kao `/84'/`. Ova metoda omogućava da ključevi budu efikasno organizovani između različitih Address tipova unutar jednog HD portfolija. Standardni indeksi koji se koriste su :




- Za P2PKH: `44'` ;
- Za P2WPKH-ugnežđen-u-P2SH: `49'` ;
- Za P2WPKH: `84'` ;
- Za P2TR: `86'`.