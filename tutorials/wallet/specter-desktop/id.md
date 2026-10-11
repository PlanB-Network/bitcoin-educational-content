---
name: Specter Desktop
description: Kelola portofolio Bitcoin multi-tanda tangan dalam kedaulatan total dengan node kamu sendiri
---

![cover](assets/cover.webp)



Specter Desktop adalah aplikasi open-source (lisensi MIT) yang dikembangkan oleh Cryptoadvance sejak 2019, yang memudahkan pengelolaan dompet Bitcoin dengan hardware wallet kamu (Ledger, Trezor, Coldcard, BitBox02, Passport, dll.) dan infrastruktur Bitcoin milikmu sendiri (Bitcoin Core node atau Electrum server). Aplikasi ini unggul terutama dalam konfigurasi multisignature, memungkinkan kamu mengamankan jumlah besar dengan mendistribusikan kekuatan penandatanganan di antara beberapa hardware wallet independen.



**Dalam tutorial ini, kamu akan mempelajari cara untuk:**




- Instal dan konfigurasikan Specter Desktop di komputer kamu (Windows, macOS, atau Linux)  
- Hubungkan Specter ke server Electrum (dalam contoh ini kita akan menggunakan Umbrel)  
- Buat wallet sederhana dengan hardware wallet (Coldcard)  
- Terima dan kirim bitcoin dengan kedaulatan penuh  
- Siapkan wallet multisignature 2-of-3 dengan beberapa hardware wallet  
- Instal Specter pada server Umbrel (bonus lanjutan)  

Semua transaksi kamu akan divalidasi secara lokal melalui infrastruktur milikmu sendiri, tanpa mengirim informasi apa pun ke server eksternal, sehingga kerahasiaan dan kedaulatan keuangan tetap terjaga. Selalu periksa transaksi di layar hardware wallet sebelum menandatangani.

## Unduh dan pemasangan

Kunjungi situs web resmi Specter Desktop untuk mengunduh aplikasi ini.


