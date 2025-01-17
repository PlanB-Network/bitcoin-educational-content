---
term: OUTPOINT

---
Yksilöllinen viittaus käyttämättömään tapahtumalähteeseen (UTXO). Se koostuu kahdesta elementistä:


- `txid`: tulosteen luoneen tapahtuman tunniste;
- `vout`: tapahtuman tulosteen indeksi.

Näiden kahden elementin yhdistelmä tunnistaa UTXO:n tarkasti. Jos esimerkiksi transaktion `txid` on `abc...123` ja lähtöindeksi on `0`, ulostulopiste merkitään seuraavasti:

```text
abc...123:0
```

Ulosmenopistettä käytetään uuden tapahtuman syötteissä (`vin`) osoittamaan, mikä UTXO on käytössä.

> ► *Käsitettä "outpoint" käytetään usein synonyymisesti UTXO:n kanssa*