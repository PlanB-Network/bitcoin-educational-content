---
term: OUTPOINT

---
En unik referanse til en ubrukt transaksjonsutgang (UTXO). Den består av to elementer:


- `txid`: identifikatoren til transaksjonen som skapte utdataene;
- `vout`: indeksen for utdata i transaksjonen.

Kombinasjonen av disse to elementene identifiserer en UTXO nøyaktig. Hvis for eksempel en transaksjon har en `txid` på `abc...123` og utgangsindeksen er `0`, vil utpunktet bli notert som:

```text
abc...123:0
```

Utpunktet brukes i inndataene (`vin`) til en ny transaksjon for å indikere hvilken UTXO som skal brukes.

> begrepet "outpoint" brukes ofte synonymt med "UTXO"