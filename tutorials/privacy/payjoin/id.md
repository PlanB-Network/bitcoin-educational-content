---
name: Payjoin
description: Apa itu Payjoin pada Bitcoin?
---
![Thumbnail Payjoin - steganografi](assets/cover.webp)

***PERHATIAN:** Menyusul penangkapan pendiri Samourai Wallet dan penyitaan server mereka pada 24 April, Payjoin Stowaway di Samourai Wallet hanya dapat berfungsi dengan menukar PSBT secara manual antara pihak-pihak yang bersangkutan, asalkan kedua pengguna terhubung ke Dojo mereka sendiri. Sedangkan untuk Sparrow, Payjoin melalui BIP78 masih berfungsi. Namun, ada kemungkinan bahwa alat-alat ini akan diluncurkan kembali dalam beberapa minggu mendatang. Sementara itu, Anda masih dapat membaca artikel ini untuk memahami cara kerja teoritis payjoin.*

_Kami terus mengikuti perkembangan kasus ini serta perkembangan terkait alat-alat yang terkait. Yakinlah bahwa kami akan memperbarui tutorial ini seiring dengan tersedianya informasi baru._

_Tutorial ini disediakan hanya untuk tujuan pendidikan dan informasi. Kami tidak mendukung atau mendorong penggunaan alat-alat ini untuk tujuan kriminal. Tanggung jawab setiap pengguna untuk mematuhi hukum di yurisdiksi mereka._

---
## Memahami Transaksi Payjoin pada Bitcoin

Payjoin adalah struktur transaksi Bitcoin yang spesifik yang meningkatkan privasi pengguna selama pembayaran dengan berkolaborasi dengan penerima pembayaran.

