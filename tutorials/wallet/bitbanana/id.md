---
name: BitBanana
description: Manajer seluler untuk simpul Lightning Anda
---

![cover](assets/cover.webp)



Dalam tutorial ini, Anda akan mempelajari cara menginstal dan mengonfigurasi BitBanana di Android untuk mengontrol node Lightning Anda dari ponsel cerdas Anda. Kita akan melihat cara menghubungkan aplikasi ke infrastruktur Anda yang sudah ada (Umbrel, RaspiBlitz, myNode, atau node LND/Core Lightning apa pun), melakukan pembayaran Lightning, mengelola saluran Anda dari jarak jauh, melihat pendapatan perutean, dan mencadangkan konfigurasi Anda. Anda juga akan belajar tentang praktik keamanan terbaik untuk melindungi akses ke node Anda, dan bagaimana perbandingannya dengan Zeus, sebuah alternatif yang populer.



## Memperkenalkan BitBanana



BitBanana adalah sebuah aplikasi mobile Android open source yang mengubah ponsel Anda menjadi sebuah dasbor lengkap untuk kendali jarak jauh dari node Lightning Anda. Tidak seperti dompet Lightning, yang menyematkan node lokal pada ponsel, BitBanana mengadopsi filosofi kendali jarak jauh 100%: aplikasi ini tidak memiliki satoshi dan hanya terhubung ke infrastruktur yang ada.



Dikembangkan oleh Michael Wünsch di bawah lisensi MIT, aplikasi ini menjamin transparansi total tanpa pengumpulan data pribadi dan build yang dapat direproduksi dan diverifikasi. BitBanana secara native mendukung LND dan Core Lightning melalui URI standar (`lndconnect://` dan `clngrpc://`), yang secara drastis menyederhanakan konfigurasi awal. Aplikasi ini juga mengenali LndHub dan Nostr Wallet Connect untuk pengguna tanpa node pribadi, meskipun mode ini beroperasi secara kustodian dengan fungsionalitas yang terbatas.



Antarmuka menawarkan akses penuh ke semua fungsi penting node Anda: mengirim dan menerima pembayaran (BOLT11, Lightning Address, LNURL, BOLT12, Keysend), manajemen saluran Lightning (pembukaan, penutupan, penyesuaian biaya, penyeimbangan kembali), kontrol koin tingkat lanjut, dan manajemen menara pengawas. BitBanana juga mengimplementasikan beberapa lapisan keamanan yang kuat: penguncian biometrik, mode siluman, PIN Darurat, dan dukungan Tor asli untuk menganonimkan koneksi.



## Platform dan pemasangan yang didukung



### Instalasi



BitBanana tersedia secara eksklusif untuk Android 8.0 atau lebih tinggi. Aplikasi ini tidak ada di iOS, dan tidak ada versi yang direncanakan. Keterbatasan ini dijelaskan oleh sejarah proyek ini: BitBanana adalah penerus langsung dari Zap Android, yang awalnya dikembangkan oleh Michael Wünsch, yang memutuskan untuk melanjutkan karyanya dengan mereknya sendiri. Zap adalah sebuah keluarga aplikasi yang terpisah (Zap Android, Zap iOS, Zap Desktop) yang dikembangkan oleh kontributor yang berbeda dengan basis kode yang terpisah. BitBanana hanya mengejar cabang Android.



Selain itu, ekosistem iOS menghadirkan kendala regulasi dan teknis yang signifikan untuk aplikasi Lightning non-kustodian. Pada tahun 2023, Apple menolak pembaruan Zeus karena "pelanggaran lisensi", dan pada tahun 2024, Phoenix Wallet meninggalkan App Store AS karena ketidakpastian peraturan mengenai penyedia layanan Lightning. Hambatan-hambatan ini menjelaskan mengapa banyak pengembang Lightning lebih memilih Android, yang menawarkan kebijakan yang lebih terbuka untuk aplikasi non-kustodian.



Tersedia tiga metode instalasi untuk Android: Google Play Store (5000+ instalasi, pembaruan otomatis), F-Droid (build yang dapat direproduksi, verifikasi kode sumber), atau APK manual dari GitHub.



![BitBanana](assets/fr/01.webp)



