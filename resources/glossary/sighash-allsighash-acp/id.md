---
term: SIGHASH_ALL/SIGHASH_ACP
---

Jenis Bendera SigHash (`0x81`) yang dikombinasikan dengan modifikasi `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) yang digunakan dalam tanda tangan transaksi Bitcoin. Kombinasi ini menentukan bahwa tanda tangan berlaku untuk semua output dan hanya untuk input spesifik dari transaksi tersebut. `SIGHASH_ALL | SIGHASH_ANYONECANPAY` memungkinkan peserta lain untuk menambahkan input tambahan ke dalam transaksi setelah tanda tangan awal. Ini sangat berguna dalam skenario kolaboratif, seperti transaksi crowdfunding, di mana kontributor berbeda dapat menambahkan input mereka sendiri sambil mempertahankan integritas dari output yang telah dikomit oleh penandatangan awal.