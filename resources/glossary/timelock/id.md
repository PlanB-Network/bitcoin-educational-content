---
term: TIMELOCK

---
Sebuah versi primitif kontrak pintar yang memungkinkan pengaturan kondisi berbasis waktu yang harus dipenuhi agar sebuah transaksi dapat ditambahkan ke dalam blok. Terdapat dua jenis penguncian waktu pada Bitcoin:


- _Timelock_ absolut, yang menentukan waktu yang tepat sebelum transaksi tidak dapat dimasukkan ke dalam blok;
- _Timelock_ relatif, yang menetapkan penundaan dari penerimaan transaksi sebelumnya.

_Timelock_ dapat didefinisikan sebagai tanggal yang dinyatakan dalam waktu Unix atau sebagai nomor blok. Terakhir, penguncian waktu dapat diterapkan pada output transaksi dengan menggunakan _opcode_ tertentu dalam skrip penguncian (`OP_CHECKLOCKTIMEVERIFY` atau `OP_CHECKSEQUENCEVERIFY`), atau ke seluruh transaksi dengan menggunakan bidang transaksi tertentu (`nLockTime` atau `nSequence`).
