---
name: BTCPay Server - Umbrel
description: Menginstal dan menggunakan Server BTCPay di Umbrel untuk menerima Bitcoin dan Lightning
---

![cover](assets/cover.webp)



Dalam ekosistem Bitcoin, menerima pembayaran merupakan tantangan besar bagi pedagang dan bisnis. Solusi tradisional, baik perbankan (kartu kredit, Stripe, PayPal) atau bahkan Bitcoin (BitPay, Coinbase Commerce), membebankan perantara yang memungut biaya yang cukup besar, mengumpulkan data bisnis Anda yang sensitif, dan dapat memblokir atau menyensor transaksi Anda sesuka hati. Ketergantungan ini bertentangan dengan prinsip-prinsip fundamental Bitcoin tentang desentralisasi, kerahasiaan, dan kedaulatan keuangan.



BTCPay Server muncul sebagai jawaban sumber terbuka untuk masalah ini. Pemroses pembayaran yang dihosting sendiri ini mengubah node Bitcoin Anda sendiri menjadi infrastruktur profesional, tanpa perantara, tanpa biaya pemrosesan tambahan, dan tanpa kompromi pada privasi. Dikembangkan oleh komunitas kontributor global sejak tahun 2017, BTCPay Server memungkinkan Anda untuk menerima pembayaran Bitcoin dan Lightning langsung ke dompet Anda, dengan tetap memegang kendali penuh atas dana Anda setiap saat.



Biasanya, menginstal BTCPay Server membutuhkan keterampilan teknis tingkat lanjut: Konfigurasi server Linux, penguasaan Docker, manajemen sertifikat SSL, dan keamanan jaringan. Umbrel merevolusi pendekatan ini dengan instalasi satu klik yang terintegrasi langsung dengan Bitcoin dan Lightning node Anda. Penyederhanaan ini membuat apa yang sebelumnya hanya diperuntukkan bagi teknisi berpengalaman menjadi dapat diakses oleh semua orang.



**Penting untuk dipahami**: Server BTCPay di Umbrel bekerja secara default hanya di jaringan lokal Anda. Anda bisa membuat faktur, menerima pembayaran Lightning dan Bitcoin, dan mengelola akuntansi Anda dari perangkat apa pun yang terhubung ke jaringan rumah Anda (komputer, ponsel cerdas, tablet). Konfigurasi ini sangat ideal untuk menagih layanan tatap muka, mengelola pembayaran tatap muka, atau menggunakan BTCPay Server dari jaringan lokal Anda. Di sisi lain, untuk mengintegrasikan BTCPay Server ke dalam toko online yang dapat diakses publik di Internet, diperlukan konfigurasi tambahan dengan paparan publik (kami akan membahas masalah ini di akhir tutorial).



Tutorial ini akan memandu Anda melalui instalasi lengkap BTCPay Server di Umbrel, mengonfigurasi node Bitcoin wallet dan Lightning Anda, membuat dan membayar faktur, dan mengelola pelaporan akuntansi. Anda akan menemukan cara menggunakan BTCPay Server secara efisien di jaringan lokal Anda, dan kemudian kita akan melihat solusi untuk tampilan publik jika Anda ingin mengintegrasikannya dengan situs e-commerce.



## Prasyarat



Untuk mengikuti tutorial ini, Anda harus sudah menginstal dan mengkonfigurasi Umbrel dengan benar. Jika Anda belum melakukannya, silakan lihat tutorial kami tentang instalasi Umbrel.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Node Bitcoin Core Anda harus sepenuhnya tersinkronisasi dengan blockchain (100% dalam aplikasi Bitcoin Umbrel). Sinkronisasi awal ini biasanya memakan waktu antara 3 hari dan 2 minggu, tergantung pada perangkat keras dan koneksi internet Anda.



