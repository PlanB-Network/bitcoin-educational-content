---
term: SIGHASH_SINGLE/SIGHASH_ACP

---
Jenis SigHash Flag (`x83`) yang dikombinasikan dengan pengubah `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) yang digunakan dalam tanda tangan transaksi Bitcoin. Kombinasi ini menetapkan bahwa tanda tangan hanya berlaku untuk satu input tertentu dan hanya untuk output yang memiliki indeks yang sama dengan input tersebut. Input dan output lainnya dapat ditambahkan atau dimodifikasi oleh pihak lain. Konfigurasi ini berguna untuk transaksi kolaboratif di mana para partisipan dapat menambahkan input mereka sendiri untuk mendanai output tertentu.