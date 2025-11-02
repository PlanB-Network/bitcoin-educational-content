---
name: Desktop Spectre
description: Kelola portofolio Bitcoin multi-tanda tangan Anda dalam kedaulatan total dengan node Anda sendiri
---

![cover](assets/cover.webp)



Specter Desktop adalah sebuah aplikasi open source (lisensi MIT) yang dikembangkan oleh Cryptoadvance sejak tahun 2019 yang memfasilitasi pengelolaan dompet Bitcoin dengan dompet perangkat keras Anda (Ledger, Trezor, Coldcard, BitBox02, Passport, dll.) dan infrastruktur Bitcoin Anda sendiri (Bitcoin core node atau Electrum Server). Aplikasi ini unggul terutama dalam konfigurasi multi-tanda tangan, memungkinkan Anda untuk mengamankan jumlah besar dengan mendistribusikan kekuatan penandatanganan di antara beberapa dompet perangkat keras independen.



**Dalam tutorial ini, Anda akan mempelajari cara untuk:**




- Instal dan konfigurasikan Specter Desktop di komputer Anda (Windows, macOS, atau Linux)
- Hubungkan Specter ke Electrum Server (kita akan menggunakan Umbrel dalam contoh ini)
- Membuat Wallet sederhana dengan Hardware Wallet (Coldcard)
- Menerima dan mengirim bitcoin dengan kedaulatan penuh
- Menyiapkan Wallet multisignature 2-on-3 dengan beberapa dompet perangkat keras
- Instal Specter pada server Umbrel (bonus lanjutan)



Semua transaksi Anda akan divalidasi secara lokal melalui infrastruktur Anda sendiri, tanpa mengirimkan informasi apa pun ke server eksternal, sehingga menjamin kerahasiaan dan kedaulatan finansial Anda. Selalu periksa transaksi pada layar Hardware Wallet Anda sebelum menandatangani.



## Unduh dan pemasangan



Kunjungi situs web resmi Specter Desktop untuk mengunduh aplikasi ini.



