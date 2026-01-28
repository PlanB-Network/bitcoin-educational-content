---
name: Tiankii
description: Rangkaian alat bantu Lightning untuk peritel dan konsumen
---

![cover](assets/cover.webp)



Dalam ekosistem Bitcoin, menerima pembayaran secara real time masih menjadi tantangan utama bagi bisnis dan individu. Solusi tradisional sering kali membutuhkan pengetahuan teknis tingkat lanjut, infrastruktur yang rumit untuk dipelihara, atau membutuhkan dana yang disimpan oleh perantara. Situasi ini menghambat adopsi massal Bitcoin sebagai mata uang sehari-hari, terlepas dari janji kemajuan teknologi Lightning Network.



Tiankii, sebuah perusahaan Salvador yang lahir pada tahun 2021, menanggapi masalah ini dengan menawarkan infrastruktur Bitcoin modular yang dapat diakses. Alih-alih memaksa adopsi ekosistem tertutup, Tiankii menawarkan serangkaian alat yang saling berhubungan yang memungkinkan siapa pun untuk mengintegrasikan Bitcoin Lightning ke dalam bisnis mereka tanpa mengorbankan kendali atas dana mereka.



## Apa itu Tiankii?



### Asal usul dan filosofi



Tiankii - istilah Nahuatl yang berarti "pasar terbuka yang dapat diakses oleh semua orang" - adalah perusahaan rintisan Bitcoin pertama di El Salvador yang 100% menggunakan Bitcoin. Didirikan oleh Darvin Otero setelah adopsi Bitcoin sebagai alat pembayaran yang sah di negara tersebut, perusahaan ini bertujuan untuk mengubah Bitcoin dari penyimpan nilai menjadi mata uang yang dapat ditransaksikan untuk pembelian sehari-hari. Tidak seperti platform kustodian, Tiankii mengadopsi pendekatan non-kustodian di mana pengguna tetap memegang kendali atas dana mereka, dengan infrastruktur yang hanya berfungsi sebagai perantara teknis.



### Arsitektur teknis



Tiankii diposisikan sebagai penyedia infrastruktur Bitcoin-as-a-Service berdasarkan Lightning Network. Teknologi lapisan kedua ini memungkinkan transaksi yang hampir seketika dengan biaya yang dapat diabaikan, sehingga memungkinkan pembayaran mikro dan pembelian sehari-hari.



Arsitekturnya didasarkan pada tiga pilar:



**Prioritas utama Lightning**: Secara sistematis mendukung jaringan Lightning untuk kecepatan dan biaya yang lebih rendah, sambil mempertahankan dukungan transaksi on-chain untuk jumlah besar.



**Standar terbuka**: Penggunaan LNURL untuk mengotomatiskan permintaan pembayaran, Lightning Address untuk ID email yang dapat dibaca, dan Kartu Bolt untuk pembayaran NFC yang dapat dioperasikan.



*modularitas *wallet-agnostik**: Kemungkinan untuk menghubungkan portofolio Lightning yang berbeda (LNbits, Blink, BlueWallet) atau node Anda sendiri, menawarkan fleksibilitas maksimum tergantung pada tingkat keahlian dan otonomi yang diperlukan.



## Alat ekosistem Tiankii



### Bitcoin POS - Terminal pembayaran di dalam toko



Aplikasi ini mengubah ponsel cerdas atau tablet menjadi terminal Lightning. Pedagang memasukkan jumlah dalam mata uang lokal, dan aplikasi menghasilkan kode QR Lightning atau menerima Kartu Bolt. Transaksi langsung dikreditkan tanpa komisi, dengan konversi otomatis dalam lebih dari 150 mata uang, manajemen tip, dan riwayat penjualan.



### Dasbor Pedagang - Manajemen penjualan terpadu



Interface web terpusat untuk menghubungkan wallet Lightning, melacak transaksi secara real time, menerbitkan faktur, dan laporan akuntansi generate. Platform ini menggabungkan semua saluran: pembayaran di dalam toko (POS), penjualan online (plug-in e-commerce), atau integrasi API. Pembayaran menyatu pada wallet yang dipilih.



### Bitcoin Kartu Nirkontak (Kartu Bolt)



