---
term: VOUT

---
Elemen spesifik dari transaksi Bitcoin yang menentukan tujuan dana yang dikirim. Sebuah transaksi dapat mencakup beberapa output, masing-masing diidentifikasi secara unik dengan kombinasi pengenal transaksi (`txid`) dan indeks yang disebut `vout`. Indeks ini, dimulai dari `0`, menandai posisi output dalam urutan output transaksi. Dengan demikian, output pertama akan ditandai dengan `"vout": 0`, yang kedua dengan `"vout": 1`, dan seterusnya.

Setiap `vout` pada dasarnya merangkum dua buah informasi:


- nilai, dinyatakan dalam bitcoin, yang mewakili jumlah yang dikirim;
- skrip penguncian (`scriptPubKey`) yang menetapkan persyaratan yang diperlukan agar dana dapat digunakan lagi dalam transaksi di masa mendatang.

Kombinasi dari `txid` dan `vout` dari bagian tertentu membentuk apa yang disebut UTXO, misalnya:

```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```