![Page d'accueil Specter](assets/fr/01.webp)



Pada halaman pengunduhan, pilih versi yang sesuai dengan sistem operasi Anda: macOS, Windows, atau Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



Setelah diunduh, instal aplikasi sesuai dengan petunjuk yang biasa diberikan oleh sistem operasi Anda. Untuk macOS, seret ikon ke dalam Aplikasi. Untuk Windows, jalankan penginstal. Untuk Linux, ikuti petunjuk paket.



## Konfigurasi awal



Pada saat pertama kali diluncurkan, Specter Desktop meminta Anda untuk memilih jenis koneksi. Anda dapat menyambung ke Electrum Server atau ke node Bitcoin core Anda sendiri.



![Choix du type de connexion](assets/fr/03.webp)



Dalam contoh ini, kita akan menggunakan koneksi ke Electrum Server yang berjalan pada Umbrel.



Untuk informasi lebih lanjut, silakan lihat tutorial Umbrel kami:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Opsi ini menawarkan sinkronisasi yang lebih cepat daripada Bitcoin core. Jika Anda lebih suka, Anda dapat memilih "Bitcoin core" dan mengonfigurasi koneksi ke node lokal Anda. Langkah-langkah berikut ini tetap sama, apa pun pilihan Anda.



Pilih "Koneksi Electrum" lalu pilih "Masukkan milik saya" untuk mengonfigurasi Electrum Server Anda sendiri.



![Configuration Electrum](assets/fr/04.webp)



Masukkan Address dari Electrum Server Anda. Dalam kasus kami dengan Umbrel, Address akan menjadi `umbrel.local` dengan port `50001`. Klik "Connect" untuk membuat sambungan.



Setelah terhubung, layar selamat datang akan muncul, dengan daftar periksa untuk membantu Anda memulai. Anda sekarang perlu menambahkan dompet perangkat keras Anda.



![Écran d'accueil](assets/fr/05.webp)



## Menambahkan Hardware Wallet



Pada menu sebelah kiri, klik "Tambah perangkat" untuk menambahkan Hardware Wallet Anda.



Specter Desktop mendukung banyak dompet perangkat keras: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault, dan masih banyak lagi.



Jika Anda ingin mempelajari lebih lanjut, lihatlah tutorial Hardware Wallet kami.



![Sélection du type de hardware wallet](assets/fr/06.webp)



Pilih Hardware Wallet Anda. Dalam contoh ini, kami menggunakan Coldcard MK4.



Silakan temukan tutorial kami di bawah ini untuk Hardware Wallet ini:



https://planb.network/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

Untuk Coldcard, Anda perlu mengekspor kunci publik dari Hardware Wallet baik melalui koneksi USB atau kartu microSD.



![Import des clés du Coldcard](assets/fr/07.webp)



Ikuti instruksi yang ditampilkan untuk mengekspor kunci dari Coldcard Anda. Berikan nama pada Hardware Wallet Anda (di sini "MK4 Tuto"). Setelah kunci diimpor, Anda bisa membuat Wallet dengan satu kunci, atau menambahkan dompet perangkat keras lain untuk Wallet multi-tanda tangan.



![Dispositif ajouté](assets/fr/08.webp)



## Pembuatan portofolio



Setelah menambahkan Hardware Wallet Anda, klik "Buat kunci tunggal Wallet" untuk membuat Wallet dengan tanda tangan tunggal.



Beri nama portofolio Anda (misalnya "Wallet untuk tuto") dan pilih jenis Address. Pilih "SegWit" untuk menggunakan alamat asli BECH32, yang mengoptimalkan biaya transaksi.



![Configuration du portefeuille](assets/fr/09.webp)



Setelah portofolio Anda dibuat, Specter menawarkan untuk menyimpan file PDF cadangan yang berisi semua informasi publik yang diperlukan untuk memulihkan portofolio Anda (deskriptor, kunci publik yang diperluas). File ini tidak berisi kunci pribadi Anda.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Menerima bitcoin



Untuk menerima bitcoin, pilih Wallet Anda di menu sebelah kiri, lalu klik tab "Terima".



Spectre secara otomatis menghasilkan penerimaan baru Address dengan kode QR.



![Génération d'une adresse de réception](assets/fr/11.webp)



Anda dapat menyalin Address atau memindai kode QR. Selalu periksa Address pada layar Hardware Wallet Anda sebelum memberikannya kepada siapa pun.



## Melihat riwayat dan alamat



Setelah Anda menerima bitcoin, Anda bisa melihat transaksi Anda di tab "Transaksi".



![Historique des transactions](assets/fr/12.webp)



Tab "Alamat" memungkinkan Anda melihat semua alamat yang dihasilkan oleh portofolio Anda, dengan status penggunaan dan jumlah yang terkait.



![Liste des adresses](assets/fr/13.webp)



## Kirim bitcoin



Untuk mengirim bitcoin, klik tab "Kirim". Masukkan Address penerima, jumlah yang akan dikirim, dan centang opsi lanjutan jika Anda ingin memilih UTXO secara manual (kontrol Coin).



![Création d'une transaction](assets/fr/14.webp)



Klik "Buat Transaksi yang Belum Ditandatangani" untuk membuat transaksi. Specter kemudian akan meminta Anda untuk menandatangani transaksi dengan Hardware Wallet Anda.



![Signature de la transaction](assets/fr/15.webp)



Jika Anda menggunakan Coldcard, Anda akan memiliki pilihan untuk menandatangani melalui USB atau menggunakan kartu microSD (air-gapped). Konfirmasikan transaksi pada layar Hardware Wallet Anda, dengan memeriksa dengan cermat Address tujuan dan jumlahnya.



Setelah transaksi ditandatangani, Anda dapat menyiarkannya di jaringan Bitcoin.



![Options de diffusion](assets/fr/16.webp)



Klik "Kirim transaksi" untuk mengirim transaksi. Specter akan mengonfirmasi bahwa transaksi Anda telah terkirim, dan Anda bisa melacak statusnya di tab Transaksi.



![Diffusion de la transaction](assets/fr/17.webp)



## Membuat dan menggunakan portofolio multi-tanda tangan



Salah satu aset utama Specter Desktop adalah kemampuannya untuk menyederhanakan pengelolaan portofolio multi-tanda tangan. Multisig Wallet membutuhkan beberapa tanda tangan untuk mengesahkan sebuah transaksi, sehingga menghilangkan satu titik kegagalan. Konfigurasi 2-on-3, misalnya, membutuhkan dua tanda tangan dari tiga dompet perangkat keras yang terpisah untuk memvalidasi setiap pengeluaran.



Untuk membuat Multisig Wallet, mulailah dengan menambahkan semua dompet perangkat keras penandatangan melalui "Tambah perangkat". Dalam contoh ini, kita akan menggunakan tiga dompet perangkat keras yang berbeda: Coldcard MK4 (sudah ditambahkan sebelumnya), Passport, dan Ledger. Diversifikasi produsen ini memperkuat keamanan dengan menghindari ketergantungan pada satu rantai atau firmware Supply.



Berikut ini tautan ke tutorial Ledger dan Passport:



https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Tambahkan Passport dengan menamai Hardware Wallet (mis. "Passport multi") dan mengimpor kuncinya melalui kartu microSD atau kode QR. Kemudian klik "Lanjutkan" untuk melanjutkan.



![Ajout du Passport](assets/fr/23.webp)



Kemudian tambahkan Ledger dengan menghubungkannya melalui USB dan membuka aplikasi Bitcoin pada Hardware Wallet. Beri nama (misalnya "Ledger multi") dan klik "Dapatkan melalui USB" lalu "Lanjutkan" untuk mengimpor kunci publiknya.



![Ajout du Ledger](assets/fr/24.webp)



Setelah Anda mendaftarkan tiga dompet perangkat keras Anda di Specter, klik "Add Wallet" dan pilih opsi "Multiple Signature" untuk membuat Wallet dengan banyak tanda tangan.



![Choix du type de wallet](assets/fr/25.webp)



Pilih tiga dompet perangkat keras yang ingin Anda sertakan dalam kuorum multisignature Anda: MK4 Tuto, Passport multi dan Ledger multi. Klik "Lanjutkan" untuk melanjutkan ke langkah berikutnya.



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Pilih konfigurasi multi-tanda tangan Anda. Pilih "SegWit" sebagai tipe Address untuk mendapatkan manfaat dari biaya yang dioptimalkan. Parameter "Tanda Tangan yang Diperlukan untuk Mengesahkan Transaksi (m dari 3)" memungkinkan Anda menentukan ambang batas: untuk konfigurasi 2 lawan 3, 2 tanda tangan diperlukan. Setiap Hardware Wallet menampilkan kunci Multisig yang sesuai. Klik "Buat Wallet" untuk menyelesaikan pembuatan.



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



Portofolio multisignature "Multi tuto" Anda sekarang sudah dibuat. Specter segera merekomendasikan agar Anda menyimpan file PDF cadangan yang berisi portofolio Descriptor. Klik "Simpan Cadangan PDF" untuk mengunduh file penting ini.



![Wallet multisig créé](assets/fr/28.webp)



Specter juga memungkinkan Anda mengekspor informasi Wallet ke setiap dompet perangkat keras Anda melalui kode QR atau file. Hal ini memungkinkan dompet perangkat keras tertentu (seperti Coldcard atau Passport) untuk menyimpan konfigurasi Multisig secara langsung di dalam memorinya.



Untuk Passport, buka kunci perangkat Anda kemudian buka "Kelola Akun" > "Hubungkan Wallet" > "Spectre" > "Multisig" > "Kode QR", lalu pindai kode QR yang dihasilkan oleh Spectre. Passport Anda kemudian akan meminta Anda untuk memindai Address yang diterima dari Wallet untuk memvalidasi konfigurasi Multisig.



Untuk MK4, colokkan ke PC dan buka kuncinya. Kemudian klik "Simpan file Tuto MK4" dan simpan file tersebut ke MK4 Anda. Pada saat Anda menandatangani Hardware Wallet, MK4 akan menggunakan file ini untuk menyelesaikan konfigurasi Multisig.



![Export vers les hardware wallets](assets/fr/29.webp)



Sebagai informasi, Anda dapat mengakses cadangan kapan saja dari tab "Pengaturan" pada portofolio Anda, lalu "Ekspor":



![Accès au backup PDF](assets/fr/30.webp)



Penggunaan sehari-hari tetap serupa dengan Wallet sederhana: Anda menerima alamat penerima seperti biasa. Untuk mengirim bitcoin, buka tab "Kirim", masukkan Address penerima dan jumlahnya, lalu klik "Buat Transaksi Tidak Ditandatangani".



![Création d'une transaction multisig](assets/fr/31.webp)



Specter membuat PSBT (Partially Signed Bitcoin Transaction) dan menampilkan "Mendapatkan 0 dari 2 tanda tangan". Sekarang Anda harus menandatangani dengan setidaknya dua dari tiga dompet perangkat keras Anda. Klik pada Hardware Wallet pertama (misalnya "MK4 Tuto") untuk menandatangani dengan Coldcard Anda, kemudian pada yang kedua (misalnya "Passport multi") untuk mendapatkan tanda tangan kedua yang diperlukan.



![Signature de la transaction](assets/fr/32.webp)



Setelah Anda mendapatkan 2 tanda tangan yang diperlukan (Interface menampilkan "Mendapatkan 2 dari 2 tanda tangan" dan "Transaksi siap dikirim"), klik "Kirim Transaksi" untuk menyiarkan transaksi di jaringan Bitcoin.



![Transaction prête à être diffusée](assets/fr/33.webp)



Pendekatan multi-tanda tangan ini sangat cocok untuk perusahaan (beberapa manajer perlu menyetujui pengeluaran), keluarga (perlindungan warisan multi-generasi), atau individu yang mengelola dana dalam jumlah besar (distribusi geografis dompet perangkat keras untuk menahan bencana lokal).



### Pentingnya pencadangan multisignature



**Harap diperhatikan**: mencadangkan portofolio multi-tanda tangan pada dasarnya berbeda dengan mencadangkan portofolio tunggal. Frasa pemulihan Anda (frasa seed) saja tidak cukup untuk memulihkan portofolio Multisig. Anda juga harus mencadangkan **output descriptor** (output descriptor), yang berisi informasi konfigurasi untuk portofolio multi-tanda tangan Anda.



output descriptor mencakup data penting: kunci publik yang diperluas (xpubs) dari setiap penandatangan bersama, ambang batas tanda tangan (2-on-3 pada contoh kita), jenis skrip yang digunakan (SegWit asli, bersarang, atau warisan), dan jalur turunan untuk setiap Hardware Wallet. Tanpa Descriptor ini, bahkan jika Anda memiliki dua dari tiga frasa pemulihan, Anda tidak akan dapat membangun kembali Wallet atau mengakses bitcoin Anda. Descriptor memungkinkan perangkat lunak Anda untuk mengetahui bagaimana cara menggabungkan kunci publik ke generate dengan alamat Bitcoin yang sesuai dengan dana Anda.



Specter Desktop secara otomatis menghasilkan file PDF cadangan ketika Anda membuat portofolio Multisig. PDF ini berisi Descriptor yang lengkap, sidik jari setiap Hardware Wallet, dan semua informasi publik yang diperlukan untuk pemulihan. **File ini tidak berisi kunci pribadi Anda** dan oleh karena itu tidak dengan sendirinya memungkinkan Anda untuk membelanjakan bitcoin Anda, tetapi memungkinkan siapa pun yang mengaksesnya untuk melihat riwayat transaksi dan saldo lengkap Anda.



Untuk mencadangkan konfigurasi multisignature Anda dengan benar, ikuti prosedur berikut: setelah membuat portofolio Anda, klik tab "Pengaturan", lalu "Ekspor" dan pilih "Simpan Cadangan PDF". Buat beberapa salinan PDF ini: cetak setidaknya dua salinan di atas kertas, dan juga simpan salinan digital terenkripsi. Simpan satu salinan PDF dengan setiap frasa pemulihan Anda, di lokasi yang terpisah secara geografis.



Bakarlah frasa pemulihan Anda di atas pelat logam yang tahan api dan tahan air untuk menjamin keawetannya. Jangan pernah meremehkan pentingnya cadangan ini: jika Anda kehilangan folder `~/.specter` komputer DAN Anda kehilangan salah satu dompet perangkat keras Anda tanpa cadangan Descriptor, semua dana Anda akan hilang secara permanen, bahkan dengan konfigurasi 2-on-3. Redundansi multi-tanda tangan melindungi dari kehilangan Hardware Wallet, namun hanya jika Anda telah mencadangkan Wallet dan Descriptor dengan benar.



## Keuntungan dan keterbatasan Specter Desktop



**Manfaat**: Kerahasiaan yang optimal dengan validasi lokal yang lengkap tanpa server pihak ketiga. Fleksibilitas multisignature untuk konfigurasi tingkat lanjut (perusahaan, keluarga, perorangan). Dukungan Hardware Wallet yang luas dengan interoperabilitas penuh (USB dan celah udara).



**Keterbatasan**: Kurva pembelajaran yang signifikan pada konsep Bitcoin tingkat lanjut (UTXO, deskriptor, jalur derivasi).



## Praktik terbaik



Selalu periksa alamat dan jumlah pada layar Hardware Wallet Anda sebelum melakukan validasi, untuk melindungi diri Anda dari malware.



Pisahkan cadangan PDF dari berkas Anda. Deskriptor publik ini dapat disimpan di brankas bank atau cloud terenkripsi, sehingga memudahkan pemulihan tanpa mengekspos kunci pribadi Anda.



Uji pemulihan pada jumlah token sebelum menggunakan portofolio Anda dengan dana besar. Buat, uji, hapus, dan pulihkan untuk memvalidasi prosedur Anda.



Selalu perbarui Specter dan firmware Anda. Mendistribusikan penandatangan bersama multi-tanda tangan Anda secara geografis (rumah/kantor/dekatnya) untuk menahan bencana lokal. Gunakan label deskriptif untuk memfasilitasi akuntansi dan pengembalian pajak.



## Bonus: Instalasi pada server Bitcoin (Umbrel, RaspiBlitz, Start9)



Jika Anda sudah memiliki server Bitcoin seperti Umbrel, RaspiBlitz, MyNode atau Start9, Anda bisa menginstal Specter Desktop langsung dari toko aplikasi mereka. Pendekatan ini menawarkan beberapa keuntungan yang signifikan: aplikasi secara otomatis mengonfigurasi dirinya sendiri dengan node Bitcoin core lokal Anda, tetap dapat diakses 24/7 melalui web Interface dari perangkat apa pun di jaringan Anda, dan Anda bahkan dapat mengaksesnya dengan aman dari jarak jauh melalui Tor. Seluruh infrastruktur Bitcoin Anda terpusat pada satu server khusus, menyederhanakan manajemen dan memperkuat kedaulatan Anda.



### Instalasi dari Toko Aplikasi Umbrel



Dari Umbrel Interface Anda, buka App Store dan cari Specter Desktop. Klik "Instal" untuk meluncurkan instalasi.



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



Setelah instalasi selesai, buka Specter Desktop pada Umbrel Anda. Layar selamat datang akan meminta Anda untuk memilih jenis koneksi Anda. Jika Anda menggunakan Specter pada Umbrel Anda, klik "Perbarui pengaturan" untuk mengonfigurasi koneksi.



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



Pilih "Remote Specter USB connection (Koneksi USB Spectre jarak jauh)" untuk mengaktifkan penggunaan dompet perangkat keras USB yang terhubung ke komputer lokal Anda ketika menggunakan Spectre pada server Umbrel jarak jauh.



![Configuration Remote Specter USB](assets/fr/20.webp)



Ikuti petunjuk yang ditampilkan untuk mengonfigurasi HWI Bridge. Anda perlu mengakses pengaturan jembatan perangkat dan menambahkan domain `http://umbrel.local:25441` ke daftar putih. Klik "Update" untuk menyimpan konfigurasi.



![HWI Bridge Settings](assets/fr/21.webp)



Jika Anda juga ingin menggunakan dompet perangkat keras USB dari komputer lokal Anda, unduh aplikasi Specter Desktop ke komputer Anda dan atur ke "Ya, saya menjalankan Specter dari jarak jauh". Klik "Simpan" untuk menyelesaikan konfigurasi.



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## Kesimpulan



Specter Desktop mendemokratisasi konfigurasi Bitcoin tingkat lanjut, membuat multi-tanda tangan dapat diakses tanpa mengorbankan kedaulatan atau kerahasiaan. Bagi pengguna yang mengelola sejumlah besar uang, ini mengubah praktik institusional menjadi solusi yang dapat digunakan oleh individu pribadi.



Meskipun aplikasi ini membutuhkan investasi awal dalam infrastruktur dan pembelajaran, aplikasi ini menawarkan kedaulatan penuh: kendali atas infrastruktur validasi, kunci fisik Ownership, dan transaksi yang bebas dari pengawasan pihak ketiga. Baik Anda seorang individu yang mengamankan tabungan Anda, keluarga yang membuat brankas multi-generasi, atau perusahaan yang mengelola arus kas, Specter Desktop adalah alat referensi untuk merekonsiliasi keamanan maksimum dan kedaulatan mutlak.



## Sumber daya



### Dokumentasi resmi




- [Situs web resmi Specter Desktop](https://specter.solutions/desktop/)
- [Kode sumber GitHub](https://github.com/cryptoadvance/specter-desktop)
- [Dokumentasi lengkap](https://docs.specter.solutions/)



### Komunitas dan dukungan




- [Grup Komunitas Telegram Specter](https://t.me/spectersupport)
- [Forum diskusi Reddit](https://reddit.com/r/specterdesktop/)
- [Laporan bug GitHub](https://github.com/cryptoadvance/specter-desktop/issues)