---
term: BIP0008
---

Razvijen nakon debata o SegWit, koji je koristio BIP9 za svoju aktivaciju, BIP8 je Soft Fork metod aktivacije koji prirodno uključuje automatski UASF (*User-Activated Soft Fork*) mehanizam. Kao i BIP9, BIP8 koristi Miner signalizaciju, ali dodaje `LOT` (*Lock-in On Time out*) parametar. Ako je `LOT` postavljen na `true`, po isteku perioda signalizacije bez dostizanja potrebnog praga, automatski se pokreće UASF, forsirajući aktivaciju Soft Fork. Ovaj pristup primorava rudare da budu kooperativni ili rizikuju UASF nametnut od strane korisnika. Štaviše, za razliku od BIP9, BIP8 definiše period signalizacije na osnovu visine bloka, eliminišući potencijalne manipulacije kroz Hash stopu od strane rudara. BIP8 takođe omogućava postavljanje promenljivog praga glasanja i uvodi parametar za minimalnu visinu bloka za aktivaciju, dajući rudarima vreme da se pripreme i unapred signaliziraju svoj pristanak bez nužnog spremanja. Kada se Soft Fork aktivira putem BIP8 sa `LOT=true` parametrom, koristi se veoma agresivna metoda protiv rudara koji su odmah pod pritiskom potencijalnog UASF-a. Zaista, ostavlja im samo 2 izbora:


- Budite kooperativni i na taj način olakšajte proces aktivacije;
- Budite nesaradljivi, u kom slučaju korisnici automatski izvode UASF da nametnu Soft Fork.