---
term: KUNCI YANG DIPERPANJANG

---
Urutan karakter yang menggabungkan kunci (publik atau pribadi), kode rantai terkait, dan serangkaian metadata. Kunci yang diperluas mengkompilasi semua elemen yang diperlukan untuk menurunkan kunci anak ke dalam satu pengenal. Kunci ini digunakan pada dompet deterministik dan hirarkis dan dapat terdiri dari dua jenis: kunci publik yang diperluas (digunakan untuk mendapatkan kunci publik anak) atau kunci pribadi yang diperluas (digunakan untuk mendapatkan kunci pribadi dan kunci publik anak). Kunci yang diperluas dengan demikian mencakup beberapa bagian data yang berbeda, yang dijelaskan dalam BIP32, sesuai dengan urutannya:


- Awalan: `prv` dan `pub` adalah HRP (Human Readable Part) yang mengindikasikan apakah itu merupakan kunci pribadi yang diperluas (`prv`) atau kunci publik yang diperluas (`pub`). Huruf pertama dari awalan menunjukkan versi kunci yang diperluas: `x` untuk Legacy atau SegWit V1 pada Bitcoin, `t` untuk Legacy atau SegWit V1 pada Bitcoin Testnet, `y` untuk Nested SegWit pada Bitcoin, `u` untuk Nested SegWit pada Bitcoin Testnet, `z` untuk SegWit V0 pada Bitcoin, `v` untuk SegWit V0 pada Bitcoin Testnet.
- Kedalaman, yang mengindikasikan jumlah turunan dari kunci master untuk mencapai kunci yang diperluas;
- Sidik jari induk. Ini mewakili 4 byte pertama dari `HASH160` dari kunci publik induk;
- Indeks. Ini adalah nomor pasangan di antara saudara-saudaranya dari mana kunci yang diperluas diturunkan;
- Kode rantai;
- Sebuah byte padding jika itu adalah kunci privat `x00`;
- Kunci pribadi atau publik;
- Sebuah checksum. Ini mewakili 4 byte pertama dari `HASH256` dari sisa kunci yang diperluas.

Dalam prakteknya, kunci publik yang diperluas digunakan untuk menghasilkan alamat penerima dan untuk mengamati transaksi dari sebuah akun tanpa mengekspos kunci privat yang terkait. Hal ini dapat memungkinkan, sebagai contoh, pembuatan sebuah dompet yang disebut sebagai dompet "watch-only". Akan tetapi, penting untuk diperhatikan bahwa kunci publik yang diperluas merupakan informasi yang sensitif untuk privasi pengguna, karena pengungkapannya dapat memungkinkan pihak ketiga untuk melacak transaksi dan melihat saldo akun yang terkait.