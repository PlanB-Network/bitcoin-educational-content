---
name: BLOCKSTREAM Explorer
description: Jelajahi Layer utama dari Bitcoin dan Liquid Network
---

![cover](assets/cover.webp)



BLOCKSTREAM Explorer adalah sebuah proyek yang memfasilitasi eksplorasi transaksi dan Global State protokol Bitcoin, serta [*Sidechain*] (https://planb.network/en/resources/glossary/Sidechain) Liquid yang dikembangkan oleh perusahaan BLOCKSTREAM.



Diprakarsai pada tahun 2014 oleh BLOCKSTREAM, sebuah perusahaan yang didirikan oleh Adam Back, penjelajah [BLOCKSTREAM.info] (https://BLOCKSTREAM.info) bertujuan untuk menyediakan infrastruktur yang kuat untuk Bitcoin, menjamin interoperabilitas dan pelacakan transaksi antar lapisan (On-Chain dan Liquid), sekaligus meningkatkan keamanan dan privasi pengguna.



Dalam tutorial ini, kami menyajikan apa yang membuatnya berbeda, layanannya, dan bagaimana ia menawarkan pemantauan tanpa batas atas operasi dan status lapisan On-Chain dan Liquid Bitcoin.



## Memulai dengan BLOCKSTREAM



### Menavigasi saluran utama



Ketika Anda masuk ke penjelajah BLOCKSTREAM.info, pada "**Dashboard**", saluran protokol Bitcoin utama dipilih secara default. Dari Interface ini, Anda memiliki gambaran umum tentang :





- Ukuran rantai utama: Blok yang baru saja ditambang.



![blocks](assets/fr/01.webp)



Bagian ini memberikan informasi mengenai blok terbaru yang ditambang, Timestamp, jumlah transaksi yang termasuk dalam setiap BLOCK, ukuran dalam kilobyte (kB), dan pengukuran setiap BLOCK dalam satuan berat (**WU** = *Weight Units*). Pengukuran terakhir ini sangat menarik, karena memungkinkan kami untuk mengevaluasi optimalisasi BLOCK, mengingat bahwa setiap BLOCK dari rantai utama dibatasi hingga `4.000.000 WU`, atau `4.000 kWU`.





- Transaksi terakhir.



![transactions](assets/fr/02.webp)



Bagian transaksi memberikan informasi tentang pengenal unik transaksi, nilai Bitcoin yang terlibat, ukuran dalam byte virtual (vB) - yang mewakili jumlah semua data (input dan output) - dan tarif biaya yang terkait. Sebagai contoh, transaksi dengan ukuran `153 vB` dengan kecepatan `2 sat/vB` akan dikenakan biaya sebesar `306 satoshi`.



### Eksplorasi cairan



Dari menu "**Blok**", Anda dapat melacak sejarah seluruh rantai utama hingga ke BLOCK yang terakhir ditambang.



![blocs](assets/fr/03.webp)



Dengan mengklik pada BLOCK tertentu, Anda dapat memperoleh rincian lebih lanjut tentang informasi dan transaksi yang termasuk di dalamnya. Sebagai contoh, untuk BLOCK 919330: Anda akan mendapatkan Hash dari BLOCK tersebut. Anda juga bisa menavigasi ke BLOCK sebelumnya, karena setiap BLOCK yang ditambang (selain Genesis) terhubung dengan BLOCK sebelumnya, dengan mempertahankan Hash pendahulunya.



![metadata](assets/fr/04.webp)



Dengan mengklik tombol **"Detail "**, Anda dapat memperoleh informasi lebih lanjut mengenai BLOCK ini, seperti statusnya, yang mengonfirmasi bahwa ia telah ditambahkan ke dalam rantai utama yang dipertahankan dan disebarkan. Anda juga dapat melihat tingkat kesulitan di mana BLOCK ini ditambang: tingkat kesulitan ini merepresentasikan daya komputasi yang dibutuhkan untuk memecahkan masalah kriptografi Mining dan disesuaikan setiap 2016 blok (sekitar 2 minggu).



![details](assets/fr/05.webp)



Di bawah bagian rincian ini, kami menemukan semua transaksi yang termasuk dalam BLOCK ini.



Transaksi pertama dalam BLOCK disebut **transaction coinbase**. Transaksi ini digunakan untuk mengalokasikan hadiah Miner dari Mining (semua biaya yang terkait dengan transaksi yang termasuk dalam BLOCK dan hibah BLOCK). Bitcoin yang dihasilkan dari transaksi ini hanya dapat digunakan setelah 100 blok berturut-turut ditambang. Dengan kata lain, untuk dapat menggunakannya, Miner harus menunggu produksi BLOCK **919430**. Hal ini dikenal dengan istilah [*"periode jatuh tempo"] (https://planb.network/fr/resources/glossary/maturity-period).



Coinbase adalah transaksi khusus: ini adalah satu-satunya transaksi yang tidak memiliki input nyata, karena tidak menggunakan bitcoin dari transaksi sebelumnya.




![coinbase](assets/fr/06.webp)



Semua transaksi lainnya dibagi menjadi dua bagian: input dan output.



Agar bitcoin dapat digunakan sebagai input dalam transaksi baru, pemrakarsa transaksi harus membuktikan kepemilikannya dengan memberikan tanda tangan yang sesuai dengan skrip tertentu. Setiap keping bitcoin (UTXO) berisi sebuah skrip yang secara umum membutuhkan tanda tangan khusus yang hanya dapat diberikan oleh pemegang kunci pribadi. Skrip ini adalah ***scriptSig*** (dalam ASM), ditulis dalam Skrip Bitcoin, dan dapat terdiri dari berbagai jenis. Pada contoh ini, kita dapat melihat bahwa UTXO yang digunakan adalah tipe P2SH dengan output tipe P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Anda dapat menelusuri sejarah UTXO tertentu menggunakan heuristik. Kami mengundang Anda untuk menemukan berbagai heuristik Bitcoin yang berbeda dan cara memperkuat kerahasiaan transaksi Bitcoin Anda:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Mari kita ambil contoh biaya keluar dari transaksi ini. Dengan mengklik pengenal transaksi, kita akan diarahkan ke bagian **Transaksi** di halaman rincian transaksi.



![transaction](assets/fr/08.webp)



Dari halaman ini, Anda dapat mengetahui transaksi tersebut termasuk ke dalam BLOCK yang mana. Bergantung pada jenis Address yang digunakan, transaksi dapat mengoptimalkan datanya (*virtual byte*) dan oleh karena itu membayar lebih sedikit biaya transaksi. Transaksi ini, misalnya, menghemat 53% biaya dengan menggunakan format SegWit BECH32 Address asli yang dimulai dengan `bc1q`.



![trx_details](assets/fr/09.webp)



## Lapisan Liquid



Liquid Network adalah [*Sidechain*] (https://planb.network/en/resources/glossary/Sidechain) dan solusi open source level 2 untuk protokol Bitcoin. Secara khusus, ini memungkinkan transaksi Bitcoin yang lebih cepat dan lebih rahasia.



Pada penjelajah BLOCKSTREAM.info, klik tombol **"Liquid"** untuk beralih ke Liquid Network.



![liquid](assets/fr/10.webp)



Dengan mengklik salah satu transaksi yang ingin kita ikuti, kita akan melihat bahwa jumlah keping Bitcoin digantikan oleh tulisan "**Rahasia**". Pada jaringan ini, transaksi bersifat rahasia, sehingga kita tidak bisa melihat jumlah setiap UTXO, baik yang masuk maupun yang keluar dari transaksi tersebut.



![liquid_trx](assets/fr/11.webp)



Namun, kami mencatat bahwa prinsip dan mekanisme yang ada pada Layer utama protokol Bitcoin adalah sama: skrip penguncian Bitcoin dan penelusuran UTXO.



![liquid_details](assets/fr/12.webp)



Liquid Network juga menyediakan aset digital non-depositori yang dapat digunakan oleh organisasi. Dalam menu **"Aset "**, Anda akan menemukan daftar aset yang terdaftar, totalnya, dan domain yang terkait dengannya.



![assets](assets/fr/13.webp)



Untuk setiap aset, Anda dapat melacak riwayat transaksi penerbitan dan pembakaran (menghapus total yang beredar).



![assets_trxs](assets/fr/14.webp)




## Opsi lainnya



Penjelajah BLOCKSTREAM.info juga mencakup visualisasi dan pelacakan transaksi pada Testnet, Bitcoin, On-Chain dan Liquid Network.



![testnet](assets/fr/15.webp)



Ketika Anda masuk ke jaringan Testnet, Anda tidak menggunakan bitcoin asli, tetapi Anda memiliki semua fitur yang dijelaskan di atas.



![liquid_testnet](assets/fr/16.webp)



Jaringan ini memiliki panjang rantai yang berbeda, di mana Anda dapat menghubungkan dan menguji pengoperasian mekanisme Bitcoin dan Liquid.





- Bagian API didedikasikan untuk siapa saja yang ingin mengintegrasikan fungsi-fungsi Explorer tertentu ke dalam aplikasi mereka sendiri. Melalui API ini Anda dapat menginterogasi rantai utama dari berbagai lapisan (On-Chain dan Liquid), melacak transaksi, dan mengetahui biaya rata-rata untuk transaksi dalam BLOCK, misalnya.



![api](assets/fr/17.webp)



Anda sekarang siap untuk memanfaatkan potensi penuh dari BLOCKSTREAM Explorer untuk melakukan kueri blockchain pada lapisan On-Chain dan Liquid. Kami harap tutorial ini bermanfaat bagi Anda, dan kami merekomendasikan tutorial kami tentang Bitcoin Explorer lainnya:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f