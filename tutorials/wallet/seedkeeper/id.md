---
name: Penangkar benih
description: Bagaimana cara mencadangkan wallet Bitcoin saya dengan kartu pintar Seedkeeper?
---

![cover](assets/cover.webp)



Seedkeeper adalah kartu pintar yang dikembangkan oleh Satochip, sebuah perusahaan Belgia yang berspesialisasi dalam solusi perangkat keras untuk mengelola dan melindungi rahasia digital. Terkenal dengan rangkaian kartu pintarnya untuk ekosistem Bitcoin, Satochip mendesain Seedkeeper sebagai alternatif dari metode tradisional untuk menyimpan frasa mnemonik.



Secara konkret, Seedkeeper berbentuk kartu pintar bersertifikasi EAL6 yang multifungsi dengan prosesor yang aman dan memori anti perusakan (yang disebut "Secure Element"). Seperti namanya, perannya adalah untuk menyimpan mnemonik dan kata sandi Bitcoin wallet secara terenkripsi dan terlindungi. Dengan Seedkeeper, Anda dapat generate, mengimpor, mengatur, dan menyimpan rahasia Anda secara langsung di dalam komponen kartu yang aman.



Menurut pendapat saya, Seedkeeper memiliki dua kegunaan utama, yang akan kita bahas dalam 2 tutorial terpisah:




- Penyimpanan frasa mnemonik Bitcoin**: alih-alih menuliskan 12 atau 24 kata di atas kertas, Anda dapat mengimpornya ke dalam kartu pintar dan melindunginya dengan kode PIN.
- Manajemen kata sandi**: Anda dapat membuat kata sandi yang kuat melalui aplikasi Seedkeeper dan menyimpannya langsung di dalam kartu pintar, memberikan Anda pengelola kata sandi offline yang nyaman dan mudah digunakan.



Secara teknis, Seedkeeper memiliki kapasitas 8192 byte, memungkinkannya untuk menyimpan minimal 50 rahasia yang terpisah (jumlah yang tepat akan tergantung pada ukuran dan metadata yang terkait dengan masing-masing rahasia). Seedkeeper dapat diakses baik [melalui pembaca kartu pintar yang terhubung](https://satochip.io/accessories/) ke komputer, atau melalui aplikasi seluler dengan koneksi NFC. Seluruh sistem beroperasi dalam mode offline, tanpa koneksi internet, menjamin permukaan serangan yang terbatas.



![Image](assets/fr/001.webp)



Fitur yang sangat menarik adalah kemampuan untuk menduplikasi konten dari satu Seedkeeper ke Seedkeeper lainnya untuk membuat cadangan. Dalam tutorial ini, kami akan menunjukkan kepada Anda cara melakukannya.



Seedkeeper juga sangat menarik jika digabungkan dengan perangkat keras tanpa kewarganegaraan wallet seperti SeedSigner atau Specter DIY. Dalam hal ini, tidak perlu menggunakan klien Satochip pada komputer atau ponsel. Seedkeeper menyimpan seed di dalam secure element dan dapat digunakan secara langsung dengan perangkat penandatanganan, sehingga tidak memerlukan kode QR kertas. Saya tidak akan mengembangkan kasus penggunaan khusus ini dalam tutorial ini, karena ini adalah subjek dari tutorial khusus lainnya:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1. Apa kasus penggunaan untuk Seedkeeper?



Dalam tutorial ini, saya hanya akan membahas kasus penggunaan yang terkait dengan Bitcoin, karena itulah tujuan dari tutorial ini. Kita tidak akan membahas fungsionalitas manajemen kata sandi, yang akan menjadi topik tutorial lain.



Dibandingkan dengan cadangan kertas sederhana dari frasa mnemonik, menggunakan Seedkeeper memiliki beberapa keuntungan:





- Tahan pencurian:** seed dalam wallet Anda tidak dapat diakses dalam bentuk teks yang jelas. Untuk mengekstraknya, Anda perlu mengetahui PIN Seedkeeper. Pencuri yang mendapatkan perangkat tidak akan dapat melakukan apa pun tanpa kode ini.





- Menyebarkan risiko pada dua faktor:** Anda dapat membagi keamanan antara faktor digital dan faktor fisik. Sebagai contoh, jika Anda menyimpan PIN Seedkeeper di dalam pengelola kata sandi Anda, Anda akan membutuhkan akses ke pengelola ini dan kepemilikan fisik smartcard untuk mendapatkan seed (kemungkinan serangan yang jauh lebih kecil).





- Manajemen terpusat:** Seedkeeper memfasilitasi pengelolaan beberapa benih dari portofolio yang berbeda.





- Pencadangan yang mudah:** cukup dengan menduplikasi cadangan terenkripsi ke SeedKeeper lain.



Namun demikian, ada sejumlah kelemahan dibandingkan dengan cadangan kertas sederhana dari seed Anda:





- Harga:** meskipun tidak mahal (sekitar €25), namun masih lebih tinggi daripada harga selembar kertas.





- Ketergantungan pada perangkat komputasi serba guna:** Memasuki dan mengelola seed membutuhkan komputer atau ponsel pintar, yang berarti bahwa mnemonik Anda melewati mesin dengan permukaan serangan yang jauh lebih luas daripada perangkat keras wallet. Hal ini dapat menimbulkan risiko jika mesin tersebut disusupi. Inilah mengapa saya tidak menyarankan penggunaan Seedkeeper untuk menyimpan seed dari perangkat keras wallet (kecuali pada penggunaan tanpa komputer, seperti pada SeedSigner). Peran perangkat keras wallet justru untuk menyimpan seed dalam lingkungan yang minimalis dan sangat aman. Dengan memasukkan seed secara manual ke komputer biasa, seed tidak lagi terbatas pada perangkat keras wallet: seed juga akan berakhir di mesin umum, yang terpapar oleh banyak vektor serangan. Jadi, lebih baik menggunakan Seedkeeper untuk wallet yang panas daripada yang dingin (kecuali perangkat keras SeedSigner / wallet tanpa kewarganegaraan).





- Risiko kehilangan yang terkait dengan PIN:** Ketidakmampuan mengakses langsung seed, tidak seperti cadangan kertas, memang memberikan perlindungan terhadap pencurian fisik. Namun seperti biasa, keamanan adalah tindakan menyeimbangkan antara risiko pencurian dan risiko kehilangan. Jika cadangan Anda memerlukan PIN, hilangnya kode ini akan membuat Anda tidak dapat memulihkan frasa mnemonik Anda, dan dengan demikian mengakses bitcoin Anda.



Dengan mempertimbangkan kelebihan dan kekurangan ini, saya menganggap bahwa penggunaan terbaik untuk Seedkeeper (terlepas dari fungsi pengelola kata sandinya) adalah, di satu sisi, menyimpan seed dari **portofolio perangkat lunak** Anda, karena sudah ada di ponsel atau komputer Anda, atau dari perangkat keras wallet tanpa layar Anda seperti Satochip, dan di sisi lain, menggunakannya dalam kombinasi dengan perangkat keras wallet tanpa nama seperti SeedSigner, yang benar-benar menjadi miliknya.



Kasus penggunaan lain yang sangat menarik untuk Seedkeeper adalah kemungkinan untuk mencadangkan *Descriptor* portofolio Anda dengan aman dan andal.



## 2. Bagaimana cara mendapatkan Seedkeeper?



Ada dua cara utama untuk mendapatkan Seedkeeper. Anda dapat [membelinya langsung dari toko resmi Satochip](https://satochip.io/product/seedkeeper/) atau dari pengecer resmi. Tetapi karena [applet Seedkeeper adalah sumber terbuka] (https://github.com/Toporin/Seedkeeper-Applet), Anda juga memiliki pilihan untuk menginstalnya sendiri pada [kartu pintar kosong] (https://satochip.io/product/blank-javacard-for-diy-project/).



Jika Anda ingin menggunakan fungsionalitas pencadangan Seedkeeper, Anda tentu saja perlu membeli dua kartu pintar.



## 3. Menginstal klien Seedkeeper



Dalam tutorial ini, kita akan mencadangkan portofolio seed kita di Seedkeeper. Langkah pertama adalah menginstal perangkat lunak pada komputer atau ponsel pintar Anda. Pada PC, Anda harus [mengunduh versi terbaru Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). Di ponsel, aplikasi Seedkeeper tersedia di [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) dan juga di [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 4. Inisialisasi pemilik benih



Luncurkan aplikasi dan klik tombol "*Klik & Pindai*".



![Image](assets/fr/003.webp)



Anda akan diminta kode PIN untuk Seedkeeper Anda. Karena ini adalah kartu baru, belum ada PIN yang ditentukan. Masukkan kode apa pun untuk melewati langkah ini, lalu klik "*Next*".



![Image](assets/fr/004.webp)



Kemudian letakkan kartu di bagian belakang ponsel cerdas Anda. Aplikasi akan mendeteksi bahwa Seedkeeper belum diinisialisasi, dan akan meminta Anda untuk mengatur kode PIN kartu pintar Anda, antara 4 hingga 16 karakter. Untuk keamanan optimal, pilihlah kata sandi yang kuat yang panjang, acak, dan terdiri dari berbagai macam karakter. Kode PIN ini adalah satu-satunya penghalang terhadap akses fisik ke frasa pemulihan Anda.



**Ingatlah juga untuk menyimpan PIN ini sekarang juga**, contohnya di dalam pengelola kata sandi, atau di media fisik yang terpisah. Dalam kasus terakhir, jangan pernah menyimpan media yang berisi PIN di tempat yang sama dengan Seedkeeper Anda, jika tidak, keamanan ini tidak akan berguna. Penting untuk memiliki cadangan yang dapat diandalkan: tanpa PIN, Anda tidak akan dapat memulihkan rahasia yang tersimpan di Seedkeeper.



![Image](assets/fr/005.webp)



Konfirmasikan kode PIN Anda untuk kedua kalinya.



![Image](assets/fr/006.webp)



Seedkeeper Anda sekarang telah diinisialisasi. Anda dapat membukanya dengan memasukkan kode PIN yang baru saja Anda tetapkan.



![Image](assets/fr/007.webp)



Sekarang Anda akan dibawa ke halaman manajemen kartu pintar Anda.



![Image](assets/fr/008.webp)



## 5. Daftarkan seed di Seedkeeper



Setelah Seedkeeper Anda terbuka, klik tombol "*+*".



![Image](assets/fr/009.webp)



Pilih "Impor rahasia*". Opsi "*Generate secret*" memungkinkan Anda membuat frasa mnemonik baru secara langsung dari dalam aplikasi.



![Image](assets/fr/010.webp)



Dalam kasus kami, kami ingin menyimpan seed dalam portofolio kami. Klik pada "*Mnemonic*".



![Image](assets/fr/011.webp)



Tetapkan "*Label*" pada rahasia ini agar dapat dengan mudah diidentifikasi jika Anda menyimpan beberapa informasi di Seedkeeper Anda.



![Image](assets/fr/012.webp)



Kemudian masukkan frasa pemulihan Anda di bidang yang tersedia. Jika mau, Anda juga dapat menambahkan passphrase BIP39 atau *Descriptor* Anda. Kemudian klik "Impor*".



![Image](assets/fr/013.webp)



*Mnemonik yang ditampilkan dalam gambar ini adalah fiktif dan bukan milik siapa pun. Ini hanya sebuah contoh. Jangan pernah mengungkapkan mnemonik Anda kepada siapa pun, atau bitcoin Anda akan dicuri



Tempatkan Seedkeeper Anda di bagian belakang ponsel cerdas Anda.



![Image](assets/fr/014.webp)



seed Anda telah terdaftar.



![Image](assets/fr/015.webp)



## 6. Akses seed Anda di Seedkeeper



Jika Anda ingin memeriksa frasa mnemonik Anda, ambil Seedkeeper Anda dan klik tombol "*Klik & Pindai*".



![Image](assets/fr/016.webp)



Masukkan kode PIN Anda, lalu tekan "*Next*".



![Image](assets/fr/017.webp)



Tempatkan Seedkeeper Anda di bagian belakang ponsel cerdas Anda.



![Image](assets/fr/018.webp)



Ini akan membawa Anda ke daftar semua rahasia Anda yang terdaftar. Dalam contoh ini, saya ingin menampilkan seed dari portofolio "*Blockstream App*" saya, jadi saya klik di atasnya.



![Image](assets/fr/019.webp)



Tekan tombol "*Mengungkapkan*".



![Image](assets/fr/020.webp)



Pindai kembali Seedkeeper Anda.



![Image](assets/fr/021.webp)



Frasa mnemonik yang Anda rekam sebelumnya, sekarang ditampilkan di layar.



![Image](assets/fr/022.webp)



## 7. Mencadangkan Penyimpanan Benih



Sekarang kita akan membuat cadangan Seedkeeper saya di Seedkeeper kedua sehingga memiliki dua salinan. Redundansi ini dapat menjadi bagian dari strategi untuk mengamankan bitcoin Anda: misalnya, menyimpan frasa Anda di dua lokasi terpisah untuk membatasi risiko fisik, atau menitipkan salinannya kepada kerabat yang dipercaya sebagai bagian dari rencana warisan.



Untuk melakukan ini, bawalah Seedkeeper kedua Anda (ingatlah untuk mengidentifikasi salah satu dari keduanya dengan tanda untuk menghindari kebingungan). Mulailah dengan menginisialisasinya, seperti yang dijelaskan pada langkah 4 tutorial ini. Pilih kata sandi yang kuat sekali lagi. Tergantung pada strategi Anda, Anda dapat memilih kata sandi yang berbeda atau menggunakan kata sandi yang sama.



![Image](assets/fr/023.webp)



Buka aplikasi, klik "*Klik & Pindai*", masukkan kata sandi Seedkeeper n°1 (sumber) Anda, lalu pindai.



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



Hanya itu saja yang bisa dilakukan! Sekarang Anda sudah tahu cara menggunakan Seedkeeper untuk menyimpan frasa mnemonik Bitcoin wallet. Dalam tutorial selanjutnya, kita akan melihat bagaimana cara menggunakan Seedkeeper untuk menyimpan kata sandi Anda. Saya juga mengundang anda untuk menemukan penggunaan gabungannya dengan SeedSigner:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

Dalam tutorial ini, kami telah menyebutkan ***Descriptor*** dalam portofolio Bitcoin Anda beberapa kali. Tidak tahu apa itu? Kalau begitu, saya sarankan Anda mengikuti kursus pelatihan CYP 201 gratis kami, yang membahas secara mendalam semua mekanisme yang terlibat dalam mengoperasikan portofolio HD!



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f