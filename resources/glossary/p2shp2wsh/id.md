---
term: P2SH-P2WSH
---

P2SH-P2WSH merupakan singkatan dari *Pay to Script Hash - Pay to Witness Script Hash*. Ini adalah model skrip standar yang digunakan untuk menetapkan kondisi pengeluaran pada sebuah UTXO, yang juga dikenal sebagai "Nested SegWit".

P2SH-P2WSH diperkenalkan bersamaan dengan implementasi SegWit pada Agustus 2017. Skrip ini mendeskripsikan sebuah P2WSH yang dibungkus dalam sebuah P2SH. Ini mengunci bitcoin berdasarkan hash dari sebuah skrip. Perbedaannya dari P2WSH klasik adalah bahwa skrip tersebut dibungkus dalam `redeemScript` dari P2SH klasik.

Skrip ini diciptakan pada saat peluncuran SegWit untuk memfasilitasi adopsinya. Ini memungkinkan penggunaan standar baru ini, bahkan dengan layanan atau dompet yang belum kompatibel secara native dengan SegWit. Saat ini, oleh karena itu, tidak lagi sangat relevan untuk menggunakan jenis skrip SegWit terbungkus ini, karena sebagian besar dompet telah mengimplementasikan SegWit native. Alamat P2SH-P2WSH ditulis menggunakan pengkodean `Base58Check` dan selalu dimulai dengan `3`, seperti alamat P2SH pada umumnya.