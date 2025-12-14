---
term: PSEUDO-RANDOM

---
Kata sifat ini digunakan untuk mendeskripsikan urutan angka yang, meskipun merupakan hasil dari proses deterministik, menampilkan karakteristik yang mendekati karakteristik urutan acak yang ideal. Konsep keacakan yang ideal menyiratkan tidak adanya prediktabilitas dan korelasi antara elemen-elemen yang berurutan. Bilangan acak semu dihasilkan oleh algoritma deterministik dan oleh karena itu, secara teori, dapat diprediksi sepenuhnya jika kita mengetahui kondisi awal generator.

_Pseudo-random number generator_ (PRNG) adalah sebuah algoritma yang digunakan untuk menghasilkan angka-angka tersebut. Algoritma ini biasanya dimulai dari nilai awal, atau "_seed_", dan kemudian menerapkan serangkaian transformasi matematis untuk menghasilkan urutan angka. Karena sifat determinasi ini, penting untuk keamanan kriptografi bahwa _seed_ awal tetap dirahasiakan. Urutan acak semu banyak digunakan di berbagai bidang, termasuk kriptografi, karena mereka menunjukkan perilaku yang tampaknya acak yang cukup untuk banyak aplikasi. Evaluasi kualitas PRNG didasarkan pada sejauh mana keluarannya mendekati keacakan yang sebenarnya dalam hal distribusi, korelasi, dan sifat statistik lainnya. Dalam konteks Bitcoin, bilangan _pseudo-random_ digunakan untuk menghasilkan kunci privat, atau untuk menghasilkan _seed_ untuk dompet deterministik dan hirarkis (dompet HD).