Situs web resmi bitbanana.app (kiri) membanggakan "100% Kustodian Mandiri dengan pengumpulan data NOL". Layar tengah menunjukkan tiga opsi pengunduhan: F-Droid (disarankan), Google Play, dan APK. Layar di sebelah kanan menunjukkan izin pemberitahuan untuk peringatan pembayaran.



Aplikasi ini meminta izin: jaringan (koneksi simpul), kamera (kode QR), NFC (LNURL), layanan latar belakang (pemberitahuan), biometrik (keamanan), dan WireGuard VPN. Tanpa pelacak, tanpa pengumpulan data. Aktifkan kata sandi atau penguncian biometrik untuk mengamankan akses.



## Konfigurasi awal



### Menghubungkan ke node LND



Untuk menghubungkan BitBanana ke node LND Anda (Umbrel, RaspiBlitz, myNode), dapatkan URI `lndconnect` atau kode QR yang berisi alamat, sertifikat TLS, dan makaroni otentikasi.



Untuk tutorial ini, kami menggunakan node LND melalui umbrel. Untuk lebih jelasnya, silakan lihat tutorial khusus kami:



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)



Pada aplikasi Lightning Node, akses menu di kanan atas dan pilih "Hubungkan wallet".



![BitBanana](assets/fr/04.webp)



Pilih **gRPC (Tor)** untuk menyambung melalui Tor (disarankan). Kode QR dan detail (Host .onion, Port 10009, Macaroon) ditampilkan.



![BitBanana](assets/fr/02.webp)



Di BitBanana, tekan "HUBUNGKAN NODE", pindai kode QR atau tempelkan URI. Otorisasi akses kamera, lalu periksa alamat .onion yang ditampilkan sebelum mengonfirmasi.



*koneksi *Core Lightning**



Jika Anda menggunakan Core Lightning (CLN) dan bukan LND, prosesnya tetap sama, dengan URI `clngrpc://` yang berisi sertifikat TLS bersama. Core Lightning secara native mendukung BOLT12 (penawaran), memungkinkan faktur yang dapat digunakan kembali dan pembayaran berulang yang tidak tersedia pada LND.



**Koneksi tanpa simpul pribadi (LNbits/hosted)**



Jika Anda tidak memiliki node Lightning, BitBanana dapat terhubung ke layanan yang dihosting melalui LndHub (protokol yang digunakan oleh BlueWallet dan LNbits) atau Nostr Wallet Connect (NWC). Harap diperhatikan: mode-mode ini beroperasi dalam mode kustodian (layanan menyimpan dana Anda) dengan fungsionalitas yang terbatas. Anda tidak akan dapat mengelola saluran atau mengonfigurasi biaya perutean, dan hanya dapat mengirim dan menerima pembayaran Lightning.



Untuk detail lebih lanjut tentang LNbits atau Nostr Wallet Connect, silakan baca berbagai tutorial kami:



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Penggunaan sehari-hari



### Interface utama



Layar beranda menampilkan saldo Lightning Anda, dengan menu di kiri atas yang memberikan akses ke bagian berikut: Saluran, Perutean, Tanda tangani/Verifikasi, Simpul, Kontak, Pengaturan, Cadangan. Ikon jam (kanan atas) membuka riwayat transaksi. Tombol "Kirim" dan "Terima" di bagian bawah memungkinkan Anda untuk mengirim dan menerima satoshi.



![BitBanana](assets/fr/05.webp)



### Pembayaran Lightning dan on-chain



![BitBanana](assets/fr/10.webp)



**Mengirim pembayaran:** Tekan tombol "Kirim" dari layar beranda. Layar pembayaran (kiri) menawarkan Anda untuk menempelkan alamat atau data pembayaran ke dalam bidang "Address atau data pembayaran", dengan pemindai QR di kanan atas untuk memindai kode. Anda juga dapat memilih kontak yang disimpan di bagian Kontak agar tidak perlu memindai setiap kali.



BitBanana dengan cerdas mengenali semua format pembayaran: faktur Lightning klasik (string karakter yang dimulai dengan `lnbc`), Lightning Address (format email seperti `utilisateur@domaine.com`), kode LNURL-pay untuk pembayaran dinamis, LNURL-withdraw untuk menarik dana, dan bahkan pembayaran Keysend langsung ke kunci publik Lightning tanpa faktur sebelumnya. Aplikasi ini secara otomatis melakukan resolusi LNURL yang diperlukan di latar belakang.



