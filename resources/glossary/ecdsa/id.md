---
term: ECDSA
---

Singkatan dari "Elliptic Curve Digital Signature Algorithm." Ini adalah algoritma tanda tangan digital yang berbasis pada kriptografi kurva eliptik (ECC). ECDSA merupakan varian dari DSA (Digital Signature Algorithm). ECDSA memanfaatkan sifat-sifat kurva eliptik untuk menyediakan tingkat keamanan yang sebanding dengan algoritma kunci publik tradisional, seperti RSA, sambil menggunakan ukuran kunci yang jauh lebih kecil. ECDSA memungkinkan untuk generasi pasangan kunci (kunci publik dan kunci privat) serta pembuatan dan verifikasi tanda tangan digital.

Dalam konteks Bitcoin, ECDSA digunakan untuk menurunkan kunci publik dari kunci privat. Ini juga digunakan untuk menandatangani transaksi, agar memenuhi skrip untuk membuka bitcoin dan menghabiskannya. Kurva eliptik yang digunakan dalam ECDSA Bitcoin adalah `secp256k1`, yang didefinisikan oleh persamaan $y^2 = x^3 + 7$. Algoritma ini telah digunakan sejak awal mula Bitcoin pada tahun 2009. Saat ini, algoritma ini berbagi tempat dengan protokol Schnorr, algoritma tanda tangan digital lain yang diperkenalkan dengan Taproot pada tahun 2021.