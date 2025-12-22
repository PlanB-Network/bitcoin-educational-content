---
name: BTCPay Server
description: Menerima pembayaran BTC tanpa perantara
---

![cover](assets/cover.webp)



![video](https://youtu.be/KqsM-n-e4aY)



BTCPay Server adalah paket perangkat lunak sumber terbuka gratis yang dibuat oleh Nicolas Dorier yang memungkinkan pembayaran bitcoin diterima tanpa perantara. Dirancang untuk menawarkan otonomi dan kedaulatan finansial, perangkat lunak ini dipasang di servernya sendiri dan menyediakan manajemen transaksi yang lengkap, mulai dari pembuatan faktur hingga validasi pembayaran on-chain atau Lightning Network, dan akuntansi. Sistem ini terintegrasi dengan mudah dengan situs e-commerce (WooComerce, Shopify, dll.) atau dapat digunakan sebagai terminal pembayaran untuk toko fisik (*POS).



BTCPay Server tidak diragukan lagi merupakan solusi paling canggih bagi para pedagang yang ingin menerima bitcoin. Ini adalah perangkat lunak yang paling komprehensif dan kuat dalam hal keamanan, kedaulatan, dan kerahasiaan. Di sisi lain, ini juga merupakan yang paling rumit untuk dipasang dan dipelihara. Ada juga alternatif yang lebih sederhana: beberapa sepenuhnya bersifat kustodian, seperti OpenNode, sementara yang lain menawarkan kompromi yang menarik antara kemudahan penggunaan dan kedaulatan, seperti Swiss Bitcoin Pay:



https://planb.academy/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a

Tujuan dari tutorial ini adalah untuk memandu Anda langkah demi langkah melalui instalasi, konfigurasi, dan penggunaan BTCPay Server, sehingga Anda dapat menggunakan infrastruktur pembayaran yang aman dan independen sesuai dengan etos Bitcoin.



## Fitur-fitur Server BTCPay



Solusi point-of-sale Bitcoin terpusat, seperti *OpenNode* misalnya, menawarkan kemudahan penggunaan, tetapi bergantung pada perusahaan pihak ketiga karena tidak dapat dihosting sendiri dan, dalam banyak kasus, bersifat eksklusif. Meskipun solusi ini mempermudah pengaturan pembayaran, namun solusi ini melibatkan biaya komisi dan mengekspos penggunanya pada lebih banyak risiko daripada solusi seperti BTCPay Server, baik dalam hal penyimpanan dana dan kerahasiaan.



BTCPay Server ditujukan untuk pedagang online atau fisik, asosiasi, dan organisasi nirlaba yang ingin menerima donasi dalam bentuk bitcoin. Ini juga merupakan solusi ideal bagi pemilik dan pengembang proyek yang mencari dukungan langsung dari komunitas mereka.



Fitur khusus dari BTCPay Server meliputi:




- otonomi penuhnya,
- tidak adanya prosedur **KYC**,
- kendali penuh atas dana**,
- penghapusan biaya platform**.



Dengan menjadi pemroses pembayaran Anda sendiri, Anda menghilangkan ketergantungan pada pihak ketiga yang tersentralisasi antara Anda dan pelanggan. Anda bisa menerima pembayaran secara langsung dalam bentuk bitcoin dan faktur pembayaran generate. Hal ini memastikan bahwa Anda maupun perusahaan Anda tidak dapat diblokir oleh pihak lain. Anda berperan sebagai bank dan pemroses pembayaran, tanpa harus membayar komisi kepada perantara untuk setiap transaksi.



Biaya transaksi untuk **on-chain** tetap ada, tetapi dapat dikurangi dengan menggunakan jaringan **Liquid** atau **Lightning**.



Selain itu :




- Antarmuka dan faktur yang dapat disesuaikan sepenuhnya;
- Dukungan **Tor** asli untuk meningkatkan kerahasiaan;
- Dukungan untuk **crowdfunding**, **POS** dan **tombol pembayaran**;
- Kompatibel dengan banyak mata uang;
- Bitcoin pembayaran langsung dan peer-to-peer;
- Kontrol penuh atas kunci pribadi Anda;
- Privasi yang ditingkatkan;
- Keamanan yang ditingkatkan;
- Perangkat lunak yang dihosting sendiri ;
- Dukungan untuk **SegWit** dan **Jaringan petir**;
- Portofolio internal berbasis node, dengan integrasi portofolio perangkat keras.



## Menginstal dan mengonfigurasi Server BTCPay



### Memilih mode hosting Anda



BTCPay Server dapat diinstal dengan beberapa cara yang berbeda. Bergantung pada kebutuhan dan sumber daya Anda, ada tiga opsi utama:




- Server BTCPay yang dihosting oleh pihak ketiga**: Anda menggunakan platform yang menghosting layanan untuk Anda. Sederhana, tetapi biasanya tidak gratis.
- Server BTCPay dihosting sendiri di server cloud** (misalnya melalui [btcpayprovider](https://btcpayprovider.com/), [Bitcoin People](http://bitcoinpeople.it/) atau penyedia lainnya). Ini adalah solusi yang direkomendasikan untuk sebagian besar pedagang pemula.
- Server BTCPay diinstal pada perangkat keras Anda sendiri (secara lokal)**: di komputer, mini-PC atau Umbrel. Metode ini lebih bersifat teknis, tetapi menawarkan kemandirian total.



https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

Untuk pedagang pemula, **penyebaran pada server cloud** adalah kompromi terbaik antara otonomi, kesederhanaan, dan keamanan, tanpa harus mengelola seluruh infrastruktur teknis.



BTCPay Server dapat digunakan dengan cepat dari sejumlah penyedia hosting. Di antara mereka, **Voltage** menonjol sebagai solusi tolok ukur bagi pengguna yang membutuhkan infrastruktur yang **andal**, **profesional**, dan **berdaulat**.



### Membuat instance Server BTCPay di Voltage



**Voltage** adalah platform hosting Bitcoin dan Lightning siap pakai yang memungkinkan Anda untuk langsung menggunakan Server BTCPay Anda sendiri, tanpa konfigurasi yang rumit atau pemeliharaan server.



Kunjungi [situs web resmi Voltage](https://voltage.cloud).



![capture](assets/fr/03.webp)



Buat **akun pengguna** dengan alamat email yang valid dan kata sandi yang kuat.



![capture](assets/fr/04.webp)



Voltage menawarkan uji coba gratis selama 7 hari. Harap dicatat bahwa setelah uji coba gratis 7 hari, Anda akan diundang untuk mendaftar langganan tetap sebesar **$25 per bulan** untuk terus **mempertahankan node Anda tetap aktif**.



Setelah Anda membuat akun Voltage dan masuk untuk pertama kalinya, Anda akan diarahkan ke halaman beranda, yang memiliki dua bagian utama:




- Bagian **Infrastruktur** untuk mengelola node Lightning, Bitcoin Core, BTCPay Server, dan layanan Bitcoin lainnya di cloud;
- dan bagian **Pembayaran** yang memungkinkan Anda mengakses API Lightning dari Voltage untuk mengintegrasikan pembayaran Bitcoin ke dalam aplikasi yang disesuaikan.



Untuk menggunakan instance **BTCPay Server** Anda, klik **Infrastruktur akses**. Di sinilah Anda dapat membuat, mengelola, dan memantau semua layanan Anda, termasuk node Bitcoin dan BTCPay Server.



#### Membuat grup



Sebelum Anda dapat menggunakan layanan, platform akan meminta Anda untuk **membuat grup**. Sebuah **grup** (ruang kerja) adalah ruang kerja yang mengelompokkan semua layanan Bitcoin dan Lightning Anda (mis. node, Server BTCPay, penjelajah, dll.). Ini seperti folder yang berisi berbagai proyek Anda.



![capture](assets/fr/05.webp)



Untuk keperluan tutorial ini, grup yang telah kita buat akan disebut **Genesis**. Anda dapat menambahkan gambar profil jika Anda mau. Setelah selesai, klik tombol **Buat**. Anda dapat mengundang pengguna lain untuk bergabung dengan grup, dan bahkan mengubah nama grup jika Anda mau.



Pada halaman beranda grup, beberapa opsi muncul:




- Lightning Nodes**: untuk menggunakan Lightning node lengkap (LND);
- Bitcoin Core Node**: untuk meluncurkan node Bitcoin yang lengkap;
- Server BTCPay**: untuk meng-host instance BTCPay yang siap digunakan;
- Akun Nostr**: untuk mengelola identitas Nostr.



Aktifkan **autentikasi ganda (2FA)** untuk mengamankan akun dan layanan Anda (tombol akan terlihat berwarna merah jika dinonaktifkan).



![capture](assets/fr/06.webp)



Klik **BTCPay Server** di antara opsi-opsi yang ada, lalu klik **Luncurkan Toko BTCPay**.



![capture](assets/fr/07.webp)



Voltage kemudian akan meminta Anda untuk **membuat dan mengonfigurasi instance Server BTCPay Anda** dengan memilih **nama layanan** (1) dan mengaktifkan pembayaran Lightning (2).



Anda akan membutuhkan simpul Lightning jika Anda memutuskan untuk menerima pembayaran Lightning.



Jika Anda belum memiliki node Bitcoin atau Lightning, Voltage akan menyarankan Anda untuk membuatnya secara otomatis.



Klik **Buat simpul Petir** (3) .



![capture](assets/fr/08.webp)



Setelah berada di antarmuka pembuatan node, Anda akan diminta untuk memilih antara tata letak **standar** dan **profesional**.



Anda dapat membuat simpul nyata (**Mainnet**) atau simpul uji (**Testnet**). Kemudian klik tombol **Lanjutkan**.



![capture](assets/fr/09.webp)



Untuk tutorial ini, mari kita gunakan paket standar. Masukkan **node name**, **password** dan tekan tombol **Buat**.



![capture](assets/fr/10.webp)



Setelah beberapa saat, node Anda akan beroperasi dan Anda akan dapat membuka saluran gratis dengan kapasitas penerimaan 500.000 sats.



![capture](assets/fr/11.webp)



Sedikit lebih jauh ke bawah di sebelah kanan, Anda akan menemukan semua informasi yang Anda butuhkan tentang simpul Anda!



![capture](assets/fr/12.webp)



Sekarang kita sudah menyiapkan dan menjalankan Lightning node kita, mari kita kembali menginstal server BTCPay. Anda sekarang dapat mengklik tombol **Buat BTCPay**.



![capture](assets/fr/13.webp)



Sebuah halaman akan terbuka dengan detail login default Anda, bersama dengan pesan yang meminta Anda untuk mengubah kata sandi awal Anda. Setelah Anda selesai melakukannya, klik tombol **Login Sekarang** untuk mengakses antarmuka Anda.



![capture](assets/fr/14.webp)



Selesai! Server BTCPay Anda siap digunakan. Anda akan diarahkan langsung ke halaman login server BTCPay Anda.



![capture](assets/fr/15.webp)



Setelah Anda masuk, konfigurasikan **toko** pertama Anda:





- Berikan **nama**.





- Pilih **mata uang default** (EUR, USD, CFA, dll.).





- Pilih **penyedia nilai tukar** (mis. CoinGecko).



![capture](assets/fr/16.webp)



Anda kemudian akan diarahkan ke dasbor toko Anda. Pada antarmuka dasbor, Anda akan melihat bahwa tombol **Buat toko Anda** ditandai dengan warna hijau, karena langkah ini telah selesai.



![capture](assets/fr/17.webp)



Sedikit lebih jauh ke bawah, kita memiliki tombol **Konfigurasi wallet** dan **Konfigurasi Lightning node**. Dalam kasus kami, kami sudah terhubung ke node Lightning yang berjalan dengan voltase. Jadi kita tidak perlu melakukannya di sini.



Mari kita lanjutkan dengan mengonfigurasi portofolio. Klik tombol **Konfigurasi portofolio**.



Karena kita baru saja memulai dengan BTCPay Server, mari hubungkan wallet yang sudah ada. Jadi, tekan **Hubungkan portofolio yang sudah ada**.



![capture](assets/fr/18.webp)



Anda kemudian harus memilih **metode impor**. Di antara pilihan yang tersedia, pilih **Masukkan kunci publik yang diperluas**.



![capture](assets/fr/19.webp)



Dengan menautkan wallet yang sudah ada, Anda dapat menerima pembayaran **langsung pada wallet eksternal ini**, tanpa server BTCPay memiliki akses ke private key Anda. Jadi, meskipun server diretas atau kunci publik (`xpub`) dibobol, penyerang dapat melihat riwayat transaksi Anda, tetapi tidak dapat mengakses dana Anda.



Setelah Anda mengklik tombol **Masukkan kunci publik yang diperluas**, Anda akan **diarahkan** ke halaman di mana Anda harus memberikan kunci ini.



Sekarang mari kita ambil **kunci publik yang diperluas**.



### Menghubungkan Bitcoin wallet



Untuk menerima pembayaran, Anda perlu menghubungkan Bitcoin wallet ke toko Anda. Untuk melakukan ini, Anda memiliki beberapa opsi:





- Portofolio perangkat keras** (Ledger, Trezor, Coldcard...);





- Portofolio perangkat lunak** (Aplikasi Blockstream, Ashigaru, Electrum, Sparrow...)





- BTCPay Server** internal wallet (tidak disarankan, karena kurang aman dan lebih banyak mengekspos dana Anda jika terjadi peretasan server).



Dalam tutorial ini, kita akan menggunakan **portofolio perangkat lunak**, yang lebih mudah diakses untuk konfigurasi awal. Anda dapat memilih dari sejumlah aplikasi yang kompatibel: **Electrum**, **Phoenix**, **Zeus**, **Muun**, dll.



Untuk demonstrasi, kita akan menggunakan **Electrum**. Buka **Electrum**, klik **Portofolio**, lalu **Informasi** :



![capture](assets/fr/20.webp)



Selanjutnya, salin **master public key (xpub)**.



![capture](assets/fr/21.webp)



Setelah Anda menyalin kunci publik utama, tempelkan kunci publik tersebut ke dalam kolom yang tersedia di halaman BTCPay Server.



![capture](assets/fr/22.webp)



Setelah verifikasi, Anda akan diarahkan ke dasbor toko Anda.



![capture](assets/fr/23.webp)



### Membuat Point of Sale (PoS)



Setelah Anda menyiapkan toko dan portofolio Anda, sekarang Anda dapat menyiapkan **Point of Sale (PoS) ** untuk mulai menerima pembayaran Bitcoin langsung dari pelanggan Anda.



Fitur terintegrasi dari **BTCPay Server** ini sangat ideal untuk **pedagang, pengrajin, pemilik restoran, atau penyedia layanan** yang ingin menerima Bitcoin **tanpa situs web** atau keahlian teknis khusus.



### Apa gunanya penjualan?



PoS adalah **antarmuka POS yang disederhanakan** yang bertindak sebagai **terminal pembayaran Bitcoin**.


Ini memungkinkan Anda untuk :




- Buat **menu produk atau layanan** dengan harga tetap.
- Hasilkan **faktur instan dengan kode QR** untuk dipindai.
- Bagikan **URL Pembayaran** yang dapat diakses melalui ponsel cerdas, tablet, atau komputer.



Dengan kata lain, PoS mengubah Server BTCPay Anda menjadi **antarmuka penjualan langsung**, di mana setiap pembayaran diterima **di Bitcoin wallet Anda sendiri**, tanpa perantara.



### Mengkonfigurasi PoS



Di dasbor BTCPay, klik **PLUGINS**, lalu **Penjualan**.



Kemudian klik **Buat aplikasi PoS baru**. Tindakan ini akan menambahkan **aplikasi baru** ke toko BTCPay Anda, seolah-olah Anda sedang memasang situs penjualan internal mini.



Sebuah halaman terbuka untuk membuat aplikasi Anda. Tentukan **nama aplikasi**: ini adalah nama internal, yang hanya dapat dilihat dari dasbor Anda (mis. _Toko Sepatu_).



Klik **Buat** untuk memvalidasi.



![capture](assets/fr/24.webp)



Setelah dibuat, Anda akan diarahkan ke halaman **Konfigurasi rinci** Point of Sale.



### Sesuaikan antarmuka penjualan Anda



Pada halaman ini, Anda dapat menentukan elemen-elemen penting dari PoS Anda:





- Nama aplikasi** (nama manajemen internal, dapat diubah sewaktu-waktu).





- Judul tampilan** (apa yang akan dilihat pelanggan Anda di bagian atas halaman).





- Gaya titik penjualan** (Mode **Deskripsi** cocok untuk layanan seperti potong rambut atau makanan, sedangkan mode **Katalog produk** ideal untuk toko yang menawarkan beberapa item).





- Menampilkan mata uang** (pilih **XOF**, **EUR** atau **USD** sesuai dengan harga yang biasa Anda gunakan).





- Daftar produk** (tambahkan produk, deskripsi, dan harga Anda di sini).



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



### Simpan dan uji PoS Anda



Setelah Anda selesai mengonfigurasi, klik **Save** untuk menyimpan pengaturan Anda, lalu **Lihat** untuk melihat pratinjau PoS Anda.



Anda akan melihat halaman yang menampilkan produk Anda, dengan setiap tombol yang sesuai dengan item atau layanan.



Segera setelah pelanggan memilih produk:



1. BTCPay secara otomatis menghasilkan faktur Bitcoin atau Lightning**.



2. Kode **QR** muncul di layar.



3. Pelanggan dapat **memindai dan membayar secara langsung** dengan Bitcoin wallet mereka.




![capture](assets/fr/27.webp)



### Hasil akhir



Anda sekarang memiliki **Pos Penjualan Bitcoin** lengkap yang dapat Anda gunakan:





- Buka dari smartphone atau tablet di toko Anda;





- Menampilkan pada layar untuk dipindai oleh pelanggan;





- Atau bagikan melalui **URL** publik, seperti halaman pemesanan yang disederhanakan.



Dengan setiap pembayaran, jumlah tersebut secara otomatis dikreditkan ke **BTCPay wallet Anda sendiri**, tanpa perantara atau biaya pihak ketiga.


Hal ini mengubah PoS Anda menjadi **terminal pembayaran Bitcoin yang berdiri sendiri**.




## Penggunaan sehari-hari



Sebelum mencairkan pembayaran yang sebenarnya, kami sarankan Anda melakukan **pengujian** untuk memastikan bahwa semuanya berfungsi dengan baik.



### Menguji pembayaran





- Buat faktur** dari antarmuka PoS Anda (misalnya, produk 1 satoshi atau jumlah kecil).





- Pindai kode QR di layar** menggunakan Bitcoin atau Lightning wallet (seperti **Phoenix**, **Muun** atau **Wallet dari Satoshi**).




![capture](assets/fr/28.webp)





- Validasi pembayaran** di wallet Anda: transaksi akan langsung terkirim.





- Kembali ke Server BTCPay**: faktur akan muncul sebagai **Lunas** dalam daftar.



![capture](assets/fr/29.webp)



Selamat! Mesin Kasir Anda sekarang sudah **berfungsi**. Anda bisa mulai menerima pembayaran Bitcoin dari pelanggan Anda, dengan mudah, cepat dan tanpa perantara.



### Membuat faktur untuk pelanggan



Pada menu **Faktur**, klik **Faktur baru**.



![capture](assets/fr/30.webp)



Masukkan **jumlah** dan **mata uang lokal** (BTCPay secara otomatis menghitung ekuivalen dalam BTC), serta informasi produk lainnya.



![capture](assets/fr/31.webp)



Bagikan **kode QR** atau **URL** kepada pelanggan.



![capture](assets/fr/32.webp)



### Melacak pembayaran yang diterima



Masih di menu **Faktur**, Anda akan melihat daftar semua transaksi Anda.


Status yang mungkin adalah :





- Pending**: pembayaran belum dikonfirmasi.





- Dibayar**: pembayaran telah dikonfirmasi.





- Kadaluarsa**: faktur yang tidak dibayar pada tanggal jatuh tempo.



### Pengembalian dana kepada pelanggan



Pada menu **Faktur**, pilih faktur yang akan diganti.



![capture](assets/fr/33.webp)



Klik **Refund** dan masukkan alamat Bitcoin yang diberikan oleh pelanggan.



![capture](assets/fr/34.webp)



![capture](assets/fr/35.webp)



### Laporan dan ekspor data



BTCPay Server memungkinkan Anda **mengekspor transaksi Anda** (dalam format CSV atau Excel). Ini sangat praktis untuk tindak lanjut akuntansi dan mesin kasir Anda.



![capture](assets/fr/36.webp)



Pada menu **Laporan**, klik **Ekspor**: semua transaksi Anda akan disimpan dalam file CSV, yang dapat Anda lihat secara lokal.



## Keselamatan dan praktik terbaik



Otonomi yang diberikan oleh BTCPay Server (kedaulatan penuh atas dana Anda) adalah kekuatan yang nyata. Namun dengan kebebasan ini, muncul tanggung jawab yang lebih besar dalam hal keamanan. Dengan mengelola pembayaran Anda sendiri, Anda mengambil peran sebagai bank Anda sendiri. Oleh karena itu, sangat penting untuk menerapkan praktik terbaik untuk melindungi dana, data, dan infrastruktur Anda. Berikut adalah poin-poin utama yang perlu dipertimbangkan.



### Akses aman ke server Anda





- Gunakan kata sandi yang kuat: kombinasikan huruf besar dan kecil, angka, dan karakter khusus. Hindari penggunaan ulang kata sandi yang sudah ada.
- Aktifkan autentikasi dua faktor (2FA) untuk mengakses antarmuka BTCPay Anda.
- Perbarui sistem operasi Anda secara teratur, instance BTCPay Server Anda dan dependensi Anda (Docker, Bitcoin node, Lightning node...). Pembaruan sering kali memperbaiki kerentanan keamanan.



### Mengelola dan mencadangkan kunci pribadi





- Simpan kunci pribadi dan seedphrase Anda secara offline, pada media fisik (kertas atau logam).
- Sebaiknya gunakan perangkat keras wallet wallet.
- Simpan beberapa salinan cadangan Anda, di lokasi fisik yang terpisah dan terlindungi.



### Pembayaran dan kerahasiaan yang aman





- Gunakan jaringan Tor atau VPN untuk menyembunyikan alamat IP peladen Anda dan melindungi privasi Anda.
- Nonaktifkan port yang tidak perlu pada server Anda dan batasi koneksi SSH hanya pada alamat tepercaya.
- Aktifkan HTTPS (sertifikat SSL) untuk semua koneksi ke antarmuka web BTCPay Anda.
- Jangan pernah berbagi antarmuka administrasi Anda dengan personel yang tidak terlatih dalam manajemen portofolio Bitcoin.



### Menerapkan praktik terbaik untuk jaringan Lightning



Toko Anda terhubung ke **node Lightning yang di-host di Voltage**, yang sangat menyederhanakan manajemen teknis jaringan. Namun demikian, tetap penting untuk menerapkan **praktik pemantauan dan keamanan yang baik**:





- Simpan kunci masuk dan akses API** node Voltage Anda (yang memungkinkan BTCPay terhubung).
- Lindungi akun Voltage Anda** dengan autentikasi dua faktor dan kata sandi yang kuat.
- Memantau status node dan saluran** dari dasbor Voltage Anda: ini membantu Anda menemukan anomali atau desinkronisasi.
- Hindari membagikan kredensial API** Anda atau mengeksposnya secara publik (misalnya dalam kode situs).
- Jika terjadi migrasi, cukup **konfigurasi ulang tautan antara BTCPay dan Voltage**: tidak ada saluran yang perlu ditutup secara manual.



Dengan Voltage, Anda mendapatkan keuntungan dari infrastruktur yang **aman, sangat tersedia** dan **secara otomatis dicadangkan**, sambil mempertahankan **kedaulatan penuh atas pembayaran Lightning Anda**.



### Mengatur dan menyusun prosedur internal





- Tentukan kebijakan manajemen akses yang jelas: siapa yang dapat membuat faktur, melihat pembayaran, mengakses node, dll.
- Dokumentasikan prosedur pencadangan dan pemulihan Anda sehingga Anda dapat bereaksi dengan cepat jika terjadi insiden.
- Uji pemulihan cadangan Anda secara teratur untuk memastikan cadangan berfungsi dengan baik.
- Latihlah staf atau kolaborator Anda dalam hal keamanan operasional dasar: kewaspadaan terhadap phishing, penggunaan kata sandi yang aman, dan menghargai kerahasiaan.



### Mengawasi dan menetapkan pemeliharaan yang berkelanjutan





- Pantau terus aktivitas server Anda menggunakan alat pencatatan atau pemantauan.
- Jadwalkan tinjauan keamanan secara berkala: periksa pembaruan, akses, cadangan, dan konsistensi transaksi.



Selamat! Anda telah mencapai bagian akhir dari tutorial ini. Sekarang Anda bisa menggunakan BTCPay Server sendiri, sehingga memudahkan Anda untuk mengelola toko Anda.



Untuk mengetahui lebih lanjut, saya sarankan Anda mengikuti kursus pelatihan lengkap kami tentang cara mengintegrasikan Bitcoin ke dalam perusahaan Anda:



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a