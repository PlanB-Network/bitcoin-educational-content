---
term: SIGHASH_NONE (0X02)
---

Jenis Bendera SigHash yang digunakan dalam tanda tangan transaksi Bitcoin untuk menunjukkan bahwa tanda tangan berlaku untuk semua input dari transaksi, tetapi tidak untuk outputnya. Penggunaan `SIGHASH_NONE` mengimplikasikan bahwa penandatangan hanya berkomitmen pada input, memungkinkan output tetap tidak ditentukan atau dapat dimodifikasi setelah penandatanganan. Jenis tanda tangan ini berguna dalam kasus di mana penandatangan ingin memberi wewenang kepada pihak lain untuk memutuskan bagaimana bitcoin akan didistribusikan dalam transaksi.