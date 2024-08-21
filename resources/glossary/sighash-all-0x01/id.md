---
term: SIGHASH_ALL (0X01)
---

Jenis Bendera SigHash yang digunakan dalam tanda tangan transaksi Bitcoin untuk menunjukkan bahwa tanda tangan berlaku untuk semua komponen transaksi. Dengan menggunakan `SIGHASH_ALL`, penandatangan menutupi semua input dan semua output. Ini berarti bahwa baik input maupun output tidak dapat dimodifikasi setelah tanda tangan tanpa membuatnya menjadi tidak valid. Jenis Bendera SigHash ini adalah yang paling umum dalam transaksi Bitcoin, karena menjamin kefinalan dan integritas transaksi secara lengkap.