---
termi: OUTPOINT
---

Uniikki viittaus käyttämättömään transaktiotulosteeseen (UTXO). Se koostuu kahdesta elementistä:
* `txid`: transaktion tunniste, joka loi tulosteen;
* `vout`: tulosteen indeksi transaktiossa.

Näiden kahden elementin yhdistelmä identifioi tarkasti UTXO:n. Esimerkiksi, jos transaktiolla on `txid` arvona `abc...123` ja tulosteen indeksi on `0`, outpoint merkitään seuraavasti:

```text
abc...123:0
```

Outpointia käytetään uuden transaktion syötteissä (`vin`) osoittamaan, mikä UTXO on käytössä.

> ► *Termi "outpoint" käytetään usein synonyyminä termille "UTXO."*