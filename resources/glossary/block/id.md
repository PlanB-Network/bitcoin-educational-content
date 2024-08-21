---
term: BLOCK
---

Struktur data dalam sistem Bitcoin. Sebuah blok berisi kumpulan transaksi yang valid dan metadata yang terkandung dalam header-nya. Setiap blok dihubungkan ke blok berikutnya melalui hash dari header-nya, dengan demikian membentuk blockchain. Blockchain bertindak sebagai server penanda waktu yang memungkinkan setiap pengguna untuk mengetahui semua transaksi yang telah lalu, untuk memverifikasi ketiadaan sebuah transaksi dan mencegah pengeluaran ganda. Transaksi disusun dalam sebuah pohon Merkle. Akumulator kriptografis ini memungkinkan untuk produksi ringkasan dari semua transaksi dalam sebuah blok, yang disebut "akar Merkle." Header dari sebuah blok mengandung 6 elemen:
* Versi dari blok;
* Cap dari blok sebelumnya;
* Akar dari pohon Merkle transaksi;
* Cap waktu dari blok;
* Target kesulitan;
* Nonce.

Agar sebuah blok dianggap valid, ia harus memiliki header yang, setelah di-hash dengan `SHA256d`, menghasilkan ringkasan yang kurang dari atau sama dengan target kesulitan.