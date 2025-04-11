---
term: P2SH-P2WPKH

---
P2SH-P2WPKH adalah singkatan dari *Bayar untuk Skrip Hash - Bayar untuk Menyaksikan Public Key Hash*. Ini adalah model skrip standar yang digunakan untuk menetapkan ketentuan pengeluaran pada UTXO, juga dikenal sebagai "Nested SegWit".

P2SH-P2WPKH diperkenalkan dengan implementasi SegWit pada bulan Agustus 2017. Skrip ini adalah P2WPKH yang dibungkus dalam P2SH. Skrip ini mengunci bitcoin berdasarkan hash dari kunci publik. Perbedaannya dengan P2WPKH klasik adalah skrip ini dibungkus dengan `redeemScript` dari P2SH klasik.

Skrip ini dibuat pada saat peluncuran SegWit untuk memfasilitasi pengadopsiannya. Skrip ini memungkinkan penggunaan standar baru ini, bahkan dengan layanan atau dompet yang belum kompatibel dengan SegWit. Ini adalah semacam skrip transisi menuju standar baru. Oleh karena itu, saat ini tidak lagi relevan untuk menggunakan jenis skrip SegWit yang dibungkus, karena sebagian besar dompet telah menerapkan SegWit asli. Alamat P2SH-P2WPKH ditulis menggunakan pengkodean `Base58Check` dan selalu diawali dengan `3`, seperti alamat P2SH lainnya.

> ► *`P2SH-P2WPKH` kadang-kadang juga disebut `P2WPKH bersarang di dalam P2SH`.*