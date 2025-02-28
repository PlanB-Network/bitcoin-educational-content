---
name: RaspiBlitz
description: Panduan untuk mengatur RaspiBlitz Anda
---

![image](assets/0.webp)

RaspiBlitz adalah sebuah proyek DIY (Do-It-Yourself) untuk Node Lightning (LND dan/atau Core Lightning) yang berjalan bersama dengan Bitcoin-Fullnode di RaspberryPi (1TB SSD) dan dilengkapi dengan layar yang memudahkan pengaturan & pemantauan.

RaspiBlitz terutama ditujukan untuk belajar cara menjalankan node Anda sendiri secara terdesentralisasi dari rumah - karena: Bukan Node Anda, Bukan Aturan Anda. Temukan & kembangkan ekosistem yang berkembang dari Lightning Network dengan menjadi bagian penuh darinya. Bangun sebagai bagian dari workshop atau proyek akhir pekan Anda sendiri.

![video](https://youtu.be/DTHlSPMz3ns)
RASPIBLITZ - Cara Menjalankan Lightning dan Bitcoin Full Node oleh BTC session

# Panduan Pengaturan Raspiblitz Parman

Raspiblitz adalah sistem yang sangat baik untuk menjalankan Bitcoin Node dan aplikasi terkait. Saya merekomendasikan ini dan node My Node kepada sebagian besar pengguna (Idealnya memiliki dua node untuk redundansi.) Salah satu keuntungan utama adalah node Raspiblitz adalah "Perangkat Lunak Sumber Terbuka Gratis", tidak seperti MyNode atau Umbrel. Mengapa itu penting? Vlad Costa menjelaskan. Anda juga dapat menjalankan RaspbiBlitz dengan koneksi WiFi daripada ethernet – berikut panduan tambahan untuk itu. (Saya belum menemukan cara untuk melakukan ini dengan MyNode).

Anda dapat membeli node yang sudah jadi dengan layar mini terpasang, atau Anda dapat membangunnya sendiri (Anda tidak memerlukan layar).

Panduan di halaman github sangat baik, tetapi mungkin terlalu rinci untuk pengguna yang cukup berpengalaman. Instruksi saya akan lebih ringkas dan mudah-mudahan lebih mudah Anda ikuti.

Pada dasarnya, prosesnya sangat mirip dengan proses pengaturan node MyNode dengan Raspberry Pi 4. Panduan Raspiblitz menyarankan Anda membeli monitor, tetapi Anda benar-benar tidak memerlukannya, dan saya tidak merekomendasikannya. Anda bahkan tidak memerlukan keyboard atau mouse tambahan. Cukup akses menu terminal perangkat melalui komputer di jaringan rumah yang sama, dan gunakan perintah ssh menggunakan terminal. Ini mungkin dilakukan dengan Linux/Mac (mudah) dan sedikit lebih sulit dengan Windows.

## Langkah 1: Beli peralatan.

Anda memerlukan peralatan yang sama persis yang Anda butuhkan untuk menjalankan node MyNode. Anda bisa mencoba salah satu atau yang lain, satu-satunya perbedaan adalah data pada kartu micro SD.

- Raspberry Pi 4, memori 4Gb atau 8Gb (4Gb sudah cukup)
- Power Resmi Raspberry Pi (Sangat Penting! Jangan membeli yang generik, serius)
- Casing untuk Pi. (Casing FLIRC sangat keren. Seluruh casing adalah heat sink dan Anda tidak memerlukan kipas, yang bisa berisik)
- Kartu microSD 32 Gb (Anda memerlukan satu, tetapi beberapa akan berguna.)
- Pembaca kartu memori (sebagian besar komputer tidak memiliki slot untuk kartu microSD).
- Hard drive eksternal SSD 1Tb.
- Kabel ethernet (untuk menghubungkan ke router rumah Anda).

Anda tidak memerlukan monitor (atau keyboard atau mouse)

Catatan: Ini adalah hard drive yang salah: Ini adalah hard drive eksternal portabel. Ini bukan SSD. SSD sangat penting. Inilah mengapa harganya murah (Harga dalam AUD)

![image](assets/1.webp)

Ini adalah tipe yang benar untuk didapatkan:

![image](assets/2.webp)

Ini lebih cepat, tetapi tidak perlu mahal:

![image](assets/3.webp)

## Langkah 2: Unduh Gambar Raspiblitz
Arahkan ke situs web github Raspiblitz, dan temukan tautan "unduh gambar":
![image](assets/4.webp)

Hash sha-256 dari file yang diunduh disediakan di situs web. Ini akan berubah dengan setiap pembaruan. Jika Anda tidak mengerti apa ini, Anda seharusnya, jadi saya menulis panduan yang bisa Anda baca di sini.

![image](assets/5.webp)

## Langkah 3: Verifikasi Gambar

Sebelum melanjutkan, jika Anda tidak tahu cara berkeliling sistem file di baris perintah, itu mudah untuk dipelajari, dan Anda seharusnya.

Berikut adalah video yang berguna untuk Linux, tetapi berlaku untuk Mac juga.

Untuk Windows, berikut adalah tutorial sederhana.
Mac/Linux

Tunggu file selesai diunduh (penting!), dan kemudian buka terminal, navigasikan ke tempat Anda mengunduh file, dan ketik perintah berikut…

```bash
shasum -a 256 xxxxxxxxxxxxxx
```

di mana xxxxxxxxxxxxxx adalah nama file yang baru saja Anda unduh. Jika Anda tidak berada di direktori tempat file tersebut, Anda harus mengetikkan jalur lengkapnya.

Komputer berpikir selama sekitar 20 detik atau lebih. Periksa bahwa hashfile keluaran cocok dengan yang diunduh dari situs web pada langkah sebelumnya. Jika identik, Anda dapat melanjutkan.
Windows

Buka prompt perintah dan navigasikan ke tempat file diunduh, dan ketik perintah ini:

```bash
certUtil -hashfile xxxxxxxxxxxxxxx SHA256
```

di mana xxxxxxxxxxxxxx adalah nama file yang baru saja Anda unduh. Jika Anda tidak berada di direktori tempat file tersebut, Anda harus mengetikkan jalur lengkapnya.

Komputer berpikir selama sekitar 20 detik atau lebih. Periksa bahwa hashfile keluaran cocok dengan yang diunduh dari situs web pada langkah sebelumnya. Jika identik, Anda dapat melanjutkan.

## Langkah 4: Flash kartu SD

Anda dapat menggunakan Balena Etcher untuk melakukan ini. Unduh di sini.

Etcher mudah digunakan. Masukkan kartu micro SD Anda dan flash perangkat lunak Raspiblitz (.img file) ke kartu SD.

![image](assets/6.webp)

![image](assets/7.webp)

![image](assets/8.webp)

![image](assets/9.webp)

Setelah selesai, drive tidak lagi dapat dibaca. Anda mungkin mendapatkan kesalahan dari sistem operasi, dan drive harus menghilang dari desktop. Tarik keluar kartunya.

## Langkah 5: Siapkan Pi dan masukkan kartu SD

Bagian-bagiannya (kasus tidak ditampilkan):

![image](assets/10.webp)

![image](assets/11.webp)

Sambungkan kabel ethernet, dan konektor USB hard drive (belum daya). Hindari menyambungkan ke port USB berwarna biru di tengah. Mereka adalah USB 3. Gunakan port USB 2, meskipun drive mungkin mampu USB 3 (lebih andal).

![image](assets/12.webp)

Kartu micro SD masuk di sini:

![image](assets/13.webp)

Akhirnya, sambungkan daya:

![image](assets/14.webp)

## Langkah 6: Temukan alamat IP dari Pi

Anda tidak pernah memerlukan monitor dengan Raspiblitz. Namun, Anda memerlukan komputer lain di jaringan rumah. Jika Pi Anda tidak terhubung melalui ethernet, dan Anda ingin mengandalkan WiFi, menemukan IP memerlukan beberapa keterampilan komputer. Maaf, tidak bisa membantu Anda. Anda memerlukan koneksi ethernet. (Masalahnya berasal dari perlu mengakses monitor dan sistem operasi untuk menghubungkan WiFi dan memasukkan kata sandi.)

Periksa router Anda, untuk daftar semua IP dari semua perangkat yang terhubung.
Saya mengetik 192.168.0.1 di Browser (instruksi yang disertakan dengan router saya), masuk, dan dapat melihat perangkat saya dengan IP 192.168.0.191. Perhatikan bahwa alamat IP ini tidak terlihat secara publik di internet (mereka melewati router terlebih dahulu), mereka hanya pengenal untuk perangkat di jaringan rumah Anda.
Menemukan IP sangat penting.

> PEMBARUAN: Anda dapat menggunakan terminal pada mesin Mac atau Linux untuk menemukan alamat IP dari semua perangkat yang terhubung Ethernet di jaringan rumah menggunakan perintah “arp -a”. Outputnya tidak sebagus yang akan ditampilkan router, tetapi semua informasi yang Anda butuhkan ada di sana. Jika tidak jelas mana yang Pi, lakukan percobaan dan kesalahan.

## Langkah 7: SSH ke Pi

Ingat untuk memasukkan kartu SD ke Pi sebelum menyalakannya. Tunggu beberapa menit, lalu di Linux/Mac lain, buka terminal.

Untuk Mac/Linux, di terminal ketik:

```bash
ssh admin@Alamat_IP_Pi_Anda
```

Untuk Windows, Anda perlu menginstal putty untuk ssh ke Pi. Ketik perintah yang sama seperti di atas.

Pertama kali Anda melakukan ini, atau kapan pun Anda mengganti OS Pi dengan mengganti kartu SD, Anda mungkin atau mungkin tidak mendapatkan kesalahan ini…

![image](assets/15.webp)

Cara memperbaikinya adalah dengan menavigasi ke tempat file “known_hosts” berada (pesan kesalahan memberi tahu Anda), dan menghapusnya. Perintahnya adalah "rm known_hosts"

Kemudian, ulangi perintah ssh untuk masuk. Ini yang akan terjadi…

![image](assets/16.webp)

Ketik yes (kata penuh) untuk melanjutkan.

Jika berhasil, Anda akan diminta kata sandi. Ini bukan untuk komputer Anda, tetapi untuk raspiblitz. Kata sandi umumnya adalah “raspiblitz”, dan Anda akan mengubahnya nanti. Jendela terminal akan berubah menjadi biru dan Anda akan memiliki opsi menu seperti menu DOS lama. Navigasi dengan tombol panah atau mouse.

![image](assets/17.webp)

Ikuti petunjuknya, atur kata sandi Anda, dan kemudian akan mendeteksi hard drive Anda dan memberi Anda opsi untuk memformatnya jika diperlukan.

Kemudian Anda akan ditanya apakah Anda ingin menyalin data blockchain dari sumber lain atau mengunduhnya kembali. Menyalinnya adalah proses pembelajaran dan instruksinya cukup baik, dan baik untuk disimpan….

![image](assets/18.webp)

Cara yang sederhana namun lebih lambat adalah mengunduh seluruh rantai dari awal…

![image](assets/19.webp)

Banyak teks akan berkedip di layar terminal. Anda mungkin mengira itu adalah proses pengunduhan blockchain, tetapi menurut saya, itu menghasilkan kunci pribadi untuk komunikasi.

Kemudian opsi lightning muncul.

![image](assets/20.webp)

Buat kata sandi baru untuk mengunci dompet lightning Anda, kemudian dompet baru akan dibuat dan Anda akan diberikan 24 kata untuk dituliskan…

![image](assets/21.webp)

Pastikan Anda menuliskannya dan menyimpannya dengan aman. Saya mendengar tentang seseorang yang tidak melakukannya karena dia tidak berencana menggunakan lightning, tetapi setahun kemudian memutuskan untuk menggunakannya, dan membuka saluran. Kemudian menyadari kata-katanya tidak dicadangkan, dan saya ingat tidak mungkin untuk mengekstrak kata-kata lagi dari perangkat, dia harus menutup semua salurannya dan memulai lagi. Dia berhasil melakukannya, tetapi orang lain mungkin tidak seberuntung itu.

Setelah ini, beberapa menit teks menggulir ke bawah jendela terminal. Kemudian…

![image](assets/22.webp)
Anda akan keluar dari sesi ssh. Masuk kembali, kali ini dengan password baru Anda, password A. Setelah masuk, Anda akan diminta password C untuk membuka dompet lightning Anda.
Sekarang kita tunggu. Sampai jumpa dalam 2 minggu. Anda bisa menutup terminal, itu tidak berpengaruh apa-apa pada Pi, itu hanya jendela komunikasi.

![image](assets/23.webp)

Jika karena alasan apa pun, Anda ingin mematikan Pi sebelum blockchain selesai diunduh, itu tidak masalah selama Anda melakukannya dengan benar. Blockchain akan melanjutkan pengunduhan dari tempat terakhir sekali Anda terhubung kembali.

Tekan CTRL+c untuk keluar dari layar biru. Anda akan mengakses terminal Linux Pi. Di sini Anda dapat mengetik “menu” yang memuat layar berikut, dan dari sana Anda dapat mematikan Pi.

![image](assets/24.webp)

AKHIR dari panduan

Jadi dari sekarang node Anda siap untuk digunakan. Jika Anda masih membutuhkan bantuan untuk menavigasi lebih banyak opsi, rujuk ke github untuk lebih banyak tutorial dan panduan https://github.com/raspiblitz/raspiblitz#feature-documentation