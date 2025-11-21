---
term: VOUT
---

Specifičan element Bitcoin transakcije koji određuje odredište poslatih sredstava. Transakcija može uključivati više izlaza, od kojih je svaki jedinstveno identifikovan kombinacijom identifikatora transakcije (`txid`) i indeksa nazvanog `vout`. Ovaj indeks, počevši od `0`, označava poziciju izlaza u nizu izlaza transakcije. Dakle, prvi izlaz će biti označen sa `"vout": 0`, drugi sa `"vout": 1`, i tako dalje.


Svaki `vout` prvenstveno obuhvata dva dela informacija:


- vrednost, izražena u bitkoinima, koja predstavlja poslatu sumu;
- skripta zaključavanja (`scriptPubKey`) koja propisuje uslove potrebne za ponovno trošenje sredstava u budućoj transakciji.


Kombinacija `txid` i `vout` određenog dela formira ono što se naziva UTXO, na primer:


```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```