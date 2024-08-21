---
term: VOUT
---

Bitcoin'i tehingu kindel element, mis määrab saadetud vahendite sihtkoha. Tehing võib sisaldada mitut väljundit, millest igaüht identifitseeritakse unikaalselt tehingu identifikaatori (`txid`) ja indeksi nimega `vout` kombinatsiooniga. See indeks, alustades numbrist `0`, märgib väljundi positsiooni tehingu väljundite jadas. Seega tähistatakse esimest väljundit `"vout": 0`, teist `"vout": 1` ja nii edasi.

Iga `vout` hõlmab peamiselt kahte teabeosa:
* väärtus, väljendatuna bitcoinides, mis esindab saadetud summat;
* lukustusskript (`scriptPubKey`), mis sätestab tingimused, mille alusel saab vahendeid tulevikus uuesti kulutada.

`txid` ja konkreetse osa `vout` kombinatsioon moodustab seda, mida nimetatakse UTXO-ks, näiteks:

```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```