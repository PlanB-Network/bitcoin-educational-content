---
name: Desktop Spectre
description: Kelola portofolio Bitcoin multi-tanda tangan Anda dalam kedaulatan total dengan node Anda sendiri
---

![cover](assets/cover.webp)



Specter Desktop adalah sebuah aplikasi open source (lisensi MIT) yang dikembangkan oleh Cryptoadvance sejak tahun 2019 yang memfasilitasi pengelolaan dompet Bitcoin dengan dompet perangkat keras Anda (Ledger, Trezor, Coldcard, BitBox02, Passport, dll.) dan infrastruktur Bitcoin Anda sendiri (Bitcoin Core node atau Electrum server). Aplikasi ini unggul terutama dalam konfigurasi multi-tanda tangan, memungkinkan Anda untuk mengamankan jumlah besar dengan mendistribusikan kekuatan penandatanganan di antara beberapa dompet perangkat keras independen.



**Dalam tutorial ini, Anda akan mempelajari cara untuk:**




- Instal dan konfigurasikan Specter Desktop di komputer Anda (Windows, macOS, atau Linux)
- Hubungkan Specter ke server Electrum (kita akan menggunakan Umbrel dalam contoh ini)
- Membuat wallet sederhana dengan perangkat keras wallet (Coldcard)
- Menerima dan mengirim bitcoin dengan kedaulatan penuh
- Menyiapkan wallet multisignature 2-on-3 dengan beberapa dompet perangkat keras
- Instal Specter pada server Umbrel (bonus lanjutan)



Semua transaksi Anda akan divalidasi secara lokal melalui infrastruktur Anda sendiri, tanpa mengirimkan informasi apa pun ke server eksternal, menjamin kerahasiaan dan kedaulatan keuangan Anda. Selalu periksa transaksi pada layar perangkat keras wallet Anda sebelum menandatangani.



## Unduh dan pemasangan



Kunjungi situs web resmi Specter Desktop untuk mengunduh aplikasi ini.



