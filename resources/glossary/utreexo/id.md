---
term: UTREEXO

---
Protokol yang didesain oleh Tadge Dryja untuk memadatkan set UTXO node Bitcoin menggunakan akumulator yang berdasarkan pada pohon Merkle. Tidak seperti set UTXO klasik yang membutuhkan ruang penyimpanan yang besar, Utreexo secara drastis mengurangi memori yang dibutuhkan dengan hanya menyimpan akar pohon Merkle. Hal ini memungkinkan node untuk memverifikasi keberadaan UTXO yang digunakan dalam input transaksi, tanpa harus menyimpan set lengkap UTXO. Dengan menggunakan Utreexo, setiap node hanya menyimpan sidik jari kriptografi yang disebut akar Merkle. Ketika transaksi dilakukan, pengguna memberikan bukti kepemilikan UTXO dan jalur Merkle yang sesuai. Dengan demikian, node dapat memverifikasi transaksi tanpa menyimpan seluruh set UTXO. Mari kita ambil contoh dengan diagram untuk memahami mekanisme ini:

![](../../dictionnaire/assets/15.webp)

Dalam contoh ini, saya sengaja mengurangi set UTXO menjadi 4 UTXO untuk memudahkan pemahaman. Pada kenyataannya, penting untuk membayangkan bahwa ada hampir 140 juta UTXO di Bitcoin pada saat saya menulis kalimat-kalimat ini. Dalam diagram ini, node Utreexo hanya perlu menyimpan Merkle Root dalam RAM. Jika node tersebut menerima transaksi yang menggunakan UTXO No. 3 (berwarna hitam), buktinya akan terdiri dari elemen-elemen berikut:


- UTXO 3;
- HASH 4;
- HASH 1-2.

Dengan informasi yang dikirimkan oleh pengirim transaksi, node Utreexo melakukan verifikasi berikut:


- Ini menghitung jejak UTXO 3, yang memberinya HASH 3;
- Ini menggabungkan HASH 3 dengan HASH 4;
- Ini menghitung jejak mereka, yang memberikan HASH 3-4;
- Ini menggabungkan HASH 3-4 dengan HASH 1-2;
- Ini menghitung jejak mereka, yang memberikannya akar Merkle.

Jika root Merkle yang diperolehnya melalui prosesnya sama dengan root Merkle yang tersimpan dalam RAM-nya, maka dapat dipastikan bahwa UTXO No. 3 memang merupakan bagian dari set UTXO.

Metode ini mengurangi kebutuhan RAM untuk operator node penuh. Akan tetapi, Utreexo memiliki keterbatasan, termasuk peningkatan ukuran blok karena adanya proof tambahan dan potensi ketergantungan node Utreexo pada Bridge Node untuk mendapatkan proof yang hilang. Bridge Node adalah node penuh tradisional yang menyediakan bukti yang diperlukan untuk node Utreexo, sehingga memungkinkan verifikasi penuh. Pendekatan ini menawarkan kompromi antara efisiensi dan desentralisasi, membuat validasi transaksi lebih mudah diakses oleh pengguna dengan sumber daya yang terbatas.