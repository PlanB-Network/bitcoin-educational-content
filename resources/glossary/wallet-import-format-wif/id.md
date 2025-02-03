---
term: FORMAT IMPOR DOMPET (WIF)

---
Sebuah metode untuk mengkodekan kunci pribadi Bitcoin dengan cara yang dapat diimpor atau diekspor dengan lebih mudah di antara dompet yang berbeda. WIF didasarkan pada pengkodean `Base58Check`, yang mencakup informasi mengenai versi, kompresi kunci publik yang sesuai, dan checksum untuk mendeteksi kesalahan dalam pengetikan. Kunci pribadi WIF dimulai dengan karakter `5` untuk kunci yang tidak dikompresi, atau `K` dan `L` untuk kunci yang dikompresi, dan berisi semua karakter yang diperlukan untuk merekonstruksi kunci pribadi yang asli. Format WIF menyediakan sebuah sarana standar untuk mentransfer kunci pribadi antara perangkat lunak dompet yang berbeda.