---
term: OUTPOINT

---
Unikaalne viide kasutamata tehingu väljundile (UTXO). Koosneb kahest elemendist:


- `txid`: väljundi loonud tehingu identifikaator;
- `vout`: tehingu väljundi indeks.

Nende kahe elemendi kombinatsioon identifitseerib täpselt UTXO. Näiteks kui tehingu `txid` on `abc...123` ja väljundindeks on `0`, märgitakse väljundpunktiks:

```text
abc...123:0
```

Uue tehingu sisendites (`vin`) kasutatakse väljundpunkti, et näidata, millist UTXO-d kulutatakse.

> ► *Mõistet "outpoint" kasutatakse sageli sünonüümina terminiga "UTXO "*