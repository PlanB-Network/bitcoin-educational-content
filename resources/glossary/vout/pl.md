---
term: VOUT
---

Określony element transakcji Bitcoin, który określa miejsce docelowe wysłanych środków. Transakcja może zawierać wiele wyjść, z których każde jest jednoznacznie identyfikowane przez kombinację identyfikatora transakcji (`txid`) i indeksu zwanego `vout`. Indeks ten, zaczynający się od `0`, oznacza pozycję wyjścia w sekwencji wyjść transakcji. Tak więc, pierwsze wyjście będzie oznaczone przez `"vout": 0`, drugie przez `"vout": 1` i tak dalej.


Każdy `vout` zawiera przede wszystkim dwie informacje:


- wartość wyrażona w bitcoinach, która reprezentuje wysłaną kwotę;
- skrypt blokujący (`scriptPubKey`), który określa warunki wymagane do ponownego wydania środków w przyszłej transakcji.


Połączenie `txid` i `vout` konkretnego elementu tworzy to, co nazywane jest na przykład UTXO:


```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```