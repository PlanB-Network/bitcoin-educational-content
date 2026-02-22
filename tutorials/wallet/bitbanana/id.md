---
name: BitBanana
description: Manajer seluler untuk node Lightning kamu
---

![cover](assets/cover.webp)



Dalam tutorial ini, kamu akan mempelajari cara menginstal dan mengonfigurasi BitBanana di Android untuk mengontrol node Lightning kamu dari ponsel cerdas. Kita akan melihat cara menghubungkan aplikasi ke infrastruktur yang sudah kamu miliki (Umbrel, RaspiBlitz, myNode, atau node LND atau Core Lightning apa pun), melakukan pembayaran Lightning, mengelola channel kamu dari jarak jauh, melihat pendapatan routing, dan mencadangkan konfigurasi kamu. Kamu juga akan belajar tentang praktik keamanan terbaik untuk melindungi akses ke node kamu, serta bagaimana perbandingannya dengan Zeus, sebuah alternatif yang populer.



## Memperkenalkan BitBanana

BitBanana adalah aplikasi mobile Android open source yang mengubah ponsel kamu menjadi dashboard lengkap untuk kendali jarak jauh node Lightning kamu. Berbeda dengan dompet Lightning yang menyematkan node lokal di ponsel, BitBanana mengadopsi filosofi kendali jarak jauh 100%: aplikasi ini tidak menyimpan satoshi dan hanya terhubung ke infrastruktur yang sudah ada.



Dikembangkan oleh Michael Wünsch di bawah lisensi MIT, aplikasi ini menjamin transparansi penuh tanpa pengumpulan data pribadi serta build yang dapat direproduksi dan diverifikasi. BitBanana secara native mendukung LND dan Core Lightning melalui URI standar (`lndconnect://` dan `clngrpc://`), yang secara signifikan menyederhanakan konfigurasi awal. Aplikasi ini juga mengenali LndHub dan Nostr Wallet Connect untuk pengguna tanpa node pribadi, meskipun mode ini berjalan secara kustodian dengan fungsionalitas yang terbatas.



Antarmukanya memberikan akses penuh ke semua fungsi penting node kamu: mengirim dan menerima pembayaran (BOLT11, Lightning Address, LNURL, BOLT12, Keysend), manajemen channel Lightning (pembukaan, penutupan, penyesuaian biaya, penyeimbangan ulang), kontrol koin tingkat lanjut, dan manajemen watchtower. BitBanana juga mengimplementasikan beberapa lapisan keamanan yang kuat: penguncian biometrik, mode siluman, PIN darurat, serta dukungan Tor native untuk menganonimkan koneksi.




## Platform dan pemasangan yang didukung



### Instalasi



BitBanana tersedia secara eksklusif untuk Android 8.0 atau versi yang lebih tinggi. Aplikasi ini tidak tersedia di iOS, dan tidak ada versi yang direncanakan. Keterbatasan ini dapat dijelaskan dari sejarah proyeknya: BitBanana adalah penerus langsung dari Zap Android, yang awalnya dikembangkan oleh Michael Wünsch, lalu dilanjutkan secara independen dengan merek sendiri. Zap sendiri merupakan keluarga aplikasi yang terpisah (Zap Android, Zap iOS, Zap Desktop) yang dikembangkan oleh kontributor berbeda dengan basis kode yang juga terpisah. BitBanana hanya melanjutkan pengembangan pada cabang Android.



Selain itu, ekosistem iOS menghadirkan kendala regulasi dan teknis yang signifikan untuk aplikasi Lightning non-kustodian. Pada tahun 2023, Apple menolak pembaruan Zeus dengan alasan "pelanggaran lisensi", dan pada tahun 2024, Phoenix Wallet meninggalkan App Store AS karena ketidakpastian regulasi terkait penyedia layanan Lightning. Hambatan-hambatan ini menjelaskan mengapa banyak pengembang Lightning lebih memilih Android, yang menawarkan kebijakan lebih terbuka untuk aplikasi non-kustodian.



Tersedia tiga metode instalasi di Android: Google Play Store (5000+ instalasi, pembaruan otomatis), F-Droid (build yang dapat direproduksi, verifikasi kode sumber), atau APK manual yang diunduh langsung dari GitHub.



![BitBanana](assets/fr/01.webp)



