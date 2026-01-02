---
name: Bitcoin Keeper
description: Bitcoin mobile wallet untuk keamanan dan multi-sig
---

![cover](assets/cover.webp)



Pengelolaan bitcoin yang aman merupakan tantangan besar bagi setiap pemegang yang sadar akan pertaruhan yang terlibat dalam kedaulatan keuangan. Di antara kesederhanaan wallet seluler dan ketangguhan solusi multi-sig, kesenjangan teknis dapat tampak menakutkan bagi banyak pengguna. Bitcoin Keeper diposisikan tepat di persimpangan ini, menawarkan pendekatan progresif terhadap keamanan yang menyertai pengguna saat mereka berevolusi.



Bitcoin Keeper adalah aplikasi seluler sumber terbuka, yang secara eksklusif didedikasikan untuk Bitcoin, yang dikembangkan oleh tim BitHyve. Ambisinya adalah untuk membuat manajemen portofolio tingkat lanjut dapat diakses, terutama konfigurasi multisignature, dengan tetap mempertahankan antarmuka yang intuitif untuk pemula. Aplikasi ini mengadopsi slogan "Amankan hari ini, Rencanakan hari esok", yang mencerminkan filosofi dukungan jangka panjang.



Tidak seperti dompet generalis yang mengelola banyak mata uang kripto, Bitcoin Keeper mempertahankan fokus yang ketat pada Bitcoin. Pendekatan khusus bitcoin ini mengurangi potensi serangan dan sangat menyederhanakan pengalaman pengguna. Aplikasi ini juga menonjol karena integrasi asli dari dompet perangkat keras yang paling luas dan fitur manajemen UTXO yang canggih.



## Apa itu Bitcoin Keeper?



### Filosofi dan tujuan



Bitcoin Keeper dirancang untuk memenuhi kebutuhan spesifik para pengguna bitcoin yang ingin mempertahankan kontrol penuh atas kunci pribadi mereka. Proyek ini sepenuhnya merangkul prinsip-prinsip dasar Bitcoin: kode sumber yang terbuka dan dapat diaudit, menghormati privasi, dan kedaulatan pengguna. Tidak ada registrasi atau informasi pribadi yang dibutuhkan untuk menggunakan aplikasi ini, dan bahkan dapat berjalan secara offline untuk operasi penandatanganan.



Tujuan utamanya adalah untuk menawarkan alat yang fleksibel dan tahan terhadap masa depan untuk menyimpan BTC selama beberapa tahun, dan bahkan beberapa generasi, berkat fungsi pewarisan. Aplikasi ini memungkinkan pengguna untuk memulai dengan mudah dengan wallet seluler, dan kemudian secara bertahap berevolusi menuju solusi multi-tanda tangan yang lebih aman.



### Arsitektur aplikasi



Bitcoin Keeper mengatur pengelolaan dana dengan dua konsep yang berbeda. Hot Wallet** adalah wallet dengan satu kunci sederhana, disimpan di ponsel, dirancang untuk pengeluaran sehari-hari dan dalam jumlah yang tidak terlalu besar. Vaults** adalah brankas multi-tanda tangan (Multi-Key) yang membutuhkan beberapa kunci untuk mengesahkan pengeluaran, yang dirancang untuk penyimpanan jangka panjang yang aman.



### Fitur utama



Bitcoin Keeper mendukung hampir semua dompet perangkat keras yang ada di pasaran: Coldcard, Trezor, Ledger, Keystone, BitBox02, Jade, Seedsigner, Passport, dan Tapsigner dari Coinkite. Integrasi dilakukan melalui berbagai metode yang berbeda, tergantung pada perangkatnya: Pemindaian kode QR, koneksi NFC, atau impor file.



Aplikasi ini juga menawarkan manajemen UTXO tingkat lanjut dengan pelabelan transaksi, kontrol koin untuk memilih input secara manual saat mengirim, dan dukungan format PSBT untuk transaksi yang ditandatangani sebagian.



## Instalasi dan konfigurasi awal



Bitcoin Keeper tersedia gratis di Android melalui Google Play Store dan iOS melalui App Store. Penerbit yang terdaftar adalah BitHyve. Sebelum menginstal, pastikan perangkat Anda bebas malware, terbaru, dan tidak di-root atau di-jailbreak.



