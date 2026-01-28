---
name: Bitcoin Core (macOS & Windows)
description: Memasang Bitcoin Core di Mac atau Windows
---

![cover](assets/cover.webp)

Memasang Bitcoin Core di komputer biasa sebenarnya bisa dilakukan, tapi kurang ideal. Kalau kamu nggak keberatan membiarkan komputermu menyala 24/7, cara ini akan berjalan dengan baik. Tapi kalau kamu perlu mematikannya, kamu mungkin bakal merasa kesal karena harus menunggu proses sinkronisasi setiap kali menyalakan perangkat lagi.

Panduan ini ditujukan untuk pengguna Mac atau Windows. Pengguna Linux kemungkinan besar sudah tahu cara melakukannya sendiri, tapi instruksinya kurang lebih mirip dengan yang ada di Mac.

## Mulai Bersih

Idealnya, kamu perlu menggunakan komputer yang bersih, bebas dari malware. Bahkan kalau kamu pakai hardware wallet, malware tetap bisa menipu kamu dan membuatmu kehilangan bitcoin.

Kamu bisa menghapus semua data di komputer lama dan menjadikannya komputer khusus untuk Bitcoin, atau beli komputer/laptop baru yang memang didedikasikan untuk itu.

## Hard Drive

Bitcoin Core akan memakan sekitar 400 gigabyte ruang di drive kamu, dan ukurannya akan terus bertambah seiring waktu. Kamu bisa memakai drive internal, tapi bisa juga menambahkan hard drive eksternal. Aku akan jelaskan dua opsi itu.
Idealnya, kamu pakai solid-state drive (SSD). Kalau komputermu tergolong lama, kemungkinan besar belum punya SSD internal. Cukup beli SSD eksternal berukuran 1 atau 2 terabyte dan gunakan itu. Drive biasa memang bisa dipakai, tapi kamu mungkin akan menghadapi berbagai masalah dan kecepatannya akan jauh lebih lambat.

![image](assets/fr/01.webp)

## Unduh Bitcoin Core

Kunjungi situs bitcoin.org (**pastikan kamu tidak pergi ke bitcoin.com**, itu situs shitcoin milik Roger Ver yang menipu orang supaya membeli Bitcoin Cash alih-alih Bitcoin).
Setelah kamu sampai di sana, agak aneh karena letak unduhan perangkat lunaknya tidak langsung terlihat jelas. Buka menu Resources, lalu klik Bitcoin Core, seperti yang ditunjukkan pada gambar di bawah ini:

![image](assets/fr/02.webp)

Ini akan membawamu ke halaman unduhan:

![image](assets/fr/03.webp)

Klik tombol oranye Unduh Bitcoin Core:

![image](assets/fr/04.webp)

Ada beberapa opsi yang bisa kamu pilih tergantung pada jenis komputermu. Dua opsi pertama yang relevan untuk panduan ini adalah Windows dan Mac. Pilih salah satu dari bilah sebelah kiri. Setelah kamu mengkliknya, proses unduhan akan dimulai secara otomatis, biasanya tersimpan di folder Downloads.

## Verifikasi unduhan (bagian 1)

Kamu memerlukan file yang berisi hash dari berbagai rilis. File ini dulu tersedia di halaman unduhan bitcoin.org, tapi sekarang telah dipindahkan ke bitcoincore.org/en/download:

![image](assets/fr/05.webp)

Kamu memerlukan file hash biner SHA256. File ini berisi hash SHA256 dari berbagai paket unduhan Bitcoin Core.

Selanjutnya, kita perlu meng-hash unduhan Bitcoin Core dan membandingkannya dengan nilai yang ada di file tersebut. Dengan begitu, kita bisa memastikan unduhan identik dengan yang diharapkan menurut bitcoincore.org.

Kembali ke direktori Unduhan dan jalankan perintah ini (ganti X dengan nama file unduhan node Bitcoin penuh secara tepat):

```bash
shasum -a 256 XXXXXXXXXXXX # <--- UNTUK MAC
certutil -hashfile XXXXXXXXXXX SHA256 # <--- UNTUK WINDOWS
```

Kamu akan mendapatkan output hash. Catat, lalu bandingkan dengan hash yang ada di file SHA256SUMS.

Jika outputnya identik, berarti kamu sudah memverifikasi bahwa tidak ada bit data yang berubah… hampir. Kita masih perlu memastikan file SHA256SUMS aman.