![Page d'accueil Specter](assets/fr/01.webp)



Pada halaman pengunduhan, pilih versi yang sesuai dengan sistem operasi Anda: macOS, Windows, atau Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



Setelah diunduh, instal aplikasi sesuai dengan petunjuk yang biasa diberikan oleh sistem operasi Anda. Untuk macOS, seret ikon ke dalam Aplikasi. Untuk Windows, jalankan penginstal. Untuk Linux, ikuti petunjuk paket.



## Konfigurasi awal



Pada saat pertama kali diluncurkan, Specter Desktop meminta Anda untuk memilih jenis koneksi. Anda dapat menyambung ke server Electrum atau ke node Bitcoin Core Anda sendiri.



![Choix du type de connexion](assets/fr/03.webp)



Dalam contoh ini, kita akan menggunakan koneksi ke server Electrum yang berjalan pada Umbrel.



Untuk informasi lebih lanjut, silakan lihat tutorial Umbrel kami:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Opsi ini menawarkan sinkronisasi yang lebih cepat daripada Bitcoin Core. Jika Anda lebih suka, Anda dapat memilih "Bitcoin Core" dan mengonfigurasi koneksi ke node lokal Anda. Langkah-langkah berikut ini tetap sama, apa pun pilihan Anda.



Pilih "Koneksi Electrum" lalu pilih "Masukkan milik saya" untuk mengonfigurasi server Electrum Anda sendiri.



![Configuration Electrum](assets/fr/04.webp)



Masukkan alamat server Electrum Anda. Dalam kasus kami dengan Umbrel, alamatnya adalah `umbrel.local` dengan port `50001`. Klik pada "Connect" untuk membuat koneksi.



Setelah terhubung, layar selamat datang akan muncul, dengan daftar periksa untuk membantu Anda memulai. Anda sekarang perlu menambahkan dompet perangkat keras Anda.



![Écran d'accueil](assets/fr/05.webp)



## Menambahkan perangkat keras wallet



Pada menu sebelah kiri, klik "Tambah perangkat" untuk menambahkan perangkat keras wallet Anda.



Specter Desktop mendukung banyak dompet perangkat keras: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault, dan masih banyak lagi.



Jika Anda ingin mempelajari lebih lanjut, lihatlah tutorial perangkat keras wallet kami.



![Sélection du type de hardware wallet](assets/fr/06.webp)



Pilih perangkat keras wallet Anda. Dalam contoh ini, kami menggunakan Coldcard MK4.



Di bawah ini Anda akan menemukan tutorial kami untuk perangkat keras wallet ini:



https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

Untuk Coldcard, Anda perlu mengekspor kunci publik dari perangkat keras wallet baik melalui koneksi USB atau kartu microSD.



![Import des clés du Coldcard](assets/fr/07.webp)



Ikuti instruksi yang ditampilkan untuk mengekspor kunci dari Coldcard Anda. Beri nama perangkat keras wallet Anda (di sini "MK4 Tuto"). Setelah kunci diimpor, Anda bisa membuat wallet dengan satu kunci, atau menambahkan dompet perangkat keras lain untuk wallet multi-tanda tangan.



![Dispositif ajouté](assets/fr/08.webp)



## Pembuatan portofolio



Setelah menambahkan perangkat keras wallet Anda, klik "Buat wallet kunci tunggal" untuk membuat wallet dengan tanda tangan tunggal.



Beri nama portofolio Anda (misalnya "Wallet untuk tuto") dan pilih jenis alamat. Pilih "Segwit" untuk menggunakan alamat bech32 asli yang mengoptimalkan biaya transaksi.



![Configuration du portefeuille](assets/fr/09.webp)



Setelah portofolio Anda dibuat, Specter menawarkan untuk menyimpan file PDF cadangan yang berisi semua informasi publik yang diperlukan untuk memulihkan portofolio Anda (deskriptor, kunci publik yang diperluas). File ini tidak berisi kunci pribadi Anda.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Menerima bitcoin



Untuk menerima bitcoin, pilih wallet Anda di menu sebelah kiri, lalu klik tab "Terima".



Spectre secara otomatis menghasilkan alamat penerimaan baru dengan kode QR.



![Génération d'une adresse de réception](assets/fr/11.webp)



Anda dapat menyalin alamat atau memindai kode QR. Selalu periksa alamat pada layar perangkat keras wallet Anda sebelum memberikannya kepada siapa pun.



## Melihat riwayat dan alamat



Setelah Anda menerima bitcoin, Anda bisa melihat transaksi Anda di tab "Transaksi".



![Historique des transactions](assets/fr/12.webp)



Tab "Alamat" memungkinkan Anda melihat semua alamat yang dihasilkan oleh portofolio Anda, dengan status penggunaan dan jumlah yang terkait.



![Liste des adresses](assets/fr/13.webp)



## Kirim bitcoin



Untuk mengirim bitcoin, klik tab "Kirim". Masukkan alamat penerima, jumlah yang akan dikirim, dan centang opsi lanjutan jika Anda ingin memilih UTXO (kontrol koin) secara manual.



![Création d'une transaction](assets/fr/14.webp)



Klik pada "Buat Transaksi yang Tidak Ditandatangani" untuk membuat transaksi. Specter kemudian akan meminta Anda untuk menandatangani transaksi dengan perangkat keras wallet Anda.



![Signature de la transaction](assets/fr/15.webp)



Jika Anda menggunakan Coldcard, Anda akan memiliki pilihan untuk menandatangani melalui USB atau menggunakan kartu microSD (celah udara). Konfirmasikan transaksi pada layar perangkat keras wallet Anda, dengan memeriksa alamat tujuan dan jumlahnya dengan cermat.



Setelah transaksi ditandatangani, Anda dapat menyiarkannya di jaringan Bitcoin.



![Options de diffusion](assets/fr/16.webp)



Klik "Kirim transaksi" untuk mengirim transaksi. Specter akan mengonfirmasi bahwa transaksi Anda telah terkirim, dan Anda bisa melacak statusnya di tab Transaksi.



![Diffusion de la transaction](assets/fr/17.webp)



## Membuat dan menggunakan portofolio multi-tanda tangan



Salah satu aset utama Specter Desktop adalah kemampuannya untuk menyederhanakan pengelolaan portofolio multi-tanda tangan. Multisig wallet membutuhkan beberapa tanda tangan untuk mengesahkan sebuah transaksi, sehingga menghilangkan satu titik kegagalan. Konfigurasi 2-on-3, misalnya, membutuhkan dua tanda tangan dari tiga dompet perangkat keras yang terpisah untuk memvalidasi pengeluaran apa pun.



Untuk membuat multisig wallet, mulailah dengan menambahkan semua dompet perangkat keras penandatanganan melalui "Tambah perangkat". Pada contoh ini, kita akan menggunakan tiga dompet perangkat keras yang berbeda: Coldcard MK4 (sudah ditambahkan sebelumnya), Passport, dan Ledger. Diversifikasi produsen ini memperkuat keamanan dengan menghindari ketergantungan pada satu rantai pasokan atau firmware.



Berikut ini tautan ke tutorial Ledger dan Passport:



https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Tambahkan Passport dengan menamai perangkat keras wallet (mis. "Passport multi") dan mengimpor kuncinya melalui kartu microSD atau kode QR. Kemudian klik "Lanjutkan" untuk melanjutkan.



![Ajout du Passport](assets/fr/23.webp)



Kemudian tambahkan Ledger dengan menghubungkannya melalui USB dan membuka aplikasi Bitcoin pada perangkat keras wallet. Beri nama (misalnya "ledger multi") dan klik "Get via USB" lalu "Continue" untuk mengimpor kunci publiknya.



![Ajout du Ledger](assets/fr/24.webp)



Setelah Anda mendaftarkan tiga dompet perangkat keras Anda di Specter, klik "Add wallet" dan pilih opsi "Multiple Signature" untuk membuat wallet dengan banyak tanda tangan.



![Choix du type de wallet](assets/fr/25.webp)



Pilih tiga dompet perangkat keras yang ingin Anda sertakan dalam kuorum multisignature Anda: MK4 Tuto, Paspor multi dan buku besar multi. Klik "Lanjutkan" untuk melanjutkan ke langkah berikutnya.



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Pilih konfigurasi multi-tanda tangan Anda. Pilih "Segwit" sebagai jenis alamat untuk mendapatkan manfaat dari biaya yang dioptimalkan. Parameter "Tanda Tangan yang Dibutuhkan untuk Mengesahkan Transaksi (m dari 3)" memungkinkan Anda menentukan ambang batas: untuk konfigurasi 2 lawan 3, 2 tanda tangan diperlukan. Setiap perangkat keras wallet menampilkan kunci multisig yang sesuai. Klik "Buat wallet" untuk menyelesaikan pembuatan.



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



Portofolio multisignature "Multi tuto" Anda sekarang telah dibuat. Specter segera merekomendasikan agar Anda menyimpan file PDF cadangan yang berisi deskriptor portofolio. Klik "Simpan PDF Cadangan" untuk mengunduh file penting ini.



![Wallet multisig créé](assets/fr/28.webp)



Specter juga memungkinkan Anda mengekspor informasi wallet ke setiap dompet perangkat keras Anda melalui kode QR atau file. Hal ini memungkinkan dompet perangkat keras tertentu (seperti Coldcard atau Passport) untuk menyimpan konfigurasi multisig secara langsung di dalam memorinya.



Untuk Passport, buka kunci perangkat Anda kemudian buka "Kelola Akun" > "Hubungkan Wallet" > "Spectre" > "Multisig" > "Kode QR", lalu pindai kode QR yang dihasilkan oleh Spectre. Passport Anda kemudian akan meminta Anda untuk memindai alamat penerima dari wallet untuk memvalidasi konfigurasi multisig.



Untuk MK4, colokkan ke PC Anda dan buka kuncinya. Kemudian klik "Simpan file Tuto MK4" dan simpan file tersebut ke MK4 Anda. Saat berikutnya Anda memasukkan perangkat keras wallet Anda, MK4 akan menggunakan file ini untuk menyelesaikan konfigurasi multisig.



![Export vers les hardware wallets](assets/fr/29.webp)



Sebagai informasi, Anda dapat mengakses cadangan kapan saja dari tab "Pengaturan" pada portofolio Anda, lalu "Ekspor":



![Accès au backup PDF](assets/fr/30.webp)



Penggunaan sehari-hari tetap serupa dengan wallet sederhana: Anda menerima alamat penerima seperti biasa. Untuk mengirim bitcoin, buka tab "Kirim", masukkan alamat penerima dan jumlahnya, lalu klik "Buat Transaksi Tidak Ditandatangani".



![Création d'une transaction multisig](assets/fr/31.webp)



Specter membuat PSBT (Partially Signed Bitcoin Transaction) dan menampilkan "Mendapatkan 0 dari 2 tanda tangan". Sekarang Anda harus menandatangani dengan setidaknya dua dari tiga dompet perangkat keras Anda. Klik pada perangkat keras wallet pertama (misalnya "MK4 Tuto") untuk menandatangani dengan Coldcard Anda, kemudian pada perangkat keras kedua (misalnya "Passport multi") untuk mendapatkan tanda tangan kedua yang diperlukan.



![Signature de la transaction](assets/fr/32.webp)



Setelah Anda mendapatkan 2 tanda tangan yang diperlukan (antarmuka menampilkan "Mendapatkan 2 dari 2 tanda tangan" dan "Transaksi siap dikirim"), klik "Kirim Transaksi" untuk menyiarkan transaksi di jaringan Bitcoin.



![Transaction prête à être diffusée](assets/fr/33.webp)



Pendekatan multi-tanda tangan ini sangat cocok untuk perusahaan (beberapa manajer perlu menyetujui pengeluaran), keluarga (perlindungan warisan multi-generasi), atau individu yang mengelola dana dalam jumlah besar (distribusi geografis dompet perangkat keras untuk menahan bencana lokal).



### Pentingnya pencadangan multisignature



**Harap diperhatikan**: mencadangkan portofolio multisig pada dasarnya berbeda dengan mencadangkan portofolio tunggal. Frasa pemulihan Anda (frasa seed) saja tidak cukup untuk memulihkan portofolio multisig. Anda juga harus mencadangkan **output descriptor** (output descriptor), yang berisi informasi konfigurasi untuk portofolio multisig Anda.



output descriptor memiliki data penting: kunci publik yang diperluas (xpubs) dari setiap penandatangan bersama, ambang batas tanda tangan (2-on-3 pada contoh kita), jenis skrip yang digunakan (asli, bersarang, atau Segwit lama), dan jalur pintas untuk setiap perangkat keras wallet. Tanpa deskriptor ini, bahkan jika Anda memiliki dua dari tiga frasa pemulihan, Anda tidak akan dapat membangun kembali wallet atau mengakses bitcoin Anda. Deskriptor ini memungkinkan perangkat lunak Anda untuk mengetahui bagaimana cara menggabungkan kunci publik ke alamat generate dan Bitcoin yang sesuai dengan dana Anda.



Specter Desktop secara otomatis menghasilkan file PDF cadangan saat Anda membuat portofolio multisig. PDF ini berisi deskriptor lengkap, sidik jari setiap perangkat keras wallet, dan semua informasi publik yang diperlukan untuk pemulihan. **File ini tidak berisi kunci pribadi Anda** dan oleh karena itu tidak dengan sendirinya memungkinkan Anda untuk membelanjakan bitcoin Anda, tetapi memungkinkan siapa pun yang mengaksesnya untuk melihat riwayat transaksi dan saldo lengkap Anda.



Untuk mencadangkan konfigurasi multisignature Anda dengan benar, ikuti prosedur berikut: setelah membuat portofolio Anda, klik tab "Pengaturan", lalu "Ekspor" dan pilih "Simpan Cadangan PDF". Buat beberapa salinan PDF ini: cetak setidaknya dua salinan di atas kertas, dan juga simpan salinan digital terenkripsi. Simpan satu salinan PDF dengan setiap frasa pemulihan Anda, di lokasi yang terpisah secara geografis.



Ukirlah frasa pemulihan Anda pada pelat logam yang tahan api dan tahan air untuk menjamin umurnya yang panjang. Jangan pernah meremehkan pentingnya cadangan ini: jika Anda kehilangan folder `~/.specter` di komputer DAN Anda kehilangan salah satu dompet perangkat keras tanpa cadangan deskriptor, semua dana Anda akan hilang secara permanen, bahkan dengan konfigurasi 2-on-3. Redundansi multi-tanda tangan melindungi dari kehilangan perangkat keras wallet, namun hanya jika anda sudah membuat cadangan deskriptor wallet anda dengan benar.



## Keuntungan dan keterbatasan Specter Desktop



**Manfaat**: Kerahasiaan yang optimal dengan validasi lokal yang lengkap tanpa server pihak ketiga. Fleksibilitas multisignature untuk konfigurasi tingkat lanjut (perusahaan, keluarga, perorangan). Dukungan perangkat keras wallet yang luas dengan interoperabilitas penuh (USB dan celah udara).



**Keterbatasan**: Kurva pembelajaran yang signifikan pada konsep Bitcoin tingkat lanjut (UTXO, deskriptor, jalur derivasi).



## Praktik terbaik



Selalu periksa alamat dan jumlah pada layar perangkat keras wallet Anda sebelum validasi, untuk melindungi diri Anda dari malware.



Pisahkan cadangan PDF dari berkas Anda. Deskriptor publik ini dapat disimpan di brankas bank atau cloud terenkripsi, sehingga memudahkan pemulihan tanpa mengekspos kunci pribadi Anda.



Uji pemulihan pada jumlah token sebelum menggunakan portofolio Anda dengan dana besar. Buat, uji, hapus, dan pulihkan untuk memvalidasi prosedur Anda.



Selalu perbarui Specter dan firmware Anda. Mendistribusikan penandatangan bersama multi-tanda tangan Anda secara geografis (rumah/kantor/dekatnya) untuk menahan bencana lokal. Gunakan label deskriptif untuk memfasilitasi akuntansi dan pengembalian pajak.



## Bonus: Instalasi pada server Bitcoin (Umbrel, RaspiBlitz, Start9)



Jika Anda sudah memiliki server Bitcoin seperti Umbrel, RaspiBlitz, MyNode atau Start9, Anda bisa menginstal Specter Desktop langsung dari toko aplikasi mereka. Pendekatan ini menawarkan beberapa keuntungan yang signifikan: aplikasi secara otomatis mengkonfigurasi dirinya sendiri dengan node Bitcoin Core lokal Anda, tetap dapat diakses 24/7 melalui antarmuka web dari perangkat apa pun di jaringan Anda, dan Anda bahkan dapat mengaksesnya dengan aman dari jarak jauh melalui Tor. Seluruh infrastruktur Bitcoin Anda terpusat pada satu server khusus, menyederhanakan manajemen dan memperkuat kedaulatan Anda.



### Instalasi dari Toko Aplikasi Umbrel



Dari antarmuka Umbrel Anda, buka App Store dan cari Specter Desktop. Klik "Instal" untuk meluncurkan instalasi.



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



Setelah instalasi selesai, buka Specter Desktop pada Umbrel Anda. Layar selamat datang akan meminta Anda untuk memilih jenis koneksi Anda. Jika Anda menggunakan Specter pada Umbrel Anda, klik "Perbarui pengaturan" untuk mengonfigurasi koneksi.



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



Pilih "Remote Specter USB connection" untuk mengaktifkan penggunaan dompet perangkat keras USB yang terhubung ke komputer lokal Anda ketika menggunakan Specter pada server Umbrel jarak jauh.



![Configuration Remote Specter USB](assets/fr/20.webp)



Ikuti petunjuk yang ditampilkan untuk mengonfigurasi HWI Bridge. Anda perlu mengakses pengaturan jembatan perangkat dan menambahkan domain `http://umbrel.local:25441` ke daftar putih. Klik "Update" untuk menyimpan konfigurasi.



![HWI Bridge Settings](assets/fr/21.webp)



Jika Anda juga ingin menggunakan dompet perangkat keras USB dari komputer lokal Anda, unduh aplikasi Specter Desktop ke komputer Anda dan atur ke "Ya, saya menjalankan Specter dari jarak jauh". Klik "Simpan" untuk menyelesaikan konfigurasi.



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## Kesimpulan



Specter Desktop mendemokratisasi konfigurasi Bitcoin tingkat lanjut, membuat multisignature dapat diakses tanpa mengorbankan kedaulatan atau kerahasiaan Anda. Bagi pengguna yang mengelola sejumlah besar uang, ini mengubah praktik institusional menjadi solusi yang dapat digunakan oleh perorangan.



Meskipun aplikasi ini membutuhkan investasi awal dalam infrastruktur dan pembelajaran, aplikasi ini menawarkan kedaulatan penuh: kendali atas infrastruktur validasi, kepemilikan fisik atas kunci, dan transaksi yang bebas dari pengawasan pihak ketiga. Baik Anda seorang individu yang mengamankan tabungan Anda, keluarga yang membuat brankas multi-generasi, atau perusahaan yang mengelola arus kas, Specter Desktop adalah alat referensi untuk merekonsiliasi keamanan maksimum dan kedaulatan mutlak.



## Sumber daya



### Dokumentasi resmi




- [Situs web resmi Specter Desktop](https://specter.solutions/desktop/)
- [Kode sumber GitHub](https://github.com/cryptoadvance/specter-desktop)
- [Dokumentasi lengkap](https://docs.specter.solutions/)



### Komunitas dan dukungan




- [Grup Komunitas Telegram Specter](https://t.me/spectersupport)
- [Forum diskusi Reddit](https://reddit.com/r/specterdesktop/)
- [Laporan bug GitHub](https://github.com/cryptoadvance/specter-desktop/issues)