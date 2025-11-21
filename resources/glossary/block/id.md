---
term: BLOK

---
Struktur data dalam sistem Bitcoin. Sebuah blok berisi sekumpulan transaksi yang valid dan metadata yang terkandung dalam headernya. Setiap blok terhubung dengan blok berikutnya dengan hash dari headernya, sehingga membentuk blockchain. Blockchain bertindak sebagai server penanda waktu yang memungkinkan setiap pengguna untuk mengetahui semua transaksi yang telah terjadi, untuk memverifikasi tidak adanya suatu transaksi dan mencegah terjadinya pembelanjaan ganda. Transaksi diatur dalam sebuah pohon Merkle. Akumulator kriptografi ini memungkinkan untuk membuat intisari dari semua transaksi dalam sebuah blok, yang disebut "akar Merkle" Header dari sebuah blok berisi 6 elemen:


- Versi blok;
- _Hash_ dari blok sebelumnya;
- Akar dari pohon transaksi Merkle;
- Stempel waktu dari blok tersebut;
- Target kesulitan;
- Nilai _nonce_.

Agar sebuah blok dianggap valid, blok tersebut harus memiliki _header_ yang, setelah di-_hashing_ dengan `SHA256d`, menghasilkan sebuah _hash_ yang kurang dari atau sama dengan target tingkat kesulitan.
