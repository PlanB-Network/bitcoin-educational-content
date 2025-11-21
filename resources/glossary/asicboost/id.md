---
term: ASICBOOST

---
ASICBOOST adalah sebuah metode optimasi algoritmik yang ditemukan pada tahun 2016, yang dirancang untuk meningkatkan efisiensi penambangan Bitcoin sekitar 20% dengan mengurangi jumlah perhitungan yang diperlukan untuk setiap upaya _hashing_ pada _block header_. Teknik ini memanfaatkan fitur fungsi hash SHA256, yang digunakan untuk menambang dengan membagi data menjadi beberapa blok sebelum memprosesnya. ASICBOOST mempertahankan salah satu blok ini agar tetap tidak berubah selama beberapa percobaan _hashing_, memungkinkan penambang hanya mengerjakan sebagian dari proses untuk blok tersebut dalam beberapa percobaan. Pembagian data ini memungkinkan penggunaan kembali hasil dari perhitungan sebelumnya, sehingga mengurangi jumlah total perhitungan yang dibutuhkan untuk menemukan _hash_ yang valid.

ASICBOOST dapat digunakan dalam dua bentuk: ASICBOOST terbuka (_Overt ASICBOOST_) dan ASICBOOST terselubung (_Covert ASICBOOST_). Bentuk _Overt ASICBOOST_ dapat dilihat oleh semua orang, karena melibatkan penggunaan _tab_ `nVersion` pada blok sebagai _nonce_, dan tidak mengubah `Nonce` yang sebenarnya. Bentuk _Covert_ berusaha untuk menyembunyikan modifikasi ini dengan menggunakan pohon Merkle. Akan tetapi, metode kedua ini menjadi kurang efektif sejak diperkenalkannya SegWit karena adanya pohon Merkle kedua. Hal ini membuat jumlah perhitungan yang dibutuhkan untuk menggunakan _Covert ASICBOOST_ menjadi lebih banyak.

Singkatnya, ASICBOOST memungkinkan para penambang untuk tidak perlu melakukan SHA256 secara keseluruhan untuk tiap percobaan _hashing_, karena sebagian hasilnya tetap tidak berubah, yang mempercepat pekerjaan para penambang.
