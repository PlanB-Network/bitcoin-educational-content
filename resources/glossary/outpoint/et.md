---
term: OUTPOINT
---

Unikaalne viide kulutamata tehinguväljundile (UTXO). See koosneb kahest elemendist:
* `txid`: tehingu identifikaator, mis lõi väljundi;
* `vout`: väljundi indeks tehingus.

Nende kahe elemendi kombinatsioon identifitseerib täpselt UTXO. Näiteks, kui tehingul on `txid` `abc...123` ja väljundi indeks on `0`, siis outpoint märgitakse kui:

```text
abc...123:0
```

Outpointi kasutatakse uue tehingu sisendites (`vin`), et näidata, millist UTXO-d kulutatakse.

> ► *Terminit "outpoint" kasutatakse sageli sünonüümina "UTXO-le".*