Untuk langkah berikutnya, kita harus memastikan gpg terinstal di komputer. Untuk itu, lihat panduan SHA256/gpg-ku, gulir sekitar setengah halaman ke bagian "Download gpg", dan cari subjudul sesuai sistem operasi kamu. Setelah itu, kembali ke sini.

## Dapatkan Kunci Publik

Kembali ke halaman unduhan, dapatkan file tanda tangan hash SHA256

![image](assets/fr/06.webp)

Klik dan simpan file ke disk, sebaiknya direktori Downloads.

File ini berisi tanda tangan oleh berbagai orang, dari file SHA256SUMS.

Kami ingin kunci publik pengembang utama, Wladimir J. van der Laan di gantungan kunci komputer kita. ID kunci publiknya adalah:
1 - 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964

Salin teks tersebut ke dalam perintah berikut:

```bash
gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 01EA5486DE18A882D4C2684590C8019E36C2E964
```

Sebagai informasi, kapan saja kamu bisa melihat kunci apa saja yang ada di keychain komputer kamu dengan perintah ini:

```bash
gpg --list-keys
```

## Verifikasi unduhan (bagian 2)

Kita sudah punya kunci publik, jadi sekarang kita bisa memverifikasi file SHA256SUMS yang berisi hash unduhan Bitcoin Core, sekaligus tanda tangan untuk hash tersebut.

Buka Terminal atau CMD lagi, dan pastikan Anda berada di direktori Downloads. Dari sana, jalankan perintah ini:

```bash
gpg –verify SHA256SUMS.asc SHA256SUMS
```

File pertama yang tercantum adalah ejaan tepat dari file tanda tangan. File kedua adalah ejaan tepat dari file teks yang berisi hash. Kedua file harus berada di direktori yang sama, dan kamu harus berada di direktori tersebut; jika tidak, kamu perlu mengetikkan jalur lengkap untuk masing-masing file.

Ini adalah output yang seharusnya kamu dapatkan:

![image](assets/fr/07.webp)

Aman untuk mengabaikan pesan PERINGATAN – itu cuma mengingatkan kamu bahwa kamu belum pernah bertemu Wladimir secara langsung untuk menanyakan kunci publiknya, lalu memberi tahu komputer agar mempercayai kunci ini sepenuhnya.

Kalau kamu melihat pesan ini, berarti sekarang kamu tahu bahwa file SHA256SUMS.asc tidak diubah setelah ditandatangani oleh Wladimir.

## Instal Bitcoin Core

Kamu tidak seharusnya memerlukan instruksi rinci tentang cara menginstal programnya.

![image](assets/fr/08.webp)

## Jalankan Bitcoin Core

Di Mac, kamu mungkin mendapatkan peringatan (Apple masih anti-Bitcoin)

![image](assets/fr/09.webp)

Klik OK, lalu buka Preferensi Sistem kamu.

![image](assets/fr/10.webp)

Klik ikon Keamanan dan Privasi:

![image](assets/fr/11.webp)

Kemudian klik "buka bagaimanapun juga":

![image](assets/fr/12.webp)

Kesalahan akan muncul lagi, tetapi kali ini kamu akan memiliki tombol BUKA yang tersedia. Klik itu.

![image](assets/fr/13.webp)

Bitcoin Core harus dijalankan, dan kamu akan disajikan beberapa opsi:

![image](assets/fr/14.webp)

Di sini kamu bisa memilih untuk menggunakan jalur default tempat blockchain akan diunduh, atau memilih drive eksternal. Aku sarankan jangan mengubah jalur default jika kamu menggunakan drive internal, supaya lebih mudah saat menginstal perangkat lunak lain yang akan berkomunikasi dengan Bitcoin Core.

Kamu juga bisa memilih untuk menjalankan node yang dipangkas, yang menghemat ruang, tapi membatasi apa yang bisa kamu lakukan dengan node. Bagaimanapun, kamu akan mengunduh seluruh blockchain dan memverifikasinya, jadi kalau punya cukup ruang, simpan semua yang sudah diunduh dan jangan pangkas kalau bisa dihindari.

Setelah kamu konfirmasi, blockchain akan mulai diunduh. Proses ini bisa memakan waktu berhari-hari.
![image](assets/fr/15.webp)

Kamu bisa mematikan komputer dan kembali lagi untuk melanjutkan pengunduhan kapan saja, ini tidak akan merusak apa pun.
