---
term: P2SH-P2WPKH
---

P2SH-P2WPKH merupakan singkatan dari *Pay to Script Hash - Pay to Witness Public Key Hash*. Ini adalah model skrip standar yang digunakan untuk menetapkan kondisi pengeluaran pada sebuah UTXO, yang juga dikenal sebagai "Nested SegWit".

P2SH-P2WPKH diperkenalkan bersamaan dengan implementasi SegWit pada Agustus 2017. Skrip ini adalah P2WPKH yang dibungkus dalam sebuah P2SH. Ini mengunci bitcoin berdasarkan hash dari kunci publik. Perbedaannya dari P2WPKH klasik adalah bahwa skrip ini dibungkus dalam `redeemScript` dari P2SH klasik.

Skrip ini diciptakan pada saat peluncuran SegWit untuk memfasilitasi adopsinya. Ini memungkinkan penggunaan standar baru ini, bahkan dengan layanan atau dompet yang belum kompatibel secara asli dengan SegWit. Ini adalah semacam skrip transisi menuju standar baru. Saat ini, oleh karena itu, tidak lagi sangat relevan untuk menggunakan jenis skrip SegWit yang dibungkus ini, karena sebagian besar dompet telah mengimplementasikan SegWit asli. Alamat P2SH-P2WPKH ditulis menggunakan pengkodean `Base58Check` dan selalu dimulai dengan `3`, seperti alamat P2SH pada umumnya.

> ► *`P2SH-P2WPKH` juga terkadang disebut `P2WPKH-nested-in-P2SH`.*