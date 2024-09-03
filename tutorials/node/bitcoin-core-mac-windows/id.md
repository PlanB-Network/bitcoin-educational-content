---
name: Noeud Bitcoin Core (mac & windows)
description: Memasang Bitcoin Core di Mac atau Windows
---

Memasang Bitcoin Core di komputer biasa bisa dilakukan, namun tidak ideal. Jika Anda tidak keberatan meninggalkan komputer Anda menyala 24/7, maka ini akan berfungsi dengan baik. Jika Anda perlu mematikan komputer, akan terasa menjengkelkan menunggu perangkat lunak untuk sinkron setiap kali Anda menyalakannya kembali.

Instruksi ini untuk Pengguna Mac atau Windows. Pengguna Linux kemungkinan besar tidak memerlukan bantuan saya, namun instruksi untuk Linux sangat mirip dengan Mac.

## Mulai Bersih

Idealnya, Anda ingin menggunakan komputer yang bersih, satu tanpa malware. Bahkan jika Anda menggunakan dompet perangkat keras, malware dapat menipu Anda keluar dari koin Anda.

Anda bisa menghapus bersih komputer lama, dan menggunakannya sebagai komputer Bitcoin yang didedikasikan, atau membeli komputer/laptop yang didedikasikan.

## Hard Drive

Bitcoin Core akan mengambil sekitar 400 gigabyte data di drive Anda, dan akan terus bertambah. Anda dapat menggunakan drive internal Anda, tetapi Anda juga dapat menambahkan hard drive eksternal. Saya akan menjelaskan kedua opsi tersebut. Idealnya, Anda harus menggunakan solid-state drive. Jika Anda memiliki komputer lama, kemungkinan besar tidak memiliki salah satu dari ini secara internal. Cukup beli SSD eksternal 1 atau 2 terabyte dan gunakan itu. Drive reguler mungkin akan bekerja, tetapi Anda mungkin akan mengalami masalah dan akan jauh lebih lambat.

![image](assets/1.webp)

## Unduh Bitcoin Core

Pergi ke bitcoin.org (pastikan Anda tidak pergi ke bitcoin.com, yang merupakan situs shitcoin milik Roger Ver, menipu orang untuk membeli Bitcoin Cash alih-alih Bitcoin)

Setelah di sana, secara aneh tidak jelas di mana mendapatkan perangkat lunaknya. Pergi ke menu sumber daya dan klik "Bitcoin Core", seperti ditunjukkan di bawah ini:

![image](assets/2.webp)

Ini akan membawa Anda ke halaman unduhan:

![image](assets/3.webp)

Klik tombol oranye Unduh Bitcoin Core:

![image](assets/4.webp)

Ada beberapa opsi untuk dipilih, tergantung pada komputer Anda. Dua pertama relevan dengan panduan ini; pilih Windows atau Mac di bilah kiri. Ini akan mulai mengunduh setelah Anda mengkliknya, kemungkinan besar ke direktori Unduhan Anda.

## Verifikasi unduhan (bagian 1)

Anda memerlukan file yang berisi hash dari berbagai rilis. File ini dulu ada di halaman unduhan bitcoin.org, tetapi sekarang telah pindah ke bitcoincore.org/en/download:

![image](assets/5.webp)

Anda memerlukan file hash biner SHA256. File ini berisi hash SHA256 dari berbagai paket unduhan Bitcoin Core.

Selanjutnya, kita perlu meng-hash unduhan Bitcoin Core dan membandingkannya dengan apa yang dikatakan file tersebut hash seharusnya. Kemudian kita tahu unduhan identik dengan apa yang diharapkan, menurut bitcoincore.org.

Navigasikan ke direktori Unduhan lagi dan eksekusi perintah ini (ganti X dengan nama file unduhan node bitcoin penuh secara tepat):

```bash
shasum -a 256 XXXXXXXXXXXX # <--- UNTUK MAC
certutil -hashfile XXXXXXXXXXX SHA256 # <--- UNTUK WINDOWS
```

Anda akan mendapatkan output hash. Catat itu, dan bandingkan dengan hash yang terkandung dalam file SHA256SUMS.

Jika outputnya identik, maka Anda telah memverifikasi bahwa tidak ada bit data yang telah diubah... hampir. Kita masih perlu memastikan file SHA256SUMS tidak berbahaya.

