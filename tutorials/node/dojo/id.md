---
name: Dojo
description: Node Bitcoin sumber terbuka untuk privasi dan otonomi
---

![cover](assets/cover.webp)



*Tutorial ini didasarkan pada [dokumentasi resmi Ashigaru] (https://ashigaru.rs/docs/), yang telah saya ambil alih dan kembangkan. Saya telah menulis ulang semua bagian untuk meningkatkan kejelasan, menambahkan penjelasan yang lebih rinci, serta ilustrasi untuk pemula, untuk membuat instalasi dan penggunaan lebih mudah dipahami.*



---

Dojo adalah sebuah program sumber terbuka yang didesain untuk bertindak sebagai sebuah server backend untuk dompet Bitcoin yang berorientasi pada privasi tertentu, yang berbasis pada sebuah node Bitcoin core. Secara historis, program ini dikembangkan untuk bekerja dengan Samourai Wallet, sebuah Wallet mobile yang menawarkan fitur privasi tingkat lanjut seperti Whirlpool (CoinJoin), Ricochet, Stonewall, PayNym... Samourai Wallet sekarang telah ditutup setelah pengembangnya ditangkap, tetapi penerus komunitasnya, **Ashigaru Wallet**, telah mengambil alih dan terus mengandalkan Dojo untuk menawarkan pengalaman yang lengkap bagi pengguna yang ingin tetap mengontrol data mereka saat menggunakan Bitcoin.



![Image](assets/fr/01.webp)



Secara praktis, Dojo bertindak sebagai pintu gerbang antara Wallet dan jaringan Bitcoin Anda. Tanpa Dojo, Wallet seluler yang ringan harus meminta server pihak ketiga untuk mendapatkan status UTXO dan riwayat Anda, atau untuk menyiarkan transaksi Anda. Hal ini menyiratkan ketergantungan dan kebocoran data sensitif ke server pihak ketiga (alamat yang digunakan, jumlah, frekuensi pembayaran, dll.). Dengan Dojo, Anda meng-host server ini sendiri, terhubung langsung ke node Bitcoin Anda sendiri. Dengan cara ini, semua permintaan portofolio Anda melewati infrastruktur yang Anda kendalikan, tanpa perantara, memperkuat kerahasiaan dan kedaulatan Anda.



## Persyaratan untuk mendirikan Dojo



Menyiapkan server Dojo tidak memerlukan mesin yang sangat kuat. Siapa pun yang memiliki komputer tingkat pemula, koneksi Internet yang stabil, dan kemampuan untuk membiarkannya menyala terus menerus (24/7) dapat menyiapkan Dojo yang berfungsi.



### Pilih jenis mesin Anda



Anda dapat menggunakan :




- sebuah laptop ;
- komputer desktop ;
- mini-PC (misalnya Intel NUC, Lenovo Thincentre Tiny...).



Setiap opsi memiliki kelebihan dan kekurangan:




- Harga: mini-PC atau desktop yang sudah diperbaharui sering kali lebih murah daripada laptop baru.
- Jejak: Mini-PC membutuhkan lebih sedikit ruang.
- Power Supply: laptop memiliki keunggulan baterai, yang berarti laptop tidak akan mati jika terjadi pemadaman listrik, tidak seperti mini-PC.
- Kemampuan upgrade: barbone pada umumnya memungkinkan Anda untuk menambah memori atau mengganti disk Hard dengan mudah.



Untuk informasi lebih lanjut mengenai cara memilih perlengkapan Anda, saya sarankan Anda mengikuti kursus ini:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### Peralatan yang direkomendasikan



Tidak perlu membeli mesin baru. Komputer yang diperbaharui dengan spesifikasi di bawah ini akan memberikan kinerja yang jauh lebih baik daripada elektronik papan tunggal (seperti Raspberry Pi).



**Spesifikasi minimum:** Spesifikasi minimum




- Arsitektur X86-64 (prosesor 64-bit).
- prosesor dual-core 2 GHz atau lebih cepat.
- minimum RAM 8 GB.
- 2 TB atau lebih SSD NVMe (untuk menyimpan Blockchain dari Bitcoin dan indeks yang diperlukan).



**Sistem operasi yang direkomendasikan: **




- Distribusi berbasis Debian, seperti Ubuntu 24.04 LTS.



**Peralatan yang direkomendasikan:**




- HP EliteDesk / EliteBook
- Dell OptiPlex
- Lenovo ThinkCentre / ThinkPad
- Intel NUC
- dll.



Sangat mungkin untuk menjalankan server Dojo pada konfigurasi perangkat keras lain. Namun, untuk mendapatkan performa terbaik dan membatasi masalah, kami menyarankan Anda untuk mengikuti rekomendasi di atas.



Dalam tutorial ini, saya akan menggunakan ThinkCentre Tiny lama dengan prosesor Intel Pentium Dual-Core G4400T, RAM 8 GB, dan SSD 2 TB.



## 1 - Menginstal Ubuntu



*Jika Anda ingin menginstal Dojo di perangkat yang sudah dikonfigurasi, Anda dapat melewati langkah ini dan langsung melanjutkan ke langkah 2.*



Setelah menyiapkan perangkat keras yang dipilih, saatnya menginstal sistem operasi. Anda bisa menggunakan hampir semua distribusi Debian, tetapi saya sarankan Anda memilih versi LTS dari Ubuntu, karena sangat cocok untuk tujuan kita. Berikut ini langkah-langkah yang harus diikuti:



### 1.1. membuat kunci USB yang dapat di-boot



Dari komputer yang sudah berfungsi (komputer yang biasa Anda gunakan), unduh citra ISO Ubuntu LTS [dari situs resmi] (https://ubuntu.com/download/desktop) (`24.04` pada saat tulisan ini dibuat, tetapi gunakan yang terbaru jika ada yang tersedia).



![Image](assets/fr/02.webp)



Masukkan kunci USB minimal 8 GB ke dalam komputer ini, kemudian buat kunci yang dapat di-boot menggunakan perangkat lunak seperti [Balena Etcher](https://etcher.balena.io/). Pilih image ISO Ubuntu yang baru saja Anda unduh, pilih kunci USB sebagai perangkat target, lalu mulai proses pembuatan (bersabarlah, mungkin perlu beberapa menit).



![Image](assets/fr/03.webp)



Masukkan kunci USB yang dapat di-boot ke dalam komputer yang dimatikan (komputer yang ingin Anda gunakan untuk menjalankan Dojo). Nyalakan komputer dan segera tekan **F12** atau **F10** pada keyboard Anda (tergantung model) untuk mengakses menu boot. Kemudian pilih kunci USB Anda sebagai perangkat prioritas dalam urutan booting komputer.



![Image](assets/fr/04.webp)



### 1.2. Instal sistem operasi



Layar beranda Ubuntu akan muncul. Pilih "Coba atau Instal Ubuntu*".



![Image](assets/fr/05.webp)



Kemudian ikuti proses instalasi Ubuntu klasik:




- Pilih bahasa.
- Pilih jenis keyboard.
- Jika Anda terhubung melalui kabel RJ45, tidak perlu mengonfigurasi Wi-Fi.
- Klik "*Instal Ubuntu*" dan centang opsi untuk menginstal perangkat lunak pihak ketiga (driver Wi-Fi, codec multimedia, dll.).
- Ketika wizard menanyakan jenis instalasi, pilih "*Hapus disk dan instal Ubuntu*". **Peringatan**: operasi ini akan menghapus isi disk sepenuhnya. Periksa dengan cermat bahwa disk yang Anda pilih sesuai dengan SSD NVMe yang ditujukan untuk Dojo.
- Buat nama pengguna yang sederhana (misalnya "*loic*").
- Tetapkan nama untuk mesin (misalnya "*dojo-node*").
- Tetapkan kata sandi yang kuat dan simpan dengan aman.
- Aktifkan opsi "*Minta kata sandi saya untuk masuk*" untuk memperkuat keamanan.
- Tunjukkan zona waktu Anda, lalu klik "*Instal*".
- Tunggu hingga instalasi selesai. Setelah selesai, sistem akan memulai ulang secara otomatis.
- Lepaskan kunci instalasi USB saat menghidupkan ulang komputer.



Untuk detail lebih lanjut tentang proses instalasi Ubuntu, silakan lihat tutorial khusus kami:



https://planb.academy/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. pembaruan sistem



Setelah boot pertama, buka terminal menggunakan kombinasi tombol ***Ctrl + Alt + T*** dan jalankan perintah berikut untuk memperbarui sistem:



```bash
sudo apt update
sudo apt upgrade -y
```



![Image](assets/fr/06.webp)



## 2. Instalasi bangunan luar



Agar Dojo dapat bekerja dengan baik, batu bata perangkat lunak tertentu harus ada di sistem Anda. Ini digunakan untuk mengelola repositori perangkat lunak, komunikasi, dekompresi arsip, dan eksekusi Dojo di dalam kontainer Docker. Semua operasi ini dilakukan di terminal.



### 2.1. Persiapan



Perintah berikut ini akan mengembalikan Anda ke folder pribadi Anda. Ini adalah praktik yang baik sebelum menjalankan serangkaian instalasi.



```bash
cd ~/
```



Sebelum menginstal perangkat lunak apa pun, pastikan database perangkat lunak yang tersedia di mesin Anda adalah yang terbaru. Hal ini untuk menghindari penginstalan versi yang sudah usang.



```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. memasang utilitas



Beberapa alat perlu ditambahkan ke dalam sistem:




- `apt-transport-https`: memungkinkan Anda mengunduh paket dengan aman melalui HTTPS
- `ca-certificates`: mengelola sertifikat yang diperlukan untuk koneksi terenkripsi
- `curl`: untuk mengambil file dari Internet
- `gnupg-agent`: untuk manajemen kunci GPG
- software-properties-common`: menyediakan utilitas untuk memanipulasi repositori APT
- `unzip`: membuka zip file dalam format ZIP



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



Selama penginstalan, sistem mungkin akan meminta konfirmasi dari Anda. Tekan tombol "*y*", lalu tekan "*Enter*".



![Image](assets/fr/08.webp)



### 2.3. Pasang Torsock



Torsocks memungkinkan perintah tertentu dijalankan melalui jaringan Tor, sehingga meningkatkan kerahasiaan komunikasi.



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. Instal Docker dan Docker Compose



Dojo berjalan di dalam kontainer Docker. Artinya, setiap layanan terisolasi dalam lingkungan yang independen, sehingga menyederhanakan pemeliharaan dan keamanan. Untuk melakukan ini, Anda perlu menginstal Docker dan alat Docker Compose, yang memungkinkan Anda untuk mengelola beberapa kontainer secara bersamaan.



#### Tambahkan kunci penandatanganan Docker



Docker menyediakan kunci tanda tangan digitalnya sendiri. Menambahkannya akan memverifikasi keaslian paket yang diunduh.



```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```



![Image](assets/fr/10.webp)



#### Repositori Docker resmi ditambahkan



Selanjutnya, Anda perlu memberi tahu sistem di mana menemukan paket-paket resmi Docker. Perintah ini menambahkan repositori baru ke konfigurasi manajer paket Anda.



```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```



![Image](assets/fr/11.webp)



#### Menginstal Docker dan Docker Compose



Komponen utama Docker sekarang dapat diinstal.



```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



![Image](assets/fr/12.webp)



#### Otorisasi pengguna



Secara default, hanya perintah yang dijalankan dengan hak administrator yang dapat meluncurkan Docker. Untuk kenyamanan yang lebih baik, saya sarankan untuk menambahkan pengguna Anda saat ini ke grup "*docker*". Ini memungkinkan Anda menggunakan Docker tanpa harus mengetikkan `sudo` setiap kali.



```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3. Pembuatan pengguna tunggal (opsional)



Jika Anda ingin meningkatkan keamanan sistem Anda, saya sarankan Anda membuat pengguna terpisah khusus untuk menjalankan Dojo. Pemisahan ini membatasi risiko: jika terjadi masalah keamanan di Dojo, hal itu tidak akan secara langsung membahayakan akun utama Anda.



### 3.1. Pembuatan akun pengguna



Perintah berikut ini membuat pengguna baru bernama "*dojo*". Pengguna ini akan memiliki direktori rumah `/home/dojo` dan akses ke terminal bash. Pengguna ini juga akan ditambahkan ke grup sudo untuk memungkinkan eksekusi perintah admin.



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2. Mengatur kata sandi



Penting untuk menetapkan kata sandi yang kuat untuk akun ini. Idealnya, Anda sebaiknya menggunakan pengelola kata sandi seperti Bitwarden untuk membuat kombinasi generate yang panjang dan sulit ditebak.



```bash
sudo passwd dojo
```



Sistem kemudian akan meminta Anda memasukkan kata sandi yang Anda pilih, lalu mengonfirmasikannya untuk kedua kalinya.



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3. Mengotorisasi pengguna untuk menggunakan Docker



Untuk mengaktifkan pengguna "*dojo*" untuk meluncurkan kontainer yang dibutuhkan untuk menjalankan Dojo, dia harus ditambahkan ke grup Docker. Hal ini untuk menghindari keharusan mendahului setiap perintah dengan `sudo`.



```bash
sudo usermod -aG docker dojo
```



### 3.4. Mulai ulang sistem



Agar perubahan grup dapat diterapkan, mesin harus dihidupkan ulang.



```bash
sudo reboot
```



### 3.5. Masuk dengan pengguna baru



Ketika sistem dimulai ulang, masuk dengan login ***dojo*** dan kata sandi yang Anda tentukan sebelumnya. Semua langkah selanjutnya harus dilakukan dari akun khusus ini.



## 4. Unduh dan periksa Dojo



Sebelum menginstal Dojo, sangat penting untuk memastikan bahwa file-file tersebut berasal dari pengembang resmi dan belum dimodifikasi. Langkah ini mengandalkan penggunaan PGP dan hash untuk memverifikasi keaslian dan integritas file.



### 4.1. mengimpor kunci PGP pengembang



Unduh kunci publik pengembang melalui Tor dan impor ke dalam gantungan kunci lokal Anda. Kunci ini akan digunakan untuk memverifikasi tanda tangan yang terkait dengan file Dojo.



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/14.webp)



### 4.2. Unduh versi terbaru Dojo



Ambil arsip terkompresi yang berisi kode sumber Dojo. Dalam contoh ini, versi terbaru adalah `1.27.0`: ubah perintah sesuai dengan [versi terbaru di repositori resmi GitHub](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases).



```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```



![Image](assets/fr/15.webp)



### 4.3. Mengunduh sidik jari dan tanda tangan



Para pengembang mempublikasikan sebuah berkas yang berisi daftar sidik jari digital dari arsip, serta berkas yang ditandatangani oleh kunci PGP mereka. Unduhlah file tersebut untuk membandingkan file Anda secara lokal.



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4. Periksa tanda tangan PGP



Periksa apakah file sidik jari telah ditandatangani oleh kunci yang diimpor.



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



Hasil yang benar menampilkan tanda tangan yang valid dengan kunci `E53AD419B242822F19E23C6D3033D463D6E544F6` dan Address terkait `dojocoder@pm.me`. Sebuah peringatan mungkin muncul yang menyatakan bahwa kunci tersebut tidak tersertifikasi: Anda dapat mengabaikannya.



Sebaliknya, jika tanda tangan tidak valid, segera hentikan proses instalasi dan mulai lagi dari awal.



![Image](assets/fr/17.webp)



### 4.5. Memeriksa integritas arsip



Hitung sidik jari SHA256 dari file yang diunduh, lalu buka file sidik jari untuk membandingkan kedua nilai tersebut.



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



Jika kedua sidik jari tersebut identik, Anda bisa yakin bahwa arsip tersebut belum dimodifikasi. Jika berbeda, jangan lanjutkan dan hapus file tersebut.



![Image](assets/fr/18.webp)



### 4.6. Mengekstrak dan mengatur file



Setelah verifikasi berhasil diselesaikan, Anda dapat membongkar arsip dan menyiapkan folder yang didedikasikan untuk instalasi Dojo.



```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7. Membersihkan file yang tidak perlu



Hapus file sementara dan arsip yang tidak lagi diperlukan untuk menjaga kebersihan lingkungan Anda.



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5. Konfigurasi dojo



Dojo adalah server backend yang menyatukan beberapa layanan untuk berinteraksi dengan portofolio Anda dan mengelola node Bitcoin Anda. Konfigurasinya bisa jadi rumit, tetapi proyek ini menawarkan metode yang disederhanakan yang secara otomatis menginstal dan mengonfigurasi komponen-komponen berikut:




- Dojo (API utama)
- Bitcoin core (simpul Bitcoin lengkap)
- BTC-RPC Explorer (web Block explorer)
- Pengindeks Fulcrum (pengindeksan blok dan transaksi secara cepat)
- Server Fulcrum Electrum tersedia di jaringan Tor
- Server Fulcrum Electrum tersedia di jaringan lokal
- Kredensial administrasi



### 5.1. Kredensial Administrasi



Untuk mengamankan akses ke berbagai layanan, Anda perlu memasukkan beberapa pengidentifikasi unik:




- `BITCOIND_RPC_USER`
- `BITCOIND_RPC_PASSWORD`
- `MYSQL_ROOT_PASSWORD`
- mYSQL_USER
- `MYSQL_PASSWORD`
- nODE_API_KEY`
- `NODE_ADMIN_KEY`
- `NODE_JWT_SECRET`



Pengidentifikasi ini **harus unik** (ini sangat penting: Anda tidak boleh menggunakan kata sandi yang sama untuk beberapa layanan), hanya terdiri dari angka, huruf besar dan huruf kecil (alfanumerik), dan panjangnya sekitar 40 karakter untuk menjamin tingkat keamanan yang tinggi. Sekali lagi, saya sangat menyarankan penggunaan pengelola kata sandi.



### 5.2. Mengakses file konfigurasi



File konfigurasi Dojo terletak di folder `conf/`. Pindah ke direktori ini:



```bash
cd ~/dojo-app/docker/my-dojo/conf/
```



![Image](assets/fr/21.webp)



### 5.3. Konfigurasi Bitcoin core



Buka file konfigurasi Bitcoin core dengan editor teks nano:



```bash
nano docker-bitcoind.conf.tpl
```



![Image](assets/fr/22.webp)



Dalam file ini, masukkan pengidentifikasi yang dihasilkan:



```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```



⚠️ ***Ganti `ID Anda di sini` dan `kata sandi Anda di sini` dengan login Anda sendiri (dengan kata sandi yang kuat)***



Anda juga dapat menyesuaikan ukuran memori cache yang digunakan oleh Bitcoin core untuk meningkatkan kinerja (Anda bahkan dapat menggunakan lebih banyak jika Anda memiliki banyak RAM yang tersedia):



```
BITCOIND_DB_CACHE=2048
```



Untuk menyimpan perubahan Anda dan menutup editor :




- tekan `Ctrl + X
- ketik `y`
- lalu tekan "*Masukkan*"



### 5.4. Konfigurasi MySQL



Kemudian buka konfigurasi basis data MySQL:



```bash
nano docker-mysql.conf.tpl
```



Masukkan detail login Anda:



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ ***Ganti `ID-mu-di sini` dan `kata sandi-mu-di sini` dengan login Anda sendiri (dengan kata sandi yang kuat dan unik).***



Simpan dengan cara yang sama (`Ctrl + X`, `y`, "*Enter*").



![Image](assets/fr/23.webp)



### 5.5. Konfigurasi pengindeks titik tumpu



Buka file berikut ini:



```bash
nano docker-indexer.conf.tpl
```



Tambahkan parameter untuk mengaktifkan Fulcrum dan mengintegrasikannya dengan benar ke dalam Dojo :



```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```



![Image](assets/fr/24.webp)



Selanjutnya, ada 2 kemungkinan, tergantung pada konfigurasi Anda. Jika Dojo diinstal pada mesin yang terpisah dari komputer Anda sehari-hari (pada mesin khusus, server...), masukkan IP Address di jaringan lokal Anda, misalnya :



```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



Untuk mengetahui IP lokal Address mesin Anda, buka terminal lain dan masukkan perintah berikut:



```bash
hostname -I
```



Kemungkinan kedua: jika Dojo dijalankan langsung di komputer pribadi Anda sehari-hari, pertahankan nilai default yang sudah ada dalam file konfigurasi :



```
INDEXER_EXTERNAL_IP=127.0.0.1
```



Simpan dan keluar dari editor (`Ctrl + X`, `y`, "*Enter*").



### 5.6. Konfigurasi layanan simpul



Terakhir, buka konfigurasi layanan Dojo utama:



```bash
nano docker-node.conf.tpl
```



Masukkan detail login Anda:



```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```



⚠️ *** Ganti `kata sandi Anda di sini` dengan kredensial Anda sendiri (dengan kata sandi yang kuat dan unik).***



![Image](assets/fr/26.webp)



Kemudian aktifkan pengindeks lokal:



```
NODE_ACTIVE_INDEXER=local_indexer
```



Simpan dan keluar dari editor (`Ctrl + X`, `y`, "*Enter*").



### 5.7. Manajemen login



Setelah konfigurasi selesai, tidak perlu menyimpan semua pengenal yang dihasilkan. Satu-satunya yang mutlak harus disimpan adalah :



```
NODE_ADMIN_KEY
```



Login ini akan memungkinkan Anda untuk masuk ke alat pemeliharaan Dojo nanti. Semua login lainnya dapat dihapus dari pengelola kata sandi atau catatan tulisan tangan anda. Mereka tetap dapat diakses dari file konfigurasi Dojo jika Anda perlu mengambilnya di masa mendatang.



## 6. Instalasi Dojo



Pada tahap ini, Dojo akan diinstal dan dijalankan pada mesin Anda. Operasi ini akan meluncurkan beberapa layanan (Bitcoin core, pengindeks Fulcrum, backend Dojo, dll.) dan memulai sinkronisasi penuh Blockchain Bitcoin. Proses ini mungkin memakan waktu beberapa hari, tergantung pada perangkat keras dan koneksi internet Anda.



### 6.1. Periksa apakah Docker berfungsi dengan baik



Sebelum memulai instalasi, pastikan bahwa Docker telah beroperasi. Jalankan perintah berikut:



```bash
docker run hello-world
```



Perintah ini mengunduh dan meluncurkan sebuah kontainer uji kecil. Jika semuanya berjalan dengan benar, Anda akan melihat pesan yang mirip dengan :



```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



Jika pesan ini tidak ditampilkan, mulailah dengan menyalakan ulang mesin Anda dengan :



```bash
sudo reboot
```



Kemudian, masuk kembali ke akun **dojo** Anda dan jalankan perintah uji coba lagi. Jika kesalahan tetap terjadi, Docker belum terinstal dengan benar. Dalam kasus ini, kembali ke langkah `2.4.` tentang menginstal Docker dan periksa setiap perintah dengan saksama.



### 6.2. Buka direktori instalasi Dojo



Skrip yang diperlukan untuk instalasi terletak di folder `my-dojo`. Pindah ke direktori ini:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/28.webp)



Gunakan perintah `ls` untuk memeriksa apakah file `dojo.sh` sudah ada. Ini adalah skrip utama yang mengotomatiskan instalasi Dojo dan peluncuran semua layanannya.



![Image](assets/fr/29.webp)



### 6.3. Mulai pemasangan



Mulai penginstalan dengan menjalankan aplikasi :



```bash
./dojo.sh install
```



Konfirmasikan penginstalan dengan menekan `y` lalu "*Enter*".



![Image](assets/fr/30.webp)



Skrip ini akan :




- unduh dan luncurkan kontainer Docker yang diperlukan,
- menginisialisasi Bitcoin core dan mulai menyinkronkan Blockchain,
- memulai pengindeks Fulcrum untuk melacak transaksi dan alamat,
- mengaktifkan backend Dojo dan API-nya.



Anda akan melihat aliran log yang terus bergulir, dengan referensi warna-warni seperti `bitcoind`, `soroban`, `nodejs`, atau `fulcrum`. Pengguliran ini menunjukkan bahwa Dojo sudah aktif dan berjalan dan mulai menjalankan berbagai layanan.



![Image](assets/fr/31.webp)



### 6.4. Tampilan log keluar



Log muncul secara real time di terminal Anda. Untuk kembali ke prompt perintah saat Dojo berjalan di latar belakang, ketik :



```
Ctrl + C
```



Jangan khawatir: menghentikan tampilan log tidak akan menghentikan layanan. Docker terus menjalankan Dojo di latar belakang (Anda tentu saja tidak perlu menghentikan komputer jika Anda ingin IBD terus berjalan).



### 6.5. Memahami *Pengunduhan Blok Awal* (IBD)



Pada saat pengaktifan, Bitcoin core harus mengunduh dan memverifikasi seluruh Blockchain sejak tahun 2009. Langkah ini disebut ***Initial Block Download* (IBD) **. Langkah ini sangat penting, karena memungkinkan node Dojo Anda untuk memverifikasi setiap blok dan transaksi Bitcoin secara independen.



Durasi sinkronisasi ini bergantung pada beberapa faktor:




- kekuatan prosesor Anda dan jumlah memori RAM yang tersedia,
- kecepatan disk Anda,
- jumlah dan kualitas peer yang terhubung dengan node Anda,
- kecepatan koneksi Internet Anda.



Dalam praktiknya, operasi ini umumnya memakan waktu antara **2 dan 7 hari**. Selama periode ini, Anda dapat membiarkan mesin Anda berjalan terus menerus. Semakin lama mesin dihidupkan, semakin cepat sinkronisasi akan selesai. Saya menyarankan Anda untuk memeriksa status sinkronisasi secara teratur dengan melihat log Bitcoin core, atau dengan menggunakan alat bantu pemeliharaan Dojo setelah terinstal (lihat bagian selanjutnya).



Untuk memperdalam pengetahuan Anda tentang IBD dan, secara umum, tentang pengoperasian dan peran node Bitcoin Anda, saya sarankan Anda untuk melihat kursus ini:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7. Pemantauan sinkronisasi



Ketika menginstal Dojo untuk pertama kalinya, Anda harus menunggu dua operasi utama selesai sepenuhnya: pengunduhan lengkap Blockchain Bitcoin (*IBD*) dan pengindeksan Blockchain ini oleh Fulcrum. Tergantung pada koneksi dan daya mesin Anda, hal ini dapat memakan waktu beberapa hari. Selama waktu ini, Anda dapat memantau kemajuan proses untuk memastikan semuanya berjalan dengan lancar.



Ada dua cara untuk memantau status sinkronisasi:




- penggunaan Dojo Maintenance Tool (atau DMT), yang sederhana namun memberikan sedikit detail selama IBD;
- konsultasi langsung log Dojo pada mesin Anda, lebih teknis tetapi jauh lebih tepat.



### 7.1. Periksa melalui Dojo Maintenance Tool (DMT)



Alat Pemeliharaan Dojo adalah Interface berbasis web yang aman dan memungkinkan Anda memantau status pabrik Anda, dan melakukan operasi tertentu. Ini adalah cara termudah dan paling mudah diakses untuk memantau kemajuan IBD. Selama fase sinkronisasi awal, informasi yang ditampilkan mungkin terbatas. Misalnya, DMT tidak menampilkan kemajuan rinci pengindeksan Fulcrum. Sebaliknya, setelah sinkronisasi selesai, DMT akan menampilkan dengan jelas:




- semua lampu pada Green;
- blok terakhir yang divalidasi untuk setiap layanan (Node, Pengindeks, Dojo DB).



Untuk mengaksesnya, Anda perlu mengetahui URL dari DMT Anda dan menyambungkannya [melalui peramban Tor](https://www.torproject.org/download/). Untuk melakukan ini, buka terminal dan masuk ke direktori `/my-dojo`:



```bash
cd ~/dojo-app/docker/my-dojo
```



Kemudian jalankan perintah berikut ini:



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



Anda kemudian akan memiliki akses ke semua informasi yang berkaitan dengan koneksi ke Dojo Anda melalui Tor. Yang kami minati di sini adalah URL berikut ini:



```
Dojo API and Maintenance Tool =
```



Untuk mengakses DMT dari mesin mana pun di jaringan mana pun (bahkan dari jarak jauh), buka Peramban Tor dan masukkan URL ini diikuti dengan `/admin`. Sebagai contoh, jika URL anda adalah `wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion`, anda harus memasukkannya di bilah [Tor Browser](https://www.torproject.org/download/):



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ ** Mohon jaga kerahasiaan Address ini



Anda kemudian akan diarahkan ke halaman autentikasi. DMT masuk menggunakan kata sandi `NODE_ADMIN_KEY` yang telah Anda buat sebelumnya.



![Image](assets/fr/33.webp)



Setelah masuk, Anda dapat mengakses *Dojo Maintenance Tool*! Selama IBD, Anda dapat melihat informasi "*Blok Terbaru*" di menu "*Full node*", yang memungkinkan Anda mengetahui status node Bitcoin Anda saat ini.



![Image](assets/fr/34.webp)



Ingatlah untuk menandai Address ini di Tor Browser untuk memudahkan pencarian di kemudian hari.



Setelah Dojo Anda tersinkronisasi sepenuhnya, Anda akan melihat tanda centang Green pada semua indikator di halaman beranda DMT.



### 7.2. Verifikasi melalui log Dojo



Cara kedua untuk melacak kemajuan IBD Anda adalah dengan melihat log mesin Anda secara langsung. Pendekatan ini menawarkan pemantauan yang jauh lebih tepat dan real-time. Anda dapat melihat bagaimana kemajuan Bitcoin core dalam mengunduh blok, dan bagaimana Fulcrum mengindeksnya.



Sambungkan ke mesin yang menghosting Dojo Anda dan buka terminal. Semua perintah harus dijalankan dari direktori `my-dojo`. Posisikan diri Anda di folder ini:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Log Bitcoin core



Lihat log Bitcoin core untuk melacak kemajuan IBD:



```bash
./dojo.sh logs bitcoind
```



Pada awalnya, Anda akan melihat fase pra-sinkronisasi header blok:



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



Ketika angka ini mencapai 100%, Bitcoin core akan memulai pengunduhan lengkap Blockchain. Anda akan melihat kemajuan IBD. Untuk mengetahui tinggi blok saat ini, lihat nilai yang ditunjukkan oleh `height=`. Anda juga dapat mengikuti kunci `progress=`, yang menunjukkan persentase kemajuan IBD.



![Image](assets/fr/36.webp)



Seperti biasa, untuk menutup log dan kembali ke command prompt, gunakan kombinasi `Ctrl + C`.



#### Log titik tumpu



Setelah Bitcoin core menyelesaikan pra-sinkronisasi header, Fulcrum mulai mengindeks Blockchain sambil berjalan. Lihat lognya dengan format :



```bash
./dojo.sh logs fulcrum
```



Anda kemudian akan melihat ketinggian blok terakhir yang diindeks, ditunjukkan setelah `height:`, serta persentase kemajuan pengindeksan.



![Image](assets/fr/37.webp)



### 7.3. Kerusakan basis data Fulcrum



Fulcrum adalah pengindeks yang sangat kuat, tetapi instalasinya bisa jadi rumit, paling tidak karena manajemen basis datanya yang rumit. Jika terjadi pemadaman listrik atau mesin mati mendadak selama sinkronisasi awal, basis data pengindeks dapat rusak. Anda dapat melihat hal ini, misalnya, jika Anda memiliki log berikut ini:



```bash
fulcrum | The database has been corrupted etc...
```



**Catatan:** Jenis kesalahan ini akan diperbaiki dengan rilis Fulcrum 2.0 yang akan datang.



Jika hal ini terjadi pada Anda, tidak ada dampak pada bitcoind (node Bitcoin Anda): IBD-nya akan terus berjalan secara independen dari Fulcrum. Namun, Anda tidak akan dapat menggunakan Fulcrum hingga Anda menghapus data yang rusak dan memulai kembali sinkronisasinya dari awal. Inilah cara kerjanya:



Hentikan Dojo:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Hapus hanya wadah dan volume Fulcrum:



```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```



Biasanya namanya adalah `my-dojo_data-fulcrum`, jika tidak demikian, sesuaikan nama yang dikembalikan oleh perintah sebelumnya.



Kemudian luncurkan kembali Dojo dan bangun kembali Fulcrum dari awal:



```bash
./dojo.sh upgrade
```



Anda kemudian dapat memeriksa apakah Fulcrum berfungsi dengan baik dengan melihat log:



```bash
docker logs -f fulcrum
```




## 8. Menggunakan Alat Pemeliharaan Dojo



Setelah simpul Bitcoin Anda disinkronkan ke kepala lungsin dengan Proof of Work yang paling banyak, dan Blockchain diindeks 100% oleh Fulcrum, Anda dapat mulai menggunakan Dojo Anda.



Dojo Anda menawarkan berbagai macam fitur, yang secara teratur disempurnakan dengan setiap versi baru. Menurut pendapat saya, 2 yang paling penting adalah :




- kemungkinan menghubungkan Ashigaru Wallet Anda untuk menggunakan node Anda sendiri untuk melihat data Blockchain dan menyiarkan transaksi Anda,
- dan Block explorer, yang memberi Anda akses ke informasi tentang Blockchain Bitcoin tanpa mengekspos data Anda ke contoh eksternal yang tidak Anda kendalikan.



Mari kita cari tahu cara menggunakannya.


### 8.1. Menghubungkan Ashigaru ke Dojo Anda



Menghubungkan Ashigaru Wallet Anda ke Dojo sangat mudah: setelah berada di DMT, buka menu "*Pairing*". Sebuah kode QR akan muncul, yang bisa Anda pindai secara langsung dengan aplikasi Ashigaru.



![Image](assets/fr/38.webp)



Dalam aplikasi Ashigaru, pertama kali Anda meluncurkannya setelah membuat atau memulihkan Wallet, Anda akan diarahkan ke halaman "*Konfigurasi server Dojo Anda*". Tekan "*Pindai QR*", lalu pindai kode QR yang ditampilkan pada DMT Anda.



![Image](assets/fr/39.webp)



Kemudian klik tombol "*Lanjutkan*".



![Image](assets/fr/40.webp)



Anda sekarang sudah terhubung ke Dojo Anda.



![Image](assets/fr/41.webp)



### 8.2. Menggunakan Block explorer



Dojo secara otomatis menginstal Block explorer, [BTC-RPC Explorer] (https://github.com/janoside/btc-RPC-explorer), yang secara langsung mengambil data dari node Bitcoin Anda sendiri. Penjelajah memungkinkan Anda mengakses informasi mentah dari Blockchain dan Mempool Anda melalui web Interface yang mudah dipahami. Jadi, Anda dapat, misalnya, memeriksa status transaksi yang tertunda, melihat saldo Address, atau memeriksa komposisi blok dengan mudah.



Untuk mengaksesnya, cukup ambil Tor Address dari peramban Anda. Untuk melakukan ini, jalankan perintah yang sama dengan yang Anda gunakan untuk mendapatkan Address dari DMT Anda:



```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



Anda akan memiliki akses ke semua informasi koneksi Dojo Anda melalui Tor. Yang kami minati di sini adalah URL berikut ini:



```
Block Explorer =
```



Jika Anda sudah terhubung ke DMT Anda, Anda juga dapat menemukan Address ini di menu "*Pairing*", di dalam JSON koneksi:



![Image](assets/fr/43.webp)



Untuk mengakses peramban Anda dari mesin apa pun di jaringan apa pun (bahkan dari jarak jauh), buka [Tor Browser] (https://www.torproject.org/download/) dan masukkan URL yang baru saja Anda ambil.



⚠️ ** Mohon jaga kerahasiaan Address ini



Anda kemudian akan memiliki akses ke Block explorer Anda sendiri.



![Image](assets/fr/44.webp)



*Kredit gambar: https://ashigaru.rs/.*



Untuk melacak transaksi, cukup masukkan txid di bilah pencarian di kanan atas.



![Image](assets/fr/45.webp)



*Kredit gambar: https://ashigaru.rs/.*



Untuk memeriksa gerakan yang terkait dengan Address, lanjutkan dengan cara yang sama dengan memasukkan Address di bilah pencarian.



![Image](assets/fr/46.webp)



*Kredit gambar: https://ashigaru.rs/.*



Anda juga dapat memasukkan Hash atau tinggi blok di bilah pencarian untuk menampilkan detail.



![Image](assets/fr/47.webp)



*Kredit gambar: https://ashigaru.rs/.*



## 9. Pemeliharaan dojo



### 9.1 Hentikan Dojo Anda



Jangan pernah memutus aliran listrik ke Dojo secara tiba-tiba, karena hal ini dapat merusak basis data tertentu, terutama pengindeks Fulcrum. Jika Anda harus mematikannya, selalu lakukan pemadaman Dojo secara menyeluruh, kemudian, setelah semua prosedur selesai, matikan mesin juga:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 Perbarui Dojo Anda



Dojo berkembang secara teratur dan versi baru dirilis untuk memperbaiki bug, meningkatkan stabilitas, dan menambahkan fitur. Oleh karena itu, penting [untuk memeriksa pembaruan secara teratur](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) dan memperbarui Dojo Anda. Prosesnya mirip dengan instalasi awal, tetapi mengharuskan Anda mengganti file tertentu dengan versi terbaru yang tersedia, sambil mempertahankan konfigurasi Anda. Berikut ini adalah langkah-langkah terperinci yang harus diikuti untuk pembaruan yang bersih dan aman:



Untuk mengetahui versi Dojo Anda saat ini, jalankan perintah :



```bash
./dojo.sh version
```



Meskipun langkah ini bersifat opsional, saya sarankan Anda memulai dengan memperbarui OS Anda. Hal ini akan mengurangi risiko ketidakcocokan dan memastikan bahwa dependensi yang digunakan oleh Dojo adalah yang terbaru:



```bash
sudo apt-get update
sudo apt-get upgrade
```



Buka direktori Dojo dan hentikan layanan yang sedang berjalan:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Kemudian, nyalakan ulang sistem Anda untuk mendapatkan sistem yang bersih:



```bash
sudo reboot
```



Dojo hadir dengan file yang ditandatangani secara digital. Tanda tangan PGP ini memastikan bahwa file-file tersebut berasal dari pengembang dan belum diubah dengan cara apa pun. Penting untuk memeriksanya setiap kali Anda memperbarui Dojo, seperti yang Anda lakukan saat pertama kali menginstalnya. Mulailah dengan mengunduh kunci publik pengembang melalui Tor, lalu impor:



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



Kembali ke direktori pribadi Anda:



```bash
cd ~/
```



Unduh versi terbaru Dojo dari GitHub melalui Tor. Dalam contoh ini, versi yang digunakan adalah versi `1.28.0` (yang belum ada pada saat artikel ini ditulis: ini hanya sebagai contoh). Ingatlah untuk mengganti file dan tautan [dengan versi yang ingin Anda instal] (https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases):



```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```



Unduh juga file yang berisi sidik jari dan tanda tangan PGP (sekali lagi, ingatlah untuk menyesuaikan versinya pada perintah):



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```



Periksa apakah file sidik jari yang diunduh telah ditandatangani oleh kunci pengembang:



```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```



Hasil yang benar akan menampilkan :



```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```



Peringatan bahwa kunci tersebut tidak bersertifikat mungkin muncul, tetapi ini tidak penting. Sebaliknya, jika tanda tangan tidak valid atau sesuai dengan kunci lain, jangan lanjutkan dan mulai lagi, periksa tautannya.



Kemudian hitung sidik jari SHA256 dari arsip dan bandingkan dengan file sidik jari resmi:



```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```



Jika kedua sidik jari sangat cocok, maka arsip tersebut asli dan utuh. Jika berbeda, segera hapus file tersebut dan jangan lanjutkan.



Buka kompresi arsip di direktori beranda Anda:



```bash
unzip samourai-dojo-1.28.0.zip -d .
```



Kemudian salin isinya ke direktori Dojo, dengan menimpa direktori :



```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```



Operasi ini membuat berkas konfigurasi Anda tetap berada di `~/dojo-app/docker/my-dojo/conf`, tetapi mengganti semua berkas lainnya dengan versi yang diperbarui.



Untuk menjaga lingkungan Anda tetap bersih, hapus file yang tidak perlu:



```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



Kembali ke direktori skrip Dojo dan jalankan perintah pembaruan:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```



Perintah ini menginstruksikan Docker untuk membangun ulang citra dengan berkas-berkas baru, lalu secara otomatis memulai ulang semua layanan. Di akhir proses, periksa log untuk memastikan bahwa Bitcoin core, Fulcrum, dan Dojo bekerja dengan benar:



```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```



Jika layanan dimulai tanpa kesalahan dan log menunjukkan blok yang sedang diproses, Dojo Anda sekarang sudah diperbarui dan beroperasi.