Kartu NFC Bolt mewakili inovasi utama Tiankii dalam mendemokratisasi Bitcoin untuk masyarakat umum. Berfungsi seperti kartu bank nirsentuh, kartu ini memungkinkan Anda membayar pembelian Bitcoin Lightning hanya dengan mengetuk terminal yang kompatibel.



Tidak seperti solusi kustodian tradisional, kartu ini mengikuti standar terbuka yang menjamin interoperabilitas. Pengguna dapat menautkannya ke wallet mereka sendiri melalui aplikasi IBI, sehingga tetap memiliki kunci pribadi dan kontrol penuh atas dana terkait. Pembayaran hanya membutuhkan waktu satu detik, tanpa perlu mengeluarkan ponsel cerdas Anda atau memiliki koneksi internet aktif pada saat pembayaran.



Solusi ini sangat inklusif bagi orang-orang yang tidak terbiasa dengan smartphone, menawarkan gerbang yang dapat diakses ke ekonomi Bitcoin.



### Aplikasi IBI - Interface individu Bitcoin



Aplikasi IBI (Individual Bitcoin Interface) dirancang untuk individu yang ingin menggunakan Bitcoin Lightning setiap hari. Keuntungan utamanya terletak pada pembuatan Address Lightning yang dipersonalisasi, pengenal pembayaran yang dapat dibaca dalam format email (contoh: alice@ibi.me).



Pengenal ini secara drastis menyederhanakan penerimaan pembayaran: tidak perlu membuat faktur baru untuk setiap transaksi, pengirim cukup memasukkan alamat Lightning. Antarmuka ini juga memungkinkan Anda mengelola Kartu Bolt Anda (aktivasi, penonaktifan, batas pengeluaran), menghubungkan berbagai dompet Lightning, dan melakukan pembayaran dengan memindai kode QR.



### Plugin perdagangan elektronik



Integrasi siap pakai untuk WooCommerce, Shopify, dan Cloudbeds. Instal dalam hitungan menit untuk menambahkan Bitcoin Lightning ke pembayaran. Manfaat: komisi nol (vs. 2-3% kartu kredit), penyelesaian instan, akses di seluruh dunia, penghapusan tolak bayar. Pembayaran tiba langsung di wallet pedagang yang terhubung.



### Bitcoin API dan alat bantu pengembang



SDK Tiankii memungkinkan untuk mengintegrasikan Bitcoin Lightning ke dalam aplikasi yang sudah ada tanpa mempertahankan node-nya sendiri. API menangani pembuatan faktur, verifikasi pembayaran, dan pengiriman massal melalui infrastruktur yang kuat yang dihosting di Google Cloud. Command Center melengkapi penawaran untuk organisasi dengan Address Lightning pada domain khusus, pembayaran massal, dan manajemen terpusat terminal dan kartu NFC.



## Instalasi dan langkah pertama



### Prasyarat penting



Menggunakan Tiankii tidak memerlukan prasyarat teknis yang rumit. Aplikasi beroperasi melalui browser web di smartphone, tablet, atau komputer. Tidak diperlukan instalasi aplikasi asli: yang Anda perlukan hanyalah akses Internet dan browser terbaru untuk mengakses IBI atau Dasbor Pedagang.



