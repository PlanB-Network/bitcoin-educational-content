---
term: BIP384

---
Memperkenalkan fungsi `combo(KEY)` untuk deskriptor. Fungsi ini menjelaskan sekumpulan skrip keluaran yang mungkin untuk kunci publik yang diberikan. Dengan demikian, fungsi ini mencakup beberapa jenis skrip pada saat yang sama, termasuk P2PK, P2PKH, P2WPKH, dan P2SH-P2WPKH. Jika kunci yang diberikan dikompresi, semua 4 jenis skrip akan diuji, dan jika tidak, hanya 2 jenis skrip Legacy yang akan diuji. Tujuannya adalah untuk menyederhanakan representasi kunci dalam deskriptor dengan menyediakan metode tunggal untuk menghasilkan varian skrip keluaran yang berbeda berdasarkan kunci publik yang sama. BIP384 diimplementasikan bersama dengan semua BIP yang berhubungan dengan deskriptor lainnya (kecuali BIP386) di versi 0.17 Bitcoin Core.