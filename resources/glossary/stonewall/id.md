---
term: TEMBOK BATU

---
Sebuah bentuk transaksi Bitcoin khusus yang bertujuan untuk meningkatkan privasi pengguna selama melakukan pembelanjaan dengan meniru koin bersama antara dua orang, tanpa benar-benar menjadi satu. Memang, transaksi ini tidak bersifat kolaboratif. Seorang pengguna dapat membuatnya sendiri, dengan hanya melibatkan UTXO mereka sendiri sebagai input. Oleh karena itu, Anda dapat membuat transaksi Stonewall untuk setiap kesempatan, tanpa perlu melakukan sinkronisasi dengan pengguna lain.

Pengoperasian transaksi Stonewall adalah sebagai berikut: pada input transaksi, pengirim menggunakan 2 UTXO milik mereka. Transaksi kemudian menghasilkan 4 output, 2 di antaranya akan memiliki jumlah yang sama persis. Dua lainnya merupakan perubahan. Di antara 2 output dengan jumlah yang sama, hanya satu yang akan benar-benar masuk ke penerima pembayaran.

Dengan demikian, hanya ada 2 peran dalam transaksi Stonewall:


- Pengirim, yang melakukan pembayaran yang sebenarnya;
- Penerima, yang mungkin tidak menyadari sifat spesifik dari transaksi dan hanya menunggu pembayaran dari pengirim.

![](../../dictionnaire/assets/33.webp)

Transaksi Stonewall tersedia di aplikasi Samourai Wallet dan perangkat lunak Sparrow Wallet.

Struktur Stonewall menambahkan banyak entropi pada transaksi dan mengaburkan jejak untuk analisis rantai. Dari luar, transaksi seperti ini dapat diartikan sebagai sebuah koin kecil antara dua orang. Akan tetapi pada kenyataannya, sama seperti transaksi Stonewall x2, transaksi ini adalah sebuah pembayaran. Dengan demikian, metode ini menghasilkan ketidakpastian dalam analisis rantai, atau bahkan mengarah pada jejak yang salah. Bahkan jika pengamat eksternal berhasil mengidentifikasi pola transaksi Stonewall, mereka tidak akan memiliki semua informasi. Mereka tidak akan dapat menentukan mana dari dua UTXO dengan jumlah yang sama yang sesuai dengan pembayaran. Selain itu, mereka tidak akan dapat menentukan apakah dua UTXO yang dimasukkan berasal dari dua orang yang berbeda atau milik satu orang yang menggabungkannya. Poin terakhir ini disebabkan oleh fakta bahwa transaksi Stonewall x2 mengikuti pola yang persis sama dengan transaksi Stonewall. Dari luar dan tanpa informasi konteks tambahan, tidak mungkin untuk membedakan transaksi Stonewall dengan transaksi Stonewall x2. Akan tetapi, yang pertama bukanlah transaksi kolaboratif, sedangkan yang kedua adalah transaksi kolaboratif. Hal ini menambah keraguan tentang pengeluaran ini.