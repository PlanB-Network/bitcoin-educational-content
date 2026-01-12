---
name: Blockstream Explorer
description: Jelajahi lapisan utama Bitcoin dan Liquid Network
---

![cover](assets/cover.webp)



Blockstream Explorer adalah sebuah proyek yang memfasilitasi eksplorasi transaksi dan status global protokol Bitcoin, serta [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) Liquid yang dikembangkan oleh perusahaan Blockstream.



Diprakarsai pada tahun 2014 oleh Blockstream, sebuah perusahaan yang didirikan oleh Adam Back, penjelajah [blockstream.info](https://blockstream.info) bertujuan untuk menyediakan infrastruktur yang kuat untuk Bitcoin, menjamin interoperabilitas dan pelacakan transaksi antar lapisan (on-chain dan Liquid), sekaligus meningkatkan keamanan dan privasi pengguna.



Dalam tutorial ini, kita akan melihat apa yang membuatnya berbeda, layanannya, dan bagaimana ia menawarkan pemantauan tanpa batas atas operasi dan status lapisan on-chain dan Liquid Bitcoin.



## Memulai dengan Blockstream Explorer



### Menavigasi saluran utama



Ketika kamu membuka penjelajah Blockstream.info, pada **Dashboard**, rantai utama protokol Bitcoin akan dipilih secara default. Dari antarmuka ini, kamu akan melihat gambaran umum tentang :




- Ukuran rantai utama: Blok yang baru saja ditambang.



![blocks](assets/fr/01.webp)



Bagian ini menyediakan informasi mengenai blok terbaru yang ditambang, stempel waktu, jumlah transaksi dalam setiap blok, ukuran dalam kilobyte (kB), dan ukuran tiap blok dalam satuan berat (**WU** = Weight Units). Ukuran dalam WU ini sangat menarik karena memungkinkan kita mengevaluasi optimalisasi blok, mengingat bahwa tiap blok di rantai utama dibatasi hingga '4.000.000' WU, atau '4.000' kWU.





- Transaksi terakhir.



![transactions](assets/fr/02.webp)



Bagian transaksi memberikan informasi mengenai pengenal unik transaksi, nilai bitcoin yang terlibat, ukuran dalam virtual byte (vB) - yang mewakili jumlah seluruh data (input dan output) - dan tarif biaya terkait. Sebagai contoh, sebuah transaksi dengan ukuran `153 vB` dengan tarif `2 sat/vB` akan dikenakan biaya sebesar `306 satoshi`.



### Eksplorasi cairan



Dari menu "**Blok**", kamu bisa melacak riwayat seluruh rantai utama hingga ke blok terakhir yang ditambang.



![blocs](assets/fr/03.webp)



Dengan mengklik blok tertentu, kamu bisa melihat detail lebih lanjut tentang informasi dan transaksi yang termasuk di dalamnya. Sebagai contoh, untuk blok 919330, kamu akan melihat hash dari blok tersebut. Kamu juga bisa menavigasi ke blok sebelumnya, karena setiap blok yang ditambang (kecuali Genesis) ditautkan ke blok sebelumnya dengan mempertahankan hash dari blok sebelumnya.



![metadata](assets/fr/04.webp)



Dengan mengklik tombol **Detail**, kamu bisa mendapatkan informasi lebih lanjut tentang blok ini, seperti statusnya yang mengonfirmasi bahwa blok tersebut sudah ditambahkan ke rantai utama yang dipertahankan dan disebarkan. Kamu juga bisa melihat tingkat kesulitan tempat blok ini ditambang. Tingkat kesulitan ini menunjukkan daya komputasi yang dibutuhkan untuk memecahkan masalah kriptografi mining dan disesuaikan setiap 2016 blok (sekitar 2 minggu).


![details](assets/fr/05.webp)



Di bawah bagian detail ini, kita dapat menemukan semua transaksi yang termasuk dalam blok ini.



Transaksi pertama dalam blok disebut dengan **transaction coinbase**. Transaksi ini digunakan untuk mengalokasikan upah mining penambang (semua biaya yang terkait dengan transaksi yang termasuk dalam blok dan hibah blok). Bitcoin yang dihasilkan dari transaksi ini hanya dapat digunakan setelah 100 blok berturut-turut ditambang. Dengan kata lain, untuk dapat menggunakannya, penambang harus menunggu produksi blok **919430**. Hal ini dikenal sebagai [*"periode jatuh tempo"](https://planb.academy/fr/resources/glossary/maturity-period).




Coinbase adalah transaksi khusus yang menjadi satu-satunya transaksi tanpa input nyata, karena tidak menggunakan bitcoin dari transaksi sebelumnya.



![coinbase](assets/fr/06.webp)



Semua transaksi lainnya dibagi menjadi dua bagian: input dan output.



Agar bitcoin bisa digunakan sebagai input dalam transaksi baru, pemrakarsa transaksi harus membuktikan kepemilikannya dengan memberikan tanda tangan yang sesuai dengan skrip tertentu. Setiap keping bitcoin (UTXO) berisi skrip yang umumnya membutuhkan tanda tangan khusus yang hanya bisa diberikan oleh pemegang private key. Skrip ini adalah ***scriptSig*** (dalam ASM), ditulis dalam Skrip Bitcoin, dan bisa terdiri dari berbagai jenis. Pada contoh ini, kita bisa melihat bahwa UTXO yang digunakan adalah tipe P2SH dengan output tipe P2WPKH (*Pay-to-Witness-Public-Key-Hash*).

Kamu juga bisa menelusuri sejarah UTXO tertentu menggunakan heuristik. Kami mengajak kamu untuk menemukan berbagai heuristik Bitcoin dan cara memperkuat kerahasiaan transaksi kamu di Bitcoin:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Mari kita ambil contoh biaya keluar dari transaksi ini. Dengan mengklik pengenal transaksi, kita akan diarahkan ke bagian **Transaksi** di halaman rincian transaksi.



![transaction](assets/fr/08.webp)



Dari halaman ini, kamu bisa melihat di blok mana transaksi tersebut dimasukkan. Bergantung pada jenis alamat yang digunakan, transaksi bisa mengoptimalkan datanya (virtual byte) dan karena itu membayar biaya transaksi yang lebih rendah. Transaksi ini, sebagai contoh, menghemat 53% biaya dengan memakai format alamat SegWit Bech32 asli yang dimulai dengan 'bc1q'.


![trx_details](assets/fr/09.webp)



## Lapisan Liquid



Liquid Network adalah [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) dan solusi open source level 2 untuk protokol Bitcoin. Secara khusus, ini memungkinkan transaksi bitcoin yang lebih cepat dan lebih rahasia.



Pada explorer Blockstream.info, klik tombol **"Liquid"** untuk beralih ke jaringan Liquid.



![liquid](assets/fr/10.webp)



Dengan mengklik salah satu transaksi yang ingin kita lacak, kita akan melihat bahwa jumlah potongan bitcoin digantikan oleh tulisan "**Rahasia**". Di jaringan ini, transaksi bisa bersifat rahasia, jadi kita tidak bisa melihat jumlah setiap UTXO, baik yang masuk maupun yang keluar dari transaksi.



![liquid_trx](assets/fr/11.webp)



Akan tetapi, kami mencatat bahwa prinsip dan mekanisme yang ada pada lapisan utama protokol Bitcoin adalah sama: skrip penguncian bitcoin dan penelusuran UTXO.



![liquid_details](assets/fr/12.webp)



Liquid Network juga menyediakan aset digital non-depositori yang dapat digunakan oleh organisasi. Dalam menu **"Aset "**, kamu akan menemukan daftar aset yang terdaftar, totalnya, dan domain yang terkait dengannya.



![assets](assets/fr/13.webp)



Untuk setiap aset, kamu dapat melacak riwayat transaksi penerbitan dan pembakaran (menghapus total yang beredar).



![assets_trxs](assets/fr/14.webp)




## Opsi lainnya



Penjelajah Blockstream.info juga mencakup visualisasi dan pelacakan transaksi pada Testnet, Bitcoin, on-chain dan Liquid Network.



![testnet](assets/fr/15.webp)



Ketika kamu masuk ke jaringan Testnet, kamu tidak menggunakan bitcoin asli, tetapi kamu memiliki semua fitur yang dijelaskan di atas.



![liquid_testnet](assets/fr/16.webp)



Jaringan ini memiliki panjang rantai yang berbeda, di mana kamu dapat menghubungkan dan menguji pengoperasian mekanisme Bitcoin dan Liquid.





- Bagian API ditujukan untuk siapa saja yang ingin mengintegrasikan fungsi-fungsi Explorer tertentu ke dalam aplikasi mereka sendiri. Melalui API ini kamu bisa menginterogasi rantai utama dari berbagai lapisan (on-chain dan Liquid), melacak transaksi, dan mengetahui biaya rata-rata untuk transaksi dalam satu blok, misalnya.



![api](assets/fr/17.webp)



Sekarang kamu siap untuk memanfaatkan potensi penuh Blockstream Explorer untuk melakukan kueri blockchain pada lapisan on-chain dan Liquid. Kami harap tutorial ini bermanfaat bagi kamu, dan kami merekomendasikan tutorial kami tentang penjelajah Bitcoin lainnya:



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f
