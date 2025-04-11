---
term: SIGHASH_NONE (0X02)

---
Jenis Bendera SigHash yang digunakan dalam tanda tangan transaksi Bitcoin untuk mengindikasikan bahwa tanda tangan tersebut berlaku untuk semua input transaksi, tetapi tidak untuk outputnya. Penggunaan `SIGHASH_NONE` mengimplikasikan bahwa penanda tangan hanya berkomitmen pada input, sehingga output tidak dapat ditentukan atau dimodifikasi setelah penandatanganan. Jenis tanda tangan ini berguna jika penanda tangan ingin memberikan wewenang kepada pihak lain untuk menentukan bagaimana bitcoin akan didistribusikan dalam transaksi.