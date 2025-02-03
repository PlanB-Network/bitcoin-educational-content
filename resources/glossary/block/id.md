---
term: BLOK

---
Struktur data dalam sistem Bitcoin. Sebuah blok berisi sekumpulan transaksi yang valid dan metadata yang terkandung dalam headernya. Setiap blok terhubung dengan blok berikutnya dengan hash dari headernya, sehingga membentuk blockchain. Blockchain bertindak sebagai server penanda waktu yang memungkinkan setiap pengguna untuk mengetahui semua transaksi yang telah terjadi, untuk memverifikasi tidak adanya suatu transaksi dan mencegah terjadinya pembelanjaan ganda. Transaksi diatur dalam sebuah pohon Merkle. Akumulator kriptografi ini memungkinkan untuk membuat intisari dari semua transaksi dalam sebuah blok, yang disebut "akar Merkle" Header dari sebuah blok berisi 6 elemen:


- Versi blok;
- Jejak dari blok sebelumnya;
- Akar dari pohon transaksi Merkle;
- Stempel waktu dari blok tersebut;
- Target kesulitan;
- The nonce.

Agar sebuah blok menjadi valid, blok tersebut harus memiliki header yang, setelah di-hash dengan `SHA256d`, menghasilkan sebuah digest yang kurang dari atau sama dengan target tingkat kesulitan.