Situs web resmi bitbanana.app (kiri) menonjolkan klaim "100% Kustodian Mandiri dengan pengumpulan data NOL". Layar di tengah menampilkan tiga opsi unduhan: F-Droid (direkomendasikan), Google Play, dan APK. Layar di sebelah kanan memperlihatkan permintaan izin notifikasi untuk peringatan pembayaran.



Aplikasi ini meminta beberapa izin: jaringan (koneksi node), kamera (kode QR), NFC (LNURL), layanan latar belakang (notifikasi), biometrik (keamanan), dan WireGuard VPN. Tanpa pelacak dan tanpa pengumpulan data. Aktifkan kata sandi atau penguncian biometrik untuk mengamankan akses.



## Konfigurasi awal



### Menghubungkan ke node LND



Untuk menghubungkan BitBanana ke node LND (Umbrel, RaspiBlitz, myNode), dapatkan URI `lndconnect` atau kode QR yang berisi alamat, sertifikat TLS, dan makaroni otentikasi.



Untuk tutorial ini, kami menggunakan node LND melalui umbrel. Untuk lebih jelasnya, silakan lihat tutorial khusus kami:



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)



Pada aplikasi Lightning Node, akses menu di kanan atas dan pilih "Hubungkan wallet".



![BitBanana](assets/fr/04.webp)



Pilih **gRPC (Tor)** untuk menyambung melalui Tor (disarankan). Kode QR dan detail (Host .onion, Port 10009, Macaroon) ditampilkan.



![BitBanana](assets/fr/02.webp)



Di BitBanana, tekan "HUBUNGKAN NODE", pindai kode QR atau tempelkan URI. Otorisasi akses kamera, lalu periksa alamat .onion yang ditampilkan sebelum mengonfirmasi.



*koneksi *Core Lightning**

Jika kamu menggunakan Core Lightning (CLN) dan bukan LND, prosesnya tetap sama, dengan URI `clngrpc://` yang berisi sertifikat TLS bersama. Core Lightning secara native mendukung BOLT12 (penawaran), yang memungkinkan invoice yang dapat digunakan kembali serta pembayaran berulang yang tidak tersedia di LND.



**Koneksi tanpa node pribadi (LNbits atau hosted)**



Jika kamu tidak memiliki node Lightning, BitBanana dapat terhubung ke layanan yang dihosting melalui LndHub (protokol yang digunakan oleh BlueWallet dan LNbits) atau Nostr Wallet Connect (NWC). Perlu diperhatikan: mode-mode ini berjalan secara kustodian, artinya layanan menyimpan dana kamu, dengan fungsionalitas yang terbatas. Kamu tidak akan dapat mengelola channel atau mengonfigurasi biaya routing, dan hanya bisa mengirim serta menerima pembayaran Lightning.


Untuk detail lebih lanjut tentang LNbits atau Nostr Wallet Connect, silakan baca berbagai tutorial kami:



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Penggunaan sehari-hari



### Interface utama



Layar beranda menampilkan saldo Lightning kamu, dengan menu di kiri atas yang memberikan akses ke bagian berikut: Channel, Routing, Tanda tangani atau Verifikasi, Node, Kontak, Pengaturan, dan Cadangan. Ikon jam di kanan atas membuka riwayat transaksi. Tombol "Kirim" dan "Terima" di bagian bawah memungkinkan kamu untuk mengirim dan menerima satoshi.



![BitBanana](assets/fr/05.webp)



### Pembayaran Lightning dan on-chain



![BitBanana](assets/fr/10.webp)


**Mengirim pembayaran:** Tekan tombol "Kirim" dari layar beranda. Layar pembayaran (kiri) memungkinkan kamu menempelkan alamat atau data pembayaran ke dalam kolom "Address atau data pembayaran", dengan pemindai QR di kanan atas untuk memindai kode. Kamu juga bisa memilih kontak yang tersimpan di bagian Kontak agar tidak perlu memindai setiap kali.



BitBanana secara cerdas mengenali semua format pembayaran: invoice Lightning klasik (string karakter yang dimulai dengan `lnbc`), Lightning Address (format mirip email seperti `user@domain.com`), kode LNURL-pay untuk pembayaran dinamis, LNURL-withdraw untuk menarik dana, serta pembayaran Keysend langsung ke public key Lightning tanpa invoice sebelumnya. Aplikasi ini secara otomatis melakukan resolusi LNURL yang diperlukan di latar belakang.



