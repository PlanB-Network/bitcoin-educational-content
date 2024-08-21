---
term: VOUT
---

Specifický prvek Bitcoinové transakce, který určuje cíl odeslaných prostředků. Transakce může obsahovat více výstupů, z nichž každý je jednoznačně identifikován kombinací identifikátoru transakce (`txid`) a indexu nazývaného `vout`. Tento index, začínající na `0`, označuje pozici výstupu v sekvenci výstupů transakce. Takže první výstup bude označen jako `"vout": 0`, druhý jako `"vout": 1` a tak dále.

Každý `vout` primárně zahrnuje dvě informace:
* hodnotu vyjádřenou v bitcoinech, která představuje odeslanou částku;
* uzamykací skript (`scriptPubKey`), který stanovuje podmínky nutné pro opětovné vynaložení prostředků v budoucí transakci.

Kombinace `txid` a `vout` konkrétního prvku tvoří to, co se nazývá UTXO, například:

```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```