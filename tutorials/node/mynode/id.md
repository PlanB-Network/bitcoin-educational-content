---
name: My Node
description: Menyiapkan MyNode Bitcoin Anda
---

![image](assets/0.webp)

https://mynodebtc.com/

Cara termudah dan paling kuat untuk menjalankan Node Bitcoin dan Lightning! Kami menggabungkan perangkat lunak sumber terbuka terbaik dengan antarmuka, manajemen, dan dukungan kami sehingga Anda dapat dengan mudah, secara pribadi, dan aman menggunakan Bitcoin dan Lightning.

## Jenis-jenis Penyediaan Node

Ada berbagai penyediaan Node. MyNode sangat luar biasa. Ada banyak aplikasi yang disertakan dengannya, dan bahkan lebih banyak lagi jika Anda membayar untuk versi premium. Jika tidak, mengunduh semua aplikasi tersebut sendiri sangat merepotkan. MyNode membuatnya cukup mudah seperti yang akan Anda lihat.

Sebuah alternatif dan opsi serupa adalah RaspiBlitz. GUI tidak sebagus itu, dan aplikasi-aplikasinya banyak yang tumpang tindih dengan aplikasi yang disertakan dengan MyNode, tetapi Raspiblitz adalah perangkat lunak sumber terbuka gratis (FOSS) dan MyNode tidak sepenuhnya demikian. Perbedaan lain adalah MyNode dijalankan dalam kontainer Docker. Saya menemukan Docker menakutkan dan sulit untuk di-troubleshoot. Ini hanya menjadi masalah jika Anda menemui kesalahan atau bug. Pengembang menawarkan bantuan untuk pengguna premium dan ada juga grup chat Telegram.

RaspiBlitz hanyalah beberapa program yang diinstal di Linux, tanpa Docker. Hard drive eksternal dapat dengan mudah dipasang ke mesin Linux lain dengan Bitcoin Core, dan Anda dapat langsung menggunakan, jika perlu.

Opsi lain adalah hanya menginstal Bitcoin Core dan berbagai Server Electrum (ada beberapa) pada sistem operasi. Saya memiliki panduan untuk Linux (Raspberry Pi), Mac, dan Windows.

## Daftar Belanja

- Raspberry Pi 4, memori 4Gb atau 8Gb (4Gb sudah cukup)

- Power Resmi Raspberry Pi (Sangat Penting! Jangan membeli yang generik, serius)

- Sebuah casing untuk Pi. Casing FLIRC sangat keren. Seluruh casing adalah heat sink dan Anda tidak memerlukan kipas, yang bisa berisik

- Kartu microSD 16 Gb (Anda memerlukan satu, tetapi beberapa akan berguna)

- Pembaca kartu memori (kebanyakan komputer tidak memiliki slot untuk kartu microSD).

- Hard drive eksternal SSD 1Tb.  
  Catatan: SSD sangat penting. jangan gunakan hard drive eksternal portabel meskipun harganya lebih murah

- Kabel ethernet (untuk menghubungkan ke router rumah Anda)

- Anda tidak memerlukan monitor

## Unduh Gambar MyNode

Navigasikan ke situs web MyNode Link

![image](assets/1.webp)

Klik <Download Now>

Unduh versi Raspberry Pi 4:

![image](assets/2.webp)

Ini adalah file besar:

![image](assets/3.webp)

Unduh hash SHA 256

![image](assets/4.webp)

Buka terminal di Mac atau Linux atau Command Prompt untuk Windows. Ketik:

```bash
shasum -a 256 NAMABERKASUNDUHAN # <--- Mac/Linux
certUtil -hashfile NAMABERKASUNDUHAN SHA256 # <--- Windows
```

Komputer berpikir selama 20 detik atau lebih. Kemudian, periksa bahwa output hashfile cocok dengan yang diunduh dari situs web pada langkah sebelumnya. Jika identik, Anda dapat melanjutkan.
Flash kartu SD

## Unduh dan instal Balena Etcher. Link

Saya tidak dapat menemukan tanda tangan digital untuk ini. Jika Anda tahu caranya, tolong beritahu saya dan saya akan memperbarui artikel ini.

Etcher mudah digunakan. Masukkan kartu micro SD Anda dan flash perangkat lunak Raspberry Pi (.img file) ke kartu SD.

![image](assets/5.webp)
![image](assets/6.webp)
Setelah selesai, drive tersebut tidak lagi dapat dibaca. Anda mungkin akan mendapatkan pesan error dari sistem operasi, dan drive tersebut akan menghilang dari desktop. Cabut kartunya.

## Siapkan Pi dan masukkan kartu SD

Bagian-bagiannya (case tidak ditampilkan):

![image](assets/12.webp)
![image](assets/13.webp)

Sambungkan kabel ethernet, dan konektor USB hard drive (belum termasuk daya). Hindari menyambungkan ke port USB berwarna biru di tengah. Itu adalah USB 3. MyNode menyarankan Anda menggunakan port USB 2, meskipun drive tersebut mungkin mendukung USB 3.

![image](assets/14.webp)

Kartu micro SD dimasukkan di sini:

![image](assets/15.webp)

Akhirnya, sambungkan daya:

![image](assets/16.webp)

## Temukan alamat IP dari Pi

Anda tidak perlu monitor dengan MyNode. Namun, Anda memerlukan komputer lain di jaringan rumah. Jika Pi Anda tidak terhubung melalui ethernet, dan Anda ingin mengandalkan WiFi, menemukan IP memerlukan keterampilan komputer tingkat tinggi. Maaf, tidak bisa membantu. Anda memerlukan koneksi ethernet. (Masalahnya berasal dari perlu mengakses monitor dan sistem operasi untuk terhubung ke WiFi dan memasukkan kata sandi).

