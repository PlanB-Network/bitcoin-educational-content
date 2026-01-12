---
name: Heritage
description: Portofolio Bitcoin dengan mekanisme pewarisan terintegrasi melalui skrip Taproot
---

![cover](assets/cover.webp)



Mewariskan bitcoin jika terjadi kematian atau ketidakmampuan merupakan tantangan besar bagi pemegang aset kripto. Tanpa rencana warisan yang sesuai, aset-aset ini menjadi tidak dapat dikembalikan kepada orang yang Anda cintai.



Heritage memberikan jawaban yang elegan dengan mengimplementasikan mekanisme peralihan orang mati secara langsung pada blockchain Bitcoin. wallet sumber terbuka ini memungkinkan kondisi suksesi on-chain untuk dikonfigurasikan: jika pemilik tidak melakukan transaksi lebih lanjut selama periode yang ditentukan, kunci alternatif yang telah ditentukan sebelumnya dapat melepaskan dana.



## Apa yang dimaksud dengan Warisan?



Heritage adalah portofolio Bitcoin yang secara native mengintegrasikan mekanisme pewarisan melalui skrip Taproot. Dikembangkan di bawah lisensi MIT oleh Jérémie Rodon, perangkat lunak sumber terbuka ini menjamin transparansi dan daya tahan.



Heritage menggunakan skrip Taproot yang dikodekan dalam alamat Bitcoin. Setiap UTXO mengintegrasikan dua jenis kondisi pengeluaran:





- Jalur utama** : Pemilik dapat membelanjakan bitcoinnya kapan saja dengan kunci primernya
- Jalur alternatif**: Untuk setiap ahli waris yang ditunjuk, skrip menggabungkan kunci publiknya dengan kunci waktu



Setiap transaksi pemilik secara otomatis menunda tanggal aktivasi klausul warisan. Jika terjadi ketidakaktifan yang berkepanjangan (kematian, ketidakmampuan), kondisi tersebut secara otomatis dipicu.



## Layanan warisan (opsional)



Heritage menawarkan dua opsi penggunaan:



**Lakukan sendiri (gratis)**: Aplikasi sumber terbuka saja. Anda mengelola semuanya secara mandiri dengan node Anda sendiri. Opsi ini menawarkan akses cadangan bawaan, warisan bawaan, dan kontrol eksklusif atas bitcoin Anda. Namun, Anda perlu membuat peringatan Anda sendiri (kalender, pengingat) agar Anda tidak lupa untuk memperbarui kunci waktu Anda, dan tidak ada pemberitahuan otomatis untuk ahli waris Anda.



**Gunakan layanan ini (0,05% per tahun)**: Layanan btc-heritage.com menambahkan fitur untuk menyederhanakan manajemen:




- Pengingat otomatis sebelum tenggat waktu Anda berakhir
- Pemberitahuan otomatis kepada ahli waris untuk memandu mereka melalui proses pemulihan
- Dukungan prioritas
- Manajemen deskriptor yang disederhanakan



Biaya: 0,05% dari jumlah yang dikelola per tahun, minimum 0,5 mBTC/tahun. Tahun pertama gratis.



Layanan ini tetap non-kustodian: kunci pribadi Anda tidak pernah meninggalkan perangkat Anda. Warisan tidak dapat mengakses dana Anda.



## Warisan CLI



Bagi pengguna tingkat lanjut yang lebih menyukai terminal, Heritage menawarkan alat bantu baris perintah (CLI) untuk kontrol granular dan pengoperasian alat berat dengan celah udara.



![Page Heritage CLI](assets/fr/03.webp)



