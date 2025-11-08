---
name: Penjelajah Blockstream
description: Jelajahi lapisan utama Bitcoin dan Liquid Network
---

![cover](assets/cover.webp)



Blockstream Explorer adalah sebuah proyek yang memfasilitasi eksplorasi transaksi dan status global protokol Bitcoin, serta [*sidechain*] (https://planb.academy/en/resources/glossary/sidechain) Liquid yang dikembangkan oleh perusahaan Blockstream.



Diprakarsai pada tahun 2014 oleh Blockstream, sebuah perusahaan yang didirikan oleh Adam Back, penjelajah [blockstream.info] (https://blockstream.info) bertujuan untuk menyediakan infrastruktur yang kuat untuk Bitcoin, menjamin interoperabilitas dan pelacakan transaksi antar lapisan (on-chain dan Liquid), sekaligus meningkatkan keamanan dan privasi pengguna.



Dalam tutorial ini, kita akan melihat apa yang membedakannya, layanannya, dan bagaimana ia menawarkan pemantauan tanpa batas atas operasi dan status lapisan on-chain dan Liquid Bitcoin.



## Memulai dengan penjelajah Blockstream



### Menavigasi saluran utama



Ketika Anda pergi ke penjelajah Blockstream.info, pada "**Dashboard**", rantai utama protokol Bitcoin dipilih secara default. Dari antarmuka ini, Anda memiliki gambaran umum tentang :





- Ukuran rantai utama: Blok yang baru saja ditambang.



![blocks](assets/fr/01.webp)



Bagian ini menyediakan informasi mengenai blok terbaru yang ditambang, stempel waktu, jumlah transaksi yang termasuk dalam setiap blok, ukuran dalam kilobyte (kB), dan pengukuran setiap blok dalam satuan berat (**WU** = *Weight Units*). Pengukuran terakhir ini sangat menarik, karena memungkinkan kita untuk mengevaluasi optimalisasi blok, mengingat bahwa setiap blok rantai utama dibatasi hingga `4.000.000 WU`, atau `4.000 kWU`.





- Transaksi terakhir.



![transactions](assets/fr/02.webp)



Bagian transaksi memberikan informasi mengenai pengenal unik transaksi, nilai bitcoin yang terlibat, ukuran dalam virtual byte (vB) - yang mewakili jumlah seluruh data (input dan output) - dan tarif biaya terkait. Sebagai contoh, sebuah transaksi dengan ukuran `153 vB` dengan tarif `2 sat/vB` akan dikenakan biaya sebesar `306 satoshi`.



### Eksplorasi cairan



Dari menu "**Blok**", Anda bisa melacak riwayat seluruh rantai utama hingga ke blok terakhir yang ditambang.



![blocs](assets/fr/03.webp)



Dengan mengklik pada blok tertentu, Anda bisa mendapatkan detail lebih lanjut mengenai informasi dan transaksi yang termasuk di dalamnya. Sebagai contoh, untuk blok 919330: Anda akan melihat hash dari blok tersebut. Anda juga dapat menavigasi ke blok sebelumnya, karena setiap blok yang ditambang (selain Genesis) ditautkan ke blok sebelumnya, dengan mempertahankan hash dari blok sebelumnya.



![metadata](assets/fr/04.webp)



Dengan mengklik tombol **"Detail "**, Anda dapat memperoleh informasi lebih lanjut mengenai blok ini, seperti statusnya, yang mengonfirmasi bahwa blok tersebut telah ditambahkan ke rantai utama yang dipertahankan dan disebarkan. Anda juga dapat melihat tingkat kesulitan di mana blok ini ditambang: tingkat kesulitan ini menunjukkan daya komputasi yang dibutuhkan untuk memecahkan masalah kriptografi mining dan disesuaikan setiap 2016 blok (sekitar 2 minggu).



![details](assets/fr/05.webp)



Di bawah bagian detail ini, kita dapat menemukan semua transaksi yang termasuk dalam blok ini.



Transaksi pertama dalam blok disebut dengan **transaction coinbase**. Transaksi ini digunakan untuk mengalokasikan upah mining penambang (semua biaya yang terkait dengan transaksi yang termasuk dalam blok dan hibah blok). Bitcoin yang dihasilkan dari transaksi ini hanya dapat digunakan setelah 100 blok berturut-turut ditambang. Dengan kata lain, untuk dapat menggunakannya, penambang harus menunggu produksi blok **919430**. Hal ini dikenal sebagai [*"periode jatuh tempo"] (https://planb.academy/fr/resources/glossary/maturity-period).



Coinbase adalah transaksi khusus: ini adalah satu-satunya transaksi yang tidak memiliki input nyata, karena tidak menggunakan bitcoin dari transaksi sebelumnya.




![coinbase](assets/fr/06.webp)



Semua transaksi lainnya dibagi menjadi dua bagian: input dan output.



Agar bitcoin dapat digunakan sebagai input dalam transaksi baru, pemrakarsa transaksi harus membuktikan kepemilikannya dengan memberikan tanda tangan yang sesuai dengan skrip tertentu. Setiap keping bitcoin (UTXO) berisi sebuah skrip yang secara umum membutuhkan tanda tangan khusus yang hanya dapat diberikan oleh pemegang kunci pribadi. Skrip ini adalah ***scriptSig*** (dalam ASM), ditulis dalam Skrip Bitcoin, dan dapat terdiri dari berbagai jenis. Pada contoh ini, kita dapat melihat bahwa UTXO yang digunakan adalah tipe P2SH dengan output tipe P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Anda dapat menelusuri sejarah UTXO tertentu menggunakan heuristik. Kami mengundang Anda untuk menemukan berbagai heuristik Bitcoin dan cara-cara untuk memperkuat kerahasiaan transaksi Anda di Bitcoin:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Mari kita ambil contoh biaya keluar dari transaksi ini. Dengan mengklik pengenal transaksi, kita akan diarahkan ke bagian **Transaksi** di halaman rincian transaksi.



![transaction](assets/fr/08.webp)



Dari halaman ini, Anda dapat mengetahui di blok mana transaksi tersebut dimasukkan. Bergantung pada jenis alamat yang digunakan, transaksi dapat mengoptimalkan datanya (*virtual byte*) dan oleh karena itu membayar lebih sedikit biaya transaksi. Transaksi ini, sebagai contoh, menghemat 53% biaya dengan menggunakan format alamat SegWit Bech32 asli yang dimulai dengan `bc1q`.



![trx_details](assets/fr/09.webp)



## Lapisan Liquid



Liquid Network adalah [*sidechain*] (https://planb.academy/en/resources/glossary/sidechain) dan solusi open source level 2 untuk protokol Bitcoin. Secara khusus, ini memungkinkan transaksi bitcoin yang lebih cepat dan lebih rahasia.



Pada penjelajah Blockstream.info, klik tombol **"Liquid"** untuk beralih ke jaringan Liquid.



![liquid](assets/fr/10.webp)



Dengan mengklik salah satu transaksi yang ingin kita lacak, kita akan melihat bahwa jumlah potongan bitcoin digantikan oleh tulisan "**Rahasia**". Di jaringan ini, transaksi bisa bersifat rahasia, jadi kita tidak bisa melihat jumlah setiap UTXO, baik yang masuk maupun yang keluar dari transaksi.



![liquid_trx](assets/fr/11.webp)



Akan tetapi, kami mencatat bahwa prinsip dan mekanisme yang ada pada lapisan utama protokol Bitcoin adalah sama: skrip penguncian bitcoin dan penelusuran UTXO.



![liquid_details](assets/fr/12.webp)



Liquid Network juga menyediakan aset digital non-depositori yang dapat digunakan oleh organisasi. Dalam menu **"Aset "**, Anda akan menemukan daftar aset yang terdaftar, totalnya, dan domain yang terkait dengannya.



![assets](assets/fr/13.webp)



Untuk setiap aset, Anda dapat melacak riwayat transaksi penerbitan dan pembakaran (menghapus total yang beredar).



![assets_trxs](assets/fr/14.webp)




## Opsi lainnya



Penjelajah Blockstream.info juga mencakup visualisasi dan pelacakan transaksi pada Testnet, Bitcoin, on-chain dan Liquid Network.



![testnet](assets/fr/15.webp)



Ketika Anda masuk ke jaringan Testnet, Anda tidak menggunakan bitcoin asli, tetapi Anda memiliki semua fitur yang dijelaskan di atas.



![liquid_testnet](assets/fr/16.webp)



Jaringan ini memiliki panjang rantai yang berbeda, di mana Anda dapat menghubungkan dan menguji pengoperasian mekanisme Bitcoin dan Liquid.





- Bagian API didedikasikan untuk siapa saja yang ingin mengintegrasikan fungsi-fungsi Explorer tertentu ke dalam aplikasi mereka sendiri. Melalui API ini Anda dapat menginterogasi rantai utama dari berbagai lapisan (on-chain dan Liquid), melacak transaksi dan mengetahui biaya rata-rata untuk transaksi dalam satu blok, misalnya.



![api](assets/fr/17.webp)



Anda sekarang siap untuk memanfaatkan potensi penuh Blockstream Explorer untuk melakukan kueri blockchain pada lapisan on-chain dan Liquid. Kami harap tutorial ini bermanfaat bagi Anda, dan kami merekomendasikan tutorial kami tentang penjelajah Bitcoin lainnya:



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f