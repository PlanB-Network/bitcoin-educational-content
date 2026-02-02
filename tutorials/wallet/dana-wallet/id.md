---
name: Dana Wallet
description: Portofolio minimalis untuk Pembayaran Diam (BIP-352)
---

![cover](assets/cover.webp)



Penggunaan kembali alamat Bitcoin adalah salah satu ancaman paling langsung terhadap kerahasiaan pengguna. Ketika seorang penerima berbagi satu alamat untuk menerima banyak pembayaran, pengamat mana pun dapat melacak semua transaksi yang terkait dan merekonstruksi riwayat keuangan mereka. Masalah ini terutama mempengaruhi pembuat konten, badan amal atau aktivis yang ingin menampilkan alamat donasi kepada publik tanpa mengorbankan privasi mereka atau para donatur.



Dana Wallet menjawab masalah ini dengan solusi yang elegan: Pembayaran Senyap. wallet yang minimalis dan bersumber terbuka, diluncurkan pada tahun 2024, menghasilkan alamat statis yang dapat digunakan kembali sambil menjamin bahwa setiap pembayaran yang diterima berakhir di alamat yang terpisah di blockchain. Pengirim tidak perlu berinteraksi dengan penerima, dan tidak ada pengamat eksternal yang dapat menghubungkan setiap transaksi secara bersamaan. Pada blockchain, pembayaran ini terlihat seperti transaksi Taproot biasa.



Dana Wallet tersedia di Mainnet dan Signet, tetapi para pengembang masih menganggapnya sebagai eksperimental dan merekomendasikan untuk tidak mendepositkan dana yang Anda tidak siap untuk kehilangannya. Dalam tutorial ini, kita akan menggunakan versi Signet untuk menemukan Pembayaran Diam tanpa mempertaruhkan dana sungguhan.



## Apa itu Dana Wallet?



### Filosofi dan tujuan



Dana Wallet mengadopsi pendekatan "SP-first": wallet menghasilkan alamat Pembayaran Diam secara eksklusif, dan hanya menerima jenis pembayaran ini. Anda tidak akan dapat membuat alamat Bitcoin klasik (standar lama, SegWit atau Taproot) dengan aplikasi ini. Pembatasan yang disengaja ini memungkinkan Anda untuk berkonsentrasi penuh dalam mempelajari protokol BIP-352 tanpa terganggu oleh fitur lain. Antarmuka yang tidak berantakan dengan sengaja mengutamakan kemudahan penggunaan daripada opsi yang banyak, membuat alat ini dapat diakses bahkan oleh pengguna yang baru mengenal konsep kerahasiaan on-chain.



Proyek ini sepenuhnya bersifat open-source, dikembangkan dengan Flutter untuk antarmuka seluler dan Rust untuk logika kriptografi internal. Arsitektur ini menggabungkan pengalaman pengguna yang lancar dengan kinerja optimal untuk operasi pemindaian intensif.



### Bagaimana cara kerja Pembayaran Diam?



Pembayaran Senyap (BIP-352) didasarkan pada mekanisme kriptografi yang canggih dengan menggunakan Elliptic Curve Diffie-Hellman Key Exchange (ECDH). Penerima menghasilkan alamat statis (dimulai dengan `sp1...` pada mainnet atau `tsp1...` pada Signet) yang terdiri dari dua kunci publik yang berbeda: kunci pemindaian ($B_{scan}$) untuk mendeteksi pembayaran yang masuk, dan kunci pengeluaran ($B_{spend}$) untuk membelanjakan dana yang diterima. Pemisahan ini memungkinkan untuk menyimpan kunci pengeluaran pada perangkat keras wallet sementara menggunakan kunci pemindaian pada perangkat yang terhubung.



Ketika pengirim ingin melakukan pembayaran, wallet-nya menggabungkan jumlah dari kunci privat masukannya dengan kunci pemindaian publik penerima untuk menghitung rahasia ECDH bersama. Rahasia ini menghasilkan "tweak" kriptografi yang, ditambahkan ke kunci pengeluaran penerima, menciptakan alamat Taproot yang unik untuk transaksi tersebut.



Penerima dapat mereproduksi perhitungan ini dengan menggunakan kunci pemindaian pribadinya dan kunci publik yang terlihat dalam transaksi (properti matematika Diffie-Hellman). Hal ini memungkinkannya untuk mendeteksi dan membelanjakan dana tanpa interaksi dengan pengirim.



Pendekatan ini menawarkan beberapa keuntungan:




