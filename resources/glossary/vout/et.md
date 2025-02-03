---
term: VOUT

---
Bitcoini tehingu konkreetne element, mis määrab saadetud raha sihtkoha. Tehing võib sisaldada mitut väljundit, millest igaüks on üheselt identifitseeritav tehingu identifikaatori (`txid`) ja indeksi `vout` kombinatsiooni abil. See indeks, mis algab numbriga `0`, tähistab väljundi positsiooni tehingu väljundite järjestuses. Seega tähistab esimest väljundit `"vout": 0`, teine `"vout": 1` ja nii edasi.

Iga "vout" sisaldab peamiselt kahte teavet:


- väärtus, mis on väljendatud bitcoinides ja mis kujutab endast saadetud summat;
- lukustusskript (`scriptPubKey`), mis määrab kindlaks tingimused, mis on vajalikud selleks, et raha saaks tulevikus tehingu käigus uuesti kulutada.

Konkreetse tüki `txid` ja `vout` kombinatsioon moodustab näiteks nn UTXO:

```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```