Dokumentasi lengkap CLI tersedia di [btc-heritage.com/heritage-cli](https://btc-heritage.com/heritage-cli). Di sini Anda akan menemukan instruksi untuk mengunduh, menghubungkan ke layanan, membuat dompet (dengan Ledger atau kunci lokal), mengelola ahli waris dan transaksi.



Tutorial ini berfokus pada aplikasi Desktop, yang lebih mudah diakses oleh sebagian besar pengguna.



## Desktop Warisan



Heritage Desktop adalah aplikasi grafis dengan antarmuka intuitif yang memandu pengguna melalui setiap langkah proses konfigurasi.



### Unduh



Kunjungi [btc-heritage.com](https://btc-heritage.com) dan klik "Unduh aplikasi".



![Page d'accueil Heritage](assets/fr/01.webp)



Pilih versi yang sesuai dengan sistem operasi Anda (Linux 64bit atau Windows 64bit). Binary tidak ditandatangani secara digital, yang dapat memicu peringatan keamanan.



![Page de téléchargement](assets/fr/02.webp)



### Instalasi di Linux



Di Linux, aplikasi ini didistribusikan dalam format AppImage. Sebelum Anda dapat menjalankannya, Anda harus menginstal ketergantungan `libfuse2`:



```bash
sudo apt install libfuse2
```



![Installation libfuse2](assets/fr/04.webp)



Kemudian buatlah file tersebut dapat dieksekusi dan jalankan:



```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```



### Peluncuran pertama



Saat pertama kali diluncurkan, wizard orientasi menawarkan tiga pilihan:



![Onboarding initial](assets/fr/05.webp)





- Menyiapkan Wallet Warisan**: Membuat wallet baru dengan rencana warisan
- Mewarisi bitcoin**: Memulihkan bitcoin sebagai ahli waris
- Jelajahi sendiri**: Menjelajahi fungsi tanpa bantuan



Pilih "Siapkan Wallet Warisan" untuk membuat wallet pertama Anda.



### Koneksi jaringan Bitcoin



Pilih cara menyambung ke jaringan Bitcoin:



![Choix connexion](assets/fr/06.webp)





- Menggunakan Layanan Warisan**: Infrastruktur yang terkelola, lebih mudah bagi ahli waris
- Menggunakan node saya sendiri**: Hubungkan ke Bitcoin Core atau node Electrum Anda sendiri



Untuk tutorial ini, kita akan menggunakan node kita sendiri.



### Manajemen kunci pribadi



Pilih cara mengelola kunci pribadi Anda:



![Gestion des clés](assets/fr/07.webp)





- Dengan Perangkat Keras Ledger**: Keamanan maksimum dengan perangkat keras wallet (disarankan)
- Penyimpanan lokal dengan kata sandi**: Kunci yang disimpan secara lokal dengan perlindungan kata sandi
- Memulihkan wallet yang sudah ada**: Memulihkan dari seed yang sudah ada



### Konfigurasi simpul



Jika Anda menggunakan node Anda sendiri, aplikasi akan memandu Anda melalui konfigurasinya. Pastikan node Bitcoin atau Electrum Anda adalah :




- Terinstal dan berjalan
- Disinkronkan dengan jaringan Bitcoin
- Dikonfigurasi untuk menerima koneksi RPC (untuk Bitcoin Core)



![Configuration nœud](assets/fr/08.webp)



Klik "Node Bitcoin saya sudah aktif dan berjalan" ketika node Anda sudah siap.



### Panel status



Klik "Status" di sudut kanan atas, lalu "Buka Konfigurasi" untuk mengakses parameter koneksi.



![Panneau Status](assets/fr/09.webp)



Tetapkan URL server Electrum Anda (misal: `umbrel.local:50001` jika Anda menggunakan Umbrel).



![Configuration Electrum](assets/fr/10.webp)



### Penciptaan wallet



Setelah koneksi dibuat, klik "Buat Wallet" di tab WALLETS.



![Créer wallet](assets/fr/11.webp)



Munculan yang menjelaskan arsitektur terpisah dari Heritage :



![Architecture split](assets/fr/12.webp)



1. **Penyedia Kunci (Offline)**: Mengelola kunci pribadi Anda dan menandatangani transaksi. Dapat berupa perangkat lunak Ledger atau wallet.


2. **Online Wallet**: Menangani sinkronisasi dengan jaringan Bitcoin, pembuatan alamat, dan penyiaran transaksi.



Isi formulir pembuatan :



![Formulaire création wallet](assets/fr/13.webp)





- Nama Wallet**: Nama unik untuk mengidentifikasi wallet Anda
- Penyedia Kunci**: Pilih Penyimpanan Kunci Lokal untuk tutorial ini
- Baru/Pemulihan**: Pilih "Baru" untuk membuat generate menjadi seed yang baru
- Jumlah Kata**: direkomendasikan 24 kata untuk keamanan maksimum



Masukkan kata sandi yang kuat dan pilih opsi untuk Online Wallet :



![Options Online Wallet](assets/fr/14.webp)





- Simpul Lokal**: Menggunakan node Electrum atau Bitcoin Core Anda sendiri
- Layanan Warisan**: Menggunakan layanan Warisan (disarankan untuk fungsi pemberitahuan)



Klik "Buat Wallet" untuk menyelesaikan pembuatan.



### Interface dari wallet



wallet Anda sekarang sudah dibuat. Antarmuka ditampilkan :



![Interface wallet](assets/fr/15.webp)





- Keseimbangan
- Tombol KIRIM dan TERIMA
- Riwayat transaksi
- Riwayat konfigurasi warisan
- Alamat wallet



### Menciptakan ahli waris



Buka tab "AHLI WARIS" untuk membuat ahli waris Anda.



![Page Heirs](assets/fr/16.webp)



Popup informasi menjelaskan:




- Ahli waris adalah kunci publik Bitcoin yang terkait dengan individu
- Setiap ahli waris memiliki frasa mnemoniknya sendiri
- Pewaris pertama harus menjadi "Cadangan" untuk diri Anda sendiri (jika kehilangan wallet utama Anda)



#### Pembuatan ahli waris cadangan



Klik "Buat Ahli Waris" dan beri nama "Cadangan".



![Création héritier Backup](assets/fr/17.webp)



Popup menjelaskan mengapa kalimat 12 kata tanpa passphrase aman bagi ahli waris:


1. **Tidak ada akses langsung**: Ahli waris tidak dapat mengakses dana hingga timelock kedaluwarsa


2. **Deteksi kompromi**: Jika seseorang mengakses frasa tersebut, Anda dapat memperbarui konfigurasi Warisan


3. **Aksesibilitas jangka panjang**: passphrase bisa dilupakan setelah bertahun-tahun



Konfigurasikan ahli waris :



![Configuration héritier](assets/fr/18.webp)





- Penyedia Kunci** : Penyimpanan Kunci Lokal
- Baru**: Menghasilkan seed baru
- Jumlah Kata**: 12 kata



Menyelesaikan kreasi :



![Finalisation héritier](assets/fr/19.webp)





- Jenis Ahli Waris**: Kunci Publik yang Diperpanjang
- Ekspor ke Layanan**: Opsional, memungkinkan pemberitahuan otomatis kepada ahli waris



Pewaris Cadangan sekarang telah dibuat:



![Héritier créé](assets/fr/20.webp)



#### Menyimpan frasa mnemonik pewaris



Klik pada Pewaris cadangan dan kemudian pada "Tampilkan Mnemonic" :



![Afficher mnemonic](assets/fr/21.webp)



**PENTING: Catatlah 12 kata ini dan simpanlah di tempat yang aman. Ini adalah kunci untuk mendapatkan kembali dana.



![Phrase mnémotechnique](assets/fr/22.webp)



#### Menghapus seed dari aplikasi



Setelah Anda menuliskan frasa, akses parameter pewaris (ikon roda gigi):



![Paramètres héritier](assets/fr/23.webp)



Gunakan "Strip Heir Seed" untuk menghapus kunci pribadi dari aplikasi. Konfirmasikan bahwa Anda telah menyimpan frasa tersebut.



![Strip Heir Seed](assets/fr/24.webp)



Ini adalah langkah keamanan: hanya kunci publik yang tersisa di aplikasi, cukup untuk mengonfigurasi pewarisan.



#### Pembuatan ahli waris kedua



Ulangi proses ini untuk membuat ahli waris kedua (misalnya "Satoshi"). Anda sekarang akan memiliki dua ahli waris:



![Deux héritiers](assets/fr/25.webp)





- Cadangan**: Kunci darurat pribadi Anda
- Satoshi**: Ahli waris yang ditunjuk



### Konfigurasi warisan



Kembali ke wallet Anda dan klik ikon Pengaturan:



![Paramètres wallet](assets/fr/26.webp)



Pada bagian "Konfigurasi Warisan", klik "Buat":



![Heritage Configuration](assets/fr/27.webp)



Tetapkan batas waktu untuk setiap ahli waris:



![Configuration délais](assets/fr/28.webp)





- Cadangan**: 180 hari (6 bulan) - Tanggal Jatuh Tempo: 2026-06-18
- Satoshi**: 455 hari (15 bulan) - Tanggal Jatuh Tempo: 2027-03-20



**Penting**: Setiap ahli waris harus memiliki penundaan yang lebih lama dari ahli waris sebelumnya. Ahli waris pertama (Cadangan) akan memiliki akses ke dana terlebih dahulu.



Juga konfigurasikan :



![Configuration finale](assets/fr/29.webp)





- Tanggal Referensi**: Tanggal awal untuk menghitung waktu tunggu
- Penundaan Jatuh Tempo Minimum**: Penundaan minimum setelah transaksi (disarankan 10 hari)



Klik "Buat" untuk memvalidasi konfigurasi.



Konfigurasi Heritage sekarang aktif:



![Configuration active](assets/fr/30.webp)



Ini menampilkan kedua ahli waris dengan tenggat waktu dan tanggal kedaluwarsa masing-masing.



### Menyimpan deskriptor



**Penting**: Simpan deskriptor wallet Anda. Tanpa mereka, bahkan dengan frasa mnemonik, pemulihan dana tidak mungkin dilakukan.



Klik "Deskriptor Cadangan" :



![Bouton Backup](assets/fr/31.webp)



Simpan file JSON yang berisi deskriptor Bitcoin Anda:



![Backup descripteurs](assets/fr/32.webp)



File ini harus diwariskan kepada ahli waris Anda, bersama dengan frasa mnemonik masing-masing.



### Menerima bitcoin



Klik "TERIMA" untuk mendapatkan alamat penerimaan generate:



![Recevoir bitcoins](assets/fr/33.webp)



Selamat! Heritage Wallet Anda siap menerima bitcoin. Setiap alamat yang dibuat secara otomatis menggabungkan kondisi Heritage Anda.



Setelah menerima transaksi, saldo Anda akan diperbarui:



![Solde mis à jour](assets/fr/34.webp)



Riwayat menampilkan transaksi dan konfigurasi Warisan yang terkait.



---

## Pemulihan oleh ahli waris



Setelah waktu yang ditetapkan telah berlalu, ahli waris dapat mengambil kembali dana tersebut.



### Prasyarat



Ahli waris membutuhkan :


1. Frasa mnemonik 12 kata miliknya


2. File cadangan deskriptor wallet asli (JSON)



### Membuat Ahli Waris Wallet



Pada tab "INHERITANSI", sebuah popup akan mengingatkan Anda tentang prasyarat ini:



![Page Heir Wallets](assets/fr/35.webp)



**Harap diperhatikan**: Tanpa file cadangan deskriptor, akses ke dana TIDAK MUNGKIN dilakukan, bahkan dengan frasa mnemonik yang benar.



Klik "Buat Ahli Waris Wallet" :



![Créer Heir Wallet](assets/fr/36.webp)



Silakan isi formulir:



![Formulaire Heir Wallet](assets/fr/37.webp)





- Nama Ahli Waris Wallet**: Nama untuk mengidentifikasi ahli waris ini wallet
- Penyedia Kunci** : Penyimpanan Kunci Lokal
- Pulihkan**: Pilih opsi ini untuk memasukkan frasa yang sudah ada



Masukkan 12 kata frasa mnemonik ahli waris dan konfigurasikan Penyedia Warisan:



![Entrée mnemonic](assets/fr/38.webp)





- Penyedia Warisan**: "Lokal" untuk menggunakan simpul Anda sendiri dengan file cadangan



Muat file cadangan JSON dan klik "Buat Pewaris Wallet" :



![Chargement backup](assets/fr/39.webp)



### Interface Ahli Waris Wallet



Pewaris Wallet dibuat. Awalnya, jika timelock belum kedaluwarsa, tidak ada warisan yang tersedia:



![Pas d'héritage disponible](assets/fr/40.webp)



Setelah penundaan berlalu dan dana telah disinkronkan dengan jaringan Bitcoin, dana tersebut akan muncul dalam daftar warisan:



![Héritage disponible](assets/fr/41.webp)



Tampilan antarmuka :




- Jenis tombol dan sidik jari
- Total dana yang dapat diwariskan
- Jumlah yang dapat dibelanjakan saat ini (0 sat jika timelock belum kedaluwarsa)
- Tanggal jatuh tempo dan kedaluwarsa



Ketika tanggal jatuh tempo tercapai, tombol "Habiskan" akan mentransfer bitcoin ke wallet pribadi.



---

## Praktik terbaik



### Menyimpan deskriptor



Deskriptor wallet sangat penting untuk merekonstruksi alamat Warisan Anda. **Tanpa deskriptor, bahkan dengan frasa mnemonik Anda, Anda tidak akan dapat menemukan dana Anda.



### Keamanan kunci





- Gunakan Ledger untuk kunci utama jika memungkinkan
- Jangan pernah menyimpan kalimat ahli waris di tempat yang sama dengan kalimat Anda sendiri
- Menyebarkan informasi di berbagai media dan lokasi



### Dokumentasi untuk orang yang Anda cintai



Tuliskan instruksi yang jelas yang menjelaskan setiap langkah proses pemulihan. Ahli waris Anda mungkin tidak terbiasa dengan Bitcoin pada saat-saat kritis.



## Alternatif



Ada solusi lain untuk mengelola pengiriman bitcoin Anda, termasuk Liana dan Bitcoin Keeper. Anda akan menemukan tutorial kami di bawah ini:



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## Kesimpulan



Heritage memungkinkan Anda untuk merencanakan suksesi Bitcoin Anda dengan cara yang berdaulat melalui aplikasi Desktop. Implementasi memerlukan pertimbangan yang cermat mengenai kerangka waktu yang tepat dan pengamanan rahasia. Jangan lupa untuk mewariskan kepada ahli waris Anda:




- Frasa mnemonik 12 kata mereka
- File cadangan deskriptor
- Petunjuk pemulihan



## Sumber daya





- [Situs web resmi Heritage](https://btc-heritage.com)
- [Dokumentasi CLI](https://btc-heritage.com/heritage-cli)
- [GitHub Heritage CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage Desktop](https://github.com/crypto7world/heritage-gui)