Setelah invoice dimuat, BitBanana akan menampilkan detail lengkap: jumlah yang tepat, perkiraan biaya routing, deskripsi pembayaran (jika disediakan oleh penerima), dan tanggal kedaluwarsa invoice. Setelah dikonfirmasi, pembayaran akan dirutekan melalui channel Lightning kamu. Kamu kemudian dapat melihat rute yang dilalui langkah demi langkah serta biaya aktual yang dibayarkan di detail transaksi.



**Menerima pembayaran:** Tekan tombol "Terima". Sebuah pemilih (layar kanan) memungkinkan kamu memilih antara Lightning (pembayaran instan melalui channel kamu) dan On-Chain. Untuk tanda terima Lightning, masukkan jumlah yang diinginkan dalam satoshi, atau biarkan bernilai 0 untuk membuat invoice tanpa jumlah tetap yang dapat diisi oleh pembayar, lalu tambahkan deskripsi opsional yang akan ditampilkan pada invoice. BitBanana akan langsung membuat invoice Lightning lengkap dengan kode QR untuk dipindai. Kamu juga dapat menyalin invoice dalam bentuk teks dan mengirimkannya melalui email. Begitu pembayaran diterima, notifikasi push akan memberi tahu kamu dan transaksi akan langsung muncul di riwayat dengan seluruh detailnya.




### Saluran dan perutean



![BitBanana](assets/fr/06.webp)



Bagian "Channel" menampilkan kemampuan kirim dan terima kamu serta daftar channel dengan avatar unik. Setiap channel menunjukkan pembagian likuiditas antara saldo lokal dan remote. Sentuh sebuah channel untuk melihat detail lengkap serta tindakan yang tersedia, seperti menutup channel atau mengubah biaya routing. Ikon tiga titik di kanan atas memberikan akses ke opsi "Rebalance" untuk menyeimbangkan kembali likuiditas channel kamu. Tombol "+" digunakan untuk membuka channel baru.



Bagian Routing (layar tengah) menampilkan pendapatan forwarding berdasarkan periode waktu (1D, 1W, 1M, 3M, 6M, 1Y), lengkap dengan riwayat forwarding yang detail untuk membantu kamu mengoptimalkan strategi routing.



Sign atau Verify (layar kanan) memungkinkan kamu menandatangani atau memverifikasi pesan secara kriptografis untuk membuktikan bahwa kamu mengontrol node tersebut.




### Multi-node dan parameter



![BitBanana](assets/fr/07.webp)



**Manage Nodes**: daftar node kamu, dengan tombol untuk menambahkan secara manual, memindai QR, atau beralih di antara node. Secara khusus, kamu dapat mengatur berbagai jenis koneksi ke node yang sama: LAN, VPN atau Tor.



**Kelola Kontak**: menyimpan kontak Lightning kamu untuk pembayaran cepat.



**Pengaturan**: menyesuaikan mata uang, bahasa, avatar. Bagian Keamanan & Privasi: Kunci Aplikasi (PIN/biometrik), Sembunyikan saldo (mode siluman), Tor (anonimisasi IP). Konfigurasi peramal harga, penjelajah blok, estimator biaya khusus.



## Keuntungan dan keterbatasan



**Sorotan:**




- Mobilitas total: kendalikan simpul Lightning kamu dari mana saja
- Fungsionalitas penuh: pembayaran (LNURL, Lightning Address, BOLT 12), manajemen saluran, kontrol koin, menara pengawas, multi-simpul
- Keamanan PIN/biometrik, mode siluman, PIN Darurat, Tor asli, pemblokiran tangkapan layar
- Gratis, sumber terbuka (MIT), tanpa komisi, tanpa pengumpulan data



**Keterbatasan:**




- Membutuhkan simpul Lightning yang aktif (atau LNbits dalam mode kustodian)
- Tidak ada versi iOS yang direncanakan
- Mengamankan akses ke telepon sangat penting (admin macaroon = akses total ke node)



## Praktik terbaik



**Keamanan:**




- Aktifkan PIN/kunci biometrik (mencegah akses tidak sah ke node)
- Mengatur PIN Darurat (menghapus data sensitif jika terjadi pemaksaan)
- Jangan pernah membagikan URI atau maket login kamu
- Mode siluman di lingkungan yang tidak bersahabat



**Login:**




- VPN mesh (Tailscale, ZeroTier): kompromi terbaik antara kecepatan dan keamanan
- Tor: kerahasiaan maksimum, latensi yang lebih tinggi
- Clearnet: hindari kecuali jika diperlukan (paparan IP, port terbuka)



### Pencadangan dan pemulihan