![Page d'accueil Specter](assets/fr/01.webp)



Pada halaman pengunduhan, pilih versi yang sesuai dengan sistem operasi: macOS, Windows, atau Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



Setelah diunduh, instal aplikasi sesuai petunjuk yang biasanya diberikan oleh sistem operasi kamu. Untuk macOS, seret ikon ke folder Aplikasi. Untuk Windows, jalankan penginstal. Untuk Linux, ikuti petunjuk paket.

## Konfigurasi awal

Saat pertama kali diluncurkan, Specter Desktop akan meminta kamu memilih jenis koneksi. Kamu bisa menyambung ke server Electrum atau ke Bitcoin Core node milikmu sendiri.



![Choix du type de connexion](assets/fr/03.webp)



Dalam contoh ini, kita akan menggunakan koneksi ke server Electrum yang berjalan pada Umbrel.



Untuk informasi lebih lanjut, silakan lihat tutorial Umbrel kami:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Opsi ini menawarkan sinkronisasi lebih cepat dibandingkan Bitcoin Core. Jika kamu mau, kamu bisa memilih "Bitcoin Core" dan mengonfigurasi koneksi ke node lokal milikmu. Langkah-langkah berikut tetap sama, apa pun pilihanmu.

Pilih "Koneksi Electrum" lalu pilih "Masukkan milik saya" untuk mengonfigurasi server Electrum milikmu sendiri.



![Configuration Electrum](assets/fr/04.webp)



Masukkan alamat server Electrum kamu. Dalam contoh kami dengan Umbrel, alamatnya adalah `umbrel.local` dengan port `50001`. Klik "Connect" untuk membuat koneksi.

Setelah terhubung, layar selamat datang akan muncul, lengkap dengan daftar periksa untuk membantumu memulai. Sekarang kamu perlu menambahkan hardware wallet kamu.


![Écran d'accueil](assets/fr/05.webp)



## Menambahkan perangkat keras wallet



Di menu sebelah kiri, klik "Tambah perangkat" untuk menambahkan hardware wallet kamu.

Specter Desktop mendukung berbagai hardware wallet: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault, dan masih banyak lagi.

Jika kamu ingin mempelajari lebih lanjut, lihat tutorial hardware wallet kami.

![Sélection du type de hardware wallet](assets/fr/06.webp)



Pilih hardware wallet kamu. Dalam contoh ini, kita menggunakan Coldcard MK4.

Di bawah ini kamu akan menemukan tutorial kami untuk hardware wallet ini:



https://planb.academy/tutorials/wallet/hardware/coldcard-mk4-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

Untuk Coldcard, kamu perlu mengekspor kunci publik dari perangkat keras wallet baik melalui koneksi USB atau kartu microSD.



![Import des clés du Coldcard](assets/fr/07.webp)



Ikuti instruksi yang ditampilkan untuk mengekspor kunci dari Coldcard kamu. Beri nama hardware wallet kamu (di sini "MK4 Tuto"). Setelah kunci diimpor, kamu bisa membuat wallet dengan satu kunci, atau menambahkan hardware wallet lain untuk membuat wallet multisignature.



![Dispositif ajouté](assets/fr/08.webp)



## Pembuatan portofolio



Setelah menambahkan hardware wallet kamu, klik "Buat wallet kunci tunggal" untuk membuat wallet dengan tanda tangan tunggal.

Beri nama portofolio kamu (misalnya "Wallet untuk tuto") dan pilih jenis alamat. Pilih "Segwit" untuk menggunakan alamat bech32 asli yang mengoptimalkan biaya transaksi.

![Configuration du portefeuille](assets/fr/09.webp)


Setelah portofolio kamu dibuat, Specter menawarkan untuk menyimpan file PDF cadangan yang berisi semua informasi publik yang diperlukan untuk memulihkan portofolio kamu (descriptor, kunci publik yang diperluas). File ini tidak berisi kunci privat kamu.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Menerima bitcoin



Untuk menerima bitcoin, pilih wallet kamu di menu sebelah kiri, lalu klik tab "Terima".



Spectre secara otomatis menghasilkan alamat penerimaan baru dengan kode QR.



![Génération d'une adresse de réception](assets/fr/11.webp)



Kamu dapat menyalin alamat atau memindai kode QR. Selalu periksa alamat di layar hardware wallet sebelum memberikannya kepada siapa pun.

## Melihat riwayat dan alamat

Setelah kamu menerima bitcoin, kamu bisa melihat transaksi di tab "Transaksi".



![Historique des transactions](assets/fr/12.webp)



Tab "Alamat" memungkinkanmu melihat semua alamat yang dihasilkan oleh portofolio kamu, dengan status penggunaan dan jumlah yang terkait.



![Liste des adresses](assets/fr/13.webp)



## Kirim bitcoin


Untuk mengirim bitcoin, klik tab "Kirim". Masukkan alamat penerima, jumlah yang ingin dikirim, dan centang opsi lanjutan jika kamu ingin memilih UTXO (coin control) secara manual.

![Création d'une transaction](assets/fr/14.webp)



Klik pada "Buat Transaksi yang Tidak Ditandatangani" untuk membuat transaksi. Specter kemudian akan meminta kamu untuk menandatangani transaksi dengan perangkat keras wallet kamu.



![Signature de la transaction](assets/fr/15.webp)



Jika kamu menggunakan Coldcard, kamu bisa memilih untuk menandatangani melalui USB atau menggunakan kartu microSD (air-gapped). Konfirmasikan transaksi di layar hardware wallet kamu, periksa alamat tujuan dan jumlahnya dengan cermat.

Setelah transaksi ditandatangani, kamu bisa menyiarkannya ke jaringan Bitcoin.



![Options de diffusion](assets/fr/16.webp)



Klik "Kirim transaksi" untuk mengirim transaksi. Specter akan mengonfirmasi bahwa transaksi kamu telah terkirim, dan kamu bisa melacak statusnya di tab Transaksi.



![Diffusion de la transaction](assets/fr/17.webp)



## Membuat dan menggunakan portofolio multi-tanda tangan


Salah satu kekuatan utama Specter Desktop adalah kemampuannya menyederhanakan pengelolaan portofolio multisignature. Multisig wallet membutuhkan beberapa tanda tangan untuk mengesahkan transaksi, sehingga menghilangkan satu titik kegagalan. Konfigurasi 2-of-3, misalnya, memerlukan dua tanda tangan dari tiga hardware wallet yang terpisah untuk memvalidasi setiap pengeluaran.

Untuk membuat multisig wallet, mulai dengan menambahkan semua hardware wallet penandatangan melalui "Tambah perangkat". Dalam contoh ini, kita akan menggunakan tiga hardware wallet berbeda: Coldcard MK4 (sudah ditambahkan sebelumnya), Passport, dan Ledger. Diversifikasi produsen ini memperkuat keamanan dengan menghindari ketergantungan pada satu rantai pasokan atau firmware.

Berikut ini tautan ke tutorial Ledger dan Passport:



https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Tambahkan Passport dengan menamai perangkat keras wallet (mis. "Passport multi") dan mengimpor kuncinya melalui kartu microSD atau kode QR. Kemudian klik "Lanjutkan" untuk melanjutkan.



![Ajout du Passport](assets/fr/23.webp)



Kemudian tambahkan Ledger dengan menghubungkannya melalui USB dan membuka aplikasi Bitcoin pada perangkat keras wallet. Beri nama (misalnya "ledger multi") dan klik "Get via USB" lalu "Continue" untuk mengimpor kunci publiknya.



![Ajout du Ledger](assets/fr/24.webp)



Setelah kamu mendaftarkan tiga dompet perangkat keras kamu di Specter, klik "Add wallet" dan pilih opsi "Multiple Signature" untuk membuat wallet dengan banyak tanda tangan.



![Choix du type de wallet](assets/fr/25.webp)



Pilih tiga dompet perangkat keras yang ingin kamu sertakan dalam kuorum multisignature: MK4 Tuto, Paspor multi dan buku besar multi. Klik "Lanjutkan" untuk melanjutkan ke langkah berikutnya.



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Pilih konfigurasi multisignature kamu. Pilih "Segwit" sebagai jenis alamat untuk mendapatkan manfaat dari biaya yang dioptimalkan. Parameter "Tanda Tangan yang Dibutuhkan untuk Mengesahkan Transaksi (m dari 3)" memungkinkan kamu menentukan ambang batas: untuk konfigurasi 2-of-3, 2 tanda tangan diperlukan. Setiap hardware wallet menampilkan kunci multisig yang sesuai. Klik "Buat wallet" untuk menyelesaikan pembuatan.



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



Portofolio multisignature "Multi tuto" kamu sekarang telah dibuat. Specter segera merekomendasikan agar kamu menyimpan file PDF cadangan yang berisi deskriptor portofolio. Klik "Simpan PDF Cadangan" untuk mengunduh file penting ini.



![Wallet multisig créé](assets/fr/28.webp)



Specter juga memungkinkan kamu mengekspor informasi wallet ke setiap hardware wallet melalui kode QR atau file. Ini memungkinkan hardware wallet tertentu (seperti Coldcard atau Passport) untuk menyimpan konfigurasi multisig langsung di memorinya.

Untuk Passport, buka perangkat kamu lalu masuk ke "Kelola Akun" > "Hubungkan Wallet" > "Specter" > "Multisig" > "Kode QR", lalu pindai kode QR yang dihasilkan oleh Specter. Passport kemudian akan meminta kamu untuk memindai alamat penerima dari wallet untuk memvalidasi konfigurasi multisig.

Untuk MK4, colokkan ke PC kamu dan buka kuncinya. Kemudian klik "Simpan file Tuto MK4" dan simpan file tersebut ke MK4 kamu. Saat berikutnya kamu memasukkan hardware wallet, MK4 akan menggunakan file ini untuk menyelesaikan konfigurasi multisig.



![Export vers les hardware wallets](assets/fr/29.webp)



Sebagai informasi, kamu dapat mengakses cadangan kapan saja dari tab "Pengaturan" pada portofolio, lalu "Ekspor":



![Accès au backup PDF](assets/fr/30.webp)



Penggunaan sehari-hari tetap serupa dengan wallet sederhana: kamu menerima alamat penerima seperti biasa. Untuk mengirim bitcoin, buka tab "Kirim", masukkan alamat penerima dan jumlahnya, lalu klik "Buat Transaksi Tidak Ditandatangani".



![Création d'une transaction multisig](assets/fr/31.webp)



Specter membuat PSBT (Partially Signed Bitcoin Transaction) dan menampilkan "Mendapatkan 0 dari 2 tanda tangan". Sekarang kamu harus menandatangani dengan setidaknya dua dari tiga hardware wallet kamu. Klik pada hardware wallet pertama (misalnya "MK4 Tuto") untuk menandatangani dengan Coldcard kamu, lalu klik hardware wallet kedua (misalnya "Passport multi") untuk mendapatkan tanda tangan kedua yang diperlukan.

![Signature de la transaction](assets/fr/32.webp)



Setelah kamu mendapatkan 2 tanda tangan yang diperlukan (antarmuka menampilkan "Mendapatkan 2 dari 2 tanda tangan" dan "Transaksi siap dikirim"), klik "Kirim Transaksi" untuk menyiarkan transaksi ke jaringan Bitcoin.



![Transaction prête à être diffusée](assets/fr/33.webp)


Pendekatan multi-tanda tangan ini sangat cocok untuk perusahaan (beberapa manajer perlu menyetujui pengeluaran), keluarga (perlindungan warisan multi-generasi), atau individu yang mengelola dana dalam jumlah besar (distribusi geografis dompet perangkat keras untuk menahan bencana lokal).

### Pentingnya pencadangan multisignature

**Harap diperhatikan**: mencadangkan portofolio multisig pada dasarnya berbeda dengan mencadangkan portofolio tunggal. Frasa seed Anda saja tidak cukup untuk memulihkan portofolio multisig. Kamu juga harus mencadangkan **output descriptor** (output descriptor), yang berisi informasi konfigurasi untuk portofolio multisig kamu.

output descriptor memiliki data penting: kunci publik yang diperluas (xpubs) dari setiap penandatangan bersama, ambang batas tanda tangan (2-on-3 pada contoh kita), jenis skrip yang digunakan (asli, bersarang, atau Segwit lama), dan jalur pintas untuk setiap perangkat keras wallet. Tanpa deskriptor ini, bahkan jika kamu memiliki dua dari tiga frasa seed, kamu tidak akan dapat membangun kembali wallet atau mengakses bitcoin kamu. Deskriptor ini memungkinkan perangkat lunak kamu untuk mengetahui bagaimana cara menggabungkan kunci publik ke alamat generate dan Bitcoin yang sesuai dengan dana kamu.

Specter Desktop secara otomatis menghasilkan file PDF cadangan saat kamu membuat portofolio multisig. PDF ini berisi deskriptor lengkap, sidik jari setiap perangkat keras wallet, dan semua informasi publik yang diperlukan untuk pemulihan. **File ini tidak berisi kunci pribadi kamu** dan oleh karena itu tidak dengan sendirinya memungkinkan kamu untuk membelanjakan bitcoin, tetapi memungkinkan siapa pun yang mengaksesnya untuk melihat riwayat transaksi dan saldo lengkap kamu.

Untuk mencadangkan konfigurasi multisignature dengan benar, ikuti prosedur berikut: setelah membuat portofolio kamu, klik tab "Pengaturan", lalu "Ekspor" dan pilih "Simpan Cadangan PDF". Buat beberapa salinan PDF ini: cetak setidaknya dua salinan di atas kertas, dan juga simpan salinan digital terenkripsi. Simpan satu salinan PDF dengan setiap frasa seed kamu, di lokasi yang terpisah secara geografis.

Ukirlah frasa seed kamu pada pelat logam yang tahan api dan tahan air untuk menjamin umurnya yang panjang. Jangan pernah meremehkan pentingnya cadangan ini: jika kamu kehilangan folder `~/.specter` di komputer DAN kamu kehilangan salah satu dompet perangkat keras tanpa cadangan deskriptor, semua dana kamu akan hilang secara permanen, bahkan dengan konfigurasi 2-on-3. Redundansi multi-tanda tangan melindungi dari kehilangan perangkat keras wallet, namun hanya jika kamu sudah membuat cadangan deskriptor wallet kamu dengan benar.

## Keuntungan dan keterbatasan Specter Desktop

**Manfaat**: Kerahasiaan yang optimal dengan validasi lokal yang lengkap tanpa server pihak ketiga. Fleksibilitas multisignature untuk konfigurasi tingkat lanjut (perusahaan, keluarga, perorangan). Dukungan perangkat keras wallet yang luas dengan interoperabilitas penuh (USB dan air-gapped).

**Keterbatasan**: Kurva pembelajaran yang signifikan pada konsep Bitcoin tingkat lanjut (UTXO, deskriptor, jalur derivasi).

## Praktik terbaik

Selalu periksa alamat dan jumlah pada layar perangkat keras wallet kamu sebelum validasi, untuk melindungi diri dari malware.

Pisahkan cadangan PDF dari berkas kamu. Deskriptor publik ini dapat disimpan di brankas bank atau cloud terenkripsi, sehingga memudahkan pemulihan tanpa mengekspos kunci pribadi kamu.

Uji pemulihan pada jumlah token sebelum menggunakan portofolio dengan dana besar. Buat, uji, hapus, dan pulihkan untuk memvalidasi prosedur kamu.

Selalu perbarui Specter dan firmware kamu. Mendistribusikan penandatangan bersama multi-tanda tangan secara geografis (rumah/kantor/dekatnya) untuk menahan bencana lokal. Gunakan label deskriptif untuk memudahkan akuntansi dan pengembalian pajak.

## Bonus: Instalasi pada server Bitcoin (Umbrel, RaspiBlitz, Start9)

Jika kamu sudah memiliki server Bitcoin seperti Umbrel, RaspiBlitz, MyNode atau Start9, kamu bisa menginstal Specter Desktop langsung dari toko aplikasi mereka. Pendekatan ini menawarkan beberapa keuntungan yang signifikan: aplikasi secara otomatis mengkonfigurasi dirinya sendiri dengan node Bitcoin Core lokal kamu, tetap dapat diakses 24/7 melalui antarmuka web dari perangkat apa pun di jaringan kamu, dan kamu bahkan dapat mengaksesnya dengan aman dari jarak jauh melalui Tor. Seluruh infrastruktur Bitcoin kamu terpusat pada satu server khusus, menyederhanakan manajemen dan memperkuat kedaulatan kamu.

### Instalasi dari Toko Aplikasi Umbrel

Dari antarmuka Umbrel kamu, buka App Store dan cari Specter Desktop. Klik "Instal" untuk meluncurkan instalasi.



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



Setelah instalasi selesai, buka Specter Desktop pada Umbrel kamu. Layar selamat datang akan meminta kamu untuk memilih jenis koneksi. Jika kamu menggunakan Specter pada Umbrel kamu, klik "Perbarui pengaturan" untuk mengonfigurasi koneksi.



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



Pilih "Remote Specter USB connection" untuk mengaktifkan penggunaan dompet perangkat keras USB yang terhubung ke komputer lokal kamu ketika menggunakan Specter pada server Umbrel jarak jauh.



![Configuration Remote Specter USB](assets/fr/20.webp)



Ikuti petunjuk yang ditampilkan untuk mengonfigurasi HWI Bridge. Kamu perlu mengakses pengaturan jembatan perangkat dan menambahkan domain `http://umbrel.local:25441` ke daftar putih. Klik "Update" untuk menyimpan konfigurasi.



![HWI Bridge Settings](assets/fr/21.webp)



Jika kamu juga ingin menggunakan dompet perangkat keras USB dari komputer lokal kamu, unduh aplikasi Specter Desktop ke komputer kamu dan atur ke "Ya, saya menjalankan Specter dari jarak jauh". Klik "Simpan" untuk menyelesaikan konfigurasi.



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## Kesimpulan



Specter Desktop mendemokratisasi konfigurasi Bitcoin tingkat lanjut, membuat multisignature dapat diakses tanpa mengorbankan kedaulatan atau kerahasiaan kamu. Bagi pengguna yang mengelola sejumlah besar uang, ini mengubah praktik institusional menjadi solusi yang dapat digunakan oleh perorangan.

Meskipun aplikasi ini membutuhkan investasi awal dalam infrastruktur dan pembelajaran, aplikasi ini menawarkan kedaulatan penuh: kendali atas infrastruktur validasi, kepemilikan fisik atas kunci, dan transaksi yang bebas dari pengawasan pihak ketiga. Baik kamu seorang individu yang mengamankan tabunganmu, keluarga yang membuat brankas multi-generasi, atau perusahaan yang mengelola arus kas, Specter Desktop adalah alat referensi untuk merekonsiliasi keamanan maksimum dan kedaulatan mutlak.



## Sumber daya



### Dokumentasi resmi




- [Situs web resmi Specter Desktop](https://specter.solutions/desktop/)
- [Kode sumber GitHub](https://github.com/cryptoadvance/specter-desktop)
- [Dokumentasi lengkap](https://docs.specter.solutions/)



### Komunitas dan dukungan




- [Grup Komunitas Telegram Specter](https://t.me/spectersupport)
- [Forum diskusi Reddit](https://reddit.com/r/specterdesktop/)
- [Laporan bug GitHub](https://github.com/cryptoadvance/specter-desktop/issues)