Pada tahun 2015, [LaurentMT](https://twitter.com/LaurentMT) pertama kali menyebutkan metode ini sebagai "transaksi steganografi" dalam dokumen yang dapat diakses [di sini](https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt). Teknik ini kemudian diadopsi oleh Samourai Wallet, yang menjadi klien pertama yang mengimplementasikannya dengan alat Stowaway pada tahun 2018. Konsep Payjoin juga ditemukan dalam [BIP79](https://github.com/bitcoin/bips/blob/master/bip-0079.mediawiki) dan [BIP78](https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki). Beberapa istilah digunakan untuk merujuk pada Payjoin:
- Payjoin
- Stowaway
- P2EP (Pay-to-End-Point)
- Transaksi steganografi

Keunikan Payjoin terletak pada kemampuannya untuk menghasilkan transaksi yang tampak biasa pada pandangan pertama tetapi sebenarnya adalah mini Coinjoin antara dua pihak. Untuk mencapai ini, struktur transaksi melibatkan penerima pembayaran bersama dengan pengirim sebenarnya dalam input. Penerima memasukkan pembayaran kepada diri mereka sendiri di tengah transaksi, yang memungkinkan mereka dibayar.

Mari kita ambil contoh konkret: jika Anda membeli sebuah baguette seharga `4000 sats` menggunakan UTXO sebesar `10,000 sats` dan memilih Payjoin, pembuat roti Anda akan menambahkan UTXO sebesar `15,000 sats` yang milik mereka sebagai input, yang akan mereka terima secara penuh sebagai output, selain `4000 sats` Anda:
![Diagram transaksi Payjoin](assets/en/1.webp)
Dalam contoh ini, tukang roti memperkenalkan `15,000 sats` sebagai input dan keluar dengan `19,000 sats`, dengan perbedaan tepat `4000 sats`, yang merupakan harga dari baguette tersebut. Dari sisi Anda, Anda memasuki dengan `10,000 sats` dan berakhir dengan `6,000 sats` sebagai output, mewakili saldo `-4000 sats`, yang merupakan harga dari baguette tersebut. Untuk menyederhanakan contoh, saya sengaja menghilangkan biaya penambangan dalam transaksi ini.
## Apa tujuan dari transaksi Payjoin?

Transaksi Payjoin melayani dua tujuan yang memungkinkan pengguna untuk meningkatkan privasi pembayaran mereka.
Pertama-tama, Payjoin bertujuan untuk menyesatkan pengamat eksternal dengan menciptakan umpan palsu dalam analisis rantai. Ini dimungkinkan melalui Heuristik Kepemilikan Input Bersama (Common Input Ownership Heuristic - CIOH). Biasanya, ketika sebuah transaksi di blockchain memiliki beberapa input, diasumsikan bahwa semua input ini kemungkinan besar milik entitas atau pengguna yang sama. Jadi, ketika seorang analis memeriksa transaksi Payjoin, mereka dipimpin untuk percaya bahwa semua input berasal dari orang yang sama. Namun, persepsi ini salah karena penerima pembayaran juga menyumbangkan input bersama dengan pembayar sebenarnya. Oleh karena itu, analisis rantai dialihkan ke interpretasi yang ternyata salah.

Selanjutnya, Payjoin juga memungkinkan untuk menipu pengamat eksternal tentang jumlah pembayaran yang sebenarnya telah dibuat. Dengan memeriksa struktur transaksi, analis mungkin percaya bahwa pembayaran setara dengan jumlah salah satu output. Namun, pada kenyataannya, jumlah pembayaran tidak sesuai dengan salah satu output. Ini sebenarnya adalah perbedaan antara output UTXO penerima dan input UTXO penerima. Dalam hal ini, transaksi Payjoin masuk ke dalam domain steganografi. Ini memungkinkan untuk menyembunyikan jumlah sebenarnya dari sebuah transaksi dalam transaksi palsu yang bertindak sebagai umpan.

> Steganografi adalah teknik menyembunyikan informasi di dalam data atau objek lain sedemikian rupa sehingga keberadaan informasi yang tersembunyi tidak dapat dipersepsi. Misalnya, sebuah pesan rahasia dapat disembunyikan di dalam titik pada teks yang tidak ada hubungannya dengan itu, membuatnya tidak terdeteksi oleh mata telanjang (ini adalah teknik micropoint). Tidak seperti enkripsi, yang membuat informasi tidak dapat dimengerti tanpa kunci dekripsi, steganografi tidak mengubah informasi. Ini tetap ditampilkan secara terang-terangan. Tujuannya lebih untuk menyembunyikan keberadaan pesan rahasia, sedangkan enkripsi jelas mengungkapkan keberadaan informasi tersembunyi, meskipun tidak dapat diakses tanpa kunci.

Mari kita kembali ke contoh kita tentang transaksi Payjoin untuk pembayaran sebuah baguette.
![Skema transaksi Payjoin dari luar](assets/en/2.webp)
Dengan melihat transaksi ini di blockchain, seorang pengamat eksternal yang mengikuti heuristik analisis rantai biasa akan menafsirkannya sebagai berikut: "*Alice menggabungkan 2 UTXO sebagai input dari transaksi untuk membayar `19,000 sats` kepada Bob*."
![Interpretasi yang salah dari transaksi Payjoin dari luar](assets/en/3.webp)
Interpretasi ini jelas salah karena, seperti yang Anda sudah tahu, kedua input UTXO tidak milik orang yang sama. Selain itu, nilai sebenarnya dari pembayaran bukanlah `19,000 sats`, melainkan `4,000 sats`. Analisis pengamat eksternal ini dengan demikian diarahkan ke kesimpulan yang salah, memastikan pelestarian kerahasiaan para pemangku kepentingan.![diagram transaksi payjoin](assets/en/1.webp)
Jika Anda ingin menganalisis transaksi Payjoin yang sebenarnya, berikut ini adalah salah satu yang saya lakukan di testnet: [8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c](https://mempool.space/fr/testnet/tx/8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c)
[**-> Temukan tutorial kami tentang cara melakukan Payjoin dengan Samourai Wallet**](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)

[**-> Temukan tutorial kami tentang cara melakukan Payjoin dengan Sparrow Wallet**](https://planb.network/tutorials/privacy/on-chain/payjoin-sparrow-wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62)

**Sumber eksternal:**
- https://docs.samourai.io/en/spend-tools#stowaway;
- https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt;
- https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki.