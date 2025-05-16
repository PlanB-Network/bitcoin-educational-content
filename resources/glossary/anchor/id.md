---
term: Anchor
---

Dalam protokol RGB, sebuah Anchor mewakili sekumpulan data sisi klien yang digunakan untuk membuktikan penyertaan satu Commitment dalam sebuah transaksi. Dalam protokol RGB, sebuah Anchor terdiri dari Elements berikut ini:




- transaction ID Bitcoin (txid) dari Witness Transaction;
- Multi Protocol Commitment (MPC);
- Deterministic Bitcoin Commitment (DBC);
- Bukti Transaksi Ekstra (ETP) jika mekanisme Tapret Commitment digunakan.


Oleh karena itu, Anchor berfungsi untuk membuat hubungan yang dapat diverifikasi antara transaksi Bitcoin tertentu dengan data pribadi yang divalidasi oleh protokol RGB. Ini menjamin bahwa data ini memang termasuk dalam Blockchain, tanpa konten persisnya dipublikasikan.