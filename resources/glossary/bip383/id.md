---
term: BIP383

---
Memperkenalkan fungsi `multi(NUM, KEY, ..., KEY)` dan `sortedmulti(NUM, KEY, ..., KEY)` untuk deskriptor. Fungsi-fungsi ini memungkinkan deskripsi skrip multisignature dalam deskriptor, dengan `sortedmulti` mengurutkan kunci publik dalam urutan leksikografis untuk memastikan kompatibilitas selama impor. BIP383 diimplementasikan bersama dengan semua BIP terkait deskriptor lainnya (kecuali BIP386) dalam versi 0.17 Bitcoin Core.