---
term: TIMELOCK
---

Sebuah primitif kontrak pintar yang memungkinkan pengaturan kondisi berbasis waktu yang harus dipenuhi agar transaksi dapat ditambahkan ke dalam blok. Ada dua jenis timelock pada Bitcoin:
* Timelock absolut, yang menentukan momen tepat sebelum transaksi tidak dapat dimasukkan dalam blok;
* Timelock relatif, yang menetapkan penundaan dari penerimaan transaksi sebelumnya.
Timelock dapat didefinisikan baik sebagai tanggal yang dinyatakan dalam waktu Unix atau sebagai nomor blok. Akhirnya, timelock dapat diterapkan pada output transaksi dengan menggunakan opcode spesifik dalam skrip penguncian (`OP_CHECKLOCKTIMEVERIFY` atau `OP_CHECKSEQUENCEVERIFY`), atau ke seluruh transaksi dengan menggunakan bidang transaksi spesifik (`nLockTime` atau `nSequence`).