- Kerahasiaan penerima**: setiap pembayaran berakhir di alamat yang berbeda
- Kerahasiaan pengirim**: tidak ada pengenal persisten yang menghubungkan pembayaran
- Tidak ada server pihak ketiga**: protokol beroperasi secara mandiri
- Transaksi yang tidak dapat dibedakan**: Pembayaran Diam terlihat seperti transaksi Taproot biasa



Kelemahan utamanya adalah biaya pemindaian: penerima harus menganalisis setiap transaksi Taproot baru untuk mendeteksi transaksi yang ditujukan kepadanya.



Jika Anda ingin mempelajari lebih lanjut mengenai pengoperasian teknis Pembayaran Senyap, kami merekomendasikan kursus BTC204 tentang kerahasiaan di Bitcoin, yang mencakup satu bab yang didedikasikan untuk Pembayaran Senyap:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Platform yang didukung



Dana Wallet tersedia sebagai aplikasi Android. APK dapat diunduh melalui repositori F-Droid khusus yang disediakan oleh pengembang, melalui Obtainium, atau langsung dari GitHub. Untuk pengguna Linux, secara teknis memungkinkan untuk mengkompilasi aplikasi Flutter untuk desktop.



Aplikasi ini tidak tersedia di iOS atau melalui toko resmi (Google Play, App Store), yang mencerminkan status eksperimental dan fokusnya pada audiens teknis.



## Instalasi



### Prasyarat penting



Untuk menginstal Dana Wallet di Android, Anda membutuhkan perangkat Android dengan opsi "Sumber tidak dikenal" yang diaktifkan di pengaturan keamanan. Tidak diperlukan akun atau pendaftaran.



### Tambahkan deposit F-Cold



Metode yang direkomendasikan adalah menambahkan repositori F-Droid khusus Dana Wallet. Buka `fdroid.silentpayments.dev` di mana Anda akan menemukan tautan repositori dan kode QR untuk dipindai. Repositori saat ini menawarkan 3 aplikasi: versi Mainnet, Pengembangan dan Signet.



![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)



### Instalasi melalui F-Droid



Buka aplikasi F-Droid di perangkat Android Anda, lalu akses Pengaturan melalui ikon di kanan bawah. Pilih "Repositori" untuk mengelola sumber aplikasi. Tekan tombol "+" untuk menambahkan repositori baru, lalu pindai kode QR atau tempel tautan `https://fdroid.silentpayments.dev/fdroid/repo`. Setelah repositori ditambahkan, Anda akan melihat tiga versi Dana Wallet yang tersedia. Pilih "Dana Wallet - Bookmark" dan tekan "Instal".



![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)



## Konfigurasi awal



### Pembuatan portofolio



Saat pertama kali diluncurkan, Dana Wallet menampilkan layar selamat datang yang memperkenalkan misinya: "Mengirim dan menerima donasi tanpa perantara". Tekan "Mulai" untuk melanjutkan. Layar berikutnya menampilkan tiga manfaat utama aplikasi ini:




- Donasi yang mudah**: mulai menerima donasi dalam hitungan detik
- Privasi secara default**: tidak perlu server atau infrastruktur yang rumit
- Pengalaman seperti email**: mengirim dan menerima bitcoin semudah email



Anda dapat memilih antara "Restore" untuk memulihkan portofolio yang sudah ada atau "Create new wallet" untuk membuat portofolio baru. Tekan "Buat wallet baru".



![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)



Aplikasi ini kemudian menghasilkan frasa pemulihan, yang harus Anda catat dengan hati-hati pada media fisik. Bahkan untuk dana uji coba yang tidak bernilai, terapkanlah praktik pencadangan yang baik.



### Interface dan parameter



Setelah portofolio dibuat, Anda akan dibawa ke antarmuka utama, yang dibagi menjadi dua tab: "Bertransaksi" dan "Pengaturan".



Tab **Transaksi** menampilkan saldo bitcoin Anda (dan konversinya ke dolar), daftar transaksi terbaru, dan dua tombol aksi: "Bayar" untuk mengirim dana, dan tombol terima (ikon unduh).



Tab **Pengaturan** menawarkan empat opsi:




- Tampilkan frasa seed**: menampilkan frasa pemulihan Anda untuk disimpan
- Ubah mata uang fiat**: mengubah mata uang tampilan (USD secara default)
- Atur url backend**: konfigurasikan URL server Blindbit (lihat bagian selanjutnya)
- Bersihkan wallet**: menghapus sepenuhnya wallet dari perangkat



![Interface principale Transact et menu Settings](assets/fr/04.webp)



### Server Blindbit



Dana Wallet menggunakan server pengindeksan yang disebut **Blindbit** untuk mendeteksi Pembayaran Diam Anda. Memahami cara kerjanya penting untuk mengevaluasi model kepercayaan aplikasi.



