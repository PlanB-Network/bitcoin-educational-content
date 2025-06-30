---
term: COINJOIN

---
_Coinjoin_ adalah sebuah teknik yang digunakan untuk mematahkan ketertelusuran bitcoin. Teknik ini bergantung pada transaksi kolaboratif dengan struktur tertentu dengan nama yang sama: transaksi _coinjoin_. Transaksi _coinjoin_ membantu meningkatkan perlindungan privasi pengguna Bitcoin dengan membuatnya lebih sulit bagi pengamat eksternal untuk menganalisis detail transaksi. Struktur ini memungkinkan pencampuran beberapa koin dalam satu transaksi, sehingga menyulitkan untuk menentukan hubungan antara alamat input dan output.

Operasi umum _coinjoin_ adalah sebagai berikut: pengguna yang berbeda ingin menggabungkan deposit sejumlah uang sebagai input transaksi. Input ini akan keluar sebagai output yang berbeda dengan jumlah yang sama. Pada akhir transaksi, tidak mungkin untuk menentukan output mana yang menjadi milik pengguna yang mana. Secara teknis tidak ada hubungan antara input dan output dari transaksi _coinjoin_. Hubungan antara setiap pengguna dan setiap UTXO terputus, dengan cara yang sama seperti sejarah setiap koin tersebut.

![](../../dictionnaire/assets/4.webp)

Untuk memungkinkan _coinjoin_ tanpa ada pengguna yang kehilangan kendali atas dana mereka setiap saat, transaksi pertama kali dibuat oleh koordinator dan kemudian dikirimkan ke setiap pengguna. Setiap pengguna kemudian menandatangani transaksi tersebut setelah memverifikasi bahwa transaksi tersebut sesuai dengan keinginan mereka, dan kemudian semua tanda tangan ditambahkan ke dalam transaksi. Jika seorang pengguna atau koordinator mencoba untuk mencuri dana orang lain dengan memodifikasi hasil dari transaksi _coinjoin_, maka tanda tangan akan menjadi tidak valid dan transaksi akan ditolak oleh node. Ketika pencatatan output peserta dilakukan dengan menggunakan Chaum _blind signature_ untuk menghindari hubungan dengan input, ini disebut sebagai "Chaumian coinjoin".

Mekanisme ini meningkatkan kerahasiaan transaksi tanpa memerlukan modifikasi pada protokol Bitcoin. Implementasi spesifik dari _coinjoin_, seperti Whirlpool, JoinMarket, atau Wabisabi, menawarkan solusi untuk memfasilitasi proses koordinasi di antara para partisipan dan meningkatkan efisiensi transaksi _coinjoin_. Berikut ini adalah contoh transaksi _coinjoin_:

```text
323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2
```

Sulit untuk menentukan dengan pasti siapa yang pertama kali memperkenalkan ide _coinjoin_ pada Bitcoin, dan siapa yang memiliki ide untuk menggunakan _blind signture_ David Chaum dalam konteks ini. Sering kali dianggap bahwa Gregory Maxwell adalah orang pertama yang mendiskusikannya dalam [pesan di BitcoinTalk pada tahun 2013] (https://bitcointalk.org/index.php?topic=279249.0):

Menggunakan tanda _blind signature_ Chaum: Pengguna terhubung dan memberikan input (dan mengubah alamat) serta versi kriptografis yang dibutakan (_blinded_) dari alamat asal koin pribadi mereka; server menandatangani token dan mengembalikannya. Pengguna terhubung kembali secara anonim, membuka kedok alamat keluaran mereka, dan mengirimkannya kembali ke server. Server dapat melihat bahwa semua output telah ditandatangani olehnya dan, akibatnya, semua output berasal dari peserta yang valid. Kemudian, orang-orang terhubung kembali dan menandatangani.

Maxwell, G. (2013, Agustus 22). *CoinJoin: Bitcoin privacy for the real world*. Forum BitcoinTalk. https://bitcointalk.org/index.php?topic=279249.0

Akan tetapi, ada penyebutan sebelumnya, baik untuk tanda tangan Chaum dalam konteks pencampuran, maupun untuk _coinjoin_. [Pada bulan Juni 2011, Duncan Townsend mempresentasikan di BitcoinTalk](https://bitcointalk.org/index.php?topic=12751.0) sebuah _mixer_ yang menggunakan tanda tangan Chaum dengan cara yang sangat mirip dengan Chaumian _coinjoin_ modern. Di _thread_ yang sama, ada [pesan dari hashcoin sebagai tanggapan terhadap Duncan Townsend](https://bitcointalk.org/index.php?topic=12751.msg315793#msg315793) untuk memperbaiki mixernya. Pesan ini menyajikan apa yang paling mirip dengan _coinjoin_. Ada juga penyebutan sistem yang serupa dalam [pesan dari Alex Mizrahi pada tahun 2012] (https://gist.github.com/killerstorm/6f843e1d3ffc38191aebca67d483bd88#file-laundry), ketika dia menasihati pencipta Tenebrix. Istilah "_coinjoin_" sendiri tidak ditemukan oleh Greg Maxwell, tetapi berasal dari ide Peter Todd.

> *Istilah "coinjoin" tidak memiliki terjemahan dalam bahasa Indonesia. Anda dapat menggunakan "coinjoin" secara langsung untuk merujuknya.*
