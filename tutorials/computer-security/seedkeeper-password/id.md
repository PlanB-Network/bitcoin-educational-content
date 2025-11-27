---
name: Penyimpanan Benih - Pengelola Kata Sandi
description: Bagaimana cara menyimpan kata sandi Anda dengan kartu pintar Seedkeeper?
---

![cover](assets/cover.webp)



Seedkeeper adalah kartu pintar yang dikembangkan oleh Satochip, sebuah perusahaan Belgia yang berspesialisasi dalam solusi perangkat keras untuk mengelola dan melindungi rahasia digital. Terkenal dengan rangkaian kartu pintarnya untuk ekosistem Bitcoin, Satochip menciptakan Seedkeeper sebagai alternatif dari metode tradisional dalam menyimpan frasa mnemonik dan rahasia digital lainnya.



Secara konkret, Seedkeeper berbentuk kartu pintar bersertifikasi EAL6 yang multifungsi dengan prosesor yang aman dan memori anti rusak (yang disebut "Secure Element"). Seperti namanya, perannya adalah untuk menyimpan mnemonik portofolio Bitcoin dan kata sandi secara terenkripsi dan terlindungi. Dengan Seedkeeper, Anda dapat generate, mengimpor, mengatur, dan menyimpan rahasia Anda secara langsung di dalam komponen kartu yang aman.



Menurut pendapat saya, Seedkeeper memiliki dua kegunaan utama, yang akan kita bahas dalam 2 tutorial terpisah:




- Penyimpanan frasa mnemonik Bitcoin**: alih-alih menuliskan 12 atau 24 kata di atas kertas, Anda dapat mengimpornya ke dalam kartu pintar dan melindunginya dengan kode PIN.
- Manajemen kata sandi**: Anda dapat membuat kata sandi yang kuat melalui aplikasi Seedkeeper dan menyimpannya langsung di dalam kartu pintar, memberikan Anda pengelola kata sandi offline yang nyaman dan mudah digunakan.



Secara teknis, Seedkeeper memiliki kapasitas 8192 byte, memungkinkannya untuk menyimpan minimal 50 rahasia yang terpisah (jumlah yang tepat akan tergantung pada ukuran dan metadata yang terkait dengan masing-masing rahasia). Seedkeeper dapat diakses baik [melalui pembaca kartu pintar yang terhubung](https://satochip.io/accessories/) ke komputer, atau melalui aplikasi seluler dengan koneksi NFC. Seluruh sistem beroperasi dalam mode offline, tanpa koneksi internet, menjamin permukaan serangan yang terbatas.



![Image](assets/fr/001.webp)



Fitur yang sangat menarik adalah kemampuan untuk menduplikasi konten dari satu Seedkeeper ke Seedkeeper lainnya untuk membuat cadangan. Dalam tutorial ini, kami akan menunjukkan kepada Anda cara melakukannya.



Dalam tutorial ini, kita hanya akan membahas penggunaan SeedKeeper untuk kata sandi tradisional, seperti halnya pengelola kata sandi. Jika Anda ingin menggunakan SeedKeeper untuk menyimpan frasa mnemonik Bitcoin wallet, silakan lihat tutorial lainnya:



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

## 1. Bagaimana cara mendapatkan Seedkeeper?



Ada dua cara utama untuk mendapatkan Seedkeeper. Anda dapat [membelinya langsung dari toko resmi Satochip](https://satochip.io/product/seedkeeper/) atau dari pengecer resmi. Tetapi karena [applet Seedkeeper adalah sumber terbuka] (https://github.com/Toporin/Seedkeeper-Applet), Anda juga memiliki pilihan untuk menginstalnya sendiri pada [kartu pintar kosong] (https://satochip.io/product/blank-javacard-for-diy-project/).



Jika Anda ingin menggunakan fungsionalitas pencadangan Seedkeeper, Anda tentu saja perlu membeli dua kartu pintar.



## 2. Menginstal klien Seedkeeper



Langkah pertama adalah menginstal perangkat lunak pada komputer atau smartphone Anda. Pada PC, Anda harus [mengunduh versi terbaru Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). Pada ponsel, aplikasi Seedkeeper tersedia di [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) dan di [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 3. Inisialisasi pemilik benih



Luncurkan aplikasi dan klik tombol "*Klik & Pindai*".



![Image](assets/fr/003.webp)



Anda akan diminta kode PIN untuk Seedkeeper Anda. Karena ini adalah kartu baru, belum ada PIN yang ditentukan. Masukkan kode apa pun untuk melewati langkah ini, lalu klik "*Next*".



![Image](assets/fr/004.webp)



Kemudian letakkan kartu di bagian belakang ponsel cerdas Anda. Aplikasi akan mendeteksi bahwa Seedkeeper belum diinisialisasi, dan akan meminta Anda untuk mengatur kode PIN kartu pintar Anda, antara 4 hingga 16 karakter. Untuk keamanan optimal, pilihlah kode PIN yang kuat yang panjangnya sepanjang mungkin, acak, dan terdiri dari berbagai macam karakter. PIN ini adalah satu-satunya penghalang terhadap akses fisik ke kata sandi Anda.



**Ingatlah juga untuk menyimpan PIN ini sekarang juga**, contohnya di dalam pengelola kata sandi, atau di media fisik yang terpisah. Dalam kasus terakhir, jangan pernah menyimpan media yang berisi PIN di tempat yang sama dengan Seedkeeper Anda, jika tidak, keamanan ini tidak akan berguna. Penting untuk memiliki cadangan yang dapat diandalkan: tanpa PIN, Anda tidak akan dapat memulihkan rahasia yang tersimpan di Seedkeeper.



![Image](assets/fr/005.webp)



Konfirmasikan kode PIN Anda untuk kedua kalinya.



![Image](assets/fr/006.webp)



Seedkeeper Anda sekarang telah diinisialisasi. Anda dapat membukanya dengan memasukkan kode PIN yang baru saja Anda tetapkan.



![Image](assets/fr/007.webp)



Sekarang Anda akan dibawa ke halaman manajemen kartu pintar Anda.



![Image](assets/fr/008.webp)



## 4. Menyimpan kata sandi di Seedkeeper



Setelah Seedkeeper Anda terbuka, klik tombol "*+*".



![Image](assets/fr/009.webp)



Pilih "Buat rahasia*". Opsi "*Import a secret*" memungkinkan Anda menyimpan rahasia yang sudah ada (misalnya, kata sandi yang pernah Anda buat sebelumnya).



![Image](assets/fr/010.webp)



Dalam kasus kami, kami ingin menyimpan kata sandi. Klik pada "*Kata Sandi*".



![Image](assets/fr/011.webp)



Tetapkan "*Label*" pada rahasia ini agar dapat dengan mudah diidentifikasi jika Anda menyimpan beberapa informasi di Seedkeeper. Anda juga dapat menambahkan pengenal yang terkait dengan kata sandi dan URL situs.



![Image](assets/fr/012.webp)



Pilih panjang dan parameter kata sandi Anda, lalu klik "*Generate*", kemudian "*Import*".



![Image](assets/fr/013.webp)



Tempatkan Seedkeeper Anda di bagian belakang ponsel cerdas Anda.



![Image](assets/fr/014.webp)



Kata sandi Anda telah terdaftar.



![Image](assets/fr/015.webp)



## 5. Mengakses kata sandi Seedkeeper Anda



Jika Anda ingin memeriksa kata sandi Anda, ambil Seedkeeper Anda dan klik tombol "*Klik & Pindai*".



![Image](assets/fr/016.webp)



Masukkan kode PIN Anda, lalu tekan "*Next*".



![Image](assets/fr/017.webp)



Tempatkan Seedkeeper Anda di bagian belakang ponsel cerdas Anda.



![Image](assets/fr/018.webp)



Ini akan membawa Anda ke daftar semua rahasia Anda yang terdaftar. Dalam contoh ini, saya ingin menampilkan kata sandi untuk akun Plan ₿ Academy saya, jadi saya klik di atasnya.



![Image](assets/fr/019.webp)



Tekan tombol "*Mengungkapkan*".



![Image](assets/fr/020.webp)



Pindai kembali Seedkeeper Anda.



![Image](assets/fr/021.webp)



Kata sandi Anda yang disimpan sebelumnya sekarang muncul di layar. Anda dapat menyalinnya dan menggunakannya di situs web yang relevan.



![Image](assets/fr/022.webp)



## 6. Mencadangkan Penyimpanan Benih



Sekarang kita akan membuat cadangan Seedkeeper saya di Seedkeeper kedua sehingga kita memiliki dua salinan. Pengulangan ini dapat menjadi bagian dari strategi untuk mengamankan kata sandi yang paling penting: contohnya, menyimpan Seedkeeper Anda di dua lokasi yang berbeda untuk membatasi risiko fisik, atau menitipkan salinannya kepada kerabat yang terpercaya.



Untuk melakukan ini, bawalah Seedkeeper kedua Anda (ingatlah untuk mengidentifikasi salah satu dari keduanya dengan tanda untuk menghindari kebingungan). Mulailah dengan menginisialisasinya, seperti yang dijelaskan pada langkah 3 tutorial ini. Sekali lagi, pilihlah kode PIN yang kuat. Tergantung pada strategi Anda, Anda bisa memilih PIN yang berbeda atau tetap menggunakan PIN yang sama.



![Image](assets/fr/023.webp)



Buka aplikasi, klik "*Klik & Pindai*", masukkan PIN Seedkeeper n°1 (sumber) Anda, lalu pindai.



![Image](assets/fr/024.webp)



Ini akan membawa Anda ke halaman beranda, dengan daftar rahasia Anda. Klik pada tiga titik kecil di bagian kanan atas antarmuka.



![Image](assets/fr/025.webp)



Pilih "*Buat cadangan*", lalu tekan "*Mulai*".



![Image](assets/fr/026.webp)



Masukkan kode PIN kartu cadangan Anda (Seedkeeper no. 2).



![Image](assets/fr/027.webp)



Kemudian pindai kartu.



![Image](assets/fr/028.webp)



Lakukan hal yang sama dengan kartu utama (Seedkeeper no. 1), lalu klik "*Buat cadangan*".



![Image](assets/fr/029.webp)



Seedkeeper n°2 Anda sekarang berisi semua rahasia yang tersimpan di Seedkeeper n°1.



![Image](assets/fr/030.webp)



Anda dapat memindai Seedkeeper n°2 Anda untuk memeriksa apakah rahasia telah disalin.



![Image](assets/fr/031.webp)



Hanya itu saja yang bisa dilakukan! Sekarang Anda sudah mengetahui cara menggunakan Seedkeeper untuk menyimpan kata sandi Anda. Di tutorial selanjutnya, kita akan melihat bagaimana cara menggunakan Seedkeeper untuk mencadangkan Bitcoin wallet. Saya juga mengundang Anda untuk menemukan penggunaan gabungannya dengan SeedSigner :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356