**Mengapa kita membutuhkan server?



Untuk mendeteksi Pembayaran Senyap, wallet Anda secara teoritis harus memindai semua transaksi Taproot di setiap blok dan melakukan penghitungan kriptografi (ECDH) untuk setiap transaksi. Pada ponsel, operasi ini akan terlalu banyak menggunakan komputasi dan bandwidth.



Server Blindbit memecahkan masalah ini dengan melakukan pra-perhitungan data perantara (disebut "tweak") untuk semua transaksi Taproot. wallet Anda kemudian mengunduh tweak ini (33 byte per transaksi) dan melakukan penghitungan akhir **secara lokal** untuk memeriksa apakah pembayaran adalah milik Anda.



**Kerahasiaan terjaga**



Tidak seperti server Electrum konvensional di mana Anda mengungkapkan alamat Anda, server Blindbit tidak mengetahui pembayaran mana yang menjadi milik Anda. Server ini menyediakan data yang sama untuk semua pengguna, dan ponsel Anda yang melakukan verifikasi akhir. Oleh karena itu, kerahasiaan Anda tetap terjaga terhadap server.



**Server default



Dana Wallet menggunakan server publik `silentpayments.dev/blindbit/signet` (untuk Signet) atau `silentpayments.dev/blindbit/mainnet` (untuk Mainnet). Anda dapat mengubah URL ini di pengaturan jika Anda meng-host server Anda sendiri.



**Hos server Blindbit Anda sendiri**



Bagi pengguna yang menginginkan kedaulatan penuh, dimungkinkan untuk meng-host server Blindbit Oracle mereka sendiri. Hal ini membutuhkan :




- Node Inti Bitcoin lengkap **non-eagle** (non-pruned)
- Menginstal Blindbit Oracle (tersedia di GitHub: `setavenger/blindbit-oracle`)
- Sekitar 10 GB ruang disk tambahan
- Keterampilan teknis (Kompilasi Go, konfigurasi server)



Belum ada aplikasi paket yang tersedia untuk Umbrel atau Start9. Instalasi tetap manual untuk saat ini. Ini adalah bidang yang masih terus berevolusi, dan solusi yang lebih mudah diakses mungkin akan muncul di masa depan.



## Penggunaan sehari-hari



### Menerima dana



Untuk menerima bitcoin, tekan tombol terima (ikon unduh) dari layar utama. Dana Wallet kemudian menampilkan alamat lengkap Pembayaran Diam Anda dalam format `tsp1q...` pada Bookmark. Antarmuka menawarkan beberapa opsi:




- Tampilkan kode QR**: menampilkan kode QR alamat Anda untuk memudahkan pemindaian
- Bagikan**: bagikan alamat melalui aplikasi ponsel Anda
- Salin**: menyalin alamat ke papan klip



Seperti yang ditunjukkan di layar, Anda dapat membagikan alamat ini secara publik di jejaring sosial Anda tanpa mengorbankan privasi Anda.



![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)



Untuk mendapatkan dana uji coba pertama Anda di Signet, gunakan faucet khusus Silent Payments yang dapat diakses di `silentpayments.dev/faucet/signet`. Salin alamat Anda `tsp1...`, tempelkan di kolom yang tersedia di faucet, lalu validasi permintaan. Tunggu hingga blok ditambang (sekitar 10 menit di Signet).



### Kirim pembayaran



Untuk mengirim dana, tekan tombol "Bayar" dari layar utama. Layar "Pilih penerima" akan muncul dengan tiga pilihan untuk menentukan penerima:




- Masukkan informasi pembayaran secara manual
- Tempel dari papan klip**: menempelkan alamat dari papan klip
- Pindai Kode QR**: pindai kode QR yang berisi alamat



Setelah alamat penerima divalidasi, layar "Masukkan jumlah" memungkinkan Anda memasukkan jumlah yang akan dikirim dalam satoshi. Saldo Anda yang tersedia akan ditampilkan sebagai referensi. Tekan "Lanjutkan ke pemilihan biaya" untuk melanjutkan.



![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)



Layar berikutnya menunjukkan tiga tingkat biaya, tergantung pada urgensi yang diperlukan:




- Cepat** (10-30 menit): biaya lebih tinggi untuk konfirmasi cepat
- Normal** (30-60 menit): biaya sedang
- Lambat** (1+ jam): biaya minimum untuk transaksi yang tidak mendesak



Setelah memilih tingkat biaya, layar konfirmasi "Siap mengirim?" akan merangkum semua rincian: alamat tujuan, jumlah, perkiraan waktu dan biaya transaksi. Periksa informasi ini dengan cermat, lalu tekan "Kirim" untuk mengirim transaksi.



