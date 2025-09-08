---
term: BIP0113

---
Memperkenalkan perubahan dalam perhitungan semua operasi penguncian waktu (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence`, dan `OP_CHECKSEQUENCEVERIFY`). BIP ini menetapkan bahwa untuk mengevaluasi validitasnya, sekarang cap waktu harus dibandingkan dengan MTP (*Median Time Past*), yang merupakan median dari cap waktu dari 11 blok terakhir. Sebelumnya, hanya cap waktu dari blok sebelumnya yang digunakan sebagai patokan. Metode ini membuat sistem lebih mudah diprediksi dan mencegah manipulasi referensi waktu oleh para penambang. BIP113 diperkenalkan melalui _soft fork_ pada tanggal 4 Juli 2016, bersamaan dengan BIP68 dan BIP112, yang diaktifkan pertama kali menggunakan metode BIP9.