Untuk melanjutkan ke langkah berikutnya, kita harus memiliki gpg terinstal di komputer kita.
Untuk melakukan itu, lihat panduan SHA256/gpg saya, dan gulir sekitar setengah jalan ke bagian "Download gpg", dan cari subjudul sistem operasi Anda. Kemudian kembali ke sini.
## Dapatkan Kunci Publik

Kembali ke halaman unduhan, dapatkan file tanda tangan hash SHA256

![image](assets/6.webp)

Klik dan simpan file ke disk, sebaiknya direktori Downloads.

File ini berisi tanda tangan oleh berbagai orang, dari file SHA256SUMS.

Kami ingin kunci publik pengembang utama, Wladimir J. van der Laan di gantungan kunci komputer kita. ID kunci publiknya adalah:
1 - 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964

Salin teks tersebut ke dalam perintah berikut:

```bash
gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 01EA5486DE18A882D4C2684590C8019E36C2E964
```

Sebagai informasi, kapan saja, Anda dapat melihat kunci apa saja yang ada di gantungan kunci komputer dengan perintah ini:

```bash
gpg --list-keys
```

## Verifikasi unduhan (bagian 2)

Kami memiliki kunci publik, jadi sekarang kami dapat memverifikasi file SHA256SUMS yang berisi hash dari unduhan Bitcoin Core, dan tanda tangan untuk hash tersebut.

Buka Terminal atau CMD lagi, dan pastikan Anda berada di direktori Downloads. Dari sana, jalankan perintah ini:

```bash
gpg –verify SHA256SUMS.asc SHA256SUMS
```

File pertama yang terdaftar adalah ejaan tepat dari file tanda tangan. File kedua yang terdaftar harus menjadi ejaan tepat dari file teks yang berisi hash. Kedua file harus berada dalam direktori yang sama dan Anda perlu berada dalam direktori file tersebut, jika tidak, Anda harus mengetikkan jalur lengkap untuk setiap file.

Ini adalah output yang harus Anda dapatkan

![image](assets/7.webp)

Aman untuk mengabaikan pesan PERINGATAN – itu hanya mengingatkan Anda bahwa Anda belum bertemu Wladimir di bagian kunci dan secara pribadi bertanya kepadanya apa kunci publiknya, dan kemudian memberitahu komputer Anda untuk mempercayai kunci ini sepenuhnya.

Jika Anda mendapatkan pesan ini, Anda sekarang tahu bahwa file SHA256SUMS.asc tidak telah diubah setelah Wladimir menandatanganinya.

## Instal Bitcoin Core

Anda tidak seharusnya memerlukan instruksi rinci tentang cara menginstal programnya.

![image](assets/8.webp)

## Jalankan Bitcoin Core

Di Mac, Anda mungkin mendapatkan peringatan (Apple masih anti-Bitcoin)

![image](assets/9.webp)

Klik OK, lalu buka Preferensi Sistem Anda

![image](assets/10.webp)

Klik ikon Keamanan dan Privasi:

![image](assets/11.webp)

Kemudian klik "buka bagaimanapun juga":

![image](assets/12.webp)

Kesalahan akan muncul lagi, tetapi kali ini Anda akan memiliki tombol BUKA yang tersedia. Klik itu.

![image](assets/13.webp)

Bitcoin Core harus dimuat dan Anda akan disajikan dengan beberapa opsi:

![image](assets/14.webp)

Di sini Anda dapat memilih untuk menggunakan jalur default untuk tempat blockchain akan diunduh, atau Anda dapat memilih drive eksternal Anda. Saya merekomendasikan tidak mengubah jalur default jika Anda akan menggunakan drive internal, itu membuat hal-hal lebih mudah untuk diatur saat Anda menginstal perangkat lunak lain untuk berkomunikasi dengan Bitcoin Core.
Anda dapat memilih untuk menjalankan node yang dipangkas, ini menghemat ruang, tetapi membatasi apa yang dapat Anda lakukan dengan node Anda. Bagaimanapun, Anda akan mengunduh seluruh blockchain dan memverifikasinya, jadi jika Anda memiliki ruang, simpan apa yang telah Anda unduh, dan jangan pangkas jika Anda bisa menghindarinya.
Setelah Anda konfirmasi, blockchain akan mulai diunduh. Ini akan memakan waktu berhari-hari.

![image](assets/15.webp)

Anda dapat mematikan komputer dan kembali untuk mengunduh jika Anda mau, ini tidak akan menyebabkan kerusakan.