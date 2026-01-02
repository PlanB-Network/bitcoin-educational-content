---
name: Amboss
description: Jelajahi dan analisis Lightning Network
---

![cover](assets/cover.webp)



Lightning Network adalah sebuah Layer di atas protokol Bitcoin yang dikembangkan untuk mendorong penggunaan Bitcoin sebagai alat pembayaran sehari-hari dengan meningkatkan kecepatan pemrosesan transaksi. Dengan tetap berpegang pada prinsip desentralisasi, Lightning Network terdiri dari node, yaitu komputer yang menjalankan implementasi Lightning, yang saling terhubung secara peer-to-peer untuk mengirimkan data pembayaran dan memverifikasi transaksi satu sama lain.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Sama seperti di rantai utama, penting bagi pengguna untuk bisa mengetahui informasi dan status jaringan, supaya koneksi antar node bisa berjalan lancar dan masalah likuiditas yang sering muncul di jaringan bisa diminimalkan. Di Lightning Network, biasanya kami menyarankan penggunaan untuk pembayaran mikro dengan jumlah yang relatif lebih kecil dibandingkan transaksi di rantai utama Bitcoin.

Perlu kamu catat bahwa tidak semua node Lightning tersedia di platform Amboss.



Seperti [Mempool Space](https://Mempool.space), yang menyediakan informasi berguna tentang rantai utama protokol Bitcoin, sejak tahun 2022 [Amboss](https://amboss.space) menyediakan informasi tentang :

- Node pada Lightning Network
- Saluran pembayaran dan kapasitas pembayarannya
- Evolusi Lightning Network dari waktu ke waktu
- Statistik tentang biaya ke node relai untuk pembayaran.

https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

Dalam tutorial ini, aku akan mengajak kamu menjelajahi platform ini sebagai sumber daya penting bagi pengguna Lightning Network, termasuk buat kamu yang ingin menghubungkan node sendiri untuk memperluas jaringan dan seterusnya.

## Temukan pasangan

Salah satu tujuan dari platform Amboss adalah memudahkan berbagai node dalam jaringan untuk saling terhubung dan bertukar informasi. Di halaman beranda platform, kamu bisa langsung mencari nama node yang sudah kamu kenal, atau menemukan node dari dompet Lightning populer yang kamu gunakan.

![home](assets/fr/01.webp)

![wallet](assets/fr/02.webp)



https://planb.academy/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

Di halaman beranda, kamu juga akan menemukan node yang diklasifikasikan menurut :

- Evolusi kapasitas: jumlah Bitcoin yang terkait dengan kunci publik node dan total yang tersedia di semua salurannya.
- Evolusi saluran: jumlah koneksi baru ke node lain dalam jaringan.
- Popularitas node: seberapa sering node tersebut digunakan.



![nodes](assets/fr/03.webp)



Oleh karena itu, memilih node yang tepat untuk disambungkan adalah dengan memeriksa kriteria berikut ini:

- Pastikan node memiliki jumlah bitcoin yang cukup. Semakin besar kapasitas node, semakin besar pula jumlah bitcoin yang bisa kamu bayarkan melaluinya.
- Pastikan node memiliki banyak koneksi dan saluran yang terbuka dengan node lain di jaringan.
- Pastikan node aktif dan masih dihargai oleh rekan-rekannya dengan memeriksa jumlah saluran baru. Semakin banyak saluran baru yang dibuka oleh node ini, semakin tinggi reputasinya di jaringan.

Setelah kamu menemukan node yang tepat, klik namanya untuk masuk ke halaman informasinya.

Di tampilan ini, dengan melihat timestamp dari saluran yang baru dibuka, kamu bisa mendapatkan gambaran tentang aktivitas node tersebut. Kamu juga akan menemukan informasi mengenai kapasitas salurannya, dan ini sangat penting kalau kamu berniat menggunakan node itu secara aktif untuk melakukan pembayaran.

![node_info](assets/fr/04.webp)



Di bagian kiri, kamu akan menemukan rincian lebih lanjut tentang lokasi node ini. Sebagai contoh, kamu dapat melihat :

- Kunci publik: pengenal tepat di bawah nama simpul.
- Posisi geografis simpul ini.




![channels](assets/fr/05.webp)



Interface ini menampilkan alamat koneksi node dalam format `pubkey@ip:port`. Dalam contoh ini, kita ingin terhubung ke node yang punya berkas berikut:

- kunci publik `pubkey` adalah: `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- iP Address: `170.75.163.209`
- Pelabuhan: `9735`



![geoinfo](assets/fr/06.webp)


Pada bagian **Channels**, Anda akan melihat daftar saluran yang terbuka dan koneksi node ke node lain dalam jaringan. Pada Interface ini, beberapa informasi sangat penting untuk mengonfirmasi bahwa node ini sesuai dengan kebutuhan kita atau dapat diandalkan:





- Rasio masuk**: Jumlah yang akan ditagih oleh node kepada Anda untuk setiap juta Satoshi yang diterimanya, tergantung saluran yang dipilih.
- Rasio (bagian per juta)**: yang mewakili jumlah Satoshi per juta unit yang akan ditagih oleh node kepada Anda ketika Anda memutuskan untuk melakukan pembayaran melalui salah satu salurannya. Katakanlah Anda memutuskan untuk melakukan pembayaran sebesar `10_000 Sats` melalui saluran yang rasio ppm-nya adalah `500 Sats`, Anda harus membayar satoshi `10_000 * 500 / 1_000_000` kepada node tersebut, yang setara dengan `5 Sats`.
- Maksimum [HTLC](https://planb.academy/resources/glossary/htlc) **: Jumlah maksimum yang dapat ditransmisikan oleh node ini melalui salah satu saluran ini.

Dengan melihat tabel pada Interface ini, kamu juga dapat menemukan semua informasi ini pada node yang dicocokkan.



![channels_info](assets/fr/07.webp)



Pada bagian **Peta saluran**, Kamu dapat melihat distribusi dan kapasitas berbagai saluran pada node ini. Kamu bisa mengubah cara distribusi ditampilkan dengan memilih salah satu opsi pada menu drop-down di bagian kanan.



![cha_maps](assets/fr/08.webp)



Bagian **Saluran yang ditutup** mengelompokkan semua saluran yang pernah ditutup oleh node menurut jenis penutupan:




- Penutupan bersama**: mewakili kesepakatan kedua belah pihak, yang menggunakan kunci pribadi mereka untuk menandatangani transaksi yang menandai penutupan saluran dan distribusi saldo di dalamnya
- Penutupan paksa: mewakili penutupan satu bagian saluran secara tiba-tiba dan sepihak. Jenis penutupan ini tidak disarankan, karena Lightning Network adalah protokol berbasis hukuman: ketika kamu mencoba menipu saldo saluran, kamu berisiko kehilangan semua saldo yang tersedia di saluran tersebut.



![closed](assets/fr/09.webp)



Dapatkan informasi tentang biaya transit untuk merutekan pembayaran melalui saluran pada node yang kamu gunakan



![fees](assets/fr/10.webp)



## Informasi jaringan



Amboss tidak hanya berfokus pada informasi anggota jaringan, tetapi juga pada kondisi jaringan itu sendiri.



Di bagian **Statistik**, di bawah menu "Simulasi" sebelah kiri, kamu akan menemukan grafik yang menunjukkan probabilitas keberhasilan pembayaran sebagai fungsi dari jumlah pembayaran.



Kamu akan melihat bahwa kurvanya menurun karena semakin besar jumlah pembayaran, semakin kecil kemungkinan pembayaran tersebut bisa tersalurkan. Ini menggambarkan masalah likuiditas yang sebenarnya terjadi di Lightning Network. Misalnya, pembayaran sebesar `10_000` satoshi memiliki peluang sekitar 79% untuk berhasil. Namun untuk pembayaran sebesar `3_000_000` satoshi, peluang keberhasilannya turun menjadi kurang dari 13%.



![network](assets/fr/11.webp)



Menu **Statistik jaringan** memungkinkanMU untuk menampilkan statistik secara grafis untuk file :




- Saluran pembayaran
- Node
- Kapasitas
- Biaya
- Evolusi saluran.



![network_stat](assets/fr/12.webp)



Pada menu **Statistik pasar**, opsi **Rincian pesanan** memungkinkan kamu untuk melihat permintaan likuiditas pada Lightning Network. Grafik ini juga dapat menunjukkan saluran mana yang paling banyak diminati dan/atau yang memiliki kapasitas besar.



![markets](assets/fr/13.webp)




## Peralatan



Amboss menyediakan berbagai alat yang bisa membantu kamu mengoptimalkan pencarian serta tindakan kamu di jaringan.


### Dekoder Lightning Network



Alat ini terutama bertanggung jawab untuk memberi kamu rincian struktur Lightning Invoice, Lightning Address atau URL Lightning.



Pada halaman beranda, di bagian **Tools**, kirimkan Lightning Address kamu, misalnya.



![decoder](assets/fr/14.webp)



Dari dekoder ini, kamu dapat memperoleh informasi seperti :




- kunci publik node yang terkait dengan Lightning Address kamu;
- Waktu kedaluwarsa Invoice dari Address kamu;
- Minimum dan maksimum yang dapat Anda kirim;
- Node Nostr yang terkait dengan Address Anda, jika Nostr diaktifkan pada node ini.



![decode](assets/fr/15.webp)



### Magma IA


Temukan alat terbaru yang diluncurkan oleh Amboss untuk mengelola koneksi kamu ke node Lightning Network secara efisien. Magma AI menggunakan kecerdasan buatan khusus untuk fokus pada hal yang paling penting: memilih node yang tepat untuk dihubungkan.


![magma](assets/fr/16.webp)



### Kalkulator Satoshi



Untuk mengetahui harga Bitcoin saat ini dalam mata uang lokal anda (EUR/USD). Di halaman beranda, gunakan kalkulator satoshi untuk mengetahui harga pasar saat ini.



![calculator](assets/fr/17.webp)




Sekarang kamu telah mengikuti tur lengkap fitur dan alat analisis platform. Silakan baca artikel kami di bawah ini mengenai penjelajah Bitcoin **Mempool.space**.



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f
