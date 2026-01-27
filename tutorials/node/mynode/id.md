---
name: My Node
description: Menyiapkan MyNode Bitcoin Milikmu
---

![image](assets/cover.webp)

https://mynodebtc.com/

Cara paling sederhana dan paling kuat untuk menjalankan Node Bitcoin dan Lightning! Kami menggabungkan perangkat lunak open source terbaik dengan antarmuka, manajemen, dan dukungan kami supaya kamu bisa menggunakan Bitcoin dan Lightning dengan mudah, privat, dan aman.

## Jenis-jenis Penyediaan Node

Ada berbagai cara untuk menyiapkan node. MyNode benar-benar keren. Ada banyak aplikasi yang langsung disertakan, dan bakal lebih banyak lagi kalau kamu pakai versi premium. Kalau nggak, mengunduh semua aplikasi itu satu per satu bakal sangat merepotkan. MyNode bikin semuanya jadi jauh lebih gampang seperti yang bakal kamu lihat nanti.

Alternatif lain yang mirip adalah RaspiBlitz. GUI-nya nggak sebagus itu, dan banyak aplikasinya tumpang tindih dengan yang ada di MyNode, tapi Raspiblitz adalah perangkat lunak FOSS gratis dan MyNode nggak sepenuhnya demikian. Perbedaan lainnya adalah MyNode berjalan dalam kontainer Docker. Buat aku, Docker itu agak menakutkan dan sulit di-troubleshoot. Ini cuma jadi masalah kalau kamu ketemu error atau bug. Pengembang menyediakan bantuan untuk pengguna premium, dan ada juga grup chat Telegram.

RaspiBlitz cuma sekumpulan program yang diinstal di Linux tanpa Docker. Hard drive eksternal bisa dengan mudah dipasang ke mesin Linux lain yang punya Bitcoin Core, dan kamu bisa langsung pakai kalau memang perlu.

Opsi lain adalah cukup menginstal Bitcoin Core dan berbagai server Electrum (ada beberapa jenis) di sistem operasi kamu. Aku punya panduan untuk Linux (Raspberry Pi), Mac, dan Windows.

## Daftar Belanja

- Raspberry Pi 4, memori 4 Gb atau 8 Gb (4 Gb sudah cukup)

- Power resmi Raspberry Pi (sangat penting, jangan beli yang generik, serius)

- Casing untuk Pi. Casing FLIRC keren banget. Seluruh casing berfungsi sebagai heat sink dan kamu nggak butuh kipas yang biasanya berisik

- Kartu microSD 16 Gb (kamu butuh satu, tapi punya beberapa bakal berguna)

- Pembaca kartu memori (kebanyakan komputer nggak punya slot microSD)

- Hard drive eksternal SSD 1 Tb
Catatan: SSD itu penting. jangan pakai hard drive eksternal portabel walaupun lebih murah

- Kabel ethernet (buat menghubungkan ke router rumah kamu)

- Kamu nggak butuh monitor

## Unduh .img MyNode

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

Komputer akan memproses selama sekitar 20 detik atau lebih. Setelah itu, cek apakah hash file output cocok dengan hash yang kamu unduh dari situs web pada langkah sebelumnya. Kalau identik, kamu bisa lanjut.

Flash kartu SD

## Unduh dan instal Balena Etcher. Link

Aku belum menemukan tanda tangan digital untuk bagian ini. Kalau kamu tahu caranya, tolong kasih tahu aku dan nanti artikel ini bakal aku perbarui.

Etcher gampang banget dipakai. Masukkan kartu microSD kamu lalu flash perangkat lunak Raspberry Pi (file .img) ke kartu SD.

![image](assets/5.webp)
![image](assets/6.webp)

Setelah selesai, drive itu nggak akan bisa dibaca lagi. Kamu mungkin bakal dapat pesan error dari sistem operasi, dan drive itu akan hilang dari desktop. Cabut kartunya.

## Siapkan Pi dan masukkan kartu SD

Bagian-bagiannya (case tidak ditampilkan):

![image](assets/12.webp)
![image](assets/13.webp)

Sambungkan kabel ethernet dan konektor USB untuk hard drive (belum termasuk daya). Hindari mencolokkannya ke port USB berwarna biru di tengah. Itu adalah USB 3. MyNode menyarankan kamu memakai port USB 2 walaupun hard drive kamu mungkin mendukung USB 3.

![image](assets/14.webp)

Kartu micro SD dimasukkan di sini:

![image](assets/15.webp)

Akhirnya, sambungkan daya:

![image](assets/16.webp)

## Temukan alamat IP dari Pi

Kamu nggak perlu monitor untuk MyNode. Tapi kamu butuh komputer lain di jaringan rumah. Kalau Pi kamu nggak terhubung lewat ethernet dan kamu ingin mengandalkan WiFi, mencari IP itu butuh skill komputer tingkat lanjut. Maaf, aku nggak bisa bantu soal itu. Kamu memang harus pakai koneksi ethernet. (Masalahnya muncul karena kamu perlu akses monitor dan sistem operasi untuk menyambungkan ke WiFi dan masukin kata sandi).

Cek router kamu untuk melihat daftar semua IP dari perangkat yang terhubung.

