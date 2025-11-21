---
term: RIPEMD160

---
Singkatan dari *Research and development in Advanced Communications technologies in Europe Integrity Primitives Evaluation Message Digest 160*, yang merupakan fungsi _hash_ kriptografi yang menghasilkan 160-bit _digest_ dari input sembarang. Fungsi ini digunakan dalam Bitcoin untuk mengubah kunci publik menjadi alamat penerima untuk standar Legacy dan SegWit v0 (untuk SegWit v1, kunci publik tidak di-_hash_). Proses ini pertama-tama melibatkan penerapan fungsi _hash_ `SHA256` pada kunci publik, diikuti dengan penerapan `RIPEMD160` pada hasilnya. Kombinasi dari dua fungsi _hash_ yang berbeda ini dikenal sebagai `HASH160` dalam konteks Bitcoin. `RIPEMD160` juga digunakan dalam dompet deterministik dan hirarkis untuk menghitung _hash_ kunci. Secara khusus, `HASH160` digunakan untuk menghitung sidik jari dari sebuah kunci induk, kemudian dimasukkan ke dalam metadata dari kunci yang diperluas (xpub, xprv...).
