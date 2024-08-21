---
term: MTP (MEDIAN TIME PAST)
---

Konsep ini digunakan dalam protokol Bitcoin untuk menentukan margin pada cap waktu konsensus jaringan. MTP didefinisikan sebagai median dari cap waktu dari 11 blok yang ditambang terakhir. Penggunaan indikator ini membantu menghindari ketidaksepakatan di antara node tentang waktu yang tepat dalam kasus adanya perbedaan. MTP awalnya digunakan untuk memverifikasi validitas cap waktu blok terhadap masa lalu. Sejak BIP113, ini juga digunakan sebagai referensi untuk waktu jaringan untuk memverifikasi validitas transaksi time-lock (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence`, dan `OP_CHECKSEQUENCEVERIFY`).