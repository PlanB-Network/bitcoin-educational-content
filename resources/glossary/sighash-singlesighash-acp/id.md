---
term: SIGHASH_SINGLE/SIGHASH_ACP
---

Jenis Bendera SigHash (`0x83`) yang dikombinasikan dengan modifikasi `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) yang digunakan dalam tanda tangan transaksi Bitcoin. Kombinasi ini menentukan bahwa tanda tangan hanya berlaku untuk satu input spesifik dan hanya untuk output yang memiliki indeks yang sama dengan input ini. Input dan output lain dapat ditambahkan atau dimodifikasi oleh pihak lain. Konfigurasi ini berguna untuk transaksi kolaboratif di mana peserta dapat menambahkan input mereka sendiri untuk membiayai output spesifik.