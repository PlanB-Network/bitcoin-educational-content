---
term: UTREEXO

---
Protokol yang didesain oleh Tadge Dryja untuk memadatkan set UTXO node Bitcoin menggunakan akumulator yang berdasarkan pada pohon Merkle. Tidak seperti set UTXO klasik yang membutuhkan ruang penyimpanan yang besar, _Utreexo_ secara drastis mengurangi memori yang dibutuhkan dengan hanya menyimpan akar pohon Merkle. Hal ini memungkinkan node untuk memverifikasi keberadaan UTXO yang digunakan dalam input transaksi, tanpa harus menyimpan set lengkap UTXO. Dengan menggunakan _Utreexo_, setiap node hanya menyimpan sidik jari kriptografi yang disebut akar Merkle. Ketika transaksi dilakukan, pengguna memberikan bukti kepemilikan UTXO dan jalur Merkle yang sesuai. Dengan demikian, node dapat memverifikasi transaksi tanpa menyimpan seluruh set UTXO. Mari kita ambil contoh dengan diagram untuk memahami mekanisme ini:

![](../../dictionnaire/assets/15.webp)

Dalam contoh ini, saya sengaja mengurangi set UTXO menjadi 4 UTXO untuk memudahkan pemahaman. Pada kenyataannya, penting untuk membayangkan bahwa ada hampir 140 juta UTXO di Bitcoin pada saat saya menulis kalimat-kalimat ini. Dalam diagram ini, node _Utreexo_ hanya perlu menyimpan akar Merkle dalam RAM. Jika node tersebut menerima transaksi yang menggunakan UTXO No. 3 (berwarna hitam), buktinya akan terdiri dari elemen-elemen berikut:


- UTXO 3;
- HASH 4;
- HASH 1-2.

Dengan informasi yang dikirimkan oleh pengirim transaksi, node Utreexo melakukan verifikasi berikut:


- Menghitung jejak UTXO 3, yang memberinya HASH 3;
- Menggabungkan HASH 3 dengan HASH 4;
- Menghitung _imprint_ mereka, yang memberikan HASH 3-4;
- Menggabungkan HASH 3-4 dengan HASH 1-2;
- Menghitung _imprint_ mereka, yang memberikan akar Merkle.

Jika akar Merkle yang diperolehnya melalui prosesnya sama dengan akar Merkle yang tersimpan dalam RAM-nya, maka dapat dipastikan bahwa UTXO No. 3 memang merupakan bagian dari set UTXO.

Metode ini mengurangi kebutuhan RAM untuk operator node penuh. Akan tetapi, Utreexo memiliki keterbatasan, termasuk peningkatan ukuran blok karena adanya _proof_ tambahan dan potensi ketergantungan node Utreexo pada _Bridge Node_ untuk mendapatkan _proof_ yang hilang. _Bridge Node_ adalah node penuh tradisional yang menyediakan bukti yang diperlukan untuk node Utreexo, sehingga memungkinkan verifikasi penuh. Pendekatan ini menawarkan kompromi antara efisiensi dan desentralisasi, membuat validasi transaksi lebih mudah diakses oleh pengguna dengan sumber daya yang terbatas.
