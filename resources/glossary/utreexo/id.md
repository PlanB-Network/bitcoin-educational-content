---
term: UTREEXO
---

Protokol yang dirancang oleh Tadge Dryja untuk mengkompakkan set UTXO node Bitcoin menggunakan akumulator berbasis pohon Merkle. Tidak seperti set UTXO klasik yang memerlukan ruang penyimpanan yang signifikan, Utreexo secara drastis mengurangi memori yang dibutuhkan dengan hanya menyimpan akar pohon Merkle. Ini memungkinkan node untuk memverifikasi keberadaan UTXO yang digunakan dalam input transaksi, tanpa harus menyimpan set UTXO lengkap. Dengan menggunakan Utreexo, setiap node hanya menyimpan sidik jari kriptografis yang disebut akar Merkle. Ketika sebuah transaksi dilakukan, pengguna menyediakan bukti kepemilikan UTXO dan jalur Merkle yang sesuai. Dengan demikian, node dapat memverifikasi transaksi tanpa menyimpan set UTXO secara keseluruhan. Mari kita ambil contoh dengan diagram untuk memahami mekanisme ini:

![](../../dictionnaire/assets/15.png)

Dalam contoh ini, saya sengaja mengurangi set UTXO menjadi 4 UTXO untuk memudahkan pemahaman. Dalam kenyataannya, penting untuk membayangkan bahwa ada hampir 140 juta UTXO di Bitcoin pada saat menulis baris ini. Dalam diagram ini, node Utreexo hanya perlu menyimpan Akar Merkle dalam RAM. Jika menerima transaksi yang menghabiskan UTXO No. 3 (dalam hitam), buktinya akan terdiri dari elemen berikut:
* UTXO 3;
* HASH 4;
* HASH 1-2.

Dengan informasi yang ditransmisikan oleh pengirim transaksi, node Utreexo melakukan verifikasi berikut:
* Menghitung sidik jari UTXO 3, yang memberinya HASH 3;
* Menggabungkan HASH 3 dengan HASH 4;
* Menghitung sidik jari mereka, yang memberinya HASH 3-4;
* Menggabungkan HASH 3-4 dengan HASH 1-2;
* Menghitung sidik jari mereka, yang memberinya akar Merkle.

Jika akar Merkle yang diperoleh melalui prosesnya sama dengan akar Merkle yang disimpan dalam RAM-nya, maka node tersebut yakin bahwa UTXO No. 3 memang bagian dari set UTXO.
Metode ini mengurangi kebutuhan RAM untuk operator node penuh. Namun, Utreexo memiliki keterbatasan, termasuk peningkatan ukuran blok karena bukti tambahan dan ketergantungan potensial node Utreexo pada Bridge Nodes untuk mendapatkan bukti yang hilang. Bridge Nodes adalah node penuh tradisional yang menyediakan bukti yang diperlukan untuk node Utreexo, sehingga memungkinkan verifikasi penuh. Pendekatan ini menawarkan kompromi antara efisiensi dan desentralisasi, membuat validasi transaksi lebih mudah diakses oleh pengguna dengan sumber daya terbatas.