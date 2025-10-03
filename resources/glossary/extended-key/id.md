---
term: EXTENDED KEY

---
Urutan karakter yang menggabungkan kunci (publik atau privat), kode rantai terkait, dan serangkaian metadata. _Extended key_ mengkompilasi semua elemen yang diperlukan untuk menurunkan kunci anak ke dalam satu pengenal. Kunci ini digunakan pada dompet deterministik hirarkis dan dapat terdiri dari dua jenis: _extended public key_ (digunakan untuk mendapatkan kunci publik anak) atau _extended private key_ (digunakan untuk mendapatkan kunci pribadi dan kunci publik anak). _Extended key_ dengan demikian mencakup beberapa bagian data yang berbeda, yang dijelaskan dalam BIP32, sesuai dengan urutannya:


- Awalan: `prv` dan `pub` adalah HRP (_Human Readable Part_) yang mengindikasikan apakah itu merupakan _extended private key_ (`prv`) atau _extended public key_ (`pub`). Huruf pertama dari awalan menunjukkan versi kunci yang diperluas: `x` untuk Legacy atau SegWit V1 pada Bitcoin, `t` untuk Legacy atau SegWit V1 pada Bitcoin Testnet, `y` untuk Nested SegWit pada Bitcoin, `u` untuk Nested SegWit pada Bitcoin Testnet, `z` untuk SegWit V0 pada Bitcoin, `v` untuk SegWit V0 pada Bitcoin Testnet.
- Kedalaman, yang mengindikasikan jumlah turunan dari kunci _master_ untuk mencapai _extended key_ terkait;
- Sidik jari induk. Ini mewakili 4 byte pertama dari `HASH160` dari kunci publik induk;
- Indeks, yang merupakan nomor pasangan di antara saudara-saudaranya dari mana kunci yang diperluas diturunkan;
- Kode rantai;
- Sebuah _byte padding_ jika itu adalah kunci privat `x00`;
- Kunci privat atau publik;
- Sebuah _checksum_. Ini mewakili 4 byte pertama dari `HASH256` dari sisa _extended key_.

Dalam prakteknya, kunci publik yang diperluas digunakan untuk menghasilkan alamat penerima dan untuk mengamati transaksi dari sebuah akun tanpa mengekspos kunci privat yang terkait. Hal ini dapat memungkinkan, sebagai contoh, pembuatan sebuah dompet yang disebut sebagai dompet "_watch-only_". Akan tetapi, penting untuk diperhatikan bahwa _extended public key_ merupakan informasi yang sensitif untuk privasi pengguna, karena pengungkapannya dapat memungkinkan pihak ketiga untuk melacak transaksi dan melihat saldo akun yang bersangkutan.
