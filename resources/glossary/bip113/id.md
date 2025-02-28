---
term: BIP113

---
Memperkenalkan perubahan dalam perhitungan semua operasi penguncian waktu (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence`, dan `OP_CHECKSEQUENCEVERIFY`). Ini menetapkan bahwa untuk mengevaluasi validitas timestamp, mereka sekarang harus dibandingkan dengan MTP (*Median Time Past*), yang merupakan median dari cap waktu dari 11 blok terakhir. Sebelumnya, hanya cap waktu dari blok sebelumnya yang digunakan. Metode ini membuat sistem lebih mudah diprediksi dan mencegah manipulasi referensi waktu oleh para penambang. BIP113 diperkenalkan melalui soft fork pada tanggal 4 Juli 2016, bersamaan dengan BIP68 dan BIP112, yang diaktifkan pertama kali menggunakan metode BIP9.