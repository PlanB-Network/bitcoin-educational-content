---
name: Amboss
description: Jelajahi dan analisis Lightning Network
---

![cover](assets/cover.webp)



Lightning Network adalah Layer dari protokol Bitcoin, yang terutama dikembangkan untuk mempromosikan adopsi pembayaran Bitcoin setiap hari dengan meningkatkan kecepatan pemrosesan setiap transaksi. Berdasarkan prinsip desentralisasi, Lightning Network terdiri dari node (komputer yang menjalankan implementasi Lightning) yang berkomunikasi secara peer-to-peer, menyampaikan data (pembayaran dan verifikasi pembayaran) satu sama lain.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Sama seperti pada rantai utama, sangat penting untuk memungkinkan pengguna mengetahui informasi dan status jaringan, untuk memfasilitasi koneksi antar node dan meminimalkan masalah likuiditas yang umumnya muncul dalam jaringan. Memang, pada Lightning Network, kami merekomendasikan pembayaran mikro dengan jumlah yang relatif lebih kecil dibandingkan dengan transaksi pada rantai utama Bitcoin.



Penting untuk dicatat bahwa tidak semua node Lightning tersedia di platform Amboss.



Seperti [Mempool Space] (https://Mempool.space), yang menyediakan informasi berguna tentang rantai utama protokol Bitcoin, sejak tahun 2022 [Amboss] (https://amboss.space) menyediakan informasi tentang :





- Node pada Lightning Network
- Saluran pembayaran dan kapasitas pembayarannya
- Evolusi Lightning Network dari waktu ke waktu
- Statistik tentang biaya ke node relai untuk pembayaran Anda.



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

Dalam tutorial ini, kami akan mengajak Anda berkeliling platform ini, yang merupakan sumber daya penting bagi pengguna Lightning Network, mereka yang ingin menghubungkan node mereka untuk memperluas jaringan, dll.




## Temukan pasangan



Salah satu tujuan dari platform Amboss adalah untuk memungkinkan berbagai node dalam jaringan untuk terhubung dan mengkomunikasikan informasi satu sama lain. Pada halaman beranda platform, Anda dapat langsung mencari nama node yang sudah Anda ketahui, atau menemukan node dari portofolio Lightning terpopuler yang Anda gunakan.



![home](assets/fr/01.webp)



![wallet](assets/fr/02.webp)



https://planb.academy/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

Di halaman beranda, Anda juga akan menemukan node yang diklasifikasikan menurut :




- Evolusi kapasitas: jumlah Bitcoin yang terkait dengan kunci publik node dan total yang tersedia di semua salurannya.
- Evolusi saluran: jumlah koneksi baru ke node lain dalam jaringan.
- Popularitas node: seberapa sering node tersebut digunakan.



![nodes](assets/fr/03.webp)



Oleh karena itu, memilih simpul yang tepat untuk disambungkan adalah dengan memeriksa kriteria berikut ini:





- Pastikan bahwa node memiliki jumlah bitcoin yang cukup; semakin besar kapasitas node, semakin besar pula jumlah bitcoin yang dapat Anda bayarkan.





- Pastikan bahwa node memiliki banyak koneksi dan saluran terbuka dengan node lain dalam jaringan.





- Pastikan node aktif dan masih dihargai oleh rekan-rekannya dengan memeriksa jumlah saluran baru; semakin banyak saluran baru yang dibuka oleh node ini, semakin dihargai oleh node lain dalam jaringan.



Setelah Anda menemukan simpul yang tepat, klik namanya untuk diarahkan ke halaman informasi simpul.



Pada Interface ini, dengan memeriksa Timestamp dari saluran yang baru dibuat, Anda akan mendapatkan petunjuk tentang aktivitas node ini. Anda juga akan menemukan informasi mengenai kapasitas saluran node ini: informasi ini sangat penting jika Anda ingin secara aktif menggunakan node ini untuk melakukan pembayaran.




![node_info](assets/fr/04.webp)



Di bagian kiri, Anda akan menemukan rincian lebih lanjut tentang lokasi node ini. Sebagai contoh, Anda dapat melihat :




- Kunci publik: pengenal tepat di bawah nama simpul.
- Posisi geografis simpul ini.




![channels](assets/fr/05.webp)



Interface ini memberi tahu Anda koneksi Address untuk node ini: berbentuk `pubkey@ip:port`. Dalam contoh kita, kita ingin menyambung ke simpul yang memiliki berkas :




- kunci publik `pubkey` adalah: `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- iP Address: `170.75.163.209`
- Pelabuhan: `9735`



![geoinfo](assets/fr/06.webp)



Pada bagian **Channels**, Anda akan melihat daftar saluran yang terbuka dan koneksi node ke node lain dalam jaringan. Pada Interface ini, beberapa informasi sangat penting untuk mengonfirmasi bahwa node ini sesuai dengan kebutuhan kita atau dapat diandalkan:





- Rasio masuk**: Jumlah yang akan ditagih oleh node kepada Anda untuk setiap juta Satoshi yang diterimanya, tergantung saluran yang dipilih.
- Rasio (bagian per juta)**: yang mewakili jumlah Satoshi per juta unit yang akan ditagih oleh node kepada Anda ketika Anda memutuskan untuk melakukan pembayaran melalui salah satu salurannya. Katakanlah Anda memutuskan untuk melakukan pembayaran sebesar `10_000 Sats` melalui saluran yang rasio ppm-nya adalah `500 Sats`, Anda harus membayar satoshi `10_000 * 500 / 1_000_000` kepada node tersebut, yang setara dengan `5 Sats`.
- Maksimum [HTLC] (https://planb.academy/resources/glossary/htlc) **: Jumlah maksimum yang dapat ditransmisikan oleh node ini melalui salah satu saluran ini.



Dengan melihat tabel pada Interface ini, Anda juga dapat menemukan semua informasi ini pada node yang dicocokkan.



![channels_info](assets/fr/07.webp)



Pada bagian **Peta saluran**, Anda dapat melihat distribusi dan kapasitas berbagai saluran pada node ini. Anda dapat mengubah kriteria distribusi yang ditampilkan dengan memilih salah satu opsi pada daftar drop-down di sebelah kanan.



![cha_maps](assets/fr/08.webp)



Bagian **Saluran yang ditutup** mengelompokkan semua saluran yang pernah ditutup oleh node menurut jenis penutupan:




- Penutupan bersama**: mewakili kesepakatan kedua belah pihak, yang menggunakan kunci pribadi mereka untuk menandatangani transaksi yang menandai penutupan saluran dan distribusi saldo di dalamnya
- Penutupan paksa: mewakili penutupan satu bagian saluran secara tiba-tiba dan sepihak. Jenis penutupan ini tidak disarankan, karena Lightning Network adalah protokol berbasis hukuman: ketika Anda mencoba menipu saldo saluran, Anda berisiko kehilangan semua saldo yang tersedia di saluran tersebut.



![closed](assets/fr/09.webp)



Dapatkan informasi tentang biaya transit untuk merutekan pembayaran Anda melalui saluran pada node yang Anda gunakan



![fees](assets/fr/10.webp)



## Informasi jaringan



Amboss tidak hanya berfokus pada informasi anggota jaringan, tetapi juga pada kondisi jaringan itu sendiri.



Di bagian **Statistik**, di bawah menu "Simulasi" sebelah kiri, Anda akan menemukan grafik yang menunjukkan probabilitas keberhasilan pembayaran sebagai fungsi dari jumlah pembayaran.



Faktanya, Anda akan melihat bahwa kurva menurun karena, ketika jumlah pembayaran Anda meningkat, Anda memiliki lebih sedikit kesempatan untuk melihat pembayaran itu dilunasi. Hal ini mencerminkan masalah likuiditas yang sebenarnya pada Lightning Network. Sebagai contoh, pembayaran Anda sebesar `10_000` satoshi memiliki peluang sebesar `79%` untuk dilakukan. Di sisi lain, untuk pembayaran sebesar `3_000_000` satoshi, Anda memiliki peluang kurang dari `13%` untuk berhasil.



![network](assets/fr/11.webp)



Menu **Statistik jaringan** memungkinkan Anda untuk menampilkan statistik secara grafis untuk file :




- Saluran pembayaran
- Simpul
- Kapasitas
- Biaya
- Evolusi saluran.



![network_stat](assets/fr/12.webp)



Pada menu **Statistik pasar**, opsi **Rincian pesanan** memungkinkan Anda untuk melihat permintaan likuiditas pada Lightning Network. Grafik ini juga dapat menunjukkan saluran mana yang paling banyak diminati dan/atau yang memiliki kapasitas besar.



![markets](assets/fr/13.webp)




## Peralatan



Amboss menawarkan sejumlah alat untuk membantu Anda mengoptimalkan pencarian dan tindakan Anda.



### Dekoder Lightning Network



Alat ini terutama bertanggung jawab untuk memberi Anda rincian struktur Lightning Invoice, Lightning Address atau URL Lightning.



Pada halaman beranda, di bagian **Tools**, kirimkan Lightning Address Anda, misalnya.



![decoder](assets/fr/14.webp)



Dari dekoder ini, Anda dapat memperoleh informasi seperti :




- kunci publik node yang terkait dengan Lightning Address Anda;
- Waktu kedaluwarsa Invoice dari Address Anda;
- Minimum dan maksimum yang dapat Anda kirim;
- Node Nostr yang terkait dengan Address Anda, jika Nostr diaktifkan pada node ini.



![decode](assets/fr/15.webp)



### Magma IA



Temukan alat terbaru yang diluncurkan oleh Amboss untuk mengelola koneksi Anda ke node Lightning Network secara efisien. Magma AI menggunakan kecerdasan buatan khusus untuk fokus pada masalah penting: membuat pilihan node yang baik untuk dihubungkan.



![magma](assets/fr/16.webp)



### Kalkulator Satoshi



Untuk mengetahui harga Bitcoin saat ini dalam mata uang lokal anda (EUR/USD). Di halaman beranda, gunakan kalkulator satoshi untuk mengetahui harga pasar saat ini.



![calculator](assets/fr/17.webp)




Anda sekarang telah mengikuti tur lengkap fitur dan alat analisis platform. Silakan baca artikel kami di bawah ini mengenai penjelajah Bitcoin **Mempool.space**.



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f