Aku cukup mengetik 192.168.0.1 di browser (sesuai instruksi dari router aku), login, lalu bisa melihat perangkat bernama "MyNode" dengan IP 192.168.0.18. Perlu dicatat kalau alamat IP ini nggak terlihat publik di internet karena semuanya lewat router dulu. IP ini cuma jadi pengenal perangkat di jaringan rumah kamu.

Menemukan IP itu penting.

> UPDATE: Kamu bisa pakai terminal di komputer Mac atau Linux untuk menemukan alamat IP dari semua perangkat yang terhubung via ethernet di jaringan rumah dengan perintah “arp -a”. Outputnya memang nggak sebagus tampilan di router, tapi semua info yang kamu butuhin ada di situ. Kalau nggak jelas mana yang Pi, pakai cara trial and error.

## SSH ke dalam Pi

Kamu punya opsi untuk login ke perangkat dari jarak jauh lewat perintah SSH, tapi ini nggak wajib (beda dengan RaspiBlitz yang memang perlu). Aku tetap bakal tunjukin caranya karena ini sangat berguna.

Buka komputer Mac atau Linux (untuk Windows, unduh putty, sebuah alat SSH) dan ketik:

```bash
ssh admin@192.168.0.18
```

Gunakan alamat IP milik kamu sendiri. Nama pengguna default untuk perangkat MyNode adalah “admin”. Kata sandinya juga default, yaitu “bolt”.

Kalau kamu pernah memakai Pi itu sebelumnya dan mengganti kartu microSD, kamu bakal dapet error seperti ini:
![image](assets/17.webp)

Yang perlu kamu lakukan cuma pergi ke lokasi file “known_hosts” dan hapus file itu. Ini aman untuk dilakukan. Pesan error bakal nunjukin jalurnya. Di aku lokasinya adalah /Users/NamaPenggunaSaya/.ssh/

Jangan lupa ada “.” sebelum ssh karena itu menandakan direktori tersembunyi.

Setelah itu coba perintah ssh lagi.

Kali ini kamu bakal melihat output seperti ini:

![image](assets/18.webp)

File yang tadi kamu hapus sudah benar-benar hilang dan kamu baru saja menambahkan fingerprint yang baru. Ketik yes lalu tekan <enter>.

Setelah itu kamu akan diminta memasukkan kata sandi. Kata sandinya adalah “bolt”.

Sekarang kamu sudah punya akses terminal ke MyNode Pi tanpa perlu monitor, dan kamu bisa memastikan semuanya berjalan lancar.

## Akses melalui Web Browser

Buka browser. Ini harus dilakukan dari komputer yang ada di jaringan rumah kamu, kamu nggak bisa melakukannya dari luar. Ada caranya, tapi rumit. Aku sendiri belum pernah coba.

Ketik alamat IP ke kolom alamat browser. Ini yang bakal muncul:

Masukkan kata sandi "bolt" – nanti kamu ganti.

Lalu ini yang bakal muncul:

Pilih Format Drive

Sekarang tinggal tunggu.

Di satu titik kamu akan ditanya apakah kamu mau memasukkan product key atau memakai edisi komunitas yang gratis. Aku bakal nunjukin edisi Premium. Aku rekomendasikan bayar versi premium kalau kamu mampu, sangat worth it.

Setelah itu kamu bakal melihat progres pengunduhan blok. Proses ini makan waktu beberapa hari:

Mesin aman untuk dimatikan selama proses pengunduhan kalau memang perlu. Masuk ke pengaturan dan cari tombol untuk mematikan mesin. Jangan langsung mencabut kabel karena kamu bisa merusak instalasi atau hard drive.

Pastikan sejak awal kamu masuk ke “Pengaturan” dan nonaktifkan quicksync. Ini bakal membuat proses initial block download dimulai dari awal.

Karena aku ingin lanjut bikin panduan, berikut tampilan MyNode lain yang sudah aku siapkan sebelumnya. Ini adalah tampilan halaman ketika blockchain sudah tersinkronisasi dan beberapa aplikasi sudah diaktifkan dan disinkronkan:

Perhatikan bahwa Electrum Server juga harus disinkronkan. Jadi segera setelah Bitcoin Blockchain selesai sinkron, klik tombol untuk memulai proses itu. Ini makan waktu satu sampai dua hari. Semua hal lain aktif dalam beberapa menit setelah kamu memilih untuk mengaktifkannya. Kamu bisa klik apa saja dan menjelajah. Kamu nggak akan merusakkan apa pun. Kalau sesuatu crash (ini pernah terjadi ke aku, tapi sepertinya karena aku pakai komponen yang murah) kamu harus flash ulang dan mulai unduh dari awal. Masalah dengan MyNode adalah kalau kamu harus flash ulang, kamu akhirnya harus memulai sinkronisasi blockchain dari nol lagi. Ada cara teknis untuk menghindari ini, tapi nggak mudah.

Kalau kamu ingin mencoba node lain juga, misalnya RaspiBlitz, kamu butuh SSD eksternal tambahan dan satu kartu microSD lagi untuk di-flash. Selain itu, peralatannya sama. Kamu cuma nggak bisa menjalankan MyNode dan RaspiBlitz secara bersamaan. Kalau mau begitu, saatnya beli Raspberry Pi tambahan.

Sekarang node kamu sudah berjalan, gunakan. Jangan cuma dibiarkan nganggur. Ikuti artikel dan video aku tentang cara menghubungkan Electrum Desktop Wallet ke Electrum Server dan Bitcoin Core di sini.
