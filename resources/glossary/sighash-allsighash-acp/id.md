---
term: SIGHASH_ALL/SIGHASH_ACP

---
Jenis SigHash Flag (`x81`) yang dikombinasikan dengan pengubah `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) yang digunakan dalam tanda tangan transaksi Bitcoin. Kombinasi ini menentukan bahwa tanda tangan berlaku untuk semua output dan hanya untuk input tertentu dari transaksi. `SIGHASH_ALL | SIGHASH_ANYONECANPAY` mengijinkan partisipan lain untuk menambahkan input tambahan pada transaksi setelah tanda tangan awal. Ini sangat berguna dalam skenario kolaboratif, seperti transaksi _crowdfunding_, di mana kontributor yang berbeda dapat menambahkan input mereka sendiri sambil menjaga kebenaran output yang dilakukan oleh penandatangan awal.