Setelah terkirim, transaksi akan muncul di riwayat transaksi Anda dengan status "Belum Dikonfirmasi" hingga transaksi tersebut dimasukkan ke dalam blokir. Saldo Anda akan diperbarui.



![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)



## Keuntungan dan keterbatasan



### Sorotan





- Pedagogis**: antarmuka yang disederhanakan yang berfokus pada pembelajaran Pembayaran Diam
- Dua arah**: mendukung pengiriman dan penerimaan, tidak seperti portofolio lainnya
- Sumber terbuka**: kode yang dapat diaudit sepenuhnya di GitHub
- Faucet khusus**: memudahkan untuk mendapatkan pendanaan pengujian
- Tanpa akun**: tidak perlu registrasi atau data pribadi



### Kendala yang perlu dipertimbangkan





- Eksperimental**: perangkat lunak yang belum diaudit, gunakan dengan hati-hati pada Mainnet
- Platform terbatas**: terutama Android, tidak ada versi iOS
- Fungsionalitas yang dikurangi**: tidak ada kontrol koin, tidak ada sub-akun, tidak ada Lightning
- Pemindaian intensif**: deteksi pembayaran menghabiskan sumber daya yang signifikan



## Praktik terbaik



### Keamanan seed



Bahkan untuk tes Signet dengan latar belakang yang tidak berarti, perlakukan frasa pemulihan Anda dengan serius. Gunakan opsi "Tampilkan frasa seed" dalam pengaturan untuk menuliskannya dengan hati-hati. Sebagai praktik yang baik, simpanlah wallet yang benar-benar terpisah untuk Signet dan Mainnet: jangan pernah menggunakan seed yang dibuat untuk pengujian pada wallet yang dimaksudkan untuk menerima dana sungguhan.



### Peringatan tentang status percobaan



Dana Wallet masih dianggap eksperimental oleh pengembangnya. Seperti yang mereka nyatakan dengan jelas: "Jangan gunakan dana yang Anda tidak rela kehilangannya". Untuk tujuan pembelajaran, pilihlah versi Signet. Jika Anda menggunakan versi Mainnet, batasi diri Anda pada jumlah token.



### Pencadangan dan pemulihan



Pemulihan dana Silent Payments membutuhkan wallet yang kompatibel dengan protokol BIP-352. wallet standar tidak dapat memindai blockchain untuk mengambil Silent Payments UTXO Anda. Tetap pasang Dana Wallet atau gunakan opsi "Pulihkan" pada saat pertama kali diluncurkan untuk memulihkan wallet yang sudah ada.



## Perbandingan dengan BIP-47 dan PayJoin



| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

Pembayaran Senyap menghilangkan transaksi notifikasi BIP-47 dengan biaya pemindaian yang lebih mahal. PayJoin memecahkan masalah yang berbeda (korelasi input) dan dapat digabungkan dengan Pembayaran Diam.



## Kesimpulan



Dana Wallet adalah alat pendidikan yang berharga untuk belajar tentang Pembayaran Senyap dalam lingkungan yang bebas risiko. Pendekatannya yang minimalis memungkinkan Anda untuk memahami mekanisme fundamental protokol BIP-352 tanpa terganggu oleh fitur-fitur sekunder. Dengan bereksperimen dengan Signet, Anda akan mengembangkan pemahaman praktis tentang teknologi yang menjanjikan untuk kerahasiaan transaksi Bitcoin ini.



Silent Payments merupakan sebuah langkah maju yang signifikan dalam mendamaikan kemudahan penggunaan dan penghormatan terhadap privasi. Antusiasme komunitas dan integrasi pertama ke berbagai dompet (Cake Wallet, BitBox02, BlueWallet untuk pengiriman) menunjukkan masa depan di mana mempublikasikan alamat donasi tidak lagi membahayakan privasi keuangan pemiliknya.



## Sumber daya



### Dokumentasi resmi




- Repositori GitHub Dana Wallet: https://github.com/cygnet3/danawallet
- Setoran F-Cold: https://fdroid.silentpayments.dev
- Situs komunitas Silent Payments: https://silentpayments.xyz
- Spesifikasi BIP-352: https://bips.dev/352



### Alat uji tanda tangan




- Faucet Pembayaran Senyap: https://silentpayments.dev/faucet/signet
- Signet Mempool Explorer: https://mempool.space/signet



### Server Blindbit (dihosting sendiri)




- Blindbit Oracle (GitHub): https://github.com/setavenger/blindbit-oracle