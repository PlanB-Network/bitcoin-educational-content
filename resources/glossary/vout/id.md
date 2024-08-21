---
term: VOUT
---

Elemen spesifik dari sebuah transaksi Bitcoin yang menentukan tujuan dari dana yang dikirim. Sebuah transaksi dapat mencakup beberapa output, masing-masing diidentifikasi secara unik oleh kombinasi dari pengenal transaksi (`txid`) dan sebuah indeks yang disebut `vout`. Indeks ini, dimulai dari `0`, menandai posisi dari output dalam urutan output transaksi. Dengan demikian, output pertama akan ditandai dengan `"vout": 0`, yang kedua dengan `"vout": 1`, dan seterusnya.

Setiap `vout` terutama mengkapsulkan dua potongan informasi:
* nilai, dinyatakan dalam bitcoin, yang mewakili jumlah yang dikirim;
* sebuah skrip penguncian (`scriptPubKey`) yang menetapkan kondisi yang diperlukan agar dana dapat dihabiskan lagi dalam transaksi masa depan.

Kombinasi dari `txid` dan `vout` dari sebuah bagian tertentu membentuk apa yang disebut UTXO, contohnya:

```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```