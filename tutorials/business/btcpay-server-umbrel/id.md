---
name: BTCPAY SERVER - Payung
description: Memasang dan menggunakan BTCPAY SERVER pada Umbrel untuk menerima Bitcoin dan Lightning
---

![cover](assets/cover.webp)



Dalam ekosistem Bitcoin, menerima pembayaran merupakan tantangan besar bagi pedagang dan bisnis. Solusi tradisional, baik perbankan (kartu kredit, Stripe, PayPal) atau bahkan Bitcoin (BitPay, Coinbase Commerce), membebankan perantara yang memungut biaya yang cukup besar, mengumpulkan data bisnis Anda yang sensitif, dan dapat melakukan BLOCK atau menyensor transaksi Anda sesuka hati. Ketergantungan ini bertentangan dengan prinsip-prinsip fundamental Bitcoin tentang desentralisasi, kerahasiaan, dan kedaulatan keuangan.



BTCPAY SERVER muncul sebagai jawaban sumber terbuka untuk masalah ini. Pemroses pembayaran yang dihosting sendiri ini mengubah node Bitcoin Anda sendiri menjadi infrastruktur profesional, tanpa perantara, tanpa biaya pemrosesan tambahan, dan tanpa kompromi pada privasi. Dikembangkan oleh komunitas kontributor global sejak tahun 2017, BTCPAY SERVER memungkinkan Anda untuk menerima pembayaran Bitcoin dan Lightning langsung ke dompet Anda, dengan tetap memegang kendali penuh atas dana Anda setiap saat.



Secara tradisional, menginstal BTCPAY SERVER membutuhkan keterampilan teknis tingkat lanjut: Konfigurasi server Linux, penguasaan Docker, manajemen sertifikat SSL, dan keamanan jaringan. Umbrel merevolusi pendekatan ini dengan instalasi satu klik yang terintegrasi langsung dengan Bitcoin dan LIGHTNING NODE Anda. Penyederhanaan ini membuat apa yang sebelumnya hanya diperuntukkan bagi teknisi berpengalaman menjadi dapat diakses oleh semua orang.



**Penting untuk dipahami**: BTCPAY SERVER pada Umbrel bekerja secara default hanya pada jaringan lokal Anda. Anda bisa membuat faktur, menerima pembayaran Lightning dan Bitcoin, dan mengelola akuntansi dari perangkat apa pun yang terhubung ke jaringan rumah Anda (komputer, ponsel cerdas, tablet). Konfigurasi ini sangat ideal untuk menagih layanan tatap muka, mengelola pembayaran tatap muka, atau menggunakan BTCPAY SERVER dari jaringan lokal Anda. Di sisi lain, untuk mengintegrasikan BTCPAY SERVER ke dalam toko online yang dapat diakses secara publik di Internet, diperlukan konfigurasi tambahan dengan eksposur publik (kami akan membahas masalah ini di akhir tutorial).



Tutorial ini akan memandu Anda melalui instalasi lengkap BTCPAY SERVER di Umbrel, mengonfigurasi Bitcoin, Wallet, dan LIGHTNING NODE, membuat dan membayar faktur, serta mengelola pelaporan akuntansi. Anda akan mengetahui cara menggunakan BTCPAY SERVER secara efektif di jaringan lokal Anda, dan kemudian kita akan membahas solusi untuk tampilan publik jika Anda ingin mengintegrasikannya dengan situs e-commerce.



## Prasyarat



Untuk mengikuti tutorial ini, Anda harus sudah menginstal dan mengonfigurasi Umbrel dengan benar. Jika Anda belum melakukannya, silakan lihat tutorial kami tentang instalasi Umbrel.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Node Bitcoin core Anda harus disinkronkan sepenuhnya dengan Blockchain (100% dalam aplikasi Bitcoin Umbrel). Sinkronisasi awal ini biasanya memakan waktu antara 3 hari hingga 2 minggu, tergantung pada perangkat keras dan koneksi internet Anda.



