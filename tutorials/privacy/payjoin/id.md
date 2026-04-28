---
name: Payjoin
description: Apa itu Payjoin pada Bitcoin?
---
![Thumbnail Payjoin - steganografi](assets/cover.webp)




## Memahami Transaksi Payjoin pada Bitcoin

Payjoin adalah struktur transaksi Bitcoin yang spesifik yang meningkatkan privasi pengguna selama pembayaran dengan berkolaborasi dengan penerima pembayaran.

Pada tahun 2015, [LaurentMT](https://twitter.com/LaurentMT) pertama kali menyebutkan metode ini sebagai "transaksi steganografi" dalam dokumen yang dapat diakses [di sini](https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt). Teknik ini kemudian diadopsi oleh Samourai Wallet, yang menjadi klien pertama yang mengimplementasikannya dengan alat Stowaway pada tahun 2018. Konsep Payjoin juga ditemukan dalam [BIP79](https://github.com/bitcoin/bips/blob/master/bip-0079.mediawiki) dan [BIP78](https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki). Beberapa istilah digunakan untuk merujuk pada Payjoin:
- Payjoin
- Stowaway
- P2EP (Pay-to-End-Point)
- Transaksi steganografi

Keunikan Payjoin ada pada kemampuannya menghasilkan transaksi yang kelihatannya biasa pada pandangan pertama tapi sebenarnya adalah mini Coinjoin antara dua pihak. Untuk mencapai itu, struktur transaksinya melibatkan penerima pembayaran bareng pengirim asli di bagian input. Penerima masukin pembayaran ke dirinya sendiri di tengah transaksi, yang bikin mereka tetap bisa nerima bayaran.

Contohnya gini: kalau kamu beli sebuah baguette seharga '4000 sats' pakai UTXO '10,000 sats' dan memilih Payjoin, si pembuat roti bakal nambahin UTXO '15,000 sats' milik mereka sebagai input, yang bakal mereka terima lagi sepenuhnya sebagai output, selain '4000 sats' dari kamu.

![Diagram transaksi Payjoin](assets/en/1.webp)

Dalam contoh ini, si pembuat roti masukin 15,000 sats sebagai input dan keluar dengan '19,000 sats', dengan selisih tepat '4000 sats', yaitu harga baguette tadi. Dari sisi kamu, kamu mulai dengan '10,000 sats' dan berakhir dengan '6,000 sats' sebagai output, yang nunjukkin saldo '-4000 sats', yaitu harga baguette tersebut. Biar contoh ini sederhana, aku sengaja ngilangin biaya mining dari transaksi ini.


## Apa tujuan dari transaksi Payjoin?

Transaksi Payjoin punya dua tujuan yang bikin pengguna bisa ningkatin privasi pembayarannya.
Pertama, Payjoin bertujuan buat ngibulin pengamat eksternal dengan bikin umpan palsu dalam analisis rantai. Ini bisa terjadi karena adanya Common Input Ownership Heuristic (CIOH). Biasanya, kalau ada transaksi di blockchain yang punya beberapa input, diasumsikan semua input itu kemungkinan besar milik entitas atau pengguna yang sama. Jadi waktu seorang analis ngeliat transaksi Payjoin, mereka bakal mikir kalau semua input itu datang dari orang yang sama. Padahal, anggapan itu salah, karena penerima pembayaran juga ikut nyumbang input bareng si pembayar. Akhirnya, analisis rantai jadi kejebak interpretasi yang sebenernya keliru.

Selain itu, Payjoin juga bisa ngecoh pengamat eksternal soal jumlah pembayaran yang beneran dilakukan. Dari struktur transaksinya, analis mungkin ngeira kalau pembayaran itu sama dengan jumlah salah satu output. Tapi kenyataannya, jumlah pembayaran nggak sama dengan salah satu output mana pun. Jumlah pembayaran sebenernya adalah selisih antara output UTXO penerima dan input UTXO penerima. Di titik ini, transaksi Payjoin masuk ke ranah steganografi. Payjoin bikin jumlah yang beneran dibayar bisa disimpen rapi di dalam transaksi palsu yang berperan sebagai umpan.

> Steganografi adalah teknik buat nyembunyiin informasi di dalam data atau objek lain dengan cara yang bikin keberadaan informasi itu sendiri nggak keliatan. Misalnya, sebuah pesan rahasia bisa disimpen di dalam titik-titik pada teks yang sebenernya nggak ada hubungannya sama sekali, jadi nggak bisa dideteksi mata telanjang (ini dikenal sebagai teknik micropoint).

Beda sama enkripsi, yang bikin informasi jadi nggak bisa dipahami tanpa kunci dekripsi, steganografi nggak ngubah informasinya. Informasinya tetap ditampilin apa adanya. Tujuannya bukan bikin pesannya nggak bisa dibaca, tapi bikin keberadaan pesan rahasia itu sendiri nggak ketahuan. Sementara itu, enkripsi justru nunjukkin bahwa ada informasi tersembunyi, walaupun isinya tetap nggak bisa diakses tanpa kunci.

Yuk kita kembali ke contoh kita tentang transaksi Payjoin untuk pembayaran sebuah baguette.
![Skema transaksi Payjoin dari luar](assets/en/2.webp)
Dengan ngeliat transaksi ini di blockchain, pengamat eksternal yang mengikuti heuristik analisis rantai biasa bakal menerjemahkannya kayak gini: "Alice menggabungkan 2 UTXO sebagai input transaksi buat bayar 19,000 sats ke Bob."
![Interpretasi yang salah dari transaksi Payjoin dari luar](assets/en/3.webp)
Interpretasi ini jelas salah karena, kayak yang kamu udah tahu, dua input UTXO itu bukan milik orang yang sama. Selain itu, nilai pembayaran yang sebenarnya bukan '19,000 sats', tapi '4,000 sats'. Jadi analisis si pengamat eksternal itu kejebak ke kesimpulan yang keliru, yang akhirnya bantu menjaga kerahasiaan para pihak yang terlibat.![diagram transaksi payjoin](assets/en/1.webp)
Jika kamu ingin menganalisis transaksi Payjoin yang sebenarnya, berikut ini adalah salah satu yang saya lakukan di testnet: [8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c](https://mempool.space/fr/testnet/tx/8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c)


- https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt;
- https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki.
- https://payjoin.org/
https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

