---
term: KUNCI PERPANJANGAN
---

Sebuah urutan karakter yang menggabungkan sebuah kunci (publik atau privat), kode rantai yang terkait, dan serangkaian metadata. Kunci perpanjangan mengkompilasi semua elemen yang diperlukan untuk menurunkan kunci anak ke dalam satu pengenal. Kunci ini digunakan dalam dompet deterministik dan hierarkis dan dapat berupa dua tipe: kunci publik perpanjangan (digunakan untuk menurunkan kunci publik anak) atau kunci privat perpanjangan (digunakan untuk menurunkan kunci privat dan publik anak). Sehingga, kunci perpanjangan mencakup beberapa potongan data yang berbeda, seperti dijelaskan dalam BIP32, dalam urutan:
* Awalan: `prv` dan `pub` adalah HRP (Human Readable Part) yang menunjukkan apakah itu kunci privat perpanjangan (`prv`) atau kunci publik perpanjangan (`pub`). Huruf pertama dari awalan menunjukkan versi dari kunci perpanjangan: `x` untuk Legacy atau SegWit V1 pada Bitcoin, `t` untuk Legacy atau SegWit V1 pada Bitcoin Testnet, `y` untuk Nested SegWit pada Bitcoin, `u` untuk Nested SegWit pada Bitcoin Testnet, `z` untuk SegWit V0 pada Bitcoin, `v` untuk SegWit V0 pada Bitcoin Testnet.
* Kedalaman, yang menunjukkan jumlah turunan dari kunci induk untuk mencapai kunci perpanjangan;
* Sidik jari induk. Ini mewakili 4 byte pertama dari `HASH160` dari kunci publik induk;
* Indeks. Ini adalah nomor pasangan di antara saudara kandungnya dari mana kunci perpanjangan diturunkan;
* Kode rantai;
* Byte padding jika itu adalah kunci privat `0x00`;
* Kunci privat atau publik;
* Checksum. Ini mewakili 4 byte pertama dari `HASH256` dari sisa kunci perpanjangan.

Dalam praktiknya, kunci publik perpanjangan digunakan untuk menghasilkan alamat penerimaan dan mengamati transaksi dari sebuah akun tanpa mengungkapkan kunci privat yang terkait. Ini dapat memungkinkan, misalnya, penciptaan dompet "hanya-pantau". Namun, penting untuk dicatat bahwa kunci publik perpanjangan adalah informasi sensitif untuk privasi pengguna, karena pengungkapannya dapat memungkinkan pihak ketiga untuk melacak transaksi dan melihat saldo dari akun yang terkait.