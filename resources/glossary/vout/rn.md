---
term: VOUT
definition: Igice kigize itunshwa ry'amafaranga rya Bitcoin cyerekana iyo amafaranga agiye, agaciro n'urufunguzo rwayo (locking script).
---

Ikintu kidasanzwe c’ugucuruza kwa Bitcoin kigena aho amahera yoherejwe aja. Ibikorwa bishobora kubamwo ibisohoka vyinshi, kimwe cose kigaragazwa mu buryo bwihariye n'uguhuza ikimenyetso c'ibikorwa (`txid`) n'urutonde rwitwa `vout`. Iyi index, itangura kuri `0`, igaragaza ikibanza c'isohoka mu rutonde rw'isohoka ry'ibikorwa. Gutyo, igisohoka ca mbere kizomenyekana na `"vout": 0`, ica kabiri na `"vout": 1`, n'ibindi.


Buri `vout` ahanini ishiramwo amakuru abiri:


- agaciro, kagaragazwa mu ma bitcoins, agereranya amahera yoherejwe;
- inyandiko yo gufunga (`scriptPubKey`) ivuga ibisabwa kugira ngo amafaranga asubire gukoreshwa mu gucuruza muri kazoza.


Ihuriro rya `txid` na `vout` ry’igice kinaka rituma haba ico bita UTXO, nk’akarorero:


```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```