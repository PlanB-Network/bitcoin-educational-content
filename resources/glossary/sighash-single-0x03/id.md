---
term: SIGHASH_SINGLE (0X03)

---
Jenis SigHash Flag yang digunakan dalam tanda tangan transaksi Bitcoin untuk mengindikasikan bahwa tanda tangan tersebut berlaku untuk semua input transaksi dan hanya untuk satu output, sesuai dengan indeks input yang sama yang ditandatangani. Dengan demikian, setiap input yang ditandatangani dengan `SIGHASH_SINGLE` secara khusus dihubungkan dengan output tertentu. Keluaran lainnya tidak terikat oleh tanda tangan dan oleh karena itu dapat dimodifikasi di kemudian hari. Jenis tanda tangan ini berguna dalam transaksi yang kompleks, di mana partisipan ingin menghubungkan input tertentu dengan output tertentu, sementara tetap memberikan fleksibilitas untuk output lain dari transaksi tersebut.