Untuk menerima pembayaran Lightning instan, Anda juga harus menginstal LND (Lightning Network Daemon) di Umbrel. Lihat tutorial kami tentang cara memasang dan mengonfigurasi LND di Umbrel jika Anda ingin mengaktifkan fitur ini.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Sediakan setidaknya 50 GB ruang disk kosong untuk BTCPAY SERVER, database, dan data Lightning. Koneksi Internet yang stabil melalui kabel Ethernet sangat disarankan untuk menghindari terputusnya koneksi.



## Memasang BTCPAY SERVER pada Umbrel



Dari Umbrel Interface (`umbrel.local`), buka App Store dan cari "BTCPAY SERVER" di kategori Bitcoin.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Klik Instal. Umbrel secara otomatis memeriksa apakah Bitcoin core dan LND sudah terpasang, lalu memulai penyebaran (2-5 menit).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Setelah terinstal, buka aplikasinya. Anda harus membuat akun administrator dengan kredensial yang kuat.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Setelah akun Anda dibuat, BTCPAY SERVER akan segera meminta Anda untuk menyiapkan toko pertama Anda. Pilih nama profesional dan pilih mata uang referensi (EUR, USD, atau BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Akses BTCPAY SERVER di jaringan lokal Anda



BTCPAY SERVER dapat diakses dari perangkat apa pun di jaringan lokal Anda (WiFi atau Ethernet). Akses dari browser Anda ke :



```url
http://umbrel.local
```



Atau langsung ke :



```url
http://umbrel.local:3003
```



**Akses jarak jauh dengan Tailscale**: Untuk mengakses BTCPAY SERVER dari mana saja di seluruh dunia, gunakan Tailscale. VPN aman ini memungkinkan Anda terhubung ke Umbrel seolah-olah Anda berada di jaringan lokal Anda. Lihat tutorial kami yang didedikasikan untuk Tailscale di Umbrel.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Mengkonfigurasi portofolio Bitcoin Anda



Untuk menerima pembayaran, Anda perlu mengonfigurasi Bitcoin Wallet. BTCPAY SERVER menampilkan opsi konfigurasi di dasbor.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Untuk mengkonfigurasi Wallet Bitcoin, buka "Dompet" > "Bitcoin".



Anda memiliki dua opsi: membuat portofolio baru secara langsung di BTCPay, atau mengimpor portofolio yang sudah ada. Untuk mengimpor, ada beberapa metode yang tersedia:




- Hubungkan Hardware Wallet** (disarankan): Impor kunci publik Anda melalui aplikasi Vault
- Impor file Wallet** (disarankan): Unggah file yang diekspor dari portofolio Anda
- Masukkan kunci publik yang diperpanjang**: Masukkan XPub/YPub/ZPub Anda secara manual
- Pindai kode QR Wallet**: Pindai kode QR dari BlueWallet, Cobo Vault, Passport atau Specter DIY
- Masukkan Wallet seed** (tidak disarankan): Masukkan frasa pemulihan 12 atau 24 kata Anda



![Options de création de portefeuille](assets/fr/06.webp)



Untuk tutorial ini, kita akan membuat Hot Wallet yang baru: kunci privat akan disimpan di server Umbrel. Dalam kasus ini, kami sangat menyarankan Anda untuk memindahkan dana secara teratur ke Cold Wallet untuk menghindari penyimpanan dalam jumlah besar di server.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Setelah dikonfigurasi, BTCPAY SERVER akan mengonfirmasi bahwa Wallet Anda siap menerima pembayaran On-Chain.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Aktifkan Lightning Network



Untuk menerima pembayaran Lightning instan, buka Dompet > Lightning. Kemudian, karena node LND Anda sudah terpasang di Umbrel, cukup klik tombol "Simpan" untuk memvalidasi koneksi antara BTCPAY SERVER dan LIGHTNING NODE Anda.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Membuat dan membayar faktur



Pada Interface BTCPAY SERVER, navigasikan ke Faktur > Buat Invoice. Masukkan jumlah, tambahkan deskripsi opsional, dan klik Buat.



![Création d'une nouvelle facture](assets/fr/10.webp)



Anda kemudian dapat mengklik tombol "Checkout" untuk menampilkan Invoice. BTCPay kemudian menghasilkan Invoice dengan kode QR terpadu (BIP21) yang berisi Bitcoin Address dan Lightning Invoice.



![Détails de la facture générée](assets/fr/11.webp)



Pelanggan Anda dapat memindai kode QR dengan Wallet yang kompatibel.



![Page de paiement avec QR code](assets/fr/12.webp)



Setelah dibayar, Invoice menjadi "Settled" dalam hitungan detik untuk Lightning.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Manajemen dan pelacakan pembayaran



Pada bagian "Pelaporan", tab "Faktur", Anda akan menemukan riwayat lengkap faktur Anda, dengan tanggal, jumlah, status, dan metode pembayaran. Anda dapat mengekspornya jika diperlukan.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Konfigurasi penyimpanan



BTCPAY SERVER memungkinkan Anda mengelola beberapa toko dengan parameter yang berbeda. Setiap toko mewakili entitas bisnis yang terpisah: toko e-commerce, tempat penjualan fisik, atau penagihan layanan.



Dalam pengaturan toko, Anda akan menemukan beberapa bagian penting:



![Paramètres du magasin](assets/fr/15.webp)





- Pengaturan Umum**: Nama toko, mata uang referensi (BTC, EUR, USD), waktu kedaluwarsa Invoice (default 15 menit), jumlah konfirmasi Blockchain yang diperlukan
- Kurs**: Konfigurasi sumber kurs Exchange dan konversi fiat/Bitcoin
- Tampilan Checkout**: Sesuaikan tampilan halaman checkout Anda (logo, warna, pesan yang dipersonalisasi)
- Pengaturan Email**: Konfigurasi pemberitahuan email untuk pembayaran yang diterima
- Akses Token**: API Manajemen token untuk integrasi e-commerce (WooCommerce, Shopify, dll.)
- Pengguna**: Mengelola akses pengguna ke toko dengan berbagai tingkat izin (Pemilik, Tamu)
- Webhook**: Konfigurasi Webhook untuk sinkronisasi waktu nyata dengan sistem akuntansi atau ERP Anda



BTCPAY SERVER juga menawarkan bagian Plugins untuk memperluas fungsionalitas dengan integrasi e-commerce, sistem point-of-sale, dan alat tambahan.



![Gestion des plugins](assets/fr/16.webp)



## Keuntungan dan keterbatasan penggunaan lokal



**Manfaat BTCPAY SERVER pada Umbrel**:




- Kedaulatan total: kontrol eksklusif atas kunci dan dana pribadi, tidak ada pihak ketiga yang dapat membekukan atau menyensor pembayaran Anda
- Penghematan substansial: hanya biaya jaringan Bitcoin (beberapa sen pada Lightning) vs. 2-3% pada prosesor tradisional
- Kerahasiaan maksimum: tidak ada pendaftaran, verifikasi identitas, atau berbagi data dengan perusahaan pihak ketiga
- Arsitektur sumber terbuka menjamin transparansi, kemampuan audit, dan keberlanjutan melalui komunitas pengembang yang besar
- Pemasangan yang mudah melalui Umbrel, tanpa perlu keahlian teknis tingkat lanjut



**Keterbatasan penting**:




- Hanya untuk jaringan lokal**: BTCPAY SERVER pada Umbrel hanya dapat diakses dari jaringan rumah Anda. Sempurna untuk penagihan tatap muka, layanan freelance, atau bisnis fisik kecil, tetapi tidak cocok untuk toko online yang dapat diakses secara publik di Internet.
- Tanggung jawab teknis penuh: pemeliharaan node, pencadangan rutin, pemantauan konektivitas
- Manajemen likuiditas kilat: membuka dan mengelola saluran dengan kapasitas masuk yang memadai
- Dukungan terbatas pada dokumentasi dan forum komunitas, yang membutuhkan lebih banyak otonomi daripada departemen layanan pelanggan komersial



Keterbatasan LAN ini merupakan kendala utama untuk mengintegrasikan BTCPAY SERVER ke dalam toko e-commerce, di mana pelanggan harus dapat mengakses halaman pembayaran dari mana saja di Internet.



## Praktik terbaik dan keamanan



Aktifkan cadangan Umbrel otomatis dan simpan salinannya di media eksternal (stik USB, disk Hard, cloud terenkripsi). Simpan benih Bitcoin (frasa pemulihan) Anda di tempat yang aman dan terpisah secara fisik. Simpan file LND channel.backup untuk pemulihan Lightning.



Memantau sinkronisasi Bitcoin core, saluran petir, dan respons BTCPAY SERVER secara teratur. Tes mingguan sederhana: generate dan membayar tagihan untuk beberapa satoshi. Selalu perbarui Umbrel (patch keamanan, peningkatan). Buatlah cadangan sebelum pembaruan besar. Untuk penggunaan profesional, pertimbangkan pemantauan eksternal (UptimeRobot) dengan peringatan email/SMS.



## Tampilkan BTCPAY SERVER secara publik untuk toko online



Untuk mengintegrasikan BTCPAY SERVER ke dalam toko e-commerce berbasis web (WooCommerce, Shopify, dll.), pelanggan Anda harus dapat mengakses halaman pembayaran dari mana saja, tidak hanya dari jaringan lokal Anda.



**Solusi: Manajer Proksi Nginx**



Anda dapat mengekspos BTCPAY SERVER secara publik menggunakan Nginx Proxy Manager (tersedia di Umbrel App Store). Solusi ini membutuhkan file :




- Nama domain (klasik atau gratis melalui DuckDNS, No-IP, Afraid.org)
- Mengkonfigurasi penerusan port (port 80 dan 443) pada router Anda
- Pemasangan Nginx Proxy Manager, yang secara otomatis mengelola sertifikat SSL



Konfigurasi ini mengekspos server Anda ke Internet dan membutuhkan kewaspadaan ekstra (kata sandi yang kuat, 2FA, pembaruan rutin). Kami akan menyiapkan tutorial khusus yang merinci prosedur lengkap ini.



## Kesimpulan



BTCPAY SERVER pada Umbrel menggabungkan kekuatan node Bitcoin dengan kesederhanaan Umbrel untuk menciptakan infrastruktur pembayaran profesional yang dihosting sendiri yang dapat diakses oleh semua orang. Kedaulatan keuangan ini disertai dengan tanggung jawab pemeliharaan, tetapi Umbrel sangat menyederhanakan beban operasional dibandingkan dengan manfaatnya: penghapusan biaya pemrosesan, perlindungan privasi Anda, resistensi terhadap penyensoran, dan kontrol penuh atas dana Anda.



Penggunaan jaringan lokal sudah mencakup berbagai macam aplikasi: penagihan untuk layanan lepas, pembayaran tatap muka, toko fisik kecil, atau sekadar belajar dan bereksperimen dengan Bitcoin dan Lightning dalam lingkungan yang terkendali. Untuk kebutuhan e-commerce yang membutuhkan eksposur publik, solusi Nginx Proxy Manager tersedia, tetapi membutuhkan konfigurasi teknis tambahan, yang akan kami jelaskan secara rinci dalam tutorial khusus.



Baik Anda menjalankan bisnis, proyek yang masih baru, atau sekadar bereksperimen, BTCPAY SERVER di Umbrel menawarkan otonomi keuangan yang lengkap. Jalurnya dimulai dengan toko pertama, Invoice pertama, pembayaran pertama yang diterima langsung ke infrastruktur berdaulat Anda.



## Sumber daya



### Dokumentasi resmi




- [Situs web resmi BTCPAY SERVER](https://btcpayserver.org)
- [Dokumentasi lengkap BTCPAY SERVER](https://docs.btcpayserver.org)
- [GitHub BTCPAY SERVER](https://github.com/btcpayserver/btcpayserver)
- [Dokumentasi skala ekor](https://tailscale.com/kb)


### Komunitas dan dukungan




- [Forum BTCPAY SERVER] (https://chat.btcpayserver.org)
- [Forum Umbrel](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)