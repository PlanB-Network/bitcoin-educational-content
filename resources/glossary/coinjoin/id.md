---
term: COINJOIN

---
Coinjoin adalah sebuah teknik yang digunakan untuk mematahkan ketertelusuran bitcoin. Teknik ini bergantung pada transaksi kolaboratif dengan struktur tertentu dengan nama yang sama: transaksi coinjoin. Transaksi coinjoin membantu meningkatkan perlindungan privasi pengguna Bitcoin dengan membuatnya lebih sulit bagi pengamat eksternal untuk menganalisis transaksi. Struktur ini memungkinkan pencampuran beberapa koin dalam satu transaksi, sehingga menyulitkan untuk menentukan hubungan antara alamat input dan output.

Operasi umum coinjoin adalah sebagai berikut: pengguna yang berbeda ingin menggabungkan deposit sejumlah uang sebagai input transaksi. Input ini akan keluar sebagai output yang berbeda dengan jumlah yang sama. Pada akhir transaksi, tidak mungkin untuk menentukan output mana yang menjadi milik pengguna yang mana. Secara teknis tidak ada hubungan antara input dan output dari transaksi coinjoin. Hubungan antara setiap pengguna dan setiap UTXO terputus, dengan cara yang sama seperti sejarah setiap koin.

![](../../dictionnaire/assets/4.webp)

Untuk memungkinkan coinjoin tanpa ada pengguna yang kehilangan kendali atas dana mereka setiap saat, transaksi pertama kali dibuat oleh koordinator dan kemudian dikirimkan ke setiap pengguna. Setiap pengguna kemudian menandatangani transaksi tersebut setelah memverifikasi bahwa transaksi tersebut sesuai dengan keinginan mereka, dan kemudian semua tanda tangan ditambahkan ke dalam transaksi. Jika seorang pengguna atau koordinator mencoba untuk mencuri dana orang lain dengan memodifikasi hasil dari transaksi coinjoin, maka tanda tangan akan menjadi tidak valid dan transaksi akan ditolak oleh node. Ketika pencatatan output peserta dilakukan dengan menggunakan tanda tangan buta Chaum untuk menghindari hubungan dengan input, ini disebut sebagai "Chaumian coinjoin".

Mekanisme ini meningkatkan kerahasiaan transaksi tanpa memerlukan modifikasi pada protokol Bitcoin. Implementasi spesifik dari coinjoin, seperti Whirlpool, JoinMarket, atau Wabisabi, menawarkan solusi untuk memfasilitasi proses koordinasi di antara para partisipan dan meningkatkan efisiensi transaksi coinjoin. Berikut ini adalah contoh transaksi coinjoin:

```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```

Sulit untuk menentukan dengan pasti siapa yang pertama kali memperkenalkan ide coinjoin pada Bitcoin, dan siapa yang memiliki ide untuk menggunakan tanda tangan buta David Chaum dalam konteks ini. Sering kali dianggap bahwa Gregory Maxwell adalah orang pertama yang mendiskusikannya dalam [pesan di BitcoinTalk pada tahun 2013] (https://bitcointalk.org/index.php?topic=279249.0):

Menggunakan tanda tangan buta Chaum: Pengguna terhubung dan memberikan input (dan mengubah alamat) serta versi kriptografis yang dibutakan dari alamat yang ingin mereka kirimkan koin pribadi mereka; server menandatangani token dan mengembalikannya. Pengguna terhubung kembali secara anonim, membuka kedok alamat keluaran mereka, dan mengirimkannya kembali ke server. Server dapat melihat bahwa semua output telah ditandatangani olehnya dan, akibatnya, semua output berasal dari peserta yang valid. Kemudian, orang-orang terhubung kembali dan menandatangani.

Maxwell, G. (2013, Agustus 22). *CoinJoin: Privasi Bitcoin untuk dunia nyata*. Forum BitcoinTalk. https://bitcointalk.org/index.php?topic=279249.0

Akan tetapi, ada penyebutan sebelumnya, baik untuk tanda tangan Chaum dalam konteks pencampuran, maupun untuk coinjoin. [Pada bulan Juni 2011, Duncan Townsend mempresentasikan di BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) sebuah mixer yang menggunakan tanda tangan Chaum dengan cara yang sangat mirip dengan coinjoin Chaumian modern. Di thread yang sama, ada [pesan dari hashcoin sebagai tanggapan terhadap Duncan Townsend](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) untuk memperbaiki mixernya. Pesan ini menyajikan apa yang paling mirip dengan coinjoin. Ada juga penyebutan sistem yang serupa dalam [pesan dari Alex Mizrahi pada tahun 2012] (https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), ketika dia menasihati pencipta Tenebrix. Istilah "coinjoin" sendiri tidak ditemukan oleh Greg Maxwell, tetapi berasal dari ide Peter Todd.

> istilah "coinjoin" tidak memiliki terjemahan dalam bahasa Perancis. Beberapa pengguna bitcoin juga menggunakan istilah "campuran", "pencampuran", atau "campuran" untuk merujuk pada transaksi coinjoin. Pencampuran adalah proses yang digunakan di jantung coinjoin. Selain itu, penting untuk tidak mengacaukan pencampuran melalui coinjoin dengan pencampuran melalui aktor pusat yang memiliki bitcoin selama proses tersebut. Hal ini tidak ada hubungannya dengan coinjoin di mana pengguna tidak kehilangan kendali atas bitcoin mereka selama proses tersebut.*