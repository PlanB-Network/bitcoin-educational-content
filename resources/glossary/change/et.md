---
term: MUUTUS

---
Bitcoini tehingute kontekstis viitab UTXO-le, mis on loodud pärast tegeliku makse rahuldamist järelejäänud vahenditega. Kui kasutatakse UTXOsid, mille bitcoinide summa on suurem kui tegeliku makse ja tehingutasude jaoks vajalik summa, on ülejääk UTXO, mis tagastatakse rahakoti sisemisele aadressile, mida nimetatakse vahetusaadressiks. Vahetuse aadress esindab seda UTXO-d. Näiteks, kui soovite maksta baguette'i eest, mis maksab `4,000 sats`, mille UTXO on `10,000 sats`, siis tekitate oma tehingus muutuse `6,000 sats` (kui me ei arvesta tehingutasusid).

![](../../dictionnaire/assets/16.webp)

> ► *Kuigi seda kasutatakse harva, võiksime muutusest rääkides nimetada seda ka "valuutaks" (change given)