**Untuk pengguna pribadi (Aplikasi IBI) **: Tidak diperlukan wallet Lightning sebelumnya. Saat Anda membuat akun, Tiankii secara otomatis mengonfigurasi Address Lightning yang berfungsi melalui [Breez SDK Liquid](https://sdk-doc-liquid.breez.technology/guide/about_breez_sdk_liquid.html), implementasi tanpa kabel yang menggunakan jaringan Liquid di latar belakang. Anda dapat langsung menerima dan mengirim pembayaran tanpa konfigurasi teknis apa pun. Solusi ini secara drastis menyederhanakan akses untuk pemula, namun tetap bersifat mandiri.



**Untuk pedagang (Dasbor Pedagang)**: Koneksi dari wallet Lightning yang ada adalah wajib untuk menggunakan terminal Point of Sale dan menerima pembayaran. Tiankii mendukung banyak solusi: dompet seluler (Blink, Strike), solusi yang dihosting sendiri (LNbits, LND / node CLN), atau dompet web (Alby). Panduan koneksi terperinci tersedia di bagian Sumber Daya pada tutorial ini.



### Untuk pelanggan pribadi: Aplikasi IBI



**Pembuatan akun



Buka akun.ibi.me untuk membuat akun Anda. Di halaman ini Anda dapat memilih di antara dua jenis akun: "Penggunaan Pribadi" untuk penggunaan perorangan, atau "Penggunaan Bisnis" untuk penggunaan komersial. Pilih "Penggunaan Pribadi" untuk mengakses alat bantu untuk menerima dan mengirim pembayaran di Bitcoin.



![Choix du type de compte](assets/fr/01.webp)



Setelah memilih "Penggunaan Pribadi", Anda akan secara otomatis diarahkan ke go.ibi.me untuk menyelesaikan pendaftaran Anda. Hal ini dapat dilakukan melalui email, nomor telepon, atau menggunakan akun Google, Microsoft, atau Twitter Anda. Setelah dibuat, Anda dapat segera mengakses antarmuka IBI Anda, dengan Lightning Address yang sudah beroperasi.



![Création du compte](assets/fr/02.webp)



**Interface utama**



Antarmuka IBI menampilkan saldo Anda dalam satoshi dan mata uang lokal (USD). Tiga tombol memungkinkan Anda untuk berinteraksi: "Terima" untuk menerima pembayaran, "Pindai" untuk memindai kode QR, dan "Kirim" untuk mengirim satoshi.



![Interface IBI](assets/fr/03.webp)



**Menerima pembayaran**



Untuk menerima satoshi, tekan "Terima". Aplikasi akan secara otomatis menghasilkan kode QR dan menampilkan Address Lightning yang telah dipersonalisasi (format nom@ibi.me). Bagikan alamat ini atau kode QR kepada pengirim: dana akan langsung masuk ke rekening IBI Anda.



![Réception avec Lightning Address](assets/fr/04.webp)



Setelah saldo Anda dikreditkan, Anda dapat menggunakan satoshi ini untuk melakukan pembayaran.



**Kirim pembayaran**



Untuk mengirim satoshi, tekan "Kirim". Anda dapat memindai kode QR Lightning, atau langsung memasukkan tujuan Lightning Address.



![Solde et boutons IBI](assets/fr/05.webp)



![Interface d'envoi](assets/fr/06.webp)



Masukkan jumlah yang diinginkan dalam satoshi, periksa jumlah yang setara dalam mata uang lokal, lalu konfirmasikan pembayaran.



![Confirmation du montant](assets/fr/07.webp)



Notifikasi sukses akan mengonfirmasi pengiriman dengan rincian: jumlah yang dikirim, biaya transaksi, dan penerima.



![Paiement réussi](assets/fr/08.webp)



**Manajemen akun



Dalam Pengaturan, Anda dapat mengelola kartu NFC Bitcoin (Kartu Bolt). Antarmuka ini memungkinkan Anda mengaktifkan, menonaktifkan, atau menetapkan batas pengeluaran untuk kartu Anda.



![Historique des transactions](assets/fr/09.webp)



![Paramètres IBI](assets/fr/10.webp)



### Untuk pedagang: Dasbor Pedagang dan POS



**Pembuatan akun bisnis



Buka akun.ibi.me untuk membuat akun Anda. Pilih "Penggunaan Bisnis" untuk mengakses alat pedagang. Jenis akun ini membuka akses ke Dasbor Penjual dan terminal point-of-sale.



Setelah memilih "Penggunaan Bisnis", Anda akan secara otomatis diarahkan ke Dasbor Pedagang (pay.tiankii.com). Ini akan membawa Anda ke antarmuka manajemen bisnis dengan pelacakan pendapatan, transaksi, dan alat pembayaran. Untuk mulai menerima pembayaran, Anda harus terlebih dahulu menghubungkan wallet Lightning Anda dengan mengklik tautan di bagian atas halaman (lihat panah pada gambar).



![Dashboard marchand](assets/fr/11.webp)



*koneksi *wallet Lightning**



Langkah penting dalam mengaktifkan kasir Anda: hubungkan wallet Lightning Anda untuk menerima pembayaran. Antarmuka menawarkan beberapa opsi koneksi. Harap diperhatikan bahwa beberapa opsi (Bitcoin Onchain dan Lightning Network) masih dalam tahap pengembangan dan tampak berwarna abu-abu pada antarmuka.



![Options de connexion wallet](assets/fr/12.webp)



Untuk tutorial ini, kami menggunakan koneksi Lightning Address, yang kompatibel dengan Chivo, Blink Wallet dan Strike. Masukkan Lightning Address Anda (format nom@domaine.com), misalnya dari LN Markets, Alby, atau pemasok lain yang kompatibel.



![Saisie de la Lightning Address](assets/fr/13.webp)



Setelah Anda masuk, akun Anda sudah beroperasi. Anda sekarang dapat mengakses POS atau kembali ke dasbor untuk mengonfigurasi pengaturan lainnya.



![Connexion réussie](assets/fr/14.webp)



*tautan Pembayaran** *Tautan Pembayaran



Menu "Alat Pembayaran" memberikan akses ke "Permintaan Pembayaran", yang memungkinkan Anda membuat dan mengelola tautan pembayaran. Fitur ini berguna untuk membuat tautan pembayaran yang dipersonalisasi untuk dikirim melalui email atau pesan: donasi, pembayaran tunggal, beberapa pembayaran, atau bahkan paywall untuk melindungi konten. Anda bisa membuat berbagai jenis tautan yang sesuai dengan kebutuhan bisnis Anda.



![Liens de paiement](assets/fr/15.webp)



**Konfigurasi terminal penjualan ** Konfigurasi terminal penjualan



Untuk menerima pembayaran di dalam toko, akses menu "Terminal Penjualan" dari "Alat Pembayaran". Bagian ini memungkinkan Anda untuk membuat dan mengelola terminal POS Anda (jumlah terminal tergantung pada paket Anda, lihat paket Freemium vs. paket Bisnis di bawah ini). Klik "Buka" untuk membuka antarmuka POS di browser Anda.



![Gestion des terminaux](assets/fr/16.webp)




**Menghasilkan penjualan**



Terminal POS menampilkan papan tombol angka untuk memasukkan jumlah penjualan. Masukkan jumlah dalam mata uang lokal Anda (misalnya 500 sats setara dengan 630,74 ARS), lalu tekan "OK" untuk mengonfirmasi.



![Saisie du montant](assets/fr/17.webp)



Aplikasi ini secara instan menghasilkan kode QR Lightning dan Lightning Address untuk pembayaran. Pelanggan dapat memindai kode QR dengan wallet atau menggunakan Kartu Bolt pada terminal NFC.



![QR code de paiement](assets/fr/18.webp)



Segera setelah pembayaran diterima, layar konfirmasi akan muncul, menunjukkan jumlah yang diterima dalam mata uang lokal dan satoshi. Anda dapat mengirimkan tanda terima melalui email, mencetak tiket, atau segera memulai penjualan baru.



![Paiement encaissé](assets/fr/19.webp)



**Pemantauan dan manajemen**



Semua transaksi dicatat di Dasbor Pedagang Anda. Anda memiliki pelacakan lengkap atas pendapatan berdasarkan periode, jumlah total penjualan, dan riwayat terperinci untuk akuntansi Anda.



Antarmuka Pengaturan menawarkan beberapa tab konfigurasi. Tab "Pengaturan Umum" memungkinkan Anda mengelola profil pedagang dan notifikasi. Tab "Pengguna" memungkinkan Anda menambahkan dan mengelola akses ke Dasbor Pedagang untuk tim Anda (manajemen multi-pengguna sesuai dengan paket Anda). Tab "Ruang Kerja Pengembangan" memberikan akses ke kunci API untuk integrasi tingkat lanjut, sementara "Langganan" memungkinkan Anda mengelola langganan.



![Paramètres du compte marchand](assets/fr/20.webp)



**Paket Premium vs Paket Bisnis



Tiankii menawarkan dua paket untuk Dasbor Pedagang. Paket **Freemium** (gratis) cocok untuk perusahaan baru dengan batasan: satu titik penjualan, satu pengguna, volume bulanan terbatas hingga 1.000 USD, dan tidak ada akses ke konektor e-commerce. Paket **Business** (biaya 0,5% per transaksi) menawarkan terminal tak terbatas, pengguna tak terbatas, volume tak terbatas, akses ke plugin WooCommerce/Shopify/Cloudbeds, dan pemberitahuan WhatsApp eksklusif.



![Comparaison plans Freemium et Business](assets/fr/21.webp)



## Manfaat dan kendala



### Sorotan



** Kustodian mandiri**: Anda menyimpan kunci pribadi Anda dan memiliki kendali penuh atas dana Anda. Tidak ada risiko pembekuan akun atau kebangkrutan platform pihak ketiga.



**Kesederhanaan**: Lightning Address sebagai alamat email, pembayaran NFC dengan ketukan sederhana, antarmuka yang intuitif tanpa memerlukan keahlian teknis.



**Ekosistem yang lengkap**: Alat untuk semua profil (individu, peritel, pengembang) dengan integrasi modular yang sesuai dengan kebutuhan Anda.



**Kepatuhan profesional**: Hosting awan yang aman, kepatuhan PCI-DSS, kepatuhan terhadap peraturan Salvador.



### Keterbatasan



**Kendala petir**: Membutuhkan koneksi wallet permanen, manajemen likuiditas untuk volume besar, risiko kegagalan jika penerima offline. Tiankii memitigasi aspek-aspek ini dengan LSP terintegrasi.



**Ketergantungan pada SaaS**: Jika Tiankii tidak tersedia, pembuatan faktur untuk sementara tidak dapat dilakukan (dana Anda tetap aman).



**Kerahasiaan**: Tiankii dapat mengamati metadata transaksi (jumlah, tanggal). Kurang privat dibandingkan solusi yang dihosting sendiri seperti BTCPay Server.



## Kesimpulan



Tiankii mengilustrasikan bagaimana infrastruktur yang dirancang dengan baik dapat menghilangkan hambatan teknis yang mencegah adopsi massal Bitcoin sebagai mata uang sehari-hari. Dengan menggabungkan kekuatan Lightning Network dengan pendekatan non-kustodian dan alat yang dapat diakses, ekosistem ini menawarkan jalur yang seimbang antara kedaulatan keuangan dan kemudahan penggunaan.



Bagi para pedagang, Tiankii mewakili peluang untuk mengurangi biaya transaksi secara drastis sambil mengakses basis pelanggan baru. Bagi konsumen, kartu Lightning Address dan NFC mengubah Bitcoin menjadi mata uang yang praktis, tanpa kerumitan teknis.



Meskipun adopsi Bitcoin secara luas masih menjadi tantangan yang membutuhkan edukasi dan waktu, infrastruktur seperti Tiankii menunjukkan bahwa perangkat teknisnya sudah ada. Misi menyederhanakan pembayaran Bitcoin tidak lagi menjadi visi yang jauh, tetapi menjadi kenyataan yang dapat diakses oleh siapa pun yang mau mengambil risiko.



## Sumber daya



### Dokumentasi resmi




- [Situs web resmi Tiankii](https://tiankii.com)
- [Pusat Bantuan Tiankii](https://help.tiankii.com)
- [Aplikasi IBI](https://go.ibi.me)
- [Dasbor Pedagang](https://pay.tiankii.com)
- [Pusat Komando](https://cc.ibi.me)



### Panduan koneksi Wallet




- [Hubungkan LNbits](https://help.tiankii.com/portal/en/kb/articles/connect-your-lnbits-wallet)
- [Hubungkan BlueWallet (LNDHub)](https://help.tiankii.com/portal/en/kb/articles/connect-your-lndhub-bluewallet)
- [Hubungkan Alby Wallet](https://help.tiankii.com/portal/en/kb/articles/connect-your-alby-wallet)
- [Connect Strike Wallet](https://help.tiankii.com/portal/es/kb/articles/como-vincular-strike-wallet)



### Komunitas




- [Lightning Network Plus](https://lightningnetwork.plus) - Sumber daya pendidikan Lightning
- [Pantai Bitcoin](https://www.bitcoinbeach.com) - Inisiatif ekonomi sirkular Salvador Bitcoin



### Alat-alat terkait




- [Blink Wallet](https://blink.sv) - Direkomendasikan kompatibel dengan Wallet Lightning
- [LNbits](https://lnbits.com) - Solusi wallet yang dihosting sendiri
- [Kartu Bolt Standar](https://github.com/boltcard) - Spesifikasi teknis untuk kartu NFC