Pada saat pertama kali diluncurkan, aplikasi akan meminta Anda untuk membuat kode PIN keamanan. Kode ini melindungi akses ke wallet Anda dan mengenkripsi data sensitif secara lokal. Pilih kode yang kuat dan hafalkan. Anda kemudian dapat mengaktifkan otentikasi biometrik (sidik jari atau ID Wajah) untuk membuka kunci yang lebih cepat.



![Installation et configuration du PIN](assets/fr/01.webp)



Aplikasi ini kemudian menyajikan beberapa layar pengantar yang menjelaskan tiga pilarnya: Pembuatan wallet untuk mengirim dan menerima bitcoin, manajemen kunci dengan kompatibilitas perangkat keras wallet, dan perencanaan warisan untuk mewariskan bitcoin. Tekan "Mulai", lalu pilih "Mulai Baru" untuk membuat konfigurasi baru.



![Écrans d'introduction](assets/fr/02.webp)



## Menemukan antarmuka



Antarmuka Bitcoin Keeper diatur di sekitar empat tab utama yang dapat diakses dari bilah navigasi bawah:



![Les quatre onglets de l'application](assets/fr/03.webp)



Tab **Dompet** menampilkan dompet Anda dan saldonya. Di sinilah Anda mengakses dompet Anda untuk mengirim dan menerima bitcoin. Tag "Hot Wallet" dan "Single-Key" atau "Multi-Key" memungkinkan Anda untuk dengan cepat mengidentifikasi jenis setiap wallet.



Tab **Keys** memusatkan pengelolaan kunci tanda tangan Anda. Di sini Anda akan menemukan Kunci Seluler yang dihasilkan oleh aplikasi, serta semua kunci yang diimpor dari dompet perangkat keras. Di sini juga Anda dapat menambahkan perangkat tanda tangan baru.



Tab **Concierge** menawarkan layanan dukungan: kirimkan pertanyaan ke tim dukungan dan terhubung dengan penasihat Bitcoin untuk mendapatkan bantuan yang disesuaikan.



Tab **Lebih Banyak** (Opsi Lainnya) memberikan akses ke pengaturan seperti koneksi server pribadi, cadangan kunci, dokumen warisan, preferensi tampilan dan manajemen wallet.



## Koneksi ke server Anda sendiri



Untuk memperkuat kerahasiaan Anda, Bitcoin Keeper memungkinkan Anda menghubungkan aplikasi ke server Electrum Anda sendiri, daripada menggunakan server publik default.



![Configuration du serveur Electrum](assets/fr/04.webp)



Dari tab Lainnya, gulir ke bawah untuk menemukan pengaturan server. Tekan "Add Server" untuk mengonfigurasi koneksi baru. Anda dapat memilih antara "Public Server" (server publik yang telah dikonfigurasi sebelumnya) dan "Private Electrum" (server Anda sendiri).



Untuk server pribadi, masukkan URL (misalnya umbrel.local untuk node Umbrel) dan nomor port (biasanya 50001). Aktifkan SSL jika server Anda mendukungnya. Anda juga dapat memindai kode QR konfigurasi. Setelah Anda memasukkan parameter, tekan "Hubungkan ke Server".



Jika Anda belum memiliki simpul Bitcoin Anda sendiri, lihatlah tutorial kami tentang Umbrel, cara sederhana dan terjangkau untuk memintal simpul Anda sendiri:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Menerima bitcoin



Dari tab Dompet, pilih wallet dari mana Anda ingin menerima dana dengan menekannya. Layar wallet akan menampilkan saldo dan tiga tombol aksi: Kirim Bitcoin, Terima Bitcoin, dan Lihat Semua Koin.



![Réception de bitcoins](assets/fr/05.webp)



Tekan "Terima Bitcoin". Bitcoin Keeper menghasilkan alamat penerimaan baru dalam format Bech32 (dimulai dengan bc1...), bersama dengan kode QR-nya. Anda bisa menambahkan label pada alamat ini untuk mengidentifikasi sumber dana. Bagikan alamat dengan pengirim dengan menampilkan kode QR atau menyalin alamat teks.



Aplikasi ini secara otomatis menghasilkan alamat baru untuk setiap penerimaan, menjaga privasi Anda. Gunakan "Dapatkan Address Baru" untuk mendapatkan alamat kosong jika perlu.



## Manajemen UTXO



Bitcoin Keeper menawarkan visibilitas lengkap dari UTXO (Hasil Transaksi yang Tidak Digunakan) yang membentuk saldo Anda. Dari layar wallet, tekan "Lihat Semua Koin" untuk mengakses manajer sudut.



![Gestion des UTXO](assets/fr/06.webp)



Layar "Kelola Koin" mencantumkan setiap UTXO satu per satu dengan jumlah dan labelnya. Tampilan ini memungkinkan Anda untuk melacak asal koin dan mengaturnya. Anda bisa memilih UTXO tertentu melalui "Pilih untuk Dikirim" untuk dikirim dengan kontrol koin, sehingga menghindari pencampuran koin dari sumber yang berbeda.



## Kirim bitcoin



Untuk mengirim, pilih portofolio sumber dan tekan "Kirim Bitcoin". Masukkan alamat tujuan (ditempelkan atau dipindai melalui kode QR) dan secara opsional tambahkan label untuk mengidentifikasi penerima.



![Envoi de bitcoins](assets/fr/07.webp)



Layar berikutnya memungkinkan Anda untuk memasukkan jumlah yang akan dikirim. Antarmuka menampilkan saldo yang tersedia dan konversi mata uang fiat. Pilih prioritas biaya: Rendah (ekonomis, ~60 menit), Sedang, atau Tinggi (prioritas). Perkiraan biaya dalam sats/vbyte ditampilkan secara real time. Tekan "Kirim" untuk melanjutkan.



![Confirmation et envoi](assets/fr/08.webp)



Layar ringkasan menampilkan semua rincian: Sumber wallet, alamat tujuan, prioritas transaksi, biaya jaringan, jumlah yang dikirim, dan total. Mohon periksa informasi ini dengan cermat, karena transaksi Bitcoin tidak dapat dibatalkan. Tekan "Konfirmasi & Kirim" untuk mengirim transaksi.



Konfirmasi "Kirim Berhasil" akan muncul dengan ringkasan lengkap. Transaksi dapat dilihat di riwayat "Transaksi Terakhir" dengan labelnya.



## Simpan kunci Anda



Mencadangkan Kunci Pemulihan Anda adalah langkah penting. Dari tab Lainnya, buka bagian "Pencadangan dan Pemulihan" dan klik "Kunci Pemulihan".



![Sauvegarde de la Recovery Key](assets/fr/09.webp)



Layar menampilkan status cadangan Anda. Untuk memverifikasi cadangan Anda, aplikasi meminta Anda mengonfirmasi kata tertentu dalam frasa Anda (mis. kata ke-7). Verifikasi ini memastikan bahwa Anda telah menuliskan frasa pemulihan dengan benar.



Dari "Pengaturan Kunci Pemulihan", Anda dapat melihat frasa lengkap Anda melalui "Lihat Kunci Pemulihan" dan melihat Sidik Jari Penandatangan kunci Anda. Simpan frasa 12 kata Anda di atas kertas, di tempat yang aman, jauh dari kelembapan dan api. Jangan pernah menyimpannya di perangkat yang terhubung.



## Menambahkan kunci eksternal (perangkat keras wallet)



Salah satu aset utama Bitcoin Keeper adalah integrasi dompet perangkat keras. Dari tab Kunci, tekan "Tambah kunci" untuk menambahkan perangkat tanda tangan baru.



![Ajout d'une clé hardware](assets/fr/10.webp)



Pilih "Tambahkan kunci dari perangkat keras" untuk menghubungkan perangkat keras wallet. Aplikasi ini mendukung berbagai macam perangkat: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner, dan Specter Solutions.



### Konfigurasi Tapsigner



Tapsigner adalah kartu NFC dari Coinkite yang sangat cocok untuk penggunaan seluler. Jika Anda ingin mempelajari lebih lanjut, kami memiliki tutorial khusus:



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

Untuk menambahkan Tapsigner, pilih dari daftar dompet perangkat keras.



![Configuration du Tapsigner](assets/fr/11.webp)



Pertama, masukkan kode PIN 6-32 digit yang tercetak di bagian belakang kartu Anda (standar pada kartu baru), atau PIN Anda jika sudah dikonfigurasi. Tekan "Lanjutkan", lalu dekatkan Tapsigner ke bagian belakang ponsel Anda ketika "Siap untuk memindai" ditampilkan. Komunikasi NFC secara otomatis mengimpor kunci publik. Anda kemudian dapat menambahkan deskripsi (misalnya "Kartu Metro") untuk mengidentifikasi kunci ini.



## Membuat portofolio multisig



Setelah Anda mengatur kunci Anda, Anda bisa membuat wallet multi-tanda tangan yang menggabungkan beberapa perangkat. Dari tab Dompet, klik "Tambahkan Wallet".



![Création d'un nouveau wallet](assets/fr/12.webp)



Anda memiliki tiga opsi: "Buat Wallet" untuk portofolio baru, "Impor Wallet" untuk memulihkan wallet yang sudah ada, atau "Wallet Kolaboratif" untuk brankas bersama. Pilih "Buat Wallet" lalu "Bitcoin Wallet".



![Sélection du type de wallet](assets/fr/13.webp)



Layar berikutnya menawarkan konfigurasi yang berbeda-beda: "Tombol tunggal", "2 dari 3 tombol multi", atau "3 dari 5 tombol multi". Untuk multi-sig yang disesuaikan, tekan "Pilih pengaturan khusus". Misalnya, pilih "1 dari 2": satu tanda tangan diperlukan dari dua tombol yang memungkinkan.



Kemudian pilih kunci yang akan membentuk Vault Anda. Dalam contoh kami, kami menggabungkan "Kunci Ponsel" (kunci perangkat lunak telepon) dengan "TAPSIGNER" (Kartu Metro). Konfigurasi ini menawarkan redundansi: jika salah satu kunci tidak dapat diakses, Anda selalu dapat menggunakan dana Anda dengan kunci lainnya.



![Finalisation du wallet multisig](assets/fr/14.webp)



Beri nama wallet Anda (misalnya, "Test PlanB"), tambahkan deskripsi opsional, dan centang tombol yang dipilih. Tekan "Buat Wallet Anda". Pesan konfirmasi "Wallet Berhasil Dibuat" akan muncul, mengingatkan Anda untuk menyimpan file pemulihan wallet.



Multisig wallet baru Anda sekarang muncul di tab Dompet dengan tag "Multi-kunci" dan indikasi "1 dari 2".



### Menyimpan file konfigurasi



**Tidak seperti wallet sederhana, di mana frasa pemulihan sudah cukup untuk memulihkan akses, multisig wallet juga membutuhkan file konfigurasi yang menjelaskan struktur brankas (kunci mana yang berpartisipasi, berapa banyak tanda tangan yang diperlukan). Tanpa file ini, bahkan dengan semua frasa pemulihan, anda tidak akan dapat membangun kembali wallet anda.



![Export du fichier de configuration](assets/fr/15.webp)



Untuk mengekspor file ini, pilih multisig wallet Anda pada tab Wallets, lalu tekan ikon Pengaturan (roda gigi) di sudut kanan atas. Dalam "Pengaturan Wallet", klik "File konfigurasi Wallet". Beberapa opsi ekspor tersedia:





- Ekspor PDF**: menghasilkan dokumen PDF yang berisi semua informasi wallet
- Tampilkan QR**: menampilkan kode QR yang dapat dipindai untuk mengimpor konfigurasi ke perangkat lain
- Airdrop / Ekspor File**: mengekspor file melalui opsi berbagi di ponsel Anda
- NFC**: berbagi melalui NFC dengan perangkat yang kompatibel



Simpan file konfigurasi ini terpisah dari frasa pemulihan Anda, idealnya pada media yang dienkripsi atau dicetak. Jika Anda kehilangan ponsel Anda, file ini digabungkan dengan frasa pemulihan untuk setiap kunci yang berpartisipasi akan memungkinkan Anda untuk membangun kembali multisig wallet Anda di Bitcoin Keeper atau perangkat lunak lain yang kompatibel.



## Praktik terbaik



### Organisasi dana



Susunlah bitcoin Anda sesuai dengan penggunaannya: wallet Single-Key untuk pengeluaran saat ini dengan jumlah yang terbatas, dan satu atau beberapa Vaults Multi-Key untuk simpanan jangka panjang. Penandaan UTXO yang sistematis akan membantu Anda melacak dari mana dana Anda berasal, yang sangat berguna untuk mengelola kerahasiaan dan menghindari pencampuran koin dengan sumber yang berbeda.



Jaga keamanan ponsel Anda: aktifkan kunci biometrik, lakukan pembaruan sistem secara teratur, dan tetap waspada terhadap aplikasi yang terinstal. Dan terus perbarui Bitcoin Keeper dengan patch keamanan.



### Keamanan cadangan



Simpan setidaknya dua salinan dari setiap frasa pemulihan di atas kertas, disimpan di lokasi yang terpisah secara geografis. Untuk jumlah yang besar, pertimbangkan untuk mengukirnya dengan logam yang tahan bencana. Jangan pernah menyimpan frasa ini pada perangkat yang terhubung ke Internet, dan jangan pernah memotretnya.



Untuk multi-sig Vault, simpan juga file konfigurasi (Wallet Recovery File), yang berisi kunci publik yang berpartisipasi dan struktur vault. File ini, digabungkan dengan frasa pemulihan kunci, memungkinkan wallet untuk dibangun kembali pada perangkat lunak yang kompatibel seperti Sparrow atau Specter.



## Keuntungan dan keterbatasan



### Sorotan





- Aplikasi khusus Bitcoin mengurangi kompleksitas dan risiko
- Integrasi asli Vaults multisig dengan panduan langkah demi langkah
- Dukungan perangkat keras wallet yang diperluas (Tapsigner, Coldcard, Ledger, Jade, dll.)
- Manajemen lanjutan UTXO dan kontrol koin
- Dapat dihubungkan ke server Electrum pribadi
- Kode sumber yang terbuka dan dapat diaudit



### Kendala yang perlu dipertimbangkan





- Interface terutama dalam bahasa Inggris
- Beberapa fitur premium (Cloud Backup, Assisted Server) memerlukan peningkatan
- Konfigurasi Multisig memerlukan pelatihan awal



## Kesimpulan



Bitcoin Keeper menonjol sebagai solusi yang dapat diskalakan untuk mengelola bitcoin Anda. Pendekatannya yang progresif, mulai dari wallet yang sederhana hingga Vault multi-tanda tangan, berarti keamanan dapat ditingkatkan seiring dengan perubahan kebutuhan. Kemampuan untuk mengintegrasikan dompet perangkat keras dengan mudah seperti Tapsigner membuka jalan untuk konfigurasi yang kuat tanpa kerumitan yang berlebihan.



Orientasi khusus bitcoin, kode sumber terbuka, dan penghormatan terhadap privasi menjadikannya pilihan yang selaras dengan nilai-nilai inti ekosistem Bitcoin.



Tutorial ini mencakup fitur-fitur penting Bitcoin Keeper dalam versi gratisnya. Aplikasi ini juga menawarkan fitur-fitur premium (Cloud Backup, Assisted Server Backup, Canary Wallets) yang akan menjadi subjek dari sebuah tutorial khusus. Dalam panduan yang akan datang, kami juga akan menjelajahi fitur Perencanaan Warisan, yang memungkinkan Anda untuk mempersiapkan pengiriman bitcoin kepada orang yang Anda cintai, berkat Brankas yang Disempurnakan dan dokumen yang menyertainya yang terintegrasi ke dalam aplikasi.



## Sumber daya





- Situs web resmi: [bitcoinkeeper.app](https://bitcoinkeeper.app)
- Pusat Bantuan: [help.bitcoinkeeper.app](https://help.bitcoinkeeper.app)
- Kode sumber: [github.com/bithyve/bitcoin-keeper](https://github.com/bithyve/bitcoin-keeper)
- Telegram : [t.me/BitcoinKeeper](https://t.me/BitcoinKeeper)
- Twitter/X: [@bitcoinkeeper_](https://x.com/bitcoinkeeper_)