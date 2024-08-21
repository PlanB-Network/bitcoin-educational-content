---
term: OUTPOINT
---

Referensi unik ke output transaksi yang belum terpakai (UTXO). Ini terdiri dari dua elemen:
* `txid`: pengenal transaksi yang menciptakan output;
* `vout`: indeks output dalam transaksi.

Kombinasi dari kedua elemen ini secara tepat mengidentifikasi sebuah UTXO. Sebagai contoh, jika sebuah transaksi memiliki `txid` `abc...123` dan indeks outputnya adalah `0`, maka outpoint akan dicatat sebagai:

```text
abc...123:0
```

Outpoint digunakan dalam input (`vin`) dari transaksi baru untuk menunjukkan UTXO mana yang sedang digunakan.

> ► *Istilah "outpoint" sering digunakan secara sinonim dengan "UTXO."*