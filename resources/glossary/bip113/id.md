---
term: BIP113
---

Memperkenalkan perubahan dalam perhitungan semua operasi timelock (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence`, dan `OP_CHECKSEQUENCEVERIFY`). Ini menentukan bahwa untuk mengevaluasi validitas dari timelocks, mereka sekarang harus dibandingkan dengan MTP (*Median Time Past*), yang merupakan median dari timestamp dari 11 blok terakhir. Sebelumnya, hanya timestamp dari blok sebelumnya yang digunakan. Metode ini membuat sistem lebih dapat diprediksi dan mencegah manipulasi referensi waktu oleh penambang. BIP113 diperkenalkan melalui soft fork pada 4 Juli 2016, bersamaan dengan BIP68 dan BIP112, diaktifkan untuk pertama kalinya menggunakan metode BIP9.