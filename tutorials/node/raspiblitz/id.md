---
name: RaspiBlitz
description: Panduan untuk mengatur RaspiBlitz kamu
---

![image](assets/0.webp)

RaspiBlitz adalah proyek DIY (Do-It-Yourself) untuk Node Lightning (LND dan atau Core Lightning) yang berjalan bersama Bitcoin full node di Raspberry Pi dengan SSD 1 TB dan dilengkapi layar yang memudahkan pengaturan dan pemantauan.

RaspiBlitz terutama ditujukan untuk belajar cara menjalankan node kamu sendiri secara terdesentralisasi dari rumah, karena: Bukan Node Kamu, Bukan Aturan Kamu. Temukan dan kembangkan ekosistem Lightning Network yang terus tumbuh dengan benar benar jadi bagian di dalamnya. Bangun sebagai bagian dari workshop atau proyek akhir pekan kamu sendiri.

![video](https://youtu.be/DTHlSPMz3ns)
RASPIBLITZ - Cara Menjalankan Lightning dan Bitcoin Full Node oleh BTC session

# Panduan Pengaturan Raspiblitz Parman

RaspiBlitz adalah sistem yang sangat baik untuk menjalankan node Bitcoin dan aplikasi terkait. Aku merekomendasikan ini dan node MyNode ke sebagian besar pengguna, idealnya punya dua node untuk redundansi. Salah satu keuntungan utama adalah bahwa node RaspiBlitz merupakan "Free Open Source Software", tidak seperti MyNode atau Umbrel. [Mengapa itu penting? Vlad Costa menjelaskan.](https://bitcoin-takeover.com/why-bitcoin-free-open-source-software-matters/amp/?__twitter_impression=true) Kamu juga bisa menjalankan Raspiblitz dengan koneksi WiFi daripada ethernet – berikut adalah [panduan tambahan](https://armantheparman.com/headless-wifi/). (Aku belum menemukan cara untuk melakukan ini dengan MyNode).

Kamu bisa membeli node yang sudah jadi dengan layar mini terpasang, atau kamu bisa membangunnya sendiri. Kamu sebenarnya tidak perlu layar.

[Panduan di halaman GitHub](https://github.com/rootzoll/raspiblitz) sangat bagus, tetapi mungkin terlalu rinci untuk pengguna dengan pengalaman sedang. Instruksi saya akan lebih ringkas dan semoga lebih mudah diikuti.

Pada dasarnya, proses ini sangat mirip dengan proses menyiapkan [node MyNode](https://armantheparman.com/mynode-bitcoin-node-easy-setup-guide-raspberry-pi/) dengan Raspberry Pi 4. Panduan RaspiBlitz menyarankan kamu membeli monitor, tapi sebenarnya kamu tidak membutuhkannya dan aku juga tidak akan merekomendasikannya. Kamu juga tidak perlu keyboard atau mouse tambahan. Cukup akses menu terminal perangkat lewat komputer di jaringan rumah yang sama dan gunakan perintah ssh lewat terminal. Ini mudah dilakukan di Linux atau Mac, dan sedikit lebih ribet kalau pakai Windows.

## Langkah 1: Beli peralatan.

Kamu memerlukan perlengkapan yang sama persis seperti saat menjalankan node MyNode. Kamu bisa coba salah satu atau yang lain, karena satu satunya perbedaan ada pada data di kartu microSD.

- Raspberry Pi 4, memori 4Gb atau 8Gb (4Gb sudah cukup)
- Power Resmi Raspberry Pi (Sangat Penting! Jangan membeli yang generik, serius)
- Casing untuk Pi. (Casing FLIRC sangat keren. Seluruh casing adalah heat sink dan Anda tidak memerlukan kipas, yang bisa berisik)
- Kartu microSD 32 Gb (kamu memerlukan satu, tetapi beberapa akan berguna.)
- Pembaca kartu memori (sebagian besar komputer tidak memiliki slot untuk kartu microSD).
- Hard drive eksternal SSD 1Tb.
- Kabel ethernet (untuk menghubungkan ke router rumah Anda).

Kamu nggak memerlukan monitor (atau keyboard atau mouse)

Catatan: Ini adalah hard drive yang salah: Ini adalah hard drive eksternal portabel. Ini bukan SSD. SSD sangat penting. Inilah mengapa harganya murah (Harga dalam AUD)

![image](assets/1.webp)

Ini adalah tipe yang benar untuk didapatkan:

![image](assets/2.webp)

Ini lebih cepat, tetapi tidak perlu mahal:

![image](assets/3.webp)

## Langkah 2: Unduh Gambar Raspiblitz
Arahkan ke [situs GitHub Raspiblitz](https://github.com/rootzoll/raspiblitz), dan temukan tautan “download image”:
![image](assets/4.webp)

Hash sha256 dari file yang kamu unduh disediakan di situs web. Angkanya akan berubah setiap kali ada pembaruan. Kalau kamu belum ngerti soal ini, sebaiknya kamu pelajari, jadi aku sudah bikin panduan yang bisa kamu baca di sini.

![image](assets/5.webp)

## Langkah 3: Verifikasi Gambar

Sebelum lanjut, kalau kamu belum tahu cara bernavigasi di sistem file lewat command line, itu gampang dipelajari dan memang seharusnya kamu kuasai.

Berikut adalah [video yang berguna untuk Linux, tetapi juga berlaku untuk Mac](https://youtu.be/id3DGvljhT4?list=PLtK75qxsQaMLZSo7KL-PmiRarU7hrpnwK).

Untuk Windows, berikut adalah [tutorial sederhana](https://www.youtube.com/watch?v=MBBWVgE0ewk&t=1s).
_PEMBARUAN: Verifikasi pgp/gpg sekarang tersedia. Anda memerlukan kunci publik Openoms. [Di sini](http://parman.org/downloadable/openoms.txt) ada (Anda mungkin perlu mode penyamaran agar tautan berfungsi – http, bukan https)_
Mac/Linux

Tunggu sampai file selesai diunduh (penting!), lalu buka terminal, pindah ke folder tempat file itu diunduh, dan ketik perintah berikut…

```bash
shasum -a 256 xxxxxxxxxxxxxx
```

di mana xxxxxxxxxxxxxx adalah nama file yang baru aja kamu unduh. Kalau kamu nggak berada di direktori tempat file tersebut, kamu harus mengetikkan jalur lengkapnya.

Komputer akan memproses selama sekitar 20 detik atau lebih. Periksa apakah hash file yang dihasilkan cocok dengan yang diunduh dari situs web sebelumnya. Jika sama, kamu bisa melanjutkan.

Windows

Buka prompt perintah dan navigasikan ke tempat file diunduh, dan ketik perintah ini:

```bash
certUtil -hashfile xxxxxxxxxxxxxxx SHA256
```

di mana xxxxxxxxxxxxxx adalah nama file yang baru aja kamu unduh. Kalau kamu tidak berada di direktori tempat file tersebut, kamu harus mengetikkan jalur lengkapnya.

Komputer akan memproses selama sekitar 20 detik atau lebih. Pastikan hash file yang dihasilkan cocok dengan yang diunduh dari situs web pada langkah sebelumnya. Jika sama, kamu bisa melanjutkan.

## Langkah 4: Flash kartu SD

Kamu bisa menggunakan Balena Etcher untuk melakukan ini. [Unduh di sini](https://www.balena.io/etcher/).

Etcher mudah dipakai. Masukkan kartu micro SD dan flash perangkat lunak Raspiblitz (.img file) ke kartu SD.

![image](assets/6.webp)

![image](assets/7.webp)

![image](assets/8.webp)

![image](assets/9.webp)

Setelah selesai, drive tidak akan bisa dibaca lagi. Kamu mungkin mendapat pesan kesalahan dari sistem operasi, dan drive akan hilang dari desktop. Cabut kartunya.

## Langkah 5: Siapkan Pi dan masukkan kartu SD

Bagian-bagiannya (kasus tidak ditampilkan):

![image](assets/10.webp)

![image](assets/11.webp)

Sambungkan kabel ethernet dan konektor USB hard drive (belum diberi daya). Hindari menyambungkan ke port USB berwarna biru di tengah karena itu USB 3. Gunakan port USB 2, meskipun drive kamu mendukung USB 3, karena ini lebih andal.

![image](assets/12.webp)

Kartu micro SD masuk di sini:

![image](assets/13.webp)

Akhirnya, sambungkan daya:

![image](assets/14.webp)

## Langkah 6: Temukan alamat IP dari Pi

Kamu tidak pernah benar-benar membutuhkan monitor dengan RaspiBlitz. Namun, kamu memerlukan komputer lain di jaringan rumah. Jika Pi kamu tidak terhubung lewat ethernet dan kamu ingin pakai WiFi, menemukan IP butuh sedikit keterampilan komputer. Maaf, aku tidak bisa membantu soal ini. Kamu memang perlu koneksi ethernet karena masalahnya terkait akses monitor dan sistem operasi untuk menghubungkan WiFi serta memasukkan kata sandi.

Periksa router kamu untuk daftar semua IP dari perangkat yang terhubung. Aku mengetik 192.168.0.1 di browser (sesuai instruksi routerku), masuk, dan bisa melihat perangkat dengan IP 192.168.0.191. Ingat, alamat IP ini tidak terlihat secara publik di internet, mereka hanya pengenal perangkat di jaringan rumahmu. Menemukan IP sangat penting.

PEMBARUAN: Kamu bisa pakai terminal di Mac atau Linux untuk menemukan alamat IP semua perangkat yang terhubung lewat Ethernet di jaringan rumah dengan perintah “arp -a”. Outputnya mungkin tidak sejelas yang ditampilkan router, tapi semua info yang kamu butuhkan ada di sana. Kalau tidak jelas mana Pi, pakai cara coba-coba.

## Langkah 7: SSH ke Pi

Ingat untuk memasukkan kartu SD ke Pi sebelum menyalakannya. Tunggu beberapa menit, lalu di Linux/Mac lain, buka terminal.

Untuk Mac/Linux, di terminal ketik:

```bash
ssh admin@Alamat_IP_Pi_Anda
```

Untuk Windows, kamu perlu menginstal [putty](http://putty.org/) untuk ssh ke Pi. Ketik perintah yang sama seperti di atas.

Pertama kali kamu melakukan ini, atau kapan pun kamu mengganti OS Pi dengan mengganti kartu SD, kamu mungkin saja mengalami kesalahan ini…

![image](assets/15.webp)

Cara memperbaikinya adalah dengan pergi ke folder tempat file “known_hosts” berada (pesan kesalahan akan memberitahumu), lalu hapus file itu dengan perintah: `rm known_hosts`.

Setelah itu, ulangi perintah ssh untuk masuk. Ini yang akan terjadi…

![image](assets/16.webp)

Ketik yes (kata penuh) untuk melanjutkan.

Jika berhasil, kamu akan diminta memasukkan kata sandi. Ini bukan untuk komputermu, tapi untuk RaspiBlitz. Kata sandi bawaan biasanya “raspiblitz”, dan nanti akan kamu ubah. Jendela terminal akan berubah menjadi biru, dan kamu akan melihat menu seperti menu DOS lama. Navigasi bisa pakai tombol panah atau mouse.

![image](assets/17.webp)

Ikuti petunjuknya, atur kata sandimu, lalu RaspiBlitz akan mendeteksi hard drive kamu dan memberi opsi untuk memformatnya jika diperlukan.

Selanjutnya, kamu akan ditanya apakah ingin menyalin data blockchain dari sumber lain atau mengunduhnya kembali. Menyalinnya adalah proses yang bagus untuk dipelajari, instruksinya cukup jelas, dan baik untuk disimpan.

![image](assets/18.webp)

Cara yang lebih sederhana, tapi lebih lambat, adalah mengunduh seluruh chain dari awal…

![image](assets/19.webp)

Akan ada banyak teks yang berkedip di layar terminal. Kamu mungkin mengira itu proses mengunduh blockchain, tapi menurutku itu sedang membuat kunci pribadi untuk komunikasi.

Setelah itu, opsi Lightning akan muncul.

![image](assets/20.webp)

Buat kata sandi baru untuk mengunci dompet Lightning kamu, lalu dompet baru akan dibuat dan kamu akan diberikan 24 kata yang harus kamu tulis…

![image](assets/21.webp)

Pastikan kamu menuliskannya dan menyimpannya dengan aman. Aku pernah dengar tentang seseorang yang awalnya tidak melakukannya karena tidak berencana pakai Lightning, tapi setahun kemudian memutuskan untuk menggunakannya dan membuka saluran. Saat itu dia sadar kata-katanya tidak dicadangkan, dan tidak mungkin mengambil kata-kata itu lagi dari perangkat. Dia harus menutup semua salurannya dan memulai ulang. Untungnya dia berhasil, tapi orang lain mungkin tidak seberuntung itu.

Setelah ini, beberapa menit teks menggulir ke bawah jendela terminal. Kemudian…

![image](assets/22.webp)
Kamu akan keluar dari sesi ssh. Masuk kembali, kali ini dengan password baru kamu, password A. Setelah masuk, kamu akan diminta memasukkan password C untuk membuka dompet Lightning kamu.
Sekarang kita tunggu. Sampai jumpa dalam 2 minggu. Kamu bisa menutup terminal, itu tidak berpengaruh apa-apa pada Pi, karena itu hanya jendela komunikasi.

![image](assets/23.webp)

Kalau karena alasan apa pun kamu ingin mematikan Pi sebelum blockchain selesai diunduh, itu tidak masalah selama dilakukan dengan benar. Blockchain akan melanjutkan pengunduhan dari titik terakhir saat kamu terhubung kembali.

Tekan CTRL+c untuk keluar dari layar biru. Kamu akan masuk ke terminal Linux Pi. Di sini, ketik “menu” untuk memunculkan layar berikut, dan dari sana kamu bisa mematikan Pi.

![image](assets/24.webp)

AKHIR dari panduan

Jadi sekarang node kamu siap digunakan. Kalau masih butuh bantuan untuk menjelajahi lebih banyak opsi, lihat GitHub untuk tutorial dan panduan lebih lengkap: https://github.com/raspiblitz/raspiblitz#feature-documentation
