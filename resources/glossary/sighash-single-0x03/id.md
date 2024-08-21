---
term: SIGHASH_SINGLE (0X03)
---

Jenis Bendera SigHash yang digunakan dalam tanda tangan transaksi Bitcoin untuk menunjukkan bahwa tanda tangan berlaku untuk semua input dari transaksi dan hanya untuk satu output, yang sesuai dengan indeks dari input yang sama yang ditandatangani. Dengan demikian, setiap input yang ditandatangani dengan `SIGHASH_SINGLE` secara spesifik dikaitkan dengan output tertentu. Output lainnya tidak diikat oleh tanda tangan dan oleh karena itu dapat dimodifikasi nanti. Jenis tanda tangan ini berguna dalam transaksi yang kompleks, di mana peserta ingin menghubungkan input tertentu dengan output spesifik, sambil memberikan fleksibilitas untuk output lain dari transaksi tersebut.