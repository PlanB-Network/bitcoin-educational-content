---
term: KUNCI WAKTU

---
Sebuah primitif kontrak pintar yang memungkinkan pengaturan kondisi berbasis waktu yang harus dipenuhi agar sebuah transaksi dapat ditambahkan ke dalam blok. Terdapat dua jenis penguncian waktu pada Bitcoin:


- Penguncian waktu absolut, yang menentukan waktu yang tepat sebelum transaksi tidak dapat dimasukkan ke dalam blok;
- Pengunci waktu relatif, yang menetapkan penundaan dari penerimaan transaksi sebelumnya.

Penguncian waktu dapat didefinisikan sebagai tanggal yang dinyatakan dalam waktu Unix atau sebagai nomor blok. Terakhir, penguncian waktu dapat diterapkan pada output transaksi dengan menggunakan opcode tertentu dalam skrip penguncian (`OP_CHECKLOCKTIMEVERIFY` atau `OP_CHECKSEQUENCEVERIFY`), atau ke seluruh transaksi dengan menggunakan bidang transaksi tertentu (`nLockTime` atau `nSequence`).