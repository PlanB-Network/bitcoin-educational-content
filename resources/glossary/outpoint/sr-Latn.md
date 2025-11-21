---
term: OUTPOINT
---

Jedinstvena referenca na neiskorišćeni izlaz transakcije (UTXO). Sastoji se od dva Elements:


- `txid`: identifikator transakcije koja je kreirala izlaz;
- `vout`: indeks izlaza u transakciji.


Kombinacija ova dva Elements precizno identifikuje UTXO. Na primer, ako transakcija ima `txid` od `abc...123` i izlazni indeks je `0`, izlazna tačka će biti zabeležena kao:


```text
abc...123:0
```


Outpoint se koristi u ulazima (`vin`) nove transakcije da označi koji UTXO se troši.


> ► *Termin "outpoint" se često koristi kao sinonim za "UTXO."*