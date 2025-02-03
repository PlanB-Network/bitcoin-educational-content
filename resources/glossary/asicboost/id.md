---
term: ASICBOOST

---
ASICBOOST adalah sebuah metode optimasi algoritmik yang ditemukan pada tahun 2016, yang dirancang untuk meningkatkan efisiensi penambangan Bitcoin sekitar 20% dengan mengurangi jumlah perhitungan yang diperlukan untuk setiap upaya hash pada header. Teknik ini mengeksploitasi fitur fungsi hash SHA256, yang digunakan untuk menambang, yang membagi data menjadi beberapa blok sebelum memprosesnya. ASICBOOST mempertahankan salah satu dari blok-blok ini tanpa perubahan di beberapa percobaan hashing, sehingga penambang hanya melakukan sebagian pekerjaan untuk blok ini selama beberapa percobaan. Pembagian data ini memungkinkan penggunaan kembali hasil dari perhitungan sebelumnya, sehingga mengurangi jumlah total perhitungan yang dibutuhkan untuk menemukan hash yang valid.

ASICBOOST dapat digunakan dalam dua bentuk: ASICBOOST terbuka dan ASICBOOST terselubung. Bentuk Overt ASICBOOST dapat dilihat oleh semua orang, karena melibatkan penggunaan bidang `nVersion` pada blok sebagai nonce, dan tidak mengubah `Nonce` yang sebenarnya. Bentuk Covert berusaha untuk menyembunyikan modifikasi ini dengan menggunakan pohon Merkle. Akan tetapi, metode kedua ini menjadi kurang efektif sejak diperkenalkannya SegWit karena adanya pohon Merkle kedua, yang meningkatkan jumlah perhitungan yang dibutuhkan untuk menggunakannya.

Singkatnya, ASICBOOST memungkinkan para penambang untuk tidak perlu melakukan SHA256 yang benar-benar lengkap untuk semua usaha hashing, karena sebagian hasilnya tetap tidak berubah, yang mempercepat pekerjaan para penambang.