---
term: PEMBAYARAN SEDERHANA

---
Pola transaksi (atau model) yang digunakan dalam analisis rantai yang ditandai dengan konsumsi satu atau lebih UTXO sebagai input dan produksi 2 UTXO sebagai output. Oleh karena itu, model ini akan terlihat seperti ini:

![](../../dictionnaire/assets/5.webp)

Model pembayaran sederhana ini mengindikasikan bahwa kemungkinan besar kita sedang melakukan transaksi pengiriman atau pembayaran. Pengguna telah menggunakan UTXO mereka sendiri sebagai input untuk memenuhi output berupa UTXO pembayaran dan UTXO kembalian (kembalian dikembalikan ke pengguna yang sama). Oleh karena itu, kita tahu bahwa pengguna yang diamati kemungkinan besar tidak lagi memiliki salah satu dari dua UTXO dalam output (yang pembayaran), tetapi mereka masih memiliki UTXO lainnya (yang kembalian).