Periksa router Anda, untuk daftar semua IP dari semua perangkat yang terhubung.

Saya mengetik 192.168.0.1 di Browser (instruksi yang datang dengan router saya), login, dan dapat melihat perangkat "MyNode" dengan IP 192.168.0.18. Catat bahwa alamat IP ini tidak terlihat secara publik ke internet (mereka melewati router terlebih dahulu), mereka hanya pengenal untuk perangkat di jaringan rumah Anda.

Menemukan IP sangat penting.

> UPDATE: Anda dapat menggunakan terminal pada komputer Mac atau Linux untuk menemukan alamat IP dari semua perangkat yang terhubung Ethernet di jaringan rumah menggunakan perintah “arp -a”. Outputnya tidak sebagus yang akan ditampilkan router, tetapi semua informasi yang Anda butuhkan ada di sana. Jika tidak jelas mana yang adalah Pi, lakukan trial and error.

## SSH ke dalam Pi

Anda memiliki opsi untuk login ke perangkat dari jarak jauh melalui perintah SSH, tetapi ini tidak diperlukan (diperlukan jika RaspiBlitz Node). Saya akan menunjukkan caranya bagaimanapun, karena ini sangat berguna.

Buka komputer Mac atau Linux (untuk Windows, unduh putty, sebuah alat SSH) dan ketik:

```bash
ssh admin@192.168.0.18
```

Gunakan alamat IP Anda sendiri. Nama pengguna untuk perangkat MyNode adalah “admin” secara default. Kata sandinya adalah “bolt” secara default.

Jika Anda telah menggunakan Pi Anda sebelumnya dan mengganti kartu micro SD, Anda akan mendapatkan error ini:

![image](assets/17.webp)

Yang perlu Anda lakukan adalah menavigasi ke tempat file “known_hosts” berada dan menghapusnya. Aman untuk dilakukan. Pesan error menunjukkan Anda jalurnya. Untuk saya itu adalah /Users/NamaPenggunaSaya/.ssh/

Jangan lupa “.” sebelum ssh, ini menunjukkan itu adalah direktori tersembunyi.

Kemudian coba perintah ssh lagi.

Kali ini Anda akan melihat output ini:

![image](assets/18.webp)

File yang Anda hapus telah dihapus dan Anda menambahkan sidik jari baru. Ketik yes dan <enter>.

Anda akan diminta untuk memasukkan kata sandi. Kata sandinya adalah “bolt”
Anda sekarang memiliki akses terminal ke MyNode Pi, tanpa monitor, dan dapat memastikan semuanya berjalan lancar.

## Akses melalui Web Browser

Buka browser. Ini harus dilakukan dari komputer di jaringan rumah Anda, Anda tidak bisa melakukan ini dari luar. Ada caranya, tapi sulit. Saya belum mencobanya.

Ketik alamat IP di jendela alamat browser. Ini yang akan terjadi:

Masukkan kata sandi "bolt" – ubah nanti.

Kemudian ini yang akan terjadi:

Pilih Format Drive

Sekarang kita tunggu.

Pada suatu titik Anda akan ditanya apakah Anda ingin memasukkan kunci produk Anda, atau menggunakan edisi "komunitas" gratis — Saya akan menunjukkan edisi Premium. Saya merekomendasikan untuk membayar versi premium jika Anda mampu, sangat berharga.

Anda kemudian akan melihat progres dari blok yang diunduh. Ini memakan waktu berhari-hari:

Aman untuk mematikan mesin selama pengunduhan jika Anda perlu. Pergi ke pengaturan dan temukan tombol untuk mematikan mesin. Jangan sekadar mencabut kabel, Anda bisa merusak instalasi atau hard drive.

Pastikan, sejak awal, pergi ke "Pengaturan" dan nonaktifkan quicksync. Ini akan memulai pengunduhan blok awal dari awal.

Saya ingin melanjutkan dengan membuat panduan, jadi inilah MyNode lain yang saya siapkan sebelumnya. Ini tampilan halaman ketika blockchain telah disinkronkan, dan beberapa "aplikasi" telah diaktifkan dan disinkronkan:

Perhatikan bahwa Electrum Server juga perlu disinkronkan, jadi segera setelah Bitcoin Blockchain disinkronkan, klik tombol untuk memulai proses itu – memakan waktu satu atau dua hari. Semuanya lainnya diaktifkan dalam beberapa menit setelah Anda memilih untuk mengaktifkannya. Anda dapat mengklik hal-hal dan menjelajah. Anda tidak akan merusak apa pun. Jika sesuatu rusak (ini terjadi pada saya, tapi saya pikir karena saya memiliki bagian yang murah) Anda harus melakukan flash ulang dan mulai mengunduh lagi. Masalah yang saya miliki dengan MyNode adalah jika Anda perlu "melakukan flash ulang" Anda akhirnya perlu memulai sinkronisasi blockchain lagi dari awal. Ada cara teknis untuk mengatasi ini, tapi tidak mudah.

Jika Anda ingin mencoba node lain juga, misalnya RaspiBlitz, Anda memerlukan hard drive eksternal SSD tambahan, dan kartu micro SD lain untuk di-flash. Selain itu, peralatannya sama, Anda hanya tidak bisa menjalankan MyNode dan RaspiBlitz secara bersamaan, jelas. Jika Anda ingin melakukan itu, saatnya untuk berbelanja Raspberry Pi lain.

Sekarang Anda memiliki node yang berjalan, gunakan, jangan biarkan itu hanya duduk di sana tidak melakukan apa-apa untuk Anda. Ikuti artikel (dan video) saya tentang cara menghubungkan Electrum Desktop Wallet Anda ke Electrum Server dan Bitcoin Core di sini.