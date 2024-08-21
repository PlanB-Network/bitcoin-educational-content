---
term: ASICBOOST
---

ASICBOOST adalah metode optimisasi algoritmik yang ditemukan pada tahun 2016, dirancang untuk meningkatkan efisiensi penambangan Bitcoin sekitar 20% dengan mengurangi jumlah perhitungan yang diperlukan untuk setiap percobaan hash dari header. Teknik ini memanfaatkan fitur dari fungsi hash SHA256, yang digunakan untuk penambangan, yang membagi data menjadi blok sebelum memprosesnya. ASICBOOST mempertahankan salah satu blok ini tidak berubah di berbagai percobaan hashing, memungkinkan penambang hanya melakukan sebagian dari pekerjaan untuk blok ini dalam beberapa percobaan. Berbagi data ini memungkinkan penggunaan kembali hasil dari perhitungan sebelumnya, sehingga mengurangi jumlah total perhitungan yang diperlukan untuk menemukan hash yang valid.

ASICBOOST dapat digunakan dalam dua bentuk: ASICBOOST Terang (Overt ASICBOOST) dan ASICBOOST Tersembunyi (Covert ASICBOOST). Bentuk ASICBOOST Terang terlihat oleh semua orang, karena melibatkan penggunaan bidang `nVersion` dari blok sebagai nonce, dan tidak mengubah `Nonce` yang sebenarnya. Bentuk Tersembunyi berusaha menyembunyikan modifikasi ini dengan menggunakan pohon Merkle. Namun, metode kedua ini menjadi kurang efektif sejak diperkenalkannya SegWit karena pohon Merkle kedua, yang meningkatkan jumlah perhitungan yang diperlukan untuk menggunakannya.

Secara ringkas, ASICBOOST memungkinkan penambang untuk tidak harus melakukan SHA256 yang benar-benar lengkap untuk semua percobaan hashing, karena sebagian dari hasil tetap tidak berubah, yang mempercepat pekerjaan penambang.