Terakhir, ada menu "Backup", yang memungkinkan kamu menyimpan konfigurasi untuk migrasi telepon atau instalasi ulang.



![BitBanana](assets/fr/08.webp)



**Penting:** Cadangan TIDAK berisi seed atau cadangan saluran (yang akan dilakukan pada node). Cadangan ini berisi: konfigurasi node (alamat, sertifikat, maket), label, kontak, parameter. Tombol Pulihkan memungkinkan kamu untuk mengimpor cadangan yang ada. Konfirmasi diperlukan sebelum menyimpan.



![BitBanana](assets/fr/09.webp)



Masukkan kata sandi enkripsi (layar kanan). Sistem akan membuka pemilih file (layar kiri) untuk menyimpan `BitBananaBackup_2025-XX-XX.dat`. Konfirmasi "Cadangan dibuat".



**Keamanan:** Simpan cadangan dalam keadaan terenkripsi (cloud pribadi, USB, NAS). Jangan pernah berbagi file atau kata sandi. Uji pemulihan secara teratur. Cadangan memulihkan koneksi, bukan dana.



## BitBanana vs Zeus: Apa perbedaannya?



Jika kamu sedang menjelajahi aplikasi mobile untuk mengelola node Lightning, kamu mungkin akan menemukan Zeus, sebuah alternatif populer dari BitBanana. Berbeda dengan BitBanana yang fokus sepenuhnya pada kendali jarak jauh node yang sudah ada, Zeus mengambil pendekatan yang lebih menyeluruh dengan menawarkan dua mode operasi: node Lightning yang tertanam langsung di aplikasi (mode embedded dengan LND terintegrasi) serta koneksi jarak jauh ke node eksternal, seperti yang dilakukan BitBanana.



Pendekatan ganda ini membuat Zeus sangat menarik bagi pemula yang ingin mencoba Lightning tanpa perlu menyiapkan infrastruktur terlebih dahulu. Mode embedded memungkinkan kamu langsung memulai dengan node mobile yang lengkap, sementara pengguna yang lebih berpengalaman dapat beralih ke koneksi jarak jauh setelah node pribadi mereka siap. Zeus juga mendukung LND dan Core Lightning untuk koneksi jarak jauh, sama seperti BitBanana.



Keunggulan lain dari Zeus adalah ketersediaannya lintas platform di iOS dan Android, sementara BitBanana tetap eksklusif di Android. Zeus juga mengintegrasikan infrastruktur LSP Olympus untuk mempermudah penerimaan pembayaran Lightning melalui channel just-in-time, menyediakan sistem Point of Sale untuk pedagang, serta fitur swap terintegrasi untuk pengelolaan likuiditas.



Namun, BitBanana tetap memiliki keunggulan tersendiri: antarmuka yang lebih sederhana dan ringan, pengalaman pengguna yang lebih nyaman berkat fokus eksklusif pada kendali jarak jauh, serta pendekatan edukatif melalui penjelasan kontekstual. Zeus memang menawarkan lebih banyak fitur, tetapi dengan konsekuensi antarmuka yang lebih kompleks. BitBanana tetap sangat cocok untuk kamu yang ingin mengontrol node secara murni dari jarak jauh, tanpa fungsi kustodian.




Untuk mengetahui lebih lanjut tentang Zeus, lihat tutorial berikut ini:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## Kesimpulan


BitBanana mengubah ponsel pintar Android kamu menjadi dashboard Lightning yang lengkap, menghadirkan mobilitas yang belum pernah ada sebelumnya bagi operator node. Aplikasi ini mencakup semua fungsi penting: pembayaran dalam semua format, manajemen channel, kontrol koin, watchtower, dukungan multi-node, serta keamanan yang ditingkatkan melalui PIN atau biometrik, Tor, dan PIN Darurat.



Sepenuhnya berdaulat, BitBanana tidak mengumpulkan data dan tidak mengorbankan privasi maupun kendali atas dana kamu. Kode sumbernya yang open source di bawah lisensi MIT menjamin transparansi penuh.




## Sumber 



### Dokumentasi resmi




- [Situs web BitBanana](https://bitbanana.app)
- [Dokumentasi lengkap](https://docs.bitbanana.app)
- [Kode sumber GitHub](https://github.com/michaelWuensch/BitBanana)



### Instalasi




- [Google Play Store](https://play.google.com/store/apps/details?id=app.michaelwuensch.bitbanana)
- [F-Cold](https://f-droid.org/packages/app.michaelwuensch.bitbanana)
