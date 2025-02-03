---
term: VOUT

---
Specifický prvek transakce Bitcoin, který určuje místo určení odeslaných prostředků. Transakce může obsahovat více výstupů, z nichž každý je jednoznačně identifikován kombinací identifikátoru transakce (`txid`) a indexu zvaného `vout`. Tento index, začínající na `0`, označuje pozici výstupu v posloupnosti výstupů transakce. První výstup bude tedy označen symbolem `"vout": 0`, druhý výstup bude označen symbolem `"vout": 1` a tak dále.

Každý `vout` obsahuje především dvě informace:


- hodnota vyjádřená v bitcoinech, která představuje odeslanou částku;
- zamykací skript (`scriptPubKey`), který stanoví podmínky nutné k tomu, aby mohly být finanční prostředky v budoucí transakci znovu použity.

Kombinace `txid` a `vout` konkrétního kusu tvoří například tzv. UTXO:

```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```