Setelah faktur dimuat, BitBanana akan menampilkan detail lengkap: jumlah yang tepat, perkiraan biaya routing, deskripsi pembayaran (jika disediakan oleh penerima), dan tanggal kedaluwarsa faktur. Setelah konfirmasi, pembayaran akan dirutekan melalui saluran Lightning Anda. Anda kemudian dapat melihat rute yang diambil langkah demi langkah dan biaya yang sebenarnya dibayarkan dalam detail transaksi.



**Menerima pembayaran:** Tekan tombol "Terima". Sebuah pemilih (layar kanan) memungkinkan Anda memilih antara Lightning (pembayaran instan melalui saluran Anda) dan On-Chain. Untuk tanda terima Lightning, masukkan jumlah yang diinginkan dalam satoshi (atau biarkan di angka 0 untuk membuat faktur tanpa jumlah yang pasti untuk diisi oleh pembayar), dan tambahkan deskripsi opsional untuk ditampilkan pada faktur. BitBanana secara instan membuat faktur Lightning dengan kode QR untuk pemindaian. Anda juga bisa menyalin faktur sebagai teks dan mengirimkannya melalui email. Segera setelah pembayaran diterima, sebuah notifikasi push akan memberitahukan Anda dan transaksi akan langsung muncul di riwayat dengan semua detailnya.



### Saluran dan perutean



![BitBanana](assets/fr/06.webp)



Bagian "Saluran" menampilkan kemampuan kirim/terima Anda dan daftar saluran Anda dengan avatar unik. Setiap saluran menunjukkan pembagian likuiditasnya antara saldo lokal dan jarak jauh. Sentuh sebuah saluran untuk mengetahui detail lengkap dan tindakan (menutup, mengubah biaya perutean). Tiga titik di kanan atas memberikan akses ke opsi "Rebalance" untuk menyeimbangkan kembali likuiditas saluran Anda. Tombol "+" membuka saluran baru.



Bagian Routing (layar tengah) menampilkan pendapatan penerusan berdasarkan periode (1D, 1W, 1M, 3M, 6M, 1Y) dengan riwayat penerusan yang mendetail untuk mengoptimalkan strategi Anda.



Sign/Verify (layar kanan) memungkinkan Anda untuk menandatangani/memverifikasi pesan secara kriptografis untuk membuktikan kontrol node.



### Multi-simpul dan parameter



![BitBanana](assets/fr/07.webp)



**Manage Nodes**: daftar node Anda, dengan tombol untuk menambahkan secara manual, memindai QR, atau beralih di antara node. Secara khusus, Anda dapat mengatur berbagai jenis koneksi ke node yang sama: LAN, VPN atau Tor.



**Kelola Kontak**: menyimpan kontak Lightning Anda untuk pembayaran cepat.



**Pengaturan**: menyesuaikan mata uang, bahasa, avatar. Bagian Keamanan & Privasi: Kunci Aplikasi (PIN/biometrik), Sembunyikan saldo (mode siluman), Tor (anonimisasi IP). Konfigurasi peramal harga, penjelajah blok, estimator biaya khusus.



## Keuntungan dan keterbatasan



**Sorotan:**




- Mobilitas total: kendalikan simpul Lightning Anda dari mana saja
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
- Jangan pernah membagikan URI atau maket login Anda
- Mode siluman di lingkungan yang tidak bersahabat



**Login:**




- VPN mesh (Tailscale, ZeroTier): kompromi terbaik antara kecepatan dan keamanan
- Tor: kerahasiaan maksimum, latensi yang lebih tinggi
- Clearnet: hindari kecuali jika diperlukan (paparan IP, port terbuka)



### Pencadangan dan pemulihan



Terakhir, ada menu "Backup", yang memungkinkan Anda menyimpan konfigurasi untuk migrasi telepon atau instalasi ulang.



![BitBanana](assets/fr/08.webp)