Untuk menerima pembayaran Lightning instan, Anda juga harus menginstal LND (Lightning Network Daemon) di Umbrel. Lihat tutorial kami tentang cara memasang dan mengonfigurasi LND di Umbrel jika Anda ingin mengaktifkan fitur ini.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Sediakan setidaknya 50 GB ruang disk kosong untuk BTCPay Server, basis data dan data Lightning. Koneksi Internet yang stabil melalui kabel Ethernet sangat disarankan untuk menghindari terputusnya koneksi.



## Menginstal Server BTCPay di Umbrel



Dari antarmuka Umbrel (`umbrel.local`), akses App Store dan cari "BTCPay Server" dalam kategori Bitcoin.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Klik Instal. Umbrel secara otomatis memeriksa apakah Bitcoin Core dan LND sudah terpasang, lalu memulai pemasangan (2-5 menit).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Setelah terinstal, buka aplikasinya. Anda harus membuat akun administrator dengan kredensial yang kuat.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Setelah akun Anda dibuat, BTCPay Server akan segera meminta Anda untuk menyiapkan toko pertama Anda. Pilih nama bisnis dan pilih mata uang referensi (EUR, USD, atau BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Mengakses Server BTCPay di jaringan lokal Anda



BTCPay Server dapat diakses dari perangkat apa pun di jaringan lokal Anda (WiFi atau Ethernet). Akses dari browser Anda ke :



```url
http://umbrel.local
```



Atau langsung ke :



```url
http://umbrel.local:3003
```



**Akses jarak jauh dengan Tailscale**: Untuk mengakses Server BTCPay dari mana saja di seluruh dunia, gunakan Tailscale. VPN aman ini memungkinkan Anda terhubung ke Umbrel seolah-olah Anda berada di jaringan lokal. Lihat tutorial kami yang didedikasikan untuk Tailscale di Umbrel.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Mengkonfigurasi portofolio Bitcoin Anda



Untuk menerima pembayaran, Anda perlu mengonfigurasi Bitcoin wallet. Server BTCPay menampilkan opsi konfigurasi di dasbor.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Untuk mengonfigurasi wallet Bitcoin, buka "Dompet" > "Bitcoin".



Anda memiliki dua opsi: membuat portofolio baru secara langsung di BTCPay, atau mengimpor portofolio yang sudah ada. Untuk mengimpor, ada beberapa metode yang tersedia:




- Hubungkan perangkat keras wallet** (disarankan): Mengimpor kunci publik Anda melalui aplikasi Vault
- Impor file wallet** (disarankan): Unggah file yang diekspor dari portofolio Anda
- Masukkan kunci publik yang diperpanjang**: Masukkan XPub/YPub/ZPub Anda secara manual
- Pindai kode QR wallet**: Pindai kode QR dari BlueWallet, Cobo Vault, Passport atau Specter DIY
- Masukkan wallet seed** (tidak disarankan): Masukkan frasa pemulihan 12 atau 24 kata Anda



![Options de création de portefeuille](assets/fr/06.webp)



Untuk tutorial ini, kita akan membuat Hot wallet yang baru: kunci pribadi akan disimpan di server Umbrel kita. Dalam kasus ini, kami sangat menyarankan Anda untuk memindahkan dana secara teratur ke wallet yang dingin untuk menghindari penyimpanan dalam jumlah besar di server.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Setelah dikonfigurasi, BTCPay Server akan mengonfirmasi bahwa wallet Anda siap menerima pembayaran on-chain.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Aktifkan Lightning Network



Untuk menerima pembayaran Lightning instan, buka Dompet > Lightning. Kemudian, karena node LND Anda sudah terpasang di Umbrel, cukup klik tombol "Simpan" untuk memvalidasi koneksi antara Server BTCPay dan node Lightning Anda.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Membuat dan membayar faktur



Pada antarmuka Server BTCPay, buka Faktur > Buat Invoice. Masukkan jumlah tagihan, tambahkan deskripsi opsional, dan klik Buat.



![Création d'une nouvelle facture](assets/fr/10.webp)



Anda kemudian dapat mengklik tombol "Checkout" untuk menampilkan faktur. BTCPay kemudian membuat faktur dengan kode QR terpadu (BIP21) yang berisi alamat Bitcoin dan faktur Lightning.



![Détails de la facture générée](assets/fr/11.webp)



Pelanggan Anda dapat memindai kode QR dengan wallet yang kompatibel.



![Page de paiement avec QR code](assets/fr/12.webp)



Setelah dibayar, faktur akan menjadi "Lunas" dalam hitungan detik untuk Lightning.



![Confirmation de paiement réussi](assets/fr/13.webp)



## Manajemen dan pelacakan pembayaran



Pada bagian "Pelaporan", tab "Faktur", Anda akan menemukan riwayat lengkap faktur Anda dengan tanggal, jumlah, status, dan metode pembayaran. Anda dapat mengekspornya jika diperlukan.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Konfigurasi penyimpanan



BTCPay Server memungkinkan Anda untuk mengelola beberapa toko dengan parameter yang berbeda. Setiap toko mewakili entitas bisnis yang terpisah: toko e-commerce, tempat penjualan fisik, atau penagihan layanan.



Dalam pengaturan toko, Anda akan menemukan beberapa bagian penting:



![Paramètres du magasin](assets/fr/15.webp)





- Pengaturan Umum**: Nama toko, mata uang referensi (BTC, EUR, USD), waktu kedaluwarsa faktur (default 15 menit), jumlah konfirmasi blockchain yang diperlukan
- Kurs**: Konfigurasi sumber nilai tukar dan konversi fiat/Bitcoin
- Tampilan Checkout**: Sesuaikan tampilan halaman checkout Anda (logo, warna, pesan yang dipersonalisasi)
- Pengaturan Email**: Konfigurasi pemberitahuan email untuk pembayaran yang diterima
- Akses Token**: Manajemen token API untuk integrasi e-commerce (WooCommerce, Shopify, dll.)
- Pengguna**: Mengelola akses pengguna ke toko dengan berbagai tingkat izin (Pemilik, Tamu)
- Webhook**: Konfigurasi Webhook untuk sinkronisasi waktu nyata dengan sistem akuntansi atau ERP Anda



BTCPay Server juga menawarkan bagian Plugin untuk memperluas fungsionalitas dengan integrasi e-commerce, sistem tempat penjualan, dan alat tambahan.



![Gestion des plugins](assets/fr/16.webp)



## Keuntungan dan keterbatasan penggunaan lokal



**Keunggulan Server BTCPay dibandingkan Umbrel**:




- Kedaulatan total: kontrol eksklusif atas kunci dan dana pribadi, tidak ada pihak ketiga yang dapat membekukan atau menyensor pembayaran Anda
- Penghematan substansial: hanya biaya jaringan Bitcoin (beberapa sen pada Lightning) vs. 2-3% pada prosesor tradisional
- Kerahasiaan maksimum: tidak ada pendaftaran, verifikasi identitas, atau berbagi data dengan perusahaan pihak ketiga
- Arsitektur sumber terbuka menjamin transparansi, kemampuan audit, dan keberlanjutan melalui komunitas pengembang yang besar
- Pemasangan yang mudah melalui Umbrel, tanpa perlu keahlian teknis tingkat lanjut



**Keterbatasan penting**:




- Hanya untuk jaringan lokal**: Server BTCPay di Umbrel hanya dapat diakses dari jaringan rumah Anda. Sempurna untuk penagihan tatap muka, layanan freelance, atau bisnis fisik kecil, tetapi tidak cocok untuk toko online yang dapat diakses publik.
- Tanggung jawab teknis penuh: pemeliharaan node, pencadangan rutin, pemantauan konektivitas
- Manajemen likuiditas kilat: membuka dan mengelola saluran dengan kapasitas masuk yang memadai
- Dukungan terbatas pada dokumentasi dan forum komunitas, yang membutuhkan lebih banyak otonomi daripada departemen layanan pelanggan komersial



Keterbatasan jaringan lokal ini merupakan kendala utama untuk mengintegrasikan BTCPay Server ke dalam toko e-commerce, di mana pelanggan harus dapat mengakses halaman pembayaran dari mana saja di Internet.



## Praktik terbaik dan keamanan



Aktifkan cadangan Umbrel otomatis dan simpan salinannya di media eksternal (stik USB, hard disk, cloud terenkripsi). Simpan benih Bitcoin (frasa pemulihan) di tempat yang aman dan terpisah secara fisik. Cadangkan file channel.backup LND untuk pemulihan Lightning.



Memantau sinkronisasi Bitcoin Core, saluran Lightning, dan respons Server BTCPay secara teratur. Tes mingguan sederhana: generate dan membayar tagihan untuk beberapa satoshi. Selalu perbarui Umbrel (patch keamanan, peningkatan). Buatlah cadangan sebelum pembaruan besar. Untuk penggunaan profesional, pertimbangkan pemantauan eksternal (UptimeRobot) dengan peringatan email/SMS.



## Mengekspos Server BTCPay secara publik untuk toko online



Untuk mengintegrasikan BTCPay Server ke dalam toko e-commerce berbasis web (WooCommerce, Shopify, dll.), pelanggan Anda harus dapat mengakses halaman pembayaran dari mana saja, bukan hanya jaringan lokal Anda.



**Solusi: Manajer Proksi Nginx**



Anda dapat mengekspos BTCPay Server secara publik menggunakan Nginx Proxy Manager (tersedia di Umbrel App Store). Solusi ini membutuhkan file :




- Nama domain (klasik atau gratis melalui DuckDNS, No-IP, Afraid.org)
- Mengkonfigurasi penerusan port (port 80 dan 443) pada router Anda
- Pemasangan Nginx Proxy Manager, yang secara otomatis mengelola sertifikat SSL



Konfigurasi ini mengekspos server Anda ke Internet dan membutuhkan kewaspadaan ekstra (kata sandi yang kuat, 2FA, pembaruan rutin). Kami akan menyiapkan tutorial khusus yang merinci prosedur lengkap ini.



## Kesimpulan



BTCPay Server di Umbrel menggabungkan kekuatan node Bitcoin dengan kesederhanaan Umbrel untuk menciptakan infrastruktur pembayaran profesional yang dapat dihosting sendiri yang dapat diakses oleh semua orang. Kedaulatan keuangan ini disertai dengan tanggung jawab pemeliharaan, tetapi Umbrel sangat menyederhanakan beban operasional dibandingkan dengan manfaatnya: penghapusan biaya pemrosesan, perlindungan privasi Anda, resistensi terhadap penyensoran, dan kontrol penuh atas dana Anda.



Penggunaan jaringan lokal sudah mencakup berbagai macam aplikasi: penagihan untuk layanan lepas, pembayaran secara langsung, toko fisik kecil, atau sekadar belajar dan bereksperimen dengan Bitcoin dan Lightning dalam lingkungan yang terkendali. Untuk kebutuhan e-commerce yang membutuhkan eksposur publik, solusi Nginx Proxy Manager tersedia, tetapi membutuhkan konfigurasi teknis tambahan, yang akan kami jelaskan secara rinci dalam tutorial khusus.



Baik Anda menjalankan bisnis, proyek yang masih baru, atau sekadar bereksperimen, BTCPay Server di Umbrel menawarkan otonomi keuangan yang lengkap. Jalannya dimulai dengan toko pertama Anda, faktur pertama Anda, pembayaran pertama Anda yang diterima langsung ke infrastruktur berdaulat Anda.



## Sumber daya



### Dokumentasi resmi




- [Situs web Server BTCPay Resmi](https://btcpayserver.org)
- [Dokumentasi Server BTCPay lengkap](https://docs.btcpayserver.org)
- [GitHub BTCPay Server](https://github.com/btcpayserver/btcpayserver)
- [Dokumentasi skala ekor](https://tailscale.com/kb)


### Komunitas dan dukungan




- [Forum BTCPay Server](https://chat.btcpayserver.org)
- [Forum Umbrel](https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)