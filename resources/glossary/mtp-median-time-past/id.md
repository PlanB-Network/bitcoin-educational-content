---
term: MTP (MEDIAN TIME PAST)

---
Konsep ini digunakan dalam protokol Bitcoin untuk menentukan batasan pada stempel waktu konsensus jaringan. MTP didefinisikan sebagai median dari stempel waktu dari 11 blok terakhir yang ditambang. Penggunaan indikator ini membantu untuk menghindari perselisihan di antara node tentang waktu yang tepat jika terjadi perbedaan. MTP pada awalnya digunakan untuk memverifikasi keabsahan stempel waktu blok dengan masa lalu. Sejak BIP113, MTP juga digunakan sebagai referensi waktu jaringan untuk memverifikasi validitas transaksi _time-lock_ (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence`, dan `OP_CHECKSEQUENCEVERIFY`).