**Penting:** Cadangan TIDAK berisi seed atau cadangan saluran (yang akan dilakukan pada node). Cadangan ini berisi: konfigurasi node (alamat, sertifikat, maket), label, kontak, parameter. Tombol Pulihkan memungkinkan Anda untuk mengimpor cadangan yang ada. Konfirmasi diperlukan sebelum menyimpan.



![BitBanana](assets/fr/09.webp)



Masukkan kata sandi enkripsi (layar kanan). Sistem akan membuka pemilih file (layar kiri) untuk menyimpan `BitBananaBackup_2025-XX-XX.dat`. Konfirmasi "Cadangan dibuat".



**Keamanan:** Simpan cadangan dalam keadaan terenkripsi (cloud pribadi, USB, NAS). Jangan pernah berbagi file atau kata sandi. Uji pemulihan secara teratur. Cadangan memulihkan koneksi, bukan dana.



## BitBanana vs Zeus: Apa perbedaannya?



Jika Anda menjelajahi aplikasi seluler untuk mengelola simpul Lightning, Anda mungkin akan menemukan Zeus, sebuah alternatif populer untuk BitBanana. Tidak seperti BitBanana, yang berfokus secara eksklusif pada kendali jarak jauh dari node yang sudah ada, Zeus mengambil pendekatan yang lebih komprehensif, menawarkan dua mode operasi: node Lightning yang tertanam langsung di aplikasi (mode tertanam dengan LND terintegrasi) dan koneksi jarak jauh ke node eksternal, seperti BitBanana.



Fungsi ganda ini membuat Zeus sangat menarik bagi para pemula yang ingin bereksperimen dengan Lightning tanpa infrastruktur sebelumnya. Mode tertanam memungkinkan start-up langsung dengan mobile node yang lengkap, sementara pengguna tingkat lanjut dapat beralih ke koneksi jarak jauh setelah node pribadi mereka dikonfigurasi. Zeus juga mendukung LND dan Core Lightning untuk koneksi jarak jauh, seperti BitBanana.



Keuntungan utama lain dari Zeus adalah ketersediaan lintas platform (iOS dan Android), sedangkan BitBanana tetap berbasis Android secara eksklusif. Zeus juga menggabungkan infrastruktur LSP Olympus untuk memfasilitasi penerimaan pembayaran Lightning melalui saluran just-in-time, sistem Point of Sale untuk pedagang, dan fungsionalitas swap yang terintegrasi untuk mengelola likuiditas.



Namun, BitBanana mempertahankan kekuatan spesifiknya: antarmuka yang lebih sederhana, lebih ramping, pengalaman pengguna yang lebih baik (UX) berkat fokus eksklusifnya pada kendali jarak jauh, dan pendekatan edukatif dengan penjelasan kontekstual. Zeus menawarkan lebih banyak fungsionalitas, tetapi dengan mengorbankan antarmuka yang lebih kompleks. Aplikasi ini tetap sangat cocok untuk pengguna yang ingin mengontrol node secara eksklusif dari jarak jauh, tanpa fungsi kustodian.



Untuk mengetahui lebih lanjut tentang Zeus, lihat tutorial berikut ini:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## Kesimpulan



BitBanana mengubah ponsel pintar Android Anda menjadi dasbor Lightning yang lengkap, menawarkan mobilitas yang belum pernah ada sebelumnya untuk operator node. Aplikasi ini mencakup semua fungsi: pembayaran (semua format), manajemen saluran, kontrol koin, menara pengawas, multi-node, dengan keamanan yang ditingkatkan (PIN / biometrik, Tor, PIN Darurat).



Sepenuhnya berdaulat, BitBanana tidak mengumpulkan data dan tidak mengorbankan kerahasiaan maupun kontrol dana Anda. Kode sumber terbuka (MIT) menjamin transparansi.



## Sumber daya



### Dokumentasi resmi




- [Situs web BitBanana](https://bitbanana.app)
- [Dokumentasi lengkap](https://docs.bitbanana.app)
- [Kode sumber GitHub](https://github.com/michaelWuensch/BitBanana)



### Instalasi




- [Google Play Store](https://play.google.com/store/apps/details?id=app.michaelwuensch.bitbanana)
- [F-Cold](https://f-droid.org/packages/app.michaelwuensch.bitbanana)