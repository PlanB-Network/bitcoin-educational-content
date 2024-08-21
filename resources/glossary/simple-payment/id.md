---
term: PEMBAYARAN SEDERHANA
---

Pola transaksi (atau model) yang digunakan dalam analisis rantai yang ditandai dengan penggunaan satu atau lebih UTXO dalam input dan produksi 2 UTXO dalam output. Model ini akan terlihat seperti ini:

![](../../dictionnaire/assets/5.png)

Model pembayaran sederhana ini menunjukkan bahwa kita kemungkinan berada dalam kehadiran transaksi pengiriman atau pembayaran. Pengguna telah menggunakan UTXO mereka sendiri dalam input untuk memenuhi dalam output sebuah UTXO pembayaran dan sebuah UTXO kembalian (kembalian dikembalikan ke pengguna yang sama). Oleh karena itu, kita tahu bahwa pengguna yang diamati kemungkinan tidak lagi memiliki salah satu dari dua UTXO dalam output (yang pembayaran), tetapi mereka masih memiliki UTXO lainnya (yang kembalian).