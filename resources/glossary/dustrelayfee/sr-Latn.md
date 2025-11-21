---
term: DUSTRELAYFEE
---

Pravilo standardizacije koje koriste mrežni čvorovi da odrede šta smatraju "Dust limitom." Ovaj parametar postavlja stopu naknade u Sats po virtualnom kilobajtu (Sats/kvB) koja služi kao referenca za izračunavanje da li je vrednost UTXO manja od potrebnih naknada za uključivanje u transakciju. Zaista, UTXO se smatra "Dust" na Bitcoin ako zahteva više u naknadama za prenos nego što je vrednost koju sam predstavlja. Izračunavanje ovog limita je sledeće:


```text
limit = (input size + output size) * fee rate
```


Kako se zahtevana stopa naknade za transakciju koja treba da bude uključena u Bitcoin blok konstantno menja, parametar `DustRelayFee` omogućava svakom čvoru da definiše stopu naknade koja se koristi u ovoj kalkulaciji. Podrazumevano, na Bitcoin Core, ova vrednost je postavljena na 3,000 Sats/kvB. Na primer, za izračunavanje Dust limita za P2PKH ulaz i izlaz, koji mere 148 i 34 bajta respektivno, kalkulacija bi bila:


```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```


To znači da čvor o kojem je reč neće prosleđivati transakcije uključujući P2PKH osiguran UTXO čija je vrednost manja od 546 Sats.