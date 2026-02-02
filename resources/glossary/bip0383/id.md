---
term: BIP0383

definition: Fungsi multi() dan sortedmulti() untuk mendeskripsikan skrip multisig dalam deskriptor.
---
Memperkenalkan fungsi `multi(NUM, KEY, ..., KEY)` dan `sortedmulti(NUM, KEY, ..., KEY)` untuk deskriptor. Fungsi-fungsi ini memungkinkan deskripsi skrip _multisignature_ dalam deskriptor, dengan `sortedmulti` mengurutkan kunci publik dalam urutan leksikografis untuk memastikan kompatibilitas selama impor. BIP383 diimplementasikan bersama dengan semua BIP terkait deskriptor lainnya (kecuali BIP386) dalam versi 0.17 Bitcoin Core.
