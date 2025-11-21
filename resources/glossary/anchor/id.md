---
term: JANGKAR (ANCHOR)
---

Dalam protokol RGB, sebuah _Anchor_ mewakili sekumpulan data sisi klien yang digunakan untuk membuktikan penyertaan satu komitmen dalam sebuah transaksi. Dalam protokol RGB, sebuah Anchor terdiri dari beberapa bagian berikut ini:

- _Transaction ID_ Bitcoin (txid) dari _Witness Transaction_;
- _Multi Protocol Commitment_ (MPC);
- _Deterministic Bitcoin Commitment_ (DBC);
- _Extra Transaction Proof_ (ETP) jika mekanisme _Tapret Commitment_ digunakan.

Oleh karena itu, _Anchor_ berfungsi untuk membuat hubungan yang dapat diverifikasi antara transaksi Bitcoin tertentu dengan data pribadi yang divalidasi oleh protokol RGB. Hal ini menjamin bahwa data ini memang termasuk dalam _Blockchain_, tanpa perlu membuka kontennya.
