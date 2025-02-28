---
term: P2SH-P2WSH

---
P2SH-P2WSH adalah singkatan dari *Bayar ke Script Hash - Bayar untuk Menyaksikan Script Hash*. Ini adalah model skrip standar yang digunakan untuk menetapkan kondisi pengeluaran pada UTXO, juga dikenal sebagai "Nested SegWit".

P2SH-P2WSH diperkenalkan dengan implementasi SegWit pada bulan Agustus 2017. Skrip ini menjelaskan P2WSH yang dibungkus dalam P2SH. Skrip ini mengunci bitcoin berdasarkan hash dari sebuah skrip. Perbedaannya dengan P2WSH klasik adalah skrip ini dibungkus dengan `redeemScript` dari P2SH klasik.

Skrip ini dibuat pada saat peluncuran SegWit untuk memfasilitasi pengadopsiannya. Skrip ini memungkinkan penggunaan standar baru ini, bahkan dengan layanan atau dompet yang belum kompatibel dengan SegWit. Saat ini, penggunaan skrip SegWit yang dibungkus seperti ini sudah tidak relevan lagi, karena sebagian besar dompet telah menerapkan SegWit asli. Alamat P2SH-P2WSH ditulis menggunakan pengkodean `Base58Check` dan selalu diawali dengan `3`, seperti alamat P2SH lainnya.