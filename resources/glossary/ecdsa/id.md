---
term: ECDSA

---
Singkatan dari "Algoritma Tanda Tangan Digital Kurva Elips." Ini adalah algoritme tanda tangan digital berdasarkan kriptografi kurva elips (ECC). Ini adalah varian dari DSA (Algoritma Tanda Tangan Digital). ECDSA menggunakan sifat kurva elips untuk memberikan tingkat keamanan yang sebanding dengan algoritma kunci publik tradisional, seperti RSA, sambil menggunakan ukuran kunci yang jauh lebih kecil. ECDSA memungkinkan pembuatan pasangan kunci (kunci publik dan privat) serta pembuatan dan verifikasi tanda tangan digital.

Dalam konteks Bitcoin, ECDSA digunakan untuk mendapatkan public key dari private key. Ini juga digunakan untuk menandatangani transaksi, untuk memenuhi skrip untuk membuka kunci bitcoin dan membelanjakannya. Kurva elips yang digunakan dalam ECDSA Bitcoin adalah `secp256k1`, yang didefinisikan dengan persamaan $y^2 = x^3 + 7$. Algoritma ini telah digunakan sejak awal kemunculan Bitcoin pada tahun 2009. Saat ini, algoritme ini digunakan bersama protokol Schnorr, algoritme tanda tangan digital lain yang diperkenalkan dengan Taproot pada tahun 2021.