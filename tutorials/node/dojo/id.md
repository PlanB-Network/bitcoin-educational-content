---
name: Dojo
description: Node Bitcoin sumber terbuka untuk privasi dan otonomi
---

![cover](assets/cover.webp)



*Tutorial ini didasarkan pada [dokumentasi resmi Ashigaru](https://ashigaru.rs/docs/), yang telah saya ambil alih dan kembangkan. Saya telah menulis ulang semua bagian untuk meningkatkan kejelasan, menambahkan penjelasan yang lebih rinci, serta ilustrasi untuk pemula, untuk membuat instalasi dan penggunaan lebih mudah dipahami.*



---

Dojo adalah program sumber terbuka yang dibuat untuk jadi server backend bagi dompet Bitcoin yang berfokus pada privasi, dan berjalan di atas node Bitcoin Core. Awalnya, program ini dikembangkan untuk bekerja dengan Samourai Wallet, dompet mobile yang menawarkan fitur privasi tingkat lanjut seperti Whirlpool (CoinJoin), Ricochet, Stonewall, dan PayNym. Samourai Wallet sekarang sudah ditutup setelah pengembangnya ditangkap, tapi penerus komunitasnya, **Ashigaru Wallet,** sekarang mengambil alih dan tetap mengandalkan Dojo untuk memberikan pengalaman lengkap bagi pengguna yang ingin tetap mengontrol data mereka saat menggunakan Bitcoin.



![Image](assets/fr/01.webp)


Secara praktis, Dojo bertindak sebagai pintu gerbang antara wallet dan jaringan Bitcoin kamu. Tanpa Dojo, wallet seluler yang ringan harus meminta server pihak ketiga untuk mendapatkan status UTXO dan riwayat kamu, atau untuk menyiarkan transaksi kamu. Ini berarti ada ketergantungan dan kebocoran data sensitif ke server pihak ketiga seperti alamat yang digunakan, jumlah, dan frekuensi pembayaran. Dengan Dojo, kamu meng-host server ini sendiri dan terhubung langsung ke node Bitcoin kamu sendiri. Dengan begitu, semua permintaan wallet kamu lewat infrastruktur yang kamu kendalikan tanpa perantara, sehingga memperkuat kerahasiaan dan kedaulatan kamu.


## Persyaratan untuk mendirikan Dojo

Menyiapkan server Dojo tidak membutuhkan mesin yang sangat kuat. Siapa pun yang punya komputer level pemula, koneksi internet yang stabil, dan bisa membiarkannya tetap menyala terus menerus (24/7) bisa menyiapkan Dojo yang berfungsi.



### Pilih jenis mesin kamu



Kamu bisa menggunakan :




- sebuah laptop ;
- komputer desktop ;
- mini-PC (misalnya Intel NUC, Lenovo Thincentre Tiny...).



Setiap opsi memiliki kelebihan dan kekurangan:




- Harga: mini-PC atau desktop yang sudah diperbaharui sering kali lebih murah daripada laptop baru.
- Jejak: Mini-PC membutuhkan lebih sedikit ruang.
- Power Supply: laptop memiliki keunggulan baterai, yang berarti laptop tidak akan mati jika terjadi pemadaman listrik, tidak seperti mini-PC.
- Kemampuan upgrade: barbone pada umumnya memungkinkan Anda untuk menambah memori atau mengganti disk Hard dengan mudah.



Untuk informasi lebih lanjut mengenai cara memilih perlengkapan kamu, aku sarankan kamu mengikuti kursus ini:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### Peralatan yang direkomendasikan



Kamu tidak perlu membeli mesin baru. Komputer yang direkondisi dengan spesifikasi di bawah ini akan memberikan kinerja yang jauh lebih baik dibandingkan single board computer seperti Raspberry Pi.



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



Sangat memungkinkan untuk menjalankan server Dojo dengan konfigurasi perangkat keras lain. Tapi untuk mendapatkan performa terbaik dan meminimalkan masalah, aku menyarankan kamu mengikuti rekomendasi di atas.


Dalam tutorial ini, aku akan menggunakan ThinkCentre Tiny lama dengan prosesor Intel Pentium Dual-Core G4400T, RAM 8 GB, dan SSD 2 TB.



## 1 - Menginstal Ubuntu



*Jika kamu ingin menginstal Dojo di perangkat yang sudah dikonfigurasi, kamu dapat melewati langkah ini dan langsung melanjutkan ke langkah 2.*



Setelah perangkat keras yang kamu pilih siap, sekarang saatnya menginstal sistem operasi. Kamu bisa menggunakan hampir semua distribusi Debian, tapi aku sarankan memilih Ubuntu versi LTS karena paling cocok untuk kebutuhan kita. Berikut langkah-langkahnya:



### 1.1. membuat kunci USB yang dapat di-boot



Dari komputer yang sudah berfungsi (komputer yang biasa Anda gunakan), unduh citra ISO Ubuntu LTS [dari situs resmi](https://ubuntu.com/download/desktop) (`24.04` pada saat tulisan ini dibuat, tetapi gunakan yang terbaru jika ada yang tersedia).



![Image](assets/fr/02.webp)



Masukkan kunci USB minimal 8 GB ke dalam komputer ini, kemudian buat kunci yang dapat di-boot menggunakan perangkat lunak seperti [Balena Etcher](https://etcher.balena.io/). Pilih image ISO Ubuntu yang baru saja kamu unduh, pilih kunci USB sebagai perangkat target, lalu mulai proses pembuatan (bersabarlah, mungkin perlu beberapa menit).



![Image](assets/fr/03.webp)



Masukkan USB bootable ke komputer yang sedang mati (komputer yang ingin kamu pakai untuk menjalankan Dojo). Nyalakan komputer dan segera tekan F12 atau F10 di keyboard kamu (tergantung model) untuk masuk ke menu boot. Lalu pilih USB tersebut sebagai perangkat prioritas dalam urutan boot.


![Image](assets/fr/04.webp)



### 1.2. Instal sistem operasi



Layar beranda Ubuntu akan muncul. Pilih "Coba atau Instal Ubuntu*".



![Image](assets/fr/05.webp)



Kemudian ikuti proses instalasi Ubuntu klasik:

- Pilih bahasa
- Pilih jenis keyboard
- Jika kamu terhubung lewat kabel RJ45, kamu tidak perlu mengonfigurasi Wi-Fi
- Klik *Instal Ubuntu* dan centang opsi untuk menginstal perangkat lunak pihak ketiga seperti driver Wi-Fi dan codec multimedia
- Saat wizard menanyakan jenis instalasi, pilih *Hapus disk dan instal Ubuntu* **Peringatan:** langkah ini akan menghapus isi disk sepenuhnya. Pastikan disk yang kamu pilih adalah SSD NVMe yang memang ditujukan untuk Dojo
- Buat nama pengguna yang sederhana seperti *loic*
- Tentukan nama untuk mesin seperti *dojo-node*
- Buat kata sandi yang kuat dan simpan dengan aman
- Aktifkan opsi *Minta kata sandi saya untuk masuk* untuk keamanan tambahan



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



Agar Dojo bisa bekerja dengan baik, beberapa komponen perangkat lunak perlu ada di sistem kamu. Komponen ini dipakai untuk mengelola repositori perangkat lunak, komunikasi, mengekstrak arsip, dan menjalankan Dojo di dalam container Docker. Semua langkah ini dilakukan lewat terminal.


### 2.1. Persiapan



Perintah berikut akan membawa kamu kembali ke folder home. Ini adalah kebiasaan yang baik sebelum menjalankan rangkaian instalasi.


```bash
cd ~/
```



Sebelum menginstal perangkat lunak apa pun, pastikan database perangkat lunak yang tersedia di mesin kamu sudah yang terbaru. Ini untuk menghindari instalasi versi yang sudah usang.


```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. memasang utilitas



Beberapa alat perlu ditambahkan ke dalam sistem:




- `apt-transport-https`: memungkinkan kamu mengunduh paket dengan aman melalui HTTPS
- `ca-certificates`: mengelola sertifikat yang diperlukan untuk koneksi terenkripsi
- `curl`: untuk mengambil file dari Internet
- `gnupg-agent`: untuk manajemen kunci GPG
- software-properties-common`: menyediakan utilitas untuk memanipulasi repositori APT
- `unzip`: membuka zip file dalam format ZIP



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



Selama penginstalan, sistem mungkin akan meminta konfirmasi dari kamu. Tekan tombol "*y*", lalu tekan "*Enter*".



![Image](assets/fr/08.webp)



### 2.3. Pasang Torsock



Torsocks memungkinkan perintah tertentu dijalankan melalui jaringan Tor, sehingga meningkatkan kerahasiaan komunikasi.



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. Instal Docker dan Docker Compose



Dojo berjalan di dalam container Docker. Artinya, setiap layanan terisolasi dalam lingkungan yang independen, sehingga memudahkan pemeliharaan dan keamanan. Untuk itu kamu perlu menginstal Docker dan alat Docker Compose, yang memungkinkan kamu mengelola beberapa container sekaligus.



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



Selanjutnya kamu perlu memberi tahu sistem di mana menemukan paket resmi Docker. Perintah ini menambahkan repositori baru ke konfigurasi package manager kamu.


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



Secara default, hanya perintah yang dijalankan dengan hak administrator yang bisa menjalankan Docker. Untuk kenyamanan, aku sarankan menambahkan pengguna kamu saat ini ke grup "docker". Ini memungkinkan kamu memakai Docker tanpa harus mengetik `sudo` setiap kali.


```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3. Pembuatan pengguna tunggal (opsional)



Kalau kamu ingin meningkatkan keamanan sistem, aku sarankan membuat pengguna terpisah khusus untuk menjalankan Dojo. Pemisahan ini membantu membatasi risiko, jadi kalau suatu saat ada masalah keamanan di Dojo, itu tidak langsung membahayakan akun utama kamu.


### 3.1. Pembuatan akun pengguna



Perintah berikut ini membuat pengguna baru bernama "*dojo*". Pengguna ini akan memiliki direktori rumah `/home/dojo` dan akses ke terminal bash. Pengguna ini juga akan ditambahkan ke grup sudo untuk memungkinkan eksekusi perintah admin.



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2. Mengatur kata sandi



Sistem kemudian akan meminta kamu memasukkan kata sandi yang kamu pilih, lalu mengonfirmasinya sekali lagi.

```bash
sudo passwd dojo
```



Sistem kemudian akan meminta kamu memasukkan kata sandi yang kamu pilih, lalu mengonfirmasinya untuk yang kedua kalinya.


https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3. Mengotorisasi pengguna untuk menggunakan Docker



Untuk mengaktifkan pengguna *dojo* agar bisa menjalankan container yang dibutuhkan untuk menjalankan Dojo, pengguna tersebut harus ditambahkan ke grup Docker. Ini supaya kamu tidak perlu menambahkan `sudo` di setiap perintah.


```bash
sudo usermod -aG docker dojo
```



### 3.4. Mulai ulang sistem



Agar perubahan grup dapat diterapkan, mesin harus dihidupkan ulang.



```bash
sudo reboot
```



### 3.5. Masuk dengan pengguna baru



Ketika sistem dimulai ulang, masuk dengan login ***dojo*** dan kata sandi yang kamu tentukan sebelumnya. Semua langkah selanjutnya harus dilakukan dari akun khusus ini.



## 4. Unduh dan periksa Dojo



Sebelum menginstal Dojo, penting untuk memastikan bahwa file yang kamu download benar benar berasal dari pengembang resmi dan belum dimodifikasi. Langkah ini menggunakan PGP dan hash untuk memverifikasi keaslian dan integritas file.


### 4.1. mengimpor kunci PGP pengembang



Unduh kunci publik pengembang lewat Tor lalu impor ke keyring lokal kamu. Kunci ini akan dipakai untuk memverifikasi tanda tangan yang terkait dengan file Dojo.


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



Para pengembang mempublikasikan sebuah file yang berisi daftar sidik jari digital dari arsip, serta file yang ditandatangani dengan kunci PGP mereka. Unduh file ini untuk membandingkan file kamu secara lokal.


```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4. Periksa tanda tangan PGP



Periksa apakah file sidik jari telah ditandatangani oleh kunci yang diimpor.



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



Hasil yang benar menampilkan tanda tangan yang valid dengan kunci `E53AD419B242822F19E23C6D3033D463D6E544F6` dan Address terkait `dojocoder@pm.me`. Sebuah peringatan mungkin muncul yang menyatakan bahwa kunci tersebut tidak tersertifikasi: kamu bisa mengabaikannya.



Sebaliknya, jika tanda tangan tidak valid, segera hentikan proses instalasi dan mulai lagi dari awal.



![Image](assets/fr/17.webp)



### 4.5. Memeriksa integritas arsip



Hitung sidik jari SHA256 dari file yang diunduh, lalu buka file sidik jari untuk membandingkan kedua nilai tersebut.



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



Jika kedua sidik jari tersebut identik, kamu bisa yakin bahwa arsipnya belum dimodifikasi. Jika berbeda, jangan lanjutkan dan hapus file tersebut.


![Image](assets/fr/18.webp)



### 4.6. Mengekstrak dan mengatur file



Setelah verifikasi berhasil, kamu bisa mengekstrak arsip dan menyiapkan folder khusus untuk instalasi Dojo.


```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7. Membersihkan file yang tidak perlu



Hapus file sementara dan arsip yang tidak lagi diperlukan untuk menjaga kebersihan lingkungan kamu.



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5. Konfigurasi dojo



Dojo adalah server backend yang menggabungkan beberapa layanan untuk berinteraksi dengan wallet kamu dan mengelola node Bitcoin. Konfigurasinya bisa cukup rumit, tapi proyek ini menyediakan metode yang disederhanakan untuk secara otomatis menginstal dan mengonfigurasi komponen berikut:



- Dojo (API utama)
- Bitcoin core (simpul Bitcoin lengkap)
- BTC-RPC Explorer (web Block explorer)
- Pengindeks Fulcrum (pengindeksan blok dan transaksi secara cepat)
- Server Fulcrum Electrum tersedia di jaringan Tor
- Server Fulcrum Electrum tersedia di jaringan lokal
- Kredensial administrasi



### 5.1. Kredensial Administrasi



Untuk mengamankan akses ke berbagai layanan, kamu perlu memasukkan beberapa pengidentifikasi unik:




- `BITCOIND_RPC_USER`
- `BITCOIND_RPC_PASSWORD`
- `MYSQL_ROOT_PASSWORD`
- mYSQL_USER
- `MYSQL_PASSWORD`
- nODE_API_KEY`
- `NODE_ADMIN_KEY`
- `NODE_JWT_SECRET`



Pengidentifikasi ini **harus unik** (penting: jangan gunakan kata sandi yang sama untuk beberapa layanan), hanya terdiri dari angka dan huruf besar-kecil (alfanumerik), dan panjangnya sekitar 40 karakter untuk memastikan tingkat keamanan tinggi. Sekali lagi, aku sangat menyarankan memakai password manager.


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



Kamu juga bisa menyesuaikan ukuran memori cache yang dipakai oleh Bitcoin Core untuk meningkatkan performa (kamu bahkan bisa menambahnya jika punya banyak RAM tersedia):


```
BITCOIND_DB_CACHE=2048
```



Untuk menyimpan perubahan kamu dan menutup editor :




- tekan `Ctrl + X
- ketik `y`
- lalu tekan "*Masukkan*"



### 5.4. Konfigurasi MySQL



Kemudian buka konfigurasi basis data MySQL:



```bash
nano docker-mysql.conf.tpl
```



Masukkan detail login kamu:



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ ***Ganti `ID-mu-di sini` dan `kata sandi-mu-di sini` dengan login kamu sendiri (dengan kata sandi yang kuat dan unik).***



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



Selanjutnya, ada 2 kemungkinan tergantung konfigurasi kamu. Jika Dojo diinstal di mesin terpisah dari komputer harian kamu (misalnya di mesin khusus atau server), masukkan IP Address di jaringan lokal kamu, contohnya:


```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



Untuk mengetahui IP Address lokal mesin kamu, buka terminal lain dan jalankan perintah berikut:


```bash
hostname -I
```



Kemungkinan kedua: jika Dojo dijalankan langsung di komputer pribadi kamu sehari-hari, biarkan nilai default yang sudah ada di file konfigurasi.


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



⚠️ *** Ganti `kata sandi di sini` dengan kredensial kamu sendiri (dengan kata sandi yang kuat dan unik).***



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



Login ini akan memungkinkan kamu masuk ke alat pemeliharaan Dojo nanti. Semua login lain bisa dihapus dari password manager atau catatan tulisan tangan kamu. Mereka tetap bisa diakses dari file konfigurasi Dojo jika suatu saat kamu membutuhkannya.


## 6. Instalasi Dojo



Pada tahap ini, Dojo akan diinstal dan dijalankan di mesin kamu. Proses ini akan meluncurkan beberapa layanan seperti Bitcoin Core, pengindeks Fulcrum, backend Dojo, dan lainnya, sekaligus memulai sinkronisasi penuh blockchain Bitcoin. Proses ini bisa memakan waktu beberapa hari, tergantung perangkat keras dan koneksi internet kamu.


### 6.1. Periksa apakah Docker berfungsi dengan baik



Sebelum memulai instalasi, pastikan bahwa Docker telah beroperasi. Jalankan perintah berikut:



```bash
docker run hello-world
```



Perintah ini akan mengunduh dan menjalankan sebuah container uji kecil. Jika semuanya berjalan lancar, kamu akan melihat pesan yang mirip dengan:


```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



Jika pesan ini tidak ditampilkan, mulailah dengan menyalakan ulang mesin dengan :



```bash
sudo reboot
```



Lalu, masuk kembali ke akun **dojo** kamu dan jalankan perintah uji coba lagi. Jika masih terjadi kesalahan, berarti Docker belum terinstal dengan benar. Dalam kasus ini, kembali ke langkah `2.4.` tentang instalasi Docker dan periksa setiap perintah dengan teliti.


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




- Unduh dan luncurkan kontainer Docker yang diperlukan,
- Menginisialisasi Bitcoin core dan mulai menyinkronkan Blockchain,
- Memulai pengindeks Fulcrum untuk melacak transaksi dan alamat,
- Mengaktifkan backend Dojo dan API-nya.



Kamu akan melihat aliran log yang terus bergulir, dengan referensi warna-warni seperti `bitcoind`, `soroban`, `nodejs`, atau `fulcrum`. Pengguliran ini menunjukkan bahwa Dojo sudah aktif dan berjalan dan mulai menjalankan berbagai layanan.



![Image](assets/fr/31.webp)



### 6.4. Tampilan log keluar



Log muncul secara real time di terminal kamu. Untuk kembali ke prompt perintah saat Dojo berjalan di latar belakang, ketik :



```
Ctrl + C
```



Jangan khawatir: menghentikan tampilan log tidak akan mematikan layanan. Docker tetap menjalankan Dojo di latar belakang, jadi kamu tidak perlu mematikan komputer jika ingin IBD terus berjalan.


### 6.5. Memahami *Pengunduhan Blok Awal* (IBD)



Saat pertama dijalankan, Bitcoin Core harus mengunduh dan memverifikasi seluruh blockchain sejak 2009. Langkah ini disebut **Initial Block Download (IBD).** Ini sangat penting karena memungkinkan node Dojo kamu memverifikasi setiap blok dan transaksi Bitcoin secara mandiri.


Durasi sinkronisasi ini bergantung pada beberapa faktor:




- Kekuatan prosesor kamu dan jumlah memori RAM yang tersedia,
- Kecepatan disk Anda,
- Jumlah dan kualitas peer yang terhubung dengan node Anda,
- Kecepatan koneksi Internet Anda.



Dalam praktiknya, proses ini biasanya memakan waktu antara **2 hingga 7 hari.** Selama periode ini, biarkan mesin kamu tetap menyala. Semakin lama mesin berjalan, semakin cepat sinkronisasi selesai. Aku menyarankan kamu memeriksa status sinkronisasi secara rutin dengan melihat log Bitcoin Core, atau menggunakan alat bantu pemeliharaan Dojo setelah terinstal (lihat bagian selanjutnya).


Untuk memperdalam pengetahuan tentang IBD dan, secara umum, tentang pengoperasian dan peran node Bitcoin kamu, aku menyarankanmu untuk melihat kursus ini:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7. Pemantauan sinkronisasi



Saat pertama kali menginstal Dojo, kamu harus menunggu dua proses utama selesai sepenuhnya: pengunduhan lengkap blockchain Bitcoin (*IBD*) dan pengindeksan blockchain ini oleh Fulcrum. Tergantung koneksi dan performa mesin kamu, ini bisa memakan beberapa hari. Selama periode ini, kamu bisa memantau kemajuan proses untuk memastikan semuanya berjalan lancar.


Ada dua cara untuk memantau status sinkronisasi:




- penggunaan Dojo Maintenance Tool (atau DMT), yang sederhana namun memberikan sedikit detail selama IBD;
- konsultasi langsung log Dojo pada mesin kamu, lebih teknis tetapi jauh lebih tepat.



### 7.1. Periksa melalui Dojo Maintenance Tool (DMT)



Alat Pemeliharaan Dojo adalah antarmuka web yang aman dan memungkinkan kamu memantau status node serta melakukan beberapa operasi tertentu. Ini adalah cara termudah dan paling mudah diakses untuk memantau kemajuan IBD. Selama fase sinkronisasi awal, informasi yang ditampilkan mungkin terbatas. Misalnya, DMT tidak menunjukkan detail kemajuan pengindeksan Fulcrum. Namun, setelah sinkronisasi selesai, DMT akan menampilkan dengan jelas:



- semua lampu pada Green;
- blok terakhir yang divalidasi untuk setiap layanan (Node, Pengindeks, Dojo DB).



Untuk mengaksesnya, kamu perlu mengetahui URL dari DMT milikmu dan menyambungkannya [melalui peramban Tor](https://www.torproject.org/download/). Untuk melakukan ini, buka terminal dan masuk ke direktori `/my-dojo`:



```bash
cd ~/dojo-app/docker/my-dojo
```



Kemudian jalankan perintah berikut ini:



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



Kamu kemudian akan punya akses ke semua informasi terkait koneksi ke Dojo kamu lewat Tor. Yang perlu kita perhatikan di sini adalah URL berikut:


```
Dojo API and Maintenance Tool =
```



Untuk mengakses DMT dari mesin mana pun di jaringan mana pun (bahkan dari jarak jauh), buka Peramban Tor dan masukkan URL ini diikuti dengan `/admin`. Sebagai contoh, jika URL kamu adalah `wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion`, kamu harus memasukkannya di bilah [Tor Browser](https://www.torproject.org/download/):



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ ** Mohon jaga kerahasiaan Address ini



Kemudian kamu akan diarahkan ke halaman autentikasi. DMT masuk menggunakan kata sandi `NODE_ADMIN_KEY` yang telah kamu buat sebelumnya.



![Image](assets/fr/33.webp)



Setelah masuk, kamu bisa mengakses *Dojo Maintenance Tool!* Selama IBD, kamu bisa melihat informasi *Blok Terbaru* di menu *Full node,* yang memberi tahu status terkini node Bitcoin kamu.


![Image](assets/fr/34.webp)



Ingatlah untuk menandai Address ini di Tor Browser untuk memudahkan pencarian di kemudian hari.



Setelah Dojo kamu tersinkronisasi sepenuhnya, kamu akan melihat tanda centang Green pada semua indikator di halaman beranda DMT.



### 7.2. Verifikasi melalui log Dojo



Cara kedua untuk memantau kemajuan IBD adalah dengan melihat log mesin secara langsung. Pendekatan ini memberikan pemantauan yang lebih akurat dan real-time. Kamu bisa melihat bagaimana Bitcoin Core mengunduh blok dan bagaimana Fulcrum mengindeksnya.

Sambungkan ke mesin yang menjalankan Dojo kamu dan buka terminal. Semua perintah dijalankan dari direktori `my-dojo`. Pindah ke folder ini:


```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Log Bitcoin core



Lihat log Bitcoin core untuk melacak kemajuan IBD:



```bash
./dojo.sh logs bitcoind
```



Pada awalnya, kamu akan melihat fase pra-sinkronisasi header blok:



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



Saat angka ini mencapai 100%, Bitcoin Core akan mulai mengunduh seluruh blockchain. Kamu akan melihat kemajuan IBD. Untuk mengetahui tinggi blok saat ini, perhatikan nilai `height=`. Kamu juga bisa mengikuti `progress=`, yang menunjukkan persentase kemajuan IBD.


![Image](assets/fr/36.webp)



Seperti biasa, untuk menutup log dan kembali ke command prompt, gunakan kombinasi `Ctrl + C`.



#### Log titik tumpu



Setelah Bitcoin core menyelesaikan pra-sinkronisasi header, Fulcrum mulai mengindeks Blockchain sambil berjalan. Lihat lognya dengan format :



```bash
./dojo.sh logs fulcrum
```



Kemudian kamu akan melihat ketinggian blok terakhir yang diindeks, ditunjukkan setelah `height:`, serta persentase kemajuan pengindeksan.



![Image](assets/fr/37.webp)



### 7.3. Kerusakan basis data Fulcrum



Fulcrum adalah pengindeks yang sangat kuat, tapi instalasinya bisa rumit, terutama karena manajemen database yang kompleks. Jika terjadi pemadaman listrik atau mesin mati mendadak saat sinkronisasi awal, database pengindeks bisa rusak. Kamu bisa mengetahuinya, misalnya, jika log kamu menunjukkan hal berikut:


```bash
fulcrum | The database has been corrupted etc...
```



**Catatan:** Jenis kesalahan ini akan diperbaiki dengan rilis Fulcrum 2.0 yang akan datang.



Jika ini terjadi, tidak ada dampak pada bitcoind (node Bitcoin kamu): IBD tetap berjalan secara mandiri dari Fulcrum. Namun, kamu tidak akan bisa menggunakan Fulcrum sampai data yang rusak dihapus dan sinkronisasi dimulai ulang. Begini caranya:


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



Kemudian kamu dapat memeriksa apakah Fulcrum berfungsi dengan baik dengan melihat log:



```bash
docker logs -f fulcrum
```




## 8. Menggunakan Alat Pemeliharaan Dojo



Setelah node Bitcoin kamu tersinkronisasi ke kepala blockchain dengan Proof of Work terbanyak, dan blockchain sudah diindeks 100% oleh Fulcrum, kamu bisa mulai menggunakan Dojo.

Dojo menawarkan berbagai fitur yang terus disempurnakan di setiap versi baru. Menurutku, dua yang paling penting adalah:

- Kemampuan menghubungkan Ashigaru Wallet untuk memakai node kamu sendiri dalam melihat data blockchain dan menyiarkan transaksi.

- Block explorer, yang memberi akses ke informasi blockchain Bitcoin tanpa mengekspos data kamu ke pihak eksternal yang tidak kamu kendalikan.

Sekarang, mari kita lihat cara menggunakannya.

### 8.1. Menghubungkan Ashigaru ke Dojo Milikmu



Menghubungkan Ashigaru Wallet ke Dojo sangat mudah: setelah masuk ke DMT, buka menu "Pairing". Sebuah kode QR akan muncul, yang bisa kamu pindai langsung dengan aplikasi Ashigaru.


![Image](assets/fr/38.webp)



Dalam aplikasi Ashigaru, pertama kali kamu meluncurkannya setelah membuat atau memulihkan Wallet, kamu akan diarahkan ke halaman "*Konfigurasi server Dojo Anda*". Tekan "*Pindai QR*", lalu pindai kode QR yang ditampilkan pada DMT kamu.



![Image](assets/fr/39.webp)



Kemudian klik tombol "*Lanjutkan*".



![Image](assets/fr/40.webp)



Sekarang kamu sudah terhubung ke Dojo milikmu.



![Image](assets/fr/41.webp)



### 8.2. Menggunakan Block explorer



Dojo secara otomatis menginstal Block explorer, [BTC-RPC Explorer](https://github.com/janoside/btc-RPC-explorer), yang secara langsung mengambil data dari node Bitcoin Anda sendiri. Penjelajah memungkinkan Anda mengakses informasi mentah dari Blockchain dan Mempool Anda melalui web Interface yang mudah dipahami. Jadi, Anda dapat, misalnya, memeriksa status transaksi yang tertunda, melihat saldo Address, atau memeriksa komposisi blok dengan mudah.




Untuk mengaksesnya, cukup ambil Tor Address dari browser kamu. Caranya, jalankan perintah yang sama seperti yang kamu gunakan untuk mendapatkan Address dari DMT:


```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



Kamu akan memiliki akses ke semua informasi koneksi Dojo kamu melalui Tor. Yang kami minati di sini adalah URL berikut ini:



```
Block Explorer =
```



Kalau kamu sudah terhubung ke DMT Anda, kamu juga dapat menemukan Address ini di menu "*Pairing*", di dalam JSON koneksi:



![Image](assets/fr/43.webp)



Untuk mengakses peramban Anda dari mesin apa pun di jaringan apa pun (bahkan dari jarak jauh), buka [Tor Browser](https://www.torproject.org/download/) dan masukkan URL yang baru saja Anda ambil.



⚠️ ** Mohon jaga kerahasiaan Address ini



Kamu kemudian akan memiliki akses ke Block explorer kamu sendiri.



![Image](assets/fr/44.webp)



*Kredit gambar: https://ashigaru.rs/.*



Untuk melacak transaksi, cukup masukkan txid di bilah pencarian di kanan atas.



![Image](assets/fr/45.webp)



*Kredit gambar: https://ashigaru.rs/.*



Untuk memeriksa gerakan yang terkait dengan Address, lanjutkan dengan cara yang sama dengan memasukkan Address di bilah pencarian.



![Image](assets/fr/46.webp)



*Kredit gambar: https://ashigaru.rs/.*



Kamu juga dapat memasukkan Hash atau tinggi blok di bilah pencarian untuk menampilkan detail.



![Image](assets/fr/47.webp)



*Kredit gambar: https://ashigaru.rs/.*



## 9. Pemeliharaan dojo



### 9.1 Hentikan Dojo Anda



Jangan pernah memutus aliran listrik ke Dojo secara mendadak, karena ini bisa merusak beberapa database, terutama pengindeks Fulcrum. Jika kamu perlu mematikannya, selalu lakukan shutdown Dojo secara menyeluruh terlebih dahulu, lalu setelah semua proses selesai, matikan mesin:


```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 Perbarui Dojo Anda



Dojo berkembang secara teratur dan versi baru dirilis untuk memperbaiki bug, meningkatkan stabilitas, dan menambahkan fitur. Oleh karena itu, penting [untuk memeriksa pembaruan secara teratur](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) dan memperbarui Dojo milikmu. Prosesnya mirip dengan instalasi awal, tetapi mengharuskan Anda mengganti file tertentu dengan versi terbaru yang tersedia, sambil mempertahankan konfigurasi kamu. Berikut ini adalah langkah-langkah terperinci yang harus diikuti untuk pembaruan yang bersih dan aman:



Untuk mengetahui versi Dojo kamu saat ini, jalankan perintah :



```bash
./dojo.sh version
```



Meskipun langkah ini opsional, aku sarankan kamu memulai dengan memperbarui OS. Ini akan mengurangi risiko ketidakcocokan dan memastikan dependensi yang dipakai Dojo sudah versi terbaru:


```bash
sudo apt-get update
sudo apt-get upgrade
```



Buka direktori Dojo dan hentikan layanan yang sedang berjalan:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Kemudian, nyalakan ulang sistem kamu untuk mendapatkan sistem yang bersih:



```bash
sudo reboot
```



Dojo dilengkapi dengan file yang ditandatangani secara digital. Tanda tangan PGP ini memastikan file benar-benar berasal dari pengembang dan tidak diubah. Penting untuk memeriksanya setiap kali kamu memperbarui Dojo, sama seperti saat pertama kali menginstalnya. Mulailah dengan mengunduh kunci publik pengembang lewat Tor, lalu impor:


```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



Kembali ke direktori pribadi milikmu:



```bash
cd ~/
```



Unduh versi terbaru Dojo dari GitHub melalui Tor. Dalam contoh ini, versi yang digunakan adalah versi `1.28.0` (yang belum ada pada saat artikel ini ditulis: ini hanya sebagai contoh). Ingatlah untuk mengganti file dan tautan [dengan versi yang ingin Anda instal](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases):



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



Untuk menjaga semuanya tetap bersih, hapus file yang tidak perlu:



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



Jika layanan berjalan tanpa kesalahan dan log menunjukkan blok sedang diproses, berarti Dojo kamu sekarang sudah diperbarui dan berfungsi.
