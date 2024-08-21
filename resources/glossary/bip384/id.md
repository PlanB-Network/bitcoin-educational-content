---
term: BIP384
---

Memperkenalkan fungsi `combo(KEY)` untuk deskriptor. Fungsi ini mendeskripsikan satu set skrip output yang mungkin untuk sebuah kunci publik tertentu. Dengan demikian, ini mencakup beberapa jenis skrip secara bersamaan, termasuk P2PK, P2PKH, P2WPKH, dan P2SH-P2WPKH. Jika kunci yang diberikan terkompresi, semua 4 jenis skrip diuji, dan jika tidak, hanya 2 jenis skrip Legacy yang diuji. Tujuannya adalah untuk menyederhanakan representasi kunci dalam deskriptor dengan menyediakan satu metode untuk menghasilkan berbagai varian skrip output berdasarkan kunci publik yang sama. BIP384 diimplementasikan bersama dengan semua BIP terkait deskriptor lainnya (kecuali BIP386) dalam versi 0.17 dari Bitcoin Core.