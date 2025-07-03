---
term: OVERT ASICBOOST

---
Versi AsicBoost yang terbuka dan transparan. AsicBoost adalah sebuah teknik optimasi algoritmik yang digunakan dalam penambangan Bitcoin. Penambang yang menggunakan versi _overt_ memanipulasi bidang `nVersion` dari blok kandidat dan menggunakan modifikasi ini sebagai _nonce_ tambahan. Metode ini membuat field `Nonce` yang sebenarnya dari blok tidak berubah selama setiap percobaan _hashing_, sehingga mengurangi perhitungan yang dibutuhkan untuk setiap SHA256, dengan menjaga beberapa data tetap sama di antara percobaan. Versi ini dapat dideteksi oleh publik dan tidak menyembunyikan modifikasinya dari seluruh jaringan, tidak seperti versi _covert_ dari AsicBoost.
