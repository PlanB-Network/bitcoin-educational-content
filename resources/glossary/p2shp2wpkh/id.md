---
term: P2SH-P2WPKH

---
P2SH-P2WPKH adalah singkatan dari *Pay to Script Hash - Pay to Witness Public Key Hash*, yang merupakan model skrip standar yang digunakan untuk menetapkan ketentuan pengeluaran pada UTXO, juga dikenal sebagai "_Nested SegWit_".

P2SH-P2WPKH diperkenalkan dengan implementasi SegWit pada bulan Agustus 2017. Skrip ini adalah P2WPKH yang dibungkus dalam P2SH. Skrip ini mengunci bitcoin berdasarkan _hash_ dari kunci publik. Perbedaannya dengan P2WPKH klasik adalah skrip ini dibungkus dengan `redeemScript` dari P2SH klasik.

Skrip ini dibuat pada saat peluncuran SegWit untuk memfasilitasi adopsinya. Skrip ini memungkinkan penggunaan standar baru ini, bahkan dengan layanan atau dompet yang belum kompatibel dengan SegWit. Skrip ini dapat dianggap sebagai semacam skrip transisi menuju standar baru. Oleh karena itu, saat ini tidak lagi relevan untuk menggunakan jenis skrip SegWit yang dibungkus, karena sebagian besar dompet telah menerapkan SegWit asli. Alamat P2SH-P2WPKH ditulis menggunakan pengkodean `Base58Check` dan selalu diawali dengan `3`, seperti alamat P2SH lainnya.

> ► *`P2SH-P2WPKH` kadang-kadang juga disebut `P2WPKH nested in P2SH`.*
