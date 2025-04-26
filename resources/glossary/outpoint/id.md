---
term: TUJUAN

---
Referensi unik untuk output transaksi yang tidak terpakai (UTXO). Terdiri dari dua elemen:


- `txid`: pengidentifikasi transaksi yang menciptakan output;
- `vout`: indeks output dalam transaksi.

Kombinasi dari kedua elemen ini secara tepat mengidentifikasi UTXO. Sebagai contoh, jika sebuah transaksi memiliki `txid` sebesar `abc... 123` dan indeks output adalah `0`, titik keluar akan dicatat sebagai:

```text
abc...123:0
```

Titik keluar digunakan dalam input (`vin`) dari transaksi baru untuk menunjukkan UTXO mana yang dibelanjakan.

> ► *Istilah "outpoint" sering digunakan secara sinonim dengan "UTXO. "*