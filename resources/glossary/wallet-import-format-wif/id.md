---
term: WALLET IMPORT FORMAT (WIF)
---

Sebuah metode untuk mengkodekan kunci privat Bitcoin sehingga dapat diimpor atau diekspor dengan lebih mudah antar dompet yang berbeda. WIF berbasis pada pengkodean `Base58Check`, yang mencakup informasi tentang versi, kompresi dari kunci publik yang sesuai, dan checksum untuk deteksi kesalahan dalam pengetikan. Sebuah kunci privat WIF dimulai dengan karakter `5` untuk kunci yang tidak dikompresi, atau `K` dan `L` untuk kunci yang dikompresi, dan mengandung semua karakter yang diperlukan untuk merekonstruksi kunci privat asli. Format WIF menyediakan sarana standar untuk mentransfer kunci privat antar perangkat lunak dompet yang berbeda.